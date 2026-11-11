lead: anthropic/claude-fable-5-2/medium mac-mini-worker
lease_until: 2026-11-11T23:45Z

# gap-vir-sc: (VIR_K) and (LEV_K) at strong coupling (queue row 710)

Research-stage working state. It grants no status. Nothing here is a public claim.

Pinned at commit dd62c14ce on `claude/ym4d-hard-route`. Written by Claude Fable 5.2, medium effort, one session, no subagents. Author run, not a check. Written in steps (save rule, row 675).

## 0. Log of the run

- 2026-11-11 11:45 UTC. Started. No earlier work of this item at the pinned commit. Reading FINISH row 710, GOAL.md, `library/gap-mid-max.md`.
- About 11:55 UTC. Read whole: row 710, GOAL.md, `gap-mid-max.md` (all sections), `gap-seed-sc.md` (all). Duplicate check done (Section 1). First plan, before any proof (kept so that a lost response loses nothing):
  1. Write the transfer operator as exp(-sV/2) A_s exp(-sV/2) and take the derivative of each eigenvalue branch in s (first-order formula). This turns (LEV_K) into an inequality between an "electric number", a plaquette mean and the level, each in the excited state minus the vacuum.
  2. Without the subtraction of the vacuum the inequality is exact for every box and every s < 2 (expected Theorem U). With the subtraction a term of order s abs(B) is left. So the expected proved range is s <= c/b^3 (outcome B), and the expected open statement is the removal of that extensive term (outcome D).
  3. The row's route (term by term in the winding polymers) with the bounds the repository has gives a range that shrinks like (R/4)^(4t); to be stated with the first term that breaks.
- About 12:00 UTC (the two times above this line were written from memory; the lock record gives 12:02 for the next step). Read whole: `gap-sc-box.md`; `gap-transfer.md` Notation and Sections 1 to 4 (the operator); `gap-seed-shape.md` was read at its headings and the lead note only (Theorem SH enters here only through `gap-mid-max.md`). Repo search done. Sections 1 to 4 below written.

## 1. Position, repo search, duplicate check, credits

**Kind of result.** Outcome (B) with outcome (D). The target of the row (a fixed C, all cubes, all s up to beta_c) is NOT proved and NOT refuted. Proved: (LEV_K) and (VIR_K) with K(s) = 2/(s log(1/s)) on every cube of side b >= 8 for s <= min(10^(-6), 1/(10 b^3)), every level and every real time; and, for every s < 4 and every box, (LEV_K) with a rate that has an explicit box term. The first term that breaks outside s b^3 <= 1/10 is named (the action of the vacuum in one slab, of order s abs(B)). One exact statement is left, (BAND-sc) of Section 7. No mass gap at a coupling of order one is claimed.

**What this file did not cover.** No check by another model. Cubes of side 4 to 7. No proof of (BAND-sc). The literature (row 711 owns it): nothing was fetched, and every name below is from memory unless a repository line is given. The Sussman-Alpoge account was not opened in this run: the two facts taken from it are read through `gap-transfer.md` Remark 2.6 (their GL3, the Bessel form of the link weights, rebuilt in Lemma J below and found equal) and `gap-sc-box.md` Section 0 (their polymer theorem; not used).

**Duplicate check (rule 0a).** `library/open-core.md`: no hit for VIR, LEV_K, virial, Hellmann, action deficit, electric number. FINISH rows: (VIR_K), (LEV_K) appear in rows 708 (source), 710 (this row) and 711 (reading item, literature only, output `library/prior/gap-vir-lit.md`). No other row attacks them. `library/gap-skeleton-final.md` mentions (VIR_K) as an open name only.

**Repo search (rule "repo first").** This checkout has one remote branch (`origin/claude/ym4d-hard-route`); `origin/main` and the PR branches are not fetched here, so they were searched only through the two digests `library/prior/gap-crux-repo-hits.md` and `library/prior/gap-crux-prior-repo.md`. Hit: `docs/NATIVE_GAUGE_TRANSFER_BLOCK_HELLMANN_MONOTONICITY_RUNG_EIGHT_BOUNDED_NOTE_2026-06-12.md` (main), described in the digest (line 811) as an SU(3) finite-block first-order split that "does not prove eventual monotonicity". It is not the statement here and was not read. In this folder: `gap-mid-max.md` Section 4.4 Way 2 states the bound K <= 12 abs(B)/m as GUIDE, "not proved". Theorem B1 below proves a bound of that kind. `gap-transfer.md` gives the operator and Remark 2.6 the link weights ("not used" there). No file takes the derivative of a level in the coupling.

