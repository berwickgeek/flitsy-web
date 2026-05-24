#!/usr/bin/env python3
"""Thin authenticated client for the Reddit Ads API.

Reads credentials written by reddit-auth.py, exchanges the stored refresh token
for a short-lived access token, and makes a request against the Ads API.

Usage:
    ./reddit-api.py GET /api/v3/me
    ./reddit-api.py GET /api/v3/ad_accounts/<account_id>/campaigns
    ./reddit-api.py POST /api/v3/ad_accounts/<account_id>/campaigns '{"data": {...}}'

Access tokens last ~1 hour; this script mints a fresh one each run, so there's
no token caching to worry about for ad-hoc calls.
"""

import base64
import json
import sys
import urllib.error
import urllib.parse
import urllib.request
from pathlib import Path

TOKEN_URL = "https://www.reddit.com/api/v1/access_token"
ADS_API_BASE = "https://ads-api.reddit.com"
USER_AGENT = "flitsy-ads-cli/1.0 (by /u/flitsy_app)"
CREDS_PATH = Path.home() / ".config" / "reddit-ads" / "credentials.json"


def load_creds():
    if not CREDS_PATH.exists():
        sys.exit(f"No credentials at {CREDS_PATH}. Run ./reddit-auth.py first.")
    return json.loads(CREDS_PATH.read_text())


def get_access_token(creds):
    data = urllib.parse.urlencode({
        "grant_type": "refresh_token",
        "refresh_token": creds["refresh_token"],
    }).encode()
    auth = base64.b64encode(f"{creds['client_id']}:{creds['client_secret']}".encode()).decode()
    req = urllib.request.Request(TOKEN_URL, data=data, method="POST")
    req.add_header("Authorization", f"Basic {auth}")
    req.add_header("User-Agent", USER_AGENT)
    with urllib.request.urlopen(req) as resp:
        return json.load(resp)["access_token"]


def call(method, path, body, token):
    url = path if path.startswith("http") else ADS_API_BASE + path
    payload = body.encode() if body else None
    req = urllib.request.Request(url, data=payload, method=method.upper())
    req.add_header("Authorization", f"Bearer {token}")
    req.add_header("User-Agent", USER_AGENT)
    if payload:
        req.add_header("Content-Type", "application/json")
    try:
        with urllib.request.urlopen(req) as resp:
            return resp.status, resp.read().decode()
    except urllib.error.HTTPError as e:
        return e.code, e.read().decode()


def main():
    if len(sys.argv) < 3:
        sys.exit("Usage: ./reddit-api.py <METHOD> <PATH> [JSON_BODY]")
    method, path = sys.argv[1], sys.argv[2]
    body = sys.argv[3] if len(sys.argv) > 3 else None

    creds = load_creds()
    token = get_access_token(creds)
    status, text = call(method, path, body, token)
    print(f"HTTP {status}")
    try:
        print(json.dumps(json.loads(text), indent=2))
    except json.JSONDecodeError:
        print(text)


if __name__ == "__main__":
    main()
