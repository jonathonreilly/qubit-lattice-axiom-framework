---
claim_id: edge_and_square_graph_weight_has_no_cubic_ordered_phase_bounded_no_go_note_2026-10-22
claim_type: bounded_theorem
claim_scope: "For the classical graph weight E = a*(number of edges) - b*(number of 4-cycles) on simple graphs (the brainstorm's Ruleset B4), the cubic lattice Z^3 is not a local minimum under single edge toggles for any b/a: removing an edge is stable only for b/a >= 1/4, while adding a body diagonal is stable only for b/a <= 1/6. With no degree cap the ground state for b/a > 4/((N-2)(N-3)) is a dense clump (the complete graph), and with a hard cap c it is the empty graph for b/a < 4/(c-1)^2 and disjoint bicliques K_{c,c} above, so Z^3 is never the ground state. A cap c = 2d makes Z^d metastable for b/a >= 1/(2(d-1)) for every d, so the cap, not the weight, picks the dimension. Seeded Metropolis runs on N = 64-625 confirm: no window of b/a gives a cubic phase. The claim is classical and finite; it does not cover quantum superpositions of graphs, other weights, or the B2 update."
upstream_dependencies:
  - minimal_axioms
  - candidate_laws
runner: scripts/edge_and_square_graph_weight_has_no_cubic_ordered_phase_2026_10_22.py
---

# The edge-and-square graph weight has no cubic ordered phase

Claim type: bounded_theorem (exact single-move and ground-state bounds) with finite Monte Carlo diagnostics.
Primary runner: `scripts/edge_and_square_graph_weight_has_no_cubic_ordered_phase_2026_10_22.py`.

The candidate-law register has zero premise weight. The 2026-10-22 brainstorm (Ruleset B) proposed replacing the fixed Z^3 lattice by a dynamical neighbour relation with weight B4: "each neighbour costs a fixed phase and each closed four-cycle earns one". It asked for a decisive cheap test: does a lattice-like ordered phase (degree 6, spectral dimension about 3) appear over a finite window of the weight ratio? This note answers no for the classical (real Boltzmann) form of B4.

## Statement

Let E(G) = a m(G) - b q(G), where m is the edge count and q the 4-cycle count of a simple graph G, with a, b > 0.

1. **Single-move window is empty (exact).** In Z^3 every edge lies in exactly 4 squares, and the largest number of length-3 paths between two non-adjacent vertices is 6 (the body diagonal). So removing an edge changes E by -a + 4b, and adding a body diagonal changes it by a - 6b. Z^3 is stable against both only if 1/4 <= b/a <= 1/6, which is empty. Z^3 is not even metastable under B4.
2. **No geometric ground state without a cap (exact).** The complete graph K_N has E = a N(N-1)/2 - 3b C(N,4). It beats both the empty graph and Z^3 once b/a > 4/((N-2)(N-3)): 1.1e-3 at N = 64 and 8.8e-5 at N = 216. The weight is not extensive, and its ground state has diameter 1.
3. **With a hard degree cap c, the ground state is still not a lattice (exact).** An edge uv lies in at most (d_u - 1)(d_v - 1) <= (c-1)^2 squares, q = (1/4) sum over edges of the square counts, and m <= cN/2. So E/N >= (m/N)(a - b(c-1)^2/4). The minimum is the empty graph for b/a < 4/(c-1)^2, and disjoint K_{c,c} bicliques above it, where the bound is saturated. At c = 6 the threshold is 0.16, and K_{6,6} gives 18.75 squares per vertex against Z^3's 3. These ground states are disconnected and zero-dimensional.
4. **The cap picks the dimension (exact).** Z^d has 2(d-1) squares per edge. Under cap 2d additions are blocked, so Z^d is a local minimum exactly when b/a >= 1/(2(d-1)). That holds for every d, so the weight does not select d = 3. Choosing c = 6 inserts it.

## Finite diagnostics (runner, seed 20261022)

Measurements: mean and maximum degree, 4-cycles per vertex, giant component, spectral dimension d_s from the lazy-walk return probability with the zero mode removed (t = 4 to 12), ball-growth slope for r = 1 to 3, and a local cubic order parameter. The order parameter is the fraction of vertices whose neighbours, joined when they share a square through the vertex, form the cross-polytope link of Z^D.

Calibration on exact tori: d_s = 0.98, 2.17, 3.40 and 4.23 for Z^1 to Z^4, so the estimator orders dimensions. The Z^3 5^3 torus reads d_s = 3.62 with order parameter 1. A random 6-regular graph on 125 vertices reads 4.23 with order parameter 0. The ball slope is weak at these sizes (Z^3 reads 1.94) and is reported only.

