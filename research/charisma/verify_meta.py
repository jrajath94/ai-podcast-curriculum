#!/usr/bin/env python3
"""Verify YouTube metadata for a list of video IDs with 429-safe retries."""
import json, sys, subprocess, time

IDS = [i.strip() for i in open(sys.argv[1]) if i.strip()]
OUT = sys.argv[2]

def fetch(vid):
    url = f"https://www.youtube.com/watch?v={vid}"
    for attempt in range(6):
        try:
            r = subprocess.run(
                ["python3", "-m", "yt_dlp", "--no-check-certificate",
                 "--extractor-args", "youtube:player_client=android",
                 "--skip-download", "--no-playlist",
                 "--print", "%(id)s\t%(title)s\t%(view_count)s\t%(upload_date)s\t%(duration)s\t%(channel)s",
                 url],
                capture_output=True, text=True, timeout=90)
            out = (r.stdout or "").strip()
            err = (r.stderr or "")
            if out and "\t" in out and "NA" not in out.split("\t")[2:4]:
                return out
            if "429" in err or "Sign in to confirm" in err or "bot" in err.lower():
                wait = 20 * (attempt + 1)
                print(f"  [{vid}] throttled, waiting {wait}s (try {attempt+1})", flush=True)
                time.sleep(wait)
                continue
            if not out:
                print(f"  [{vid}] empty output: {err[-200:]}", flush=True)
                time.sleep(10)
                continue
            return out
        except subprocess.TimeoutExpired:
            print(f"  [{vid}] timeout, retrying", flush=True)
            time.sleep(15)
    return f"{vid}\tFAILED\tNA\tNA\tNA\tNA"

results = []
for n, vid in enumerate(IDS, 1):
    print(f"[{n}/{len(IDS)}] {vid}", flush=True)
    results.append(fetch(vid))
    if n < len(IDS):
        time.sleep(8)

with open(OUT, "w") as f:
    for r in results:
        f.write(r + "\n")
print(f"wrote {OUT}")
