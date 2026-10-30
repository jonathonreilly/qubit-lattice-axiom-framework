---
claim_id: wave_law_shift_sourced_by_the_momentum_constraint_keeps_no_slice_bend_memory_and_stays_causal_bounded_theorem_note_2026-10-22
claim_type: bounded_theorem
claim_scope: "In linearised ADM on flat space (8 pi G = c = 1, one Fourier mode k along z, the update law's tied lapse n = tr h / 6) with the second-order shift-driver family d_t B_i = mu d_j hdot_ij + nu d_i tr(hdot) + a d_i tr K - eta B_i (B = d_t beta): the scalar-sector characteristic polynomial is (w^2 - k^2)(3w^4 - (1 + 6(mu + nu)) k^2 w^2 + a k^4)/3 and the vector one w^2(w^2 - mu k^2), so every label-rate driver (a = 0) has a double zero root at every k; the static slice bend (beta = grad xi, K_ij = d_i d_j xi, edges and tied lapse unchanged) is an exact static solution of every label-rate driver for all mu, nu, eta, so such a driver integrates to a memory of the history and leaves a tilt; the choice nu = -mu/2, a = mu is identically the wave shift d_t^2 beta_i = mu [Delta beta_i - 2 d_j(K_ij - delta_ij K)], whose source is the momentum constraint (zero in static, stationary and homogeneous states, FRW and Bianchi I included); its scalar polynomial is (w^2 - k^2)(3w^2 - k^2)(w^2 - mu k^2)/3, with no zero root at k != 0, speeds 1, 1/sqrt3 and sqrt(mu), causal for mu <= 1; it is diagonalisable at mu = 3/4 (k = 1) and has a constraint-only Jordan block at mu = 1. Finite diagnostics (RK4 at k = 1, and a 1D plane-symmetric leapfrog run): constraints hold to 3e-16, a static star formed by an inflow pulse or set from isotropic consistent data is not tilted by the wave shift (max |beta| 0 in the latter) while the undamped label-rate driver doubles its tilt, a sudden spin-up leaves edges ringing at 2.281 against 2/sqrt(mu) = 2.309 and an adiabatic one 2e-4, damping eta = 0.5 freezes a rotating edge offset of 1.333, and the plane-symmetric wave shift is zero beyond the light cone (7e-9) where the minimal-strain shift is 0.42. Estimates against measured spins, masses and cosmological perturbations are linear and indicative. Supplied model, finite diagnostic: linear ADM on flat space, the tied lapse, the driver family and its coefficients, the dust and stress test sources, k = 1, step sizes, and the measured inputs."
upstream_dependencies:
  - minimal_axioms
  - candidate_laws
runner: scripts/wave_law_shift_sourced_by_the_momentum_constraint_keeps_no_slice_bend_memory_and_stays_causal_2026_10_22.py
---

# A wave-law shift sourced by the momentum constraint keeps no slice-bend memory and stays causal

Claim type: bounded_theorem.
Primary runner: `scripts/wave_law_shift_sourced_by_the_momentum_constraint_keeps_no_slice_bend_memory_and_stays_causal_2026_10_22.py`.

The [candidate-law register](CANDIDATE_LAWS.md) has zero premise weight. Its gravity sector reads edge values, the floor and the split trigger in a frame fixed by a shift, the multiplier of the momentum constraint. Stationarity in the shift gives the constraint but does not fix the shift, so a law for it is supplied. Earlier choices (zero shift, minimal strain, label-frame strain-rate drivers) failed on rotating bodies, on causality (minimal strain responds at every distance at once) or on static stars (a growing slice tilt). This note asks which second-order shift drivers avoid all three failures in linear theory. The [minimal axioms](MINIMAL_AXIOMS_2026-06-29.md) fix none of the inputs used here.

## Statement

