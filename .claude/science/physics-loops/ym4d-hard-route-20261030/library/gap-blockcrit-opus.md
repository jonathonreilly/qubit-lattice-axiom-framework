# A gauge-invariant block criterion for 4D Wilson SU(2) (FINISH row 836), by Claude Opus 5.5 (max effort), author

- Clone: `/Users/jonreilly/ym4d-lead/clone`, commit `83f6ffafe92a18e8d6d415b47453e830424e4160` (`git pull --ff-only`: already up to date).
- Lane directory D = `.claude/science/physics-loops/ym4d-hard-route-20261030`. Paths below are relative to D.
- Read in full for this note: FINISH rows 794 to 837 (`FINISH.md` lines 870-913); `library/gap-mixed-opus.md` (row 818) with its check `library/gap-mixed-check-astra.md` (row 829, verdicts and disposition); `library/gap-shape-exercise-astra.md` Route D (lines 241-357) and Route C (lines 475-618) with `library/gap-shape-check-opus.md` (row 824, all); `library/gap-arealaw-opus.md` Sections 1 and 3 (lines 57-306) with the verdict lines of `library/gap-arealaw-check-astra.md` (row 828); `library/gap-block-astra.md` Sections 1, 2, 5 (lines 33-203, 438-561) with `library/gap-block-check-opus.md` items 6 and 10 (row 808); `library/gap-skeleton-final.md` Sections 0-5 (lines 1-150) and 13.8, 13.12, 13.13 (lines 376-530); `library/prior/gap-lit-dp.md` (row 821, all); `library/gap-tu-retry.md` lines 55-347 (row 786, checked by row 794); `library/gap-ds-gauge.md` (row 691, all; checked by row 693); `library/gap-vmf-lip.md` lines 57-80, 192-315, 419-560 with the verdict lines of `library/gap-vmf-lip-check-opus.md` (row 790); `library/gap-crux-exercise-astra.md` lines 1240-1380 (the definition of PA_g) and the RESULT fields of FINISH rows 763, 764, 769, 775, 777, 779 (PA_g refuted on its covers).
- Coordinator message (2026-11-12): the row 832 guide result, quoted in Section 6.3. GUIDE only.
- Method: by hand. A GUIDE run (numpy, under 50 MB, seconds) checked walk sums and compared block shapes; no proof step rests on it.
- Labels: PROVED (hand proof in this note; one author, not an independent check), READ (from a file, with path and line), ARGUED (an inference short of proof), GUIDE (a numeric run that may refute or guide, never discharge), OPEN (missing).
- No repository file was edited. Only this file and GUIDE scripts in the scratchpad folder `lane836/guide/` were written.

## 0. Checkpoint (updated in place)

