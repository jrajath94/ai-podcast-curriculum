# AUDIT REPORT — Charisma track (Track 15), AI Podcast Curriculum
Date: 2026-10-06. Auditor role only. No fixes applied.

## Overall verdict: CONDITIONAL — 5 of 10 chapters PASS outright, 5 carry FAIL items

Clean PASS: ep02, ep03, ep05, ep06, ep09.
Conditional (FAIL items listed below, fixable without rebuild): ep01, ep04, ep07, ep08, ep10.

Read order verified: MASTER_BRIEF.md, REJECTIONS.md, TRACK_AUDITOR_BRIEF.md, VISUAL_SYSTEM_GENERIC.md. Fidelity spot-checked against all 10 transcripts (deep pass on ep01/ep07/ep08; noun sweeps on the rest). Arithmetic recomputed by hand. STE greps run mechanically.

## Builder honest gaps — verification result
1. ep07 second half missing: CONFIRMED declared, twice (ep07.md line ~27; Go deeper note). Acceptable.
2. [uncertain] flags: PARTIAL. Only ep01 (12.5x) and ep03 (95%/90min/71%) carry bracket flags. The coverage map promises flags for "54% lie detection sourcing" and "Wiseman retellings" — neither exists. ep07 and ep08 carry zero flags. See FAIL items.
3. Research exclusions: CONFIRMED carried forward in _coverage.md (Cabane videos, Hidden Brain, Greene #839). Acceptable.
4. Bose headline reworded for STE: CONFIRMED — and it created a misquote. See ep07 G8 FAIL.

## Per-chapter, per-gate verdicts

Gates used (adapted per assignment): G1 fidelity vs transcript, G2 depth + one-sitting conciseness, G3 numbers recomputed, G4 figures (state-change-only, four tests, shells, medium ladder, captions, no blank cells), G5 memory aids, G6 for-life format (imbibe + think-it-yourself + skills), G7 STE100, G8 honesty/[uncertain], G9 standalone check (index must not claim arc membership).

### ep01 (Van Edwards, Cues) — CONDITIONAL
- G1 PASS. 30-row coverage map verified. Spot items confirmed in transcript: 58,000 working hours/11 companies/25 ft/+15%/-30% (transcript lines ~1220-1234), 12.5x, 465/271, Truman, Casa de Luz, Monica Moore, Siminoff, shark-tank retelling ("Siminoff in the tank"). No unmapped major claim found.
- G2 PASS. Zero-prereq readable; tight; no repeated teaching.
- G3 PASS. 465-271 = 194 ✓; 194/271 = 71.6% ≈ "about 72 percent" ✓.
- G4 PASS. 5 figures, numbering consistent, captions name "AI Podcast Curriculum" + source, figure-audit table has no blank cells, mermaid nodes within limits.
- G5 PASS. BoVoVeO, SELLL, THANB all decode correctly.
- G6 PASS. Imbibe, Think-it-yourself, Skills all present and concrete.
- G7 PASS. Mechanical grep: 0 contractions, 0 em/en dashes, 0 prose semicolons, 0 banned filler across the track.
- G8 FAIL (minor). The coverage map promises [uncertain] flags for "54% lie detection sourcing" and "Wiseman retellings". The 54% claim appears at "Lie detection first" with NO flag. Passing = add the promised flag or remove the promise from _coverage.md.
- G9 PASS (N/A).

### ep02 (Voss, Hard Conversations) — PASS
- G1 PASS. Spot items verified in transcript: Good Guys siege, Prince's Gate, FARC, Nick Nanton, Picco, Mnookin, Kahneman, lost-luggage. No unmapped major claim.
- G2-G4 PASS. G5 PASS (VLM CQNA decodes; phrase mnemonic works). G6 PASS. G7 PASS. G8 PASS.
- Advisory (not a FAIL): frontmatter `concepts` lists "black-swan" but the chapter body never mentions it — the single transcript mention is a sponsor read for a real-estate course (transcript line 4636), which the coverage map correctly excludes. The concept tag is stale metadata. Remove it or teach it.

### ep03 (Van Edwards, Conversations) — PASS
- G1 PASS. Spot items verified: 3x500 experiments, Stern, McAdams, Seinfeld, Schmobbert, Jason, 95%/90-min/71% [uncertain] flagged correctly.
- G2 PASS. Repeats ep01 material (McAdams ladder, eye contact, listening cues) but each repeat adds new information (ladder upgrade, oxytocin-vs-thinking distinction). Not dead repetition.
- G3-G9 PASS.
- Advisory: mnemonic "TCD: Traits, Concerns, Deeps narrative" — "Deeps narrative" is a typo for "Deep narrative". Copy-edit.

### ep04 (Houpert, Confidence) — CONDITIONAL
- G1 PASS. Spot items verified: SkiErg, Onnit, Aubrey Marcus, Naval, Tiger Woods, Carrey, Jamaica, Lucy, communicator gallery (Robbins/Clinton/Fry/Shapiro).
- G2-G4 PASS. G6 PASS. G7 PASS. G8 PASS.
- G5 FAIL. Memory aid: "Mnemonic for the five styles: CAECE. Conviction, Authentic, Comedian, Energetic, Empathetic." The five styles initial as C-A-C-E-E = "CACEE", not "CAECE". The mnemonic does not decode. Passing = correct the acronym (or drop it).

### ep05 (Huberman, Bonding) — PASS
- G1 PASS. Spot items verified: tachykinin, Matthews, Schore, Barrett, vasopressin, Ram Dass, Carollo, Eilish, dancing-dates-with-sister.
- G2-G9 PASS. DCEF and CAP mnemonics decode correctly.

### ep06 (Tye, Valence/Rank) — PASS
- G1 PASS. Spot items verified: Draper/Mad Men, cucumber/grape, milkshake FOMO, yum-yuck-me (Meister), Ben Baris (transcript: "the late and great Ben Baris"), Klüver-Bucy, psychedelics section including Huberman's trial-participation disclosure and the advise-against-recreational-use line.
- G2-G9 PASS. FAB mnemonic is good.

### ep07 (Cialdini, Influence) — CONDITIONAL
- G1 PASS. All seven principles, defenses, and studies verified against transcript: blood donor 33→55 (lines ~212-235), email deadlock 30%→6% (lines ~552-568), Beijing asterisk, Opower 30B lbs, e-commerce 29 tests with scarcity-of-supply #1 / social proof #2 / scarcity-of-time #3 (lines ~1230-1290), trend "30 last year, 35 six months ago, 40 now" (lines ~1255-1285), Gordon Sinclair "will you" + pause, campus "I'm a student here too".
- G2 PASS. G4 PASS. G5 PASS (ReLiSoAuScCoUn decodes). G6 PASS. G7 PASS.
- G3 FAIL (2 items).
  1. ep07.md line ~82: "Sales rose another 15 percent, for a 60 percent total gain over the original." The transcript says the headline change produced "a 45 increase in sales" and the testimonials "increased purchases by 15" — with NO stated base. Additive (45+15=60) assumes both percentages apply to the original base; compounded they give 1.45 × 1.15 = +66.75%. The 60% is a builder computation presented as episode fact. Passing = present as "45% then 15% (base unspecified)" or mark the total [uncertain].
  2. ep07.md line ~106 and Q&A #8: "Donations rose 400 percent" + "quadrupled giving" + "Four hundred percent is the measured difference". The transcript says "donations went up 400 percent" — an increase OF 400% = 5x, which is quintupled, not quadrupled (4x). The chapter states both "rose 400 percent" and "quadrupled" as if identical. They are not. Passing = pick the correct multiplier for the transcript's wording and use one term consistently.
- G8 FAIL. ep07.md line ~82 and Q&A #6 present the headline "Hear what you lose by waiting" as the Bose ad's headline (Q&A #6: "Why did 'Hear what you lose by waiting' beat 'new'?"). The transcript's actual headline was "hear what you've been missing" (transcript line ~1204). The builder reworded it for STE and never marked it as a paraphrase; the Q&A then treats the rewording as a verbatim episode quote. Passing = quote the verbatim headline and, if STE demands it, carry the rewording as a clearly marked paraphrase.
- G9 PASS (N/A).

### ep08 (Greene, Daily Laws) — CONDITIONAL
- G1 PASS. All 13 laws plus stories verified in transcript: Wren, Napoleon, supermarket (3 mentions), birthday party, Hollywood, hate-follow, George Sand, 70,000 generations (transcript line 1773, line-wrapped "70 / 000 generations"), Ramachandran, Navy SEAL.
- G2-G4 PASS. G6-G9 PASS.
- G5 FAIL. Memory aid: "DoPeRS CaNDi DOrM SAF. Demonstrate, Purpose, Release, Suspend judgment, Character, Absence, Wonder, Desire, Own time, Resist madness, Madness of groups is R... (use the table instead. Thirteen is too many for one acronym)." The acronym does not decode to the 13 laws (no mapping for "DOrM"; the trailing parenthetical is incoherent), and the builder concedes it. A memory aid that cannot be decoded is not a memory aid. Passing = replace with a working device (the four-triads-plus-one structure right below it already works — promote that, delete the broken acronym).

### ep09 (Duhigg, Supercommunicators) — PASS
- G1 PASS. Spot items verified: Epley, Provine, Dartmouth, Terry Maguire (transcript spelling), Adam Mastriani (transcript spelling), "van Bal at NYU" (transcript error for Jay Van Bavel — chapter's correction is correct), "Erie Hassan at Princeton" (transcript error for Uri Hasson — chapter's correction is correct).
- G2-G9 PASS. PES and QLV M mnemonics decode.

### ep10 (Dicks, Storytelling) — CONDITIONAL
- G1 PASS. Full Spoon of Power retelling, six devices, movie proofs (Harry Met Sally, Star Wars, Independence Day, Die Hard), frayed endings, but-and-therefore, Homework for Life, BABC, swim test, Facebook/kiss-your-wife metaphor all match transcript coverage.
- G3 PASS. G4 PASS. G6 PASS. G7 PASS. G8 PASS.
- G2 FAIL (copy-edit). Q&A #4, ep10.md lines ~184-185: the answer begins `"M` then a line break then `etal object" opens a prediction gap`. Stray "M" character plus a broken word ("Metal" split across lines). Passing = join the word, delete the stray character.
- G5 FAIL. Memory aid: "Mnemonic for the six devices: EB BHCH. Elephant, Backpack, Breadcrumbs, Hourglass, Crystal ball, Humor." Six devices initial as E-B-B-H-C-H = "EBBHCH"; the chapter's "EB BHCH" drops a B. The phrase mnemonic ("Every Brave Bard Holds Captivating Hearers") has six words and is correct, but the acronym string is wrong. Same error repeated in cheatsheet.md. Passing = correct the acronym in both files.

## G9 standalone check — PASS
index.md states: "Charisma is track 15 of 15 in the AI Podcast Curriculum, and it stands outside the thinking arc." cheatsheet.md makes no arc claim. No false arc membership anywhere.

## Figure gates (F1–F7) — PASS with advisories
- F1: every chapter carries a Figure audit table; all figure cells filled; body figure numbers match audit ids (5/4/4/3/3/2/2/2/3/3).
- F2: medium ladder honored — tables first for comparisons, mermaid (≤8 nodes) for flows.
- F3/F4: shell numbers on captions match the spec's shell phrasing (Shell 1 toy, Shell 2 count, Shell 3 rule, Shell 4 symbol). No Shell 0/5 used; acceptable.
- F5: every caption names "AI Podcast Curriculum" + source. PASS.
- F6: no reject-list items; numbers code-computed where computed (194, 72%).
- F7: symbols consistent (no cross-figure symbol system needed; chips not used).
- Advisories (not FAILs): (a) the Figure audit "Four tests" column systematically answers T3 ("what one number can the reader change?") with "none, static plate" — the test is dodged, not passed, on every figure; (b) two mermaid node labels exceed the 4-word guidance (ep02 fig2 "Label it: It seems like..."; ep10 fig2 "B: Son packs for camp now").

## FAIL item count
G1: 0 (1 metadata advisory, ep02). G2: 1 (ep10 line-break defect; ep03 typo advisory). G3: 2 (both ep07). G4: 0. G5: 3 (ep04, ep08, ep10 + cheatsheet). G6: 0. G7: 0. G8: 2 (ep07 misquote; ep01 missing promised flag). G9: 0.

## What passing looks like (no fixes applied, per auditor role)
ep01: add the [uncertain] flag to the 54% lie-detection sourcing (or amend _coverage.md's promise). ep04: fix CAECE → CACEE (or drop). ep07: quote "hear what you've been missing" verbatim and mark any STE rewording as paraphrase; replace "60 percent total gain" with "45% then 15% (base unspecified)" or flag [uncertain]; resolve 400%/quadrupled to one consistent multiplier. ep08: delete the broken 13-law acronym, promote the triads. ep10: repair the "M/etal" line break; fix EB BHCH → EBBHCH in ep10.md and cheatsheet.md. ep02: remove the stale "black-swan" concept tag. ep03: fix "Deeps narrative" typo.
