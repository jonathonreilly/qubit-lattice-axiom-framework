---
claim_id: a_covariant_momentum_term_keeps_the_volume_rate_shift_hyperbolic_through_collapse_and_static_stars_attract_bounded_theorem_note_2026-10-22
claim_type: bounded_theorem
claim_scope: "In the continuum ADM limit of the response law, with the update law's tied lapse and the candidate shift law of #9976 (not adopted) (d_t - beta^j d_j)^2 beta_i = mu c_l^2 [Delta beta_i - 2 d_j(K_ij - delta_ij K) - kappa d_i(N K)] at mu = 3/4, kappa = 2(1 - mu)/mu = 2/3. (A) exact: with the momentum term read on shell (as the matter momentum), the free (off-constraint) system for a radial plane wave has characteristic polynomial proportional to (v^2 - 1)(12 v^4 - 13 v^2 + 3 - 3 kappa) on isotropic cubes; at kappa = kappa_max the fast longitudinal gauge mode and the light-speed constraint-violating mode coincide at v = 1 and form a Jordan block, so the system is only weakly hyperbolic there and constraint violations grow like k t; reading the term covariantly, -2 D_j(K^j_i - delta^j_i K) with the cube's own edges, gives the same polynomial and is diagonalizable at kappa_max, with eigenvector conditioning at the generic level over l_r/l_t in [1/2, 2]; a shift perturbation of a static star with unchanged edges, K and matter is pure gauge and obeys a closed linear system for the slice and label displacements (derived by hand; only its momentum identity is checked numerically). (B) finite diagnostics: planar periodic noise grows ~60-fold in 40 M on shell and stays within a few-fold covariantly; a dust ball collapsing from 3 r_s under the on-shell reading fails to converge before any horizon (finer grid crashes first); with the covariant reading (and a supplied core device: on-shell with kappa 0.3 at labels r < 2) the run goes through horizon formation, excision of the crunching core at 15.5 M and on to 110 M with every untrapped edge in [0.51, 1.91] and every edge on the grid >= 0.20, a shift-wave sonic surface at R ~ 2.5 M, and an exterior whose edges are within 3% and lapse within 5% of the vacuum attractor while its shift charge is still 30-80% above it and relaxing; the vacuum attractor is the same under both readings (spread 0.2%); the literal flat-lattice divergence still runs away under the normal-frame law (failure at 10.8 M); two TOV polytrope stars (M = 1.40, N_c = 0.67; M = 1.64, N_c = 0.46) shed one pure-gauge shift bump by radiation (late/peak 3e-3 and 0.10, still falling), and in the compact star the source per proper time blows up within 6 M_sun while the per-tick form does not. These are finite runs whose modified core, excision, Kreiss-Oliger dissipation and outer sponge are part of each diagnostic's definition; they are not evidence of unmodified nonlinear stability, of convergence of the post-crunch shift charge, or of attraction of static stars from all perturbations. Supplied: continuum ADM, spherical symmetry (planar for B1), mu, kappa, the dust profile, the core device, excision, dissipation, grids and the polytrope."
upstream_dependencies:
  - minimal_axioms
  - a_normal_frame_wave_shift_fed_by_the_per_tick_volume_rate_gives_black_hole_exteriors_an_attracting_horizon_regular_slicing_bounded_theorem_note_2026-10-22
  - a_black_hole_exterior_keeps_a_regular_tied_lapse_slicing_only_while_its_shift_charge_lasts_bounded_theorem_note_2026-10-22
runner: scripts/a_covariant_momentum_term_keeps_the_volume_rate_shift_hyperbolic_through_collapse_and_static_stars_attract_2026_10_22.py
---

# A covariant momentum term removes the kappa_max Jordan block of the volume-rate shift; with a supplied core device one dust collapse runs past excision, and two static stars shed a gauge bump

Claim type: bounded_theorem.
Primary runner: `scripts/a_covariant_momentum_term_keeps_the_volume_rate_shift_hyperbolic_through_collapse_and_static_stars_attract_2026_10_22.py`.

Model status (2026-11-14). The update law's tied lapse and the response law (CL-1 and CL-3 in the three-law numbering of the originating register) are used here as supplied conditional model definitions with zero premise weight. The originating register text is not in this repository, and these clauses are not the entries of the same number in [docs/CANDIDATE_LAWS.md](CANDIDATE_LAWS.md). The held text said the register "has adopted" the normal-frame wave shift; no adoption is established, and the source note that introduces it states "not adopted". It is read here as a candidate law.

