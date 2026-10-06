import subprocess, re, time

WORK = '/home/hatch/workspace/ai-podcast-curriculum/research/conversations-with-tyler/_work'
missing = [u.split('v=')[1] for u in open(WORK + '/missing.txt').read().split()]
out = open(WORK + '/jina_views.txt', 'w')
for vid in missing:
    ok = False
    for a in range(2):
        try:
            r = subprocess.run(
                ['curl', '-s', '-m', '45',
                 f'https://r.jina.ai/https://www.youtube.com/watch?v={vid}'],
                capture_output=True, text=True, timeout=70)
            m = re.findall(r'([\d,]+) views', r.stdout)
            if m:
                out.write(vid + ' ' + m[0].replace(',', '') + '\n')
                out.flush()
                ok = True
                break
        except Exception:
            pass
        time.sleep(3)
    if not ok:
        out.write(vid + ' NA\n')
        out.flush()
    print('did', vid, 'ok' if ok else 'NA', flush=True)
out.close()
print('JINA-DONE', flush=True)
