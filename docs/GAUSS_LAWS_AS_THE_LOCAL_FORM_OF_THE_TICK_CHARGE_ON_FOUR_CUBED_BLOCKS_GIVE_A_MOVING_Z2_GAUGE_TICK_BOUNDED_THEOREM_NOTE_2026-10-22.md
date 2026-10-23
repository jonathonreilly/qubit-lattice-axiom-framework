---
claim_id: gauss_laws_as_the_local_form_of_the_tick_charge_on_four_cubed_blocks_give_a_moving_z2_gauge_tick_bounded_theorem_note_2026-10-22
claim_type: bounded_theorem
claim_scope: "One qubit per site of Z^3, read at rung 2. Gauss stars G_v = X_v prod X(edge nbrs) on vertex sites and G_c = X_c prod X(face nbrs) on cube sites. Block gates exp(-i pi/4 P) on two tilings of 4^3 blocks (offsets 0 and (2,2,2)), with P the hops Z_e Z_v Z_v', the plaquettes Z^4 on the edge nbrs of a face site, and their duals; tick = on-site exp(-i pi/4 X) on every site, then the tiling-A gates, then the tiling-B gates. Exact: every P commutes with every G (any angle); on 2^3 cubes the Gauss restrictions force every site's X constant up to sign (frozen), and no hop or plaquette fits; on 4^3 blocks no edge or face site is forced in both tilings. On the 8^3 torus (512 qubits, GF(2) tableau with phases) all 128 stars are conserved with sign, the conserved Pauli group is exactly the Gauss group (dim 128), every site's X and Z move, and gauge and matter sites mix in one tick. The rule is invariant under the 24 maps that keep both tilings and the roles up to vertex-cube / edge-face duality; primal and dual sectors never mix. Finite diagnostic: the Heisenberg front of X_e has radius 2t-1 for 2<=t<=9 on 40^3 with no recurrence in 24 ticks (period 12 on 8^3 and 24 on 12^3). The spin-1/2 U(1) ring exchange and hop commute exactly with the U(1) divergence. Not shown: a photon, deconfinement, a U(1) dynamics, or any measured number."
upstream_dependencies:
  - minimal_axioms
  - candidate_laws
runner: scripts/gauss_laws_as_the_local_form_of_the_tick_charge_on_four_cubed_blocks_give_a_moving_z2_gauge_tick_2026_10_22.py
---

# Gauss laws as the local form of the tick's charge, on 4^3 blocks, give a moving Z2 gauge tick

Claim type: bounded_theorem.
Primary runner: `scripts/gauss_laws_as_the_local_form_of_the_tick_charge_on_four_cubed_blocks_give_a_moving_z2_gauge_tick_2026_10_22.py`.

The [candidate-law register](CANDIDATE_LAWS.md) has zero premise weight. The cell-complex draft found that the free tick has no local constants of motion, only a global U(1). It also found that Margolus rules keeping the stars and plaquettes freeze the gauge sites on 2^3 cubes, and that 4^3 blocks on two tilings leave every edge site free in at least one tiling. It proposed Rule G (UNTESTED): Gauss laws are the local form of the tick's own U(1), carried on blocks of side >= 4. This note builds such a rule and tests it.

## Rule G-blocks (explicit)

- Roles (rung 2): a site's number of odd coordinates is 0, 1, 2 or 3, giving vertex, edge, face or cube of 2Z^3.
- Local charges, the local form of the tick's charge: G_v = X_v prod_{edge nbrs} X on each vertex site, and the dual G_c = X_c prod_{face nbrs} X on each cube site. Matter sits on the vertex (dual: cube) sites, and the flux on the edge (dual: face) sites.
- Block gates: two tilings of 4^3 blocks, at offsets 0 and (2,2,2). Each gate is exp(-i pi/4 P), for every P of the following list that lies inside one block:
  - the hop Z_e Z_v Z_v' at each edge site;
  - the plaquette, Z on the 4 edge neighbours of a face site;
  - the dual hop Z_f Z_c Z_c' at each face site;
  - the dual plaquette, Z on the 4 face neighbours of an edge site.
  Every P is a site together with some of its nearest neighbours.
- Tick: the on-site layer exp(-i pi/4 X) on every site, then the tiling-A gates, then the tiling-B gates. The A and B gates commute.

## Statement

1. Exact conservation for any angle. Every generator commutes with every G_v and G_c (128 x 576 symplectic products, all zero), and X-type terms commute with X-type stars. So exp(-i theta P) keeps every Gauss law at every gate, for every theta. The Clifford point theta = pi/4 is used only so that 512 qubits can be checked exactly.
2. Freezing at 2^3, freedom at 4^3 (exact, GF(2)). Within a block, a gate that keeps every G must map each Gauss restriction to plus or minus itself.
   - On 2^3 cubes, in both tilings, the span of the restrictions contains X_j for all 512 sites. Every gate is then a Pauli times something diagonal in X, so the electric and matter configuration is frozen. In addition, no hop or plaquette fits in a 2^3 cube (span 3 > 2).
   - On 4^3 blocks, 96 edge and 96 face sites are forced in each tiling, and none is forced in both.
   This strengthens the cell-complex draft's freezing theorem, which used stars plus plaquettes, to stars alone.
