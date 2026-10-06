# ep08 patch — Caesar Augustus subsection (surgical fix)

## Defect

The current `### Caesar Augustus` subsection in ep08.md contains two errors,
both verified against the transcript
(`research/dwarkesh-patel/transcripts/bc6uFV9CJGg.txt`):

1. **False transcript claim.** The chapter says: "[uncertain] The available
   transcript cuts off mid-sentence during the Augustus segment; the summary
   above reflects the portion available." The transcript is complete: the
   Augustus segment runs in full, and the file ends with a clean sign-off
   ("Awesome, that was excellent, Mark. Thanks so much. That was a lot of fun.
   Yeah, really fun. Thanks for having me. Absolutely."). The `[uncertain]`
   marker must be deleted, not just reworded.
2. **Misframed thesis.** The chapter says Zuckerberg's point is "structural vs
   personal power: institutions outlast individuals." That is not what he says.
   His point: Augustus redefined peace itself — from "the temporary time
   between when your enemies inevitably attack you" to a positive-sum economy —
   and the general principle is "the bounds on what people can conceive of at
   the time as rational ways to work." The parallel he draws is explicit:
   investors cannot wrap their heads around open-sourcing Llama ("that must
   just be the temporary time between which you're making things proprietary,
   right?"), the same zero-sum frame Augustus faced. The fix reframes the
   subsection around this, and covers the parts the chapter drops entirely:
   Dwarkesh's 19-year-old angle, the Picasso quote, and the Open Compute
   Project example (the concrete proof that open-sourcing the complement
   works: the industry standardized on Meta's server designs, supply chains
   built out around them, volumes went up, and it "saved us billions of
   dollars").

The misframing also propagates into the "Think it yourself" drill 4
("apply the structural-vs-personal power distinction"), which must be
rewritten to match the actual thesis.

## Replacement subsection (drop-in, STE100)

Replace everything from `### Caesar Augustus` through the end of the
`[uncertain]` paragraph (i.e., up to but not including `## Questions and
answers`) with the following:

```
### Caesar Augustus

The unexpected segment, and it is about open source, not Rome. Zuckerberg's
point: Augustus became emperor and tried to establish peace, but at the time
there was no real conception of peace. People's understanding of peace was
"the temporary time between when your enemies inevitably attack you." A short
rest. Augustus's novel idea was changing the economy "from being something
mercenary and militaristic to this actually positive-sum thing."

The general principle Zuckerberg draws: "the bounds on what people can
conceive of at the time as rational ways to work." That applies directly to
the metaverse and to AI. Investors cannot wrap their heads around
open-sourcing Llama: "I don't understand, it's open source. That must just
be the temporary time between which you're making things proprietary, right?"
The zero-sum frame is the same one Augustus faced. Zuckerberg's reply, in
effect: "I think there are more reasonable things than people think."

Dwarkesh adds his own read, flagged as "probably totally off": maybe it is
about being 19. Caesar Augustus was 19 and already one of the most important
people in Roman politics, leading battles and forming the Second Triumvirate.
Maybe the 19-year-old Mark thought, "I can do this because Caesar Augustus
did this." His gloss: the Picasso line, "all children are artists and the
challenge is to remain an artist as you grow up." When you are young, wild
ideas are easier; there are analogies to the innovator's dilemma in a life
and in a company. The open question he puts to Zuckerberg: how do you stay
dynamic?

Zuckerberg then grounds the open-source philosophy in Meta's history. The
biggest example: the Open Compute Project. Meta open-sourced its server,
network switch, and data center designs. The industry standardized on them.
Supply chains built out around Meta's design. Volumes went up, costs fell
for everyone, and it "saved us billions of dollars." The pattern he names:
open-source the complement (infrastructure, and now models), monetize the
product. He is explicit about the boundary: "We don't take the code for
Instagram and make it open source." Products stay closed; the layers
underneath get opened when opening them makes the ecosystem, and Meta,
stronger.
```

## Replacement drill 4 (in `## Think it yourself`)

Replace:

```
4. Augustus: apply the structural-vs-personal power distinction to a team or organization you know. What is personal that should be structural?
```

with:

```
4. Augustus: find one thing in your work that everyone treats as zero-sum ("the temporary time between attacks") and reframe it as positive-sum. What would the Augustus move be? What stops people from seeing it?
```

## Effect on the coverage map

`_coverage.md` for ep08 should gain one row (currently missing): the Augustus
segment maps to ep08.md's `### Caesar Augustus` subsection. The false
`[uncertain]` about a cut-off transcript should be struck from the coverage
map's `[uncertain]` collection.
