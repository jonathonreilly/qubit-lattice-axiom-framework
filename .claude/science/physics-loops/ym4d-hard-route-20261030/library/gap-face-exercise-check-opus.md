lead: Claude Opus 5.5 (lead session), dispatched 2026-11-17
row: 1105

Checker: Claude Opus 5.5, effort max, laptop subagent.
This is a same-provider check. The writer of row 1103 is Claude Fable 5.2.
So this check is not independent of the writer's provider.

## Plan (initial; I refine it after I read the row)

1. Read row 1105 of FINISH.md. That row is the full brief.
2. Read the row 1103 output and the sources that the brief names.
3. Check one statement per step. Append each verdict here before the next step.
4. Write the RESULT line.

## Plan (refined from row 1105)

Source: `library/gap-face-exercise-fable.md` (row 1103, Claude Fable 5.2),
steps 2, 3, 7.1, 7.2, 8 and section 9.7 (work item W1), and its runs in
`runs/gap-face-exercise-fable/`. I do not read the other check of row 1103
(`library/gap-face-exercise-check-astra.md`).

Statements, in check order:

- S1. Step 2: the coupling conversion beta = 4 beta_theirs, and the ranges
  of inventory item N1a.
- S2. Step 3: C1.
- S3. Step 3: C2 (test 1: direction mu periodic, nu free; the change of
  variables).
