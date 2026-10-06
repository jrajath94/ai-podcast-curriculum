# AUDIT REPORT — You Are Not So Smart track (David McRaney)
Auditor: subagent 5d87f1cc. Date: 2026-10-06. Verbatim-first reading: MASTER_BRIEF.md, REJECTIONS.md, TRACK_AUDITOR_BRIEF.md, VISUAL_SYSTEM_GENERIC.md. All 10 chapters read in full (ep01–ep10), index.md, cheatsheet.md, _coverage.md, and all 10 transcripts consulted. Spot-checks against transcripts done for ep01 (Dunning-Kruger), ep07 (Deep Canvassing), ep08 (QAnon); quote/number verification across all 10. ste_check.py run on all chapters + cheatsheet + index: 0 hard failures. Primary episode/transcript URLs verified live (ep01 pair fetched, both resolve and match local transcripts). Chapter dates match research/episodes.json publish_date (RSS feed) exactly.

Gates used are the parent's adapted G1–G9.

## Verdict summary

| Gate | Pass | Fail |
|---|---|---|
| G1 fidelity (reading = listening) | 10/10 | 0 |
| G2 depth + conciseness (zero-prereq, one-sitting, no repeats) | 10/10 | 0 |
| G3 numbers (transcript-sourced or computed, arithmetic recomputed) | 9/10 | ep07 (1 item) |
| G4 figures (state-change-only, shells, ladder, captions, no blank cells) | 10/10 | 0 |
| G5 memory aids | 10/10 | 0 |
| G6 for-life format (imbibe + think-it-yourself + skills) | 10/10 | 0 |
| G7 STE100 | 10/10 | 0 |
| G8 honesty ([uncertain], no invented quotes/numbers, episode-vs-synthesis) | 10/10 | 0 |
| G9 thinking arc | 10/10 | 0 |

One hard FAIL item total: ep07 G3 (Fermi drill arithmetic). Everything else passes. Minor notes listed per chapter below; none rise to FAIL.

## Per-chapter verdicts

### ep01 Dunning-Kruger — PASS all gates
- G1: PASS. Spot-checked 10 items vs transcript yanss-036: fighting-game tournament (8–10 friends, lost both matches), small pond (bottom 20%), "relatively meagre, to often non-existent", buffers (30%, up to 100%, concrete x8), "it takes a village... to know themselves", Wheeler "But I wore the juice", mediocrity enablers, American Idol/Jeopardy. All present. Coverage-map lines sampled (ep01:30, :95) verified.
- G3: buffer arithmetic recomputed: 10 weeks x1.3 = 13, x2 = 20, 100 tons x8 = 800. Correct. Ehrlinger 8/10 vs 6/10 matches transcript.
- G8: quotes verified verbatim or faithfully paraphrased ("wore the juice" verbatim; "takes a village" paraphrased, meaning preserved).
- Minor: Jeopardy-uncle toy (30/10/3/7/23) is invented arithmetic but labeled "original toy, from episode claims" in the caption. Acceptable; toy is internally consistent and the "go negative" gloss matches the transcript's "going to make us losers".

### ep02 Naive Realism — PASS all gates
- G1: PASS. Sweet-spot trick, "too" test, Einstein/"Reality is an illusion", umwelt, Russell stone, oak-vs-bigot, Pronin blind spot, Cheney, Lord-Ross-Lepper, Kahneman "15 IQ points", end-of-history illusion, Ireland exercise, Douglass, Lincoln line — all in transcript, all in chapter.
- G3: no computed arithmetic; transcript numbers reproduced faithfully.
- G8: three signature quotes verified verbatim ("If you thought it sensible to be more idealistic...", "What I have never experienced in 40 years...", "Every time a hypothesis fails, I gain 15 IQ points").

### ep03 Belief — PASS all gates
- G1: PASS. Mackay watermelon teeth / "tell the time", Haidt sacred rule, Gaza heat policy, hero maker / "playing David in the story of David and Goliath", ~1,000 genes via fearfulness, rudeness loop, Monckton full life story (Harrow, empire, KGB playbook), "entire sense of self would fall to pieces", 140 characters, Bushido code, Dadaab. All verified in transcript.
- G8: [uncertain] on the 140-character limit (platform changed since 2014) — honest and correct. willstorr.com link marked [uncertain].
- G3: Fermi drill (20 net variants at 1% = 20-point shift) recomputed correct.

