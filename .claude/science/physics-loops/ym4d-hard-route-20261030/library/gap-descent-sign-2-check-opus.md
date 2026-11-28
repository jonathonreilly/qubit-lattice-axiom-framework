lead: anthropic/claude-opus-5-5/max laptop-subagent
row: 1088

# Check of row 1085 (`gap-descent-sign-2.md`), line by line

Checker: Claude Opus 5.5 (max), laptop subagent.
Author of row 1085: Claude Fable 5.2 medium.
This is a SAME-PROVIDER check (Anthropic model checking an Anthropic model).
It is not an independent check in the sense of a different provider.
The independent recomputation is row 1087; this file did not read it.

## Plan (at most eight steps; one step per response, results appended below)

Refined after step 1. Items C1-C8 are the check items of row 1088 (listed in step 1).

1. Read row 1088 in FINISH.md; read the file under check in full; refine this plan. DONE.
2. Read the context: row 1081 file, its checks (rows 1082, 1083), Lemma KIN and sections 6.1, 7.4 of row 1076, section 7.3 of row 1072. DONE.
3. Read the scripts and logs in runs/gap-descent-sign-2/. DONE.
4. Check by hand C1 (Z formula), C4 (centre symmetry), C5 (Lemma FACE-PROD). DONE.
5. Check by hand C2 (pillow coefficient formula, its tests, 3.4) and C3 (l_1 = beta_M^2/4). DONE.
6. Rerun copies of the scripts under /tmp (small, one thread): C6 (3.9 (a)-(c), truncation agreement), C7 (sector remarks). DONE.
7. C8 (scope against MON-L for beta_L in [beta, infinity) at beta_M = beta, route BR-2 of row 1072); verdict table. DONE.
8. RESULT line. DONE.

## Step results

### Step 1 (row 1088 read; file under check read in full). DONE.

Row 1088 (FINISH.md line 1169) asks for a line-by-line check of
`library/gap-descent-sign-2.md` (row 1085, 197 lines, 30971 bytes, read in full)
and its scripts in `runs/gap-descent-sign-2/`. The check items, in the row's order:

- C1. The reduction P_0 M P_0 = K_0^(1/2) Z E_T K_0^(1/2), Z = sum_d a_d^4 chi_d chi_d (3.1, given Lemma KIN (c)).
- C2. Level 3/2 on the pillow graph; the coefficient formula and its tests (3.2, 3.4; recalled, GUIDE).
- C3. l_1 = beta_M^2/4 at leading order (3.2).
- C4. The centre symmetry at beta_T = 0 (3.5).
- C5. Lemma FACE-PROD (3.8).
- C6. The kill-test computations of 3.9 (a)-(c) and their truncation agreement.
- C7. The sector-form remarks (3.7).
- C8. The scope of the negatives: does the counterexample touch (MON-L) for beta_L in [beta, infinity) at beta_M = beta in the window, as route BR-2 of row 1072 needs it?

Verdicts allowed: HOLDS, HOLDS AFTER CORRECTION (with text), FAILS (first failing line).
Row 1088 forbids a new attack. Reruns go in copies under /tmp.
Row 1087 (the cross-provider recomputation) runs at the same time; this file does not read it.

### Step 2 (context read). DONE.

Read in full: `library/gap-descent-sign.md` (row 1081, 181 lines).
Read: Lemma KIN to Lemma KIN-CVX and Remark FLAT (section 6.1, lines 303-346),
Example KIN-7 (6.4, lines 392-416) and brief P2 (7.4, lines 444-452) of
`library/gap-bridge-vectors-max.md` (row 1076); section 7.3 (lines 406-420)
and the route table 7.1 of `library/gap-bridge-exercise-opus.md` (row 1072);
the verdict ledgers, the spin-network and CUM sections and the several-sheet
paragraphs of check 1082 (`gap-descent-sign-check-astra.md`, lines 1-60,
230-329, 466-515) and check 1083 (`gap-descent-sign-check-opus.md`, lines
579-662). The rest of the two checks was not read; nothing below relies on it.

Facts used below (each read in its source):
- Lemma KIN (c) (row 1076 L312): R T R^(-1) = S* D S, S = K_Phi^(1/2) e^(-V_f/2),
  D = prod over cuts of M_c; heat kernel D = e^(-tN), N = sum_c C_c.
  Lemma KIN (a): C_c commute with each other, with K_Phi and with G.
  Check 1079 reports KIN (c) HOLDS (as quoted by check 1083 L590-L594;
  I did not read 1079).
- Identity KIN-5 (row 1076 L332): B_t = e^(-tN/2) S S* e^(-tN/2);
  dm/dt = n_1 - n_0 where lambda_0, lambda_1 are simple.
- Check 1082 (L480-L488): the large-t formula l_i = norm(P_1 M phi_i)^2 / lambda_i^2
  needs lambda_i(t = infinity) > 0 simple in P_0 M P_0, phi_i in ker N,
  and 3/2 the first contributing positive level. Check 1083 (L611-L614)
  reports the same formula HOLDS, and checked l_0 ~ beta_M^4/16 at leading order;
  the coefficient of l_1 ~ beta_M^2/4 was not checked by either check.
- (MON-L) as route BR-2 needs it (row 1072 L414): m(beta_L, beta, beta) >= m(infinity, beta, beta)
  for beta_L in [beta, infinity), at (beta_M, beta_T) = (beta, beta), beta in the window.
