lead: anthropic/claude-opus-5-5/max mac-mini-worker
lease_until: 2026-11-07T12:50Z

# FC-r2: the complex frame-change BLOCK of gates/fc-gate.md §2

Row 404 (`fc-r2`). Pinned at commit 2f8fd8e61. Written section by section; the Result is §6.
Proved by Claude (Mini worker 1), not yet checked by the other model.

Moves: the complex frame-change BLOCK of `gates/fc-gate.md` §2 on `library/fc.md` (Lemma G seams and datum conversion, (2.3) membership, the reduction to CC). FC is the open lemma of `library/stage-claude.md:275`, needed only under the one-frame reading (R1) of the stage spaces (owner `stage-claude`, inside H-STAGE).

Provenance: Claude Opus 5.5 (claude-opus-5-5), max effort, Mac mini worker 1, checkout at 2f8fd8e61 (branch `claude/ym4d-hard-route`). Research text, not an audit; grants no status. Written arguments only; no numeric run (none was needed). Sources: CA-I, CA-II and SA (`theorem_0_complete_account_raw_{I,II}.tex`, `YM4_sketch_500.tex`) at `31a47c543775`, fetched by URL into a scratch folder, SHA-256 equal to `library/arr.md:21-23`. Balaban CMP 99a p. 82 ((1.30)-(1.32)), CMP 102b pp. 279-281 (Theorem 1, (12)-(21)), CMP 109 pp. 252-253 ((0.3)-(0.12)), CMP 119 p. 256 ((2.10)-(2.12)) read from `~/ym4d-papers/` (page images where the OCR is garbled).

Credit: Tadeusz Balaban for the averages (CMP 109 (0.3)-(0.12)), the determining sets (CMP 119 (2.10)-(2.12)), the background theorem (CMP 102b Theorem 1, Proposition 2) and the datum convention (CMP 99a (1.31), CMP 102b (20)). Ethan Sussman and Levent Alpoge, with Claude and Codex as authors of their text, for the complete account at `31a47c543775`: the response chart (CA-I 4.5: (K1), (K2), (K6), (K8)), the chart class and its inclusion statement (CA-I 12936-13060), nested criticality (CA-I 128485), the data-axial frame and its twist bounds (CA-I 17322-17600), the quotation of the CMP 122a stage spaces (CA-I 148080-148240) and their weight exponents (CA-I 49596-49645). Claude for `library/fc.md` and `library/stage-claude.md`; Codex for `gates/fc-gate.md` and `library/prior/fc.md`.

## 0. Duplicate check (rule 0a) and consumers

Searched `library/open-core.md`, `library/l17c.md`, `library/open-registry.md` and the FINISH rows for: frame change, common gauge, double block, seam, Lemma CC, C_rel, b_D, chart datum, FC, fc-gate, one-frame, (R1).

* No other row attacks this item. FINISH rows 388 (`stage-gate`), 392 (`fc`) and 404 (this row) are its lineage. The registry has no row for the frame change; FC-test, FC-mean-match and FC6 (owner FCON) are different statements that share the letters.
* `C_rel` in `library/open-core.md:246` is the velocity constant of the L16 path statement (LOC). It is a different object: a bound along a path of data in A_in, not a gauge comparison of two fixed fields. No overlap.

Consumers. FC has one consumer, the source inclusion (SRC) of `stage-claude.md` §5.1, and only under (R1). Under the birth-frame reading (R♭) Lemma F gives (SRC) with no frame change. Which reading is CMP 122a's is not settled (`gates/fc-gate.md` §2.1-2.2). So this note is worth doing only for the (R1) branch. It says, at the end, what (R1) costs.

## 1. What changed: three structural findings

These three facts reorganize the three items of the row. Each is proved in the section named.

