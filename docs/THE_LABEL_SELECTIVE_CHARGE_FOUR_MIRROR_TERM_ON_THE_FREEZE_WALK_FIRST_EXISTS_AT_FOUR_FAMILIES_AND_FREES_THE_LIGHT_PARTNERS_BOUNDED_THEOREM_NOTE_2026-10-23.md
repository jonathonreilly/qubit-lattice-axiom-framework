---
claim_id: the_label_selective_charge_four_mirror_term_on_the_freeze_walk_first_exists_at_four_families_and_frees_the_light_partners_bounded_theorem_note_2026-10-23
claim_type: bounded_theorem
claim_scope: "On rule FREEZE (twist-local-single), a cell-local, charge-4 interaction of the mirror-labelled modes (tau3 = -1 on Pi+) only. Exact: (A) no T-invariant such term exists for N_f = 2 or 3 families; the T-invariant count is C(N_f, 4), so the first one is at N_f = 4, where it is unique and forced to be SU(4)-family symmetric. (B) One-cell exact diagonalisation at N_f = 4: the term alone has a 2-fold cell ground state, A (mirror occupation 2 of 8) and B (6 of 8), whose turn charges differ. A supplied T-, SU(4)- and Z4-invariant mirror number bias selects A: a unique symmetric cell state with a single-particle gap. G_R(0) is then finite (no pole and no zero at the node). The light Weyls at the nodes are untouched (G_L^-1 = -h_LL to 4e-5 at |K| = 0.1). At X the light-labelled modes, which the free walk gaps only by mixing with the mirror, are freed: their lowest pole goes 1.23 -> 0.35 -> 0.21 -> 0.06 as g = 0, 1, 4, 16 (cell-gap units). (C) The light-labelled projection of FREEZE has 6 opposite-sign nodes at X and M per family; at N_f = 4 the gapped set carries Spin-Z4 index 8 mod 16 and SU(4)^3 index 2. Not covered: the infinite-lattice phase diagram, Floquet (rather than Floquet-Hamiltonian) interaction, N_f = 8."
upstream_dependencies:
  - minimal_axioms
  - candidate_laws
  - the_composite_twist_walk_is_a_five_layer_cube_local_circuit_and_freezing_one_copy_leaves_one_l_and_one_r_per_node_bounded_theorem_note_2026-10-23
  - the_block_local_quartic_gaps_the_dirac_mirror_symmetrically_and_releases_the_light_partners_bounded_theorem_note_2026-10-22
  - the_light_copy_zone_corner_partners_are_vector_like_only_through_the_sublattice_charge_bounded_theorem_note_2026-10-22
runner: scripts/the_label_selective_charge_four_mirror_term_on_the_freeze_walk_first_exists_at_four_families_and_frees_the_light_partners_2026_10_23.py
---

# On the FREEZE walk, the mirror-only charge-4 term first exists at four families and frees the light partners

Claim type: bounded_theorem (exact statements, plus one-cell exact diagonalisation and one grid search, each labelled).
Runner: runner.py, TOTAL: PASS=10 FAIL=0. It takes 6 s, peaks at 250 MB, and prints 5.8 k characters. It was run through scripts/runner_cache.execute_runner under a unique filename (status ok, exit 0). The axioms are unchanged.

## Question

The twist-local-single note left this open. FREEZE leaves one light and one mirror Weyl per node per family (K = 0 and R), and no free label term can gap the mirror. So can a mirror-only (tau3 = -1), charge-4, cell-local, multi-family interaction:
- gap the mirror symmetrically,
- leave the light Weyls gapless,
- and avoid freeing any light partner (Golterman-Shamir)?

Naming: by twist-local-single's own sign rule (det v > 0 = "L"), the tau3 = -1 label is its "L" with q = 2. Its section C calls the same states "R". Chirality naming is a convention, so this note says "light" (tau3 = +1, q = 1) and "mirror" (tau3 = -1, q = 2). At each node the two labels have opposite signs, and each sign is the same at K = 0 and at R (A0).

