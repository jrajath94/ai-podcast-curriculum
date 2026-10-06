# EXAM REPORT — ACQUIRED Track, Exam Gate E1

- Track: ACQUIRED (Ben Gilbert & David Rosenthal)
- Date: 2026-10-06
- Chapters examined: `ep01.md` (341 lines) through `ep11-synthesis.md` (225 lines)
- Examiner score: **30/30 questions fully answerable from chapter text**

## Verdict: PASS

Every one of the 30 questions below is answered entirely from the chapter text, with a chapter:line citation for each factual claim. No question fails. Two cross-chapter inconsistencies were found and are flagged at the end; they do not break any question because each question cites a single chapter.

Composition: 10 numerical questions (recomputed arithmetic from chapter numbers), 5 explain-like-I'm-new, 7 applied, 8 deep mechanism/decision questions. All 11 chapters covered.

---

## The 30 questions

### Q1 (ep01, numerical). The RIVA 128 emulator rendered "about one frame per hour" (ep01:47). A game needs 30 frames per second. How many times slower was the emulator than the real chip? Show the arithmetic.

**Answer.** 30 frames/sec × 60 sec/min × 60 min/hour = 108,000 frames/hour. The emulator managed 1 frame/hour (ep01:47), so it was 108,000 times slower, which the chapter rounds to "roughly 100,000 times slower" (ep01:307). Nvidia shipped the chip on that emulator anyway; the tape-out went straight to production (ep01:47, 242).

### Q2 (ep01, deep). Why is architectural compatibility Jensen's single non-negotiable rule? Trace the mechanism.

**Answer.** Jensen states that "every accelerator Nvidia makes must be architecturally compatible with every other one" and that everything else is negotiable (ep01:122). The mechanism: developers invest years learning CUDA and writing CUDA code; if a new generation invalidates that investment, the platform dies (ep01:122). Compatibility is what "turns a product line into a platform" and protects the installed base he cites, 250 to 300 million active CUDA GPUs, all compatible (ep01:122). The moat economics follow: the moat is not one chip but those compatible GPUs, the CUDA software stack, the trained developers, the libraries, and the switching cost of rewriting all of it (ep01:182).

### Q3 (ep01, applied). A car-parts company sells $20 sensors to 10 million cars per year: a $200M market. Apply Jensen's "thousand times" flip. What are the two market framings and what ratio does the chapter claim between them?

**Answer.** Framing 1 (chip company): cars × chips per car = 10M × $20 = $200M (ep01:225). Framing 2 (intelligence company): the value of the outcome × everyone who benefits — e.g., the value of a chauffeur for everyone with a car (ep01:225, 277). Jensen's claimed ratio: "roughly a thousand times" larger opportunity (ep01:225), i.e., ~$200B in this toy. The flip is pricing the outcome, not the component (ep01:225, 277).

### Q4 (ep02, numerical). TSMC spent "almost 6 billion dollars" on 2010 capex, "roughly triple" the "2 to 2.5 billion" spent yearly the prior decade (ep02:107). Recompute the multiple range and check the chapter's wording.

**Answer.** 6 / 2 = 3.0× and 6 / 2.5 = 2.4×. The true multiple lies in 2.4–3.0×, so the chapter's "roughly triple" is consistent (ep02:107). (The same bet paired the capex with R&D fixed at 8% of revenue by fiat, recession or not — ep02:105.)

### Q5 (ep02, deep). The learning curve says: take all of Apple's order for maximum volume. Morris took half and borrowed. Reconcile this with numbers.

**Answer.** The learning-curve logic is: price early at end-game cost, win the volume, drive down the curve fastest (ep02:159-161). But a whale order is existential if the forecast is wrong: "if your forecast of iPhone demand is off by 5 or 10 percent... the node generation's profitability collapses, free cash flow collapses, and you cannot fund the next node" (ep02:161). Morris's compromise: keep the dividend, sell no stock, borrow billions, and "take half of what Apple said it needed" (ep02:126) — because "customers have no skin in the game when they state demand" (ep02:126). The half-order is the compromise "between the curve and survival" (ep02:161).

