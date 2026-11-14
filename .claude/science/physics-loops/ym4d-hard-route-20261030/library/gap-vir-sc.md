lead: anthropic/claude-fable-5-2/medium mac-mini-worker
lease_until: 2026-11-11T23:45Z

# gap-vir-sc: (VIR_K) and (LEV_K) at strong coupling (queue row 710)

Research-stage working state. It grants no status. Nothing here is a public claim.

Pinned at commit dd62c14ce on `claude/ym4d-hard-route`. **Lead note (row 715, 2026-11-11; Claude Opus 5.5, lead session):** checked line by line by Claude Opus 5.5 high (`library/gap-vir-sc-check.md`; same provider). Every numbered statement holds, Theorem U at every s below 4 included. Theorem B1 holds after two corrections of its input marks: the continuity of lambda_1 comes from min-max or (RK) (2), not from Lemma 4.1; the (VIR_K) clause needs the Peter-Weyl theorem (RECALLED), which belongs in the mark. Written by Claude Fable 5.2, medium effort, one session, no subagents. Author run, not a check. Written in steps (save rule, row 675).

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

- 12:10 UTC. GUIDE run done under the numeric lock (memory free 59 percent at the start), lock released. Sections 5 to 9 written.

## 5. GUIDE: a one-plaquette model (a run; it proves nothing)

Scripts and logs: `/tmp/gap-vir-sc-scripts/toy.py`, `toy2.py`; `/tmp/gap-vir-sc-scratch/toy.log`, `toy2.log` (on the Mini, outside git). Model: one spatial plaquette with four links; the gauge-invariant functions are the class functions of the plaquette variable, with the basis chi_j, j <= 15; T = exp(-s(1 - S)/2) diag(c_j(s)^4) exp(-s(1 - S)/2), S the multiplication by (1/2) chi_(1/2) (entries 1/2 next to the diagonal). mpmath, 700 digits, derivative by a central difference.

