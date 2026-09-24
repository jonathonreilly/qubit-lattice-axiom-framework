# Referee report: persistent sources, attempt 1

- **Author:** `w-jonathonsmac4f50-j89fe` (`claude-opus-5`).
- **Referee:** `w-macbookpro90c72-j3271` (`grok-4.6`). Different model family.
- **Checks:** own inverse of the killed 7-point operator on the 4-torus. The author's script is not called.

## The statement that survives

On the `4×4×4` torus, with the 7-point stencil and killing rate `1/10`, the Green matrix solves a collinear pinned line. For `n = 2, 3, 4` sources at value `1`, `c = M⁻¹ α` meets every pin and `(I−P)m` vanishes off the line.

At `n = 3` the charges are symmetric, and the interior source is strictly lighter than the ends: `0.447653871` against `0.528563241`. At `n = 4` the line wraps the torus, so there are no ends and all four charges are equal. The total charge rises with `n`, while the charge per source falls: `0.692647018` for one source, then `0.562325833`, `0.501593451` and `0.439033578`.

These are numbers of this killed finite torus, not of `Z³`. Two lengths are not a law for the infinite line.

## Steps

**1.** Each row of `A` sums to `1/10`. `A` and `G = A⁻¹` are symmetric on the sampled pairs.

**2.** Embedding `c` and applying `G` pins the chosen sites at `1`. Applying `A` returns `c` on those sites and `0` elsewhere.

**3.** The `n = 3` ends match and exceed the middle. The four `n = 4` charges match.

**4.** The totals increase and the per-source costs decrease, each below the isolated cost `1/G(0)`. The nine-decimal prints match the exact rationals.

## Verdict

The line solve survives. An interior source is screened more than an end, and on this torus a longer line is cheaper per site to hold at the same value. The `n = 4` row is a ring, not a longer open line.
