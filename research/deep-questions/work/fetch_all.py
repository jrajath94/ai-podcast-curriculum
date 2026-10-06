#!/usr/bin/env python3
"""Fetch verified view counts + metadata for candidate videos, in chunks of 25.
All output goes to the workspace (not /tmp, which is full). Idempotent: skips
IDs already present in metadata.tsv."""
import subprocess, sys, time, os

WORK = os.path.expanduser('~/workspace/ai-podcast-curriculum/research/deep-questions/work')
TSV = os.path.join(WORK, 'metadata.tsv')
CAND = os.path.join(WORK, 'dq_candidates.txt')
ERR = os.path.join(WORK, 'fetch_errors.log')

BASE = ["python3", "-m", "yt_dlp", "--no-check-certificate", "--skip-download",
        "--no-warnings", "--retries", "2", "--socket-timeout", "30",
        "--print", "%(id)s\t%(title)s\t%(view_count)s\t%(upload_date)s\t%(duration)s"]

with open(CAND) as f:
    all_ids = [l.strip() for l in f if l.strip()]

done = set()
if os.path.exists(TSV):
    with open(TSV) as f:
        for line in f:
            parts = line.rstrip('\n').split('\t')
            if parts:
                done.add(parts[0])

todo = [v for v in all_ids if v not in done]
print(f"total={len(all_ids)} done={len(done)} todo={len(todo)}", flush=True)

with open(TSV, 'a') as out, open(ERR, 'a') as errlog:
    for i in range(0, len(todo), 25):
        chunk = todo[i:i+25]
        urls = [f"https://www.youtube.com/watch?v={v}" for v in chunk]
        try:
            r = subprocess.run(BASE + urls, capture_output=True, text=True, timeout=600)
            n = 0
            for line in r.stdout.splitlines():
                fields = line.split('\\\\t')
                if len(fields) >= 5:
                    out.write('\t'.join(fields) + '\n')
                    n += 1
            out.flush()
            if r.stderr:
                errlog.write(r.stderr + '\n')
                errlog.flush()
            print(f"chunk {i//25+1}: wrote {n}/{len(chunk)}", flush=True)
        except Exception as e:
            print(f"chunk {i//25+1} EXC: {e}", flush=True)
        time.sleep(5)
print("finished", flush=True)