### ep04 Arguing — PASS all gates
- G1: PASS. Mercier/Sperber 2011, trust bottlenecks, two meanings of arguing, NYT half-quote, mushroom rule, restaurant division-of-labor, Hsee chocolate, disjunction coin flip ($200/$100), Hawaii trip, sunk-cost reframe, bat-and-ball, 5–10 minute conversion, abolition, printing-press astrology panic. All verified.
- G3: EV recomputed: 0.5x200 - 0.5x100 = +$50. Correct. Bat-and-ball: 0.05+1.05=1.10. Correct. Fermi (5x12=60) correct.
- G8: "If everybody was deaf, people would stop talking" verified verbatim.

### ep05 Bayes — PASS all gates
- G1: PASS. Grayscale/job hunt, credence/2-to-1 odds, trick coin, hair/Jane, car crash "at least a little", Bob-and-Amy, breast cancer, plumber base rates, fallacy of gray, Bayes net/Harvard legacy/explaining away, Anna cascade, source-check. All verified.
- G3: breast-cancer arithmetic recomputed: 0.0009/0.1008 = 0.0089 ≈ 0.9%. Correct. Drill (99% test, 1/10,000: 1 of 101) correct. Fermi (3x52=156, x2=312, /20≈15) correct.
- G8: "I would accept 2 to 1 odds" and "at least a little bit" verified verbatim.

### ep06 Search Effect — PASS all gates
- G1: PASS. Glove/paper, old couple, biologist/chemist/statistician, 9 experiments, moon/glass/dimples induction, weather self-assessment, brain slider, "without outside sources", filtered useless-search, library vs internet, presidency/voting booth, "rising exponentially", contractor's buffer. All verified.
- G8: "You erroneously include knowledge stored outside of your own head as your own" verified verbatim.

### ep07 Deep Canvassing — FAIL G3 (1 item); PASS all other gates
- G1: PASS. Prop 8 (52%), "Let's just go ask", $83M/1%, 12,000+ conversations (transcript: "more than 12 000 conversations"), Broockman/Kalla fraud + retraction, Miami restart, recycling placebo, 3d/3w/6w/3mo, 0.25–0.3 SD, ~10/100, 70% finish, "puddles", 1.5-hour training, Petty/Cacioppo, analogic perspective taking, tree-bark stage, Ross 40-year echo. All verified.
- G3: **FAIL — Think-it-yourself drill 2 (ep07.md:211) arithmetic is wrong.** The drill: "0.25 SD effect, tolerance scale SD 20 points, election needs a 2-point swing. How many treated voters per 100 deliver the swing?" The chapter's answer: "0.25 times 20 is 5 points per treated voter on average. 2 points over 100 voters needs 40 point-voters of movement, about 8 treated voters per 100 at full effect." Recomputed: 5 points per treated voter is right, but 2 points x 100 voters = 200 point-voters of movement (not 40), and 200/5 = 40 treated voters per 100 (not 8). The chapter appears to have multiplied 2 x 20 = 40 (swing times SD, dimensionally wrong) and divided 40/5 = 8. Both the intermediate (40) and final (8) numbers are wrong; the correct answer is 40 treated voters per 100. Passing fix: replace "40 point-voters of movement, about 8 treated voters per 100" with "200 point-voters of movement, about 40 treated voters per 100 at full effect". (The drill's first clause, 0.25 SD ≈ 50th→60th percentile, is correct: Φ(0.25)=0.5987.) Drill 1 (500 open / 350 complete / 35 change; 28,600 knocks per 1,000 converts) recomputed correct. All trial numbers (0.25–0.3 SD, 10/100, 3 months) match transcript.
- G8: PASS. The 9-month flag is handled exactly right: inline [Note] ("The trial's published measurement window was 3 months, so 3 months is the verified figure and 9 months is her characterization") plus a Q&A follow-up naming "the honest uncertainty". Builder gap 2 closed.
- Minor: figure-audit row u04 says "Figure 4 (implied in text)" while the figure exists below the table — sloppy audit cell, not a missing figure.

