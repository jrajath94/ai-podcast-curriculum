# EXAM REPORT — AI Podcast Curriculum, Hidden Brain track
# Exam gate E1 (adversarial examiner)
# Date: 2026-10-06
# Examiner: subagent b9df6069 (parent orchestrator)
# Method: read all 7 chapters end to end, then wrote each question and
# answered it from the chapter text ONLY, with chapter:line citations.
# Note: TRACK_AUDITOR_BRIEF.md specifies 20 questions for E1. The assigned
# task explicitly overrides this with 21 (3 per chapter x 7 chapters).
# The task instruction is followed.

## Distribution

| Chapter | Q | Type mix |
|---|---|---|
| ep01 Subtraction Neglect | 1, 2, 3 | numerical, explain-like-new, applied |
| ep02 The Divided Brain | 4, 5, 6 | explain-like-new, mechanism, applied |
| ep03 Resilience | 7, 8, 9 | numerical, mechanism, applied |
| ep04 Courage | 10, 11, 12 | explain-like-new, mechanism, applied |
| ep05 Forgetting | 13, 14, 15 | numerical, explain-like-new, applied |
| ep06 Memorability | 16, 17, 18 | numerical, mechanism, applied |
| ep07 Choking Under Pressure | 19, 20, 21 | numerical, explain-like-new, applied |

Type totals: numerical 5 (Q1, Q7, Q13, Q16, Q19), explain-like-new 5
(Q2, Q4, Q10, Q14, Q20), applied 7 (Q3, Q6, Q9, Q12, Q15, Q18, Q21),
mechanism 4 (Q5, Q8, Q11, Q17).

---

## Chapter ep01 — Subtraction Neglect

### Q1 [numerical]
In the recipe experiment, 2 of 90 volunteers removed an ingredient when
asked to improve a five-ingredient dish. Recompute the add-to-remove ratio
from these numbers. A product team of 90 engineers each proposes one change.
If the bias holds, how many subtractive proposals do you expect?

**Answer:** 90 minus 2 gives 88 volunteers who added. 88 divided by 2 is 44,
so the add-to-remove ratio is 44 to 1. You expect roughly 2 subtractive
proposals and roughly 88 additive ones. This matches the chapter's own
answer sketch for Drill 1.
Citations: ep01:83 (2 of 90 removed, about 2 percent), ep01:85 (hand-worked
ratio 88 to 2, 44 to 1), ep01:287 (Drill 1 answer sketch: expect roughly
88 additive proposals and 2 subtractive ones).

### Q2 [explain like I am new]
Explain subtraction neglect to someone who has never heard of it. What was
the Nature 2021 grid experiment, and what did it rule out?

**Answer:** Subtraction neglect is the automatic impulse to solve a problem
by addition even when the better solution is to take something away. In the
2021 Nature experiments, volunteers saw a digital grid of colored squares
and had to make it symmetrical. They could add squares or remove them, and
both approaches worked. Most people chose to add. The moment subtraction was
pointed out as an option, people took it. This rules out the idea that
subtraction was worse. The defect is that removal simply did not occur to
people as a possibility.
Citations: ep01:33 (definition of subtraction neglect), ep01:66 (Nature
2021 grid experiment, published in Nature in 2021), ep01:242 (Q&A 1 answer:
the defect is not that subtraction is worse, it never occurs to you).

### Q3 [applied]
Your calendar is full and you want to add a gym habit. Walk through the
episode's tools in order, using the chapter's exact decision rule and the
visibility trick.

**Answer:** Do not add the gym to a full calendar; that repeats the
impossible-itinerary mistake of adding to a schedule that is physically
impossible to complete. First, write a stop doing list and apply Klotz's
decision rule: if you will add new things to your day and you are already
at capacity, you must name what you will take away (one meeting, one show,
one scroll session). Second, use the stop-editing cap: limit the gym plan
itself, for example three days, 40 minutes, walk there, modeled on the
10-most-important-comments cap. Third, make the subtraction visible: tell
one person what you cut, so the removal has social evidence, the same
function as Nike's window cut into the Air Max sole. If you cannot find
anything to cut, you are at true capacity, and the honest move is to admit
that adding the gym means failing at something else.
Citations: ep01:169 (stop doing list and the decision rule), ep01:89
(impossible itinerary: 14 hours of activity plus over 2 hours of travel,
participants added anyway), ep01:173 (10-comment cap), ep01:257 (Q&A 6
applied answer), ep01:248 (Nike window reference via the chapter plate
logic: name the removed thing and the gain).

