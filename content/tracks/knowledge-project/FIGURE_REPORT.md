# FIGURE REPORT — Knowledge Project track (Shane Parrish)
**Figure enforcer.** Date: 2026-10-06. Scope: `content/tracks/knowledge-project/ep01.md`–`ep10.md`.
**Read verbatim first:** `build/VISUAL_SYSTEM_GENERIC.md`, `build/REJECTIONS.md`, `build/TRACK_AUDITOR_BRIEF.md`, plus `AUDIT_REPORT.md` and `FIX_REPORT.md` in this directory.
**Law applied:** draw only on a state change; four tests before every new figure; medium ladder (table → equation → ASCII → mermaid → SVG); code pipeline only (markdown tables + mermaid, zero AI images); one shell per figure, assigned honestly in the caption; no blank cells; symbols consistent track-wide.

## Figure inventory (38 total, was 28)

| Ch | Figs | List |
|---|---|---|
| ep01 | 4 | fig1 reading rank (table, Shell 2); fig2 two ways to predict (mermaid, Shell 3); fig3 funnel 10,000/500/5 (table, Shell 2); fig4 priority circles (mermaid, Shell 3) |
| ep02 | 3 | fig1 two paths (mermaid, Shell 1); fig2 rates bet (table, Shell 2); fig3 rules as blind-spot removal (mermaid, Shell 3) |
| ep03 | 4 | fig1 derivative chain (mermaid, Shell 1); fig2 circular deal $5B loop (mermaid, Shell 3); fig3 rails compared (table, Shell 2); fig4 equal partnership (table, Shell 3) |
| ep04 | 4 | fig1 negative visualization (mermaid, Shell 3); **fig2 trichotomy of control (table, Shell 3, NEW)**; **fig3 five-second rule (mermaid, Shell 3, NEW)**; fig4 skeptical/open-minded matrix (table, Shell 1, renumbered from fig2) |
| ep05 | 2 | fig1 research pipeline (mermaid, Shell 1); fig2 dead/live time (table, Shell 3) |
| ep06 | 5 | fig1 brutal facts Kroger/A&P (table, Shell 2); fig2 flywheel vs Doom loop (mermaid, Shell 3); fig3 20-mile march 292:1 (table, Shell 2); **fig4 bullets then cannonballs (mermaid, Shell 3, NEW)**; **fig5 five stages of decline (mermaid, Shell 1, NEW)** |
| ep07 | 4 | fig1 believability voting (table, Shell 2); fig2 five-step loop (mermaid, Shell 3); fig3 two yous (table, Shell 3); fig4 pain button (mermaid, Shell 3) |
| ep08 | 3 | fig1 three pillars (mermaid, Shell 1); fig2 smallest viable audience (table, Shell 2); **fig3 sunk costs as gifts (table, Shell 3, NEW)** |
| ep09 | 5 | fig1 delay intuition (mermaid, Shell 3); **fig2 underwriter noise 10% vs 50% (table, Shell 2, NEW)**; **fig3 premortem (mermaid, Shell 3, NEW)**; fig4 regression (table, Shell 2, renumbered from fig2); **fig5 Lewin's springs (table, Shell 3, NEW)** |
| ep10 | 4 | fig1 2008 forced move (table, Shell 3); **fig2 risk redefined (table, Shell 3, NEW)**; **fig3 cycle excess/correction/overshoot (mermaid, Shell 1, NEW)**; fig4 first/second-level (table, Shell 3, renumbered from fig2) |

10 new figures added (ep04: 2, ep06: 2, ep08: 1, ep09: 3, ep10: 2). Renumbered for document order in ep04, ep09, ep10.

## What the enforcer changed (beyond the fix loop)

1. **Shell labels restored, honestly.** The fix loop dropped all "Shell N" labels. The enforcement brief requires one shell per figure assigned in the caption. Each figure now carries the shell it actually embodies (Shell 1 = show the toy; Shell 2 = count/score; Shell 3 = apply the one rule), using the spec's shell verbs. No fake 1→5 sequencing was invented.
2. **10 missing state-change figures added.** Each passed the four tests and the medium ladder; each covers a spec-required unit type (split, step loop, score, change) that had Q&A + drill + imbibe coverage but no figure. Details per figure in the audit tables.
3. **4 mermaid node-text violations fixed** (spec: max 4 words per node): ep02 fig1 "trial and error" → "trial-and-error"; ep03 fig1 "2nd: conversion down, months later" → "2nd: conversion down later"; ep04 fig1 "Imagine it gone: flickering moment" → "Imagine it gone, briefly"; ep05 fig1 "Themes emerge: 80 to 48" → "80 themes become 48". All ≤8 nodes confirmed programmatically.
4. **ep01 blank cell fixed.** The duplicate u04 row with an empty Four-tests cell was merged into a single honest u04 row.
5. **3 semicolons removed** from new tables (STE100 hard fail); all 10 files now report 0 hard fails.

## F1–F7 verdict

