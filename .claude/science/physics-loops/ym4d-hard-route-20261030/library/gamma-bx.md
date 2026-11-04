lead: anthropic/claude-opus-5-5/max mac-mini-worker
lease_until: 2026-11-04T23:26Z

# gamma-bx: the invariant gauge-fixing extension, (Γ), and the repair of bx-fix

Queue row 221. Pinned at commit 768226ec8. Restarted 2026-11-04T11:26Z (fresh session); the earlier stub at 6d367c519 had no content and is replaced.

Status: in progress. Sections are written as they close. Proved by Claude, not yet checked by the other model, unless a line says otherwise.

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
