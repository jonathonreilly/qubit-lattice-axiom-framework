---
claim_id: the_composite_two_cell_light_label_makes_the_corner_stabilizers_reducible_but_the_light_floquet_winding_forces_the_mirror_to_carry_the_opposite_chirality_bounded_theorem_note_2026-10-23
claim_type: bounded_theorem
claim_scope: "Free-band, symmetry-level test of escape 1 of the corner-stabilizer no-go. The light label is defined on a doubled cell (2x2x2 CL-1 cells = a 4^3 block) by folding FREEZE's composite light label. The rule keeps the 12 tetrahedral rotations about the block centre (and, as a control, about a cell centre) and the doubled translations. Exact (Schur, finite group): every doubled-zone corner stabilizer acts reducibly on the light space. At the zone centre, the Gamma light Weyl's 2T irrep appears exactly once more, in one X combination, and the other two X irreps are distinct with no light partner; the same holds at pi for R and M. Exact (topology, any cell size, any walk-invariant splitting): the Floquet 3D winding W3 is additive over sectors, vanishes on any sector gapped at one quasienergy, and equals minus the net node chirality at 0 and at pi. Finite diagnostic: W3(light) = -2 and W3(mirror) = +2 on FREEZE. Not covered: interacting gapping (the Floquet anomaly is cited, not proven), and labels that are not walk-invariant sectors."
upstream_dependencies:
  - minimal_axioms
  - candidate_laws
  - the_corner_stabilizer_forces_a_scalar_light_block_at_x_and_m_so_no_rotation_covariant_freeze_deformation_gaps_the_light_partners_light_light_bounded_theorem_note_2026-10-23
  - the_composite_twist_walk_is_a_five_layer_cube_local_circuit_and_freezing_one_copy_leaves_one_l_and_one_r_per_node_bounded_theorem_note_2026-10-23
runner: scripts/the_composite_two_cell_light_label_makes_the_corner_stabilizers_reducible_but_the_light_floquet_winding_forces_the_mirror_to_carry_the_opposite_chirality_2026_10_23.py
---

# The composite two-cell light label makes the corner stabilizers reducible, but the light Floquet winding forces the mirror to carry the opposite chirality

Claim type: bounded_theorem (two exact statements plus one finite diagnostic).
Runner: runner.py, TOTAL: PASS=4 FAIL=0, 1.2 s, 106 MB peak, 2.4 k characters of stdout. It was run through
scripts/runner_cache.execute_runner under a unique filename: status ok, exit 0. Axioms unchanged.

## Question

freeze-gapped-partners proved a single-cell obstruction. D2 lifts to Q8, which acts irreducibly on the light
spinor doublet, so the light block at X and M is scalar and the light partners cannot be gapped among light
modes. Escape 1 asks whether a composite two-cell light label avoids this, and if so, whether a covariant
cube-local light-light term can gap the extra partners while keeping only the K = 0 (and R) light Weyls.

## Construction

- Doubled cell = 2x2x2 CL-1 cells (a 4^3 block). Doubled translations only; the single-cell translation is now an
  internal symmetry that the label may break.
- Folding: the doubled-cell Bloch space at Q is the sum over the 8 cell momenta K = Q/2 + pi n, with n in {0,1}^3.
  It is 64-dimensional.
