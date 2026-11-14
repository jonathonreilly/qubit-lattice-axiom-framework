lead: anthropic/claude-opus-5-5/max mac-mini-worker
lease_until: 2026-11-04T13:53Z

# ur-gauge: check of `ur-ya.md`, the Hessian gauge identity, (UR) and (YA)

Queue row 217. Written 2026-11-04 on commit 1face7c7e. Complete for this item.

Provenance: Claude Opus 5.5 (`claude-opus-5-5`), effort max, Mac mini worker; commit 1face7c7e; Sussman-Alpoge outline `YM4_sketch_500.tex` at `31a47c543775`, fetched by URL to a scratch folder (SHA-1 107abaef…2348885), cited as SA nnnn; Balaban CMP 109 read from `~/ym4d-papers/cmp109.txt`. One reading by one model, not an audit. Every step is by hand; no numerics were run, so the numeric lock was not taken (memory free was 43%, below the 50% floor, in any case). No subagent.

Credit: Ethan Sussman and Levent Alpoge, with Claude and Codex as authors of their text, for PH1-PH23 (SA 12889-13424), ER1-ER14 (SA 6460-6720), the Landau pair and its covariance (SA 1a.3.6, 1a.3.10, SA 7700-7750) and the soft block axial factor (SA 7178-7186). T. Balaban for the soft gauge fixing (CMP 109 (0.14)-(0.19)) and for the standing assumption that every activity is invariant under all complex gauge maps (CMP 109 (1.19)). Codex for `ur-ya.md`, whose Sections 2, 4 and 5 are used below as checked.

## 1. Check of `ur-ya.md` (Codex), line by line

Verdicts. Each is an implication from the inputs that the note names.

| Item | Verdict | Remark |
|---|---|---|
| §2, ER8u from ER7 | ADVANCE | SA ER9 with ε_0 = C(c + c²)α_j and ε_1 = cα_j. ER7 then gives tower radius CK_T(c + c²)α_j < α_j/2 for small c. Conditional on ER7. |
| §2, (1) | ADVANCE | Circle radii a_j/(4‖v‖), a_j/(4‖w‖) keep ‖sv + tw‖_{1,j;X} ≤ a_j/2. Cauchy gives the factor 16‖v‖‖w‖/a_j². The norm is the one on X, as in SA ER14, because G(X,·,z) reads the pair on X only. |
| §2, (2) | ADVANCE | The weight costs e^{2mC_M(q+1)}; the two site sums cost C(q+1)^8; the rooted count costs C e^{κ_D q}. The series converges when 2mC_M < (κ − κ_D)/2. Only m < δ is needed for the site sums; m < δ/2 is harmless. |
| §2, "ER8u plus (R) proves UR" | ADVANCE | This is SA PH5a. DG(X,(1,0),z) = 0 by constant colour invariance (SA ER3), so (PH4) is the composite Hessian. |
| §3, counterexample (3)-(4) | ADVANCE (correct) | Checked below. (R) is false for the contour response, uniformly in j. |
| §3, "the checked inputs give only the block-constant subgroup" | ADVANCE, with a note | True of the sources that `b2-extract.md` §4 cites (`h-walk.md` test 2.1, `carrier-adopt.md` Lemma L(c), `a2-full.md` §10 item 5). But other notes already use full invariance: `wf-c.md` §§3-4 ("G̃ is gauge invariant ... in its Landau reading"), `wf7-bf.md` §2 ("Gauge invariance removes that gauge"), `d1-floor.md` 4b, `inn-fix.md` 4.4. The chain is inconsistent here. Section 3 below removes the inconsistency. |
| §4, (6) and (7) | ADVANCE | A_p(W) = 1 − ½ tr W = ½ det(W − 1) on SL(2,ℂ), so abs(A_p) ≤ C abs(W − 1)² ≤ Cα_j²η_j⁴. The tent quadrature η⁴ Σ_p h_z(p) = 1 per orientation is SA PH21 (rechecked in `b2-extract.md` Step 9). This is SA 13570-13577 ("its own tent action obeys abs(A(h_z, U)) ≤ Ca²"). |
| §4, unmultiplied tent kernel | ADVANCE | Each A_p is invariant under every bare gauge map, so its Hessian at 1 kills gradients. The plaquette curl d_η of a response is a combination of first difference quotients, bounded by (5). This is SA 13323-13345. |
| §4, "UR would imply (8)" | ADVANCE | Proved in Section 4 below, as (8). |
| §5, (9) | ADVANCE given (8) | 1 + T² ≤ 2T³ for T ≥ 1. The own tent is filed once, so it adds C g_j once, not per domain. |
| §5, young ages, (10) | ADVANCE given (8) | 1 + n ≤ 2^n; N exists because L ≥ 3 > √2; σ ≥ L^{−N} and ρ ≥ 1 for n < N. |

