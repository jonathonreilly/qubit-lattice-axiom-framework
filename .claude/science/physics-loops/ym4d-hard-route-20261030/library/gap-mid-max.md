lead: anthropic/claude-fable-5-2/max mac-mini-worker
lease_until: 2026-11-11T22:45Z

# gap-mid-max: an attack on the middle range of the mass gap (queue row 708)

Research-stage working state. It grants no status. Nothing here is a public claim.

Pinned at commit 43010014c on `claude/ym4d-hard-route`. Author run, not a check. Written in steps; each step is appended before the next is thought through (save rule, row 675).

## 0. Log of the run

- 2026-11-11 10:45 UTC. Started. No earlier work of this item in the file at the pinned commit. Reading the files the row names.
- Step 1 done: reading, duplicate check, Part 1 and the first status block (Sections 1 to 3).

## 1. Position, reading state, duplicate check, credits

**Kind of result.** No proof of the seed at a coupling of order one. The file gives (a) four candidate statements with the test, (b) attempts on three of them, each carried to a proof of what can be proved and to one named open statement, (c) a status block and proof items.

**Read in full:** FINISH row 708; GOAL.md; `library/gap-crux-restate.md`; `library/gap-seed-shape.md`; `library/prior/gap-seed-size.md`; `library/prior/gap-seed-lit.md`; `library/gap-skeleton-final.md` Sections 12 and 13. **Read in part:** `library/gap-seed-limit.md` and `library/gap-seed-sc.md` (statements only); `library/prior/gap-crux-lit-2.md` (headings and the synthesis, lines 327 to 417); `library/gap-skeleton-max-b.md` lines 134, 164 to 185, 205 to 212, 257 to 260, 412 to 415. **Not read:** every primary paper; the Sussman-Alpoge repository (the row forbids network access for this item, and the three literature digests report that the outline and the account hold no statement on the physical gap). Nothing was fetched from the network.

**Duplicate check (rule 0a).** Searched `library/open-core.md`, the FINISH rows and `library/gap-*.md`, `library/prior/gap-*.md` for: virial, Gronwall, Bhanot, mixed action, adjoint coupling, finite-size shift, trace anomaly, interaction measure, Hellmann, step scaling, Dobrushin comparison, Casimir, pressure, SO(3), electric flux, characteristic. `open-core.md` has no hit. Matches that bind this file:

