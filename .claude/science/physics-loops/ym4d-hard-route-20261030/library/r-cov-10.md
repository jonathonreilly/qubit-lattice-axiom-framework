# r-cov-10: one transport for carried pair reads
Provenance: Codex (GPT-6 family; requested effort max; exact runtime variant and effort not exposed); checkout `313310d007bc5903fecff474fc508cc11eb2cd4f`; Sussman–Alpoge `31a47c543775`; research text, not an audit.

## 1. Target and source

The target is (10) of `r-cov-a.md`, for each fixed frame and history.
One substitution must serve every factor that shares a stored variable.
It must respect each factor's assigned reference and current throughout localisation.
This would supply (R-cov) for both healed terms and their later regular descendants.

Credit Ethan Sussman and Levent Alpoge, with Claude and Codex as the authors of their text.
Their pinned `YM4_sketch_500.tex` supplies the operation, carriage rules, and localisation used below.
Line numbers refer to that version.
The earlier notes prove ingredient identities under their named background inputs.
They do not yet prove compatibility between different pair reads of shared data.

## 2. What the outline fixes

SA 17558 keeps the stored tests independent of the later background.
It evaluates the carried forms at the current pair.
Changing that pair also creates a difference of the old and new forms.
Both forms read the same stored field.

SA 17922–17923 says: “The new argument, its gauge factor and its stored data are formed together.”
SA 17930–17936 uses the background generated from the new argument's averages inside a healed box.
SA 6160–6172 assigns stored bond forms their adjoint action at their initial sites.
SA 19420 and 19424 require invariance of the resulting entries and island factors.
These passages prescribe carriage and assert covariance.
They do not supply a common substitution for its arbitrary pair reads.
The required identity is assumed; its proposed construction is sketched.

The prior search, `lit-large-field.md`, Section 1, records no healing operation in their YM3 or QED3 manuscripts.
No proof of this step is imported from those manuscripts.

## 3. A necessary compatibility test

Let two carried quadratic reads share a stored field \(a\):
\[
 q_\sharp(p,a)=\langle a,\Delta(p_\sharp)a\rangle,
 \qquad q_\flat(p,a)=\langle a,\Delta(p_\flat)a\rangle.
 \tag{1}
\]
Suppose \(p_\sharp=p_\flat\) at \(p\).
Their difference then vanishes for every stored configuration.
Any common transport preserving both reads must give
\[
 (q_\sharp-q_\flat)(p^g,T_g\xi)=0.
 \tag{2}
\]
If the transformed difference is nonzero on a set of positive measure, no measure-preserving substitution can satisfy (2).
Indeed, the inverse image of that set has the same positive measure.
This excludes nonlinear substitutions too.
Failure of one proposed linear transport would be weaker.

The same test applies to an interpolated integrand \(K(p,\xi)e^{-\lambda(q_\sharp-q_\flat)/2}\), where \(K\ne0\).
Divide its transport identities at real \(\lambda\) and at zero.
Equality for all \(\lambda\) forces (2).
This argument requires identifying that interpolation in the complete integrand.

## 4. The flat witness and its missing identification

The known coefficient witness supplies a failed *uncompensated* pair read.
It does not supply the requested carried-read counterexample.

Choose a node-free level-\(j\) block with centre \(y\).
Choose an interior site \(x\ne y\).
Put \(T=\operatorname{diag}(1,-1)\).
Let \(g_\epsilon(x)=e^{i\epsilon T}\), and let \(g_\epsilon=1\) at the other level-\(j\) sites.
Lift this map constantly through the level-\(j\) pillars.
Take \(p_0=(1,0)\) and \(p_\epsilon=p_0^{g_\epsilon}\).
Both pairs are flat, with zero current.
Every coarse average above level \(j\) equals one.
A real inverse gauge gives zero local potential, so both pairs meet the flat core conditions.

Vary the gauge at \(x\) from \(e^{i\epsilon T}\) to \(e^{i(\epsilon-t)T}\).
The contour from \(y\) to \(x\) becomes \(e^{i(t-\epsilon)T}\).
Its absolute gauge exponent and quadratic form are
\[
 F_\epsilon(t)=1-\cos(t-\epsilon),\qquad
 q_{p_\epsilon}(a(t))=\cos\epsilon\,t^2.
 \tag{3}
\]
Here \(a(t)\) is the corresponding unscaled bond fluctuation.
The commuting configuration makes its logarithmic coordinates linear in \(t\).
Choose \(\epsilon,t\ne0\) sufficiently small that the local cutoffs equal one.
This is the absolute contour coefficient of SA 10200–10204.

On this flat orbit, let \(\Pi p=(1,0)\) be the pinned axial background at the common higher datum.
Consider the uncompensated read
\[
 D(p,a)=q_{\Pi p}(a)-q_p(a).
 \tag{4}
\]
It has \(D(p_0,a)=0\) for every \(a\), but
\[
 D(p_\epsilon,a(t))=(1-\cos\epsilon)t^2>0.
 \tag{5}
\]
Continuity gives a nonzero difference on an open set of chart variables.
Give that chart a measure with positive density on this set.
Section 3 excludes any common measure-preserving substitution for these two reads on a support containing the set.

**The identification of (4) with an actual carried difference is missing.**
SA 17930–17936 requires the gauge relating the generated background to the argument.
SA 5762–5811 also retains the node gauge and the independent current in the response.
Replacing that complete read by \(\Pi p\) discards required data.
For this flat example, returning \(\Pi p_\epsilon\) by \(g_\epsilon\) gives \(p_\epsilon\) itself.
Thus the mismatch of references in (4) can disappear.
The coefficient witness cannot establish that no substitution serves the prescribed reads.

## 5. Survival into a healed member

No surviving member counterexample has been identified.
The carried-form correction has the exact identity
\[
 -\tfrac12q_\flat(a)-\tfrac12\bigl(q_\sharp(a)-q_\flat(a)\bigr)
 =-\tfrac12q_\sharp(a).
 \tag{6}
\]
Hence a defect caused solely by the intermediate reference cancels before localisation when these pieces are recombined.
This cancellation does not identify their separate parameterised reads.
SA 17985–17997 forms a healed member only after integration and the connected expansion.
Neither (5) nor (6) computes such a member.
Survival of an actual discrepancy therefore remains unresolved.

## Result

**Correction to the uncompensated reading (4). Row 243 remains open.**
Equations (4)–(5) rule out common transport for the uncompensated read.
They do not identify that read with the outline's prescribed carried read.
The returning gauge cannot be omitted.
No proof of (10), or counterexample to its actual integrand, is established here.

**First input still open:** identify the complete pair, current, reference, and coordinate read for each carried factor.
For factors sharing a stored variable, their induced transports must agree throughout the localisation parameters.
The ingredient identities in `r-cov-a.md` do not establish that agreement.
Consequently (R-cov), (Γ), and (FG) remain open for the full R-formed family.
This research calculation grants no status and has not been checked by another model.
