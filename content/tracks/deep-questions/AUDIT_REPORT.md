# AUDIT REPORT — Deep Questions with Cal Newport (track 14)
# Adversarial audit vs adapted G1–G9 + F1–F7 + E1. Auditor only; no fixes.
# Date: 2026-10-06. Scope: ep01–ep08.md, index.md, cheatsheet.md, _coverage.md
# against transcripts in research/deep-questions/transcripts/ (8 available; ranks 8–9 absent).

## Verdicts at a glance (per chapter per gate)

| Gate | ep01 | ep02 | ep03 | ep04 | ep05 | ep06 | ep07 | ep08 |
|---|---|---|---|---|---|---|---|---|
| G1 fidelity | PASS | PASS | PASS | PASS | PASS | PASS | FAIL | PASS |
| G1b imbibe/drills | PASS | PASS | PASS | PASS | PASS | PASS | PASS | PASS |
| G2 no-jump | PASS | PASS | PASS | PASS | PASS | PASS | PASS | PASS |
| G3 zero-knowledge | PASS | FAIL | PASS | PASS | PASS | PASS | FAIL | FAIL |
| G4 mechanisms | PASS | PASS | PASS | PASS | PASS | PASS | PASS | PASS |
| G5 numbers/currency | PASS* | PASS | PASS | PASS* | PASS | PASS* | PASS | PASS |
| G6 Q&A | PASS | PASS | PASS | PASS | PASS | PASS | PASS | PASS |
| G7 density | PASS | PASS | PASS | PASS | PASS | PASS | PASS | PASS |
| G7b depth+conciseness | PASS | PASS | PASS | PASS | PASS | PASS | PASS | PASS |
| G8 STE100 | PASS | PASS | PASS | PASS | PASS | PASS | FAIL | PASS |
| G9 honesty | PASS | PASS | PASS | PASS | PASS | PASS | PASS | PASS |
| F1–F7 figures | PASS | PASS | PASS | PASS | PASS | PASS | PASS | PASS |
| E1 exam (20/20) | — | — | — | — | — | — | — | — |

E1: PASS, 20/20 answered from chapter text only (see Exam gate section).
G5 *: PASS with advisory (inline [uncertain] marking absent; see findings).

Chapter word counts: ep01 4128, ep02 3819, ep03 3767, ep04 3531, ep05 3967,
ep06 4046, ep07 5581, ep08 6401. All one-sitting tight.

## FAIL items (must fix to pass)

1. **G8, ep07.md:57** — banned filler "unlocked": "This machinery was
   unlocked for the attention economy by accident, about a decade ago, at
   Facebook." "Unlock" is on the STE100 banned list. Replace with a plain
   verb (e.g. "was opened up for" / "was put to work for"). Only banned-word
   hit in the entire track; everything else is clean.

2. **G1, ep07** — invented location name. The Matt (lawyer) answer says the
   lawyer "becomes a wills-and-trusts lawyer near Newburyport." The transcript
   says: "I could be an estate wills and trust lawyer in a town up in Cape
   an[n] you know North of Boston and small town kind of near the water."
   The source says Cape Ann; "Newburyport" appears nowhere. Worse, the
   chapter contradicts its own coverage map, which correctly records
   "NoVA to Cape Ann wills-and-trusts" (_coverage.md). Passing = "Cape Ann"
   (or "a small town near the ocean north of Boston").

3. **G1/G5, ep07** — misattributed sales number. The chapter says his student
   books "How to Win at College and How to Become a Straight-A Student ...
   have quietly sold around 400,000 copies combined." The transcript says:
   "those three student books 400,000 copies all in ... 275,000 on How to
   Become a Straight A Student." The 400,000 figure covers THREE student
   books, not the two named. Passing = name the number as three books
   combined (or name all three titles if asserting).

4. **G3, ep08:210** — "the Zeigarnik effect" used in a subchapter title and
   lead sentence, never defined. A zero-knowledge reader cannot know it
   means intrusive recall of uncompleted tasks. Passing = one defining
   sentence at first use.

5. **G3, ep07** — "career capital" used ("do not throw away career capital")
   never defined. It is Cal's technical term (rare and valuable skills that
   buy autonomy); first use must define it.

6. **G3, ep02** — "He uses Obsidian and a Moleskine." Obsidian is never
   identified (a note-taking app). Zero-knowledge readers do not know the
   brand. Passing = "a note-taking app" appositive.

## Advisory findings (not FAIL, fix recommended)

