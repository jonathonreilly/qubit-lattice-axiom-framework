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

### 2.2 Lemma B: the gauge freedom may be spent on the base

**Lemma B (base representative).** Let V₀ be real D-data satisfying the hypothesis of (K6) (CMP 102b (7) with ε₁ ≤ ε̄₁, CA-I 15669-15680), and U₀ := U_k(V₀). Let u be a G-valued gauge map, equal to 1 on the exterior of the localized problem. Write û for its values at the sites of the D-hierarchy. Then:
(a) V₀^û satisfies the same hypothesis with the same ε₁;
(b) the minimal orbit with data V₀^û is the image under u of the minimal orbit with data V₀, so U_k(V₀^û) = U₀^{u′} for a G-valued u′ with u′ = û at the hierarchy sites;
(c) |∂U_k(V₀^û) − 1| and |J(U_k(V₀^û))| equal those of U₀ pointwise, and (U_k(V₀^û), J(U_k(V₀^û))) ∈ 𝔖 with the same constants;
(d) (K6)(a)-(d) hold at the base U_k(V₀^û).

*Proof.* The regularity conditions of Balaban's spaces are stated through plaquette variables, covariant derivatives and the existence of gauges on cubes; Balaban notes their gauge invariance (CMP 99a p. 77, after (1.10)). The averages are covariant with the gauge at the endpoints of each hierarchy bond (Lemma A, last clause, iterated), so U ↦ U^ũ maps 𝔅_k(𝔅_k, V₀) onto 𝔅_k(𝔅_k, V₀^û) for any fine extension ũ of û. The Wilson action is gauge invariant, so minimal and critical orbits correspond (CMP 102b Theorem 1, Proposition 2). The norms in (c) are unitarily invariant, and J(U^u) = R(u)J(U) (CA-I 4.5 conventions item 2). (d): (K6) is stated for every real V₀ with this hypothesis. ∎

**Consequence.** To write O(𝐔) = U(D, M^D𝐔) as a chart response, the base may be any representative U(D, (M^DQ^u)^k̂) of the orbit of Q^u, with k G-valued at real points. Then 𝐔 is not gauge-transformed, Q is untouched, and no D′-constraint can change. The only conditions on k are: k = 1 on the exterior; k = 1 at the hierarchy sites where the base's data must stay equal to the target's for the datum to vanish (the centres, see Lemma G′(i)); and the resulting datum must be small. In particular the level-j sites of the collar next to Γ′_j (endpoints of retained D′-constraints, the "rim" of row 404) need no pin: on Γ′_j the datum is the small quantity k makes it, not zero. This removes the rim and its corners from the problem. `fc.md` pinned g at those endpoints because it moved 𝐔; the gate's demand that "the piecewise lift fixes every retained D′ endpoint" is met trivially: the lift acts on the base, and the target's D′-data are never touched.

At complex points the same holds with k ∈ G^c, provided the base stays in the chart's domain; §3 treats this.

### 2.3 Lemma T: local frames and their transitions

For a centre y let E(y) := {x : ‖x−y‖_∞ ≤ L}, and for x ∈ E(y)
  k_y(x) := V(γ_{y,x})⁻¹Ṽ(γ_{y,x})   (so k_y(y) = 1 and Ṽ^{k_y}(γ_{y,x}) = V(γ_{y,x})).
Its local relative datum on a bond b = (x,x′) ⊂ E(y) is ρ_y(b) := V(b)·Ṽ^{k_y}(b)⁻¹ (target times base inverse, the order of CMP 99a (1.31)). The transition of two frames is τ_{zy}(x) := k_z(x)k_y(x)⁻¹.

Put Θ := e^{8dεL} (it dominates every conjugation factor below) and a_loc, t_max as in the lemma.

**Lemma T.** Assume (T_ε) and (P_κ) for V and Ṽ on {‖·−y‖_∞ ≤ 3L} and 𝓜(V) = 𝓜(Ṽ) on the coarse bonds with both ends in {‖·−y‖_∞ ≤ L}. Assume the twist ceiling (CE): Θ ≤ 1.1, and the curvature ceiling (CK): 10⁴Θ²L²κ ≤ 1. Then:
(a) ‖log ρ_y(b)‖ ≤ a_loc := 4.42(d−1)Θ²Lκ for every bond b ⊂ E(y);
(b) for every centre z with z − y ∈ L{−1,0,1}^d and every x with ‖x−y‖_∞ ≤ h+1, ‖x−z‖_∞ ≤ L:
  ‖log τ_{zy}(x)‖ ≤ t_max := C_τL²κ,  C_τ := 3.8Θ²[5.2d(d−1) + 2d·a_M/Θ];
