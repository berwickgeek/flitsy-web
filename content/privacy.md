---
title: "Privacy Policy"
subtitle: "Effective 16 May 2026"
lastmod: 2026-05-16
description: "How Flitsy collects, uses, and protects your data."
---

This is the privacy policy for Flitsy CRM ("Flitsy", "we", "us").
We try to keep it short and in plain English. If anything below is
unclear, email us at [j@jaym.cc](mailto:j@jaym.cc) and we'll explain.

## Who we are

Flitsy is operated by **The Trustee for the Aly Boo Family Trust**
(ABN 70 204 274 606), trading as Flitsy, at 1 Latitude Blvd,
Nikenbah QLD 4655, Australia.

## What Flitsy is

Flitsy is a CRM you control through an AI assistant (such as Claude,
ChatGPT, or any MCP-compatible client) instead of a web app. You add
Flitsy as a connector in your chosen assistant; the assistant calls
Flitsy's tools on your behalf to read and update your CRM data.

## What we collect

We only collect what's needed to run your CRM.

**Account info.** Your email address and name, via WorkOS when you
sign in. That's it for identity.

**Your CRM data.** Whatever you put in: organisations, people,
interactions, notes, tasks, attachments, settings. You own it. We
store it on your behalf.

**Email content, when you connect a mailbox.** If you connect Gmail
or Outlook to send mail through Flitsy, we store an encrypted refresh
token so we can send on your behalf, plus the headers and body of
messages sent through Flitsy (so they appear as interactions in your
CRM). We do not read other messages in your inbox.

**Inbound email, when you forward it to your dataset address.** If
you set up email forwarding into Flitsy, the messages you forward are
stored as interactions.

**Operational logs.** Standard server logs (request paths, status
codes, timestamps, IP addresses) for security and debugging. We do
not run analytics, session replay, or any third-party tracking on
our pages.

## How we use it

To run your CRM. That's the entire list. We don't sell your data,
we don't share it with advertisers, and we don't use it to train
anyone's AI models.

## Google user data — Limited Use disclosure

Flitsy's use and transfer to any other app of information received
from Google APIs will adhere to the
[Google API Services User Data Policy](https://developers.google.com/terms/api-services-user-data-policy),
including the Limited Use requirements.

In plain terms: when you connect Gmail, we only use the access to
send email you've asked us to send, and to record those sends in
your CRM as interactions. We do not read other messages, we do not
share Gmail data with third parties except as needed to perform the
send (i.e. Google itself), and we do not use Gmail data to train
machine-learning models — ours or anyone else's.

## Who we share data with

Flitsy uses a small set of trusted services to run. Each one only
sees what it needs to do its job:

- **Railway** (Singapore) — hosts the Flitsy app and Postgres database.
- **WorkOS** — handles sign-in.
- **Cohere** (US/Canada) — generates semantic-search embeddings of
  your notes and interaction content (including any email content
  saved as interactions). Cohere does not store or train on the
  content we send.
- **Google** (when you connect Gmail) — receives the emails you send
  through Flitsy.
- **Microsoft** (when you connect a Microsoft 365 mailbox) — same as
  above, for Outlook.
- **Amazon Web Services** — receives inbound email forwarded to your
  Flitsy dataset address, and stores attachments.

Your AI assistant (e.g. Claude, ChatGPT, or another MCP client you
connect) sees the CRM data its tool calls return. That data flows
through the assistant's provider in the normal course of your
conversation; how they handle it is governed by their own privacy
policy. Pick an assistant you trust.

## Can a human at Flitsy see my data?

Only with your permission, and only when you ask us for support and
agree we should look. We don't read your data routinely. Our access
to support-investigate is logged.

## Where data lives

Your data is stored in Postgres on Railway, currently in Singapore.
Backups are kept for up to 30 days.

## Security

- Sign-in tokens and OAuth refresh tokens are encrypted at rest in
  the database (pgcrypto).
- All traffic to and from Flitsy uses TLS.
- The app runs in a tenant-isolated environment on Railway.

We're a small operation. We follow sensible practices but we're not
going to pretend we have a SOC 2 report. If you need one, we're not
the right fit yet.

## Deleting your data

You can delete your Flitsy account at any time by emailing
[j@jaym.cc](mailto:j@jaym.cc). When you do:

- Your data is removed from the live database immediately.
- It disappears from Railway backups within 30 days as old backups
  roll off.

You can also disconnect Gmail or Outlook from Flitsy at any time;
that revokes our access and removes the stored refresh token. You
can also revoke our access directly in your
[Google Account](https://myaccount.google.com/permissions) or
[Microsoft Account](https://account.microsoft.com/privacy/app-access).

## Your rights

You can ask us to:

- Show you what data we hold about you
- Correct anything that's wrong
- Delete it

Email [j@jaym.cc](mailto:j@jaym.cc) and we'll respond within 30 days.

If you're in the EU/UK, GDPR gives you these rights formally. If
you're in California, CCPA does. If you're in Australia, the
Australian Privacy Principles do. We handle requests the same way
regardless of where you are.

If you're unhappy with how we've handled a privacy issue, you can
complain to the Office of the Australian Information Commissioner
([oaic.gov.au](https://www.oaic.gov.au/)) or your local data
protection authority.

## Kids

Flitsy is for adults running a CRM at work. We don't knowingly
collect data from anyone under 16. If you think a child has signed
up, email us and we'll delete the account.

## Changes to this policy

If we change anything material, we'll email the address on your
account at least 14 days before it takes effect. Smaller wording
fixes get a quiet update with a new "Effective" date at the top.

## Contact

Privacy questions, deletion requests, anything else:
[j@jaym.cc](mailto:j@jaym.cc)
