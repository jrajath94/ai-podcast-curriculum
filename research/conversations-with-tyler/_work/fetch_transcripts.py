"""Fetch official transcripts from conversationswithtyler.com episode pages.
Writes plain-text transcripts to transcripts/<video_id>.txt"""
import re, html, subprocess, os, sys, time

WORK = '/home/hatch/workspace/ai-podcast-curriculum/research/conversations-with-tyler/_work'
TDIR = '/home/hatch/workspace/ai-podcast-curriculum/research/conversations-with-tyler/transcripts'
os.makedirs(TDIR, exist_ok=True)

# (video_id, slug)
EPS = [
    ('ehlhrqSWPbo', 'malcolm-gladwell'),
    ('VSRuncwwJyQ', 'camille-paglia'),
    ('XCWvAZ0eknY', 'stephen-kotkin'),
    ('vfbndRTlsg4', 'peter-thiel-political-theology'),
    ('i_yJTCDU4uE', 'peter-thiel'),
    ('KQkK8ThNsOY', 'jhumpa-lahiri'),
    ('CVaWR8ISEd4', 'steven-pinker'),
    ('b_6vYwCkIpc', 'david-deutsch'),
    ('rOYjgXY-Ts4', 'any-austin'),
    ('v7hEF8CS79U', 'niall-ferguson'),
]

def extract(html_text):
    i = html_text.find('Read the full transcript')
    if i < 0:
        return None, 'no transcript marker'
    tail = html_text[i:]
    end = tail.find('</main>')
    if end < 0:
        return None, 'no </main>'
    seg = tail[:end]
    seg = seg[:seg.rfind('</p>') + 4]
    paras = []
    for ln in seg.split('\\n'):
        for m in re.finditer(r'<p[^>]*>(.*?)</p>', ln):
            t = re.sub(r'<[^>]+>', '', m.group(1))
            t = t.replace('\\"', '"').replace("\\'", "'").replace('\\/', '/')
            t = html.unescape(t).strip()
            if t:
                paras.append(t)
    # drop sponsor line (first para) if it matches
    if paras and 'sponsoring this transcript' in paras[0]:
        paras = paras[1:]
    return '\n\n'.join(paras), None

for vid, slug in EPS:
    url = f'https://conversationswithtyler.com/episodes/{slug}/'
    dest = os.path.join(TDIR, vid + '.txt')
    if os.path.exists(dest) and os.path.getsize(dest) > 5000:
        print(f'{vid} exists, skip', flush=True)
        continue
    ok = False
    for a in range(3):
        r = subprocess.run(['curl', '-s', '-m', '60', url],
                           capture_output=True, text=True, timeout=90)
        if len(r.stdout) > 50000:
            txt, err = extract(r.stdout)
            if txt and len(txt) > 5000:
                open(dest, 'w').write(txt)
                print(f'{vid} OK {len(txt)} chars', flush=True)
                ok = True
                break
            else:
                print(f'{vid} extract fail: {err}', flush=True)
        time.sleep(4)
    if not ok:
        print(f'{vid} FAILED', flush=True)
    time.sleep(3)
print('DONE', flush=True)