(c) (near-parallel transport) for b = (x,x′) in both frames, Ad_{V(b)}τ_{zy}(x′) = ρ_z(b)·τ_{zy}(x)·ρ_y(b)⁻¹ exactly.
For d = 4, a_M ≤ 61Θ gives a_loc ≤ 13.3Θ²Lκ and C_τ ≤ 2.1·10³Θ².

*Proof.* (a) With f_W the comb frames of Lemma C from y (R = L), k_y = f_V⁻¹f_Ṽ and a direct expansion gives ρ_y(b) = Ad_{f_V(x)⁻¹}[V^{f_V}(b)·Ṽ^{f_Ṽ}(b)⁻¹]. Each factor in the bracket has exponent (d−1)LΘκ (Lemma C(a); the inverse is the same flip product read backwards). The conjugation costs ‖f_V(x)^{±1}‖ ≤ e^{εdL}, so by (E2) and (E3) the exponent of ρ_y(b) is ≤ 1.3Θ·2(d−1)LΘκ, and (E3′) gives (a).
(b) Let P := γ_{z,x}·γ̄_{y,x} (from z through x to y). Expanding the definitions,
  τ_{zy}(x) = Ad_{V(γ_{z,x})⁻¹}[Ṽ(P)·V(P)⁻¹].
Let S be the path from z to y made of the m ≤ d straight coarse segments through the centres z, z − Lv₁e_{ν₁}, …, y (v = (z−y)/L). Then
  Ṽ(P)V(P)⁻¹ = [Ṽ(P)Ṽ(S)⁻¹]·[Ṽ(S)V(S)⁻¹]·[V(S)V(P)⁻¹].
In the comb frame g of Ṽ from y, Ṽ(P)Ṽ(S)⁻¹ = Ad_{g(z)⁻¹}[Ṽ^g(P)Ṽ^g(S)⁻¹]. P and S stay in E(y), ℓ_P ≤ dL + d(h+1) ≤ 1.6dL and ℓ_S ≤ dL, so by Lemma C(b) the bracket has exponent 2.6d(d−1)L²Θκ, and the conjugation multiplies by at most 1.3Θ. The same holds for V(S)V(P)⁻¹. For the middle factor, Ṽ(S)V(S)⁻¹ = Π_i Ad_{V(S₁⋯S_{i−1})}[Ṽ(S_i)V(S_i)⁻¹] by telescoping, each segment has exponent 2a_ML²κ (Corollary A′), and each conjugation costs at most 1.3Θ. Add the exponents (total ≤ Θ²[6.76d(d−1) + 2.6d·a_M/Θ]L²κ), conjugate by V(γ_{z,x})⁻¹ (factor 1.3Θ), and apply (E3′); with Θ ≤ 1.1 the result is below C_τL²κ. (CK) keeps every exponent below 0.4.
(c) From the definition of ρ_w, V(b)k_w(x′) = ρ_w(b)k_w(x)Ṽ(b) for w = y, z. Hence V(b)k_z(x′)k_y(x′)⁻¹V(b)⁻¹ = ρ_z(b)k_z(x)Ṽ(b)·Ṽ(b)⁻¹k_y(x)⁻¹ρ_y(b)⁻¹. ∎

The point of (c): the frames disagree by O(L²κ), but their disagreement is transported along every bond up to the local data ρ = O(Lκ). This is what lets a partition of unity on the scale L spread the disagreement.

### 2.4 Lemma G′: the patched frame (all seams)

Hat functions: ψ(s) := max(0, 1−|s|) and, for a centre z, φ_z(x) := Π_ν ψ((x_ν − z_ν)/L). Then φ_z ≥ 0, Σ_z φ_z = 1 (a product of one-dimensional partitions Σ_{n∈ℤ}ψ(s−n) = 1), φ_z(y) = δ_{zy} for centres y, φ_z(x) ≠ 0 only if ‖x−z‖_∞ < L, and for every bond (x, x+e_μ), Σ_z|φ_z(x+e_μ) − φ_z(x)| ≤ 2/L (only the μ-factor changes, by at most 1/L, at two values of z_μ, and the other factors sum to 1).

