---
claim_id: with_the_wave_shift_the_collapse_floor_stays_inside_horizons_and_the_edge_top_needs_delta_at_least_one_bounded_theorem_note_2026-10-22
claim_type: bounded_theorem
claim_scope: "In linear theory on flat space with the update law's tied lapse n = tr h / 6 and Newtonian potential Phi = Psi (G = c = 1, symbolic): the wave shift d_t^2 beta = mu (Lap beta - 16 pi j) is, in the scalar sector, beta = grad phi with phi_tt = mu Lap phi + 4 mu dPhi/dt, sourced by the potential's rate; the mean log edge equals Phi at quasi-static order for both the zero and the wave shift, the wave shift changing the departure from -Psi by the factor (mu k^2 + (2 mu - 1) w^2) / (mu k^2 - w^2); on a flat slice the Painlevé-Gullstrand shift sqrt(2M/r) leaves the residual -(9/4) sqrt(2M) r^(-5/2) and the stationary radial vacuum shifts are a r + Q / r^2, so the wave law has no stationary Painlevé-Gullstrand state; since the tied lapse gives l_min <= N on every cube, a static zero-shift exterior with N = sqrt(1 - 2M/R) puts an edge at the floor 2^(-3-m) by R = 2M / (1 - 4^(-3-m)) = 2.032, 2.0157, 2.0078 M (m = 0, 0.5, 1), outside the horizon. In nonlinear spherically symmetric ADM collapse of a smooth dust ball from rest (R0 = 5 and 10 Schwarzschild radii, mu = 3/4, grids h = 0.1 and 0.05) up to the crunch of the core: no edge outside the trapped surface comes near the floor (smallest exterior tangential edge 0.51 and 0.52 with the wave shift, 0.37 and 0.38 with zero shift, against 1/8); the only floor crossing is in the crushing core inside the trapped surface with zero shift; the wave shift points outward, reaches 0.25 at R = 2M and has the exterior form Q / r^2 with Q = 4.1-4.4 M^2; the one-cube-per-tick cap is not approached (largest b 0.0052 and 0.0261 for eps0 = 0.0075 and 0.0375); the largest exterior radial edge (1.22-1.97) passes the top 2^(1 + Delta - m) for 29-98% of phases m at Delta = 0 and for none at Delta = 1, so Delta >= 1 is needed. The exterior after the core crunch is not followed. Supplied model, finite diagnostic: ADM as the response law's continuum limit, the dust profile, M = 1, the on-shell source form, the flat-label vector Laplacian as nonlinear completion, mu = 3/4, the grids, dissipation and run lengths, and the floor and top values."
upstream_dependencies:
  - minimal_axioms
  - candidate_laws
runner: scripts/with_the_wave_shift_the_collapse_floor_stays_inside_horizons_and_the_edge_top_needs_delta_at_least_one_2026_10_22.py
---

# With the wave shift the collapse floor stays inside horizons, and the edge top needs Delta at least one

Claim type: bounded_theorem.
Primary runner: `scripts/with_the_wave_shift_the_collapse_floor_stays_inside_horizons_and_the_edge_top_needs_delta_at_least_one_2026_10_22.py`.

The [candidate-law register](CANDIDATE_LAWS.md) has zero premise weight. Its edge registers run from an eighth of the flat length to 2^(1+Delta) times it, and its gravity sector reads edges in a frame fixed by the shift, for which the register carries the undamped wave shift, sourced by the momentum constraint. A static, zero-shift reading of a black-hole exterior drives an edge to the floor outside the horizon. This note asks whether that happens in dynamical collapse with the wave shift, and what the binding register wall is outside the horizon. The [minimal axioms](MINIMAL_AXIOMS_2026-06-29.md) fix none of the inputs used here.

## Statement

A. Linear theory, exact (sympy), on flat space with the tied lapse n = tr h / 6 and the Newtonian potential Phi = Psi.

1. Shift sourced by the potential's rate. From d_t^2 beta = mu (Lap beta - 16 pi j), continuity Lap psi = -rho_t (j = grad psi) and Poisson Lap Phi = 4 pi rho, the scalar sector is beta = grad phi with phi_tt = mu Lap phi + 4 mu dPhi/dt. Infalling momentum density sources the shift through the rate of the potential. The runner states that the sign is outward for infall, the Painlevé-Gullstrand sign.
2. Edges follow the potential. The mean log edge, tr h / 6, tends to Phi at quasi-static order (w -> 0) for both the zero shift and the wave shift: edges follow the potential, not the dust. The wave shift changes the departure from -Psi by the factor (mu k^2 + (2 mu - 1) w^2) / (mu k^2 - w^2), which is 1 + O(w^2 / k^2).
3. No stationary Painlevé-Gullstrand state. The Painlevé-Gullstrand grid (flat slices, N = 1, beta^r = sqrt(2M/r)) is not stationary for the wave law. On a flat slice the radial vector Laplacian of sqrt(2M/r) is -(9/4) sqrt(2M) r^(-5/2), and the stationary radial vacuum shifts are a r + Q / r^2. The runner states, and does not compute, that the constraint part vanishes for a radial shift on a flat slice.
4. Static exterior meets the floor outside 2M. The tied lapse is N^2 = 3 / sum_i l_i^(-2) (edges in far-edge units), so l_min <= N on every cube. A static zero-shift exterior (static slicing, N = sqrt(1 - 2M/R)) therefore has an edge at the floor 2^(-3-m) by the radius R = 2M / (1 - 4^(-3-m)), outside the horizon.