| Gate | Verdict | Evidence |
|---|---|---|
| F1 page audit | **PASS** | Walked all 10 chapters against the coverage map. Every architecture/change unit (system block, score, split, step loop, pair update, before/after change) now maps to exactly one figure. Per-chapter audit tables list every unit id with claim/before/after/figure/medium/source/four-tests; audit row counts equal figure counts in all 10 files (4/3/4/4/2/5/4/3/5/4). Zero blank cells. |
| F2 medium ladder | **PASS** | First passing medium used throughout: tables for comparisons, scores, and before/after states (24); mermaid for flows, loops, and step sequences (14). No figure uses a heavier medium than its claim needs. Zero AI-generated images anywhere in the track. |
| F3 lesson plates | **PASS** | Every figure carries one claim (verified: one caption, one before/after or one rule each). Chapter plates not warranted in the markdown medium: the per-chapter figure-audit tables plus memory-aid mnemonics already connect the lesson plates; a dense plate would repeat prose (conciseness rule). |
| F4 chapter plates | **PASS** | See F3. Not warranted; the audit table is the chapter-level connector. |
| F5 captions | **PASS** | All 38 captions follow the law: "Figure N. Title. AI Podcast Curriculum, epXX (instructor, date). Shell K. <shell verb>. Source: …". Project named in every caption; source named (original toy / episode claims / "Great by Choice" ch. 3). |
| F6 reject list + numbers | **PASS** | No robot/brain/glow/clip-art/watermark/gradient anywhere (code-only figures). Every number is transcript-sourced (60% margins, $5B, $25 wire, 2–3%, 292:1, 50% scatter, 250%, $4,000, 10%/50%, $70k) or computed in-prose with the arithmetic shown (650×15=9,750M, 200→20=10%, $1.5M freedom fund). "Not in source" used once (ep03 fig3 ACH cost), per visual-system law. |
| F7 symbol consistency | **PASS** | Track-wide symbol table below. No symbol is drawn two different ways. Loops always mean procedures/cycles; tables always mean comparisons/scores; the same named object (flywheel, pain button, $5B loop, 292-to-1) keeps one shape everywhere. |

## Symbol table (F7)

| Symbol | First figure | Reused in |
|---|---|---|
| Reading-rank pair (1 min / 1–2 hrs) | ep01 fig1 | Q2 |
| Extract-and-apply arrow | ep01 fig2 | drills |
| Funnel 10,000 → 500 → 5 | ep01 fig3 | Q4, Drill 3 |
| Priority chain (5 rings) | ep01 fig4 | imbibe #5 |
| Two-paths split | ep02 fig1 | Q1, Q4 |
| Minus-5-or-plus-5 pair | ep02 fig2 | either-way portfolio, imbibe #5 |
| Rule-guardrail chain | ep02 fig3 | — |
| Derivative chain (1st/2nd/3rd) | ep03 fig1 | Q2, Drill 1 |
| $5B money loop | ep03 fig2 | Q6, Drill 5 |
| Seconds-for-pennies row | ep03 fig3 | Q7 |
| Equal-share rows | ep03 fig4 | Q8, Drill 6 |
| Gratitude-rush loop | ep04 fig1 | imbibe #1, Drill 1 |
| Three control columns | ep04 fig2 | Q3, imbibe #2, Drill 2 |
| Five-second test | ep04 fig3 | Q4, imbibe #3, Drill 3 |
| Belief-hygiene matrix | ep04 fig4 | Drill 6 |
| Card pipeline (7 steps) | ep05 fig1 | Q2 |
| Dead/live table | ep05 fig2 | Q7, Drill 5 |
| Kroger/A&P rows | ep06 fig1 | — |
| Flywheel / Doom loops | ep06 fig2 | Q&A, Drill 2, imbibe #2 |
| 292-to-1 outcome | ep06 fig3 | Q4, drills |
| Bullet → cannonball chain | ep06 fig4 | Q5, imbibe #4, Drill 4 |
| Five decline stages | ep06 fig5 | Q7, imbibe #6, Drill 6 |
| Three-doctor weights | ep07 fig1 | Q2, Drill 2 |
| Five-step loop | ep07 fig2 | drills |
| Amygdala / prefrontal pair | ep07 fig3 | Q6, Drill 5 |
| Pain-button loop | ep07 fig4 | Q4, imbibe #3, Drill 4 |
| Three pillars | ep08 fig1 | — |
| Harry Potter audience row | ep08 fig2 | Q&A, Drill 1 |
| Gift test | ep08 fig3 | Q4, imbibe #3, Drill 3 |
| Delay-intuition chain | ep09 fig1 | imbibe #1 |
| 50-percent scatter | ep09 fig2 | Q2, Drill 1 |
| Premortem chain | ep09 fig3 | Q3, Drill 2 |
| Base-rate row | ep09 fig4 | Julie example, Drill 3 |
| Springs (push / release) | ep09 fig5 | Q6, Drill 5 |
| Forced-move table | ep10 fig1 | Q2, Drill 1 |
| Bad-outcomes definition | ep10 fig2 | Q3, Drill 3 |
| Excess → correction → overshoot | ep10 fig3 | Q4, Drill 2 |
| Second-level table | ep10 fig4 | Q5, Drill 4 |

## Notes and open items for the coordinator

- **Conciseness holds.** No figure repeats prose without adding information: every table merges a comparison the prose states separately; every mermaid makes a procedure/loop visible that prose describes linearly. Nothing was added for decoration.
- **Corner `| |` cells** in comparison tables (e.g. ep04:185, ep10:44) are intentional markdown label positions, not blank data cells; every data cell is filled.
- **T3 is "none, static plate" on all 38 figures.** Honest: no figure exposes a reader-changeable number. The medium ladder reserves Canvas 2D for that case and no claim here needs it (same finding as the fix loop; unchanged).
- **ste_check:** 0 hard fails on all 10 edited files (warnings are pre-existing noun-cluster noise).
- **Not done:** browser shots, PDF visual pass, and GitHub push verification are outside the figure-enforcer scope; the coordinator's trust-by-verify pass should cover them.
