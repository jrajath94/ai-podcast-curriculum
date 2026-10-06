# FIGURE REPORT — Lex Fridman Track
Date: 2026-10-06. Role: figure enforcer. Spec: VISUAL_SYSTEM_GENERIC.md (binding).
Prior state: zero figures (AUDIT_REPORT.md). This retrofit: 19 figures added across 10 chapters. ep10: no figures (no drawable state-changing claims; see audit table).

Medium ladder honored throughout: table first for comparisons, equation for the residual definition, ASCII skipped (no trace claims), mermaid for flows, SVG for one geometry claim (NVL72 rack). No AI image generation. No OpenRouter. The SVG plate is code-generated (`assets/gen_nvl72.py`) and was visually inspected in headless Chromium: before/after panels, center arrow naming the operation, footer claim, source line, flat fills, 8px grid, no banned elements.

Caption format (every figure): "Figure N. Title. AI Podcast Curriculum, epXX (source, date). Shell K. <shell line>. Source: original toy/table/plate/equation."

## Per-page audit tables

### ep01 — 2 figures

| Unit id | Claim | Before | After | Figure id | Medium | Source |
|---|---|---|---|---|---|---|
| u01 | X narrows hundreds of millions of posts to 1,500 candidates to the posts shown | Hundreds of millions of posts | The handful you see | Figure 1 | mermaid | original toy (episode numbers) |
| u02 | A note shows only if raters who disagree both rate it helpful | Note proposed | Shown / hidden | Figure 2 | mermaid | original toy |
| u03 | Token drift: 1% per-token error, ~63 of 100 hundred-token runs contain an error | Clean generation | Error essentially certain by 1,000 tokens | none — prose toy complete (M-08 fix); a plate would restate numbers | — | prose |
| u04 | Constraint chain: silicon, then transformers, then electricity | — (ordered list, no state change) | — | none — STE mnemonic covers it | — | prose |
| u05 | Autopilot: photons in, controls out (end-to-end) | Pixels in | Controls out | none here — pipeline figure lives in ep02 Figure 1; no duplicate drawn | — | ep02 |

### ep02 — 1 figure

| Unit id | Claim | Before | After | Figure id | Medium | Source |
|---|---|---|---|---|---|---|
| u01 | Full flow: 100% of fuel and 100% of oxidizer each pass through a turbine | Fraction of propellant does turbine work | Full flow; 300 bar vs 267 bar | none — one-off unit, no downstream symbol reuse (fails test 4); prose mechanism complete | — | prose |
| u02 | Mars: $1B/ton x 1M tons = $1,000T; target $1M/ton = $1T | Impossible | Merely very hard | none — numbers fully worked in prose + Q2; a plate would restate | — | prose |
| u03 | Eight cameras fuse into one 3D vector space; planning happens there | 8 separate 2D image streams | One 3D vector space, planner acts | Figure 1 | mermaid | original toy (episode numbers) |
| u04 | Money is a database; inflation is editors adding entries | — (metaphor, no state change) | — | none | — | prose |
| u05 | Laws get sunset clauses | — (rule, no state change) | — | none | — | prose |

### ep03 — 2 figures

| Unit id | Claim | Before | After | Figure id | Medium | Source |
|---|---|---|---|---|---|---|
| u01 | RLHF: base model to helpful assistant in 4 steps | Knowledgeable but unhelpful continuer | Helpful assistant | Figure 1 | mermaid | original toy |
| u02 | Nonprofit board controls; investor returns split at the 100x cap | Returns uncapped (implicit) | 100x to investors, excess to mission | Figure 2 | mermaid | original toy (episode numbers) |
| u03 | Scaling laws: loss falls predictably with compute | — (relationship; slope not in episode) | — | none — any plate would invent the slope or restate prose | — | prose |
| u04 | SVB: borrow short, lend long, plus internet speed, equals instant bank run | Stable bank | Collapsed | none — narrative mechanism; one-off, no reuse | — | prose |