**Lemma G′.** Let 𝒦 be a set of centres and 𝒳 := ∪_{y∈𝒦}B(y). Assume (T_ε), (P_κ) for V and Ṽ on the 3L-neighbourhood of 𝒦, 𝓜(V) = 𝓜(Ṽ) on every coarse bond with both ends within L of 𝒦, (CE), (CK), and (CK3): C_τ²L³κ ≤ 1/20. For x ∈ 𝒳 let y(x) be the centre of its block and put
  k(x) := exp(Λ(x))·k_{y(x)}(x),  Λ(x) := Σ_z φ_z(x) log τ_{z y(x)}(x).
Then:
(i) k(y) = 1 for every y ∈ 𝒦;
(ii) for every bond b = (x,x′) with x, x′ ∈ 𝒳: ‖log(V(b)·Ṽ^k(b)⁻¹)‖ ≤ C_rel Lκ, with C_rel := 2C_τ + 14.2(d−1)Θ² + 1;
(iii) ‖k(x)^{±1}‖ ≤ e^{2εdL + C_τL²κ};
(iv) if V = Ṽ on every bond within distance L of x, then k(x) = 1;
(v) if V, Ṽ are G-valued, so is k.
For d = 4 under (CE): C_rel ≤ 5.2·10³. The constant depends on d only.

*Proof.* (i) Λ(y) = log τ_{yy}(y) = 0 and k_y(y) = 1. Every z with φ_z(x) ≠ 0 has z − y(x) ∈ L{−1,0,1}^d (since ‖z − y(x)‖_∞ < L + h < 2L), so Lemma T(b) gives ‖Λ(x)‖ ≤ t_max.
(ii) Let y := y(x), y′ := y(x′). *Common reference.* With a_z := log τ_{zy}(x′) and c := log τ_{y′y}(x′), τ_{zy′} = τ_{zy}τ_{y′y}⁻¹, so by (BCH) Λ(x′) = Σ_zφ_z(x′)a_z − c + R̄ with ‖R̄‖ ≤ 1.1t_max², and k_{y′}(x′) = τ_{y′y}(x′)k_y(x′). Hence k(x′) = e^{Λ_y(x′)+E}k_y(x′), where Λ_y(x′) := Σ_zφ_z(x′)a_z and, by (BCH) again, ‖E‖ ≤ 3.5t_max². (All centres involved satisfy the hypotheses of Lemma T(b) at x′, because ‖x′ − y‖_∞ ≤ h+1 and ‖x′ − z‖_∞ ≤ L.)
*Factorization.* Since V(b)k_y(x′)Ṽ(b)⁻¹k_y(x)⁻¹ = ρ_y(b),
  V(b)Ṽ^k(b)⁻¹ = V(b)k(x′)Ṽ(b)⁻¹k(x)⁻¹ = e^{Ad_{V(b)}(Λ_y(x′)+E)}·ρ_y(b)·e^{−Λ(x)}.
*Transport of the weights.*
  Ad_{V(b)}Λ_y(x′) − Λ(x) = Σ_z(φ_z(x′) − φ_z(x))·log τ_{zy}(x) + Σ_zφ_z(x′)[Ad_{V(b)}log τ_{zy}(x′) − log τ_{zy}(x)].
The first sum is at most (2/L)t_max. By Lemma T(c), Ad_{V(b)}log τ_{zy}(x′) = log(ρ_z(b)τ_{zy}(x)ρ_y(b)⁻¹), and two uses of (BCH) bound each bracket by 2a_loc(1 + 2.3t_max) ≤ 2.1a_loc.
*Assembly.* Write the product as e^{Ad_{e^{X}}Y}·e^{X}e^{Z} with X := Ad_{V(b)}(Λ_y(x′)+E), Y := log ρ_y(b), Z := −Λ(x). Then ‖X + Z‖ ≤ 2t_max/L + 2.1a_loc + 3.9t_max², ‖log(e^Xe^Z) − X − Z‖ ≤ 1.3t_max², and ‖Ad_{e^X}Y‖ ≤ 1.01a_loc. A last (BCH) gives ‖log(V(b)Ṽ^k(b)⁻¹)‖ ≤ 2t_max/L + 3.2a_loc + 5.3t_max². By (CK3), 5.3t_max² = 5.3C_τ²L⁴κ² ≤ 0.27Lκ. Insert t_max = C_τL²κ and a_loc = 4.42(d−1)Θ²Lκ.
(iii) ‖k_y^{±1}‖ ≤ e^{2εdL} and ‖e^{±Λ}‖ ≤ e^{t_max}. (iv) Then k_z(x) = 1 for every z with φ_z(x) ≠ 0, because the comb γ_{z,x} stays within L of x; so τ = 1, Λ = 0 and k(x) = k_{y(x)}(x) = 1. (v) Then each log τ lies in the real Lie algebra and Λ is a real combination of them. ∎

