# FIGURE REPORT: Hidden Brain track
# Figure enforcer pass. Date: 2026-10-06.
# Scope: ep01.md through ep07.md. Read verbatim first: VISUAL_SYSTEM_GENERIC.md,
# REJECTIONS.md, TRACK_AUDITOR_BRIEF.md (FIGURE GATES F1-F7).

## Method

- Walked every chapter top to bottom. Listed every state-changing claim
  (count, merge, score, mask, move, new symbol).
- Applied the four tests before drawing. Failed any test means no drawing.
- Applied the medium ladder. Table won for comparisons. ASCII won for the
  bridge trace. Mermaid won for flows and loops. No claim needed SVG,
  Canvas, 3D, Manim, or Hyperframes, so none was drawn.
- No AI image generation was used anywhere in this pass. Code and text
  pipeline only.
- Every number is episode-sourced (labeled in the caption) or hand-computed
  with the arithmetic shown. Nothing invented.

## Figure inventory: 34 figures

### ep01: Why You Are Always Overwhelmed, 6 figures

| Fig | Title | Medium | Shell | Source |
|---|---|---|---|---|
| 1 | The Duplo bridge, two solutions | ASCII | 3 | original toy, from episode claims |
| 2 | The essay experiment | table | 2 | episode claims |
| 3 | The biology loop | mermaid | 3 | original toy, from episode claims |
| 4 | The Embarcadero, before and after subtraction | table | 3 | episode claims |
| 5 | Pronovost's subtraction | table | 3 | episode claims |
| 6 | The subtraction experiments, side by side | table | 2 | episode claims |

### ep02: Why Your Brain Works NOTHING Like You Think, 5 figures

| Fig | Title | Medium | Shell | Source |
|---|---|---|---|---|
| 1 | The bird's two attentions | table | 2 | original toy, from episode claims |
| 2 | The moral experiment, rTPJ intact versus disabled | table | 3 | episode claims |
| 3 | Denial after stroke | table | 3 | episode claims |
| 4 | Master and emissary | mermaid | 4 | original toy, from episode claims |
| 5 | The whole-part-whole practice loop | mermaid | 3 | original toy, from episode claims |

### ep03: Why You Are Not As Broken As You Believe, 5 figures

| Fig | Title | Medium | Shell | Source |
|---|---|---|---|---|
| 1 | 9/11 PTSD rates over time | table | 3 | episode claims |
| 2 | The four trajectories | table | 2 | episode claims |
| 3 | The grief script versus the evidence | table | 3 | episode claims |
| 4 | The therapist's sample versus the population | table | 2 | episode claims |
| 5 | How a trigger warning backfires | mermaid | 3 | original toy, from episode claims |

### ep04: Brave People Share One Thing, 3 figures

| Fig | Title | Medium | Shell | Source |
|---|---|---|---|---|
| 1 | Social discounting: generosity by social distance | table | 2 | original toy, from episode claims |
| 2 | Amygdala size and distress recognition | table | 2 | episode claims |
| 3 | Two models of courage | table | 3 | original toy, from episode claims |

### ep05: The Hidden Power Of Forgetting, 6 figures

| Fig | Title | Medium | Shell | Source |
|---|---|---|---|---|
| 1 | Jill Price versus a typical memory | table | 2 | episode claims |
| 2 | The city-grid model of memory access | mermaid | 2 | original toy, from episode claims |
| 3 | Grade recall accuracy | table | 2 | episode claims |
| 4 | The mood-memory loop | mermaid | 3 | original toy, from episode claims |
| 5 | The memory model, before and after | table | 3 | original toy, from episode claims |
| 6 | The Chris study: who gets the generous edit | table | 2 | episode claims |

### ep06: The Secret Coding in Your Brain, 4 figures

| Fig | Title | Medium | Shell | Source |
|---|---|---|---|---|
| 1 | The three quiz items: what you remember versus what is real | table | 2 | episode claims |
| 2 | What predicts memorability in the museum study | table | 2 | episode claims |
| 3 | How ResMem learns | mermaid | 3 | original toy, from episode claims |
| 4 | ResMem's masterpiece test | table | 3 | episode claims |