- **G5/G9, inline [uncertain]**: zero `[uncertain]` markers in any chapter.
  Three numbers are episode claims kept as stated and documented only in
  _coverage.md's honest-gaps section: ep04 "TikTok has 600 million users"
  (verified in transcript), ep06 "500 million people submitting posts a day"
  (verified verbatim), ep06 "half a trillion dollars ... for about $30 a
  month" (verified; hedged with "something like"). The strict G5 reading
  wants unverified claims marked inline. They are faithful to the source,
  so this is advisory, not fail.
- **G9 quote nit, ep06**: Thompson/Atlantic quote renders "a way to leave a
  mark on a world" — transcript says "a way to leave one's mark on a world."
  Minor; restore "one's" for verbatim accuracy.
- **G7 sample**: 20 random paragraphs sampled; ~17 carry a number, mechanism
  step, failure mode, or decision rule outright. The weakest (ep01 "Cal
  generalizes the point. These are things that are good for your soul...")
  was verified verbatim in the transcript, so it is episode-faithful, not
  builder padding.
- **Figures**: shell labels are inconsistent (ep01 starts at Shell 2; ep02
  has two Shell 3s and skips 4; ep05 skips Shell 2). Cosmetic metadata on
  tables; no blank figure cells, all units mapped.
- **Minor, ep01**: "ten thousand amorphous strangers" is the builder's
  illustrative number; the transcript says "an amorphous large crowd."
  Illustrative, not a factual claim; leave or soften.

## Builder honest gaps — verified

1. **Missing ranks 8–9**: CONFIRMED. transcripts/ holds 8 files only;
   dDV1bDiJSWE and PqXz2Yl_M6k are absent. index.md and _coverage.md both
   document the gap with view counts (174,874 / 125,777) that match
   episodes.json exactly. No chapters built from invented content. Honest.
2. **2 STE exceptions are verbatim YouTube titles**: CONFIRMED. The only
   HARD fails from ste_check.py are ep06.md:14 and :19 ("Abandoning") —
   both in YAML frontmatter (video_title + sources label). YouTube oEmbed
   returns exactly "Why Smart People Are Abandoning Social Media |
   Cal Newport", matching episodes.json. Legitimate verbatim-title
   exceptions in metadata, not prose. (The one prose contraction, "It's
   time to move on" in ep06:162, is inside a quote verified verbatim in the
   transcript — legitimate verbatim-quote exception.)
3. **Sponsor segments omitted**: CONFIRMED as intentional. Zocdoc/Henson/
   Blinkist/ExpressVPN reads appear in the ep07 and ep08 transcripts (5–12
   hits each); _coverage.md documents the omission as ads, not substance.
   Not missed coverage.
4. **Garbled names described generically**: CONFIRMED. Transcript says "by
   Docker ... Popular Science book" (garbled "Dacher Keltner"); the chapter
   says "a popular-science book on awe by a Berkeley psychologist" without
   asserting name or title. Correctly conservative.

## Gate evidence

**G1 fidelity** — Spot-checked 3 episodes with 8+ substantive items each,
all verified in the chapter:
- ep07 (XOPBN1kj5Xc): von Ahn TED mechanics, Khan Academy + LLM credit,
  Haynes article + LTP/Pavlovian/reward-prediction-error (verbatim
  "11 distinct brain regions ... just six"), like-button origin (30–40
  congrats), guitar strain, flow-vs-deliberate-practice + skier,
  broccoli/Happy Meal, EFT honey/bear, Matt lawyer + pirate example,
  Dylan study method + Dartmouth 4.0/3.96/no-study-past-8pm (verbatim),
  Epstein journal credit (episode 272, verbatim), Nicole + modeling +
  Feynman/von Neumann, Mara loops, Brian Ultralearning, Randall
  hobbies/strategic skills, Cage Excel planner, Don Astro Chimps/Kirkus,
  October books (Dr No crabs + anticlimax, Tishby Israel — all verbatim).
- ep08 (BcE1MqziyzQ): two pictures/dragon, Allen GTD ch.5 quote (1–6h,
  20h — verbatim), digital-not-physical, three capabilities, tool ladder,
  six lists, workingmemory.txt (5–6 vs 20–30), one-item rule, sorry
  messages (7 seconds / 7 hours — verbatim), 99% claim (verbatim), Felipe
  overhead (30 min, six sessions — verbatim), William/Rowe, Esteban,
  Martin two plans, Tracy reading + Kindle loophole, Sahil intervals,
  Don case, November books (Mounk/Gilbert/Halevi/Schwarzenegger/Grisham).
- ep06 (X-Lb81yUph4): definition (3 properties), exclusions, three harms,
  two disassociation flavors + FBI term (verbatim), Thompson quote
  (verbatim minus "one's"), reassuring-story excuses, slope + dark-web line,
  dopamine motivation + cookie, cigarette pack, embeddings "a thousand
  categories" (verbatim), tribal circuits 200–300k years, Comet Pizza,
  Pizza Hut + 500M posts/day (verbatim), mountain climber/flourishing/
  willpower rent, Selma + $30/half-trillion (verified), essay conclusion
  (verbatim incl. "It's time to move on").
- ep01 spot phrases: "tens of billions", "momentarily devastating", saloon,
  revolvers, "never had a social media account" — all verbatim in transcript.
- Coverage map: every major claim mapped with chapter:line; no unmapped
  major items found in spot checks.

**G1b** — All 8 chapters carry "## How to imbibe this" (this-week actions,
observable behavior changes, e.g. boredom ledger, day-one booking, EFT
library) and "## Think it yourself" (brain-first drills, Fermi questions,
argue-both-sides; no AI). None are motivational fluff.

**G2** — Full read of all 8 chapters: every ### adds one increment. No
0→0.5 jumps; no subchapter introduces two ideas (ep08 "Triage and the sorry
message" = one move). The repeated concepts across chapters (dopamine in
ep06→ep07, Don's case in ep07→ep08, shutdown ritual ep02→ep07) are
episode-faithful recurrences with explicit cross-references, not
re-taught material.

**G3** — 10 terms spot-checked: context shift (ep03 defined), solitude
(ep01 defined), pseudo-deep (ep03 defined), embeddings (ep06 defined),
reward prediction error (ep07 defined), long-term potentiation (ep07
defined), EFT/vmPFC (ep07 defined), demoderation/disassociation (ep06
defined), deliberate practice/flow (ep07 defined), chronic overload (ep05
defined). FAIL items: Zeigarnik (ep08), career capital (ep07), Obsidian
(ep02) — see above.

**G4** — Every explained mechanism rebuilt with a worked toy/number:
boredom intercept (ep01 fig.1), three session types scored on a 60-min memo
(ep03 fig.1), five moves (ep03 fig.2), detox/app-fix failure (ep04 fig.1),
values→tech→fences cycling example (ep04 fig.2), overhead spiral 25×2=50h
in a 45h week (ep05 fig.2 — arithmetic recomputed and correct), dopamine
prediction circuit + cookie (ep06), echo chamber derived from engagement
optimization (ep06 + drill), like-button causal chain (ep07 fig.1), EFT
honey/bear (ep07 fig.2), tool ladder (ep08 fig.1), six lists (ep08 fig.2),
the dump via workingmemory.txt (ep08 fig.3), Felipe 4h vs 4×1h
(30-min overhead → 3.5h vs 2h full cylinders; transcript's "six sessions"
preserved — ep08). Arithmetic recomputed everywhere; all correct.

**G5** — All 8 frontmatter dates match episodes.json exactly (20220515 …
20251211). "700 unread messages / 75 projects" (ep05), "1M+ English units /
Mongolian / French-speaking Africa" (ep03), "1,600-person experiment"
(ep04), "Foucault" (ep08), "2-hour midday rest" (ep05) all verified
verbatim in transcripts. No invented numbers found. [uncertain] advisory
noted above.

**G6** — 8 Q&A per chapter (all within 6–8), full follow-up answers. Each
chapter has exactly 1 "explain like I am new" Q and ≥1 "Applied:" Q
(ep01: 2, ep07: 2). Verified counts programmatically.

**G7** — 20-paragraph random sample: ~17/20 carry a number, mechanism step,
failure mode, or decision rule; remainder are episode-required narrative
with concrete facts (dates, names, events). See advisory note.

**G7b** — Chapters run 3.5–6.4k words: fully zero-prereq followable (modulo
the 3 G3 fails) and one-sitting tight. No paragraph restates earlier
teaching without adding information (cross-chapter recurrences are
episode-faithful and cross-referenced).

**G8** — Mechanical: 0 em dashes, 0 semicolons in prose, 0 true
contractions outside one verbatim quote, 1 banned word ("unlocked",
ep07:57 — FAIL), 2 HARD hits both verbatim YouTube title in frontmatter
(verified via oEmbed — PASS with documented exception). Apostrophe hits are
all possessives. ste_check.py exits 0 on every file except ep06 (the title
exceptions).

**G9** — No invented quotes/numbers. Episode-vs-synthesis separated:
prose attributes to Cal/the episode ("Cal states", "the episode rejects",
figure sources "from episode claims"); curriculum-layer sections
(drills/skills/cheatsheet) are clearly the builder's. "Skills you can now
use" present in all 8. Thompson quote minor nit noted.

**F1–F7** — Every chapter has a figure audit table; no blank figure cells.
All figures pass state-change-only (before → rule → after). Medium ladder:
tables throughout + one mermaid (ep06 slope = order/flow claim, the first
medium that passes). Captions name "AI Podcast Curriculum" + shell +
source on every figure. Lesson plates (one claim) + one chapter plate per
chapter. No AI-generated images (code-pipeline only: markdown tables +
mermaid), so the reject list is trivially satisfied; palette/grid rules
apply to generated still plates, of which there are none. Symbols
consistent (before/rule/after columns across all plates).

**E1 exam** — 20 questions, all answered from chapter text only:
1. Name the four perks of skipping social media. → Boredom (productive),
   lower anxiety, privacy, saner self-importance (BAPS). (ep01)
2. Solitude vs loneliness? → Solitude: time alone with own thoughts, no
   competing input; the workshop where experience becomes framework.
   Loneliness: pain of wanting connection and not having it. (ep01)
3. The 30-day silent test and its result? → Step away 30 days, tell no one,
   see who notices. Many wrote back: momentarily devastating — no one
   noticed. (ep01)
4. The three root-document categories? → Core documents, Productivity,
   Discipline (CPD). (ep02)
5. The four inputs to the weekly plan? → Strategic plans, calendar, task
   list, values plan. (ep02)
6. State the cascade. → Strategy shapes the week, the week shapes the day,
   the day shapes now (SWDN). (ep02)
7. Define deep work; the two conditions? → Focus without distraction on a
   cognitively demanding task. HAD: hard task, absence of switches. (ep03)
8. The three session types, sorted by the memo example? → Deep / shallow /
   pseudo-deep; strategy memo + email checks every 5–6 min = pseudo-deep.
   (ep03)
9. The five moves? → Define, Measure, Schedule, Ritualize, Train (DMSRT).
   (ep03)
10. Why did the detox fail? → The phone stayed (willpower vs engineering);
    and the phone numbed an existential void — removal meant confronting
    it. (ep04)
11. Digital minimalism vs minimization? → Minimalism = intention (values
    first, tech backwards). Minimization = less-is-better; rejected. (ep04)
12. The three steps of the cycling example? → Value (connection + cycling);
    tech chosen backwards (Facebook group); fences from the why (strip
    feed, desktop only). (ep04)
13. The three wounds of chronic overload? → Planning-center short circuit,
    overhead spiral, relentless pace (POR). (ep05)
14. Recompute the overhead spiral. → 25 projects × 2h fixed weekly overhead
    = 50h; in a 45h week the week is full (−5h) before any work starts.
    (ep05)
15. The three slow-productivity principles? → Do fewer things, work at a
    natural pace, obsess over quality (FPQ). (ep05)
16. Define a curated conversation platform. → Many people conversing +
    algorithmic curation + curation optimized for engagement (CCE). (ep06)
17. The three harms in order? → Distraction → demoderation →
    disassociation, connected by gravity (3D). (ep06)
18. Why no technological fix (Pizza Hut test)? → The two drivers —
    conversation at scale and engagement-optimized curation — ARE the
    service; 500M posts/day makes curation mandatory. (ep06)
19. Why can no app make learning as addictive as TikTok? → Learning
    requires strain (deliberate practice); dopamine neurons compare pure
    reward vs reward-minus-strain; pure reward wins. (ep07)
20. The two EFT playbook moves? → Stock the hippocampus with resonant
    examples; clarify the value sentence (EV). (ep07)
21. (bonus, ep08) The six lists? → Ready, backburner, waiting, to-discuss,
    clarify, scheduled (RBWTCS). The one-item rule? → One item per
    obligation; moves between lists, never duplicates.
22. (bonus, ep08) The 30-day maintenance routine? → Morning 5-min review,
    evening shutdown review, weekly 30-min configure with inbox to zero,
    for 4 weeks.

## Bottom line

Strong track. Six real FAIL items, all fixable with small edits: one banned
word (ep07), one invented place name + one misattributed number (ep07),
three undefined terms (ep02/ep07/ep08). The builder's four honest gaps all
verify as true. Arithmetic, quotes, dates, ranks, and view counts all check
out against transcripts, episodes.json, and YouTube oEmbed. Recommend:
fix the six FAIL items, consider the inline-[uncertain] advisory, then
SHIP.
