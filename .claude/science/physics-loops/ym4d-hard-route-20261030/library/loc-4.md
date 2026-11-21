# loc-4: one-move admission and the carriage gap
Provenance: Codex / GPT-6 (serving variant and configured effort not exposed; assigned effort max); checkout `76cc170178f7010b0aa5cadc8de06dec33dd74c4`; Sussman–Alpoge commit `31a47c543775`; research text, not an audit; grants no status.

Credit: Ethan Sussman and Levent Alpoge, with Claude and Codex as authors of their text, for the cited constructions. Sources at the pinned commit: [YM4](https://github.com/ethanwsussman/Yang--Mills-LLM-experiment/blob/31a47c543775/YM4_sketch_500.tex), [YM3_I](https://github.com/ethanwsussman/Yang--Mills-LLM-experiment/blob/31a47c543775/YM3/YM3_I.tex), and [QED3](https://github.com/ethanwsussman/Yang--Mills-LLM-experiment/blob/31a47c543775/QED3/QED3.tex). Balaban supplies the underlying background-localisation method. All arguments below are written mathematics.

## 1. Source check

This note partially repairs our `loc-3.md`, following `gates/loc-3-check.md`. It addresses queue row 226 and (LOC).

The outline assumes domain inclusion at SA L5813–5824. It says: “Every occurrence of (R10) requires a domain-inclusion hypothesis”.
SA L17904–17918 sketches its use for carried terms. It invokes “the response and hereditary-domain estimates”.
SA L5826–5855 proves the bracket algebra conditional on that inclusion and the response properties.
Thus bracket algebra supplies no admission theorem.
SA L6149–6157 also retains stage inclusion as an analytic hypothesis for the layered spaces.
Those spaces quantify over preceding structures, with their own radii and tower assignments.

The earlier manuscripts keep the same distinction.
YM3_I L48576–48658 proves strip transfer after assuming a complex ball in the local function's domain.
QED3 L8723–8788 proves total-connection inclusion by explicit radius inequalities.
QED3 L9504–9546 proves room after scaling by comparing every threshold.
These are detailed conditional proofs. Neither supplies the missing YM4 history invariant.

`red.md` adopts the active independent-current response. Its named row, walk and current bounds remain inputs.
Its scalar-gradient correction does not supply domain inclusion.
`d3-local.md` supplies conditional locality of new terms. Regional Gaussian matrices and coherent logarithms remain separate inputs.

## 2. What the admission results supply

- `o1-decoupled.md`, Theorem I, admits the inner triple
  \(P_{\rm in}(B)=(1,\mathcal H(B),J(e^{i\eta_j\mathcal H(B)}))\).
  It requires \(X\subset T'_j(\square_0)\), \(\|B\|<r_I\),
  \(e^{C_g\|B\|}|\phi(B)|_X<\alpha_{0,j}\), and \(C_{\mathcal H}\|B\|<\alpha_{1,j}\).
  Its restriction identity admits every lower tower. It does not identify a general shifted triple with an inner triple.
  Its check accepts this implication. Section 4.5's radius substitution and coupling floor were wrong as printed.
  Use the check's envelope \(\bar a=\max(a,\alpha_0^{\rm input})\) and floor \(x_i\ge\max(C_x,e^{2q},e^2)\).
- `a3-close.md`, Lemma T, bounds every tower quantity by \(K^\sharp(b_0+b_1^2)\), with its stated unit factors.
  Thus simple radii \((b_0,b_1)\) suffice when \(K^\sharp(b_0+b_1^2)<a_0\) and \(b_1<a_1\).
  A half-radius hypothesis alone does not imply this inequality; the Schwarz argument below avoids that loss.
  The check cited by `wf-c.md` for Lemma T explicitly excludes `a3-close.md` Section 2.
  Do not attribute a check of T to `gates/a3-close-meet-gate.md`.
- `wf-c.md`, Theorem A, treats its specified curves from half-radius inputs.
  It assumes \(\alpha_k\le C_\alpha\alpha_{0,k}\) and its listed response and tower estimates.
  It admits the generated inner triples on the full complex parameter disc, with margin at least \(1/5\).
  `b4-step.md` Section 0 checks precisely this implication.
  It does not state admission for every carried composition or every stage.
- `bx-fix.md`, Lemma 5 and (A2-H), add the Hölder clauses for those inner triples.
  They require \(C_{\mathcal HH}\|B\|<a_1\).
  `gates/bx-fix-check.md` accepts these implications but rejects Proposition I's unrestricted preservation claim.
  Long members retain outer evaluations. The check also rejects replacing a pair Taylor ball by a critical-map image.

## 3. Proposition O, geometry only

Retain the collared-nest hypotheses of `loc-3.md`, Proposition O.
For each seam component \(S\) initially outside \(\operatorname{int}W_0\), there is one first admission index \(n_S+1\).
Then
\[
(n_S+1)\mu_W\ge\max_{x\in S}d_t(x,W_0),\qquad
d_{\mathbf B}(b,W_{n_S}^c)\le d_{\mathbf B}(b,S).
\]
Lemma S makes admission all-or-nothing. Nestedness gives the first index.
Iterating \(W_{n+1}\subset W_n^{+\mu_W}\) proves the first inequality.
Before admission, \(S\subset\overline{W_{n_S}^c}\), which proves the second.
These facts give no lower bound on the response.
They neither refute (N2′) nor produce a joint history from separate open failure events.

## 4. Admission that does follow

**Inner curves.** Let \(Q(s,t,\nu)=P_{\rm in}(B_{t,\nu}(s))\) be exactly a curve of Theorem A.
Retain its hypotheses and the repaired constants above.
Increase \(C_{\mathcal H}\) to \(\max(C_{\mathcal H},C_{\mathcal HH})\) in the potential ceiling.
For \(|s_\Delta|<e^{\bar\kappa}\), \(0\le t\le1\), and \(|\nu|<c_\nu/s_k\),
\[
 Q(s,t,\nu)\in\mathcal U_j^H(X;\alpha_{0,j},\alpha_{1,j},\alpha_{0,j}).       \tag{1}
\]
Here \(s_k<c_\nu/2\), so the scalar disc has radius greater than two.

Indeed, Theorem A puts the input clauses below \(5/8\) of their radii.
The endpoint and residual-gauge bounds give
\[
 e^{C_g\|B\|}|\phi(B)|_X
 \le (9/8)^2(5/8)\alpha_{0,\ell}L^{-2(\ell-j)}.
\]
At age zero the coefficient is \(405/512<4/5\).
At positive age, the repaired slow-radius bound and \(L\ge3\) make it smaller than \(1/2\).
Theorem I transfers this bound to every allowed \(Z,p,n\) and both tower rules.
The real factor is one. Lemma 5 bounds the complex Hölder clause below half its radius.
This proves (1), including all Boolean corners and a fixed margin.
Consequently any bounded holomorphic partial map on that core can be composed with this particular \(Q\).
This statement concerns the prescribed Landau representative. It asserts no additional complex gauge descent.

**Single-layer outer curves.** Assume \(0<a_0\le a_1\), \(a_1^2\le C_0a_0\), and sufficiently small radii.
Fix the geometric and theorem constants before choosing those radii below the auxiliary chart ceilings.
Let \(P\) lie in the half-radius \(\mathcal U_j^H\) core.
Suppose \((\mathbf H_s,\mathsf j_s)\) is holomorphic for \(|s_\Delta|<e^{\bar\kappa}\), with
\[
 \sup_s\bigl(\|\mathbf H_s\|_{1,\alpha_H}+\|\mathsf j_s\|_\infty\bigr)\le b.
\]
Use local units and the witnessing real gauges for this norm.
There is a fixed \(c>0\) such that
\[
 P\dotplus\nu(\mathbf H_s,\mathsf j_s)\in\mathcal U_j^H(X;a_0,a_1,a_0)
 \quad\text{for }|\nu|<\varrho:=ca_0/b.                         \tag{2}
\]
Require \(b<ca_0\), so \(\varrho>1\). A zero response needs no restriction.

Here is the tower argument from `wf-room.md` Section 3, using Lemma T.
Plaquette multiplication and the small logarithm series bound simple field changes by \(C|\nu|b\).
On an auxiliary disc \(|\nu|<R=da_0/b\), choose fixed \(d\) so those fields satisfy radii \((2a_0,2a_1)\).
Lemma T makes each normalized tower quantity \(f(\nu)\) holomorphic there, with
\[
 |f(\nu)|\le A a_0,\quad A=K^\sharp(2+4C_0),\qquad |f(0)|<a_0/2.
\]
Schwarz's lemma, applied through norm-one linear functionals, gives
\(\|f(\nu)-f(0)\|\le(A+1/2)a_0|\nu|/R\).
Choose \(c<d/[4(A+1/2)]\).
Then every tower clause stays below \(3/4\) of its radius.
This fixes an arbitrary clause and uses uniform constants; it does not sum over towers.
Decrease \(c\) for the simple field clauses and \(|\mathbf J+\nu\mathsf j_s|<3a_0/4\).
Their logarithms remain in the auxiliary chart.

It remains to check the added Hölder clauses.
Fix each real gauge witnessing the half-radius Hölder core of \(P\).
Let \(h=\nu\mathbf H_s\), and suppose its ordinary \(C^{1,\alpha_H}\) norm in these gauges is at most \(\epsilon\).
On the small logarithm chart,
\[
 \|A'\boxplus h-A'\|_{1,\alpha_H}\le C\epsilon.
\]
The constant is independent of the mesh.
To see this, use the discrete product rule on each fixed-size cube.
It gives \(\|fg\|_{1,\alpha_H}\le C_D\|f\|_{1,\alpha_H}\|g\|_{1,\alpha_H}\).
The exponential and logarithm series converge in this norm on a fixed small ball.
Their difference at \(h\) and zero has a factor \(h\) in each monomial.
Summing their absolute series proves the displayed norm estimate.
If \(C\epsilon<a_1/4\), the complex Hölder clause remains below \(3a_1/4\).
The real clauses do not change.
Since \(a_0\le a_1\), another fixed reduction of \(c\) gives this bound throughout (2).
This proves (2), with margin for every simple, tower and Hölder clause.
Lemma 0 and Proposition PH of `bx-fix.md` supply the response's covariant Hölder estimate under their named inputs.
The conversion to these gauges costs a fixed constant.
Indeed, \(\nabla^{\mathbf U}h=\nabla h+K h(\cdot+\eta e_\mu)\), where \(K=(\operatorname{Ad}(\mathbf U_\mu)-I)/\eta\).
In the witnessing gauge, the potential of \(\mathbf U\) has bounded \(C^{1,\alpha_H}\) norm.
The exponential series therefore bounds \(K\) in \(C^{\alpha_H}\), uniformly in \(\eta\).
Straight transports differ from identity by at most a constant times their length.
The product rule and \([h]_{\alpha_H}\le C_D\|\nabla h\|_\infty\) now give the ordinary estimate.
Thus \(\epsilon\le C|\nu|B\|B'\|\) in local units, with \(B\) the uniform response constant.
If the complete response bound is \(b\le C e^{C\bar\kappa}L^{-(k-j)}\delta(\theta_k)\), (2) gives (R11).
The current bound must be included in this estimate, with its own unit conversion.
Neither (1) nor (2) proves that every carried argument reaches the required input core.

## 5. The remaining composition input is necessary

For a carried partial map \(F\), let \(D_F\) be its assigned domain, including its earlier substitutions.
The missing assertion is
\[
 Q_m(s,\nu;P):=(\rho_XP)\dotplus\nu\mathfrak h_m(s;P,B')\in D_F
 \quad\bigl(|s_\Delta|<e^{\bar\kappa},\ |\nu|<\varrho_F>1\bigr).       \tag{D4}
\]
It must hold on the entire next input domain, at every move and stage.
It must include stored arguments, gauges, logarithm charts, and all defining compositions of \(F\).
The inclusion must depend only on the assigned read set, so equal traces give equal partial-map domains.
For bounds, retain a finite supremum \(M_F\) on this parameter domain.
The radius in (R11) additionally requires its stated quantitative lower bound for \(\varrho_F\).

Here is an explicit failure of deriving (D4) by repeating a one-move admission statement.
This is a scalar composition counterexample, not a Yang–Mills response counterexample.
Fix \(R=e^{\bar\kappa}>1\) and an integer \(N>8R\).
On \(D=\{|z|<1\}\), define the bounded holomorphic partial map
\[
 F(z)=\sqrt{1-z},\quad F(0)=1,\quad |F(z)|<\sqrt2,\qquad
 Q_\pm(s,\nu;z)=z\pm\nu s/N.
\]
Each move sends \(|z|<1/2\), \(|s|<R\), \(|\nu|<2\) into \(|z|<3/4\).
Thus every individual move has uniform complex room.
Apply \(N\) consecutive pairs \(Q_+,Q_-\), starting at zero.
At the physical parameters \(s=\nu=1\), the intermediate arguments alternate between \(1/N\) and zero.
Every physical argument lies in the half disc.
At the mixed corner with every plus parameter one and every minus parameter zero, the composite argument is
\[
 z_*=N/N=1\notin D.                                            \tag{3}
\]
So the carried evaluation \(F(z_*)\) is not defined.
There is no holomorphic extension through that point.
Such an extension would satisfy \(F(1)=0\) and \(2F(1)F'(1)=-1\).
In the would-be full Boolean bracket, only this corner attains the positive displacement one.
Its square-root singularity cannot cancel against the other corner functions, which extend near zero after translation.
Thus resummation at physical parameters cannot repair the individual partial maps.

For the actual construction, a domain invariant must exclude this accumulation.
One sufficient form is a clause-by-clause budget on every defining composition:
\[
 \|\mathcal R_a(Q_0)\|\le(1-\epsilon_a)r_a,\qquad
 \sum_m\sup_{s_m,\nu_m}\|\mathcal R_a(Q_m)-\mathcal R_a(Q_{m-1})\|
 <\epsilon_a r_a.                                               \tag{4}
\]
The suprema include all earlier parameter choices and all prefixes.
Here \(Q_m\) denotes a composition prefix in a fixed target chart; \(r_a\) is that target clause's radius.
Continuation and logarithm charts require their own retained room.
The triangle inequality then admits every prefix. This proves the sufficiency of (4).
It does not prove (4) for the history-dependent maps.
The valid parts of the four named results do not establish that all-history assertion.

## 6. Corrected Lemma M

Assume (D4), response splitting, and the local read and index properties (D2).
Let \(F\) be holomorphic on \(D_F\), with the finite bound required in (D4).
Physical identification includes the recorded gauge and stored-data transport; (D4) must admit those maps too.
Use the component construction of `red.md` Section 3(2) and `d3-local.md` Section 3.
Keep their two-radius collars. Do not assume every term of \(W_s\) is tagged.

Let \(\mathcal P\) be the finite parameter grid.
Let \(\mathcal A\) cover \(F\)'s fixed carrier and all read collars.
Set \(\mathcal C=\mathcal P\setminus\mathcal A\) and
\[
 E(s,\nu)=F(Q(s,\nu;P))-F(\rho_XP),\qquad
 e_K=\sum_{I\subset K}(-1)^{|K|-|I|}E(\mathbf1_{I\cup\mathcal A},1).
\]
Then
\[
 F(P^{\rm old})=F(\rho_XP)+\sum_{K\subset\mathcal C}e_K,
 \qquad
 |e_K|\le\frac{2M_F}{\varrho_F}(e^{\bar\kappa}-1)^{-|K|}.          \tag{5}
\]
Each \(e_K\) is a partial map reading only \(K\cup\mathcal A\), with its collars included.
It vanishes if a component containing a differenced cube misses the anchor.
It also vanishes if the response has no datum on any component read by the anchor.

For the identity, the coefficient of the corner indexed by \(I\) is \((1-1)^{|\mathcal C\setminus I|}\).
Only the full corner survives. Physical identification in (D1) gives the old evaluation there.
At any other corner, splitting restricts each read to its surviving component.
An unanchored component can be toggled without changing the value, so its two signs cancel.
Zero response makes \(E\) zero.
Domain equality follows from the local-domain clause of (D4).

For the bound, \(E(s,0)=0\) and \(|E|\le2M_F\) on the scalar disc.
Schwarz's lemma gives \(|E(s,1)|\le2M_F/\varrho_F\).
For each differenced variable, integrate against \(1/[z(z-1)]\) on \(|z|=R'<e^{\bar\kappa}\).
The integral costs at most \((R'-1)^{-1}\).
Iterate and let \(R'\uparrow e^{\bar\kappa}\). This proves (5).
The empty bracket has the same bound because we subtracted the base value.
No \(\varrho_F^{-1}\) gain applies to that base value itself.

## 7. Corrected Theorem W

Assume (D1), (D2), (D3), (SUP), the repaired component property, and (D4) at every move.
Then exact (LOC) holds through every later step and every \(\mathbf R\) stage.

Induct in the order of moves.
For each carried piece, (D4) admits every evaluation used in (5).
Lemma M replaces it by pieces on fixed local read sets.
The new pieces have the same property by (D3).
Products and integrals over common measures preserve equality on equal traces.
The finite polymer sums preserve it too.
Absolute convergence, retained from (D3), permits equality through the inner walk and cluster sums.
This proves the induction, including equality of partial-map domains.

If a healed component misses the full read window, (SUP) leaves its trace unchanged.
The corresponding completed \(V_{\mathfrak X}(Y)\) slot therefore has the same value.
Regular slots one cell inside \(\Lambda\) have the common never-large trace, giving (Act).
This is the window version of locality in `loc-3.md`.
Absorbing whole components into \(Y\), with their quantitative cost, remains a separate bound.

## Result

**Correction of our text.** Proposition O is geometry only.
Section 4 admits the specified inner curves and single-layer outer shifts, with their Hölder clauses and complex room.
Lemmas M and W hold with (D4); the outline already proves their bracket algebra under that hypothesis.
The explicit map and argument (3) refute iteration of one-move room without a domain invariant.
They do not refute the actual Yang–Mills response.

**First input still open:** (D4) for the actual carried compositions on every history and stage, with the required complex radii.
In particular, the outer long-member evaluations of `wf7-bf.md` Section 3 need their inherited domains checked after carriage.
Theorem A's inner-image admission and the rejected Proposition I do not supply this.
No actual Yang–Mills argument outside its assigned core has been established here.
Regional Gaussian existence for (D3) remains a further input.
Thus this note does not close row 226 or (LOC). Its new arguments have not been checked by the other model.