Setting: linearised ADM on flat space, 8 pi G = c = 1, one Fourier mode k along z, the tied lapse n = tr h / 6 (h_00 = -h_kk / 3). Driver family, B = d_t beta:

    d_t B_i = mu d_j hdot_ij + nu d_i tr(hdot) + a d_i tr K - eta B_i.

mu and nu weight label-frame strain rates; a weights the gradient of the normal observers' expansion rate tr K.

A. Exact (symbolic in k and all coefficients).

1. Dispersion, eta = 0. The scalar sector (h_xx + h_yy, h_zz, K_xx + K_yy, K_zz, beta_z, B_z) has characteristic polynomial (w^2 - k^2)(3w^4 - (1 + 6(mu + nu)) k^2 w^2 + a k^4)/3. The vector sector (h_xz, K_xz, beta_x, B_x) has w^2(w^2 - mu k^2). With label rates only (a = 0) the scalar sector has a double root w = 0 at every k.
2. Slice-bend memory. The static slice bend t -> t - xi(x) (beta = grad xi, K_ij = d_i d_j xi, edges and tied lapse unchanged) is an exact static solution of every label-rate driver (a = 0), for any mu, nu, eta: the source is d_t of the labels' strain, which vanishes on it. Such a driver therefore integrates to beta_dot = F[h] - F[h_0] - eta (beta - beta_0), and the end tilt is (F_end - F_0)/eta, a memory of the history. The wave shift is not static on the bend (d_t B = -i k^3 mu xi), so it radiates it.
3. Formation feeds the bend. From isotropic edges to the tied-lapse static star (h_zz = 10U, tr h = 6U), the label source integrates to 12 i k U (mu + nu). This is nonzero for every label driver except nu = -mu, which the runner states fails for other starting edges (stated, not computed).
4. Identity, any k direction: mu [d_j hdot_ij - d_i tr(hdot)/2 + d_i tr K] = mu [Delta beta_i - 2 (d_j K_ij - d_i K)]. So nu = -mu/2, a = mu is the wave shift

       d_t^2 beta_i = mu [Delta beta_i - 2 d_j(K_ij - delta_ij K)],

   a wave equation whose source is the momentum constraint, on shell 2 x 8 pi G J_i. Residual 0 in all three components.
5. Wave-shift spectrum. Scalar sector (w^2 - k^2)(3w^2 - k^2)(w^2 - mu k^2)/3, vector sector w^2(w^2 - mu k^2). Speeds are 1, 1/sqrt3 (the tied lapse) and sqrt(mu). The scalar sector has no zero root at k != 0, so there is no slice-bend memory. Causal iff mu <= 1.
6. Hyperbolicity. At mu = 3/4 (k = 1) the scalar matrix is diagonalisable. At mu = 1 the shift speed equals the speed of the (h_xx + h_yy, K_xx + K_yy) pair, which is the constraint subsystem, and rank(M - i) = 5 at multiplicity 2: a Jordan block that only constraint violation excites. The vector zero root has 2 eigenvectors (a frozen relabelling and stationary rotation) and no Jordan block.
7. Homogeneous states. For any homogeneous, possibly anisotropic K(t) (FRW K = -H delta, Bianchi I), d_j(K_ij - delta_ij K) = 0 and Delta beta = 0 at beta = 0, so beta = 0 is exact: labels stay comoving. Static fields (K = 0, J = 0, any anisotropic stress) source nothing either.

B. Finite diagnostics (k = 1, RK4, dt = 0.05; matter formed from vacuum by a stress pulse, so every constraint holds).

