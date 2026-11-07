# Ordinary preparatory stages
Provenance: Codex, commit `c8e88e636`; research text, not an audit; no status granted; not yet checked by the other model.

## Scope and source

This note treats ordinary preparatory stages on a component that continues.
It does not treat carriage after a component stops.
The target is the domain input shared by B4, (LOC), and (R-cov).

Credit Tadeusz Balaban for the stage method.
Credit Ethan Sussman and Levent Alpoge, with Claude and Codex as authors of their text,
for the constructions used below.
SA denotes their [outline](https://github.com/ethanwsussman/Yang--Mills-LLM-experiment/blob/31a47c543775/YM4_sketch_500.tex).
CA-I denotes their [complete account, part I](https://github.com/ethanwsussman/Yang--Mills-LLM-experiment/blob/31a47c543775/theorem_0_complete_account_raw_I.tex).
Both have revision `31a47c543775`. Line numbers refer to those files.
The index README, relevant chunk rows and neighbouring rows, and `obligations.md` were read first.
The literature record is `lit-large-field.md`, especially lines 103–107:
“Nothing is healed or dropped out.” Its YM3 comparison supplies no preparatory R-stage theorem.

**What is imported.** CA-I 54987–54995 says “Assume the following” and imports
“The inductive theorem on one stage of the preparatory integrations”.
CA-I 55074–55078 then applies that theorem at every stage.
This is an assumption, not its proof.
CA-I 49498–49511 calls real-background inclusion one of the
“conditions that the application has to meet”.
SA 6155–6158 calls stage inclusions “analytic inclusion hypotheses”.

The reconstruction must retain all seven entries, not curvature alone.
CA-I 49595–49624 lists
\[
 |\partial\mathbb U-1|,\quad |\partial U_{p,X}-1|,\quad
 |\mathbb J|,\quad |J_{p,X}|,\quad |\partial U-1|,\quad
 |A'|,\quad |\nabla_U^\eta A'|.                         \tag{1}
\]
Its coefficient in (1.64) is
\[
 1-\beta\sum_{i=h+1}^{j}2^{-|m-i|}
   -\beta\sum_{q=m+1}^{k}2^{-(q-m)}.
\]
Here \(k_0=k-N_0\), with \(N_0\) the overlap-depth parameter of the prepared geometry.
The lift is \(\mathsf L_0^{2(m-k_0)_+}\).
For (1.66), the radius index is \(j\), and the lift is \(\mathsf L_0^{2(j-m)}\).
For (1.68), the lift is one.
The source says the lift “multiplies every one of the seven entries” (49620–49624).
Below we use SA's (R22) version and keep a separate continuation margin.
This is a proposed replacement, not a transcription of the unavailable paper.

## Explicit domains

Fix a finite cutoff, one history, its frames, and all real near stored variables.
Put \(h=k-\mathsf N_k\), \(j=h+n\).
The stage integrates \(R_n=Z_{j+1}\setminus Z''_{j+1}\).
CA-I 53806–53814 says that only “the member of level \(j+1\)” changes.
Use the determining sequence after that replacement.
Keep the action sequence separate, as SA 6108–6111 requires:
“it governs the sums and the coupling profiles”.

Here is a precise domain specification in terms of **fixed formation data**.
A clause record includes its level, layer, region, real reference, units, and erosion rule.
Include every subdomain, truncation, and preceding structure prescribed by SA 5696–5727 and 6150–6154.
These lines say “every allowed \(Z,p,n\)” and “with one splitting”.
The same real splitting must serve all records. Each box can have its own real gauge witness.
These witnesses do not replace the prescribed returning gauges.

In a record of top level \(s\), write \(P=(U,A',\mathbb J)\), \(W=e^{i\eta_sA'}U\).
For each tower \(e=(Z,p,d)\), \(1\le d\le p\le s\), set
\[
 b_e(P)=i^{-1}\Log\{M_{\mathbf B'_e}(W)M_{\mathbf B'_e}(U)^{-1}\},
 \qquad T_e(P)=\Phi_{M_{\mathbf B'_e}(U)}(b_e(P)).       \tag{2}
\]
The normalized seven entries are
\[
\begin{array}{c|c}
 Q_a(P)&\text{radius}\\ \hline
 \eta_s^{-2}|\partial W-1|&a_0\\
 L^{s-p}\eta_p^{-2}|\partial T_e(P)-1|&a_0\\
 |\mathbb J|&a_2\\
 L^{s-p}L^{2(p-d)}|J(T_e(P))|&a_0\\
 \eta_s^{-2}|\partial U-1|&a_0\\
 |A'|&a_1\\
 |\nabla_U A'|&a_1
\end{array}                                                     \tag{3}
\]
The tower entries are read after removing two level-\(p-1\) cube layers.
Repeat them with \(W=U\). These are exactly the normalizations in SA (R4)–(R6), 5673–5720.
SA 5706 requires the tower “to exist in the chosen continuation domain”.
The independent current is not \(J(W)\).
SA 5758–5760 says that replacing it by the physical current “would change the construction”.

At a native layer \(m\), use base radii \((\alpha_{0,m},\alpha_{1,m},\alpha_{0,m})\).
Multiply them by \(L_\flat^{2e_\sigma(x)}c_\sigma(x\mid m)\).
Explicitly, (R22), SA 6126–6148, gives
\[
 c_{\sigma_n}(x\mid m)=1-\beta_s(1-2^{-(k-m)})
 +(1-n/(2\mathsf N_k))\,g_k(m)
 -\beta_R\sum_{\ell\in{\rm Re}_{\sigma_n}(x)}2^{-|m-\ell|},
 \quad
 g_k(m)=
 \begin{cases}\theta_s\beta_s2^{-(k-m)},&m<k,\\ \beta_s,&m=k.\end{cases}
\]
For the current ordinary run, record \(h+1,\ldots,h+n\) as temporary remake entries on \(Z\).
This extends the recorded-mark convention to the active run; it is a choice in our replacement target.
The integer \(e_\sigma(x)\ge0\) is the supplied difference of regularity layers before and after remaking.
Fix \(\beta_s+3\beta_R<1\). Distinct recorded levels give \(c_\sigma\ge1-\beta_s-3\beta_R>0\).
Indeed, \(\sum_{\ell\ge0}2^{-|m-\ell|}\le1+2\sum_{r\ge1}2^{-r}=3\).
Table (3) gives the native inequalities. Transport each whole inequality to another record's units by (R7), SA 5738–5745:
\((\eta,A',\mathbb J)\mapsto(L^v\eta,L^{-v}A',L^{-3v}\mathbb J)\).
The gradient then scales by \(L^{-2v}\); group plaquettes do not change.
Convert each slot's radius by its own factor; potential and gradient slots scale differently.
Every inherited record keeps its own radius and reference data.
Impose the inequalities for all records, including those whose domains are larger than a carried term.

Also retain the real gauge clause on every box of side at most \(C_{\rm box}LM\):
\(|A|,|\nabla A|<C_{\rm pot}M a_0^{\rm lift}\), where \(a_0^{\rm lift}\) excludes \(c_\sigma\).
This is SA 5683–5685 and 6144–6145: “except for the real-potential gauge bounds”.
For the operator reads, retain the printed cube families as well.
CA-I 48472–48477 requires a gauge on each cube intersection and the bounds
\(\ell_i|A|,\ell_i^2|\nabla A|<L_0^{2e}BM\alpha_{0,i}\), with \(C=1\).
CA-I 48527–48565 gives the following cube families at stage level \(j\).
All cubes have side \(M\ell_i\). Each bound is read on \(Q\cap X\).

| Cube condition | Radius index \(i\) | Exponent \(e\) |
|---|---|---|
| \(Q\subset\Omega''_m,\ Q\not\subset\Omega''_{m+1},\ m<j\) | \(m\) | \((m-k_0)_+\) |
| \(Q\subset\Omega''_j,\ Q\not\subset\Omega_{k_0+1}\) | \(j\) | \((j-k_0)_+\) |
| \(Q\subset\Omega''_j\cap\Omega_{k_0+1},\ \bar m=\max\{i\le j:Q\subset\Omega_i\}\) | \(j\) | \(j-\bar m\) |
| \(Q\subset\Omega_m,\ j<m\le k\), meeting \(\Omega_{m+1}^c\) when \(m<k\) | \(m\) | \(0\) |

Real gauge existence is a condition of these domains, not a consequence of their definition.

Denote this intersection by \(\mathcal H_n(X)\).
To specify *room*, fix for each tower a continuation ball \(\|b\|<r_{B,e}\),
a number \(0<q_e<1\), and \(0<\epsilon_e<r_{B,e}\).
Require in addition
\[
 \|M_{\mathbf B'_e}(W)M_{\mathbf B'_e}(U)^{-1}-I\|<q_e,
 \qquad \|b_e(P)\|<r_{B,e}-\epsilon_e.                 \tag{4}
\]
Call the resulting domain \(\mathcal H_n^\epsilon(X)\).
Holomorphy is on each fixed-real-\(U\) slice, with the pair tie on overlaps.
Neither definition asserts a uniform neighbourhood of the fields used by the integration.

The parameter set \(\mathcal P_n\) contains all retained earlier parameters and all Boolean corners.
Its walk radii are \(|s_\Delta|<e^{\bar\kappa}\).
Its interpolation radii are the quantitative \(\varrho_F>1\) of (R11), SA 5813–5825.
Near stored fields stay real. Their switches satisfy \(|\mu_b|<\lambda_l^{\rm st}\).
Far stored fields have radius \(\lambda_l^{\rm st}\) times their real range.
These are SA 6160–6173: “Borel in the near variables” and “jointly analytic”.

## The stage assertion to prove

This is the boundary part of the desired theorem. It remains a target.
Fix the ordinary geometry, the A1–A3 data, regular activities and scalar sources of the admitted construction.
Their previously named bounds remain premises; no new status is assigned to them here.
Assume each previously born boundary family \(C_i=(\mathbb C_k^{(i)}(X))_X\)
is local, tied and holomorphic on its specified birth domain, with norm at most \(C_0=c_G+1\).
At stage \(n\), its current read includes all intervening substitutions and recorded returns.
Assume these stage-\(n\) reads are already formed, holomorphic, and bounded on \(D_n\).
The cumulative input is
\(\sup_x\sum_{i\le n}\sum_{X\ni x}\|C_i(X)\|_{\infty,n}\le3(N_0+3)C_0\).
It must persist at \(n+1\); CA-I 55034–55037 states that bound.
The theorem must construct domains \(D_n\) of the form above which admit those reads with room.
They must contain the integration's real support and the prescribed complex domains of its consumers.
Uniformity is in the cutoff, volume, history, stage count, and earlier parameters.

Let \(I_{n+1}\) be the two fluctuation integrals of CA-I 54293–54298, including \(z^{(j)}\) and cutoffs.
The claimed new family is
\[
 \mathbb C_k^{(n+1)}=\log I_{n+1}
       +A(x^{(n+1)}-x^{(n)},U_k^{(n+1)})
       =\sum_X\mathbb C_k^{(n+1)}(X),
 \qquad \mathbb B_k^{(n+1)}=\mathbb B_k^{(n)}+\mathbb C_k^{(n+1)}.       \tag{5}
\]
CA-I 54314–54329 calls this “the stage term”.
The logarithm uses the branch supplied by a convergent normalized expansion.
Each summand must be holomorphic on \(D_{n+1}(X)\), including its exterior analytic slots.
It must read only fields in \(X\).
It is filed at the least \(m\ge j+1\) with \(X\subset\Omega_{m+1}^c\),
and must satisfy \(X\in\mathbb D_m\), \(X\cap\Omega_m\ne\varnothing\), \(X\cap R_n\ne\varnothing\).
Here \(\mathbb D_m\) consists of face-connected unions of the \(Mu_m\)-cubes of \(\pi_m\).
These are the quoted representation conditions in CA-I 54341–54346.

The norm, with all parameter and stored-slot suprema inside the sum, is
\[
 \|C\|_{n,a}:=\sup_m\sup_{\square\in\pi_m}
   \sum_{\substack{X\ni\square\\m(X)=m}}
   e^{a_md_m(X)}\sup_{D_n(X)\times\mathcal P_n}|C(X)|.
                                                               \tag{6}
\]
CA-I 54349–54356 specifies this weighted norm and its pointwise consequence.
The target is
\[
 \|\mathbb C_k^{(n+1)}\|_{n+1,a}\le c_G+1,
 \qquad |\mathbb C_k^{(n+1)}(X)|\le(c_G+1)e^{-a_md_m(X)}.       \tag{7}
\]
Use \(a_k=(1+3\beta_s)\kappa\) and \(a_m=(1-\beta_s)\kappa\) for \(m<k\).
The stronger lower-level rate requires the additional condition \((F_m)\).
CA-I 55019–55024 says “under \((F_m)\) ... otherwise”; it does not give that condition's definition here.
Thus this reconstruction does not assert the stronger rate at every level.
The proposed norm closure is the split from CA-I 55039–55044:
\[
 \|C_G\|\le c_G,\qquad
 \|C_I\|\le K'_S(N_0+8)C_0\vartheta\le1.                       \tag{8}
\]
The constants and the positive coupling ceiling needed to prove (8) have not been constructed in this note.

## Proof attempt: build inclusion into the spaces

Let \(E_{n,F}(P,\xi,z)\) be the **complete** read of an older term \(F\) during stage \(n+1\).
Here \(\xi\) ranges over its real integration support, and \(z\in\mathcal P_n\).
Include the shifted read, the zero-fluctuation read, all localization reads, and all earlier compositions.
Take \(X\) to contain their complete assigned read sets; each \(F\) keeps its own birth carrier.
The map includes the current, returning gauge, and stored-coordinate read.
It is a partial map until its logarithms and continuations exist.
CA-I 54301–54312 requires the difference between these two backgrounds.
SA 17921–17925 says their gauge factor and stored data are “formed together”.

For a birth domain \(D_F\), let \(D_F^{[-\epsilon]}\) mean that each normalized inequality
has an \(\epsilon\) reserve in its own units, including the logarithm and continuation inequalities (4).
All reserves are fixed data, not distances chosen after evaluating a field.
Define recursively
\[
 D_{n+1}^{\rm safe}(X)=\operatorname{int}\left\{
 P\in\mathcal H_{n+1}^\epsilon(X):
 \begin{array}{l}
 \text{every required }E_{n,F}(P,\xi,z)\text{ exists, and}\\
 E_{n,F}(P,\xi,z)\in D_F^{[-\epsilon]}
 \text{ for every }F,\xi,z
 \end{array}\right\}.                                      \tag{9}
\]
Interior is taken on each fixed-real-reference slice.
For a previously produced stage term, \(D_F\) is its already fixed birth space.
Require each existing read to be jointly holomorphic in its analytic variables.
Keep sharp tests in the real kernel; their indicators are not analytically continued.

**Lemma.** On (9), every old value has its birth bound and its required Cauchy bound.
Any open subset of \(\mathcal H_{n+1}^\epsilon(X)\) with these read inclusions and reserves is contained in (9).

**Proof.** Membership gives \(E_{n,F}\in D_F\), so
\[
 |F(E_{n,F}(P,\xi,z))|\le M_F:=\sup_{D_F}|F|.                 \tag{10}
\]
Composition gives holomorphy for fixed \(\xi\).
Suppose one read uses an interpolation \(|\nu|<\varrho_F\), with \(\varrho_F>1\).
For fixed remaining variables, put
\(G(\nu)=F(E(\nu))-F(E(0))\).
Then \(G(0)=0\) and \(|G|\le2M_F\).
For \(1<r<\varrho_F\), the maximum principle applied to \(G(\nu)/\nu\)
gives \(|G(1)|\le2M_F/r\).
Let \(r\uparrow\varrho_F\).
For a cube parameter, the difference between values at one and zero is
\[
 \frac1{2\pi i}\int_{|s|=r}\frac{G(s)}{s(s-1)}\,ds.
\]
Its norm is at most \(\sup|G|/(r-1)\).
Iterate over a set \(K\) of parameters, then let \(r\uparrow e^{\bar\kappa}\).
This proves
\[
 |\Delta_KG(1)|\le\frac{2M_F}{\varrho_F}
                       (e^{\bar\kappa}-1)^{-|K|}.            \tag{11}
\]
Thus (9) preserves exactly the analytic bound used by (LOC).
An open set satisfying the conditions inside braces lies in their interior, proving the last assertion. \(\square\)

For a fixed finite measure, (10) also permits integration of a carried factor.
Cauchy's formula on a smaller polydisc passes through the integral by its uniform bound.
This proves holomorphy and the bound \(M_F\) times the measure's total variation.
It does **not** prove zero-freeness of the full stage integral, or (8).
Nor does (10) localize a read whose response extends beyond its birth carrier.
Those later steps still need their Gaussian and connected-expansion estimates.

The lemma leaves one necessary statement:
\[
 D_{n+1}^{\rm req}(X)\subset D_{n+1}^{\rm safe}(X),            \tag{12}
\]
where \(D^{\rm req}\) is the full consumer domain, including its physical support.
B4 requires uniform domain size: SA 4876 says
“We must still prove the existence and uniform size of those domains.”
For (LOC), `loc-4.md` 155–162 requires \(|\nu|<\varrho_F>1\)
“on the entire next input domain”.
An empty or history-dependent thin domain in (9) does not supply either requirement.
The lemma's last assertion shows why renaming the domains cannot remove (12).

There is already a related conditional construction later in CA-I.
Its inherited domains are intersections of shell clauses and diminished term clauses
(119692–119709); its proof spends increments against their differences (119958–119985).
But its theorem assumes that the lettered stage clauses imply every old term's clauses
“with the unused room” (119822–119825).
Its increment proof also uses the stage-layer and bump bounds “in the form stated”
(116656–116668, 116700–116719; applied at 117604–117615).
These are useful conditional arguments, not a verification of (12) from our checked inputs.

## First open input

The unresolved instance occurs already at the first ordinary stage \(0\to1\).
It does not depend on a later stop.
Fix an older chart \(\tau\), its real reference \(U_\tau\), and either erosion rule's tower \(e\).
Let \((\widehat U_i,\widehat J_i)\) be the full pair read at the two endpoints, including earlier parameters.
Let \(u_i\) be the recorded return to that chart.
On the old bare mesh, the required expressions are
\[
 W_r(b)=u_r(b_-)\widehat U_r(b)u_r(b_+)^{-1},\quad
 K_r(b)=\operatorname{Ad}(u_r(b_-))\widehat J_r(b),\quad
 b_{r,\tau e}=\frac1{\mathrm i}\Log\{M_{\mathbf B'_{\tau e}}(W_r)
                              M_{\mathbf B'_{\tau e}}(U_\tau)^{-1}\}.       \tag{13}
\]
Here \(r=0,1\) labels the endpoints.
The exact missing statement is: **these maps exist holomorphically on all of
\(D_1^{\rm req}\times\mathcal P_0\), uniformly over the integration support, and fit the old continuation ball with fixed room.**
For all stages, a sufficient quantitative form is `d4-stage.md` (5):
\[
 \sup\|b_{0,\tau e}\|\le r_{B,\tau e}-\epsilon_{\tau e},\qquad
 \sum_n\sup\|b_{n+1,\tau e}-b_{n,\tau e}\|<\epsilon_{\tau e}.        \tag{14}
\]
Each supremum includes the full earlier parameter domain and every required corner.
The sufficient potential version is equation (6) of the same note:
\(\sup\|w_0\|_*<R/4\) and \(\sum_n\sup\|w_{n+1}-w_n\|_*<R/4\).
It uses one old reference throughout, with \(C_AR<r_B\).
The admitted averaging bound and Cauchy's estimate then give
\(\sum_n\sup\|\Delta b_n\|\le2C_A\sum_n\sup\|\Delta w_n\|_*<r_B/2\).
The initial datum is below \(r_B/4\). This proves (14) with \(\epsilon=r_B/2\), conditional on those potential bounds.
The quoted consumer line is SA 5706:
“This expression is required to exist in the chosen continuation domain.”
All seven size entries and the stored slots then need their own stage margins.

Here is why the checked results do not yet prove (14).

- `wf-c.md` Lemma C, lines 68–75, assumes \(\|w\|_*\le r_C\) and proves
  \(|Q-1|\le C_C(\kappa+\|w\|_*)\), uniformly in depth.
  Its Theorem \(6c^C\), lines 128–140, compares data along a segment in one common ball.
  `b4-step.md` Section 0 checks both as implications, “first failing step none”.
  We still have to put the actual returned field (13) in that ball.
- The checked A3 contraction gives
  \(\|D_bH[v]\|_{X,\omega}\le2\mathcal B\|v\|_{Y,\omega}\)
  on its admitted fixed system (`dec-field.md` 247–279, “Assume [PW], [NL]”).
  Changing the determining member changes two row levels and their nodes;
  `stage-tangent.md` (2), (5), and (8) retains the resulting coefficient and multiplier derivatives.
  This derivative bound alone does not control their full transported composition.
- A2 gives \(\operatorname{Re}\langle v,Av\rangle\ge(c_L/2)\|v\|^2\)
  at a “complex regular pair” (`a2-layers.md` 665–673), with its checks' separation and axial-slice conditions.
  It supplies the Gaussian gap **after** admission to that pair domain.
- `kept-cov.md` and Claude's `gates/kept-cov-check.md` prove common returning-coordinate covariance,
  with the relative kept form and the native-action premise retained.
  The check still lists “domain admission”.
  `gates/r-inv-check.md` likewise states “It gives no admission (D4)”.
  These identities permit consistent returns; they do not bound their size.

In particular, put \(\gamma=\dot u u^{-1}\) along a proposed common-chart path.
Differentiating the first equation of (13) gives
\[
 \dot W(b)=u(b_-)\dot{\widehat U}(b)u(b_+)^{-1}
                 +\gamma(b_-)W(b)-W(b)\gamma(b_+).             \tag{15}
\]
The second term needs a covariant difference bound in old tower units.
A condition-number bound for \(u\) does not supply it.
Nor can one set \(u=1\) without changing the stored-coordinate read.
SA 17923–17925 requires that read to be formed with the gauge.
This is the specific estimate needed before the geometric radius budget can be used.

## Result

**Partial proof (first open input); attempt to prove the assumed stage theorem.**
Equations (1)–(8) state the reconstructed stage target and its domain requirements.
The lemma proves admission and the Cauchy estimate on the proposed inverse-image domains.
It does not prove that those domains contain the required fields with uniform room.
No actual ordinary-stage admission is closed.
The first open input is (13)–(14), starting at ordinary stage \(0\to1\):
the complete returned datum must lie in every old (R5) continuation ball on the full complex source.
Consequently the stage theorem, its localized norm bound, B4, and (LOC) remain unproved here.
No counterexample to the actual stage map is claimed.
All arguments are by hand. This text is not yet checked by the other model.
