lead: anthropic/claude-opus-5-5/max mac-mini-worker
lease_until: 2026-11-03T14:08Z

# a2-full: the outline's A2 from separated layers to its full scope

Pinned at branch claude/ym4d-hard-route, commit 7668755cf. Queue row 109. Same-model, ungated, research-stage working state. Complete for this item.

Provenance: Anthropic Claude Opus 5.5 (`claude-opus-5-5`), effort max as configured for this worker (Mac mini); repository commit 7668755cf; Sussman–Alpoge outline `YM4_sketch_500.tex` at commit `31a47c543775`, fetched by URL into a scratch folder and not committed (outline line numbers below, written SA nnnn, refer to that file); Balaban CMP 119 read from `~/ym4d-papers/cmp119.txt` (OCR, outside git). Research text by one model, not an audit and not a gate; it grants no status. No step rests on a computation; no numerical job was run.

**Credit.** The obligation A2 and its list of versions (SA 3835–3863), the operators and the identification paragraph (SA 10138–10208), the physical diagram PX93–PX105 (SA 11141–11262), the localized Gaussian comparison (SA 13895–14200), the profiles and exponent (SA 6331–6355), the step anatomy (SA 7590–7614, 7855–7880) and the walk mechanisms (SA 10540–10560) are Ethan Sussman and Levent Alpoge's outline, with Claude and Codex as authors of their text. Tadeusz Balaban supplies the programme: the background expansion (CMP 102 (174); CMP 109 (2.4)–(2.11), as the outline cites them), the effective action with a position-dependent coupling g_k^2(x) (CMP 119 (2.23)–(2.24)), separate currents (CMP 109) and decoupling parameters (CMP 116, as cited at SA 10552). The layered A2 operator estimates used here are `a2-layers.md` (Claude) with the repairs of `gates/a2-layers-gate.md` (Codex), and `a2-curved.md` (Codex) as gated in `gates/a2-curved-gate.md` (Claude). The response bounds are (1b) Theorem 4 as proved in `a3-derivative.md` and `a3-clauses.md` and gated as recorded there.

## 0. Disposition

**Item (1), proved.** At the pair of the step, A (SA 10204) is the Hessian of the step's exponent on the next fibre: PX93-PX104 hold, every identity written (Theorem I). The gauge identity Delta^W - Delta'_pi[J(U)] = S^T Delta^W S with the outline's explicit formula is re-derived from the BCH expansion of the gauge action (Lemma 3.2). The gauge-fixing gradient term -C_V^T E_V^(2)[J-hat_GF] C_V vanishes wherever V(y,x) = 1, which covers every physical pair and its continuation in the tower axial gauge. At every complex regular pair it is at most C_II alpha_1, and A^full = A plus that term keeps the half-gap (Lemma 4.1, Theorem II).

**Item (2), proved as implications at the coarse level.** The signed-profile, source and boundary perturbations are bounded by C_IV g_k^2 (or C_IV e^{-theta rho/32} for the boundary), uniformly in depth, on the whole complex datum polydisc, by a Cauchy-locality lemma that reads only the gated response decay (T4) (Theorem IV). The counterterm arrays are bounded by C_V eps_ct (g_k/r_k)^2, given the outline's polymer accounting (H-ct) (Theorem V). The gap survives by a coarse stability lemma (Lemma 5.2). **The queue's route for (2) is refuted for profiles:** in the fine X-form norm the profile perturbation is b k g_k^2, unbounded in depth (test 2.1). It is harmless because the profile never enters the fine operators.

**Item (3), proved as an implication** from the walk expansion of chi_Y A chi_Y (outline statement 5, not in this checkout), with the collar and l_P chosen after kappa-bar (Theorem VI).

No counterexample to a consumed statement was found. Open: (H-walk), (H-ct), (H-prof), all outside A2 proper, and a cross-provider gate (Section 10).

## 1. What is consumed

