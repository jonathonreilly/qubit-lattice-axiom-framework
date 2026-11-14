lead: anthropic/claude-fable-5-2/max mac-mini-worker
lease_until: 2026-11-11T19:45Z

# The crux of the mass gap, restated (row 697, `gap-crux-restate`)

Author run, started 2026-11-11T07:45Z at commit 51785e8cb. Research-stage working state. Nothing here is a claim of a mass gap.

Status of this file: complete for this run (ended 2026-11-11, about 10:30Z). The final status block is Section 6. The main result is Theorem S (Section 3.4).

**No mass gap is proved here.** Check state (2026-11-11, added by the lead): the statements of Sections 1, 3 and 4 are checked line by line by Claude Opus 5.5 (row 698, `library/gap-seed-check.md`), and Sections 1, 3.1 and 3.4 also by Codex gpt-6-astra (row 699, `library/gap-seed-check-astra.md`). No statement fails. The corrections of the two checks are applied below and each is marked with its row. Not checked: the candidates and estimates of Section 2, and Section 5. The seed inequality itself is not proved.

## 0. Position, repo search, reading state

**Kind of result.** A proof of a step that both max plans left open: Theorem S (Section 3.4). One inequality between two partition functions of periodic tori, at one size, gives a gap that is uniform on all dyadic cubes. The crux of the gap on periodic boxes is then one finite statement, (SEED). The file also proves the supporting steps (Theorems D, F, Lemma J, Propositions N, R, T) and names the open step of the flux half, (TUBE'). No tool for the seed at couplings of order one was found. Section 5 says this in plain words.

**Repo search (rule 0a), done before the attempts.** Searched `library/gap-*.md`, `library/prior/gap-*.md`, `library/open-core.md` for: Knabe, frustration, heat bath, subadditiv, Renyi, step scaling, Simon-Lieb, chessboard, Mack, vortex, Casimir, doubling. Matches that bind this file:

- Run 1 (`gap-skeleton-max.md`): Lemma 4 (doubling identities with entropies, lines 262-275), crux (F) (line 126), B7 (the Knabe threshold, lines 159-164, excluded there by the rate filter). I do not attack B7 again.
- Run 2 (`gap-skeleton-max-b.md`): A1 and crux (FE) (lines 140-147), Section 1.5 (lines 241-282): Lemma 1 (a)-(d), Lemma 1', Lemma 2, the crossing identity, and the named failure Lemma NSM. A5 (STEP), A9 (SL).
- Row 691 (`gap-ds-gauge.md`): Theorem W, Propositions B and S.
- So the torus algebra and the flux doubling are not new here. What is added: the monotone deficit and the closed recursion (Lemmas K, X, E, Theorem S), the form with no infinite-volume constant (Theorem D), the form with no entropy term (Theorem F), the exact first-order identity (Lemma J), and the open statement (TUBE').

**Read for this file.** FINISH row 697; `gap-skeleton-final.md` whole; the passages above; `gap-ds-gauge.md` 3.1, 4, 6; `prior/gap-crux-lit-2.md` headings, T7, C5 (the seed criterion), the synthesis tables and "Routes bounded". **Not read:** the bodies of `gap-zf-box-x.md`, `gap-zf-box-s.md`, `gap-ac-lat.md` (their statements are taken from Sections 12-13 of the final skeleton); every primary paper. Nothing was fetched from the network.

**Credits.** Sussman and Alpoge with Claude and Codex (the account; not used in any proof below). Run 1 and run 2 of Claude Fable 5.2 max (Lemma 4; Lemma 1, 1', 2, crossing, NSM). Osterwalder and Seiler, Luscher (transfer operator, through row 667). 't Hooft (twists and flux). Tomboulis and Yaffe, Kanazawa (the inequality; GUIDE here). Ursachi (the idea of a doubling defect as the criterion; abstract only, GUIDE). Mack and Petkova (the Z_2 and SO(3) splitting; GUIDE).

**Marks.** PROVED = proved by hand in this file from the named inputs, not checked. GUIDE = a statement of a paper, recalled, used in no proof. RECALLED = a known fact used only in a test (ii).

## 1. Setting and inputs

Torus with sides n = (n_1, ..., n_4), all n_mu >= 3. Action A(U) = sum over plaquettes of (1 - (1/2) tr U_p). Z(n) = integral of exp(-beta A) over Haar measure, F(n) = log Z(n), |n| = n_1 n_2 n_3 n_4. beta > 0 is fixed unless said.

**(TM)** (input; `library/gap-transfer.md`, row 667, check row 671). For each direction mu and each choice of the other three sides there is a positive trace-class operator T on a Hilbert space with Z(n) = Tr T^(n_mu). Its largest eigenvalue is simple, with a strictly positive eigenfunction. (Rows 698, 699: `gap-transfer.md` states this for the cube with equal sides. Both checks find that no step there uses equal sides. The statement for every box with sides at least 3 is Lemma 1.1 of `library/gap-seed-check.md` and point 1 of `library/gap-seed-check-astra.md`: replace N^3 by the product of the three sides and keep the gauge projection.)

**(TM-c)** (input; run 2, Lemma 1'). For nu different from mu, the centre flip C_nu (multiply by -1 every link of direction nu that crosses the plane x_nu = 0 of the slice) is a unitary involution that commutes with T, and Tr(T^(n_mu) C_nu) = Z^(mu nu)(n). Here Z^(mu nu) is the partition function with the weight exp(-beta (1 - (1/2) tr U_p)) replaced by exp(-beta (1 + (1/2) tr U_p)) on one stack of (mu,nu)-plaquettes (corrected, rows 698 and 699: the first wording, "the sign of beta changed", gives an extra factor exp(2 beta) for each plaquette of the stack), one plaquette for each value of the other two coordinates. It is positive, and it is symmetric in mu and nu.

**Lemma A** (run 2, Lemma 1 (a), (b); two-line proofs there). Let S >= 0 be trace class with eigenvalues lambda_0 >= lambda_1 >= ... . (a) k -> (Tr S^k)^(1/k) is non-increasing and tends to lambda_0. So Tr S^(jk) <= (Tr S^k)^j for integers j, k >= 1. (b) for S not zero and integers k >= 1 (corrected, row 699: for S = 0 the quotient is 0/0), lambda_0^k >= Tr S^(2k) / Tr S^k.

**Consequences used below** (run 2, Lemma 1 (c)). F(n)/|n| is non-increasing in each side. f := inf over n of F(n)/|n| is finite, and

(LB) Z(n) >= exp(f |n|) for every torus.

Delta(n) := F(n) - f |n| >= 0 is the excess free energy. Multiplying one side by an integer j multiplies Delta by at most j.

For the box B = (n_2, n_3, n_4) with transfer operator T in direction 1, eigenvalues lambda_0 > lambda_1 >= ..., put r_i = lambda_i / lambda_0, S(k; B) = sum over i >= 1 of r_i^k, and m(B) = log(lambda_0 / lambda_1). Then r_1^k <= S(k; B) and S(k + k'; B) <= S(k; B) S(k'; B).

## 2. Part 1: candidate statements of the crux

The object in every candidate is the Wilson SU(2) measure at one real beta. "Uniform" means: constants do not depend on the torus or box. For the tree, each statement is needed in the scaling form: for beta >= beta_1 with rates proportional to the scale function a(beta), and on [r_0, beta_1] with fixed rates (final skeleton, Sections 4 and 13.6).

The test (i)-(iii) has the same answer to (i) for all five. I give it once.

**(i) for all five.** The group enters the definitions through two facts only. Fact T: the single-plane twist has classical cost zero for SU(2), because iσ_1 and iσ_2 anticommute (run 1, Facts 1-3). For U(1) the same twist costs beta pi^2 n_3 n_4 / (2 n_1 n_2) at Gaussian order, and for Z_2 it costs 2 beta n_3 n_4. Fact B: the one-loop coefficient b_0 = 11/(24 pi^2) is positive. No exact inequality found here or in the sources uses Fact B at couplings of order one. So in every candidate the group enters the proof only at the step that is still open. I found no candidate for which this is not so.

**C1. One seed on two periodic tori (new; not Route T, not Route Z, no boundary values).** Put

Phi(n) := 16 F(n,n,n,n) - F(2n,2n,2n,2n) >= 0, the free-energy defect of doubling the symmetric torus.

- (SEED): there is n >= 3 with Phi(n) <= 1.9 x 10^(-4). Scaling form for the tree: there are L_0 and beta_1 such that for every beta >= beta_1 (SEED) holds at some n <= L_0 / a(beta), and on [r_0, beta_1] it holds at some n <= n_max.
- What it gives (Theorems D and S, PROVED): the cubes of side 2^(k+1) n, k >= 0, have a gap of at least log(1/(5041 (exp(Phi(n)) - 1)))/n >= 0.04/n, on the whole space, flux sectors included. In the scaling form the gap is at least 0.04/L_0 in physical units, uniformly in the cutoff. The step from one size to all dyadic sizes is a theorem. It closes the recursion that run 2 could not close in its Section 1.5.
- The seed in other words: Phi(n) = 96 n^4 times the integral over [0, beta] of (abar_2n - abar_n), with abar_n the mean plaquette action on the n^4 torus (Theorem D (f)). So (SEED) is a bound on the finite-size shift of one number.
- (ii) U(1) at weak coupling: the periodic box has an excited state of energy at most (2 pi / side)(1 + o(1)) (RECALLED, the photon; run 2's K5). By Theorem D (c), read backwards, Phi(n) >= log(1 + exp(-pi - o(1))) > 0.04. With the twelve lowest photon states of the box (six momenta, two polarisations, energy pi/n each; RECALLED) Theorem D (b) gives Phi(n) >= log(1 + 12 exp(-pi)) - o(1), about 0.41. So (SEED) is false at every size. Z_2 at its transition: two phases, so m(box) tends to 0 (RECALLED) and Phi(n) >= log 2 - o(1). Z_2 at large beta: the flux sectors are degenerate with the vacuum (RECALLED), same bound; this is why C1 is the gap with confinement.
- (iii) Theorems D and S hold for every group. The proof of (SEED) must use the group, and by the rate filter it must work at a size of the order of the correlation length.

**C2. Flux on tori with normalised bulk (the published lead (a) in exact form).** Twist in the plane (1,2). Z_odd(n) := (Z(n) - Z^(12)(n))/2, u(n) := Z_odd(n)/Z(n), v(n) := Z_odd(n) exp(-f |n|), so 0 <= u <= v (by (LB)).

- (FLUX-4): there are sigma > 0 and L_0 such that for every L >= L_0 there is a torus (a, b | L, L) with v(a, b | L, L) <= exp(-sigma a b).
- What it gives (Theorem F, PROVED): u(ja, kb | L, L) <= exp(-sigma (ja)(kb)) for all integers j, k >= 1. With the Tomboulis-Yaffe inequality (GUIDE; Kanazawa, Theorem 1) this is the area law with tension sigma. It is not a gap for the zero-flux sector.
- (ii) U(1) at weak coupling has no area law (RECALLED: Guth; Frohlich and Spencer), and the Tomboulis-Yaffe inequality holds for U(1) (GUIDE: Kanazawa, Theorem 4), so (FLUX-4) is false. At Gaussian order sup over (a,b) of -log v / (ab) is of order g^2 / L^2: the flux spreads over the transverse section. Z_2 at large beta: u tends to 1/2, false.
- (iii) Theorem F holds for every group with a central Z_2. The step that would make (FLUX-4) finite is (TUBE) of Section 4.3; it is false for U(1) on thin transverse sections (estimate there).

**C3. The finite-box hypothesis (W) (kept; `library/gap-ds-gauge.md`).** (W) at (R, delta) for one R. It is the only form in this lane in which one scale is enough, and the reason is that it quantifies over all boundary values. (ii) Proposition B there: (W) gives decay, so it is false for U(1) at weak coupling and for Z_2 at its transition. (iii) Theorem W holds for every compact fibre. Sections 3.3 and 4.3 show why no statement about periodic tori alone can replace the boundary values with the tools at hand.

**C4. Dominance (kept; `library/gap-zf-box-s.md`, Theorem V).** (DOM_B) on one complex neighbourhood of [r_0, beta_1], uniform in the box. (ii) A transition at real beta_c puts zeros of large boxes at beta_c (RECALLED for U(1) and Z_2), and by Proposition D there dominance fails. (iii) Theorem V holds for every group.

**C5. Continuity in the twisted fibre (kept; (AC'-lat), `library/gap-ac-lat.md`).** For beta >= beta_1: inf over n >= 2 of m(beta, n) > 0. This is the one candidate in which Fact T is used in a proof, at small n (the chart (CH), row 679). (ii) U(1) has no twisted fibre with a unique minimum; Z_2 has no twist eater. (iii) The chart is non-Abelian; nothing known carries it to large n.

**How the five stand to each other.** C1 and C3 are finite: one scale is enough. C1 asks for one inequality between two partition functions of periodic tori. C3 asks for a bound over all boundary values of one cube. C2, C4 and C5 are statements at all scales. C1 is the gap with confinement; C2 is the flux half; C3 and C4 are stronger (all boundary values; complex beta); C5 is C1 for another family. I could not find a statement that is weaker than the gap and still closes the tree.

## Status block (kept current; the final version is Section 6)

- Written: Sections 0-2 (Part 1), Section 3 (attempt 1: ended with a proof, Theorem S), Section 4 (attempt 2: ended at its stop statement (TUBE')), Sections 5-6.
- Proved here, not checked: Theorem D, Corollary D2, Proposition R, Proposition N, Lemma J with the seam bound, Lemmas K, X, E, Theorem S, Corollary S2, Theorem F, Proposition T.
- Open: (SEED) for SU(2) at couplings of order one (C1); (TUBE') (C2); C3, C4, C5 as before.

## 3. Part 2, attempt 1: the gap on periodic boxes from two tori per scale (C1; lead (b))

Lead (b) asks for a seed and a doubling step for ratios of partition functions of small tori. This section proves what a seed gives (3.1, 3.2), records three ways to the doubling step that failed (3.3), and then proves the step (Theorem S, 3.4).

### 3.1 Theorem D (PROVED from (TM), (TM-c), Lemma A)

Let n >= 3, Phi(n) = 16 F(n,n,n,n) - F(2n,2n,2n,2n), and let T be the transfer operator in direction 1 of the box B_2 = (2n, 2n, 2n).

- (a) Phi(n) >= 0.
- (b) 1 + S(n; B_2) <= exp(Phi(n)).
- (c) exp(-n m(B_2)) <= exp(Phi(n)) - 1. So if Phi(n) < log 2, then m(B_2) >= (1/n) log(1 / (exp(Phi(n)) - 1)). Read backwards: Phi(n) >= log(1 + exp(-n m(B_2))).
- (d) The number N(E) of eigenvalues lambda_i, i >= 1, with log(lambda_0 / lambda_i) <= E satisfies N(E) <= exp(n E) (exp(Phi(n)) - 1).
- (e) The odd-flux weight of the torus (2n)^4, for each of the six planes, satisfies u <= S(2n; B_2) <= (exp(Phi(n)) - 1)^2. So 1 - Z^(mu nu)/Z <= 2 (exp(Phi(n)) - 1)^2.
- (f) Phi(n; beta) = 96 n^4 times the integral over s in [0, beta] of (abar_2n(s) - abar_n(s)), where abar_n(s) is the expectation of 1 - (1/2) tr U_p on the n^4 torus at coupling s.

Proof. (a) Lemma A (a) with j = 2, in the direction mu: Z(..., 2 n_mu, ...) <= Z(..., n_mu, ...)^2. Four such steps give Z((2n)^4) <= Z(n^4)^16.
(b) Tr T^n = Z(n, 2n, 2n, 2n) =: Z_1 and Tr T^(2n) = Z((2n)^4). By Lemma A (b), lambda_0^n >= Z((2n)^4) / Z_1. So 1 + S(n; B_2) = Tr T^n / lambda_0^n <= Z_1^2 / Z((2n)^4). Three steps of (a), in the directions 2, 3, 4, give Z_1 <= Z(n^4)^8. So 1 + S(n; B_2) <= Z(n^4)^16 / Z((2n)^4) = exp(Phi(n)).
(c) r_1^n <= S(n; B_2), and r_1 = exp(-m(B_2)).
(d) N(E) exp(-n E) <= S(n; B_2).
(e) Z_odd = Tr(T^(2n) P) with P = (1 - C_nu)/2. The eigenvector of lambda_0 is strictly positive, and C_nu maps positive functions to positive functions and commutes with T. So this eigenvector is even, and Tr(T^(2n) P) <= sum over i >= 1 of lambda_i^(2n) = lambda_0^(2n) S(2n; B_2). Also Z >= lambda_0^(2n), and S(2n; B_2) <= S(n; B_2)^2.
(f) dF(n)/dbeta = -6 |n| abar_n and F(n; 0) = 0 (run 2, Lemma 2). So d Phi/d beta = -96 n^4 abar_n + 96 n^4 abar_2n. QED

**Corollary D2 (PROVED).** (i) If Phi(n) <= C exp(-c n) <= 1, then m((2n)^3) >= c - log(2C)/n. (Use e^x - 1 <= 2x on [0,1].)
(ii) Let (Phi-step) be the statement: there are eps_0 > 0, K and n_0 such that Phi(n) <= eps_0 and n >= n_0 give Phi(2n) <= K Phi(n)^2. Let (Phi-step) hold with K >= 2 and eps_0 <= 1/2, and let n_1 >= n_0 with Phi(n_1) < min(eps_0, 1/K). Put Phi_k = Phi(2^k n_1). Then K Phi_k <= (K Phi_0)^(2^k), and for every k >= 0:

m((2^(k+1) n_1)^3) >= (1/(2^k n_1)) log(1/(2 Phi_k)) >= log(1/(K Phi(n_1))) / n_1.

Proof of (ii). Induction: K Phi_(k+1) <= (K Phi_k)^2, and Phi_k <= Phi_0 < eps_0 keeps the step valid. Then Theorem D (c) with e^x - 1 <= 2x, and log(1/(2 Phi_k)) >= 2^k log(1/(K Phi_0)) + log(K/2). QED

So one seed and the step give a gap for all dyadic boxes, with a rate that does not depend on the box. The rate is in the units of the seed size n_1. The rate filter then says that the seed size is at least of the order of the correlation length.

### 3.2 Proposition R: a seed has an exponential reach, and no more (PROVED)

Let Delta(n,n,n,n) <= eps. Then for every k >= 0 with 8^k eps <= 1: m((2^k n)^3) >= (1/n) log(1/(2 8^k eps)).

Proof. Multiply three sides by 2^k: Delta(n, 2^k n, 2^k n, 2^k n) <= 8^k eps. By run 2's Lemma 1 (d), 1 + S(n; (2^k n)^3) <= exp(Delta(n, 2^k n, 2^k n, 2^k n)). Then r_1^n <= exp(8^k eps) - 1 <= 2 8^k eps. QED

Meaning. If Delta(n^4) <= exp(-mu n), the gap of every cube of side 2^k n <= n exp(mu n / 3) (corrected, row 698: the proof covers these cubes, not every box up to that side) is at least mu - (3k log 2 + log 2)/n. Positivity alone carries a seed over exponentially many scales. It does not carry it to infinite volume, and it uses f, which is a limit over all sizes: Delta(n^4) = sum over k >= 0 of 16^(-(k+1)) Phi(2^k n). Theorem D is the form that uses two finite tori and reaches one doubling.

### 3.3 The doubling step: three ways that failed (kept as a record; Section 3.4 has the way that works)

**Way 1: positivity of the transfer operators in all four directions. It cannot work (Proposition N, PROVED).**

Lemma A, (LB) and Theorem D (a), (b) use (TM) only through this weaker property (TM'): for each direction mu and each choice of the other sides, Z(n) is the integral of lambda^(n_mu) against a positive measure on (0, Lambda] that has an atom of mass at least 1 at Lambda; and Z is symmetric in the sides. Theorem D (c)-(e), Corollary D2 and Proposition R use one more property of a trace: every eigenvalue has multiplicity at least one. It enters through r_1^k <= S(k) and S(k + k') <= S(k) S(k'). Call (TM') with integer multiplicities (TM-int).

Proposition N. Let 0 < q < 1, c > 0, f real, w(k) = c q^k, and Z_w(n) := exp( f |n| + sum over mu of (|n| / n_mu) w(n_mu) ). Then Z_w has (TM'), its infimum of F/|n| is f, and for every n:

32 n^3 c q^n <= Phi(n) <= 64 n^3 c q^n and Phi(2n) >= Phi(n)^2 / (16 n^3 c).

So for given n, eps and K, the choice c <= min( eps / (64 n^3 q^n), 1 / (16 n^3 K) ) gives Phi(n) <= eps and Phi(2n) >= K Phi(n)^2.

Proof. As a function of n_1, with V = n_2 n_3 n_4: Z_w = Lambda^(n_1) exp(V c q^(n_1)), Lambda = exp(f V + sum over mu >= 2 of (V/n_mu) w(n_mu)), and exp(V c q^(n_1)) = sum over j >= 0 of ((V c)^j / j!) (q^j)^(n_1). This is a positive combination of exponentials and the top weight is 1. F/|n| = f + sum over mu of w(n_mu)/n_mu, which is above f and tends to f. So Delta(n^4) = 4 n^3 w(n) and Phi(n) = 16 Delta(n) - Delta(2n) = 64 n^3 c q^n - 32 n^3 c q^(2n). The two bounds on Phi(n) follow from 0 < q^n < 1. Then Phi(2n) >= 32 (2n)^3 c q^(2n) = 256 n^3 c q^(2n), and Phi(n)^2 <= 4096 n^6 c^2 q^(2n). QED

What Proposition N shows. Z_w is an ideal gas of one kind of winding excitation with weight c per unit volume. Phi(2n) is linear in c and Phi(n)^2 is quadratic. So a doubling step needs that a state counts at least once: a light state of the box (4n)^3 must be seen, with weight at least one, in the sums of the box (2n)^3. A positive measure does not know this. A trace does, and Section 3.4 uses it.

Remark N2 (the integer class; PROVED for the family; the general case is Theorem S). Z_w is not in (TM-int): its weights (V c)^j / j! are not integers. The gas of the same kind with integer multiplicities is Z = exp(f |n|) times the product over mu of (1 - q^(n_mu))^(-c |n| / n_mu), with c a positive integer; it has w(k) = -c log(1 - q^k). For it, when q^n <= 1/2: Phi(n) >= 32 n^3 c q^n and Phi(2n) <= 1024 n^3 c q^(2n), so Phi(2n) <= Phi(n)^2 / (n^3 c) <= Phi(n)^2. The step holds with K = 1. The same holds for several species with integer c_j, by (sum of c_j x_j)^2 >= sum of c_j x_j^2. The reason, in this family: by the symmetry of Z, a winding weight that is a thermal state in one direction is a factor exp(n_mu times a deficit) in the other three, and integer multiplicity then makes it extensive. So integer multiplicity together with the symmetry in the four directions is a real restriction, and Proposition N does not exclude a proof of a doubling step from (TM-int). Section 3.4 gives such a proof, for the thermal sums (the form (FIT) below). The place where Z_w fails is the doubling of the time, S(2k; B) <= S(k; B)^2, which needs multiplicities at least one.

By Theorem S no symmetric model with positive transfer operators violates the step in the form (FIT). For local quantum Hamiltonians without this structure no finite-size criterion can exist: the spectral gap problem is undecidable (GUIDE: Cubitt, Perez-Garcia and Wolf; recalled, not read here).

**Way 2: compare the torus (2n)^4 with sixteen tori n^4 by cutting and gluing. Exact result, of the wrong size (PROVED).**

The links of the torus (2n)^4 are the disjoint union of the links of sixteen blocks, and each block is the link set of a torus n^4. A plaquette of the large torus lies in one block, or it is a seam plaquette that has links of at least two blocks. The number of seam plaquettes is N_seam = 96 n^4 (1 - (1 - 1/n)^2) = 192 n^3 - 96 n^2.

Lemma J (gauge averaging; PROVED). Let mu be a probability measure on link configurations that is invariant under all gauge transformations. Let p be a plaquette with corners x_0, ..., x_3, and let k_1, k_2, k_3 be fixed elements of SU(2). Then the expectation of (1/2) tr(U_01 k_1 U_12 k_2 U_32^(-1) k_3 U_03^(-1)) equals (1/2 tr k_1)(1/2 tr k_2)(1/2 tr k_3) times the expectation of (1/2) tr U_p. (Seam case.) If the links of p belong to two independent systems, each with a gauge-invariant law, then the expectation of (1/2) tr U_p is 0.
Proof. A gauge transformation g replaces k_c by g_c^(-1) k_c g_c and leaves mu invariant. Average over g_c with Haar measure: the average of g^(-1) k g commutes with SU(2), so it is the scalar (1/2) tr k. Seam case: a gauge transformation of the second system at one end of its link multiplies that link by g and leaves the links of the first system fixed; the Haar average of g is 0. QED

Consequence. Under the product of the sixteen Gibbs measures, a seam plaquette of the large torus has expectation of (1/2) tr equal to 0 (seam case: its links lie in at least two blocks), and the plaquette of a small torus that it replaces has 1 - abar_n. Jensen's inequality for Z((2n)^4) / Z(n^4)^16 gives

Phi(n) <= beta (192 n^3 - 96 n^2) (1 - abar_n(beta)).

This is true and of order beta n^3. Theorem D needs Phi(n) < log 2. The bound cannot be improved at first order: by Lemma J the first-order cost of a seam plaquette is exactly beta (1 - abar_n), whatever the coupling. A gluing of independent pieces always pays the full plaquette energy on the seam.

**Way 3: a smooth deformation in place of a cut (the Mermin-Wagner idea). It fails for the same exact reason.**

For spin models with a continuous symmetry, a twist is spread over the whole torus and costs only a gradient energy. The lattice gauge measure has no continuous global symmetry. The deformations at hand multiply links by fixed elements h_l. By Lemma J the first-order cost of a plaquette is beta (1 - abar) (1 - product over corners of (1/2) tr k_c) >= 0, where k_c is the product of the h at the corner. It is zero only if every k_c is in the centre, that is, only if the deformation is a gauge transformation times a field with values in the centre. For an Abelian spreading of the flux pi over the plane (1,2), k_c = exp(i a_c σ_3) with a_c of order pi times a coordinate over n_1 n_2, and the cost is beta (1 - abar) times a sum of a_c^2 / 2. The sum is of order pi^2 |n| / min(n_1, n_2)^2. It grows with the size of the torus. For U(1) the same spreading is covariant and costs beta pi^2 n_3 n_4 / (2 n_1 n_2), which does not grow on symmetric tori. So first-order comparison sees the gauge potential of the deformation, not its field strength. It gives nothing that is uniform in the size.

**State after three ways.** (Phi-step) failed in three ways: positivity without integer multiplicities (Proposition N), gluing (exact surface term), deformation (Lemma J: no covariant first-order comparison). The exact statement that was left at this point:

(FIT) There are n_0 and theta in (0, 1] such that for all n >= n_0: S(2n; (4n)^3) <= (1/theta) S(n; (2n)^3)^2 whenever S(n; (2n)^3) <= theta. In words: the thermal sum of the doubled box at the doubled time is at most a constant times the square of the thermal sum of the box.

(FIT) closes C1 in this sense (PROVED implication; the seed can be read from two tori, by Theorem D (b)): if S(n_1; (2 n_1)^3) < theta for one n_1 >= n_0, then S(2^k n_1; (2^(k+1) n_1)^3) <= theta (S(n_1; (2n_1)^3)/theta)^(2^k), so m((2^(k+1) n_1)^3) >= log(theta / S(n_1; (2 n_1)^3)) / n_1 for all k. The proof is the induction of Corollary D2, with r_1^k <= S(k; B). Remark, not a proof for a lattice model: for the gas Z_w the two sides of (FIT) are about 64 n^3 w(2n) and 64 n^6 w(n)^2 / theta, so (FIT) holds exactly when n^3 c, the weighted number of one-particle states of the box of side n, is at least of order theta. Proposition N is the case where n^3 c is made small by hand.

**A fourth way works.** Section 3.4 proves (FIT), with theta = 1/5041, from (TM) and the symmetry of Z alone. It was found after the three ways above; they stay in the file as the record of what does not work. (Phi-step) itself, an inequality between Phi(2n) and Phi(n)^2, is not proved and is no longer needed.

### 3.4 Theorem S: one seed gives a uniform gap on dyadic boxes (PROVED from (TM) and the symmetry of Z)

This is the main result of the file. It answers lead (b) with yes. The step that both max plans left open is true, and the reason is one fact that their chains did not use: the deficit of the ground state is non-increasing in the size (Lemma K). Run 2 writes that every inequality that touches the deficit carries it on both sides and cancels (its Section 1.5). With Lemma K it does not cancel. Run 2 compared the boxes at a time equal to the side; that is the one shape for which Lemma E below gives nothing. The shape with time equal to half the side closes.

**Setting for the lemmas.** Let W(a, b) be defined for integers a, b >= 3, positive, with W(a, b) = W(b, a), and for each b let there be a positive trace-class operator T_b with W(a, b) = Tr T_b^a for all a. Put lambda(b) = the largest eigenvalue of T_b, e(b) = log lambda(b), 1 + S(a; b) = W(a, b) / lambda(b)^a >= 1, g(a, b) = log(1 + S(a; b)) >= 0. Assume ell := inf over a, b of log W(a, b) / (a b) is finite, and put kappa(b) = e(b) - ell b.

The use: W(a, b) = Z(a, b, c, d) with c, d fixed. It is symmetric in a and b because Z is invariant under the lattice symmetry that exchanges two axes. T_b is the transfer operator of the box (b, c, d). Then S(a; b) is S(a; (b, c, d)) of Section 1. The same holds for any two of the four directions.

**Lemma K (the deficit is non-negative, convex and non-increasing; PROVED).** (a) e(b) = lim over a of (1/a) log W(a, b) = inf over a. (b) e(jb) <= j e(b) for integers j >= 1, and ell = inf over b of e(b)/b, so kappa >= 0. (c) e and kappa are convex: e(b+1) + e(b-1) >= 2 e(b) for b >= 4 (domain corrected, rows 698 and 699: all three sizes must be at least 3; this is all that (d) uses). (d) kappa(b+1) <= kappa(b) for all b >= 3.

Proof. (a) Lemma A (a) for T_b. (b) W(a, jb) = Tr T_a^(jb) <= (Tr T_a^b)^j = W(a, b)^j by the symmetry and Lemma A (a) for T_a; take (1/a) log and let a grow. The formula for ell follows from (a). (c) For fixed a, b -> log W(a, b) = log Tr T_a^b is the logarithm of a sum of exponentials of b with positive weights, so it is convex in b. By (a), e is a pointwise limit of convex functions. (d) Suppose kappa(b_0 + 1) - kappa(b_0) = c > 0. By convexity the increments do not decrease, so kappa(b) >= c (b - b_0) for b >= b_0, and e(b)/b >= ell + c/2 for all large b. Choose b_1 with e(b_1)/b_1 < ell + c/2. By (b), e(j b_1)/(j b_1) < ell + c/2 for all j. Contradiction. QED

**Lemma X (crossing with Lemma K; PROVED).** For all a, b: a kappa(b) + g(a, b) = b kappa(a) + g(b, a). For a < b: (b - a) kappa(b) <= g(a, b).

Proof. W(a, b) = lambda(b)^a (1 + S(a; b)) and W(b, a) = lambda(a)^b (1 + S(b; a)) are equal; take logarithms; the terms ell a b cancel. For a < b: g(b, a) >= 0 and kappa(a) >= kappa(b) by Lemma K (d), so a kappa(b) + g(a, b) >= b kappa(b). QED

In words: the deficit of the ground state of the box is bounded by the thermal sum of the same box at a shorter time. For a gas of particles of mass M this says, roughly, exp(-M b) <= b exp(-M a). The inequality is exact.

**Lemma E (one side of the box doubled at fixed time; PROVED).** For a < b: 1 + S(a; 2b) <= (1 + S(a; b))^(2b/(b-a)). For a = b/2 the exponent is 4.

Proof. W(a, 2b) = Tr T_a^(2b) <= (Tr T_a^b)^2 = W(a, b)^2. So lambda(2b)^a (1 + S(a; 2b)) <= lambda(b)^(2a) (1 + S(a; b))^2, and 1 + S(a; 2b) <= (1 + S(a; b))^2 exp(a (2 kappa(b) - kappa(2b))) <= (1 + S(a; b))^2 exp(2a kappa(b)). By Lemma X, 2a kappa(b) <= (2a/(b-a)) g(a, b). QED

**Theorem S.** Let n >= 3 and s = S(n; (2n)^3), the thermal sum of the cube of side 2n at time n. Then

S(2n; (4n)^3) <= ((1 + s)^64 - 1)^2.

If s < 1/5041, then for every k >= 0, with n_k = 2^k n:

S(n_k; (2 n_k)^3) <= (5041 s)^(2^k) / 5041 and m((2 n_k)^3) >= log(1/(5041 s)) / n.

By Theorem D (b), s <= exp(Phi(n)) - 1. So the seed holds if Phi(n) = 16 F(n,n,n,n) - F(2n,2n,2n,2n) <= 1.9 x 10^(-4) for one n >= 3.

Proof. Lemma E with a = n, b = 2n, for the pair of directions (1, 2) with the sides (2n, 2n) of the directions 3, 4 fixed: 1 + S(n; (4n, 2n, 2n)) <= (1 + s)^4. Lemma E for the pair (1, 3) with the sides (4n, 2n) fixed: 1 + S(n; (4n, 4n, 2n)) <= (1 + s)^16. Lemma E for the pair (1, 4) with the sides (4n, 4n) fixed: 1 + S(n; (4n)^3) <= (1 + s)^64. Then S(2n; (4n)^3) <= S(n; (4n)^3)^2, because every eigenvalue has multiplicity at least one.
For x <= 1/640: (1 + x)^64 - 1 <= e^(64x) - 1 <= 64 x e^(64x) <= 64 e^(0.1) x <= 71 x, so the map sends x to at most 5041 x^2. If 5041 s < 1, induction gives 5041 s_k <= (5041 s)^(2^k), and all s_k stay below 1/5041 < 1/640. The top eigenvalue is simple, so r_1^(n_k) <= s_k and m((2 n_k)^3) >= (1/n_k) log(1/s_k) >= (1/n_k)(2^k log(1/(5041 s)) + log 5041) >= log(1/(5041 s))/n. Last claim: exp(1.9 x 10^(-4)) - 1 < 1.91 x 10^(-4) < 1/5041. QED

**Corollary S2 (two dimensions, same proof with one doubling).** For a symmetric W as above: S(2n; 4n) <= ((1 + S(n; 2n))^4 - 1)^2. If S(n; 2n) <= 1/20, then S(2n; 4n) <= 19 S(n; 2n)^2 and the circles of length 2^(k+1) n have gap at least log(1/(19 S(n; 2n)))/n. (For x <= 1/20: (1 + x)^4 - 1 <= 4.32 x, and 4.32^2 < 19.) This is a statement for every model on the square lattice that satisfies the setting of the lemmas. For the O(3) sigma model that setting is plausible by the argument of `gap-transfer.md` and is not proved here (scope corrected, row 698).

**Corollary S3 (all cubes from a seed on one block of sizes; PROVED).** Theorem S holds with (a, b) in place of (n, 2n) whenever 3 <= a <= b/2: S(2a; (2b)^3) <= ((1 + S(a; b^3))^64 - 1)^2. So let N >= 3 and s_max := the maximum over the integers b with 2N <= b < 4N of S(floor(b/2); b^3). If s_max < 1/5041, then every cube of side L >= 2N has m(L^3) >= log(1/(5041 s_max)) / (2N).

Proof. For a <= b/2 the exponent 2b/(b - a) of Lemma E is at most 4, and the pair (2a, 2b) has the same property; the proof of Theorem S is unchanged. Every integer L >= 2N is 2^k b with one b in [2N, 4N); apply the recursion from (floor(b/2), b), and use floor(b/2) < 2N. QED

**Correction (row 699, Codex gpt-6-astra).** The last sentence of this proof is false. Not every integer L >= 2N is 2^k b with an integer b in [2N, 4N): take N = 3 and L = 13. The check of row 698 accepted the step; the check of row 699 is right. As proved above, Corollary S3 covers only the sides 2^k b. The conclusion holds for every integer side, and from one seed, by the next two statements. They are written by Codex gpt-6-astra (`library/gap-seed-check-astra.md`, point 8). The lead (Claude Fable 5.2) re-derived both line by line and found no error.

**Lemma E' (row 699).** For integers h >= b > a >= 3: 1 + S(a; h) <= (1 + S(a; b))^(h/(b - a)).

Proof. By Lemma A (a) for T_a and h >= b: W(a, h) = Tr T_a^h <= (Tr T_a^b)^(h/b) = W(a, b)^(h/b). Take logarithms: a e(h) + g(a, h) <= (h/b)(a e(b) + g(a, b)). The terms ell a h cancel, and kappa(h) >= 0 (Lemma K (b)). So g(a, h) <= (a h / b) kappa(b) + (h/b) g(a, b). By Lemma X, kappa(b) <= g(a, b)/(b - a). So g(a, h) <= (h/b)(a/(b - a) + 1) g(a, b) = (h/(b - a)) g(a, b). QED

**Corollary S3' (every cube from one seed; row 699).** Let N >= 3 and s = S(N; (2N)^3) < 1/5041, q = 5041 s. Then for every integer L >= 2N: m(L^3) >= log(1/q)/N. More exactly, with k >= 0 such that D := 2^(k+1) N <= L < 2D: S(D/2; L^3) <= q^(2^k)/71.

Proof. By Theorem S, S(D/2; D^3) <= s_k = q^(2^k)/5041. Apply Lemma E' with a = D/2, b = D, h = L three times, once in each direction, with the other two sides fixed at (D, D), then (L, D), then (L, L). Each exponent is L/(D - D/2) = 2L/D < 4. So 1 + S(D/2; L^3) <= (1 + s_k)^64, and S(D/2; L^3) <= 71 s_k = q^(2^k)/71 by the estimate in the proof of Theorem S. The lowest excited eigenvalue ratio rho_1 of the cube of side L obeys rho_1^(D/2) <= S(D/2; L^3), and D/2 = 2^k N. So m(L^3) >= (2^k log(1/q) + log 71)/(2^k N) >= log(1/q)/N. QED

So seeds at other block sizes are not needed.

**What Theorem S is and is not.**

- It is a finite criterion on periodic tori, with no boundary values and no complex coupling. One inequality between two partition functions at one size gives a gap that is uniform on the cubes of side 2^(k+1) n. Their limit is a volume-first limit along a sequence. Cubes of other sides need seeds on a block of sizes (Corollary S3), or they are multiples: Lemma E with W(a, jb) <= W(a, b)^j gives the exponent j b/(b - a), so the cube of side 2 j n_k has m >= (1/n_k) log(1/(14 j^3 s_k)) when 14 j^3 s_k < 1. Boxes that are not cubes are not treated.
- There is an exact alternative: either S(n; (2n)^3) >= 1/5041 for every n >= 3, or the dyadic cubes from some size on have a uniform gap. In the first case Phi(n) >= 1.98 x 10^(-4) for every n. I did not prove that a uniform gap forces the second case (it needs a bound on the number of states).
- It holds for every group and for every symmetric model with positive transfer operators. The test: U(1) at weak coupling has s >= 12 exp(-pi) (1 - o(1)), about 0.52 (the photon, RECALLED). Z_2 at its transition has s >= 1 - o(1) (two phases, RECALLED). Z_2 at large beta has s >= 7 - o(1) (eight flux sectors, RECALLED). The seed is false in all three, and it must be.
- The gap is on the whole space of the box, flux sectors included. So the seed is the gap with confinement at one finite size.
- Why it is consistent that no large light object can appear later: by (LB) a periodic torus never has less free energy per volume than the bulk. A sector that does not fit into small tori cannot add pressure in the bulk. Lemma K is the sharp form of this.
- Two sanity runs (guides only; a run can refute and cannot discharge). Run 1: transfer matrices of the Ising model at six couplings and of the 3-state Potts model at four couplings on rings up to 10 and 6 sites. No violation of the symmetry, of Lemma K (with the exact free energy of Onsager for Ising), of Lemma X, of Lemma E or of Corollary S2 was found; the smallest margin in Lemma X was 1.2 x 10^(-6). Run 2: the Ising model in three dimensions, boxes (b, c) with b up to 6 for c = 2 and up to 4 for c = 3, five couplings: no violation of the symmetry, of the convexity of e in b, or of Lemma E with the side c fixed. Scripts: check2d.py and check3d.py in /tmp/gap-crux-restate-scratch on the Mac mini, not kept in the repository. The proofs above do not use the runs.

## 4. Part 2, attempt 2: the flux half (C2; lead (a))

### 4.1 Theorem F (PROVED from (TM), (TM-c), Lemma A, (LB))

Torus with sides (a, b | c, d) in the directions (1, 2 | 3, 4), twist in the plane (1,2), Z_odd = (Z - Z^(12))/2, Z_even = (Z + Z^(12))/2, u = Z_odd / Z, v = Z_odd exp(-f |n|).

- (a) Z_odd = Tr(T_1^a P_2) = Tr(T_2^b P_1), where T_mu is the transfer operator in direction mu and P_nu = (1 - C_nu)/2 is the projection on the odd subspace of C_nu. So 0 <= Z_odd < Z_even.
- (b) Z_odd(ja, kb | c, d) <= Z_odd(a, b | c, d)^(jk) for all integers j, k >= 1.
- (c) v(ja, kb | c, d) <= v(a, b | c, d)^(jk), and u <= v on every torus.
- (d) If v(a_0, b_0 | c, d) < 1, put sigma = log(1 / v(a_0, b_0 | c, d)) / (a_0 b_0). Then u(j a_0, k b_0 | c, d) <= exp(-sigma (j a_0)(k b_0)) for all j, k >= 1.
- (e) If v >= 1 on every torus (a, b | c, d) with the same c, d, then for every a the top eigenvalue mu_0(a) of T_2 on the odd subspace of the slice (a, c, d) satisfies log mu_0(a) >= f a c d. So the flux energy log(lambda_0(a)/mu_0(a)) is at most the deficit log lambda_0(a) - f a c d of that slice, for every a.

Proof. (a) (TM-c) for the pairs (mu, nu) = (1, 2) and (2, 1); Z^(12) is symmetric in the two directions and positive. (b) P_2 commutes with T_1, so T_1 P_2 is a positive trace-class operator and (T_1 P_2)^a = T_1^a P_2. Lemma A (a) gives Tr (T_1 P_2)^(ja) <= (Tr (T_1 P_2)^a)^j. This is the step in direction 1. On the torus (ja, b | c, d) do the same in direction 2 with T_2 P_1. (c) f |n| is multiplied by jk; u <= v is (LB). (d) from (c). (e) Z_odd(a, b)^(1/b) tends to mu_0(a) as b grows (Lemma A (a)), and v >= 1 says Z_odd(a, b)^(1/b) >= exp(f a c d). QED

What it says. The doubling of run 1's Lemma 4 carries an entropy term because it uses the ratio Z_odd / Z_even. With the bulk constant f in place of Z_even there is no entropy term. For fixed transverse sides there is an exact alternative: either one torus has v < 1, and then the odd-flux weight decays like the exponential of the area of the face (1,2) on all its multiples; or the flux energy never exceeds the deficit of the slice. With the Tomboulis-Yaffe inequality (GUIDE: Kanazawa, Theorem 1: the Wilson loop of a rectangle C in the plane (1,2) is at most 2 u^(A_C / (n_1 n_2))) case one is the area law, with tension sigma, on Z^2 times the transverse torus. This is close to node T3 (b) of the final skeleton; I did not open its source, and the proof above does not use it.

Theorem F does not reach four dimensions. The tension sigma depends on (c, d). The four-dimensional statement is (FLUX-4) of Part 1.

### 4.2 How C1 and C2 are tied

v = u exp(Delta) on every torus. By Theorem D (e), on the torus (2n)^4: u <= S(2n; (2n)^3) <= S(n; (2n)^3)^2. So under the seed of Theorem S the odd-flux weight of the dyadic symmetric tori is at most s_k^2, which falls like an exponential of the side and not of the area. And C2 says nothing about the zero-flux sector. The gap and the area law are two statements. The gap half now has its step (Theorem S); the flux half has not.

### 4.3 The transverse step (TUBE): what it would give, where it fails, three ways that failed

**(TUBE).** There are K >= 1 and n_0 such that on all tori with all sides at least n_0: Z_odd(a, b | 2c, d) <= K Z_odd(a, b | c, d) Z(a, b | c, d), and the same with d doubled.

In words: when the transverse section is doubled, the odd flux sits in one of the two halves, and the other half is in its vacuum. The flux does not gain by spreading over both.

**Proposition T (PROVED implication).** Assume (TUBE), and D := sup over L >= L_0 of Delta(L, L, L, L) finite, with L_0 >= n_0. Put M = K^8 exp(12 D). If v(L_0, L_0 | L_0, L_0) < M^(-1/3), then with sigma = log(1/(M^(1/3) v(L_0^4))) / L_0^2 and L = 2^k L_0:

u(L, L | L, L) <= v(L, L | L, L) <= exp(-sigma L^2) for all k >= 0.

Proof. (TUBE) and the definition of v give v(a, b | 2c, d) <= K exp(Delta(a, b, c, d)) v(a, b | c, d). So v(L, L | 2L, L) <= K exp(Delta(L^4)) v(L^4), and v(L, L | 2L, 2L) <= K exp(Delta(L, L, 2L, L)) v(L, L | 2L, L) <= K^2 exp(3 Delta(L^4)) v(L^4), because doubling one side at most doubles Delta. Theorem F (c) with j = k = 2 gives v((2L)^4) <= v(L, L | 2L, 2L)^4 <= M v(L^4)^4. So M^(1/3) v((2^k L_0)^4) <= (M^(1/3) v(L_0^4))^(4^k). QED

So one seed, (TUBE), and a bounded excess free energy give (FLUX-4) on dyadic symmetric tori. The seed is one inequality between three partition functions and the number f.

**(TUBE) against U(1) (estimate at Gaussian order, not a proof).** For the Gaussian weight, Z_odd / Z_even is about 2 exp(-x) for large x, with x = (g^2/2) a b / (c d): the flux spreads over the section, and its energy falls like the inverse of the section. Doubling c halves x. The ratio of the two sides of (TUBE) is then about exp(x/2 - R), where R = 2F(c) - F(2c) is the doubling defect of the photon gas in direction 3, about 0.41 a b d / c^3 when c is the shortest side. So the ratio is exp( (a b / (c d)) (g^2/4 - 0.41 d^2/c^2) ), which is unbounded in a b when d < 0.78 g c. (TUBE) for all shapes is false for U(1): it fails on sections that are thin in the direction that is not doubled. On square sections at weak coupling the estimate does not refute it, and there the seed fails instead (u is near 1/2).

**Way 1: positivity.** In direction 3, Z and Z^(12) are traces of two operators on two spaces, T^c on the periodic slice and T_tw^c on the slice with the twist. Z_odd is half their difference, and Lemma A gives only Z(2c) <= Z(c)^2 and Z^(12)(2c) <= Z^(12)(c)^2. With Z_even in place of Z and K = 2, (TUBE) is

(TUBE') Z(c)^2 - Z(2c) >= Z^(12)(c)^2 - Z^(12)(2c), that is, Tr Lambda^2(T_tw^c) <= Tr Lambda^2(T^c),

because Z^2 - (Z^(12))^2 = 4 Z_odd Z_even and (Tr S)^2 - Tr S^2 = 2 Tr Lambda^2 S. The first elementary symmetric function obeys the same inequality (Z^(12) <= Z). Positivity gives nothing for the second: the two operators act on different spaces and no map between them is known that is positive.

**Way 2: reflection positivity across the section.** Let c be even, and split the stack of twisted plaquettes into two halves H and theta H by two reflection planes that bisect links of direction 3. Put G_H = product over p in H of exp(-beta tr U_p), so Z^(12)/Z is the expectation of G_H times theta G_H, and put tau = expectation of G_H. Reflection positivity in direction 3 (the input behind (TM)) and the Schwarz inequality give tau^2 <= Z^(12)/Z, so u <= (1 - tau^2)/2. This is an upper bound on the odd-flux weight, of the right direction. But G_H is a stack with a boundary, a pair of 't Hooft loops, and the only lower bound that I have for tau is Jensen's, exp(-2 beta (1 - abar) |H|) with |H| = c d / 2. For c and d powers of two, iterating the reflection in the directions 3 and 4 down to single plaquettes gives Z^(12)/Z >= (expectation of exp(-beta tr U_p))^(c d): a cost per plaquette of the section. It is the trivial bound. It does not see that the stack can be moved for free.

**Way 3: move the flux into one half by a deformation.** By Lemma J every such deformation pays beta (1 - abar) (1 - product of normalised corner traces) per plaquette. A deformation that is not a gauge transformation times a centre field pays on a set of plaquettes of positive density.

**Remark F3 (the same lemmas in the transverse plane; PROVED given a transfer operator for the twisted slice).** (Row 698, point 10: this input, (TM) for the twisted action, is supplied by Lemma 1.1 of `library/gap-seed-check.md`. One model checked this.) For fixed (a, b), both Z and Z^(12) are symmetric in (c, d), and each is a trace in c and in d (for Z^(12) the twisted plaquettes are spatial, so the transfer operator has the same form; this input is (TM) for the twisted action and is not in row 667). So Lemmas K and X apply to both. With tau(a, b) := ell(a, b) - ell_tw(a, b) >= 0, the difference of the two free energies per unit of transverse area, and f_m = log(Z / Z^(12)): for c < d,

-(d/(d-c)) g_tw(c; d) <= f_m(a, b | c, d) - tau(a, b) c d <= (d/(d-c)) g(c; d),

where g and g_tw are the logarithms of 1 plus the thermal sums of the untwisted and the twisted box (d, a, b) at time c. So the cost of the twist is linear in the transverse area up to thermal sums, and the area law is the statement that tau(a, b) falls like exp(-sigma a b). The limit of this remark: the errors are of the size of the gap terms, exp(-m c), which is far above exp(-sigma a b). The area law needs the difference g - g_tw, and the lemmas do not give it.

**Stop.** (TUBE) failed in three ways. The one exact next statement of this attempt is (TUBE'), for tori with square section: prove it, or find a torus on which it fails for SU(2). It is one inequality between four partition functions, and it can be tested by a run before any proof is tried.

### 4.4 Where the group sits in the flux weight (an exact identity, PROVED; no attempt)

Write U_l = s_l V_l with s_l = +-1 and V_l in a measurable section of SU(2) over SO(3). Haar measure is the product. (1/2) tr U_p = s_p J_p(V), with s_p the product of the four signs and J_p(V) = (1/2) tr of the product of the V_l around p, a number in [-1, 1]. For fixed V this is a Z_2 gauge theory with couplings beta J_p(V). The twist changes the sign of s_p on the stack, so it acts on the Z_2 part only. So

u(SU(2), beta) = expectation over V of u(Z_2 with couplings beta J(V)), where V has the law with density Z_(Z_2)[beta J(V)] / Z.

The odd-flux weight of SU(2) is the mean of the odd-flux weight of a Z_2 gauge theory in a random SO(3) environment (Mack and Petkova, GUIDE, use this splitting for Wilson loops). For the group Z_2 the environment is trivial and J = 1. For SU(2) the environment can make J_p small and can change its sign. This is the place where Fact T acts: a twist of the SO(3) field costs no classical action. No bound follows from the identity alone.

## 5. The leads (a) to (d), and the verdict

**Lead (a), the twist ratio and the Tomboulis-Yaffe inequality.** Its exact form here is C2 with Theorem F and Proposition T. The inequality holds for every group. Its premise is the confinement half of the crux. A premise taken from a Migdal-Kadanoff comparison does not pass test (ii): that recursion drives U(1) to strong coupling in four dimensions as well (RECALLED; this is the objection of Ito and Seiler to the argument of Tomboulis, known here from the digests only). The transverse step (TUBE') is open.

**Lead (b), seed and doubling.** The answer is yes, for the gap.

1. The statement: Theorem S. If Phi(n) <= 1.9 x 10^(-4) at one size, all cubes of side 2^(k+1) n have a gap of at least 0.04/n. The doubling step is proved by hand from the positivity of the transfer operators and the symmetry of the torus. It uses no property of the group.
2. Why it fails for U(1): the seed is false at every size, because the photon keeps Phi above 0.04 (about 0.41 with its twelve lowest states). For Z_2 the seed is false at the transition and at large beta.
3. For the flux (the area law) the analogous step is (TUBE'), and it is open. Theorem F gives the two directions of the sheet only.

The abstract of Ursachi's preprint reports a criterion of this shape for the O(3) sigma model in two dimensions. Corollary S2 is a criterion of this shape for every reflection-positive model in two dimensions. Nobody here has read the body of the preprint, so I cannot say if the two are the same argument. Nothing in this file is taken from it beyond the idea that the defect of doubling can be the criterion.

**Lead (c), two-scale disintegration.** In two dimensions the plaquettes are independent after an axial gauge fixing, so the two scales are one plaquette and a product measure. In four dimensions the Bianchi constraint ties the plaquettes of every cube. A two-scale criterion then needs a small coupling between the scales, and that is a mixing statement of the kind of (W). I see no new handle (abstract only).

**Lead (d), logarithmic Sobolev inequality and mixing.** It is an equivalence between two forms of one hypothesis. It could carry (W) to a uniform Poincare constant, and so toward (HS-sup). It is not a mechanism.

**Verdict.**

1. The crux of the gap on periodic boxes now has a finite form with no boundary values: (SEED), one inequality between the partition functions of two tori at one size. The passage from that size to all dyadic sizes is Theorem S. If the check confirms it, the open content of C1 is the seed alone.
2. The seed is still the whole difficulty at couplings of order one. By the rate filter it sits at a size of the order of the correlation length (for a gas of one scalar particle of mass M, s is about 0.5 (M n)^(3/2) exp(-M n), and s < 1/5041 needs M n of about 12; an estimate). The group enters there and nowhere else. I found no exact tool in which the group acts at couplings of order one. The exact tools of this lane (positivity in four directions, the centre flips, reflection positivity, first-order comparison, the finite-box criterion, and now Lemma K) hold for every compact group with a central Z_2. Run 1's third test says the same from outside: SU(2) with an adjoint Higgs field has the centre, reflection positivity and Fact B, and it has a phase with a photon (RECALLED there).
3. What the seed is: 96 n^4 times the integral over the coupling of the difference of the plaquette averages on the tori (2n)^4 and n^4 is at most 1.9 x 10^(-4). On the strong-coupling disc it can be proved by hand (item 2 below). At couplings of order one I know no method by hand. A direct Monte Carlo measurement cannot reach the threshold either: at n = 4 and beta = 2.3 the plaquette difference would have to be known to about 3 x 10^(-9). A run can measure Phi where it is of order 0.01 or more, and the seed size can be estimated from the measured masses and string tension. Such numbers are guides.
4. In the scaling form the seed is one statement about the continuum family: at one physical size L_0 the doubling defect is below 1.9 x 10^(-4), uniformly in the cutoff. Then the gap is at least 0.04/L_0. This is the cleanest form of the crux that I can give: it has one size, no boundary values, no complex coupling and no free walls.
5. The flux half is not closed by Theorem S. The seed bounds the odd-flux weight with the rate of the gap, not with the area. For the area law the open step is (TUBE').

**What changes in the plan (the author's reading; the lead decides).**

- Theorem S needs its check before anything is built on it. It is short (Lemmas K, X, E and ten lines), so two checks by two providers are cheap. The points to attack: Lemma K (d) (the deficit is non-increasing), the use of the symmetry of Z for each pair of directions with the other two sides fixed, and the place where multiplicity at least one is used.
- If it holds, the tree has a third conditional form next to (W) and (DOM_B): the account, with (SEED) in the scaling form, gives a gap of periodic cubes that is uniform in physical units. Its inputs are (TM) and the scale function only. It does not need (2L), (SCAL_B), (CP), free walls or a complex neighbourhood. The limit along dyadic cubes is a volume-first limit along a sequence; the identification with other sequences is the same uniqueness question as before (T7, Z10).
- I do not recommend another restatement run on the gap half. The next real step there is a proof of the seed, and for that one of these is needed: a correlation inequality of Griffiths type for SU(2); a dual representation with positive weights; or a monotone quantity along the scale. None is known to me.

## 6. Part 3: status block (final)

**Proved here by hand. Checked line by line by Claude Opus 5.5 (row 698; Sections 1, 3, 4) and by Codex gpt-6-astra (row 699; Sections 1, 3.1, 3.4). No statement fails; the corrections are applied in the text. The proof step of Corollary S3 was false and is replaced by Lemma E' and Corollary S3' (Section 3.4).** Inputs: (TM) and (TM-c) (rows 667, 671; run 2, Lemma 1'), Lemma A (run 2, Lemma 1), and the invariance of Z under permutations of the four sides.

| Statement | Content | Section |
|---|---|---|
| Lemma K | the deficit kappa(b) = e(b) - ell b of the ground state is non-negative, convex and non-increasing in b | 3.4 |
| Lemma X | (b - a) kappa(b) <= log(1 + S(a; b)) for a < b | 3.4 |
| Lemma E | 1 + S(a; 2b) <= (1 + S(a; b))^(2b/(b-a)) for a < b | 3.4 |
| **Theorem S** | S(2n; (4n)^3) <= ((1 + S(n; (2n)^3))^64 - 1)^2; a seed S(n; (2n)^3) < 1/5041, or Phi(n) <= 1.9 x 10^(-4), gives a uniform gap on the cubes of side 2^(k+1) n | 3.4 |
| Corollary S2 | the same in two dimensions: seed S(n; 2n) <= 1/20 | 3.4 |
| Corollary S3 | seeds on one block of sizes 2N <= b < 4N give a uniform gap on the cubes of side 2^k b (as first stated, on every cube: that proof step was false, row 699) | 3.4 |
| Lemma E', Corollary S3' | one seed s = S(N; (2N)^3) < 1/5041 gives m(L^3) >= log(1/(5041 s))/N on every cube of integer side L >= 2N (row 699) | 3.4 |
| Theorem D | Phi(n) = 16 F(n^4) - F((2n)^4) bounds the thermal sum, the gap, the count of states and the odd-flux weight of the box (2n)^3; Phi is an integral of plaquette differences | 3.1 |
| Corollary D2, Proposition R | consequences of a decay of Phi; the reach of a seed for Delta | 3.1, 3.2 |
| Proposition N, Remark N2 | the step fails for positive measures without integer multiplicity; the place is the doubling of the time | 3.3 |
| Lemma J, seam bound | exact first-order value of a deformed or glued plaquette; Phi(n) <= beta (192 n^3 - 96 n^2)(1 - abar_n) | 3.3 |
| Theorem F | v = Z_odd exp(-f abs(n)) obeys v(ja, kb) <= v(a, b)^(jk); a seed v < 1 gives area decay of the odd-flux weight on all multiples; the alternative (e) | 4.1 |
| Proposition T | (TUBE), a bounded Delta and one seed give (FLUX-4) on dyadic symmetric tori | 4.3 |
| Identity 4.4 | the odd-flux weight of SU(2) is a mean over SO(3) environments of the odd-flux weight of a Z_2 theory | 4.4 |

**Failed, and why.**

- Three ways to the doubling step of the gap failed before the fourth worked: positivity without integer multiplicity (Proposition N), gluing (the exact surface term), deformation (Lemma J). They are kept as a record.
- (TUBE), in the form (TUBE'): the odd-flux weight is not a trace in the transverse directions; reflection positivity across the section gives only a cost per plaquette of the stack; deformation fails by Lemma J. At Gaussian order (TUBE) is false for U(1) on thin sections (estimate, not proved).
- The seed at couplings of order one: no attempt was made, because I have no tool to try.

**The one exact next statement of each attempt.**

- Attempt 1: (SEED), in the scaling form of C1. On the strong-coupling disc first (item 2).
- Attempt 2: (TUBE') of Section 4.3 on tori with a square section.

**Not done.** The bodies of `gap-zf-box-x.md`, `gap-zf-box-s.md` and `gap-ac-lat.md` were not read. Two numeric jobs were run under the numeric lock, at 64 percent free memory: the sanity runs of Section 3.4 (each under two minutes, at most 700 MB); they are guides. The Gaussian estimates for U(1) (the photon bounds, the value 0.41 of the defect of the photon gas, the threshold 0.78 g) are estimates from recalled formulas; no proof uses them. The Tomboulis-Yaffe inequality is not rebuilt here; the area law in Theorem F and Proposition T is stated for the odd-flux weight, and for Wilson loops only through that GUIDE. A converse of Theorem S (a uniform gap gives the seed) is not proved.

**Proof items for the medium workers.**

1. `gap-seed-check` (worker 2, check; first). Check line by line Lemmas K, X, E, Theorem S and Corollary S2, then the other rows of the table. Inputs: the statement of (TM) in `library/gap-transfer.md` and its check; `gap-skeleton-max-b.md` lines 241-256. Read: Sections 1, 3, 4 of this file. Points that carry weight: (i) Lemma K (c), (d): convexity of e from the crossed direction, and the step from convexity to monotonicity; (ii) the symmetry W(a, b) = W(b, a) for each pair of directions with the other two sides fixed, and that the transfer operator of the row 667 exists for every box with sides at least 3; (iii) multiplicity at least one in S(2k; B) <= S(k; B)^2; (iv) Theorem D (e) uses that the top eigenvector is even under the centre flips. Because the theorem carries the new form of the crux, a second check by another provider is worth its cost.
2. `gap-seed-sc` (worker 1, proof). Prove (SEED) on a strong-coupling disc with explicit constants: there are r_1 > 0 and C with Phi(n; beta) <= C n^3 (beta / r_1)^(4n) for 0 <= beta <= r_1 and n >= 3 (the periodic form of Theorem SC; 4n plaquettes is the smallest tube that winds once; corrected, row 701: this holds for n >= 4 only. On the torus 3^4 the smallest winding set is a plane of 9 plaquettes and Phi(3; beta) has exact order beta^9. The right exponent is e(n) = min(4n, n^2). Proved in `library/gap-seed-sc.md` with r_1 = 1/12800: abs(Phi(n; beta)) <= 0.16 n^4 (12800 abs(beta))^(e(n)); the seed and the gap follow there for beta < 1/12800. Checked line by line by Claude Opus 5.5 high, row 704, `library/gap-seed-sc-check.md`: every statement holds). With Theorem S this is a proof by hand of a uniform gap of periodic cubes at strong coupling that uses no cluster expansion beyond one size. Consumer: the base of C1 and a cross-check of Theorem S against kappa_0 = 4 log 2. Read: `library/gap-sc-box.md`, Theorem SC and its polymer bounds.
3. `gap-seed-guide` (guide; reading and a small run). (a) From published values of the glueball mass and the string tension at beta between 2.2 and 2.6, estimate the size n at which S(n; (2n)^3) falls below 1/5041, as the sum over one-particle states and flux states. (b) Under the numeric lock, measure Phi(n; beta) by Theorem D (f) for n = 3, 4 where it is above 0.01, for SU(2) and for U(1), and compare the decay in n with (a). Write the pass and fail criteria first. Prediction for U(1) at beta above 1.01: Phi stays above 0.4. What it can show: where the seed sits. It can show no proof step.
4. `gap-seed-shape` (worker 1, proof, small). Improve the constant of Theorem S by the choice of shape: with time n and box side r n the exponent of one doubling is 2r/(r-1), and r = 3 gives the map x -> ((1+x)^27 - 1)^2. State the best seed in terms of Phi for a torus (n, rn, rn, rn), with the analogue of Theorem D (b). Also treat boxes that are not cubes. Consumer: the size of the seed in item 3.
5. `gap-tube-test` (worker 1, proof, then guide; low priority). Decide (TUBE') on tori (a, b | c, c) in the strong-coupling disc: expand both sides in polymers and find the sign of the first order at which they differ. Consumer: Proposition T. (TUBE') is needed at every scale, so this does not close C2.
