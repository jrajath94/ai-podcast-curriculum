# Chapter frontmatter schema

```yaml
---
page_id: <track>-ch01        # unique
course_slug: <track>         # e.g. acquired
course_name: "<Track Name>"
course_order: 1
order: 1
nav: "Ch 1 · <short title>"
title: "Chapter 1: <title>"
summary: "<one line>"
date: "<episode upload date>"
instructor: "<guest name>"
offering: "<show name>"
video_id: "<youtube id>"      # oEmbed-verified
video_title: "<episode title>"
video_caption: "<one line on coverage>"
concepts: [tag1, tag2]
sources:
  - tag: episode
    label: "<episode title>"
    url: https://www.youtube.com/watch?v=<id>
---
```

Body conventions (rendered by the shared build.py):
- `### Subchapter` headings, one idea each.
- `> [!QA]` blocks: Q: / A: / Follow-up: lines.
- `> [!MEMORY]` blocks for memory aids, `> [!KEY]` for key ideas.
- Images: `![alt](assets/<file> "caption")` → figure + figcaption.
- Mermaid: fenced `mermaid` blocks. ASCII: fenced `ascii` blocks.
- Timestamp links: `[label](ts:12:34)` → YouTube timestamp link (needs video_id).
