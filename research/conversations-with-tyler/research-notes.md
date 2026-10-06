# Research notes — Conversations with Tyler, top-10 by views (Oct 6, 2026)

1. View counts verified per-video on Oct 6, 2026 (not estimates): 276 videos via yt-dlp
   `%(view_count)s`; the other 25 via Jina Reader scrape of the watch page. Cross-check:
   Jina returned 347,982 for the Gladwell video, identical to yt-dlp's 347982.
2. Ranking covers the FULL official catalog (301 videos in the Mercatus Center
   "Conversations with Tyler" playlist, incl. the new dedicated-channel uploads).
   Near-misses just outside top 10: Sam Altman 45,777; Fuchsia Dunlop 41,220.
3. Transcripts are the OFFICIAL published transcripts from conversationswithtyler.com
   episode pages (51k-81k chars each, speaker-labeled), not YouTube auto-captions.
   rOYjgXY-Ts4 (Any Austin) is Ep. 245, recorded Mar 7 2025, uploaded Jun 11 2025.
4. Caveats: view counts are a moving snapshot (Oct 6 2026) and favor older episodes
   (7 of 10 are 2015-2017). Peter Thiel appears twice (2015 Ep.1 + 2024 political
   theology) — both kept since ranking is strictly by verified views. Guest identity
   for rank 9 verified via official episode page: "Any Austin" (stylized name).
5. Infra notes for the coordinator: (a) /tmp was 100% full (512M tmpfs, mostly other
   agents' files) — all work done under ~/workspace; (b) yt-dlp YouTube extraction
   began failing mid-run with proxy SSL CERTIFICATE_VERIFY_FAILED — curl-based paths
   (Jina Reader, conversationswithtyler.com direct) kept working; (c) transcripts
   extracted from Medium-export markup (`graf graf--p` paragraphs) on episode pages.
