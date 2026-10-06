# FIGURE REPORT — Clearer Thinking track (Spencer Greenberg)
**Figure enforcer:** subagent 73e42e73 | **Date:** 2026-10-06
**Scope:** `content/tracks/clearer-thinking/ep01.md`–`ep10.md` against VISUAL_SYSTEM_GENERIC.md (binding on pictures) + TRACK_AUDITOR_BRIEF figure gates F1–F7.
**Read first (verbatim):** `build/VISUAL_SYSTEM_GENERIC.md`, `stanford-frontier-ai/build/REJECTIONS.md`, `build/TRACK_AUDITOR_BRIEF.md`.

## Verdict

**F1–F7: PASS on all 10 chapters.** 45 figures total (35 lesson figures + 10 chapter plates), all code-pipeline (markdown tables, equation block, mermaid). No AI image generation, no OpenRouter, per the order.

## Figure inventory

| Ch | Figures (in reading order) | Plates |
|---|---|---|
| ep01 | Fig1 backoff schedule (table, S2), Fig2 mass vs spaced (table, S3), Fig3 memory types (table, S1), Fig4 Quantum Country cost (table, S2) | Fig5 (chapter plate, table, S5) |
| ep02 | Fig1 three laws (table, S1), Fig2 real-rate arithmetic (table, S2), Fig3 offense to study (mermaid, S3) | Fig4 (chapter plate, table, S5) |
| ep03 | Fig1 ELM (mermaid, S1), Fig2 3v9 study (table, S2), Fig3 tipping point (table, S3), Fig4 deep-canvassing protocol (table, S4) | Fig5 (chapter plate, table, S5) |
| ep04 | Fig1 error equation (equation, S1) NEW, Fig2 underwriters (table, S2), Fig3 three noise kinds (table, S3), Fig4 noise-audit loop (mermaid, S4) | Fig5 (chapter plate, table, S5) |
| ep05 | Fig1 spreadsheet needs (table, S1), Fig2 frame changes choice (mermaid, S2), Fig3 intuition conditions (table, S3) | Fig4 (chapter plate, table, S5) |
| ep06 | Fig1 soldier vs scout (table, S1), Fig2 EV cases (table, S2), Fig3 calibrated confidence (mermaid, S3) | Fig4 (chapter plate, table, S5) |
| ep07 | Fig1 tower (mermaid, S1), Fig2 disagreement triage (table, S2), Fig3 light-gassing loop (mermaid, S3) NEW, Fig4 group size (table, S4) | Fig5 (chapter plate, table, S5) |
| ep08 | Fig1 futarchy split (table, S1), Fig2 CEO market (table, S2), Fig3 bill auction (mermaid, S3) | Fig4 (chapter plate, table, S5) |
| ep09 | Fig1 income comparison (table, S1), Fig2 pond and river (table, S2) NEW, Fig3 implicit to explicit (table, S3), Fig4 moral aggregation (mermaid, S4) | Fig5 (chapter plate, table, S5) |
| ep10 | Fig1 two tribes (table, S1), Fig2 domino parity (table, S2), Fig3 relevance loop (mermaid, S3) | Fig4 (chapter plate, table, S5) |

All 45 captions follow the required form: "Figure N. Title. AI Podcast Curriculum, epXX (source, date). Shell K. <shell line>. Source: …". All assign one shell per figure, S1→S5 in reading order.

## Changes made by the enforcer