3. The tick on the 8^3 torus (exact Clifford tableau with phases, 512 qubits).
   - (a) All 128 stars are conserved with sign.
   - (b) The group of Paulis conserved up to sign has dimension exactly 128, equal to the rank of the Gauss group. There is no frozen field and no extra local or global Pauli constant, not even a topological loop. Inside a 4^3 box the only conserved Paulis are the 2 Gauss stars that fit.
   - (c) X and Z move on every vertex, edge, face and cube site.
   - (d) One tick maps X_e onto matter sites and X_v onto edge sites, so gauge and matter are coupled.
   - (e) Control: with two on-site layers per tick, exp(-i pi/2 X) is a Pauli and the conserved dimension jumps to 640. The choice of one on-site layer is load-bearing.
4. Symmetry (exact). Of the 96 maps (48 point maps about a block centre, times translation 0 or (2,2,2)), exactly 24 keep the roles up to vertex-cube / edge-face duality, and the rule is invariant under all 24. The (2,2,2) translation swaps the tilings, and since the A and B gates commute, the tick is exactly invariant under it. The 90-degree rotations break the grading against the tilings, so the 24-element group is the most that any rule on these tilings can have.
5. Two copies, not one field (exact). No operator crosses between the primal sector (vertex and edge sites) and the dual sector (face and cube sites): 0 of 1024 rows leak. The rule is two decoupled Z2 gauge-matter systems that duality exchanges.
6. Propagation (finite diagnostic). On a 40^3 torus the Heisenberg support of X_e has radius 2t - 1 fine sites (one coarse cell per tick) for 2 <= t <= 9. It saturates near L/2, its weight grows into the thousands, and it does not recur within 24 ticks. The finite-torus periods (12 on 8^3, 24 on 12^3, and 24 on 16^3 in a scratch run) are commensurability effects.
7. U(1) local form (exact on joint supports). On spin-1/2 links, the ring exchange on a face's four edge sites and the matter hop psi_v'^dag S^-_e psi_v + h.c. commute with the U(1) divergence div E - n. At spin 1/2 the electric term (S^z)^2 = 1/4 is constant, so the U(1) rule has no on-site layer, and its dynamics was not simulated.
8. Global versus local (exact). prod_v G_v = prod_v X_v: the primal Gauss laws multiply to the global matter parity exp(i pi Q), the Z2 inside the tick's U(1).

## Answers

- Is Rule G realisable? Yes, in the Z2 form. An explicit reversible, nearest-neighbour-supported qubit tick on 4^3 blocks with two tilings conserves every Gauss star exactly, conserves nothing else that is a Pauli, moves every gauge and matter site, and couples them. The freezing is a property of the 2^3 tick cubes, not of qubit gauge rules: it is exact at 2^3 and gone at 4^3.
- What is derived and what is supplied? Derived: the global group, the U(1) mode number of the free tick, and the fact that its local form on a qubit edge register is exactly Z2 (the parity subgroup; item 8); the block side >= 4 (items 2 and 4); and that single-site X terms do not freeze the dynamics. Supplied: the flux register on edge sites, the boundary-map form of the stars, the generator list (the lowest-weight gauge-invariant operators), the angle pi/4 and the layer order.
- Is there a photon or a deconfined Z2? Not shown. The Clifford tick spreads operators ballistically and scrambles them like an infinite-temperature Floquet system; for the single-site operators tested, the weight grows, so they are not gliders. A systematic glider search and any dispersion relation were not done. "Deconfined" needs an energy or a stationary state, and a Floquet tick has neither. The U(1) photon would need the quantum-link dynamics, which is beyond exact reach here.

## Gate (Rule G-blocks)

1. Measured numbers: none. pi/4 is the Clifford point, the square root of the Pauli involution. PASS.
2. Observed structure by name: no group is written in. U(1) comes from the tick's commutant, and Z2 is what one qubit per edge carries exactly. The star form comes from the rung-2 boundary map. The generator list matches the standard Z2 lattice gauge theory with matter (Wegner, Fradkin-Shenker); it is the minimal gauge-invariant set, but it is chosen. PASS with that caveat.
3. Prediction it was not built for:
   - No conserved Pauli beyond the Gauss group: no topological constants, and a one-cell-per-tick light cone.
   - Primal and dual are always decoupled.
   Neither has a measured test, so the rule is UNTESTED against measurement.
4. Axiom bent: none. Every gate is a site plus nearest neighbours, and the 4^3 block is only the schedule.

## Boundary

- Clifford angle only, beyond the any-angle conservation theorem. 8^3 is exact; 12^3 and 40^3 are diagnostics.
- The block tilings do not change which gates commute: all Z gates commute, so the tilings only select which generators act. With side-4 blocks, the plaquettes whose odd coordinates are (1, 3) mod 4 never act.
- No coupling between primal and dual sectors, no fermionic charge (the matter is a qubit, with bosonic Z2 charge), and no chiral content.
- The U(1) checks are commutators only.

## Notes used

- Built on and narrowed: the cell-complex-from-update draft (freezing from stars alone, Rule G realised in Z2 form) and the emergent-gauge-composite draft (its stars are now conserved by an explicit tick, with matter).
- Cited: Margolus 1984; Wegner 1971; Kogut 1979; Fradkin-Shenker 1979; Chandrasekharan-Wiese 1997 (quantum link).
