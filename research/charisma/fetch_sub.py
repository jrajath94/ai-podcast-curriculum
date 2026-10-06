#!/usr/bin/env python3
"""Fetch English captions for a YouTube video and save as clean plain text.
Same cleaning as podcast-deep-dive/bin/fetch_transcript.py, but adds
--no-check-certificate + android player client for this VM.
Usage: fetch_sub.py <video_url_or_id> <output_txt>
"""
import os, re, sys, subprocess, tempfile, glob, html

BASE = ["python3", "-m", "yt_dlp", "--skip-download", "--no-check-certificate",
        "--extractor-args", "youtube:player_client=android"]

def run(cmd, **kw):
    return subprocess.run(cmd, capture_output=True, text=True, **kw)

def main():
    if len(sys.argv) != 3:
        print("usage: fetch_sub.py <video_url_or_id> <output_txt>", file=sys.stderr)
        sys.exit(2)
    src, out = sys.argv[1], sys.argv[2]
    if not src.startswith("http"):
        src = f"https://www.youtube.com/watch?v={src}"
    tmp = tempfile.mkdtemp(prefix="tr_")
    ok = None
    err_last = ""
    for args in (
        ["--write-subs", "--sub-langs", "en.*"],
        ["--write-auto-subs", "--sub-langs", "en.*"],
    ):
        r = run(BASE + args + ["--sub-format", "srt",
                "-o", os.path.join(tmp, "%(id)s.%(ext)s"), src], timeout=240)
        files = glob.glob(os.path.join(tmp, "*.srt")) + glob.glob(os.path.join(tmp, "*.vtt"))
        err_last = (r.stderr or "")[-300:]
        if files:
            ok = files[0]
            break
    if not ok:
        print(f"NO_CAPTIONS for {src} :: {err_last}", file=sys.stderr)
        sys.exit(1)
    raw = open(ok, encoding="utf-8", errors="replace").read()
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