### ep08 QAnon — PASS all gates
- G1: PASS. Redirect (believers not beliefs), narrative-vs-theory, three-question test wording, D&D analogy, hourglass, fandom/Alien, content-vs-quality motives, three base motives, logic loop, Kate Starbird information voids, distrust descent, thermometer 24/100 (Castro 22), 5–7%, dark triad, rallies 40–50, bar metaphor, CSIS 22/139/34/37, FBI 2019 bulletin, alert 5→50–100/day, NYT 50→750/year, 45% JFK / half cannot name plotter. All verified against transcript.
- G3: drill answers recomputed: 0.45x0.5=22.5% correct; hashtag Fermi internally consistent.
- G8: all numbers match transcript; no invented quotes found.

### ep09 Tribal Psychology — PASS all gates
- G1: PASS. Tajfel dots ($4/$3 vs $5/$5), Brewer inclusion/exclusion, Pew 92/94, 20% hardcore, 27/36 threat, party-vs-policy anger, Cohen welfare flip (100%), Linden expert revocation, gun-control math bending, Iraq/Gaines, Hastorf-Cantril football film (90% Dartmouth), Comey 2017, information-deficit-model history, post-truth 2,000%, HPV (75%, 3,000 deaths) vs HBV (95%), science curiosity, Mason's humanizing drill, fast-food analogy. All verified.
- G3: Fermi drills recomputed correct (10,000 refusers; 13,500–18,000 threat-perceivers; $4/$3 sacrifice accounting correct).

### ep10 The Self — PASS all gates
- G1: PASS. "An experience that is not what it seems", Libet half-second, tennis-ball blind spots, 2–3 blind hours, mirror saccade test, duplicator/hamster (5-year-olds, name strengthens), Parfit/Star Trek, I-vs-me (James), infantile amnesia (~2), East/West narration, longest childhood, reflected self/ostracism, "not myself"/wine-blame, Bronnie Ware #1 regret (transcript line 166 — present, initial grep missed it on "aware" substring), materialism/dementia, "meat machine" (Minsky), complex AI, twins ~50%, nightly rebuild/dissonance patches. All verified.
- G9: the track close ("the debugger is the deepest bug", three operating rules) turns every prior instrument on its holder. Drills are the hardest in the track (no scaffolding, falsification design, track-wide synthesis) — matches the parent's "hardest yet" bar.

## Gate-by-gate notes

