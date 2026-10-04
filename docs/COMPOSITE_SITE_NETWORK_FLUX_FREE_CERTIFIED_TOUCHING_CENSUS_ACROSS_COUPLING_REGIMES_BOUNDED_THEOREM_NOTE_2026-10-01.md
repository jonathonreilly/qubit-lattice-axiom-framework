---
claim_id: composite_site_network_flux_free_certified_touching_census_across_coupling_regimes_bounded_theorem_note_2026-10-01
claim_type: bounded_theorem
claim_scope: "Supplied u=+1 quadratic Majorana comparator of the landed notes, one copy, the landed hopping-sign convention, four-site Bloch matrix H(f) = i M(f), D = det M >= 0 (symbolic check), charge = sign of T = Im Tr(P d1H P d2H P d3H), at ten rational couplings (J_x, J_y, J_z; kappa): H1 (6/5, 4/5, 1; 1/5), H2 (6/5, 4/5, 1; 1/4) (triangle regime, either side of the line-node flip), K1 (3/2, 1/2, 11/5; 1), K2 (3/2, 1/2, 11/5; 73/100), K3 (3/2, 1/2, 14/5; 2), K4 (6/5, 4/5, 3; 8/5), K5 (6/5, 4/5, 7/2; 2) (J_z > J_x + J_y), L1 (2, 1/2, 1; 2), L2 (2, 1/2, 1; 9/10), L3 (2, 1/2, 1; 4/5) (J_z < |J_x - J_y|). At each coupling: exact ring verification that M has rank 2 at every listed off-plane orbit (cos 2 pi f_3 a root of an irreducible integer quintic, one real orbit of four points) and at every line root of q; charges signed by outward-rounded interval enclosure of exact expressions and matched to the exact line-family classification; a Hessian-positive-definite box around each touching containing it (unique zero in the box, a2 > 0); and an adaptive outward-rounded Taylor clearing of the whole torus with D > 0 outside the boxes. Census: H1 two line touchings (+, -); H2 four off-plane (+, -, -, +) and two line (-, +); K1 and K3 four off-plane (+, -, -, +) and four line (-, +, -, +); K2 four line (+, -, -, +); K4 and K5 four line (-, +, +, -); L1 and L2 four off-plane (+, -, -, +); L3 none. Total charge 0 at each (a consequence of inversion symmetry, checked). Not covered: couplings between these, boundary couplings J_z = |J_x - J_y|, J_z = J_x + J_y and J_x = J_y, a proof that the off-plane degree is 5 for all couplings, spin-model equivalence or physical reading."
upstream_dependencies:
  - minimal_axioms
  - the_hyperhoneycomb_embeds_in_the_doubled_cubic_lattice_a_three_dimensional_composite_site_network_with_an_exact_charge_bounded_theorem_note_2026-09-24
  - composite_site_network_flux_free_middle_bands_touch_at_two_exact_points_below_kappa_star_and_six_above_by_an_interval_certificate_bounded_theorem_note_2026-09-26
runner: scripts/composite_site_network_flux_free_certified_touching_census_across_coupling_regimes_2026_10_01.py
---

# Certified touching census across coupling regimes

**Date:** 2026-10-01
**Type:** bounded_theorem
**Status:** exact algebra plus outward-rounded interval certificates, for a supplied comparator; unaudited.

## Supplied setting

The comparator is the one in
`COMPOSITE_SITE_NETWORK_FLUX_FREE_MIDDLE_BANDS_TOUCH_AT_TWO_EXACT_POINTS_BELOW_KAPPA_STAR_AND_SIX_ABOVE_BY_AN_INTERVAL_CERTIFICATE_BOUNDED_THEOREM_NOTE_2026-09-26.md`,
with general couplings. `D = det M ≥ 0`. A touching's charge is the sign of
`T = Im Tr(P∂₁H P∂₂H P∂₃H)`, where `P` is the kernel projector.

The ten couplings below cover:
- the triangle regime `|J_x − J_y| < J_z < J_x + J_y`, on both sides of the line-node flip;
- the regime `J_z > J_x + J_y`, before and after the flip, on both sides of the
  birth-sign threshold `J₀`, and beyond `φ(J_x + J_y)`;
- the regime `J_z < |J_x − J_y|`.

## Census

Off-plane charges are listed for the four sign images. Line charges are listed
per root of the line quadratic in increasing `cos 2πx`, each as the `x < 1/2`
node followed by its partner.

