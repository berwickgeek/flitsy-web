#!/usr/bin/env python3
"""Generate 1080x1080 Reddit ad creatives for Flitsy, rendered from the live
site's content and brand tokens. Writes HTML, then shells out to headless
Chrome to rasterize each to PNG."""
import subprocess, pathlib, os

HERE = pathlib.Path(__file__).parent
CHROME = "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"

MARK = '''<svg class="mark" viewBox="0 0 260 200" xmlns="http://www.w3.org/2000/svg">
  <g transform="translate(0,10) scale(1.125)"><path d="M 42 8 C 32 8, 26 14, 26 30 L 26 64 C 26 75, 22 76, 6 80 C 22 84, 26 85, 26 96 L 26 130 C 26 146, 32 152, 42 152" fill="none" stroke="#1a1714" stroke-width="14" stroke-linecap="round" stroke-miterlimit="10"/></g>
  <g transform="translate(75,25) scale(0.95)" fill="none" stroke="#1a1714" stroke-width="16" stroke-linecap="round"><path d="M 78 8 C 62 8, 52 14, 52 30 L 52 150"/><path d="M 14 58 L 70 58"/></g>
  <rect x="178" y="50" width="13" height="125" rx="2.5" fill="#d09863"/>
  <g transform="translate(260,10) scale(-1.125,1.125)"><path d="M 42 8 C 32 8, 26 14, 26 30 L 26 64 C 26 75, 22 76, 6 80 C 22 84, 26 85, 26 96 L 26 130 C 26 146, 32 152, 42 152" fill="none" stroke="#1a1714" stroke-width="14" stroke-linecap="round" stroke-miterlimit="10"/></g>
</svg>'''

HEAD = '''<!doctype html><html><head><meta charset="utf-8">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Fraunces:opsz,wght@9..144,500;9..144,600;9..144,700&family=Inter:wght@400;500;600;700&family=IBM+Plex+Mono:wght@400;500&display=swap" rel="stylesheet">
<style>
:root{
  --ink:#1a1a1a;--ink-2:#3a3a3a;--ink-3:#5a5a5a;
  --paper:#fdf8ee;--paper-2:#f5ecd9;--rule:#dccfb1;--rule-soft:#ece1c5;
  --muted:#7a705a;--accent:#d09863;--accent-2:#8e6638;--accent-bg:#f7e9d4;
  --warm:#e07a3a;--warm-bg:#fde7d4;--leaf:#3a8a4f;
  --display:'Fraunces',Georgia,serif;--sans:'Inter',system-ui,sans-serif;--mono:'IBM Plex Mono',monospace;
}
*{box-sizing:border-box;margin:0;padding:0}
html,body{width:1080px;height:1080px;overflow:hidden}
.card{
  width:1080px;height:1080px;position:relative;
  font-family:var(--sans);color:var(--ink);
  background:
    radial-gradient(1200px 600px at 8% -8%, #fff7e8 0, transparent 60%),
    radial-gradient(900px 520px at 112% 24%, #f1e3c5 0, transparent 60%),
    var(--paper);
  padding:84px;display:flex;flex-direction:column;
}
.mark{height:64px;width:auto;display:block}
.brandrow{display:flex;align-items:center;gap:18px}
.wordmark{font-family:var(--display);font-weight:600;font-size:46px;letter-spacing:-0.01em}
.eyebrow{font-family:var(--mono);font-size:20px;letter-spacing:0.16em;text-transform:uppercase;color:var(--muted)}
h1{font-family:var(--display);font-weight:600;letter-spacing:-0.02em;line-height:1.04;color:var(--ink)}
em{font-style:italic;color:var(--accent-2)}
.lede{color:var(--ink-3);line-height:1.42}
.cursor{display:inline-block;width:14px;height:0.9em;background:var(--accent);border-radius:3px;vertical-align:-2px;margin-left:6px}
.foot{margin-top:auto;display:flex;align-items:center;justify-content:space-between}
.url{font-family:var(--mono);font-size:30px;color:var(--ink);font-weight:500}
.chips{display:flex;flex-wrap:wrap;gap:12px}
.chip{font-family:var(--mono);font-size:21px;color:var(--ink-2);background:#fff;border:1px solid var(--rule);border-radius:999px;padding:10px 18px;display:inline-flex;align-items:center;gap:9px}
.chip .dot{width:9px;height:9px;border-radius:50%;background:var(--leaf)}
.chip.beta .dot{background:var(--accent)}
/* chat */
.turn{display:flex;gap:20px;margin-bottom:26px}
.av{width:58px;height:58px;border-radius:14px;flex:none;display:flex;align-items:center;justify-content:center;font-weight:700;font-size:22px}
.av.user{background:var(--warm);color:#fff;font-family:var(--sans)}
.av.ai{background:var(--ink);color:var(--paper);font-size:30px}
.bubble{border-radius:20px;padding:24px 28px;font-size:30px;line-height:1.4;max-width:760px}
.bubble.user{background:var(--warm-bg);border:1px solid #f3cda8}
.bubble.ai{background:#fff;border:1px solid var(--rule-soft);box-shadow:0 2px 14px rgba(26,26,26,.05)}
.who{font-family:var(--mono);font-size:18px;color:var(--muted);margin-bottom:8px}
/* tool call */
.tool{background:#fff;border:1px solid var(--rule);border-radius:16px;overflow:hidden;margin-top:18px}
.tool-head{display:flex;align-items:center;gap:14px;padding:18px 22px;background:var(--paper-2);border-bottom:1px solid var(--rule-soft);font-family:var(--mono);font-size:21px}
.tool-head .ic{color:var(--accent-2)}
.tool-head .name{font-weight:500}
.tool-head .args{color:var(--muted)}
.tool-head .ms{margin-left:auto;color:var(--muted);font-size:18px}
.mt-row{display:grid;grid-template-columns:1.4fr 1fr 1fr 0.5fr;padding:16px 22px;font-size:23px;border-bottom:1px solid var(--rule-soft);align-items:center}
.mt-row:last-child{border-bottom:0}
.mt-row.head{font-family:var(--mono);font-size:17px;text-transform:uppercase;letter-spacing:0.08em;color:var(--muted)}
.mt-row .nm{font-weight:600}
.pill-warn{background:var(--warm-bg);color:var(--accent-2);border-radius:8px;padding:3px 12px;font-weight:700;font-size:21px}
/* steps */
.steps{display:flex;flex-direction:column;gap:30px;margin-top:14px}
.step{display:flex;gap:24px;align-items:flex-start}
.n{width:52px;height:52px;border-radius:50%;background:var(--ink);color:var(--paper);display:flex;align-items:center;justify-content:center;font-weight:700;font-size:26px;flex:none;font-family:var(--mono)}
.step .b{font-size:29px;line-height:1.35}
.step .b b{font-weight:700}
.step .b span{color:var(--ink-3)}
.urlbox{display:inline-flex;align-items:center;gap:14px;background:#fff;border:1px solid var(--rule);border-radius:12px;padding:14px 20px;margin-top:12px;font-family:var(--mono);font-size:26px}
.urlbox .copy{background:var(--ink);color:var(--paper);border-radius:8px;padding:7px 16px;font-size:18px;font-family:var(--sans);font-weight:600}
.price{font-family:var(--display);font-weight:600;font-size:120px;line-height:0.95;letter-spacing:-0.03em}
</style></head><body>'''
TAIL = "</body></html>"

