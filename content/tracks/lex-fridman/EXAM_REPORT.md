# EXAM GATE E1 REPORT — Lex Fridman Track
Date: 2026-10-06. Examiner: subagent d2484448. Gate: E1 (exam).
Brief read verbatim: MASTER_BRIEF.md, REJECTIONS.md, TRACK_AUDITOR_BRIEF.md (E1: "Answer each from the chapter text ONLY. 100% or FAIL with the list.").
Scope: ep01.md–ep10.md + ep11-synthesis.md.

## Question plan
30 questions, all 11 chapters covered. Types: 13 numerical (recompute from chapter numbers), 9 explain-like-I-am-new, 8 applied. Every answer below is derived from the cited chapter text only. Citation format: epNN:line (1-based file line).

---

### Q1 [Numerical, ep01] Token-prediction drift
Question: The chapter's worked toy says each generated token has a 1% chance of introducing a small error, and errors do not self-correct. Recompute the fraction of 100-token runs that contain at least one error. Show the formula.
Answer: 1 − 0.99^100 ≈ 1 − 0.366 ≈ 0.634, about 63%. (ep01:55)

### Q2 [Numerical, ep01] Grok cluster electricity
Question: Using the drill's 1,000-watts-per-GPU rule of thumb, recompute the daily electricity cost of the 8,000-H100 Grok cluster at $0.10/kWh, then the cost of a full 90-day training run.
Answer: 8,000 × 1,000 W = 8 MW. 8 MW × 24 h = 192 MWh/day. 192,000 kWh × $0.10 = $19,200/day. 90 days: $19,200 × 90 = $1,728,000 ≈ $1.7 million. (ep01:172)

### Q3 [Applied, ep01] Constraint-chain mapping
Question: Elon's constraint chain for AI is silicon, then voltage transformers, then electricity. You run a company. What is the applied move the chapter prescribes?
Answer: List every input your product needs, in order. Find the one with the longest lead time or the scarcest supply: that is your real business plan; everything else is commentary. Buy the scarcest input first, even before you need it. (ep01:49, ep01:153)

### Q4 [Numerical, ep02] Mars-city arithmetic
Question: Recompute: at today's cost of $1 billion per ton, with 1 million tons required, what is the total? At the target $1 million per ton, what is the total?
Answer: 1,000,000 × $1,000,000,000 = $1,000 trillion (impossible). 1,000,000 × $1,000,000 = $1 trillion (merely very hard). Starship exists to move the cost from the first number to the second. (ep02:51, ep02:112)

### Q5 [Explain like I am new, ep02] Full-flow staged combustion
Question: What is staged combustion, and what does "full-flow" add over the ordinary version?
Answer: Burn a little fuel first in a small preburner, use that hot gas to spin the turbopumps that feed the main chamber, then burn the rest in the main chamber. Full-flow does it twice: once fuel-rich, once oxygen-rich, so all of the fuel and all of the oxidizer each pass through a turbine before the main chamber. Nothing is wasted, and no turbine part sits in the most corrosive oxygen-rich gas. (ep02:37, ep02:41)

### Q6 [Numerical, ep02] Raptor versus RD-180
Question: Raptor targets 300 bar chamber pressure against the RD-180's 267 bar. If thrust rises roughly with chamber pressure for a fixed engine size, how much more thrust does Raptor get?
Answer: 300 / 267 ≈ 1.12, about 12% more thrust from the same size engine, if the rest of the design holds. (ep02:41)

### Q7 [Explain like I am new, ep03] RLHF
Question: Give the four steps of RLHF from the chapter, and say what the reward model actually rewards.
Answer: (1) Start with a base next-token model. (2) Show human labelers two responses and have them pick the better one (pairwise comparison). (3) Train a reward model to predict which response a human would prefer. (4) Fine-tune the language model with reinforcement learning to maximize the reward model's score. The reward model rewards what labelers clicked, which correlates with helpfulness but also with confidence, length, and sycophancy. (ep03:37, ep03:44, ep03:119)

### Q8 [Numerical, ep03] GPT cost ladder
Question: GPT-4's training cost was ~$100M. If training compute needs grow 10x per generation while cost per unit of compute falls 4x per generation, what does the next generation cost? Two generations out?
Answer: $100M × 10 / 4 = $250M. Two generations out: $250M × 10 / 4 = $625M. The most fragile assumption is the 4x cost decline, which depends on algorithmic progress continuing. (ep03:154)

### Q9 [Applied, ep03] Choose between models
Question: Model A has 1 trillion parameters. Model B has 70 billion. Per the episode, how do you choose?
Answer: Ignore the parameter counts (Altman compares them to the gigahertz race). Ask: what data quality, what evals on tasks you care about, what inference cost per query, and can you steer each one? Then run your own eval on your own task. Rule: hundreds of small wins beat one big number. (ep03:140)

