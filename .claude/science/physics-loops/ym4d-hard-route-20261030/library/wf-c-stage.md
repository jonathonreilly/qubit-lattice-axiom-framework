# WF-c at the first prepared-shell stage
Provenance: Codex (GPT-6 family; requested effort max; runtime variant and effort not exposed); checkout `642076279980fed422f1f41498277cdc9496f942`; Sussman–Alpoge commit `31a47c543775`; research text, not an audit; grants no status.

## 1. Scope and checked input

This note addresses row 254 and (D4).
Credit Ethan Sussman and Levent Alpoge, with Claude and Codex as authors of their text, for the outline's constructions.
SA denotes their [pinned outline](https://github.com/ethanwsussman/Yang--Mills-LLM-experiment/blob/31a47c543775/YM4_sketch_500.tex).
Credit Claude for `wf-c.md` and Codex for the stage reductions.

The usable check of `wf-c.md` is `b4-step.md` Section 0, as row 177 records.
The search for `wf-c` in `gates/` has no match in this checkout.
That check accepts Lemmas C and RC and Theorem 6c^C on their stated common datum ball.
It accepts Theorem A on its box-first domain, with its radius convention.
It accepts (H-node) on common interior pillars or over one Landau reference.
It rejects the inference from a bounded condition number to small gauge displacement on collar pillars.
Thus the checked input does not include that extra conclusion.

## 2. What the outline supplies

The index places Theorem 6(c) in chunk 09, not chunk 08.
Chunks 15 and 16 locate (OA7) and the stages.
The neighbouring rows and `obligations.md` retain their hypotheses.

SA 9783–9789 sketches comparison on a collared region.
Each part's collar lies in one layer.
Its gauge is prescribed only at tops away from collars.
SA 9913 sketches the defect-of-lifts proof using a geometric sum in that layer.
`wf-c.md` supplies the complex version on its common datum ball.

SA 17415–17447 defines the partially changed sequence and preserves each term's birth space.
SA 17585 defines the shell integrations.
SA 17654 retains the completed integrations when a later test fails.
SA 17612–17630 sketches the real test comparison.
SA 7913 sketches the extra gauge correction at former tops carrying stored fields.

The full complex admission remains an assumed input.
SA 6155–6158 calls stage inclusions “analytic inclusion hypotheses”.
SA 16825–16851 assumes initial room and (OA7), including current and node bounds.
SA 16898–16935 proves the larger-ball implication from those inputs.
SA 4036–4037 says actual inclusions “remain to be verified”.
SA 17229–17233 explicitly retains the primitive Yang–Mills verification.
This note therefore tests an extension of our collar lemma, not a missing qualification in their conditional theorem.

## 3. The attempted extension

Put \(j=t-\mathsf N_t\ge1\) and \(l=j+1\) for an eligible component \(C\).
At the first stage,
\[
 \Omega_l^0\cap C=\Omega_l^\circ\cap C,
 \qquad \Omega_l^1\cap C=C\setminus Z_l''(C).
 \tag{1}
\]
Only this determining member changes.
The action sequence stays fixed.
For endpoint set \(E(c)\), the affected rows are
\[
\begin{aligned}
 \Gamma_j^n&=\{c\in\mathbb T^{(j)}:E(c)\subset\Omega_0,
 E(c)\cap\Omega_j\ne\varnothing,
 E(c)\cap\Omega_l^n=\varnothing\},\\
 \Gamma_l^n&=\{c\in\mathbb T^{(l)}:E(c)\subset\Omega_0,
 E(c)\cap\Omega_l^n\ne\varnothing,
 E(c)\cap\Omega_{l+1}=\varnothing\},\qquad n=0,1.
\end{aligned} \tag{2}
\]
These are (R2), including omitted inward bonds.
Their endpoint sets can change.
Each preceding chart retains its own birth sequence and real reference.
It does not replace them by the stage-one sequence.

Lemma C does extend uniformly over an arbitrary parameter family satisfying its hypotheses uniformly.
Indeed, its product estimate uses only
\[
 \sum_{m=q}^{j-1}L^{m-j}\le(L-1)^{-1},\qquad
 \sum_{m=q}^{j-1}L^{2(m-j)}\le(L^2-1)^{-1}.
\]
Taking a parameter supremum does not change these constants.
Theorem 6c^C has the same property once both data lie in its common ball.
The forcing norm already includes its row sum.
Thus the number of parameters is not the obstruction.

The first missing hypothesis is the common ball for the actual complete composition.
For each preceding chart \(\tau\), the required old datum is
\[
 b_{1,\tau}=i^{-1}\Log\!\left[
 M_{\mathbf B_\tau}(X_1^{u_\tau})
 M_{\mathbf B_\tau}(U_\tau)^{-1}\right].                 \tag{3}
\]
Here \(X_1\) includes every retained earlier substitution, with parameters \(\zeta\).
Lemma RC requires (3) inside the assigned old continuation ball before applying the identity theorem.
It does not put (3) there.
Theorem A starts from its half-radius box-first input.
It does not establish that input for (3) on \(D_1^+\times\{\zeta\}\).
(LD) uses the response's own sequence and metric.
It cannot identify the two row spaces in (2).
`removed-fix.md` Section 7.3 retains exactly this distinction.

## 4. Explicit failures of two transfer arguments

**Replacing the independent current by the physical current fails.**
Use the identity-reference chart on a finite lattice.
Set \(U=I\), \(A'=0\), and \(\mathbf J(b)=i\epsilon H\) on one positive bond.
Set the other current components to zero, with the required orientation reversal.
Here \(H=\operatorname{diag}(1,-1)\) and \(\epsilon>0\) is below every applicable current radius.
At finite cutoff their minimum is positive.
All determining averages and tower backgrounds are identity.
Thus every curvature and tower-current clause is zero.
The pair satisfies (R4)–(R6), while \(\mathbf J\ne J(I)=0\).

At zero response datum, (R9) vanishes.
The returned current remains \(\mathbf J\), or \(L^{-3}\mathbf J\) after one unit change.
Replacing it by the background's own current gives zero instead.
This is an explicit failure on a common datum chart.
The holomorphic difference \(\mathbf J-J(\mathbf U)\) vanishes on physical pairs but not on this pair.
The physical graph therefore cannot support the required identity-theorem argument in the independent-current variables.
Theorem 6c^C itself does not make this replacement; its Remark 3 excludes it.

**Orbit comparison does not bound the separate quantities \(A_e,G_e\).**
Here is a chart example with zero curvature and zero current.
Choose adjacent bare sites \(x,y\), with \(v(x)=e^{i\epsilon H}\), \(v(y)=I\), and \(v=I\) elsewhere.
Fix \(0<\epsilon<1\).
Take
\[
 U_\tau=I,\quad \widehat U_0=I,\quad u_0=I,\qquad
 \widehat U_1(b)=v(b_-)^{-1}v(b_+),\quad u_1=v.
 \tag{4}
\]
Both raw fields are real and flat.
With themselves as real references, both have zero complex potential and satisfy every hereditary core clause.
Real gauge covariance supplies the flat tower backgrounds.
After return, \(W_0=W_1=I\).
Hence every old logarithm and (R5) datum is exactly zero.
However, at \(b=(x,y)\), the definitions in `d4-chart.md` give
\[
 B=1,\qquad
 A_e\ge\frac{2\lambda_e(b)}\eta\sin(\epsilon/2),\qquad
 G_e\ge\frac{2\lambda_e(b)}\eta\sin(\epsilon/2).
 \tag{5}
\]
Indeed, the eigenvalues of \(e^{i\epsilon H}-I\) have modulus \(2\sin(\epsilon/2)\).
For a tower with fixed positive \(\lambda_e(b)\), these bounds diverge under bare-mesh refinement.
The two terms in the exact returned-field difference cancel.
Consequently even exact orbit agreement and \(B=1\) do not prove the separate uniform bounds requested here.

Example (4) does not assert that the stage selects this return.
It refutes an inference from core membership and gauge condition numbers alone.
The actual return also fixes the stored data through the former-top correction at SA 7913.
That prescription must be estimated, not replaced by an arbitrary gauge or by \(u=I\).

## 5. Multiplier transport and the old tower

For any admitted path, put \(\gamma=\dot u u^{-1}\) and \(K=\operatorname{Ad}(u)\widehat J\).
Differentiating the inverse gives
\[
 \dot K=\operatorname{Ad}(u)\dot{\widehat J}+[\gamma,K],
 \qquad
 \dot W(b)=u(x)\dot{\widehat U}(b)u(y)^{-1}
              +\gamma(x)W(b)-W(b)\gamma(y).
 \tag{6}
\]
The current \(\widehat J\) uses the multiplier increment, not \(J(\widehat U)\).
In `stage-tangent.md` (7), that increment is
\(R_hK_h^{\mathsf T}\lambda-K_0^{\mathsf T}\lambda_0\).
Both terms must be differentiated.
The changing reference and row lift enter the anchor derivative in its (8).
The checked fixed-sequence estimate (LD) does not bound those additional derivatives.
Theorem 6c^C bounds its physical background-current difference instead.
Section 4 shows why these are different tasks.

Suppose the assigned path exists on the entire larger source, in every preceding chart.
Let \(T,a_e,g_e\) be the full-domain integrals in `oa7.md` (9).
Then `stage-tangent.md` (13) gives
\[
 A_e\le a_e,\qquad B\le e^T,\qquad G_e\le e^Tg_e,
 \qquad E_e\le e^{2T}(a_e+g_e).
 \tag{7}
\]
Its (14) requires, for every old tower,
\[
 \sup\|w_0\|_{*,e}<R_e/4,\qquad C_{A,e}R_e<r_{B,\tau,e},
 \qquad
 e^{2T}(a_e+g_e)<\min\{q-q_0,(1-q)R_e/4\}.
 \tag{8}
\]
Here \(\sup|W_0U_\tau^{-1}-I|\le q_0<q<1\).
These bounds keep the whole path in the old half ball.
The logarithm estimate costs \((1-q)^{-1}\).
The fixed-reference averaging bound then admits the old (R5) continuation.
Apply this separately with each erosion rule's assigned tower and radius.
Neither rule permits replacing the old reference or determining set.

The collar results do not verify (8) for the stage maps.
They also do not bound the assigned covariant gauge tangent entering \(g_e\).
The example (4) explains why its omission cannot be repaired by a condition-number estimate.
Thus (7) remains a conditional implication here.

## Result

**Correction of the attempted transfer from WF-c to the stage.**
The common-ball parameter extension holds, but it does not establish the required stage admission.
Section 4 gives explicit configurations refuting physical-current replacement and the inference from orbit bounds to separate \(A_e,G_e\) bounds.
They are not counterexamples to the prescribed prepared-shell map.
No actual drop-out configuration violating its bound has been established.

**First input still open:** establish (3) on \(D_1^+\times\{\zeta\}\) for every preceding chart.
It must identify the actual continued pair, multiplier current, and return preserving the stored data.
Its full tangent must satisfy (8), including the covariant gauge term.
Uniform \(A_e,G_e,B\), old (R5), and (D4) remain unproved for the actual stage.
This lane does not close row 254.
The new examples have not been checked by another provider.
All calculations above are written arguments; no computational run supplies a proof step.
