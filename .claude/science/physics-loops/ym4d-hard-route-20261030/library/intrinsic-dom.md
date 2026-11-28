# Intrinsic tower domains

Provenance: Research text by Codex, based on checkout `1555d69a7` and the outline and complete account at `31a47c543775` by Ethan Sussman and Levent Alpoge, with Claude and Codex as authors of their text. This note grants no scientific status and is not an audit.

## 1. Target and source findings

Row 259 asks whether intrinsic domains remove (D4)'s old continuation-ball test.
Credit Tadeusz Balaban for the background and stage methods.
SA means [the outline](https://github.com/ethanwsussman/Yang--Mills-LLM-experiment/blob/31a47c543775/YM4_sketch_500.tex).
CA-I means [the complete account](https://github.com/ethanwsussman/Yang--Mills-LLM-experiment/blob/31a47c543775/theorem_0_complete_account_raw_I.tex).
Line numbers below refer to that revision. Both files were fetched once.
The index README, relevant chunk rows, their neighbours and obligation entries were consulted before the source excerpts.
The literature comparison is `lit-large-field.md:83–107`; its scalar, QED3 and YM3 routes do not supply this stage theorem.
The four requested Result sections leave actual stage admission open.

The source distinguishes these statements:

| Source | Clause read | Standing used here |
|---|---|---|
| SA 5696–5727 | (R5) uses \(\Phi_{M_e(U)}(i^{-1}\Log[M_e(\mathbf U)M_e(U)^{-1}])\), in its “chosen continuation domain”. | Definition, including existence. |
| CA-I 42679–42682 | Additional complex tower existence exceeds what “membership in the classes already presupposes”. | Explicit scope exclusion; not a nonexistence claim. |
| SA 9660–9667, 9693–9695 | Real uniqueness is “one orbit”; continuation is on \(\lVert B\rVert_\infty<r_B\). | Background theorem, sketched here. |
| SA 9832–9849, 9891–9911 | The multiplier contraction uses the slice, a right inverse, nonlinear bounds and a fixed small ball. | Sketch; more than a Hessian gap. |
| SA 9746–9755 | Tower existence follows from small simple conditions; the ambient version requires memberwise containment. | Sketched. `a3-close.md:74–99` gives a conditional rebuild and states its layered limitation. |
| CA-I 46053–46081, 47850–47984 | \(\mathsf A=\mathsf Q_{\mathbb B\mathbb B}\), \(\mathsf A\mathsf C=1\), \(\operatorname{Re}\mathsf Q\ge\gamma_0/4\) on \(\mathcal U(\varepsilon_1)\). | Conditional operator theorem. Its block identities have a written proof. |
| SA 6150–6158 | Stage substitutions require “analytic inclusion hypotheses”, with every preceding structure included. | Assumed inclusion; not a consequence of the order of stages. |

Thus a fixed-tower holomorphic branch is not a new missing result.
The proposed enlargement must cover the stage fields and preserve the consumer estimates.

## 2. The intrinsic branch: correction and local proof

**A critical field is not unique without a gauge condition.**
Take identity data and a nonnode site \(x\) in a nontrivial pillar.
Let \(g_t(x)=e^{itT}\), with \(T\ne0\), and let \(g_t=1\) elsewhere.
The pure gauges \(U_t(b)=g_t(b_-)g_t(b_+)^{-1}\) have identity averages at all determining nodes.
Every plaquette is identity, so the Wilson first variation vanishes.
For small nonzero real \(t\), these are distinct constrained critical fields arbitrarily close to \(1\).
This is also the orbit \(\{1^u\}\) in SA 9667; SA 9610–9616 defines its constraints and residual gauges.
Therefore neighbourhood size cannot give the requested uniqueness of a field.
Use the regular critical **orbit**, with SA's unique axial representative, or first solve on a normalized slice.
This correction does not rule out the intrinsic route.

Here is the quantitative implicit-function argument that the repaired route needs.
Fix a tower, a real regular datum and its real critical representative.
Use local holomorphic coordinates on a fixed gauge slice.
Let \(S(a)\) be the Wilson action and \(q(a)=b\) the actual average constraint in local row coordinates.
Include the exact reduced-datum map when using straightened rows.
Write \(x=(a,\lambda-\lambda_*)\), and set
\[
 F(x,b)=\big(DS(a)-Dq(a)^{\mathsf T}\lambda,\ q(a)-b\big),
 \qquad F(0,0)=0.
 \tag{1}
\]
All pairings and transposes are the declared bilinear ones.
The derivative in the unknowns is
\[
 L=\begin{pmatrix}H_*&-Q_*^{\mathsf T}\\Q_*&0\end{pmatrix},\qquad
 H_*=D^2S(0)-\lambda_*\cdot D^2q(0),\quad Q_*=Dq(0).
 \tag{2}
\]
The multiplier term matters; SA 9891 gives it as
\(\mathsf W_0\delta=\left.\frac d{dt}K_{t\delta}^{\mathsf T}\omega_0\right|_{t=0}\).

**Local lemma.** Use the weighted field, force and row norms appropriate to this tower.
Suppose \(F\) is holomorphic for \(\|x\|,\|b\|<R\), and
\[
 \|L^{-1}\|\le M,\quad
 \|F(0,b)\|\le A\|b\|,\quad
 \|D_xF(x,b)-L\|\le K(\|x\|+\|b\|).
 \tag{3}
\]
Take positive constants \(M,A,K\ge1\), increasing bounds if needed, then choose
\[
 r\le\min\{R/2,(4MK)^{-1}\},\qquad
 \delta\le\min\{r,r/(4MA)\}.
 \tag{4}
\]
For \(\|b\|<\delta\), define \(T_b(x)=x-L^{-1}F(x,b)\).
Integration of its derivative along a segment gives Lipschitz constant at most \(1/2\) on the closed \(r\)-ball.
Also \(\|T_b(0)\|\le MA\|b\|<r/4\), so that ball maps into the ball of radius \(3r/4\).
Iteration from zero has successive differences bounded by a geometric series with ratio \(1/2\).
Its limit solves (1); the same inequality gives uniqueness in the \(r\)-ball and
\(\|x(b)\|\le2MA\|b\|<r/2\).
The iterates are holomorphic and converge uniformly on smaller datum balls.
Passing their Cauchy formulas to the limit proves holomorphy. This proves the lemma by hand.
This gives a uniform radius when \(R,M,A,K\) are uniform in the stated norms.

The CA-I gap does not by itself supply (3).
CA-I 45294–45313 defines \(\mathsf Q=C_\flat^{\mathsf T}\Delta^{(k)}C_\flat\) on free fluctuation bonds.
CA-I 47931–47936 identifies this form with the physical one only on \(J=J(\mathbf U)\).
It is not the full saddle matrix (2).
That matrix also needs a bounded right inverse for \(Q_*\), the constrained inverse and the multiplier correction.
Its bounds must control the weighted maximum norms of the seven entries, not just an \(L^2\) norm.
SA 10139–10155 keeps these operators distinct.
Likewise, `a2-layers.md:665–680` starts with a complex regular pair and proves its fluctuation half-gap.
It does not make a previously inadmissible datum regular.

On admitted towers, the stronger local input already exists:
`a1-balaban.md:2459–2545` constructs the uniform datum ball, normalized representative and agreement on real overlaps.
Its displayed bound is \(\|A(B)\|_X\le C\|B\|_\infty\).
`wf-c.md:68–87` bounds collar maps, assuming \(\|w\|_*\le r_C\), by
\(|Q[\mathbf U]-1|\le C_C(\kappa+\|w\|_*)\).
These are used with their stated inputs, not promoted to proofs on every proposed stage domain.

**Agreement with (R5).** In a common normalized uniqueness ball, the intrinsic solution and (R5) solve (1).
They therefore coincide. Equivalently, their holomorphic germs coincide since their canonical real values coincide.
The identity theorem extends this equality over each connected overlap reached from an open real box.
It does not identify an arbitrary disconnected overlap or a second branch outside the uniqueness ball.
The next section supplies compatibility and full overlap agreement for its specified small radii.

The real centre is a reference used to select the branch, not a holomorphic argument inserted into it.
One freezes that reference to prove local holomorphy, then proves overlap agreement.
SA 5665–5670 writes \(P=(U,A',\mathbf J)\) with \(U\) real.
CA-I 45500–45507 requires both
\((\alpha_1,\alpha_0^J)\le\varepsilon_1(a_1^\oplus,a_0^\oplus)/4\)
and real-part membership in \(\mathcal U_{\mathbb R}\).
CA-I 45451–45481 defines that class by three real gauge conditions.
These clauses do not assert a real tower minimizer at every such point.
The phrase \(\operatorname{Re}P\) must use real local coordinates or the specified splitting; a matrix real part need not be group-valued.

## 3. A uniform intrinsic tube, on the admitted real datum class

Fix one determining set \(e\).
Use the admitted real datum class \(\mathcal R_e\) and the common radius \(r_B\) of `a1-balaban.md:2459–2545`.
Its real data have the margin required at lines 2527–2529.
Choose the common continuation radius with \(r_B\le1/8\) from the outset.
For \(V\in\mathcal R_e\), let \(\Phi_V\) be the canonical continuation on the full \(r_B\)-ball.
Choose
\[
 \delta\le\min\{1/40,r_B/40\},\qquad
 \mathcal T_e=\bigcup_{V\in\mathcal R_e}\{e^{iB}V:\|B\|_\infty<\delta\}.
 \tag{5}
\]
This union records no preferred real centre.

**Gluing proof.** Suppose the small patches at \(V_0,V_1\) intersect at
\(D_*=e^{iB_0}V_0=e^{iB_1}V_1\).
For any \(D=e^{iC}V_1\) in the second small patch,
\[
 DV_0^{-1}=e^{iC}e^{-iB_1}e^{iB_0},\qquad
 \|DV_0^{-1}-1\|<e^{3\delta}-1\le6\delta\le1/4.
\]
The product estimate follows by telescoping the three exponentials; apply it separately to each row.
Here \(e^t-1\le t/(1-t)\le2t\) for \(0\le t\le1/2\), by the exponential series.
The logarithm series gives \(\|\Log(DV_0^{-1})\|\le2\|DV_0^{-1}-1\|<12\delta\le r_B/2\).
Thus the entire second small patch lies in the first **large** continuation patch.
On a real open box about \(C=0\), the two maps give the same canonical real critical representative.
The identity theorem, one coordinate at a time, gives equality on the connected complex \(C\)-ball.
Hence
\[
 T_e(D):=\Phi_V\big(i^{-1}\Log(DV^{-1})\big)
 \tag{6}
\]
is well-defined and holomorphic on \(\mathcal T_e\), and solves the same constrained critical equations.
The radius \(\delta\) is independent of the number of rows, depth and volume whenever \(r_B\) is.
This proves an intrinsic **datum tube** construction from the admitted background theorem.
It uses local coordinates to prove holomorphy; membership does not remember any earlier centre.

**Agreement on every overlap with a full \(r_B\)-patch.**
Suppose \(D=e^{iB}V_0=e^{iC}V_1\), where \(\|B\|<r_B\), \(\|C\|<\delta\), and both centres are admitted.
Use SA 9720's real conjugation \(D^{\mathfrak c}=(D^*)^{-1}\).
Then \(D^{\mathfrak c}=e^{iB^*}V_0=e^{iC^*}V_1\), and \(\|D-D^{\mathfrak c}\|\le4\delta\).
The identity
\(e^X-e^Y=\int_0^1e^{(1-t)X}(X-Y)e^{tY}\,dt\)
gives this bound and the exponential bounds below.
On \(\|Z-1\|\le1/4\), subtracting logarithm series gives Lipschitz constant at most \(2\).
Both \(DV_0^{-1}\) and \(D^{\mathfrak c}V_0^{-1}\) lie there, since \(e^{r_B}-1\le1/7\).
Consequently \(\|B-B^*\|\le8\delta\).
Set \(B_t=(B+B^*)/2+t(B-B^*)/2\), \(0\le t\le1\), and \(D_t=e^{iB_t}V_0\).
This convex combination has \(\|B_t\|<r_B\), and \(\|D_t-D\|\le8\delta\).
Thus \(\|D_tV_1^{-1}-1\|\le10\delta\le1/4\), and its logarithm has norm at most \(20\delta\le r_B/2\).
The path stays in both full continuation patches and starts at a real datum.
The two continuations agree on a real open box there, hence on its complex neighbourhood.
The identity theorem along this path gives agreement at \(D\).
Therefore (6) equals (R5) wherever both are defined with these common-radius choices.

Real node gauges also preserve this construction.
Their action conjugates the datum tests and each row increment, preserving the admitted real class and its norm balls.
SA 9718 gives
\(\Phi_{V^v}(\operatorname{Ad}(v)B)=\Phi_V(B)^{\tilde v}\), with \(\tilde v\) the specified lift.
Insert this identity in (6): \(T_e(D^v)=T_e(D)^{\tilde v}\).
Thus native real-gauge covariance holds on the tube. This gives no invariance of its norm bounds under arbitrary complex gauges.

There is also a concrete field domain already covered by this construction.
Under `a3-close.md:74–87`'s single-level hypotheses, its averaging estimate gives
\[
 \|i^{-1}\Log[M_e(e^{i\eta_pw}U)M_e(U)^{-1}]\|_\infty
 \le2L^{d-p}\|w\|_\infty.
 \tag{7}
\]
Here \(d\le p\) is the tower depth, and \(M_e(U)\in\mathcal R_e\) requires its stated real-regularity margin.
Thus \(\|w\|_\infty<\min\{c_T,\delta/2\}L^{p-d}\) puts the datum in (5), uniformly in depth.
No earlier centre occurs in (7).
This is a conditional consequence of the existing averaging and background results, not a new proof of those results.
The full layered stage class is not the single-level class in this argument.
`a3-close.md:99` expressly leaves its layered case open.

## 4. Proposed absolute stage domains

Keep the geometric records of `stage-thm.md:58–63`: levels, regions, both erosion rules, truncations and preceding structures.
Discard each record's old real reference and its old (R5) ball.
On an open set where every required \(M_e(\mathbf U)\) lies in (5) and \(M_e(U)\in\mathcal R_e\), use \(T_e=T_e(M_e(\mathbf U))\).
For a record of level \(s\), and tower \(e=(Z,p,d)\), impose the seven normalized bounds
\[
 \begin{array}{c|c}
 q_a(P)&r_a\ \text{before the layer lift}\\\hline
 \eta_s^{-2}|\partial\mathbf U-1|&\alpha_{0,m}\\
 L^{s-p}\eta_p^{-2}|\partial T_e-1|&\alpha_{0,m}\\
 |\mathbf J|&\alpha_{0,m}\\
 L^{s-p}L^{2(p-d)}|J(T_e)|&\alpha_{0,m}\\
 \eta_s^{-2}|\partial U-1|&\alpha_{0,m}\\
 |A'|&\alpha_{1,m}\\
 |\nabla_UA'|&\alpha_{1,m}
 \end{array}
 \qquad q_a(P)<c_n(m)r_a^{\rm lift}.
 \tag{8}
\]
Use the radius index and unit conversion of each record, including the \(j\)-indexed case of `stage-thm.md:40–43`.
CA-I 49595–49624 gives these seven entries and puts the lift outside their entire bracket.
Read tower entries on the prescribed erosion, and also with \(\mathbf U=U\), as SA 5707–5720 requires.
Keep one real splitting for all records, and keep \(\mathbf J\) independent of \(J(\mathbf U)\).

Also require the real gauge witnesses of CA-I 48472–48477:
\[
 U^u=e^{i\eta A},\quad
 \ell_i|A|,\ \ell_i^2|\nabla^\eta A|
 <L_0^{2e(Q)}BM\alpha_{0,i}\quad\text{on }Q\cap X.
 \tag{9}
\]
Use all four cube families in CA-I 48527–48565, listed in `stage-thm.md:122–127`.
These witnesses are real; they are not prescribed returning gauges.
Their bounds do not acquire the coefficient \(c_n\) (`stage-thm.md:113–118`).
Call this domain \(D_n^{\rm int}\), and take its pair image with the required tie.
There is no old-chart test (4) of `stage-thm.md`.

**First open input.** Prove that the requested lifted, layered stage fields lie in such an open set.
For every inherited determining set, prove absolute admission to (5), with uniform room and compatible representatives.
This must hold on the full earlier-parameter domain and the required interpolation discs.
The seven bounds cannot establish existence of the tower quantities that occur in those same bounds.
Defining (8) only where (6) exists is legitimate, but does not prove coverage of the required fields.
The local operator theorem and the single-level estimate (7) do not complete this step.

## 5. What inclusion follows, and where transport remains

Fix the clause roster, units, lifts and real splitting.
For the **same field**, \(c_{n+1}(m)\le c_n(m)\) gives \(D_{n+1}^{\rm int}\subset D_n^{\rm int}\).
Each inequality in (8) only becomes weaker; unchanged gauge witnesses still work.
This proves literal nesting without old-chart transport.
It is conditional on using the same intrinsic functions and all the earlier geometric records.

An actual stage requires a different statement.
Let \(S_n(P;\zeta)\) be a previous consumer's argument expressed in the new variables.
The parameter \(\zeta\) includes earlier parameters, fluctuations, returns and switches.
CA-I 53806–53814 replaces the determining member at level \(j+1\).
SA 17564 requires the backgrounds to be “both written in the new variables”.
Thus neither their equality nor \(S_n(P;\zeta)=P\) follows from an intrinsic definition.

`d4-stage.md:24–51` gives, for fixed lifts and retained distinct marks,
\[
 d_n(m)=c_n(m)-c_{n+1}(m)
 =\frac{g_k(m)}{2N}+\beta_R\sum_{l\in E_n}2^{-|m-l|},
 \qquad \sum_n d_n(m)\le g_k(m)/2+3\beta_R.
 \tag{10}
\]
If, for every old read and every clause, the actual map satisfies
\[
 q_a(S_n(P;\zeta))\le q_a(P)+\epsilon_{n,a},\qquad
 \sup_{P,\zeta}\epsilon_{n,a}<d_n(m)r_a^{\rm lift}/2,
 \tag{11}
\]
then
\[
 q_a(S_n(P;\zeta))<c_n(m)r_a^{\rm lift}-d_n(m)r_a^{\rm lift}/2.
 \tag{12}
\]
This proves the numerical part of stage inclusion, with half the margin left.
The proof is addition of the two bounds. It works for each earlier stage by composition when every inclusion has the full parameter quantifiers.
Equation (10) supplies an allowance, not the estimate (11).
For example, \(|z|<c-d\), with \(0<d<c\), has the expected coefficient margin.
The entire map \(S(z)=z+2d\) sends \(z=c-d-\epsilon\), \(0<\epsilon<\min\{d,c-d\}\), outside \(|z|<c\).
This refutes the inference from margin and holomorphy alone; it is not a Yang–Mills counterexample.

Transport remains at the **actual argument** \(S_n\), not necessarily at an old logarithmic datum.
Its old and new towers solve different constraint problems.
Their absolute values still need a comparison on one source domain.
`wf-c.md:36–47,68–75` supplies a comparison only under its fixed collar geometry and small-potential hypotheses.
The conditional A3 derivative in `dec-field.md:247–279` reads “Assume [PW], [NL]” on an admitted fixed system.
Neither statement estimates the full stage map merely by changing the definition of its target domain.

Returns also act on the independent current and stored fields.
For complex \(g\), \(\|gXg^{-1}\|\le\|g\|\|g^{-1}\|\|X\|\); the absolute norms need that factor controlled.
SA 5729–5736 says the core is “not saturated” under complex gauges.
If the real factor or cube family changes, (9) needs a new witness or a restriction argument.
Those conditions have no expenditure supplied by (10).

## 6. Consumers

| Consumer | What the intrinsic replacement must supply |
|---|---|
| B4 | SA 4006–4012 requires holomorphy on the “product box”, with a “majorant independent” of label count. It specifies no particular tower centre. A holomorphic tower alone does not give either assertion for the step. |
| (LOC) and Boolean corners | SA 5813–5825 states a “domain-inclusion hypothesis”: every interpolated argument stays in the core for \(\lvert\nu\rvert<\varrho_F>1\), with separate inner and removed radii. SA 5830–5838 reads every Boolean corner. SA 17907–17925 also forms the argument, gauge and stored data together. Intrinsic domains are acceptable if these complete maps enter them. |
| (R-cov) | Use relative kept forms as pair functions. `kept-cov.md:45–83,171–214` gives their intertwining and return identities. `gates/kept-cov-check.md:31–39,83–92` retains native-orbit covariance and domain admission as inputs. Section 3 supplies native real-gauge covariance on the intrinsic tube; admission of the actual returned reads remains necessary. |
| Cauchy estimates | They require an admitted parameter polydisc and its supremum bound. SA 5927–5942 still uses the coefficient chart \(\mathsf e_X(A,J)=(e^{i\eta_jA},J)\) at \((1,0)\), with a fixed-gauge linear response. This is a local coordinate, not an old (R5) membership test. |
| Majorants | SA 18108–18128 places “both suprema” over the admitted pair domain inside the stored-field integral. A larger intrinsic domain needs the same bound on its larger supremum. SA 6166–6173 also keeps near variables Borel and far variables and switches jointly analytic. |

For clarity, the Cauchy claim has a direct proof.
Let \(H(s,\nu)=f(S(P;s,\nu))\) be holomorphic and bounded by \(M_f\) on
\(|s_\Delta|<R_s=e^{\bar\kappa}\), \(|\nu|<\varrho_F\).
The function \(H(s,\nu)-H(s,0)\) vanishes at zero and is bounded by \(2M_f\).
Schwarz's lemma gives \(|H(s,1)-H(s,0)|\le2M_f/\varrho_F\).
At each point of the real unit cube, Cauchy circles of radius less than \(R_s-1\) lie in the source polydisc.
Apply Cauchy's formula in each differenced variable and integrate over that cube.
Taking radii up to \(R_s-1\) gives the Boolean bracket bound
\[
 \frac{2M_f}{\varrho_F}(R_s-1)^{-|\mathcal K|}.
 \tag{13}
\]
This is SA 5849–5861's calculation. The domain enters only through the holomorphic pullback and its bound.

Existing activities do not automatically extend when their tower map extends.
For instance, \((3/2-z)^{-1}\) is bounded and holomorphic on \(|z|<1\), but has a pole in \(|z|<2\).
Thus agreement with (R5) preserves existing values; it does not prove all new activity domains or their majorants.
One must construct the activities on the intrinsic domains and reproduce the stated bounds.
The explicit chart clause is SA 5706 and 5724–5727, built into the original core definition.
The consumers above can use a replacement core, provided their inclusion, tie, locality, stored-slot and norm hypotheses are proved there.

## Result

**Partial proof (first open input); an attempted replacement of the assumed stage-domain input.**
Literal uniqueness without gauge fixing is false, by the pure-gauge family in section 2.
After that correction, sections 2–3 prove a quantitative local implication and glue the admitted canonical branches into an intrinsic datum tube.
They agree with (R5) on every overlap for the stated common-radius choices.
Sections 4–5 define the proposed seven-entry domains and prove nesting for an unchanged field, plus inclusion conditional on (11).

The first open input is uniform intrinsic-tube coverage for the full lifted, layered stage family in section 4.
Even with that input, the actual stage needs (11), the changed gauge witnesses and stored-slot admission.
The checked covariance identities and Cauchy algebra do not replace those estimates.
No claim is made that the intrinsic route fails, or that an actual stage exits its domain.
This note closes no full (D4), B4 or (LOC) statement.
All new arguments are by hand. This text is not yet checked by the other model.
