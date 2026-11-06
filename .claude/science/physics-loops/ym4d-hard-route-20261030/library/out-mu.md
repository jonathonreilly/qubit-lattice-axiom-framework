# Uniqueness of the regular axial minimizer and nesting on window subdomains

## Scope and inputs

This note proves your account's `4.13:lem-minimizer-unique` in its regular-real and continued-complex meaning, with the ceilings below.
All account and outline line numbers refer to commit `31a47c543775`. CA-I, CA-II and CA-III denote your complete account.
The target is CA-I 45162–45201. Your outline states the regular orbit and restriction at 9660–9667 and 9776–9781; 9913 sketches restriction.

Use the fields and input conditions of Tadeusz Balaban's CMP 109, Lemma 4, on \(\square_0=\tilde\square^5\).
Let \(Z\subset X\subset\tilde\square^2\), with \(X\in\mathbf D_j\) and \((p,Z)\in\mathfrak T_j(X)\), and let \(1\le n\le p\le j\).
The outer tower is \((\square_q)_{q\le j}\), with \(\square_j\supset\tilde\square^4\). All grids, roots, outward bonds and seam readouts keep your conventions.
The inner tower is \(\mathcal T=\boldsymbol\Omega^{\mathfrak r}(Z,n)\), for either rule of your `4.8:def-tower-rules` (CA-I 32839–33043):
\[
\begin{array}{ll}
\mathfrak r_1:&\Omega_q\text{ consists of }\mathfrak M L^q\text{-cubes},\quad \operatorname{dist}(\Omega_q^c,\Omega_{q+1})>R_1\mathfrak M L^q\quad(0\le q<n),\\
\mathfrak r_2:&\Omega_q\text{ consists of }M_1L^q\text{-cubes},\quad \operatorname{dist}(\Omega_q,\Omega_{q-1}^c)\ge M_1L^q\quad(1\le q\le n).
\end{array}
\]
Each member is maximal under its rule. Empty terminal members are allowed. Retain \(R_1\ge\max(L,4d)\), \(L\ge4d\), \(M_1/\mathfrak M\ge R_1\), and \(M\ge2LR_1M_1\).
Use Balaban's actual group averages and auxiliary potential average \(Q\). This note makes no transfer to the outline's symmetrised replacement.

**Published inputs, not re-proved here.** Tadeusz Balaban, CMP 98, Propositions 2, 4 and 6 supply real data tests and analytic averaging.
For Proposition 4, use (131), (134)–(135); for Proposition 6, use (159)–(164), with the zero-curvature reference in (52).
Tadeusz Balaban, CMP 102b, Theorem 1 supplies existence, regularity and uniqueness of the critical orbit.
Its (8) is the regular variational space; its (6) is the uniqueness space, with \(B_3\varepsilon_1\le\varepsilon_0\le a_0\), \(\varepsilon_1\le a_1\).
Its §G, Proposition 9, (172)–(173) and (181) supply the holomorphic chart, value bounds and gauge covariance.
The derivative estimates (189)–(190) are not inputs to this proof.

We reuse your tower geometry, your real refinement lemma `9.3:lem-refinement` (CA-III 36939–37000), and your literal-frame proof.
From `4.5:lem-literal-frame` we use only (AX1), (AX2-poly) and the chart-admission paragraph of (AX3), proved at CA-I 17673–17770.
Those clauses use the published real averaging and contour estimates recorded there, including CMP 102b §F (145)–(151), (160), and CMP 99a (1.65).
They do not use the derivative hypothesis (A), the complex-curvature strengthening, the pointwise clause (AX2-pt), or the nesting conclusion.
Conditions (i)–(ii) of the input space supply the real field and twist. Condition (iii) and the output hereditary clause do not supply admission.

