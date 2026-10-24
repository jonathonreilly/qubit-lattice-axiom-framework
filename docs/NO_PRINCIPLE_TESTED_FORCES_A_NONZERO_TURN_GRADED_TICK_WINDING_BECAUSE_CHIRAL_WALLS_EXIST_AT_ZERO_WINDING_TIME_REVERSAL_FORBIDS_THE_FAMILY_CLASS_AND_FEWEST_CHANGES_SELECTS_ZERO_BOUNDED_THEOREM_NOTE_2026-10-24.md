---
claim_id: no_principle_tested_forces_a_nonzero_turn_graded_tick_winding_because_chiral_walls_exist_at_zero_winding_time_reversal_forbids_the_family_class_and_fewest_changes_selects_zero_bounded_theorem_note_2026-10-24
claim_type: bounded_theorem
claim_scope: "Free-field Floquet ticks on CL-1's 2x2x2 cell on the (111) turn axis, with the site-gauged turn T3 as a symmetry; FREEZE, CTWIST and the F/F^+ slab (g = 0.5) rebuilt from twist-local-single / floquet-pi-slab / slab-parity. (0) Every copy-flip winding W = f(q_l,+) + f(q_m,-), q_m != q_l, has all three Z3 components nonzero. (a) A W = 0 slab (Ls = 6) has a one-handed light q 2 on one wall and its mirror on the other; gappable-mirror bookkeeping holds for every N_f at W = 0. (b) Lemma: a Floquet antiunitary T, a unitary chiral symmetry, or an axis-reversing unitary that normalises the turn group forces a zero component of W, so each forbids the family class; CL-1's tick has all three (and the C2' of its 24 rotations), FREEZE has no on-cell one; FREEZE plus its T partner has W = 0; a T-less turn-commuting circuit has W = 0. (c) W(CTWIST) = W(U_A) = 2 W_F, and FREEZE halves it; a fewest-changes cost (leave-site / leave-cell probability per tick) is 0 at the identity, -> 0 for CL-1's tick as eps -> 0, O(1) for every W != 0 tick tested, and invariant under U -> U^+ while W flips. (d) W is additive; the W = 0 class holds the identity and every turn-commuting circuit. Not covered: interactions, gauge fields, the copy-mass factor, K-dependent intertwiners in the numerical search (the lemma covers them), principles not listed."
upstream_dependencies:
  - minimal_axioms
  - candidate_laws
  - no_adopted_rule_fixes_the_floquet_slab_layer_parity_because_the_zoom_ladder_keeps_one_orientation_the_vacuum_fold_is_blind_to_inversion_and_adopted_half_ticks_carry_no_turn_winding_bounded_theorem_note_2026-10-24
  - a_circuit_slab_puts_its_mirror_in_the_other_copy_only_through_a_nonzero_turn_graded_winding_which_forces_equal_flow_at_quasi_energy_pi_and_is_set_by_termination_bounded_theorem_note_2026-10-23
  - the_composite_twist_walk_is_a_five_layer_cube_local_circuit_and_freezing_one_copy_leaves_one_l_and_one_r_per_node_bounded_theorem_note_2026-10-23
runner: scripts/no_principle_tested_forces_a_nonzero_turn_graded_tick_winding_because_chiral_walls_exist_at_zero_winding_time_reversal_forbids_the_family_class_and_fewest_changes_selects_zero_2026_10_24.py
---

# No principle tested forces a nonzero turn-graded tick winding: chiral walls exist at zero winding, time reversal forbids the family class, and fewest changes selects zero

Claim type: bounded_theorem. Exact statements are labelled [T], finite diagnostics [F] and readings [S].
Runner: runner.py, TOTAL: PASS=10 FAIL=0, 1.0 s, 64 MB peak, 5.9 k characters of stdout, seeded, AUDIT_TIMEOUT_SEC = 120.
It was tested under a unique filename (scratch/tick_winding_origin_test_run.py). Axioms unchanged. No rule adopted.

## Question

slab-parity showed that mod-3 families (the copy-flipped mirror) happen exactly when the update tick has a nonzero
turn-graded winding W, and that FREEZE has W_F = (-2, 1, 1) while CL-1's adopted tick has W = 0. Does any adopted or
independently motivated principle FORCE W != 0, without choosing it to get families? Four candidates were checked in order:
(a) chirality consistency, (b) the record arrow / time reversal, (c) FREEZE from CL-2 fewest changes, (d) least information.