- Rotations act about the block centre c = (1/2,1/2,1/2) cells: x -> R x + (c - R c), with CL-1's site gauges V
  and the phase exp(-i K'.t_R). A cell-centre version is run as a control.
- The composite light label is the fold of FREEZE's tau3 = +1, Pi+ label (rank 16).

## A. Escape 1 moves the Schur wall (exact)

- A0. The folded walk and the label are covariant under the 12 rotations (residual 1e-14).
- A1. Commutant dimensions of the stabilizer on the light space, with the single-cell value equal to 1 for
  comparison:

  | point | stabilizer | commutant |
  |---|---|---|
  | Gamma_D | 2T | 24 |
  | X_D | D2 | 64 |
  | M_D | D2 | 64 |
  | R_D | 2T | 24 |

  Every value is greater than 1, so every stabilizer acts reducibly. Both rotation centres give the same numbers.
  - General reason: Q8's only spinorial irrep is the 2-dimensional one. Any light space of dimension 2m is m copies
    of it, and the light block at a D2 point is 1_2 (x) (m x m). For m >= 2, levels can split pairwise. The
    single-cell obstruction was m = 1.
- A2. The zone centre is where all of FREEZE's light nodes fold. The quasienergy-0 light space is Gamma plus the
  X-triplet, 8 dimensions. Its 2T commutant has dimension 6 = 4 + 1 + 1:
  - the X-triplet is three distinct 2-dimensional irreps (commutant 3);
  - exactly one of them is isomorphic to Gamma's irrep (intertwiner dimension 1).
  The same holds at pi for R plus the M-triplet.
  - Consequence (Schur): a T-covariant light-light term at the zone centre is block-diagonal by irrep. It can pair
    Gamma's Weyl (chirality -1) only with one X combination, which destroys the protected Weyl. The other two X
    irreps (+1 each) have no light partner at all. They can only be shifted, which by the earlier note's A2
    trichotomy leaves a node, a light Fermi surface, or a zero.
  - This is the multiplicity form of the old wall. Reducibility is necessary but not sufficient.

## B. What actually blocks: the light Floquet winding

These are exact statements, derived here, valid for any cell size and any walk-invariant light/rest splitting P.

- B-i (additivity). If [U, P] = 0, then U = (PUP + 1 - P)(P^perp U P^perp + P), a commuting product. W3 is additive
  under pointwise products, so W3(U) = W3(light) + W3(rest).
- B-ii (gap kills winding). If PUP has no eigenvalue exp(i e) anywhere on the torus, a branch cut at e gives a
  smooth Hermitian H with PUP = P exp(-iH) P. Then exp(-i t H) is a homotopy from the sector to 1, so the sector
  has W3 = 0.
  - Contrapositive: a sector with W3 != 0 is gapless at EVERY quasienergy at the free level.
- B-iii (node formula). Put the branch cut at 0, or at pi. The obstruction to a global log then localizes on the
  nodes at that quasienergy, which gives W3 = -n_0 = -n_pi in the runner's chirality convention.
  - The general node formula is derived as a localization argument; the runner checks it numerically.
  - Numerically: W3(light) = -2.0000 and W3(mirror) = +2.0000 on a 28^3 grid. The light block is never singular
    (smallest singular value 0.35). This matches the corner bookkeeping n_0 = n_pi = +2 (light) and -2 (mirror).
  - The total is 0, as a cube-local circuit requires.
- Consequences:
  - (a) Any light-light term (one that keeps the label invariant) conserves W3(light) = -2. The light sector
    therefore always keeps net chirality +2 at 0 and +2 at pi.
  - (b) The target light content is the Gamma Weyl at 0 and the R Weyl at pi, each -1, and nothing else. It has
    W3(light) = +1.
    - Light with only the Gamma Weyl (R absent) is impossible, because n_0 = n_pi is required.
  - (c) So any relabelling (on any doubled or larger cell) that reaches the target must move 3 units of winding.
    The complement then has W3 = -1. By B-ii it is gapless at every quasienergy and cannot be gapped by
    complement-only terms at the free level.
  - (d) Interacting level: a U(1) Floquet sector with nonzero W3 carries a quantized Floquet chiral-magnetic
    response. This is LITERATURE (Higashikawa-Nakagawa-Ueda 2019), cited and not used in a proof. It suggests
    that mirror-only SMG is anomalous. Not proven here.

## Answers

1. Is the doubled-zone corner stabilizer action reducible? YES at every corner (commutants 24, 64, 64, 24 against
   1 before). Exact.
2. Is there a covariant cube-local light-light term that gaps the partners and keeps only Gamma and R? NO, at the
   free level.
   - With the folded composite label, Schur leaves two X irreps (and two M irreps) without a light partner. The
     only pairing channel consumes the Gamma (respectively R) Weyl.
   - With any label, light-light terms conserve W3(light) = -2, which is incompatible with the target's +1.
3. Bookkeeping: light net chirality is +2 at 0 and +2 at pi (W3 = -2). Mirror is the opposite. The target needs
   W3(light) = +1.
   - Escape 1 cannot evade Nielsen-Ninomiya through a stand-alone light Floquet winding with a gappable mirror.
   - It can do so only if the mirror carries the opposite winding (W3 = -1), and that mirror is then gapless at
     every quasienergy.
4. Gate: below.

Verdict: NO-GO for escape 1 as a partner-gapping route (exact, bounded to free, walk-invariant sectors under T
and translation at any zoom).
- The Schur wall does move, but the real obstruction is the conserved light winding, and no zoom changes it.
- Walls move. What escapes this note:
  - (i) accept a nonzero-W3 mirror, and test whether a Floquet-anomalous mirror (gapless at all quasienergies)
    is physically acceptable, for example as a hidden sector;
  - (ii) labels that are not walk-invariant sectors, for example interaction-defined composites, where W3 is not
    defined;
  - (iii) the Golterman-Shamir zero route from the earlier note.

## Gate (candidate rule: "light label = composite two-cell (4^3-block) label, with a T-covariant light-light layer gapping the partners")

1. Numbers: none. Pass.
2. Named structure: none. It uses only cells, rotations, and labels already in FREEZE. Pass.
3. Prediction not built for: it predicts that the light sector keeps net chirality +2 at 0 and at pi (W3 = -2)
   whatever the light-light layer is. That contradicts the target content. The rule cannot deliver what it was
   proposed for. FAIL.
4. Axiom bent: none (cube-local, one mode per site; only the cell-scale translation is broken internally).

Result: FAIL. Not adopted.

## Smuggling review

- Supplied:
  - FREEZE and its labels;
  - CL-1's site gauges V;
  - T as the symmetry;
  - the block-centre rotation convention (cell-centre run as a control, with identical numbers);
  - the polar part of the light block as the light-sector diagnostic.
- Forced:
  - the reducibility numbers;
  - the 2T multiplicity pattern (6, 3, 1);
  - W3 additivity, the vanishing of W3 on a gapped sector, and W3 = -n_0 = -n_pi;
  - W3(light) = -2.
- Literature (cited, not used in a proof): the Floquet chiral magnetic effect.
- Not used: any measured number.
