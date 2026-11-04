lead: anthropic/claude-opus-5-5/max mac-mini-worker
lease_until: 2026-11-04T23:26Z

# gamma-bx: the invariant gauge-fixing extension, (Γ), and the repair of bx-fix

Queue row 221. Pinned at commit 768226ec8. Restarted 2026-11-04T11:26Z (fresh session); the earlier stub at 6d367c519 had no content and is replaced.

Status: complete for this item (Section 4). Proved by Claude, not yet checked by the other model, unless a line says otherwise.

**Moves:** (Γ) for the floor's (P3) and Proposition W, and (BX), hence B4's (19) (`b2-extract.md` §7; `p2-floor.md` §3).

**Provenance.** Anthropic Claude Opus 5.5 (`claude-opus-5-5`), effort max, Mac mini worker, fresh session; checkout `768226ec8`. Sussman–Alpoge outline `YM4_sketch_500.tex` at `31a47c543775`, fetched by URL into a private scratch folder (sha1 `107abaef…2348885`, 32992 lines), cited as SA nnnn. Research text, not an audit; it grants no status. No subagent. Memory free was 55 percent at the start, but no numeric job was needed: every step below is a written argument.

**Credit.** Ethan Sussman and Levent Alpoge, with Claude and Codex as the authors of their text, for the soft block axial factor and its Faddeev–Popov identity (SA 7178–7182, 7666–7673), the covariance and invariant-extension paragraph (SA 7748–7754, 7913), the axial Gaussian gauge form (SA 7875–7878), the precision 𝖠 (SA 10200–10208), the pointed window theorem (SA 13426–13866) and the box package (SA 15821–15826). T. Balaban for the soft gauge fixing (CMP 109 (0.14)–(0.19)) and the invariance assumption (CMP 109 (1.19)). OpenAI Codex for `gates/ur-gauge-check.md` (defects D1, D2) and `gates/bx-fix-check.md` (defects 1–4), whose findings this note repairs, and for `ur-ya.md`, `bx.md`, `pw-bridge.md`, `dec-field.md`. Claude for `ur-gauge.md`, `bx-fix.md`, `a2-full.md`, `a2-layers.md`, `h-walk.md`, `p2-floor.md`, `a3-derivative.md` §6.1.

## 0. What the outline does with the object (FINISH item 9)

- **The factor.** SA 7178–7182 defines the *absolute* factor 𝔊_k(V;P'') and GF_k(V) = Σ_{y,x}[1 − ½ Re tr V(y,x)]. SA 10200–10204 reads its quadratic part G^{(2)}_V at V = 𝓜^k𝐔 for a general pair. SA 7875–7878 fixes the normalisation only where every background contour is 1: x_k GF_k(e^{ig_kB}V^{bg}_k; P'') = ½Σ[|B(y,x)|² + O(g_k|B|³)], with x_k g_k² = 1.
- **Covariance.** SA 7748 asserts that "every ingredient of a step is gauge covariant", so E^{(k+1)}(X,·) is invariant, with the one-line reason at SA 7913. For the absolute G^{(2)}_V this is false off the slice (`h-walk.md` test 2.1; check D2).
- **Invariant extension.** SA 7754: "A function F constructed on a slice … has a unique invariant extension, F^♮(𝔷) = F(𝖼[𝔷]·𝔷) … The extension retains locality, the bounds, and holomorphy in (A′,𝐉) at fixed real U." No map 𝖼 is constructed and no bound is proved.
- **Classification.** Sketched. This note constructs the extension (Rule (REL′)), proves the bounds the step reads, and identifies the physical composite. It is a proof of a step the outline sketches, not a correction of their text: SA 7754 permits the extension.

## 1. Rule (REL′): the correctly normalised covariant factor

**Setting.** Step k → k+1 on the node-free blocks P'' of SA 7875. For a pair 𝐏 = (𝐔, 𝐉) of the step's class let V := 𝓜^k𝐔 be its level-k averaged background. Write the integration field as W = e^{ig_kB}V, with x_k g_k² = 1 (SA 7878). W(y,x) is the averaged contour variable (Federbush's mean over 𝒢(y,x), SA 7065), y a centre in P'', x ∈ B(y)∖y. Gauge maps act by U^h(b) = h(b_−)U(b)h(b_+)^{−1}, so (e^{ig_kB}V)^h = e^{ig_kB^h}V^h with B^h(b) := Ad(h(b_−))B(b).

**Rule (REL′).** The factor of the regular step is ur-gauge's relative factor,

  𝔊^{rel}_k(W;V) := Π_{y∈P''} Π_{x∈B(y)∖y} z_𝔊^{−1} 1{|W(y,x)V(y,x)^{−1} − 1| < ε_k} e^{−x_k(1 − ½ Re tr(W(y,x)V(y,x)^{−1}))},

with SA's blocks, pairs, threshold and normaliser. Its exponent in the Gaussian chart is the holomorphic function

  GF^{rel}_k(B;V) := x_k Σ_{y,x} [1 − ½ tr((e^{ig_kB}V)(y,x) V(y,x)^{−1})]    (1.1)

(Re tr = tr on SU(2)). Its **precision part** is the B-Hessian G^{(2),rel}_V := D²_B GF^{rel}_k(0;V). Equivalently, it is the D-Hessian at D = 0 of D ↦ Σ_{y,x}[1 − ½ tr((e^{iD}V)(y,x)V(y,x)^{−1})], **with no factor x_k**, since D = g_kB and x_kg_k² = 1. This is the repair of D1: (REL) put x_k in front of the unscaled functional. The higher part is GF^{rel}_{≥3}(B;V) := GF^{rel}_k(B;V) − ½G^{(2),rel}_V[B,B]. The precision of the step is

  𝖠^{rel}(𝐏) := 𝖢_V^T (G^{(2),rel}_V + Δ_k) 𝖢_V,    (1.2)

with SA's Δ_k and pivot elimination 𝖢_V (SA 10200–10204). The large-field moves keep SA's absolute factor (SA 17531, 17558), as (REL) did.

