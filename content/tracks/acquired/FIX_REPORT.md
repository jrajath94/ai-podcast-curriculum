# FIX REPORT — Acquired track (12 findings + 3 coverage corrections)
Fix agent: subagent. Date: 2026-10-06.
Source: AUDIT_REPORT.md. All HIGH fixes verified against the cited transcript files before editing.

## HIGH (fidelity)

### 1. H1 — ep04 Waymo economics — DONE
ep04.md:146. Replaced the false "about what Google earns in a month" comparison with the transcript's actual claim (verified in `research/acquired/transcripts/lCEB7xHer5U.txt`: "That's one year of Uber's profits."). New text: "The hosts note the 10 to 15 billion dollars Waymo burned is, in their words, 'one year of Uber's profits.'" No single-host attribution: the transcript does not clearly identify the speaker, so the audit's "per the hosts" phrasing is used.

### 2. H2 — ep03 nine-waves table row 9 — DONE
ep03.md:66-74. Removed row 9 "(Reality Labs losses)" (builder invention; never in the transcript). Verified in `QciJ9ubeLQk.txt`: eight named waves (MySpace, Twitter gen 1, Instagram, Snapchat, WhatsApp, TikTok, Apple app tracking transparency, ChatGPT); Ben says "that's nine" (apparent double-count of ATT). Added a note under the table: "The episode names eight waves, though Ben says 'that is nine.' He seems to double-count Apple ATT, which he calls out as its own category. Nothing else is named as the ninth." Figure caption retitled "The nine waves (eight named)".

### 3. H3 — ep03 "Jamie Dimon opened the show" — DONE
ep03.md:27. Deleted the claim. Verified: `QciJ9ubeLQk.txt` contains zero mentions of Dimon.

### 4. H4 — ep07 "constellation of apps" subsection — DONE
ep07.md:106-112. Added "### The constellation of apps: playing the other team's game" after "The mobile crisis" section, grounded in `CS2Lqdwja8o.txt`: the early-2010s industry belief in specialized single-purpose apps; Facebook's constellation (Slingshot, Poke, Messenger, Paper, Rooms, Riff, Camera); why it conflicted with Facebook's bundling value (engagement compounds when use cases feed into each other; single-purpose apps invited users to unbundle Facebook itself).

### 5. H5 — ep10 Jensen quote — DONE
ep10.md:42. Fixed "the moment the AI bell rang around the world" to the transcript's "the AI heard around the world" (verified in `nFB-AILkamw.txt`: "in Jensen's words the AI heard around the world").

## MEDIUM

### 6. M1 — ep01 CUDA subchapter split — DONE
ep01.md:78-96. Split "### CUDA: the ten-thousand-person-year platform" into four one-idea subchapters: "CUDA: the ten-thousand-person-year bet", "CUDA: the first-principles case", "CUDA: winning the researchers", "CUDA: the emergence evidence". No claims added or removed; the flywheel figure and emergent-abilities definition moved with their owning subchapters.

### 7. M2 — ep04 transformer subchapter split — DONE
ep04.md:83-113. Split "### The transformer: attention is all you need" into four one-idea subchapters: "The parallelization wall: why LSTMs had to go", "The attention idea: read everything first", "The rewrite and the scaling: Noam's version wins", "The publication and its cost: the paper that left the building". The transformer-chain figure stays with the publication subchapter. Verbatim quote "This can't work" untouched (transcript-quote exemption).

### 8. M3 — ep05 "Dutch auction" defined — DONE
ep05.md:121. Added one sentence at first use: "A Dutch auction is an IPO format where bidders submit price-and-quantity bids, and shares sell at the highest price that clears the full offering."

### 9. M4 — ep11 hardware terms defined — DONE
ep11-synthesis.md:56,74. Defined at first use: SXM ("NVIDIA's soldered server GPU board form factor, used in place of PCIe add-in cards") and TDP ("thermal design power: the maximum heat the cooling system must remove") in the NVLink paragraph; NDR ("an InfiniBand speed grade, 400 Gb/s per port"), PSU ("power supply unit"), and 8U ("eight rack units tall; one rack unit (U) is 1.75 inches") before the DGX spec table.

