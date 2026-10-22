---
claim_id: the_tied_lapse_leaves_the_shift_free_a_geometry_only_momentum_constraint_excludes_moving_sources_and_minimal_strain_fixes_the_shift_bounded_theorem_note_2026-10-22
claim_type: bounded_theorem
claim_scope: "For the update law's fixed-step lapse (linearised: h_00 = -h_kk/3) and edge registers: in linearised GR on flat space the tied lapse leaves a 3-dimensional gauge kernel (spatial displacements with a compensating time relabelling) whose shift projection has rank 3 at every sampled (omega, k), so stationarity of the total phase in the shift fixes no shift; the shift-shift block has rank 2 and the shift equation is the momentum constraint; for a moving dust source G_0i = 8 pi T_0i != 0, so a momentum constraint built from the edges alone, with odds invariant under every edge displacement, forces T_0i = 0. On finite edge registers the displacement shift is a partial isometry with no nonzero invariant odds (a cyclic shift has some, but wraps lengths); with invariance read where both ends lie in the window, a single edge value is not gauge-invariant; a pure corner displacement lengthens all 18 edges of a cube and changes the fixed-step lapse at first order. For Oppenheimer-Snyder collapse from rest at R0: with matter on labels the dust surface's tangential edge shrinks as R_b/R0 on every slicing; with matter allowed to move through the labels, a Painleve-Gullstrand-type grid (Schwarzschild slices checked symbolically, glued to the closed FRW interior) keeps every edge in [l0, l0/E], inside [L/8, 2L] whenever R0 > 1.004 r_s, until the shift saturates at R_sat/r_s of order 1e-5 to 1e-3 deep inside the horizon. In linearised form the minimal-strain shift removes exactly the displacement part of the edge rate and fixes the shift uniquely at each sampled generic k. Supplied model, finite diagnostic: linearised GR and continuum OS in place of register dynamics, supplied register sizes and grids; no CL-1 tick under the full generator, no register-level collapse."
upstream_dependencies:
  - minimal_axioms
  - candidate_laws
runner: scripts/the_tied_lapse_leaves_the_shift_free_a_geometry_only_momentum_constraint_excludes_moving_sources_and_minimal_strain_fixes_the_shift_2026_10_22.py
---

# The tied lapse leaves the shift free, a geometry-only momentum constraint excludes moving sources, and minimal strain fixes the shift

Claim type: bounded_theorem.
Primary runner: `scripts/the_tied_lapse_leaves_the_shift_free_a_geometry_only_momentum_constraint_excludes_moving_sources_and_minimal_strain_fixes_the_shift_2026_10_22.py`.

The [candidate-law register](CANDIDATE_LAWS.md) has zero premise weight. Its update law (CL-1 in the three-law numbering) fixes the lapse by one step eps0 read from each cube's edges, and its response law (CL-3) defines the edges' momentum constraint as the generator of a site's displacement: the edge-register shift that changes each edge at the site by the flat projection of one common displacement. This note asks what then fixes the shift, whether edge-register values are gauge-invariant, whether a momentum constraint built from the edges alone admits moving matter, and whether gravitational collapse keeps a representative inside the edge window [L/8, 2L] up to the horizon. The [minimal axioms](MINIMAL_AXIOMS_2026-06-29.md) fix none of the inputs used here.

## Statement

A. Linearised GR on flat space with the fixed-step lapse (Bona-Masso f = 1/3: dN/N = h_kk/6, h_00 = -h_kk/3).

1. The tied lapse does not fix the spatial gauge: at every sampled (omega, k) the action on (h_ij, beta_i) has a kernel of exactly 3, the spatial displacements with a compensating time relabelling, and its shift projection has rank 3. Every shift is a stationary shift of some edge history, so "the shift at which the total phase is stationary" fixes nothing.
2. Given the edge history, the shift-shift block has rank 2 (K_ij K^ij - K^2 is blind to a longitudinal shift), and the shift equation is the momentum constraint G_0i = 8 pi T_0i, which constrains the edges and the shift together.
3. For a moving dust source the linearised solution has G_0i = 8 pi T_0i != 0. A momentum constraint built only from the edges is the geometry part of G_0i, so requiring the odds to be invariant under every edge displacement forces T_0i = 0: it excludes the field of every moving mass, in every gauge. The momentum constraint must include matter.

