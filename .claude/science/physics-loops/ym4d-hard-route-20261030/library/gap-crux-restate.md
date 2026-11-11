lead: anthropic/claude-fable-5-2/max mac-mini-worker
lease_until: 2026-11-11T19:45Z

# The crux of the mass gap, restated (row 697, `gap-crux-restate`)

Author run, started 2026-11-11T07:45Z at commit 51785e8cb. Research-stage working state. Nothing here is a claim of a mass gap.

Status of this file: in progress. Sections are appended as each step ends. The status block (Part 3) is kept current.

**No mass gap is proved here.** Nothing in this file is checked by a model that did not write it.

## 0. Position, repo search, reading state

**Kind of result.** Proofs of steps that the two max plans left as algebra or as remarks (Theorems D, F, Lemma J, Proposition R), a new exact form of each soft half of the crux, and one named lemma per attempt with the ways it failed. No new mechanism for couplings of order one was found. Section 5 says this in plain words.

**Repo search (rule 0a), done before the attempts.** Searched `library/gap-*.md`, `library/prior/gap-*.md`, `library/open-core.md` for: Knabe, frustration, heat bath, subadditiv, Renyi, step scaling, Simon-Lieb, chessboard, Mack, vortex, Casimir, doubling. Matches that bind this file:

- Run 1 (`gap-skeleton-max.md`): Lemma 4 (doubling identities with entropies, lines 262-275), crux (F) (line 126), B7 (the Knabe threshold, lines 159-164, excluded there by the rate filter). I do not attack B7 again.
- Run 2 (`gap-skeleton-max-b.md`): A1 and crux (FE) (lines 140-147), Section 1.5 (lines 241-282): Lemma 1 (a)-(d), Lemma 1', Lemma 2, the crossing identity, and the named failure Lemma NSM. A5 (STEP), A9 (SL).
- Row 691 (`gap-ds-gauge.md`): Theorem W, Propositions B and S.
- So the torus algebra and the flux doubling are not new here. What is added: the form with no infinite-volume constant (Theorem D), the form with no entropy term (Theorem F), the exact first-order identity (Lemma J), and the closed statements (Phi-step), (TUBE).

**Read for this file.** FINISH row 697; `gap-skeleton-final.md` whole; the passages above; `gap-ds-gauge.md` 3.1, 4, 6; `prior/gap-crux-lit-2.md` headings, T7, C5 (the seed criterion), the synthesis tables and "Routes bounded". **Not read:** the bodies of `gap-zf-box-x.md`, `gap-zf-box-s.md`, `gap-ac-lat.md` (their statements are taken from Sections 12-13 of the final skeleton); every primary paper. Nothing was fetched from the network.

