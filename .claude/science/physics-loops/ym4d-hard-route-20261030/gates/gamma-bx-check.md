# gamma-bx-check
Provenance: Codex (GPT-6 family; requested effort xhigh; exact runtime model and effort not exposed); checkout `497241b0d6870e05bf812bb5853948a14550ea87`; Sussman–Alpoge `31a47c543775`. Research text, not an audit; no status granted.

Queue row 234. Hand check of Claude's `library/gamma-bx.md`.
Credit Ethan Sussman and Levent Alpoge, with Claude and Codex as authors of their text, for the cited outline constructions.
SA references name source lines of `YM4_sketch_500.tex`, fetched once to `/tmp/sa_ym4.tex`.
The question is whether (Γ), (BX), and regional prescription (10) follow.

## 1. Relative factor and core bound

Checked line by line by Codex:

| Statement | Verdict | First failing step |
|---|---|---|
| Rule (REL′) | ADVANCE | None for the new regular-step prescription. `x_k g_k²=1` gives the unweighted D-Hessian. |
| Lemma 1 | WRONG as stated | (c) extends the cutoff's covariance to complex gauge maps. The trace identities remain valid. |
| Lemma 2 | ADVANCE, conditional on its named operator inputs | None for the relative regular precision. Only unitary gauge transfer and the holomorphic trace identities are needed. |

**Cutoff defect.** Put `R=exp(itσ₁)` and `h=diag(e^s,e^{-s})`, with `s>0` arbitrarily small.
Indeed `‖h(R−1)h⁻¹e₂‖²=(cos t−1)²+e^{4s}sin²t>‖R−1‖²`.
Choose `t` so the two norms straddle `ε_k`.
The indicators differ although both means exist; SA 7773 explicitly allows this norm growth.
Restrict cutoff covariance to real maps. Complex covariance survives for the holomorphic trace and its derivatives.
Also, Lemma 1(e)'s cubic bound is per contour summand. The displayed total needs a sum over stencils.
Repeating a nonzero flat commuting fluctuation on disjoint blocks rules out a volume-independent bound by one supremum.
The local derivative and operator bounds used in Lemma 2 survive both corrections.

Lemma 2's unitary block gauge preserves regularity and commutes with regional masks.
At the axial real centre, the two corrections cost at most `c_L/8` from Theorem II's `3c_L/4`.
The local walk term changes; the remaining terms do not. These are bounds for the **new** operator.
SA 7178–7185, 7666–7673, 7773, 7875–7881 and 10200–10208 supply the corresponding definitions.

## 2. Invariance and identification

| Statement | Verdict | First failing step |
|---|---|---|
| Proposition 3 | WRONG for the complete regular family | Proof: “lower members are invariant by induction”. Incoming healed R-terms are not covered by that induction. |
| Proposition 4 | CORRECT-NO-ADVANCE as a conditional identification | None assuming (c) and full covariance. The claimed unconditional identification first lacks the lower-read equality used in (b)–(c). |
| Theorem Γ | WRONG for the stated class | (i) imports Proposition 3; (ii) consequently lacks (FG) for every old regular member. |

SA 7754 prescribes an invariant extension, but factor agreement alone does not identify whole recursive members.
Proposition 4(c) assumes that **all** lower reads stay on their slices.
SA 7185 supplies this for selected critical representatives, not the independent-current rules at 14680–14683, 14895–14899 and 15366–15372.
Thus (b)'s whole-integrand assertion also needs (c). Given (c) and covariance, (e)'s uniqueness argument works.
Part (d) compares representatives of the same critical orbit and datum, not unrelated torus and box backgrounds.

**The covariance induction is not closed.** SA 17534 and 17548 explicitly put aged R-terms into the regular action and then into `E^{(j+1)}`.
SA 17985–17991 supplies the healed contribution to those R-terms.
Thus “formed by a regular step” does not mean “has only invariant regular ancestors”.
Replacing the gauge factor does not prove invariance of an incoming activity.
The proof works for invariant incoming terms, and hence for the construction using regular steps alone.
For the actual family, (R-cov) or another proof of these incoming terms' invariance remains necessary.
The final claim that (R-cov) does not bind (19) is unsupported.
This is a missing input, not a computed noninvariant member. SA 7748–7754 and 7913 sketch covariance; SA 3942, 15998 and 16950 require it.