1. **Lemma G's construction is wrong on seams, by a factor L (§2.1).** The comb gauge of `fc.md` §2.5, pinned at the block centres, gives relative seam data of size about L²κ/2 on an explicit pair of SU(2) fields with plaquettes at most κ and equal coarse data. The claimed bound is 3Lκ. With L²κ the scale gain L⁻¹ of the advanced clause is lost entirely, so (FC*) could never be paid from the stage gap. The order Lκ is nevertheless the right one: every gauge leaves at least about Lκ/6 on the same pair (§2.6), and Lemma G′ (§2.4) attains C_rel·Lκ with C_rel a number that depends on d only, not on L.
2. **The chart base may be any gauge representative of Q^u (§2.2, Lemma B).** The chart identity (K6) needs a real base U_k(V₀) with regular real data V₀. Any real gauge transform of the base's data is again such a datum. So the gauge freedom may be spent on the base, not on 𝐔. Then no pin is needed at the D′-endpoints next to Γ′_j (the "rim"). Only the coarse centres are pinned, and the hat-function patching pins them exactly. The rim and its corners disappear from Lemma G.
3. **The chart datum on the layer interface carries Balaban's block correction (§2.5).** On the level-(j+1) bonds from the collar into Ω_{j+1}, CMP 99a (1.31) adds to the raw ratio an average over the block of the relative contour transports. For any gauge whose relative links are O(Lκ), this correction is O(L²κ). A bump correction inside each interface block removes it at a cost O(Lκ) (Lemma G″). Without it the datum bound fails by a factor L at the interface.

## 2. Item (1): the collar datum on all seams

Kind: correction of our own text (`fc.md` §2.5), then a new proof. The account does not state a frame change at complex data; its nested criticality is real (CA-I 128485).

### 2.0 Setting, norms and the elementary estimates

Work in level-j units on the level-j lattice Λ ≅ ℤ^d (d = 4). L is odd, L ≥ 13, h := (L−1)/2. The level-(j+1) sites ("centres") form C = y_∗ + Lℤ^d; the block of y ∈ C is B(y) = {x : ‖x−y‖_∞ ≤ h}; the blocks partition Λ (CA-I 1.5:def-block-average, (1.5:eq-block-average-2)). A field W assigns to each oriented bond b = (b₋,b₊) a matrix W(b) ∈ GL(N,ℂ), with W(−b) = W(b)⁻¹. For a path γ = (x₀,…,x_n), W(γ) := W(x₀,x₁)⋯W(x_{n−1},x_n). Gauge action, as in CA-I 4.5 conventions item 2: W^u(b) = u(b₋)W(b)u(b₊)⁻¹, so W^u(γ) = u(x₀)W(γ)u(x_n)⁻¹ and (W^a)^c = W^{ca}.

‖·‖ is the operator norm on N×N matrices, and δ(X) := ‖X − 1‖. The account's norm |Y| = (tr Y*Y)^{1/2}, tr 1 = 1, satisfies |Y| ≤ ‖Y‖ ≤ √N |Y|; every bound below converts with the factor c_N := √N.

Hypotheses on a set N of sites, for W ∈ {V, Ṽ}:
* (T_ε) every link is W(b) = e^{iA(b)}W_r(b) with W_r(b) ∈ G and ‖A(b)‖ ≤ ε; hence ‖W(b)^{±1}‖ ≤ e^ε.
* (P_κ) δ(W(∂p)) ≤ κ for every plaquette p of N, every base corner and both orientations.

Elementary facts (each a one-line identity):
* (E1) XY − 1 = (X−1)(Y−1) + (X−1) + (Y−1), so 1 + δ(X₁⋯X_n) ≤ Π(1 + δ(X_i)) ≤ exp Σδ(X_i).
* (E2) δ(TXT⁻¹) ≤ ‖T‖‖T⁻¹‖δ(X).
* (E3) If δ(X) ≤ ½, log X := Σ_{n≥1}(−1)^{n+1}(X−1)^n/n converges, e^{log X} = X and ‖log X‖ ≤ −ln(1−δ(X)) ≤ 1.39 δ(X). Conversely δ(e^Y) ≤ e^{‖Y‖} − 1, and e^t − 1 ≤ 1.3t for 0 ≤ t ≤ ½.
* (E3′) *Exponent form.* Say X has exponent n if δ(X) ≤ e^n − 1. Products add exponents (by (E1)). If n ≤ 0.4 then ‖log X‖ ≤ −ln(2 − e^n) ≤ 1.7n: the function n ↦ −ln(2−e^n) is convex and vanishes at 0, and its value at 0.4 is 0.677 < 1.7·0.4. An element with ‖log X‖ ≤ s has exponent s.
* (BCH) `library/b-in.md:194`, ADVANCE in `gates/b-in-gate.md`: for ‖X‖ ≤ 1/40 and ‖Y‖ ≤ 1/80, ‖log(e^Xe^Y) − X − Y‖ ≤ 1.1‖X‖‖Y‖. Its proof uses only ‖ad_F‖ ≤ 2‖F‖, which holds in the operator norm.

