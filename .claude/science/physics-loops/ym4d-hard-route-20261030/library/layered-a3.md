# Layered comparison and intrinsic tube margins

Provenance: Codex (GPT-6 family), research session, 2026-11-04; initial note at `ada28a0eb`, continued at `a2aab0ac7909c4a7365d1135906c00af519653e3`. Sections 11–14 and then 15–20 record further continuations at that same checkout. This is research text, not an audit, and grants no status. Sources: Ethan Sussman and Levent Alpoge, with Claude and Codex as the authors of their text, at `31a47c543775`. Source inputs remain conditional and are unchecked here. Not yet checked by the other model.

Pinned texts: [Sussman–Alpoge outline](https://raw.githubusercontent.com/ethanwsussman/Yang--Mills-LLM-experiment/31a47c543775/YM4_sketch_500.tex) and [complete account I](https://raw.githubusercontent.com/ethanwsussman/Yang--Mills-LLM-experiment/31a47c543775/theorem_0_complete_account_raw_I.tex). All SA and CA-I line numbers below refer to these versions.

## 1. Target and source finding

This is input (B) of `stage-resp.md`. Input (A), the actual stage map, remains assigned to `shift-map.md`.
The required Result sections were read first. Source lookup used `sa-index/README.md`, chunks 05, 09–10 and 16, and `obligations.md`.
The CA-I lookup used its index, chiefly chunks 05–06 and 09.
The literature search is reused from `lit-large-field.md:35–52,219–302`; the targeted reads below use the two pinned texts.

The relevant outline proof is a sketch. SA 9913 ends:

> It is here that the argument needs the boundary to run within one layer.

SA 9789 states the layered conclusion under wider gaps and small local profiles: the radii must “dominate $C$ times the profile”.
It does not give the required complex layered comparison there.
CA-I 49502–49511 makes background inclusion an application condition; its first requirement is “must lie in a space”.
The local operator theorem cannot supply that inclusion.

Fix a finite history and all records of `intrinsic-dom.md` section 4, including both erosion rules and every predecessor.
Write \(e=(Z,p,d)\), \(D_e=M_{\mathbf B'_e}(\mathbf U)\), and use its intrinsic map \(T_e(D_e)\).
Let \(\lambda_a=L_\flat^{2e_a}\) be the lift of the particular clause, with its own radius index.
Write \(r_a^{\rm lift}=\lambda_a r_a\), and let \(F_a\) denote the seven normalized readouts in intrinsic-dom (8).

Here is a sufficient layered comparison for T0. On the full earlier-parameter and switch domains, the path supplied by (A) must satisfy, for \(0\le t\le1\),
\[
 \operatorname{dist}_\infty(D_e(t),\mathcal T_e^c)\ge\eta_*>0,
 \qquad
 \|\partial_tF_a\|
 \le C r_a^{\rm lift}\sum_{l\in E_n}
       u_l\sqrt{1+|m-l|}\,e^{-D|m-l|},\quad D\ge\log4.
 \tag{1}
\]
The distance uses the rowwise matrix norm, relative to the complex datum group.
Here \(m\) is the clause's radius index, \(E_n\) its new remake levels, and \(u_l\) the relative forcing size supplied by (A).
Constants must be independent of depth, volume, record, and retained parameters.
The clause roster includes tower curvature and current, real gauge witnesses, and the assigned independent current.
Real gauge witnesses need their own bounds; they have no coefficient (R22).
Returns and node choices must be compatible with the representatives in (A).

The coefficient (R22), SA 6126–6133, contains \(-\beta_R\sum_{l\in\mathrm{Re}_\sigma(x)}2^{-|m-l|}\) and the phase term \(\varpi_\phi\mathsf g_k(m)\).
For fixed lifts, one stage releases \(\mathsf g_k(m)/(2\mathsf N_k)+\beta_R\sum_{l\in E_n}2^{-|m-l|}\).
With \(Cu_l<\beta_R/2\), the readout estimate spends less than half each new mark's allowance.
This is the integration in `stage-resp.md:137–146`; its displayed factor is \(\tfrac12\beta_Rr_a2^{-|m-l|}\).
Reads with no new mark still need its separate phase allowance (6).
Thus (1) is a target, not a claim that the map or all its premises have been proved.

## 2. What the actual lifts pay

SA 6143–6145 specifies “The lift is $L_\flat^{2e_\sigma(x)}$” and excludes real-potential gauge bounds only from (R22).
CA-I 49620–49624 says the power “multiplies every one of the seven entries”.
The gauge bounds are, verbatim in their mathematical content (CA-I 48474–48475),
\[
 \ell_i|A|<\mathsf L_0^{2e}BCM\alpha_{0,i},\qquad
 \ell_i^2|\nabla^\eta A|<\mathsf L_0^{2e}BCM\alpha_{0,i}.
 \tag{2}
\]
The four actual choices are below. In this table only, \(p\) is CA-I's exit-stage level; all four families use \(C=1\).

| Family | Radius index | Exponent | Source quotation |
|---|---:|---:|---|
| G1, \(m<p\) | \(m\) | \((m-k_0)_+\) | CA-I 48533: \(\mathsf L_0^{2\max\{0,m-k_0\}}BCM\alpha_{0,m}\) |
| G2, \(m=p,\ Q\not\subset\Omega_{k_0+1}\) | \(p\) | \((p-k_0)_+\) | CA-I 48541: \(\mathsf L_0^{2\max\{0,p-k_0\}}BCM\alpha_{0,p}\) |
| G3, \(m=p,\ Q\subset\Omega_{k_0+1}\) | \(p\) | \(p-\bar m\) | CA-I 48550, 48558: \(\bar m=\max\{i\le p:Q\subset\Omega_i\}\), \(\mathsf L_0^{2(p-\bar m)}BCM\alpha_{0,p}\) |
| G4, \(m>p\) | \(m\) | \(0\) | CA-I 48564–48565: \(BCM\alpha_{0,m}\), “no power” |

CA-I 49629–49637 gives the matching seven-entry exponents: \((m-k_0)_+\) at index \(m\), \(j-m\) at index \(j\), and zero above \(j\).
Its bound \(0\le e\le n-k_0\le N_0\) (49641) is an **upper** bound.
It gives no lower bound in terms of a tower's loss \(q-h_q\).
Likewise, CA-I 49653's \(\mathsf L_0^{2e}\le\mathsf c_1R_n\) controls the lifted radius, not the reversed scale loss.

Even when the lift exponent equals that loss, it does not absorb it.
SA 17624 specifies \(2\le L_\flat<L/2\). Hence, for \(v\ge1\),
\[
 \frac{L^{2v}}{L_\flat^{2v}}>4^v.
 \tag{3}
\]
CA-I uses the stronger hypothesis \(\mathsf L_0^2\le L/3\) (48904).
There the same quotient is at least \((3L)^v\).
These are algebraic failures of the proposed absorption, not counterexamples to an actual stage.
SA 6148 requires \(c\le c_\sigma\le1+\beta_s\); this bounded coefficient cannot cancel the growth in (3).

The favorable conversion runs the other way: \(L^{-2v}L_\flat^{2v}<4^{-v}\).
This agrees with SA 17624's conversion from scale \(j+1\) to \(j\).
It cannot be reversed to bound a coarser tower from finer ambient control.
Also, G3 keeps radius index \(p\) while \(\bar m\) varies.
One must not infer a bound on lift ratios from the difference of radius indices alone.

## 3. What profile decay does pay

The real critical profile estimate is SA 9681:
\[
 \eta^{-2}l(x)^2|\partial U-1|,\quad l(x)^3|J(U)|
 \le C P_\sigma(x),\qquad
 P_\sigma(x)=\max_\tau e^{-\delta_{\rm prof} d_\sigma(x,\tau)}
                         |\partial\mathbf V(\tau)-1|.
 \tag{4}
\]
Here \(\sigma\) fixes one determining sequence. SA 9678 requires \(U\) to be “critical and regular at a fixed small radius”.
We write its profile rate as \(\delta_{\rm prof}\); \(\delta\) below is the intrinsic tube radius.
For general real factors in a complex pair, use their actual curvature bounds instead.
`a3-profile.md:625–660` proves (4) as an implication from its named background inputs.

Prepared gaps give decay in this metric, not in the cell count \(R_i\).
CA-I 53781 says “separated by one layer” of level-\(i\) \(M\)-cubes.
SA 17401 gives \(\operatorname{dist}_\infty(Z_j,\Omega_{j+1})\ge LM\) in level-\(j\) units.
For two points in one separated nest, each complete intervening layer contributes at least \(\rho\) to \(d_\sigma\).
Indeed, its crossing has length at least \(\rho\xi_r\), with metric density \(\xi_r^{-1}\).
The crossing arcs have disjoint interiors. Thus
\(d_\sigma(x,y)\ge\rho(|i-j|-1)_+\), exactly SA 10628–10631 (PX4).
SA 9916 requires \((\text{rate})\times\rho\ge C\log L\) in the order of choice.

**Summation lemma.** Suppose a response has already been summed over cells, leaving one contribution per shell.
Put \(r=|m-l|\). If its radius conversion costs at most \(e^{br}\), and its profile gives \(e^{-ar}\), then
\[
 a\ge b+\log4
 \quad\Longrightarrow\quad
 \sum_l\sqrt{1+|m-l|}\,e^{-(a-b)|m-l|}\le3.
 \tag{5}
\]
Proof: \(1=4^0\) and \(r+2\le4(r+1)\) give \(1+r\le4^r\) by induction.
Each summand is at most \(2^{-r}\).
There are at most two shell indices at each positive distance. Sum \(1+2\sum_{r\ge1}2^{-r}=3\).
If \(v=r\) in (3), then \(b=2\log(L/L_\flat)\).
The endpoint loss in (PX4) changes only a fixed prefactor.
If a conversion instead includes \(\lambda_{\rm source}/\lambda_{\rm target}\), its growth must be included in \(b\).
This ratio is not automatically controlled by the shell index, as G3 shows.

This is not a new cell-count estimate. SA 10653–10661 already proves that step, conditionally on its kernel bound:
\[
 m_{\rm ker}-\delta_{\rm wt}>(8+|p_{\rm scale}|)\log L/\rho.
\]
The notation here distinguishes its decay rate and scale exponent from our layer indices.

The possible loss is precise. At the **same point**, an unlocalised target tower can assign scale \(\xi_q\) where the ambient nest assigns \(\xi_{h_q}\).
Equation (4) then gives only \(C L^{2(q-h_q)}P_\sigma(x)\) in target curvature units.
(PX4) compares two points in one nest. It cannot assign distance \(\rho(q-h_q)\) to these two descriptions of one point.
A test through \(x\) contributes its full size to \(P_\sigma(x)\), since its distance is zero.
Thus the prepared gap alone does not supply decay for this local mismatch.
This does not show that an actual inherited carrier has the mismatch.
Section 6 below proves that it is absent for several important carrier classes.

## 4. A replacement for restriction, with tube room

For datum admission, equality with the ambient background is unnecessary.
Test the separated target tower directly. The following is an implication from the existing real-admission and averaging results.

Write \(\mathbf U=e^{i\eta w}U\), with \(U\) real, and let \(\xi_e\) be the target tower scale.
Include the full averaging carriers and the seam-test collars. Define
\[
 K_e=\sup_{p'\subset Z}\eta^{-2}\xi_e(p')^2|\partial U(p')-1|,
 \qquad
 W_e=\max\left\{\sup_b\xi_e(b)|w(b)|,
       \sup_{(q,c)}\xi_q\sup_{\mathcal P(q,c)}|w|\right\}.
 \tag{6}
\]
The second supremum includes each intermediate row read by the actual iterated means.
Let \(\varepsilon_{\rm adm}\) be an admitted real-datum threshold with the margin used in intrinsic-dom (5).
`a1-balaban.md:2527–2529` requires that real increments “keep the datum within the larger existence radius”.
Let \(C_0L^2\) be the real averaging constant, and \(r_{\rm AV}\) its small complex radius.
Assume, uniformly over all required records and parameters,
\[
 C_0L^2K_e\le\varepsilon_{\rm adm}/2,
 \qquad W_e\le\min\{r_{\rm AV}/2,\delta/4\}.
 \tag{7}
\]
SA 9667's converse gives “within $2\varepsilon$” inside a layer and “within $CL^2\varepsilon$ across a seam”.
Apply this with \(\varepsilon=K_e\).
Choose \(C_0\) to cover both. Thus \(V_e=M_e(U)\in\mathcal R_e\), with a fixed regularity margin.
This argument needs no containment \(T'_q\subset\Omega_q\).

`wf-c.md:43` gives the averaging bound
\(|\beta_q(c)|\le2\xi_q\sup_{\mathcal P(q,c)}|w|\).
Apply it in the **target** tower, whose real curvature and perturbation now meet its hypotheses.
It gives an actual logarithmic datum
\[
 D_e=M_e(\mathbf U)=e^{ib_e}V_e,\qquad \|b_e\|_\infty\le2W_e\le\delta/2.
 \tag{8}
\]
The depth-uniform averaging implication is also used at `a3-close.md:87`, with bound \(2\xi'_q\sup|w|\).
Intrinsic-dom (5)–(6) now defines the required canonical tower.
This replaces restriction for admission. It does **not** assert that this tower equals \(U|_Z\).
Such an identity needs compatible constraints, the issue assigned to (A).

There is quantitative room. Let a group-valued datum \(D'\) satisfy \(\|D'-D_e\|_\infty<\delta/8\).
Unitarity of \(V_e\), the exponential series, and \(\delta\le1/40\) give
\[
 \|D'V_e^{-1}-1\|
 <\delta/8+\frac{\delta}{2-\delta}<3\delta/4,
 \qquad
 \|\Log(D'V_e^{-1})\|
 <\frac{3\delta/4}{1-3\delta/4}<\delta.
 \tag{9}
\]
The logarithm bound follows by summing its absolutely convergent series.
Hence \(D'\) lies in the same small patch about \(V_e\).
This proves \(\operatorname{dist}_\infty(D_e,\mathcal T_e^c)\ge\delta/8\), uniformly in the number of rows.
No lift enlarges \(\delta\): intrinsic-dom (5) fixes the raw datum radius.

## 5. Limit of the single-layer argument

The first failed application is the hypothesis at `wf-c.md:36`: “the single layer j of B”.
Its first use in Lemma C's proof is line 77:

> On the collar l = ξ_j, so [PA] gives ϖ_m ≤ C_Lκ L^{2(m−j)}

Across a seam this becomes the unsummed loss discussed above.
The subsequent real-admission step, `wf-c.md:97`, uses:

> its curvature in B'-local units is at most κ, since ξ' ≤ l.

If a target tower crosses into a region with \(\xi_q>l\), that reason no longer applies.
The earlier round did not establish such a crossing for an actual stage carrier.
The corresponding restriction step in `a3-close.md:68` explicitly uses
\(T'_q\subset Z\subset X\subset\Omega_j\subset\Omega_q\).
Neither lifts nor smallness of the profile in ambient units restores this containment.
SA 9755 likewise requires the tower to lie “member by member” in the ambient sequence.

For a real critical ambient field, (4) bounds the first quantity in (6) by
\[
 K_e\le C\sup_{x\in Z}(\xi_e(x)/l(x))^2P_\sigma(x).
 \tag{10}
\]
The first open input is to admit every actual \(M_e(U)\) with a uniform real margin, then bound its complex increment as in (8).
Proving (7) on the actual layered carriers would suffice. It is not a necessary condition; direct bounds on the averaged tests could be sharper.
The G1–G4 gauges control their stated cubes and scales. Their classification alone does not prove (7) on every inherited tower carrier.
In particular, (4) is a bound on an admitted critical field, not an estimate for arbitrary real factors throughout the complex source domain.
One must establish these bounds for the actual family, before invoking its tower responses.

## 6. Continuation: the actual direction of the geometric comparison

The continuation read the two pinned source files once, in bounded excerpts.
It first searched the index and read neighbouring rows: SA chunks 05, 09, 10 and 16;
CA-I chunks 05, 06, 09 and 10; and the corresponding obligations.
The earlier literature search is retained. `lit-large-field.md:95–107,280–302` records the QED3/YM3 comparison and its lack of this preparation operation.
Bałaban's CMP 119, pp. 256–257 and 261, was also read from the local paper copy.
The rendered equations were used to repair the text extraction, not to check a proof by computation.

**Expansion of the determining regions.** SA 17415 puts each prepared box in
“\(\Omega_l^c\cap X\)”. Together with (R21), SA 6100–6109, this gives
\[
 \Omega_l^{\nu}\cap X\subseteq\Omega_l^{\nu+1}\cap X.
 \tag{11}
\]
Proof: the changed member replaces \(\Omega_l^\circ\cap X\) by \(X\setminus Z''_l\).
Since \(Z''_l\subset X\setminus\Omega_l^\circ\), the latter contains the former.
All other members are unchanged. Iterate this inclusion for the completed stages.
This argument uses the determining regions. It does not replace them by the action regions.
SA 6110–6111 says the action sequence “governs the sums and the coupling profiles”.

For an earlier birth record, SA 17443–17447 gives the stronger explicit identity
\(\Omega_l^{\nu_\mu}(\mathcal S_t)=\Omega_l(\mathcal S^\mu)\cup Z_{[j,t]}\), \(l\le j\).
Thus birth members also lie in their retained members.
SA 17440 says the current determining choice is \(\nu=n\), while the spaces involve all choices.
Combining this statement with (11) places each retained member inside the current determining member.
These are geometric implications from those formation statements, not a proof of the stage map.

Here is the consequence for carriers. Express all scales in the same physical units.
Let \(O_q\) be an earlier determining sequence and \(\Omega_q\) the current one, with \(O_q\subset\Omega_q\).
Let a level-\(q\) row have an endpoint \(y\in O_q\).
Include its double block, its mean paths, and the fixed extra stencil collar.
Write \(D\xi_q\) for a bound on their sup-distance from \(y\), with fixed \(D\).
Such a \(D\) follows by adding the two block diameters and the fixed collar widths.
SA 9634 calls the row carrier its “double block”. All intermediate means stay in that carrier.
Choose the gap with \(\rho>DL\).
If a carrier point \(x\) were outside \(O_{q-1}\), separation would give
\[
 \rho\xi_{q-1}<|x-y|_\infty\le D\xi_q=DL\xi_{q-1},
\]
a contradiction. Hence \(x\in O_{q-1}\subset\Omega_{q-1}\).
For \(q=0\), the bare scale is already the smallest scale.
Consequently
\[
 \xi_q/l(x)\le L
 \quad\hbox{on every such full carrier}.                 \tag{12}
\]
The same bound covers all its intermediate rows, whose scales do not exceed \(\xi_q\).
For an element inside a memberwise contained tower, the bound is even \(\xi_e/l\le1\).
Its extra stencil can use (12).
This proves (12) for inherited determining rows and for localisations formed by meeting towers with those sequences.
It uses no target response estimate.

The four gauge families have the following exact interpretation.
In G1, \(Q\subset\Omega''_m=\widehat\Omega_m\) (CA-I 48529).
In G2 and G3, \(Q\subset\Omega''_p=\widehat\Omega_p\) (48538 and 48524 with 48489–48493).
In G4, \(Q\subset\Omega_m=\widehat\Omega_m\) (48562).
Thus a sub-tower inside such a cube, cut at depth at most \(m\), has the same bound (12), including its fixed carrier collar.
Here G2 and G3 have \(m=p\).
The proof uses \(Q\subset\widehat\Omega_m\), then the preceding separation argument with \(q\le m\).
It also applies to such a cube retained from an earlier record, since (11) preserves its containment.

**The G3 index does not by itself exhibit an obstruction.** Its old index \(\bar m\) is not the current ambient index.
CA-I 48711–48716 places
\[
 (\Omega_{k_0+1}\setminus\Omega_{p+1})\cap\mathsf Z
 \subset(\Omega''_p\setminus\widehat\Omega_{p+1})\cap\mathsf Z
 \subset\widehat X_p.
\]
The source calls this “the territory of index \(p\)”.
Its proof, CA-I 48780–48789, uses \(Z''_p\subset Z''_k\) and takes complements.
If (4) applies in the current stage nest, its scale on this territory is \(\ell_p\).
Replacing that scale by \(\ell_{\bar m}\) would invent a loss.
If the real field is known to be critical only in the old nest, its old profile cannot instead be read in the current metric.
That change would need a new field estimate.
Equation (3) remains correct algebra. G3 alone proves neither a loss for the current profile nor admission of an old real factor.

This leaves a specific distinction. SA 5696–5698 quantifies over “every subdomain” and both erosions.
It does not say that each resulting pure tower is a memberwise meet with the ambient sequence.
CA-I 9844–9845 instead writes its auxiliary field as
\[
 U_{p,X}=U\bigl(\mathbf B_p(X)\cup\{\Gamma_i\}_{i<p},M^\cdot(\mathbf U)\bigr).
 \tag{13}
\]
CA-I 9954–9962 requires the corresponding reads for every admissible \(X''\subset Y\), “not only for \(X''=Y\)”.
Bałaban, CMP 119, p. 257, (2.14), separately defines the localised determining set by the formula
\[
 (\mathbf B\cap\Omega^{\sim-2})\ \cup
 \bigl(\mathbf B_j(\Omega)\cap(\Omega\setminus\Omega^{\sim-2})\bigr).
\]
It uses the old rows inside and tower rows in the boundary collar.
His next paragraph treats boundaries in several layers by restricting and combining these constructions.
Thus a pure tower, a tower met with a nest, and (13) cannot be identified by their names.
I have not proved that every record required by (1) has the containment used in (12).

## 7. First attack: make the required distance statement explicit

There are two different profiles. The functions \(\varphi_A,\varphi_A^\circ\) are coupling cutoffs.
CA-I 53939–53955 locates their zero sets and the support of their difference.
In particular, “\(\varphi_A=0\) on all of \([A]_i\)” (53945).
Neither that statement nor its proof at 53995–54025 bounds a curvature test.
CA-I 54241–54257 says the integration structure “does not depend on the profiles”.
The exponential datum profile in (4) is a different function, defined in SA 9681 and 9789.
No inference from \(\varphi_A(x)=0\) to \(P_\sigma(x)=0\) is valid.

Let \(h(x)\) be the current ambient layer index.
For each required carrier occurrence, let \(q\) be its target scale index.
For curvature, take each corner that supplies the target element's largest scale.
Taking a supremum over all corners only enlarges (10).
For a row, use its own \(q\) at **every** point of its carrier.
Let \(a_\tau=|\partial\mathbf V(\tau)-1|\).
A sufficient distance relation is, with one fixed integer \(b\ge0\),
\[
 d_\sigma(x,\operatorname{supp}\tau)
 \ge\rho\bigl(q-h(x)-b\bigr)_+
 \quad\text{for all required }(e,q,x)\text{ and all }\tau\text{ with }a_\tau>0.
 \tag{14}
\]
This states the quantifiers which a use of (5) needs for the *whole* datum profile.
For the carriers proved in section 6, it holds with \(b=1\): its right side is zero.
It needs additional content when \(q>h(x)+b\).

Assume (14), \(\sup_\tau a_\tau\le\epsilon_*\), and \(\delta_{\rm prof}\rho\ge2\log L\).
Write \(v=q-h(x)\). For \(v\le b\), the scale loss is at most \(L^{2b}\).
For \(v>b\),
\[
 L^{2v}e^{-\delta_{\rm prof}d_\sigma(x,\tau)}
 \le L^{2b}e^{-(\delta_{\rm prof}\rho-2\log L)(v-b)}
 \le L^{2b}.
\]
Insert this into (10). If \(C_P\) is its fixed constant, then
\[
 K_e\le C_P L^{2b}\epsilon_* ,\qquad
 \epsilon_*\le\frac{\varepsilon_{\rm adm}}{2C_0C_PL^{2b+2}}
 \ \Longrightarrow\ C_0L^2K_e\le\varepsilon_{\rm adm}/2 .       \tag{15}
\]
This proves the requested real admission estimate under the explicit distance relation.
The constants are chosen before depth, volume and history.

Now try to prove (14) by crossing layers. For each test let
\(i_\tau=\min_{z\in\operatorname{supp}\tau}h(z)\).
The disjoint crossing arcs in SA 10628–10631 give exactly
\[
 d_\sigma(x,\operatorname{supp}\tau)
 \ge\rho\bigl(i_\tau-h(x)-1\bigr)_+ .                      \tag{16}
\]
Indeed, every path to every point of the test crosses those complete layers.
Taking the infimum over paths and test points preserves this bound.
Thus (16) implies (14) for tests with \(i_\tau\ge q-b+1\).
It says nothing of that size for tests near \(x\) in a lower ambient layer.
Splitting the maximum in (4) at this threshold leaves, exactly,
\[
 \sup_{(e,q,x)}L^{2(q-h(x))}
 \max_{i_\tau<q-b+1}a_\tau e^{-\delta_{\rm prof}d_\sigma(x,\tau)}.       \tag{17}
\]
There is no sum estimate which removes this maximum.

Here is a hand test of this route's missing implication.
Take \(\Omega_0\) to be a large torus and all \(\Omega_i=\varnothing\), \(i\ge1\).
SA 9599 says: “A member may be \(T_\ell\) or empty”. Separation is vacuous, and all bare bonds are determining rows.
Use the maximal-cube erosion of either kind, retaining the cubes beyond each required gap.
Choose a cubical \(Z\) whose side exceeds twice the finite sum of those gap widths and rounding losses.
Its member at depth \(q\) then contains a cube.
This is an admissible erosion under SA 5598–5604, not a claim that gap inequalities identify an unspecified formation rule.
SA 5605–5610 says: “An assignment specifies the actual sets, not just these inequalities.”
Choose a bare plaquette \(\tau\) in that member.
A real field with one link \(e^{i\epsilon T}\), all other links equal to one, has a nonzero test there.
Here \(T=\operatorname{diag}(1,-1)\), \(0<\epsilon<1\).
Its determining datum fixes every link, so the constrained criticality condition is vacuous.
This uses SA 9616's definition, “stationary along the curves in \(C(\mathbf B,\mathbf V)\)”.
Its nonzero plaquette norms are \(2\sin(\epsilon/2)\), which lie between \(\epsilon/2\) and \(\epsilon\).
The bounds follow from \(\sin t\le t\) and \(\sin t\ge t-t^3/6\), \(0\le t\le1/2\).
At a corner \(x\in\tau\), \(d(x,\tau)=0\), while \(q-h(x)=q\).
Also \(K_e\ge L^{2q}\epsilon/2\).
The field is regular at a fixed small ambient radius: its current is a sum of a fixed number of plaquette defects.
Thus separatedness, criticality and the two erosion rules alone cannot prove (14) or small \(K_e\).

This example is **not** a label of the requested family.
SA 17317 says a label starts at “\(\Omega_0=\Omega_1^\sim\)” and “not at \(T_\ell\)”.
For the empty \(\Omega_1\) used here, that rule would make \(\Omega_0\) empty too.
The example refutes an inference from separatedness alone; it cannot refute the actual stage assertion.
The failed step of this attack is replacing \(i_\tau\) by the unrelated target index \(q\) in (16).
Section 6 repairs that step for contained carriers, but not for the full inherited list.

## 8. Second attack: pay by the running radii, without profile decay

This attack also applies to real factors which are not critical.
Suppose the actual returned splitting has the following *simple* bounds, before any target tower is invoked:
\[
 \eta^{-2}l(x)^2|\partial U-1|\le A_0(x),\qquad
 l(x)|w(x)|\le A_1(x).                                    \tag{18}
\]
Use all plaquette corners and all intermediate row carriers as above.
Direct substitution in (6) proves
\[
 K_e\le\sup_x L^{2(q_e(x)-h(x))}A_0(x),\qquad
 W_e\le\sup_{(q,x)\in\mathcal C_e}L^{q-h(x)}A_1(x).          \tag{19}
\]
Here \(\mathcal C_e\) includes the local-field term of (6) and every row-point occurrence.
In the curvature supremum \(q_e(x)\) means the target element scale for that occurrence.
This proof uses only multiplication by the scale ratio. It uses no average or tower response.
Set \(w_*:=\min\{r_{\rm AV}/2,\delta/4\}\).
For the carriers of section 6, the sufficient choices are
\[
 \sup A_0\le\frac{\varepsilon_{\rm adm}}{2C_0L^4},\qquad
 \sup A_1\le w_*/L .                                     \tag{20}
\]
They prove **both** parts of (7) on that class.
The averaging implication then gives (8); the logarithm calculation (9) gives tube distance \(\delta/8\).
In particular, this complex admission argument comes before all tower responses.

The lifted radii can meet any fixed ceiling of this kind.
For CA-I's displayed stage factors, 48879–48888 bounds
\(\mathsf L_0^{2e}\le c_1R_m\) at the radius index \(m\).
CA-I 49681–49687 applies this to both radii, including the fluctuation radius.
Its exact radius reading is “\(\mathsf c_1R_n\alpha_{\cdot,n}\) in each layer”.
CA-I 49360–49375 already proves the resulting one-sided small-coupling ceiling.
Its conclusion is: “For every fixed \(L\) and \(M\) it can be met by taking the couplings small.”
This source result is a conditional proof, not a new omission in their text.

For completeness, the frame version's limiting step has a short hand proof.
SA 6027 and 6033 specify \(R(y)\) and \(\alpha_{\iota,m}=C_\iota\theta_m^{-1/2}(\log\theta_m)^q\).
The former is “the smallest power of \(L\) not below \((\log y)^r\)”.
They give \(\check R_m\le L(\log\theta_m)^r\).
Any fixed polynomial loss \(C\check R_m^a\) therefore leaves a bound
\(C' e^{-y/2}y^{q+ar}\), \(y=\log\theta_m\).
Choose an integer \(N>q+ar\). The exponential series gives
\[
 e^{-y/2}y^{q+ar}\le 2^NN!\,y^{q+ar-N}\longrightarrow0.
 \tag{21}
\]
This gives one coupling ceiling uniform in \(m\), since every \(\theta_m\ge\gamma^{-2}\).
The lift bound must belong to the same radius system.
CA-I's hypothesis \(\mathsf L_0^2\le L/3\) cannot silently be substituted for SA's weaker bound on \(L_\flat\).

There is a useful extension of (20). If every occurrence with radius index \(m\) satisfies
\[
 L^{(q-h(x))_+}\le C_R R_m^a,\qquad
 A_\iota(x)\le C_A R_m^c\alpha_{\iota,m},                  \tag{22}
\]
with fixed \(a,c,C_R,C_A\), then (19) costs at most
\(C_R^2C_AR_m^{2a+c}\alpha_{0,m}\) and
\(C_RC_AR_m^{a+c}\alpha_{1,m}\).
Equation (21) pays both, without any distance relation.
Thus the exponential loss in (3) is not, by itself, a failure of admission.
A loss confined to a logarithmic window can be paid by the small running radius.

The attempted application fails at two parts of the **same carrier estimate** (19).
The bound \(e\le N_0\) in CA-I 49641 bounds the lift exponent, not \(q-h(x)\) for every inherited tower.
The diagnostic in section 7 lets that latter difference grow while its local ambient radius stays fixed.
Thus a bound of the form (22) does not follow from the erosion rules alone.
Nor does the gauge-family classification state (18) for a returned complex splitting at all earlier parameters.
The seven bounds describe the required space; assuming them for the output would assume the inclusion being proved.
CA-I 49498–49511 explicitly calls this background inclusion a condition that the application “has to meet”.
Thus (20) closes a real subcase, and (22) is a tested alternative, but neither has been verified on the whole source family.

## 9. Third attack: use finite averaging and continuation directly

One might avoid (10) and estimate the datum itself.
The depth-uniform averaging argument used in section 4 gives
\[
 \|b_e\|_\infty\le2\sup_{(q,x)\in\mathcal C_e}\xi_q|w(x)|=2W_e,
 \tag{23}
\]
once the real reference and the means' complex charts are admitted.
Its inputs are exactly the raw carrier bounds in (7), not the target tower responses.
Applying it to (18) reproduces the second inequality of (19).
It does not remove the scale ratio. Using a response of \(T_e\) to bound it would require the tube we are trying to enter.

There is also a direct check of why real profile bounds and holomorphy do not supply the complex estimate.
Work in a commuting subgroup, with \(T=\operatorname{diag}(1,-1)\) and a real site function \(f\).
Set
\[
 g_z(x)=e^{izf(x)T},\qquad
 \mathbf U_z(x,y)=g_z(x)g_z(y)^{-1},\qquad
 w_z(x,y)=z\,[f(x)-f(y)]T/\eta .                          \tag{24}
\]
The real factor of this splitting is \(U=1\).
Every contour product telescopes to its endpoint quotient.
All contours with the same endpoints agree, so every finite mean of them has that same value.
This is the actual mean convention of SA 5631–5643 (R3), with the identity branch.
Induction through the block means gives, for a row \(c\),
\[
 M_e(\mathbf U_z)(c)=e^{iz[f(c_-)-f(c_+)]T},\qquad
 b_e(c)=z[f(c_-)-f(c_+)]T .                              \tag{25}
\]
All plaquette and seam tests are one. In particular the real profile is zero.
For real \(z\), this is a real pure-gauge family.
For \(z=it\), put \(a=|t[f(c_-)-f(c_+)]|\).
The row matrix has norm \(e^a\).
Any row in the intrinsic tube has norm less than \(e^\delta\), since
\(\|e^{iB}V\|\le e^{\|B\|}\) for unitary \(V\) and \(\|B\|<\delta\).
Hence \(a>\delta\) puts this row outside that tube, despite zero curvature.
Choose \(f\) with oscillation \(\operatorname{osc}f=|f(c_-)-f(c_+)|\).
Taking \(|t|\operatorname{osc}f<r_B/2\) keeps **all** row logarithms inside the larger identity continuation patch.
The ratio \(\delta\le r_B/40\) leaves such choices.
This proves a failure of the proposed profile-to-complex-datum implication.
It is not a counterexample to the actual stage source: that source may exclude these \(w_z\) by its own carrier bounds.

The example also prevents a change to a convenient complex gauge from proving the required raw margin.
Real node gauges preserve the row norms; general complex node gauges do not.
For route (7), the actual return must therefore be included in the estimate of \(w\).
Section 19 instead controls its effect directly at the datum nodes.

Conversely, a bound for the actual datum does not prove the stronger carrier supremum \(W_e\).
In the same bare-layer diagnostic, take \(f\) supported at one fine vertex, with value \(a>0\).
At \(z=i\), every row in (25) has \(\|b_e(c)\|\le a\), independent of its length.
The fine potential has size at most \(a/\eta\) and first difference at most \(2a/\eta^2\).
Choosing \(2a\) below the simple source radius and \(a<\delta/4\) puts these data well inside every intrinsic tube.
All field and tower curvatures remain zero: the real pure-gauge identity extends along this small complex path.
But a level-\(q\) row whose full carrier contains a nonzero fine bond has
\(\xi_q\sup|w|=L^q a\).
Thus (23) can lose arbitrarily much while the datum remains small.
This rules out reversing (23) as a bootstrap for (7).
Again the unresolved application question is whether the actual inherited carrier list permits this crossing.

Cauchy continuation from the real locus does not fix this problem.
For example, replace \(z\) in (24) by \(\epsilon\sin(Nz)\).
On the real axis its absolute value is at most \(\epsilon\), for every positive integer \(N\).
At \(z=i/2\) its absolute value is
\(\epsilon\sinh(N/2)=\epsilon(e^{N/2}-e^{-N/2})/2\), which is unbounded.
All these maps are entire and real on the real axis.
Thus real-axis estimates and an identity theorem give no uniform full-disc bound.
A Cauchy argument needs a bound on a larger *complex* source, or a direct bound for the prescribed stage map.
Neither may be supplied by target-tube membership.

The failed step of this third attack is the unproved uniform norm of the actual complex row map, including its return, before its use in (23).
CA-I 54248 names the map \((e^{i\eta\mathbb H_k^{(n)}(b)}\mathbb U,\mathbb J+\mathcal J(b))\).
CA-I 54287 instructs the reader to express the old background through the new one and the collar fluctuation.
Those prescriptions, rather than an arbitrary holomorphic extension of their real locus, are what this estimate must control.

## 10. The single remaining lemma for this admission route

**Lemma IC (uniform transfer to inherited carriers; unproved).**
Fix the construction lengths, admissible formation rules, real background theorem and averaging convention used above.
Then choose the coupling ceiling, independently of depth, volume and history.
Take the actual raw stage map from input (A), not a different holomorphic extension of its real values.
For every stage use the full required source \(D_{n+1}^{\rm req}(X)\) of `stage-thm.md` (12), with its intrinsic domain convention from section 1 here.
Let \(\mathfrak S_n\) include that source and the full parameter set \(\mathcal P_n\) specified at `stage-thm.md:142–147`, plus the prescribed new fluctuation discs.
In particular, retain \(|s_\Delta|<e^{\bar\kappa}\), \(|\nu_F|<\varrho_F\), and \(|\mu_b|<\lambda_l^{\rm st}\).
Near stored fields remain real; far fields keep their stated enlarged radii.
No part of this domain may be removed because an output fails (26).
For every \((P,\zeta)\in\mathfrak S_n\) and every interpolation time \(0\le t\le1\), use the prescribed returned field and its prescribed real splitting
\(\mathbf U_{n,t}=e^{i\eta w_{n,t}}U_{n,t}\).
Use every inherited record of section 1, both erosions, and the full carriers in (6).
Without assuming admission of that record's output tower, prove
\[
 \sup_{n,t,P,\zeta,e} C_0L^2
    \sup_{p'\subset Z_e}\eta^{-2}\xi_e(p')^2
                |\partial U_{n,t}(p')-1|
       \le\varepsilon_{\rm adm}/2,
 \qquad
 \sup_{n,t,P,\zeta,e}W_e(w_{n,t})\le w_* .                 \tag{26}
\]
The real factor must be defined on each full carrier; its prescribed return cannot be discarded.
The suprema include carrier points, not only the eroded sites where a tower readout is tested.
This is one raw-field transfer lemma. It addresses admission, with no derivative estimate or current response.
It is a sufficient route to the margin in (1), not a necessary consequence of that margin.
Its inherited real and averaging inputs would give (8)–(9) with \(\eta_*=\delta/8\).

The three attacks above address (26) in distinct ways.
The metric attack isolates the exact unsuppressed term (17).
The radius attack proves (19)–(22), but lacks their full carrier and returned-field hypotheses.
The analytic attack computes the finite mean (25) and shows why real profiles and continuation cannot replace those hypotheses.
None establishes a counterexample in \(\mathfrak S_n\).

## 11. Second continuation: geometry of full carriers

This continuation again used both indexes before reading the source excerpts.
The additional SA rows are in chunks 05, 10, 16 and 19, with their neighbouring rows and obligations.
The additional CA-I rows are in chunks 05, 06, 09 and 10.
The literature record in section 1 is reused.
The relevant claims in the sources have the following scope:

| Source lines | Short quotation | Use here |
|---|---|---|
| SA 5598–5609 | “cut at depth \(n\)” and “actual sets” | Both erosion rules; supplied geometric data. |
| CA-I 48527–48565 | “\(Q\subset\Omega''_m\)” in G1; analogous inclusions in G2–G4 | Proved classification of local gauge cubes, conditional on the stage nest. |
| SA 17575–17583 | “contained in a cube of \(O(1)\) level-\(i\) cells”; “the boxes are nested” | The quiet-component geometry, part of the operation's definition. |
| SA 17598 | “at no point unfolded” | The core operation is retained. This is not an exclusion of the core from every analytic domain. |
| CA-I 54341–54346 | “face-connected unions of cubes” and “\(X\cap R_n\ne\emptyset\)” | Allowed stage supports need not be single gauge cubes. |
| SA 5696–5724, 6150–6154 | “every allowed \(Z,p,n\)” and “every preceding structure” | The full tower roster that must be treated. |

Here and below geometric arguments use non-wrapping lifts.
SA 17583 supplies these lifts for the operation's boxes.
The tower floor in SA 9658 supplies them for the local cubes under discussion.
All distances in this section are physical sup-distances.

**Full-carrier depth bound.** Write \(T_q\) for a tower member and \(Z=T_0\).
Choose a fixed constant \(D\) that bounds every row carrier, intermediate mean and required stencil by \(D\xi_q\) from its level-\(q\) endpoint.
This is the double-block fact of SA 9634, with the fixed stencil added.
Here the stencil is the fixed plaquette stencil; enlarging an entire gauge cube is not part of this carrier estimate.
For both erosion rules, set
\[
 g=\min\{\rho/L,M_1'\},\qquad g_0=g-D>0.
\]
The order of lengths allows this choice: SA 9916 places \(\rho\), then \(M_1'\), after the one-step constants.
The gap of either rule gives
\(\operatorname{dist}(y,T_{q-1}^{c})\ge g\xi_q\) for \(y\in T_q\), \(q\ge1\).
Since \(T_{q-1}\subset Z\), every point \(x\) of the full carrier satisfies
\[
 \operatorname{dist}(x,Z^c)\ge g_0\xi_q .                 \tag{27}
\]
Proof: distance to a closed set is 1-Lipschitz, so moving by \(D\xi_q\) loses at most that amount.
The same proof applies to a plaquette corner in \(T_q\), with a smaller loss.
Every intermediate carrier lies in this full carrier and has scale at most \(\xi_q\).
Thus (27) also holds with its own, possibly smaller, scale.
Bare rows need no estimate: their scale is at most every ambient scale.

Suppose now that \(Z\subset Q\), where \(Q\) is a printed G1–G4 cube of index \(m\).
Its side is \(M\xi_m\), and it lies in the current \(\Omega_m\), by section 6.
The distance of a point of \(Q\) to \(Q^c\) is at most \(2M\xi_m\).
This loose bound includes the possible one-mesh boundary offset.
Equation (27) therefore gives \(\xi_q\le2M\xi_m/g_0\).
Also \(l(x)\ge\xi_m\), since the whole carrier lies in \(Z\subset Q\).
Fix an integer \(b_Q\ge0\) with
\(L^{b_Q}\ge\max\{1,2M/g_0\}\). Then
\[
 \xi_q/l(x)\le L^{b_Q}
 \quad\text{on every full carrier of every tower in }Q. \tag{28}
\]
No restriction \(q\le m\) was used.
Thus section 6's depth restriction can be removed for these local towers.
Retained cubes have the same property because (11) preserves their containment.

For this entire class, (14) holds with \(b=b_Q\): its right side is zero.
If the real field is critical, (10) and (15) prove real admission at the stated datum ceiling.
More generally, the simple bounds (18) imply both parts of (7) when
\[
 \sup A_0\le\frac{\varepsilon_{\rm adm}}{2C_0L^{2b_Q+2}},
 \qquad \sup A_1\le L^{-b_Q}w_* .                       \tag{29}
\]
This proves complex admission on that class before using a target tower response.

**Protected-core estimate.** There is also a useful bound for much larger towers.
Let \(C\ne\varnothing\) be a closed set disjoint from \(Z\).
Suppose each carrier point satisfies
\(\operatorname{dist}(x,C)\le H R_m l(x)\), with its stated radius index \(m\).
Since \(C\subset Z^c\), (27) gives
\[
 \xi_q/l(x)\le \max\{1,H/g_0\}R_m .                     \tag{30}
\]
Here \(R_m\ge1\); the maximum also covers bare rows.
This uses an upper bound on distance to the excluded core.
It does not use the unsupported lower bound in (14).

The quiet geometry supplies such an upper bound outside its bottom core.
Write \(h_0=k-\mathsf N_k\), \(C=X_{\rm op}\cap Z_{h_0}\), and let \(r=h(x)<k\).
Assume the full carrier lies in \(X_{\rm op}\setminus C\).
Then \(r\ge h_0\): outside \(Z_{h_0}\), a point lies in \(\Lambda_{h_0}\subset\Omega_{h_0}\).
Since current determining regions expand, \(x\notin\Omega_{r+1}^{\rm current}\) implies \(x\notin\Omega_{r+1}^{\rm old}\).
By SA 17577–17583, both \(x\) and \(C\) lie in the old level-\(r+1\) box.
Its diameter is at most \(C_{\rm box}M\check R_{r+1}\xi_{r+1}\), with fixed \(C_{\rm box}\).
The running-minimum rule gives \(\check R_{r+1}\le\check R_r\).
It follows that
\[
 \operatorname{dist}(x,C)\le C_{\rm box}ML\check R_r\xi_r,
 \qquad \xi_q/l(x)\le C_{\rm geom}\check R_r.            \tag{31}
\]
Here (31) applies to towers whose **domains exclude \(C\)**, not merely to readout points outside \(C\).
For \(r=k\) the ratio is already at most one.
Equation (31) proves a polynomial carrier bound for all such exterior towers, including both erosions.
Together with (19), it costs at most \(C_{\rm geom}^2\check R_r^2A_0(x)\) and \(C_{\rm geom}\check R_rA_1(x)\).
The hand limit (21) pays these losses when the simple source bounds have fixed polynomial losses in the same radius system.

**Where this geometric attack stops.** A general inherited \(Z\) is not known to exclude \(C\) or to lie in one printed cube.
CA-I 54341–54346 permits unions of cubes meeting the collar; it gives neither exclusion.
The phrase “at no point unfolded” concerns the stored integral, not each \(Z\) in (R5).
Replacing a carrier that crosses \(C\) by a collection of exterior carriers changes its determining map.
It needs an identity of those maps, including their seam rows and returns.
Neither (27) nor (31) proves that identity.
This is why the argument has not yet verified Lemma IC for the actual full roster.

## 12. Second new attack: pay every compressed-level loss

This attack removes the unknown distance relation on the compressed outer levels.
It also separates the two radius systems used in section 8.
Let \(s=k_\sharp+1\) be the overlap threshold of SA 17624, and put \(d=k-s\).
That line defines it by “\(M\check R_{k_\sharp+1}L^{k_\sharp+1-k}=M\)”.
Hence
\[
 \check R_s=L^d .                                      \tag{32}
\]
This is the SA frame system. No CA-I bound on \(\mathsf L_0\) is substituted for it.
SA 6020–6033 supplies
\(\theta_s\le\theta_m+\bar B(m-s)\) for \(s\le m\),
\(\check R_s\le L(\log\theta_s)^r\), and
\(\alpha_{\iota,m}=C_\iota\theta_m^{-1/2}(\log\theta_m)^q\).
The second inequality follows because the running minimum is at most \(\theta_s\).

**Frame comparison.** There is a constant \(C_R\), fixed before the coupling ceiling, such that
\[
 \check R_s\le C_R(\log\theta_m)^r\qquad(s\le m\le k).
                                                               \tag{33}
\]
Here is a hand proof that does not assume a comparison between the two size systems.
Put \(y=\theta_m\ge e\) and \(B=\max\{1,\bar B\}\).
Then \(\theta_s\le y+Bd\) and
\(\log(y+Bd)\le\log y+\log(1+Bd)\).
For \(r\ge1\), \((a+b)^r\le2^r(a^r+b^r)\) for nonnegative \(a,b\).
For integers \(d\ge1\), choose an integer \(N>r\).
The exponential series with \(c=(\log L)/2\) gives
\[
 (\log(1+Bd))^r\le B^r d^r
       \le B^rN!c^{-N}L^{d/2}=:C_*L^{d/2}.
\]
We used \(d^{r-N}\le1\); \(d=0\) satisfies (33) directly.
By (32), \(z=L^{d/2}\) therefore obeys
\(z^2\le A(\log y)^r+Ez\), with fixed \(A,E\).
If \(z\le2E\), then \(z^2\le4E^2\).
Otherwise \(Ez<z^2/2\), so \(z^2\le2A(\log y)^r\).
Since \(\log y\ge1\), both cases prove (33).

Take any carrier occurrence with ambient index \(h(x)\ge s\), target index \(q'\le k\), and radius index \(m\in[s,k]\).
Then
\[
 L^{(q'-h(x))_+}\le\check R_s
                 \le C_R(\log\theta_m)^r.               \tag{34}
\]
This statement covers arbitrary carrier shapes and every target depth.
It uses the indices of this operation; it is not an identification of earlier records' radius indices.
For this operation, SA 17624 gives \(e\le d+1\) in the overlap cases.
Its weaker hypothesis \(L_\flat<L\) is enough:
\[
 \lambda=L_\flat^{2e}\le L^{2(d+1)}
                  \le L^2C_R^2(\log\theta_m)^{2r}.       \tag{35}
\]
Thus no reversed absorption of the form refuted in (3) is needed.

Suppose the actual simple source bounds at this occurrence are
\(A_\iota(x)\le C_A\lambda\alpha_{\iota,m}\), in the current ambient units.
This is a hypothesis on the returned source, not on the output tower.
Equations (19), (34) and (35) give
\[
 K_{\rm high}\le C\sup_{m\ge s}\theta_m^{-1/2}
                         (\log\theta_m)^{q+4r},\qquad
 W_{\rm high}\le C\sup_{m\ge s}\theta_m^{-1/2}
                         (\log\theta_m)^{q+3r}.          \tag{36}
\]
Here the suprema mean the corresponding carrier occurrences.
Equation (21), with a larger fixed integer \(N\), makes them smaller than
\(\varepsilon_{\rm adm}/(2C_0L^2)\) and \(w_*\), respectively.
This proves both admission estimates on the whole compressed region, conditional only on the stated simple source bounds there.

For CA-I's distinct system, the same conclusion follows from its own hypotheses.
CA-I 48868–48878 states
\(R_s=L^{N_0-1}\) and \(R_s\le(L+1)(m-s)^{\beta_0}R_m\) for \(m>s\), with \(s=k_0+1\).
Since \(m-s\le N_0-1\), the exponential-series argument bounds
\((1+N_0-1)^{\beta_0}\le C L^{(N_0-1)/2}\).
Consequently \(R_s\le C'R_m^2\).
At \(m=s\), this also follows directly from \(R_m\ge1\).
Together with the proved lift bound \(\mathsf L_0^{2e}\le c_1R_m\) at CA-I 49644–49653, this gives
\(K_{\rm high}\le C\sup R_m^5\alpha_{0,m}\) and
\(W_{\rm high}\le C\sup R_m^3\alpha_{1,m}\).
These are again paid by the hand limit in (21), using CA-I's radius definitions quoted at 49348–49366.

**Real critical fields: deriving the simple bound from (10).**
There is no need to assume a second simple curvature estimate if the datum has the following layer bounds.
Write \(i_\tau=\min_{z\in\operatorname{supp}\tau}h(z)\), as in section 7.
For a fixed exponent \(Q>0\), suppose
\[
 a_\tau\le A f_Q(\theta_{i_\tau}),\qquad
 f_Q(y)=y^{-1/2}(\log y)^Q .                            \tag{36a}
\]
Fixed polynomial lifts can be included by increasing \(Q\).
This is a hypothesis about the actual ambient determining datum, not its target tower.
SA 6030–6033 supplies the power-log form of the curvature thresholds and analytic radii.
The verification of (36a) must retain the current nest and the full support of each seam test.

The drift bounds (R19), SA 6020–6024, give
\[
 f_Q(\theta_i)\le C\sqrt{1+|i-h|}\,f_Q(\theta_h)
 \quad\text{at a sufficiently small, fixed coupling ceiling}.
\]
Proof: \(f_Q\) is decreasing for \(y\ge e^{2Q}\), since its derivative has the sign of \(Q-\tfrac12\log y\).
If \(i\le h\), the lower drift bound gives \(\theta_i\ge\theta_h-c_5\).
For \(\theta_h\ge2c_5\), the ratio is at most \(\sqrt2\) when \(\theta_i<\theta_h\), and at most one otherwise.
If \(i>h\), the upper drift gives \(\theta_h\le\theta_i+\bar B(i-h)\).
When \(\theta_i<\theta_h\), the logarithm ratio is at most one and the square-root ratio is at most \(\sqrt{1+\bar B(i-h)}\).
The remaining case again follows from monotonicity.

The native tests also have a fixed width in layer index.
SA 9623 defines them as “plaquette products” with \(\mathcal M(V_{j-1})\) on the finer pieces.
SA 9625 specifies that the construction “omits the inward bonds at every level”.
Let \(a\) be the largest level of an actual determining row used by such a test.
By (R2), it has an endpoint \(y\in\Omega_a\setminus\Omega_{a+1}\).
The four edges, their one-step replacements and their full double blocks lie within \(D_{\rm test}\xi_a\) of \(y\).
Here \(D_{\rm test}\) is fixed: their levels differ by at most one, and each block has fixed diameter in its own units.
Choose \(\rho>LD_{\rm test}\), in the order of SA 9916.
Separation then keeps this support inside \(\Omega_{a-1}\) and outside \(\Omega_{a+2}\).
For the first assertion use \(\operatorname{dist}(\Omega_a,\Omega_{a-1}^c)>\rho\xi_{a-1}\).
For the second use \(\operatorname{dist}(\Omega_{a+2},\Omega_{a+1}^c)>\rho\xi_{a+1}\).
At \(a=0\) replace the first assertion by nonnegativity of the index; empty top members cause no problem.
Thus all support indices lie between \(i_\tau\) and \(i_\tau+2\).
This concerns the determining-datum tests, not the larger history cutoffs.
Equation (PX4), SA 10628–10631, at every support point now gives
\[
 d_\sigma(x,\operatorname{supp}\tau)
       \ge\rho\bigl(|i_\tau-h(x)|-3\bigr)_+ .
\]
Taking an infimum over the support preserves this inequality.
Hence (4), (36a) and the last two bounds imply
\[
 P_\sigma(x)\le C A f_Q(\theta_{h(x)}),\qquad
 \eta^{-2}l(x)^2|\partial U-1|\le C A f_Q(\theta_{h(x)}).
                                                               \tag{36b}
\]
To see uniformity, put \(v=|i_\tau-h(x)|\).
For \(\delta_{\rm prof}\rho\ge\log4\), the factor
\(\sqrt{1+v}\exp[-\delta_{\rm prof}\rho(v-3)_+]\) has a fixed finite supremum, by the same elementary bound used in (5).
Take a maximum, not a sum, over the tests.
Inserting (36b) in (10) and then (28), (31), or (34) proves
\(C_0L^2K_e\le\varepsilon_{\rm adm}/2\) on their respective carrier classes, after the coupling ceiling is lowered once.
This is a real admission proof from the datum profile.
It is conditional on (36a) and criticality in that same current nest.
Different retained inward-bond tests require their own support argument; they are not substituted for these native tests.
It asserts no such profile estimate for an arbitrary real splitting factor on the complex source.

**Where this radius attack stops.** Below \(s\), (34) is false as an inference from (32).
Its exact missing factor is \(L^{s-h(x)}\).
The waiting depth \(\mathsf N_k=\check R_k\) is not the overlap depth \(1+\log_L\check R_s\).
SA 6034 and 17624 define these different integers.
Equation (31) pays the missing factor for towers excluding the bottom core.
It does not pay it for a tower whose full carrier crosses that core.
Also, (36) must be applied to the returned field's simple bounds on the full complex source.
It cannot turn a required seven-entry inequality into an estimate for that returned field.

## 13. Third new attack: estimate the return before averaging

The previous attacks need a bound on the potential after the prescribed complex return.
Here is the exact bound that a return would have to supply.
Use the gauge action of section 9, and suppose the raw field and return are
\[
 \widetilde{\mathbf U}=e^{i\eta a}U,\qquad
 r=e^{i\chi}v,\qquad U,v\text{ real},\qquad\sup|\chi|\le s_0.
\]
Set \(V=U^v\), \(\bar a(b)=\operatorname{Ad}(v(b_-))a(b)\), and
\[
 D_V\chi(b)=\eta^{-1}\{\chi(b_-)-\operatorname{Ad}(V(b))\chi(b_+)\},
 \qquad B_b=|a(b)|+|D_V\chi(b)|.
\]
The returned field has the exact left factor
\[
 \widetilde{\mathbf U}^{r}(b)V(b)^{-1}
 =e^{i\chi(b_-)}e^{i\eta\bar a(b)}
       e^{-i\operatorname{Ad}(V(b))\chi(b_+)}.           \tag{37}
\]
Put \(E=e^{2s_0+1}\).
If \(\eta|a(b)|\le1\), subtracting one in (37) gives
\[
 \big|\widetilde{\mathbf U}^{r}(b)V(b)^{-1}-1\big|
       \le E\eta B_b.                                  \tag{38}
\]
Indeed, separate the middle exponential minus one.
Its norm is at most \(e^{2s_0+\eta|a|}\eta|a|\).
For the remaining two exponentials use the exact identity
\[
 e^A e^{-C}-1=\int_0^1e^{tA}(A-C)e^{-tC}\,dt.
\]
Here \(A=i\chi(b_-)\), \(C=i\operatorname{Ad}(V(b))\chi(b_+)\).
The real link \(V(b)\) preserves norms, so this term is at most
\(e^{2s_0}\eta|D_V\chi(b)|\). This proves (38).

If \(E\eta B_b\le1/2\), the logarithm series gives a returned splitting
\(\widetilde{\mathbf U}^{r}=e^{i\eta w^{\rm ret}}V\) with
\[
 |w^{\rm ret}(b)|\le2E B_b,
 \qquad W_e(w^{\rm ret})\le2E\{W_e(a)+W_e(D_V\chi)\}.    \tag{39}
\]
The definition (6) makes sense for each of these one-forms.
Since \(\eta\le\xi_q\) at every occurrence, a bound
\[
 W_e(a)+W_e(D_V\chi)\le w_*/(2E),\qquad w_*\le1/2,      \tag{40}
\]
also ensures both smallness hypotheses used in (38)–(39).
The real curvature is unchanged by \(v\), so \(K_e(V)=K_e(U)\).
Equations (39)–(40) therefore prove precisely the complex half of (7), before any averaging or target response.
They apply pointwise in all retained parameters when the factorization of the actual return is supplied there.

**Where this return attack stops.** A bound on \(\chi\) alone does not imply (40).
For example, at \(U=1\), let \(\chi=i a_0 fT\), with \(f=1\) at one fine site and zero elsewhere.
Then \(\sup|\chi|=a_0\), but on an incident bond \(|D\chi|=a_0/\eta\).
A level-\(q\) carrier through that bond has contribution \(L^q a_0\) to \(W_e(D\chi)\).
This is the covariant-gradient version of section 9's exact pure-gauge calculation.
It is not an asserted stage return.
It shows exactly why a node-value estimate, or a real curvature profile, cannot prove (40).
CA-I 54248 prescribes the map \((e^{i\eta\mathbb H_k^{(n)}(b)}\mathbb U,\mathbb J+\mathcal J(b))\).
CA-I 54287 calls the re-expression the “shifted background”.
Those prescriptions still need the bound (40) on any inherited carrier not covered by sections 11–12.
Using the response of that carrier's target tower to produce (40) would assume its admission.

## 14. What remains after these three attacks

Lemma IC, with its full source and return quantifiers, remains the single first unproved step.
The new work gives the following precise reductions within that lemma:

1. **Geometric localisation.** Equation (28) proves (14) for every tower inside a printed G1–G4 cube, with no depth restriction.
   Equation (31) proves a polynomial bound for every full carrier outside a quiet operation's bottom core.
   The attempt stops at domains crossing the core: the supplied support rule does not exclude them, and replacing their determining maps is unproved.
2. **Running radii.** Equations (33)–(36) pay every scale loss in the compressed outer region, without (14).
   The attempt stops below that region at the factor \(L^{s-h(x)}\) on a carrier crossing the core.
   The bound on the lift exponent does not bound that factor.
3. **Direct complex return.** Equations (37)–(40) reduce the complex admission estimate to the raw potential and a covariant gradient of the actual return.
   The attempt stops at (40) on the same full carrier roster.
   A value bound for the return is insufficient, as the explicit one-site calculation shows.

These failures concern one estimate, (26), rather than three replacement conjectures.
They do not establish that a prohibited crossing or a bad return occurs in an actual stage history.
The earlier separated-nest example is excluded as a label, as corrected in section 7.
Nor may an inherited carrier be removed merely because it defeats one of these bounds.

The consequence of a proof of (26) remains exact: real averaging admits \(V_e\), complex averaging gives (8), and (9) gives room \(\delta/8\).
The derivative half of (1) would then read the actual forcing from input (A), the weighted response bounds and the shell-distance estimate.
Admission alone proves no derivative estimate, real gauge witness or phase-only allowance.
Thus this continuation does not relabel a proof of admission as a proof of the full layered comparison.

## 15. Third continuation: the remaining real test

This continuation attacks the real half of (26) first.
Failure there would stop the proposed proof of (7), before any complex return.
The following source distinctions matter.

| Source | Quoted mathematical content | Scope |
|---|---|---|
| SA 5696–5703, 5721–5727 | \(Z\subset X,\ p\le j,\ 1\le n\le p\); \(\Phi_{M_{\mathbf B'}(U)}\) | Pure towers, with existence imposed separately. |
| CA-I 9844–9845, 9957–9962 | \(\mathbf B_p(X'')\cup\{\Gamma_i\}_{i<p}\) | Auxiliary problems retain lower determining rows. |
| CA-I 54341–54346 | \(X\subset\Omega_{m+1}^c,\ X\cap\Omega_m\ne\varnothing,\ X\cap R_n\ne\varnothing\) | Filing conditions for stage supports. |
| SA 17575–17583 | \(\Omega_i^c\cap X=H_i^{[8]},\ Z_i\cap X=H_i^{[10]}\) | A quiet component can retain an older core. |
| CA-I 53783–53814 | \(Z''_i=Z_i\ (i\le h)\), \(R_n=Z_{h+n+1}\setminus Z''_{h+n+1}\) | Preparation does not alter the levels below its window. |
| SA 6021–6035, 17334 | \(\mathsf N_k=\check R_k\), \(R(y)=L^{\lceil\log_L((\log y)^r)\rceil}\), \(r\ge2\) | The full waiting depth is much larger than the overlap depth. |

These are definitions, supplied geometry, or conditional results. They are not new proofs of source admission.
The index reads used chunks 05, 07, 09, 11, 16–17 and the nearby obligation rows.
The CA-I reads used chunks 05–06 and 09–10, including their stage-question rows.
The earlier literature record is reused.
Bałaban, CMP 119, pp. 256–257, defines maximal erosion towers and then the different joined localisation (2.14).
Its pp. 261–262 use auxiliary configurations with the retained lower rows.
Those constructions must not be identified with a whole-domain pure tower without a map identity.

I also followed the later-account pointers in stage-thm.md:285–291.
CA-I 116656–116668 supplies layer and current bounds as inputs.
Their displayed sizes are \(B_{\mathbb H}p(y)\) and
\(\ell^3|\mathcal J^\sharp[1](\sigma;b)|\le2K_\chi p\).
At 116700–116719 the bump estimate assumes (D0)–(D2) and its smallness hypothesis.
Only under those hypotheses does it give
\(Q_e^+(x)\le Q_e(x)(1+\pi_\times)+\pi\mathbf r_{e,m(x)}\).
CA-I 119822–119827 assumes that the lettered clauses imply the inherited clauses with room.
Its exact clause is \(\mathfrak L_{n'}\Rightarrow\text{the clauses of }T\) at \(Z^{\rm on}\), with unused room \(\rho_m\).
The proof at 119958–119985 then adds a bounded increment to a smaller threshold.
The displayed threshold identity there is
\(\theta^{(n)}_{T,a}+\iota_n^a\mathbf r_a^T=\theta^{(n-1)}_{T,a}\).
It is a conditional threshold argument, not a proof of the real carrier bound below.
In particular, 117592 retains the real factor: \(\Delta_5=\Delta_8=0\).
That preserves an existing real bound. It cannot create one in a larger tower scale.

## 16. Geometry attack: test a support which contains the quiet core

The support condition does not imply exclusion of the core.
Here is the precise geometric test, without a claim about its field weight.
Take a quiet component born at a level \(h\ge2\), with no earlier creations.
SA 17583 includes a component with one creation at \(h=k-\mathsf N_k\) in the operation's class.
Then \(\Omega_1\) can be the torus, so \(\Omega_0=\Omega_1^\sim\) is also the torus.
This obeys the initial-member rule which excluded section 7's diagnostic.
In the central part of \(\Omega_h^c\), the ambient index is \(h-1\).
Preparation leaves this fact unchanged, by CA-I 53784 and (R21).

Choose a large, non-wrapping cube union \(Y\) of \(\pi_k\).
Let it contain the component, its first collar, and a point of \(\Omega_k\).
The torus can be enlarged first, with all these sets fixed in a common lift.
Then its filing index is exactly \(k\).
Indeed, \(Y\subset\Omega_{k+1}^c\), while \(Y\cap\Omega_k\ne\varnothing\) excludes every smaller index.
It also meets \(R_0\). Thus it meets all three conditions at CA-I 54343–54346.
Connectedness follows because \(Y\) is a rectangular cube union.

For the maximal erosion rules, a fixed enlargement of \(Y\) makes its depth-\(k\) member contain the core.
Here is a direct size bound.
At step \(i\), retain every permitted cube beyond the required gap.
Removing a gap and rounding to full cubes loses at most
\[
 c_i=\begin{cases}
 (\rho+1)\xi_{i-1}+\mathfrak M\xi_i,&\text{first rule},\\
 2M_1'\xi_i,&\text{second rule}.
 \end{cases}
\]
The additional \(\xi_{i-1}\) makes the first gap strict.
Induction gives
\[
 \{x:d_\infty(x,Y^c)>E_k\}\subset T_k(Y),\qquad
 E_k=\sum_{i=1}^k c_i\le C_{\rm er}\xi_k.                 \tag{41}
\]
For the induction, a point beyond the previous loss plus \(c_i\) has its whole level-\(i\) cube beyond the gap.
The geometric series \(\sum_{i=1}^k\xi_i\le L\xi_k/(L-1)\) proves the last bound.
Choose \(Y\) to contain the core plus this fixed collar and the row stencils.
Both maximal assignments are compatible with translations of the fixed partitions and common non-wrapping lifts.
The second-rule construction is also the maximal-tower construction on Bałaban's p. 256.

At a test \(\tau\) inside the retained core, take \(x\in\operatorname{supp}\tau\).
For this geometric candidate, \(q=k\), \(h(x)=h-1\), and
\[
 d_\sigma(x,\operatorname{supp}\tau)=0,\qquad
 q-h(x)=\mathsf N_k+1.                                  \tag{42}
\]
Thus (14) would force every such test to be exactly flat once \(\mathsf N_k+1>b\).
Neither a gap nor a small positive radius forces exact flatness.
The cutoff profiles do not do so either: CA-I 53943–54025 proves facts about their scalar values.
It gives no identity \(\partial\mathbf V(\tau)=1\).

This completes the geometric test. It does **not** give an actual stage counterexample.
The filing rule lists permitted supports; it does not prove that a term requires this record on each such support.
Also, a supplied erosion rule must be used as supplied, by SA 5605–5610.
If the record uses a meet or the auxiliary map in section 15, replacing it by \(T_k(Y)\) is invalid.
The exact failed step is identifying this permitted whole-domain tower with a required inherited record at a valid stage evaluation.
G1–G4 cannot resolve that step: they classify individual cubes, not this identification.

## 17. Radius attack: the waiting-depth loss grows at small coupling

The missing factor below the overlap region cannot be paid by the same limit as (21).
This can be proved on allowed frames, without numerical estimates.
Let \(N=L^v\), fix \(a\in(L^{-1},1)\), and put
\[
 y=(aN)^{1/r},\quad X=e^y,\quad k=N+2,\quad
 \theta_i=X+B(k-i),\quad 0\le i\le k,                    \tag{43}
\]
where \(\underline\lambda\le B\le\bar B\) is fixed.
This frame satisfies the drift bounds in SA 6021–6024.
For any fixed coupling ceiling \(\gamma\), take \(v\) large enough that \(X\ge\gamma^{-2}\); the frame then satisfies the range bound as well.
For sufficiently large \(v\), all its radii equal \(N\).
To prove this, first note \((\log X)^r=aN\in(N/L,N)\).
Also
\[
 0\le\log(X+B(N+2))-\log X\le B(N+2)e^{-y}=o(1).
\]
The last limit follows from the exponential series: choose an integer \(d>r\) and use \(e^y\ge y^d/d!\).
The distance from \(y\) to the upper endpoint \(N^{1/r}\) tends to infinity.
Therefore every \((\log\theta_i)^r\) remains in \((N/L,N)\).
The running-minimum rule now gives \(\check R_i=N\), hence \(\mathsf N_k=N\) and \(h=2\).

Fix \(Q\ge0\). For large \(v\), \(X\le\theta_1\le2X\), so
\[
 L^{2(k-1)}\theta_1^{-1/2}(\log\theta_1)^Q
 \ge 2^{-1/2}L^{2(N+1)}e^{-y/2}y^Q
 \longrightarrow\infty.                                \tag{44}
\]
Indeed \(r\ge2\) gives \(y/N\to0\).
Eventually \(y/2\le N\log L\), leaving at least \(2^{-1/2}L^{N+2}y^Q\).
The local datum radius itself still tends to zero, by (21).
Both statements hold at arbitrarily small coupling, with all construction constants fixed.

This calculation is the reverse of the compressed-region estimate (36).
There only \(\log_L\check R\) levels were lost. Here the candidate loses \(\check R\) levels.
The coefficient (R22) stays bounded, and the printed lifts occur above the overlap threshold.
They supply no suppression \(L^{-2N}\) of a lower-core datum.

This attack rules out paying the *uncontrolled upper envelope* merely by lowering the coupling ceiling.
It does not prove that the actual field attains that envelope.
The failed step is assigning a fixed positive fraction of a local radius to an actual inherited core test.
A lower bound or a source-realisation argument is needed for that assignment.
The next attack constructs the datum itself.

## 18. Constraint attack: a nonflat datum with identity next average

**Finite lemma.** For fixed odd \(L\ge3\), there is a real nonflat field supported in one block whose next average is identity.
Its amplitude can be made arbitrarily small.
This uses the actual map (R3), SA 5631–5645, equivalently (QC1)–(QC3), SA 7945–7984.
It does not replace that map by its derivative.

Work temporarily at unit spacing. Let \(B\) have \(L^4\) vertices.
Let \(E_B\) be the positive bonds with both ends in \(B\).
There are \(4(L-1)L^3\) such bonds.
Put \(T=\operatorname{diag}(1,-1)\), and set
\[
 V_z(b)=e^{iz a(b)T},\qquad a\in\mathbb R^{E_B},\qquad
 a(b)=0\quad(b\notin E_B).
\]
Every transport commutes.
On the small branch its contour mean is the exponential of the arithmetic mean of its path sums.
Substitution in (R3) therefore gives the **exact** formula
\[
 \mathcal M(V_z)(c)=e^{iz(Qa)(c)T}.                       \tag{45}
\]
Here \(Q\) is a fixed real linear map.
More explicitly, let \(\overline a(y,x)\) be the mean of the oriented path sums from \(y\) to \(x\), and set
\(\sigma_a(y)=L^{-4}\sum_{x\in B(y)}\overline a(y,x)\).
Substitution into (QC3) gives
\[
 (Qa)(c)=\sigma_a(y)+L^{-4}\sum_{x\in B(y)}a([x,x+Le_\mu])
                      -\sigma_a(y+Le_\mu).
\]
This is the row printed in SA 8183–8189 as (QC15).
Here the cancellation is exact, since all factors commute and all logarithms stay on the small branch.
Only the eight coarse bonds incident to the block's centre can read \(a\).
This follows from the double-block support in SA 7949–7955.
Consequently \(\dim\ker Q\ge4(L-1)L^3-8\).

The subspace of curl-free cochains on \(B\) has dimension \(L^4-1\).
To see this, sum a cochain along coordinate paths from one vertex.
Interchanging two adjacent coordinate steps changes the sum by one plaquette curl.
Zero curls thus give a site potential, unique after fixing its value at the base vertex.
Conversely its gradient has zero curls.
For \(L\ge3\),
\[
 4(L-1)L^3-8-(L^4-1)=L^3(3L-4)-7>0.
\]
Thus \(\ker Q\) contains a cochain with a nonzero curl on an internal plaquette \(p_*\).
Fix one, normalize \(\|a\|_\infty=1\), and put \(d_*:=|(da)(p_*)|>0\).
These choices depend only on \(L\).
All contour lengths are bounded at fixed \(L\).
Choose a fixed \(z_*>0\) so that their logarithms stay on the small branch and \(4z_*\le1\).
For real \(0<z<z_*\), (45) and the elementary sine bounds give
\[
 \mathcal M(V_z)=1,\qquad
 |\partial V_z(p_*)-1|
 =2\left|\sin\frac{z(da)(p_*)}{2}\right|
 \ge z d_*/2.                                           \tag{46}
\]
This proves the lemma by finite linear algebra and exact group identities.
No matrix was found by search or numerical computation.

Place this datum at level one, in the interior of the proposed core of section 16.
Retain its level-one determining rows and put identity on all other determining rows.
The native tests are \(O_L(z)\)-regular: they read only a fixed number of these factors.
With the real background theorem as input, there is a regular critical \(U_z\) for this datum.
Its average on the four retained bonds of \(p_*\) is \(V_z\).
The following conclusion needs no estimate for the proposed target tower response.

Suppose the full fine patch of that averaged plaquette lies in \(T_k(Y)\).
Let \(m_0\) be the maximum fine plaquette defect on that patch.
The real one-step averaging bound gives \(z d_*/2\le C_L m_0\).
This is the one-step use of the converse at SA 9667, with its own fixed seam factor.
Its local form follows by putting a real field in a comb gauge on the fixed rectangular patch.
Each non-tree link is a product of a fixed number of plaquettes.
To obtain that product, commute successive coordinate steps of the comb; each exchange inserts one plaquette.
For a fixed patch the number of exchanges is bounded in terms of \(L\) alone.
Unitarity bounds each product defect by the sum of its plaquette defects.
For the mean, SA 8031–8038 gives the explicit fixed-point bound
\[
 Z=\overline X+\frac1n\sum_j E(X_j,Z),\qquad
 \max_j\|X_j\|\le t\ \Longrightarrow\ \|Z\|\le2t.
\]
The exponential and logarithm series prove this on a fixed small ball, as in SA 8004–8026.
Thus each mean of the short transports remains \(O_L(m_0)\) from identity.
Apply this bound to the internal contour means, then to the closed logarithms and final transport in (QC3).
It follows that the coarse plaquette defect is at most \(C_Lm_0\).
If \(m_0\) is above that fixed small neighborhood, enlarge \(C_L\) and use the trivial upper bound two.
Thus the local bound holds in either case.

Since the target scale on this patch is \(\xi_k\),
\[
 K_e(U_z)\ge c_L L^{2k}z .                              \tag{47}
\]
Here \(\eta=L^{-k}\), and \(c_L>0\) includes \(d_*/2\) and the one-step constant.
Also the nonzero native test has zero distance from itself.
Thus this candidate violates (14), and (47) violates (7) for large \(k\) at fixed \(z>0\).
Taking \(z=C_{\rm seed}A_1\theta_1^{-1/2}(\log\theta_1)^{\mathfrak p_0}\) along (43) retains the violation by (44), with \(Q=\mathfrak p_0\).
The real datum remains arbitrarily small in its own units.

**Attempt to make this an actual history.** Identity at level two satisfies the next averaging constraint exactly, by (46).
Block axial gauge preserves that identity when the gauge equals one at the block centres.
It preserves the nonzero plaquette as well.
Thus this is a nonflat fluctuation over identity, not the pure-gauge diagnostic of section 9.
This reaches the averaging constraint needed for a fluctuation-test construction.
It also reaches a nonpivot test, as follows.

Use the specified block axial gauge, formed with the contour mean, as SA 9676 requires.
In the commuting subgroup this mean is the exponential of the arithmetic mean of the path sums from the block centre.
Taking these means as the site gauge sets each mean contour transport to identity.
After this gauge, every link has the form \(e^{iz a'(b)T}\), with \(a'\) fixed and \(\|a'\|_\infty\le C_L\).
The internal curl at \(p_*\) still equals \((da)(p_*)\).
One of its four bonds therefore has \(|a'(b)|\ge d_*/4\).
All four bonds are nonpivots: SA 8167–8170 places each pivot across a block face,
\[
 b_0(c)=(y+he_\mu,y+(h+1)e_\mu),\qquad h=(L-1)/2.
\]
For small \(z\), the selected bond has
\[
 |V_z^{\rm ax}(b)-1|\ge z d_*/8.                         \tag{46a}
\]
Choose \(z=C_{\rm seed}\delta_1\), with fixed \(C_{\rm seed}>16/d_*\).
At \(V_2=1\), the localised one-level background is identity in block axial gauge.
This uses the real background input with identity data.
SA 9667 states that its orbit is \(\{\mathbf1^u\}\), and 9676 says both representatives equal identity there.
The test in SA 17317 is
\[
 \chi'_1(\square)=
 \mathbf1\{|V_1(\mathcal M U_{2,\square}(V_2))^{-1}-1|<2\delta_1\},
\]
on the stated nonpivot bonds.
Hence a test cube containing \(b\) fails this test.
At the same time all plaquette defects of \(V_z^{\rm ax}\) are at most \(4z\), by real-gauge invariance and \(\|a\|_\infty=1\).
SA 6032–6033 gives \(\delta_1=(A_1/A_0)\varepsilon_1\).
The allowed floor \(A_0>4C_{\rm seed}A_1\), consistent with \(A_0\gg A_1\) at SA 19480, makes those defects less than \(\varepsilon_1\).
Each fixed one-level datum test is also \(O_L(z)\), since its paths have fixed length.
A further fixed increase of this floor meets all those test bounds.
Small coupling makes \(z<z_*\) and validates (46a).
This is a regular exact pair with a failed approximate fluctuation test.
It does not yet give the whole quiet history through level \(k\).

SA 17336 gives the next obstruction.
The third test, collar tests and rim tests use
\(\mathcal A_i=i^{-1}\log(V_i(V_i^{\rm bg})^{-1})\).
The true mixed background enters \(V_i^{\rm bg}\).
The equality \(\mathcal M(V_z)=1\) does not imply \(V_i^{\rm bg}=1\) on the later shells.
Those lower rows are still present in the mixed problem.
The real response bound at SA 9734–9740 can estimate the tail only after the constraints and returning nodes of that problem are matched.
It does not identify the mixed problem with the identity-datum problem.
The nonpivot issue is settled by (46a).
The later mixed-background tests and their prescribed returns are not settled by it.

The failed step is precise: (46) has not been placed in \(\mathfrak S_n\) with the proposed inherited tower record.
A complete retained history realising the seed and requiring that record would suffice; it has not been constructed.
Without that step, (47) is a conditional obstruction, not a counterexample to an actual stage family.
It also explains why coarse averaging alone cannot prove the requested \(K_e\) bound.
An average can erase a datum while its lower-scale curvature remains.

## 19. Complex admission by values at the tower nodes

Section 13 bounds a return through its covariant gradient because it seeks \(W_e\).
There is also a route directly to (8).
Only values at the target nodes enter the returned datum.
This does not prove the \(W_e\) inequality of (7).

Fix a record \(e\). Suppose its **raw** mean is already defined and satisfies
\[
 M_e(\widetilde{\mathbf U})=e^{ib}V,\qquad
 V\in\mathcal R_e,\qquad \|b\|_\infty\le b_0.
\]
Let the actual return, restricted to its nodes, have the factorisation
\[
 r(x)=e^{i\chi(x)}v(x),\qquad v(x)\text{ real},\qquad
 \sup_{\operatorname{nodes}(e)}|\chi|\le\chi_0 .
\]
These are inputs about raw means and return values, before a target background response.
The small complex gauges must stay in the regular mean branches.
Gauge covariance then gives \(M_e(\widetilde{\mathbf U}^{\,r})=M_e(\widetilde{\mathbf U})^r\).
For completeness, each contour product transforms by its endpoint factors.
The equation defining its mean is covariant under these factors.
The logarithm in (R3) is conjugated at its base point.
Thus the assertion follows from SA 5631–5649, first locally and then throughout the specified common branch.
SA 8046–8049 states this qualification explicitly: the transformed families must remain in their analytic domains.

Write \(V^v(c)=v(c_-)V(c)v(c_+)^{-1}\).
This is an admitted real datum, by real-gauge covariance.
Row by row,
\[
 \begin{split}
 M_e(\widetilde{\mathbf U}^{\,r})(c)V^v(c)^{-1}
 &=e^{i\chi(c_-)}
   e^{i\operatorname{Ad}(v(c_-))b(c)}
   e^{-i\operatorname{Ad}(V^v(c))\chi(c_+)} .
 \end{split}                                             \tag{48}
\]
Set \(s=b_0+2\chi_0\).
Telescoping this product and using the exponential series gives
\[
 \|M_e(\widetilde{\mathbf U}^{\,r})V^{v,-1}-1\|_\infty
 \le e^s-1.
\]
For \(0\le s\le1/4\), the logarithm series then gives
\[
 \left\|i^{-1}\Log\{M_e(\widetilde{\mathbf U}^{\,r})V^{v,-1}\}\right\|_\infty
 \le\frac{e^s-1}{2-e^s}
 \le\frac{s}{1-2s}\le2s.                                \tag{49}
\]
The middle inequality uses \(e^s\le(1-s)^{-1}\).
In particular,
\[
 b_0\le\delta/8,\qquad \chi_0\le\delta/16
 \quad\Longrightarrow\quad \|b_e^{\rm ret}\|_\infty\le\delta/2 .
                                                               \tag{50}
\]
Equation (9) now gives the same distance \(\delta/8\) from the tube boundary.
No depth or number of rows occurs in this proof.
No covariant derivative of the return occurs either.

This is a useful correction to the route, not a correction to (39).
A value bound is insufficient for \(W_e\), but is sufficient for the effect of a return on an already admitted raw datum.
SA 5733–5736 still prevents using complex gauge invariance as domain admission: the core is not saturated under that action.
Equation (50) supplies an explicit small neighborhood where the datum conclusion does hold.

The source's straightening estimate does not complete its application.
SA 11554 assumes local gauges in the scale of the very row being considered.
At 11583 it assumes \(\xi\|A\|_\infty\le r\).
Only then do 11587–11591 bound the gauge products by summing the raw radii.
Applying that argument to a core-crossing target row would reintroduce the unproved carrier estimate.
Thus (50) is a proved alternative sufficient condition for (8), not a bound for the actual return.

## 20. The precise step left by this continuation

Here is the smaller first step inside Lemma IC.
It is stated with the same source quantifiers, not with the test data substituted for them.

**Lemma RC (real curvature on inherited carriers; unproved).**
Fix the supplied formations, both actual erosion assignments, and the real background and averaging inputs.
There is a coupling ceiling \(\gamma_*>0\), independent of cutoff, torus, history and stage, with this property.
Take the full source \(\mathfrak S_n\) of section 10 at couplings below \(\gamma_*\).
Use its prescribed splitting and return, including at complex values of its allowed parameters.
For every inherited record \(e\) and every interpolation time,
\[
 \sup_{(P,\zeta)\in\mathfrak S_n}
 \sup_{0\le t\le1}\sup_{p'\subset Z_e}
 \eta^{-2}\xi_e(p')^2|\partial U_{n,t}(p')-1|
 \le \frac{\varepsilon_{\rm adm}}{2C_0L^2}.              \tag{51}
\]
In particular this must hold on the real, zero-fluctuation slice.
The real field need not be critical at all complex source points.
For critical points, (10) is an available sufficient estimate, with the metric of that same critical problem.
The statement cannot change the prescribed return or discard a record.

This is exactly the real half of (26).
It is one substep of that sufficient route to (1), not a necessary consequence of (1).
It asserts neither complex admission nor the derivative comparison.
It is the first stopping step here.
The three attacks below first test its necessary restriction to a real critical source field.

1. **Geometry, section 16.** The quiet geometry and support filing allow the candidate (41)–(42).
   The distance relation can hold there only if the local tests are flat or the whole-domain tower is absent.
   The attempt fails to identify that pure tower as a required record on an actual source evaluation.
   It therefore proves neither universal separation nor an actual counterexample.
2. **Running-coupling smallness, section 17.** The explicit frames (43) obey the drift and waiting rules.
   Their worst scale envelope diverges by (44).
   Lowering the coupling ceiling alone cannot pay it.
   The attempt fails because an upper envelope gives no lower bound on an actual field.
3. **Exact constrained data, section 18.** The commuting construction solves the real nonlinear averaging constraint exactly.
   With the retained lower rows, (47) forces large target-scale curvature.
   The attempt fails at its embedding into the complete history and inherited roster.
   The nonpivot failure is proved in (46a), but the later mixed-background tests and the actual inherited record are not verified by the identity next average.

These are failures of proposed proofs and of a proposed counterexample.
They do not show that (51) is false.
The new complex calculation (48)–(50) also leaves (51) untouched.
If both parts of (26) are proved, sections 4 and 7 give (8)–(9).
Alternatively, real admission plus the actual raw-datum and node bounds (50) gives those same conclusions directly.
Neither route supplies the derivative half of (1), its real gauge witnesses, or its assigned current.
Those still require the matched map and forcing from input (A).

## Result

**Partial proof.** This continues the layered step sketched by the sources. It grants no status.
The first remaining step is Lemma RC (51), the real curvature bound in route (7).
Sections 16–18 attack it by the geometry of permitted supports, explicit allowed frames, and exact nonflat data with identity next average.
Section 20 states exactly why each attack stops.
The constructed datum is not yet a counterexample on an actual stage source.

New proved results are (41), the growth estimate (44), the finite nonlinear-mean lemma (45)–(46), its nonpivot test (46a), and the conditional lower bound (47).
The node estimate (48)–(50) gives complex tube room \(\delta/8\) from an admitted raw datum and a small prescribed return.
It needs no target response and does not require a bound for \(W_e\) after the return.
The earlier positive carrier estimates remain valid on their stated classes and hypotheses.

The actual full source has not been shown to satisfy (7) or the alternative (50).
Thus (8)–(9) and the full layered comparison (1) remain conditional there.
Credit remains with Ethan Sussman and Levent Alpoge, with Claude and Codex as authors of their source text, and with Bałaban for his constructions.
All new arguments are written by hand. No run discharges a step.
This text is not yet checked by the other model.
