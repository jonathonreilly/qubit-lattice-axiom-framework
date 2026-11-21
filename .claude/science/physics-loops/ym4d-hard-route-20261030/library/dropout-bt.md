# Drop-out terms in their formation-stage boundary spaces

Provenance: Codex (GPT-6 family; exact serving variant and runtime effort not exposed), checkout c8e88e63666ed78725508cb53107236bd06fa8bb, 2026-11-04. Research text, not an audit; grants no status. Sources: Tadeusz Balaban; Ethan Sussman and Levent Alpoge, with Claude and Codex as authors of their text, pinned at 31a47c543775. Not yet checked by the other model.

## 1. Finding and sources

**The boundary filing is allowed. Freezing all its arguments is not the outline's rule.**
Its (LOC) consumer expressly compares the old and new backgrounds, both in the new variables.
Thus the proposed filing does not remove (D4) from the existing proof.
This is a correction to that proposed inference, not a counterexample to Yang–Mills or to a different representation.

SA means the [pinned outline](https://github.com/ethanwsussman/Yang--Mills-LLM-experiment/blob/31a47c543775/YM4_sketch_500.tex).
CA-I means the [pinned complete account](https://github.com/ethanwsussman/Yang--Mills-LLM-experiment/blob/31a47c543775/theorem_0_complete_account_raw_I.tex).
Their SHA-256 values are, respectively,
`d7f77d4da3eb23038250c52468a341281d9ba86b4af21d3371d208a2537d4b6f` and
`4cb5cb5e0af8dbddbee207926621300350e018c6cf1d6567a753167ce10e6e93`.
The index and its neighbouring rows guided the bounded readings below.
The seven prior Results and `d4-chart.md`, `wf-c-stage.md`, `d4-route.md` were read first; none is treated as a checked stage theorem.
All deductions below are by hand.

The relevant source classification is precise:

- CA-I 49537–49540 quotes Balaban, CMP 122 (1989), p. 191: “we leave the new terms” \(\mathbb B_k^{(n)}\) “as a part of all boundary terms”. The later-space assertion is labelled “printed without proof” at 49535. This is a recipe, not an inclusion proof. The local paper collection has no CMP 122 text; the quotation is checked against CA-I, not against that printed page.
- CA-I 49498–49500 calls these “conditions that the application has to meet”; CA-I 54987–54992 says “Assume” the stage theorem of (1.60)–(1.70). Neither passage discharges the stage input.
- SA 17654 already implements the recipe: “The terms produced up to that point are added to the boundary terms.” SA 6187–6189 gives each slot its formation structure-domain: “It retains that domain at later steps.”
- SA 6155–6158 still calls stage substitutions “analytic inclusion hypotheses”. A permanent domain is not a permanent value of the argument.

## 2. The spaces with formation-stage labels

Fix all formation data. Let \(C\) stop after \(n\) stages of level \(t\), and put \(h=t-\mathsf N_t\ge0\).
Keep the old regions, prepared boxes, and stage count with the mark.
For each \(0\le\nu(C)\le n\), use exactly (R21), SA 6095–6111:
\[
 \Omega_l^{\boldsymbol\nu}\cap C=
 \begin{cases}
 C\setminus Z_l''(C),&h<l\le h+\nu(C),\\
 \Omega_l^\circ\cap C,&h+\nu(C)<l\le h+n.
 \end{cases}                                                     \tag{1}
\]
Other entries stay as recorded. The source calls \(\nu=n\) the “determining sequence” and \(\nu=0\) the “action sequence”.
Use the first for backgrounds and the second for term indices and weights.
In particular, filing a term does not replace its determining constraints by its action regions.

A boundary slot is \(f=(j,X,o,\sigma_f)\), including its formation moment and domain (SA 6185–6189).
For a term made at moment \(\mu\), its persistent sequence is
\[
 \Omega_l^{\boldsymbol\nu_\mu}(\mathcal S_k)
   =\Omega_l(\mathcal S^\mu)\cup Z_{[j,k]},\quad l\le j.             \tag{2}
\]
Here \(\nu_\mu=n\) on older marks and \(0\) on later ones.
SA 17440–17447 says the term “retains permanently the space in which it was made” and gives (2).
Thus an old term and a stage-\(n\) term need not have the same sequence.

For every structure \(\tau=(\mathcal S,\boldsymbol\nu;s,\phi)\) read by this slot, retain (R22):
\[
 \begin{split}
 c_\tau(x\mid m)&=1-\beta_{\rm s}(1-2^{-(s-m)})
       +\varpi_\phi\mathsf g_s(m)
       -\beta_{\rm R}\sum_{l\in\operatorname{Re}_\tau(x)}2^{-|m-l|},\\
 \mathsf g_s(m)&=
 \begin{cases}\theta_{\rm s}\beta_{\rm s}2^{-(s-m)},&m<s,\\
 \beta_{\rm s},&m=s.
 \end{cases}
 \end{split}                                                     \tag{3}
\]
The phase weight is \(0\) at output, \(1\) at input, and \(1-r/(2\mathsf N_s)\) after \(r\) stages (SA 6117–6121).
The remake set contains the first \(\nu(C)\) stage levels of each mark through \(x\).
The fixed fractions obey \(0<\theta_{\rm s}<1\), \(\beta_{\rm R}=c_{\rm R}\beta_{\rm s}\).
The supplied original and remade layer assignments give their nonnegative difference \(e_\tau(x)\).
Multiply the supplied layer radii by \(L_\flat^{2e_\tau(x)}c_\tau(x\mid m)\); omit \(c_\tau\) from the real-potential gauge bounds.
Retain the level-one convention at layer zero, the level-\(s-1\) convention at an unfinished top, and the separate initial structure.
These are SA 6137–6148; its required range is \(c\le c_\tau\le1+\beta_{\rm s}\).
No new radius is chosen when a term is filed.

Write \(D_f=\widetilde U^c_{\sigma_f}(X)\).
For one splitting \(P=(U,A',\mathbf J)\), \(\mathbf U=e^{i\eta_jA'}U\), with \(U\) real and \(A',\mathbf J\) independent complex forms, it imposes (R4), SA 5665–5685, with those radii:
\[
 |\partial U-1|,|\partial\mathbf U-1|<a_0\eta_j^2,\qquad
 |A'|,|\nabla_UA'|<a_1,\qquad |\mathbf J|<a_2.
\]
In each specified box of side at most \(C_{\rm box}LM\), a real gauge has
\(U=e^{i\eta_jA}\), \(|A|,|\nabla A|<C_{\rm pot}Ma_0\).
For each subdomain \(Z\subset X\), level \(p\le j\), depth \(1\le d\le p\), erosion rule, and preceding structure, form that structure's determining set \(\mathbf B'\) and require (R5), SA 5696–5706:
\[
 U_d(Z;P)=\Phi_{M_{\mathbf B'}(U)}
  \left(i^{-1}\Log\{M_{\mathbf B'}(\mathbf U)M_{\mathbf B'}(U)^{-1}\}\right).
                                                               \tag{4}
\]
The assigned branch and continuation must exist. Remove two layers of level-\(p-1\) \(M\)-cubes and require (R6), SA 5706–5720,
\[
 |\partial U_d-1|<a_0L^{-(j-p)}\eta_p^2,
 \qquad |J(U_d)|<a_0L^{-(j-p)}L^{2(d-p)},                         \tag{5}
\]
with the prescribed local layer radii, and also with \(\mathbf U\) replaced by \(U\).
Both actual erosion assignments are retained (SA 5598–5610: “the actual sets”).
Rule I uses \(\mathfrak M\)-cubes with gaps greater than \(\rho\) in outer units.
Rule II uses \(M_1'\)-cubes with gaps at least \(M_1'\) in inner units.
The determining bonds are exactly (R2), SA 5612–5629: their endpoints lie in \(\Omega_0\), at least one lies in \(\Omega_r\), neither lies in \(\Omega_{r+1}\), and the read is \(\mathcal M^rU\) there.
The source excludes “inward bonds crossing into the next layer”.
SA 5721–5727 requires “every allowed” subdomain and an open continuation domain.
SA 6150–6154 requires “one splitting” on “every preceding structure”, including the small-field-core clauses.
This is the original hereditary space with its saved formation data, not a claim that a later substituted pair belongs to it.

Keep one copy of each stored coordinate, with its original measure and test range.
SA 6160–6173 makes near fields Borel, with analytic switches \(|\mu_b|<\lambda_l^{\rm st}\),
\(\lambda_l^{\rm st}=(\log\theta_l)^{6r+1}\).
Far fields have the stated analytic ball of radius \(\lambda_l^{\rm st}\) times their real range.
At switch zero there is no dependence on that near field; at field zero there is no dependence on its switch.
The pair tie holds at every switch value. The physical value has \(\mu_b=1\).
The source states “No variable is integrated twice” (SA 6284–6286).

Here is an exact way to express the proposed extra freezing.
For a fixed stored fibre, adjoin a saved pair-splitting \(q_f\in D_f\) for each stopped slot, with the stored domains just specified and shared stored coordinates identified.
The resulting space is
\[
 \mathfrak D_\ell^{\rm saved}
  =\widetilde U^c_{\sigma_\ell}\times\prod_{f\ {\rm stopped}}D_f
       \times\mathscr S_{\rm stored}.                           \tag{6}
\]
All pair functions must retain their ties. Repeated uses of one saved argument use one coordinate.
The function \(F_f(q_f,\xi_f)\) needs no later chart on (6).
But the extra \(q_f\)'s are not new free variables of the outline's kernels.
To recover its actual history, (6) must be restricted to the graph of the old reads
\(q_f=T_{\ell f}(P_\ell,\xi;\zeta)\).
The exact later admission space is therefore
\[
 \{(P_\ell,\xi):T_{\ell f}(P_\ell,\xi;\zeta)\in D_f
       \text{ for every required }f,\zeta\}.                    \tag{7}
\]
These are partial maps until their gauges, branches and continuations exist.
Defining (7) does not prove that it contains the required later input domain.

## 3. What can stay fixed, and the forced read

**A limited freezing lemma.** If a later move is a projection which leaves \((q_f,\xi_f)\) unchanged, then it leaves \(F_f(q_f,\xi_f)\) unchanged.
Its supremum cannot increase on any subset of the old domain.
Proof: the projection composed with the coordinate read is that same read; substitute into \(F_f\) and take suprema.
The proof is uniform in the number and values of all other parameters.
This applies to saved coordinates on (6). It does not identify (6) with an actual later state.

For the actual stopped operation the source distinguishes these reads:

| Read | What the source permits |
|---|---|
| Stored variables, tests, gauge and delta factors | They stay in the retained operation; the latter factors have no background dependence (SA 17558). This is not a statement that every field argument of the exponent is fixed. |
| Complete kept forms and elimination factors | They are fixed **functions** of the pair, evaluated at the changing current background (SA 17558–17564). |
| Fields not supplied by the stored variables | They are specified averages of one compatible real field, not extra independent frozen coordinates (SA 18139–18157). |

This applies to drop-outs: SA 18131–18134 lists “complete kept forms and elimination factors” among what they retain.
The exact clause at SA 17558 is:

> They are evaluated at the current background, which in a term of level \(k\) is \(U_k(\mathbf V)\). The background changes with every later step and with every stage of \(\mathbf R\).

The ensuing difference is (SA 17561)
\[
 -\tfrac12\langle A',
 [\Delta^{\rm loc}_{\mathfrak k}(U^\sharp)
  -\Delta^{\rm loc}_{\mathfrak k}(U^\flat)]A'\rangle.             \tag{8}
\]
SA 17564 defines \(U^\flat\) after and \(U^\sharp\) before the move, **“both written in the new variables”**, and says “Localisation turns these differences into boundary terms.”
This is the requested forced re-expression clause.
It requires evaluation maps into the old function's domain; it does not require replacing that domain by a later one.

The necessity is algebraic. Put \(K(p)=-\tfrac12\langle A',\Delta^{\rm loc}(p)A'\rangle\).
Then
\[
 e^{K(p_{\rm old})}
   =e^{K(p_{\rm new})}e^{K(p_{\rm old})-K(p_{\rm new})}.          \tag{9}
\]
Keeping the old factor is exact before the change of integration variables.
After that change it is \(e^{K(T_{\ell f}(P_\ell,\xi;\zeta))}\).
Replacing this by a factor at a fixed independent \(q_f\) is not an identity supplied by (9).
Saving the relation \(q_f=T_{\ell f}\) retains precisely that read.
We have not exhibited a nonzero difference for a particular stage; none is needed to identify the clause the proposed proof would have to replace.

The collar consumer is explicit too. SA 19518 says boundary terms in stages enter as “differences in the collar field, taken one block of bonds at a time”.
SA 17912–17923 identifies the old and new evaluations and forms the new argument, gauge and stored data together.
CA-I 54337–54339 likewise puts the carried action terms on the descending spaces and says they are evaluated “at the current background”.
Thus it is insufficient to freeze only the primitive stored coordinates.

For a slot affected by this collar move, (D4) still asks for
\[
 T_{\ell f}(P_\ell,\xi;\zeta;s,\nu)\in D_f,
 \quad |s_\Delta|<e^{\bar\kappa},\quad |\nu|<\rho_F,
 \quad \rho_F=c_FL^{k-j}a_{0,j}\delta(\theta_k)^{-1}
                   e^{-C_F\bar\kappa}>1.                       \tag{10}
\]
All earlier parameters are included. Inner and removed moves have their own radii.
SA 5813–5825 states this as an inclusion hypothesis; `loc-4.md` lines 152–162 requires the full compositions, stored arguments and gauges.
There is no new bound for (10) here.
The unchanged-coordinate lemma gives arbitrary scalar room only for a read proved independent of that move; it gives none for (8).
Nor does a stop at stage \(n\) retroactively admit a term's formation at stage \(0\to1\).

## 4. The consumers

| Consumer | Formation-stage filing | Extra freezing of the argument |
|---|---|---|
| Ordinary B4 | Accepted as a type of input. SA 4880 includes “boundary terms” and stored excesses; 4893–4907 requires their majorants and carrier oscillations. SA 6187–6189 preserves the slot domain. | Not supplied by B4's input class. The effective exponent still reads \(B_{\mathcal S}(j,X,o;U,\text{stored data})\), SA 6345–6347. Its boundary bound does not justify an extra free \(q_f\). SA 4036–4037 leaves “background/core inclusions and history formation” unverified. |
| (LOC) and the boundary induction | Accepted, with localisation performed on each old function's domain. | The affected reads force the substitution at SA 17561–17564 and the collar differences at 19518. SA 17916 is \(f(U^{\rm old})-f(U^{\rm new})=\sum_{Y\supset X}f_Y\). Its bound uses the analytic interpolation of 17907–17918 and hence (10). |
| Drop-out majorant, SA 6315–6318 and 7555–7559 | Accepted only for the same partial operation with its carrying Wilson factor. SA 6315–6316 says there is “no new free entry of type (R24)”. | A saved complex pair cannot replace the real compatibility fibre. SA 7559 requires configurations “compatible with the stored variables”; SA 18175–18176 says the Wilson field “stays real”. |
| History sum | The final positive sum is insensitive to the name of a slot when factors, measures, carriers and bounds are unchanged. | It uses the actual-read envelope first. SA 19011–19019 replaces the “actual later read” by the mass majorant, despite background dependence on all variable groups. SA 18816–18823 forms one envelope before the fibre supremum and integrates its Borel majorants. A bound at one saved value cannot replace that envelope. |

The last two conclusions have short hand proofs.
With \(\omega,\xi\) fixed, let
\[
 m_\omega(\xi)=1_{S_\omega}(\xi)
   \sup_{\mathfrak e\in\mathfrak K^\sharp(\omega,\xi)}
   e^{-A(\upsilon1_X,U)}\mathsf K_\omega(\xi;\mathfrak e).        \tag{11}
\]
This is SA 18139–18176, including its compatibility equation
\(\mathcal M^jU=V_j(\xi)\) on the specified determining bonds.
The other fibre clauses retain the recorded tests, inner-island domains and one-sided complete-form and Jacobian bounds.
SA 18151 reads all unstored fields as “the specified averages of” \(U\).

Use zero for an empty fibre. On \(S_\omega\), if a later read is in this fibre and changes none of the factors, it is at most (11), by the definition of supremum.
Adding records can restrict the fibre; it cannot increase this supremum when the same factor is retained.
Multiplying by the nonnegative reserve and integrating any common Borel majorant preserves the inequality.
This proves invariance under relabelling, conditional on actual-read membership.
It proves neither that membership nor the mass estimate itself.
SA 7511 explicitly says the drop-out majorant “remains a required input”.
In particular, a boundary sup norm alone does not supply its real Wilson energy.

After these envelopes and the source's entropy bound are available, let \(a_\gamma\ge0\) be their integrated record weights, with
\(\sum_{\gamma\text{ rooted at }z}a_\gamma\le1\) as in SA 19133–19137.
For finitely many records,
\[
 \sum_{\mathfrak F\ {\rm allowed}}\prod_{\gamma\in\mathfrak F}a_\gamma
 \le\prod_\gamma(1+a_\gamma)
 \le\exp\!\left(\sum_\gamma a_\gamma\right).                    \tag{12}
\]
The first inequality adds nonnegative terms. The second follows from \(1+x\le e^x\), \(x\ge0\).
Increasing finite sums give the countable version.
This proves the last summation step of SA 19139–19160 under its weight input.
A bijective relabelling of slots changes no factor in (11) or (12).
Thus the history sum itself needs no new chart, but it cannot repair the earlier failed admission.

## Result

**Correction of the proposed no-re-expression route.**
Balaban's boundary filing is already present at SA 17654 and 6187–6189.
Section 2 records the formation-domain rules; (6) states the extra saved-argument construction. Neither proves a later inclusion.
The projection lemma proves carriage for unchanged reads.
Equations (11)–(12) prove that relabelling preserves already valid majorants and the final positive history sum.

The outline does **not** accept replacing its changing reads by independent saved arguments.
The decisive consumer clause is SA 17564, “both written in the new variables”, used by (LOC) and by the boundary induction at SA 19518.
Keeping the old domain is compatible with that clause; dispensing with its evaluation map is not.

**First open input:** admission of the actual collar read into each formation-stage hereditary domain, on the full enlarged disc (10), uniformly over earlier parameters.
For the earlier activities at stage \(0\to1\), this still includes their old (R5) continuations.
This note proves no uniform \(A_e,G_e,B\), no collar radius \(\rho_F>1\), and no claim that every pair field is fixed on a stopped component.
A different representation could avoid this consumer only after an exact measure identity and replacement formation estimates are proved.
No such impossibility claim is made.
The text is not yet checked by the other model.
