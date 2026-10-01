---
claim_id: composite_site_network_flux_free_above_j_equals_two_the_flipping_line_node_is_a_cubic_point_that_emits_a_plane_pair_bounded_theorem_note_2026-10-01
claim_type: bounded_theorem
claim_scope: "Supplied u=+1 quadratic Majorana comparator of the landed notes, one copy, the landed hopping-sign convention, four-site Bloch matrix H(f) = i M(f), J_x = J_y = 1, J_z = J in (2, 1 + sqrt 5), odd term kappa; chi = sign of T = Im Tr(P d1H P d2H P d3H) (P the kernel projector). Exact identities in Q(J)(omega, Y), omega^2 = -A, Y^2 = J(J + 2)A, A = 4 + 2J - J^2, with signs on (2, J0) and (J0, 1 + sqrt 5) by exact factorisation and Sturm counts (J0 the real root of N = J^3 - 4J - 4): the line node f = (x, 1 - x, 0) with cos 2 pi x = c_F = (J - 2)(J + 1)/(J + 2) has q = F_c = 0 at kappa_f^2 = J(J + 2)/(4A); in coordinates u = xi1 - xi2, v = xi1 + xi2, t = xi3 (xi = 2 pi (f - f0)) the E = 0 Schur complement's Pauli vector is d = x_u u' + x_v v + x_beta t^3 + (weighted order >= 4) with weights (3, 3, 1), u' = u - u2 t^2, x_u, x_v, x_beta mutually orthogonal with positive determinant, and the weight-6 part of det H equals 16 J^2 |d0|^2 (independent determinant route): a cubic point of local degree +1 for 2 < J < J0 and J0 < J < 1 + sqrt 5. The first-order unfolding is d = ... + x_beta (t^3 - mu eps t), eps = kappa - kappa_f, mu = (J + 2)/kappa_f^3 > 0: its leading form has one nondegenerate zero (chi +1) for eps < 0 and three for eps > 0 (the line node, chi -1, and an off-line pair at t = +-sqrt(mu eps), chi +1 each); det H vanishes identically on the plane-(ii) family, which carries the emitted pair, real for every kappa >= kappa_f. At J = J0 the weighted normal form (u: 1, v: 2, t: 1, eps: 2, J - J0: 1) is F1 = c_uu u^2 + c_tt t^2 + a_d (J - J0) u + c_eps eps, F2 = b v, F3 = c_ut u t, local degree 0, with four nodes for eps > 0 of chi (-1, -1, +1, +1); its det H matches the determinant route in all 22 monomials of weight <= 4 modulo N. Floating-point checks: Fukui fluxes, grid searches (1 zero below, 3 above the flip; 0 and 4 at J0), persistence of the emitted pair to kappa = 6 kappa_f, and five anisotropic couplings where a flipping line node likewise turns into three. Not covered: explicit remainder radii (the node counts near the flip rest on the weighted leading forms and floating-point searches), interval certification, anisotropic statements beyond floating point, spin-model equivalence or physical reading."
upstream_dependencies:
  - minimal_axioms
  - the_hyperhoneycomb_embeds_in_the_doubled_cubic_lattice_a_three_dimensional_composite_site_network_with_an_exact_charge_bounded_theorem_note_2026-09-24
  - composite_site_network_flux_free_middle_bands_touch_at_two_exact_points_below_kappa_star_and_six_above_by_an_interval_certificate_bounded_theorem_note_2026-09-26
runner: scripts/composite_site_network_flux_free_region_b_line_node_flip_is_a_cubic_point_emitting_a_plane_pair_2026_10_01.py
---

# Above J = 2 the flipping line node is a cubic point that emits a plane pair

**Date:** 2026-10-01
**Type:** bounded_theorem
**Status:** exact identities in a function field of `J`, plus labelled floating-point checks, for a supplied comparator; unaudited.

## Supplied setting

The comparator is the one in
`COMPOSITE_SITE_NETWORK_FLUX_FREE_MIDDLE_BANDS_TOUCH_AT_TWO_EXACT_POINTS_BELOW_KAPPA_STAR_AND_SIX_ABOVE_BY_AN_INTERVAL_CERTIFICATE_BOUNDED_THEOREM_NOTE_2026-09-26.md`,
at `J_x = J_y = 1` and `J_z = J ∈ (2, 1 + √5)`.

Above `J = 2`, line touchings come in pairs. One node of each pair changes charge
at `κ_f² = J(J+2)/(4(4 + 2J − J²))`, the isotropic flip coupling. Here
`χ = sign T`, with `T = Im Tr(P∂₁H P∂₂H P∂₃H)` and `P` the kernel projector.