---

## Chapter ep02 — The Divided Brain

### Q4 [explain like I am new]
A friend says "I am a left-brain person, I am logical, not creative." Correct
them using the episode's real division and the bird analogy.

**Answer:** The pop version is wrong: the two halves do not do different
things. They do the same things, but in different ways. The right hemisphere
takes in the whole picture, context, meaning, and tone. The left hemisphere
zooms into details, breaks things into pieces, and executes. Both hemispheres
are involved in doing everything. The bird analogy shows why both are needed
at once: to pick up a seed the bird needs precise, targeted attention on a
detail, but it simultaneously needs the opposite attention, sustained, broad,
and vigilant for predators. Narrow alone means it eats but gets eaten. Wide
alone means it sees danger but starves.
Citations: ep02:24-27 (both halves do the same things in different ways;
scientists found the pop version toxic), ep02:41 (the bird's two attentions),
ep02:45-51 (Figure 1 table: narrow alone = eat but get eaten, wide alone =
see danger but starve).

### Q5 [mechanism]
Walk through the moral experiment. What exactly changed when researchers
temporarily disabled the right temporal parietal junction, and what does
that change prove about what the left hemisphere alone can and cannot do?

**Answer:** Two coffee scenarios. One: a woman puts what she thinks is sugar
in her friend's cup, but it is poison, and the friend dies. Two: a woman
puts what she thinks is poison in the coffee of someone she hates, but it is
sugar, and the person lives. With the right TPJ working, people say the
second is morally worse because intent is what matters: she tried to kill
someone. When researchers temporarily disabled the right TPJ with a painless
procedure, people gave bizarre, entirely utilitarian answers: the first
scenario is worse because someone is dead on the floor, which justifies the
harsher punishment. The change proves that judging intent requires seeing
the bigger picture (what she believed, what she meant), and that the left
hemisphere working alone cannot do it: it can only count outcomes, not read
intentions.
Citations: ep02:91 (the two coffee scenarios, intent is what matters),
ep02:93 (rTPJ disabled, utilitarian answers, someone dead on the floor),
ep02:95-101 (Figure 2 table: rTPJ intact judges intent, rTPJ disabled judges
outcome), ep02:184 (Q&A 2 answer: the left hemisphere alone can only count
outcomes).

### Q6 [applied]
You are debugging a production outage and the whole team is deep in log
lines. The episode prescribes a specific loop. Name it, apply it step by
step, and state the failure mode of skipping the last step.

**Answer:** The team is stuck in emissary mode: parts, details, log lines.
Run the whole-part-whole loop. Right hemisphere first: what is the whole
system doing, what changed at the highest level, what does the failure look
like from the user's seat? Then left hemisphere: zoom into the suspect
component and trace the exact sequence. Then, critically, hand it back to
the whole: does the fix make sense in the full picture, or did the detail
work produce a patch that breaks something else? The failure mode of skipping
the return to the whole is that you fix the log line and miss the system.
The left hemisphere, alone, is confident the patch is complete.
Citations: ep02:61-63 (the music practice loop: whole, parts, then back to
the whole; skip the last step and you stay in parts forever), ep02:75-77
(corpus callosum as gatekeeper: the two views must stay separate and
connected), ep02:192-193 (Q&A 5 applied answer on debugging).

---

## Chapter ep03 — Resilience

### Q7 [numerical]
After 9/11, experts predicted a permanent mental health crisis and FEMA
allocated about 130 million dollars for free therapy in New York. Early
surveys found roughly 8 percent PTSD among Manhattan residents, 20 percent
near the World Trade Center, and possibly 30 percent or higher among the
directly affected. What did the six-month reading show, and what two
quantities did the early prediction confuse?

**Answer:** By six months the numbers were more or less back to normal, quite
low for the city as a whole. The prediction confused initial distress with
lasting damage. The early spike measured initial distress, which is the
stress response working as designed. The six-month reading measured lasting
damage, which is what the predictions were really about. COVID repeated the
pattern: predicted suicide catastrophe, suicides stayed the same or declined
globally.
Citations: ep03:57 (FEMA 130 million, 8/20/30 percent early surveys, back to
normal by six months), ep03:194 (Q&A 2 answer: confused initial distress
with lasting damage), ep03:61-63 (COVID: suicides stayed the same or
declined).

### Q8 [mechanism]
Therapists are trained professionals, yet the episode says they systematically
overestimate human fragility. Reconstruct the exact sampling mechanism, and
state whose picture of human nature it distorts.

**Answer:** A therapist's entire workday is spent, by definition, with the
people who struggle. The resilient majority never makes an appointment, so
the therapist never meets them. Seeing traumatized people all day, they
overgeneralize from that sample to the general population: the struggling
look like the population. The professional class that defines normal samples
the chronic 10 percent, not the majority. The chapter calls this very human,
not evil or dumb, but the distortion matters because therapists and
researchers are the people who write the official story about human nature.
Citations: ep03:117-124 (the therapist's sample: office sees the chronic
10 percent daily, the resilient majority is rarely seen), ep03:77 (chronic
trajectory characterizes at most about 10 percent).

### Q9 [applied]
A close friend lost a parent and seems fine two weeks later. Her family
thinks she is in denial. What does the episode say to do, and what two
things does it say not to do?

**Answer:** Do not pathologize her. Fast return to function is the resilience
trajectory, the majority pattern, not denial. That is Julia's mother's
mistake: she sent a resilient daughter to a grief counselor for not grieving
enough. Two things not to do: do not apply the denial label, and do not build
the eggshell cage (do not stop laughing around her, do not tiptoe). Bonanno
and Keltner's research shows genuine laughter during grief correlates with
better long-term mental health. Be normal with her and let her grieve in her
own pattern. Only worry if she enters the chronic trajectory: unable to
function over the long term, in which case she needs professional help, not
amateur diagnosis.
Citations: ep03:205-207 (Q&A 6 applied answer), ep03:33-39 (Julia: mother
called resilience denial of grief and suggested a counselor), ep03:141-147
(eggshell cage; laughter during grief correlates with better long-term
mental health), ep03:77 (chronic is at most about 10 percent and needs care).

---

## Chapter ep04 — Courage

### Q10 [explain like I am new]
Explain the episode's definition of courage to someone who believes brave
people are fearless. Use the Cory Booker story and the episode's formula.

**Answer:** The episode says, as strongly as it can, that the fearless model
of bravery is bankrupt and simply not true. Cory Booker ran into a burning
house to save his neighbor's daughter and later said terror filled him and
he thought he was trapped. He was not fearless. He acted anyway. The
episode's formula: courage is fear plus an expanded circle of love. Brave
people expanded their circle until strangers count as kin; they think of
strangers the way they think of their children, siblings, or parents. The
figure states the two models: movie model is feel no fear then act (so if
you feel fear, you conclude you are not brave, and you freeze); episode model
is feel fear then act for the widened circle (fear is expected, love
decides).
Citations: ep04:96-100 (Booker: terror filled him, thought he was trapped),
ep04:108 (the fearless idea is bankrupt; courageous people expanded their
circle of love), ep04:110-115 (Figure 3: the two models of courage).

### Q11 [mechanism]
Marsh scanned the brains of altruistic kidney donors. What structural
difference did she find, what behavior does it track, and what causal caution
does the chapter require?

**Answer:** Extreme altruists seem to have larger amygdalas than the rest of
us. The amygdala helps us recognize distress in other people, and extreme
altruists appear more sensitive to the pain of others. Psychopaths, at the
other end, tend to have smaller amygdalas and often fail to recognize others'
distress. The structure tracks the behavior: sensitivity to others' distress
is the hardware under the donors' flat generosity curve. The required
caution: the scans establish a correlation, not a proven causal direction.
Does a larger amygdala cause the altruism? Keep the claim inside the
evidence: the difference exists, and the mechanism is the episode's
interpretation.
Citations: ep04:84 (scans: larger amygdalas in extreme altruists, smaller in
psychopaths), ep04:150 (Q&A 4 answer: correlation from brain scans, not
proven causal direction; keep the claim inside the evidence).

### Q12 [applied]
You witness a medical emergency on a crowded street. The episode names the
force that will make you wait, and gives a two-part counter. Name both.

**Answer:** The force is the bystander effect: when many people can help,
each one waits for someone else to move first, and responsibility divides by
the number of witnesses until nobody feels it is theirs. The two-part
counter: first, name the effect out loud in your head, then break the
diffusion by assigning responsibility, to yourself first. Do not wait for
the crowd. Walk over. If you need others, point at specific people: one
calls emergency services, one helps you directly. Specific assignment
collapses the diffusion. The deeper move, from the donors: see the stranger
as kin. You do not need to feel no fear; you need the circle to include
them. Freezing does not disqualify you; the smallest widened-circle action
counts, and calling for help is still help.
Citations: ep04:144 (bystander effect as diffusion; responsibility divides
by the number of witnesses), ep04:156 (Q&A 6 applied answer: name the
effect, assign specific people, see the stranger as kin, freezing does not
disqualify).

---

## Chapter ep05 — Forgetting

### Q13 [numerical]
Researchers had volunteers' real school grades. People recalled A-grade
tests accurately 89 percent of the time and D-grade tests only 29 percent
of the time. Recompute the ratio, and state what the result proves about
whether the editing is deliberate.

**Answer:** 89 divided by 29 is about 3.07, roughly a three-to-one bias
toward remembering success. The volunteers knew the researchers held the
real records, so this was not deliberate deception. Their memories had
genuinely reshaped: success strengthened, failure weakened. It proves the
edit is real and unconscious, and it proves the direction: the brain keeps
the version of the past that helps you move forward. Your brain is not lying
to you. It edits for you.
Citations: ep05:111-113 (grades study: 89 percent for A, 29 percent for D;
volunteers knew researchers had the real grades), ep05:117-119 (Figure 3
table; three-to-one bias toward remembering success), ep05:192 (Q&A 3
answer: the edit is real and unconscious).

### Q14 [explain like I am new]
Explain to a newcomer why forgetting helps, using Jill Price and the
chapter's correction of the filing-cabinet metaphor.

**Answer:** Jill Price has highly superior autobiographical memory: she can
recall the weather on September 30, 1998 (sunny, clouds at about 3:00, no
rain), a childhood Muppets-studio meltdown in perfect detail, and every
moment of the drive to the hospital where her husband died, unfaded years
later. It sounds like a superpower, but it is a curse: every painful memory
stays as fresh as the day it happened. The filing-cabinet metaphor is the
mistake behind the shame: we picture storing folders and retrieving them
unchanged, so forgetting feels like failure. The real model is
reconstruction: you rebuild the event each time from the gist plus your
current mood and context. Forgetting discards what you do not need (the
breakfast details, the traffic lights, the D grades) so the gist stays
usable. When we say time heals our wounds, what we mean is that time helps
us forget. Not for someone like Jill.
Citations: ep05:29-41 (Jill Price: Sept 30 1998 weather; Muppets meltdown;
husband's death drive unfaded), ep05:43-51 (Figure 1 table: typical memory
versus Jill), ep05:57-65 (filing cabinet versus reconstruction model),
ep05:53-55 (time heals because time forgets).

### Q15 [applied]
You keep replaying an embarrassing mistake from last month. Diagnose it with
the episode's three-part mechanism and give the prescribed fix, including
what Jill Price would tell you.

**Answer:** First, recognize the mechanism: emotion cemented it. The
embarrassment built dense roads to that memory in the city grid, so it
surfaces easily. Second, know that replaying rebuilds it each time
(reconstruction), and each rebuild re-cements it. Third, use the gist rule:
extract the lesson in one sentence and let the sensory detail fade on
purpose. Do not rehearse the scene. Rehearse the sentence. The sentence is
the gist your future self needs. The blush is not. Jill Price would tell you
that you do not want the alternative: perfect retention of every
embarrassment is not a gift. Let the fade happen.
Citations: ep05:67-77 (city-grid model: dense connections mean easy recall),
ep05:57-65 (reconstruction: remembering rebuilds the event each time),
ep05:200-201 (Q&A 6 applied answer: emotion cemented it, rehearsing
re-cements it, rehearse the one-sentence gist, the Jill test).

---

## Chapter ep06 — Memorability

### Q16 [numerical]
ResMem returns a score of 0.7 for one of your slides. What does that number
mean, in the chapter's terms? The museum study tested five candidate
predictors. Which ones passed, and what would you change first to raise the
score?

**Answer:** ResMem scores run from 0 to 1: 1 means 100 percent of people
remember the image, 0 means no one does. A 0.7 means roughly 70 percent of
people would remember it. Of the five candidates tested at the Art Institute
of Chicago, size passed (bigger paintings were more memorable) and context
passed (paintings in the modern, spacious wing beat cluttered rooms).
Beauty, emotion, and colorfulness all failed. So change first: make the key
element bigger and give it space (one idea per slide, the spacious-wing
treatment). Do not rely on making it prettier or more emotional.
Citations: ep06:99 (ResMem score: 1 means 100 percent remember, 0 means no
one does), ep06:79-87 (museum predictors: size yes, context yes, beauty no,
emotion no, colorfulness no; Figure 2 table).

### Q17 [mechanism]
Before building ResMem, Bainbridge tested two plausible theories for the
visual Mandela effect. Name both theories, state the verdict, and explain
why the verdict mattered for what came next.

**Answer:** Theory one: wrong versions of the images are everywhere on the
internet and we absorbed misinformation. Theory two: mental associations lead
us astray (a rich 1930s banker has to have a monocle). Bainbridge tested
these theories and they were wrong. The brain simply has a propensity to
remember certain images, and the wrong version of the image is just more
sticky. The verdict mattered because it ruled out cultural transmission and
association as the cause and pointed at the brain itself: memory errors are
systematic, not random. Systematic errors have rules, and rules can be
learned, which is what ResMem then did by training on ordinary photos with
no art history at all.
Citations: ep06:63 (the two theories tested: misinformation, mental
associations; they were wrong; the wrong version is just more sticky),
ep06:156 (Q&A 1 answer: systematic errors have rules, and rules can be
learned, which is what ResMem did), ep06:99 (trained on regular
photographs, knew nothing about Picasso).

### Q18 [applied]
You give a work presentation next week. Give the episode's four-part
playbook and the two-test warning, with the chapter's own names for the
pieces.

**Answer:** You do not fight for attention. You fight to be remembered in
other people's brains, and the fight is rigged by their hardware. Playbook:
make the key slide big (size mattered), give it space (the spacious wing
beat the cluttered room, so one idea per slide), do not rely on beauty or
emotion to carry it (both failed as predictors), and add one distinctive
visual hook, the equivalent of C-3PO's silver leg: the specific, slightly odd
detail the brain files. Then test it: show the slide to a colleague for ten
seconds, take it away, and ask what they remember. That is your personal
ResMem. Warning: run the stickiness test and the meaning test separately.
A shocking or garish design may score high on recall and low on trust.
ResMem cannot tell you if the image has meaning, and neither can a recall
quiz. The brain does not file by importance: boring and important still
needs the hook.
Citations: ep06:170-171 (Q&A 6 applied answer: size, space, one idea per
slide, the silver-leg hook, the 10-second colleague test), ep06:105-109
(the boundary: ResMem scores memorability, not meaning; the car-crash photo
counterexample).

---

## Chapter ep07 — Choking Under Pressure

### Q19 [numerical]
Beilock's digit ladder runs three tasks: repeat 7624, repeat 589743, repeat
910482 in reverse. Order them by difficulty and state exactly what
operations the hardest one adds. What three things does the ladder prove
about working memory?

**Answer:** Easiest: repeat 7624 (4 digits, hold and echo). Harder: repeat
589743 (6 digits, hold more). Much harder: repeat 910482 in reverse (6
digits, but hold the whole series, ask what the last number is, re-hold the
whole series from the start, pick out the second-to-last, and so on).
The reversal adds computing on top of holding: the store must hold the
series, compute the reversal, and emit it in order. The ladder proves three
things: the store is small, it is shared between holding and computing, and
adding operations degrades both. Map it to Cate's race: four digits is the
warm-up swim, six digits is the final with the plan loaded, six reversed is
the final with the false-start worry loaded on top. Same store, more
operations, collapse.
Citations: ep07:43 (the three digit tasks), ep07:49-51 (Figure 1 ladder
table: hold and echo, hold more, hold reorder emit), ep07:168 (Q&A 2 answer:
the ladder proves the store is small, shared, and degrades under added
operations; the Cate mapping).

### Q20 [explain like I am new]
Explain choking to someone who has never heard the term, using the chapter's
workspace metaphor and the Cate Campbell story.

**Answer:** Your brain has a small workspace called working memory. It holds
the few things you are actively thinking about while you do a task. Under
pressure, worry moves into that workspace: the flinch, the crowd, the voice
saying you will mess up. The workspace is small, so the worry pushes out
the task. Cate Campbell did not forget how to swim. On the blocks she made
a slight flinch, worried it would be judged a false start, and her working
memory, which should have run the race plan, ran the worry instead. She
swam the first 50 meters too fast on autopilot and died in the second half,
finishing sixth. Choking is not skill failure. It is workspace theft.
Citations: ep07:37-41 (working memory as cognitive horsepower; the hijack),
ep07:33 (Cate: flinch, attention shifted to the false-start worry, first 50
too fast, finished sixth), ep07:55-59 (Figure 4: the hijack table, the skill
does not leave, the processor gets reassigned), ep07:163 (Q&A 1 answer:
choking is workspace theft, not skill failure).

### Q21 [applied]
You have a job interview in one hour and your heart pounds. Run the
episode's toolkit in order, and state the one instruction the episode says
not to follow.

**Answer:** First, reframe, now: sweaty palms and pounding heart mean your
body readies itself, shunting blood to your brain so you can think. Say it
literally. The symptoms do not change; the label changes, and the label
decides what working memory does with them: fuel versus verdict. Second,
breathe: two minutes of slow exhales, giving the store a neutral occupant
and calming the body. Third, ritual: pick one now, a short phrase or a
backward count from 20, and run it in the waiting room to hold the slot that
worry wants. Fourth, trust the practice: your preparation moved the answers
toward automaticity, so stop rehearsing and let the store stay clear for the
novel parts, the interviewer's actual questions. Do not try to "calm down."
That is a suppression task, and suppression bills the store. If you blank
mid-interview, breathe once, run the ritual phrase, and let the automatic
knowledge surface instead of chasing it with the worried store.
Citations: ep07:113 (reframe: beating heart shunts blood to the brain;
the label decides: fuel versus verdict), ep07:119-129 (breathe and ritual
mechanisms), ep07:135-140 (Figure 3: the four solutions and their
mechanisms), ep07:179-180 (Q&A 6 applied answer, including do not try to
calm down).

---

## Think-it-yourself drills verification

For each chapter, every drill was checked: does the drill have a correct
expected answer, and is that answer derivable from the chapter text?

- ep01, Drills 1-6: guided with answer sketches. Drill 1: 44 to 1 from
  ep01:85. Drill 2: name the generator for your own instances; the F=MA
  pattern is the model (ep01:41-43). Drill 3: design the visibility window;
  Nike's sole window is the model (ep01:248-251). Drill 4: design a
  subtraction rule; one-in-one-out is the model (ep01:177-179). Drill 5:
  compare your count to the UVA baseline of fewer than 10 percent of 750
  (ep01:130). Drill 6: open thought experiment, the Strider mechanism is
  the model (ep01:197-201). Verdict: derivable.
- ep02, Drills 1-6: guided with answer sketches. Drill 1: narrow/wide
  attention for a slow query, from the bird figure (ep02:45-51). Drill 2:
  tone versus words, from the Joe/PBS section (ep02:83). Drill 3: predict
  intact versus disabled verdicts, from Figure 2 (ep02:95-101). Drill 4:
  confidence audit, the anti-confabulation move (ep02:169-171). Drill 5:
  whole-part-whole rep, from the loop (ep02:61-63). Drill 6: emissary
  takeover, from the modern-world section (ep02:143-159). Verdict:
  derivable.
- ep03, Drills 1-6: semi-guided. Drill 1: compute the gap between your
  predicted percentage and the chapter's at most 10 percent (ep03:77).
  Drill 2: apply the four trajectories to a fast recovery (ep03:69-79).
  Drill 3: FEMA for/against from the 130 million and the six-month reading
  (ep03:57, ep03:194). Drill 4: flexibility check, the chapter names rigid
  responses as the predictor (ep03:133-137). Drill 5: contagion audit,
  from the resilience blind spot and contagion (ep03:109-115). Drill 6:
  steelman both sides of the descendant argument (ep03:165-171). Verdict:
  derivable.
- ep04, Drills 1-6: semi-guided. Drill 1: draw your discount curve; the
  chapter's curve is the model (ep04:70-76). Drill 2: filmer's question,
  both sides in the chapter (ep04:144-145). Drill 3: three risks as
  decision points (ep04:55, ep04:153). Drill 4: reconstruct the four-step
  chain and mark scans versus interpretation; the chapter explicitly marks
  the boundary at ep04:150. Drill 5: the bigger thing, Vedantam's model
  (ep04:121). Drill 6: hardware versus circle, both sides present in the
  chapter; Q&A 3 follow-up gives the boundary (ep04:147). Verdict:
  derivable.
- ep05, Drills 1-6: semi-guided. Drill 1: gist ratio, the breakfast model
  (ep05:79-83). Drill 2: 89/29 audit, the editor at work (ep05:111-113).
  Drill 3: build a road, the city-grid model (ep05:67-77). Drill 4: Chris
  test, the chapter predicts the negatives get dropped (ep05:123-129).
  Drill 5: mood versus life, the mood loop (ep05:149-157). Drill 6: argue
  both sides, the Jill Price evidence for side B (ep05:43-55). Verdict:
  derivable.
- ep06, Drills 1-6: less guided. Drill 1: wrong-version audit, the three
  quiz items are the model (ep06:27-35). Drill 2: redesign for
  memorability, the museum findings are the constraints (ep06:79-87).
  Drill 3: fame direction, both directions argued in the chapter; the trap
  card and Q&A 4 give the evidence (ep06:145, ep06:161-163). Drill 4: design
  a meaning test ResMem cannot run, the boundary section gives the shape
  (ep06:105-109). Drill 5: shared-hardware experiment, the 10,000-face
  design is the model (ep06:69). Drill 6: canary diagnostic, the
  Alzheimer's application is the model (ep06:131-137). Verdict: derivable.
- ep07, Drills 1-6: no answer sketches by design ("Reason from the
  episode, unaided," ep07:209). Expected answers are still derivable.
  Drill 1 (flinch autopsy): the expected answer is that the race was lost
  at the starting blocks when the flinch worry hijacked the store, not at
  the turn; the chapter states nearly everything important happened before
  the race began (ep07:33). Drill 2 (design the experiment): groups,
  warning, and measurement follow the yellow-square design (ep07:87-91)
  plus the reframing intervention (ep07:113). Drill 3 (oath rewrite): each
  change is justified as store management from Figure 3 (ep07:135-140).
  Drill 4 (hijack inventory): framework from the hijack model
  (ep07:55-59). Drill 5 (stereotype audit): mechanism at ep07:103, naming
  move at ep07:160. Drill 6 (track synthesis): the seven ideas are all
  named in the chapter's own closing (ep07:209-211). Verdict: derivable.

---

## Gate verdict: E1 PASS

- 21 of 21 questions answered from the chapter text ONLY, every answer
  carrying chapter:line citations.
- Type quotas met: 5 numerical (need 4), 5 explain-like-new (need 4),
  7 applied (need 4), 4 mechanism.
- All 21 test deep understanding: mechanisms (Q5, Q8, Q11, Q13, Q17,
  Q19), recomputed numbers (Q1, Q7, Q13, Q16, Q19), and decisions
  (Q3, Q6, Q9, Q12, Q15, Q18, Q21). No trivia.
- All "Think it yourself" drills across all 7 chapters have correct
  expected answers derivable from the chapter text, including ep07's
  sketch-free drills.
- Honest-gap note: chapters for ranks 1, 2, and 8 have no episode
  transcripts (stated in the task context). Nothing in this exam required
  transcript content; every citation is to the chapter files themselves.
- No failures. Nothing in the FAIL list.
