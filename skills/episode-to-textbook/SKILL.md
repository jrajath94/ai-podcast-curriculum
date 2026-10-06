---
name: "episode-to-textbook"
description: "Convert a podcast episode transcript into a textbook chapter: zero-knowledge progression, subchapters, hand-worked numbers, figures, Q&A, memory aids, practical skills. Use when turning episode transcripts into curriculum chapters."
---

# Episode to Textbook

## Purpose
Turn one episode transcript into one textbook chapter that teaches a zero-knowledge reader the episode's ideas as if from a textbook — same bar as the Stanford Frontier AI curriculum.

## Workflow
1. Read FIRST (verbatim): `~/workspace/stanford-frontier-ai/build/MASTER_BRIEF.md`, `~/workspace/stanford-frontier-ai/build/REJECTIONS.md`. Figure law: `~/workspace/stanford-frontier-ai/build/VISUAL_SYSTEM.md` (generic spec — captions name the project, never a course).
2. Read the full transcript. List the episode's major claims, numbers, anecdotes-with-a-point, and arguments. This is the coverage set — every item must land in the chapter.
3. Draft the chapter in markdown with YAML frontmatter (schema in references/chapter-frontmatter.md).
4. Structure per MASTER_BRIEF.md content laws: textbook narrative chain per section (problem → attempt from zero with hand-worked numbers → break demonstrated → hinge question → new idea from zero → map back → honest price → consolidate at END only); ### subchapters, one increment each; zero-knowledge (define every term at first use); expansion first, then cut only zero-information sentences.
5. Figures: one per state-change per the visual spec (medium ladder: table → ASCII → mermaid → SVG first; generated plates only where the ladder demands). Captions name the project + source.
6. Q&A: 6–8 per chapter with full follow-up answers — at least one "explain like I am new" and one applied question.
7. End every chapter with `## Skills you can now use`: concrete things the reader can now DO (worked examples: sanity-check a claim with arithmetic, estimate a cost, reason about a tradeoff).
8. Memory aids: mnemonics, never-confuse pairs, trap cards.
9. Honesty: the transcript is the source. Quotes must be verbatim and spot-checkable. Never invent numbers. `[uncertain]` where unverifiable. Separate "in the episode, the guest says…" from your synthesis.
10. Media: the episode as youtube-nocookie embed (video_id in frontmatter, oEmbed-verified); 1–2 verified go-deeper links (HTTP 200).
11. Self-check against REJECTIONS.md's 15 patterns before delivering. Then hand to a separate auditor agent — never self-certify.

## Output Contract
- One `<slug>.md` chapter file with valid frontmatter.
- A coverage list mapping each major transcript claim → chapter location.
- Report: stats (lines, subchapters, QAs, figures), [uncertain] notes, honest gaps.

## Operating Rules
- No token limits: write until the bar is met; split across appends.
- ASD-STE100: short sentences, plain words, no contractions, no em dashes, no semicolons in prose, no banned filler.
- Images via media pipeline only. Never touch the user's OpenRouter key.
- Never invent quotes, numbers, or benchmarks. Attribute everything.