### Q6 (ep02, applied). A factory with a $20B fixed cost (ep02:163) prices at end-game cost and forecasts 1M mature wafers, but demand comes in 10% low. Using Morris's Apple analysis, name exactly what breaks.

**Answer.** Per ep02:161, three things break in sequence: (1) the node generation's profitability collapses; (2) free cash flow collapses; (3) the company cannot fund the next node. The mechanism: the learning curve requires the forecasted volume to amortize the fixed cost; a 5–10% miss on a fully-built node is existential, not just disappointing (ep02:161). (The chapter's Fermi math makes the fixed-cost exposure explicit: a $20B fab must sell ~1M wafers to pay for itself — ep02:256.)

### Q7 (ep03, explain like I'm new). Explain Zuckerberg's "learn faster" formula and why it let Meta survive nine death waves.

**Answer.** Zuckerberg's identity claim: "We are a technology company focused on human connection, not a specific type of app" (ep03:45) — so Meta was never the app under attack. The formula: "If we can learn faster than every other company, we are going to win" (ep03:49): ship early, get real feedback, learn what people actually want, ship again; by version 3–5 the product has absorbed more reality than any competitor's (ep03:49). Each wave (MySpace, Twitter gen 1, Instagram, Snapchat, WhatsApp, TikTok, Apple ATT, ChatGPT — eight named, Ben says nine — ep03:41) attacked an app; "the learning machine underneath kept producing the next app" (ep03:206-207).

### Q8 (ep03, deep). Why is the mobile rewrite a 1.5-year mistake and the political miscalculation a 20-year mistake? The mechanisms differ.

**Answer.** The HTML5 rewrite was a technical mistake with a clear fix: the web-everywhere plan lost to native feel, the fix was a pure rewrite with features paused for about a year (ep03:129-134); the scarce resource was pain tolerance, "a year and a half of pain" while the stock halved (ep03:134-138). The political mistake was a misdiagnosed crisis *type*: Zuckerberg "treated a political crisis as a corporate crisis" — the corporate instinct (take ownership, fix it) invited more kicking because "many attackers were not operating in good faith" and "accepting responsibility for things Meta did not do became an invitation to be kicked for more" (ep03:140-146). Duration: started 2016, "another 10 years to fully work through" (ep03:146), versus the rewrite's clear technical path (ep03:153 table).

### Q9 (ep03, applied). A founder ships one polished product every two years and wonders why a smaller, faster competitor wins. Diagnose using the chapter's Meta-vs-Apple comparison.

**Answer.** The chapter contrasts the two cultures directly: Meta ships "early, near embarrassment" for fast feedback; Apple ships "long polish, ship when perfect" with feedback delayed until launch (ep03:87-90). The price of Meta's way is "small brand damage per ship"; the price of waiting is "learning time lost forever" (ep03:89-90). The founder's two-year cadence is the Apple column without Apple's brand; the diagnosis from the chapter is "if you want praise every time you ship, you will ship too late to learn" (ep03:206-207 Q&A), and "never near embarrassment = shipping too late to learn" (ep03:244).

### Q10 (ep04, numerical). Google's monthly tokens served: 10T (Apr 2024), ~500T (Apr 2025), 980T (Jun 2025) (ep04:186-193). Compute the 14-month multiple and the implied monthly compounding rate.

**Answer.** Multiple: 980T / 10T = 98× in ~14 months (ep04:186). Monthly rate: 98^(1/14) ≈ 1.39, i.e., about 39% compounding per month. The chapter flags the one-year jump as "50 times in one year" (ep04:186, 192). This is the ocean of inference over which Google amortizes training costs (ep04:186).

### Q11 (ep04, deep). Within two years of publishing "Attention Is All You Need," all eight authors had left Google (ep04:116, 219). What is the mechanism of the exodus, and what did Google pay to reverse it for one researcher?

**Answer.** The mechanism: "Google treated the transformer as a research result to publish and a feature to add to search. Startups treated it as a company to build. Ambitious researchers follow the steepest mission gradient. The lesson: a lab that publishes everything but commercializes cautiously will train its competitors' founders" (ep04:244). The paper had 173,000+ citations by 2025 and gave every startup the recipe (ep04:116, 219). The price of reversal: in 2024 Google paid $2.7B in a licensing deal with Character AI that brought Noam Shazeer back — "Larry and Sergey decided that competing seriously required Noam back, so they wrote a blank check" (ep04:148).