### ep04 — 2 figures

| Unit id | Claim | Before | After | Figure id | Medium | Source |
|---|---|---|---|---|---|---|
| u01 | Signal chain: record, detect, transmit, decode; 22 ms end to end | ~200 Mbps raw at the electrode | Cursor moves at 22 ms | Figure 1 | mermaid | original toy (episode numbers) |
| u02 | Calibration: open-loop fit, then closed-loop co-adaptation | Rough decoder, no control | Refined decoder, patient in control | Figure 2 | mermaid | original toy |
| u03 | Firmware switches the decoder to spike band power; function recovers | Threads retracted, signal lost | Coarser signal, performance recovered | none — prose + Q2 complete; decoder symbol covered by Figures 1-2 | — | prose |
| u04 | The decoder is a dataset plus a compile; offline metrics lie | — (definition + warnings) | — | none | — | prose |

### ep05 — 1 figure

| Unit id | Claim | Before | After | Figure id | Medium | Source |
|---|---|---|---|---|---|---|
| u01 | Avatars vary on two axes: realism x identity | One fixed self | Contextual identity points | Figure 1 | table | original table (episode examples) |
| u02 | Moderation: AI flags, humans review edges, board handles precedents | Billions of unreviewed posts | Categorized, appealable decisions | none — one-off pipeline, no downstream reuse | — | prose |
| u03 | Metaverse use cases: Games, Social, Productivity, Fitness; each funds the next | — (ordered list) | — | none — GSPF mnemonic covers it | — | prose |
| u04 | RSC: 6,000 GPUs scaling toward 16,000 | 6,000 | 16,000 | none — number pair in prose; a plate would restate | — | prose |

### ep06 — 3 figures

| Unit id | Claim | Before | After | Figure id | Medium | Source |
|---|---|---|---|---|---|---|
| u01 | Residual: the layer adds its output to its input | y = F(x) (replace) | y = x + F(x) (add) | Figure 1 | equation + toy | original toy (numbers computed) |
| u02 | Software 2.0: the program is the weights | Humans write code (1.0) | Optimization writes weights (2.0) | Figure 2 | table | original table (episode numbers) |
| u03 | Data engine: deploy, mine failures, label, retrain | Current model with failures | Retrained model, one step up | Figure 3 | mermaid | original toy |
| u04 | Neural net: mix, bend, stack, tune | — (definition) | — | none — prose 4-step complete | — | prose |
| u05 | Few-shot: pretraining once, adaptation cheap (zebra) | — (analogy) | — | none | — | prose |

### ep07 — 1 figure

| Unit id | Claim | Before | After | Figure id | Medium | Source |
|---|---|---|---|---|---|---|
| u01 | Codec avatars: scan once, stream parameters not pixels | Millions of pixels per frame (~2 Mbps) | Dozens of parameters per frame (~96 kbps) | Figure 1 | mermaid | original toy (episode numbers) |
| u02 | Predictability bounds: creator sets bounds, reviews failures, tightens | Unbounded persona | Bounded, trusted persona | none — reuses the ep06 data-engine symbol; prose + ep06 Figure 3 cover it | — | prose |
| u03 | Uncanny valley: near-perfect disturbs, imperfect-but-communicative does not | — (qualitative; drawing the curve would invent data) | — | none | — | prose |

### ep08 — 1 figure

| Unit id | Claim | Before | After | Figure id | Medium | Source |
|---|---|---|---|---|---|---|
| u01 | Sora works on spacetime patches, not text tokens | 1D token sequence | Spacetime patch grid | Figure 1 | table | original table (counts computed) |
| u02 | Tasks ladder: automation climbs 5s, 5min, 5h, 5d | — (ordered list) | — | none — SSMHD mnemonic covers it | — | prose |
| u03 | Board saga: legal power without operational power is fiction | Board fires CEO (legal) | Company does not follow (operational) | none — narrative; ep03 Figure 2 is the visual reference | — | prose |
| u04 | Compute becomes the currency of the future | — (thesis) | — | none | — | prose |

