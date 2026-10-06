#!/bin/bash
# Fetch verified metadata for Hidden Brain videos missing from meta.tsv.
cd ~/workspace/ai-podcast-curriculum/research/hidden-brain
have=$(cut -f1 meta.tsv 2>/dev/null | sort -u)
for vid in $(cat ids.txt); do
  echo "$have" | grep -qx "$vid" && continue
  timeout 90 python3 -m yt_dlp --no-check-certificate --skip-download --no-warnings \
    --print $'%(id)s\t%(title)s\t%(view_count)s\t%(upload_date)s\t%(duration)s' \
    "https://www.youtube.com/watch?v=$vid" 2>/dev/null >> meta.tsv
  echo "fetched $vid -> $(tail -1 meta.tsv | cut -f1)" >&2
  sleep 3
done
echo "META-DONE $(wc -l < meta.tsv)"
