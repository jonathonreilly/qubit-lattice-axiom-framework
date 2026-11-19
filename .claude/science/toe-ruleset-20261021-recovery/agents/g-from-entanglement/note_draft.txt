---
claim_id: the_cube_tick_seas_entanglement_is_blind_to_the_conformal_factor_so_a_jacobson_g_from_it_has_no_newtonian_part_and_exceeds_the_hinge_sum_g_bounded_theorem_note_2026-10-22
claim_type: bounded_theorem
claim_scope: "For the half-filled sea of the update law's cube tick (one fermion mode per site, face phase -1), with each cube's hop normalised to R^2 = 1 and hop weights sqrt(gamma^ii): a cube-wise common rescaling of the edges (any spatial conformal factor) leaves every half-tick, and so the vacuum and all its entanglement entropies, exactly unchanged while proper areas change (8^3 torus, random factors over the edge window [1/8, 4]: |dS| = 3.6e-13). The vacuum entropy is therefore not eta times proper area, and a Jacobson-type coupling 1/(4G) = dS/dA built on it has no response to the conformal (Newtonian) mode. The first law dS = d<K> holds as an identity (ratio 0.997 at d = 1e-3, relative-entropy remainder positive and quadratic) and imposes no equation by itself. Finite diagnostics: the planar (100) area coefficient of the pi-flux sea, the tick's eps0 -> 0 limit (corrections ~eps0^2, 4.3e-4 at eps0 = 0.0375), is eta_100 = 0.196645 nats per site^2 (exact torus identity with the transverse-momentum chain sum to 1e-10; cubes l = 3..8 give 0.1966); lattice balls give 0.229 per geometric area (orientation dependent); transverse stretching gives dlnS/dlnA = 0.457, area-preserving normal stretching dlnS = -0.911 eps, fixed-volume dS/dA = 0.2695. Estimates: with a two-scalar photon (0.0485) and the copy-mass factor (<= 1.71), G = 1/(4 eta) is 4.7 to 8.0 times the hinge-sum G under the unit map's cell-rung reading (19 to 32 under the site reading). Supplied model, finite diagnostic: pi-flux sea and cube tick at eps0 = 0.0375, hop = 1/length, planar and lattice-ball cuts, photon as two lattice scalars; rishon and edge-register entanglement omitted."
upstream_dependencies:
  - minimal_axioms
  - candidate_laws
runner: scripts/the_cube_tick_seas_entanglement_is_blind_to_the_conformal_factor_so_a_jacobson_g_from_it_has_no_newtonian_part_and_exceeds_the_hinge_sum_g_2026_10_22.py
---

# The cube tick sea's entanglement is blind to the conformal factor, so a Jacobson G from it has no Newtonian part and exceeds the hinge-sum G

Claim type: bounded_theorem.
Primary runner: `scripts/the_cube_tick_seas_entanglement_is_blind_to_the_conformal_factor_so_a_jacobson_g_from_it_has_no_newtonian_part_and_exceeds_the_hinge_sum_g_2026_10_22.py`.

The [candidate-law register](CANDIDATE_LAWS.md) has zero premise weight. Its response law (CL-3 in the three-law numbering) carries the hinge sum with coefficient one, which fixes G through the unit map 8 pi G hbar/c^3 = L^2 with L the flat cell rung; the rung is set from the measured G. A candidate replacement rule asks whether G can instead be derived from information: lengths respond so that information is stationary, and no boundary holds more than a fixed information per area. In Jacobson's form, the vacuum's entanglement entropy S = eta A plus the first law dS = d<K> gives Einstein's equations with 1/(4G) = eta. This note computes eta for the update law's half-filled sea, tests the first law, and tests whether the vacuum entropy tracks proper area under the edge deformations that carry geometry in the register. The [minimal axioms](MINIMAL_AXIOMS_2026-06-29.md) fix none of the inputs used here.

## Statement

A. Exact.

