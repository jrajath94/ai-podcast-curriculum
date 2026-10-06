# AUDIT REPORT — Conversations with Tyler track
Auditor: subagent (depth 2/2). Date: 2026-10-06.
Scope: `content/tracks/conversations-with-tyler/` — ep01–ep10, index.md, cheatsheet.md, _coverage.md.
Sources read verbatim: MASTER_BRIEF.md, REJECTIONS.md, TRACK_AUDITOR_BRIEF.md, VISUAL_SYSTEM_GENERIC.md, TRACK_BUILDER_BRIEF.md.
Transcripts: official conversationswithtyler.com transcripts in `research/conversations-with-tyler/transcripts/`.

## Verdict summary

| Chapter | G1 | G1b | G2 | G3 | G4 | G5 | G6 | G7 | G7b | G8 | G9 | Figures F1–F7 | Chapter verdict |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| ep01 Gladwell | PASS | PASS | PASS | PASS | PASS | PASS | PASS | PASS | PASS | FAIL | PASS | PASS | FAIL |
| ep02 Paglia | PASS | PASS | PASS | FAIL | PASS | PASS | PASS | PASS | PASS | FAIL | PASS | PASS | FAIL |
| ep03 Kotkin | PASS | PASS | PASS | PASS | PASS | PASS | PASS | PASS | PASS | PASS | PASS | PASS | PASS |
| ep04 Thiel I | PASS | PASS | FAIL | FAIL | PASS | PASS | PASS | PASS | PASS | PASS | PASS | PASS | FAIL |
| ep05 Thiel II | PASS | PASS | FAIL | FAIL | PASS | PASS | PASS | PASS | PASS | PASS | PASS | PASS | FAIL |
| ep06 Lahiri | PASS | PASS | PASS* | PASS | PASS | PASS | PASS | PASS | PASS | FAIL | PASS | PASS | FAIL |
| ep07 Pinker | PASS | PASS | PASS* | PASS | PASS | PASS | PASS | PASS | PASS | PASS | PASS | PASS | PASS |
| ep08 Deutsch | PASS | PASS | PASS | PASS | PASS | PASS | PASS | PASS | PASS | PASS | PASS | PASS | PASS |
| ep09 Austin | PASS | PASS | PASS | FAIL | PASS | PASS | PASS | PASS | PASS | PASS | PASS | PASS | FAIL |
| ep10 Ferguson | PASS | PASS | PASS | FAIL | PASS | PASS | PASS | PASS | PASS | PASS | PASS | PASS | FAIL |

PASS* = pass with noted borderline (see findings). Chapter verdict FAIL = at least one FAIL item per the brief's letter ("every hit is a FAIL item" for G8; zero unmapped major items for G1; etc.).

## Builder's honest gaps — verification

1. **ep01–ep05 written in a prior session, not fully re-audited by builder: CONFIRMED AS A REAL RISK.** I read all five fully and spot-checked 8+ transcript items per episode. Coverage is strong (all items found), but the structural failures live exactly here: ep04 has zero `###` subchapters, ep05 has two. The prior-session chapters need the re-audit the builder skipped.
2. **Figures are tables only (first medium on ladder): CONFIRMED, ACCEPTABLE.** Every figure is a comparison/count table, which is the first medium that passes the ladder for these claims. Captions name the project ("AI Podcast Curriculum") + shell + source. Figure-audit tables exist in all 10 chapters with no blank figure cells. Notes: shells used are 1/2/3/5 (shell 4 never used); numbers are hand-verified rather than code-computed — I recomputed every one (see G3-numbers below) and all check out.
3. **ep08 Wittgenstein attribution: RESOLVED, NOT A FAIL.** Transcript line 73 (`b_6vYwCkIpc.txt`): "as Wittgenstein is supposed to have said (I don't know whether he really did), if it were true, what would it feel like? It would feel just like this." The chapter conveys the caution in prose ("which Deutsch attributes with a caution he may not have said it") and `_coverage.md` tags it `[uncertain attribution]`. Faithful handling.

## FAIL findings (chapter, location, gate, what's missing, what passing looks like)

### F1. ep04 — G2 no-subchapter structure
- Location: ep04.md, whole chapter.
- Gate: G2 / MASTER_BRIEF law 4 / REJECTIONS #5.
- What's missing: the chapter has zero `###` subchapters. Five `##` sections each introduce 3–6 ideas: "Why not Calvinism?" (five points, Girardian argument, intellectual argument, EAs-as-Calvinists, Pope Francis, Lutheranism); "Schmitt: friends, enemies, and the scapegoat machine" (friend-enemy, Reagan dinner, scapegoat-machine critique, cyclicality objection, Thucydides vs Daniel); "The Antichrist comes first" (risk list, two novels, post-1945 novel, Bostrom 2019, feudalism objection, Bitcoin coda); "Agency, Shakespeare, and Caesar" (agency vs Lutheranism, Rand, mimetic Shakespeare, Caesar reenactment, Booth); "AI: bad news for the math people" (math-verbal reversal, French Revolution testing, AI geopolitics, hedgehog/fox).
- Passing: split each into `###` subchapters, one idea each.

