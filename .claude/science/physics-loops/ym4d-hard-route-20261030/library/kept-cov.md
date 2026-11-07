# Kept forms and returning gauges
Provenance: Codex (GPT-6 family; requested effort max; runtime variant and effort not exposed); checkout `fc3c5409279f632d35175af569db649a3a79055c`; Sussman–Alpoge `31a47c543775`; research text, not an audit.

## 1. Scope and sources

This note addresses queue row 249 and the carried coefficients in (R-cov).
It uses Rule (REL′), including the operator of `gamma-bx.md`, Lemma 2.
The corrections in `gates/gamma-bx-check.md` govern that input.
Only real bare gauge maps are required.
The current remains an independent pair coordinate.

Credit Ethan Sussman and Levent Alpoge, with Claude and Codex as the authors of their text.
Their pinned outline supplies the chains, pivot charts, keep rule and carriage prescription used below.
SA references denote source lines located through `sa-index/` and then read in the source.
This note grants no scientific status.

## 2. What the outline supplies

SA 17550–17558 defines the kept chains by their cells.
It sketches the resulting local conditional form.
SA 17558 says the carried tests, gauge factors and delta functions “depend on no background”.
It makes the kept forms and elimination factors pair functions, “constructed once and for all”.
SA 17561–17564 compares two backgrounds, “both written in the new variables”.
These passages prescribe carriage but do not give its covariance calculation.

SA 8090–8098 gives covariance of the nonlinear constraint, (QC10).
SA 8165–8360 constructs its pivot chart and coarea density, (QC19)–(QC25).
Those chart identities are cited inputs, on their stated domains.
The missing step here is covariance of the retained coefficients and their returned reads.

## 3. The kept form

Fix the history geometry and all carrier labels.
Put \(p=(\mathbf U,\mathbf J)\) and
\[
 p^g=(\mathbf U^g,\operatorname{Ad}(g)\mathbf J),\qquad
 (D_j(g)a)(b)=\operatorname{Ad}(g(b_-))a(b).
 \tag{1}
\]
Here \(g\) on level \(j\) means its restriction to that level's sites.
Use the corresponding endpoint actions for each other operator space.
Every \(D_j(g)\) is orthogonal for the colour pairing.
Scalar cell masks commute with these actions.

The plain pivot map intertwines these actions by (QC10) and (QC19).
Rule (REL′) therefore gives
\[
 A_j(p^g)=D_j(g)A_j(p)D_j(g)^{-1},
 \qquad A_j=\mathsf C_V^{\mathsf T}
       (G_V^{(2),\mathrm{rel}}+\Delta_j)\mathsf C_V.
 \tag{2}
\]
This uses Lemma 2's operator inputs, including their independent-current continuation.
It does not substitute the physical current for \(\mathbf J\).
SA 10163–10198 specifies that continuation by covariant commutators and invariant pairings.

Compression preserves (2).
Taking the inverse on the compressed space preserves it too.
Thus the conditional resolvent has the same intertwining identity.
Lemma 2 supplies this identity for each walk term, with the same carrier.
For a chain \(W_1C_YW_2\), the intermediate actions cancel:
\[
 (D_0W_1D_1^{-1})(D_1C_YD_1^{-1})(D_1W_2D_2^{-1})
       =D_0(W_1C_YW_2)D_2^{-1}.
 \tag{3}
\]
The same calculation applies to each resolvent walk in \(C_Y\).
The pivot embeddings at either end also intertwine.
Hence the identity holds in the stored free coordinates and their constrained embeddings.

Let \(\varepsilon_{\mathfrak k}(\gamma)\) select a chain by SA 17550's cell rule.
Gauge changes leave every cell and \(\varepsilon_{\mathfrak k}(\gamma)\) fixed.
Sum (3) with these selectors and the Schur-complement signs.
Normal convergence, supplied by Lemma 2's walk input, gives
\[
 \boxed{\Delta^{\mathrm{loc}}_{\mathfrak k}(p^g)
    =D_j(g)\Delta^{\mathrm{loc}}_{\mathfrak k}(p)D_j(g)^{-1}.}
 \tag{4}
\]
Consequently its quadratic form is invariant when its stored coordinate transforms by \(D_j(g)\).
Rejected chains satisfy the same identity, carrier by carrier.
Scalar walk parameters preserve every identity before summation.
No positivity of the truncated kept form is used.

## 4. Elimination factors

Write \(K_V=Dq_V(0)\).
For the pivot \(b_c\), put \(J_c(V)=D_{a(b_c)}q_{V,c}(0)\).
Let \(D_E,D_F,D_C\) act on full bonds, free bonds and coarse rows.
Differentiating (QC10) gives
\[
 K_{V^g}D_E=D_CK_V,\qquad
 J_c(V^g)=\operatorname{Ad}(g(c_-))J_c(V)
                   \operatorname{Ad}(g(b_{c,-}))^{-1}.
 \tag{5}
\]
Both adjoint matrices have determinant one.
Thus \(\det J_c(V^g)=\det J_c(V)\), without any assumption of a constant gauge.
(QC19) now gives
\[
 h_{V^g}D_C=D_Eh_V,\qquad
 \mathsf C_{V^g}D_F=D_E\mathsf C_V.
 \tag{6}
\]

