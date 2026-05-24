# Reddit Ad Test for Flitsy: A $100 AUD Playbook (and an Honest Reality Check)

## TL;DR
- **A $100 AUD (~$66 USD) Reddit ad test will not, on its own, produce statistically meaningful conversion data for an MCP-native CRM** — at B2B SaaS conversion-objective CPCs of US$0.80–$1.75, you'll get roughly 35–80 clicks total, well below the ~500-click bar industry sources cite for reliable read-outs. Run it anyway, but design it as a **CPC/learning probe + retargeting-pool builder**, not a conversion test.
- **The single best $100 spend is a hybrid**: ~$60 AUD on a single Reddit traffic campaign targeting r/ClaudeAI + r/LocalLLaMA + r/SideProject with a free-form (text-style) ad, ~$40 AUD held back to retarget the resulting pixel audience with a stronger founder-led creative. In parallel, invest equal or greater *time* in organic posts to r/SideProject, r/ClaudeAI, and the r/SaaS / r/Entrepreneur weekly feedback threads — that's where this specific category (agent-native CRM via MCP) will actually find its first 50 signups in 2026.
- **Realistic outcome of the $100 spend**: expect 50–150 site visitors, 0–5 signups directly attributable, and — most valuably — a seeded retargeting pixel, a CPC benchmark, and one or two creative angles validated for the next budget. Decision rule: only scale if CPC stays under US$1.50 *and* signup rate clears 3%.

## Key Findings

**Verification gap on the product itself.** I was unable to directly fetch flitsy.app or surface its public copy in indexed search results; the name collides with several unrelated brands (Flits Shopify loyalty app, Flitsmeister traffic app, Flits crypto wallet, Filtsy AR app). All product-specific recommendations below assume the user's brief is accurate: **Flitsy is an MCP-server-fronted CRM that lets AI agents (Claude, ChatGPT with developer mode, Cursor, etc.) read/write CRM data via the Model Context Protocol.** Before launching anything, **confirm on the live site exactly which signup flow exists (waitlist / free tier / paid trial)** because the offer mechanic in §5 hinges on it.

**Reddit's economics at $100.** Reddit's hard minimum is US$5/day per campaign and US$25 lifetime; that's not the binding constraint. The binding constraint is the *learning floor*. 2025–2026 advertiser benchmarks from AbeTheAgency (citing AdBacklog, Metadata.io, Affect Group and InterTeam Marketing) put broad B2B/tech SaaS CPCs at **~US$0.50–$2.00, with niche/rational B2B in specialized SaaS reaching $4–$8 per click in very narrow, high-intent segments**. Stackmatix's 2026 traffic-vs-conversion split puts conversion-objective CPC at **US$0.80–$1.75 vs. $0.20–$0.80 for traffic**. Industry CPAs for B2B/SaaS qualified signups commonly land at **US$50–$100+**. At those prices, $100 AUD ≈ $66 USD is one CPA, not a campaign.

**Reddit's culture and self-promotion enforcement have tightened.** Per Soar Agency's analysis, on **April 14, 2026, r/SaaS moderators announced a once-per-60-days self-promo limit, expanded it to comment plugs and product mentions, and said repeat violations can blacklist the product URL in AutoMod**. r/Entrepreneur, r/smallbusiness, r/sales, and r/msp are all hostile to overt promo. Organic posts must be value-led and run through the appropriate weekly threads.

**Where Flitsy's audience actually lives.** Three concentric rings, in priority order:
1. **AI / MCP enthusiasts** — r/ClaudeAI (~862K), r/LocalLLaMA (~727K), r/artificial (~1.2M), r/mcp (small/niche, verify size). These users are *building* with MCP and immediately understand "agentic CRM."
2. **Indie founders shipping product** — r/SideProject (~688K, the most promo-friendly major sub), r/indiehackers (~151K), r/EntrepreneurRideAlong (~688K with a Self-Promotion flair).
3. **CRM-in-market buyers** — r/SaaS (~677K, hostile), r/startups (~2.0M, restricted), r/sales (~449K, banned), r/CRM (~20K, vendor-skeptical), r/Entrepreneur (~5.2M, banned in main feed).

The asymmetry matters: **ring 1 is where ad spend will be most efficient and organic posts will be most welcome**; ring 3 is where the buyers are but the rules are punitive.

