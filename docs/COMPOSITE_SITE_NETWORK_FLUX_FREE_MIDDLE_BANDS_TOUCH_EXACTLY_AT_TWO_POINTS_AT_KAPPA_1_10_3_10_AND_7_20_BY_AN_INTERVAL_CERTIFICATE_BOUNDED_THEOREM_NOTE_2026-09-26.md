---
claim_id: composite_site_network_flux_free_middle_bands_touch_exactly_at_two_points_at_kappa_1_10_3_10_and_7_20_by_an_interval_certificate_bounded_theorem_note_2026-09-26
claim_type: bounded_theorem
claim_scope: "Supplied u=+1 quadratic Majorana comparator of the landed notes, one copy, the landed hopping-sign convention, isotropic J = 1, four-site Bloch matrix H(f) = i M(f). For kappa = 1/10, 3/10 and 7/20, det H(f) vanishes exactly at the two points +-f*, f* = (x*, 1 - x*, 0) with cos 2 pi x* = [1 - sqrt(1 + 4 kappa^2 + 16 kappa^4)]/(4 kappa^2). At these points zero is a double level, with the two outer levels nonzero. At every other point of the zone H has exactly two negative and two positive levels, so the middle gap is open. Computer-assisted: exact rational algebra, which holds for every kappa, plus interval arithmetic (outward-rounded IEEE float operations and mpmath interval phases) with the landed Lipschitz bound. No node charge, dispersion order, other coupling, interval of couplings, spin-Hamiltonian equivalence, ground-sector selection, phase or physical identification."
upstream_dependencies:
  - minimal_axioms
  - the_hyperhoneycomb_embeds_in_the_doubled_cubic_lattice_a_three_dimensional_composite_site_network_with_an_exact_charge_bounded_theorem_note_2026-09-24
  - composite_site_network_flux_free_bands_with_the_odd_term_two_certified_touchings_of_opposite_charge_become_six_at_kappa_root_3_over_20_bounded_theorem_note_2026-09-26
runner: scripts/composite_site_network_flux_free_middle_bands_touch_exactly_at_two_line_points_interval_certificate_2026_09_26.py
---

# The flux-free comparator's middle bands touch exactly at two points at κ = 1/10, 3/10 and 7/20

**Date:** 2026-09-26
**Type:** bounded_theorem
**Status:** computer-assisted certificate for a supplied comparator at three couplings; unaudited.

## Supplied setting

Use the supplied comparator of the landed note
`COMPOSITE_SITE_NETWORK_FLUX_FREE_BANDS_WITH_THE_ODD_TERM_TWO_CERTIFIED_TOUCHINGS_OF_OPPOSITE_CHARGE_BECOME_SIX_AT_KAPPA_ROOT_3_OVER_20_BOUNDED_THEOREM_NOTE_2026-09-26.md`:
the colored network of
`THE_HYPERHONEYCOMB_EMBEDS_IN_THE_DOUBLED_CUBIC_LATTICE_A_THREE_DIMENSIONAL_COMPOSITE_SITE_NETWORK_WITH_AN_EXACT_CHARGE_BOUNDED_THEOREM_NOTE_2026-09-24.md`
with the explicitly supplied real antisymmetric hopping matrix. Take `u = +1`,
one quadratic copy, the landed four-site reduction `H(f) = i M(f)` over the
fractional zone, and `J = 1`.

That note left several things open, including a certified exclusion of zeros
outside its numerical groups and an exact node count. It also retained two
facts used here:
- the line identity `D = 16[1 + 4c²κ² − 2c − 4κ² − 2]²` on
  `f = (x, 1 − x, 0)`, with `c = cos 2πx`;
- the Lipschitz bound `‖H(f) − H(f′)‖ ≤ lip ‖f − f′‖∞`.

This block answers the node-count question at three couplings below
`κ* = √(3/20)`.

## Result

**Theorem (computer-assisted).** For `κ = 1/10`, `3/10` and `7/20`, `det H(f)`
vanishes exactly at `±f*`, with `f* = (x*, 1 − x*, 0)` and
`cos 2πx* = [1 − √(1 + 4κ² + 16κ⁴)]/(4κ²)`.
- At `±f*`, zero is a double level and the outer two levels are nonzero.
- At every other point of the zone, `H` has exactly two negative and two
  positive levels.

So the two middle bands touch exactly at two points, at zero energy, and the
middle gap is open everywhere else.

The enclosed node positions are `x* ∈ [0.336048651569, 0.336048651571]`,
`[0.354913386979, 0.354913386981]` and `[0.361266669448, 0.361266669450]`.

## Proof structure