The residual \(R_V=q_V-K_V\) has the same covariance as \(q_V\).
Transform the equation \(d=R_V(t-h_Vd)\) by (5)–(6).
Its unique small solution is \(d_{V^g}(D_Et)=D_Cd_V(t)\).
Consequently
\[
 \Psi_{V^g}(D_Et)=D_E\Psi_V(t),\qquad
 D\Psi_{V^g}(D_Et)=D_E D\Psi_V(t)D_E^{-1}.
 \tag{7}
\]
The pivot diagonal blocks in (QC25) are therefore conjugate, separately for each coarse bond.
Their determinants and trace logarithms agree on the prescribed branches.
The Haar factor agrees because \(\operatorname{tr}(D_Ea)_b^2=\operatorname{tr}a_b^2\).

SA 7481–7487 separates these variable-dependent chart densities from \(z^{(j)}\).
Each \(z^{(j)}(c)\) is the inverse pivot determinant, with fixed scale and Haar constants.
The alternative normalization gives \((\det J_c)^{-1}=L^{-3}(\det\mathsf m_c)^{-1}\).
Thus
\[
 \boxed{z^{(j)}(c;p^g)=z^{(j)}(c;p).}
 \tag{8}
\]
The factor does not read \(\mathbf J\).
Equation (7) also proves covariance when a chart density remains attached to that factor.
These are algebraic holomorphic identities at complex pairs for real \(g\).
No absolute value of a complex determinant is introduced.
The coefficient calculations also hold for admitted complex frame changes on the same holomorphic branch.
Their adjoint matrices remain orthogonal for the bilinear trace pairing.
This assertion concerns coefficients, not cutoff functions.

## 5. Return to the recorded stored sites

Use one recorded frame for each stored coordinate.
Keep its original site when the determining tower changes.
Use the tree entrances of the chosen operation frame.
SA 7911 compensates background gauge changes on stored variables.
SA 7913 pins former tops carrying stored fields during later node corrections.
SA 17923–17925 forbids moving a stored field to successively higher tops.
These rules fix the endpoints of the return.
Different factors can use different backgrounds between those endpoints.
SA 6397–6400 sets each adapted contour to the identity at its recorded stored site.

