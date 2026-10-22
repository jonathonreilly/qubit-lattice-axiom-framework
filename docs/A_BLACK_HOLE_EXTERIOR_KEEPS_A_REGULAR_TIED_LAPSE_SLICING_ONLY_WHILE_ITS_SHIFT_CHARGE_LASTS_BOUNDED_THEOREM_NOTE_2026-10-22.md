---
claim_id: a_black_hole_exterior_keeps_a_regular_tied_lapse_slicing_only_while_its_shift_charge_lasts_bounded_theorem_note_2026-10-22
claim_type: bounded_theorem
claim_scope: "In the continuum ADM limit of the response law, in spherical symmetry, for a Schwarzschild exterior under the update law's tied lapse (N^2 = 3/(1/A + 2/B) read from the edges) and the wave shift in its on-shell form with mu = 3/4: (A) exact: a stationary slicing has N^2 gamma_RR = 1 and reduces to dr/dR = sqrt(gamma(3 gamma - 2 s^2)) with 3 f gamma^2 - (3 + 2 s^2 f - beta^2) gamma + 2 s^2 = 0 (s = r/R, f = 1 - 2M/R), edges l_r = (3 gamma - 2 s^2)^(-1/2) and l_t = 1/s, and vacuum shift beta^r = Q/r^2 + a r; the root that is flat far away is the static type at the horizon (N and l_r to 0), so a slicing regular through the horizon must pass a double-root point outside it and is tuned, one per Q; at such a horizon the radial light speed in labels equals beta^r, so a label-frame shift wave crosses the horizon outward; the stationary charge is Q = -(16 pi/3) int r^3 S^r/A dr, the matter's radial momentum moment, is odd under time reversal, and slicings with Q < 0 cross only the past horizon. (B) Finite diagnostics: the regular family exists for 0 < Q <~ 10 M^2 with its critical point at R = 3.2-4.0 M, tangential edges >= 0.32 outside the horizon, and a radial edge peak of 61 (Q = 0.25) to 1.1 (Q = 10); every far phase stays inside the window [2^(-3-m), 2^(1+Delta-m)] outside the horizon only for 5.5 <~ Q <~ 10 (Delta = 1) or 3.2 <~ Q <~ 10 (Delta = 2). In a nonlinear vacuum evolution excised inside the horizon, the Q = 4 member is stationary while the core holds Q; with the shift wave advected in the normal frame the charge drains into the hole (4.0 to 1.2 in 32 M); with the source read literally on the flat lattice it runs through zero in 6 M. So under the shift law as written, a time-symmetric core bounce reverses Q and the exterior is left on the static slicing, whose edges reach the window floor outside the horizon: a visible bounce, in tension with black-hole observations. The cure tested, cells inside a trapped surface keep their shift, is a candidate clause, not derived and not adopted; it holds Q at its trapping value 3.6-5.0 M^2 and needs Delta >= 2. Supplied: the continuum ADM limit, spherical symmetry, mu = 3/4, the on-shell source, the flat-label Laplacian, excision boundary conditions and dissipation, and Q at trapping from the sibling collapse runs."
upstream_dependencies:
  - minimal_axioms
  - candidate_laws
runner: scripts/a_black_hole_exterior_keeps_a_regular_tied_lapse_slicing_only_while_its_shift_charge_lasts_2026_10_22.py
---

# A black-hole exterior keeps a regular tied-lapse slicing only while its shift charge lasts

Claim type: bounded_theorem.
Primary runner: `scripts/a_black_hole_exterior_keeps_a_regular_tied_lapse_slicing_only_while_its_shift_charge_lasts_2026_10_22.py`.

The [candidate-law register](CANDIDATE_LAWS.md) has zero premise weight. Its strong-field item found that, with the wave shift, the window floor stays inside the horizon through horizon formation, and left open what happens after the core crunches. If the exterior relaxes to the static zero-shift slicing, the tied lapse N = sqrt(1 - 2M/R) puts an edge at the floor at R of about 2.01 to 2.03 M, outside the horizon. This note finds all stationary exterior slicings, asks which one the evolution keeps, and tests cures. The [minimal axioms](MINIMAL_AXIOMS_2026-06-29.md) fix none of the inputs used here. Units are G = c = M = 1, edges are in far-edge units, r is the site label and R the areal radius.

## Statement

A. Stationary slicings (exact).

