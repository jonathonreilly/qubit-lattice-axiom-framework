---
claim_id: the_composite_twist_walk_is_a_five_layer_cube_local_circuit_and_freezing_one_copy_leaves_one_l_and_one_r_per_node_bounded_theorem_note_2026-10-23
claim_type: bounded_theorem
claim_scope: "Free bands of composite TWIST (CTWIST) on CL-1's 2^3 cell (one mode per site, 8 cell states, the 12 tetrahedral rotations T with CL-1's site gauges). (A) CTWIST is not an even.odd.even product of cube-local layers (exact). Numerically it factorises into five cube-local layers even.odd.even.odd.even on CL-1's two tilings: block-coordinate polar ascent finds unitary gates whose product matches CTWIST to residual below 1e-10 on the 5^3 momentum grid and at four off-grid momenta; this is a numerical diagnostic, and an exact gate witness is open. No circuit whose layers each commute with the site rotations was found to depth 9 (finite search). (B) Representation statement: at the T-fixed nodes every level of any T-covariant cell walk is a 2-fold spinor irrep, and the two eta copies carry identical irreps (T acts trivially on the eta algebra), so no free term built from T alone distinguishes the copies. Degeneracy alone gives no Weyl dispersion and no persistence of a Weyl node under deformation: a constant scalar unitary is T-covariant and has none (negative result). Rule FREEZE (the sector where CL-1's chirality disagrees with the walk's does not hop) is unitary, T-covariant, numerically factorises into five cube-local layers (same caveat), and its computed bands have exactly one nondegenerate L Weyl (q = 2) and one R Weyl (q = 1) per node. (C) The label term exp(i phi (1 - tau3)/2), computed at phi = pi/2 and pi, relocates the R content without gapping it; other phases and other free terms are not covered. Not covered: an exact five-layer gate witness, interactions, the multi-family mirror term, measurement."
upstream_dependencies:
  - minimal_axioms
  - candidate_laws
  - the_cell_taste_doublet_is_a_geometric_tetrahedral_twist_giving_a_one_qubit_chiral_turn_charge_walk_bounded_theorem_note_2026-10-23
  - two_qubit_site_dirac_walk_is_vector_like_and_a_tetrahedral_twist_gives_a_chiral_turn_charge_with_a_pinned_pi_doubler_bounded_theorem_note_2026-10-22
runner: scripts/the_composite_twist_walk_is_a_five_layer_cube_local_circuit_and_freezing_one_copy_leaves_one_l_and_one_r_per_node_2026_10_23.py
---

# The composite TWIST walk factorises numerically into five cube-local layers; freezing one copy leaves one L and one R per node

Claim type: bounded_theorem (exact free-band statements, one numerical factorisation and one finite search, each labelled).
Primary runner: `scripts/the_composite_twist_walk_is_a_five_layer_cube_local_circuit_and_freezing_one_copy_leaves_one_l_and_one_r_per_node_2026_10_23.py`; cache `logs/runner-cache/the_composite_twist_walk_is_a_five_layer_cube_local_circuit_and_freezing_one_copy_leaves_one_l_and_one_r_per_node_2026_10_23.txt`. Axioms unchanged.

