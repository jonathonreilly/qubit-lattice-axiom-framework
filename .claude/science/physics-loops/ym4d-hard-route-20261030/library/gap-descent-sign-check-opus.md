lead: anthropic/claude-opus-5-5/max laptop-subagent
row: 1083

# Check of row 1081 (gap-descent-sign.md) and its GUIDE scripts

Provenance: row 1081 was written by Claude Fable 5.2 medium. This check is
by Claude Opus 5.5 (max). Both are Anthropic models, so this is a
SAME-PROVIDER check, not an independent one. Row 1082 is the cross-provider
check; this file did not read it.

## Plan (revised after reading row 1083; at most eight steps)

1. Read FINISH row 1083 (done; items listed below).
2. Read the file under check in full, and the context in row 1076:
   sections 6.1, 6.4, brief P2 of section 7.4, Examples KIN-6 and KIN-7.
3. Tests first: Proposition DIL on frozen Q_8 against Example KIN-7;
   Corollary N2-SMALL at beta_M = 3/2 by hand.
4. Check the spin-network form (N diagonal, face part non-negative) and
   Lemma TP-2.
5. Check Lemma SC, Proposition DIL, Corollary N2-SMALL line by line.
6. Check the ARGUED cumulant reading and the three written failures of
   step (S).
7. Check the kill-test code (basis, 6j symbols, truncations, agreement);
   small rerun copied to /tmp, threads 1, one job at a time.
8. Verdicts per item and the RESULT line.

## Step results

### Step 1. Row 1083 (FINISH.md line 1164), items to check

Row 1083 asks for a line-by-line check of `library/gap-descent-sign.md`
(row 1081, by Claude Fable 5.2 medium) and its GUIDE scripts in
`runs/gap-descent-sign/`. The items:

- C1. The spin-network form with N diagonal and a non-negative face part.
- C2. Lemma TP-2 (n = 2: total positivity of order 2, a simple lambda_1,
  phi_1/phi_0 monotone).
- C3. Lemma SC (single crossing gives the sign when r(1) is at most 1).
- C4. Proposition DIL (any group, any box:
  m(t) - m(s) >= (t - s)(nu_1 - 2 n_0(s)); on one-sheet boxes
  n_0(0) <= 3/4 gives a non-decreasing gap).
- C5. Corollary N2-SMALL ((FLUX-EXC) at n = 2 for beta_M <= 3/2).
- C6. The ARGUED cumulant reading at large beta_M (right skew for SU(2),
  left skew for the point mass of Q_8).
- C7. The three written failures of step (S), Cov_p(r^2, c) >= 0.
- C8. The kill-test code: the basis, the 6j symbols, the truncations,
  whether two or three truncations agree. A numeric result is GUIDE
  grade only.

Tests first: Proposition DIL on frozen Q_8 against Example KIN-7 of row
1076 (it must not give the false sign there); N2-SMALL at beta_M = 3/2 by
hand. Verdicts: HOLDS, HOLDS AFTER CORRECTION (with the text), FAILS (with
the first failing line). No new attack. Proofs must be Lean-formalizable;
no computer-assisted proof.

The row 1081 RESULT line in FINISH.md (line 1162) says "checked by no
one" and lists: PROVED the spin-network form, TP-2, SC, DIL, N2-SMALL;
ARGUED the cumulant reading; OPEN (FLUX-EXC) at n = 2 for beta_M > 3/2,
at n >= 3 outside the dilute range, and for several sheets.

### Step 2. Read in full: the file under check and its context. DONE.

Read in full: `library/gap-descent-sign.md` (181 lines, row 1081).
Read from `library/gap-bridge-vectors-max.md` (row 1076, by Claude Fable
5.2 max): section 6.1 (L303-L346: Lemma KIN, Corollaries KIN-1 to KIN-3,
Lemma KIN-4, Identity KIN-5, Example KIN-6, Corollary KIN-D, Lemma
KIN-CVX), section 6.3 and 6.4 (L383-L416: Example KIN-7), section 7.4
(L444-L452: brief P2), VB-18 (L260-L264).

Definitions used in this check (from row 1076 section 6.1):
- S = K_Phi^(1/2) e^(-V_f/2) on K; R T R^(-1) = S* D S; D = product of
  M_c over cuts; heat kernel D = e^(-tN), N = sum of cut Casimirs C_c.
- lambda_0 >= lambda_1 >= ... the ordered eigenvalues;
  m = log lambda_0 - log lambda_1.
- B_t = e^(-tN/2) S S* e^(-tN/2) has the non-zero spectrum of S* e^(-tN) S;
  phi_i its unit eigenvectors; n_i = <phi_i, N phi_i>.
- KIN-5: where lambda_0, lambda_1 are simple, dm/dt = n_1 - n_0.
- KIN-7 (Q_8, n = 2): in the limit beta_M -> infinity, with eta = e^(-beta_L),
  A_L = 1 - 16 eta, B_L = 1 - 12 eta, K_00 = 1 - 12 eta, mu = 1 - 4 eta,
  lim [m(beta_L) - m(infinity)] = log K_00 - log mu = -8 eta + O(eta^2).

The row 1081 file has no line numbers in its own text; I cite its lines
as L<number> of the file as read (cat -n numbering).

### Step 3. Tests first. DONE.

**3a. Proposition DIL on frozen Q_8 against Example KIN-7 (row 1081 L144).**
By hand, in the KIN-7 limit (beta_M -> infinity at fixed beta_L):
- D on K (class functions of q = Phi_2 Phi_1^(-1)) has eigenvalues 1
  (trivial), A_L (sigma_i, sigma_j, sigma_k) and B_L (tau). B_L > A_L for
  every beta_L > 0, since lambda_tau - lambda_sigma = (2 sinh b - 2 cosh b + 2)/(2 cosh b + 6)
  = 2(1 - e^(-b))/(2 cosh b + 6) > 0. So delta_2 = 1 x B_L for every beta_L,
  not only at large beta_L. Correct as written.
- The top eigenvector of S S* = K_Phi^(1/2) E^2 K_Phi^(1/2) tends to e_0 (the
  normalised point mass at q = 1), since E^2 e^(-beta_M) tends to the
  projection on e_0 and K_Phi tends to 1. A point mass has weight d_rho^2/8
  on chi_rho. So <psi, D psi> tends to 1/8 + (3/8) A_L + (1/2) B_L = K_00.
  At large beta_L this is 1 - 12 eta. Correct.
- The bound tends to 2 log K_00 - log B_L = log(1 - 12 eta) + O(eta^2)
  = -12 eta + O(eta^2). The true limit is -8 eta. So the bound lies below
  the dip. It does not give the false sign. Correct.
- Consistency of the step "lambda_0 lambda_1 (beta_L) <= delta_2 lambda_0 lambda_1 (infinity)"
  in this limit: it reads K_00 mu <= B_L; at large beta_L,
  (1 - 12 eta)(1 - 4 eta) = 1 - 16 eta <= 1 - 12 eta. Correct.

