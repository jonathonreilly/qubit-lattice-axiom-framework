# bx-fix-check (row 220)
Provenance: OpenAI Codex, GPT-6 family (exact deployment and runtime effort not exposed; queue effort xhigh); checkout `1face7c7e66a2d2af9ca25d078043eab93db804a`; Sussman–Alpoge commit `31a47c543775`; research check, not an audit; no status granted.

Credit: Ethan Sussman and Levent Alpoge, with Claude and Codex as the authors of their text. Their pinned outline supplies the core, pointed-window argument and background statements examined below. Tadeusz Balaban supplies the cited Hölder method. Claude wrote `library/bx-fix.md`; Codex wrote `library/bx.md`.

This checks B4's input (BX), by hand. Verdicts remain implications from the named premises. Sections are saved as they are checked.

## 1. Clause (H) and Lemmas 0–3

Checked line by line by Codex:

| Statement | Verdict | First failing step |
|---|---|---|
| Section 2.2, definition (H) | ADVANCE | None. It adds two spatial seminorm bounds; openness is on the fixed-real-factor slices. |
| Section 2.3, exclusion of `bx.md`'s input | ADVANCE | None, with the running-radius comparison used there. |
| Lemma 0 | ADVANCE | None, conditional on [PW-H], [PW], [NL] and the stated smooth cutoff. |
| Lemma 1 | ADVANCE | None, conditional on the stated straightened [AV] package. |
| Lemma 2 | ADVANCE | None for its displayed bound (4.1), with radius `a_*`. |
| Lemma 3 | ADVANCE | None. The window restriction permits absorption of the commutator term into the sharper remainder. |

For the exclusion, take the two plaquettes a distance `σ` apart where their logarithmic curvatures are opposite. A potential of size `b_0` permits only `O(σ b_0)` relative transport. Thus
\[
2\sigma^{\alpha_H}[\nabla w]_{\alpha_H}
\ge 2c'_L\varepsilon a(1-C\sigma b_0)-Cb_0^2.
\]
Under (H), BCH gives `b_0 = O(Mα_0+α_1)` and a seminorm of that same order. With the stated running radii, `b_0²=o(a)`; the required `aσ^{-α_H}` exceeds the allowed seminorm. This also rules out a different admissible splitting. The matrix-product, translation-difference and axial-product estimates in Lemmas 0–3 introduce no mesh-dependent constant.

## 2. Affine reconstruction and Theorem BX′

| Statement | Verdict | First failing step |
|---|---|---|
| Lemma 4(a) | ADVANCE | None. Both centered contour sums vanish on an affine field, including at each preceding averaging level. |
| Lemma 4(b) | WRONG as proved | Its first sentence identifies the Landau derivative with a solution of the **plain** constraint `K_T a=B`. |
| Lemma 4(c) | WRONG as proved | Its use of (b). The Ward cancellation itself is correct when `DG_X(0)=0`. |
| Lemma 4′ | WRONG as proved | The first restriction identity substitutes the Landau map for the prescribed critical representative. |
| BX′-1, top-row datum estimate | ADVANCE | None, from Lemmas 2–3. |
| Theorem BX′, complete package | WRONG as proved | BX′-2 imports Lemma 4(b); BX′-3 imports Lemmas 4(c), 4′. BX′-4 has the separate failure below. |

**1. The node factor was dropped.** SA 9627–9644, 9693–9717 and `a3-derivative.md` (35), (37) distinguish these maps. They give
\[
\Phi(B)=(e^{i\eta\mathcal H(B)})^{u_B},\qquad
\mathcal Q^{\rm st}(\mathcal H(B))=\mathsf b(B),\qquad
u_Bv[\mathcal H(B)]=1\quad\text{at nodes}.
\]
Write `n(a)` for the linear node factor and `δ_node n(c)=n(c_-)-n(c_+)`. The exact linear identity is
\[
K^{\rm plain}a=K^{\rm red}a+\delta_{\rm node}n(a),\qquad
K^{\rm plain}H_TB=B+\delta_{\rm node}n(H_TB).
\]
The proof has not made the last term zero. Landau gauge fixes averages of the gauge parameter, not its values at nodes. Thus its asserted solution set with `χ=0` at nodes does not follow. Lemma 4′ repeats the identification and then uses the resulting top-row equality. The boundary multiplier construction for the bare affine field is sound. A repair must retain `u_B`, or verify the affine field directly in the reduced Landau system. This report does not claim the affine Hessian identity is false.

