---
claim_id: the_corner_stabilizer_forces_a_scalar_light_block_at_x_and_m_so_no_rotation_covariant_freeze_deformation_gaps_the_light_partners_light_light_bounded_theorem_note_2026-10-23
claim_type: bounded_theorem
claim_scope: "Any cell walk covariant under the 12 tetrahedral rotations T (CL-1's site gauges), on the FREEZE cell content (light label tau3 = +1 on Pi+, a spinor doublet). Exact: X and M are fixed mod 2 pi by the D2 subgroup of T, whose lift Q8 acts irreducibly on the light doublet, so the light-labelled block of the walk (and of any T- and cell-translation-symmetric light Green's function) is a scalar at X and M. Consequence (exact, continuity): with a Weyl at K = 0 at quasienergy 0, the light-labelled sector is gapless at or around every X and M -- a node at quasienergy 0 or pi, a crossing surface, or a zero of the light block. No light-light partner mass exists. Finite diagnostics: 3 random T-covariant deformations; a designed light-light scalar layer; corner chirality bookkeeping of FREEZE (net +2 at 0 and at pi per family). Not covered: translation-breaking (zoomed) rules beyond the Schur remark in section D, and the infinite-lattice interacting phase."
upstream_dependencies:
  - minimal_axioms
  - candidate_laws
  - the_composite_twist_walk_is_a_five_layer_cube_local_circuit_and_freezing_one_copy_leaves_one_l_and_one_r_per_node_bounded_theorem_note_2026-10-23
  - the_label_selective_charge_four_mirror_term_on_the_freeze_walk_first_exists_at_four_families_and_frees_the_light_partners_bounded_theorem_note_2026-10-23
runner: scripts/the_corner_stabilizer_forces_a_scalar_light_block_at_x_and_m_so_no_rotation_covariant_freeze_deformation_gaps_the_light_partners_light_light_2026_10_23.py
---

# The corner stabilizer forces a scalar light block at X and M: no rotation-covariant FREEZE deformation gaps the light partners light-light

Claim type: bounded_theorem (one exact Schur statement plus an exact continuity corollary; numerics labelled).
Runner: runner.py, TOTAL: PASS=6 FAIL=0, 0.9 s, 84 MB peak, 2.4 k characters; run through
scripts/runner_cache.execute_runner under a unique filename (status ok, exit 0). Axioms unchanged.

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
- A2 (corollary, continuity). Take the polar part of the light-labelled block, or the inverse light Green's
  function at zero frequency. Either one is a T-covariant 2x2 function on the torus with a Weyl at K = 0, and
  it is scalar at X. Its two eigenvalues are a band that rises from 0 and a band that falls from 0, and they
  coincide at X.
  - A band gapped away from isolated nodes stays on one side of 0 (and of pi). Two such bands can coincide
    only at 0 or pi.
  - So exactly one of three things happens: (i) X is a node at quasienergy 0 or pi; (ii) a band crosses 0 or pi
    along a surface (a light Fermi surface); (iii) the light block vanishes or the Green's function has a zero.
  - In case (iii) the local winding around X is preserved (it is topological), so the partner survives as a
    Golterman-Shamir zero with its old chirality.
  - The same argument holds at M relative to R at quasienergy pi.
- Therefore no deformation of FREEZE, free or interacting, T- and translation-symmetric, leaves the
  light-labelled sector with only the K = 0 and R Weyls. A light-light mass at X would be a 2x2 term that
  commutes with Q8, which is a scalar: it shifts the 2-fold X level and never splits it.

## B. Finite diagnostics

- B1. 3 random T-covariant deformations U_F exp(i H_cov) (H_cov a rotation-twirled random Bloch Hamiltonian on
  all 8 modes). Covariance holds to 4e-15, and the light block at X, M is scalar to 2e-15. Its phase at X is
  generic (-1.38, -0.61, 1.32), not 0 or pi, so by A2 those cases have light crossing surfaces.
- B2. The designed light-light layer exp(i a phi(K) tau3 Pi+), with phi = 3 - sum cos K_i cos K_j, is
  T-invariant, vanishes at K = 0 and R, and equals 4 at X and M.
  - The node Weyls are untouched (U = U_F exactly there).
  - The X level stays 2-fold and moves to quasienergy 4a.
  - The lower light band crosses 0 on the line 0 -> X at s = 0.919 (a = 0.1) and at s = 0.691 (a = 0.25).
    That crossing is a light Fermi surface, which is the partner smeared rather than gapped.

## C. Anomaly bookkeeping (light-labelled projection of FREEZE, polar part; matches freeze-mirror-smg C2)

- Light: K = 0 and R carry -1; the 3 X (quasienergy 0) and the 3 M (pi) carry +1. Net +2 at 0 and +2 at pi.
- Mirror: exactly opposite (-2, -2), and the total is 0, as a cube-local circuit requires (total winding 0).
- The target content of the light sector, the K = 0 and R Weyls only, would be net -1 at 0 and -1 at pi. That
  is a nonzero Floquet 3D winding.
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

A light-light mass needs the same irrep with opposite chirality. That gives:
- Only s(x)w can pair, and that pairs the K = 0 light Weyl with an X combination, which kills the Weyl.
- s(x)w^2 and s have no light partner. Their only same-irrep, opposite-sign partners are mirror modes.

Zooming therefore does not give light-light partner gapping either (at the corner fixed point; nodes moved off
the fixed point are not covered).

## Answers

1. A T-covariant FREEZE variant with light-labelled nodes only at K = 0 and R: does NOT EXIST. This is exact,
   for any depth or range and any mixing (A1-A2).
2. Mirror-only charge-4 gapping without releasing partners: impossible under T and translation, whatever the
   mirror term is. After any symmetric mirror gapping, the light Green's function block is still scalar at X
   and M (A1), so the partners come back as poles, a pole surface, or zeros (A2). The release found in
   freeze-mirror-smg (B4b) is therefore GENERIC; it is not a FREEZE accident. Not recomputed here.
3. Light-sector net chirality: +2 at 0 and +2 at pi per family on FREEZE. The target content would be a
   Floquet winding of -1 that a mirror-only gap cannot cancel.

Verdict: NO-GO (exact, bounded to T-covariant cell-translation-invariant rules). The obstruction is the Q8
stabilizer of the zone-boundary corners acting irreducibly on the light spinor, not the specific FREEZE gates.
Walls move: what escapes the theorem is a rule that breaks either (a) the D2 part of the corner stabilizer on
the light doublet, for example a light label that is not a spinor doublet, as in a composite multi-cell label,
or (b) the cell-scale translation in a way that moves the partners off fixed points. Neither is tested here.

## Gate (the candidate rule "add a T-covariant light-light layer that gaps the X/M light partners")

1. Numbers: none (a free). Pass.
2. Named structure: none. Pass.
3. Prediction not built for: the rule cannot be built (A1). Its tested instance (B2) produces a light Fermi
   surface. FAIL.
4. Axiom bent: none (cell-local, one mode per site).

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
  - the node / crossing / zero trichotomy;
  - the corner chirality signs and the nets (+-2).
- Literature, cited and not used in a proof: the Floquet chiral magnetic effect; the Spin-Z4 Z16
  classification (via freeze-mirror-smg).
- Not used: any measured number.

## Next

- Test a rule in which the light label is not a single-cell spinor doublet, for example a composite two-cell
  label whose stabilizer at X acts reducibly. Or break D2 covariance on the light sector with a reason.
- Otherwise, accept partner zeros and test whether a light-propagator zero at X is physically benign
  (the open Golterman-Shamir question).