A2 (SA 3835) asks for Re<B, E B> >= c||B||^2 on gauge-fixed fibres QB = 0, with c/2 on the claimed complex neighbourhoods, and names the versions the flat case does not supply: "non-Abelian, nonzero-current, signed-profile, layered or enlarged-complex-domain" (SA 3861). Rows 90-93 proved the non-Abelian, nonzero-current and layered versions for the operator A of SA 10204, on a small complex neighbourhood (`a2-layers.md` Theorems A, B, with the gate's cap and separation repairs). This note settles the rest. The consumers, read in the outline:

- **(C1) The step Gaussian.** SA 7604: x_k[A(U_k(V_k)) + GF_k(V_k)] = x_k A(U_{k+1}) + (1/2)<B, Delta^(k) B> + O(g_k|B|^3) with A_k = g_k B, and SA 7607: completing the square gives C^(k)(Lambda_{k+1}). SA 10208 and SA 14108-14120 identify A(P_W) = C^T Delta^(k) C at the pair of the step. This is the identification of item (1).
- **(C2) The localized Gaussian comparison** (SA 13895-14200). It needs (FG1): C = (chi A(s) chi)^{-1} within epsilon_0(K) of a real reference C_0 = (chi A_0 chi)^{-1}, at complex regular pairs P, with decoupling parameters |s_Delta| <= e^{kappa-bar} on the coarse cubes outside the collar Z_0^# of the support (SA 14158-14190), a complex coefficient ratio tau with |tau - 1| <= c(LM)^{-4} (SA 14196), and integrands with |F(b)| <= F_0 e^{rho|b|^2}, rho <= rho_0(K) (FG5). This is item (3), and the place where items (2) enter.
- **(C3) Signed layer profiles.** The exponent is -A(x_k(.), U) + ... with x_k(p) = beta - sum_{j<=k} b_j phi_j(p), phi_j in [0,1] (SA 6331-6343). The background is the regular critical point of the plain Wilson action (SA 9589), and the Gaussian of the step absorbs the quadratic part of -x_k A with the constant x_k (SA 7614, "the prime"). So the profile deviation x_k(p) - x_k stays in the exponent, as does the source shift zeta_k(.; w) of SA 22590, and "the part of the coupling that depends on position" is interpolated in the t_1-integral (SA 7460). Its quadratic part in B is the signed-profile perturbation.
- **(C4) Counterterm arrays.** The bracket sum_j {E^(j) - b_j A(phi_j, .)} over the levels j <= k (SA 6338-6342, 7820, 7864). Without the subtraction of b_j A the bracket contains sum_{j<=k} b_j {A} ~ c_0 k {A} (the outline's own remark, SA 7864).

Two consumers lie outside A's definition and are not treated here. One is the patch operation of SA 17645 (Balaban CMP 122 (1.71)), whose Gaussian carries the profile weights phi on both the action and the gauge term. The other is the seam node terms of GF (SA 7758-7761), which the outline assigns to the boundary exponent. They are listed in Section 10.

## 2. Counterexample tests (done before the proofs)

**2.1 The signed profile is not a small perturbation of the fine form.** Item (2) of the queue row asks for each comparison "in the proved weighted form norm", the X-form norm of `a2-layers.md` §1, followed by the relative Schur estimate. For the profile this fails. Take a separated sequence of depth k+1 with every layer nonempty and nesting as in SA 6331, with b_i = b > 0 for all i (allowed: SA 9767 asks only -C <= x_q - x_{q'} <= C(q' - q)). On plaquettes of L_0 away from the transition zones, x_k(p) = x_0 = beta, so the relative weight in B units is w(p) = (x_k(p) - x_k)/x_k = b k g_k^2. Take h = v e_b on one bond b of L_0 whose six plaquettes lie in L_0 away from the transition zones (xi_b = eta). Then ||h||_X^2 = 9 eta^2 |v|^2: the mass term gives eta^2|v|^2 and the eight nonzero covariant differences give 8 eta^2 |v|^2. By PX114 with unitary prefixes, sum_p D^2 A_p[h, h] >= (6 - C alpha_0) eta^2 |v|^2. So sum_p w(p) D^2 A_p[h, h] >= (1/2) b k g_k^2 ||h||_X^2 for C alpha_0 <= 3/2. Once k >= 2/(b g_k^2), which a deep label allows (the number of layers is not bounded by 1/g_k^2), this exceeds ||h||_X^2. So the fine-form route fails for every gap c_L. It is also not needed. The profile never enters the fine operators: G_0, G, G_1 use the plain Delta^W (SA 10140, 9589). It acts only through B -> A(w, U(V(B))), and there the response decays across the layers. Section 6 proves that the resulting coarse perturbation is O(g_k^2), uniformly in depth.

**2.2 Unsubtracted counterterm arrays.** Taken alone, the array (b_j A(phi_j, .))_{j<=k} contributes sum_{j<=k} b_j g_k^2 times a positive form of A's size to the coarse Hessian. This is ~ c_0 k g_k^2, not uniformly small (SA 7864). Only the subtracted brackets E^(j) - b_j A(phi_j) are summable, with weights omega_n <= C(n+1)^{3/2} L^{-alpha_H(n-1)} at age n = k+1-j (SA 7864). The step Gaussian carries x_k = beta - sum_{j<=k} b_j, so the consumed grouping is the subtracted one. Section 7.

**2.3 The gauge-fixing gradient off the axial locus.** GF_k(V) = sum_{y,x}[1 - (1/2) Re tr V(y,x)] is absolute (SA 7182). At a complex pair P_c = (U_c, J), U_c = e^{i eta A'}U, with M^k U block axial, V_c(y,x) = e^{i theta_{yx}} with theta_{yx} = O(C_L alpha_1) and theta_{yx} not zero in general. Then J-hat_GF(V_c) is not zero, and the next-fibre Hessian PX104 differs from the formula A(P_c) by exactly -C_V^T E_V^(2)[J-hat_GF] C_V. This is the term the a2-layers gate found. It is O(alpha_1), not a counterexample to the half-gap, and it vanishes wherever V_c(y,x) = 1 exactly. The physical complex pairs, obtained by continuing the axial representative in the datum, are of that kind. Section 4.

**2.4 Decoupling parameters near the support.** Without the sigma_0 convention, a walk of length zero in a parameter cube carries s^omega = s(cube). At s = 0 the corresponding diagonal block of chi A(s) chi then vanishes, and coercivity fails outright. Mechanism (i) exempts the first 2^4 cubes near a walk's start for this reason (SA 10552). With sigma_0 but with parameters allowed next to the support, nothing forces an s-dependent walk across any distance. The walk bounds then give no smallness to couplings amplified by e^{kappa-bar}, and the gap does not follow. That is a failure of the proof route, not a counterexample, because the walk decomposition is not unique and its terms have no lower bounds. The outline removes both problems: only coarse cubes outside the collar Z_0^# carry parameters (SA 14160). Section 8 proves the gap given the walk bounds, with the collar width chosen after kappa-bar.

**2.5 Complex coefficient ratio.** Re<u, tau A u> >= (Re tau) c_L||u||^2 - |Im tau| ||A|| ||u||^2. This needs an upper bound on ||A||. The bound is supplied in Section 5 (Lemma 5.1), so |tau - 1| <= c_L/(4(c_L + C_A)) suffices.

No counterexample to a consumed statement was found. Tests 2.1 and 2.2 kill two readings of item (2): the fine-form route for profiles, and comparison of the unsubtracted arrays. They fix where each comparison must be made.

## 3. Item (1): A is the consumed next-step Hessian at the pair of the step

**Setting.** Notation of `a2-layers.md` §1 and SA 10106-10208. A separated sequence (Omega_j)_{j<=k+1}, cut at depth k for the fine problem, with inward bonds omitted. Fine fields A live on the bonds with both ends in Omega_0. S(A) := A_in(e^{i eta A}U) is the action of the inner plaquettes (all four bonds in Omega_0), and Delta^W = D^2 S(0). All transposes and gradients use one physical pairing <.,.> (eta^4 per fine bond). The gauge action is U(b) -> u(b_-) U(b) u(b_+)^{-1}, with the start-point convention U_A = e^{i eta A}U (SA 10129). D lambda(b) = eta^{-1}(lambda^+(b) - lambda(b_-)) with lambda^+(b) = Ad(U(b)) lambda(b_+). A *physical pair* is (U, j_U): U is a real regular critical point for its datum (A1, `a1-balaban.md`, row 81), j_U := grad S(0) is its inner-action current, and V = M^k U is block axial, V(y,x) = 1, on the blocks of Omega_{k+1}. These blocks contain no node except their centre (SA 9783; `a2-layers.md` 2.3). At such pairs all inverses below exist (`a2-layers.md` Theorems 4, 5, A; 7.2(iv) gives W = Q G Q^T invertible, so Q is onto).

**Lemma 3.1 (projection algebra).** With M' = Q'G'^2 Q'^T: R^T = R, R^2 = R, Q'G'R = 0, R Delta_U G' R = R, Q S = Q, R D^T S = 0, S D G' R = 0.

*Proof.* G' and M' are symmetric, so R^T = R. R^2 = 1 - 2G'Q'^T M'^{-1} Q'G' + G'Q'^T M'^{-1}(Q'G'G'Q'^T)M'^{-1}Q'G' = R. Q'G'R = Q'G' - (Q'G'^2 Q'^T)M'^{-1}Q'G' = 0. Delta_U G' = 1 - Q'^T a Q'G', so R Delta_U G' R = R^2 - R Q'^T a (Q'G'R) = R. QS = Q - QDG'RD^T = Q - D-bar Q'G'RD^T = Q, by QD = D-bar Q' (statement 3, SA 10299; PX38). R D^T S = R D^T - (R D^T D G' R) D^T = R D^T - R D^T = 0, since D^T D = Delta_U. S D G' R = D G' R - D G'(R Delta_U G' R) = 0. ∎

**Lemma 3.2 (the gauge identity, exactly).** At J = j_U the bilinear form of SA 10176-10185 satisfies Delta^W - Delta'_pi[j_U] = S^T Delta^W S. So the identity of SA 10189 and statement 3 holds, with the outline's explicit formula.

*Proof.* (i) *The gauge vector field.* For u = e^{it lambda}, (U_A)^u(b) = e^{it lambda(b_-)} e^{i eta A(b)} e^{-it lambda^+(b)} U(b). By the Baker-Campbell-Hausdorff formula to first order in t, and to first order in A, log(e^X e^Y e^Z) = X + Y + Z + (1/2)[X,Y] + (1/2)[Y,Z] + (terms of order t^2 or t A^2). So the generator is

    X_lambda(A) = -D lambda + (i/2)[lambda + lambda^+, A] + O(|lambda||A|^2),      (3.1)

with lambda at b_-. Write B(lambda, C) := (i/2)[lambda + lambda^+, C] = D X_lambda(0)[C]. (ii) *Invariance.* S is exactly invariant under every gauge transformation of the sites of Omega_0, since inner plaquettes use only field bonds. So <grad S(A), X_lambda(A)> = 0 for all A and lambda. Differentiate at A = 0 in the direction C:

    <D lambda, Delta^W C> = <j_U, B(lambda, C)>      for all lambda, C.      (3.2)

(iii) *Expansion.* Define T: site functions -> 1-forms by Delta^W D = T, so <T lambda, C> = <j_U, B(lambda, C)> by (3.2). S^T = 1 - D R G' D^T. With lambda_A = G'R D^T A, <A, D R G' D^T X> = <D lambda_A, X>. Expanding,

    <A, (Delta^W - S^T Delta^W S) C> = <T lambda_A, C> + <T lambda_C, A> - <D lambda_A, T lambda_C>.

