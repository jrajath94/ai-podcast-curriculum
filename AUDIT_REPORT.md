# TRACK AUDIT REPORT — Acquired (Ben Gilbert & David Rosenthal)
Auditor: track-auditor subagent. Date: 2026-10-06.
Scope: ep01.md–ep10.md, ep11-synthesis.md, index.md, cheatsheet.md vs transcripts in
`research/acquired/transcripts/` and `research/acquired/episodes.json`.
Method: full read of all 11 chapters; transcript cross-check of every major claim and
number in 3 deep spot-checks (ep01 Jensen, ep04 Google III, ep07 Meta) plus batch
keyword/number verification across all 10 episode transcripts; hand-recomputation of
every worked number; live re-verification of both [S] synthesis sources (NVIDIA H100
product page, DGX H100 user guide — all specs confirmed); style grep sweep for
contractions, em/en dashes, semicolons, banned filler.

## Verdict summary

| Chapter | Verdict | Findings |
|---|---|---|
| ep01 · Jensen Huang | FAIL | G2 (1), G8 (1 semicolon), G5 (captions) |
| ep02 · TSMC / Morris Chang | FAIL | G5 (captions) |
| ep03 · Zuckerberg | FAIL | G1 (2), G8 (11 semicolons), G5 (captions) |
| ep04 · Google III | FAIL | G1 (1), G2 (1), G8 (4 semicolons), G5 (captions) |
| ep05 · Google I | FAIL | G3 (1), G8 (7 semicolons), G5 (captions) |
| ep06 · Microsoft I | FAIL | G8 (17 semicolons + 1 banned word), G5 (captions) |
| ep07 · Meta | FAIL | G1 (1), G8 (19 semicolons), G5 (captions) |
| ep08 · Nvidia II | FAIL | G8 (10 semicolons), G5 (no formal captions) |
| ep09 · Nvidia I | FAIL | G8 (10 semicolons + 4 banned words), G5 (no formal captions) |
| ep10 · Nvidia III | FAIL | G9 (1 misquote), G8 (19 semicolons + 4 banned words), G5 (no formal captions) |
| ep11 · Hardware synthesis | FAIL | G3 (5 undefined terms), G8 (11 semicolons), G5 (no formal captions) |

Finding counts by category: G1: 4 · G2: 2 · G3: 2 (6 terms) · G4: 0 · G5: 1 systemic ·
G6: 0 · G7: 0 · G8: 2 systemic (109 prose semicolons; 9 banned-word hits) ·
G9: 1 · P1: 0 · P2: 0 · P3: 0. Total: 12 findings.

What passed clean: G4 (every hand-worked number recomputed — all correct; the ep06
IBM-deal arithmetic mismatch is properly flagged [uncertain]); G6 (7–8 Q&A per
chapter, every one with a full follow-up answer, beginner-explainers and applied
questions present in all 11); G7 (density holds — every sampled paragraph carries a
number, mechanism step, failure mode, or decision rule); all [S] synthesis specs
verified live against NVIDIA's pages; P1/P2/P3 (imbibe sections concrete, drills
brain-first with a real easy→unaided arc across the track).

---

## HIGH severity

### H1. [G1] ep04 — Waymo economics line misquotes the transcript's comparison
Location: ep04.md, "Waymo: the 100-million-mile grind" closing paragraph.
Chapter says: "The episode notes dryly that the 10 to 15 billion dollars Waymo cost
is about what Google earns in a month."
Transcript (`lCEB7xHer5U.txt`) says: "they have burned somewhere in the neighborhood
of 10 to 15 billion. that's sort of why i was listing all the investments to get to
this point. >> jump change compared to foundational models. >> dude, also let's just
keep it scoped in this sector. that's one year of uber's profits."
The transcript's comparison is to ONE YEAR OF UBER'S PROFITS, not Google's monthly
earnings. The chapter replaced the actual comparison with a different one.
Fix: replace the sentence with the transcript's claim — the $10–15B burn is "one
year of Uber's profits" per the hosts — or cut the comparison.

