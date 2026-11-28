# ur-gauge-check
Provenance: Codex (GPT-6 family; requested effort xhigh; runtime variant and effort not exposed); checkout `6d367c519f0d145221b3786676c6c50a7354169f`; Sussman–Alpoge `31a47c543775`. Research text, not an audit; no status granted.

Queue row 223. This checks Claude's `library/ur-gauge.md`, §§2–4, by hand.
Credit Ethan Sussman and Levent Alpoge, with Claude and Codex as authors of their text, for the SA formulas below.
SA line numbers refer to `YM4_sketch_500.tex`, fetched once to `/tmp/sa_ym4.tex`.
The question is whether (UR) and (YA) lose the missing gauge-invariance input in B4's (19).

## 1. Section 2: Hessians and representatives

Checked line by line by Codex, first failing step none, with the stated background inputs retained.

| Statement | Verdict | Hand check |
|---|---|---|
| Lemma 1 | ADVANCE | Constant colour invariance gives `DG(1,0)=0` on each adjoint coordinate. Differentiating `G(P_s^{g_t})` gives `D²G[w,−∇χ]+DG[∂s∂tΨ]=0`. The second term vanishes. Complex bilinearity and restriction to the endpoints in X give the stated scope. |
| Lemma 2 | CORRECT-NO-ADVANCE | Given P81–P82, select the critical orbit's tower axial representative. Every added contour action has zero gradient there. Fixed-depth saddle invertibility identifies the augmented branch locally. `a3-derivative.md` Proposition 6.4 supplies its Landau pair. Differentiation adds only `(∇χ,0)`, since `J(1)=0`. No uniform bound on χ is needed. |
| Corollary 3 | ADVANCE, conditional on (FG) | Expand both Hessian slots using Lemma 2. Lemma 1 kills all three gradient terms. The composite's second-derivative correction also vanishes because `DG(1,0)=0`. |

This does not prove (FG). The face-crossing example in `ur-ya.md` §§2–3 still rules out uniform physical response bounds for the contour representative itself.

## 2. Section 3: (REL) and the regular members

Checked line by line by Codex; WRONG first at (REL)'s operator definition.

| Statement | Verdict | First failing step |
|---|---|---|
| (REL), relative factor | CORRECT-NO-ADVANCE | None on real fields. It is a normalized covariant insertion, and equals the absolute factor when every background contour is 1. |
| (REL), its operator definition and claim that no computed value changes | WRONG | The sentence beginning “Accordingly” inserts an extra `x_k` into the unscaled Hessian. Even after fixing that, equality on the axial slice does not identify the general-core operators. See D1–D2. |
| Lemma 4(a–c) | ADVANCE for the relative construction | None on the real insertion domain. Haar translation proves (a); substitution proves (b); `W^g=g(y)Wg(y)^{-1}` proves (c). This does not assert a Haar identity at complex backgrounds. |
| Lemma 4(d) | WRONG as written | `G^(2)_1=τ*τ` contradicts (REL)'s weighted, unscaled definition; D1. The finite-stencil analyticity and bound hold for the correctly normalized relative operator. |
| Proposition 5(i) | CORRECT-NO-ADVANCE for newly defined relative members | Its covariance argument works given the named covariant ingredients and induction on old members. It does not prove (FG) for the original absolute-factor members. |
| Proposition 5(ii) | WRONG | Its appeal to Lemma 4(b) requires axial backgrounds. The core evaluations in D2 do not satisfy that condition. |
| Proposition 5(iii) | WRONG as written | D1 already changes the operator at the flat pair. After correcting it, real covariance transfers axial bounds for the new relative operator; equality does not transfer the old complex-core formulas. Those require the corresponding relative-operator estimates. |

