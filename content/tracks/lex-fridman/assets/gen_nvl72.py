#!/usr/bin/env python3
"""Code-generated lesson plate: NVL72 rack as one logical GPU (ep11).
Visual system: VISUAL_SYSTEM_GENERIC.md. Flat fills only, 8px grid, 2px stroke.
Numbers from the chapter ([Added 2026] ModulEdge explainer): 72 Blackwell GPUs,
9 NVSwitch boards, 36 Grace CPUs, 13.5 TB HBM3e, ~130 PFLOPS FP4, 120-132 kW,
2 L/s direct-to-chip liquid cooling, ~$3-3.4M/rack.
"""
import xml.etree.ElementTree as ET

W, H = 960, 760
BG, INK, MUTED, LINE, PANEL = "#F7F4EE", "#1B2838", "#5C6B7A", "#D9D3C7", "#FFFDF8"
GREEN_DEV, YELLOW_CTL, BLUE_STORE, GRAY_CHIP, TEAL = "#D9E8D3", "#F6E7A8", "#E7F1F8", "#E6E2DA", "#1F7A72"
FONT = "Inter, 'Source Sans 3', 'IBM Plex Sans', sans-serif"

def el(tag, **a):
    e = ET.Element(tag)
    for k, v in a.items():
        e.set(k.replace("_", "-"), str(v))
    return e

def text(parent, x, y, s, size=16, weight=500, fill=INK, anchor="start"):
    t = el("text", x=x, y=y, font_family=FONT, font_size=size,
           font_weight=weight, fill=fill, text_anchor=anchor)
    t.text = s
    parent.append(t)
    return t

svg = el("svg", xmlns="http://www.w3.org/2000/svg", width=W, height=H,
         viewBox=f"0 0 {W} {H}", role="img")
svg.append(el("rect", x=0, y=0, width=W, height=H, fill=BG))
title = el("title"); title.text = "NVL72 rack: 72 GPUs acting as one logical GPU"
svg.append(title)

# Title + claim line
text(svg, 32, 48, "The NVL72 rack: 72 GPUs acting as one logical GPU", size=32, weight=600)
text(svg, 32, 80, "NVLink 5.0 fabric plus 9 NVSwitch boards fuse 72 Blackwell GPUs into one machine.",
     size=16, weight=450, fill=MUTED)

PY, PH = 112, 560          # panel top, height
LX, LW = 32, 400           # left panel x, width
RX, RW = 528, 400          # right panel x, width

def panel(x, heading):
    svg.append(el("rect", x=x, y=PY, width=LW, height=PH, rx=12,
                  fill=PANEL, stroke=LINE, stroke_width=2))
    text(svg, x + 16, PY + 32, heading, size=16, weight=600)

# ---- LEFT: before (72 separate GPUs) ----
panel(LX, "Before: 72 separate GPUs")
gx, gy = LX + 16, PY + 56
cols, rows, pw, ph, gap = 8, 9, 32, 16, 8
for r in range(rows):
    for c in range(cols):
        svg.append(el("rect", x=gx + c * (pw + gap), y=gy + r * (ph + gap),
                      width=pw, height=ph, rx=999, fill=PANEL,
                      stroke=INK, stroke_width=2))
text(svg, LX + 16, gy + rows * (ph + gap) + 32,
     "72 separate GPUs, no shared memory", size=14, weight=500, fill=MUTED)
# count box: GPU power alone (72 x 1000-1200 W = 72-86 kW, computed)
svg.append(el("rect", x=LX + 16, y=gy + rows * (ph + gap) + 48,
              width=LW - 32, height=56, rx=8, fill=BLUE_STORE,
              stroke=LINE, stroke_width=2))
text(svg, LX + 32, gy + rows * (ph + gap) + 72,
     "72-86 kW in GPUs alone", size=15, weight=600)