**Ceilings and their order.** Fix \(d,G,\beta,L\), the propagator and averaging constants, block sizes and gaps in your order.
Keep your order \(C_1,C_H,\bar\varepsilon_1\). Choose \(\varepsilon_*>0\) below the thresholds of CMP 102b Theorem 1 and §G, with \(\varepsilon_*<\bar\varepsilon_1\) and \(B_3\varepsilon_*<a_0/4\).
Choose a uniform base-one chart radius \(0<r\le\min(1/4,C_1\varepsilon_*/4)\), and put \(K=B_5\varepsilon_*/r\).
Let \(a_{98}>0\), \(C_A\ge1\) be the rescaled averaging constants used below. Shrink \(a_{98}\) to fit all identity logarithms and \(a_{98}\le\log(4/3)\).
Put \(C_D=4C_AL\). Let \(C_7\ge2\) be your converse data-test constant (CA-I 17533).
Choose \(\delta>0\), independently of all depths and domains, and set \(\epsilon_W=B_3C_D\delta\), so that
\[
\delta<r/2,\quad K\delta<a_{98}/2,\quad C_AK\delta<r/2,\quad L\delta<a_{98}/2,
\qquad C_D\delta<a_1/2,\quad C_7\epsilon_W<a_1/2,\quad B_3C_7\epsilon_W<a_0/2,\quad\epsilon_W<a_0/2. \tag{1}
\]
Next choose \(B^{(109)}\) and \(M\) with your existing floors. There is no upper bound on \(M\).
Retain all Lemma 4 restrictions and the literal-frame ceilings used by the three clauses above (CA-I 17519–17597).
In particular, retain \(\alpha_1'''\le\min(\alpha_1^{(98)},1)\), \(2C_vM\alpha_1'''\le1/6\), and the real-curvature threshold of CMP 98 Proposition 2.
Here \(C_v,C_V\) are your literal-frame constants and \(\alpha_i'''=(1+2\beta)\alpha_i\) for \(i=0,1\).
Require \(C_VM(\alpha_0'''+\alpha_1''')\) to lie in the identity logarithm chart, and impose
\[
2C_VM(\alpha_0'''+\alpha_1''')<r/2,\qquad 2L[\alpha_2+2KC_VM(\alpha_0'''+\alpha_1''')]<a_{98}, \tag{2}
\]
\[
2LC_A[\alpha_2+2KC_VM(\alpha_0'''+\alpha_1''')]+2\alpha_3<\delta. \tag{3}
\]
Choose \(\alpha_1\), then \(\alpha_0\) subject to its bounds relative to \(\alpha_1\), then \(\alpha_3\), then \(\alpha_2\).
Keep \(4B_3\alpha_3\le\beta L^{-2}\alpha_0\), \(2B_3\alpha_3<\alpha_1/2\), and \(c\alpha_2\le\alpha_3\), as at CA-I 34745–34883.
All added inequalities are downward ceilings with positive right sides. Decreasing amplitudes in this order meets them without a cycle.
For running radii, impose them at every radius used. A fixed larger \(\tau\)-disc requires its radius in front of the first term of (3).

**Limits.** Real uniqueness concerns only Balaban's regular space. At complex data the object is its specified analytic continuation.
This does not assert uniqueness of all complex critical points, or minimality outside the regular space.
Locality means the nesting identity and dependence on the intrinsic layered datum. It does not mean finite-range response.
This note does not check the composite radii in CA-I §4.26 or the boxes and data at CA-II 35714.
It also does not cover boxes without memberwise domination by the background sequence, complex continuation on two-layer boxes of unbounded size, or the CA-III §9.1 nesting uses.
Those later applications require their own domain and radius arguments. This note does not close every nesting use in your account.

## Statement in your notation

Write \(M_{\mathcal T}\) for your layered datum \(M^{\boldsymbol\cdot}\) on \(\mathcal T\), and \(U_{\mathcal T}=U_n^{\mathfrak r}(Z;\cdot)\). Datum norms are suprema over the actual determining bonds.
In outer top-block units, let \(\xi_j=L^{-j}\) and
\[
W_j(D)=U_j(\square_0,e^{iD})=\mathcal U_j(D)^{u_j(D)},\qquad \mathcal U_j(D)=e^{i\xi_j H_j(D)}.
\]
The functions \(H_j,u_j\) are those of CMP 102b §G, Proposition 9 at base datum \(1\).
For every \(\|D\|_\infty<\delta\), the datum \(M_{\mathcal T}(\mathcal U_j(D)|_Z)\) belongs to the actual inner chart.
Every admitted real datum has exactly one regular axial minimizer. Its continuation is single-valued and holomorphic on this ball.
Let \(\bar u_{\mathcal T}\) equal \(u_j\) at each inner block root and be constant on that block; on the fixed fine shell it equals \(u_j\).
Then
\[
U_n^{\mathfrak r}\bigl(Z;M^{\boldsymbol\cdot}(\mathcal U_j)\bigr)
=(W_j|_Z)^{\bar u_{\mathcal T}^{-1}}=(\mathcal U_j|_Z)^{\bar u_{\mathcal T}^{-1}u_j}. \tag{4}
\]
In particular, (4) holds at every Lemma 4 datum \(D=\tau B+B'\), \(|\tau|\le1\), \(\|B'\|_\infty<2\alpha_3\), under (1)–(3).
We use your action \(U^h(b)=h(b_-)U(b)h(b_+)^{-1}\), hence \((U^a)^c=U^{ca}\) (CA-I 129758–129790).

## Proof

**Chart admission.** For any admissible tower \(\mathcal S\), put \(N_{0,\mathcal S}(F)=\sup_b\ell_{\mathcal S}(b)|F(b)|\), where \(\ell_{\mathcal S}\) is the local block side.
At the identity datum, the real tests (7) of CMP 102b hold with the positive parameter \(\varepsilon_*\).
Equation (172) and Proposition 9 therefore give the radius \(r\), uniformly in depth and domain.
Indeed \(\|B\|_\infty<r\) implies \(\|e^{iB}-1\|<C_1\varepsilon_*\), after the stated chart restriction.
The first bound of (19), together with (173), gives \(N_{0,\mathcal S}(H_{\mathcal S}(B))\le B_5\varepsilon_*\).
Also \(H_{\mathcal S}(0)=0\): the identity is the axial minimizer, and §G selects its zero Landau potential.
Restrict to the complex line \(zB/\|B\|_\infty\). Apply Schwarz's inequality to every norm-one functional of each weighted bond value.
Taking the supremum gives the dimension-independent bound
\[
N_{0,\mathcal S}(H_{\mathcal S}(B))\le K\|B\|_\infty\qquad(\|B\|_\infty<r). \tag{5}
\]
For a complex potential \(F\), consider an output bond of side \(s\), fine spacing \(h\), and two-block carrier \(E\). CMP 98 Propositions 4 and 6 give
\[
s\sup_E|F|<a_{98}\ \Longrightarrow\
\left|\tfrac1i\log M^q(e^{ihF})(c)\right|\le C_As\sup_E|F|,\qquad |Q_q(hF)(c)|\le C_As\sup_E|F|. \tag{6}
\]
Both maps are defined and holomorphic on this domain. These are two bounds, not an identification of the maps. Rescale the fine spacing to \(h/s=L^{-q}\) and the potential to \(sF\).
At reference \(1\), (52) is automatic. Equations (159)–(164) give the plain average; (131), (134)–(135) give the auxiliary bound.
In particular, (134)–(135) express \(Q\) as its bounded linear part plus a quadratic remainder. Shrinking \(a_{98}\) absorbs that remainder.
Shrink it also until the group error is below \(1/2\); then \(|\log(1+E')|\le2|E'|\) gives the logarithm bound.
Two-block locality is your `4.6:lem-averaging-locality` (CA-I 24239–24405). Extend values by zero outside the carrier if needed. No derivative bound enters (6).
Every inner averaging carrier and axial-tree carrier lies in the outer top region.
Indeed \(Z\subset\tilde\square^2\), whereas \(\square_j\supset\tilde\square^4\). In window units, layers have side \(M\) and the largest blocks have side at most \(L\).
Even a two-block carrier has length at most \(2dL<2M\). The inclusion persists for domains with holes; the inner gap gives its own fixed fine collar.
In outer top-block units, (5) gives \(|H_j(D)|\le K\|D\|_\infty\), and an inner level-\(q\) block has side \(L^{q-j}\le1\).
Thus (6), and the direct fine-row bound at level zero, give
\[
\left\|\tfrac1i\log M_{\mathcal T}(\mathcal U_j(D)|_Z)\right\|_\infty\le C_AK\|D\|_\infty<r/2. \tag{7}
\]
By (1), the whole \(\delta\)-ball therefore maps into every inner base-one chart, with margin.
This proves membership in your existence set (CA-I 38650–38673), rather than relying on that set being open.

We next admit the actual Lemma 4 datum on **all** window determining rows, including the collar and outward rows.
Your literal-frame clauses give, throughout the input twist polydisc,
\[
\|V-1\|_\infty\le C_VM(\alpha_0'''+\alpha_1'''),\qquad B_V=\tfrac1i\log V,\qquad \|B_V\|_\infty\le2C_VM(\alpha_0'''+\alpha_1'''). \tag{8}
\]
By (2), (5) applies to the incoming depth-\((k+1)\) chart at \(B_V\), in every layer and its collar.
For \(q\ge1\), a truncated outgoing level-\(q\) row and its two-block carrier lie in \(\square_{q-1}\).
The adjacent block across an outward face is at most one level-\(q\) block side from \(\square_q\).
The separation exceeds that side because \(R_1\ge L\) and \(\mathfrak M\ge1\). Passing to this carrier loses at most a factor \(L\).
In the \(\eta\)-units of CMP 109 (3.30), with \(s_q=L^q\eta\), define
\[
F=\frac1{i\eta}\log\bigl(e^{i\eta A}e^{iL^{-1}\eta H_{k+1}(B_V)}\bigr),\quad
s_q\sup_E|L^{-1}H_{k+1}(B_V)|\le LK\|B_V\|_\infty,\quad s_q\sup_E|A|\le L\alpha_2. \tag{9}
\]
Here \(|A|<\alpha_2\) throughout the window and \(q\le j\le k+1\). The incoming top side is \(L\) in these units.
At \(q=0\), the same bound follows from the fine-row bound. A factor \(|\tau|\le1\) in the incoming chart argument preserves (9).
For \(t=|X|+|Y|\le\log(4/3)\), submultiplicativity gives \(|e^{iX}e^{iY}-1|\le e^t-1\).
The log series then gives \(|\log(e^{iX}e^{iY})|\le-\log(2-e^t)\le2t\), since \(e^t/(2-e^t)\le2\).
Apply this with \(X=\eta A\), \(Y=L^{-1}\eta H_{k+1}\). Equations (2), (8)–(9) and \(\eta\le s_q\) ensure its smallness condition.
Hence \(s_q\sup_E|F|\le2L(\alpha_2+K\|B_V\|_\infty)<a_{98}\).
Apply the auxiliary \(Q\) bound in (6) to (3.30), keeping its unchanged rows. It gives \(\|B\|_\infty\le2LC_A(\alpha_2+K\|B_V\|_\infty)\).
Therefore (8) and (3) give \(\|\tau B+B'\|_\infty\le2LC_A[\alpha_2+2KC_VM(\alpha_0'''+\alpha_1''')]+2\alpha_3<\delta\).
This includes the near case \(A=0\). It uses neither the output assertion of Lemma 4 nor the near-case membership conclusion.

**Real criticality and the action domain.** Let \(D\) be real with \(\|D\|_\infty<\delta\).
Each ordinary factor of a data plaquette differs from one by at most \(\|D\|_\infty\).
At a seam, the prescribed one-level finer average has logarithm at most \(C_AL\|D\|_\infty\), by (6).
Separation prevents an arbitrarily large level jump. All factors are unitary, so telescoping four factors gives test parameter \(C_D\|D\|_\infty\).
Theorem 1 yields \(W_j(D)\in\mathfrak U_j(\boldsymbol\square,\epsilon_W)\). Equation (1) pays for both applications of that theorem below.
On the same outer action domain, form \(\widehat\Omega_0=\square_0\), \(\widehat\Omega_q=\Omega_q^{\mathfrak r}(Z)\) for \(1\le q\le n\), and empty members for \(n<q\le j\).
The first separation follows from the inner separation and \(Z\subset\square_0\); later separations are the inner ones.
This tower is memberwise smaller than \(\boldsymbol\square\), since \(Z\subset\square_j\). Your proof at CA-I 32975–32985 admits rule 2 at the common threshold \(R_1\).
Discarding empty terminal layers changes neither the constraints nor the action. If \(\Omega_1(Z)\) is empty, all inner bonds are prescribed and restriction is immediate.
Otherwise, your `9.3:lem-refinement` makes \(W_j(D)\) critical and minimal for the refined data, by inclusion of the actual constraint fibres.
Let \(V(t)\) be any differentiable inner constraint-preserving curve through \(W_j(D)|_Z\). Extend it by the fixed outer field to \(\widehat V(t)\).
The level-zero shell fixes all changing bonds except those touching \(\Omega_1(Z)\). The first inner gap puts every plaquette containing such a bond inside \(Z\).
Thus \(\left.\frac d{dt}A_{\square_0}(\widehat V(t))\right|_0=\left.\frac d{dt}A_Z(V(t))\right|_0\); every other plaquette term is fixed.
The extended curve preserves all refined constraints: positive-level rows are inner rows, and extra level-zero rows are fixed.
For small \(t\), it remains in the regular open class, since the base field is strictly inside. The outer derivative vanishes, hence so does the inner derivative.
Inner local scales only decrease, so the curvature and current bounds put the restriction in the inner regular uniqueness space.
CMP 98 Proposition 2, with the seam convention, bounds the inner data test by \(C_7\epsilon_W\).
Equation (1) gives \(C_7\epsilon_W<a_1/2\) and \(B_3C_7\epsilon_W<a_0/2\). The second Theorem 1 application therefore identifies the restricted critical orbit with the minimal orbit.
Both applications use the uniqueness ceiling \(\varepsilon_0=a_0/2\); neither occurrence of \(B_3\) is omitted.

**The axial representative.** The inner hierarchy uses a subset of the globally aligned outer trees and their iterated averages.
Its blocks have levels at most \(n\le j\) and lie in the outer top region. Your `4.26:def-block-axial` gives this inheritance (CA-I 130021–130052).
Thus \(W_j(D)|_Z\) is already inner axial. A residual gauge between two such representatives is one at every determining root.
The tree equations propagate that value along every edge, successively through all levels and the fixed shell. Therefore
\[
U_{\mathcal T}\bigl(M_{\mathcal T}(W_j(D)|_Z)\bigr)=W_j(D)|_Z. \tag{10}
\]
Every attained real minimizer in the regular open variational space is critical along each admissible two-sided curve.
CMP 102b Theorem 1 supplies existence in its (8) and uniqueness of the critical orbit in its (6). The ceilings put the problem inside that uniqueness space.
Consequently all such minimizers lie on this orbit, and axial normalization selects exactly one.

**Continuation.** For real \(D\), covariance of the actual averages and CMP 102b (181), followed by (10), gives
\[
U_{\mathcal T}\bigl(M_{\mathcal T}(\mathcal U_j|_Z)\bigr)
=\bigl[U_{\mathcal T}(M_{\mathcal T}(W_j|_Z))\bigr]^{\bar u_{\mathcal T}^{-1}}
=(W_j|_Z)^{\bar u_{\mathcal T}^{-1}}=(\mathcal U_j|_Z)^{\bar u_{\mathcal T}^{-1}u_j}.
\]
Both sides are holomorphic on the whole \(\delta\)-ball. For the left side, (7) proves admission into the actual inner chart.
For the right side, §G gives the holomorphic outer field and gauge; root evaluation and inversion preserve holomorphy.
They agree on an open real slice of full dimension. Apply the one-variable identity theorem successively in a real basis of the finite datum space.
Then continue through the connected ball. This proves (4) on the full complex domain.
The acting element is \(g=\bar u_{\mathcal T}^{-1}u_j\), as fixed by your action and the equality above; see your convention discussion at CA-I 130178–130191.
Let \(\mathcal J_j=R(u_j^{-1})J_j\). Covariance gives \(\partial U_{\mathcal T}=R(g)\partial\mathcal U_j\) and \(J_{n,\mathcal T}=(L^n\xi_j)^3R(g)\mathcal J_j\) on the corresponding source domains.
The current factor converts to inner top-block units. Your scalar bounds at CA-I 33691–33735 and 31106–31131 use the same norm bounds on \(u_j^{\pm1}\) and \(\bar u_{\mathcal T}^{\pm1}\).
Those scalar estimates are reused. No derivative-decay estimate or other background theorem follows from this argument. \(\square\)

## Who wrote and checked this

Codex wrote the working note. A fresh Claude session checked it line by line; first failing step: none.
Codex wrote this outward version. Its separate reading against the working note by Claude is pending.
These are model readings of research text, not human review or an audit. They grant no scientific status.

[Full working note](mu.md)
