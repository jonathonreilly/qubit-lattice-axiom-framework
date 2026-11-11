lead: anthropic/claude-opus-5-5/high mac-mini-worker
lease_until: 2026-11-12T00:19Z

# Check of `library/gap-vir-sc.md` (row 715)

Provenance: written by Claude Opus 5.5, effort high, Mac mini worker 2, at commit 2a7b3fde7. One reading by one model. Not an audit. The checked file was written by Claude Fable 5.2 medium (row 710). Both are Claude models, so this is not a check by the other provider.

## Status block

Started 2026-11-11T12:19Z. In progress. Verdicts are appended one at a time below.

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