1. **ep04: added Figure 1, the error equation** (`error² = bias² + noise²`, equation block). The episode's central formula was prose-only; per the spec it is an atomic unit (a formula part) and a state-changing claim with no figure. Medium ladder: table fails (claim is a definition, not a value comparison); equation block is the first that passes. Four tests: T1 object = error split into two components; T2 rule = independent components add in quadrature, per the episode; T3 number = reader can plug bias/noise values; T4 reuse = Q&A, memory aids, premortum rationale, plate. Renumbered old Fig1→2 (S2), Fig2→3 (S3), Fig3→4 (S4).
2. **ep07: added Figure 3, the light-gassing loop** (mermaid). Light gassing was a named new symbol with a reinforcing move and no figure (audit row pointed at `ch-text`). Medium ladder: table fails (claim is a move/loop); mermaid is the first that passes. Four tests: T1 object = reinforcing loop; T2 rule = warm agreement reinforces the false map, warmth hides the drift; T3 N/A (no numeric claim); T4 reuse = Q&A, memory aids, imbibing. Node labels ≤4 words. Renumbered old Fig3→4 (S4), plate→5.
3. **ep09: added Figure 2, the pond and the river** (table). The pond→river escalation is a scored state change (1 child vs a million, duty vs no stopping point) with no figure. Medium ladder: table passes first (comparison of values). Four tests: T1 object = pond vs river; T2 rule = distance does not matter, so the logic has no stopping point; T3 numbers = 1 vs a million, both from the episode prose; T4 reuse = demandingness in Q&A, memory aids, drills. Renumbered old Fig2→3 (S3), Fig3→4 (S4), plate→5.
4. **Moved 4 misplaced mermaid figures into their body sections** (N-4 class): ep04 audit loop → "How to run one"; ep05 frame → "Frames change the answer"; ep06 confidence → "Social versus epistemic confidence"; ep08 bill auction → "Bill auctions". (ep09 and ep10 mermaids were already correctly placed; ep08's original body placement after "Small-scale trials" was also moved up into "Bill auctions" and the duplicate removed.)
5. **Fixed ep05 figure order**: moving the frame mermaid into its section put Figure 3 before Figure 2 in reading order; renumbered frame→Figure 2 (S2), intuition→Figure 3 (S3).
6. **All 10 chapter-plate captions**: added the missing `(source, date)` element, e.g. "AI Podcast Curriculum, ep01 (original toy, 2023-03-13)". Plates otherwise meet the spec: one title; left = cost without the rule; center = the stored object; right = cost with the rule; bottom = one-line tradeoff; one-sentence footer; every number from the page (verified: 10×30min=5h, 300×12s=1h, 4×1/3≈1.3h, 4×1/2=2h) or episode-sourced; no banned decoration.
7. **Rewrote all 10 figure-audit tables** (F-C2): figure ids now read "Figure 1"…"Figure 5 (chapter plate)", matching body captions exactly (verified by script: 10/10 match). Fixed mediums (ep01 u05 was wrongly "equation"; all plates are tables). Eliminated every `ch-text` pseudo-id: units now point at real figures (mentor rules, protocol, hygiene, wisdom, Monkey Island, small-scale trials, feedback → their chapter plates where the plate carries them).

## F1–F7 per-chapter verdicts

- **F1 (page audit: every state-changing claim has a figure; no blank cells):** PASS all 10. Audit tables list every unit with Before/After; zero blank cells (script-verified); every unit maps to a body figure.
- **F2 (medium ladder honored):** PASS all 10. Table for value comparisons; equation block for the ep04 definition (first medium that passes); mermaid for flows, branches, and loops. No figure uses a heavier medium than its claim needs.
- **F3/F4 (lesson plates one claim; chapter plates where warranted):** PASS all 10. Each lesson figure carries exactly one claim. Each chapter ends with one chapter plate meeting the full plate spec.
- **F5 (captions name the project + source):** PASS all 10. All 45 captions name "AI Podcast Curriculum", carry epXX with (source, date), Shell K with the shell line, and a Source tag.
- **F6 (reject list; every number computed or sourced):** PASS all 10. No reject-list items (no robot/brain/glow/clip art/watermark; one claim per lesson plate). Recomputed: 4×1/3≈1.3h, 4×1/2=2h (ep01); 1−6.2=−5.2≈−5 (ep02); 52/10=5.2→"about 5 to 1" (ep04); 64−2=62, 32+30=62 (ep10); 10×30min=5h, 300×12s=1h (ep01 plate). All other numbers are episode claims, none invented. New figures: ep04 equation has no numbers (episode formula); ep07 loop has no numbers; ep09 pond/river numbers (1, a million) are the episode's.
- **F7 (symbols consistent track-wide):** PASS. Track symbol table below; no conflicting redefinitions found. ("premortem" in ep05 refers to Klein's team ritual, a different referent from ep04's episode "premortum"; usage is consistent per referent.)

## Track symbol table (F7)

| Symbol | Meaning | First figure | Reused in |
|---|---|---|---|
| backoff ladder | review after days, week, month, quarter, year | ep01 Fig1 | ep01 imbibing, drills, skills |
| error equation | error² = bias² + noise² | ep04 Fig1 | ep04 Q&A, memory aids, plate |
| noise kinds | level, pattern, occasion | ep04 Fig3 | ep04 audit, Q&A; ep10 |
| noise audit | shared cases → independent re-judgment → decompose → fix | ep04 Fig4 | ep04 imbibing, drills |
| premortum | imagine failure, adjust, average | ep04 prose | ep04 Q&A, imbibing; ep10 |
| soldier / scout | reasoning as combat vs as mapping | ep06 Fig1 | ep02, ep04, ep10 |
| ELM routes | central vs peripheral by elaboration | ep03 Fig1 | ep03 Q&A; ep10 |
| tipping point | doubt ~15%, update ~30% | ep03 Fig3 | ep03 Q&A, imbibing |
| deep-canvassing protocol | rapport, consent, number, story, accept | ep03 Fig4 | ep03 imbibing, drills, skills |
| futarchy split | vote values, bet beliefs, execute | ep08 Fig1 | ep08 throughout |
| conditional market | call-off pricing under each decision | ep08 Fig2 | ep08 Q&A |
| bill auction | propose → market judges → 5% fee | ep08 Fig3 | ep08 Q&A, memory aids |
| tower | joint brick-laying climbs higher | ep07 Fig1 | ep07 throughout |
| light gassing | warm agreement reinforces false map | ep07 Fig3 | ep07 Q&A, memory aids, imbibing |
| buzzer problem | ~7 breaks conversation, cap at 4 | ep07 Fig4 | ep07 Q&A, drills |
| demandingness | pond → river, no stopping point | ep09 Fig2 | ep09 Q&A, memory aids, drills |
| explicit model | assumptions written, attackable | ep09 Fig3 | ep09 Q&A, skills |
| moral aggregation | average or split by credence | ep09 Fig4 | ep09 Q&A, memory aids |
| two tribes | axiomatic vs ecological rationality | ep10 Fig1 | ep10 Q&A |
| domino parity | 32/30 cannot make 31/31 | ep10 Fig2 | ep10 Q&A, drills |
| relevance loop | goals held in mind ↔ world | ep10 Fig3 | ep10 Q&A |

## Considered and deliberately not drawn (four tests or conciseness)

Each of these was tested against the four tests and the conciseness rule ("kill any figure that repeats prose without adding information"). None is a state-changing claim left without a figure; all are static counts, background vocabulary, or prose-complete single paragraphs where a figure would decorate or restate:

- ep01: sweet-spot 30/4/26 partition; 10%-question; medical-student 1/3 and 1/2 (static counts).
- ep02: French-economist nationality finding; MMT test; aspiration vividness; lookism (static claims).
- ep03: belief/attitude/value taxonomy (would restate one tight paragraph and break the S1–S5 ladder); assimilation/accommodation (background vocabulary); street-epistemology protocol (sibling of Fig4; second protocol figure is redundant).
- ep04: "model of you beats you" before/after (restates two sentences); premortum procedure flow (episode gives no numbers; would invent — F6).
- ep05: counting-replaces-thinking; constructed preferences; three bricklayers (parable illustration); "tell me when to think" (each restates adjacent prose or would decorate).
- ep06: rational-irrationality taxonomy; press-secretary/board (definitions; memory-aid lines already serve).
- ep07: garden/forest (metaphor illustration); marginal thinking (restates paragraph).
- ep08: sacred-money flow (side idea, one prose-complete paragraph); decision-selection-bias (prose-complete).
- ep09: Monte Carlo point-vs-distribution (prose marks the numbers explicitly illustrative — "or whatever the sampling shows"; a figure would hand-wave a score — F6); bed-nets evidence bar (static counts).
- ep10: nine-dot solution (second illustration of the insight unit already carried by the worked Fig2; geometry figure adds little); typical-mind fallacy; paradigm history; Simon-on-diagrams (each prose-complete or decorative).

## Notes for the parent

- F-C2 (audit-table ids vs captions) and F-C3 (four-test evidence) from the audit are now closed: ids match 10/10 by script, and the four tests are documented per figure in this report.
- The old N-4 issue (figures after the audit table) is closed: all figures now sit in their body sections; only chapter plates follow the audit table, which is the established end-of-chapter pattern.
- No chapter text was altered except captions, figure blocks, and audit tables. No new style violations introduced (scanned: zero em dashes, semicolons in captions, or banned filler in edited regions).
- Suggested follow-up (not in this task's scope): the `cheatsheet.md` and `index.md` carry no figures; if they ever need the figure law applied, that is a separate pass.
