---
claim_id: the_corner_stabilizer_forces_a_scalar_light_block_at_x_and_m_so_no_rotation_covariant_freeze_deformation_gaps_the_light_partners_light_light_bounded_theorem_note_2026-10-23
claim_type: bounded_theorem
claim_scope: "Any cell walk covariant under the 12 tetrahedral rotations T (CL-1's site gauges), on the FREEZE cell content (light label tau3 = +1 on Pi+, a spinor doublet). Exact: X and M are fixed mod 2 pi by the D2 subgroup of T, whose lift Q8 acts irreducibly on the light doublet, so the compressed light-labelled block P_L U P_L of the walk (and of any T- and cell-translation-symmetric light Green's function) is a scalar at X and M, and no T-covariant light-light term splits the X level. Corollary (exact, continuity), for the polar part W(K) of the compressed light block as a map T^3 -> U(2): with a node of W at K = 0 at phase 0, W has a phase-0 or phase-pi point at X, a crossing surface, or the compression is singular. This is a statement about the polar-compressed map; it is a statement about the walk's light spectrum only when the light label is walk-invariant. FREEZE's light label is not walk-invariant: at X = (pi,0,0) the CTWIST mixing is h1 - i h2 = -2 sqrt2/3, the active block has eigenphases +-acos(1/3), and X is not a quasienergy-0 node of FREEZE, although the compression is I/3 with polar part I (negative result kept). Finite diagnostics: 3 random T-covariant deformations; a designed light-light scalar layer; degree bookkeeping of FREEZE's polar-compressed light map (net +2 at phase 0 and at pi per family). Not covered: a bridge from the compressed map to physical light or mirror spectra, Fermi surfaces or Green-function zeros; translation-breaking (zoomed) rules beyond the Schur remark in section D; the infinite-lattice interacting phase."
upstream_dependencies:
  - minimal_axioms
  - candidate_laws
  - the_composite_twist_walk_is_a_five_layer_cube_local_circuit_and_freezing_one_copy_leaves_one_l_and_one_r_per_node_bounded_theorem_note_2026-10-23
  - the_label_selective_charge_four_mirror_term_on_the_freeze_walk_first_exists_at_four_families_and_frees_the_light_partners_bounded_theorem_note_2026-10-23
runner: scripts/the_corner_stabilizer_forces_a_scalar_light_block_at_x_and_m_so_no_rotation_covariant_freeze_deformation_gaps_the_light_partners_light_light_2026_10_23.py
---

# The corner stabilizer forces a scalar light-labelled block at X and M, so no rotation-covariant light-light term splits it; the spectral no-go holds only for a walk-invariant light label

Claim type: bounded_theorem (one exact Schur statement plus an exact continuity corollary about the polar-compressed
map; numerics labelled). Primary runner: `scripts/the_corner_stabilizer_forces_a_scalar_light_block_at_x_and_m_so_no_rotation_covariant_freeze_deformation_gaps_the_light_partners_light_light_2026_10_23.py`; cache `logs/runner-cache/the_corner_stabilizer_forces_a_scalar_light_block_at_x_and_m_so_no_rotation_covariant_freeze_deformation_gaps_the_light_partners_light_light_2026_10_23.txt`. Axioms unchanged.