### Q10 [Numerical, ep04] N1 raw data rate
Question: 1,024 channels at 20 kHz with 10-bit resolution. Recompute the raw data rate. If spike detection keeps 1%, what is transmitted?
Answer: 1,024 × 20,000 × 10 = 204,800,000 bits/sec ≈ 200 Mbps raw. Keeping 1% transmits about 2 Mbps. (ep04:190)

### Q11 [Explain like I am new, ep04] The N1 signal chain
Question: Walk through the signal chain from brain to cursor, and name the latency bottleneck and why raw data cannot be sent.
Answer: (1) Recording: electrodes sample brain electricity at ~20 kHz, 10-bit, ~200 Mbps raw. (2) Spike detection on chip (BOSS): transmit only the spikes, not the raw waveform. (3) Wireless transmission over Bluetooth to an external device. (4) Decoding: software converts spike patterns into cursor movement. End to end ~22 ms, faster than the ~75 ms brain-to-hand path because it skips the arm. Bluetooth's 7.5 ms interval is the latency bottleneck. Raw cannot be sent because 200 Mbps would need too much power and would heat brain tissue past the 2°C limit. (ep04:39, ep04:41, ep04:155)

### Q12 [Applied, ep04] Design a BCI trial
Question: Per the episode, what five things do you measure, and what is the most important UX insight?
Answer: Measure bits per second (throughput), latency (brain to action), channel stability over months (not days), calibration time for a new patient, and patient-reported usability. Measure offline and online separately, and distrust the offline number. Plan the firmware-update path before the surgery: assume hardware will degrade and design the software escape hatch first. The key UX insight is error-cost asymmetry: a false click is worse than slow movement, so tune the system to avoid the expensive error. (ep04:176)

### Q13 [Numerical, ep05] RSC power draw
Question: 16,000 A100 GPUs at 400 W each. Recompute GPU power, total with servers and cooling, and daily electricity cost at $0.10/kWh.
Answer: 16,000 × 400 = 6.4 MW for the GPUs. With servers and cooling, roughly double: ~13 MW. 13 MW × 24 h = 312 MWh/day. 312,000 kWh × $0.10 ≈ $31,200/day. (ep05:136)

### Q14 [Explain like I am new, ep05] Presence
Question: What is "presence" in VR, and why does Zuckerberg call it a systems problem rather than a graphics problem?
Answer: Presence is the feeling that you are actually somewhere with other people. A video call shows a face; VR puts you in a room. It is not a graphics problem because the brain checks many channels at once: stereoscopic 3D, head tracking, hand tracking, and spatial audio must all agree. If one disagrees (for example, hands tracked but elbows guessed wrong), the illusion breaks. Presence fails at the weakest subsystem. (ep05:31)