### ep09 — 2 figures

| Unit id | Claim | Before | After | Figure id | Medium | Source |
|---|---|---|---|---|---|---|
| u01 | Danger thresholds: weak, middle, strong | Bad advice | Active deception | Figure 1 | table | original table |
| u02 | Outer vs inner alignment, with the evolution case | Conflated | Distinguished | Figure 2 | table | original table |
| u03 | Suggester/verifier: oversight works until the capability gap grows | Verification works | Verification is theater | none — one-off structure, no downstream reuse; lottery/hash examples complete | — | prose |
| u04 | Instrumental convergence: any goal implies survival/resource sub-goals | — (general claim) | — | none — prose + examples complete | — | prose |
| u05 | Paperclip maximizer: optimizing a trivial goal destroys value as a side effect | — (thought experiment) | — | none | — | prose |

### ep10 — 0 figures

| Unit id | Claim | Before | After | Figure id | Medium | Source |
|---|---|---|---|---|---|---|
| u01 | Constraints shrink the search space to the interesting region | Infinite, boring space | Bounded, interesting region | none — philosophical mechanism; the chapter's own constraint toy (Think it yourself #3) is the worked unit; a plate would decorate | — | prose |
| u02 | One failed supply-chain node cascades | Intact chain | Cascade | none — the episode names no concrete chain; a plate would invent structure | — | prose |
| u03 | Design the hell first | — (design rule) | — | none | — | prose |
| u04 | Spotify: 20,000 artists at the CD peak vs ~1M now | 20,000 | ~1,000,000 | none — two numbers in prose; a plate would restate | — | prose |

### ep11 — 4 figures

| Unit id | Claim | Before | After | Figure id | Medium | Source |
|---|---|---|---|---|---|---|
| u01 | Three vectors: flops, memory bandwidth, interconnect. Training is interconnect-bound; inference is memory-bandwidth-bound | One-dimensional chip race | Three vectors; buy the binding one | Figure 1 | table | original table |
| u02 | Export controls cut the interconnect vector (H800); H20 serves on memory bandwidth | H100 full | H800/H20 compliant | Figure 2 | table | original table |
| u03 | 72 GPUs become one logical GPU through the NVLink fabric | 72 separate GPUs | One rack-computer | Figure 3 | SVG (`assets/nvl72-rack.svg`, code-generated) | original plate (chapter numbers, [Added 2026] ModulEdge) |
| u04 | Cluster power ladder: 20 MW, 150 MW, 1.8 GW; 10x per generation | GPT-4 at 20 MW | Stargate at 1.8 GW | Figure 4 | mermaid | original toy (episode numbers) |
| u05 | Jevons paradox: cheaper intelligence means more total GPUs | Expensive, small market | Cheap, bigger market | none — prose + evidence complete; drawing the curve would invent data | — | prose |

## Four-test record (drawn figures only)

