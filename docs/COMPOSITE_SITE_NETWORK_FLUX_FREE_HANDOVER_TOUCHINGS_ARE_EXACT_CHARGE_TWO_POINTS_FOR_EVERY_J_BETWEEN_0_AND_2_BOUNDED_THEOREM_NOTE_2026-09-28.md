---
claim_id: composite_site_network_flux_free_handover_touchings_are_exact_charge_two_points_for_every_j_between_0_and_2_bounded_theorem_note_2026-09-28
claim_type: bounded_theorem
claim_scope: "Supplied u=+1 quadratic Majorana comparator of the landed notes, one copy, the landed hopping-sign convention, couplings J_x = J_y = 1, J_z = J, odd term kappa, four-site Bloch matrix H(f) = i M(f). Parametrise by q > 0: kappa = q, J = 8q^2/(1 + 4q^2), which runs once over J in (0, 2) and satisfies kappa^2 = J/[4(2 - J)], the handover coupling of open PR 9350, whose two plane families of touchings both reach f+- = (x, 1 - x, 1/2) with e^{2 pi i x} = (2q +- i)^2/(1 + 4q^2). Exact rational algebra in q (sympy), for every q > 0: det(H - lambda) = lambda^2 (lambda^2 - c) with c = 256 q^2 (8q^2 + 1)/(4q^2 + 1)^2; D = det H and its gradient vanish and its Hessian is 4 pi^2 h(q) (1, -1, 0)(1, -1, 0)^T with h(q) = 512 q^2 (8q^2 + 1)(128q^6 + 16q^4 + 16q^2 + 1)/(4q^2 + 1)^4 > 0; with u = d1 - d2 (weight two), v = d1 + d2, t = d3 (weight one), D vanishes to weighted order three and its weighted-degree-4 part equals c |d|^2, where d is the Pauli vector of the effective two-level Hamiltonian to weighted order two (no first-order (v, t) part, no identity part, d = n u + quadratic(v, t), n != 0); the homogeneous resultant of the two components of the quadratic part transverse to n is -2^21 q^10 (6q^2 + 1)(12q^2 + 1)^2/(8q^2 + 1)^4 < 0, so their zero lines interlace, d has an isolated zero and d/|d| has local degree of magnitude two. So at the handover the merged touchings are isolated charge-two points for every J in (0, 2), extending open PR 9357 (J = 1). Floating-point sphere fluxes at J = 2/5 and 8/5 are -2 at f+ and +2 at f-. No statement at other couplings, anisotropies J_x != J_y, exact touching count at kappa_h, spin-Hamiltonian equivalence, phase or physical identification."
upstream_dependencies:
  - minimal_axioms
  - the_hyperhoneycomb_embeds_in_the_doubled_cubic_lattice_a_three_dimensional_composite_site_network_with_an_exact_charge_bounded_theorem_note_2026-09-24
  - composite_site_network_flux_free_bands_with_the_odd_term_two_certified_touchings_of_opposite_charge_become_six_at_kappa_root_3_over_20_bounded_theorem_note_2026-09-26
runner: scripts/composite_site_network_flux_free_handover_touchings_are_exact_charge_two_points_for_every_j_2026_09_28.py
---

# At the handover the flux-free comparator's merged touchings are exact charge-two points for every J between 0 and 2

**Date:** 2026-09-28
**Type:** bounded_theorem
**Status:** exact local algebra for a supplied comparator on a one-parameter family of couplings; unaudited.

## Supplied setting