text(svg, LX + 32, gy + rows * (ph + gap) + 92,
     "72 x 1,000-1,200 W per GPU (computed)", size=13, weight=450, fill=MUTED)

# ---- CENTER: the one rule ----
ax0, ax1, ay = LX + LW, RX, PY + 280
svg.append(el("line", x1=ax0, y1=ay, x2=ax1 - 8, y2=ay, stroke=INK, stroke_width=2))
svg.append(el("polygon", points=f"{ax1 - 8},{ay - 7} {ax1 - 8},{ay + 7} {ax1},{ay}",
              fill=INK))
text(svg, (ax0 + ax1) / 2, ay - 12, "NVLink 5.0", size=13, weight=500, anchor="middle")

# ---- RIGHT: after (one rack-computer) ----
panel(RX, "After: one rack, one logical GPU")
ix = RX + 16
yy = PY + 56

text(svg, ix, yy, "9 NVSwitch boards (non-blocking fabric)", size=14, weight=500, fill=MUTED)
yy += 16
sw, sh, sg = 32, 24, 8
for i in range(9):
    svg.append(el("rect", x=ix + i * (sw + sg), y=yy, width=sw, height=sh, rx=12,
                  fill=YELLOW_CTL, stroke=INK, stroke_width=2))
# explicit grid-aligned anchors (all multiples of 8)
text(svg, ix, 224, "72 Blackwell GPUs (18 trays x 4)", size=14, weight=500, fill=MUTED)
gw, gh, gg, gcols, grows = 24, 16, 8, 9, 8
for r in range(grows):
    for c in range(gcols):
        svg.append(el("rect", x=ix + c * (gw + gg), y=240 + r * (gh + gg),
                      width=gw, height=gh, rx=999, fill=GREEN_DEV,
                      stroke=INK, stroke_width=2))
text(svg, ix, 448, "36 Grace CPUs", size=14, weight=500, fill=MUTED)
cw, cg, ccols, crows = 16, 8, 12, 3
for r in range(crows):
    for c in range(ccols):
        svg.append(el("rect", x=ix + c * (cw + cg), y=464 + r * (cw + cg),
                      width=cw, height=cw, rx=8, fill=GRAY_CHIP,
                      stroke=INK, stroke_width=2))
# cooling strip (store: blue)
svg.append(el("rect", x=ix, y=552, width=RW - 32, height=40, rx=12,
              fill=BLUE_STORE, stroke=INK, stroke_width=2))
text(svg, ix + 16, 552 + 25, "Direct-to-chip liquid cooling (~2 L/s). Mandatory.",
     size=14, weight=500)
yy = 608
# count boxes: unified memory, compute, power
boxes = [("13.5 TB HBM3e", "unified memory"), ("~130 PFLOPS FP4", "one machine"),
         ("120-132 kW", "16-17x avg rack")]
bw = (RW - 32 - 2 * 16) / 3
for i, (big, small) in enumerate(boxes):
    bx = ix + i * (bw + 16)
    svg.append(el("rect", x=bx, y=yy, width=bw, height=56, rx=8,
                  fill=BLUE_STORE, stroke=LINE, stroke_width=2))
    text(svg, bx + bw / 2, yy + 24, big, size=14, weight=600, anchor="middle")
    text(svg, bx + bw / 2, yy + 43, small, size=12, weight=450, fill=MUTED,
         anchor="middle")

# ---- Footer claim + source ----
text(svg, 32, PY + PH + 32,
     "At this scale the rack is the computer. The data center is racks wired together.",
     size=16, weight=600)
text(svg, 32, PY + PH + 56,
     "Source: original plate. Numbers from the chapter ([Added 2026] ModulEdge explainer).",
     size=13, weight=450, fill=MUTED)

out = "/home/hatch/workspace/ai-podcast-curriculum/content/tracks/lex-fridman/assets/nvl72-rack.svg"
ET.ElementTree(svg).write(out, encoding="unicode", xml_declaration=True)
print("wrote", out)
