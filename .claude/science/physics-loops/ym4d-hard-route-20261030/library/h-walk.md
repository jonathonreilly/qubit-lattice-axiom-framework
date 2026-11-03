lead: anthropic/claude-opus-5-5/max mac-mini-worker
lease_until: 2026-11-03T15:20Z

# h-walk: the walk expansion of chi_Y A chi_Y (outline statement 5, (1c.8)-(1c.9))

Queue row 115. Pinned at branch claude/ym4d-hard-route, commit c90e340cc. Same-model, ungated, research-stage working state. Written section by section.

Provenance: Anthropic Claude Opus 5.5 (`claude-opus-5-5`), effort max as configured for this worker (Mac mini); repository commit c90e340cc; Sussman–Alpoge outline `YM4_sketch_500.tex` at commit `31a47c543775`, fetched by URL into a scratch folder (SHA-256 d7f77d4d…b6f, as recorded in `sa-2.8.md`) and not committed; SA nnnn below are its line numbers. Balaban CMP 95, 96, 99 (389-434) read from `~/ym4d-papers/` (OCR, outside git). Research text by one model, not an audit and not a gate; it grants no status. No step rests on a computation. No numerical job was run, so the numeric lock was not needed. No subagent.

**Credit.** The statement (statement 5, SA 10302-10340), the operators (SA 10142-10208), the walk vocabulary (SA 10210), the unfolding with auxiliary unknowns (mechanism (f), SA 10540), the tree treatment of H^T J (mechanism (g), SA 10548), the multiplier (mechanism (h), SA 10550) and the consumer (SA 14108-14196) are Ethan Sussman and Levent Alpoge's outline, with Claude and Codex as authors of their text. Tadeusz Balaban supplies the method: generalized random-walk expansions from local inverses built on **cut-down sequences** around each cube (CMP 99b pp. 408-410, (3.87)-(3.94), Theorem 3.7, Corollary 3.8), the summation lemma (CMP 96 Lemma 2.1, (2.50)-(2.66)) and the walk-relative distance (CMP 99b (3.93)); CMP 95 Proposition 1.2 is the one-region prototype. The global operator bounds used as inputs are Claude's `a2-layers.md` §7 with Codex's repairs in `gates/a2-layers-gate.md`, resting on Codex's `a2-curved.md` §8 as gated in `gates/a2-curved-gate.md`. The parametrix lemma template is `path_expansion_locality.md` Lemma 1 (Claude, after Dimock arXiv:1108.1335 §2.4). The local saddle system and its commutator estimates are Codex's `flat-port.md` §§8-11, gated in `gates/flat-port-gate.md`.

## 0. Disposition

**Proved as an implication, with two clauses corrected (Theorem H, §8).** The outline's statement 5 for chi_Y A chi_Y holds at the pairs regular for the longer sequence, real or complex, with independent current. That is (H-walk), the only input of A2 item (3) (`a2-full.md` Theorem VI). The corrected clauses:

- A tree walk of length m carries M_1^{-m/3}, not M_1^{-m} (test 2.3).
- Single terms are gauge covariant only under the subgroup under which A itself is, because G^(2)_V breaks full covariance (test 2.1, defect D1).

The rate is independent of M_1, the hull is O(M_1) local units, and the terms are canonical. Theorem VI reads this form verbatim (§9).

