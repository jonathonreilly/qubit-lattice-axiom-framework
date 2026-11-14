---
claim_id: the_composite_two_cell_light_label_makes_the_corner_stabilizers_reducible_but_the_light_floquet_winding_forces_the_mirror_to_carry_the_opposite_chirality_bounded_theorem_note_2026-10-23
claim_type: bounded_theorem
claim_scope: "Free-band, symmetry-level test of escape 1 of the corner-stabilizer no-go. The light label is defined on a doubled cell (2x2x2 CL-1 cells = a 4^3 block) by folding FREEZE's composite light label. The rule keeps the 12 tetrahedral rotations about the block centre (and, as a control, about a cell centre) and the doubled translations. Exact (Schur, finite group): every doubled-zone corner stabilizer acts reducibly on the light space. At the zone centre, the Gamma light Weyl's 2T irrep appears exactly once more, in one X combination, and the other two X irreps are distinct with no light partner; the same holds at pi for R and M. Exact (topology, any cell size, any walk-invariant splitting): the Floquet 3D winding W3 is additive over sectors, vanishes on any sector gapped at one quasienergy, and equals minus the net node chirality at 0 and at pi. FREEZE's light label is not walk-invariant (light-to-mirror-label block norm 2 sqrt2/3 at X; the Pi+ sector is invariant), so these sector statements do not apply to it. Finite diagnostic: the polar part of FREEZE's compressed light block, a map T^3 -> U(2), has degree W3 = -2 and the mirror-label map +2. Not covered: a walk-invariant light label carrying that winding, any transfer from the compressed-map degree to light or mirror spectra or to a mirror obstruction, interacting gapping (the Floquet anomaly is cited, not proven)."
upstream_dependencies:
  - minimal_axioms
  - candidate_laws
  - the_corner_stabilizer_forces_a_scalar_light_block_at_x_and_m_so_no_rotation_covariant_freeze_deformation_gaps_the_light_partners_light_light_bounded_theorem_note_2026-10-23
  - the_composite_twist_walk_is_a_five_layer_cube_local_circuit_and_freezing_one_copy_leaves_one_l_and_one_r_per_node_bounded_theorem_note_2026-10-23
runner: scripts/the_composite_two_cell_light_label_makes_the_corner_stabilizers_reducible_but_the_light_floquet_winding_forces_the_mirror_to_carry_the_opposite_chirality_2026_10_23.py
---

# The composite two-cell light label makes the corner stabilizers reducible; a walk-invariant light Floquet winding would force the mirror to carry the opposite chirality, and FREEZE's compressed light map has degree -2

Claim type: bounded_theorem (two exact statements plus one finite diagnostic).
Primary runner: `scripts/the_composite_two_cell_light_label_makes_the_corner_stabilizers_reducible_but_the_light_floquet_winding_forces_the_mirror_to_carry_the_opposite_chirality_2026_10_23.py`; cache `logs/runner-cache/the_composite_two_cell_light_label_makes_the_corner_stabilizers_reducible_but_the_light_floquet_winding_forces_the_mirror_to_carry_the_opposite_chirality_2026_10_23.txt`. Axioms unchanged.

