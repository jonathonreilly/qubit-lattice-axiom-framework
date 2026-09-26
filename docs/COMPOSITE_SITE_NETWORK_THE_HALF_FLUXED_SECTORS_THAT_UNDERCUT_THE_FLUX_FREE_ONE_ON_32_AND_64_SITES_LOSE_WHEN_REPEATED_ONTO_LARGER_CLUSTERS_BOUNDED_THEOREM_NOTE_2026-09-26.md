---
claim_id: composite_site_network_the_half_fluxed_sectors_that_undercut_the_flux_free_one_on_32_and_64_sites_lose_when_repeated_onto_larger_clusters_bounded_theorem_note_2026-09-26
claim_type: bounded_theorem
claim_scope: "Supplied colored periodic network of composite sites of the landed network note, isotropic bonds and the three-site odd term kappa in the sign convention of open PR 9255, six-Majorana representation, with open PR 9255's exact projection onto physical states. Finite search results: on 32 sites at kappa = 0.3 the sweep over every sector reproduces open PR 9255's exception (a half-fluxed sector 0.824 below the flux-free one), and that bond pattern repeated periodically onto the 64-, 128- and 256-site clusters, in its best winding class, lies 0.587, 2.894 and 5.508 above the flux-free physical energy; on 64 sites annealing finds half-fluxed sectors 1.435 and 1.248 below the flux-free one at kappa = 0.45 and 0.6, and the same patterns repeated onto 128 and 256 sites lie 1.824 to 5.228 above it; on 128 and 256 sites annealing from the flux-free sector, random bonds and the repeated minima finds no sector whose physical energy lies below the flux-free one at kappa = 0.45 and 0.6. Annealing is a search, not a proof; finite clusters; no phase or physical identification."
upstream_dependencies:
  - minimal_axioms
  - the_hyperhoneycomb_embeds_in_the_doubled_cubic_lattice_a_three_dimensional_composite_site_network_with_an_exact_charge_bounded_theorem_note_2026-09-24
  - composite_sites_give_the_carved_majoranas_an_exact_charge_one_qubit_per_site_cannot_two_can_bounded_theorem_note_2026-09-24
runner: scripts/composite_site_network_small_cluster_flux_exceptions_repeated_onto_larger_clusters_2026_09_26.py
---

# The composite-site network: the half-fluxed sectors that undercut the flux-free one on 32 and 64 sites lose when repeated onto larger clusters

**Date:** 2026-09-26
**Type:** bounded_theorem
**Status:** exhaustive sweep on 32 sites and annealed searches on 64 to 256 sites, with the exact projection; unaudited.

## Result

Open PR 9255 found the flux-free sector lowest on every cluster it searched,
except one: on 32 sites at `κ = ±0.3` a half-fluxed sector lies `0.82` below
it. Open PR 9273 then certified the flux-free sector's band touchings: two
below `κ = √(3/20)` at isotropic couplings, six above. Whether the flux-free
sector is the lowest one at those couplings decides whether the six-touching
regime describes the ground sector. This block asks whether the small-cluster
exceptions persist as the cluster grows.

- **The 32-site exception does not repeat.** Sweeping all 131 072 sectors
  of the 32-site cluster at `κ = 0.3` reproduces the exception: a sector with
  16 of its 32 ten-loops at `−1` lies `0.824` below the flux-free physical
  energy (`−85.641` against `−84.817`). Carried periodically onto the 64-,
  128- and 256-site clusters, in its best winding class, the same bond pattern
  lies `0.587`, `2.894` and `5.508` above the flux-free physical energy there.
  The margin grows with the cluster, by about `0.02` per site at 256 sites.
- **Neither do the 64-site ones.** On 64 sites, annealing finds half-fluxed
  sectors (32 of 64 loops at `−1`) below the flux-free one: `1.435` below at
  `κ = 0.45` and `1.248` below at `κ = 0.6`, which is the six-touching regime
  of open PR 9273. Carried onto 128 and 256 sites, the same patterns lie
  `1.824` and `3.037` above the flux-free energy at `κ = 0.45`, and `3.216` and
  `5.228` above it at `κ = 0.6`.
- **Nothing lower on 128 and 256 sites.** Annealing started from the
  flux-free sector, from two random bond sets and from the carried 64-site
  minimum finds no sector with a physical energy below the flux-free one, at
  `κ = 0.45` and `0.6` on both clusters. The minima found are either
  flux-free or lie `0.08` to `6.3` above it.

So on these clusters the half-fluxed sectors undercut the flux-free one only on
the two smallest tori. On the larger clusters searched, the flux-free sector,
whose band touchings open PR 9273 certified, stays the lowest found at these
couplings. This is support from finite searches, not a proof.

## Setting and decision points

- **D-network, D-bonds, D-odd, D-majorana (supplied, landed).** The colored
  periodic network, bonds and odd term of the landed network note
  `THE_HYPERHONEYCOMB_EMBEDS_IN_THE_DOUBLED_CUBIC_LATTICE_A_THREE_DIMENSIONAL_COMPOSITE_SITE_NETWORK_WITH_AN_EXACT_CHARGE_BOUNDED_THEOREM_NOTE_2026-09-24.md`,
  in the six-Majorana representation of the landed composite-site note
  `COMPOSITE_SITES_GIVE_THE_CARVED_MAJORANAS_AN_EXACT_CHARGE_ONE_QUBIT_PER_SITE_CANNOT_TWO_CAN_BOUNDED_THEOREM_NOTE_2026-09-24.md`.
  The filenames are historical; the note bodies govern.
- **D-projection (open PR 9255).** A sector's lowest physical energy is its
  free ground energy, plus its lowest level when the product of the local
  constraints on the free ground state is `−1`.
- **D-repeat (method choice).** A bond pattern of a small torus is carried
  to a larger torus through the infinite network: each bond of the larger
  torus takes the value of the small-torus bond it maps to. Each repeated
  pattern is compared in all eight winding classes (sign flips across the
  three cuts), and the lowest is kept.

## Method

1. **32 sites.** All `2^17 = 131 072` gauge-inequivalent sectors (bond
   variables on a cotree), physical energies by the exact projection.
2. **64 sites.** Simulated annealing over all bond variables on the free
   energy (six random starts and the flux-free start, 4000 steps each),
   then the physical energy of the lowest configuration found.
3. **Repetition.** The lowest small-cluster patterns carried to the 64-,
   128- and 256-site clusters, best of eight winding classes.
4. **128 and 256 sites.** Annealing from the flux-free sector, two random
   starts and the repeated 64-site minimum (6000 and 4000 steps).

## Relation to other work

- Open PR 9255's annealing at `κ = 0` and `0.3` on 64 and 256 sites found no
  sector below the flux-free one; this block extends the search to
  `κ = 0.45` and `0.6`, where open PR 9273 certified six touchings, and adds
  the repetition test.
- Open PR 9264's finite-cluster level counts are counts in the flux-free
  sector; this block supports, without proving, that this sector stays
  lowest on the larger clusters at these couplings.

## Boundary

- Annealing is a search, not a proof: a lower sector on 128 or 256 sites
  that these searches did not reach is not excluded.
- Finite clusters of one supplied network; no thermodynamic-limit flux
  theorem, no phase and no physical identification.
- The small-cluster exceptions are recorded as found; which winding class
  or boundary effect produces them is not analysed here.

## Reproduction

```bash
python3 scripts/composite_site_network_small_cluster_flux_exceptions_repeated_onto_larger_clusters_2026_09_26.py
```

Three checks; prints `TOTAL: PASS=3 FAIL=0` in about 11 min.