Lemma G′ uses no frozen set and no rim: by Lemma B nothing else is pinned. The comb frames of `fc.md` are the frames k_y; what was missing is the patching, which spends the O(L²κ) disagreement of neighbouring frames over L steps.

### 2.5 Lemma G″: the block correction at the layer interface

The chart datum is Balaban's B of CMP 99a (1.31), quoted in CMP 102b (20) and used by the account through (K2) (CA-I 14672-14705: Q_j(U;ηℋ^J(B)) = B, "the counterpart at free current J of [CMP 102b (20)]"). With V′ := V·Ū₀⁻¹ (target data times base data inverse):
* on a bond b ⊂ Λ_i: e^{iB_b} = V′_b, the left ratio;
* on an interlayer bond b with b₋ in the finer layer and b₊ in the next layer: e^{iB_b} = exp[−L^{−d}Σ_{x∈B(b₋)} log(relative transport of V′ along the contour Γ_{b₋,x})]·V′_b.
In the frame D the collar is a level-j layer and Ω_{j+1} the next one. On an interlayer bond b = (y, y′), y a collar centre and y′ ∈ Ω_{j+1}, the raw ratio V′_b is 1: both data are D′-data and k = 1 at centres. The correction is not 0.

**Lemma G″ (d = 4).** Let y be a collar centre with an interlayer bond (y, y′). Let C_W(y,x), x ∈ B(y), be the contour variables of (1.31): monotone paths from y to x inside B(y), or Federbush means of families of them, so that C_{W^u}(y,x) = u(y)C_W(y,x)u(x)⁻¹. Put
  m_y(k) := L^{−d}Σ_{x∈B(y)} log(C_V(y,x)·C_{Ṽ^k}(y,x)⁻¹).
(a) For k of Lemma G′, ‖m_y(k)‖ ≤ C_mL²κ, C_m := 1.7Θ(C_τ + 0.9d(d−1)) ≤ 4.8·10³.
(b) Let r(x) := ‖x−y‖_∞, ρ(x) := c_L·min(r, h − r) with c_L := 1/avg_{B(y)}min(r, h−r). Then c_L ≤ 50/L and max ρ ≤ 11.4. There is s_y with ‖s_y‖ ≤ 2‖m_y(k)‖, real at real data, such that
  k^♯(x) := exp(ρ(x)·Ad_{C_V(y,x)⁻¹}s_y)·k(x) on B(y),  k^♯ := k elsewhere,
satisfies m_y(k^♯) = 0.
(c) k^♯ = k at y and on the boundary rows r = h of B(y). So k^♯ = 1 at all centres, and the data on bonds leaving B(y) do not change.
(d) On bonds inside B(y), ‖log(V(b)Ṽ^{k^♯}(b)⁻¹)‖ ≤ (C_rel + 110C_m + 1)Lκ =: C^♯_rel Lκ, and C^♯_rel ≤ 5.4·10⁵.

