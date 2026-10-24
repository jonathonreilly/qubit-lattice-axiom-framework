---
claim_id: the_cell_slab_cannot_put_its_mirror_in_the_other_copy_because_turn_axis_eigenvalue_flow_forces_q_mirror_equal_q_light_on_any_static_slab_bounded_theorem_note_2026-10-23
claim_type: bounded_theorem
claim_scope: "Free-field cell slab on CL-1's 2x2x2 cell (layer hop (B/2 + i eps)/2, copy mass (1 - s) R_e, Mc = 1, Ls = 32 or 40). (T1) At K = 0 the copy sign s commutes with every cell-built layer term, each copy is its own Shamir chain (r_+ = 1 - m, r_- = 1 + Mc - m), and the far boundary can hold copy s only with the hand opposite to that copy's near-wall hand: s+ with -1 or s- with +1, never s- with -1. (a) A layer mass stepping (sharp or tanh) from the (0, Mc) window [s+, q 2] to the (2, 2 + Mc) window [s-, q 1] puts s- (q 1) on the far wall with the light's hand +1, and both mirrors s+ (-1, q 2) and s- (-1, q 1) on the interior interface; it crosses the bulk gap closings m = Mc and m = 2 and is a chosen profile. (b) A hop s A keeps the wall content; a turn-commuting copy-flipping hop has rank <= 4 < 8, so no turn-covariant copy flip exists. (T2) On any static (Hamiltonian) turn-symmetric slab whose only E = 0 crossings on the turn axis are the K = 0 wall Weyls, the turn-sector eigenvalue flow forces q_mirror = q_light for every N_f. The families-mod-3 mod 3 is therefore not recovered on any realised slab. Not covered: interactions, gauge fields, Floquet (circuit) slabs, slabs with extra axis crossings, multi-Weyl nodes."
upstream_dependencies:
  - minimal_axioms
  - candidate_laws
  - the_slab_mirror_sits_on_the_light_copy_so_the_turn_anomaly_allows_every_family_count_and_the_number_conserving_spin12_term_cannot_gap_the_mirror_bounded_theorem_note_2026-10-23
  - the_cube_cell_slab_wall_holds_at_most_two_opposite_handed_copies_so_families_are_not_wall_nodes_while_the_supplied_wilson_kernel_gives_a_turn_triplet_only_in_an_unforced_window_bounded_theorem_note_2026-10-23
  - three_fold_turn_anomaly_gives_family_count_zero_mod_three_under_a_supplied_mirror_term_bounded_theorem_note_2026-10-21
  - the_composite_twist_walk_is_a_five_layer_cube_local_circuit_and_freezing_one_copy_leaves_one_l_and_one_r_per_node_bounded_theorem_note_2026-10-23
runner: scripts/the_cell_slab_cannot_put_its_mirror_in_the_other_copy_because_turn_axis_eigenvalue_flow_forces_q_mirror_equal_q_light_on_any_static_slab_2026_10_23.py
---

# The cell slab cannot put its mirror in the other copy: turn-axis eigenvalue flow forces q_mirror = q_light on any static slab

Claim type: bounded_theorem. Exact statements are labelled [T], finite diagnostics [F] and readings [S].
Runner: runner.py, TOTAL: PASS=14 FAIL=0, 0.7 s, 51 MB peak, 4.6 k characters of stdout, seeded, AUDIT_TIMEOUT_SEC = 120.
It was tested under a unique filename (scratch/copy_flip_slab_test_run.py). Axioms unchanged. No rule adopted.

## Question

anomaly-family-count found that on the adopted cell slab in its one-copy window both walls hold the s = +1 copy
(q_mirror = q_light = 2), so the cube-turn anomaly gives no family-count constraint. The mod 3 of families-mod-3 needs the
mirror in the other copy (s = -1, q = 1), as in the Floquet FREEZE walk. Is there a slab, with the same cell and layer hop,
whose near wall holds s+ (q 2, hand +1) and whose far wall holds s- (q 1) as the mirror (hand -1), with a gapped bulk and
no fitting? Candidates: (a) a layer-dependent mass crossing between the two one-copy windows; (b) a layer hop that carries
or flips the copy.

