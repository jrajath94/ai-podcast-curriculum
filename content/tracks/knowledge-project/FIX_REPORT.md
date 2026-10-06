# FIX REPORT — Knowledge Project track (Shane Parrish)
**Fix agent.** Date: 2026-10-06. Scope: `content/tracks/knowledge-project/`, against `research/knowledge-project/transcripts/`.
**Read verbatim first:** AUDIT_REPORT.md, `build/VISUAL_SYSTEM_GENERIC.md`.
**Rule followed:** edit in place, verify each fix against the transcript, run `ste-lint/bin/ste_check.py` on every edited file (0 hard fails on all 11 files), fix nothing that is not broken.

## F1 — ep03 60% operating margins (G1/G3/G8) — NOT BROKEN, auditor false positive

**Before:** audit claimed the transcript says only "two of the highest operating margins in the history of business" and that "No 60% anywhere in the transcript."
**After:** no edit. The claim is transcript-faithful.
**Verification:** `research/knowledge-project/transcripts/yBBhd0-Os74.txt` contains, in one breath: "those two companies have two of the highest operating margins in [snorts] the history of business. They have like 60% operating margins and they're they're duopies and and they were created by the banks." The sentence the auditor quoted is immediately followed by the 60% sentence — the audit stopped one sentence early. Chapter wording ("roughly 60 percent operating margins, among the highest in the history of business", body and Q7) is a faithful paraphrase of "like 60%". Independently corroborated: podcastnotes.org episode notes for this exact video record "Visa and Mastercard have two of the highest operating margins in the history of business, around 60%"; citybiz.co and podcastalpha.substack.com both report Gurley said ~60% on this episode. Cutting the number would have removed episode-faithful content. No change made, by design.

## F2 — ep03 figure-sparse (G4) — FIXED

**Before:** 1 figure (fig1 derivatives mermaid) for 16 coverage claims.
**After:** 4 figures, all state-change-only, ladder-correct, four tests documented in the figure-audit table (u01-u04).
- Figure 2 (ep03.md:125). Circular deal money loop. Mermaid, 4 nodes: Cloud provider --Gives $5B--> AI lab --Spends back on cloud--> Cloud provider, plus Books revenue / Books capability nodes. Medium ladder: a move forces mermaid (table banned for moves). Numbers transcript-verified ($5B, "if you did not give it to them, they would not spend it").
- Figure 3 (ep03.md:148). Stablecoin rails comparison table. 4 rows: ACH 3 days (cost: Not in source, per visual-system law), same-day wire $25 plus a page of forms, card payment 2 to 3 percent, USDC seconds for pennies. Medium ladder: comparison of values forces a table. Every number from the transcript (three days, $25 + forms, "2 or 3%", "within seconds... for pennies", dollar-for-dollar backing already in body).
- Figure 4 (ep03.md:192). Equal-partnership before/after table. 6 rows: leadership, compensation, talent, sharing, new people, orphan work (the 15-year splash page). Medium ladder: architecture comparison forces a table. Content transcript-verified ("no lead partner, there's no king, there's no president... just five", equal shares, shared CFO introductions, no comp review, the website story).
**Verification:** figure numbering sequential in document order (1-4); audit table rows u02-u04 added with the Four tests column; ste_check 0 hard fails.

## F3 — ep07 figure-sparse (G4) — FIXED

**Before:** 1 figure (fig1 five-step loop mermaid) for 20 coverage claims.
**After:** 4 figures, all state-change-only, ladder-correct, four tests documented (u01-u04).
- Figure 1 (ep07.md:57). Believability-weighted voting: the three-doctor method. Table: voter / believability / weight. No invented numbers — weights are qualitative (near zero; weighted by track record), because the episode gives no numeric scores. Medium ladder: a score (inputs, weights, output) forces a table.
- Figure 2 (ep07.md:100). The five-step loop (existing figure, renumbered from Figure 1; content unchanged).
- Figure 3 (ep07.md:118). The two yous: before/after table. Rows: lives in (amygdala / prefrontal cortex), built for (fight or flight / truth and learning), hears challenge as (attack / useful data), Dalio's move (name it: that is the emotional you / let it hold the pen). Medium ladder: state comparison forces a table.
- Figure 4 (ep07.md:139). The pain button loop. Mermaid, 7 nodes: Pain hits -> Capture facts fast -> Answer the prompts -> Design the action -> Follow through -> {Pain recurs?} Yes->prompts, No->Principle banked. Medium ladder: a step loop forces mermaid.
**Verification:** renumbering was needed because the believability claim sits before the five-step section in document order; figures now read 1-4 top to bottom; the only other "Figure" reference in the chapter was the audit table, updated to fig1-fig4. ste_check 0 hard fails.

