# AUDIT REPORT: Hidden Brain track
# Auditor verdict: FAIL (1 substantive honesty item, ep01)
# Date: 2026-10-06. Auditor read all 7 transcripts and all 7 chapters end to end.

## Method
- Read verbatim: MASTER_BRIEF.md, REJECTIONS.md, TRACK_AUDITOR_BRIEF.md, VISUAL_SYSTEM_GENERIC.md.
- Read all 7 chapter files, index.md, cheatsheet.md, _coverage.md in full.
- Read all 7 transcripts (.txt) in full; cross-checked every major claim, number, quote, and story.
- Ran ste_check.py on every track file. Grepped for em dashes, en dashes, semicolons, banned filler, contractions.
- Verified the 8 STE hard fails against live YouTube titles via web search (video ids match: 3wiMC4zsq8o, DZj73Fu939s, aJX2H54MPXY, Exq_aynYzrM, and the rank-1 Gloria Mark video).
- Recomputed every arithmetic claim by hand.

## Verdict table (gates per task mapping)

G1 fidelity | G2 depth+conciseness | G3 numbers | G4 figures | G5 memory aids | G6 for-life format | G7 STE100 | G8 honesty | G9 thinking arc

| Chapter | G1 | G2 | G3 | G4 | G5 | G6 | G7 | G8 | G9 |
|---|---|---|---|---|---|---|---|---|---|
| ep01 Subtraction Neglect | PASS | PASS | PASS | PASS | PASS | PASS | PASS* | FAIL | PASS |
| ep02 Divided Brain | PASS | PASS | PASS | PASS | PASS | PASS | PASS | PASS | PASS |
| ep03 Resilience | PASS | PASS | PASS | PASS | PASS | PASS | PASS* | PASS | PASS |
| ep04 Courage | PASS | PASS | PASS | PASS | PASS | PASS | PASS | PASS | PASS |
| ep05 Forgetting | PASS | PASS | PASS | PASS | PASS | PASS | PASS | PASS (minor) | PASS |
| ep06 Memorability | PASS | PASS | PASS | PASS | PASS | PASS | PASS | PASS | PASS |
| ep07 Choking | PASS | PASS | PASS | PASS | PASS | PASS | PASS | PASS | PASS |
| index.md | PASS | PASS | n/a | n/a | n/a | n/a | PASS* | PASS | PASS |
| cheatsheet.md | PASS | PASS | PASS | n/a | PASS | n/a | PASS* | PASS | n/a |
| _coverage.md | PASS | n/a | n/a | n/a | n/a | n/a | PASS* | PASS | n/a |

F1-F7 figures: PASS (with observations, see below). E1 exam gate: PASS, 20/20 answered from chapter text.

*G7 PASS with documented exception: the 8 STE hard fails are all verbatim episode titles, verified truly verbatim against YouTube (see G7 section). ste_check.py exits 1 on those files solely for these.

## FAIL item (the one that blocks the track)

### F-1. ep01 invents numbers about Klotz's exam (G8 honesty). Locations: ep01.md lines 45, 225, 236, 277.
- Line 45 ("Hand-worked arithmetic"): "a student who crams 40 memorized problems into memory can solve exactly those 40 variants. An exam with 20 problems drawn from 200 variants defeats him. A student who masters 1 equation and its applications covers all 200 variants."
- Line 236 (Q&A 3): "40 memorized problems with no shared structure."
- Line 277 (Drill 2): "Klotz traded 40 memorized problems for 1 equation."
- Line 225 (Trap card): "Klotz subtracted 40 memorized problems down to 1 equation."
- The transcript says only "dozens" (Klotz: "I stopped memorizing dozens of other equations and tangential ideas") and "cram as many of those into my brain as possible." No 40, no 20, no 200. These numbers are presented as facts about Klotz (not as an illustrative toy), used in Q&A follow-ups and drills as if sourced.
- What passing looks like: relabel the 40/20/200 as an explicitly illustrative toy ("imagine 40 memorized problems...") or drop the numbers and keep the mechanism (instances vs generator), which needs no numbers. One-line fix in 4 places.

## Minor observations (not fails)

