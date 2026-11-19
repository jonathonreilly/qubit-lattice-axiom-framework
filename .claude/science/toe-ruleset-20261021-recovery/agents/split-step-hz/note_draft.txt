---
claim_id: split_epoch_step_in_h_is_geometric_of_order_hl_squared_with_zero_vacuum_jump_bounded_theorem_note_2026-10-22
claim_type: bounded_theorem
claim_scope: "Under the candidate laws' split (children's edges at the parent's value minus s register steps, so the edge halves for every s) and the response law (Lambda a constant per proper 4-volume, vacuum standard on the same edges), the vacuum energy density does not jump at a split (exact 4-volume count). On the supplied cubic-frustum hinge carrier, with a triggered split keeping 8 pi G rho/3 continuous, ln H jumps by +(3/4)(H L)^2 per split (L the post-split edge), a sawtooth of period ln 2 in ln(1+z), exactly two steps in 0 < z <= 3 for any phase; the phase is not fixed by any law. Splits fire at a fixed local edge, so a spread of split times does not smear the step in 1+z; in a finite diagnostic with independent Born edge offsets at the register's wall-margin bound the fundamental keeps 0.988 of its size. With L = sqrt(8 pi) l_P the step is 2.6e-121 today and 5.4e-120 at z = 3; CPL fits give |dw| <= 5e-118 (rho_DE on z < 3) and <= 1e-112 (toy BAO + theta*), with the DESI sign pattern but some 1e110 below a 0.01 sensitivity. In the tensor spectrum of the discrete-tick toy, the period-ln 2 fundamental is second order (<= 1.1 (H l)^2), and the first-order structure is a fast lattice oscillation. Supplied: the carrier, the unit map, LambdaCDM numbers, the toy BAO errors, the Gaussian edge-offset model and the 1D tensor toy."
upstream_dependencies:
  - minimal_axioms
  - candidate_laws
runner: scripts/split_epoch_step_in_h_is_geometric_of_order_hl_squared_with_zero_vacuum_jump_2026_10_22.py
---

# The split-epoch step in H is geometric, of order (H L)^2, with zero vacuum jump

Claim type: bounded_theorem.
Primary runner: `scripts/split_epoch_step_in_h_is_geometric_of_order_hl_squared_with_zero_vacuum_jump_2026_10_22.py`.

The [candidate-law register](CANDIDATE_LAWS.md) has zero premise weight. It predicts dark energy exactly constant, w = -1, apart from a log-periodic step in H(z) at split epochs and a period-ln 2 ripple in the tensor spectrum, but it gives no amplitude for either. This note computes both from the law text. The [minimal axioms](MINIMAL_AXIOMS_2026-06-29.md) fix no Lambda and no carrier.

## Statement

