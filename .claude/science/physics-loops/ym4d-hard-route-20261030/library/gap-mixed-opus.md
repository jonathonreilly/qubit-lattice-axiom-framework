# Uniform Langevin gap past 2/9: the mixed-Hessian estimate (FINISH row 818), by Claude Opus 5.5 (max effort), author

- Clone: `/Users/jonreilly/ym4d-lead/clone`, commit `0ed7f11be` for the first reads; after the pull the coordinator asked for, the clone is at `d6432f134` (`git -C` the clone `rev-parse --short HEAD`), and `gap-shape-exercise-astra.md` was read there.
- Lane directory D = `.claude/science/physics-loops/ym4d-hard-route-20261030`.
- Read in full: `D/library/gap-gamma2-astra.md` (row 812, Codex gpt-6-astra max) and its check `D/library/gap-gamma2-check-opus.md` (row 815, Claude Opus 5.5); `D/library/gap-vmf-lip.md` (Codex gpt-6-astra) with `D/library/gap-vmf-lip-check-opus.md` (Claude Opus 5.5); `D/library/gap-tu-retry.md` (Codex gpt-6-astra) with `D/library/gap-tu-check-opus.md` (Claude Opus 5.5). Read for orientation only: `D/library/gap-joint-astra.md` Section 4 (lines 367-502). Read after a coordinator message, not checked by anyone yet: `D/library/gap-shape-exercise-astra.md` (row 814, Codex gpt-6-astra), Route D (Lemma D1, lines 241-357) and Route C ((C1)-(C7), lines 475-618).
- Method: by hand. Labels: PROVED (hand proof in this note, author proof, not an independent check), READ (from a file, with path and line), ARGUED (an inference short of proof), GUIDE (a numeric run that may refute or guide, never discharge), OPEN (missing).
- No repository file was edited. Besides this file, only GUIDE scripts in the scratchpad folder `guide/` (next to `mixed-opus/`) were written.
- Notation follows `gap-gamma2-astra.md` (1)-(2) (READ, lines 75-101): M = (S^3)^E with the unit round metric, S_beta = beta sum_p (1 - q_p), q_p = tr U_p / 2, L = -Delta + grad S . grad, E, H, C, Q as there. Q = H + 2E + C is its (3) (READ, line 109). Equation labels (A1), (A2), ... in this note are new; plain numbers (3), (26), (27) refer to `gap-gamma2-astra.md`.

## 0. Checkpoint (updated in place)

- Final checkpoint. All sections written: 1 (slice comparison), 2 (weighted chord Dobrushin), 3 (Theorem A, beta < 1/4, every torus), 4 (perfect plaquette code, Theorem B, beta < 8/27 on periods in 82 Z, ceiling 1/3), 5 (pointwise mixed-Hessian constant at least 14), 6 (Villain test), 7 (order one), 8 (summary).
- Not done: an explicit 3-separated defect set for every even torus; a hand proof of `c_* <= 14`; any order-one estimate. No repository file was edited; GUIDE scripts live only in the scratchpad `guide/` folder.

## 1. A gauge slice can only raise the invariant gap

**PROVED (Lemma S).** Let V be the vertex set and E the link set of the torus. Write `s(e), t(e)` for the source and target of the positively oriented link e. The gauge group `G^V` acts by `(g.U)_e = g_{s(e)} U_e g_{t(e)}^{-1}`. Let F be a forest: a set of links with no cycle in the undirected graph (V, F), parallel links between the same two vertices included. Choose one root `r(tau)` in each component `tau` of (V, F); an isolated vertex is its own component. Put

    G_F = { g in G^V : g_{r(tau)} = 1 for every component tau },
    S_F = { U : U_e = 1 for every e in F },  identified with (S^3)^{E \ F}.

(i) The map `Phi(g, U') = g.U'` from `G_F x S_F` to `M = (S^3)^E` is a diffeomorphism. It carries the product of Haar measure on `G_F` and `prod_{e not in F} d sigma(U'_e)` to `prod_{e in E} d sigma(U_e)`.

(ii) `mu_beta = Phi_*(Haar x mu_F)`, where `mu_F` is proportional to `exp(-S_beta(U')) prod_{e not in F} d sigma(U'_e)` on `S_F`.

(iii) Let f be smooth and gauge invariant, and `f_F` its restriction to `S_F`. Then `Var_{mu_beta} f = Var_{mu_F} f_F` and

    E(f) >= E_F(f_F) := mu_F( sum_{e not in F} |grad_e f_F|^2 ).               (A1)

(iv) Consequently `gamma_inv(beta, Lambda) >= gamma(mu_F)`, the Poincare constant of `mu_F` over all smooth functions on `(S^3)^{E \ F}` with the product unit metric. The same holds with fixed center signs `epsilon_p`.

*Proof.* (i) Given U, define g on each tree from its root: `g_r = 1`, and for a forest link e between a vertex already reached and a new vertex, solve `U_e = g_{s(e)} g_{t(e)}^{-1}` for the new value (`g_{t(e)} = U_e^{-1} g_{s(e)}` or `g_{s(e)} = U_e g_{t(e)}`). Acyclicity makes this unique and well defined. Then `U' = g^{-1}.U` lies in `S_F`. So Phi is bijective with a smooth inverse. For the measure, the inverse map sends `(U_e)_{e in F}` to g by these successive solutions. At each step the new value is the image of `U_e` under inversion and a translation, both Haar preserving; Fubini along the tree order shows that `(U_e)_{e in F} -> g` maps product Haar to Haar on `G_F`. For fixed g, each `U'_e = g_{s(e)}^{-1} U_e g_{t(e)}`, `e not in F`, is again a Haar-preserving image. (ii) follows from (i) and gauge invariance, `S_beta(g.U') = S_beta(U')`. (iii) The variance identity is (ii) applied to f and f^2, since `f(g.U') = f_F(U')`. Gauge transformations act by isometries of M (left and right multiplications on each factor). For invariant f this gives `|grad f|^2(g.U') = |grad f|^2(U')`, so `E(f) = mu_F(|grad f|^2 on S_F)`. On `S_F` the gradient of `f_F` for the product metric of the non-forest factors is the list of components `grad_e f`, `e not in F`. Dropping the forest components gives (A1). (iv) For invariant nonconstant f, `E(f)/Var f >= E_F(f_F)/Var f_F >= gamma(mu_F)`. Center signs keep the action gauge invariant and change nothing above. QED.