### O-1. ep05 "3 p.m." interpolation (G8). Location: ep05.md Figure 1 table row 1.
- Table says Jill recalled "Sunny, clouds at 3 p.m., no rain." Transcript says "the clouds came over at about 3:00" with no a.m./p.m. The p.m. is a small interpolation. Harmless in context, but under the honesty law it should read "about 3:00" or carry no a.m./p.m.

### O-2. ep02 quote STE-normalized (G8). Location: ep02.md lines 29-33.
- Chapter quotes the warning as "Do not touch it. It is toxic. Do not even go there." Transcript: "Don't touch it. It's toxic. Don't even go there." Normalization to STE (no contractions) is standard practice and disclosed nowhere as verbatim, which is the right call; noted for the record that this quote is STE-normalized, not character-verbatim.

### O-3. Figure coverage gaps (G4/F1). Not fails: the visual law makes the two-paragraph rule a ceiling, not a quota, and every chapter's figure-audit table has zero blank cells.
- ep01: the Nature grid experiment (a count: most added) and the 98-vs-47 exam result (a score) have no figure; the same pattern is covered by fig2 (essay 17/83).
- ep03: FEMA $130M spending, the COVID suicide correction, and the laughter-health mechanism have no figures.
- ep05: the grades study and mood loop have figures; the city-grid model does. Jill's three events have fig1. Fine.
- All drawn figures pass the four tests as documented in the figure-audit tables; medium ladder honored (table for comparisons, mermaid for flows/loops, ASCII for the bridge trace).

### O-4. Text-medium figure interpretation (F2/F5/F6/F7).
- The track renders figures as markdown tables, mermaid graphs, and one ASCII trace rather than SVG plates. This is the medium ladder's first-choice media for comparisons and flows, and every caption names the project ("AI Podcast Curriculum"), the episode source, and the shell, e.g. "Figure 1. The Duplo bridge, two solutions. AI Podcast Curriculum, ep01 (Leidy Klotz, 2026-04-20). Shell 3. Apply the one rule. Source: original toy, from episode claims." The color/shape spec (warm paper #F7F4EE etc.) targets SVG/still plates and does not apply to text media. Chapter plates exist in every chapter in the required shape: left = cost without the rule, center = stored object, right = cost with the rule, bottom = tradeoff in one line. Reject list respected: no brain/robot/glow/stock imagery anywhere.

## Gate-by-gate evidence

### G1 Fidelity (reading = watching)
- I read all 7 transcripts fully and checked every major claim, number, story, and quote against the chapters. Result: no major unmapped items in any chapter.
- Spot checks against _coverage.md line mappings (ep01:29-35, ep01:169-182, ep02:78-91, ep05:99-110, ep07:73-77): every mapped range contains the claimed content. Line numbers are accurate.
- Transcript-vs-chapter deltas found and judged:
  - ep01: transcript auto-caption says "Lidwell"; chapter correctly uses Klotz. Caption typo fixed, not propagated. Good.
  - ep03: transcript caption says "Elizabeth Kubler-Ross"; chapter uses the correct standard spelling "Elisabeth Kübler-Ross." Good.
  - ep07: chapter names no film for stereotype threat; transcript names "White Men Can't Jump." Chapter's description ("the stereotype that white players are not as good at basketball as Black players") is accurate. Acceptable omission.
  - ep07: "35 words they both knew cold" is a correct hand count of the oath text without the name (verified by recount: 35). Computed, not invented.
- Ranks 1, 2, 8 (Gloria Mark, Dave Evans, Ethan Kross) have no transcripts and no chapters; index.md and cheatsheet.md document this honestly with cause (YouTube timedtext HTTP 429 across 4 retry rounds). Nothing was built from titles alone. The ranking was kept intact. PASS as documented honest gap.