1. Conformal blindness. In the update law each cube's hop is R = sum_i w_i W_i with w_i = sqrt(gamma^ii), scaled so that R^2 = 1 (the W_i anticommute, so R^2 = sum w_i^2 / |w|^2), and the lapse clause fixes the step. A common rescaling of one cube's edges, gamma_ij -> lambda_c^2 gamma_ij, multiplies w by 1/lambda_c and leaves R unchanged. So any spatial conformal factor, constant or varying cube by cube, leaves every half-tick, the vacuum (occupied quasi-energy band) and every entanglement entropy exactly unchanged, while proper areas scale by lambda^2. Hence S is not eta times proper area for any eta, and dS/dA along the conformal mode is zero.
2. First law. For a Gaussian state S = -Tr[C ln C + (1-C) ln(1-C)], and dS = Tr[K dC] with K = ln((1-C)/C) for every change of state; d<K> - dS is the relative entropy, nonnegative and second order. The first law therefore holds for any edge deformation and constrains nothing by itself; Jacobson's content lies entirely in the area term.
3. Momentum decomposition. For a (100) cut of the pi-flux sea, transverse momentum (ky, kz) and the pair (ky, ky + pi) reduce the sea to decoupled chains with hop t_x and staggered mass +-M, M = 2 sqrt(t_y^2 cos^2 ky + t_z^2 cos^2 kz), so eta_100 is the Brillouin-zone mean of the half-chain entropy s(M/t_x). The finite-torus version is an identity (checked to 1e-10).
4. Consequence of 1. A coupling read from dS/dA has no conformal (Newtonian, scalar) part: 1/G_N = 0, only a shape response. Over the register's edge window [L/8, 2^(1+Delta) L] the vacuum entropy per proper area varies by at least 256 x 4^Delta, so the vacuum itself does not hold "a fixed information per area".

B. Finite diagnostics (supplied model).

5. eta_100 = 0.196645 nats per site^2 for the two-copy pi-flux sea (grid-converged to 1e-6; it is not pi/16 = 0.196350). The half-chain entropy has the c = 1 tail -(1/6) ln M (fitted slope -0.1666). Cubes l = 3..8 in the infinite lattice, fitted to S = 6 eta l^2 + 12 b l + c ln l + d, give 0.1966.
6. Lattice balls R = 2.5..6 give 0.2292 per geometric area 4 pi R_eff^2 (1.17 eta_100): per unit area the vacuum entropy depends on the cut's orientation.
7. The tick's Floquet vacuum tends to the pi-flux sea as eps0 -> 0 with corrections ~eps0^2: +7.7e-6, +4.3e-4, +2.8e-2 at eps0 = 0.005, 0.0375, 0.3 (8^3 slab).
8. The copy mass dimerises the heavy copy between the tilings: odd-tiling and even-tiling cuts move oppositely, and the cut-averaged entropy changes by factors 0.99, 1.12, 1.71 at MN/eps0 = 0.5, 1, 1.9.
9. Shape response (planar cut, eps = 0.01): stretching the transverse edges raises the area by 2 eps but S by 0.457 of that fraction; stretching the normal edges at fixed area changes S by -0.911 eps; at fixed volume dS/dA = 0.2695 per site^2. A random shape deformation on the 8^3 torus changes S by 0.51, so the conformal invariance in item 1 is not a trivially insensitive check.
10. Bisognano-Wichmann: per transverse mode the lattice modular Hamiltonian's bond and site terms are (2 pi/v) x distance x the local energy (v = 2) to 0.999 at M = 0.1, falling to 0.835 at M = 2. Modes with M < 0.3, where the local form holds to 1%, carry 2.3% of eta_100: the area coefficient is a cell-scale quantity, where d<K> is not a weighted energy.

## Derivation

Item 1 is read from the update law's text. Item 2 is the differential of the Gaussian entropy. Item 3 Fourier-transforms the staggered hop along z and y. The runner tabulates s(u) from open chains of 600 sites (eigh_tridiagonal), interpolates in ln u with a cubic spline and a c = 1 tail below u = 0.02, and averages over a 500 x 500 midpoint grid avoiding the Dirac points. Infinite-lattice correlations use C = 1/2 - (1/2) H |H|^-1, where H^2 = sum_mu (2 + T_mu^2 + T_mu^-2) is translation invariant and |H|^-1 at displacement 2n is pi^-1/2 int dt t^-1/2 prod_mu (-1)^n_mu e^-2t I_n_mu(2t). The tick is built on an 8^3 antiperiodic torus (no zero modes at L = 0 mod 4) cube by cube, its single-particle Floquet operator Schur-decomposed, and the band with quasi-energy w < 0 filled. The first-law check perturbs every hop to 1/(1 + d g), g a seeded smooth random field, around a 4^3 cube. The scalar estimate uses the harmonic chain with transverse mass^2 = sum 4 sin^2(k/2) and symplectic eigenvalues of sqrt(X_A P_A).

## Finite checks