**Lemma 1 (identities and bounds of the factor).**
- (a) *Faddeev–Popov.* ∫Π_x du(x) 𝔊^{rel}_k(W^u;V) = 1 for u = 1 on T^{(k+1)} and V fixed. So the step's transformation is unchanged for every V that depends on V_{k+1} only.
- (b) *Slice agreement.* If V(y,x) = 1 at every pair of the factor, then 𝔊^{rel}_k(·;V) = 𝔊_k(·;P'') and GF^{rel}_k(B;V) = x_kGF_k(e^{ig_kB}V;P'') identically in B. So all Taylor coefficients agree, and G^{(2),rel}_V is SA 7878's quadratic coefficient.
- (c) *Covariance.* For every gauge map h, real or complex, with both sides defined: 𝔊^{rel}_k(W^h;V^h) = 𝔊^{rel}_k(W;V) and GF^{rel}_k(B^h;V^h) = GF^{rel}_k(B;V). Hence G^{(2),rel}_{V^h}[B^h,B^h] = G^{(2),rel}_V[B,B], and the same holds for the higher part.
- (d) *No linear term.* D_BGF^{rel}_k(0;V) = 0 at every V where the means are defined.
- (e) *Normalisation and bounds.* Let τ_VB(y,x) be the linear part in B of (ig_k)^{−1} log((e^{ig_kB}V)(y,x)V(y,x)^{−1}), and |X|² := ½ tr X² on 𝔰𝔩(2). Then G^{(2),rel}_V[B,B] = Σ_{y,x}|τ_VB(y,x)|². At V = 1, τ_1B(y,x) is the mean of B(Γ) over 𝒢(y,x), so G^{(2),rel}_1 = SA's flat operator (CF2–CF3, FX27: GF(e^{ita}) = ½t²‖Ga‖², hence G^TG). At every real V whose contour families have diameter at most c: |τ_VB(y,x)| ≤ C_L sup|B| on the stencil of B(y), so ‖G^{(2),rel}_V‖ ≤ C_L. If |V(b) − V_r(b)| ≤ δ ≤ c with V_r real, then ‖G^{(2),rel}_V − G^{(2),rel}_{V_r}‖ ≤ C_Lδ. Finally |GF^{rel}_{≥3}(B;V)| ≤ C_L g_k sup|B|³ when g_k sup|B| ≤ c.

*Proof.* (a)–(c) are `ur-gauge.md` Lemma 4 (a)–(c), checked by Codex (ADVANCE for the relative construction); the normalisation does not enter them. For complex h in (c) the same algebra holds, because the mean is bi-covariant under G^c-maps near G (SA 7069: M({u𝐔_jv}) = uM v).
(d) At B = 0 the ratio is 1. The logarithm X(B) of an SL(2,ℂ) element near 1 is traceless, and 1 − ½ tr e^{iX} = ¼ tr X² + O(X⁴). So the first derivative vanishes.
(e) X(B) = g_kτ_VB + O(g_k²|B|²). So x_k[¼ tr X²] = ¼ tr(τ_VB)² + O(g_k|B|³) = ½|τ_VB|² + O(g_k|B|³). This gives the Hessian, the value at V = 1 (SA 7878: "when V^{bg}_k = 1, B(y,x) coincides with the mean of B(Γ)"), and the cubic bound by Cauchy on the disc g_k sup|B| < 2c. At real V each contour transport is unitary, so the linear part of log V(Γ)-variations is Σ_{b∈Γ} Ad(transport)g_kB(b), of size at most 2(L−1)g_k sup|B|. The Federbush mean is a contraction fixed point with constants uniform in the family (SA 7773), so its derivative is a weighted mean of these with total weight 1 + O(c). This gives C_L. The perturbation bound follows by Cauchy in V on the polydisc of radius c around V_r. □

**Lemma 2 (core bound for the relative precision).** Assume the hypotheses of `a2-layers.md` Theorems A–B and `a2-full.md` Theorem II, and the further ceiling (C_II + C_R)(α_1 + γ_0) ≤ c_L/8, with C_R := C_L³ from Lemma 1(e). Then at **every** regular pair 𝐏 of the step, real or complex, with independent current, and on every conditioning set Y:
- (i) Re⟨u, χ_Y𝖠^{rel}(𝐏)χ_Yu⟩_H ≥ (5/8)c_L‖u‖²;
- (ii) ‖𝖠^{rel}(𝐏)‖ ≤ C_A + c_L/4 + C_Rα_1;
- (iii) `h-walk.md` Theorem H holds for 𝖠^{rel}, with A^{loc,rel}_κ := θ_κ𝖢_V^T(G^{(2),rel}_V − a)𝖢_V, and every walk term is covariant under every gauge map;
- (iv) `a2-full.md` Theorem A2-full and Lemma 5.2 (the consumed and decoupled precisions) hold for 𝖠^{rel} at every such 𝐏, with c_L/2 replaced by c_L/2 − c_L/8 in their conclusions;
- (v) the gauge-fixing gradient term of `a2-full.md` §4 is identically zero for (REL′).

*Proof.* *Reduction to a block-axial real part.* Let U be the real centre of 𝐏 and V_r := 𝓜^kU. Put h_k(y) := 1 at centres and h_k(x) := V_r(y,x) for x ∈ B(y)∖y. Then V_r^{h_k}(y,x) = h_k(y)V_r(y,x)h_k(x)^{−1} = 1. Let h be the bare lift of h_k, constant on level-k pillars. It is unitary, and 𝓜^k(U^h) = (𝓜^kU)^{h_k} (covariance of the averages, (I2) of `h-walk.md`). The simple clauses (R4), the tower clauses and the level-k gauge clause bound gauge-invariant or covariant quantities, so 𝐏^h is a regular pair with the same radii. By Lemma 1(c) and the covariance of Δ_k and 𝖢_V under every bare map (`a2-full.md` §10 item 5), 𝖠^{rel}(𝐏) = Ad(h)^{−1}𝖠^{rel}(𝐏^h)Ad(h). Ad(h) is unitary on the free coordinates and commutes with χ_Y. So it suffices to prove (i)–(iv) at 𝐏^h, whose real part is block axial.
*At a block-axial real part.* `a2-full.md` Lemma 4.1(b) gives V_c(y,x) = e^{iθ_{yx}} with |θ_{yx}| ≤ C_Lα_1 for V_c := 𝓜^k𝐔^h. Expand both exponents to second order in D at a pair (y,x). With X = δ(D) + q(D) + O(D³) the logarithm of (e^{iD}V_c)(y,x)V_c(y,x)^{−1}, the relative summand is ¼ tr δ² + O(D³). The absolute summand is 1 − ½ tr(e^{iX}e^{iθ}) = [1 − ½ tr e^{iθ}] + ½ tr(Xθ) + ¼ tr(X²) + O(|X|²|θ| + |X|³), using tr X = 0 and X² = −det X·1. So the two quadratic parts differ by at most C|θ|(|q(D)| + |δ(D)|²) ≤ C_L|θ| sup|D|². Hence ‖𝖢_V^T(G^{(2),rel}_{V_c} − G^{(2)}_{V_c})𝖢_V‖ ≤ C_Rα_1. Then 𝖠^{rel} = A^{full} + 𝖢_V^TE^{(2)}_V[Ĵ_{GF}]𝖢_V + 𝖢_V^T(G^{(2),rel} − G^{(2)})𝖢_V, and `a2-full.md` Theorem II and (4.1) give Re⟨u,𝖠^{rel}u⟩_H ≥ (3/4 − 1/8)c_L‖u‖². Compression to Y preserves this. Lemma 5.1 gives (ii). (iii): Lemma 1(e) is input (I3) of `h-walk.md` for G^{(2),rel}_V, so Theorem H applies verbatim; Lemma 1(c) gives the gauge clause of (H3) for every map. (iv): the cited proofs read the precision only through (i), (ii) and Theorem H, and the extra perturbations are those already bounded there. (v) is Lemma 1(d). □