---

## Details

### 1. Campaign type / approach at $100 AUD

**Verdict: Don't run a Reddit *conversion-objective* campaign at $100.** Reddit's conversion algorithm needs ~50 conversion events to exit the learning phase. At a US$50 CPA that's $2,500 of spend. Conversion mode at $66 USD will simply never optimise — you'll pay conversion-CPC rates and still get random delivery.

**Instead run a Traffic (CPC) objective campaign**, capped at a manual CPC bid you control (around US$0.75–$1.00 with the option to flex to $1.50 in narrow subs). Use this campaign for three jobs at once:
1. Drop the **Reddit Pixel** on flitsy.app to populate a retargeting audience (this is permanent value).
2. Get a **CPC benchmark** by subreddit for your category — the single most valuable artefact from a $100 test.
3. Catch the small number of high-intent clicks that *will* convert (think: Claude power users who land on the page and self-serve into a free tier or waitlist).

**Hybrid is non-negotiable at this budget.** Plan to spend ~5–10 hours of your own time on organic posting in the same week as the ads run. The paid spend warms the retargeting pixel; the organic posts produce the actual signups; the two reinforce each other (people who saw the ad later see the organic post and trust both more).

**What "success" looks like at $100**: a defensible CPC number, ~50–150 unique site visitors in your Reddit Pixel audience, and one validated creative angle. Realistically, 0–5 direct signups. That's not failure — that's the data you paid for.

### 2. Subreddits

Prioritised list with audience size, promo tolerance, and recommended use (paid targeting vs. organic posting). Sizes are mid-2025/early-2026 figures from GummySearch / SubredditStats and may have grown modestly since.

| Subreddit | Approx members | Self-promo posture | Use for paid? | Use for organic? |
|---|---|---|---|---|
| **r/ClaudeAI** | 862K | Tolerated when it's a Claude-powered build | **YES — primary target** | YES — "Built a CRM that Claude drives via MCP" framing |
| **r/SideProject** | 688K | Welcomed — whole sub is for showing projects | **YES — primary target** | YES — best organic launch sub |
| **r/LocalLLaMA** | 727K | Tolerated if open-source / technically substantive | **YES — secondary** (test) | Risky unless self-hostable |
| **r/mcp** / r/ModelContextProtocol | Small, verify | Niche, on-topic by definition | YES if ad inventory exists | YES — exactly the audience |
| **r/indiehackers** | 151K | Value-led promo welcomed; weekly project threads | YES — small but qualified | YES |
| **r/EntrepreneurRideAlong** | 688K | Self-Promotion flair built-in | YES | YES — build-in-public posts |
| **r/artificial** | 1.2M | Looser than r/MachineLearning, no promo thread | Test, expect higher CPC | Cautious — value content only |
| **r/SaaS** | 677K | **April 14, 2026 mod rule: 1 promo per 60 days**; weekly feedback thread is the only safe lane | Test for paid only | **Weekly Feedback Thread only** |
| **r/startups** | 2.0M | "I will not promote" disclaimer enforced; monthly Share Your Startup sticky | Possible, costlier | Sticky thread only |
| **r/CRM** | ~20K | Vendor-skeptical but tolerant of "what CRM?" recs | Skip (too small for paid efficiency) | YES — answer questions, don't post |
| **r/Entrepreneur** | 5.2M | Banned in feed; recurring promo thread is the lane | Skip — wrong audience anyway | Only the weekly thread |
| **r/smallbusiness** | 2.5M | "Not for advertisements" | Skip | Skip |
| **r/sales** | 449K | Immediate ban for promo | Skip for paid | Comment-only, expertise-led |
| **r/msp** | 170K | Aggressively anti-vendor | Skip | Skip until you have ROI proof |

**Hard nos for paid at $100**: r/Entrepreneur (audience too broad, CPCs inflated by every founder advertising), r/smallbusiness (wrong buyer for an MCP CRM), r/msp (will torch your creative in the comments).

### 3. Ad creative

**Format: Free-Form (text-led) ad, with the optional addition of one screenshot.** Per Reddit Ads' own format docs and 2026 B2B/SaaS guides (Conbersa, Obility, InterTeam), free-form ads "look almost the same as regular posts" and are the strongest fit for SaaS / dev tools / B2B services. Image ads underperform here. Video is overkill for a $100 test. **Avoid carousel and product ads — they read as ads instantly.**

