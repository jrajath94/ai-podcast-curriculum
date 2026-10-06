#!/bin/bash
# Final slow retry for subtitle downloads (60s pacing to dodge 429s).
cd ~/workspace/ai-podcast-curriculum/research/hidden-brain/transcripts
for vid in uYzzfQ51V2U kpfzh2rsV1c aJX2H54MPXY A8uokmk_MvE p6l-bd34Hhk; do
  ls "$vid".*.srt >/dev/null 2>&1 && { echo "SKIP $vid (have srt)"; continue; }
  echo "=== $vid"
  timeout 180 python3 -m yt_dlp --no-check-certificate \
    --extractor-args "youtube:player_client=android" \
    --skip-download --no-warnings --write-subs --write-auto-subs \
    --sub-langs "en.*" --sub-format "srt" \
    -o "%(id)s.%(ext)s" "https://www.youtube.com/watch?v=$vid" 2>&1 | grep -E "Writing|ERROR" | head -4
  sleep 60
done
echo "SUBS-RETRY2-DONE"
ls *.srt 2>/dev/null | wc -l
