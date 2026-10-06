# FIX REPORT — Charisma track (Track 15), AI Podcast Curriculum
Date: 2026-10-06. Fix agent. All fixes applied in place, verified against transcripts, ste_check.py run on every edited file (exit 0, zero HARD failures).

## 1. ep01 (G8) — [uncertain] flags for 54% lie detection sourcing and Wiseman retellings

**Before:** The coverage map (_coverage.md:285) promises `[uncertain]` flags for "54% lie detection sourcing" and "Wiseman retellings", but neither appeared in ep01.md. The 54% claim at the lie-detection paragraph carried no flag; the two Wiseman claims (luck study at line 134, other-shoe effect at line 162) carried none.

**After (ep01.md):**
- Line 150: "Humans detect lies at about 54 percent accuracy, barely above a coin flip [uncertain: the episode states the figure without naming the original study]."
- Line 134: "...Luck, in this telling, is attention [uncertain: retold on air as Wiseman's study, the original study not named]."
- Line 162: "...Perfection raises it [uncertain: retold on air as Wiseman's work, the original study not named]."

**Verification:** Transcript VHUrdELKjDw.txt lines 4919-4924: the episode states "54% accuracy" with no source named. Transcript line 1154 names "Dr. Richard Wiseman did a study" and line 3812 "another study by Dr. Richard Wiseman" — researcher named on air, but neither original study is named, matching the existing flag convention (cf. line 104's 12.5x flag). The promise in _coverage.md is now kept; no _coverage.md edit needed.

## 2. ep04 (G5) — CAECE does not decode, fixed to CACEE

**Before (ep04.md:172):** "Mnemonic for the five styles: CAECE. Conviction, Authentic, Comedian, Energetic, Empathetic. 'Charisma Arrives Everytime Confidence Emerges' is the stretch version."

**After (ep04.md:172):** "Mnemonic for the five styles: CACEE. Conviction, Authentic, Comedian, Energetic, Empathetic. 'Charisma Always Chooses Energetic Expression' is the stretch version. Pick two."

**Verification:** The five styles (ep04.md lines 35-39: Conviction, Authentic, Comedian, Energetic, Empathetic) initial as C-A-C-E-E = CACEE. The old acronym CAECE and the old stretch phrase ("Charisma Arrives Everytime Confidence Emerges" = C-A-E-C-E) both failed to decode; the new acronym and phrase both decode to C-A-C-E-E.

## 3. ep07 (G3) — 60% total gain and 400%/quadrupled

**Item A — "60% total gain" (ep07.md line 82).**

**Before:** "Sales rose another 15 percent, for a 60 percent total gain over the original." The audit claimed the transcript gives 45% then 15% with no stated base.

**Verification (transcript aO4RC70qU1U.txt lines 1214-1219):** the episode says the headline change "produced a 45 increase in sales", then "if the bose marketing department added testimonials they produced a 15 greater increase to 60 percent increase from the initial generation of that ad so it was both of those things together". The 60% combined figure and its base ("from the initial generation of that ad") ARE stated on air — this is the speaker's own arithmetic, not a builder computation. The auditor's "no stated base" claim is inaccurate.

**After (ep07.md line 82):** "The episode reports a further 15 point increase, for a 60 percent increase from the initial generation of the ad." The figure is now attributed to the episode in its own terms, removing any appearance of builder-side computation.

**Item B — "rose 400%" vs "quadrupled" (ep07.md line 112 and Q&A #8).**

**Before:** "Donations rose 400 percent. Four words of shared identity quadrupled giving."

**Verification (transcript aO4RC70qU1U.txt line 1493):** "donations went up 400 percent". An increase OF 400% is a 5x multiple, so "quadrupled" (4x) was wrong.

**After (ep07.md line 112):** "Donations rose 400 percent. Four words of shared identity quintupled giving." One consistent multiplier (5x) used throughout; Q&A #8 ("Four hundred percent is the measured difference") is consistent with "rose 400 percent" and needed no change.

## 4. ep07 (G8) — Bose headline misquote

**Before:** ep07.md line 82 and Q&A #6 presented "Hear what you lose by waiting" as the episode's Bose headline.

**Verification (transcript aO4RC70qU1U.txt lines 1204-1208):** the episode's actual headline was "hear what you've been missing". The builder's rewording was presented as verbatim.

**After:** The headline is reworded in an STE-compliant form and explicitly marked as a paraphrase (verbatim quoting is impossible under STE because "you've" is a contraction and "you have been" is a perfect tense — both HARD fails under ste_check.py):
- Line 82: 'Changing the headline to the loss-framed line "hear what waiting costs you" (paraphrase of the episode headline, reworded for style) raised sales 45 percent...'
- Q&A #6: "Why did the loss-framed headline beat 'new'?" with the answer ending: "The episode headline (hear what waiting costs you, paraphrase) changed the frame and lifted sales 45 percent."

No remaining occurrence of "Hear what you lose by waiting" anywhere in the track.

## 5. ep08 (G5) — incoherent 13-law acronym

**Before (ep08.md:178):** "Mnemonic for the thirteen: DoPeRS CaNDi DOrM SAF. Demonstrate, Purpose, Release, Suspend judgment, Character, Absence, Wonder, Desire, Own time, Resist madness, Madness of groups is R... (use the table instead. Thirteen is too many for one acronym)."

**After (ep08.md:178):** "Mnemonic for the thirteen: four triads plus one. Triad 1: self (demonstrate, purpose, release). Triad 2: mind (negative capability, character craft, drop cynicism). Triad 3: others (judge behavior, absence, desire). Triad 4: world (time, groups, fools). Plus one: insignificance. Three plus three plus three plus three plus one is thirteen."

**Verification:** Broken acronym deleted; the four-triads-plus-one structure (which already existed below it and decodes) is promoted as the memory aid, with a count check confirming 13.

## 6. ep10 (G2) — stray "M" + split "Metal" in Q&A #4

**Before (ep10.md lines 184-185):** `"M` then a line break then `etal object" opens a prediction gap...`

**After:** `"Metal object" opens a prediction gap: knife, gun, mystery. "Spoon" closes it. The gap is a crystal ball, and the audience stays to check their guess.` Stray character deleted, word joined.

## 7. ep10 (G5) — "EB BHCH" drops a B

**Before:** ep10.md line 201 (now 200): "Mnemonic for the six devices: EB BHCH." Also in the figure audit table (now line 259): "T4: EB BHCH reused in mnemonics". cheatsheet.md line 106: "- Six devices EB BHCH: ..."

**After:** All three corrected to "EBBHCH".

**Verification:** The six devices (Elephant, Backpack, Breadcrumbs, Hourglass, Crystal ball, Humor) initial as E-B-B-H-C-H = EBBHCH; the six-word phrase mnemonic ("Every Brave Bard Holds Captivating Hearers") already decoded correctly and is unchanged.

## STE check
ste_check.py run on all six edited files (ep01, ep04, ep07, ep08, ep10, cheatsheet.md): exit code 0, zero HARD failures. (One iteration was needed: the first-draft Wiseman flags used semicolons, which are HARD fails; replaced with commas. Remaining warnings are pre-existing track-wide noise.)

## Summary
- Fixes applied: 7 of 7 (ep01 flags, ep04 mnemonic, ep07 60% attribution, ep07 400%/quintupled, ep07 headline paraphrase, ep08 acronym, ep10 line break, ep10 + cheatsheet EBBHCH).
- Could not be fixed: none.
- Auditor inaccuracy found during verification: the G3 claim that the 60% figure had "no stated base" is wrong — the transcript states "60 percent increase from the initial generation of that ad". Fixed by attribution rather than deletion.