*Proof.* (a) With γ = γ_{y,x}, C_V(y,x)C_{Ṽ^k}(y,x)⁻¹ = C_V(y,x)k(x)C_Ṽ(y,x)⁻¹ = [C_V(y,x)V(γ)⁻¹]·e^{Ad_{V(γ)}Λ(x)}·[Ṽ(γ)C_Ṽ(y,x)⁻¹], because V(γ)k_y(x)Ṽ(γ)⁻¹ = 1. The outer factors are loops at y of length ≤ 2dh inside B(y); by Lemma C(b) from y with R = h, and Lemma A's bound for Federbush means, each has exponent ≤ 0.9d(d−1)ΘL²κ (as dh(d−1)h ≤ d(d−1)L²/4, times 1.72). The middle has exponent ≤ Θt_max. Apply (E3′).
(b) *The bump.* For d = 4 the number of x with r(x) = r ≥ 1 is (2r+1)⁴ − (2r−1)⁴ = 64r³ + 16r ≥ 64r³. Keeping only h/2 ≤ r ≤ h−1, where r³ ≥ h³/8 and min(r, h−r) = h − r, gives Σ_x min(r, h−r) ≥ 8h³·Σ_{u=1}^{⌊h/2⌋}u ≥ h³(h²−1). Divided by L⁴ = (2h+1)⁴ ≤ 22.1h⁴ (h ≥ 6), the average is ≥ 0.044h; and h ≥ 6L/13. So c_L ≤ 50/L and max ρ = c_L⌊h/2⌋ ≤ 11.4.
*The equation.* By covariance and k^♯(y) = 1, C_{Ṽ^{k^♯}}(y,x) = C_Ṽ(y,x)k^♯(x)⁻¹, so the relative contour transport of k^♯ is C_V(y,x)k^♯(x)C_Ṽ(y,x)⁻¹ = e^{ρ(x)s}·e^{q(x)}, with q(x) := log(C_V(y,x)k(x)C_Ṽ(y,x)⁻¹), ‖q‖ ≤ q̄ := C_mL²κ. By (BCH), m_y(k^♯) = s + m_y(k) + avg_xR(x;s) with ‖R(x;s)‖ ≤ 1.1·11.4‖s‖q̄, because avg ρ = 1. The map s ↦ −m_y(k) − avg_xR(x;s) is continuous and maps the ball ‖s‖ ≤ 2‖m_y(k)‖ into itself once 25q̄ ≤ 1. Brouwer's fixed-point theorem (finite dimension) gives s_y. At real data the map preserves the real Lie algebra, so the fixed point may be taken there.
(c) ρ = 0 at r = 0 and at r = h.
(d) For b = (x,x′) inside B(y), the new datum is e^{Ad_{V(b)}σ(x′)}·[V(b)Ṽ^k(b)⁻¹]·e^{−σ(x)} with σ(x) := ρ(x)Ad_{C_V(y,x)⁻¹}s_y, and Ad_{V(b)}σ(x′) − σ(x) = Ad_{C_V(y,x)⁻¹}[ρ(x′)Ad_{H_b}s_y − ρ(x)s_y], H_b := C_V(y,x)V(b)C_V(y,x′)⁻¹ a short loop at y. So its norm is ≤ Θ‖s_y‖(c_L + 2.1·11.4·δ(H_b)) ≤ 110C_mLκ + (small). The cross terms are of second order and are absorbed by the +1 under (CK3). ∎

Without Lemma G″ the interlayer datum is of order C_mL²κ. Its response at the persistent level-(j+1) layer would again carry no factor L⁻¹.

The constants of Lemmas G′ and G″ are crude. They are recorded only to show that they depend on d alone; nothing below uses their size beyond that.

### 2.6 The order Lκ is necessary

**Proposition G1.** On the pair (V, Ṽ) of Proposition G0, for every G-valued gauge k (on either field, at any sites), some bond b of the loop ℓ below has ‖log(V(b)Ṽ^k(b)⁻¹)‖ ≥ (L−1)κ/8. For G^c-valued k with ‖Ad_k^{±1}‖ ≤ 𝔎 the same holds with (L−1)κ/(8𝔎²).

*Proof.* Let w be a centre, and ℓ the loop w → w+Le₁ (straight), then h steps along −e₂, then L steps along −e₁, then h steps along +e₂ back to w. It encloses the hL plaquettes of the rows 0, …, h−1 of the (1,2)-plane, each with holonomy exp(iκσ₃) (S decreases by 1 there). So V(ℓ) = exp(iκhLσ₃) and Ṽ(ℓ) = 1. Write β(b) := V(b)Ṽ^k(b)⁻¹ along ℓ = (b₁, …, b_n), n = 2L + 2h = 3L − 1. Telescoping gives V(ℓ) = Π_i Ad_{T_i}β(b_i)·Ṽ^k(ℓ), with T_i the Ṽ^k-transport along b₁⋯b_{i−1}; here Ṽ ≡ 1, so Ṽ^k(ℓ) = 1 and T_i = k(w)k(x_i)⁻¹ ∈ G. If every ‖log β(b_i)‖ ≤ s, the product has exponent ns, and −ln(2 − e^t) ≤ t(1 + 2t) for t ≤ 0.1; so either ns > 0.1, or κhL ≤ ns(1.2). Both give s ≥ κhL/(1.2(3L−1)) ≥ (L−1)κ/8, because κ ≤ 1/(100L²). For complex k the conjugations cost ‖Ad_{T_i}‖ ≤ 𝔎². ∎