B. Edge registers: the displacement shift as an operator (one site, four registers of 6 values: the +x and -x axis edges, which move two steps per unit displacement, and two diagonals, which move one step).

4. On finite registers the displacement shift is a partial isometry, and the only odds invariant under it are zero (iterate psi = S^k psi until a raised edge leaves the window). A cyclic shift has invariant odds but wraps a length from the top of the window to its bottom. So "only odds invariant under every such shift occur" is empty as written on finite registers.
5. With the invariance read only where both ends of a gauge step lie in the window, physical odds are functions on orbit segments. A single edge value, and "an edge at the floor", is not gauge-invariant: imposing the constraint spreads it, while displacement-invariant combinations (here n_+x + n_-x) are constant on each segment.
6. Moving a cube's 8 corners outward, a pure displacement with no curvature, lengthens all 18 of its edges (12 axis edges and 6 face diagonals), so the split trigger and the floor are reachable by gauge alone; and displacing one corner changes the fixed-step lapse at first order, so the lapse ties the slicing to the spatial gauge.

C. Oppenheimer-Snyder collapse from rest at R0 (E^2 = 1 - r_s/R0).

7. With matter fixed on labels (the edge-only generator), the dust surface keeps its label sphere and its areal radius R_b is a spacetime scalar, so for unwrinkled representatives its mean tangential edge is l0 R_b/R0 on every slicing; it meets L/8 before R_b = r_s iff R0 > 8 (l0/L) r_s, so for every far phase once R0 > 16 r_s. (Stated in the runner; the phase fractions below are evaluated from this formula.)
8. With matter allowed to move through the labels (the full generator), the T = const slices of ds^2 = -dT^2 + E^-2 (dr + V dT)^2, V^2 = 2M/r - 2M/R0, are Schwarzschild, glued to the dust proper-time slices of the closed FRW interior. On a static areal grid gamma_RR = 1/E^2 outside and 1/(1 - R^2 sin^2 chi0/R_b^2), in [1, 1/E^2], inside, so every edge stays in [l0, l0/E] at every tick: inside [L/8, 2L] whenever 1/E <= 16, that is R0 > 1.004 r_s.
9. This grid stays static until the shift needs more than one cube per tick (sin 2 theta = 1), at R_sat of order (2/3) sin^2(eps0) M, deep inside the horizon.
10. The fixed step on this grid gives N = sqrt(3/(2 + 1/gamma_RR)) times a constant: uniform outside, a rescaled Painleve-Gullstrand tick, and inside rising over the dust proper-time lapse by at most sqrt(3/(2 + E^2)) - 1, of order r_s/(6 R0); exact for marginally bound collapse (E = 1).

D. The minimal-strain shift (Smarr-York).

11. The minimal-strain shift, the least sum of squared edge rates, removes exactly the displacement part of the edge motion and leaves the rate orthogonal to every displacement; at each sampled generic k it fixes the shift uniquely. (Uniqueness up to Killing motions, and zero strain on the marginally bound grid of item 8, are stated, not computed.)
12. With the full generator imposed and the shift fixed by minimal strain, the shift is still the multiplier of the momentum constraint (item 2), so the constraint holds and the gauge is fixed, not broken; the condition is elliptic, so the shift is nonlocal within a slice but, being gauge, carries no signal. (Stated in the runner, not computed.)

## Derivation

Items 1 and 2 build the linearised Einstein operator as a 10 x 10 quadratic form at six random (omega, k), restrict it to (h_ij, beta_i) with h_00 = -h_kk/3, and compute kernel dimensions and ranks by singular values; each displacement with the compensating time relabelling is checked to lie in the kernel. Item 3 takes a dust source with velocity (0.3, 0.1, 0), chooses omega so k.u = 0, solves the harmonic-gauge equation and compares G with T. Items 4 and 5 build the shift on the 1296 joint register states, count the invariant subspace, merge states into orbit segments by union-find, and project a product state centred mid-window onto segment functions. Item 6 fits gamma to a cube's 18 edges by least squares and differentiates the lapse numerically. Item 8 checks the three metric components with sympy (exact simplification) and evaluates the interior gamma_RR on 201 points. Item 9 finds R_sat by bisection on the per-tick block-rotation limit. Item 11 solves the least-squares shift for five random wavevectors with random displacement, transverse-traceless and transverse-trace parts.

