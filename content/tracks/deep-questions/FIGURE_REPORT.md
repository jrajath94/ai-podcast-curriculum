# FIGURE REPORT — Deep Questions track (Cal Newport)
# Figure-enforcer pass, 2026-10-06. After the audit fix loop (6 FAILs fixed).
# Binding law: ~/workspace/ai-podcast-curriculum/build/VISUAL_SYSTEM_GENERIC.md
# Gates: TRACK_AUDITOR_BRIEF.md F1–F7. Code pipeline only: markdown tables + mermaid. No AI images.

## Figure inventory per chapter

| Chapter | Figures | Lesson plates | Chapter plate |
|---|---|---|---|
| ep01 Perks of No Social Media | 5 (4 kept, 1 new) | Fig 1 boredom intercept; Fig 2 inputs build the world; Fig 3 ambient reaction vs controlled output (NEW); Fig 4 illusion of influence vs calibrated importance | Fig 5 cost of platforms vs four perks |
| ep02 Planning System | 7 (5 kept, 2 new) | Fig 1 root document; Fig 2 core-document cadences; Fig 3 cascade; Fig 4 full capture; Fig 5 shutdown ritual (NEW); Fig 6 hard disciplines, written and two-sized (NEW) | Fig 7 system-hopping vs one rooted system |
| ep03 Deep Work | 3 (unchanged) | Fig 1 three session types on a 60-min memo; Fig 2 five moves | Fig 3 forgetting depth vs prioritizing it |
| ep04 Digital Minimalism | 4 (3 kept, 1 new) | Fig 1 why detox and app fixes failed; Fig 2 values-first cycling example; Fig 3 the 30-day declutter loop (NEW, mermaid) | Fig 4 failed fixes vs the philosophy |
| ep05 Slow Productivity | 4 (unchanged) | Fig 1 paleolithic vs modern day; Fig 2 overhead spiral, computed; Fig 3 three principles vs three wounds | Fig 4 overload vs redesign |
| ep06 Slope of Terribleness | 6 (3 kept, 3 new) | Fig 1 app classification, CCE test (NEW); Fig 2 slope, three zones (mermaid); Fig 3 dopamine prediction loop (NEW, mermaid); Fig 4 echo chamber + tribal circuits merge (NEW, mermaid); Fig 5 arresting the fall | Fig 6 reassuring story vs mechanism |
| ep07 Learning vs Social Media | 4 (3 kept, 1 new) | Fig 1 why learning loses the dopamine game; Fig 2 dopamine vs EFT; Fig 3 the two-move EFT playbook (NEW) | Fig 4 dopamine game vs EFT playbook |
| ep08 5-Step Productivity System | 8 (5 kept, 3 new) | Fig 1 fantasy workday vs the dragon (NEW); Fig 2 tool ladder; Fig 3 six lists; Fig 4 the dump; Fig 5 30-day maintenance; Fig 6 Felipe overhead math, computed (NEW); Fig 7 interval protocol (NEW) | Fig 8 chaos vs day-one protocol |

Total: 41 figures (30 kept, 11 new). Every chapter ends with exactly one chapter plate.

## New figures and the four tests

Each new figure passed all four tests (object shape, rule forces shape, one reader-changeable number, symbol reused on a later page) before drawing:

- ep01 Fig 3 privacy: number = posts and audience size; symbol reused in imbibe, Q&A, memory aids, chapter plate.
- ep02 Fig 5 shutdown: number = shut/not-shut state; symbol reused in ep07 (Mara) and ep08 (evening shutdown).
- ep02 Fig 6 disciplines: number = daily metric code; symbol reused in the chapter plate.
- ep04 Fig 3 declutter: number = 30 days; symbol reused in imbibe and Q&A.
- ep06 Fig 1 definition: number = 3 criteria, binary per app; symbol reused across ep06 and the chapter plate. Eight apps shown (BlueSky stays in prose) to respect the 8-item toy cap.
- ep06 Fig 3 dopamine loop: number = checks per day; symbol reused in ep07.
- ep06 Fig 4 demoderation: number = minutes per day on platform (exposure); symbols reused in the Pizza Hut argument and chapter plate.
- ep07 Fig 3 playbook: number = 3 resonant examples; symbol reused in Q&A applied question and drills.
- ep08 Fig 1 dragon: number = 4–6 hours for day one; symbol reused in maintenance and the chapter plate.
- ep08 Fig 6 Felipe: number = session length; computed 4x(60-30)=120 min = 2 h vs 240-30=210 min = 3.5 h; symbol reused in the memory-aid trap card.
- ep08 Fig 7 Sahil: number = 30 min start, +10 min steps, 2–3 months; symbol reused in imbibe and drills.

## Considered and rejected (four tests failed — not drawn)