- Brief P2 (row 1076 L446): (FLUX-EXC) for SU(2) on ONE-SHEET boxes, for all beta_L, beta_M > 0.
  VB-3 (row 1076 L181): (FLUX-EXC) stated "for all t > 0 and all boxes".
- Example KIN-7 (row 1076 L404): frozen Q_8, one-sheet box, n = 2, Wilson endpoint form.

### Step 3 (scripts and logs read). DONE.

Read in full: `tplaq.py`, `gram_test.py`, `assembly_test.py`, `sectors.py`, `endpoint.py`,
`endpoint2.py`, and all 17 logs. Read from the JSON files the digits quoted in 3.9.

What the code computes (checked against 3.1 and 3.8):
- `tplaq.py`: `C[d]` is multiplication by chi_d on characters (fusion rule; index = 2j).
  `ET` is multiplication by e^(beta_T (x - 1)) (entries I_|n-m| - I_(n+m), scaled).
  n = 2: `M0` = K_0^(1/2) (sum_d a_d^4 X_d (x) X_d) K_0^(1/2), X_d = chi_d E_T, so
  `M0` = K_0^(1/2) Z E_T K_0^(1/2) (constants c^4 and e^(-2 beta_T) dropped; they cancel in
  every ratio and in l_i). n = 3: `M0` = K_0^(1/2) Z_12 Z_23 E_T K_0^(1/2).
  Level 3/2: `R[q,p,b]` = sqrt(2 d_j d_j') {j j' 1/2; J_II J_I b}^2 (half of the coefficient
  formula of 3.1 in the sector s_x = s_y = 1/2); weights `wq` = d_JI d_JII a_JI^nI a_JII^nII;
  K weights a_j^nI a_j'^nII per layer; four adjacent pairs (1, 3) and two diagonal pairs (2, 2).
  For n = 3 the factor 2 (two gaps) and the spectator weight a_c^4 are as stated in 3.6.
  The match to 3.1 is exact.
- `endpoint2.py`: sector (p, q) matrices of one sheet; face gap = min(singlet gap of one
  sheet, best cycle with doubled spins at most 4); m(t = infinity) from `tplaq.run`.
  `endpoint.py`: the same with four candidate cycles; it also prints the operator-order checks.
- `gram_test.py` compares the TOTAL Gram sum over all sectors (s_x, s_y) with the exact
  identity; it does not compare sector by sector. `assembly_test.py` compares the einsum with
  a loop over the same formula (not an independent formula).

Logs against the text:
- Every number in the tables of 3.3, 3.6, 3.7 and 3.8 that I compared (all rows of the
  beta_T = 0 table of 3.3; all entries of the beta_T > 0 sign table; all rows of the n = 3
  table; the 18 sector values of 3.7; all rows of the endpoint table) is in the saved logs,
  with the printed rounding.
- The digits of 3.9 (a), (b) are in the JSON files: l_1 - l_0 at beta_M = 10, beta_T = 0 is
  -0.6107714675445894 (12,12), -0.6107714675445877 (16,16), -0.6107714675446108 (22,20),
  -0.6107714675445663 (18,18), -0.6107714675445717 (26,24); at 8.5: -0.1008507688808304 (18,18)
  and -0.1008507688808269 (26,24); at beta_T = 0.1, beta_M = 10: -0.3143977371225706 and
  -0.3143977371225475; n = 3 at 10: -0.5551180738401342 (10,10), -0.5551180738401023 (12,12).
  All as quoted.
- The endpoint logs at (2Jmax 40; 18,18) and (56; 24,22) agree in every printed digit
  (endpoint2: identical files after the header; endpoint: two last-digit differences in the
  operator-order columns at beta_M = 16 and 24).
- The small-beta log `log_smallbeta.txt` has NO saved script in the folder (no file produced it).
  Its numbers match 3.2. It is reproduced in step 6 below.
- The n = 2 logs and JSON files carry no centre-parity column (added later, as the Files
  paragraph says). The claim "(at beta_T = 0.05, beta_M = 10: +0.93 and -0.92)" in 3.5 is in no
  saved log. It is rerun in step 6.
- The sentence "For beta_M >= 3 the ratio lambda_2/lambda_1 is at most 0.82" (3.3): at
  beta_T = 0.5, beta_M = 3 the log gives 0.820441. Text correction: "at most 0.821".
- `scripts/lab_ops.py` is absent in this checkout (confirmed), so no numeric lock exists.

### Step 4 (C1, C4, C5 by hand). DONE.

Notation. Square with sites x_1..x_4, link l from x_l to x_(l+1) (x_5 = x_1).
q_l = Phi_l(2) Phi_l(1)^(-1); U_k = Phi_1(k) Phi_2(k) Phi_3(k) Phi_4(k).
f = e^(beta_M x) = c sum_J d_J a_J chi_J with c = 2 I_1(beta_M)/beta_M
(because int e^(beta x) chi_J = I_(2J) - I_(2J+2) = (2 d_J/beta) I_(d_J)).