The last term equals <D lambda_A, Delta^W D lambda_C>, which is symmetric in A and C. So it is -(1/2)<j_U, B(lambda_C, D lambda_A) + B(lambda_A, D lambda_C)>. (iv) *Matching.* The first two terms are (1/2)<j_U, i[lambda_A, C] + i[lambda_A^+, C] + i[lambda_C, A] + i[lambda_C^+, A]>. Since i[lambda^+, C] = -i[C, lambda^+], these are the first four terms of SA 10176-10185. In the third, lambda^+ = lambda + eta D lambda, so B(lambda_C, D lambda_A) + B(lambda_A, D lambda_C) = i[lambda_C, D lambda_A] + i[lambda_A, D lambda_C] + (i eta/2)([D lambda_C, D lambda_A] + [D lambda_A, D lambda_C]). The bracket in eta vanishes, which leaves the last two terms of SA 10176-10185. Reversing the gauge-action convention sends lambda to -lambda in (3.1) and leaves (3.2) unchanged. ∎

This closes the item "PX94-95 ... gauge identity, unchecked" of `a2-layers.md` §8.1 and `gates/a2-curved-gate.md` remark 2. The exact G_1^{-1} = K of `a2-curved.md` §§10, 12 now stands, not only up to O(gamma_0).

**Lemma 3.3 (stationarity with multiplier, PX93, along the branch).** On the whole datum polydisc, the Landau representative a(B) of the background satisfies R D^T a = 0, grad S(a) = K_a^T omega(B) and Q^st(a) = b(B), with omega(B) unique. Here K_a is the derivative of the straightened rows at a, and K_0 = Q. At B = 0: j_U = Q^T omega, and H^T j_U = H_1^T j_U = omega.

*Proof.* This is `a3-derivative.md` Lemma 6.2 and Proposition 6.4 (37), gated ADVANCE for the Landau identification in `gates/a3-derivative-gate.md`. Lemma 6.2 gets the multiplier from criticality, exact covariance and the node factor of Lemma 6.1. It is the correct form of the outline's PX93 argument: the exactly invariant directions are the gauge directions with node values matched (36), not those with Q'lambda = 0, and PX93's "Ward identity" step needs exactly this. Q is onto, since W = Q G Q^T is invertible (`a2-layers.md` 7.2(iv)), so omega is unique. Finally H^T j_U = (QGQ^T)^{-1} Q G Q^T omega = omega, and the same holds for H_1. ∎

**Lemma 3.4 (physical second variant, PX95-PX96).** At J = j_U: G_1^{-1} = S^T K_L S + D R D^T + Q^T a Q with K_L = Delta^W - Delta^(2)[omega]. Also G_1 D R = D G' R, R D^T H_1 = 0, S H_1 = H_1, and H_1^T K_L H_1 = W_1^{-1} - a, with W_1 = Q G_1 Q^T.

*Proof.* By definition (SA 10149-10153), G_1^{-1} = Delta^W + DRD^T + Q^T a Q - Delta'_pi[J] - S^T Delta^(2)[H^T J] S. At J = j_U, Lemma 3.2 and H^T j_U = omega give the first formula. Next, G_1^{-1} D G' R = S^T K_L (S D G' R) + D(R Delta_U G' R) + Q^T a D-bar(Q'G'R) = D R by Lemma 3.1, so G_1 D R = D G' R. Transposing, R D^T G_1 = R G' D^T. Then R D^T H_1 = R G' (QD)^T W_1^{-1} = (Q'G'R)^T D-bar^T W_1^{-1} = 0, and S H_1 = H_1. Finally H_1^T G_1^{-1} H_1 = W_1^{-1}, H_1^T DRD^T H_1 = ||R D^T H_1||^2 = 0 and H_1^T Q^T a Q H_1 = a, since Q H_1 = 1. Subtracting gives the last identity. ∎

**Lemma 3.5 (the coarse value Hessian, PX97 and PX100).** Let A_eff(B) := A(Phi(B)) = S(a(B)) on the branch, with reduced datum b(B). Then da/dB at 0 is h_B = H_1 Db(0), and D^2 A_eff(0) = Db(0)^T (W_1^{-1} - a) Db(0) + <omega, D^2 b(0)>. On the active mask (level-k bonds touching Omega_{k+1}, injected by iota) PX100 holds (`a2-layers.md` 2.3, confirmed by `gates/a2-layers-gate.md` §6). So the coarse precision there is iota^T (W_1^{-1} - a) iota and the coarse current is iota^T H_1^T j_U = iota^T omega.

*Proof.* The background is Phi(B) = (e^{i eta a(B)}U)^{u_B} (`a3-derivative.md` (37)), and the action is gauge invariant, so A_eff(B) = S(a(B)). By Lemma 3.3, dA_eff = <grad S(a), a'> = <omega, K_a a'> = <omega, Db B'>. So the derivative is omega(B)^T Db(B), and D^2 A_eff(0) = omega'^T Db + <omega, D^2 b>. Differentiating stationarity at 0 gives K_L h = Q^T omega', with Q h = Db B' and R D^T h = 0 (the slice is linear). Then G_1^{-1} h = S^T K_L h + Q^T a Q h = Q^T(omega' + a Db B'), using S h = h and S^T Q^T = Q^T. So h = G_1 Q^T(omega' + a Db B'), and applying Q gives omega' = (W_1^{-1} - a) Db B' and h = H_1 Db B'. ∎

**Lemma 3.6 (the next fibre, PX101-PX104).** Let q_V(D) = log(M(e^{iD}V) M(V)^{-1})/i on the level-k bonds touching Omega_{k+1}. Let Phi_V be its pivot graph, with D Phi_V(0) = C_V, and let h_V be the pivot injection with Dq_V(0) h_V = 1. For a C^2 function F of D with gradient J-hat at 0, the Hessian of F ∘ Phi_V at 0 is C_V^T D^2 F(0) C_V - E_V^(2)[J-hat], where E_V^(2)[J-hat][u, v] := <h_V^T J-hat, D^2 q_V(0)[C_V u, C_V v]>.

*Proof.* q_V(Phi_V(u)) = 0. Differentiating twice gives Dq_V(0) D^2 Phi_V(0)[u,v] + D^2 q_V(0)[C_V u, C_V v] = 0. Phi_V changes only pivot values beyond first order, so D^2 Phi_V(0)[u,v] = h_V z with z = -D^2 q_V(0)[C_V u, C_V v]. The chain rule gives D^2(F ∘ Phi_V)(0)[u,v] = <C_V u, D^2 F(0) C_V v> + <J-hat, h_V z>. ∎

**Theorem I (identification).** At a physical pair, consider the step's exponent D -> A_{Omega_0}(U_k(e^{iD}V)) + GF_k(e^{iD}V), restricted to the next fibre D = Phi_V(u). Here A_{Omega_0} = sum_{p in Omega_0} a_p is the inner action, the one for which the background is critical (SA 9612-9616). The remaining plaquettes of the exponent are P_bdry of Corollary IV.3. The Hessian in the free coordinates u of this exponent is

    C_V^T ( G^(2)_V + (Q G_1 Q^T)^{-1} - a - E_V^(2)[iota^T H_1^T j_U] ) C_V = A.

Here G^(2)_V is the Hessian at D = 0 of D -> GF_k(e^{iD}V) (SA 7878: x_k GF_k(e^{i g_k B} V) = (1/2) sum |B(y,x)|^2 + O(g_k|B|^3)), and E^(2)[H_1^T J] of SA 10204 is read with the pivot transpose that PX103 requires. In B units (A_k = g_k B, x_k g_k^2 = 1) this is Delta^(k) of SA 7604, and the identification of SA 10208 and SA 14108-14120 holds. The same identity holds at every complex datum of the A1 polydisc, if the representative is the outline's tower axial one relative to the real block axial reference (SA 7186: the contour variables of M^n U coincide with those of M^n U_0), continued holomorphically.