Exact or closed-form checks (the runner asserts each):
- Slab entropy on 8^3: real space 24.7041949901 = chain sum 24.7041949901.
- R^2 - 1 = 2e-16; copy sign s^2 = 1; Floquet trace 256 = half filling.
- Conformal rescaling over [1/8, 4]: |dS| = 3.6e-13 (shape deformation: 0.510).
- First law: dS = 1.295e-4 against d<K> = 1.299e-4 at d = 1e-3; remainder ratio 100 between d = 1e-2 and 1e-3 (quadratic).

Finite diagnostics (supplied model, finite diagnostic): items 5 to 10 above.

## Estimates against measurement

Jacobson's relation 1/(4G) = eta per site^2 (hbar = c = 1) against the hinge sum's G: under the unit map's named unit (the flat cell rung L = 2 sites = sqrt(8 pi) l_P, reading B) the needed eta is pi/2 = 1.571 per site^2; if the area unit were the site spacing (reading A) it is 2 pi.

| content (supplied) | eta per site^2 | G_A4/G (B) | G_A4/G (A) |
|---|---|---|---|
| sea, two copies | 0.197 | 7.99 | 32.0 |
| sea + photon as two scalars (0.0485) | 0.245 | 6.41 | 25.6 |
| fixed-volume dS/dA + photon | 0.318 | 4.94 | 19.8 |
| sea x largest copy-mass factor | 0.337 | 4.66 | 18.6 |

- Every row misses by more than a factor 2 (the kill criterion set before computing).
- To close the gap at reading B the omitted rishon and edge-register sites would have to add 1.33 nats per site^2 of cut, more than one maximally entangled pair (ln 2 = 0.693) per cut bond, and that amount would be set by the supplied register sizes and flavours, so it would be fitted.
- Independently of magnitude, item 4 gives no Newtonian coupling, which measured gravity has; this agrees with the companion result that the tick sea induces no Newtonian sector (THE_CUBE_TICK_SEA_INDUCES_NEITHER_A_LORENTZ_INVARIANT_MAXWELL_TERM_NOR_A_NEWTONIAN_SECTOR_BOUNDED_THEOREM_NOTE_2026-10-21).

## Boundary

Not claimed: the entanglement of the link registers' rishons or of the edge registers (omitted); the photon's edge (electric-centre) term (omitted); cuts other than (100) and lattice balls; the full copy-mass sea in infinite volume (the copy-mass factor is an 8^3 slab ratio); any statement about entanglement-based gravity with a different matter tick, in particular one whose hop is not normalised per cube. Earlier area-law notes on main (AREA_LAW_QUARTER_BROADER_NO_GO_NOTE_2026-04-25, PLANCK_ANCHOR_BP_DERIVATION_PROBE_2026-06-05) treat a Fermi-surface hopping carrier with a logarithmic area law and the coefficient 1/4; they do not cover the pi-flux Dirac sea, its conformal blindness or the hinge-sum unit map, and this note neither uses nor contradicts their results.

## Supplied vs forced

Supplied: the pi-flux sea as the tick's eps0 -> 0 limit; the tick at eps0 = 0.0375 and copy masses MN/eps0 = 0.5, 1, 1.9; hop weight = 1/length; the (100) planar cut and lattice balls; the photon as two massless lattice scalars; readings A and B of the unit map; the kill criterion (a factor 2). Forced, given those: conformal blindness and the absence of a Newtonian response; the first law as an identity; the momentum decomposition; eta_100 and the other numbers in items 5 to 10; the table.

## Dependencies

- [Minimal axioms](MINIMAL_AXIOMS_2026-06-29.md): Z^3 sites, one qubit per site, nearest-neighbour admissibility, records. They fix none of the supplied inputs above.
- [Candidate-law register](CANDIDATE_LAWS.md): the update law's cube tick (per-cube normalised hop, face phase -1, copy mass, lapse clause), the response law's hinge sum and unit map, the edge window. Zero premise weight; results using it are conditional on it.

## How to run

```
python3 scripts/the_cube_tick_seas_entanglement_is_blind_to_the_conformal_factor_so_a_jacobson_g_from_it_has_no_newtonian_part_and_exceeds_the_hinge_sum_g_2026_10_22.py
```

Needs numpy and scipy. It is self-contained, declares `AUDIT_TIMEOUT_SEC = 120`, runs in about 7 to 12 s with under 200 MB resident, prints about 5.6 kB and ends with `TOTAL: PASS=14 FAIL=0`. Its random draws are seeded; two repeated runs (one through `runner_cache.execute_runner` in a clean origin/main worktree) gave identical output apart from the elapsed-time line.