Repo first. This builds on, and narrows:
- anomaly-family-count (q_mirror = q_light in the one-copy window; the bookkeeping and Omega twist selection);
- wall-families C (the windows (0, Mc), (Mc, 2), (2, 2 + Mc); opposite hands of the copies; turn charges differ by w^2);
- families-mod-3 (the index N (q_l - q_m) = 0 mod 3);
- twist-local-single (FREEZE: 1L with q = 2 and 1R with q = 1 per node, a circuit).

A git grep of origin/main for "eigenvalue flow", "copy flip" and "copy-flip" in docs and scripts found no prior note.

## Pass criteria

Written before the runner (criteria_pre_run.txt; three short scratch explorations preceded them and are disclosed there).
PASS needed: P1 walls in different copies with opposite hands; P2 no interior gapless state; P3 the construction forced;
P4 allowed N_f = {3, 6, 9}. Predicted verdict FAIL at P1, P2, P3. It FAILED, as predicted; every line matched its prediction.

## A. The copy sign is exact at K = 0

- A1 [T]. At K = 0, s commutes with R_e, R_o, eps and the turn (defect 6e-18). Every cell-built layer term (any m(l),
  Mc(l), any hop made of R_e, R_o, eps, s) therefore keeps s at K = 0. At generic K it does not ([s, R_o] = 0.33): the copy
  is a K = 0 label, which is where the wall Weyls sit.
- A2 [T]. Turn spectra on the copies at K = 0: s+ {1, 1, w, w}, s- {1, 1, w^2, w^2}. A wall pair of copy charge q has turn
  eigenvalues {w^(q+1), w^(q+2)}: q = 2 is {1, w}, q = 1 is {w^2, 1}.

## B. Candidate (a): a layer mass crossing between the one-copy windows

- B1 [T]/[F]. Uniform windows (Mc = 1, Ls = 32). In (0, Mc) both walls hold s+ (q 2): near +1, far -1. In (2, 2 + Mc) both
  walls hold s- (q 1): near -1, far +1. Each window holds ONE copy, on both walls.
- B2 [F]. Both end phases have bulk gap 0.52. Going from one to the other crosses the bulk gap closings m = Mc (the s- ratio
  reaches 1) and m = 2 (the s+ ratio reaches -1); the K = 0 gap is 1e-16 at both.
- B3 [T]/[F]. Sharp step 0.5 -> 2.5. Near wall s+ (+1, q 2). Far wall s- (q 1) but with hand +1, the SAME hand as the light:
  a second light Weyl, not the mirror. The interior interface holds BOTH mirrors, s+ (-1, q 2) and s- (-1, q 1).
- B4 [F]. A smooth profile m = 1.5 + tanh((l - 19.5)/3), Ls = 40, gives the same four Weyls. Smoothing does not remove the
  interface modes.
- B5 [T]. Exact reason. At K = 0 each copy is its own Shamir chain with ratio r_+ = 1 - m or r_- = 1 + Mc - m. Its pair
  exists only if F_s(end) << 0, where F_s is the cumulative log|r_s|. The hand-h_s member sits at the maximum of F_s and the
  hand -h_s member at its minimum, with h_+ = +1 and h_- = -1. The left boundary condition fixes which member can sit at
  l = 0. So the far boundary holds copy s only with hand -h_s: s+ with -1, or s- with +1. It can never hold s- with -1.
  Every copy is vector-like on its own, so the light's opposite-hand partner is always in the light's copy.
- So (a) puts the two walls in different copies only with the SAME hand. It doubles the light content (q 2 and q 1 lights
  per family) and puts the mirrors in the interior. The profile is chosen (two masses in two windows): FAIL at P1, P2, P3.

## C. Candidate (b): the layer hop and the copy

- C1 [T]/[F]. A hop s A (the hop carries the copy sign) is, at K = 0, the gauge (-1)^l on the s- copy. |r| is unchanged, and
  every window keeps the same copy on both walls (checked at m = 0.5 and 1.5).
- C2 [T]. A hop that FLIPS the copy (anticommutes with s) and commutes with the turn can only connect the eigenvalue-1
  sectors (A2): rank <= 4 < 8 (max over 20 random draws: 4). No turn-covariant copy flip exists. This is the "turn charges
  differ by w^2" fact of wall-families C5.
- C3 [F]. Adding such a turn-commuting copy-mixing hop (g = 0.3) splits the K = 0 pairs. The surviving K = 0 zero modes on
  both walls lie in the w sector, which is s+ only. Neither wall becomes a q = 1 pair {1, w^2}.