Criteria written before the run. P1: c_j by quadrature against Lemma J (d). P2: Theorem U (iv) for the six top levels on a grid of 15 couplings from 10^(-6) to 3.9; a failure would refute the theorem or its use. P3: report kappa_i := (-E_i'/E_i) s log(1/s) and K_i s.

Results. P1 pass. P2: the first run (90 digits) reported a failure at s = 10^(-6) and 10^(-4); it was round-off (levels below 10^(-90)); at 700 digits P2 passes at every point, with the smallest margin at the vacuum (5 x 10^(-6) at s = 10^(-6)). P3, levels 1 to 5:

| s | kappa_1 | kappa_5 | K_1 s | max over i of K_i s |
|---|---|---|---|---|
| 10^(-6) | 0.909 | 0.873 | 0.066 | 0.066 |
| 10^(-4) | 0.869 | 0.821 | 0.094 | 0.094 |
| 10^(-2) | 0.769 | 0.696 | 0.167 | 0.167 |
| 0.1 | 0.623 | 0.534 | 0.271 | 0.271 |
| 0.5 | 0.319 | 0.253 | 0.460 | 0.460 |
| 1 | | | 0.593 | 0.593 |
| 2 | | | 0.543 | 0.637 |
| 3 | | | 0.171 | 0.615 |
| 3.9 | | | -0.044 | 0.565 |

Reading. With the magnetic term and the vacuum subtraction, in a model with no volume, the rate has the form of the row with C below 1 (kappa is below 1 because the true logarithm is log(4/s)), for all five levels. K s stays below 0.64 up to s = 3.9, and the first level stops falling near s = 3.6 (its E_1 has a minimum of about 3.23; a model of one plaquette has no scaling region). What the run cannot show: anything about the box term, which is the open point.

## 6. The route the row names, and the five dangers

**The route (compare s dG/ds with -t dG/dt term by term in the winding polymers). A sketch, not written as a proof, because Theorem B covers more.** With what the repository has for a periodic box with sides at least 5 and an integer t >= 3 (`gap-seed-sc.md` (P), Corollary 2.3, Proposition 4.4; the limit q to infinity taken with a normal-family argument, which I did not write out): G(t; B; s) = s^(4t) h(s) with h analytic on abs(s) < R = 1/12800, h(0) = 3 abs(B) 4^(-4t), abs(h) <= M R^(-4t), M = abs(B) t/100. Then s G' = 4t G + s^(4t+1) h'(s) and abs(h') <= 2 M R^(-4t-1) for s <= R/2, so s G' <= 4t G + 2M (s/R)^(4t+1), and G >= 3 abs(B) (s/4)^(4t) - 2M (s/R)^(4t+1). The remainder is below one percent of the leading term only for s <= R (R/4)^(4t)/t. In that range s G' <= 4.01 t G, and with -t dG/dt >= t m S/(1 + S) this gives (VIR_K) at the integer time t with K about 4.1/(s log(1/s)).
- The first term that breaks: the Cauchy remainder 2M (s/R)^(4t+1). It has the base 1/R = 12800 where the leading term has the base 1/4. The range s <= R (R/4)^(4t)/t is below 10^(-60) at t = 3 and shrinks like 51200^(-4t). Theorem B (s <= 1/(10 b^3), all real t >= 4) contains it for t >= 4 and 8 <= b <= 10^18; the sketch adds only t = 3 and the sides 5 to 7, in a range below 10^(-60).
- Why no bound of this kind can reach the target (PROVED, one line): (VIR_K) with K = C/(s log(1/s)) allows a constant factor C between s D_s G and 4t S, and no change of the base. An upper bound on D_s G of the form (const)^t (s/4)^(4t) with const > 1 is too weak at large t. So the s-derivative must be known with the exact exponential rate of the lowest levels, that is, the derivative of those levels themselves. This is why Sections 3 and 4 work with the levels and not with the polymers.
- A further obstacle to any proof by analyticity in s, uniform in t (GUIDE, not proved): for complex s the lowest band contributes a sum over momenta of rho(p; s)^t; when t times the complex band width is of order one this sum has zeros (for a cosine band it is a product of functions of the kind of J_0 at a complex argument). So G(t; B; .) has zeros at abs(s) of the order of a negative power of t, and no disc in s that is uniform in t carries a zero-free G. The derivative in s has to be controlled on the real axis.

**The five dangers of the row.**
1. Spatial decoration. In the level form a decoration is part of the level E_i(s); it has no separate term. In Theorem U (ii) the spatial plaquettes enter through -s <V_1>, with the favourable sign for each state alone, and the unbounded electric part is bounded by the level itself. No term with more plaquettes per unit of time than the level allows was found. The danger is real only through the vacuum subtraction (4).
2. Many windings and excited levels. (LEV_K) is a statement for each level, and Theorems U and B1 hold for all levels at once, with no count of them. In the thermal form the levels at least log(1/s) above the lowest ones are harmless at the times of the row, even with the crude extensive bound: Proposition SUF below.
3. Uniformity in b. This is where the proof stops: s b^3 <= 1/10.
4. The vacuum part. This is the exact obstruction. In formulas: -s E' = (<N>_w - <N>_(w_0)) - s (<V_1>_psi - <V_1>_(psi_0)) - s (<R>_w - <R>_(w_0)), three differences of quantities of order abs(B) (for the first one, of order s^2 abs(B) in the vacuum; GUIDE). Theorem U bounds the first and third brackets of the excited state by E and the vacuum terms by 9 s abs(B) + 12 s abs(B)/log(4/s).
5. Non-differentiable points. Resolved GIVEN (RK): the ordered levels are piecewise analytic (Section 2), and (VIR_K) is derived from the integrated (LEV_K) without differentiating G (proof of Theorem B1).

## 7. What is left: one exact statement, and why it is enough at the times of the row

**Proposition SUF (PROVED GIVEN Corollary U', Theorem B, and the bound G(4; B; s) <= (4 abs(B)/100)(12800 s)^16 for a periodic box with sides at least 4, which is the proof of `gap-sc-box.md` Theorem SC (ii) with (P) and Corollary 2.3 of `gap-seed-sc.md` and the limit q to infinity by Lemma A).** Let b >= 8, B = b^3, 0 < s <= 10^(-6), L = log(1/s), C_1 >= 0. Assume at (B, s):
(H1) m(B; s) <= 4.5 L;
(H2) every unit eigenvector psi of T(s) orthogonal to psi_0 with E < 5L has s (DD(psi) - DD(psi_0)) <= C_1.
Let t >= 4 be an integer with
(T) 0.8 b^6 12800^16 s^(t/2 - 3) <= 1, and (T') 0.04 b^3 12800^16 s^16 <= 1.
Then (VIR_K) holds at (t, s) with K(s) = (C_1 + 1)/(s log(1/s)).
Example: s <= exp(-200), 256 <= b <= exp(1000), every integer t >= ceil(log_2 b).

Proof. For an integer t >= 2, G(t; .) = log Tr T^t - t log lambda_0 is real-analytic, d/ds Tr T^t = t Tr(T^(t-1) T'), and in an orthonormal eigenbasis of T on H_inv this is t times the sum of lambda_i^t DD(psi_i). So D_s G = (t/(1+S)) sum over i >= 1 of (DD(psi_i) - DD(psi_0)) rho_i^t, and -t dG/dt = (t/(1+S)) sum over i >= 1 of E_i rho_i^t. (VIR_K) at (t, s) is: sum over i >= 1 of d_i rho_i^t <= 0, with d_i := s (DD(psi_i) - DD(psi_0)) - (C_1 + 1) E_i/L.
Levels with E_i < 5L: d_i <= C_1 - (C_1 + 1) m/L <= -1, because m >= L (Theorem B). By (H1) the level i = 1 is one of them. So their sum is at most -rho_1^t = -exp(-t m) <= -s^(4.5 t).
Levels with E_i >= 5L: by Corollary U' and log(4/s) >= L, d_i <= 10 s b^3. Their sum of rho_i^t is at most exp(-5L (t - 4)) S(4) = s^(5t - 20) S(4). By (T'), G(4) <= 1, so S(4) <= 2 G(4) <= 0.08 b^3 12800^16 s^16. So their part is at most 0.8 b^6 12800^16 s^(5t - 3).
The total is at most s^(4.5 t) (-1 + 0.8 b^6 12800^16 s^(t/2 - 3)) <= 0 by (T).
Example: 16 log 12800 < 151.4. With t >= log_2 b: (t/2 - 3) >= 0.7213 log b - 3, and 200 (0.7213 log b - 3) >= 151.4 + 6 log b when log b >= 5.44; log 256 > 5.54. (T'): 3 log b <= 3200 - 151.4 - 3.3. QED

So at the times of the row the extensive error of Corollary U' does no harm above the lowest levels: the lower end ceil(log_2 b) of the time range is what removes it. What is left concerns only the levels below 5 log(1/s), which at small s should be the single band of 3 b^3 one-plaquette states (GUIDE: the next unperturbed levels have six links).

**(BAND-sc), the one exact statement left (OPEN).** There are beta_c > 0 and C_1 such that for every cube B = b^3 with b >= 256 and every 0 < s <= beta_c:
(H1) m(B; s) <= 4.5 log(1/s), and
(H2) every unit eigenvector psi of T(s) orthogonal to the vacuum with E < 5 log(1/s) satisfies
(<N>_(w_psi) - <N>_(w_0)) - s (<psi, V_1 psi> - <psi_0, V_1 psi_0>) - s (<R>_(w_psi) - <R>_(w_0)) <= C_1
(the left side is s (DD(psi) - DD(psi_0)), by Theorem U (ii)). In words: a state of the lowest band changes the electric number and the spatial action of one time slab by a bounded amount against the vacuum, uniformly in the cube.
By Proposition SUF, (BAND-sc) with beta_c <= exp(-200) gives (VIR_K) with K = (C_1 + 1)/(s log(1/s)) on every cube with 256 <= b <= exp(1000), at the integer times from ceil(log_2 b) on. (The real times between them, and the constants 4.5, 5, exp(-200), are not optimised; the real times need the derivative of Tr T^t at real t, which I did not write.)

What I expect and did not prove (GUIDE). (BAND-sc) should be true with C_1 near 4, by the expansion of the one-particle band (the levels as convergent series in s, uniformly in the periodic box). The repository has no such expansion: `gap-seed-sc.md` Section 7 lists "a bound uniform in n with the sharp base beta/4" as open, and (H1), an upper bound on the gap of the cube, is not in the repository either (the lower bound is `gap-seed-sc.md` Theorem 4). From memory, not verified: R. Schor proved that the glueball mass at strong coupling in infinite volume is 4 log(1/beta) plus an analytic function, and O'Carroll, Braga and Schor treated the spectrum above it; if row 711 confirms a source page, the infinite-volume form of (H1) and of (H2) for the mass is in the literature, and what is ours to do is the periodic cube. A weaker soft route that I see and did not carry out: replace the extensive bound of Corollary U' by one of order s^2 abs(B) (the vacuum side follows from the convexity of log lambda_0, Lemma 4.2: its derivative is at least the value at s = 0; the excited side needs a bound on <psi, exp(s sum of s_p) psi> by the electric number). That would move the range from s b^3 <= 1/10 to s^2 b^3 of order one, and no further.

## 8. Direction, not proof: what the strong-coupling computation says about an identity for s dG/ds at a coupling of order one

(One page. Nothing here is proved beyond the two exact formulas quoted from Theorem U.)

1. **The exact formulas hold at every coupling below 4.** For every level of every box: s d(log lambda)/ds = <N>_w - s <R>_w - s <V_1>_psi (Theorem U (ii)), and -log lambda = <eta>_w + D(w, q) with D := sum of w log(w/q) >= 0 (Theorem U (iii)). The first is the action of one time slab in the state, split into its time-like part (read as the electric number N of the kinetic operator, corrected by R) and its space-like part. The second writes the level as an electric energy <eta>_w plus a relative entropy. Subtracting the vacuum gives, for an excited level,
-s dE/ds = Delta N - s Delta R - s Delta V_1, and E = Delta eta + Delta D,
where Delta is "excited state minus vacuum". So at integer t: s D_s G = (t/(1+S)) sum over i of rho_i^t (Delta N - s Delta R - s Delta V_1)_i. This is an identity for s dG/ds at every coupling. It is the lattice form of the action sum rule (the names C. Michael and H. Rothe are in row 711; not read).

2. **Where the rate 1/(s log(1/s)) comes from.** At small s, eta_j is 2j log(4/s) up to bounded terms, so the electric energy is log(4/s) times the electric number, and D, R, V_1 are corrections. Then -s E' is about Delta N and E is about log(4/s) Delta N. The rate K = 1/(s log(4/s)) is the ratio of "number" to "energy per number". It is exact in the model without spatial plaquettes (Proposition EL) and it is seen in the one-plaquette run (Section 5). The lead's reading in the row (4t against 4t log(4/s)) is this statement for the lowest band, where Delta N = 4.

3. **What changes at a coupling of order one.** For large s the link weights tend to the heat-kernel form, c_j/c_0 about exp(-2j(j+1)/s) (RECALLED asymptotics of the Bessel ratio; not used). Then -s (eta_j - eta_0)' is about eta_j - eta_0: the electric number and the electric energy become the same quantity, and the two formulas give
E + s dE/ds = Delta D + s Delta V_1 + (small),
that is, K s - 1 = -(Delta D + s Delta V_1)/E. This is Way 1 of `gap-mid-max.md` 4.4 as an identity: the electric part alone gives K = 1/s, and everything beyond it is the magnetic deficit plus the entropy term. With the GUIDE value K s about 8 at beta = 2.4 (`gap-mid-max.md` 4.3), Delta D + s Delta V_1 is about -7 E there. So the mechanism of strong coupling (the electric number carries the derivative, the rest is a correction) is not what holds (VIR_K) at a coupling of order one; there the inequality, if true, is a statement about the magnetic and entropy deficits of an excited state. Nothing proved at small s continues to that range by itself.

4. **The form an identity would need.** The first formula is already an identity for the left side of (VIR_K). What is missing is a second identity for the right side, the level E itself, in terms of local expectations: here E contains the relative entropy D, which is not the expectation of a local observable. In the continuum the second identity is the trace anomaly. On the lattice the candidate is the response to an anisotropy: the operator depends on a time-like coupling (in C_s) and a space-like one (in M_s) separately, Theorem U (ii) gives the two partial derivatives of every level (Delta N - s Delta R for the first, -s Delta V_1 for the second), and E is a combination of them whose two coefficients are the derivatives of the couplings with respect to the anisotropy at fixed physics (RECALLED: Karsch's coefficients; the energy sum rule). At small s these coefficients are explicit (the energy is log(4/s) per unit of time-like number). At a coupling of order one they are non-perturbative functions; a proof of (VIR_K) there would need bounds of order one on them, and that is a statement of the same kind as (VIR_K) for the two-coupling family. I see no reduction in strength, only a second exact formula to test numerically.

5. **The part that is the same at every coupling.** The inequality for one state alone (Theorem U) is easy and exact. The difficulty at small s is only the subtraction of the vacuum, that is, the locality of an excitation in the electric number and in the spatial action (statement (BAND-sc)). At a coupling of order one the same locality is a mixing statement of the kind of (W) (row 691) and of Proposition MIX of `gap-mid-max.md`. So candidate C-A does not avoid the mixing input: its inequality "of order one" contains, before any constant is discussed, the statement that an excited state of a large box differs from the vacuum by a bounded amount of action per slab.

## 9. Status block (final)

**Verdict on the row's target** (beta_c > 0 and C with (VIR_K), K = C/(s log(1/s)), for all cubes b >= 4, all s <= beta_c, all t from ceil(log_2 b) to b/2): OPEN. Not proved, not refuted. No term and no level was found for which the inequality fails; the solvable model and the one-plaquette run agree with the rate. As a kill test: candidate C-A is not killed at strong coupling, and it is not established there either.

| Statement | Mark |
|---|---|
| Lemma J (link weights c_j = (2 exp(-s)/s) J_(2j+1); -s eta_j' <= 2j; eta_j >= 2j log(4/s)) | PROVED |
| Lemma C (C_s is diagonal in the link representations; no completeness needed) | PROVED GIVEN Schur orthogonality (RECALLED) |
| Theorem U (every level of every box, 0 < s < 4: s d log lambda/ds = <N>_w - s<R>_w - s<V_1> <= (-log lambda)/log(4/s)) | PROVED GIVEN Lemmas J, C; the branch form GIVEN (RK) |
| Proposition EL (no spatial plaquettes: (LEV_K) for all levels and boxes, K = (1 + s^2/6)/(s (log(4/s) - s^2/8)), s <= 2) | PROVED GIVEN Lemmas J, C |
| Corollary U' (with the vacuum: an extra s abs(B)(9 + 12/log(4/s))) | PROVED GIVEN Theorem U |
| Theorem B1 ((LEV_K), (VIR_K) for every box and s < 4 with K_B = 1/(s log(4/s)) + abs(B)(9 + 12/log(4/s))/m; the bound of Way 2, now proved) | PROVED GIVEN Corollary U', (RK), Lemma 4.1 of `gap-mid-max.md` |
| Theorem B (b >= 8, s <= min(10^(-6), 1/(10 b^3)): (LEV_K) for all levels and (VIR_K) for all real t >= 4 with K = 2/(s log(1/s)); for s <= 10^(-6): K = (1 + 10 s b^3)/(s log(1/s))) | PROVED GIVEN Theorem B1 and `gap-seed-sc.md` Theorem 4 |
| Proposition SUF ((H1), (H2) give (VIR_K) at the integer times of the row) | PROVED GIVEN Corollary U', Theorem B, the periodic form of Theorem SC (ii) |
| (BAND-sc) | OPEN; the one exact statement left |
| The row's target for s b^3 > 1/10 | OPEN |
| The term-by-term polymer route (Section 6) | sketch; range s <= R (R/4)^(4t)/t; breaks at the Cauchy remainder |
| Section 5 (one-plaquette run), Section 8 (direction) | GUIDE |

**Outcome letters of the row.** (A) no. (B) yes: the restriction is s b^3 <= 1/10 (and b >= 8, s <= 10^(-6)); the first term that breaks is the vacuum term of Corollary U'. Inside the range the integral of K from beta_0 to beta_1 is 2 log(log(1/beta_0)/log(1/beta_1)); Corollary TR1 then reaches only beta_1 <= 1/(10 b^3) <= 6 x 10^(-9) (b >= 256), far inside the range of Theorem DOB (beta < 1/18): nothing new. (C) no counterexample; the proved rate grows like 10 s b^3 against an allowance of log b, and that growth is a defect of the proof, not a property found in the model. (D) (BAND-sc).

**Not done, not verified.** No second model read this file. (RK) and Schur orthogonality are not rebuilt in `library/`. Cubes of side 4 to 7 are not covered by Theorem B. (VIR_K) at non-integer times is proved only where (LEV_K) is proved (Theorems B1, B), not in Proposition SUF. The normal-family step of Section 6 is not written. The run of Section 5 is a guide; its first pass failed by round-off and was repeated at 700 digits. No literature was read; the names Schor, O'Carroll, Braga, Michael, Rothe, Karsch, Kato are from memory or from row 711. `origin/main` and the PR branches are not fetched in this checkout and were searched through two digests only. Nothing was committed or pushed; the only repository file written is this one.

**For the lead.**
1. Check item: Theorem U and Lemma C line by line (the first-order formula, the log-sum step, the trace argument that C_s vanishes off the H_n), Lemma J (c), (e), (f), and the arithmetic of Theorem B and Proposition SUF.
2. If C-A is kept: the proof item is (BAND-sc), by an expansion of the one-plaquette band on the periodic cube; ask row 711 for the source pages on the strong-coupling glueball mass first.
3. `gap-mid-max.md` 4.4 Way 2 can cite Theorem B1 for its bound (I did not edit that file).

RESULT: (VIR_K) and (LEV_K) with K = 2/(s log(1/s)) are proved on cubes b >= 8 only for s <= min(10^(-6), 1/(10 b^3)) (all levels, all real t >= 4), together with an exact inequality for every single level at every s < 4 (Theorem U) and a box-dependent rate K_B (Theorem B1); the row's uniform target is neither proved nor refuted, the term that breaks is the vacuum's action per slab (order s b^3), and what stays open is (BAND-sc): bounded change of electric number and spatial action for the lowest band, uniformly in the cube.
