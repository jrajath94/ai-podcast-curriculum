# FIX REPORT ,  Clearer Thinking track (Spencer Greenberg)
**Fix agent:** subagent 89dd352f | **Date:** 2026-10-06
**Sources verified against:** `research/clearer-thinking/transcripts/*.txt`, `research/clearer-thinking/episodes.json`

All 15 audit findings fixed. Every edited file ran through `~/workspace/skills/ste-lint/bin/ste_check.py`: 11 of 12 edited files exit 0 (clean or warnings only). The one exception is a pre-existing false positive on ep09's verbatim YouTube title (see note N1).

---

## F-1. ep01 cost anchor ,  transcript: "for a TOTAL of maybe 10 to 15 seconds of practice time" (bgsKaGGnIws)

- **Before:** chapter said 10-15 seconds *per review*, five exposures = about one minute per item per year (ep01.md:83, Q&A answers, memory aid, drill 1 answer, skills line, figure audit, chapter plate, cheatsheet.md:20).
- **After:** cost anchor = 10-15 seconds **total** per item per year, after four to five exposures. Drill 1 recomputed: 10 chapters × 30 pieces × 12 s = 3,600 s ≈ **1 hour per year** (was 5 hours). Chapter plate rebuilt with the corrected arithmetic.
- **Verification:** quoted passage pulled directly from `transcripts/bgsKaGGnIws.txt` ("after maybe only four exposures you only need to see this thing once a year. So for a total of maybe 10 to 15 seconds of practice time..."). Figure 4 (Quantum Country: one third extra for 6 months, one half for a year) was re-verified episode-accurate and left untouched.

## F-2. ep04 premortem ,  replaced Klein team ritual with the episode's individual "premortum" (bEiQw3Mk0rI)

- **Before:** chapter presented Gary Klein's team premortem ("gather the team... it is a year later, the project failed disastrously") plus "prospective hindsight" theory as the episode's protocol (summary, concepts, section :109-113, Q&A, memory aids, imbibing, drills, skills, chapter plate).
- **After:** section now describes what the episode actually contains ,  Spencer's proposal, confirmed by Kahneman: make a judgment, imagine it turns out bad, name the most likely explanation, adjust, average the original with the adjusted estimate ("about one third as good as asking somebody else" ,  the crowd within one head). Every occurrence renamed `premortem` → `premortum`, including concept tag, summary, Q&A :141/:160/:171, memory aids, imbibing, drill 6, skills, cheatsheet.md:68, `_coverage.md:86`, and two cross-references in ep10.md (:115, :167).
- **Verification:** passage pulled directly from `transcripts/bEiQw3Mk0rI.txt`. No "premortem" remains in ep04.md (case-insensitive grep). Klein material fully removed per the task order (not relabeled).

## F-3. ep04 judges statistic ,  expected pairwise difference, not ±4 (bEiQw3Mk0rI)

- **Before:** "sentences scattered plus or minus 4 years around that average... ranging from about 3 years to about 11" (ep04.md:39, memory aid, cheatsheet.md:61).
- **After:** "pick two judges at random and the expected difference between their sentences is about 4 years" on a 7-year average.
- **Verification:** transcript: "if you take a crime with the average sentence [of] seven years, and you take two judges at random, the difference that you would expect to find is about four years."

## F-4. ep08 sacred money ,  inverted meaning restored (kBkzT4J1CJU)

- **Before:** "For charity: money goes in but never comes out... nobody can raid it" (ep08.md:144-146, cheatsheet).
- **After:** sacred money = ordinary money exchanged at a sacred bank for money **spendable only on sacred things** (health, education, charity), with the bank verifying each payment. recipients convert back to regular money for living expenses.
- **Verification:** transcript: "sacred money would just be money that's committed to only being spent on sacred things... you could spend it on like health or education or charity... now you can only spend this on sacred things."

## F-5. Mermaid node text ≤ 4 words (visual system rule)