**Credits.** Row 708 (Claude Fable 5.2 max): (VIR_K), (LEV_K), Theorem TR, Remark LEV, Way 2, and the reading "4t against 4t log(4/s)" (the lead's). Row 667 (`gap-transfer.md`): the transfer operator, its trace, positivity, the simple top eigenvalue. Rows 683, 701 (Claude Opus 5.5; Claude Fable 5.2 medium): the strong-coupling expansion on the box and on the torus, the gap bound of `gap-seed-sc.md` Theorem 4 (with Theorem S and Corollary S3' of rows 697, 699). Sussman and Alpoge with Claude and Codex: the link weights in Bessel form (GL3, through `gap-transfer.md` 2.6). Osterwalder and Seiler; Luscher (transfer operator; names through row 667). Kogut and Susskind (the electric and magnetic split; RECALLED name). Rellich; Kato (analytic families; RECALLED, used as input (RK)). C. Michael; H. Rothe (lattice sum rules; names from row 711, not read).

**Marks.** PROVED = proved by hand here from the named inputs, not checked by another model. PROVED GIVEN (X). RECALLED = a standard fact not rebuilt here. GUIDE = a run or an estimate, used in no proof. OPEN.

## 2. Setting, and the link weights

**The operator.** B is a periodic box with all sides at least 3, E its set of 3 abs(B) spatial links, X = SU(2)^E, H = L^2(X). As in `gap-transfer.md` (N.4, N.7, Section 1), at the coupling s > 0:

- V_1 := sum over the 3 abs(B) spatial plaquettes of (1 - s_p), 0 <= V_1 <= 6 abs(B); M_s := multiplication by exp(-s V_1/2);
- C_s := the integral operator with the kernel prod over l in E of c_s(u_l v_l^(-1)), c_s(g) = exp(-s (1 - (1/2) tr g));
- P := the gauge projection; T(s) := P M_s C_s M_s P = M_s C_s M_s P on H_inv = Ran P.

Z(t, B; s) = Tr T(s)^t, T(s) >= 0 is trace class, its top eigenvalue lambda_0(s) is simple with a gauge-invariant positive eigenvector psi_0, and exp(-12 s abs(B)) <= lambda_0 <= 1 (`gap-transfer.md` Statements 1 to 4; the box with three sides: `gap-crux-restate.md` line 33). Levels: for an eigenvalue lambda > 0, Ehat := -log lambda >= 0 and E := log(lambda_0/lambda) = Ehat - Ehat_0.

**Lemma J (the link weights; PROVED, elementary).** For an integer n >= 0 and s > 0 put J_n(s) := sum over k >= 0 of (s/2)^(n+2k)/(k! (n+k)!), and r_n := J_(n+1)/J_n. For j in {0, 1/2, 1, ...} put c_j(s) := (1/(2j+1)) times the Haar integral of c_s(g) chi_j(g), with chi_j the character of the representation of dimension 2j+1.
(a) J_n(s) = (1/pi) integral over [0, pi] of exp(s cos x) cos(n x) dx.
(b) J_(n-1) - J_(n+1) = (2n/s) J_n for n >= 1, and s J_n' = n J_n + s J_(n+1).
(c) 0 < r_n(s) <= s/(2(n+1)).
(d) c_j(s) = (2 exp(-s)/s) J_(2j+1)(s) > 0.
(e) With eta_j := -log c_j: -s eta_j'(s) = 2j - s (1 - r_(2j+1)(s)). So for 0 < s <= 4: 2j - s <= -s eta_j' <= 2j.
(f) c_j(s) <= (s/4)^(2j) for all s > 0. So eta_j(s) >= 2j log(4/s), and eta_0 >= 0.

