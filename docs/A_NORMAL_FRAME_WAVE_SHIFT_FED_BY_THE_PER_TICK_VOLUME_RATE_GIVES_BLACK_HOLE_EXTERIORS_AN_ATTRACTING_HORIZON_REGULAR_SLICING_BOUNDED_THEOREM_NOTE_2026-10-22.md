---
claim_id: a_normal_frame_wave_shift_fed_by_the_per_tick_volume_rate_gives_black_hole_exteriors_an_attracting_horizon_regular_slicing_bounded_theorem_note_2026-10-22
claim_type: bounded_theorem
claim_scope: "In the continuum ADM limit of the response law, under the update law's tied lapse (N^2 = 3/(1/A + 2/B) read from the edges), for a candidate revision of the shift law: the wave law read along the slice normals, (d_t - beta^j d_j)^2 beta_i = mu c_l^2 [Delta beta_i - 2 d_j(K_ij - delta_ij K) - kappa d_i(N K)], with c_l the local light speed in labels, the momentum-constraint part read on shell as the matter momentum, and N K the cube's fractional volume change per tick along the normal. (A) exact, flat-background principal symbol on the constraint surface: the longitudinal gauge speeds obey v^4 - (mu + q) v^2 + mu q (1 - kappa) = 0 (v in local light speeds, q = l_t^2/(l_t^2 + 2 l_r^2) the tied lapse speed squared), so they are real for every kappa >= 0 and positive for every edge ratio and lapse iff kappa < 1; in weak fields (q = 1/3) they are at most c iff kappa <= 2(1 - mu)/mu (2/3 at mu = 3/4), and at that value the fast mode is exactly c and no gauge mode outruns light wherever l_r >= l_t; the same source taken per proper time (K instead of N K) gives the constant term mu q (1 - kappa/N) and is ill-posed wherever N < kappa; the source and the advection vanish on static slices, homogeneous slices and stationary axisymmetric azimuthal shifts, so beta = 0 for static stars, FRW and Bianchi I, and the rotating-body equation is the register's up to the factor c_l^2; the law is time-reversal invariant; in labels every characteristic moves at -beta +- v c_l, so inside the shift-wave sonic surface (outside the horizon) the core cannot signal the exterior, unlike the register's label-frame law. (B) finite diagnostics in spherical symmetry with mu = 3/4 and kappa = 2/3: three different starting slicings (label-family Q0 = 4, 8, and 6 with a shift bump) end within 120 M on one stationary horizon-regular exterior (spread <= 3%; scratch run stationary to 400 M), with largest exterior radial edge 1.81 (log2 0.85), smallest tangential edge 0.49, lapse 0.58-0.59 at 2M, shift-wave sonic surface at R ~ 2.1-2.2 M and r^2 beta ~ 9.7 at 6M; every exterior edge lies inside the window [2^(-3-m), 2^(1+Delta-m)] at every far phase for Delta = 1; a core shift seed inside the horizon reaches the exterior only at the 2e-4 numerical-leak level in 15 M (label frame: 0.34 in 1.4 M); a weak-field bump spreads at 0.93 c; h = 0.05 and 0.1 agree to 2%. kappa is supplied: at kappa = 1/2 the radial edge is 2.49 (needs Delta = 2), so with Delta = 1 kappa must lie within about 10% of its weak-field causal maximum. Supplied: the normal-frame reading, kappa (or the rule placing it at the causal maximum), mu = 3/4, the on-shell reading, the flat-label Laplacian times N^2/A, spherical symmetry, excision, dissipation and boundaries."
upstream_dependencies:
  - minimal_axioms
  - candidate_laws
runner: scripts/a_normal_frame_wave_shift_fed_by_the_per_tick_volume_rate_gives_black_hole_exteriors_an_attracting_horizon_regular_slicing_2026_10_22.py
---

# A normal-frame wave shift fed by the per-tick volume rate gives black-hole exteriors an attracting horizon-regular slicing

Claim type: bounded_theorem.
Primary runner: `scripts/a_normal_frame_wave_shift_fed_by_the_per_tick_volume_rate_gives_black_hole_exteriors_an_attracting_horizon_regular_slicing_2026_10_22.py`.

