lead: anthropic/claude-fable-5-2/medium laptop-subagent
row: 1081

# The descent sign (FLUX-EXC) for SU(2) on one-sheet boxes (row 1081): working file

Note on the save protocol. One read of FINISH row 1081 came before this file was created. This file was created by the second tool call.

## Plan (eight steps)

1. Read row 1081, brief P2 (section 7.4 of row 1076), sections 6.1 and 6.4 of `library/gap-bridge-vectors-max.md`. Fix the exact statement and the operators.
2. Prior-work grep: `library/open-core.md`, `parts/gap.md`, FINISH rows, for the statement (FLUX-EXC), (MON-L), descent sign.
3. Kill test A (GUIDE): SU(2), n = 3, one sheet. Basis (j_1, j_2, L). Compute m(beta_L, beta_M) - m(infinity, beta_M) at two truncations.
4. Kill test B (GUIDE): two sheets on a transverse path of three sites. Same quantity, two truncations.
5. If no dip: n = 2 by hand (one variable on [0, pi], weight sin^2).
6. If no dip: the structure for n at least 3; attempt a proof; apply the tests (Q_8 and 2T must fail, U(1) may pass, Example KIN-6).
7. Several sheets, only if step 6 gives a mechanism.
8. Marks, scope of negatives, credits, RESULT line.

## Step log

### Step 1 (reading; the model fixed). DONE.

Read: FINISH row 1081; `library/gap-bridge-vectors-max.md` sections 6.1, 6.3, 6.4, 7.4 (row 1076, by Claude Fable 5.2 max; check 1079 not returned when this row started). I use Lemma KIN as stated there. I did not re-prove it. It is not yet cross-checked.

