# flitsy-web

Marketing site for [flitsy.app](https://flitsy.app). Hugo static site, deployed to S3 + CloudFront.

## Local development

Requires Hugo extended (>= 0.150). Install via `brew install hugo`.

```bash
hugo server --buildDrafts
```

Open http://localhost:1313.

## Structure

```
content/        Markdown pages (privacy, terms, _index)
layouts/        Templates
  _default/
    baseof.html   Shared shell — nav, footer, head
    single.html   Doc-page layout (privacy, terms)
  index.html      Homepage — the "conversation" layout
static/         Served at site root
  css/style.css
  js/app.js
hugo.toml       Site config
```

The homepage is hand-built in `layouts/index.html` rather than driven
by content/markdown — the conversation layout is design, not copy.

## Deploy

Production: S3 + CloudFront, Route53 ALIAS at the apex.

GitHub Actions builds on push to `main`, syncs `public/` to the S3
bucket via OIDC, and invalidates the CloudFront distribution.