**D1. Wrong Hessian normalization.** At `V=1`, write the unweighted contour action as
`GF(e^{itA})=t²‖τA‖²/2+O(t³)` (SA CF2–CF3, 8438–8449).
The Hessian defined in (REL) is therefore `x_k τ*τ`, not `τ*τ`.
SA 7878 instead uses `x_k GF(e^{ig_kB}V^bg)`, with `x_k g_k²=1`.
Thus (REL)'s operator is not SA 10204's operator even at the flat background.
The exact repair is to omit `x_k` in the Hessian definition, or replace `e^{iA}` there by `e^{ig_kA}`.
This repairs the normalization only.

**D2. Axial agreement does not cover the core reads.** This persists after D1's repair.
It suffices to take k=0. Take one node-free block, centre y, and a non-centre site x.
Set `T=diag(1,−1)`, `g(x)=e^{iεT}`, and `g=1` elsewhere, with ε nonzero and arbitrarily small.
The background `V^bg=1^g` is real and flat; its current is zero.
It is an allowed core pair: gauge it to 1, and every tower has zero curvature and current.
Every path mean from y to x equals `e^{−iεT}`.
Vary only this gauge value to `e^{i(ε−t)T}`. The coarse datum stays 1, and the varied contour is `e^{i(t−ε)T}`.
For this one summand the absolute and relative actions are exactly

`f_abs(t)=1−cos(t−ε)`, `f_rel(t)=1−cos t`.

Choose ε and t small enough that both indicators equal 1.
At `t=0` the values differ, and the quadratic forms on this fibre direction are `cos ε` and `1`.
All other contour summands remain zero. This is a hand counterexample, with no seam or large field.
SA explicitly reads the general-core operator at `V=M^k U` (10200–10204; 14095–14101).
The localized activities also read general core pairs (14680–14683; 14895–14899; 15366–15372).
Hence the assertion that the step never evaluates the ingredient off the axial slice is false.

The physical node-free integral, its axial datum continuation, and `G∘P^c` can still be preserved by a corrected relative construction.
That is a narrower claim. It does not identify the old off-slice functions or their class bounds with the new ones.
SA 7754 allows an invariant extension from a slice; adopting and bounding that extension is not equality of the absolute and relative local rules.

## 3. Section 4: the conditional estimates

Checked line by line by Codex, first failing step none in these implications.

| Statement | Verdict | Hand check |
|---|---|---|
| Theorem UR | ADVANCE, conditional on (FG), (ER8u), (Cl), (5), (En) | Corollary 3 permits the Landau response. Cauchy gives `C g_j α_j⁻² e^{−κd(X)}e^{−δ(dist(x,X)+dist(y,X))}`. The two coarse bond sums cost `(q+1)^8`; entropy leaves a strictly positive exponential rate. No bare-coordinate count enters. |
| Corollary 6 | ADVANCE, also conditional on (TI) and the prescribed extractor | The second displacement weight is bounded by `C_m e^{m(abs(x)+abs(y))}`. The finite isometry average has moment at most `sup_z C_m(z)`. Thus `abs(b_j)≤C g_j α_j⁻²`. |
| Corollary 7(a–c) | ADVANCE under those hypotheses and the stated age/datum inputs | Multiply `abs(A_{j,z})≤Cα_j²` by Corollary 6. The tent Hessian kills fine gradients and has a uniform Landau moment. For large domains use `1+T²≤2T³`; for young ages use `1+n≤2^n` and `L>√2`. File the own tent once. |
| “Their only input that is open … is (ER8u)” | WRONG | Section 3 has not identified the unchanged regular family with a fully invariant family having the same core bound. The conditional estimates do not discharge that input. |

No counterexample to (UR), (YA), or (19) is asserted.

## 4. SA's factor and its readers

