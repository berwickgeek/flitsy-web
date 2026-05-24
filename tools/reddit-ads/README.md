# Reddit Ads API tooling

One-time OAuth setup + a thin client for driving the Reddit Ads API, used to run
the campaign described in [`docs/reddit-ad-test-playbook.md`](../../docs/reddit-ad-test-playbook.md).

No third-party dependencies — pure Python 3 stdlib.

## Files

| File | Purpose |
|---|---|
| `reddit-auth.py` | One-time browser authorization → saves a permanent refresh token |
| `reddit-api.py`  | Mints a fresh access token from the refresh token and makes a call |

## Credentials

Secrets are **never** committed. They live in `~/.config/reddit-ads/credentials.json`
(mode `0600`), written by `reddit-auth.py`:

```json
{ "client_id": "...", "client_secret": "...", "refresh_token": "...", "scope": "..." }
```

## Setup (done once)

1. Register an app at <https://www.reddit.com/prefs/apps>:
   - type: **web app**
   - redirect uri: `http://localhost:8080/callback`
2. Run the auth flow:
   ```bash
   ./reddit-auth.py            # prompts for client_id / client_secret
   # or: REDDIT_CLIENT_ID=xxx REDDIT_CLIENT_SECRET=yyy ./reddit-auth.py
   ```
3. A browser tab opens Reddit's consent screen. Click **Allow**. The localhost
   server catches the code, swaps it for a refresh token, and saves it.

Granted scopes: `identity adsread adsedit adsconversions` (full campaign management).

## Making calls

```bash
./reddit-api.py GET /api/v3/me
./reddit-api.py GET /api/v3/ad_accounts/<account_id>/campaigns
./reddit-api.py POST /api/v3/ad_accounts/<account_id>/campaigns '{"data": {...}}'
```

Base URL is `https://ads-api.reddit.com`. Access tokens are short-lived (~1h) and
minted per call, so there's nothing to refresh manually.

## Rotating the secret

If the client secret leaks, reset it on the app's page at
<https://www.reddit.com/prefs/apps>, then re-run `./reddit-auth.py`.
