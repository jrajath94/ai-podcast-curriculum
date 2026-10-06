# AUDIT REPORT — Lex Fridman Track
# Track auditor verdict. Date: 2026-10-06. Auditor does not fix.

Scope: all 11 chapters (ep01–ep10, ep11-synthesis), index.md, cheatsheet.md,
_coverage.md, against TRACK_AUDITOR_BRIEF.md gates G1–G9 + G1b + G7b, plus
figure status per the parent's 2026-10-06 scoping note (figures deferred to
the retrofit step; this audit judges content gates only, and records that
zero figures exist in the track — none decorative, none to kill).

Method: every chapter read in full. G1 spot-checks ran 8+ transcript items
each against ep01 (JN3KPFbWCy8.txt), ep03 (L_Guz73e6fw.txt), ep06
(cdiD-9MMpb0.txt); quote-level checks against ep04, ep05, ep07, ep08, ep09,
ep10, ep11 (#459: _1f-o0nqpEI.txt). G8 checked mechanically (grep).
G7b checked by sentence-level duplicate scan. E1: 20 questions written and
answered from chapter text only (appendix).

## Verdict per chapter

| Chapter | Verdict | Failing gates |
|---|---|---|
| ep01 (Musk #400) | FAIL | G1 (2 imported sections), G3 (6 terms) |
| ep02 (Musk #252) | PASS | — (1 minor G3 note) |
| ep03 (Altman #367) | FAIL | G1/G5 (2 items), G3 (2 terms) |
| ep04 (Neuralink #438) | FAIL (narrow) | G9 (1 invented quote) |
| ep05 (Zuckerberg #267) | PASS | — |
| ep06 (Karpathy #333) | PASS | — (1 minor G2 note) |
| ep07 (Zuckerberg #398) | FAIL (narrow) | G1/G5 (1 number) |
| ep08 (Altman #419) | PASS | — |
| ep09 (Yudkowsky #368) | PASS | — (1 minor G9 wording note) |
| ep10 (Grimes #281) | FAIL (narrow) | G7b (2 internal repeats) |
| ep11 (Synthesis) | PASS | — (2 minor G5/G3 notes) |
| index.md | PASS | — (1 minor accuracy note) |
| cheatsheet.md | PASS | — (1 minor G5 note) |
| _coverage.md | ADVISORY | map is accurate to the chapters, but the chapters contain non-episode material (see F-01..F-04) |

## Numbered findings

### F-01 [G1, ep01, §Physics from first principles] — Battery anecdote is not in the episode
The chapter states: "The concrete example he gives is batteries. People said
battery packs would always cost 600 dollars per kilowatt-hour. He broke a
battery into its raw materials (lithium, nickel, cobalt, aluminum), priced
the materials on the commodities market…"
The ep01 transcript contains zero mentions of "battery", "kilowatt",
"lithium", or "commodit". This is Musk's famous anecdote from other
interviews, imported and presented as "the concrete example he gives" in
this episode.
Fix: replace with an example actually given in #400, or reframe explicitly
as background context labeled [Added], never as episode content.

### F-02 [G1, ep01, §The simulation argument] — Ancestor-simulation argument is not in the episode
The chapter presents the ancestor-simulation argument ("If any civilization
reaches the point where it can run ancestor simulations… Therefore we are
probably simulated") plus the decision rule "make the simulation interesting:
be useful, create, expand consciousness."
The ep01 transcript's simulation discussion is about determinism versus free
will ("if we are in a simulation the reason… would be to see what happens";
SpaceX/Tesla run simulations the same way). The ancestor-simulation
argument and the "make it interesting" rule do not appear. (The transcript's
"giant computer simulation" line is Grok's fun-mode joke about soma, not
Elon's argument.)
Fix: rewrite the section to the episode's actual simulation discussion
(determinism/free will, simulations-as-experiments), or label the
ancestor-simulation content [Added] and separate it from episode claims.

### F-03 [G1/G5, ep03, §GPT-4 as an early, flawed, proto-AGI system] — "Shitty book" test misrepresents the transcript
The chapter states: "he says GPT-4 is not AGI by a test like 'write a shitty
book': a long, coherent, genuinely new piece of work sustained over hundreds
of pages."
The transcript: "if I were reading a Sci-Fi book and there was a character
that was an AGI and that character was gpt4 I'll be like well this is a
shitty book… that's not very cool." Altman means GPT-4 would be an
underwhelming fictional AGI character — "it doesn't feel that close to me."
There is no "write a shitty book" sustained-coherence test in the episode.
The chapter invented the test and its definition. The cheatsheet repeats it
("'shitty book' test (sustained coherence) as the bar it fails").
Fix: rewrite to Altman's actual point (GPT-4 does not feel close to AGI;
the sci-fi-character remark as his informal bar), and correct the cheatsheet
line.

### F-04 [G1/G5, ep03, §The ChatGPT moment] — "Tens of thousands of comparisons" not in the episode
The chapter states: "in the episode Altman says remarkably little data is
needed: tens of thousands of comparisons, not billions."
Exhaustive search of the ep03 transcript finds no quantity attached to RLHF
preference data (the only "tens of thousands" nearby refers to numbers of
people in the world, a different sentence). The number is unattributed.
Fix: remove the specific number, or attribute it to its real source with a
citation — never as Altman's claim in this episode.

### F-05 [G9, ep04, §The decoder is a dataset plus a compile] — Invented quote
The chapter states: 'In the episode, a team member says the decoder is "a
dataset plus a compile."'
The transcript contains "how do you compile it the best model" and dataset/
label discussion, but the pithy formulation "a dataset plus a compile" never
appears. Quotation marks present it as a verbatim saying.
Fix: remove the quotation marks and render as paraphrase ("the team's
framing amounts to: the decoder is a dataset plus a compile step"), or drop
the formulation.

### F-06 [G1/G5, ep07, §AI versions of the living] — "28 launch AIs" not in the episode
The chapter states: "In the episode, he mentions 28 launch AIs with celebrity
personas."
The ep07 transcript contains zero occurrences of "28". It says "we're
starting out with a set" (no number). Snoop Dogg / Jane Austen /
Marcus Aurelius personas are verified in the transcript; the count 28 is
imported from outside reporting and misattributed to the episode.
Fix: drop "28" or reframe as background ("Meta's launch set, reported as 28
outside the episode") without "In the episode" attribution.

### F-07 [G3, ep01/ep03] — Seven technical terms used before defined
Zero-knowledge law: define every term at or before first use. Violations:
1. "token" — first body use ep01 ("predict the next token"); first gloss is
   ep08 ("tokens (text pieces)"), 7 chapters later. ep03 and ep06 also use it
   undefined.
2. "GPU" / "H100" — ep01 uses "8,000 Nvidia H100 GPUs" with no definition of
   either; ep11 never defines them for a zero-knowledge reader.
3. "FLOPS" — ep01 ("Not raw FLOPS") undefined at first use; only glossed in
   ep01's memory aids, not at first use.
4. "autoregressive" — ep01 ("the architecture itself is autoregressive"),
   never defined.
5. "vector" — ep01 X-algorithm section ("represent the user as a vector")
   undefined; ep06 defines it ("a list of numbers") 5 chapters later.
6. "parameter" — ep01 ("parameter count") and ep03 ("parameters to the
   gigahertz race") undefined; first defined in ep06 ("knobs (parameters)").
7. "HBM" — ep11 ("13.5 terabytes of HBM3e"), never expanded or defined.
8. "CUDA" — ep11 describes it functionally but never expands the acronym or
   states plainly that it is Nvidia's GPU programming platform.
Fix: add one-sentence first-use definitions in ep01 (token, GPU, H100,
FLOPS, autoregressive, vector, parameter), ep11 (HBM, CUDA).

### F-08 [G7b, ep10] — Two sentences repeated verbatim inside the chapter
1. "If you cannot prevent the hell version, you do not understand the
   technology." — appears in §Artificial hells (L91) and again in Q6 (L127).
2. "The population is too big for a low-tech fallback." — appears in
   §Supply chains (L99) and again in Q7 (L130).
Fix: keep the teaching in the section; compress the Q&A restatement to a
cross-reference.

### Minor findings
- M-01 [G9, ep09]: "His line: you cannot fetch the coffee if you are dead."
  The transcript has "you can't bring the coffee if you're dead." Reword to
  match the transcript.
- M-02 [G5, ep11]: "$5.6 million" — the episode says "shocking 5 million
  dollar number." Either use the episode's figure or label $5.6M as the
  widely-reported precise figure, not the episode's.
- M-03 [G5, cheatsheet]: "Megapacks" (ep11 line 171) appears in neither the
  ep11 chapter nor the #459 transcript. Remove or source it.
- M-04 [G9, index.md]: the intelligence-arc claims "Episodes 9-11 (unaided):
  drills state the question and stop," but the ep09 and ep11 Fermi drills
  still carry scaffolding and embedded answers (ep11 Q3 even gives
  "Answer: B, probably"). Soften the claim to match the drills.
- M-05 [G2, ep06]: §"The AGI path: pixels, Optimus, and the concerning part"
  carries three increments (text-insufficiency, Optimus hedge, digital-only
  concern). Split into two subchapters per the one-increment rule.
- M-06 [G3, ep02]: "parameter" also used undefined here (covered by F-07 fix
  in ep01, which precedes it).
- M-07 [G7b, advisory]: the "A note on honesty" boilerplate + "Reading this
  chapter equals watching the whole episode" repeats across all 10 chapters.
  Not teaching, so not a fail — but consider stating it once in index.md and
  trimming per-chapter to one line.
- M-08 [G4, advisory]: two mechanisms lack worked numbers — ep01 token drift
  ("random walk with a pull" has no toy) and ep02 full-flow staged combustion
  (explained, not worked). Everything else has Fermi/toy coverage.
- M-09 [Media]: x.ai (ep01 go-deeper) returns 403 to curl — bot-blocking, not
  a dead link; canonical URL, retain.

## What verified clean (spot-check record)
- ep01: 8,000 H100s (caption "A1 100s"), 220 CPU-seconds, 1,500 candidates,
  Taiwan "100% likely", "speciesist" (caption garbles as "speciest"),
  $40M+, compute doubling, vector correlation, soma, cynicism red flag.
- ep02: Raptor 300 bar vs RD-180 267 bar, $1B/ton → $1M/ton Mars math,
  rocket raw-materials example (legitimately in this episode).
- ep03: alignment admission verbatim ("I do not think we have yet discovered
  a way to align a super powerful system"), jailbreak/Spotify analogy.
- ep04: BOSS chip name, 1,024 channels, 20 kHz/10-bit/200 Mbps, Bluetooth
  7.5 ms, 22 ms vs 75 ms, thread retraction + firmware fix, 8.5 BPS,
  4.2–4.6 record range, goal of 10, Bliss 17 BPS, Civ 6 Korea, 400
  electrodes (patient 2).
- ep05: 20 harm categories ("about 20 different kinds of harm"), RSC
  6,000 → 16,000 GPUs, Agent Smith joke.
- ep06: Transformer 2016 transcript error correctly flagged and corrected to
  2017; "complicated alien artifact"; annotation 0 → 1,000; residual
  connections; bitter lesson; World of Bits 2015; radio 1/10 light-year;
  nuclear "my number one concern for society" verbatim.
- ep07: codec avatars, Quest 3 $500, Snoop Dogg dungeon master, Jane Austen /
  Marcus Aurelius, AI Studio.
- ep08: "unbecoming of a builder", "missed the old Elon", "boring Tuesday at
  9:46 in the morning" — all verbatim.
- ep09: "summoning the demon" verbatim; "We never become right. We just
  become less wrong." verbatim; coffee line present (wording differs, M-01).
- ep10: Oscar Wilde close, blastocyst, Ek 20,000 vs ~1M artists (with
  Grimes's own "propaganda" caveat preserved).
- ep11: powerPlantNoBlowup, 1200x, 37B active, MLA 80–90%, GPT-4 20,000
  A100s, Memphis 200,000 GPUs, Singapore 20–30% revenue, Stargate Abilene
  2.2 GW in / 1.8 GW to chips. [Added 2026] sources return HTTP 200.
- Frontmatter: all video_ids, dates, view counts match episodes.json.
- G6: 8 Q&As per chapter, each with follow-ups, Q1 explain-like-new,
  Q8 applied — all 11 chapters.
- G1b: "How to imbibe this" and "Think it yourself" present and concrete in
  all 11 chapters, with observable-behavior-change lines.
- G7: 20-paragraph sample — every paragraph carries a number, mechanism
  step, failure mode, or decision rule.
- G8: zero contractions, zero em dashes, zero semicolons in prose, zero
  banned-filler hits (mechanical grep over all files).
- E1: 20/20 (appendix).

## Figure status (per parent scoping — retrofit is a separate step)
Zero figures exist in the track: no image embeds, no mermaid, assets/ empty.
F5 caption compliance against the old format is vacuous (no captions exist);
no decorative or prose-repeating figures exist to kill. Candidate units the
retrofit should cover: ep01 X-algorithm funnel + Community Notes bridging;
ep03 RLHF 4-step loop; ep04 N1 signal chain + calibration loop; ep06 data-
engine staircase + residual connection; ep07 codec-avatar pipeline; ep11
three-vector model + NVL72 rack layout + power ladder.

## Consolidated fix list by severity
CRITICAL (fix before ship — fidelity/honesty):
1. ep01: remove or [Added]-label the battery $600/kWh anecdote (F-01).
2. ep01: rewrite the simulation-argument section to the episode's actual
   determinism/free-will discussion (F-02).
3. ep03: rewrite the "shitty book" test to Altman's actual remark; fix
   cheatsheet line (F-03).
4. ep03: remove unattributed "tens of thousands of comparisons" (F-04).
5. ep04: unquote "a dataset plus a compile" (F-05).
6. ep07: fix "28 launch AIs" attribution (F-06).
MAJOR (fix before ship — zero knowledge):
7. Add first-use definitions: token, GPU, H100, FLOPS, autoregressive,
   vector, parameter (ep01); HBM, CUDA (ep11) (F-07).
MINOR (fix in the same pass):
8. ep10: de-duplicate the two repeated sentences (F-08).
9. M-01 through M-06 as listed above.
ADVISORY: M-07, M-08, M-09.

## Appendix E1 — 20 understanding-check questions, answered from chapter text only
1. Q: What two failure modes does Elon name for war and peace, and what is
   the middle path? A: Conspicuous kindness (signals weakness, invites
   attack) and provocation (corners the adversary, triggers attack). Stay
   between: do not look like prey, do not poke the bear. (ep01)
2. Q: What does STE stand for in the constraint chain? A: Silicon, voltage
   Transformers, Electricity — in that scarcity order. (ep01)
3. Q: What Raptor chamber pressure does Elon target, and what was the prior
   record? A: ~300 bar; the Russian RD-180 at ~267 bar. (ep02)
4. Q: Walk the Mars-city arithmetic. A: ~$1B/ton today × ~1M tons =
   ~$1,000T (impossible); at ~$1M/ton the city costs ~$1T (merely very
   hard). (ep02)
5. Q: Name the four RLHF steps. A: Demonstrate, Compare (pairwise),
   Reward model, Reinforce. (ep03)
6. Q: What is Altman's honest admission on alignment? A: "I do not think we
   have yet discovered a way to align a super powerful system." (ep03)
7. Q: Name the four N1 signal-chain stations and end-to-end latency.
   A: Record (20 kHz, 10-bit, ~200 Mbps) → Detect spikes on chip → Transmit
   via Bluetooth (7.5 ms interval) → Decode. ~22 ms brain-to-cursor vs
   ~75 ms brain-to-hand. (ep04)
8. Q: Why did the threads retract, and what fixed it? A: The brain moves
   with heartbeat/breath while the skull does not; ~4 weeks post-surgery
   threads pulled out. An over-the-air firmware update switched decoding to
   spike band power. (ep04)
9. Q: What does "the metaverse is a time, not a place" mean, and what is the
   use-case order? A: The era when immersive presence becomes normal.
   Order: Games, Social, Productivity, Fitness — each funds the next. (ep05)
10. Q: What is the RSC's GPU trajectory in the episode? A: 6,000 Nvidia
    A100 GPUs, scaling toward 16,000 GPUs. (ep05)
11. Q: What is Software 2.0, and what is the program? A: Humans specify
    dataset, loss function, architecture; optimization finds the weights.
    The program is the weights. (ep06)
12. Q: Name the four data-engine steps. A: Deploy, Mine failures, Label,
    Retrain. (ep06)
13. Q: Why does a codec-avatar call use less bandwidth than video? A: It
    streams expression parameters (dozens of numbers per frame, ~96 kbps),
    not pixels (~2 Mbps for 1080p30 video). (ep07)
14. Q: What is the predictability-bounds problem for creator AIs? A: The AI
    must be capable enough to be useful without saying things the creator
    would never say; the creator sets bounds and tightens them from failure
    review. (ep07)
15. Q: What is the board saga's governance lesson? A: Legal power without
    operational power is fiction — the board could fire on paper but not run
    the company without the talent and compute. (ep08)
16. Q: What is the 5-second to 5-day ladder? A: AI automates tasks smallest
    first (5-sec, 5-min, 5-hour, 5-day); jobs unbundle gradually. Watch
    percent of tasks automated, not jobs destroyed. (ep08)
17. Q: What is the "first critical try" thesis? A: Alignment must be solved
    on the first system capable of deceiving operators and escaping control;
    a misaligned superintelligence gives no second try. (ep09)
18. Q: Distinguish outer from inner alignment using the evolution example.
    A: Outer: is the training objective right? Inner: does the trained model
    pursue it? Evolution optimized inclusive fitness (Haldane: two brothers
    or eight cousins); humans pursue proxies (pleasure, status). (ep09)
19. Q: What is Grimes's "design the hell first" rule? A: For every utopian
    technology, design the abuse case before the use case — if you cannot
    prevent the hell version, you do not understand the technology. (ep10)
20. Q: Which vector binds training vs inference, and what proves it? A:
    Training is interconnect-bound (export controls cut the H800's
    interconnect; DeepSeek innovated around it); inference is memory-
    bandwidth-bound (the H20 beats the H800 at serving; MLA cut the KV
    cache 80–90%). (ep11)
Result: 20/20 answered from chapter text. E1 PASS.
