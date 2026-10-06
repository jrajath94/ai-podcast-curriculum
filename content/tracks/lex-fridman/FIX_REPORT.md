# FIX REPORT — Lex Fridman Track
Date: 2026-10-06. Fix agent: applied all findings from AUDIT_REPORT.md (2026-10-06).
Every HIGH finding was verified against the cited transcript file before editing.
Style gates re-checked after editing: zero contractions, zero em dashes, zero semicolons in prose, zero banned-filler hits (full-track mechanical grep).

## HIGH (fidelity/honesty)

- F-01 [G1, ep01] — DONE. Verified: ep01 transcript (JN3KPFbWCy8.txt) has zero mentions of battery/kilowatt/lithium. ep01.md:59: replaced the imported battery $600/kWh anecdote in §Physics from first principles with the episode's actual example: reasoning in the limit (even capturing the entire power of the sun, you still care about useful compute per watt; the silicon-to-voltage-transformer constraint chain).
- F-02 [G1, ep01] — DONE. Verified: transcript's simulation discussion is determinism vs free will (run simulations to see what happens; SpaceX/Tesla run simulations the same way); no ancestor-simulation argument, no "make it interesting" rule. ep01.md:67: rewrote §The simulation argument to the episode's actual discussion. ep01.md:159: rewrote the "simulation wager" drill to match (treat decisions as experiments with unknown outcomes). _coverage.md:21: map line updated.
- F-03 [G1/G5, ep03] — DONE. Verified: transcript (L_Guz73e6fw.txt) has Altman's actual remark: GPT-4 as a fictional AGI character would make a "shitty book" (underwhelming); no "write a shitty book" sustained-coherence test. ep03.md:33: rewrote to Altman's actual point (the sci-fi-character remark as his informal bar). cheatsheet.md:40: corrected the line. _coverage.md:59: map line updated.
- F-04 [G1/G5, ep03] — DONE. Verified: transcript's only "tens of thousands" refers to people in the world, not RLHF comparisons. ep03.md:40: removed the number (now "the amount is small compared to the pretraining data, not billions of comparisons"). ep03.md:101: removed the second use in the parrot explainer ("Do this many times over").
- F-05 [G9, ep04] — DONE. Verified: ep04 transcript (Kbk9BiPhm7o.txt) contains "how do you compile it the best model" but never "a dataset plus a compile". ep04.md:93: removed the quote framing; now "the team's framing amounts to: the decoder is a dataset plus a compile step." _coverage.md:92: map line updated to mark it as paraphrased.
- F-06 [G1/G5, ep07] — DONE. Verified: ep07 transcript (MVYrJJNdrEg.txt) has zero "28"; it says "starting out with a set". ep07.md:69: dropped "28" from the body; added "[Added: Meta's launch set was reported as 28 personas outside the episode.]" ep07.md:9 (frontmatter summary) and cheatsheet.md:103 softened to "launch set / launch AI personas" with the 28 figure labeled as outside reporting. _coverage.md:163: map line updated.

## MEDIUM

- F-07 [G3] — DONE. Added one-sentence first-use definitions: ep01.md:47 (GPU, H100), ep01.md:53 (token, autoregressive), ep01.md:59 (FLOPS), ep01.md:79 (parameter), ep01.md:91 (vector); ep11-synthesis.md:53 (CUDA: "Nvidia's GPU programming platform"), ep11-synthesis.md:71 (HBM: "High Bandwidth Memory, fast memory stacked next to the GPU chip"). M-06 (ep02 "parameter") covered by the ep01 definition, per audit.
- F-08 [G7b, ep10] — DONE. ep10.md:123 (Q6): compressed the verbatim repeat to a cross-reference ("see the Artificial hells section above for the rule in full"). ep10.md:126 (Q7): compressed to "(stated in the Supply chains section above)". Teaching kept in the sections.

## MINOR

- M-01 [G9, ep09] — DONE. ep09.md:84: "you cannot fetch the coffee if you are dead" → "you cannot bring the coffee if you are dead" (matches transcript "you can't bring the coffee if you're dead").
- M-02 [G5, ep11] — DONE. ep11-synthesis.md:65: header now "The 5 million dollar training cost, honestly accounted" with "(the episode's figure, widely reported as 5.6 million)". ep11-synthesis.md:168: drill now "the 5 million dollar exercise". _coverage.md:253: map line updated.
- M-03 [G5, cheatsheet] — DONE. cheatsheet.md:171: removed "Megapacks" (not in ep11 chapter or #459 transcript).
- M-04 [G9, index] — DONE. index.md:39: arc claim softened from "Episodes 9-11 (unaided): drills state the question and stop" to "Episodes 9-11 (toward unaided): scaffolding shrinks but does not vanish", noting some drills still carry guidance and embedded answers.
- M-05 [G2, ep06] — DONE. ep06.md:152-154: split the three-increment § into two subchapters: "The AGI path: text is not enough, and embodiment is the hedge" (text-insufficiency + Optimus hedge) and "The concerning part: the digital-only path is faster" (digital-only concern).
- M-06 [G3, ep02] — DONE by F-07 (no separate edit needed; "parameter" is defined at first body use in ep01, which precedes ep02).
- M-07 [G7b, advisory] — DONE. index.md:43: added "A note on method (applies to every chapter)" carrying the shared method once. All 10 chapters trimmed to one line (ep01.md:29, ep02.md:29, ep03.md:27, ep04.md:27, ep05.md:27, ep06.md:27, ep07.md:27, ep08.md:27, ep09.md:27, ep10.md:27); chapter-specific notes preserved (ep06 Transformer 2016/2017 correction, ep08 board-saga scoping, ep09 contested-positions note, ep03-ep05/ep07/ep10 date scoping).
- M-08 [G4, advisory] — DONE. ep01.md:55: added a worked token-drift toy (1 percent per-token error rate; ~63 of 100 hundred-token runs contain an error; error essentially certain by 1,000 tokens). ep02.md:41: added worked staged-combustion numbers (300/267 bar ≈ 1.12, about 12 percent more thrust at fixed engine size; full flow = 100 percent of both propellants through turbines). Both are arithmetic on existing chapter claims; no new factual claims introduced.
- M-09 [Media] — VERIFIED, no file change. ep01.md:181: the https://x.ai go-deeper link is canonical and retained; its 403 to curl is bot-blocking, not a dead link.

## Verification summary

- All 6 HIGH findings fixed against transcript evidence; both MEDIUM findings fixed; all 9 MINOR findings applied or verified.
- Mechanical style gate (the audit's G8): zero contractions, zero em dashes, zero semicolons, zero banned-filler hits across all 13 content files. Two semicolons and one banned word ("harness") introduced during editing were caught and removed before final.
- Leftovers sweep: no "shitty book", "tens of thousands of comparisons", quoted "dataset plus a compile", or battery-anecdote text remains anywhere except AUDIT_REPORT.md itself. _coverage.md map lines updated for F-01, F-02, F-03, F-05, F-06, M-02.
- Not changed (per task constraints): no figures added; no new claims beyond what the audit required; AUDIT_REPORT.md itself untouched.

## Blockers

None. All findings applied.