**Three creative angles to A/B at this budget (rotate, don't all run simultaneously — pick the strongest 1–2 for week one):**

**Angle A — "Stop pasting CRM data into Claude" (problem framing).** Targets r/ClaudeAI, r/mcp, r/LocalLLaMA.
> *Headline:* Your CRM still makes Claude do screenshots. Mine doesn't.
> *Body:* I got tired of pasting contact lists into Claude every time I wanted help drafting follow-ups. So I built Flitsy — a CRM with an MCP server baked in. Claude (or Cursor, or any MCP client) just connects and queries it directly. Add a contact, log a call, run a pipeline report — all in chat. Free tier available if you want to point Claude at it. [link]

**Angle B — "I replaced HubSpot with a folder Claude can edit" (build-in-public).** Targets r/SideProject, r/indiehackers, r/EntrepreneurRideAlong.
> *Headline:* Ditched HubSpot for a CRM Claude operates for me. Here's the build.
> *Body:* Solo founder, hated paying $50/seat for a CRM I clicked through twice a week. Spent a weekend building Flitsy: it's a real CRM, but its primary interface is an MCP server my AI agent talks to. I say "who haven't I followed up with in 2 weeks?" and Claude actually queries the pipeline. Open to whoever wants to try it — pricing is [confirm on site]. AMA in the comments.

**Angle C — "For agencies running 5+ client CRMs" (pain-point B2B).** Targets r/agency (verify size), r/SideProject, r/SaaS feedback thread.
> *Headline:* Running an agency? Your CRM should answer questions, not store them.
> *Body:* If you're juggling client work and lose 30 minutes a day digging through a CRM, the MCP era fixes that. Flitsy is an agent-first CRM — Claude/ChatGPT plugs into your data and you ask it things in English. Built for solo operators and small teams. Two-minute setup if you've got Claude Desktop. [link]

**Reddit copy rules that are non-negotiable:**
- Lowercase headlines, no exclamation points, no emoji.
- First sentence states the problem in the user's words.
- Acknowledge a trade-off ("not for enterprise sales orgs", "still rough around the edges") — Reddit rewards this.
- Use a real founder username and **enable comments** on the ad. Reply to every comment within 2 hours. This single behaviour is the most underused conversion lever on Reddit ads.
- Headline cap: 80 characters to avoid truncation on mobile (Reddit's own spec).

### 4. The link / landing page

**Send traffic to a dedicated landing page, not flitsy.app's homepage.** The page needs four things:
1. **Headline matches the ad headline** (message-match is the #1 driver of B2B landing-page conversion rate).
2. **A 60-second Loom or animated gif** showing Claude actually using the Flitsy MCP server. Reddit users want to see the thing work, not read about it.
3. **One CTA above the fold** — the *exact same CTA the website currently has* (sign up / join waitlist / start free), not a new variant.
4. A short FAQ at the bottom addressing: "is this open source?", "what's the pricing?", "what MCP clients work?", "is my data leaving my machine?". These are the four questions Reddit users will ask in the comments anyway.

**UTM tracking — use these exact UTMs** so the ad traffic shows up cleanly in GA4/Plausible:
- `utm_source=reddit&utm_medium=cpc&utm_campaign=flitsy_q2_test&utm_content=[angle_a|angle_b|angle_c]&utm_term=[subreddit_name]`

**Reddit Pixel setup is mandatory** even at $100 — it's a 10-minute job and the pixel audience persists. Install via GTM (Reddit's recommended method): create a Custom HTML tag with the pixel snippet, fire on All Pages, then configure a `SignUp` standard event firing on your post-signup thank-you page (and `Lead` on waitlist confirmation if relevant). If you have the engineering bandwidth, also wire up the **Reddit Conversions API** server-side — it survives Safari ITP and ad blockers, which kill ~30–40% of pixel-based attribution per CustomerLabs' analysis. For a $100 test, pixel-only is acceptable; CAPI becomes important at scale.

Set a **28-day click attribution window** in Reddit Ads Manager (Stackmatix flags that the default 7-day window "dramatically undercounts" B2B conversions, as most happen within 10 days of ad exposure).

### 5. The offer

**Match the offer to whatever exists on flitsy.app today** — do not invent a new mechanic for this test. Three scenarios:

- **If Flitsy is a waitlist**: lead with "Reddit early-access" — promise everyone who signs from this campaign gets in before the public waitlist. Tag them in your DB and honour it. This is the highest-friction → highest-quality signup.
- **If Flitsy has a free tier**: hammer "free, no credit card, connect Claude in 60 seconds." For an MCP-native CRM, the free tier IS the marketing — anyone who connects it will tell three friends in r/ClaudeAI organically.
- **If Flitsy is paid-only with a trial**: extend the trial for Reddit traffic (e.g. 30 days vs. 14) and use a discount code like `REDDIT30` so you can attribute conversions even when the pixel misses them. Don't run a lifetime deal — it attracts the wrong customer for a CRM (people who will never expand, but will demand support forever).

**Strongest offer for this category, in priority order**: (1) free tier with generous limits → (2) extended trial + founder Slack/Discord access → (3) lifetime discount (e.g. "50% off forever for the first 100 from Reddit"). Lifetime deals work on Reddit specifically because Redditors love feeling like they're early — but only if your unit economics support it.

### 6. Spend allocation

Budget split for a 7–10 day test (all USD-equivalent; ≈ $66 USD = $100 AUD at current rates):

| Phase | Duration | Daily budget | Total | Job |
|---|---|---|---|---|
| **Phase 1 — Cold traffic** | Days 1–5 | $7–$10/day | ~$40 USD ($60 AUD) | Single ad group, **one** free-form ad (Angle A or B — pick the one most aligned to your strongest sub), targeting r/ClaudeAI + r/SideProject + r/LocalLLaMA + r/mcp + r/indiehackers + r/EntrepreneurRideAlong (combine in one ad group to give Reddit's algo room). Manual CPC bid US$0.85. |
| **Phase 2 — Retarget** | Days 6–10 | $5–$6/day | ~$25 USD ($40 AUD) | Same free-form creative or a stronger founder-led variant, targeting **Reddit Pixel website visitors (last 30 days)**. Retargeting conversion rates on Reddit are typically 3–5× cold traffic. |

**Why a single ad group, not split tests:** at $100, splitting across 3 ad groups gives each ~$22 — none will have enough volume to even leave learning. Stackmatix's first-time advertiser guide makes this point bluntly: "Running five campaigns at $10 per day each gives you $50 in total daily spend but starves every individual campaign of the volume needed to optimize. Two campaigns at $25 each will outperform five at $10 every time." Concentrate. Run a second creative *sequentially* in week two if the first one validates.

**Bidding:** start with manual CPC at $0.85; if delivery is thin after 48 hours, raise to $1.20. Avoid Reddit's auto-bid / Max Campaigns at this budget — Max Campaigns have a $20/day or $620 lifetime minimum and need volume to work.

**Placement:** Enable both Feed and Conversation placements. Per Reddit's official Conversation Ads data (reported by Search Engine Land): "Combining Feed and Conversation Ads drives Action Intent more than twice as strongly as Feed only (+2.44% to +5.46%), Reddit said. Campaigns using both placements saw 83% higher brand awareness compared to Feed only."

**Geo targeting:** **Don't restrict to Australia.** Reddit's CRM/MCP audience is overwhelmingly US/EU. Target **US + CA + UK + AU + NZ + EU-English** and let the auction find the best clicks. The AUD billing currency doesn't change targeting reach.

### 7. Measurement

**Watch these metrics, in this order:**

| Metric | Healthy benchmark for B2B SaaS Reddit | Red flag |
|---|---|---|
| **CPC** | US$0.50–$1.50 (broad B2B/tech) per AbeTheAgency; up to $4–$8 in "narrow, high-intent" niche segments | >$2.50 sustained = wrong audience or weak creative |
| **CTR** | 0.3–0.6% (free-form), up to 1% if creative is sharp | <0.2% = creative is dying, kill and replace |
| **Click-to-signup rate** | AbeTheAgency cites "~1–5% click-to-trial or click-to-demo conversion rates from Reddit traffic" for B2B SaaS; "lower rates for long, high-friction forms and higher rates for simpler actions" | <0.5% = landing page mismatch |
| **CPA / CPSignup** | $30–$80 USD for product-led SaaS | >$150 = re-evaluate before scaling |
| **Comments / upvote ratio on the ad** | Net positive upvotes, ≥5 comments by day 3 | Net downvoted = pull the ad immediately |

**The single most diagnostic metric for Reddit specifically is the comment/upvote signal on the ad itself.** If your ad gets downvoted, Reddit's algorithm will throttle delivery and your CPC will spike. If it gets upvoted with positive comments, your effective CPC will drop as the auction rewards engagement. Check the ad's actual Reddit thread daily and reply to every comment.

**Decision criteria after $100 spent:**
- **Scale (raise to $500–$1,500/month)** if: CPC ≤ $1.50, CTR ≥ 0.35%, ≥2 attributed signups, no net-downvoted ads. Specifically scale the winning subreddit and the winning angle.
- **Iterate (re-test with new creative on same $100)** if: CPC ≤ $1.50 but signups = 0. Creative or landing page is broken, not the channel.
- **Pivot away from Reddit ads** if: CPC > $2.50 across two creative variants, OR ads are net-downvoted. In that case, double down on organic posting in r/SideProject and r/ClaudeAI, and consider redirecting future budget to Google Search ads on "MCP CRM" / "Claude CRM" / "AI agent CRM" keywords — much lower-volume but pure-intent traffic.

### 8. Alternatives and honest take

**You asked for honesty. Here it is.**

For a brand-new MCP-native CRM in May 2026, **$100 AUD spent on Reddit ads is below the threshold where the channel can prove or disprove itself.** The cost isn't the money — it's the risk of drawing the wrong conclusion. If you get unlucky and your one creative tanks, you might write off Reddit when it's actually the highest-fit channel for this category.

**Higher-ROI uses of the same $100 or the same week of effort:**

1. **Organic Reddit (cost: $0 + ~10 hours of your time).** For Flitsy specifically, organic will outperform paid. Your audience — Claude power users, MCP early adopters, indie founders — *lives* in r/ClaudeAI and r/SideProject and will reward an authentic founder post (with a working demo) with a wave of traffic that no $100 ad campaign can match. Concrete plan:
   - Post a build story to **r/SideProject** with a 30-second video of Claude actually driving Flitsy ("I gave Claude my CRM via MCP and it's eerie"). This format consistently hits front page of the sub.
   - Post a more technical write-up to **r/ClaudeAI** focused on the MCP server architecture and what you learned building it. Top of subreddit potential.
   - Drop into the **r/SaaS weekly feedback thread** (the one sanctioned lane post the April 14, 2026 rule change) with a specific feedback ask, not a pitch.
   - Spend the rest of the week answering "what CRM should I use?" questions in r/Entrepreneur, r/startups, r/smallbusiness without linking — let your profile do the selling.
   - **Expected outcome: 5–50× more signups than the $100 ad spend, but front-loaded with effort.**

2. **Spend the $100 on a Claude Pro / Cursor Pro budget for a public build-in-public series on X/LinkedIn.** Lower fit for a $100 single shot, but compounds.

3. **Google Search ads on intent keywords** ($100 AUD): bids on "MCP CRM", "Claude CRM", "AI CRM Australia", "agentic CRM" are currently low-competition because the category is so new. Probably 30–60 clicks at much higher intent than Reddit. **Worth a parallel $50 test** alongside the Reddit campaign if you want to A/B channels.

4. **Hacker News.** A genuinely good "Show HN: I built a CRM Claude operates via MCP" post will outperform any $100 ad spend you can construct, and the audience overlap with Reddit's r/ClaudeAI is high. Free; one shot; submission timing is debated in the literature — most launch guides recommend Tuesday–Thursday mornings US time, but Myriade's analysis of 157,000+ Show HN posts via the public HN BigQuery dataset found that "contrary to our intuition, the weekend worked better" for breakout (30+ vote) success, and Max Woolf's large-scale statistical analysis concluded "submission time alone did not strongly determine which posts went viral." Quality of post matters far more than timing.

5. **Direct outreach to MCP-server directory listings** (PulseMCP, Glama, MCP Servers awesome lists, Lobehub). Free, evergreen distribution, and the people browsing those directories are exactly your ICP. Submit Flitsy as an MCP server with a "remote" install option.

**The strongest play for $100 AUD specifically:** spend ~$60 on the Reddit traffic test described in §6 *primarily to seed the Reddit Pixel*, while running the organic plan in parallel. The pixel audience you build during week one becomes the most valuable artefact, because three months from now when you have a $1,000 budget, you'll already have a warm retargeting pool of MCP-curious Redditors. The $100 isn't really an ad test — it's tuition for the channel.

---

## Recommendations

**Stage 1 — Pre-flight (this week):**
1. Confirm flitsy.app's actual signup mechanic (waitlist / free / paid) and lock the offer accordingly.
2. Install Reddit Pixel via GTM. Configure `SignUp` and `Lead` events. Verify with Reddit Pixel Helper. *Threshold to skip ads:* if you can't get the pixel firing on the thank-you page, don't run paid traffic — wait until tracking works.
3. Build the dedicated landing page (`/reddit` or `/mcp-crm`) with the matched headline, demo video, single CTA, and FAQ.
4. Pick **one** ad angle (start with Angle A — "Stop pasting CRM data into Claude" — it targets the warmest audience).

**Stage 2 — Launch (days 1–5):**
5. Single ad group, single free-form creative, manual CPC bid US$0.85, daily budget US$8, targeting r/ClaudeAI + r/SideProject + r/LocalLLaMA + r/mcp + r/indiehackers + r/EntrepreneurRideAlong, Feed + Conversation placements, 28-day attribution.
6. Same day: post the Angle B build-story to r/SideProject and the technical version to r/ClaudeAI.
7. Reply to every comment on both the ad and the organic posts within 2 hours.

**Stage 3 — Retarget (days 6–10):**
8. Pause the cold ad group. Spin up a retargeting ad group at US$5/day targeting Reddit Pixel website visitors (last 30 days), same creative or Angle B as a variant.
9. Drop a feedback-ask post into the r/SaaS weekly feedback thread.

**Stage 4 — Decide (day 11):**
10. Apply the §7 decision criteria. Document CPC, CTR, signup count, and the qualitative comment signal in one place.
11. **Scale, iterate, or pivot** per §7. If pivoting, redirect next budget to Google Search ads on MCP-CRM intent keywords and double organic frequency.

**Benchmarks that change the recommendation:**
- If observed CPC averages **<$0.80 USD** in week one, scale immediately to $500/month — you've found a cheap channel.
- If organic post hits >500 upvotes on r/SideProject or r/ClaudeAI, **stop the ads** — you're getting the same outcome for free and ads may even cannibalise organic reach.
- If three creative angles tested over $300 total spend all CPA above $150, **Reddit is not your channel for now** — re-test in 6 months when MCP awareness is higher.

## Caveats

- **Product copy unverified.** I could not fetch flitsy.app or find indexed content for it. All product-specific creative angles are written against the user's brief; verify language and feature claims against the live site before publishing ads.
- **Subscriber counts are mid-2025 / early-2026 snapshots** (primarily from GummySearch, which closed Nov 30, 2025). Real numbers in May 2026 are likely modestly higher across the board. r/mcp and r/agency could not be confirmed — verify directly on Reddit.
- **The r/SaaS 60-day self-promo rule (April 14, 2026)** is sourced to Soar Agency's analysis. Verify against the r/SaaS sidebar directly before structuring any organic plan around it.
- **CPC and CPA benchmarks are US-dollar figures from US-published advertiser data** (AbeTheAgency citing AdBacklog / Metadata.io / Affect Group / InterTeam Marketing; Stackmatix 2026 first-time advertiser guides). Australian advertisers pay in AUD but the auction is global; the underlying USD economics apply. The $100 AUD ≈ $66 USD conversion is approximate at current rates.
- **"~500 clicks for statistical significance"** is an industry rule of thumb (Stackmatix), not a hard mathematical floor. It depends on baseline conversion rates. For a high-intent landing page converting at 5%+, you can get directional read at 200 clicks; for a 1% conversion page, you need 1,000+.
- **MCP is a fast-moving category.** The user's positioning advantage may evaporate within 12 months as HubSpot, Salesforce/Agentforce, Zoho and Attio-class incumbents ship their own MCP servers (all already in flight as of mid-2025–2026). The Reddit play here is partly a land-grab on category awareness, not just signups.