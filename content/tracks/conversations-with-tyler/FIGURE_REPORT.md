# FIGURE REPORT — Conversations with Tyler track
Enforcer: figure-enforcer subagent (depth 2/2). Date: 2026-10-06.
Sources read verbatim: VISUAL_SYSTEM_GENERIC.md, REJECTIONS.md, TRACK_AUDITOR_BRIEF.md, plus AUDIT_REPORT.md and FIX_REPORT.md (both 2026-10-06).
Scope: ep01.md–ep10.md at `~/workspace/ai-podcast-curriculum/content/tracks/conversations-with-tyler/`.

## Method
1. Read VISUAL_SYSTEM_GENERIC.md, REJECTIONS.md, TRACK_AUDITOR_BRIEF.md verbatim.
2. Read all 10 chapters end to end. For each figure: checked placement against its claim prose, caption format, shell assignment, medium-ladder position, table cells (no blanks), and reject-list compliance.
3. Post-restructure focus (ep04 45 `###` subchapters, ep05 23 `###`): verified every figure caption still exists, numbering still sequential, and each figure still sits inside or adjacent to the section carrying its claim.
4. Programmatic checks: figure caption counts per chapter, audit-table unit-row counts per chapter, blank-cell scan, caption format regex, duplicate-number scan.

## Figures per chapter

| Chapter | Lesson figures | Chapter plate | Total | Audit rows |
|---|---|---|---|---|
| ep01 Gladwell | 1 five-part model · 2 way station vs dead end · 3 Court vs data · 4 education vs luxury · 5 spend-to-zero vs endowment · 6 exclusivity vs opportunity · 7 backlash pattern | 8 The base beats the peak | 8 | u01–u08, no blanks |
| ep02 Paglia | 1 Bloom saga ledger · 2 culture cycle · 3 Brazil vs North America · 4 Stones vs Beatles · 5 pay gap decomposition · 6 two diets of attention | 7 The mall beats the seminar | 7 | u01–u07, no blanks |
| ep03 Kotkin | 1 three Siberias · 2 cybernetics fantasy · 3 three architectures · 4 collectivization arithmetic · 5 two theories of Stalin · 6 four partitions | 7 Power explains the monster | 7 | u01–u07, no blanks |
| ep04 Thiel I | 1 three options on terrible history · 2 two theories of history · 3 two apocalypses · 4 the katechon, three cases · 5 the math-verbal reversal | 6 Integration beats specialization | 6 | u01–u06, no blanks |
| ep05 Thiel II | 1 two-track stagnation · 2 vertical vs horizontal progress · 3 two globalization peaks · 4 company names as forecasts · 5 inequality's three questions | 6 The margin beats the average | 6 | u01–u06, no blanks |
| ep06 Lahiri | 1 naming Rhode Island · 2 the taped translation · 3 two blindnesses · 4 forced vs chosen language · 5 uniform vs costume | 6 Translation as belonging | 6 | u01–u06, no blanks |
| ep07 Pinker | 1 the two machines · 2 the erosion machine · 3 the wall · 4 the treadmill | 5 Reason is grafted, not given | 5 | u01–u05, no blanks |
| ep08 Deutsch | 1 the transporter decision · 2 the Everett bubble · 3 the Zeus wall | 4 No barriers, anywhere | 4 | u01–u04, no blanks |
| ep09 Austin | 1 the 90 percent rule · 2 ideal form vs real pole · 3 better vs different | 4 Learn to look | 4 | u01–u04, no blanks |
| ep10 Ferguson | 1 three pessimisms · 2 the mundane middle · 3 Collingwood's method · 4 the Empire audit | 5 The past is an instrument | 5 | u01–u05, no blanks |
| **Track total** | | | **58** | |

## F1–F7 verdicts

| Chapter | F1 page audit | F2 medium ladder | F3/F4 lesson + chapter plates | F5 captions / no blank cells | F6 reject list / numbers | F7 symbol consistency | Verdict |
|---|---|---|---|---|---|---|---|
| ep01 | PASS | PASS | PASS | PASS | PASS | PASS | PASS |
| ep02 | PASS | PASS | PASS | PASS | PASS | PASS | PASS |
| ep03 | PASS | PASS | PASS | PASS | PASS | PASS | PASS |
| ep04 | PASS | PASS | PASS | PASS | PASS | PASS | PASS |
| ep05 | PASS | PASS | PASS | PASS | PASS | PASS | PASS |
| ep06 | PASS | PASS | PASS | PASS | PASS | PASS | PASS |
| ep07 | PASS | PASS | PASS | PASS | PASS | PASS | PASS |
| ep08 | PASS | PASS | PASS | PASS | PASS | PASS | PASS |
| ep09 | PASS | PASS | PASS | PASS | PASS | PASS | PASS |
| ep10 | PASS | PASS | PASS | PASS | PASS | PASS | PASS |

