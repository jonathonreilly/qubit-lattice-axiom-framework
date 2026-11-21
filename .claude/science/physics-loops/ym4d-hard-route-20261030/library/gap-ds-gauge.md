lead: anthropic/claude-fable-5-2/medium mac-mini-worker
lease_until: 2026-11-11T15:52Z

# gap-ds-gauge (FINISH row 691): the finite-box criterion (DS-tw)

Provenance: Claude Fable 5.2, medium effort, one session, pinned at commit 53b90e6c9. Proved by Claude. Research-stage working state; no status is granted.

Check: checked line by line by Claude Opus 5.5 (high), `library/gap-ds-gauge-check.md` (FINISH row 693). No statement fails. Three corrections, applied in place by the lead (Claude Fable 5.2) on 2026-11-11 and marked "Corrected 2026-11-11": the trivial case of (A), the range of distances in (C), and one word in Corollary 3.6. The check did not cover Lemma C of `library/gap-ac-lat.md` (apart from its sign rule), Lemma 6' of `library/gap-transport-check.md`, the claims on other files, or the heuristics.

## 0. Repo search and duplicate check

- `library/open-core.md`: no entry for (DS-tw), P1-next, a finite-box criterion or a Dobrushin-type statement (grep for `DS-tw`, `P1-next`, `finite-box`, `Dobrushin`: no hit).
- `FINISH.md`: (DS-tw) is row 691 only. Rows 677, 678, 685 and the digests 686-690 name it as a follow-up or read literature; none attacks it.
- Not read (skipped, reported as skipped): `library/gap-zf-box-x.md` Sections 2 and 3, and `docs/SU2_TWO_REGION_BOUNDARY_RESPONSE_BOUNDED_THEOREM_NOTE_2026-11-08.md` on origin/main. Both are one-link Dobrushin arguments; the one-link case is (W) with V a single link and is not used here. The Sussman-Alpoge repository was not opened: the index has no entry for this statement.
- Digests read by grep: `library/prior/gap-crux-lit-cross.md` lines 17-19, 106, 113 say that the Dobrushin-Shlosman papers and Martinelli-Olivieri were **not read** by anyone here. `library/sa-index/`: no hit for "Dobrushin". So nothing in the repository or in the Sussman-Alpoge account proves a finite-box criterion; all of Section 3 is rebuilt here.
- Read in full: `library/gap-ac-lat.md` Sections 1, 3, 5-7; `library/gap-skeleton-max.md` lines 150-157 and 546. No numeric run was made in this item.
- Credit. The shape of the weighted hypothesis (W) of Section 3 is the one I remember from Dobrushin and Shlosman, "Constructive criterion for the uniqueness of Gibbs field" (1985). I did not read that paper; I do not claim that (W) or its proof here agree with theirs. The single-link case (V one link) is Dobrushin's uniqueness condition. The revealing argument discussed in 2.1 is van den Berg and Maes's disagreement percolation (memory). The flip lemma and Lemma C are from `library/gap-ac-lat.md` (row 678).

## 1. Result in short

1. **(a) with the plain hypothesis (D) is not proved, and the block argument cannot prove it.** The block form of Dobrushin's argument stops at one step (2.1): (D) controls the inner cube and says nothing about the collar between the inner cube and the boundary. An argument that uses only range one, a compact fibre and (D) for every cube of side R is refuted by an explicit example (Proposition H, 2.2): a range-one specification with fibre Z_2 on the links of Z^4, with hard constraints, for which (D) holds with delta = 0 for every cube of side R, and which has two Gibbs states. The example has hard constraints and is not translation invariant. Wilson's weight is positive, so this is not a counterexample to (a) for Wilson's SU(2) specification. For positive specifications (a) with plain (D) stays open (2.3).
2. **(a) is proved under the weighted hypothesis (W)** (Theorem W, Section 3), for every delta below 1, with explicit rate: conclusions (1) and (2) of the row, for all bounded measurable local functions F, G, on Z^4 and on every torus, for Wilson's action and every action that is conjugate to it by a flip in each cube. The proof does not use the group.
3. **(b)** holds for (W): (W) at (beta, R, delta) forces R + 2 >= (1/2) ln(1/delta) times the correlation length (Section 4).
4. **(c)** is not closed. A sufficient condition for (W) is proved (Section 5): exponential decay of the influence of one boundary link, uniformly in the boundary values, for cubes.

## 2. The plain hypothesis (D): where the block argument stops

Notation for the whole file. Sites are the points of Z^4 (or of a torus, Section 3). A link is a pair (x, i), x a site, i a direction; x is its lower end. For links l, l', d(l, l') is the sup-norm distance of the lower ends. A plaquette has four links. For a set Lambda of links, the boundary of Lambda is the set of links outside Lambda that share a plaquette with a link of Lambda. For a set S of sites, L(S) is the set of links with both ends in S. The cube of side R at the site a is V_R + a, V_R = L({0, ..., R}^4); it has |V_R| = 4 R (R+1)^3 links. Its inner cube is L(a + {R/4, ..., 3R/4}^4), R divisible by 4. The fibre is a compact metric space G with a probability measure lambda (Haar measure of SU(2) for Wilson). A specification gamma is given by a continuous function phi_p of the four link variables of each plaquette p: gamma_Lambda(d sigma | tau) = Z^{-1} exp(-sum over the p that meet Lambda of phi_p(sigma, tau)) times the product of lambda over Lambda. It depends on tau only through the boundary of Lambda. Wilson: phi_p = beta (1 - (1/2) tr U_p). TV(P, P') = sup over events of |P(A) - P'(A)|.

**(D) at (R, delta):** for every cube V of side R and all boundary values tau, tau', the laws that gamma_V(. | tau) and gamma_V(. | tau') induce on the inner cube differ by at most delta in total variation.