**Lemma F (plaquette flips).** An elementary flip replaces two consecutive bonds u → u+e_μ → u+e_μ+e_ν of a path by u → u+e_ν → u+e_μ+e_ν, or the reverse. If γ′ arises from γ by m flips and every prefix met on the way has length ≤ ℓ, then δ(W(γ)W(γ′)⁻¹) ≤ e^{mθκ} − 1, θ := e^{2εℓ}.

*Proof.* If γ_{i+1} is γ_i with one flip at u, the two paths share the prefix α and the suffix, so W(γ_i)W(γ_{i+1})⁻¹ = W(α)W(∂p)^{±1}W(α)⁻¹, ∂p the plaquette loop at u. By (E2) and (T_ε) its δ is ≤ θκ. Telescope with (E1). ∎

**Combs.** For y, x ∈ Λ, the comb γ_{y,x} goes from y first along e_d to the d-th coordinate of x, then along e_{d−1}, …, last along e_1 (the order 4,3,2,1 of SA 7078). It stays in the coordinate box spanned by y and x and has length ‖x−y‖₁.

**Lemma C (comb frames).** Fix y and R ≥ 1, and let f_W(x) := W(γ_{y,x}) for ‖x−y‖_∞ ≤ R. Then f_W(y) = 1, W^{f_W}(γ_{y,x}) = 1, and:
(a) for a bond b = (x, x+e_μ) inside the box, W^{f_W}(b) = W(γ_{y,x}b)W(γ_{y,x+e_μ})⁻¹ and δ(W^{f_W}(b)) ≤ e^{(d−1)Rθκ} − 1, θ = e^{2ε(dR+1)};
(b) for any path P of length ℓ_P inside the box from u to v, δ(W^{f_W}(P)) ≤ e^{ℓ_P(d−1)Rθ′κ} − 1, θ′ = e^{2ε(dR+ℓ_P)}.

*Proof.* (a) Move the last step e_μ of γ_{y,x}b backwards past the legs of the directions ν < μ: one flip per step of those legs, Σ_{ν<μ}|x_ν−y_ν| ≤ (d−1)R flips. If x_μ ≥ y_μ the step joins the e_μ-leg, which gives γ_{y,x+e_μ}. If x_μ < y_μ it cancels the last step of that leg (W(u,u−e_μ)W(u−e_μ,u) = 1), which again gives γ_{y,x+e_μ}. Prefixes have length ≤ dR + 1. Apply Lemma F. (b) W^{f_W}(P) = W(γ_{y,u}P)W(γ_{y,v})⁻¹. Replace γ_{y,u}b₁ by γ_{y,u₁} as in (a), then γ_{y,u₁}b₂ by γ_{y,u₂}, and so on: at most ℓ_P(d−1)R flips, prefixes ≤ dR + ℓ_P. ∎

