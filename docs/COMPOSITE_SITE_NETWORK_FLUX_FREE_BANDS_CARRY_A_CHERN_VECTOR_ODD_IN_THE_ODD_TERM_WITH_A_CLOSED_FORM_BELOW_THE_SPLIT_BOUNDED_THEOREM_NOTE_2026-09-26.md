---
claim_id: composite_site_network_flux_free_bands_carry_a_chern_vector_odd_in_the_odd_term_with_a_closed_form_below_the_split_bounded_theorem_note_2026-09-26
claim_type: bounded_theorem
claim_scope: "Supplied u = +1 quadratic Majorana comparator of the landed composite-site network notes (one of three identical copies, the fixed hopping-sign convention), with bonds J_x = J_y = 1, J_z = J and odd term kappa. Exact: on the line f = (x, 1 - x, 0), from the landed determinant identity, the middle levels vanish on the curve J^2 = 2 (1 + c)(1 + 2 kappa^2 (1 - c)), c = cos 2 pi x; at J = 1 its root in (-1, 1) is c = -(1 + 4 kappa^2) / (1 + (1 + 4 kappa^2 + 16 kappa^4)^(1/2)); the curve passes through c = 1 at J = 2 for every kappa. Finite diagnostics: the numerical zero on the line matches that root to 3e-9; discrete overlap fluxes of the lowest two bands on 96 slices per fractional axis average to (0.667, -0.667, 0) at kappa = 0.1 and (0.708, -0.708, 0) at kappa = 0.3, near (arccos c / pi, -arccos c / pi, 0) = (0.672, -0.672, 0) and (0.710, -0.710, 0); they reverse at kappa = -0.3; at kappa = 0.6 they average (0.104, -0.104, 0), near minus the flux-weighted sum of the six numerical group positions modulo one, (0.093, -0.093, 0). No certified continuum Chern number, node count, transport coefficient, spin-Hamiltonian equivalence, ground-sector selection, phase or physical identification."
upstream_dependencies:
  - minimal_axioms
  - the_hyperhoneycomb_embeds_in_the_doubled_cubic_lattice_a_three_dimensional_composite_site_network_with_an_exact_charge_bounded_theorem_note_2026-09-24
  - composite_site_network_flux_free_bands_with_the_odd_term_two_certified_touchings_of_opposite_charge_become_six_at_kappa_root_3_over_20_bounded_theorem_note_2026-09-26
runner: scripts/composite_site_network_flux_free_bands_chern_vector_with_the_odd_term_2026_09_26.py
---

# The composite-site comparator's flux-free bands: slice fluxes averaged along each axis, odd in the odd term, near a closed form below the split

**Date:** 2026-09-26
**Type:** bounded_theorem
**Status:** exact algebra on one momentum line and finite discrete-flux diagnostics for a supplied comparator; unaudited.

## Supplied setting

Use the supplied `u = +1` quadratic Majorana comparator of the landed
composite-site network notes, one of three identical copies, in the fixed
hopping-sign convention and the four-site Bloch reduction of the landed note
`COMPOSITE_SITE_NETWORK_FLUX_FREE_BANDS_WITH_THE_ODD_TERM_TWO_CERTIFIED_TOUCHINGS_OF_OPPOSITE_CHARGE_BECOME_SIX_AT_KAPPA_ROOT_3_OVER_20_BOUNDED_THEOREM_NOTE_2026-09-26.md`.
As that note records, equality to the named spin Hamiltonian is not
established in this sign convention, and `u = +1` is not proved to be the
lowest sector. Filenames are historical; note bodies govern.

## Exact on the line f = (x, 1 − x, 0)

That landed note gives, with `J_x = J_y = 1`, `J_z = J` and `c = cos 2πx`,
`det H = 16 [J² + 4c²κ² − 2c − 4κ² − 2]²` on this line. So, for
`−1 < c < 1`, the middle levels vanish exactly on the curve

`J² = 2(1 + c)[1 + 2κ²(1 − c)]`.

- **At isotropic J.** At `J = 1` this is `4κ²c² − 2c − (1 + 4κ²) = 0`,
  whose root in `(−1, 1)` is
  `c = −(1 + 4κ²) / (1 + √(1 + 4κ² + 16κ⁴))`, tending to `−1/2` as `κ → 0`.
- **At J = 2.** The curve passes through `c = 1`, the zone centre, for
  every `κ`. The finite scan of the landed note found a cleared zone at
  `J_z = 2.5`, `κ = 0.3`; the exact statement here is only that the
  zero-determinant curve reaches the zone centre at `J = 2`.

## Finite diagnostics reproduced by the runner

- **The numerical zero on the line.** Minimising the middle gap along the
  line finds its zero within `3 × 10⁻⁹` of the root above, at `J = 1`
  (`κ = 0.05` to `0.35`) and at `J = 1.5` (`κ = 0.3`, `0.5`).
- **Slice fluxes and their averages.** The runner computes discrete
  determinant-overlap fluxes of the lowest two bands on 96 slices per
  fractional axis (mesh 48, periodic seams), all integer-valued. Averaged
  over the slices of each axis they give `(0.667, −0.667, 0)` at `κ = 0.1`
  and `(0.708, −0.708, 0)` at `κ = 0.3`. The zero-determinant root gives
  `(arccos c / π, −arccos c / π, 0) = (0.672, −0.672, 0)` and
  `(0.710, −0.710, 0)`, which is what these averages would be if the
  continuum slice Chern numbers were `+1` outside the interval between the
  two zeros on the line and `0` inside, mirrored along `f₂`. The agreement is
  within two slice spacings.
- **Odd in the odd term.** At `κ = −0.3` every slice flux changes sign.
- **Six numerical groups.** At `κ = 0.6` the adaptive search of the landed
  note leaves six numerical groups, and the slice fluxes average to
  `(0.104, −0.104, 0)`. Minus the sum of the six group positions weighted by
  their rounded sphere fluxes, modulo one, is `(0.093, −0.093, 0)`, within
  two slice spacings. The same weighting gives the closed-form value below
  the split.

## What this does not establish

- No certified continuum Chern number: discrete overlap fluxes need
  nonsingular overlaps and a gap across each continuous slice, which the
  sampled gaps do not certify.
- No node count, no transport coefficient of a physical system, no
  spin-Hamiltonian equivalence, no ground-sector selection, no phase and no
  physical identification.
- The averages carry the slice resolution `1/96`.

## Prior art (not premises)

Hall-type responses from separated band touchings (for example A. A.
Burkov and L. Balents, Phys. Rev. Lett. 107, 127205 (2011)); Weyl-type
touchings in three-dimensional Kitaev-type Majorana models (M. Hermanns,
K. O'Brien, S. Trebst, Phys. Rev. Lett. 114, 157202 (2015)).

## Reproduction

```bash
python3 scripts/composite_site_network_flux_free_bands_chern_vector_with_the_odd_term_2026_09_26.py
```

Five checks; prints `TOTAL: PASS=5 FAIL=0` in about 15 s.