### Q12 (ep04, explain like I'm new). What was wrong with RNNs and LSTMs, and what did the attention/transformer idea change?

**Answer.** Google Translate's RNNs "forgot things too quickly: their effective context window was short" (ep04:91). LSTMs added a persistent memory and cut Translate's error rate 60% in 2016, but they were "computationally intense and parallelize poorly" (ep04:91). The attention idea (Jakob Uszkoreit): tell the model to "pay attention to the entire text, then predict the next word from the whole context" — like a professional human translator who reads everything first, then translates with full context (ep04:95). Looking at everything is expensive but "parallelizes beautifully," and bigger models kept getting better — it scaled (ep04:95, 100).

### Q13 (ep05, numerical). Google's revenue: $86M (2001), $440M (2002), $1.5B (2003) (ep05:128-130). Compute the 2001→2002 and 2001→2003 multiples.

**Answer.** 2001→2002: 440 / 86 ≈ 5.1×. 2001→2003: 1,500 / 86 ≈ 17.4×. The chapter calls this the three-year "detonation" (ep05:197 memory aid). Note the margin structure behind it: AdWords stayed an 85%-gross-margin business while AdSense kept ~20% (ep05:121).

### Q14 (ep05, explain like I'm new). Explain PageRank, including the anchor-text insight.

**Answer.** Scholars rank papers by citations; PageRank treats a hyperlink the same way: "a link from page A to page B is page A's vote that B matters" (ep05:40). The bonus insight: "the clickable words they choose [anchor text] are usually a better description of your page than anything you wrote about yourself," so Google used them as free descriptions (ep05:43). By 2007 ranking used 200 signals, but the citation idea was the seed (ep05:43). (Ascii summary at ep05:45-52.)

### Q15 (ep05, deep). Google promised AOL a $100M guarantee it did not have (ep05:92). Using the chapter's numbers, explain why this was arithmetic, not hope.

**Answer.** Sergey Brin's own framing: "We could have gone bankrupt. This is quite literally Google betting the company" (ep05:92). It was rational because "they were certain the ads would perform, because their monetization per search was the best in the industry" (ep05:92). The distribution logic: "whoever monetizes each search best can pay the most for distribution" (ep05:96). The results: AOL made $35M in H2 2002 alone and $200M in 2003, "blowing through the guarantee" (ep05:94, 99-102). The chapter's follow-up rule: a bet like this is rational "when your monetization per unit is provably the best in the industry" (ep05:170).

### Q16 (ep06, explain like I'm new). Explain the IBM deal: what Microsoft paid, what it got, and how IBM's price sheet sold DOS for them.

**Answer.** Microsoft bought QDOS for "about $75,000" total and turned it into DOS (ep06:77). IBM paid a fixed fee (the chapter cites components $775,000 + $45,000 + $310,000 with an [uncertain] flag on the total — ep06:79) with "no per-copy royalties. Every copy IBM sold paid Microsoft nothing more" (ep06:79). Crucially, Microsoft kept the right to license DOS to anyone else (ep06:79). Then IBM's own menu did the selling: Pascal $450, CP/M-86 $175, DOS $60 — "DOS was built for the machine and cheapest. IBM kept the $60 as pure margin, so its incentives pointed customers at DOS" (ep06:81, 88). Ben calls it "arguably the single best business negotiation of all time" (ep06:84).

### Q17 (ep06, numerical). At the 1986 IPO Gates owned 49%, Allen 28%, Ballmer 7.5%, TVI ~6% (ep06:133). What did everyone else hold combined?

**Answer.** 49 + 28 + 7.5 + 6 = 90.5%. Everyone else held 100 − 90.5 = 9.5%. The chapter's point: capital efficiency bought founder control — "Owning 49 percent at IPO meant Gates could make audacious pivots no hired CEO could" (ep06:167).

### Q18 (ep06, applied). A startup is offered a fixed-fee deal, no royalties, freedom to license to all competitors, plus the partner's price menu steering buyers to its product. Apply Ben's IBM verdict: who builds the market, who taxes it, and what single belief would the incumbent need to flip?

