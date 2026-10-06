# AUDIT REPORT — Clearer Thinking track (Spencer Greenberg)
**Auditor:** subagent 01a510d8 (adversarial, no-fix mandate)
**Date:** 2026-10-06
**Scope:** `content/tracks/clearer-thinking/` — ep01.md–ep10.md, index.md, cheatsheet.md, _coverage.md, against adapted G1–G9 + figure law + E1 exam gate.
**Method:** Read all 10 chapters fully. Spot-checked 24 substantive claims (8 each) against transcripts ep02 (`a8qiJckz-8o`), ep06 (`TFk_Y3Eg29U`), ep09 (`GJXK-bbitrw`) — all 24 verified present and accurate. Target-checked disputed items in ep01, ep04, ep08 transcripts. Recomputed all chapter arithmetic. Ran style greps (em dash, semicolon, contraction, banned filler). Verified all 13 go-deeper links live (12 × HTTP 200; 1 dead). Note: transcripts are faster-whisper base.en renders of the official MP3s; "premortum", "Redloss", "Parford", "Vivekis", "reading priorities", "Carlson" are transcription errors the chapters handle with [uncertain] flags or correct spellings — all honest.

## Verdict

**15 chapter-gate FAILs out of 90 (75 PASS).** Three are material fidelity failures that misstate the episodes (ep01 cost anchor, ep04 premortem, ep08 sacred money). Four are visual-system mermaid violations. Six are non-verbatim `video_title` frontmatter. One is a banned-filler hit in the cheatsheet. One is a dead go-deeper link. The track is structurally strong — every chapter has all required sections, 8 Q&As, memory aids, concrete imbibing plans, brain-first drills — but it does **not** pass as-is.

## Per-chapter per-gate results

| Ch | G1 fidelity | G2 depth+concise | G3 numbers | G4 figures | G5 memory aids | G6 for-life | G7 style | G8 honesty | G9 arc |
|---|---|---|---|---|---|---|---|---|---|
| ep01 | **FAIL** | PASS | **FAIL** | PASS¹ | PASS | PASS | PASS | PASS | PASS |
| ep02 | PASS | PASS | PASS | **FAIL** | PASS | PASS | PASS | **FAIL** | PASS |
| ep03 | PASS | PASS² | PASS | PASS | PASS | PASS | PASS | **FAIL** | PASS |
| ep04 | **FAIL** | PASS² | PASS | PASS | PASS | PASS | PASS | **FAIL** | PASS |
| ep05 | PASS | PASS³ | PASS | PASS | PASS | PASS | PASS | **FAIL** | PASS |
| ep06 | PASS | PASS | PASS | PASS | PASS | PASS | PASS | **FAIL** | PASS |
| ep07 | PASS | PASS | PASS | PASS | PASS | PASS | PASS | **FAIL** | PASS |
| ep08 | **FAIL** | PASS | PASS | **FAIL** | PASS | PASS | PASS | **FAIL** | PASS |
| ep09 | PASS | PASS | PASS | **FAIL** | PASS | PASS | PASS | PASS | PASS |
| ep10 | PASS | PASS | PASS | **FAIL** | PASS | PASS | PASS | PASS | PASS |
| index | — | — | — | — | — | — | PASS | PASS | PASS⁴ |
| cheatsheet | — | — | — | — | — | — | **FAIL** | — | — |

¹ Track-wide: chapter plates are prose descriptions, not figures (see F-C1).
² Two-idea subchapters noted (see N-1). ³ "phronesis" undefined (see N-2). ⁴ Arc stated; progression asserted not demonstrated (see N-3).

## Critical findings (FAIL items)