**One-sheet box.** Transverse sites x, y; one transverse link. Slice sites (k, x), (k, y), k = 1..n. Variables Phi_k in SU(2) (k = 1..n), after the reduction a = 1 of Lemma KIN (b). G = SU(2)^2 acts by Phi_k -> g Phi_k h^(-1), same (g, h) for all k. K = L^2(SU(2)^n)^G. Face potential V_f = - beta_M sum_{k<n} x(Phi_{k+1} Phi_k^(-1)), x = (1/2) tr. K_Phi = product over k of convolution with w_M. Cuts: (k, x) and (k, y), k = 1..n-1. C_(k,x) is the Casimir of left rotation of Phi_{k'}, k' > k; C_(k,y) the same for right rotation. So the face is the transfer operator of the SU(2) x SU(2) principal chiral chain (the O(4) chain) on n sites with free ends, on singlets, and N = sum_k (C^L_{>k} + C^R_{>k}).

**Spin-network basis (used in steps 3 to 6).** Peter-Weyl: L^2(SU(2)) = sum_j V_j x V_j. A G-singlet needs the left spins j_1..j_n coupled to 0 and the right spins j_1..j_n coupled to 0.
- n = 2: j_1 = j_2 = j; one vector per j, the character chi_j(Phi_2 Phi_1^(-1)). Class functions, as in the brief.
- n = 3: one vector |j_1 j_2 j_3> per triple with the triangle condition and j_1 + j_2 + j_3 an integer. No multiplicity.
- On singlets C^L_{>k} = C^L_{<=k}. For n = 3: C_{>1} = j_1(j_1+1) and C_{>2} = j_3(j_3+1), for left and for right. So **N = 2 j_1(j_1+1) + 2 j_3(j_3+1) is diagonal**, and D = lambda_{j_1}(beta_L)^2 lambda_{j_3}(beta_L)^2 (Wilson) or e^(-tN) (heat kernel). K_Phi = lambda_{j_1} lambda_{j_2} lambda_{j_3} at beta_M, diagonal.
- Multiplication by chi_J(Phi_2 Phi_1^(-1)) keeps j_3 and has entries <j_1' j_2' j_3| chi_J(21) |j_1 j_2 j_3> = sqrt(d_1 d_1' d_2 d_2') {j_1 j_2 j_3; j_2' j_1' J}^2 >= 0, d = 2j+1 (tensor-operator formula for a scalar product, once for the left indices and once for the right; the two phases cancel). Hand checks: at j_3 = 0 it gives 1 (chi_J chi_j = sum of chi_j'); for |1/2 1/2 0> -> |1/2 0 1/2> under chi_(1/2)(32) it gives 1/2, and the direct integral gives <tr(AB), tr(A)tr(B)> = 1 - 1/2 = 1/2. Numeric check in step 3: the matrices X12 and X23 must commute.
- General n: in the sequential coupling tree from one end, all C_{>k} are diagonal at once, so N is diagonal for every n. The face part has non-negative entries. This is the structure named in the brief, item (2).

**Two-sheet box, n = 2 (transverse path x, y, z).** Variables Phi_a(k), Phi_b(k), k = 1, 2. Put A = Phi_a(1)^(-1) Phi_a(2), B = Phi_b(2) Phi_b(1)^(-1). Both are fixed by g_x, g_z and conjugated by g_y. So K = functions of (A, B) under joint conjugation. The one-sheet n = 3 space is the same: there A' = Phi_1^(-1) Phi_2, B' = Phi_2^(-1) Phi_3, conjugated by h. Under this identification: spin of A = j_1, spin of B = j_3, and the rotation A -> A W^(-1), B -> W B (the cut (1, y)) has Casimir j_2(j_2+1). Hence for two sheets, n = 2:
  V_f = - beta_M (x(A) + x(B)) (the same matrix E as one sheet, n = 3);
  K_Phi = lambda_{j_1}(beta_M)^2 lambda_{j_3}(beta_M)^2;
  D = lambda_{j_1}(beta_L) lambda_{j_2}(beta_L) lambda_{j_3}(beta_L); heat kernel N = j_1(j_1+1) + j_2(j_2+1) + j_3(j_3+1).
So both kill tests use the same two matrices X12, X23 and different diagonal operators. No 6j symbol enters D in this basis.

### Step 2 (prior-work grep). DONE.

Grep of `library/open-core.md`, `parts/gap.md`, and FINISH.md for FLUX-EXC, MON-L, descent sign, Lemma KIN, KIN-7. `open-core.md`: no hit. `parts/gap.md` L156, L158: (MON-L) is named as open, with rows 1072, 1076 and this row 1081 as the proof row. FINISH: rows 1072-1076, 1079 (check of 1076, queued), 1080 (reading), 1081. `library/descent.md` and `descent-draft.md` are about a different descent (H-M, Theorems A and B). No other row covers (FLUX-EXC) for SU(2) at n >= 3 or two sheets. The n = 2 GUIDE run of row 1076 section 6.4 is on file (no dip for SU(2), n = 2) and is not redone except as a regression check of my code.

`scripts/lab_ops.py` is not in this checkout, so there is no numeric lock to take. Runs are one at a time, one BLAS thread.

### Steps 3 and 4 (kill tests A and B; GUIDE). DONE: no dip found.

Script: `runs/gap-descent-sign/su2box.py` (double precision, one BLAS thread, one job at a time; logs `log_*.txt`, data `out_*.json` in the same folder). It builds X12 and X23 from the 6j formula of step 1 (Racah's sum), E^2 = exp(beta_M (X12 + X23)) by one symmetric eigen-decomposition, and takes the top three eigenvalues of D^(1/2) K^(1/2) E^2 K^(1/2) D^(1/2). Truncation: all 2j <= 2Jmax. The runs refute or guide. They discharge no proof step.

Checks of the code. (i) X12 and X23 commute on the interior of the truncated basis to 7 x 10^(-15) (they are multiplications by x(Phi_2 Phi_1^(-1)) and x(Phi_3 Phi_2^(-1)); this tests the 6j formula and its signs). (ii) Spectrum of X12 inside [-1, 1]. (iii) Model n2 (block j_3 = 0, 2Jmax = 40) gives positive differences, as row 1076 section 6.4 reported for n = 2. (iv) The two-sheet model at beta_L = infinity gives m equal to the n = 2 one-sheet value with a double first excited level (m = 2.2829867354 at beta_M = 2.4 in both): the two sheets decouple on the face, as they must on a transverse path.

Grid. beta_M in {0.5, 1, 2, 2.4, 3, 4, 6, 8}. Wilson form: beta_L at 24 values in [0.05, 1000]. Heat-kernel form: t at 18 values in [0, 3], with n_0(t), n_1(t) read from the eigenvectors. Truncations 2Jmax = 10 (dimension 381; beta_M <= 4 only), 14 (dimension 932), 18 (dimension 1855).

**Kill test A (one sheet, n = 3).**
| beta_M | m(infinity) | least m(beta_L) - m(infinity) on the grid | least n_1 - n_0 on the t grid | n_0(0) | n_1(0) |
|---|---|---|---|---|---|
| 0.5 | 4.03746520 | +4.63e-3 (at beta_L = 1000) | 1.5005 | 0.0029 | 2.3196 |
| 1 | 2.66283430 | +4.73e-3 | 1.5013 | 0.0469 | 2.4110 |
| 2 | 1.80446197 | +4.50e-3 | 1.4996 | 0.5799 | 2.8278 |
| 2.4 | 1.76681077 | +4.60e-3 | 1.4860 | 0.9521 | 3.2505 |
| 3 | 1.78511129 | +5.30e-3 | 1.4371 | 1.5530 | 4.2069 |
| 4 | 1.82478377 | +7.04e-3 | 1.3522 | 2.5640 | 6.0927 |
| 6 | 1.86194096 | +1.06e-2 | 1.2923 | 4.5732 | 9.9049 |
| 8 | 1.87883955 | +1.42e-2 | 1.2679 | 6.5754 | 13.7008 |
The difference m(beta_L) - m(infinity) is positive at every grid point and decreases in beta_L at every grid step. The least value is always at the largest beta_L, where it tends to 0 from above. Truncations 14 and 18 agree to 2 x 10^(-11) (beta_M <= 4), 2 x 10^(-10) (beta_M = 6), 6 x 10^(-8) (beta_M = 8) in the Wilson differences, and to 5 x 10^(-7) or better in n_1 - n_0.

**Kill test B (two sheets on a transverse path of three sites, n = 2).**
| beta_M | m(infinity) | least m(beta_L) - m(infinity) | least n_1 - n_0 | n_0(0) | n_1(0) |
|---|---|---|---|---|---|
| 0.5 | 4.21189951 | +3.00e-3 | 1.4982 | 0.0029 | 1.5011 |
| 1 | 2.99368776 | +2.95e-3 | 1.4737 | 0.0439 | 1.5176 |
| 2 | 2.29886497 | +2.61e-3 | 1.2749 | 0.4835 | 1.7856 |
| 2.4 | 2.28298674 | +2.58e-3 | 1.1760 | 0.7862 | 2.0764 |
| 3 | 2.33334858 | +2.91e-3 | 1.0568 | 1.2895 | 2.7455 |
| 4 | 2.42107967 | +4.01e-3 | 0.9710 | 2.1569 | 4.1693 |
| 6 | 2.50397387 | +6.38e-3 | 1.0119 | 3.8951 | 7.1080 |
| 8 | 2.54032609 | +8.70e-3 | 1.0723 | 5.6303 | 10.0167 |
Positive and decreasing in beta_L on the whole grid. Truncations 14 and 18 agree to 10^(-11) for beta_M <= 4, 2 x 10^(-7) at 6, 3 x 10^(-5) at 8 (Wilson differences), so the beta_M = 8 row is good to about four digits only. On the face the first excited level is double here, so n_1(0) is the value in the eigenvector the solver returned; the sign statement for t > 0 does not depend on it.

**Reading.** No dip for SU(2) on either box, in either form, at three (A: two for beta_M > 4) truncations. In all runs n_1 - n_0 stays above 0.97, while n_0 grows about linearly in beta_M. The excess does not shrink as the vacuum fills with flux. This is unlike Q_8 (Example KIN-7), where the dip appears once the vacuum is close to a point mass. The kill tests do not end the row. They prove nothing.

Later run, larger truncation (test A, `log_n3_22.txt`, 2Jmax = 22, dimension 3246): beta_M = 8 gives m(infinity) = 1.8788395546 and least n_1 - n_0 = 1.2679, the same as at 18; beta_M = 12 gives m(infinity) = 1.8948680320, least Wilson difference +2.13e-2, least n_1 - n_0 = 1.2684, n_0(0) = 10.57, n_1(0) = 21.28 (one truncation only for beta_M = 12).

**The kill tests do not depend on Lemma KIN (hand remark).** The same matrices come from the spin-network basis of the unreduced slice. One sheet, n = 3: the slice graph is two plaquettes that share the link Phi_2. A gauge-invariant function is a spin network with spin j_A on (a(1,x), Phi_1, a(1,y)), j_B on Phi_2, j_C on (a(2,x), Phi_3, a(2,y)), and a triangle at the two trivalent sites. Convolution by a class function w on one link multiplies a spin network by lambda_j of that link. So K_a K_Phi = lambda_{j_A}(beta_L)^2 lambda_{j_C}(beta_L)^2 lambda_{j_A} lambda_{j_B} lambda_{j_C}(beta_M) with no reduction, and V is the multiplication by the two plaquette characters. This is the operator of step 1 with (j_1, j_2, j_3) = (j_A, j_B, j_C). Two sheets, n = 2: two plaquettes that share the link a(1, y); K_a = lambda_{j_A} lambda_{j_B} lambda_{j_C}(beta_L), K_Phi = lambda_{j_A}^2 lambda_{j_C}^2 (beta_M). Again the operator of step 1. So on these two boxes the direct computation and Lemma KIN (c) agree. This is a hand consistency check of Lemma KIN (c) on two boxes. It is not a check of its proof.

### Step 5 (n = 2 by hand). DONE: structure PROVED; the sign PROVED for beta_M <= 3/2 and under a single-crossing condition; the full sign OPEN.

**5.1 The operator.** Write a class function as f = u(theta)/sin(theta), chi_j = sin(n theta)/sin(theta), n = 2j+1 >= 1. In the orthonormal basis e_n = chi_j of K = l^2({1, 2, ...}):
- multiplication by cos(theta) is J, J e_n = (e_{n+1} + e_{n-1})/2, e_0 = 0; so E^2 = e^(beta J), beta = beta_M, with entries k_beta(n, m) = I_{n-m}(beta) - I_{n+m}(beta) (images of e^(beta cos) = I_0 + 2 sum I_k cos(k theta));
- K_Phi = diag(a_n^2), a_n = I_n(beta)/I_1(beta);
- N = 2 C = diag(c_n), c_n = (n^2 - 1)/2; D = e^(-tN) or diag(g_n^2), g_n = I_n(beta_L)/I_1(beta_L).
The operator with the spectrum of R T R^(-1) is B_t = e^(-tN/2) A e^(-tN/2), A(n, m) = a_n a_m k_beta(n, m). (Lemma KIN (c); for n = 2 it is also the standard one-plaquette computation, see the remark above.)

**Lemma TP-2 (PROVED, with two recalled theorems).** For n = 2, every beta > 0 and every t >= 0 (and every Wilson D): (i) all entries and all 2 x 2 minors of B_t are strictly positive; (ii) lambda_0 > lambda_1 > lambda_2; (iii) with phi_0 > 0 the top eigenvector, r = phi_1/phi_0 is strictly monotone in n. I fix the sign r(1) > 0, so r is strictly decreasing.
Proof. (i) B = d_n d_m k_beta(n, m) with d > 0, so it is enough to treat k_beta = e^(beta J). J is the generator part of a nearest-neighbour walk on {1, 2, ...} killed at 0. By Karlin and McGregor (1959, coincidence probabilities) the determinant det[k_beta(n_i, m_j)], n_1 < n_2, m_1 < m_2, is e^(2 beta) times the probability that two independent rate-one walks (generator J - 1) from n_1, n_2 reach m_1, m_2 without meeting; nearest-neighbour steps force the ordered pairing. It is positive. A direct form for Lean: I + eps J has non-negative 2 x 2 minors for eps <= 1; Cauchy-Binet keeps this under products; e^(beta J) is the limit of (I + beta J/k)^k; strictness from one explicit non-crossing pair of paths. (ii) and (iii): B_t is compact and positive. Its second exterior power, on the pairs n_1 < n_2, has strictly positive entries (the minors). By Jentzsch's theorem its top eigenvalue is simple with a strictly positive eigenvector. The top eigenvalue is lambda_0 lambda_1 with eigenvector phi_0 ^ phi_1; if lambda_1 = lambda_2 it would be double. So lambda_1 > lambda_2, and phi_0(i) phi_1(j) - phi_0(j) phi_1(i) has one strict sign for all i < j: r is strictly monotone. lambda_0 > lambda_1 by Perron-Frobenius. QED
Consequence. At n = 2 the simplicity hypothesis of Identity KIN-5 holds for all t >= 0. So m is differentiable in t and m'(t) = n_1(t) - n_0(t) on the whole half-line. This is the Gantmacher-Krein oscillation structure; I use only its order-2 part.

**Reduction (PROVED).** With p = phi_0^2 (a probability on {1, 2, ...}), E_p r = 0, E_p r^2 = 1:
  n_1 - n_0 = E_p[(r^2 - 1) c] = Cov_p(r^2, c).
(FLUX-EXC) at n = 2 is the statement Cov_p(r^2, c) >= 0 for all beta, t.

**Lemma SC (single crossing; PROVED).** If r(1) <= 1, then n_1 >= n_0, and the same holds with c replaced by any non-decreasing sequence.
Proof. r decreases strictly from r(1) in (0, 1] and E_p r = 0, E_p r^2 = 1, so r goes below -1. Let n' be the last n with r(n) >= -1. Then r^2 - 1 <= 0 for n <= n' and > 0 for n > n'. So (r^2 - 1)(c_n - c_n') >= 0 for every n, and E_p[(r^2 - 1) c] >= c_n' E_p[r^2 - 1] = 0. QED
r(1) <= 1 says: the excited state has no more weight on the trivial character than the vacuum has. GUIDE (`runs/gap-descent-sign/n2_reduction.py`, 60 characters): r(1) <= 1 at all t for beta_M <= 6; r(1) > 1 at small t for beta_M >= 8 (1.052 at beta_M = 8, t = 0; 1.141 at beta_M = 16, t = 0). So Lemma SC does not cover large beta_M, and I have no proof of r(1) <= 1 where the run shows it.

**Proposition DIL (dilute vacuum; PROVED; any compact group, any box).** Let psi be the unit top eigenvector of S S*, and let delta_2 be the product of the two largest eigenvalues of D on K, with multiplicity. Then
  m(beta_L) - m(infinity) >= 2 log <psi, D psi> - log delta_2.
Heat-kernel form: let nu_1 be the second smallest eigenvalue of N on K with multiplicity (the smallest is 0, on the constants). Then for 0 <= s <= t
  m(t) - m(s) >= (t - s)(nu_1 - 2 n_0(s)) >= (t - s)(nu_1 - 2 n_0(0)),
and where lambda_1 is simple, n_1(t) - n_0(t) >= nu_1 - 2 n_0(t).
Proof. lambda_0 lambda_1 is the norm of the second exterior power of S* D S, which has the spectrum of Lambda^2(D^(1/2)) Lambda^2(S S*) Lambda^2(D^(1/2)); so lambda_0 lambda_1 (beta_L) <= delta_2 lambda_0 lambda_1 (infinity). By Rayleigh with the face vacuum Omega: lambda_0(beta_L) >= <Omega, S* D S Omega> = lambda_0(infinity) <psi, D psi>, psi = S Omega/norm. m = 2 log lambda_0 - log(lambda_0 lambda_1). Heat kernel: <psi, e^(-tN) psi> >= e^(-t <psi, N psi>) by Jensen, <psi, N psi> = n_0(0), delta_2 = e^(-t nu_1); start at s by replacing S with e^(-sN/2) S; n_0 is non-increasing by Lemma KIN-CVX. The pointwise form: n_0 + n_1 is the trace of N on a two-dimensional space, at least 0 + nu_1 (Ky Fan). QED
One-sheet boxes, every n: nu_1 = 3/2. (A non-constant singlet has a cut with left spin L_k not 0; then the right spin R_k has the same parity class; both at least 1/2 gives 2 x 3/4; an integer pair gives at least 2 x 2 > 3/2. The value 3/2 is taken at chi_(1/2)(Phi_2 Phi_1^(-1)).) So:
  **on a one-sheet box, if n_0(0) <= 3/4, then m(t) is non-decreasing on [0, infinity).**
This is Corollary KIN-2 of row 1076 with its bracket bounded. It carries the same volume factor: n_0(0) grows with the box and with beta_M. GUIDE values of n_0(0): n = 2 crosses 3/4 near beta_M = 3.3; n = 3 near beta_M = 2.2.

**Corollary N2-SMALL (PROVED by hand).** For n = 2, heat-kernel form, beta_M <= 3/2: n_1(t) >= n_0(t) for all t >= 0, so m(t) is non-decreasing.
Proof. phi_0 = lambda_0^(-1) K^(1/2) E^2 K^(1/2) phi_0 at t = 0, so N^(1/2) phi_0 = lambda_0^(-1) (N^(1/2) K^(1/2)) E (E K^(1/2) phi_0). Here norm(E K^(1/2) phi_0)^2 = lambda_0, norm(E)^2 = e^(beta), norm(N^(1/2) K^(1/2))^2 = sup_n c_n a_n^2. So n_0(0) <= e^(beta) sup_n (c_n a_n^2)/lambda_0. From the power series, I_n(beta) <= (beta/2n) I_{n-1}(beta), so a_n <= prod_{k=2..n} beta/(2k). c_2 a_2^2 <= 3 beta^2/32, and c_{n+1} a_{n+1}^2 / (c_n a_n^2) <= ((n+2)/(n-1)) (beta/(2n+2))^2 < 1 for n >= 2, beta <= 3/2. lambda_0 >= A(1, 1) = I_0 - I_2 = 2 I_1(beta)/beta >= 1 + beta^2/8. At beta = 3/2: n_0(0) <= (3 x 2.25/32) x 4.4817/1.28125 = 0.738 <= 3/4; the bound increases in beta. Proposition DIL with Lemma TP-2 gives n_1 - n_0 >= 3/2 - 2 n_0(t) >= 0. QED
The bound is crude: the run gives n_0(0) = 0.022 at beta_M = 1 against the bound 0.69.

**Remark CUM (ARGUED; GUIDE).** Fix t > 0 and let beta tend to infinity. With I_nu(beta) = e^(beta) (2 pi beta)^(-1/2) e^(-nu^2/(2 beta)) (1 + o(1)): A(n, m) is proportional to e^(-(n^2+m^2)/beta) 2 sinh(nm/beta) = (2nm/beta)(1 + n^2 m^2/(6 beta^2) + ...). The leading term has rank one. So phi_0 is close to n e^(-t c_n/2) normalised, phi_1 is close to the part of n^3 e^(-t c_n/2) orthogonal to it, r is close to a linear function of c, and for a linear r the reduction gives exactly n_1 - n_0 = kappa_3(c)/kappa_2(c), the third over the second cumulant of N in the vacuum. So in this corner (FLUX-EXC) says: the flux distribution of the vacuum is skewed to the right. The run shows kappa_3/kappa_2 within 25 per cent of n_1 - n_0 at all 45 points of the grid (beta_M from 0.5 to 16, t from 0 to 1.5), and above it at every point. For frozen Q_8 near the point mass the vacuum weights are 1/8, 3/8, 4/8 on rising electric cost: skewed to the left. That is Example KIN-7 in this language. Not a proof: r is not linear, and the error terms are not controlled.

**The named step that failed: (S) Cov_p(r^2, c) >= 0 at n = 2 for beta_M > 3/2 and all t.** Three written ways.
- Way 1, Proposition DIL. It needs n_0 <= 3/4. The run gives n_0(0) > 3/4 for beta_M above about 3.3, and 3/2 - 2 n_0 is negative there while n_1 - n_0 is 1.2 or more. The method bounds lambda_0 lambda_1 by an operator norm and loses the volume factor. FAILS beyond the dilute range (scope: this bound; proved range beta_M <= 3/2).
- Way 2, total positivity and a single crossing (Lemma SC). It needs r(1) <= 1. The run gives r(1) > 1 for beta_M >= 8 at small t; there r^2 - 1 has the pattern (+, -, +). Also I did not prove r(1) <= 1 anywhere outside the range of Way 1. FAILS at large beta_M (GUIDE), OPEN in between.
- Way 3, two crossings (the Karlin-Novikoff argument). For the pattern (+, -, +), E_p[(r^2 - 1) c] >= gamma E_p[(r^2 - 1) xi] for any increasing xi in which c is convex, gamma >= 0 (interpolate c by a linear function of xi at the two crossings). So one ordered moment <xi>_1 >= <xi>_0 would do. I tried: xi = c (circular); xi = -kappa_n, where the eigen-equations give sum_n kappa_n phi_i(n)^2 = lambda_i int e^(-beta cos) Omega_i^2 (Omega_i the eigenfunction of E K E), which has no sign because lambda_0 > lambda_1 while the integral is larger in the excited state; xi from a virial identity with the field sin(theta) d/d theta, which gives int cos(theta) u'^2 and not int u'^2. None gives a sign. FAILS as tried.
Also tried and not counted: Collatz-Wielandt bounds for lambda_0 and for the compound operator with the face eigenvectors as test vectors (the lower bound for lambda_0 is zero on an infinite basis; with Rayleigh instead it is Proposition DIL again); convexity (KIN-CVX gives no sign for a difference).

### Step 6 (the structure for n >= 3). DONE: what survives is PROVED; no mechanism for the sign; OPEN.

**What survives (PROVED, with the recalled tensor-operator formula of step 1).**
- N is diagonal in the sequential spin-network basis for every n (step 1). For n = 3, N = 2 j_1(j_1+1) + 2 j_3(j_3+1).
- The face part has non-negative entries: e^(beta x) = sum_J c_J(beta) chi_J with c_J = 2(2J+1) I_{2J+1}(beta)/beta > 0, and multiplication by chi_J has the entries sqrt(d d d d){6j}^2 >= 0. K_Phi and D are positive and diagonal. So B_t has non-negative entries, and the vacuum has non-negative spin-network coefficients for every t.
- Proposition DIL holds for every n with nu_1 = 3/2: if n_0(0) <= 3/4 then m is non-decreasing in t. GUIDE: at n = 3 this covers beta_M up to about 2.2.

**What does not survive.**
- The linear order. At n = 2 the basis is {1, 2, ...} and B_t is totally positive of order 2 (Lemma TP-2). At n = 3 the basis is the set of triangles (j_1, j_2, j_3), and N depends on (j_1, j_3) only. I found no order in which the 2 x 2 minors keep a sign, and I did not prove that none exists.
- Simplicity of lambda_1. On the two-sheet face the first excited level is double (the sheets decouple at beta_L = infinity; kill test B, check (iv)). So the derivative form dm/dt = n_1 - n_0 of Identity KIN-5 is not available at t = 0 there. The endpoint form and Proposition DIL do not need it.
- The reduction to one covariance. Without a monotone ratio phi_1/phi_0 there is no single-crossing lemma.

**What the sign looks like in the runs (GUIDE).** At n = 3 and for two sheets, n_1 - n_0 stays between 0.97 and 1.5 at its least point in t, for beta_M from 0.5 to 12, while n_0(0) grows from 0.003 to 10.6. Remark CUM gives the reading at n = 2: the excess is the skewness of the vacuum's flux distribution. An argument for n >= 3 would need a property of the vacuum that says "the flux on the cuts is skewed to the right" and that a point mass violates. I have no such statement in a provable form. OPEN.

**Tests on what is proved here.**
- Example KIN-6: Proposition DIL is consistent with it. There psi = e_a, <psi, D psi>^2 = e^(-2ta), delta_2 = e^(-t(a+c)), and the bound reads m(t) - m(0) >= -t(a - c), which is the true value. The hypothesis n_0 <= nu_1/2 fails there (a > (a + c)/2). Lemma SC needs the vacuum to sit low in the order of N; in KIN-6 it sits at the top.
- Frozen Q_8 (Example KIN-7): Proposition DIL holds for Q_8 in its Wilson form and does not give (MON-L) there. In the limit of KIN-7: delta_2 = B_L = 1 - 12 eta, <psi, D psi> = 1/8 + (3/8) A_L + (1/2) B_L = 1 - 12 eta, so the bound is m(beta_L) - m(infinity) >= -12 eta + O(eta^2); the true value is -8 eta. So the proposition is consistent with the dip, and its hypothesis fails where the dip is. Nothing in this file proves (MON-L) for a class that contains Q_8 or 2T at large beta_M.
- Compact U(1): Proposition DIL holds for it in the same dilute range. Allowed by the brief.
- What uses the continuous group: only the range statements. The value nu_1 = 3/2 and the bound on n_0(0) use SU(2) characters; the proved range beta_M <= 3/2 is a strong-coupling range, where Q_8 has no dip either (row 1076: dip only above about 2.2). So the proved part does not yet separate SU(2) from Q_8. The separation is in the open part.

### Step 7 (several sheets). DONE as far as the stop rule allows: one kill test run (step 4), one new test named; no proof.

- Two sheets on a transverse path, n = 2: kill test B, no dip (step 4). Proposition DIL applies with nu_1 = 3/2 (N = j_1(j_1+1) + j_2(j_2+1) + j_3(j_3+1), least non-zero value at (1/2, 1/2, 0)).
- Any transverse tree: the kernel of N on K is the constants, so nu_1 > 0 and Proposition DIL gives a dilute range.
- **A transverse lattice with a plaquette is different (PROVED observation; the sign ARGUED in one corner).** A class function of a transverse plaquette of one layer is fixed by every rho_c(W) (a rotation at one corner). So N = 0 on all functions of the layers' transverse plaquettes: the kernel of N is infinite-dimensional, nu_1 = 0, and Proposition DIL gives nothing. For large t the first excited state lies in that kernel, and by second-order perturbation in eps = e^(-3t/4) (P_0 on the kernel of N, P_1 on the level N = 3/2, M = S S*):
    log lambda_i(t) = log lambda_i(infinity) + e^(-3t/2) l_i + ..., l_i = norm(P_1 M phi_i)^2 / lambda_i(infinity)^2, n_i(t) = (3/2) e^(-3t/2) l_i + ...
  So at large t the sign of n_1 - n_0 is the sign of l_1 - l_0: the charged leakage of the excited state against that of the vacuum, each relative to its own eigenvalue. Hand estimate for one transverse plaquette, n = 2, beta_T = 0, small beta_M (leading order): l_0 is about beta_M^4/16 and l_1 about beta_M^2/4, so l_1 > l_0 there (ARGUED). For beta_M of order one the sign of l_1 - l_0 is not computed. **This is the cheapest kill test for several sheets, and it was not run here**: the box with one transverse plaquette and n = 2 (eight Phi links), sign of l_1 - l_0 or of m(t) - m(0) at large t. On one-sheet boxes this question does not arise (the kernel of N is the constants).
- No proof for several sheets. The brief puts several sheets after a mechanism for n >= 3, and there is none.

### Step 8 (marks, scope, credits, RESULT). DONE.

**Marks.**
- Kill test A (SU(2), one sheet, n = 3) and kill test B (two sheets, n = 2): no dip in Wilson or heat-kernel form; beta_M in [0.5, 8] at truncations 2Jmax = 14 and 18 (and 10 for beta_M <= 4), beta_M = 8 also at 22, beta_M = 12 at 22 only (test A). GUIDE. Not a proof.
- Spin-network form of both boxes (N diagonal; face part with non-negative entries; the two boxes share X12, X23): PROVED with the recalled tensor-operator formula; the formula was checked by two hand cases and by the commutator [X12, X23] = 0 to 10^(-14) (GUIDE).
- Lemma TP-2 (n = 2: strict positivity of 2 x 2 minors, lambda_0 > lambda_1 > lambda_2, monotone ratio): PROVED with the recalled theorems of Karlin-McGregor and Jentzsch.
- Reduction n_1 - n_0 = Cov_p(r^2, c) at n = 2: PROVED.
- Lemma SC (single crossing): PROVED. Its hypothesis r(1) <= 1: not proved anywhere; GUIDE says true for beta_M <= 6 and false for beta_M >= 8 at small t.
- Proposition DIL (any compact group, any box): PROVED. One-sheet corollary (n_0(0) <= 3/4 gives m non-decreasing in t): PROVED.
- Corollary N2-SMALL (n = 2, heat kernel, beta_M <= 3/2: n_1 >= n_0 for all t): PROVED by hand.
- Remark CUM (third cumulant reading at large beta_M, fixed t): ARGUED.
- (FLUX-EXC) for SU(2), n = 2, beta_M > 3/2: OPEN. Step (S) failed in three written ways (step 5).
- (FLUX-EXC) for SU(2), one sheet, n >= 3, outside the dilute range: OPEN. No mechanism.
- Several sheets: OPEN. Large-t criterion l_1 >= l_0 for boxes with a transverse plaquette: stated; ARGUED at small beta_M; not tested numerically.
- The Wilson endpoint form m(beta_L) >= m(infinity) is proved here only through Proposition DIL's general inequality; no explicit Wilson range was worked out.

**Scope of the negatives.** "FAILS" in step 5 is about three named methods as I applied them at n = 2. It is not a statement that (FLUX-EXC) is false or unprovable. No counterexample for SU(2) was found on the two boxes and grids of steps 3 and 4. Nothing was computed for n >= 4, for two sheets with n = 3, for a box with a transverse plaquette, or in infinite volume. The volume-free form asked for by BR-2 is not touched: Proposition DIL has a threshold that shrinks with the box.

**Not checked.** One session, one author (Claude Fable 5.2 medium), no second reader. Lemma KIN of row 1076 is used as stated; its check (row 1079) had not returned. The kill tests agree with a direct spin-network computation that does not use Lemma KIN (remark after step 4). No numeric lock existed in this checkout (`scripts/lab_ops.py` absent); runs were serial, one BLAS thread, largest matrix 3246 x 3246.

**Credits.** Lemma KIN, Identity KIN-5, Lemma KIN-CVX, Corollary KIN-2, Examples KIN-6 and KIN-7 and brief P2: row 1076 (`library/gap-bridge-vectors-max.md`, Claude Fable 5.2 max). Coincidence probabilities and determinants of transition functions: S. Karlin and J. McGregor (1959). Oscillation matrices and kernels: F. Gantmacher and M. Krein. Positive kernels: R. Jentzsch; O. Perron and G. Frobenius. Two-crossing convex inequalities: S. Karlin and A. Novikoff (1963). Sums of lowest eigenvalues: Ky Fan. 6j symbols and the scalar-product formula: G. Racah; E. Wigner; A. R. Edmonds' text. The lattice Hamiltonian picture with electric Casimirs on links and the one-plaquette problem: J. Kogut and L. Susskind. Bessel-ratio bounds from the power series: classical (D. Amos has sharper ones). The lane builds on T. Balaban and on the account of Sussman and Alpoge; no step of theirs is used in this row.

**Files.** `runs/gap-descent-sign/su2box.py`, `n2_reduction.py`, logs `log_*.txt`, data `out_*.json` (all small).

RESULT: Row 1081 (Claude Fable 5.2 medium, laptop subagent; one session, checked by no one). No counterexample: the kill tests for SU(2) (one sheet n = 3; two sheets n = 2; beta_M 0.5 to 8 at two or three truncations, 12 at one) show m(beta_L) - m(infinity) > 0 and n_1 - n_0 >= 0.97 everywhere (GUIDE). PROVED: the spin-network form with N diagonal and a non-negative face part; Lemma TP-2 (n = 2: total positivity of order 2, simple lambda_1, monotone phi_1/phi_0); Lemma SC (single crossing gives the sign when r(1) <= 1); Proposition DIL (any group, any box: m(t) - m(s) >= (t - s)(nu_1 - 2 n_0(s)); on one-sheet boxes n_0(0) <= 3/4 gives a non-decreasing gap); Corollary N2-SMALL ((FLUX-EXC) at n = 2 for beta_M <= 3/2). ARGUED: at large beta_M the excess is the third over the second cumulant of the vacuum's flux (right skew; Q_8's point mass is left-skewed). OPEN: (FLUX-EXC) for SU(2) at n = 2 with beta_M > 3/2 (step (S), Cov_p(r^2, c) >= 0, failed in three written ways: dilute bound, single crossing, two-crossing moment), at n >= 3 outside the dilute range, and for several sheets; new untested kill test named for boxes with a transverse plaquette (sign of l_1 - l_0 at large t). Output `library/gap-descent-sign.md`.