### G2 Depth + conciseness (zero-prereq, one-sitting, no repeated teaching)
- Zero-prereq spot check (10 terms, all defined at first use): subtraction neglect, acquisitiveness, HSAM, reconstruction, city grid (as model), rTPJ, confabulation, social discounting, bystander effect, ResMem, working memory, stereotype threat, Mandela effect, corpus callosum, resilience trajectory. All defined at or before first use. No forward references found.
- Subchapter audit (read 2+ chapters fully; checked all 7): every ### adds exactly one increment. No double-idea subchapters found.
- Repetition audit: no paragraph restates earlier teaching without new information. The chapter-plate tables consolidate at the END (permitted by the brief). Mnemonics repeat only in the cheatsheet (expected). The ep02 figure-audit claims master/emissary symbols are "reused across chapters"; grep shows "emissary" appears only in ep02. The claim is aspirational, not a repetition problem. No bloat found; chapters are long but dense.

### G3 Numbers (transcript-sourced or computed; arithmetic recomputed)
- ep01: 17/83 essay ✓; 2 of 90 recipe, add-to-remove 88:2 = 44:1 ✓; music 3x ✓; itinerary 14 hours, 1 in 4 ✓; 750 ideas, <10% subtractive = <75 vs >675 ✓ (chapter states this); freeway 2-to-1 ✓; 30,000 deaths/year ✓; Springsteen 50+ songs to 10, Because the Night #13, Fire #2 ✓; 98 vs 47 ✓.
- ep02: 302 neurons (nematode) ✓; ~600M years (Nematostella) ✓; 35,000 notes (B minor mass) ✓.
- ep03: 8%/20%/30% early PTSD, back to near normal by 6 months ✓; $130M FEMA ✓; four trajectories, chronic at most ~10% ✓; 2018 Clinical Psychology Review ✓.
- ep04: 3 risks, 6 lanes ✓.
- ep05: 89% vs 29% grades; "three-to-one bias" = 89/29 = 3.07 ✓; Sept 30 1998 ✓; Meng Po five-ingredient soup ✓.
- ep06: 40 altered images ✓; 10,000 faces ✓; ResMem score 0 to 1 ✓.
- ep07: digit ladder 7624 / 589743 / 910482 reversed ✓; 24.17s Beijing ✓; 6th place Rio ✓; 35 oath words ✓ (recount verified).
- View counts in front matter (20,092 / 10,798 / 9,221 / 8,972 / 8,753 / 6,799 / 5,940) are research-sourced, consistent with ranks 3,4,5,6,7,9,10. Not transcript-verifiable; accepted as ranking metadata.

### G4 Figures (state-change-only, four tests, shells, medium ladder, captions, no blank cells)
- Every chapter has a Figure audit table; zero blank cells in any of the 7 tables.
- All figure captions name the project + episode source + shell (see O-4). Every figure carries "One claim per plate."
- Chapter plates in all 7 chapters follow the required 4-column shape.
- Observations O-3/O-4 recorded; no fails.

### G5 Memory aids
- Mnemonics in all 7: SAIL (ep01), HOW (ep02), HOLD (ep03), WIDE (ep04), GIST (ep05), STICK (ep06), STORE (ep07). All decode to episode content.
- Never-confuse pairs: 3 per chapter, all accurate to the episode (e.g. "Confabulation is not lying", "Reframing is not positive thinking", "A ritual is not superstition", "Memorability is not beauty", "Resilience is not denial").
- Trap cards: 4 per chapter, each pairs a real failure mode with the episode's correction.
- Cheatsheet: one dense page, all key facts/numbers/names/decisions, cross-track number table, honest missing-episodes section. PASS.

### G6 For-life format (G1b: imbibe + think-it-yourself + skills)
- "## How to imbibe this": present in all 7 chapters, 7 concrete practices each with observable behavior changes. Not motivational fluff. PASS.
- "## Think it yourself": present in all 7 chapters, brain-first drills marked "done WITHOUT AI." PASS.
- "## Skills you can now use": present in all 7 chapters, 8 actionable skills each. PASS (required by G9 of the brief).
- "## Q&A": 8 per chapter, each with full follow-up answers, each including a beginner-explanation question and applied questions. PASS.
- "## Go deeper": every chapter links the episode + 2 verified sources with live HTTP checks noted (200/301/303). PASS.

