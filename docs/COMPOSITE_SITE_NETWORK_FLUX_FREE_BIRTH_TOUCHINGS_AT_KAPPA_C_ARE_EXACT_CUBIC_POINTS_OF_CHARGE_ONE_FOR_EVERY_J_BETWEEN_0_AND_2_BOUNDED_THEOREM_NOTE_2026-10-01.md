---
claim_id: composite_site_network_flux_free_birth_touchings_at_kappa_c_are_exact_cubic_points_of_charge_one_for_every_j_between_0_and_2_bounded_theorem_note_2026-10-01
claim_type: bounded_theorem
claim_scope: "Supplied u=+1 quadratic Majorana comparator of the landed notes, one copy, the landed hopping-sign convention, J_x = J_y = 1, J_z = J in (0, 2), four-site Bloch matrix H(f) = i M(f), at the birth coupling kappa_c^2 = J(J+2)/[4(4+2J-J^2)] of the landed certificate note, where the line node f0 = (x, 1-x, 0), cos 2 pi x = (J-2)(J+1)/(J+2), merges with the two plane-(ii) nodes. Exact symbolic identities in J over the function field Q(J)(omega, Y), omega^2 = -A, Y^2 = J(J+2)A, A = 4+2J-J^2 (no floating point): det(H - lambda) = lambda^2 (lambda^2 - 16J^2) at f0; with xi = 2 pi (f - f0), u = xi1 - xi2, v = xi1 + xi2, t = xi3, the E = 0 Schur complement on the kernel has no t-linear or t^3 term and no identity part through weight 3 (weights u: 2, v: 3, t: 1); its t^2 term is -u2 times its u term, u2 = W(J+2)/(2(J^3-4J-4)) < 0, so with u' = u - u2 t^2 its Pauli vector is d = x_u u' + x_v v + x_beta t^3 + (weight >= 4), x_u, x_v, x_beta mutually orthogonal with norms a^2 = (J^3-4J-4)^2/((J+2)^2 A), b^2 = 2J^3(J+1)^2/((J+2)^2 A), g^2 = J^4(J+2)/(8(J^3-4J-4)^2) and positive determinant; D = det H has a rank-two Hessian, and in weights (3,3,1) for (u', v, t) its weights 0 to 5 vanish and its weight-6 part is 16J^2 (a^2 u'^2 + b^2 v^2 + g^2 t^6) = 16J^2 |d0|^2. So the birth touching is an isolated cubic point (linear in two directions, cubic in the third) of local degree +1 for every J in (0, 2); at kappa = kappa_c + eps it unfolds as d = x_u u'' + x_v v + x_beta (t^3 - mu eps t), mu = 8YA/(J^2(J+2)) > 0: three nodes of charges (-,+,+) for eps > 0 and one (+) for eps < 0, to first order matching the landed family formulas. The data lie on a genus-one curve, so no one-parameter rational parametrisation exists. Floating-point sphere fluxes -1 around f0 and +1 around its mirror at J = 0.4, 1, 1.6 are a consistency check. Not covered: the mirror point exactly, weights beyond those listed, the link between the E = 0 Schur complement and the two-band problem beyond weight five (argued), other couplings, spin-model equivalence or physical reading."
upstream_dependencies:
  - minimal_axioms
  - the_hyperhoneycomb_embeds_in_the_doubled_cubic_lattice_a_three_dimensional_composite_site_network_with_an_exact_charge_bounded_theorem_note_2026-09-24
  - composite_site_network_flux_free_middle_bands_touch_at_two_exact_points_below_kappa_star_and_six_above_by_an_interval_certificate_bounded_theorem_note_2026-09-26
  - composite_site_network_flux_free_handover_touchings_are_exact_charge_two_points_for_every_j_between_0_and_2_bounded_theorem_note_2026-09-28
runner: scripts/composite_site_network_flux_free_birth_touchings_are_exact_cubic_points_of_charge_one_for_every_j_2026_10_01.py
---

# The birth touchings at κ_c are exact cubic points of charge one for every J between 0 and 2

**Date:** 2026-10-01
**Type:** bounded_theorem
**Status:** exact symbolic algebra for a supplied comparator; unaudited.

## Supplied setting

Use the supplied comparator and the three exact touching families of the landed note
`COMPOSITE_SITE_NETWORK_FLUX_FREE_MIDDLE_BANDS_TOUCH_AT_TWO_EXACT_POINTS_BELOW_KAPPA_STAR_AND_SIX_ABOVE_BY_AN_INTERVAL_CERTIFICATE_BOUNDED_THEOREM_NOTE_2026-09-26.md`,
with `J_x = J_y = 1` and `J_z = J ∈ (0, 2)`.

**Where this sits.** At `κ_c² = J(J+2)/[4(4+2J−J²)]` the line node
`f₀ = (x, 1−x, 0)`, with `cos 2πx = (J−2)(J+1)/(J+2)`, meets the two
plane-(ii) nodes, which are born there. The landed handover note
`COMPOSITE_SITE_NETWORK_FLUX_FREE_HANDOVER_TOUCHINGS_ARE_EXACT_CHARGE_TWO_POINTS_FOR_EVERY_J_BETWEEN_0_AND_2_BOUNDED_THEOREM_NOTE_2026-09-28.md`
treats the other transition, at `κ_h`. This block treats the birth.

