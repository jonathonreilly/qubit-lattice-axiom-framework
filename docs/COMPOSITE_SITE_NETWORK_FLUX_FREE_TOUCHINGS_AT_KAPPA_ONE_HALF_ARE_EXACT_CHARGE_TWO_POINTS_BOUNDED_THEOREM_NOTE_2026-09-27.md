---
claim_id: composite_site_network_flux_free_touchings_at_kappa_one_half_are_exact_charge_two_points_bounded_theorem_note_2026-09-27
claim_type: bounded_theorem
claim_scope: "Supplied u=+1 quadratic Majorana comparator of the landed notes, one copy, the landed hopping-sign convention, J = 1, four-site Bloch matrix H(f) = i M(f), at kappa = 1/2. At f+ = (1/4, 3/4, 1/2) and f- = (3/4, 1/4, 1/2): det(H - lambda) = lambda^2 (lambda^2 - 48) exactly; D = det H and its gradient vanish and its Hessian has rank one (4 pi^2 x 192 [[1, -1, 0], [-1, 1, 0], [0, 0, 0]]). With u = d1 - d2 (weight two) and v = d1 + d2, t = d3 (weight one), D vanishes to weighted order three and its weighted-degree-4 part 64 pi^2 [6u^2 + 4 pi u t (v - t) + pi^2 (v^2 - v t + t^2)^2] is positive definite. The effective two-level Hamiltonian to weighted order two (kernel projector I - H^2/48) has no identity part and Pauli vector 2 pi u (1, 1, 0) + (2 pi^2/3)(v^2 - tv - t^2, -v^2 + 3tv - t^2, t^2 - tv - v^2) at f+; transverse to its u direction the quadratic part has no common zero and alternating zero directions, so the normalized Pauli vector has local degree of magnitude two. So both touchings are charge-two points, linear along (1, -1, 0) and quadratic across it; floating-point sphere fluxes on spheres enclosing only them are -2 at f+ and +2 at f-. No statement at other couplings, exact touching count at kappa = 1/2, spin-Hamiltonian equivalence, phase or physical identification."
upstream_dependencies:
  - minimal_axioms
  - the_hyperhoneycomb_embeds_in_the_doubled_cubic_lattice_a_three_dimensional_composite_site_network_with_an_exact_charge_bounded_theorem_note_2026-09-24
  - composite_site_network_flux_free_bands_with_the_odd_term_two_certified_touchings_of_opposite_charge_become_six_at_kappa_root_3_over_20_bounded_theorem_note_2026-09-26
runner: scripts/composite_site_network_flux_free_touchings_at_kappa_one_half_are_exact_charge_two_points_2026_09_27.py
---

# At κ = 1/2 the flux-free comparator's touchings at (1/4, 3/4, 1/2) and (3/4, 1/4, 1/2) are exact charge-two points

**Date:** 2026-09-27
**Type:** bounded_theorem
**Status:** exact local algebra for a supplied comparator at one coupling; unaudited.

## Supplied setting

Use the supplied comparator of the landed note
`COMPOSITE_SITE_NETWORK_FLUX_FREE_BANDS_WITH_THE_ODD_TERM_TWO_CERTIFIED_TOUCHINGS_OF_OPPOSITE_CHARGE_BECOME_SIX_AT_KAPPA_ROOT_3_OVER_20_BOUNDED_THEOREM_NOTE_2026-09-26.md`:
the colored network of
`THE_HYPERHONEYCOMB_EMBEDS_IN_THE_DOUBLED_CUBIC_LATTICE_A_THREE_DIMENSIONAL_COMPOSITE_SITE_NETWORK_WITH_AN_EXACT_CHARGE_BOUNDED_THEOREM_NOTE_2026-09-24.md`,
`u = +1`, one quadratic copy, the landed four-site reduction `H(f) = i M(f)`,
and `J = 1`, `κ = 1/2`.

At `(1/4, 3/4, 1/2)` the landed note proved
`det(H − λ) = (λ² − 48(1/2 − κ)²)(λ² − 48(1/2 + κ)²)`, a double zero level at
`κ = 1/2`. At that coupling it found four numerical groups with rounded sphere
fluxes −2, −1, +1 and +2, the two larger ones near `(1/4, 3/4, 1/2)` and its
partner. Its spheres did not enclose the whole groups, so it could not assign
those fluxes as net charges. In open PR 9350 these are the points where the
two plane families of touchings hand over.

