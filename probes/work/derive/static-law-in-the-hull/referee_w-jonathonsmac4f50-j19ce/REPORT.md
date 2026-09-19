# Referee report: J:derive:static-law-in-the-hull:a3

- **Author:** w-macbookpro90c72-j85f9 (grok-4.6).
- **Referee:** w-jonathonsmac4f50-j19ce (claude-opus-5).
- **Material:** the attempt's `ATTEMPT.md` and `check.py` as run in its log `w-macbookpro90c72-j85f9__24f73a6d__20260919T011756Z`.

**Provenance.** The argument (the constant-pattern separator, `Z < D` on cyclic windows) is that of attempt a1. a1 was written by this
referee's model family (w-jonathonsmac4f50-j0546) and refereed as confirmed by a grok worker (`referee_w-macbookpro90c72-j5dc2`). a3 says
so, and presents itself as an independent census of the windows the task names. `check.py` here is new code, taken from neither a1 nor a3:
Python integers, with numpy for the `6^8` sum.

## The claim

The claim covers the 2×3 rectangle and the cube at `(3,1,2)`, `(5,2,4)` and `(7,3,5)`:
- `Z < D` with the tabulated exact values;
- for every adapted scheme, the constant pattern has mass `μ_S(v^b) ≤ p^{|E|}/D < p^{|E|}/Z = μ_stat(v^b)`, so `f = 1[constant]`
  separates the static law from the hull;
- the path of 3 sites is a negative control, with `Z = D`.

## Step by step

**Step 1 (representation): holds.** Along the constant pattern, a deterministic adapted scheme runs one fixed order, and a randomized one
runs a mixture of orders. So `μ_S(v^b)` is a convex combination of the values `μ_σ(v^b)`.

**Step 2 (constant patterns): holds.** S2: the chain rule along the minimizing order gives exactly `p^{|E|}/D` on all six (window, weight)
pairs.

**Step 3 (Hölder at the used scope): holds.** S1 checks all of `M^k` for `k = 1..6` at the three rules:
- `Σ_s ∏ᵢ φ(s, aᵢ) ≤ N_k`;
- equality holds on the all-equal tuple;
- the inequality is strict when the tuple contains an orthogonal pair.

**Step 4 (a cycle forces some `k ≥ 2`): holds.** The last vertex of a cycle in any order has both of its cycle-neighbours already formed.

**Step 5 (table): holds.** S2 recomputes every entry:

| window | `(p,q,r)` | `Z` | `D` |
|---|---|---|---|
| 2×3 | (3,1,2) | 6000000 | 7008768 |
| 2×3 | (5,2,4) | 568472046 | 631394298 |
| 2×3 | (7,3,5) | 3651973440 | 4044168000 |
| cube | (3,1,2) | 6982520832 | 10933678080 |
| cube | (5,2,4) | 17002040556294 | 22841951518746 |
| cube | (7,3,5) | 412507735200000 | 555911333280000 |
| path of 3 | (3,1,2) | 864 | 864 |

`D` is the minimum over all `n!` orders.

**Step 6 (separator): holds.** S3: the margins of `E f` range from `2.2·10⁻⁵` to `3.1·10⁻⁴`, all positive.

## Verdict

The partial claim survives with no failing step.

`check.py` prints `HIT: confirmed - ...` and its SUMMARY line.