*Proof.* Apply Lemma 3.6 to F = A_eff + GF. D^2 A_eff on the mask is iota^T(W_1^{-1} - a) iota (Lemma 3.5; PX105 gives raw = per-length at xi_k = 1), with gradient iota^T omega = iota^T H_1^T j_U. D^2 GF = G^(2)_V, and its gradient J-hat_GF vanishes at V(y,x) = 1 (Lemma 4.1(a)). W_1 = Q G_1 Q^T with G_1 at J = j_U is the operator of SA 10150, by Lemma 3.4. For complex data: in the tower axial gauge the contour variables of M^k U are those of the real reference, so V(y,x) = 1 persists. Both sides are holomorphic on the polydisc: the left by A1, the right by `a2-layers.md` Theorem B at the regular complex pairs (U(B), J(U(B))) (SA 9801, the lemma of 1b.7). They agree on a real neighbourhood, where every real datum gives a physical pair. The identity theorem extends the equality. ∎

*Remark (Balaban's second expression).* H_1^T[G_1^{-1} - DRD^T - Q^T a Q]H_1 differs from (QG_1Q^T)^{-1} - a by -H_1^T D R D^T H_1 = -||R D^T H_1||^2, which is zero on shell by Lemma 3.4, as SA 10208 states.

## 4. Item (1), continued: the gauge-fixing gradient -C_V^T E_V^(2)[J-hat_GF] C_V

The outline defines A with G^(2)_V and without the gradient of GF (SA 10204). PX104 shows the next free precision contains -E_V^(2)[J-hat + J-hat_GF]. Theorem I covers V(y,x) = 1. This section treats every complex regular pair.

**Lemma 4.1.** Let GF_k(W) = sum_{y,x}[1 - (1/2) tr W(y,x)], the holomorphic continuation of SA 7182 (Re tr = tr on SU(2)). The sum runs over the blocks of Omega_{k+1}, which carry no extra node, and W(y,x) is the contour mean of SA 7065 (Federbush's mean, holomorphic near the identity).
(a) If V(y,x) = 1 for all (y,x), real or complex, then J-hat_GF(V) := grad_D GF_k(e^{iD}V)|_{D=0} = 0.
(b) Let (U_c, J) be a complex regular pair, U_c = e^{i eta A'}U, whose real part U has M^k U block axial on the blocks of Omega_{k+1}. Then V_c = M^k U_c has V_c(y,x) = e^{i theta_{yx}} with |theta_{yx}| <= C_L alpha_1, |J-hat_GF(V_c)(b)| <= C_L alpha_1 at every bond, and

    || C_V^T E_V^(2)[J-hat_GF(V_c)] C_V ||_{l^2 -> l^2} <= C_II alpha_1,      C_II = C_II(L).      (4.1)

*Proof.* (a) Put W_t(y,x) = (e^{itD}V)(y,x). The mean is a group element, so W_t(y,x) = e^{it delta_{yx}(D) + O(t^2)} V(y,x), with delta_{yx}(D) in sl(2,C) linear in D. At V(y,x) = 1, d/dt tr W_t(y,x) = i tr delta_{yx}(D) = 0, because sl(2,C) is traceless. (b) M^k is holomorphic and local. `a2-layers.md` Theorem B(a), from the recursion `a2-curved.md` (8.4)-(8.7) on a complex disc, gives |V_c(b) - V(b)| <= C_L alpha_1 on the level-k bonds near Omega_{k+1}. The contour means are finite holomorphic functions of the bonds of one block, so V_c(y,x) = V(y,x) + O(C_L alpha_1) = 1 + O(C_L alpha_1). Then d/dt tr W_t(y,x) = i tr(delta_{yx}(D) e^{i theta_{yx}}) = -tr(delta_{yx}(D) theta_{yx}) + O(|delta||theta|^2). Each bond enters the means of one block, linearly with a coefficient bounded by C_L, so |J-hat_GF(b)| <= C_L alpha_1. Finally E_V^(2)[J][u,v] = <h_V^T J, D^2 q_V(0)[C_V u, C_V v]>. Here h_V (pivot injection), D^2 q_V(0) (plain one-step second jet) and C_V (pivot elimination) are finite-stencil analytic functions of V, with norms at most C_L near V = 1 (`a2-curved.md` §5, (5.2)-(5.7), gated). Summing over rows with bounded overlap gives (4.1). ∎

**Theorem II (half-gap of the actual next-fibre operator at every complex regular pair).** Put A^full(P) := A(P) - C_V^T E_V^(2)[J-hat_GF(V_c)] C_V. Under the hypotheses of `a2-layers.md` Theorem B, together with (C_B + C_II)(alpha_1 + gamma_0) <= c_L/4, every complex regular pair P = (U_c, J) whose real part has M^k U block axial satisfies

    Re <u, A^full(P) u>_H >= (3/4) c_L ||u||^2,

and the same holds for chi_Y A^full chi_Y on every conditioning set. A^full = A wherever V_c(y,x) = 1, so at every physical pair (Theorem I). *Proof.* `a2-layers.md` Theorem B gives ||A(U_c,J) - A(U,0)|| <= C_B(alpha_1 + gamma_0), and A(U,0) >= c_L. Add (4.1). Conditioning is compression: extend a conditioned vector by zero (`a2-curved.md` (2.1)). ∎

This proves the a2-layers gate's "visible local repair" (`gates/a2-layers-gate.md` §7, first bullet). The gate left its bound on J-hat_GF and the operator norm as a claim; both are now proved. Either convention can be used downstream. One is A^full at every pair, with the bound above. The other is A itself, restricted to pairs with V(y,x) = 1, which includes every pair the step and its holomorphic continuation produce.

## 5. A two-sided bound for A, and coarse perturbation stability

**Lemma 5.1 (upper bound).** At every real regular pair, 0 < A <= C_A I on the free coordinates, with C_A = C_A(L). At complex regular pairs within Theorem B's neighbourhood, ||A(P)|| <= C_A + c_L/4.

*Proof.* G_1^{-1} <= 2 C_up in the X form (`a2-layers.md` 7.4). The variational formula for the positive G_1^{-1} gives <b, (Q G_1 Q^T)^{-1} b> = min_{Qh=b} <h, G_1^{-1} h> <= <E b, G_1^{-1} E b> <= 2 C_up K_E^2 ||b||^2. Here E is the right inverse of Q of `a2-layers.md` 5.4(c), ||E||_{row->X} <= K_E, and the row norm is the counting norm at xi_k = 1. Also a = a_0 = 1, ||E^(2)[H_1^T J]|| <= C_L C_omega1 gamma_0 (`a2-layers.md` 7.4, 7.5), ||G^(2)_V|| <= C_L (finite contour stencils) and ||C_V|| <= C_L. Positivity is Theorem A. The complex statement adds Theorem B's C_B(alpha_1 + gamma_0) <= c_L/4. ∎

**Lemma 5.2 (stability).** Let P be a complex symmetric form on the free coordinates and tau a complex number. Suppose Re A_0 >= (3/4) c_L, ||A_0|| <= C_A + c_L/4, ||P|| <= e and |tau - 1| <= t. Then

    Re <u, tau (A_0 + P) u>_H >= [ (3/4) c_L - t (c_L + C_A) - (1 + t) e ] ||u||^2.

So the bracket is >= c_L/2 if t <= c_L/(8(c_L + C_A)) and e <= c_L/10. The same holds after compression to any conditioning set. *Proof.* With z = <u, A_0 u>_H, Re(tau z) >= Re z - |tau - 1||z| >= (3/4) c_L ||u||^2 - t (C_A + c_L/4)||u||^2, and |<u, tau P u>| <= (1 + t) e ||u||^2. ∎

*Variant.* If tau multiplies only the action part, so that the precision is C_V^T(G^(2)_V + tau Delta_k)C_V (t governs the gauge-fixing weight and x the action, SA 7864), apply Lemma 5.2 with tau = 1 and the extra perturbation (tau - 1)C_V^T Delta_k C_V. Its norm is at most t C_A, by the proof of Lemma 5.1. So t <= c_L/(20 C_A) suffices.

Lemma 5.2 is the "relative Schur estimate" at the level where each perturbation actually enters: the coarse form on the free coordinates, in the counting norm in which A2 is stated (SA 3845). Fine-level perturbations, where any occur, pass to that level through `a2-curved.md` (7.1) (relative error e on the fine form gives 2e on the Schur complement, for e <= 1/4; gated). Test 2.1 shows the profile is not one of them. It also explains the complex coefficient ratio of SA 14196: |tau - 1| <= c(LM)^{-4} is far inside t <= c_L/(8(c_L + C_A)) once M is large.

## 6. Item (2), plaquette weights: signed layer profiles, sources and the boundary of Omega_0

**Setting.** This is the pair of the step. U_0 = U_{k+1} is real and critical for the depth-k sequence with datum V_k^bg (SA 7461). Phi(B) is the A1 chart in the level-k datum B (counting units, xi_k = 1). Phi(B) = (e^{i eta a(B)}U_0)^{u_B}, with Landau potential a(B), holomorphic on the sup-norm polydisc P_{r_B} (`a3-derivative.md` Proposition 6.4). A complex datum V_{k+1} of the next step is a point B_0 of this polydisc, since V_k^bg depends holomorphically on V_{k+1}. **Input (T4):** (1b) Theorem 4, first paragraph (`a3-derivative.md` §7). It is gated as an implication (rows 85, 89, 98, 100, 101). At the pair of the step it also reads U_0 in Reg, which is discharged same-model in `a3-close.md` with its gate pending (row 106). For every B in P_{r_B} and every row c, h_c = d a/d B(c) satisfies xi_y|h_c|_y + xi_y^2|grad h_c|_y <= C_1 e^{-theta d_B(y, y_c)}, with theta = delta_0/8. Also |P_a - 1| <= C(kappa + r_B) eta^2 xi_p^{-2} at every plaquette of e^{i eta a(B)}U_0 (7.6 there), and |a|, |grad a| <= C r_B in local units.

For a complex weight w on plaquettes (inner, or meeting Omega_0), put F_w(B) := sum_p w(p) A_p(Phi(B)), with A_p = 1 - (1/2) tr P_p. In the step's B-normalization, a term -sum_p (x(p) - x_k) A_p of the exponent has B-Hessian equal to that of F_w with w = (x(p) - x_k)/t, where t is the scaling number (t = x_k in the run, SA 7864). Its fibre Hessian is P_w := C_V^T D^2 F_w C_V - E_V^(2)[grad F_w] (Lemma 3.6). Let n(p) := k - j(p) be the depth of the layer of p.

**Lemma 6.1 (Cauchy locality).** For B_0 in P_{r_B/2} and rows c, c',

    |d_c d_{c'} F_w(B_0)| <= (C_6/r_B) sum_p |w(p)| eta^4 xi_p^{-4} e^{-(theta/2)(d_B(p,c) + d_B(p,c'))},
    |d_c F_w(B_0)| <= C_6 (kappa + r_B) sum_p |w(p)| eta^4 xi_p^{-4} e^{-theta d_B(p,c)},

with C_6 = C_6(L).

*Proof.* A_p is a class function of the holonomy, so A_p(Phi(B)) = A_p(e^{i eta a(B)}U_0). *One derivative.* In the exponential chart, d/ds A_p(e^{i eta(a + s h)}U_0) = DA_p(U_a)[Xi_a h], with Xi_a the bondwise dexp factor and |Xi_a - 1| <= C eta|a| <= C r_B (`a3-derivative.md` 7.3). For a left variation, d/dt P(e^{it eta v}U_a) = i X P with X = eta sum_r Ad(T_{r-1}) v(b_r) = eta^2 dfrak_{U_a} v(p) (PX115). Since tr X = 0, DA_p(U_a)[v] = -(i/2) eta^2 tr(dfrak v(p) (P_a - 1)). By PX117, |dfrak v - d v| <= C kappa eta xi^{-2}|v|, so |dfrak(Xi_a h_c)(p)| <= C xi_p^{-2} e^{-theta d_B(p,c)} by (T4). Hence

    |d/ds A_p(Phi(B + s e_c))| <= C (kappa + r_B) eta^4 xi_p^{-4} e^{-theta d_B(p,c)}      for all B in P_{r_B}.      (6.1)

This is the gradient bound, at B = B_0. *Two derivatives.* Put g(z_1, z_2) = A_p(Phi(B_0 + z_1 e_c + z_2 e_{c'})), holomorphic for |z_i| < r_B/4, and let g~ := g(z_1,z_2) - g(z_1,0) - g(0,z_2) + g(0,0). By (6.1) along segments, |g~| <= 2|z_2| C(kappa + r_B) eta^4 xi_p^{-4} e^{-theta d_B(p,c')}, and the same with z_1, c in place of z_2, c'. So on |z_1| = |z_2| = r_B/4, |g~| <= C r_B (kappa + r_B) eta^4 xi_p^{-4} e^{-(theta/2)(d_B(p,c) + d_B(p,c'))}. The subtracted terms each miss one variable, so they integrate to zero against (z_1 z_2)^{-2}, and Cauchy gives d_1 d_2 g(0) = (2 pi i)^{-2} ∮∮ g~ (z_1 z_2)^{-2}. Hence |d_1 d_2 g(0)| <= (16/r_B^2) C r_B (kappa + r_B)(...) <= (C_6/r_B)(...), using kappa + r_B <= 1. For c = c' use g(z) - g(0) and (2/2 pi i)∮(g(z) - g(0)) z^{-3} dz. Sum over p with the weights w(p). ∎