**Credits.** Sussman and Alpoge with Claude and Codex (the account; not used in any proof below). Run 1 and run 2 of Claude Fable 5.2 max (Lemma 4; Lemma 1, 1', 2, crossing, NSM). Osterwalder and Seiler, Luscher (transfer operator, through row 667). 't Hooft (twists and flux). Tomboulis and Yaffe, Kanazawa (the inequality; GUIDE here). Ursachi (the idea of a doubling defect as the criterion; abstract only, GUIDE). Mack and Petkova (the Z_2 and SO(3) splitting; GUIDE).

**Marks.** PROVED = proved by hand in this file from the named inputs, not checked. GUIDE = a statement of a paper, recalled, used in no proof. RECALLED = a known fact used only in a test (ii).

## 1. Setting and inputs

Torus with sides n = (n_1, ..., n_4), all n_mu >= 3. Action A(U) = sum over plaquettes of (1 - (1/2) tr U_p). Z(n) = integral of exp(-beta A) over Haar measure, F(n) = log Z(n), |n| = n_1 n_2 n_3 n_4. beta > 0 is fixed unless said.

**(TM)** (input; `library/gap-transfer.md`, row 667, check row 671). For each direction mu and each choice of the other three sides there is a positive trace-class operator T on a Hilbert space with Z(n) = Tr T^(n_mu). Its largest eigenvalue is simple, with a strictly positive eigenfunction.

**(TM-c)** (input; run 2, Lemma 1'). For nu different from mu, the centre flip C_nu (multiply by -1 every link of direction nu that crosses the plane x_nu = 0 of the slice) is a unitary involution that commutes with T, and Tr(T^(n_mu) C_nu) = Z^(mu nu)(n). Here Z^(mu nu) is the partition function with the sign of beta changed on one stack of (mu,nu)-plaquettes, one plaquette for each value of the other two coordinates. It is positive, and it is symmetric in mu and nu.

**Lemma A** (run 2, Lemma 1 (a), (b); two-line proofs there). Let S >= 0 be trace class with eigenvalues lambda_0 >= lambda_1 >= ... . (a) k -> (Tr S^k)^(1/k) is non-increasing and tends to lambda_0. So Tr S^(jk) <= (Tr S^k)^j for integers j, k >= 1. (b) lambda_0^k >= Tr S^(2k) / Tr S^k.

**Consequences used below** (run 2, Lemma 1 (c)). F(n)/|n| is non-increasing in each side. f := inf over n of F(n)/|n| is finite, and

(LB) Z(n) >= exp(f |n|) for every torus.

Delta(n) := F(n) - f |n| >= 0 is the excess free energy. Multiplying one side by an integer j multiplies Delta by at most j.

For the box B = (n_2, n_3, n_4) with transfer operator T in direction 1, eigenvalues lambda_0 > lambda_1 >= ..., put r_i = lambda_i / lambda_0, S(k; B) = sum over i >= 1 of r_i^k, and m(B) = log(lambda_0 / lambda_1). Then r_1^k <= S(k; B) and S(k + k'; B) <= S(k; B) S(k'; B).

## 2. Part 1: candidate statements of the crux

The object in every candidate is the Wilson SU(2) measure at one real beta. "Uniform" means: constants do not depend on the torus or box. For the tree, each statement is needed in the scaling form: for beta >= beta_1 with rates proportional to the scale function a(beta), and on [r_0, beta_1] with fixed rates (final skeleton, Sections 4 and 13.6).

The test (i)-(iii) has the same answer to (i) for all five. I give it once.

**(i) for all five.** The group enters the definitions through two facts only. Fact T: the single-plane twist has classical cost zero for SU(2), because iσ_1 and iσ_2 anticommute (run 1, Facts 1-3). For U(1) the same twist costs beta pi^2 n_3 n_4 / (2 n_1 n_2) at Gaussian order, and for Z_2 it costs 2 beta n_3 n_4. Fact B: the one-loop coefficient b_0 = 11/(24 pi^2) is positive. No exact inequality found here or in the sources uses Fact B at couplings of order one. So in every candidate the group enters the proof only at the step that is still open. I found no candidate for which this is not so.

**C1. Two tori per scale (new form; not Route T, not Route Z, not a finite-box criterion).** Put

Phi(n) := 16 F(n,n,n,n) - F(2n,2n,2n,2n) >= 0, the free-energy defect of doubling the symmetric torus.

- (Phi-dec): there are C, c > 0 with Phi(n) <= C exp(-c n) for all n >= C.
- (Phi-step), the form with a seed: there are eps_0 > 0, K and n_0 with: Phi(n) <= eps_0 and n >= n_0 give Phi(2n) <= K Phi(n)^2.
- What it gives (Theorem D, Corollary D2, PROVED): (Phi-dec) gives m((2n)^3) >= c - log(2C)/n. (Phi-step) with one seed Phi(n_1) < min(eps_0, 1/K), n_1 >= n_0, gives m((2^k n_1)^3) >= log(1/(K Phi(n_1))) / n_1 for all k >= 1. The gap is on the whole space, flux sectors included, so it also bounds the odd-flux weight.
- It is run 2's (FE) with the infinite-volume constant removed: each scale is one inequality between two partition functions, and Phi(n) = 96 n^4 times the integral over [0, beta] of (abar_2n - abar_n), with abar_n the mean plaquette action on the n^4 torus.
- (ii) U(1) at weak coupling: the periodic box has an excited state of energy at most (2 pi / side)(1 + o(1)) (RECALLED, the photon; run 2's K5). By Theorem D (c), read backwards, Phi(n) >= log(1 + exp(-n m((2n)^3))) >= log(1 + exp(-pi - o(1))) > 0.04. With the twelve lowest photon states of the box (six momenta, two polarisations, energy pi/n each; RECALLED) Theorem D (b) gives Phi(n) >= log(1 + 12 exp(-pi)) - o(1), about 0.41. So (Phi-dec) is false, and no seed below these values exists. Z_2 at its transition: two phases, so m(box) tends to 0 (RECALLED) and Phi(n) >= log 2 - o(1). Z_2 at large beta: the flux sectors are degenerate with the vacuum (RECALLED), same bound; this is why C1 is the gap with confinement.
- (iii) Theorem D holds for every group. The step (Phi-step) is not a consequence of positivity alone (Proposition N); with integer multiplicities it is undecided (Remark N2).

**C2. Flux on tori with normalised bulk (the published lead (a) in exact form).** Twist in the plane (1,2). Z_odd(n) := (Z(n) - Z^(12)(n))/2, u(n) := Z_odd(n)/Z(n), v(n) := Z_odd(n) exp(-f |n|), so 0 <= u <= v (by (LB)).

- (FLUX-4): there are sigma > 0 and L_0 such that for every L >= L_0 there is a torus (a, b | L, L) with v(a, b | L, L) <= exp(-sigma a b).
- What it gives (Theorem F, PROVED): u(ja, kb | L, L) <= exp(-sigma (ja)(kb)) for all integers j, k >= 1. With the Tomboulis-Yaffe inequality (GUIDE; Kanazawa, Theorem 1) this is the area law with tension sigma. It is not a gap for the zero-flux sector.
- (ii) U(1) at weak coupling has no area law (RECALLED: Guth; Frohlich and Spencer), and the Tomboulis-Yaffe inequality holds for U(1) (GUIDE: Kanazawa, Theorem 4), so (FLUX-4) is false. At Gaussian order sup over (a,b) of -log v / (ab) is of order g^2 / L^2: the flux spreads over the transverse section. Z_2 at large beta: u tends to 1/2, false.
- (iii) Theorem F holds for every group with a central Z_2. The step that would make (FLUX-4) finite is (TUBE) of Section 4.3; it is false for U(1) on thin transverse sections (estimate there).

**C3. The finite-box hypothesis (W) (kept; `library/gap-ds-gauge.md`).** (W) at (R, delta) for one R. It is the only form in this lane in which one scale is enough, and the reason is that it quantifies over all boundary values. (ii) Proposition B there: (W) gives decay, so it is false for U(1) at weak coupling and for Z_2 at its transition. (iii) Theorem W holds for every compact fibre. Sections 3.3 and 4.3 show why no statement about periodic tori alone can replace the boundary values with the tools at hand.

**C4. Dominance (kept; `library/gap-zf-box-s.md`, Theorem V).** (DOM_B) on one complex neighbourhood of [r_0, beta_1], uniform in the box. (ii) A transition at real beta_c puts zeros of large boxes at beta_c (RECALLED for U(1) and Z_2), and by Proposition D there dominance fails. (iii) Theorem V holds for every group.

**C5. Continuity in the twisted fibre (kept; (AC'-lat), `library/gap-ac-lat.md`).** For beta >= beta_1: inf over n >= 2 of m(beta, n) > 0. This is the one candidate in which Fact T is used in a proof, at small n (the chart (CH), row 679). (ii) U(1) has no twisted fibre with a unique minimum; Z_2 has no twist eater. (iii) The chart is non-Abelian; nothing known carries it to large n.

**The five are one statement.** C1 is the gap with confinement on periodic boxes. C2 is its flux half. C3 and C4 are stronger (all boundary values; complex beta). C5 is C1 for another family. I could not find a sixth statement that is weaker than the gap and still closes the tree.

## Status block (kept current; the final version is Section 6)

- Written: Sections 0-2 (Part 1), Section 3 (attempt 1, ended at its stop statement (FIT)), Section 4 (attempt 2, ended at its stop statement (TUBE')).
- Proved here, not checked: Theorem D, Corollary D2, Proposition R, Proposition N, Lemma J with the seam bound, Theorem F, Proposition T.
- Open: every candidate of Part 1.

## 3. Part 2, attempt 1: the gap on periodic boxes from two tori per scale (C1; lead (b))

Lead (b) asks for a seed and a doubling step for ratios of partition functions of small tori. This section proves the part of it that is exact, names the step that is missing, and writes down three ways in which the step failed.

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
(ii) Let (Phi-step) hold with K >= 2 and eps_0 <= 1/2, and let n_1 >= n_0 with Phi(n_1) < min(eps_0, 1/K). Put Phi_k = Phi(2^k n_1). Then K Phi_k <= (K Phi_0)^(2^k), and for every k >= 0:

m((2^(k+1) n_1)^3) >= (1/(2^k n_1)) log(1/(2 Phi_k)) >= log(1/(K Phi(n_1))) / n_1.

Proof of (ii). Induction: K Phi_(k+1) <= (K Phi_k)^2, and Phi_k <= Phi_0 < eps_0 keeps the step valid. Then Theorem D (c) with e^x - 1 <= 2x, and log(1/(2 Phi_k)) >= 2^k log(1/(K Phi_0)) + log(K/2). QED

So one seed and the step give a gap for all dyadic boxes, with a rate that does not depend on the box. The rate is in the units of the seed size n_1. The rate filter then says that the seed size is at least of the order of the correlation length.

### 3.2 Proposition R: a seed has an exponential reach, and no more (PROVED)

Let Delta(n,n,n,n) <= eps. Then for every k >= 0 with 8^k eps <= 1: m((2^k n)^3) >= (1/n) log(1/(2 8^k eps)).

Proof. Multiply three sides by 2^k: Delta(n, 2^k n, 2^k n, 2^k n) <= 8^k eps. By run 2's Lemma 1 (d), 1 + S(n; (2^k n)^3) <= exp(Delta(n, 2^k n, 2^k n, 2^k n)). Then r_1^n <= exp(8^k eps) - 1 <= 2 8^k eps. QED

Meaning. If Delta(n^4) <= exp(-mu n), the gap of every box of side up to n exp(mu n / 3) is at least mu - (3k log 2 + log 2)/n. Positivity alone carries a seed over exponentially many scales. It does not carry it to infinite volume, and it uses f, which is a limit over all sizes: Delta(n^4) = sum over k >= 0 of 16^(-(k+1)) Phi(2^k n). Theorem D is the form that uses two finite tori and reaches one doubling.

### 3.3 The missing step (Phi-step), and three ways that failed

**Way 1: positivity of the transfer operators in all four directions. It cannot work (Proposition N, PROVED).**

Lemma A, (LB) and Theorem D (a), (b) use (TM) only through this weaker property (TM'): for each direction mu and each choice of the other sides, Z(n) is the integral of lambda^(n_mu) against a positive measure on (0, Lambda] that has an atom of mass at least 1 at Lambda; and Z is symmetric in the sides. Theorem D (c)-(e), Corollary D2 and Proposition R use one more property of a trace: every eigenvalue has multiplicity at least one. It enters through r_1^k <= S(k) and S(k + k') <= S(k) S(k'). Call (TM') with integer multiplicities (TM-int).

Proposition N. Let 0 < q < 1, c > 0, f real, w(k) = c q^k, and Z_w(n) := exp( f |n| + sum over mu of (|n| / n_mu) w(n_mu) ). Then Z_w has (TM'), its infimum of F/|n| is f, and for every n:

32 n^3 c q^n <= Phi(n) <= 64 n^3 c q^n and Phi(2n) >= Phi(n)^2 / (16 n^3 c).

So for given n, eps and K, the choice c <= min( eps / (64 n^3 q^n), 1 / (16 n^3 K) ) gives Phi(n) <= eps and Phi(2n) >= K Phi(n)^2.

Proof. As a function of n_1, with V = n_2 n_3 n_4: Z_w = Lambda^(n_1) exp(V c q^(n_1)), Lambda = exp(f V + sum over mu >= 2 of (V/n_mu) w(n_mu)), and exp(V c q^(n_1)) = sum over j >= 0 of ((V c)^j / j!) (q^j)^(n_1). This is a positive combination of exponentials and the top weight is 1. F/|n| = f + sum over mu of w(n_mu)/n_mu, which is above f and tends to f. So Delta(n^4) = 4 n^3 w(n) and Phi(n) = 16 Delta(n) - Delta(2n) = 64 n^3 c q^n - 32 n^3 c q^(2n). The two bounds on Phi(n) follow from 0 < q^n < 1. Then Phi(2n) >= 32 (2n)^3 c q^(2n) = 256 n^3 c q^(2n), and Phi(n)^2 <= 4096 n^6 c^2 q^(2n). QED

What Proposition N shows. Z_w is an ideal gas of one kind of winding excitation with weight c per unit volume. Phi(2n) is linear in c and Phi(n)^2 is quadratic. So the step needs a lower bound on the number of light states of the doubled box in terms of the single box: a light state of the box (4n)^3 must already be seen, with at least a fixed weight, in the box (2n)^3. Positivity does not know this. This is the exact content of run 2's Lemma NSM, and it is the same as the statement that the gap of the box does not fall when the box is doubled.

Remark N2 (the integer class; PROVED for the family, open in general). Z_w is not in (TM-int): its weights (V c)^j / j! are not integers. The gas of the same kind with integer multiplicities is Z = exp(f |n|) times the product over mu of (1 - q^(n_mu))^(-c |n| / n_mu), with c a positive integer; it has w(k) = -c log(1 - q^k). For it, when q^n <= 1/2: Phi(n) >= 32 n^3 c q^n and Phi(2n) <= 1024 n^3 c q^(2n), so Phi(2n) <= Phi(n)^2 / (n^3 c) <= Phi(n)^2. The step holds with K = 1. The same holds for several species with integer c_j, by (sum of c_j x_j)^2 >= sum of c_j x_j^2. The reason, in this family: by the symmetry of Z, a winding weight that is a thermal state in one direction is a factor exp(n_mu times a deficit) in the other three, and integer multiplicity then makes it extensive. So integer multiplicity together with the symmetry in the four directions is a real restriction, and Proposition N does not exclude a proof of the step from (TM-int). I have no such proof and no counter-model in (TM-int). A counter-model would be a local model with a light state that exists only in boxes above a certain size. The two max plans did not separate (TM') from (TM-int); this is the one soft structure that this file leaves undecided.

I do not know a local reflection-positive lattice model in which (Phi-step) fails. For local quantum Hamiltonians without positivity no finite-size criterion can exist: the spectral gap problem is undecidable (GUIDE: Cubitt, Perez-Garcia and Wolf; recalled, not read here).

**Way 2: compare the torus (2n)^4 with sixteen tori n^4 by cutting and gluing. Exact result, of the wrong size (PROVED).**

The links of the torus (2n)^4 are the disjoint union of the links of sixteen blocks, and each block is the link set of a torus n^4. A plaquette of the large torus lies in one block, or it is a seam plaquette that has links of at least two blocks. The number of seam plaquettes is N_seam = 96 n^4 (1 - (1 - 1/n)^2) = 192 n^3 - 96 n^2.

Lemma J (gauge averaging; PROVED). Let mu be a probability measure on link configurations that is invariant under all gauge transformations. Let p be a plaquette with corners x_0, ..., x_3, and let k_1, k_2, k_3 be fixed elements of SU(2). Then the expectation of (1/2) tr(U_01 k_1 U_12 k_2 U_32^(-1) k_3 U_03^(-1)) equals (1/2 tr k_1)(1/2 tr k_2)(1/2 tr k_3) times the expectation of (1/2) tr U_p. (Seam case.) If the links of p belong to two independent systems, each with a gauge-invariant law, then the expectation of (1/2) tr U_p is 0.
Proof. A gauge transformation g replaces k_c by g_c^(-1) k_c g_c and leaves mu invariant. Average over g_c with Haar measure: the average of g^(-1) k g commutes with SU(2), so it is the scalar (1/2) tr k. Seam case: a gauge transformation of the second system at one end of its link multiplies that link by g and leaves the links of the first system fixed; the Haar average of g is 0. QED

Consequence. Under the product of the sixteen Gibbs measures, a seam plaquette of the large torus has expectation of (1/2) tr equal to 0 (seam case: its links lie in at least two blocks), and the plaquette of a small torus that it replaces has 1 - abar_n. Jensen's inequality for Z((2n)^4) / Z(n^4)^16 gives

Phi(n) <= beta (192 n^3 - 96 n^2) (1 - abar_n(beta)).

This is true and of order beta n^3. Theorem D needs Phi(n) < log 2. The bound cannot be improved at first order: by Lemma J the first-order cost of a seam plaquette is exactly beta (1 - abar_n), whatever the coupling. A gluing of independent pieces always pays the full plaquette energy on the seam.

**Way 3: a smooth deformation in place of a cut (the Mermin-Wagner idea). It fails for the same exact reason.**

For spin models with a continuous symmetry, a twist is spread over the whole torus and costs only a gradient energy. The lattice gauge measure has no continuous global symmetry. The deformations at hand multiply links by fixed elements h_l. By Lemma J the first-order cost of a plaquette is beta (1 - abar) (1 - product over corners of (1/2) tr k_c) >= 0, where k_c is the product of the h at the corner. It is zero only if every k_c is in the centre, that is, only if the deformation is a gauge transformation times a field with values in the centre. For an Abelian spreading of the flux pi over the plane (1,2), k_c = exp(i a_c σ_3) with a_c of order pi times a coordinate over n_1 n_2, and the cost is beta (1 - abar) times a sum of a_c^2 / 2. The sum is of order pi^2 |n| / min(n_1, n_2)^2. It grows with the size of the torus. For U(1) the same spreading is covariant and costs beta pi^2 n_3 n_4 / (2 n_1 n_2), which does not grow on symmetric tori. So first-order comparison sees the gauge potential of the deformation, not its field strength. It gives nothing that is uniform in the size.

**Stop.** (Phi-step) failed in three ways: positivity (Proposition N: impossible without integer multiplicities; undecided with them), gluing (exact surface term), deformation (Lemma J: no covariant first-order comparison). The one exact next statement of this attempt:

(FIT) There are n_0 and theta in (0, 1] such that for all n >= n_0: S(2n; (4n)^3) <= (1/theta) S(n; (2n)^3)^2 whenever S(n; (2n)^3) <= theta. In words: the thermal sum of the doubled box at the doubled time is at most a constant times the square of the thermal sum of the box.

(FIT) closes C1 in this sense (PROVED implication; the seed can be read from two tori, by Theorem D (b)): if S(n_1; (2 n_1)^3) < theta for one n_1 >= n_0, then S(2^k n_1; (2^(k+1) n_1)^3) <= theta (S(n_1; (2n_1)^3)/theta)^(2^k), so m((2^(k+1) n_1)^3) >= log(theta / S(n_1; (2 n_1)^3)) / n_1 for all k. The proof is the induction of Corollary D2, with r_1^k <= S(k; B). Remark, not a proof for a lattice model: for the gas Z_w the two sides of (FIT) are about 64 n^3 w(2n) and 64 n^6 w(n)^2 / theta, so (FIT) holds exactly when n^3 c, the weighted number of one-particle states of the box of side n, is at least of order theta. Proposition N is the case where n^3 c is made small by hand.

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

v = u exp(Delta) on every torus. By Theorem D (e), on the torus (2n)^4: u <= (exp(Phi(n)) - 1)^2. So C1 bounds the odd-flux weight, but with the rate of the gap: (Phi-dec) gives u <= exp(-2cn + const), not exp(-sigma n^2). And C2 says nothing about the zero-flux sector. The gap and the area law are two statements, and each half has its own missing step.

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

**Stop.** (TUBE) failed in three ways. The one exact next statement of this attempt is (TUBE'), for tori with square section: prove it, or find a torus on which it fails for SU(2). It is one inequality between four partition functions, and it can be tested by a run before any proof is tried.

### 4.4 Where the group sits in the flux weight (an exact identity, PROVED; no attempt)

Write U_l = s_l V_l with s_l = +-1 and V_l in a measurable section of SU(2) over SO(3). Haar measure is the product. (1/2) tr U_p = s_p J_p(V), with s_p the product of the four signs and J_p(V) = (1/2) tr of the product of the V_l around p, a number in [-1, 1]. For fixed V this is a Z_2 gauge theory with couplings beta J_p(V). The twist changes the sign of s_p on the stack, so it acts on the Z_2 part only. So

u(SU(2), beta) = expectation over V of u(Z_2 with couplings beta J(V)), where V has the law with density Z_(Z_2)[beta J(V)] / Z.

The odd-flux weight of SU(2) is the mean of the odd-flux weight of a Z_2 gauge theory in a random SO(3) environment (Mack and Petkova, GUIDE, use this splitting for Wilson loops). For the group Z_2 the environment is trivial and J = 1. For SU(2) the environment can make J_p small and can change its sign. This is the place where Fact T acts: a twist of the SO(3) field costs no classical action. No bound follows from the identity alone.

## 5. The leads (a) to (d), and the verdict

**Lead (a), the twist ratio and the Tomboulis-Yaffe inequality.** Its exact form here is C2 with Theorem F and Proposition T. The inequality holds for every group. Its premise is the confinement half of the crux. A premise taken from a Migdal-Kadanoff comparison does not pass test (ii): that recursion drives U(1) to strong coupling in four dimensions as well (RECALLED; this is the objection of Ito and Seiler to the argument of Tomboulis, known here from the digests only).

**Lead (b), seed and doubling.** The answer has three parts.

1. What a seed gives is exact: Theorem D (two tori, one doubling), Proposition R (exponentially many scales, with the constant f), Theorem F (all multiples in the two directions of the sheet).
2. The step that carries a seed to all scales is (FIT) for the gap and (TUBE') for the flux. It does not follow from positivity (Proposition N). For true traces it is undecided (Remark N2). Run 1's argument at its line 128 and run 2's no-go in its Section 1.5 exclude a step without a threshold; they do not exclude a step below a threshold.
3. U(1) does not fail at the step. It fails at the seed: Phi >= 0.04 at every size (about 0.41 with the twelve lowest photon states), and u is near 1/2 on square tori at weak coupling. (TUBE) fails for it on thin sections only.

A guess about the sigma model, whose preprint nobody here has read: the O(3) model has a continuous global symmetry, so a twist can be spread by a covariant deformation, and first-order comparison then gives a true lower bound for a twisted partition function (the Mermin-Wagner comparison). Lower bounds for partition functions of larger tori are what positivity lacks. The gauge theory has no such deformation (Lemma J). If the doubling step of the preprint uses the symmetry in this way, it does not transfer to the gauge theory.

**Lead (c), two-scale disintegration.** In two dimensions the plaquettes are independent after an axial gauge fixing, so the two scales are one plaquette and a product measure. In four dimensions the Bianchi constraint ties the plaquettes of every cube. A two-scale criterion then needs a small coupling between the scales, and that is a mixing statement of the kind of (W). I see no new handle (abstract only).

**Lead (d), logarithmic Sobolev inequality and mixing.** It is an equivalence between two forms of one hypothesis. It could carry (W) to a uniform Poincare constant, and so toward (HS-sup). It is not a mechanism.

**Verdict.**

1. I found no statement of the crux that is weaker than the gap and still closes the tree. I found no exact tool in which the group acts at couplings of order one. The exact tools of this lane are: positivity of the transfer operators in four directions, the centre flips, reflection positivity, first-order comparison, and the finite-box criterion. Each holds for every compact group with a central Z_2. The group enters through Fact T, which is used at weak coupling in the twisted chart, and through Fact B, which no exact inequality uses.
2. Run 1's third test says the same from outside: SU(2) with an adjoint Higgs field has the centre, reflection positivity and Fact B, and it has a phase with a photon (RECALLED there). So a proof must use the pure Wilson form at a quantitative step at couplings of order one. I know no method by hand for such a step. This agrees with the verdict of both max plans.
3. What this run adds is on the soft side. Each half of the crux has an exact finite form, a proved criterion and one named step. The one new question is Remark N2: is the step a consequence of positivity with integer multiplicities and the symmetry of the four directions? It costs little to decide and nobody had separated it.
4. A proof of (FIT) would still leave the seed. The seed is one inequality between two partition functions at the scale of the correlation length. The rate filter forbids a seed at a perturbative scale, and no method by hand computes a number at couplings of order one. The gain over (W) would be this: the seed is a statement about periodic tori with no boundary values, and by Theorem D (f) a run can measure it from plaquette averages. A run is a guide and not a proof.

**What changes in the plan (the author's reading; the lead decides).**

- The tree can carry C1 as a third conditional form next to (W) and (DOM_B): "(Phi-dec) in scaling form gives a gap of periodic boxes that is uniform in physical units" (Theorem D and Corollary D2 with rates c a(beta)). It needs no complex coupling and no free walls. It is a form of the hypothesis and not a reduction of it: it is as strong as the gap with confinement.
- Order of work that I recommend: item 1, then item 2, then item 3 of Section 6. Items 4 and 5 only if the lead has spare capacity.
- I do not recommend another restatement run before one of these exists: a correlation inequality of Griffiths type for SU(2); a dual representation with positive weights; a covariant first-order comparison (a way around Lemma J); or a positive answer to item 2.

## 6. Part 3: status block (final)

**Proved here by hand. Not checked by another model.** Inputs: (TM) and (TM-c) (rows 667, 671; run 2, Lemma 1'), Lemma A (run 2, Lemma 1).

| Statement | Content | Section |
|---|---|---|
| Theorem D | Phi(n) = 16 F(n^4) - F((2n)^4) bounds the thermal sum, the gap, the count of states and the odd-flux weight of the box (2n)^3; Phi is an integral of plaquette differences | 3.1 |
| Corollary D2 | (Phi-dec) gives a uniform box gap; (Phi-step) with one seed gives a uniform gap on dyadic boxes | 3.1 |
| Proposition R | a seed for Delta reaches boxes of side n exp(mu n / 3), not infinite volume | 3.2 |
| Proposition N, Remark N2 | (Phi-step) does not follow from positivity; in the integer family it holds with K = 1 | 3.3 |
| Lemma J, seam bound | exact first-order value of a deformed or glued plaquette; Phi(n) <= beta (192 n^3 - 96 n^2)(1 - abar_n) | 3.3 |
| (FIT) closes C1 | implication, by induction | 3.3 |
| Theorem F | v = Z_odd exp(-f abs(n)) obeys v(ja, kb) <= v(a, b)^(jk); a seed v < 1 gives area decay of the odd-flux weight on all multiples; the alternative (e) | 4.1 |
| Proposition T | (TUBE), a bounded Delta and one seed give (FLUX-4) on dyadic symmetric tori | 4.3 |
| Identity 4.4 | the odd-flux weight of SU(2) is a mean over SO(3) environments of the odd-flux weight of a Z_2 theory | 4.4 |

**Failed, and why.**

- (Phi-step), in the form (FIT): positivity alone cannot give it (Proposition N); gluing pays the exact surface term beta (1 - abar) per seam plaquette; no deformation other than a gauge transformation times a centre field is free at first order (Lemma J).
- (TUBE), in the form (TUBE'): the odd-flux weight is not a trace in the transverse directions; reflection positivity across the section gives only a cost per plaquette of the stack; deformation fails by Lemma J. At Gaussian order (TUBE) is false for U(1) on thin sections (estimate, not proved).

**The one exact next statement of each attempt.**

- Attempt 1: (FIT) of Section 3.3. Before it, the question of item 2.
- Attempt 2: (TUBE') of Section 4.3 on tori with a square section.

**Not done.** No numeric job was started. The bodies of `gap-zf-box-x.md`, `gap-zf-box-s.md` and `gap-ac-lat.md` were not read. The Gaussian estimates for U(1) (the photon bound 0.04, the value 0.41, the threshold 0.78 g) are estimates from recalled formulas; no proof uses them. The Tomboulis-Yaffe inequality is not rebuilt here; the area law in Theorem F and Proposition T is stated for the odd-flux weight, and for Wilson loops only through that GUIDE.

**Proof items for the medium workers.**

1. `gap-defect-check` (worker 2, check). Check line by line every row of the table above. Inputs: the statement of (TM) in `library/gap-transfer.md` and its check; `gap-skeleton-max-b.md` lines 241-256. Read: Sections 1, 3, 4 of this file. Points that carry weight: Theorem D (e) uses that the top eigenvector is even under the centre flips; Theorem F (a) uses (TM-c) for both directions of the twist plane; Theorem D (c)-(e) use integer multiplicity.
2. `gap-int-class` (worker 1, proof). Statement: let Z be a function of the sides that is symmetric and has (TM-int) in each direction (Section 3.3). Prove or refute: there are theta > 0 and n_0, which may depend on Z, with (FIT). Start in two dimensions, where the class is Z(a, b) = Z(b, a) = sum of lambda_i(b)^a with integer multiplicities, and (FIT) reads S(2n; 4n) <= (1/theta) S(n; 2n)^2. Known here: the class is closed under sums and products; a single extra state forces lambda(b) = q^b (from 1 + lambda(b)^a = 1 + lambda(a)^b); the integer gases satisfy the step. A refutation is a table of spectra, consistent with the symmetry for all sizes, with a light state that first appears at one size. A proof must name the step where integer multiplicity is used. If it is refuted, the missing input is locality and not integrality, and the soft side is closed. Read: Section 3.3 here; run 2, Section 1.5.
3. `gap-defect-guide` (guide run, under the numeric lock). Compute Phi(n; beta) by Theorem D (f) from plaquette averages on the tori n^4 and (2n)^4 for n = 3, 4, for SU(2) at beta from 0 to 2.6 and for U(1) at beta from 0 to 1.2. Write the pass and fail criteria first. Prediction for SU(2): Phi(n; beta) stays below log 2 up to a coupling that grows with n. Prediction for U(1): Phi rises above log 2 near beta = 1.0 and stays there. The plaquette difference must be known to better than 0.1 / (96 n^4 beta). What the run can show: at which sizes a seed exists, and if Phi(2n) <= K Phi(n)^2 holds in the data. It can show no proof step.
4. `gap-tube-test` (worker 1, proof, then guide). Decide (TUBE') on tori (a, b | c, c) in the strong-coupling disc: expand both sides in polymers and find the sign of the first order at which they differ. Then a run on the smallest tori at beta between 1.5 and 2.5. Consumer: Proposition T. Low priority: (TUBE') is needed at every scale.
5. `gap-defect-sc` (worker 1, proof). Prove Phi(n; beta) <= C n^3 (beta / r_1)^(4n) for 0 <= beta <= r_1 with explicit C and r_1, for periodic tori (the periodic form of Theorem SC; the exponent 4n is the smallest tube that winds once). Consumer: the base of C1, and a cross-check of Theorem D against kappa_0 = 4 log 2. Low priority.

<!-- END -->