Proof. (a) Expand exp(s cos x) = sum over m of s^m cos^m x/m!. cos^m x = 2^(-m) sum over i of binom(m, i) cos((m - 2i) x) (the imaginary parts cancel in pairs). (1/pi) integral of cos(k x) cos(n x) over [0, pi] is 1 for k = n = 0, 1/2 for abs(k) = n >= 1 and 0 otherwise. So the coefficient of s^m is 2^(-m) binom(m, (m-n)/2)/m! when m - n is even and non-negative, and 0 otherwise. With m = n + 2k this is 2^(-m)/(k! (n+k)!). (b) In J_(n+1) shift k to k - 1: J_(n-1) - J_(n+1) = sum over k of (s/2)^(n-1+2k) ((n+k) - k)/(k! (n+k)!) = (2n/s) J_n. s J_n' = sum of (n + 2k) (s/2)^(n+2k)/(k! (n+k)!) = n J_n + 2 sum over k >= 1 of (s/2)^(n+2k)/((k-1)! (n+k)!) = n J_n + s J_(n+1). (c) Term by term: the k-th term of J_(n+1) is the k-th term of J_n times (s/2)/(n+k+1) <= s/(2(n+1)). (d) A class function f of the angle x (eigenvalues exp(+-ix)) has Haar integral (2/pi) integral over [0, pi] of f(x) sin^2 x dx (Haar measure is the surface measure of the unit sphere of R^4, `gap-transfer.md` N.1, and x is the polar angle). chi_j = sin((2j+1) x)/sin x (`gap-transfer.md` 2.5). So (2j+1) exp(s) c_j = (2/pi) integral of exp(s cos x) sin((2j+1) x) sin x = (1/pi) integral of exp(s cos x) (cos(2j x) - cos((2j+2) x)) = J_(2j) - J_(2j+2) = (2 (2j+1)/s) J_(2j+1), by (a) and (b). (e) eta_j = s + log(s/2) - log J_(2j+1), so -s eta_j' = -s - 1 + (2j+1) + s r_(2j+1), by (b). For s <= 4, r_(2j+1) <= s/4 <= 1 by (c). (f) (2/s) J_(2j+1) = sum over k of (s/2)^(2j+2k)/(k! (2j+1+k)!) <= ((s/2)^(2j)/(2j+1)!) sum over k of (s/2)^(2k)/(k!)^2, because (2j+1+k)! >= (2j+1)! k!. A sum of squares of non-negative numbers is at most the square of their sum, so the last sum is at most (sum of (s/2)^k/k!)^2 = exp(s). And (2j+1)! >= 2^(2j). QED

(d) agrees with the form recorded in `gap-transfer.md` Remark 2.6 from the Sussman-Alpoge account (their GL3). So that line is now rebuilt.

