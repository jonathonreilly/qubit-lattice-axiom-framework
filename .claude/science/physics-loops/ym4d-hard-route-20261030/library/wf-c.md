lead: anthropic/claude-opus-5-5/max mac-mini-worker
lease_until: 2026-11-04T05:15Z

# WF-c: complex box localisation, Landau node lift, pointed-core admission

Row 173. Pinned at commit b264f9a3c. Finished 2026-11-03 (worker); research text, no status.

Provenance: Claude Opus 5.5 (`claude-opus-5-5`), effort max, Mac mini worker, fresh session. Research text, not an audit; it grants no status. Outline: Sussman–Alpoge `YM4_sketch_500.tex` at `31a47c543775`; SA numbers are its lines. No numeric job was run.

Credit: Ethan Sussman and Levent Alpoge, with Claude and Codex as authors of their text, for the window maps, the pair class (R4)–(R6), Theorems 5 and 6 of (1b) and the box-map package. T. Balaban for background localisation (CMP 109, 116 as cited there) and the axial/Landau gauge constructions (CMP 95, 96, 102). OpenAI Codex for `ld-decoupled.md`, `b4-step.md`, `nl-r9.md`, `pw-bridge.md`.

## 1. Check of `ld-decoupled.md` (Codex)

Checked line by line by Claude, Sections 2–4 and the new arithmetic of Section 1. Section 1 is itself Codex's check of `cond-c.md`; it is not re-reviewed (FINISH, How we work 5), except its frame-factor display.

**Verdict: (LD) ADVANCE.** Checked line by line by Claude, first failing step none. It is an implication from [PW] (`pw-bridge.md` (6.6)–(6.7), Section 7), [NL] (`nl-r9.md` Section 6, `dec-field.md` (5.1)), AV, BC and the WF domains.

What was redone:

- *(1), floors.* θ_L = (τ_L/16)min(M,ρ) = τ_Lρ/16 ≥ τ_Lρ'/16 ≥ 16 log L. Correct.
- *(2), rates.* `pw-bridge.md` (6.4)–(6.6) already pay the tags: the column bound has rate τ_L/8 after the factor e^{16κ̄}e^{128κ̄t/ℓ_P} with ℓ_P ≥ 2048κ̄/τ_L. A weight of rate λ = τ_L/16 then leaves τ_L/16 for the column sum, as (6.7) states. The 16 + 128t/ℓ_P count is (6.4) verbatim (two traversals, arcs of length ℓ_P/4, sixteen cubes each by (P)).
- *(3), BC.* For the determining sequence Lemma G of `cond-c.md` gives d(Ω_i^c, Ω_{i+1}) ≥ Mξ_{i+1} ≥ c_gξ_i. The segment between the last exit from Ω_i^c and the next entry into Ω_{i+1} lies in layer i, where the weight is 1/ξ_i. There are k−p−1 such disjoint segments for a start in layer p. Correct; it is `geo-5.md` Section 3.6.
- *(4)–(5), weighted fixed point.* Contraction constants q = C_WB³R ≤ 1/8 and q_C = 2C_CBR ≤ 1/4 match `dec-field.md` Proposition 5.1. The weighted step needs W(0) = 0 and C(0) = 0 and the weighted Lipschitz bounds on unweighted balls; `nl-r9.md` Section 6 and its Result state both. The weighted norms are finite on a finite torus, so absorption is legitimate. B/((1−q)(1−q_C)) = 32B/21 ≤ 2B. Correct. The same bound also follows by integrating (5.2) of `dec-field.md` along tB', 0 ≤ t ≤ 1.
- *(6).* The X norm is sup_y w(y) max{ξ_y|a|, ξ_y²|∇a|} (`dec-field.md` Section 5), so the sum in (6) costs a factor 2, absorbed in C.
- *(7) and (LD).* On the path V(ν) = e^{iη_k(t+νζ)h}U_+ the tangent is exactly ζh, since h_b commutes with its multiples. AV with (6) gives |v'_c| ≤ C δ_k (ξ_c/ξ_p) e^{−θ_L(k−p−1)_+}, |ζ| ≤ 1. This is the form `cond-c.md` 6.4 reads.
- *Section 1, frame factor.* √(b+1) ≤ √2 e^{b−1} for b ≥ 1 (equality at b = 1, and the right side grows faster). So ρ_j e^{−θ_L(b−1)} ≤ C√(1+a) e^{−(θ_L−1)(b−1)}. Correct.

Clarifications, none a defect: (i) the fine-layer pointwise size of h is δ_k/ξ_p, larger than the top-layer δ_k/ξ_k by L^{k−p}; the factor e^{−θ_L(k−p−1)} pays it, which is why θ_L > log L matters. (ii) The proof reads the step's own sequence for both d_B and BC; that is the common determining sequence of `cond-c.md` Lemma E, so no second metric enters.

## 2. Item (1): Theorem 6(c) at complex data

**Result of this section (proved by Claude, not yet checked by the other model).** The common collar chart that `b4-step.md` Section 3 (2) names as its first unproved input holds, on every instance of its family (1) and in setting (1b). It follows from one new estimate, Lemma C: the complex collar datum stays within C(κ + ‖w‖_*) of the lift. The proof does not rerun Lemma 10.3 at complex fields, which is where `b4-step.md` (4) stopped. It perturbs the real Corollary 10.4 by left factors e^{iγ} of unitaries, whose sizes sum geometrically over the collar levels. With the complex restriction identity (Lemma RC, identity theorem) and T4 on the polydisc of a real reference, this gives Theorem 6c^C, which is SA 6(c) at complex data with all three members, the current and the gauge.

### 2.1 Setting, conventions, inputs