- **Uncapped, starting from the 5^3 torus at T = 0.15.** For b/a = 0.05 and 0.12 the graph evaporates (mean degree below 0.3). For b/a = 0.2 to 1.2 it collapses to a near-complete clump (mean degree about 124 of 124). The window between 1/6 and 1/4 goes to the clump.
- **Uncapped, random start with mean degree 6, annealed from T = 2 to 0.15 on N = 64.** Every b/a in 0.05 to 1.2 collapses to K_64.
- **Cap 6, starting from the torus at T = 0.15.** The lattice survives at b/a = 0.6 and 1.2. At 0.3 it melts thermally, since the removal cost is 0.2 against T = 0.15. Below 1/4 it evaporates. This matches item 4: a metastable branch only.
- **Cap 6, random start annealed (300 sweeps on N = 64).** The local cubic order parameter stays 0, and the squares per vertex grow to 8.8 and 13.3, heading toward the K_{6,6} value of 18.75. At b/a = 0.4 the graph fragments (giant component 38 of 64).
- **Methodological caution.** Shorter anneals at N = 125 and 216 (exploratory, not in the runner) gave mean degree about 5.9, d_s = 2.9 to 3.35 and ball slope about 1.9, which mimic the Z^3 torus. Yet the local cubic order parameter was exactly 0, with a broad spread of squares per edge and some triangles. Degree plus spectral dimension at these sizes cannot certify a lattice; a local order parameter is needed.
- **Cap picks d.** Starting from Z^2 (cap 4), Z^3 (cap 6) and Z^4 (cap 8) at b/a = 1.2, each lattice stays metastable with order parameter 1 and d_s = 2.27, 3.62 and 4.09.

## Literature (checked by web search; abstracts only, not full texts)

- Konopka, Markopoulou and Smolin, "Quantum Graphity", hep-th/0611197: a complete-graph model whose low-temperature phase is argued, not proved, to be a low-dimensional lattice. Quach et al., arXiv:1203.5367: in that model a honeycomb lattice is a stable local minimum only under particular parameter constraints.
- Conrady, "Space as a low-temperature regime of graphs", J. Stat. Phys. 142 (2011) 898, arXiv:1009.3195: a weight designed to have 2D triangulations as ground states, with a fixed edge count.
- Trugenberger, "Combinatorial quantum gravity: geometry from random bits", arXiv:1610.05934; Kelly, Trugenberger and Biancalana, arXiv:1811.12905 and arXiv:1901.09870. These works use Ollivier curvature, which depends only on short-cycle counts at an edge, as the action on REGULAR graphs, so the degree is fixed as input. The abstracts report that action minima are "cubic complexes up to defects". A later random 3-regular study reports dimension 1, and a review reports a 2D phase.
- Consistent reading: every emergent-lattice result found fixes a degree, an edge count, or a designed ground state. That matches items 3 and 4: the dimension enters through the constraint. No paper found claims that an unconstrained edge-plus-square weight orders into Z^3.

## Gate result (anti-smuggling gate)

- B4, unconstrained: the gate is not reached, because the rule fails. No window of b/a gives the lattice; the outcome is FAIL as a lattice-origin rule.
- B4 plus a degree cap of 6: FAILS clause (2) of the gate. The cap value 6 = 2d inserts the observed dimension, and even then Z^3 is only metastable, never the ground state.
- Axiom bent by Ruleset B: the Lattice axiom (Z^3 is given), replaced by a dynamical neighbour relation. That bend is not earned by B4.

## What this does not close

- The test is classical. B4 as a quantum phase weight on graph superpositions, with the B2 local unitary, is not tested here; interference between graphs could change which configurations dominate. That is UNTESTED.
- Other weights. Any weight built only from short-cycle counts must avoid both the clique and the biclique. Two examples:
  - A cost for pairs of squares sharing two edges kills K_{c,c}, but Z^d of every d has no such pairs, so d would still be unselected (PLAUSIBLE).
  - A rule that selects d = 3 needs an ingredient that sees dimension: for example, the spectral properties of the B2 update or record consistency. That remains MISSING.
- Dark matter as graph disclinations and Kibble-Zurek seeds (Ruleset B scorecard) both presuppose an ordered phase. They are therefore unsupported by B4.

## Relation to repo notes

- The repo has no prior dynamical-graph or graphity work on main (searched: graphity, dynamical graph, geometrogenesis, Trugenberger).
- BACKGROUND_INDEPENDENCE_NOTE.md measures spectral dimension on a FIXED weighted cubic lattice (about 2.9), with a related estimator. It is not contradicted.
- E1 of the brainstorm (removing the lattice does not remove chirality doubling) is unaffected; this note removes the other half of Ruleset B's motivation, the lattice as an ordered phase.