### F-1. ep01.md:83 — review-cost anchor contradicts the episode (G1, G3) — MATERIAL
- **Location:** ep01.md:83 (also :214, :219, :255, :293, :315; cheatsheet.md:20; drill answer ep01:277).
- **Gate:** G1 fidelity, G3 numbers.
- **What's wrong:** Chapter: "Matuschak estimates each review at 10 to 15 seconds. Five exposures at 12 seconds each is about one minute of total practice time per item." Transcript (`bgsKaGGnIws`): "after maybe only four exposures you only need to see this thing once a year. **So for a total of maybe 10 to 15 seconds of practice time** you can really durably and reliably remember [that item] for a year or years to come." The episode's 10–15 seconds is the **total** per item, not per review. The chapter inflates the episode's cost claim ~4–6× and builds the entire cost anchor on it (memory aid "one minute per idea per year", Figure 4, chapter plate "300 prompts × 1 minute/year = 5 hours/year", drill 1's Fermi answer).
- **What passing looks like:** Cost anchor = 10–15 seconds total per item per year. All downstream arithmetic (Figure 4 table, memory aids, drill 1 answer "300 minutes = 5 hours", chapter plate) recomputed from the episode's number, or the deviation explicitly marked as builder synthesis.

### F-2. ep04.md:109-113 — the premortem section is not what the episode discussed (G1, G8) — MATERIAL
- **Location:** ep04.md:109-113 (also summary :9, concepts :16, :131, Q&A :141, :160, memory aids :182, imbibing :199, :228, drill :220, chapter plate :261).
- **Gate:** G1 fidelity, G8 honesty (episode-vs-synthesis not separated).
- **What's wrong:** Chapter presents Gary Klein's **team** premortem as "the episode's most portable protocol": "Before a project launches, gather the team and announce: it is a year later, the project failed disastrously. Everyone now writes down why it failed." plus "prospective hindsight" theory. The transcript contains only a brief **individual-judgment** exercise (rendered "premortum"): Spencer proposes imagining a single judgment turns out bad, asking the most likely explanation, adjusting, and averaging with the original — Kahneman confirms it is "about one third as good as asking somebody else" (the crowd-within). No team ritual, no "year later", no prospective-hindsight framing appears in the episode. The chapter imported book content and attributed it to the episode.
- **What passing looks like:** Replace the section with what the episode actually contains: the individual "premortum" + crowd-within averaging procedure, attributed to Spencer's proposal with Kahneman's confirmation. The Klein team premortem may stay only if explicitly labeled as synthesis from outside the episode.

### F-3. ep04.md:39 — judges ±4 years overstates the episode statistic (G8)
- **Location:** ep04.md:39 (also memory aids :182, cheatsheet.md:61).
- **Gate:** G8 honesty.
- **What's wrong:** Chapter: "individual judges' sentences scattered plus or minus 4 years around that average... Sentences ranging from about 3 years to about 11." Transcript (`bEiQw3Mk0rI`): "if you take a crime with the average sentence [of] seven years, and you take two judges at random, the difference that you would expect to find is about four years." The episode's statistic is the **expected pairwise difference** (~4 years), not ±4 around the mean; the "3 to 11" range is not in the episode.
- **What passing looks like:** State the episode's statistic as given (expected difference between two random judges ≈ 4 years on a 7-year average); any conversion to scatter width labeled as computation.

### F-4. ep08.md:144-146 — sacred money inverted (G1) — MATERIAL
- **Location:** ep08.md:144-146 ("Side ideas worth stealing" → "Sacred money").
- **Gate:** G1 fidelity.
- **What's wrong:** Chapter: "For charity: money goes in but never comes out... nobody can raid it, so everyone can trust it." Transcript (`kBkzT4J1CJU`): "sacred money would just be money that's committed to **only being spent on sacred things**... you could spend it on like health or education." The chapter states the opposite of the episode: the episode's sacred money **is** spendable (on sacred things); the chapter's version is never disbursed.
- **What passing looks like:** Sacred money = funds consecrated to sacred purposes only (health, education, etc.), per the episode. The never-disburse trust-fund variant, if kept, must be labeled builder synthesis.

