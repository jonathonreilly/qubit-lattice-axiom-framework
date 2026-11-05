---
claim_id: the_minimal_turn_neutral_far_wall_term_for_three_families_has_a_free_family_matrix_whose_only_rule_blind_choice_keeps_u3_so_no_family_label_bounded_theorem_note_2026-10-24
claim_type: bounded_theorem
claim_scope: "1+1D 3-4-5-0 far-wall proxy (far-wall-smg) with N_f = 3 identical copies, family-blind U(1)_A x U(1)_B, mirror turn charge q = 1 per mode (frame k = 0: a term's turn charge is its total occupation change mod 3). Exact: the turn charge of n1 l1 + n2 l2 is 2(n1+n2) mod 3, and the mixed turn-U(1)_A,B anomaly is 2 N_f mod 3. The fewest-change turn-neutral flavour change is uniquely +-(l2 - l1) = +-(1,3,-3,-1) (norm 8), which conserves mode number; mode-number-breaking ones start at norm 12. K-nullity plus one-site Pauli force flavours 4 and 5 into the family epsilon, leaving a free 3x3 family matrix C on flavours 3 and 0. The coefficient space carries U(3); its only invariant line is C = 1 (commutant u(3), dimension 9); every other choice lies on a U(3) orbit of dimension 4 to 8 (not unique). The q = 1 turn is the centre of family SU(3). In the k = -q_mirror frame the minimal norm-6 term's 81-dimensional family space has no SU(3) singlet. A primitive, Lagrangian, A,B-neutral, turn-neutral gapping lattice exists at N_f = 3 (graph of R x (2J/3 - 1)) and not at N_f = 1; it keeps S3 and a real family map. Not covered: the gapping dynamics of any of these sets, the full U(3) stabiliser of a fermionic gapping set, 3+1D and the 16 (argued, not computed), gauge fields."
upstream_dependencies:
  - minimal_axioms
  - candidate_laws
  - the_fewest_change_symmetric_far_wall_term_is_forced_and_gaps_the_3450_mirror_in_a_wall_mode_chain_while_the_flux_pump_separates_anomalous_content_bounded_theorem_note_2026-10-23
  - the_slab_mirror_sits_on_the_light_copy_so_the_turn_anomaly_allows_every_family_count_and_the_number_conserving_spin12_term_cannot_gap_the_mirror_bounded_theorem_note_2026-10-23
  - the_spin10_pair_square_on_two_sixteens_is_a_spin12_casimir_with_a_unique_singlet_ground_state_and_gap_four_g_but_a_frozen_far_region_still_moves_the_mirror_bounded_theorem_note_2026-10-23
  - the_family_class_tick_gives_no_family_label_from_the_copy_mass_slab_depth_zoom_rung_or_record_cadence_and_its_copy_mass_keeps_the_family_fixing_antiunitary_bounded_theorem_note_2026-10-24
runner: see stems.txt
---

# The minimal turn-neutral far-wall term for three families has a free family matrix whose only rule-blind choice keeps U(3), so it gives no family label

Claim type: bounded_theorem. Labels: [T] exact, [F] finite or numerical, [S] argued reading.
Runner: runner.py, TOTAL: PASS=20 FAIL=0, under 1 s, about 40 MB, 2.9 k characters, seeded, AUDIT_TIMEOUT_SEC = 120.
It was tested under a unique filename (gap_vertex_family_tensor_test_run.py, then deleted). Axioms and CL text are
unchanged, and no rule is adopted. Criteria were written before any code ran (criteria_pre_run.txt). Every prediction held.
Verdict: FAIL on brief P2 (menu M4), on both FAIL branches.

## Question (brief P2)
On the family-class tick the mirror sits in the other copy, with turn charge q = 1 for every family. For N_f = 3, what is
the fewest-change symmetric far-wall gapping term, and what is its family tensor? Is its U(3) commutant smaller than SU(3),
which would give a rule-made family label?