### ep07: Why You Choke Under Pressure, 5 figures

| Fig | Title | Medium | Shell | Source |
|---|---|---|---|---|
| 1 | The working-memory ladder | table | 2 | original toy, from episode claims |
| 2 | Reframing arousal | table | 3 | original toy, from episode claims |
| 3 | The four solutions and their mechanisms | table | 3 | original toy, from episode claims |
| 4 | The hijack: what occupies the store | table | 3 | original toy, from episode claims |
| 5 | The yellow square: pain before the problem | table | 2 | original toy, from episode claims |

## Fixes applied (correctness)

1. ep01 fig1 ASCII was internally wrong. The SUBTRACT column showed Tower A
   unchanged at 5 blocks and Tower B at 4 with the label "level, 5 blocks".
   Five does not equal four, so the bridge was not level, and the total was
   9 blocks, not 5. The ADD column said "level, 6 blocks" for 5 plus 5.
   Fixed: BEFORE uneven at 9 blocks, ADD level at 10 blocks, SUBTRACT level
   at 8 blocks with the minus-one on Tower A.
2. ep01 Duplo prose said "Half the material." The transcript uses that phrase
   only for Keichline's hollow block (transcript line 399), never for the
   Duplo bridge (lines 91-104 give no tower heights and no material claim).
   Removed the phrase from the Duplo section. The fixed figure shows the true
   toy arithmetic: 8 blocks versus 10.
3. ep02 fig4 mermaid broke the mermaid rule. Node text ran to 8 words. The
   rule allows 4. Rebuilt as a 2-node asymmetric graph with 4-word and 3-word
   node text. The solid edge is "needs". The dashed edge is "denies".
4. ep03 fig1 applied "Back to near normal" to all three subgroups. The
   transcript gives the 6-month reading for the city as a whole only.
   The column header now reads "At 6 months (city-wide reading)".
5. ep05 fig1 and prose said Jill recalled clouds "at 3 p.m." The transcript
   says "about 3:00" with no a.m. or p.m. Both now read "about 3:00".
6. ep02 audit table claimed master/emissary symbols were "reused across
   chapters". The word "emissary" appears only in ep02. The row now says
   "reused within the chapter (Q&A 4-6, drills 5-6)". The matching prose
   under fig4 was softened the same way.

## Additions (8 new figures, F1 gaps closed)

1. ep01 fig6: the five Klotz experiments side by side (essay 17%, recipe
   2 of 90, music 3-to-1, itinerary 1 in 4, UVA under 10%). The prose listed
   them in separate sections. The table shows the family pattern: the
   subtract rate is always the small number. All values episode-sourced.
2. ep02 fig5: the whole-part-whole practice loop as a mermaid cycle. The
   spec mandates a figure for every step loop. The loop is reused in Q&A 5,
   imbibe practice 1, and drill 5.
3. ep03 fig4: the therapist's sample versus the population. The section's
   whole claim is the sampling gap: the profession that defines normal meets
   the chronic 10 percent, not the resilient majority.
4. ep03 fig5: the trigger-warning causal chain as a mermaid flow. Warning to
   brace to rigidity to more anxiety. The prose states the chain. The figure
   gives it a shape reused by the warning trap card.
5. ep05 fig5: filing cabinet versus reconstruction, before and after. The
   section replaces one model of memory with another. The spec mandates a
   figure for every schema change.
6. ep05 fig6: the Chris study as a 2-by-2 table (target by valence). The
   interaction is the claim: the generous edit applies to the self, not to
   the stranger.
7. ep07 fig4: the hijack as working-memory occupancy, before and after.
   The chapter's central mechanism had no figure. The store holds the plan
   normally and the worry when hijacked.
8. ep07 fig5: the yellow-square result as a two-group table. The claim is
   about timing. Pain circuitry fires at the warning, before any math.

## Units with no figure (justified, no blank cells)

