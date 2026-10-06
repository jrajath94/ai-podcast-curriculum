# Dwarkesh Patel — research notes (researched 2026-10-06)

1. Every view count was fetched live from YouTube via yt-dlp on 2026-10-06 (not estimated); counts move daily, so re-verify at build time.
2. Completeness check: metadata (view_count, upload_date, duration) was fetched for all 211 channel videos and ranked globally; the 18 videos above the #10 threshold (786,741 views) are all history/geopolitics (Sarah Paine, David Reich, etc.) — zero AI-central misses. #11 (Satya Nadella — Microsoft's AGI plan & quantum, 756,544) is recorded in episodes.json as the first replacement.
3. AI-centrality is judgment: rank 6 ("The OpenAI/Hugging Face attack") is a 24-min solo explainer about secret AI societies inside OpenAI, not an interview; ranks are view-ranked, not quality-ranked. One borderline excluded title: "Marc Andreessen — AI, crypto, 1000 Elon Musks..." (~AI-discussing but broad; below threshold).
4. Transcripts are YouTube captions (mix of manual "en-orig" and auto-generated), converted to plain text; spot-checked coherent English and correct topics, but expect minor transcription errors — verify quotable lines against the video.
5. Fetching was intermittent (transient "not a bot" sign-in checks and HTTP 429s); the `--extractor-args "youtube:player_client=android"` flag bypassed most blocks. If re-running later, expect similar flakiness.