Use the supplied comparator of the landed note
[COMPOSITE_SITE_NETWORK_FLUX_FREE_BANDS_WITH_THE_ODD_TERM_TWO_CERTIFIED_TOUCHINGS_OF_OPPOSITE_CHARGE_BECOME_SIX_AT_KAPPA_ROOT_3_OVER_20_BOUNDED_THEOREM_NOTE_2026-09-26](COMPOSITE_SITE_NETWORK_FLUX_FREE_BANDS_WITH_THE_ODD_TERM_TWO_CERTIFIED_TOUCHINGS_OF_OPPOSITE_CHARGE_BECOME_SIX_AT_KAPPA_ROOT_3_OVER_20_BOUNDED_THEOREM_NOTE_2026-09-26.md):
the colored network of
[THE_HYPERHONEYCOMB_EMBEDS_IN_THE_DOUBLED_CUBIC_LATTICE_A_THREE_DIMENSIONAL_COMPOSITE_SITE_NETWORK_WITH_AN_EXACT_CHARGE_BOUNDED_THEOREM_NOTE_2026-09-24](THE_HYPERHONEYCOMB_EMBEDS_IN_THE_DOUBLED_CUBIC_LATTICE_A_THREE_DIMENSIONAL_COMPOSITE_SITE_NETWORK_WITH_AN_EXACT_CHARGE_BOUNDED_THEOREM_NOTE_2026-09-24.md),
`u = +1`, one quadratic copy, the landed four-site reduction `H(f) = i M(f)`,
couplings `J_x = J_y = 1`, `J_z = J` and odd term `κ`.

**Where the handover happens.** Open PR 9350 found three exact families of
touchings of the middle bands. The touchings of the plane `f₁ + f₂ = 1` hand
over to those of the plane `f₁ + f₂ = 2f₃` at `κ_h² = J/[4(2 − J)]`. Open PR
9357 showed that at `J = 1`, `κ = 1/2` the merged touchings are exact
charge-two points. That note left the handover at other `J` open.

**Parametrisation.** Set `κ = q` and `J = 8q²/(1 + 4q²)` for `q > 0`. Then:
- `J` increases from 0 to 2 as `q` runs over `(0, ∞)`, so each `J` in
  `(0, 2)` occurs once;
- `κ² = κ_h²`;
- the merged touchings are `f± = (x, 1 − x, 1/2)` with
  `e^{2πix} = (2q ± i)²/(1 + 4q²)`, a rational point of the circle.

So every quantity below is a rational function of `q`, and the algebra holds
for every `J` at once. The coordinates used throughout are `u = δ₁ − δ₂`
(weight two) and `v = δ₁ + δ₂`, `t = δ₃` (weight one), measured from `f±`.

## Result

All statements hold for every `q > 0`, at both `f+` and `f−`.

1. **Both families meet at f±.** At `κ = q`:
   - family (ii) of open PR 9350 has `cos 2πf₃ = −1` and
     `cos 2πx = J − 1 = (4q² − 1)/(4q² + 1)`;
   - family (iii) has `√(5J² + 8J + J(J + 2)/κ²) = J + 4`, so
     `cos 2πf₃ = −1` and `cos 2π(1/2 + g) = J − 1`.
2. **Double zero level.** `det(H − λ) = λ²(λ² − c)` with
   `c = 256q²(8q² + 1)/(4q² + 1)²`, which is `48` at `J = 1`.
3. **Rank-one Hessian.** `D = det H` and its gradient vanish. Its Hessian is
   `4π² h(q) (1, −1, 0)(1, −1, 0)ᵀ`, with
   `h(q) = 512q²(8q² + 1)(128q⁶ + 16q⁴ + 16q² + 1)/(4q² + 1)⁴`, which is
   positive and equals `192` at `J = 1`. `D` also vanishes to weighted
   order three.
4. **Effective Hamiltonian.** Use the kernel projector and `H⁻¹ = H/c` on its
   complement. The displayed kernel vectors are orthogonal with squared norms two;
   all matrix elements, including the cross element, are divided by those norms
   to obtain an orthonormal two-level basis. To weighted order two:
   - the first-order projection in `v` and `t` vanishes, and so does the
     identity part;
   - the Pauli vector is `d = n u + (quadratic in v, t)`;
   - `n = (2π, ∓4πq, 4πq(4q² − 1)/(4q² + 1))` at `f±`, never zero.