**Lemma A (Balaban's average along a coarse bond).** Let c = (w, w′), w′ = w + Le_ν, be a coarse bond, and let 𝓜 be Balaban's symmetrised average (CMP 109 (0.10)-(0.12), the account's 1.5:def-block-average (a)):
  𝓜(W)(c) = exp(L^{−d}Σ_{x∈B(w)} log W_x)·W([w,w′]),  W_x := W(w,x)W([x,x′])W(x′,w′)W([w,w′])⁻¹,
where [x,x′] is the straight path of L bonds from x to x′ = x + Le_ν and W(w,x) is the Federbush mean of the comb transports W(Γ), Γ ∈ G(w,x) (all orders of the directions). Assume (T_ε), (P_κ) on the box {‖·−w‖_∞ ≤ R_c}, R_c := L + h, and that, in the frame g of the proof, each Federbush mean lies in {‖log‖ ≤ 1/80} (Balaban's small-diameter clause, CMP 109 (0.5)-(0.10)). Put ϑ := e^{2ε(d+2)R_c} and assume 1.7·dh(d−1)R_cϑκ ≤ 1/160 and (3.44dh + L)(d−1)R_cϑκ ≤ 0.4. Then
  ‖log W_x‖ ≤ 1.7·(3.44 dh + L)(d−1)R_c ϑκ =: a_M L²κ for every x, and so ‖L^{−d}Σ_x log W_x‖ ≤ a_M L²κ.
Covariance: for any gauge u, 𝓜(W^u)(c) = u(w)𝓜(W)(c)u(w′)⁻¹ exactly.

*Proof.* Work in the frame g := f_W of Lemma C from w on the box of radius R_c. Since g(w) = 1 and W_x is closed at w, W_x = W^g_x. The straight path [w,w′] is the comb γ_{w,w′}, so W^g([w,w′]) = 1. Each comb Γ ∈ G(w,x) has length ≤ dh, so by Lemma C(b) W^g(Γ) has exponent n_Γ := dh(d−1)R_cϑκ. The Federbush mean Y = log W^g(w,x) solves Σ_Γ log(e^{X_Γ}e^{−Y}) = 0 with X_Γ := log W^g(Γ), ‖X_Γ‖ ≤ 1.7n_Γ =: r ≤ 1/160 by (E3′). By (BCH), Y = avg X_Γ + avg R_Γ with ‖R_Γ‖ ≤ 1.1 r‖Y‖, so ‖Y‖ ≤ r/(1−1.1r) ≤ 1.01r ≤ 1.72n_Γ. The mean is covariant (both sides of (0.10) transform by Ad of the left factor), so W^g(w,x) is the mean of the W^g(Γ). The same holds for W^g(x′,w′) = W^g(w′,x′)⁻¹, whose combs also lie in the box. The straight path [x,x′] has length L, so W^g([x,x′]) has exponent L(d−1)R_cϑκ. Adding exponents, W_x = W^g_x has exponent (3.44dh + L)(d−1)R_cϑκ ≤ 0.4; apply (E3′). The covariance is CMP 109 (0.12) with W(w,x) ↦ u(w)W(w,x)u(x)⁻¹: every W_x is conjugated by u(w), and W([w,w′]) ↦ u(w)W([w,w′])u(w′)⁻¹. ∎

For d = 4 and L ≥ 13 (h ≤ L/2, R_c ≤ 1.5L): a_M ≤ 1.7·(3.44·2 + 1)·3·1.5·ϑ ≤ 61ϑ.

**Corollary A′ (relative transport between adjacent centres).** If moreover 𝓜(V)(c) = 𝓜(Ṽ)(c), then Ṽ([w,w′])V([w,w′])⁻¹ = e^{−Ā_Ṽ}e^{Ā_V} with Ā_W := L^{−d}Σ_x log W_x, so
  δ(Ṽ([w,w′])V([w,w′])⁻¹) ≤ e^{2a_M L²κ} − 1.
*Proof.* W([w,w′]) = e^{−Ā_W}𝓜(W)(c) by Lemma A; take the ratio. ∎

### 2.1 Proposition G0: the comb construction of `fc.md` fails on seams

`fc.md` §2.5 puts each field in the comb gauge of each level-(j+1) block from its centre and composes the two frames: h := h_Q⁻¹h_𝐔, g = h on the block, so g = 1 at every centre. It then claims |δd(c)| ≤ ‖Ad_{h_Q}‖(2C_axLκ + C_BCH(dLκ)²), C_ax = (d−1)/2, for every c ∈ 𝒞⁺ (fc.md line 132).

**Proposition G0.** Let G = SU(2), σ₃ = diag(1,−1), d = 4, L ≥ 13 odd, h = (L−1)/2, κ ≤ 1/(100L²). Let S: ℤ → ℤ have period 2L, with S(t) = h − t for 0 ≤ t ≤ L−1 and S(t) = t − L − h for L ≤ t ≤ 2L−1. Put the centres at second coordinate ≡ h (mod L). Define the real fields
  V(x, x+e₁) := exp(iκS(x₂)σ₃),  V(b) := 1 on bonds of the other directions,  Ṽ :≡ 1.
Then (P_κ) holds for both fields, 𝓜(V)(c) = 𝓜(Ṽ)(c) = 1 on every coarse bond c, and the construction of `fc.md` §2.5 gives, on the seam bond b = (x, x+e₁) with x₁ − y₁ = h and x₂ ≡ 0 (mod L),
  |δd(b)| = κ·L·h = κL(L−1)/2,
while every internal bond gets at most κh. The claimed bound is 3Lκ + O(L²κ²). It fails by the factor (L−1)/6.

*Proof.* S is continuous on ℤ (S(L−1) = S(L) = −h, S(2L−1) = S(2L) = h), |S(t+1) − S(t)| ≤ 1, Σ_{t=0}^{L−1}S(t) = 0, Σ_{t=L}^{2L−1}S(t) = 0, and S(t+L) = −S(t). The fields are diagonal, so every transport is exp(iκσ₃·a(path)) with a the integer-valued line integral of a(x,x+e₁) := S(x₂).
(P_κ): a (1,2)-plaquette has holonomy exp(±iκ(S(x₂) − S(x₂+1))σ₃), and |e^{iκs} − 1| ≤ κ|s| ≤ κ. Every other plaquette has holonomy 1.
Coarse data. For commuting arguments near 1 the Federbush mean is the exponential of the mean exponent (the equation (0.10) is linear then). So 𝓜(V)(c) = exp(iκσ₃·avg_{x∈B(w)}[ā(w,x) + a([x,x′]) − ā(w′,x′)]), ā(w,x) the mean of a over the combs G(w,x). For c along e₁: a([x,x′]) = L·S(x₂) has block mean 0, and a is invariant under translation by Le₁, so ā(w′,x′) = ā(w,x). For c along e₂: a([x,x′]) = 0 and translation by Le₂ reverses the sign of a, so the bracket is 2ā(w,x). A comb from w to x crosses its e₁-leg at row w₂ (where S(w₂) = S(h) = 0) or at row x₂, the latter for half of the orders. So ā(w,x) = ½(x₁ − w₁)S(x₂), whose block mean is ½·0·0 = 0. For c along e₃ or e₄ the field is invariant under the translation and a([x,x′]) = 0. Hence 𝓜(V) ≡ 1.
The construction: h_Ṽ = 1 and h_V(x) = V(γ_{y,x}) = exp(iκσ₃(x₁ − y₁)S(x₂)), because the comb ends with its e₁-leg at row x₂. The exponent of V^h on a bond b is a(b) + λ(b₋) − λ(b₊) with λ(x) = (x₁−y₁)S(x₂), y the centre of the block of x. On the seam b = (x,x+e₁), x₁ − y₁ = h and x+e₁ lies in the next block at offset −h, so the exponent is S(x₂)(1 + h + h) = L·S(x₂), and |S(x₂)| = h at x₂ ≡ 0. On internal e₁-bonds the exponent is 0; on internal e₂-bonds it is (x₁−y₁)(S(x₂) − S(x₂+1)), at most h in size. ∎

So `fc.md`'s Lemma G is not only unproved on seams (gate §2.5, failure 1): its construction violates its displayed bound. With seam data of order L²κ, the response next to the collar is of order B_♯L²κ ≍ B_♯C_av(1+β₀)L₀² times the stage-n unit, so the scale gain L⁻¹ of (FC*) disappears and no choice of L can pay it.
