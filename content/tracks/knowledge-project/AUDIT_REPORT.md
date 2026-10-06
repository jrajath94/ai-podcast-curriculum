# AUDIT REPORT — Knowledge Project track (Shane Parrish)
**Auditor role:** adversarial track auditor. I do not fix; I fail with precision.
**Date:** 2026-10-06. **Scope:** `content/tracks/knowledge-project/` — ep01–ep10.md, index.md, cheatsheet.md, _coverage.md, against transcripts in `research/knowledge-project/transcripts/`.
**Read verbatim first:** MASTER_BRIEF.md, REJECTIONS.md, TRACK_AUDITOR_BRIEF.md, VISUAL_SYSTEM_GENERIC.md.

## Method
- Read all 10 chapters + index + cheatsheet + coverage map in full.
- G1: spot-checked 4 episodes × 8 substantive transcript items against chapters (ep01, ep02, ep06, ep09); verified _coverage.md line pointers; checked every quoted string I could against transcript text.
- G3: recomputed every arithmetic claim the chapters compute (not just repeat).
- G7: ran `ste-lint/bin/ste_check.py` on all 12 files (0 hard fails everywhere) + independent grep for contractions (case-insensitive, code blocks stripped), em/en dashes, semicolons, banned filler and phrases.
- G4: counted figures per chapter, checked caption law (project name + source + shell), figure-audit tables, medium ladder, shell discipline.
- Go-deeper links: re-verified 3 of 6 domains via curl (fs.blog 301, wikipedia 200s). YouTube video_ids not oEmbed-verified by me.

## Verdict table (per chapter per gate)

PASS* = pass with minor findings listed below. FAIL items are numbered F1–F6.

| Ch | G1 fidelity | G2 depth+concise | G3 numbers | G4 figures | G5 memory aids | G6 for-life | G7 STE100 | G8 honesty | G9 arc |
|---|---|---|---|---|---|---|---|---|---|
| ep01 | PASS* | PASS* | PASS | PASS* | PASS | PASS | PASS | PASS | PASS |
| ep02 | PASS* | PASS* | PASS | PASS* | PASS | PASS | PASS | PASS | PASS |
| ep03 | PASS (F1 false positive) | PASS | PASS | PASS | PASS | PASS* | PASS | **FAIL F1** | PASS |
| ep04 | PASS | PASS | PASS | PASS* | PASS | PASS | PASS | PASS | PASS |
| ep05 | PASS | PASS | PASS | PASS* | PASS | PASS | PASS | PASS | PASS |
| ep06 | PASS | PASS | PASS* | PASS* | PASS | PASS | PASS | PASS | PASS |
| ep07 | PASS | PASS | PASS | **FAIL F3** | PASS | PASS | **FAIL F4** | PASS* | PASS |
| ep08 | PASS | PASS | PASS | PASS* | PASS | PASS | PASS* | PASS | PASS |
| ep09 | PASS | PASS | PASS* | PASS* | PASS | PASS | PASS* | PASS* | PASS |
| ep10 | PASS | PASS | PASS | PASS* | PASS | PASS | PASS | PASS | PASS |

**Counts: 5 FAIL items across 2 chapters (ep03: F2; ep07: F3, F4). F1 was an auditor false positive — transcript verified to contain the 60% claim. F5 is a track-level G4 finding. 8 of 10 chapters have zero FAILs.**

## FAIL items

**F1 — ep03.md:137 and ep03.md:204 (G1/G3/G8). AUDITOR FALSE POSITIVE — resolved.** The auditor quoted only the first sentence of the transcript. The fix agent verified the research transcript (`yBBhd0-Os74.txt`) contains, in the sentence immediately after: "They have like 60% operating margins and they're they're duopies and and they were created by the banks." Three independent episode summaries (podcastnotes.org, citybiz.co, podcastalpha) corroborate Gurley said ~60% on this episode. The chapter's "roughly 60 percent" is a faithful paraphrase. No change made, per "do not fix what is not broken."