- B is a separated sequence with local scale l and metric d_B. W is a single μ-collared part (SA 9783–9789): a union of aligned cubes of side μξ_j whose collar C (its O(1) outermost cube layers) lies in the single layer j of B. B' is the joined sequence. (G1)–(G3) of `a3-derivative.md` Section 10 hold ((G1) discharged in `a3-close.md`, row 103). Hence d_B ≤ d_{B'} on W, ω := e^{θ d_B(·,W^c)} lies in 𝒲_θ for d_{B'}, and every collar row c has d_B(y_c, W^c) ≤ c_1μ (R3).
- *Old rows* are rows of B with carrier in W; they are rows of B' (Lemma 10.2 (ii)–(iii)). *Collar rows* are the new rows of B', of level q < j, in C. A collar row b has its end points in level-j blocks B(y_±). Either y_− = y_+, or b leads from B(c_−) into B(c_+) for a level-j row c = (y_−, y_+) of B (a *corridor* bond).
- Gauge action U^g(b) = g(b_−)U(b)g(b_+)^{-1}, so (U^a)^b = U^{ba}, and (e^{iηY}V)^g = e^{iηY^g}V^g with Y^g(b) = Ad(g(b_−))Y(b). Norms of Lie-algebra elements are matrix operator norms; Ad by a unitary is an isometry.
- ‖w‖_* := sup_b l(b)|w(b)| for a complex potential w on W.

Inputs, with their standing:

- [AV] The averaging bootstrap (`a1-balaban.md` 3.5, gate row 91 Section 1), as used in the proofs of `wf-room-2.md` Lemma A′ and `o1-decoupled.md` Lemma RI. If U is real with curvature at most κη²l^{−2} on the carriers and ‖w‖_* ≤ r_*, then M^m(e^{iηw}U)(b) = e^{iβ_m(b)}M^m(U)(b) with |β_m(b)| ≤ 2t_m sup_{P(b)}|w|, t_m = L^mη, for every level-m bond b whose carrier lies in the region. Checked (rows 91, 125).
- [PA] Plaquettes of averages: if U is real with a local regular gauge of potential at most κη/l and curvature at most κη²/l², then ϖ_m := sup|∂M^m(U) − 1| ≤ C_Lκ(t_m/l)² (`a3-derivative.md` (7); its proof reads only these initial bounds). Checked (row 89).
- [CR] `a3-derivative.md` Lemma 10.3 and Corollary 10.4 (real, unitary transports). Checked (row 89).
- [FM] The Federbush mean is holomorphic and Lipschitz near a common transport (`a3-derivative.md` 4.1).
- [P81], [P82°], [T4] for B and for B': `a3-derivative.md` Sections 6–8 with Lemma 8.2, and `wf-room-2.md` Lemma D (all-site gauge factor). Checked as implications (rows 89, 91, 100, 101, 125).
- [9.3] The real restriction identity (`a1-balaban.md` 9.2), and [AX]: the canonical representative is the unique element of its orbit in axial gauge outside the nodes, with all comb transports of averages equal to 1 down each pillar (SA 9667–9671; `a1-balaban.md` 9.1). Checked (row 91).

### 2.2 Lemma C: the complex collar datum

For a configuration 𝐔 on W near the unitary group define:

- (D1) the multilevel block-axial gauge G[𝐔] on the collar sites: G[𝐔] = 1 at level-j sites; for x of level m < j in the level-(m+1) block of y, G[𝐔](x) = G[𝐔](y)·T_m[𝐔](y,x). Here T_m is the contour variable of M^m(𝐔) from y to x in B(y): the comb transport, or the Federbush mean over the contour family. Outside C put G[𝐔] = 1.
- (D2) for a collar row b of level q: V^U[𝐔](b) = G(b_−)M^q(𝐔)(b)G(b_+)^{−1}, and V^J[𝐔](b) = 1 if y_− = y_+, = M^j(𝐔)(c) on a corridor of c. On old rows V^U[𝐔] = V^J[𝐔] = M_B(𝐔).
- (D3) Q[𝐔](b) = V^U[𝐔](b)V^J[𝐔](b)^{−1}.

Covariance gives T_m[𝐔^G](y,x) = G(y)T_m[𝐔](y,x)G(x)^{−1} = 1, so 𝐔^{G[𝐔]} is block axial at every collar level. Thus V^U[𝐔] = M_{B'}((𝐔|_W)^{G[𝐔]}) is the restricted datum after the node gauge, and V^J[𝐔] is the joined datum (SA 9786) of M_B(𝐔). These are exactly the V^U, V^J of `a3-derivative.md` (R2) and Corollary 10.4.

**(N) Node covariance.** For a gauge transformation h on W, G[𝐔^h](x) = h(y_j(x))G[𝐔](x)h(x)^{−1}, where y_j(x) is the level-j site above x. Hence V^U[𝐔^h](b) = h(y_−)V^U[𝐔](b)h(y_+)^{−1}, the same for V^J, and Q[𝐔^h](b) = h(y_−)Q[𝐔](b)h(y_−)^{−1}.

*Proof.* Induction down the levels: at level j both sides are 1. If it holds at y, then G[𝐔^h](x) = h(y_j)G[𝐔](y)h(y)^{−1}·h(y)T_m[𝐔](y,x)h(x)^{−1} = h(y_j)G[𝐔](x)h(x)^{−1}. Insert this and M^q(𝐔^h)(b) = h(b_−)M^q(𝐔)(b)h(b_+)^{−1} in (D2); the lift is 1 = h(y)1h(y)^{−1} inside a block and M^j(𝐔^h)(c) = h(y_−)M^j(𝐔)(c)h(y_+)^{−1} on a corridor. □

**(P) Left-perturbation product inequality.** For unitary W_1, …, W_N and complex γ_i, ‖∏(e^{iγ_i}W_i) − ∏W_i‖ ≤ e^{Σ|γ_i|} − 1 and ‖(∏e^{iγ_i}W_i)^{±1}‖ ≤ e^{Σ|γ_i|}. Also We^{iγ} = e^{iAd(W)γ}W with |Ad(W)γ| = |γ|.

*Proof.* Telescope: ∏Y − ∏W = Σ_k Y_1⋯Y_{k−1}(e^{iγ_k} − 1)W_kW_{k+1}⋯W_N, with Y_i = e^{iγ_i}W_i. The k-th term has norm at most (∏_{i<k}e^{|γ_i|})(e^{|γ_k|} − 1), and these sum to e^{Σ|γ_i|} − 1. The inverse is ∏ reversed of W_i^{−1}e^{−iγ_i}, which the last identity puts in the same form. □

**Lemma C.** There are κ_C, r_C > 0 and C_C ≥ 1, depending on L and the contour convention only, with the following property. Let U be real on the carriers in W of the collar rows and comb blocks. Suppose U has, in a local regular gauge, potential at most κη/l and curvature at most κη²/l², with κ ≤ κ_C. Let w be complex with ‖w‖_* ≤ r_C, and put 𝐔 = e^{iηw}U. Then:

- (a) G[𝐔], V^U[𝐔], V^J[𝐔] and Q[𝐔] are holomorphic in w, and unitary at real w.
- (b) at every collar site, |G[𝐔]^{±1}| ≤ e^{C_C‖w‖_*}, and G[𝐔] = e^{iΓ}G[U] with |Γ| ≤ C_C‖w‖_*;
- (c) at every collar row, |Q[𝐔] − 1| ≤ C_C(κ + ‖w‖_*);
- (d) if ‖w‖_* ≤ r_C/2 and ‖h‖_* ≤ 1, then |D_wQ[e^{iηw}U][h]| ≤ C_C.

The constants do not depend on j, q, the depth, the volume or the number of collar levels.

*Proof.* *Step 1 (real reference).* At w = 0 every contour variable is unitary, so G[U] is unitary. Corollary 10.4 bounds |Q[U](b) − 1| = |M^q(U^G)(b) − lift(b)| by C_LΣ_{q≤m<j}ϖ_m, since the lift is unitary. Its proof reads only Lemma 10.3 for the real block-axial fields M^m(U^G) and their plaquette bounds ϖ_m. On the collar l = ξ_j, so [PA] gives ϖ_m ≤ C_Lκ L^{2(m−j)}, which is below Lemma 10.3's threshold for κ ≤ κ_C. Hence |Q[U](b) − 1| ≤ C_Lκ Σ_{m<j}L^{2(m−j)} ≤ C'_Lκ.

*Step 2 (averages).* By [AV], M^m(𝐔)(b) = e^{iβ_m(b)}M^m(U)(b) with |β_m(b)| ≤ 2L^{m−j}‖w‖_* for every level-m bond of the collar and every corridor level-j bond, since t_m = L^{m−j}ξ_j there. This fixes r_C ≤ r_* and κ_C ≤ r_*.

*Step 3 (contour variables).* A comb has at most 4L level-m bonds, so (P) gives |T_m[𝐔] − T_m[U]| ≤ e^{8L^{1+m−j}‖w‖_*} − 1. For the mean, each contour transport is perturbed in the same way, and [FM] gives |T_m[𝐔] − T_m[U]| ≤ C_F(e^{C_LL^{m−j}‖w‖_*} − 1). Since T_m[U] is unitary, write T_m[𝐔] = e^{iγ_m}T_m[U] with |γ_m| ≤ C_TL^{m−j}‖w‖_*, using |log(1 + E)| ≤ 2|E| for |E| ≤ 1/2.

*Step 4 (gauge).* G[𝐔](x) is the product, down the pillar from y_j(x), of the factors e^{iγ_m}T_m[U]. By (P) its norm and inverse norm are at most exp(C_TΣ_{m<j}L^{m−j}‖w‖_*) ≤ e^{C_T‖w‖_*/(L−1)}, and the same telescoping gives (b).

*Step 5 (Q).* Q[𝐔](b) is the ordered product of G[𝐔](b_−), M^q(𝐔)(b), G[𝐔](b_+)^{−1} and V^J[𝐔](b)^{−1}. Each factor is a product of left-perturbed unitaries (move the perturbations to the left with the isometry in (P)). The total perturbation is at most C_1‖w‖_*, with C_1 = 2C_T/(L−1) + 4. The unperturbed product is Q[U](b). So |Q[𝐔](b) − Q[U](b)| ≤ e^{C_1‖w‖_*} − 1 ≤ 2C_1‖w‖_*, and Step 1 gives (c).

*Step 6 (holomorphy, derivative).* Each object is a finite composition of averages, Federbush means near unitaries, products and inverses. These are holomorphic on ‖w‖_* < r_C by [AV] and [FM], and real at real w. This is (a). For (d), Q[e^{iη(w+ζh)}U](b) − Q[U](b) is holomorphic in |ζ| < r_C/2 and bounded by e^{C_1r_C} − 1 ≤ 1. Cauchy's estimate gives |D_wQ[h]| ≤ 2/r_C. □

So the step at which `b4-step.md` (4) stopped is not needed. There the factors are complex transports with unknown condition numbers. Here every factor is e^{iγ} times a unitary, and Σ|γ| is a geometric series in L^{m−j}.

### 2.3 Corollary CC: the common collar chart (`b4-step.md` (2))

**Corollary CC.** In the setting of Lemma C put V_* := V^U[U] (real). Then V^U[𝐔] = e^{ib_U}V_* and V^J[𝐔] = e^{ib_J}V_*, with b_U, b_J holomorphic in w and real at real w, and:

- b_U = b_J on old rows, so supp(b_U − b_J) lies in the collar rows;
- ‖b_U‖_∞ ≤ C_C'‖w‖_*, ‖b_U − b_J‖_∞ ≤ 6C_C(κ + ‖w‖_*), and |∂(b_U − b_J)[h]| ≤ C_C'' for ‖h‖_* ≤ 1, ‖w‖_* ≤ r_C/2 (chain rule, with Lemma C(d) and the Lipschitz bound of the logarithm near 1);
- V_* is a real C_*κ-regular datum for B'. Indeed U^{G[U]}|_W is real, and its curvature in B'-local units is at most κ, since ξ' ≤ l. The converse bound of SA Theorem 1 (`a1-balaban.md` 9.2) then applies.

*Proof.* On old rows, [AV] gives b_U = b_J = β_q(c), |β_q(c)| ≤ 2L‖w‖_*. On collar rows, V^U[𝐔](b) is the left-perturbed unitary product of Step 5 without its last factor, so b_U(b) is its logarithm relative to V_*(b), of size at most C‖w‖_*. Next b_J = (1/i)log(Q[𝐔]^{−1}e^{ib_U}). The function X ↦ log(e^{−X}e^{ib}) − ib vanishes at X = 0 and is holomorphic for ‖X‖, ‖b‖ ≤ 1/4, so it is at most 3‖X‖ for ‖X‖ ≤ 1/8. With ‖log Q‖ ≤ 2|Q − 1|, Lemma C(c)–(d) give the bounds. □

This is `b4-step.md` (2) with regularity radius a := κ + ‖w‖_* and C = 6C_C, once (2L + 6C_C + C_C')(κ + ‖w‖_*) < r'_B/2, the chart radius of B' at V_*. The constants, chart margin and gauge bounds are independent of depth and volume.

**The two settings.**

- *Setting (1b), complex datum increments.* V_r is real ε_1-regular, U_r = Φ(0), and Φ(β) = (e^{iη𝓗(β)}U_r)^{u(β)} (Proposition 6.4). P81's local gauges give κ = C_L𝔐ε_1. (31) gives ‖𝓗(β)‖_* ≤ C‖β‖_∞, and Lemma D(i) gives |u(β) − 1| ≤ C‖β‖_∞ at every site. Apply Lemma C to e^{iη𝓗(β)}U_r and then (N) with h = u(β). On old rows M_B(Φ(β)) = e^{iβ}V_r exactly. Here it is cleaner to take V_* := V^J[U_r] = V^J_r. Then b_J(β) = β^J, the lift of β: β on old rows, β(c) on the corridors of c, and 0 inside blocks. Also b_U(β) = (1/i)log(Q[Φ(β)]e^{iβ^J}) on collar rows, so ‖b_U − b_J‖_∞ ≤ C(ε_1 + ‖β‖_∞).
- *The WF family of `b4-step.md` (1).* 𝐔_ν = e^{iη_k(t+νζ)𝐇_k(P;s,B')}U_+(P) with U_+(P) = e^{iηA'}U, and T is the first-rule box tower of a Rule W window R_z. Theorem C2 of `cond-c.md` gives R_z ⊂ Ω_j^0 ∩ Ω_j^1. So the old truncation S^{≤j} has constant depth j on R_z, and T is the joined sequence of the single part R_z, with collar in the single layer j. (G1)–(G3) hold by (C) and Definition A (gaps > ρξ'_q). U satisfies the hypothesis of Lemma C with κ = C_potMα_0 (the real gauge clause of (R4), on a box of side C_boxLM ⊃ R_z). Write 𝐔_ν = e^{iηw_ν}U, w_ν = A' ⊞ (η_k/η)(t+νζ)𝐇_k (bondwise BCH). Then ‖w_ν‖_* ≤ 2α_1 + C(1+|ν|)‖𝐇_k‖_X ≤ 2α_1 + C(δ_k + c_να_k), by dec-field (5.2) ([PW], [NL]) on |ν| < c_ν/s_k. Since ∂_νw_ν = ζ(η_k/η)𝐇_k + O(α_1|𝐇_k|), Lemma C(d) gives |∂_ν(b_U − b_J)| ≤ Cδ_kσ_j on collar rows, the datum-lemma input (4.4) of `wf7-extension.md`.

In both settings the bounds hold on the whole polydisc |s_Δ| < e^{κ̄}, for all independent currents, 0 ≤ t ≤ 1 and |ν| < c_ν/s_k. They read (s, 𝐉) only through 𝐇_k, holomorphically. The box pair carries the current of its own background (SA 15955), so no independent current enters the box map.

### 2.4 Lemma RC: restriction at complex data

**Lemma RC.** In setting (1b), with P81 for B and B' and (G1)–(G3), let Φ' be the P81 chart of B' at V^J_r. Let ‖β‖_∞ < r_1, with r_1 so small that ‖b_U(β)‖_∞ < r'_B/2. Put X(β) := (Φ(β)|_W)^{G[Φ(β)]}. Let g_ax(β) be the B'-axial gauge fixing of X(β): g_ax = 1 at the nodes of B', and g_ax(x) = g_ax(z)T^{B'}_n[X](z,x) at a non-node site x of B'-level n with block centre z. Then:

- (i) X(β)^{g_ax(β)} = Φ'(b_U(β));
- (ii) g_ax is holomorphic in β and unitary at real β, with |g_ax^{±1}| ≤ e^{C(ε_1+‖β‖)};
- (iii) g_ax = 1 at every site of an interior pillar, that is, a pillar of B in W∖C, which is also a pillar of B' (SA 9786).

*Proof.* *Real β.* Lemma 10.2 ((9.3) for the joined sequence) makes Φ(β)|_W critical and regular for (B', M_{B'}(Φ(β)|_W)). A real gauge maps constraint sets onto constraint sets and preserves the action. So X(β) is critical and regular for (B', V^U[Φ(β)]) = (B', e^{ib_U}V^J_r). A1's uniqueness for B' puts X(β) in the G^res(B')-orbit of Φ'(b_U(β)). The transformation g_ax is 1 at nodes and makes every comb transport of averages equal to 1, so [AX] gives (i).

*Complex β.* Both sides of (i) are holomorphic on the connected polydisc. The left side composes Φ, Lemma C's G and comb transports of averages of X near unitaries. The right side is Φ' ∘ b_U. They agree at real β, so the identity theorem gives (i) everywhere.

*(ii).* By (N) and covariance, g_ax(x) is a node value times a product of contour variables of e^{iη𝓗}U_r, times (uG)(x)^{−1}. Each contour variable is a left-perturbed unitary (Lemma C, Step 3), so (P) applies.

*(iii).* On an interior pillar G = 1, and Φ(β) satisfies B's axial condition. That condition holds at real β, hence at complex β by the identity theorem. B''s axial condition there is the same condition on the same averages, which read only W∖C. So the recursion gives g_ax = 1 site by site. □

### 2.5 Theorem 6c^C

**Theorem 6c^C (SA 1b Theorem 6(c) at complex data; implication).** Assume P81 and P82° for B and B' above the floors, (G1)–(G3), and the collar in one layer j. Let V_r be real and ε_1-regular below the P81 ceiling. For ‖β‖_∞ < r_1 put U°_W(β) := Φ'(β^J), the localised background at the complex joined datum e^{iβ^J}V^J_r. Then

  Φ(β)|_W = (e^{iηf(β)}U°_W(β))^{w(β)},

with f and w holomorphic in β, f real and w unitary at real β, and the following bounds. Here θ = δ_0/8 and C_μ = C e^{θ(c_1μ + D_L)}, with C depending on L and ρ only.

- (i) Over every top y of B', ξ'_y|f| + ξ'²_y|∇f| + ξ'³_y|D^*Df| ≤ C_μ(ε_1 + ‖β‖_∞) e^{−θ d_B(y,W^c)}.
- (ii) Current. At every bond b whose six plaquettes lie in W, J(Φ(β))(b) = Ad(w(b_−))(J(U°_W(β))(b) + δJ(b)), with ξ'³_b|δJ(b)| ≤ the bound in (i).
- (iii) Gauge. At every site x of an interior pillar, |w(x) − 1| ≤ C_μ(ε_1 + ‖β‖_∞) e^{−θ d_B(x,W^c)}. At every site of W, |w|·|w^{−1}| ≤ e^{C‖β‖_∞}. At real β, w is unitary but need not be near 1 in the collar, as SA allows.

*Proof.* Let U'_* := Φ'(0) = U°_W(0). It is real, regular and critical by P81, and Φ'(b) = (e^{iη𝓗'(b)}U'_*)^{u'(b)} (Proposition 6.4 for B'). Write 𝓗'_U = 𝓗'(b_U), 𝓗'_J = 𝓗'(β^J), and the same for u'.

*T4 along the collar segment.* The segment b_s = β^J + s(b_U − β^J), 0 ≤ s ≤ 1, lies in the r'_B/2-ball. The forcing D𝖻(b_s)[b_U − β^J] lives on collar rows and their D_L-neighbours. By (R3) and (30), its Y_ω-norm is at most C_b e^{θ(c_1μ+D_L)}‖b_U − β^J‖_∞. Then (33)–(34) with Lemma 8.2 bound Δ := 𝓗'_U − 𝓗'_J = ∫_0^1 D𝓗'(b_s)[b_U − β^J]ds by ‖Δ‖_{X,ω} ≤ (4/3)C_linC_b e^{θ(c_1μ+D_L)}‖b_U − β^J‖_∞. Sections 7.1, 7.3 and 7.5, with Lemma D(i) of `wf-room-2.md`, give the same bound for ξ'³|D^TDΔ|, for the current difference J(e^{iη𝓗'_U}U'_*) − J(e^{iη𝓗'_J}U'_*) (at bonds with plaquettes in W), and for |u'_U − u'_J| at every site. All are weighted by ω^{−1}. The operator bound contains the row sum, so no collar count enters. Corollary CC gives ‖b_U − β^J‖_∞ ≤ C(ε_1 + ‖β‖_∞).

*Algebra.* Put f̃ := (1/iη)log(e^{iη𝓗'_U}e^{−iη𝓗'_J}) bondwise, f := Ad(u'_J(b_−))f̃, and w' := u'_U(u'_J)^{−1}. From (e^{iηY}V)^g = e^{iηY^g}V^g,
  e^{iηf}Φ'(β^J) = (e^{iηf̃}e^{iη𝓗'_J}U'_*)^{u'_J} = (e^{iη𝓗'_U}U'_*)^{u'_J},
so (e^{iηf}U°_W)^{w'} = Φ'(b_U). By Lemma RC, Φ(β)|_W = (Φ'(b_U))^{G^{−1}g_ax^{−1}}. So the theorem holds with w := G^{−1}g_ax^{−1}w'.

*Sizes.* The BCH function vanishes at 𝓗'_U = 𝓗'_J and η|𝓗'| ≤ Cη/ξ' is small, so |f̃ − Δ| ≤ |Δ| and |f| ≤ 4|Δ|. The forward covariant difference is covariant: ∇_{V^g}(Ad(g)Y) = Ad(g)∇_VY. Hence ∇_{U°_W}f = Ad(u'_J)∇_{e^{iη𝓗'_J}U'_*}f̃, and changing the transport costs C|𝓗'_J| per factor. This gives ξ'²|∇f| ≤ C(ξ'²|∇Δ| + ξ'|Δ|), and in the same way ξ'³|D^*Df| ≤ C(ξ'³|D^*DΔ| + ξ'²|∇Δ| + ξ'|Δ|). This is (i).

For (ii), the current is based at the initial site, so J(V^g)(b) = Ad(g(b_−))J(V)(b). At bonds whose plaquettes lie in W, J(Φ|_W) = J(Φ). Then δJ = Ad(u'_J)[J(e^{iη𝓗'_U}U'_*) − J(e^{iη𝓗'_J}U'_*)], which is bounded above.

For (iii), on an interior pillar G = 1 and g_ax = 1 (Lemma RC (iii)), so w = w'. Also |w' − 1| ≤ |u'_U − u'_J||(u'_J)^{−1}|. Elsewhere use Lemma C(b) and Lemma RC(ii). □

*Remarks.*

- (1) SA writes w = v_q[f]^{−1} at the tops away from the collars. Here w = v'[𝓗'_U]^{−1}v'[𝓗'_J] there (by (37) for B'), the node factor of the same difference computed over U'_*. Consumers read only (iii).
- (2) *WF setting.* With V_* = V^U[U] and the box tower T, the same proof applies verbatim to the two box pairs F_T(V^U[𝐔_ν]) and F_T(V^J[𝐔_ν]) over the common real reference U_T(V_*). It uses P81 and P82° for T, which is a separated Definition A tower. The amplitude is C_μ(κ + ‖w_ν‖_*), and by Lemma C(d) the ν-derivative of the comparison carries Cδ_kσ_j. This is the compatible boundary comparison of SA 15822 and 16849 for the box backgrounds, in the weighted form of `wf7-extension.md` (4.5), whose common-chart premise Corollary CC now supplies.
- (3) *(H-pair) of `o1-decoupled.md` for the background replacement.* Take G = W, D = d_B(·,W^c), X = f, g = w, δ𝐉 = δJ, θ_P = θ and ε_P = C_μ(ε_1 + ‖β‖_∞). The condition ε_P ≤ c_Pa_min is a ceiling on ε_1 and ‖β‖, chosen after μ. For an *independent* current in the original pair, δ𝐉 also contains the difference of the prescribed reduced-current assignments. That difference is a specification item outside 6(c) (`wf-room-2.md` 6.3 (S6)). The box-first route does not form removed pairs, so it does not read this case.
- (4) The single-map chart that `wf7-bf.md` Section 3 assumes ("T4 throughout the datum paths") needs less than Corollary CC. By [AV] alone, m_T(𝐔_ν) = e^{iB(w_ν)}m_T(U) with |B| ≤ 2L‖w_ν‖_* on every row of T, collar rows included. This is the (R5) chart of SA 5696.

**Counterexample attempts (done first).**

- (a) *Complex transports with large condition number* (`b4-step.md` (4)). These cannot occur here. Every complex factor is e^{iγ} times a unitary average of the real factor, with Σ|γ| ≤ C_1‖w‖_* (Steps 2–5).
- (b) *Depth growth.* The number of collar levels j − q is unbounded, but the perturbations decay like L^{m−j}, and the real errors like L^{2(m−j)}. No constant grows.
- (c) *A pure-gauge real factor* (`wf-room-2.md` C4). Lemma C reads U only through gauge-invariant plaquettes and its real local gauge. The node gauge enters only through (N), as a conjugation at level-j nodes.

No failure.

## 3. Item (2): the node-lift comparison (H-node)

(H-node) (`o1-decoupled.md` 3.1, `removed-fix.md` (5.18)) asks, in the assigned representatives of the two compared maps, for |g(x) − 1| ≤ ε_N e^{−θ_P D_x} on G, where g is the gauge of (H-pair). Its only readers are Theorem D of `o1-decoupled.md` and `removed-fix.md`, and only for the assigned-representative bound. Their common-gauge bound (removed-fix (5.17)) does not read it.

**Proposition N (proved by Claude, not yet checked by the other model).** In the setting of Theorem 6c^C, with D = d_B(·,W^c), C_μ and θ as there, and G' := the union of the interior pillars:

- (a) *Canonical representatives with common nodes.* The P81 charts Φ and Φ' are the axial representatives, and the relating gauge is g = w. On G', w = w' = u'_U(u'_J)^{−1}. So
  |g(x) − 1| ≤ C_μ(ε_1 + ‖β‖_∞) e^{−θD_x} at every site of G'.
  This includes the nodes, where w = v'[𝓗'_U]^{−1}v'[𝓗'_J], and every bare site below them, by the all-site Landau-factor bound used in Theorem 6c^C (iii). The collar pillars satisfy D ≤ c_1μ + C_L. Hence on all of W, (H-node) holds with ε_N = C_μe^{θ(c_1μ+C_L)}(ε_1 + ‖β‖_∞) outside G' and the bounded condition number of Theorem 6c^C (iii) inside C. This is the case the queue row names. The proof is the axial recursion of [AX] from the node values, with Lemma D(i) of `wf-room-2.md` for every site.
- (b) *Landau representatives over a common real reference.* Suppose both maps are read in their Landau representatives over the same real reference U'_*. This is the case of the two box pairs of Remark (2) of Section 2.5, over U_T(V_*), and of the inner substitution over **1** (SA 5(c)). The representatives are e^{iη𝓗'_U}U'_* = e^{iηf̃}·e^{iη𝓗'_J}U'_*. So (H-pair) holds with g = **1** exactly and X = f̃, and (H-node) holds with ε_N = 0. The two Landau factors themselves satisfy |u'_U − u'_J| ≤ C_μ(ε_1 + ‖β‖_∞)e^{−θD} at every site.
- (c) *Landau representatives over two different real references* (B over U_r, B' over U'_*). On G' the relating gauge is k = u(β)^{−1}u'(b_U(β)). This is the ratio of the B-Landau and B'-Landau factors of the *same* configuration, since Φ(β)|_W = Φ'(b_U) on G' by Lemma RC. At β = 0, k = u'(B_0), which decays from the collar. For β ≠ 0, the two factors are node factors of two Landau potentials of the same orbit, under the gauge conditions R_BD^*_{U_r} = 0 and R_{B'}D^*_{U'_*} = 0. Their gauge difference e^{iχ} solves, to first order, R_{B'}Δχ = (R_{B'} − R_B)D^*(·) + R_BD^*f_0 + (quadratic), with node data Q'χ that decays like f_0. So |k − 1| decays from the collar **if** (SC) holds:
  (SC) the kernel of R_B − R_{B'} decays like e^{−θ(d_B(x,C)+d_B(y,C))}, in a common frame on W.
  The natural proof of (SC) is the resolvent identity G'_B − G'_{B'} = G'_B(L'_{B'} − L'_B)G'_{B'}, with L' = Δ + Q'^*aQ'. The two operators differ only on the collar (pillar averages and a = ξ^{−2}) and by the reference change f_0. The identity is then combined with the weighted G' bounds of P82° and the explicit formula for R through G', Q' and the site Gram matrix (SA PX41). **(c) is not proved here.** No counterexample was found: the scalar sector is massive through Q'^*aQ', so the effect of the collar should decay.

**What this settles.**

- (a) and (b) are proved, from Theorem 6c^C and T4.
- The box-first route compares only maps over one reference: the box map with itself along a datum path, the two box pairs of the compatible boundary comparison, and the inner triple over **1**. This is case (b). It evaluates gauge-invariant member values (`wf7-bf.md` Section 2), so it reads neither (c) nor any (H-node) at all.
- (c) is read only by the assigned-representative form of the removed-current bound, whose route the box-first construction replaces (`cond-c.md`, `wf7-bf.md`). There Theorem D's common-gauge bound already suffices.
- So (c) moves off the critical path. If a later consumer needs it, its first unproved step is (SC).

## 4. Item (3): pointed-core admission (10.2) beyond its hereditary part

(10.2) of `a1-balaban.md` is SA (BGR32) with its reference margin (SA 12296–12333). For every actual substitution curve X_ν on the retained disc and every clause a of its assigned core, ‖R_a(X_ν) − R_a(X_0)‖ < ε_ar_a and ‖R_a(X_0)‖ ≤ (1 − ε_a)r_a. The hereditary part is closed: Lemma T of `a3-close.md` (tower clauses from simple ones, checked in `gates/a3-close-meet-gate.md`) and Theorem I of `o1-decoupled.md` (inner triple, no K^♯ loss). What is left is the simple clauses along the actual curves, with their currents, nodes and gauges, and the reference margins.

**Which curves the adopted route forms.**

- On the box-first route with Rule W (`wf7-bf.md`, `cond-c.md`), the window identity (2) of `wf7-bf.md` is exact and contains only box terms: Φ_ζ(s,t,ν) = G̃_{j,z}(X, F_T(m_T(𝐔_{t,ν}))), with 𝐔_{t,ν} = e^{iη_k(t+νζ)𝐇_k(P;s,B')}U_+(P). No outer and no removed term is formed.
- G̃ is gauge invariant (`wf7-bf.md` Section 2). So the only core membership read is that of the box pair, in its Landau reading (`wf-room-2.md` 7.4): the inner Landau triple P_in(B_{t,ν}) := (**1**, 𝓗(B_{t,ν}), J(e^{iη_j𝓗})) on X. Here B_{t,ν} := (1/i)log V is the node-reduced box datum of Lemma N at 𝐔_{t,ν}.
- Rule W puts X and its current stencil inside T_j(R_z), a single level j (`wf7-bf.md` Section 2). So the layered X that `o1-decoupled.md` 4.5 excludes does not arise.

Hence (10.2) on this route consists of two statements: (A1) the input curve 𝐔_{t,ν} has the hypotheses of Lemmas N and E, and (A2) the inner triple lies in its core with margin.

**Theorem A (implication; proved by Claude, not yet checked by the other model).** Let P be a pair of the step's local core at half radii (α_0/2, α_1/2), including its □_0-tower clause at radius α_0/2. Assume [PW] (`pw-bridge.md`, `dec-field.md` (5.2)), (LD) (`ld-decoupled.md`, checked in Section 1), (O1) (`o1-decoupled.md` Theorem B), Theorem L and Corollary R of `wf-room-2.md`, Lemmas N and E there, and Theorem I with the order of constants of `o1-decoupled.md` 4.5. Use the radius convention α_k ≤ C_αα_{0,k} stated in the proof. There is c_A > 0, depending on L, ρ, M, C_α and the fixed constants and not on j, k, the depth or the volume, such that the following hold if s_k < c_ν/2 and c_ν ≤ c_A. Every |s_Δ| < e^{κ̄}, independent current, 0 ≤ t ≤ 1 and |ν| < c_ν/s_k is covered.

- (A1) 𝐔_{t,ν} satisfies the simple conditions (R4) of its level, at the full radii (α_0, α_1), on a cube of side C_boxLM containing R_z. Here the level is k+1 at top-layer base points, and the local layer p at lower-layer base points in ambient local units. The same holds for the real-gauge clause and the □_0-tower clause at radius α_0. The current of the outer pair, 𝐉 + 𝗃 by (6.1) of `wf-room-2.md`, also satisfies its clause, although the inner substitution does not read it.
- (A2) P_in(B_{t,ν}) ∈ U°_j(X; α_{0,j}, α_{1,j}, α_{0,j}). Every simple and every hereditary clause is at most 4/5 of its radius, and at most 1/2 when the age m := ℓ(z) − j is at least 1. Here ℓ(z) is the level of Rule W's partition at z: k at (W1), p − 1 at (W2), j at (W3).

*Proof of (A1).* Write h := (η_k/η)(t+νζ)𝐇_k. Then |t + νζ|δ_k ≤ δ_k + c_να_k ≤ (s_k + c_ν)α_k, since δ_k = s_kα_k. [PW] gives ξ_y|h| + ξ_y²|∇h| ≤ C(s_k + c_ν)α_k at top-layer points. In layer p, (LD) and its weighted form (6) give the factor e^{−θ_L(k−p−1)_+}. Each clause then moves by at most the following, in units of its radius:

- *real-factor curvature and real-gauge clause:* 0. The shift enters A' only; U is unchanged.
- *curvature of 𝐔:* the plaquette expansion (P2) gives |∂(e^{iηh}𝐔) − ∂𝐔| ≤ C(ξ²|∇h| + ξ|h|(ξ|A'| + ξ|h|) + ξ|h|α_0)η²ξ^{−2}. This is ≤ C(s_k + c_ν)α_kη²ξ^{−2}, which is at most CC_α(s_k + c_ν) times the radius α_0η²ξ^{−2}. *Radius convention used here:* α_k ≤ C_αα_{0,k}, with C_α fixed before the radii. This holds if WF1's "analytic field radius" is the curvature-type radius, as SA 5(c) measures the response (|𝐀| < cα_{0,k}). It also holds if α_k = α_{1,k} with α_1 ≤ C_αα_0, for example α_1 = C'Mα_0, which the relation Mα_0 ≪ α_1 permits. If instead α_1 ~ √α_0 were taken, this line would need s_k + c_ν ≤ cα_0/α_1, and c_ν would shrink with the radii.
- *|A'|, |∇_UA'|:* A' ↦ A' ⊞ h moves them by at most C(ξ|h| + ξ²|∇h|) ≤ C(s_k + c_ν)α_1.
- *current:* (6.4) of `wf-room-2.md` with (O1) from Theorem B gives ‖𝗃‖_F ≤ CC_H(1 + C_Hα_0)‖𝐇_k‖_X|t+νζ| ≤ C(s_k + c_ν)α_0.
- *tower clauses (□_0 at level k+1, and every hereditary clause):* Theorem L(b) bounds the change of every tower quantity by 2C_b sup‖h‖_{1,y}. In layered position, Corollary R gives the change with premise (i) from `ld-decoupled.md` (5) (rate γ_H = τ_L/16 from the step-data set E) and premise (ii) from BC (`ld-decoupled.md` (3)). Its ratio to the shrinking gap β_s2^{−n} is at most (C'/β_s)(s_k + c_ν) once γc_gML ≥ log 4.

So every clause moves by at most C_A(s_k + c_ν) ≤ 2C_Ac_ν of its radius. Choose c_A with 2C_Ac_A ≤ 1/8. Each clause of P is at most 1/2 of its radius (input), so by the triangle inequality each clause of 𝐔_{t,ν} is at most 5/8 of its full radius. This is (BGR32) with X_0 = P and ε_a = 3/8. The bound is uniform in s and 𝐉, because [PW], (LD), (O1) and (6.4) are.

*Proof of (A2).*

- (A1) is the hypothesis of Lemma N at the level ℓ = ℓ(z). R_z is a π_ℓ-cube enlarged by a ≤ 2L − 2 cubes (Rule W). So its side is at most 4LMξ_ℓ, within the real-gauge clause (C_box ≥ 4). Its local scales are at least ξ_ℓ: at (W2), R_z ⊂ Ω_{p−1} meets the layers p−1, p, p+1. So the curvature and real-gauge bounds in level-ℓ units follow from those in ambient units, because ξ_ℓ ≤ l. Lemma N gives the node-reduced datum with ‖B_{t,ν}‖ ≤ C_BMα_{0,ℓ}τ, τ = ξ_j/ξ_ℓ = L^{−m}, and |v||v^{−1}| ≤ e^{CMα_1}.
- Lemma E with the R_z-tower clause of (A1) gives ‖f(B_{t,ν})‖ ≤ (1+β)aτ², with a ≤ (5/8)α_{0,ℓ}. There is no B' term here, so `wf-room.md` (7.1) is not needed and |φ|_X ≤ (1+β)aτ².
- Apply Theorem I with B = B_{t,ν} (ς = 1, B' = 0), β = 1/8 and the ceiling e^{C_g sup|B|} ≤ 1 + β of `o1-decoupled.md` 4.5. This gives e^{C_g sup|B|}|φ|_X ≤ (81/64)(5/8)α_{0,ℓ}τ².
  - For m ≥ 1, the slow-radius bound α_{0,ℓ}τ² ≤ 2(1+m)^{1/2}L^{−2m}α_{0,j} (4.5) and L² ≥ 4 give at most (81/64)(5/8)·2√2L^{−2}α_{0,j} < α_{0,j}/2.
  - For m = 0 (W3, and W2 with j = p − 1), τ = 1 and α_{0,ℓ} = α_{0,j}, so the bound is (405/512)α_{0,j} < (4/5)α_{0,j}.
  - Also C_𝓗 sup|B| ≤ C_𝓗C_BMα_{0,ℓ}τ < α_{1,j}/2, under the radius relation Mα_0 ≪ α_1 (SA 9911; `o1-decoupled.md` defect 4).
- Theorem I then gives the simple clauses (R4) of P_in, and every (R6) clause at every Z ⊂ X, p ≤ j, n ≤ p and both rules, each below the same fraction of its radius. The conversion factors L^{j−p} and L^{2j−p−n} only help.
- The bound holds at every point of the disc, so the analytic curve stays in the core, and Cauchy's inequality in ν has its fixed fraction of room (SA 15862–15864). At the young age m = 0 the margin comes from the half-radius input, not from τ. This is the same room SA 15829–15831 reserves for those ages, and no half-datum-ball step is used. Lemma N's datum bound C_BMα_0τ ≤ C_BMα_0 lies in the chart once CMα_0 < r_B/2. □

**What (10.2) still leaves, honestly.**

- The outline's own window scheme with outer and removed terms is not admitted here. Its removed curves would need the joint-core path that SA 12371–12376 itself flags, and the box-first route does not form them.
- (A1) assumes the step's input pair lies in the half-radius core, the hypothesis (R5)–(R6) puts on the class. It is not a new obligation of this note.
- Theorem A reads Lemma E's tower-clause input at the local layer. In the layered position Corollary R supplies it, with its shrinking gaps β_s2^{−n}.
- These are implications from the named inputs. Of those inputs, (LD) was checked here (Section 1). Theorem B, Theorem L, Corollary R, Lemmas N and E, and Theorem I carry their own check status, as recorded in their files.

## 5. Standing, what changes elsewhere, what stays open

| Statement | Result | Where | Reads |
|---|---|---|---|
| (LD) of `ld-decoupled.md` (Codex) | **checked line by line by Claude, first failing step none** | Section 1 | [PW], [NL], AV, BC |
| Lemma C, complex collar datum | proved by Claude, not yet checked by the other model | 2.2 | [AV], [PA], [CR], [FM] |
| Corollary CC, common collar chart = `b4-step.md` (2) | proved by Claude, not yet checked | 2.3 | Lemma C, SA Theorem 1 converse |
| Lemma RC, restriction at complex data | proved by Claude, not yet checked | 2.4 | [9.3], [AX], P81, identity theorem |
| Theorem 6c^C, SA 6(c) at complex data: field, gradient, D^*D, current, gauge; WF form = compatible boundary comparison | proved by Claude, not yet checked; implication | 2.5 | the above, T4/P82° for B, B' (or the box tower), (G1)–(G3) |
| Proposition N (a), (b): (H-node) for axial representatives with common nodes, and for Landau representatives over one reference | proved by Claude, not yet checked | 3 | Theorem 6c^C, T4, Lemma D(i) |
| Proposition N (c): Landau representatives over two references | **open**, reduced to (SC); off the box-first path | 3 | (SC) |
| Theorem A, (10.2) on the box-first route: input room (A1), inner admission (A2) | proved by Claude, not yet checked; implication | 4 | [PW], (LD), (O1), Theorem L, Corollary R, Lemmas N, E, Theorem I, radius convention α_k ≤ C_αα_{0,k} |

**What changes elsewhere (for the lead to forward; no other file edited).**

1. `b4-step.md` Section 3 and its Result. Its first unproved input, the common collar chart (2), is Corollary CC. Its consequence (3) is Theorem 6c^C. The core admission it asks for is Theorem A (A2). The stop in (4) is bypassed: no complex transport is telescoped. B4 can resume at the B1 majorant and the finer derivatives (row 172, "resume after row 173").
2. `t0-skeleton.md`, node WF-c. (1) is proved as an implication (Theorem 6c^C). (2) is proved for the representatives the adopted route uses (Proposition N (a), (b)), and the remaining case (c) is off-path. (3) is proved on the box-first route (Theorem A). Rank 4's last node is therefore closed as an implication, pending one check by Codex of Sections 2–4.
3. `ref-chart.md` 9e, Lemma 6c^C. Theorem 6c^C is that lemma in setting (1b). It carries out the gate's visible repair in order: the collar gauge is normalised first (G[𝐔], Lemma C), then b_U(β) is defined, then the identity theorem is applied on the common domain (Lemma RC). `pre-213.md` Theorem P no longer needs it, so this changes no consumer of (Pre).
4. `o1-decoupled.md` Section 5, items 2 and 3. Item 2 is Theorem 6c^C with Remark (3). Its worry that a two-constants argument misses ξ²|∇X| does not arise, since the proof is direct rather than by real-slice transfer. Item 3 is Proposition N (a), (b), with (c) recorded as off-path.
5. `a3-close.md` Section 2, "Open" item 1 (simple conditions along the actual curves). On the box-first route this is Theorem A. The outline's outer and removed curves are not formed there.

**Open, hardest first.**

1. One check of Sections 2–4 by Codex (FINISH, How we work 5).
2. (SC), only if a consumer of Proposition N (c) reappears.
3. The radius convention α_k ≤ C_αα_{0,k} (Theorem A) is a reading of SA (WF1) and 5(c). If the outline intends α_1 ~ √α_0, c_ν would shrink with the radii, and the room argument of SA (WF6) would change. This is a question for the lead about the adopted radius rule, not a new obligation.

**Method.** All steps are written by hand. No numeric job was run, and none was needed. Sources read: SA 5655–5720, 9755–9800, 10185–10200, 12140–12175, 12290–12380, 15700–15965, 16826–16860 (outline at `31a47c543775`, fetched once by URL into a private scratch folder, SHA-256 `d7f77d4d…`, the same file as earlier rows). Library: `ld-decoupled.md`, `b4-step.md` (in full); `o1-decoupled.md` 0–5; `a3-derivative.md` 1–3, 6–10; `wf-room-2.md` 0–1, 4–7; `cond-c.md` 2, 6.4; `wf7-bf.md` 2–3; `wf7-extension.md` 3–4; `removed-fix.md` 3, 7; `pw-bridge.md` 6; `nl-r9.md` 6; `dec-field.md` 5; `a1-balaban.md` 9, 10; `a3-close.md` 2; `pre-213.md` 2–3; `ref-chart.md` 9e; `geo-5.md` 3.6. Gates: `removed-fix-gate.md`, and the 6(c) and (H-node) lines of the o1-decoupled, pw-bridge and dec-field gates.

## Result

(LD) of `ld-decoupled.md` was checked line by line by Claude, first failing step none.

Items (1) and (3) of row 173 are proved by Claude as implications, not yet checked by the other model:

- Lemma C (the complex collar datum stays within C(κ + ‖w‖_*) of the lift, uniformly in depth) gives `b4-step.md`'s common collar chart (2).
- With Lemma RC, it gives SA 6(c) at complex data with every member (Theorem 6c^C). This covers decoupling parameters and independent currents, which enter only through 𝐇_k.
- Theorem A gives pointed-core admission (10.2) on the box-first route.

Item (2), (H-node), is proved for axial representatives with common nodes and for Landau representatives over one reference, which are the cases the adopted route reads. The case of Landau representatives over two different references stays open, reduced to the scalar-sector comparison (SC), and is off the critical path.