## A. Which terms T allows (exact)

The mirror label at a cell is a spin doublet r. The turn group it generates has 24 elements, and det r = w^(2q) != 1. Schur-Weyl gives Lambda^4(r x C^N) = sum over lambda of S_lambda(r) x S_lambda'(C^N). Taking each piece in turn:
- (2,2) is det^2 = w^(4q), which is not invariant;
- (3,1) is spin-1 x det, which has no T singlet;
- (4) needs N >= 4, and it is Sym^4(r) x Lambda^4(C^N), where Sym^4(r) has exactly one T-invariant line.

The character averages confirm this. For N_f = 2..8 the T-invariant charge-4 counts are 0, 0, 1, 5, 15, 35, 70, which is C(N_f, 4). The light label gives the same counts.

- A1. No term exists at N_f = 2 or 3.
- A2. At N_f = 4 the term is unique and SU(4)-family symmetric without that being imposed: Q = sum_s c_s eps_abcd r_a,s1 r_b,s2 r_c,s3 r_d,s4. "Multi-family" is therefore forced. The count 4 is set by the turn charge, not chosen.

## B. One cell, N_f = 4 (exact diagonalisation)

- B1. Q is T-invariant at the operator level (all 12 turns) and SU(4)-invariant (residuals 1e-13).
  - -(Q + Q^+) on the 8 mirror modes has a 2-FOLD ground state: A = |0> + Q^+|0> and B = |8> + Q|8>, with mirror occupations 2 and 6. Their turn charges differ by det(r)^4 = w^(8q) != 1.
  - So this is not a symmetry doublet. It is the term's particle-hole balance, and in a lattice it would be an extensive cell pseudospin.
  - G_R(0) = 0 holds only as the A/B average, because A and B give opposite finite values.
- B2. A mirror number term mu (N_R - 4)/4 with mu = 0.2 is T-, SU(4)- and Z4-invariant. It is SUPPLIED, not forced. It selects A: the cell ground state is unique and symmetric, the split is 0.2, and the single-particle gap is 1.05 in units of the cell gap. G_R(0) = -0.636 x 1, finite and the same on every mirror mode (Schur).
- B3 (Golterman-Shamir counting at both nodes, state A). Near the node G_R(0,K) = g0 + u sigma.K with g0 != 0. So the node carries neither a pole nor a zero. The would-be zero has the same winding as the mirror pole it replaced (sign checked at K = 0 and R). Its zero surface sits at |K| ~ |g0/u| ~ 3, outside the node region. The mirror winding is moved, not removed.
- B4a (one light family kept, 10 modes, 1024 states; g = 1). The light Weyl near K = 0 is untouched: G_L(0,K)^-1 = -h_LL(K) up to relative error 3.7e-5 at |K| = 0.1 and 4.6e-6 at 0.05. That is ~K^3, consistent with the O(K^2) label leak and the Schur ban on any light-mirror mass at the node.
- B4b (release at X = (pi,0,0)). The light-labelled projection at X is exactly 0, and the free walk gaps those states to 1.231 only by mixing them with the mirror. As g grows, the lowest light pole goes 1.231 (g = 0), 0.352 (1), 0.209 (4), 0.060 (16). By g = 16, 99.6% of the light weight is below 0.15. The gap falls as ~h_LR^2/g. A light partner is FREED, exactly as in the block-quartic note.

## C. Anomaly and the projected light walk