The normal-frame wave shift fed by the per-tick volume rate ([A_NORMAL_FRAME_WAVE_SHIFT_FED_BY_THE_PER_TICK_VOLUME_RATE_GIVES_BLACK_HOLE_EXTERIORS_AN_ATTRACTING_HORIZON_REGULAR_SLICING_BOUNDED_THEOREM_NOTE_2026-10-22.md](A_NORMAL_FRAME_WAVE_SHIFT_FED_BY_THE_PER_TICK_VOLUME_RATE_GIVES_BLACK_HOLE_EXTERIORS_AN_ATTRACTING_HORIZON_REGULAR_SLICING_BOUNDED_THEOREM_NOTE_2026-10-22.md), the shift-charge-law note, #9976, carried in this PR) has been tested so far only on vacuum black-hole exteriors. This note tests it on matter collapse through the crunch, on neutron-star end states, on collapsing cores, and against the literal flat-lattice reading of its momentum term ([A_BLACK_HOLE_EXTERIOR_KEEPS_A_REGULAR_TIED_LAPSE_SLICING_ONLY_WHILE_ITS_SHIFT_CHARGE_LASTS_BOUNDED_THEOREM_NOTE_2026-10-22.md](A_BLACK_HOLE_EXTERIOR_KEEPS_A_REGULAR_TIED_LAPSE_SLICING_ONLY_WHILE_ITS_SHIFT_CHARGE_LASTS_BOUNDED_THEOREM_NOTE_2026-10-22.md), post-crunch C3, #9964, carried in this PR). The [minimal axioms](MINIMAL_AXIOMS_2026-06-29.md) fix none of the inputs used here. Units G = c = 1; black-hole runs M = 1, stars in M_sun; edges in far-edge units.

## Result in one paragraph

The candidate law fails in one place, and the failure is a reading, not the volume-rate source. With its momentum term read on shell (as matter momentum, the reading the sibling runs used), the law at kappa = kappa_max puts the fast gauge mode exactly on the light cone on every isotropic cube. That is where the constraint-violating light-speed mode lives, and the two lock into a Jordan block (A1). Any constraint error is then amplified in proportion to k t. In a collapsing dust ball the isotropic core turns this into a grid-scale blow-up before any horizon forms (B2), so under the on-shell reading item (1) cannot be followed at all. Reading the term covariantly, with D_j taken from the cube's own edges, removes the block (A2, B1). It equals the on-shell reading on every constraint-obeying state, and it also cures the literal flat-lattice runaway, which persists under the normal-frame law (B5). With that reading and a supplied core device, one dust collapse goes through horizon formation and the crunch (excised) inside the Delta = 1 window, and the exterior's edges reach the vacuum attractor's values while its shift charge is still relaxing (B3, B4). For two TOV stars one pure-gauge shift bump radiates away (B6), and in the compact star the per-proper-time form blows up while the per-tick form does not (B7).

## Candidate law text (revision of the #9976 candidate sentence)

> "The shift obeys the undamped wave law read along the slice normals, (d_t - beta^j d_j)^2 beta_i = mu c_l^2 [Delta beta_i - 2 D_j(K^j_i - delta^j_i K) - kappa d_i(N K)], where D_j is the divergence read with the cube's own edges (the flat-lattice difference plus the connection of the cube's and its neighbours' edges), c_l = N/l ..." (rest unchanged).

Smuggling check:
- The covariant divergence uses only edge registers of the cube and its neighbours. That is the same block as the existing Laplacian and the c_l factor. It adds no register and no constant.
- On every state obeying the constraints, which the register already requires ("only odds obeying the constraints in that frame occur"), it equals the matter momentum. So no stationary or physical result of the shift-charge-law note changes, and B4 confirms this for the attractor.
- It changes only how the law responds off the constraint surface. That response matters, because the coherent limit holds the constraints only up to (l_P/L)^2 and every continuum evaluation carries errors.
- It is not the literal flat-lattice text. The flat d_j has a large vacuum part near holes (post-crunch C3) and still runs away under the normal frame (B5). The current sentence's "d_j" must therefore be read as D_j in any case.
- Alternative fix considered: kappa strictly below kappa_max. It does not remove the degeneracy, only moves it to the surface (1 - mu)(1 - q) = mu q kappa (l_r < l_t, which occurs in cores). Conditioning near kappa_max stays poor (A2 numbers), and Delta = 1 needs kappa >= ~0.6 (shift-charge-law B6). Rejected.

## Statement

A. Exact (sympy).
1. Linearise ADM, the tied lapse and the shift law about constant edges (A, 1, 1), in the variables (a, b, K_xx, K_yy, beta, d_t beta), for a radial plane wave with the constraints not imposed. The characteristic polynomial is proportional to (v^2 - 1)(12 v^4 - 13 v^2 + 3 - 3 kappa) at A = 1 for both readings. At kappa = 2/3 the quartic has the root v = 1, which is double with the transverse-edge (Hamiltonian-violating) mode. In the on-shell reading the Jordan form has nonzero off-diagonals (weakly hyperbolic).
2. The covariant reading adds +4 mu c_l^2 d_x K^y_y to the shift row and is diagonalizable at kappa_max. Over A in [1/4, 4], its largest eigenvector condition number at kappa_max is 6e2. The on-shell reading reaches 6e7 there; the generic level set by variable scaling is ~1e3.
3. Static star, pure gauge (derived by hand, not computed; the runner prints it as NOT CHECKED, and B7 checks only its momentum identity on evolved data). Write f for the normal slice displacement and xi for the label displacement. Then N f_t = dN_tied(xi) - xi N', xi_t = b + N^2 f'/A, dK_ij = -D_i D_j(N f) + f D_i D_j N, and dS_r = -(rho + P) N f'. These feed the linearised law for b. The tied-lapse static labels exist with a regular centre r = e^(-nu_c) R and flatten to r/R -> 1.

B. Finite diagnostics. Statements marked scratch report runs that are not in the runner or the repository; they are reported results, unverified here, and no conclusion of this note rests on them.
1. Planar periodic ADM, seeded noise 1e-6, 40 M, h = 0.1. The edge amplitude grows x62 on shell at kappa_max, x3.6 covariantly, and x5.2 at kappa = 0. Single-mode scratch runs give growth proportional to k for the on-shell reading (x30, x50 and x130 at k = 1, 2 and 4 in 20 M) and none covariantly.
2. Dust ball from rest at R0 = 6 M under the on-shell reading. The shift at 6M after 8 M (no horizon yet) is 4.81 at h = 0.05, and the run crashes at h = 0.025. The covariant run gives 4.811 and 4.814. In scratch runs the spherical centre is exponentially unstable for kappa >= 0.6 and only linearly drifting for kappa <= 0.5 (faster at finer grids), with every shift reading. That is why the core device is needed.
3. Covariant reading with the core device. The AH grows past 1.5 M and the trapped region reaches R = 1.2 M at 15.5 M. The core is excised there and all rest mass leaves through the excision by ~20 M. The run continues to 110 M.
   - Every untrapped edge stays in [0.506, 1.91], so the floor is never reached outside the horizon. Every edge on the grid is >= 0.20, so no floor is reached at all.
   - At Delta = 1 every far phase fits, since the top is 2 and the floor 1/8.
   - The sonic surface sits at R = 2.25-2.5 M.
   - Scratch checks: h = 0.04 agrees with 0.05 to 1% in edges and 5% in Q at 160 M. A 200 M run reaches l_r 1.79-1.84, l_t 0.483, N(2M) 0.54 and Q(6M) 11.8-12.0, with Q(12M) falling from 30 to 18. Of five core-device settings, two survive excision; the other three crash 2-3 M after excision at R < 1.3 M, inside the horizon.
4. Vacuum attractor from the shift-charge-law separatrix, 120 M: l_r 1.81, l_t 0.493, N(2M) 0.593, Q6 9.67, Q12 14.10. The covariant reading reproduces these to 0.2%. The matter exterior at 110 M differs by -1% in l_r, +3% in l_t, -5% in N(2M), +31% in Q6 and +76% in Q12. The edges are effectively on the attractor; the shift charge is still relaxing toward it.
5. The literal flat-lattice divergence under the normal-frame law fails from the attractor data at 10.8 M.
6. TOV polytropes (K = 100, Gamma = 2), with a shift bump and unchanged data:
   - M = 1.40 (N_c 0.67): the amplitude peaks at 1.5e-2 and is 4e-5 at 190-210 M_sun.
   - M = 1.64 (N_c 0.46): peak 3.5e-2, 3.6e-3 at 190-210, falling monotonically from 60 M_sun on.
   - The h = 0.1 and 0.05 amplitudes agree to two digits (scratch). Outer-boundary reflections return after ~2 r_out.
7. Compact star: the K-per-proper-time source blows up at 6.1 M_sun, as predicted where N < kappa. The momentum identity dM_r = 8 pi dS_r holds on the evolved data to 4e-4 at h = 0.05.

C. Estimates.
- The gauge relaxation of a 1.4 M_sun star takes ~0.3 ms, and a few ms for 1.64 M_sun. No gauge-invariant observable is involved.
- Item 3 of the brief (N K large in cores). N K reaches ~1-3 near the excision and ~0.6 in the pre-horizon core, with no pathology of its own under the per-tick form. The only pathology found is the kappa_max on-shell Jordan block, which concerns the reading of the momentum term, not the size of N K.

## Answers to the open items

1. Matter collapse.
   - On-shell reading: it cannot be followed. The core blows up before the horizon forms.
   - Covariant reading: the floor stays off the grid's untrapped part throughout, and all exterior edges stay in the Delta = 1 window. After the crunch the exterior's edges reach attractor values within ~100 M, while its shift charge is still relaxing at 200 M (not yet shown to converge to the attractor value).
2. Neutron stars: for two TOV polytropes, one pure-gauge shift bump radiates away at linear order (B6). Attraction from all perturbations, and nonlinear perturbations, are not shown.
3. Volume-rate source in cores: the per-tick form is well behaved. The pathology lies in the on-shell reading at kappa_max.
4. Literal flat-lattice source: still a runaway under the normal frame. The covariant reading cures it.

## Boundary

Supplied: the continuum ADM limit; spherical symmetry (planar in B1); mu = 3/4 and kappa = 2/3; the dust ball (R0 = 6 M, tanh edge 6%); the core device (on-shell reading with kappa 0.3 at labels r < 2, needed because the covariant term is numerically unstable at the spherical origin in this code at every kappa, and the on-shell term at kappa >= 0.6); excision at the trapped R = 1.2 M with extrapolated ghosts; KO dissipation 0.8; the grids; the TOV polytrope; the outer sponge.

Not claimed: that the modified-core runs show the unmodified law's nonlinear stability (the core device, excision, dissipation and sponge are part of each diagnostic); attraction of static stars from all perturbations; that the on-shell blow-up at the spherical centre is purely continuum (spherical-coordinate origin terms add to it; the clean continuum statement is A1/B1); convergence of the post-crunch shift charge to the attractor value; nonlinear star perturbations; non-spherical collapse; extreme Kerr; adoption of the revised reading.

## Dependencies

- [Minimal axioms](MINIMAL_AXIOMS_2026-06-29.md): they fix none of the supplied inputs.
- Supplied model (originating three-law register, not in this repository; stated here as conditional definitions with zero premise weight). [docs/CANDIDATE_LAWS.md](CANDIDATE_LAWS.md) does not contain these clauses.
- Used:
  - shift-charge-law, [A_NORMAL_FRAME_WAVE_SHIFT_FED_BY_THE_PER_TICK_VOLUME_RATE_GIVES_BLACK_HOLE_EXTERIORS_AN_ATTRACTING_HORIZON_REGULAR_SLICING_BOUNDED_THEOREM_NOTE_2026-10-22.md](A_NORMAL_FRAME_WAVE_SHIFT_FED_BY_THE_PER_TICK_VOLUME_RATE_GIVES_BLACK_HOLE_EXTERIORS_AN_ATTRACTING_HORIZON_REGULAR_SLICING_BOUNDED_THEOREM_NOTE_2026-10-22.md) (#9976, carried): the symbol, the attractor, the separatrix data and the per-tick vs per-proper-time constant term;
  - post-crunch, [A_BLACK_HOLE_EXTERIOR_KEEPS_A_REGULAR_TIED_LAPSE_SLICING_ONLY_WHILE_ITS_SHIFT_CHARGE_LASTS_BOUNDED_THEOREM_NOTE_2026-10-22.md](A_BLACK_HOLE_EXTERIOR_KEEPS_A_REGULAR_TIED_LAPSE_SLICING_ONLY_WHILE_ITS_SHIFT_CHARGE_LASTS_BOUNDED_THEOREM_NOTE_2026-10-22.md) (#9964, carried): C3 literal runaway, C2 drain;
  - wave-shift-collapse (#9957, logged; not in this repository, recorded only in the consolidation map): the dust code, AH test and window, re-implemented in this runner; what is said of #9957 itself is a historical reported result, unverified here.
- Narrowed: shift-charge-law A1's well-posedness holds on the constraint surface only; off it, the on-shell reading at kappa_max is weakly hyperbolic.

## How to run

python3 scripts/a_covariant_momentum_term_keeps_the_volume_rate_shift_hyperbolic_through_collapse_and_static_stars_attract_2026_10_22.py

AUDIT_TIMEOUT_SEC = 120; about 55-65 s, peak about 120 MB, stdout ~6.3 kB; ends with TOTAL: PASS=9 FAIL=0 and exits nonzero if any counted check fails. A3, C1 and C2 are printed as NOT CHECKED, ESTIMATE and PROPOSAL lines and not counted.
