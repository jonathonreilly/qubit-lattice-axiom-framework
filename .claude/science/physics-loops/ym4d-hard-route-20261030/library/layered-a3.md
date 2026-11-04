# Layered comparison and intrinsic tube margins

Provenance: Codex (GPT-6 family), research session, 2026-11-04, checkout `ada28a0eb`; not an audit and grants no status. Sources: Ethan Sussman and Levent Alpoge, with Claude and Codex as the authors of their text, at `31a47c543775`. Source inputs remain conditional and are unchecked here. Not yet checked by the other model.

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

The missing application is precise. At the **same point**, a target tower can assign scale \(\xi_q\) where the ambient nest assigns \(\xi_{h_q}\).
Equation (4) then gives only \(C L^{2(q-h_q)}P_\sigma(x)\) in target curvature units.
(PX4) compares two points in one nest. It cannot assign distance \(\rho(q-h_q)\) to these two descriptions of one point.
A test through \(x\) contributes its full size to \(P_\sigma(x)\), since its distance is zero.
Thus neither (4) nor the prepared gap supplies the decay required by (5) for this local mismatch.
This diagnoses the proposed estimate; it does not exhibit a bad stage field.

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

## 5. First failing clause

The first failed application is the hypothesis at `wf-c.md:36`: “the single layer j of B”.
Its first use in Lemma C's proof is line 77:

> On the collar l = ξ_j, so [PA] gives ϖ_m ≤ C_Lκ L^{2(m−j)}

Across a seam this becomes the unsummed loss discussed above.
The subsequent real-admission step, `wf-c.md:97`, uses:

> its curvature in B'-local units is at most κ, since ξ' ≤ l.

Across the seam in question, \(\xi_q>l=\xi_{h_q}\). The quoted reason no longer applies.
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

## Result

**Partial proof (first open input), for the layered step sketched by the sources.**
The lifts do not absorb the reversed scale loss; (3) gives the exact failure.
Profile decay pays fixed scale losses when the required distance relation holds, by (5).
Direct target-datum admission replaces the lost restriction for existence, conditionally on (7), and leaves tube distance \(\delta/8\).

The first open input is the uniform real target-datum admission and complex bound (8) for the actual layered stage family.
No full comparison (1), stage inclusion, or counterexample to that family is proved here.
No run discharges a step. This text is not yet checked by the other model.