1. A stationary slicing t = T + h(R) of Schwarzschild has lapse N = gamma_RR^(-1/2) and shift beta^R = sqrt(1 - f gamma)/gamma on the ingoing branch. The tied lapse read from edges A = gamma (dR/dr)^2 and B = R^2/r^2 gives dr/dR = sqrt(gamma(3 gamma - 2 s^2)). The label shift beta = beta^r then gives the quadratic 3 f gamma^2 - (3 + 2 s^2 f - beta^2) gamma + 2 s^2 = 0. The edges are l_r = (3 gamma - 2 s^2)^(-1/2) and l_t = 1/s. In vacuum the stationary wave shift is Q/r^2 + a r, and a = 0 for a flat exterior.
2. The discriminant is (2(x - sqrt(3/2))^2 - beta^2)(2(x + sqrt(3/2))^2 - beta^2), with x = s sqrt f. The root that is flat far away (gamma -> 1) diverges at the horizon like (3 - beta^2)/(3f). That is the static type: N and l_r go to 0, which is the floor. The root that stays finite at the horizon is gamma = 2 s^2/(3 - beta^2). A slicing regular through the horizon must therefore change roots at a double root outside the horizon, a sonic-type point. That fixes the label constant, so there is one regular slicing per Q and it is tuned.
3. At the horizon of such a slicing the radial light speed in labels, N/sqrt(A) = (dr/dR)/gamma, equals beta^r. Outgoing light stays at a fixed label, while the label-frame wave shift moves sqrt(mu) labels per tick, so the shift carries data from inside the horizon to the outside. It is also radially faster than light in labels wherever l_r/l_t > sqrt((3/mu - 1)/2), which is 1.22 at mu = 3/4.
4. Integrating the r^3 moment of the wave law gives Q(t) = -(16 pi/3) int r^3 S^r/A dr - (1/(3 mu)) int r^3 d_t^2 beta dr. A stationary exterior charge is the radial momentum moment of the matter.
5. S^r, beta and d_t^2 beta are odd under time reversal, so Q is odd. A time-symmetric bounce of the core sends Q to -Q. The edges depend only on beta^2, but the sign of Q sets the slice direction: Q < 0 slicings are the time reverse and cross only the past horizon. With Q <= 0, a collapse exterior is left with the static root at the future horizon, and its edges reach the floor 2^(-3-m) at R = 2M/(1 - 4^(-3-m)).

B. The regular family (finite diagnostics).

1. For each Q from 0.25 to 10 there is one separatrix. It is flat at infinity, its critical point lies at R = 3.16 to 4.02 M, and it is regular through 2M. Outside the horizon the tangential edges stay at or above 0.32. The largest exterior radial edge is 61 (Q = 0.25), 14.6 (1), 6.9 (2), 4.35 (3), 3.04 (4), 2.28 (5), 2.00 (5.5), 1.76 (6), 1.24 (8) and 1.13 (10). For Q <= 6 it sits at the horizon.
2. The family ends at Q_max of about 10: at Q = 10.5 the flat separatrix meets a second critical point at R = 3.33 M, outside the horizon.

C. Evolution (finite diagnostics; vacuum ADM with the tied lapse, labels excised inside the horizon, starting from the Q = 4 separatrix).

1. With the core holding Q (label-frame law, shift held inside the horizon), the slicing stays stationary for 40 M. Label perturbations of +-0.02 oscillate about it until the excision boundary fails at about 50 M. Persistence is shown; attraction is not.
2. With the shift wave advected in the normal frame at the local radial light speed, (d_t - beta d_r)^2 beta = mu (N^2/A) Lap beta, nothing enters through the excision boundary, but the charge falls into the hole. Q at 6M drops from 4.0 to 1.2 in 32 M, and the radial edge passes 4 outside the horizon. The slicing heads to the static one.
3. With the source read literally on the flat lattice, Lap beta_i - 2 d_j(K_ij - delta_ij K) rather than its on-shell value, the source has a vacuum part near the hole: 2V is about 65 at R = 2.5 M, against a covariant momentum constraint of 1e-6. It drives Q through zero within 6 M. The on-shell equality in the register holds only at linear order.

So under the shift law as written, the core sets Q (A4), its bounce reverses Q (A5), and the reversal reaches the exterior (A3). The advected and literal readings also lose Q (C2, C3). In each case the exterior is left on the static slicing, whose edges reach the window walls outside the horizon: a visible bounce.