B. Nonlinear spherical collapse, finite diagnostic. A smooth dust ball (tanh edge of width 6% of its radius, ADM mass M = 1) collapses from rest at areal radius R0 = 10 or 20 M, in regularised spherically symmetric ADM with the tied lapse, and either zero shift or the wave shift d_t^2 beta^r = mu [Lap_flat beta^r - 16 pi S^r] with mu = 3/4. Edges are in far-edge units, and a trapped surface marks the apparent horizon.

5. Through apparent-horizon formation and up to the crunch of the core, no edge outside the trapped region comes near the floor, for either shift. The first floor crossing is in the crushing core inside the horizon (zero shift), and with the wave shift no edge reaches the floor before the run ends. The runner states that the tied lapse (Bona-Masso f = 1/3) is not singularity-avoiding, which is why the core crunches.
6. The wave shift points outward, raises the smallest exterior tangential edge and lowers the largest exterior radial edge relative to zero shift, and reaches 0.25 at R = 2M (the runner sets this against a Painlevé-Gullstrand value of about 0.95, stated). Outside the matter it takes the stationary form Q / r^2.

C. Estimates.

7. The one-cube-per-tick cap b = beta sin(eps0) / sqrt3 is not reached anywhere up to the crunch.
8. The binding wall outside the horizon is the top, not the floor: radial edges stretch while tangential ones shrink, with no glued split. With far edges at 2^m times the flat length, m in [0, 1), the top 2^(1 + Delta - m) is passed for a fraction log2(l_r) - Delta of phases m. At Delta = 0 that is a large fraction in every run; at Delta = 1 it is none.
9. The quasi-static Newtonian shift charge Q = (4/5) M R_b |dR_b/dt| is about 1.6 M^2 at R_b = 2M, against the measured exterior r^2 beta of about 4 M^2: agreement in order of magnitude only.

## Derivation

Items 1 and 2 solve the linear Fourier equations (d_t -> -i w, Lap -> -k^2) with sympy: the shift from continuity and Poisson, and the edges by gauge transformation from Newtonian gauge (n = Phi - T', beta = grad(T - L'), h_ij = -2 Psi delta_ij - 2 d_i d_j L) under the tied lapse. Item 3 applies the radial vector Laplacian symbolically. Item 4 checks l_min <= N on 2000 seeded random edge triples and evaluates the closed-form radii. Items 5-6 integrate the spherically symmetric ADM equations (metric functions A, B, extrinsic curvatures K_A, K_B, the regularisation variable lambda, the shift and its rate, conserved dust density and radial momentum) with fourth-order differences, RK4 (dt = h / 4), Kreiss-Oliger dissipation 0.1 and upwind MUSCL dust transport. The initial data are conformally flat and time-symmetric. A run ends at 1.6 free-fall times or when an edge falls below 1/20. Items 7-9 evaluate closed forms on the run data.

## Finite checks

Symbolic checks (the runner asserts each): the shift equation of item 1; the departure factor of item 2 and both quasi-static limits Phi; the residual -9 sqrt(2) sqrt(M) / (4 r^(5/2)) of item 3, and that a r + b / r^2 are stationary. Item 4: l_min <= N on 2000 seeded draws; floor radii 2.032, 2.0157 and 2.0078 M for m = 0, 0.5 and 1.

Collapse runs (supplied model, finite diagnostic). R0 is given in Schwarzschild radii r_s = 2M; "outside AH" means outside the outermost trapped surface at the run's end:

| run | R0 | shift | h | AH at t (R_AH) | run ends | exterior l_t min (R) | exterior l_r max (R) | all edges | beta(2M) | max beta | r^2 beta | floor 1/8 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| z10 | 5 r_s | zero | 0.10 | 38.5 (1.95 M) | 42.0 | 0.371 (2.06) | 1.968 (2.28) | 0.060-1.968 | 0.00 | 0.00 | 0.0 | t 42.0 at R 0.04-0.27 M, inside AH |
| w10 | 5 r_s | wave | 0.10 | 37.5 (1.92 M) | 39.0 | 0.509 (2.06) | 1.326 (3.93) | 0.419-1.326 | 0.23 | 1.21 | 3.6-5.0 | none |
| w10f | 5 r_s | wave | 0.05 | 37.5 (1.93 M) | 39.0 | 0.503 (2.00) | 1.322 (3.95) | 0.348-1.322 | 0.22 | 0.98 | 3.6-5.0 | none |
| z20 | 10 r_s | zero | 0.10 | 108.5 (1.82 M) | 111.0 | 0.381 (2.00) | 1.646 (2.70) | 0.171-1.646 | 0.00 | 0.00 | 0.0 | none |
| w20 | 10 r_s | wave | 0.10 | 107.0 (1.81 M) | 108.0 | 0.521 (2.00) | 1.222 (5.09) | 0.381-1.222 | 0.25 | 0.75 | 4.1-4.4 | none |

