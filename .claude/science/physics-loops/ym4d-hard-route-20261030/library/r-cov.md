# r-cov: gauge covariance of the large-field operation
Provenance: Codex (GPT-6 family; requested effort max; exact runtime variant and effort not exposed); checkout `6c5f42191c4ca23fce4672117033d43b709b0df7`; Sussman–Alpoge `31a47c543775`; research text, not an audit.

## 1. Scope and sources

The target is real bare gauge invariance of each term formed by \(\mathcal R\).
This includes aged terms filed into the regular action.
It also includes terms filed into \(E^{(j+1)}\).
Invariance of their total sum would not suffice.

The operation and slice-extension proposal come from Ethan Sussman and Levent Alpoge.
Claude and Codex are the authors of their cited text.
Line numbers below refer to their pinned `YM4_sketch_500.tex`.
The local inputs are Claude's `gamma-bx.md` and Codex's `gamma-bx-check.md`.
This note grants no scientific status.

## 2. What the outline supplies

SA 17534 and 17548 put aged remainders into the regular action and then into \(E^{(j+1)}\).
SA 17989–17997 puts the connected healed contribution into those remainders.
Thus the induction objection in `gamma-bx-check.md`, Section 2, applies.

SA 17585 calls both post-tree tests “not gauge invariant”.
Its frame average restores lattice symmetry and preserves the sum of outcomes.
It does not average over the gauge group.
SA 17499 requires that the “measure must be gauge invariant” before replacing a gauge draw by its factor.
SA 7660–7681 gives the corresponding Haar and tree identities.

SA 7747–7754 and 7913 sketch covariance and slice extension.
The extension is said to retain “locality, the bounds, and holomorphy”.
SA 5733–5736 separately requires holomorphic descent on intersecting complex gauge orbits.
SA 6155–6158 retains stage-domain inclusions as hypotheses.
These are distinct requirements.

The existing literature search is `lit-large-field.md`, Section 1.
It records no healing operation in the cited YM3 or QED3 manuscripts.
No replacement proof is imported from them here.

## 3. A small axial map need not preserve the core

Here is an obstruction to the direct use of Route B.
It concerns the total complex field, not merely its real reference.