### H2. [G1/G9] ep03 — the 9th "death wave" is builder invention
Location: ep03.md, "Figure 2. The nine waves" table, row 9: "(Reality Labs losses)".
Transcript (`QciJ9ubeLQk.txt`) names eight waves: "Myspace Twitter gen one yep um
Instagram Snapchat WhatsApp Tik Tock Apple app track transparency put in its own
whole category um and now chat GPT that's nine". Eight distinct waves are named;
Ben says "that's nine" (he appears to double-count ATT as its own category, or
miscounts). The transcript never names Reality Labs as the ninth wave.
Fix: do not present "(Reality Labs losses)" as episode content. Either list the
eight named waves and note Ben's count, or mark row 9 explicitly as
[builder inference].

### H3. [G1] ep03 — "Jamie Dimon opened the show" is not in the transcript
Location: ep03.md, "The story" intro: "Jamie Dimon opened the show."
`QciJ9ubeLQk.txt` contains zero mentions of Dimon. The transcript's opening lists
surprise appearances as "Jensen hang Daniel e Emily Chang" and "Mike Taylor" —
no Dimon. (He may have appeared in the unreleased full-show video, but the
fidelity standard is the transcript.)
Fix: delete the claim, or move it out of episode-derived content with a real source.

### H4. [G1] ep07 — the "constellation of apps" strategy is missing
Location: ep07.md, "The mobile crisis" section.
Transcript (`CS2Lqdwja8o.txt`): "you can see why Facebook adopted that uh sort of
early 2010's constellation of apps strategy for a while they had slingshot poke
messenger p paper rooms riff camera the belief by a lot of companies for the
direction mobile was going was there's going to be specialized apps each for
their own tiny little purpose and that's not great if a lot of your value is we
bundle a lot of stuff in to create the most user engagement..."
This is a substantive strategic point — Facebook's own response to unbundling, and
the bundling-vs-unbundling tension at the heart of its mobile strategy. The chapter
lists the five reasons mobile was dangerous but never mentions Facebook's
constellation response.
Fix: add a subsection covering the constellation strategy: the single-purpose-app
belief, the app list, and why it conflicted with Facebook's bundling value.

### H5. [G9] ep10 — Jensen quote misquoted ("bell" vs "heard")
Location: ep10.md, "The bleakest moment, then the detonation": "Jensen's phrase for
November 30, 2022: the moment the AI bell rang around the world."
Transcript (`nFB-AILkamw.txt`): "this all leads to November 30th 2022 in Jensen's
words the AI heard around the world open AI comes out with chat DPT..."
("the AI heard around the world" — a play on "the shot heard around the world".)
Fix: correct to "the AI heard around the world".

---

## MEDIUM severity

### M1. [G2] ep01 — the CUDA subchapter carries four ideas, not one
Location: ep01.md, "### CUDA: the ten-thousand-person-year platform".
It introduces: (1) CUDA as a platform and the 10,000-person-year bet; (2) the
first-principles justification after AlexNet (universal function approximator,
prediction beats causality); (3) the researcher-adoption story (democratized
supercomputing, LeCun/Ng/Hinton/Sutskever outreach); (4) emergence (GAN cat,
BERT, emergent abilities).
Fix: split into separate ### subchapters — the bet, the first-principles case,
the adoption, the emergence evidence — one increment each.

### M2. [G2] ep04 — the transformer subchapter carries five ideas, not one
Location: ep04.md, "### The transformer: attention is all you need".
It introduces: (1) the Translate/RNN→LSTM history; (2) the attention idea itself;
(3) Noam's rewrite; (4) scaling plus BERT; (5) the publish decision, citation count,
and author exodus.
Fix: split — the parallelization wall, the attention idea, the rewrite and
scaling, the publication and its cost — one increment each.

### M3. [G3] ep05 — "Dutch auction" used without definition
Location: ep05.md:124: "The 2004 IPO used a Dutch auction." No definition follows;
the Q&A (line 168) also uses the term unexplained. A zero-knowledge reader has no
way to know what a Dutch auction is.
Fix: add a one-sentence definition at first use (bidders submit price/quantity
bids; the clearing price is the highest price that sells all shares).

