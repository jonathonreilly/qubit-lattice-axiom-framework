---
claim_id: no_vacuum_of_family_blind_rules_tested_gives_three_hierarchical_families_with_a_t_odd_phase_adjoint_vacua_cannot_enter_masses_and_quartic_alignment_is_t_even_bounded_theorem_note_2026-10-24
claim_type: bounded_theorem
claim_scope: "Family-blind rules with family U(3) (gap-vertex-family-tensor Lemma). Exact: (A0) SU(3) has no singlet in adj x 6 or adj x adj x 6, so no vacuum built from family-adjoint (triality-0) order parameters can enter a 16.16 mass term; (A1) Spin(10) 16 x 16 has no singlet and 16 x 16bar one, so the only gauge-singlet Lorentz-scalar family bilinear is light x mirror; (A2) Wick: on-site density-density energy of a Slater state is ((trG)^2 - trG^2)/2, so repulsive family-blind density terms are attractive in the family-adjoint exchange channel; (C) for any convex U(3)-invariant cost the det channel of the forced far-wall term (C = 1) condenses with equal singular values (locked SU(3) kept); (D) tr U = 0 forces the Z3 character spectrum, which has equal singular values, keeps T x P23 and gives commuting mass functions (J = 0, V = 1). Finite: (B) supplied half-filled naive lattice Dirac band, on-site exchange g: first-order family-density (Stoner) transition at g_c = 2.40 (bandwidth 1.73) straight to the U(1)^3 vertex (1,0,-1), alpha/g_c = 3e-3; (E) two Hermitian adjoints with seeded U(3)-invariant potentials to quartic order: P-linear potentials always align; with tr(ABAB) misalignment occurs (0.16 wide box, 0.50 with dominant tr(ABAB) > 0) but every minimum found (79 sets) has det[A,B] = 0 (J = 0). Not covered: fluctuation-induced (Coleman-Weinberg) signs, sextic and higher potentials, triality-carrying (3, 6) composite vacua, the far-wall SMG dynamics, 3+1D interacting numerics."
upstream_dependencies:
  - the_minimal_turn_neutral_far_wall_term_for_three_families_has_a_free_family_matrix_whose_only_rule_blind_choice_keeps_u3_so_no_family_label_bounded_theorem_note_2026-10-24
  - the_family_class_tick_gives_no_family_label_from_the_copy_mass_slab_depth_zoom_rung_or_record_cadence_and_its_copy_mass_keeps_the_family_fixing_antiunitary_bounded_theorem_note_2026-10-24
  - the_family_class_tick_keeps_a_time_reversing_antiunitary_that_fixes_every_family_so_it_supplies_no_quark_cp_phase_and_keeps_theta_bar_at_zero_or_pi_bounded_theorem_note_2026-10-24
  - far_termination_winding_keeps_a_pi_free_screening_near_wall_but_the_end_is_a_chosen_boundary_bit_and_the_far_wall_must_gap_all_three_families_together_bounded_theorem_note_2026-10-24
  - a_turn_kept_by_the_update_and_broken_by_the_vacuum_gives_cp_and_theta_bar_together_unless_a_nelson_barr_block_is_supplied_bounded_theorem_note_2026-10-22 (open PR #10047)
runner: see stems.txt
---

# No vacuum of the family-blind rules tested gives three hierarchical families with a T-odd phase: adjoint vacua cannot enter masses, and quartic alignment is T-even

Claim type: bounded_theorem. Labels: [T] exact, [F] finite diagnostic, [S] reading or estimate.
Runner: runner.py, TOTAL: PASS=12 FAIL=0, 8 s, 175 MB peak, 2.1 k characters, seeded, AUDIT_TIMEOUT_SEC = 120.
Tested under a unique filename (scratchpad spontaneous_family_breaking_test_run.py, deleted). Axioms and CL text
unchanged. No rule adopted. Criteria: criteria_pre_run.txt, written before code.
Deviations from the pre-run criteria (recorded as results, not hidden):
- C1 first run FAILED as a sampling defect: the g range (0.5-6) left only 2/150 sets condensed (the det channel is
  cubic, so condensation is first order and needs larger g). Range changed to 4-40: 118/150 condense, 0 asymmetric.
- E2 PREDICTION FAILED: I predicted a nonzero fraction of T-odd (J != 0) quartic minima. None was found in 79
  bounded sets (max det[A,B]/norm^6 6.5e-8). The check now records the computed fact.
- E "at most two distinct eigenvalues per matrix in most cases" partly failed: with two adjoints and mixed cubics,
  both spectra are 1+1+1 in 15% (wide box) and 54% (dominant tr(ABAB)) of minima. The ratios are O(1) (no hierarchy
  measure was computed; [S]).
- B: no intermediate U(2)xU(1) window appeared; the transition is first order straight to U(1)^3.

Repo first: git grep of origin/main docs for "vacuum alignment", "flavon", "familon", "family ferromagnet" finds
nothing relevant; open PRs: #10047 (spontaneous-turn-cp), #10068 (cp-source-new-tick). Built on gap-vertex-family-tensor
(Lemma, centre identity D2, epsilon structure), family-labels (R1-R3, 12 kept antiunitaries), cp-source-new-tick
(generalized-CP lemma), far-termination-winding (bulk keeps T, X = 1 on copies). Contradicts none.

## Question (BACKLOG 5b)
The adopted rules are family-blind (U(3) commutant), so forced terms cannot label families (gap-vertex Lemma). Can a
VACUUM of the adopted registers break U(3) spontaneously into three families with (i) a hierarchy and (ii) a phase odd
under every family-fixing antiunitary (J != 0), with no fitted input?

## A. Which order parameters can matter [T]
- A0. Triality obstruction. A light mass term is psi_i^T C psi_j (gauge part) M_ij with psi in the 3 of family SU(3),
  so M must lie in 6bar (or 3 for the 120). SU(3) has no singlet in adj x 6 or adj x adj x 6 (computed: 0, 0; control
  6bar x 6: 1). Reason: the family centre acts on psi psi as w^2 and trivially on adjoints. So ANY vacuum built only
  from family-adjoint (triality-0) order parameters, Hermitian or unitary, cannot feed a 16.16 mass term at any order.
  By gap-vertex D2 the turn on q = 2 families is this centre, so a mass-feeding family vacuum must carry triality,
  i.e. break the family centre = turn (or be combined with a triality-carrying register, and registers carry no family
  charge: register line "Registers carry no family charge"). This links 5b to spontaneous-turn-cp (#10047): a
  turn-breaking vacuum gives CP and theta together unless a Nelson-Barr block is supplied.
- A1. Spin(10): 16 x 16 has 0 singlets, 16 x 16bar has 1 (computed on the 16 built from the Spin(10) Clifford algebra).
  Two same-hand Weyls make a Lorentz scalar only in 16 x 16 (gauge-charged: 10 + 120 + 126), and psi^dagger psi is a
  Lorentz vector. So a gauge-singlet Lorentz-scalar family bilinear exists only as light (near wall) x mirror (far
  wall), the Dirac pairing. Condensing it makes the low-energy content vector-like (excluded by V - A) or removes the
  light families at the condensate scale; the register already requires the mirror in the symmetric phase.
- A2. Wick identity, exact on Slater states (max err 4e-16): <sum_{i<j} n_i n_j> = ((trG)^2 - trG^2)/2. The exchange
  part -trG^2/2 rewards family polarisation: a repulsive family-blind density-density term (Gauss's law among charges)
  is ATTRACTIVE in the family-adjoint channel; an attractive one is attractive in pairing channels instead.

## B. (a) Family-adjoint density condensate (Stoner) [F]
Supplied: naive lattice Dirac band E = +-|sin K| (DOS ~ e^2 at the node; stand-in for the half-filled light sea),
L = 24^3, on-site exchange g, family-total charge fixed (sum delta = 0).
- The node's vanishing DOS makes the band cost steeper than g delta^2 at small delta, so U(3) is unbroken below a
  finite threshold: g_c = 2.40 in band units (bandwidth 1.73). A Gauss-law-sized coupling (alpha ~ 1/137 in cell units)
  is 3e-3 of g_c: no breaking from the adopted links.
- Above g_c the transition is first order straight to the constraint polytope's vertex (1, 0, -1): U(1)^3, three
  distinct families (one family's sea empty, one full, one at the node). No U(2)xU(1) window appeared.
- Physics reading [S]: this is a family-density (chemical-potential) texture, a Lorentz vector order with cell-scale
  densities, equally spaced (no hierarchy), and real (density is T-even, so the kept antiunitary survives: J = 0).
- Verdict (a): R1 PASS only at strong supplied coupling; R2 FAIL; R3 FAIL; also excluded by Lorentz invariance and by
  the absence of a cell-scale family background, and by A0 it cannot feed masses anyway.

## C. (a') The forced far-wall term's own channel [T]
The norm-8 term with the rule-blind C = 1 (gap-vertex) is (sum_i psi3^+_i psi0_i) x eps(psi4^+)^3 eps(psi5)^3, and the
epsilon pair equals 6 det M with M_ij = psi4^+_i psi5_j (adjoint action M -> g M g^+).
- Lemma: for any convex, U(3)-invariant cost K(sigma) of M's singular values (true in the Gaussian/HF class, where
  the energy is linear in the one-body density matrix and the constraint is linear), F = K - g prod(sigma) is minimised
  at equal singular values: Jensen gives K(mean) <= K(sigma), AM-GM gives prod(mean) >= prod(sigma).
- Finite check: 118/150 random convex costs condense, 0 asymmetric. The vacuum is M = sigma U: a locked diagonal SU(3)
  (colour-flavour-locking type) survives. The mirror-gapping interaction does not label families; it prefers the most
  family-symmetric condensate.

## D. (b) Z3 family-character vacuum [T]
- With M = sigma U, the det channel fixes only det U; the eigen-phases are flat at this order. tr U = 0 holds exactly
  for the equally spaced spectrum e^(ib)(1, w, w^2) (20/20 minimisations, error 4e-6), a single orbit. So the Z3
  character vacuum IS the minimum whenever the coefficient of |tr U|^2 is positive; that sign is fluctuation-induced
  and not fixed by the rules (not computed).
- It breaks U(3) -> U(1)^3 (distinct eigen-phases): R1 holds in form. But its singular values are all 1 (no hierarchy,
  R3 FAIL); conj(U0) = P23 U0 P23, so T x P23 is kept (a family-permuting antiunitary, X = P23) and the
  generalized-CP lemma gives J = 0 (max 2e-17 over 200); and every mass function of one normal order parameter
  commutes with every other, so V = 1 (R2 FAIL). By A0 it also cannot enter a 16.16 mass term.

## E. (c) T-odd vacuum texture from two misaligned order parameters [T]/[F]
Two Hermitian adjoints A, B (stand-ins for up- and down-type family order parameters; Georgi-style sequential
breaking), all U(3)-invariant terms to quartic order, seeded couplings (FITTED class by construction).
- E1 [T]/[F]. Every term except tr(ABAB) and (trAB)^2 is linear in P = |W|^2 (W the relative rotation), so at fixed
  spectra the minimum is a vertex of the Birkhoff polytope (a permutation): aligned, [A,B] = 0, no mixing, J = 0
  (18/18 sets, max commutator 1e-5).
- E2 [F]. With tr(ABAB) and (trAB)^2: misaligned minima occur in 16% of a wide box and 50% when tr(ABAB) is dominant
  and positive (tr(ABAB) - tr(A^2B^2) = tr([A,B]^2)/2 <= 0, so k4 > 0 rewards a commutator). But EVERY minimum found
  (79 bounded sets, plus 180 + 30 in exploratory scans not in the runner) has det[A,B] = 0: the misalignment is real
  (orthogonal up to rephasing), J = 0. Spontaneous T x C2' breaking was never preferred at quartic order. [S] Reading:
  with A diagonal, V depends on B only through B_ii and |B_ij|^2, while the triple-product phase is fixed by the
  spectrum; the minima seem to sit on the boundary where that phase is 0 or pi. Not proved.
- E3 [T]. If masses were Hermitian functions of adjoints, arg det would be 0 or pi (theta_tree = 0 or pi), a
  parity-type (Babu-Mohapatra) protection. But A0 forbids adjoints from entering 16.16 masses, so this protection is not
  available on the adopted content; a triality-carrying (6-valued) vacuum has independent phases, and theta_bar
  returns with J (cp-source-new-tick section 5, #10047).
- Verdict (c): a T-odd vacuum needs at least sextic terms with chosen signs/sizes (not tested); couplings are not fixed
  by any rule: gate item 1 would fail. theta_bar: protected only in the forbidden adjoint case.

## General obstruction (answer to the brief's last item)
- A single U(3) adjoint with polynomial potential breaks to U(2)xU(1) generically (for SU(3) the quartic is degenerate
  and the cubic picks diag(1,1,-2), Li 1974, cited as supplied); U(1)^3 needs a tuned or higher-order potential.
  Here the rule-fixed channels give: the Gauss-law exchange channel, no breaking at alpha (B1); the forced far-wall
  det channel, a locked SU(3) (C); neither gives U(2)xU(1) or U(1)^3 at the couplings the rules fix.
- U(1)^3 vacua that do occur (B2 at strong supplied coupling, D, E's 1+1+1 minima) give O(1) eigenvalue ratios, never
  a hierarchy: polynomial or mean-field potentials with O(1) coefficients have O(1)-separated stationary points.
- A continuous spontaneous U(3) breaking also leaves familons (Goldstones); at cell-scale f they are harmless, at low f
  excluded (K -> pi + familon); not quantified.

## Answer
NO, on every candidate tested.
- (a) A family-adjoint bilinear: the only gauge-singlet scalar one is light x mirror (vector-like, excluded); the
  density (Stoner) one has a finite threshold far above alpha, goes first order straight to U(1)^3 (1,0,-1) at strong
  supplied coupling, is Lorentz-violating, T-even and equally spaced. The forced far-wall det channel locks a diagonal
  SU(3) (exact, convex class).
- (b) The Z3 character vacuum is the unique tr U = 0 orbit and is the minimum iff a fluctuation sign is positive; it
  gives no hierarchy and keeps T x P23 (J = 0, V = 1).
- (c) Misaligned two-adjoint vacua exist for chosen couplings but are T-even at quartic order in every case found.
- Above all (A0): adjoint (triality-0) vacua cannot enter 16.16 masses at all. A family vacuum that feeds masses must
  carry family triality, i.e. break the centre = turn on q = 2 families, which puts 5b on the spontaneous-turn-cp route
  (CP and theta tied unless a Nelson-Barr block is supplied).
R1: only in form (B2 strong coupling, D). R2: FAIL everywhere. R3: FAIL everywhere.

## Route (not a wall)
A triality-carrying composite vacuum in the 6 (or 3) of family, built from gauge-singlet four-fermion composites
(16^4 contains singlets; gap-vertex: Omega has triality 1 and no SU(3) singlet, so every contraction is a choice) or
from a far-wall composite transmitted through the leak. It must (1) be selected by energy rather than chosen,
(2) break the turn without giving theta_bar (Nelson-Barr-type block), and (3) give exponentially separated values,
which no polynomial potential with O(1) coefficients did here; a hierarchy needs a different source (rung or depth
exponents, family-labels (b)/(c)), so 5b and item 6 must be solved together.

## Gate and smuggling review
No rule is proposed, so the gate is not applied. A rule that picked the |tr U|^2 sign, the quartic couplings, a
6-valued vacuum frame or the Stoner coupling would choose numbers or family structure (gate items 1 and 2).
- Supplied: the naive lattice Dirac band and on-site exchange g (B); the convex cost class (C); unitary-U and two
  Hermitian adjoints as order-parameter stand-ins (D, E); all potential couplings (seeded, FITTED class); alpha as
  the Gauss-law scale; the Spin(10) spinor construction; Li 1974 and Babu-Mohapatra as literature.
- Forced: A0, A1, A2, the C lemma, D1-D3, E1 (Birkhoff), E3.
- Not shown: Coleman-Weinberg signs, sextic potentials, triality-carrying vacua, interacting 3+1D dynamics, the far
  wall SMG itself, a proof of the E2 T-even pattern.