**C1. P_0 M P_0 = K_0^(1/2) Z E_T K_0^(1/2) (3.1, L41). Re-derived; HOLDS.**
- ker N. The cut rotations at layer 2 and G together generate independent gauge
  rotations of layer 1 and layer 2. So ker N in K is the set of functions gauge
  invariant in each layer: class functions of U_1 and U_2. U_1, U_2 are independent and
  Haar distributed when the eight links are, so chi_a(U_1) chi_b(U_2) is an orthonormal basis.
- P_0 = int prod_x dh_x rho(h) (average over the four layer-2 rotations). For psi in ker N,
  P_0 (e^(-V_f) psi) = psi E_T P_0 F with F = prod_l f(q_l). Under rho(h),
  q_l -> h_(x_l) Phi_l(2) h_(x_(l+1))^(-1) Phi_l(1)^(-1). Integrate h at x_2, x_3, x_4 with
  int dh chi_J(A h^(-1)) chi_J'(h B) = delta_JJ' chi_J(AB)/d_J: the ring becomes
  sum_J (c d_J a_J)^4 d_J^(-3) chi_J(h_1 U_2 h_1^(-1) U_1^(-1)). Then
  int dh chi_J(h C h^(-1) D) = chi_J(C) chi_J(D)/d_J gives
  P_0 F = c^4 sum_J a_J^4 chi_J(U_1) chi_J(U_2) = c^4 Z.
- K_Phi commutes with every rho_c (Lemma KIN (a)), hence with P_0. On chi_a(U_1) chi_b(U_2) it
  is a_a^4 a_b^4 (Schur: int w(V) chi_a(V Y) dV = chi_a(Y) (int w chi_a)/d_a, once per link).
- So P_0 M P_0 = c^4 K_0^(1/2) Z E_T K_0^(1/2) on ker N. The constant c^4 cancels in every
  eigenvalue ratio and in l_i (numerator and lambda_i^2 both scale by c^8).
- n = 3 (used in 3.6): integrating layer 3 first gives Z_23 (the integrand is invariant
  under the joint rotation of layers 2 and 3, so the result does not depend on the layer-2
  rotation); then layer 2 gives Z_12. So P_0 F = c^8 Z_12 Z_23, as `tplaq.py` builds it.
- Also: B_t tends to P_0 M P_0 in norm (norm of e^(-tN/2) - P_0 is e^(-3t/4)), and for the
  Wilson weight D tends to P_0 in norm (norm of D - P_0 at most 4 lambda_(1/2)(beta_L)).
Verdict C1: HOLDS (the constant is c^4 = (2 I_1(beta_M)/beta_M)^4; given Lemma KIN (c)).

**C4. Centre symmetry at beta_T = 0 (3.5, L92). Re-derived; HOLDS. One RESULT phrase corrected.**
c: Phi_(l_0)(k) -> -Phi_(l_0)(k) for every k. Then q_(l_0)(k) is fixed; each transverse
plaquette through l_0 changes sign. K_Phi commutes with c (convolution: V(-Phi) = -(V Phi));
G and every rho_c commute with c (-1 is central). At beta_T = 0, V_f has no transverse term.
So c commutes with S, N, B_t, for every n and every transverse lattice. On ker N it is
chi_a(U_1) chi_b(U_2) -> (-1)^(a+b) chi_a(U_1) chi_b(U_2) (chi_j(-U) = (-1)^(2j) chi_j(U)).
The code's `cpar` is <phi, c phi> with this sign. The U(1) remark is right: for U(1) the
kernel Z = sum_n a_n^4 e^(i n (theta_2 - theta_1)) conserves a + b.
Correction (RESULT line, L197): "the centre symmetry at beta_T = 0 (phi_1 is the
lowest centre-odd state)" is listed as PROVED. The symmetry is proved. That phi_1 is
centre-odd is GUIDE only (3.5: nine n = 2 values in `log_sectors_bT0.txt`, twelve n = 3
values). Corrected text: "PROVED by hand: ... the centre symmetry at beta_T = 0; GUIDE: phi_1
is centre-odd at every sampled beta_M (nine values for n = 2, twelve for n = 3)."

