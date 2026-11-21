# regional-gauss: regional gaps and coherent logarithms
Provenance: Codex (GPT-6 family; exact serving variant not exposed), requested effort max; checkout `71c90bcbcf35f85afe41819f1498afe0b145a5aa`; Sussman–Alpoge commit `31a47c543775`; research text, not an audit; grants no status.

Moves: row 231, the regional existence input of [d3-local.md](d3-local.md), Sections 2 and 4, for (D3).

Credit: Ethan Sussman and Levent Alpoge, with Claude and Codex as authors of their text.
The regional construction below uses their [YM4 outline](https://github.com/ethanwsussman/Yang--Mills-LLM-experiment/blob/31a47c543775/YM4_sketch_500.tex) (SA) and [YM3_I](https://github.com/ethanwsussman/Yang--Mills-LLM-experiment/blob/31a47c543775/YM3/YM3_I.tex).
Each source was fetched once. Line numbers refer to these versions.

## 1. What the outline supplies

| Passage | Short quotation | Classification |
|---|---|---|
| SA L6237–6243 | “typed input data” | **Assumed.** Covariance matrices, localization maps and logarithm branches are supplied together. |
| SA L17541–17548 | “logarithm of the operator built on $Y$” | **Sketched.** Regional finite differences localize the determinant. This paragraph does not establish the regional gap. |
| SA L3926–3937 | “We must still verify” | **Assumed for the actual cores.** The Gaussian and cluster conclusions remain conditional on their matrix/core hypotheses. |
| SA L20317–20336, (RF9) | “part of this Gaussian-localization input” | **Assumed explicitly.** This later definition requires the intrinsic regional gap, complex continuation and local walks. |

SA L14118–14157 sketches the gap from flat positivity, local gauges, kernel moments and a localization identity.
SA L14159–14218 then treats collared decoupling, using those bounds.
Its ordinary compressions do not establish the intrinsic regional construction in (RF9).
The finite Gaussian comparison at SA L13906–14099 starts with the reference and perturbation bounds (FG1).
It does not supply the missing regional bounds.

YM3_I gives detailed proofs under its operator and core inputs.
Proposition II-44-37, L40674–40949, constructs the local trace logarithm and normaliser.
Proposition II-69-13, L51590–51682, proves the history version's regional gap.
The following propositions construct its local determinant terms and exact determinant identity.
The task therefore needs a four-dimensional port of those inputs and arguments.

## 2. The checked four-dimensional input

Use positive, nonpivot bonds in level-\(k\) units, with counting measure and three colour coordinates.
All transposes in the operator construction are bilinear.
Inequalities use the Hermitian norm.

[a2-layers.md](a2-layers.md), Sections 7.5–7.6, supplies the real gap and complex perturbation estimate.
[a2-full.md](a2-full.md), Sections 3–5, supplies identification and the upper bound.
Use the repairs in [a2-layers-gate.md](../gates/a2-layers-gate.md), Sections 6–7, and [a2-full-gate.md](../gates/a2-full-gate.md), Sections 3–5.
In particular, retain the real axial hypothesis and distinguish ambient from free-coordinate constraint Hessians.
These are checked implications; their inverse and coefficient premises remain premises.

Their usable statement is
\[
 \gamma I\le\mathsf A[\mathcal S,(U,0)]\le BI,
 \qquad
 \|\mathsf A[\mathcal S,P]-\mathsf A[\mathcal S,(U,0)]\|
       \le C_*(\alpha_1+\gamma_0).                         \tag{1}
\]
Here \(\mathcal S\) is any admitted separated sequence through \(k+1\).
Its real reference satisfies the stated regularity and top axial conditions.
The constants are independent of depth, volume and region shape.
The matrix is the specified independent-current precision of [inv-root.md](inv-root.md), (10).
At the physical step pair it is the actual Gaussian precision.
An off-shell regional current need not equal the current of its inner action.

The repaired walk bounds also give
\[
 \max\!\left\{\sup_b\sum_{b',\omega},\sup_{b'}\sum_{b,\omega}\right\}
 e^{\eta\ell_\omega(b,b')}\|A_\omega(b,b')\|\le W.       \tag{2}
\]
This is [inv-root.md](inv-root.md), (11), checked in [carrier-adopt.md](carrier-adopt.md), Section 1.
Use the full read sets of [h-walk-fix.md](h-walk-fix.md), Lemma N and Theorem H′.
[carrier-check.md](../gates/carrier-check.md), Sections 4–6, checks their use for the replacement carrier series.
These bounds apply on the admitted domains, not on every formally named core.

## 3. Intrinsic regional matrices and their gap

Here is the precise core on which the port works.
Call it \(\mathcal R_4(X)\).
It contains one splitting \(\mathbf U=e^{i\eta_kA'}U\), with independent current \(J\).
Require the regular-pair clauses of `a2-layers.md`, Section 1, on contained stencils in \(X\).
Require their real gauges on every tested cube contained in \(X\).
Require the real top average to be block axial on the move's next blocks.
Fix \(\alpha_0\) below (1)'s ceiling and choose
\[
                    C_*(\alpha_1+\gamma_0)\le\gamma/4.     \tag{3}
\]
Retain the checked operator premises of Section 2 on this class.
This defines a sufficient domain; it does not redefine an admitted move core.

Fix the move's sequence \(\Omega_0\supset\cdots\supset\Omega_{k+1}\), integration mask \(I\), and coarse cube set.
For a union \(Y\subset X\) of those cubes, form the maximal erosion tower:
\[
 T_0(Y)=Y,\qquad
 T_{q+1}(Y)=\bigcup\{Q:\ Q\text{ is an aligned }M_1\xi_{q+1}
 \text{ cube},\ \operatorname{dist}_\infty(Q,T_q(Y)^c)>\rho\xi_q\},
 \quad \Omega_q^Y=\Omega_q\cap T_q(Y),
 \quad \xi_q=L^{q-k}.                                  \tag{4}
\]
Use the same grid and strict erosion convention throughout.
Each intersection remains a union of aligned cubes.
Its complement is the union of the two complements.
Distance to that union is their minimum.
Thus \(\Omega^Y\) has the original separation \(\rho\xi_q\).
This is the dimension-independent meet argument of [meet-6c.md](meet-6c.md), Lemma J*.

The restricted pair remains regular for this meet.
Indeed, its new layer index \(i\) is at most its old index.
Replacing the old scale by \(\xi_i\) weakens each curvature, perturbation and current bound.
For the gauge clause, take a tested cube \(Q\subset X\) in the new layers \(i,i+1\).
Let \(j\ge i\) be largest with \(Q\subset\Omega_j\), using the fine sequence through \(k\).
If \(j<k\), some point of \(Q\) lies outside \(\Omega_{j+1}\).
Separation prevents \(Q\) from meeting \(\Omega_{j+2}\), since its diameter is smaller than \(\rho\xi_{j+1}\).
Increase the separation floor once to ensure this inequality for every tested gauge cube.
Hence \(Q\) lies in the old layers \(j,j+1\).
For \(j=k\), it lies in the terminal fine layer.
The old gauge applies, since its allowed cube size increases with \(j\).
Its bounds also hold in the smaller unit \(\xi_i\).
The retained next blocks inherit the real axial condition.
Their averaging contours remain inside the meet by separation.
This proves regional admission from \(\mathcal R_4(X)\), without a new critical-point construction.

Define
\[
 e_{k+1}=\sum_{q=0}^{k}(\rho\xi_q+M_1\xi_{q+1})
       <\frac{L(\rho+LM_1)}{L-1}.
\]
Induction in (4) shows that distance greater than \(e_q\) from \(Y^c\) implies membership in \(T_q(Y)\).
Choose \(r_N>e_{k+1}+C_{\rm st}(L)\), where \(C_{\rm st}\) covers the top averaging and pivot stencils.
Choose \(M\) afterwards, with \(4(r_N+1)<LM\).
Let \(I_Y\) contain the bonds of \(I\) whose closed \(r_N\)-neighbourhood lies in \(Y\).
They are valid nonpivot coordinates for the meet, with the original integration mask.

Rebuild every average, inverse, multiplier and pivot map on \(\Omega^Y\), using only \(P|_{X\cap\Omega_0^Y}\).
Then set
\[
 A_Y(P)=\chi_{I_Y}\mathsf A[\Omega^Y,P|_{\Omega_0^Y}]
                       \chi_{I_Y}^{\mathsf T}.           \tag{5}
\]
Equation (1) applies to the rebuilt operator before compression.
Zero extension of vectors and (3) give
\[
 \gamma I\le A_Y(U,0)\le BI,\qquad
 \|A_Y(P)-A_Y(U,0)\|\le\gamma/4,\qquad
 \operatorname{Re}A_Y(P)\ge3\gamma I/4.                  \tag{6}
\]
All defining inverses exist by the same regional application of the checked package.
Also \(\|A_Yv\|\|v\|\ge\operatorname{Re}\langle v,A_Yv\rangle\ge3\gamma\|v\|^2/4\).
Finite dimension gives the regional covariance \(C_Y=A_Y^{-1}\), with \(\|C_Y\|\le4/(3\gamma)\).
Empty coordinate sets cause no exception.
For the full torus, (4) leaves the sequence unchanged, so (5) is the move's integration block.

This ports the gap in YM3_I II-69-13 on \(\mathcal R_4\).
The stronger checked layered estimate replaces its mesh localization step.
It does not infer (6) by compressing an unrelated ambient operator.
Four dimensions change the geometric constants, not the meet or zero-extension arguments.

## 4. Existence and coherence of the logarithms

Set, uniformly for all these regions,
\[
 c=(B+\gamma)/2,\qquad
 q=\frac{B-\gamma/2}{B+\gamma}<1,\qquad T_Y=I-c^{-1}A_Y.
\]
The real spectral interval in (6) gives
\[
 \|I-c^{-1}A_Y(U,0)\|\le\frac{B-\gamma}{B+\gamma}.
\]
Adding the perturbation divided by \(c\) gives \(\|T_Y\|\le q\).
Thus
\[
 L_Y=(\log c)I-\sum_{n\ge1}\frac{T_Y^n}{n},\qquad
 \|L_Y\|\le |\log c|-\log(1-q)                         \tag{7}
\]
converges normally on every fixed-real-background slice.
Each defining matrix is holomorphic there, so \(L_Y\) is holomorphic.
The scalar power-series identity, applied to the single matrix \(T_Y\), gives \(e^{L_Y}=A_Y\).
At a positive real matrix, (7) is its real spectral logarithm.
This is the four-dimensional version of YM3_I (II-44-14) and (II-68-16).
The colour trace still has dimension three.
The spatial dimension does not replace that factor by four.

There is no patching choice in (7).
Identical regional data, sequence traces, masks and coordinate conventions give identical matrices and logarithms.
If coordinates are related by an admitted similarity \(S\), each partial sum transforms by \(S^{-1}(\cdot)S\).
The limit has the same property.
The same matrix presented by two real splittings gives the same series.
This conclusion requires equality of the matrices; it does not establish that equality for different constructions.
Coherence concerns the same regional problem, not commutation of logarithms with compression.

Disconnected regions also cause no branch ambiguity.
A coordinate-monotone cube path to another wall-component first crosses the complement.
Consequently each erosion test in (4) is determined inside its own component.
All contained stencils split, and the inverses split by uniqueness.
Thus \(A_Y=\bigoplus_iA_{Y_i}\), and (7) gives \(L_Y=\bigoplus_iL_{Y_i}\).
Set the trace of the empty matrix to zero and its determinant to one.

In particular,
\[
 e^{\operatorname{Tr}L_Y}=\det A_Y,\qquad
 Z_Y:=\int_{\mathbb R^{3|I_Y|}}e^{-v^{\mathsf T}A_Yv/2}\,dv
      =(2\pi)^{3|I_Y|/2}e^{-\operatorname{Tr}L_Y/2}.       \tag{8}
\]
Here \(|I_Y|\) counts positive bonds, not colour coordinates.
Triangularizing \(L_Y\) proves the determinant identity, since exponentiation exponentiates its diagonal entries.
For real data, orthogonal diagonalization proves the Gaussian integral formula (8).
For complex data, (6) supplies an integrable Gaussian majorant on compact subsets.
For each real reference \(A_0\), both sides are holomorphic on the symmetric matrix ball \(\|A-A_0\|<\gamma/2\).
The series (7) converges there, and the real part remains positive.
They agree on its real matrices.
Apply the one-variable identity theorem successively to their independent entries near \(A_0\).
Connectedness of the ball gives the asserted continuation.
Thus (8) uses one coherent determinant root, without a scalar principal-log choice for \(\det A_Y\).

The finite differences in `d3-local.md`, (1), now exist on \(\mathcal R_4\).
Their full sum is \(-\operatorname{Tr}L_{\mathcal P}/2\).
Component additivity makes their disconnected coefficients zero.
This proves the normaliser's existence and exact locality on this domain.
It does not prove its polymer decay bound.

**Collared complex parameters.** The same conclusion survives a sufficiently small additional matrix perturbation.
For example, (2) bounds the change from precision tags outside a collar of width \(w\) by
\[
 \|\chi(A(s)-A(1))\chi^{\mathsf T}\|
 \le 2W\exp\{16\bar\kappa-\eta(w-R_h)/2\},               \tag{9}
\]
Use the transpose-closed precision series, with \(M\ge8R_h\), \(C_g\bar\kappa/M\le\eta/2\) and \(w\ge2R_h\).
Indeed a varied carrier has length at least \(w-R_h\).
A traversal, split into segments of length \(M/4\), meets at most \(16+C_g\ell/M\) parameter cubes.
Hence \(|s^\omega-1|\le2e^{16\bar\kappa+C_g\bar\kappa\ell/M}\); summing (2) proves (9).
This is the checked four-dimensional count in `inv-root.md`, Section 5.
Budget \(\gamma/8\) for (3) and \(\gamma/8\) for (9); (6)–(8) then remain valid.
The collar must exist inside each regional problem.
This argument supplies no gap for arbitrary tags adjacent to the integration bonds.

## 5. First input that does not port

The first unestablished input is the real-reference comparison on the **full admitted move core**.
Section 3 requires an axial real reference.
SA (R4)–(R6), L5664–5731, requires small local gauges, not axiality of the given representative.
Thus full-core membership does not imply membership in \(\mathcal R_4\).
The missing assertion is
\[
 P\in\mathcal K_{\mathrm{move}}(X)
 \Longrightarrow \text{a regional prescription with (6), agreeing with the move's Gaussian}. \tag{10}
\]

YM3_I L40189–40201 uses unitary gauge covariance to transfer its local flat comparison.
That transfer does not identify our raw absolute gauge form.
This is already exposed by [ur-gauge-check.md](../gates/ur-gauge-check.md), D2.
Its hand witness applies here.

Take \(k=0\), a node-free block centre \(y\), and one interior site \(x\ne y\).
Set \(T=\operatorname{diag}(1,-1)\), \(g(x)=e^{i\varepsilon T}\), and \(g=1\) elsewhere.
The pair \((\mathbf1^g,0)\) is real and flat, with zero current.
It lies in the core: gauge it to one; every tower has zero curvature and current.
Take \(\varepsilon\ne0\) arbitrarily small.
Every contour from \(y\) to \(x\) equals \(e^{-i\varepsilon T}\).
Vary \(g(x)\) to \(e^{i(\varepsilon-t)T}\); the coarse datum stays one.
The absolute summand and its axial-relative replacement are
\[
 f_{\rm abs}(t)=1-\cos(t-\varepsilon),\qquad
 f_{\rm rel}(t)=1-\cos t.
\]
Their second derivatives at zero are \(\cos\varepsilon\) and \(1\).
All other contour summands vanish.
For small \(\varepsilon,t\), both cutoff indicators equal one.
Hence these prescribed gauge forms differ even on an admitted fibre direction.
This refutes their identification by unrestricted gauge transfer, not positivity of the perturbed form.
It is not a counterexample to the outline's existence theorem.

SA L7754 already specifies the extension \(F^\natural(z)=F(c[z]\cdot z)\) from a slice.
Applying that prescription to the regional Gaussian requires its core estimates and full-region identification with the consumed Gaussian.
Those are the missing application in (10), not a missing abstract extension formula.
Equality on physical axial pairs alone does not supply the estimates.
This is the same unresolved distinction recorded in `a2-full.md`, Section 10, defect 5.
The simple gauge radius also carries \(CM\), which must be included when choosing the radii.
[c4-order.md](c4-order.md), rows 12 and 16, permits that order of choice.
It does not verify every lifted core or stage substitution; SA L6138–6158 explicitly retains those inclusions.

A further issue is the patch precision at SA L17643–17645.
Its action and gauge form carry profiles, which can vanish.
`a2-full.md`, Section 10, explicitly excludes this Gaussian.
Its actual integration subspace and regional gap still need an argument.

## Result

**Proof of a sketched step, conditional on the checked covariance inputs.**
Sections 3–4 construct intrinsic regional matrices, uniform gaps and coherent logarithms on \(\mathcal R_4\).
They supply the regional normaliser in `d3-local.md` on that domain.
The new argument is by Codex, not yet checked by the other model.

**Correction of an inference, not an outline theorem.**
The checked axial gap cannot be transferred to the raw absolute operator by unrestricted gauge covariance.
Section 5 gives the explicit failure, using the previously checked witness.

**Open:** the full-core prescription and estimate (10), the patch precision, and summable polymer bounds.
The separate (D1) response obligation also remains.
Thus this does not prove every-move (D3) or (LOC).
Every proof step above is by hand; no run supplies a mathematical conclusion.