**2. BX′-4's chart path is not admitted by a condition number.** Its last sentence infers a bond-log ball from `|v||v^{-1}|≤exp(CMα_1)`. Even a unitary node field has condition number one while `v(c_-)v(c_+)^{-1}` can be arbitrarily far from one. This is the term created when the zero datum is gauged. The specified composite gauge needs bounds on those adjacent-node ratios along its path, or another common-chart argument. Gauge invariance and the identity theorem require an admitted domain first.

There is also a radius reversal in Section 7: `α_k≤C_αα_{0,k}` and `α_1≤C′Mα_0` do not imply `a_out≤C_Mα_k`. That conclusion needs `α_{0,k+1}≤Cα_k` as well. Lemma 2's estimate with its stated `a_*` remains valid.

## 3. Preservation and the Hölder response

| Statement | Verdict | First failing step |
|---|---|---|
| Lemma 5 | ADVANCE | None, conditional on [T4]. Integrate its Hölder response and sum its decaying columns. |
| (A2-H) | ADVANCE | None, with the stated enlarged constant in `o1-decoupled.md` 4.5 and WF-c's original admission premises. |
| (ER8u)-H, membership of the image `P_in(B)` | ADVANCE | None, conditional on original core admission and Lemma 5. |
| (ER8u)-H as the replacement for Proposition W's Taylor ball | WRONG | The sentence “So the Taylor expansion … stays … on the whole ball” changes a datum-image inclusion into a pair-chart inclusion. |
| Rule (C), its added Hölder clause | ADVANCE | None for inner Landau triples with the stated margin; the original hereditary admission remains required. |
| Proposition I | WRONG | Item 1: not every member evaluation in the cited step is an inner Landau triple. Item 2 also depends on BX′. |
| Lemma M | ADVANCE | None. The mesh-uniform exponent is exactly `1−4/8=1/2`. |
| Proposition PH | ADVANCE | None, conditional on all four inputs of `pw-bridge.md` and their fixed choices. |

**3. Image admission does not supply the member's Taylor ball.** Proposition W, steps 1 and 4, and SA (PW16), use Cauchy estimates for `G_X` in its potential/current chart. The estimate concerns the small **local pair** of size `a_outσ²`, not merely a datum of global size `a_outσ`. A critical-map image is not an open ball in that pair space. Nor can an original first-order ball lie in (H): on mesh `η`, the field
\[
A_2(x)=r\eta\cos(\pi x_1/\eta)T,\qquad A_1=A_3=A_4=0
\]
has first-order norm `O(r)` and gradient Hölder seminorm at least `4rη^{-α_H}`. Shrinking `r` by a fixed constant does not fix this. A valid repair is the **augmented** pair ball: original (ER8u) admits its first-order part, and `r≤α_1` admits its Hölder part in gauge one. The subsequent Taylor bounds must use that augmented norm. This is not the image-ball argument written in (ER8u)-H.

**4. The induction omits outer evaluations.** `wf7-bf.md` Section 3, “Long members”, explicitly keeps their original outer presentation and its admitted member-core displacement bound. Lemma 5 and (A2-H) prove admission of inner triples only. Rule (C) is also stated for two inner Landau triples. An (H) estimate for these outer substitutions is still needed. The separate admission that large-field consumers were not checked cannot establish the unrestricted induction either.

For Lemma M, the near and far sums both equal at most `Cs^{4/7}` before the `7/8` power. The kernel-difference norm is therefore `Cs^{1/2}`. In PH, `pw-bridge.md` (5.2), (6.1)–(6.2) and the composed-source argument retain `W^{2,8}` control of the potential. Applying Lemma M to its first differences preserves the column decay. Bounded connection coefficients and their first differences control the covariant correction. For `s≤m`, `(s/m)^{1/2}≤(s/m)^{α_H}` precisely when `α_H≤1/2`. The existing column sums then give `[PW-H]` with `B=Ce^{16κ̄}`. No additional Hölder premise is needed **for PH**; this does not repair BX′ or Proposition I.

## 4. Does the outline already exclude the input?

**No: its specified core does not exclude `bx.md`'s input by a Hölder condition or a physical-current condition. But (PW6) is an explicit additional input to the window deduction. The example fails that input. It does not refute conditional WF15.**