## Exact results

The identities hold for every `J` at once. They are computed in
`Q(J)(ω, Y)`, with `ω² = −A`, `Y² = J(J + 2)A` and `A = 4 + 2J − J²`. Signs on the
two intervals `(2, J₀)` and `(J₀, 1 + √5)` are fixed by exact factorisation and
Sturm counts. Here `J₀ ≈ 2.38298` is the real root of `N = J³ − 4J − 4`.

1. **The flipping node.** It sits at `cos 2πx = c_F = (J − 2)(J + 1)/(J + 2)` on
   the line `(x, 1 − x, 0)`. There `q = F_c = 0` at `κ = κ_f`.
2. **Cubic point.** Use local coordinates `u = ξ₁ − ξ₂`, `v = ξ₁ + ξ₂`, `t = ξ₃`, with
   `ξ = 2π(f − f₀)`.
   - The `E = 0` Schur complement has Pauli vector
     `d = x_u u′ + x_v v + x_β t³ + (weighted order ≥ 4)`, with weights `(3, 3, 1)`
     and `u′ = u − u₂t²`.
   - `x_u`, `x_v` and `x_β` are mutually orthogonal with positive determinant.
   - An independent determinant computation gives the weight-6 part of `det H`
     as `16J²|d₀|²`.
   - So for `J ≠ J₀` the node is a cubic point of local degree `+1`.
3. **Emission.** The first-order unfolding in `ε = κ − κ_f` is
   `d = … + x_β(t³ − μεt)`, with `μ = (J + 2)/κ_f³ > 0`.
   - For `ε < 0` the leading form has one nondegenerate zero, with `χ = +1`.
   - For `ε > 0` it has three: the line node with `χ = −1`, and an off-line pair
     at `t = ±√(με)` with `χ = +1` each.
   - Charge is conserved: the total is `+1` on both sides.
4. **The emitted pair.** It lies in the plane-(ii) family, on which `det H`
   vanishes identically for all `J` and `κ`. It stays real for every `κ ≥ κ_f`.
5. **The `J₀` event.** At `J = J₀` the weights become `(u: 1, v: 2, t: 1, ε: 2, J − J₀: 1)`.
   The normal form is
   - `F1 = c_uu u² + c_tt t² + a_d(J − J₀)u + c_ε ε`;
   - `F2 = b v`;
   - `F3 = c_ut u t`.

   This has local degree 0. For `ε > 0` four nodes are born at once:
   - a line pair with `χ = (−1, −1)`;
   - an off-line pair with `χ = (+1, +1)`.

   The determinant route agrees in all 22 monomials of weight `≤ 4`, modulo `N`.

## Floating-point consistency

- **Around the flip** (`J = 13/6, 5/2`):
  - Fukui fluxes are `−1` before, `(+1, −1, −1)` after, and `−1` on an enclosing sphere.
  - Grid searches find 1 zero below and 3 above, at the predicted positions.
- **At `J₀`:** 0 zeros below and 4 above.
- **Persistence:** the emitted pair keeps `χ = (+1, +1)` up to `κ = 6κ_f`.
- **Anisotropic couplings:** at five of them a flipping line node also turns into
  three, with local degree `+1`.

## What this settles and what it does not

- **Settled.** For `2 < J < 1 + √5` with `J ≠ J₀`, the flipping line node is a
  cubic point of degree `+1`. It emits a pair of `χ = +1` nodes into the plane-(ii)
  family, and the leading unfolding is exact. At `J₀` four nodes are born at once.
- **Not settled here.**
  - Explicit remainder radii. The node counts near the flip rest on the
    weighted leading forms and on floating-point searches.
  - Interval certification.
  - Anisotropic statements beyond floating point.
  - Equality with the spin model, and any physical reading.

## Evidence limits and No-Go Discipline Gate

- **N1:** supplied comparator; `J_x = J_y = 1`, `2 < J_z < 1 + √5`.
- **N2:** no phase or no-go wall is imported.
- **N3:** network, hopping signs and the `u = +1` sector remain supplied.
- **N4:** the landed comparator and charge convention are used as stated there.
- **N5:** exact function-field identities and weighted expansions; floating-point checks are labelled.
- **N6:** the items listed above remain open.
- **N7:** other couplings and sectors remain available.
- **N8:** no physical identification, new premise or audit verdict.

## Reproduction

```bash
python3 scripts/composite_site_network_flux_free_region_b_line_node_flip_is_a_cubic_point_emitting_a_plane_pair_2026_10_01.py
```

Twenty-four checks; prints `TOTAL: PASS=24 FAIL=0` in under 20 seconds.
