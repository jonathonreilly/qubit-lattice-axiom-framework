# Referee report: J:derive:beyond-the-union-bound:a2

- **Author:** w-macbookpro90c72-ja988 (grok-4.6).
- **Referee:** w-jonathonsmac4f50-j3743 (claude-opus-5).
- **Material:** the attempt's `ATTEMPT.md` and `check.py` as run in its log `w-macbookpro90c72-ja988__f67a3bd3__20260919T012316Z`.

**Disclosure.** This referee's model family wrote another attempt on this problem (w-jonathonsmac4f50-jae8a, the history-count certificates
that a2 mentions). a2 takes a different route and does not build on it. `check.py` is independent code: its own geometry, Fractions and
sympy. Nothing is taken from the author's script.

## The claim

The object is the isolated fork-pair kernel of block 30's dominating automaton `η'`.
- **The kernel.** There is one majority child and there are four amplification children, giving seven child fork pairs.
  `P(some child pair both 1) = 1 − (1−ε₂)⁴`, and the mean number of such pairs is `4ε₂ + 3ε₂²`.
- **The threshold.** The mean is below 1 iff `ε₂ < (−2+√7)/3`. On `(p,1,2)` that first happens at `p = 13`.
- **The eroder.** At `ε = 0`, two steps on the depth-2 cone erase an isolated base pair.
- **Where the route stops.** An atom-sum `(q, r)` closure has `r`-coefficient `> 1` at every `p`, so the route stops at its step 5.

## Step by step

**Steps 1–2 (geometry): hold.**
- G1: `d₁, d₂, d₃` equal the kernel's deviations directly, at six values of `p`. The identity for `d₂ − d₃` holds, and at `p = 11`,
  `d₂ = 43/164 > d₃ = 3/14`.
- G2: the three predecessors of a site are pairwise forks.
- G3: `w = u + e₁ = v + e₂`, with four one-parent children, all fork-adjacent to `w`. There are seven child fork pairs.

**Steps 3–4 (kernel, threshold): hold as defined, with a scope correction.**
- G4, over the 16 amplification patterns:
  - `P = 1 − (1−ε)⁴` and the mean is `4ε + 3ε²`, symbolically;
  - the threshold root is `(−2+√7)/3 = 0.21525`;
  - the first integer below it is `p = 13`, since `d₂(12) = 11/47` and `d₂(13) = 45/214`.
- **The scope correction (G5).** `w` has two more fork neighbours with no parent in `{u, v}`. They are 1 with probability `ε₁`, and the
  child-only count leaves them out. Counting every next-level fork pair that contains a child gives 23 pairs:

  | `p` | children only | all 23 pairs |
  |---|---|---|
  | 13 | `0.9738` | `1.0469` |
  | 14 | — | `0.9241` |

  So for the full pair count the threshold is `p = 14`, not 13. The attempt's kernel is exact for pairs among the children, which is how it
  defines "descendant fork-pairs".

**Step 5 (atom-sum closure fails): holds** as a no-go for that method. G6:
- there are 7 fork pairs among the five predecessors;
- `A_r` is `10.10`, `10.25`, `12.18` and `12.74` at `p = 200, 84, 13, 11`;
- the `ε → 0` limit is 10, the number of configurations with `N_u, N_v ≥ 2`.

**The eroder: holds.** G7:
- each of the 9 base fork pairs gives one mid-level 1 and a top of 0;
- 32 of the 64 base masks force the top.

## Verdict

The partial claim survives, with the scope correction above.

`check.py` prints `HIT: confirmed - ...` and its SUMMARY line.
