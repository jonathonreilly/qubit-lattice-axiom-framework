---
claim_id: composite_site_network_flux_free_the_line_touchings_and_their_charges_are_exact_for_general_couplings_bounded_theorem_note_2026-10-01
claim_type: bounded_theorem
claim_scope: "Supplied u=+1 quadratic Majorana comparator of the landed notes, one copy, the landed hopping-sign convention, general couplings J_x, J_y, J_z > 0 and odd term kappa > 0, four-site Bloch matrix H(f) = i M(f). Exact (sympy, symbolic in all couplings): the characteristic polynomial of M has no mu^3 or mu^1 term for every f, so the spectrum is {+-lambda1, +-lambda2}, det H >= 0 and a zero-energy touching of the middle bands is exactly a zero of det H. On the line f = (x, 1-x, 0), det H = 16 q(c)^2 with q(c) = 4 kappa^2 c^2 - 2 J_x J_y c + J_z^2 - J_x^2 - J_y^2 - 4 kappa^2, c = cos 2 pi x (the landed polynomial at J_x = J_y = 1); at a root the levels are (0, 0, +-4 J_z) and all 3 x 3 minors of M vanish (a double zero). From q(+-1) and the discriminant identities: in the triangle regime |J_x - J_y| < J_z < J_x + J_y exactly one root c_- lies in (-1, 1) for every kappa (two line nodes); for J_z > J_x + J_y two roots for kappa above an explicit threshold (four nodes); for J_z < |J_x - J_y| none. The chirality T = Im Tr(P d1H P d2H P d3H) = 64 pi^3 kappa d F_c(c_-) sin(2 pi x)/J_z^3 at the x < 1/2 node, with F_c(c) = J_x J_y (J_x+J_y+J_z) c^2 + (J_x+J_y)(J_x^2+J_y^2+J_z(J_x+J_y)) c + (J_x+J_z)(J_y+J_z)(J_x+J_y-J_z) and d > 0; it reduces to the landed isotropic formula; F_c(-1) < 0 and c_-(kappa) decreases strictly, so in the triangle regime the charge of the x < 1/2 node flips from +1 to -1 exactly once iff |J_x^2 - J_y^2| < J_z^2 and is -1 for every kappa otherwise. The shear f -> (f1, f2, f1 + f2 - f3) is a spectral symmetry iff J_x = J_y. Independent exact rational arithmetic at 2400 couplings agrees; the closed forms reproduce the line nodes and chirality signs of the anisotropic certificate at five couplings to 50 digits. Reported, not asserted: a closed form for the flip coupling (numerically verified) and a PSLQ identification of the off-plane nodes as roots of an integer quintic. Not covered: off-plane nodes exactly, spin-model equivalence or physical reading."
upstream_dependencies:
  - minimal_axioms
  - the_hyperhoneycomb_embeds_in_the_doubled_cubic_lattice_a_three_dimensional_composite_site_network_with_an_exact_charge_bounded_theorem_note_2026-09-24
  - composite_site_network_flux_free_middle_bands_touch_at_two_exact_points_below_kappa_star_and_six_above_by_an_interval_certificate_bounded_theorem_note_2026-09-26
runner: scripts/composite_site_network_flux_free_exact_line_touchings_and_charges_for_general_couplings_2026_10_01.py
---

# The line touchings of the flux-free comparator and their charges are exact for general couplings

**Date:** 2026-10-01
**Type:** bounded_theorem
**Status:** exact symbolic algebra for a supplied comparator; unaudited.

## Supplied setting

Use the supplied comparator of the landed note
[current mathematical parent](COMPOSITE_SITE_NETWORK_FLUX_FREE_MIDDLE_BANDS_TOUCH_AT_TWO_EXACT_POINTS_BELOW_KAPPA_STAR_AND_SIX_ABOVE_BY_AN_INTERVAL_CERTIFICATE_BOUNDED_THEOREM_NOTE_2026-09-26.md)
with general couplings `J_x`, `J_y`, `J_z > 0` and `κ > 0`. That note's
exact families assume `J_x = J_y`. For `J_x ≠ J_y`, a numerical study
of the anisotropic comparator located candidate touchings on the line `f₁ + f₂ = 1`,
`f₃ = 0` besides off-plane ones. This block treats that line exactly for all
couplings.

Write `c = cos 2πx`, `P = J_xJ_y` and `u = κ²`.

## Result

1. **The spectrum is symmetric everywhere.** The characteristic polynomial
   of `M` has no `μ³` or `μ¹` term, for every `f` and all couplings. So
   `spec H = {±λ₁, ±λ₂}` and `det H = λ₁²λ₂² ≥ 0`. A zero-energy touching
   of the middle bands is exactly a zero of `det H`.
2. **The line.** On `f = (x, 1−x, 0)`, `det H = 16 q(c)²`, with
   `q(c) = 4κ²c² − 2J_xJ_y c + J_z² − J_x² − J_y² − 4κ²`. At
   `J_x = J_y = 1` this is the landed line polynomial.
3. **Double zero.** At a root of `q` the levels are `(0, 0, ±4J_z)`, the
   kernel projector has rank two, and all sixteen 3 × 3 minors of `M`
   vanish. So the gradient of `det H` vanishes there too.