**Answer.** "IBM builds the market. Microsoft taxed it forever" (ep06:210): Microsoft used IBM to generate demand, then used every other PC maker to capture the value — "the PC industry's profits flowed uphill to the one company with zero marginal cost" (ep06:100-109). IBM's error: "It optimized for control of the hardware and treated software as a component. The component became the platform. Never let the complement become the point of integration" (ep06:210-211). The belief to flip: software is the platform, not a component (ep06:210).

### Q19 (ep07, numerical). US and Canada ARPU went from $11 at IPO to $227 (ep07:217). Compute the multiple.

**Answer.** 227 / 11 ≈ 20.6×. Global ARPU is $44 (ep07:217). The chapter pairs this with ~$12 revenue per person across 3.3B daily actives (ep07:215) as its "monetization is insane" observation.

### Q20 (ep07, deep). Why did the Town Square→living room shift enable TikTok, and why couldn't Facebook's authenticated network stop it?

**Answer.** Social moved from "the Town Square (public, permanent, performative)" to "the living room (small, private, ephemeral)" (ep07:150). Second-order effect: "once social moves to the living room, media can divorce from social entirely. TikTok is not social media. It is media. Your graph does not matter. The AI does" (ep07:152). "Facebook's durable advantage, the authenticated network, became irrelevant to the engagement at hand. All that was left was the habit of tapping the app, and habits break" (ep07:152). The shift Meta identified created the opening Meta did not see (ep07:242-243).

### Q21 (ep07, applied). A founder faces a platform shift and must decide whether to rebuild natively and pause features for a year. Using Meta's mobile crisis, advise: which of the five breaks is existential, and what did Meta's stock do?