| Figure | What it looks like | Why the rule forces that shape | One number the reader can change | Symbol the next page reuses |
|---|---|---|---|---|
| ep01 F1 funnel | A funnel: wide pool, narrow band, few posts | Ranking by dot product lets only top scores pass each gate | 1,500 candidates (or 220 CPU-seconds) | Vector pill: user/post vectors, reused in ep01 drill #3 and ep06 |
| ep01 F2 bridging gate | Two rater groups, one AND-gate, shown/hidden | The rule needs one gate per disagreeing side | Sides that must agree: 2 (1 gives averaging) | Bridging rule, reused in ep05 bridging toy |
| ep02 F1 pipeline | Four stations, images left, steering right | Planning must happen in vector space, not image space | 8 cameras (or 13 ms saved) | 3D-vector-space block, reused in ep02 fleet argument and ep06 |
| ep03 F1 RLHF | Four stations in a line | Optimizing predicted human preference forces the reward-model middleman | The reward score being maximized | Reward-model block, reused in ep09 (RLHF worsened calibration) |
| ep03 F2 capped-profit | Board on top, money splitting at the cap | The 100x cap forces the split shape | 100x | Structure symbol, reused in ep08 board saga |
| ep04 F1 signal chain | Four stations, data shrinking left to right | Heat limits force detect-on-chip before transmit | 7.5 ms Bluetooth interval (or 22 vs 75 ms) | Decoder block, reused in ep04 calibration section |
| ep04 F2 calibration | Two phases with a feedback arrow | Labels must come from known intentions first | Error count per loop iteration | Decoder block (from F1), reused in the dataset-plus-compile section |
| ep05 F1 axes | Two rows: the realism axis, the identity axis | Identity is contextual, so it needs two dimensions | — (table rung; no scalar) | Axes, reused in ep07 identity section |
| ep06 F1 residual | Two equations: replace vs add, plus a worked toy | Gradients must flow unchanged, so the input is added not replaced | F(x) = [0.1, -0.2] | Vector pill x, reused on the next page; add-node enters the symbol table |
| ep06 F2 1.0-vs-2.0 | Four rows comparing the two regimes | The comparison is the claim | — (table rung; no scalar) | Dataset/loss/architecture symbols, reused in the data-engine section |
| ep06 F3 staircase | Four stations closing into a loop | Failures must flow back into training | Loop speed (labelers, retrain time) | DMLR loop, reused in ep07 predictability bounds |
| ep07 F1 codec pipeline | Three stations: heavy once, light live | Bandwidth must collapse, so learning goes up front | Parameter count (100 x 30 x 4 B = 96 kbps) | Expression-parameter vector, reused in ep07 drill #1 |
| ep08 F1 tokens/patches | Four rows: unit, shape, learning target, cost | The structural difference is the claim | — (table rung; no scalar) | Spacetime patch, reused in ep08 drill #3 |
| ep09 F1 thresholds | Three rows: weak, middle, strong | The escalation is the claim | — (table rung; no scalar) | Ladder, reused in ep09 drills #5 and Q8 |
| ep09 F2 inner/outer | Three rows: question, evolution case, failure mode | The distinction is the claim | — (table rung; no scalar) | Outer/inner symbols, reused in ep09 Q4 and Q8 |
| ep11 F1 three vectors | Five columns: vector, measures, training, inference, proof | The binding vector differs by workload | — (table rung; no scalar) | FMI vectors, reused in ep11 drill #3 and Q3 |
| ep11 F2 chip table | Two rows: H800, H20 against the H100 | Export controls cut one vector per chip | — (table rung; no scalar) | FMI vectors (from F1), reused in ep11 Q5 |
| ep11 F3 NVL72 plate | Before: 72 pills. After: rack with switches, GPUs, CPUs, cooling. Footer: the rack is the computer | Non-blocking TB/s interconnect forces the single-fabric shape | 72 GPUs | Rack-computer symbol, reused in ep11 drill #1 |
| ep11 F4 power ladder | Three rungs ascending | 10x model scale per generation forces the spacing | The 10x multiplier | MW rungs, reused in ep11 drill #5 |

## Track symbol table (F7)