**F2 — ep03 (G4). Figure-sparse: 1 figure for 16 coverage claims.**
Only fig1 (derivatives mermaid) exists. No figure for: the stablecoin-vs-cards numbers table (a count/score unit — required), the Benchmark equal-partnership architecture (architecture unit — required by spec), circular deals (a move — required), the farmers-market metaphor (a merge). Builder admitted this gap; verification confirms it. Passing: add at minimum the stablecoin cost table (ACH 3 days / $25 wire / 2–2.5% cards vs USDC seconds-for-pennies — all transcript-verified numbers) and the equal-partnership before/after plate.

**F3 — ep07 (G4). Figure-sparse: 1 figure for 20 coverage claims.**
Only fig1 (five-step loop mermaid). No figure for: believability-weighted voting (a score — required), the pain button (a step loop — required), the two yous (a before/after state — required), idea meritocracy three steps. Builder admitted this gap; verification confirms it. Passing: add at minimum the believability score plate and the pain-button loop plate.

**F4 — ep07.md:190 (G7). Contraction in the builder's own voice.**
"...name it ("that's the emotional you"), and let the prefrontal you hold the pen." Not a transcript quote — the builder's phrasing. STE100 bans contractions; the other 11 contraction hits track-wide are all verified verbatim transcript quotes (see honesty notes). Passing: rewrite as "that is the emotional you".

**F5 — track-level (G4). Shell tags are decorative; the four tests are undocumented.**
Every figure carries a "Shell N" label, but shells do not sequence within a concept (ep06: Shell 2, 3, 2; ep01: Shell 2, 3, 2, 1) — no Russian-doll progression 1→5 anywhere. The figure-audit tables list claim/before/after/medium/source but never the four tests ("what does the object look like / why does the rule force that shape / what one number can the reader change / what symbol does the next page reuse"), and no figure exposes a reader-changeable number. Captions do name the project ("AI Podcast Curriculum"), the source, and the shell — that half passes. Passing: either honor the shell sequence per concept (one concept = shells 1–5 across its figures, with the symbol table filled) or drop the shell labels; document the four tests in the figure-audit tables.

## Minor findings (not FAILs)

