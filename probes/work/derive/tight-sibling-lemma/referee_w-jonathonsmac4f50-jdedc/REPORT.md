# Referee report: J:derive:tight-sibling-lemma:a1

- **Author:** w-macbookpro90c72-j133a (grok-4.6).
- **Referee:** w-jonathonsmac4f50-jdedc (claude-opus-5).
- **Material:** the attempt's `ATTEMPT.md` and `check.py` as run in its log `w-macbookpro90c72-j133a__941d6e5f__20260919T013129Z`.

**Disclosure.** This referee's model family refereed attempts a4 and a5 of this problem (grok), using the same enumeration on the cube.
`check.py` is independent code: its own automaton on the isolated `3×2×2` box, and its own exhaustive enumeration of the counted family,
with forks. Nothing is taken from `probes/lib/family.py` or the author's script.

## The claim

The census covers all 4096 noise patterns on the `3×2×2` box. Consider every processed `z` that has a fork-related pair of processed
1-predecessors: there are 4544 such (pattern, `z`, pair) cases.
- At those `z`, `brute_min(c* = 1)` lies in `{−8, …, −1}` and is never 0.
- So the box contains no local tight-sibling counterexample.
- The lemma on `Z³` stays open.

## Step by step

**Step 2 (census): holds, with a definitional correction.**
- **B1.** The 4544 cases reproduce. Every pair of 1-predecessors of `z` is a fork pair. Without a level cap, which is how
  `family.brute_min` enumerates, the histogram is exactly the attempt's.
- **B2.** The task defines `v(z)` over trees with all nodes at levels `≤ level(z)`. With that cap, the histogram is
  `{−8:16, −7:240, −6:400, −5:1408, −4:560, −3:448, −2:1328, −1:144}`.
  - 96 cases move up by one.
  - None reaches 0.
  - So the attempt's numbers are not the definition's values, but its conclusion holds for the definition's values too.

**Step 1's "equivalent local test": does not follow as stated.** The attempt reasons that because `v(z) < 0`, the two predecessors
"cannot both be tight". That does not follow. What the census shows is that the lemma's conclusion holds at every such `z`.

**B3: the census never tests the lemma's hypothesis.** No `z` in any of the 4096 patterns has all its 1-predecessors processed and tight
(capped values). This is the same situation a4 and a5 found on the cube.

**Step 3 (scope): stated correctly.**

## Verdict

The finite census survives, both with and without the level cap, with the corrections above.

`check.py` prints `HIT: confirmed - ...` and its SUMMARY line.
