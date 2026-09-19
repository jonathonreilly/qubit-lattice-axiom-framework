# lightcone-formation, attempt 3 (worker w-macbookpro90c72-j05f1, model grok-4.6)

Grok a2 did FSS on the doubled graph; a5 Dobrushin `β<3/7`; a6 reversibility and `{E,14−E}`. This attempt takes a different route: Peierls defect costs of `π=∏_x Z_x` on the six-axis menu, plus an exhaustive product-identity check on `C_3`.

## (1) The statement attempted

For six-axis `(p,1,2)`, the 7-stencil light-cone chain is reversible w.r.t. `π∝∏_x Z_x` (product identity exhaustive on `C_3` at `(5,1,2)`). On the `2×2×2` cube the unnormalized `π`-weight of a one-site antipodal or orthogonal flip is strictly smaller than that of a constant at `p=3,5,10,20`, and both ratios decrease in `p`. A Peierls cost is therefore already positive at `p=3`. This is not an infinite-volume ordered-phase theorem (`L=2` stencil degeneracy; no contour entropy bound) and does not redo FSS or Dobrushin.

## (2) Steps

**Step 1 — product identity (PROVED; CHECKED I.1).** `φ` is symmetric, the 7-stencil is undirected, so `∏_x ∏_{y∈N(x)} φ(s'_x,s_y)` is symmetric in `(s,s')`. Exhaustive on `C_3`, six-axis, `(5,1,2)`: all `6^6` pairs.

**Step 2 — cube defect ratios (CHECKED P).** `L=2` 7-stencil double-counts each graph neighbour. At `(p,1,2)`:

| p | antipodal-flip / const | orthogonal-flip / const |
|---|---|---|
| 3 | `2167007881/207594140625` | `28796658496/207594140625` |
| 5 | `7077735687223/341437969896529303` | `715012822753408/341437969896529303` |
| 10 | (strictly smaller; exact in the log) | (strictly smaller) |
| 20 | (strictly smaller) | (strictly smaller) |

Both families decrease in `p`. Six constants have equal weight at `p=5`.

**Step 3 — what this is not (PROVED as a boundary).** A positive single-site cost on a degenerate cube does not control large contours on `Z^3`. Sphere FSS (a2) and Dobrushin (a5) are other routes.

## (3) Where the route stops

**First failing step of a Peierls theorem: the contour sum on a nondegenerate torus.** `L=2` is not that torus.

## (4) What would finish it

One-flip ratios as a function of `p` on `(Z/4Z)^3` (nondegenerate 7-stencil) and a chessboard / Peierls entropy bound for `∏_x Z_x`.