Local labels (2026-11-14). "CL-1" is this note's source label for the supplied cube tick (a Margolus-type walk on 2^3
cubes, one fermion mode per site, two tilings) and its chirality chi; it is not CL-1 of the current
[candidate-law register](CANDIDATE_LAWS.md), which is a historical alias with zero premise weight. "R10" and "R11" are
source-local requirement labels: R10, the light copy carries a nonzero turn charge so that a family count follows;
R11, light and mirror sit at different exact momenta. composite-twist (#10028) is recorded only in the consolidation's
source map; CTWIST is rebuilt inline by the runner. Statements here are conditional on these supplied models.

## Question

composite-twist left three items open on CTWIST, U(K) = f + i(h1 tau1 + h2 tau2 + tau3 g.sigma):
(i) the light content is doubled by CL-1's chirality eta = chi acting as a spectator;
(ii) the hop spans up to 3 site steps -- is the walk a product of cube-local (2^3) layers on CL-1's two tilings?
(iii) after (i)-(ii), is the content one L (q = 2) and one R (q = 1) per node, and what does a label mirror
term (1 - tau3)/2 do?

## A. Layers (item ii)

- A1 (exact no-go, depth 3). Any even.odd.even product C1 D C2 D^+ C3 (D = diag(e^{-iK.a}); this contains
  CL-1's own odd.even shape) needs the ranges of the z_i coefficients to cut the cell into 8 one-dimensional
  vertex spaces. CTWIST's three range projectors have rank 4 and commute, but their joint spaces have dims
  (2,2,2,2,0,0,0,0): two states on each vertex of one tetrahedron. So depth 3 is impossible.
- A2 (numerical diagnostic, depth 5; narrowed 2026-11-14). Block-coordinate (polar) ascent finds unitary gates with
  CTWIST ~ C1 . O(C2) . C3 . O(C4) . C5, where C1, C3, C5 are even-cube gates and O(C) = D C D^+ odd-cube gates, to a
  residual below 1e-10 (printed about 1e-14) on the 5^3 grid and at four off-grid momenta. Each such product is a
  Laurent polynomial of degree <= 2 per direction, so if equality held exactly on the 5^3 grid it would hold
  everywhere. A small residual does not prove that exactly satisfying unitary gates exist, so this is not an exact
  circuit theorem: an analytic or certified exact gate witness is an open obligation. Control (A2c): the same ascent
  at depth 3, where A1 proves no factorisation exists, stalls far from 0. If an exact witness exists, conjugating by
  C5 gives two CL-1-shaped ticks (odd.even.odd.even) with different gates. A later source's winding theorem
  (#10064) excludes turn-covariant layerings; it does not supply this gate witness.
- A3 (finite diagnostic). With every layer commuting with the 12 site rotations (frames V; diagonal gauges are
  absorbed into the gates), no factorisation was found at depth 5, 7 or 9 (rms floors 1.59, 1.30, 1.25). The
  depth-5 gates found are not T-invariant. T-covariance holds for the full walk, not gate by gate. This is a
  search, not a proof.

Answer (ii): numerically, the walk matches a product of five cube-local layers. If an exact five-layer witness
exists, CTWIST is a finite cube-local circuit with the same status as CL-1's tick, with five layers instead of two;
that exact witness is open. (Rematched 2026-11-14 against the current axioms: the earlier text said CTWIST would then
"not bend nearest-neighbour admissibility". The current Admissibility axiom names a neighborhood rule for the site
distribution and is not a dynamics axiom, so it neither fixes nor bounds a walk's gates; the layer question is a
property of the supplied walk, not an axiom comparison.) Open as well: whether some covariant layering exists (A3 found
none).

## B. The eta doubling (item i)

- B1 (exact, a representation statement). Every T-invariant on-cell operator commutes with sigma and tau3
  (dim 8 = M2 + M2 on the eta copies). At the T-fixed nodes K = 0 and R, U(node) is such an operator for any
  T-covariant cell walk, so every level there is a 2-fold spinor irrep.
- B1c (negative result for the earlier reading, corrected 2026-11-14 from the second hold, R5). The source added
  that a free T-keeping term "can never gap a node Weyl". Degeneracy does not support that. Witness: the constant
  scalar walk e^(0.3 i) 1 is T-covariant and its node levels are degenerate, but its velocity is 0, so it has no
  Weyl dispersion at all (runner B1c). Degeneracy supplies neither a nonzero velocity nor an obstruction to
  deforming or annihilating a node. What holds: FREEZE's computed node Weyls are nondegenerate (smallest
  |det velocity| 0.192, runner B1c). Their persistence under deformations of FREEZE is not shown here.
- B2 (exact). The eta algebra (commutant of sigma and tau) is M2 = <chi, eta_x>, and T acts on it trivially. The
  two copies have identical irreps at both nodes, so no rotation tells them apart. Only a cell operator (chi) can.
  The doubling therefore cannot be removed by a free term built from T alone. A rule has to use chi.
- B3 (exact). Chirality agreement: the T-invariant cell relabelling Y = P_w + P_wbar eta_x gives U_A = Y U Y^+,
  whose taste flips are tau_1,2 eta_x. U_A conserves Pi+ = (1 + chi tau3)/2, the states where CL-1's chirality
  agrees with the walk's. eta_x is an exact symmetry of U_A that swaps Pi+ and Pi-, so choosing Pi+ is a
  convention, not a lopsided physics choice.
- Rule FREEZE: U_F = Pi+ U_A + Pi- (i tau3). The disagreeing sector does not hop; each cell ticks it by a
  quarter phase.
  - B4. U_F is unitary and T-covariant. On a 12^3 grid, quasienergy 0 occurs only at K = 0 and pi only at R
    (gap >= 0.30 elsewhere). The frozen states are flat at +-pi/2, the point equidistant from both node
    quasienergies.
  - B6. U_F also matches a product of five cube-local layers numerically (residual about 6e-15; same caveat as A2).

## Answers

(iii) Light content. Under FREEZE, exactly one L Weyl (q = 2) and one R Weyl (q = 1) sit at each node (B5):
2 L + 2 R in all, half of CTWIST's 4 + 4. By Schur (B1, different characters), no T-invariant L-R mass exists.
R10 still holds (every light L at q = 2), now with n_L halved.

Label mirror term (C1-C2, computed at two phases plus one root-find):
- exp(i phi (1 - tau3)/2) on Pi+ at phi = pi/2 moves the K = 0 R Weyl to pi/2, still a 2-fold irrep, and opens a
  quasienergy-0 Fermi surface: sigma_min(U - 1) = 7e-9 at k = 2.22 on a generic line.
- At phi = pi, the R-labelled states at the R node land at quasienergy 0.
- The label is exact at the nodes and leaks O(K^2).

At the phases computed the label term relocates the mirror and does not gap it. Other phases and other free terms
are not computed (the earlier "any free label term" and "never" are narrowed, second hold R5). A free route that
separates the mirror is not found here. As in
composite-twist, w^(4q) != 1 per family, so that term must be multi-family (the SMG route), which is not
computed here. R11 (light and mirror at different momenta) is still NOT MET.

Gate (rule FREEZE):
1. Numbers: none fitted. The +-pi/2 placement is the point equidistant from the two node quasienergies, and the
   +i versus -i assignment is fixed by tau3. Pass, with that convention flagged.
2. Named structure: none. It uses chi (CL-1's own chirality) and tau3 (cell geometry). Pass.
3. Prediction not built for: 4 cell-local, non-propagating modes per cell at quasienergy +-pi/2 (inert dark
   states in the vacuum); light content 2 L + 2 R with a pinned pi-node. Not compared with measurement. UNTESTED.
4. Comparison with the current axioms (rematched 2026-11-14): one mode per site, sites on Z^3, so the Lattice and
   Qubit axioms are not departed from; the tick and its gates are supplied, since no axiom states an update rule and
   Admissibility is not a dynamics axiom. Whether FREEZE is a finite cube-local circuit depends on an exact five-layer
   witness (A2, B6 are numerical; the exact witness is open). As with CTWIST, it replaces CL-1's O-covariant tick with
   a T-covariant walk.

Result: FREEZE passes items 1 and 2; item 4 records no axiom departure, and its circuit status waits on an exact
five-layer witness; item 3 is UNTESTED. It is a candidate with zero premise weight, not adopted.
Honest weakness: FREEZE removes the doubling by declaring half the cell inert. It uses a structural selector,
but its motive is the count. B2 shows that no free term built from T alone can tell the eta copies apart, so a
rule that removes the doubling has to use a cell operator such as chi.

## Smuggling review

- Supplied:
  - CTWIST itself (from composite-twist);
  - the chirality-agreement selector chi tau3;
  - the frozen-sector tick i tau3;
  - the layer ansatz (even/odd cube gates).
- Forced:
  - the depth-3 no-go and the tetrahedral (2,2,2,2,0,0,0,0) range structure;
  - (numerical, not forced) the depth-5 factorisation;
  - Schur/Kramers degeneracy at the nodes (a representation statement; no velocity or persistence, B1c);
  - the trivial T action on the eta algebra;
  - the content 1 L (q = 2) + 1 R (q = 1) per node;
  - the failure of the label mirror term at the two phases computed.
- Not used: any measured number or named gauge group.

Next probe: an analytic or certified exact gate witness for A2 and B6, and an exact covariant-layer obstruction or construction for A3. Then the multi-family charge-4 mirror
interaction on Pi+ with FREEZE.
