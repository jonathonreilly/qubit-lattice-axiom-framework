# TC: prescribed tensor counter-insertions
Provenance: Codex (GPT-6; requested effort xhigh, runtime effort not exposed); checkout `79e6c7ba00a3e95ffdee2dd6ad329e6d8fd95bca`; Sussman–Alpoge `31a47c543775`; research text, not an audit; no status granted.

## 1. Source and task

Credit Ethan Sussman and Levent Alpoge, with Claude and Codex as authors of their text, for the cited constructions.
SA means their [pinned outline](https://github.com/ethanwsussman/Yang--Mills-LLM-experiment/blob/31a47c543775/YM4_sketch_500.tex).
It was fetched once to `/tmp/sa_ym4.tex`.
This note treats queue row 228 and equation (1) of `b4-typed.md`.

The requested passages have these roles.

| SA lines | Short quotation | Classification and scope |
|---|---|---|
| 4006–4037 | “must satisfy” | Assumed obligation. B4 requires the joint typed estimates. |
| 5066–5082 | “A suitable test is” | Assumed obligation. The potential test includes full tensor subtraction on complex integrand pairs. |
| 6486–6526 | “prescribed counter-insertion normalization”; \(T[\mathsf A[c]]=c\) | Assumed normalization. ER3 proves the chain rule; it does not prove this pulled-back tensor identity. |
| 22879–22918 | “to be proved” | Sketched ordinary-source induction. It does not build the typed extension. The reserve implication there is conditional. |

(Gamma) and (FG) remain named inputs.
Rule (REL) is not used.

## 2. The construction that is actually specified

SA 13347–13395 defines the scalar Wilson tent, then proves its affine normalization from the stated affine-response input.
Its formula is

\[
 A_{j,z}(U)=\sum_{\mu<\nu}\sum_{p_{\mu\nu}}
 h_z(p)\left(1-\tfrac12\operatorname{tr}U(\partial p)\right).
\]

SA 13345–13346 calls these “midpoint tents”.
SA 13323–13345 proves their uniform Hessian bound, conditional on the physical first-difference response estimate.
SA 13795–13802 gives the scalar counterterm's core bound.
These are proved conditional scalar statements.
They do not specify mixed curvature insertions.

SA 6686–6742 proves the tensor extraction bound from its core and response inputs.
It constructs an extractor, not its right inverse.
SA 5060 requires “all of its prescribed tensor counter-insertions”.
This is an obligation, not a formula.

The only occurrence of the tensor-action notation `\mathsf A[c]` is SA 6524.
That occurrence states its required normalization.
`b4-typed.md`:74–84 also names a prescribed family without defining one.
The ordinary induction carries only the scalar extractor and its Wilson tent.

SA 5918–5925 and 16150–16152 fix that scalar family's filing.
SA 32692–32700 identifies the same scalar object again.
SA 32349–32380 leaves the additional typed Ward inputs as assumptions.
None of these passages gives the missing mixed-curvature formula.

**Correction to `b4-typed.md`:** (TC) names a family whose full prescription has not been supplied.
The phrase *prescribed insertion* does not define its values away from its affine jet.
At this revision, no formula identifies which full family (TC) refers to.
The following counterexample shows why the normalization cannot fill this gap.
It does not assert failure of an unidentified SA family.

## 3. Explicit witness to the missing specification

Retain the original core and response inputs of `b4-typed.md`.
Write \(\eta=L^{-j}\), \(a=\alpha_j\), and \(\mathcal K_{j,z}\) for the origin's core on a fixed support.
It has curvature bound \(\|W_p-1\|\le C a\eta^2\) and contains the ball \(\|(A,J)\|_1<r_* a\).
These are the inherited whole-core and (ER8u) premises, not conclusions here.
Retain affine reproduction (AR) and the Landau first-difference response bound.

Index the six plaquette orientations by \(u\).
Let \(W_{u,r}(x)\), \(1\le r\le4\), be the four adjacent plaquettes, based at \(x\), with positive orientation \(u\).
Set

\[
 Q_u(x)=\frac14\sum_{r=1}^4\frac{W_{u,r}(x)-W_{u,r}(x)^{-1}}{2i},\qquad
 w_z(x)=\prod_{r=1}^4(1-|x_r-z_r|)_+,
 \qquad R_{uv,z}(U)=\sum_x w_z(x)\tfrac12\operatorname{tr}(Q_u(x)Q_v(x)).
 \tag{2}
\]

Both holonomies in each trace have the same base point.
Let \(A_{u,z}\) be the orientation-\(u\) part of SA's midpoint Wilson tent.
For a symmetric complex matrix \(c=(c_{uv})\), define witnesses in the full colour-invariant curvature space:

\[
 C^0_{j,z}[c]=\sum_u c_{uu}A_{u,z}+\sum_{u<v}c_{uv}R_{uv,z},
 \qquad
 C^-_{j,z}[c]=C^0_{j,z}[c]
       +j a^{-2}A_{j,z}\sum_{u<v}c_{uv}R_{uv,z}.
 \tag{3}
\]

File each expression once on one fixed enlarged coarse cube containing its support.
Use the same formula on its infinite-lattice companion and every common torus lift.
The coefficient uses only the origin and its fixed frame prefix.
This gives heredity, including on every common restriction where the support is retained.
These formulas are witnesses, not replacements adopted for SA's unspecified tensor insertion.

## 4. Hand verification and the failing bound

Both maps in (3) are linear in \(c\).
Gauge transformations conjugate each \(Q_u(x)\) at \(x\); cyclicity makes (2) gauge invariant.
The Wilson summands are gauge invariant too.
Matrix inversion is polynomial on \(SL(2,\mathbb C)\), so all these functions are holomorphic on every admitted core.
They ignore the independent current.
This proves their invariance directly; it proves neither (Gamma) nor (FG) for the original regular members.

At the flat pair, \(R_{uv,z}=DR_{uv,z}=0\).
On an affine response of curvature \(F\), (AR) gives \(DQ_u=\eta^2 F_u\).
The unshifted quadrature is \(\eta^4\sum_x w_z(x)=1\).
In one dimension it follows from
\(N^{-1}[1+2\sum_{r=1}^{N-1}(1-r/N)]=1\), with \(N=\eta^{-1}\).
Multiply four copies.
SA's midpoint quadrature gives the diagonal terms.
Hence

\[
 \frac12D^2(C^0[c]\circ p_j)(0)[\ell_F,\ell_F]
       =\frac12\sum_{u,v}c_{uv}\langle F_u,F_v\rangle.
 \tag{4}
\]

The first derivative is zero, so the second derivative of \(p_j\) contributes nothing.
Also \(A_{j,z}=DA_{j,z}=0\) at the flat pair, so each product \(A_{j,z}R_{uv,z}\) has zero Hessian there.
Thus \(T(C^-[c])=T(C^0[c])=c\), with the full pointed convention of `b4-typed.md`.
Both families retain the scalar Wilson tent and each orientation's Wilson weight.

On the whole core, \(\|W^{-1}\|\le2\) after the inherited radius ceiling is imposed.
Therefore \(\|Q_u\|\le C a\eta^2\).
Quadrature gives \(|R_{uv,z}|\le C a^2\).
The determinant identity \(1-\tfrac12\operatorname{tr}W=\tfrac12\det(W-1)\) gives the same bound for \(A_{u,z}\).
Filing on the fixed support costs one fixed factor in the member norm.
Consequently

\[
 \|C^0[c]\|_{j,\kappa}\le C\|c\|a^2,\qquad
 g_j:=\|R_{12,13,z}\|_{j,\kappa}\le C_1a^2.
 \tag{5}
\]

Their composed Hessians are weighted sums of products of physical curls of the first response.
Put \(L_u(b,x)=\tfrac14\sum_{r=1}^4d_\eta H\delta_b(p_{u,r}(x))\), using positive orientations.
For \(R_{uv,z}\), the kernel is

\[
 \sum_x\eta^4w_z(x)\big[
 \langle L_u(b,x),L_v(b',x)\rangle
 +\langle L_u(b',x),L_v(b,x)\rangle\big].
\]

The contour and Landau curls agree, since their responses differ by a gradient.
The retained Landau bound and quadrature bound this kernel by
\(C e^{-\delta(|b-z|+|b'-z|)}\), uniformly in \(j\).
Summing with any smaller exponential weight gives a uniform Hessian moment.
SA's diagonal calculation gives the same result for \(A_{u,z}\).
The quartic addition has zero Hessian, so \(C^-\) has exactly the same Hessians as \(C^0\).

For an input \(E\) of norm \(g\), retain (FG) and the original core, response, and entropy premises.
The conditional UR estimate and ER13 give
\(\|K_E\|_{\rm moments}+\|T(E)\|\le Cg a^{-2}\).
Equation (5) and the preceding kernel bound then prove
\(\|C^0[T(E)]\|\le Cg\) and \(\|K_{E-C^0[T(E)]}\|_{\rm moments}\le Cg a^{-2}\).
Thus \(C^0\) supplies an explicit conditional completion of (TC).
This is an existence statement; it does not identify an already prescribed insertion.

Now take the actual-core member \(E_j=R_{12,13,z}\).
Its tensor \(c_*\) has \(c_{12,13}=c_{13,12}=1\), with all other entries zero.
Thus

\[
 C^-[T(E_j)]=R_{12,13,z}+j a^{-2}A_{j,z}R_{12,13,z},
 \qquad K_{E_j-C^-[T(E_j)]}=0.
 \tag{6}
\]

Here is an admitted pair where the member bound fails.
Put \(T=\operatorname{diag}(1,-1)\), \(t=\epsilon a\), and \(J=0\).
On a box containing all plaquettes in (2), set
\(A_2(x)=A_3(x)=t(x_1-z_1)T\), with other components zero.
Extend using a fixed compact cutoff equal to one on that box.
Its physical \(C^1\) norm is at most \(C_0t\), uniformly in \(\eta\).
Choose fixed \(\epsilon>0\) so that \(C_0\epsilon<r_*\) and \(t\eta^2\le1\).
Then \(P_j=(e^{i\eta A},0)\) lies in the actual core by (ER8u).

All four holonomies in each of the planes \(12\) and \(13\) equal \(e^{it\eta^2T}\).
Therefore

\[
 R_{12,13,z}(P_j)=\eta^{-4}\sin^2(t\eta^2)
                 \ge \frac{\epsilon^2a^2}{4}.
 \tag{7}
\]

For \(0\le s\le1\), \(\cos s\ge1-s^2/2\ge1/2\), hence \(\sin s\ge s/2\).
This proves (7) by hand.
Also \(A_{j,z}(P_j)=2\eta^{-4}(1-\cos(t\eta^2))\ge R_{12,13,z}(P_j)\), since \(2(1-\cos s)-\sin^2s=(1-\cos s)^2\).
Equations (5)–(7) now give

\[
 \frac{\|C^-[T(E_j)]\|_{j,\kappa}}{\|E_j\|_{j,\kappa}}
       \ge \frac{j\epsilon^4}{16C_1}\longrightarrow\infty.
 \tag{8}
\]

Thus the uniform member clause fails, although the matching jet and residual Hessian clause hold.
This failure already occurs on a real near-zero part of the original complex core.
No core enlargement or independent-current identity was used.

## Result

**Correction.** `b4-typed.md` has not specified the full tensor insertion whose (TC) it asks to prove.
Its conditional reduction remains conditional.
The outline proves the scalar construction and states the full tensor obligation.
It does not provide the full formula needed to identify a prescribed member.

The family \(C^0\) in (3) satisfies (TC) under the retained inputs.
The family \(C^-\) has the same affine jets and Hessians, but fails the uniform member bound by (8).
Neither family is asserted to be SA's prescribed one.
Consequently this note neither proves nor refutes (TC) for that unidentified family.
The hand argument is by Codex, not yet checked by the other model.

Open: specify the full insertion, its filing and companion, then verify all of (TC) for that exact prescription.
(Gamma), (FG), and the inherited background/core inputs remain named premises.
The history reserve, formed-copy bound, and joint capacity allocation also remain separate B4 inputs.