## Derivation

A1 substitutes the stationary metric into N^2 = 3/(1/A + 2/B) and into beta^r = (dr/dR) beta^R, then eliminates dr/dR. A2 factors the discriminant and takes f -> 0 in each root. A3 evaluates dr/dR = 2 s^2 beta/(3 - beta^2) on the horizon root gamma = 2 s^2/(3 - beta^2), so (dr/dR)/gamma = beta exactly. A4 multiplies the radial wave law, whose vector Laplacian is d_r of div beta, by r^3/3 and integrates by parts; outside the matter, div(Q r^-2 r-hat) = 0. A5 is the parity of each factor under t -> -t together with F(beta) = F(-beta). B finds the critical points (F = 0, dF/dgamma = 0, and the total derivative condition) and integrates the separatrix in a parametrisation that passes through them. C evolves A, B, K^r_r, K^theta_theta, beta and d_t beta with fourth-order differences, RK4, Kreiss-Oliger dissipation 0.8, h = 0.1, an inner boundary at R of about 1.4 M (inside the horizon), and an outer boundary at r = 70 held at the stationary values.

## Checks

The runner prints 14 checks: A1-A5 exact (sympy; A4 is checked numerically on a smooth profile to 1e-4); B1-B2 and C1-C3 finite diagnostics; D1-D4 estimates.

## Estimates against measurement

- Window band. Every far phase stays inside the window outside the horizon only for 5.5 <~ Q <~ 10 with Delta = 1, or 3.2 <~ Q <~ 10 with Delta = 2. On this family the top is the binding wall, not the floor.
- Candidate cure, not adopted: cells inside a trapped surface keep their shift. The exterior then keeps the charge it had at trapping, 3.6 to 5.0 M^2 in the sibling collapse runs from 5 and 10 r_s, which is roughly independent of scale for collapse from rest. That puts the largest radial edge at 3.5 to 2.3. Every far phase fits with Delta >= 2; with Delta = 1 only 20 to 80 percent do. The clause is supplied, not derived, and the trapped test is not local to a cell (at best local to a block, like the shift).
- A memory source built on the accumulated inward mass flux gives Q of about 0.4 M R0^2 for a ball falling from rest at R0, past Q_max for R0 >~ 5 M: excluded.
- Timing. Under the current law the reversal reaches R = 6M in about (label distance)/sqrt(mu), about 5 M: milliseconds for stellar holes, not Hawking times. A prompt re-emergence of this kind is excluded for Cyg X-1.
- Exterior observables are those of general relativity on every member of the family; only gauge and edge values differ.

## Boundary

Supplied: the continuum ADM limit of the response law; spherical symmetry; mu = 3/4; the on-shell (matter) form of the shift source, except in C3; the flat-label vector Laplacian as the nonlinear completion; excision inside the horizon, its boundary conditions and the dissipation; Q at trapping from the sibling collapse runs; the Newtonian flux-memory estimate; the trapped-shift clause, which is a candidate.

Forced, given those: the stationary reduction and quadratic; the root structure and the tuning; the light-speed identity at the horizon; the charge identity and its time-reversal parity; the family's extent and edge values.

Not computed: the matter collapse continued through the crunch (freezing the interior made the code fail by t of about 47 M); attraction toward the family at fixed Q; the stationary family of the advected law; register-level odds; non-spherical collapse; the trapped test in cell or block terms.

Not claimed: that no shift law keeps the exterior regular. A law that keeps Q in the window band, by a rule rather than a supplied value, would remove the tension.

## Dependencies

- [minimal_axioms](MINIMAL_AXIOMS_2026-06-29.md)
- [candidate_laws](CANDIDATE_LAWS.md)
- Used: the wave-shift collapse runs (Q of 3.6 to 5.0 M^2 at trapping, the static-floor radius, PG not a stationary state); the static zero-shift end state (floor-horizon B2); no trumpet labels without a shift and gauge shocks of the tied lapse (strong-field-tick C5, A4); the time-symmetric turn at the floor (qcrush B3).

## How to run

python3 scripts/a_black_hole_exterior_keeps_a_regular_tied_lapse_slicing_only_while_its_shift_charge_lasts_2026_10_22.py

AUDIT_TIMEOUT_SEC = 120; about 30-40 s, peak about 130 MB; ends with TOTAL: PASS=14 FAIL=0.
