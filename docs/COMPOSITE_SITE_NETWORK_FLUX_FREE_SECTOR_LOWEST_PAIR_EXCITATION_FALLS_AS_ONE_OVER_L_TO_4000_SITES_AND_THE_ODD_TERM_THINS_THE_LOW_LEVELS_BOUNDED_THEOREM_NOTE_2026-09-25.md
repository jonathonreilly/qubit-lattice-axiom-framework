---
claim_id: composite_site_network_flux_free_sector_lowest_pair_excitation_falls_as_one_over_l_to_4000_sites_and_the_odd_term_thins_the_low_levels_bounded_theorem_note_2026-09-25
claim_type: bounded_theorem
claim_scope: Eight supplied cut-twisted comparator sectors on finite periodic clusters, without a completeness theorem
  for all locally flux-free classes. For a nonsingular sector whose free-ground total parity is positive, the lowest
  same-bond projected excitation costs twice its lowest positive matter energy. The matching singular-value bound
  holds for kappa=0 andJz=2.5. Finite spectra and pooled counts do not prove a1/L law, nodal dimension, ground-flux
  selection or physical spin excitation map.
upstream_dependencies:
- minimal_axioms
- the_hyperhoneycomb_embeds_in_the_doubled_cubic_lattice_a_three_dimensional_composite_site_network_with_an_exact_charge_bounded_theorem_note_2026-09-24
- composite_sites_give_the_carved_majoranas_an_exact_charge_one_qubit_per_site_cannot_two_can_bounded_theorem_note_2026-09-24
- composite_site_network_spin_model_ground_state_is_locally_flux_free_on_the_clusters_searched_with_the_projection_exact_bounded_theorem_note_2026-09-25
runner: scripts/composite_site_network_physical_excitations_in_the_flux_free_ground_sector_2026_09_25.py
---

# Finite projected-comparator excitations in eight cut-twisted sectors

**Type:** bounded_theorem
**Status:** conditional sector identities and finite numerical spectra; unaudited.

## Scope and representation

Use the current network and composite parents, and the explicitly supplied Majorana comparator and Clifford projection of the linked sector note. Its sign/mapping limitation applies: these are projected-comparator energies, not an established positive-J spin/odd-term operator correspondence. Choose the eight sectors made by reversing bonds wrapping each selected coordinate direction from u=+1. Contractible ten-loops keep their products. The runner compares these eight representatives; it does not establish that they exhaust every locally flux-free gauge class at each size. 'Ground class' below means the lowest projected energy among those eight candidates. It does not mean the unrestricted spin or flux ground state.

## Conditional excitation and matching identities

For a nonsingular selected sector with free-ground total parity +1, a single matter occupation changes that parity and is removed by local projection. Two occupations preserve it. Three identical flavours allow the lowest positive level epsilon1 to be occupied in two distinct copies, giving minimal positive same-bond excitation2epsilon1. Gauge projection is nonzero by the connected-graph stabilizer argument in the sector note. Degenerate zero-mode ground spaces need a separate excitation convention; the formula is asserted only for the nonsingular selected ground classes. Other bond sectors and winding changes are excluded.

At kappa=0, each color is a perfect matching. The z matching has all singular values2Jz=5, while each of x,y has norm2. For any bond signs, the reverse triangle bound gives ||Av||>=||Azv||-||(Ax+Ay)v||>=||v||. Thus every singular value, or absolute eigenvalue of iA, is at least1. Negative eigenvalues are not claimed to be positive. This is a finite all-signs bound for the specified matching graph.

The printed1/L trend uses only four sizes. Counts pool spectra of eight sectors, not a single physical density of states. E² and E³ are comparison powers under separately assumed regular linear nodal geometries; finite count slopes do not classify nodes, gaps or phases.

## Diagnostic 1 — the 32-site control

The eight winding classes of the locally flux-free sector on the 32-site
cluster reproduce the lowest comparator energies among the chosen flux-free representatives of open PR 9255's
enumeration of all 131072 sectors to all printed digits: `−77.66563` (isotropic,
`κ = 0`, class 7), `−130.62793` (`J_z = 2.5`, class 7) and `−84.81708`
(isotropic, `κ = 0.3`, class 3), each with constraint product `+1`.

## Diagnostic 2 — the levels against the cluster size

`e_1` is the lowest single-particle level of the physical ground class; the
last column is the lowest level of any of the eight classes. The ground class
is labelled by the directions whose wrapping bonds are flipped (bit `d` for
direction `d`).