### F-5. Mermaid node-text rule violations (G4) — ep02, ep08, ep09, ep10
- **Rule:** VISUAL_SYSTEM_GENERIC.md, "Node text maximum 4 words."
- ep02.md:112 — `E[Note it, still study the view]` (6 words).
- ep08.md:135 — `F[Proposer gets 5 percent of gains]` (6 words).
- ep09.md:128-132 — `A[Moral uncertainty: credences across theories]` (6), `C[Weighted average: blend recommendations by credence]` (6), `D[Budget split: each theory gets its credence share of resources]` (10), `E[Risk: action no theory endorses]` (6).
- ep10.md:108 — `C[Notice what matters for the goals]` (6 words).
- **What passing looks like:** Rewrite node labels to ≤4 words each (move the extra words into captions or surrounding prose).

### F-6. Six frontmatter `video_title` values are not the episode titles (G8)
- Builder brief requires `video_title: "<episode title>"`; verified against `research/clearer-thinking/episodes.json`:
- ep03.md:14 "How minds change with David McRaney" → actual "Deep canvassing, street epistemology, and other tools of persuasion with David McRaney"
- ep04.md:14 "Noise with Daniel Kahneman" → actual "Beyond cognitive biases: improving judgment by reducing noise with Daniel Kahneman"
- ep05.md:14 "Practical wisdom with Barry Schwartz" → actual "Beyond the assumption that humans are rational (with Barry Schwartz)"
- ep06.md:14 "The scout mindset with Julia Galef" → actual "Scout and Soldier Mindsets with Julia Galef"
- ep07.md:14 "How to have great conversations with Uri Bram" → actual "Our 300th episode! - How to have better intellectual conversations (with Uri Bram)"
- ep08.md:14 "Futarchy with Robin Hanson" → actual "Systems of governance built on prediction markets with Robin Hanson"
- (ep01, ep02, ep09, ep10 titles verified verbatim.) **What passing looks like:** verbatim titles from episodes.json.

### F-7. cheatsheet.md:68 — banned filler (G7)
- "Prospective hindsight unlocks doubt." — "unlock" is on the banned-filler list. Rewrite without it.

### F-8. ep08.md:252 — dead go-deeper link (builder-brief MEDIA law)
- `https://overcomingbias.com` — HTTPS times out (curl 000); redirect chain http → www → https://www.overcomingbias.com/ never completes. All 12 other go-deeper links across the track return HTTP 200 (verified 2026-10-06). **What passing looks like:** replace with a live URL or remove.

## Track-wide figure-law notes (G4)

### F-C1. Chapter plates are prose descriptions, not figures — all 10 chapters
Every chapter ends with "Figure N (chapter plate)" followed by a **text description** of left/center/right/footer regions (e.g., ep01.md:311-315). VISUAL_SYSTEM_GENERIC.md requires one actual chapter plate per concept (dense, left = cost without the rule, right = cost with it, bottom = tradeoff). A paragraph describing a plate is not a plate. The lesson figures themselves (tables, mermaid) pass captions (all 45 captions name "AI Podcast Curriculum" + shell + source), state-change-only, and the medium ladder; the audit tables have no blank cells. But the chapter-plate requirement is unmet in all 10 chapters.

### F-C2. Audit-table figure ids do not match body captions
Audit tables use `fig1…fig4`, `ch-plate`, `ch-text` while body captions read "Figure 1…4", "Figure 5 (chapter plate)". Cosmetic; align the labels.

### F-C3. No documented four-test evidence per figure
The spec requires each figure to pass four tests (what it looks like, why the rule forces the shape, what one number the reader can change, what symbol the next page reuses). Captions name shells but no figure records the four tests. Recommend a tests column or per-figure note.

## Non-failing observations (notes)