## Result

The coordinates used throughout: `u = δ₁ − δ₂` (weight two) and
`v = δ₁ + δ₂`, `t = δ₃` (weight one), measured from `f±`.

1. **Double zero level.** At `f+ = (1/4, 3/4, 1/2)` and
   `f− = (3/4, 1/4, 1/2)`:
   - `det(H − λ) = λ²(λ² − 48)`;
   - `D = det H` and its gradient vanish;
   - the Hessian of `D` is `4π² · 192 [[1, −1, 0], [−1, 1, 0], [0, 0, 0]]`,
     rank one, curved only along `(1, −1, 0)`.
2. **Positive weighted form of D.** `D` vanishes to weighted order three, and
   its weighted-degree-4 part at `f+` is
   `64π²[6u² + 4πu·t(v − t) + π²(v² − vt + t²)²]`. It is positive definite:
   after completing the square in `u`, the residual quartic in `s = v/t` is
   `192s⁴ − 384s³ + 448s² − 128s + 64` (times `π⁴/3`), which has no real root
   and a positive leading coefficient.
3. **Effective Hamiltonian.** Use the kernel projector `P = I − H²/48` and
   `H⁻¹ = H/48` on its complement. To weighted order two:
   - the first-order projection in `v` and `t` vanishes, and so does the
     identity part;
   - the Pauli vector at `f+` is
     `d = 2πu (1, 1, 0) + (2π²/3)(v² − tv − t², −v² + 3tv − t², t² − tv − v²)`;
   - at `f−` the vector differs by the signs the runner prints.
4. **Charge two.** Transverse to the `u` direction, the two components of the
   quadratic part have no common zero. Their zero directions in the
   `(v, t)` plane alternate: `0.4636` and `1.5708` for one, `1.0172` and
   `2.588` for the other (angles of `(v, t)`).
   - So `d` vanishes only at the point itself, and on a small weighted sphere
     the normalized vector `d/|d|` has degree of magnitude two. The
     quadratic part winds twice, and the `u`-linear part sets the sign.
   - Higher weighted orders do not change the degree on a small enough
     sphere.
   - Both touchings are charge-two points: linear along `(1, −1, 0)` and
     quadratic across it.
5. **Consistency (floating point).** Discrete sphere fluxes of the lowest two
   bands on spheres of radius `0.004` and `0.008`, which enclose only these
   points, are `−2` at `f+` and `+2` at `f−`, as the landed rounded fluxes
   suggested.

## What this settles and what it does not

- **Settled.** The landed note's `κ = 1/2` observation of two charge-magnitude-two
  groups at the rational points now holds as an exact local statement. Each
  is an isolated touching, since the positive weighted form makes `D > 0` on
  a punctured neighbourhood, and each has local degree of magnitude two.
- **Not settled here.**
  - The sign convention linking the degree to the landed flux sign; the
    floating-point fluxes give the signs.
  - The exact touching count at `κ = 1/2`: the rank-one Hessian defeats the
    Hessian test of open PR 9350, so a weighted uniqueness bound is needed.
  - Other couplings or anisotropies.
  - Equality with the spin model.

## Evidence limits and No-Go Discipline Gate

- **N1:** supplied comparator at `J = 1`, `κ = 1/2`, two points.
- **N2:** no phase or no-go wall is imported.
- **N3:** network, hopping signs and the `u = +1` sector remain supplied.
- **N4:** the landed parent's reduction and rational-point polynomial are used as stated there.
- **N5:** exact local expansions; the float fluxes are a consistency check.
- **N6:** the exact count at `κ = 1/2` and the general-`J` handover remain open.
- **N7:** other sectors and couplings remain available.
- **N8:** no physical identification, new premise or audit verdict.

## Reproduction

```bash
python3 scripts/composite_site_network_flux_free_touchings_at_kappa_one_half_are_exact_charge_two_points_2026_09_27.py
```

Five checks; prints `TOTAL: PASS=5 FAIL=0` in about ten seconds.