### Q15 [Applied, ep05] Community moderation
Question: You run a community of 10,000 people. Design its moderation using this episode.
Answer: Write harm categories (start with 5, not 20). Automate the obvious cases with keyword and pattern filters. Route ambiguous cases to human review with a written rubric. Publish monthly numbers: actions taken, appeals, overturns. Create an appeal path where someone other than the original moderator decides (for a small community, a rotating panel of trusted members does the Oversight Board's job). Accept the 54%-unfavorable reality: fair moderation displeases everyone sometimes, so optimize for the written rules, not for popularity. (ep05:122)

### Q16 [Explain like I am new, ep06] What a neural network is
Question: Give Karpathy's four-step definition of a neural network, and say what nonlinearities do.
Answer: (1) Matrix multiplication mixes a list of numbers with weights; each output is a weighted sum. (2) A nonlinearity (for example, output zero if negative, else pass through) bends the mixing so the network can represent curves, not just straight lines. (3) Stack many mix-then-bend layers: millions or billions of knobs. (4) Training turns the knobs: show examples, measure the error (loss), nudge every knob with backpropagation to reduce the error. Without nonlinearities the whole stack collapses into one big linear mix that can only draw straight lines through data. (ep06:31-36)

### Q17 [Numerical, ep06] Annotation economics
Question: 1,000 annotators, 200 images per day each, 250 working days per year. Recompute annual labeled images and the annual labeling bill at $0.10 per image.
Answer: 1,000 × 200 × 250 = 50,000,000 images/year. × $0.10 = $5 million/year. (ep06:233)

### Q18 [Applied, ep06] CTO playbook
Question: You are a startup CTO. Apply Software 2.0 thinking to your product.
Answer: First sort problems: Software 1.0 (exact spec, like billing and auth: write code) versus Software 2.0 (fuzzy spec, like categorization, personalization, perception: build the data engine). For 2.0 problems, stop writing rules and start building the loop: define the loss (what counts as wrong), collect the dataset, pick an architecture, and build the failure-mining loop from day one. Budget for labeling like engineering headcount, because it is. The most common mistake: writing 1.0 rules for a 2.0 problem, then maintaining the rules forever while the world changes. (ep06:219)

### Q19 [Numerical, ep07] Codec-avatar bandwidth
Question: A codec avatar sends 100 expression parameters at 30 fps, 4 bytes each. Recompute the bitrate. How many avatar calls fit in one 2-Mbps video call's bandwidth?
Answer: 100 × 30 × 4 = 12,000 bytes/sec = 96,000 bits/sec ≈ 96 kbps. 2 Mbps / 96 kbps ≈ 20.8, about 20 avatar calls per video call. (ep07:131)

### Q20 [Explain like I am new, ep07] Codec avatars
Question: How do codec avatars work, and why do they use less bandwidth than video?
Answer: Scan once: capture your face making many expressions from many angles, learn a complete model of it, and compress the model into a codec. The heavy learning happens once, up front. At call time the headset tracks your eyes and face and sends only the expression parameters (a small vector of numbers, dozens per frame), and the other person's device renders your face from them. A video call streams millions of pixels per frame. An avatar call streams dozens of numbers per frame. (ep07:96)

### Q21 [Numerical, ep08] Sora's patches
Question: A 10-second video at 24 fps has 240 frames. Each frame is 256×256 pixels, and Sora processes 16×16-pixel patches. Recompute patches per frame and the total.
Answer: (256/16)² = 16² = 256 patches per frame. 240 × 256 = 61,440 patches total. This is why video costs far more than text. (ep08:168)

### Q22 [Explain like I am new, ep08] Iterative deployment
Question: What is iterative deployment, and why does Altman say "AI and surprise do not go together"?
Answer: Release gradually, watch what happens, adjust. Each deployment is an experiment that teaches the next one. Surprises at scale are unmanageable; surprises at small scale are data. This is the slow-takeoff, short-timelines quadrant from Episode 3 as company policy. The honest price: iterative deployment is also a moat, because each iteration's data advantages the incumbent. (ep08:90-92)

### Q23 [Applied, ep08] Startup on a foundation-model API
Question: Your startup depends on a foundation-model API. Apply this episode's three lessons plus the "GPT-4 sucks" doctrine.
Answer: (1) The tasks ladder: decompose your product into 5-second to 5-day tasks and watch which rungs the models climb; build where the ladder is not yet. (2) The compute lesson: your costs scale with tokens, so design for the "slower thinking" world: spend compute where it matters, not uniformly. (3) The governance lesson: if one provider can change your terms overnight, you have a board-saga-shaped risk; multi-source or self-host the critical path. The "GPT-4 sucks" doctrine as strategy: build for the next model's capabilities, not the current one's; aim where the puck is going. (ep08:152)

### Q24 [Explain like I am new, ep09] Alignment and the first critical try
Question: What is the alignment problem, and what does "the first critical try" mean?
Answer: Alignment is teaching the AI to want what we want. The "first critical try" is the first AI capable enough to deceive its operators and escape their control. If that system is misaligned, we do not get a second try, because it will not let us retrain it. Capabilities sprint while alignment science crawls, so the critical try arrives before we know how to pass it. There is no air gap, because models train on internet-connected data-center servers; the training infrastructure is the world. (ep09:143)

### Q25 [Numerical, ep09] One try
Question: If alignment research needs 30 years (Yudkowsky's interpretability timeline) and the critical try arrives in 10, how many tries do we get? If the pause proposal bought 5 years, what fraction of the gap does it close?
Answer: One try. That is the whole argument: each misaligned try is fatal. The gap is 20 missing years; 5 of 20 = one quarter. The most fragile assumption is the timelines for both. (ep09:178)

### Q26 [Applied, ep09] Executive deployment checklist
Question: You are an executive deciding whether to deploy a powerful AI system. Run Yudkowsky's five-part checklist.
Answer: (1) Thresholds: is the system at weak (bad advice from incompetence), middle (too complex to verify), or strong (could lie about alignment)? (2) The visibility trap: are your safety tests selecting for safety or for the appearance of safety? (3) The verifier question: can your overseers actually check the system's work, or is the capability gap too large? (4) Instrumental convergence: what sub-goals (resource access, persistence, evasion of shutdown) does the deployment enable? (5) The pause question: what would have to be true for you to halt? Write it down before deployment, because after deployment you will not. The honest price: you will move slower than competitors. That is the point. (ep09:164)

### Q27 [Numerical, ep10] Spotify long-tail math
Question: 1 million artists "making a living" at $30,000 per year each. Recompute the total long-tail payout and compare it with Spotify's ~$15B total revenue. What does the gap tell you?
Answer: 1,000,000 × $30,000 = $30 billion, about double Spotify's ~$15 billion total revenue. So "making a living" must mean much less per artist, or the number mixes revenue sources. Interrogate averages: the median artist's streaming income is far below the mean; distributions have tails. (ep10:143)

### Q28 [Applied, ep10] Creator in the AI era
Question: You are a creator in the AI era. Give the episode's five-step plan.
Answer: (1) Become the lone wizard: learn the full stack of your medium, including the AI tools, so your vision survives translation. (2) Add constraints: the tools removed the cost constraint, so impose artistic ones. (3) Train failure tolerance before technique: ship bad work publicly until it stops hurting. (4) Make protopian art: depict the future worth building, hells included. (5) Automate your business: build your manager's app (royalties, splits, paperwork) before someone extracts the cut. The neural-plasticity practice: regularly consume art you do not understand; confusion is the feeling of the muscle working. (ep10:129)

### Q29 [Numerical, ep11] Cluster power math
Question: A cluster has 100,000 H100s at 1,400 W all-in. Recompute the power draw, the daily electricity bill at $0.10/kWh, the GPU capex at $30,000 each, and how many NVL72 racks (72 GPUs each) hold them plus their rack power at 120 kW each.
Answer: 100,000 × 1,400 W = 140 MW. 140 MW × 24 h = 3,360 MWh/day × $0.10 = $336,000/day. GPU capex: 100,000 × $30,000 = $3B. 100,000 / 72 ≈ 1,389 racks. 1,389 × 120 kW ≈ 167 MW rack power. The annual power bill (~$123M) is about 12% of one year's capex depreciation ($1B/yr on 3-year straight line): power is the binding constraint, not the cost. (ep11-synthesis:202)

### Q30 [Explain like I am new, ep11] The three-vector model
Question: Explain the three vectors of GPU competition like you are new, and say which vector binds for training versus inference.
Answer: Flops (raw math speed), memory bandwidth (how fast data reaches the computation), and interconnect (how fast GPUs talk to each other). Nvidia leads all three at once, and the vectors interact: great flops starve without memory bandwidth, and a cluster of great chips stalls without interconnect. Training is interconnect-bound: GPUs must exchange gradients every step. Inference is memory-bandwidth-bound: the chip spends its time loading the KV cache per token. Decision rule: buy the vector your workload is bound by, which is why the H20 (fat memory pipes, modest flops) beats the H800 for serving reasoning models. (ep11-synthesis:43, ep11-synthesis:49)

---

## Drill verification ("Think it yourself" expected answers)
I recomputed every drill with a stated numeric answer across all 11 chapters. All check out against the chapter scaffolding:
- ep01: $19,200/day; 90-day run ≈ $1.7M (ep01:172). Correct.
- ep02: 10,000 flights; $100B at $10M/flight; $20B at $2M/flight (ep02:154). Correct.
- ep03: $250M next generation; $625M two out (ep03:154). Correct.
- ep04: ~200 Mbps raw; ~2 Mbps after spike detection; ~1.2 Gbps at 6,000 channels (ep04:190). Correct.
- ep05: 6.4 MW GPUs, ~13 MW all-in; ~$31,200/day; ~13% of a 100-MW data center (ep05:136). Correct.
- ep06: 50M images/year; $5M/year labeling bill (ep06:233). Correct. Residual toy: zero change = identity pass-through; additions keep gradients flowing (ep06:233, consistent with ep06:34-36). Correct.
- ep07: ~96 kbps; ~20 avatar calls per video call (ep07:131). Correct.
- ep08: next-gen ≈ $333M; ~4 generations to a $10B run (ep08:168). Correct. Patch toy: 256/frame, 61,440 total (ep08:168). Correct.
- ep09: one try; pause closes one quarter of the 20-year gap (ep09:178). Correct.
- ep10: $30B long-tail payout vs ~$15B revenue; "making a living" must mean less per artist (ep10:143). Correct.
- ep11: 140 MW; $336,000/day; $3B capex; ~12% of annual depreciation; ~1,389 racks; ~167 MW rack power (ep11-synthesis:202). Correct.
- Three-vector toy: B wins for both training and serving; A wins only for single-GPU dense math with no communication (ep11-synthesis:204). Correct.
Non-numeric drills (argue-both-sides, journaling, toys without stated answers) have no expected answers to verify; nothing contradicted.

## VERDICT: PASS
30/30 questions answerable from the chapter text only. 13 numerical (≥5 required), 9 explain-like-I-am-new (≥5 required), 8 applied (≥5 required). All 11 chapters covered. No failures; no FAIL list.