### F2. ep05 — G2 missing subchapters
- Location: ep05.md lines 108–191 ("Overrated and underrated", "Company names predict" is fine, "Germany, California, and the average", "Advice and the audience").
- Gate: G2 / law 4.
- What's missing: "Advice and the audience" (~37 lines) bundles ~15 topics (Mercatus advice, vertical-progress tips, nonprofits, plumber, private cities, democracy update, Congress 35/535, Solyndra, money, Indonesia, life extension, inequality, Gresham's law, super-rich happiness) with no subchapters. "Overrated and underrated" bundles Keynes, NYC, China, Brazil. "Germany, California, and the average" bundles Germany/California, death-age arithmetic, favorite novels.
- Passing: `###` per topic, one idea each.

### F3. G3 zero-knowledge — undefined terms at first use (7 terms)
- ep05.md:88 — "zero-marginal-product worker": used, never defined. (Marginal product = the extra output one more worker adds; a zero-marginal-product worker adds none.) Passing: one-sentence definition at first use.
- ep05.md:84 — "the Straussian reading": used three times, never defined. (Reading for the hidden/esoteric message, after Leo Strauss.) Passing: define at first use.
- ep04.md:90 — "the Overton window": used, never defined. (The range of ideas acceptable in public discourse.) Passing: define at first use.
- ep04.md:151 — "eschaton" (in the immanentize-the-eschaton quote): undefined; the katechon gloss does not cover it. Passing: gloss it.
- ep10.md:78ff — "Whig or Tory, Jacobite": the section gives context but never defines the three terms for a zero-knowledge reader. Passing: one line each at first use.
- ep10.md:115 — "The Rankean in Taylor revolted": "Rankean" undefined. (After Leopold von Ranke: history from primary documents, no invention.) Passing: define at first use.
- ep09.md:130 — "Is the Mishnah bigger than the Torah now?": neither term defined. Passing: one clause each.
- ep02.md:240 — "poststructuralist or postmodernist": undefined. Passing: one clause.
- Well-defined counter-examples (not fails): Caribbean Enlightenment (ep01), negative influence (ep01), dissertation director (ep02), hermeneutics of infrastructure (ep09), katechon (ep04), hysteresis (ep05), mysterianism/qualia (ep07), open/closed-class words (ep07), marination (ep03).

### F4. G8 style hits (4 hits, 3 chapters)
- ep01.md:224 — contraction "that's" in the quoted thought "that's what the kids think". Passing: "that is".
- ep02.md:260 — banned word "realms" in builder paraphrase ("the political and professional realms should go"; only "equal opportunity feminist" is the transcript quote). Passing: rephrase without the banned word.
- ep06.md:35 — banned word "unlocked" ("It unlocked something"). Passing: rephrase.
- ep06.md:314 — banned word "unlocks" ("What unlocks?"). Passing: rephrase.
- Clean: no em dashes anywhere; no semicolons in prose (all `;` hits are inside table markup).

### Borderline notes (not fails)
- ep06 G2: "### Starnone and Ferrante" bundles Starnone, Ferrante unmasking, bilingual selves, Gogol-passing; "### Parents and process" bundles parents, inhibition, "The Exchange", process. Each is arguably one theme (anonymity; process), but a strict one-idea reading wants splits.
- ep07 G2: "### Rap and the passive" bundles rap, aerobic exercise, behavioral economics; "### The passive, defended" bundles passive voice, Shatner, Sontag on photography. These are lightning-round items of 2–4 sentences each; grouping is defensible, but the subchapter titles misname the contents.
- ep02 G2: "### The fights" groups four anecdotes; all serve the single idea (her break with feminism). Acceptable.
- G6: only ep01 uses the literal "like I am new" phrasing, but every chapter has beginner-explanation questions in substance ("What is hysteresis in this episode?", "Explain the two-machine theory of language in one example") plus applied follow-ups. Passes on substance.
- Quotes: two quotes are contraction-expanded paraphrases presented in quotation marks — ep01 "Why does not Louis Vuitton sell a $59 bag?" (transcript: "why doesn't Louis Vuitton sell a $59 bag?") and the athlete/pessimist line is paraphrased without quotes (fine). The coverage map discloses the STE100-paraphrase policy globally but does not flag these two instances individually. Minor; not a fail given the disclosed policy.

