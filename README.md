# AI Podcast Curriculum

A textbook-style curriculum built from the most-viewed AI podcast episodes.
Same format and quality bar as the Stanford Frontier AI project: zero-knowledge
progression, subchapters, hand-worked numbers, figures, interview-grade Q&A,
memory aids — plus practical skills in every chapter.

## The 14 tracks

| Track | Show | What it teaches |
|---|---|---|
| `modern-wisdom` | Modern Wisdom — Chris Williamson | <!-- fill after build --> |
| `huberman-lab` | Huberman Lab — Andrew Huberman | <!-- fill after build --> |
| `dwarkesh-patel` | Dwarkesh Patel | <!-- fill after build --> |
| `lex-fridman` | Lex Fridman | <!-- fill after build --> |
| `acquired` | Acquired | <!-- fill after build --> |
| `naval-ravikant` | Naval Ravikant | Wealth, leverage, judgment, happiness — for life |
| `knowledge-project` | The Knowledge Project — Shane Parrish | Mental models, clear thinking, decision-making |
| `dating` | Dating instruction (best of the field) | Genuinely instructional dating: approach, attraction, relationships |
| `fear-social-freedom` | Fear & social freedom | Neuroscience of fear + protocols + social courage in practice |
| `clearer-thinking` | Clearer Thinking — Spencer Greenberg | Rationality, cognitive biases, belief calibration |
| `conversations-with-tyler` | Conversations with Tyler — Tyler Cowen | How a great mind thinks: probing interviews with top thinkers |
| `hidden-brain` | Hidden Brain — Shankar Vedantam | How minds work: the cognitive science of behavior |
| `you-are-not-so-smart` | You Are Not So Smart — David McRaney | Debugging self-delusion: biases, fallacies, motivated reasoning |
| `deep-questions` | Deep Questions — Cal Newport | Sustained focus: deep work, attention, knowledge-work craft |

The thinking arc across tracks 7, 10, 11, 12, 13, 14: mental models → rationality → great minds → how minds work → debugging self-delusion → sustained focus.

Each track: 10 chapters (one per episode), a track index, and a cheatsheet.
Every chapter is built to be imbibed: "How to imbibe this" practices and
"Think it yourself" brain-first drills. The intelligence thread runs across
tracks — the drills get progressively harder, training the reader to think.

## How to read it

Start with the track that matches your curiosity. Inside a track, read
episodes in order — each chapter assumes zero knowledge and builds one idea
at a time. Every chapter ends with "Skills you can now use": concrete things
you can now do, not just know.

Hardware readers: start at `site/hardware.html` — it cross-links the three
angles (why Nvidia is so expensive, what is inside a GPU and a rack, how to
build an AI cluster) wherever they appear across tracks.

## How to rebuild the site

One command, from this directory:

```
python3 build/build.py content site "AI Podcast Curriculum"
```

Output goes to `site/`. The site is fully static: it renders offline except
for the YouTube embeds, which need internet.

## The two skills

- `skills/podcast-deep-dive/` — research any podcast show: top episodes by
  verified view counts, transcripts, topics and key claims. See its SKILL.md.
- `skills/episode-to-textbook/` — convert an episode transcript into a
  textbook chapter at this repo's bar. See its SKILL.md.

Both are also installed at `~/workspace/skills/` for agent use.

## Sources

`research/episodes.json` lists all 50 episodes: title, YouTube URL, view
count and the date it was checked, publish date, guest, key topics.
`research/transcripts/` holds the transcripts the chapters were built from —
the source of truth. Chapters never invent quotes or numbers; anything
unverifiable is marked `[uncertain]`.

View counts verified: <!-- fill date -->.