**PROVED (conditional laws on the slice).** For `e not in F`, the conditional law of `U'_e` under `mu_F`, given the other non-forest links, is `nu_h` (density proportional to `exp(h.x)` on the unit `S^3`), with `h = beta sum_{p containing e} epsilon_p conj(W_p)`. Here `W_p` is the product of the other three links of p in the cyclic order that starts at e, with forest links equal to 1 and inversions as the orientation requires. Each `W_p` is a unit quaternion. This is the computation READ in `gap-gamma2-astra.md` lines 261-263 (check: `gap-gamma2-check-opus.md` item 4, "Conditional law"); setting some factors to 1 changes nothing in it.

**PROVED (slice influence).** For distinct non-forest links e, k let `n^F_{ek}` be the number of plaquettes containing both (as indexed plaquettes; it is 0, 1, or 2, and 2 only for parallel links at period 2). Changing `U'_k` alone changes each staple `W_p` with p containing e and k by exactly `|U'_k - U''_k|`, since k occurs once in p and the other factors are fixed unit quaternions (left and right multiplication and inversion are Euclidean isometries; READ `gap-vmf-lip.md` lines 329-346, check section 4). Other staples do not change. So `|h - h'| <= beta n^F_{ek} |U'_k - U''_k|`. Corollary V1 (READ `gap-vmf-lip.md` (7), lines 209-220; check section 2, HOLDS) gives the chord Dobrushin hypothesis (8) of Lemma DC with

    C^F_{ek} = beta n^F_{ek} / 4.                                                (A2)

**ARGUED (why this helps).** Gauge invariance is a redundancy of the full product chart. The slice removes the redundant link variables. A non-forest link then has fewer plaquette neighbours that can move. The single-link chord Dobrushin count drops from 18 to at most 16 in Section 3 and to 12 in the bulk of Section 4. The zero-field example of `gap-gamma2-astra.md` 5.2 is not contradicted: it shows that `beta/4` per neighbour is sharp, and the slice lowers the number of moving neighbours, not the price of each.

## 2. Weighted chord Dobrushin and its spectral consequence

**PROVED (Lemma W).** Let `mu` be a probability law on `Omega = (S^3)^I`, with `|I| = N`, whose one-site conditional laws have versions `gamma_i(.|w)` satisfying the chord hypothesis (8) of `gap-vmf-lip.md` with coefficients `C_ij >= 0`, `C_ii = 0`. Suppose a vector `w` with positive entries and a number `alpha < 1` satisfy

    sum_j C_ij w_j <= alpha w_i   for every i.                                    (A3)

Then, with `q = 1 - (1 - alpha)/N` and `K = N^{-1} sum_i Pi_i` (`Pi_i` the conditional expectation at i):

(a) `osc(P^t f) <= 2 q^t Delta_w(f) / min_i w_i`, where `Delta_w(f) = sum_i w_i delta_i(f)` and `P` is the averaged update of Lemma DC;

(b) `K <= q I` on the centered subspace of `L^2(mu)`, hence `sum_i mu(Var_i f) >= (1 - alpha) Var_mu f`;

(c) if every conditional law has Poincare constant at least c, uniformly in the exterior, then `mu(|grad f|^2) >= c (1 - alpha) Var_mu f`.

*Proof.* Inequality (9) of Lemma DC, `delta_j(Gamma_i g) <= delta_j(g) + C_ij delta_i(g)` (READ `gap-vmf-lip.md` line 263; check section 3), averaged over i gives `delta(Pg) <= R^T delta(g)` entrywise with `R = (1 - 1/N) I + C/N` (READ, same check, "orientation of R"). Then `Delta_w(Pg) = w^T delta(Pg) <= (R w)^T delta(g)`. By (A3), `(Rw)_i <= (1 - 1/N + alpha/N) w_i = q w_i`. So `Delta_w(Pg) <= q Delta_w(g)`, and iteration gives `Delta_w(P^t f) <= q^t Delta_w(f)`. Changing one coordinate at a time and using the chord diameter 2 gives `osc(g) <= 2 sum_i delta_i(g) <= 2 Delta_w(g)/min_i w_i`. This proves (a). For (b), repeat the argument after (13) of `gap-gamma2-astra.md` (READ lines 313-319; check item 5) with `2 D_ch(f)` replaced by `2 Delta_w(f)/min_i w_i`, a finite constant for each smooth f: the positive spectral measure of a centered smooth f cannot charge `[q + eps, 1]`, smooth functions are dense, and `N <f, (I - K) f> = sum_i mu(Var_i f)`. For (c), integrate the conditional Poincare inequalities and sum: `mu(|grad f|^2) >= c sum_i mu(Var_i f)`. QED.

With `w = 1` this is exactly the chord route (13)-(15) of `gap-gamma2-astra.md`. By Perron-Frobenius, the best `alpha` in (A3) over positive w is the spectral radius of C (for irreducible C); (A3) is the Collatz-Wielandt form of that bound.