## G1 coverage spot-checks (auditor's own, 8+ items per episode, transcript → chapter)

- ep01 (Gladwell): Mennonite/original sin, 10,000 hours, Jackie Robinson, Mamie/Kenneth Clark doll tests, Dumbarton Oaks, Rosenwald, underhand free throw, Tina Fey satire, Snowden, Klarman, David Epstein, Louis Vuitton $59, "Oh, thank God!", fur-lined rat hole, Brown Face Big Master p.178, Lynda Resnick, Terry Martin, Goodbye Cruel World — all present in both. 18/18.
- ep02 (Paglia): 7 publishers/5 agents, Salon 1995, lamb vindaloo, Amelia Earhart, Kate Millett, Rita Mae Brown, "Rolling Stones are sexist", Morlocks/Eloi, Spenser/Sade intro (verbatim line 1) — all present. 9/9.
- ep03 (Kotkin): "empty than Canada", Baikal, Israel-neighborhood, Akademgorodok, Dzungars, Danish label butter, six resignations, "What would Stalin do?", Mephisto, 38th parallel, $10M house, de Certeau, Englewood — all present. 13/13.
- ep04 (Thiel I): pin factory, Romulus/Cain and Abel, Benson, Solovyov, 1 Thessalonians 5:3, Booth/"Sic semper tyrannis", hedgehog/fox, Pope Francis rebuttal (verbatim line 39) — all present. 8/8.
- ep05 (Thiel II): 140 characters, hysteresis, mail-room Einstein letter, Alcatraz 7 months 3 days, least-conformist Japan, OGX/McLaren, Airbnb/Uber names, Solyndra, "long substance, short status", 2.2–2.5 yrs/decade, Asperger's, Indonesia, plumber, $100K/$1B (line 13), Congress 35/535 (line 457) — all present. 16/16.
- Zero unmapped major items found. The coverage map's "Unmapped" lists (intros/outros/banter) are accurate.

## G3 numbers — recomputed

