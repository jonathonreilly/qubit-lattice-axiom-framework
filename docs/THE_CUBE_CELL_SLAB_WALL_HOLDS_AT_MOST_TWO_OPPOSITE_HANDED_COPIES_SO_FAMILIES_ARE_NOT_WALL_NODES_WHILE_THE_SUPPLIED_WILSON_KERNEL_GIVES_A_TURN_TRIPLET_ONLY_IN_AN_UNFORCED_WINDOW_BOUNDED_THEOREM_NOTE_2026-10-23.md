---
claim_id: the_cube_cell_slab_wall_holds_at_most_two_opposite_handed_copies_so_families_are_not_wall_nodes_while_the_supplied_wilson_kernel_gives_a_turn_triplet_only_in_an_unforced_window_bounded_theorem_note_2026-10-23
claim_type: bounded_theorem
claim_scope: "Free-field wall spectra of two domain-wall slabs (layer index as a role-block coordinate, open layer chain, Shamir-type layer hop). (W) The adopted tick-form slab (chiral-tick-form: Wilson-type kernel, 4 components per Z^3 site): near-wall Weyl nodes sit at the zone corners with n pi-components exactly when 2n < m < 2n + 2 (zero-mode ratio 1 - m + 2n); windows (0,2), (2,4), (4,6), (6,8) give 1 (G), 3 (X), 3 (M), 1 (R) nodes; within a window all nodes have one hand, the hand alternates as (-1)^n, and the far wall carries the opposite total; on the 3-node walls the three-fold turn about (111) acts as the single node's spinor pair times {1, w, w^2}, a turn triplet. (C) The same slab built on CL-1's own cell (2x2x2 cube cell, 8 one-mode sites, face phase -1, both tilings): D = R_e - R_o, B = R_e + R_o and eps = (-1)^(x+y+z) anticommute exactly with D^2 + B^2 = 4; D vanishes only at K = 0, on two 4-component copies s = +1, -1; with CL-1's copy operator (1 - s) R_e (copy mass Mc <= 1) the near wall holds the s = +1 copy for 0 < m < 2 and the s = -1 copy for Mc < m < Mc + 2, never more than two; the two copies have OPPOSITE hands, so the two-copy window is vector-like; their turn charges differ by a nontrivial cube root; at Mc = 3 the bulk is gapless. Nothing in CL-1 fixes the layer mass window. Not covered: interactions, gauge fields, the far-wall fate, a Floquet (circuit) version of the cell slab, a derivation of the Wilson kernel from the cell."
upstream_dependencies:
  - minimal_axioms
  - candidate_laws
  - a_domain_wall_tick_with_the_layer_direction_as_space_puts_one_weyl_cone_on_each_wall_but_the_circuit_forces_the_mirror_onto_the_far_wall_bounded_theorem_note_2026-10-23
  - the_overlap_of_the_cube_walk_euclidean_kernel_gives_exact_ginsparg_wilson_chirality_without_doublers_but_its_chiral_projector_is_not_a_walk_sector_bounded_theorem_note_2026-10-23
runner: scripts/the_cube_cell_slab_wall_holds_at_most_two_opposite_handed_copies_so_families_are_not_wall_nodes_while_the_supplied_wilson_kernel_gives_a_turn_triplet_only_in_an_unforced_window_2026_10_23.py
---

# The cube-cell slab wall holds at most two opposite-handed copies, so families are not wall nodes; the supplied Wilson kernel gives a turn triplet only in an unforced window

Claim type: bounded_theorem (exact zero-mode recursions and cell algebra; labelled finite diagnostics; the domain-wall
construction and the Wilson-kernel identification are supplied and cited).
Runner: runner.py, TOTAL: PASS=12 FAIL=0, 17 s, 59 MB peak, 4.7 k characters; run under a unique filename.
Axioms unchanged. No rule adopted.

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

## W. Adopted slab (Wilson-type kernel, 4 components per site)

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
A = (B/2 + i eps)/2, with CL-1's own copy operator (1 - s) R_e as the copy-dependent mass. D vanishes only at K = 0
(next-smallest |D| on 16^3 is 0.23), on all 8 modes: two 4-component copies (s = +1: 4, s = -1: 4). There are no X, M or
R points in this cell: the 8-site cell has no Wilson-type corner doublers to supply a triplet.
Finite diagnostics (Ls = 24):
- C2 for Mc = 0.8 and 1: near-wall copies = s+ iff 0 < m < 2, s- iff Mc < m < Mc + 2 (layer mass m - Mc); all six points
  gapped (0.37 to 0.60). Windows: (0, Mc) one copy (s+), (Mc, 2) two, (2, 2 + Mc) one (s-).
- C2b the pre-set 'gapped at Mc = 3' FAILED: at Mc = 3 the bulk is gapless (1e-16 on the 8^4 grid), because (1 - s) R_e
  does not anticommute with D. A separate large-copy-mass s- window is not a gapped phase. Recorded as a result.
- C3 no wall state elsewhere in the block zone: at most 2 wall copies per field.
- C4 a lone s+ copy has hand +1, a lone s- copy -1 (far wall opposite in each case): the copies have OPPOSITE hands.
- C4b in the two-copy window the near wall has net chirality 0 (s+ +1, s- -1, no first-order mixing): a vector-like
  pair, not two families.
- C5 the turn (site-phase lift, keeps both tilings, s and eps; defect 0) acts on each copy as a spin-1/2 pair times a copy
  phase; the s- copy's phase is the s+ copy's times w^2 (dq = 2): charges {q, q + 2}, never a triplet.

## Answer

On CL-1's own cell the wall carries exactly ONE Weyl copy per field in every gapped chiral window, (0, Mc) [s = +1] or
(2, 2 + Mc) [s = -1], and a vector-like pair in (Mc, 2). There is no window with three. The turn triplet exists only for
the supplied Wilson-type kernel (4 components per site = 32 modes per 2x2x2 cell, four times CL-1's 8), and only for
m in (2,4) or (4,6). Nothing in CL-1 or the tick-form clause selects that window; the adopted m = 0.6 is in (0,2). The
copy mass's role in CL-1 (making s = +1 the one light copy) agrees with the (0, Mc) window, which is a reason, though not
forced, for the low window.

Where families must come from, if not wall nodes: (a) extra layers do not add copies (Ls changes only the |r|^Ls overlap);
(b) no wall-bound states at other momenta on the cell slab (C3); (c) so it is the cell content: either a 4-mode-per-site
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

Forced: the window conditions (exact recursion), the cell algebra (D, B, eps), the two-copy limit of the cell, the
opposite hands of the cell copies, the triplet structure of the X and M nodes under the turn, the far-wall mirror (A-T2).
Supplied: the Wilson-type kernel and its 4-component sites; the choice of B/2 and eps in the cell-slab layer hop and of
CL-1's (1 - s) R_e as the copy mass term; the grids. Not shown: a Floquet circuit version of the cell slab, whether
the cell slab's (1 - s) R_e gap closing at large Mc is the same as CL-1's 'partner gapped while MN < 2 eps' condition,
anything interacting or gauged.
