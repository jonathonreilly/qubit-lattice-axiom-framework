# Re-blocking in the Sussman–Alpoge complete account

Provenance: Codex, 2026-11-05, checkout `03e30ac41147c9916126d2ff9af23ef4f82bff9d`. Research text, not an audit; grants no status. Hand proofs only. New arguments have not been checked by another model.

Credit: Ethan Sussman and Levent Alpoge, with Claude and Codex as authors of their text, for the outline and complete account at `31a47c543775`; Tadeusz Balaban for the underlying block averages, constrained minimisers, and renormalisation construction. Source line numbers below refer to the pinned CA-I or outline.

Target: `4.12:prop-reblocking-inside`, its real-factor corollary, then `4.12:prop-reblocking-outside`. This note continues their route and does not change any scientific status.

## 1. Source comparison and exact scope

The local index was consulted first. Relevant entries are CA-index chunks 01–02, especially CA-I 42950–43206 and 44127–45159. The outline index has no entry named re-blocking. Its nearest entries are Theorem 5(b) and Theorem 6(c), SA 9755 and 9783–9789. They concern settled subordinate towers and joined, collared sequences. They do not identify an arbitrary consumer refinement with an old determining set.

The inside proposition declares its proof incomplete at a marked step. In CA-I 42724–45161, every occurrence of `$(\ast)$` is a reference to that reservation. None labels an equation or an individual inferential step. Thus this note does not invent an identity for the missing marker. The actual proof is CA-I 44220–44801. The corollary explicitly assumes the proposition at 44804–44812. The outside proposition remains outstanding at 45085–45106.

All occurrences of the three target labels were searched in CA-I, II and III. The explicit references are confined to CA-I 44129–45140. They comprise the proof's two cases, its assembly, the real-factor interpretation, the corollary, the refined-minimiser remark, the scope discussion, and the outside proposition. These passages were read. In particular, the outside proposition requests **(a) and (b)**, not (c). The real-factor corollary requests (c). No complex-domain conclusion follows from either real argument.

A second search by the statements' names found the unlabelled consumer at CA-I 10047–10058. It takes the real-factor condition along the large-field chain as supplied, including re-blocking, and uses it as a hypothesis at straddling domains. The status lists at CA-I 166615–166624 and CA-III 111207–111210, 111366–111373 retain these open declarations. Those passages were also read. The local inside implication below does not discharge that consumer on every straddling domain.

Comparison with our closest texts:

| Text read | What it supplies | Difference from this task |
|---|---|---|
| `geoh.md`, Lemma 8 and Theorem 2, lines 178–205 | Quiet padding and the carrier of a specified main-step source | It leaves background/source matching explicit. It gives neither the consumer minimiser nor a compatible relative gauge. |
| `dom.md`, Lemmas 10–12, lines 249–290; Lemma 16, lines 330–341 | Decay along an admitted path of one fixed determining system; a flat extension construction | A refined determining system changes the constraints. The required extension/path remains open for curved data. |
| `st1-r4.md`, Lemma 5, lines 347–368; Lemma 8, lines 539–625 | A regular critical orbit and ambient estimates for settled subordinate towers | These have their own separation, admission and settlement hypotheses. They do not prove those hypotheses for every CA consumer refinement. |
| `pr-lay.md`, Lemmas 5–7 and Theorem 8, lines 258–328 | Geometry transfer, real cube gauges and conditional admission | These require their geometry, regularity and domain inputs. A separate cube gauge is not a single gauge on all refined bonds. |

The literature search reuses `lit-balaban.md`. The targeted readings are Balaban CMP 98, pp. 42–43, Propositions 6–7; CMP 102, pp. 278–279, Theorem 1, and p. 309, Proposition 9. They provide averaging/response estimates after admission. They do not, by the quoted statements alone, identify the changed constraints. The local copies are in `~/ym4d-papers`. No new route replaces these inputs.

Here and below an **input** means the exact hypothesis or cited theorem in CA-I §4.12. It is not a claim to have rebuilt all of Balaban. The determining-set and interface-averaging hypotheses are explicit at 43055–43084. The block-scale minimiser and response are explicit inputs at 43113–43205. Current hypotheses J1–J2 are explicit at 42786–42808. The new work below concerns the implication from these inputs.

## 2. Inside boxes: repairs and port

Write \(\alpha_m=\tilde\alpha_{0,m}\), \(\eta=L^{-k}\), and \(\ell_m=L^{m-k}\). Keep the account's order: choose \(L_0,L\), the response constants and \(M_1\), then \(M\), then small couplings. No constant below is chosen from a run.

There are two small qualifications to the printed proof.

First, for an arbitrary compact matrix group, the principal logarithm belongs to its Lie algebra only inside the radius \(\epsilon_G\) at CA-I 42746–42747. The axial lemma at 43787–43865 incorrectly infers this membership from distance at most one. Its norm estimate is valid. Its Lie-algebra conclusion needs
\[
 (d-1)D_{\mathfrak Q}\alpha_k\eta\le\epsilon_G.             \tag{1}
\]
For the T0 group \(SU(2)\), one may take \(\epsilon_G=1\): the two eigenvalues are \(e^{it},e^{-it}\), with \(|t|\le\pi/3\), so the principal logarithm has trace zero. For a fixed general group, (1) is another final coupling ceiling; any dependence on \(G\) must be retained.

Second, J2 requires estimates at every bond within two lattice steps (42801–42804). The direct-response estimate (43190–43195) supplies values near one element and a derivative at its base point. The application at 44698–44709 does not itself check that whole stencil. The following finite enlargement does.

**Lemma 1 (completion of the current stencil).** Let \(B_H^0\) be a constant for CA's response bound. There is an enlarged constant \(B_H\), fixed at the same early stage, such that for every interior bond \(\xi\) based at \(x\),
\[
 \ell_{\mathfrak B}(\xi)^r |T_r\mathcal H(y)|
 \le B_H\|b\|(x),\qquad r=1,2,3,                         \tag{2}
\]
on the entire J2 stencil. Here \(T_1\mathcal H=\mathcal H\), \(T_2\mathcal H=\nabla\mathcal H\), and \(T_3\mathcal H=D^*D\mathcal H\), with the appropriate site or bond arguments. All required elements must belong to the domain.

*Proof.* Use the response estimate at the base of each required element. A path of at most eight fine bonds joins any site in its one-step enlargement to a site in \(\xi^+\). Along each crossing, the determining-set hypothesis changes block level by at most one. Consequently its local side is at least \(L^{-8}\ell_{\mathfrak B}(\xi)\). The same path has scaled length at most \(8/M_1\), since every block side is at least \(\eta\). The triangle inequality for scaled distance gives
\[
 \|b\|(y)\le e^{8\delta/M_1}\|b\|(x).
\]
Apply CA's response estimate at \(y\), then multiply by the ratio of local sides to power \(r\le3\). Thus
\[
 B_H=L^{24}e^{8\delta/M_1}B_H^0                         \tag{3}
\]
suffices. The finite stencil lies inside \(X''\): its vertices start in the two-layer interior; \(n\ge1\), \(L\ge15\), and \(M\ge M_1\ge1\) give clearance at least \(2ML\eta\). The determining-set convention for nearest neighbours is the one used at CA-I 44286–44303. This proves (2). □