- **N-1 (G2, minor):** Two `###` subchapters introduce more than one idea. ep03.md:107 "Moral dumbfounding and confabulation" covers two experiments; ep04.md:121 "Groups and crowds" covers group polarization, wisdom of crowds, and crowd-within. Splitting each would meet the one-increment rule.
- **N-2 (G2, minor):** ep05.md:96 drops "Aristotle's phronesis" without defining the term. Every other checked term (power law, expected utility, real interest rate, elaboration, confabulation, noise, futarchy, welfare function, reflective equilibrium, relevance realization, Monte Carlo, reactance, steelman, System 1/2, incommensurable) is defined at first use.
- **N-3 (G9):** The index states the difficulty arc (guided → Fermi/journaling → unaided mechanism design), but all 10 chapters use the identical six-drill template (Fermi, argue-both-sides, journal, first-principles, observe, design) with worked answers even in ep10 (e.g., ep10.md:279 gives "about 12.99 million"). The progression is asserted, not demonstrated. Removing worked answers from late-chapter drills would make the arc real.
- **N-4 (G4):** ep04.md:246 places the Figure 3 mermaid diagram after the figure-audit table that references it; move figures above their audit rows.
- **N-5 (G7 scope):** Audited to the parent task's G7 scope (contractions, em dashes, semicolons, banned filler) — all chapters PASS; zero hits. Full ASD-STE100 (-ing verbs, perfect tenses, noun clusters) was not gate-checked per the task's scoping; chapters do contain -ing verbs, so a full-STE100 gate would need a separate pass.
- **N-6:** The `_coverage.md` map is accurate: every mapped claim's chapter:line checks out, the "Unmapped" lists are honest (intros/outros/tangents only), and the April-13th date inconsistency (ep06) was correctly handled by omission. Frontmatter `date` values all match `episodes.json` upload dates.

## What passed cleanly

- **G1 spot checks:** 24/24 substantive claims verified across ep02, ep06, ep09 transcripts (three laws, 6.2%→−5% real rate, deficits, French-economist study, 18-year blogging, MMT, rules 7/8/2, Zuckerberg/Daniel Gross, lookism, Bezos 30%/base 10%, Musk 10%, 70%-to-investors, 85/87/82/90 wording chain, Monkey Island, Jerry Taylor, CFAR 2012, lead filter, 80th–95th percentile, $3/day, bed nets dozens of RCTs + couple thousand per life, million-mile river, Parfit, Rethink Priorities, GiveWell $1,000).
- **G3 arithmetic:** all recomputed numbers check out — 5×12s=60s (but see F-1 for the misread source), 1−6.2=−5.2≈−5, 18×365×500=3.285M, 17,000×20min=340,000min≈5,700hr, 208×16=3,328, 3,328×20min≈1,110hr, 52/10≈5×, 350×10min=3,500min≈58hr, 2×52/3×0.5hr≈17hr/yr, 50×$10k=$500k, $3×365=$1,095, $1,095/$100k=1.1%, 12,988,816≈12.99M tilings.
- **G5 memory aids:** mnemonics, never-confuse pairs, and trap cards verified correct in all chapters (the 87>85>80 / 82>85>90 wording chain matches the transcript verbatim).
- **G6 for-life format:** all chapters have concrete "How to imbibe this" (this-week action, catch-yourself trigger, per-idea behavior changes, monthly audit) and 6 brain-first "Think it yourself" drills; "Skills you can now use" present in all 10 chapters.
- **G8 [uncertain] flags:** honest and precise throughout (Redlawsk/Redloss, Custers, Parford→Parfit, reading→Rethink Priorities, crowd-within "third" gloss — the transcript does say "about one third", so the flag is over-cautious but honest). No invented quotes found anywhere.
- **G9 arc stated:** index.md states the cognition arc (Knowledge Project → rationality → Tyler → Hidden Brain → YNSS → Cal Newport) and the intelligence-thread drill progression.

## E1 exam gate — 20 questions, answered from chapter text only