## 3. The BX repairs

The conditional passes below retain **(FG) as an open input** where a member occurs.
Proposition 3 has not supplied it for the complete family.

| Statement | Verdict | First failing step |
|---|---|---|
| Lemma 4* | ADVANCE for (b*); CORRECT-NO-ADVANCE for (c*) conditional on (FG) | None in the conditional argument below; (c*) still needs (FG). |
| Lemma 4′* | ADVANCE conditional on (FG) | None given [9.3], [T4], and the stated geometry. The node correction restores top-row agreement. |
| Lemma P | ADVANCE conditional on (FG) | None. Endpoint data bound adjacent gauge ratios; the path-sum ceiling admits the logarithmic path. |
| Lemma B | ADVANCE | None, conditional on (ER8u). Gauge one supplies (H), and scalar Cauchy gives the stated estimates. |
| Lemma O | ADVANCE as the stated response implication | None with [PW-H], the radius flow, and the cited ambient-layer conventions. |
| Theorem BX* | WRONG with only its stated invariance premise | BX*-3 uses (FG) through Lemma 4*(c*); (REL′) alone has not supplied it. The package works with (FG) added. |
| Proposition I* | WRONG as proved | Item 2 imports the unresolved BX*/(FG) input. Independently, the final paragraph promotes half-radius bounds to the full core. |

For Lemma 4*, use the **plain** constraint derivative `K_T`.
The cited `a3-derivative.md` Lemma 6.2 instead names the straightened derivative (SA 9627–9644).
The required plain equation follows directly: criticality annihilates `ker Dm`, so `F′=Dmᵀλ`.
At zero, surjectivity gives `λ(0)=0`; differentiation gives `L₀a_Φ=K_Tᵀλ̇`.
Subtract the affine solution and pair with the difference: `‖d(a_Φ−ℓᵇ)‖²=0`.
The box Poincaré lemma gives a gradient. The Landau relation adds another gradient (SA 9693–9717).
The Hessian gauge identity removes both, and the interior current is zero.

The corrected collar datum in Lemma 4′* has zero top rows; [T4] gives its exponential decay.
BX*-2's weighted response sums, Lemma P's admitted path, and Lemma B's augmented ball repair the earlier analytic defects.
SA PW1–PW16 (13426–13787) and 15821–15835 retain their response and domain premises.

**Induction defect.** A bound on a half ball does not bound a holomorphic function on the full ball.
For example, `f(z)=g(2z/r)^N` is bounded by `g` on `|z|<r/2`, but not on `|z|<r`.
Proposition I* needs an explicit, non-shrinking two-radius induction, with bounds on the larger input domain.
Its separate evaluation-admission arguments survive with their named room and response premises.
BX* also retains its old-age condition; young ages use the separate whole-core estimate (SA 13837–13855).

## 4. Regional prescription (10)

**No, not on the full admitted move core.** There is an advance for regular moves using (REL′).
Given the named layered inputs on each regional restriction, use `regional-gauss.md`'s fixed meet prescription with `A^{rel}`.
Lemma 2 removes its axial-reference restriction. The real comparison and complex perturbation bound give (6).
Section 4's normally convergent logarithm then gives coherence. An ambient compression alone would not give this intrinsic construction.

Two applications remain missing: admission of every lifted/stage core to these hypotheses, and identification with each move's consumed Gaussian.
On physical axial pairs the regular operators agree. Off that slice the relative prescription changes the raw absolute operator.
In particular, (REL′) retains the absolute factors in the large-field operations (SA 17531, 17558).
At the admitted flat pair `1^g`, their contour Hessians are `cos ε` and `1` on the same fibre direction.
Thus unrestricted gauge covariance cannot identify them.
The profile-weighted patch precision (SA 17643–17645), its actual integration subspace, and its regional gap remain outside Lemma 2.
SA RF9 (20317–20336) retains the regional gap and continuation as inputs.
