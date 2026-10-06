---
name: "podcast-deep-dive"
description: "Research a podcast show: find its top episodes by verified YouTube view counts, fetch transcripts, extract topics and key claims. Use when Raj asks for podcast-based learning material or a deep dive on a show."
---

# Podcast Deep Dive

## Purpose
Turn a podcast show into research-grade source material: the top N most-viewed episodes on a topic, with verified view counts and full plain-text transcripts, plus a topic/claim extraction per episode.

## Workflow
1. Resolve the show's official YouTube channel URL. Verify it loads (`python3 -m yt_dlp --flat-playlist --print "%(id)s" "<channel>/videos" | head -3`). Never guess video IDs.
2. Dump the catalog: `python3 -m yt_dlp --flat-playlist --print "%(id)s\t%(title)s" "<channel>/videos" > catalog.txt`.
3. Filter to topic-relevant episodes by title keywords (and known guests). Keep the filter broad; rank later.
4. Verify metadata per candidate — view counts must come from YouTube, never estimated:
   `python3 -m yt_dlp --skip-download --print "%(id)s\t%(title)s\t%(view_count)s\t%(upload_date)s\t%(duration)s" "https://www.youtube.com/watch?v=<id>"`
5. Rank by view_count descending, take the top N. Record: title, URL, video_id, view_count, upload_date, guest, duration_s.
6. Fetch transcripts with `bin/fetch_transcript.py <video_id> <out.txt>` (tries manual subs, falls back to auto-subs; exits 1 with NO_CAPTIONS if none exist — replace that episode with the next-ranked).
7. For each episode, read the transcript and write: 3–6 topic tags + the 5–10 substantive claims worth teaching (with approximate position in the episode, e.g. "early/middle/late", never invented timestamps).
8. Save `episodes.json` (schema in references/episodes-schema.md) + a short research-notes.md with data-quality caveats.

## Output Contract
- `episodes.json`: ranked array, every number verified from tool output.
- `transcripts/<video_id>.txt`: clean plain text, one directory per show.
- `research-notes.md`: replacements, missing captions, anomalies.

## Operating Rules
- View counts, dates, guests: verified from YouTube output only. No estimates, no memory.
- If a channel URL 404s, find the correct official channel before proceeding.
- Mandatory-inclusion episodes (user-named) outrank pure view ranking; note the override in research-notes.md.
- Transcripts are the source of truth for claims. Quote verbatim or paraphrase with attribution; mark synthesis as synthesis.
