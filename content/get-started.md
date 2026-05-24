---
title: "Get started"
description: "Add Flitsy to your AI client in two minutes."
---

There's one Flitsy MCP URL — the same one for everyone. Paste it into
your AI client and your account is created the moment you connect.

```
https://my.flitsy.app/mcp
```

Below is how to wire it into the most common clients.

## Claude

<a class="btn btn-railway" href="https://claude.ai/customize/connectors?modal=add-custom-connector&amp;connectorName=Flitsy&amp;connectorUrl=https%3A%2F%2Fmy.flitsy.app%2Fmcp">Add Flitsy to Claude</a>

One click opens claude.ai with the name and URL already filled in. Claude will
note the connector came from a link and ask you to verify it — that's expected;
the details are Flitsy's own (`https://my.flitsy.app/mcp`). Hit **Add**,
authorize when prompted, and your account is created on first connect.

Prefer to do it by hand? Open <https://claude.ai/customize/connectors>, click
**Add custom connector**, and paste `https://my.flitsy.app/mcp`.

That's it. Ask Claude anything about your customers — pipeline,
follow-ups, who's gone quiet — and it'll route through Flitsy.

## Claude Code

Run `claude mcp add flitsy https://my.flitsy.app/mcp` in any project,
or add an entry to `~/.claude.json` under `mcpServers`. Restart Claude
Code and your Flitsy tools show up next session.

## Cursor

**Settings → MCP → Add server.** Paste `https://my.flitsy.app/mcp`
and save.

## Zed

Open your Zed settings JSON and add Flitsy under `context_servers`.
Zed picks up the new server on next reload.

## ChatGPT (beta)

ChatGPT's MCP support is rolling out. If you have access, paste
`https://my.flitsy.app/mcp` into its connector settings — same flow
as Claude.

## Anywhere else

If your client speaks MCP, paste the URL in. There's no Flitsy-specific
plumbing — the URL is the whole integration.

---

Stuck somewhere? [hello@flitsy.app](mailto:hello@flitsy.app). Real
people, fast replies.
