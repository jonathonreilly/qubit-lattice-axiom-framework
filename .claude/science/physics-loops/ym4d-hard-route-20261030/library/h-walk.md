lead: anthropic/claude-opus-5-5/max mac-mini-worker
lease_until: 2026-11-03T15:20Z

# h-walk: the walk expansion of chi_Y A chi_Y (outline statement 5, (1c.8)-(1c.9))

Queue row 115. Pinned at branch claude/ym4d-hard-route, commit c90e340cc. Same-model, ungated, research-stage working state. Written section by section.

Provenance: Anthropic Claude Opus 5.5 (`claude-opus-5-5`), effort max as configured for this worker (Mac mini); repository commit c90e340cc; Sussman–Alpoge outline `YM4_sketch_500.tex` at commit `31a47c543775`, fetched by URL into a scratch folder (SHA-256 d7f77d4d…b6f, as recorded in `sa-2.8.md`) and not committed; SA nnnn below are its line numbers. Balaban CMP 95, 96, 99 (389-434) read from `~/ym4d-papers/` (OCR, outside git). Research text by one model, not an audit and not a gate; it grants no status. No step rests on a computation. No numerical job was run, so the numeric lock was not needed. No subagent.

**Credit.** The statement (statement 5, SA 10302-10340), the operators (SA 10142-10208), the walk vocabulary (SA 10210), the unfolding with auxiliary unknowns (mechanism (f), SA 10540), the tree treatment of H^T J (mechanism (g), SA 10548), the multiplier (mechanism (h), SA 10550) and the consumer (SA 14108-14196) are Ethan Sussman and Levent Alpoge's outline, with Claude and Codex as authors of their text. Tadeusz Balaban supplies the method: generalized random-walk expansions from local inverses built on **cut-down sequences** around each cube (CMP 99b pp. 408-410, (3.87)-(3.94), Theorem 3.7, Corollary 3.8), the summation lemma (CMP 96 Lemma 2.1, (2.50)-(2.66)) and the walk-relative distance (CMP 99b (3.93)); CMP 95 Proposition 1.2 is the one-region prototype. The global operator bounds used as inputs are Claude's `a2-layers.md` §7 with Codex's repairs in `gates/a2-layers-gate.md`, resting on Codex's `a2-curved.md` §8 as gated in `gates/a2-curved-gate.md`. The parametrix lemma template is `path_expansion_locality.md` Lemma 1 (Claude, after Dimock arXiv:1108.1335 §2.4). The local saddle system and its commutator estimates are Codex's `flat-port.md` §§8-11, gated in `gates/flat-port-gate.md`.

## 0. Disposition (provisional; final in §10)

In progress.

## 1. The statement attacked, and what its consumer reads

**Setting** (SA 10106-10208; `a2-layers.md` §1). L is odd; M_1 and R_1 are powers of L; rho = R_1 M_1. The sequence (Omega_j)_{j<=k+1} is separated: each Omega_j is a union of level-j M_1-cubes, and dist(Omega_j^c, Omega_{j+1}) > rho xi_j. The layers L_j, tops (pillars) y with scale xi_y, rows c (interior and outward, with inward bonds omitted) and the layer metric d_B are the outline's. Pairings are physical and bilinear: eta^4 per fine bond or site, xi_y^4 per top, xi_c^4 per row. A regular pair P = (U_c, J) has U_c = e^{i eta A'}U with U real, and an independent current J, with radii (alpha_0, alpha_1, gamma_0) (SA 10128-10137). The operators G', R, S, G_0, G, H, G_1, H_1, Delta_k and

    A = C_V^T (G^(2)_V + Delta_k) C_V,    Delta_k = (Q G_1 Q^T)^{-1} - a - E^(2)[H_1^T J]

are SA 10142-10206. A acts on the free (non-pivot) level-k coordinates of the bonds of T^(k) that touch Omega_{k+1}. Its kernels are taken in counting measure (xi_k = 1).