GUIDE check at finite beta_M (my own 5 x 5 script, not the row's;
`/private/tmp/claude-501/-Users-jonreilly-Projects-Physics--claude-worktrees-peaceful-heisenberg-e2d2a0/b3f5c21a-8638-4944-b69d-c639619895d6/scratchpad/gds-check/q8_dil.py`,
one thread). It reproduces row 1076's dip: at beta_M = 2.4, beta_L = 3.5,
m(infinity) = 1.955630 and m(beta_L) = 1.916303 (row 1076 L410: 1.9556 and
1.9162). The DIL bound there is -0.1191, below the true -0.0393. At
beta_M = 12, beta_L = 8 the true difference is -2.680 x 10^(-3) (row 1076:
-2.680 x 10^(-3)) and the DIL bound is -4.020 x 10^(-3), against
-12 e^(-8) = -4.026 x 10^(-3). The bound lies below the true difference at
all 15 grid points (beta_M in {2.4, 6, 12}, beta_L in {1, 2, 3.5, 5, 8}).
This confirms L144. It proves nothing; the proof is checked in step 5.

Verdict 3a: L144 HOLDS. DIL is a lower bound; it gives a negative bound
where Q_8 dips; its Wilson-form hypothesis <psi, D psi>^2 >= delta_2 fails
there, since (1 - 12 eta)^2 < 1 - 12 eta.

**3b. Corollary N2-SMALL at beta_M = 3/2 by hand (row 1081 L116-L118).**
Each line of the proof, checked:
- B_0 phi_0 = lambda_0 phi_0 with B_0 = S S* = K^(1/2) E^2 K^(1/2): correct
  (S = K_Phi^(1/2) E, E self-adjoint).
- norm(E K^(1/2) phi_0)^2 = <phi_0, B_0 phi_0> = lambda_0: correct.
  norm(E)^2 = sup e^(beta cos) = e^(beta): correct.
  norm(N^(1/2) K^(1/2))^2 = sup_n c_n a_n^2 (diagonal): correct.
  So n_0(0) = norm(N^(1/2) phi_0)^2 <= e^(beta) sup_n(c_n a_n^2)/lambda_0: correct.
- I_n(x) <= (x/(2n)) I_(n-1)(x): term by term the ratio of the k-th terms is
  (x/2)/(k + n) <= x/(2n). Correct. So a_n <= prod_(k=2..n) beta/(2k).
- c_1 = 0, c_2 = 3/2, a_2 <= beta/4: c_2 a_2^2 <= 3 beta^2/32. Correct.
- c_(n+1)/c_n = n(n+2)/((n-1)(n+1)) <= (n+2)/(n-1): the row's factor is a
  valid (loose) upper bound. With a_(n+1)/a_n <= beta/(2n+2), the ratio is
  at most beta^2/9 at n = 2, which is 1/4 at beta = 3/2, and smaller for
  larger n. So sup_n c_n a_n^2 = c_2 a_2^2. Correct.
- lambda_0 >= <e_1, A e_1> = a_1^2 (I_0 - I_2) = 2 I_1(beta)/beta (recurrence
  I_(n-1) - I_(n+1) = (2n/x) I_n at n = 1) = sum_k (beta/2)^(2k)/(k!(k+1)!)
  >= 1 + beta^2/8. Correct.
- Arithmetic at beta = 3/2: 3 x 2.25/32 = 0.2109375; e^(1.5) = 4.481689;
  1 + 2.25/8 = 1.28125; 0.2109375 x 4.481689/1.28125 = 0.737839 <= 3/4.
  Correct.
- The bound increases in beta: d/dbeta of its log is
  2/beta + 1 - (beta/4)/(1 + beta^2/8) > 0, since (beta/4)/(1 + beta^2/8) <= 2^(-3/2) < 1.
  Correct. So n_0(0) <= 0.738 for all beta <= 3/2.
- Final line: nu_1 = 3/2 at n = 2 (c_2 = 3/2 is the least non-zero c_n);
  lambda_1 simple by Lemma TP-2; n_0(t) <= n_0(0) by Lemma KIN-CVX (log
  lambda_0 convex with derivative -n_0); so n_1 - n_0 >= 3/2 - 2 n_0(t)
  >= 3/2 - 1.4757 > 0. Correct, given DIL's pointwise form (step 5).

One slip in the remark after the proof (L118): "the run gives n_0(0) = 0.022
at beta_M = 1 against the bound 0.69". The value 0.022 is right (my script
`n2_small.py` in the same folder: 0.021938). The bound at beta_M = 1 is
(3/32) e/(1 + 1/8) = 0.2265, not 0.69 (0.69 is the bound near beta_M = 1.47).
Corrected text for L118: "The bound is crude: the run gives n_0(0) = 0.022
at beta_M = 1 against the bound 0.23, and 0.097 at beta_M = 3/2 against
0.738." (GUIDE values from my script: n_0(0) = 0.096935 at beta = 3/2.)

Verdict 3b: N2-SMALL HOLDS at beta_M = 3/2 by hand. The remark L118 HOLDS
AFTER CORRECTION (the number 0.69 replaced by 0.23). The proof uses DIL's
pointwise form; that form is checked in step 5.

### Step 4. C1 (spin-network form) and C2 (Lemma TP-2). DONE.

**C1, one-sheet set-up (L25).** Checked: the plaquette between slice sites
k, k+1 is x(Phi_(k+1) Phi_k^(-1)) at a = 1; the cut (k, x) rotates
Phi_(k') -> W Phi_(k') for k' > k (left), the cut (k, y) rotates
Phi_(k') -> Phi_(k') W^(-1) (right). The face is the principal chiral
(O(4)) chain on singlets. Correct.

**C1, basis and N (L27-L30).** Peter-Weyl gives, for fixed (j_1..j_n), the
multiplicity space Inv(V_(j_1) x ... x V_(j_n)) x Inv(dual). On singlets
C^L_(>k) = C^L_(<=k). For n = 3 both invariant spaces are one-dimensional
(triangle and integer sum), so one vector per triple, and
N = 2 j_1(j_1+1) + 2 j_3(j_3+1), D = lambda_(j_1)^2 lambda_(j_3)^2 (beta_L),
K_Phi = lambda_(j_1) lambda_(j_2) lambda_(j_3) (beta_M) (Schur, since w is a
class function). Correct.