## F4 — ep07.md:190 contraction (G7) — FIXED

**Before:** `...name it ("that's the emotional you"), and let the prefrontal you hold the pen.`
**After:** `...name it ("that is the emotional you"), and let the prefrontal you hold the pen.`
**Verification:** not a transcript quote (builder's own voice), so STE100 no-contraction rule applies. Independent grep confirms no remaining contractions in ep07 outside verified verbatim transcript quotes. The new Figure 3 table uses the same fixed wording ("that is the emotional you") for consistency.

## F5 — track-level shell tags + four tests (G4) — FIXED

**Before:** every figure carried a decorative "Shell N" label with no 1-5 sequencing anywhere (ep06: Shell 2,3,2; ep01: Shell 2,3,2,1); figure-audit tables never documented the four tests.
**After (decision: drop the labels):** the Russian-doll 1-5 sequencing was never built — the figures are standalone lesson plates. Faking sequential numbers would lie about content (a count table is genuinely Shell-2 content; renumbering it Shell 1 would mislabel it). Per the audit's passing criteria, all 23 "Shell N. <verb>." labels were removed from captions across ep01-ep10 via exact-pattern edit (verified: zero "Shell [0-9]" remain in any chapter or the cheatsheet). Captions keep the project name, episode, and source per caption law.
**Four tests:** every figure-audit table (all 10 chapters, 29 figures: 23 existing + 6 new) now carries a "Four tests" column: T1 object look / T2 rule forcing the shape / T3 one changeable number / T4 symbol the next page reuses. Honest answers throughout: T3 is "none, static plate" everywhere — no figure exposes a reader-changeable number (the medium ladder reserves Canvas 2D for that case, and no claim here needs it). Ep01's table also gained its missing u04 row for fig4 (priority circles), which the old table omitted.
**Verification:** spot-checked captions render cleanly ("Figure 1. Reading time and rank, per the episode. AI Podcast Curriculum, ep01 (Naval Ravikant, 2019-08-17). Source: original toy, from episode claims."); ste_check 0 hard fails on all chapters.

## Typos — FIXED (4)

- ep03.md:258 "5, The circularity check." -> "5. The circularity check."
- ep08.md:205 "with a invoice attached" -> "with an invoice attached"
- ep09.md:33 opening quote "Put aside your intuition. do not try to form..." -> "Do not try to form..." (transcript has "Don't"; the chapter normalizes to STE100, so the capital D is correct)
- cheatsheet.md:124 "800 rejection letters, day one -> in a row." -> "First book sold on day one, then 800 rejection letters in a row." (matches ep08.md:155 body)

## Blanket source notes — ADDED

- ep07.md:25: "Note on the source: the transcript is YouTube auto-generated captions. Numbers and names below follow the transcript. Where the captions garble a name, it is marked [uncertain]." (ep02-style; the chapter previously had no note although it rests on auto captions with numbers like 250%, $4,000, ~75 years, 22%)
- ep09.md:27: replaced its looser note with the ep02-style convention, preserving its name mappings: 'Numbers and names below follow the transcript. Where the captions garble a name, it is mapped ("Paul Mill" = Paul Meehl, "Nick Nesbet" = Richard Nisbett) or marked [uncertain].'

## Summary

- Fixes applied: 5 of 6 findings (F2, F3, F4, F5, typos + source notes).
- Could not be "fixed" as stated: F1. The finding's premise is wrong — the research transcript contains "They have like 60% operating margins" in the sentence immediately after the one the auditor quoted, and three independent episode summaries corroborate ~60%. The chapter is faithful; cutting or [uncertain]-tagging the number would have damaged an accurate chapter. Recommend the coordinator record F1 as a false positive in the audit report rather than a pass-by-fix.
- ste_check.py: 0 hard fails on all 11 edited files (ep01-ep10, cheatsheet). Warnings are pre-existing noun-cluster noise, unchanged in kind.
- Nothing else touched: no other prose, numbers, quotes, or figures were altered.