| Label | `(J_x, J_y, J_z; κ)` | Regime | Off-plane | Line | Total |
|---|---|---|---|---|---|
| H1 | `(6/5, 4/5, 1; 1/5)` | triangle, below flip | none | `+, −` | 0 |
| H2 | `(6/5, 4/5, 1; 1/4)` | triangle, above flip | `+, −, −, +` | `−, +` | 0 |
| K1 | `(3/2, 1/2, 11/5; 1)` | `J_z > s`, `J_z < J₀`, above flip | `+, −, −, +` | `−, +, −, +` | 0 |
| K2 | `(3/2, 1/2, 11/5; 73/100)` | `J_z > s`, `J_z < J₀`, below flip | none | `+, −, −, +` | 0 |
| K3 | `(3/2, 1/2, 14/5; 2)` | `J_z > s`, `J₀ < J_z < φs`, above flip | `+, −, −, +` | `−, +, −, +` | 0 |
| K4 | `(6/5, 4/5, 3; 8/5)` | `J_z > s`, `J₀ < J_z < φs`, below flip | none | `−, +, +, −` | 0 |
| K5 | `(6/5, 4/5, 7/2; 2)` | `J_z > φs`, no flip | none | `−, +, +, −` | 0 |
| L1 | `(2, 1/2, 1; 2)` | `J_z < \|J_x − J_y\|` | `+, −, −, +` | none | 0 |
| L2 | `(2, 1/2, 1; 9/10)` | `J_z < \|J_x − J_y\|` | `+, −, −, +` | none | 0 |
| L3 | `(2, 1/2, 1; 4/5)` | `J_z < \|J_x − J_y\|` | none | none | 0 |

Here `s = J_x + J_y`.

Patterns at these couplings:
- Among the listed H/K fixtures, an off-plane orbit is present above the
  line-node flip and absent below it or where there is no flip. L1 and L2
  have off-plane orbits despite having no line-node flip. This finite table
  does not establish an all-coupling pattern.
- The line charges agree with the exact line-family classification at every
  coupling where it applies.
- Wherever an off-plane orbit occurs, `cos 2πf₃` is a root of an irreducible
  integer quintic, with one real orbit of four points.

## How each entry is established

1. **Exact rank.** `M` has rank 2 exactly at every listed off-plane point and line
   root. This is checked in the ring `Q[α, t, d, i]/(…)`, or by the exact line
   factor.
2. **Charges.** The sign of `T` comes from outward-rounded enclosures of exact
   expressions.
3. **Isolation.** Around each touching there is a box on which the Hessian of `D`
   is positive definite and the touching lies inside. So it is the unique zero
   there. Also `a₂ > 0` on the box.
4. **Completeness.** The whole torus is cleared on adaptive dyadic cubes, using a
   second-order Taylor lower bound with iv-enclosed phases, `nextafter`-outward
   sums and a third-order remainder. `D > 0` on every cube not contained in a box.
   - At L3 the whole torus clears, so the bands are gapped there.

## Controls

Each of the following fails as it should:
- removing a box leaves uncleared cubes outside;
- a perturbed quintic, a flipped sign, or a perturbed line factor gives a nonzero determinant;
- a wrong listed centre leaves a node unmatched;
- a moved centre puts the node outside its box;
- an oversized box breaks the Hessian test.

Two further comparisons are floating point. The Taylor bound lies below sampled
`D`. On an adversarial trigonometric test, the third-order remainder is needed
and it suffices.

## What this settles and what it does not

- **Settled.** At these ten couplings, the complete set of middle-band touchings
  with their charges. It spans every coupling regime.
- **Not settled here.**
  - Couplings in between.
  - The boundary couplings `J_z = |J_x − J_y|`, `J_z = J_x + J_y` and `J_x = J_y`.
  - A proof that the off-plane degree is 5 for all couplings.
  - Equality with the spin model, and any physical reading.


## Reviewed source connections

- [COMPOSITE_SITE_NETWORK_FLUX_FREE_CERTIFIED_TOUCHING_CENSUS_WITH_CHARGES_AT_FIVE_ANISOTROPIC_COUPLINGS_BOUNDED_THEOREM_NOTE_2026-10-01.md](COMPOSITE_SITE_NETWORK_FLUX_FREE_CERTIFIED_TOUCHING_CENSUS_WITH_CHARGES_AT_FIVE_ANISOTROPIC_COUPLINGS_BOUNDED_THEOREM_NOTE_2026-10-01.md)
- [COMPOSITE_SITE_NETWORK_FLUX_FREE_LINE_NODES_OUTSIDE_THE_COUPLING_TRIANGLE_BOUNDED_THEOREM_NOTE_2026-10-01.md](COMPOSITE_SITE_NETWORK_FLUX_FREE_LINE_NODES_OUTSIDE_THE_COUPLING_TRIANGLE_BOUNDED_THEOREM_NOTE_2026-10-01.md)

## Evidence limits and No-Go Discipline Gate

- **N1:** supplied comparator at ten rational couplings.
- **N2:** no phase or no-go wall is imported.
- **N3:** network, hopping signs and the `u = +1` sector remain supplied.
- **N4:** the landed comparator and charge convention are used as stated there.
- **N5:** exact algebra and outward-rounded interval certificates.
- **N6:** the items listed above remain open.
- **N7:** other couplings and sectors remain available.
- **N8:** no physical identification, new premise or audit verdict.

## Reproduction

```bash
python3 scripts/composite_site_network_flux_free_certified_touching_census_across_coupling_regimes_2026_10_01.py
```

Thirty-eight checks; prints `TOTAL: PASS=38 FAIL=0` in about 80 seconds.