- C1 (bookkeeping; the Z16 classification of Spin-Z4 anomalies is a LITERATURE input, Garcia-Etxebarria-Montero / Tachikawa-Yonekura). The gapped set is 2 N_f mirror Weyls of Z4 charge 1, with index 2 N_f mod 16. That is 8 at N_f = 4. The SU(N_f)^3 index of the gapped set is 2 (two fundamentals). The N_f = 4 term keeps both Z4 and SU(4), so a symmetric trivial mirror gap that leaves only the light node Weyls is anomaly-forbidden. Z4 alone first permits N_f = 8 (16 Weyls). Even then, SU(8) would have to be broken by the choice among the 70 terms.
- C2 (finite diagnostic: 12^3 grid plus refinement). The polar part of the light-labelled projection P_L U_F P_L has 8 nodes per family:
  - the 2 light Weyls (K = 0 and R, sign -1);
  - 6 at the X and M points with the opposite sign +1, which are the partners the free walk gaps only through light-mirror mixing.
  The mirror projection mirrors this. The signed count is +2 at quasienergy 0 and +2 at pi. The polar projection is not a finite-depth circuit, so this count is not a static anomaly statement, and the IR bookkeeping is not closed by C2.

## Answers

1. Symmetric gap of the mirror: on one cell, only with the supplied mu (unique, symmetric, gapped, B2). Without mu the cell ground state is 2-fold (B1). Whether the infinite lattice is symmetric and gapped is not computed. C1 forbids the clean outcome at N_f = 4.
2. Light untouched: yes at the nodes (B4a), protected by Schur plus the O(K^2) label leak.
3. Zeros versus poles: at the node there is neither a pole nor a zero (g0 != 0). The mirror winding moves to a distant zero surface with the pole's sign (B3). The light partners at X and M come back as poles (B4b, C2).
4. Golterman-Shamir release: YES. 6 light partners per family at X and M are freed, with gap ~1/g.
5. Multi-family count: the term exists only for N_f >= 4. Spin-Z4 anomaly freedom needs N_f = 0 mod 8. SU(N_f) must be broken.

Verdict: NOT a chirality fix. A label-selective charge-4 mirror term on FREEZE repeats the block-quartic far-end failure. It lands on the light copy's zone-boundary partners, which FREEZE gaps only through the mirror.

## Gate (the candidate rule "mirror term = the unique T-invariant charge-4 product of the mirror label")

1. Numbers: the coupling g is free (not fitted), and mu is SUPPLIED with no derivation. Pass on g; mu is flagged.
2. Named structure: no gauge group or particle content is written in. N_f = 4 and SU(4) are FORCED by the turn charge (A2), not inserted. Pass.
3. Prediction not built for: the family threshold C(N_f, 4) (none below 4), plus the release at X and M. These are internal predictions that were not compared with measurement. Against the target (a chiral light spectrum) the rule FAILS: partners are freed.
4. Axiom bent: none. The term is cell-local, uses one mode per site, and adds no new site structure. It is composite-before-atomic compliant, because families are cell copies and the term uses no single-site structure.

Result: FAIL (it does not deliver the chirality it was built for). It is not adopted.

## Smuggling review

- Supplied:
  - FREEZE and its labels (twist-local-single);
  - the choice of the mirror label tau3 = -1 (eta_x makes the choice conventional);
  - families as identical copies;
  - mu;
  - the Floquet-Hamiltonian H_F = i log U_F (and i log(-U_F) at R) used for the exact diagonalisation;
  - one-cell twisted clusters;
  - the Z16 classification (literature).
- Forced:
  - the T-invariant counts and the N_f = 4 threshold;
  - the uniqueness of the term and its SU(4) symmetry;
  - the 2-fold degeneracy and the turn-charge split;
  - the finite G_R(0) for A;
  - the untouched light node;
  - the release at X.
- Not used: any measured number.

## Boundary and next

Not computed:
- the infinite-lattice phase (sign-free QMC is unlikely to be available, given the complex T-invariant c);
- the interaction applied as a Floquet layer;
- N_f = 8 with an SU(8)-breaking choice;
- whether a rule can make the free walk itself gap the X and M light partners without the mirror. The light-partner-gap note says this costs light chirality, unless a momentum-selective mirror phase exists.

The sharpest next probe asks for a T-covariant FREEZE variant whose light-labelled projection has no nodes at X and M. That means the partners are gapped light-light, not light-mirror.
