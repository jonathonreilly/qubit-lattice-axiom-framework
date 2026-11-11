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

**(TM)** (input; `library/gap-transfer.md`, row 667, check row 671). For each direction mu and each choice of the other three sides there is a positive trace-class operator T on a Hilbert space with Z(n) = Tr T^(n_mu).

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
- (ii) U(1) at weak coupling: the periodic box has an excited state of energy at most (2 pi / side)(1 + o(1)) (RECALLED, the photon; run 2's K5). By Theorem D (c), read backwards, Phi(n) >= log(1 + exp(-n m((2n)^3))) >= log(1 + exp(-pi - o(1))) > 0.04. So (Phi-dec) is false, and no seed below 0.04 exists. Z_2 at its transition: two phases, so m(box) tends to 0 (RECALLED) and Phi(n) >= log 2 - o(1). Z_2 at large beta: the flux sectors are degenerate with the vacuum (RECALLED), same bound; this is why C1 is the gap with confinement.
- (iii) Theorem D holds for every group. The step (Phi-step) is not a consequence of (TM): Section 3.3.

**C2. Flux on tori with normalised bulk (the published lead (a) in exact form).** Twist in the plane (1,2). Z_odd(n) := (Z(n) - Z^(12)(n))/2, u(n) := Z_odd(n)/Z(n), v(n) := Z_odd(n) exp(-f |n|), so 0 <= u <= v (by (LB)).

- (FLUX-4): there are sigma > 0 and L_0 such that for every L >= L_0 there is a torus (a, b | L, L) with v(a, b | L, L) <= exp(-sigma a b).
- What it gives (Theorem F, PROVED): u(ja, kb | L, L) <= exp(-sigma (ja)(kb)) for all integers j, k >= 1. With the Tomboulis-Yaffe inequality (GUIDE; Kanazawa, Theorem 1) this is the area law with tension sigma. It is not a gap for the zero-flux sector.
- (ii) U(1) at weak coupling has no area law (RECALLED: Guth; Frohlich and Spencer), and the Tomboulis-Yaffe inequality holds for U(1) (GUIDE: Kanazawa, Theorem 4), so (FLUX-4) is false. At Gaussian order sup over (a,b) of -log v / (ab) is of order g^2 / L^2: the flux spreads over the transverse section. Z_2 at large beta: u tends to 1/2, false.
- (iii) Theorem F holds for every group with a central Z_2. The step that would make (FLUX-4) finite is (TUBE) of Section 4.3; it is false for U(1) on thin transverse sections (estimate there).

**C3. The finite-box hypothesis (W) (kept; `library/gap-ds-gauge.md`).** (W) at (R, delta) for one R. It is the only form in this lane in which one scale is enough, and the reason is that it quantifies over all boundary values. (ii) Proposition B there: (W) gives decay, so it is false for U(1) at weak coupling and for Z_2 at its transition. (iii) Theorem W holds for every compact fibre. Sections 3.3 and 4.3 show why no statement about periodic tori alone can replace the boundary values with the tools at hand.

**C4. Dominance (kept; `library/gap-zf-box-s.md`, Theorem V).** (DOM_B) on one complex neighbourhood of [r_0, beta_1], uniform in the box. (ii) A transition at real beta_c puts zeros of large boxes at beta_c (RECALLED for U(1) and Z_2), and by Proposition D there dominance fails. (iii) Theorem V holds for every group.

**C5. Continuity in the twisted fibre (kept; (AC'-lat), `library/gap-ac-lat.md`).** For beta >= beta_1: inf over n >= 2 of m(beta, n) > 0. This is the one candidate in which Fact T is used in a proof, at small n (the chart (CH), row 679). (ii) U(1) has no twisted fibre with a unique minimum; Z_2 has no twist eater. (iii) The chart is non-Abelian; nothing known carries it to large n.

**The five are one statement.** C1 is the gap with confinement on periodic boxes. C2 is its flux half. C3 and C4 are stronger (all boundary values; complex beta). C5 is C1 for another family. I could not find a sixth statement that is weaker than the gap and still closes the tree.

## Status block (first version, after Part 1; kept current at the end of the file)

- Written: Sections 0-2. Proofs of Theorems D and F, Lemma J and Proposition R follow in Sections 3 and 4.
- Open: every candidate. No attempt has been made yet at this point of the file.

<!-- END -->
