---
claim_id: block_coin_links_carry_only_gauge_and_axis_anisotropy_and_connection_sits_on_sites_bounded_theorem_note_2026-10-21
claim_type: bounded_theorem
claim_scope: "For the supplied spin-3/2 block coin with all edges open: unitary edge-only coins are exactly those with flux pi on every face and per-axis moduli on the unit sphere, so links carry pure gauge and a two-parameter axis anisotropy; any field strength inside a block breaks unitarity; the moduli carry only the E part of a spatial metric; the coin's hop is the incidence operator d + d^T of the coarse cell complex up to site phases; every unitarity-preserving U(1) dressing is one phase chi per site between half-ticks, covariant under block phases; a supplied quadratic chi law has one isotropic massless pair; and a positive site-and-edge law on the block graph is nearest-neighbour Markov. Speed and metric-trace comparisons with measurement are estimates. No carrier for chi, photon, photon speed, Coulomb phase or physical identification is established."
upstream_dependencies:
  - minimal_axioms
  - candidate_laws
runner: scripts/block_coin_links_carry_only_gauge_and_axis_anisotropy_and_connection_sits_on_sites_2026_10_21.py
---

# Block-coin links carry only gauge and axis anisotropy, and the connection sits on sites

Claim type: bounded_theorem.
Primary runner: `scripts/block_coin_links_carry_only_gauge_and_axis_anisotropy_and_connection_sits_on_sites_2026_10_21.py`.

The [candidate-law register](CANDIDATE_LAWS.md) has zero premise weight. Its block coin uses spin-3/2 overlap phases on the 12 edges of each block. This note asks what a link inside that coin can carry, and where a U(1) connection must sit. The [minimal axioms](MINIMAL_AXIOMS_2026-06-29.md) put possibilities, conditions and records on sites. They choose none of the models used.

## What a link inside the coin can carry

- The coin is a Hermitian involution with flux pi on all six faces.
- At the coin the unitary edge-coin family has tangent dimension 9 (Jacobian rank 15 of 24): 7 site rephasings and 2 axis anisotropies.
- Only if: all 38 solutions of W^2 = 1 found from random starts with every edge open have per-axis moduli with sum m_a^2 = 1 and flux pi on every face (spread 3e-16, |sum - 1| 2e-16, |flux - pi| 9e-15). Two more solutions have a closed edge.
- If: 20 of 20 random per-axis moduli on the unit sphere, with any site rephasing, give W^2 = 1.
- One link phase d inside a block gives ||W^2 - 1|| = d/3. For all 19 non-Hermitian unitary edge coins found, a random U(1) dressing breaks unitarity (minimum 0.056) while pure gauge keeps it.
- The polar part of a dressed edge hop is a gauge-covariant Hermitian involution, but its extra weight lies on body diagonals (0.0896 and 0.2452 at dressings 0.2 and 0.6), which reach beyond the six neighbours.

## Metric content of the moduli

With per-axis moduli c on even blocks and c' on odd blocks the band is exactly cos w = sum_a c_a c'_a cos K_a (error 3e-15), and W(c)^2 = 1 if and only if |c| = 1. The massless quadratic form is diag(c_a c'_a): it has no shear terms, unitarity fixes its trace, and c different from c' opens a gap. Under the 24 rotations the three moduli span A1 + E and the six metric components span A1 + E + T2. Unitarity removes A1, so the moduli carry E only, 2 of 6 components. They carry neither the trace (the light-bending part) nor the T2 shear.

## The connection sits on sites

- The tick is a product of two reflections: U + U^dag = H^2 - 2 with H = W_even + W_odd.
- Every plaquette of Z^3 carries flux pi: 96 block faces and 96 mixed plaquettes on the torus used.
- The hop is the incidence operator d + d^T of the coarse cell complex (sites with 0, 1, 2, 3 odd coordinates as vertices, edges, faces and cubes) up to site phases, to 7e-15 over 3072 entries on the 8^3 torus. d^2 = 0 is what puts pi through every plaquette.
- Link phases that keep every block coin unitary are pure gauge inside each block. They equal one site phase chi = phi_e - phi_o applied between half-ticks, leave block faces at pi, and change mixed fluxes by the alternating sum of chi.
- U(chi) = Theta^dag W_odd Theta W_even is unitary and covariant under independent phases on every block. Without chi, block phases change the bare tick by 0.66.
- Each half-tick keeps every block's odds inside the block, so all transport between blocks passes through sites. A site is the link of the block lattice joining its even and odd block.

## A supplied quadratic law for chi

With electric energy E^2/2 and a magnetic sum over the 12 mixed plaquettes per cell, block phases are the only zero modes away from k = 0. At k = 0 there are four zeros (gauge and uniform connection) and gapped modes 8, 8, 8, 24. There is one isotropic massless pair with omega^2/k^2 in [0.49995, 0.50000] in four directions and no second massless point; the zone corners are gapped at 4, 4 and 8. The coin speed is 1/sqrt(3) cell per tick and the chi speed is tau sqrt(g_E g_B / 2), so they agree only if tau^2 g_E g_B = 2/3, a supplied tuning.

## The admissibility form

On the triangle-free block graph with 8 binary sites, a positive law built from site and edge factors is nearest-neighbour Markov: dependence on non-neighbours is 1e-15. Adding one four-site face ring makes a corner's conditional depend on its face-diagonal partner (0.604).

## Estimates against measurement

The lattice energy hbar c/a is 2.44e27 eV for a = sqrt(8 pi) l_P, so the photon-mass bound of 1e-18 eV is 4e-46 of it, a tuning an unprotected composite would need. Speed ties (|c_e - c_gamma| below about 1e-11 in the laboratory, 1e-16 to 1e-21 from the Crab, model dependent; GW170817 within [-3e-15, +7e-16]) need tau^2 g_E g_B = 2/3 to about 2e-11 or better. The Cassini bound gamma - 1 = (2.1 +- 2.3)e-5 concerns the metric trace, which the moduli cannot carry.

## Checks

The runner prints `TOTAL: PASS=17 FAIL=0`. Its PASS lines cover the coin's involution and face flux, the tangent dimension, the only-if and if directions, unitarity breaking by field strength, the polar part, the band and gap of the moduli, the representation count, the two-reflection form, the plaquette fluxes, the incidence operator, the site-phase dressing, block-phase covariance, site-mediated transport, the zero modes and massless pair of the chi law, and the Markov property.

## Supplied and boundary

Supplied: the block coin and partitions, all edges open, minimal coupling as hop or site phases, the quadratic chi law and its couplings, and positivity with a joint law for the Markov check. The coin uses every qubit, so a carrier for chi lies outside the current axioms. Measured comparisons are estimates. No carrier for chi, photon, photon speed, Coulomb phase or physical identification is established.
