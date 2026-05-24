# flitsy-web

Public marketing site for [flitsy.app](https://flitsy.app). Hugo
extended static site, deployed to S3 + CloudFront with Route53 ALIAS
at the apex.

GITHUB_REPO: berwickgeek/flitsy-web

## Sibling project: flitsy-crm

The actual product — a multi-tenant MCP-first CRM — lives in a
separate repo, **`berwickgeek/flitsy-crm`**, checked out locally at
`/Volumes/CORSAIR/Development/Projects/flitsy-crm`. FastAPI + FastMCP
+ Postgres on Railway, served on `crm.flitsy.app` today and
`my.flitsy.app` after the cutover. Marketing copy that mentions
specific MCP tools, pricing, features, or capabilities should match
the product reality there — when in doubt, check `flitsy-crm/docs/`
or the live tool list before writing claims.

The homepage design here was ported from
`flitsy-crm/flitsy_crm/static/index.html` and will be deleted from
that repo once `flitsy.app` is fully served from here.

## Stack

- Hugo extended (>= 0.150) — `brew install hugo`
- Vanilla HTML/CSS/JS — no build pipeline beyond Hugo itself
- Brand fonts: Fraunces (display), Inter (sans), IBM Plex Mono
- Hosting: S3 (`flitsy-web`, ap-southeast-2) + CloudFront
  (distribution `EBJSMK1NCVU16`) via Origin Access Control

## Structure

```
brand/              Canonical brand kit — this project OWNS these
  README.md         Brand guide notes
  Brand Guide.html  Visual reference (open in browser)
  colors.css        Drop-in CSS variables
  logos/            Mark, wordmark, lockups (SVG, animated + static)
  icons/            Favicon, apple-touch, app-icon (SVG)
  exports/          Rasterized PNGs at common sizes
content/
  _index.md         Front page (no body — design is in the template)
  privacy.md        Sourced from flitsy-crm/docs/privacy.md
  terms.md          Sourced from flitsy-crm/docs/terms.md
layouts/
  _default/
    baseof.html     Shared shell — head, nav, footer, font preload
    single.html     Doc-page layout (renders Markdown into a paper card)
  index.html        Homepage — the hand-built "conversation" layout
static/
  brand/            Web-served subset (favicons, nav logo, OG image)
  css/style.css     Extracted from the original single-file design
  js/app.js         Sticky nav, smooth scroll, animated compose placeholder
hugo.toml           Site config (baseURL, params, disableKinds)
```

`/brand/` is the canonical home for all Flitsy logo and branding
assets — they live here regardless of whether the marketing site uses
them. When grabbing assets for any other Flitsy surface (app, social,
press, decks), pull from `/brand/`. The Hugo-served subset in
`/static/brand/` is a deliberate copy — keep it in sync.

The homepage is hand-built in `layouts/index.html` rather than driven
by content/markdown — the conversation IS the design, not copy. To
add new sections, edit that template.

For new ordinary pages (e.g. `/changelog`, `/about`), drop a
`content/<page>.md` with frontmatter — `single.html` handles the
rendering.

## Local dev

```bash
hugo server --buildDrafts
```

Open <http://localhost:1313>. Live-reload covers templates, content,
CSS, and JS.

## Deploy

```bash
hugo --gc --minify
AWS_PROFILE=personal aws s3 sync public/ s3://flitsy-web/ --delete
AWS_PROFILE=personal AWS_REGION=us-east-1 aws cloudfront create-invalidation \
  --distribution-id EBJSMK1NCVU16 --paths "/*"
```

Eventually wired to a GitHub Actions workflow on push to `main` (not
built yet).

## Brand notes

- Mark is `{f|}` — lowercase f framed by curly braces with a blinking
  amber cursor. See `brand/README.md` and `brand/Brand Guide.html`
  for the canonical spec. Animated SVGs blink at 1.1s / 50% duty —
  don't change the period.
- Palette: cream `#fdf8ee`, ink `#1a1714`, amber `#d09863` (cursor /
  accent — low-saturation, NOT for primary text or large fills).
  Warm orange `--warm` stays as the user-bubble color.
- Tone is conversational and lightly self-aware ("five minutes", "we
  never see your data"), not corporate. Read the existing copy before
  writing new copy.
- The hero animation is the staggered fade-in of conversation turns
  + the typing-placeholder rotation in the compose box. If you add
  sections, keep that feel.
- **Don't use a standalone lowercase "f" in a rounded square** — it
  reads as Facebook. Use the full mark (both braces + f + cursor) or
  the wordmark.
