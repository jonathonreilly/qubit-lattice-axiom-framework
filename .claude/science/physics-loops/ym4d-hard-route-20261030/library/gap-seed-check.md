lead: anthropic/claude-opus-5-5/high mac-mini-worker
lease_until: 2026-11-11T21:12Z

# Check of `library/gap-crux-restate.md` (row 698, `gap-seed-check`)

Provenance: Claude Opus 5.5, effort high, Mac mini worker 2, at commit 547801e01. A check by hand, line by line; not an audit. I did not write any part of the text checked. Same provider as the author (Anthropic), different model; this is not an independent check in the sense of a different provider (row 699 is the second check).

## Status block (kept current)

- Started 2026-11-11T09:12Z. Read: FINISH row 698, `library/gap-crux-restate.md` in full.
- Read also: `library/gap-transfer.md` (notation, A, Sections 1-5, 9, 10), `library/gap-transfer-check.md` (verdicts, R1-R8, correction table), `library/gap-skeleton-max-b.md` lines 241-282 (run 2, Lemmas 1, 1', 2).
- Points done: (1)-(12), verdict table, inputs, not covered. **Check complete** (2026-11-11).

## Repo search

Before checking I searched for an owner of the statements checked here: `grep -n` in `library/open-core.md` and in FINISH.md for `Theorem S`, `gap-seed`, `Lemma K`, `SEED`, `TUBE`. Hits: only FINISH rows 697 (the author row), 698 (this row), 699 (`gap-seed-check-astra`, the second check by another provider) and the proof items listed at the end of `gap-crux-restate.md`. `open-core.md` has no hit. No other row checks this text. I attack no open lemma (the row forbids proving the seed); every new statement below is a lemma used inside the check.

## Point (1). The inputs (TM), (TM-c) for boxes with unequal sides

**What the text needs.** For every 4-torus n = (n_1, ..., n_4), all n_mu >= 3, and every direction mu: a positive trace-class T on a Hilbert space with Z(n) = Tr T^(n_mu), simple top eigenvalue with a strictly positive eigenfunction; for nu != mu a unitary involution C_nu commuting with T, mapping positive functions to positive functions, with Tr(T^(n_mu) C_nu) = Z^(mu nu)(n) > 0, and Z^(mu nu) symmetric in mu, nu; and Z(n) invariant under permutations of the four sides. Used for the boxes (2n)^3, (4n, 2n, 2n), (4n, 4n, 2n), (4n)^3, (n, 2n, 2n) and (b, c, d) of Lemma K, in every direction.

**Places of `gap-transfer.md` that use the equal side N.** I went through every occurrence of N, N^3 and N >= 3 (lines 38-48, 118, 125, 131, 147-148, 164, 169-171, 175, 183-184, 189, 192-194, 260). None uses that the three sides are equal. They are of three kinds.

1. Counts: N.3 (|V| = N^3, |E| = 3N^3), N.4 (3N^3 spatial plaquettes, 0 <= V <= 6 beta N^3), 1.1 (3N^3 T time-like plaquettes), 2.2 (|I| = 12 N^3, sum of |iota_i|^2 = 2|E|). With Lambda = Z/N_1 x Z/N_2 x Z/N_3 each N^3 becomes |Lambda| = N_1 N_2 N_3; the arguments are word for word the same.
2. Constants that carry these counts: N.7 (K_0 >= e^(-6 beta N^3)), N.8 (kappa_- = e^(-12 beta N^3)), 1.4, (1a), (4a)-(4c), (5b), 5.2. They become e^(-6 beta |Lambda|), e^(-12 beta |Lambda|), and (5b) becomes m >= -log(1 - e^(-24 beta |Lambda|)). Only the size of these constants changes; Theorem S uses none of them.
3. Distinctness of links, where a side of at least 2 is needed in one direction: N.4 (the four links of a spatial plaquette in the plane (i,j) are distinct when N_i, N_j >= 2), 5.5 (the four links of p_* are distinct; needs N_1, N_2 >= 2), 5.7 (the configuration with u_(0,1) = -1 gives W = -2; needs (0,1) != (e_2,1), i.e. N_2 >= 2), 9.3 (the two links of direction k in a plaquette of the plane (k,j) are distinct; needs N_j >= 2). All hold for sides >= 3. The time-like plaquettes of 1.1 are distinct for T >= 2, independent of the spatial sides.

No step uses a rotation of the spatial cube, an exchange of spatial axes, or N_i = N_j. The tool of Section A is stated for any compact metric space. So the extension holds.

**Lemma 1.1 (transfer operator on every box; checker's statement, proved from `gap-transfer.md` with R1-R8).** Let N_1, N_2, N_3 >= 3, Lambda = Z/N_1 x Z/N_2 x Z/N_3, beta > 0, and let T_P be the operator of Section 1 of `gap-transfer.md` built on Lambda. Then: (i) T_P is positive and trace class on H = L^2(SU(2)^E); (ii) for every k >= 2, Z(N_1, N_2, N_3 | time k) = Tr T_P^k, where Z is the Wilson SU(2) partition function of the 4-torus Lambda x Z/k with normalized Haar measure; (iii) the top eigenvalue lambda_0 = ||T_P|| is simple, with an eigenfunction that is continuous, gauge invariant and >= e^(-12 beta |Lambda|) everywhere; (iv) for k in {1,2,3}, C_k f = f o Z_k (Z_k flips the sign of every link (x,k) with x_k = 0) is a unitary involution, maps a.e.-positive functions to a.e.-positive functions, commutes with T_P, and for every time extent t >= 2

Tr(T_P^t C_k) = Z^(0k)(N | t) := integral over all links of exp(-S'(U)),

where S' is the Wilson action with the plaquette weight exp(-beta(1 - (1/2) tr U_P)) replaced by exp(-beta(1 + (1/2) tr U_P)) on the stack of time-like plaquettes in the plane (0,k) based at (x, t-1) with x_k = 0 (one plaquette for each value of the two other spatial coordinates). (v) Z and Z^(mu nu) are invariant under the permutations of the four axes (with the plane {mu, nu} carried along), and Z^(mu nu) does not depend on where the stack sits; in particular Tr(T_mu^(n_mu) C_nu) = Z^(mu nu)(n) = Tr(T_nu^(n_nu) C_mu).

Proof. (i)-(iii): Sections 1-4 of `gap-transfer.md` with N^3 replaced by |Lambda| (list above): statements (1b), (2c), (3), (4b), (4c). (iv): 9.3 gives V o Z_k = V, K_0(Z_k u, Z_k v) = K_0(u, v), Z_k(h.u) = h.(Z_k u) and preservation of du; hence C_k commutes with M, C_E, P and T_P, and C_k^2 = 1, C_k^* = C_k^(-1) = C_k. Positivity of f o Z_k is clear. For the trace: T_P C_k is the integral operator with kernel A_T(u, Z_k w) (substitute w = Z_k v), a bounded continuous kernel; T_P^(t-1) has kernel A^(t-1) (the (t-1)-fold composition); by A0(e) Tr(T_P^(t-1) T_P C_k) is the integral of A^(t-1)(u, w) A_T(w, Z_k u) over u, w. Write each A_T as the integral over the time-like links (1.3): the result is the integral of prod over t of T_0(U(t), g_t . U(t+1)) with U(t) := Z_k U(0) in the last factor. In that last factor the time-like plaquette in the plane (0,k) based at (x, t-1) has holonomy g(x) (Z_k U(0))_(x,k) g(x+e_k)^(-1) U(t-1)_(x,k)^(-1), which is minus the untwisted holonomy exactly when x_k = 0; all other plaquettes are unchanged (the spatial potential V of slice 0 is Z_k-invariant, and the time-like plaquettes in planes (0,j), j != k, contain no link (x,k)). This is Z^(0k). (v) Exchange of axes: for a permutation sigma of {1,...,4} the map x -> sigma x of the tori and U'_(sigma x, sigma i) := U_(x,i) is a bijection of links that preserves product Haar measure and sends the plaquette at x in the plane (i,j) to the plaquette at sigma x in the plane (sigma i, sigma j), traversed either in its standard order or in the reverse order; tr U^(-1) = tr U (N.2), so the action, and the stack's twisted weight, are preserved. Position of the stack: multiplying by -1 the links (y, mu) with y_mu = a, y_nu = b (a measure-preserving change of variables) flips the sign of tr U_P exactly on the plaquettes of the plane (mu,nu) based at y_mu = a, y_nu in {b-1, b} (a plaquette in a plane (mu, rho), rho != nu, contains two such links or none); so the stack at nu-position b-1 and the one at b give the same integral; the same with the roles of mu and nu exchanged. So Z^(mu nu) depends on the unordered plane only, and the stack built by C_nu in the transfer in direction mu and the one built by C_mu in direction nu give the same number. QED

**Correction to the wording of (TM-c) (line 35 of the text).** "the sign of beta changed on one stack" must read "the weight exp(-beta(1 - (1/2) tr U_p)) replaced by exp(-beta(1 + (1/2) tr U_p)) on one stack" (equivalently U_p -> -U_p there). With the normalized action A(U) of line 31, a literal change beta -> -beta gives exp(+beta(1 - (1/2) tr U_p)) = e^(2 beta) exp(-beta(1 + (1/2) tr U_p)), i.e. the twisted partition function times e^(2 beta n_rho n_sigma); that number can exceed Z (at beta -> infinity), and then Z_odd = (Z - Z^(12))/2 would be negative, against Theorem F (a). Every proof in the text uses Z^(mu nu) only through Tr(T^k C_nu), which is the corrected object. With the correction, 0 < Z^(mu nu) <= Z: Tr(T^k C) = sum of lambda_i^k c_i with c_i = +-1 in a joint eigenbasis (C commutes with the compact T, so each eigenspace of T is C-invariant and splits into +-1 parts; A2(iv)).

**Verdict (1): HOLDS AFTER CORRECTION.** The construction gives, for every periodic box with three sides >= 3, everything the text asks for: Lemma 1.1. The only correction is the wording of the twisted weight in (TM-c); no statement of the text loses its proof. Two remarks for the record. (a) Lemma K and Lemma E use W(a, b) = Tr T_b^a only for a, b >= 3 as a partition function; Lemma A is applied to the operators T_b and T_b^k for all k >= 1, which needs only that T_b is positive trace class. (b) The traces in (TM) are over H = L^2(SU(2)^E) with T_P = 0 on the non-invariant part; the eigenvalue list lambda_0 > lambda_1 >= ... of the text is the list of positive eigenvalues of T_P with multiplicity (A2), so S(k; B) = sum over i >= 1 of r_i^k counts every positive eigenvalue but the top one with its multiplicity, and zero eigenvalues do not contribute.

## Point (2). Lemma A and every use of it

**Lemma A (a).** Let S >= 0 be trace class, S != 0, eigenvalues lambda_0 >= lambda_1 >= ... > 0 with multiplicity (A2 of `gap-transfer.md`), so Tr S^k = sum of lambda_i^k for k >= 1 (A2 (iv) applied to S^k, which has the same eigenvectors and the eigenvalues lambda_i^k). Since lambda_0^k <= Tr S^k, lambda_0 <= (Tr S^k)^(1/k), so Tr S^(k+1) = sum lambda_i lambda_i^k <= lambda_0 Tr S^k <= (Tr S^k)^(1 + 1/k), which is (Tr S^(k+1))^(1/(k+1)) <= (Tr S^k)^(1/k). Limit: lambda_0^k <= Tr S^k <= lambda_0^(k-1) Tr S, so lambda_0 <= (Tr S^k)^(1/k) <= lambda_0^(1-1/k) (Tr S)^(1/k) -> lambda_0. Monotonicity from k to jk gives Tr S^(jk) <= (Tr S^k)^j. **Holds.**

**Lemma A (b).** Tr S^(2k) = sum lambda_i^k lambda_i^k <= lambda_0^k Tr S^k. **Holds.**

**The consequences of Section 1 (lines 39-45).**
- F(n)/|n| non-increasing in each side: (Tr T^(n_mu))^(1/n_mu) non-increasing in n_mu by (a), for n_mu >= 3 where Z is defined; divide log by the product of the other three sides. **Holds.**
- f finite: there are 6|n| plaquettes, each with 0 <= 1 - (1/2) tr U_p <= 2, so e^(-12 beta |n|) <= Z(n) <= 1 and -12 beta <= f <= 0. **Holds.**
- (LB) Z(n) >= exp(f |n|): the definition of f as an infimum. **Holds** (trivially).
- Delta(..., j n_mu, ...) <= j Delta(n): Z(..., j n_mu, ...) = Tr T^(j n_mu) <= (Tr T^(n_mu))^j by (a), and f |n| is multiplied by j. **Holds.**
- r_1^k <= S(k; B): the term i = 1 of the sum (if lambda_1 does not exist, S = 0 and m = +infinity). S(k + k'; B) <= S(k; B) S(k'; B): sum over i >= 1 of r_i^(k+k') <= r_1^(k') S(k) <= S(k') S(k). Both use that lambda_1 is counted in S with weight at least one: a trace. **Holds.**

**Uses of Lemma A in the text, each checked.** Theorem D (a) (a with j = 2), (b) (b, and a three times), (e) (via S(2n) <= S(n)^2); Proposition R (via run 2, Lemma 1 (d), whose proof uses (a)); Lemma K (a), (b); Lemma E (a with j = 2, for the operator T_a, i.e. W(a, 2b) = Tr T_a^(2b) <= (Tr T_a^b)^2); Theorem F (b) (a for T_1 P_2), (e) (the limit in (a)); Proposition T (via "doubling one side at most doubles Delta"). In each use the operator is the transfer operator of Lemma 1.1 of a box with sides >= 3, or T P with P a spectral projection commuting with T (checked in point (10)). **Verdict (2): HOLDS.**

## Point (3). Theorem D (a)-(f) and Corollary D2

Setting: T = transfer operator in direction 1 of B_2 = (2n, 2n, 2n), n >= 3, so Tr T^k = Z(k, 2n, 2n, 2n) for k >= 3 (Lemma 1.1).

**(a).** Z((2n)^4) <= Z(n, 2n, 2n, 2n)^2 <= Z(n, n, 2n, 2n)^4 <= Z(n, n, n, 2n)^8 <= Z(n^4)^16, each step Lemma A (a) with j = 2 in one direction, with the operator of the box formed by the other three sides (Lemma 1.1, all sides >= 3). **Holds.**

**(b) (weight).** Z_1 := Z(n, 2n, 2n, 2n) = Tr T^n and Z((2n)^4) = Tr T^(2n). Lemma A (b): lambda_0^n >= Z((2n)^4)/Z_1 (this is the lower bound on the top eigenvalue). Then 1 + S(n; B_2) = Tr T^n / lambda_0^n <= Z_1 Z_1 / Z((2n)^4). The chain Z_1 <= Z(n^4)^8 is the last three steps of (a) (directions 2, 3, 4, each by Lemma A (a) with j = 2 for the transfer operator in that direction of the box formed by the other three sides; e.g. Z(n, 2n, 2n, 2n) <= Z(n, n, 2n, 2n)^2 uses the operator in direction 2 of the box (n, 2n, 2n), sides >= 3). So 1 + S(n; B_2) <= Z(n^4)^16 / Z((2n)^4) = exp(Phi(n)). I checked the powers: 8 + 8 = 16, and the 16 of Phi. **Holds.**

**(c).** r_1^n <= S(n; B_2) <= e^Phi - 1 and r_1 = e^(-m(B_2)). The bound m >= (1/n) log(1/(e^Phi - 1)) holds always (it is vacuous when e^Phi - 1 >= 1); the condition Phi < log 2 only makes it positive. Read backwards: Phi >= log(1 + e^(-n m)). **Holds.**

**(d).** Each i >= 1 with log(lambda_0/lambda_i) <= E has r_i^n >= e^(-nE); so N(E) e^(-nE) <= S(n; B_2) <= e^Phi - 1. **Holds.**

**(e) (weight).** Fix nu in {2, 3, 4} and the torus (2n)^4 = (time 2n) x B_2. Z_odd := (Z - Z^(1 nu))/2 = Tr(T^(2n) (1 - C_nu)/2) by Lemma 1.1 (iv) with the corrected twisted weight (point (1)). C_nu commutes with T, so C_nu Omega is a unit eigenvector of lambda_0, hence C_nu Omega = c Omega with |c| = 1 (simplicity), and c = 1 because Omega > 0 and C_nu Omega = Omega o Z_nu > 0. So Omega is even. Every eigenspace of T for a positive eigenvalue is finite-dimensional and C_nu-invariant, so the orthonormal eigenvectors phi_i of A2 can be chosen as eigenvectors of C_nu, with phi_0 = Omega. Put P = (1 - C_nu)/2, an orthogonal projection commuting with T. Then Tr(T^(2n) P) = Tr(P T^(2n) P) = sum over i of lambda_i^(2n) ||P phi_i||^2 (the computation of A2.7 for the positive trace-class P T^(2n) P, whose range lies in the closed span of the phi_i; T = 0 on its complement), and ||P phi_i||^2 is 0 or 1, and 0 for i = 0. So Z_odd <= sum over i >= 1 of lambda_i^(2n) = lambda_0^(2n) S(2n; B_2). Also Z = Tr T^(2n) >= lambda_0^(2n). So u = Z_odd/Z <= S(2n; B_2) <= S(n; B_2)^2 <= (e^Phi - 1)^2, and 1 - Z^(1 nu)/Z = 2u. The other planes (mu, nu): by Lemma 1.1 (v) the axis permutation that sends {mu, nu} to {1, nu'} leaves the torus (2n)^4 and B_2 fixed. **Holds.** The step "the top eigenvector is even under the centre flips" is correct and needs exactly simplicity, positivity of Omega and positivity of C_nu.

**(f).** dF/dbeta = -<A> = -sum over the 6|n| plaquettes of <1 - (1/2) tr U_p>; differentiation under the integral is allowed (the integrand is smooth in beta, bounded with bounded derivative on a compact space). On n^4 every plaquette has the same expectation (translations and axis permutations act transitively on the plaquettes of a symmetric torus and preserve the measure), so this is -6|n| abar_n. F(n; 0) = log 1 = 0. d Phi/d beta = 16(-6 n^4 abar_n) - (-6 (2n)^4 abar_2n) = 96 n^4 (abar_2n - abar_n). Integrate from 0. **Holds.**

**Corollary D2 (i).** e^x - 1 <= 2x on [0, 1] (the convex function e^x - 1 - 2x is 0 at 0 and e - 3 < 0 at 1). With Phi <= C e^(-cn) <= 1 and (c): m((2n)^3) >= (1/n) log(1/(2 Phi)) >= (1/n)(cn - log(2C)). **Holds.**

**Corollary D2 (ii).** Assume (Phi-step) with K >= 2, eps_0 <= 1/2, and Phi_0 = Phi(n_1) < min(eps_0, 1/K), n_1 >= n_0. Induction hypothesis: Phi_k <= Phi_0 and K Phi_k <= (K Phi_0)^(2^k). Since 2^k n_1 >= n_0 and Phi_k <= Phi_0 < eps_0, the step applies: K Phi_(k+1) <= (K Phi_k)^2 <= (K Phi_0)^(2^(k+1)), and Phi_(k+1) <= (K Phi_k) Phi_k <= (K Phi_0) Phi_k < Phi_k. Then (c) at time 2^k n_1 for the box (2^(k+1) n_1)^3, with Phi_k <= 1/2 and e^x - 1 <= 2x: m >= (1/(2^k n_1)) log(1/(2 Phi_k)) and log(1/(2 Phi_k)) = log(K/2) + log(1/(K Phi_k)) >= log(K/2) + 2^k log(1/(K Phi_0)) >= 2^k log(1/(K Phi_0)) (K >= 2). **Holds** as an implication; (Phi-step) is not proved, and the text says it is no longer needed (Theorem S replaces it).

**Verdict (3): HOLDS** (with the corrected reading of Z^(mu nu) from point (1), used in (e)).

## Point (4). Proposition R

**Statement.** Delta(n^4) <= eps and 8^k eps <= 1 give m((2^k n)^3) >= (1/n) log(1/(2 8^k eps)).

**Check.** Multiplying one side by 2^k multiplies Delta by at most 2^k (point (2)); three sides give Delta(n, 2^k n, 2^k n, 2^k n) <= 8^k eps. Run 2, Lemma 1 (d) (checked: log lambda_0 = lim over n_1 of F/n_1 = n_2 n_3 n_4 lim f >= n_2 n_3 n_4 f, so Z = lambda_0^(n_1)(1 + S(n_1)) >= exp(f |n|)(1 + S(n_1)), i.e. 1 + S(n_1) <= exp(Delta)) gives 1 + S(n; (2^k n)^3) <= exp(8^k eps). With e^x - 1 <= 2x on [0, 1] and r_1^n <= S: the claim. **Holds.**

The identity Delta(n^4) = sum over k >= 0 of 16^(-(k+1)) Phi(2^k n): Phi(n) = 16 Delta(n^4) - Delta((2n)^4) (the f terms cancel, 16 n^4 = (2n)^4), so Delta(n^4) = sum over k < K of 16^(-(k+1)) Phi(2^k n) + 16^(-K) Delta((2^K n)^4), and 16^(-K) Delta((2^K n)^4) = n^4 (F((2^K n)^4)/(2^K n)^4 - f) -> 0 because F/|n| is non-increasing in each side, so its infimum over all tori equals its limit along the cubes. **Holds.**

**Wording correction (line 123).** "the gap of every box of side up to n exp(mu n / 3)" must read "the gap of every cube of side 2^k n <= n exp(mu n/3)" (the proof covers dyadic multiples; any integer multiple j n with j^3 eps <= 1 works the same way, other sides do not). The rate mu - (3k log 2 + log 2)/n is right for side 2^k n.

**Verdict (4): HOLDS** (wording correction above).

## Point (5). Lemma K (a)-(d)

Setting of the lemmas (line 174), as used: W(a, b) = Z(a, b, c, d), c, d >= 3 fixed, a, b >= 3; T_b = transfer operator in direction 1 of the box (b, c, d) (Lemma 1.1), W(a, b) = Tr T_b^a; symmetry W(a, b) = W(b, a) is Lemma 1.1 (v) (exchange of the axes 1, 2). ell = inf over a, b of log W(a, b)/(ab) >= -12 beta c d is finite. Note: ell depends on (c, d); it is not the four-dimensional f times cd. The lemmas never compare it with f, so this is consistent; I flag it only because Section 1 and Section 3.4 use the word deficit for both Delta and kappa.

**(a).** By Lemma A (a) for T_b, a -> (1/a) log W(a, b) is non-increasing on a >= 3 and tends to e(b). A non-increasing sequence tends to its infimum. **Holds.**

**(b).** W(a, jb) = W(jb, a) = Tr T_a^(jb) <= (Tr T_a^b)^j = W(b, a)^j = W(a, b)^j (symmetry twice, Lemma A (a) for T_a). Divide by a, let a -> infinity, use (a): e(jb) <= j e(b). e(b)/b = inf over a of log W(a, b)/(ab) by (a), so inf over b of e(b)/b = ell, and kappa(b) = b(e(b)/b - ell) >= 0. **Holds.**

**(c) (weight: convexity from the crossed direction, and passage to the limit).** Fix a. h_a(b) := (1/a) log W(a, b) = (1/a) log Tr T_a^b (symmetry, then the transfer operator T_a of the box (a, c, d) in direction 2). With the eigenvalues mu_j of T_a (multiplicity): Tr T_a^b = sum of mu_j^b, and Cauchy-Schwarz on the sequence (mu_j^((b-1)/2) mu_j^((b+1)/2)) gives (Tr T_a^b)^2 <= Tr T_a^(b-1) Tr T_a^(b+1). So h_a(b+1) + h_a(b-1) - 2 h_a(b) >= 0 for every integer b >= 4 (so that b - 1 >= 3 and W(a, b-1) is a partition function; as operator traces it holds for b >= 2). By (a), h_a(b) -> e(b) as a -> infinity, for each fixed b. The inequality is a non-strict inequality between three numbers that each converge; it passes to the limit: e(b+1) + e(b-1) - 2 e(b) = lim over a of (h_a(b+1) + h_a(b-1) - 2 h_a(b)) >= 0. Subtracting the linear ell b does not change second differences. **Holds** on the integers b >= 4, which is all that (d) uses. (The text's phrase "a sum of exponentials of b with positive weights" is right: the weights are the multiplicities, and the sum may be infinite; the Cauchy-Schwarz form above covers the infinite case.)

**(d) (weight: from convexity and the infimum to a non-increasing deficit).** Suppose kappa(b_0 + 1) - kappa(b_0) = c > 0 for some b_0 >= 3. By (c), for every j >= b_0 + 1 (so j >= 4), kappa(j + 1) - kappa(j) >= kappa(j) - kappa(j - 1); by induction every increment from b_0 on is >= c. So kappa(b) >= kappa(b_0) + c(b - b_0) >= c(b - b_0) for b >= b_0 (kappa(b_0) >= 0 by (b)), and for b >= 2 b_0: e(b)/b = ell + kappa(b)/b >= ell + c/2. Since ell = inf over b of e(b)/b, there is b_1 >= 3 with e(b_1)/b_1 < ell + c/2. By (b), e(j b_1)/(j b_1) <= e(b_1)/b_1 < ell + c/2 for every j >= 1; take j with j b_1 >= 2 b_0. Contradiction. So kappa(b + 1) <= kappa(b) for every b >= 3. **Holds.** Every step is explicit; the only inputs are (b) (subadditivity along multiples) and (c) (convexity at the integers >= 4).

A consistency check by hand (not a proof step): for a free massless field in two dimensions the ground state energy of a circle of length b is eps b - pi c/(6b) + o(1/b), so kappa(b) = pi c/(6b) + o(1/b): non-negative, convex, decreasing, as (b)-(d) require.

**Verdict (5): HOLDS.**

## Point (6). Lemma X and Lemma E

**Lemma X.** W(a, b) = lambda(b)^a (1 + S(a; b)) is the definition of S(a; b) (line 174), and W(b, a) = lambda(a)^b (1 + S(b; a)); W(a, b) = W(b, a). Logarithms: a e(b) + g(a, b) = b e(a) + g(b, a); subtract ell a b from both sides: a kappa(b) + g(a, b) = b kappa(a) + g(b, a). For a < b: g(b, a) >= 0 and kappa(a) >= kappa(b) (Lemma K (d)), so a kappa(b) + g(a, b) >= b kappa(b), i.e. (b - a) kappa(b) <= g(a, b). **Holds.**

**Lemma E.** For a < b: W(a, 2b) = W(2b, a) = Tr T_a^(2b) <= (Tr T_a^b)^2 = W(a, b)^2 (Lemma A (a), j = 2). Write both sides with the definition of S: lambda(2b)^a (1 + S(a; 2b)) <= lambda(b)^(2a) (1 + S(a; b))^2, so 1 + S(a; 2b) <= (1 + S(a; b))^2 exp(a(2 e(b) - e(2b))). And 2 e(b) - e(2b) = 2 kappa(b) - kappa(2b) (the ell terms: 2 ell b - ell 2b = 0) <= 2 kappa(b) (kappa(2b) >= 0). By Lemma X, kappa(b) <= g(a, b)/(b - a). So 1 + S(a; 2b) <= (1 + S(a; b))^2 exp(2a g(a, b)/(b - a)) = (1 + S(a; b))^(2 + 2a/(b - a)), and 2 + 2a/(b - a) = 2b/(b - a). For a = b/2: 2b/(b/2) = 4. **Holds.**

The same proof with W(a, jb) <= W(a, b)^j gives 1 + S(a; jb) <= (1 + S(a; b))^(jb/(b-a)) (used in Section 3.4, first bullet of "What Theorem S is and is not"; checked in point (7)).

**Verdict (6): HOLDS.**

## Point (7). Theorem S

Notation: for a box B = (b_1, b_2, b_3) and k >= 1, S(k; B) is the thermal sum of the transfer operator in direction 1 of the 4-torus (time | B), i.e. of the operator T_B of Lemma 1.1 on the box B: S(k; B) = sum over i >= 1 of (lambda_i/lambda_0)^k, the list of positive eigenvalues with multiplicity (A2), lambda_0 simple. So 1 + S(k; B) = Tr T_B^k / lambda_0^k, and s = S(n; (2n)^3).

**The three uses of Lemma E, with the fixed sides.**

1. Pair (1, 2); sides of directions 3, 4 fixed at (2n, 2n). W(x, y) := Z(x, y, 2n, 2n), T_y = transfer in direction 1 of the box (y, 2n, 2n), W(x, y) = W(y, x) by exchange of the axes 1, 2. Then S(x; y) of the lemma is S(x; (y, 2n, 2n)). Lemma E with a = n, b = 2n (a < b, a = b/2): 1 + S(n; (4n, 2n, 2n)) <= (1 + S(n; (2n, 2n, 2n)))^4 = (1 + s)^4. Correct.
2. Pair (1, 3); sides of directions 2, 4 fixed at (4n, 2n). W(x, y) := Z(x, 4n, y, 2n), T_y = transfer in direction 1 of (4n, y, 2n), symmetry by exchange of the axes 1, 3. Lemma E, a = n, b = 2n: 1 + S(n; (4n, 4n, 2n)) <= (1 + S(n; (4n, 2n, 2n)))^4 <= (1 + s)^16. Correct.
3. Pair (1, 4); sides of directions 2, 3 fixed at (4n, 4n). W(x, y) := Z(x, 4n, 4n, y), T_y = transfer in direction 1 of (4n, 4n, y), symmetry by exchange of the axes 1, 4. Lemma E: 1 + S(n; (4n)^3) <= (1 + S(n; (4n, 4n, 2n)))^4 <= (1 + s)^64. Correct.

Each use has its own ell and kappa (they depend on the fixed sides); each use is self-contained, so nothing is mixed. Each needs Lemma 1.1 for boxes with unequal sides (point (1)): (y, 2n, 2n), (4n, y, 2n), (4n, 4n, y) for all y >= 3 (Lemma K takes limits over y), and the transposed boxes (x, 2n, 2n) etc. for T_a. All sides >= 3 since n >= 3.

**The step S(2n; B) <= S(n; B)^2 for B = (4n)^3.** This is S(k + k') <= S(k) S(k') with k = k' = n (point (2)): sum over i >= 1 of r_i^(2n) <= r_1^n S(n) and r_1^n <= S(n). S is the sum over all excited eigenvalues counted with multiplicity, including all flux sectors; the top eigenvalue is simple (Lemma 1.1 (iii)), so r_1 < 1 and the eigenvalue lambda_0 is not part of S. (If lambda_0 were degenerate, S(n; B) >= 1 and the induction hypothesis s_k < 1/5041 could not hold; simplicity is therefore also forced by the conclusion, but it is proved anyway.) Hence S(2n; (4n)^3) <= S(n; (4n)^3)^2 <= ((1 + s)^64 - 1)^2. **Holds.**

**Constants.**
- For 0 <= x <= 1/640: (1 + x)^64 <= e^(64x) (since 1 + x <= e^x); e^y - 1 <= y e^y for y >= 0 (mean value theorem); with y = 64 x <= 0.1: (1 + x)^64 - 1 <= 64 x e^(0.1). e^(0.1) = 1.10517... (series: 1 + 0.1 + 0.005 + 0.000167 + 0.000004 = 1.105171), and 64 x 1.105171 = 70.731 <= 71. So (1 + x)^64 - 1 <= 71 x and the map is <= (71 x)^2 = 5041 x^2 (71^2 = 5041). Correct.
- 1/5041 = 1.98373 x 10^(-4) < 1/640 = 1.5625 x 10^(-3). Correct.
- exp(1.9 x 10^(-4)) - 1 = 1.9 x 10^(-4) + 1.805 x 10^(-8) + ... < 1.901 x 10^(-4) < 1.91 x 10^(-4) < 1.9837 x 10^(-4) = 1/5041. Correct.
- Part 1 (line 60) claims gap >= 0.04/n under Phi(n) <= 1.9 x 10^(-4): 5041 x 1.9002 x 10^(-4) = 0.95789, log(1/0.95789) = 0.04302 >= 0.04. Correct.
- Corollary S3's bullet (line 213): 1 + S(n_k; (2 j n_k)^3) <= (1 + s_k)^(8 j^3) by the generalized Lemma E (exponent jb/(b-a) = 2j in each of three directions, (2j)^3 = 8 j^3). With y = 8 j^3 s_k and 14 j^3 s_k < 1: y < 4/7, and (e^y - 1)/y is increasing, equal to 1.349 at y = 4/7 (e^(4/7) = 1.7708), so (1 + s_k)^(8j^3) - 1 <= 1.349 y < 14 j^3 s_k. So m >= (1/n_k) log(1/(14 j^3 s_k)). Correct. (The crude bound y e^y used for 71 would give 14.2 here; the claim is still true by the sharper bound.)
- Line 214: s >= 1/5041 for every n gives Phi(n) >= log(1 + 1/5041) = 1.98353 x 10^(-4) >= 1.98 x 10^(-4) (by Theorem D (b)). Correct.

**Induction.** Put s_k = S(n_k; (2 n_k)^3), n_k = 2^k n; s_0 = s, and the step above with n_k in place of n (n_k >= 3) gives s_(k+1) <= ((1 + s_k)^64 - 1)^2. Hypothesis: 5041 s_k <= (5041 s)^(2^k) < 1. Then s_k < 1/5041 <= 1/640, so s_(k+1) <= 5041 s_k^2 and 5041 s_(k+1) <= (5041 s_k)^2 <= (5041 s)^(2^(k+1)). Correct.

**Gap bound.** r_1^(n_k) <= s_k (r_1 for the box (2 n_k)^3), so m((2 n_k)^3) >= (1/n_k) log(1/s_k), and log(1/s_k) >= log 5041 + 2^k log(1/(5041 s)), so m >= log(1/(5041 s))/n + (log 5041)/n_k >= log(1/(5041 s))/n. Correct.

**Last claim.** s <= exp(Phi(n)) - 1 (Theorem D (b), same box (2n)^3, same time n). With Phi(n) <= 1.9 x 10^(-4): s < 1/5041. Correct.

**Verdict (7): HOLDS.** Theorem S is proved from Lemma 1.1 (which supplies (TM) for every box and the symmetry of Z), Lemma A, and the elementary inequalities above. It uses no property of SU(2) beyond Lemma 1.1.

## Point (8). Corollaries S2 and S3

**Corollary S2.** For a symmetric W as in the setting of the lemmas (a two-dimensional model: W(a, b) the partition function of the a x b torus): Lemma E with a = n, b = 2n gives 1 + S(n; 4n) <= (1 + S(n; 2n))^4, and S(2n; 4n) <= S(n; 4n)^2. For x <= 1/20: (1 + x)^4 - 1 = x(4 + 6x + 4x^2 + x^3) <= x(4 + 0.3 + 0.01 + 0.000125) = 4.3101 x <= 4.32 x, and 4.32^2 = 18.66 < 19. Induction: if x_0 = S(n; 2n) <= 1/20 then 19 x_0 <= 0.95 < 1, 19 x_k <= (19 x_0)^(2^k), x_k <= x_0 <= 1/20, and the gap of the circle of length 2^(k+1) n is >= (1/n_k)(2^k log(1/(19 x_0)) + log 19) >= log(1/(19 x_0))/n. **Holds** for every W satisfying the setting (positive trace-class transfer operators in both directions with simple top eigenvalue, symmetry, ell finite).

**Correction (line 205).** "This is a statement for every reflection-positive model on the square lattice with a positive transfer operator, the O(3) sigma model included." The corollary needs a positive trace-class transfer operator with simple top eigenvalue for every circle length >= 3, and W(a, b) = W(b, a). For the O(3) model these are not proved in this repository (Lemma 1.1 is for SU(2) lattice gauge theory). The analogue for the nearest-neighbour O(3) model is very likely true by the same Gram-expansion and Jentzsch argument (the kernel exp(beta sum_x s_x . s'_x) is a positive-definite kernel on (S^2)^b), but that is a remark, not a proved input. Replace by: "This is a statement for every model on the square lattice that satisfies the setting of the lemmas; for the O(3) model that setting is plausible by the argument of `gap-transfer.md` and is not proved here."

**Corollary S3.** For 3 <= a <= b/2: 2b/(b - a) <= 4 iff a <= b/2. The three uses of Lemma E as in point (7) with (a, b) for (n, 2n) and boxes (2b, b, b), (2b, 2b, b), (2b)^3: 1 + S(a; (2b)^3) <= (1 + S(a; b^3))^(e^3) with e = 2b/(b - a) <= 4, so <= (1 + S(a; b^3))^64 (base >= 1). Then S(2a; (2b)^3) <= S(a; (2b)^3)^2. The pair (2a, 2b) again has 2a <= (2b)/2. For L >= 2N there is a unique k >= 0 and b in [2N, 4N) with L = 2^k b; a = floor(b/2) satisfies N <= a <= b/2 (so a >= 3) and a < 2N. The recursion and the gap bound of Theorem S give m(L^3) >= log(1/(5041 s_max))/a >= log(1/(5041 s_max))/(2N) (the logarithm is positive since s_max < 1/5041). **Holds.**

**Verdict (8): S2 HOLDS AFTER CORRECTION (the scope sentence about O(3)); S3 HOLDS.**

## Point (9). Proposition N, Remark N2, Lemma J and the seam bound

**Proposition N.** As a function of n_1 with V = n_2 n_3 n_4: the term mu = 1 of the exponent is V w(n_1) = V c q^(n_1), and the terms mu >= 2 are n_1 (V/n_mu) w(n_mu). So Z_w = Lambda^(n_1) exp(V c q^(n_1)) with log Lambda = f V + sum over mu >= 2 of (V/n_mu) w(n_mu), and exp(V c q^(n_1)) = sum over j >= 0 of ((Vc)^j/j!) (q^j)^(n_1): the integral of lambda^(n_1) against the measure with masses (Vc)^j/j! at Lambda q^j, mass 1 at Lambda. Symmetric in the sides. F/|n| = f + sum over mu of w(n_mu)/n_mu > f, tending to f, so the infimum is f. Delta(n^4) = 4 n^3 c q^n, Phi(n) = 16 Delta(n^4) - Delta((2n)^4) = 64 n^3 c q^n - 32 n^3 c q^(2n). Since 0 < q^(2n) <= q^n: 32 n^3 c q^n <= Phi(n) <= 64 n^3 c q^n. Phi(2n) >= 32 (2n)^3 c q^(2n) = 256 n^3 c q^(2n) and Phi(n)^2 <= 4096 n^6 c^2 q^(2n), so Phi(2n) >= Phi(n)^2/(16 n^3 c). The choice of c: Phi(n) <= 64 n^3 c q^n <= eps and 1/(16 n^3 c) >= K. **Holds.** The claim that Lemma A, (LB) and Theorem D (a), (b) use only (TM') is right: Lemma A (a), (b) hold for integrals of lambda^k against a positive measure with an atom of mass >= 1 at the top (lambda_0^k <= the integral is exactly the atom), and (LB) is the definition of f.

**Remark N2.** As a function of n_1, the factor mu = 1 is (1 - q^(n_1))^(-cV) = sum over j of binom(cV + j - 1, j) q^(j n_1), integer coefficients since cV is a positive integer; the factors mu >= 2 are n_1-th powers. So (TM-int) holds. With x = q^n: Delta(n^4) = -4 n^3 c log(1 - x), and Phi(n) = -64 n^3 c log(1 - x) + 32 n^3 c log(1 - x^2) = 32 n^3 c log((1 + x)/(1 - x)) >= 64 n^3 c x (since log((1+x)/(1-x)) = 2(x + x^3/3 + ...) >= 2x). Phi(2n) = 256 n^3 c log((1 + x^2)/(1 - x^2)) <= 256 n^3 c 2x^2/(1 - x^4) <= 546 n^3 c x^2 when x <= 1/2 (2 x 16/15 x 256 = 546.1). So the text's bounds Phi(n) >= 32 n^3 c q^n and Phi(2n) <= 1024 n^3 c q^(2n) hold (with room), and Phi(2n) <= Phi(n)^2/(n^3 c) <= Phi(n)^2. Several species: Phi(n) >= 64 n^3 sum c_j x_j, Phi(2n) <= 546 n^3 sum c_j x_j^2 <= 546 n^3 (sum c_j x_j)^2 (c_j >= 1 integers), so Phi(2n) <= Phi(n)^2. **Holds.** The sentence "Section 3.4 gives such a proof, for the thermal sums (the form (FIT))" is right: Theorem S gives (FIT) with theta = 1/5041 (point (7)).

**Lemma J.** Convention (h.U)_(xy) = h_x U_(xy) h_y^(-1). Under h, U_01 k_1 U_12 becomes h_0 U_01 (h_1^(-1) k_1 h_1) U_12 h_2^(-1), and likewise k_2 -> h_2^(-1) k_2 h_2 (U_32^(-1) -> h_2 U_32^(-1) h_3^(-1)), k_3 -> h_3^(-1) k_3 h_3, and h_0 cancels in the trace. The corners x_1, x_2, x_3 are distinct (sides >= 2). Invariance of mu and Fubini: the expectation equals its average over independent Haar h_1, h_2, h_3; the expression is linear in each conjugated k_c, and the Haar average of h^(-1) k h commutes with every element of SU(2), hence with all 2 x 2 complex matrices (SU(2) spans them: 1, i sigma_1, i sigma_2, i sigma_3), so it is the scalar (1/2) tr k. **Holds.** Seam case: I checked the geometry of the sixteen blocks (block = links (x, mu) with x in one sub-cube of side n; the link leaving the sub-cube is identified with the wrap-around link of the small torus). A big-torus plaquette at x in the plane (mu, nu) is a seam plaquette iff x_mu or x_nu is n - 1 in local coordinates; then the link (x + e_mu, nu) (or (x + e_nu, mu)) is the only link of the plaquette in its block, and the gauge transformation of that block's small torus at its base vertex multiplies it on the left by g and moves no other link of the plaquette. Independence of the blocks and the Haar average of g, which is 0 (invariance under g -> -g), give expectation 0. **Holds.**

**Seam bound.** The interior plaquettes of the big torus and of the small tori are the same functions; the big torus has N_seam = 96 n^4 (1 - (1 - 1/n)^2) = 192 n^3 - 96 n^2 seam plaquettes and the sixteen small tori have the same number of wrap-around plaquettes. Z((2n)^4)/Z(n^4)^16 is the expectation, under the product of the sixteen Gibbs measures, of exp(-beta(A_big - sum of A_small)) >= exp(-beta times the expectation) (Jensen); in the expectation each seam plaquette contributes E(1 - (1/2) tr U_p) = 1 (Lemma J, seam case) and each wrap-around plaquette of a small torus contributes E(1 - (1/2) tr U_p) = abar_n, so the expectation of A_big - sum of A_small is N_seam (1 - abar_n). Hence Phi(n) <= beta (192 n^3 - 96 n^2)(1 - abar_n). **Holds.** (Line 152 says the replaced small-torus plaquette "has 1 - abar_n"; this is the expectation of (1/2) tr, with abar_n = E(1 - (1/2) tr) as in Theorem D (f). Consistent.)

**Verdict (9): HOLDS.**

## Point (10). Theorem F, Section 4.2, Proposition T, Remark F3, Identity 4.4

**Theorem F.** (a) Lemma 1.1 (iv), (v) with the corrected twisted weight: Tr(T_1^a C_2) = Z^(12) = Tr(T_2^b C_1), so Z_odd = Tr(T_1^a P_2) = Tr(T_2^b P_1) >= 0; Z_even - Z_odd = Z^(12) > 0. Holds. (b) P_2 is an orthogonal projection commuting with T_1, so T_1 P_2 = P_2 T_1 P_2 is positive and trace class (T_1 = X^* X with X Hilbert-Schmidt gives P_2 T_1 P_2 = (X P_2)^*(X P_2)), and (T_1 P_2)^a = T_1^a P_2. Lemma A (a): Z_odd(ja, b | c, d) <= Z_odd(a, b | c, d)^j. On the torus (ja, b | c, d) the same in direction 2 with T_2' (box (ja, c, d)) and P_1', using Z_odd = Tr(T_2'^b P_1') from Lemma 1.1 (v). Holds. (c) f|n| scales by jk; u <= v is (LB). Holds. (d) From (c). Holds. (e) If T_2 P_1 = 0 then v = 0 < 1, excluded; else Z_odd(a, b)^(1/b) = (Tr (T_2 P_1)^b)^(1/b) tends to the top eigenvalue mu_0(a) of T_2 P_1, which is the top of T_2 on the odd subspace; v >= 1 for every b gives mu_0(a) >= exp(f a c d). Holds (the hypothesis must be read as "for every b", as written: "on every torus"). **Theorem F: HOLDS** (with the corrected Z^(12) of point (1)).

**Section 4.2.** v = Z_odd e^(-f|n|) = u Z e^(-f|n|) = u e^Delta. On (2 n_k)^4: u <= S(2 n_k; (2 n_k)^3) <= s_k^2 (Theorem D (e)). "Falls like an exponential of the side": s_k^2 <= (5041 s)^(2^(k+1))/5041^2, an upper bound linear in the side 2 n_k; it is a statement about the bound, not a lower bound on u. **HOLDS.**

**Proposition T.** (TUBE) gives v(a, b | 2c, d) = Z_odd(a, b | 2c, d) e^(-2f abcd) <= K v(a, b | c, d) Z(a, b | c, d) e^(-f abcd) = K e^(Delta(a, b, c, d)) v(a, b | c, d). Then v(L, L | 2L, L) <= K e^(Delta(L^4)) v(L^4); with d doubled on (L, L | 2L, L) and Delta(L, L, 2L, L) <= 2 Delta(L^4): v(L, L | 2L, 2L) <= K^2 e^(3 Delta(L^4)) v(L^4). Theorem F (c), j = k = 2: v((2L)^4) <= v(L, L | 2L, 2L)^4 <= K^8 e^(12 Delta(L^4)) v(L^4)^4 <= M v(L^4)^4 for L >= L_0. So M^(1/3) v((2L)^4) <= (M^(1/3) v(L^4))^4, and by induction M^(1/3) v((2^k L_0)^4) <= (M^(1/3) v(L_0^4))^(4^k). Since M >= 1: v(L^4) <= exp(-4^k L_0^2 sigma) = exp(-sigma L^2). Sides >= L_0 >= n_0 keep (TUBE) applicable. **HOLDS** as an implication. (TUBE) is open; at Gaussian order it is estimated false for U(1) on thin sections (an estimate, not checked here beyond its form).

**Remark F3.** The extra input, (TM) for the twisted action in the transfer direction 3 (twisted plaquettes spatial), follows from `gap-transfer.md` word for word: the proof of statements (1)-(4) uses of the spatial potential only that it is real, bounded, continuous and gauge invariant; the twisted potential V' = beta sum over p of (1 - (1/2) eps_p tr u_p), eps_p = +-1, has these properties (0 <= V' <= 6 beta |Lambda|), so T' = M' C_E M' is positive, trace class, with simple top eigenvalue and positive eigenfunction; Statement (5) is not needed. I record this as a checked extension (same status as Lemma 1.1), so the qualifier "given a transfer operator for the twisted slice" can be dropped. Symmetry in (c, d): exchange of the axes 3, 4 keeps the plane (1, 2). The inequality: log W = ell c d + c kappa(d) + g(c; d) for both families, so f_m - tau c d = c(kappa(d) - kappa_tw(d)) + g(c; d) - g_tw(c; d); Lemma X gives 0 <= c kappa(d) <= c g/(d - c) for each family; hence f_m - tau cd <= (d/(d-c)) g(c; d) and >= -(d/(d-c)) g_tw(c; d). tau >= 0 because Z^(12) <= Z. **HOLDS.** The reading "the area law is the statement that tau(a, b) falls like exp(-sigma ab)" is an interpretation, not a claim; I do not check it.

**Identity 4.4.** Haar measure is invariant under U -> -U, so for a measurable section Sigma of SU(2) -> SO(3) the map (s, V) -> sV, {+-1} x Sigma -> SU(2), carries (uniform on +-1) x (2 Haar restricted to Sigma) to Haar measure: product. (1/2) tr U_p = s_p J_p(V) (signs are central, s^(-1) = s). For fixed V the integrand is the Z_2 gauge theory with couplings beta J_p(V); the twist replaces s_p J_p by -s_p J_p on the stack, which is the twisted Z_2 theory with the same couplings. Integrating over V: Z_odd/Z = integral of Z_Z2[beta J(V)] u_Z2[beta J(V)] dV / integral of Z_Z2[beta J(V)] dV. **HOLDS** (normalizations of the Z_2 sums and of dV cancel in the ratio).

**Verdict (10): HOLDS** (Theorem F with the corrected Z^(12); Remark F3's extra input is supplied above).

## Point (11). The RECALLED claims about U(1) and Z_2

**Where they occur.** Line 53 (classical twist costs), 62 (C1 (ii): the photon, twelve photon states, Z_2 at its transition and at large beta), 69 (C2 (ii)), 74 (C4 (ii)), 76 (C5 (ii)), 215 (third bullet after Theorem S), 256 (U(1) estimate for (TUBE)), 286, 291, 303 (Section 5). **No proof uses them.** I checked every proof block of Sections 3 and 4 (Theorem D, D2, R, N, N2, J, seam bound, K, X, E, S, S2, S3, F, T, F3, 4.4): none cites U(1), Z_2, the photon, a phase transition or a recalled energy. They appear only in the tests (ii) and in comments. Confirmed.

The arithmetic of the recalled numbers is right: 12 e^(-pi) = 0.5186 (line 215: "about 0.52"); log(1 + 12 e^(-pi)) = 0.418 (line 62: "about 0.41"); log(1 + e^(-pi)) = 0.0423 > 0.04 (line 62; the margin is small, so the o(1) matters).

**My own arguments.** I have short arguments only for a fixed size n with beta -> infinity; none for the claims as stated at a fixed coupling uniformly in the size (which is what "the seed is false at every size" needs).

*(Z_2, fixed n, large beta; checker's argument, by hand, not used by any proof.)* Assume for the Z_2 gauge theory the analogue of Lemma 1.1 (its transfer operator has the same Gram-expansion proof; not written out here). For the box B = (2n)^3 and the eight characters e of Z_2^3, E_e = (1/8) sum over k in Z_2^3 of e(k) C^k are orthogonal projections commuting with T, Omega lies in the range of E_0 (point (3) (e)), so lambda_0^n <= Tr(T^n E_0) = (1/8) sum over k of Z_k, where Z_k = Tr(T^n C^k) is the twisted partition function. Hence

1 + s = Tr T^n / lambda_0^n >= 8 / (1 + sum over k != 0 of Z_k/Z).

Bounds: with normalized counting measure, Z >= 2^(-|E|) 2^(|V|-1) (the pure-gauge configurations sigma_xy = g_x g_y have no frustrated plaquette); for k != 0 every 2-torus slice in a twisted plane (0, i) contains exactly one twisted plaquette, and the product of sigma_p over a 2-torus slice is 1 (each link appears twice), so each slice has a frustrated plaquette, at least 4n^2 in all, and Z_k <= exp(-2 beta 4n^2). So Z_k/Z <= 2^(|E| - |V| + 1) e^(-8 beta n^2) with |E| - |V| = 3 |V| = 24 n^4, which tends to 0 as beta -> infinity at fixed n. So s(n; beta) -> 7 or more: at each fixed n the seed fails for Z_2 at large enough beta (beta of order n^2). This is the fixed-size version of the text's "Z_2 at large beta has s >= 7 - o(1)". The fixed-beta, all-n version needs a Peierls bound with entropy control (deconfined phase); I have no short proof.

*(U(1), fixed n, large beta; sketch.)* The flux group is U(1)^3, with rotations R_theta commuting with T and E_0 = (2 pi)^(-3) integral of R_theta d theta. As above, 1 + s >= Z / Tr(T^n E_0) = Z / ((2 pi)^(-3) integral of Z(theta) d theta). For |theta| >= delta, every 2-torus slice in a twisted plane has plaquette phases summing to theta_i mod 2 pi, so some plaquette has |phase| >= delta/(4n^2) and Z(theta) <= exp(-beta(1 - cos(delta/(4n^2)))); and Z >= (Haar measure of the set where every link is within beta^(-1/2) of 1, a power of beta^(-1/2)) times e^(-C) . So the ratio tends to 0 as beta -> infinity for each delta > 0, and 1 + s >= (2 pi/delta)^3 (1 - o(1)): s -> infinity at fixed n. The seed fails at each fixed size at large enough beta. Not written out in full (the constant C and the measure of the small set are standard estimates I did not do line by line); marked as a sketch. The fixed-beta statement (the photon at every size) is the massless phase of Guth and Frohlich-Spencer; I have no short proof.

*(Z_2 at its transition.)* No argument. It rests on the existence and the nature of the transition, which is not proved here.

**Verdict (11): HOLDS** for "no proof uses them". The claims themselves stay RECALLED; I add proofs only of the fixed-size, beta -> infinity versions (Z_2 by hand, U(1) as a sketch). These versions do not show that the seed fails at a fixed coupling for every size.

## Point (12). My attempt to break Theorem S

Pass and fail criterion, written first: Theorem S fails in a model if S(2n; (4n)^3) > ((1 + s)^64 - 1)^2 with s = S(n; (2n)^3) <= 1/640 (or if the symmetric trace structure holds and the induction gives a gap bound that the model violates). Everything below is by hand; no run.

**Model 1: layered two-dimensional models (exact, integer multiplicities).** Let a two-dimensional model have W_2(a, b) = sum over l >= 0 of m_l w_l^(ab), m_0 = 1, m_l positive integers, 1 = w_0 > w_1 >= ... > 0 with sum of m_l w_l^3 finite (two-dimensional lattice gauge theory on a torus has this form, character expansion; recalled, used only as motivation, the model is defined abstractly). Its transfer operator on a circle of length b is the diagonal operator with eigenvalues w_l^b, multiplicity m_l: positive, trace class, simple top. Put Z(n) = product over planes mu < nu of W_2(n_mu, n_nu)^(|n|/(n_mu n_nu)) (independent copies on every plane). Transfer in direction 1 of the box B: the factors of planes not containing 1 are n_1-th powers of numbers; the factor of the plane (1, nu) is (Tr T_(b_nu)^(n_1))^(|B|/b_nu) = Tr of the tensor power. So Z = Tr T_B^(n_1) with T_B a tensor product of positive trace-class operators: positive, trace class, simple top, integer multiplicities; Z is symmetric in the four sides. With sigma(x) := sum over l >= 1 of m_l w_l^x: 1 + S(t; B) = product over nu of (1 + sigma(t b_nu))^(|B|/b_nu). Hence s = (1 + sigma(2n^2))^(12 n^2) - 1 and S(2n; (4n)^3) = (1 + sigma(8n^2))^(48 n^2) - 1. Since the m_l are integers >= 1, sigma(4x) <= sigma(x)^4. If s <= 1/640 then, with sigma := sigma(2n^2), 12 n^2 log(1 + sigma) = log(1 + s) < 1/640, so sigma < 1/(7000 n^2); then S(2n; (4n)^3) <= exp(48 n^2 sigma^4) - 1 <= 49 n^2 sigma^4, while ((1 + s)^64 - 1)^2 >= (64 log(1 + s))^2 = (768 n^2 log(1 + sigma))^2 >= (760 n^2 sigma)^2 (log(1 + sigma) >= sigma/(1 + sigma)). The ratio left/right is at most 49 sigma^2/(760^2 n^2) < 10^(-11). **No violation**; the margin is huge because these excitations are strings (energy proportional to the length), so S falls like an exponential of an area.

**Model 2: independent modes (free massive lattice field; formula recalled, used only in this test).** For the Gaussian field with nearest-neighbour action and mass M, the transfer operator of a box B is a product of oscillators: 1 + S(t; B) = product over the momenta k of B of (1 - x_k(t))^(-1), x_k(t) = e^(-t omega_k), cosh omega_k = 1 + (M^2 + sum_j 4 sin^2(k_j/2))/2 (recalled; positive trace-class, simple top, symmetric W). Put X = sum over k in the grid G_2n of the box (2n)^3 of e^(-n omega_k). Then log(1 + s) >= X. For the box (4n)^3 at time 2n, the grid G_4n contains G_2n; send each k in G_4n to k' in G_2n by rounding each coordinate toward 0 on the coarser grid. omega is increasing in each |k_j| on (-pi, pi], so e^(-n omega_k) <= e^(-n omega_(k')), and the map is at most 27-to-1 (in each coordinate at most 3 points go to 0 and 2 to every other point). Hence sum over G_4n of e^(-2n omega_k) <= 27 sum over G_2n of e^(-2n omega_(k')) <= 27 X^2, and log(1 + S(2n; (4n)^3)) <= sum over G_4n of x/(1 - x) with x = e^(-2n omega_k) <= 27 X^2/(1 - e^(-2nM')) where M' = omega_0 > 0. So for s <= 1/640 (so X < 1/640): S(2n; (4n)^3) <= 28 X^2 (once e^(-2n M') <= 1/50, i.e. at all n with 2nM' >= 4), while ((1 + s)^64 - 1)^2 >= 4096 X^2. Ratio at most 28/4096 < 1/146. **No violation**, for every mass, in the whole range where the seed holds and 2nM' >= 4 (for 2nM' < 4 one has X >= e^(-2) > 1/640, outside the range). The loss of Theorem S against this model is a factor of about 150: most of it is the exponent 4 of Lemma E in each of three directions (64 against the true 8 at first order).

**Where a counterexample would have to sit.** By Lemmas K and X, a model whose small box has s small but whose large boxes have a light state must lower the ground-state deficit kappa at a larger size, which Lemma K (d) forbids, or produce many states at a fixed time that Lemma E does not see; Lemma E is exact up to its exponent. I found no candidate. This is not a proof; Theorem S is proved in point (7).

**Verdict (12): no counterexample found; Theorem S survives both hand-solvable models with margins of about 10^11 and 150.**

## Verdict table

| Point | Statement(s) | Verdict |
|---|---|---|
| (1) | (TM), (TM-c) for every periodic box with sides >= 3; symmetry of Z | HOLDS AFTER CORRECTION: Lemma 1.1 above (no step of `gap-transfer.md` uses equal sides); the twisted weight of (TM-c) is exp(-beta(1 + (1/2) tr U_p)) on the stack, not "beta with its sign changed" |
| (2) | Lemma A and its uses; consequences of Section 1 | HOLDS |
| (3) | Theorem D (a)-(f), Corollary D2 | HOLDS (D (e) with the corrected Z^(mu nu)) |
| (4) | Proposition R | HOLDS; wording: "every box of side up to" -> "every cube of side 2^k n up to" |
| (5) | Lemma K (a)-(d) | HOLDS |
| (6) | Lemma X, Lemma E (exponent 2b/(b-a)) | HOLDS |
| (7) | Theorem S (three uses of Lemma E, S(2n) <= S(n)^2, constants 64, 71, 5041, 1/640, 1.9 x 10^(-4), induction, gap) | HOLDS |
| (8) | Corollary S2; Corollary S3 | S2 HOLDS AFTER CORRECTION (the O(3) scope sentence is not proved); S3 HOLDS |
| (9) | Proposition N, Remark N2, Lemma J, seam bound | HOLDS |
| (10) | Theorem F, Section 4.2, Proposition T, Remark F3, Identity 4.4 | HOLDS (F with the corrected Z^(12); F3's extra input supplied in point (10)) |
| (11) | RECALLED claims unused by proofs | HOLDS; own proofs only of fixed-size, beta -> infinity versions (Z_2 by hand, U(1) sketch) |
| (12) | Own attempt to break Theorem S | no counterexample; two hand-solvable models satisfy it with margins about 10^11 and 150 |

No statement FAILS. In the row 675 terms: Theorem S and its lemmas CORRECT-NO-ADVANCE on the seed itself, ADVANCE on the step (the doubling step that the earlier plans left open is proved).

## Exact list of inputs of Theorem S

1. For every box B = (b_1, b_2, b_3) with all sides >= 3 (needed: (y, 2n, 2n), (4n, y, 2n), (4n, 4n, y) and their transposes, y >= 3 arbitrary, and (2 n_k)^3): a positive trace-class operator T_B with Z(t | B) = Tr T_B^t for every t >= 3, and a simple top eigenvalue (Lemma 1.1 (i)-(iii); from `gap-transfer.md` statements (1b), (2c), (3), (4b) with N^3 replaced by |B|). The positive eigenfunction is not needed by Theorem S (only by Theorem D (e) and Theorem F).
2. Invariance of Z under the exchange of two axes (Lemma 1.1 (v)).
3. Finiteness of ell for each pair of fixed sides: e^(-12 beta |n|) <= Z <= 1.
4. Lemma A (a), (b) (elementary, point (2)); the spectral theorem for compact positive operators (A2 of `gap-transfer.md`) for Tr T^k = sum of lambda_i^k with multiplicity.
5. For the last line only: Theorem D (b) (same inputs).

Nothing about SU(2) beyond these enters. (TM-c), the centre flips, are not inputs of Theorem S.

## What this check did not cover

- `gap-transfer.md` Sections 6-8 and its check's foundations table: not re-checked (not used by the text). Sections 1-5 and 9.3 were read and their side-dependence checked, not re-proved line by line; I rely on the row 671 check for (1)-(5).
- Section 2 of the text (the candidates C1-C5, tests (i)-(iii)), the Ways 2 and 3 of Section 3.3 beyond Lemma J and the seam bound, Section 4.3's U(1) Gaussian estimate for (TUBE), Sections 5 and 6 (plans and verdicts): read, not checked as mathematics (they are estimates, recalled facts or opinions). The claim "every exact tool holds word for word for U(1)" is not checked.
- The Tomboulis-Yaffe inequality and every GUIDE item: not checked, and not used by any checked proof.
- The O(3) transfer structure (Corollary S2's scope) and the Z_2/U(1) transfer structures used in my point (11) arguments: not proved here.
- The sanity runs of Section 3.4 (scripts in a scratch folder of the author): not re-run; they are guides only. I ran no numeric job.
- Independence: same provider as the author (Anthropic), different model. Row 699 is the check by another provider.

**No mass gap is proved by this file or by the checked text, whatever the verdicts.** (SEED) at couplings of order one, (TUBE'), and C3-C5 stay open.