**The counterexample (3)-(4).** I redid it from `prefactor-loc.md` Sections 2-3.

1. The augmented branch is the saddle of Δ̃_j = d^*d + Σ_{r<j} Q_{0,r}^* τ_r^* τ_r Q_{0,r} under Q_{0,j}a = B. Lemma B (ii) gives Q_r J_r = 1 for the face-crossing insertion J_r.
2. Put v := J_1 ⋯ J_j B for B_1 ≡ T, B_μ ≡ 0 (μ ≠ 1). Then Q_{0,j}v = B. Also Q_{0,r}v = J_{r+1} ⋯ J_j B is a face-crossing field of level-j faces.
3. τ_r averages path sums along R3 contours from a node to a point of the same level-(r+1) cube. With L odd the cubes are nested, so such a contour never crosses a level-j face. Hence τ_r Q_{0,r} v = 0 for r < j.
4. On a plaquette in a (1,μ) plane, both 1-bonds lie at the same x_1, so both cross a face or neither does. Hence dv = 0.
5. So Δ̃_j v = 0, and (v, 0) solves the saddle system with datum B. Lemma B (vii) makes the polynomially bounded solution unique. So R_{0,j}B = v.
6. In the chart U_b = e^{iηA_b}, the physical response is η^{−1}v: abs = η^{−1} on crossing bonds. Its difference quotient across a crossing is η^{−2}.
7. If (R) held, Σ_x e^{−δ dist(x,X)} ≤ C would bound sup_X abs(H_jB) uniformly in j. Truncation of B and Lemma B's decay at fixed j make the sum legitimate.

The gauge function that converts the smooth response (η T on each 1-bond, as a link angle) into v is χ(x) = T n_1(x) − ηT x_1, with n_1(x) the block index in direction 1. It varies inside each final block. So it is not a block-constant direction, as the note says.

What this refutes. It refutes SA ER12 **for the representative fixed by (Id)**. SA writes ER2 for "its configuration-current pair in a fixed gauge near zero" and leaves the gauge open (SA 6487). With the Landau representative, ER12 holds by (5). So this is not a correction of SA's text (FINISH item 6 (3)). It does not refute UR, YA or (19).

**First failing step of `ur-ya.md`:** none. Its first failing input is correctly named: (R) for the contour response, and no Hessian gauge identity to transfer the Landau bound. Sections 2-4 below supply that identity.

## 2. The Hessian gauge identity

**Where the outline treats it (FINISH item 9).** SA PH2-PH3 (SA 12920-12928) *assume* that "every summand is local in its pair variables and invariant under all local gauge transformations for which the arguments remain in its declared domain". SA PH5 (SA 12955-12961) *assumes* the moment bound. SA PH5a (SA 12990-13014) derives it from a core ball, the response decay ER12 and entropy. SA *assumes* ER12 (SA 6672-6677) for "the response" of a pair "in a fixed gauge near zero" (SA ER2). The step from one representative's response to another's is not written. Classification: assumed. This section proves that step, given full gauge invariance. Section 3 supplies full gauge invariance for regular members.

**Setting.** Level j is fixed. η = L^{−j} is the bare spacing in level-j units. A pair is P = (e^{iηA}, J) in the chart of SA ER1, with v = (A, J) and ‖v‖_{1,j;X} = max over X of abs(A), abs(∇_jA), abs(J). For a bare site function χ put (∇χ)(b) = η^{−1}(χ(b_+) − χ(b_−)). A real bare gauge map g acts by P^g = (U^g, Ad(g)J), with the convention of SA PH8 and the current covariance of `inn-fix.md` §2 (ii).

