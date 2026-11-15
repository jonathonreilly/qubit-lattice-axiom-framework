lead: anthropic/claude-opus-5-5/max mac-mini-worker
lease_until: 2026-11-15T13:45Z

# gap-unit-check-opus: line-by-line check of row 988 (`library/gap-unit-max.md`)

Queue row 991 (`FINISH.md` line 1069). Check item, no new attack. Worker: Claude Opus 5.5 max, Mac mini worker 3. Started 2026-11-15T01:45Z at pinned commit d0d88c388. Author of the checked file: Claude Fable 5.2 max (row 988). This check is a different model on the same text; it is not an independent derivation of the lane's results except where a step below is re-derived by a different argument, and each such step says so.

Marks: HOLDS, HOLDS AFTER CORRECTION, FAILS, each with the line of `library/gap-unit-max.md` it refers to.

## Plan (at most eight steps; one per response, each appended before the next)

1. Read `FINISH.md` rules (efficiency, build on published work) and `library/gap-unit-max.md` in full; record the exact statements to be checked with their line numbers. Grep `library/open-core.md` and FINISH rows for overlap.
2. Check Identity G (S = 0 at beta_t = 0 for every beta_s; X as a beta_t integral).
3. Check Lemma ORD (S(t; B) has a zero of order 4t at beta = 0).
4. Check Lemma FLOOR (sector form).
5. Check the consequence in 7.1.
6. Check the Schwarz form of the Route Z transport, and write out the Borel-Caratheodory step (zeta_n := Z/Z(beta = 0), zeta_n(0) = 1, log|zeta_n| <= c |beta| Vol on D' gives |log zeta_n| <= C Vol on D).
7. Verdict table, corrections, what stays open; RESULT line.

## Status

- 2026-11-15T01:45Z: Step 1 in progress.
- Step 1 written (below).

## Step 1. Sources, statements under check, overlap

**Read.** `GOAL.md` in full; `FINISH.md` lines 1-84, 299-356 (Joining, Working efficiently, Rules) and rows 988, 991, 992 (lines 1066-1070); `library/gap-unit-max.md` in full (369 lines); `library/gap-crux-restate.md` Section 1 (L29-46), 3.1 Theorem D (L90-116), 3.4 setting and Lemmas K, X, E, Theorem S (L170-201); `library/gap-hcphys-max.md` 4.2 (L131-163) for S, X, U; `library/gap-skeleton-max-b.md` L299-308 (Theorem LP, Lemma HM, Corollary 4), L347-358 (Theorem Z), L460-463 (Theorem ZB).

**Statements under check** (line numbers of `library/gap-unit-max.md`):

| Item | Lines | Claimed mark in the file |
|---|---|---|
| Identity G (a), (b) and proof | 199-209 | PROVED by hand, not checked |
| Lemma FLOOR and its use (17.04, pi, pi/2) | 174-186 | PROVED (one line) |
| Lemma ORD and proof | 286-296 | PROVED given two RECALLED facts, not checked |
| Schwarz form of the transport | 298-300 | PROVED (classical) |
| Consequence in 7.1 (zero-freeness gives (SEED)) | 302-310 | ARGUED; Borel-Caratheodory step not written |
| Borel-Caratheodory step asked by N1 | 350-352 | to be written here |

Definitions used (from `gap-crux-restate.md` Section 1 and 3.1): Z(n) = int exp(-beta A) dU on the torus with sides n = (n_1, ..., n_4), A = sum over plaquettes of (1 - (1/2) tr U_p), F = log Z; (TM): Z(n) = Tr T^(n_mu), T positive trace class with simple top eigenvalue; S(k; B) = sum over i >= 1 of (lambda_i/lambda_0)^k; Phi(n) = 16 F(n^4) - F((2n)^4); Theorem D (b) proof: 1 + S(n; B_2) <= Z(n, 2n, 2n, 2n)^2 / Z((2n)^4).

**Overlap (rule 0a).** `library/open-core.md`: no line names Identity G, Lemma ORD, Lemma FLOOR, the Schwarz form or this Borel-Caratheodory step (its one hit for "Borel", L231, is Borel component-locality, unrelated). `library/l17c.md`: no hit. `FINISH.md`: these names occur only in rows 988 (the source), 991 (this row) and 992 (the reading N4, a different item). Prior uses of Borel-Caratheodory in the lane: Theorem Z step 3 (`gap-skeleton-max-b.md` L355), Theorem ZB (L463), and row 681's repair (Lemma S: a Harnack chain and Borel-Caratheodory, after its defect Z1: no bounded domain satisfies (TUBE)). Step 6 compares with these. This row is a check, not an attack, so rule 0a does not stop it.

## Step 2. Identity G (`gap-unit-max.md` L197-213): HOLDS (reading note on abar_t)

**Setting checked (L199-200).** B is a periodic spatial box with |B| sites, B x t the periodic torus with t >= 1 time steps. Each of the |B| t sites carries three temporal plaquettes (0, i), so A_t has 3 |B| t terms: correct. The transfer operator in temporal gauge is T(beta_t) = e^(-V/2) K_(beta_t) e^(-V/2) on gauge-invariant functions of the spatial links, V = beta_s A_3, A_3 the spatial action of one slice (3 |B| plaquettes). K_beta has kernel prod over links l of exp(-beta (1 - (1/2) tr(U_l U'_l^(-1)))), averaged over the gauge group of the slice (the integral over the temporal links). This is (TM) of `gap-crux-restate.md` L33 with two couplings; nothing in that construction uses beta_t = beta_s.

**(a) HOLDS.** At beta_t = 0 the temporal links occur in no factor, so each integrates to 1. The spatial links at different times then occur in disjoint factors exp(-beta_s A_3(U(tau))), so Z(B x t) = Z_3(B)^t with Z_3(B) = int exp(-beta_s A_3) dU > 0. In operator form: K_0 has kernel 1, so K_0 = P_0, the projection on constants (Haar probability measure), and T(0) = |psi><psi| with psi = e^(-V/2), a gauge-invariant function. So T(0) has rank one, lambda_0 = ||psi||^2 = Z_3(B), lambda_i = 0 for i >= 1, and S(t; B) = 0 for every t >= 1.

**(b) HOLDS, with this reading:** abar_t(s) := <A_t>_(s) / (3 |B| t), the expectation of A_t at temporal coupling s, divided by the number of temporal plaquettes. ("Mean" must include the average over the three orientations: when the sides of B differ, the three orientations need not have the same expectation. With this reading the identity holds for every box.) Derivation, written out:
1. X(t; B) = log(1 + S(t; B)) = log Z(B x t) - t log lambda_0, since Z(B x t) = Tr T^t = lambda_0^t (1 + S(t; B)).
2. log Z(B x t) is real analytic in s = beta_t (a finite-dimensional integral of an entire integrand, Z > 0), and d log Z(B x t)/ds = -<A_t>_(s) = -3 |B| t abar_t(s).
3. lambda_0(s) is real analytic on a neighbourhood of [0, infinity). Input (RECALLED, classical; Kato, analytic perturbation of an isolated simple eigenvalue): s -> T(s) is holomorphic in operator norm (the kernel is entire in s and bounded on compact sets of s, on a probability space), and lambda_0(s) is isolated and simple. Simplicity: for s > 0 the gauge-averaged kernel is at least e^(-2 s (number of links)) > 0 (Jentzsch); at s = 0 by (a). For s >= 0 the class function exp((s/2) tr g) has non-negative character coefficients (2 I_(2j+1)(s)/s >= 0), so T(s) >= 0 and lambda_0 = ||T(s)||.
4. abar_inf(s) := lim over t of abar_t(s) exists and equals -(1/(3 |B|)) d log lambda_0/ds. Proof: f_t(s) := (1/t) log Z(B x t) is convex in s (log of a Laplace transform) and f_t -> log lambda_0 pointwise, because S(t; B) <= S(1; B) r_1^(t-1) -> 0. For convex differentiable f_t with differentiable pointwise limit f: for h > 0, (f_t(s) - f_t(s - h))/h <= f_t'(s) <= (f_t(s + h) - f_t(s))/h; let t -> infinity, then h -> 0. This is used at interior points s > 0 only, where s - h > 0 for small h. The value at s = 0 is not needed: step 5 integrates over (0, beta_t], the integrand is bounded (0 <= abar <= 2), and X is continuous at s = 0. The file's proof gives exactly this argument in one sentence (L208-209).
5. So dX/ds = -3 |B| t abar_t(s) + 3 |B| t abar_inf(s) on [0, beta_t], X is C^1 there, and X(t; B)(beta_s, 0) = 0 by (a). Integrating gives (b).

**What it does not show.** Nothing about the sign or size of abar_inf - abar_t. The file says so (Route 2, L215-229). The remark at L211-213 (the path keeps beta_s fixed; it differs from Theorem D (f)) is correct as a description.

Verdict: **Identity G HOLDS** (L202-209), with the reading of abar_t above. The two inputs are classical and named: Kato's analytic perturbation theorem and Jentzsch's theorem (both RECALLED, as in (TM)).

## Step 3. Lemma ORD (`gap-unit-max.md` L286-296): HOLDS (two notes; recalled fact (ii) replaced by an explicit bound)

Statement (L287-290): SU(2) Wilson, periodic box B with all sides >= 4, t >= 1: S(t; B) is analytic in beta near 0 with a zero of order >= 4t; the same in beta_t at fixed real beta_s. Checked line by line.

1. **Character expansion (L291-292).** With Haar probability measure, dg = (2/pi) sin^2(theta) d(theta), and (1/pi) int_0^pi e^(beta cos theta) cos(k theta) d(theta) = I_k(beta), the coefficient of chi_j in e^(beta cos theta) = e^((beta/2) tr g) is I_(2j) - I_(2j+2) = (2j+1) 2 I_(2j+1)(beta)/beta. So convolution with the one-link kernel e^(-beta) e^((beta/2) tr g) acts on the spin-j matrix coefficients as the scalar e^(-beta) 2 I_(2j+1)(beta)/beta = c(beta) rho_j(beta), with c(beta) = e^(-beta) 2 I_1(beta)/beta and rho_j = I_(2j+1)/I_1. Since I_n(z) = (z/2)^n/n! (1 + O(z^2)), rho_j has a zero of order exactly 2j at 0: correct. **Note 1 (normalisation, harmless):** the file writes K_beta = sum_R rho_R P_R and drops the scalar c(beta)^(number of links). That scalar is analytic, equals 1 at 0, and has no zero for |beta| < j_(1,1) = 3.83 (zeros of I_1 lie on the imaginary axis, I_1(iy) = i J_1(y)). It cancels in every ratio lambda_i/lambda_0, so S(t; B) is unchanged. With the scalar kept, the identity reads K_beta - c(beta)^(#links) P_0 = beta^4 N(beta).
2. **Gauss's law (L292-293).** P_R maps gauge-invariant functions to zero unless, at each site x, the tensor product of the spins of the links at x contains the trivial representation. A site with exactly one non-trivial link fails this (V_j, j >= 1/2, has no invariant vector). So every site touched by supp R has at least two links of supp R; a finite graph with all degrees >= 2 contains a cycle: correct.
3. **Cycle length >= 4 (L293).** A cycle on the periodic box either lifts to a closed cycle of Z^3, which is bipartite with girth 4, or its lift has a non-zero displacement that is a multiple of a side, so its length is at least that side >= 4: correct. (With sides >= 3 the bound would be 3, so the hypothesis "sides >= 4" is the right one.) Hence the order of rho_R = sum over l of 2 j_l >= |supp R| >= 4.
4. **Analyticity of N in trace norm (L294); replaces RECALLED fact (ii).** For |beta| <= 1: |I_n(beta)| <= (|beta|/2)^n e^(1/4)/n! and |I_1(beta)| >= (|beta|/2)(1 - 0.14), so |rho_j(beta)| <= 1.5 (|beta|/2)^(2j)/(2j+1)!. ||P_R||_1 <= prod over l of (2j_l + 1)^2. So sum over R of |rho_R(beta)| ||P_R||_1 <= prod over l of (1 + sum over n >= 2 of 1.5 n^2 (|beta|/2)^(n-1)/n!) < infinity, uniformly on |beta| <= 1. Each term rho_R(beta)/beta^4 with R allowed is analytic on |beta| <= 1 and, by the maximum principle, bounded there by its maximum on |beta| = 1. So N(beta) = sum over allowed R != 0 of (rho_R(beta)/beta^4) P_R converges uniformly in trace norm and is analytic on |beta| < 1. The radius is box-dependent through the number of links only in the size of the bound, not in its existence; Lemma ORD claims nothing uniform.
5. **Rank-one part (L295).** T_0 := A P_0 A with A = e^(-beta A_3/2) (multiplication operator; **Note 2:** the file writes "integral e^(-beta V)", with V here the unscaled spatial action of one slice, whereas Route 2 at L200 used V for beta_s times it; harmless clash of notation). T_0 = |A1><A1|, eigenvalue Z_3(beta) = int e^(-beta A_3) dU, entire with Z_3(0) = 1, so non-zero on a (box-dependent) disc. T_0 (1 - Pi_0) = 0 for Pi_0 = |A1><A1|/Z_3: correct.
6. **T' = O(beta^4) in trace norm (L296).** T = T_0 + beta^4 M, M = c^(#links) A N A analytic in trace norm. The Riesz projection Pi(beta) = (1/2 pi i) closed integral over |z - Z_3(beta)| = 1/2 of (z - T)^(-1) dz is analytic near 0, and Pi - Pi_0 = (1/2 pi i) closed integral of (z - T)^(-1) beta^4 M (z - T_0)^(-1) dz has trace norm O(beta^4). So T' = T(1 - Pi) = T_0 (Pi_0 - Pi) + beta^4 M (1 - Pi) has ||T'||_1 = O(beta^4): correct.
7. **Order 4t (L296).** S(t) = Tr T'^t / lambda_0^t (Pi commutes with T; T' acts on the range of 1 - Pi with the eigenvalues lambda_i, i >= 1). |Tr T'^t| <= ||T'||_1^t = O(beta^(4t)), and lambda_0 = Z_3 + O(beta^4) is non-zero near 0. Tr T'^t is analytic, so S(t) is analytic with a zero of order >= 4t: correct. The order is exactly 4t whenever the spin-1/2 plaquette loop gives an eigenvalue of order (beta/4)^4 (expected; not needed).
8. **The beta_t clause (L289-290).** At fixed real beta_s, A = e^(-beta_s A_3/2) is fixed and T_0 has the fixed eigenvalue Z_3(beta_s) > 0; steps 4-7 run in beta_t unchanged: correct.

The use in 7.1 (L304): G_n := 2 log Z(n, 2n, 2n, 2n) - log Z((2n)^4) = 2 X(n; (2n)^3) - X(2n; (2n)^3), checked from Z(n, 2n, 2n, 2n) = lambda_0^n (1 + S(n)) and Z((2n)^4) = lambda_0^(2n) (1 + S(2n)). X(k) = log(1 + S(k)) has a zero of order >= 4k, so G_n has a zero of order >= 4n at 0, for n >= 2 (sides 2n >= 4): correct.

Verdict: **Lemma ORD HOLDS** (L286-296), with Notes 1-2 (normalisation scalar dropped, notation V). RECALLED fact (i) (Kato: analytic perturbation of an isolated simple eigenvalue and its Riesz projection) stays a classical input. RECALLED fact (ii) is not needed: item 4 gives the trace-norm analyticity from the character expansion directly.

## Step 4. Lemma FLOOR (`gap-unit-max.md` L174-186): HOLDS

Statement (L174-177): T >= 0 trace class with simple top eigenvalue; the trace runs over a T-invariant subspace H' that holds the top eigenvector; if H' holds an eigenvector of level E (eigenvalue lambda_0 e^(-E)) other than the ground state, then S(a) >= e^(-aE). Proof (L178): S(a) is a sum of non-negative terms (lambda_i/lambda_0)^a over the eigenvectors in H' other than the ground state, and one term is e^(-aE). Correct. It is the sector form of r_1^k <= S(k; B) (`gap-crux-restate.md` L45) and of Theorem D (c) read backwards. Simplicity of the top eigenvalue is used only to define S relative to one ground state.

Numbers (L176-177), checked by hand and by a one-line evaluation (arithmetic only, not a proof step): with E = m((2n)^3) and a = n, s < 1/5041 gives e^(-nm) < 1/5041, so n m > log 5041 = 2 log 71 = 8.5254 > 8.52, and side times gap = 2nm > 17.05 > 17.04: correct. The same formula at threshold 1/1650 gives 2 log 1650 = 14.82, which matches "14.8" of row 712 P1 quoted at L273.

Use (L180-186). Arithmetic: untwisted level 2 pi/side with side 2n gives nE = pi and e^(-pi) = 0.0432 > 0.04; twisted level pi/side gives nE = pi/2 and e^(-pi/2) = 0.2079 > 0.2: correct. The two level positions are RECALLED (small-box perturbation theory, twist-eaters) and marked so in the file; this check does not verify them. The remark that Lemma X needs a < b (L185-186) is correct (`gap-crux-restate.md` L182: the bound (b - a) kappa(b) <= g(a, b) is for a < b, and Lemma E, Theorem S, Corollary S3 use a <= b/2). "17.04 against pi" (L184) compares 17.04 with side times gap = pi in the twisted box (2 pi untwisted); the reading is right, and in both cases the perturbative value lies below the floor.

Verdict: **Lemma FLOOR HOLDS** (L174-178); the numbers at L176-177 and L181-183 are correct.

Order change: the consequence in 7.1 uses the Schwarz form and the Borel-Caratheodory step, so Step 5 below checks those and Step 6 checks the consequence.