First determine the action on the recorded data.
At a block draw with incoming action \(v\), let \(\ell\) lift its coarse restriction.
For the draw variable use
\[
 u'=\ell u v^{-1},\qquad
 (W^v)^{u'}=(W^u)^\ell.
 \tag{9}
\]
The map preserves Haar measure and the condition that \(u\) fixes coarse sites.
The absolute gauge factor is unchanged because \(\ell\) is constant on each gauge block.
Iterate (9) through the recorded stages.
Inside a level-\(k\) component this gives the lift \(\widehat g(x)=g(y_k(x))\).
Outside the component it retains \(\widehat g(x)=g(x)\).
For a reference tree rooted at \(o\), path cancellation gives
\[
 c_{S^v}(x)=v(o)c_S(x)v(x)^{-1}.
 \tag{10}
\]
Thus re-fixing the reference tree leaves \(v(o)\) throughout its interior.
The entrance bonds join all shell roots to this same root.
Together these rules define a real action \(d_g\) on each recorded coordinate.
It depends on \(g\), the history and the frame.
It does not depend on a background, an integration variable or a localisation parameter.

Here is the return calculation, including background-dependent returns.
For a native factor let \(\widehat p_f\) transform by \(h_f\).
Write its return as \(r_f\).
On a return contour from a recorded node \(y\) to a stored site \(x\),
\[
 r_f(x)=r_f(y)\tau_f(y,x),\qquad
 \tau'_f(y,x)=h_f(y)\tau_f(y,x)h_f(x)^{-1}.
 \tag{11}
\]
Contour means have the same endpoint identity by (QC10)'s underlying mean covariance.
At an exterior root, \(r_f=r'_f=1\) and \(h_f=g=d_g\).
An interior root inherits its action through (9) or (10).
Thus \(r'_f(y)h_f(y)=d_g(y)r_f(y)\) holds at the starting node.
Insert this into (11):
\[
 r'_f(x)h_f(x)
   =d_g(y)r_f(y)\tau_f(y,x)=d_g(x)r_f(x).
 \tag{12}
\]
The last equality is the block or tree lift defining \(d_g(x)\).
Repeat along the finite recorded tower.
At an active junction, the node factor is the datum divided by its reduced average (SA 7747).
Both transform at the prescribed endpoints, so this quotient preserves the same identity.
At a former stored top, later node corrections equal the identity there.
They therefore preserve (12).
This calculation uses the endpoints, not the value of \(\tau_f\).
It applies to both backgrounds of SA 17561.

The identity also survives the response interpolation.
In SA 10356–10410, every decoupled operator intertwines the site actions.
Its scalar walk parameters are unchanged.
Conjugation preserves the nonlinear products, logarithms and constraint residuals.
It therefore carries a solution of (R9) into a solution with transformed data.
Uniqueness of the stipulated small branch identifies the two solutions.
This uses the defining decoupled equations, not identities restricted to \(s=1\).
The multiplier and its independent-current increment transform at their own base sites.
The shift \((e^{i\eta\lambda H}\mathbf U,\mathbf J+\lambda\mathsf j)\) is consequently covariant for every allowed \((s,\lambda)\).
The recorded node returns still obey (12).
Their extensions away from stored sites need not coincide between factors.

Thus the action in `r-cov-reads.md` (5) satisfies
\[
 \boxed{r'_fh_fr_f^{-1}=d_g\quad\text{at every stored site read by }f.}
 \tag{13}
\]
Both endpoints are included for group coordinates.
Equality away from these sites is unnecessary.
For \(\widehat a_f=\operatorname{Ad}(r_f^{-1})a\), (13) gives
\[
 \widehat a'_f
  =\operatorname{Ad}((r'_f)^{-1}d_gr_f)\widehat a_f
  =\operatorname{Ad}(h_f)\widehat a_f.
 \tag{14}
\]
Apply (4) and (8) to this simultaneous transformation.
Every carried scalar read is unchanged.
The old and new quadratic reads therefore use the same transformed \(a\).
Their difference is invariant before any localisation.
This does not differentiate an absolute gauge factor at a newly substituted background.
That factor remains a function of the stored variables under SA's carriage rule.

## 6. The complete R integrand

Let \(T_g\) apply the actions just constructed to the recorded variables.
Group links use their endpoint actions.
Relative group variables and forms use initial-site conjugation.
Gauge draws use (9).
Each transformation preserves its Haar or Lebesgue measure.
The adjoint determinant is one, so no Jacobian remains.
Equations (6)–(7) let the same substitution pass through pivot elimination.

The stored tests are preserved.
Plaquette tests and fluctuation norms are unchanged by real conjugation.
The strip substitution at SA 17518–17526 commutes with it.
Indeed its response conjugates, and its cutoff depends only on the logarithm's norm.
Its Jacobian therefore transforms as the same scalar density.
Averaging constraints transform by conjugation at their coarse initial sites.
Their delta functions are invariant.
The absolute gauge factors are preserved by the block lifts in (9).

After (10), the shell field, core datum and reference receive the same root conjugation.
The tree condition and the \(B\)-test are unchanged.
The vacuum side of the last-shell test stays equal to one under that conjugation.
Its local critical orbit conjugates with its datum.
The reference numerator and denominator undergo the same substitution.
This proves the test identities within each frame; frame averaging is not used to repair them.

Equations (4), (8) and (13) preserve all carried pair-dependent factors.
Wilson traces are invariant.
Assume the activities read at this formation event are invariant.
The preceding identities then preserve every factor in its integrand.

Hence, in the notation of `r-cov-a.md` (10),
\[
 \boxed{1_{S_\omega}(T_g\xi)=1_{S_\omega}(\xi),\qquad
 I(p^g,T_g\xi;s)=I(p,\xi;s).}
 \tag{15}
\]
This is an identity of the complete integrand on its admitted domains.
It is independent of the splitting into a patch form and its compensating remainder.
For complex parameters, keep the real stored coordinates fixed.
The coefficient identities and the stipulated holomorphic continuation give the same equality.
Only the real action \(d_g\) acts on the tests.

The substitution does not depend on localisation parameters.
Thus evaluations, differences, derivatives and Cauchy brackets preserve (15).
Switches are scalar, and zero-field evaluation commutes with \(T_g\).
Carrier restrictions and frame sums preserve the identity too.
Each connected coefficient is a sum of invariant products.
Normal convergence preserves equality and the chosen logarithm branch.
Every R-formed member is therefore invariant under real bare gauge maps.
Regular steps also preserve invariant inputs under Rule (REL′).
Induct on formation events, starting with the bare Wilson action.
Every activity read at an event precedes its output.
This includes healed ancestors later filed into the regular action.

## Result

**Proof of the covariance step sketched by the outline, under Rule (REL′) and the named analytic inputs.**
The kept forms satisfy (4), chain by chain.
The elimination factors satisfy (8), coarse bond by coarse bond.
The recorded returns satisfy (13) on every shared coordinate.
This settles `r-cov-reads.md` (5) and `r-cov-a.md` (10), with the corrected carriage prescription.
No uncancelled noncovariant chain or factor remains under that prescription.

**First input still open:** admission of every lifted and stage core to the operator and response domains used here.
This is the domain input named in `gates/gamma-bx-check.md`, Section 4.
Covariance neither proves that admission nor a lower bound for the truncated kept form.
This proof is by Codex and has not been checked by another model.
It is not an audit and grants no status.
