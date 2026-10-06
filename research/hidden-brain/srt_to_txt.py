#!/usr/bin/env python3
"""Convert Hidden Brain .srt subtitle files to plain-text transcripts.
Strips timestamps/indices/tags, dedupes repeated caption lines, joins into paragraphs.
Prefers en-orig (manual captions) over en (auto) when both exist.
Usage: python3 srt_to_txt.py <transcripts_dir>   (reads *.srt, writes <video_id>.txt)
"""
import os, re, sys, glob

def srt_to_text(path):
    with open(path, encoding="utf-8", errors="replace") as f:
        raw = f.read()
    blocks = re.split(r"\n\s*\n", raw.strip())
    lines = []
    for b in blocks:
        b = b.strip()
        if not b:
            continue
        blines = b.splitlines()
        # drop numeric index line and timestamp line
        content = [l for l in blines if not re.match(r"^\d+$", l.strip())
                   and not re.match(r"^\d{2}:\d{2}:\d{2}", l.strip())]
        text = " ".join(content).strip()
        text = re.sub(r"<[^>]+>", "", text)          # strip <i> etc
        text = re.sub(r"\[.*?\]", "", text)          # strip [Music]
        text = re.sub(r"\s+", " ", text).strip()
        if text:
            lines.append(text)
    # dedupe consecutive duplicates (caption overlap)
    dedup = []
    for l in lines:
        if not dedup or dedup[-1] != l:
            dedup.append(l)
    return "\n".join(dedup)

def main():
    d = sys.argv[1]
    done = []
    vids = sorted({os.path.basename(p).split(".")[0]
                   for p in glob.glob(os.path.join(d, "*.srt"))})
    for vid in vids:
        orig = os.path.join(d, vid + ".en-orig.srt")
        auto = os.path.join(d, vid + ".en.srt")
        src = orig if os.path.exists(orig) else auto
        if not os.path.exists(src):
            continue
        text = srt_to_text(src)
        out = os.path.join(d, vid + ".txt")
        with open(out, "w", encoding="utf-8") as f:
            f.write(text + "\n")
        words = len(text.split())
        done.append((vid, os.path.basename(src), words))
        print(f"{vid}: {words} words from {os.path.basename(src)}")
    print(f"CONVERTED {len(done)}")

if __name__ == "__main__":
    main()
