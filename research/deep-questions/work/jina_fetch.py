#!/usr/bin/env python3
"""Fetch view counts + upload dates via Jina Reader (YouTube bot-checks yt-dlp).
Idempotent: skips IDs already in jina_meta.tsv. Polite 3s spacing."""
import subprocess, re, time, os, sys

WORK = os.path.expanduser('~/workspace/ai-podcast-curriculum/research/deep-questions/work')
CAND = os.path.join(WORK, 'dq_candidates.txt')
TSV = os.path.join(WORK, 'jina_meta.tsv')
LOG = os.path.join(WORK, 'jina_fetch.log')

MONTHS = {'Jan':'01','Feb':'02','Mar':'03','Apr':'04','May':'05','Jun':'06',
          'Jul':'07','Aug':'08','Sep':'09','Oct':'10','Nov':'11','Dec':'12'}

def parse(text):
    title, views, date_iso = None, None, None
    m = re.search(r'^Title:\s*(.+)$', text, re.M)
    if m: title = m.group(1).strip()
    # description block: " 26,431 views • Aug 17, 2026 •"
    m = re.search(r'([\d,]+)\s+views\s+•\s+([A-Z][a-z]{2})\s+(\d{1,2}),\s+(\d{4})', text)
    if m:
        views = int(m.group(1).replace(',', ''))
        mon = MONTHS.get(m.group(2))
        if mon: date_iso = f"{m.group(4)}{mon}{int(m.group(3)):02d}"
    else:
        # compact form: "1.2M views" / "345K views"
        m = re.search(r'([\d.]+)([KM])\s+views', text)
        if m:
            mult = 1000000 if m.group(2) == 'M' else 1000
            views = int(float(m.group(1)) * mult)
            views = -views  # mark as approximate (negative)
    return title, views, date_iso

with open(CAND) as f:
    all_ids = [l.strip() for l in f if l.strip()]
done = set()
if os.path.exists(TSV):
    with open(TSV) as f:
        for line in f:
            p = line.rstrip('\n').split('\t')
            if p: done.add(p[0])
todo = [v for v in all_ids if v not in done]
print(f"total={len(all_ids)} done={len(done)} todo={len(todo)}", flush=True)

log = open(LOG, 'a')
out = open(TSV, 'a')
fails = 0
for i, vid in enumerate(todo):
    url = f"https://r.jina.ai/https://www.youtube.com/watch?v={vid}"
    try:
        r = subprocess.run(['curl', '-s', '--max-time', '45', url],
                           capture_output=True, text=True, timeout=60)
        text = r.stdout or ''
        if 'rate limit' in text.lower() or 'too many requests' in text.lower():
            log.write(f"{vid}\tJINA_RATE_LIMIT\n"); log.flush()
            print(f"[{i+1}/{len(todo)}] {vid} RATE LIMITED, backing off 60s", flush=True)
            time.sleep(60); fails += 1
            if fails > 5:
                print("too many rate limits, stopping", flush=True); break
            continue
        title, views, date_iso = parse(text)
        if views is None:
            log.write(f"{vid}\tPARSE_FAIL len={len(text)}\n"); log.flush()
            print(f"[{i+1}/{len(todo)}] {vid} parse fail", flush=True)
        else:
            out.write(f"{vid}\t{title or ''}\t{views}\t{date_iso or ''}\n"); out.flush()
    except Exception as e:
        log.write(f"{vid}\tEXC {e}\n"); log.flush()
    time.sleep(3)
out.close(); log.close()
print("finished", flush=True)
