---
claim_id: the_cube_cell_slab_wall_holds_at_most_two_opposite_handed_copies_so_families_are_not_wall_nodes_while_the_supplied_wilson_kernel_gives_a_turn_triplet_only_in_an_unforced_window_bounded_theorem_note_2026-10-23
claim_type: bounded_theorem
claim_scope: "Free-field wall spectra of two domain-wall slabs (layer index as a role-block coordinate, open layer chain, Shamir-type layer hop). (W) The supplied tick-form slab (the source's 'adopted' slab, chiral-tick-form: Wilson-type kernel, 4 components per Z^3 site): near-wall Weyl nodes sit at the zone corners with n pi-components exactly when 2n < m < 2n + 2 (zero-mode ratio 1 - m + 2n); windows (0,2), (2,4), (4,6), (6,8) give 1 (G), 3 (X), 3 (M), 1 (R) nodes; within a window all nodes have one hand, the hand alternates as (-1)^n, and the far wall carries the opposite total; on the 3-node walls the three-fold turn about (111) acts as the single node's spinor pair times {1, w, w^2}, a turn triplet. (C) The same slab built on CL-1's own cell (2x2x2 cube cell, 8 one-mode sites, face phase -1, both tilings): D = R_e - R_o, B = R_e + R_o and eps = (-1)^(x+y+z) anticommute exactly with D^2 + B^2 = 4, so at copy mass Mc = 0 every wall zero mode lies in ker D; on a 16^3 grid D vanishes only at K = 0, on two 4-component copies s = +1, -1; with CL-1's copy operator (1 - s) R_e (tested at Mc = 0.8 and 1) the near wall holds the s = +1 copy for 0 < m < 2 and the s = -1 copy for Mc < m < Mc + 2 at K = 0, and at the six gapped test points no other wall state appears on an 8^3 grid (a finite diagnostic: the copy mass does not anticommute with D, so extra off-K = 0 wall zeros elsewhere in the windows are not excluded); the two copies have OPPOSITE hands, so the two-copy window is vector-like; their turn charges differ by a nontrivial cube root; at Mc = 3 the bulk is gapless. Nothing in CL-1 fixes the layer mass window. Not covered: interactions, gauge fields, the far-wall fate, a Floquet (circuit) version of the cell slab, a derivation of the Wilson kernel from the cell."
upstream_dependencies:
  - minimal_axioms
  - candidate_laws
  - a_domain_wall_tick_with_the_layer_direction_as_space_puts_one_weyl_cone_on_each_wall_but_the_circuit_forces_the_mirror_onto_the_far_wall_bounded_theorem_note_2026-10-23
  - the_overlap_of_the_cube_walk_euclidean_kernel_gives_exact_ginsparg_wilson_chirality_without_doublers_but_its_chiral_projector_is_not_a_walk_sector_bounded_theorem_note_2026-10-23
runner: scripts/the_cube_cell_slab_wall_holds_at_most_two_opposite_handed_copies_so_families_are_not_wall_nodes_while_the_supplied_wilson_kernel_gives_a_turn_triplet_only_in_an_unforced_window_2026_10_23.py
---

# At the tested points the cube-cell slab wall holds at most two opposite-handed copies, so families are not wall nodes there; the supplied Wilson kernel gives a turn triplet only in an unforced window

Claim type: bounded_theorem (exact zero-mode recursions and cell algebra; labelled finite diagnostics; the domain-wall
construction and the Wilson-kernel identification are supplied and cited).
Primary runner: `scripts/the_cube_cell_slab_wall_holds_at_most_two_opposite_handed_copies_so_families_are_not_wall_nodes_while_the_supplied_wilson_kernel_gives_a_turn_triplet_only_in_an_unforced_window_2026_10_23.py` (13 PASS / 0 FAIL, about 25 s, 62 MB peak, 5.2 k characters; exits nonzero on any failed check).
Axioms unchanged. No rule adopted.

**Repair 2026-11-14 (PR 10129 hold, finding 9).** The source version stated that the cell slab has wall states only at K = 0, at most two copies, and no other wall nodes, for every gapped window. Only part of that is exact. At Mc = 0 the (D, B, eps) algebra gives H^2 = D^2 + M^2, so wall zero modes need ker D (new check C1b); that ker D is nonzero only at K = 0 is a 16^3-grid result. With the copy mass, (1 - s) R_e does not anticommute with D (C1b control, C2b), and the exclusion of other wall states is the finite diagnostic C3: six gapped test points, an 8^3 grid, Ls = 24. A global spectral argument for every gapped (m, Mc) is an open obligation. This is not evidence of an extra node.

