lead: anthropic/claude-opus-5-5/high mac-mini-worker
lease_until: 2026-11-12T00:19Z

# Check of `library/gap-vir-sc.md` (row 715)

Provenance: written by Claude Opus 5.5, effort high, Mac mini worker 2, at commit 2a7b3fde7. One reading by one model. Not an audit. The checked file was written by Claude Fable 5.2 medium (row 710). Both are Claude models, so this is not a check by the other provider.

## Status block

Started 2026-11-11T12:19Z. Complete. No statement fails; Theorem B1 holds after two corrections of its input marks; see the summary table in Section 12 and the final status block.

Read whole: `gap-vir-sc.md` (232 lines); `gap-transfer.md` lead note (row 671), Notation, Sections A and 1 to 4; `gap-mid-max.md` lead note (row 709) and Sections 4.1 to 4.5; `gap-seed-sc.md` Theorem 4 (statement and proof). Not read: the inputs of Theorem 4 (Theorems S, D, 3, Corollary S3'); they are checked rows (698, 699, 704) and are taken as given. Sussman-Alpoge account: not opened; their GL3 (link weights in Bessel form) enters only through `gap-transfer.md` Remark 2.6, and Lemma J (d) agrees with it.

Repo search: `grep -rln gap-vir-sc` in this folder hits FINISH.md (rows 710, 715), the source file, `gap-mid-max.md` line 365 (the proposal of the item) and `gap-skeleton-final.md` line 522 (a summary that says "not checked, check = row 715"). No earlier check of `gap-vir-sc.md` exists. This is a check of our own new text, so rule 0a (duplicate attack) does not apply; no open lemma is attacked here.

## 1. Lemma J (link weights)

Verdict: **(a) to (f) HOLD.**

- (a) The expansion of cos^m x and the three values of (1/pi) integral of cos(kx) cos(nx) give the coefficient 2^(-m) binom(m, (m-n)/2)/m! for n >= 1 (two terms m - 2i = +-n, each with weight 1/2) and for n = 0 (one term, weight 1). With m = n + 2k this is 2^(-m)/(k! (n+k)!). Sum and integral exchange by uniform convergence. Checked.
- (b) Both identities re-derived term by term. In the first, the k-th coefficient of J_(n-1) is (n+k)/(k! (n+k)!) and of the shifted J_(n+1) is k/(k! (n+k)!); the difference gives n, hence (2n/s) J_n. In the second, s J_(n+1) shifted by k -> k-1 is exactly 2 sum over k >= 1 of (s/2)^(n+2k)/((k-1)! (n+k)!). Checked.
- (c) Term ratio (s/2)/(n+1+k) <= s/(2(n+1)). Checked.
- (d) Weyl's formula for a class function on SU(2), (2/pi) integral over [0, pi] of f(x) sin^2 x dx, is correct (the polar angle of S^3; integral of sin^2 over [0, pi] is pi/2). sin((2j+1)x) sin x = (cos 2jx - cos(2j+2)x)/2. Then (b) with n = 2j+1 >= 1 gives c_j = (2 e^(-s)/s) J_(2j+1). Agrees with `gap-transfer.md` 2.6 (their GL3). The scalar of Lemma C is the same c_j, because chi_j(w^(-1)) = chi_j(w) is real. Checked.
- (e) eta_j = s + log(s/2) - log J_(2j+1) is correct. With s J_n'/J_n = n + s r_n from (b): -s eta_j' = -s - 1 + (2j+1) + s r_(2j+1). For s <= 4, 0 < r_(2j+1) <= s/(2(2j+2)) <= s/4 <= 1, so 0 <= 1 - r < 1 and 2j - s <= -s eta_j' <= 2j. Checked.
- (f) (2/s) J_(2j+1) = sum over k of (s/2)^(2j+2k)/(k! (2j+1+k)!); (2j+1+k)! >= (2j+1)! k!; sum of squares at most square of sum gives at most e^s; (n+1)! >= 2^n for n = 2j >= 0 (induction). So c_j <= (s/2)^(2j)/(2j+1)! <= (s/4)^(2j). The bound eta_j >= 2j log(4/s) holds for every s > 0 (it is vacuous in sign when s >= 4). Checked.

**Independent hand test at j = 1/2, s = 1 (row 715 asks for it).** Different derivation: under Haar measure, t = cos x = (1/2) tr g has the semicircle density (2/pi) sqrt(1 - t^2) on [-1, 1], with even moments E t^(2k) = Cat_k/4^k (Catalan numbers). Since chi_(1/2) = 2t, c_(1/2)(s) = (1/2) e^(-s) E[e^(st) 2t] = e^(-s) sum over odd m of (s^m/m!) Cat_((m+1)/2)/4^((m+1)/2). With m = 2k+1 and Cat_(k+1) = (2k+2)!/((k+1)! (k+2)!), the m-th term is 2 s^(2k+1)/(4^(k+1) k! (k+2)!). The k-th term of (2/s) J_2(s) is 2 s^(2k+1)/(2^(2k+2) k! (k+2)!). They are equal term by term, so (d) holds at j = 1/2 for all s as an identity of series. Numbers at s = 1 (five terms, the tail is below 10^(-8)): moment series 1/4 + 1/48 + 1/1536 + 1/92160 + 1/8847360 = 0.2714953; times e^(-1) = 0.3678794 gives c_(1/2)(1) = 0.0998775. Bessel side: J_2(1) = 1/8 + 1/96 + 1/3072 + 1/184320 + ... = 0.1357477; times 2 e^(-1) gives 0.0998775. Equal. (f) at j = 1/2, s = 1: 0.0999 <= (1/4)^1 = 0.25, and the intermediate bound (s/2)^(2j)/(2j+1)! = 1/4 as well. Holds with room. (e) at the same point: J_3(1) = 1/48 + 1/768 + 1/30720 + ... = 0.0221684, r_2(1) = 0.163307, -s eta' = 1 - 1 + r_2 = 0.163307, inside [2j - s, 2j] = [0, 1]. Hand arithmetic, displayed above; it is a check, not an input of any proof.

## 2. Lemma C (the kinetic operator is diagonal in the link representations)

Verdict: **HOLDS.** The input list should read "Schur's lemma, irreducibility of D^j, and Schur orthogonality (RECALLED)", not Schur orthogonality alone. No step changes.

- One link. With w = u v^(-1) (Haar invariance), (C f)(u) = sum over e of A_(ae) D^j_(eb)(u) for f = D^j_(ab), A = integral of c(w) D^j(w^(-1)) dw. A commutes with every D^j(g) because c is a class function (substitute w -> g w g^(-1)). So A is scalar by Schur's lemma. This needs D^j irreducible, which `gap-transfer.md` 2.5 does not prove; it is a standard fact and is RECALLED here as part of "Schur". The scalar is tr A/(2j+1) = c_j (chi_j real). For dc_s/ds = -(1 - (1/2) tr g) c_s, also a class function, the scalar is c_j' (smooth integrand on a compact group). Checked.
- Several links. The kernel is a product, so C_s is c_n on H_n; the kernel of C_s' is a sum over l with one factor differentiated, so C_s' is c_n' = sum over l of c_(j_l)' times the product of the other c_(j_l'). Checked.
- Orthogonality of H_n and H_n' for n != n': some link has j_l != j_l', and H_j is orthogonal to H_j' (Schur orthogonality; D^j and D^j' are inequivalent because their dimensions differ). Checked.
- **The trace argument (most care).** C_s Pi_n = c_n Pi_n, and taking adjoints Pi_n C_s = c_n Pi_n; so C_s commutes with each Pi_n and maps Y (the complement of the closed span of all H_n) into Y. Take an orthonormal basis of H made of bases of the H_n and of Y. By Definition A1 of `gap-transfer.md` the trace of the positive trace-class operator C_s does not depend on the basis, and Tr C_s = 1 (Statement 3, 3.2). The H_n part gives sum over n of c_n dim H_n = product over links of sum over j of (2j+1)^2 c_j (non-negative terms, Tonelli). By (2d) of `gap-transfer.md` and orthonormality of characters, e^(-s) a_j = integral of c_s chi_j = (2j+1) c_j, so sum over j of (2j+1) c_j chi_j(1) = c_s(1) = 1. So the trace over Y is 0. For a positive operator, <e, C e> = 0 on each basis vector gives C e = 0 (Cauchy-Schwarz for the form, as in A2.1), so C_s = 0 on Y. Peter-Weyl is not used. Checked. (Orthonormality of the characters can also be read off directly from Weyl's formula: (2/pi) integral of sin((2j+1)x) sin((2k+1)x) dx = delta.)
- C_s' on Y. Y does not depend on s. (C_(s+h) - C_s)/h converges to C_s' in Hilbert-Schmidt norm (the kernel difference quotients converge uniformly on the compact X x X), and C_(s+h) y = C_s y = 0 for y in Y. So C_s' y = 0. Checked.
- Quadratic form. For f = sum of Pi_n f + y: cross terms vanish, and sup over n of abs(c_n') <= norm of C_s' (C_s' acts on H_n as c_n'), so sum over n of c_n' norm(Pi_n f)^2 converges absolutely and equals <f, C_s' f>. The file does not write this line; it is immediate. Checked.
- Pi_n commutes with P: the gauge action multiplies each link on both sides by fixed elements, so each R_h is unitary and preserves H_n, hence commutes with Pi_n; P is the Haar average of the R_h. Checked.
- Box with unequal sides: `gap-transfer.md` is written for the cube N^3; the extension to boxes with sides at least 3 is recorded in `gap-crux-restate.md` line 33 (checked in rows 698, 699). Lemma C uses only Statement 3, which needs no equal sides.

## 3. Input (RK) and its three consequences

Verdict: **(RK) is RECALLED and correctly cited; consequences (1), (2), (3) HOLD given (RK).**

- (RK). T(s) = M_s C_s M_s P has a kernel entire in s and bounded on compact sets, so it is a bounded holomorphic family, self-adjoint for real s. Kato VII Section 3 (Rellich's theorem for self-adjoint holomorphic families of type (A); a bounded family is of type (A)) gives r real-analytic eigenvalues and real-analytic orthonormal eigenvectors near an isolated eigenvalue of multiplicity r. A positive eigenvalue of a compact operator is isolated and of finite multiplicity (A2 (ii), (iii)). So the citation fits. It is not rebuilt in `library/`.
- Positive eigenvectors lie in H_inv: T(s) = MCMP = PMCMP (`gap-transfer.md` 1.6), so lambda psi = T psi is in Ran P. T'(s) = P(M'CM + MC'M + MCM')P because P does not depend on s.
- (1) Differentiate <psi, T psi> = lambda: the two terms with psi' give lambda d/ds norm(psi)^2 = 0 (lambda real, T self-adjoint). Checked.
- (2) The ordered positive eigenvalues are continuous: by the min-max formula (A2 (iii)), abs(lambda_i(s) - lambda_i(s')) <= norm(T(s) - T(s')). Near s_0 the eigenvalues near lambda_i(s_0) are the r branches of (RK); two distinct analytic functions meet only at isolated points, so on each one-sided punctured neighbourhood the order is fixed and lambda_i is one branch. Compactness of [s, s'] gives finitely many pieces, as long as lambda_i stays above a positive bound (0 is the only accumulation point). Checked.
- (3) lambda_0 is simple at every s (`gap-transfer.md` 4b), so it is one analytic branch on the whole half-line. Checked.

## 4. Theorem U

Verdict: **(i) to (iv) HOLD.** Two convergence lines are missing; they are supplied below and change nothing. Theorem U holds at every coupling 0 < s < 4 as stated, for every box with sides at least 3.

- (i) lambda = <psi, T psi> = <M psi, C M psi> uses P psi = psi and M real; then Lemma C. w >= 0 because c_n > 0 (Lemma J (d)), and sum of w = 1. Sum of q_n <= norm(M psi)^2 = <psi, exp(-s V_1) psi> <= 1. Checked.
- **(ii), the three terms of T' (most care).** M' = -(V_1/2) M is correct, since V = s V_1 and V_1 does not depend on s. First term: <psi, P M' C M P psi> = <M' psi, C M psi> = -(1/2) <V_1 psi, M C M psi>. Here P psi = psi is used twice: once to drop the outer P, once to write M C M psi = M C M P psi = T psi = lambda psi. Both uses are right because psi is in H_inv. So the first term is -(lambda/2) <psi, V_1 psi>, a real number. The third term <psi, M C M' psi> is the complex conjugate of the first, so the same real number. Together: -lambda <psi, V_1 psi>. Middle term: <M psi, C' M psi> = sum of c_n' q_n by Lemma C. Then s c_n'/c_n = sum over l of s (log c_(j_l))' = sum over l of (-s eta_(j_l)') = N(n) - s R(n) by Lemma J (e). **The sign of the magnetic term is minus, and it is right:** raising s lowers exp(-s V_1/2), so the level falls with the state's own spatial action. Bounds: R sums over all 3 abs(B) links, including those with j_l = 0 (where 1 - r_1 is in [0, 1] for s <= 4), so 0 <= R <= 3 abs(B); 0 <= V_1 <= 6 abs(B). Hence -9 s abs(B) <= s DD <= <N>_w. Checked.
  - Missing line 1 (finiteness of <N>_w): sup over n of abs(c_n') <= norm(C_s') and sum of q_n <= 1, so sum of c_n' q_n converges absolutely; with 0 <= s R <= 3 s abs(B) this gives <N>_w < infinity.
- **(iii), the log-sum step (most care).** For q_n > 0 (equivalently w(n) > 0), lambda = c_n q_n/w(n) gives -log lambda = eta(n) + log(w(n)/q_n) for each such n. Averaging over w is right.
  - Missing line 2 (splitting the average into two sums): w log(w/q) >= w - q (from log x <= x - 1), so the negative parts of D are summable; eta(n) >= 0 for s < 4 (Lemma J (f)). So <eta>_w and D are each in (-infinity, infinity], their sum is the finite number -log lambda, and both are finite.
  - The log-sum inequality for a countable sum follows from the finite one by monotone limits; simpler, the same pointwise bound gives D >= sum of (w - q) = 1 - sum of q >= 0 by (i). Either way D >= 0. Checked.
  - eta(n) = sum of eta_(j_l) >= log(4/s) sum of 2 j_l = log(4/s) N(n), by Lemma J (f). Checked.
- (iv) From (ii), s DD <= <N>_w, and from (iii), <N>_w <= (-log lambda)/log(4/s), using log(4/s) > 0. Checked.
- Branch form. On an analytic branch DD = lambda'/lambda = (log lambda)'. d/ds [Ehat/log(4/s)] = Ehat'/log(4/s) + Ehat/(s log^2(4/s)) >= 0 is the same as -s Ehat' <= Ehat/log(4/s). So Ehat/log(4/s) is non-decreasing on each branch; for an ordered level it extends across the finitely many junctions by continuity (consequence (2)). Checked.
- Where s < 4 is used: only in the bounds 0 <= 1 - r <= 1 (Lemma J (e)), eta >= 0 and log(4/s) > 0. The identity s DD = <N>_w - s <V_1> - s <R>_w and the identity -log lambda = <eta>_w + D hold at every s > 0 (for the second, D >= 0 still holds, and eta >= 0 at every s > 0 because (2j+1)^2 c_j <= sum over k of (2k+1)^2 c_k = 1 by the trace argument of Lemma C; only the bound eta >= log(4/s) N needs s < 4 to be useful). The statement as written is restricted to s < 4 and is correct there.

## 5. Proposition EL (no spatial plaquettes)

Verdict: **HOLDS.**

- With V_1 = 0, T = C_s P, and C_s, P, Pi_n commute (Lemma C), so T is c_n on Pi_n H_inv and 0 on Y. The vacuum label n = 0 (constants, dimension 1) is the unique top: c_j/c_0 = J_(2j+1)/J_1 = r_1 ... r_(2j) < 1 for s <= 2 (Lemma J (c)). Checked.
- -s E' = sum over links of [(2j_l - s(1 - r_(2j_l+1))) - (0 - s(1 - r_1))] = N - s times the sum over links with j_l > 0 of (r_1 - r_(2j_l+1)). This is at most N + s times the sum of r_(2j_l+1) over those links. r_(2j+1) <= s/(2(2j+2)) <= s/6 for j >= 1/2, and there are at most N such links. So -s E' <= N(1 + s^2/6). Checked.
- J_1 >= s/2. (2j+1+k)!/(2j+1)! = (2j+2)...(2j+1+k) >= (k+1)! >= 2^k, so J_(2j+1) <= ((s/2)^(2j+1)/(2j+1)!) e^(s^2/8). Then eta_j - eta_0 >= 2j log(2/s) + log((2j+1)!) - s^2/8, and this is >= 2j(log(4/s) - s^2/8) because log((2j+1)!) >= 2j log 2 and (1 - 2j) s^2/8 <= 0 for j >= 1/2. log(4/s) - s^2/8 is decreasing on (0, 2], with value log 2 - 1/2 > 0.19 at s = 2. Checked.
- From branches to ordered levels: every label gives an explicit level satisfying E(s') >= E(s) exp(-integral of K). Pointwise domination of a countable family (finitely many members below any bound) gives the same domination of its order statistics. So (LEV_K) holds for the ordered levels with no (RK). The file says this in one line; it is right. Checked.
- K(s) s log(1/s) = (1 + s^2/6) log(1/s)/(log(4/s) - s^2/8) tends to 1. Checked. Section 8 item 2 calls the rate "exact" in this model; it is exact only to leading order (K is (1 + s^2/6)/(s (log(4/s) - s^2/8)), not 1/(s log(4/s))). Wording only.

## 6. Corollary U'

Verdict: **HOLDS.** s DD(psi) <= Ehat/log(4/s) = (E + Ehat_0)/log(4/s) by Theorem U (iv); Ehat_0 <= 12 s abs(B) by `gap-transfer.md` (4b) (kappa_- = exp(-12 beta N^3), with N^3 replaced by abs(B) for a box, `gap-crux-restate.md` line 33); -s DD(psi_0) <= 9 s abs(B) by Theorem U (ii). Sum: s(DD(psi) - DD(psi_0)) <= E/log(4/s) + s abs(B)(9 + 12/log(4/s)). The orthogonality psi ⊥ psi_0 is not used in the inequality; it only makes E >= 0 meaningful. Checked.

## 7. Theorem B1 ((LEV_K) with a box term)

Verdict: **HOLDS AFTER CORRECTION.** Two input attributions are wrong or missing; no inequality changes.

- On an analytic branch of an excited eigenvalue: -E' = DD(psi) - DD(psi_0) (E = log lambda_0 - log lambda). By Corollary U', -E' <= E/(s log(4/s)) + abs(B)(9 + 12/log(4/s)). Since lambda_0 is simple at every s, no other branch meets it, so E >= m on every excited branch, and the box term is at most abs(B)(9 + 12/log(4/s)) E/m. So (log E)' >= -K_B. Checked.
- Ordered levels: by (RK) (2), log E_i is continuous and piecewise one branch on [s, s'] while lambda_i stays positive (it then stays above a positive bound by compactness). Integrate across the finitely many pieces. Checked.
- **Correction 1.** "m = E_1 is continuous by (RK) (2) or by Lemma 4.1". Lemma 4.1 of `gap-mid-max.md` gives the continuity of lambda_0 only, not of lambda_1. Corrected text: "m = E_1 is continuous: lambda_0 by Lemma 4.1 (a), and lambda_1 by the min-max formula, abs(lambda_1(s) - lambda_1(s')) <= norm(T(s) - T(s')), or by (RK) (2). m > 0 by `gap-transfer.md` Statement (5)." K_B is then continuous and positive on (0, 4).
- (VIR_K) from (LEV_K). Remark LEV of `gap-mid-max.md` gives G(t exp(I_h); s+h) <= G(t; s), I_h = integral of K over [s, s+h]; the mean value theorem in t, (exp(I_h) - 1)/h -> K(s) (K continuous), and the joint continuity of dG/dt for t >= 4 (Lemma 4.1 (b); t > 3 suffices by the row-709 note) give the upper limit <= -K(s) t (dG/dt)(t; s). Checked.
- **Correction 2.** Remark LEV pairs the i-th ordered level at s with the i-th at s + h, for all i. This needs every eigenvalue of T on H_inv to be positive on [s, s+h], which the proof gets from Peter-Weyl (named in its last parenthesis, RECALLED). The statement's mark omits it. Corrected mark: "PROVED GIVEN Corollary U', (RK), Lemma 4.1 of `gap-mid-max.md`, and, for the (VIR_K) clause, the Peter-Weyl theorem for SU(2) (RECALLED; it makes C_s injective, hence T(s) injective on H_inv)." The injectivity step is: <f, T f> = <M f, C M f> = 0 forces M f in Y = 0, and M is invertible. Without Peter-Weyl the (LEV_K) clause for positive levels stands, and the (VIR_K) clause is not proved as written.

## 8. Theorem B (the target on a restricted range)

Verdict: **HOLDS.** Arithmetic redone by hand:

- `gap-seed-sc.md` Theorem 4 with n = 4: s <= 10^(-6) gives theta = 12800 s <= 0.0128 < 1 and 4 theta^4 <= 1.1 x 10^(-7) <= 0.18; b >= 8 = 2n. So m >= 4 log(1/theta) - (4 log 4 + log 1614)/4.
- log 12800 = 7 log 2 + 2 log 10 = 4.852 + 4.605 = 9.457 < 9.47. 4 log 4 = 5.545 < 5.55. log 1614 = 7.3865 < 7.39 (e^7.39 = 1619.7). (5.55 + 7.39)/4 = 3.235 < 3.24.
- m >= 4(L - 9.47) - 3.24 = 4L - 41.12. L >= 6 log 10 = 13.8155, so 3L >= 41.446 >= 41.12, and m >= L. Checked.
- log(4/s) = L + 1.386 > 15.2, so 9 + 12/log(4/s) < 9.79 < 10, and 1/(s log(4/s)) <= 1/(sL). K_B <= 1/(sL) + 10 b^3/L = (1 + 10 s b^3)/(sL). For s <= 1/(10 b^3) this is at most 2/(sL). Both (LEV_K) and (VIR_K) are monotone in K (exp(-integral of K) decreases; -t dG/dt >= 0). Checked.
- The (VIR_K) clause inherits Correction 2 of Theorem B1 (Peter-Weyl).
- "What Theorem B gives": d/ds log L(s) = -1/(sL), so the integral of 2/(sL) over [beta_0, beta_1] is 2 log(L_0/L_1). Checked. b >= 256 gives 1/(10 b^3) <= 1/(1.678 x 10^8) < 6 x 10^(-9). Checked. This range lies inside `gap-seed-sc.md` (beta < 1/12800) and Theorem DOB (beta < 1/18): nothing new is reached. Agreed.

## 9. Proposition SUF

Verdict: **HOLDS.** The cited bound and the arithmetic were redone.

- Cited bound G(4; B; s) <= (4 abs(B)/100)(12800 s)^16. `gap-sc-box.md` Theorem SC (ii) with k = 4 gives abs(log Z(4) - (1/q) log Z(4q)) <= (abs(B) 4/100)(12800 s)^16 for every q, on free-wall boxes. The periodic form needs (P) of `gap-seed-sc.md` (log Xi bounded by (32/3) abs(beta) N, with N = 6 k abs(B) on the torus, the same M) and Corollary 2.3 there (order of vanishing 4k when every spatial side is at least 4, c_B = 4). (1/q) log Z(4q) -> 4 log lambda_0 as q -> infinity (Lemma A), and the bound is uniform in q. So the bound holds for the periodic box with sides at least 4 and real 0 < s < 1/12800. I read Theorem SC and the statements of (P) and Corollary 2.3, not their proofs (checked rows 694, 704).
- G(t; .) is real-analytic for integer t >= 2 (Tr T^t analytic; lambda_0 a simple analytic branch). d/ds Tr T^t = t Tr(T^(t-1) T'). Evaluated in any orthonormal eigenbasis of T on H_inv, this is t times the sum of lambda_i^t DD(psi_i); zero eigenvalues drop out because t - 1 >= 1. **This step uses no branches**: it holds for any choice of eigenbasis in a degenerate eigenspace. (H2) and Corollary U' are stated for every unit eigenvector, so they apply to that basis. Good design; checked.
- D_s G = (t/(1+S)) sum over i >= 1 of (DD_i - DD_0) rho_i^t and -t dG/dt = (t/(1+S)) sum over i >= 1 of E_i rho_i^t. Checked. (VIR_K) at integer t is the sum over i >= 1 of d_i rho_i^t <= 0 with d_i = s(DD_i - DD_0) - (C_1 + 1) E_i/L. Checked.
- Levels with E_i < 5L: d_i <= C_1 - (C_1 + 1) m/L <= -1 (m >= L, Theorem B). By (H1), m <= 4.5 L < 5L, so i = 1 is one of them; their part is at most -rho_1^t = -exp(-tm) <= -s^(4.5 t). Checked.
- Levels with E_i >= 5L: d_i <= E_i/L + 10 s b^3 - (C_1 + 1) E_i/L <= 10 s b^3. rho_i^t <= exp(-5L(t-4)) rho_i^4, so their sum of rho_i^t is at most s^(5t-20) S(4). (T') gives G(4) <= 1, and e^x - 1 <= 2x on [0, 1] (convexity, endpoint values 0 and e - 3 < 0), so S(4) <= 0.08 b^3 12800^16 s^16. Their part is at most 10 s b^3 x s^(5t-20) x 0.08 b^3 12800^16 s^16 = 0.8 b^6 12800^16 s^(5t-3). Checked.
- Total at most s^(4.5t)(-1 + 0.8 b^6 12800^16 s^(t/2 - 3)) <= 0 by (T). Checked.
- Example (s <= e^(-200), 256 <= b <= e^1000, integer t >= ceil(log_2 b)): t >= 8 so t/2 - 3 > 0, and a larger L only helps. 16 log 12800 = 151.32 < 151.4. t/2 >= log b/(2 log 2) = 0.72135 log b. 200(0.7213 log b - 3) >= 151.4 + 6 log b iff 138.27 log b >= 751.4 iff log b >= 5.435; log 256 = 5.545. Checked. (T'): the exact condition is 3 log b <= 16L - 16 log 12800 + log 25, that is 3 log b <= 3200 - 151.32 + 3.22; the file writes "- 3.3" in place of "+ 3.22". That is a stricter condition, still sufficient, and 3000 <= 3045.3. A sign slip with no effect.
- What SUF does not cover (the file says so): non-integer times, and the hypotheses (H1), (H2), which are (BAND-sc), open.

## 10. Labels outside the numbered statements

- **Section 8 (direction).** The section heading says "Direction, not proof", and its first line says nothing in it is proved beyond the two formulas of Theorem U. That one line covers every sentence of the section; the sentences carry no separate marks. Each identity it quotes is proved elsewhere in the file: item 1's formula for s D_s G at integer t is the computation in the proof of Proposition SUF, and E = Delta eta + Delta D follows from Theorem U (iii). Item 3 ("E + s dE/ds = Delta D + s Delta V_1 + (small)") is heuristic. Its sign and the reading K s - 1 = -(Delta D + s Delta V_1)/E were re-derived from the large-s form of the Bessel ratio, I_(2j+1)/I_1 about exp(-2j(j+1)/s), and they are consistent; that ratio is marked RECALLED there. One overstatement: item 2 says the rate is "exact" in the model of Proposition EL; it is right only to leading order (Section 5 above). **Verdict: Section 8 marks every non-proved sentence as direction, through its heading and first line.**
- **Section 6, one label is too strong.** "Why no bound of this kind can reach the target (PROVED, one line)" gives a reason, not a precise statement with a proof: "a bound of this kind" is not defined. Corrected mark: GUIDE, unless the claim is stated exactly (which bounds, which constants) and proved; the file does not do this. No proof uses this sentence. The rest of Section 6 is marked sketch or GUIDE, and the normal-family step is flagged as not written.
- **Section 7, the GUIDE paragraph.** I checked one line of it: the vacuum side of the "soft route". log lambda_0 is convex in s (`gap-mid-max.md` Lemma 4.2), so DD(psi_0)(s) >= its limit at s -> 0+, which is -6 abs(B) (psi_0 -> 1, <V_1> -> 3 abs(B), R -> 3 abs(B), and the first gauge-invariant label with N > 0 is a plaquette with N = 4, whose weight w vanishes as s -> 0). So -s DD(psi_0) <= 6 s abs(B), which equals the leading term of s(<V_1> + <R>) in any state. This supports the sentence. The excited side is not done, as the file says.
- **Section 1, one phrase.** "every real time" should read "every real t >= 4" (as in Theorem B). Wording only.

## 11. Inputs that are recalled, not rebuilt

- (RK), Rellich's theorem (Kato, Chapter VII Section 3): used in consequence (1) only for the branch form of Theorem U, in consequence (2) for Theorem B1, and in (3). Correctly marked RECALLED. Proposition EL and Proposition SUF do not use it (SUF uses only the analyticity of Tr T^t and of the simple lambda_0, and (3) for the latter).
- Schur: Lemma C uses Schur's lemma together with the irreducibility of D^j (neither is proved in `gap-transfer.md`, whose 2.5 only defines D^l and computes chi_l), and Schur orthogonality (mutual orthogonality of the H_j, orthonormality of characters). The file marks "Schur orthogonality" only; the corrected mark names all three. Orthonormality of characters can be read from Weyl's formula by hand.
- Peter-Weyl for SU(2): used in Theorem B1 (and so in Theorem B) for the (VIR_K) clause, to make every level positive. Named in the proof, missing from the mark (Section 7 above).
- Weyl's integration formula for SU(2), in Lemma J (d): the file derives it in one line from N.1 of `gap-transfer.md` (Haar = surface measure of S^3; the polar slice at angle x has area proportional to sin^2 x). Adequate.

## 12. Summary table

| Statement | Verdict |
|---|---|
| Lemma J (a), (b), (c), (d), (e), (f) | HOLDS (each); hand test of (d), (e), (f) at j = 1/2, s = 1 passes, and (d) at j = 1/2 holds as a series identity by a second derivation (semicircle moments) |
| Lemma C | HOLDS; mark should name Schur's lemma, irreducibility of D^j and Schur orthogonality as RECALLED; the trace argument without Peter-Weyl is correct |
| Consequences (1), (2), (3) of (RK) | HOLD given (RK); (RK) is correctly cited |
| Theorem U (i) | HOLDS |
| Theorem U (ii) | HOLDS; three terms of T' and the minus sign of the magnetic term checked; P psi = psi used correctly (twice); finiteness of <N>_w is a missing line, supplied |
| Theorem U (iii) | HOLDS; the split into <eta>_w + D needs one convergence line, supplied; D >= 0 also follows from w log(w/q) >= w - q |
| Theorem U (iv) and the branch form | HOLDS; valid at every 0 < s < 4 for every box with sides at least 3 |
| Proposition EL | HOLDS; Section 8 calls its rate "exact", it is right to leading order |
| Corollary U' | HOLDS |
| Theorem B1 | HOLDS AFTER CORRECTION: continuity of lambda_1 is from min-max or (RK) (2), not Lemma 4.1; the (VIR_K) clause needs Peter-Weyl, which belongs in the mark |
| Theorem B | HOLDS; all arithmetic redone; (VIR_K) clause inherits the Peter-Weyl input |
| Proposition SUF and its example | HOLDS; the cited bound on G(4) is Theorem SC (ii) at k = 4 on the periodic box, limit q -> infinity; one sign slip in the (T') arithmetic of the example ("- 3.3" for "+ 3.22") is harmless |
| Section 8 | marks every non-proved sentence as direction (by heading and first line) |
| Section 6, "PROVED, one line" | label too strong; should be GUIDE; no proof uses it |

No statement FAILS. The first-order formula is right, so Theorem U can be used at a coupling of order one below 4, for every level of every box, given (RK) for its branch form and the Schur facts above. The open statement of the source, (BAND-sc), is not touched by this check.

## Status block (final)

Completed 2026-11-11 (12:19Z to 12:28Z). Check of our own new text; not a proof of an open lemma; no open lemma attacked. No numerics were run; the hand test is displayed arithmetic. Same provider as the author (Claude), different model; so by the rules of this folder it is not the other-provider check. Not covered: the proofs of the cited checked inputs (`gap-seed-sc.md` Theorems S, D, 3, Corollary S3', (P), Corollary 2.3; `gap-sc-box.md` Theorem SC), Section 5 (GUIDE run; not re-run), and the literature names (Schor, O'Carroll, Braga, Michael, Rothe, Karsch). Nothing was committed or pushed; the only file written is this one.

RESULT: every numbered statement of `gap-vir-sc.md` holds — Lemma J (a)-(f), Lemma C, the (RK) consequences, Theorem U (i)-(iv) at every s < 4, Proposition EL, Corollary U', Theorem B, Proposition SUF — and Theorem B1 holds after correcting two input attributions (continuity of lambda_1 by min-max, Peter-Weyl for the (VIR_K) clause); recalled inputs are Rellich-Kato, Schur's lemma with irreducibility and orthogonality, and Peter-Weyl; the hand test at j = 1/2, s = 1 passes; Section 8 is marked as direction; (BAND-sc) stays open.
