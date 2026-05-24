#!/usr/bin/env python3
"""One-time OAuth2 authorization for the Reddit Ads API.

Spins up a temporary localhost server, opens Reddit's consent screen in your
browser, captures the returned authorization code, and exchanges it for a
permanent refresh token. The refresh token + client credentials are written to
~/.config/reddit-ads/credentials.json (mode 0600) so reddit-api.py can mint
fresh access tokens indefinitely without you re-authorizing.

Usage:
    ./reddit-auth.py
    # ...or feed creds via env to skip the prompts:
    REDDIT_CLIENT_ID=xxx REDDIT_CLIENT_SECRET=yyy ./reddit-auth.py

Before running, register an app at https://www.reddit.com/prefs/apps:
  - type:          "web app"
  - redirect uri:  http://localhost:8080/callback   (must match REDIRECT_URI)
"""

import base64
import http.server
import json
import os
import secrets
import sys
import urllib.parse
import urllib.request
import webbrowser
from pathlib import Path

PORT = 8080
REDIRECT_URI = f"http://localhost:{PORT}/callback"
# Full campaign management: read reporting + create/edit campaigns + conversions.
# `identity` lets us confirm which Reddit account authorized.
SCOPES = "identity adsread adsedit adsconversions"
AUTHORIZE_URL = "https://www.reddit.com/api/v1/authorize"
TOKEN_URL = "https://www.reddit.com/api/v1/access_token"
USER_AGENT = "flitsy-ads-cli/1.0 (by /u/flitsy_app)"

CONFIG_DIR = Path.home() / ".config" / "reddit-ads"
CREDS_PATH = CONFIG_DIR / "credentials.json"

# Filled in by the callback handler, read by the main flow.
_result = {}


class CallbackHandler(http.server.BaseHTTPRequestHandler):
    def do_GET(self):
        parsed = urllib.parse.urlparse(self.path)
        if parsed.path != "/callback":
            self.send_response(404)
            self.end_headers()
            return
        params = urllib.parse.parse_qs(parsed.query)
        _result["code"] = params.get("code", [None])[0]
        _result["state"] = params.get("state", [None])[0]
        _result["error"] = params.get("error", [None])[0]

        self.send_response(200)
        self.send_header("Content-Type", "text/html; charset=utf-8")
        self.end_headers()
        if _result["error"]:
            body = f"<h2>Authorization failed: {_result['error']}</h2>"
        else:
            body = "<h2>Flitsy &times; Reddit Ads authorized.</h2><p>You can close this tab and return to the terminal.</p>"
        self.wfile.write(f"<html><body style='font-family:system-ui;padding:3rem'>{body}</body></html>".encode())

    def log_message(self, format, *args):
        pass  # quiet


def exchange_code(client_id, client_secret, code):
    data = urllib.parse.urlencode({
        "grant_type": "authorization_code",
        "code": code,
        "redirect_uri": REDIRECT_URI,
    }).encode()
    auth = base64.b64encode(f"{client_id}:{client_secret}".encode()).decode()
    req = urllib.request.Request(TOKEN_URL, data=data, method="POST")
    req.add_header("Authorization", f"Basic {auth}")
    req.add_header("User-Agent", USER_AGENT)
    req.add_header("Content-Type", "application/x-www-form-urlencoded")
    with urllib.request.urlopen(req) as resp:
        return json.load(resp)


def main():
    client_id = os.environ.get("REDDIT_CLIENT_ID") or input("Reddit app client_id: ").strip()
    client_secret = os.environ.get("REDDIT_CLIENT_SECRET") or input("Reddit app client_secret: ").strip()
    if not client_id or not client_secret:
        sys.exit("client_id and client_secret are required.")

    state = secrets.token_urlsafe(16)
    query = urllib.parse.urlencode({
        "client_id": client_id,
        "response_type": "code",
        "state": state,
        "redirect_uri": REDIRECT_URI,
        "duration": "permanent",  # permanent => issues a refresh_token
        "scope": SCOPES,
    })
    authorize_url = f"{AUTHORIZE_URL}?{query}"

    print(f"\nOpening Reddit consent in your browser. If it doesn't open, visit:\n{authorize_url}\n")
    print(f"Listening on {REDIRECT_URI} for the callback...\n")

    server = http.server.HTTPServer(("localhost", PORT), CallbackHandler)
    webbrowser.open(authorize_url)
    # Handle exactly one request (the callback), then stop.
    server.handle_request()
    server.server_close()

    if _result.get("error"):
        sys.exit(f"Authorization denied: {_result['error']}")
    if not _result.get("code"):
        sys.exit("No authorization code received.")
    if _result.get("state") != state:
        sys.exit("State mismatch — possible CSRF, aborting.")

    print("Code received. Exchanging for tokens...")
    tokens = exchange_code(client_id, client_secret, _result["code"])
    if "refresh_token" not in tokens:
        sys.exit(f"No refresh_token in response: {tokens}")

    CONFIG_DIR.mkdir(parents=True, exist_ok=True)
    creds = {
        "client_id": client_id,
        "client_secret": client_secret,
        "refresh_token": tokens["refresh_token"],
        "scope": tokens.get("scope", SCOPES),
    }
    CREDS_PATH.write_text(json.dumps(creds, indent=2))
    CREDS_PATH.chmod(0o600)
    print(f"\nDone. Refresh token saved to {CREDS_PATH}")
    print(f"Granted scopes: {tokens.get('scope')}")


if __name__ == "__main__":
    main()