# ---- creatives -------------------------------------------------------------
CARDS = {}

CARDS["01-hero"] = f'''<div class="card">
  <div class="brandrow">{MARK}<span class="wordmark">flitsy</span></div>
  <h1 style="font-size:96px;margin-top:120px">A CRM that lives <em>inside your chat.</em></h1>
  <p class="lede" style="font-size:38px;margin-top:36px;max-width:880px">Paste one URL into Claude. Your customers, email, and calendar are right there. The AI reads, drafts, and chases the follow-ups — you stay in flow.</p>
  <div class="foot">
    <span class="url">flitsy.app<span class="cursor"></span></span>
    <div class="chips">
      <span class="chip"><span class="dot"></span>Claude</span>
      <span class="chip"><span class="dot"></span>Cursor</span>
      <span class="chip beta"><span class="dot"></span>ChatGPT</span>
    </div>
  </div>
</div>'''

CARDS["02-pipeline"] = f'''<div class="card">
  <div class="eyebrow">Just ask</div>
  <div class="turn" style="margin-top:26px"><div class="av user">JM</div><div><div class="who">You</div><div class="bubble user">What's stalled in my pipeline?</div></div></div>
  <div class="turn"><div class="av ai">✶</div><div style="flex:1"><div class="who">Claude · with Flitsy connected</div>
    <div class="bubble ai" style="padding:22px 24px">Here's what's gone quiet:
      <div class="tool">
        <div class="tool-head"><span class="ic">⌁</span><span class="name">flitsy.deals.list</span><span class="args">{{ stalled_gt: 14 }}</span><span class="ms">312 ms</span></div>
        <div class="mt-row head"><div>Account</div><div>Owner</div><div>Stage</div><div>Days</div></div>
        <div class="mt-row"><div class="nm">Acme Co.</div><div>Sarah Lin</div><div>Negotiation</div><div><span class="pill-warn">23</span></div></div>
        <div class="mt-row"><div class="nm">Northwind</div><div>D. Pao</div><div>Demo</div><div><span class="pill-warn">19</span></div></div>
        <div class="mt-row"><div class="nm">Globex</div><div>Sarah Lin</div><div>Proposal</div><div>16</div></div>
      </div>
    </div></div></div>
  <div class="foot"><span class="url">flitsy.app<span class="cursor"></span></span><span class="eyebrow">No dashboard. The AI is the UI.</span></div>
</div>'''