Enlarging an existential response constant preserves its original estimate. Use this enlarged \(B_H\) everywhere, including \(\Gamma_0\) and \(\Gamma_2\). This does not silently obtain the same numerical bound for a previously fixed, smaller constant.

**Proposition 2 (inside implication in the account's intended geometry).** Assume the exact §4.12 inputs, \(\Gamma_0\)–\(\Gamma_3\), and the consumer geometry and gains of Definition `4.12:def-consumer-radii`, including its level-\(k\) provision. For \(SU(2)\), clauses (a)–(c) of `4.12:prop-reblocking-inside` and `4.12:cor-real-factor-slots` follow, with the early choice (3). For another fixed compact group impose (1) as well. The proof uses the account's route.

*Proof.* Set \(\mathfrak B=\mathfrak B_E(p,X'')\) and \(V=M_{\mathfrak B}\bar U\). The source bound and averaging input give
\[
 |\partial V(P)-1|\le2\alpha_k\ell(P)^2\le2\alpha_k\ell_p^2.
\]
Thus the minimiser input applies with \(\varepsilon_1=2\alpha_k\ell_p^2\). Its smallness conditions are \(\Gamma_0(ii)\). This proves (a). For an element \(\xi\subset X''^{\sim2}\), put \(n=n_E(\xi)\). The two-layer clearance, \(M\ge M_1\), and the determining-set level rule give, as in CA-I 44271–44303,
\[
 \ell_{\mathfrak B}(\xi)\ge L^{-1}\ell_{\min(p,n)}.       \tag{4}
\]

If \(n\ge p\), the minimiser bounds and (4) give exactly
\[
 |\partial U_E-1|\le2L^2B_3\alpha_k\eta^2,
 \qquad |J(U_E)|\le2L^3B_3\alpha_k\ell_p^{-1}.           \tag{5}
\]

For \(n<p\), put \(a_*=(\pi/3)(d-1)D_{\mathfrak Q}\alpha_k\). The lexicographic box gauge in CA-I 43787–43865 writes \(\bar U^a=e^{i\eta\mathfrak a}\) with \(\|\mathfrak a\|_\infty\le a_*\). To recall its hand argument: commuting the last step of a coordinate path through the later coordinate segments uses at most \((d-1)D_{\mathfrak Q}/\eta\) elementary plaquettes. Unitarity and telescoping bound the link's distance from one by their number times \(\alpha_k\eta^2\). The principal-log estimate supplies the stated \(a_*\). Condition (1) supplies Lie-algebra membership when needed.

The real averaging input, including its interface clause, gives one datum \(b\) and one base-point gauge with
\[
 V=(e^{ib})^{\varsigma},\qquad
 |b(\mathbf b)|\le c_Q a_*\ell(\mathbf b).               \tag{6}
\]
In the thresholds, read \(c_2\) as the averaging smallness constant \(c_{\rm av}\); the definition of the averaging map uses the latter name. This is a notational identification, not a further estimate.

Since \(\ell(\mathbf b)\le1\), \(\sup|b|\le c_Qa_*<b_H\). Equation (6) and gauge covariance give \(|\partial e^{ib}(P)-1|=|\partial V(P)-1|\). Thus the already verified datum bound with \(\varepsilon_1=2\alpha_k\ell_p^2\) verifies the other response hypothesis. This avoids any assumption about the number of edges in an interface plaquette. Gauge covariance and regular uniqueness identify
\[
 U_E=(e^{i\eta\mathcal H_{\mathfrak B}(b)})^\sigma.       \tag{7}
\]
Both readouts have gauge-invariant norms.

Here is the weighted estimate, retaining its scale gain. At a site with \(c_E(x)=n'<p\), bonds of size at most \(\ell_{n'+1}\) contribute at most \(c_Qa_*c_dL\ell_{n'}\). For a bond of size \(\ell_m\), \(m\ge n'+2\), both endpoint blocks have level at least \(m-1\). The separation input gives
\[
 d(x,\mathbf b)\ge(m-n'-2)_+M/M_1.
\]
Keep half the decay for the bond sum. With \(q=Le^{-\delta M/(2M_1)}\le1/2\), the remaining contribution is bounded by
\[
 c_Qa_*c_d\ell_{n'}L^2\sum_{r\ge0}q^r
 \le2c_Qa_*c_d\ell_{n'}L^2.
\]
If \(c_E(x)\ge p\), every bond has size at most \(\ell_p\), and summability gives \(c_Qa_*c_d\ell_p\). Thus, in both cases,
\[
 \|b\|(x)\le K_b\alpha_k\ell_{\min(p,c_E(x))},\quad
 K_b=\frac\pi3(d-1)c_Qc_d(1+3L^2)D_{\mathfrak Q}.         \tag{8}
\]
This is the account's estimate, with \(L+2L^2\le1+3L^2\).

At \(\xi\) with \(n<p\), (2), (4), and (8) give
\[
 |\mathcal H|\le LB_HK_b\alpha_k,\quad
 |\nabla\mathcal H|\le L^2B_HK_b\alpha_k/\ell_n,\quad
 |D^*D\mathcal H|\le L^3B_HK_b\alpha_k/\ell_n^2,          \tag{9}
\]
on the needed stencils. The left-perturbation plaquette estimate, CA-I 43867–43995, at the identity gives
\[
 |\partial e^{i\eta\mathcal H}-1|
 \le 2\eta^2L^2B_HK_b\alpha_k/\ell_n
       +12\eta^2L^2(B_HK_b\alpha_k)^2
 \le3L^2B_HK_b\alpha_k\eta^2/\ell_n.                     \tag{10}
\]
The last inequality uses \(12B_HK_b\alpha_k\ell_n\le1\), which follows from \(\Gamma_0(v)\). For J2 choose \(\ell=\ell_n/L\) and \(w=B_H\|b\|(x)\). Then \(\ell\ge\eta\), \(w\le1/64\), and (2) checks its entire stencil. Therefore
\[
 |J(e^{i\eta\mathcal H})|
 \le(2+2C_Jw)w(L/\ell_n)^3
 \le3L^3B_HK_b\alpha_k\ell_n^{-2}.                       \tag{11}
\]
Here \(2C_Jw\le1\) is the other part of \(\Gamma_0(v)\). Equations (5), (10), and (11) are (b).

For completeness, divide by the actual radii. When \(n\ge p\), both ratios are at most
\[
 2L^3B_3(1+\beta_0)
 \frac{\sqrt{1+k-n}\,L^{-2(k-n)}}{\vartheta_E(\xi)}.
\]
When \(n<p\), they are at most
\[
 3L^3B_HK_b(1+\beta_0)
 \frac{\sqrt{1+k-n}\,L^{-(k-n)}}{\vartheta_E(\xi)}.       \tag{12}
\]
For \(n\le k_0\), the numerator with one power of \(L^{-1}\) is decreasing and bounded by \(\sqrt{1+N_0}L^{-N_0}\). For \(k_0<n<k\), put \(m=k-n\). Since \(L\ge3L_0^2\), division by \(L_0^{2(n-k_0)}\) gives at most \(\sqrt{1+m}3^{-m}L_0^{-2N_0}\le L_0^{-2N_0}\). The two-power numerator is smaller. Thus \(\Gamma_1\) and \(\Gamma_2\) make both ratios at most \(1/2\). At \(n=k\), use the level-\(k\) provision and \(\Gamma_3\). This proves (c).

The corollary now follows without a new estimate. Off the core, each composite has real factor \(\bar U\). Its derived real slots are precisely the two readouts just bounded, at every prescribed pair \((p,X'')\). □

**Scope retained.** Definition `4.12:def-consumer-radii(i)` states its level-\(k\) assertion for boxes in \(Z''_k\cup B_5\) (43437–43440). The general definition of admissible box at 43265–43274 is wider. The above (c) proof needs the former provision; it does not infer it for arbitrary boxes in the wider class. Clauses (a) and (b) do not need it. Likewise a large \(N_0\) alone proves \(\Gamma_1\)–\(\Gamma_3\) from the displayed hypotheses. The radius ceilings in \(\Gamma_0\) require small couplings, as the separate assertion at 43618–43627 says. These qualifications are not counterexamples to the propositions.

## 3. Outside boxes: three new attacks

The exact target is CA-I 45085–45106. The account proposes a relative-datum estimate (45114–45133), or comparison with a box-restricted tower (45135–45159). Both are real statements. The arguments below use those routes and retain their failure points.

### Attack 1: local axial gauges, then smooth gluing

**Lemma 3 (two configurations in one common box).** Let \(G=SU(2)\). Let \(U_1,U_2\) be defined on a box \(Q\) of side at most \(D\), with
\[
 |\partial U_r-1|\le F_r\eta^2\quad(r=1,2).
\]
Let \(\mathfrak B\) be a determining set in \(Q\), including every averaging carrier used below. Put \(a_r^*=(\pi/3)(d-1)DF_r\). Assume \((d-1)DF_r\eta\le1\), \(a_r^*\le c_{\rm av}\), and \(c_Q\ell(\mathbf b)(a_1^*+a_2^*)\le1\) on every block bond. These are explicit sufficient smallness conditions. Put \(D_r=M_{\mathfrak B}(U_r)\). There are one gauge \(\sigma\) and one Lie-algebra datum \(B\), defined on this entire block lattice, such that
\[
 D_1=(e^{iB}D_2)^\sigma,\qquad
 |B(\mathbf b)|\le\frac{\pi^2}{9}(d-1)c_QD\ell(\mathbf b)(F_1+F_2).       \tag{13}
\]
This is a small-curvature statement. No equality of coarse averages is needed on this one box.

*Proof.* The box argument gives gauges \(a_r\) with \(U_r^{a_r}=e^{i\eta A_r}\) and \(|A_r|\le(\pi/3)(d-1)DF_r\). Apply the interface averaging hypothesis separately to each whole configuration. Thus
\[
 D_r=(e^{ib_r})^{\rho_r},\qquad
 |b_r(\mathbf b)|\le(\pi/3)(d-1)c_QD\ell(\mathbf b)F_r.
\]
For the positively oriented bond \(\langle z,z'\rangle\), define
\[
 A(\mathbf b)=i^{-1}\log(e^{ib_1(\mathbf b)}e^{-ib_2(\mathbf b)}),\quad
 B(\mathbf b)=\operatorname{Ad}_{\rho_2(z)}A(\mathbf b),\quad
 \sigma=\rho_1\rho_2^{-1}.
\]
Multiplication at the two endpoints gives the identity in (13) exactly. The inverse bond is defined by the same configuration identity. For Hermitian \(b\), the integral formula for \(e^{ib}-I\) gives \(|e^{ib}-I|\le|b|\). Therefore
\[
 |e^{ib_1}e^{-ib_2}-I|\le|b_1|+|b_2|,
\]
and the \(SU(2)\) principal-log bound gives (13). □

Taking \(D=3\ell_p\) gives the requested first-order power \(\ell_j\ell_p\) on uniform level-\(j\) bonds, including crossing bonds whose complete carriers lie in that box. This is a version of the proposed local datum lemma. It adds a common containing box and smallness. Its constant uses the account's \(c_Q(d,L)\); it does not prove the proposed constant depending on \(d\) alone. Crucially, it supplies a gauge on one box, not compatible gauges on an unbounded collection of boxes.

For the underlying fine fields on one such box, set \(g=a_1^{-1}a_2\). Left multiplication by \(a_1(x)\) and right multiplication by \(a_2(y)^{-1}\) turn \(U_1(x,y)g(y)-g(x)U_2(x,y)\) into \(e^{i\eta A_1(x,y)}-e^{i\eta A_2(x,y)}\). Its norm is at most \(\eta(|A_1|+|A_2|)\), by telescoping through the identity. Thus these gauges have the local fine-bond bound (14) when \(D\) is a fixed multiple of \(s\).

I then tried to glue these gauges. The following precise gluing fact succeeds.

**Lemma 4 (gluing already aligned relative gauges).** Fix \(s>0\), \(F\ge0\), and nonnegative constants \(C_0,C_1,C_\lambda\). Let \(Q_a\) cover a lattice domain and the required one-bond neighbourhoods. Let \(\lambda_a\ge0\), \(\sum_a\lambda_a=1\), be a locally finite partition, subordinate with that neighbourhood room. Suppose, for every bond \(\langle x,y\rangle\),
\[
 \sum_a|\lambda_a(y)-\lambda_a(x)|\le C_\lambda\eta/s.
\]
Let \(g_a:Q_a\to SU(2)\) satisfy, on every bond where its weight at either endpoint is nonzero,
\[
 |U_1(x,y)g_a(y)-g_a(x)U_2(x,y)|\le C_0\eta sF.          \tag{14}
\]
Suppose also that all gauges active at either endpoint satisfy, at \(x\),
\[
 |g_a(x)-g_b(x)|\le C_1s^2F\le\tfrac12.                 \tag{15}
\]
Then there is one global \(g\) with
\[
 |U_1(x,y)g(y)-g(x)U_2(x,y)|
 \le4(C_0+C_\lambda C_1)\eta sF.                         \tag{16}
\]

*Proof.* Regard \(SU(2)\) as the unit quaternions in its usual two-dimensional matrix representation. A real linear combination of such matrices remains a quaternion. Define \(h(x)=\sum_a\lambda_a(x)g_a(x)\). By (15), it is within \(1/2\) of any active \(g_a(x)\), so its quaternion norm is at least \(1/2\). Put \(g=h/|h|\). It belongs to \(SU(2)\).

For a fixed bond, subtract any one active value \(g_{a_0}(x)\) from the weight-difference sum. This is permitted because the weight differences sum to zero. Then
\[
\begin{split}
 U_1h(y)-h(x)U_2
 &=\sum_a\lambda_a(y)[U_1g_a(y)-g_a(x)U_2]\\
 &\quad+\sum_a[\lambda_a(y)-\lambda_a(x)]
          [g_a(x)-g_{a_0}(x)]U_2.
\end{split}
\]
Equations (14)–(15) bound this by \((C_0+C_\lambda C_1)\eta sF\). Normalization is equivariant under left and right unit quaternions. For nonzero quaternions \(v,w\),
\[
 \left|\frac v{|v|}-\frac w{|w|}\right|
 \le\frac{2|v-w|}{\min(|v|,|w|)}.
\]
Apply this with \(v=U_1h(y)\), \(w=h(x)U_2\). Both norms are at least \(1/2\), proving (16). □

**Exact failure of Attack 1.** The coarse-average equality must produce (15), in one choice of local frames, on every overlap. The box estimates prove (14), but do not fix the independent constant rotations of those frames. They also do not control those rotations on the artificial boundary towers. Choosing a constant separately on each overlap does not give one choice per box: the choices must agree around cycles. I did not derive this consistency and its \(s^2F\) bound from the actual nonlinear averaging constraint. Lemma 4 therefore cannot yet be applied. This is a missing proof, not a topological counterexample. The proof has not assumed a global small gauge.

### Attack 2: the constrained variational problem

I tried to obtain the missing gain directly from the constraint, without choosing overlap gauges first. The linear problem exposes exactly what this would require.

**Lemma 5 (exact refinement identity at quadratic order).** On a finite real gauge slice let \(K\) be positive definite. Let \(Q_f\) have full row rank and let \(Q_c=RQ_f\) have full row rank. For a field \(a\), let \(u_c\) minimize \(\frac12\langle u,Ku\rangle\) subject to \(Q_cu=Q_ca\). Put
\[
 B=Q_f(a-u_c),\qquad
 H_f=K^{-1}Q_f^*(Q_fK^{-1}Q_f^*)^{-1}.
\]
Then \(RB=0\), and the minimizer with constraint \(Q_fu=Q_fa\) is
\[
                         u_f=u_c+H_fB.                  \tag{17}
\]

*Proof.* Positivity and full row rank make the displayed inverse positive definite. Direct multiplication gives \(Q_fH_f=I\). Hence the right side has the required fine data. For \(v\in\ker Q_f\), also \(v\in\ker Q_c\), so \(\langle Ku_c,v\rangle=0\). Moreover \(KH_fB\in\operatorname{ran}Q_f^*\), so its inner product with \(v\) vanishes. Thus the right side is critical on the fine affine constraint. Positivity makes it the unique minimizer. Finally \(RB=Q_c(a-u_c)=0\). □

This is the finite variational content of the account's refined-minimiser identity, CA-I 44940–44982. In the nonlinear problem, the source grants composition of the averages at 44874–44875. That grant must remain visible; equality of two separately prescribed averages does not prove it.

**Exact failure of Attack 2.** The identity supplies no first-order bound on \(B\). Already for \(R=(1/2,1/2)\), its kernel contains \((t,-t)\) for every \(t\). Thus the mean-zero condition alone gives no factor \(\ell_j/\ell_p\). This two-coordinate example is not a gauge-theory counterexample: curvature and the quotient by gauge may supply that factor. To exploit them one needs a uniform sup-norm right inverse for the constrained covariant curl, on the actual towers, followed by a nonlinear continuation preserving the fixed coarse data. A finite-dimensional inverse or an energy-norm bound does not give a uniform sup-norm estimate as \(\eta\to0\). The quoted Balaban response estimate applies after the relative datum is small; using it to assert that smallness would be circular. I obtained (17), but not that right-inverse estimate.

### Attack 3: localize the tower and pay its boundary error

I next tried the account's second route, including its proposed error term, rather than replacing its constraints by those in ST1. There are two distinct checks in this attack.

First, the identity needed at an artificial boundary is not automatic. If coarse averaging \(Q_c\) factors as \(RQ_f\), fixing fine data implies the coarse constraint. This follows by multiplication, as in Lemma 5. Cutting a coarse block and introducing a new boundary tower replaces those rows. No matrix \(R\) for the new rows follows from the old one. In the nonlinear setting the needed assertion is the same: a local constraint map must compose to the retained coarse map, on its complete carriers. Restriction of the field by itself proves only agreement on rows whose complete carriers survive. This is exactly the compatibility reserved at CA-I 45153–45159. DOM's same-system path lemma does not address it.

Second, even granting the displayed comparison at CA-I 45143–45154 does not yield the printed below-slot bound by unchanged bookkeeping. Write \(q=\ell_n\), \(n<p\). Up to the fixed powers of \(L\) from (4), its allowed curvature error is
\[
 C_{\rm loc}B_3\alpha_k e^{-\delta\Delta/M_1}\eta^2q^{-2}.
\]
The desired bound in (b) is of order \(B_HK_b\alpha_k\eta^2q^{-1}\). Their ratio has the factor
\[
                       e^{-\delta\Delta/M_1}/q.          \tag{18}
\]
The current comparison has exactly the same factor: its error has \(q^{-3}\), while the target in (b) has \(q^{-2}\). To make (18) uniformly bounded would require
\[
 \delta\Delta/M_1\ge (k-n)\log L-O(1).                  \tag{19}
\]
For a point inside the local box, where the restricted minimiser can be read, the available \(\Delta\) is bounded by a constant times \(M\): an admissible box has side at most \(204M\). This is independent of \(k-n\). The proposition has no upper bound on \(k-n\). Fixing \(M\) before taking the ultraviolet depth therefore cannot enforce (19) by this estimate alone. A final small-coupling ceiling does not cancel (18), since \(\alpha_k\) occurs on both sides.

**Exact failure of Attack 3.** I could establish neither the changed-row compatibility nor the extra scale factor needed in the boundary error. Even if the first were granted, the stated localization inequality by itself loses one power of \(\ell_n\). A refined boundary-datum estimate could recover it, but that is additional proof work. This calculation refutes only the proposed deduction from that error estimate alone. It is not a counterexample to localization or to the outside proposition.

## 4. Constant order and the exact remaining statement

The inside port fixes \(B_H\) by (3) before \(M\). It then uses the account's
\[
 M\ge\max\{M_1,2M_1/\delta,2M_1\delta^{-1}\log(2L)\}.
\]
After this choice, \(K_b\) is fixed. Choose a finite \(N_*\) so that the decreasing function \(W(N)\) meets \(\Gamma_1\) and \(\Gamma_2\), and the increasing \(L_0^{2N}\) meets \(\Gamma_3\). Finally choose the coupling ceiling to ensure \(\Gamma_0\), \(N_0\ge N_*\), and (1) when needed. The limit \(g(\log g^{-2})^{q_0}\to0\) follows by setting \(u=\log g^{-1}\) and bounding \(e^u\) below by \(u^r/r!\) for an integer \(r>q_0\). Thus this is a hand existence argument for the ceiling, in the prescribed order.

The three attacks leave the following **single uniform tower estimate**. It is deliberately stated at the actual consumer, rather than on a surrogate fixed system.

**Lemma RB (outside consumer, actual boundary tower; open).** In the setting and under all hypotheses of CA-I `4.12:prop-reblocking-outside`, with the §4.12 input theorems fixed first, set
\[
 \mathfrak B=\mathfrak B_E(p,X''),\qquad D=M_{\mathfrak B}\bar U.
\]
For every such pair, \(D\) admits the regular constrained minimiser supplied by `4.12:eq-constrained-minimisers-b` with \(\varepsilon_1=2\alpha_k\ell_p^2\). For every plaquette or bond \(\xi\subset X''^{\sim2}\), put \(n=n_E(\xi)\). Then
\[
\begin{array}{c|cc}
 & \eta^{-2}|\partial U(\mathfrak B,D)(\xi)-1|
 & |J(U(\mathfrak B,D))(\xi)|\\ \hline
 n\ge p & 2L^2B_3\alpha_k & 2L^3B_3\alpha_k\ell_p^{-1}\\
 n<p & 3L^2B_HK_b\alpha_k\ell_n^{-1}
     & 3L^3B_HK_b\alpha_k\ell_n^{-2}
\end{array}                                                   \tag{20}
\]
The first column is read on plaquettes and the second on bonds. Here \(D_{\mathfrak Q}=204M\) in \(K_b\); it is a fixed parameter, not the diameter of \(X''\). The constants are uniform in \(k,E,p,X''\), the number of refined blocks, and the diameter. No containing box for \(X''\), global small gauge, stronger source-slot condition, or compatibility of new boundary rows is added as a hypothesis.

This is equivalent to the outstanding outside proposition, not a claimed reduction to an easier theorem. The new reductions identify what is absent from three possible proofs: a compatible relative gauge; a uniform constrained sup-norm inverse; or a compatible tower localization with the missing scale gain. None has been substituted for (20). In particular, a proof of a one-box datum lemma alone must not be reported as a proof of (20).

## Result of the first round

**Open lemma** — Lemma RB, equation (20), for every actual outside consumer and its own boundary tower, remains unproved after the three attacks above.

The inside argument and real-factor corollary have been ported as the explicit implication in Proposition 2. The new stencil enlargement makes its current estimate valid on the whole required stencil. Its compact-group and level-\(k\) scope qualifications remain explicit; this note does not declare the literal broader wording proved. Lemmas 3–5 are hand-proved intermediate results. There is no counterexample to either target proposition here. No computer-assisted step, audit, status change, or independent-check claim is used.

## 5. Second round: anchored gauges on a uniform coarse lattice

Provenance of this continuation: Codex, 2026-11-05, at the same checkout. Sections 1–4 and their result are preserved. This round resumes Lemma RB. It does not count the first round's attacks as new attacks.

The two requested raw files were fetched once in this round, at the pinned upstream revision. Their line counts are 32,992 and 166,711. The additional outline readings were 7049–7073, 7236–7311, 7372–7378, 7780–7799, 7931–8054, 9660–9700, 9755–9789 and 9860–9916. The CA-I readings were 788–885 and 42724–45161, located through the index and its neighbouring rows. The target-label search in the three CA copies again found explicit uses only in CA-I §4.12; the unlabelled use at 10047–10058 was also reread. Balaban CMP 98, pp. 42–43, CMP 99, pp. 77–79, and CMP 102, pp. 307–309, were read from the local paper texts. The local QED3/YM3 manuscript search found no such files in this checkout or the paper folder. No substitute manuscript is assumed. The comparison with GEOH, DOM, ST1 and PR-lay remains as in §1.

### Attack 4: fix the frames at coarse base points

The first round left the constants of the local gauges unrelated. Equality of coarse data can relate them. The needed extra fact concerns the average in its original endpoint frames. An estimate only modulo an unspecified gauge does not supply this fact.

**Lemma 6 (anchored average; a port of the uniform-scale estimate).** Let \(G=SU(2)\) and put \(s=\ell_p\). On the complete carriers of the uniform iterates through level \(p\), suppose
\[
 |\partial U-1|\le F\eta^2.
\]
Use the actual symmetrised average of CA-I 817–864, in its small-curvature branch. Retain the uniform-scale curvature-averaging input from CA-I 43043–43052. There are early constants \(c_A>0\) and \(C_A<\infty\), depending only on the fixed averaging scheme and \(d,L\), such that \(Fs^2<c_A\) implies
\[
 |\mathcal M_p(U)(z,z')-U([z,z'])|\le C_A Fs^2
 \quad (|z-z'|=s).                                      \tag{21}
\]
Here \([z,z']\) is the straight fine path. Both terms use the same endpoint frames. All needed double blocks must be present.

*Proof.* This is the additional assertion of outline Proposition 1a.1.4, at 7247. We spell out its iteration, retaining its curvature-averaging input. Apply that input in units where \(s=1\): the mesh becomes \(\eta/s\), the curvature parameter becomes \(Fs^2\), and the group-valued plaquettes do not change. Choose \(c_A\le c_{\rm av}\).

First consider one step on mesh \(h\), with plaquette norm at most \(\epsilon\). Every open contour in the double block has the endpoints of the straight coarse path. Its product with the inverse straight path is a loop of length at most \((2d+2)L\) in mesh units. Sort its steps by coordinate, preserving their order within each coordinate. At most \((2d+2)^2L^2\) adjacent exchanges are needed. Then cancel opposite steps within each coordinate. Every intermediate path stays in the rectangular double block: each coordinate is a prefix of the original coordinate-step sequence. Each exchange costs at most \(\epsilon\), by unitary telescoping. Thus all the path comparisons cost at most
\[
 r=(2d+2)^2L^2\epsilon.
\]

The inner contour mean is the one in outline (QC1)–(QC7), 7963–8053. Its proved local contraction gives the following bound. If all inputs differ from a unitary \(T_0\) by at most \(r\), then their mean differs from \(T_0\) by at most \(4r\), for a fixed sufficiently small \(r\). Indeed, normalize by \(T_0^{-1}\), use \(|\log(I+E)|\le2|E|\), and use \(|Z|\le2\max|\log(T_jT_0^{-1})|\) from (QC7). For real inputs \(Z\) is anti-Hermitian, so \(|e^Z-I|\le|Z|\).

Replace the two inner means by chosen contour transports. The cost is at most \(8r\). The remaining closed contour costs at most \(r\). Hence each closed variable of the outer mean is within \(9r\) of the identity. Its logarithm has norm at most \(18r\). The outer average is the exponential of the arithmetic mean of these logarithms, as in (QC3). It is within \(18r\) of the identity. Therefore
\[
 |\mathcal M(V)(c)-V([c])|
 \le 18(2d+2)^2L^2\epsilon.                              \tag{22}
\]
Choose the smallness ceiling so that every logarithm and inner mean just used is in its stated neighbourhood.

At level \(q\), the retained curvature-averaging input gives \(\epsilon_q\le2F\ell_q^2\). Let \(e_q\) bound the difference between a level-\(q\) average and its straight fine transport, with \(e_0=0\). Equation (22) and telescoping the \(L\) straight level-\(q\) factors give
\[
 e_{q+1}\le L e_q+C_*F\ell_{q+1}^2,
 \qquad C_*=36(2d+2)^2.
\]
After division by \(\ell_{q+1}^2\), the coefficient of the previous error is \(L^{-1}\). The finite geometric sum gives
\[
 e_p\le\frac{C_*}{1-L^{-1}}Fs^2.
\]
Take \(C_A=C_* /(1-L^{-1})\). A fixed ceiling on \(Fs^2\) ensures the smallness required at every earlier level. This proves (21), with no factor growing with \(p\). This port does not prove the separately retained curvature-averaging input. □

**Lemma 7 (one relative gauge on a uniform cover).** Let \(G=SU(2)\). Work on the whole lattice, or on a periodic lattice whose periods are multiples of \(s=L^p\eta\) and at least \(8s\). Suppose
\[
 |\partial U_r-1|\le F_r\eta^2,\qquad
 \mathcal M_p(U_1)=\mathcal M_p(U_2),\qquad F=F_1+F_2.
\]
Assume the smallness and averaging inputs of Lemma 6. There are fixed constants \(C_1,C_g\), independent of \(p\), volume and diameter, such that, when \(C_1s^2F\le1/2\), a single gauge \(g\) satisfies
\[
 g(z)=I\quad\hbox{at every level-\(p\) base point},\qquad
 |U_1(x,y)g(y)-g(x)U_2(x,y)|\le C_g\eta sF.              \tag{23}
\]
Consequently, if \(C_g\eta sF\le1\),
\[
 U_1^{g^{-1}}=e^{i\eta A}U_2,\qquad
 \|A\|_\infty\le(\pi/3)C_gsF.                          \tag{24}
\]
This theorem includes nontrivial coarse holonomies. It does not require a small gauge for either field on the whole domain.

*Proof.* Around every coarse site \(z\), take the cube \(Q_z\) of radius \(2s\) in the sup norm. Use a coordinate-ordered path from \(z\) to \(x\), with the sign appropriate to each displacement. Let its transport in \(U_r\) be \(a_{r,z}(x)\). The signed version of the axial argument in §2 gives
\[
 |U_r^{a_{r,z}}(x,y)-I|\le C_0\eta sF_r,
 \qquad C_0=2(d-1).
\]
For a bond in direction \(\mu\), move its last step past the later coordinate segments. There are at most \(2(d-1)s/\eta\) exchanges; a reverse step cancels when it meets its inverse. This proves the bound also across a coordinate hyperplane through \(z\).

Put \(g_z=a_{1,z}^{-1}a_{2,z}\). Multiplication by the endpoint unitaries gives
\[
 |U_1(x,y)g_z(y)-g_z(x)U_2(x,y)|\le C_0\eta sF.          \tag{25}
\]
Along any path of \(N\) fine bonds in \(Q_z\), the corresponding transport error is at most \(NC_0\eta sF\). This follows by telescoping, with all other factors unitary.

Equality of the actual coarse data and (21) imply, for each straight coarse edge \(c\),
\[
 |U_1([c])-U_2([c])|\le C_As^2F.                         \tag{26}
\]
For coarse sites \(z,z'\) with \(|z-z'|_\infty\le2s\), connect them by at most \(2d\) such edges inside \(Q_z\). Since \(g_z(z)=I\), (25) along their fine paths and (26) give
\[
 |g_z(z')-I|\le2d(C_0+C_A)s^2F.                         \tag{27}
\]
The estimates use the shared coarse datum directly. No constants are chosen separately on overlaps or transported around cycles.

Use the tensor-product hat weights
\[
 \lambda_z(x)=\prod_{\mu=1}^d
       \left(1-\frac{|x_\mu-z_\mu|}{s}\right)_+.
\]
On a torus use the local periodic coordinate displacements in this formula. The weights sum to one. On a fine bond, the one-dimensional hats give
\(\sum_z|\lambda_z(y)-\lambda_z(x)|\le2\eta/s\); summing the other factors gives one. The supports, with one-bond room, lie in \(Q_z\).

Let \(z,z'\) have nonzero weight at either endpoint of a fixed fine bond. Then \(|z-z'|_\infty\le2s\). A coordinate path from \(z'\) to the first endpoint \(x\) lies in \(Q_z\cap Q_{z'}\) and has at most \(2ds/\eta\) bonds. Apply (25) to both relative gauges along it. Since \(g_{z'}(z')=I\), (27) gives
\[
 |g_z(x)-g_{z'}(x)|\le C_1s^2F,
 \qquad C_1=4d(C_A+2C_0).
\]
Lemma 4 applies with \(C_\lambda=2\). It constructs \(g\) by normalizing \(\sum_z\lambda_zg_z\) and gives (23) with
\[
 C_g=4(C_0+2C_1).
\]
At a coarse site only its own hat is nonzero. Thus \(g(z)=I\). These constructions are periodic when the data are periodic. Finally apply the \(SU(2)\) logarithm bound to \(U_1^{g^{-1}}(x,y)U_2(x,y)^{-1}\). This proves (24). □

**What this advances.** On a uniform coarse cover, the overlap condition (15) now follows from the actual coarse equality. It is no longer an independent hypothesis there. Retain, separately, the general-background averaging estimate of Balaban CMP 98, Propositions 6–7, in the form of outline 7264–7298. Its constant is denoted \(C_{\rm rel}\). After its smallness ceiling, (24) gives, for every uniform refinement \(0\le j\le p\),
\[
 \mathcal M_j(U_1)=
       (e^{iB_j}\mathcal M_j(U_2))^{\sigma_j},\qquad
 |B_j|\le C_{\rm rel}(\pi/3)C_g\ell_j\ell_p(F_1+F_2).
                                                               \tag{27a}
\]
Indeed apply the retained averaging estimate to \(e^{i\eta A}U_2\) in units \(s=1\), then use exact gauge covariance to restore \(g\). It supplies one gauge on the entire uniform refined lattice, including crossing bonds. This is an implication from the stated averaging input, not a new proof of that input. Its constants may depend on the averaging scheme and \(L\); a constant depending on \(d\) alone is not asserted.

**Exact failure of Attack 4 on Lemma RB.** The source comparison field \(U_\nu\) lives on \(\mathfrak B_\nu(p,X'')\), with a variable boundary tower. Even granting the uniform source curvature needed to apply the block-scale minimiser input with \(\varepsilon_1=2\alpha_k\ell_p^2\), that input's all-cell bound is only
\[
 F_\nu(y)\le2B_3\alpha_k\ell_p^2
                    \ell_{\mathfrak B_\nu}(y)^{-2}.       \tag{28}
\]
The uniform-cover proof needs the source and comparison field on every complete enlarged cube. Such cubes need not lie in \(X''\). More seriously, on a tower cell of side \(s_y\), (28) gives a local relative-potential bound \(s_yF_\nu(y)\) of order \(\alpha_k\ell_p^2/s_y\), not \(\alpha_ks_y\). The refined-datum bound obtained this way has no uniform first-order gain at a bottom tower cell. Lemma 7 does not prove the needed stronger local bound for this minimiser. It also does not identify the new constraint rows when a cube cuts the tower. Thus it closes the uniform-cover alignment problem, but not the actual outside proposition.

## 6. Attack 5: recover the scale gain from scaled distance

The first round tested the physical-distance error printed at CA-I 45143–45154. This attack instead asks whether a comparison in the actual scaled metric could recover the lost power. These are different estimates. The following geometric deduction succeeds.

**Lemma 8 (a macroscopic collar gives one local-scale factor).** Fix a site \(x\) of consumer level \(n\). Suppose every path from \(x\) to the boundary of a box \(Q\) travels physical length at least \(R>0\). Throughout the part of such a path inside \(Q\), assume the separation rule
\[
 c_E(y)\ge n+2\quad\Longrightarrow\quad
 d(x,y)\ge(c_E(y)-n-1)M/M_1.                             \tag{29}
\]
Use the scaled path metric of CA-I 43442–43450. Its local scale is the determining block side; allowing the larger adjacent side costs at most \(L\). Put \(\rho=d(x,\partial Q)\). Under \(\Phi2\),
\[
 e^{-\delta\rho}
 \le\frac{M L^2}{4R\log L}\,\ell_n.
 \quad\text{In particular, if }R\ge M,\quad
 e^{-\delta\rho}\le C_{\rm geo}\ell_n,\quad
 C_{\rm geo}=\frac{L^2}{4\log L}.                         \tag{30}
\]
The constant in the last inequality is fixed before \(M\).

*Proof.* Put \(a=M_1\log L/M>0\). Parametrize a path up to its first exit from \(Q\) by scaled length \(t\), with total length \(T\). At a site reached by a prefix of length \(t\), its distance from \(x\) is at most \(t\). For levels at least \(n+2\), (29) gives
\[
 \ell_{c_E(y)}\le L\ell_n e^{at}.
\]
The same inequality holds for levels at most \(n+1\). The determining block is no larger than this scale. Including the adjacent-block allowance, the physical length of a path increment of scaled length \(dt\) is therefore at most
\(M_1L^2\ell_ne^{at}\,dt\).

This argument also applies to the discrete path definition. On an edge starting at prefix length \(t_j\), use its largest adjacent block side. Then
\[
 \text{edge length}\le M_1L^2\ell_ne^{at_j}(t_{j+1}-t_j)
 \le M_1L^2\ell_n\int_{t_j}^{t_{j+1}}e^{at}\,dt.
\]
Summing gives
\[
 R\le\frac{M_1L^2\ell_n}{a}(e^{aT}-1),\qquad
 T\ge\frac1a\log\left(1+\frac{aR}{M_1L^2\ell_n}\right).
\]
This holds for every path, hence for its infimum \(\rho\). By \(\Phi2\),
\(\delta/a\ge2\log(2L)/\log L\ge2\).
Writing \(v=R\log L/(M L^2\ell_n)>0\), we obtain
\[
 e^{-\delta\rho}\le(1+v)^{-2}\le(4v)^{-1}.
\]
The last inequality is \((1-v)^2\ge0\). It is exactly (30). □

**Application to the proposed error.** Suppose, as an additional analytic assertion, that the two comparisons at CA-I 45143–45154 hold with \(e^{-\delta d(x,\partial Q)}\) in place of \(e^{-\delta\Delta/M_1}\). Keep the actual determining sets on both sides. At a below-slot readout with a collar as in Lemma 8, (4) then gives the errors
\[
 \begin{split}
 E_2&\le C_{\rm loc}B_3C_{\rm geo}L^2\alpha_k\eta^2\ell_n^{-1},\\
 E_4&\le C_{\rm loc}B_3C_{\rm geo}L^3\alpha_k\ell_n^{-2}.
 \end{split}                                             \tag{31}
\]
These have exactly the powers required in (20). Thus a macroscopic collar and scaled decay can remove the defect in (18). Increasing a physical collar by a fixed amount in the printed estimate cannot do this.

There is also room for constants on the covered class. If \(Q\) has sides at most \(102M\), the inside proof uses at most half of the \(K_b\) in (20). If \(C_{\rm loc}\) is fixed before \(M\), an early enlargement of \(B_H\) can make
\[
 C_{\rm loc}B_3C_{\rm geo}\le\tfrac32 B_HK_b
\]
for every allowed \(M\ge M_1\). The remaining half of the printed below-slot bound then pays (31). This is a conditional constant comparison; no value of \(C_{\rm loc}\) has been proved here. The inside estimate must apply at the readout of \(X''\cap Q\), including its two-layer exclusion.

I tried to obtain the strengthened comparison by extending a local constrained variation to the full domain. Such an extension must preserve the old constraint rows that cross the artificial boundary. Averaging locality proves this only for rows with complete carriers away from that boundary. It does not prove it for the replaced rows. The granted composition at CA-I 44874–44875 concerns refinement; it does not say that intersection with \(Q\) preserves the requisite rows. The outline's own comparison, 9783–9789 and 9913, requires a joined sequence with a single-layer collar. DOM Lemma 11 requires a path in one fixed determining system. Neither statement supplies the present comparison.

**Exact failure of Attack 5.** The geometric scale gain (30) is proved. The required analytic comparison in scaled distance, for the actual changed boundary tower, is not. Nor has a box with the stated collar been supplied for every outside readout. The physical-distance comparison in the account cannot be substituted for this stronger assertion. This attack therefore does not prove (20), even though it removes the scale-loss objection when its analytic and geometric premises hold.

## 7. Attack 6: work with curvature before choosing a relative gauge

I next tried a direct regularity argument. It would avoid the smallness of a relative datum and avoid changing the determining system. At quadratic order there is an exact useful identity.

**Lemma 9 (the quadratic constrained minimum is a curvature projection).** Let \(H_1,H_2\) be finite-dimensional real Hilbert spaces, \(C:H_1\to H_2\) a linear curl, and \(Q:H_1\to H_0\) a fixed linear constraint map. For \(a\in H_1\), minimize
\[
 \tfrac12\|Cu\|_2^2\quad\hbox{subject to }Qu=Qa.
\]
Let \(W=C(\ker Q)\), and let \(P\) be the orthogonal projection onto \(W^\perp\) in \(H_2\). A minimum exists and every minimizer has the same curvature,
\[
                         Cu=P(Ca).                       \tag{32}
\]
In particular it depends on \(a\) only through its curvature, and
\(\|Cu\|_2\le\|Ca\|_2\). No gauge slice or invertibility of \(C^*C\) is needed.

*Proof.* The feasible set is \(a+\ker Q\), so its set of curvatures is \(Ca+W\). This affine subspace is closed. Write \(Ca=P(Ca)+(I-P)(Ca)\), with the second term in \(W\). Its unique vector of least norm is \(P(Ca)\). Some element of \(\ker Q\) maps to \(-(I-P)(Ca)\), by the definition of \(W\). Adding that element to \(a\) gives a minimizer. Orthogonality proves both the uniqueness of the curvature and the norm bound. □

Equation (32) bypasses the mean-zero datum of Attack 2 and takes curvature as its direct input. The remaining question is a uniform pointwise estimate for this particular projection and its current readout on the actual tower.

Energy contraction alone cannot give that estimate. For an integer \(m\ge1\), take a unit vector in \(\mathbb R^{m^2+1}\) with coordinates
\[
 v=2^{-1/2}(1,m^{-1},\ldots,m^{-1}).
\]
There are \(m^2\) coordinates equal to \(m^{-1}/\sqrt2\); hence \(\|v\|_2=1\). The orthogonal projection \(P_m=vv^*\) has \(2\)-norm one, but
\[
 \|P_m\|_{\infty\to\infty}\ge
 \sum_j|(P_m)_{1j}|=\tfrac12(1+m).                       \tag{33}
\]
This is only a demonstration about norm inference. These matrices are not asserted to be the lattice projection in (32).

The alternative is a local maximum argument. The outline sketches it at 9860–9868. To test its last step, take \(A,\theta,\lambda,R\ge0\) and nonnegative functions \(r,v\) satisfying
\[
 r(x)\le A v_R(x)+\theta r_R(x),\qquad
 v_R(x)=\sup_{d(x,y)\le R}v(y),\quad
 r_R(x)=\sup_{d(x,y)\le R}r(y).                           \tag{34}
\]
On a finite domain define \(\|f\|_{\lambda,x_0}=\sup_y e^{-\lambda d(x_0,y)}|f(y)|\). The triangle inequality gives
\(\|f_R\|_{\lambda,x_0}\le e^{\lambda R}\|f\|_{\lambda,x_0}\).
If \(\theta e^{\lambda R}<1\), multiplication of (34) by the weight and taking suprema gives
\[
 r(x_0)\le
 \frac{Ae^{\lambda R}}{1-\theta e^{\lambda R}}
 \sup_y e^{-\lambda d(x_0,y)}v(y).                        \tag{35}
\]
All quantities are finite, so moving the last term to the left is legitimate. This proves the maximum argument, given (34).

The missing step is (34) for the actual gauge-invariant curvature and current, with \(v\) given by the actual datum tests. To derive it from (32), one needs a uniform absolute-row or local-cutoff estimate for the curvature projection and its differentiated readout. The energy argument supplies neither. In the nonlinear problem, a second difficulty enters at precisely this step: the second variation on a constraint fibre contains the constraint's second derivative contracted with its multiplier. It is not just \(C^*C\). The explicit extra current term is recorded in outline 7372–7378. The general response estimate of Balaban CMP 102, Proposition 9 and (190), applies on its admitted regular branch; its statement does not establish (34) for a new boundary tower.

**Exact failure of Attack 6.** I obtained (32) and the implication (34) ⇒ (35). I did not prove the uniform pointwise curvature/current estimate needed to establish (34) on the actual determining sets, or its nonlinear absorption with the required constants. Equation (33) identifies why a variational norm bound cannot fill that step. The outline's sketched local regularity profile, 9678–9684, cannot be used as an already proved replacement for it. No counterexample to that profile or to re-blocking is claimed.

## 8. Constant order and remaining obligation after this round

The new constants in Lemmas 6–9 are fixed after the averaging scheme, \(d,L\), and the existing early analytic constants. Lemma 7's \(s^2F\) ceiling is imposed afterwards. Lemma 8 uses exactly the existing \(\Phi2\) floor and leaves \(C_{\rm geo}\) independent of \(M\). None of the three attacks permits choosing \(M\), a response constant, or a coupling ceiling as a function of \(k-n\), the number of blocks, or the diameter.

One part of the outside implication does not require a containing box. If the source bound \(|\partial\bar U-1|<\alpha_k\eta^2\) holds on every carrier in \(X''\), the averaging argument at CA-I 44226–44258 proves clause (a) on that domain verbatim. The two-layer argument at 44271–44303 then proves clause (b) at \(n\ge p\). The box is used in the below-slot argument to supply the common small gauge. This observation is conditional on the stated carrier coverage; it does not infer that coverage for arbitrary outside consumers from their names.

The single remaining target is still **Lemma RB, with the exact hypotheses and constants of (20)**. The uniform-cover theorem is a new partial result for the first route proposed by the account. The scaled-collar calculation is a new sufficient geometric step for its second route. The curvature projection is a third approach to the same local regularity estimate. None is substituted for the actual boundary tower or for an unproved source-membership assertion.

## Result

**Open lemma** — For every outside consumer allowed by CA-I `4.12:prop-reblocking-outside`, prove existence of its actual constrained minimiser and the two cases of the curvature/current bounds in (20), uniformly in depth, domain and boundary tower, with the account's order of constants.

Three new attacks were completed in this round. Anchoring the gauges closes the uniform-cover overlap problem (Lemma 7), but the all-cell minimiser estimate (28) loses the required scale gain. Scaled distance supplies that power (Lemma 8), but the actual tower comparison and all-consumer collar coverage remain unproved. Working directly with curvature gives the quadratic projection (Lemma 9) and the weighted maximum argument (35), but not the required uniform local inequality (34).

The inside implication and real-factor corollary in Proposition 2 are retained with their stated qualifications. There is no proof of the literal full pair of propositions and no counterexample to either. The new results are hand proofs or explicitly stated implications from the account's inputs; none has been checked by another model. This is research text, not an audit, and grants no status.