8. For the wave shift at mu = 3/4 and mu = 1 all speeds are at most 1. At mu = 3/4 the largest growth rate is 9e-16 and the momentum-constraint residual is 3e-16.
9. Star formation by an inflow pulse (unit bump on t in [5, 25], run to t = 400). The undamped label-rate driver (mu = 1/3) keeps a growing tilt after the star is static, and the damped one (eta = 0.5) freezes a tilt. The wave shift only rings, with no growth.
10. Spin-up. The wave shift reaches the stationary frame-dragging shift with edge rate 0. A sudden spin-up leaves edges ringing at about 2K/(sqrt(mu) k) (K = 1), an adiabatic one almost nothing. With zero shift the edges wind without bound.
11. Damping only hurts the wave shift. eta = 0.5 freezes a rotating edge offset and gives no gain for stars, so the law takes eta = 0.
12. Static star from isotropic consistent data, with no matter motion. The wave shift stays exactly 0 because J = 0 is its only source, while the label-rate driver tilts.
13. Plane-symmetric spin-up switched on for t in [0, 1] (counter-moving sheets, total momentum 0; 1600 points, dz = 0.05, dt = 0.02, mu = 1, leapfrog, run to t = 15). The wave shift is zero beyond the light cone |z| > 1 + t. Inside the cone it settles to the minimal-strain state, edge rate -2K + d_z beta = 0. The minimal-strain shift instead moves labels at every distance at once.

## Derivation

Items 1, 5 and 6 build the 6 x 6 scalar and 4 x 4 vector first-order matrices in sympy and factor det(M - i w). Item 2 applies the matrices to the bend vector. Item 4 expands both sides of the identity for a general wavevector (kx, ky, kz) and a general symmetric K. Item 7 differentiates a homogeneous diagonal K(t) in space. Items 8-12 integrate the full 18-component linear system (6 edges h_ij, 6 K_ij, beta, B) together with the matter density and momenta, with the matter coupled through K_dot_ij -= S_ij - delta_ij (S - rho)/2. Item 13 integrates the 1D plane-symmetric wave shift with a second-order leapfrog stencil against a prescribed K profile.

## Finite checks

Exact checks (sympy; the runner asserts each):
- Dispersion polynomials of items 1 and 5 match the stated forms; the bend residual is 0 for label-rate drivers and d_t B = -i k^3 mu xi for the wave shift; the integrated formation source is 12 i k (mu + nu) U; the identity residual is 0 in all 3 components; the homogeneous source is 0 identically.
- Hyperbolicity: diagonalisable at mu = 3/4, k = 1; rank(M - i) = 5 at mu = 1; vector kernel dimension 2.

Finite diagnostics (supplied model, finite diagnostic), from the runner's table:

| driver | max speed | growth | star tilt (mid -> end) | sudden spin-up edge ring | slow spin-up edge | constraint residual |
|---|---|---|---|---|---|---|
| zero shift | 1.000 | 1e-16 | 0.00 -> 0.00 | 589.00 | 690.000 | 3e-16 |
| label rate mu = 1/3 | 1.000 | 3e-09 | 102.78 -> 213.89 | 3.45 | 0.001 | 3e-16 |
| label rate mu = 1/3, eta = 0.5 | 1.000 | 1e-16 | 3.33 -> 3.33 | 3.00 | 3.000 | 3e-16 |
| wave mu = 3/4 | 1.000 | 9e-16 | 0.02 -> 0.02 | 2.28 | 0.000 | 3e-16 |
| wave mu = 1 | 1.000 | 2e-08 | 0.01 -> 0.01 | 1.97 | 0.000 | 3e-16 |
| wave mu = 3/4, eta = 0.5 | 1.000 | 3e-16 | 0.00 -> 0.00 | 1.33 | 1.333 | 3e-16 |

- Sudden spin-up ring for the wave shift at mu = 3/4: 2.281, against 2/sqrt(3/4) = 2.309. Slow ramp: 0.0002. Zero shift: 690.
- Damped wave shift (eta = 0.5) slow spin-up offset: 1.333, against 0.0002 at eta = 0.
- Static star from isotropic data: wave shift max |beta| 0e+00; label-rate driver 134 -> 267.
- Plane-symmetric run: beyond the cone, wave shift 7e-09 (asserted below 1e-6 of its maximum) and minimal strain 0.42; inside, the largest edge rate is 4e-03 (O(dz^2) stencil error, asserted below 1e-2 of max |2K|).
- The growth of 2e-08 at mu = 1 sits at the Jordan block of item 6. The runner asserts the growth bound (below 1e-8) only at mu = 3/4, and the speed bound at both.