**Answer.** The five breaks: closed platforms, Platform dies (apps can't run inside apps), no mobile revenue (425M mobile users, "zero meaningful mobile revenue" in the S1), no code velocity (two-week App Store review), competitive reset (ep07:103-107). The existential one is #3 combined with #5: the S1 confession of 425M mobile users with no revenue (ep07:105), while single-purpose apps peeled off use cases (ep07:107). Meta's stock: IPO at $38, bottomed at $17.68 on Sept 4 2012 (down 53.5%), underwater 16 months (ep07:118) — and the turnaround came from the native rewrite plus inventing feed ads (ep07:118). (The rewrite rule also applies: "a rewrite that also adds features never ships" — ep03:129.)

### Q22 (ep08, numerical). Data center revenue went from ~$3B to over $10.5B in two years (ep08:117-123). Recompute the CAGR.

**Answer.** (10.5 / 3)^(1/2) − 1 = sqrt(3.5) − 1 ≈ 1.8708 − 1 = 87.1% per year, matching the chapter's drill answer "roughly 87% per year" (ep08:117-123; drill at ep08:216). Context: two years before, data center was ~$3B, "roughly half of gaming's ~$6B, and had been flat" (ep08:117).

### Q23 (ep08, explain like I'm new). NVIDIA "did not predict deep learning" (ep08:204). Explain to a newcomer what Jensen actually built, why, and how AlexNet turned it into a moat.

**Answer.** Jensen didn't forecast AI; he was "enamored with the idea of hardware that accelerates specific use cases" and took the inverted Field-of-Dreams view: "if we do not build it, they cannot possibly come" — the capability has to exist before anyone can ask for it (ep08:63). From 2006–2008 NVIDIA poured resources into CUDA with no clear market (ep08:63-66). Then AlexNet (2012): trained on NVIDIA GPUs with CUDA, it scored ~15% error against the old best of ~25% — "a ten-point margin in a field that measured single points" (ep08:89). The preparation met luck "only after a decade of unfunded preparation" (ep08:89). But even then the market took years to believe: the stock stayed under $5 a share 2012–2015 and didn't recover its $20B 2007 peak until 2016 — "narratives lag technology by roughly a decade" (ep08:98, 160-161).

### Q24 (ep08, applied). You are a well-funded competitor with unlimited money but only 3 years. Using the CUDA math, explain why money alone can't reproduce the moat in that window.

**Answer.** Because "catching up is not a money problem. It is a time problem" (ep10:208). The moat is "denominated in 3 million developers' code and 1,100 engineers' accumulated software, not in transistor counts, which competitors can match" (ep08:166, 226). Even with unlimited budget "you cannot hire 10,000 experienced GPU-software engineers instantly, and their work compounds" (ep10:208). The full replication test adds: CoWoS packaging is 10–15% of TSMC's total capacity, custom-built, years to add, largely reserved by NVIDIA; then reproduce ~10,000 person-years of CUDA-quality software "costing billions"; then "survive the years that takes while NVIDIA keeps shipping" (ep10:157). "Good luck getting that" (ep10:157).

### Q25 (ep09, numerical). NVIDIA doubled performance-per-dollar every 6 months; competitors every 24 (ep09:188, 211). After 4 years, how many times ahead is NVIDIA?

**Answer.** 4 years = 8 NVIDIA cycles, 2 competitor cycles. 2^8 / 2^2 = 256 / 4 = 64× ahead (ep09:188, 211). The ascii figure shows it visually: NVIDIA ships 9 times while competitors ship 3 (ep09:78-80).

### Q26 (ep09, deep). NV1 bet on quadrilaterals while the industry standardized on triangles (ep09:55). Why did the "cleverer" primitive lose? Connect the three failures.

**Answer.** (1) The primitive: "a triangle is the fewest vertices in a closed shape, the cheapest way to describe a surface" (ep09:55); Microsoft's ecosystem standardized on the triangle paradigm (ep09:55). (2) Memory economics: NVIDIA's tight-memory chips cost "about $200 in components per chip, while competitors with more generous memory designs paid about $50" (ep09:56) as Moore's law dropped memory prices. (3) The customer: Sega, their one big customer, "gets cold feet about quadrilaterals" and switched horses in 1996 (ep09:55). "Everything is going wrong at once: wrong primitive, wrong memory economics, one customer walking away" (ep09:56). Lesson: "Bet on the industry standard's primitive, not your own cleverer one" (ep09:169).

### Q27 (ep10, numerical). A DGX H100 holds 8× $40K GPUs ($320K) and sells from $500K (ep10:105, 113-115). Compute the implied integration margin and explain why customers pay it.

**Answer.** ($500K − $320K) / $500K = 36%, "about $180,000 of extra margin from selling the solution" (ep10:105, 115; drill confirms 36% at ep10:265). Customers pay it because "the bundle removes integration risk and every in-house developer is productive immediately" (ep10:208) — "buy the solution and every developer you already have runs CUDA on day one" (ep10:111).

### Q28 (ep10, deep). The strongest bear case is the inference shift (ep10:190). Explain the mechanism and name the leading indicator that would prove it right.

**Answer.** The mechanism: "Models get trained once, then run forever. If compute shifts from training (where NVIDIA is dominant) to inference (where it is less differentiated), the moat narrows" (ep10:190). In the chapter's Q&A: "training is a one-time cost per model generation. Inference is the perpetual workload, and NVIDIA is less differentiated there. It would be proven right by inference revenue overtaking training revenue while NVIDIA's share of inference falls" (ep10:223). Leading indicator: "watch hyperscalers' custom inference silicon (Google TPUs, AWS Trainium)" (ep10:223).

### Q29 (ep11, numerical). Recompute the 1,000-GPU Fermi cluster from the DGX specs: number of boxes, hardware cost, and facility power (ep11:111-115).

**Answer.** Boxes: 1,000 GPUs / 8 per DGX = 125 DGX H100 boxes (ep11:111-114). Hardware: 125 × $500,000 = $62.5M before networking (ep11:113). Power: 125 × 10.2 kW = 1.275 MW compute alone (ep11:114); add ~30% for networking/cooling/overhead → ~1.7 MW facility (ep11:115). ("1.7 megawatts is a small factory's power draw" — ep11:116.)

### Q30 (ep11, applied). A model needs 1 TB of weights. H100s have 80 GB HBM3 each; a DGX H100 has 640 GB total; NVLink is 900 GB/s intra-node and InfiniBand 400 Gb/s inter-node (ep11:54, 79, 95-96). How many GPUs minimum, does it fit one DGX, and which interconnect do you need?

**Answer.** Minimum GPUs: 1 TB / 80 GB = 12.5 → 13 GPUs (ep11:54). One DGX holds 640 GB total — under 1 TB — so it does NOT fit in one box (ep11:79). Therefore you need at least 2 DGX nodes, i.e., scale-out over InfiniBand (400 Gb/s per port), not just NVLink scale-up (ep11:95-96, 147). The chapter's own Q2 answer states the logic: scale-up "makes 8 GPUs behave as one giant GPU... when the model or batch does not fit on eight cards" you need scale-out (ep11:147).

---

## "Think it yourself" drill verification

Every drill with an expected answer was recomputed against the chapter's numbers. All PASS. Drills without stated answers (journals, argue-both-sides, observe, unaided) introduce no new factual claims and are derivable from their chapters.

| Chapter | Drill | Expected answer in chapter | Recomputation | Verdict |
|---|---|---|---|---|
| ep01:307 | Fermi: 1 frame/hour vs 30 fps | 108,000 frames/hour; ~100,000× slower | 30×60×60 = 108,000; 108,000/1 = 108,000 | PASS |
| ep02:256 | Fermi: $20B fab, $15–20K/wafer | 1M wafers to pay for itself | 20,000,000,000 / 20,000 = 1,000,000 | PASS |
| ep03:267 | Fermi: 3.3B users × $1; "twice as profitable" | Inputs at ep03:166, 174 | 3.3B × $1 = $3.3B; tax = half of potential | PASS |
| ep04:274 | Fermi: ~1Q tokens/month; $140B earnings | Inputs at ep04:186, 174 | $0.001/1000 tok = $1e-6/tok → $1B/month inference | PASS |
| ep05:281 | Fermi: 10K q/day → 14M/day, ~800 days | 1,400×; ~0.9%/day | 14M/10K = 1,400; 1400^(1/800) ≈ 1.0091 | PASS |
| ep06:268 | Fermi: MS $25M/$98M vs Compaq $111M | Inputs at ep06:100, 98 | margins are drill-supplied; inputs correct | PASS |
| ep07:284 | Fermi: 230M views/day, 5M users | 46 views/user/day | 230/5 = 46 | PASS |
| ep08:216 | Guided: $3B → $10.5B, 2 yrs | ~87%/yr | (10.5/3)^0.5 − 1 = 87.1% | PASS |
| ep09:188 | Guided: 6-mo vs 24-mo doubling, 4 yrs | 64× | 2^8/2^2 = 256/4 = 64 | PASS |
| ep10:265 | Compute: DGX $500K, 8×$40K; cloud $37K/mo on ~$120K build | 36%; ~3.2 months | (500−320)/500 = 36%; 120/37 ≈ 3.24 | PASS |
| ep11:196 | Compute: 32 petaFLOPS, 10.2 kW | ≈3.1 TFLOPS/W | 32e15/10,200 = 3.14e12 | PASS |
| ep11:197 | Fermi: $100/hr per 8 H100s, 1,000 GPUs, 30 days | $9M | 125×100×24×30 = 9,000,000 | PASS |

---

## Flags (not failures)

Two cross-chapter inconsistencies were found during verification. Neither breaks any exam question (each question cites a single chapter), but they should be reconciled:

1. **Mellanox acquisition year.** ep01:155 says "In 2019 Nvidia bought Mellanox... for about 7 billion dollars." ep08:115 says "In 2020, NVIDIA acquires Mellanox... for about $7 billion." The two chapters disagree by one year.
2. **RIVA 128 emulator speed.** ep01:47 says "It rendered about one frame per hour." ep09:68 says the Riva 128 was debugged "on an emulator running one frame every 30 seconds." These differ by 120× (108,000× slower vs 900× slower relative to 30 fps). Q1 above cites ep01 only.

## Final verdict

**30/30 — E1 PASS.** All 30 questions are answered wholly from chapter text with chapter:line citations. All "Think it yourself" drills with expected answers recompute correctly. Two reconciliation flags are listed above for the parent to pass back to the build side.