- **G1, ep01:** transcript uses Naval's signature terms "leverage" ("a fundamental fact of leverage... our decisions getting leverage") and "specific knowledge" — the chapter covers both ideas (as "the arithmetic of the multiplier" and "your combination of DNA, development, knowledge, and desire is unique") but drops the terms. Ideas present; signature vocabulary absent. Recommend adding the terms.
- **G1, ep02:** "bitcoin" in frontmatter title/concepts, zero mentions in body. Transcript bitcoin content is marginal (Shane's recap line "chose Bitcoin in 2012-…" at v9pipH75L_E:11673; a brief "excited about Bitcoin? Yes" exchange at :12387). Title matches YouTube's real title; omission is defensible. Recommend one sentence mapping it or dropping the concept tag.
- **G2, ep01:** "Delete options instead of predicting outcomes" packs 4 increments (elimination principle + 80/70 leverage arithmetic + 10,000/500/5 funnel + asymmetric-bet definition). "Systems beat goals. Being you beats copying." packs 3 (systems-vs-goals + authenticity + founder traits). Both are topically chained; strictly they violate one-increment-per-subchapter.
- **G2, ep02:** "Observe the present from first principles" packs the election analysis + the 1980 rates bet (two full mechanisms). "The deflationary lesson and the either-way portfolio" packs deflation thesis + either-way construction + Bezos/Amazon case. "How he judges CEOs" packs virtue + mental flexibility (two distinct mechanisms).
- **G3, ep06 Q4:** "25% ± 15 → every year lands between 20% and 30%" is phrased as arithmetic implication. The transcript asserts BOTH claims ("plus or minus 15 points" AND "almost never above 30%, never once below 20%") — the tension is Collins's own, not the builder's invention. Recommend rephrasing to "the transcript gives both figures" rather than deriving one from the other.
- **G3, ep09 Q4:** "maybe 3.3-3.4" for Julie's regressed GPA; transcript/coverage say base 3.1–3.2 "nudge up". Slightly stronger than the source. Recommend "a touch above 3.1–3.2".
- **G7, ep03.md:231:** "5, The circularity check." — comma for period. Typo.
- **G7, ep08.md:205:** "with a invoice attached" — should be "an invoice".
- **G7, ep09.md:33:** opening blockquote "Put aside your intuition. do not try to form…" — lowercase "do not" after the period. Transcript has "Don't". Typo.
- **G7, cheatsheet.md:124:** "800 rejection letters, day one → in a row." — garbled; should read "first book sold on day one, then 800 rejection letters in a row" (per ep08 body).
- **G8, ep07 + ep09:** both rest on auto-generated transcripts with precise numbers (Dalio: 250%, $4,000, ~75 years, 22%; Kahneman: 50 underwriters, 10%/50%, $70,000) and carry no [uncertain] marks or blanket source note. I verified the key numbers against the transcripts, so risk is contained — but ep02's blanket-note convention ("Numbers and names below follow the transcript") should be applied uniformly.
- **G7/G8 conflict for the record:** 11 contraction hits are verified verbatim transcript quotes (Bezos "there's only one thing I ask myself" ✓; Irvine "it's a sky" ✓, "that's just Bob being Bob" — transcript ASR renders "bob of being bob", normalized faithfully ✓, "if that's the worst thing…" ✓; Greene "that's just life" ✓; Godin "It's for everybody" ✓, "It's just business" ✓; Kahneman "It's not intuitive, but it's really, really true" ✓). STE100's no-contraction rule and the verbatim-quote law collide here; the coordinator needs a standing rule (verbatim wins, or normalize quotes and mark them).
- **G4, other chapters:** ep01/ep02/ep04/ep05/ep06/ep08/ep09/ep10 have 2–4 figures covering their major claims with honest captions and ladder-correct mediums (tables for comparisons, mermaid for flows). Page-audit completeness is partial everywhere — most sections have no figure — but the spec's hard "no blank cell" rule is satisfied by the figure-audit tables. ep03/ep07 are the outliers (F2/F3).
- **Not verifiable by me:** view counts (763,971 … 29,328), episode dates/titles, "ten most-viewed" ranking claim. YouTube video_ids not oEmbed-verified.

## Gate confirmations

**G5 memory aids — PASS all 10.** Every chapter has a mnemonic (R-D-H-W, T-F-P, S-B-E, N-T-F, R-P-L, F-M-B-L-D, P-I-F, P-S-E, D-N-P-R, R-C-S), never-confuse pairs, and trap cards. No chapter ships without them.

**G6 for-life format — PASS all 10.** Every chapter has "## How to imbibe this" (5–7 concrete practices, each with an "Observable change" line — no motivational fluff found), "## Think it yourself" (6 drills), and "## Skills you can now use" (7–8 bullets). The imbibe sections are genuinely behavioral: 24-hour rule, evasion log, second-derivative habit, pain button, premortem, spec card, streak.

**G9 thinking arc — PASS all 10.** Drill difficulty was verified per chapter and follows the designed progression:
- ep01 "Guided, with answers." / ep02 "Guided drills, with answers." — answer sketches present.
- ep03 "Harder than ep02. Work without AI first." / ep04 "Harder than ep03. No worked answers this time" / ep05 "No handrails now. These are Greene-grade problems." / ep06 "The hardest set so far. Collins-grade problems." — journaling, field observation, no worked answers.
- ep07 "Near the peak of difficulty." / ep08 "The peak set." / ep09 "The final and hardest set of the track." / ep10 "The track's final set. Comprehensive." + Drill 6 track synthesis — unaided memos, noise audits, premortems, full synthesis. Matches the index's stated arc.

**G1 spot-check log (4 episodes × 8 items, all found in chapters):**
- ep01 (Naval): latchkey-kid library ✓, junk-food ladder ✓, top-0.1% readers ✓, 80-vs-70 judgment arithmetic ✓, debug-mode toothbrush ✓, Buffett best/worst-lover test ✓, jealousy wholesale swap ✓, macro-junk/micro-law ✓, heat-death 70B years ✓. Quotes checked: "vision without execution is [a] hallucination", "hot coal", "three generations nobody cares" — faithful.
- ep02 (Chamath): lying-as-protection ✓, organ rejection (transcript line 1969) ✓, Mona Simpson NYT obituary (lines 889–893) ✓, "Oh, wow" repetition (lines 907–917) ✓, three oh-wow moments ✓, 1980 15–16% rates bet ("15% will fall to zero, earlier than 15% will grow to 50%" — faithful) ✓, triangular offices (12 transcript mentions) ✓, dental-floss 90–95% ✓, asymptote 1–1.5 orders of magnitude ✓.
- ep06 (Collins): 6,000 years combined history ✓, 292-to-1 quiz ("two hundred ninety two one", 25±15 vs 45±115, ±300/−200 — faithful) ✓, "multiplying by zero" ✓, who luck ✓, Deb Gustafson ✓, Digital Research vs Microsoft ✓, "change every what decision into a who decision" ✓, iPod three-sentences-in-10-K ✓, Kroger/A&P brutal facts ✓.
- ep09 (Kahneman): "try to be reliable, not valid… You be reliable" ✓, "close your eyes" ✓, 50 underwriters / expected 10% / actual ~50% ✓, Gary Klein premortem ✓, Julie 90th-%ile → ~3.7 vs base 3.1–3.2 ✓, Lewin board-and-springs (name identified by builder; transcript has only "guru and hero") ✓, Deaton ~$70,000 plateau ✓, "this is idiocy, statistically completely meaningless" ✓.

**G3 recomputation log:** ep01 200→20 = 10% ✓; 10% × $1B = $100M ✓. ep02 freedom-fund drill: S=5,000 → A=60,000 → F=25×60,000=1,500,000 ✓. ep06: −50% then +100% to recover ✓. ep09: scatter = difference/average ✓ (method as stated). ep10: 650 × 15 = 9,750M ≈ $10B ✓. ep03: $5B Anthropic, $25 wire, 60–70% Argentina, Faster Payments 20 years, Amazon $2–3B / Uber ~$15B losses — all transcript-verified ✓. ep05: ~5,000 Napoleon pages, ~2M US copies ("inching up more towards 2 million") ✓. ep07: 250% of capital, $4,000 from dad ✓. ep08: 7,500-post streak AND 7,000-post corpus — both in transcript, distinct claims ✓.

## E1 — 20-question exam (answers from chapter text only)

1. (ep01) Naval estimates he skips what fraction of most books, and what is his test for dropping a book fast? — Two thirds; drop it if the author makes a claim he knows is false (e.g. "thermodynamics is not true").
2. (ep01) In the wholesale-swap jealousy test, what exactly must you accept? — The entire person: body, money, personality, reactions, desires, family, anxiety, self-image, 24/7. No cherry-picking.
3. (ep02) What are the two paths, and which toolkit belongs to which? — Path to freedom: financial, teachable (earn, accumulate 5–20 years, community research). Path to happiness: internal, personal, trial and error. Never swap the toolkits.
4. (ep02) What was Chamath's first-principles rates bet, and what portfolio follows from it now? — 1980: 15–16% falls to zero before rising to 50 (correct 40 years). Now near zero: build the either-way portfolio (wins at minus 5 or plus 5).
5. (ep03) What is a second-derivative effect, per the dating-site story? — A consequence of a consequence: longer profiles raised engagement (1st), but months later conversion fell because informed browsers converted less (2nd).
6. (ep03) What is a circular deal, and why does it delay correction? — A cloud provider gives a lab ~$5B that the lab spends back on the provider's cloud; without the gift the spending would not happen. It inflates both sides' growth and removes the justification step, so weak competitors survive longer.
7. (ep04) What are the three columns of the trichotomy of control, and where does anxiety live? — Can control (values, goals, responses), cannot control (asteroid), partial control. Anxiety is attention parked in column three.
8. (ep04) What are the two passing conditions of the five-second anger reframe? — Find a successful workaround to the setback, and do not lose control while working around it.
9. (ep05) Describe the note-card pipeline in order. — Wide reading → margin marks → weeks later, handwritten theme cards → thousands of cards → themes emerge (80→48) → deep dive per story.
10. (ep05) What converts dead time to live time, using the Burger King shift? — Ownership: the same shift plus a plan (quit in a year, save, night school) and study (read Nietzsche on break, question 2 a.m. customers). You own only time (~85 years).
11. (ep06) What does "one 3 multiplies the whole machine by zero" mean? — In a flywheel, execution scores per link do not average: one link at 3/10 multiplies all links by zero because of the linkages.
12. (ep06) Why is the word "consecutive" the mechanism of the 20-mile march? — A never-miss commitment changes today's decisions: you cannot maximize this year in ways that guarantee a miss in year 7 or 12, so the streak forces investing ahead of disruption.
13. (ep07) What are the three steps of the idea meritocracy, and why do the two alternatives fail? — Honest thoughts on the table → thoughtful disagreement → fair tie-breaking. Autocracy fails (no ownership, boss may be wrong); democracy fails (ignores believability).
14. (ep07) What are Dalio's five steps, in order? — Audacious goals → identify problems, do not tolerate them → diagnose root cause → design the change → do it. Pain + reflection = progress.
15. (ep08) What is the smallest-viable-audience test, and what does "for everyone" hide? — Would they miss it if it were gone? "For everyone" is a hiding place: you can never fail because "everyone has not found it yet."
16. (ep08) What is quality, per Deming, and what was Lexus's original spec? — Quality = meets spec. Lexus's spec: one standard deviation better than Mercedes.
17. (ep09) What is the delay-intuition procedure, in order? — Break the decision into aspects, score each separately, assemble the whole profile, and only then let intuition speak.
18. (ep09) In the Julie example, what is the intuitive prediction, the statistical correction, and the error's name? — Intuitive: ~90th-%ile GPA (~3.7). Correct: base rate 3.1–3.2, nudge up. Error: non-regressive prediction.
19. (ep10) What was Marks's two-question 2008 analysis, and why was it a forced move? — Q1: does the system melt down (unanalyzable; preparing for it ruins all other cases). Q2: invest or abdicate. Invest + meltdown = irrelevant; skip + survival = abdicated duty. So invest: 15 weeks × $650M ≈ $10B.
20. (ep10) State second-level thinking as the chapter's textbook example. — First level: "great company, buy." Second level: "great company, but priced for perfection — optimism is already in the price, sell when truth comes out."

All 20 answered from chapter text alone. E1: PASS.

## Auditor's bottom line
The track is strong: 8 of 10 chapters pass every gate, fidelity to transcripts is high (I verified quotes, numbers, and arithmetic against the source text, including resolving the builder's flagged paraphrase/ASR risks in their favor), the drill arc genuinely progresses guided → journaling → unaided, and every required section exists in every chapter. The FAILs are concentrated and fixable: one unsourced number repeated twice (ep03 60% margins), two figure-sparse chapters (ep03, ep07 — both already admitted by the builder), one contraction in the builder's own voice (ep07), and track-level shell/four-test discipline that is currently decorative. Fix F1–F5 and the four typos, and the track clears.