**Conditional gap constants.** Inequality (10) of `gap-gamma2-astra.md` gives `c = 2` for every field (READ lines 249-257; check item 4, HOLDS). Lemma D1 of `gap-shape-exercise-astra.md` (READ lines 266-339, by Codex gpt-6-astra, not yet checked) gives the sharp `c = 3`. Below, every bound is stated with the checked `c = 2`, and the D1 value is added in brackets.

## 3. Theorem A: a uniform invariant gap for beta < 1/4 on every torus

**PROVED (Theorem A).** Let `Lambda` be a periodic four-torus whose largest period is at least 3, with any fixed center signs. For `0 <= beta < 1/4`,

    gamma_inv(beta, Lambda) >= 2 (1 - 4 beta)        [ >= 3 (1 - 4 beta) with Lemma D1, READ ].     (A4)

The only torus with all periods below 3 is `(Z/2)^4`. Its invariant gap is positive at each beta: the Holley-Stroock bound of `gap-gamma2-check-opus.md` item 3 gives at least `3 exp(-2 beta |P|) = 3 exp(-192 beta)` (READ; `|P| = 96`). Hence, on every compact `[0, b_+]` with `b_+ < 1/4`, the invariant Langevin gap is bounded below uniformly over all periodic tori, by `min{2(1 - 4 b_+), 3 exp(-192 b_+)}`, and by `2(1 - 4 b_+)` on the tori with a period at least 3.

*Proof.* Call a direction with the largest period "time", and write `T >= 3` for that period and `t = x_0` for the level. Take the axial forest

    F_ax = { (x, 0) : 0 <= x_0 <= T - 2 }.

It is a union of vertex-disjoint time paths, one per spatial position, so it is a forest. The non-forest links are the spatial links `(x, i)`, `i = 1, 2, 3`, at every level, and the closing time links `(x, 0)` with `x_0 = T - 1`. Count plaquette occurrences of non-forest neighbours, as in (A2):

| link | plaquettes and moving neighbours | weighted sum `sum_k n_ek w_k` |
|---|---|---|
| spatial, level t, `1 <= t <= T-2` | 4 space-space plaquettes: 12 spatial at level t; upper time plaquette (forest time links at level t): 1 spatial at t+1; lower one (forest at t-1): 1 spatial at t-1 | `12 w_t + w_{t+1} + w_{t-1}` |
| spatial, level `T-1` | 12 spatial at `T-1`; upper time plaquette has closing time links: 2 closing + 1 spatial at level 0; lower: 1 spatial at `T-2` | `12 w_{T-1} + 2a + w_0 + w_{T-2}` |
| spatial, level 0 | 12 spatial at 0; upper: 1 spatial at 1; lower plaquette has closing links: 2 closing + 1 spatial at `T-1` | `12 w_0 + w_1 + 2a + w_{T-1}` |
| closing | 6 time-space plaquettes, each with 1 spatial at `T-1`, 1 spatial at 0, 1 closing | `6 w_{T-1} + 6 w_0 + 6 a` |

Here `w_t` is the weight of a spatial link at level t and `a` that of a closing link. Every period is at least 2, so no plaquette repeats a link; at period 2 two parallel links can share two plaquettes, and occurrence counting covers it, as in (A2).

For `T >= 4` take `w_t = 1` for `1 <= t <= T-2`, `w_0 = w_{T-1} = 3`, `a = 4`. The four rows give 14 (or `12 + 1 + 3 = 16` at levels 1 and `T-2`), `36 + 8 + 3 + 1 = 48 = 16 * 3`, `48 = 16 * 3`, and `18 + 18 + 24 = 60 = 15 * 4`. For `T = 3` take `w_1 = 1`, `w_0 = w_2 = 2`, `a = 5/2`. The rows give `12 + 2 + 2 = 16`, `24 + 5 + 2 + 1 = 32 = 16 * 2`, `32`, and `12 + 12 + 15 = 39 = 15.6 * 5/2`. In both cases `sum_k n_ek w_k <= 16 w_e` for every non-forest e. By (A2), (A3) holds with `alpha = (beta/4) * 16 = 4 beta`. Lemma W(c) with `c = 2` gives `gamma(mu_{F_ax}) >= 2(1 - 4 beta)`, and Lemma S(iv) gives (A4). QED.

**GUIDE (not a proof step).** A short script (stdin, no file written) built `F_ax` on the tori with periods `(3,2,2,2), (3,3,3,3), (3,2,4,3), (4,2,2,2), (4,4,4,4), (5,3,2,4), (6,4,4,4), (7,3,3,3)`, checked acyclicity by union-find, and computed `max_e sum_k n_ek w_k / w_e` with the weights above. It printed 16.0 on every torus. Memory use was a few megabytes.

**PROVED (the constants of (G2) and (27)).** By `gap-gamma2-astra.md` (8) (READ lines 192-209; check item 2, HOLDS), a uniform invariant gap `lambda_*` on `[0, b_+]` gives (G2) with `delta = 1 - theta = lambda_*/(2(lambda_* + 24 b_+))` and `kappa = lambda_*/2`, and (27) with the same `delta, kappa` (it is an exact rewrite, check item 8). On the tori with a period at least 3, take `lambda_* = 2(1 - 4 b_+)`. For example, `b_+ = 6/25 = 0.24`, which lies above `2/9` and above `11/48`:

    lambda_* = 2/25,  delta = (2/25)/(2 * 146/25) = 1/146,  theta = 145/146,  kappa = 1/25,      (A5)