**Lemma C (the kinetic operator is diagonal in the link representations; PROVED GIVEN Schur's orthogonality relations for SU(2), RECALLED).** For j as above let H_j be the span in L^2(SU(2)) of the matrix coefficients of the representation D^j; the H_j are finite dimensional (dimension (2j+1)^2) and mutually orthogonal. For a label n = (j_l), l in E, let H_n be the tensor product of the H_(j_l), a subspace of H, and Pi_n its orthogonal projection. Put c_n(s) := prod over l of c_(j_l)(s) and N(n) := sum over l of 2 j_l. Then
C_s = sum over n of c_n(s) Pi_n, and for the derivative in s (the integral operator with the kernel d/ds of the kernel of C_s): C_s' = sum over n of c_n'(s) Pi_n,
both in the sense of quadratic forms on H. Each Pi_n commutes with P.

Proof. One link. For a class function c and f = D^j_(ab): integral of c(u v^(-1)) D^j_(ab)(v) dv = integral of c(w) D^j_(ab)(w^(-1) u) dw = sum over e of [integral of c(w) D^j(w^(-1)) dw]_(ae) D^j_(eb)(u). The matrix in the bracket commutes with D^j (c is a class function), so it is a scalar (Schur), equal to its trace divided by 2j+1, which is c_j when c = c_s (chi_j is real), and c_j' when c = d c_s/ds (differentiate under the integral). The kernel of C_s is a product over the links, and the kernel of C_s' is a sum over l of such products with one factor differentiated. So on H_n, C_s is c_n and C_s' is c_n'. Off the closed span of the H_n: C_s >= 0 is self-adjoint and commutes with every Pi_n, so it maps the orthogonal complement Y of all H_n to itself and is non-negative there. Tr C_s = 1 (`gap-transfer.md` Statement 3). The sum over n of c_n dim H_n is the product over the links of sum over j of (2j+1)^2 c_j = c_s(1) = 1, because c_s = sum over j of (2j+1) c_j chi_j with absolute convergence (`gap-transfer.md` (2d), with the orthonormality of the characters) and chi_j(1) = 2j+1. So the trace of C_s on Y is 0 and C_s = 0 on Y. (By the Peter-Weyl theorem Y = 0; this is not needed.) For C_s' on Y: C_s vanishes on Y for every s, and the difference quotients of the kernels converge uniformly, so C_s' = 0 on Y. The gauge action multiplies each link variable on both sides by fixed elements, which maps each H_j to itself; so it maps H_n to itself and P commutes with Pi_n. QED

**Input (RK) (RECALLED: Rellich; Kato, Perturbation theory, Chapter II Section 6 and Chapter VII Section 3; not rebuilt).** The kernel of T(s) is entire in s and bounded on compact sets, so T(s) is an entire family in the Hilbert-Schmidt norm, self-adjoint for real s. For such a family: near every real s_0, the eigenvalues of T(s) in a neighbourhood of an eigenvalue lambda(s_0) > 0 of multiplicity r are given by r real-analytic functions, with real-analytic orthonormal eigenvectors.

Consequences used (PROVED GIVEN (RK)). (1) Along an analytic branch (lambda(s), psi(s)): lambda' = <psi, T'(s) psi>, because <psi', T psi> + <T psi, psi'> = lambda d/ds of the norm squared = 0. (2) The ordered positive eigenvalues lambda_i(s) are continuous, and on a compact interval of couplings each ordered level, as long as it stays above a positive bound, is made of finitely many pieces, each a piece of one analytic branch: near s_0 the finitely many branches that pass near lambda_i(s_0) are equal or cross at isolated points, so on each side of s_0 the i-th in order is one of them. (3) lambda_0 is simple, so it is one analytic branch.

## 3. Theorem U: the first-order formula and the inequality without the vacuum subtraction

**Theorem U (PROVED GIVEN Lemma J, Lemma C).** Let B be a box with sides at least 3, 0 < s < 4, and psi a unit eigenvector of T(s) in H_inv with eigenvalue lambda > 0. Put q_n := norm squared of Pi_n M_s psi, w(n) := c_n(s) q_n/lambda, and DD(psi) := <psi, T'(s) psi>/lambda. Then:
(i) w is a probability weight on the labels, and the sum of the q_n is at most <psi, exp(-s V_1) psi> <= 1.
(ii) (first-order formula) s DD(psi) = <N>_w - s <psi, V_1 psi> - s <R>_w, where R(n) := sum over l of (1 - r_(2 j_l + 1)(s)), 0 <= R <= 3 abs(B). Hence -9 s abs(B) <= s DD(psi) <= <N>_w.
(iii) (energy) -log lambda = <eta>_w + sum over n of w(n) log(w(n)/q_n) >= <eta>_w >= log(4/s) <N>_w, with eta(n) := sum over l of eta_(j_l).
(iv) s DD(psi) <= (-log lambda)/log(4/s).
Along an analytic branch, DD(psi(s)) = d log lambda/ds. So every unsubtracted level Ehat = -log lambda of every box satisfies -s dEhat/ds <= Ehat/log(4/s) on (0, 4): Ehat(s)/log(4/s) is non-decreasing.

Proof. (i) lambda = <psi, T psi> = <M psi, C M psi> (P psi = psi) = sum of c_n q_n by Lemma C. The Pi_n are mutually orthogonal, so the sum of the q_n is at most the norm squared of M psi.
(ii) T' = P (M' C M + M C' M + M C M') P with M' = -(V_1/2) M (differentiate the kernel). <psi, M' C M psi> = -(1/2) <V_1 psi, M C M psi> = -(1/2) <V_1 psi, T psi> = -(lambda/2) <psi, V_1 psi>, using M C M psi = M C M P psi = T psi. The term with M on the right is the complex conjugate, and V_1 is real. So these two give -lambda <psi, V_1 psi>. The middle term is <M psi, C' M psi> = sum of c_n' q_n (Lemma C). So s DD = -s <V_1> + sum of w(n) s c_n'/c_n, and s c_n'/c_n = sum over l of (-s eta_(j_l)') = N(n) - s R(n) by Lemma J (e). 0 <= 1 - r <= 1 for s <= 4 (Lemma J (c)), there are 3 abs(B) links, and 0 <= V_1 <= 6 abs(B).
(iii) For each n with q_n > 0: lambda = c_n q_n/w(n), so -log lambda = eta(n) + log(w(n)/q_n). Average over w. By the log-sum inequality, sum of w log(w/q) >= (sum of w) log(sum of w / sum of q) >= 0 by (i). eta(n) >= log(4/s) N(n) by Lemma J (f), where log(4/s) > 0.
(iv) By (ii) and (iii). QED

**Remarks.** (1) Theorem U holds at every coupling below 4 and for every level of every box, the vacuum included. It is the one place in this file where an inequality of the kind of (LEV_K) is exact. Its content: the s-derivative of a level counts the electric number N of the state (the total of 2j over the links, read in the kinetic operator), and the level itself is at least log(4/s) times that number. The magnetic term has the favourable sign because V_1 >= 0.
(2) What it does not give: (LEV_K) is the same inequality for E = Ehat - Ehat_0. The vacuum has Ehat_0 of order s abs(B) and s DD(psi_0) of order -s abs(B) (its action in one slab). These do not cancel against anything in Theorem U. This is danger (4) of the row, in exact form.

**Proposition EL (the model without spatial plaquettes; PROVED GIVEN Lemma J, Lemma C; a test of the rate).** Replace V_1 by 0 (the time-like plaquettes only). Then T = C_s P, its eigenvalues on H_inv are numbers c_n(s) (for the labels n for which H_n meets H_inv), the vacuum is n = 0, and for every level, every box and every 0 < s <= 2:
E = sum over l of (eta_(j_l) - eta_0), -s E' <= N (1 + s^2/6), and E >= N (log(4/s) - s^2/8). So (LEV_K) holds for every level of every box with K(s) = (1 + s^2/6)/(s (log(4/s) - s^2/8)).
Proof. P commutes with C_s and with each Pi_n, so T is c_n on Pi_n H_inv; c_j/c_0 = J_(2j+1)/J_1 < 1 for j >= 1/2 (Lemma J (c)), so n = 0 is the top. By Lemma J (e), -s E' = N - s sum over the links with j_l > 0 of (r_1 - r_(2 j_l + 1)) <= N + s sum over these links of r_(2 j_l + 1). For j >= 1/2, r_(2j+1) <= s/(2 (2j+2)) <= s/6, and the number of these links is at most N (each has 2 j_l >= 1). So -s E' <= N (1 + s^2/6). For E: J_1 >= s/2, and J_(2j+1) <= ((s/2)^(2j+1)/(2j+1)!) sum over k of (s/2)^(2k)/(k! 2^k) = ((s/2)^(2j+1)/(2j+1)!) exp(s^2/8), because (2j+1+k)!/(2j+1)! >= (k+1)! >= 2^k. So eta_j - eta_0 = log(J_1/J_(2j+1)) >= 2j log(2/s) + log((2j+1)!) - s^2/8 >= 2j (log(4/s) - s^2/8) for j >= 1/2, and log(4/s) - s^2/8 >= log 2 - 1/2 > 0 on (0, 2]. All branches are explicit here, so (RK) is not needed. QED
So in the solvable case the rate of the row is right, for all levels, uniformly in the box: K(s) s log(1/s) tends to 1 as s tends to 0.

## 4. With the vacuum subtraction: a rate with a box term, and the target on s b^3 <= 1/10

**Corollary U' (PROVED GIVEN Theorem U and `gap-transfer.md` (4b)).** For B, s, psi as in Theorem U with psi orthogonal to psi_0, and E = log(lambda_0/lambda):
s (DD(psi) - DD(psi_0)) <= E/log(4/s) + s abs(B) (9 + 12/log(4/s)).
Proof. s DD(psi) <= Ehat/log(4/s) = (E + Ehat_0)/log(4/s), and Ehat_0 = -log lambda_0 <= 12 s abs(B). -s DD(psi_0) <= 9 s abs(B) by Theorem U (ii). QED

**Theorem B1 ((LEV_K) with a box term, every coupling below 4; PROVED GIVEN Corollary U', (RK), and `gap-mid-max.md` Lemma 4.1 for the continuity of the gap).** Let B be a box with sides at least 3 and m(B; s) = E_1(s) > 0 its gap. Put
K_B(s) := 1/(s log(4/s)) + abs(B) (9 + 12/log(4/s))/m(B; s), 0 < s < 4.
Then K_B is continuous, and for all 0 < s < s' < 4 and every ordered level with lambda_i > 0 on [s, s']: E_i(s') >= E_i(s) exp(- integral of K_B over [s, s']). This is (LEV_K) with K = K_B. Hence (VIR_K) holds with K = K_B at every real t >= 4.