## Finite checks

Exact or closed-form checks (the runner asserts each):
- Gauge kernel dimension 3 and its shift-projection rank 3 at all six sampled (omega, k); shift-shift block rank 2 at all six.
- Moving source: G = 25.1327 T (8 pi, asserted below 1e-9); |G_0i|/|G_00| = 0.316 = |T_0i|/|T_00| = 0.316.
- Register shift: invariant dimension 0 for the truncated shift, 216 of 1296 for the cyclic shift.
- Orbit segments: 336 segments with more than one state; n_+x + n_-x constant on each, n_+x never; projection raises var(n_+x) from 0.26 to 2.90; the projected state has probability 0.67 of an edge within one step of the floor.
- Pure displacement: all 18 edges grow; d ln N/du = 0.0278 per cube edge.
- Painleve-Gullstrand-type slices: the three Schwarzschild components agree exactly (sympy); interior maximum of gamma_RR equals 1/E^2 (below 1e-12); 1/E = 1.732, 1.225, 1.054, 1.005, 1.000 at R0/r_s = 1.5, 3, 10, 100, 1e5.
- Minimal strain: shift recovered equal to the displacement to 1e-10 at five random k, residual orthogonal to every displacement; residual rate fractions (the gauge-invariant transverse-traceless and trace parts) 0.43, 0.54, 0.31, 0.59, 0.38.

Finite diagnostics (supplied model, finite diagnostic, no physical identification):
- Matter on labels, floor reached first at a fraction of window phases (phases uniform in log l0, from the formula of item 7): R0/r_s = 10: 32%; 16, 100, 1e5: 100%.
- Shift saturation radius R_sat/r_s: eps0 = 0.0075: 2.4e-05 (R0/r_s = 1.5), 1.9e-05 (10), 1.9e-05 (1e5); eps0 = 0.0375: 6.0e-04, 4.8e-04, 4.7e-04.
- Fixed-step lapse rise inside, sqrt(3/(2 + E^2)) - 1: 0.1339, 0.0607, 0.0171, 0.0017 at R0/r_s = 1.5, 3, 10, 100.

## Boundary

Supplied: linearised GR (sections A and D) and continuum Oppenheimer-Snyder collapse (section C) in place of register dynamics; the Bona-Masso form of the fixed-step lapse; the four-register one-site toy with 6 values each; unwrinkled representatives in item 7 and a log-uniform measure over window phases; the Martel-Poisson form of the Painleve-Gullstrand-type coordinates; eps0 in 0.0075 to 0.0375. Forced, given those: the 3-dimensional gauge kernel left by the tied lapse; the rank-2 shift block and the shift equation as the momentum constraint; T_0i = 0 for a geometry-only constraint; the absence of invariant odds under the truncated shift; the gauge variance of single edge values; the growth of all cube edges under a pure displacement; the Painleve-Gullstrand-type grid's edge range [l0, l0/E]; the least-squares uniqueness of the minimal-strain shift at the sampled k. Not claimed: the update law's tick under the full generator; a register-level collapse; the block-pair rotation current as matter translation; behaviour after the shift saturates; uniqueness of minimal strain as the register's gauge condition; any statement beyond linear order in sections A and D.

## Dependencies

- [Minimal axioms](MINIMAL_AXIOMS_2026-06-29.md): Z^3 sites, one qubit per site, nearest-neighbour admissibility, records. They fix none of the supplied inputs above.
- [Candidate-law register](CANDIDATE_LAWS.md): the update law's fixed-step lapse, edge registers, window and split trigger, and the response law's momentum constraint as a displacement generator. Zero premise weight; results using it are conditional on it.

## How to run

```
python3 scripts/the_tied_lapse_leaves_the_shift_free_a_geometry_only_momentum_constraint_excludes_moving_sources_and_minimal_strain_fixes_the_shift_2026_10_22.py
```

Needs numpy and sympy. It is self-contained, declares `AUDIT_TIMEOUT_SEC = 120`, runs in about 1 s with about 150 MB resident, prints about 5.9 kB and ends with `TOTAL: PASS=12 FAIL=0`. Its random draws are seeded; two repeated runs gave identical output apart from the elapsed-time line.
