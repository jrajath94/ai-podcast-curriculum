# FIGURE REPORT — Acquired track, AI Podcast Curriculum
Date: 2026-10-06. Enforcer pass against the binding law
~/workspace/ai-podcast-curriculum/build/VISUAL_SYSTEM_GENERIC.md
(which supersedes the old VISUAL_SYSTEM.md on pictures) plus
TRACK_AUDITOR_BRIEF.md gates F1-F7.

## Method
1. Read VISUAL_SYSTEM.md, REJECTIONS.md, TRACK_AUDITOR_BRIEF.md,
   then the new VISUAL_SYSTEM_GENERIC.md verbatim.
2. Read all 11 chapters (ep01-ep11-synthesis), cheatsheet, index.
3. Walked every state-changing claim (a number that moves, a mechanism
   with steps, a before/after, a comparison). Added 32 missing figures
   inline, all on the medium ladder (table / ASCII / mermaid).
4. Retrofitted all 69 captions to the new law:
   "Figure N. <Title>. AI Podcast Curriculum, epXX (<source>, <date>).
   Shell K. <shell line>. Source: <original toy | original table>..."
5. Assigned one russian-doll shell per figure (Shell 1 show the toy,
   Shell 2 count or score the toy, Shell 3 apply the one rule,
   Shell 4 show the new symbol). Symbol reuse across chapters is
   noted in the F7 section below.
6. Mechanical verification after every edit: figure numbering sequential
   per chapter, every mermaid graph <= 8 nodes with <= 4 words per node,
   every ASCII block <= 12 lines, no blank cells in any table, every
   audit-table figure id resolves to a caption.

## Figure counts per chapter (final)
| Chapter | Before | After | Added |
|---|---|---|---|
| ep01 (Jensen Huang) | 7 | 9 | 2 |
| ep02 (Morris Chang) | 4 | 6 | 2 |
| ep03 (Zuckerberg) | 6 | 7 | 1 |
| ep04 (Google III) | 3 | 7 | 4 |
| ep05 (Google I) | 3 | 5 | 2 |
| ep06 (Microsoft I) | 4 | 7 | 3 |
| ep07 (Meta) | 3 | 7 | 4 |
| ep08 (Nvidia II) | 2 | 6 | 4 |
| ep09 (Nvidia I) | 1 | 3 | 2 |
| ep10 (Nvidia III) | 1 | 8 | 7 |
| ep11 (Hardware synthesis) | 3 | 4 | 1 (caption only; DGX table previously had none) |
| TOTAL | 37 | 69 | 32 |

Removed: 0. Every existing figure passed the four tests and the
conciseness bar (each adds a before/after, a count, or a mechanism
the prose does not already show in that shape), so none were cut.

## Added figures, with locations
- ep01: fig3 Scale and emergence (table, Shell 2) in "CUDA: the
  emergence evidence"; fig5 The data-center journey (mermaid, Shell 3)
  in "The data center: separating compute from the screen".
- ep02: fig4 Why Intel could not be the foundry (table, Shell 1) in
  "Winning Apple"; fig6 The learning curve as a loop (mermaid, Shell 3)
  in "The learning curve".
- ep03: fig3 Ship culture: Meta versus Apple (table, Shell 1) in
  "Ship before you are proud".
- ep04: fig2 The TPU trade (table, Shell 1) in "The TPU";
  fig3 The talent exodus (table, Shell 1) in "The publication and its
  cost"; fig7 Seven powers: search era versus AI era (table, Shell 2)
  and fig6 The token scale explosion (table, Shell 2) in
  "The value-capture problem" / Gemini section.
- ep05: fig3 The AOL bet, in arithmetic (table, Shell 2) in "The AOL
  bet"; fig5 The revenue detonation, 2001-2003 (table, Shell 2) in
  "AdSense and the end of trade-offs".
- ep06: fig4 The hedge: OS/2 versus Windows (table, Shell 1) in
  "Windows: the hedge that won"; fig5 Ownership at the 1986 IPO
  (table, Shell 2) in "Capital efficiency"; fig7 The seven powers,
  1975-1995 (table, Shell 2) in "The seven powers".
- ep07: fig1 Share of the species (table, Shell 2) in "The scale";
  fig4 The five mobile breaks (table, Shell 1) in "The mobile crisis";
  fig6 Town square to living room (ASCII, Shell 3) in
  "Town Square to living room"; fig7 The two maths of Reality Labs
  (table, Shell 1) in "Reality Labs: the $60 billion hedge".
- ep08: fig2 The drawdown and the decade of disbelief (table, Shell 2)
  in "The 80 percent collapse"; fig3 Three rushes, one shovel
  (table, Shell 1) in "Crypto"; fig4 The data-center 3X (table,
  Shell 2) in "The data center pivot"; fig5 Capital efficiency
  (table, Shell 1) in "The 2022 numbers".
- ep09: fig1 The primitive bet (table, Shell 1) in "Death #1";
  fig3 The revenue rocket and the plateau (table, Shell 2) in
  "The revenue rocket and the plateau".
- ep10: fig1 The scaling ladder, GPT-1 to GPT-4 (table, Shell 2);
  fig2 The OpenAI-Microsoft funnel (mermaid, Shell 3);
  fig4 The DGX bundle math (ASCII, Shell 2); fig5 The detonation
  quarter (table, Shell 2); fig6 The CUDA developer curve (table,
  Shell 2); fig7 The replication test (table, Shell 1);
  fig8 Export controls hit the revenue line (table, Shell 1).