- Final checkpoint. All sections written: 1 (inputs), 2 (the criterion: vertex blocks, admissible gauge fixing, Lemma GF, coefficient (2.4)), 3 (Theorem R, the reduction; Theorem R', quotient form), 4 (Theorem ST: stars, beta < (sqrt 37 - 5)/3), 5 (Corollary SEED), 6 (larger blocks GUIDE, Proposition CEIL, the four tools, order one), 7 (Theorem U, U(1) Villain), 8 (summary).
- Not done: hand proofs for blocks larger than the star (GUIDE values only); any order-one estimate; an outside literature search on star blocks. No repository file was edited; GUIDE scripts are in the scratchpad folder `lane836/guide/`.

## 1. Setting and the inputs reused

**Conventions (READ `library/gap-arealaw-opus.md` lines 59-71).** Lane beta is Wilson's beta_W. SU(2) is the unit quaternions, the sphere S^3 in R^4, with `<a, b> = Re(a conj(b))`, chord metric `|a - b|`, Haar probability sigma. On a periodic four-torus Lambda with vertex set V and link set E, the measure is

    mu(dU) = Z^(-1) prod_p exp(beta eps_p x_p) prod_e sigma(dU_e),   x_p = Re U_p = (1/2) tr U_p,

with fixed centre signs eps_p in {+1, -1} (eps = 1 is the untwisted law). The gauge group SU(2)^V acts by `(g.U)_e = g_s(e) U_e conj(g_t(e))`; mu is invariant. Write x = beta/4 throughout.

**Function classes.** For a function f on SU(2)^E and a link e, `delta_e(f)` is the chord Lipschitz constant of f in the variable U_e (the others fixed), as in Lemma DC (READ `library/gap-vmf-lip.md` lines 246-252). `Lip` is the class of continuous f with all `delta_e(f)` finite; `Lip_inv` its gauge-invariant part. Gauge transformations act on each link by left and right multiplication, which are chord isometries, so `delta_e(f o g) = delta_e(f)` for every gauge transformation g.

**Block kernels.** For a link set B, `gamma_B(dsigma | y)` is the Wilson conditional law of the links of B given the links y off B; its density with respect to Haar on SU(2)^B is proportional to the product of `exp(beta eps_p x_p)` over the plaquettes p that meet B. `Gamma_B g(y) = integral g(sigma, y) gamma_B(dsigma | y)` is the block heat-bath operator; it is the mu-conditional expectation given the links off B, a self-adjoint projection in L^2(mu).

**Inputs reused (all checked by another model, as marked).**

- Theorem V and Corollary V1 (READ `library/gap-vmf-lip.md` lines 59-78 and 209-220; check `library/gap-vmf-lip-check-opus.md` lines 9-33, HOLDS): for `mu_F` proportional to `exp(<F, h>) sigma(dh)` on S^3, `d_Lip(mu_F, mu_F') <= |F - F'|/4` for all F, F' in R^4 (chord Wasserstein in dual form).
- Lemma DC, chord form (READ `library/gap-vmf-lip.md` lines 222-313; check lines 35-55, HOLDS), with the refinement that the diameter 2 in its step (11) may be replaced by the actual conditional discrepancy at the sites of D (READ `library/gap-block-astra.md` (B26), lines 497-512; check `library/gap-block-check-opus.md` item 6, "Modified DC step ... HOLDS").
- Lemma W (READ `library/gap-mixed-opus.md` lines 44-62; check `library/gap-mixed-check-astra.md` item 2, HOLDS) and Lemma S, the forest slice (READ `library/gap-mixed-opus.md` lines 18-40; check item 1, HOLDS).
- Lemma D1 (READ `library/gap-shape-exercise-astra.md` lines 266-339; check `library/gap-shape-check-opus.md` item 1, HOLDS): every tilted law `mu_h` on S^3 has Poincare constant at least 3, uniformly in h. The gauge reserve (C4) (READ lines 475-553; check item 2, HOLDS).
- Lemma S of row 825, slab independence (READ `library/gap-arealaw-opus.md` lines 186-211; check `library/gap-arealaw-check-astra.md` line 82, HOLDS).
- The chain from a plaquette-mean comparison to the seed and to a lattice gap: Theorem DOB, its proof and its arithmetic through Theorem SH (READ `library/gap-vmf-lip.md` lines 419-560; check row 790).
- Theorem V for periodic Villain U(1) at beta >= 2^14, gauge-invariant Langevin gap tending to 0 (READ `library/gap-tu-retry.md` lines 89-101 and 333-345; check row 794, `library/gap-tu-check-opus.md`, every step HOLDS).
- Theorem W of row 691, the Dobrushin-Shlosman-type block criterion in Hamming form, and Proposition H (READ `library/gap-ds-gauge.md` lines 44-150; check row 693, no statement fails).

## 2. The criterion

### 2.1 Vertex blocks and their internal gauge group

Let Q be a finite set of vertices. Put

    B(Q)  = the links with at least one endpoint in Q,
    O(Q)  = the endpoints of links of B(Q) that are not in Q (outer vertices),
    Ev(Q) = the links j not in B(Q) that share a plaquette with a link of B(Q) (exterior events),
    P_j   = the plaquettes that contain j and at least one link of B(Q), for j in Ev(Q).

A block of this kind contains every link at every vertex of Q. The group G_Q = SU(2)^Q acts on SU(2)^B(Q) by the gauge action at the vertices of Q only: a link with both ends in Q is rotated at both ends, a link from Q to an outer vertex only at its Q-end.

**Lemma G (PROVED).** Let B = B(Q).
(i) gamma_B(. | y) depends on y only through the links of Ev(Q).
(ii) gamma_B(. | y) is invariant under G_Q, for every exterior y and every choice of centre signs.
(iii) Every plaquette of P_j contains at least two links of B, and they meet at a vertex of Q.
(iv) Gamma_B maps Lip into Lip, and Lip_inv into Lip_inv.

*Proof.* (i) The density of gamma_B is the product of the plaquette factors of the plaquettes that meet B; their links off B are exterior events by definition. (ii) Each factor `exp(beta eps_p Re U_p)` is invariant under the full gauge group. A gauge transformation supported on Q moves only links with an endpoint in Q, that is links of B. So the density is G_Q-invariant, and so is Haar measure. (iii) Write j = (u, u') and p = (u, u', w', w). Since j is not in B, u and u' are not in Q. A link of p in B therefore has w or w' as an endpoint in Q. If w is in Q, both (w, u) and (w, w') are in B and meet at w; the case w' in Q is the same. (iv) Gamma_B g is the integral of g against a kernel whose density is smooth in the exterior, so Gamma_B g is continuous. Its seminorms vanish for the links of B; for the other links off Ev(Q), `delta_j(Gamma_B g) <= delta_j(g)`; for j in Ev(Q), `delta_j(Gamma_B g) <= delta_j(g) + osc(g) L_j`, with L_j a Lipschitz constant of y_j -> gamma_B(. | y) in total variation (the density is a smooth positive function of y_j on a compact set). Lemma GF below gives the sharp form. For a gauge transformation h, gamma_B(. | h.y) is the image of gamma_B(. | y) under h restricted to B (covariance of the conditional law), so `Gamma_B(g o h) = (Gamma_B g) o h`. QED

### 2.2 Admissible fixing sets: the boundary gauge

The outer vertices carry no symmetry of the block law: a gauge rotation at an outer vertex also moves exterior links. This is the boundary gauge, and the following rule handles it.

**Definition.** A set F of links of B(Q) is *admissible* if the graph (V, F) is a forest and each of its components contains at most one outer vertex. In a component with an outer vertex, that vertex is its root. In a component without one, choose a root in Q (vertices of Q met by no link of F are their own components). Put `G'_F = {eta in G_Q : eta_r = 1 at the roots in Q}` and `S_F = {sigma in SU(2)^B : sigma_f = 1 for f in F}`, identified with SU(2)^(B \ F).

**Lemma F (PROVED; the proof of Lemma S (i)-(ii) of row 818, READ `library/gap-mixed-opus.md` lines 26-34, with outer vertices as roots).** For admissible F, the map `Phi(eta, sigma') = eta.sigma'` is a bijection from `G'_F x S_F` onto SU(2)^B. It carries Haar on G'_F times Haar on SU(2)^(B \ F) to Haar on SU(2)^B, and

    gamma_B(. | y) = Phi_*( Haar_(G'_F) (x) gammatilde_F(. | y) ),                       (2.1)

where gammatilde_F(. | y) on S_F has density proportional to the product of the plaquette factors with the F-links set to 1.

*Proof.* Given sigma, process each tree of F from its root. For a tree link f from a reached vertex to a new vertex u, the vertex u is in Q, because each tree has at most one outer vertex and it is the root. The action of eta_u on f is a left or right multiplication by eta_u or its conjugate, so exactly one eta_u gives `(eta.sigma)_f = 1`. Acyclicity makes the definition consistent, and the inverse is smooth. The new value is an inversion and translation of sigma_f, so Fubini along the tree order maps Haar on the F-links to Haar on G'_F; for fixed eta the non-F links are translated. Invariance of the density under G_Q, which contains G'_F (Lemma G (ii)), gives (2.1), as in Lemma S (ii). QED

A component with two outer vertices is not admissible: no gauge freedom of the block would fix its second link to 1. This is the explicit boundary-gauge constraint.

### 2.3 The gauge-fixed response (Lemma GF)

For admissible F and j in Ev(Q), define on the free links `B \ F`

    n(c, d) = number of plaquettes that contain both links c and d,
    C^F_cd  = x n(c, d)  (c != d free),     b^(F,j)_c = x n(c, j),
    K^(F,j)_c = [ (I - C^F)^(-1) b^(F,j) ]_c .                                          (2.2)

**Lemma GF (PROVED from Corollary V1 and the refined Lemma DC, both READ and checked).** Let all torus periods be at least 3. Suppose the largest row sum of C^F is below 1. Let y, y' be exteriors that differ only at the link j in Ev(Q). Then for every function h on SU(2)^B with finite seminorms,

    | gamma_B(h | y) - gamma_B(h | y') |  <=  sum_(c in B \ F) delta_c(h) K^(F,j)_c |y_j - y'_j| .          (GF)

Consequently, for g in Lip,

    delta_j(Gamma_B g) <= delta_j(g) + sum_(c in B \ F) K^(F,j)_c delta_c(g)   (j in Ev(Q)),
    delta_j(Gamma_B g) = 0 (j in B),     delta_j(Gamma_B g) <= delta_j(g) (otherwise).   (2.3)

*Proof.* Step 1. Use (2.1) for y and for y'. The map Phi and the Haar factor do not depend on the exterior. So
`gamma_B(h | y) - gamma_B(h | y') = integral [ gammatilde_F(h_eta | y) - gammatilde_F(h_eta | y') ] dHaar(eta)`, with `h_eta = h o Phi(eta, .)`.
Step 2. Phi(eta, .) acts on each free link by a left or right multiplication, an isometry. So `delta_c(h_eta) = delta_c(h)` for c free.
Step 3. Under gammatilde_F(. | y) the conditional law of a free link c given the other free links has density proportional to `exp(<F_c, U_c>)`, a von Mises-Fisher law, with F_c equal to beta times the sum over the plaquettes p through c of eps_p times the conjugated staple of c in p (F-links set to 1). At periods at least 3 no plaquette repeats a link, so each other link of p enters the staple once, as a left or right factor. Changing a free link d moves F_c by at most `beta n(c, d) |U_d - U'_d|`; changing j moves F_c by at most `beta n(c, j) |y_j - y'_j|`. Corollary V1 bounds the corresponding chord distances of the conditional laws by x n(c, d) |U_d - U'_d| and x n(c, j) |y_j - y'_j|.
Step 4. The two gauge-fixed laws have the same conditional laws at every free site outside `D = {c : n(c, j) > 0}`. The refined Lemma DC (the diameter 2 in its step (11) replaced by the actual conditional discrepancy, READ `library/gap-block-astra.md` lines 497-512, check `library/gap-block-check-opus.md` item 6) gives
`|gammatilde_F(h_eta | y) - gammatilde_F(h_eta | y')| <= sum_c delta_c(h_eta) [ (sum_(m >= 0) (C^F)^m) b^(F,j) ]_c |y_j - y'_j|`. The series is (I - C^F)^(-1) because the row sums are below 1.
Step 5. Integrate over eta and use Step 2. This is (GF).
Step 6. For (2.3), split `Gamma_B g(y) - Gamma_B g(y')` into the change of the integrand under the fixed law gamma_B(. | y), at most `delta_j(g) |y_j - y'_j|`, and the change of the law for the fixed integrand `h = g( . , y')`, bounded by (GF) with `delta_c(h) <= delta_c(g)`. The other two cases of (2.3) are immediate. QED

**Remark GF' (PROVED).** (1) The hypothesis "largest row sum of C^F below 1" may be replaced by "spectral radius of C^F below 1". Run the proof of Lemma DC with the weighted seminorm `sum_c u_c delta_c`, where u is a positive vector with `C^F u <= rho u` on each connected component (its Perron vector; C^F is symmetric and nonnegative): the averaged update contracts this seminorm by `1 - (1 - rho)/N`, so `P^t f -> mu(f)` uniformly, and the telescoping gives the same bound with the convergent series `(I - C^F)^(-1) = sum_m (C^F)^m`. (2) With F empty, Steps 3 to 6 apply to any link set B (no gauge fixing; Phi is the identity), which gives valid numbers K for arbitrary link blocks.

**What the lemma does with gauge directions (ARGUED, a reading of the proof).** The coupling behind (GF) shares the gauge rotation eta exactly between the two copies. Directions of G_Q are never paid. The block configuration is measured only on the free links, that is in the section S_F of the quotient SU(2)^B / G'_F. So (GF) is a Dobrushin bound in a metric on block configurations modulo the internal gauge group. The boundary gauge enters only through the admissibility rule.

### 2.4 The block coefficient and the criterion

Fix a shape Q_0 and the family A of all its images under translations and the hyperoctahedral group B_4 of Z^4, placed on a torus whose periods are large enough that each block, its events and their plaquettes embed as in Z^4 (for the star of Section 4: all periods at least 3). For each block and each of its events choose an admissible F, compatibly with the symmetries; at an event fixed by a nontrivial symmetry of the block, average the bound (2.3) over the orbit of the chosen F (a convex combination of valid bounds is valid). Define the **block coefficient**

    alpha(Q_0; beta) = |B(Q_0)|^(-1) sum_(j in Ev(Q_0)) sum_(c in B \ F_j) K^(F_j, j)_c ,                 (2.4)

the total gauge-fixed response of one block to unit changes of all its exterior events, per link of the block.

**Criterion (BC).** `alpha(Q_0; beta) < 1`.

**General form (BC-gen).** A finite family A of link sets B_a (vertex blocks B(Q_a) or any link sets), with Ev(a) the links off B_a that share a plaquette with B_a; nonnegative numbers K^a_je (j in Ev(a), e in B_a) such that (2.3) holds with them (Remark GF' (2) supplies such numbers for any link set); weights w_e > 0 and a margin kappa > 0 with

    sum_(a : e in B_a) sum_(j in Ev(a)) w_j K^a_je  <=  (n_e - kappa) w_e   for every link e,   n_e = #{a : e in B_a}.   (BC-gen)

**Lemma SYM (PROVED).** For the family generated by Q_0, with the symmetric choices above and w = 1, every link has the same n_e = n, and the left side of (BC-gen) equals n alpha(Q_0; beta) at every link. So (BC) is (BC-gen) with kappa = n (1 - alpha).

*Proof.* The left side at e and the number n_e are sums over the blocks that contain e, a configuration of bounded size around e. Any two links are related by an isometry of Z^4 that carries this local configuration, with its chosen F's (or orbit averages), onto the other. So both are constant in e. Summing the left side over all links counts every (block, event, link) triple once: the total is `|A| |B(Q_0)| alpha`. Summing n_e gives `|A| |B(Q_0)|`. Divide. QED

**What the criterion is and is not (ARGUED).** (BC) is a condition on one finite block: a finite sum of explicit walk sums at a given beta. It is uniform in the exterior, in the centre signs and in the torus. It measures responses modulo the internal gauge group. It is not the pair-angle criterion PA_g of `library/gap-crux-exercise-astra.md` lines 1328-1333 (READ), which bounds an L^2 pair norm by 1/160 and fails at every block size for 1/16 <= beta <= 64 (rows 763 to 779, READ, checked): (BC) tolerates order-one local responses at the block boundary and asks only that their sum, averaged over the positions of a link inside the blocks, stay below the number of blocks that contain it. Section 4 verifies (BC) at beta = 1/4, inside the range where PA_g fails. It is the chord, gauge-fixed analogue of the weighted hypothesis (W) of row 691 (READ `library/gap-ds-gauge.md` lines 83-89), with vertex blocks in place of cubes of links.

## 3. The reduction: the block condition gives contraction, gap, decay and comparison

Write `Gamma_a = Gamma_(B_a)`, `P = |A|^(-1) sum_a Gamma_a` (the averaged block heat bath, self-adjoint in L^2(mu)), `delta(g)` for the column vector of the seminorms delta_e(g), and `Delta_w(g) = sum_e w_e delta_e(g)`. Let `K_je = sum_a K^a_je` and N = diag(n_e).

**Theorem R (PROVED).** Assume (BC-gen) with margin kappa > 0, on a torus with all periods at least 3. Then:

(a) *Contraction.* For every g in Lip, `delta(P g) <= |A|^(-1) M delta(g)` entrywise with `M = |A| I - N + K`, and `Delta_w(P g) <= (1 - kappa/|A|) Delta_w(g)`.

(b) *Block gap.* For every f in L^2(mu), `sum_a mu(Var_(B_a) f) >= kappa Var_mu(f)`. Here `Var_(B_a) f` is the variance of f under gamma_(B_a)(. | exterior).

(c) *Langevin gap.* If every block law gamma_(B_a)(. | y) has Poincare constant at least c_* for every exterior y, then for every smooth f
`mu(|grad f|^2) >= (kappa c_* / n_max) Var_mu(f)`, n_max = max_e n_e. This holds for all f, so in particular the gauge-invariant Langevin gap gamma_inv(beta, Lambda) of the lane (the infimum of `mu(|grad f|^2)/Var f` over smooth invariant f, unit round metric; READ `library/gap-mixed-opus.md` lines 7 and 30) is at least `kappa c_*/n_max`.

(d) *Comparison.* Let mu~ be a probability measure on SU(2)^E with `mu~(Gamma_a g) = mu~(g)` for every bounded measurable g and every a outside a set A_D of blocks. Then for every f in Lip,
`|mu~(f) - mu(f)| <= 2 sum_(a in A_D) sum_(e in B_a) [ (N - K)^(-1) delta(f) ]_e`, the inverse being a convergent nonnegative series.

(e) *Decay.* Under the hypotheses of Lemma SYM (all n_e = n, w = 1, column sums of K equal to n alpha with alpha < 1), suppose K_je > 0 only when j and e lie within distance r in some distance on links. Let f be in Lip and g bounded measurable, depending on the links of a set Y. Let m_0 be the least m such that a chain of m steps of length at most r joins the support of delta(f) to the union of the blocks that meet Y. Then
`|Cov_mu(f, g)| <= (6 / (1 - alpha)) sup|g| Delta(f) alpha^(m_0)`.
The constants do not depend on the torus.

*Proof.* (a) The bounds (2.3) hold for each block by the hypothesis of (BC-gen) (Lemma GF supplies them for vertex blocks). Average over a: for j in B_a the contribution is 0, for j in Ev(a) it is at most `delta_j(g) + sum_e K^a_je delta_e(g)`, otherwise at most delta_j(g). So `|A| delta_j(Pg) <= (|A| - n_j) delta_j(g) + sum_e K_je delta_e(g)`, which is the matrix bound. Multiply by w_j and sum over j; (BC-gen) bounds the coefficient of delta_e(g) by `|A| - n_e + n_e - kappa`, times w_e.

(b) This is Lemma W (b) (READ `library/gap-mixed-opus.md` lines 56-58; check item 2) with blocks in place of sites. For centred f in Lip, (a) and the chord diameter 2 give `sup |P^t f| <= osc(P^t f) <= 2 sum_e delta_e(P^t f) <= (2/min w) (1 - kappa/|A|)^t Delta_w(f)`. Hence `<f, P^(2t) f> <= ||f||_1 sup|P^(2t) f|` decays like `(1 - kappa/|A|)^(2t)`, so the spectral measure of the self-adjoint operator P at f gives no mass to `|s| > 1 - kappa/|A|`. Lip is dense in L^2(mu) (polynomials in the matrix entries are Lipschitz, Stone-Weierstrass), so P restricted to the centred subspace has spectrum in `[-1 + kappa/|A|, 1 - kappa/|A|]`. Then `sum_a mu(Var_(B_a) f) = |A| <f, (I - P) f> >= kappa Var f`, because Gamma_a is the conditional expectation onto the functions of the links off B_a.

(c) `sum_a mu(|grad_(B_a) f|^2) = sum_e n_e mu(|grad_e f|^2) <= n_max mu(|grad f|^2)`. Conditionally on the exterior of B_a, the block Poincare inequality gives `gamma_(B_a)(|grad_(B_a) f|^2) >= c_* Var_(B_a) f`. Integrate, sum over a and use (b).

(d) By (a), `osc(P^T f) -> 0` and `mu(P^T f) = mu(f)`, so `P^T f -> mu(f)` uniformly, and `mu~(f) - mu(f) = sum_(t >= 0) mu~(P^t f - P^(t+1) f)`. For a not in A_D, `mu~(Gamma_a h) = mu~(h)`; for a in A_D, `|mu~(h - Gamma_a h)| <= osc_(B_a)(h) <= 2 sum_(e in B_a) delta_e(h)`. So each term is at most `(2/|A|) sum_(a in A_D) sum_(e in B_a) delta_e(P^t f)`, and `delta(P^t f) <= (M/|A|)^t delta(f)` entrywise (all entries are nonnegative). With `u = N w`, (BC-gen) gives `u^T (M/|A|) <= (1 - kappa/|A|) u^T` and `u^T N^(-1) K <= (1 - kappa/n_max) u^T`, so both Neumann series converge and `sum_t (M/|A|)^t = |A| (N - K)^(-1)`.

(e) Take `G = 1 + g/(2 sup|g|)`, so `1/2 <= G <= 3/2`, and `mu~ = G mu / mu(G)`. Since G depends only on the links of Y, mu~ has the block kernels of mu at every block that does not meet Y (Bayes). Then `mu~(f) - mu(f) = Cov_mu(f, g) / (2 sup|g| mu(G))`. In (d), `(N - K)^(-1) = n^(-1) sum_(m >= 0) (K/n)^m`. A nonzero entry of (K/n)^m from e to e' needs a chain of m steps of length at most r. Each link lies in at most n blocks, and the column sums of (K/n)^m are at most alpha^m. So the bound of (d) is at most `2 n n^(-1) sum_(m >= m_0) alpha^m Delta(f) = 2 alpha^(m_0) Delta(f)/(1 - alpha)`. Multiply by `2 sup|g| mu(G) <= 3 sup|g|`. QED

**Theorem R' (PROVED; the quotient form, the most general gauge-invariant version).** Let `d_w(U, U') = min over gauge transformations h of sum_e w_e |U_e - (h.U')_e|`, a continuous gauge-invariant pseudometric. Suppose that for every link j and all U, U' differing only at j,

    sum_a W_(d_w)( Gamma_a(U, .), Gamma_a(U', .) ) <= (|A| - kappa) w_j |U_j - U'_j| ,              (QBC)

where Gamma_a(U, .) is the law after resampling B_a from U and W_(d_w) is the Wasserstein distance for d_w. Then (b) and (c) hold for every gauge-invariant f, in particular for the gauge-invariant Langevin gap.

*Proof.* For f in Lip_inv, `|f(U) - f(U')| <= L d_w(U, U')` with `L = max_e delta_e(f)/w_e`: apply the coordinate bounds to U and h.U' and use invariance. P commutes with gauge transformations (Lemma G (iv)), so Pf is invariant. Join U to h*.U', with h* optimal, by single-link changes along which the weighted distances add up to d_w(U, U'). For each step, couple P(z_i, .) and P(z_(i+1), .) as the mixture over a of near-optimal couplings; (QBC) bounds the step by `L (1 - kappa/|A|) w_(e_i) |dz_i|`. Summing gives `Lip_(d_w)(Pf) <= (1 - kappa/|A|) Lip_(d_w)(f)`. The spectral step of (b) runs in the closed invariant subspace, where invariant Lipschitz functions are dense (average a Lipschitz approximant over the compact gauge group; gauge maps are isometries). (c) follows as before. QED

The families of Sections 4 to 6 verify the stronger (BC-gen); by Kantorovich duality for the weighted l^1 chord metric, (GF) also gives (QBC) with the same margin, because d_w is at most the l^1 distance. Theorem R' is recorded because it is the natural gauge-invariant form; none of the theorems below needs it.

**Relation to the earlier block criteria (ARGUED, from READ statements).** Theorem W of row 691 (`library/gap-ds-gauge.md` lines 91-99) proves weak mixing, uniqueness and covariance decay from (W), a Hamming (total variation) condition on cubes of links, for every compact fibre, with no use of the group; whether (W) holds for Wilson SU(2) beyond the single-link regime is OPEN there (line 212). Theorem R is the chord analogue for vertex blocks, and adds the spectral consequences (b), (c). Its gauge input is Lemma F: the coupling inside a block is built in the gauge-fixed section, so gauge directions cost nothing. Section 4 verifies it beyond every single-link range in the lane.

## 4. The star block: the coefficient is below 1 for beta < (sqrt 37 - 5)/3

Take Q_0 = {v}. The block B_v = B({v}) is the star of the 8 links at v. Write D = {+-e_1, ..., +-e_4}, l_c for the link between v and v + c, and U_c for its variable oriented away from v (the link variable or its conjugate; both are chord isometries of each other). The gauge rotation at v acts by `U_c -> eta U_c` for all c.

**Lemma STAR (PROVED, geometry at periods at least 3).** (i) Two star links l_c, l_d share a plaquette if and only if c and d are perpendicular, and then exactly one, the corner plaquette `p_cd = (v, v+c, v+c+d, v+d)`. The 24 corner plaquettes are the only plaquettes that meet B_v. (ii) Each corner plaquette has two far links, `(v+c, v+c+d)` and `(v+d, v+d+c)`. They do not touch v. The 48 far links are distinct, and Ev({v}) is the set of the 48 far links. Each far link lies in exactly one corner plaquette of the star. (iii) A link j = (u, u+f) is a far link of exactly 12 stars, those at `u - c` and `u + f - c` with c perpendicular to f, and it lies in exactly 2 stars, those at u and u + f. (iv) The plaquette term of p_cd is `<U_c T_cd, U_d>`, with T_cd the product of its two far links (in order).

*Proof.* (i) The two links of a plaquette at a common vertex are perpendicular, so every plaquette through l_c contains a second star link l_d with d perpendicular to c, and is p_cd. (ii) The endpoints v+c and v+c+d differ from v because c + d has two nonzero coordinates equal to +-1, nonzero modulo periods at least 2. If (v+c, v+c+d) were also (v+c', v+c'+d') for another pair, then either c = c' and d = d', or `c = c' - d` with c' perpendicular to d, and c' - d has two nonzero coordinates, which is not a unit vector modulo periods at least 3. The same computation shows that a far link determines its corner plaquette. (iii) Solve `(u, u+f) = (v+c, v+c+d)` up to orientation: v = u - c with d = f, or v = u + f - c with d = -f, c perpendicular to f in both. The 12 vertices are distinct and differ from u, u + f at periods at least 3. (iv) Go round p_cd from v: `U_p = U_c T_cd conj(U_d)` and `Re U_p = <U_c T_cd, U_d>` (READ `library/gap-arealaw-opus.md` lines 65-69 for the identity `Re(a conj(b)) = <a, b>`). QED

**Theorem ST (PROVED).** Let Lambda be a periodic four-torus with all periods at least 3, with any centre signs. Put x = beta/4,

    S(x) = (1 + x) / (1 - 4x - 6x^2),      alpha_*(beta) = 6 x S(x) = (3 beta/2)(1 + beta/4) / (1 - beta - 3 beta^2/8),
    beta_* = (sqrt 37 - 5)/3 = 0.36092... .

For `0 <= beta < beta_*` one has `alpha_*(beta) < 1`, and the star family satisfies (BC-gen) with w = 1, n = 2 and kappa = 2(1 - alpha_*). Hence, uniformly in the torus:

(i) `sum_v mu(Var_(star v) f) >= 2 (1 - alpha_*) Var_mu f` for every f in L^2(mu);

(ii) `mu(|grad f|^2) >= 3 (1 - 3 beta/2)(1 - alpha_*) Var_mu f` for every smooth f; in particular the gauge-invariant Langevin gap is at least `3 (1 - 3 beta/2)(1 - alpha_*(beta)) > 0`;

(iii) for f in Lip and g bounded measurable depending on the links of Y, `|Cov_mu(f, g)| <= 6 sup|g| Delta(f) alpha_*^(m_0) / (1 - alpha_*)`, where m_0 is at least two thirds of the periodic l^infinity distance between the midpoints of the links in the support of delta(f) and the midpoints of the links of the stars that meet Y.

*Proof.* Step 1 (the fixing set). Let j be a far link of the star at v, lying in p_cd and touching v + c. Take `F_j = {l_c}`. Its only component is {v, v+c}, with one outer vertex, so F_j is admissible. This choice is equivariant under the symmetries of the star, and the stabilizer of (v, j) fixes l_c.

Step 2 (the walk sum). The free links are l_e, e in D \ {c}. By Lemma STAR, `n(l_e, j) = 1` for e = d and 0 otherwise, so `b = x 1_d`. Two free links interact exactly when their directions are perpendicular, with n = 1. The interaction graph Gamma_7 is the octahedral graph K_{2,2,2,2} minus the vertex c: the vertex -c is joined to the six directions perpendicular to c, and these six form an octahedron (each joined to four). The largest row sum of C^F is 6x, below 1 for beta < 2/3. With A the adjacency matrix of Gamma_7,
`sum_e K^(F,j)_e = x sum_(m >= 0) x^m (A^m 1)_d`, by the symmetry of A. Put `s_m = (A^m 1)_d` (d in the octahedron) and `t_m = (A^m 1)_(-c)`. Then `s_0 = t_0 = 1`, `s_(m+1) = 4 s_m + t_m`, `t_(m+1) = 6 s_m`. The generating functions satisfy `Sg = 1 + x (4 Sg + Tg)` and `Tg = 1 + 6 x Sg`, so `Sg = (1 + x)/(1 - 4x - 6x^2) = S(x)`, for `4x + 6x^2 < 1` (the series has nonnegative terms and its radius is the root `(sqrt 10 - 2)/6 = 0.1937...` of the denominator, above x = 0.0903 at beta_*). So each event has total response x S(x).

Step 3 (the coefficient). All 48 events of a star are equivalent under its symmetries. By (2.4), `alpha(star; beta) = 48 x S(x)/8 = 6 x S(x) = alpha_*(beta)`. Lemma SYM applies with n = 2 (Lemma STAR (iii)): the column sums of K are `2 alpha_*` at every link.

Step 4 (the threshold). For x below the radius, `6x S(x) < 1` if and only if `6x(1 + x) < 1 - 4x - 6x^2`, that is `12 x^2 + 10 x - 1 < 0`, that is `x < (sqrt 37 - 5)/12`, that is `beta < beta_*`. Check: at x = (sqrt 37 - 5)/12, `12 x^2 = (62 - 10 sqrt 37)/12` and `10 x - 1 = (10 sqrt 37 - 62)/12`.

Step 5 (the block Poincare constant). Under gamma_(B_v)(. | y), the conditional law of one star link given the other seven is von Mises-Fisher (its density is the exponential of a linear function of U_c). Lemma D1 gives Poincare constant at least 3 for each. Changing l_d moves the field of l_c by at most `beta |U_d - U'_d|` when c and d are perpendicular, and not at all otherwise; Corollary V1 gives influences at most x on the 6-regular graph K_{2,2,2,2}, row sums 6x = 3 beta/2. Lemma W (b)-(c) (READ, checked) gives `c_* >= 3 (1 - 3 beta/2)` for beta < 2/3, for every exterior.

Step 6 (conclusions). Theorem R (b) with kappa = 2(1 - alpha_*) gives (i). Theorem R (c) with n_max = 2 gives `kappa c_*/2 = 3 (1 - 3beta/2)(1 - alpha_*)`, which is (ii). For (iii), K_je > 0 requires j to be a far link of a star that contains e; far links of the star at v have midpoints within l^infinity distance 1 of v, star links within 1/2, so r = 3/2 in Theorem R (e). QED

**Values (PROVED arithmetic).** alpha_*(1/4) = 0.5484..., gap bound 0.847...; alpha_*(0.3) = 0.7261..., gap bound 0.452...; alpha_*(0.35) = 0.9452..., gap bound 0.0781...; alpha_* = 1 at beta_*.

**Comparison of ranges (uniform gaps for 4D Wilson SU(2) on periodic tori).**

| method | range in beta = beta_W | status |
|---|---|---|
| single-link chord Dobrushin, full lattice | beta < 2/9 = 0.2222 | READ `library/gap-vmf-lip.md`, checked (row 790) |
| Route C: D1, (C4), pointwise mixed Hessian | beta < 11/48 = 0.2292, periods at least 4 plus exceptions | READ `library/gap-shape-exercise-astra.md` (C6), checked (row 824) |
| axial forest slice (Theorem A, row 818) | beta < 1/4 | READ, checked (row 829) |
| perfect-code slice (Theorem B, row 818) | beta < 8/27 = 0.2963 (0.2996 with optimal weights), periods in 82 Z | READ, checked (row 829) |
| any global forest with single-link chord Dobrushin | fails for every beta >= 1/3 | READ (ceiling), checked with corrections (row 829) |
| unrefereed claims (Bhattacharjee-Bhattacharya-Lockwood, Hexagon 2610.00341 v4/v7, as read by row 819) | 1/3 (forest gauge, 12 partners), 0.345 (v4) and 0.348 (v7) (Dobrushin-Shlosman blocks of three links in forest gauge, ten outside partners), free-boundary infinite-volume state | READ `library/gap-novelty-opus.md` lines 351-363; the preprint was not read here |
| unrefereed conditional claim (Mihajlovic, three-link functional) | 0.354 | READ `library/gap-arealaw-opus.md` lines 474-476 |
| **star blocks, Theorem ST** | **beta < (sqrt 37 - 5)/3 = 0.3609, all periods at least 3, all flux sectors** | **PROVED here** |
| larger vertex blocks (Section 6.1) | up to about 0.42 | GUIDE only |

**Why stars beat the forest ceiling (ARGUED).** The ceiling of row 818 concerns one global slice: every forest leaves each non-forest link with more than 12 moving neighbours on average, and the price beta/4 per neighbour is attained. In the star scheme the gauge fixing depends on the event: for the far link j in p_cd the fixed link is l_c, so the event moves one free link, and the response spreads only through the 7-site star graph (spectral radius (2 + sqrt 10)x = 5.16x) instead of the bulk. A link is a far link of 12 stars and lies in 2, which makes 6 events per kill against 18 for single links and 12 for the best slices. The extra gauge input is exact (Lemma F with the rotation at v), not a quadratic reserve.

**Scope (PROVED statements only).** Theorem ST is a strong-coupling theorem. It holds for every centre-sign configuration, so for all twisted measures. Tori with a period equal to 2 are not covered (stars then have coinciding far links); Theorem A of row 818 covers them below 1/4 when some period is at least 3. Nothing here concerns beta of order one.

## 5. The seed of the skeleton and a lattice gap for beta < beta_*

The seed of `library/gap-skeleton-final.md` (13.8, line 399, with Theorem SH of 13.11-13.12, READ) is a bound on the thermal sum `S(a; (2a)^3; beta)` of the transfer operator. Theorem DOB (READ `library/gap-vmf-lip.md` lines 438-560, checked by row 790) derives it from a comparison of plaquette means of the tori with time extents a and 2a. Here the comparison comes from Theorem R (d) for stars.

Notation as there: `abar_(t,B)(s)` is the mean of 1 - x_p over the plaquettes of the periodic torus with time extent t and spatial box B at coupling s; `Phi_B(a; beta) = 2 F(a, B; beta) - F(2a, B; beta)` with F = log Z.

**Lemma M* (PROVED; the star version of Lemma M of `library/gap-mid-max.md` Section 8, reused in `library/gap-vmf-lip.md` lines 468-474).** Let mu_long be the Wilson law on the torus (2a, B), and mu~ the law on the torus (a, B) of its links with time coordinate in [0, a-1] (spatial links at times 0, ..., a-1 and time links starting there), times read modulo a. Then `mu~(Gamma_v g) = mu~(g)` for every bounded measurable g and every star v of (a, B) at a time t in [1, a-2].

*Proof.* At such t the star, its 24 corner plaquettes and its 48 far links use spatial links at times t-1, t, t+1 and time links starting at t-1 or t <= a-2. None of them uses the wrap from a-1 to 0, so they are the same links and plaquettes in both tori. In the long torus the conditional law of the star given all other links is the Gibbs star kernel, a function of the 48 far links (Lemma G (i)). These far links are folded variables. So the same kernel is also the conditional law given the folded variables only (tower property), and in the torus (a, B) it is the Gibbs star kernel at v. QED

**Corollary SEED (PROVED, given the READ chain of Theorem DOB).** Let `0 < beta < beta_*`, `alpha = alpha_*(beta)`, `a >= 3` an integer, `j = floor(a/2)`, `m_0 = max(0, ceil((2j - 3)/3))`, and B a periodic spatial box with all sides at least 3. For every `0 <= s <= beta`,

    | abar_(2a,B)(s) - abar_(a,B)(s) |  <=  8 alpha^(m_0) / (1 - alpha),                        (17*)
    0 <= Phi_B(a; beta)  <=  96 a |B| beta alpha^(m_0) / (1 - alpha).                          (18*)

If `768 a^4 beta alpha^(m_0) / (1 - alpha) <= 3/5000`, then `S(a; (2a)^3; beta) < 1/1650`, and `m(L^3; beta) >= 3/(50 a)` for every integer `L >= 64 a`. For each fixed beta in (0, beta_*) such an a exists.

*Proof.* Comparison. Apply Theorem R (d) on the torus (a, B), at coupling s, with mu = mu_(a,B;s), mu~ as in Lemma M*, and A_D the stars at times 0 and a - 1. Since alpha_* increases in beta, alpha_*(s) <= alpha. As in Theorem R (e), with n = 2 and each link in at most 2 stars of A_D, the bound is at most `2 alpha^(m) Delta(f)/(1 - alpha)`, where m is the least number of K-steps from the support of delta(f) to the links of the stars in A_D. Distances. Give a spatial link at time t the position t and a time link starting at t the position t + 1/2, on the circle R/aZ. A K-step joins a far link of a star at time t (positions in [t-1, t+1]) to a link of that star (positions in [t - 1/2, t + 1/2]), so it moves the position by at most 3/2. The links of the stars at times 0 and a - 1 have positions in {a - 3/2, a - 1, a - 1/2, 0, 1/2}. Take as in Theorem DOB the 3|B| spatial plaquettes at time j and the 3|B| time plaquettes of the slab [j-1, j]; their links have positions in [j-1, j], and their images in the long torus do not cross the cut. The circular distance is at least `min(j - 3/2, a - 3/2 - j) = j - 3/2`, since a >= 2j. So m >= m_0. Each x_p has Delta(x_p) <= 4. Translation invariance makes the average over these plaquettes equal to the plaquette mean in each torus (READ `library/gap-vmf-lip.md` lines 501-502). This proves (17*).
From the comparison to the seed. The identities `dF(t, B; s)/ds = -6 t |B| abar_(t,B)(s)`, `Phi_B(a; beta) = 12 a |B| integral_0^beta (abar_(2a,B) - abar_(a,B)) ds` and `S(a; B) <= e^(Phi_B) - 1` are READ (`library/gap-vmf-lip.md` lines 506-520). Substituting (17*) gives (18*). For B = (2a)^3, |B| = 8 a^3 and the coefficient is 768. The arithmetic from the displayed condition to `S < 1/1650` and to the gap through the corrected Theorem SH is READ unchanged (lines 521-594): only the factor `q^(floor(a/2) - 1)/(1 - q)` of (19) is replaced by `alpha^(m_0)/(1 - alpha)`. Existence: `m_0 >= (a - 4)/3`, so the left side is at most `768 a^4 beta alpha^((a-4)/3)/(1 - alpha)`, which tends to 0 as a grows. QED

**Remarks.** (1) The bound covers the full excited sum, both halves of the seed (READ `library/gap-vmf-lip.md` lines 538-547). (2) The sizes are large: at beta = 0.3 the displayed condition first holds near a = 360 (PROVED arithmetic: `4 ln a + ((a - 4)/3) ln alpha` with alpha = 0.7261 crosses `ln(6e-4 (1 - alpha)/(768 beta))` near there). This is a strong-coupling seed. (3) Previous checked range of the seed: beta < 2/9 (Theorem DOB, chord form). Theorem ST moves it to beta < 0.3609. Row 835 attacks the seed by slab independence in a separate lane; this corollary is a by-product of the block criterion and was not coordinated with it.

## 6. Larger blocks, the ceiling of the method, and what blocks order one

### 6.1 Larger vertex blocks (GUIDE)

A script (`lane836/guide/blockwalk.py`, `blockwalk2.py`, `blockwalk3.py`, `blockwalk4.py`; numpy; under 30 MB; seconds to minutes) evaluates (2.4) for vertex blocks in Z^4: for each event it takes the best admissible F (exhaustive for at most 4 vertices; for larger Q only F = a breadth-first spanning tree of Q plus one outward link, so those values are lower bounds for the method on that shape), solves (I - C^F)^(-1) b, and bisects for the beta where alpha(Q_0; beta) = 1.

| Q_0 (vertices) | links | events | crossing beta |
|---|---|---|---|
| star (1) | 8 | 48 | 0.36092 (equals (sqrt 37 - 5)/3) |
| pair (2) | 15 | 78 | 0.38421 |
| line of 3 / L-shape (3) | 22 | 108 / 104 | 0.39342 / 0.39255 |
| unit square (4) | 28 | 124 | 0.40410 |
| line of 4 / 5 | 29 / 36 | 138 / 168 | 0.39825 / 0.40123 (heuristic F for 5) |
| 3x2 / 4x2 rectangles | 41 / 54 | 170 / 216 | 0.41175 / 0.41519 (heuristic F) |
| 3x3 / 4x4 squares | 60 / 104 | 232 / 372 | 0.41789 / 0.42143 (heuristic F) |
| unit 3-cube (8) / 3x3x2 box (18) | 52 / 111 | 192 / 350 | 0.41174 / 0.40957 (heuristic F) |
| unit 4-cube (16) | 96 | 288 | 0.39448 (heuristic F) |

**Reading (GUIDE, decides nothing).** The crossing rises from 0.361 to about 0.42 for flat blocks and falls for thick four-dimensional blocks. This fits the mechanism of 6.2: thick blocks bring back the bulk propagation of a gauge slice. A hand proof for any row would follow Theorem ST step by step (finite symmetric walk sums); none is given here, so only the star row is a theorem. A further script (`lane836/guide/starcheck.py`) reproduces the walk sum S(x) of Theorem ST at three values of x, the spectral radius 2 + sqrt 10 of Gamma_7, and the Gaussian star potentials and the l^1 value 1/3 of 6.5 (c); these hand results do not rest on it.

### 6.2 The ceiling of the method (PROVED)

**Proposition CEIL.** Let Q be any finite vertex set and F any admissible fixing set. Some vertex of Q carries at least 7 free links, and the matrix C^F of (2.2) has spectral radius at least `(2 + sqrt 10) x`. Hence for `beta >= (2/3)(sqrt 10 - 2) = 0.7749...` the hypothesis of Lemma GF, in either form of Remark GF' (1), fails for every vertex block and every admissible gauge fixing: the method of Sections 2 to 4 gives no bound there, whatever the block.

*Proof.* A component of F with k vertices of Q has k links if its root is outer (degree sum over Q equal to 2k - 1) and k - 1 links otherwise (sum 2k - 2). So the sum over Q of the F-degrees is at most 2|Q| - 1, and some vertex v of Q has F-degree at most 1. At least 7 of the 8 links at v are free. Two free links at v in perpendicular directions share their corner plaquette, so C^F has an entry at least x between them. The induced graph on the free links at v contains Gamma_7 (Section 4, Step 2), whose adjacency spectral radius is 2 + sqrt 10 (Perron vector (x_0, y) on (-c, octahedron) with `lambda x_0 = 6 y`, `lambda y = x_0 + 4y`). A principal submatrix of a nonnegative matrix has no larger spectral radius. So the spectral radius of C^F is at least `(2 + sqrt 10) x`, which is at least 1 exactly when `beta >= 4/(2 + sqrt 10) = (2/3)(sqrt 10 - 2)`; then neither form of the hypothesis holds. QED

**ARGUED.** The price x per shared plaquette is the worst case of Corollary V1, attained at zero field (READ `library/gap-mixed-opus.md` lines 146-148, the slice version of `library/gap-gamma2-astra.md` 5.2; check row 829 item 5). In the star every free link has its six staples adjustable through free or exterior links, so zero fields occur there and the entries of C^F are sharp worst-case influences. So the ceiling belongs to worst-case single-site responses inside gauge-fixed blocks, not to the counting.

### 6.3 The row 832 guide (coordinator message, GUIDE only)

The coordinator reported (2026-11-12): on a 2^4 block of 32 links with a typical Wilson exterior, the debiased linear-response row sum over the 160 boundary links, with the best single interior plaquette as observable, per unit chord change, is 0.21 at beta 0.5, 0.72 at beta 1.0 and about 2.3-2.7 at beta 2.0 (noise floor about 1.0 there); the same estimator on non-invariant block-link coordinates gives 1.24, 2.2 and 4.0-5.2.

**Reading (ARGUED; the run decides nothing).** (1) That quantity is a typical-exterior, one-observable proxy for a row of a response matrix of a link block (the internal links of a vertex 2-cube), not the worst-case coefficient (2.4). A single 1-Lipschitz observable gives a lower bound on the chord response at that exterior, up to its Lipschitz normalization. (2) At beta 0.5, Theorem ST's worst-case coefficient is alpha_*(0.5) = 2.08 > 1, while the typical gauge-invariant proxy is 0.21: a factor of about 10 separates worst case from typical there. (3) At beta 2 even the typical gauge-invariant proxy of this block is above 1 (if the noise floor allows that reading). So at order one two things must change at once: the worst-case quantifier and the block size.

### 6.4 The four suggested tools

- **D1** (READ, checked) enters only the block Poincare constant c_* (3 in place of the checked 2 of `library/gap-gamma2-astra.md` (10)). It raises the gap bound of Theorem ST (ii) by 3/2 and does not move beta_*.
- **The gauge reserve (C4)** (READ, checked) is not used. Its source, the gauge identity at a vertex ((C2) there), enters here in exact form: the rotation at v is a symmetry of the block law and Lemma F removes it. (C4) is a pointwise bound on mixed Hessians of invariant functions, which serves Bochner routes. It gives no chord response bound, and Proposition CEIL holds whatever reserve is added to the Langevin side.
- **Forest gauge fixing** is Lemma F: Lemma S of row 818 inside a block with outer vertices as roots. The gain over the global slices comes from choosing F per event (Section 4).
- **Slab independence.** **Proposition SL (PROVED).** Take as blocks the slabs: for a direction nu and a layer k, all nu-links from layer k to layer k + 1. By Lemma S of row 825 (READ, checked) the block law is the layer law, a three-dimensional model on S^3 with one bond per plaquette of type (rho, nu). Remark GF' (2), Lemma GF with F empty (there is no internal gauge symmetry: every gauge rotation at a layer vertex also moves horizontal links), gives for each event, a horizontal link in one bond, the total response `2x/(1 - 6x)` (two sites change field; the layer graph is the 6-regular cubic lattice, periods at least 3). Each slab has 6 events per link and each link lies in one slab. So the coefficient is `12x/(1 - 6x)`, below 1 exactly for beta < 2/9: slabs reproduce the single-link range. (ARGUED: a bound of one site per bond change would give beta < 1/3; no such bound is proved.) Slab independence drives the area law to 2/3 in row 825 because there only the slab's own mixing matters (row sum 6x); a block criterion also pays every horizontal link at the slab's boundary.

### 6.5 What blocks order one (beta about 2)

**PROVED.** (a) Through Lemma GF, (BC) cannot be verified for any vertex block at beta >= 0.775 (Proposition CEIL); at beta = 2 the worst-case internal propagation is at least `(2 + sqrt 10)/2 = 2.58` per step. (b) Every event moves at least one free link: by the proof of Lemma G (iii), the block links of a plaquette of P_j form a path that joins two outer vertices (u and w' when only w is in Q, u and u' when w and w' are in Q), so an admissible F cannot contain all of them. So `alpha(Q_0; beta) >= x |Ev(Q_0)| / |B(Q_0)|` for the method; at beta = 2 this is `|Ev|/(2|B|)`, above 1 for every block in the table of 6.1.

**ARGUED.** (c) The worst case is a real obstruction, not only a limit of the bound. At large beta and at the block scale, an SU(2) block law with a smooth exterior is close to three copies of a Gaussian (abelian) block law. For the star, the Gaussian response to a unit change of one corner staple is the harmonic response on K_{2,2,2,2}: the Laplacian 6 - A has eigenvalues 8 on the antipodally even part and 6 on the odd part, and the response to the edge current between a and b, normalized by the best common rotation, has l^1 norm 1/3 (computed by hand: the potentials are -7/48, 7/48, 1/48, -1/48 at a, b, -a, -b and 0 elsewhere). So the optimal star coefficient tends to `48 (1/3)/8 = 2 > 1` at weak coupling, for SU(2) as for U(1). No fixed small block can satisfy the criterion at weak coupling; only blocks larger than the correlation length can, and only if the gauge-invariant response decays inside them uniformly in the exterior. (d) That decay, uniform in the exterior, is a strong-mixing statement at order one. It is the crux in finite form, as (W) was in row 691 (`library/gap-ds-gauge.md` lines 163-172). By Theorem R (e), (BC) with coefficient alpha and step range r gives invariant correlations decaying at rate at least `log(1/alpha)/r`; so with correlation length xi, `r >= xi log(1/alpha)` (PROVED from (e)): a coefficient well below 1 needs blocks of range at least of order xi.

**OPEN (the exact missing statement).** (BC-ord1): for one shape Q_0 and one compact beta interval inside [1.5, 2.5], a bound below 1 on the coefficient (2.4) with response bounds that are not single-site, for example the optimal gauge-quotient couplings of Theorem R', uniform in the exterior. Weaker useful forms: the same with the supremum over exteriors replaced by an average under the Wilson law of the exterior, together with a theorem that converts annealed block smallness into Theorem R's conclusions; the literature read in row 821 (`library/prior/gap-lit-dp.md`) gives such conversions only for quenched, independent environments.

## 7. Binding test: periodic Villain U(1) in its Coulomb phase

The model (READ `library/gap-tu-retry.md` (1)-(3), lines 66-89): angles on the links of `T_M = (Z/MZ)^4`, weight `prod_p phi_beta((d_1 theta)_p)` with the positive Villain function phi_beta, metric dtheta^2, and gamma_V(beta; M) the Poincare gap of the Langevin generator on gauge-invariant functions. Theorem V there (READ line 92; checked by row 794): at every fixed beta >= 2^14, gamma_V(beta; M) -> 0 as M -> infinity.

**Theorem U (PROVED).** Fix beta >= 2^14. Let Q_0 be any finite vertex shape (or any finite link-block shape) and take the family it generates on the cubic tori (Z/MZ)^4. For every kappa > 0 there is M_0 such that for M >= M_0 no choice of weights w > 0 and of numbers K^a that make (2.3) valid for the Villain block kernels (chord metric on circles) satisfies (BC-gen) with margin kappa. If the numbers are chosen by a translation-invariant local rule, as in (2.4), the coefficient does not depend on M, so it is at least 1: (BC) fails for every shape and every such rule. The same holds for the quotient form (QBC).

*Proof.* Every step of Theorem R except the hypothesis holds for this model. (a) is the hypothesis applied to block averages. (b) uses the chord diameter 2, self-adjointness of P and density of Lipschitz functions; all hold on circles. (c) needs a block Poincare constant uniform in the exterior and in M: the block density with respect to Haar on the circles of the block is a product of at most a fixed number of factors phi_beta, each bounded above and below by positive constants at fixed beta, so Holley-Stroock from the circle gap 1 gives `c_*(beta, Q_0) > 0`, independent of the exterior and of M (the argument of row 818 Section 6, READ `library/gap-mixed-opus.md` line 197, check row 829 item 7). If (BC-gen) held with margin kappa on infinitely many tori, Theorem R (c) would give `gamma_V(beta; M) >= kappa c_*/n_max > 0` along them, against the full limit gamma_V(beta; M) -> 0 of Theorem V. For a local rule the column sums are the same numbers on every torus that embeds the block configuration, so a margin on one large torus would give it on all. For (QBC) use Theorem R' in the same way. QED

**The named step.** The step that fails is the coefficient inequality (BC) itself. The gauge structure (Lemma G, abelian gauge invariance; Lemma F, tree gauge on circles: READ `library/gap-mixed-opus.md` line 197, "Step (S1) holds verbatim"), the reduction (Theorem R (a)-(c)) and the block Poincare constant all hold for U(1). For SU(2) at small beta the coefficient is small because Corollary V1 gives the price x = beta/4 per plaquette, linear in beta. For Villain at large beta the price per plaquette does not vanish as beta grows: at the exterior with all staple angles 0, the one-link law is close to a centred Gaussian of variance 1/(6 beta), and moving one staple by s moves its mean by about s/6 (ARGUED there, READ `library/gap-mixed-opus.md` line 199; row 829 corrects only that line's last sentence: beta/4 is an upper bound for Wilson SU(2), attained at suitable exteriors).

**Mechanism at the block level (ARGUED, with one PROVED model case).**

- For the star, the Gaussian computation of 6.5 (c) gives the optimal coupling cost 1/3 per unit event, so the coefficient tends to 2 > 1 at large beta. This is a scale-free (beta-independent) harmonic response, the photon at the scale of one star.
- **Proposition GFF (PROVED; standard Gaussian facts).** For the lattice Gaussian field on Z^d with energy `(1/2) sum_(x~y) (phi_x - phi_y)^2 + (m^2/2) sum_x phi_x^2`, m >= 0, and any family of finite site blocks, the exact chord (here absolute-value) responses are `K^a_yx = H_a(x, y)`, the exit distribution from B_a of the random walk killed with probability `m^2/(2d + m^2)` per step. So the column sum at x is exactly `n_x - sum_(a contains x) rho_a(x)`, with rho_a(x) the probability of killing before exit. The margin of (BC-gen) is positive if and only if m > 0, and it is exactly 0 for the massless field, for every block family.
  *Proof.* The block conditional law is Gaussian with a covariance that does not depend on the exterior and mean `H_a phi_(boundary)` (the discrete Dirichlet problem for `-Laplacian + m^2`). For two exteriors differing by 1 at y the means differ by `H_a(., y) >= 0`; the translation coupling has cost `sum_x H_a(x, y)`, and the test function `phi_x` shows that `K^a_yx >= H_a(x, y)` for any valid K. Finally `sum_(y) H_a(x, y) = 1 - rho_a(x)`. QED
  So (BC) sees the mass exactly: a massless Gaussian field is marginal for every block. Here the fibre is R, not compact, so Theorem R (b) does not apply as written; the proposition is a statement about the coefficient only.
- For the abelian gauge field the photon plays the role of the massless scalar. Theorem U says the coefficient must reach 1 for every shape; the Gaussian star value 2 and Proposition GFF show how.

**Where SU(2) enters, and what the test means (ARGUED).** Theorem ST uses SU(2) only through the S^3 constants of Corollary V1 (1/4) and D1 (3); its gauge fixing works for every compact group. For U(1) with the Wilson cosine the zero-field chord constant on the circle is `E[(x.e)^2] = 1/2` instead of 1/4, so the same proof would give the star range beta < (sqrt 37 - 5)/6 = 0.18 if the circle analogue of Corollary V1 holds with 1/2 for every field (not proved here). That is as it must be: U(1) has a gap at strong coupling. So the criterion passes the binding test in the form of `library/gap-skeleton-final.md` 13.14 (Proposition T1, READ line 537): the reduction (Theorem R) is the same for every group, and the hypothesis (BC) fails for U(1) in the Coulomb phase. The SU(2)-specific content can only enter at order one, through the coefficient of blocks larger than the correlation length, where U(1) is massless and SU(2) is expected to be massive. That large-block coefficient is (BC-ord1) of 6.5, OPEN.

## 8. Summary of statements, provenance and next steps

| statement | mark | where |
|---|---|---|
| Lemma G: vertex blocks, internal gauge invariance of block laws, every event plaquette has two block links meeting at a vertex of Q | PROVED | 2.1 |
| Lemma F: gauge-fixed disintegration of block laws, outer vertices as roots (the boundary gauge) | PROVED (the proof of Lemma S of row 818, READ and checked, adapted) | 2.2 |
| Lemma GF: the gauge-fixed response bound (GF), (2.3) | PROVED from Corollary V1 and the refined Lemma DC (READ, checked) | 2.3 |
| Criterion (BC): block coefficient alpha(Q_0; beta) < 1; general form (BC-gen); Lemma SYM | definition; Lemma SYM PROVED | 2.4 |
| Theorem R: (BC-gen) implies contraction, block gap, Langevin gap on all functions, comparison, exponential clustering, all uniform in the torus and the centre signs | PROVED | 3 |
| Theorem R': the gauge-quotient (path-coupling) form, giving the gauge-invariant gap | PROVED | 3 |
| Lemma STAR and Theorem ST: star blocks satisfy (BC) for beta < (sqrt 37 - 5)/3 = 0.3609; Langevin gap at least 3(1 - 3beta/2)(1 - alpha_*(beta)); clustering | PROVED (uses D1, READ and checked, for the constant 3) | 4 |
| Lemma M* and Corollary SEED: the seed S(a; (2a)^3) < 1/1650 and a volume-uniform lattice gap on periodic cubes for every 0 < beta < 0.3609 | PROVED, given the READ chain of Theorem DOB and Theorem SH | 5 |
| larger vertex blocks reach about 0.42; thick blocks fall back | GUIDE | 6.1 |
| Proposition CEIL: the method gives no bound for any vertex block at beta >= (2/3)(sqrt 10 - 2) = 0.775 | PROVED | 6.2 |
| Proposition SL: slab blocks (slab independence) give only beta < 2/9 | PROVED | 6.4 |
| reading of the row 832 guide; Gaussian star coefficient 2 at weak coupling; the need for blocks larger than the correlation length | ARGUED / GUIDE | 6.3, 6.5 |
| (BC-ord1), or an annealed version with a conversion theorem | OPEN | 6.5 |
| Theorem U: periodic Villain U(1) at beta >= 2^14 fails (BC) for every block shape | PROVED from Theorem V of `library/gap-tu-retry.md` (READ, checked) | 7 |
| Proposition GFF: for the massless Gaussian field the exact margin is 0 for every block family; positive iff m > 0 | PROVED | 7 |
| U(1) Wilson star range 0.18 under a circle analogue of Corollary V1 | ARGUED | 7 |

**What is new here, as far as the lane's files show (ARGUED; no outside search was run).** A `git grep` of the lane for star, vertex and plaquette blocks finds only the plans of `library/gap-zf-box-x.md` 3.3 ("Way 2", block heat bath, not carried out, READ line 167) and the reading of the unrefereed Hexagon preprint by row 819 (Dobrushin-Shlosman blocks of three links in forest gauge, 0.345-0.348, READ `library/gap-novelty-opus.md` lines 356-358). The vertex-star block with a gauge fixing chosen per boundary event, the threshold (sqrt 37 - 5)/3, and the ceiling (2/3)(sqrt 10 - 2) of the method were not found there. Before any outward use, a literature reading row on vertex-star blocks and gauge-fixed couplings in Dobrushin-Shlosman criteria for lattice gauge theories is needed (owner rule of 2026-11-12: a literature search on each new path).

**Provenance and credits.** One author, Claude Opus 5.5 at max effort, by hand in one session; this is not a check. Reused results, with their authors: Theorem V, Corollary V1, Lemma DC, Lemma INF, (AS-bg), the chord form of Theorem DOB and its seed arithmetic (`library/gap-vmf-lip.md`, Codex gpt-6-astra; checked by Claude Opus 5.5, row 790); the refined Lemma DC step ((B26) of `library/gap-block-astra.md`, Codex gpt-6-astra; checked by Claude Opus 5.5, row 808); Lemma S (forest slice), Lemma W, Theorems A and B and the ceiling 1/3 (`library/gap-mixed-opus.md`, Claude Opus 5.5; checked by Codex gpt-6-astra, row 829); Lemma D1 and (C4) (`library/gap-shape-exercise-astra.md`, Codex gpt-6-astra; checked by Claude Opus 5.5, row 824); Lemma S of row 825 (`library/gap-arealaw-opus.md`, Claude Opus 5.5; checked by Codex gpt-6-astra, row 828); Theorem V for Villain and Lemma L (`library/gap-tu-retry.md`, Codex gpt-6-astra; checked by Claude Opus 5.5, row 794); Theorem W and Proposition H (`library/gap-ds-gauge.md`, Claude Fable 5.2; checked by Claude Opus 5.5, row 693); Lemma M and the first Theorem DOB (`library/gap-mid-max.md`, Claude Fable 5.2, row 708); Theorem SH (`library/gap-seed-shape.md`, Claude Fable 5.2, row 705); the PA_g results (rows 763 to 779, Codex gpt-6-astra, checked by Claude Opus 5.5). The comparison method is Dobrushin's; the averaged block form follows the shape of the Dobrushin-Shlosman criteria (recalled through row 691, not read here); the path-coupling step of Theorem R' is the idea of Bubley and Dyer (recalled, not read). The claims of Bhattacharjee, Bhattacharya and Lockwood and of Mihajlovic are quoted only through rows 819 and 825.

**Next steps for the lead (ARGUED).** (1) A cross-provider check of Lemma F, Lemma GF, Theorem R (a)-(e), Lemma STAR, Theorem ST and Lemma M* with Corollary SEED; the points that most need it are Step 1 of Lemma GF (the disintegration with outer roots and its use for two exteriors), the walk sum of Theorem ST Step 2, the column-sum symmetry of Lemma SYM, and the distance count in Corollary SEED. (2) The literature row named above. (3) Hand proofs for the pair block (GUIDE 0.384) or the unit-square block (GUIDE 0.404) would follow Theorem ST step by step; they move only the strong-coupling range. (4) The order-one statement (BC-ord1) needs a new kind of response estimate; Proposition CEIL shows that no choice of vertex block or gauge fixing does it with worst-case single-site responses.

This note is an author proof by one model. It is not an independent check and not an audit.

RESULT: PROVED a gauge-invariant block criterion (BC) for 4D Wilson SU(2) (one vertex block, a gauge fixing inside the block chosen per boundary event, the boundary gauge handled by an admissibility rule, and a finite walk-sum coefficient alpha(Q_0; beta) < 1) and its reduction (Theorem R: contraction, block and Langevin gaps on all functions, comparison and exponential clustering, uniform in the torus and the flux sectors); PROVED alpha < 1 for star blocks for beta < (sqrt 37 - 5)/3 = 0.3609 on every torus with periods at least 3 (Langevin gap at least 3(1 - 3beta/2)(1 - alpha_*)), and with the Theorem DOB chain the seed of gap-skeleton-final and a volume-uniform lattice gap on periodic cubes there, beyond 2/9, the 1/3 forest ceiling and the unrefereed 0.348; GUIDE: larger flat blocks reach about 0.42; PROVED: this method gives no bound for any vertex block at beta >= 0.775 (Proposition CEIL) and slab blocks give only 2/9, so order one stays OPEN and needs exterior-uniform (or annealed) responses, not single-site ones, of blocks larger than the correlation length (row 832 GUIDE: typical gauge-invariant 2^4 responses still about 2.5 at beta 2); periodic Villain U(1) at beta >= 2^14 fails (BC) for every block shape at the coefficient step (PROVED from Theorem V), by its massless harmonic response (exact zero margin for the massless Gaussian field).
