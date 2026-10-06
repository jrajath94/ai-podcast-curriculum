# TRACK BUILDER BRIEF — AI Podcast Curriculum
# Read verbatim before any other project file:
#   1. ~/workspace/stanford-frontier-ai/build/MASTER_BRIEF.md
#   2. ~/workspace/stanford-frontier-ai/build/REJECTIONS.md
#   3. ~/workspace/stanford-frontier-ai/build/PIPELINE.md
# Figure law for THIS project: ~/workspace/stanford-frontier-ai/build/VISUAL_SYSTEM.md
# (generic spec — captions name the PROJECT "AI Podcast Curriculum", never a course).

## Your assignment
You are the BUILDER for one track: {TRACK_NAME} ({TRACK_SLUG}).
Research is done: ~/workspace/ai-podcast-curriculum/research/{TRACK_SLUG}/episodes.json
lists the 10 episodes (ranked by verified YouTube view counts, Oct 2026),
and transcripts live in research/{TRACK_SLUG}/transcripts/<video_id>.txt.

## What you deliver
In ~/workspace/ai-podcast-curriculum/content/tracks/{TRACK_SLUG}/:
- ep01.md … ep10.md — one textbook chapter per episode, in view-count rank order.
- index.md — track index: the 10 episodes, each with a one-line "why this
  episode matters" (what the reader gains that no other episode gives).
- cheatsheet.md — one dense page: every key fact, number, name, decision.
- _coverage.md — the coverage map: every major claim/topic from each
  episode mapped to chapter:line. Zero unmapped major claims.

Frontmatter per chapter (YAML):
---
page_id: {TRACK_SLUG}-ep01
course_slug: {TRACK_SLUG}
course_name: "{TRACK_NAME}"
course_order: {N}
order: 1
nav: "Ep 1 · <short title>"
title: "Episode 1: <title>"
summary: "<one line>"
date: "<episode upload date>"
instructor: "<guest name>"
offering: "<show name>"
video_id: "<youtube id>"
video_title: "<episode title>"
video_caption: "<one line on what the episode covers>"
concepts: [tag1, tag2]
sources:
  - tag: episode
    label: "<episode title>"
    url: https://www.youtube.com/watch?v=<id>
---

## Content laws (from MASTER_BRIEF.md, adapted)
- PURPOSE: FOR LIFE, NOT INTERVIEWS. Every chapter is built to be
  INTERNALIZED. Three mandatory sections in every chapter:
  (a) "## How to imbibe this" — concrete practices: what to do THIS
  WEEK, how to catch yourself living it or violating it, one
  observable behavior change per major idea.
  (b) "## Think it yourself" — drills the reader does with their OWN
  BRAIN before touching AI: worked reasoning exercises, Fermi-style
  questions drawn from the episode, journaling prompts, "argue both
  sides" drills. The reader reclaims cognition, not outsources it.
  (c) Fidelity: reading the chapter must EQUAL watching the episode.
  Every substantive claim, story-with-a-point, number, and argument
  from the transcript appears. The examiner checks coverage against
  the transcript and fails anything important missing.
- TEXTBOOK NARRATIVE per section: concrete problem → first attempt from
  zero (hand-worked toy, real numbers) → breaks DEMONSTRATED with numbers →
  one-sentence hinge question → new idea from zero → map back → honest
  price with numbers → consolidate at the END only.
- ZERO KNOWLEDGE: define every term at first use. The reader knows
  software, not ML.
- NO JUMPS: one increment per ### subchapter.
- EXPANSION FIRST: cover every major claim, number, anecdote-with-a-point,
  and argument from the episode. Then cut only zero-information sentences.
- Every paragraph carries a number, mechanism step, failure mode, or
  decision rule.
- WHAT IS USED WHERE: map ideas to real systems/models where the episode
  supports it; verify Oct-2026 facts; mark the rest [uncertain]/unknown.
- Q&A: 6–8 per chapter, full follow-up answers — including at least one
  "explain this to me like I am new" and one applied question.
- BOTH kinds of value (Raj's explicit order): (a) deep AI understanding
  AND (b) practical skills. Every chapter ends with a "## Skills you can
  now use" section: concrete things the reader can now DO (e.g., sanity-check
  a scaling claim with arithmetic; estimate training cost from parameter
  count; reason about GPU economics).
- MEMORY AIDS: mnemonics, never-confuse pairs, trap cards in every chapter.
- THE INTELLIGENCE THREAD: across the curriculum, the "Think it yourself"
  drills get progressively harder — the track index states this arc
  explicitly (early chapters: guided drills; later chapters: unaided
  reasoning from first principles). The curriculum trains the reader to
  THINK, not just informs them.
- HONESTY: the episode transcript is the source. Never invent quotes —
  if you quote, it must be verbatim from the transcript (spot-checkable).
  Never invent numbers. [uncertain] where unverifiable. Attribute every
  claim: "In the episode, <guest> says…" vs. your own synthesis, clearly
  separated.
- STYLE: ASD-STE100. No contractions. No em dashes. No semicolons in prose.
  No banned filler.
- MEDIA: the episode itself is the youtube-nocookie embed (video_id in
  frontmatter). Add 1–2 verified go-deeper links per chapter (papers, docs
  mentioned in the episode — check they return HTTP 200).
- NO TOKEN LIMITS. Write until the bar is met.
- DEPTH + CONCISENESS (Raj's standing bar): every chapter must be fully
  understandable from zero prerequisites AND tight enough to learn in one
  sitting. Define every term at first use, but never repeat teaching: each
  paragraph must add new information. If a later paragraph restates an
  earlier one, cut it or compress it to a cross-reference.

## Hardware chapters (Acquired track especially)
Three angles are non-negotiable: (a) why Nvidia is so expensive
(economics + technology moat), (b) what is inside a GPU and a data-center
rack, (c) how to build an AI cluster (networking, power, cooling). If the
10 episodes leave an angle thin, add a synthesis chapter grounded in the
episodes PLUS verified 2026 sources — clearly mark which claims come from
episodes vs. added sources.

## Report back
Per-chapter stats (lines, ###, QAs, figures referenced), the coverage map
location, [uncertain] notes, and honest gaps (episodes whose transcripts
were thin, claims you could not verify).