## A. Lattice and anomaly [T]
- A1. l1 = (1,-2,1,2) and l2 = (2,1,-2,1) are neutral, K-null, mutually null and primitive (far-wall-smg A2, rederived).
- A2. With the mirror at q = 1 per mode, a term's turn charge is its total occupation change. For n1 l1 + n2 l2 this is
  2(n1+n2) mod 3, so a single-family l1 or l2 term is turn-charged.
- A3. Per family the coefficients are sum K q^2 = 0, sum K q QA = 2 and sum K q QB = 2. So the mixed turn-U(1) anomaly is
  2 N_f mod 3, which vanishes only for N_f = 0 mod 3. This is the proxy image of the family-class tick's count.

## B. Fewest-change term [T]
- B1. Among turn-neutral flavour changes L != 0 in the lattice, the minimum l1-norm is 8. It is reached only at
  +-(l2 - l1) = +-(1,3,-3,-1), so the flavour content is unique.
  - This L has sum 0: it CONSERVES mode number.
  - Mode number has a mixed anomaly with U(1)_A (2 per family, 6 at N_f = 3). So this term cannot gap the far wall on its
    own. That is the proxy version of the anomaly-family-count correction: the gapping set must break mode number.
- B2. The smallest mode-number-breaking turn-neutral L have norm 12: +-(5,0,-3,4) and +-(4,-3,0,5), with sum L = +-6.

## C/D/E. Family tensor of the norm-8 term [T]/[F]
- C1. The norm-8 family distributions of L = (1,3,-3,-1) over 3 families come to 414 null patterns. The one-site ones
  (Pauli: at most one fermion per mode per site) are exactly 9, and they force flavours 4 and 5 to occupy all three
  families once.
  The term is O = C_ij psi3^+_i (eps psi4^+ psi4^+ psi4^+)(eps psi5 psi5 psi5) psi0_j.
  - The epsilon on flavours 4 and 5 is FORCED by Pauli.
  - C is free.
  - Other patterns need 2 or 3 sites, so they lose on locality.
- D1. The coefficient space has dimension 9 (C). Its u(3)-invariant and su(3)-invariant subspaces are each one line,
  C = 1.
- D2. The family centre w*1 acts on the term as w^(-sum L) = 1. The mirror's uniform q = 1 turn IS the centre of family
  SU(3). So "turn-neutral" equals "triality zero", which is exactly the condition that allows an SU(3) singlet.
- E1. Tangent-space commutants:

  | C | commutant | dimension |
  |---|---|---|
  | 1 | u(3) | 9 |
  | generic | i*1 | 1 |
  | E11 | u(1)+u(2) | 5 |
  | diag(1,2,3) | torus | 3 |
  | diag(1,1,2) | u(1)+u(2) | 5 |

- E2. Every C other than 1 lies on a U(3) orbit of dimension 4 to 8. So fewest changes (all nine monomials have 8
  changes) does not fix C.
- E3. Phase removal does not fix C either. The rephasing has rank 5 on the 9 monomials, so a generic C keeps 4 phases.

## Lemma [T]
If the rules are family-blind (U(3) commutes with them, family-labels A2/B1) and fewest changes plus phase removal fixes a
term uniquely up to a phase, then g.T is proportional to T for all g in U(3). So T spans a one-dimensional representation,
and its commutant contains SU(3).
Consequently brief P2's PASS (unique, and commutant below SU(3)) is impossible for any family-blind rule. The outcome is
always one of the two FAIL branches. The same argument applies in any representation, including the 16.

## G. Control: frame k = -q_mirror [T]
With the twist chosen so that the mirror is turn-neutral, the turn constrains nothing.
- The minimal term is l1 or l2 (norm 6). On one site its family space is 3b x L2(3) x 3b x L2(3b), of dimension 81.
- That space has NO SU(3) singlet (centre phase w^-2), so every choice breaks SU(3).
- A generic choice has discrete commutant, but it is picked from an 81-dimensional space. This is the "not unique" branch.