### 2.1 The step that fails, in three forms

The lead's sketch has three possible exact forms. Each one stops at the same place: the collar V minus the inner cube V'.

(i) *Resampling (dynamics).* Take a coupling of two Gibbs measures and resample the cube V in both copies, with a coupling of gamma_V(. | tau), gamma_V(. | tau') that makes the copies agree on V' with probability at least 1 - delta. If the copies differ somewhere on the boundary of V, (D) gives nothing on the collar: after the step the collar may disagree everywhere. The collar holds the fraction 1 - 2^{-4} of V and it covers the inner cubes of the neighbours. So one disagreement on the boundary of V can produce of order |V| disagreements, and no count of the form "delta times the number of spoiled blocks" comes out. If one only uses "inner cube agrees with probability 1 - delta, collar arbitrary", the set of agreement never contains the boundary of a cube (a connected shell of diameter R), because two inner cubes that both stay in agreement are separated by a collar of width R/4. So no cube is ever resampled with agreeing boundary values, and the disagreement does not contract.

(ii) *Revealing (disagreement percolation in blocks).* Reveal the two copies block by block and couple each new block given what is revealed. For a single link (V = V' = one link) this works, because every conditional law of the link given anything is a mixture of gamma_link(. | tau). For a cube with a collar it fails: once a block next to V' is revealed, it lies inside V, and the conditional law of V' given a part of the collar is not a mixture of the laws gamma_V(. | tau). (D) does not bound the dependence of this conditional law on the far boundary. Only blocks at mutual distance at least R/4 can be coupled this way; they do not separate anything.

(iii) *Functions (the dual form).* For f on the inner cube, g = gamma_V f has oscillation at most delta osc(f), and mu(f) = mu(g) for every Gibbs state mu. But g is a function on the boundary of V, a set of diameter R, and it is not a sum of functions supported in inner cubes. To iterate one needs (D) for functions on a shell, that is, for sets of diameter R and more. (D) for two adjacent inner cubes jointly does not follow from (D) for each: the joint law of two blocks can depend on the boundary when neither marginal does.

In all three forms the missing statement is the same: a bound on what one disagreement at the boundary does to the collar. This is point (i) of the row. (D) bounds a probability of any disagreement in V'. A contraction needs the expected number of disagreements created in all of V per disagreement on the boundary. Proposition H shows that the gap is real and not a matter of technique.

### 2.2 Proposition H: (D) with delta = 0 and two Gibbs states (fibre Z_2, hard constraints)

**The specification.** Fix P >= 3. T is the set of sites x of Z^4 with 0 <= x_1 < P and 0 <= x_2 < P (a thick tube). F is the set of plaquettes none of whose four sites lies in T. The fibre is Z_2 = {1, -1} with the uniform measure. X is the set of configurations s on the links of Z^4 with s(dp) = 1 for every p in F, where s(dp) is the product of s over the four links of p. X is a closed subgroup of the compact group Z_2^(links). The specification is uniform on X: for a finite set Lambda of links and x in X, gamma_Lambda(. | x) is the uniform measure on the finite set {z in X : z = x outside Lambda}. This is the Z_2 lattice gauge specification with plaquette weight 1{s(dp) = 1} on F and weight 1 on the other plaquettes. It has range one. Boundary values are the restrictions of points of X.

For a finite Lambda let Delta_Lambda be the group of the y in X with y = 1 outside Lambda. Then {z in X : z = x outside Lambda} = x Delta_Lambda.

**Proposition H.** Let R be divisible by 4 with 4 <= R and R/2 + 1 <= P.
(1) For every cube V of side R, with inner cube V', and all x, x' in X, the laws induced on V' by gamma_V(. | x) and gamma_V(. | x') are equal. So (D) holds at (R, 0).
(2) There are two different Gibbs states for this specification.
(3) For every finite Lambda there are boundary values x, x' for which gamma_Lambda(. | x) and gamma_Lambda(. | x') have disjoint supports on a fixed set of 4(P+1) links, as soon as Lambda contains that set. So no bound of the form C exp(-c dist/R) on the influence of the boundary holds.

Proof.
*Step 1 (flat on a box is exact).* Let B be a box of sites (a product of four intervals) and s a configuration on L(B) with s(dp) = 1 for every plaquette with its four sites in B. Then there is g : B -> Z_2 with s_(x,y) = g_x g_y for every link of L(B). Proof: fix a corner o of B and let g_x be the product of s along the path from o to x that first moves in direction 1, then 2, then 3, then 4. For a link (x, x + e_i), the paths to x and to x + e_i differ by moving the step in direction i past the later steps in the directions j > i; each elementary move changes the product by the factor s(dp) = 1 of one plaquette in B. QED Step 1.

*Step 2 (two boxes).* Let B_1, B_2 be boxes with B_1 intersect B_2 not empty, such that no link joins B_1 minus B_2 to B_2 minus B_1. If s on L(B_1 union B_2) has s(dp) = 1 on the plaquettes inside B_1 and on those inside B_2, then s_(x,y) = g_x g_y on L(B_1 union B_2) for some g. Proof: Step 1 gives g_1 on B_1 and g_2 on B_2. On the box B_1 intersect B_2, which is connected, g_1 g_2 has product 1 across every link, so it is a constant c. Put g = g_1 on B_1 and g = c g_2 on B_2. Every link of L(B_1 union B_2) lies in L(B_1) or L(B_2). QED Step 2.