## D. Theorem: turn-axis eigenvalue flow

On the turn axis K = kappa (1, 1, 1) the turn is a symmetry, so the slab's bands carry turn eigenvalues 1, w, w^2.
- D1 [F]. The negative-energy count per turn sector is the same on both sides of K = 0 and all around the axis loop:
  [64, 32, 32] for the m = 0.5 slab and the step slab. The axis carries no crossing other than the K = 0 wall Weyls.
- D2 [T]/[F]. A Weyl pair with copy charge q and hand h moves one state between sectors as it passes K = 0. The flow is
  h (w^(q+2) - w^(q+1)) in the group ring Z[Z3]. On a turn-symmetric Weyl, the velocity along the axis has the sign of
  det v, and the axis states are the spin-1/2 turn eigenstates. Checked on all 8 wall pairs of B1 and B3, with one global
  sign.
- D3 [T]. Suppose a static slab's only axis crossings are N_f near pairs (q_l, +1) and N_f far pairs (q_m, -1). Then the K = 0
  flow must vanish, and it vanishes iff q_m = q_l, for EVERY N_f (Z[Z3] is torsion-free, checked for N_f = 1..9). The three
  single-pair flows sum to 0, so a copy-flipped mirror needs extra axis Weyls (one per charge, with an off-axis turn orbit
  for Nielsen-Ninomiya), which is more light content.
- D4 [S]. FREEZE (1L q 2, 1R q 1 per node) is a Floquet walk. Its quasi-energy has a second gap at pi, which can absorb the
  flow, so D3 does not apply to it. That is the reading of how FREEZE evades D3; it is not checked here.

## E. Bookkeeping

- E1 [T]. Using the families-mod-3 index with Omega twist selection (single copy: t = 0; cross-copy B(s+) B(s-): t1 + t2 = 0):
  - uniform slab (light 2 | mirror 2): every N_f in 1..9;
  - step slab (lights {2, 1} | mirrors {2, 1}, cross-copy Omega kept at k = 0): every N_f;
  - only the copy-flip pair (2 | 1) gives {3, 6, 9}, and no static slab realises it.
- Light-copy turn charge: on the uniform slab all families share q = 2 (anomaly-family-count D4 unchanged). The step slab
  gives each family two light copies with different charges (2 and 1), which conflicts with CL-1's one light copy.

## Answer

1. No. On CL-1's cell slab, no layer profile and no turn-covariant layer hop puts the mirror in the other copy.
   - (a) The two-window crossing gives a far wall in the other copy, but with the light's hand, plus both mirrors on an
     interior interface. It crosses two bulk gap closings and is a chosen two-mass profile, not the generic slab.
   - (b) A copy-carrying hop changes nothing. A copy-flipping hop cannot commute with the turn.
2. The obstruction is general (D3). On any static turn-symmetric slab whose only axis crossings are the wall Weyls,
   q_mirror = q_light for every N_f. The anomaly-family-count result "every N_f passes" therefore holds for every static
   slab of that kind, not just the one-copy window.
3. The mod 3 is not recovered. Any static realisation of q_mirror != q_light needs extra axis Weyls. The remaining routes
   are a circuit (Floquet) slab with a second quasi-energy gap, as FREEZE does, or extra axis nodes from a rule. Neither is
   adopted.

## Gate (anti-smuggling)

No rule is proposed. Choosing the step profile, or adding a copy-mixing hop to obtain 3, would be a fitted choice and would
FAIL item 1. UNTESTED prediction: a Floquet cell slab built from FREEZE-type layers can carry q_mirror != q_light on its
walls only if its pi gap hosts a compensating flow h (w^(q+2) - w^(q+1)).

## Smuggling review

Supplied:
- the cell-slab kernel;
- the Hamiltonian (not circuit) form;
- (m, Mc, Ls);
- the step and tanh profiles;
- the random copy-mixing hop;
- free fields.

Cited:
- the families-mod-3 index and Omega selection (anomaly-family-count);
- Nielsen-Ninomiya.

Forced:
- the K = 0 copy conservation;
- the per-copy argmax/argmin rule;
- the rank bound on turn-covariant copy flips;
- the axis flow formula and the theorem q_mirror = q_light;
- the all-N bookkeeping on realised slabs.

Not shown:
- interacting or gauged slabs;
- multi-Weyl nodes;
- slabs with extra axis crossings;
- the Floquet extension.