Verdict basis, per gate:

- **F1 (page audit):** Every state-changing claim (count, merge, score, before/after contrast) has a figure; every figure has a matching unit row in the chapter's figure-audit table. Post-restructure check: ep04 figures 1–5 still close their original `##` sections (Three options → Fig 1; Schmitt → Fig 2; Antichrist → Fig 3; katechon → Fig 4; AI → Fig 5); ep05 figures 1, 3, 4, 5 still close their sections (Fig 3 stays at the end of the Brazil subchapter, Fig 5 at the end of the Gresham subchapter, both confirmed from the fix report). Narrative claims without a state change (satire mechanism, Georgia Tech story, Fermi stress tests, lightning rounds) correctly have no figure — the spec only mandates figures for state changes.
- **F2 (medium ladder):** All figures are tables, the first medium that passes for comparison-of-values claims. Step-sequence tables (ep06 Fig 2 taped translation, ep07 Figs 2/4, ep08 Fig 2 bubble stages, ep10 Fig 3 Collingwood steps) are count/step toys where the ladder bans mermaid for counts; table passes first. No ASCII/mermaid/SVG needed anywhere. Code pipeline only — zero AI-generated images in the track.
- **F3/F4 (lesson plates + chapter plates):** Every lesson figure encodes exactly one claim (before/after columns, one rule). Every chapter ends with a chapter plate carrying Left (cost without the rule) / Center (the stored object) / Right (cost with it), a one-line Tradeoff, and a one-sentence Footer. All chapter-plate numbers come from the page (ep02 "59 mentions of Foucault", ep05 "$100K experiments" / "175-degree talent", ep06 "the million drafts", ep09 "3 to 4 percent", ep10 "the 17 books").
- **F5 (captions + cells):** All 58 captions match the required form: "Figure N. Title. AI Podcast Curriculum, epXX (source, date). Shell K. <shell line>. Source: …". Programmatic blank-cell scan of all 10 audit tables: 0 blank cells. `N/A` cells (ep10 Fig 1) and `[uncertain: not observed]` (ep01 Fig 4) are honestly marked, not blank.
- **F6 (reject list + numbers):** Text tables only — no robot, brain, glowing network, Comic Sans, watermark, logo, or decorative element; each lesson plate carries one rule. Numbers are transcript-sourced or hand-computed with the arithmetic shown in prose (ep01 endowment arithmetic independently recomputed by the auditor: 0.95^20 ≈ 0.36, 0.95^100 ≈ 0.006; ep05 10,000:1 from $100K/$1B).
- **F7 (symbol consistency):** No drawn symbols track-wide (all tables); naming is fully uniform: "Figure N." prefix, "(chapter plate)" modifier on plates, shell phrases verbatim from the spec (Shell 1 "Show the toy", Shell 2 "Count the toy", Shell 3 "Apply the one rule", Shell 5 "Name the next page that reuses the symbol"), identical audit-table columns in all 10 chapters. Shell 4 never used — no figure introduces a new graphical symbol, consistent with the tables-only medium choice.

## Four-tests and conciseness check
- Spot-applied the four tests to every figure: each names its object (the table), its rule (the before/after columns), its changeable value (the chosen option, ratio, or count), and a reusable symbol named in the chapter plate footer (e.g. "the broad base", "the 24/7 eye", "the margin").
- Conciseness: **no figure killed.** Every figure carries at least one row that adds structure beyond the prose (a named rule, a forecast, a response function, or examples present only in the figure, e.g. ep05 Fig 2 "The next Zuckerberg does not do social networks"). Chapter plates are the single allowed dense plate per chapter.

## Borderline notes (not fails)
1. **ep05 Fig 2 placement:** "Vertical versus horizontal progress" sits at the end of the "Talent: the 175-degree opposites" section (line 92), ~88 lines before the main vertical-progress prose (line 178–180, "### Vertical progress tips"). This placement predates the restructure (fix preserved content verbatim in order) and was auditor-passed. Moving it would break sequential numbering; left in place.
2. **ep02 Fig 1 header/shape:** last row ("Response to rejection | Infuriation, not discouragement") is non-numeric under an "Item | Number" header. Kept — it encodes the saga's response function, the unit's actual point, and the cell is not blank.
3. **Numbering:** verified 1..N sequential in all 10 chapters, caption count == audit-row count in every chapter, no duplicates, no gaps.
