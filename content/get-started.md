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

1. Open <https://claude.ai/customize/connectors> (or go to **Settings → Connectors** in Claude).
2. Click **Add custom connector**.
3. Paste `https://my.flitsy.app/mcp`.
4. Authorize when prompted — your account is created on first connect.

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
