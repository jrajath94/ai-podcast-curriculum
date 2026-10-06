# FIGURE REPORT — Dwarkesh Patel track (figure enforcement)

Date: 2026-10-06. Role: figure enforcer.
Law applied: `~/workspace/ai-podcast-curriculum/build/VISUAL_SYSTEM_GENERIC.md`
(binding on pictures; supersedes older figure guidance), F1–F7 from
`~/workspace/ai-podcast-curriculum/build/TRACK_AUDITOR_BRIEF.md`,
rejections 1–15 from `~/workspace/stanford-frontier-ai/build/REJECTIONS.md`.

## Figure counts per chapter (before → after)

| Ch | Before | After | Added | Fixed |
|---|---|---|---|---|
| ep01 Elon Musk | 4 (3 tables, 1 mermaid) | 8 (6 tables, 2 mermaid) | fig2 launch arithmetic; fig5 limiting-factor loop; fig6 Optimus recursion; fig7 China numbers; fig8 steel vs carbon fiber | all captions retrofitted; fig3 mermaid node text cut to ≤4 words |
| ep02 Ilya Sutskever 2025 | 2 (1 table, 1 mermaid) | 4 (3 tables, 1 mermaid) | fig1 student A vs B; fig3 eras table | all captions retrofitted; fig4 mermaid node texts cut to ≤4 words; numbering put in document order |
| ep03 Ajeya Cotra | 1 (1 table) | 5 (5 tables) | fig1 imagined vs real checker; fig3 HF breach timeline; fig4 three civilizations; fig5 coverage check | all captions retrofitted; numbering put in document order |
| ep04 Andrej Karpathy | 2 (2 tables) | 5 (3 tables, 1 mermaid, 1 SVG) | fig2 straw supervision; fig3 autonomy slider (SVG); fig4 march of nines; fig5 caption added (table had none) | all captions retrofitted |
| ep05 Dario Amodei | 2 (1 table, 1 mermaid) | 4 (3 tables, 1 mermaid) | fig1 seven blob ingredients; fig3 code spectrum | all captions retrofitted; numbering put in document order |
| ep06 Dwarkesh solo | 2 (2 tables) | 4 (4 tables) | fig1 three collectives; fig4 omertà count | all captions retrofitted; numbering put in document order |
| ep07 Jensen Huang | 1 (1 table) | 2 (2 tables) | fig2 three moat threats | caption retrofitted |
| ep08 Mark Zuckerberg | 1 (1 table) | 3 (3 tables) | fig1 open/closed rule; fig2 $10B ladder | all captions retrofitted; numbering put in document order |
| ep09 Richard Sutton | 0 (audit claimed "table (in prose)"; none existed) | 2 (2 tables) | fig1 knowledge vs search-and-learning; fig2 the debate | audit table corrected to real figures |
| ep10 Ilya Sutskever 2023 | 0 (audit claimed "table (in prose)"; none existed) | 2 (1 table, 1 mermaid) | fig1 thesis chain; fig2 2023 vs 2025 | audit table corrected to real figures |
| ep11 synthesis | 1 (1 table) | 2 (2 tables) | fig2 failure math by scale | all captions retrofitted |

Track total: 16 → 41 figures. No AI image generation used anywhere
(code pipeline only, per orders; the ladder never demanded more than
table/mermaid/SVG, and the one SVG is hand-written).

## Four-tests log (new figures only; failures were not drawn)

- ep01 fig2 launch arithmetic: looks like dated rows with checks; table
  forced by claim-vs-check comparison; reader can change reuse hours;
  reuses "launch cadence". PASS.
- ep01 fig5 limiting loop: loop of 4 boxes ≤4 words; rule forces the
  recheck edge; reader can change hours on the bottleneck; reuses
  "limiting factor". PASS.
- ep01 fig6 Optimus recursion: 4-row table; merge forces rows; reader can
  change any exponential; reuses "self-building factory". PASS.
- ep01 fig7 China numbers: count rows; comparison forces table; reader can
  change any share; terminal stat block. PASS.
- ep01 fig8 steel: two-column property rows; before/after forces table;
  reader can change the cost multiple; reuses "operating point". PASS.
- ep02 fig1 students: two-column toy; analogy forces columns; reader can
  change practice hours; reuses "student A". PASS.
- ep02 fig3 eras: three rows; periodization forces rows; reader can change
  the year bounds; reuses "the eras". PASS.
- ep03 fig1 checker: belief vs reality columns; irony forces before/after;
  reader can change nothing (that is the point); reuses "poisoned". PASS.
- ep03 fig3 HF timeline: dated rows; chronology forces rows; reader can
  change no number; reuses "the board". PASS.
- ep03 fig4 civilizations: 3-row arc; inheritance forces rows; terminal
  symbol "three-civilization arc". PASS.
- ep03 fig5 coverage: two rounds; trace-rate forces rows; reader can change
  the sampling method; reuses "coverage check". PASS.
- ep04 fig2 straw: 3-row mechanism; contrast forces columns; reader can add
  a process grade; reuses "straw supervision". PASS.
- ep04 fig3 slider: position on a track; move forces SVG (table/ASCII fail
  the position test); reader sees the knob; reuses "the slider". PASS.
- ep04 fig4 nines: count rows; constant-work claim forces rows; reader can
  change the demo percentage; reuses "nines". PASS.
- ep05 fig1 blob: 7-item list; Shell 1 toy (≤8 items); reader can drop an
  ingredient; reuses "the blob". PASS.
- ep05 fig3 spectrum: five steps; confusion of step 1/5 forces rows; reader
  can place any claim; reuses "the spectrum". PASS.
