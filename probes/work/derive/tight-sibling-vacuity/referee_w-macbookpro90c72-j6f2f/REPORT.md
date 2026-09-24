# Referee report: J:derive:tight-sibling-vacuity:a1

- **Author:** `w-jonathonsmac4f50-j2496` (`claude-opus-5`).
- **Referee:** `w-macbookpro90c72-j6f2f` (`grok-4.6`). Different model family.
- **Material:** the attempt's ten marks. The one-set and the costs below are recomputed. The author's dynamic program is not called.

## The statement

(Q) says a processed site with at least two processed 1-predecessors cannot have all of them tight. Block 33's (H) says `v(z) ≤ 0` at every processed site. The attempt says both fail at one explicit realization, and that `c*(η, 333) = 10/9`.

## Steps

**R1.** From `M = {000, 001, 010, 100, 021, 102, 210, 113, 131, 311}`, a site is 1 when it is marked or has two 1-predecessors. The one-set in `[0,3]³` equals the one-set in `[−2,6]³`: 37 sites, all inside the small cube. Predecessors drop a coordinate, so nothing outside `[0,3]³` can acquire two 1-predecessors once the small cube is closed. This is the realization on `Z³`.

**R2.** One seed, nine amplified sites, 27 processed sites. Level sizes `1,3,3,4,3,6,7,6,3,1`. `333` is processed, and so are `233`, `323` and `332`.

**R3.** A level bitmask sweep and a separate 0-1 program (each non-seed has a predecessor in the set) both give `v(233) = v(323) = v(332) = 0` and `v(333) = 1`. (Q) is false. (H) is false at the processed site `333`. The tight-sibling hypothesis holds there, and no rooted tree has cost ≤ 0.

**R4.** Over closed sets at `333` with an amplified site, `min(E − |A|) = 1`, `min(E − (10/9)|A|) = 0` and `min(E − (11/9)|A|) = −1`. The integer program gives `min(9E − 10A) = 0`, so the ratio `10/9` is achieved and is the minimum. Lifting the level cap does not change it: `333` is the only site at level 9. Thus `c*(η, 333) = 10/9`.

**R5.** Deleting any one of the nine non-seed marks makes `333` not processed. The witness is minimal for single-mark deletion.

## Verdict

The counterexample survives. (Q), the tight-sibling lemma and (H) fail at this realization, and the family constant is at least `10/9`.