Source: [Sussman–Alpoge outline at `31a47c543775`](https://github.com/ethanwsussman/Yang--Mills-LLM-experiment/blob/31a47c543775/YM4_sketch_500.tex). The following references use its source lines. Short quotations and the defining formulas identify the decisive passages.

**Core definitions.** SA 5665–5733 defines the core as “triples satisfying (R4)--(R6)”. Its simple clauses are
\[
|\partial U-1|,|\partial\mathbf U-1|<a_0\eta_j^2,
\quad |A'|,|\nabla_UA'|<a_1,\quad|\mathbf J|<a_2,
\quad |A|,|\nabla A|<C_{\rm pot}Ma_0.
\]
The tower clauses require continuation and bounds on the reconstructed `U_n(Z;P)` and its current. They impose neither a seminorm on `∇A′` nor `J(𝐔)=𝐉`. SA 9646–9654 repeats that definition. SA 7151–7176 distinguishes physical regularity from these pair domains; its real-centre requirement ends “but not a small current”. SA 5758–5762 explicitly warns that replacing the independent current by the field's current changes the construction.

The other defining passages agree: SA 4863–4880 (independent-current pair space), 6120–6158 (layer radii and hereditary layered space), 6559–6635 ((ER7)–(ER8), a **first-order** near-zero ball), 7292–7300 (separate complex-curvature bound), 9746–9774 (tower and substitution conclusions), and 32686–32691 (domain glossary). None adds the proposed (H). These passages were read in bounded excerpts, including their full defining clauses.

In particular, Theorem 5(c), SA 9758–9772, forms its inner datum from the scale-`k+1` **box background** `H_{k+1}`. This produces a different evaluation field; it does not exclude the raw pair from the core. The calculation in `bx.md` does not test that preliminary replacement.

**A1–A3's regularity conclusions.** SA 3811–3897 states obligations for critical orbits, constrained coercivity, and inverse/response kernels. Their detailed conclusions are SA 9616–9623 and 9660–9744, Theorems 1–4. Physical regularity includes the actual-current bound `|J(U)|<ε L(b)^{-3}`. Theorem 2 then supplies
\[
|\nabla A(x)-\nabla A(x')|
\le Cm\varepsilon\xi_j^{-2-\alpha_H}|x-x'|^{\alpha_H}.
\]
Theorem 3 concerns `Φ(B)` and its Landau pair. Theorem 4 supplies Hölder estimates for their **response**, also for the response at noncritical independent-current pairs. It does not assert that the input field itself has those estimates. A2's coercivity bound concerns a constrained Hessian, not an input-field seminorm. Thus neither criticality nor the physical-current bound can be imposed on `bx.md`'s complete input through these conclusions.

The outline does prove a scalar Hölder implication in (BGH20), SA 12637–12725. Its applications (BGH24)–(BGH30), SA 12753–12882, require potential and Laplacian readouts, or the retained Hölder operator norm for decoupled responses. They do not strengthen (R4). SA 12220–12224 also explains that Cauchy estimates preserve an existing spatial seminorm. These are regularity results for their stated outputs, not a further core-membership test.

**PW6 and WF15.** SA 13558–13575 asserts the complete-field estimate
\[
|B|\le Ca_{\rm out}\sigma,\quad
|\nabla B|\le Ca_{\rm out}\sigma^2,\quad
|\nabla B(x)-\nabla B(x')|
\le Ca_{\rm out}\sigma^{2+\alpha}|x-x'|^\alpha,
\]
and calls these “not consequences of holomorphy alone”. It attributes them to A1–A3; this passage does not derive them for every raw (R4)–(R6) input. SA 3955–3959 separately requires spatial regularity for the nonlinear remainder. SA 15750–15845 specifies the actual nonlinear datum, reconstructed box pair, domain room and complete-field regularity. Reconstructing at old scale `j` cannot alter that prescribed datum or create its missing scale-`k` bound.

WF15 is introduced at SA 16316–16329 with “Under the explicit background” and concludes “on every specified complex core”. Its qualification retains the window and geometry inputs, including PW6; SA 16350–16355 reiterates them. The further near-class statement at SA 16646–16658 explicitly restricts its complete field, but does not redefine (R4)–(R6). Hence the defensible finding is a failure of the **core-to-PW6 inference** on arbitrary inputs, not a counterexample to the outline's conditional theorem. With zero fluctuation, `bx.md`'s window derivative is zero anyway.

## Result

The new Hölder estimates, including PH, pass as named implications. The complete BX′ repair and its preservation claim do not: the representative, chart-path and consumer-domain steps above remain unresolved. This is a check of our research text and a comparison with the outline, not a new status claim or a proposed public correction.
