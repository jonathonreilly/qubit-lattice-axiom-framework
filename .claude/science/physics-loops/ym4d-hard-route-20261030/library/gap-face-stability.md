lead: Claude Opus 5.5 lead session, row queued 2026-11-17 06:11Z
row: FINISH 1091, written by Claude Fable 5.2 medium (laptop subagent)

# gap-face-stability (FINISH 1091): a positive interval for the face

Research text, not an audit. It grants no status. It claims no Yang-Mills mass gap.
PROVED means a written hand argument in this file. Nobody has checked it yet. Nothing was formalized in Lean.

## Plan (eight steps; refined after step 1)

1. Read row 1091, rows 1077, 1078, 1084, 1086, and OpenAI's Section 3 (Theorem 3.1 and Sections 3.8 to 3.12). DONE.
2. Search the lane for prior block-Dobrushin work and for the row 1092 reading. DONE.
3. Hardest first: decide which anchor statement the face needs, and test whether OpenAI's argument can give it in a field or with pins. DONE (step 3 result).
4. Prove the abstract block criterion (Theorem FST-BD). DONE.
5. Prove the two implications to (17): from a pinned square of one sheet (FST-P), and from one unpinned sheet in a small field (FST-F). DONE.
6. Prove what a multi-point statement at zero field gives (FST-T implies FST-F), and what Theorem 3.1 gives for cumulants. DONE.
7. Write the exact failing steps and the counterexamples; check the two-dimensional mechanisms hypothesis by hypothesis. DONE.
8. Marks, limits, credits, RESULT line. DONE.

## Step 1 result: sources read and the target

Sources read in full: `library/gap-face-2d-astra.md` (row 1077, gpt-6-astra max), `library/gap-face-2d-check-opus.md` (row 1078, Claude Opus 5.5 max), `library/gap-checkerboard-singlet-astra.md` (row 1084). Row 1086's check (`library/gap-checkerboard-singlet-check-opus.md`) was read at its verdict lines for Lemma DEC, (DEC4), Theorem A and the RESULT line, not in full.

OpenAI's paper, *Sharp mass bounds for the two-dimensional O(4) model*, pin `4eaee875`: I made no new download. I read the LaTeX source that row 1078 fetched into `/tmp/opus-face2d-openai.NylL2Z/src/preliminary.tex`: lines 1-66 (Theorem 3.1 and the proof outline) and lines 833-1192 (Sections 3.8 to 3.11 in full, and the start of 3.12). Sections 3.1 to 3.7 were not re-read; rows 1077 and 1078 cover (3.4)-(3.8).

Facts from the source that this row uses:

- Theorem 3.1 is for unpinned tori (sides at least C Xi) and unpinned free subgraphs, couplings 0 <= beta_e <= beta, local Lipschitz F, G, with L_F = sup norm plus the largest one-site Lipschitz constant. The prefactor is C (1 + beta + |A| + |A'| + d)^20. It is polynomial in the support sizes.
- Section 3.10, (3.61) in the PDF numbering (`eq:pre:10-3`): for a bounded observable O on A whose average under a common left rotation is zero, |E O| <= C ||O|| |A| exp(-c d_pin / s). Pins, signed couplings and right twists are allowed there. This is the pinned statement the paper proves. It is for charged observables only.
- Section 3.11 opens with the restriction to the untwisted zero-field ferromagnet and says "This restriction is essential." The conversion to all observables uses: Newman's covariance inequality for associated variables (`eq:pre:11-1`), Ginibre's inequality for zero-field XY, the Fortuin-Kasteleyn representation for zero-field Ising, the lattice condition for the amplitude marginals, and two localizations. The localizations control conditional means in L^1 and use the sup norm of the observable.

Target (row 1078, corrected J1): the face law (1) of row 1077 obeys (17) on some interval 0 <= lambda <= eps_beta, eps_beta > 0, for every beta in [2.3, 2.6], with constants independent of both longitudinal sides, of the transverse size and of the state.

Notation. Row 1077's: K = SU(2) = S^3, transverse torus (Z/T)^2 with edge set E_T, T >= 3. D is a longitudinal torus Z/L x Z/M. A site is x = (u, e) with u in D, e in E_T. The face density is proportional to exp{ beta sum_e sum_<uv> Phi_e(u).Phi_e(v) + lambda sum_u sum_p tau_p(u) }, tau_p(u) = (1/2) tr of the plaquette word. rho is the round distance on S^3. Lip_x(f) is the Lipschitz constant of f in the coordinate x with all others fixed. osc_x(f) is the oscillation in the coordinate x.

Two elementary facts about the perturbation are used throughout.

(M1) Multilinearity. For fixed other links, tau_p is a linear function of the unit quaternion Phi_e (row 1077, Section 3.3, uses the same fact). So, given all other sheets, sheet e is a two-dimensional O(4) model in an external field: its conditional density is proportional to exp{ beta sum_<uv> Phi(u).Phi(v) + sum_u H_u.Phi(u) }, with H_u = lambda (h_p(u) + h_p'(u)), where p, p' are the two transverse squares that contain e and h_p(u) is a unit vector (the conjugate of the product of the other three links of p, in the right order). So |H_u| <= 2 lambda.

(M2) Each h_p(u) depends on the three other links of p at the same u only. Left or right multiplication by a unit quaternion is an isometry of R^4. So a change of one of these links from q to q' changes h_p(u) by |q - q'| <= rho(q, q'). For T >= 3 two distinct transverse edges lie in at most one common square, and every edge e has exactly six such neighbours e' (three in each of its two squares). I write e ~ e'.

## Step 2 result: lane search and the row 1092 reading

- `library/prior/gap-face-stability-read-luna.md` (row 1092): absent after `git pull --ff-only` at the start, before step 4 and before the RESULT line (see step 8). Not read.
- Lane grep for Dobrushin, Shlosman, Follmer, Kunsch, Olivieri, "complete analyticity": the closest prior work is `library/gap-ds-gauge.md` (row 691, Claude Fable 5.2 medium; checked line by line by Claude Opus 5.5 high, row 693). Its Theorem W is a block criterion of Dobrushin-Shlosman type for the links of Z^4 with cube blocks and a weighted hypothesis (W). I read its header, Section 0 and its statement lines only. Theorem FST-BD below uses the same mechanism (an averaged block heat bath that contracts a sum of one-site seminorms). It differs in three ways that this row needs: any family of blocks, here one sheet or a square in one sheet; Lipschitz seminorms and influences of unbounded range with an exponential weight; and a covariance bound of Newman form that the face inherits. I give a short self-contained proof instead of adapting Theorem W.
- `library/gap-ds-gauge.md` line 15 records that nobody in the lane has read the Dobrushin-Shlosman papers or Martinelli-Olivieri. That is still true for this row. Every statement about those papers in step 7 is from memory and is marked so.
- Labels: grep for `FST-` in the lane gave no hit. I use FST-BD, FST-P, FST-F, FST-T.

## Step 3 result: hardest first. What the face needs from one sheet, and why the paper does not give it

The step most likely to fail is this: any control of all observables of one sheet once the on-site term has broken the sheet's own O(4) symmetry. I attacked it first.

**3.1 The face needs a single-sheet statement, with no transverse size in it. PROVED (it is M1).** By M1 the face is a family of sheets, each a two-dimensional O(4) model in a field H with |H_u| <= 2 lambda, and the field of sheet e is a function of its six neighbours. So every argument that goes from sheet to sheet needs the response of one sheet's law to a change of its field at one site u. That response is a covariance: d/dt E_{H + t delta_u a}[F] = Cov_H(F, a.Phi(u)). The transverse size T does not enter. Step 5 turns this remark into two theorems.

**3.2 The paper's argument in a field. FAILS at three named steps (counterexamples in step 7).**

- Ward step, (3.6). In a field the second variation of the action under a rotation of the sheet gains an on-site term. Row 1077's (9) is exactly this computation for one sheet. So the stiffness iteration (Sections 3.1 to 3.8) and the charged decay (3.61) are not available for a sheet in a field by any written step.
- Ginibre step, Section 3.11.1. A field whose direction varies from site to site leaves the class of zero-field ferromagnetic XY models after the two-circle decomposition. Positivity of cosine-character means fails (Lemma G1, step 7).
- Amplitude association, Section 3.11.2. With fields of two directions the gamma-marginal of an XY pair is not associated (Lemma G2, step 7).

**3.3 The paper's argument with pins.** Pins break the symmetry only at the boundary. (3.61) holds with pins, for charged observables. Section 3.11 does not: it is stated for the unpinned zero-field ferromagnet, and pins of different directions act on the conditional XY sectors as boundary fields of different directions, which is the situation of G1 and G2. So the influence of pins on rotation-invariant (neutral) observables is not controlled by any written step. This is the exact open item; I call it FST-N in step 7.

**3.4 Decision.** A statement about one sheet that would give (17) cannot be taken from the paper. I therefore (i) isolate the statement as a hypothesis, in three forms of decreasing strength (FST-P pinned square; FST-T zero-field multi-point; FST-F small field), (ii) prove that each gives (17) on a positive interval with constants free of L, M, T, and (iii) record exactly where a proof of the hypothesis from the paper stops.

## Step 4 result: Theorem FST-BD, an averaged block criterion. PROVED

**Setting.** S is a finite set with a metric d. For x in S, (Omega_x, rho_x) is a compact metric space of diameter at most D_0. Omega is the product. mu is a probability measure on Omega with a strictly positive continuous density with respect to a product reference measure. For V a subset of S and eta in Omega, mu_V^eta is the conditional law of the V-coordinates given the others, defined for every eta by the density. (P_V f)(eta) is the integral of f(xi_V, eta_{V^c}) against mu_V^eta. So mu(P_V f) = mu(f).

For a bounded measurable f, Lip_x(f) is the supremum of |f(eta) - f(eta')| / rho_x(eta_x, eta'_x) over pairs that differ only at x. The class Lc is the set of f with every Lip_x(f) finite. Telescoping one coordinate at a time gives osc(f) <= D_0 sum_x Lip_x(f). With the discrete metric, Lip_x = osc_x, D_0 = 1 and Lc is all bounded measurable functions.

A block family is a finite list B_1, ..., B_N of subsets of S (the blocks) whose union is S. n_x is the number of blocks that contain x; n_min and n_max are its extreme values. P = (1/N) sum_V P_V.

**Hypothesis (C), influence.** There are numbers k^V_{x->u} >= 0 (V a block, x not in V, u in V) such that for every block V, every F in Lc that depends on the V-coordinates only, and every pair eta, eta' that differ only at x not in V:

    | mu_V^eta(F) - mu_V^eta'(F) | <= rho_x(eta_x, eta'_x) sum_{u in V} k^V_{x->u} Lip_u(F).

(A coupling of the two laws with E rho_u(xi_u, xi'_u) <= k^V_{x->u} rho_x(eta_x, eta'_x) for every u gives (C). (C) itself needs no coupling.)

**Hypothesis (D_a), weighted Dobrushin-Shlosman sum.** There are a >= 0 and gamma < 1 with, for every u in S,

    sum_{V containing u} sum_{x not in V} e^{a d(x,u)} k^V_{x->u} <= gamma n_u.

**Theorem FST-BD.** Assume (C) and (D_a). Put theta = 1 - (1 - gamma) n_min / N.

(i) Let w be a positive function on S with w(x) <= e^{a d(x,u)} w(u) for all x, u. Put Delta_w(f) = sum_x w(x) Lip_x(f). Then Delta_w(P f) <= theta Delta_w(f) for every f in Lc.

(ii) sup |P^n f - mu(f)| <= D_0 theta^n Delta_1(f).

(iii) Let g be bounded measurable and depend only on the coordinates in a set B. Let B+ be the union of the blocks that meet B. Then for f in Lc

    |Cov_mu(f, g)| <= 2 ||g|| D_0 (n_max / n_min) (1 - gamma)^{-1} sum_x Lip_x(f) e^{-a d(x, B+)}.

(iv) Newman form. Assume also (I): there is X such that for every block V, every eta and all F, G in Lc on the V-coordinates,

    |Cov_{mu_V^eta}(F, G)| <= X sum_{u,b in V} Lip_u(F) Lip_b(G) e^{-a d(u,b)}.

Then for all f, g in Lc

    |Cov_mu(f, g)| <= (X n_max / ((1 - gamma) n_min)) sum_{x,b in S} Lip_x(f) Lip_b(g) e^{-a d(x,b)}.

**Proof.** Step A, one block. Let V be a block and f in Lc. P_V f does not depend on the V-coordinates, so Lip_x(P_V f) = 0 for x in V. Let x be outside V and let eta, eta' differ only at x. Then

    P_V f(eta) - P_V f(eta') = [mu_V^eta(f(., eta)) - mu_V^eta(f(., eta'))] + [mu_V^eta(f(., eta')) - mu_V^eta'(f(., eta'))].

The first bracket is at most Lip_x(f) rho_x(eta_x, eta'_x). The function xi -> f(xi, eta') has one-site constants at most those of f, so (C) bounds the second bracket. Hence

    Lip_x(P_V f) <= Lip_x(f) + sum_{u in V} k^V_{x->u} Lip_u(f)   (x not in V).      (BD1)

Step B, (i). Lip_x(P f) <= (1/N) sum_V Lip_x(P_V f). Multiply (BD1) by w(x), sum over x not in V, then over V:

    Delta_w(P f) <= sum_x w(x) Lip_x(f) (N - n_x)/N + (1/N) sum_u Lip_u(f) sum_{V containing u} sum_{x not in V} w(x) k^V_{x->u}.

Use w(x) <= e^{a d(x,u)} w(u) and (D_a). The second term is at most (gamma/N) sum_u n_u w(u) Lip_u(f). So Delta_w(P f) <= sum_u w(u) Lip_u(f) [1 - (1 - gamma) n_u / N] <= theta Delta_w(f).

Step C, (ii). The constant weight is allowed. mu(P^n f) = mu(f), so |P^n f - mu(f)| <= osc(P^n f) <= D_0 Delta_1(P^n f) <= D_0 theta^n Delta_1(f).

Step D, a comparison identity. Let g > 0 be bounded and depend on B only. Put nu = g mu / mu(g). Then Cov_mu(f, g) = mu(g) (nu(f) - mu(f)). By (ii), nu(P^n f) tends to mu(f). So

    nu(f) - mu(f) = sum_{n >= 0} [nu(P^n f) - nu(P^{n+1} f)] = (1/N) sum_{n >= 0} sum_V nu(h_n - P_V h_n),   h_n = P^n f.      (BD2)

If V does not meet B, then g does not depend on the V-coordinates, so mu(g P_V h) = mu(P_V(g h)) = mu(g h), and nu(h - P_V h) = 0. Only blocks that meet B contribute.

Step E, (iii). For any V, |h - P_V h| <= D_0 sum_{u in V} Lip_u(h) pointwise. Take w(x) = e^{-a d(x, B+)}; it is allowed in (i) by the triangle inequality, and w = 1 on B+. A site u lies in at most n_max blocks. So the inner sum over V in (BD2) is at most D_0 n_max Delta_w(h_n) <= D_0 n_max theta^n Delta_w(f). Summing the geometric series, |nu(f) - mu(f)| <= D_0 n_max Delta_w(f) / ((1 - gamma) n_min). For a general bounded g replace g by g + c with c > ||g||; the covariance does not change and mu(g + c) tends to 2 ||g|| as c tends to ||g||. This gives (iii).

Step F, (iv). The conditional law of nu on V is g mu_V^eta / mu_V^eta(g). So nu(h - P_V h) is the nu-average of Cov_{mu_V^eta}(h, g) / mu_V^eta(g), and by (I) it is at most (X / inf g) sum_{u,b in V} Lip_u(h) Lip_b(g) e^{-a d(u,b)}. If g is constant there is nothing to prove. Otherwise put W(u) = sum_b Lip_b(g) e^{-a d(u,b)} > 0. W is allowed in (i). A pair u, b lies in at most n_max common blocks. So the sum over V in (BD2) is at most (X n_max / inf g) Delta_W(h_n) <= (X n_max / inf g) theta^n Delta_W(f). Sum the series: |nu(f) - mu(f)| <= X n_max Delta_W(f) / (inf g (1 - gamma) n_min). Replace g by g + c: the Lipschitz constants and the covariance do not change, and mu(g + c) / inf(g + c) tends to 1 as c tends to infinity. This gives (iv). QED

Remarks. (a) Every step is a finite sum, a conditional expectation on a finite product of compact spaces, or a geometric series. It is Lean-formalizable. (b) The proof never conditions on B and never truncates a block. That is why it needs the hypothesis for whole blocks only. On a torus all blocks are whole. (c) Credit: the mechanism is Dobrushin's and Dobrushin and Shlosman's (constructive criterion; from memory, not read). The covariance form (iv) is of the type of Follmer's and Kunsch's covariance estimates under Dobrushin's condition (from memory, not read) and of Newman's inequality for associated variables, which OpenAI's Section 3.11.1 uses. The lane's Theorem W (row 691) is the same mechanism for cube blocks of links.

## Step 5 result: two implications to (17). PROVED

The face law lives on S = D x E_T, D = Z/L x Z/M. The metric is d((u,e),(u',e')) = |u - u'|_1 (periodic) + d_T(e,e'), where d_T is the graph distance for the relation e ~ e' of M2.

### 5.1 FST-P: one pinned square of one sheet

**Hypothesis FST-P(l, gamma_0)** for the zero-field sheet at coupling beta. Lambda is an l x l square in Z^2 and dLambda its 4l outer neighbours. For pins eta on dLambda, mu_Lambda^eta is the O(4) law in Lambda with all bonds inside Lambda and to dLambda at strength beta. There are numbers k0_{y->w} >= 0 (y in dLambda, w in Lambda) with

    | mu_Lambda^eta(F) - mu_Lambda^eta'(F) | <= sum_{w in Lambda} k0_{y->w} osc_w(F)

for all bounded measurable F and all pins eta, eta' that differ only at y, and

    sum_{y in dLambda} sum_{w in Lambda} k0_{y->w} <= gamma_0 l^2,   gamma_0 < 1.

This is the Dobrushin-Shlosman sum for one square, in the Hamming metric. It is a statement about one finite pinned system.

**Theorem FST-P.** Assume FST-P(l, gamma_0). Put

    gamma(lambda, a) = e^{a(2l-1)} [ gamma_0 + 8 l (e^{4 lambda l^2} - 1) + 6 l^2 (e^{4 lambda} - 1) ].

If gamma(lambda, a) < 1, then for all T >= 3 and all L, M >= l + 2, the face law on D x E_T obeys, for every bounded measurable f and every bounded measurable g that depends on a set B only,

    |Cov(f, g)| <= (2 ||g|| / (1 - gamma(lambda, a))) e^{2 a (l-1)} sum_x osc_x(f) e^{-a d(x, B)}.

gamma(0, 0) = gamma_0 < 1, so the condition holds on a rectangle 0 <= lambda <= eps, 0 <= a <= a_0 with eps, a_0 > 0 depending on l and gamma_0 only. One admissible choice: a = ln(2/(1+gamma_0)) / (2l - 1), and any lambda with 8 l (e^{4 lambda l^2} - 1) + 6 l^2 (e^{4 lambda} - 1) <= (1 - gamma_0)/4. Then gamma(lambda, a) <= (1 + 3 gamma_0)/(2 + 2 gamma_0) < 1.

**Proof.** Apply FST-BD with the discrete metric and the blocks V = (z + Lambda) x {e}, z in D, e in E_T. Since L, M >= l + 2, each block with its outer boundary sits in D without overlap. N = |D| |E_T| and n_x = l^2 for every x.

Influence on a block V = (z + Lambda) x {e}. By M1 the law of the block given everything else is the pinned O(4) law of sheet e in z + Lambda, tilted by exp{sum_{u in z+Lambda} H_u.Phi(u)}, |H_u| <= 2 lambda. It depends on the outside through the pins (y, e), y in z + dLambda, and through the links (u, e'), u in z + Lambda, e' ~ e.

- Tilt. |sum_u H_u.Phi(u)| <= 2 lambda l^2. So the density of the tilted law with respect to the untilted one lies in [e^{-4 lambda l^2}, e^{4 lambda l^2}], and |mu^{eta,H}(F) - mu^{eta,0}(F)| <= (e^{4 lambda l^2} - 1) osc(F) <= (e^{4 lambda l^2} - 1) sum_w osc_w(F).
- A change of one pin (y, e): by the triangle inequality through the two untilted laws and FST-P, (C) holds with k = k0_{y->w} + 2 (e^{4 lambda l^2} - 1).
- A change of one link (u, e'), e' ~ e: only H_u changes, by at most 2 lambda in norm (M2; one common square). The two tilted laws have a density ratio in [e^{-4 lambda}, e^{4 lambda}]. So (C) holds with k = e^{4 lambda} - 1 for every w in the block.

The sum in (D_a) for a site (w, e): each of the l^2 blocks that contain it is a translate, so the pin terms add up to sum_y sum_{w'} k0_{y->w'} + l^2 . 4l . 2 (e^{4 lambda l^2} - 1), and the link terms to l^2 . 6 l^2 (e^{4 lambda} - 1). Every influencing site is at distance at most 2l - 1 from the target. Dividing by n = l^2 gives (D_a) with gamma(lambda, a). FST-BD (iii) gives the bound with B+; every point of B+ is within 2(l-1) of B. QED

**Corollary (17) from FST-P.** For local Lipschitz F, H (invariant or not), osc_x(F) <= pi Lip_x(F), and the bound gives |Cov(F, tau_{n e_0} H)| <= C_{F,H} e^{-a n} with C_{F,H} = 2 pi ||H|| (1 - gamma)^{-1} e^{a(2l - 2 + r)} sum_x Lip_x(F), r the longitudinal extent of the two supports. C_{F,H} and a do not depend on L, M, T or lambda in [0, eps]. The bound holds on every torus, so it holds for every local limit of the periodic measures. If FST-P(l, gamma_0) holds for each beta in [2.3, 2.6], then (17) holds on [0, eps_beta] for each such beta; if l and gamma_0 can be chosen uniformly on the window, so can eps and a. The decay holds in all four directions, for all local observables.

### 5.2 FST-F: one unpinned sheet in a small field

**Hypothesis FST-F(h_0, a, X)** for the sheet at coupling beta. There is L_0 such that on every torus D with L, M >= L_0, for every field H with sup_u |H_u| <= h_0, the law mu_D^H proportional to exp{beta sum_<uv> Phi(u).Phi(v) + sum_u H_u.Phi(u)} obeys, for all F, G with finite one-site Lipschitz constants (local or not),

    |Cov_H(F, G)| <= X sum_{v,w in D} Lip_v(F) Lip_w(G) e^{-2a |v-w|_1}.

This is a two-point statement. It has no pins. It is uniform over small fields of arbitrary direction.

**Theorem FST-F.** Assume FST-F(h_0, a, X). Put S_a = ((1 + e^{-a})/(1 - e^{-a}))^2 and gamma = 6 lambda X e^a S_a. If lambda <= h_0/2 and gamma < 1, then for all T >= 3, all L, M >= L_0 and all f, g with finite one-site Lipschitz constants, the face law obeys

    |Cov(f, g)| <= (X / (1 - gamma)) sum_{x,b} Lip_x(f) Lip_b(g) e^{-a d(x,b)}.

So (17) holds on 0 <= lambda <= eps = min(h_0/2, 1/(12 X e^a S_a)), with rate a and prefactor 2X e^{a r} sum Lip_x(F) sum Lip_b(H), independent of L, M, T, lambda and the state.

**Proof.** Apply FST-BD with the round metric (D_0 = pi) and the blocks V_e = D x {e}: one whole sheet. N = |E_T|, n_x = 1. By M1 the law of the block is mu_D^H with |H| <= 2 lambda <= h_0.

(C): let x = (u, e'), e' ~ e, and change eta_x. Only H_u changes, to H_u + delta with |delta| <= lambda rho(eta_x, eta'_x) by M2. Every field H + s delta, 0 <= s <= 1, is a convex combination of the two fields H and H + delta, each of sup norm at most 2 lambda, so it has sup norm at most 2 lambda <= h_0. So

    mu^{H+delta}(F) - mu^H(F) = integral_0^1 Cov_{H + s delta}(F, delta.Phi(u)) ds,

and G = delta.Phi(u) has Lip_u(G) <= |delta|. FST-F gives (C) with k^{V_e}_{(u,e')->(w,e)} = lambda X e^{-2a|u-w|}. For e' not a neighbour of e the influence is zero.

(D_a): for the target (w, e), sum over the six neighbours e' and over u: 6 lambda X sum_u e^{a(|u-w|+1)} e^{-2a|u-w|} <= 6 lambda X e^a S_a = gamma.

(I): two sites of one block are in one sheet, d = |v-w|_1, and FST-F gives (I) with the same X since e^{-2a|v-w|} <= e^{-a|v-w|}.

FST-BD (iv) with n_max = n_min = 1 gives the claim. QED

Remark. The face inherits the hypothesis: the conclusion is FST-F's bound for the four-dimensional face law. The interval is explicit: eps is of order 1/X. If X is of the order of the sheet's susceptibility, of order Xi(beta)^2, then eps is of order Xi^{-2}. This matches the region beta_T Xi^2 <= eps of row 1066. That last sentence is a GUIDE-grade reading, not a proved size.

## Step 6 result: multi-point statements at zero field

### 6.1 FST-T: a multi-point statement that gives FST-F. PROVED implication

**Hypothesis FST-T(C_T, a, X_T)** for the zero-field sheet at coupling beta. There is L_0 such that on every torus D with L, M >= L_0, for every n >= 0, every assignment u -> a_u of vectors in R^4 with |a_u| <= 1, and all F, G with finite one-site Lipschitz constants,

    sum_{u_1,...,u_n in D} | kappa_{n+2}(F, G, a_{u_1}.Phi(u_1), ..., a_{u_n}.Phi(u_n)) | <= n! C_T^n X_T sum_{v,w} Lip_v(F) Lip_w(G) e^{-2a|v-w|_1}.

kappa is the joint cumulant under the zero-field law. This is tree-type decay in summed form: the two observables keep their exponential kernel, and each extra spin insertion, summed over its position, costs a factor C_T, with the factorial that counts orderings. It has no pins and no field.

**Proposition FST-T.** FST-T(C_T, a, X_T) implies FST-F(h_0, a, X) with h_0 = 1/(2 C_T) and X = 2 X_T.

**Proof.** Fix a torus, a field H with sup |H_u| <= h_0, and F, G. Put W = sum_u H_u.Phi(u) and g(t) = Cov_{tH}(F, G), t real. Then g(t) is the mixed derivative in (s, r) at 0 of log E_0 exp{tW + sF + rG}. The expectation is an entire function of (t, s, r) and is positive for real arguments, so g is real-analytic on the real line, and its n-th derivative at 0 is kappa_{n+2}(F, G, W, ..., W). By multilinearity, with H_u = |H_u| a_u, this is sum over (u_1, ..., u_n) of the product of the |H_{u_i}| times the cumulant in FST-T. So |g^(n)(0)| / n! <= (h_0 C_T)^n X_T K, K = sum Lip_v(F) Lip_w(G) e^{-2a|v-w|}. The Taylor series of g at 0 therefore converges for |t| < 2. Its sum is real-analytic on (-2, 2) and has the derivatives of g at 0. Two real-analytic functions on an interval with the same derivatives at one point are equal. So g(1) = sum_n g^(n)(0)/n!, and |g(1)| <= X_T K sum_n 2^{-n} = 2 X_T K. QED

So the chain is: FST-T gives FST-F gives (17) on a positive interval. FST-P gives (17) directly. I did not prove FST-P implies FST-F in the Lipschitz form, and I did not prove FST-T from FST-P. Of the three, FST-F is the weakest statement for which I have a proof of the implication. I do not claim that it is the weakest statement that exists. A convergent expansion of the face itself around the product of sheets (row 1078, O7(c)) would start from FST-T-type bounds for products over sheets; by M1 it is not needed, because FST-F is a two-point statement and FST-BD does the sheet-to-sheet step.

### 6.2 What Theorem 3.1 gives for cumulants: order three with rate c/2. PROVED GIVEN OpenAI Theorem 3.1

**Lemma K3.** Take the zero-field sheet on a free subgraph or on a torus with sides at least C Xi(beta). Let F_1, F_2, F_3 be local Lipschitz with supports A_1, A_2, A_3, n = |A_1| + |A_2| + |A_3|. Let d_i be the distance from A_i to the union of the other two and d* = max d_i. Then

    |kappa_3(F_1, F_2, F_3)| <= 4 C'_beta (1 + n)^20 L_{F_1} L_{F_2} L_{F_3} e^{-c d* / (2 Xi(beta))},

with C'_beta = C (1 + beta)^20 sup_{r >= 0} (1 + r)^20 e^{-c r/(2 Xi)}.

Proof. kappa_3(F_1, F_2, F_3) = Cov(F_1, F_2 F_3) - E[F_2] Cov(F_1, F_3) - E[F_3] Cov(F_1, F_2) (expand both sides). F_2 F_3 is local Lipschitz on A_2 u A_3 with L_{F_2 F_3} <= 2 L_{F_2} L_{F_3}. Each of the three covariances has F_1 at distance at least d_1 from the other support. Theorem 3.1 bounds each; (1 + beta + n + d)^20 <= (1 + beta)^20 (1 + n)^20 (1 + d)^20 and the polynomial in d is absorbed in half the rate. This gives the bound with d_1. The cumulant is symmetric, so the same holds with d_2 and d_3. QED

For three one-site observables d* is the second smallest of the three pairwise distances, so d* is at least half the length of the shortest tree on the three sites. So at lambda = 0 the third cumulants decay along trees at rate c/(4 Xi), with polynomial prefactors. This uses the theorem's polynomial support factor: a two-site observable costs only a constant.

**Consequence. ARGUED (outline written, constants not tracked).** The derivative at lambda = 0 of a face covariance is sum_{u,p} kappa_3^0(F, G, tau_p(u)) under the product of sheets. (a) A covariance bound for the product of independent sheets follows from the single-sheet bound by the martingale decomposition over sheets: F - E F is the sum over sheets j of M_j F = E[F | sheets j, j+1, ...] - E[F | sheets j+1, ...]; different j are orthogonal; E[M_j F M_j G] is an average of single-sheet covariances of functions whose norms are at most those of F, G. (b) If the square p shares no sheet with the supports of F and G, then tau_p(u) is independent of (F, G) and the cumulant is zero. So the number of squares p that contribute does not depend on T. (c) For the others, Lemma K3 with (a) gives decay in the distance from u to the supports, which is summable over u, uniformly in L, M. Hence the first derivative at lambda = 0 of the covariance in (17) is bounded uniformly in L, M, T, and it decays exponentially in the separation n. This removes the difficulty of row 1078, O7(c), at the single point lambda = 0 and at first order only.

**Why this does not continue to all orders. ARGUED.** For kappa_{n+2} the same method (isolate one group of insertions from the rest, use Theorem 3.1 for the two groups) gives decay in the largest gap between two groups. That gap is only at least (tree length)/(n+1). So the rate is c/((n+1) Xi), and the sum over the n positions is of order ((n+1) Xi / c)^{2n}. Against the 1/n! of the Taylor series this leaves a factor of order n^n: the bounds on the Taylor coefficients of lambda -> Cov_lambda(F, G) at 0 are finite at every order and uniform in L, M, T, but they do not show a positive radius. I recall that cumulant bounds from mixing rates alone have this (n!)^{1+kappa} form in general (Statulevicius; from memory, not read). FST-T asks for the n-independent rate. That is the exact difference between "two-point mixing with polynomial support factors", which the paper proves, and "tree-type decay", which the expansion needs. No step here derives the second from the first. I do not claim that no such derivation exists.

## Step 7 result: where a proof of the hypotheses stops; counterexamples; two-dimensional mechanisms

### 7.1 Lemma G1: Ginibre positivity fails with fields of two directions. PROVED

Two XY spins with weight exp{J cos(theta_1 - theta_2) + h cos(theta_1) - h cos(theta_2)}, J >= 0, h > 0, and uniform reference measure. Put r = I_1(h)/I_0(h) in (0, 1). At J = 0 the spins are independent, E cos(theta_1) = r, E cos(theta_2) = -r, E sin(theta_i) = 0. So E cos(theta_1 - theta_2) = -r^2 < 0, and

    d/dJ E cos(theta_1) at J = 0 equals Cov(cos theta_1, cos theta_1 cos theta_2 + sin theta_1 sin theta_2) = -r Var(cos theta_1) < 0.

By continuity both strict inequalities hold for small J > 0. So with two antiparallel fields the mean of the cosine character cos(theta_1 - theta_2) is negative and a one-point cosine mean decreases when the ferromagnetic coupling increases. Both contradict the two properties that Section 3.11.1 proves at zero field (nonnegative cosine-character means; monotonicity in every coupling). The model satisfies every other input of that section: nonnegative coupling, no twist, no pin. Where it applies: by M1 the sheet in the face has a field; after the two-circle decomposition the z-sector has the field cos(alpha_u) (H_u^1, H_u^2), whose direction varies with u because the neighbouring sheets vary. Scope: this refutes the step, for small J at fixed h. It does not refute decay for the sheet in a field, and it says nothing at J in the window.

### 7.2 Lemma G2: the amplitude marginal is not associated with fields of two directions. PROVED

Same two-site XY model, with the paper's split s_i = (tau_i^1 cos gamma_i, tau_i^2 sin gamma_i), gamma_i in [0, pi/2], fields (h, 0) at site 1 and (-h, 0) at site 2. Write c_i = cos gamma_i, s_i = sin gamma_i. Summing the four signs,

    Z^2 = 4 cosh(J s_1 s_2),   Z^1 = 2 e^{J c_1 c_2} cosh(h (c_1 - c_2)) + 2 e^{-J c_1 c_2} cosh(h (c_1 + c_2)).

The density of (gamma_1, gamma_2) with respect to the product measure is proportional to Z^1 Z^2. At J = 0 it is a product a(gamma_1) a(gamma_2), a proportional to cosh(h cos gamma). The J-derivative of log(Z^1 Z^2) at J = 0 is

    U = c_1 c_2 [cosh(h(c_1 - c_2)) - cosh(h(c_1 + c_2))] / [cosh(h(c_1 - c_2)) + cosh(h(c_1 + c_2))] = - phi(c_1) phi(c_2),   phi(c) = c tanh(h c).

For any observable A, d/dJ E_J[A] at 0 is Cov_0(A, U). With the product law at J = 0 a direct expansion gives

    d/dJ Cov_J(gamma_1, gamma_2) at J = 0 equals - [Cov_a(gamma, phi(cos gamma))]^2.

phi(cos gamma) is strictly decreasing in gamma on (0, pi/2) and a is a positive density, so Cov_a(gamma, phi(cos gamma)) < 0 strictly (Chebyshev's sum inequality). Cov_0(gamma_1, gamma_2) = 0. So Cov_J(gamma_1, gamma_2) < 0 for all small J > 0: two increasing functions of the amplitudes are negatively correlated. The gamma-marginal is not associated. At h = 0, phi = 0 and the derivative vanishes, in agreement with Section 3.11.2. Scope: as G1. The statement "the gamma marginal is associated" is proved in the paper for every nonnegative coupling at zero field; with fields of two directions it is false for small J. Nothing is claimed at the couplings of the window.

### 7.3 The Ward step in a field. PROVED in row 1077

Row 1077's (9), checked by row 1078 (E1): rotating one sheet in the face law adds 2 lambda sum_u f_u^2 to the second variation. By M1 this is the second variation of a single sheet in its field. So (3.6) fails for the sheet in a field for every lambda > 0, and with it the written route to (3.61). I add nothing to that computation.

### 7.4 The Newman form at zero field. OPEN; one sub-step FAILS

FST-F at H = 0 asks for |Cov(F, G)| <= X sum Lip_v(F) Lip_w(G) e^{-2a|v-w|} for all Lipschitz F, G, local or not. Theorem 3.1 gives, for local F, G, a bound with L_F L_G and a polynomial in the supports. That is not the same: L_F contains the sup norm. The place where the sup norm enters is Section 3.11.2: the Lipschitz constant in gamma_i of a conditional mean E[F | gamma] contains Cov(F, tau_e tau_e'), which the paper bounds by 2 ||F||, and the localization then needs F local. A proof of the Newman form along the same lines would need the conditional sign correlations E[tau_w tau_i | gamma] to decay uniformly in the conditioning. That uniform statement FAILS: at gamma = 0 on all sites the first sign species is an Ising model with couplings b cos(alpha_x) cos(alpha_y), which is b at alpha = 0, and for b in [2.3, 2.6] the two-dimensional Ising model at coupling b has long-range order (Peierls; classical, cited, not rebuilt). The paper avoids this with its L^1 localization. So the Newman form for the zero-field sheet is OPEN, not refuted.

### 7.5 The exact open item FST-N, and FST-P

**FST-N (OPEN).** For the O(4) sheet at beta in [2.3, 2.6]: the influence of arbitrary pins (or of an arbitrary field of sup norm at most h_0) on the expectation of a local observable that is invariant under the common left rotation decays exponentially with the distance to the pins, uniformly in the pins.

(3.61) is the same statement for charged observables, and the paper proves it with pins. A neutral observable does not see a common rotation of the pins; (3.61) does not control its dependence on the other degrees of freedom of the pins. FST-P needs FST-N in a quantitative Hamming form on one square. FST-F needs it for small fields, in Newman form.

A remark on orders. At H = 0 the response Cov_0(F, a.Phi(u)) of a neutral F to the field vanishes by symmetry. So for the invariant observables of (17) the first-order effect of the field is zero and the first nonzero term is kappa_3(F, Phi(u), Phi(u')), a three-point function with one neutral entry. Lemma K3 bounds it at H = 0. FST-F asks for the same control inside a small field, where the symmetry is gone.

### 7.6 Two-dimensional mechanisms, hypothesis by hypothesis. From memory; none of the three papers was read

The row 1092 reading was absent, so this section is from memory and is ARGUED at best.

- **Dobrushin-Shlosman constructive criterion (1985).** As I recall it, the criterion is a finite-volume inequality for one volume V and all boundary conditions, for a spin space with a metric. Compact continuous spins and a bounded continuous on-site potential (G-invariant or not) cause no difficulty. Its hypothesis for the sheet is FST-P. I did not use the paper: FST-BD rebuilds what (17) needs. Unverified hypothesis: FST-P itself. It quantifies over all pins of a square.
- **Complete analyticity (Dobrushin and Shlosman, 1985 and 1987).** As I recall it, the equivalent conditions are stated for a finite spin space and for all finite volumes. I did not check whether they extend to S^3. They are not needed: (17) is a statement on tori, and FST-BD (iii), (iv) give it from one block shape.
- **Weak mixing implies strong mixing in two dimensions (Martinelli, Olivieri and Schonmann, 1994).** As I recall it: finite spin space, finite range, translation invariance; weak mixing is a bound on the influence of the boundary condition on the bulk, uniform over all boundary conditions; the conclusion is strong mixing for squares. For the sheet two hypotheses are not verified. (i) The spin space S^3 is not finite; I did not check the proof for compact spins with a bounded pair interaction. (ii) Weak mixing with arbitrary pins is FST-N plus (3.61); Theorem 3.1 has no pins. So this mechanism would at best reduce FST-P to FST-N. It does not remove FST-N.
- **The G-invariant on-site potential.** For the face at fixed T the residual group G_T acts and the on-site term is G_T-invariant. This does not help any of the three mechanisms: each needs all boundary conditions of a block, and by row 1077's (10) the G_T directions do not move the invariant coordinates.

So each mechanism has the same first unverified hypothesis: control of neutral observables under pins or fields (FST-N). I found no step of the paper that gives it.

### 7.7 Counterexample to the implication itself: none found

I looked for a model that satisfies every input of Theorem 3.1's conclusion (exponential decay for all local Lipschitz observables on free subgraphs and large tori, uniformly under weakening of pair couplings) and violates FST-F or FST-P. I found none. Models at a first-order transition (Potts with many states at the transition) satisfy the free-subgraph input but fail the torus input, as I recall (the periodic state is a mixture); slightly inside the disordered phase they satisfy everything and the interval is positive. One-dimensional Ising chains satisfy the inputs and FST-F with X of the order of the correlation length. Row 1077's example (16) breaks translation invariance by a pin and uses a coupling 1/N. So the implication "Theorem 3.1's conclusion gives FST-F" is OPEN in both directions: not proved, not refuted. G1, G2 and 7.4 refute steps of one proof, on models that satisfy the inputs of those steps. They do not refute the implication.

## Step 8 result: controls, marks, limits, credits

### 8.1 Controls

- **Compact U(1).** FST-BD, Theorem FST-P, Theorem FST-F and Proposition FST-T are group-blind: they hold for any compact group with a multilinear plaquette term, with the same proofs. They do not contradict row 1077's (18): for XY sheets at large stiffness the hypotheses fail at the anchor (no exponential decay, given Frohlich and Spencer). The group enters through the hypothesis only.
- **Frozen Q_8 and 2T.** The hypotheses fail at the anchor in the frozen limit (row 1077, Section 5.3). No conflict.
- **Five dimensions.** With transverse torus (Z/T)^3 each edge lies in four squares and has twelve neighbours. The theorems hold with 6 replaced by 12 and |H_u| <= 4 lambda. So this step does not separate four from five dimensions. It need not: the anchor is the same product of two-dimensional sheets, and the statement is about the face at beta_L = infinity only.
- **Row 1078, O7(b).** The Ising example (16) is a statement about a gap and a perturbation norm only; it is not in the scope of the theorems, which assume a summable response of each sheet (FST-F or FST-P) and do not use the anchor gap. I did not compute whether (16) has such a response. The theorems use exactly the structure that (14) does not see: the product over sheets, the locality of the perturbation, and a summable response of each sheet.
- **Numerics.** No numeric run was made. Nothing here rests on a computation.

### 8.2 Marks

| Mark | Statement and scope |
|---|---|
| PROVED | M1, M2 (the face is a family of O(4) sheets in fields of norm at most 2 lambda; six neighbours; Lipschitz dependence). |
| PROVED | Theorem FST-BD (i)-(iv): averaged block criterion on a finite product of compact metric spaces, with a covariance bound of Newman form. Hand proof in step 4; not checked by anyone; not formalized. |
| PROVED GIVEN FST-P(l, gamma_0) | Theorem FST-P: (17) for 0 <= lambda <= eps(l, gamma_0), all T >= 3, all L, M >= l + 2, all local limits of periodic measures, all bounded local observables, in all four directions. FST-P is a Dobrushin-Shlosman sum below 1 for one pinned l x l square of the zero-field sheet. FST-P itself is OPEN. |
| PROVED GIVEN FST-F(h_0, a, X) | Theorem FST-F: (17) for 0 <= lambda <= min(h_0/2, 1/(12 X e^a S_a)), same uniformity, for all Lipschitz observables, with the face inheriting the Newman-form bound. FST-F is a two-point bound for one unpinned sheet in a field of sup norm at most h_0. FST-F itself is OPEN. |
| PROVED (implication) | Proposition FST-T: tree-type summed cumulant bounds at zero field (FST-T) give FST-F with h_0 = 1/(2 C_T). FST-T itself is OPEN. |
| PROVED GIVEN OpenAI Theorem 3.1 | Lemma K3: third cumulants of local Lipschitz observables of the zero-field sheet decay in the largest isolation distance at rate c/(2 Xi); along trees at rate c/(4 Xi) for one-site observables. |
| ARGUED | The first lambda-derivative at 0 of the covariance in (17) is bounded uniformly in L, M, T (outline in 6.2). Higher orders by the same method have rate c/((n+1) Xi) and give no positive radius. Statements about the Dobrushin-Shlosman, Martinelli-Olivieri-Schonmann, Follmer, Kunsch and Statulevicius results are from memory. |
| PROVED (counterexamples to steps) | G1: with two antiparallel fields a cosine-character mean is negative and a one-point mean decreases in J, for small J > 0. G2: with the same fields the gamma-marginal of an XY pair is not associated, for small J > 0. Both models have nonnegative couplings, no twists and no pins. |
| FAILS | For a sheet in a field or with pins of several directions: OpenAI's (3.6) (row 1077's (9)); the Ginibre step of Section 3.11.1 as a general lemma (G1); the amplitude association of Section 3.11.2 as a general lemma (G2); a uniform-in-conditioning bound on conditional sign correlations (7.4). Each failure is of one step of one proof, at the stated parameters. None is a failure of FST-F, FST-P, FST-N or (17). |
| OPEN | FST-N (pins or small fields do not move neutral local observables far away); hence FST-P, FST-F, FST-T; hence the target, (17) on a positive interval. The implication from Theorem 3.1's conclusion to FST-F: not proved, not refuted (7.7). |

### 8.3 What changed for the target

Before this row the target was a statement about a four-dimensional law of growing transverse size. After it, the target follows from a statement about one two-dimensional O(4) sheet, with no T in it: FST-F (unpinned, small field, two-point) or FST-P (one pinned square). The sheet-to-sheet step is closed by FST-BD. The interval is explicit in the constants of the hypothesis. The target itself is not proved: neither hypothesis follows from the posted theorem by a written step, and the first missing input is FST-N.

The next scientific decision is whether FST-N can be proved for the O(4) sheet. Two concrete entries: (i) pins of one direction keep the Ginibre class (a field cos(theta_x) with a nonnegative coefficient is a cosine character), so a version of Section 3.11 with aligned pins may hold, and a domination of general pins by aligned pins for plane rotators is the type of inequality I recall from Messager, Miracle-Sole and Pfister (from memory, not read; it would have to be read and rebuilt); (ii) a direct proof of FST-F at second order, where the neutral response is the three-point function of 7.5.

### 8.4 Limits of this row

- Nobody has checked this file. FST-BD and the two theorems are short, but a line-by-line check by a different model is needed before any use.
- The row 1092 reading did not arrive. Every literature statement about Dobrushin-Shlosman, Martinelli-Olivieri-Schonmann, Follmer, Kunsch, Statulevicius and Messager-Miracle-Sole-Pfister is from memory. None is load-bearing for a PROVED mark.
- OpenAI's Sections 3.1 to 3.7 were not re-read here. Theorem 3.1 is an imported, unrefereed input (ARGUED), used only in Lemma K3 and in 6.2.
- The plausibility of FST-P in the Hamming metric for continuous spins is not established. The theorem with the Lipschitz metric and pinned squares can be written the same way from FST-BD; I did not write it.
- (17) is covered for local limits of periodic measures. Free longitudinal boundaries would need truncated blocks and are not covered.
- Files changed: this file only. No download, no commit, no push. The paper copy read is row 1078's in `/tmp/opus-face2d-openai.NylL2Z`.

### 8.5 Credits

OpenAI's authors for the two-dimensional O(4) mixing theorem, its pinned charged decay (3.61), its Ward identity and its association argument. Jian Ding, Fenglin Huang and Peng Yang for the independent loop-soup decay mechanism mapped in row 1084 (not used here). Ethan Sussman and Levent Alpoge, with Claude and Codex as authors of their text, for the account whose scope the face route serves; Tadeusz Balaban for the ultraviolet construction behind it; neither is used as a gap input. Roland Dobrushin and Senya Shlosman for the block criterion that FST-BD rebuilds; Hans Follmer and Hans Kunsch for the covariance form; Charles Newman for the association inequality; Jean Ginibre for the plane-rotator inequality; Fabio Martinelli, Enzo Olivieri and Roberto Schonmann for the two-dimensional mixing theorem discussed in 7.6. Row 1077 (gpt-6-astra max) for the face law, (9), (15) and (17); row 1078 (Claude Opus 5.5 max) for O7 and the corrected decision J1; row 1084 (gpt-6-astra max) and row 1086 (Claude Opus 5.5 max) for Lemma DEC and the P4 counterexamples; row 691 (Claude Fable 5.2 medium) for Theorem W.

RESULT: target (17) on a positive interval is NOT proved; it is reduced to one two-dimensional sheet: PROVED Theorem FST-BD (averaged block criterion with a Newman-form covariance bound) and, from it, PROVED GIVEN FST-F (one unpinned O(4) sheet in any field of sup norm at most h_0 has a two-point Lipschitz covariance kernel X e^{-2a|v-w|}) that (17) holds for 0 <= lambda <= min(h_0/2, 1/(12 X e^a S_a)) with constants independent of L, M, T and the state, and PROVED GIVEN FST-P (a Dobrushin-Shlosman sum below 1 on one pinned square) the same on an explicit interval; PROVED that tree-type summed cumulant bounds at zero field (FST-T) give FST-F; PROVED GIVEN OpenAI Theorem 3.1 only third-cumulant tree decay at lambda = 0 (Lemma K3), with higher orders ARGUED to lose the rate as c/(n+1); FST-F, FST-P, FST-T and the neutral-observable pin/field statement FST-N are OPEN; OpenAI's (3.6), Ginibre step and amplitude association FAIL for a sheet in a field as general lemmas (row 1077's (9); two-site counterexamples G1, G2 at small J), which refutes those steps only; no counterexample to the implication was found; row 1092 reading absent, literature statements from memory; unchecked, not formalized, no mass gap claimed.