**Local labels (2026-11-14).** CL-1 here names the source's supplied cube-tick update law (its cell, tilings and copy operator), not entry CL-1 of [`CANDIDATE_LAWS.md`](CANDIDATE_LAWS.md); the "tick-form clause" and "adopted slab" are source-branch texts, used here as supplied models with no premise weight. Source names: two-tiling-family-space is [#10044](THE_TWO_TILING_TICK_HAS_NO_CELL_LOCAL_FAMILY_SYMMETRY_AND_A_TURN_TRIPLET_FORCES_TURN_INVARIANT_MIXING_TO_BE_CP_BLIND_BOUNDED_THEOREM_NOTE_2026-10-22.md), families-from-tastes is [#10016](THE_CUBE_TASTES_ARE_TWO_DOUBLETS_AND_NO_SYMMETRY_PROTECTS_A_FAMILY_TRIPLET_BOUNDED_THEOREM_NOTE_2026-10-22.md), family-count-5mode is [#10022](THE_LIGHT_COPY_CARRIES_A_NONZERO_TURN_CHARGE_SO_A_SYMMETRICALLY_GAPPED_MIRROR_NEEDS_FAMILY_COUNT_ZERO_MOD_THREE_BOUNDED_THEOREM_NOTE_2026-10-22.md) and spontaneous-turn-cp is [#10047](A_TURN_KEPT_BY_THE_UPDATE_AND_BROKEN_BY_THE_VACUUM_GIVES_CP_AND_THETA_BAR_TOGETHER_UNLESS_A_NELSON_BARR_BLOCK_IS_SUPPLIED_BOUNDED_THEOREM_NOTE_2026-10-22.md), all carried in this PR. chiral-tick-form (#10056), overlap-from-walk (#10049), families-mod-3 (#9903) and composite-before-atomic are not in this repository; what this note takes from them (the slab, its m = 0.6 point, A-T2, the overlap doubler counts) is a historical reported result, unverified here, and is used only as a supplied input.

## Question

The working tick form (CL-1 tick-form paragraph, chiral-tick-form) puts one Weyl node per wall at k = 0. How many light
Weyl copies does the near wall carry per field, at what momenta and hands, and how does the three-fold cube turn act on
them, across the layer-mass windows? A window with three same-handed nodes permuted by the turn would be a
framework-native family triplet.