*Step 3 (shape of an inner cube without the tube).* Let S' = I_1 x I_2 x I_3 x I_4 be the site box of an inner cube; each I_i has R/2 + 1 <= P points. J_i = I_i intersect [0, P), i = 1, 2, is empty, or all of I_i, or a segment of I_i that contains one end point of I_i (because I_i has at most P points, it cannot pass [0, P) on both sides). S' minus T = B_1 union B_2 with B_1 = (I_1 minus J_1) x I_2 x I_3 x I_4 and B_2 = I_1 x (I_2 minus J_2) x I_3 x I_4. Each is a box or empty. If both are non-empty they meet in (I_1 minus J_1) x (I_2 minus J_2) x I_3 x I_4. A point of B_1 minus B_2 has second coordinate in J_2 and first coordinate outside J_1; a point of B_2 minus B_1 has first coordinate in J_1 and second outside J_2; they differ in two coordinates, so no link joins them. A plaquette with four sites in B_1 (or B_2) is in F.

*Step 4 (proof of (1)).* The law induced on V' by gamma_V(. | x) is uniform on the coset x|_{V'} times Delta_V|_{V'} (the image of a uniform measure on a coset under a homomorphism is uniform on the image coset). So (1) follows if for every x in X there is y in Delta_V with y = x on V'. Let x in X. By Steps 2 and 3 (or Step 1 if one of the boxes is empty) there is g on S' minus T with x_(u,v) = g_u g_v for all links with both ends in S' minus T. Extend g by 1 to all other sites. Define y_(u,v) = g_u g_v on the links with both ends outside T; y = x on the links of V' that touch T; y = 1 on all other links that touch T. Then y(dp) = 1 for every p in F (the product of g_u g_v around a plaquette is 1), so y is in X. y = x on V'. y = 1 on every link that does not touch S'; a link that touches S' lies in V because S' has distance R/4 >= 1 from the complement of the site box of V. So y is in Delta_V. QED (1).

*Step 5 (the two sectors).* Let c_0 be the closed path around the square {-1, ..., P}^2 in the plane x_3 = x_4 = 0, and h(s) the product of s along c_0. Its sites are outside T. X_+ = {h = 1} and X_- = {h = -1} are closed, disjoint, and X_+ is a subgroup. X_- is not empty: let s = -1 on the links (x, x + e_2) with x_2 = 0 and x_1 >= P, and s = 1 elsewhere. A (1,2)-plaquette with base x, x_2 = 0, x_1 >= P contains two such links; with x_1 = P - 1 it contains the site (P-1, 0, ., .) of T, so it is not in F; a (2,j)-plaquette, j = 3, 4, contains two such links or none; the other plaquettes contain none. So s is in X, and c_0 contains exactly one such link, the one at x_1 = P, so h(s) = -1.
Every y in X with finite support has h(y) = 1: the translate c_n of c_0 by n e_3 misses the support for large n, and h(y) is the same on c_0 and c_n, because the band between c_k and c_{k+1} is a union of plaquettes of F (their sites lie over the path c_0, outside T), each with y(dp) = 1. So Delta_Lambda is contained in X_+ for every finite Lambda.

*Step 6 (proof of (2) and (3)).* Let m_+ be the Haar measure of the compact group X_+, and m_- its image under multiplication by a fixed s_- in X_-. Both are measures on X, with disjoint supports. m_+ is invariant under multiplication by Delta_Lambda, a finite subgroup of X_+; so is m_-, because the group is abelian. The classes of "equal outside Lambda" in X are the orbits x Delta_Lambda. For a bounded measurable f put f^(x) = |Delta_Lambda|^{-1} sum over y in Delta_Lambda of f(xy) = gamma_Lambda(f | x). It depends on x only outside Lambda, and for g measurable outside Lambda, m(f^ g) = m(f g) by the invariance. So gamma_Lambda(f | .) is the conditional expectation of f given the outside, for m = m_+ and m = m_-: both are Gibbs states. This is (2). For (3): if Lambda contains the links of c_0, gamma_Lambda(. | x) lives on {h = h(x)}, because x Delta_Lambda lies in the sector of x. Take x in X_+ and x' in X_-. QED

**What the example uses and does not use.** It has range one, a compact (finite) fibre, and (D) with delta = 0 for every cube of side R at every position, with R as large as wanted against the range (take P large). It has hard constraints, admissible boundary values only, and no translation invariance in the directions 1 and 2. So it refutes this statement: "range one, compact fibre and (D) for all cubes of side R with delta small give uniqueness". It refutes each of the three forms of 2.1 as a proof, because none of them uses positivity or translation invariance. The same construction works in dimension two (a finite hole) and three.

The mechanism is topological: the boundary value fixes a holonomy that no inner cube can see, and that every shell around the tube carries. In terms of 2.1 (iii): the law of the links of a shell depends on the boundary value, and the law of each piece of diameter below P does not.

### 2.3 What stays open for positive specifications

For a positive specification I have no proof of (a) from (D) and no counterexample. One remark, **heuristic, not proved**: if the constraint of Proposition H is replaced by a large finite plaquette coupling, a boundary value can force a defect (a frustrated plaquette, or a vortex sheet) into the cube, and the defect then lies in the inner cube with a probability that is not small; for a point defect an averaging over the translates of the cube gives a probability at least about 2^{-4} for some translate. So the softened examples violate (D) for small delta. This suggests that for positive specifications (D) with delta below a constant like 2^{-4} may be enough, by a proof that uses positivity. I did not find such a proof. The remark also says that "Known answers: Z_2 at large b: true, R of order one" in `library/gap-skeleton-max.md` line 155 is doubtful for the plain (D): in the deconfined phase of Z_2 a boundary value with frustrated plaquettes forces a vortex sheet through the cube (**heuristic, not proved**).

So the exact answer to point (i) of the row: (D) alone does not give the contraction; a weighted form is needed for the argument; the corrected hypothesis is (W) below.

## 3. Theorem W: the criterion with the weighted hypothesis

### 3.1 Statement

The lattice is Z^4 or a torus (Z/n_1) x ... x (Z/n_4) with all n_i >= R + 4. Then every cube V_R + a together with its boundary is a copy of the same set in Z^4. All links of (V_R + a) union its boundary have their lower ends in a + {-1, ..., R+1}^4, so their mutual distance d is at most r = R + 2. The fibre G and the specification gamma are as in Section 2, with phi_p continuous; G is any compact metric space with a probability measure. For configurations eta, eta' on a set V, rho_V(eta, eta') is the number of links l of V with eta_l different from eta'_l.

