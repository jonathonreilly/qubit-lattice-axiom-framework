# J:derive:review-20261016-irreducible-coin-certificate:a1 — attempt

Worker: Claude Sonnet 5.5 (same family as the source campaign; not an independent referee). Unrefereed. Owner-requested research
work: not accepted science, no audit verdict, no PR, no premise adopted. Status words ("retained", "closed", "derived from the
axioms") are not used; every computed statement below is labelled CHECKED and is computer-assisted.

## 0. Plain-language summary

The question: take a walk step on the cubic lattice that hops at most one site in each direction (the 27-point cell), carries an
internal "coin" that is an irreducible representation of the cube's rotation group (lifted to its double cover), and looks the same
after every proper cube rotation. Must it be the do-nothing step (a constant phase)? The sources show it for a coin of one
dimension and for spin 1/2, and claim it for the three remaining irreducible coins E (2-dim), spin 1 (3-dim) and spin 3/2 (4-dim) from
archived computer output that the current-main notes do not accept as a certificate (they ask for a reproduction from raw covariant
matrices with exact characteristic-zero ideal membership).

I rebuilt the whole calculation from raw covariance equations with new code (sympy and Fractions only; no Singular, no pickles, no
numerical filter) and solved it exactly. For E, spin 1, spin 1/2 and spin 3/2 the unitarity equations have exactly one solution over
the complex numbers once the global phase is fixed: the identity. No exact dispersive counterexample exists in this class. For spin
3/2 the only non-constant behaviour that survives the two line tests (axis and body diagonal) is an axis conditional shift exp(-/+ i t Gamma), Gamma =
F(C4x) (x) sigma_x; it is killed by the other rotations through a linear-algebra proof that 1 lies in the ideal.

`check.py` reruns everything: `TOTAL: PASS=67 FAIL=0`, 225 s wall on a machine under load average about 200 (77 s of CPU), peak resident memory 298 MB.

## 1. What I read (stated as required)

- Read in full: `docs/MINIMAL_AXIOMS_2026-06-29.md` (233 lines) and `docs/ai_methodology/skills/PRIMITIVE_REGISTRY_CHECK.md`
  (130 lines), on main `a77a3449c91a753b06ce2a63876cd460b62cb4cf`.
- Source branch `claude/toe-campaign-24h-20261015`, frozen commit `b0178fa585cad5ac9e02e70dff2175593dbc5dab` (it is an ancestor of
  the fetched branch head `8c01c25cbb8b751e66fb2f16c039cb6c1d8bc9c9`). The five source objects were extracted from the frozen commit
  and their sha256 verified: all five match the task (RECOVERY_STATUS.json). I read in full `spinj_exact.py` (246 lines),
  `spin32_branch.py` (20), `tosing_alg.py` (26), `tosing_branch.py` (35) and the 511-line frozen-commit note, plus the archived logs
  `spin32_exact.log`, `spin32.log`, `spin32_b{0,1,2}.out`, `specE_exact2.log`, `spin1_exact.log` for comparison only.
- Corrected current-main notes preferred over the snapshot: `docs/TWO_QUBIT_SITE_UNFREEZES_THE_CUBIC_TICK_DOUBLER_FREE_DIRAC_WALK_BOUNDED_THEOREM_NOTE_2026-10-16.md`
  lines 362-421 (the table "Which sites unfreeze", "Irreducible-coin extension — archived proof candidate" at :399-415),
  `docs/CUBIC_COVARIANCE_FREEZES_A_ONE_QUBIT_TICK_CELL_CLASSIFICATION_BOUNDED_THEOREM_NOTE_2026-10-16.md` (premises :60-75, Theorem 0 :77),
  and `.claude/science/review-fixes/review-drain-20261016/CUBIC_TICK_SCOPE.md:17-21` and `:63-74` (the obligation: reproduce the E,
  spin-1 and spin-3/2 eliminations from raw covariant matrices with complete real/imaginary constraints and exact characteristic-zero
  ideal membership).
- Prior-art search: no landed note or script on main treats the irreducible-coin elimination beyond the archived candidate
  (`grep` of `docs`, `scripts`, `.claude/science` for "irreducible coin"); no other `probes/work` attempt carries this task id. Open
  PRs searched with `gh pr list`: none on the irreducible coin. Open PR #9872 (Margolus spin-3/2 edge hop) is a block-centred
  construction with rotations about block centres, a different setting from the site-centred 27-point cell (the parent note already
  separates block-centred covariance, `...CUBIC_COVARIANCE...:` "block-centred" row, and `CUBIC_TICK_SCOPE.md:22`); no overlap.

## 2. Three layers, kept apart

**What the axioms say** (`docs/MINIMAL_AXIOMS_2026-06-29.md`): the Lattice axiom supplies the points of Z^3, nearest-neighbour
adjacency, translations and proper cubic rotations about each site (:35-41); the Qubit axiom supplies the one-site algebra M_2(C)
(:43-53); Admissibility and Record are not used. The memo states that axioms and approved primitives are the complete supplied
foundation (:108-112) and that Admissibility is not a dynamics axiom and does not choose a transfer operator (:114-130). The three
approved primitives (`PRIMITIVE_REGISTRY_CHECK.md:31-129`: scale reference, `c_t = c_s`, realized state) supply no coin, no
stencil, no unitary tick.

**What the lane supplied (models, ASSUMED)** — all of these are mathematical hypotheses, not framework content:
- (M1) a one-step translation-invariant unitary U(k) = sum_{n in {-1,0,1}^3} A_n e^{i k.n} on C^d, d = 2, 3, 4;
- (M2) the coin is an irreducible unitary representation D of the binary octahedral group 2O (conjugation action; the sign ambiguity of
  a lift cancels), with covariance A_{Rn} = D(R) A_n D(R)^{-1} for the 24 proper rotations R;
- (M3) unitarity with respect to the D-invariant Hermitian form H (unique up to scale for an irreducible D).
The coins of dimension 3 and 4 exceed the one-site algebra M_2(C); the 4-dimensional one is the parked M_4(C) fork (current-main
two-qubit note, section "Bearing on the parked M_4(C) fork"). The 2-dimensional E acts on a qubit through S_3 (the axis
permutation); whether this action belongs to the soldering menu was not examined (reading).

**What is proved** — Section 4, with labels.

## 3. Setting and notation

Cell: C = {-1,0,1}^3, 27 points, O-orbits of sizes 1, 6, 12, 8 with stabilisers O, C4, C2, C3. U(k)^dagger means
H^{-1} U(k)^* H. Unitarity of U for all real k is equivalent to the 125 matrix identities

  C_m := sum_n A_n H^{-1} A_{n-m}^* H = delta_{m,0} 1,   m in {-2,...,2}^3.   (L)

Irreducible representations of 2O (order 48): A1, A2 (dim 1), E (2), T1, T2 (3), E_{1/2}, E_{5/2} (2, spinorial), H (4, spinorial).
Twisting a representation by the sign character leaves its conjugation action unchanged, so A2 ~ A1, T2 ~ T1 = spin 1,
E_{5/2} ~ E_{1/2} = spin 1/2 for the purposes of (M2). Spin 3/2 restricts to the irreducible H = E (x) E_{1/2}.

**Clifford spinor times flavour, explicit.** Every irreducible projective representation of O is one of these eight. The spinorial
ones carry the 2O cocycle: E_{1/2} = spinor (x) trivial flavour, E_{5/2} = spinor (x) sign flavour, H = spinor (x) E with E a linear
(non-projective) flavour. A spinor times a *spinorial* (projective) flavour is not irreducible: E_{1/2}(x)E_{1/2} = A1 + T1,
E_{1/2}(x)E_{5/2} = A2 + T2. Those reducible coins (this is where the two-qubit Clifford walk lives: spinor (x) C^2 with trivial
flavour action) are outside the present statement. A covariant triple of anticommuting involutions Gamma_a (a vector under
conjugation) needs T1 inside End(D): the multiplicity of T1 in End(D) is 0 for E, 1 for T1 (but dimension 3 is odd and Cl(3) irreps
are 2-dimensional, so no triple), 1 for E_{1/2}, 2 for H (CHECKED, P1.12). So for the irreducible coins a Clifford triple exists only for
spin 1/2 and spin 3/2, and for spin 3/2 the flavour algebra End(E) = A1 + A2 + E has only scalar invariants (Schur), so the
two-qubit mechanism (two *invariant* flavour involutions anticommuting with the triple) has no room. I do not rely on this heuristic:
the computation below imposes **no** Clifford ansatz; A_n ranges over the full covariant space (7, 12, 7, 19 complex parameters),
which contains every spinor-times-flavour form. For spin 3/2 these 19 parameters split (CHECKED, P2b.2) as spin-scalar (x)
{identity, J, E-doublet} = 4+1+2 and spin-vector (x) {identity, J, E-doublet} = 3+3+6, where J is the unique A2 element of End(E);
the identity-flavour channel (4+3 = 7) is the one-qubit sector u(k)(x)1.

## 4. Steps

Labels: PROVED = full argument given here; CHECKED = executed by `check.py` in exact arithmetic (names `P<part>.<...>`);
ASSUMED = premise; READING = interpretation.

1. **PROVED (Lemma 1, Laurent form).** U U^dagger = 1 on the torus iff (L): a trigonometric polynomial vanishes identically iff all
   its Fourier coefficients do. With the form H: U^* H U = H iff U H^{-1} U^* H = 1 (square matrices).
2. **PROVED (Lemma 2, Schur gauge).** Reindexing n -> Rn in sum_n A_n gives D(R) U(0) D(R)^{-1} = U(0). D irreducible, so U(0) = lambda 1;
   U(0) is unitary, so |lambda| = 1. Replacing A_n by lambda^{-1} A_n keeps (M1)-(M3). Hence WLOG sum_n A_n = 1. CHECKED on the
   covariant bases: the origin coefficient A_0 and U(0) are scalar for every covariant family (P2.*.b, P2.*.c); the commutant of D is
   one-dimensional, i.e. D is irreducible (the n = 0 orbit has stabiliser O).
3. **PROVED (Lemma 3, one-dimensional coins).** D = chi gives A_{Rn} = A_n, so U is a scalar trigonometric polynomial of modulus one;
   a Laurent polynomial u with u(z) conj(u)(1/z) = 1 is a unit of C[z^{+-1}], hence a monomial c z^m; invariance under O forces
   R m = m for all R, so m = 0 and U = c.
4. **CHECKED (reduction to four coins).** The eight characters A1, A2, E, T1, T2, E_{1/2}, E_{5/2}, H are orthonormal on the 48 elements of
   2O, their dimensions have squares summing to 48: the list is complete (P1.10). The character of E (x) E_{1/2} equals the spin-3/2
   character and the vector representation has the spin-1 character on all 48 elements (P1.8, P1.9). By Lemma 3 and the
   Ad-equivalences, the cases left are E, T1 = spin 1, E_{1/2} = spin 1/2 (already a landed result; used here as a control), and H = spin 3/2.
5. **CHECKED (exact models).** E: the S_3 action on the sum-zero plane in the rational basis e1-e2, e2-e3 with Gram form
   [[2,-1],[-1,2]] (P1.4, P1.5). Spin 1: D(R) = R. Spin 1/2 and spin 3/2 in a *Pauli-factorised rational model*: A = sum_mu a^mu (x)
   sigma_mu with a^mu in End(flavour); Ad_S sigma_a = sum_b R_ba sigma_b (verified for all 24 lifts, P1.7), so covariance is a rational
   linear condition on the coefficient tuple and the unitarity ideal lives over Q (no sqrt 2, sqrt 3 in the equation system). The Pauli
   basis is checked against the explicit 4x4 lift D = F (x) S (P2.spin32.e, P2.spin12.e). The raw covariance nullspaces have dimensions
   7, 12, 7, 19, equal to 1 + dim commutant(C4) + dim commutant(C2) + dim commutant(C3) (P2.*.a).
6. **CHECKED (unitarity equations).** All 125 identities (L), split into real and imaginary parts in the real unknowns x_j, y_j
   (A_n = sum_j (x_j + i y_j) M_{jn}), give 77, 82, 64 and 1115 distinct real quadrics in 14, 24, 14 and 38 unknowns for E, spin 1,
   spin 1/2, spin 3/2 (P3.*). No orbit-representative shortcut is used. The identity walk satisfies all of them.
7. **CHECKED (positive controls).** The machinery must not hide genuine moving covariant walks: for the subgroup D4 the axial shifts
   exp(+-i k_z sigma_z) lie in the D4-covariant space (15 parameters) and satisfy all 109 equations exactly (P4.1), and the exact
   line-branch test keeps their branches (P4.2); the same for D3 and the body-diagonal shifts exp(+-i (k1+k2+k3) sigma.n) (P4.3,
   P4.4); the shift (x) identity on the E flavour is a covariant unitary walk of the spin-1/2 (x) E coin under D4 for the form
   H_E (x) 1 (P4.5). These are the companion note's D4 and D3 results, reproduced by the same code path.
8. **PROVED (Lemma 4, line lemma).** Let R0 in O fix the direction a (R0 a = a) and let P be the projector onto a one-dimensional
   eigenspace of D(R0). Covariance at the fixed momentum gives U(ta) D(R0) = D(R0) U(ta), so U(ta) preserves the line V = range P and acts there
   by a Laurent polynomial u(z), z = e^{it}, with |u| = 1 (U is H-unitary and V is an invariant line). A Laurent polynomial of
   modulus one on the circle is c z^m (Lemma 3's unit argument), and u(1) = 1 by Lemma 2, so u = z^m. Writing B_r = sum_{n.a=r} A_n, rank
   one gives P U(ta) P = sum_r z^r tr(P B_r) P, i.e. the *linear* conditions tr(P B_r) = delta_{r,m}, r in {n.a}: for the axis a = (1,0,0)
   m in {-1,0,1}; for the body diagonal a = (1,1,1) m in {-3,...,3}.
9. **CHECKED (exact branch exhaustion).** Every irrep used has simple spectrum for D(C4x) (all eigenspaces one-dimensional: 2, 3, 2, 4
   of them) and one-dimensional C3 eigenspaces on the body diagonal (2, 3, 2, 2 of them; for spin 3/2 the third eigenvalue is
   doubly degenerate and is not used). A branch is a choice of exponents (m_j) on the axis and (q_a) on the diagonal. Whether the
   linear system of Step 8 has a solution c in C^p is decided *exactly*: it is a linear system over K = Q(i, sqrt 3) in the complex
   unknowns c; solvability over C equals solvability over K; I rewrite it over Q by Weil restriction and compare every right-hand
   side with the exact left null space (no numerical discard). Results (P6.*.a): E 9 x 49 patterns -> only the trivial branch;
   spin 1/2 9 x 49 -> trivial; spin 1 27 x 343 -> trivial; spin 3/2 81 x 49 -> trivial and the two axis branches
   (-1,+1,+1,-1), (+1,-1,-1,+1) (body exponents 0 in all cases). In the spin-3/2 projector order (F = +,-) x (sigma_x = +,-) the moving
   branch is U(t,0,0) = exp(-+ i t Gamma) with Gamma = F(C4x) (x) sigma_x, Gamma^2 = 1 (READING of the exponent pattern: exponent =
   -F*sigma_x). Archived `spin32_exact.log` lists the same three branches in its own ordering (comparison only).
10. **PROVED (Lemma 5, exact elimination).** (a) *Linear cascade.* If a Q-linear combination of the quadrics has degree <= 1, it is
    an element of the ideal, so its solution set can be substituted into the other generators without losing a complex solution;
    a nonzero constant in the Q-span gives 1 in the ideal (no solution over C). Iterating is pure exact linear algebra over Q.
    (b) *Nilpotency.* If every remaining unknown v has v^N in the ideal, the only common zero over C is 0 (Nullstellensatz), so the
    solution set is a single point; the unknowns being real is not used, so the conclusion holds over C, which contains the real
    solutions.
11. **CHECKED (Route A, no line lemma: E and spin 1/2).** With sum_n A_n = 1, the cascade reduces E to 17 equations in 8 unknowns and
    spin 1/2 to 18 equations in 9 unknowns; sympy's Buchberger algorithm over Q (grevlex) shows every unknown nilpotent (indices <= 3),
    hence the unique solution is the identity walk (P5.E, P5.spin12). This is a closure with no branch assumption at all.
12. **CHECKED (Route B closure of every consistent branch).** Trivial branch: the line conditions plus the cascade leave 1 equation in 1 unknown (E, index 2), 3 equations in
    2 unknowns (spin 1: x7, y8, indices 2), nothing (spin 1/2) and 37 equations in 10 unknowns (spin 3/2, indices 3); all unknowns nilpotent; the
    unique solution reconstructs to A_0 = 1, A_n = 0 (n != 0) (P6.*.b). Spin 3/2 moving branches: the cascade reaches a nonzero constant
    after 4 rounds of linear algebra, i.e. **1 lies in the ideal for both** (P6.spin32.c): no solution over C. The trivial residual of
    spin 3/2 is re-solved in grlex and lex orders with identical nilpotency indices (P6.spin32.d).
13. **CHECKED (explicit certificates, engine-independent; partly complete).** (i) Trivial-branch residues: for E (1 unknown) and spin 1 (2 unknowns)
    every remaining unknown has an explicit cofactor identity x^N = sum_i c_i f_i (N = 2, degree-2 Macaulay matrix over Q) verified by
    polynomial multiplication. For spin 3/2 (10 unknowns, N = 3) such identities with cofactor degree <= 1 exist and are verified for
    **4 of the 10** unknowns (x9, x10, y10, y13); the other 6 need a larger Macaulay matrix (degree 4, thousands of rows) that did not
    fit the time budget in pure-Python sympy, so for those 6 the nilpotency rests on the three Groebner computations (grevlex, grlex,
    lex) of Step 12 only. (ii) For each of the two moving spin-3/2 axis branches the cascade's row operations are recorded, giving an
    explicit identity 1 = sum_i c_i f_i over the 1115 quadrics plus the branch's linear conditions (103 nonzero cofactors, 14,968
    terms, cofactor degree <= 3), verified by multiplying out in the polynomial ring (P7.spin32.moving*). So both moving branches
    are refuted by an explicit, independently verifiable certificate, not only by rerunning the elimination.
14. **PROVED + CHECKED (sign-twisted covariance).** If covariance holds only up to the sign character, A_{Rn} = s(R) D A_n D^{-1}:
    for T1 and E_{1/2} every twisted-covariant family has U(0) = 0, hence none is unitary (P8.1, P8.2); for E and H, E (x) sign = E
    with intertwiner T (T F = s F T), H-conformal; W_n := A_n T is plainly covariant and unitary, so U = W T^{-1} (P8.3-P8.5), and the plain
    case applies. (Only characters 1 and sign exist for O; other phase choices were not examined.)
15. **Assembly (CHECKED, computer-assisted; not a hand proof).** For D in {E, T1 = spin 1, E_{1/2} = spin 1/2, H = spin 3/2} every walk with
    (M1)-(M3) is lambda times the identity (Steps 2, 11, 12); with Step 3 and Step 4 this covers all eight irreducible
    representations of 2O, and with Step 14 sign-twisted covariance. No exact dispersive counterexample exists in this class.

## 5. What is new, and what is not

Not new: the statement (archived as "Theorem 8" in the frozen note, `...UNFREEZES...2026-10-16.md` frozen :352-398, downgraded on current
main to an "archived proof candidate", `...UNFREEZES...:399-415`), the strategy (axis and body-diagonal lines, branch exhaustion,
Groebner closure), the branch census (my census agrees with the archived logs: trivial only for E and spin 1, trivial plus two axis
branches for spin 3/2), and the spin-1/2 and scalar cases (the parent note and Step 3).

New in this attempt (same-family, unrefereed):
(a) an independent reconstruction from raw covariance (nullspace of the generator conditions, not the stabiliser-commutant
parametrisation of `spinj_exact.py`), with complete real/imaginary unitarity constraints from all 125 shifts;
(b) branch exhaustion by exact K-linear algebra (Weil restriction) in a different formulation (one trace condition per
one-dimensional eigenprojector); the archive has a numerical least-squares prefilter (`spinj_exact.py:199-236`) and its own exact
left-null-space recheck (`spinj_exact.py:158-198`, logs `*_exact.log`), whose branch lists agree with mine; `spin32_branch.py:14-20` is a
random-start numerical search and certifies nothing;
(c) a rational Pauli-factorised model that keeps the whole spin-3/2 ideal over Q, so no Singular over Q(sqrt 3) is needed;
(d) the linear cascade: both moving spin-3/2 branches are dispatched by four rounds of exact linear algebra (no Groebner basis), with an
explicit cofactor identity 1 = sum c_i f_i recorded and verified;
(e) characteristic-zero closure of the trivial residues by Buchberger in three monomial orders (spin 3/2 residue: grevlex, grlex, lex)
plus explicit Macaulay-matrix cofactors verified by multiplication (complete for E and spin 1, 4 of 10 unknowns for spin 3/2);
(f) Route A closures of E and spin 1/2 that use no line lemma, agreeing with Route B;
(g) positive D4/D3 controls, the character-complete irreducible list, the sign-twist reduction and the Clifford-times-flavour census.

## 6. First unresolved step, and limits

- **First unresolved step: Step 9 for spin 1 and spin 3/2.** The closure of these two coins uses the line lemma (Step 8, hand proof)
  and the exact branch exhaustion (Step 9, one implementation). A line-free closure (Route A) did not finish in sympy: after the
  cascade, spin 1 leaves 45 equations in 18 unknowns and spin 3/2 leaves 81 equations in 33 unknowns, too large for sympy's Groebner
  routines within this budget. So for spin 1 and spin 3/2 the branch census is supported by the positive controls (Step 7),
  by Route A/Route B agreement on E and spin 1/2, and by agreement with the archived census, but not by a second line-free
  derivation.
- Trust base: sympy's `DomainMatrix.rref` over QQ and `groebner`; mitigated by the cofactor identities of Step 13. For 6 of the 10
  residual unknowns of the spin-3/2 trivial branch only Groebner evidence (three monomial orders, one algorithm) exists; an explicit
  degree-4 cofactor computation for them is a further, purely mechanical step.
- No cross-family confirmation; the J-agent protocol's independent check is still owed.
- Not touched: reducible coins (the two-qubit unfreezing lives there), larger hop ranges (range two is landed, range three is
  another task), other covariance phases than 1 and sign, block-centred covariance, any link to the axioms beyond the premises of
  Section 2. The result does not show that a physical coin must be irreducible, nor that a coin of dimension 3 or 4 is available.
