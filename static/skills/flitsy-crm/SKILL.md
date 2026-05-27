---
name: flitsy-crm
description: Use the Flitsy CRM through MCP tools. Drives sensible defaults across ~130 tools (browse contacts, review inbox, draft outreach in the user's voice, log interactions, manage deals, plan the week). Use whenever the user asks to check their CRM, look up an org or person, review who's waiting on a reply, draft a follow-up, log a call, move a deal, or plan outreach against their Flitsy dataset.
when_to_use: User says "check my CRM", "who needs a reply", "draft a follow-up to <name>", "log this call", "what's on for this week", "where are we with <org>", "find <person/org>", or otherwise references their contacts, deals, inbox, or outreach pipeline.
---

# Flitsy CRM

Flitsy is MCP-first. **There is no end-user dashboard** — only these tools and a thin `/admin` page for dataset administration. If a capability isn't a tool, say so plainly. Never tell the user to "log into the CRM" or "open the dashboard."

## Orient before guessing

If you're unsure which tool fits, call `get_help()` or read `crm://help`. Tools are grouped by intent: orient, browse_search, stay_on_top, capture, plan_ahead, reach_out, build_pipeline, understand_relationships, bring_in_prospects, curate_data, customize, manage_team, connect_services, stay_alerted, reflect, automate, manage_workspace.

## Default workflows

**"What needs my attention?"** → combine `next_best_action`, `get_followups_due`, `get_overdue_tasks`, `get_inbound_awaiting_reply`. Return a short ranked list, not raw tool dumps.

**"Catch me up on <org>"** → `get_organisation` for facts, `get_org_timeline` for activity, `search_notes` for context. Lead with last interaction date and any open task.

**"Draft a follow-up to <person>"** → `draft_message` returns the recent thread plus the dataset's voice/signature facts in one call. Compose from that — do not invent a new tone. Show the draft for approval; only call `send_email` after the user says yes.

**"Log this call/meeting"** → `log_interaction` with type, body, and the person/org. Don't create a task as a side effect unless asked.

**"Plan my week" / "What happened this week?"** → `plan_my_week`, `weekly_digest`. Both return structured ranked output meant for direct rendering — don't re-aggregate.

**Capture a new contact** → `upsert_person` (auto-resolves the org via email domain). Prefer over creating org + person separately.

## Email voice

The dataset stores the user's voice/persona/signature as facts; `draft_message` surfaces them. If those facts are missing, run the `setup_voice` prompt rather than guessing — a generic "professional" tone is wrong by default.

## Inbound mail

There is no Gmail/Outlook OAuth read sync (intentionally out of scope). Users forward into their dataset's `cr-<token>@in.flitsy.app` address. Show that address with `get_inbound_email` when the user asks how to get email into the CRM.

## Tier gates

Some tools are Pro-only; Scale tier has no purchase path. If a call returns a tier-gate error, surface it — don't retry or work around. Point the user at their Polar billing portal to upgrade.

## Avoid

- Suggesting a dashboard, settings page, or "logging in" — none exist for end users.
- Exposing raw UUIDs in user-facing text — use human-readable names; pass UUIDs back into tool calls.
- Manual fan-out where a digest tool already aggregates (`weekly_digest`, `pipeline_summary`, `plan_my_week`).
- Calling `send_email` without explicit user approval of the draft.

## Resources to attach

- `crm://help` — full tool list grouped by intent
- `crm://config` — dataset config (statuses, interaction types, voice facts)
- `crm://digest/today`, `crm://digest/week`
- `crm://org/<external_id_or_uuid>`
- Prompts: `morning_review`, `weekly_review`, `draft_followup`, `triage_unmatched_senders`, `org_brief`, `setup_voice`, `find_warm_intro`, `whats_possible`