**Theorem IV (plaquette-weight perturbations).** Let rho = R_1 M_1 satisfy theta rho >= 64 log L and theta rho >= 16. Suppose |w(p)| <= omega_0 (1 + n(p)) for every plaquette p meeting Omega_0. Then for every B_0 in P_{r_B/2},

    ||P_w||_{l^2 -> l^2} <= C_IV omega_0,      C_IV = C_IV(L),      (6.2)

uniformly in depth, volume, regions and torus. If in addition w vanishes on every plaquette at d_B-distance less than D from the active mask, then ||P_w|| <= C_IV omega_0 (1 + D) e^{-theta D/8}.

*Proof.* *Pillar grouping.* A pillar y of scale xi_y holds at most 6(xi_y/eta)^4 plaquettes, with xi_p within a factor L of xi_y, and has d_B-diameter O(1). So sum_{p in y} eta^4 xi_p^{-4} <= 6 L^4, and d_B(p,c) >= d_B(y,c) - C. Let W_y := sup_{p in y}|w(p)| <= omega_0(1 + n(y)). *Layer separation.* An active row c (level k, touching Omega_{k+1}) has distance > rho - 1 to Omega_k^c in level-k units. A path from c to layer L_j must also cross L_{k-1}, ..., L_{j+1}, and each crossing costs >= rho in d_B (L_i has width > rho xi_i and weight xi_i^{-1}). So d_B(y,c) >= (rho/2) n(y). *Counting.* By the ball count of `a2-layers.md` §7.3 (rederived in `gates/a2-layers-gate.md` §7), #{y : d_B(y,c) <= R} <= C_L (1 + R)^5 L^{8R/rho}. So sum_y e^{-(theta/4) d_B(y,c)} <= C_L sum_m (2+m)^5 e^{(8 log L/rho - theta/4)m} =: K_L < infinity, since theta rho >= 64 log L. The same holds for sums over rows c', which carry O(1) rows per top. *Schur test.* By Lemma 6.1,

    sup_c sum_{c'} |d_c d_{c'} F_w| <= (C_6/r_B) 6 L^4 e^{C theta} sup_c sum_y W_y e^{-(theta/2)d_B(y,c)} sum_{c'} e^{-(theta/2) d_B(y,c')}.

