---
claim_id: composite_site_network_flux_free_sector_lowest_pair_excitation_falls_as_one_over_l_to_4000_sites_and_the_odd_term_thins_the_low_levels_bounded_theorem_note_2026-09-25
claim_type: bounded_theorem
claim_scope: "Supplied colored periodic network of composite sites of the landed network note, bonds J_lam (tau^lam tau^lam)(sigma.sigma) and the three-site odd term kappa in the runner's sign convention, in the six-Majorana representation, inside the locally flux-free sector (open PR 9255) on periodic clusters of 256, 864, 2048 and 4000 sites. Exact: the eight winding classes of the sector; in a class with constraint product +1 the lowest physical excitation with the same bond variables is a fermion pair costing 2 e1; at J_z = 2.5, kappa = 0 every level of every sector is at least 1 (Weyl's inequality). Finite spectra: the 32-site control reproduces open PR 9255's flux-free energies; the physical ground class has product +1 in every case; isotropic, kappa = 0: e1 = 0.828, 0.522, 0.389, 0.351 at L = 8, 12, 16, 20 (L e1 6.6, 6.3, 6.2, 7.0), pooled level counts on L = 20 grow with exponents 2.58 and 2.41 between the values 2 (line of nodes) and 3 (isolated nodes); kappa = 0.3: e1 = 1.07, 0.47, 0.49, 0.34, lowest level of any class 0.250 to 0.059, count exponents 2.97 and 3.13, and a quarter to a third as many levels below 0.25 and 0.5 as at kappa = 0 (at kappa = 0.3 open PR 9255 found a lower half-fluxed sector on 32 sites); J_z = 2.5: every level at least 1 with equality attained, e1 2.12 to 1.22. No thermodynamic-limit, node, phase or physical-field claim."
upstream_dependencies:
  - minimal_axioms
  - the_hyperhoneycomb_embeds_in_the_doubled_cubic_lattice_a_three_dimensional_composite_site_network_with_an_exact_charge_bounded_theorem_note_2026-09-24
  - composite_sites_give_the_carved_majoranas_an_exact_charge_one_qubit_per_site_cannot_two_can_bounded_theorem_note_2026-09-24
runner: scripts/composite_site_network_physical_excitations_in_the_flux_free_ground_sector_2026_09_25.py
---

# The composite-site network's flux-free sector: the lowest pair excitation falls as 1/L to 4000 sites, and the odd term thins the low levels

**Date:** 2026-09-25
**Type:** bounded_theorem
**Status:** exact statements about the supplied model's flux-free sector, with finite-cluster spectra; unaudited.

## Result

Open PR 9255 placed the ground state of the supplied composite-site network
in its locally flux-free sector on the clusters it searched, with an exact
projection onto physical states. This block asks what the physical
excitations of that sector look like as the cluster grows, from 256 to 4000
sites, in the three coupling cases of that PR.

- **Isotropic couplings, no odd term: a pair excitation that falls roughly
  as `1/L`.** The lowest single-particle level of the physical ground class is
  `e_1 = 0.828`, `0.522`, `0.389`, `0.351` at `L = 8, 12, 16, 20`, so
  `L e_1 = 6.6, 6.3, 6.2, 7.0`, and the lowest physical excitation with the
  same bonds, `2 e_1`, falls from `1.66` to `0.70`. On `L = 12` and `20` some
  winding class has a level below `5 × 10⁻⁵`.
- **The count of low levels.** Pooled over the eight classes on `L = 20`,
  56 levels lie below `0.25`, 336 below `0.5` and 1788 below `1.0`: count
  exponents `2.58` and `2.41`, between the value `2` of a line of nodes and
  the value `3` of isolated nodes. These clusters do not separate the two.
- **The odd term thins the low levels.** At `κ = 0.3` the counts are 14, 110
  and 960, a quarter and a third of the `κ = 0` counts below `0.25` and `0.5`,
  with exponents `2.97` and `3.13`, near the isolated-node value; the lowest
  level of any class is `0.250`, `0.254`, `0.175` and `0.059` at `L = 8` to `20`.
  Open PR 9255 found a half-fluxed sector below the flux-free one at
  `κ = ±0.3` on 32 sites, so this case describes the flux-free sector, not
  necessarily the ground sector.
- **The anisotropic control.** At `J_z = 2.5`, `κ = 0` every level of every
  class is at least `1` on every cluster, with equality attained, as the
  matching bound requires; the pair excitation costs at least `2`.

Finite clusters of one supplied network: the `1/L` trend and the count
exponents are finite-size diagnostics, not a limit, a node theorem or a
phase.

## Setting and decision points