Each chapter's figure audit table now maps every state-changing unit. Units
without figures carry the reason in the Four tests column. Summary of the
reasons: the episode gives no counts (grid experiment, laughter-health
correlation), the claim is a single number fully carried by one prose
sentence (exam 98 vs 47, Springsteen 50 to 10, COVID binary contrast), the
table would restate a list the prose already enumerates (three risks, oath
story), the figure would invent numbers (1/N bystander model), or the unit
is a narrative illustration of a figured mechanism (Curry, Booker, Meng Po,
bike crash). Row counts per chapter audit table: ep01 11, ep02 8, ep03 8,
ep04 6, ep05 9, ep06 7, ep07 9. Zero blank cells in all 58 rows.

## F1-F7 verdicts

| Gate | ep01 | ep02 | ep03 | ep04 | ep05 | ep06 | ep07 |
|---|---|---|---|---|---|---|---|
| F1 page audit, every state-changing claim mapped | PASS | PASS | PASS | PASS | PASS | PASS | PASS |
| F2 medium ladder honored | PASS | PASS | PASS | PASS | PASS | PASS | PASS |
| F3 lesson plates, one claim each | PASS | PASS | PASS | PASS | PASS | PASS | PASS |
| F4 chapter plates present, 4-column shape | PASS | PASS | PASS | PASS | PASS | PASS | PASS |
| F5 captions name project, source, shell | PASS | PASS | PASS | PASS | PASS | PASS | PASS |
| F6 reject list, numbers sourced or computed | PASS | PASS | PASS | PASS | PASS | PASS | PASS |
| F7 symbols consistent track-wide | PASS | PASS | PASS | PASS | PASS | PASS | PASS |

F1 detail: every figure changes reader state (count, before/after, flow,
loop, or new symbol). No decorative figures found. No figure repeats prose
without adding structure. The conciseness rule removed zero existing figures
and blocked six candidate figures (documented in the audit tables).

F2 detail: table was the first passing medium for all comparisons and
before/after claims. ASCII was the first passing medium for the bridge
trace. Mermaid was the first passing medium for flows and loops. No claim
required position, count geometry, drag interaction, space, or timed proof,
so SVG, Canvas, three.js, Manim, and Hyperframes were never reached.

F5 detail: all 34 captions follow the required shape. Example: "Figure 6.
The subtraction experiments, side by side. AI Podcast Curriculum, ep01
(Leidy Klotz, 2026-04-20). Shell 2. Count or score the toy. Source: episode
claims." Shell lines used: Shell 2 (count or score the toy), Shell 3 (apply
the one rule), Shell 4 (show the new symbol).

F6 detail: reject list clean. No robot, brain, glowing network, stock photo,
Comic Sans, watermark, clip art, gradient, glow, or shadow anywhere. Every
number traces to the episode transcript (caption-labeled) or to hand-worked
arithmetic shown in prose (44-to-1, 89/29 three-to-one, 35 oath words).
The ep05 mermaid style fills use flat spec colors only (green device
#D9E8D3, pink pool #F3D4D8).

F7 detail: symbol cross-check across all 7 chapters. "Loop" appears in four
chapters, always qualified (reward loop, practice loop, mood loop, training
loop). "Store" appears only in ep07. "Circle" appears only in ep04.
"Chip" language is consistent (narrow/wide, intent/outcome, denial, Jill,
road/alley, 89/29, digit, fuel). No symbol means two different things
anywhere. No conflicts found.

## Notes

- Figure numbers are stable identifiers. In ep01, ep02, ep05, and ep07 the
  new figures sit earlier in the document than some lower-numbered figures
  (for example ep01 fig6 appears before fig4). Renumbering would break the
  E1 exam citations in AUDIT_REPORT.md, which reference figure numbers.
  Numbers were left stable. Captions are self-contained, so reading order
  is unaffected.
- ste_check.py on all 7 chapters: 4 hard fails remain, all the contraction
  front matter (ep01 and ep03, video_title and sources label). These are the
  documented verbatim-title exceptions: the titles on YouTube contain a
  contraction, and the chapters quote them exactly. Zero other hard fails. This pass introduced zero hard fails
  and removed one pre-existing em-dash hard fail at ep01:45.
- Honest gaps unchanged: ranks 1, 2, 8 have no transcripts and no chapters.