1. **(ep01)** What is the exponential backoff schedule? → Review after 1–3 days, ~1 week, ~1 month, ~1 quarter, then ~yearly; 4–5 exposures total (ep01.md:61-63).
2. **(ep01)** What is the sweet spot per book? → ~12 interesting ideas, ~30 keep-worthy pieces; ~4 retained naturally, cards for the other 26 (ep01.md:125-129).
3. **(ep02)** State Cowen's three laws. → Flaw it (something wrong with everything), source it (literature on everything), bound it (all propositions about real interest rates are wrong) (ep02.md:29-45).
4. **(ep02)** What is "devalue and dismiss"? → Find one flaw, lower their status, stop learning — the two Ds; the sting is the signal (ep02.md:93-103).
5. **(ep03)** What does elaboration equal, and what are the two routes? → Elaboration = motivation × ability; central route (high elaboration, weighs argument quality) vs peripheral route (low, responds to cues) (ep03.md:47-57).
6. **(ep03)** What are the affective tipping-point numbers? → Doubt ~15% counter-evidence, update ~30%, backfire below (ep03.md:115-129).
7. **(ep04)** What is the error equation? → Total error² = bias² + noise² (ep04.md:29-33).
8. **(ep04)** Name the three kinds of noise. → Level (average harshness differs), pattern (feature weights differ — usually biggest), occasion (same judge varies) (ep04.md:59-75).
9. **(ep05)** What three things does the spreadsheet need? → Complete options, numbered values, stable preferences (ep05.md:31-35).
10. **(ep05)** When is intuition trustworthy (Kahneman-Klein)? → Regular environment for patterns + fast, unambiguous feedback; firefighters yes, stock pickers no (ep05.md:76-88).
11. **(ep06)** Soldier vs scout? → Soldier treats reasoning as combat (defend your side); scout treats it as mapping (see the territory) (ep06.md:29-43).
12. **(ep06)** What were the Bezos and Musk probability estimates? → Bezos: base rate ~10%, personal estimate 30%, acted on EV; Musk: ~10% each for Tesla/SpaceX, assumed likely failure, acted on mission + EV (ep06.md:79-94).
13. **(ep07)** What fraction of disagreements are definitional, and what is the fix? → About 1 in 3; taboo the contested word and restate claims without it (ep07.md:78-88).
14. **(ep07)** What is light gassing? → The opposite of gaslighting: warm agreement reinforcing the group's false perceptions, drifting the map from reality (ep07.md:122-128).
15. **(ep08)** What is futarchy's slogan and mechanism? → Vote on values, bet on beliefs: citizens vote the welfare measure, conditional prediction markets pick the policies (ep08.md:39-47).
16. **(ep08)** How does the CEO decision market work? → Market A (trades called off if CEO stays) prices value-if-fired; Market B prices value-if-kept; the higher price names the decision (ep08.md:55-77).
17. **(ep09)** What is the $3-a-day arithmetic? → Global poor live on ~$3/day; a poor American at $25–30k after taxes sits at the 80th–95th global percentile (ep09.md:37-45).
18. **(ep09)** What are the two moral-uncertainty aggregation rules? → Weighted average (blend recommendations by credence) vs budget split (each theory gets its credence share of resources) (ep09.md:115-125).
19. **(ep10)** Why is the domino tiling impossible? → 31 dominoes need 31 black + 31 white squares; opposite-corner removal leaves 32 of one color and 30 of the other (ep10.md:70-84).
20. **(ep10)** What is relevance realization? → The problem of what to attend to; an emergent loop of holding goals in mind while interacting with the world (ep10.md:93-103).

**E1 result: 20/20 answerable from chapter text only — PASS.**

## Fix priority for the builder

1. F-1 (ep01 cost anchor) — touches the chapter's central number; recompute everything downstream.
2. F-2 (ep04 premortem) — replace with the episode's actual individual "premortum" + crowd-within content.
3. F-4 (ep08 sacred money) — restore the episode's meaning (spendable on sacred things).
4. F-6 (six video_titles) — one-line verbatim replacements from episodes.json.
5. F-5 (mermaid labels) — shorten 9 node labels to ≤4 words.
6. F-3 (ep04 ±4), F-7 (cheatsheet "unlocks"), F-8 (dead link) — small fixes.
7. F-C1 (chapter plates) — render actual plates or formally downgrade the requirement.

---
*End of audit report.*