### M4. [G3] ep11 — five hardware terms used without definition
Location: ep11-synthesis.md. First uses with no definition: "TDP" (line 56, "700W
TDP"), "SXM" (line 56, "on the SXM variant"), "NDR" (line 82, "400 Gb/s InfiniBand
(NDR)"), "PSU" (line 83, "6x 3.3 kW PSUs"), "8U" (line 84, "8U rackmount").
Fix: define each at first use — TDP (thermal design power, max heat the cooling
must remove), SXM (NVIDIA's soldered server GPU board form factor, vs PCIe cards),
NDR (InfiniBand speed grade, 400 Gb/s), PSU (power supply unit), U (rack unit,
1.75 inches).

### M5. [G5] Track-wide — figure captions do not name the project
VISUAL_SYSTEM.md: "Name the project in the caption." TRACK_AUDITOR_BRIEF F5:
captions name the PROJECT ("AI Podcast Curriculum") + source.
All 30 "Figure N." captions in ep01–ep07 read "Source: episode." — naming neither
the project nor the episode (e.g. ep01.md:53 "Figure 1. The RIVA 128 decision.
Source: episode."). ep08–ep11 use inline figures with no captions at all.
Fix: rewrite every caption to name the project and the specific source, e.g.
"Figure 1. The RIVA 128 decision. AI Podcast Curriculum, ep01 (Jensen Huang
interview, 2023-10-16); toy built from episode claims."

---

## LOW severity (systemic, mechanical fixes)

### L1. [G8] ~109 semicolons in prose across 10 chapters
Per the brief every semicolon in prose is a FAIL item. Counts (code blocks, ASCII
art, and markdown tables excluded): ep01: 1 (line 270), ep02: 0, ep03: 11 (lines
25, 47, 89, 93, 110, 134, 140, 191, 220, 230, 244), ep04: 4 (62, 72, 171, 199),
ep05: 7 (33, 56, 76, 116, 164, 168, 178), ep06: 17 (49, 72, 84, 121, 129, 131, 133,
165, 173, 179, 187, 192, 202, 212, 223, 227, 246, 248), ep07: 19 (25, 35, 37, 39,
54, 62, 66, 72, 80, 133, 143, 151, 167, 183, 185, 202, 207, 221, 251, 261),
ep08: 10 (78, 95, 99, 105, 136, 141, 156, 163, 166, 175, 181), ep09: 10 (47, 67, 78,
92, 107, 117, 127, 132, 147, 169), ep10: 19 (46, 48, 50, 56, 57, 67, 86, 88, 92,
108, 110, 112, 114, 132, 136, 141, 152, 157, 167, 172, 177, 195, 203), ep11: 11
(42, 48, 56, 72, 120, 135, 140, 150, 155, 160, 165, 184).
Fix: split each into two sentences or restructure with a colon. (index.md has 17
em-dashes and cheatsheet.md 2 — outside chapter scope, but clean them in the same
pass.)

### L2. [G8] 9 banned-filler hits
- ep06:72 "The technical unlock:" → "unlock"
- ep09:122, 152, 163, 178 "holds all the leverage" / "high leverage" / "holds the
  leverage" / "renewal leverage" → "leverage" (4 hits; legitimate business sense,
  but the brief bans the word — replace with "bargaining power", "negotiating
  advantage")
- ep10:48 "Two unlocks changed everything" / "the Transformer unlocked something
  new" → "unlock" (2 hits)
- ep10:114 "cutting-edge CoWoS packaging" → "cutting-edge"
- ep10:153 "the most leverage to unbundle" → "leverage"
Fix: replace each with plain wording.

---

## Explicitly checked and passed (no findings)

- G4 numbers: every hand-worked number recomputed — ep01 drill (108,000 frames/hr,
  ~100,000x slower ✓), ep02 drill (1M wafers ✓), ep05 drill (~0.9%/day ✓),
  ep07 drill (46 views/user/day ✓), ep08 drill (~87% CAGR ✓), ep09 drill (64x ✓),
  ep10 drills (36% margin ✓, ~3.2-month payback ✓), ep11 drills (3.1 TFLOPS/W ✓,
  $9M ✓). Episode numbers (valuations, chip prices, dates) verified against
  transcripts in all 10 episodes. The ep06 IBM-deal component mismatch is correctly
  flagged [uncertain], not papered over.
- G6 Q&A: 8/7/7/7/7/7/7/8/8/8/7 per chapter — all within 6–8, every question has a
  full follow-up answer, beginner-explainers and applied questions present in all 11.
- G7 density: sampled 26 long digit-free paragraphs; all carry a mechanism step,
  definition, failure mode, or decision rule. No zero-information paragraphs found.
- G9 honesty otherwise: quotes verified verbatim ("if you lose my money I'll kill
  you", "my will to survive exceeds almost everybody else's will to kill me",
  "the AI heard around the world" excepted per H5); [E]/[S] tagging in ep11 is
  complete and consistent; both [S] sources re-verified live 2026-10-06
  (H100: 3,958 TFLOPS FP8 w/ sparsity, 67 TFLOPS FP32, 80GB/3.35TB/s, 700W,
  NVLink 900GB/s; DGX H100: 8x H100/640GB, 2x Xeon 8480C/112 cores, 4x NVSwitch,
  2TB DDR5, 8x ConnectX-7 400Gb/s, 6x 3.3kW PSUs 4+2, 10.2kW, 8U, 287.6 lbs,
  5–30 °C — all match the chapter).
- P1/P2/P3: "How to imbibe this" present in all 11 chapters with concrete
  this-week actions, self-catching practices, per-idea behavior changes, and
  monthly reviews — genuine, not filler. "Think it yourself" drills are brain-first
  throughout with a real progression: guided computations with shown answers
  (ep01–ep03) → Fermi/journaling/argue-both-sides (ep04–ep07) → unaided reasoning
  and capstones (ep08–ep11). The intelligence-thread arc described in index.md
  holds.

## Notes for the fix loop (not chapter FAILs)

- Contractions found only inside verbatim transcript quotes — exempt from STE100
  (quote fidelity wins): ep04:100 ("This can't work"), ep07:112/125/232/244
  ("we're really buying is time"), ep08:85 ("It's like when people..."). No fix.
- Builder's `_coverage.md` has three errors worth correcting: it attributes the
  moat question to "(Dwarkesh's question)" — the transcript shows Ben asking;
  it claims MIG is covered at ep11:44-66 but MIG never appears in the chapter;
  the ep07 transcript-artifact typos it flags ("path Matos," "stevik,"
  "microsof Ian," stray "横跨") are still in ep07.md — the cleanup pass is still
  owed.
- E1 exam gate (20 questions, 100% answerable) was not run: it is in
  TRACK_AUDITOR_BRIEF.md but outside this task's adapted gate list (G1–G9 +
  P1–P3). Recommend running it after the fix loop.
- No em dashes or en dashes in any of the 11 chapters (clean); none of the other
  banned phrases ("it is important to note", "in today's world", "when it comes
  to", "at its core") appear.

## Consolidated fix list (severity order)

1. ep04: fix Waymo economics comparison → "one year of Uber's profits" [H1/G1]
2. ep03: fix nine-waves table row 9 — remove or mark [builder inference] [H2/G1/G9]
3. ep03: remove "Jamie Dimon opened the show" (not in transcript) [H3/G1]
4. ep07: add the "constellation of apps" strategy subsection [H4/G1]
5. ep10: fix Jensen quote → "the AI heard around the world" [H5/G9]
6. ep01: split the CUDA subchapter into one-idea subchapters [M1/G2]
7. ep04: split the transformer subchapter into one-idea subchapters [M2/G2]
8. ep05: define "Dutch auction" at first use [M3/G3]
9. ep11: define TDP, SXM, NDR, PSU, 8U at first use [M4/G3]
10. All chapters: rewrite figure captions to name "AI Podcast Curriculum" + specific source [M5/G5]
11. All chapters: remove ~109 prose semicolons (per-chapter lines in L1) [L1/G8]
12. ep06/ep09/ep10: replace 9 banned-word hits (per-line in L2) [L2/G8]