**C5. Lemma FACE-PROD (3.8, L118). Re-derived; HOLDS.**
At beta_T = 0 and a = 1, e^(-V_f) = prod_l e^(beta_M x(q_l)) and K_Phi = prod_l K_l, so
M = S S* = tensor product over l of T_1 = K^(1/2) e^(beta_M x(q)) K^(1/2) on L^2(Phi_l(1), Phi_l(2)).
T_1 commutes with the left action (q -> g q g^(-1)) and the right action (q fixed) of its
sheet, so T_1 = sum over (p, q) of T_1|M_(p,q) (x) 1. Site x_(l+1) is the end of link l
(right action) and the start of link l+1 (left action); an invariant of V_(q_l)* (x) V_(p_(l+1))
exists only for q_l = p_(l+1) and is one-dimensional. Every site of the square has one
incoming and one outgoing link, so K = sum over cycles of tensor products of M_(p_l, p_(l+1)),
and the face eigenvalues are products along a cycle. The top eigenvector of T_1 is positive
(Perron-Frobenius), hence in the (0, 0) sector, so the vacuum is mu_(0,0)^4. QED as written.
The centre flip at l_0 acts on sector (p, q) of sheet l_0 as (-1)^(2p), so the cycle
(1/2, 1/2, 1/2, 1/2) is centre-odd, as stated.
Sector matrices. For p = q the entry (1/2) sqrt(d_1 d_1' d_2 d_2') {p j_2' j_1'; 1/2 j_1 j_2}^2 equals
row 1081's entry {j_1 j_2 p; j_2' j_1' 1/2}^2 (6j column and row symmetries), i.e. the block
j_3 = p of row 1081's X_12. That block was checked by checks 1082 and 1083 (commutator test,
two hand values, 6j routine against sympy). The face gap in the table uses only the (0, 0)
block (beta_M <= 1) and the (1/2, 1/2) block (beta_M >= 2) as its minimum. The phase claim for
p not q (Edmonds (7.1.6) gives (-1)^(j_1 + j_2' + p) (-1)^(j_1 + j_2' + q) = (-1)^(2 j_1 + 2 j_2' + p + q),
constant on a sector since 2 j_2' = 2 j_2 +- 1 and 2 j_1 + 2 j_2 = 2p mod 2) I checked only
for this factor, not for the reduced matrix elements. It enters only cycles that are not the
minimum; step 6 bounds them independently of signs.
Verdict C5: HOLDS.

### Step 5 (C2 and C3). DONE.

**C2. Level 3/2 on the pillow graph and the coefficient formula (3.1 L42-L47, 3.2, 3.4).**
- Level 3/2 (L42). The lowest positive level of N is 3/2 (two cut spins 1/2); the number of
  half-integer cut spins in one layer gap is even, as stated (the layer loop must close).
  The next level is 2 (one cut spin 1). With spin 0 at the other two sites the arcs carry one
  spin each, so K_Phi = a_j^(n_I) a_j'^(n_II) a_k^(n_I) a_k'^(n_II), and integrating the n_I - 1
  inner rotations of arc I gives d_J a_J^(n_I) chi_J(side I) (one factor 1/d_J per join).
  HOLDS.
- The Schur-complement formula. In the S* e^(-tN) S picture it is first-order perturbation:
  lambda_i(t) = lambda_i + e^(-3t/2) <Omega_i, S* P_(3/2) S Omega_i> + O(e^(-2t)), and with
  phi_i = P_0 S Omega_i / sqrt(lambda_i) one has norm(P_(3/2) M phi_i)^2 = lambda_i norm(P_(3/2) S Omega_i)^2.
  This gives l_i = norm(P_(3/2) M phi_i)^2 / lambda_i^2 and n_i = (3/2) e^(-3t/2) l_i + O(e^(-2t)),
  under the conditions of check 1082 (lambda_i simple within its symmetry sector; the
  remainder is analytic in w = e^(-t/4) by Corollary KIN-D). HOLDS. The conditions hold on
  every grid point in the saved logs (lambda_2/lambda_1 < 1 at all points; at small beta_M the
  near pair lies in different swap sectors, as 3.3 says).
- The tests of 3.2. The Gram identity (L46) is right: I re-derived it by three Schur
  integrals in the tree gauge (X = T_II, Y = V_y, Z = B_II). `log_gram_3.txt` holds. But the
  Gram test compares the total over all sectors. It fixes the coefficient vectors only up to an
  orthogonal change of the state basis, so by itself it does not fix the relative signs inside
  the sector s_x = s_y = 1/2, and it does not fix the split of weight between states with
  different K_Phi weights. The hand checks (a = b = 0 sector; 3.4; small beta_M) test labels
  where each loop label meets one state, so they do not test interference either.
- Independent check (this row; GUIDE). Script `/tmp/check1088-opus/pillow/pillow_cg.py`
  (not in the repo). It uses no 6j symbol: explicit spin matrices, intertwiners as null
  vectors of the vertex Casimir, Haar integrals as projectors onto invariants (null space of
  the total Casimir), tree gauge T_I = V_x = B_I = 1, and the spin-network norm computed the
  same way. It compares each coefficient with the formula of 3.1 and tests whether the ratio
  depends only on the state. Results (logs in the same folder):
  - all sectors, loop labels with doubled spins at most 3: 12242 non-zero coefficients over
    3466 states; max | |mine/claimed| - 1 | = 2.0 x 10^(-13); ratio independent of the loop
    label for every state (max deviation 2.0 x 10^(-13)); no coefficient outside the claimed support;
  - sector s_x = s_y = 1/2 only, doubled spins at most 5: 6998 coefficients over 398 states,
    the same (2.8 x 10^(-13));
  - the normalization: norm(s)^2 = 1/prod_e d_e to 6 x 10^(-15) for every state.
  So, for these labels, the formula of 3.1 equals the true coefficient up to one sign per
  state. K_Phi and P_(3/2) are diagonal in the state basis, so l_i is unchanged by such signs.
  This closes the gap of the Gram test for loop spins at most 5/2. The runs of 3.3 use loop
  spins up to 23/2; for those the formula is the same closed form, tested here only for small
  labels.
- 3.4 (L90). Re-derived: the integral over each link factorizes, giving
  <F, rho(h) F> = prod_l sum_J a_J^2 chi_J(h_l) chi_J(h_(l+1)); the projection on cut spins and the
  pair pattern (1/2, 1/2, 0, 0) give 4 sum over |J_I - J_II| = 1/2 of a_(J_I)^(2 n_I) a_(J_II)^(2 n_II); the
  formula of 3.1 gives the amplitude 2 a_(J_I)^(n_I) a_(J_II)^(n_II) per loop label (using
  {J_I J_II 1/2; J_II J_I 0} = +-1/sqrt(d_I d_II)). HOLDS (a = b = 0 only, as stated).
Verdict C2: HOLDS as GUIDE, with the coefficient formula now confirmed by an independent
implementation up to signs per state for loop spins at most 5/2 (sector used) and 3/2 (all
sectors). Text correction to 3.2 L50: "So the coefficient formula of 3.1 is an orthonormal
expansion with the right Gram matrix" should add "(this fixes the coefficients only up to an
orthogonal change of the state basis; the relative signs in the sector s_x = s_y = 1/2 were
not tested by it)". The formula stays "recalled, GUIDE"; it is not proved by hand anywhere.

**C3. l_1 = beta_M^2/4 at leading order (3.2 L53). Re-derived; HOLDS AFTER CORRECTION of the mark.**
At beta_T = 0 and small beta_M: phi_1 = (chi_0 chi_(1/2) + chi_(1/2) chi_0)/sqrt 2 (swap-even);
the 2 x 2 block of K_0^(1/2) Z K_0^(1/2) on {(1,2), (2,1)} is a_2^4 [[1, a_2^4], [a_2^4, 1]], so
lambda_1 = a_2^4 (1 + a_2^4) and lambda_2/lambda_1 = 1 - 2 a_2^4 + ... (0.999532 at beta_M = 0.5,
where a_2 = 0.12372; matches the log). G = E_T K_0^(1/2) phi_1 = a_2^2 (chi_0 chi_(1/2) + chi_(1/2) chi_0)/sqrt 2.
For an adjacent pair and the component chi_(1/2)(U_1) chi_0(U_2): the loop label (J_I, J_II, a, b) =
(1/2, 0, 1/2, 0) has weight 2 a_2; the cheapest state has k = 0 on B_I, k' = 1/2 on B_II, j = 1/2,
j' = 0, with K_Phi = a_2 a_2^3 = a_2^4. Its coefficient is 1/2 by one Haar integral, with no 6j:
int dg tr(X g) tr(g^(-1) Y) = tr(XY)/2, and the merged loop is a normalized spin-1/2 loop.
So the amplitude is 2 a_2 x (1/2) x a_2^2/sqrt 2, and
l_1 = 4 pairs x 2 components x (a_2^3/sqrt 2)^2 a_2^4 / a_2^8 = 4 a_2^2 = beta_M^2/4 + O(beta_M^4).
The two components reach different states, so no interference enters at this order. Diagonal
pairs and the other states enter at relative order beta_M^2. l_0 = 16 a_2^4 (1 + a_2^4 + ...) also
re-derived (the a_2^4 is two diagonal pairs x two arcs x 4 a_2^8, against 16 a_2^4).
Correction: the mark "PROVED at leading order by hand, given the coefficient formula" (L170)
should read "derived at leading order by hand, without the 6j formula (one Haar integral);
the remainder O(beta_M^2) is not bounded in the text; ARGUED for the full asymptotic
statement". The leading coefficient 1/4 HOLDS. The run (`log_smallbeta.txt`: 1.000117,
1.000729, 1.002911 at beta_M = 0.02, 0.05, 0.1) fits 1 + 0.29 beta_M^2.

### Step 6 (reruns and independent GUIDE checks; C6, C7). DONE.

All runs: copies in `/tmp/check1088-opus/rerun/` (SHA-256 of each copy equal to the repo file),
one at a time, OMP/OPENBLAS/VECLIB threads 1, each under one minute, peak memory small.
Nothing was written in the checkout except this file (the runs folder still has 30 files).

Reruns of row 1085's scripts (confirm the logs):
- `tplaq.py 2 12 12 0.0 0.05` at beta_M = 8.5, 9, 10: same l_1 - l_0 as the log
  (-0.1008508, -0.2963451, -0.6107715 at beta_T = 0). With the centre-parity column (absent in the
  saved n = 2 logs): phi_1 has centre parity -1.000 at 8.5, 9, 10 (beta_T = 0); at beta_T = 0.05,
  beta_M = 10 the parities of phi_0, phi_1 are +0.927, -0.921. So the unsaved claim "+0.93 and -0.92"
  of 3.5 HOLDS.
- `tplaq.py 3 10 10 0.0` at beta_M = 10: l_1 - l_0 = -0.5551180738401342, the JSON value.
- `endpoint2.py 40 18 18 4`: all 14 data rows identical to `log_endpoint2_J40.txt`.
- `sectors.py 18 18 0.0` (NEIG = 7): identical to `log_sectors_bT0.txt`.
- `gram_test.py 3` and `assembly_test.py`: identical to their logs.
- Small beta (script written here, `smallbeta_check.py`, since none was saved): reproduces
  every number of `log_smallbeta.txt`.
- Truncation agreement, from all saved JSON files: n = 2 main grid (three truncations, 52 points)
  max |difference| of l_0, l_1 = 1.1 x 10^(-13); fine grid (two truncations, 78 points)
  9.6 x 10^(-14); n = 3 (36 points) 1.2 x 10^(-13). As stated (10^(-13), 1.3 x 10^(-13)).

Independent implementations (GUIDE; my code, not row 1085's):
- `minf_indep.py`: P_0 M P_0 built with fusion matrices from Gauss-Legendre quadrature in the class
  angle and Bessel ratios from mpmath (30 digits). m(t = infinity) = 2.767209, 0.454295, 0.395467,
  0.344243, 0.260247, 0.145668 at beta_M = 2.4, 8, 8.5, 9, 10, 12, and lambda_1/lambda_0 = 0.7708608069 at
  10: equal to row 1085's values in every printed digit.
- `l_indep.py`: end-to-end l_0, l_1 with the m-basis coefficients of step 5 (no 6j), my own
  enumeration of level-3/2 states, my own loop and K_Phi weights, and the P_0 M P_0 above. Against
  `tplaq.run` at the same truncation: (A, D) = (4, 4), beta_M = 2.4 and 10: equal to 12 digits;
  (7, 7): beta_M = 10 gives l_1 - l_0 = -0.610771467567 (tplaq: -0.610771467567; row 1085's converged
  value -0.6107714675446), beta_M = 8.5 gives -0.100850768881 (row 1085: -0.10085076888083).
  So 3.9 (a) at beta_M = 8.5 and 10 is reproduced by a second implementation that shares only the
  hand reduction of 3.1 (checked in steps 4 and 5).
- `endpoint2_abs.py` (copy of endpoint2 with every sector entry replaced by its absolute value;
  sheet spins up to 3). Entrywise domination gives mu(p, q) <= mu_abs(p, q), so every cycle cost with
  absolute values is a lower bound on the true cost. Result: the face minimum is unchanged at all 14
  beta_M (singlet gap for beta_M <= 1, the cycle (1/2)^4 for beta_M >= 2, same values), and the
  second-best cycle too. So the face gap of 3.8 does not depend on the phase convention for p not
  q, and sheet spins 5/2 and 3 add no lower cycle.

**C6. 3.9 (a)-(c) and truncation agreement.** HOLDS as GUIDE, with these text corrections:
- 3.9 (a) and the 3.3 table print l_0, l_1 as 7-digit log values padded with zeros. Example:
  l_1(beta_M = 10) = 14.057128 (JSON 14.05712827), not 14.057130; l_0(8.5) = 12.493752, not 12.493750.
  The differences l_1 - l_0 are right.
- "lambda_2/lambda_1 is at most 0.82" (3.3): 0.820441 at beta_T = 0.5, beta_M = 3; read "at most 0.821".
- "Regression ... 2.540323 at 8 (row 1081: ... 2.5403231)": row 1081's table (L77) prints 2.54032609
  (truncation 14); 2.5403231 is the truncation-18 value in row 1081's saved `out_2s_18.json`
  (2.540323082648627), also quoted by checks 1082 (L431) and 1083 (L546). The regression holds
  against that value; cite the saved file, not the table.
- The lines "beta_M >= 8.5 (monotone) or >= 9 (endpoint)" (L148, L175) mean the grid points
  8.5 to 48 (n = 2), 8.5 to 14 (n = 3) and 9 to 24 (endpoint); the RESULT line already says
  "every grid beta_M". One grid point suffices for a counterexample.
Item (c) is the stronger of the three: it uses no pillow coefficient, its t = infinity side is
reproduced by my independent build, and its face side rests on FACE-PROD (C5) and on row 1081's
checked (1/2, 1/2) and (0, 0) blocks, with the other cycles bounded above independently of signs.
Item (a) is now reproduced by a second implementation. Neither item has error bounds; both stay GUIDE.

**C7. Sector remarks (3.7).** HOLDS as GUIDE after one correction. The layer swap commutes with
P_0 M P_0 for every beta_T (Z, E_T, K_0 symmetric), and the centre flip at beta_T = 0 (C4). All 18
quoted sector values are in the log and the rerun. Correction to L114: "for beta_M from 3 to 12,
inside the row's range and also at beta_T = 0.5" should read "for beta_M from 3 to 12 at beta_T = 0,
and from 3 to 10 at beta_T = 0.5 (at beta_M = 12, beta_T = 0.5 the value is +0.040; on the grid)".
The reading "not the gap m" is right: the lowest swap-odd state is phi_2 or below, never phi_1.

### Step 7 (C8, remaining lines, verdict table). DONE.

**C8. Scope: does the counterexample touch (MON-L) as route BR-2 needs it? No.**
Route BR-2 (row 1072 L410-L414) needs (MON-L): m(beta_L, beta, beta) >= m(infinity, beta, beta) for
beta_L in [beta, infinity), at beta_M = beta_T = beta, with beta in the window [2.3, 2.6] (row 1072 L76).
The counterexample misses that range in all three couplings:
- beta_T. All three items are at beta_T = 0. Item (a) is negative also on the grid 0.02 <= beta_T <= 0.15;
  item (c) extends to small beta_T > 0 only by continuity, size not computed. At beta_T = 0.2 the large-t
  sign is positive at every grid beta_M (0.5 to 48), at beta_T = 0.5 at every grid beta_M (0.5 to 16).
  No run has beta_T >= 1.
- beta_M. Negative only for beta_M >= 8.5 (a, b) or >= 9 (c), on the grid. At beta_M = 2.4: l_1 - l_0 =
  +1.28 (beta_T = 0) to +1.25 (beta_T = 0.5), and m(beta_L = 0) - m(infinity) = +1.013 (beta_T = 0).
- beta_L. Item (a) is the t -> infinity asymptotic of the heat-kernel form (beta_L -> 0 in the Wilson
  language), not the Wilson weight on [beta, infinity). Item (c) compares beta_L = 0 with beta_L = infinity,
  and by continuity covers small beta_L only. Nothing was computed at finite beta_L (row 1085 L186).
What it does refute (GUIDE): the all-coupling box statement "n_1 >= n_0 for all t > 0 and
m(beta_L) >= m(infinity) for all beta_L > 0, on every box and at all (beta_M, beta_T)", i.e. VB-3's
(FLUX-EXC) "for all t > 0 and all boxes" (row 1076 L181) and its endpoint analogue, on the box with one
transverse plaquette. It does not touch brief P2 (one-sheet boxes, row 1076 L446), nor VB-18.
Reading (not a new attack): a box route to BR-2's (MON-L) must restrict the couplings, since the
all-coupling box form is false at beta_T = 0, large beta_M (GUIDE).

Corrections that follow (row 1085 lines):
- L148 "What it refutes: (FLUX-EXC) and (MON-L), in the monotone form and in the endpoint form, on boxes
  with a transverse plaquette, ..." should name the statement: "What it refutes: the all-coupling box
  forms of (FLUX-EXC) and of (MON-L) (for all t > 0, all beta_L > 0, all (beta_M, beta_T)), ... It does not
  touch (MON-L) as route BR-2 uses it (beta_L in [beta, infinity) at beta_M = beta_T = beta in [2.3, 2.6])."
  The same holds for the mark at L175 and for the phrase "(MON-L)" in the RESULT line context.
- L180 "about the window couplings (beta_M near 2.4, where both tests are positive on these boxes)"
  should read "about the window couplings (at beta_M = 2.4 both tests are positive on these boxes, the
  large-t sign for 0 <= beta_T <= 0.5 and the endpoint test at beta_T = 0; the window point
  beta_T = beta_M = beta of route BR-2, and finite beta_L, were not computed)". `parts/gap.md` L160 repeats
  the uncorrected sentence; the lead may wish to carry the correction there (not edited here).
- L163 "The three-dimensional test-bed VB-18 has such boxes when its transverse lattice has a plaquette;
  I did not check which boxes VB-18 needs." should read "VB-18 uses the split 2 + 1; its transverse lattice
  is one-dimensional and has no plaquette (row 1076 L262), so its boxes are transverse paths and this
  counterexample does not touch VB-18 or the strength warning of brief P2."

**Remaining lines, checked briefly.**
- L1-L35 (plan, row read, files, prior-work grep): consistent. The three named files were re-grepped:
  `open-core.md` and `open-registry.md` have no hit; `parts/gap.md` L157-L160 now carry entries added
  after the row (including row 1085 itself). `scripts/lab_ops.py` absent (confirmed).
- Steps 4 and 5 NOT RUN (L152-L155): this follows the row's text (task 2 is conditional on no negative
  sign; a confirmed negative sign ends the row). The negative sign lies outside the asked grid
  (beta_M 0.5 to 8), which L155 states. The counterexample is on a different box from step (S), so
  step (S) and Remark CUM are untouched, as L154 says.