- S4. Step 3: C2'.
- S5. Step 3: C3.
- S6. Step 3: C4 (test 2: "an invariant function orthogonal to constants has
  support without degree-1 sites"; c_j at most c_(1/2)).
- S7. Step 3: C5(a).
- S8. Step 3: C6.
- S9. Step 3: C7 (test 5: the rank count on a torus).
- S10. Section 7.1: C14 (test 3: (a) gauge fixing with free boundary and
  positive variance; (b) each of the eleven graphs on four vertices; is the
  frozen-triangle case marked as a belief).
- S11. Section 7.2: C15 (test 4: "rows in W and columns in V is V tensor W"
  for finite support; the basis claim).
- S12. Step 8: the reduction "(F4-KP) gives the T-analog at the corner".
- S13. Test 6: search `main` and the open PR branches for C6, C7, C14, C15
  and for the corner (beta_L, beta_M, beta_T) = (0, beta, 0).

Verdict for each: HOLDS, HOLDS AFTER CORRECTION (with corrected text), or
FAILS (first failing line and, where possible, a counterexample). A run may
only guide or refute; a HOLDS needs a written argument.

## Progress

- Step 0: file created.
- Step 1: row 1105 read; plan refined. Next: read the source steps.
- Step 2: read in full: the source file L1-578 (header, steps 1-3),
  L1007-1118 (7.1, 7.2), L1220-1336 (step 8), L1441-1494 (9.7); and the four
  files of `runs/gap-face-exercise-fable/` (two scripts, two outputs).
  Source file: 1554 lines, commit 0bdd62338 of the clone. Next: S1.
- S1 done: HOLDS.
- S2 done (C1): HOLDS.
- S3 done (C2): HOLDS.
- S4 done (C2'): HOLDS AFTER CORRECTION (total-effect bound only for cubic boxes).
- S5 done (C3): HOLDS.
- S6 done (C4): HOLDS AFTER CORRECTION (general weight: use sup |c_j|; spatial sides >= 4).
- S7 done (C5a): HOLDS AFTER CORRECTION (Var A depends on L_4 when spatial couplings > 0).
- S8 done (C6): HOLDS AFTER CORRECTION (C_4 surfaces are sums of products; forest gap written only for the star).
- S9 done (C7): HOLDS.
- S10 done (C14): HOLDS AFTER CORRECTION ((c) false for small non-frozen couplings; (a) box dependence).
- S11 done (C15): HOLDS.
- S12 done ((F4-KP) -> T-analog): HOLDS AFTER CORRECTION (polymer set, KP constant, tori).
- S13 done (repo search): nothing found for C6, C14, C15, the corner; C7's rank count is on main (real form).
- RESULT written.

## S1. Step 2: the conversion beta = 4 beta_theirs and the ranges of N1a

Source text (step 2, L198-201 and N1a, L222). The run's weight is
exp(beta * (1/2) tr U_p) per unoriented plaquette.

**Arithmetic (proved here).** For SU(2), tr U is real, so
N beta_th Re Tr U_p = 2 beta_th tr U_p = 4 beta_th * (1/2) tr U_p.
So beta = 4 beta_th, if and only if the cited paper also counts each
unoriented plaquette once. If a paper summed over both orientations, the
factor would be 8, since Re Tr(U^-1) = Re Tr U.

**Shen-Zhu-Zhu convention (read by me, 2026-11-17, through a fetch tool;
the tool's own small model extracted the text, so this is a reading).**
- ar5iv HTML of arXiv:2204.12737, eq. (1.2): S(Q) = N beta Re sum over
  p in P^+_{Lambda_L} of Tr(Q_p); eq. (1.1): density exp(S(Q)) against
  the product of Haar measures over the positive edges.
- The sentence that defines P^+ (quoted in three parts by the tool): "the
  subset of plaquettes p=e1e2e3e4 such that the beginning point of e1 is
  lexicographically the smallest among all the vertices in p" / "and the
  ending point of e1 is the second smallest."
- Count (proved here): the vertices of the unit square at x in the plane
  (i, j), i < j, are ordered x < x+e_j < x+e_i < x+e_i+e_j
  lexicographically. The first clause fixes the start x. The second clause
  fixes the first step x -> x+e_j, which is an edge. So P^+ holds exactly
  one closed path per unoriented square. So the factor is 4, not 8.
- arXiv abstract page of 2204.12737 (v1 only, 27 Apr 2022): "Assuming
  |beta| < (N-2)/(32(d-1)N) for ... SO(N), or |beta| < 1/(16(d-1)) for
  SU(N)". For d = 4: beta_th < 1/48, so beta < 4/48 = 1/12 = 0.0833.
  The abstract lists log-Sobolev and Poincare inequalities and the mass gap
  (exponential decay for "a large class of observables") among the results.
- Cross-check (proved here, guide only for the paper's constant): with one
  path per square, the Hessian of one plaquette term is at most
  N|beta|(sum_i |X_i|)^2 <= 4N|beta| sum_i |X_i|^2, and each edge lies in
  2(d-1) squares. This gives 8N|beta|(d-1). With Ric(SU(N)) = N/2 for the
  metric Tr(X Y*), N/2 > 8N|beta|(d-1) is |beta| < 1/(16(d-1)): the
  abstract's threshold. A sum over both orientations would give 1/(32(d-1)).
  So the threshold and the one-per-square count agree.

**Cao-Nissim-Sheffield convention (not read by me).** The arXiv abstract
page of 2509.04688 (v1 4 Sep 2025, v2 28 Sep 2025, title "Dynamical approach
to area law for lattice Yang-Mills") names no beta range. No HTML version
exists (HTTP 404 for /html/2509.04688 and /html/2509.04688v2). I did not
download the PDF. So for this paper I use the lane's reading:
`library/gap-arealaw-opus.md` Section 1 (read of CNS p. 2 (1.1)-(1.2),
Definition 1.4, p. 3 Definition 2.1, p. 5) and its check
`library/gap-arealaw-check-astra.md` L73. They give the weight
exp(N beta sum_p Re Tr Q_p), the threshold beta*_SU(N) = 1/(8(d-1)), and
the Bakry-Emery constant K = (N+2)/2 - 1 - 4N beta (d-1).
- Consistency (proved here, given that reading): the CNS slab action of
  Definition 2.1 is N beta sum_e Re Tr(Q_x A_e Q_y^-1 B_e^-1), one term per
  positive edge e of the slice, that is one term per vertical square of the
  slab. It is the conditional law of the full measure. A full action with
  two paths per square would give the coefficient 2N beta there. So CNS also
  count each square once, and beta = 4 beta_CNS.
- K > 0 for SU(N) is N/2 > 4N beta (d-1), that is beta < 1/(8(d-1)). For
  d = 4: beta_CNS < 1/24, beta < 4/24 = 1/6 = 0.1667.

**Verdict S1: HOLDS.** beta = 4 beta_th is right for both papers (SZZ: the
one-path-per-square rule read in the primary text through a fetch tool;
CNS: from the lane's reading plus the slab-action argument above). The
ranges beta < 1/12 = 0.0833 (SZZ, gap and log-Sobolev) and beta < 1/6 =
0.1667 (CNS, area law) are right. The source's own remark in N1b is also
right: the SZZ abstract says 1/(16(d-1)), so a form 1/[16N(d-1)] is a
misprint. Not verified by me: the CNS theorem number "Thm 1.6" (the lane
reading cites Definition 1.4 for the threshold), and that SZZ's mass-gap
corollary covers every gauge-invariant local observable in periodic boxes
(the abstract says "a large class of observables"). N1a claims only the
ranges, so these do not change the verdict.

## S2. Step 3: C1 (chain)

Statement (L281-290): V_0..V_n with density prod_{t<n} f(V_t V_{t+1}^-1)
against Haar on G^{n+1}; then V_0 is Haar, the h_t = V_t V_{t+1}^-1 are
i.i.d. with density f and independent of V_0, and
E D^j(V_0 V_t^-1) = c_j(f)^t 1.

Check (my own derivation).
1. Change of variables. Replace V_n by h_{n-1} = V_{n-1} V_n^-1 with
   V_0..V_{n-1} fixed: for fixed V_{n-1} this is inversion, then left
   translation; both keep Haar measure (a compact group is unimodular). By
   Fubini the product measure is kept. Then replace V_{n-1} by h_{n-2},
   with h_{n-1} now a free variable, and so on. The composite is the map of
   the text, and dV_0..dV_n = dV_0 dh_0..dh_{n-1}. The inverse is
   V_{t+1} = h_t^-1 V_t, so the map is a bijection.
2. The density becomes prod_t f(h_t). Since int f = 1 it is already a
   probability density. So V_0 is Haar, the h_t are i.i.d. with density f,
   and they are independent of V_0.
3. V_t = h_{t-1}^-1 ... h_0^-1 V_0, so V_0 V_t^-1 = h_0 h_1 ... h_{t-1}.
   So D^j(V_0 V_t^-1) = D^j(h_0) ... D^j(h_{t-1}). By independence the mean
   is the product of the means.
4. Schur. For a class function f, the matrix M = int f(h) D^j(h) dh
   commutes with every D^j(g) (substitute h -> g h g^-1). So M = lambda 1,
   and (2j+1) lambda = int f chi_j. So lambda = c_j(f) as defined in step 3.
5. For the Wilson weight, c_j = I_{2j+1}(beta)/I_1(beta): with
   w = cos(theta) and Haar density (2/pi) sin^2(theta) on [0, pi],
   int e^{beta w} chi_j = I_{2j}(beta) - I_{2j+2}(beta)
   = (2(2j+1)/beta) I_{2j+1}(beta), and int e^{beta w} = (2/beta) I_1(beta).
   This also confirms D2 (L208).

**Verdict S2 (C1): HOLDS.** No gap found.

## S3. Step 3: C2 (leaf lemma); test 1 (mu periodic, nu free)

Statement (L292-313): free boundary in nu; measure
Z^-1 Psi(U') prod_{p || mu nu} f_p(U_p) prod dU, Psi >= 0 integrable in the
links U' not in direction mu. Then (a) the mu-nu plaquette variables are
independent with densities f_p and independent of U'; (b) U' has law
proportional to Psi(U') dU'.

Check (my own derivation).
1. A ladder is the set of mu-links M_k = U_mu(x + k e_nu), k = 0..L_nu, for
   one base point x with x_nu = 0. Its rails are b_k = U_nu(x + k e_nu) and
   a_k = U_nu(x + e_mu + k e_nu). Both rails are in U'.
2. Every mu-nu plaquette lies in exactly one ladder: the plaquette with
   mu-edges U_mu(y) and U_mu(y + e_nu) lies in the ladder of the base point
   y - y_nu e_nu, between levels y_nu and y_nu + 1. Different ladders have
   disjoint mu-links. A ladder has L_nu + 1 mu-links and L_nu plaquettes.
3. P_k = M_k a_k M_{k+1}^-1 b_k^-1 gives M_{k+1} = b_k^-1 P_k^-1 M_k a_k
   (I re-derived it). For fixed U' and M_k, the map P_k -> M_{k+1} is
   inversion and two translations, so it keeps Haar measure. Done in the
   order k = 0, 1, ..., this gives dM_0 ... dM_{L_nu} = dM_0 dP_0 ...
   dP_{L_nu - 1} for each fixed U' (Fubini, as in C1).
4. **Test 1.** If direction mu is periodic, the only change is that
   x + e_mu is read mod L_mu, so the rail a_k is another nu-link of U'.
   Steps 1-3 use only that U' is fixed and that the ladder is an open path
   in direction nu. Both stay true. Periodicity in mu never closes a ladder;
   only periodicity in nu does (that is C2'). The degenerate case L_mu = 1
   (a_k = b_k) is also covered. So test 1 passes.
5. In the new variables (U', M_0 of each ladder, all P) the density is
   Z^-1 Psi(U') prod_p f_p(P_p). It is a product, with int f_p = 1. This
   gives (a) and (b), and Z = int Psi dU'.
6. The plaquette variable is taken with the base point and orientation of
   P_k. A class function does not see the base point. The orientation is a
   convention of the measure; (a) holds for the same convention. For SU(2)
   every class function is also invariant under U -> U^-1.

**Guide run (refutes or guides only).** Script
`runs/gap-face-exercise-check-opus/c2_periodic_mu.py` (copied from scratch by the lead).
Group S_3; mu periodic with L_mu = 1, 1, 2; nu free with L_nu = 1, 2, 1;
a different weight on each plaquette; Psi a random positive function of all
nu-links. Exact enumeration of the joint law of (plaquettes, nu-links)
against prod f_p times Psi/sum(Psi): largest deviations 7.8e-16, 2.5e-16,
1.0e-15 (rounding). Not refuted.

**Verdict S3 (C2): HOLDS.** Test 1 passes (step 4).

## S4. Step 3: C2' (periodic ladder)

Statement (L315-327): with nu periodic of length L, each ladder gives the
factor 1 + sum_{j>=1/2} (prod_k c_j(f_k)) chi_j(A) chi_j(B), A and B the
nu-holonomies of the two rails; the factor is within
sum_{j>=1/2} (2j+1)^2 c_j^L of 1; "With all sides >= L and L -> infinity the
total effect is at most (1+5c_{1/2}^L)^{L^3}-1 -> 0".

Check of the formula (my own derivation).
1. Expand f_k = sum_j (2j+1) c_j(f_k) chi_j (c_0 = 1 since int f_k = 1).
2. Schur orthogonality gives int chi_j(X M^-1) chi_j'(M Y) dM =
   delta_jj' chi_j(XY)/(2j+1) (I re-derived it from
   int conj(D_ab) D'_cd = delta delta delta/(2j+1)). Integrating
   M_1, ..., M_{L-1} in turn forces one common j and leaves
   chi_j(M_0 A M_0^-1 B^-1) with A = a_0 a_1 ... a_{L-1} and
   B = b_0 b_1 ... b_{L-1}: the holonomies along the rails at x + e_mu and
   at x, in the right order.
3. int chi_j(M A M^-1 B^-1) dM = chi_j(A) chi_j(B^-1)/(2j+1). The powers of
   (2j+1) cancel: L from the expansion, L - 1 + 1 from the integrals. For
   SU(2), chi_j(B^-1) = chi_j(B). So the formula holds.
4. |chi_j| <= 2j+1 gives the bound sum_{j>=1/2} (2j+1)^2 prod_k c_j(f_k),
   which is the text's bound for equal weights.
5. Run 1 of row 1103 (`run1_leaf_s3.py`, S_3, L = 2, two different weights)
   tests exactly this formula; I read the script: it compares the ladder
   integral with sum_rho c_rho(f_0) c_rho(f_1) chi_rho(A) chi_rho(B^-1). Its
   output 1.1e-15 does not refute it.

Check of the "total effect" sentence.
6. The constant 5. sum_{j>=1/2} (2j+1)^2 c_j^L <= 5 c_{1/2}^L holds for L
   large (c_j <= c_1 < c_{1/2} for j >= 1, and sum_j (2j+1)^2 c_j < infinity).
   Guide run (`.../scratchpad/row1105/c2prime_bound.py`): in the window it
   fails at L = 1, 2 and holds for L = 3..7 at beta = 2.3, 2.4, 2.5, 2.6.
   The run also gives c_{1/2} = 0.4793, 0.4935, 0.5072, 0.5203 and
   c_1(2.5) = 0.1885, which agree with D2.
7. **Failing line:** "With all sides $\ge L$ and $L\to\infty$ the total
   effect is at most $(1+5c_{1/2}^L)^{L^3}-1\to0$." In a box with sides
   L_rho and V sites, the ladders of one orientation mu-nu number V/L_nu,
   each of length L_nu. So the product bound is
   (1 + 5 c_{1/2}^{L_nu})^{V/L_nu} - 1. It is (1+5c^L)^{L^3} - 1 only for a
   cubic box of side L, and for one orientation (the star has three leaf
   orientations, so 3L^3 ladders). For boxes with all sides >= L it need not
   tend to 0. Counterexample to the bound tending to 0: L_nu = L and the
   other three sides e^L. Then V/L_nu = e^{3L}, and
   e^{3L} c_{1/2}^L = (e^3 c_{1/2})^L -> infinity, since
   e^3 c_{1/2} > 9 in the window. This refutes the bound, not the
   smallness of local effects. Local effects are of the size of the
   interaction strength c_{1/2}^{L_nu}, but the text does not prove that.

**Verdict S4 (C2'): HOLDS AFTER CORRECTION.** The ladder formula and the
per-ladder bound hold. Corrected text for the last part: "In a box with sides
L_rho and V sites, the V/L_nu ladders of the orientation mu-nu have length
L_nu. For L_nu >= L_1(beta) (L_1 = 3 in the window, guide) each factor is
within 5 c_{1/2}^{L_nu} of 1, so their product is within
(1+5c_{1/2}^{L_nu})^{V/L_nu} - 1 of 1. For cubic boxes of side L this is
(1+5c_{1/2}^L)^{L^3} - 1 -> 0 per orientation. It does not tend to 0 for
every family with all sides >= L (L_nu = L with the other sides e^L is a
counterexample). For such boxes a reduction of the periodic box to C2 needs a
local argument, for example an expansion in the Polyakov-line interaction of
strength about c_{1/2}^{L_nu}; that argument is not written." T asks for all
boxes with every side >= L_0, so this correction matters wherever C2' is
used to carry C4 to periodic boxes (C11 uses "up to the terms of C2'").

## S5. Step 3: C3 (forest faces)

Statement (L329-339): E a forest, free boundary; then the plaquette
variables with orientation in E are independent, each with its own weight;
links in a direction in no plane of E are independent Haar; any compact
group.

Check (my own derivation).
1. The model is prod_{p: o(p) in E} f_p(U_p) prod dU; orientations not in E
   carry no factor.
2. Induction on |E|. Base E empty: all links are independent Haar.
3. A forest with an edge has a vertex mu of degree 1 with one neighbour nu.
   The mu-links occur only in mu-nu plaquettes, and the other factors (the
   orientations of E \ {mu nu}) contain no mu-link. The boundary is free in
   nu. So C2 applies with Psi = that product of factors.
4. C2(a): the mu-nu plaquettes are independent, with densities f_p, and
   independent of U'. C2(b): U' has the law of the E \ {mu nu} model on the
   links not in direction mu. C2 does not need the links of every direction
   to be present, so the next step of the induction applies C2 to this
   smaller model. E \ {mu nu} is a forest.
5. Combining (the plaquettes of E \ {mu nu} are functions of U') gives the
   joint independence of all E-plaquettes. A direction in no plane of E
   stays isolated at every step; its links stay in U' and are Haar by
   induction.
6. Group: C2 uses only that Haar measure is invariant under inversion and
   translations (compact groups are unimodular). It does not use the class
   property of f_p. So "every compact group, U(1) included" holds.
7. Remark (not a correction): the proof gives a little more. At the end,
   one direction of each tree (the last one left) keeps Haar links,
   independent of all plaquettes. For the star this is direction 4. This is
   what C4 uses.

**Verdict S5 (C3): HOLDS.**

## S6. Step 3: C4 (star face and its rate); test 2

Statement (L341-364): E = {14, 24, 34} with weight f, free boundary in
direction 4; for gauge-invariant local A, B separated by T steps in
direction 4, |<A;B>| <= ||A||_2 ||B||_2 c_{1/2}(f)^{4T}; zero if the
spatial supports are disjoint; rate 4(-log c_{1/2}(beta_t)) = 2.94, 2.82,
2.72, 2.61.

Check (my own derivation).
1. Temporal gauge. Direction 4 is open, so g_{x,0} = 1,
   g_{x,t+1} = g_{x,t} U_4(x,t) sets U_4 = 1 with no constraint. For fixed
   temporal links the induced map on spatial links keeps Haar measure, so
   gauge-invariant expectations can be computed with U_4 = 1. In that gauge
   a 14-plaquette is U_1(x,t) U_1(x,t+1)^-1. With no 12, 13, 23 plaquettes
   the measure is prod_l prod_t f(U_l(t) U_l(t+1)^-1) prod dU: one C1 chain
   per spatial link position l, all independent. Correct.
2. One-step operator. (K_l phi)(u) = int f(p) phi(p^-1 u) dp. On matrix
   entries, K_l D^j = [int f(p) D^j(p^-1) dp] D^j = c_j(f) D^j, since for
   SU(2) a class function has f(p^-1) = f(p). K is self-adjoint on
   L^2(Haar) and diagonal on the Peter-Weyl basis, with eigenvalue
   prod_l c_{j_l}(f) on the label (j_l). Correct.
3. Markov step. With t_1 the last slice of A and t_2 = t_1 + T the first
   slice of B, <AB> = E[ E[A|U(t_1)] E[B|U(t_1)] ] and
   E[B|U(t_1)] = K^T b, b = E[B|U(t_2)]. The chain is stationary (Haar
   start) and reversible. So <A;B> = <a - abar, K^T (b - bbar)>, and
   ||a - abar||_2 <= ||A||_2. Correct.
4. **Test 2, first part.** The law of the chain is invariant under
   time-independent gauge maps u_l -> g_x u_l g_y^-1 (the increments are
   conjugated, f is a class function, Haar is invariant). So a and b are
   invariant functions of one slice. Each label space
   H_(j) = span of tensor products of D^{j_l} entries is mapped into itself
   by the gauge group, so the projection onto invariants acts label by
   label. In H_(j), the site x carries the tensor product of the spaces
   V_{j_l} (or duals) of the incident links with j_l != 0. If exactly one
   such link meets x, that factor is one non-trivial irreducible
   representation, which has no non-zero invariant vector. So an invariant
   function orthogonal to the constants has components only on labels whose
   support has no degree-1 site. **This step HOLDS.**
5. A finite non-empty graph with all degrees >= 2 has a cycle. Correct.
   "Cycles of the cubic lattice have at least 4 links" needs a hypothesis:
   the spatial directions are free, or periodic with side >= 4. A periodic
   spatial side of length 3 has a cycle of 3 links (a Polyakov loop), side
   2 has a 2-cycle, side 1 a self-loop (V_j tensor V_j* has an invariant).
   C4 states no condition on the spatial sides.
6. **Test 2, second part: c_j <= c_{1/2}.**
   - For the Wilson weight with beta > 0 it HOLDS. Proof (mine): with
     g = I_nu - I_{nu+1}, the recurrences I_nu' = I_{nu+1} + (nu/x) I_nu and
     I_{nu+1}' = I_nu - ((nu+1)/x) I_{nu+1} give
     g' + g = (nu I_nu + (nu+1) I_{nu+1})/x > 0 for nu >= 0, x > 0. So
     e^x g(x) is increasing, and it tends to g(0+) >= 0. So
     I_{nu+1}(x) < I_nu(x), and 1 > c_{1/2} > c_1 > ... > 0.
   - For a general weight it FAILS. Counterexample: f = 1 + 0.9 chi_1. It
     is a positive continuous class function (chi_1 >= -1, so f >= 0.1)
     with int f = 1, c_{1/2}(f) = 0, c_1(f) = 0.3, all other c_j = 0
     (orthogonality; guide quadrature `.../scratchpad/row1105/c4_weight.py`
     agrees). Take a spatial plaquette s and A = chi_1(U_s(0)),
     B = chi_1(U_s(T)). At one time the spatial links are i.i.d. Haar, so
     U_s(0) is Haar: <A> = 0, ||A||_2 = 1. U_l(T) = Q_l U_l(0) with
     E D^1(Q_l) = E D^1(Q_l^-1) = c_1^T 1, independent over l. So
     E[B | U(0)] = c_1^{4T} A and <A;B> = 0.3^{4T} > 0, while the stated
     bound is ||A|| ||B|| c_{1/2}(f)^{4T} = 0.
   C4 is stated for "weight f ... (for example Wilson at any beta_t)", so
   its first line fails as written; the Wilson case is right.
7. Disjoint spatial supports: in temporal gauge A and B are functions of
   disjoint sets of independent chains, so <A;B> = 0. Correct.
8. Rates: -4 log c_{1/2} = 2.942, 2.825, 2.715, 2.613 at 2.3, 2.4, 2.5,
   2.6 (c_{1/2} from S4 step 6). Correct. The rate is sharp:
   A = chi_{1/2}(U_s(0)), B = chi_{1/2}(U_s(T)) gives <A;B> = c_{1/2}^{4T}.
   For a translation with a large spatial part the supports become disjoint
   and the correlation is 0, so the bound holds in every direction, up to a
   constant, uniformly in the box.

**Verdict S6 (C4): HOLDS AFTER CORRECTION.** First failing line: "Let
$E=\{14,24,34\}$ with weight $f$ ... $|\langle A;B\rangle|\le\|A\|_2\|B\|_2\,c_{1/2}(f)^{4T}$"
(fails for f = 1 + 0.9 chi_1, step 6). Corrected text: "Let E = {14,24,34}
with weight f, free boundary in direction 4, and spatial directions free or
periodic with every side >= 4. Put rho(f) = sup_{j>=1/2} |c_j(f)| (< 1).
Then |<A;B>| <= ||A||_2 ||B||_2 rho(f)^{4T}. For the Wilson weight at
beta_t >= 0, rho = c_{1/2}(beta_t), since I_{nu+1} < I_nu; the rate
4(-log c_{1/2}(beta_t)) is then sharp." The use in the run (Wilson weight)
is not affected.

## S7. Step 3: C5(a) (the face beta_14 = beta_24 = beta_34 = infinity)

Statement (L367-370): free boundary in 4; in the gauge U_4 = 1 all time
slices are equal; so <A; tau_{t e_4} A> = Var A for all t: rate 0; T-analog
false.

Check (my own derivation).
1. Temporal gauge is valid (open direction 4; S6 step 1). A frozen
   i4-plaquette (i = 1, 2, 3) in that gauge is U_i(x,t) U_i(x,t+1)^-1 = 1.
   So U(t) = U(0) for every t. Correct.
2. If A and tau_{t e_4} A both lie in the box, then in this gauge both are
   the same function of U(0). So tau_{t e_4} A = A almost surely and
   <A; tau_{t e_4} A> = Var A. Correct.
3. **Gap in the conclusion.** The text does not fix the spatial couplings
   beta_12, beta_13, beta_23. Var A is taken in the law of the one slice
   U(0). Since all L_4 + 1 slices are equal, every spatial plaquette weight
   enters L_4 + 1 times: the slice law is the 3D model with couplings
   (L_4 + 1) beta_ij. So Var A depends on the box, and for positive spatial
   couplings it tends to 0 as L_4 -> infinity. "Rate 0" at one fixed box
   does not by itself refute a bound C e^{-m t} that is uniform in boxes.
4. Repair. (i) If beta_12 = beta_13 = beta_23 = 0, the slice law is Haar
   and Var A is a fixed positive number (A = w(U_p) for a spatial
   plaquette p: Var = 1/4 under Haar). Then the T-analog is false at once.
   (ii) If they are positive, the T-analog is still false provided Var A
   decays at most polynomially in L_4: take t near L_4. A one-link
   conditioning bound gives this for A = w(U_p) (sketch, mine, not written
   in full): given all other links, the link l of p has density
   proportional to exp(kappa (1/2) tr(U_l V)) with V in SU(2) and
   kappa <= 4 (L_4 + 1) max beta_ij (four spatial plaquettes meet at l in
   3D), and A is a linear function x.n of the unit quaternion x = U_l V.
   Its conditional variance under that von Mises-Fisher law on S^3 is at
   least c min(1, kappa^-2). So Var A >= c'/(L_4 beta_s)^2.

**Verdict S7 (C5(a)): HOLDS AFTER CORRECTION.** First failing line: "So
$\langle A;\tau_{te_4}A\rangle=\operatorname{Var}A$ for all $t$: rate 0.
T-analog false." (Var A depends on the box and tends to 0 when the spatial
couplings are positive.) Corrected text: "In the gauge U_4 = 1 all time
slices are equal, and the slice law is the 3D model with couplings
(L_4+1) beta_ij. So <A; tau_{t e_4} A> = Var_Lambda A for every t that keeps
both supports in the box. If the spatial couplings are 0, Var A does not
depend on the box and the T-analog is false. If they are positive,
Var_Lambda A -> 0 as L_4 -> infinity, but only polynomially (for a plaquette
observable, Var >= c/(L_4 beta_s)^2 by conditioning on one link; sketch),
so the T-analog is again false." Mark: the case of zero spatial couplings is
argued in full; the polynomial lower bound is a sketch.

## S8. Step 3: C6 (classification of the corner models)

Statement (L392-408): couplings each 0 or finite; leaf orientations are
integrated out by C2; what remains is the 2-core of E; the table of the
graphs on four vertices; "the proved corners are exactly the forests"; the
spanning trees are 4 stars and 12 paths, three orientations on, three off.

Check (my own derivation).
1. The graphs on four vertices up to relabelling are eleven: 0 edges (1);
   1 edge (1); 2 edges, adjacent or disjoint (2); 3 edges: triangle plus an
   isolated vertex, star K_{1,3}, path P_4 (3; P_3 plus a disjoint edge
   needs five vertices); 4 edges: complement of two adjacent edges = paw
   (triangle plus pendant edge), complement of two disjoint edges = C_4
   (2); 5 edges: K_4 minus an edge (1); 6 edges: K_4 (1). Total 11. The
   table lists all eleven. Correct.
2. 2-cores: the six forests -> empty; triangle and paw -> triangle; C_4,
   K_4 minus an edge (degrees 3, 3, 2, 2) and K_4 -> themselves. Correct.
3. Leaf removal by C2: as in S5, each step needs only free boundary in the
   neighbour direction and that the leaf's links occur in one orientation.
   Correct.
4. "What the model is": forests -> independent plaquettes (C3, holds).
   Triangle {12,13,23}: direction 4 is in no plane, so its links are Haar
   and the slices x_4 = const are independent 3D gauge theories (holds);
   paw: the same after the pendant leaf is removed (holds). C_4
   {12,23,34,41}: the missing planes are 13 and 24 (holds).
5. **Failing line (C_4 row):** "its closed surfaces are products of a loop
   in the 13-plane with a loop in the 24-plane". By C15 (with A = 13-plane,
   B = 24-plane) the closed surfaces mod 2 are the **sums** of products
   dP x dQ, not single products. Counterexample: two unit hypercubes
   dP1 x dQ1 and dP2 x dQ2 with P1, P2 sharing an edge e and Q1, Q2 sharing
   an edge f. Their sum has 16 + 16 - 2 = 30 plaquettes (they share only
   e x f). A product of a loop of length a with a loop of length b has ab
   plaquettes, and loops of the square lattice have even length >= 4, so
   ab is a multiple of 4; 30 is not. Run 2 of row 1103 found area 30, and
   the writer checked it by hand (L1284-1285).
6. **Forest row, gap column:** "proved, all finite couplings (C3, C4)". C3
   gives independent plaquettes for every forest. The clustering bound
   (the T-analog) is written only for the star, and C4 says "Other forests
   are handled the same way (not written out here)". So "proved" holds for
   the star (Wilson weight, C4 as corrected in S6) and trivially for the
   empty graph. For the other forests it is argued, not written. I did not
   prove it either. I found no counterexample: in the forests I tried by
   hand (one edge; {12, 34}) a gauge-invariant local observable that meets
   a Haar link only once has mean zero against everything else.
7. "K_4 minus an edge ... at least as hard as N5": it contains the triangle
   model as a sub-face (set the two other couplings to 0). "At least as
   hard" is a reading, not a theorem: a gap proof at positive couplings of
   the five orientations would not by itself give the triangle model.
8. Spanning trees of K_4: 4^{4-2} = 16 (Cayley) = 4 stars + 12 paths
   (4!/2). Each has three edges. Correct.

**Verdict S8 (C6): HOLDS AFTER CORRECTION.** Corrected text of the C_4 row:
"a model with planes 13 and 24 missing; its closed surfaces mod 2 are the
finite sums of products dP x dQ of a unit square boundary in the 13-plane and
one in the 24-plane (C15); not every closed surface is one product (area 30)."
Corrected text of the forest row: "independent plaquettes (C3) for every
forest; gap proved for the star (C4); for the other forests argued 'the same
way', not written." The rest of C6 (the eleven graphs, the 2-cores, the leaf
reduction, the spanning-tree count) holds. "At least as hard as N5" is a
reading.

## S9. Step 3: C7 (at most half of the plaquettes); test 5

Statement (L410-420): K a set of plaquettes of a periodic box with V sites,
no non-empty subset closed mod 2; then |K| <= 3V - 3; proof by
rank d_2 = dim Z_1 - dim H_1 = (4V - (V-1)) - 4.

Check (my own derivation).
1. "No non-empty subset of K is closed mod 2" is the same as: the vectors
   dp, p in K, are linearly independent over F_2. So |K| <= rank d_2.
2. **Test 5 (rank on a torus).** The periodic box with its unit cells is a
   CW structure on the 4-torus T^4 for every side length >= 1. (Side 2 gives
   two distinct edges between the same two sites; side 1 gives an edge from
   a site to itself, with CW boundary 0 mod 2.) Over F_2: dim C_0 = V,
   dim C_1 = 4V, dim C_2 = 6V. H_0 = F_2, so rank d_1 = V - 1 and
   dim Z_1 = 3V + 1. H_1(T^4; F_2) = F_2^4, so
   rank d_2 = dim B_1 = 3V + 1 - 4 = 3V - 3. **Holds.**
3. Guide run (`.../scratchpad/row1105/c7_rank.py`): exact F_2 rank for
   sides (3,3,3,3), (2,2,2,2), (1,2,3,4), (4,3,3,2), (1,1,1,1), (2,3,5,1):
   240, 45, 69, 213, 0, 87, equal to 3V - 3 in all six cases.
4. "Spanning-tree faces reach 3V up to boundary terms": in a free box a
   spanning-tree face is a forest face, with no closed surface (C3). In a
   periodic box it has 3V plaquettes, but it contains closed surfaces: for
   the star, all 14-plaquettes at fixed (x_2, x_3) form a closed 2-torus,
   and likewise for 24 and 34. So at least L_2 L_3 + L_1 L_3 + L_1 L_2
   plaquettes must go. That is the "boundary term"; it is o(V) for boxes
   with all sides large. Holds as a loose statement.
5. The remark "a closed surface carries a non-trivial term of the character
   expansion", used to say that an independent-plaquette end-point must
   avoid closed surfaces: for Z_2 it is exact (the product of the plaquette
   variables of a mod-2 cycle is 1, a deterministic relation). C3 is
   group-blind, so a group-blind independence statement must avoid closed
   surfaces. For SU(2) alone it is a character-expansion heuristic, not
   proved in the file. This does not change the bound.

**Verdict S9 (C7): HOLDS.** (The SU(2)-only form of the remark in step 5 is
a heuristic; the bound and its group-blind use hold.)

## S10. Section 7.1: C14 (stiff faces); test 3

Statement (L1017-1047): couplings in (0, infinity], none zero, free
boundary; F = frozen orientations. (a) two frozen orientations mu-nu, mu-rho
with nu-rho not frozen give <A; tau_{t e_mu} A> = Var A > 0 for all t, rate
0 in direction mu. (b) every F with |F| >= 3, and every pair sharing a
direction, falls under (a), except the triangle (3D O(4) per layer: ordered
above 1.0109, THM given FSS; rate 0: BELIEF) and F = all six (trivial).
(c) so the only frozen sets that can carry a positive rate in every
direction are one orientation and the two opposite orientations {12, 34}.

**Test 3(a): gauge fixing and positive variance.**
1. Direction mu is free, so U_mu = 1 can be reached (S6 step 1). In that
   gauge a frozen mu-nu plaquette is U_nu(x + e_mu) U_nu(x)^-1 = 1, so
   U_nu does not depend on x_mu; the same for U_rho. The nu-rho plaquette
   uses only U_nu, U_rho at one value of x_mu. So for A = w(U_p) (gauge
   invariant; the plaquette matrix itself is only conjugated)
   tau_{t e_mu} A = A almost surely in this gauge, hence in every gauge.
   **The gauge-fixing step holds.**
2. Positive variance at one fixed box holds: beta_nu-rho is finite, and the
   law of A has a density. But, as in C5(a) (S7), the nu-rho plaquettes at
   the L_mu + 1 values of x_mu are now equal, so their weight enters
   L_mu + 1 times: the effective coupling is (L_mu + 1) beta_nu-rho. So
   Var_Lambda A -> 0 as L_mu -> infinity. "Var A > 0 for all t: the rate in
   direction mu is 0" is right in each box, but uniform failure of the
   T-analog needs Var_Lambda A not exponentially small in L_mu. The
   one-link conditioning sketch of S7 step 4 gives Var >= c/L_mu^2 (the
   column of equal nu-links is one quaternion with concentration
   <= (L_mu + 1) times a sum of couplings). So (a) holds after the same
   correction as C5(a).

**Test 3(b): the eleven graphs.** "Falls under (a)" means: some vertex has
two frozen edges whose third side is not frozen (an open wedge).
| F (up to relabelling) | open wedge? | case |
|---|---|---|
| empty | no | not a face at infinity |
| one edge | no | left for (c) |
| two adjacent edges {mu nu, mu rho} | yes, at mu | (a) |
| two disjoint edges {12, 34} | no (no vertex has two edges) | left for (c) |
| triangle | no (every wedge closes) | exception (b) |
| star {14, 24, 34} | yes, at 4 (12 not frozen) | (a) |
| path {12, 23, 34} | yes, at 2 (13 not frozen) | (a) |
| paw {12, 13, 23, 14} | yes, at 1 (24 not frozen) | (a) |
| C_4 {12, 23, 34, 14} | yes, at 1 (24 not frozen) | (a) |
| K_4 minus 34 | yes, at 1: 13, 14 (34 not frozen) | (a) |
| K_4 | no | exception (trivial) |
A graph has no open wedge if and only if it is a disjoint union of cliques;
on four vertices with >= 3 edges these are only the triangle and K_4.
**(b) holds.**

**Is the frozen triangle marked correctly?** In the gauge where the frozen
3D slices are 1 (free boundary), each sigma-layer is a 3D O(4) model with
couplings beta_{i sigma} u_{x+e_i} . u_x (unit quaternions; I re-derived
it). 1.0109 is the infrared-bound threshold (N/2) W_3 = 2 x 0.505462
(Watson's integral for Z^3) for O(4) with coupling beta sigma.sigma; so
"ordered above 1.0109, THM given Frohlich-Simon-Spencer" is right for equal
couplings. "Rate 0 for invariant observables" (Goldstone modes) is not
proved; it is marked BELIEF, which is right. The block header "exact except
the triangle case" and Attempt 1 ("the triangle case rests on a BELIEF")
agree.

**(c) fails as worded.** First failing line: "So the only frozen sets that
can carry a positive rate in every direction are: **one orientation** (the
lane's face) and **two opposite orientations**". C14 ranges over all
couplings in (0, infinity]. Counterexample: F = the triangle {12, 13, 23}
with small finite beta_14 = beta_24 = beta_34. Then each layer is a 3D O(4)
model at high temperature, which has exponential decay of correlations (a
convergent high-temperature expansion; THM, standard), and different layers
are independent. So this F carries a positive rate in every direction. Also
F = all six carries one trivially (all gauge-invariant observables are
constant); (b) sets it aside, (c) omits it.

**Verdict S10 (C14): HOLDS AFTER CORRECTION.** (a): add the box dependence
of Var A as in S7. (b): holds. Corrected (c): "With the non-frozen
couplings at window size (more generally, large enough that the 3D O(4)
layers of the frozen triangle are ordered; >= 1.0109 for equal couplings by
the infrared bound), and given the BELIEF that the ordered 3D O(4) model has
no gap for invariant observables, the only frozen sets other than the empty
set and the trivial F = all six that can carry a positive rate in every
direction are one orientation and two opposite orientations. For small
non-frozen couplings the frozen triangle also carries a positive rate."
Not checked here: the closing paragraph ("Faces with some couplings zero
add nothing stiff"; the proved stiff points "given N4c"), which rests on
N4c (a preprint, unchecked) and on the lane's word "stiff".

## S11. Section 7.2: C15 (closed surfaces of the mixed-only corner); test 4

Statement (L1069-1095): A = Z^2 (directions 1, 2), B = Z^2 (directions
3, 4); a finite set S of mixed plaquettes e x f is closed mod 2 iff
S = sum over (P,Q) in T of dP (x) dQ for a unique finite set T of pairs of
unit squares; area formula |S| = sum over adjacent P ~ P' of
per_B(phi(P) symdiff phi(P')); every non-empty closed mixed surface has at
least 16 plaquettes; equality only for single hypercube shells, which are
tori.

Check (my own derivation).
1. Boundary of e x f mod 2 is (de) x f + e x (df). So the coefficient of
   the link e x {b} in dS is (d_B row_e)(b), and that of {a} x f is
   (d_A column_f)(a). So S is closed iff every row is a cycle of B and every
   column a cycle of A. Correct.
2. **Test 4, first part.** Finitely supported 0-1 matrices on
   E_A x E_B are the algebraic tensor product X (x) Y, X = F_2[E_A],
   Y = F_2[E_B]. "All rows in W" is the subspace X (x) W (write
   M = sum_e e (x) row_e, a finite sum), and "all columns in V" is
   V (x) Y. For subspaces V of X and W of Y, (X (x) W) cap (V (x) Y) =
   V (x) W: choose complements X = V + V', Y = W + W'; then X (x) Y splits
   into four parts, X (x) W = VW + V'W and V (x) Y = VW + VW', and the
   intersection is VW. Finite support makes all sums finite. **Holds.**
3. **Test 4, second part (basis).** V = finite cycles of Z^2.
   Spanning: every finite cycle z is the boundary of the finite set of
   squares whose centre sees z an odd number of times along a ray to
   infinity (parity argument; the set is finite because squares outside a
   box around supp z have a ray that misses z); equivalently
   H_1(R^2; F_2) = 0 with finite cellular chains. Independence: a
   non-empty finite set R of squares has a boundary edge (the top edge of
   its highest square, leftmost among the highest, is in no other square
   of R), so dR != 0. So {dP} is a basis of V, likewise {dQ} of W, and
   {dP (x) dQ} is a basis of V (x) W. Uniqueness of T follows. **Holds.**
4. dP (x) dQ is the set of the 16 mixed plaquettes of the hypercube P x Q
   (4 edges of dP times 4 edges of dQ). Each of its links (edge of P times
   vertex of Q, or vertex of P times edge of Q) lies in exactly two of
   them; vertices 16, links 32, faces 16, Euler characteristic 0; it is
   (dP) x (dQ) = S^1 x S^1. Correct.
5. Area formula: S = sum_P dP (x) d_B phi(P). Each edge e of A lies in
   exactly two squares P, P'; so row_e = d_B(phi(P) + phi(P')) and
   |row_e| = per_B(phi(P) symdiff phi(P')). Summing over e gives the
   formula. Correct.
6. Lower bound 16: S != 0 has a non-zero column, a non-zero cycle of A with
   >= 4 edges, so >= 4 non-zero rows, each a non-zero cycle of B with >= 4
   edges. If |S| = 16: exactly 4 non-zero rows and 4 non-zero columns,
   each with exactly 4 ones; a 4-edge non-zero cycle of Z^2 is a unit
   square boundary; the 16 ones fill a 4 x 4 block, so S = dP (x) dQ.
   Correct.
7. Run 2 (I read the script and output): two 3 x 3 site grids, 144 mixed
   plaquettes, 216 links, rank 128, kernel 16 = 4 x 4 = dim V (x) W (each
   grid has dim Z_1 = 12 - 9 + 1 = 4). Area counts 16: 16; 24: 32
   (4 dominoes x 4 squares, both ways); 30: 32 (4 x 4 adjacent pairs, two
   pairings). These counts match my hand counts. Guide only.
8. Scope remark (not a correction of C15): C15 is for Z^2 x Z^2. In a
   periodic box each torus factor has H_1 = F_2^2, so non-contractible
   products (gamma x delta with gamma, delta winding loops, area L_a L_b)
   are extra closed surfaces, and the minimum area becomes
   min(4, L_1, L_2) x min(4, L_3, L_4). This matters for S12.

**Verdict S11 (C15): HOLDS.** Test 4 passes in both parts.

## S12. Step 8: the reduction "(F4-KP) gives the T-analog at the corner"

Statement (L1248-1261): polymers are "the connected closed mixed surfaces
gamma with a non-trivial SU(2) representation on each plaquette and an
intertwiner at each link", with the activities w(gamma) of the character
expansion of W(beta_12 = beta_34 = 0; four mixed at beta). (F4-KP): some
a > 0 has sup_p sum_{gamma ni p} |w(gamma)| e^{a|gamma|} <= a. "Given
(F4-KP), the standard convergence theorem ... gives a unique limit state, and
exponential clustering of gauge-invariant local observables with a rate that
does not depend on the volume."

Check (my own derivation).
1. The logic "convergent polymer expansion -> unique limit, volume-uniform
   exponential clustering of bounded gauge-invariant local observables" is
   the standard strong-coupling route (Osterwalder-Seiler; Seiler LNP 159),
   with the observables inserted as sources. It holds if the polymer system
   is exactly the character expansion and the KP hypothesis is met in the
   right form. Three points fail that test as written.
2. **Failing line: the polymer set.** For SU(2), a labelled support has a
   non-zero link integral iff at each link the spins admit an invariant.
   Since -1 acts by (-1)^{2 sum j}, the plaquettes with half-integer spin
   form a mod-2 cycle (so C15 governs that part). Plaquettes with integer
   spin need not: (1,1,1) at a link has an invariant. Counterexample to
   "closed" in the mod-2 sense of C15: P1, P2 adjacent squares of A sharing
   the edge e0, Q a square of B, and the support
   (dP1 union dP2) x dQ = 7 x 4 = 28 mixed plaquettes, all with spin 1. It
   is three cylinders (theta graph times a circle) glued along the two
   circles {a} x dQ, a an end of e0; the links on those circles lie in 3
   plaquettes, so the support is not closed mod 2. Its activity is not 0:
   integrating the links inside each cylinder gives a positive constant times
   chi_1(H1) chi_1(H2) (C2' gluing), H1, H2 the circle holonomies; each is
   Haar, and int chi_1^3 = 1 (V_1 tensor V_1 tensor V_1 has a 1-dimensional
   invariant). So "closed mixed surfaces" must read: link-connected sets of
   mixed plaquettes with spins j_p >= 1/2 such that every link integral is
   non-zero (no free link; half-integer part closed mod 2). The 16-plaquette
   minimum and the torus case still hold for this wider set (each non-empty
   row and column has all degrees >= 2, so it contains a cycle; the S11
   step 6 count goes through).
3. **KP form.** Polymers interact when they share a link, not only a
   plaquette. A polymer gamma has at most 2|gamma| links (each link of a
   polymer lies in >= 2 of its plaquettes), and each link lies in 4 mixed
   plaquettes. So the per-plaquette bound gives
   sum over gamma' meeting gamma of |w| e^{a|gamma'|} <= 8 |gamma| x (the
   per-plaquette sum). The KP hypothesis with a(gamma) = a|gamma| then
   needs the per-plaquette sum <= a/8, not <= a. ("There is a > 0" does not
   absorb the 8 in general.)
4. **Boxes.** T asks for periodic boxes with every side >= L_0. There, extra
   polymers wind around the torus (S11 step 8). (F4-KP) must hold on each
   such torus, with winding polymers, uniformly in the sides; for sides >= 4
   their areas are >= 16. This is standard but must be stated.
5. **Rate.** KP gives some positive rate that does not depend on the
   volume. "Rate close to 4(-log c_{1/2})" (route F4, L1108-1109; step 8
   item 1) is not implied by KP alone. The tube dP x (path of length t in
   B), capped by two 12-plaquette observables, gives a term c_{1/2}^{4t};
   so 4(-log c_{1/2}) is the expected leading rate, but that is a reading.

**Verdict S12: HOLDS AFTER CORRECTION.** Corrected text: "(F4-KP). Let
beta <= 2.6. Polymers: link-connected sets gamma of mixed plaquettes with
spins j_p >= 1/2 whose SU(2) link integrals are all non-zero (equivalently:
no free link, the half-integer part closed mod 2, admissible spins at every
link), with the activities w(gamma) of the character expansion; two polymers
are compatible iff they share no link. Then there is a > 0 with
sup_p sum_{gamma ni p} |w(gamma)| e^{a|gamma|} <= a/8, on Z^4 and on every
periodic box with all sides >= 4 (winding polymers included). Given this,
the Kotecky-Preiss theorem and the standard source argument give a unique
limit state and exponential clustering of bounded gauge-invariant local
observables with a positive rate that does not depend on the box." Note for
W3: the entropy count must include integer-spin decorations, not only the
contour model of C15.

## S13. Test 6: search of `main` and the open PR branches

Method. Clone `~/ym4d-lead/clone` (shallow, blob-less partial clone).
`origin/main` fetched 2026-11-17: still `8b11ae2bb` (2026-11-15). Main has
93,292 files; the note folders `docs`, `research`, `formalization`,
`.claude/science` hold 12,898 `.md`, 1,190 `.txt` and 2,077 `.py` files
(the other files there are `.gz`, `.json` and logs). Plan: fetch the blobs
of those `.md`, `.txt`, `.py` files in one batch into the clone, then
`git grep` on `origin/main`. Open PRs: 18 (from `gh pr list`); for each, the
files that differ from `origin/main` at the PR head, searched with
`git grep` at the PR head commit.

**Main, done.** Blobs of all 15,211 `.md`/`.txt`/`.py` files of the four
note folders fetched into the clone in one batch (the `.git` grew from 108 MB
to 168 MB); every search below ran with `GIT_NO_LAZY_FETCH=1` on
`origin/main` = `8b11ae2bb`, case-insensitive, over `docs`, `research`,
`formalization`, `.claude/science` (`.md`, `.txt`). Files with a hit:
| Pattern | Files | Relevant? |
|---|---|---|
| 2-core / two-core | 1 | no (a combinatorics note on cycle letters) |
| forest face / forest corner; leaf lemma; spanning-tree face; independent plaquettes; four-cycle corner/face | 0 | - |
| 3V - 3 | 1 | **yes, in part**: `docs/FINITE_CLOCK_DIRECT_MAXWELL_SCALING_AND_COULOMB_WILSON_INTERACTIONS_BOUNDED_THEOREM_NOTE_2026-09-14.md` L89 states, on T_L = (Z/LZ)^4 (L even >= 4), r = dim im_R d_1 = 3V - 3 (6V plaquettes, 4V edges), from the Fourier symbol. That is the real-coefficient form of the rank count of C7. The use in C7 (F_2 coefficients; at most half of the plaquettes free of closed surfaces) is not there. |
| closed surface(s) mod 2 / closed mod 2 | 0 | - |
| closed surface | 18 | no new statement: generic character-expansion facts (e.g. the gluing rule in `research/mass-gap/library/gap-seed-sc-check.md` L27; Z_2 / U(1) remarks in `research/mass-gap/library/gap-skeleton-max-b.md`) |
| stiff face / end-point; frozen orientation / plane; doubly flat | 0 | - |
| mixed plaquettes only / mixed-only; mixed surface | 1 + 1 | no (an orientation factor of electric/magnetic signs; a scale-comparator meta note) |
| hypercube shell; dP (x) dQ | 0 | - |
| Kunneth / Künneth | 2 | no (a Picard-Fuchs citation note; a Hodge-Laplacian remark in `research/mass-gap/library/gap-transport-check.md`) |
| (0, beta, 0); beta_L = beta_T = 0; beta_L = 0; beta_T = 0; (beta_L, beta_M, beta_T); beta_12 = beta_34 = 0 | 0 | - |
| star face / K_{1,3}; spanning tree near plaquette | 2; 3 | no (graph-census panel; spanning-tree gauge fixing remarks) |
| plane-dependent / anisotropic coupling | 7 | no (condensed-matter notes; a 5D anisotropic SU(2) literature entry in `research/mass-gap/library/prior/gap-tests-lit.md` L23) |

**Open PRs, done.** 18 open PRs (`gh pr list`, 2026-11-17): 9865, 9868,
10114, 10124, 10126, 10127, 10128, 10129, 10131, 10132, 10133, 10134,
10135, 10139, 10140, 10147, 10170, 10171. Each head fetched with depth 1
(`refs/pull/N/head`). For each, the `.md`/`.txt`/`.py` files added or
changed against `origin/main` (tree diff; 10 to 2,998 files per PR) were
fetched in one batch (5,659 blobs; `.git` now 204 MB) and searched with
`git grep` at the head, with the same patterns in six groups. In PR #10132
I left out `FINISH.md`, the row 1103 file, its runs, this file and the row
1106 check file. Hits:
- #10114 and #10133 (`.claude/science/toe-ruleset-20261021/agents/ym4d-existence/EXISTENCE.md`
  L3301; `checks/x7_criteria.md` L16): the mean diagonal of a projector,
  "(3V - 3)/(6V) untwisted and 1/2 twisted". This is again the
  real-coefficient rank 3V - 3 of the plaquette map on the 4-torus (and
  3V with a twist). It is the count used in C7, not the C7 conclusion.
- #10132 (the lane branch, head `5f85495a3d4a`; the row 1103 file and its
  runs are unchanged from `0bdd62338`): `library/prior/gap-mixed-corner-read-luna.md`
  (row W2, gpt-6-luna, written after row 1103). I read only its first 12
  lines and its RESULT line: "No published result for the
  four-mixed-orientation SU(2) corner was found in this bounded search"; it
  calls the C15 basis the Kunneth tensor product of the 1-cycles of the
  factors, and says F4-KP remains open. Also `library/gap-wall-vectors-max.md`
  6.8 (the doubly flat corner remark that C14 cites) and
  `library/gap-bridge-vectors-max.md` L357 (sheets at beta_T = 0); row 1103
  already used both. The other hits (forest, leaf, Kunneth, "mixed
  plaquettes only") are other uses of the words.
- #10114, #10126, #10133, #10135: "four-cycle" only, in unrelated graph
  counts. #10114, #10133: "2-core" and Kunneth hits in unrelated contexts.
- No other PR has a hit.

**Result S13.** On `main` and in the 18 open PRs I found no statement of
C6 (the 2-core classification of the corners), C14 (the stiff faces), C15
(the closed mixed surfaces) or the corner (beta_L, beta_M, beta_T) =
(0, beta, 0) as a gapped end-point, other than the lane's own later reading
in #10132, which also found none in the literature. For C7, the rank
3V - 3 itself is on `main` (`docs/FINITE_CLOCK_DIRECT_MAXWELL_SCALING_AND_COULOMB_WILSON_INTERACTIONS_BOUNDED_THEOREM_NOTE_2026-09-14.md`
L89, real coefficients) and in #10114 / #10133; the bound "at most half of
the plaquettes free of closed surfaces" is not. This is a bounded text
search with fixed patterns, not a proof of absence.

**Exposure note (written at once, 2026-11-17).** While I listed matched
lines in PR #10132 (the lane branch, head `5f85495a3d4a`, newer than this
clone's `0bdd62338`), my grep printed the first 280 characters of
`parts/gap.md` L167-168 at that head. Those two lines summarise row 1103 and
the row 1106 check (the other check of row 1103, which the brief told me not
to read). I did not open `library/gap-face-exercise-check-astra.md` and I
read no more of those two lines. All twelve verdicts S1-S12 above were
written to this file before that grep. I change no verdict because of it.
From here on I exclude `parts/gap.md` L160-175 of that head from my reading.

## Summary

Who checked what: every verdict below was checked line by line by Claude
Opus 5.5 (effort max, laptop subagent) in this file, against the row 1103
file at `0bdd62338` (unchanged at `5f85495a3d4a`). Same provider as the
writer (Claude Fable 5.2), so this is not a cross-provider check. Runs
(guides only, all exact or quadrature, in
`runs/gap-face-exercise-check-opus/` (copied from scratch by the lead)):
`c2_periodic_mu.py`, `c2prime_bound.py`, `c4_weight.py`, `c7_rank.py`. No
verdict rests on a run.

| # | Statement | Verdict | Main point |
|---|---|---|---|
| S1 | beta = 4 beta_th; N1a ranges | HOLDS | SZZ P^+ has one path per square (read); CNS from the lane reading plus the slab-action argument; 1/12 and 1/6 |
| S2 | C1 | HOLDS | - |
| S3 | C2 | HOLDS | test 1 passes: periodic mu never closes a ladder |
| S4 | C2' | HOLDS AFTER CORRECTION | formula right; (1+5c^L)^{L^3} only for cubic boxes (counterexample L_nu = L, other sides e^L); 5 needs L >= 3 in the window |
| S5 | C3 | HOLDS | group-blind; does not use the class property |
| S6 | C4 | HOLDS AFTER CORRECTION | degree-1 step holds; c_j <= c_{1/2} holds for Wilson (I_{nu+1} < I_nu), fails for f = 1 + 0.9 chi_1; periodic spatial sides must be >= 4 |
| S7 | C5(a) | HOLDS AFTER CORRECTION | Var A is taken at couplings (L_4+1) beta_ij and tends to 0; T-analog still false (zero spatial couplings: at once; positive: Var >= c/L_4^2, sketch) |
| S8 | C6 | HOLDS AFTER CORRECTION | eleven graphs and 2-cores right; C_4 surfaces are sums of products (area 30 is not a product); forest gap written only for the star |
| S9 | C7 | HOLDS | rank 3V - 3 on every periodic box (CW structure of T^4); six boxes computed |
| S10 | C14 | HOLDS AFTER CORRECTION | (a) gauge step right, Var box-dependent as in S7; (b) all eleven graphs right; triangle correctly a BELIEF; (c) false for small non-frozen couplings (frozen triangle at high temperature has a gap) |
| S11 | C15 | HOLDS | test 4 passes: (X (x) W) cap (V (x) Y) = V (x) W; {dP} a basis |
| S12 | (F4-KP) gives the T-analog | HOLDS AFTER CORRECTION | polymers must include integer-spin supports that are not closed mod 2 (spin-1 theta, 28 plaquettes, activity != 0); KP per-plaquette bound needs a/8; periodic boxes with winding polymers; "rate close to 4(-log c)" is a reading |
| S13 | test 6: search | no prior statement found | C6, C14, C15, corner (0, beta, 0): none on main or in 18 open PRs (except the lane's own later W2 reading, which found none); C7's rank 3V - 3 is on main and in #10114/#10133 in real form |

Side effects (not files of the repository): the clone `~/ym4d-lead/clone`
now holds 15,211 more blobs of `main` and 3,828 PR blobs, and 18 PR head
commits (shallow, depth 1, no refs created); its `.git` grew from 108 MB to
204 MB. No ref was changed (`origin/main` stayed `8b11ae2bb`). No commit,
no push. Only this output file was edited.

Not covered: C5(b), C5(c), C8-C13 and the closing paragraph of C14 (not in
the brief); (F4-KP) itself (open); the CNS primary text (no HTML version; not
downloaded); the general-forest clustering (not proved by the writer or by
me).

RESULT: Row 1105 (Claude Opus 5.5 max, laptop subagent; same-provider check of row 1103 by Claude Fable 5.2): HOLDS: beta = 4 beta_theirs and the N1a ranges (1/12, 1/6), C1, C2, C3, C7, C15. HOLDS AFTER CORRECTION: C2' (the total-effect bound holds only for cubic boxes), C4 (a general weight needs sup_j |c_j(f)|, counterexample f = 1 + 0.9 chi_1; periodic spatial sides >= 4; the Wilson case holds), C5(a) and C14(a) (Var A depends on the box; the T-analog still fails), C6 (C_4 surfaces are sums of products; the forest gap is written only for the star), C14 ((c) is false for small non-frozen couplings: the frozen triangle with high-temperature O(4) layers has a gap; the triangle BELIEF is marked correctly), the reduction "(F4-KP) gives the T-analog" (polymers must include integer-spin supports that are not closed mod 2, such as a 28-plaquette spin-1 theta; the KP bound needs a/8; periodic boxes with winding polymers). FAILS: none. Search: no prior statement of C6, C14, C15 or the corner (0, beta, 0) on main or in the 18 open PRs; the rank 3V - 3 of C7 is on main in real form. Two summary lines of the row 1106 check were seen by accident after all verdicts were written; no verdict was changed.
