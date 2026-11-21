lead: anthropic/claude-fable-5-2/max mac-mini-worker
lease_until: 2026-11-11T22:45Z

# gap-mid-max: an attack on the middle range of the mass gap (queue row 708)

Research-stage working state. It grants no status. Nothing here is a public claim.

Pinned at commit 43010014c on `claude/ym4d-hard-route`. Author run, not a check.

**Lead note (row 709, 2026-11-11; Claude Opus 5.5, lead session).** Sections 4 to 8 and 10 are checked line by line by Claude Opus 5.5 high (`library/gap-mid-check.md`; same provider, different model). No statement fails. Theorem TR, Remarks CH and LEV, Proposition Delta, Corollary TR1, Theorem CRIT, Identity FL, Lemma M, Proposition MIX and Lemma INF hold. Five hold after correction, and no correction changes a threshold, a constant used downstream or a conclusion: (1) Theorem DOB: the sentence "two links of a common plaquette have positions that differ by at most 1" is false for the slab [a - 1, a]; measure positions on the circle R/aZ, or note that every link of that slab is in D; d at least floor(a/2) - 1 stands. (2) Lemma DC: fact (c) needs the mass accounting (end mass at most alpha M), and Step 3 needs that osc(f_i) does not increase. (3) Proposition BE: read abs(X)^2 as -2 tr X^2; it proves only that curvature is worth at most beta = 1/3; the positive side below 1/3 is not proved. (4) Lemma 4.2: write the two-line proof on derivatives of convex limits; abar_inf is defined outside the countable set only. (5) Lemma 4.1 (b): add the dominated-convergence line; t above 3 suffices (t at least 4 is a convenience). The check re-derived the constants 8, 96, 768 and the example (1/36, 90), and found a second example (beta = 1/54, a = 50). Theorem DOB is new in this repository (a wider range than `gap-seed-sc.md`, a worse rate, another route); no proof uses a RECALLED or GUIDE statement; K7 enters no proof. Written in steps; each step is appended before the next is thought through (save rule, row 675).

## 0. Log of the run