- L141 "Why (ARGUED)": consistent with the data (Z(U, U) <= sum_d a_d^4 d^2 = Z(+-1, +-1), since
  |chi_d| <= d); the tunnelling reading is not checked. ARGUED, as marked.
- L157-L162 (tests): the bullets on FACE-PROD, the Z formula, the centre element of Q_8, 2T, SU(2), the
  U(1) remark and Example KIN-6 HOLD.
- L182-L191 (not checked): accurate. Add: no saved script produced `log_smallbeta.txt`; the n = 2
  logs have no centre-parity column (both reproduced in step 6 of this file).
- L193 (credits): no change needed for the checked content.

**Verdict table.**

| Item | Lines | Verdict |
|---|---|---|
| C1: P_0 M P_0 = K_0^(1/2) Z E_T K_0^(1/2), Z = sum_d a_d^4 chi_d chi_d; ker N = class functions of U_1, U_2 | L40-L41, L168 | HOLDS (constant c^4 = (2 I_1(beta_M)/beta_M)^4; given Lemma KIN (c)); n = 3 form Z_12 Z_23 also HOLDS |
| C2: level 3/2 on the pillow graph, arc weights, K_Phi weights | L42-L43 | HOLDS |
| C2: Schur-complement large-t formula and its conditions | L47, L56 | HOLDS (conditions met on every saved grid point) |
| C2: coefficient formula and its tests | L44-L52, L169 | HOLDS as GUIDE; Gram test re-derived, but it fixes the coefficients only up to an orthogonal change of state basis (correction to L50); independently confirmed here up to one sign per state for loop spins <= 5/2 (sector used) and <= 3/2 (all sectors) |
| C2: 3.4 identity | L90 | HOLDS (a = b = 0, as stated) |
| C3: l_1 = beta_M^2/4 at leading order | L53, L170 | HOLDS AFTER CORRECTION: coefficient 1/4 right (re-derived with one Haar integral, no 6j); mark "PROVED ... given the coefficient formula" -> "derived at leading order; remainder not bounded" |
| C3: l_0 = 16 a_2^4 (1 + a_2^4 + ...) | L53 | HOLDS |
| C4: centre symmetry at beta_T = 0 | L92, L171 | HOLDS |
| C4: "phi_1 is the lowest centre-odd state" in the RESULT line, listed as PROVED | L197 | HOLDS AFTER CORRECTION: GUIDE (sampled beta_M only) |
| C5: Lemma FACE-PROD, sector structure, centre parity of (1/2)^4 | L118-L121, L172 | HOLDS |
| C6: 3.9 (a), n = 2, monotone form | L145 | HOLDS as GUIDE; reproduced by a second implementation at beta_M = 8.5, 10 |
| C6: 3.9 (b), n = 3 | L146 | HOLDS as GUIDE (rerun at beta_M = 10; code read; no second implementation) |
| C6: 3.9 (c), endpoint form | L147 | HOLDS as GUIDE; t = infinity side independently reproduced; face minimum robust to p-not-q signs and to sheet spins up to 3 |
| C6: truncation agreement | L56, L95, L145-L147 | HOLDS (1.1e-13, 9.6e-14, 1.2e-13 over all saved points) |
| C6: tables of 3.3, 3.6, 3.8 | L58-L138 | HOLDS AFTER CORRECTION of cosmetic digits (l columns padded; "0.82" -> "0.821"; regression citation) |
| C7: sector remarks | L111-L114, L177 | HOLDS AFTER CORRECTION of the beta_T = 0.5 range (3 to 10, not 3 to 12) |
| C8: scope of the negatives | L148-L149, L175, L180, L163 | HOLDS AFTER CORRECTION: the counterexample refutes the all-coupling box form only; it does not touch (MON-L) for beta_L in [beta, infinity) at beta_M = beta_T = beta in [2.3, 2.6] (route BR-2), nor brief P2, nor VB-18 (corrected texts above) |
| Steps 4, 5 not run | L152-L155 | HOLDS (per the row's text) |

No item FAILS. No line of row 1085 claims a mass gap, and none is claimed here.

**What this check did not cover.** Lemma KIN itself (used as stated; check 1079 reports KIN (c) HOLDS,
as quoted by check 1083). A hand proof of the pillow coefficient formula (only the numerical
m-basis confirmation for small loop spins). An independent implementation of the n = 3 assembly and of
the face (1/2, 1/2) block (both read and rerun only; the block is row 1081's checked block). Error bounds
for any eigenvalue. The finite-t and finite-beta_L behaviour between the ends. Row 1087's file (not read,
as instructed). This is a SAME-PROVIDER check (Anthropic model checking an Anthropic model); it is not an
independent check in the sense of the lane's rules. My scripts and logs are in `/tmp/check1088-opus/`
(`pillow/pillow_cg.py`, `rerun/minf_indep.py`, `rerun/l_indep.py`, `rerun/endpoint2_abs.py`,
`rerun/smallbeta_check.py`); they are scratch files and are not in the repo.

Checked line by line by Claude Opus 5.5 (max), laptop subagent.

### Step 8 (RESULT). DONE.

RESULT: Row 1088 (Claude Opus 5.5 max, laptop subagent; SAME-PROVIDER check of row 1085, written by Claude Fable 5.2 medium; row 1087 not read). No item FAILS. HOLDS: the reduction P_0 M P_0 = K_0^(1/2) Z E_T K_0^(1/2), Z = sum_d a_d^4 chi_d chi_d (re-derived by hand, constant (2 I_1(beta_M)/beta_M)^4 cancels; n = 3 form Z_12 Z_23 too); Lemma FACE-PROD; the centre symmetry at beta_T = 0; level 3/2 and the large-t formula under check 1082's conditions (met on the grid); the 3.4 identity; l_0 = 16 a_2^4 (1 + a_2^4); the kill-test numbers of 3.9 (a)-(c) as GUIDE (reruns reproduce the logs; truncation agreement 1.2e-13 or better over all saved points). New GUIDE evidence here: an m-basis computation with no 6j confirms the pillow coefficient formula up to one sign per state (12242 coefficients, loop spins at most 3/2, all sectors; 6998 in the sector used, loop spins at most 5/2), which the Gram test alone could not fix; a second end-to-end implementation reproduces l_1 - l_0 = -0.6107714676 (beta_M = 10) and -0.1008507689 (8.5); an independent build gives m(beta_L = 0) = 0.260247 at beta_M = 10; the face minimum is unchanged when every sector entry is replaced by its absolute value (a sign-free lower bound on the other cycles). HOLDS AFTER CORRECTION: l_1 = beta_M^2/4 (coefficient right by one Haar integral; the mark is "derived at leading order, remainder not bounded", not PROVED); "phi_1 is the lowest centre-odd state" is GUIDE, not PROVED; the Gram test fixes coefficients only up to an orthogonal change of basis; the beta_T = 0.5 sector range is 3 to 10; cosmetic digits; and the scope: the counterexample refutes only the all-coupling box form of (FLUX-EXC) and (MON-L) (beta_T = 0 to 0.15, beta_M at least 8.5, t to infinity or beta_L = 0); it does not touch (MON-L) for beta_L in [beta, infinity) at beta_M = beta_T = beta in [2.3, 2.6] as route BR-2 needs it, nor brief P2 (one-sheet boxes), nor VB-18 (no transverse plaquette in the 2 + 1 split; row 1085 L163 corrected); at beta_M = 2.4 the tests were run only at beta_T at most 0.5. Output `library/gap-descent-sign-2-check-opus.md`.