| case | `L` (sites) | ground class (product) | `e_1` | `L e_1` | `2 e_1` | lowest level, any class |
|---|---|---|---|---|---|---|
| isotropic, `κ = 0` | 8 (256) | 7 (+1) | 0.8284 | 6.63 | 1.657 | 0.0770 |
| | 12 (864) | 4 (+1) | 0.5221 | 6.27 | 1.044 | 0.0000 |
| | 16 (2048) | 4 (+1) | 0.3885 | 6.22 | 0.777 | 0.0770 |
| | 20 (4000) | 7 (+1) | 0.3511 | 7.02 | 0.702 | 0.0000 |
| isotropic, `κ = 0.3` | 8 (256) | 4 (+1) | 1.0725 | 8.58 | 2.145 | 0.2498 |
| | 12 (864) | 5 (+1) | 0.4707 | 5.65 | 0.941 | 0.2539 |
| | 16 (2048) | 7 (+1) | 0.4862 | 7.78 | 0.972 | 0.1747 |
| | 20 (4000) | 5 (+1) | 0.3408 | 6.82 | 0.682 | 0.0592 |
| `J_z = 2.5`, `κ = 0` | 8 (256) | 7 (+1) | 2.1248 | 17.00 | 4.250 | 1.0000 |
| | 12 (864) | 7 (+1) | 1.6148 | 19.38 | 3.230 | 1.0000 |
| | 16 (2048) | 4 (+1) | 1.3299 | 21.28 | 2.660 | 1.0000 |
| | 20 (4000) | 4 (+1) | 1.2217 | 24.43 | 2.443 | 1.0000 |

The ground class changes with `L` in the two isotropic cases, as boundary
conditions do when levels come close to zero. In the control `L e_1` grows
and `e_1` approaches the bound `1` from above.

## Diagnostic 3 — the count of low levels on `L = 20`

| case | levels below 0.25 | below 0.5 | below 1.0 | exponent 0.25–0.5 | exponent 0.5–1.0 |
|---|---|---|---|---|---|
| isotropic, `κ = 0` | 56 | 336 | 1788 | 2.58 | 2.41 |
| isotropic, `κ = 0.3` | 14 | 110 | 960 | 2.97 | 3.13 |
| `J_z = 2.5`, `κ = 0` | 0 | 0 | 1 | — | — |

The counts pool the eight classes (16000 positive levels per case). The
exponent is `log(N(E_2)/N(E_1)) / log(E_2/E_1)`. With linear crossings it is
`2` for a line of nodes and `3` for isolated nodes; curvature above the
crossings and the discreteness of the cluster move it away from either, so
the value at `κ = 0` is not read as one or the other.


## Evidence limits and No-Go Discipline Gate

- **N1:** supplied finite graph, Clifford representation, comparator and named sectors.
- **N2:** no imported flux-selection or phase theorem.
- **N3:** source Hamiltonian, odd sign and representation are supplied.
- **N4:** current parent scope and spin-map sign limitation remain explicit.
- **N5:** numerical spectra and searches are not certified global enclosures.
- **N6:** operator mapping, exhaustive larger flux classes and limiting inference remain open.
- **N7:** unvisited sectors, zero modes and alternate sign conventions remain counterroutes.
- **N8:** no physical particle claim, new premise or audit verdict.

## Actual inputs

- [MINIMAL_AXIOMS_2026-06-29](MINIMAL_AXIOMS_2026-06-29.md)
- [THE_HYPERHONEYCOMB_EMBEDS_IN_THE_DOUBLED_CUBIC_LATTICE_A_THREE_DIMENSIONAL_COMPOSITE_SITE_NETWORK_WITH_AN_EXACT_CHARGE_BOUNDED_THEOREM_NOTE_2026-09-24](THE_HYPERHONEYCOMB_EMBEDS_IN_THE_DOUBLED_CUBIC_LATTICE_A_THREE_DIMENSIONAL_COMPOSITE_SITE_NETWORK_WITH_AN_EXACT_CHARGE_BOUNDED_THEOREM_NOTE_2026-09-24.md)
- [COMPOSITE_SITES_GIVE_THE_CARVED_MAJORANAS_AN_EXACT_CHARGE_ONE_QUBIT_PER_SITE_CANNOT_TWO_CAN_BOUNDED_THEOREM_NOTE_2026-09-24](COMPOSITE_SITES_GIVE_THE_CARVED_MAJORANAS_AN_EXACT_CHARGE_ONE_QUBIT_PER_SITE_CANNOT_TWO_CAN_BOUNDED_THEOREM_NOTE_2026-09-24.md)
- [COMPOSITE_SITE_NETWORK_SPIN_MODEL_GROUND_STATE_IS_LOCALLY_FLUX_FREE_ON_THE_CLUSTERS_SEARCHED_WITH_THE_PROJECTION_EXACT_BOUNDED_THEOREM_NOTE_2026-09-25](COMPOSITE_SITE_NETWORK_SPIN_MODEL_GROUND_STATE_IS_LOCALLY_FLUX_FREE_ON_THE_CLUSTERS_SEARCHED_WITH_THE_PROJECTION_EXACT_BOUNDED_THEOREM_NOTE_2026-09-25.md)