- 2026-11-11 10:45 UTC. Started. No earlier work of this item in the file at the pinned commit. Reading the files the row names.
- Step 1 done: reading, duplicate check, Part 1 and the first status block (Sections 1 to 3).
- Step 2 done: attempt 1, the coupling direction (Section 4).
- Step 3 done: attempt 2 (Section 5), the flux split (Section 6), attempt 3 (Section 7).
- Step 4 done: Section 8 and the final status block (Section 9). A last pass over the proofs follows; corrections, if any, are marked in the text.
- Step 5 done: last pass (small corrections applied in place: the range of t in the notation, Remark CH, the wording of (VIR-log)); candidate C-E added to Part 1; Section 10 added (Theorem DOB, the seed for beta < 1/18, with Dobrushin's comparison estimate rebuilt).

## 1. Position, reading state, duplicate check, credits

**Kind of result.** No proof of the seed at a coupling of order one. One proof of the seed in a new range, beta < 1/18 (Theorem DOB, Section 10; strong coupling). The file gives (a) five candidate statements with the test, (b) attempts on three of them, each carried to a proof of what can be proved and to one named open statement, (c) a status block and proof items.

**Read in full:** FINISH row 708; GOAL.md; `library/gap-crux-restate.md`; `library/gap-seed-shape.md`; `library/prior/gap-seed-size.md`; `library/prior/gap-seed-lit.md`; `library/gap-skeleton-final.md` Sections 12 and 13. **Read in part:** `library/gap-seed-limit.md` and `library/gap-seed-sc.md` (statements only); `library/prior/gap-crux-lit-2.md` (headings and the synthesis, lines 327 to 417); `library/gap-skeleton-max-b.md` lines 134, 164 to 185, 205 to 212, 257 to 260, 412 to 415. **Not read:** every primary paper; the Sussman-Alpoge repository (the row forbids network access for this item, and the three literature digests report that the outline and the account hold no statement on the physical gap). Nothing was fetched from the network.

**Duplicate check (rule 0a).** Searched `library/open-core.md`, the FINISH rows and `library/gap-*.md`, `library/prior/gap-*.md` for: virial, Gronwall, Bhanot, mixed action, adjoint coupling, finite-size shift, trace anomaly, interaction measure, Hellmann, step scaling, Dobrushin comparison, Casimir, pressure, SO(3), electric flux, characteristic. `open-core.md` has no hit. Matches that bind this file:

- Run 2 (`gap-skeleton-max-b.md`) already lists, as heuristic candidates with their kill lines: A4 transport in the coupling with crux (DEF) (lines 164 to 170), A5 step scaling with crux (STEP) (172 to 178), A6 flux duality with crux (VORT) (180 to 185), A10 the dilation identity (207 to 211), and the warning K7 (line 134: the mixed fundamental and adjoint action has a critical end point near the Wilson axis; recalled from Bhanot and Creutz). Its Lemma 2 (line 259) is the integral of the plaquette shift.
- Run 1 (`gap-skeleton-max.md` line 80): the third test (an adjoint Higgs field).
- Row 677 (`gap-zf-box-x.md`): (HS-sup), the gradient bound for the Poisson equation of the action. Row 691: (W). Row 697: (TUBE').
- So the leads (a), (b), (c) of the row are A5, A6, A4 of run 2. I do not state them again as heuristics. What is new below: each is put in the finite form that Theorems S and SH make possible, the implications are proved, and the open statement of each is an inequality of order one with no small number in it. I do not attack (HS-sup), (W), (TUBE') or (VORT).

**Credits.** Tadeusz Balaban (the ultraviolet part, not used in a proof here). Sussman and Alpoge with Claude and Codex (the account; not used in a proof here). Claude Fable 5.2 max, rows 669, 670, 697 (candidates A4 to A10, K7, Lemmas A, K, X, E, Theorems S, D, F). Codex gpt-6-astra, row 699 (Lemma E'). Claude Fable 5.2 medium, rows 701, 705 (the strong-coupling seed; Lemma E2, Theorem SH, Theorem D-shape). Claude Opus 5.5, rows 698, 703, 704 (checks). Osterwalder and Seiler, Luscher (transfer operator, through row 667). 't Hooft (twists and flux). Bhanot and Creutz (the mixed action; RECALLED). Bakry and Emery; Shen, Zhu and Zhu (curvature at small beta; RECALLED). Dobrushin (uniqueness condition and comparison estimate; the argument is his, rebuilt by hand in Section 10). Kazakov and Zheng (the bootstrap of the loop equations; known here through the two digests named in C-E).

**Marks.** PROVED = proved by hand in this file from the named inputs; not checked by another model. PROVED GIVEN (X). GUIDE = estimate or recalled number, used in no proof. RECALLED = a known fact used only in a test. OPEN.

**Notation.** As in `gap-crux-restate.md` Section 1 and `gap-seed-shape.md` Section 1. Box B = (b_1, b_2, b_3), abs(B) = b_1 b_2 b_3, all sides at least 3. T_B(beta) is the transfer operator, lambda_0 > lambda_1 >= ... its eigenvalues, rho_i = lambda_i / lambda_0, E_i = log(1/rho_i). For real t >= 3 (T^3 is trace class, so the sum converges):

G(t; B; beta) := log(1 + sum over i >= 1 of rho_i^t) = log Tr T_B^t - t log lambda_0.

For integer t >= 3 this is g(t; B) = log Z(t, B) - t e(B) = log(1 + S(t; B)). F(n) = log Z(n). f = inf F(n)/abs(n). Delta(n) = F(n) - f abs(n) >= 0. abar_n = mean plaquette action on the torus n. Thresholds t(r) of Theorem SH: t(2) = 1/1650, t(4) = 1/25.

## 2. Part 1: five candidate statements

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

- Proposition Delta (Section 4.3, PROVED GIVEN Theorem SH): for every a >= 3 and r = b/a > 1, S(a; b^3) <= exp(r^3 Delta(a, a, a, a)) - 1. So Delta(a^4) <= 6.1 x 10^(-4) at one a gives the seed at r = 4. In a model of the class with no uniform gap, Delta(a^4) > 6.1 x 10^(-4) for every a >= 3.
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

**C-E. A positivity certificate over the local equations of the Wilson weight (the bootstrap form; not one of the row's leads; added after Section 8 was written).**

- Setting. Q is a cube of side q <= a - 1 in Z^4. It embeds without wrapping in the tori (a, B) and (2a, B) when the sides of B are at least a. A state on Q is a probability law omega on SU(2)^(links of Q). (SD_s): at every link l whose six plaquettes lie in Q, the one-link conditional law of omega is the Gibbs one at the coupling s (density proportional to exp(s sum of x_p) with respect to Haar measure). In the form of an integration by parts this is omega(L_l f) = 0 for smooth f, with L_l f = Delta_l f + s <grad_l (sum of x_p), grad_l f>: the loop equations of the Wilson weight (the equivalence of the two forms is standard and is not proved here). (SYM): omega is the restriction of a law on a periodic torus with all sides at least a, or on Z^4, that is invariant under translations and lattice symmetries and is reflection positive.
- (BOOT_eps) at (a, q, beta): for every s in (0, beta], any two states on Q with (SD_s) and (SYM) give each central plaquette of Q mean values that differ by at most eps.
- What it gives: the restrictions to Q of the Gibbs measures of the tori (a, B) and (2a, B) are two such states (the remark behind Lemma M). So abs(abar_(2a,B) - abar_(a,B)) <= eps, and as in Proposition MIX, Phi_B(a; beta) <= 12 a abs(B) beta eps. The seed at r = 2 needs eps of about 6 x 10^(-4)/(96 a^4 beta).
- (i) The group and the weight enter through (SD_s): the equations contain the gradient of the Wilson weight, and for SU(2) products of traces reduce by tr A tr B = tr AB + tr AB^(-1) (as read in `prior/gap-crux-lit-nonab.md` line 164 and `prior/gap-crux-lit-cross.md` lines 55 to 59, on the bootstrap papers of Kazakov and Zheng). (ii) U(1) at weak coupling: the two tori differ at the plaquette by a power of a (RECALLED), so (BOOT_eps) is false for the eps that is needed; Z_2 at its transition: two states. (iii) A proof would be a certificate: a finite identity that writes eps minus the difference as a sum of squares plus combinations of the equations (SD_s). Such a certificate is specific to the weight. (iv) On the line of K7 the two phases are two states with (SD) and (SYM) for that weight, so no certificate exists there, and the equations of the Wilson weight are different equations. This is the only candidate in this file whose proof object must change when the weight changes.
- Verdict. Without (SYM), (BOOT_eps) is the insensitivity of one plaquette to all boundary values of Q, a hypothesis of the kind of (W) (row 691); I do not attack it. With (SYM) it is weaker than (W): the seed needs agreement only among symmetric, reflection-positive states. The published bootstrap bounds (as read in the two digests: loops up to length 24, about 0.1 percent for the plaquette) come from numerical optimisation, are far from the eps that is needed, and do not compare volumes. Under the owner's rule a certificate can enter the chain only if it is small enough to check by hand. I have no reason to think that a certificate of the needed precision is that small. So C-E names a kind of proof object that passes all four tests in the right way, and it gives no proof.

**On lead (e).** It has no statement of its own: its content is the remark that C-A and C-B are inequalities of order one, and Section 4.5 says what a hand proof of one step would need. I did not find a different object that is easier. The honest position after Part 1: in the coupling direction the right object is K_b(s), the logarithmic rate of C-A, and what is needed about it is a growth of at most log b.

## 3. Status block (kept current)

- Written: Sections 0 to 10. The file is complete for this run. The final status block is Section 9 (Section 10 was written after it and is counted in it).
- Proved in this file (not checked): Lemma 4.1, Lemma 4.2, Theorem TR, Remarks CH and LEV, Proposition Delta, Corollary TR1, Theorem CRIT, Identity FL, Proposition BE, Lemma M, Proposition MIX, Lemma DC, Lemma INF, Theorem DOB (the seed for beta < 1/18).
- Failed: the deficit bound (DEF_K), in three ways (Section 4.4); (BE-block), by a counterexample (Section 7).
- Open: (VIR-log) for SU(2); (NOCRIT); (MF) and (S_0); (BOOT_eps); the seed at a coupling of order one.

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

**Remark CH (PROVED, by the same proof).** The proof uses (VIR_K) only at the one time t = t_0 E(s) for each s, on the characteristic curve. So the hypothesis can be weakened to: for every s in [beta_0, beta_1), the inequality holds at t = t_0 E(s). On that curve the thermal sum is at most its value at (t_0, beta_0), which is small in the use below. So what has to be bounded is the rate K at times where the box is already cold.

**Remark LEV (a transparent sufficient condition; PROVED).** Order the levels, E_1(s) <= E_2(s) <= ... . If for all s < s' in the interval and all i >= 1

(LEV_K) E_i(s') >= E_i(s) exp(- integral of K over [s, s']),

then G(t exp(integral of K over [s, s']); B; s') <= G(t; B; s) for every t >= 3, term by term in the sum. So the conclusion of Theorem TR holds with no derivative. (LEV_K) says: no ordered level falls faster than at the logarithmic rate K. (VIR_K) asks this only for the thermal mean. Where the levels are differentiable, (LEV_K) is - dE_i/ds <= K E_i, and - dE_i/ds is the action of one time slab in the vacuum minus its action in the level i (first-order perturbation; interpretation, used in no proof). I call this difference the action deficit of the level.

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

(VIR-log) For the Wilson SU(2) theory and beta_1 > 0 there are beta_0 <= 1/25600 and an even b >= 256 such that (VIR_K) holds on the cube b^3 on [beta_0, beta_1], for the times [ceil(log_2 b), b/2] (by Remark CH: on the characteristic curve only), with integral of K at most log(b/(2 ceil(log_2 b))).

**How the threshold log b separates the cases (GUIDE; two-dimensional Ising model, recalled from Onsager's solution, used in no proof).** On a ring of length b, in the phase with one state the lowest level tends to the mass m(J) > 0 and - d log E_1/dJ stays bounded on compact sets of couplings: K_b is bounded in b. At the critical coupling E_1 is of order 1/b with a derivative of order one: K_b grows like b. In the phase with two states E_1 is the tunnel splitting, of order exp(-tau(J) b), and - d log E_1/dJ = b tau'(J): K_b grows like b at every coupling of that phase. So a growth of K_b below log b holds in the first case and fails in the other two, with room to spare.

I know no weaker statement that gives the seed along the coupling. It is implied by (LEV_K) with a constant K, which is the statement that the lattice beta function, read from every level of the box, is bounded away from zero on [beta_0, beta_1].

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

## 8. Lead (c) without a derivative: the seed as a locality statement for one observable

Theorem D-shape (d) writes the seed as an integral over the coupling of abar_(2a,B) - abar_(a,B). The next lemma shows that this difference is the response of one plaquette to a change of the local rules at a distance of about a/2. It is the place where any mixing input enters the chain.

**Setting.** a >= 3, B a box, n = (a, B), n' = (2a, B), coupling s. Lambda_0 is the set of the links of n' in the first half: the space links with time coordinate 0, ..., a - 1 and the time links from time j to j + 1 for j = 0, ..., a - 1. Reducing the time coordinate modulo a is a bijection from Lambda_0 to the links of n. Let mu' be the Gibbs measure of n' and mu~ the law on the configurations of n that is the image of the marginal of mu' on Lambda_0. Let D be the set of these links of n: the space links at the times 0 and a - 1, and the time links from time a - 1.

**Lemma M (PROVED).** For every link l of n outside D, the conditional law under mu~ of U_l given all other links has the density proportional to exp(s times the sum of x_p over the six plaquettes of n through l) with respect to Haar measure. This is the one-link law of the Gibbs measure mu_n of n.

Proof. Let l' in Lambda_0 be the link that maps to l. If l is a space link at a time j with 1 <= j <= a - 2, its plaquettes in n' are four space plaquettes of the slice j and two time plaquettes of the slabs [j - 1, j] and [j, j + 1]. If l is a time link from j <= a - 2, its six plaquettes lie in the slab [j, j + 1]. In both cases every link of these plaquettes is in Lambda_0, and the bijection maps them to the six plaquettes of n through l, with no wrapping. Under mu' the conditional law of U_(l') given all other links of n' has the density proportional to exp(s sum of x_p over these six plaquettes). It depends on links of Lambda_0 only. The conditional law given the links of Lambda_0 other than l' is the mean of that law over the remaining links, and the law does not depend on them. QED

So mu~ and mu_n are two laws on the same space with the same one-link conditional laws outside D, and D is the cut where the first half of the long torus is closed on itself.

**Proposition MIX (PROVED from Lemma M and Theorem D-shape (a), (d)).** Let j = floor(a/2) and let P be the set of the 3 abs(B) space plaquettes at time j and the 3 abs(B) time plaquettes of the slab [j - 1, j]. Their links have time distance at least floor(a/2) - 1 from D. Suppose that for every s in (0, beta] and every p in P

abs( mu_n(x_p) - mu~(x_p) ) <= eps(a).

Then Phi_B(a; beta) = 2 F(a, B) - F(2a, B) <= 12 a abs(B) beta eps(a), and S(a; B; beta) <= exp(12 a abs(B) beta eps(a)) - 1.

Proof. mu_n and mu' are invariant under time translations, so abar_(a,B) is the mean over p in P of mu_n(1 - x_p), and abar_(2a,B) is the mean over the same plaquettes of mu'(1 - x_p) = mu~(1 - x_p). So abs(abar_(2a,B) - abar_(a,B)) <= eps(a) at every s. Integrate (Theorem D-shape (d)); then Theorem D-shape (a). QED

**What it asks of SU(2).** A bound eps(a) <= C exp(-m_* a/2) for all couplings up to beta: the plaquette at mid-height does not feel the rules at the cut. Test: (ii) for U(1) at weak coupling the response to the cut falls like a power of a (RECALLED: the Casimir effect of the photon), and with eps(a) of order a^(-4) the bound 12 a abs(B) beta eps(a) is of order one at r = 2, in agreement with the failure of the seed; for Z_2 at its transition the two laws can sit in different phases. (iv) On the line of K7 the same. For beta < 1/18 the bound follows from Dobrushin's uniqueness condition by his comparison estimate; this is proved in Section 10 (Theorem DOB). Above the Dobrushin range it is a strong mixing statement for one observable, weaker than (W) of row 691 in that it concerns one observable and one pair of laws, and not known.

## 10. The mechanism of Section 8 carried through where it can be: the seed for beta < 1/18 (Theorem DOB)

(Placed here in the order of writing; Section 9 is the final status block and counts this section.)

This section proves the bound eps(a) of Proposition MIX in the range of Dobrushin's uniqueness condition, with every step written. It is strong coupling, not the middle range. Its use: the chain "mixing input, Lemma M, Proposition MIX, Theorem SH" is closed once, and the proved range of the seed grows from beta < 1/12800 to beta < 1/18.

**Notation.** Lambda is a finite set of links, Omega = SU(2)^Lambda. For a bounded function f on Omega, delta_l(f) is the supremum of abs(f(w) - f(w')) over pairs that agree off the link l, and Delta(f) is the sum over l of delta_l(f). The oscillation of f is at most Delta(f) (change the links one at a time). For two probability laws, d(nu, nu') := the supremum over sets of abs(nu(A) - nu'(A)); then the difference of the integrals of a function h is at most d(nu, nu') times the oscillation of h. A one-link specification gamma is a family of laws gamma_l(. | w) of U_l given the other links. Its influence matrix is C(l, k) := the supremum of d(gamma_l(. | w), gamma_l(. | w')) over pairs w, w' that agree off k, for k not l. alpha := the maximum over l of the sum over k of C(l, k). Two links are neighbours if C(l, k) > 0 or C(k, l) > 0; dist is the graph distance.

**Lemma DC (Dobrushin's comparison estimate on a finite set; PROVED; the argument is Dobrushin's, rebuilt here).** Let alpha < 1. Let mu be a law whose one-link conditional laws are the gamma_l at every link. Let mu~ be a law whose one-link conditional laws are the gamma_l at every link outside a set D. Let f be continuous, let supp f be the set of links with delta_l(f) > 0, and let d be the distance from supp f to D. Then

abs( mu~(f) - mu(f) ) <= Delta(f) alpha^d / (1 - alpha).

Proof. Let (Gamma_l g)(w) be the integral of g(xi, w off l) against gamma_l(d xi | w), and Gamma~_l the same with the one-link conditional law of mu~. Then mu(Gamma_l g) = mu(g) for all l, mu~(Gamma~_l g) = mu~(g) for all l, and Gamma~_l = Gamma_l (mu~-almost surely) for l outside D.
Step 1. delta_l(Gamma_l g) = 0, and for k not l: delta_k(Gamma_l g) <= delta_k(g) + C(l, k) delta_l(g). (For w, w' that differ at k only: Gamma_l g(w) - Gamma_l g(w') is the integral of g(xi, w) - g(xi, w') against gamma_l(. | w), at most delta_k(g), plus the integral of g(xi, w') against gamma_l(. | w) - gamma_l(. | w'), at most C(l, k) times the oscillation of g in xi, which is at most delta_l(g).)
Step 2. Fix an order l_1, ..., l_N of the links and apply the Gamma in this order again and again: f_0 = f, f_i = Gamma_(l_i) f_(i-1), with indices of the links taken cyclically. Keep vectors v_i^(m) >= 0 on Lambda, m >= 0 ("mass of level m at step i"): v_0^(0) = delta(f), v_0^(m) = 0 for m >= 1; at step i with l = l_i, the mass at l is removed in every level, and for k not l, v_i^(m)(k) = v_(i-1)^(m)(k) + C(l, k) v_(i-1)^(m-1)(l). By Step 1 and induction, delta(f_i) <= the sum over m of v_i^(m), entry by entry. Three facts follow from the rule. (a) A removal of the mass x of level m - 1 creates mass of level m of total amount at most alpha x. So the total mass of level m that is ever created is A_m <= alpha^m Delta(f). (b) Mass of level m sits at distance at most m from supp f, because C(l, k) vanishes unless k is a neighbour of l. (c) In one cycle every link is updated once. So every unit of mass present at the start of a cycle is removed in it, and what it leaves at the end of the cycle is at most alpha times it. The total mass after n cycles is at most alpha^n Delta(f).
Step 3. By (c), the oscillation of f_i tends to 0. mu(f_i) = mu(f) for all i. So f_i tends to the constant mu(f) uniformly, and mu~(f_i) tends to mu(f).
Step 4. mu~(f_(i-1)) - mu~(f_i) = mu~(Gamma~_l f_(i-1) - Gamma_l f_(i-1)) with l = l_i. It is 0 for l outside D. For l in D its absolute value is at most delta_l(f_(i-1)), because d of two laws is at most 1; and delta_l(f_(i-1)) is at most the mass at l that step i removes. By (b) this mass has level at least d. By (a) the sum over all steps is at most the sum over m >= d of A_m <= Delta(f) alpha^d/(1 - alpha). Sum over i and use Step 3. QED

**Lemma INF (the influence of one link; PROVED).** On a torus with all sides at least 3, at the coupling s, let gamma_l be the one-link law with density proportional to exp(s times the sum of x_p over the six plaquettes through l). Then C(l, k) <= s if l and k lie in a common plaquette, and C(l, k) = 0 otherwise. Each link has 18 such k. So alpha <= 18 s.

Proof. Two distinct links lie in at most one common plaquette (sides at least 3), and the six plaquettes through l contain 18 other links. Let k be in the plaquette p_0 through l. A change of U_k changes the density of U_l from exp(h)/Z to exp(h + g)/Z', where g(U_l) = s (1/2) tr(U_l A) and A is the difference of two elements of SU(2) (the products of the three other links of p_0 before and after). A = a_0 + i (a . sigma) with a real vector (a_0, a) of length at most 2, and (1/2) tr(U A) takes values in [-abs(A), abs(A)]. So the oscillation of g is at most 4 s. For rho_tau := exp(h + tau g)/Z_tau: d rho_tau/d tau = rho_tau (g - m_tau), with m_tau the mean of g under rho_tau. The mean of abs(g - m_tau) under rho_tau is at most the standard deviation, which is at most half the oscillation, 2 s. So the integral of abs(rho_1 - rho_0) is at most 2 s, and d = (1/2) of that integral is at most s. QED

**Theorem DOB (PROVED from Lemma DC, Lemma INF, Lemma M, Proposition MIX; the gap GIVEN Theorem SH).** Let 0 < beta < 1/18, alpha := 18 beta, a >= 3 an integer, B a box with sides at least 3. Then for every s in (0, beta]:

abs( abar_(2a,B)(s) - abar_(a,B)(s) ) <= 8 alpha^(floor(a/2) - 1)/(1 - alpha), and Phi_B(a; beta) <= 96 a abs(B) beta alpha^(floor(a/2) - 1)/(1 - alpha).

For B = (2a)^3: if 768 a^4 beta alpha^(floor(a/2) - 1)/(1 - alpha) <= 6 x 10^(-4), then S(a; (2a)^3; beta) < 1/1650, every periodic cube at beta has a gap, and m(L^3) >= 0.06/a for every integer L >= 64 a. For every beta < 1/18 such an a exists. Example: beta = 1/36, a = 90.

Proof. Apply Lemma DC on the torus n = (a, B) with gamma the Gibbs specification at s, mu = mu_n, mu~ and D of Lemma M, f = x_p for p in the set P of Proposition MIX. delta_l(x_p) <= 2 for the four links of p and 0 otherwise, so Delta(f) <= 8. Give a space link at time j the position j and a time link from j to j + 1 the position j + 1/2. Two links of a common plaquette have positions that differ by at most 1. The links of the plaquettes of P have positions in [floor(a/2) - 1, floor(a/2)], and the links of D have positions 0, a - 1 and a - 1/2. So d >= floor(a/2) - 1. alpha(s) <= 18 s <= alpha. This gives eps(a) = 8 alpha^(floor(a/2) - 1)/(1 - alpha) in Proposition MIX. For B = (2a)^3, abs(B) = 8 a^3, and exp(6 x 10^(-4)) - 1 < 6.01 x 10^(-4) < 1/1650. The gap: as in the proof of Corollary TR1, from S(a; (2a)^3) <= 1/1650. Existence of a: a^4 alpha^(a/2) tends to 0. Example: alpha = 1/2, 768/36 < 21.34, and the condition is 42.7 a^4 2^(-(floor(a/2) - 1)) <= 6 x 10^(-4); at a = 90: 90^4 = 6.561 x 10^7, 2^(-44) < 5.69 x 10^(-14), and 42.7 x 6.561 x 10^7 x 5.69 x 10^(-14) < 1.6 x 10^(-4). QED

**Remarks.** (1) The range 1/18 is what the crude bound of Lemma INF gives. With the sharper one-link bound of `gap-zf-box-x.md` (its Lemma 2.1 and 2.5.2: threshold about 0.102) the same proof gives beta <= 1/10; I did not port it. (2) The rate is poor: at beta = 1/36 the bound is m >= 6.7 x 10^(-4), where the leading strong-coupling value is 4 log(4/beta), about 20 (GUIDE). The statement is the existence of a uniform gap by this route. (3) Test: Lemma DC and Lemma INF hold for every compact group with a bounded one-plaquette weight (with another constant in Lemma INF). So Theorem DOB is a theorem of the class "small beta", true for U(1) and Z_2 as well, as it must be. Above the Dobrushin range the influence bound alpha < 1 fails for every group, and nothing here replaces it.

## 9. Part 3: status block (final)

**No mass gap at a coupling of order one is proved here. The seed in the middle range is open, and I found no tool for it.**

**Proved here by hand, not checked by another model.**

| Statement | Content | Inputs | Section |
|---|---|---|---|
| Lemma 4.1 | lambda_0, G and dG/dt are continuous in the coupling (t >= 4), from the traces alone | (TM), Lemma A | 4.1 |
| Lemma 4.2 | at integer t the derivative of the thermal sum in beta is 6 t abs(B) (abar_inf - abar_t), outside a countable set | (TM), Lemma A | 4.1 |
| Theorem TR | (VIR_K) on one box carries the thermal sum along t(s) = t_0 exp(integral of K) | Lemma 4.1 | 4.2 |
| Remark LEV | the same from (LEV_K): no ordered level falls faster than at the rate K | none | 4.2 |
| Proposition Delta | g(a; b^3) <= (b/a)^3 Delta(a^4); Delta(a^4) <= 6.1 x 10^(-4) is a seed at r = 4; gapless models of the class have Delta(a^4) > 6.1 x 10^(-4) at every size | Lemma A, (LB), Theorem SH | 4.3 |
| Corollary TR1 | (VIR_K) on one cube b^3 with integral of K <= log(b/(2 ceil(log_2 b))) gives the seed at beta_1 and m >= 0.12/b on cubes of side >= 32 b | Theorem TR, Theorem SH, `gap-seed-sc.md` Theorem 1 (iii) | 4.3 |
| Theorem CRIT | the set of couplings with a seed is open; its first boundary point is a critical coupling: all thermal sums at ratio 4 are >= 1/25, Delta(a^4) > 6.1 x 10^(-4) at every size, the seed size diverges on approach | Lemma 4.1, Proposition Delta, Theorem SH, `gap-seed-sc.md` | 5.1 |
| Identity FL | 1 + S = (1 + S_0)/(1 - U); the seed needs both the zero-flux sum and the twist weight small; the two are independent in the class (one half of the independence RECALLED) | (TM), (TM-c), `gap-seed-shape.md` 4.1 | 6 |
| Proposition BE | the Bakry-Emery tensor of the lattice measure is (1/2 - 3 beta/2) on a link direction at an explicit configuration; negative for beta > 1/3 | none | 7 |
| Lemma M, Proposition MIX | the plaquette shift between the tori of time a and 2a is the response of a plaquette at mid-height to a change of the one-link laws at the cut; a bound eps(a) on it gives Phi_B(a) <= 12 a abs(B) beta eps(a) | Theorem D-shape | 8 |
| Lemma DC, Lemma INF | Dobrushin's comparison estimate on a finite set of links, rebuilt; the influence of one link on another is at most s, so alpha <= 18 s | none | 10 |
| **Theorem DOB** | for beta < 1/18 the plaquette shift is at most 8 (18 beta)^(floor(a/2) - 1)/(1 - 18 beta); the seed S(a; (2a)^3) < 1/1650 holds for large a (a = 90 at beta = 1/36), and with it a gap of every periodic cube. Before: beta < 1/12800 | Lemma DC, Lemma INF, Lemma M, Proposition MIX; the gap GIVEN Theorem SH | 10 |

Theorem SH (row 705) was not yet checked when this file was written (its check is row 707). Every statement above that names it is PROVED GIVEN Theorem SH.

**Failed, and why.**

- (DEF_K), the bound of the action deficit of a level by K times its energy with K independent of the box (Section 4.4), in three ways. Pointwise: the natural inequality gives K = 1/beta, which the published scale values contradict by a factor of about 8 (GUIDE), so the truth is a cancellation. Locality: the constant of a stability theorem depends on the gap, and the resulting bound ends at a finite coupling (the same end as Proposition B of row 677). Convexity: it bounds second derivatives of F and e, not the first derivative of their difference; and the Ising model of the class shows that no property of the class can give it.
- (BE-block): false above beta = 1/3 in the pointwise form (Proposition BE).
- (CAS) and the flux split: not mechanisms. (CAS) restates the seed in steps. The flux split shows that the seed is two independent statements.

**The leads of the row, answered.**

- (a) Doubling map. The weakest statement that gives the seed is the seed after finitely many doublings; an inequality that excludes a fixed point on a compact interval is (CAS), and it needs only theta < 1, a number of order one. In the class a gapless model keeps Delta(a^4) above 6.1 x 10^(-4) at every size (Proposition Delta). No inequality for SU(2) was found.
- (b) Flux sectors. The seed does not reduce to one part (Identity FL and the two models). The flux part is (MF), which is (TUBE') and (VORT) of the earlier rows.
- (c) Derivative form. Yes, as a theorem: Theorem TR and Corollary TR1. The input from SU(2) is (VIR-log): the logarithmic rate K_b of the box b^3 grows more slowly than log b. Without a derivative: Proposition MIX.
- (d) Curvature. No. It covers beta < 1/3 in the pointwise form at every scale.
- Not a lead of the row: C-E, the certificate form. Proposition MIX turns a bound eps on the disagreement of symmetric states at one plaquette into the seed. It is the only form found in which the Wilson weight itself, and not only the group, is in the proof object.
- (e) Finite number of steps. The steps are few. Each step is an inequality of order one between two quantities that are each exponentially small, so a hand proof of a step needs an identity and not two estimates; the identity that the continuum has (the trace anomaly) has no lattice form (Section 4.5).

**The one exact next statement of each attempt.**

- Attempt 1 (coupling direction): (VIR-log) of Section 4.4.
- Attempt 2 (scale direction): (NOCRIT) of Section 5.1: beta*(1/25) is infinite. By Corollary TR1 it follows from (VIR-log).
- Attempt 3 (curvature): none; the statement is false.
- Flux: (TUBE') of row 697, unchanged.

**What the author concludes (the lead decides).**

1. The middle range now has an exact name. In the coupling it is the first critical coupling beta*(1/25) of Theorem CRIT. The mass gap of the periodic cubes at every coupling is (NOCRIT).
2. What is missing can be stated with no small number: an order-one bound on a logarithmic derivative on one large box, (VIR-log). The strong-coupling seed (proved) and Theorem SH supply every small number. This is a change of form, not of difficulty. In plain words (GUIDE numbers from `gap-seed-shape.md` Section 5): the seed at r = 2 says that the relative gap b m(b^3) of one cube is above about 21 (above 14.8 by the rate filter alone). A massless theory keeps b m(b^3) bounded. So the middle range is the range of sides b over which b m(b^3) has to rise from its value in a small box to about 21, and (VIR-log) says that along the coupling the gap of a large box falls no faster than exponentially.
3. K7 is decisive for the method. A statement that is true for the one-plaquette weights with a small positive adjoint term cannot give (NOCRIT), because such a weight has a first-order line near beta_F = 1.5 (RECALLED, not proved by anyone here). So a proof at every coupling must use a property of the Wilson weight that an adjoint term destroys. The only exact such property I can name is that the weight is log-linear in x = (1/2) tr U_p, so that the one-link law is fixed by one vector, the sum of the staples. Its exact form is the set of loop equations of C-E. I know no inequality that uses it and can be proved by hand. Mean-field theory predicts a transition for the Wilson weight itself (RECALLED), so the property must be used with a precision that mean-field arguments do not have.
4. For the scaling form (large beta) the middle range is the same range in physical size, and the effective weight at the scale where the coupling is of order one is a weight of the kind of K7. So the scaling form does not avoid the question.
5. I do not recommend another max run on the middle range before a new tool exists. The item below that is worth a worker's time is the check (item 1). Theorem DOB moves the proved range of the seed from beta < 1/12800 to beta < 1/18; that is still strong coupling, and its value is the template of Section 8, not the range.

**Proof items for the medium workers.**

1. `gap-mid-check` (check; first). Check Sections 4 to 8 and Section 10 line by line. In Section 10: Lemma DC, Step 2 (the bookkeeping of the levels, facts (a) to (c)) and Step 4; Lemma INF (the bound of the distance of two laws by a quarter of the oscillation of the exponent); the distance d in the proof of Theorem DOB; the arithmetic of the example. Read: this file; `gap-crux-restate.md` Section 1 and 3.4; `gap-seed-shape.md` 1.4, 1.5, 2, 4.1; `gap-seed-sc.md` Theorem 1. Points that carry weight: (i) Lemma 4.1 (b): the moment argument and the restriction t >= 4; (ii) Theorem TR: the step from the upper right derivative to monotonicity, and the use of joint continuity of dG/dt; (iii) Corollary TR1: the arithmetic and the use of Theorem SH (ii) for the pair (a, 4a); (iv) Proposition Delta: three uses of Lemma A (a) with sides b >= a >= 3; (v) Theorem CRIT (d), (e); (vi) Identity FL: that the three flips commute and fix the vacuum; the product model; (vii) Proposition BE: the normalisation Ric = 1/2 and the six distinct plaquettes; (viii) Lemma M: which links are excluded, and the conditioning step.
2. `gap-seed-dob-sharp` (proof; small; low priority). Theorem DOB is proved in Section 10 for beta < 1/18 with the crude influence bound of Lemma INF. Port the sharper one-link bound of `gap-zf-box-x.md` (Lemma 2.1 and 2.5.2: 18 neighbours, each of influence at most c(x)/2, with 9 c(x) < 1 up to about 0.102) into Lemma INF, and state Theorem DOB for beta <= 1/10 with an explicit a_D(beta). Consumer: the base of the chain. Value: small; it is still the strong-coupling regime. The part of Section 10 that matters is the template: any bound on the response of one plaquette to the cut, from any source, gives the seed through Lemma M and Proposition MIX.
3. `gap-vir-sc` (proof; hard; only if the lead wants C-A tested). Decide whether (VIR_K) or (LEV_K) can be proved in the strong-coupling range for all cubes, with K(s) of order 1/(s log(1/s)): expand G(t; b^3; s) in polymers that wind around the time direction and compare s dG/ds with -t dG/dt term by term. If this fails where everything converges, C-A is not a usable route. Read: `gap-seed-sc.md` Sections 2 and 3; `gap-sc-box.md`.
4. `gap-vir-guide` (GUIDE; small run under the numeric lock). For the two-dimensional Ising model (in the class; Corollary S2), from exact transfer matrices of rings of length b up to 12: K_b(J) := the maximum over the excited levels below a cut of - d log E_i/dJ. Write pass and fail first. Prediction: bounded in b for J below the critical value, growth like a power of b at the critical value. It can show whether the threshold "log b" of Corollary TR1 separates the two cases at sizes that can be reached. It can show no proof step.

**Not done.** No numeric job was run. No paper was read; every statement about U(1), Z_2, the mixed action, the small-volume expansion, mean-field theory and published masses is RECALLED or GUIDE and is used in no proof. The launch text allowed fetching public sources; the row forbids the network for this item, and I followed the row. The body of `library/gap-transfer.md` was not read: Lemma 4.1 uses the traces only, and the sentence on first-order perturbation in Remark LEV is an interpretation. The bound K <= 12 abs(B)/m of Section 4.4 is not proved. Remark Y is a sketch. Of `library/gap-zf-box-x.md` only the lines found by a search for "Dobrushin" and "Theorem A" were read; Section 10 does not use that file. The equivalence of the two forms of (SD_s) in C-E is not proved. Budget used at the end of the run: about 11 of the cap of 25. Nothing was committed or pushed; the only file written is this one.