## Fixed figures (existing, repaired)
- F6 blank header cells: ep01 fig7 (hyperscale table), ep02 fig1
  (foundry bet), ep03 fig3 (invention vs discovery), ep04 fig1
  (dilemma) all had an empty first header cell; filled with "Axis"
  or "Dimension".
- F6 mermaid 4-word node rule: ep02 fig2 "Morris retakes CEO at 78"
  -> "Morris retakes CEO"; ep02 fig5 "Williams: all 16 when ready"
  -> "Williams promises all 16"; ep02 fig2 "700 laid off by rating"
  -> "700 laid off"; ep03 fig5 "No edge in keeping it closed"
  -> "No edge keeping closed"; ep08 fig6 all nodes rewritten to
  <= 4 words; ep11 fig4 three nodes rewritten to <= 4 words.
- F5: all 69 captions retrofitted to the new law (project + shell +
  source). ep11's DGX spec table had no caption; it is now
  Figure 2 with source labeled as built from the official spec.
- F1: every chapter's "## Figure audit" table rewritten to the full
  per-page audit format (unit id, claim, before, after, figure id,
  medium, source). No blank cells. Units with no state change are
  marked "(none, ...)" explicitly rather than left blank (see F1 note).
- F7: index.md and cheatsheet.md claimed "40+ direct reports, no
  1:1s"; ep01 does not state "no 1:1s". Removed the phrase in both
  files so the track agrees with the chapter.

## F1-F7 verdict
- F1 (page audit): PASS. Every state-changing claim maps to a real
  inline figure; audit tables have the full 7 columns with no blank
  cells. Five static units carry an explicit "(none, ...)" figure cell
  with the reason, per the binding law's decision rule (draw ONLY on
  state change; a static list or ratio fails the four tests, so no
  figure is drawn): ep05 u06 (seven-point playbook), ep09 u05 (Xbox
  deal terms) and u06 (2006 bear/bull narrative), ep10 u09 (employee
  efficiency ratio), ep11 u05 ([E]/[S] tagging rule). These are not
  blank cells; they are honest no-draw decisions.
- F2 (medium ladder): PASS. Tables for comparisons, ASCII traces
  (<= 12 lines, before/after lines), mermaid for flows (<= 8 nodes).
  No generated image plates exist and none were needed; the ladder
  serves every state change, so the code-pipeline-only rule for
  generated plates was never triggered. No AI image generation, no
  OpenRouter, per the law.
- F3/F4 (lesson plates / chapter plates): PASS by ladder figures;
  no separate generated plates exist in this track (assets/ is empty).
- F5 (captions): PASS. 69/69 captions name "AI Podcast Curriculum",
  the shell (1-4), and the source (episode claims, or the named
  official spec for ep11).
- F6 (reject list; numbers sourced): PASS. No decorative figures;
  no blank cells; every mermaid node <= 4 words; every ASCII <= 12
  lines. The audit Source column marks each figure's numbers as
  "episode claims" (transcript-sourced) or "computed in prose" /
  "computed from specs" (ep10 fig4 bundle margin, ep11 fig3 Fermi
  cluster). No invented numbers.
- F7 (symbol consistency): PASS. Track-wide check: H100
  ($40,000 / 250B transistors / ~20,000 cores / 700W / 80GB HBM3 at
  3.35 TB/s / NVLink 900 GB/s vs PCIe 128 GB/s), DGX H100 ($500K,
  8x$40K=$320K, ~$180K margin), CUDA developer curve
  (100K/1M/2M/3M/4M) and 10,000 person-years, 500M CUDA-capable GPUs,
  CoWoS 10-15 percent of TSMC capacity, China 25 percent of revenue,
  TSMC 8 percent R and D / $6B capex, Nvidia gross margin 24
  percent -> 70+ percent. All consistent across chapters and figures.
  Symbol reuse across chapters (Shell 5 intent): the RIVA/emulation
  chain (ep01 -> ep09), CUDA flywheel and person-years (ep01 ->
  ep08 -> ep10), H100/DGX symbols (ep10 -> ep11), the seven powers
  (ep04 -> ep06), the learning curve (ep02), the town-square/living-
  room pair (ep07). Same terms, same units, same abbreviations
  everywhere.

## Conciseness bar (figures)
Reviewed every pre-existing figure against the bar: kill any figure
that repeats what the prose already teaches without adding
information. Result: 0 removed. Each figure encodes a before/after,
a counted score, or a mechanism in a shape the prose lacks
(flow order, loop, score matrix, one-card spec). Added figures only
where the prose made a state-changing claim with no figure.

## Notes for the parent / content team
- Pre-existing style hits (outside my added text; my added text is
  clean): 15 contraction hits in prose/quotes (ep02 "couldn't",
  ep03 "IPO'd", ep04 "didn't"/"can't" x3, ep07 "we're" x6 mostly in
  the Zuckerberg 2012 email quote, ep08 "3X'd" x2, "We've"/"we're" in
  the Andreessen quote, "didn't"). Flagged for the content fixer, not
  touched here since this pass is figures-only.
- The audit-table "(none, ...)" rows are deliberate per the binding
  law, not gaps. If the coordinator wants zero such rows, the
  alternative is to delete those prose passages, which is a content
  decision, not a figure one.
- No chapter plates (dense end-of-concept plates) exist in this
  track; the ladder figures are the lesson plates. If Raj wants
  generated plates, that is a separate build task under the code-
  pipeline-only rule.