So the operator inputs of the regular step hold for (REL′) at every regular pair. For SA's absolute rule they are proved only at pairs whose real part is block axial (`a2-full.md` §10 item 5).

**Proposition 3 (full invariance of the regular family under (REL′)).** Let every regular step use (REL′). Let T be a term formed by regular steps: a regular member G of level j (no stored field, SA 5883–5888; formed as a product, trace or logarithm of walk, carrier and cluster terms), its own-counterterm member G̃ := G − b_j𝖠_{j,z}, a pointed total Σ_{X∋z}G(X,·,z), or a regular contribution to R^{(j)} (the aged terms and the t_2 expectation of young terms, SA 7895–7900). Then:
- (i) T(X,𝐏^g,z) = T(X,𝐏,z) for every real bare gauge map g and every pair 𝐏, real or complex, with 𝐏 and 𝐏^g in its domain;
- (ii) the same holds for every complex g in a connected set of maps that contains a real map and keeps 𝐏^g in the domain;
- (iii) in particular (FG) of `ur-gauge.md` §2 holds for G and for G̃.

*Proof.* (i) This is the argument of `ur-gauge.md` Proposition 5 (i). Codex checked it as correct for newly defined relative members (`gates/ur-gauge-check.md` §2). (REL′) has the same ingredients; its normalisation is a constant and does not enter covariance. In order: the averages are covariant, 𝓜^k(𝐔^g) = (𝓜^k𝐔)^{g_k}; the six propagators, Δ_k, 𝖢_V and E^{(2)} are covariant under every bare map (`h-walk.md` §8; `a2-full.md` §10 item 5); G^{(2),rel}_V and GF^{rel}_{≥3} are covariant (Lemma 1(c)); the Wilson action is invariant; lower members are invariant by induction on the level, with the bare action as base. These identities are algebraic, so they hold at complex pairs for real g. Then every walk, carrier and cluster term is covariant, and a product, trace or logarithm of covariant terms is invariant. The tent action 𝖠_{j,z} = A(h_z,·) is a sum of plaquette terms, so it is invariant. A pointed total is a sum of invariant terms. The aged and young regular contributions to R^{(j)} are built from the same ingredients and from lower regular terms. (ii) g ↦ T(X,𝐏^g,z) is holomorphic on that set. By (i) it is constant on its unitary points, which form a totally real submanifold of full dimension. The identity theorem gives (ii); this is SA 7913's argument. (iii) is (i) at real pairs near (1,0). □