The [candidate-law register](CANDIDATE_LAWS.md) has zero premise weight. Its post-crunch item found an open tension: under the wave shift as written, a black hole's exterior shift charge Q = r^2 beta^r is set by the core, is odd under time reversal, and leaks out of the horizon in the label frame. After a time-symmetric core bounce the exterior is left on the static slicing, whose edges reach the window floor at R of about 2.01-2.03 M. That is a visible bounce, which observations exclude. The cure tested there (trapped cells keep their shift) is not cell-local. This note gives a block-local revision of the shift law under which the exterior settles onto a single stationary, horizon-regular slicing. The slicing is an attractor and is causally sealed from the core. The [minimal axioms](MINIMAL_AXIOMS_2026-06-29.md) fix none of the inputs used here. Units are G = c = M = 1, edges are in far-edge units, r is the site label and R the areal radius.

## Candidate law text (revision of the CL-3 shift sentence; not adopted)

> "The shift obeys the undamped wave law read along the slice normals, (d_t - beta^j d_j)^2 beta_i = mu c_l^2 [Delta beta_i - 2 d_j(K_ij - delta_ij K) - kappa d_i(N K)], where c_l = N/l is the cube's light speed in labels (its tied lapse over its edge along i), N K is the cube's fractional volume change per tick along the slice normal, read from its edges' change between ticks, and kappa is a supplied constant with 0 < kappa <= 2(1 - mu)/mu, with mu as before."

Smuggling check, item by item:
- The normal-frame reading. In the current text the wave runs at sqrt(mu) labels per tick whatever the shift. This revision makes it run at sqrt(mu) times the cube's own light speed, relative to the cubes' normals. That is the same locality as the existing Laplacian: the block of cubes, one rung up. It uses only registers the update law already reads (edges, the tied lapse, the shift). No trapped test, horizon finder or outgoing-light expansion is used.
- The source term. -kappa d_i(N K) is the label difference of neighbouring cubes' per-tick volume rates, so it is block-local. In weak fields it equals the trace-weight change -2 d_j(K_ij - zeta delta_ij K) with kappa = 2(1 - zeta). Here zeta = 2/3 replaces the register's 1, which is what made the vacuum source vanish on shell.
- Per tick, not per proper time. A1 forces this. With K per proper time the gauge system is ill-posed wherever the lapse N is below kappa: in collapsing cores, and (with kappa ~ 0.5-0.67) in J0740-class neutron-star cores.
- kappa is supplied. Its upper end is forced by weak-field causality (A2). Placing it at that end ("the fastest longitudinal gauge mode is the light cone") is a rule choice, not a derivation. Delta = 1 needs kappa within about 10% of that end (B6). Delta = 2 holds at kappa = 0.5.
- mu now affects a stationary state: the black-hole slicing. The register line "mu affects no stationary state" would have to read "no static, homogeneous or stationary-rotating state".
- What is not used: no time-even source, no damping, no threshold, and no new register.

## Statement

A. Exact (sympy, on the constraint surface of a flat background with edges l_r, l_t and tied lapse).

1. For a radial plane wave the constraints force the tangential perturbations to zero. The longitudinal symbol is v^4 - (mu + q) v^2 + mu q (1 - kappa) = 0. Here v is in units of c_l, and q = l_t^2/(l_t^2 + 2 l_r^2) is the tied lapse speed squared, which is 1/3 for equal edges. With kappa = 0 the roots are mu and q, the register's shift and lapse speeds. If the source is K per proper time, the constant term becomes mu q (1 - kappa/N), with v^2 < 0 wherever N < kappa.
2. The discriminant is (mu - q)^2 + 4 mu q kappa >= 0, so the speeds are real. They are positive iff kappa < 1, at every edge ratio and lapse. Both are at most c iff (1 - mu)(1 - q) >= mu q kappa. In weak fields that means kappa <= 2(1 - mu)/mu, which is 2/3 at mu = 3/4, where the speeds are 1 and sqrt(1/12). At that kappa no gauge mode is faster than light wherever l_r >= l_t (q <= 1/3). Physical modes stay at c and the transverse shift modes at sqrt(mu).
3. The source and the advection vanish on static slices (K = 0), on homogeneous slices (N K uniform), and for stationary axisymmetric azimuthal shifts (D_i beta^i = 0, so K = 0, and beta^j d_j beta = 0). So beta = 0 around static stars, on FRW and on Bianchi I, and the rotating-body equation is the register's up to the factor c_l^2.
4. The law is invariant under time reversal: beta, K and d_t are odd, so each term is consistent. No time-even source is needed. The time-reversed (white-hole, Q < 0) slicing is also stationary and repels in forward time.
5. In labels every gauge characteristic moves at -beta +- v c_l. Inside the surface beta = v_max c_l, all of them point inward. By A2 that surface lies at or outside the horizon, so the core cannot signal the exterior through the gauge. In the register's label frame the wave moves sqrt(mu) labels per tick at every beta, and does cross the horizon (post-crunch A3).