Split e^{-(theta/2)d_B(y,c)} = e^{-(theta/4)d_B(y,c)} e^{-(theta/4)d_B(y,c)}. The first factor is <= e^{-theta rho n(y)/8}, and (1 + n) e^{-theta rho n/8} <= 1 for theta rho >= 16. So the right side is at most (C/r_B) omega_0 K_L^2, and by symmetry the same bound holds for columns. So ||D^2 F_w|| <= C omega_0 / r_B. In the same way sup_c |d_c F_w| <= C(kappa + r_B) omega_0 K_L. Then ||E_V^(2)[grad F_w]|| <= C_L sup|grad F_w| (the stencils of Lemma 4.1(b)), and ||C_V|| <= C_L. *Vanishing near the mask.* Only pillars with d_B(y,c) >= D - C contribute. Keep the factor e^{-(theta/8)d_B} and pay for (1 + n) with half of the rest. ∎

**Corollary IV.1 (signed layer profiles).** Input (H-prof): |x_k(p) - x_k| <= C_x (1 + n(p)), also for complex x. *Derivation from the outline.* SA 9767 asks -C <= x_q - x_{q'} <= C(q' - q). At consecutive q this gives |b_{q+1}| <= C. SA 6331 makes phi_i zero outside the small-field region of step i and one on its interior region. Proposition 2.3 (SA 17398) nests the regions: Omega_i ⊃ Lambda_i ⊃ Omega_{i+1}. Read "small-field region" as Omega_i and "interior region" as Lambda_i, each up to one cube of level i. Take p in the layer L_j = Omega_j \ Omega_{j+1}. For i <= j - 1, p lies in Omega_j ⊂ Lambda_i, so phi_i(p) = 1. For i >= j + 1, p lies outside Omega_i, so phi_i(p) = 0. The cube margins add at most two more indices. So x_k(p) - x_k = sum_{i<=k} b_i(1 - phi_i(p)) has at most n(p) + 3 nonzero terms, and C_x = 3C. The only unchecked step is the reading of the two region names, together with the premise that the step's background is formed on the label's regions (the determining sequence, SA 17440). SA 17640 states the same conclusion: "x_k + O(1+k-j) on the shell of level j". Then the signed-profile perturbation of the step's precision satisfies

    ||P_prof|| <= C_IV C_x |t|^{-1} = C_IV C_x g_k^2      (t = x_k),

on the whole datum polydisc P_{r_B/2}, for complex x and complex t with |t/x_k - 1| <= 1/2. With an interpolation parameter t_1 on a disc |t_1| <= R (the position-dependent coupling of the t_1-integral, SA 7460), the precision A + t_1 P_prof keeps the gap c_L/2 once R C_IV C_x g_k^2 <= c_L/10 (Lemma 5.2). That is a ceiling on g_k, chosen after R and L. Test 2.1 shows why this must be done at the coarse level: the decay across the layers pays for the growth (1 + n) of the profile, and the fine X-form norm has no such decay.

**Corollary IV.2 (source profiles).** For the running source shift of SA 22590, -A(x_k(.) - zeta_k(.; w), U), the extra weight is zeta_k/t. If |zeta_k(p; w)| <= C_zeta (1 + n(p)), then ||P_src|| <= C_IV C_zeta g_k^2. The bound on zeta_k belongs to the source lane (`parts/witness.md`, UV-CT). It is the only input this needs.

**Corollary IV.3 (boundary comparison, SA 10190).** A uses the Hessian of the inner action (SA 10141). The step's exponent also contains the plaquettes that meet Omega_0 without being inner, with weight x(p)/t, and |x(p)/t| <= 1 + C_x g_k^2 (1 + k) <= C(1 + n(p)) there, since n(p) = k on L_0. These plaquettes lie at d_B-distance >= rho(k+1)/2 - C >= rho/4 from the active mask. By the last clause of Theorem IV, their perturbation, including the linear-term contribution through E_V^(2), is at most C_IV (1 + rho) e^{-theta rho/32}. This is <= c_L/10 once rho >= rho_IV(L). That is a lower bound on R_1 M_1, chosen after L, as mechanism (a) allows.

## 7. Item (2), counterterm arrays

**What a comparison can and cannot use.** A level-j term E^(j)(X, U) acts on the step's fluctuation only through the background U_k(V(B)), which is nonlocal in B. Two crude routes fail, and both failures were checked by hand. (i) Without the subtraction of b_j A(phi_j), the coarse Hessian of the array is ~ sum_{j<=k} b_j g_k^2 ~ c_0 k g_k^2 (test 2.2; SA 7864). (ii) With it, a Cauchy bound in the field composed with the decay (T4), as in Lemma 6.1, gives per level-k cube about L^{4(k-j)} level-j domains. Each contributes (domain bound / alpha_{1,j}) L^{-(k-j)} e^{-theta d}. Even with the irrelevant bound q_j^3 eta_{k-j}^{4+alpha_H} on one side of a geometric mean, the sum grows like L^{(k-j)(3 - alpha_H)/2}. So the comparison must use the structure the outline builds for the integrand: polymers *in the fluctuation variable*, with the irrelevant size.

**Input (H-ct).** On the step's complex fluctuation domain {B : |g_k B(c)| < r_k for every active row c}, the subtracted brackets sum_{j<=k}{E^(j) - b_j A(phi_j, .)}, together with the aged remainders, admit a representation sum_Y F_Y(B). Here Y runs over connected unions of level-k cubes of side M, each F_Y is holomorphic and depends only on B on Y, and |F_Y| <= eps_ct e^{-kappa |Y|}, with eps_ct <= C sum_{n>=1} omega_n and omega_n <= C(n+1)^{3/2} L^{-alpha_H(n-1)} at age n = k+1-j. This is the outline's own accounting (SA 7864, with the regular-part bound of SA 7590 and the decoupled response 1c.10). It is upstream of A2 and unchecked here.

**Theorem V.** Under (H-ct), with kappa >= kappa_0(L, M), the fibre Hessian P_ct of the brackets (B-normalization, the fibre graph in B coordinates) satisfies

    ||P_ct||_{l^2 -> l^2} <= C_V eps_ct (g_k / r_k)^2,      C_V = C_V(L, M).

*Proof.* In B units the polydisc has radius r_k/g_k. For c, c' in Y, the two-variable Cauchy formula gives |d_c d_{c'} F_Y(0)| <= sup|F_Y| (g_k/r_k)^2, and the one-variable formula gives |d_c F_Y(0)| <= sup|F_Y| (g_k/r_k). A cube carries at most C M^4 rows, and at most C_0^n polymers of n cubes contain a given cube. So sup_c sum_{c'} |d_c d_{c'} F| <= sum_n C_0^n C M^4 n eps_ct e^{-kappa n} (g_k/r_k)^2, which is finite for kappa > log C_0 + 1, and the Schur test bounds the Hessian. The fibre graph in B coordinates is u -> g_k^{-1} Phi_V(g_k u), whose second derivative is g_k D^2 Phi_V(0). So the curvature term is g_k E_V^(2)[grad F] <= C_L eps_ct g_k^2/r_k <= C_L eps_ct (g_k/r_k)^2 for r_k <= 1. ∎