**Proposition 4 (identification with SA's family; the invariant extension).** Write G^{rel} for a member formed with (REL′) at every regular step and G^{abs} for the member formed with SA's factor. Let 𝒜_j be the set of pairs whose averaged backgrounds have (𝓜^n𝐔)(y,x) = 1 at every pair of every factor block, at every level n < j.
- (a) *Measure layer.* The actual step puts the factor only on blocks where every background contour is 1 (SA 7875), with V^{bg}_k = 𝓜^kU_{k+1} a function of V_{k+1}. There 𝔊^{rel}_k = 𝔊_k identically (Lemma 1(b)). So the transformation T, every measure-level identity of the step, and every total they produce at physical data are unchanged.
- (b) *Formula layer on the slice.* 𝒜_{k+1} contains every physical pair in the prescribed representative (Id) and its holomorphic continuation in the datum, because the tower axial continuation keeps every contour variable 1 (`a2-full.md` Theorem A2-full; `prefactor-loc.md` §2). At 𝐏 ∈ 𝒜_{k+1} the step-k integrand is the same function of B under both rules, with every Taylor coefficient, and 𝖠^{rel}(𝐏) = 𝖠(𝐏).
- (c) *Members on the slice.* Suppose that SA's step, at a pair of 𝒜_{k+1}, reads every lower member only at pairs of 𝒜_k. This holds where it reads U_k(·), whose values lie in Ax°(·,1) (SA 7185), and where it subtracts lower members at the pair itself. Then G^{rel} = G^{abs} on 𝒜_j at every level, by induction with (b). In particular G^{rel}_z∘P^c = G^{abs}_z∘P^c on the datum polydisc.
- (d) *Any representative.* For the Landau branch P^L and for the box inner triples P^T_{in}: G^{rel}_z∘P^L = G^{rel}_z∘P^c on the datum polydisc. At real data, P^c(B) = P^L(B)^{u_B} with u_B real (`a3-derivative.md` Proposition 6.4; `ur-gauge.md` Lemma 2), so Proposition 3 (i) applies. Both sides are holomorphic on the polydisc, which is connected, and they agree on its real points.
- (e) *Uniqueness: G^{rel} is SA 7754's invariant extension.* Let 𝒞 be a connected component of the core that meets the real pairs. If F is holomorphic on 𝒞, invariant under real gauge maps, and equal to G^{abs} on the real pairs of 𝒞 ∩ 𝒜_j, then F = G^{rel} on 𝒞, given (c). Indeed every real pair of 𝒞 is joined by a path of real gauge maps to its tower axial representative (Ax° meets every orbit once, SA 7185); real maps preserve the core, so that representative is a real pair of 𝒞 ∩ 𝒜_j. So F = G^{rel} on the real pairs of 𝒞, and the identity theorem extends this to 𝒞.

*What (c) does not cover, and why the chain needs (REL′).* Where the chain reads members off the slice, the old values are not fixed by the slice. Examples: the box-first route's inner Landau triples (`wf-c.md` §3), and the local activities at independent-current cores (SA 14680–14683, 14895–14899, 15366–15372). These readings, and the sentences "gauge invariance removes that gauge" (`wf7-bf.md` §2) and "evaluates gauge-invariant members" (`wf-c.md` §3), use an invariance that the absolute family does not have. With G^{rel} they hold, and by (d) they reproduce the slice values.

**Remark (the absolute family).** For SA's factor written at a general background (SA 7182, 10204), the ingredient that breaks (Γ) is named exactly. At the real flat pair 1^g, with g = e^{iεT} at one non-centre site, the factor has the non-zero constant term x_k(1 − cos ε) and a non-zero linear term (`h-walk.md` test 2.1). Its quadratic form on the fibre direction at that site is cos ε instead of 1 (check D2). So 𝖠(1^g) is not conjugate to 𝖠(1). I did not compute a member's value at 1^g, so I do not claim that a particular absolute member fails (Γ). The chain does not need that claim, because (REL′) replaces the family and keeps the physical composite (Proposition 4).

## 2. (Γ): decision

**Theorem Γ.** Assume (REL′) at every regular step.
- (i) **(Γ) holds for every term of the class that regular steps form**: each regular member, each pointed total, each own-counterterm member G̃, and each regular contribution to R^{(j)}. This is Proposition 3 (i) at real pairs: for every non-wrapping X, every real pair 𝐏 in the core and every real gauge map u on X^~ with 𝐏^u in the core, T(X,𝐏^u) = T(X,𝐏).
- (ii) **For Proposition W** (`b2-extract.md` §7): (FG) holds for every old regular member and for G̃. So `ur-gauge.md` Lemma 1, Corollary 3, Theorem UR and Corollaries 6–7 apply; Codex checked them as ADVANCE conditional on (FG). Hence (UR) and (YA) are implications from (ER8u), the Landau bound (5) (conditional on P81–P82) and, for (8), (TI). Input (G) of Theorem P now holds for every map, so `p2-floor.md` defect 3 ("the requirement moves from (R) to (G)") is void.
- (iii) **For the floor** (`p2-floor.md` §3): Proposition R′ holds for the regular part of R^{(j)}, and Reduction E′ holds with the Landau branch (Proposition 4 (d)). Under the Hölder core of Section 3 the floor's Cauchy disc must be measured in the augmented norm of Lemma B below. Lemma G's gauge then also needs a Hölder bound; `a1-balaban.md` §6 supplies it at radius CMBεσ² for a critical background, rescaled as in Lemma G (this is the reading of `p2-floor.md` Reduction E′).
- (iv) **Not decided: terms formed by the large-field operation R.** The healed gas R′_♯(Y) (SA 17985–17991) enters R^{(j)} also at the never-large label (`p2-floor.md` §2). These operations keep SA's absolute factors (SA 17531, 17558), and R's test on B and last-shell test are "not gauge invariant" (SA 17585). The first missing input is

  > **(R-cov).** Each operation of R (stage integrals with 𝔊_j, the tree gauge of (3), the test on B, the last-shell test, the frame sum) is covariant under the bare gauge map that equals a given exterior real map outside each component and its top lift inside it; and R reads the exterior pair only through (REL′)-covariant ingredients.

  *Repair sketch, not proved.* Absolute 𝔊_j is invariant under maps constant on level-(j+1) blocks, so the top lift is the right extension inside a component. A test that is a norm of a field in a gauge fixed by a slice with a covariant reference is invariant up to one conjugation at the root, and norms ignore it. Whether R's references transform this way needs SA 17585–17640 and 2.10 read in full; that is rank 7's lane, not this one.

  *Why the floor cannot skip it.* The crude bound |R′_♯(Y)| ≤ Ce^{−(1+c)p_0(g_j)} with p_0(g) = A_0(log g^{−2})^{𝔭_0} (SA 6029) gives N·L^{4(K−j)}e^{−(1+c)p_0(g_j)} after the cube count. That is not bounded uniformly in K − j, since p_0 grows only like a power of log(K − j). So the healed part also needs the σ⁴ gain of a Taylor path, hence (Γ) or (R-cov).

No term of the class was found to fail (Γ) under (REL′). For SA's absolute family, (Γ) is not supplied, and the failing ingredient is the one named in the Remark above.

## 3. Repair of `bx-fix.md` along `gates/bx-fix-check.md`

Notation of `bx-fix.md` §§2–7. Kept as checked by Codex (ADVANCE): (H), the exclusion §2.3, Lemmas 0–3, Lemma 4(a), BX′-1, Lemma 5, (A2-H), the image membership of (ER8u)-H, Rule (C) for inner triples, Lemma M, Proposition PH. Below, G̃_X is an old regular member with its own counterterm, formed under (REL′); it satisfies (FG) by Proposition 3. T is a first-rule box tower T_0 ⊃ … ⊃ T_j over the flat reference, K_T the linearised **plain** constraint, ℓ^b the bare axial affine field and ℓ^T := K_Tℓ^b. Φ_T is the box critical map (P81: holomorphic, Φ_T(0) = 1, M_{𝐁_T}Φ_T(B) = e^{iB}, critical at real B), 𝓗_T its Landau map, H_T := D𝓗_T(0), and Φ_T(B) = (e^{iη𝓗_T(B)})^{u_B} with u_Bv[𝓗_T(B)] = 1 at the nodes (`a3-derivative.md` Proposition 6.4). P^T_{in}(B) := (1, 𝓗_T(B), J(e^{iη𝓗_T(B)})).

### 3.1 Lemma 4* (affine data, with the right representative)

**Lemma 4\*.**
- (b\*) DΦ_T(0)ℓ^T = ℓ^b + dχ on T_0 for a site function χ, and H_Tℓ^T = ℓ^b + dχ′ for a site function χ′. Neither χ′ nor, in general, χ needs to vanish at the nodes.
- (c\*) Let X and its read stencil lie in T_1. For P ∈ {(Φ_T, J(Φ_T)), P^T_{in}} and every datum e on the rows of T,
  D²(G̃_X∘P)(0)[ℓ^T, e] = D²G̃_X(0)[(ℓ^b,0), DP(0)e],  so  D²(G̃_X∘P)(0)[ℓ^T,ℓ^T] = D²G̃_X(0)[(ℓ^b,0),(ℓ^b,0)].

*Proof.* (b\*) *The critical representative solves the plain linear system.* In the chart Φ_T(B) = e^{iηA_B}, criticality at real B gives F′(A_B) = K_{A_B}^Tω(B) (`a3-derivative.md` Lemma 6.2). At B = 0, F′(0) = 0 and K_0 is onto, so ω(0) = 0. Differentiate along ℓ^T (real, then complex-linearly): with a_Φ := DΦ_T(0)ℓ^T and L_0 := F″(0), the Hessian of A_{T_0} at 1,
  L_0a_Φ = K_T^Tω̇,  K_Ta_Φ = ℓ^T.
*The affine field solves it too.* `bx-fix.md` §6 (b) shows L_0ℓ^b = K_T^Tλ, with λ supported on the level-0 boundary rows, and K_Tℓ^b = ℓ^T. Codex checked this part ("the boundary multiplier construction for the bare affine field is sound").
*Uniqueness up to a gradient.* Put a := a_Φ − ℓ^b. Then K_Ta = 0 and L_0a = K_T^T(ω̇ − λ). So ⟨a, L_0a⟩ = ⟨K_Ta, ω̇ − λ⟩ = 0. Since ⟨a, L_0a⟩ = Σ_{p⊂T_0}|da(p)|² in the normalisation of A_{T_0}, da = 0 on every plaquette of T_0. T_0 is a box, so a = dχ (discrete Poincaré lemma). This uses no node condition: that was the defect.
*Landau response.* In the chart, (e^{iηA})^{e^{itφ}} = e^{iη(A + tX_φ(A) + O(t²))} with X_φ(0) = −dφ (`a3-derivative.md` §6.1, Notation). So DΦ_T(0)e = H_Te − dψ_e with iψ_e := Du_B(0)e. Hence H_Tℓ^T = ℓ^b + d(χ + ψ_{ℓ^T}). □
(c\*) DG̃_X(0) = 0 by constant colour invariance, so D²(G̃_X∘P)(0)[e,e′] = D²G̃_X(0)[DP(0)e, DP(0)e′]. By (b\*), DP(0)ℓ^T = (ℓ^b + dφ, J′(1)(ℓ^b + dφ)) with φ = χ or χ′. The linear current at 1 is d^Td. On a bond all of whose plaquettes lie in T_0 it vanishes on ℓ^b (constant curl) and on dφ (dd = 0). So DP(0)ℓ^T = (ℓ^b + dφ, 0) on the stencil. `ur-gauge.md` Lemma 1 (ADVANCE given (FG); its step (v) admits any site function) gives D²G̃_X(0)[(dφ,0), w] = 0 for every w. □

### 3.2 Lemma 4′* (torus comparison through the Landau branch)

**Lemma 4′\*.** Let P_j be the level-j torus critical map in the prescribed representative (Id), P^L_j its Landau branch over 1, ℓ̃ the torus datum equal to ℓ_F on the fundamental domain centred at z, L := DP_j(0)ℓ̃ and L^L := DP^L_j(0)ℓ̃. Let T′ be an admitted box tower around z of radius R′ ≤ (torus side)/4, with X ⊂ T′_1 and D := 2 + diam X ≤ R′/2. Then

  |D²(G̃_X∘P_j)(0)[ℓ̃,ℓ̃] − D²G̃_X(0)[(ℓ^b,0),(ℓ^b,0)]| ≤ C‖D²G̃_X(0)‖_X |F|² D R′^s e^{−c(R′−D)}.

*Proof.* (1) *Switch to the Landau branch.* At real data P_j = (P^L_j)^{u}, with u real and u_Bv[a] = 1 at the tops (`ur-gauge.md` Lemma 2; `a3-derivative.md` Proposition 6.4). So L = L^L + dψ on the torus. The current of a gradient at 1 is 0. By `ur-gauge.md` Lemma 1, D²(G̃_X∘P_j)(0)[ℓ̃,ℓ̃] = D²G̃_X(0)[(L^L, J′L^L), (L^L, J′L^L)]. The contour response L itself has no uniform decay (`ur-ya.md` (3)–(4)); L^L has it (`ur-ya.md` (5)).
(2) *Restriction.* `a1-balaban.md` (9.3) (gated) linearised gives L|_{T′_0} = DΦ_{T′}(0)[K_{T′}L] + gradient. A pure gauge datum has a gradient response: dψ solves the linear box system with datum K_{T′}dψ = d_{rows}(ψ|_{nodes}) (exact covariance of the averages) and L_0dψ = 0, so (b\*)'s uniqueness gives DΦ_{T′}(0)[d_{rows}ψ] = dψ + gradient. Hence L^L|_{T′_0} = DΦ_{T′}(0)[K_{T′}L^L] + gradient = H_{T′}[K_{T′}L^L] + gradient, by (b\*)'s Landau relation.
(3) *Decompose the datum.* Let ψ̂ be the pillar lift of ψ from the tops to all nodes of T′. On level-j rows, K_{T′}L = ℓ̃ = ℓ_F = ℓ^{T′} (torus constraint; Lemma 4(a)), so K_{T′}L^L = ℓ^{T′} − d_{rows}ψ̂ there. Define δ̂ := K_{T′}L^L − ℓ^{T′} + d_{rows}ψ̂. It vanishes on level-j rows and lives on the collar rows. By (2) applied to the pure gauge datum d_{rows}ψ̂, H_{T′}[K_{T′}L^L] = ℓ^b + H_{T′}δ̂ + gradient.
(4) *Bound the collar datum.* Near T′, |L^L| ≤ CΣ_ce^{−δd}|ℓ̃(c)| ≤ C|F|R′, uniformly in j. K_{T′} has row norm at most 2 (`o1-decoupled.md` 4.3). |ℓ^{T′}| ≤ |F|R′. At a top, ψ = −(linear node factor of L^L), a pillar mean of transported values of L^L (SA 7092–7096; `a3-derivative.md` (35)–(36)), so |ψ̂| ≤ C|F|R′. Hence |δ̂| ≤ C|F|R′.
(5) *Decay.* [T4]'s decay for the box Landau response, with the cell-weighted sum, gives ‖H_{T′}δ̂‖_X ≤ C|F|R′S_{θ/2}e^{−(θ/2)d(X,\text{collar})}, and d(X, collar) ≥ c(R′ − D). The current slot is bounded by [T4]'s D^TD bound (`a3-derivative.md` 7.6).
(6) *Conclude.* On X, (L^L, J′L^L) = (ℓ^b, 0) + (E, J′E) + gradient with E := H_{T′}δ̂. Drop the gradient by `ur-gauge.md` Lemma 1, and expand bilinearly. □

### 3.3 Lemma P (an admitted node-gauge path; repairs BX′-4)

For data B on the rows of T put 𝒫_r := {sup|B| < r} and F(B) := G̃_X(P^T_{in}(B)). Let r_B be at most the inner admission radius of `wf-c.md` Theorem A (A2) and of Lemma 5, so that P^T_{in}(B) lies in G̃_X's core for B ∈ 𝒫_{r_B}. A node gauge w acts by e^{iB^w(c)} := w(c_−)e^{iB(c)}w(c_+)^{−1}; cn(w) := sup_x|w(x)||w(x)^{−1}|. For two data put Π(B,B′) := max_x min_γ Σ_{c∈γ}(|B(c)| + |B′(c)|), the minimum over row paths γ from z to the node x.

**Lemma P.** There are C_P, c_P depending only on the box geometry constants such that: if B, B′ ∈ 𝒫_{c_Pr_B}, B′ = B^w with cn(w) ≤ 2, and C_PΠ(B,B′) ≤ 1, then F(B′) = F(B).

*Proof.* (i) *Infinitesimal invariance on the whole polydisc.* Let B ∈ 𝒫_{r_B} be real and w a unitary node gauge near 1. Φ_T(B^w) and Φ_T(B)^{w̃} (w̃ the pillar lift) are real critical fields near 1 with the same plain datum, since the action is invariant and the constraint set is covariant. By [T4]'s uniqueness of the critical orbit modulo residual gauge they differ by a real residual map. With Φ_T = (e^{iη𝓗_T})^{u_B}, the triples P^T_{in}(B^w) and P^T_{in}(B) differ by a real gauge map, and both lie in the core. Proposition 3 (i) gives F(B^w) = F(B). Differentiate at w = 1 along e^{itξ}: dF(B)[δ_ξB] = 0, with δ_ξB the infinitesimal action. This is complex-linear in ξ and holomorphic in B. It vanishes on the real points of the connected polydisc 𝒫_{r_B}, so it vanishes on all of 𝒫_{r_B}, for every complex ξ.
(ii) *Adjacent ratios.* From B′ = B^w, w(c_−)w(c_+)^{−1} = e^{iB′(c)}·w(c_+)e^{−iB(c)}w(c_+)^{−1}. So |w(c_−)w(c_+)^{−1} − 1| ≤ C_1(|B(c)| + |B′(c)|) =: C_1β(c), using cn(w) ≤ 2. This is the bound the check asks for; a condition number alone does not give it.
(iii) *The path.* Let c := w(z) = u e^{Y} (polar form: u ∈ SU(2), Y Hermitian, e^{2|Y|} ≤ cn(c) ≤ 2). Stage 1: the constant maps c_t := u_te^{tY}, with u_t ⊂ SU(2) from 1 to u. A constant map acts by B ↦ Ad(c_t)B, so the data stay below 2 sup|B|. Stage 2: w_t := c·e^{tℓ} with ℓ := log(c^{−1}w) nodewise. By (ii), c^{−1}w(c_−)(c^{−1}w(c_+))^{−1} is within 2C_1β(c) of 1. Multiplying along a row path from z gives |ℓ(x)| ≤ C_2Π(B,B′) ≤ 1/8. By BCH, log(e^{ℓ_1}e^{−ℓ_2}) = (ℓ_1 − ℓ_2)(1 + O(|ℓ_1| + |ℓ_2|)), so |ℓ(c_−) − ℓ(c_+)| ≤ C_3β(c). The datum along stage 2 is Ad(c) of (1/i)log(e^{tℓ(c_−)}e^{iB(c)}e^{−tℓ(c_+)}), of size at most C_4β(c) < r_B for c_P small. So B^{w_t} ∈ 𝒫_{r_B} on the whole path.
(iv) By (i), d/dt F(B^{w_t}) = dF(B^{w_t})[δ_{ξ_t}B^{w_t}] = 0, with ξ_t the generator of the path. So F(B′) = F(B). □

*Application (BX\*-4 below).* Take B = B^N, Lemma N's node-reduced datum of the window curve (`wf-room-2.md` 7.2; this is the datum whose inner triple Theorem A (A2) admits), and B′ = B̂, the complete axial datum of Lemma 3. Both are node-gauge transforms of the plain box datum, so B̂ = (B^N)^w with w the composite of Lemma N's v, the real (H) gauge g, the straightening node factors of Lemma 1 and the comb gauge g_z. The unitary parts do not change cn; Lemma N gives cn(h) ≤ e^{CMα_1}; the straightening factors and g_z are products of exponentials of complex data of size at most C a_* on the box. So cn(w) ≤ e^{CM(α_1 + a_*)} ≤ 2. On level-j rows |B̂| ≤ CMa_{out}σ (BX′-1) and |B^N| ≤ C_BMα_0τ with τ ≤ σ (Lemma N); level-q rows carry the extra factor L^{q−j}. A row path from z needs at most CM/σ level-j rows and C M_1 rows per lower level, so Π(B^N, B̂) ≤ CM²(a_{out} + α_0) + CMM_1a_{out}σΣ_{q<j}L^{q−j} ≤ C_MM a_{out}. The ceiling C_PC_MMa_{out} ≤ 1 is one more smallness condition on the radii after M.

*Note on Lemma P.* If the row graph of T has several components, take one base node per component. A map that is constant on a component acts on each of its rows by one conjugation, so stages 1–2 and the bounds are unchanged; Π is measured from each base node. The ceiling C_PC_MMa_{out} ≤ 1 then also covers the collar layers, whose rows carry the factor L^{q−j}.

### 3.4 Lemma B (the augmented pair ball; repairs (ER8u)-H's ball claim)

For a level-j pair (1, A′, 𝐉) on X put N^H_X(A′,𝐉) := max(‖(A′,𝐉)‖_{1,j;X}, [∇A′]_{α_H,X}).

**Lemma B.** Let r ≤ min(cα_j, α_{1,j}), with cα_j the radius of (ER8u). Every pair (1, A′, 𝐉) on X with N^H_X(A′,𝐉) < r lies in U^H_j(X). Hence, for a regular member G of level j bounded by g_je^{−κd_j(X)} on U^H_j(X), Cauchy's estimates hold on this ball in the norm N^H_X: |D^nG(X,(1,0),z)[v,…,v]| ≤ n!g_je^{−κd_j(X)}(N^H_X(v)/r)^n, and the Taylor remainder after order n is at most 2g_je^{−κd_j(X)}(2N^H_X(v)/r)^{n+1} for N^H_X(v) ≤ r/4.

*Proof.* (ER8u) puts the pair in U°_j(X). For (H) take g = 1 and A_r = 0 on every cube D ⊂ X: the real clauses hold trivially, A″ = A′, and [∇A′]_{α_H,D} ≤ [∇A′]_{α_H,X} < r ≤ α_{1,j}. The ball is convex and balanced, so λ ↦ G(X,(1,λv),z) is holomorphic on |λ| < r/N^H_X(v); Cauchy's estimate in λ gives the bounds. □

This is the "augmented pair ball" of the check's defect 3. Codex's example A_2 = rη cos(πx_1/η)T has first-order norm O(r) and lies outside it, as it must.

### 3.5 Theorem BX* (the repaired package) and how Proposition W reads it

Put α′_k := α_k + α_{0,k+1}. With a_* of `bx-fix.md` (4.1), a_{out} := C_8a_* ≤ C_M α′_k, because α_1 ≤ C′Mα_{0,k+1}. This removes the radius reversal: no lower bound α_{0,k+1} ≤ Cα_k is used. The age bound holds for α′_k: with α_{0,i}^{−2} = cθ_i(log θ_i)^{−2q} and the flow θ_j ≤ θ_{k+1} + B_♯(k+1−j), (α_{0,k+1}/α_{0,j})² ≤ θ_j/θ_{k+1} ≤ 1 + B_♯(k+1−j). So ρ′ := max(1, α′_k/α_j) satisfies ρ′² ≤ C_M(2 + k − j), and (WF1)'s weights change only by C_M.

**Theorem BX\* (implication; proved by Claude, not yet checked).** Assume the hypotheses of `bx-fix.md` Lemma 2 on the input 𝐏 ∈ U^H_{k+1} at half radii, [T4] for the Rule W box tower T of R_z, [9.3], (REL′) at every regular step, the old-age condition C_{ax}a_{out}σ ≤ r_B/2 (SA (PW5)) and C_PC_MMa_{out} ≤ 1. Then:
- **(BX\*-1) datum.** BX′-1 holds as stated (Codex: ADVANCE).
- **(BX\*-2) pair.** For X ∋ z with stencil in T_1 and D := 2 + diam X ≤ C_w/(2σ), on X,
  P^T_{in}(B̂) = (1, ℓ^b + dψ + e_1, e_2),  dψ := H_Tℓ^T − ℓ^b a gradient (Lemma 4\*),
  N^H_X(e) ≤ CD^s[a_{out}σ^{2+α_H} + r_B^{−1}a_{out}²σ⁴],  N^H_X(ℓ^b + dψ) ≤ CD^sa_{out}σ².
- **(BX\*-3) Hessian.** D²(G̃_X∘P^T_{in})(0)[ℓ^T,ℓ^T] = D²G̃_X(0)[(ℓ^b,0),(ℓ^b,0)], and |D²G̃_X(0)[(ℓ^b,0),(ℓ^b,0)] − D²(G̃_X∘P_j)(0)[ℓ̃,ℓ̃]| ≤ C‖D²G̃_X(0)‖_X|F|²D^se^{−cM/σ}.
- **(BX\*-4) node gauge.** G̃_X(P^T_{in}(B̂)) = G̃_X(P^T_{in}(B^N)), the window value of `wf-c.md` Theorem A.

*Proof.* (BX\*-2): the proof of BX′-2 with DP^T_{in}(0)ℓ^T = (ℓ^b + dψ, 0) taken from Lemma 4\*(b\*),(c\*) instead of Lemma 4(b). Then e_1 = H_Tr + (N_2)_1 and e_2 = J′(1)H_Tr + (N_2)_2, and BX′-2's sums bound them; [T4]'s Hölder member has the same kernel decay and gives the Hölder part of N^H. The second bound is [T4]'s value, gradient and Hölder members applied to ℓ^T, with |F| ≤ Ca_{out}σ² from BX′-1. (BX\*-3): Lemma 4\*(c\*) with T, and Lemma 4′\* with T′ := T and R′ := C_w/σ. (BX\*-4): Lemma P with its application. □

**Proposition W\* (the regular part of (19), read with BX\*).** Under the hypotheses of `b2-extract.md` Proposition W, with (BX) replaced by BX\*, (FG) by Proposition 3, α_k by α′_k and ρ by ρ′, (WF8) holds: the inner window value after the vacuum and own-counterterm subtraction is at most C_Mg_j[ρ′²σ^{4+α_H} + ρ′³σ⁶]. So the regular part of (19) holds with ω_n = C_M(1 + n)^{3/2}L^{−α_H(n−1)}.

*Proof.* Proposition W's Steps 1 and 4 expand in the datum; the check (defect 3) shows that this lacks room. Expand instead in pair space. By BX\*-4 the window value is G̃_X(P^T_{in}(B̂)). Write v := (ℓ^b + dψ + e_1, e_2) from BX\*-2, so N^H_X(v) ≤ CD^sa_{out}σ². For domains with CD^sa_{out}σ² ≤ r/4, r := c′α_j, Lemma B gives
  G̃_X(P^T_{in}(B̂)) = G̃_X(1,0) + ½D²G̃_X(0)[v,v] + R_3,  |R_3| ≤ Cg_je^{−κd_j(X)}(D^sa_{out}σ²/α_j)³.
The gradient drops from the quadratic term (`ur-gauge.md` Lemma 1): D²G̃_X(0)[v,v] = D²G̃_X(0)[(ℓ^b+e_1,e_2),(ℓ^b+e_1,e_2)]. It stays in R_3, where it is small by BX\*-2. *Step 2:* Σ_{X∋z}D²G̃_X(0)[(ℓ^b,0),(ℓ^b,0)] = Σ_{X∋z}D²(G̃_X∘P_j)(0)[ℓ̃,ℓ̃] + O(g_jα_j^{−2}a_{out}²σ⁴e^{−cM/σ}) = O(g_jα_j^{−2}a_{out}²σ⁴e^{−cM/σ}), by BX\*-3 and (P20). *Step 3:* the cross and error terms are at most Cg_je^{−κd_j(X)}α_j^{−2}D^{2s}a_{out}σ²[a_{out}σ^{2+α_H} + r_B^{−1}a_{out}²σ⁴], by Lemma B's Cauchy bound. *Steps 5–7* are unchanged, with (YA) for the remaining domains, since 1 + T² ≤ 2T³. Summation with the rooted count, α′_k and ρ′ gives (WF8) and the weights. □

So Proposition W reads (P20), (ER8u) with Lemma B, BX\*, (YA), (UR) for (8), and (FG). Each input of BX\* is on the ledger already: [T4], [AV], [9.3], [PW], [NL], [PW-H] (Proposition PH), and (H) on the step's input.

### 3.6 Proposition I* (the Hölder core is preserved)

**Lemma O (outer evaluations satisfy (H)).** Let 𝐏 ∈ U^H_{k+1} at half radii on the step's domain, and 𝐔_{t,ν} = e^{iηh}𝐔 the step's curve, with h := (η_k/η)(t+νζ)𝐇_k, for every fine parameter of the polydisc. Let j ≤ k and X a level-j domain in the step's domain. Assume CL^{1−α_H}(s_k + c_ν) ≤ 1/8, the radius convention α_k ≤ C_αα_{0,k}, Mα_{0,i} ≤ α_{1,i} at every level, and L ≥ L_0(C_α). Then the level-j reading of (𝐔_{t,ν}, 𝐉) on X satisfies (H) at level j at half its radii, on every cube of side at most C_boxLM.

*Proof.* A level-j cube of side C_boxLM has side C_boxLMσ′ ≤ C_boxLM in level-(k+1) units, σ′ = L^{−(k+1−j)}. Take 𝐏's (H) gauge g on a level-(k+1) cube containing it. Steps 1–3 of `bx-fix.md` Lemma 2 (ADVANCE) use only (H) of 𝐏 and (3.1), which hold at every top-layer point. They give, in level-(k+1) units, [∇A_r]_α < C_potMα_{0,k+1}/2 and [∇(A″ ⊞ h̃)]_α ≤ α_{1,k+1}/2 + CL³(s_k + c_ν)α_k. In level-j units a gradient Hölder seminorm gains σ′^{2+α_H} ≤ L^{−2−α_H}. For the response part, σ′^{2+α_H}CL³(s_k + c_ν)α_k ≤ L^{−(2+α_H)(k−j)}α_k/8. By the flow, α_{0,i}/α_{0,j} ≤ (1 + B_♯(i−j))^{1/2} for i > j, and the same holds for α_1 where α_1 ∝ α_0. Since L^{−(2+α_H)(k+1−j)}(1 + B_♯(k+1−j))^{1/2} ≤ 1/(4C_α) for L ≥ L_0(C_α), all three bounds are below half the level-j radii. The binding case is the young age j = k. In layered position (W2) the layer factor and ambient units enter as in `bx-fix.md` §10, last paragraph. □

**Proposition I\* (implication).** Suppose (I_k): every regular member of level ℓ ≤ k is holomorphic on U^H_ℓ with its class bounds. In the box-first step k (`wf7-bf.md`, `cond-c.md` Rule W, `wf-c.md` Theorem A), every member evaluation lies in U^H_ℓ:
1. inner Landau triples, by Lemma 5 and (A2-H) (ADVANCE);
2. points of the pair-space Cauchy and Taylor balls of Proposition W\*, (UR) and (YA), by Lemma B; Theorem UR's bidisc uses N^H, and the Landau columns satisfy N^H_X(h^Lδ_x) ≤ C′e^{−δ dist(x,X)} by (5) and [T4]'s Hölder member;
3. the outer presentations of long members (`wf7-bf.md` §3), by Lemma O together with their original core admission, which `wf7-bf.md` keeps;
4. Cauchy segments between two pairs with a common real centre and a common (H) gauge, since (H) is convex in A′ at fixed U and g (Rule (C), extended from inner triples to this case).
At every input in U^H_{k+1} at half radii Theorem BX\* holds, so Proposition W\* gives (19) there, given its other inputs. With B4's other estimates, the new members of level k+1 are bounded on U^H_{k+1}, and (I_{k+1}) follows. Large-field consumers are still not checked against (H), as `bx-fix.md` §9 says.

*Proof.* Items 1–4 cover the evaluation points that `bx-fix.md` §9 lists, with item 3 added for the outer presentations the check names (defect 4), and item 2 replacing the image argument (defect 3). Item 2 for (BX) is Theorem BX\*. □

## 4. Result

**Kind of result (FINISH item 9).** A proof of steps the outline sketches (the invariant extension and full covariance, SA 7748–7754 and 7913), and a repair of our own text (`ur-gauge.md` §3; `bx-fix.md` §§6–8). It is not a correction of their text, and not an issue candidate.

**Proved here by Claude, not yet checked by the other model:**
1. **Rule (REL′)**, the correctly normalised relative factor (D1 repaired). Its precision part G^{(2),rel}_V is the B-Hessian of x_kGF^{rel}_k(e^{ig_kB}V;V), that is τ_V^*τ_V, with no extra x_k. It equals SA's flat operator at V = 1 and SA 7878's coefficient on the slice. **Lemma 1:** Faddeev–Popov identity, slice agreement, covariance under every gauge map, no linear term, and the bounds (I3) needs.
2. **Lemma 2 (core bound).** The half-gap, the upper bound, Theorem H's walk expansion and the consumed and decoupled precisions hold for 𝖠^{rel} at **every** regular pair, real or complex, with independent current. Proof: real covariance moves the real part to block axial, and there 𝖠^{rel} is within C_Rα_1 of SA's operator. For SA's rule these bounds were proved only at block-axial pairs.
3. **Proposition 3.** Every term that regular steps form under (REL′) is invariant under every real bare gauge map, at real and complex pairs, and under complex maps connected to them in the domain. So (FG) holds for every old regular member and its own-counterterm member.
4. **Proposition 4 (identification).** The measure layer is unchanged. On the axial slice the step's integrand is unchanged. Where SA's step reads lower members only on the slice, the members agree there, so G^{rel}∘P^c = G^{abs}∘P^c on the datum polydisc. The Landau branch and the box inner triples give the same composite. G^{rel} is the unique holomorphic invariant extension of the slice values: SA 7754's F^♮. This answers D2: the off-slice values do change, and the chain must read G^{rel} there.
5. **Theorem Γ.** (Γ) **holds** for every term of the class formed by regular steps: members, pointed totals, own-counterterm members, and the regular parts of R^{(j)}. Hence `ur-gauge.md` Theorem UR and Corollaries 6–7 apply, and (UR), (YA) are implications from (ER8u) (supplied: (ER7), Codex, checked by Claude), (5) (conditional on P81–P82) and (TI). `p2-floor.md` Proposition R′ (regular part) and Reduction E′ hold.
6. **Lemma 4\*.** The critical representative's affine response is ℓ^b + dχ, by an elementary uniqueness argument (closed forms on a box are exact). The Landau response is ℓ^b plus a gradient that need not vanish at nodes. The Hessian identity follows from (FG) (defect 1 repaired).
7. **Lemma 4′\*.** Torus comparison through the Landau branch, with error e^{−c(R′−D)}. It avoids the contour response, which has no uniform decay (`ur-ya.md` (3)–(4)).
8. **Lemma P.** An admitted node-gauge path from the data bounds and cn(w) ≤ 2. Adjacent-node ratios are bounded by the data (defect 2 repaired).
9. **Lemma B.** The augmented pair ball lies in U^H, and Cauchy estimates run in N^H (defect 3 repaired).
10. **Theorem BX\* and Proposition W\*.** (BX) on the Hölder core, expanded in pair space, with a_{out} ≤ C_Mα′_k and the age bound for α′_k (radius reversal repaired). This gives (WF8) and the regular part of (19).
11. **Lemma O and Proposition I\*.** Outer presentations satisfy (H), and the Hölder core is preserved under the step (defect 4 repaired).

**What stays open.**
- **(R-cov):** (Γ) for terms formed by the large-field operation R (the healed gas, SA 17985–17991). It binds the floor's R-part, not (19). No failing term was found.
- B4's (19) still reads (20) through (TI) (`ti-2.md` checked; (DOM) by Codex, not yet checked; (ID) = B4 at lower levels), and BX\*'s ledger inputs [T4] (conditional on P81, P82°, M1), [9.3], [PW], [NL], [AV].
- Hypothesis (c) of Proposition 4 (SA's step reads lower members only on the slice) was not checked passage by passage. The chain does not need it: by Proposition 4 (d)–(e) it can take G^{rel} as its definition.
- For SA's absolute family I name the failing ingredient (Remark in §1) but did not compute a member at 1^g.
- This note needs one line-by-line check by Codex.

**For the lead (evidence for other files; only this file was written).**
- `ur-gauge.md` §3: replace (REL)'s operator definition by (REL′), Lemma 4(d) by Lemma 1(e), and Proposition 5 (ii)–(iii) by Proposition 4 and Lemma 2.
- `h-walk.md` test 2.1 and (H3), `a2-full.md` §4 and §10 item 5: under (REL′) the gauge clause is full, the gauge-fixing gradient term is zero, and Theorem II needs no axial hypothesis.
- `b2-extract.md` Proposition W: Steps 1 and 4 expand in pair space on the augmented ball (Proposition W\*); (BX) becomes BX\*; α_k becomes α′_k; (FG) comes from (REL′).
- `p2-floor.md` §3: (Γ) is supplied for regular terms; the R-part is open only at healed terms, through (R-cov); under the Hölder core, Lemma G's gauge reads the Hölder bound of `a1-balaban.md` §6.
- `bx-fix.md`: Lemma 4 (b), (c), Lemma 4′, BX′-2 to BX′-4, the ball claim of (ER8u)-H and Proposition I are replaced by Lemmas 4\*, 4′\*, P, B, O, Theorem BX\* and Proposition I\*.
- `t0-skeleton.md`: in B4's (19), (UR), (YA) and (BX) become implications under (REL′); in D1's floor, (P3) reduces to (R-cov) for healed terms and Proposition W\*'s inputs.

**Moves.** (Γ) is decided for regular terms (it holds under (REL′)) and is open only for R-stage terms, through (R-cov). (BX) is repaired as BX\*. So B4's (19) reads (20), (ER7), the ledger inputs of BX\* and the Hölder core, and nothing new. If Codex's check passes, (UR), (YA) and (BX) leave (19)'s list of open inputs.

**Method.** No numeric job was run; none was needed. Every step is a written argument. Only this file was written. **Status:** complete, 2026-11-04 (worker).
