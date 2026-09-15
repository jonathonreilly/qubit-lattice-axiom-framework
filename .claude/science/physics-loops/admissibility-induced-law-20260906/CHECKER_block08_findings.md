# Refuting pass — block 08 (supervisor-run, disjoint machinery; 2026-09-15)

Owner directive: no subagents. This pass is the supervisor's own refutation attempt with machinery disjoint from the runner's (`specs/supervisor_control_block08_refuter.py`, output in `.out.txt`); it is not an independent review and grants no review PASS.

## Load-bearing numbers recomputed by different routes

| item | runner's route | refuting route | result |
|---|---|---|---|
| Q2d: TV(`μ_{C_2} P_{C_2}`, `μ_{C_2}`) at (3,1,2) | the fraction transfer `P(w → v)` pushed forward from `μ_{C_2}` over 1296 × 1296 pairs | the cube law's marginal on the plane `x_1 = 1` by an integer-weighted enumeration of all 6^8 configurations (Q2a says the marginal is `μ P`) | `356696849/806187919680`, equal (R1) |
| Q4: `c_3` at (3,1,2) | fraction kernels; TV as half the ℓ¹ distance | integer `φ` products normalized per tuple; TV as the sum of positive parts | `27/110`, equal (R2) |
| Q3e: the stationary `2×2` plane law | exact Gaussian elimination on the 32-orbit quotient | power iteration of the quotient, 40 steps, from a point mass | agree to below `10^{-12}` in every orbit (R3) |
| Q4a: the path count `N(000, 111)` | multinomial `3!/(1!1!1!)` | explicit enumeration of monotone paths | `6` (R4) |
| Q1f: the third-difference criterion | the alternating product of `K_3` values | a genuinely pair-additive `F` as a control | alternating sum `0` (R5) |

## Attempts to refute the theorems (reasoning; nothing refuted)

- Q2a's "iff": the common factor `Π_{t ≥ 2} P_C` is strictly positive (positivity), so cancelling it is legitimate; the reduction is exact.
- Q2c's marginal argument: the sites of the corner square record only corner-square sites in both planes — true for the two-predecessor structure in-plane and the `x_1`-predecessor; the sum over the other sites of the new plane removes leaves in reverse order (they are maximal among the remaining sites of the new plane and have no successors in the old plane).
- Q3a: the contraction uses only that every entry is at least `δ_C > 0`; `ε = 6^{|C|} δ_C ≤ 1` because the uniform law is a probability; if `ε = 1` the chain is iid (constant rule).
- Q4a's induction: the bound `P(x ∈ D | past) ≤ c Σ_{z ∈ A_x} 1_{z ∈ D}` uses the maximal coupling and the triangle inequality along one-entry changes; the path identity `N(z, x) = Σ_{z' ∈ A_x} N(z, z')` is the last-step decomposition; both hold for sites with fewer than three predecessors (`c ≥ c_k`).
- Q4b's conditional independence: the level chain is Markov because every predecessor of a level-`t` site lies at level `t − 1` (`|x − e_i|_1 = |x|_1 − 1`); the disjointness of the cones follows from `z ≤ x, z ≤ y ⇒ z ≤ x∧y`; the oscillation bound counts descending monotone paths of length `|y|_1 − m` (at most `3^ℓ`).
- Q4c's series: `Σ_j C(n+j, n) x^j = (1 − x)^{−n−1}` for `|x| < 1` with `x = 2c`; paths from plane `n` to plane `0` have exactly `n` steps `−e_1`; in-plane steps `j ≥ 0` in two directions.
- Q4d(i): the boundary rays of `Q_a` are the only sites whose kernels differ between corners `a` and `a'`; a site at in-plane distance `d` from the rays has at most `2^ℓ` monotone paths of length `ℓ ≥ d` to them; the series `Σ_{ℓ ≥ d} (2c)^ℓ` converges for `2c < 1`.
- Q4e: the two-sided stationary chain is translation-invariant in `x_1` by stationarity and in-plane by uniqueness; the convergence of box laws combines Q3b (the plane chain error, rate `θ`) with the in-plane boundary influence.

## Findings

F1 (fixed before the census): the first draft of the runner's cube pass used the lcm of the individual normalizers as the common denominator; the per-configuration denominator is a product, so the correct common multiple is `6 Z_1^3 (lcm Z_2)^3 (lcm Z_3)` — the runner's own assertion `Σ W = L` caught it. F2 (fixed): the first draft of the note placed `(2, 1, 2)` on the region's boundary by misreading the control's `3c = 1/3`; all eight triples are inside. F3 (fixed): classical names appeared in the status block and in three theorem sections; moved to Prior art / Imports (runner F4). Nothing refuted in the theorems; verdict of this pass: PASS-NO-BLOCKER at the supervisor's own standard, pending the owner's independent review.