**(W) at (R, delta).** Let N_R = R (R+1)^3, the number of links of V_R in each of the four directions (|V_R| = 4 N_R). There are numbers k_z >= 0, z in the boundary of V_R, such that for each direction i the sum of k_z over the z of direction i is at most delta N_R, and such that: for every a, every z in the boundary of V_R, and all boundary values tau, tau' that are equal except at the link z + a, there is a coupling of gamma_{V_R + a}(. | tau) and gamma_{V_R + a}(. | tau') with expectation of rho_{V_R + a} at most k_z.

In words: one changed link on the boundary of the cube changes, on average, at most k_z links in the whole cube, collar included; and for each direction the sum of the k_z over the boundary links of that direction is below the number of links of that direction in the cube. (The sum is taken per direction because a translation keeps the direction of a link; see the three facts in 3.3. If the k_z are invariant under the lattice symmetries that map the cube to itself and permute the four directions, the condition is the same as: sum of all k_z <= delta |V_R|. Without symmetry, sum of all k_z <= delta |V_R| / 4 is sufficient.) For Wilson's specification on Z^4 it is enough to take a = 0, by translation invariance.

For a finite set Lambda of links, Lambda° is the set of the l in Lambda such that every cube V_R + a that contains l lies in Lambda, and B_Lambda = (Lambda minus Lambda°) union the boundary of Lambda.