- ep01: 0.95^20 = 0.3585 → ~64% spent ✓; 0.95^100 = 0.00592 → ~99% ✓; drill answers $599M/$358M/$6M remain ✓; 3:35 = 215 s ÷ 3.75 laps = 57.3 s/lap ✓; 2014−1961 = 53 years ✓; 7+5 = 12 rejections ✓.
- ep02: 7+5 = 12 ✓.
- ep03: 1% → 99:1 forced-to-voluntary ✓; 10,000 ha → 100 voluntary, 9,800 forced ✓.
- ep05: $1B/$100K = 10,000:1 ✓; 35/535 = 6.54% → "about 6.5 percent" ✓ (535 = House+Senate, chapter's context); Solyndra 2r/2πr = 1/π ✓.
- ep06: ages 3→18 = 15 years ✓.
- All transcript numbers match (38 colleges, $40B endowment, $450B fracking, 165 irregulars, snuck ~120 yrs, 90% algorithm, 12% gamers, 18–20M deaths, six resignations 3+3).

## E1 exam gate — 20 understanding-check questions, answered from chapter text only

1. Q: Name the five parts of Tyler's model of Gladwell. A: Caribbean Enlightenment (mother), Mennonite influence, Canadian modesty, mathematician father, 10,000 hours at the Washington Post.
2. Q: What arithmetic does Gladwell use against endowments? A: At 5% of the remaining balance per year, ~64% is spent after 20 years and ~99% after 100 years; spend-to-zero concentrates $50–100M/year for 10–20 years on the problem now.
3. Q: What is the Bloom saga ledger? A: 0 courses with Bloom; 7 publishers and 5 agents rejected Sexual Personae; 20 years of work; publication at age 43.
4. Q: How does Paglia decompose the 72–75 cent figure? A: It is an average across different jobs, not same-job pay; same-job gaps are rare; the average reflects flexibility choices and, at root, biological differences.
5. Q: Why does the 1% voluntary collectivization figure matter? A: The forced-to-voluntary ratio was 99 to 1, so the policy was confiscation, not persuasion scaled up.
6. Q: State Kotkin's definition of totalitarianism in one mechanism. A: The regime galvanizes people's agency, and those people, using their agency, destroy their own agency.
7. Q: What are Thiel's three options on terrible history? A: The Christian in-between (history is terrible; forgive), the woke version (terrible; forget forgiveness), the Nietzschean right (forget history as an oppressive guilt trip). The first is most tenable.
8. Q: What is the katechon and why is it dangerous? A: The restraining force holding back the Antichrist/one-world state; the danger is mimetic — the restrainer becomes the thing it restrains (Claudius/Nero; anti-communism morphing into neoliberal world governance).
9. Q: What is the 10,000-to-1 ratio and what does it prove? A: ~$100K to start a software company vs ~$1B to take a drug through the FDA; it proves the regulatory asymmetry between bits and atoms.
10. Q: What is hysteresis in ep05? A: Failure begets failure through discouragement (no sane parent pushes nuclear engineering); talent follows precedent, so signal successes in atoms could flip the cycle.
11. Q: Describe the taped-translation method step by step. A: Mother reads Ashapoorna Devi aloud in Bengali; daughter tapes her; replays the tapes; translates from sound, checking the script painfully; phones about skipped paragraphs. Six stories translated without reading the script.
12. Q: What does "My blindness is a point of view" mean in the chapter? A: Romano's near-blindness became a lens that forced harder looking; Lahiri borrows the structure voluntarily — partial Italian forces harder looking at English problems.
13. Q: What are Pinker's two machines of language? A: Rote memory (arbitrary pairings like sing/sang; ~165 irregulars) and the rule system (add -ed; walk/walked).
14. Q: How does the euphemism treadmill work? A: Attitudes stain labels, not the reverse: negro → black → African American, each absorbing the taint; it holds now, possibly because prejudice is weaker.
15. Q: Why does the transporter not trouble Deutsch? A: Physicalism — he is a running program; moving the program moves him; the multiverse fork changes nothing because rational choice tracks the proportion of worlds, which plays probability's role.
16. Q: What is the Zeus wall? A: Any claimed barrier to knowledge is logically equivalent to the supernatural; simulation theory without testable effects is Zeus with computers.
17. Q: What is the 90 percent rule? A: ~90% of Austin's discovery is the YouTube algorithm; algorithm = audience; everything else is the margin.
18. Q: What is the ideal-form move? A: Judge the game's pole against the ideal form, then judge the real pole against the ideal form; reality fails too, because building means collisions — glitches reveal the build in both.
19. Q: What is Collingwood's method? A: Reconstitute past thought from surviving relics, juxtapose it with the thought of your own time, ask what light it sheds on your predicament; never study the past for its own sake or condescend with modern values.
20. Q: What is Ferguson's Empire argument in one paragraph? A: Cost-benefit against realistic counterfactuals: the 19th-century empire ran free trade, free migration, free capital, and abolition, and built more infrastructure than indigenous alternatives; it failed primary education; net, against what was available, benign.

Result: 20/20 answerable from chapter text. E1 PASS.

## Other gates — notes

- G1b: all 10 chapters have "## How to imbibe this" (this-week actions, catch-yourself triggers, per-idea behavior changes) and "## Think it yourself" (guided-with-answers in ep01–ep03, less scaffolding ep04–ep07, unaided ep08–ep10 — the intelligence-thread arc the index states). Concrete, not fluff. PASS.
- G4: every mechanism rebuilt with a worked toy or number (endowment arithmetic, 99:1, 10,000:1, treadmill stages, bubble stages, Collingwood steps, ideal-form comparisons). PASS.
- G5: every number traced to transcript or computed; [uncertain] used at ep01:132 (Harvard behavior), ep03:315 (Baikal one-fifth, marked as general knowledge), ep08 Wittgenstein (prose caution + coverage tag). No invented quotes found; spot-checked quotes verbatim (Pope Francis line 39; $59 bag line 147; Spenser intro line 1; Collingwood lines 135/137; Lahiri degrees line 45). PASS.
- G7: sampled 20 paragraphs across all chapters; each carries a number, mechanism step, failure mode, or decision rule. PASS.
- G7b: chapters are 273–408 lines, one-sitting tight; zero-prereq except the G3 items; no repeated teaching found (memory aids are end-consolidation, permitted). PASS.
- G9: "## Skills you can now use" present in all 10; episode-vs-synthesis separated ("In the episode…" vs drills/aids); Wittgenstein handled honestly. PASS.
- Figures F1–F7: figure-audit tables complete in all 10 (4–8 units each, no blank cells); captions name project + shell + source; medium ladder honored (table = first passing medium for comparison/count claims); reject list clean (no robot/brain/glow/clipart; palette N/A for markdown tables). PASS with the two minor notes above (shell 4 unused; hand-verified not code-computed numbers).

## Recommended fix order for the builder

1. ep04 + ep05: add `###` subchapters (F1, F2) — the largest structural debt, both in prior-session chapters.
2. G3 definitions (F3) — 8 one-line glosses across ep02/ep04/ep05/ep09/ep10.
3. G8 style hits (F4) — 4 one-word rephrasings.
4. Optional: split ep06's "Starnone and Ferrante" / "Parents and process" and retitle ep07's lightning-round subchapters.