1. **Exact algebra, every κ.** The determinants are exact polynomial-ring
   determinants with rational amplitudes `2J = 2` and `2κ`. On the line
   `z₂ = 1/z₁`, `w = 1`, the following all vanish modulo
   `P_κ(z) = κ²z⁴ − z³ − (1 + 2κ²)z² − z + κ²`, with `z = e^{2πix}`:
   - `D = det H`;
   - the three momentum derivatives `∂D/∂f_j = 2πi z_j ∂D/∂z_j`;
   - the constant and linear coefficients of `det(H − λ)`.

   So at every root of `P_κ`, `D = 0`, `∇D = 0` and `λ = 0` has multiplicity
   at least two. For `κ > 0`, `P_κ` has exactly the two unit-circle roots
   `e^{±2πix*}`, which give `±f*`. At the three couplings `P_κ` is
   irreducible over the rationals and the quadratic coefficient's remainder
   is nonzero, so the multiplicity is exactly two.

   Two consistency checks tie this to the landed note: the same computation
   reproduces the landed line identity, and it reproduces the characteristic
   polynomial `(λ² − 48(1/2 − κ)²)(λ² − 48(1/2 + κ)²)` at `(1/4, 3/4, 1/2)`.
2. **Rigorous clearing.** Cubes `[c − h, c + h]³` with exact dyadic centres
   start from `32³` and are split eight ways, thirteen times. For each cube:
   - `H(c)` is enclosed entrywise, using `mpmath` interval phases and
     outward-rounded float arithmetic (one `nextafter` step per correctly
     rounded IEEE operation);
   - interval `LDL*` factorizations of `H(c) ∓ rI` give certified negative
     counts, with `r` rounded up from `lip·h`;
   - equal counts at `±r` mean `H(c)` has no level in `[−r, r]`, so by
     Weyl's inequality no level vanishes in the cube and the negative count
     holds throughout.

   Every cleared cube has negative count exactly 2. The uncleared cubes form
   two groups at each coupling.
3. **Boxes.** The bounding box of each group contains its exact node, and on
   the whole box the interval Hessian of `D` is positive definite (interval
   Cholesky):

   | κ | box widths | smallest pivot |
   |---|---|---|
   | 1/10 | `2.4e-4`, `2.4e-4`, `2.4e-4` | at least `72` |
   | 3/10 | `1.8e-4`, `1.8e-4`, `3.7e-4` | at least `122` |
   | 7/20 | `1.8e-4`, `1.8e-4`, `8.1e-4` | at least `13` |

   With `D(f*) = 0` and `∇D(f*) = 0`, Taylor's theorem along segments in the
   convex box gives `D > 0` on the box except at `f*`.
4. **Conclusion.**
   - `D ≠ 0` off `±f*`.
   - The negative count is locally constant where `D ≠ 0`. It is 2 on the
     cleared cubes and on each punctured box, which is connected and meets
     the cleared cubes.
   - So `λ₂ < 0 < λ₃` off `±f*`. At `±f*`, `λ₂ = λ₃ = 0` with `λ₁ < 0 < λ₄`.

A sanity check also passes: at dyadic points the interval matrices contain
40-digit evaluations of the entries, and the interval inertia agrees with
floating eigenvalue counts.

## What this settles and what it does not

- At these couplings the landed note's two numerical groups contain exactly
  one touching each, at the exact line points, and no other zero exists
  anywhere in the zone.
- The smallest Hessian pivot falls from about `122` at `κ = 3/10` to about
  `13` at `7/20`, and the box stretches along `f₃`. This is consistent with
  the landed curvature identity, which vanishes at `κ* = √(3/20)`. The
  softening itself is a finite observation, not a statement about `κ*`.
- Not certified here:
  - the node charges (the landed discrete fluxes remain diagnostics);
  - the dispersion order;
  - any coupling between the sampled values, including a statement for an
    interval of `κ`;
  - the six-group regime above `κ*`;
  - anisotropic couplings;
  - equality with the spin model.

## Arithmetic boundary

The certificate assumes:
- IEEE 754 double precision with round-to-nearest for `+ − × ÷`, so one
  outward `nextafter` step encloses each exact result;
- the correctness of `mpmath`'s interval `cos` and `sin`;
- `sympy`'s exact rational polynomial arithmetic.

Floating eigenvalues enter the sanity check and nothing in the certificate.

## Evidence limits and No-Go Discipline Gate

- **N1:** supplied comparator at three rational couplings, `J = 1`.
- **N2:** no phase or no-go wall is imported.
- **N3:** network, hopping signs and the `u = +1` sector remain supplied.
- **N4:** the landed parent's reduction, line identity and Lipschitz bound are used as stated there.
- **N5:** an exact count at three couplings; nothing is claimed between them.
- **N6:** charges, a coupling interval and the six-group regime remain open.
- **N7:** other sectors, couplings and certificates remain available.
- **N8:** no physical identification, new premise or audit verdict.

## Reproduction

```bash
python3 scripts/composite_site_network_flux_free_middle_bands_touch_exactly_at_two_line_points_interval_certificate_2026_09_26.py
```

Five checks; prints `TOTAL: PASS=5 FAIL=0` in about thirty seconds.