Repo first. Builds on chiral-tick-form (the slab, its m = 0.6 point, and A-T2: a local slab has W3 = 0, so the far wall
carries the mirror), overlap-from-walk (4D overlap doubler counts 1, 5, 11, 15 for m0 = 1, 3, 5, 7; Wilson-kernel
identification supplied), two-tiling-family-space (cell fibre = spin x 2 tastes without the copy mass, x 1 with it;
turn-CP lemma), families-from-tastes (cell tastes E + E, never 1 + 3), family-count-5mode and families-mod-3 (N = 0 mod 3
from the light copy's nonzero turn charge, conditional on mirror gapping). No main note on domain-wall family counts
was found (git grep on origin/main).

## W. Supplied tick-form slab (the source's adopted slab; Wilson-type kernel, 4 components per site)

Exact (zero-mode recursion, rederived): at a corner with n pi-components, A chi = 0 and psi_s = (1 - m + 2n)^s chi solve
H psi = 0 on the near wall, so a node exists iff |1 - m + 2n| < 1, i.e. 2n < m < 2n + 2.
Finite diagnostics (Ls = 12; pre-set criteria in the runner lines):
- W1 bulk gapped at m = 0.6, 1, 3, 5, 7 (gaps 0.6, 1.0, 1.0, 1.0, 1.0).
- W2 nodes: m = 0.6, 1: G; m = 3: the three X points; m = 5: the three M points; m = 7: R. Each node is 2-dim.
- W3 hands: near-wall totals -1, -1, +3, -3, +1; all nodes in a window share a hand; far wall opposite.
- W4 m = 3: no in-gap state away from the X points (10^3 grid).
- W5 the turn (spinor lift, covariance 6e-16) permutes X1 -> X2 -> X3 (and the M's); the 6-dim wall space has turn phases
  {e^(i pi/3), -1, e^(-i pi/3)} each twice = G's spinor pair x {1, w, w^2}, and not x {1, 1, 1}: a turn TRIPLET.
- W6 the three X nodes are also split by unit translations; with only 2Z^3 block translations (CL-1's role layout)
  they fold to block K = 0 and the turn is their only label.
So the window (2,4) gives three same-handed wall Weyls forming a turn triplet. It is anomaly-consistent in the inflow
sense (net +3 on the near wall, -3 on the far wall; A-T2 holds for every m), so the mirror is still forced onto the far
wall, now as a mirror triplet. Under the turn-CP lemma (two-tiling-family-space C), turn-invariant masses on this
triplet give J = 0.

## C. The slab on CL-1's own cell

Exact (cell algebra, checked to 2e-15 at generic K): the even and odd cube hops are reflections, so D = R_e - R_o and
B = R_e + R_o anticommute and D^2 + B^2 = 4; every hop flips eps = (-1)^(x+y+z), so eps anticommutes with both; the copy
sign s commutes with R_e. Hence (D, B, eps) is a kinetic/mass/layer-chirality triple for a Shamir layer hop
A = (B/2 + i eps)/2, with CL-1's own copy operator (1 - s) R_e as the copy-dependent mass. At Mc = 0, D x 1 anticommutes
with every other term of the slab Hamiltonian, so H^2 = D^2 x 1 + M^2 >= D^2 and a wall zero mode needs ker D (C1b,
defect 1e-16; control at Mc = 1: 1.39). On a 16^3 grid D vanishes only at K = 0 (next-smallest |D| is 0.23), on all 8
modes: two 4-component copies (s = +1: 4, s = -1: 4). There are no X, M or R points in this cell: the 8-site cell has no
Wilson-type corner doublers to supply a triplet. With Mc > 0 the anticommutation fails, so the following counts are
finite diagnostics.
Finite diagnostics (Ls = 24):
- C2 for Mc = 0.8 and 1: near-wall copies = s+ iff 0 < m < 2, s- iff Mc < m < Mc + 2 (layer mass m - Mc); all six points
  gapped (0.37 to 0.60). Windows: (0, Mc) one copy (s+), (Mc, 2) two, (2, 2 + Mc) one (s-).
- C2b the pre-set 'gapped at Mc = 3' FAILED: at Mc = 3 the bulk is gapless (1e-16 on the 8^4 grid), because (1 - s) R_e
  does not anticommute with D. A separate large-copy-mass s- window is not a gapped phase. Recorded as a result.
- C3 (finite-grid diagnostic) at the six gapped test points (m, Mc) in {0.4, 1.4, 2.4} x {0.8} and {0.5, 1.5, 2.5} x {1},
  on an 8^3 grid with |k| >= 0.9 and Ls = 24, no state lies below 0.05 (minima 0.31 to 0.48). At those points the wall
  holds at most 2 copies per field. The source tested one point, (1.5, 1). Other (m, Mc) are not covered.
- C4 a lone s+ copy has hand +1, a lone s- copy -1 (far wall opposite in each case): the copies have OPPOSITE hands.
- C4b in the two-copy window the near wall has net chirality 0 (s+ +1, s- -1, no first-order mixing): a vector-like
  pair, not two families.
- C5 the turn (site-phase lift, keeps both tilings, s and eps; defect 0) acts on each copy as a spin-1/2 pair times a copy
  phase; the s- copy's phase is the s+ copy's times w^2 (dq = 2): charges {q, q + 2}, never a triplet.

## Answer

On CL-1's own cell, at the tested points, the wall carries exactly ONE Weyl copy per field in each gapped chiral window,
(0, Mc) [s = +1] or (2, 2 + Mc) [s = -1], and a vector-like pair in (Mc, 2); no tested point has three. At Mc = 0 this
follows from ker D (exact, given the 16^3 grid for ker D); with the copy mass it is the finite diagnostic C3, and a global
spectral argument for every gapped (m, Mc) is open. The turn triplet exists only for
the supplied Wilson-type kernel (4 components per site = 32 modes per 2x2x2 cell, four times CL-1's 8), and only for
m in (2,4) or (4,6). Nothing in CL-1 or the tick-form clause selects that window; the source's chosen m = 0.6 is in (0,2). The
copy mass's role in CL-1 (making s = +1 the one light copy) agrees with the (0, Mc) window, which is a reason, though not
forced, for the low window.

Where families must come from, if not wall nodes: (a) extra layers do not add copies (Ls changes only the |r|^Ls overlap);
(b) no wall-bound states at other momenta on the cell slab at the tested points (C3); (c) so it is the cell content: either a 4-mode-per-site
composite that realises the Wilson kernel (the X-window triplet then becomes a family candidate, but needs a rule for its
window and a composite construction; composite-before-atomic), stacked copies (families-mod-3 / family-count-5mode,
N = 0 mod 3 conditional), or a two-rung parent-cube space (two-tiling-family-space B: a turn triplet in one parent cube,
broken by the second tiling). Whichever is used, a turn triplet with turn-invariant masses gives J = 0 (lemma), so CP needs
a turn-breaking vacuum (spontaneous-turn-cp).

## Gate (anti-smuggling)

No rule proposed. Supplied: both slab kernels, the Shamir layer hop, m, Mc in slab units, Ls, free fields, Hamiltonian
(not circuit) form of the cell slab. Choosing m in (2,4) to get three would be a fitted choice (FAILS the gate) unless a
rule fixes the window. Prediction not built for (UNTESTED): a cell-built slab at m in (Mc, 2) has a vector-like light
pair on every wall, which an s-breaking term gaps; only the outer windows are chiral.

## Smuggling review

Forced: the window conditions (exact recursion), the cell algebra (D, B, eps), the two-copy limit of the cell at Mc = 0 (given
the 16^3 grid for ker D; at Mc > 0 only at the tested points), the
opposite hands of the cell copies, the triplet structure of the X and M nodes under the turn, the far-wall mirror (A-T2).
Supplied: the Wilson-type kernel and its 4-component sites; the choice of B/2 and eps in the cell-slab layer hop and of
CL-1's (1 - s) R_e as the copy mass term; the grids. Not shown: a Floquet circuit version of the cell slab, whether
the cell slab's (1 - s) R_e gap closing at large Mc is the same as CL-1's 'partner gapped while MN < 2 eps' condition,
anything interacting or gauged.
