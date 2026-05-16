# Pricing model — spec for the marketing page

This document is the source-of-truth for the public pricing story on flitsy.app. It is **not** a rendered page — use it to regenerate `content/pricing.md` and `layouts/_default/pricing.html` so they reflect what the product actually does.

Last updated: 2026-05-16.

---

## TL;DR

| | Free | Pro |
|---|---|---|
| **Price** | $0 | $19 USD / month |
| **Users** | 1 owner + 1 other (2 total) | 2 included, then $19 USD / extra seat / month |
| **Records (orgs + people)** | 6,000 max | unlimited |
| **External tools** (email send, forms, tracking, enrichment, inbox sync) | — | yes |
| **Note search** | keyword (FTS) only | semantic + keyword (hybrid) |
| **Billing** | n/a | monthly only |
| **Trial** | none — Free is the on-ramp | — |

Upgrade lives at **`my.flitsy.app/upgrade`**.

---

## The model in detail

### One owner, one account, one dataset

Each Flitsy account has a single human owner and a single shared dataset. Other users (admins or members) can be invited as seats on the same account; they share the dataset. Pricing therefore attaches to the **account**, never to the dataset.

### What's gated to Pro

Three independent triggers — hit any one and the account needs Pro:

1. **Adding a 3rd user.** Free supports 1 owner + 1 other. The act of inviting seat #3 fires the gate.
2. **Hitting 6,001 records.** Combined organisation + people count, per account. Upsert refuses when it would push you over.
3. **Calling an external-facing tool.** Sending email, sending SMS, generating quotes, public forms, link/open tracking, inbox sync, contact enrichment.

A fourth, softer gate is **note embeddings + semantic search**. On Free, notes are stored but not embedded — `search_notes` falls back to Postgres full-text. The result is still useful; it just won't find "the conversation about the broken aircon" unless your note literally says "broken aircon." Pro turns on the embedding pipeline (Cohere `embed-v4.0`) and the hybrid ranker. This isn't a refusal — it's a silent capability difference.

### Pro pricing structure

- **$19 USD / month base.** Includes seats 1–2 (so an upgrading solo or pair pays the base only).
- **+$19 USD / month per extra seat**, starting at seat 3.

Worked examples:

| Account | Monthly |
|---|---|
| Solo on Pro | $19 |
| 2-user team on Pro | $19 |
| 3-user team | $38 |
| 5-user team | $76 |
| 10-user team | $171 |

### Currency and billing

- **Customer-facing currency: USD.** Stripe products configured with `presentment_currency=USD`.
- The Stripe account itself settles in AUD; expect a ~2% FX shave on conversion. (This is a Stripe config detail, not a customer-visible concern.)
- **Monthly only.** No annual discount, no "pay yearly save 20%" — purely cadence simplicity for launch. We can revisit later if customers ask.
- **No trial.** Free is the on-ramp. A prospect can use the product indefinitely under the Free caps to evaluate.

---

## Positioning

Flitsy is conceptually a CRM and positioned in the **modern CRM category** for marketing clarity. Comparison anchors:

| | Approx entry price | Approx Pro price |
|---|---|---|
| Salesforce / HubSpot | $25–80/seat | $80–165/seat |
| Attio | ~$34/seat | ~$59/seat |
| Folk | ~$20/seat | ~$40/seat |
| Streak (Gmail-native) | ~$19/seat | ~$59/seat |
| **Flitsy** | **$0** | **$19/seat-equivalent** |

The truthful read is that Flitsy's *actual* competitor is "doing nothing" — solo founders, consultants, and small teams using a mix of inbox + spreadsheet + memory. Marketing should anchor against the CRM category (prospect knows what that is) while the product story emphasises "no UI to maintain — your CRM lives in Claude."

What flitsy is not:
- Not a sales-rep CRM (no rep dashboards, no quota tracking).
- Not an AI sales agent (no autonomous outbound).
- Not a generic database (it has CRM-specific intent: organisations, people, interactions, follow-ups, deals).

---

## What's stale in the current `layouts/_default/pricing.html`

The hardcoded layout file pre-dates these decisions. To rebuild the page, the following must change:

| Hardcoded today | Should be |
|---|---|
| "Up to 50 organisations & people" | Up to 6,000 |
| "30-day data retention" | Drop entirely — no retention limit on Free |
| "Connect any one MCP client / Unlimited" | Drop — not a constraint we apply |
| "Team members: 1" on Free | 2 (1 owner + 1 other) |
| "$19 / user / month" implying per-seat from seat 1 | $19 base covers 2 seats; +$19 per extra seat from #3 |
| "20% annual discount" FAQ | Remove — monthly only |
| "Email forwarding to `cr-…@flitsy.app`" | Use the new inbound domain (TBC — moving to `.c.app`) |
| "Deal pipeline: View-only on Free, Full kanban on Pro" | Not a tier distinction — both tiers get deal management; Pro adds external surfaces |
| "Smart views: Pro only" | Re-check against `tools.yaml` — most smart views (`next_best_action`, `weekly_digest`, `plan_my_week`, `get_followups_due`) are `tier: free` and should stay that way |
| "30-day refund, no questions" | Not decided — leave or remove pending call |

---

## Suggested FAQ for the page

- **What counts as a "user"?** A human with a login. An AI client (Claude, Cursor, ChatGPT) connecting on behalf of that human is part of their seat — the seat travels with the person, not the device.
- **How long is Free actually free?** Forever, under the caps. There's no countdown.
- **What happens if I hit the record cap on Free?** Reads and existing data stay accessible; the next `upsert` refuses with an upgrade link.
- **What happens if I downgrade after using Pro?** Existing data over the cap stays read-only (visible, not deletable, not editable) until you prune or re-upgrade. No silent data loss.
- **Can I add a 3rd seat without upgrading?** No — adding a 3rd seat is itself the upgrade trigger.
- **Does my search just get worse on Free?** Yes, honestly — it falls back to keyword. Still useful, not magic. Pro turns on semantic.
- **Annual billing?** Monthly only at launch.
- **Refunds?** [Decision pending.]

---

## Implementation status

The pricing model is **decided**; the enforcement code is **in progress**. See [berwickgeek/flitsy-crm](https://github.com/berwickgeek/flitsy-crm) issue tracker for the implementation tasks (cap enforcement, seat gate, plan column on accounts, Stripe wiring, `/upgrade` page).

Don't publish the new pricing page until the upgrade flow works end-to-end — the page is the contract.