- **Before → after:**
  - ep02.md:112 `Note it, still study the view` → `Study the view anyway`
  - ep03.md:67-69 (auditor-missed) `Respond to cues: count, source, familiarity` → `Respond to cues`. `Strong args persuade, weak args backfire` → `Strong beats weak`. `Many args persuade, regardless of quality` → `Count beats quality` (cue detail preserved in the preceding prose paragraph)
  - ep08.md:135 `Proposer gets 5 percent of gains` → `Proposer takes 5 percent`
  - ep09.md:129-132 `Moral uncertainty: credences across theories` → `Credences across theories`. `Weighted average: blend recommendations by credence` → `Weighted average`. `Budget split: each theory gets its credence share of resources` → `Budget split`. `Risk: action no theory endorses` → `Endorsed by none`
  - ep10.md:108 `Notice what matters for the goals` → `Notice what matters`
- **Verification:** post-fix awk scan of all mermaid node labels across ep01-ep10: zero labels over 4 words.

## F-6. Six video_titles → verbatim YouTube titles (episodes.json)

- ep03 → "Deep canvassing, street epistemology, and other tools of persuasion with David McRaney"
- ep04 → "Beyond cognitive biases: improving judgment by reducing noise with Daniel Kahneman"
- ep05 → "Beyond the assumption that humans are rational (with Barry Schwartz)"
- ep06 → "Scout and Soldier Mindsets with Julia Galef"
- ep07 → "Our 300th episode! - How to have better intellectual conversations (with Uri Bram)"
- ep08 → "Systems of governance built on prediction markets with Robin Hanson"
- **Verification:** each copied character-for-character from `research/clearer-thinking/episodes.json` (dumped video_id → title mapping). ep01, ep02, ep09, ep10 already verbatim, untouched.

## F-7. cheatsheet.md:68 ,  banned filler "unlocks"

- **Before:** "Premortem: declare it dead a year hence, autopsy the future. Prospective hindsight unlocks doubt."
- **After:** "Premortum: imagine the judgment failed, explain why, adjust, average the two. Two estimates from one head." (fixes the banned word and the F-2 rename in one line)
- **Verification:** grep for the banned word across the track: zero hits.

## F-8. ep08 dead go-deeper link

- **Before:** `https://overcomingbias.com` (curl → 000, chain never completes).
- **After:** `https://www.overcomingbias.com/` ,  verified HTTP 200 via curl (1.57 s). Same destination site, live host variant.

## F-C1. Chapter plates ,  prose descriptions → actual plates (all 10 chapters)

- **Before:** each chapter ended with a paragraph *describing* a plate ("Left (without the rule): ...").
- **After:** each chapter ends with an actual chapter plate per VISUAL_SYSTEM_GENERIC.md: one title line (caption kept), a 3-column table (Left: cost without the rule | Center: the stored object | Right: cost with the rule), a one-line Tradeoff (bottom region), and a one-sentence Footer (the connection). Table is the first medium that passes the four tests (the claim is a comparison of values: without-rule vs with-rule). All plate numbers derive from page content (ep01 plate uses the corrected 10-15 s anchor. ep04 plate uses the premortum and the corrected judges statistic).
- **Verification:** every chapter file has exactly one chapter-plate caption. grep for the old prose-plate markers ("Left (without the rule)") returns zero hits.

---

## Notes for the re-audit

- **N1 (ste_check):** ep09.md:14 still trips HARD flags on the title's own phrasing, but that line is the verbatim YouTube title from episodes.json (audit-verified correct, required verbatim). Unfixable without violating F-6. Checker false positive on required content.
- **N2:** ep05.md:122 and :165 retain generic references to the Klein team premortem as a real-world concept, not attributed to any episode. Left untouched per "do not fix what is not broken". The re-audit may decide whether to rename.
- **N3:** ep01 Figure 4's Quantum Country numbers (one third / one half) were re-verified episode-accurate and deliberately not changed.
- **N4:** ste_check exit-0 on all edited files except the N1 false positive. Remaining warnings (ing-check review items, apostrophe-s possessives, long-sentence, noun-cluster) are pre-existing across all chapters ,  the audit scoped G7 to contractions/em dashes/semicolons/banned filler and noted a full-STE100 pass was never gated. My edits introduced zero new HARD failures. One self-inflicted conditional-perfect in ep02's new plate was caught and fixed before delivery.
- F-C2 (audit-table fig-id labels) and F-C3 (four-test documentation) were not in the fix order and were not touched.

**Fixes applied: all 15 findings across 12 files. Nothing from the task list could not be fixed.**