Proof. On an analytic branch, -E' = DD(psi) - DD(psi_0) <= E/(s log(4/s)) + abs(B)(9 + 12/log(4/s)) <= K_B E, because E >= m. So (log E)' >= -K_B on each branch. By (RK) (2), log E_i is continuous and made of finitely many such pieces on [s, s']; integrate. m = E_1 is continuous by (RK) (2) or by Lemma 4.1.
(VIR_K) from (LEV_K): by Remark LEV of `gap-mid-max.md`, G(t exp(integral of K over [s, s+h]); s+h) <= G(t; s). So G(t; s+h) - G(t; s) <= G(t; s+h) - G(t exp(...); s+h) = -(dG/dt)(xi; s+h) t (exp(integral) - 1) for a xi between. Divide by h and let h decrease to 0; dG/dt is jointly continuous for t >= 4 (Lemma 4.1) and K is continuous. The upper limit is at most -K(s) t (dG/dt)(t; s). (Levels with lambda_i = 0 do not enter G. By the Peter-Weyl theorem, RECALLED, there are none in H_inv; without it, read the statement for the positive levels.) QED

This proves the bound that `gap-mid-max.md` 4.4 Way 2 gives as GUIDE (there K <= 12 abs(B)/m), with the unbounded electric part handled by Theorem U.

**Theorem B (the row's target on a restricted range; PROVED GIVEN Theorem B1 and `gap-seed-sc.md` Theorem 4).** Let b >= 8 and B = b^3. For 0 < s <= 10^(-6): m(B; s) >= log(1/s), and (LEV_K), (VIR_K) hold on (0, 10^(-6)] with
K(s) = (1 + 10 s b^3)/(s log(1/s)).
In particular, for 0 < s <= min(10^(-6), 1/(10 b^3)): (LEV_K) for every level and (VIR_K) for every real t >= 4 hold with K(s) = 2/(s log(1/s)).

Proof. `gap-seed-sc.md` Theorem 4 with n = 4: theta = 12800 s <= 0.0128, 4 theta^4 <= 0.18, and b >= 8 = 2n, so m >= 4 log(1/theta) - (4 log 4 + log 1614)/4. log 12800 = 7 log 2 + 2 log 10 < 4.86 + 4.61 = 9.47; 4 log 4 < 5.55, log 1614 < 7.39, so the last term is below 3.24. With L := log(1/s) >= 6 log 10 > 13.81: m >= 4L - 37.88 - 3.24 = 4L - 41.12 >= L, because 3L >= 41.43. log(4/s) >= L and log(4/s) > 15, so 9 + 12/log(4/s) < 10 and K_B(s) <= 1/(sL) + 10 b^3/L. A larger continuous K keeps (LEV_K) and (VIR_K). QED

**What Theorem B gives and does not give.**
- Integral of K: for beta_0 < beta_1 in the range, the integral of 2/(s log(1/s)) is 2 log(L_0/L_1), L_i = log(1/beta_i). So exp(integral of K) = (L_0/L_1)^2.
- In Corollary TR1 (b >= 256, beta_0 <= 1/25600): the range is beta_1 <= 1/(10 b^3) <= 6 x 10^(-9). The seed there is known (Theorem DOB: beta < 1/18; `gap-seed-sc.md`: beta < 1/12800). Nothing new is reached.
- Outside the range the proof gives K_b(s) <= (1 + 10 s b^3)/(s log(1/s)): a rate that grows like b^3. The allowance of Corollary TR1 is an integral of at most log(b/(2 ceil(log_2 b))). The integral of 10 b^3/log(1/s) over [beta_0, beta_1] is about 10 b^3 (beta_1 - beta_0)/L. So the proved rate is inside the allowance only on intervals of length of order (L log b)/(10 b^3). It is useless for the transport, as expected of a bound of the kind of Way 2.
- **The first term that breaks outside s b^3 <= 1/10:** the term s abs(B)(9 + 12/log(4/s)) of Corollary U'. It is made of two numbers of the vacuum: its level Ehat_0 <= 12 s abs(B) and its derivative -s DD(psi_0) <= 9 s abs(B). In the true (LEV_K) these cancel against the same extensive parts of the excited state. Theorem U cannot see the cancellation, because it bounds each state alone.
- Not covered: cubes of side 4 to 7 (no explicit lower bound on m was taken from the repository for them; Theorem B1 holds for them with their own m).

### Status block (first; kept current in Section 9)

- Proved (not checked): Lemma J, Lemma C, Theorem U, Proposition EL, Corollary U', Theorem B1, Theorem B.
- Inputs not rebuilt: (RK) Rellich's theorem; Schur orthogonality for SU(2).
- Open: the target of the row for s b^3 > 1/10.