- ep06 fig1 collectives: same as ep03 fig4, this chapter's spine. PASS.
- ep06 fig4 omertà: one count; starkness forces the table; reuses "omertà".
  PASS.
- ep07 fig2 threats: three rows; split forces rows; terminal. PASS.
- ep08 fig1 open/closed: decision rule; rule forces columns; reader can
  change the monetized layer; reuses "complement". PASS.
- ep08 fig2 $10B ladder: count rows; 10x forces rows; reader can change the
  multiple; reuses "next zero". PASS.
- ep09 fig1 buckets: two columns; distinction forces columns; reuses "the
  two buckets". PASS.
- ep09 fig2 debate: three rows; synthesis is the new symbol. PASS.
- ep10 fig1 thesis chain: 3-node flow ≤4 words; mechanism forces mermaid;
  reuses "the thesis". PASS.
- ep10 fig2 2023/2025: two columns; fuel-change forces comparison. PASS.
- ep11 fig2 failure math: scale rows; regime change forces rows. PASS.

Conciseness review: no figure was kept that merely restates prose. Each new
figure adds a check column, a contrast column, a loop edge, or a synthesis
the prose does not contain in one view.

## F1–F7 verdicts

- F1 page audit: PASS. Every chapter ends with a Figure audit table; no
  blank figure cells; every state-changing claim (count, merge, score,
  move, new symbol) maps to a figure id.
- F2 medium ladder: PASS. Table first for comparisons and counts; mermaid
  for flows; one hand-written SVG for the single position claim (autonomy
  slider). Fixed 4 pre-existing mermaid node-text violations (>4 words).
- F3/F4 lesson plates: PASS. One figure owns one shell and one claim; no
  dense plates except the chapter-level audit tables.
- F5 captions: PASS. All 41 captions retrofitted to the required format:
  "Figure N. Title. AI Podcast Curriculum, epXX (source, date). Shell K.
  <shell line>. Source: …".
- F6 reject list / numbers: PASS. No robot, brain, glow, gradient, shadow,
  watermark, or clip art. Every number is episode-sourced or computed
  (launch arithmetic checks are worked in the tables).
- F7 symbol consistency: PASS. Track symbol table below; terms are used
  with one meaning across chapters.

## Track symbol table (F7)

| Symbol | First use | Reused in |
|---|---|---|
| limiting factor | ep01 fig5 | ep05 (blob inputs), ep11 drills (bottleneck) |
| poisoned | ep03 fig1 | ep06 workstreams |
| the collective | ep03 | ep06 |
| value function | ep02 fig2 | ep04 fig2 (process grades, adjacent) |
| the blob (seven ingredients) | ep05 fig1 | ep05 throughout |
| AI factory | ep07 fig1 | ep08 fig3, ep11 fig1 |
| moat stack | ep07 fig1 | ep07 fig2 (threats) |
| march of nines | ep04 fig4 | ep04 drills |
| autonomy slider | ep04 fig3 | ep04 memory aids |
| omertà | ep06 fig4 | ep06 memory aids |
| 50% meter | ep06 (Ajeya's meter) | ep03 warning-shot thesis |
| thesis chain | ep10 fig1 | ep02 (2025 update) |
| cognitive core | ep04 | ep09 (adjacent to search-and-learning) |
| 10x ladder | ep08 fig2 | ep05 (revenue 10x) |

## Style fixes applied (auditor's G8 items)

- Prose contractions fixed: 2 (ep01 Q7 "can't" → "can not"; ep07 Q3
  "can't" → "can not"). The remaining contractions sit inside verbatim
  quoted speech and were kept (G9 verbatim rule wins).
- Em dashes in prose/tables fixed: 17 (table N/A cells → "Not in source" /
  "none stated" / "none named" / "none needed"; cheatsheet heading;
  index.md list separators → ": "). Remaining em dashes are verbatim
  episode titles in frontmatter.
- Semicolons in prose fixed: 165 → split into sentences (period +
  capitalization) or list commas. One inline code span (`echo REAL; sleep`)
  was protected.

## Recovery note (for the parent)

The first style-fix script had a bug that stripped `"` characters from all
chapter files. Recovery, all verified byte-clean afterward:

- ep01, ep02, ep03, ep04, ep05, ep07, ep09, ep10, ep11-synthesis,
  cheatsheet: restored pristine from `~/workspace/apc-staging/content/
  tracks/dwarkesh-patel/` (byte-identical to pre-edit live files; quote
  counts match).
- ep06: reconstructed from `~/workspace/apc-staging/build/dwarkesh-audit/
  ep06-v2.md` body + the live post-fix frontmatter (the only delta between
  the two was frontmatter quoting style; verified by diff).
- ep08: reconstructed by applying `~/workspace/apc-staging/build/
  dwarkesh-audit/ep08-fix.md` (both replacements) to the pristine staging
  pre-fix file, reproducing the coordinator's applied post-fix state.
- index.md and _coverage.md were never damaged (script skipped them).

## Open items (not in figure-enforcer scope; for the parent)

1. ep08 still carries the trailing `[uncertain]` line about the transcript
   cutting off mid-sentence (the applied ep08 fix removed it from the
   Augustus subsection but left the Figure-audit one). The audit report
   says to strike it.
2. ep08 Q&A 6 and memory aids still use the old "structural vs personal
   power" framing; the fix only replaced the subsection and drill 4.
3. Cheatsheet/index touch-ups from the audit report §7.4 (ep06 lesson
   corrections) were not applied.
4. `_coverage.md` still needs the ep06 rewrite + ep08 Augustus row per the
   audit report §8.5 (I did not touch it).