Repo first (criteria_pre_run.txt). A git grep of origin/main (docs, scripts) for "turn-graded winding", "anomalous floquet"
and "tick winding" found nothing. Open PR #9863 (3D winding W3 of supplied walks) is a different invariant; it is cited,
not used. Builds on slab-parity, floquet-pi-slab (sum rule, B1 lemma, B2 corollary), twist-local-single (CTWIST, U_A,
FREEZE), anomaly-family-count (index), and the register (CL-1 24-rotation covariance; "The arrow. The record set only
grows, while the update is reversible"; record-arrow-family-phase: every arrow structure keeps cube inversion or sigma_d K).

## Pass criteria

Written before any code ran (criteria_pre_run.txt), used unchanged. PASS = a principle that forces W != 0 and is not a
disguised choice. Predicted: FAIL for (a)-(d). Every line matched its prediction. One runner predicate (c2) was wrong in
its arithmetic: FREEZE and U_A both leave every site with probability 1 (CTWIST's K = 0 block is exactly zero), so
"FREEZE < run" holds in the leave-cell cost, not the leave-site cost. The predicate was corrected before the final run.

## 0. The copy-flip class

- 0 [T]. W lies in Z[Z3] with augmentation 0. A copy-flipped wall pair (light q_l hand +, mirror q_m hand -) needs
  W = f(q_l,+) + f(q_m,-), with f(q,h) = h(e_(q+2) - e_(q+1)).
  - W = 0 <=> q_m = q_l.
  - Every copy-flip W is +-((1,1,1) - 3 e_a): all three components are nonzero. W_F is the (q_l, q_m) = (2, 1) element.
  - Elements with a zero component, such as (0, 1, -1), are single-pair flows f(q, h). They are nonzero but NOT copy-flip.

## (a) Chirality

- a1 [T]/[F]. The W = 0 slab (Ls = 6, F/F^+ layers, label gates) has a one-handed light q 2 on the near wall (layer 0,
  hand +1) and its mirror q 2 on the far wall (layer 5, hand -1). Near-wall flow (-1, 1, 0) = f(2,+), far-wall flow
  (1, -1, 0), total W = 0.
  - Each wall's anomaly is inflowed by the slab. W is the SUM of both walls' flows, not the single-wall inflow.
  - So the adopted one-handed content does not need W != 0.
- a2 [T]. Gappable-mirror bookkeeping (anomaly-family-count index N_f (q_l - q_m) = 0 mod 3, Omega twist k = -q_m).
  - At W = 0 (q_m = q_l) it holds for every N_f.
  - At W = W_F it restricts N_f to {3, 6, 9, 12, ...}.
  - W != 0 only restricts the family count. Chirality plus gappability are satisfied in the W = 0 class.

Answer (a): FAIL as forcing.

## (b) Time reversal and the record arrow

- b1 [T]. Lemma. Let Theta be one of:
  - a Floquet antiunitary T, U(k) -> U(-k)^+;
  - a unitary chiral symmetry, U(k) -> U(k)^+;
  - an axis-reversing unitary, U(kappa) -> U(-kappa).
  If Theta normalises the turn group (Theta T3 Theta^-1 = w^c T3^(+-1)), it maps turn sector a to sigma(a) and forces
  W_a = -W_sigma(a). In all 12 (type, sign, c) cases, sigma is either an involution of Z3 with a fixed point or a shift.
  Together with sum W = 0, this forces a zero component of W (checked by null space, 12/12).
  - So EACH such symmetry forbids the copy-flip (family) class.
  - The lemma covers K-dependent sector-mapping Theta as well, since a determinant winding is conjugation-invariant.
  - T alone (sigma(a) = -a) allows W in Z (0, 1, -1), a non-family class. Chiral or inversion symmetry commuting with
    the turn (sigma = id) forces W = 0 entirely.
- b2 [T]/[F]. CL-1's tick has all three symmetries.
  - T: B U1(k)^* B^+ = U1(-k)^+ with B = exp(i eps R_e), the half-tick (identity to 4e-16). Theta = K up to a half-tick
    conjugation, and K commutes with T3.
  - On-cell chiral and k -> -k intertwiners commuting with T3 each exist and are unitary (1-dimensional, condition 1.00).
  - The 24-rotation covariance contains the axis-reversing C2' about (1,-1,0). It maps T3 -> T3^-1 exactly, so CL-1's
    covariance alone forces W_0 = 0.
  - FREEZE has no invertible on-cell intertwiner of any of the three types: the generic element of each linear
    intertwiner space is singular (condition ~1e-16). This is required by the lemma, since W_F has no zero component.
    Its T-covariance (12 rotations) has no axis-reversing element.
- b3 [T]/[F]. Control: the T-closure of FREEZE (FREEZE plus its image under Theta = K, U_F(-k)^T) has W = (0, 0, 0).
- b4 [T]/[F]. A random depth-6 turn-commuting cube-local circuit has no on-cell T, chiral or inversion intertwiner, yet
  W = 0 (floquet-pi-slab B1). W = 0 is not equivalent to T.
- b5 [S]. The record arrow lives in the records ("the record set only grows, while the update is reversible"). It never
  enters the unitary U, so it cannot set U's determinant winding. The arrow structures that record-arrow-family-phase found
  (cube inversion, sigma_d K) both normalise the (111) turn, so by b1 each would FORBID the family class.

Answer (b): FAIL as forcing. T breaking is NECESSARY for the family class (and with it, breaking CL-1's C2' and any
turn-normalising chiral or inversion symmetry), not sufficient.

## (c) FREEZE from fewest changes

- c1 [T]/[F]. Where W comes from: W(CTWIST) = W(U_A) = (-4, 2, 2) = 2 W_F. eta_x commutes with T3 and swaps Pi+ and Pi-,
  so each half carries W_F.
  - Freeze the disagreeing half: W_F (with FREEZE's i tau3 quarter phase, or with the identity).
  - Run it: 2 W_F. Reverse it (Pi- U_A^+): 0.
  - FREEZE does not create the winding. It halves one already present in the supplied CTWIST.
- c2 [T]/[F]. Change cost = per-tick probability that a mode leaves its site / its cell (site-averaged, from the K = 0
  Fourier block on a 6^3 grid, exact for these trig-polynomial ticks):

    tick                       leave site / leave cell   W
    identity                   0.000 / 0.000            (0, 0, 0)
    CL-1 tick, eps 0.3         0.167 / 0.087            (0, 0, 0)
    CL-1 tick, eps 0.05        0.005 / 0.002            (0, 0, 0)
    CTWIST                     1.000 / 1.000            (-4, 2, 2)
    U_A (run)                  1.000 / 1.000            (-4, 2, 2)
    FREEZE                     1.000 / 0.500            (-2, 1, 1)
    freeze, identity on Pi-    0.728 / 0.500            (-2, 1, 1)
    reverse                    1.000 / 1.000            (0, 0, 0)

  - The global minimum is the identity (W = 0). Adopted-form W = 0 ticks go to zero cost continuously (eps -> 0), while
    every W != 0 tick tested costs O(1).
  - [T] cost(U) = cost(U^+) on a sector (same moduli), while W(U^+) = -W(U). So run and reverse cost the same: the
    measure is blind to the sign of W.
  - Inside the supplied CTWIST + Pi split, freezing beats running in cell cost. But the cheapest frozen half is the
    identity, not FREEZE's i tau3 quarter phase (same W_F). So FREEZE's quarter phase is not a fewest-changes output
    either; it was chosen for the equidistant dark-state placement (twist-local-single gate item 1).

Answer (c): FAIL. Fewest changes selects FREEZE-like freezing only inside the supplied CTWIST + Pi split, whose W is already
nonzero. Globally it selects W = 0.

## (d) Least information among tick classes

- d1 [T]/[F]. W is additive under composition: W(F U_CL1) = W_F, W(F F) = 2 W_F. The tick classes are the cosets of
  Z[Z3]_0.
  - The W = 0 class contains the identity, CL-1's tick and every circuit of turn-commuting cube-local gates.
  - A nonzero class needs gates that are NOT individually turn-commuting (floquet-pi-slab B2).
  - Any least-information or least-structure selection therefore picks W = 0: the wrong direction.
- d2 [S]. If the copy-flip class were forced, its minimal element would be +-W_F (n = +-1). Nothing tested forces it.

Answer (d): FAIL, selecting W = 0.

## Answer

FAIL, as predicted. No principle tested forces W != 0.
- (a) Chirality and gappability are satisfied at W = 0.
- (b) T, chiral and axis-reversing symmetries each FORBID the family class (lemma). CL-1's tick has all three, including
  the C2' in its own 24-rotation covariance. Breaking them is necessary, not sufficient. The record arrow does not act on U.
- (c) Fewest changes is minimal at W = 0, is blind to the sign of W, and does not single out FREEZE's quarter phase.
- (d) Least information selects W = 0.

Positive side result [T]: a W != 0 (family-class) tick requires breaking BOTH Floquet time reversal and the axis-reversing
part of CL-1's 24-rotation covariance (it is at most T-covariant, as FREEZE is). Adopting FREEZE-class ticks is therefore a
symmetry-lowering CL-1-level choice, and its cost is now explicit.

## Gate (anti-smuggling)

No rule is proposed. "The update tick is FREEZE-class" stays the open CL-1 decision named in slab-parity. Its gate entry
must now list, as things it bends inside CL-1 (not the axioms): Floquet T, the axis-reversing C2' of the 24 rotations, and
fewest changes (cost 1.000 / 0.500 against 0 for the identity). Predictions of its own (pinned pi node, pi partners on both
walls, inert dark states at +-pi/2) remain UNTESTED.

## Smuggling review

Supplied: FREEZE, CTWIST, the Pi split, the F/F^+ slab and label gates, g, eps, the cost measure's form (leave-site /
leave-cell probability, one reading of CL-2's "fewest occupation changes"), the 6^3 grid, free fields.

Forced: the copy-flip class has no zero component; W = 0 slabs carry one-handed walls; the index allows every N_f at W = 0;
the symmetry lemma (12 cases); CL-1's T, chiral, inversion and C2' symmetries; W = 0 for FREEZE's T-closure and for T-less
turn-commuting circuits; W(CTWIST) = 2 W_F; cost(U) = cost(U^+); additivity of W.

Not shown: interactions; gauge fields; the copy-mass factor; an exhaustive search over K-dependent intertwiners (the lemma
needs none); other candidate principles (for example an anomaly-matching requirement across zoom rungs) not listed in the
criteria.
