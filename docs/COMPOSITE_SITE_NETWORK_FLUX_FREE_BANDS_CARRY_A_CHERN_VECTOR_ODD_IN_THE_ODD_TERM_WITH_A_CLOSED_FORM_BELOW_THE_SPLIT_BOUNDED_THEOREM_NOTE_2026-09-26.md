---
claim_id: composite_site_network_flux_free_bands_carry_a_chern_vector_odd_in_the_odd_term_with_a_closed_form_below_the_split_bounded_theorem_note_2026-09-26
claim_type: bounded_theorem
claim_scope: "Supplied colored periodic network of composite sites of the landed network note, bonds J_x = J_y = 1, J_z = J and the three-site odd term kappa in the sign convention of open PR 9255, in the u = +1 sector (one free-Majorana copy), with open PR 9273's Bloch reduction. Exact on the line f = (x, 1 - x, 0): the touching lies on J^2 = 2 (1 + c)(1 + 2 kappa^2 (1 - c)), c = cos 2 pi x; at isotropic J, c = [1 - (1 + 4 kappa^2 + 16 kappa^4)^(1/2)] / (4 kappa^2); the curve reaches c = 1 (the zone centre) exactly at J = 2 for every kappa. Finite computations: the numerical touching on the line matches the closed form to 3e-9; the slice-averaged Chern numbers of the lowest two bands on 96 slices per axis are (arccos(c)/pi, -arccos(c)/pi, 0) up to the slice spacing below the split, change sign with kappa, and at kappa = 0.6 (six touchings) equal minus the charge-weighted sum of the certified touching positions modulo one, (0.093, -0.093, 0), within the slice spacing (0.104 measured). No transport coefficient of a physical system, phase or physical identification is claimed."
upstream_dependencies:
  - minimal_axioms
  - the_hyperhoneycomb_embeds_in_the_doubled_cubic_lattice_a_three_dimensional_composite_site_network_with_an_exact_charge_bounded_theorem_note_2026-09-24
runner: scripts/composite_site_network_flux_free_bands_chern_vector_with_the_odd_term_2026_09_26.py
---

# The composite-site network's flux-free bands carry a Chern vector that is odd in the odd term, with a closed form below the split

**Date:** 2026-09-26
**Type:** bounded_theorem
**Status:** exact statements on the touching line and finite slice computations for one sector of the supplied model; unaudited.

## Result

Open PR 9273 certified the band touchings of the composite-site network's
flux-free sector with the odd term: two, of charge `−1` and `+1`, below
`κ_c² = J(J + 2)/[4(4 + 2J − J²)]`, and six above. Touchings of opposite
charge at different momenta leave two-dimensional slices of the zone with
nonzero Chern numbers. Averaged over the slices along each fractional axis,
these give a Chern vector of the lowest two bands. This block gives it in
closed form below the split.

- **Exact on the touching line.** The touching lies on
  `J² = 2(1 + c)(1 + 2κ²(1 − c))` with `c = cos 2πx`. At isotropic `J`
  this is a quadratic in `c` whose root in `[−1, 1]` is
  `c = [1 − √(1 + 4κ² + 16κ⁴)]/(4κ²)`, tending to `−1/2` as `κ → 0` (the
  touching approaches `x = 1/3`). For every `κ` the curve reaches `c = 1`,
  the zone centre, exactly at `J = 2`: there the touchings meet at the zone
  centre, the change to the gapped side that the landed note's matching
  bound shows at `J = 2.5`, `κ = 0`. The numerical touching on the line
  matches the root to `3 × 10⁻⁹` at `J = 1` (`κ = 0.05`–`0.35`) and
  `J = 1.5` (`κ = 0.3`, `0.5`).
- **The Chern vector in closed form.** Below the split, the Chern number of
  the lowest two bands is `+1` on the slices `f₁ = const` outside the
  interval between the two touchings and `0` inside, and the mirror of that
  along `f₂`. So the slice-averaged Chern vector is
  `(arccos c / π, −arccos c / π, 0)`. On 96 slices per axis the averages
  are `(0.667, −0.667, 0)` at `κ = 0.1` and `(0.708, −0.708, 0)` at
  `κ = 0.3`, against `0.672` and `0.710`, within the slice spacing. As `κ`
  leaves zero the vector jumps from nothing to `(2/3, −2/3, 0)`. At `κ = 0`
  the touchings form a line and slices through it are gapless.
- **Odd in the odd term.** At `κ = −0.3` every slice Chern number changes
  sign: the vector is `(−0.708, +0.708, 0)`.
- **Six touchings: a small vector, and one rule for both regimes.** At
  `κ = 0.6` the averages are `(0.104, −0.104, 0)`. That matches minus the
  charge-weighted sum of the six certified touching positions modulo one,
  `(0.093, −0.093, 0)`, within the slice spacing. The same rule gives the
  closed form below the split. After the split the on-plane touchings have
  reversed their charges and the off-plane ones sit far apart, so their
  dipole, and with it the Chern vector, nearly cancels.

## Setting and decision points

- **D-network, D-bonds, D-odd, D-majorana (supplied, landed).** As in open
  PR 9273: the colored periodic network, bonds and odd term of the landed
  network note
  `THE_HYPERHONEYCOMB_EMBEDS_IN_THE_DOUBLED_CUBIC_LATTICE_A_THREE_DIMENSIONAL_COMPOSITE_SITE_NETWORK_WITH_AN_EXACT_CHARGE_BOUNDED_THEOREM_NOTE_2026-09-24.md`,
  one of the three identical free-Majorana copies. The filenames are
  historical; the note bodies govern.
- **D-sector (open PR 9255).** The sector with every bond variable `u = +1`.
  Open PR 9277 supports, without proving, that it is the lowest sector on
  the larger clusters searched at `κ = 0.45` and `0.6`.

## Method

1. **The touching line.** From open PR 9273, the determinant of `H` on
   `f = (x, 1 − x, 0)` is `16 (J² + 4c²κ² − 2c − 4κ² − 2)²`, so the touching
   sits where `J² = 2(1 + c)(1 + 2κ²(1 − c))`. At `J = 1` this is a quadratic
   in `c` with the root `c = [1 − √(1 + 4κ² + 16κ⁴)]/(4κ²)` in `[−1, 1]`.
2. **Slices.** The Chern number of the lowest two bands on each of 96
   slices per fractional axis, by the lattice link method with periodic
   seams. Their average is the component of the Chern vector along that
   axis, up to the slice spacing `1/96`.

## Relation to other work

- A Chern vector from separated touchings of opposite charge is the band
  structure's way of carrying a Hall-type response. Here it is a number of
  one free-Majorana copy in one sector; no transport coefficient of a
  physical system is computed.
- **Prior art (not premises).** Hall responses from separated band
  touchings (for example A. A. Burkov and L. Balents, Phys. Rev. Lett. 107,
  127205 (2011)); Weyl-type touchings in three-dimensional Kitaev-type
  Majorana models (M. Hermanns, K. O'Brien, S. Trebst, Phys. Rev. Lett. 114,
  157202 (2015)).

## Boundary

- One sector, one copy, and slices at spacing `1/96`: the averages carry
  that resolution.
- The closed form holds below the split, where the two touchings lie on the
  line. Above it the six-touching values are finite computations.
- No transport coefficient of a physical system, no phase and no physical
  identification.

## Reproduction

```bash
python3 scripts/composite_site_network_flux_free_bands_chern_vector_with_the_odd_term_2026_09_26.py
```

Five checks; prints `TOTAL: PASS=5 FAIL=0` in about 15 s.
