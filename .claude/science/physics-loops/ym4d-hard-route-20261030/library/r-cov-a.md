# r-cov-a: carried factors in the large-field operation
Provenance: Codex (GPT-6 family; requested effort max; exact runtime variant and effort not exposed); checkout `408191a7667374b8b510d7b694eed8c7e9958e9f`; Sussman–Alpoge `31a47c543775`; research text, not an audit.

## 1. Scope and source

Queue row 238 asks for real bare gauge invariance of each healed member.
This includes aged contributions to the regular action and to \(E^{(j+1)}\).
Invariance of the summed measure does not settle this question.

Credit Ethan Sussman and Levent Alpoge, with Claude and Codex as the authors of their text.
Their pinned `YM4_sketch_500.tex` supplies the large-field operation and its localisation rules.
The local inputs are `r-cov.md`, `gamma-bx.md`, `gamma-bx-check.md`, and `p2-floor.md`, Sections 2–3.
The corrections in `gamma-bx-check.md` govern the claims used here.
In particular, covariance of the relative regular precision does not identify the absolute large-field precision.

The outline sketches the required covariance at SA 7748–7754 and 7913.
SA 17499 requires an invariant measure before replacing a gauge draw by its density factor.
SA 17585 calls the two post-tree tests “not gauge invariant”.
Neither statement alone refutes covariance of an integrated healed member.

## 2. The stage draw and its residual action

Fix a component \(X\) and its level \(k\).
Let \(g\) be real, and let \(\widehat g\) equal \(g\) outside \(X\).
Inside \(X\), set \(\widehat g(x)=g(y_k(x))\), where \(y_k(x)\) is its level-\(k\) ancestor.
A stage gauge block contained in \(X\) has level at most \(k\).
Thus \(\widehat g\) is constant on that block.

On a stage contour, the absolute gauge factor therefore obeys
\[
 G_j(W^{\widehat g})=G_j(W).
 \tag{1}
\]
Both the cutoff and the trace are unchanged by unitary conjugation.
The averaging constraint transforms by conjugation at its initial coarse site.
Haar measure and its delta at the identity are unchanged.

More generally, write a stage action as \(v=q\ell\), where \(q\) fixes its coarse sites.
Here \(\ell\) is the block lift of the coarse restriction.
For the gauge draw, `r-cov.md` (5) gives
\[
 \int_H G_j((W^v)^u)F((W^v)^u)\,du
 =\int_H G_j(W^u)F((W^u)^\ell)\,du.
 \tag{2}
\]
The substitution is \(u\mapsto\ell^{-1}uq\ell\).
It preserves product Haar measure.
Thus a stage draw removes the finer gauge action and carries the coarse action to the next stage.
The identity transports the complete function \(F\).
It does not identify a separately changed pair argument of \(F\).

## 3. Re-fixing the reference tree

The box tree gives more than the fluctuation condition \(B|_{T_0}=0\).
Use the entrance tree \(T\) of \(\delta_{\rm ax}\), rooted at the exterior site \(o\).
The reference minimum satisfies \(V_\Lambda|_T=1\) (SA 17604).
Let \(v\) be a gauge action on its top sites.
The tree transport of \(V_\Lambda^v\) to an interior vertex \(x\) is
\[
 p_{V_\Lambda^v}(x)=v(o)v(x)^{-1}.
 \tag{3}
\]
Re-fixing this tree therefore leaves the composite action \(v(o)\) at every interior top site.
The entrance bond is essential here.
The transformed field is the selected reference minimum, by uniqueness of its critical orbit and tree representative.
This uses the background input of SA Proposition 2.4.
The equality continues on its specified analytic chart by uniqueness there.