- ep04 "positive beats negative" framing: fails test 3, no reader-changeable number. Carried by prose.
- ep07 Q&A Randall hobbies-vs-strategic split: fails test 4, no reuse on a later page. One Q&A among eight; conciseness wins.
- ep08 step-4 configure batching merge: fails test 4, the consolidated card is never reused. Carried by prose.
- ep06 Pizza Hut chain as mermaid: not a state change (a proof, not a count/merge/score/mask/move/symbol). Carried by prose and the chapter plate.

## F1 — page audit: PASS

Walked all 8 chapters top to bottom. Every state-changing claim now maps to a figure; every figure audit table has zero blank cells (verified programmatically: 41 captions numbered 1..N in document order, audit rows reference the same 1..N, chapter plate last in every table). Q&A application sections reuse already-figured mechanisms and carry no new atomic units except the Felipe math and Sahil protocol, which got figures.

## F2 — medium ladder: PASS

First passing medium in table → equation → ASCII → mermaid → SVG order, every figure:
- Tables for comparisons of values and before/rule/after state changes (37 figures).
- Mermaid for flow/dependency claims only (4 figures: ep04 declutter loop, ep06 slope, ep06 dopamine loop, ep06 demoderation merge). All respect the mermaid rule: one graph, at most 5 nodes, node text at most 4 words.
- No equation/ASCII/SVG/Canvas/three.js/Manim/Hyperframes figure qualified above a lower medium.

## F3/F4 — lesson plates + chapter plates: PASS

Every lesson plate carries exactly one claim. Every chapter ends with exactly one chapter plate (left: cost without the rule; center: the stored object; right: cost with the rule; tradeoff line; one-sentence footer). Chapter plates connect lesson plates and replace none of them.

## F5 — captions: PASS

All 41 captions normalized to the required format: "Figure N. Title. AI Podcast Curriculum, epXX (source, date). Shell K. <shell line>. Source: …". Shell lines use the russian-doll wording (Shell 1 toy, Shell 2 count/score, Shell 3 apply one rule, Shell 4 new symbol, Shell 5 next-page reuse). Shells are assigned per question, not per chapter — multiple figures may share a shell number when they advance different questions (same reading the prior audit accepted).

## F6 — reject list and numbers: PASS

No AI-generated images anywhere; code pipeline only. No robot, brain, glow, gradient, logo, watermark, or clip art. Every number is computed or transcript-sourced:
- Computed: ep05 overhead 25 x 2 h = 50 h in a 45 h week (pre-existing, re-verified); ep08 Felipe 4x(60-30) = 2 h vs 240-30 = 3.5 h (new).
- Transcript-sourced: 30-day declutter, 1,600-person experiment, ~1,000 embedding categories, 200,000–300,000 years of tribal wiring, 500M posts/day, 30-min session spin-up, +10 min progression, 2–3 months, 4–6 h day one, 7 sec / 7 h sorry message, 5–6 vs 20–30 workingmemory items, six Felipe sessions.

## F7 — symbol consistency: PASS

Checked track-wide: context shift (ep03 only, defined), shutdown (ep02 defined; ep07/ep08 same meaning), controlled output vs ambient reaction (ep01 only), dopamine as motivation chemical (ep06/ep07 identical), EFT (ep07 only), slope of terribleness (ep06 only), digital minimalism = intention not minimization (ep04 defined; ep05 mention is the book title only), slow productivity (ep05 defined; ep04/ep07/ep08 references consistent), root document (ep02 only), full capture (ep02 only), productivity dragon (ep08 only), deliberate practice vs flow (ep07 only). No symbol is redefined or contradicted anywhere.

## Source corrections (binding source-order rule)

Three figures re-sourced from "original toy" to "episode figure" because Cal drew the underlying visuals in the episode (source order: official source figure first): ep06 Fig 2 (slope diagram), ep06 Fig 5 (mountain climber + flourishing scale), ep08 Fig 1 (the two workday pictures). Captions now read "(episode, DATE)" with "Source: episode figure."

## Drive-by STE fixes (hard fails found during this pass)

- ep01 audit row: semicolon in the u03 Claim cell → reworded.
- ep08 Fig 7 footer: "-ing" verb ("smoking") → reworded.
- ep07 Q&A Matt paragraph: banned word "leverage" (introduced by the earlier fix loop; the audit had found only "unlocked") → "an edge".
- ste_check.py now reports zero hard fails except the two pre-existing ep06 frontmatter "Abandoning" hits, which are verbatim YouTube titles documented as legitimate exceptions in AUDIT_REPORT.md.

## Post-pass hygiene

- wm_clean.py Layer A run on all six edited chapters (ep01, ep02, ep04, ep06, ep07, ep08); structure re-verified after cleaning.
- Backups of pre-pass chapters in /tmp/ep0{1..8}.bak (ephemeral).

## Verdict

F1 PASS · F2 PASS · F3/F4 PASS · F5 PASS · F6 PASS · F7 PASS.