## Method

All arithmetic is exact, in the function field `Q(J)(ω, Y)`, where:
- `ω² = −A` and `Y² = J(J+2)A`, with `A = 4 + 2J − J²`;
- `κ_c = Y/(2A)`;
- `e^{2πix} = (J + ω)²/(2(J+2))`.

The data lie on a smooth intersection of two quadrics, a genus-one curve, so
no one-parameter rational parametrisation exists. The identities therefore
hold for every `J` at once.

## Result

Write `ξ = 2π(f − f₀)`, `u = ξ₁ − ξ₂`, `v = ξ₁ + ξ₂`, `t = ξ₃`, and
`c = 16J²`.

1. **Double zero level.** `det(H − λ) = λ²(λ² − 16J²)` at `f₀`. The kernel
   projector is `P = (M₀² + c)/c`.
2. **Effective Hamiltonian.** Take the `E = 0` Schur complement on the
   kernel, with weights `u: 2`, `v: 3`, `t: 1`.
   - The `t`-linear and `t³` matrices vanish, and so does the identity part
     through weight 3.
   - The `t²` term equals `−u₂` times the `u` term, where
     `u₂ = W(J+2)/(2(J³ − 4J − 4)) < 0` and `W = √A`.
   - With `u′ = u − u₂t²`, the Pauli vector is
     `d = x_u u′ + x_v v + x_β t³ + (weight ≥ 4)`.
3. **Frame.** `x_u`, `x_v`, `x_β` are mutually orthogonal, with
   - `a² = (J³−4J−4)²/((J+2)²A)`;
   - `b² = 2J³(J+1)²/((J+2)²A)`;
   - `g² = J⁴(J+2)/(8(J³−4J−4)²)`;
   - `det[x_u, x_v, x_β] = W Y J³(J+1)/(2(J+2)²A²) > 0`.

   All signs hold on `(0, 2)`, by factorisation and Sturm counts.
4. **Determinant.** `D = det H` has the quadratic part `c a²u² + c b²v²`, so
   its Hessian has rank two, with kernel along `f₃`. In weights `(3, 3, 1)`
   for `(u′, v, t)`, weights 0 to 5 vanish, and the weight-6 part is
   `c(a²u′² + b²v² + g²t⁶) = c|d₀|²`. This is computed from the determinant,
   independently of the Schur route.
5. **Charge.** In an orthonormal frame of orientation `+1`,
   `d₀ = (a u′, b v, g t³)`, with Jacobian `3abg t² ≥ 0`. So the birth
   touching is an isolated cubic point of local degree `+1`: linear in two
   directions and cubic along `f₃`.
6. **Unfolding.** At `κ = κ_c + ε`, `d = x_u u″ + x_v v + x_β(t³ − μεt)`,
   with `μ = 8YA/(J²(J+2)) > 0`.
   - For `ε > 0` there are three nodes, with charges `(−, +, +)`.
   - For `ε < 0` there is one node, with charge `+`.
   - To first order this matches the landed family formulas: the plane
     `f₃`, the line cosine and the plane cosine.
7. **Consistency (floating point).** An independent float Schur code agrees
   with the exact forms to `1e-14`. Sphere Berry fluxes are `−1` around `f₀`
   and `+1` around its mirror, at `J = 0.4, 1, 1.6`.

Example values at `J = 1`:
- `κ_c = √15/10`;
- `a² = 49/45`, `b² = 8/45`, `g² = 3/392`;
- `u₂ = −3√5/14`;
- `μ = 40√15/3`.

## What this settles and what it does not

- **Settled.** The birth touchings at `κ_c` are isolated cubic points of
  charge one for every `J ∈ (0, 2)`. With the landed handover note, both
  transitions of the families are now exact local statements: charge one
  and cubic at `κ_c`, and charge two and quadratic at `κ_h`.
- **Not settled here.**
  - The mirror point exactly; its float flux is checked, not its algebra.
  - Weights beyond those listed.
  - The step from the `E = 0` Schur complement to the two-band problem.
     It changes `d` at weight five or more; this is argued, not
     computed.
  - Couplings off `κ_c`, equality with the spin model, and any physical
     reading.

## Evidence limits and No-Go Discipline Gate

- **N1:** supplied comparator with `J_x = J_y = 1`, `J_z = J ∈ (0, 2)`, at `κ_c` and its first-order unfolding.
- **N2:** no phase or no-go wall is imported.
- **N3:** network, hopping signs and the `u = +1` sector remain supplied.
- **N4:** the landed certificate and handover notes govern their scopes.
- **N5:** exact identities in a function field; the float fluxes are a consistency check.
- **N6:** the mirror point exactly and higher weights remain open.
- **N7:** other sectors and couplings remain available.
- **N8:** no physical identification, new premise or audit verdict.

## Reproduction

```bash
python3 scripts/composite_site_network_flux_free_birth_touchings_are_exact_cubic_points_of_charge_one_for_every_j_2026_10_01.py
```

Eleven checks; prints `TOTAL: PASS=11 FAIL=0` in about ten seconds.