## H. A symmetric gapping set (bosonic lattice) [T]
- H1. N_f = 1: the only Lagrangian lattice is turn-charged, so there is no symmetric gapping.
- H3. N_f = 3, family-diagonal lattice: also turn-charged (the turn would break spontaneously).
- H2. N_f = 3: the graph of R x U, with R the 3-4-5 rotation and U = 2J/3 - 1, is primitive, Lagrangian, A,B-neutral and
  turn-neutral in every element. This is an explicit symmetric gapping lattice at N_f = 3, consistent with A3.
  - Its LLL basis has two kinds of vector:
    - four L = 0 family-relative half-steps (norm 12);
    - the family-democratic sums of l1 and of l2 (norm 18, sum L = 6).
- H4. Its family-net charges have rank 3, so no continuous family torus survives.
- H5. It is invariant under all of S3, so it does not distinguish the three families. R1 fails.
- H6. U is real. So the copy-basis antiunitary with X = 1 is kept, and R2 fails. Its commutant is u(1)+u(2), a 1+2 split
  about (1,1,1).
- H7. It does not contain the norm-8 minimal monomials.
- It is one construction, not a proven fewest-change set. Other rational U exist, and that choice is supplied.

## Answer
1. The minimal symmetric (A, B, turn) far-wall term for N_f = 3 is the one-site 8-fermion term
   C_ij psi3^+_i eps(psi4^+)^3 eps(psi5)^3 psi0_j.
   - Its flavour content and its epsilons are forced.
   - The family matrix C is not forced.
   - The only rule-blind choice, C = 1, has commutant U(3) (this contains SU(3)): FAIL.
   - Any other choice is a supplied family frame: FAIL (not unique).
   - It also conserves mode number, so it cannot be the gapping term alone.
2. The menu's two outcomes need correcting.
   - The epsilon_ijk outcome is the forced part (on flavours 4 and 5), and it is U(3)-blind there (det x det*).
   - The d_ijk outcome is unavailable: no rule picks a non-invariant tensor (Lemma).
3. A full symmetric gapping set exists at N_f = 3 and not at N_f = 1, which supports the family-class count in the proxy.
   But the set's family structure keeps S3 and is real, so it fails R1 and R2.

## Transfer to the 16 [S]
- In the 16 the far-wall term must be a Spin(10) singlet: its net occupation change dN is 0 mod 4 (the Z4 centre).
- Turn-neutral at q = 1 adds dN = 0 mod 3. So:
  - the mode-number-conserving minimum is B^+B type (four fermions, U(3)-invariant via delta, which cannot gap:
    anomaly-family-count D1);
  - the minimal mode-number-breaking term needs dN = +-12. Its triality is 0, so SU(3)-singlet (epsilon^4-type)
    contractions exist, and the rule-blind choice keeps SU(3) x Z12.
- In the k = -q frame, Omega (dN = 4, triality 1) has no SU(3) singlet. Any family contraction of Omega is then a choice.
- What changes: the proxy's U(1)_A,B lattice is replaced by Spin(10) and Z4, and the minimal orders change (8 -> 4 or 12).
- What does not change: the Lemma, the centre identity, and the conclusion. None of the 16 statements is computed here.

## Gate and smuggling review
No rule is proposed, so the gate is not applied. A rule that picks C (or U), or a non-singlet Omega contraction, would
choose a family frame, which is a chosen family structure (gate item 2).
- Supplied:
  - the 1+1D 3450 proxy and its charges;
  - frame k = 0 (as in the brief), with k = -q as a control;
  - the norm and the locality tie-break;
  - the bosonic K-matrix gapping criterion;
  - the R x U construction.
- Forced:
  - A1-A3, B1-B2;
  - the epsilons;
  - the dimension-9 space, the invariant line and the commutants;
  - the centre identity;
  - the Lemma;
  - the N_f = 1 obstruction;
  - H2-H7 for the given U.
- Not shown:
  - dynamics: whether any of these sets actually gaps;
  - minimality of the gapping set;
  - the full fermionic U(3) stabiliser of the set;
  - the 16 in 3+1D.