Use a uniform, node-free tower of depth \(j\).
Measure lengths at its top level, so \(\eta=L^{-j}\).
Let \(T=\operatorname{diag}(1,-1)\), with \(\|T\|=1\).
Choose the radii within the flat continuation chart.
Set \(t=a_1/2>0\), and take \(L^j>2\).
On a torus, or a box with the required margins, put
\[
 U=1,\qquad A'_1=itT,\qquad A'_\mu=0\ (\mu>1),\qquad \mathbf J=0.
 \tag{1}
\]
Then \(\mathbf U_1=e^{-\eta tT}\), and all other links equal one.
All plaquettes equal one.
The current and \(\nabla_UA'\) vanish.
The real potential gauge is zero, so its \(CMa_0\) bound holds.

All averaging paths have the same transport between their endpoints.
Thus every mean equals that transport.
Restriction and every tower truncation retain a flat connection.
For real \(s\), the corresponding family \(e^{i\eta sT}\) is flat and critical on each constraint fibre.
Its continuation to \(s=it\) is the same exponential family, up to the prescribed residual gauge.
Consequently every tower curvature and current in (R6) is zero.
For sufficiently small radii, the data stay in these continuation charts.
Hence (1) satisfies (R4)–(R6), with room in each inequality.

Let \(y(x)\) be the top centre of the pillar containing \(x\).
The tower axial transformation pinned at the tops is
\[
 c(x)=e^{-t(x_1-y(x)_1)T}.
 \tag{2}
\]
Indeed, it makes every within-pillar transport equal one.
This verifies every lower axial condition too.
The pinned slice has a unique representative, so (2) is its transformation.
Its condition number satisfies
\[
 \|c(x)\|\,\|c(x)^{-1}\|
 =e^{2t|x_1-y(x)_1|}\le e^t.
 \tag{3}
\]
There is no large condition number here.

Take a positive bond crossing a top-block face in direction one.
The two top centres differ by one.
Direct multiplication gives
\[
 \mathbf U^c(b)=e^{-tT},\qquad \|\mathbf U^c(b)\|=e^t.
 \tag{4}
\]
For any splitting \(\mathbf U^c=e^{i\eta A''}U''\) with \(U''\) unitary,
\[
 e^t=\|e^{i\eta A''(b)}\|
 \le e^{\eta\|A''(b)\|}.
\]
Thus \(\|A''(b)\|\ge t/\eta>a_1\).
No splitting places this axial representative in the same core.
Any fixed enlargement of \(a_1\) also fails at sufficiently large depth.

This refutes core preservation by the pinned axial transformation.
It does not refute an extension defined on a larger domain.
Such an extension needs its own bounds and an identification argument.
Small condition number alone supplies neither.
Axializing only the real reference \(U\) avoids (4).
It leaves the total complex field off the axial slice.
That alternative still needs descent and the pair tie of SA 5729–5736.

## 4. What a gauge draw does prove

A non-invariant test does not, by itself, give a non-invariant output member.
Here is the exact distinction needed for Route A.

Let \(H\) fix the coarse sites.
Let \(\ell\) be a gauge map constant on each block.
Write \(v=q\ell\), with \(q\in H\).
For the absolute gauge factor \(G\), define
\[
 K(W,F)=\int_H G(W^u)F(W^u)\,du.
\]
Block constancy gives \(G(S^\ell)=G(S)\).
The substitution \(h=\ell^{-1}uq\ell\) preserves Haar measure.
Therefore
\[
 K(W^v,F)=K(W,F\circ\ell),
 \qquad (F\circ\ell)(S)=F(S^\ell).
 \tag{5}
\]
This identity holds before choosing an input measure.
Replacing the draw by multiplication by \(G\) additionally requires an \(H\)-invariant input measure.
That is precisely the distinction at SA 17499 and 7660–7670.

A rooted tree has a related identity.
Let \(p_W(x)\) be its transport from the exterior root \(o\) to \(x\).
Then
\[
 p_{W^v}(x)=v(o)p_W(x)v(x)^{-1}.
\]
Consequently each normalized bond between tree vertices transforms by the common conjugation \(v(o)\).
Norm tests and a vacuum reference in those coordinates are unchanged.
This explains why the quoted failure of pointwise test invariance is not a counterexample to an integrated member.

These identities do not yet establish the required covariance of the carried factors.
They transport integration coordinates.
The target also transforms the arbitrary exterior pair read by each factor.
Those two actions must be identified for the actual stage and patch formulas.

## 5. The unresolved identification

The raw absolute precision cannot be transferred by unrestricted unitary covariance.
The witness in `regional-gauss.md`, Section 5, is explicit.
Choose one non-centre site \(x\), and set \(g(x)=e^{i\varepsilon T}\), with \(g=1\) elsewhere.
Both \((1,0)\) and \((1^g,0)\) are admitted real flat pairs.
On the fibre direction changing that site, the absolute contour term is
\[
 f_\varepsilon(s)=1-\cos(s-\varepsilon),
 \qquad f_\varepsilon''(0)=\cos\varepsilon\ne1=f_0''(0).
 \tag{6}
\]
The coarse datum stays fixed.
Both cutoffs equal one for sufficiently small \(s,\varepsilon\).
Thus an unrestricted change of background does not conjugate this raw gauge Hessian.
Lemma 2 of `gamma-bx.md` concerns the relative precision and does not identify this absolute one.

Equation (6) is an ingredient counterexample.
It is not a counterexample to a final \(R\) member.
Carried exponents, integrations, and connected sums can cancel an ingredient's gauge dependence.
SA 17989 defines the healed remainder only after those operations.
No calculation here identifies a surviving non-invariant member in that sum.

## Result

**Correction:** the pinned axial map need not preserve the admitted complex core.
Equations (1)–(4) prove this by hand, even with uniformly small condition number.
Thus Route B cannot obtain its member bound by direct evaluation on the same slice core.

**Row 237 remains open.** Route A is not disproved by the non-invariant tests or by (6).
Its first open input is the identification of the carried stage factors under the patched gauge action in (5).
That identification must hold at arbitrary admitted pairs and survive localization into each healed member.
It cannot be replaced by covariance of the relative regular precision.

No proof or counterexample for the final \(R\)-formed members is established here.
Accordingly this note does not supply \((\Gamma)\), \((FG)\), or the floor's missing \(R\)-input.
The correction is by Codex and has not been checked by the other model.