**(FG) Full gauge invariance near the flat pair.** For each domain X and base point z there is a neighbourhood N_X of (1,0) in the real pairs on X such that G(X, P^g, z) = G(X, P, z) whenever P and P^g lie in N_X and g is a real bare gauge map.

**Lemma 1 (Hessian gauge identity).** Let G(X,·,z) be holomorphic near (1,0), read the pair on X only, be invariant under constant real gauge maps, and satisfy (FG). Then for every complex bare site function χ and every complex pair direction w,

  D²G(X,(1,0),z)[(∇χ, 0), w] = 0.        (2.1)

*Proof.* (i) Constant invariance gives DG(X,(1,0),z) = 0: on each local coordinate the derivative is an Ad-invariant linear form on su(2)^ℂ, and such a form is zero (SA ER3; `b2-extract.md` Step 1).
(ii) Let χ be real and finitely supported, and let w = (A_w, J_w) be real. Put P_s := (e^{isηA_w}, sJ_w) and g_t := e^{itχ}. For small real s, t both P_s and P_s^{g_t} lie in N_X, since χ has finite support. By (FG), φ(s,t) := G(X, P_s^{g_t}, z) does not depend on t. So ∂_s∂_tφ(0,0) = 0.
(iii) Let Ψ(s,t) be the chart coordinates of P_s^{g_t}. Then Ψ(0,0) = 0 and ∂_sΨ(0,0) = w. The gauge generator at the flat pair is ∂_tΨ(0,0) = (−∇χ, 0) (`a3-derivative.md` §6, Notation: X_χ(0) = −Dχ; the current part vanishes because J = 0 there). The chain rule gives
  0 = ∂_s∂_tφ(0,0) = D²G(X,(1,0),z)[(−∇χ, 0), w] + DG(X,(1,0),z)[∂_s∂_tΨ(0,0)].