**Walks** (SA 10210). A cell is a union of O(1) cubes of side O(M_1 xi_j) in two consecutive layers. In a walk, consecutive cells overlap. In a tree walk, each cell overlaps an earlier one, its parent. The hull [[omega]] enlarges the walk by O(M_1) local units, and the carrier is [omega] = [[omega]] ∩ Omega_0. d_B(omega; y, y') is the least weighted length of a tree that passes through y and y' and meets the cells X_1, ..., X_m. It need not meet X_0.

**Statement 5 for chi_Y A chi_Y** (SA 10309, 10318-10340), unpacked into clauses:

- (S1) chi_Y A chi_Y = sum_omega A_omega over tree walks, with at most C^m tree walks of length m from a given first cell (SA 10548).
- (S2) |A_omega(b, b')| <= C_A (C M_1^{-1/2})^{|omega|} M_1^{-|omega|/2} e^{-delta_0 d_B(omega; b, b')}. Here C_A e^{-delta_0 d(b,b')} is "the kernel bound that 6 states for C^(k)(Y)". The outline names statement 6 but does not state it; I read it as a kernel bound in counting measure.
- (S3) Each A_omega is holomorphic on the local class on [omega]. It depends on the regions only through their traces on [[omega]]. It is gauge covariant and real at real pairs. It is the same function for two sequences, tori or cutoffs that a translation in M_1 xi_{k+1} Z^4 carrying Omega_{k+1} and Y relates on the hull. Single terms are covariant under the isometries that preserve the level-(k+1) M_1-cubes.
- (S4) All this holds at the pairs regular for the longer sequence (Omega_j)_{j<=k+1}, under a ceiling on the radii fixed before M_1, for M_1 and R_1 large, with constants depending only on L.

**The consumer.** `a2-full.md` Theorem VI and SA 14158-14196 read (S1) with the count, (S2), mechanism (i) with delta_0 >= 2C kappa-bar/l_P, holomorphy of A_omega on the class (for complex regular pairs), and A(s) := sum_omega s^omega A_omega. Nothing else of statement 5 is read there.

**What is proved here** (Theorem H, §8), as an implication. The inputs are named in §5:

- (S1) holds with the count.
- (S2) holds with M_1^{-1/3} per cell, that is (C M_1^{-1/6})^{|omega|} M_1^{-|omega|/6} in the outline's two-factor form, and with a rate delta_h(L) independent of M_1.
- (S3) holds with the hull O(M_1) local units. Covariance is under the subgroup that leaves A itself covariant (defect D1, §2.1). Every term coming from Delta_k is fully covariant.
- (S4) holds as stated.

Theorem VI goes through with this exponent (§9).

## 2. Counterexample tests (done before the proofs)

**2.1 Full gauge covariance of the terms is impossible (wording defect D1).** A sum of covariant terms is covariant, and A is not covariant. G^(2)_V is the Hessian of GF_k(V) = sum_{y,x}[1 - (1/2) Re tr V(y,x)] (SA 7182), and GF(V^u) = sum[1 - (1/2) Re tr u(y) V(y,x) u(x)^{-1}]. Take V = 1 on one level-(k+1) block, and u = 1 except u(x) = e^{i eps T} at one non-centre point x. Along e^{iB}V^u the summand at (y, x) is 1 - (1/2) Re tr(e^{i gamma} e^{-i eps T}) with gamma = gamma_{y,x}(B). Its first-order term (1/2) eps tr(gamma T) + O(eps^2) is non-zero, and its second-order term differs from that at V by O(eps^2). So G^(2)_{V^u} is not the conjugate of G^(2)_V (this is `a2-full.md` §10 defect 5 made explicit). No expansion of A has every term gauge covariant. **Repair:** covariance under gauge transformations whose level-k action is constant on each level-(k+1) block of the mask. Every term from Delta_k, C_V and E^(2) is covariant under the full group (§8).

**2.2 Global coefficients in local models destroy locality (a route killed, not the statement).** Take the parametrix of G_1^{-1} itself, with local models G_{1,kappa}^{-1}. Its remainder contains h~_kappa (G_1^{-1} - G_{1,kappa}^{-1}) G_{1,kappa} theta_kappa. G_1^{-1} contains D R D^T, Delta'_pi[J] and S^T Delta^(2)[H^T J] S, and R, lambda_A and H^T J read the whole configuration. So every term of that expansion reads the whole field, and (S3) fails for it. This is `flat-port.md` §11's remark about inserting the global P, extended to the curved operators. Exact agreement of the local models with the global system near the cutoffs needs a finite-range system: the unfolding of mechanism (f), §4.

**2.3 Trees lose part of the M_1 power.** A vertex of the H^T J expansion (mechanism (g)) is a coefficient perturbation, not a commutator. Take the tree term G_{1,loc} V_beta G_{1,loc}, where V_beta carries a walk beta of H of length one. Its trunk has two cubes and its branch two cells, so it has three steps and one factor M_1^{-1}. Along this route a tree of length m carries M_1^{-m/3}, not M_1^{-m} (§7). This is not a counterexample: the decomposition is not unique, and its terms have no lower bounds. The consumers need only a geometric factor with a reserve (§9).

**2.4 A rate independent of M_1 needs chained local decay.** Suppose only the norm of the sum of walk terms of length n is bounded, by (C/M_1)^n, as in `flat-port.md` (8.9)-(8.11). A term of length n can connect points at d_B-distance about n M_1. Then e^{-delta d} <= (C/M_1)^n forces delta <= log(M_1/C)/M_1, and the rate degenerates as M_1 grows. Balaban's chaining (CMP 99b (3.91)-(3.94); CMP 96 (2.52)-(2.66)) pays each leg by the local inverse's own decay. That rate is set by L. §6 does this.

**2.5 Periodized local models in a chosen gauge break single-term covariance.** The small real gauge on a cube is not unique: two choices differ by a non-constant u near the cut-off zone, where a periodized configuration does not transform covariantly. Balaban's cut-down sequences (CMP 99b p. 408) need no gauge choice. The local model is the same operator for a smaller separated sequence. §3 uses them.

**2.6 Dirichlet faces finer than the blocks** (mechanism (b), SA 10506) would cost powers of eta^{-1}. In a cut-down sequence every artificial boundary lies in its bare layer, a collar of width rho' eta. Dirichlet conditions are imposed only there.

**2.7 The scalar second-order block.** The unfolding needs the variable lambda in a norm that controls A_s lambda, because the term D R D^T enters as <D^T A, A_s lambda>. With the full second differences sum ||D_a D_b lambda||^2 (`flat-port.md` (8.3)) this needs elliptic regularity, which fails uniformly at re-entrant Dirichlet corners. The graph norm of A_s avoids it. Conjugating A_s by a merely Lipschitz weight in that norm is not O(tau): across one fine bond the error is about tau |lambda|/(eta xi), which the norm does not control. So the unfolded system is not conjugated as a whole. Its decay is derived from its block formula and the gated conjugation bounds of the individual operators (Lemma L, §5).

**2.8 The Haar mean and the Montel limit of mechanism (i) (SA 10560) are not needed.** The terms built here are canonical: two sequences or tori with room that agree on a hull, up to a grid translation, give literally the same local matrices and cutoffs (§3 (C5), §8).

No counterexample to a consumed statement was found. Tests 2.1 and 2.3 change the wording of (S2)-(S3). Tests 2.2 and 2.4-2.7 fix the route.

## 3. Geometry: cubes, cutoffs, boxes and cut-down sequences

Work with the depth-k sequence (Omega_j)_{j<=k} of the step. The longer sequence enters only in §8. Fix the thresholds of the global theory, `a2-layers.md` §7.5 with `gates/a2-layers-gate.md` §§4-5: a cube size M' and a gap rho', both powers of L, with M' >= M_*(L), rho' >= rho_*(L) and tau_0 rho' >= 16 log L. They depend on L only. Let r_0 = r_0(L) be the d_B-range of all local operators in §4. Every pillar, row carrier and plaquette has d_B-diameter <= 4L (`a2-layers.md` 5.1), and r_0 <= 8L suffices. Assume

    (G0)  R_1 >= 64 L,   M_1 >= M_C(L) := 16 L (rho' + 4M' + 16 L r_0).

**Cubes.** Let K_j be the level-j M_1-cubes (closed, side M_1 xi_j, on the grid M_1 xi_j Z^4) contained in the closure of L_j, and K = union of the K_j. Since Omega_{j+1} is a union of level-(j+1) M_1-cubes, and each of these is a union of L^4 level-j M_1-cubes, the K_j tile L_j, and K covers Omega_0. For kappa in K_j write xi_kappa = xi_j. Let kappa^(t) be the concentric closed cube of side (1 + 2t) M_1 xi_kappa. Cells are the boxes X_kappa := kappa^(3).

*Two layers.* kappa^(4) has side 9 M_1 xi_j and meets at most two consecutive layers. Indeed L_j separates L_{j-1} from L_{j+1} by width > rho xi_j >= 64 L M_1 xi_j. Also Omega_{j+2} is at distance > rho xi_{j+1} from L_j, and Omega_{j-1}^c is at distance > rho xi_{j-1} >= 64 M_1 xi_j from Omega_j (R_1 >= 64L). So near kappa the local scale takes at most two values, xi_kappa and xi_kappa L^{±1}.

**Cutoffs.** Fix smooth even profiles p, q: R -> [0,1] with p = 1 on [-1/2, 1/2], p = 0 off [-3/4, 3/4], q = 1 on [-3/2, 3/2] and q = 0 off [-5/2, 5/2]. Let c_kappa be the centre of kappa. Put phi_kappa(x) = prod_mu p((x_mu - c_mu)/(M_1 xi_kappa)), theta_kappa = phi_kappa / sum_{kappa'} phi_{kappa'} and h~_kappa(x) = prod_mu q((x_mu - c_mu)/(M_1 xi_kappa)). The denominator is >= 1, because every point lies in some kappa', where phi_{kappa'} = 1. A function on cubes is applied to a variable at its base point: the initial point of a bond, the site, the top, or the initial point of a row (the convention of `flat-port.md` §8.2). Then:

- (c1) sum_kappa theta_kappa = 1 on every component; supp theta_kappa ⊂ kappa^(1/4); h~_kappa = 1 on kappa^(1); supp h~_kappa ⊂ kappa^(2) ⊂ X_kappa.
- (c2) |f(x) - f(x')| <= C_p |x - x'|_inf / (M_1 xi_kappa) and |second difference of f| <= C_p eta^2/(M_1 xi_kappa)^2 for f = theta_kappa, h~_kappa. Near kappa a fine bond has d_B-length eta/xi with xi in {xi_kappa, L xi_kappa, xi_kappa/L}. So both cutoffs change by at most C_p L/M_1 per unit of d_B, and by at most C_p L eta/(M_1 xi) across a fine bond of scale xi.
- (c3) The r_0-neighbourhood (in d_B) of kappa^(1/4) lies in kappa^(1), and that of kappa^(2) lies in kappa^(5/2). Indeed d_B-distance r_0 is physical distance <= r_0 L xi_kappa, and M_1 >= 16 L r_0.
- (c4) Bounded overlap: a point lies in at most nu_0 = nu_0(L) boxes X_kappa (cubes of at most three levels, side ratio L), and a box meets at most nu_1 = nu_1(L) other boxes.

A walk is a sequence omega = (kappa_0, ..., kappa_n) with X_{kappa_{i-1}} ∩ X_{kappa_i} ≠ ∅. By (c4) at most nu_1^n walks of length n start at a given cube.

**Lemma C (cut-down sequences; after Balaban CMP 99b p. 408).** For kappa in K, let i_0 be the least i with kappa^(4) ∩ L_i ≠ ∅, and i_1 the largest i with kappa^(4) ∩ Omega_i ≠ ∅; then i_1 <= i_0 + 1. Let C_{i_1} be the smallest union of level-i_1 M'-cubes containing kappa^(7/2). For i = i_1, ..., 1, let C_{i-1} be the cube concentric with C_i whose half-side is larger by (rho' + 2M') xi_{i-1}, rounded outward to the level-(i-1) M'-grid. Put Omega^kappa_i = Omega_i ∩ C_i for i <= i_1 and Omega^kappa_i = ∅ for i > i_1. Then:

- (C1) (Omega^kappa_i) is separated with cube size M' and gap rho', and lies in C_0 ⊂ kappa^(4).
- (C2) Omega^kappa_i ∩ kappa^(7/2) = Omega_i ∩ kappa^(7/2) for every i. So on X_kappa enlarged by r_0 (inside kappa^(7/2) by (c3)) the two sequences have the same layers, tops, pillars, rows, omitted inward bonds and inner plaquettes.
- (C3) The cut-down layer index of a point is at most its original index. So the d_B-density of the cut-down is >= the original one, d^kappa_B >= d_B, with equality of densities on kappa^(7/2).
- (C4) Let P be a regular pair for (Omega_j)_{j<=k}, with radii (alpha_0, alpha_1, gamma_0) and the gauge clause on cubes of side <= c_g M_1 xi_j in L_j ∪ L_{j+1}. Its restriction to Omega^kappa_0 is a regular pair for (Omega^kappa_i) with the same radii and the gauge clause for cube size M'. The same holds for the local class on a set containing kappa^(4).
- (C5) C_i, Omega^kappa, theta_kappa and h~_kappa are determined by kappa and the sets Omega_i ∩ kappa^(4). A translation in M_1 xi_k Z^4 maps every level-j grid (j <= k) to itself, so if it maps these sets for kappa onto those for kappa', it maps every object above for kappa onto that for kappa'.

*Proof.* The grids nest (L M' xi_{i-1} = M' xi_i, and M' divides M_1), so Omega_i, a union of level-i M_1-cubes, is a union of level-i M'-cubes. An intersection of two unions of cubes of one grid is again such a union. Nesting: Omega_{i+1} ∩ C_{i+1} ⊂ Omega_i ∩ C_i. *Separation (C1):* (Omega^kappa_i)^c = Omega_i^c ∪ C_i^c. Also dist(Omega_i^c, Omega^kappa_{i+1}) >= dist(Omega_i^c, Omega_{i+1}) > rho xi_i >= rho' xi_i, and dist(C_i^c, C_{i+1}) >= (rho' + M') xi_i. *Size:* the half-side of C_0 exceeds that of kappa^(7/2) by at most M' xi_{i_1} + sum_{i<i_1} (rho' + 3M') xi_i <= 2 L (rho' + 4M') xi_kappa <= M_1 xi_kappa / 2. Here xi_{i_1} <= L xi_kappa and M_1 >= M_C. So C_0 ⊂ kappa^(4). *(C2):* for i <= i_1, C_i ⊃ C_{i_1} ⊃ kappa^(7/2). For i > i_1, both sides are empty by the choice of i_1. The listed combinatorial objects at x are determined by the sets Omega_i within one pillar or row carrier of x, which is d_B-distance <= 4L. *(C3):* x in Omega^kappa_i implies x in Omega_i. Outside Omega^kappa_0 the cut-down counts length in the bare unit, which is the largest density.

*(C4).* Pointwise clauses: at x in the cut-down layer i and the original layer i' >= i, |dU - 1| < alpha_0 eta^2 xi_{i'}^{-2} <= alpha_0 eta^2 xi_i^{-2}, xi_i |A'| <= xi_{i'}|A'| < alpha_1, likewise for nabla A', and |J| < gamma_0 xi_{i'}^{-3} <= gamma_0 xi_i^{-3}. Gauge clause: let Q be a cube of side <= c_g M' xi_i inside the cut-down L^kappa_i ∪ L^kappa_{i+1}. By the choice of i_0, kappa^(4) ∩ Omega_0 ⊂ Omega_{i_0}, and kappa^(4) misses Omega_{i_0+2}. So Omega^kappa_0 ⊂ L_{i_0} ∪ L_{i_0+1}, and every such Q lies there. For i = i_1, Q ⊂ Omega_{i_1} ∩ C_{i_1} ⊂ L_{i_1}, of side <= c_g M_1 xi_{i_1}: the original clause at level i_1 applies. For i <= i_0, Q ⊂ L_{i_0} ∪ L_{i_0+1}, of side <= c_g M' xi_i <= c_g M_1 xi_{i_0}. The original clause at level i_0 gives a real gauge with xi_{i_0}|A|, xi_{i_0}^2 |nabla A| <= alpha_0 on Q, so the same holds with xi_i <= xi_{i_0}. *(C5)* holds by construction. ∎

So every local model below is an instance of the global theory, on a separated sequence of its own, with no gauge choice and no Dirichlet face finer than the blocks. Its constants are those of `a2-layers.md` §7 at (M', rho'). They depend on L only, not on M_1.

## 4. The unfolded systems (Lemma U; mechanisms (f), (h))

Fix a separated sequence S (the actual one, or a cut-down), a regular pair P = (U_c, J), and a row function j, the *coefficient*. The G-stage has j = 0. The G_1-stage has j = H^T J, or a local part of it (§7). Write m for the local scale (xi_b on bonds, xi_x on sites, xi_y on tops, xi_c on rows), D = D_{U_c}, and A_s = G'^{-1} = Delta_U + Q'^T a Q'.

**Spaces.** In each of the following, ||.|| is the physical L^2 norm of the displayed integrand.

- A: 1-forms on the bonds of Omega_0, with ||A||_E^2 = ||nabla_U A||^2 + ||m^{-1} A||^2. This is the X norm of `a2-layers.md` §1.
- Y = (h, lambda, mu): two site functions and a top function, with ||Y||_Y^2 = ||h||^2 + ||lambda||_Lambda^2 + ||m^2 mu||_top^2. Here ||lambda||_Lambda^2 = ||m^{-2} lambda||^2 + ||m^{-1} D lambda||^2 + ||A_s lambda||^2 is the graph norm (§2.7).
- Z = (h', lambda', mu'): an adjoint copy, in the same space.
- nu: a row function, with ||nu||_{row*}^2 = sum_c xi_c^6 |nu_c|^2.

Let 𝒳 = E ⊕ Y ⊕ Y ⊕ row* and let 𝒳* be its dual under the bilinear pairing. All four parts have the scaling of ||A||_E, as in `flat-port.md` (8.3). Every integrand has a base point, so ||Psi||_𝒳^2 = sum_y ||Psi||_{𝒳,y}^2. Here ||Psi||_{𝒳,y} is the norm restricted to the integrand terms based in pillar y, the *local norm at y*. A dual vector F is *supported near z* if <F, Psi> = 0 whenever Psi vanishes within r_0 of z.

**Local operators.** All have d_B-range <= r_0. Their coefficients are holomorphic in P and affine in (J, j).

- The scalar system X(h, lambda, mu) = (h + A_s lambda, A_s h - Q'^T mu, -Q' lambda). It is symmetric:
  <Y'', X Y> = <h'', h> + <h'', A_s lambda> + <lambda'', A_s h> - <lambda'', Q'^T mu> - <mu'', Q' lambda>.
- B A = (D^T A, 0, 0), and Pi Y = lambda.
- The local quadratic form on pairs (A, lambda):

      q((A, lambda)) = <A, (Delta^W + Q^T a Q) A> + <D^T A, A_s lambda> - c_J(A, lambda) - <A - D lambda, Delta^(2)[j] (A - D lambda)>,
      c_J(A, lambda) = < i[lambda, A] - i[A, lambda^+] - i[lambda, D lambda], J >_f.

  c_J is the quadratic form of SA's explicit current continuation (eq. ym4:explicit-current-continuation) at C = A, with lambda in place of lambda_A. Its polarization defines the blocks q_AA, q_Aλ, q_λA = q_Aλ^T and q_λλ.

The **unfolded system** K = K[S, P, j]: 𝒳 → 𝒳* is symmetric. Its rows are

    A:   q_AA A + q_Aλ Pi Y - B^T Z + Q^T nu
    Y:   Pi^T q_λA A + Pi^T q_λλ Pi Y + X Z
    Z:   -B A + X Y
    nu:  Q A

Its unknowns are Psi = (A; h, lambda, mu; h', lambda', mu'; nu), the eight of mechanism (f).

**Lemma U.** Suppose G' = A_s^{-1}, N = (Q' G'^2 Q'^T)^{-1}, T and W = Q T^{-1} Q^T exist. Here L = Pi X^{-1} B and T = q_AA + q_Aλ L + L^T q_λA + L^T q_λλ L. Then:

- (a) X is invertible, and Pi X^{-1}(s, 0, 0) = G' R s. Hence L A = G' R D^T A = lambda_A of SA 10175.
- (b) T = G^{-1} = G_0^{-1} - Delta'_pi[J] when j = 0. In general T = G_1^{-1}[j] := G^{-1} - S^T Delta^(2)[j] S, so T = G_1^{-1} at j = H^T J.
- (c) K is invertible, with [K^{-1}]_{νν} = -W^{-1}, [K^{-1}]_{Aν} = T^{-1} Q^T W^{-1}, [K^{-1}]_{AA} = T^{-1} - T^{-1} Q^T W^{-1} Q T^{-1}. So at j = 0, H = [K^{-1}]_{Aν} and (Q G Q^T)^{-1} = -[K^{-1}]_{νν}. At j = H^T J the same blocks give H_1 and (Q G_1 Q^T)^{-1}.
- (d) For a source F = (f; g; g'; f_ν), the solution of K Psi = F is

      Y = X^{-1}(g' + B A),   Z = X^{-1}(g - Pi^T q_λA A - Pi^T q_λλ Pi Y),
      f~ = f + B^T X^{-1} g - (q_Aλ + L^T q_λλ) Pi X^{-1} g',                   (4.1)
      nu = W^{-1}(Q T^{-1} f~ - f_ν),   A = T^{-1}(f~ - Q^T nu),

  and X^{-1}(s_h, s_λ, s_μ) = (h, lambda, mu) with

      mu = N(Q' G' s_h + s_μ - Q' G'^2 s_λ),   h = G'(s_λ + Q'^T mu),   lambda = G'(s_h - h).      (4.2)

*Proof.* (4.2) solves X(h, lambda, mu) = (s_h, s_λ, s_μ). Indeed h + A_s lambda = s_h, and A_s h - Q'^T mu = s_λ. Also -Q' lambda = -Q' G' s_h + Q' G'^2 (s_λ + Q'^T mu) = -Q' G' s_h + Q' G'^2 s_λ + N^{-1} mu = s_μ. The spaces are finite-dimensional, so X is invertible. With (s, 0, 0): mu = N Q' G' s and h = G' Q'^T N Q' G' s = (1 - R) s. So lambda = G' R s, with R = 1 - G' Q'^T N Q' G' as in SA 10142. This proves (a).

For (b): A_s lambda_A = R D^T A. So <D^T A, A_s lambda_A> = <D^T A, R D^T A> = <A, D R D^T A>; R is symmetric for the site pairing, since R = 1 - T_0^T (T_0 T_0^T)^{-1} T_0 with T_0 = Q' G'. Next, c_J(A, lambda_A) = <A, Delta'_pi[J] A> by the outline's formula at C = A, and A - D lambda_A = S A. Hence q((A, L A)) = <A, (Delta^W + D R D^T + Q^T a Q - Delta'_pi[J] - S^T Delta^(2)[j] S) A>. T is the symmetric operator of the quadratic form A -> q((A, L A)), and symmetric bilinear forms are determined by their quadratic forms.

For (d): the Z-row gives Y. The Y-row gives Z, since X^T = X. Substitute both into the A-row, using Pi Y = Pi X^{-1} g' + L A and B^T X^{-1} Pi^T = (Pi X^{-1} B)^T = L^T:

    T A + Q^T nu = f~,

with f~ as in (4.1). The nu-row gives Q A = f_ν, which yields nu and A. The blocks in (c) are read off from (4.1) at g = g' = 0. ∎

The existence of G', N, G, G_1[j] and W, W_1[j] at the pairs used is `a2-layers.md` (7.3), §7.2(ii), (iv), §7.4, and §7.6 for complex pairs. The coefficient j is arbitrary there, subject to the bound sup xi^3 |j| <= gamma_j: the proof of 7.4 reads only that bound, through `a2-curved.md` (8.10). This supplies the hypotheses of Lemma U.