- Run 2 (`gap-skeleton-max-b.md`) already lists, as heuristic candidates with their kill lines: A4 transport in the coupling with crux (DEF) (lines 164 to 170), A5 step scaling with crux (STEP) (172 to 178), A6 flux duality with crux (VORT) (180 to 185), A10 the dilation identity (207 to 211), and the warning K7 (line 134: the mixed fundamental and adjoint action has a critical end point near the Wilson axis; recalled from Bhanot and Creutz). Its Lemma 2 (line 259) is the integral of the plaquette shift.
- Run 1 (`gap-skeleton-max.md` line 80): the third test (an adjoint Higgs field).
- Row 677 (`gap-zf-box-x.md`): (HS-sup), the gradient bound for the Poisson equation of the action. Row 691: (W). Row 697: (TUBE').
- So the leads (a), (b), (c) of the row are A5, A6, A4 of run 2. I do not state them again as heuristics. What is new below: each is put in the finite form that Theorems S and SH make possible, the implications are proved, and the open statement of each is an inequality of order one with no small number in it. I do not attack (HS-sup), (W), (TUBE') or (VORT).

**Credits.** Tadeusz Balaban (the ultraviolet part, not used in a proof here). Sussman and Alpoge with Claude and Codex (the account; not used in a proof here). Claude Fable 5.2 max, rows 669, 670, 697 (candidates A4 to A10, K7, Lemmas A, K, X, E, Theorems S, D, F). Codex gpt-6-astra, row 699 (Lemma E'). Claude Fable 5.2 medium, rows 701, 705 (the strong-coupling seed; Lemma E2, Theorem SH, Theorem D-shape). Claude Opus 5.5, rows 698, 703, 704 (checks). Osterwalder and Seiler, Luscher (transfer operator, through row 667). 't Hooft (twists and flux). Bhanot and Creutz (the mixed action; RECALLED). Bakry and Emery; Shen, Zhu and Zhu (curvature at small beta; RECALLED). Dobrushin (uniqueness condition; RECALLED, used only in a proof item).

**Marks.** PROVED = proved by hand in this file from the named inputs; not checked by another model. PROVED GIVEN (X). GUIDE = estimate or recalled number, used in no proof. RECALLED = a known fact used only in a test. OPEN.

**Notation.** As in `gap-crux-restate.md` Section 1 and `gap-seed-shape.md` Section 1. Box B = (b_1, b_2, b_3), abs(B) = b_1 b_2 b_3, all sides at least 3. T_B(beta) is the transfer operator, lambda_0 > lambda_1 >= ... its eigenvalues, rho_i = lambda_i / lambda_0, E_i = log(1/rho_i). For real t >= 2:

G(t; B; beta) := log(1 + sum over i >= 1 of rho_i^t) = log Tr T_B^t - t log lambda_0.

For integer t >= 3 this is g(t; B) = log Z(t, B) - t e(B) = log(1 + S(t; B)). F(n) = log Z(n). f = inf F(n)/abs(n). Delta(n) = F(n) - f abs(n) >= 0. abar_n = mean plaquette action on the torus n. Thresholds t(r) of Theorem SH: t(2) = 1/1650, t(4) = 1/25.

## 2. Part 1: four candidate statements

One remark first. Of the three kinds of tool that row 697 names, two fail the test (ii) as mechanisms. A correlation inequality of Griffiths type holds for Z_2 (Griffiths, Kelly, Sherman) and for U(1) (Ginibre) (RECALLED), the two groups for which the seed is false. A dual form with positive weights exists for both (surfaces for Z_2, integer currents for the Villain form of U(1); RECALLED), and for U(1) it is the tool that proves the absence of a gap. So for SU(2) such a tool could organise a proof, and it cannot be the place where the group decides. The third kind, a monotone quantity, exists for every group: the deficit kappa of Lemma K. What would decide is strictness, and that is statement C-B below.

A second remark, on K7. It is the sharpest test, and I use it as test (iv) next to (i) to (iii): the candidate must be false, or its proof must break, for the one-plaquette weight exp(beta_F x + beta_A (4 x^2 - 1)/3), x = (1/2) tr U_p, at the couplings of its first-order line (RECALLED from Bhanot and Creutz; the line ends near (beta_F, beta_A) = (1.5, 0.9); GUIDE values). On that line two phases coexist, so every thermal sum of a periodic box is at least 1 - o(1) (as for the Ising model in `gap-seed-shape.md` 4.1). That weight has the same group, centre, twist with zero classical cost, reflection positivity, positive characters, Ricci curvature and one-loop coefficient as the Wilson weight. So no statement that uses only those can give the seed at a coupling of order one. The Wilson weight differs in one exact point: it is the exponential of a function that is linear on R^4, restricted to the sphere SU(2) (log-linear in x; the adjoint term makes it log-convex in x). I found no inequality that uses this.

**C-A. A bound of order one on the derivative in beta, on one box (lead (c), with lead (e)).**

- (VIR_K) for a box B, an interval [beta_0, beta_1], a continuous K >= 0 and a range of times: for every s in the interval and every real t in the range,

 D_s G(t; B; s) <= - K(s) t (dG/dt)(t; B; s),

 where D_s is the upper right derivative in s. In words: along the coupling, no part of the spectrum of the box falls faster than at the logarithmic rate K. At integer t the left side is 6 t abs(B) (abar_(inf,B) - abar_(t,B)), the shift of the mean plaquette action between the infinite and the finite time extent (Lemma 4.2). The right side is K t times the thermal mean of the energy.
- What it gives (Theorem TR and Corollary TR1, Section 4, PROVED GIVEN Theorem SH and `gap-seed-sc.md` Theorem 1): (VIR_K) on one cube of side b, with b at least 2 t_0 exp(integral of K) and t_0 = ceil(log_2 b), gives the seed at beta_1 and a gap of at least 0.12/b on every cube of side at least 32 b. K need not be bounded in b: a bound K <= log(b/(2 t_0))/(beta_1 - beta_0) is enough. The trivial bound is of order abs(B)/m (GUIDE).
- (i) The group enters through (VIR_K) only. (ii) U(1): the seed holds at small beta (strong coupling holds for every group) and fails at weak coupling (RECALLED: photon), so by Theorem TR (VIR_K) with K of order log b fails on every interval that crosses the transition near beta = 1.01. Z_2: the same at its transition. At a first-order point a level E = (difference of free energy densities) times abs(B) crosses zero with slope of order abs(B); at a critical point K_b grows like a power of b (GUIDE: finite-size scaling). (iii) No proof exists; the missing line is the bound of the action deficit of an excited state by its energy (Section 4.4). (iv) K7: at the end point the scalar mass vanishes at a finite coupling, so K is unbounded there.
- Kind: an inequality of order one. No small number has to be proved. The small number comes from strong coupling and is carried by the theorem.

**C-B. Strict fall of the Casimir free energy of the symmetric torus (lead (a)).**

- Proposition Delta (Section 5, PROVED GIVEN Theorem SH): for every a >= 3 and r = b/a > 1, S(a; b^3) <= exp(r^3 Delta(a, a, a, a)) - 1. So Delta(a^4) <= 6.1 x 10^(-4) at one a gives the seed at r = 4. In a model of the class with no uniform gap, Delta(a^4) > 6.1 x 10^(-4) for every a >= 3.
- (CAS) There are theta < 1 and M such that Delta(3^4) <= M and, for every a >= 3 with 6.1 x 10^(-4) < Delta(a^4) <= M: Delta((2a)^4) <= theta Delta(a^4).
- What it gives: after at most log(M / 6.1 x 10^(-4)) / log(1/theta) doublings from a = 3 the seed holds (immediate from Proposition Delta).
- (i) The group would enter in the proof of theta < 1. (ii) U(1) at weak coupling: Delta(a^4) tends to a constant of the free Maxwell field on the symmetric torus (RECALLED: scale invariance), so no theta < 1; by Proposition Delta that constant is above 6.1 x 10^(-4), a fact about every massless theory of the class. Z_2 at large beta: Delta(a^4) rises to log 8 (RECALLED: eight flux sectors). (iii) No proof exists. (iv) On the first-order line Delta(a^4) rises to log 2.
- Verdict: (CAS) is the statement that the theory has no fixed point of the doubling map above the threshold. It holds in every model of the class that has the seed after finitely many doublings, so as a mechanism it is empty: it restates the seed in steps. It has one use: it shows that the middle range needs inequalities of order one only (theta < 1 on a compact interval). Theorem CRIT (Section 5) gives the same content in the coupling: the first coupling at which the seed is lost is a critical point of the lattice theory.

**C-C. Flux sectors (lead (b)).**

- Identity FL (Section 6, PROVED from (TM-c)): with S_0 the thermal sum of the sector of zero electric flux and U := (1/8) sum over k in Z_2^3, k not 0, of (1 - Z[k]/Z), where Z[k] = Tr(T^t C^k): 1 + S = (1 + S_0)/(1 - U). So the seed S <= t holds if and only if (1 + S_0) <= (1 + t)(1 - U).
- (MF) at one box: U <= t/3 (the twists in the three time planes cost almost nothing), together with (S_0): S_0 <= t/3. For t <= 1 the two give S <= t.
- (i) Fact T of row 697 (the twist has zero classical cost for SU(2)). (ii) U(1): the Z_2 twist costs beta pi^2 times a ratio of sides at Gaussian order, so U stays of order one at weak coupling; Z_2 at large beta: U tends to 7/8 while S_0 tends to 0. (iii), (iv): on the first-order line of K7 (MF) can hold and (S_0) fails.
- Verdict: the seed does not reduce to one part. The two parts are independent in the class (Section 6). (MF) is run 2's (VORT) and row 697's flux half, whose open step is (TUBE'); by rule 0a I do not attack it. Only the identity and the independence are added.

**C-D. Curvature at a block scale (lead (d)).**

- (BE-block) For the conditional law of the links of a block given the block variables of one renormalization step, the Bakry-Emery tensor Ric + Hess(beta A + blocking term) is at least rho > 0 at every configuration, with rho independent of the volume.
- Verdict: false for beta > 1/3 for every blocking that leaves one link and the eighteen links of its staples free (Proposition BE, Section 7, PROVED: an explicit configuration with tensor (1/2 - 3 beta/2) on a link direction). The same number holds for U(1) with 0 in place of 1/2, and for the weight of K7. So the curvature of SU(2) is worth beta < 1/3 and no more, at every scale, in the pointwise form. A form with an averaged curvature is a mixing hypothesis of the kind of (W) (row 691), which is covered there.

**Why there is no fifth.** Lead (e) has no statement of its own: its content is the remark that C-A and C-B are inequalities of order one, and Section 4.5 says what a hand proof of one step would need. I did not find a different object. The honest position after Part 1: the right object in the coupling direction is K_b(s), the logarithmic rate of C-A, and what is needed about it is a growth of at most log b.

## 3. Status block (kept current)

- Written: Sections 0 to 3 (Part 1) and Section 4 (attempt 1). Sections 5 to 7 follow; statements quoted above with "Section 5" to "Section 7" are not yet written out below unless this line is updated.
- Proved so far in this file (not checked): Lemma 4.1, Lemma 4.2, Theorem TR, Proposition Delta (stated in 4.3, proof there), Corollary TR1, Remark LEV.
- Failed: the deficit bound (DEF_K), in three ways (Section 4.4).
- Open: (VIR_K) for SU(2) with K of order log b; (CAS); (MF) and (S_0); the seed at a coupling of order one.

## 4. Part 2, attempt 1: transport of the seed along the coupling (C-A)

The aim: turn "the seed holds at small beta" into "the seed holds at beta_1" with an input that has no small number in it. The result is Theorem TR with Corollary TR1. The input (VIR_K) is not proved; Section 4.4 records three ways that failed.

### 4.1 Regularity from the traces alone (PROVED from (TM) and Lemma A)

**Lemma 4.1.** Fix a box B. Write p_n(beta) = Tr T_B(beta)^n = Z(n, B; beta) for integers n >= 3.
(a) lambda_0(beta) is continuous in beta > 0.
(b) For real t >= 4 the functions G(t; B; beta) and (dG/dt)(t; B; beta) are jointly continuous in (t, beta). For fixed beta, G is smooth, convex and non-increasing in t.

Proof. Each p_n is continuous in beta (an integral of exp(-beta A) over a compact space). (a) By Lemma A (a), lambda_0 = inf over n of p_n^(1/n), an infimum of continuous functions, so it is upper semicontinuous. By Lemma A (b), lambda_0^n >= p_(2n)/p_n, and (p_(2n)/p_n)^(1/n) tends to lambda_0; so lambda_0 = sup over n of (p_(2n)/p_n)^(1/n), which is lower semicontinuous. (b) Let nu_beta be the measure on [0, Lambda] that puts the mass lambda_i^3 at each eigenvalue lambda_i (with multiplicity); Lambda is a bound for lambda_0 on a compact set of couplings, for example the maximum of p_3^(1/3). Its total mass is p_3 and its moments are the integrals of x^k, equal to p_(k+3), k >= 0. They are continuous in beta. Polynomials are dense in the continuous functions on [0, Lambda], and the masses are bounded on compact sets of couplings, so the integral of h against nu_beta is continuous in beta for every continuous h. Now Tr T^t = integral of x^(t-3) d nu_beta, and d/dt Tr T^t = integral of x^(t-3) log x d nu_beta. For t >= 4 both integrands are continuous on [0, Lambda] and depend continuously on t in the sup norm on compact sets of t. So both integrals are jointly continuous. G = log Tr T^t - t log lambda_0, and Tr T^t >= lambda_0^t > 0. In t, G = log(1 + sum of rho_i^t) is a logarithm of a sum of exponentials with rates log rho_i <= 0. QED

**Lemma 4.2 (the derivative in the coupling at integer time).** Let t >= 3 be an integer. Then e(B; beta) = log lambda_0 is convex in beta, and the right derivative of g(t; B; beta) in beta exists at every beta. There is a countable set N_B such that for beta outside N_B:

d g(t; B; beta)/d beta = 6 t abs(B) (abar_(inf,B)(beta) - abar_(t,B)(beta)),

where abar_(inf,B) is the limit of abar_(t,B) as t grows.

Proof. F(t, B; beta) = log Z is smooth and convex in beta, with dF/dbeta = -6 t abs(B) abar_(t,B) (there are 6 t abs(B) plaquettes). e = limit of F(t, B; .)/t (Lemma A (a)), a pointwise limit of convex functions, so it is convex. A convex function has a right derivative everywhere and is differentiable outside a countable set. Where the limit of a sequence of convex functions is differentiable, the derivatives converge to its derivative. So outside N_B: de/dbeta = -6 abs(B) lim abar_(t,B). Subtract. QED

### 4.2 Theorem TR (PROVED from Lemma 4.1)

**Theorem TR.** Let B be a box, 0 < beta_0 < beta_1, K a continuous non-negative function on [beta_0, beta_1], t_0 >= 4, and E(s) := exp(integral of K over [beta_0, s]). Assume (VIR_K): for every s in [beta_0, beta_1) and every real t in [t_0, t_0 E(beta_1)],

limsup as h decreases to 0 of (G(t; B; s + h) - G(t; B; s))/h <= - K(s) t (dG/dt)(t; B; s).

Then for every s in [beta_0, beta_1]: G(t_0 E(s); B; s) <= G(t_0; B; beta_0). In particular, for every integer a >= t_0 E(beta_1): S(a; B; beta_1) <= S(t_0; B; beta_0) when t_0 is an integer.

Proof. Put tau(s) = t_0 E(s), so tau' = K tau, and phi(s) = G(tau(s); B; s). phi is continuous (Lemma 4.1). For h > 0:

phi(s + h) - phi(s) = [G(tau(s+h); s+h) - G(tau(s); s+h)] + [G(tau(s); s+h) - G(tau(s); s)].

By the mean value theorem in t the first bracket is (dG/dt)(xi_h; s+h)(tau(s+h) - tau(s)) with xi_h between tau(s) and tau(s+h). As h decreases to 0, xi_h tends to tau(s), and dG/dt is jointly continuous, so the first bracket divided by h tends to (dG/dt)(tau(s); s) K(s) tau(s). By (VIR_K) the upper limit of the second bracket divided by h is at most -K(s) tau(s) (dG/dt)(tau(s); s). So the upper right derivative of phi is at most 0 at every point of [beta_0, beta_1).
A continuous function with this property is non-increasing. (For eps > 0 let psi(s) = phi(s) - eps s. If psi(s_2) > psi(s_1) for some s_1 < s_2, take c strictly between, and s* the supremum of the s in [s_1, s_2] with psi(s) <= c. Then s* < s_2, psi(s*) = c and psi > c on (s*, s_2], so the upper right derivative of psi at s* is at least 0. But it is at most -eps. So psi is non-increasing for every eps > 0, and so is phi.)
Last claim: G is non-increasing in t. QED

**Remark LEV (a transparent sufficient condition; PROVED).** Order the levels, E_1(s) <= E_2(s) <= ... . If for all s < s' in the interval and all i >= 1

(LEV_K) E_i(s') >= E_i(s) exp(- integral of K over [s, s']),

then G(t exp(integral of K over [s, s']); B; s') <= G(t; B; s) for every t >= 2, term by term in the sum. So the conclusion of Theorem TR holds with no derivative. (LEV_K) says: no ordered level falls faster than at the logarithmic rate K. (VIR_K) asks this only for the thermal mean. Where the levels are differentiable, (LEV_K) is - dE_i/ds <= K E_i, and - dE_i/ds is the action of one time slab in the vacuum minus its action in the level i (first-order perturbation; interpretation, used in no proof). I call this difference the action deficit of the level.

### 4.3 From strong coupling to beta_1 (PROVED GIVEN Theorem SH of row 705, not yet checked, and `gap-seed-sc.md` Theorem 1 (iii), checked in row 704)

**Proposition Delta.** For integers a >= 3 and b >= a: g(a; b^3) <= (b/a)^3 Delta(a, a, a, a). So if Delta(a^4) <= 6.1 x 10^(-4) for one a >= 3, then S(a; (4a)^3) < 1/25 = t(4), and Theorem SH gives a uniform gap on all cubes of side at least 4a. In a model of the class with inf over L of m(L^3) = 0: Delta(a^4) > 6.1 x 10^(-4) for every a >= 3.

Proof. By Lemma A (a), for the transfer operator of each direction, Z(a, b, b, b) <= Z(a, a, b, b)^(b/a) <= Z(a, a, a, b)^((b/a)^2) <= Z(a^4)^((b/a)^3). By (LB), lambda_0(b^3) = lim Z(t, b^3)^(1/t) >= exp(f b^3). So g(a; b^3) = F(a, b^3) - a log lambda_0(b^3) <= (b/a)^3 F(a^4) - a b^3 f = (b/a)^3 Delta(a^4). With b = 4a: g <= 64 x 6.1 x 10^(-4) = 0.03904, and exp(0.03904) - 1 < 0.0399 < 1/25. The last sentence is the contrapositive, by Theorem SH (iii). QED

(The first inequality is Proposition R of row 697 for b = 2^k a. The form with t(4) and the lower bound for gapless models are the additions.)

**Corollary TR1.** Let beta_0 <= 1/25600 (so theta := 12800 beta_0 <= 1/2), b >= 256 an even integer, a = b/2, t_0 = ceil(log_2 b), beta_1 > beta_0, and assume (VIR_K) for the cube B = b^3 on [beta_0, beta_1] and the times [t_0, a], with

integral of K over [beta_0, beta_1] <= log(a/t_0).

Then S(a; b^3; beta_1) < 5.1 x 10^(-4) < 1/1650 = t(2). So, at beta_1, every periodic cube has a gap, inf over L >= 2b of m(L^3) > 0, and m(L^3) >= 0.06/a = 0.12/b for every integer L >= 32 b.

Proof. Strong coupling: by `gap-seed-sc.md` Theorem 1 (iii), Phi(n; beta_0) <= 0.16 n^4 theta^(4n) for n >= 4. Since F(N^4)/N^4 decreases to f along N = 2^k n, Delta(n^4) = sum over k >= 0 of 16^(-(k+1)) Phi(2^k n) <= 0.01 n^4 sum over k of theta^(4 n 2^k) <= 0.0101 n^4 theta^(4n) (theta^16 <= 2^(-16)). With n = t_0 >= 8 and Proposition Delta: g(t_0; b^3; beta_0) <= 0.0101 b^3 t_0 theta^(4 t_0) <= 0.0101 b^3 t_0 16^(-t_0) <= 0.0101 t_0/b, because 16^(-t_0) <= b^(-4). For b >= 256: t_0 <= log_2 b + 1, and (log_2 b + 1)/b is decreasing there, so t_0/b <= 9/256 < 0.036 and g(t_0; b^3; beta_0) < 3.7 x 10^(-4) < 5.05 x 10^(-4). Transport: E(beta_1) <= a/t_0, so [t_0, t_0 E(beta_1)] lies in [t_0, a], and Theorem TR gives G(t_0 E(beta_1); b^3; beta_1) <= g(t_0; b^3; beta_0). Since a >= t_0 E(beta_1): g(a; b^3; beta_1) < 5.05 x 10^(-4), S < 5.1 x 10^(-4). Gap: by the line "r = 2, two stages" of `gap-seed-shape.md` 1.5, s_1 = S(a; (4a)^3) <= 0.0396, and Theorem SH (ii) for the pair (a, 4a) with K_SH = 22.2 gives m(L^3) >= (1/a)(log(1/(22.2 x 0.0396)) - 0.85 x 2^(-k)) for L >= 2^k 4a. log(1/0.8792) > 0.128, and for k >= 4 the second term is below 0.054. So m(L^3) >= 0.07/a for L >= 64 a = 32 b. QED

**What the corollary says.** The seed at beta_1 follows from the strong-coupling seed (proved) and one inequality on one cube in which nothing is small: the logarithmic rate K_b of the box b^3 on [beta_0, beta_1] is at most log(b/(2 t_0))/(beta_1 - beta_0). The side b is free. So the mass gap at beta_1 is implied by: K_b grows more slowly than (log b)/(beta_1 - beta_0) along some sequence of sides. The price is the size: b is of the order exp(integral of K). With the GUIDE value K about 3.3 for beta between 2.3 and 2.6 (from the values of a sqrt(sigma) in `prior/gap-seed-size.md`: log(0.29023/0.36778)/0.0728 = -3.25, and -3.41, -3.51, -3.35 on the next three intervals) and K of order 1/(beta log(4/beta)) at small beta (GUIDE, from E = n log(4/beta)), the box at beta = 2.3 would have b of order 10^3 to 10^4 lattice units. The seed box of row 706 has b about 20. So the theorem trades a small box with a small number for a large box with an inequality of order one.

### 4.4 The deficit bound (DEF_K): three ways that failed

(DEF_K): for the box b^3, every ordered excited level and every s in [beta_0, beta_1]: - dE_i/ds <= K E_i, with K independent of b, or at most c log b.

**Way 1: a pointwise operator inequality.** This is run 2's attempt (its Section 1.4; I recall its conclusion and add the numbers). In the picture with continuous time the energy of a level above the vacuum is the sum of an electric and a magnetic part, and s times its action deficit is their difference up to the normalisation. If both parts were non-negative after subtraction of the vacuum, (DEF_K) would hold with K = 1/s. Integrated, K = 1/s gives E_i(beta) >= E_i(beta_0) beta_0/beta, a fall no faster than a power. The published values give K about 3.3 at beta = 2.3 to 2.6, where 1/s is about 0.4 (GUIDE). So, if those values are right, the magnetic part of an excited level lies below the vacuum by about (K s - 1)/2, that is about 3, times its energy. The pointwise inequality is then false, not only unproved. What is true has to come from a cancellation between two terms that are each several times the energy.

**Way 2: a relative bound from locality.** The derivative of the slab operator in s is a sum of abs(B) local terms of norm at most 2 each. So - dE_i/ds <= 12 abs(B), and with E_i >= m: K <= 12 abs(B)/m (GUIDE: I did not prove the bound on each ordered level from (TM) alone). To remove the factor abs(B) one needs that an excited level differs from the vacuum only in a region whose size does not grow with the box, in the sense of the expectation of each local term. That is a clustering statement for excited levels. Stability theorems for gaps of quantum lattice systems prove such statements from a gap and a local gap condition (RECALLED: Bravyi, Hastings and Michalakis; Michalakis and Zwolak; not read here). The constant they give depends on the gap, K <= C m^(-p) with p > 0. Then - m' <= C m^(1-p), so m(s)^p >= m(beta_0)^p - p C (s - beta_0), and the bound ends at a finite coupling. This is Proposition B of row 677 (`gap-zf-box-x.md`; a zero-free radius that shrinks with the gap cannot cross the middle range) in another form. So Way 2 ends where Route Z ended.

**Way 3: convexity in the coupling.** F(t, B; .) and e(B; .) are convex. G = F - t e is a difference of two convex functions, and (VIR_K) is a one-sided bound on its first derivative. Convexity gives one-sided bounds on second derivatives of F and of e, and nothing on the derivative of the difference. Sums of the k largest log-eigenvalues are not convex in general. The class shows that nothing of this kind can work: in the Ising model of `gap-seed-shape.md` 4.1 every hypothesis of the lemmas holds at every J, the seed holds at small J (high temperature expansion, RECALLED) and fails at large J (two phases). By Theorem TR, read backwards, (VIR_K) with K of order log b fails on every interval of couplings that crosses the transition. So no proof of (DEF_K) can use the properties of the class only; by K7 it cannot use the group only.

**Stop.** (DEF_K) failed in three ways. The exact next statement of this attempt:

(VIR-log) For the Wilson SU(2) theory and beta_1 > 0 there are beta_0 <= 1/25600 and infinitely many even b such that (VIR_K) holds on the cube b^3 on [beta_0, beta_1], for the times [ceil(log_2 b), b/2], with integral of K at most log(b/(2 ceil(log_2 b))).

It is equivalent to nothing weaker that I know. It is implied by (LEV_K) with a constant K, which is the statement that the lattice beta function, read from every level of the box, is bounded away from zero on [beta_0, beta_1].

### 4.5 Lead (e): what a hand proof of one step would need

A step is an interval [s, s + delta] of couplings on the box b^3. The inequality to prove on it, at integer t, is (Lemma 4.2)

6 abs(B) (abar_(inf,B) - abar_(t,B)) <= K times the thermal mean of the energy at time t.

Both sides are of the size of the thermal sum, so they are exponentially small in t m. A hand proof cannot estimate each side and compare: it would need each to a relative precision of order one, that is, an absolute precision of order exp(-t m). It needs an identity that produces the ratio. In the continuum that identity is the trace anomaly: the dilation current gives the action deficit of a state at rest as its energy divided by the beta function. The lattice has no dilation. Its substitute is a comparison of the theory at (s, lattice of spacing 1) with the theory at (s', lattice of spacing 2), which is one block step of a renormalization map at a coupling of order one, with the two sides of the comparison equal up to a factor of order one in every level of the box. So lead (e) in the coupling direction returns to lead (a): the one step that is needed is a block step in the middle range with relative errors of order one. No such step is proved anywhere, and I see no way to one by hand. The number of steps is not the difficulty: about seven doublings, or an interval of couplings of length about 2.5.

## 5. Part 2, attempt 2: the scale direction and the first critical coupling (C-B)

### 5.1 Theorem CRIT (PROVED GIVEN Theorem SH, Proposition Delta, and `gap-seed-sc.md` Theorem 1 (iii))

For t' in (0, 1/25] let Sigma(t') be the set of couplings beta > 0 for which there is an integer a >= 3 with S(a; (4a)^3; beta) < t'. Let beta*(t') be the supremum of the beta with (0, beta) inside Sigma(t').

**Theorem CRIT.**
(a) Sigma(t') is open.
(b) Sigma(t') contains (0, 1/12800). So beta*(t') >= 1/12800.
(c) For every beta < beta*(1/25) the cubes at beta have a uniform gap: inf over L >= 4a of m(L^3) > 0, with a the seed size at beta.
(d) If beta* := beta*(t') is finite, then S(a; (4a)^3; beta*) >= t' for every a >= 3. For t' = 1/25 also Delta(a^4; beta*) > 6.1 x 10^(-4) for every a >= 3.
(e) Let beta* = beta*(1/25) be finite and t'' < 1/25. If beta_j tends to beta* and a_j are integers with S(a_j; (4a_j)^3; beta_j) < t'', then a_j tends to infinity.

Proof. (a) For a fixed a, S(a; (4a)^3; beta) = Z(a, (4a)^3; beta)/lambda_0^a - 1 is continuous in beta (Lemma 4.1 (a)). Sigma(t') is a union over a of open sets. (b) Let theta = 12800 beta < 1. As in the proof of Corollary TR1, Delta(a^4) <= 0.01 a^4 theta^(4a)/(1 - theta^(4a)) for a >= 4, which tends to 0 as a grows. By Proposition Delta, g(a; (4a)^3) <= 64 Delta(a^4). (c) Theorem SH, line r = 4. (d) Every beta < beta* is in Sigma(t'). If beta* were in Sigma(t'), then by (a) so would be an interval around it, and (0, beta* + eps) would lie in Sigma(t'). The bound on Delta: g(a; (4a)^3) <= 64 Delta(a^4) and g >= log(1.04) > 0.0392. (e) If not, a subsequence has a_j = a fixed, and by continuity S(a; (4a)^3; beta*) <= t'' < 1/25, against (d). QED

The same holds with the shape r = 2 and the threshold 1/1650, or with any finite set of shapes of the table of `gap-seed-shape.md` 1.5.

**What it says.** The middle range, in the coupling, is the question whether beta*(1/25) is finite. If it is, beta* is a critical coupling of the lattice theory in the sense of the class: at beta* every cube of ratio 4 has a thermal sum of at least 1/25, the Casimir free energy of every symmetric torus is above 6.1 x 10^(-4), and the size of the seed box diverges as beta rises to beta*. A first-order point with two phases and a point with an infinite correlation length are both of this kind. So:

(NOCRIT) beta*(1/25) is infinite for the Wilson SU(2) theory.

(NOCRIT) gives the gap of all cubes at every coupling. By Corollary TR1, (VIR-log) for every beta_1 gives (NOCRIT) (the corollary gives S(a; (2a)^3) < 1/1650, and then S(a; (4a)^3) <= 0.0396 < 1/25). By K7 (RECALLED) the same statement is false for the weight with an adjoint term on its first-order line. So (NOCRIT) is a statement about the Wilson weight and not about the group.

### 5.2 (CAS): why it is not attacked

1. (PROVED, Proposition Delta.) In a model of the class with no uniform gap, Delta(a^4) stays above 6.1 x 10^(-4) at every size. The class contains such models (`gap-seed-shape.md` 4.1 and 4.2). So no property of the class gives theta < 1.
2. (GUIDE.) At the ultraviolet end theta tends to 1. In a small periodic box the flat connections form a set of positive dimension, the integral over them is not Gaussian in every direction, and Delta(a^4) is c_1 log(1/g^2(a)) + c_2 to leading order, with g(a) the running coupling at the size a (RECALLED: Luscher; van Baal; the constants are not computed here). One doubling changes it by about - 2 c_1 b_0 g^2 log 2, which tends to 0 with g. So (CAS) with one theta < 1 can hold only from a size where the coupling is of order one, and M is of order one.
3. On the interval that is left, theta < 1 is one block step at a coupling of order one with a relative error below one. This is the statement that lead (e) needs (Section 4.5).

So (CAS) has the same strength as the seed and I name no lemma under it. Its exact form in the coupling is (NOCRIT).

## 6. The flux split (C-C): an identity and the independence of the two parts

**Identity FL (PROVED from (TM) and (TM-c)).** Time is direction 0, the box is B, and C_1, C_2, C_3 are the centre flips of (TM-c). They are unitary involutions that commute with T. They commute with each other, because each multiplies by -1 the links of one direction on one plane. For k in Z_2^3 put C^k = C_1^(k_1) C_2^(k_2) C_3^(k_3), Z[k] := Tr(T^t C^k), P_0 := the product of the (1 + C_i)/2 = (1/8) sum over k of C^k, the projection on the sector of zero electric flux. Let 1 + S_0 := Tr(T^t P_0)/lambda_0^t and U := Tr(T^t (1 - P_0))/Tr T^t = (1/8) sum over k not 0 of (1 - Z[k]/Z). Then

S_0 >= 0, 0 <= U <= S/(1 + S) < 1, and 1 + S = (1 + S_0)/(1 - U).

Proof. The top eigenvector is strictly positive, each C_i maps positive functions to positive functions and commutes with T, and the top eigenvalue is simple. So the top eigenvector is fixed by each C_i and lies in the range of P_0. P_0 commutes with T, so Tr(T^t P_0) is the sum of lambda_i^t over an eigenbasis of the range of P_0, which contains the vacuum: S_0 >= 0. Tr(T^t (1 - P_0)) is a sum of lambda_i^t over excited states only, so it is at most lambda_0^t S. Then Tr(T^t P_0) = Tr T^t (1 - U). QED

For k a unit vector, Z[k] is the partition function with one twisted stack in the plane (0, i), by (TM-c). For the other k it is defined by the trace; I did not need its form as an integral.

**Consequences.** (1) S <= t if and only if (1 + S_0) <= (1 + t)(1 - U). (2) If U <= t/3 and S_0 <= t/3 with t <= 1, then S <= t. (3) The seed forces U <= t/(1 + t): each of the three single twists has 1 - Z[k]/Z <= 8t.

**The two parts are independent in the class.**
- U small, S_0 not small (PROVED GIVEN the strong-coupling seed and `gap-seed-shape.md` 4.1): take the product of the Wilson SU(2) theory at a small coupling with an independent four-dimensional Ising model at large J on the sites. The partition function is the product, so it is symmetric; the transfer operator is the tensor product, positive, trace class, with a simple top eigenvalue; the centre flips act on the gauge factor only. Then U is the U of the gauge factor, which is at most S_gauge and small, and S_0 >= S_Ising, which tends to 1.
- S_0 small, U not small (RECALLED): the Z_2 theory at large beta, where U tends to 7/8.
So neither part gives the other without the group and the weight. The seed is both.

**Remark Y (a sketch; not proved here).** One could ask for a theorem like Theorem S for the sector of zero flux alone. The crossed direction does not allow it. Seen from a space direction, the projection on zero electric flux of the first direction is a sum over the two values of a magnetic twist of the slice. So the function to which Lemma E would apply is a trace of powers of a direct sum of transfer operators of twisted slices (given the transfer operator for twisted weights, Lemma 1.1 of `gap-seed-check.md`, and a form of (TM-c) for several stacks, which I did not write out). Its top eigenvalue is that of the untwisted slice. When the twist costs nothing, the twisted slices have top eigenvalues almost equal to it, and the thermal sum of the direct sum is near the number of twisted sectors, up to 7. This is 't Hooft's duality at a finite size: where electric flux is heavy, magnetic flux is light, and a doubling lemma for one sector pays for the other.

By rule 0a the flux half is not attacked here: its open step is (TUBE') of row 697, and (VORT) of run 2.

## 7. Part 2, attempt 3: curvature at a block scale (C-D), ended by a counterexample

**Setting.** Lambda is the set of links of a torus with all sides at least 3. M = SU(2)^Lambda with a product of bi-invariant metrics, one positive multiple for each link. For a tangent vector X = i omega (n . sigma), n a unit vector, at the identity of one factor, exp(sX) has trace 2 cos(s omega). With the metric abs(X)^2 = -2 tr(X^2) = 4 omega^2 the group is the sphere of radius 2 and Ric = (1/2) times the metric. The measure has the density exp(-Psi), Psi = -beta sum over plaquettes of x_p + W, x_p = (1/2) tr U_p, where W is the logarithm of a blocking weight, or 0.

**Proposition BE (PROVED).** Let l_0 be a link and U# the configuration with U_(l_0) = -1 and U_l = 1 for every other link. For a tangent vector X at the link l_0:

(Ric + Hess Psi)(X, X) at U# = (1/2 - 3 beta/2) abs(X)^2 + Hess W(X, X).

The value does not depend on the multiples of the metric. So if W does not depend on U_(l_0), the Bakry-Emery tensor of the measure has a negative direction at U# for every beta > 1/3.

Proof. The six plaquettes through l_0 are distinct (sides at least 3) and each contains l_0 once. At U# each of them has U_p = -1, a central element. Move U_(l_0) to exp(sX) U_(l_0) (or U_(l_0) exp(sX), according to the orientation; the result is the same because -1 is central and the trace is a class function). Then x_p(s) = (1/2) tr(-exp(sX)) = -cos(s omega), and the second derivative of -beta x_p at s = 0 is -beta omega^2 = -(beta/4) abs(X)^2. The curve s -> exp(sX) U_(l_0) is a geodesic of every bi-invariant metric, so the second derivative along it is the Hessian. Six plaquettes give -(3 beta/2) abs(X)^2. The plaquettes that do not contain l_0 do not move. The Ricci tensor of a product is the sum of the Ricci tensors of the factors, and the Ricci tensor of a factor does not change when its metric is multiplied by a constant. QED

**What it kills.** (BE-block) as stated in C-D, for every blocking whose weight leaves one link free, for example a decimation. For a blocking whose weight depends on every link, the proposition gives the price: Hess W must be at least (3 beta/2 - 1/2 + rho) on every link direction at the configurations U#. Then the blocking weight pins every link to within about beta^(-1/2), the conditional law is almost a point, and the law of the block variables is the full problem again. The same computation for U(1) gives -6 beta (d theta)^2 with no Ricci term, and for the weight of K7 it gives a number of the same size. So the positive curvature of SU(2) is worth the range beta < 1/3 of the pointwise criterion, at every scale, and nothing in the middle range. U# has a small probability at large beta; a criterion that weighs configurations by their probability is a mixing hypothesis of the kind of (W) (row 691) and is covered there.

Test: (i) the group enters through Ric = 1/2; (ii) for U(1) the criterion fails at every beta > 0, and U(1) has a gap at small beta all the same, so the criterion is not the reason for a gap; (iii) the line that breaks is the lower bound on the Hessian; (iv) K7: the same Hessian bound.