4. **Where the line nodes exist.** This follows from
   `q(1) = J_z² − (J_x + J_y)²`, `q(−1) = J_z² − (J_x − J_y)²` and the
   discriminant identities.
   - **Triangle regime** `|J_x − J_y| < J_z < J_x + J_y`: exactly one root
     `c₋ ∈ (−1, 1)` for every `κ`, giving two line nodes.
   - **`J_z > J_x + J_y`:** two roots when `κ` is above an explicit
     threshold, giving four nodes.
   - **`J_z < |J_x − J_y|`:** no root.
5. **Charge.** At the `x < 1/2` node,
   `T = Im Tr(P∂₁H P∂₂H P∂₃H) = 64π³κ d F_c(c₋) sin(2πx)/J_z³`, with `d > 0`
   and
   `F_c(c) = J_xJ_y(J_x+J_y+J_z)c² + (J_x+J_y)(J_x²+J_y²+J_z(J_x+J_y))c + (J_x+J_z)(J_y+J_z)(J_x+J_y−J_z)`.
   - Where `T ≠ 0`, the node is conical with chirality `sign T`; the partner
     has the opposite sign. At a flip `T = 0`, this linear test gives no
     conical charge or merged-point local degree.
   - At `J_x = J_y = 1` this equals the landed isotropic formula, to 50
     digits at nine couplings.
6. **When the charge flips.**
   - `F_c(−1) = −(J_x+J_y)(J_x−J_y)² − J_z³ < 0`.
   - `c₋(κ)` decreases strictly from its `κ → 0` value to `−1`.
   - So in the triangle regime, the charge of the `x < 1/2` node goes from
     `+1` to `−1` exactly once iff `|J_x² − J_y²| < J_z²`. Otherwise it is
     `−1` for every `κ`.
   - An exact rational test confirms this at 300 couplings and 83 values of
     `κ` each.
7. **Shear symmetry.** `f → (f₁, f₂, f₁ + f₂ − f₃)` is a spectral symmetry
   iff `J_x = J_y`. `det M(Rf) − det M(f)` carries the factor `J_x − J_y`.
8. **Cross-checks.**
   - Independent exact rational arithmetic at 2400 couplings (1833 nodes)
     agrees.
   - The closed forms reproduce, to 50 digits, the line nodes and chirality
     signs of the anisotropic certificate at five couplings:
     `(1, 0.8, 1; 0.45)`, `(1.2, 0.8, 1; 0.3)`, `(1, 0.8, 1; 0.8)`,
     `(1.2, 0.8, 1; 0.2)` and `(0.9, 1.1, 1.3; 0.4)`.

**Reported, not asserted:**
- a closed form for the flip coupling `κ_c`, numerically verified;
- a PSLQ identification that the off-plane touchings' `cos 2πf₃` satisfies
  an integer quintic, with `cos 2πf₁ + cos 2πf₂` and their product
  polynomial in it. This corrects an earlier impression that they are not
  low-degree algebraic, but it is an identification, not a proof.

## What this settles and what it does not

- **Settled.** For all couplings, the line touchings are exact, with an
  explicit existence regime and an exact charge. The charge flips exactly
  once with `κ` in the triangle regime iff `|J_x² − J_y²| < J_z²`. The
  symmetric spectrum makes `det H` an exact touching detector everywhere.
- **Not settled here.**
  - The off-plane nodes exactly.
  - The flip coupling as a proved identity.
  - Equality with the spin model, and any physical reading.

## Evidence limits and No-Go Discipline Gate

- **N1:** supplied comparator with general positive couplings.
- **N2:** no phase or no-go wall is imported.
- **N3:** network, hopping signs and the `u = +1` sector remain supplied.
- **N4:** the landed families are recovered at `J_x = J_y`.
- **N5:** exact symbolic identities and exact rational grids; 50-digit cross-checks.
- **N6:** off-plane nodes exactly and the flip coupling remain open.
- **N7:** other sectors remain available.
- **N8:** no physical identification, new premise or audit verdict.

## Reproduction

```bash
python3 scripts/composite_site_network_flux_free_exact_line_touchings_and_charges_for_general_couplings_2026_10_01.py
```

Ten checks; prints `TOTAL: PASS=10 FAIL=0` in about thirty seconds.

For the triangle-regime sign statement, `F_c` is an upward quadratic with
`F_c(−1)<0`, so it has exactly one crossing to the right of `−1`. Its value
at `c₀=(J_z²−J_x²−J_y²)/(2J_xJ_y)` has the sign of
`(J_y²+J_z²−J_x²)(J_x²+J_z²−J_y²)`. Implicit differentiation of `q(c₋)=0`
gives `dc₋/d(κ²)=−2(1−c₋²)/d<0`. These signs establish the unique flip
criterion; a finite rational grid is only a cross-check.

The [current axiom memo](MINIMAL_AXIOMS_2026-06-29.md) sets the premise boundary. The supplied comparator is not a framework-law or physical-species selection. Original source and execution history remain recoverable at [PR #9426](https://github.com/jonathonreilly/qubit-lattice-axiom-framework/pull/9426); this is provenance, not audit authority.

Network definition: [current supplied network](THE_HYPERHONEYCOMB_EMBEDS_IN_THE_DOUBLED_CUBIC_LATTICE_A_THREE_DIMENSIONAL_COMPOSITE_SITE_NETWORK_WITH_AN_EXACT_CHARGE_BOUNDED_THEOREM_NOTE_2026-09-24.md).
