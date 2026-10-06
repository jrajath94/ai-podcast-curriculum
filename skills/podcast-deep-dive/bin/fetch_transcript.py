#!/usr/bin/env python3
"""Fetch English captions for a YouTube video and save as clean plain text.
Usage: fetch_transcript.py <video_url_or_id> <output_txt>
Requires: yt-dlp (pip install yt-dlp). Tries manual subs first, then auto-subs.
"""
import os, re, sys, subprocess, tempfile, glob, html

def run(cmd, **kw):
    return subprocess.run(cmd, capture_output=True, text=True, **kw)

def main():
    if len(sys.argv) != 3:
        print("usage: fetch_transcript.py <video_url_or_id> <output_txt>", file=sys.stderr)
        sys.exit(2)
    src, out = sys.argv[1], sys.argv[2]
    if not src.startswith("http"):
        src = f"https://www.youtube.com/watch?v={src}"
    tmp = tempfile.mkdtemp(prefix="tr_")
    ok = False
    for args in (
        ["--write-subs", "--sub-langs", "en.*"],
        ["--write-auto-subs", "--sub-langs", "en.*"],
    ):
        r = run(["python3", "-m", "yt_dlp", "--skip-download"] + args +
                ["--sub-format", "srt", "-o", os.path.join(tmp, "%(id)s.%(ext)s"), src])
        files = glob.glob(os.path.join(tmp, "*.srt")) + glob.glob(os.path.join(tmp, "*.vtt"))
        if files:
            ok = files[0]
            break
    if not ok:
        print(f"NO_CAPTIONS for {src}", file=sys.stderr)
        sys.exit(1)
    raw = open(ok, encoding="utf-8", errors="replace").read()
    # strip timestamps, tags, duplicate lines; keep order
    lines, seen = [], set()
    for ln in raw.splitlines():
        ln = ln.strip()
        if not ln or re.match(r"^\d+$", ln): continue
        if re.match(r"^\d{2}:\d{2}:\d{2}", ln): continue
        if "-->" in ln: continue
        ln = re.sub(r"<[^>]+>", "", ln)
        ln = html.unescape(ln).strip()
        if ln and ln not in seen:
            seen.add(ln); lines.append(ln)
    os.makedirs(os.path.dirname(os.path.abspath(out)), exist_ok=True)
    open(out, "w", encoding="utf-8").write("\n".join(lines) + "\n")
    print(f"WROTE {out} ({len(lines)} lines)")

if __name__ == "__main__":
    main()