With r_k ~ alpha_{1,k} = g_k C_1 (log g_k^{-2})^{q_1} (Balaban CMP 119 (2.28); the outline's radii run the same way, SA 7455), (g_k/r_k)^2 = C_1^{-2}(log g_k^{-2})^{-2 q_1}. This is small but only logarithmically, so it costs a ceiling g_k <= g_*(L, M). With an interpolation parameter |t_2| <= R (the young terms "in a measure which itself contains them", SA 7460), the gap c_L/2 survives once R C_V eps_ct (g_k/r_k)^2 <= c_L/10.

*Remark.* Where the consumer keeps these brackets in the integrand instead of the precision, as (FG5) allows, no comparison with A is needed. The brackets are bounded on the sharp test domain, so they enter F_0 rather than rho. Theorem V is needed only for a consumer that absorbs their quadratic part into the Gaussian.

## 8. Item (3), coercivity on the enlarged complex decoupling arrays

**The consumer.** SA 14158-14190: chi = chi_{Z_0}, C(Z_0; s) = (chi A(s) chi)^{-1}, with independent |s_Delta| <= e^{kappa-bar} on the coarse cubes outside the collar Z_0^#, and A(s) obtained from the walk expansion of A (statement 5, SA 10315: chi_Y A chi_Y "taken at the pairs that are regular for the longer sequence"). The parameter convention is mechanism (i), SA 10552. A walk omega carries s^omega = prod over the parameter cubes in P(omega) not among the first 2^4 near its first cell. For |s| <= e^{kappa-bar} and delta >= C kappa-bar/l_P, |s^omega| e^{-delta d_B(omega; y, y')} <= e^{2^4 kappa-bar} e^{-(delta - C kappa-bar/l_P) d_B(y,y')}.

**Input (H-walk), statement 5 for chi_Y A chi_Y.** A = sum_omega A_omega with |A_omega(y,y')| <= C_A' (C M_1^{-1/2})^{|omega|} M_1^{-|omega|/2} e^{-delta_0 d_B(omega; y, y')}, with at most C^m tree walks of length m from a given first cell (SA 10548), and A(s) := sum_omega s^omega A_omega. The same bounds hold at the complex regular pairs used, with A_omega holomorphic on the local class on [omega]. This is an A3/(1c.8)-(1c.9) statement and is not proved in this checkout. `a2-layers.md` §7.2 has the exponential Combes-Thomas bounds for G, G_1 and the row Gram, which are the inputs mechanisms (f), (g) need, but no walk expansion.

**Theorem VI.** Let delta_0 >= 2C kappa-bar/l_P and M_1 >= M_*(C). Suppose every parameter cube lies at d_B-distance >= w from Z_0. Then for all independent |s_Delta| <= e^{kappa-bar},

    || chi (A(s) - A) chi || <= C_VI e^{2^4 kappa-bar} e^{-delta_0 w/4},

with C_VI = C_VI(L, C_A'). So if w >= (4/delta_0)(2^4 kappa-bar + log(20 C_VI/c_L)), then Re <u, chi A(s) chi u>_H >= Re <u, chi A chi u>_H - (c_L/20)||u||^2 at every pair where the input holds. With Theorem II this is >= (3/4 - 1/20) c_L at complex regular pairs, on every conditioning set. The same holds for A^full, since the gauge-gradient term is local (finite stencil on the mask) and carries no parameter.

*Proof.* Only walks with P(omega) beyond the first 2^4 cubes contribute to A(s) - A, and for y, y' in Z_0 such a walk meets a parameter cube. Every tree admitted in d_B(omega; y, y') then passes through y and through a cell near that cube, so d_B(omega; y, y') >= w - C. Split e^{-delta_0 d_B(omega)} into three factors e^{-(delta_0/2)d_B(omega)} e^{-(delta_0/4)d_B(omega)} e^{-(delta_0/4)d_B(omega)}. Mechanism (i) with delta = delta_0/2 >= C kappa-bar/l_P bounds |s^omega| times the first factor by e^{2^4 kappa-bar}. The second is <= e^{-(delta_0/4)(w - C)}. Then |s^omega - 1| |A_omega(y,y')| <= 2 e^{2^4 kappa-bar} e^{-(delta_0/4)(w - C)} C_A' (C M_1^{-1/2})^{|omega|} e^{-(delta_0/4) d_B(omega; y, y')}. Sum over walks: for each first cell there are C^m walks of length m, so (C M_1^{-1/2})^m C^m is summable for M_1 large. Sum over y' with the remaining factor and d_B(y,y') <= d_B(omega; y, y'): the count of Theorem IV gives a constant. The Schur test finishes. ∎

**Order of constants.** This is the outline's order (SA 10582). First L, and with it c_L, C_A, the rates theta and delta_0, and the ceilings on alpha_0, alpha_1, gamma_0 from Theorems A, B and II. Then M_1 and rho = R_1 M_1, with theta rho >= 64 log L and rho >= rho_IV(L). Then kappa-bar. Then l_P >= 2C kappa-bar/delta_0. Then M, which fixes the collar width w >= (4/delta_0)(2^4 kappa-bar + log(20 C_VI/c_L)); SA 14183 has the collar cost e^{C kappa-bar - cM}. Then the field strengths. Last, the coupling ceiling g_k <= g_*(L, M, R) of Corollary IV.1 and Theorem V, which is new. No constant chosen earlier depends on a later one.

*Why the collar matters.* The proof uses w only through e^{-delta_0 w/4}, which must beat e^{2^4 kappa-bar}. With parameters next to the support, the s-dependent terms of chi A(s) chi include walks of length one, of size up to C_A'(C M_1^{-1/2}) M_1^{-1/2}, amplified by up to e^{2^4 kappa-bar}. The walk bounds then give no gap once e^{2^4 kappa-bar} M_1^{-1} is not small. Whether the gap actually fails there depends on the expansion chosen, so this is recorded as a limit of the method (test 2.4), not as a counterexample.

## 9. Assembly: A2 in the scope its consumers read

**Theorem A2-full.** Fix L >= L_0 and choose the constants in the order of Section 8. Let P be the pair of a step: real, or a point of its complex datum polydisc P_{r_B/2}, with the representative continued in the tower axial gauge (SA 7186), so that V(y,x) = 1. The consumed precision is

    A_cons := C_V^T(G^(2)_V + tau Delta_k)C_V + t_1 (P_prof + P_src) + P_bdry + t_2 P_ct,

with |tau - 1| <= c_L/(20 C_A) and |t_1|, |t_2| <= R. Assume the hypotheses of `a2-layers.md` Theorems A and B with the gate's repairs, the ceiling of Theorem II, (T4), (H-prof), the source bound of IV.2, (H-ct), rho >= rho_IV(L), and g_k <= g_*(L, M, R) such that

    R C_IV (C_x + C_zeta) g_k^2 <= c_L/20,   C_IV(1 + rho) e^{-theta rho/32} <= c_L/20,   R C_V eps_ct (g_k/r_k)^2 <= c_L/20.

Then Re <u, chi_Y A_cons chi_Y u>_H >= (c_L/2 + c_L/20)||u||^2 on every conditioning set Y. Under (H-walk), with the collar w >= (4/delta_0)(2^4 kappa-bar + log(20 C_VI/c_L)), the decoupled precision chi(A_cons - A + A(s))chi keeps Re >= (c_L/2)||u||^2 for all independent |s_Delta| <= e^{kappa-bar}. At every other complex regular pair, Re A^full(P) >= (3/4) c_L (Theorem II). At the pair of the step, Theorem I identifies C_V^T(G^(2)_V + Delta_k)C_V with the next-fibre Hessian of PX104.

*Proof.* At the step's pair A^full = A (Lemma 4.1(a)), and Theorem II gives Re A >= (3/4) c_L, with ||A|| <= C_A + c_L/4 (Lemma 5.1). The coefficient ratio costs at most c_L/20 (Lemma 5.2, variant). Corollaries IV.1-IV.2, Corollary IV.3 and Theorem V cost at most c_L/20 each, by the three displayed ceilings. That is 4 c_L/20 in all, so Lemma 5.2 leaves (3/4 - 1/5) c_L = (c_L/2 + c_L/20). Theorem VI with this collar costs at most c_L/20 more. Compression to Y is `a2-curved.md` (2.1). ∎

Here the perturbations P_prof, P_src, P_bdry, P_ct are taken undecoupled, as SA 14158-14190 decouples only A. A consumer that also decouples them needs the analogue of (H-walk) for them. The Schur bounds of §§6-7 then apply term by term.

## 10. Verdict, what stays open, what changes

| Item (row 109) | Verdict | Where | Reads |
|---|---|---|---|
| (1) A = consumed next-step Hessian at the pair of the step, PX93-PX104 | **proved** (finite-dimensional, every identity written; the gauge identity re-derived from BCH) | §3 Theorem I, Lemmas 3.1-3.6 | A1 (row 81); PX100 (gated in `gates/a2-layers-gate.md` §6); `a3-derivative.md` Lemma 6.2, Prop. 6.4 (gated) |
| (1) the term -C_V^T E_V^(2)[J-hat_GF] C_V | **proved**: zero at V(y,x) = 1 (all physical pairs and their continuation); <= C_II alpha_1 at every complex regular pair; half-gap of A^full | §4 Lemma 4.1, Theorem II | `a2-layers.md` Theorem B; `a2-curved.md` §5 |
| (2) signed layer profiles | **proved as an implication**, at the coarse level: ||P_prof|| <= C_IV C_x g_k^2 on the whole datum polydisc, complex weights included. The fine X-form route of the queue text is **refuted** (test 2.1) | §6 Lemma 6.1, Theorem IV, Cor. IV.1 | (T4) (gated; U_0 in Reg via row 103, gate row 106 pending); (H-prof), derived from SA 6331, 9767 and Prop. 2.3 (SA 17398) up to the reading of two region names |
| (2) boundary comparison (SA 10190), source profiles | **proved as an implication** (boundary: no new input; sources: given a bound on zeta_k) | Cor. IV.2, IV.3 | (T4); source lane for zeta_k |
| (2) counterterm arrays | **proved as an implication** from the outline's polymer accounting; unsubtracted arrays and field-Cauchy routes **refuted** (test 2.2, §7) | §7 Theorem V | (H-ct): SA 7590, 7864, 1c.10, unchecked |
| (2) relative Schur step | **proved** at the coarse level where the perturbations enter (Lemmas 5.1-5.2); `a2-curved.md` (7.1) remains for fine-level ones | §5 | `a2-layers.md` 5.4(c), 7.4 |
| (3) enlarged complex decoupling arrays | **proved as an implication** from statement 5 for chi_Y A chi_Y, with the collar and l_P chosen after kappa-bar | §8 Theorem VI | (H-walk): statement 5 / 1c.8-1c.9, **not in this checkout** |

**Defects found, ranked by what they break.**
1. *The queue's route for item (2), a fine X-form bound plus the relative Schur estimate, is false for the signed profile* (test 2.1: the relative weight b k g_k^2 is unbounded across depth). It breaks nothing in the outline, which never puts the profile into the fine form. Any note that adds the profile to Delta^W must instead use Theorem IV.
2. *SA 10204 needs the pivot transpose.* E^(2)[H_1^T J] must be read as E_V^(2)[iota^T H_1^T J] with h_V^T, as PX103 says. Without it the identification of SA 10208 is off by the difference of the two multipliers. Repair: the reading in Theorem I.
3. *SA 10208 / 14111 assert the identification at P_W without a gauge clause.* At a complex pair off the axial locus it fails by -C_V^T E_V^(2)[J-hat_GF] C_V (test 2.3). Repair: Theorem I with the tower axial continuation, or A^full with Theorem II.
4. *The PX93 "Ward identity" step* as written uses gauge directions with Q'lambda = 0. Those directions are not exactly invariant at A != 0 (§3, Lemma 3.3). The correct argument is `a3-derivative.md` Lemma 6.2, with node factors. The conclusion j_U = Q^T omega stands.
5. *`a2-layers.md` §1 calls "V block axial" a normalization, "gauge covariance of all operators" making it no restriction.* That holds for G', R, S, G_0, G, H, G_1, H_1, Delta_k and C_V. It fails for G^(2)_V and J-hat_GF. The absolute GF of SA 7182 is invariant only under gauge transformations that are constant on each block, since GF(V^u) = sum[1 - (1/2) tr(u(y) V(y,x) u(x)^{-1})]. So a2-layers' Theorems A and B are statements at pairs with V axial. At other real pairs A is a different operator. Harmless: the step's pairs are axial (SA 7866), their continuation stays axial (tower axial gauge, SA 7186), and Theorem II covers complex pairs whose real part is axial. Repair: state the axial condition as a hypothesis, as Theorem II does.

No counterexample to a consumed statement was found.

**What stays open, hardest first.**
1. **(H-walk): statement 5 for chi_Y A chi_Y** at the regular pairs of the longer sequence (walk expansions with the (C M_1^{-1/2})^{|omega|} bound, holomorphic terms, real at real pairs, covariant). It is the only input of item (3), and an A3/(1c.8)-(1c.9) obligation, not A2. Templates exist. `path_expansion_locality.md` Lemma 1 is the path expansion of an inverse from local inverses with commutator smallness. `flat-port.md` §11 gives walk bounds for the flat local systems, and `a2-layers.md` §7.2 gives the curved Combes-Thomas bounds. Mechanism (h) (SA 10550) makes (Q G_1 Q^T)^{-1} a block of the inverse of a finite-range saddle system. So the next lane should build local inverses of that saddle system on patches, then use mechanism (g), the tree treatment, for H_1^T J. No walk expansion of chi_Y A chi_Y exists in this checkout.
2. **(H-ct): the polymer form of the counterterm brackets in the fluctuation variable** with the irrelevant size (SA 7590, 7864; 1c.10). This is upstream RG accounting ((1d), (2a)), not A2.
3. **(H-prof)**: reduced in Corollary IV.1 to the reading "small-field region of step i" = Omega_i and "interior region" = Lambda_i (SA 6331), and to the premise that the step's background lives on the label's regions. The rest follows from SA 9767 and Proposition 2.3.
4. Cross-provider gate of this note. Look hardest at Lemma 3.2 (signs of the BCH term), Lemma 6.1 (the double-difference Cauchy step and the use of (T4) at complex data), the layer-separation bound d_B(y,c) >= (rho/2)n(y) in Theorem IV, and Theorem VI's use of mechanism (i).
5. Outside A's definition and not treated: the patch Gaussian of SA 17645 (Balaban CMP 122 (1.71); profile weights on the action and on the gauge term, degenerate where phi = 0), and the seam node terms of GF (SA 7758-7761, boundary exponent).

**What changes for the lead (evidence only; no other file was edited).**
- `sa-ledger.md` rank 2 (A2): once a cross-provider gate confirms §§3-8, A2 holds in the scope its consumers read. It is conditional only on (H-walk), (H-ct) and (H-prof), which belong to other ranks (A3 locality, RG accounting), on the zeta_k bound for consumers with sources, and on the pending gates of its inputs ((T4) reads U_0 in Reg, row 103, gate row 106).
- The non-Abelian, nonzero-current, layered, signed-profile and complex versions are then done. The identification of A with the step's Hessian is done, and the "enlarged-complex-domain" version reduces to statement 5.
- `gates/a2-curved-gate.md` remark 2 and `a2-layers.md` §8.1 (PX94-95 gauge identity) are closed by Lemma 3.2. The exact identity G_1^{-1} = K of `a2-curved.md` §§10, 12 now holds, not only up to O(gamma_0).
- `gates/a2-layers-gate.md` §7 "visible local repair" for the complex gauge term is proved (Theorem II), and its "Full A2 scope" obligation is discharged as far as A2 is concerned.
- Item (2)'s route in the queue text should be corrected: profiles are compared at the coarse level, by (T4) decay, not in the fine X-form.

**Moves:** `sa-ledger.md` rank 2 (A2), from separated layers to its full consumed scope.

**Method.** Every step is a written argument; no computation, enumeration or numerics. No numerical job was run; the numeric lock was not needed. No subagent. Only this file was written.

Credit, repeated for the parts used: the obligation, operators, physical diagram PX93-PX105, localized Gaussian comparison, profiles, step anatomy and walk mechanisms are due to Ethan Sussman and Levent Alpoge, with Claude and Codex as authors of their text (`31a47c543775`). The background-field programme, separate currents, position-dependent couplings and decoupling parameters are T. Balaban's (CMP 102, 109, 116, 119). The layered operator estimates are Claude's `a2-layers.md` with Codex's gate repairs. The curved one-step and second-jet inputs are Codex's `a2-curved.md` with Claude's gate. The response bounds are the gated A3 chain (`a3-derivative.md`, `p82-curved.md`, `flat-port.md`, `a1-balaban.md`, with their gates).