**Route** (Balaban CMP 99b §C with the outline's mechanisms (f)-(h)):

- Unfold every non-local piece of A (R, lambda_A, Delta'_pi[J], S^T Delta^(2)[j] S and the row multiplier) into one symmetric finite-range system with eight unknowns. Its inverse has H, H_1, (QGQ^T)^{-1} and (QG_1Q^T)^{-1} as blocks (Lemma U).
- Take as local models the same system for Balaban's cut-down sequences. These are separated sequences of their own, with no gauge choice, so their inverse bounds are the gated global ones of `a2-layers.md` §7 (Lemmas C, L).
- Build the parametrix and chain the local decays to get walk terms with a rate independent of M_1 (Theorem W).
- Treat the non-local coefficient H^T J by vertices that carry walks of H, which gives trees (Theorem T).
- Assemble A (Theorem H).

**Inputs:** (I1) the gated conjugation package of `a2-layers.md` §7 (rows 92-93, with Codex's repairs); (I2) gauge covariance of the averaging maps (covariance clause only); (I3) the level-k local maps (gated `a2-curved.md` §5). No counterexample to a consumed statement was found. Open: a cross-provider gate (§10).

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

**Literature read for this item** (targeted, reusing `lit-balaban.md` and `lit-large-field.md` §3):

- Balaban CMP 95 Proposition 1.2 (pp. 35-37 of the OCR): the one-region random-walk representation of G from local inverses.
- CMP 96 §2.B, (2.37)-(2.67): G' from local inverses with Neumann conditions; the commutator remainder (2.38)-(2.39); the chaining (2.52)-(2.56); the summation Lemma 2.1; Proposition 2.2. Also (2.141), the two-scale expansion.
- CMP 99b §C, pp. 408-416: *cut-down sequences* Omega_n(□) around each cube, with gap 2R_0 M_0 L^n eta and walk cubes of size M = K R_0 M_0 (p. 408). Their operators satisfy the global theorems "correspondingly" and serve as local inverses. Also (3.87)-(3.90) and Theorem 3.7; the walk-relative distance and the per-walk bound (3.93)-(3.94), Corollary 3.8; the sequential expansions of (Q'G'^2Q'^*)^{-1} through comparison terms (3.95), Theorem 3.9; G_0 with the commutator of D R D^*, Theorem 3.10.

Balaban expands the operators one after another, inserting earlier expansions into comparison terms. This note unfolds them instead into one finite-range system (mechanism (f)), so that local models agree with the global system *exactly* near each cutoff. None of the papers read here treats an independent current, or the multiplier H^T J as a non-local coefficient, inside a walk expansion. CMP 99b takes J = J(U), and its Theorems 3.12-3.13 work on shell. CMP 116, which the outline cites for the decoupled expansions (SA 10552-10558), and the papers [11, 13] cited at CMP 119 l. 1617 are not in hand. Mechanism (g) is the outline's sketch of the tree treatment, and §7 carries it out.

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

Work with the depth-k sequence (Omega_j)_{j<=k} of the step. The longer sequence enters only in §8. Fix the thresholds of the global theory, `a2-layers.md` §7.5 with `gates/a2-layers-gate.md` §§4-5: a cube size M' and a gap rho', both powers of L, with M' >= M_*(L), rho' >= rho_*(L) (these include (4.0) of `a2-layers.md`) and tau_L rho' >= 256 log L, where tau_L := tau_0 2^{-25} is the rate of Lemma L (§5) and tau_0 = tau_0(L) is the conjugation threshold of `a2-layers.md` 7.2. They depend on L only. Let r_0 = r_0(L) be the d_B-range of all local operators in §4. Every pillar, row carrier and plaquette has d_B-diameter <= 4L (`a2-layers.md` 5.1), and r_0 <= 8L suffices. Assume

    (G0)  R_1 >= 64 L,   M_1 >= M_C(L) := 16 L (rho' + 4M' + 16 L r_0).

**Cubes.** Let K_j be the level-j M_1-cubes (closed, side M_1 xi_j, on the grid M_1 xi_j Z^4) contained in the closure of L_j, and K = union of the K_j. Since Omega_{j+1} is a union of level-(j+1) M_1-cubes, and each of these is a union of L^4 level-j M_1-cubes, the K_j tile L_j, and K covers Omega_0. For kappa in K_j write xi_kappa = xi_j. Let kappa^(t) be the concentric closed cube of side (1 + 2t) M_1 xi_kappa. Cells are the boxes X_kappa := kappa^(3).

*Two layers.* kappa^(4) has side 9 M_1 xi_j and meets at most two consecutive layers. Indeed L_j separates L_{j-1} from L_{j+1} by width > rho xi_j >= 64 L M_1 xi_j. Also Omega_{j+2} is at distance > rho xi_{j+1} from L_j, and Omega_{j-1}^c is at distance > rho xi_{j-1} >= 64 M_1 xi_j from Omega_j (R_1 >= 64L). So near kappa the local scale takes at most two values, xi_kappa and xi_kappa L^{±1}.

**Cutoffs.** Fix smooth even profiles p, q: R -> [0,1] with p = 1 on [-1/2, 1/2], p = 0 off [-3/4, 3/4], q = 1 on [-3/2, 3/2] and q = 0 off [-5/2, 5/2]. Let c_kappa be the centre of kappa. Put phi_kappa(x) = prod_mu p((x_mu - c_mu)/(M_1 xi_kappa)), theta_kappa = phi_kappa / sum_{kappa'} phi_{kappa'} and h~_kappa(x) = prod_mu q((x_mu - c_mu)/(M_1 xi_kappa)). The denominator is >= 1, because every point lies in some kappa', where phi_{kappa'} = 1. A function on cubes is applied to a variable at its base point: the initial point of a bond, the site, the top, or the initial point of a row (the convention of `flat-port.md` §8.2). Then:

- (c1) sum_kappa theta_kappa = 1 on every component; supp theta_kappa ⊂ kappa^(1/4); h~_kappa = 1 on kappa^(1); supp h~_kappa ⊂ kappa^(2) ⊂ X_kappa.
- (c2) |f(x) - f(x')| <= C_p |x - x'|_inf / (M_1 xi_kappa) and |second difference of f| <= C_p eta^2/(M_1 xi_kappa)^2 for f = theta_kappa, h~_kappa. Near kappa a fine bond has d_B-length eta/xi with xi in {xi_kappa, L xi_kappa, xi_kappa/L}. So both cutoffs change by at most C_p L/M_1 per unit of d_B, and by at most C_p L eta/(M_1 xi) across a fine bond of scale xi.
- (c3) The r_0-neighbourhood (in d_B) of kappa^(1/4) lies in kappa^(1), and that of kappa^(2) lies in kappa^(5/2). Indeed d_B-distance r_0 is physical distance <= r_0 L xi_kappa, and M_1 >= 16 L r_0.
- (c4) Bounded overlap: a point lies in at most nu_0 = nu_0(L) boxes X_kappa (cubes of at most three levels, side ratio L), and a box meets at most nu_1 = nu_1(L) other boxes.

A walk is a sequence omega = (kappa_0, ..., kappa_n) with X_{kappa_{i-1}} ∩ X_{kappa_i} ≠ ∅. By (c4) at most nu_1^n walks of length n start at a given cube.

**Lemma C (cut-down sequences; after Balaban CMP 99b p. 408).** For kappa in K, let i_0 be the least i with kappa^(4) ∩ L_i ≠ ∅, and i_1 the largest i with kappa^(4) ∩ Omega_i ≠ ∅; then i_1 <= i_0 + 1. Let C_{i_1} be the smallest union of level-i_1 M'-cubes containing kappa^(7/2). (It is a box, a product of intervals.) For i = i_1, ..., 1, let C_{i-1} be the box obtained from C_i by moving every face outward by (rho' + 2M') xi_{i-1}, then rounding outward to the level-(i-1) M'-grid. Put Omega^kappa_i = Omega_i ∩ C_i for i <= i_1 and Omega^kappa_i = ∅ for i > i_1. Then:

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

## 5. Local decay of the unfolded inverse (Lemmas D, P, S, K, L)

**Inputs.** (I1) is the conjugation package of `a2-layers.md` §7, with the repairs of `gates/a2-layers-gate.md` (§5 separation choice, §7 cap, items 2-5). It holds on every separated sequence with cube size >= M' and gap >= rho', at every regular pair below the ceiling a_*(L) (real: §§7.1-7.5; complex: §7.6(b)-(c), "the conjugation bounds of 7.2 hold at the complex pair with the same proofs"), and for every coefficient with sup xi^3 |j| <= gamma_j(L). It reads: for every tau-Lipschitz real weight theta (5.1 there) with tau <= tau_0(L),

- (i) ||e^θ G' e^{-θ}||_{V*->V} <= C, with ||lambda||_V^2 = ||m^{-1} lambda||^2 + ||D lambda||^2. In the scale-conjugated form (gate item 2), ||m^{-2} e^θ G' e^{-θ} g|| + ||m^{-1} D(e^θ G' e^{-θ} g)|| <= C ||g||, and the transpose holds as well.
- (ii) The normalized site Gram and R: N_θ^{-1} is bounded and ||e^θ R e^{-θ} - R|| <= C_R tau (7.4 there). N differs from the normalized Gram by the diagonal scale factors Xi^{±2}.
- (iii) ||e^θ T^{-1} e^{-θ}||_{E*->E} <= C for T^{-1} = G ((7.5) there) and T^{-1} = G_1[j] (§7.4 there).
- (iv) ||e^θ W^{-1} e^{-θ}||_{row->row*} <= C for W = Q G Q^T (7.2(iv) there) and W_1[j] = Q G_1[j] Q^T (§7.4 there).

All constants are C = C(L). (I1) rests in turn on `a2-curved.md` §8, gated in row 93. This note does not re-derive it.

Fix a smooth pillar partition of unity chi_x (sum_x chi_x = 1, supp chi_x within r_0 of pillar x, slopes <= C per unit d_B). For a dual vector G put <chi_x G, Psi> := <G, chi_x Psi>. By bounded overlap and Cauchy-Schwarz,

    sum_x ||chi_x G||_*^2 <= C_L ||G||_*^2,     ||sum_x G_x||_*^2 <= C_L sum_x ||G_x||_*^2   if each G_x is supported near x.      (5.0)

Let K_τ := sup_y sum_x e^{-τ d_B(y,x)}. By the ball count #{x : d_B(x,y) <= r} <= C_L (1+r)^5 L^{8r/rho} (`a2-layers.md` §7.3, rederived in `gates/a2-layers-gate.md` §4; Balaban CMP 96 Lemma 2.1), K_τ <= C_L sum_m (2+m)^5 e^{-(τ/2) m} < infinity whenever τ rho' >= 16 log L. The smallest rate summed below is tau_L/16, and tau_L rho' >= 256 log L (§3) covers it. On the actual sequence the gap is rho >= rho', so the same bounds hold there.

**Lemma D (conjugation gives local decay).** Let O: 𝒜* -> 𝒜 satisfy ||e^θ O e^{-θ}|| <= C_O for every tau-Lipschitz theta, where 𝒜 is any of the local-norm spaces of §4. If F is supported near z, then ||O F||_{𝒜,y} <= C_L C_O e^{-τ d_B(y,z)} ||F||_* for every pillar y.

*Proof.* Take theta = tau d_B(., z). This is tau-Lipschitz and finite on the finite lattice, so the gate's cap repair is not needed. Let zeta be a cutoff equal to 1 within r_0 of z, supported within 2r_0. Then <e^θ F, Psi> = <F, zeta e^θ Psi>, and ||zeta e^θ Psi|| <= C e^{2τ r_0} ||Psi|| by the product rule: e^θ changes by a factor <= e^{τ eta/m} across a fine bond. So ||e^θ O F|| <= C_O C e^{2τ r_0} ||F||_*. Conversely e^{θ(x)} >= e^{τ d_B(y,z) - 4Lτ} on pillar y. By the product rule again, ||Phi||_{𝒜,y} <= C e^{-τ d_B(y,z)} ||e^θ Phi||_𝒜. ∎

**Lemma P (composition).** Let O_1: 𝒜_1* -> 𝒜_1 and O_2: 𝒜_2* -> 𝒜_2 have local decay with constants C_1, C_2 and rate tau. Let l: 𝒜_1 -> 𝒜_2* be local, with ||chi_x l Phi||_* <= C_l sum_{d_B(x',x) <= 2r_0} ||Phi||_{𝒜_1,x'}. Then O_2 l O_1 has local decay with constant C_L C_1 C_2 C_l K_{τ/2} and rate tau/2. If O_1 or O_2 is itself local, the rate is not reduced.

*Proof.* Write l O_1 F = sum_x chi_x l O_1 F. Each term is supported near x, with norm <= C_l N_L C_1 e^{2τ r_0} e^{-τ d_B(x,z)} ||F||, where N_L bounds the number of pillars within 2r_0. Apply O_2, then sum over x using e^{-τ(d(y,x) + d(x,z))} <= e^{-(τ/2) d(y,z)} e^{-(τ/2) d(y,x)}. ∎

**Lemma S (Schur).** If ||chi_x O chi_z F|| <= k(x, z) ||F|| in local norms (with the local norm of a dual vector at x read as ||chi_x .||_*), then ||O|| <= C_L (sup_x sum_z k(x,z))^{1/2} (sup_z sum_x k(x,z))^{1/2}. *Proof.* Use (5.0), Cauchy-Schwarz and ||Phi||^2 = sum_x ||Phi||_x^2. ∎

**Lemma K (commutators with the cutoffs).** For every cube kappa, every Psi and every pillar x,

    ||chi_x [K, h~_kappa] Psi||_* <= (C_K/M_1) sum_{d_B(x',x) <= 2r_0} ||Psi||_{𝒳,x'},

and chi_x [K, h~_kappa] = 0 unless x lies within 2r_0 of the set where h~_kappa is not locally constant, which is contained in kappa^(2) \ kappa^(1). C_K = C_K(L).

*Proof.* Take K block by block, using (c2) of §3.

- Multiplication blocks (the identity in X, the mass parts, the pairings with J and j): these commute with h~ up to a base-point shift of one bond. That costs <= C_p L eta/(M_1 m) <= C_p L/M_1 relative to the zeroth-order part.
- First-order difference blocks (D, D^T, nabla_U, B, B^T, the D-terms of c_J and of Delta^(2)[j] D): here the commutator multiplies by a difference of h~ across one bond, of size <= C_p L eta/(M_1 m), against a coefficient of size eta^{-1}. That is C/(M_1 m) times the field, which the m^{-1} part of the local norm controls.
- Second-order blocks (A_s in X, Delta^W in q_AA, D A_s in q_Aλ): the product rule leaves a first-order operator with coefficient D h~ and a zeroth-order one with coefficient D^2 h~. These are bounded by (C/M_1)(||m^{-1} D .|| + ||m^{-2} .||) or (C/M_1)(||nabla_U .|| + ||m^{-1} .||). For D A_s, pair against A'': <A'', [D, h~] A_s lambda> + <D^T A'', [A_s, h~] lambda>. The first is bounded by ||m^{-1} A''|| (C/M_1) ||A_s lambda||, the second by ||D^T A''|| (C/M_1) ||lambda||_Λ. Delta^W is handled through the factorization PX114 (curl squared plus a remainder of mass-form size), as in `gates/a2-layers-gate.md` item 4.
- Averaging blocks (Q, Q^T, Q', Q'^T, Q^T a Q, Delta^(2)[j], and E-type stencils): the commutator is the oscillation of h~ over a read set of physical diameter <= C xi. That is <= C L^2/M_1 times the absolute operator, which is bounded by the row and column counts. This is `flat-port.md` (8.8), whose estimate uses no flatness beyond these counts.

Every curved coefficient is bounded by the class: unitary links times e^{i eta A'} with |eta A'| <= alpha_1 eta/xi, |J| <= gamma_0 xi^{-3}, and |j| <= gamma_j xi^{-3}. ∎

**Lemma L (the local inverse).** Assume (I1), M_1 >= M_C(L), the ceiling (alpha_0, alpha_1, gamma_0) <= a_*(L), and sup xi^3 |j| <= gamma_j(L). Then for every separated sequence with cube size >= M' and gap >= rho' (the actual sequence and every cut-down), every regular pair, and every such coefficient, K = K[S, P, j] is invertible. For F supported near z and every pillar y,

    ||K^{-1} F||_{𝒳,y} <= B_L e^{-τ_L d_B(y,z)} ||F||_{𝒳*},      τ_L := tau_0 2^{-25},              (5.1)

with B_L = B_L(L). K^{-1} is holomorphic in (P, J, j) on the class and real at real data.

*Proof.* Invertibility is Lemma U with (I1). By (4.1)-(4.2), each component of K^{-1} F is a finite sum of words l_m O_m ... l_1 O_1 l_0 F. Each l_i is local in the sense of Lemma P with C_l <= C_L; it is built from B, B^T, Pi, Pi^T, Q, Q^T, Q', Q'^T, the blocks of q, and the identity. Each O_i is one of: G' as L^2 -> Λ, or as Λ* -> L^2; N; T^{-1}; W^{-1}. Count the inverse factors, using (4.2) and (4.1):

- X^{-1} uses at most five: lambda = G'(s_h - G'(s_λ + Q'^T N(... - Q' G'^2 s_λ))).
- f~ uses at most ten, through its term L^T q_λλ Pi X^{-1} g' with L^T = B^T X^{-1} Pi^T.
- A and nu add T^{-1} Q^T W^{-1} Q T^{-1}, so at most 13.
- Y = X^{-1}(g' + B A) uses at most 18.
- Z = X^{-1}(... - Pi^T q_λλ Pi Y) uses at most 23.

So no word has more than 25 inverse factors.

Each O_i has local decay at rate tau_0. For T^{-1} and W^{-1} this is Lemma D with (iii) and (iv). For N it is Lemma D with (ii). For G' as V* -> V it is Lemma D with (i). For G' as L^2 -> Λ: the m^{-2} and m^{-1}D parts come from the scale-conjugated (i), and the third part is local, since A_s G' s = s. For G' as Λ* -> L^2: transpose the L^2 -> Λ statement, using that G' is symmetric and that a dual vector supported near z sees only the Λ-norm near z. Lemma P, applied at most 25 times, gives (5.1). The Λ-part of lambda (and of lambda') needs no further step: by (4.2), A_s lambda = s_h - h, a local expression in a source component and an already bounded unknown. Holomorphy and reality: the entries of K are holomorphic in the data and real at real data, and K is invertible throughout the class. ∎

The rate tau_L is small but depends on L only, and so does B_L. Neither depends on M_1, the box, the depth, the volume or the regions.

## 6. Theorem W: the walk expansion of a finite-range unfolded system

Let S be the depth-k sequence and P a regular pair for it below the ceiling. Let j be a *local* coefficient: its value at a row c is a function of the data within a fixed number of boxes of c, with sup xi^3 |j| <= gamma_j. For kappa in K let S^kappa be its cut-down (Lemma C), P^kappa the restriction of P to Omega^kappa_0, and j^kappa := j on the rows of S^kappa that are rows of S inside kappa^(7/2), and 0 on the other rows. Put

    K := K[S, P, j],   K_kappa := K[S^kappa, P^kappa, j^kappa],   S_kappa := K_kappa^{-1},
    B := sum_kappa h~_kappa S_kappa theta_kappa,   R_kappa := -[K, h~_kappa] S_kappa theta_kappa.

Fields on Omega^kappa_0 are extended by zero.

**Theorem W.** Assume the hypotheses of Lemma L. There are M_W(L) and C_W(L) such that for M_1 >= M_W:

- (a) K B = 1 - R with R = sum_kappa R_kappa and ||R||_{𝒳*->𝒳*} <= 1/2. Hence

      K^{-1} = sum_omega T_omega,   T_omega := h~_{kappa_0} S_{kappa_0} theta_{kappa_0} R_{kappa_1} ... R_{kappa_n},      (6.1)

  over walks omega = (kappa_0, ..., kappa_n), n >= 0. Only walks with X_{kappa_{i-1}} ∩ X_{kappa_i} ≠ ∅ contribute, and the series converges absolutely in operator norm.
- (b) For F supported near z and every pillar y,

      ||T_omega F||_{𝒳,y} <= B_L (C_W/M_1)^n e^{-(τ_L/2) d_B(omega; y, z)} ||F||_*,      (6.2)

  where d_B(omega; y, z) is the least d_B-length of a polygonal path from y to z that meets X_{kappa_1}, ..., X_{kappa_n}. It is >= the outline's tree distance, since a path is a tree. The output of T_omega lies in supp h~_{kappa_0} ⊂ X_{kappa_0}, and T_omega reads F only on supp theta_{kappa_n}.
- (c) T_omega depends on (P, J) and on the data entering j only through their values on the hull [[omega]] := union_i kappa_i^(4), enlarged by the read range of j. It depends on S only through the sets Omega_i ∩ [[omega]]. It is holomorphic on the local class on [[omega]] ∩ Omega_0 and real at real data.
- (d) T_omega is canonical. A translation in M_1 xi_k Z^4 that carries the data on [[omega]] to the data on [[omega']] carries T_omega to T_{omega'}. If K is gauge covariant (input (I2), §8), so is T_omega, for every gauge transformation.

*Proof of the identity in (a).* K (h~_κ S_κ θ_κ F) = h~_κ K Φ + [K, h~_κ] Φ, with Φ = S_κ θ_κ F. At every base point within r_0 of supp h~_κ ⊂ κ^(2), (K Φ)(x) = (K_κ Φ)(x). Indeed, by (C2) the two systems have the same coefficients there, the coefficient j^κ agrees with j on the rows they read, and both read Φ only within r_0 of x, inside κ^(5/2) ⊂ C_0. So h~_κ K Φ = h~_κ K_κ Φ = h~_κ θ_κ F = θ_κ F, by (c1). Summing over κ with sum_κ θ_κ = 1 gives K B = 1 - R. In a product θ_{κ_{i-1}} R_{κ_i} ≠ 0, the set supp θ_{κ_{i-1}} lies within r_0 of supp ∇h~_{κ_i}, so X_{κ_{i-1}} ∩ X_{κ_i} ≠ ∅.

*Proof of (b) (chaining; Balaban CMP 99b (3.91)-(3.94), CMP 96 (2.52)-(2.56)).* θ_{κ_n} F is supported near z, with norm <= C ||F||. By Lemma L for K_{κ_n}, and d^κ_B >= d_B on its domain (C3), Φ_n := S_{κ_n} θ_{κ_n} F obeys ||Φ_n||_x <= C B_L e^{-τ_L d_B(x,z)} ||F||. Let G_n := [K, h~_{κ_n}] Φ_n = sum_{y_n} chi_{y_n} G_n. By Lemma K, chi_{y_n} G_n vanishes unless y_n is within 2r_0 of supp ∇h~_{κ_n}, and

    ||chi_{y_n} G_n||_* <= (C_K N_L/M_1) C B_L e^{2r_0 τ_L} e^{-τ_L d_B(y_n, z)} ||F||.

The next factor θ_{κ_{n-1}} kills chi_{y_n} G_n unless y_n is within r_0 of supp θ_{κ_{n-1}}. Then θ_{κ_{n-1}} chi_{y_n} G_n is supported near y_n, and Lemma L for K_{κ_{n-1}} applies to it. Iterating to κ_0:

    ||T_omega F||_y <= B_L (C_1/M_1)^n sum_{y_1, ..., y_n} e^{-τ_L [d(y, y_1) + d(y_1, y_2) + ... + d(y_n, z)]} ||F||,

with y_i ranging over pillars of X_{κ_{i-1}} ∩ X_{κ_i} (by (c3)) and C_1 = C_1(L) B_L. Split τ_L = τ_L/2 + τ_L/2. The path y -> y_1 -> ... -> y_n -> z meets X_{κ_1}, ..., X_{κ_n}, so the first half is <= e^{-(τ_L/2) d_B(omega; y, z)}. For the second half, drop the last leg and sum over y_n, then y_{n-1}, ..., then y_1. Each sum is <= K_{τ_L/2}. This gives (6.2) with C_W := C_1 K_{τ_L/2}.

*Proof of the bound in (a).* Apply the same chaining with n = 1 to chi_x R chi_z. Each κ contributes <= B_L (C_W/M_1) e^{-(τ_L/2) d_B(x,z)}. For given (x, z) at most nu_0 cubes contribute (c4). Lemma S gives ||R|| <= C_L nu_0 B_L (C_W/M_1) K_{τ_L/2} <= 1/2 once M_1 >= M_W(L). Hence (1 - R)^{-1} = sum_n R^n converges, B(1 - R)^{-1} is a right inverse of K, and K is invertible (also by Lemma L), so K^{-1} = sum_n B R^n. Expanding B R^n over cubes gives (6.1). For absolute convergence: by (6.2), Lemma S and the walk count nu_1^n, the walks of length n have total norm <= C_L B_L (nu_1 C_W/M_1)^n K_{τ_L/2}, which is summable.

*Proof of (c), (d).* S_κ is the inverse of a matrix whose entries are holomorphic functions of the data on Omega^κ_0 ⊂ κ^(4) (Lemma L). By (C5) and the construction of j^κ, it depends on S only through Omega_i ∩ κ^(4). The commutators [K, h~_κ] = [K_κ, h~_κ] read data within κ^(5/2). Finite products of such factors are holomorphic, and the series converges uniformly on the class, so the sum is holomorphic. Reality is inherited factor by factor. (d) follows from (C5). For covariance: every cutoff is a scalar function evaluated at base points, and the gauge group acts by Ad at base points, so the two commute. A covariant K therefore gives covariant K_κ, S_κ and T_omega. ∎

**Remark (what is new against the templates).** `path_expansion_locality.md` Lemma 1 gives the identity and norm convergence. `flat-port.md` §§8, 11 give the flat local models with periodic or bare read sets, and a total walk norm. Theorem W adds two things. First, its local models are cut-down sequences at curved complex pairs with an independent current, so their inverse bounds are the gated global ones (Lemma L). Second, it has the chained per-walk bound (6.2), with a rate independent of M_1 (test 2.4). The separate partition theta_κ with cutoff h~_κ follows mechanism (f). The template's h S h form, with sum h^2 = 1, would serve equally.

## 7. Trees: H^T J, then G_1, H_1, (Q G_1 Q^T)^{-1} and H_1^T J (mechanism (g))

**Stage 1 (the G-system).** Theorem W with j = 0 gives K_G := K[S, P, 0], with K_G^{-1} = sum_β T^G_β. By Lemma U(c), H = [K_G^{-1}]_{Aν} = sum_β H_β with H_β := [T^G_β]_{Aν}, over walks β = (κ'_0, ..., κ'_m).

**Lemma J (the multiplier as a sum over walks).** Let e_c be the unit row vector at c (componentwise in g^c), and put j_β(c) := xi_c^{-4} <H_β e_c, J>_f. Then H^T J = sum_β j_β, absolutely; this is the transpose for the bilinear pairings, as in `gates/a2-layers-gate.md` item 5. j_β is supported on the rows in supp θ_{κ'_m}. It depends on the data only on [[β]], is holomorphic, and is real at real data. Moreover

    xi_c^3 |j_β(c)| <= C_J gamma_0 (C_W/M_1)^m e^{-(τ_L/4) d_B(β; c)},                       (7.1)

where d_B(β; c) is the least length of a path from X_{κ'_0} to c that meets X_{κ'_1}, ..., X_{κ'_m}.

*Proof.* The ν-source space has norm sum_c xi_c^2 |f_c|^2, so ||e_c|| = xi_c. By (6.2), the A-component of T^G_β e_c is supported in X_{κ'_0}, with ||.||_{E,y} <= B_L (C_W/M_1)^m e^{-(τ_L/2) d_B(β; y, c)} xi_c. Next, ||chi_y J||_{E*} <= ||m chi_y J||_{L^2} <= 2 gamma_0: there are at most 4(xi_y/eta)^4 bonds of weight eta^4 near y, each with |J| < gamma_0 xi_y^{-3}. So |<H_β e_c, J>_f| <= C gamma_0 xi_c B_L (C_W/M_1)^m sum_{y in X_{κ'_0}} e^{-(τ_L/2) d_B(β; y, c)}. For y in X_{κ'_0}, d_B(β; y, c) >= d_B(β; c) and d_B(β; y, c) >= d_B(y, c). So the sum is <= K_{τ_L/4} e^{-(τ_L/4) d_B(β; c)}. Multiplying by xi_c^{-4} xi_c^3 gives (7.1). ∎

**Stage 2 (the G_1-system).** Let j^(0) := sum_{|β|=0} j_β, the terms of walk length zero. At a row c it reads the data on κ^(4) for the at most nu_0 cubes κ with c in supp θ_κ. By (7.1), sup xi^3 |j^(0)| <= C_0 gamma_0 with C_0 := nu_0 C_J. So j^(0) is a local coefficient, and once C_0 gamma_0 <= gamma_j Theorem W applies to K^(0) := K[S, P, j^(0)]. Write S^(0)_κ, R^(0)_κ, B^(0) for its objects.

For |β| >= 1 put V_β := K[S, P, j_β] - K[S, P, 0]. This is the j-linear part of K with coefficient j_β: the Delta^(2)[j_β]-terms of q_AA, q_Aλ, q_λλ. The coefficient enters K linearly, so

    K_1 := K[S, P, H^T J] = K^(0) + sum_{|β|>=1} V_β,

absolutely. V_β is local near X_{κ'_m}: chi_x V_β = 0 unless x is within 2r_0 of the rows in supp j_β. By the coefficient bound of `a2-curved.md` (8.3)/(8.10), localized to the row carriers,

    ||chi_x V_β Psi||_* <= C_Δ sup_{c within 2r_0 of x} xi_c^3 |j_β(c)| sum_{d_B(x',x) <= 2r_0} ||Psi||_{𝒳,x'}.        (7.2)

**Tree walks.** A tree walk ω consists of three pieces of data:

- a trunk walk (κ_0, ..., κ_n);
- a set I ⊂ {1, ..., n} of vertex positions;
- for each i in I, a walk β_i = (κ'_0, ..., κ'_{m_i}) with m_i >= 1 and X_{κ'_{m_i}} ∩ X_{κ_i} ≠ ∅.

Its cells are the trunk cells and the branch cells. The parent of κ_i is κ_{i-1}, the parent of κ'_{m_i} is κ_i, and the parent of κ'_{l-1} is κ'_l. So every cell overlaps its parent, as in SA 10210. Put |ω| := n + sum_{i in I} (m_i + 1), the number of cells minus one, and

    T^(1)_ω := h~_{κ_0} S^(0)_{κ_0} θ_{κ_0} F_1 ... F_n,   F_i = R^(0)_{κ_i} (i not in I),   F_i = -V_{β_i} h~_{κ_i} S^(0)_{κ_i} θ_{κ_i} (i in I).

Let d_B(ω; y, z) be the least length of a tree that contains y and z and meets every cell of ω except X_{κ_0}.

**Theorem T.** There are M_T(L), a_T(L), B_1(L), C_T(L) such that for M_1 >= M_T and gamma_0 <= a_T:

- (a) K_1 B^(0) = 1 - R' with R' := R^(0) - sum_{|β|>=1} sum_κ V_β h~_κ S^(0)_κ θ_κ and ||R'|| <= 3/4. So K_1^{-1} = sum_ω T^(1)_ω over tree walks, absolutely.
- (b) For F supported near z and every pillar y,

      ||T^(1)_ω F||_{𝒳,y} <= B_1 (C_T M_1^{-1/3})^{|ω|} e^{-(τ_L/4) d_B(ω; y, z)} ||F||_*.            (7.3)

- (c) At most C_T^m tree walks with |ω| = m start at a given cube.
- (d) Theorem W(c)-(d) hold for T^(1)_ω, with hull [[ω]] := the union of the hulls of the trunk and of the branches, each enlarged by the read range of j^(0) (O(M_1) local units).

*Proof.* (a) K_1 B^(0) = K^(0) B^(0) + sum_β V_β B^(0) = 1 - R^(0) + sum_{β,κ} V_β h~_κ S^(0)_κ θ_κ, and ||R^(0)|| <= 1/2 by Theorem W. For the vertex part, apply Lemma S to chi_x V_β h~_κ S^(0)_κ θ_κ chi_z, using (7.2), (7.1) and Lemma L. For given (x, z), the pairs (β, κ) with |β| = m that contribute number at most nu_0^2 nu_1^{m+1}. So the vertex part has norm <= C gamma_0 sum_{m>=1} (nu_1 C_W/M_1)^m <= C' gamma_0/M_1 <= 1/4. Expanding B^(0) sum_n R'^n gives the tree walks. Each nonzero vertex factor needs supp V_{β_i} to meet supp h~_{κ_i}, that is, X_{κ'_{m_i}} ∩ X_{κ_i} ≠ ∅ by (c3).

(b) Chain as in the proof of Theorem W(b). At a vertex step i, (7.2) and (7.1) give the factor C_Δ N_L C_J gamma_0 (C_W/M_1)^{m_i} e^{-(τ_L/4) d_B(β_i; y_i) + C}. So

    ||T^(1)_ω F||_y <= B_L C_3^n M_1^{-p} sum_{y_1..y_n} e^{-τ_L sum_i d(y_{i-1}, y_i)} prod_{i in I} e^{-(τ_L/4) d_B(β_i; y_i)} ||F||,
    p := (n - |I|) + sum_{i in I} m_i.

For fixed y_1, ..., y_n, take the trunk path y -> y_1 -> ... -> y_n -> z, and for each i in I a near-optimal path from y_i through the cells of β_i to X_{κ'_0(β_i)}. The union is a connected set containing y and z that meets every cell of ω except X_{κ_0}. So it contains such a tree, of length <= sum d(y_{i-1}, y_i) + sum_{i in I} d_B(β_i; y_i). Spend (τ_L/4) sum d and the branch exponentials on e^{-(τ_L/4) d_B(ω; y, z)}. The remaining e^{-(3τ_L/4) sum d} pays the sums over y_n, ..., y_1, at <= K_{3τ_L/4} each. Finally, 3p - |ω| = 2(n - |I|) + 2(sum_{i in I} m_i - |I|) >= 0, since every m_i >= 1. So C_3^n M_1^{-p} <= (C_3 M_1^{-1/3})^{|ω|}.

(c) There are at most nu_1^n trunks and 2^n vertex sets. A branch with m_i steps has its last cell among <= nu_1 cubes meeting X_{κ_i}, and then <= nu_1^{m_i} backward continuations. The number of ways to split m = n + sum(m_i + 1) is <= 2^m. So the count is <= (4 nu_1)^{2m}.

(d) Every factor is local with the stated read sets (Theorem W(c), Lemma J), and holomorphic. The cutoffs commute with the gauge action, and j_β is covariant when K_G is. ∎

**Corollary T (the four objects consumed by A).** By Lemma U(c) at j = H^T J:

- H_1 = sum_ω [T^(1)_ω]_{Aν}.
- (Q G_1 Q^T)^{-1} = -sum_ω [T^(1)_ω]_{νν}.
- H_1^T J = sum_ω j^(1)_ω, with j^(1)_ω(c) := xi_c^{-4} <[T^(1)_ω]_{Aν} e_c, J>_f, supported on the rows of supp θ_{κ_n}, and

      xi_c^3 |j^(1)_ω(c)| <= C_J' gamma_0 (C_T M_1^{-1/3})^{|ω|} e^{-(τ_L/8) d_B(ω; c)},           (7.4)

  where d_B(ω; c) is the least length of a tree through c that meets every cell of ω. The proof is that of Lemma J with (7.3) in place of (6.2). The output side lies in X_{κ_0}, so here X_{κ_0} is met as well.

Every term has properties (c)-(d) of Theorem T. This is mechanism (g) of the outline, with the count it asserts. Its M_1-power is the one of test 2.3.

## 8. Theorem H: the walk expansion of A and of chi_Y A chi_Y

**Two more inputs**, used only where named:

- (I2) Gauge covariance of the averaging maps: Q(U^u), Q'(U^u) are the conjugates of Q(U), Q'(U) by the induced action at block centres. This is the covariance of Balaban's averaging (CMP 98) and of the outline's straightened rows (statement 3, SA 10282-10296). With it, every block of K is covariant, since Delta^W, D_U, Delta'_pi[J] and Delta^(2)[j] are built covariantly. Covariance of C_V and of the Delta_k-operators is recorded in `a2-full.md` §10 defect 5 (same-model, gate row 114). (I2) is not re-derived here. It is used only for the covariance clause.
- (I3) The level-k maps C_V (pivot elimination), G^(2)_V (soft axial gauge Hessian), a and E^(2)[psi] are finite analytic functions of V = M^k U near Omega_{k+1}, with finite stencils. ||C_V|| <= C_L, and ||E^(2)[psi]|| <= C_L sup |psi| over its stencil. Sources: `a2-curved.md` §5 and (5.7), gated in `gates/a2-curved-gate.md` (§5 ADVANCE); `a2-layers.md` §7.6(a); `a2-full.md` Lemmas 4.1(b), 5.1.

**Lemma 8.1 (class).** A regular pair for the longer sequence (Omega_j)_{j<=k+1}, with radii (alpha_0, alpha_1, gamma_0), is a regular pair for S = (Omega_j)_{j<=k} with the same radii. *Proof.* The layers below k agree. The top layer of S is Omega_k = L_k^long ∪ L_{k+1}^long, of scale xi_k = 1. On Omega_{k+1} the longer class imposes its bounds with xi_{k+1} = L > 1. These are stronger: |dU - 1| < alpha_0 eta^2 L^{-2}, |A'| < alpha_1/L, |J| < gamma_0 L^{-3}. The level-k gauge clause of S concerns cubes of side <= c_g M_1 in Omega_k = L_k^long ∪ L_{k+1}^long, which is the longer class's level-k clause. ∎

So Theorems W and T apply to S at every pair regular for the longer sequence. On the active rows (level k, touching Omega_{k+1}, xi = 1), Corollary T and the definition give

    A = C_V^T (G^(2)_V - a) C_V + C_V^T [(Q G_1 Q^T)^{-1}]_act C_V - C_V^T E^(2)[H_1^T J] C_V
      = sum_{κ in K_k} A^loc_κ + sum_ω (A^G_ω + A^E_ω),

with three kinds of term:

- A^loc_κ := θ_κ C_V^T (G^(2)_V - a) C_V, for the level-k cubes meeting the mask. Each is a walk of length 0.
- A^G_ω := -C_V^T [T^(1)_ω]_{νν,act} C_V, rooted at κ_0.
- A^E_ω := -C_V^T E^(2)[j^(1)_ω] C_V, rooted at κ_n. Its kernel lives near the rows of supp θ_{κ_n}, so its root is re-taken there. Re-rooting a tree changes neither its cells nor its length.

**Theorem H.** Let L >= L_0. Fix M', rho', r_0, tau_L, B_L, C_K, C_W, C_T and the ceilings a_*, gamma_j, a_T as above, all functions of L. Put a_h(L) := min{a_*, a_T, gamma_j/C_0, a_B} on (alpha_0, alpha_1, gamma_0), where a_B is the complex ceiling of `a2-layers.md` Theorem B. Assume R_1 >= 64L, M_1 >= M_h(L) := max{M_C, M_W, M_T}, and (I1)-(I3). Then at every regular pair P for (Omega_j)_{j<=k+1} with radii below a_h, real or complex, with independent current:

- (H1) A = sum_ω A_ω over tree walks, with A_ω ∈ {A^loc_κ, A^G_ω, A^E_ω}, absolutely convergent. At most C_h^m indices of length m have a given first cell.
- (H2) |A_ω(b, b')| <= C_h (C_h M_1^{-1/3})^{|ω|} e^{-δ_h d_B(ω; b, b')}, with δ_h := tau_L/8, in counting measure on the free level-k coordinates. Here d_B(ω; b, b') is the least length of a tree through b, b' that meets every cell of ω except the root, and the left argument b lies within O(1) of the root cell. In the outline's two-factor form this reads (C_h M_1^{-1/6})^{|ω|} M_1^{-|ω|/6}. d_B is the metric of the depth-k sequence. On Omega_{k+1} it counts level-k units, so it dominates the metric of the longer sequence, and (H2) holds for either.
- (H3) A_ω is holomorphic on the local class on [ω] and real at real pairs. It depends on the regions only through their traces on [[ω]], which enlarges the cells by O(M_1) local units. It is the same function for two sequences, tori or cutoffs that a translation in M_1 xi_{k+1} Z^4 carrying Omega_{k+1} (and Y) relates on the hull. It is covariant under the lattice isometries that preserve the level-(k+1) M_1-grid, the regions and Omega_{k+1}. Given (I2), A^G_ω and A^E_ω are covariant under every gauge transformation, and A^loc_κ under those that are constant on each level-(k+1) block of the mask. A itself is covariant exactly under the latter (§2.1).
- (H4) For every conditioning set Y, chi_Y A chi_Y = sum_ω chi_Y A_ω chi_Y, with the same bounds and properties. This is statement 5 for chi_Y A chi_Y, in the corrected form (S2)-(S3) of §1.

*Proof.* (H1), (H2). C_V and E^(2) have O(1) stencils (I3), so composing with them moves kernel arguments by O(1). That costs only a constant in (H2), absorbed by e^{δ_h C}.

- *A^G_ω:* take the source e_{c'} in the ν-slot, with ||e_{c'}|| = 1 at xi = 1. The output's local row* norm at c is >= |ν_c|. So (7.3) gives |[T^(1)_ω]_{νν}(c, c')| <= B_1 (C_T M_1^{-1/3})^{|ω|} e^{-(τ_L/4) d_B(ω; c, c')}.
- *A^E_ω:* by (I3) and (7.4), |A^E_ω(b, b')| <= C_L C_J' gamma_0 (C_T M_1^{-1/3})^{|ω|} e^{-(τ_L/8) d_B(ω; c)} with c within O(1) of b and b'. A tree through c meeting every cell, together with O(1) legs to b and b', is a tree through b, b' meeting every cell.
- *A^loc_κ:* it has range O(1) and norm <= C_L.

The index count is that of Theorem T(c), doubled for the two roots, plus single cubes.

(H3). Every factor is local with the read sets of Theorem W(c) and Theorem T(d), and C_V, G^(2)_V, a, E^(2) read V within O(1) (I3). The isometries named map the cube family, the cutoffs (even product profiles) and the cut-down construction to themselves. A coarse-grid point is a grid point of every finer grid, so the finer grids are preserved too. Gauge: Theorem W(d) and Theorem T(d) with (I2). C_V and E^(2) are covariant (I3, `a2-full.md` §10 item 5), and G^(2)_V only under block-constant transformations. (H4): compress. ∎

**Order of constants.** First L. Then, as functions of L alone: M', rho', r_0, tau_0, tau_L, B_L, C_K, C_W, C_T, C_h, δ_h, and the ceilings a_*, gamma_j, a_T, a_B, a_h. Then R_1 >= 64L and M_1 >= M_h(L). The ceilings are fixed before M_1 and do not depend on it, as SA 10335 and SA 10582 require. Only the walk factor M_1^{-1/3} involves M_1. No constant depends on k, the volume, the regions, Y or the pair.

**By-product (statement 5 for the other operators, in energy norms).** The same theorems give walk expansions for the blocks of K_G^{-1} and K_1^{-1}, and of the systems without the ν-row (whose (A,A) block is T^{-1} itself). These blocks are G, G_1, H, H_1, (Q G Q^T)^{-1}, (Q G_1 Q^T)^{-1}, Balaban's G~ = G - H Q G (the (A,A) block), and 1 - R, a block of X^{-1}. The bounds hold in the local energy norms of §4. The pointwise, derivative and Hölder norms of statement 4 that statement 5 also asks for are **not** claimed: they need a local regularity upgrade, as in `flat-port.md` §11. For chi_Y A chi_Y, a unit-lattice kernel, the energy norms are the consumed norms.

## 9. The consumer reads Theorem H as written

`a2-full.md` Theorem VI states (H-walk) with (C M_1^{-1/2})^{|ω|} M_1^{-|ω|/2}, the count C^m, and holomorphic A_ω at the complex regular pairs used. It reads that input in three places.

1. "Sum over walks: for each first cell there are C^m walks of length m, so (C M_1^{-1/2})^m C^m is summable for M_1 large." With (H1)-(H2), the sum is sum_m (C_h M_1^{-1/3})^m C_h^m, which is <= 2 once M_1 >= (2 C_h^2)^3. This is one more lower bound on M_1, as a function of L.
2. Mechanism (i) with delta = delta_0/2 >= C kappa-bar/l_P. Take delta_0 := δ_h(L). The order of constants in a2-full §8 (L, then M_1 and rho, then kappa-bar, then l_P >= 2C kappa-bar/delta_0, then M) is unchanged, because δ_h depends on L only. Mechanism (i) needs the root cell X_0 within O(1) top units of the left argument, and (H2) supplies this for all three kinds of term.
3. "Every tree admitted in d_B(ω; y, y') then passes through y and through a cell near that cube, so d_B(ω; y, y') >= w - C." This uses only that the tree meets every non-root cell and contains y. That is the definition in (H2).

Theorem VI's factor M_1^{-|ω|/2}, reserved for |ω| + 1 (SA 10316, 10558), is replaced by M_1^{-|ω|/6}, which absorbs |ω| + 1 for M_1 >= e^6. The proof of Theorem VI therefore goes through verbatim with (C M_1^{-1/6}, M_1^{-1/6}, δ_h) in place of (C M_1^{-1/2}, M_1^{-1/2}, delta_0), and its conclusion is unchanged: the decoupled precision keeps Re >= (c_L/2)||u||^2 for all independent |s_Δ| <= e^{kappa-bar}, with the collar w >= (4/δ_h)(2^4 kappa-bar + log(20 C_VI/c_L)).

Two more facts about A(s) := sum_ω s^ω A_ω. At s ≡ 1, A(1) = A by (H1). A(s) is holomorphic on the polydisc |s_Δ| <= e^{kappa-bar}, because each A_ω is a monomial in s times a fixed matrix and the series converges uniformly there (Theorem VI's estimate).

## 10. Verdict, defects, what stays open, what changes

**Verdict.** (H-walk), the outline's statement 5 for chi_Y A chi_Y at the pairs regular for the longer sequence, is **proved as an implication** (Theorem H). This is the only input of A2 item (3) (`a2-full.md` §10, open item 1). Two clauses are corrected: the M_1-power per cell is 1/3, not 1 (test 2.3), and gauge covariance holds only for the subgroup under which A is covariant (test 2.1). In that form it is what `a2-full.md` Theorem VI reads (§9). The implication reads three inputs:

- (I1), the gated global conjugation package of `a2-layers.md` §7 with Codex's repairs, itself conditional on the gated `a2-curved.md` §8;
- (I2), gauge covariance of the averaging maps, used only for the covariance clause;
- (I3), the level-k local maps (gated `a2-curved.md` §5).

No counterexample to a consumed statement was found (§2).

| Step | Verdict | Where | Reads |
|---|---|---|---|
| Counterexample tests | none found; two clauses corrected (2.1, 2.3); four routes killed (2.2, 2.4-2.6); two norm choices fixed (2.7-2.8) | §2 | outline; `a2-full.md` §10 defect 5 |
| Cut-down local models: separated, agree on the box, class transfer, canonical | **proved** | §3 Lemma C | outline geometry; Balaban CMP 99b p. 408 |
| Unfolded 8-unknown system: Schur complements G^{-1}, G_1^{-1}[j]; blocks H, H_1, (QGQ^T)^{-1}, (QG_1Q^T)^{-1} | **proved** (finite-dimensional algebra) | §4 Lemma U | SA 10142-10206 and explicit current formula |
| Local decay of the unfolded inverse, uniform in M_1, box, depth and regions | **implication** | §5 Lemmas D, P, S, K, L | (I1) |
| Parametrix walk expansion with chained per-walk bound and rate independent of M_1 | **proved** given Lemma L | §6 Theorem W | Lemmas C, K, L |
| Tree expansion through the multiplier H^T J (mechanism (g)); G_1, H_1, (QG_1Q^T)^{-1}, H_1^T J | **proved** given Theorem W | §7 Lemma J, Theorem T, Corollary T | (7.2): `a2-curved.md` (8.3)/(8.10) |
| Statement 5 for chi_Y A chi_Y (corrected clauses) | **proved as an implication** | §8 Theorem H | (I1)-(I3) |
| Consumer: Theorem VI with exponent 1/6 | **goes through verbatim** | §9 | `a2-full.md` Theorem VI |

**Defects found, ranked by what they break.**

1. *Statement 5's covariance clause for chi_Y A chi_Y cannot hold for the full gauge group* (test 2.1). A is not covariant, because of G^(2)_V, so no expansion has fully covariant terms. It breaks nothing that is consumed. Repair: the block-constant subgroup, as in Theorem H (H3). It also removes the need for the Haar mean of mechanism (i).
2. *The tree terms' M_1-power.* Vertices of the H^T J expansion carry no commutator, so this route gives M_1^{-1/3} per cell, not (C M_1^{-1/2})^{|ω|} M_1^{-|ω|/2}. The consumers need only a geometric factor with a reserve (§9). If a later consumer reads the exact exponent, that is open. Keeping the walks of H of length <= l in the local coefficient raises the power to (l+1)/(l+3), and never to 1.
3. *Statement 6 is not stated in the outline.* Statement 5 bounds chi_Y A chi_Y by "the kernel bound that 6 states for C^(k)(Y)" (SA 10328). It is read here as A's own unit-lattice kernel bound, and (H2) implies that bound, summed over the trees through b, b'.
4. *Mechanism (i)'s single assignment for all tori* (Haar mean, push-forward, Montel limit along a subsequence; SA 10560) is not needed. The canonical cut-down construction is literally the same on tori and sequences that agree on the hull (Lemma C (C5)). That also avoids its normality step, which needs an entrywise bound allowed to depend on the level.
5. *Mechanism (f)'s remainder bound O(M_1^{-1} e^{-c δ M_1/L})* is not used and not needed. The chained local decay (6.2) gives the rate.

**What stays open, hardest first.**

1. Cross-provider gate of this note. Look hardest at: Lemma C (C4) (class transfer, especially the cut-down levels below i_0); Lemma L (the word count, and the transposition of G' to Λ* -> L^2 in the graph norm); Theorem W(b) (the chaining and the identification of the intermediate pillars with X_{κ_{i-1}} ∩ X_{κ_i}); Theorem T(b) (the vertex accounting 3p >= |ω| and the tree assembled from the trunk path and the branch paths).
2. The inputs. (I1) is gated (rows 92-93), with its Section 7 repairs. (I2), gauge covariance of the averaging maps, is read from the outline and Balaban CMP 98, and is not rebuilt here. It enters only the covariance clause, which no consumer of A2 item (3) reads.
3. Not part of this item. The walk-chain expansion of the inverse root r(s) (SA 14154-14170). The walk expansion of C^(k)(Y) = (chi_Y A chi_Y)^{-1} itself, also listed in statement 5. Statement 5 for the propagators in statement 4's pointwise and Hölder norms; §8 gives them in energy norms only.

**What changes for the lead (evidence only; no other file was edited).**

- `a2-full.md` §10, open item 1: (H-walk) is no longer "not in hand". It is proved as an implication here, same-model and gate pending. Theorem VI, and with it A2 item (3), then rests on (I1) (gated), (I2), and this note's gate.
- `sa-ledger.md` rank 2 (A2): the "enlarged-complex-domain" version now reduces to gated (I1) plus this note, with the exponent and covariance wording above. (H-ct) and (H-prof) are unchanged.
- The outline's statement 5 wording should carry the corrected exponent and covariance clauses (defects 1-2), and a stated "statement 6" bound (defect 3).

**Moves:** the only input of A2 item (3), `a2-full.md` §10 open item 1 (outline statement 5 / (1c.8)-(1c.9) for chi_Y A chi_Y), from "not in hand" to "proved as an implication, gate pending".

**Method.** Every step is a written argument. There is no computation, enumeration or numerics. No numerical job was run, so the numeric lock was not needed. No subagent. Only this file was written.

Credit, repeated for the parts used:

- Ethan Sussman and Levent Alpoge, with Claude and Codex as authors of their text (`31a47c543775`): the statement, operators, walk vocabulary, unfolding with auxiliary unknowns, tree treatment of the multiplier, multiplier mechanism and consumer.
- T. Balaban: cut-down local models, generalized random-walk expansions and their chaining, the summation lemma and the walk-relative distance (CMP 95 Prop. 1.2; CMP 96 Lemma 2.1, (2.50)-(2.66); CMP 99b (3.87)-(3.94), Theorem 3.7, Corollary 3.8).
- The gated global bounds: Claude's `a2-layers.md` §7 with Codex's gate repairs, on Codex's `a2-curved.md` §8 with Claude's gate.
- The flat local system and commutator estimates: Codex's `flat-port.md` §§8-11.
- The parametrix template: `path_expansion_locality.md` Lemma 1, after Dimock arXiv:1108.1335 §2.4.
