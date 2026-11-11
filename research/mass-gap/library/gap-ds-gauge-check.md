lead: anthropic/claude-opus-5-5/high mac-mini-worker
lease_until: 2026-11-11T16:38Z

# gap-ds-gauge-check (FINISH row 693): check of `library/gap-ds-gauge.md` (row 691)

Provenance: Claude Opus 5.5, high effort, Mac mini worker 2, at commit dcb15d3d2. One reading by one other model than the author (Claude Fable 5.2 medium). Not an audit. Written section by section.

Duplicate check: `library/open-core.md` has no entry for Theorem W, (W) or (DS-tw). In `FINISH.md` this check is row 693 only. This item proves no new lemma. Repo search: the checked file is the only text in this folder on (W). The Sussman-Alpoge index (`library/sa-index/`) has no hit for "Dobrushin" (the author's search, line 13 of the checked file; not redone). Nothing from their account bears on this check. Read in full: `library/gap-ds-gauge.md` (218 lines). Read in part: `library/gap-ac-lat.md` lines 27 (flip lemma) and 113 (Lemma C). No numeric run.

Notation is that of the checked file. "Line n" means line n of `library/gap-ds-gauge.md` at dcb15d3d2.

## 1. Theorem W (A), Section 3.3 (lines 113-139)

**Verdict: HOLDS.** There is one degenerate case. On a torus, Lambda can be the set of all links. Then B_Lambda is empty and w is not finite. But then gamma_Lambda does not depend on tau, and the claim TV = 0 is trivial. Add this sentence. I checked the steps in the order of the row.

- **The weight w (line 115).** D(l) = d(l, B_Lambda) is defined on Lambda union its boundary. d is the sup-norm distance of the lower ends; on a torus it is the torus sup-norm distance. Both are pseudo-metrics, so |D(l) - D(l')| <= d(l, l'). On B_Lambda, D = 0 and w = 1. Correct.
- **Inequality (1) (line 117).** A link of V_R + a has its lower end in a + {0, ..., R}^4. A boundary link shares a plaquette with a link of the cube. The four lower ends of a plaquette are within sup distance 1 of each other. So the boundary links have lower ends in a + {-1, ..., R+1}^4, and d <= R + 2 = r on the cube with its boundary. Then w_l <= e^{eps r} w_{l'}. With eps = ln(1/delta)/(2r), e^theta = delta^{-1/2} and e^theta delta = sqrt(delta). Correct. The cube with its boundary lies in Lambda union its boundary when the cube lies in Lambda, so w is defined there.
- **Near-minimal coupling (lines 119-123).** Phi(P) >= 0, so Phi_* is finite. The product coupling exists. A minimizer would also exist (Phi is lower semicontinuous in the weak topology, because {sigma_l != sigma'_l} is open). The near-minimal choice avoids that argument and costs only eta_1. T_a P is a coupling of the same two measures (Lemma 3), so Phi(T_a P) >= Phi_* >= Phi(P) - eta_1. The bound sum_{l in V} w_l p^a_l <= (max_V w)(sum_z k_z p_{z+a} + eta_0) uses Lemma 3. Then (max_V w) k_z p_{z+a} <= e^theta k_z w_{z+a} p_{z+a} by (1), and (max_V w) eta_0 <= w_max eta_0. The displayed inequality is correct.
- **Sum over translates, (2) (line 125).** sum over a in Acal of sum_{l in V_R + a} w_l p_l = sum_{l in Lambda} n_l w_l p_l. sum over a of sum_z k_z w_{z+a} p_{z+a} = sum_y K_y w_y p_y, with y = z + a running over Lambda union its boundary. Correct.
- **Fact 1, K_y <= delta N_R (line 128).** For fixed y, a -> z = y - a is one to one, and z has the direction of y. So K_y is at most the sum of k_z over the boundary links z of V_R with that direction. (W) bounds this sum by delta N_R. Correct. On a torus, distinct a give distinct z because the lower ends of V_R union its boundary lie in {-1, ..., R+1}^4, R + 3 values per coordinate, and n_i >= R + 4 > R + 3.
- **Fact 2, the support of K_y (line 129).** If K_y > 0, y is in the boundary of a cube contained in Lambda, so y is in Lambda union its boundary. That set equals Lambda° union B_Lambda (disjoint union). The fact is true and trivial.
- **Fact 3, n_l (line 130).** The a with l in V_R + a correspond one to one to the links l - a of V_R with the direction of l. There are N_R of them (on a torus, distinct because n_i >= R + 1). For l in Lambda°, each such cube lies in Lambda, so a is in Acal and n_l = N_R. Correct.
- **Inequality (3) (lines 133-135).** On the left of (2), drop the links of Lambda minus Lambda° (the terms are not negative) and use n_l = N_R on Lambda°. On the right, use Fact 1 and Fact 2, and use w = 1, p <= 1 on B_Lambda (for y in the boundary of Lambda, p_y = 1{tau_y != tau'_y} <= 1). This gives N_R X <= sqrt(delta) N_R (X + |B_Lambda|) + N (eta_0 w_max + eta_1), with X = sum over Lambda° of w_l p_l. X is finite. Rearranging gives (3). Correct.
- **The last step (line 137).** For S in Lambda°: TV <= P(sigma != sigma' on S) <= sum_{l in S} p_l <= exp(-eps d(S, B_Lambda)) X, because w_l >= exp(eps d(S, B_Lambda)) for l in S. The left side does not depend on P, eta_0, eta_1. Let them tend to 0. Constant sqrt(delta)/(1 - sqrt(delta)): correct. If Lambda° is not empty, Acal is not empty, because a link of Lambda° lies in at least one cube and every such cube lies in Lambda.

**Where translation is used.** The specification itself need not be translation invariant. The proof uses three things. (a) The family of cubes is the family of all translates V_R + a. (b) (W) gives one family k_z that holds at every translate a (a uniformity in a, which is weaker than invariance). (c) The two counting facts use translation: n_l = N_R on Lambda° (all translates that contain l are counted), and a -> y - a is one to one. Nothing else uses translation.

**A cube that touches the boundary of Lambda.** This case is handled. Acal contains every cube that lies in Lambda, including cubes whose boundary meets the boundary of Lambda. For such a cube, a boundary link z + a outside Lambda enters with p = 1{tau != tau'} and w = 1. Lemma 3 handles it, because omega = tau there (last line of the proof of Lemma 3). Cubes not contained in Lambda are never resampled. Their links in Lambda are in Lambda minus Lambda°, which is in B_Lambda, and there the bound uses only p <= 1.

## 2. Lemmas 1, 2, 3 (lines 101-111)

**Lemma 3 (resampling keeps both marginals): HOLDS.** Draw (sigma, sigma') from P. Given sigma, the first coordinate eta of K(omega, omega'; .) has the law gamma_V(. | omega). This law depends only on omega, so it does not depend on sigma'. So the law of (sigma on Lambda minus V, eta) is the law of sigma on Lambda minus V, followed by gamma_V(. | sigma on Lambda minus V, tau). This is gamma_Lambda(. | tau). Reason: for fixed sigma on Lambda minus V, the density of gamma_Lambda(. | tau) in the V-part is proportional to exp(-sum over p meeting V of phi_p). The terms of the plaquettes that meet Lambda but not V are constant. Every plaquette that meets V meets Lambda. So this conditional density is the density of gamma_V(. | omega). The second marginal is the same. p^a_l = p_l off V is clear. E rho_V(eta, eta') <= E c_a(omega, omega') + eta_0 = sum_z k_z P(omega_{z+a} != omega'_{z+a}) + eta_0. For z + a in Lambda minus V this probability is p_{z+a}. For z + a outside Lambda it is 1{tau != tau'} = p_{z+a}. Correct.

**Lemma 2 (measurable family): HOLDS.**
- Uniform continuity. f_omega(eta) = exp(-H(eta, omega))/Z(omega). H is a finite sum of continuous phi_p, and Z is continuous and positive. So f is jointly continuous on the compact set Theta x G^V. Hence it is uniformly continuous. So there is kappa > 0 with sup_eta |f_omega - f_omega~| <= eta_0/|V| when dist(omega, omega~) < kappa. lambda^V is a probability measure, so TV <= eta_0/(2|V|). Correct.
- (i) The maximal coupling. With t = int (f_omega - f_omega~)_+ = int (f_omega~ - f_omega)_+ (both densities integrate to 1), the new point has the law min(f, f~) lambda + (int (f - min(f, f~)) lambda) (f~ - f)_+ lambda / t = min(f, f~) lambda + (f~ - f)_+ lambda = f~ lambda. P(new != old) <= int (f - min(f, f~)) = t = TV. f > 0, so min/f is defined. Correct. Measurability: f and t are continuous in (omega, omega~, eta), and the kernel is defined piecewise on the Borel sets {t = 0} and {t > 0}. Correct.
- (ii) The cells. The pairs with a given set of disagreement form a Borel set. There are finitely many such sets. Theta x Theta is compact, so a finite cover by sets of diameter below kappa in each coordinate cuts each such set into finitely many Borel cells. c_a depends only on the set of disagreement, so it is constant on a cell. The chosen pair (omega_i, omega'_i) lies in the cell, so c_a(omega_i, omega'_i) = c_i. Lemma 1 gives K_i. Correct.
- (iii) The chain and eta_0. dist(omega, omega_i) < kappa and dist(omega'_i, omega') < kappa, because both pairs are in the same cell. So E rho_V <= |V| (eta_0/(2|V|)) + c_i + |V| (eta_0/(2|V|)) = c_i + eta_0. Correct.
- What is imported: the existence of a disintegration (a regular conditional probability) of K_i with respect to its first marginal on the compact metric space G^V x G^V. The file says this (line 152). It is standard measure theory, but it is not rebuilt in `library/`. Under the rule of GOAL.md ("any literature lemma the chain needs is rebuilt"), this is one named imported fact. It is not a gap in the argument.

**Lemma 1 (several changed links): HOLDS.** omega^m equals omega' on the boundary of V, so gamma_V(. | omega^m) = gamma_V(. | omega'). omega^{j-1} and omega^j differ exactly at y_j. Every configuration on the boundary is an allowed boundary value, because the weight is positive. So (W) applies. By induction eta^{j-1} has the law mu_{j-1}, so (eta^{j-1}, eta^j) has the law K_j. rho_V is the Hamming metric, so the triangle inequality holds. The bound is sum_j k_{y_j - a} = c_a. Correct. This uses the same disintegration fact as Lemma 2.

## 3. Theorem W (B), (C), (D') (lines 141-147)

**(B) one Gibbs state on Z^4: HOLDS.** One step is written short. Line 143 says that a weak limit point of gamma_{Lambda_N}(. | tau) is a Gibbs state "because gamma_Lambda maps continuous functions to continuous functions". The full step: for N large, Lambda is in Lambda_N, so mu_N(gamma_Lambda(fg)) = mu_N(fg) for continuous f and continuous g that do not depend on Lambda. gamma_Lambda(fg) = g gamma_Lambda(f) is continuous, so the identity passes to the limit. A monotone class argument then gives the DLR equations. Only existence uses this, and existence is classical; the uniqueness part does not use it. The uniqueness argument: |mu(f) - nu(f)| <= osc(f) sup TV on S. A link with both ends in {-N + R, ..., N - R}^4 is in Lambda_N°: a cube that contains it has its sites within R of those ends, so in {-N, ..., N}^4. The links of B_{Lambda_N} have lower ends at sup norm at least N - R - 1, so d(S, B_{Lambda_N}) >= N - R - 1 - c(S). |B_{Lambda_N}| <= 4 (2N + 3)^4. (A) gives a bound polynomial in N times exp(-eps N), which tends to 0. Continuous local functions determine a measure on the compact product. Correct.

**(C) covariance: HOLDS AFTER CORRECTION.** The proof covers only D >= R + 1. Line 145 applies (A) with S = X. (A) needs X in Lambda°. A link of X has d(., X) = 0, and the proof shows that d(l, X) <= D - 1 - R gives l in Lambda°. So X is in Lambda° when D >= R + 1. For D <= R, X need not be in Lambda°, and (A) does not apply. (For D = 0, X is not even in Lambda.) For those D the claim must come from the trivial bound |Cov(F, G)| <= osc(F) sup|G| (write Cov = mu((F - c)(G - mu(G))) with c the midpoint of the range of F). The right side of (C) is at least this when D = 0. For 1 <= D <= R it is at least (1 - sqrt(delta))^{-1} 4 |X| 3^4 exp(-eps R) osc(F) sup|G|. Here exp(-eps R) = delta^{R/(2(R+2))} >= sqrt(delta). So it is at least osc(F) sup|G| when 324 sqrt(delta) >= 1, that is, when delta >= 324^{-2}. For smaller delta the statement as written is not proved for 1 <= D <= R (it may be true; I did not decide this).

*Corrected statement (C').* Under (W) at (R, delta), delta < 1: |mu(FG) - mu(F) mu(G)| <= (sqrt(delta)(1 - sqrt(delta)))^{-1} sup|G| osc(F) 4 |X| (2D + 1)^4 exp(-eps D) for all D >= 0. The written statement (C) holds as it stands for D >= R + 1, and for every D when delta >= 324^{-2}.

*Proof.* For D >= R + 1, the proof of line 145 gives the written (C), which is stronger. For D <= R the right side of (C') is at least 4 exp(-eps R)/sqrt(delta) osc(F) sup|G| >= 4 osc(F) sup|G|, because exp(-eps R) >= sqrt(delta). The trivial bound finishes. QED

*Effect.* None on the stated uses. For delta_4 = 1/4 (line 95) the written (C) holds for all D, because 1/4 >= 324^{-2}. Proposition B uses only large D.

The rest of the proof of (C): HOLDS. Lambda = {l : d(l, X) <= D - 1} does not meet Y, because every link of Y has d(., X) >= D. The identity mu(FG) - mu(F) mu(G) = mu(G (gamma_Lambda F - mu(gamma_Lambda F))) and the bound by sup|G| osc(F) sup TV are correct. Links of Lambda minus Lambda° have d(., X) >= D - R (integer distances), and links of the boundary of Lambda have d(., X) >= D. So d(X, B_Lambda) >= D - R. The last factor exp(eps R) <= exp(eps r) = delta^{-1/2} gives the constant (1 - sqrt(delta))^{-1}. Correct.

**The size of B_Lambda: right.** Links of Lambda have lower ends within D - 1 of a lower end of a link of X. Links of the boundary of Lambda share a plaquette with a link of Lambda, so their lower ends are within D. There are at most |X| such lower ends, at most (2D + 1)^4 sites within sup distance D of each (on a torus the ball is not larger), and 4 links per site. So |B_Lambda| <= |Lambda union its boundary| <= 4 |X| (2D + 1)^4.

**The torus; may Lambda wrap: yes.** The proof of (A) uses only three facts about each cube: the cube with its boundary is an embedded copy of V_R union its boundary in Z^4, the counting map a -> y - a is one to one, and d <= R + 2 on it. All three hold when n_i >= R + 3, so n_i >= R + 4 is enough. In detail: the lower ends lie in a + {-1, ..., R+1}^4, R + 3 values per coordinate, so the projection from Z^4 is one to one there. A plaquette that meets the projected cube lifts to a plaquette that meets V_R + a. So the boundary of the projected cube is the projection of the boundary. Lambda itself may wrap, and Lambda°, B_Lambda and D are defined in the torus. The torus measure satisfies the DLR equation by the density computation of Lemma 3. Constants do not depend on n_i. Correct.

**(D') flips: HOLDS**, for the use that is made of Lemma C. The hypothesis of (D') is phi_p(phi_{L_a} sigma) = beta (1 - (1/2) tr sigma(dp)) for each p that meets V_R + a. phi_L is an involution. So phi_p(sigma) = W_p(phi_L sigma), with W_p Wilson's plaquette term. Hence gamma^{act}_V(. | tau) is the image under phi_L of gamma^W_V(. | phi_L tau). This uses that Haar measure of SU(2) is invariant under U -> -U (left multiplication by -1). Boundary values that differ only at z + a stay so after phi_L. The image of a Wilson coupling under phi_L x phi_L is a coupling for the action with the same rho_V. Wilson's (W) on Z^4 at translate a is transferred to the torus cube because the torus cube with its boundary and its plaquettes is a copy of the one in Z^4 (n_i >= R + 3 suffices). Correct.

Lemma C of `library/gap-ac-lat.md` (line 113 there) gives this hypothesis for the twisted action. I checked the step it needs: by the flip lemma (line 27 there), flipping the links of L multiplies U_p by (-1)^{|L intersect p|}, because -1 is central. So the sign of tr U_p changes exactly on d*L, termwise for each plaquette. If d*L agrees with P_{c_0} on the plaquettes that meet Q, then on those plaquettes the twisted term at phi_L sigma is Wilson's term at sigma. This is exactly the hypothesis of (D'), plaquette by plaquette. I did not re-check that the set L chosen in the proof of Lemma C has this d*L. That is row 678's geometry, and it is still not checked by another model (line 203 of the checked file says so). So (D') for the twisted actions is an implication from Lemma C.

**Where the group is used.** Only in (D'): -1 is in G, Haar measure is invariant under multiplication by -1, and -1 is central (for the flip lemma). Section 5 of the checked file (lines 174-176) says the same. I found no other use of SU(2) in Sections 3.2-3.4: Lemma 2 uses positivity and continuity of the density, not the group. For a finite fibre the continuity is trivial. So the proof of (A), (B), (C) holds word for word for U(1) and Z_2, as the row asks.

## 4. Proposition H, Steps 1 to 6 (lines 42-69)

**Verdict: HOLDS** (all three parts).

**Range one: yes.** gamma_Lambda(. | x) is uniform on {z in X : z = x outside Lambda}. The constraint on the Lambda-part is s(dp) = 1 for the plaquettes p in F that meet Lambda. So the law depends on x only through the links that share a plaquette with Lambda. It is the product of the plaquette weights 1{s(dp) = 1} (p in F) times counting measure. The specification is consistent: it is uniform on a coset of Delta_Lambda, and for V in Lambda, Delta_V is a subgroup of Delta_Lambda. {z in X : z = x outside Lambda} = x Delta_Lambda holds because X is a group and every element has order 2.

**Step 1: correct.** Take o to be the corner with the smallest coordinates, so the monotone path stays in B. The path to x + e_i and the path to x followed by the step e_i differ by moving one step e_i past the steps e_j, j > i. Each elementary move crosses one plaquette in the (i, j) plane with its four sites in B (B is a box). Each changes the product by s(dp) = 1. So g_{x+e_i} = g_x s_(x, x+e_i).

**Step 2: correct.** B_1 intersect B_2 is a box, so it is connected. g_1 g_2 is constant on it. Every link of L(B_1 union B_2) lies in L(B_1) or L(B_2): if one end is in B_1 intersect B_2, the other end is in B_1 or B_2; if one end is in B_1 minus B_2, the other end cannot be in B_2 minus B_1, by hypothesis.

**Step 3: correct.** |I_i| = R/2 + 1 <= P. [0, P) has P points, so I_i minus J_i is one interval or empty (two pieces would need at least P + 2 points). S' minus T = {x in S' : x_1 not in J_1 or x_2 not in J_2} = B_1 union B_2. If both are non-empty, their intersection is non-empty. Points of B_1 minus B_2 and of B_2 minus B_1 differ in coordinates 1 and 2, so no link joins them. A plaquette with four sites in B_1 has x_1 outside [0, P) at each site, so no site in T, so it is in F. If both boxes are empty (S' inside T), g is the empty function and Step 4 still works.

**Step 4: correct; y is in Delta_V.** Check of y. (a) y is in X: a plaquette of F has its four sites outside T, so all four links have both ends outside T, and y = g_u g_v on each; the product around the plaquette is 1. (b) y = x on V': links of V' with both ends outside T have both ends in S' minus T, and there y = g_u g_v = x; links of V' that touch T have y = x by definition. (c) y = 1 outside V: y can differ from 1 only on links of V' or on links with an end in S' minus T, because g = 1 off S' minus T. Each such link has both ends within distance 1 of S'. S' has sup distance R/4 >= 1 from the complement of the site box of V (R >= 4), so these links lie in V. The reduction of (1) to "for every x there is y in Delta_V with y = x on V'" is right: then every coset x|_{V'} (Delta_V|_{V'}) equals the subgroup Delta_V|_{V'}, and the uniform law on it does not depend on x.

**Step 5: correct; X_- is not empty.** The sites of c_0 have x_1 in {-1, P} or x_2 in {-1, P}, so they are outside T. Check of s: a (2, j)-plaquette, j = 3, 4, has two links of direction 2 with the same (x_1, x_2), so both are flipped or neither. A (1, 2)-plaquette with base y has the direction-2 links at y and y + e_1. Both are flipped if y_2 = 0 and y_1 >= P. Exactly one is flipped only if y_2 = 0 and y_1 = P - 1. That plaquette contains the site (P - 1, 0, y_3, y_4), which is in T, so it is not in F. Plaquettes without direction 2 contain no flipped link. So s is in X. The direction-2 links of c_0 have x_1 in {-1, P} and x_2 in {-1, ..., P - 1}. Exactly one is flipped, at (P, 0, 0, 0). So h(s) = -1. The band argument: the plaquettes between c_k and c_{k+1} lie in the (1, 3) and (2, 3) planes over the sites of c_0, so they are in F. Their product is h(c_k) h(c_{k+1}), because each link of direction 3 appears in two of them. So h is the same on all c_k, and a finitely supported y has h(y) = 1.

**Step 6: correct; m_+ and m_- are Gibbs states.** X_+ is a closed subgroup of a compact abelian group, so it has a Haar measure. X_- = s_- X_+, so m_- lives on X_- and the supports are disjoint. m_+ is invariant under X_+, which contains Delta_Lambda. For m_-: m_-(f( . y)) = m_+(f(s_- . y)) = m_+(f(s_- y .)) = m_+(f(s_- .)) for y in Delta_Lambda, by commutativity and the invariance of m_+. The DLR identity m(f^ g) = m(fg) for g measurable outside Lambda follows from g(xy) = g(x) and the invariance. Both measures give mass 1 to X. Part (3): c_0 has 4(P + 1) links. If Lambda contains them, gamma_Lambda(. | x) lives on x Delta_Lambda, inside {h = h(x)}. For x in X_+ and x' in X_-, h differs, and h is a function of the links of c_0. So the two laws on those links have disjoint supports. Correct.

**What it lacks against a translation-invariant positive specification.** (a) It is not positive: the weight 1{s(dp) = 1} vanishes, the specification is defined only for admissible boundary values x in X, and the plaquette term is not a finite continuous phi_p. So it is outside Section 2's class, which Lemma 2 needs. (b) It is not translation invariant in directions 1 and 2, and not invariant under the lattice rotations that move directions 1, 2 to 3, 4. It is invariant under translations in directions 3 and 4. (c) The plaquette weight is not one function for all plaquettes (it is the constraint on F and 1 off F). (d) It fails (W) at every scale. This must be so: otherwise Theorem W (B) would give one Gibbs state. The file states (a) and (b) (line 67). So the example refutes only a proof that uses range one, a compact fibre and (D), and nothing more. It says nothing about Wilson's weight.

The remark that "the same construction works in dimension two (a finite hole) and three" (line 67) and the remark for every compact group (line 178, "not written out") are not proved. No proof uses them.

## 5. Corollary 3.6, Proposition B, Proposition S, and the constants of line 95

**Line 95 (delta_4 = 1/4): HOLDS.** eps = ln 4/(2(R + 2)) = ln 2/(R + 2). ln 2/(R + 2) >= 0.46/R is equivalent to 0.233 R >= 0.92, true for R >= 4. (1 - 1/2)^{-1} times 4 = 8. For (2D + 1)^4 exp(-eps D/2) <= (16/eps)^4: put f(D) = (2D + 1) exp(-eps D/8). Its maximum over D >= 0 is at 2D + 1 = 16/eps, with value (16/eps) exp(-1 + eps/16) <= 16/eps for eps <= 1. So f^4 <= (16/eps)^4. Then exp(-eps D/2) = 2^{-D/(2(R+2))} <= exp(-0.23 D/R) because ln 2/(2(R + 2)) >= 0.23/R iff 0.1166 R >= 0.46, true for R >= 4. C(F, G) = 8 sup|G| osc(F) |X| (16 (R + 2)/ln 2)^4. Correct. Note: C depends on R (polynomially). It does not depend on the torus, as the row asks. With delta = 1/4 the case D <= R of Section 3 above is covered, so (C) holds as written.

**Corollary 3.6: HOLDS AFTER a one-word correction.** Line 159 says "a link with both ends at site distance at least R from the complement of the site box is in Lambda°". With the sup-norm site distance to the complement this is off by one: take x with x_j = R - 1; its distance to the site -1 is R, but the cube a + {0, ..., R}^4 with a_j = -1 contains x and leaves the box. The right condition is distance at least R + 1, equivalently both ends in {R, ..., R' - R}^4. With it, the links of Lambda minus Lambda° have lower ends with a coordinate <= R - 1 or >= R' - R, and the links of the boundary of Lambda are farther out. S has lower-end coordinates in [R'/4, 3R'/4]. So d(S, B_Lambda) >= R'/4 - R, which is at least the R'/4 - R - 1 that the file uses. So the inequality used holds and the conclusion is unchanged. |B_Lambda| <= 4 (R' + 3)^4: the lower ends lie in {-1, ..., R' + 1}^4. Correct. The condition holds for R' >= C R ln R: one needs eps (R'/4 - R - 1) >= ln(4 (R' + 3)^4 sqrt(delta)/((1 - sqrt(delta)) delta')), and 1/eps = 2(R + 2)/ln(1/delta), so R' of order R ln R' suffices, that is R' of order R ln R, with C depending on delta and delta'. Correct. The last sentence (with hard constraints (D) does not give (W)) is right: Proposition H has (D) at (R, 0) and fails the conclusion (B) of Theorem W, so (W) fails there at every scale.

**Proposition B: HOLDS.** With D = d(X, Y + x) >= |x| - c(X, Y), Theorem W (C) gives |Cov(F, G_x)| <= const (2D + 1)^4 exp(-eps D). For any m' < eps this is at most C'(F, G) exp(-m' |x|). So m >= eps. Only large |x| matters, so the correction of (C) for D <= R does not touch it. xi = 1/m <= 2(R + 2)/ln(1/delta), which is R + 2 >= (1/2) ln(1/delta) xi. m_gi >= m because the supremum for m_gi is over fewer pairs F, G. Correct. The consequence with Lemma 6' of `library/gap-transport-check.md` is labelled as given that lemma, and I did not check that lemma. Cosmetic: the letter m is used for the rate in Proposition B and for a different rate in Proposition S.

**Proposition S: HOLDS.** The constant 384 checked by hand.
- k_z := sum over l in V of C_0 exp(-m d(l, z)). Then E rho_V = sum_l P(sigma_l != sigma'_l) <= k_z. Four links per lower end gives k_z <= 4 C_0 A(m).
- The boundary links of direction i have lower ends in {-1, ..., R + 1}^4 and are not in V_R. The direction-i links of V_R (N_R of them) also have lower ends there. So their number is at most (R + 3)^4 - R (R + 1)^3 <= (R + 3)^4 - R^4.
- (R + 3)^4 - R^4 = 3 ((R + 3)^3 + (R + 3)^2 R + (R + 3) R^2 + R^3) <= 12 (R + 3)^3.
- So the sum per direction is at most 48 C_0 A(m) (R + 3)^3. R + 3 <= 2 (R + 1) for R >= 1, so (R + 3)^3 <= 8 (R + 1)^3. That gives 384 C_0 A(m) (R + 1)^3 = (384 C_0 A(m)/R) N_R, which is at most delta N_R when R >= 384 C_0 A(m)/delta. Correct.
- The hypothesis is uniform over all cubes of side R (all translates) and all boundary values, so the k_z do not depend on a. This is what (W) needs.

## 6. The statements labelled heuristic

Two passages are labelled heuristic: Section 2.3 (line 73) and the last paragraph of Section 6 (line 189). I did not try to prove them.

- **Section 2.3.** It is used in no proof. It feeds only (i) the comment that the line "Z_2 at large b: true, R of order one" of `library/gap-skeleton-max.md` is doubtful (line 214), which is a recommendation to the lead, and (ii) the kill test proposed for (D-to-W) (line 217). Both are labelled.
- **End of Section 6.** It is used in no proof. It appears as a conditional sentence ("A converse cannot be proved without using the group, if the following is true"). Nothing in the status block rests on it.
- Also unproved and not used in a proof: the three forms of Section 2.1 (an informal account of why the block argument stops; Proposition H is the proof that the gap is real), the paragraph "Class of F, G" in 3.1 (gauge invariance of every Gibbs state; correct as a sketch, and nothing depends on it), and the remarks on dimension 2 and 3 and on every compact group (Section 4 above).

The status block (line 205) lists the heuristics correctly.

## 7. Theorem W (A) re-derived by my own route (marked: re-derivation by the checker)

**Route.** Iterate the averaged resampling map from the product coupling, and take a Cesàro mean. This replaces the near-minimal coupling of line 119. It needs no infimum and builds the coupling explicitly. It shares with the file Lemma 3, inequality (1) and the three counting facts. I checked those separately in Sections 1 and 2, and I derived the counting facts myself there. So this is a second derivation of the step from the per-cube inequality to (3). It is not an independent check of Lemma 3 or of the counting.

**Statement.** As in (A): under (W) at (R, delta), delta < 1, for finite Lambda, boundary values tau, tau', and S in Lambda°, TV(laws on S) <= (sqrt(delta)/(1 - sqrt(delta))) |B_Lambda| exp(-eps d(S, B_Lambda)).

**Proof.** If B_Lambda is empty (only possible on a torus with Lambda all links), gamma_Lambda does not depend on tau, and TV = 0. Otherwise define w, theta, Acal, N as in the file. For a coupling P of gamma_Lambda(. | tau) and gamma_Lambda(. | tau') put X(P) = sum over Lambda° of w_l p_l and Phi(P) = sum over Lambda of w_l p_l >= X(P) >= 0. Fix eta_0 > 0 and let T_a be the map of Lemma 3.

Step 1 (one cube). For a in Acal and V = V_R + a, Lemma 3 and (1) give
Phi(T_a P) <= Phi(P) - sum_{l in V} w_l p_l + e^theta sum_z k_z w_{z+a} p_{z+a} + eta_0 w_max.

Step 2 (average). Put U P = (1/N) sum over a in Acal of T_a P. A mixture of couplings of the same two measures is a coupling of them, and its disagreement probabilities are the averages. Phi is linear in the vector p. So, averaging Step 1 and summing over a as in (2),
Phi(U P) <= Phi(P) - (1/N) (sum_l n_l w_l p_l - e^theta sum_y K_y w_y p_y) + eta_0 w_max.
The counting facts give sum_l n_l w_l p_l >= N_R X(P) and e^theta sum_y K_y w_y p_y <= sqrt(delta) N_R (X(P) + |B_Lambda|). Hence
Phi(U P) <= Phi(P) - (N_R/N) ((1 - sqrt(delta)) X(P) - sqrt(delta) |B_Lambda|) + eta_0 w_max.

Step 3 (iterate). Let P_0 be the product coupling and P_{t+1} = U P_t. Sum Step 2 over t = 0, ..., T - 1 and use Phi(P_T) >= 0:
(N_R/N) (1 - sqrt(delta)) sum_{t < T} X(P_t) <= Phi(P_0) + T ((N_R/N) sqrt(delta) |B_Lambda| + eta_0 w_max).
Let Pbar = (1/T) sum_{t < T} P_t. It is a coupling, and X(Pbar) is the mean of the X(P_t). So
X(Pbar) <= (sqrt(delta)/(1 - sqrt(delta))) |B_Lambda| + (N/(N_R (1 - sqrt(delta)))) (Phi(P_0)/T + eta_0 w_max).
Phi(P_0) <= |Lambda| w_max is finite.

Step 4 (conclude). TV on S <= sum_{l in S} p_l(Pbar) <= exp(-eps d(S, B_Lambda)) X(Pbar). The left side does not depend on T or eta_0. Let T tend to infinity, then eta_0 to 0. QED

The constant and the rate agree with the file. The two derivations agree.

## 8. Is (W) the condition of Dobrushin and Shlosman (1985)?

**Not read.** The primary text is R. L. Dobrushin and S. B. Shlosman, "Constructive criterion for the uniqueness of Gibbs field", in J. Fritz, A. Jaffe, D. Szász (eds.), Statistical Physics and Dynamical Systems, Progress in Physics 10, Birkhäuser, 1985, pp. 347-370, DOI 10.1007/978-1-4899-6653-7_20 (metadata from the Crossref API, fetched 2026-11-11). The Springer link returned a bot check ("Client Challenge"), so I stopped there, by the literature rule of `FINISH.md`. It is not in `~/ym4d-papers` (that folder holds Balaban's papers only). I do not reconstruct their statement from memory. So I cannot say whether (W) is their condition. Theorem W stands as a rebuild in this repository, with its own proof, checked here. It is not claimed as new, as the checked file says (line 15).

## 9. Table of verdicts

| Statement (line in `library/gap-ds-gauge.md`) | Verdict | Note |
|---|---|---|
| Theorem W (A), weak mixing (90, 113-137) | HOLDS | Add the trivial case B_Lambda empty (torus, Lambda all links). Re-derived by my own route, Section 7. |
| Lemma 1, gluing (101-102) | HOLDS | Uses the existence of a disintegration on compact metric spaces (imported, named). |
| Lemma 2, measurable couplings (104-108) | HOLDS | Explicit maximal coupling and cells correct; error eta_0 correct. Same imported fact. |
| Lemma 3, resampling step (110-111) | HOLDS | Both marginals kept; the bound on the sum over V is correct. |
| Theorem W (B), one Gibbs state on Z^4 (91, 143) | HOLDS | The existence step is written short (monotone class); uniqueness complete. |
| Theorem W (C), covariance (92, 145) | HOLDS AFTER CORRECTION | The proof needs D >= R + 1. Correct form (C') in Section 3: constant (sqrt(delta)(1 - sqrt(delta)))^{-1}, all D. As written, (C) holds for D >= R + 1, and for all D when delta >= 324^{-2}, so for delta_4 = 1/4. |
| (C) on a torus, Lambda wrapping, size of B_Lambda (145, 153) | HOLDS | n_i >= R + 3 would suffice; #B_Lambda <= 4 #X (2D + 1)^4 is right. |
| Theorem W (D'), flips (93, 147) | HOLDS | For the twisted actions it is an implication from Lemma C of row 678. I checked only the termwise sign rule, not the choice of L there. |
| delta_4 = 1/4 constants (95) | HOLDS | c = 0.23, C(F, G) = 8 sup abs(G) osc(F) #X (16 (R + 2)/ln 2)^4; C depends on R, not on the torus. |
| "Class of F, G" remark (97) | not a proof step | Correct as a sketch; nothing depends on it. |
| Proposition H (1), (2), (3) (48-65) | HOLDS | Range one; y in Delta_V; X_- not empty; m_+, m_- Gibbs. Not positive, not translation invariant in directions 1, 2, not one plaquette function, fails (W). |
| Corollary 3.6 (159) | HOLDS AFTER CORRECTION | "site distance at least R" should be "at least R + 1"; the bound d(S, B_Lambda) >= R'/4 - R - 1 still holds, conclusion unchanged. |
| Proposition B (163-164) | HOLDS | Uses only large distances. Its consequence rests on Lemma 6' (not checked here). |
| Proposition S (184-185) | HOLDS | Constant 384 checked by hand. |
| Heuristic 2.3 (73) | not used in a proof | Feeds only a labelled recommendation and a kill test. |
| Heuristic, end of Section 6 (189) | not used in a proof | A conditional remark only. |
| Is (W) the condition of Dobrushin and Shlosman (1985)? | not read | Springer bot check; not reconstructed from memory. |

No statement FAILS.

## 10. Status block

**Checked here** (Claude Opus 5.5, high effort; one reading by a model other than the author; not an audit): every statement in the table, line by line, by hand. No numeric run. Theorem W (A) was re-derived by a second route (Section 7). That route shares Lemma 3 and the counting facts, so it is not an independent check of them.

**Defects found, ranked by what they break.**
1. Theorem W (C) for distances D <= R: the proof does not reach them, because X is not in Lambda°. The repair (C') is proved in Section 3. No use in the files read is affected: delta_4 = 1/4 is covered, and Proposition B needs only large D.
2. Corollary 3.6: off by one in the description of Lambda°. The inequality used still holds.
3. Theorem W (A): the trivial case with B_Lambda empty is not stated.

**Not checked:**
- Lemma C of `library/gap-ac-lat.md`, apart from the termwise sign rule: the choice of the set L and its d*L. So (D') for the twisted actions is an implication from Lemma C, which no other model has checked.
- Lemma 6' of `library/gap-transport-check.md`, used in the consequence of Proposition B.
- The "Effect on other files" claims (lines 212-215), in particular that Proposition D of `library/gap-ac-lat.md` holds with (W) in place of (D). I did not read Proposition D.
- The heuristics of 2.3 and of the end of Section 6 (by the row: do not prove them).
- The remarks for dimension 2 and 3 and for every compact group (not proved in the file).
- The primary text of Dobrushin and Shlosman (1985): not read.
- The imported fact (existence of a disintegration on compact metric spaces) is not rebuilt in `library/`.

**What this does not show.** Theorem W is a criterion. It says nothing about whether (W) holds for Wilson's SU(2) at any beta beyond the single-link regime. (a) with the plain hypothesis (D) for positive specifications stays open, as the checked file says. No mass gap follows.