**Theorem W.** Let gamma satisfy (W) at (R, delta) with delta < 1. Put eps = ln(1/delta) / (2 (R + 2)).
(A) (Finite sets.) For every finite set Lambda of links, all boundary values tau, tau', and every S contained in Lambda°, the laws that gamma_Lambda(. | tau) and gamma_Lambda(. | tau') induce on S satisfy TV <= (sqrt(delta) / (1 - sqrt(delta))) |B_Lambda| exp(-eps d(S, B_Lambda)). (Corrected 2026-11-11 after the check: if B_Lambda is empty, which can happen only on a torus with Lambda the set of all links, then gamma_Lambda does not depend on tau and TV = 0. The proof below is for B_Lambda not empty.)
(B) (One Gibbs state.) On Z^4 there is exactly one Gibbs state for gamma.
(C) (Covariance.) Let mu be the Gibbs state of (B), or the measure Z^{-1} exp(-sum over all p of phi_p) on a torus with all n_i >= R + 4. For bounded measurable F, G that depend on the links of finite sets X, Y with D = d(X, Y): |mu(FG) - mu(F) mu(G)| <= (1 - sqrt(delta))^{-1} sup|G| osc(F) 4 |X| (2D + 1)^4 exp(-eps D). No constant depends on the torus. (Corrected 2026-11-11 after the check. The proof below needs X inside Lambda°, so it covers D >= R + 1 only. As written, (C) is proved for D >= R + 1, and for every D when delta >= 324^{-2}; the value delta_4 = 1/4 used below is in that range. For every delta < 1 and every D >= 0 the proved form is (C'): the same bound with the constant (sqrt(delta)(1 - sqrt(delta)))^{-1} in place of (1 - sqrt(delta))^{-1}. For D <= R, (C') follows from the trivial bound |Cov(F, G)| <= osc(F) sup|G| and exp(-eps R) >= sqrt(delta). The proof of (C') is in Section 3 of `library/gap-ds-gauge-check.md`.)
(D') (Flips.) Let the fibre be SU(2) and let (W) hold at (R, delta) for Wilson's specification at beta on Z^4. Then (W) holds at (R, delta), with the same k_z, on every torus with all n_i >= R + 4 for every action sum of phi_p such that for each a there is a set L_a of links with phi_p(phi_{L_a} sigma) = beta (1 - (1/2) tr sigma(dp)) for every plaquette p that meets V_R + a. So (A), (C) hold for these actions. The twisted actions A_S of `library/gap-ac-lat.md` are of this kind when the fibre side is at least R + 4 (Lemma C there, applied to the cube with its boundary).

With delta_4 = 1/4: eps = ln 2 / (R + 2) >= 0.46 / R for R >= 4, and the bound of (C) is 8 sup|G| osc(F) |X| (2D+1)^4 2^{-D/(R+2)}. Since (2D+1)^4 exp(-eps D / 2) <= (16/eps)^4 for eps <= 1, this is at most C(F, G) exp(-c D / R) with c = 0.23 and C(F, G) = 8 sup|G| osc(F) |X| (16 (R+2) / ln 2)^4.

**Class of F, G.** All bounded measurable local functions; gauge invariance is not used. It would not enlarge anything: every Gibbs state of a lattice gauge specification is invariant under local gauge transformations (the conditional law of the links at a site x given the others is invariant under the transformation at x, and the state is the mixture of these laws), so it is determined by its values on gauge-invariant functions.

### 3.2 Lemmas

**Lemma 1 (several changed links).** Assume (W). For every a and all boundary values omega, omega' of V = V_R + a there is a coupling of gamma_V(. | omega), gamma_V(. | omega') with expectation of rho_V at most c_a(omega, omega') = sum of k_z over the z in the boundary of V_R with omega_{z+a} different from omega'_{z+a}.
Proof. List the links of the boundary of V where omega and omega' differ: y_1, ..., y_m. Let omega^j be equal to omega' at y_1, ..., y_j and to omega elsewhere. gamma_V(. | omega^m) = gamma_V(. | omega') because gamma_V depends only on the boundary of V. (W) gives a coupling K_j of mu_{j-1} = gamma_V(. | omega^{j-1}) and mu_j with expectation of rho_V at most k_{y_j - a}. Write K_j(d eta, d eta') = mu_{j-1}(d eta) kappa_j(eta, d eta') with a probability kernel kappa_j (regular conditional probability; G^V is a compact metric space). Let (eta^0, ..., eta^m) be the Markov chain with eta^0 distributed by mu_0 and transitions kappa_j. Then (eta^{j-1}, eta^j) has the law K_j, so eta^m has the law mu_m, and rho_V(eta^0, eta^m) <= sum over j of rho_V(eta^{j-1}, eta^j) because rho_V is a metric. The law of (eta^0, eta^m) is the coupling. QED

**Lemma 2 (a measurable family of couplings).** Assume (W) and fix a and eta_0 > 0. There is a probability kernel K from pairs (omega, omega') of boundary values of V = V_R + a to G^V x G^V such that K(omega, omega'; .) is a coupling of gamma_V(. | omega) and gamma_V(. | omega') with expectation of rho_V at most c_a(omega, omega') + eta_0.
Proof. Theta = G^(boundary of V) is a compact metric space. gamma_V(d eta | omega) = f_omega(eta) lambda^V(d eta) with f_omega(eta) = exp(-H(eta, omega)) / Z(omega), jointly continuous and positive on the compact set Theta x G^V. So there is kappa > 0 such that dist(omega, omega~) < kappa gives TV(gamma_V(. | omega), gamma_V(. | omega~)) = (1/2) int |f_omega - f_omega~| d lambda^V <= eta_0 / (2 |V|).
(i) An explicit maximal coupling. For omega, omega~ in Theta put t = int (f_omega - f_omega~)_+ d lambda^V, and let m(omega, omega~; eta, .) be the kernel: with probability min(f_omega, f_omega~)(eta) / f_omega(eta) the new point is eta; otherwise it is distributed by (f_omega~ - f_omega)_+ lambda^V / t (if t = 0 the second case has probability zero for almost every eta; put the new point equal to eta). It is measurable in (omega, omega~, eta). If eta has the law gamma_V(. | omega), the new point eta~ has the law min(f, f~) lambda + (f~ - f)_+ lambda = f~ lambda = gamma_V(. | omega~), and P(eta different from eta~) <= t = TV.
(ii) Cells. The set of pairs with a given set of disagreement {y : omega_y different from omega'_y} is a Borel set, and there are finitely many such sets. Cut each of them into finitely many Borel cells C_i on which omega and omega' each vary by less than kappa. On C_i the function c_a is a constant c_i. Choose (omega_i, omega'_i) in C_i and, by Lemma 1, a coupling K_i of gamma_V(. | omega_i), gamma_V(. | omega'_i) with expectation of rho_V at most c_i; write K_i = gamma_V(d eta | omega_i) kappa_i(eta, d eta').
(iii) For (omega, omega') in C_i let K(omega, omega'; .) be the law of (eta, eta') in the chain: eta distributed by gamma_V(. | omega); eta_i by m(omega, omega_i; eta, .); eta'_i by kappa_i(eta_i, .); eta' by m(omega'_i, omega'; eta'_i, .). By (i), eta_i has the law gamma_V(. | omega_i), then eta'_i has the law gamma_V(. | omega'_i), then eta' has the law gamma_V(. | omega'). rho_V(eta, eta') <= |V| 1{eta different from eta_i} + rho_V(eta_i, eta'_i) + |V| 1{eta'_i different from eta'}, with expectation at most eta_0/2 + c_i + eta_0/2. K is measurable on each cell as a composition of measurable kernels. QED

**Lemma 3 (one resampling step).** Let Lambda be finite, tau, tau' boundary values of Lambda, and P a coupling of gamma_Lambda(. | tau), gamma_Lambda(. | tau'), a measure on pairs (sigma, sigma') of configurations on Lambda. Put p_l = P(sigma_l different from sigma'_l) for l in Lambda and p_l = 1{tau_l different from tau'_l} for l outside. Let V = V_R + a lie in Lambda and eta_0 > 0. Then there is a coupling T_a P of the same two measures with disagreement probabilities p^a_l such that p^a_l = p_l for l in Lambda minus V, and sum over l in V of p^a_l <= sum over z in the boundary of V_R of k_z p_{z+a} + eta_0.
Proof. Draw (sigma, sigma') from P. Let omega be sigma on Lambda minus V and tau outside Lambda, and omega' the same with sigma', tau'. Draw (eta, eta') from K(omega, omega'; .) of Lemma 2. T_a P is the law of (eta on V and sigma on Lambda minus V; eta' on V and sigma' on Lambda minus V). First marginal: sigma has the law gamma_Lambda(. | tau), and replacing its part in V by a draw from gamma_V(. | omega) gives again gamma_Lambda(. | tau), because the density of gamma_Lambda(. | tau), as a function of the part in V with the rest fixed, is proportional to exp(-sum over the p that meet V of phi_p), which is the density of gamma_V(. | omega). The same for the second marginal. Outside V nothing changed. Given (sigma, sigma'), the expectation of rho_V(eta, eta') is at most sum over z of k_z 1{omega_{z+a} different from omega'_{z+a}} + eta_0; take the expectation over P. For z + a outside Lambda, omega_{z+a} = tau_{z+a}. QED

### 3.3 Proof of (A)

Fix Lambda, tau, tau'. Let Acal be the set of the a with V_R + a contained in Lambda, N = |Acal|. If Lambda° is empty there is nothing to prove. Let D(l) = d(l, B_Lambda) and w_l = exp(eps D(l)) for links l in Lambda union its boundary. D changes by at most d(l, l'), and d <= r = R + 2 on each cube with its boundary, so

(1) w_l <= e^theta w_{l'} for l, l' in (V_R + a) union its boundary, theta = eps r, e^theta delta = sqrt(delta).

For a coupling P put Phi(P) = sum over l in Lambda of w_l p_l. Let Phi_* be the infimum of Phi over all couplings (the product coupling exists). Fix eta_1 > 0 and a coupling P with Phi(P) <= Phi_* + eta_1, and eta_0 > 0. By Lemma 3 and (1), for a in Acal, with V = V_R + a:

Phi(T_a P) = Phi(P) - sum_{l in V} w_l p_l + sum_{l in V} w_l p^a_l <= Phi(P) - sum_{l in V} w_l p_l + e^theta sum_z k_z w_{z+a} p_{z+a} + eta_0 w_max,

because sum_{l in V} w_l p^a_l <= (max over V of w)(sum_z k_z p_{z+a} + eta_0) and max over V of w <= e^theta w_{z+a}. Here w_max is the maximum of w. Since Phi(T_a P) >= Phi_* >= Phi(P) - eta_1, summing over a in Acal gives

(2) sum_{l in Lambda} n_l w_l p_l <= e^theta sum_y K_y w_y p_y + N (eta_0 w_max + eta_1),

where n_l is the number of a in Acal with l in V_R + a, and K_y is the sum of k_{y-a} over the a in Acal with y - a in the boundary of V_R. Three facts:
- K_y <= delta N_R: the link z = y - a has the direction of y, and different a give different z; so K_y is at most the sum of k_z over the z of the direction of y.
- K_y = 0 unless y is in the boundary of a cube contained in Lambda; such a y is in Lambda or in the boundary of Lambda. So the y with K_y > 0 lie in Lambda° union B_Lambda.
- n_l <= N_R, and n_l = N_R for l in Lambda°: the a with l in V_R + a correspond to the links l - a of V_R, which have the direction of l, and for l in Lambda° all of them are in Acal.
On B_Lambda, w = 1 and p <= 1. So (2) gives

N_R sum_{l in Lambda°} w_l p_l <= sqrt(delta) N_R (sum_{l in Lambda°} w_l p_l + |B_Lambda|) + N (eta_0 w_max + eta_1),

(3) sum_{l in Lambda°} w_l p_l <= (sqrt(delta) / (1 - sqrt(delta))) |B_Lambda| + N (eta_0 w_max + eta_1) / ((1 - sqrt(delta)) N_R).

For S in Lambda°, the total variation distance of the two laws on S is at most P(sigma, sigma' differ on S) <= sum_{l in S} p_l <= exp(-eps d(S, B_Lambda)) sum_{l in Lambda°} w_l p_l. The left side does not depend on P, eta_0, eta_1. Let eta_0, eta_1 tend to zero in (3). QED (A)

Remark on what is proved. The decay in (A) is in the distance from B_Lambda, the part of Lambda near its boundary, and not in the distance from the links where tau and tau' differ. This is weak mixing. The proof does not give strong mixing, because links near the boundary of Lambda are covered by fewer than N_R cubes.

### 3.4 Proof of (B), (C), (D')

(B). A Gibbs state exists: G^(links) is compact, and every weak limit point of gamma_{Lambda_N}(. | tau), Lambda_N = L({-N, ..., N}^4), is a Gibbs state because gamma_Lambda maps continuous functions to continuous functions. Let mu, nu be Gibbs states and f a continuous function of the links of a finite set S. mu(f) is the mu-average of gamma_{Lambda_N}(f | tau) and nu(f) the nu-average, so |mu(f) - nu(f)| <= osc(f) sup over tau, tau' of the TV distance on S. A link with both ends in {-N + R, ..., N - R}^4 is in Lambda_N°. So d(S, B_{Lambda_N}) >= N - R - c(S) and |B_{Lambda_N}| <= 4 (2N + 3)^4, and (A) gives the limit zero as N grows. So mu = nu.

(C). mu satisfies mu(gamma_Lambda(f | .) g) = mu(f g) for every finite Lambda and every bounded g that does not depend on the links of Lambda (on the torus by the same density computation as in Lemma 3; Lambda may wrap around the torus). Let Lambda be the set of links l with d(l, X) <= D - 1. It does not meet Y. So mu(FG) - mu(F) mu(G) = mu(G (gamma_Lambda F - mu(gamma_Lambda F))), and its modulus is at most sup|G| osc(F) times the supremum over tau, tau' of the TV distance on X. If d(l, X) <= D - 1 - R and l is in V_R + a, every link of V_R + a is within d <= R of l, so within D - 1 of X: l is in Lambda°. So the links of B_Lambda have d(., X) >= D - R, and d(X, B_Lambda) >= D - R. Links of Lambda and of its boundary have lower ends within D of a lower end of a link of X, so |B_Lambda| <= 4 |X| (2D + 1)^4. On a torus the proof of (A) holds as written: it uses only that each cube with its boundary is embedded (n_i >= R + 4) and that a -> y - a is one to one. (A) gives TV <= (sqrt(delta)/(1 - sqrt(delta))) 4 |X| (2D+1)^4 exp(-eps (D - R)), and exp(eps R) <= exp(eps r) = delta^{-1/2}. QED (C)

(D'). phi_L multiplies the links of L by -1. It is a bijection of configurations that preserves the product of Haar measures, maps pairs that differ exactly at one link y to pairs that differ exactly at y, and preserves rho_V. By the hypothesis on the action, its density in V = V_R + a given tau is the Wilson density at (phi_{L_a} sigma, phi_{L_a} tau), so gamma^{action}_V(. | tau) is the image under phi_{L_a} of gamma^{Wilson}_V(. | phi_{L_a} tau). The image under phi_{L_a} x phi_{L_a} of a coupling for Wilson's specification is a coupling for the action with the same expectation of rho_V. The cube with its boundary in the torus is a copy of the one in Z^4, and Wilson's specification is translation invariant. QED

### 3.5 The five points of the row

(i) (D) alone does not give the contraction (Section 2). The weighted form (W) does. The weight is, per direction, the sum of k_z over the boundary against the number N_R of links of the cube.
(ii) Measurable couplings: Lemma 2, by continuity of the density in the boundary value and an explicit maximal coupling. No measurable selection theorem is used. The one imported fact is the existence of regular conditional probabilities on compact metric spaces (Lemma 1, Lemma 2 (ii)).
(iii) Torus: the proof of (A) is local; it needs n_i >= R + 4 and nothing else. The set Lambda may wrap.
(iv) Flips: (D').
(v) Any delta < 1 works; delta_4 = 1/4 gives eps = ln 2 / (R + 2).

### 3.6 Corollary: (W) gives (D) at a larger scale

Let (W) hold at (R, delta), delta < 1. For the cube Lambda = V_{R'} (R' divisible by 4) and S its inner cube: a link with both ends at site distance at least R + 1 from the complement of the site box is in Lambda° (corrected 2026-11-11 after the check; the first version said R, which is off by one, and the bound that follows holds as written), so d(S, B_Lambda) >= R'/4 - R - 1, and |B_Lambda| <= 4 (R' + 3)^4. By (A), (D) holds at (R', delta') as soon as (sqrt(delta)/(1 - sqrt(delta))) 4 (R' + 3)^4 exp(-eps (R'/4 - R - 1)) <= delta'. For fixed delta, delta' this holds for R' >= C R ln R. So (W) at R is at least as strong as (D) at a scale of order R ln R. Whether (D) gives (W) at some scale is open for positive specifications and false with hard constraints (Proposition H: there (D) holds at (R, 0) and the conclusion of (A) fails).

## 4. Statement (b): the size of the hypothesis

**Proposition B (proved, for (W)).** Let (W) hold at (beta, R, delta), delta < 1, for a specification on Z^4, and let mu be its Gibbs state. Let m be the supremum of the rates m' such that |mu(F G_x) - mu(F) mu(G)| <= C(F, G) exp(-m' |x|) for all bounded local F, G, where G_x is G translated by x and |x| is the sup norm. Then m >= eps = ln(1/delta) / (2 (R+2)). With the correlation length xi = 1/m: R + 2 >= (1/2) ln(1/delta) xi. The same holds for the rate m_gi of the gauge-invariant functions alone, because m_gi >= m.
Proof. Theorem W (C): d(X, Y + x) >= |x| - c(X, Y), and the factor (2D+1)^4 is absorbed by any m' < eps. QED

Consequence, **given Lemma 6' of `library/gap-transport-check.md` (not re-read here; checked by one model there)**: m_gi <= C exp(-c_AF beta (1 + o(1))) gives R + 2 >= (ln(1/delta) / (2C)) exp(c_AF beta (1 + o(1))). So (W) can hold only for cubes of side at least of the order of the correlation length.

What this says, as the row asks. Theorem W is true for every compact fibre, with or without a gap; where there is no gap, (W) fails at every R, by Proposition B. It does not cross the region of couplings of order one. It replaces a crux by the one hypothesis (W) at one scale. The gap does not follow from anything in this file.

For the plain (D): (b) is not proved, because (a) is not. Proposition H shows that with hard constraints (D) at (R, 0) puts no bound on R against any length. By 3.6, (W) at R gives (D) at R' of order R ln R, so (D) is the weaker hypothesis at comparable scales.

## 5. Statement (a), the line by line check for other fibres

The proof of Theorem W (A), (B), (C) uses: a compact metric fibre with a probability measure; plaquette terms phi_p that are continuous; range one (gamma_V depends on the boundary of V only; the density computation in Lemma 3); translation only through the counting facts in 3.3. It uses no group structure, no gauge invariance, no positivity of phi beyond finiteness, no reflection positivity. So it holds word for word for U(1) and Z_2 (for a finite fibre the continuity in Lemma 2 is trivial).

Lines that use the group: only (D'). It uses that -1 is a central element (true in SU(2), U(1), Z_2) and that the flip preserves Haar measure. The remark on gauge invariance of Gibbs states in 3.1 uses the gauge group, but nothing depends on it.

Proposition H uses the fibre Z_2 and hard constraints. The same example exists for every compact group G (flat connections outside the tube; the sectors are the conjugacy classes of the holonomy around the tube), **not written out**.

## 6. Statement (c): what is proved about a converse

(a) is closed only in the form with (W), so (c) is treated for (W), briefly.

**Proposition S (a sufficient condition; proved).** Suppose there are C_0, m > 0 and R_0 such that for every cube V of side R >= R_0, every z in the boundary of V and all boundary values that are equal except at z, there is a coupling of the two laws gamma_V with P(sigma_l different from sigma'_l) <= C_0 exp(-m d(l, z)) for every l in V. Put A(m) = sum over x in Z^4 of exp(-m |x|), finite. Then (W) holds at (R, delta) for every R >= max(R_0, 384 C_0 A(m) / delta).
Proof. Take k_z = sum over l in V of C_0 exp(-m d(l, z)) <= 4 C_0 A(m) (four links per lower end). The boundary links of V_R of one direction have lower ends in {-1, ..., R+1}^4 and are not in V_R; their number is at most (R+3)^4 - R (R+1)^3 <= (R+3)^4 - R^4 <= 12 (R+3)^3. So the sum of k_z over one direction is at most 48 C_0 A(m) (R+3)^3, and (R+3)^3 <= 8 (R+1)^3 gives at most (384 C_0 A(m) / R) N_R. QED

So: exponential decay of the influence of one boundary link, uniform in the boundary values, for cubes (a strong-mixing property for cubes) gives (W) at large R; (W) gives weak mixing for all finite sets (Theorem W (A)) and (D) at larger scales (3.6). I did not prove that weak mixing gives back (W).

**Not proved, and why.** A gap for gauge-invariant functions in the one Gibbs state does not give (W) or (D) by any argument I have. The obstruction is the one of `library/gap-ac-lat.md` 3.2: both hypotheses are suprema over all boundary values, rough ones included, and a covariance bound in one state does not control them. A converse cannot be proved without using the group, if the following is true (**heuristic, not proved**): Z_2 lattice gauge theory in four dimensions at large beta has one Gibbs state with exponential decay for gauge-invariant functions, while a boundary value with frustrated plaquettes forces a vortex sheet through the cube, so that (D) fails at every R, and then (W) fails at every R by 3.6.

## 7. Status block

**Stop:** rule (ii) of row 691, in this exact sense: a counterexample to the group-free and positivity-free form of (a) (Proposition H), the corrected hypothesis (W), and a proof of (a) under (W) (Theorem W). (a) with the plain (D) for Wilson's positive weight is neither proved nor refuted.

**Proved here** (by hand, one author, Claude; checked line by line by Claude Opus 5.5 high, `library/gap-ds-gauge-check.md`, row 693: no statement fails, three corrections marked above; no numeric run):
- Proposition H: a range-one Z_2 link specification on Z^4 with hard constraints for which (D) holds at (R, 0) for every cube, with two Gibbs states and no decay of the influence of the boundary.
- Theorem W: under (W) at (R, delta), delta < 1: (A) weak mixing for every finite set, TV <= (sqrt(delta)/(1 - sqrt(delta))) |B_Lambda| exp(-eps d(S, B_Lambda)), eps = ln(1/delta)/(2(R+2)); (B) one Gibbs state on Z^4; (C) covariance bound for all bounded measurable local F, G on Z^4 and on every torus with sides at least R + 4, constants independent of the torus; (D') transfer of (W) to every action conjugate to Wilson's by a flip in each cube. With delta_4 = 1/4: rate ln 2/(R+2).
- Lemmas 1-3: gluing of couplings, a measurable family of couplings without a selection theorem, the resampling step.
- Corollary 3.6: (W) at R gives (D) at R' of order R ln R.
- Proposition B: (W) at (R, delta) forces R + 2 >= (1/2) ln(1/delta) xi.
- Proposition S: uniform exponential decay of the influence of one boundary link in cubes gives (W) at R >= 384 C_0 A(m)/delta.

**Used and not proved here:** existence of regular conditional probabilities on compact metric spaces (measure theory); Lemma C of `library/gap-ac-lat.md` for the twisted actions (row 678, not checked by another model); Lemma 6' of `library/gap-transport-check.md` in the consequence of Proposition B.

**Heuristic, labelled as such:** 2.3 (softened examples violate (D) for delta below about 2^{-4}; plain (D) for deconfined Z_2), Section 6 last paragraph.

**Open:**
- (a) with plain (D) for positive specifications. The step that fails is the collar step of 2.1.
- (c): any converse from a gap in one state.
- Whether (W) holds for Wilson's SU(2) at any beta beyond the single-link Dobrushin regime (V one link, small beta). Nothing here bears on it.

**Effect on other files (for the lead; I did not edit them).**
- Proposition D of `library/gap-ac-lat.md` 3.4 holds with (W) in place of (D): its second hypothesis ("P1-next in torus form") is Theorem W (C), (D') under (W), for all n >= R + 4, with rate ln(1/delta)/(2(R+2)). Its statement with the plain (D) stays conditional.
- `library/gap-skeleton-max.md` lines 150-157 and 546 state the criterion with (D) and credit it to Dobrushin and Shlosman from memory. As written it is not a known theorem here; with hard constraints it is false (Proposition H). The line "Z_2 at large b: true, R of order one" is doubtful (2.3).
- The crux hypothesis at one scale should be (W), or (D) together with the next statement.

**The one exact next statement (D-to-W).** For a range-one specification on the links of Z^4 with compact fibre and continuous finite plaquette terms phi_p (positive weight): there are absolute delta_4 > 0, delta' < 1 and C such that (D) at (R, delta_4) gives (W) at (R', delta') for some R' <= C R ln R. Equivalent task: bound, for boundary values that differ at one link, the expected number of disagreeing links in the collar of a cube, using (D) for the smaller cubes inside the collar and the positivity of the weight. Kill test first: soften Proposition H (plaquette coupling b large instead of the constraint, tube kept) and decide by hand whether (D) can hold there with delta below 2^{-4} while the two sectors stay distinct; 2.3 says no, without proof. If (D-to-W) is false for positive weights, the crux hypothesis is (W) and nothing weaker of this type.