Local labels (2026-11-14). "CL-1" is the source label for the supplied cube tick and its site gauges V; it is not CL-1
of the current [candidate-law register](CANDIDATE_LAWS.md) (a historical alias with zero premise weight).
freeze-mirror-smg (#10031) is recorded only in the consolidation's source map; its results quoted here are historical
reported results, unverified here.

Correction (2026-11-14, from the PR 10131 hold). The earlier text read the polar part of the compressed light block
as the light walk's spectrum ("X sits at quasienergy 0"). That is wrong for FREEZE, whose light label is not an
invariant subspace (A3 below). The Schur statement A1 stands. A2 and its consequences are now stated for the
polar-compressed map, and for walks with a walk-invariant light label.

## Question

freeze-mirror-smg asked for a T-covariant, cube-local FREEZE variant whose light-labelled projection has no
nodes at X and M, so that the X/M light partners are gapped among light modes and a mirror-only charge-4
term could then gap the mirror without releasing them.

## A. Theorem (exact)

- A1. X = (pi,0,0) and M = (pi,pi,0) (and their T-images) are fixed mod 2 pi by the four diagonal rotations
  D2 of T. The light label is V-invariant, and D2 lifts to Q8 on it, with a commutant of dimension 1
  (irreducible). For any T-covariant U, V_R U(X) V_R^+ = U(R X) = U(X), so P_L U(X) P_L is a scalar. The
  same holds at M.
  - The A4 characters w^q are trivial on D2, so this holds for either label and any family count.
  - It uses only T-covariance and cell-scale translation. It does not depend on depth, range, light-mirror
    mixing, or Pi+/Pi- mixing.
- A2 (corollary, continuity; narrowed 2026-11-14). Let W(K) be the polar part of the compressed light block
  P_L U(K) P_L, defined where the compression is invertible: a T-covariant map T^3 -> U(2). Suppose W has a node
  at K = 0 at phase 0 and is scalar at X. Its two eigenphases rise and fall from 0 and coincide at X.
  - An eigenphase gapped away from isolated nodes stays on one side of 0 (and of pi). Two such can coincide only at
    0 or pi.
  - So one of three things happens: (i) W(X) has phase 0 or pi; (ii) an eigenphase of W crosses 0 or pi along a
    surface; (iii) the compression P_L U P_L is singular somewhere on the path.
  - The same argument holds at M relative to R at phase pi.
  - This is a statement about the map W. It is a statement about the walk's quasienergies only if the light label
    is walk-invariant, [U, P_L] = 0: then the compression is the restriction and W is the light walk itself, and
    (i)-(ii) are a node or a light Fermi surface. A zero of the compression is not identified with a
    Golterman-Shamir zero of a Green's function; that identification would need its own proof.
- A3 (negative result for the earlier spectral reading, kept with its witness). FREEZE's light label is NOT
  walk-invariant. At X = (pi,0,0) the CTWIST formula gives f = 1/3, g = 0 and h1 - i h2 = (sqrt2/3)(-1 + wbar + w)
  = -2 sqrt2/3. The active Pi+ block therefore has eigenvalues 1/3 +- i sqrt(8/9), with phases +-acos(1/3) = +-1.231,
  and the frozen block +-pi/2: X is not a quasienergy-0 node of FREEZE. The compression is I/3 with polar part I
  only because compression discards the mixing (runner A3: light-to-mirror-label block norm 0.9428 = 2 sqrt2/3;
  control: at K = 0 the label is invariant and the walk has its quasienergy-0 node).
- Therefore, exactly: no T-covariant light-light term splits the X level (a 2x2 term that commutes with Q8 is a
  scalar). For a T- and translation-symmetric walk with a walk-invariant light label, the light sector cannot
  have only the K = 0 and R Weyls. For FREEZE and its deformations, whose light label is not walk-invariant,
  the corresponding statement holds for the polar-compressed map W only.

## B. Finite diagnostics

- B1. 3 random T-covariant deformations U_F exp(i H_cov) (H_cov a rotation-twirled random Bloch Hamiltonian on
  all 8 modes). Covariance holds to 4e-15, and the light block at X, M is scalar to 2e-15. The phase of the
  compressed block at X is generic (-1.38, -0.61, 1.32), not 0 or pi, so by A2 the polar-compressed maps of those
  cases have crossing surfaces (statements about the compressed map, not the walk spectrum).
- B2. The designed light-light layer exp(i a phi(K) tau3 Pi+), with phi = 3 - sum cos K_i cos K_j, is
  T-invariant, vanishes at K = 0 and R, and equals 4 at X and M.
  - The walk at K = 0 and R is untouched (U = U_F exactly there).
  - The compressed light block at X stays scalar and its phase moves to 4a.
  - The lower eigenphase of the polar-compressed light map crosses 0 on the line 0 -> X at s = 0.919 (a = 0.1)
    and at s = 0.691 (a = 0.25). For a walk-invariant label that crossing would be a light Fermi surface; here it
    is a crossing of the compressed map.

## C. Degree bookkeeping of the polar-compressed light map of FREEZE (matches freeze-mirror-smg C2)

These are local degrees of the polar-compressed maps at the corners (phase 0 or pi of the map), not chiralities of
walk nodes (A3).
- Light-label map: K = 0 and R carry -1; the 3 X (phase 0) and the 3 M (phase pi) carry +1. Net +2 at 0 and +2 at pi.
- Mirror-label map: exactly opposite (-2, -2); the measured sum is 0.
- Conditional on a walk-invariant light sector: its target content, the K = 0 and R Weyls only, would be net -1 at
  0 and -1 at pi, a nonzero Floquet 3D winding.
  - It is not Nielsen-Ninomiya consistent as a stand-alone static sector.
  - It is allowed only as a Floquet-anomalous sector, which is a LITERATURE fact (Floquet chiral magnetic
    effect, Higashikawa-Nakagawa-Ueda 2019) and is not used here.
  - It would need the mirror to carry the opposite winding, so the mirror cannot then be gapped trivially by
    mirror-only terms.
- The Spin-Z4 count of the gapped mirror set is unchanged from freeze-mirror-smg: 2 N_f mod 16 (8 at
  N_f = 4).
- A1 forbids the target at the free level regardless of this bookkeeping.

## D. Zoom remark (exact Schur, derived in this note, not run)

On a doubled superlattice (translation broken from 2 to 4 sites), the corners fold to the superlattice
centre, where the full binary tetrahedral group 2T acts. The irreps are:
- light at K = 0: s(x)w (-1);
- light X-triplet: s(x)w (x) {1, omega, omega-bar} = {s(x)w, s(x)w^2, s} (+1 each).

The signs are the corner degrees of the polar-compressed map (C), not chiralities of FREEZE's spectrum (A3). For a
walk with a walk-invariant light label carrying nodes with these signs, a light-light mass would need the same irrep
with opposite sign. That gives:
- Only s(x)w can pair, and that pairs the K = 0 light node with an X combination, which removes it.
- s(x)w^2 and s have no light partner. Their only same-irrep, opposite-sign partners are mirror modes.

Under that hypothesis zooming does not give light-light partner gapping either (at the corner fixed point; nodes
moved off the fixed point are not covered). For FREEZE, whose light label is not walk-invariant, this is a statement
about irreps of label spaces only (narrowed 2026-11-14 with #10042, second hold R2).

## Answers

1. A T-covariant, translation-symmetric walk whose light label is walk-invariant cannot have light nodes only at
   K = 0 and R (A1-A2, exact for any depth or range). For FREEZE-type walks, whose light label is not
   walk-invariant (A3), this holds for the polar-compressed map only; the walk-spectrum statement is not shown.
2. After any T- and translation-symmetric mirror gapping, the light Green's function block is still scalar at X
   and M (A1, exact). Whether the partners then come back as poles, a pole surface or zeros needs a bridge from the
   compressed map, or from the Green's function block, to the full spectrum; that bridge is not supplied here. The
   release found in freeze-mirror-smg (B4b) is a historical reported result, not recomputed here, and this note
   does not show that it is generic.
3. Polar-compressed light map of FREEZE: net degree +2 at phase 0 and +2 at pi per family. For a walk-invariant light
   sector, the target content would be a Floquet winding of -1 that a mirror-only gap cannot cancel.

Verdict (narrowed 2026-11-14): exact Schur statement for every T-covariant cell-translation-invariant rule (the
light-labelled block is scalar at X and M; no T-covariant light-light term splits it); spectral no-go only for
walk-invariant light labels; for FREEZE, a statement about the polar-compressed map. The Schur obstruction is the Q8
stabilizer of the zone-boundary corners acting irreducibly on the light spinor, not the specific FREEZE gates.
Walls move: what escapes the theorem is a rule that breaks either (a) the D2 part of the corner stabilizer on
the light doublet, for example a light label that is not a spinor doublet, as in a composite multi-cell label,
or (b) the cell-scale translation in a way that moves the partners off fixed points. Neither is tested here.

## Gate (the candidate rule "add a T-covariant light-light layer that gaps the X/M light partners")

1. Numbers: none (a free). Pass.
2. Named structure: none. Pass.
3. Prediction not built for: no T-covariant light-light term splits the X level (A1). In its tested instance (B2)
   the polar-compressed light map acquires a crossing surface. FAIL.
4. Comparison with the current axioms (rematched 2026-11-14): cell-local, one mode per site on Z^3, so the Lattice
   and Qubit axioms are not departed from; the walk and the layer are supplied, and no axiom states an update rule.

Result: FAIL. Not adopted. The no-go itself is the deliverable.

## Smuggling review

- Supplied:
  - FREEZE and its labels;
  - CL-1's site gauges V;
  - the choice of T (rotations only) as the symmetry;
  - the designed phi in B2;
  - the polar part and the zero-frequency Green's function as the "light sector" diagnostics.
- Forced:
  - the D2 stabilizer of X and M;
  - Q8 irreducibility on the light doublet;
  - the scalar light block;
  - the node / crossing / singular-compression trichotomy for the polar-compressed map;
  - the corner degree signs and the nets (+-2) of that map.
- Literature, cited and not used in a proof: the Floquet chiral magnetic effect; the Spin-Z4 Z16
  classification (via freeze-mirror-smg).
- Not used: any measured number.

## Next

- Test a rule in which the light label is not a single-cell spinor doublet, for example a composite two-cell
  label whose stabilizer at X acts reducibly. Or break D2 covariance on the light sector with a reason.
- Construct a walk-invariant light sector, or a bridge from the compressed map to the walk spectrum.
- Otherwise, test whether a light-propagator zero at X exists and is physically benign (the open Golterman-Shamir
  question); a zero of the compressed unitary block is not such a zero without proof.