Local labels (2026-11-14). "CL-1" is the source label for the supplied cube tick and its site gauges; it is not CL-1 of
the current [candidate-law register](CANDIDATE_LAWS.md) (a historical alias with zero premise weight).
freeze-gapped-partners is [#10030](THE_CORNER_STABILIZER_FORCES_A_SCALAR_LIGHT_BLOCK_AT_X_AND_M_SO_NO_ROTATION_COVARIANT_FREEZE_DEFORMATION_GAPS_THE_LIGHT_PARTNERS_LIGHT_LIGHT_BOUNDED_THEOREM_NOTE_2026-10-23.md).

Correction (2026-11-14, from the PR 10131 hold). FREEZE's light label is not an invariant subspace of the walk
(runner B0; at X the CTWIST mixing h1 - i h2 = -2 sqrt2/3 couples it to the mirror label). The B-i to B-iii
statements below hold for walk-invariant splittings and are kept. The measured W3 = -2 is the degree of the polar
part of a compressed block, not a sector winding, so consequences (a)-(c) and the verdict are narrowed.

## Question

freeze-gapped-partners proved a single-cell Schur statement. D2 lifts to Q8, which acts irreducibly on the light
spinor doublet, so the compressed light block at X and M is scalar and no T-covariant light-light term splits it. Escape 1 asks whether a composite two-cell light label avoids this, and if so, whether a covariant
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
- A2. The zone centre is where Gamma and the X-triplet fold (the points where FREEZE's polar-compressed light map has
  phase 0; R and the M-triplet, where it has phase pi, fold to R_D). The light-label space at Gamma plus the X-triplet
  has 8 dimensions. Its 2T commutant has dimension 6 = 4 + 1 + 1 (a representation statement, independent of the
  spectral reading):
  - the X-triplet is three distinct 2-dimensional irreps (commutant 3);
  - exactly one of them is isomorphic to Gamma's irrep (intertwiner dimension 1).
  The same holds at pi for R plus the M-triplet.
  - Consequence (Schur): a T-covariant light-light term at the zone centre is block-diagonal by irrep. It can pair
    Gamma's Weyl (chirality -1) only with one X combination, which destroys the protected Weyl. The other two X
    irreps (+1 each) have no light partner at all. They can only be shifted, which by the earlier note's A2
    trichotomy leaves a phase-0/pi point, a crossing surface or a singular compression of the polar-compressed
    map (a light node or Fermi surface only for a walk-invariant label).
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
  - Numerically, for FREEZE's polar-compressed maps (not walk-invariant sectors, runner B0): degree -2.0000 for the
    light-label map and +2.0000 for the mirror-label map on a 28^3 grid. The compression is never singular
    (smallest singular value 0.35). This matches the corner degree bookkeeping of those maps, +2 (light) and -2
    (mirror) at phase 0 and at pi.
  - The measured sum is 0. Additivity (B-i) does not apply to compressed blocks, so this sum is a measurement.
- Consequences, for a walk with a walk-invariant light label (none is constructed here):
  - (a) Any light-light term that keeps the label invariant conserves W3(light).
  - (b) The target light content is the Gamma Weyl at 0 and the R Weyl at pi, each -1, and nothing else. It has
    W3(light) = +1.
    - Light with only the Gamma Weyl (R absent) is impossible, because n_0 = n_pi is required.
  - (c) If such a walk had total W3 = 0, its complement would have W3 = -1, and by B-ii it would be gapless at every
    quasienergy and could not be gapped by complement-only terms at the free level.
  - For FREEZE itself: the compressed-map degree -2 is invariant under deformations that keep the compression
    invertible (homotopy), but it does not by itself fix the light spectrum, the mirror's chirality or a mirror
    obstruction. That transfer needs a hypothesis-preserving bridge, not supplied here.
  - (d) Interacting level: a U(1) Floquet sector with nonzero W3 carries a quantized Floquet chiral-magnetic
    response. This is LITERATURE (Higashikawa-Nakagawa-Ueda 2019), cited and not used in a proof. It suggests
    that mirror-only SMG is anomalous. Not proven here.

## Answers

1. Is the doubled-zone corner stabilizer action reducible? YES at every corner (commutants 24, 64, 64, 24 against
   1 before). Exact.
2. Is there a covariant cube-local light-light term that gaps the partners and keeps only Gamma and R? Not with the
   folded composite label at the free level (Schur, exact): Schur leaves two X irreps (and two M irreps) without a
   light partner, and the only pairing channel consumes the Gamma (respectively R) Weyl.
   - For a walk-invariant light label, light-light terms conserve W3(light), and a target W3 of +1 then fixes the
     complement's winding. FREEZE's label is not walk-invariant, so its -2 does not enter this argument.
3. Bookkeeping: FREEZE's polar-compressed light map has degree -2 (+2 at phase 0 and at pi); the mirror-label map is
   the opposite. For a walk-invariant light sector the target needs W3(light) = +1, and its complement would then
   carry W3 = -1 and be gapless at every quasienergy.
4. Gate: below.

Verdict (narrowed 2026-11-14): with the folded composite label, escape 1 fails as a partner-gapping route by Schur
multiplicity (exact, free level). The winding argument is exact for walk-invariant sectors under T and translation
at any zoom; FREEZE's light label is not one, so its compressed-map degree does not by itself establish a light or
mirror spectral obstruction.
- The Schur wall moves to a multiplicity wall.
- Walls move. What escapes this note:
  - (i) accept a nonzero-W3 mirror, and test whether a Floquet-anomalous mirror (gapless at all quasienergies)
    is physically acceptable, for example as a hidden sector;
  - (ii) labels that are not walk-invariant sectors, for example interaction-defined composites, where W3 is not
    defined;
  - (iii) the Golterman-Shamir zero route from the earlier note.

## Gate (candidate rule: "light label = composite two-cell (4^3-block) label, with a T-covariant light-light layer gapping the partners")

1. Numbers: none. Pass.
2. Named structure: none. It uses only cells, rotations, and labels already in FREEZE. Pass.
3. Prediction not built for: by Schur multiplicity the folded label leaves two X (and two M) irreps without a light
   partner whatever the light-light layer is, and the only pairing channel consumes the protected Weyl. The rule
   cannot deliver what it was proposed for. FAIL.
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
  - W3 additivity, the vanishing of W3 on a gapped sector, and W3 = -n_0 = -n_pi (walk-invariant sectors);
  - the compressed-map degree -2 (a finite diagnostic of a map, not a sector winding).
- Literature (cited, not used in a proof): the Floquet chiral magnetic effect.
- Not used: any measured number.
