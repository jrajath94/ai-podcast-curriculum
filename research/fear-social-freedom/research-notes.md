# Research Notes — Fear & Social Freedom (Track 9)

10 episodes, arc-ordered: (a) what fear/anxiety IS → (b) protocols to overcome it → (c) social courage in practice.

## Verification method
- View counts, upload dates, durations: from `yt-dlp --print` on each watch URL, October 6, 2026. NOT estimated.
- Candidates were found in the real channel catalogs: Huberman Lab flat-playlist dump (447 entries),
  Modern Wisdom dump (2295 entries), DOAC dump (539 entries), plus targeted web search.
- All 10 transcripts fetched via the podcast-deep-dive `fetch_transcript.py` (manual subs, auto-sub fallback),
  converted to plain text, saved in `transcripts/<video_id>.txt`.

## Caveats
1. YouTube rate-limited this VM's IP repeatedly during the session (HTTP 429 / bot-checks).
   - 5 of 8 metadata lookups in the first batch failed; retried one-by-one with 15–18s sleeps — all resolved.
   - `fetch_transcript.py` exits with `NO_CAPTIONS` when the subs endpoint is rate-limited too.
     Retried with 75s spacing: all 10 transcripts fetched. **Do not trust a first NO_CAPTIONS.**
   - Consequence: no episode was dropped for captions. There are no replacements in this list.
2. Dr. Julie Smith DOAC date: Jina rendered "Mar 2, 2022"; yt-dlp returned `20220303` — used yt-dlp's value.
3. Rank 4 (Think Fast Talk Smart, 876 views): tiny view count, kept on the useful-over-famous rule —
   it is the only episode squarely on performance/speaking anxiety with an explicit protocol
   (F.E.A.R. framework, arousal reappraisal). Flagged low-reach in the JSON via the raw number.
4. Rank 8 (Modern Wisdom Zinsser, 45,480 views): full-length episode, 2022; title verified in the
   channel catalog. Modern Wisdom #917 (Vanessa Van Edwards, "The Art Of Effortless Confidence",
   Mar 2025) could NOT be found in the 2295-entry channel dump — possibly removed from YouTube.
   Zinsser is the stronger protocol pick anyway (Army performance psychologist).
5. DOAC Alex Honnold "Fear Is A Skill You Can Train" (Aug 2026) is a 26-min "Most Replayed Moment"
   compilation, not a full episode; the full episode ("The Greatest Climber Alive", Feb 19 2026)
   appears re-uploaded by a clip-farm channel (9 views), so no verified official YouTube ID — excluded.
6. Arc check: (a) neuroscience = ranks 1, 2, 10 (Haidt covers social-comparison/FOMO neuroscience);
   (b) protocols = ranks 3, 4, 5; (c) practice = ranks 6, 7, 8, 9. Every rank verified genuinely
   useful, not motivational fluff — each carries at least one concrete mechanism or drill.