So the gate's form |b_D| ≤ C_rel·Lκ is the right order: no gauge makes the datum o(Lκ) on this pair. Hence any sup-norm route to FC carries the factor L, and the gain must come from (FC*)'s L⁻¹, as in `fc.md`.

### 2.7 Item (1) answered: the datum b_D, the lift, the D′-data and the exterior

Fix an ordinary stage n+1, a real point 𝐔 = U first (§3 treats complex points), the old tower D (p ≥ j+1) on X″ and the new tower D′. Put V := M^jU and Ṽ := M^jQ(U) on the level-j sites, and let 𝒦 be the centres of the collar blocks, of the Γ′_j-blocks within coarse distance 3 of the collar, and of the Ω_{j+1}-blocks adjacent to the collar.

Premises (geometric, as in the account's conventions; not proved here):
* (GEO) Both nests are admissible (CA-I 4.5 conventions item 7) with gap R𝔐 ≥ 4L in level-j units; the collar is a union of level-(j+1) blocks; Γ′_j is a union of level-(j+1) blocks (M is a power of L). Consequence: Γ_{j−1} and finer layers are farther than 4L from 𝒳.
* (EXT) The 4L-neighbourhood of 𝒳 meets neither X″^c nor the boundary gauge layer of the localized problems, except where D and D′ retain the same constraints (the staircase of CA-I 128565-128575). Without (EXT) the account's own nested criticality holds only off the boundary layer (CA-I (III), 128577-128580).
* (CURV) (P_κ) and (T_ε) hold for V and Ṽ on the 4L-neighbourhood of 𝒳, with κ := C_av times the stage-(n+1) fine-curvature bound at level-j scale (entries 1 and 2 of CA-I 148213-148216) and ε the twist of the level-j averages. C_av is the averaging constant (real data: CMP 98 Propositions 1-2; complex data: CA-I 4.5:rem-block-curvature-complex (a), printed without proof).
* (COORD) The datum of the D-hierarchy is CMP 99a (1.31): the left ratio on intralayer bonds, the block correction on interlayer bonds with b₋ in the finer layer (§2.5).

**Theorem G (item (1)).** Under (GEO), (EXT), (CURV), (COORD), (CE), (CK), (CK3), let k^♯ be given by Lemma G′ on 𝒦 followed by Lemma G″ on every interface block, and extended by 1 off 𝒳. Let the base be U^♯₀ := U_k((M^DQ(U))^{k̂^♯}), in the orbit of Q(U) by Lemma B. Then:
(a) the chart datum b_D of the target data M^DU relative to U^♯₀ satisfies |b_D(c)| ≤ c_N·C^♯_rel·L·κ_loc(c) on every bond c of the D-hierarchy, κ_loc(c) the curvature bound on the 4L-neighbourhood of c, and b_D(c) = 0 on every bond farther than 4L from the collar;
(b) no D′-constraint of U is changed (U is not moved), and U^♯₀ = U on the exterior;
(c) the composite entries of U^♯₀ equal those of Q(U) pointwise.

*Proof.* (a) On level-j bonds with both ends in 𝒳: Lemma G′(ii) and Lemma G″(d), converted with c_N. On level-(j+1) bonds and interlayer bonds: the raw ratio is 1 (Lemma N of `fc.md`, ADVANCE, and k^♯ = 1 at centres) and the correction is 0 by Lemma G″. Far from the collar: on Γ′_j, V = Ṽ (Lemma N), so k^♯ = 1 by Lemma G′(iv) and the datum vanishes; in Ω_{j+1} the D-data are of level ≥ j+1 and see k^♯ only at centres; finer layers are beyond 4L by (GEO). (b) The gauge acts on the base only; (EXT) and Lemma G′(iv) give k^♯ = 1 near the exterior. (c) Lemma B(c). ∎

What Theorem G does not give. It does not identify (1.31)'s contour family on the interface with a named one (Lemma G″ works for any monotone family or its Federbush means). It does not treat the boundary layer (premise (EXT)). It does not convert to the chart's datum norm beyond the factor c_N; the account leaves that norm on 𝔤^c unnamed (CA-I 12988-12991).
