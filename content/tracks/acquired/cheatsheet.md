---
page_id: acquired-cheatsheet
course_slug: acquired
course_name: "Acquired"
course_order: 5
order: 98
nav: "Cheatsheet"
title: "Acquired: Cheatsheet"
summary: "Every key fact, number, name, and decision from the Acquired track on one dense page."
date: 2026-10-06
instructor: "Ben Gilbert and David Rosenthal"
offering: "Acquired"
---

## NVIDIA trilogy (ep01, ep08, ep09, ep10, ep11)

- Founded 1993 (Denny's); seed $2M at $6M post (Sequoia, Sutter Hill); IPO 1999 at $600M (100x).
- Two near-deaths: quadrilateral bet (Sega walked 1996); RIVA 128 in 9 months (emulator: 1 frame/30 sec), 1M units in 4 months (1997).
- Six-month ship cadence vs competitors' 18–24 months; 90 competitors → 2 (NVIDIA, ATI).
- GeForce 256 (1999): 5x performance; coined "GPU". Xbox deal: $500M/yr + $200M advance; only 3 consoles ever (Xbox, PS3, Switch).
- Revenue: $158M → $375M → $735M → $1.4B (FY99–CY01); fastest semiconductor to $1B; then flat ~$2B; $2.8B in 2005.
- Gross margin 29% (2004) → 66%+ → 70–72% (2023); pre-CUDA commoditized era 24%.
- CUDA: launched 2006; 1,100 employees with CUDA in title; "if we don't build it, they can't come."
- Stock: ~$20B peak mid-2007 → −80% (2008) → −50% (2011) → back to $20B only in 2016; under $5/share 2012–2015; ~$220 at Apr 2022 recording; crashed under $300B; over $1T by Aug 2023.
- AlexNet 2012: ~15% error vs ~25% (ImageNet, Fei-Fei Li); the big bang; NVIDIA/CUDA right there.
- Andreessen 2016: "every single one effectively comes in building on NVIDIA's platforms."
- Crypto 2018: third application of same chips (parallel guess-and-check); crypto winter → revenue declined.
- Mellanox acquired 2020, ~$7B (data-center networking; Megatron 8.3B params taught the bandwidth lesson, Aug 2019).
- Data center: ~$3B → $10.5B/yr (3X in 2 yrs), dethroning gaming (~$6B); Q2 FY24: $10.3B of $13.5B total (+141% QoQ, +171% YoY).
- H100: $40,000; 250B transistors; ~20,000 cores (18,500 CUDA + 640 tensor + 80 SMs); 70 lbs; 9x A100 training; 700W TDP; 80GB HBM3 @ 3.35 TB/s; NVLink 900 GB/s (vs PCIe 128 GB/s); FP8 3,958 TFLOPS.
- DGX H100: 8x H100, 640GB HBM3, 32 PFLOPS FP8, 10.2 kW max, 6x 3.3kW PSUs (4+2), 8U, 287.6 lbs, 8x ConnectX-7 400Gb/s InfiniBand; box from $500K (8×$40K=$320K → ~$180K integration margin); SuperPOD: 256 racks, hundreds of $M; DGX Cloud $37K/mo.
- CUDA developers: 100K (4 yrs) → 1M (2016) → 2M (2018) → 3M (2022) → 4M (May 2023); ~10,000 person-years invested; 500M CUDA-capable GPUs.
- CoWoS: 10–15% of TSMC capacity, years to add; NVIDIA reserved most.
- China: 25% of revenue; Sept 2022 export controls → A800 detuned variants.
- Employees 26,000 (vs Microsoft 220,000); CapEx ~$1B/yr (vs TSMC $30B).
- Bear cases: margin prize invites attack; training→inference shift. Bull: replication needs a decade.
- Jensen: "my will to survive exceeds almost everybody else's will to kill me"; 40+ direct reports; "the mission is the boss"; dislikes the word "vision."
- Fermi anchor: 1,000-GPU cluster = 125 DGX × $500K = $62.5M, ~1.7 MW with overhead.

## TSMC (ep02)

- Morris Chang; pure-play foundry (never competes with customers); founded 1987.
- 1997: Jensen's letter betting TSMC could build NVIDIA's chips.
- 2009 40nm crisis: $100M pizza dinner; 28nm bet (8% R&D, $6B capex); Apple 20nm detour.
- Learning curve = moat; builds everyone's chips including NVIDIA's.

## Meta (ep03, ep07)

- Zuckerberg: learn-faster loop; nine death waves; invention vs discovery; HTML5 rewrite; open-source logic (commoditize complements).
- Growth team invented growth as a science; Beacon; mobile 5-reasons crisis; IPO.
- 2012 acquisition email: "buying time" (Instagram); Town Square → living room; FAIR; Cambridge Analytica; ATT; Reality Labs $60B hedge math.

## Google (ep04, ep05)

- Part I: PageRank as citations; AdWords auction; AOL $100M bet; toolbar distribution; IPO; 7-point playbook.
- Part III: innovator's dilemma; transformer origin ("Attention Is All You Need," 2017); TPU; talent exodus; OpenAI/Microsoft; Waymo; Gemini; value-capture problem; 7-powers moat analysis.

## Microsoft (ep06)

- IBM deal ($775K testing/consulting + $45K DOS + $310K languages, components as stated; do not sum to the episode's own ~$430K total [uncertain]); QDOS $75K; clones; Windows hedge vs OS/2; kept 49%; seven powers.

## Cross-track patterns

- Picks and shovels: get paid by every prospector (NVIDIA/CUDA, TSMC/foundry, AdWords/auction).
- Bet-the-company moments: RIVA 128, CUDA, HTML5 rewrite, AdWords.
- Preparation > prediction: CUDA built with no market; AI arrived.
- Narratives lag technology ~a decade (NVIDIA took until 2016 to recover 2007 peak).
- Scale-up (NVLink 900 GB/s) vs scale-out (InfiniBand 400 Gb/s): two networks, two jobs.
- Read bandwidth before FLOPS; power (watts) is the binding constraint; the cluster is the computer.
