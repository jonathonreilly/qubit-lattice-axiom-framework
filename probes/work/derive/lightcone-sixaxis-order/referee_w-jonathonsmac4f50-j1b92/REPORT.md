# Referee report: J:derive:lightcone-sixaxis-order:a3

- **Author:** w-macbookpro90c72-jc50a (grok-4.6).
- **Referee:** w-jonathonsmac4f50-j1b92 (claude-opus-5).
- **Material:** the attempt's `ATTEMPT.md` and `check.py` at sha `5077ddbb`, and its log.

`check.py` in this directory re-verifies every finite fact with independent code (exact integers and rationals).

## The claim

The attempt claims four things:
- (a) Synchronous light-cone formation with any symmetric pair weight is reversible with respect to `π = Π_x Z_x` on any
  undirected neighbourhood, whether or not the site itself is included.
- (b) `π` is invariant under signed axis permutations. On the `2×2×2` torus at `(3,1,2)`, a one-site antipodal flip and a
  `4 + 4` split are lighter than a constant, so the constants are local maxima of `π`.
- (c) The static law is a different interaction.
- (d) What "memory" means for a reversible chain.

No infinite-volume contour threshold is claimed.

## Step by step

**Step 1 (product identity): holds.** `Π_x Π_{y∈N(x)} φ(s'_x, s_y)` is symmetric in `(s, s')` on the 4-cycle, both for the
3-stencil (site included) and for the 2-stencil (site omitted). Z1 checks every third configuration against all 1296.

**Step 2 (detailed balance): holds.** On the two-site ring with stencil `{x, x ± 1}`, where the neighbour is counted twice,
the `36 × 36` kernel is stochastic, and `π(s)P(s → s') = π(s')P(s' → s)` holds for all 1296 pairs (Z2, exact).

**Step 3 (symmetry): holds.** `π` on the `2×2×2` torus with the 7-stencil is invariant under random signed axis
permutations, tested on 200 configurations. The six constants have equal weight (Z3).

**Step 4 (Peierls ratios on the cube): holds, and more broadly than stated.**
- The one-site antipodal flip has ratio exactly `2167007881/207594140625 ≈ 0.01044` (Z4).
- The attempt infers "local maxima" from two perturbations. Z4 checks all 40 single-site changes of a constant: their ratios
  lie in `[0.01044, 0.13872]`, all below 1. The `4 + 4` split has ratio `0.01192`.
- The constants are therefore local maxima under all single-site moves on this cube.
- The `L = 2` cube is degenerate (`±e_j` coincide), as the attempt says.

**Step 5 (memory for a reversible chain): holds** as a reading. On a finite torus the kernel is strictly positive, so it has
a unique stationary law, which it approaches from every start.

## Classic failure modes

None found:
- The infinite-volume threshold is explicitly not claimed.
- The `L = 2` degeneracy is stated.
- The "local maxima" statement, made from two perturbations, is confirmed for all single-site moves.

## Verdict

The partial result survives with no failing step.

`check.py` prints `HIT: confirmed - ...` and its SUMMARY line.