B. Finite diagnostics. Vacuum ADM with the tied lapse, the revised law at mu = 3/4 and kappa = 2/3, labels excised inside the horizon, outer boundary at r = 70.

1. Attractor. Three different starting slicings are used: the label-family separatrices with Q0 = 4 and 8, and Q0 = 6 with a 20% shift bump. Their initial largest radial edges are 3.02, 1.24 and 1.76. After 120 M all three are on one stationary exterior. The spreads are 1.3% (largest l_r), 1.1% (smallest l_t) and 3.0% (lapse at 2M).

   Start | t | ext l_r max | l_t min | N(2M) | r^2 beta at 6M, 12M
   ------|---|-------------|---------|-------|--------------------
   Q0 = 4 | 120 | 1.81 | 0.493 | 0.593 | 9.67, 14.10
   Q0 = 8 | 120 | 1.80 | 0.492 | 0.576 | 9.62, 13.74
   Q0 = 6, bump | 120 | 1.78 | 0.497 | 0.582 | 9.69, 14.01

2. Window. The largest exterior radial edge is 1.81 (log2 0.85) and the smallest tangential edge 0.49. Every exterior edge is therefore inside [2^(-3-m), 2^(1+Delta-m)] at every far phase m with Delta = 1. The shift-wave sonic surface (beta = sqrt(mu) c_l) sits at R of about 2.1-2.2 M. The slow-gauge sonic point (beta/c_l = sqrt(1/12)) sits near 5 M.
3. Stationarity. Edges and lapse drift by 1.6% between t = 80 and 120 M. A scratch run with r_out = 150 to 400 M kept l_r max at 1.78-1.86 and l_t min at 0.49.
4. Core signal. A shift seed at R = 1.0 M, inside the horizon, reaches the exterior (2-8 M) at 2.1e-4 of the seed after 15 M. That is the leak level of centred differences. Under the register's label-frame law the same seed is 0.34 of itself at 2-3 M within 1.4 M, and that law then fails on this data. A finite flip of the core's shift (Q to -Q) crashes the excised interior in both laws, so it was replaced by this linear test.
5. Weak field. A compact longitudinal shift bump on a flat slice spreads at 0.93 c.
6. kappa scan at mu = 3/4, radial edge on the attractor: 0.5 gives 2.49 and 2/3 gives 1.81. Interpolating, Delta = 1 needs kappa >~ 0.6; Delta = 2 holds at least down to kappa = 0.5 (lower kappa not run in this form).
7. Resolution. h = 0.05 and h = 0.1 agree to 1.8% at 80 M. Scratch runs at h = 0.025 agreed for the K-per-proper-time form too, which A1 shows is still ill-posed at the lattice cutoff.

## Derivation

A1 linearises the free ADM equations in the normal frame on a flat background with constant edges (A, B). The tied lapse gives delta N = N^3 a/(6A) on the constraint surface b = k_y = 0, where a and b are the fractional radial and tangential edge-squared perturbations. With d_t a = -2 N k_x + 2 beta', d_t K_rr = -N'' and the revised shift law, the 3x3 symbol's determinant gives the quartic (N^2 = 3 q A is used). A2 is the quartic's discriminant and its value at v = 1. A3 is direct substitution. A4 counts the parity of each factor. A5 follows from A1-A2 with the advection -beta. B evolves A, B, K^r_r, K^theta_theta, beta and (d_t - beta d_r) beta. It uses fourth-order differences, RK4, Kreiss-Oliger dissipation 0.8 and h = 0.1. The inner boundary is an outflow boundary inside the horizon, with labels removed below R = 0.5 and added by linear extrapolation when the inner edge rises above R = 1.7. The outer boundary is held.

## Literature reading (from memory, not re-checked in this run)

