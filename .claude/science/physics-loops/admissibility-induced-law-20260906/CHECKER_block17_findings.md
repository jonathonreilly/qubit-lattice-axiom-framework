# Refuting pass — block 17 (supervisor-run, disjoint machinery; 2026-09-15)

Routes compared (control `specs/supervisor_control_block17_static_order.py`, refuting pass `specs/supervisor_control_block17_refuter.py`, outputs in `.out.txt`):

| item | runner's route | refuting route | result |
|---|---|---|---|
| reflection positivity (T2) | the direct expectation `E[F · F∘θ]` for pseudo-random `F` | the explicit sum-of-squares decomposition `Z E[F F∘θ] = Σ_{v_P} W_P G(v_P)²` computed as such, on the ring at `(3,1,2)` and `(5,2,4)` | equal, nonnegative |
| the chessboard instance (T3) | `P(two bonds bad)² ≤ P(all bad)` on the ring | the two-step quadratic-form form through the *other* site plane: `P(A_0 ∩ A_2)² ≤ P(A_0 ∩ θA_0) P(A_2 ∩ θA_2)` and each of those squared `≤ P(all bad)` | both steps hold |
| the enclosing-cycle counts (T5) | self-avoiding closed dual walks | polyomino placements (translations times orientations) of the polyominoes of perimeter `4, 6, 8` | equal: `1, 4, 22` |
| the series (T5, T7) | closed forms symbolically | exact partial sums to `400` terms at `y = 1/2` and `y = 4/5` | agree to `10^{−30}` |
| the three-dimensional counts (T7) | the twelve-neighbour adjacency | a second implementation from the common-unit-square criterion | equal: `1, 12, 158, 2148` |

Findings (all fixed before the census):
- **F1 (fixed).** The runner's first expected count of enclosing dual cycles of length six was `2`; the domino has two orientations and the count is `4` (within the bound `(n/2)3^{n−1} = 729`); the refuting route by polyomino placements confirmed `1, 4, 22`.
- **F2 (fixed).** The three-dimensional threshold `p_0 = 6m/ε = 34,992,000 m` was first checked against its per-`m` value instead of `69,984,000` at `m = 2`.
- **F3 (fixed).** Three tokens the lane forbids as substrings appeared in the note ("converges", "dominated convergence", "sharp thresholds"); reworded.
- **F4 (fixed, in the refuting pass itself).** The first second-adjacency routine counted the two collinear bonds as neighbours (14 instead of 12); corrected to the common-unit-square criterion.

Attempts to refute (nothing refuted): T2 was re-read for bonds lying inside the fixed plane (assigned to the plane weight, so they do not break the factorization); T3 for a cell whose two canonical bonds are both in the set (the joint event's disseminated version is contained in the single-bond one); T5's case (b) for the length of a separating boundary-to-boundary dual path (the lattice path inside the box `|·|_∞ ≤ L'/2` forces at least `L'/2` steps from the boundary and back); T6 (iv) for the use of the value symmetry (the unique state is symmetric because the image of a Gibbs state under a symmetry of `φ` is a Gibbs state, hence the same state). Verdict of this pass: PASS-NO-BLOCKER at the supervisor's own standard, pending the owner's independent review; the three-dimensional statement remains conditional on the named lemma.