CARDS["03-email"] = f'''<div class="card">
  <h1 style="font-size:70px">It drafts in <em>your</em> voice.</h1>
  <p class="lede" style="font-size:32px;margin-top:18px">Matched to your last thread. Nothing sends until you hit Send.</p>
  <div class="tool" style="margin-top:40px">
    <div class="tool-head"><span class="ic">✦</span><span class="name">draft_message</span><span class="ms">2,140 ms</span></div>
    <div style="padding:30px 34px;font-size:27px;line-height:1.5">
      <div style="color:var(--muted);font-family:var(--mono);font-size:20px;margin-bottom:6px">To: Sarah Lin &lt;sarah@acme.co&gt;</div>
      <div style="font-weight:700;font-size:30px;margin-bottom:18px">A quick check-in on the proposal</div>
      <p style="margin-bottom:14px">Hi Sarah,</p>
      <p style="margin-bottom:14px">Wanted to circle back on the proposal we walked through three weeks back — I know you mentioned a board check-in was next on the list.</p>
      <p style="color:var(--ink-3)">If a one-pager would help going into that meeting, happy to put one together…</p>
    </div>
  </div>
  <div class="foot"><span class="url">flitsy.app<span class="cursor"></span></span></div>
</div>'''

CARDS["04-setup"] = f'''<div class="card">
  <div class="brandrow">{MARK}<span class="wordmark">flitsy</span></div>
  <h1 style="font-size:74px;margin-top:70px">Three small things. <em>About five minutes.</em></h1>
  <div class="steps">
    <div class="step"><div class="n">1</div><div class="b"><b>Copy the Flitsy MCP URL.</b> One URL, same for everyone.<div class="urlbox">https://my.flitsy.app/mcp<span class="copy">Copy</span></div></div></div>
    <div class="step"><div class="n">2</div><div class="b"><b>Paste it into your AI client.</b> <span>Claude, Cursor, Zed — anything that speaks MCP. Your account is created the moment you connect.</span></div></div>
    <div class="step"><div class="n">3</div><div class="b"><b>Connect your stack.</b> <span>Gmail, Slack, calendar, Sheets, Notion. Each one's a switch, not a project.</span></div></div>
  </div>
  <div class="foot"><span class="url">flitsy.app<span class="cursor"></span></span></div>
</div>'''

CARDS["05-pricing"] = f'''<div class="card">
  <div class="brandrow">{MARK}<span class="wordmark">flitsy</span></div>
  <div style="margin-top:auto;margin-bottom:auto">
    <div class="eyebrow">No trial clock</div>
    <h1 style="font-size:88px;margin-top:24px">Free forever<br>for <em>2 users</em>.</h1>
    <p class="lede" style="font-size:38px;margin-top:30px;max-width:840px">Up to 6,000 records, no card. Pro is <b style="color:var(--ink);font-weight:700">$19/mo</b> when you outgrow it — unlimited records, every integration, smart views, and Flitsy email sending.</p>
  </div>
  <div class="foot"><span class="url">flitsy.app<span class="cursor"></span></span><span class="eyebrow">A CRM with no screens</span></div>
</div>'''

CARDS["06-aitheui"] = f'''<div class="card">
  <div class="eyebrow">MCP-first CRM</div>
  <h1 style="font-size:104px;margin-top:90px">No dashboard.<br>No tabs.<br><em>The AI is the UI.</em></h1>
  <p class="lede" style="font-size:36px;margin-top:40px;max-width:860px">Flitsy comes to the tools you already talk to — not the other way around. Stop copy-pasting context. Stop building reports nobody reads.</p>
  <div class="foot">
    <span class="url">flitsy.app<span class="cursor"></span></span>
    <div class="chips">
      <span class="chip"><span class="dot"></span>Claude</span>
      <span class="chip"><span class="dot"></span>Zed</span>
      <span class="chip beta"><span class="dot"></span>Any MCP client</span>
    </div>
  </div>
</div>'''

# ---- render ----------------------------------------------------------------
for name, body in CARDS.items():
    html = HEAD + body + TAIL
    hp = HERE / f"{name}.html"
    hp.write_text(html)
    out = HERE / f"{name}.png"
    subprocess.run([CHROME, "--headless", "--disable-gpu", "--hide-scrollbars",
                    f"--screenshot={out}", "--window-size=1080,1080",
                    "--force-device-scale-factor=1", "--virtual-time-budget=4000",
                    f"file://{hp}"], check=True,
                   stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    print(f"rendered {out.name}")
print("done")