1. Vacuum. Lambda per proper 4-volume, summed over the 8 children and 2 child ticks of a split frustum cell, equals the parent's exactly. The vacuum energy density does not jump at a split. The step is set by the factor 2 (the children start at 4s - s = 3s, so l(4s)/l(3s) = 2 for every s), not by 1/s or e^(-s).
2. Rest energies. At K = 0 the flat-edge band gives cos w = cos mu. The mass angle and the proper tick both scale with the edge, so a split keeps every rest energy. Matter changes only through state mismatch, of order K^2 or mu^2.
3. H. On the hinge carrier, A(u) = u^2 + 2u^4 + O(u^6) with A = X l^2/4 and u = H l/2, so H^2 = X - X^2 l^2/2 and delta ln H = -(H l)^2/4. A triggered split keeps X = 8 pi G rho/3 continuous (Lambda kept, the vacuum carried to the vacuum) and halves l, so ln H jumps by +(3/4)(H L)^2. Exact root-finding gives 0.75 at H L = 5.93e-61. The jump is geometric, not a vacuum jump.
4. Synchrony. A split fires when its own edges and its neighbours' face edges are full, which is at a fixed local edge. Since 1 + z is the edge ratio, a spread of split times does not smear the step in z. Only the neighbour wait spreads the edge at which a split fires.
5. H(z) and w(z). There is a sawtooth in ln H of period ln 2 in ln(1+z), with steps at 1 + z_k = 2^k (1 + z_0). There are exactly two steps in 0 < z <= 3 for every phase, and 10 (90%) or 11 since recombination. Between splits w + 1 = (H l)^2 E^2 (1 + 2 dlnH/dlna)/(3 Omega_L), which is positive below z ~ 0.04 and phantom above it. Each split adds a phantom spike with integral -(H L)^2 E^2/(2 Omega_L) over ln a. The phase z_0 is set by where today's edge sits in the octave, and no law fixes it.
6. Tensors. In the discrete-tick toy the octave repeats exactly. The period-ln 2 fundamental is second order, at most 1.1 (H l_c)^2. The first-order structure, ptp about 1.5 H l_c (edge-seeds' "ripple"), is a fast lattice oscillation at about 0.32/(H l_c) cycles per octave with amplitude about 0.4 H l_c.

## Derivation

Item 1 is additivity of proper 4-volume over the children's frusta, which tile the parent's. A count per cell per tick in lattice units would instead change by a factor of 1/16, and the dropped fixed-4-volume-per-record clause gave a kick at each split (split-junction T2, T4). Item 3 inverts the hinge series. With X held fixed, l = 2L before the split and l = L after it give Delta ln H = (1/4) X ((2L)^2 - L^2). This rederives split-junction A6 (0.748 there). Item 4 follows spectral-tilt D1: every rule component is a function of the local edge, so the uniform-edge slice is the uniform-density slice. A frozen Born offset per edge shifts each cube's cycle by its overshoot max(0, mean own - min neighbour) and does not accumulate, because the children inherit the parent's overshoot. The ripple's fundamental is multiplied by F = E[exp(2 pi i O/s)]. Item 5 differentiates the inferred rho_DE = Omega_L - (1/2) E^4 (l/L)^2 (H0 L)^2 with l ~ a between splits. Item 6 reuses the edge-seeds leapfrog (the stationary discrete hinge phase for one TT amplitude, with vacuum-carrying splits) on one octave of 128 log-spaced modes, and Fourier-analyses it over the exactly repeating octave.

## Checks

The runner ends with `TOTAL: PASS=15 FAIL=0` in about 1 s, with 154 MB peak.

- A1 to A3 are exact: the 4-volume count difference is 0, l(4s)/l(3s) = 2, and cos w(K = 0) = cos mu.
- B1 and B2: the series is A = u^2 + 2u^4, and the jump/(HL)^2 is 0.74999891 at H L = 1e-3, 0.74989 at 1e-2 and 0.75 at 5.93e-61. Today the jump is 2.64e-121, and at z = 3 it is 5.41e-120.
- C2: at sigma = 0.0315 in ln l (the wall-margin bound, Delta = 1), |F| = 0.9881 against a Gaussian estimate of 0.9881, with a phase lag of 0.60 rad (a phase shift only). At the excluded one-cell spread 0.2, |F| = 0.63. The supplied Poisson stepping, read as a firing-edge spread, gives 0.985.
- D1: exactly 2 steps for z <= 3 at all 2000 sampled phases.
- D2: the analytic w + 1 matches the numerical derivative. Per (H0 L)^2 it is 0.0565, -3.49, -10.9 and -209 at z = 0, 0.5, 1 and 2.
- D3: a CPL fit to rho_DE on 0 < z < 3 over 16 phases gives w0 + 1 in [122, 497] and wa in [-1274, -369] per (H0 L)^2, so |dw| <= 4.5e-118. The ratio wa/(1 + w0) lies between -3.03 and -2.55.
- D4: a toy BAO projection (1% errors at the DR2 redshifts plus theta*, r_d held) gives C = 2.7e8 per (H0 L)^2 with the sawtooth out to z*, and 195 from z < 3 alone, so |dw| <= 9.6e-113.
- D5 and D6: see the estimates below.
- E1: c1/(H l)^2 = 1.08, 0.79, 0.40 and 0.83 at H l = 0.08, 0.04, 0.02 and 0.01. The peak harmonic sits at n H l = 0.32 to 0.33, with |c_peak|/(H l) = 0.35 to 0.51.

## Estimates against measurement

- The DESI direction. Every phase gives w0 > -1 and wa < 0, and the fitted ratio wa/(1 + w0), about -2.6 to -3.0, lies close to DESI's degeneracy line (-3.0 to -3.8). The size is the problem. Mimicking (w0, wa) = (-0.75, -0.86) needs (H0 l)^2 ~ 2e-4, an edge about 1.4% of the Hubble length, against 3.5e-121. The step cannot produce the DESI hint, and it lies about 1e110 to 1e115 below the roughly 0.01 sensitivity of the final DESI and Euclid data. The prediction of the response law is therefore unchanged: w = -1 to every measurable precision, and a detected evolution of dark energy would falsify CL-3 as written (desi-de).
- Other split-epoch sources, as a fraction of H^2 per split. The dark-constant kick (H L)^2/8 enters only if the zero mean is not kept, and is about 4e-122. Radiation flips (0.04 K^2) give about 1e-66. The proton split-energy ceiling (0.05 mu^2, a desi-de estimate, not rerun) gives about 9e-39, the largest for known content. All of them are more than 1e30 below detectability.
- Tensors. The laws' only de Sitter phase is today's, with P_t ~ 7e-122. Its period-ln 2 ripple is about 4e-121 of that, and the fast oscillation is about 2e-61, at about 5e59 cycles per octave, which cannot be resolved. A supplied inflation at H = 1e13 GeV, which is not in the laws, would give about 2e-11 and 2e-6 (at 8e4 cycles per octave).
- The early-time hinge correction. Through the sound horizon it reaches a fraction of order (comoving horizon at the start)/r_d, which depends on the start. It is a constant offset, not a w(z) shape, so it is not included above.

## Boundary

Forced: items 1 to 5 given the carrier, with the phase free. Supplied: the cubic-frustum hinge carrier A(u) and the triggered-split partition clause (split-junction), the unit map L = sqrt(8 pi) l_P with edges in [L, 2L), LambdaCDM (H0 = 67.7, Omega_m = 0.31), independent Gaussian edge offsets and the wall margin of 22 spreads with Delta = 1, the toy BAO errors with r_d held, and the 1D-axis tensor toy (sin eps0 = 0.3, H l_c >= 0.01, extrapolated down to 1e-61). Not shown: correlated or inhomogeneous offsets beyond the toy, bound regions that never split, the full 3D tensor modes, and the massive split-energy coefficient (cited as an estimate). Narrows: the register's "log-periodic ripple of period ln 2" in the tensor spectrum is second order in its fundamental; edge-seeds' first-order "ripple" is a fast lattice oscillation.