### G7 STE100
- ste_check.py: ep02, ep04, ep05, ep06, ep07 fully PASS (0 hard fails).
- 8 remaining hard fails, ALL verified as verbatim episode titles against live YouTube:
  1. ep01.md:14 video_title "Why You're Always Overwhelmed" — verified: youtube.com/watch?v=3wiMC4zsq8o title "Why You're Always Overwhelmed."
  2. ep01.md:19 sources label, same title.
  3. ep03.md:14 video_title "Why You're Not As Broken As You Believe" — verified: youtube.com/watch?v=DZj73Fu939s.
  4. ep03.md:19 sources label, same title.
  5. index.md:41 "The Real Reason You Can't Focus (It's Not Just Your Phone)" (rank-1 missing episode) — verified: official Hidden Brain video with Gloria Mark, same title.
  6. cheatsheet.md:124 same title in Missing section.
  7. _coverage.md:5 "Why You're Always Overwhelmed" (section heading).
  8. _coverage.md:63 "Why You're Not As Broken As You Believe" (section heading).
- Additionally, ep04's front-matter title contains "It's Not What You Expect," which is the verbatim YouTube title (verified: youtube.com/watch?v=aJX2H54MPXY); the checker reports it only as an apostrophe-s WARN, not a hard fail.
- Zero em dashes, zero en dashes, zero semicolons in prose, zero banned filler words across all 9 files. -ing WARNs are gerunds/nouns/participles, not verbs; possessive WARNs are possessives, not contractions.
- Note: chapter `title` fields deliberately use STE-safe paraphrase ("Episode 1: Why You Are Always Overwhelmed") while `video_title` keeps the verbatim title for honest sourcing. Correct approach.

### G8 Honesty ([uncertain], invented quotes/numbers, episode-vs-synthesis)
- Builder's honest gaps verified:
  1. 3 missing episodes: honestly documented in index.md and cheatsheet.md, no chapters built. CONFIRMED.
  2. 8 STE hard fails are verbatim titles: CONFIRMED (see G7).
  3. [uncertain] marks: Greene's book title marked [uncertain] in ep05 Go deeper ✓. Post-checklist death counts: chapter refuses to invent a number ("Deaths fell"; "Exact death counts after the checklist are not given in the episode.") ✓. ResMem URL: coverage map marks it independently verified (GitHub Brain-Bridge-Lab/resmem, HTTP 200), not episode-sourced; chapter places it in Go deeper with the verification note ✓.
- Misattribution flags: Burke quote flagged misattributed (ep04) ✓; Einstein/servant-gift line flagged "sometimes misattributed" (ep02) ✓.
- Episode-vs-synthesis: chapters keep episode claims in the narrative and put builder arithmetic, drills, and applications in clearly separated sections (Hand-worked arithmetic, Q&A follow-ups, drills, imbibe). PASS except F-1, where invented numbers were placed in the narrative as episode fact.
- FAIL: F-1 (ep01 40/20/200 invention). See above.

### G9 Thinking arc (intelligence thread: how minds work; progressive drill difficulty)
- Track position correct: index.md places Hidden Brain 4th in the arc (models -> rationality -> watching great minds -> how minds work -> debugging self-delusion -> sustained focus), described as "the self-knowledge foundation." Consistent.
- Drill difficulty progression verified: ep01/ep02 "Guided, with answer sketches" (6-7 sketches each) -> ep03/ep04/ep05 "Semi-guided: fewer answer sketches" -> ep06 "Less guided now: work them, then check your reasoning" (no sketches) -> ep07 "No answer sketches. Reason from the episode, unaided" + Drill 6 full track synthesis (one paragraph uniting all 7 ideas). The 2 "answer sketch" greps in ep07 are the words "no answer sketches" themselves. PASS.

## E1 exam gate: 20 questions, answered from chapter text only