SA 7181–7182 defines the **absolute** factor:
\[
\mathfrak G_k(V;P'')=
\prod_{y\in P''}\prod_{x\in B(y)\setminus y}
 z_{\mathfrak G}^{-1}\mathbf1\{|V(y,x)-\mathbf1|<\varepsilon_k\}
 e^{-x_k(1-\frac12\operatorname{Re}\operatorname{tr}V(y,x))},
\qquad
\mathrm{GF}_k(V)=\sum_{y,x}[1-\tfrac12\operatorname{Re}\operatorname{tr}V(y,x)].
\]
Undefined means receive no factor (7178, 7666, 17346).
Since contour means are invertible, `V(y,x)(V^bg(y,x))⁻¹=V(y,x)` exactly when `V^bg(y,x)=1`.
This holds for the physical node-free axial background and its datum continuation, not for every core pair.
The following short quotations identify the direct reads and their scope. Repeated reads are grouped.
The equality column concerns the factor; D1 separately concerns its incorrectly normalized Hessian.

| SA lines / reader | Quoted formula or identifying excerpt | Does (REL) preserve this read? |
|---|---|---|
| 7065, 7185: mean and selected background | `U(y,x):=\operatorname{av}(U(\Gamma))`; `\operatorname{Ax}(\Omega_\bullet,U_0)` | Yes when the reference contours are 1. A relative tower condition alone does not make an arbitrary reference axial. |
| 7129, 7142–7147, 7569, 7595–7598: transformation and regular action | `\mathfrak{G}_k(V)`; `\mathbf{T}^{\mathrm{sf}}_k[\mathsf{t}]` | Yes at the selected node-free axial background, for every integration field V. |
| 7357–7370: one-step rigidity | `\alpha_1+C\varpi+2\delta` | The soft contour defect is unchanged on those blocks. |
| 7493–7496, 7820: normalization | `z_{\mathfrak{G}}=\mathfrak{z}(x_k,\varepsilon_k)`; `-(L^4-1)\log z_{\mathfrak{G}}` | Yes; real Haar translation preserves the normalizer. |
| 7604, 7866: quadratic expansion | `x_k\big[A(U_k(V_k))+\mathrm{GF}_k(V_k)\big]` | Yes for the stated node-free interior. The seam terms are retained separately. |
| 7666–7673, 7875, 7881: insertion and product | `\int\prod_xdu(x)\,\mathfrak{G}_k(V^u;P'')=1`; `\mathfrak{G}_k(V^v)=\mathfrak{G}_k(V)` | The first identity is exact. The second is stated only for block-constant v. An insertion identity does not identify off-slice integrands. |
| 7755–7761, 7765–7771: seam reads | `\mathrm{GF}_i(\mathcal{M}^iU;P'')`; `\Phi=f_{\mathfrak{G}}\big(V^+(c)\,\mathsf{p}^{-1}V(s)^{-1}\big)` | Not generally equal after a relative replacement. (REL) excludes these factors, so this is not the counterexample used here. |
| 7873, 17317, 17346, 17369: tests and totality | `\mathfrak{G}_k`; `\chi'_k`; `\chi^{(k)}` | The indicators agree wherever the chosen background contours are 1. Undefined-factor conventions must also be retained. |
| 7875–7881: the axial Gaussian gauge form | `x_k\,\mathrm{GF}_k(e^{ig_kB}V^{\mathrm{bg}}_k;P^{\prime\prime})`; “every background contour variable is” `\mathbf1` | Yes on the specified blocks. The factor `g_k` in the argument is essential; D1. |
| 8438–8449 (CF2–CF3), 9468–9475 (FX27): flat precision | `\mathrm{GF}(e^{ita})=\tfrac12t^2\|Ga\|^2+O(t^3)`; `G^{\mathsf T}G` | Yes at the flat reference, with the correct scaling. |
| 10200–10208: general operator and physical identification | `V=\mathcal M^k\mathbf U`; `\mathsf A=\mathsf C_V^{\mathsf T}(\mathsf G^{(2)}_V+\Delta_k)\mathsf C_V` | No at general core pairs; D2. Yes at the specified axial physical pair. |
| 11229–11247 (PX104): next-fibre Hessian | `D\mapsto\mathrm{GF}(e^{iD}V)`; `\widehat J+\widehat J_{\rm GF}` | No at an arbitrary reference. SA explicitly distinguishes absolute and relative derivatives there. |
| 11800–11805 (after BGR6): matching requirement | “different blocks away from that field” | SA already states the limitation used in D2. |
| 14093–14138: regular Gaussian comparison | `\mathrm{GF}^{(2)}_V+\Delta_k(P)`; `\mathsf A(P)` | No for arbitrary regular complex P. The physical identification is narrower. |
| 14680–14683, 14895–14899, 15366–15372: local activities | “At a fixed core pair”; `E_X(\mathbf V)` | These read the local Gaussian rules on independent-current cores, not just the physical axial graph. D2 applies to their input operator. |
| 14843–14875 (SI1–SI2): complete regular integral | `\Xi(P,z)`; `{\cal N}[\theta;x](P)+\log\Xi(P,z)` | Yes on the specified physical graph, after correcting D1. This is not an equality on all cores. |
| 15465, 15561–15563: intrinsic gauge remainder | `V^{G,A}`; `t^{-2}V^{G,A}(tB)` | Its Taylor coefficients agree on axial backgrounds only. The general-core gauge rule changes. |
| 7133–7136, 17531, 17558: carried operations | `\zeta(\Omega^c_{k+1})`; `\mathfrak{G}_j`; “depend on no background” | These absolute factors are retained by (REL)'s scope restriction. They cannot be replaced using a later background. |
| 17257, 17676, 17709–17715, 18290–18297: failed-test payments | `\sum_{j=m_\flat}^{m-1}x_j\mathrm{GF}_j(X;V_j)`; `\mathrm{GF}_{t-1}(\mathfrak c^\sim;V_{t-1})` | These read the original kept factors. (REL) leaves the large-field operations unchanged. |
| 18735–18749: gauge normalizer bound | `z(\theta,\epsilon)`; `c\theta^{-3/2}\le z(\theta,\epsilon)\le C\theta^{-3/2}` | Yes for the real insertion, with the same frame and threshold. |
| 19410, 20250–20254, 20530–20564 (RF14–RF15): frame and Gaussian coefficient | `S(B)=\mathcal S_k(e^{iB})+\mathrm{GF}_k(e^{iB})`; `\tau\Delta_A+\Delta_{\rm GF}` | The frame fixes the gauge weight and scaling. At an axial reference the correctly scaled relative term agrees. D1 does not. |
| 22576, 22750–22756: mass and history identities | `\int du\,\mathfrak G(V^u)\,\mathbf 1_{\mathcal B}(V^u)` | A normalized draw preserves mass. Its product formula also needs invariance under the group of that move. Neither fact proves pointwise equality. |
| 26307–26334: tame-step insertion | `e^{-x_{j-1}[A(U_{j-1}(V))+\mathrm{GF}_{j-1}(V)]}` | Yes at its selected axial background; this also preserves its higher fluctuation terms. |
| 27775–27790, 27829–27840, 27893–27903 (GCB36–GCB40) | `\mathcal T^{\mathsf T}\mathcal T`; `\theta g^2=1` | Yes at the flat reference. The gauge coefficient after scaling is one. |
| 31908–31923 (CP1): assigned vacuum number | `\mathsf e_k=\mathfrak n_k+`; `\mathbf N^\circ` | The explicit gauge count is unchanged. Equality of the Gaussian numbers also requires the correctly matched operator. |

SA's gauge-invariance claim is sketched at 7748–7754 and 7913; PH2 assumes it at 12920–12928.
PH5a derives the moment bound at 12990–13016 from its named core, response, and entropy inputs.
The check confirms the conditional transfer and estimates. It rejects the unchanged-object claim in §3.
An admissible repair must specify a correctly normalized invariant extension, prove its core bound, and identify its physical composite with the old one.
No change to (19)'s input list follows from the text as written.