| Symbol | Meaning | First use | Reuse |
|---|---|---|---|
| Vector pill | Embedding of a user, post, or token as a list of numbers | ep01 F1 | ep01 drill #3, ep02 F1, ep06 F1 |
| 1,500-candidate pool | Ranked shortlist between retrieval and display | ep01 F1 | — (terminal) |
| Disagreeing rater pair | Two raters from historically opposite sides | ep01 F2 | ep05 bridging toy |
| Bridging AND-gate | Note shows only if both sides rate helpful | ep01 F2 | ep05 |
| Reward model | Predicts which response a human would prefer | ep03 F1 | ep09 (calibration discussion) |
| 100x cap split | Investor returns split at 100x; excess funds the mission | ep03 F2 | ep08 board saga |
| Spike | Detected action potential | ep04 F1 | ep04 F2 |
| Decoder block | Spike patterns to cursor mapping | ep04 F1 | ep04 F2, dataset-plus-compile section |
| Avatar axes | Realism x identity, two dimensions | ep05 F1 | ep07 identity section |
| DMLR loop | Deploy, mine failures, label, retrain | ep06 F3 | ep07 predictability bounds |
| Residual add | y = x + F(x); the layer adds, not replaces | ep06 F1 | track table |
| Weights-blob | The program in Software 2.0 | ep06 F2 | ep06 drills |
| Expression-parameter vector | Codec avatar stream unit (dozens of numbers per frame) | ep07 F1 | ep07 drill #1 |
| Spacetime patch | Sora's unit of video | ep08 F1 | ep08 drill #3 |
| W/M/S ladder | Weak, middle, strong danger thresholds | ep09 F1 | ep09 drills, Q8 |
| Outer / inner | Objective right? vs model pursues it? | ep09 F2 | ep09 Q4, Q8 |
| FMI vectors | Flops, memory bandwidth, interconnect | ep11 F1 | ep11 drills, Q3, Q5 |
| Rack-computer | NVL72 as one logical GPU | ep11 F3 | ep11 drill #1 |
| MW rung | Cluster power level (20 MW, 150 MW, 1.8 GW) | ep11 F4 | ep11 drill #5 |

## F1–F7 verdict

- **F1 (page audit; every state-changing claim has a figure; no blank cells): PASS.** All 40 units mapped above. Units without figures carry a recorded reason: prose-complete, not a state change, or fails the four tests (test 4, no downstream reuse). No blank cells in any table.
- **F2 (medium ladder honored): PASS.** 8 tables (comparison claims), 1 equation (residual definition), 10 mermaid (flows), 1 SVG (rack geometry). Each figure uses the first rung that passes. No AI images, no OpenRouter.
- **F3/F4 (lesson plates carry one claim; chapter plates where warranted): PASS.** Every figure carries exactly one claim. The NVL72 plate is the single dense plate: before/after plus one footer claim.
- **F5 (captions name the project and the source): PASS.** Every caption names "AI Podcast Curriculum", the episode and date, the shell, and the source (original toy/table/plate/equation).
- **F6 (reject list; every number computed or transcript-sourced): PASS.** No gradient, glow, shadow, logo, watermark, robot, brain, or clip art. SVG plate visually inspected. Numbers: episode numbers throughout; computed: 72-86 kW (72 x 1,000-1,200 W), 61,440 patches, y = [2.1, 2.8], 96 kbps. No invented numbers.
- **F7 (symbols consistent track-wide): PASS.** Symbol table above; no symbol changes meaning between chapters.

## Verification

- `ste_check.py` on all edited chapters: zero hard failures in added figure lines (pre-existing prose hits untouched, outside this task's scope).
- `build.py` smoke test on the 13 content pages: builds clean (13 pages). 10 mermaid blocks convert; the SVG image becomes `<figure>` + `<figcaption>`; the asset copies to output.
- SVG plate: 197 rects, all on the 8px grid, none out of bounds; screenshot-reviewed.

## Follow-ups for the parent (content bugs found, NOT fixed — outside figure mandate)

The fix agent's leftovers sweep missed three cheatsheet lines that contradict the fixed chapters:
1. `cheatsheet.md` ep01: "Batteries: materials a fraction of $600/kWh." — F-01 removed the battery anecdote from ep01.md; the cheatsheet still carries it.
2. `cheatsheet.md` ep01: "Simulation: ancestor simulations outnumber reality. Act to make it interesting." — F-02 rewrote the section to determinism/free-will; the cheatsheet still carries the old framing.
3. `cheatsheet.md` ep03: "RLHF in 4 steps: Demonstrate, Compare (pairwise, tens of thousands), Reward model, Reinforce." — F-04 removed the unattributed "tens of thousands" from ep03.md; the cheatsheet still carries it.