Lift this composite action down the tower.
It is constant on the interior shell and core, whose ancestor blocks lie inside the prepared box.
The geometric margins in SA 17585 supply this containment.
Write this constant as \(c=v(o)\).
Then the transformed shell coordinates and core data satisfy
\[
 V_0' =cV_0c^{-1},\qquad
 V''{}'=cV''c^{-1},\qquad
 B'=\operatorname{Ad}(c)B,\qquad
 \zeta'=c\zeta c^{-1}.
 \tag{4}
\]
The principal logarithm commutes with this conjugation on its domain.
The tree delta, Lebesgue measure, and test \(|g_kB|<\delta'_k\) are unchanged.
For Lebesgue measure, \(\operatorname{Ad}(c)\) is orthogonal with determinant one.

The last-shell datum now transforms correctly:
\[
 (1,\zeta')=(1,\zeta)^c.
 \tag{5}
\]
Its local critical orbit transforms with the datum.
Each tested curvature norm is therefore unchanged.
This proves the last-shell identification for these jointly transported data.
It does not justify resetting the vacuum after an arbitrary change of representative.

Indeed, take a vacuum interface plaquette and change the gauge at one interface vertex to \(e^{itT}\).
Here \(T=\operatorname{diag}(1,-1)\), and one incident edge belongs to each side.
Transforming both sides keeps holonomy one.
Transforming only the core side leaves holonomy \(e^{\pm itT}\).
The reference-tree step, not the fluctuation-tree condition alone, excludes this mismatch in (5).
This is the distinction also needed in `inn-213.md`, Section 3.

The argument holds in each fixed frame.
Its reference denominator transforms with its numerator by the same change of variables.
Thus the frame average preserves this identity.
It supplies no additional gauge averaging.

## 4. The quadratic factors under simultaneous transport

These factors are covariant when their reference and their coordinates receive the same gauge action.
This statement also allows an independent current.

Write \(C_b,C_s,C_p\) for the adjoint actions on bare bonds, shell rows, and plaquette base points.
Let \(S\) be the real reference used in the patch form.
For a simultaneous real gauge action \(h\), the response and curvature derivatives obey
\[
 H_{S^h}C_s=C_bH_S,
 \qquad D_{S^h}C_b=C_pD_S.
 \tag{6}
\]
The second identity follows by differentiating plaquette covariance.
For the first, transform the linearised constraint and its Landau condition.
Their transformed solution is \(C_bH_SB\); uniqueness on the fixed slice identifies it with \(H_{S^h}C_sB\).
Here the shell-data derivative includes its node factors, as in `sa-2.8-terms.md` (1.2).
The six-propagator formulas at SA 10139–10158 give a separate instance of this conjugation algebra.
Their independent-current insertions transform at the same base sites.

The profile is scalar.
Hence the literal patch form of SA 17645 satisfies
\[
 q_{S^h}(C_sB)
 =\|\phi^{1/2}D_{S^h}H_{S^h}C_sB\|^2
 =\|\phi^{1/2}D_SH_SB\|^2=q_S(B).
 \tag{7}
\]
Its tree subspace is preserved because \(B|_{rT_0}=0\) is preserved.
This identifies the profile-weighted form itself.
It does not replace it by the regular relative precision.

The same calculation applies to a carried stage form \(\Delta\).
For its absolute gauge part, it requires block constancy on every contour read by that part.
Equation (1), differentiated twice, supplies exactly that condition under \(\widehat g\).
The relative regular part allows every real bare map.
Geometric masks commute with these adjoint actions.
Therefore a defined restricted inverse, Schur complement, or retained walk transforms by conjugation.
The carrier rule at SA 17550–17558 does not change under a gauge map.
Elimination densities \(z^{(j)}\) agree by the Haar change of variables in their constraint fibres.

All these statements hold at arbitrary admitted pairs with both readings defined.
They prove simultaneous transport, not the pair identification needed next.

## 5. Where the proposed identification still fails

An exterior transport is not yet the full action \(\mathbf p\mapsto\mathbf p^g\) on a member's argument.
Choose a non-centre site \(x\) strictly inside \(X\), away from all level-\(k\) tops.
Put \(g(x)=e^{i\epsilon T}\), with \(g=1\) elsewhere and \(T=\operatorname{diag}(1,-1)\).
Then \(\widehat g=1\).
Both \(\mathbf p=(1,0)\) and \(\mathbf p^g=(1^g,0)\) are admitted real flat pairs.
Their current is zero, and a real inverse gauge gives zero potential in every local chart.

Take the absolute stage contour from its centre to \(x\).
On the fibre direction at \(x\), its unscaled exponent is
\[
 f_\epsilon(s)=1-\cos(s-\epsilon),
 \qquad f_\epsilon''(0)=\cos\epsilon\ne1=f_0''(0).
 \tag{8}
\]
Choose \(s,\epsilon\) small enough that both gauge cutoffs equal one.
The coarse datum is unchanged.
Thus changing the coefficient's pair argument to \(\mathbf p^g\), while applying only \(\widehat g\) to its coordinates, fails.
This is the absolute-factor witness of `r-cov.md` (6), now with \(\widehat g=1\).
It does not contradict (1) or (7), which transform the reference simultaneously.

**Survival into a healed member is unresolved.**
It need not survive even into the complete unlocalised integrand.
For example, the carried-form rule at SA 17558 retains the exact identity
\[
 -\tfrac12\langle a,\Delta_{\rm old}a\rangle
 =-\tfrac12\langle a,\Delta_{\rm new}a\rangle
  -\tfrac12\langle a,(\Delta_{\rm old}-\Delta_{\rm new})a\rangle.
 \tag{9}
\]
Any dependence introduced solely through \(\Delta_{\rm new}\) cancels in this sum.
Likewise, (2) removes (8)'s finer gauge action when the remaining function is fixed.
Neither cancellation identifies a changed exterior-pair read of every localised summand.

## 6. What localisation must preserve

Here is the exact sufficient condition for memberwise invariance.
For each frame and history, use one measure-preserving substitution \(\xi\mapsto T_g\xi\) on the stored variables.
Let \(I(\mathbf p,\xi;s)\) denote the complete integrand with the localisation parameters of SA 17898–17924.
Require, on every restricted carrier and throughout that parameter domain,
\[
 1_{S_\omega}(T_g\xi)=1_{S_\omega}(\xi),\qquad
 I(\mathbf p^g,T_g\xi;s)=I(\mathbf p,\xi;s).
 \tag{10}
\]
The substitution must serve all factors sharing a stored variable.
It must also preserve the assigned currents and references in their pair reads.

Given (10), localisation preserves invariance.
Indeed, integration and each parameter evaluation commute with this fixed substitution.
Their differences, derivatives, and Cauchy brackets therefore commute too.
Products preserve the equality.
Each connected Mayer coefficient is a sum of such products with field-independent combinatorial coefficients.
Normal convergence then passes the equality to each \(\mathbf R'_\sharp(Y)\) of SA 17985–17997.
The fixed logarithm branch is preserved by its connected series.
Subtraction at the vacuum and later regular steps preserve the equality under their stated relative-factor inputs.
This covers both aged remainders and their later contributions to \(E^{(j+1)}\).

Equation (9) must cancel with the same localisation parameters and the same assignment to carriers.
Its endpoint identity alone does not prove this.
SA 17921–17924 says that the new argument, gauge factor, and stored data are formed together.
It does not give the intertwining identity (10) for their arbitrary pair reads.
The relative regular precision supplies simultaneous covariance, not this identification of the carried large-field formulas.

## Result

**Partial proof and correction of Route A.**
The stage draw and the jointly transported tree tests have the identities (1)–(5).
The entrance-tree correction is needed for the vacuum last-shell test.
The literal patch form and stage coefficients have simultaneous covariance, (6)–(7).

**The first input still open is (10): one compatible transport of all carried pair reads, before localisation.**
The absolute coefficient fails if that transport is replaced by the top lift alone, as (8) shows.
This is a coefficient counterexample, not a counterexample to a healed member.
Equation (9) explains a possible cancellation; its memberwise preservation remains unproved.
Thus this note does not establish (R-cov), \((\Gamma)\), or \((FG)\) for the full class.
The arguments are by Codex and have not been checked by the other model.