- G1: coverage map (_coverage.md) sampled at 7 chapter:line mappings — all land on the claimed content. Deliberate omissions (intros/outros, monologues, book plugs, ad breaks, ep211 HBO clips/Pizzagate detail) are non-claims or disclosed; nothing important missing. Builder gap 1 (8/10 interview-only transcripts) verified true and disclosed in index.md + _coverage.md; no monologue content is claimed as episode content.
- G2: every technical term spot-checked (umwelt, disjunction effect, credence, Bayes net, transactive memory, affective polarization, analogic perspective taking, minimal group paradigm, double curse, keystone) is defined at first body use. No paragraph restates earlier teaching without new information; cross-chapter links (ep07 "Ross echo", ep10 track recap) are explicit chaining, not repetition. One track-level nit: front-matter summaries use terms (double curse, transactive memory, Bayes net, affective polarization, keystone, hourglass) before the body's Definition lines. Minor; the teaching point defines each.
- G4: 5 figures per chapter in body (Figures 1–4 lesson plates + Figure 5 chapter plate), all table-medium — the first ladder rung for comparison claims, defensible throughout. Every figure shows before/after with a one-rule row; captions name "AI Podcast Curriculum" + episode + date + shell + source. Audit tables have no blank cells. Two cosmetic notes: shell numbering is not strictly sequential within chapters (e.g. ep01: Shell 1, 3, 2, 3, 4); ep08's hourglass could arguably use mermaid, but the stage table passes the four tests.
- G5: all 10 chapters have Memory aids with one-line rules, never-confuse pairs, and trap cards. Cheatsheet compresses every chapter's numbers faithfully (spot-checked ep01, ep05, ep07, ep08 sections).
- G6: all 10 chapters have "## How to imbibe this" (this-week actions, catch-yourself tallies, per-idea behavior changes, monthly review), "## Think it yourself" (6 brain-first drills, "done WITHOUT AI", answers shown early, scaffolding removed by ep08–ep10), and "## Skills you can now use". Drill difficulty escalates across the track as index.md promises.
- G7: ste_check.py: 0 hard failures on all 10 chapters + cheatsheet + index. No em dashes, no semicolons in prose, zero banned filler words/phrases (grep). One tension noted: ep07:90 and cheatsheet:121 keep the verbatim transcript contraction "that's" inside a quoted sentence ("there is nothing you can tell this person that's going to change their mind"). Verbatim per G5's quote rule; the builder's own paraphrase policy would prefer "that will". Minor.
- G8: [uncertain] used correctly (ep03 140-char note, paper/book/secondary links in Go deeper). Episode-vs-synthesis separated: invented toys labeled "original toy" in captions, drills quarantined in "Think it yourself", applied Q&As in Q&A. ~12 signature quotes checked vs transcripts: all verbatim or meaning-preserving paraphrases; zero invented quotes. Go-deeper primary episode + transcript links verified live (ep01 pair fetched, resolve, match local transcripts); chapter dates match episodes.json RSS publish_dates exactly (URL-slug dates differ slightly — WordPress page date vs RSS pubDate, not an error).
- G9: index.md documents the arc (diagnosis eps 1–4 → repair ep5 → new hole ep6 → field manual ep7 → social machine eps 8–9 → deepest cut ep10) and every chapter's "Why this episode matters" chains to prior chapters. This is the debugging-self-delusion step; drills are the hardest yet (ep10: design a falsification experiment, define "myself" without circularity, derive the track's single best daily practice).

## Builder's honest gaps — verification
1. 8/10 transcripts interview-only (monologues excluded): CONFIRMED TRUE, disclosed in index.md and _coverage.md. No chapter claims monologue content. No action.
2. ep07 effect-duration flag (9 months claimed, 3-month trial): HANDLED. Explicit [Note] at ep07:66 + Q&A follow-up naming the honest uncertainty. No action.
3. Go-deeper links not fully verified: PARTIALLY OPEN. Primary episode/transcript links verified live; secondary links carry honest [uncertain] markers; the 10 frontmatter audio_urls are pattern-consistent with the RSS feed but not individually fetched. Recommend a link-check pass before ship (low priority; all [uncertain]-marked).
4. Verbatim quotes paraphrased to hold STE bar: VERIFIED. ~12 quotes checked; meaning preserved everywhere, no invented quotes, verbatim where it matters.

## FAIL items (must fix before ship)
1. [ep07, ep07.md:211, G3] Think-it-yourself Fermi drill 2 answer is arithmetically wrong: "2 points over 100 voters needs 40 point-voters of movement, about 8 treated voters per 100 at full effect." Correct: 200 point-voters of movement, about 40 treated voters per 100. Fix the two numbers; the follow-up question ("what breaks first, the linearity or the turnout?") stays valid.

## Minor notes (not FAIL)
- M1 (track-wide, G2): front-matter summaries use key terms before the body's Definition lines. Consider defining on first mention even in summaries, or accept as index metadata.
- M2 (ep07, G7): verbatim "that's" contraction inside a quoted sentence (ep07:90, cheatsheet:121). Verbatim per transcript; builder policy prefers paraphrase.
- M3 (ep07, G4): figure-audit row u04 says "Figure 4 (implied in text)" though Figure 4 exists below the table. Clean the cell.
- M4 (track-wide, G4): shell numbers not strictly sequential within chapters (ep01: 1,3,2,3,4). Cosmetic.
- M5 (track-wide, G8): 10 frontmatter audio_urls not individually verified (pattern-consistent with RSS feed). Recommend a fetch pass.
