#!/bin/bash
# Retry subtitle downloads for videos missing .srt files. Slow pacing.
cd ~/workspace/ai-podcast-curriculum/research/hidden-brain/transcripts
for vid in uYzzfQ51V2U kpfzh2rsV1c Exq_aynYzrM aJX2H54MPXY A8uokmk_MvE p6l-bd34Hhk PFY96JwLHTQ bTQM2XMec6M; do
  ls "$vid".*.srt >/dev/null 2>&1 && { echo "SKIP $vid (have srt)"; continue; }
  echo "=== $vid"
  timeout 180 python3 -m yt_dlp --no-check-certificate \
    --extractor-args "youtube:player_client=android" \
    --skip-download --no-warnings --write-subs --write-auto-subs \
    --sub-langs "en.*" --sub-format "srt" \
    -o "%(id)s.%(ext)s" "https://www.youtube.com/watch?v=$vid" 2>&1 | grep -E "Writing|ERROR" | head -4
  sleep 25
done
echo "SUBS-DONE"
ls *.srt 2>/dev/null | wc -l