No random draws.

## Estimates against measurement

Linear and indicative, with c = 3e8 m/s, G = 6.674e-11 and the edge window ln 16 = 2.77.
- Rotating bodies. A sudden spin-up's edge strain is at most 2 K r / c with K ~ 3 w_LT: Earth 4.3e-15, Sun 1.2e-11, Sgr A* (a = 0.5) 0.25, extreme Kerr (a = 1) 0.50, all inside the window. The extreme Kerr value uses the linear formula at the horizon, so it is indicative only.
- Neutron stars. The static-star tilt is exactly 0 (items 4 and 12). Formation leaves only outgoing gauge waves, with a peak tilt of about 4 (GM / r c^2)(v / c): 0.24 c for U = 0.2 and v = 0.3 c. This formula is stated, not integrated.
- Cosmology. The background shift is 0 exactly (item 7). A perturbation's stationary shift is about 6 Omega_m (aH / ck)^2 delta v / c, about 1e-8 c at 10 Mpc (delta = 1, v = 300 km/s). This formula is stated.
- Causality of the split trigger. Outside the light cone the response to a kilogram moved a metre is 0, where the minimal-strain shift gives G m / (c^2 r) = 7.4e-28 at once.
- The runner records the no-damping choice (eta = 0) and the statement that mu sets only the gauge-wave speed as a stated check, not a computed one.

## Boundary

Not claimed: the shift law at register level (CL-1's block-pair rotations) or its derivation from the register; any nonlinear completion; strong-field or horizon dynamics; 3D radiation of the gauge waves (only the 1D plane-symmetric run of item 13); diagonalisability at values of mu other than 3/4, in particular at mu = 1/3, where the shift speed sqrt(mu) equals the tied-lapse speed 1/sqrt3 and the scalar roots are double (not examined); the failure of nu = -mu for other starting edges (stated); the closed-form estimates of the neutron-star tilt and the cosmological shift (stated, evaluated on supplied numbers); any experimental exclusion.

## Supplied vs forced

Supplied: linear ADM on flat space with the tied lapse; the driver family and its coefficient values (mu = 1/3, 3/4, 1; eta = 0, 0.5); the dust and stress test sources and their bump profiles; k = 1, the step sizes, the grid and the run lengths; the measured J, R and masses, the Sgr A* spin (indicative), the cosmological delta and v, and the window ln 16. Forced, given those: the double zero root and the slice-bend memory of every label-rate driver; the identity that makes nu = -mu/2, a = mu a wave equation sourced by the momentum constraint; its spectrum, with no scalar zero root at k != 0 and speed sqrt(mu); zero source in static, stationary and homogeneous states; the mu = 1 Jordan block confined to the constraint subsystem.

## Dependencies

- [Minimal axioms](MINIMAL_AXIOMS_2026-06-29.md): Z^3 sites, one qubit per site, nearest-neighbour admissibility, records. They fix none of the supplied inputs above.
- [Candidate-law register](CANDIDATE_LAWS.md): the update law's tied lapse, the momentum constraint as the generator of a site's displacement with the shift as its multiplier, the edge window, and the frame in which edge values and the split trigger are read. Zero premise weight; results using it are conditional on it.

## How to run

```
python3 scripts/wave_law_shift_sourced_by_the_momentum_constraint_keeps_no_slice_bend_memory_and_stays_causal_2026_10_22.py
```

Needs numpy and sympy. It is self-contained, declares `AUDIT_TIMEOUT_SEC = 90`, runs in about 4 s with about 90 MB resident, prints about 5.1 kB and ends with `TOTAL: PASS=18 FAIL=0`. It has no random draws; two runs gave identical output apart from the elapsed-time line.