- Consistency: the runner asserts the exterior momentum-constraint residual at the final snapshot below 3e-3 (the value is not printed), and grid agreement of the exterior edge extremes, l_t 0.509 against 0.503 and l_r 1.326 against 1.322. The prose says agreement to 0.01; the assertion tolerance is 0.02 for l_t and 0.03 for l_r.
- Smallest exterior tangential edge: wave 0.51 and 0.52, zero 0.37 and 0.38 (R0 = 5 and 10 r_s); asserted above 0.3 with no floor crossing outside the trapped surface.
- The wave shift raises the smallest exterior l_t and lowers the largest exterior l_r relative to zero shift in both pairs (asserted); the runner's "halves the slice stretching" is a reading of these numbers. In run w20, beta(2M) = 0.25 (asserted between 0 and 0.5) and Q = r^2 beta = 4.1-4.4 M^2 at r = 3, 5 and 10.

No unseeded random draws.

## Estimates against measurement

These compare with the register's own walls, not with measured data.
- Cube cap: largest b = 0.0052 at eps0 = 0.0075 and 0.0261 at eps0 = 0.0375 (asserted below 0.1), using the largest shift over all runs.
- Top fraction, log2(l_r) - Delta clipped to [0, 1]:

| run | largest exterior l_r | Delta = 0 | Delta = 1 |
|---|---|---|---|
| w10 | 1.33 | 41% | 0% |
| w20 | 1.22 | 29% | 0% |
| z10 | 1.97 | 98% | 0% |
| z20 | 1.65 | 72% | 0% |

- Shift charge: the Newtonian estimate 1.6 M^2 against the measured 4.4 M^2, ratio 2.7 (asserted between 1 and 5); labels r > R, strong field, order of magnitude only.

## Boundary

Not claimed: the exterior after the core crunch (late-time slice stretching), which the runs do not follow; register-level odds; non-spherical collapse; the nonlinear completion of the wave shift beyond the flat-label vector Laplacian; the geometric (constraint) form of the wave source, which the runner states is origin-unstable in this code and replaces by the on-shell matter form; the outward sign of item 1, the flat-slice constraint statement of item 3 and the Painlevé-Gullstrand comparison value of item 6 (stated); convergence beyond the two-grid comparison; that Delta >= 1 suffices after the crunch; any experimental exclusion.

## Supplied vs forced

Supplied: ADM general relativity as the response law's continuum limit; the tied lapse; the wave shift with mu = 3/4 and its on-shell source form; the flat-label vector Laplacian; the smooth dust ball (tanh edge 6%), M = 1 and R0 = 10, 20 M; the grids h = 0.1, 0.05, the time step, the dissipation 0.1 and the stopping rules; the floor 2^(-3-m), the top 2^(1+Delta-m) and the far-edge phase m; eps0 = 0.0075 and 0.0375. Forced, given those: the shift sourced by the potential's rate; edges following the potential at quasi-static order for both shifts; no stationary Painlevé-Gullstrand state of the wave law; l_min <= N and hence a floor edge just outside 2M in a static zero-shift exterior; in the runs, exterior edges well above the floor up to the crunch, the outward shift with exterior Q / r^2 form, an unapproached cube cap, and an exterior radial edge that passes the top at Delta = 0 but not at Delta = 1.

## Dependencies

- [Minimal axioms](MINIMAL_AXIOMS_2026-06-29.md): Z^3 sites, one qubit per site, nearest-neighbour admissibility, records. They fix none of the supplied inputs above.
- [Candidate-law register](CANDIDATE_LAWS.md): the update law's tied lapse and one-cube-per-tick shift cap, the edge registers' range from an eighth of the flat length to 2^(1+Delta) times it, and the response law's wave shift sourced by the momentum constraint, with general relativity as its continuum limit. Zero premise weight; results using it are conditional on it.

## How to run

```
python3 scripts/with_the_wave_shift_the_collapse_floor_stays_inside_horizons_and_the_edge_top_needs_delta_at_least_one_2026_10_22.py
```

Needs numpy, scipy and sympy. It is self-contained, declares `AUDIT_TIMEOUT_SEC = 120`, runs in about 24 s with about 290 MB resident, prints about 5.1 kB and ends with `TOTAL: PASS=11 FAIL=0`. Its random draws use a fixed seed; two runs gave identical output apart from the elapsed-time line.