Moving-puncture evolutions (1+log lapse with Gamma-driver shift; Hannam, Husa, Pollney, Bruegmann and O Murchadha 2007-2008; Baumgarte and Naculich 2007 for maximal slices) settle on stationary "trumpet" slices. They are unique by regularity at a critical point where a gauge speed equals the shift. They are reached because data inside that point cannot escape, and they need the lapse condition. The coordinates are damped onto them by the Gamma-driver's eta. Here the lapse is tied to the edges, so the 1+log condition is not available. The trumpet mechanism (a gauge-sonic surface outside the horizon) is carried by the shift instead, and settling happens by gauge radiation, with no damping. The Gamma-driver's source is the divergence of the trace-free distortion rate (zeta = 1/3, kappa = 4/3). With the tied lapse that is ill-posed (A1), so the Gamma-driver itself cannot be copied. Its 3/4 is chosen so that its longitudinal speed (conformal Laplacian) equals c. The analogous rule here is kappa = 2(1 - mu)/mu. The puncture trumpet's radial edge in puncture labels diverges at the puncture, inside the horizon, so it says nothing about [L/8, 2^(1+Delta) L] outside the horizon. That was not computed.

## Other routes tested (scratch, not in the runner)

- Normal frame without the source (kappa = 0): Q drains to 0 and the slicing heads to the static one (l_r 3.1 to 11 by 48 M, then failure). This is post-crunch C2.
- Source from the tied lapse's own rate, sum of q_i K^i_i: it removes the K-form's anisotropy defect, but in strong fields the shift runs away (r^2 beta past 20) and the run fails by 80 M.
- Sources from the outgoing-light expansion theta_+ of a cell face: these need a surface choice (the label surfaces), so they are not cell-local. Any source confined to trapped cells is, under the normal-frame law, inside the sealed region and cannot act on the exterior. Under the label-frame law it leaks the bounce as well. Not pursued.
- A time-even source: not needed, because the selection comes from causality (A5), not from a time arrow.

## Estimates against measurement

- Frame dragging. Earth and Kerr bounds come from stationary axisymmetric states, where the extra terms vanish (A3). The remaining change is the factor N^2 gamma^jj, a relative 7e-10 at the Earth, so the edge ring of about 4e-15 is unchanged. The extreme-Kerr ring (at most 0.5 in the register) was not recomputed.
- GP-B, LAGEOS, Shapiro delay and bending are gauge-invariant at linear order and unchanged.
- Black holes. The exterior slicing no longer depends on the core's history, so a time-symmetric core bounce cannot re-emerge promptly. Only the register's (L/r_s)^2-per-crossing estimate remains, which is consistent with Cyg X-1 and GW ringdowns.

## Boundary

Supplied: the continuum ADM limit of the response law; spherical symmetry; mu = 3/4; kappa (here at its weak-field causal maximum 2/3); the on-shell (matter) reading of the momentum-constraint part (the literal flat-lattice divergence of post-crunch C3 is not cured here); the flat-label Laplacian times N^2/A as the nonlinear completion; excision, its regridding, dissipation and the held outer boundary.

Forced, given those: the principal symbol, the reality, positivity and weak-field causality bounds, and the per-tick form; the vanishing on static, homogeneous and stationary-rotating states; T-invariance; the sealed region inside the gauge-sonic surface; the attractor's edge values (finite diagnostics).

Not computed: matter collapse through a crunch under the revised law; neutron-star and static-star end states as attractors (only beta = 0 being a solution is shown); extreme Kerr; non-spherical or off-axis propagation (A1 is along a principal axis); register-level odds; the far field beyond about 20 M at late times (gauge waves reflect off the held boundary); a finite core Q flip (the excised interior fails in both laws).

Not claimed: that kappa is derived; that the law is adopted; that the strong-anisotropy regime l_r << l_t is free of superluminal gauge modes (it is not, as with the register's label-frame shift).

## Dependencies

- [minimal_axioms](MINIMAL_AXIOMS_2026-06-29.md)
- [candidate_laws](CANDIDATE_LAWS.md)
- Used: the post-crunch stationary family, separatrices and charge parity (A1-A5, B1); its normal-frame drain (C2) and literal-source runaway (C3); the wave-shift collapse charges at trapping; the floor-placement window.

## How to run

python3 scripts/a_normal_frame_wave_shift_fed_by_the_per_tick_volume_rate_gives_black_hole_exteriors_an_attracting_horizon_regular_slicing_2026_10_22.py

AUDIT_TIMEOUT_SEC = 120; about 45 s, peak about 130 MB; ends with TOTAL: PASS=14 FAIL=0.
