#!/bin/bash
# Usage: fetch_chunk.sh dq_chunk_XX
cd ~/workspace/ai-podcast-curriculum/research/deep-questions/work
chunk="$1"
urls=""
while read -r v; do urls="$urls https://www.youtube.com/watch?v=$v"; done < "$chunk"
timeout 110 python3 -m yt_dlp --no-check-certificate --skip-download --no-warnings \
  --print "%(id)s\\t%(title)s\\t%(view_count)s\\t%(upload_date)s\\t%(duration)s" $urls \
  2>>fetch_errors.log >> metadata.tsv
echo "done $chunk rc=$? lines=$(wc -l < metadata.tsv)"