that is, for every gauge-invariant f and every `0 <= beta <= 6/25`,

    C_m + R/3 >= -(2/3 - 1/146) H_d - (145/146) H_m - (49/25) E.

With Lemma D1 (READ, unchecked), `lambda_* = 3/25`, `delta = 1/98`, `kappa = 3/50`. These are exact rational values.

**Comparison with the new Codex input (READ, unchecked).** Route C of `gap-shape-exercise-astra.md` gives `Q >= (33/8 - 18 beta) E` and the interval `beta < 11/48` for tori with all periods at least 4, plus finitely many exceptions; it states that thin tori with a period 2 or 3 and unbounded other periods are not covered (lines 601-605). Theorem A uses only checked inputs, covers every torus, and reaches `1/4 = 11/48 + 1/48`. In effective terms, Route C pays each mixed-Hessian neighbour `beta / (33/8) = (8/33) beta` against 18 neighbours; Theorem A pays `beta/4` against at most 16 weighted neighbours. The gain comes from the count, not from the per-neighbour constant.

## 4. A perfect plaquette code, Theorem B (beta < 8/27), and the ceiling 1/3 of the slice method

In this section the directions are labelled 1, 2, 3, 4, and `pi(x) = (x_1, ..., x_4) mod 2`.

**PROVED (Lemma P, a perfect plaquette code).** Let every period be even. Put, in the listed coordinates,

    A_1 = {000, 111} in (pi_2, pi_3, pi_4),   A_2 = {001, 110} in (pi_1, pi_3, pi_4),
    A_3 = {101, 010} in (pi_1, pi_2, pi_4),   A_4 = {001, 110} in (pi_1, pi_2, pi_3),
    F = { (x, mu) : the three parities of x transverse to mu lie in A_mu }.

Then every plaquette contains exactly one link of F.

*Proof.* Take a plaquette in the plane `(mu, nu)` with base point x, and let `{rho, sigma}` be the other two directions. Its four links have base points in `{x, x + e_mu, x + e_nu}`, all with the same pair `tau = (pi_rho, pi_sigma)`. Its two mu-links have base points x and `x + e_nu`, whose `pi_nu` take both values. So the number of its mu-links in F is the number of points of `A_mu` whose `(rho, sigma)` part is `tau`; similarly for its nu-links. The two points of each `A_mu` differ in all three coordinates, so each of these numbers is 0 or 1, and it is 1 exactly when `tau` lies in the projection of `A_mu` (resp. `A_nu`) to the `(rho, sigma)` coordinates. The six projections pair up as follows:

| plane | projection of `A_mu` | projection of `A_nu` |
|---|---|---|
| (1,2), onto (3,4) | {00, 11} | {01, 10} |
| (1,3), onto (2,4) | {00, 11} | {01, 10} |
| (1,4), onto (2,3) | {00, 11} | {01, 10} |
| (2,3), onto (1,4) | {01, 10} | {11, 00} |
| (2,4), onto (1,3) | {00, 11} | {01, 10} |
| (3,4), onto (1,2) | {10, 01} | {00, 11} |

In every row the two sets partition `(Z/2)^2`. So exactly one of the four links lies in F. QED.

**PROVED (structure of F).** Two links of F never share a plaquette. Two links of different directions that meet at a vertex always share a plaquette, so each vertex meets F only along one straight line. Membership of `(x, mu)` depends only on the transverse parities, so `(x, mu)` in F implies `(x + e_mu, mu)` in F. A quarter of the direction-mu links lie in F (two of eight transverse classes), so `|F| = |V|`. Hence every vertex has exactly one outgoing F-link, and the components of F are closed straight lines ("F-lines") wrapping the torus. Every non-F link lies in six plaquettes, each with exactly one F-link and two other non-F links: its count `sum_k n_ek` is exactly 12.

**GUIDE (not a proof step).** A stdin script checked the exact cover and the single outgoing link on the tori `(2,2,2,2), (4,4,4,4), (2,4,6,8), (6,6,4,2)`: zero bad plaquettes, one outgoing F-link per vertex.

**PROVED (a 3-separated defect set).** Let every period be a multiple of `m = 82`. Put

    Gamma = { x : x_1 + 3 x_2 + 9 x_3 + 27 x_4 = 0 mod 82 },   D = { the F-link leaving x : x in Gamma },   F' = F \ D.