- **D-network, D-bonds, D-odd, D-majorana (supplied, landed).** The colored
  periodic network, bonds and odd term of the landed network note
  `THE_HYPERHONEYCOMB_EMBEDS_IN_THE_DOUBLED_CUBIC_LATTICE_A_THREE_DIMENSIONAL_COMPOSITE_SITE_NETWORK_WITH_AN_EXACT_CHARGE_BOUNDED_THEOREM_NOTE_2026-09-24.md`,
  in the six-Majorana representation of the landed composite-site note
  `COMPOSITE_SITES_GIVE_THE_CARVED_MAJORANAS_AN_EXACT_CHARGE_ONE_QUBIT_PER_SITE_CANNOT_TWO_CAN_BOUNDED_THEOREM_NOTE_2026-09-24.md`.
  The filenames are historical; the note bodies govern.
- **The projection rule and the flux sector (open PR 9255).** The product
  of all local constraints on a sector's free ground state, and the finding
  that the ground state lies in the locally flux-free sector on the clusters
  searched there. This note works inside that sector and does not search
  the flux sectors again on the larger clusters.
- **The clusters (method).** Periodic `L × L × L` boxes of the network with
  `L = 8, 12, 16, 20` (256, 864, 2048 and 4000 sites); levels from the
  singular values of the real antisymmetric hopping matrix, the constraint
  product from its real Schur form.

None is adopted.

## Theorem 1 — winding classes, physical excitations and the matching bound

1. **Winding classes.** Inside the locally flux-free sector, flipping every
   bond that wraps the torus in one direction changes no ten-site loop and
   changes the fermions' boundary condition in that direction. The eight
   combinations are the sector's winding classes. The physical ground state
   of the sector is the class with the lowest physical energy.
2. **Physical excitations with the same bonds.** In a class whose constraint
   product is `+1`, adding one fermion to one copy flips the product and
   leaves the physical space. Adding one fermion to each of two copies keeps
   it. The lowest physical excitation with the same bond variables therefore
   costs `2 e_1`, with `e_1` the lowest single-particle level, since the three
   copies share their levels.
3. **The matching bound at `J_z = 2.5`, `κ = 0`.** The hopping matrix is the
   z-bond matching, whose levels are all `2 J_z = 5`, plus the x- and y-bond
   matchings, each of norm `2`. Weyl's inequality puts every level of every
   sector at `5 − 4 = 1` or above, on every cluster.
4. **Level counts.** For linear crossings, the number of levels below `E`
   grows as `E²` for a line of nodes and as `E³` for isolated nodes, so the
   exponent of the pooled count distinguishes the two when the clusters are
   large enough.

Statements 1–3 are exact; statement 4 is the standard counting that the
diagnostics compare against. ∎

## Diagnostic 1 — the 32-site control

The eight winding classes of the locally flux-free sector on the 32-site
cluster reproduce the lowest flux-free physical energies of open PR 9255's
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

## What this does not do

- It claims no thermodynamic limit, gap, node set or phase: the `1/L` trend
  holds over four cluster sizes, and the count exponents are finite-cluster
  numbers.
- It does not search the flux sectors on these clusters; at `κ = 0.3` the
  flux-free sector need not hold the ground state (open PR 9255).
- It treats excitations with the same bond variables only. Changing winding
  class or bond sector is a different excitation and is not bounded here.
- It gives no physical-field identification for the fermions and names no
  graph.
- It adopts no network, bond, odd term, sign convention or representation.

## Prior art (not premises)

Kitaev 2006 (the honeycomb model's exact solution and its projection); Yao
and Lee 2011 (the six-Majorana composite construction); Mandal and
Surendran 2009, Hermanns, O'Brien and Trebst 2015, and O'Brien, Hermanns
and Trebst 2016 (three-dimensional tricoordinated Kitaev models: lines of
nodes, and isolated nodes once time reversal is broken). All cited as prior
art, not as premises.

## Checks

The runner has four checks: the 32-site control against open PR 9255's
enumeration; isotropic couplings at `κ = 0` and at `κ = 0.3` (reported, each
passing when the physical ground class has product `+1` on every cluster);
the `J_z = 2.5` control, where every level must be at least `1`. The fresh
run takes about five minutes.

## Independent check

None yet.

## Evidence limits and No-Go Discipline Gate

- **N1 — Domain:** the explicit supplied network, Hamiltonian, flux-free sector and clusters above.
- **N2 — Independence:** self-checked; the 32-site control is internal to this runner.
- **N3 — Imports:** the network, the Hamiltonian and the representation are supplied, not framework admissions.
- **N4 — Dependencies:** the landed parents' scopes govern; open PRs are cited, not relied on.
- **N5 — Resolution:** floating-point spectra and determinants; the count exponents are finite-cluster numbers.
- **N6 — Residuals:** larger clusters, the flux sectors at these sizes, other excitations and the thermodynamic limit remain open.
- **N7 — Counterroutes:** other sign conventions, representations, sectors and cluster shapes remain available.
- **N8 — Boundary:** source note, not an audit verdict.

## Premise authority

The framework boundary is [the current axiom memo](MINIMAL_AXIOMS_2026-06-29.md).