### 10. M5 — figure captions rewritten — DONE
All 30 existing captions (ep01:7, ep02:4, ep03:6, ep04:3, ep05:3, ep06:4, ep07:3) rewritten to the mandated format naming the project and the source episode, e.g. ep01.md:53: "Figure 1. The RIVA 128 decision. AI Podcast Curriculum, ep01 (Jensen Huang interview, 2023-10-16); toy built from episode claims." ep07 Figure 3 caption notes its real source ("built from Zuckerberg's 2012 email as quoted in the episode"). Captions added to all 7 inline figures that had none: ep08.md:57,119; ep09.md:76; ep10.md:84; ep11-synthesis.md:70,118,135 (each placed outside its code block). 37 captions total, all format-verified. Note: the mandated caption format itself carries one semicolon per caption ("...; toy built from episode claims"), per the audit's own example — these are the only semicolons left in chapter text, alongside exempt code/table/frontmatter ones.

## LOW

### 11. L1 — prose semicolons removed — DONE
All ~109 prose semicolons across ep01-ep11 split into two sentences or restructured (colon, list, or parenthetical). Verified: 0 semicolons remain in prose (code blocks, markdown tables, frontmatter, and the mandated caption format excluded). Also cleaned the 17 em-dashes in index.md (incl. frontmatter title, now "Acquired: Track Index") and 2 in cheatsheet.md (incl. title, now "Acquired: Cheatsheet"); 0 em-dashes remain in all 13 content files.

### 12. L2 — banned-word hits replaced — DONE
9 hits, all replaced:
- ep06.md:71 "The technical unlock:" → "The technical opening:"
- ep09.md:124 "holds all the leverage" → "holds all the bargaining power"
- ep09.md:154 "high leverage for the platform owner" → "high negotiating advantage for the platform owner"
- ep09.md:165 "who holds the leverage at renewal" → "who holds the bargaining power at renewal"
- ep09.md:180 "renewal leverage" → "renewal bargaining power"
- ep10.md:48 "Two unlocks changed everything" → "Two breakthroughs changed everything"; "the Transformer unlocked something new" → "the Transformer opened something new"
- ep10.md:116 "cutting-edge CoWoS packaging" → "advanced CoWoS packaging"
- ep10.md:155 "the most leverage to unbundle" → "the most bargaining power to unbundle"
Verified: zero banned-word hits remain in any chapter.

## _coverage.md corrections (auditor-flagged)

### (a) Moat question attribution — DONE
_coverage.md:17. "will the moat persist (Dwarkesh's question)" → "will the moat persist (Ben's question)".

### (b) MIG claim removed — DONE
_coverage.md:198. Removed "MIG" from the [S] H100 product-page source list: MIG does not appear in ep11, so the coverage claim was false. (Chose removal over adding MIG coverage, per the no-new-claims constraint.)

### (c) ep07 transcript-artifact typos — DONE (verified absent)
_coverage.md:105,208. Re-checked ep07.md: none of "path Matos," "stevik," "microsof Ian," or stray "横跨" appear in the chapter (word-boundary search clean). The builder's cleanup pass evidently already removed them; the _coverage.md notes were stale. Both notes updated to say the typos were re-verified absent.

## Caveats for the parent
- Two pre-existing contractions remain untouched per the audit's standing rule (contractions inside verbatim transcript quotes are exempt): ep04's Greg Corrado quote "This can't work" and ep07's Zuckerberg-email quote "we're really buying is time" (lines shifted by the new subsection). I introduced no new contractions.
- cheatsheet.md retains semicolons in its terse bullet notation (auditor flagged only em-dashes there; cheatsheet bullets are not prose sentences).
- ep11-synthesis.md:15 frontmatter `video_caption` keeps its semicolon (YAML metadata, not prose; not audit-flagged).
- The E1 exam gate (20 questions, 100% answerable) was out of scope for this fix pass; recommend running it next.

## Result: 12/12 findings fixed, 3/3 coverage corrections fixed. No blockers.