(a) Every F-line meets Gamma: along a mu-line the linear form changes by `a_mu` in `{1, 3, 9, 27}`, which is invertible mod 82, and the line has a multiple of 82 points. So every F-line loses at least one link, and F' is a forest (a union of paths). (b) Gamma is 3-separated in the periodic `l^infinity` distance: if `x != x'` in Gamma had a difference representative z with `|z|_infinity <= 2`, then `a.z = 0 mod 82` (82 divides every period), and `|a.z| <= 2 * 40 = 80` forces `a.z = 0`; reading `z_1 + 3 z_2 + 9 z_3 + 27 z_4 = 0` with digits in `{-2, ..., 2}` modulo 3, then 9, then 27 gives `z = 0`. (c) Base points of two links of one plaquette differ by a vector in `{-1, 0, 1}^4`. So if a non-F link were in a plaquette with a defect d and in another plaquette with a defect d', then `|base(d) - base(d')|_infinity <= 2`, and by (b) `d = d'`; two distinct links share at most one plaquette when the periods are at least 3. Hence every non-F link is adjacent to at most one defect, through exactly one plaquette.

**PROVED (Theorem B).** On every torus whose periods are all multiples of 82, with any fixed center signs,

    gamma_inv(beta, Lambda) >= 2 (1 - 27 beta / 8)   for 0 <= beta < 8/27 = 0.2962...,     [ 3(1 - 27 beta/8) with D1 ]     (A6)

and the optimal two-level weights give the interval `beta < (2/3)(sqrt 6 - 2) = 0.2996...`.

*Proof.* Use Lemma S with the forest F' and Lemma W with weight `lambda` on defects and 1 on non-F links. A defect has 18 non-forest neighbours, all non-F (its six plaquettes contained no other F-link): weighted sum 18. A non-F link adjacent to no defect has six covered plaquettes: sum 12. A non-F link adjacent to one defect has one uncovered plaquette (the defect and two non-F links) and five covered ones: sum `12 + lambda`. With `lambda = 4/3` the ratios are `18/(4/3) = 27/2`, `12`, and `40/3 < 27/2`. So (A3) holds with `alpha = (beta/4)(27/2) = 27 beta/8`, and Lemmas W(c) and S give (A6). With `lambda = 3 sqrt 6 - 6`, which solves `lambda (12 + lambda) = 18`, the largest ratio is `6 + 3 sqrt 6`, giving the second interval. QED.

**GUIDE (not a proof step).** On `(Z/8)^4` with two defects at `l^infinity` distance 4 and `lambda = 4/3`, a stdin script found the ratio histogram `12.0` (12252 links), `13.333` (36 links), `13.5` (2 defects), as computed above.

**PROVED (ceiling of the slice method).** Let F be any forest on a torus with periods at least 3 in which no plaquette contains three forest links. Then (i) the bound (A2) is attained: the optimal worst-exterior chord coefficients satisfy `C*_{ek} >= beta n^F_{ek}/4` whenever `n^F_{ek} = 1`; and (ii) for every positive weight vector, `max_e sum_k C*_{ek} w_k / w_e > 3 beta`. Hence condition (A3) with `alpha < 1` fails for every such forest once `beta >= 1/3`.

*Proof.* (i) Each plaquette through a non-forest link e has a non-forest link other than e, so each of the six staples of e can be set to any unit quaternion. Choose them so that the six terms `epsilon_p conj(W_p)` are three copies of 1 and three of -1: the conditional field is 0 and the conditional law is Haar. Moving a neighbour k that shares one plaquette with e along a unit-speed geodesic moves the field with speed `beta`. The derivative of the conditional mean of the chord-1-Lipschitz function `x.w` (w the direction of that motion) is `beta Haar((x.w)^2) = beta/4`, while chord displacement over geodesic length tends to 1. This is the argument of `gap-gamma2-astra.md` 5.2 (READ lines 507-521; check item 7, HOLDS), now on the slice. (ii) `N^F = (n^F_{ek})` is symmetric and nonnegative, so its spectral radius is at least its average row sum. With `x_p` the number of forest links in plaquette p (at most 3 in a forest), the total of the row sums is `sum_p (4 - x_p)(3 - x_p) >= sum_p (12 - 6 x_p) = 72 |V| - 36 |F|`, using `x_p^2 >= x_p` and `sum_p x_p = 6|F|`. The number of non-forest links is `4|V| - |F|`. Since `|F| <= |V| - 1`,

    average row sum >= 12 + 24 (|V| - |F|) / (4|V| - |F|) > 12.

By (i), `C* >= (beta/4) N^F` entrywise on the pairs with `n = 1`, and on period-at-least-3 tori every nonzero `n^F_{ek}` equals 1. The Collatz-Wielandt inequality `max_e (C* w)_e / w_e >= rho(C*)` for nonnegative matrices and positive w, with `rho(C*) >= (beta/4) rho(N^F) > 3 beta`, proves (ii). QED.

**ARGUED.** The perfect code shows that the average count can be brought down to `12 + O(1/m)` when defects are sparse. Whether the spectral radius itself tends to 12 depends on whether isolated defects bind a Perron vector; a rough four-dimensional Green-function estimate suggests they do not, so this method should approach, but never reach, `beta = 1/3`. Theorem B reaches `0.2996...`. Covering every even torus (not only multiples of 82) needs a 3-separated set meeting every F-line on each torus; that combinatorial step is **OPEN** here. For general tori Theorem A (`beta < 1/4`) is what is proved.

**PROVED (constants of (G2) and (27) from Theorem B).** On the tori with all periods in `82 Z`, take `b_+ = 2/7 = 0.2857...` (above `11/48`, below `8/27`). Then `27 b_+/8 = 27/28`, `lambda_* = 1/14`, and (8) of `gap-gamma2-astra.md` gives

    delta = (1/14) / (2 (1/14 + 96/14)) = 1/194,   theta = 193/194,   kappa = 1/28,

so `C_m + R/3 >= -(2/3 - 1/194) H_d - (193/194) H_m - (55/28) E` for every invariant f and `0 <= beta <= 2/7` on those tori.

## 5. The pointwise mixed-Hessian constant: a ceiling for Bochner routes that bound C_m pointwise

Write `M_U` for the off-diagonal-block part of `Hess S_beta` at U, divided by beta, so that `C_m = beta mu(M_U(grad f, grad f))`. Route C (READ) uses `M_U >= -18`. Let `c_*` be the least constant with `M_U >= -c_*` for every U on every even torus.

**PROVED (c_* >= 14, attained on horizontal vectors).** Let every period be even. In directions 1-4 fix the plane signs

    s_12 = s_13 = s_24 = s_34 = -1,   s_14 = s_23 = +1,

and put `U_nu(x) = prod_{mu < nu} s_{mu nu}^{x_mu}`, a configuration with values `+1, -1`. Each plaquette of the plane `(mu, nu)` then equals `s_{mu nu}`: for `mu < nu`, `U_mu(x + e_nu) = U_mu(x)` and `U_nu(x + e_mu) = s_{mu nu} U_nu(x)`; periodicity needs only even periods. At such a central configuration the central factors commute out of every plaquette, and the expansion used for (22) of `gap-gamma2-astra.md` (READ lines 471-479; check item 7) gives, in left-invariant coordinates,

    Hess S_beta (X, X) = beta sum_p q_p |(dX)_p|^2,    diagonal block at a mu-link = beta (sum_{p containing it} q_p) I = 2 beta (sum_{nu != mu} s_{mu nu}) I = -2 beta I,

with `dX` the plain lattice curl. Take the staggered field `X_mu(x) = (-1)^{x_1 + x_2 + x_3 + x_4} a_mu T`, T a unit imaginary quaternion, `a = (1, -1, -1, 1)`. As in (23), `|(dX)_{mu nu}|^2 = 4 (a_mu - a_nu)^2` at every site. The six signed squares give `-4 - 4 + 0 + 0 - 4 - 4 = -16`, so `Hess S (X, X) = -16 beta |X|^2` (per site `4 * (-16) = -64` against `|X|^2 = 4`), and hence

    beta M_U (X, X) = Hess S (X, X) - (diagonal part) = -16 beta |X|^2 + 2 beta |X|^2 = -14 beta |X|^2.      (A7)

The field is divergence free (`sum_mu a_mu = 0`), so it is orthogonal to the gauge directions `d_0 Y` at this central configuration. So `c_* >= 14`, even on horizontal vectors.

**ARGUED.** Gradients of invariant functions vanish at central configurations, but at generic points `U_c exp(eps X)` the horizontal space, as eps tends to 0, still contains X (the extra vertical directions `[Z, X]` are orthogonal to X). So no pointwise bound `M_U(grad f, grad f) >= -c |grad f|^2` with `c < 14` holds for invariant f either.

**PROVED (consequence for Route C).** In (C5) of `gap-shape-exercise-astra.md` (READ), the only coupling-dependent input is `C_m >= -18 beta E`. Any argument that bounds `C_m` by a pointwise operator bound on `M_U` gets at best `C_m >= -14 beta E`. With the reserves of D1 (3) and (C4) (9/8), both READ and unchecked, such a route stops at `33/(8 * 14) = 33/112 = 0.2946...`. On tori with all periods in `82 Z`, Theorem B already passes this value (`8/27 = 0.2962...`) with checked inputs; on general tori Theorem A gives `1/4`.

**GUIDE (not a proof step).** Scripts `mixhess.py`, `optmix.py` to `optmix4.py` in `/private/tmp/claude-501/-Users-jonreilly-Projects-Physics--claude-worktrees-peaceful-heisenberg-e2d2a0/b3f5c21a-8638-4944-b69d-c639619895d6/scratchpad/guide/` build the mixed Hessian on `(Z/4)^4` (3072 coordinates) and minimise its lowest eigenvalue over configurations by Hellmann-Feynman descent. Results: identity configuration `-6`; all-`(-1)` central configuration `-10` (full Hessian `-16`, matching (23)); Haar-random configurations about `-7.4`; descent from five Haar-random starts converged to `-14.0` every time, each time at a central configuration with four planes of flux `-1` and two of flux `+1` (mean `q_p = -1/3`). Peak memory under 90 MB. This suggests `c_* = 14`; it proves nothing.

**OPEN.** A hand proof of `M_U >= -14` (or any constant below 18) for all U. With it, Route C (if its inputs check) would give `Q >= (33/8 - c beta) E`.

## 6. Binding test: periodic Villain U(1) at beta >= 2^14

The positive arguments of Sections 1-4 have four steps:

- (S1) the slice comparison, Lemma S;
- (S2) a conditional Poincare inequality for each one-link law of the slice, uniform in the exterior;
- (S3) the influence bound (A2), which uses Theorem V of `gap-vmf-lip.md` (the sharp von Mises-Fisher covariance constant `a(|F|) <= 1/4` and a conditional field linear in beta);
- (S4) the weighted row-sum condition (A3) with `alpha < 1`, then Lemma W.

**PROVED (where the argument fails for Villain).** Replace SU(2) by U(1), the unit 3-spheres by unit circles, and the Wilson weight by the periodic Villain weight `prod_p phi_beta((d_1 theta)_p)` of `gap-tu-retry.md` (1) (READ lines 67-81), at a fixed `beta >= 2^14`. Step (S1) holds verbatim: the U(1) gauge group acts by translations, which are isometries; tree gauge fixing, the Haar computation and (A1) use nothing else. Step (S2) holds at this fixed beta: the one-link conditional density is a product of six factors `phi_beta(+-theta_e + c_p)`, and `phi_beta > 0` is smooth, so its log-oscillation is at most `6 osc(log phi_beta) < infinity`; the Holley-Stroock comparison with the Haar circle gap 1 (READ `gap-tu-retry.md` lines 372-379) gives a positive constant `c_V(beta)` uniform in the exterior. Lemma W(c) needs only a chord Dobrushin hypothesis (8) on the circle; its proof does not use the sphere. Therefore, if for some sequence of tori `M_j -> infinity` there were forests and weights with optimal Villain chord influences satisfying (A3) with one `alpha < 1`, Lemma S and Lemma W would give `gamma_V(beta; M_j) >= c_V(beta) (1 - alpha) > 0` for all j. Theorem V of `gap-tu-retry.md` (READ (4), line 95; check `gap-tu-check-opus.md` item 4, HOLDS) says `gamma_V(beta; M) -> 0`. So for every `alpha < 1`, only finitely many cubic tori `(Z/M)^4` admit a forest and weights satisfying (A3). The argument fails for Villain at the named step (S4), and the SU(2) input that makes (S4) true at small beta is (S3).

**ARGUED (mechanism).** At the exterior with all six staple angles 0, the Villain conditional law is proportional to `phi_beta(theta)^6`, close to a centered Gaussian of variance `1/(6 beta)`. Moving one neighbour by s moves one factor's centre by s and the conditional mean by about `s/6`. So the optimal chord influence of one neighbour tends to `1/6`, not to `beta/4`, as beta grows; with the slice counts of at least 12 the weighted row sum is about 2. For Wilson SU(2) the same quantity is `beta/4` per neighbour for every exterior, which is small exactly in the strong-coupling range.

**READ (the new Codex controls).** Route C of `gap-shape-exercise-astra.md` fails for U(1) because the bracket source of (C2) vanishes (lines 607-610). The ceiling (A7) concerns the SU(2) Wilson Hessian and plays no role in the Villain test.

## 7. Toward order one: what the suggested ideas give, and what is missing

### 7.1 Block conditioning

**PROVED (exact block identity).** For a partition of the links into blocks B, with `L_B = sum_{e in B} L_e`,

    Q(f) = sum_B mu((L_B f)^2) + sum_{B != B'} sum_{e in B, j in B'} [ mu(||grad_j grad_e f||_HS^2) + C_ej ],    C_ej = mu(Hess_ej S(grad_e f, grad_j f)).      (A8)

*Proof.* Expand `(sum_B L_B f)^2`. For `e != j`, integrate by parts in e: `mu(L_e f L_j f) = mu(<grad_e f, grad_e L_j f>)`. In left-invariant frames `Y_e^a` commutes with `Y_j^b` and with the j-Laplacian, so `grad_e L_j f = L_j(grad_e f) + Hess_ej S(., grad_j f)`, and `mu(Y_e^a f L_j(Y_e^a f)) = mu(|grad_j Y_e^a f|^2)`. Summing gives the bracket. This is the computation behind (C5) of `gap-shape-exercise-astra.md` (READ), with blocks in place of links. QED.

**ARGUED (why blocks alone do not move the interval).** Inside a block, the mixed terms are indeed paid by the block's own conditional Bochner identity: `mu((L_B f)^2) >= gamma_B mu(|grad_B f|^2)`, with `gamma_B` the block gap uniform in the exterior. Two prices remain. First, `gamma_B` for a block of several links is itself an interacting finite-volume gap; the only exterior-uniform bounds available by hand are Holley-Stroock (exponentially small in the block size) or the same single-link Dobrushin argument inside the block. Second, the block-boundary terms in (A8) are still bounded pointwise. For the full mixed form Section 5 shows that no pointwise bound beats `14 beta`; for the boundary part alone the best constant depends on the partition and is not computed here. A block route therefore needs a block influence estimate (Dobrushin-Shlosman type) proved by hand, or an integrated bound on the boundary terms. Neither is supplied here.

### 7.2 Specific heat and slow modes

**PROVED (a specific-heat bound from Theorem A).** By (25) of `gap-gamma2-astra.md` (READ lines 546-562; check item 8), a uniform invariant gap `lambda_*` gives `p''_Lambda(beta) <= 12 p'_Lambda(beta) / (beta lambda_*)`. With Theorem A, for `0 < beta < 1/4` and every torus with a period at least 3,

    p''_Lambda(beta) <= 6 p'_Lambda(beta) / (beta (1 - 4 beta)).

This is a necessary consequence, not new evidence at order one.

**ARGUED (no slow mode is constructed).** No gauge-invariant family with Rayleigh quotient tending to 0 is constructed at any beta. The configurations (A7) are thin center-flux configurations with two thirds of the plaquettes at `q_p = -1`; their neighbourhoods have `mu_beta`-probability exponentially small in the volume, so they obstruct only pointwise estimates and do not by themselves give slow modes. The plaquette test and the energy test of `gap-gamma2-astra.md` 5.3 (READ) give no slow family. Standard lattice literature reports no bulk transition for the SU(2) Wilson action, only a crossover near beta of about 2.2 in this normalization; this is context, not an input, and it makes a counterexample at order one unlikely.

### 7.3 The weakest sufficient statement reached, and the exact missing statement

**PROVED (sufficient).** By Lemma S, a uniform invariant Langevin gap on an interval follows from a uniform Poincare inequality for some family of slice laws `mu_{F_Lambda}`. By Lemma W, that in turn follows from the weighted row-sum condition (A3) for their chord influences. Theorems A and B verify (A3) for `beta < 1/4` (all tori) and `beta < 8/27` (periods in `82 Z`; `0.2996...` with optimal two-level weights).

**PROVED (limits of the two pointwise mechanisms).** (i) Condition (A3) with worst-exterior single-link chord influences fails for `beta >= 1/3` on every forest without plaquettes containing three forest links (Section 4). (ii) Any Bochner route that bounds `C_m` by a pointwise operator bound on the mixed Hessian loses at least `14 beta E` (Section 5); with the reserves of D1 and (C4) it cannot pass `33/112`.

**OPEN (the missing estimate at order one).** For beta in an order-one interval, neither (G2), nor its rewrite (27), nor a uniform Poincare inequality for slice laws is proved. What is missing is an estimate of a different type from both pointwise mechanisms: either a hand-proved block contraction for the slice laws (influences of block boundaries on block laws, in a metric for which a weighted row sum stays below 1), or an integrated bound on `C_m` that uses the rarity of configurations near (A7) against the test-function weight `|grad f|^2` (the remark of `gap-gamma2-astra.md` lines 594-596, recorded in its check as a heuristic, item 8, is exactly the obstacle such a bound must overcome). Whether forests with plaquettes containing three forest links can beat `1/3` is not settled; the counting in Section 4 suggests they cannot (ARGUED).

### 7.4 The mechanisms side by side

| mechanism | price per neighbour | weighted count | interval | status |
|---|---|---|---|---|
| chord Dobrushin, full lattice (`gap-gamma2-astra.md` (15)) | `beta/4` | 18 | `beta < 2/9` | READ, checked |
| Bochner, D1 + (C4) + `C_m >= -18 beta E` (Route C) | `8 beta/33` | 18 | `beta < 11/48`, periods `>= 4` | READ, not checked |
| slice chord Dobrushin, axial forest (Theorem A) | `beta/4` | 16 | `beta < 1/4`, every torus | PROVED here |
| slice chord Dobrushin, perfect code (Theorem B) | `beta/4` | `27/2` (or `6 + 3 sqrt 6`) | `beta < 8/27` (or `0.2996...`), periods in `82 Z` | PROVED here |
| any forest, single-link worst exterior | `beta/4` (attained) | `> 12` | never `beta >= 1/3` | PROVED here (ceiling) |
| Bochner with pointwise `C_m` and D1 + (C4) | `c_* >= 14` | | never past `33/112` | PROVED here (ceiling); GUIDE: `c_* = 14` |

## 8. Summary of statements

- **PROVED** Lemma S (Section 1): for every forest F, `gamma_inv(beta, Lambda) >= gamma(mu_F)`; the slice laws have von Mises-Fisher one-link kernels with influences `beta n^F_ek / 4`.
- **PROVED** Lemma W (Section 2): weighted chord Dobrushin gives `sum_e mu(Var_e f) >= (1 - alpha) Var f`, hence `E >= c (1 - alpha) Var`.
- **PROVED** Theorem A (Section 3): `gamma_inv >= 2(1 - 4 beta)` for `0 <= beta < 1/4` on every torus with a period at least 3; `(Z/2)^4` has a positive gap (Holley-Stroock). So (G2) and (27) hold on every `[0, b_+]`, `b_+ < 1/4`, uniformly over all periodic tori; at `b_+ = 6/25`, `theta = 145/146`, `kappa = 1/25`.
- **PROVED** Lemma P and Theorem B (Section 4): a perfect plaquette code on even tori; with the defect set `Gamma` mod 82, `gamma_inv >= 2(1 - 27 beta/8)` for `beta < 8/27` on tori with all periods in `82 Z`, and the interval `beta < (2/3)(sqrt 6 - 2) = 0.2996...` with optimal weights; at `b_+ = 2/7`, `theta = 193/194`, `kappa = 1/28`.
- **PROVED** ceilings: the slice single-link chord Dobrushin condition fails for `beta >= 1/3` on every forest without plaquettes holding three forest links; the mixed Hessian has `c_* >= 14` on horizontal vectors at a center-flux configuration (A7), so a Bochner route with pointwise `C_m` and the D1 + (C4) reserves cannot pass `33/112`.
- **PROVED** binding test (Section 6): for periodic Villain U(1) at `beta >= 2^14`, steps (S1)-(S2) hold, so by Theorem V of `gap-tu-retry.md` the row-sum step (S4) must fail on all but finitely many tori.
- **READ, not checked:** Lemma D1 and Route C of `gap-shape-exercise-astra.md` (row 814, Codex gpt-6-astra). They are used only in brackets and in comparisons.
- **GUIDE:** axial weighted sums (16.0 on eight tori), the perfect code (exact cover on four tori), local defect ratios on `(Z/8)^4`, and the mixed-Hessian descent on `(Z/4)^4` (converges to `-14`).
- **ARGUED:** the slice method approaches but does not reach `1/3`; forests with three-forest-link plaquettes do not beat `1/3`; no slow mode is expected at order one.
- **OPEN:** an explicit defect set for every even torus (Theorem B for all even periods); `c_* <= 14`; (G2), equivalently (27), on an order-one interval.

Credits. Codex gpt-6-astra wrote `gap-gamma2-astra.md`, `gap-vmf-lip.md`, `gap-tu-retry.md` and `gap-shape-exercise-astra.md`, whose results are reused above as marked. Claude Opus 5.5 wrote the checks `gap-gamma2-check-opus.md`, `gap-vmf-lip-check-opus.md` and `gap-tu-check-opus.md`. The comparison method is Dobrushin's; the averaged update and its spectral consequence are from the Codex notes as checked. The tree-gauge slice is a standard device of lattice gauge theory; its use here to shorten Dobrushin neighbour counts was not found in the lane notes searched (`git grep` of `library/` for axial, temporal and tree gauge), and an outside literature search was not run: it should be queued before any outward use.

This note is an author proof by one model. It is not an independent check and not an audit.

RESULT: PROVED a volume-uniform gauge-invariant Langevin gap (so (G2) and (27) with explicit constants) for 0 <= beta < 1/4 on every periodic torus (gap >= 2(1-4beta) when some period is at least 3; (Z/2)^4 has its own positive bound) and for beta < 8/27 (0.2996 with optimal weights) on tori with all periods in 82Z, by a gauge-slice comparison plus weighted chord Dobrushin, beyond 2/9 and the unchecked 11/48; PROVED that this method cannot reach beta = 1/3 and that any pointwise bound on the mixed Hessian loses at least 14beta (so Route C with its reserves stops by 33/112); the argument fails for periodic Villain U(1) at beta >= 2^14 at the row-sum step; no slow mode constructed; order one remains OPEN.