**C1, the face matrices (L31).** The scalar-product formula used is
Edmonds (7.1.6): <j_1' j_2' L | T^k(1).U^k(2) | j_1 j_2 L> =
(-1)^(j_1 + j_2' + L) {L j_2' j_1'; k j_1 j_2} <j_1'||T||j_1><j_2'||U||j_2>.
Multiplication by chi_J(Phi_2 Phi_1^(-1)) = sum_(a,b) D^J_(ab)(Phi_2) conj(D^J_(ab)(Phi_1))
splits into a scalar product on the left indices (sum over a) times one on
the right indices (sum over b). For n = 3, L = j_3 on both sides, so the
same sign appears twice and the entry is a square. By the 6j symmetries
{j_3 j_2' j_1'; J j_1 j_2} = {j_1 j_2 j_3; j_2' j_1' J}, the 6j of L31.
I redid both hand checks: at j_3 = 0, {j j 0; j' j' J}^2 = 1/(d_j d_j'),
so the entry is 1; for |1/2 1/2 0> -> |1/2 0 1/2> under chi_(1/2)(32),
2 x {0 1/2 1/2; 0 1/2 1/2}^2 = 2 x 1/4 = 1/2, and the direct integral is
<tr(AB), tr(A) tr(B)> = <tr(AB), tr(AB) + tr(AB^(-1))> = 1 + E[(1/2) tr(B^(-2))]
= 1 - 1/2 = 1/2 (E over Haar A of tr(AB) tr(AB^(-1)) = (1/2) tr(B^(-2)),
and E tr(B^2) = E[chi_1 - 1] = -1). Correct for n = 3.

A wording point (L50 (i)): with squared 6j symbols the sign of each 6j
symbol does not enter, so the commutator test checks the magnitudes and
the claim that no extra sign appears; it does not check 6j signs.
Harmless.

**C1, general n (L32, and again L132): HOLDS AFTER CORRECTION.** "N is
diagonal for every n" is correct: in the sequential coupling basis
|j; L_2..L_(n-2); R_2..R_(n-2)> every C^L_(<=k) = L_k(L_k+1) and every
C^R_(<=k) = R_k(R_k+1) is diagonal. "The face part has non-negative
entries" for every n is not proved by the written argument. For n >= 4
each side has an intertwiner space of dimension > 1, and the left and right
intermediate labels L_k and R_k are independent. The entry of
chi_J(Phi_(k+1) Phi_k^(-1)) is then (positive factor) x c(L' <- L) x c(R' <- R),
a product of two different recoupling coefficients, not a square. The text
gives no sign rule for that product. I did not test it; it is neither
proved nor refuted here. Corrected text for L32: "General n: in the
sequential coupling tree from one end, all C_(>k) are diagonal at once, so
N is diagonal for every n. For n = 3 (and for the two-sheet box with
n = 2) the face part has non-negative entries, since each side has a
one-dimensional intertwiner space and the entry is a square. For n >= 4 the
entry is a product of a left and a right recoupling coefficient with
independent intermediate spins; its sign is OPEN." The same restriction
applies to L132 ("The face part has non-negative entries ... the vacuum
has non-negative spin-network coefficients for every t"): it holds for
n = 3; for n >= 4 it is OPEN. Nothing proved in row 1081 uses the n >= 4
case. The RESULT phrase "the spin-network form with N diagonal and a
non-negative face part" should be read for the two boxes (as in L161).

**C1, two-sheet box (L34-L38).** Checked: A = Phi_a(1)^(-1) Phi_a(2) and
B = Phi_b(2) Phi_b(1)^(-1) are fixed by g_x, g_z and conjugated by g_y;
fixing Phi_a(1) = Phi_b(1) = 1 by g_x, g_z shows K = functions of (A, B)
under joint conjugation. For one sheet, n = 3, A' = Phi_1^(-1) Phi_2,
B' = Phi_2^(-1) Phi_3. The identification of the three Casimirs:
two-sheet cut (1, x) (A -> W A) is the right rotation of Phi_1 (spin j_1);
cut (1, z) (B -> B W^(-1)) is the right rotation of Phi_3 (j_3); cut (1, y)
(A -> A W^(-1), B -> W B) is the right rotation of Phi_2 alone (j_2). I
checked it on chi_(1/2)(A'), chi_(1/2)(B'), chi_(1/2)(A'B') = |1/2 1/2 0>,
|0 1/2 1/2>, |1/2 0 1/2>. The plaquettes are x(A), x(B) in both. The joint
eigenspaces of the three Casimirs are one-dimensional, so the two bases
agree up to signs, which do not change the spectra. K_Phi and D swap
their forms between the boxes (lambda_1 lambda_2 lambda_3 against
lambda_1^2 lambda_3^2), as L36-L37 say. Correct.

**C1, the remark that the kill tests do not depend on Lemma KIN (L84).**
Checked: for one sheet, n = 3, the slice graph has two trivalent sites
(2, x), (2, y) joined by three paths (a(1,x), Phi_1, a(1,y)), (Phi_2),
(a(2,x), Phi_3, a(2,y)): a theta graph. Its gauge-invariant functions are
theta spin networks; convolution on one link of a path multiplies by
lambda of that path's spin. For two sheets, n = 2, the trivalent sites are
(1, y), (2, y), and the paths carry (Phi_a(1), a(1,x), Phi_a(2)),
(a(1,y)), (Phi_b(1), a(1,z), Phi_b(2)). The weights in L84 follow.
Correct, as a consistency check of Lemma KIN (c) on these two boxes.

Verdict C1: HOLDS for the two boxes (one sheet n = 3, two sheets n = 2),
with the recalled formula Edmonds (7.1.6). HOLDS AFTER CORRECTION for
general n (L32, L132): restrict "non-negative face part" to n <= 3.

**C2, Lemma TP-2 (L94-L96).**
- (i) B = diag(d) k_beta diag(d) with d_n = a_n e^(-t c_n/2) (heat kernel)
  or d_n = a_n g_n (Wilson), all > 0; minors scale by products of d.
  Correct. J - 1 generates the rate-one walk with steps +-1 at rate 1/2
  each, killed on reaching 0; e^(beta J)(n, m) = e^(beta) P_n(X_beta = m, alive) > 0.
  Karlin-McGregor: a 2 x 2 minor is e^(2 beta) times the probability that
  the two walkers do not meet. In continuous time the jumps are at distinct
  times almost surely and the steps are +-1, so the walkers cannot cross
  without meeting. That probability is positive for n_1 < n_2,
  m_1 < m_2 (move the walkers to their targets in a non-crossing order,
  staying >= 1). Correct, with the recalled theorem.
- The Lean sketch: I + eps J is tridiagonal; its only non-trivial 2 x 2
  minors are 1 - eps^2/4 and (eps/2)^2, so it is TP2 for eps <= 2 (the row
  says eps <= 1, which is stronger than needed). Cauchy-Binet and the
  entrywise limit give non-negative minors of e^(beta J). Strict positivity
  needs a lower bound that survives the limit; a fixed family of
  non-crossing path pairs gives one. The sketch is short but sound.
- (ii), (iii): B_t is compact (d_n decays faster than geometrically) and
  positive. Lambda^2(B_t) is compact with strictly positive entries; by
  Jentzsch its spectral radius lambda_0 lambda_1 is simple with a strictly
  positive eigenvector. If lambda_1 = lambda_2, then phi_0 ^ phi_1 and
  phi_0 ^ phi_2 both have eigenvalue lambda_0 lambda_1: contradiction.
  phi_0 ^ phi_1 = +-(the Jentzsch vector), so
  phi_0(i) phi_1(j) - phi_0(j) phi_1(i) has one strict sign on i < j;
  dividing by phi_0(i) phi_0(j) > 0 gives strict monotonicity of r.
  lambda_0 > lambda_1 by Perron-Frobenius on B_t (strictly positive
  entries). Choosing r(1) > 0: r cannot be constant in sign because
  E_p r = <phi_0, phi_1> = 0 and p > 0, so r(1) != 0 and r decreases.
  Correct.
- Consequence (L96): simple top two eigenvalues for all t >= 0, so
  m'(t) = n_1 - n_0 (one-sided at t = 0; n_i(0) finite since
  phi_i(0) = A phi_i/lambda_i has entries O(a_n)). Correct.

**Reduction (L98-L100).** n_1 = E_p[r^2 c], n_0 = E_p[c], E_p r^2 = 1,
E_p r = 0. So n_1 - n_0 = E_p[(r^2 - 1) c] = Cov_p(r^2, c). Correct.

Verdict C2: Lemma TP-2 HOLDS (with the recalled theorems of Karlin and
McGregor and of Jentzsch). The reduction HOLDS.

### Step 5. C3 (Lemma SC), C4 (Proposition DIL), C5 (N2-SMALL). DONE.

**C3, Lemma SC (L102-L104).** Line by line:
- r strictly decreasing, r(1) in (0, 1], E_p r = 0, E_p r^2 = 1. If
  r^2 <= 1 everywhere, then E_p r^2 <= 1 with equality only if r = +-1
  p-almost everywhere, which a strictly decreasing r cannot do on three or
  more points. So some r(n) has abs value > 1; since r(n) < r(1) <= 1 for
  n >= 2, it is r(n) < -1. Correct.
- n' = last n with r(n) >= -1 exists (r(1) > 0) and is finite. For n <= n',
  r(n) in [-1, 1], so r^2 - 1 <= 0; for n > n', r^2 - 1 > 0. Correct.
- With c non-decreasing, (r^2 - 1)(c_n - c_(n')) >= 0 for every n, and
  E_p[(r^2 - 1) c] = E_p[(r^2 - 1)(c - c_(n'))] + c_(n') E_p[r^2 - 1] >= 0.
  Correct (finite, since E_p[r^2 c] = n_1).
- "r(1) <= 1 says the excited state has no more weight on the trivial
  character than the vacuum": r(1) = phi_1(1)/phi_0(1) with e_1 = chi_0.
  Correct.
Verdict C3: HOLDS. The "any non-decreasing sequence" clause needs the
expectations to be finite; add "with E_p[r^2 c'] finite". The GUIDE claim
about r(1) is checked in step 7.

**C4, Proposition DIL (L106-L114), Wilson form.**
- S* D S = (D^(1/2) S)* (D^(1/2) S) has the non-zero spectrum of
  D^(1/2) S S* D^(1/2). Lambda^2 is multiplicative, and Lambda^2(X* X),
  Lambda^2(X X*) have the same non-zero spectrum. So
  lambda_0 lambda_1 (beta_L) = norm Lambda^2(D^(1/2) S S* D^(1/2))
  <= norm(Lambda^2 D^(1/2))^2 norm(Lambda^2(S S*)) = delta_2 (lambda_0 lambda_1)(infinity).
  Here norm(Lambda^2 D^(1/2))^2 = d_0 d_1 for D >= 0, and S S*, S* S share
  the non-zero spectrum. D and S preserve K (Lemma KIN (a)). Correct.
- Rayleigh with the unit face vacuum Omega: lambda_0(beta_L) >=
  <Omega, S* D S Omega> = norm(S Omega)^2 <psi, D psi> = lambda_0(infinity) <psi, D psi>.
  Correct.
- m = 2 log lambda_0 - log(lambda_0 lambda_1), so
  m(beta_L) - m(infinity) >= 2 log <psi, D psi> - log delta_2. Correct.

**C4, heat-kernel form.**
- With S_s = e^(-sN/2) S: S_s* e^(-(t-s)N) S_s = S* e^(-tN) S and
  S_s* S_s = S* e^(-sN) S, so the Wilson form with D = e^(-(t-s)N) compares
  m(t) with m(s). The unit top eigenvector of S_s S_s* = B_s is phi_0(s), so
  <psi_s, N psi_s> = n_0(s). Correct.
- Jensen on the spectral measure of N at psi_s:
  <psi_s, e^(-uN) psi_s> >= e^(-u n_0(s)). delta_2 = e^(-(t-s)(0 + nu_1)).
  So m(t) - m(s) >= (t - s)(nu_1 - 2 n_0(s)). Correct.
- n_0(s) <= n_0(0): Lemma KIN-CVX (log lambda_0 convex; its derivative is
  -n_0, so n_0 is non-increasing). Correct.
- Pointwise form: n_0 + n_1 = trace of N on span(phi_0, phi_1) >= nu_0 + nu_1
  = nu_1 (Ky Fan, for an orthonormal pair in the form domain of N; for
  t > 0 the phi_i lie in the range of e^(-tN/2)). Correct.

**C4, nu_1 = 3/2 on one-sheet boxes (L112): HOLDS AFTER CORRECTION.** The
value is right; one clause of the reason is wrong. In the sequential basis
the N-eigenvalue is sum_k [L_k(L_k+1) + R_k(R_k+1)], with L_k, R_k the
couplings of j_1..j_k on the left and on the right. If all L_k = 0 then
j_1 = 0, j_2 = 0, ..., and j_n = 0 (L_(n-1) = 0 couples to j_n), so a
non-constant vector has some L_k != 0. L_k and R_k are both congruent to
j_1 + ... + j_k mod 1. Half-integer: both >= 1/2, cut sum >= 3/2. Integer:
L_k >= 1 but R_k may be 0 (for n >= 4, e.g. j = (1/2, 1/2, 1/2, 1/2),
L_2 = 1, R_2 = 0), so the cut sum is >= 2 + 0, not ">= 2 x 2". Corrected
text: "an integer L_k >= 1 gives at least 2 > 3/2, whatever R_k is." The
value 3/2 is taken at chi_(1/2)(Phi_2 Phi_1^(-1)): correct.

**C4, the one-sheet corollary (L113).** For 0 <= s <= t:
m(t) - m(s) >= (t - s)(3/2 - 2 n_0(0)) >= 0 when n_0(0) <= 3/4. Correct.

**C4, scope and wording points.**
- L106 says "any compact group". The Wilson form holds for any compact
  group with a positive class-function weight. The heat-kernel form needs
  Casimirs, so a compact Lie group. Scope note, no change to results.
- L108 "(the smallest is 0, on the constants)": on a box with a transverse
  plaquette the kernel of N on K is larger (the row says so at L152);
  then nu_1 = 0 and the bound is empty. Better: "(the smallest is 0; its
  eigenspace contains the constants)".
- L114 "This is Corollary KIN-2 of row 1076 with its bracket bounded":
  loose. KIN-2 bounds lambda_1(beta_L) by lambda_1(infinity) (operator
  order) and leaves the bracket log lambda_0(infinity) - log lambda_0(beta_L).
  Bounding that bracket by Rayleigh alone gives
  m(beta_L) - m(infinity) >= log <psi, D psi> <= 0, which never gives
  monotonicity. DIL also bounds lambda_0 lambda_1 through Lambda^2, which
  adds the term -log delta_2 > 0. Suggested text: "This sharpens Corollary
  KIN-2 of row 1076: the bracket is bounded by Rayleigh, and lambda_1 is
  bounded through Lambda^2 instead of operator order." The volume remark
  that follows is right (n_0(0) grows with the box).
- Example KIN-6 (L143): psi = the N = a vector, <psi, D psi>^2 = e^(-2ta),
  delta_2 = e^(-t(a+c)), bound -t(a - c) = the true value. Correct; Jensen
  is exact there because psi is an eigenvector of N.
- Q_8 (L144): step 3a. HOLDS.

Verdict C4: Proposition DIL HOLDS (Wilson form: any compact group; heat-
kernel form: compact Lie groups). The one-sheet corollary HOLDS, with the
reason for nu_1 = 3/2 corrected as above. The GUIDE thresholds (3.3 at
n = 2, 2.2 at n = 3) are checked in step 7.

**C5, Corollary N2-SMALL.** Checked line by line in step 3b; it uses DIL's
pointwise form and nu_1 = c_2 = 3/2, both checked here. Verdict C5: HOLDS.
Remark L118 HOLDS AFTER CORRECTION (bound 0.23 at beta_M = 1, not 0.69).

### Step 6. C6 (Remark CUM) and C7 (the three failures of step (S)). DONE.

**C6, Remark CUM (L120).**
- Asymptotics: with I_nu ~ e^(beta)(2 pi beta)^(-1/2) e^(-nu^2/(2 beta)),
  a_n ~ e^(-(n^2-1)/(2 beta)) and
  k_beta(n, m) ~ C e^(-(n^2+m^2)/(2 beta)) 2 sinh(nm/beta), so
  A(n, m) ~ C' e^(-(n^2+m^2)/beta) 2 sinh(nm/beta). Correct. The next
  equality drops the exponential factor; corrected text:
  "= e^(-(n^2+m^2)/beta) (2nm/beta)(1 + n^2 m^2/(6 beta^2) + ...)".
  The leading term is rank one in u_n = n e^(-n^2/beta), the next is rank
  one in n^3 e^(-n^2/beta) with weight 1/(6 beta^2). I checked the same
  Schur complement from the moment form k_beta(n, m) =
  (2/pi) int sin(n th) sin(m th) e^(beta cos th) d th, Gaussian moments
  (p-1)!! beta^(-(p+1)/2): in the basis (n, n^3) the Gram matrix is
  proportional to [[1, -1/(2 beta)], [-1/(2 beta), 15/(36 beta^2)]],
  determinant 1/(6 beta^2). Consistent.
- phi_0 ~ n e^(-t c_n/2), phi_1 ~ the part of n^3 e^(-t c_n/2) orthogonal
  to it, so r ~ (n^2 - E_p n^2)/sd = (c - mu)/sigma, linear in c since
  n^2 = 2c + 1. Correct at leading order; error terms not controlled, as
  the row says.
- For linear r = (c - mu)/sigma: E_p[(r^2 - 1) c] = E_p[(c - mu)^2 c]/sigma^2 - mu
  = kappa_3/kappa_2 + mu - mu = kappa_3/kappa_2. Exact algebra. Correct.
- In the corner the limit weights are p_n proportional to n^2 e^(-t c_n);
  for small t this is close to a Gamma(3/2) law in c (kappa_3/kappa_2 =
  2/t > 0), and for large t a two-point law on c in {0, 3/2} with small
  weight q at 3/2 (kappa_3/kappa_2 = (3/2)(1 - 2q) > 0). So "skewed to the
  right" fits both ends of the corner. ARGUED, as marked.
- **The Q_8 sentence: HOLDS AFTER CORRECTION.** "For frozen Q_8 near the
  point mass the vacuum weights are 1/8, 3/8, 4/8 on rising electric
  cost". The weights are right (d_rho^2/8), but the order is not. In the
  KIN-7 limit the electric cost of a character is 1 - (its D eigenvalue):
  sigma costs 1 - A_L = 16 eta, tau costs 1 - B_L = 12 eta. So on rising
  cost the weights are 1/8 (trivial, 0), 4/8 (tau, 12 eta), 3/8
  (sigma x 3, 16 eta). With these costs: mean 12 eta, kappa_2 = 24 eta^2,
  kappa_3 = (1/8)(-12)^3 + (3/8)(4)^3 = -192 (units eta^3) < 0: skewed to
  the left. Corrected text: "For frozen Q_8 near the point mass the
  vacuum weights are 1/8, 4/8, 3/8 on rising electric cost (0, 12 eta,
  16 eta for the trivial character, tau and the three sigma): skewed to
  the left, kappa_3/kappa_2 = -8 eta." The conclusion stands.
- A confirmation of "That is Example KIN-7 in this language": with these
  weights the linear-r excited state has weights p r^2 = 3/4 on the
  trivial character, 0 on tau, 1/4 on sigma; its cost is 4 eta. That is
  the excited state of KIN-7 (row 1076 L406: "three quarters of it is the
  trivial character, and it pays 4 eta"). And kappa_3/kappa_2 = -8 eta is
  exactly the KIN-7 limit of m(beta_L) - m(infinity). So in the KIN-7
  limit the cumulant reading is exact for Q_8, to first order in eta.
- The GUIDE sentence ("within 25 per cent ... at all 45 points ... and
  above it at every point") is checked in step 7.

Verdict C6: the ARGUED reading HOLDS as ARGUED (not a proof; the row says
so). Two text corrections: the dropped factor in the sinh expansion, and
the order of the Q_8 weights.

**C7, the three written failures of step (S) (L122-L126).**
- Way 1 (DIL). The pointwise bound n_1 - n_0 >= 3/2 - 2 n_0(t) gives no
  sign where n_0(t) > 3/4. That is a fact about the bound. Where it
  happens (n_0(0) > 3/4 for beta_M above about 3.3 at n = 2) is GUIDE. Two
  precisions: since n_0(t) is non-increasing, Way 1 still gives the sign
  for t large enough at every beta_M; it fails only at small t. And for
  beta_M in (3/2, 3.3) the GUIDE says n_0(0) <= 3/4, so there Way 1 is not
  a failed way but an unproved bound (the hand bound of N2-SMALL is
  crude). The row's own wording ("FAILS beyond the dilute range ...;
  proved range beta_M <= 3/2") is consistent with this. HOLDS.
- Way 2 (Lemma SC). If r(1) > 1, then r^2 - 1 > 0 at n = 1, < 0 while
  -1 < r < 1, > 0 once r < -1: the pattern (+, -, +), and the
  single-crossing step does not apply. Correct. That r(1) > 1 occurs at
  large beta_M is GUIDE (step 7). It also fits Remark CUM: in the corner,
  r(1) ~ mu/sigma, which tends to sqrt(3/2) = 1.22 for the Gamma(3/2) law
  (small t) and is below 1 for the two-point law (large t). HOLDS.
- Way 3 (two crossings). Let f = r^2 - 1 with pattern (+, -, +), c = g(xi)
  with g convex and non-decreasing, xi increasing in n, and l the chord of
  g through the two ends of the block where f <= 0. Then g - l <= 0 inside
  the block and >= 0 outside, so f (g - l) >= 0 everywhere and
  E_p[f c] >= E_p[f l(xi)] = gamma E_p[f xi], gamma = slope of the chord
  >= 0 (E_p f = 0 removes the constant). So <xi>_1 >= <xi>_0 for one such
  xi would give (S). Correct (Karlin and Novikoff's method; if the
  negative block is one point, use a supporting line). The tried xi:
  xi = c is circular, correct. xi = -kappa_n with kappa_n = a_n^2 e^(-t c_n):
  from E K_t E Omega_i = lambda_i Omega_i and phi_i = K_t^(1/2) E Omega_i/sqrt(lambda_i),
  <phi_i, K_t phi_i> = norm(K_t E Omega_i)^2/lambda_i = lambda_i int e^(-beta cos) Omega_i^2,
  the identity of L125. Correct; it gives no sign by itself, as the row
  says. The virial attempt is described, not written out; I cannot check
  it beyond its description. "FAILS as tried" is a statement about the
  attempts. HOLDS.
- Stop rule: one named step (S), three written ways, each with a named
  failing point. Ways 1 and 2 fail at points located by GUIDE runs; Way 3
  fails for lack of an ordered moment. The scope statement (L173) limits
  "FAILS" to the three methods as applied at n = 2. Consistent with the
  row's stop rule.

Verdict C7: HOLDS (each written failure is correctly described and
scoped). No item of C7 claims a negative beyond its method.

### Step 7. C8 (the kill-test code) and the GUIDE claims. DONE.

Read in full: `runs/gap-descent-sign/su2box.py` (124 lines),
`n2_reduction.py` (31 lines), all ten logs. My scripts are in
`/private/tmp/claude-501/-Users-jonreilly-Projects-Physics--claude-worktrees-peaceful-heisenberg-e2d2a0/b3f5c21a-8638-4944-b69d-c639619895d6/scratchpad/gds-check/`
(`json_check.py`, `indep_checks.py`; copies of the row's scripts in
`rerun/`). All runs: one thread, one job at a time, largest matrix 381 x 381
for the reruns. Every result below is GUIDE grade.

**Code read line by line (su2box.py).**
- 6j: the Racah formula with doubled arguments; the four triads
  (abc), (aef), (dbf), (dec), the sums t_1..t_4, s_1..s_3 and the
  triangle factor are the standard ones. Independent check: against
  sympy's exact `wigner_6j`, 2813 cases (every {a b c; b+-1 a+-1 1/2} with
  doubled spins up to 12, plus 400 random 6j up to doubled 16): largest
  error 7.4 x 10^(-16).
- Basis: triples with the triangle rule and integer sum, every 2j <= 2Jmax;
  model n2 is the block j_3 = 0. Matches L29.
- X12, X23: 0.5 sqrt(d_1 d_1' d_2 d_2') {j_1 j_2 j_3; j_2' j_1' 1/2}^2 and the
  mirror formula, as in L31 with J = 1/2 and x = chi_(1/2)/2. The two hand
  entries come out exactly: X12[(1/2,1/2,0) <- (0,0,0)] = 0.5 and
  2 X23[(1/2,0,1/2) <- (1/2,1/2,0)] = 0.5. The 6j symmetry used for
  symmetry of X12 holds ({j_1 j_2 j_3; j_2' j_1' J} = {j_1' j_2' j_3; j_2 j_1 J}).
- K, D, N per model: n3, 2s, n2 exactly as in L30, L35-L37 and Lemma KIN.
- The operator diagonalised is D^(1/2) K^(1/2) E^2 K^(1/2) D^(1/2), the
  B form of S* D S; E^2 is the exponential of the truncated X12 + X23
  (rescaled, which leaves gaps and eigenvectors unchanged). Top three
  eigenpairs; m, n_0, n_1 as defined. Correct.
- The commutator is measured on the interior (2j <= 2Jmax - 2), where one
  step of X stays in the basis, so there it is exact up to rounding.
  Correct.

**Reproduction.** A copy of su2box.py run as `n3 10` reproduces
`log_n3_10.txt` digit for digit.

**Independent cross-check of the 6j matrices.** At beta_L = infinity the
two-sheet face gap (which uses the full X12, X23) must equal the n = 2
one-sheet face gap. My own n = 2 code (power-series Bessel functions, no
6j) gives 4.2118995134, 2.2829867354, 2.4210796688 at beta_M = 0.5, 2.4, 4;
the logged two-sheet values are the same to all ten digits. Confirms
check (iv) of L50 by a different implementation.

**Claims from the saved data (`out_*.json`, read only).**
- Test A, every truncation (10, 14, 18, 22): m(beta_L) - m(infinity) > 0
  at all grid points, strictly decreasing in beta_L at every grid step;
  m(t) non-decreasing on the t grid; least n_1 - n_0 = 1.2679. Confirms
  L65.
- Test A agreement, 14 against 18: Wilson differences 2.1 x 10^(-11)
  (beta_M <= 4), 1.8 x 10^(-10) (6), 5.6 x 10^(-8) (8); n_1 - n_0 at most
  5.1 x 10^(-7). 18 against 22 at beta_M = 8: 1.8 x 10^(-12) and
  2.2 x 10^(-11). 10 against 14 (beta_M <= 4): 1.2 x 10^(-8) at most.
  Confirms L65 and L82.
- Test B, every truncation (10, 14, 18): positive and strictly decreasing
  in beta_L; m(t) non-decreasing; least n_1 - n_0 = 0.97096. 14 against 18:
  Wilson differences 2.0 x 10^(-11) (beta_M <= 4), 1.6 x 10^(-7) (6),
  2.6 x 10^(-5) (8); n_1 - n_0 (t > 0) 6.2 x 10^(-6) (6), 1.3 x 10^(-3) (8).
  Confirms L78 ("10^(-11)" is 2 x 10^(-11) at beta_M = 0.5; immaterial).
- **Two text corrections (HOLDS AFTER CORRECTION).** (1) L52 says
  "2Jmax = 10 (dimension 381; beta_M <= 4 only)". That holds for test A.
  For test B the 10 run covers beta_M up to 8 and is not converged at 6
  and 8: against 14, n_1 - n_0 moves by 0.073 and 0.32, the Wilson
  difference by 6.7 x 10^(-4) and 4.3 x 10^(-3); the signs agree.
  Corrected text: "Truncations 2Jmax = 10 (dimension 381; test A for
  beta_M <= 4 only; test B for all beta_M, not converged at beta_M = 6, 8),
  14 (dimension 932), 18 (dimension 1855)." The same applies to L80 "at
  three (A: two for beta_M > 4) truncations": for B at beta_M = 6, 8 two
  truncations agree, and the third has the same signs. (2) The test B
  table row beta_M = 8 quotes truncation 14 (m(infinity) = 2.54032609,
  least difference +8.70e-3, n_1(0) = 10.0167); truncation 18 gives
  2.54032308, +8.67e-3, 10.0168. The row's caveat "good to about four
  digits only" covers this.
- L78 caveat on the double level: harmless, and in fact not needed. On
  the degenerate pair {phi x omega, omega x phi} the matrix of N is a
  multiple of the identity: the cross terms of C_(j_1), C_(j_3) vanish by
  orthogonality, and the cross term 2 J^R_A . J^L_B vanishes because J_i
  maps class functions into the spin-1 part under conjugation (Schur). So
  n_1(0) does not depend on the vector returned. The logged n_1(0) agree
  across truncations (4.1692, 4.1693, 4.1693 at beta_M = 4), as this
  predicts. A remark, not a correction.

**n2_reduction.py (L104, L120, L123) read line by line.** 60 characters,
the matrix of L89-L92, signs fixed by r(1) > 0, cumulants of c under p.
Correct. From its log (45 points): r is strictly decreasing at all 45
(a GUIDE check of TP-2 (iii)); r(1) <= 1 for beta_M <= 6 (largest 0.9891
at beta_M = 6, t = 0); r(1) > 1 with the pattern (+, -, +) at beta_M = 8
(t = 0, 0.05), 12 and 16 (t = 0, 0.05, 0.2); r(1) = 1.0519 and 1.1409 at
beta_M = 8, 16, t = 0. Confirms L104, with one scope precision: "at all t"
means the five grid values t in {0, 0.05, 0.2, 0.6, 1.5}. kappa_3/kappa_2
divided by n_1 - n_0 lies in [1.0000, 1.2388] (largest at beta_M = 3,
t = 0): within 25 per cent. At the closest point (beta_M = 0.5, t = 1.5) a
rerun of a copy gives kappa_3/kappa_2 - (n_1 - n_0) = +1.9 x 10^(-5), so
"above it at every point" holds strictly. Confirms L120. Where
3/2 - 2 n_0 < 0 the log gives n_1 - n_0 >= 1.55. Confirms L123. The
crossing of n_0(0) = 3/4: between beta_M = 3 (0.645) and 4 (1.078),
linear interpolation 3.24, at n = 2; between 2 (0.580) and 2.4 (0.952),
interpolation 2.18, at n = 3. Confirms L114 ("near 3.3", "near 2.2").

Verdict C8: the code HOLDS as GUIDE: basis, 6j symbols, matrices and
operators are right, the runs reproduce, and two or three truncations
agree where the row says so, with the two text corrections above. No
numeric result here is a proof step.

### Step 8. Remaining lines, verdicts, what was not covered, RESULT. DONE.

**Remaining lines of row 1081, checked briefly.**
- L42, L44: `scripts/lab_ops.py` is absent in this checkout (confirmed);
  `parts/gap.md` has changed since the row ran (its L156, L158 now carry
  check results), so the cited line numbers have drifted. No science
  content.
- Dependencies on row 1076. Row 1081 uses Lemma KIN (c), Identity KIN-5
  and Lemma KIN-CVX as stated. I checked the parts it uses for DIL and
  N2-SMALL (log-convexity by Laplace transforms; -n_0 as the derivative;
  Jensen; Ky Fan), and the theta-graph remark (L84) confirms KIN (c) on
  the two kill-test boxes without KIN. Check 1079 (gpt-6-astra xhigh,
  `library/gap-bridge-vectors-check-astra.md`, read only at its verdict
  lines 364, 370, 373) reports KIN (c) HOLDS, KIN-5 HOLDS for t > 0 with
  simple positive eigenvalues, KIN-CVX HOLDS when the two eigenvalues are
  positive. That is its finding, not mine. Row 1081 uses KIN-5 also at
  t = 0 (one-sided); there n_i(0) is finite at n = 2 (step 4), so this
  is fine.
- Context from `parts/gap.md` L158 (summary of check 1079): it finds
  FAILS as written "the inference from the Wilson Q_8 box to the
  heat-kernel (FLUX-EXC)" and "the claim that every proof must use
  continuity of the group". Row 1081 uses Q_8 only in the Wilson form
  (L144; checked in step 3a), so no proved item of row 1081 is affected.
  Its readings L80, L140, L146 that contrast SU(2) with Q_8 should be read
  as Wilson-form statements about Q_8. In particular L140 ("an argument
  ... would need a property ... that a point mass violates") binds only a
  proof that would also apply to the Wilson form of a finite group.
- L148-L154 (several sheets). "Any transverse tree: the kernel of N on K
  is the constants": correct (a function invariant under all cut
  rotations and G is gauge invariant on a forest, hence constant). The
  transverse-plaquette observation (class functions of a layer's
  transverse plaquette are fixed by every rho_c(W)): correct. The
  second-order formula: with B_t = (P_0 + eps P_1 + ...) M (P_0 + eps P_1 + ...),
  eps = e^(-3t/4), the unperturbed operator vanishes on Ran P_1 and
  P_1 phi_i = 0, so lambda_i(t) = lambda_i + eps^2 norm(P_1 M phi_i)^2/lambda_i + ...:
  the formula for l_i and n_i HOLDS. Notation: in L153 "lambda_i(infinity)"
  means t = infinity, while elsewhere in the file infinity means
  beta_L = infinity (t = 0); suggest "lambda_i(t = infinity)". The lowest
  non-zero level N = 3/2 there needs two half-integer cut spins, since a
  single half-integer vertical spin cannot close around the square;
  consistent. The hand value l_0 ~ beta_M^4/16: I recomputed it
  (P_1 M phi_0 ~ (beta/2)(beta/4) sum over the four vertical plaquettes of
  chi_(1/2)(P_mu), orthonormal); correct at leading order. The value
  l_1 ~ beta_M^2/4: I checked only that it is of order beta_M^2; the
  coefficient is not checked. ARGUED, as marked.
- L160-L177 (marks, scope, credits): consistent with the steps, after the
  corrections below. The scope paragraph (L173) is accurate.

**Verdicts.**

| Item | Lines | Verdict |
|---|---|---|
| Test: DIL on frozen Q_8 against KIN-7 | L144 | HOLDS. The Wilson bound tends to -12 eta, below the true -8 eta; it lies below the true difference at 15 finite points (GUIDE, independent 5 x 5 script). It does not give the false sign. |
| Test: N2-SMALL at beta_M = 3/2 by hand | L117 | HOLDS. n_0(0) <= 0.2109375 x 4.481689/1.28125 = 0.737839 <= 3/4; every inequality checked. |
| Remark after N2-SMALL | L118 | HOLDS AFTER CORRECTION: "against the bound 0.23" (not 0.69); 0.097 at beta_M = 3/2 against 0.738. |
| C1 spin-network form, one sheet n = 3, two sheets n = 2 | L25-L38, L84 | HOLDS, with the recalled Edmonds (7.1.6). Both hand checks redone; the two-box identification checked on three Casimirs; the theta-graph remark checked. |
| C1, N diagonal for every n | L32, L131 | HOLDS. |
| C1, non-negative face part for every n | L32, L132 | HOLDS AFTER CORRECTION: proved for n <= 3 only (entries are squares there); for n >= 4 the entry is a product of left and right recoupling coefficients with independent intermediate spins, and its sign is OPEN (not proved, not refuted here). Corrected text in step 4. |
| C2 Lemma TP-2 | L94-L96 | HOLDS, with the recalled theorems of Karlin-McGregor and Jentzsch. |
| C2 reduction to Cov_p(r^2, c) | L98-L100 | HOLDS. |
| C3 Lemma SC | L102-L104 | HOLDS (add finiteness of the expectation for a general non-decreasing sequence). Its GUIDE sentence holds on the five grid values of t. |
| C4 Proposition DIL | L106-L111 | HOLDS: Wilson form for any compact group with a positive class-function weight; heat-kernel form for compact Lie groups. |
| C4 nu_1 = 3/2 on one-sheet boxes | L112 | HOLDS AFTER CORRECTION of the reason: "an integer L_k >= 1 gives at least 2 > 3/2, whatever R_k is" (R_k can be 0 for n >= 4). The value is right. |
| C4 one-sheet corollary | L113-L114 | HOLDS. Wording: L114's "Corollary KIN-2 with its bracket bounded" understates DIL (DIL also bounds lambda_0 lambda_1 through Lambda^2); suggested text in step 5. GUIDE crossings 3.3 and 2.2 confirmed (3.24 and 2.18 by interpolation). |
| C5 Corollary N2-SMALL | L116-L117 | HOLDS. |
| C6 Remark CUM | L120 | HOLDS as ARGUED. Two corrections: the sinh expansion keeps its factor e^(-(n^2+m^2)/beta); the Q_8 weights on rising electric cost are 1/8, 4/8, 3/8 (costs 0, 12 eta, 16 eta), kappa_3/kappa_2 = -8 eta (left skew; equal to the KIN-7 limit of m(beta_L) - m(infinity)). GUIDE sentence confirmed (ratio in [1.0000, 1.2388]; above at all 45 points, by 1.9 x 10^(-5) at the closest). |
| C7 three failures of step (S) | L122-L126 | HOLDS. Precision for Way 1: it fails only at small t; for 3/2 < beta_M < 3.3 it is an unproved bound, not a failed one. The two-crossing reduction of Way 3 is correct. |
| C8 kill-test code and runs | L48-L82, scripts | HOLDS as GUIDE. 6j matches sympy to 7.4 x 10^(-16) (2813 cases); a rerun reproduces log_n3_10.txt exactly; the two-sheet face gap equals an independent n = 2 code to ten digits; all signs and monotonicity claims hold in the saved data; truncations agree as stated. Two text corrections: L52 (truncation 10 for test B covers beta_M <= 8 and is not converged at 6, 8) and the test B row beta_M = 8 (quoted from truncation 14; 18 gives 2.54032308, +8.67e-3). |
| Several sheets | L150-L154 | HOLDS for the tree statement, the plaquette kernel and the second-order formula; l_0 checked at leading order; l_1 ARGUED, coefficient not checked. |

No item FAILS. No line of row 1081 claims a mass gap, and none is claimed
here.

**What this check did not cover.** The proof of Lemma KIN itself (row
1076; used as stated, confirmed on the two boxes by the theta-graph
computation, reported HOLDS by check 1079). The coefficient of l_1 in
L154. The virial attempt of Way 3 beyond its description. Reruns at
truncations 14 to 22 (read from the saved data; only truncation 10 was
rerun). The sign question for n >= 4 (not tested). This is a
same-provider check (Anthropic model checking an Anthropic model); it is
not an independent check in the sense of the lane's rules.

Checked line by line by Claude Opus 5.5 (max), laptop subagent.

RESULT: Row 1083 (Claude Opus 5.5 max, laptop subagent; SAME-PROVIDER check of row 1081, written by Claude Fable 5.2 medium; row 1082 not read). No item FAILS. HOLDS: Proposition DIL (tested first: on frozen Q_8 its Wilson bound tends to -12 eta, below the true KIN-7 dip -8 eta, and lies below the true difference at 15 finite points, GUIDE); Corollary N2-SMALL (by hand at beta_M = 3/2: n_0(0) <= 0.7378 <= 3/4); Lemma TP-2 and the reduction n_1 - n_0 = Cov_p(r^2, c); Lemma SC; the spin-network form with N diagonal for one sheet n = 3 and two sheets n = 2; the three written failures of step (S); Remark CUM as ARGUED; the kill-test code as GUIDE (6j equal to sympy's to 7.4e-16; rerun reproduces the log; two-sheet face gap equal to an independent n = 2 code to ten digits; truncations agree as stated). HOLDS AFTER CORRECTION: the non-negative face part for every n (proved for n <= 3 only; n >= 4 OPEN); the reason for nu_1 = 3/2 (integer case gives >= 2 + 0, not 2 x 2); the Q_8 weights on rising electric cost are 1/8, 4/8, 3/8 (kappa_3/kappa_2 = -8 eta, equal to the KIN-7 limit); the bound in L118 is 0.23, not 0.69; the dropped factor in the sinh expansion; truncation 10 of the two-sheet test is not converged at beta_M = 6, 8. Output `library/gap-descent-sign-check-opus.md`.