1. (ep01) Define subtraction neglect. -> The automatic impulse to solve a problem by addition even when the better solution is to take something away. (ep01 ### Subtraction neglect)
2. (ep01) In the essay experiment, what shares added vs subtracted? -> 83% added words, 17% subtracted. (ep01 fig2)
3. (ep01) Name all five steps of Pronovost's checklist. -> Wash hands with soap; clean the patient's skin with antiseptic; sterile drapes over the entire patient; sterile mask, hat, gown, and gloves; sterile dressing over the catheter site. (ep01 ### The five-step checklist)
4. (ep02) What is the real division between the hemispheres? -> Not what they do but how: both do the same things in different ways; right takes the whole, left zeros in on details. (ep02 ### How, not what)
5. (ep02) What changes in the moral experiment when the right TPJ is disabled? -> Judgment flips from intent-based (attempted poisoning worse) to outcome-based (accidental death worse). (ep02 fig2)
6. (ep02) What is confabulation, and which story demonstrates it? -> The left hemisphere inventing a story that fits its beliefs when evidence contradicts it; the mother's-arm patient. (ep02 ### Confabulation)
7. (ep03) Name the four trajectories and the chronic ceiling. -> Resilience (majority), recovery, delayed, chronic; chronic at most ~10%. (ep03 fig2)
8. (ep03) Why does Kubler-Ross's model not describe grief? -> It studied people facing their own death, was never supported as a grief map, and prescribes feelings instead of describing them. (ep03 ### The five stages were never about grief)
9. (ep03) What happened to 9/11 PTSD rates by six months? -> Early 8%/20%/30% readings fell back to near normal for the city as a whole. (ep03 fig1)
10. (ep04) What is social discounting, and how did kidney donors differ? -> Generosity falls with social distance; donors' curve is flat, strangers count as kin. (ep04 fig1)
11. (ep04) What brain difference did Marsh find? -> Extreme altruists have larger amygdalas (heightened distress recognition); psychopaths tend to have smaller ones. (ep04 fig2)
12. (ep04) Name the freeway rescuer's three risks. -> Ran across six lanes to her window; ran around the car to the driver's seat; gunned a U-turn on the interstate. (ep04 ### Three risks)
13. (ep05) Explain the city-grid model. -> Memories are synaptic networks; dense connections are many roads (easy recall), sparse ones a single alley (needs a lucky cue). (ep05 fig2)
14. (ep05) What did the grades study find? -> A grades recalled 89% accurately, D grades 29%; the edit is genuine and favors success. (ep05 fig3)
15. (ep05) What is the mood-memory loop? -> Sad mood retrieves sad memories, which confirm a sad life story, which deepens the mood. (ep05 fig4)
16. (ep06) What is the visual Mandela effect? Name the three quiz items. -> Crowds sharing the same false visual memory; Monopoly Man's monocle (none), C-3PO's silver leg, Waldo's cane. (ep06 fig1)
17. (ep06) What did ResMem train on, and what did it predict? -> Trained on ordinary photos (faces, scenes, objects), zero art history; predicted famous paintings more memorable than obscure ones. (ep06 fig4)
18. (ep06) Which memorability predictors failed in the museum study? -> Beauty, emotion, colorfulness; size and spacious context passed. (ep06 fig2)
19. (ep07) Describe the digit ladder and what each rung proves. -> 7624 easy (hold and echo), 589743 harder (near capacity), 910482 reversed much harder (hold + reorder + emit); the store is small and shared between holding and computing. (ep07 fig1)
20. (ep07) Name the four anti-choke tools and each mechanism. -> Practice to automaticity (moves skill off the store); reframe symptoms (relabels arousal as fuel); breathe (evicts worry, calms body); ritual (holds the slot with a harmless placeholder). (ep07 fig3)

E1 result: 20/20 answerable from chapter text alone. PASS.

## Builder's honest gaps: verification summary
1. 3 missing episodes documented, no chapters built from titles alone: VERIFIED TRUE.
2. 8 remaining STE hard fails are verbatim episode titles: VERIFIED TRUE (all 8 hits are verbatim titles, each confirmed against live YouTube titles).
3. [uncertain] marks on Greene's book title, post-checklist death counts, ResMem URL: VERIFIED TRUE and correctly handled (no numbers invented; URL marked independently verified).

## Bottom line
The track is strong: full-fidelity coverage of all 7 transcripts, honest numbers, dense zero-prereq chapters, working figure system, real memory aids, for-life sections in every chapter, clean STE except verbatim titles, honest gaps, and a working progressive drill arc. One substantive honesty fail blocks PASS: ep01's invented 40/20/200 exam numbers (F-1). Fix those 4 lines and the track passes.