5. **Two computations agree.** The weighted-degree-4 part of `D`, from the
   determinant, equals `c |d|²` from the effective Hamiltonian, identically
   in `q`.
6. **Charge two.** Transverse to `n`, the quadratic part has two components:
   - at `f+` they are `A = 8q²(12q² + 1) v(2t − v)/(8q² + 1)` and
     `B = 32q²((4q² + 1)v² + 8q²tv − 8q²t²)/(8q² + 1)`;
   - their homogeneous resultant is
     `−2²¹ q¹⁰ (6q² + 1)(12q² + 1)²/(8q² + 1)⁴`, negative for every `q > 0`,
     and the same at `f−`.

   For two binary quadratic forms, a negative resultant means both have
   real, distinct zero lines and the lines interlace. Therefore:
   - the transverse part has no common zero, so near `f±` the vector `d` vanishes at `f±` alone;
   - by item 5, `D > 0` on a punctured neighbourhood, so the touching is
     isolated;
   - the transverse part winds twice around the circle, so `d/|d|` has local
     degree of magnitude two on a small weighted sphere; the `u`-linear part
     sets the sign;
   - higher weighted orders do not change the degree on a small enough
     sphere.
7. **Consistency (floating point).** At `J = 2/5` (`κ = 1/4`) and
   `J = 8/5` (`κ = 1`), discrete sphere fluxes of the lowest two bands on
   spheres of radius `0.004` and `0.008` around `f+` and `f−` are `−2` and
   `+2`.

## What this settles and what it does not

- **Settled.** At the handover coupling, the merged touchings are isolated
  charge-two points for every `J` in `(0, 2)`: linear along `(1, −1, 0)` and
  quadratic across it. The `J = 1` statement of open PR 9357 is the case
  `q = 1/2`, and its numbers (`c = 48`, Hessian `192`) are reproduced.
- **Not settled here.**
  - The sign convention linking the degree to the flux sign; the
    floating-point fluxes give the signs at two couplings.
  - The exact touching count at `κ_h`.
  - Couplings off the handover, and anisotropies `J_x ≠ J_y`.
  - Equality with the spin model.

## Evidence limits and No-Go Discipline Gate

- **N1:** supplied comparator with `J_x = J_y = 1`, `J_z = J` in `(0, 2)`, at `κ = κ_h`, two points.
- **N2:** no phase or no-go wall is imported.
- **N3:** network, hopping signs and the `u = +1` sector remain supplied.
- **N4:** the landed parent's reduction is used as stated there; open PR 9350's families are checked at `κ_h`, not assumed.
- **N5:** exact local algebra in `q`; the float fluxes are a consistency check.
- **N6:** the exact count at `κ_h` and anisotropic couplings remain open.
- **N7:** other sectors and couplings remain available.
- **N8:** no physical identification, new premise or audit verdict.

## Reproduction

```bash
python3 scripts/composite_site_network_flux_free_handover_touchings_are_exact_charge_two_points_for_every_j_2026_09_28.py
```

Seven checks; prints `TOTAL: PASS=7 FAIL=0` in about ten seconds.

## Coupled source inputs

- [Reviewed 9350 source](COMPOSITE_SITE_NETWORK_FLUX_FREE_MIDDLE_BANDS_TOUCH_AT_TWO_EXACT_POINTS_BELOW_KAPPA_STAR_AND_SIX_ABOVE_BY_AN_INTERVAL_CERTIFICATE_BOUNDED_THEOREM_NOTE_2026-09-26.md).
- [Reviewed 9357 source](COMPOSITE_SITE_NETWORK_FLUX_FREE_TOUCHINGS_AT_KAPPA_ONE_HALF_ARE_EXACT_CHARGE_TWO_POINTS_BOUNDED_THEOREM_NOTE_2026-09-27.md).

## Premise authority

[Current axiom memo](MINIMAL_AXIOMS_2026-06-29.md).