The last term is the first-derivative term from the second-order gauge correction. It is zero by (i), for every j.
(iv) D²G(X,(1,0),z) is complex bilinear, because G is holomorphic. Real χ and real w span the complex ones, so (2.1) holds for complex finitely supported χ and complex w.
(v) Let χ be arbitrary. G(X,·,z) reads the pair on X only. So D²G(X,(1,0),z)[v, w] depends on v only through its values on the bonds of X. Choose χ' finitely supported with χ' = χ at every end point of a bond of X. Then (∇χ', 0) = (∇χ, 0) on X, and (iv) applies. ∎

**Lemma 2 (the two responses differ by a gradient).** Let P^c be the augmented contour branch fixed by (Id) (`b2-extract.md` §4), with response h^c = DP^c(0). Let P^L(B) := (e^{iηa(B)}, J(e^{iηa(B)})), where a(B) is the Landau potential of Theorem 3 in `a3-derivative.md`, with response h^L = DP^L(0). Then for each coarse bond x and colour,

  h^c δ_x = h^L δ_x + (∇χ_x, 0)        (2.2)

for a bare site function χ_x, real for real data.

*Proof.* At the flat reference U_0 = 1, the augmented branch meets the hypotheses of `a3-derivative.md` Lemma 6.3 (P81 as used there). It is holomorphic near 0, equals 1 at 0, and has averages e^{iB}. At real B it is critical for the Wilson action on the constraint set. Indeed, let U^ax be the tower axial representative of the critical orbit of S with datum e^{iB}; it exists by solving from the top down (SA 7185). Every contour variable of U^ax is 1, so each soft contour term 1 − ½ Re tr W has zero gradient there. So U^ax is critical for S̃ = S + Σ G_{r,r+1}∘M_{0,r} on the constraint set. The augmented branch is the locally unique critical point of S̃ near 1 (`prefactor-loc.md` §2, Lemma B). So the branch is U^ax, and it is critical for S. Proposition 6.4 of `a3-derivative.md` then gives P^c(B) = P^L(B)^{u_B} on the datum polydisc, with u_B holomorphic, real at real B, and u_0 = 1. The current is covariant, J(U^g) = Ad(g)J(U), and J(1) = 0; so the current part of the gauge factor has zero first derivative at B = 0. Differentiate at B = 0 along δ_x. The gauge factor contributes the generator −∇ of iχ := Du_B(0)δ_x in the potential slot and nothing in the current slot. The current slot of h^c δ_x − h^L δ_x is D_1^*D_1 of a gradient, which is zero. ∎

**Corollary 3 (the actual kernel is the Landau kernel).** Assume (FG) for G. Then for every X ∋ z and all coarse bonds x, y,

  D²G(X,(1,0),z)[h^c δ_x, h^c δ_y] = D²G(X,(1,0),z)[h^L δ_x, h^L δ_y].        (2.3)

So the actual kernel K_z of SA PH4 equals the kernel formed with the Landau response, domain by domain.

*Proof.* Insert (2.2) in both slots and expand bilinearly. Each of the three terms that contains a gradient vanishes by (2.1). ∎

*The lead's form of the identity.* For real B near 0, (FG) and P^c(B) = P^L(B)^{u_B} give G_z(P^c(B)) = G_z(P^L(B)). The identity theorem extends this to the datum polydisc. Differentiating twice, the second-order gauge correction enters only through DG_z(1,0)[D²(gauge)(0)], which is zero. So the "first-derivative term" is identically zero, uniformly in j. No bound on it is needed.

*What Section 2 does not show.* It does not prove (FG). Codex is right that the block-constant invariance in `b2-extract.md` §4 does not give (2.1): the gauge function of Section 1 varies inside blocks. Section 3 treats (FG).

## 3. (FG) for the regular members: the soft axial factor relative to the background

**Where (FG) stands.**
- *Outline:* assumed at PH2 (SA 12920-12925). Asserted at 1a.3.10 (SA 7748: "Every ingredient of a step is gauge covariant ... Consequently E^(k+1)(X,·) is invariant under (U,J) → (U^u, Ad(u)J) for G-valued u"), with the one-line reason at SA 7913 ("the objects are words in transports and logarithms, each typed at a site"). Used for the extension to complex orbits (SA 9654). Classification: sketched.
- *Balaban:* assumed at CMP 109 (1.19), for all G^c-valued maps, as "an easily verifiable statement for all explicitly defined terms".
- *Our chain:* `h-walk.md` test 2.1 and `a2-full.md` §10 item 5 show that G^(2)_V, written as the Hessian of the absolute GF_k(V) = Σ[1 − ½ Re tr V(y,x)] (SA 7182) at a general V, is covariant only under maps constant on blocks. So, as our notes write 𝖠 = C_V^T(G^(2)_V + Δ_k)C_V (SA 10204), a member is only block-constant invariant. Every other ingredient is covariant under the full group (`h-walk.md` §8; `a2-full.md` §10 item 5).

The defect is in the writing of one ingredient off the axial slice. The step never evaluates it there. The rule below writes that ingredient covariantly, and changes no value at the pairs the step uses.

**Rule (REL), adopted here for the regular step.** At the step from level k to k+1, let V^bg := M^k𝐔 be the averaged background of the pair 𝐔. Replace SA's soft block axial factor (SA 7178-7182) by

  𝔊^rel_k(V; V^bg) := Π_{y∈P''} Π_{x∈B(y)∖y} z_𝔊^{−1} 1{abs(W(y,x) − 1) < ε_k} e^{−x_k(1 − ½ Re tr W(y,x))},  W(y,x) := V(y,x) V^bg(y,x)^{−1},

with the same blocks P'', the same pairs (y,x) and the same z_𝔊. Here V(y,x) is the averaged contour variable (Federbush's mean, SA 7065). Accordingly, G^(2)_V in 𝖠 denotes the Hessian at A = 0 of A ↦ x_k Σ[1 − ½ Re tr((e^{iA}V)(y,x) V(y,x)^{−1})]. The cubic and higher gauge-fixing terms of the integrand are those of 𝔊^rel_k. The background map itself (the augmented branch, with its absolute contour terms) is not changed.

**Lemma 4.**
- (a) *Faddeev-Popov identity.* For fixed V^bg and u = 1 on T^(k+1), ∫Π_x du(x) 𝔊^rel_k(V^u; V^bg) = 1. Hence (Tρ_k)(V_{k+1}) = ∫dV δ(M(V)V_{k+1}^{−1}) 𝔊^rel_k(V; V^bg) ρ_k(V) for every V^bg that depends on V_{k+1} only.
- (b) *Agreement on the axial slice.* If V^bg(y,x) = 1 at every pair of the factor, then 𝔊^rel_k(·; V^bg) = 𝔊_k identically in V. So their quadratic parts and all higher terms agree.
- (c) *Covariance.* For every level-k gauge map g, 𝔊^rel_k(V^g; (V^bg)^g) = 𝔊^rel_k(V; V^bg). Hence G^(2)_{V^g} = Ad(g) G^(2)_V Ad(g)^{−1} for every g, and the gradient of the relative factor at A = 0 is zero at every V.
- (d) *The inputs that the operator notes read.* G^(2)_V is a finite analytic function of V on the contour stencil of one block, G^(2)_1 = τ^*τ, and ‖G^(2)_V‖ ≤ C_L near regular real V. These are `h-walk.md` (I3) and the norm input of `a2-full.md` Lemma 5.1.

*Proof.* (a) For u = 1 at the centre y, V^u(y,x) = V(y,x)u(x)^{−1} (SA 1a.3.3). In the Haar integral over u(x), substitute h = V(y,x)u(x)^{−1}V^bg(y,x)^{−1}; Haar measure is invariant on both sides. Each pair gives z_𝔊^{−1}∫dh 1{abs(h − 1) < ε_k}e^{−x_k(1 − ½ Re tr h)} = 1. Whether V(y,x) is defined does not change under u: the ratios of contour transports change by conjugation. The second claim is then SA's Faddeev-Popov step (SA 1a.3.3; CMP 109 (0.15)-(0.16)) with 𝔊^rel_k in place of 𝔊_k.
(b) W(y,x) = V(y,x) when V^bg(y,x) = 1.
(c) The mean is covariant: V^g(y,x) = g(y)V(y,x)g(x)^{−1} (`a3-derivative.md` Lemma 6.1, proof). So W ↦ g(y)Wg(y)^{−1}. The trace and the test abs(W − 1) are invariant under unitary conjugation. At A = 0, W = 1, and 1 − ½ Re tr e^{iX} has zero first derivative for traceless X.
(d) (e^{iA}V)(y,x) is an analytic function of A and V on the bonds of the contour family of B(y). The linear part of its logarithm relative to V(y,x) is the transported contour mean τ_V A, with τ_1 = τ. By (c), at real V, G^(2)_V is a conjugate of its value at the axial representative of V, where (b) gives SA's operator with ‖·‖ ≤ C_L (`a2-full.md` Lemma 5.1). Continuity covers nearby complex V. ∎

**Where (b) applies.** SA chooses P'' as "a family of blocks with no additional node, on which every background contour variable is 1" (SA 7875). The step's backgrounds are tower axial (SA 7185-7186). The holomorphic continuation keeps V(y,x) = 1 (`a2-full.md` Theorem I, proof). So under (REL) every integrand that the step forms at its own pair is the same as SA's. The effective action, every member value at those pairs, every composite G_z ∘ P^c and every kernel K_z are unchanged. So are the identities checked at the step's pair (`a2-full.md` Theorem I; `prefactor-loc.md` Theorem S; Theorem P of `b2-extract.md`).

**Proposition 5 ((FG) for regular members under (REL)).** Let G be a regular member of level k+1: no stored field (SA 5883-5888), formed by the small-field step as a product, trace or logarithm of walk, carrier and cluster terms. This is the scope of the (G) row of `b2-extract.md` §4. Under (REL):
- (i) G(X, 𝐏^g, z) = G(X, 𝐏, z) for every real bare gauge map g and every real pair 𝐏 of its domain with 𝐏^g in the domain. So (FG) holds.
- (ii) At every pair the step evaluates, G has the value it has under SA's factor.
- (iii) The operator bounds of `a2-layers.md` Theorems A-B, `a2-full.md` Theorems I-II and `h-walk.md` Theorem H hold at every real regular pair, not only at axial ones. They also hold at the complex pairs those notes cover.

*Proof.* Let g be a real bare map and g_k := g restricted to T^(k). Under 𝐏 ↦ 𝐏^g the fluctuation transforms by Ad(g_k), and dA is invariant. Take the ingredients one at a time.
1. M^k(𝐔^g) = (M^k𝐔)^{g_k}, by covariance of the averages ((I2) of `h-walk.md`).
2. The six propagators, Δ_k, C_V and E^(2) are covariant under every bare map (`h-walk.md` §8; `a2-full.md` §10 item 5).
3. G^(2)_V and the higher gauge-fixing terms are covariant, by Lemma 4 (c).
4. The Wilson action of the fluctuated background and the old members read 𝐔 through U_k(e^{iA}M^k𝐔). Now U_k(V^{g_k}) = U_k(V)^{g̃}, with g̃ the lift of g_k, constant on level-k blocks (SA 7185; `prefactor-loc.md` Lemma D (c)). The action is invariant. Old members are invariant under such lifts (the (G) row of `b2-extract.md` §4), and under every map by induction on the level with this proposition.
5. The pivot elimination is covariant (item 2). The Haar densities in exponential coordinates are invariant under conjugation, bond by bond.
So 𝖠(𝐏^g) = Ad(g_k)𝖠(𝐏)Ad(g_k)^{−1}, and the integrand at (𝐏^g, Ad(g_k)A) equals the integrand at (𝐏, A).
Every building block of the walk expansion is now covariant, including A^loc_κ = θ_κC_V^T(G^(2)_V − a)C_V. So the gauge clause of `h-walk.md` (H3) holds for the full group. `carrier-adopt.md` Lemma L(c) gives the same for the stored carrier series. A member is a product, trace or logarithm of covariant terms, so it is invariant. This is (i).
(ii) is Lemma 4 (b) with the paragraph before this proposition.
(iii) The operator notes read G^(2)_V only through Lemma 4 (d) and through Theorem I at axial pairs. With (i)'s covariance, 𝖠(𝐏^g) is conjugate to 𝖠(𝐏), and conjugation by a real map preserves the norms used. So the bounds move from the axial representative to every real regular pair. ∎

**What changes in other notes (for the lead to forward).**
- `h-walk.md` test 2.1 (defect D1) and (H3): the computation stays true for the absolute factor. Under (REL), the gauge clause holds for every gauge map, and SA's Haar mean (mechanism (i), SA 10560) is again available.
- `a2-full.md` §10 item 5: the axial hypothesis is no longer needed (Proposition 5 (iii)).
- `carrier-adopt.md` Lemma L(c), "what (c) does not give": now given for regular members.
- `b2-extract.md` §4, (G) and (Id): any representative on the orbit gives the same composite. (Id) need not change.
- `wf-c.md` §§3-4, `wf7-bf.md` §2, `d1-floor.md` 4b and `inn-fix.md` 4.4 use full invariance. For regular members, that input is now supplied.

**Scope and limits.** (REL) is a rule for the regular step only. The large-field moves keep SA's factor, which reads no background there (SA 17558). Proposition 5 does not cover members formed by the R stages: there the frames, trees and tests are not gauge invariant (SA 17585). (UR) and (YA) for regular members do not read them.

**Relation to the outline.** (REL) is the covariant writing of SA's factor that SA 1a.3.10 needs. It agrees with SA's factor at every background SA's step uses. So it is not a correction of SA's text (FINISH item 6 (3)): their statement fails only for a reading off the slice that they never evaluate.

## 4. (UR), the coefficient bound (8), and (YA) for the multiplied counterterm

**Theorem UR.** Fix j and one old regular member G of level j with norm g_j, on its torus or its infinite-lattice companion. Assume:
- (FG) for G. Under (REL) this is Proposition 5.
- (ER8u): for each domain X, the triples (1, A', J) with ‖(A', J)‖_{1,j;X} < a_j := cα_j lie in the core of G on X, with c > 0 independent of j (SA ER8; it reduces to ER7, `d1-floor.md` 4c-4d).
- (Cl): G(X,·,z) is holomorphic on the core and abs(G(X,P,z)) ≤ g_j e^{−κd_j(X)} there (SA OSF2).
- (5) for the Landau response, with C and δ independent of j (`flat-port.md` (9.9); `a3-derivative.md` (34), (39), on the whole datum polydisc, conditional on P81-P82 as those notes state).
- (En): #{X ∋ z : q ≤ d_j(X) < q + 1} ≤ C_D e^{κ_D q} with κ > κ_D, and diam_j X ≤ C_M(d_j(X) + 1).

Then, for 0 < m < δ with 2mC_M ≤ (κ − κ_D)/2,

  C_m(z) := Σ_{μ,ν,a,b} Σ_{x,y} e^{m(abs(x−z) + abs(y−z))} abs(K_z^{μν;ab}(x,y)) ≤ C g_j α_j^{−2},        (4.1)

with C independent of j, z and the torus. This is (UR) of Proposition W.

*Proof.* By Corollary 3, K_z(x,y) = Σ_{X∋z} D²G(X,(1,0),z)[h^Lδ_x, h^Lδ_y], domain by domain. The three entries of ‖h^Lδ_x‖_{1,j;X} are the three members of (5). Their stencils add a fixed collar to X, which changes only the constant. So ‖h^Lδ_x‖_{1,j;X} ≤ C' e^{−δ dist(x,X)}. This is (R) for the Landau response. Now `ur-ya.md` (1)-(2), checked in Section 1, apply verbatim. (ER8u) gives the ball of radius a_j. Two-variable Cauchy on the bidisc gives (1). The weighted site sums and the rooted count give (2). ∎

**Corollary 6 (the coefficient bound (8)).** Assume also (TI) for G, so that its prescribed coefficient is b_j = b[Ḡ], with Ḡ the average of `b2-extract.md` Lemma R (`ti-2.md` Corollary R14). Then

  abs(b_j) ≤ C g_j α_j^{−2}.        (8)

*Proof.* By Theorem P (d) of `b2-extract.md` at z = 0, b[Ḡ] = Σ_{x,y} K̄_0^{μν}(x̃,ỹ)(ỹ − x̃)_μ(ỹ − x̃)_ν, where K̄ is the colour-reduced kernel of Ḡ. For t ≥ 0, t²e^{−mt} ≤ (2/(em))², so abs((ỹ − x̃)_μ(ỹ − x̃)_ν) ≤ (abs(x̃) + abs(ỹ))² ≤ C_m e^{m(abs(x) + abs(y))}. Hence abs(b[Ḡ]) ≤ C_m C̄_m(0). The kernel of Ḡ at 0 is the average, over the finite group 𝔊_N, of transported kernels of G at the points g^{−1}0. This uses only the covariance of P_j under 𝔊_N (`b2-extract.md` §4, last paragraph), and isometries preserve distances. So C̄_m(0) ≤ max_z C_m(z), and (4.1) gives (8). ∎

**Corollary 7 ((YA), including the multiplied counterterm).** Under the hypotheses of Theorem UR and Corollary 6:
- (a) On the whole core of G, abs(b_j A_{j,z}(P)) ≤ C g_j. This follows from (7) and (8).
- (b) The own-counterterm member G̃ = G − b_j A_{j,z} also satisfies (UR). Its kernel is K_z − b_j K^A_z. The unmultiplied tent kernel has abs(K^A_z(x,y)) ≤ Ce^{−δ(abs(x−z) + abs(y−z))}, uniformly in j (`ur-ya.md` §4, checked in Section 1). With (8), its m-moment is at most C g_j α_j^{−2}.
- (c) The large-domain part and the young-age part of (YA) hold: `ur-ya.md` (9) and (10), checked in Section 1, with (6), (7) and now (8). They read the supplied age bound ρ² ≤ C_a(1 + n) (WF1) and the axial datum estimate abs(B)/r_{B,j} ≤ C_0ρL^{−n}, which are inputs of Proposition W already.

So Proposition W's (UR) and (YA) hold as implications. Their only input that is open on the critical path is (ER8u) = (ER7), already Proposition W's named first open input (`b2-extract.md` §7). Corollary 6 also reads (TI), which `ti-2.md` proves from (DOM) and (ID).

**On "choose the Landau representative in (Id)".** It is not needed. Under (FG), every representative on the orbit gives the same composite G_z ∘ P (Section 2). So (Id) stays the contour branch. This matters for the tests: they are not gauge invariant (`b2-extract.md` §6, last item; SA 17585), and they keep their contour reading. The Landau representative is used only inside the proof of Theorem UR.

## Result

**Check (Section 1).** `ur-ya.md` (Codex) was checked line by line by Claude. First failing step: none. Sections 2, 4 and 5 ADVANCE as implications from their named inputs. The counterexample (3)-(4) is correct. The contour response of a constant datum is the face-crossing field, of physical size η^{−1}. So (R) = SA ER12 is false for the representative fixed by (Id), uniformly in j. It holds for the Landau representative. This is not a correction of SA's text, because SA leaves the gauge of ER2 open. It refutes neither (UR), (YA) nor (19).

**Proved here by Claude, not yet checked by the other model:**
- **Lemma 1 (Hessian gauge identity).** Under full gauge invariance (FG), D²G(X,(1,0),z)[(∇χ,0), w] = 0 for every bare site function χ and every direction w. The first-derivative term from the second-order gauge correction is DG(1,0)[·] = 0 by colour invariance, so it vanishes identically, for every j.
- **Lemma 2 and Corollary 3.** The contour and Landau responses differ by a bare gradient (`a3-derivative.md` Proposition 6.4). So, under (FG), the actual kernel K_z equals the kernel formed with the Landau response, domain by domain.
- **Rule (REL), Lemma 4, Proposition 5.** Write the soft block axial factor relative to the averaged background: W(y,x) = V(y,x)V^bg(y,x)^{−1}. This is an exact Faddeev-Popov insertion. It equals SA's factor at every background the step uses, so no value that the step computes changes. It is covariant under every gauge map. With it, every ingredient of the regular step is covariant, and every regular member satisfies (FG). The operator bounds then hold at every real regular pair, not only at axial ones.
- **Theorem UR.** (FG), (ER8u), the class bound and the Landau bound (5) give C_m(z) ≤ C g_j α_j^{−2}, uniformly in j, z and the torus.
- **Corollaries 6-7.** With (TI): abs(b_j) ≤ C g_j α_j^{−2}, that is (8). Then abs(b_j A_{j,z}) ≤ C g_j on the whole core, G − b_jA_{j,z} satisfies (UR), and (YA) holds, by `ur-ya.md` (9)-(10).

**Kind of result (FINISH item 9).** The outline assumes (FG) (PH2) and sketches it (1a.3.10, SA 7913). It assumes ER12 and PH5 and derives PH5a. This note proves the transfer between representatives that the outline leaves unwritten (Lemma 1, Corollary 3), proves (FG) for the regular step in the covariant writing of SA's factor (Proposition 5), and proves PH5a with the Landau response (Theorem UR). It is not a correction of their text. It is not a candidate for an issue: SA 7913's "words in transports and logarithms, each typed at a site" admits the covariant writing.

**What stays open.**
- (ER8u) = (ER7), the uniform complex tower estimate. Theorem UR reads it. It is already the first open input of Proposition W and of D1's (P3).
- (5) is conditional on P81-P82, as `a3-derivative.md` states.
- Corollary 6 reads (TI) (`ti-2.md`, from (DOM) and (ID)).
- Proposition 5 (iii) was checked against the inputs that the operator notes state ((I3) of `h-walk.md`, `a2-full.md` Lemma 5.1, `a2-layers.md` 7.6). Their proofs were not reread.
- (FG) for members formed by the R stages is not treated. (UR) and (YA) for regular members do not read it.
- For (19), Proposition W still reads (20), (ER8u) and (BX) (`bx-fix.md`, check pending in row 220).

**Moves.** (UR) and (YA) of Proposition W become implications from (ER8u), so B4's (19) reads (ER7), (BX) and (20), and nothing new. (REL) also supplies the full invariance that `wf-c.md`, `wf7-bf.md`, `d1-floor.md` and `inn-fix.md` already use, and it lifts the block-constant restriction of `h-walk.md` test 2.1 and `carrier-adopt.md` Lemma L(c). Codex should check Sections 2-4 and the adoption of (REL).
