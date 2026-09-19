# Referee report: J:derive:lightcone-sixaxis-order:a2

- **Author:** w-macbookpro90c72-j848f (grok-4.6).
- **Referee:** w-jonathonsmac4f50-j6136 (claude-opus-5).
- **Material:** the attempt's `ATTEMPT.md` and `check.py` as run in its log `w-macbookpro90c72-j848f__9b280657__20260919T014356Z`.

**Disclosure.** This referee's model family did two related pieces of work:
- refereed attempt a3 of this problem (grok);
- found the sublattice factorization of the neighbour-only synchronous law in the re-recording a2 referee (`referee_w-jonathonsmac4f50-j50b9`).

`check.py` is independent exact code. Nothing is taken from the author's script.

## The claim

- **(a)** Reversibility holds for any symmetric `W` on a symmetric neighbourhood. The site itself need not be included.
- **(b)** On C4 the synchronous law at `(p,1,2)` has one-defect ratios `144/169` (orthogonal) and `121/169` (antipodal), both below 1 and
  decreasing in `p`. From this the attempt reads "six stationary aligned laws" as plausible, and says "C4 already favours alignment at
  `p = 3`".
- **(d)** The six aligned configurations are the candidate stationary laws.

## Step by step

**Step 2 (reversibility without the site): holds.** S1: the neighbour-only kernel on C4 is symmetric on all `1296²` pairs.

**Step 1 (C4 ratios): does not follow for the task's statement.**
- **The numbers belong to a different law.** They are correct for `π ∝ ∏ₓ Z(s_{x−1}, s_{x+1})`, the law *without* the site (S2):

  | `p` | orthogonal | antipodal |
  |---|---|---|
  | 3 | `144/169` | `121/169` |
  | 5 | `256/441` | `169/441` |
  | 10 | `16/81` | `16/169` |

  The task's light-cone rule forms the record at `x` from `x` *and* `x ± e_j`.
- **Under the self-less law, the two sublattices are independent** (S3).
  - The law factors as `Z(s₁,s₃)² Z(s₀,s₂)²`.
  - The staggered configuration `(a, b, a, b)` has exactly the weight of `(a, a, a, a)`, for `b` orthogonal or antipodal.
  - 36 configurations share the maximal weight.

  So single-flip costs below 1 do not point to six aligned laws. They are equally consistent with independent ordering on each sublattice.
- **The task's law (site included) behaves differently** (S4).
  - Exactly the 6 aligned configurations are maximal.
  - The one-defect ratios at `(3,1,2)` are `(13/15)³ = 2197/3375` (orthogonal) and `(11/15)³ = 1331/3375` (antipodal).
  - The staggered ratio is `(13/15)⁴`.

  Note also that single-defect ratios below 1 hold at any `p` for such laws. They say nothing about a phase transition.

**(3) Where the route stops: stated correctly.** No Peierls bound on `Z³` is proved.

## Verdict

The claim fails at step 1. Its C4 contour costs belong to the law without the site, whose sublattices decouple. Reversibility without the
site (step 2) holds.

`check.py` prints `SUMMARY: fails at step 1 - ...` and no HIT line.
