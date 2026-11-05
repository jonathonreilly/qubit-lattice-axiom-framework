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

## Result of the second round

**Open lemma** — For every outside consumer allowed by CA-I `4.12:prop-reblocking-outside`, prove existence of its actual constrained minimiser and the two cases of the curvature/current bounds in (20), uniformly in depth, domain and boundary tower, with the account's order of constants.

Three new attacks were completed in this round. Anchoring the gauges closes the uniform-cover overlap problem (Lemma 7), but the all-cell minimiser estimate (28) loses the required scale gain. Scaled distance supplies that power (Lemma 8), but the actual tower comparison and all-consumer collar coverage remain unproved. Working directly with curvature gives the quadratic projection (Lemma 9) and the weighted maximum argument (35), but not the required uniform local inequality (34).

The inside implication and real-factor corollary in Proposition 2 are retained with their stated qualifications. There is no proof of the literal full pair of propositions and no counterexample to either. The new results are hand proofs or explicitly stated implications from the account's inputs; none has been checked by another model. This is research text, not an audit, and grants no status.

## 9. Third round: use the frozen admission and locality results

Provenance of this continuation: Codex, 2026-11-05, checkout `5129d8d4e01a632c1293ab712f8a758dcc64e6f5`. Sections 1–8, their proofs and their results are preserved. This round resumes their Lemma RB. It grants no status. Credit remains with Ethan Sussman and Levent Alpoge, with Claude and Codex as authors of their text, and Tadeusz Balaban for the constructions being extended.

The new inputs are frozen `mu.md`, `oc.md`, `pda.md`, and checked ports `port/p4-operator.md` and `port/p7-torus.md`. They retain their own hypotheses. In particular:

| Input | What can now be used | What is not its conclusion |
|---|---|---|
| MU, §§4–7 and Result | Admission and arbitrary-subdomain nesting in the actual CMP 109 Lemma 4 windows; both tower rules | Admission of every outside re-blocking datum, or equality after replacing the induced inner datum by a different datum |
| OC, §§4–5 and Result | The own-constant cube gauge, including its first differences, for the stated small pairs and real backgrounds | A cube gauge for an arbitrary re-minimised CMP 122b field before its admission |
| PDA, Result and freeze scope | Geometric (A1) for one prepared operation, including stopped prefixes, from old (A1) | (A2), admission of fields, or equality of constraint maps after cutting a domain |
| P4, A9 and A9-F8 | The stated covariance/source operators and their local analytic extensions on admitted backgrounds | A new real background, or identification of those operators with the response to a change of determining data |
| P7, P7-H2, P7-Hmin and the non-wrapping proof | Equality of terms with matching complete footprints; torus-independent constants on the stated domains | Equality of minimisers whose artificial boundary data differ |

The source comparison in §1 remains valid for GEOH, DOM, ST1 and PR-lay. None of these new results replaces their differing rows or admission premises. The following three attacks use the account's two proposed routes: refinement and localisation. They do not count any of Attacks 1–6 again.

## 10. Attack 7: use MU to replace the tower comparison by exact nesting

The proposed shortcut is to restrict the outside minimiser to a small box, apply MU, then use Proposition 2 there. MU now proves the nesting step in its stated windows. The datum in that identity must still be tracked.

**Corollary 10 (where the induced and prescribed data can differ).** Let \(W=U(\mathcal S,M_{\mathcal S}\bar U)\) be an admitted real minimiser to which frozen MU applies. Let \(Y\) and its actual inner tower \(\mathcal T\) satisfy MU's hypotheses. Keep the endpoint frames fixed, and put
\[
 D_Y^W=M_{\mathcal T}(W|_Y),\qquad
 D_Y^0=M_{\mathcal T}(\bar U|_Y).                         \tag{36}
\]
Let \(\mathcal R_Y\) be the inner rows which are also rows of \(\mathcal S\), with the same averaging functional, complete carrier and endpoint frames. Then
\[
 D_Y^W(c)=D_Y^0(c)\quad(c\in\mathcal R_Y),\qquad
 U(\mathcal T,D_Y^W)\simeq W|_Y.                          \tag{37}
\]
Here \(\simeq\) denotes the real gauge identification specified by MU. If
\(\sup_c|D_Y^0(c)(D_Y^W(c))^{-1}-1|<\epsilon_G\), the datum
\[
 B_Y(c)=i^{-1}\log\bigl(D_Y^0(c)(D_Y^W(c))^{-1}\bigr)      \tag{38}
\]
is Lie-algebra valued, is zero on \(\mathcal R_Y\), and satisfies
\[
 D_Y^0=e^{iB_Y}D_Y^W,\qquad
 |B_Y(c)|\le(\pi/3)|D_Y^0(c)-D_Y^W(c)|.                  \tag{39}
\]

*Proof.* On a row in \(\mathcal R_Y\), locality identifies its two inner evaluations with the corresponding outer evaluations. The constraint on \(W\) makes those equal. MU supplies the second identity in (37), including its real criticality and boundary-action argument; those are ported, not proved again. The principal logarithm and the unitary norm identity give (38)–(39), by CA-I 42740–42747. The logarithm of the identity is zero. □

This is a statement about actual row functionals. Agreement of row endpoints, or agreement of the sets of sites, is insufficient. It also has an explicit admission premise on \(W\); it cannot first construct an outside minimiser by assuming that minimiser is in MU's window.

For localisation, take \(\mathcal S=\mathfrak B_E(p,X'')\) and \(Y=X''\cap\mathfrak Q\). Equation (37) identifies the restriction with a minimiser whose datum is \(D_Y^W\). Proposition 2 estimates the minimiser at \(D_Y^0\). These are two different inputs. Thus MU removes the need to re-prove criticality at the **induced** datum on its admitted class. It does not set \(B_Y=0\).

I next tried to show that every changed row lies in a distant artificial collar. There is a useful limited conclusion. In a region where both boundary towers have saturated at level \(p\), their block levels both equal \(\min(p,c_E)\). If their fixed roots and interface rules agree there, a row with its whole carrier in that region belongs to \(\mathcal R_Y\). Equation (39) is therefore supported off those rows. The sufficient saturation criterion at CA-I 43000–43006 applies at distance at least \(2M_1\ell_p\) from the respective boundaries. The two-layer readout condition gives only \(2M\ell_n\) when \(n<p\). Their ratio is
\[
 \frac{2M\ell_n}{2M_1\ell_p}
       =\frac M{M_1}L^{n-p},                              \tag{40}
\]
which can be arbitrarily small. Saturation at level \(p\) is a sufficient criterion, not a necessary one; the failure of (40) to exceed one is not a counterexample. It shows why this criterion does not establish all-consumer row agreement. Near the inherited boundary, a separate comparison of the actual intrinsic tower rules is still needed.

PDA does not fill that comparison. It proves (A1) for the prepared \(\Omega''\) sequence, with its own completion rule. The consumer tower is instead the tower of **each** \(X''\), and the cut tower is the tower of **each** \(X''\cap\mathfrak Q\). Even an (A1) proof for both would assert gaps and grids, not equality of their averaging functionals. MU's own proof respects this distinction: its boundary data are averages of the field being restricted (`mu.md`, (5.3)–(5.5)).

**Exact failure of Attack 7.** Exact nesting reaches \(D_Y^W\), whereas the inside estimate reads \(D_Y^0\). I did not establish an admitted, uniformly small change between these data on the actual changed rows, or place every such row at the required scaled distance from every readout. Using (37) with \(D_Y^0\) in its left side would change MU's statement. The new result is the exact support reduction (36)–(39) on MU's admitted class, not an outside admission theorem.

## 11. Attack 8: obtain the missing datum response from P4

The second attempt uses the newly available operator port instead of the raw datum estimate of Attack 7. P4 constructs inverses and source operators. To use them, the linear problem produced by differentiating the **actual constrained minimum** must be identified. The following calculation keeps the nonlinear constraint term.

**Lemma 11 (response from a constraint lift and a tangent inverse).** Work in finite-dimensional real coordinates on a fixed gauge slice. Let \(S\) and \(q=(q_a)\) be \(C^2\), where \(q\) gives independent coordinates of the actual determining datum. Suppose a differentiable curve \((u_t,\lambda_t,d_t)\) satisfies
\[
 q(u_t)=d_t,\qquad
 \nabla S(u_t)=Q_t^T\lambda_t,\qquad Q_t=Dq(u_t),        \tag{41}
\]
and \(Q_t\) is onto. At one fixed \(t\), define
\[
 K=\nabla^2 S(u_t)-\sum_a\lambda_{t,a}\nabla^2q_a(u_t).   \tag{42}
\]
Let the columns of \(Z\) be a basis of \(\ker Q_t\), assume \(Z^TKZ\) invertible, and put
\[
 C=Z(Z^TKZ)^{-1}Z^T.
\]
For any right inverse \(E\) of \(Q_t\), the response is
\[
                  \dot u_t=(I-CK)E\dot d_t.             \tag{43}
\]
The expression is independent of the chosen right inverse.

*Proof.* Differentiate both equations in (41). Their derivatives are
\[
 Q_t\dot u_t=\dot d_t,\qquad
 K\dot u_t-Q_t^T\dot\lambda_t=0.                        \tag{44}
\]
The term subtracted in (42) is precisely the derivative of \(Q_t^T\) contracted with \(\lambda_t\). Write \(\dot u_t=E\dot d_t+Zz\). Multiplying the second equation of (44) by \(Z^T\) gives
\[
 Z^TKZz=-Z^TKE\dot d_t.
\]
Inversion proves (43). If \(E_1-E_2=ZT\), then
\(CKZT=Z(Z^TKZ)^{-1}(Z^TKZ)T=ZT\). Hence
\((I-CK)(E_1-E_2)=0\). □

This is the differential form of the account's refinement-and-response route. It is not a replacement for Balaban's construction. The correct inverse is on the tangent space, and the Hessian is the Lagrange Hessian (42). Dropping its last term would return the incomplete curvature-only attempt of §7.

P4's square completion has the closely related, already proved formula \(-\mathsf C\mathsf J A'\). But its \(A'\) is the complementary **fluctuation field**, and \(\mathsf C\) is the inverse form on the integrated fluctuation coordinates: CA-I 46053–46074. Here \(\dot d\) is a change of the prescribed **averaged datum**. To identify the formulas one must supply the actual lift \(E\), its constraint normalisation and carriers, and the equality of the physical graph form with (42) in these coordinates. A similarity of Schur-complement formulas does not identify their spaces.

There is a simple hand test of whether positivity and decay of the form alone could supply the missing lift. Let
\[
 S(x,z)=\tfrac12(x^2+z^2),\qquad q(x,z)=x/N,
 \qquad N\in\mathbb N,\ N\ge1.
\]
The full Hessian is the identity. The tangent inverse is \(C=\operatorname{diag}(0,1)\), independent of \(N\). Both are diagonal and have norm one. Yet the exact minimum at datum \(d\) is
\[
                 u(d)=(Nd,0),\qquad u'(d)=(N,0).        \tag{45}
\]
Indeed the constraint fixes \(x=Nd\), and the nonnegative term \(z^2/2\) has its unique minimum at zero. Thus even bounds on the **whole** form, its tangent inverse, and their off-diagonal entries do not control the datum response without a bound on the correctly normalised lift. This is a test of the inference, not a lattice counterexample; Balaban's actual normalisation must be used, not varied as in this example.

I then tried to integrate (43) along the principal-log path suggested by (38). On any interval where the path is admitted, the formula is valid. P4-H-prepared's (A1) is now supplied by PDA for its prepared operation. However, P4 still requires the separate (A2) and the real-background class. Its local-ball clause begins with a globally given \(U\in\mathcal U_{\mathbb R}\), CA-I 46111–46121. The cutoff extends the **perturbation** about that background; it does not construct the missing real background. OC supplies the real gauges for its stated pair classes, and expressly leaves later re-minimised CMP 122b admission separate (`oc.md`, end of §5). These premises cannot be assumed at the next time of continuation to prove that the continuation has not left them.

**Exact failure of Attack 8.** The required response is (43), with the actual tower's lift and multiplier term. I did not identify a uniformly local lift and all its curvature/current readouts with P4's source operator on every outside consumer, or establish admission along the required datum path. Example (45) rules out filling that identification from operator bounds alone. The calculation closes the algebraic identification problem **once** those objects are supplied; it does not supply them.

## 12. Attack 9: build a torus comparison field, then retain its boundary error

P7 suggests moving a protected local calculation to a convenient torus. I first constructed the required real extension on a healed cube. This avoids assuming that an arbitrary exterior field already has a global small gauge. The construction uses the account's axial gauge and its exponential-product estimate, not a replacement averaging map.

**Lemma 12 (real extension of a cube germ).** Let \(G=SU(2)\), let \(R\ge4\eta\), and let \(Q\) be a fine-lattice cube of side \(4R\). Suppose
\[
                    |\partial U-1|\le F\eta^2\quad\hbox{on }Q.
\]
Put \(c_{\rm ax}=\frac{4\pi}{3}(d-1)\) and \(a=c_{\rm ax}RF\). If
\[
                         4\eta a\le1,\qquad R^2F\le1,  \tag{46}
\]
there are a real gauge \(g\) on \(Q\) and a configuration \(V=e^{i\eta A^{\rm ext}}\) on the whole fine lattice such that
\[
 \|A^{\rm ext}\|_\infty\le a,\qquad
 |\partial V-1|\le C_{\rm ext}F\eta^2,\qquad
 C_{\rm ext}=1+4c_{\rm ax}+24c_{\rm ax}^2.                 \tag{47}
\]
The configuration equals \(U^g\) on every bond whose endpoints have distance at least \(R+2\eta\) from \(\partial Q\). It equals one outside \(Q\) and in its outer two fine layers. It can be repeated on any compatible torus with periods at least \(8R\), with the same bounds. The assertion concerns the extension field, not its constrained minimiser.

*Proof.* The axial lemma gives \(U^g=e^{i\eta A}\) on \(Q\), with \(|A|\le a\). Indeed its smallness condition is \(4(d-1)RF\eta\le1\), which follows from (46). The \(SU(2)\) logarithm is the one justified in §2.

For \(x\in Q\), let \(r(x)\) be its distance in the maximum norm to the geometric boundary. Define
\[
 \chi(x)=\min\{1,(r(x)-2\eta)_+/R\},\qquad
 \chi_b=\min\{\chi(x),\chi(y)\}\quad(b=\langle x,y\rangle).
\]
Set \(A^{\rm ext}(b)=\chi_bA(b)\) on positive bonds of \(Q\), and set it to zero on other positive bonds. Reverse bonds have inverse group variables. The function \(\chi\) is \(R^{-1}\)-Lipschitz and lies in \([0,1]\). The value, support and agreement assertions follow directly.

Here is the curvature check; no bound on the full first derivative of the axial potential is assumed. On a plaquette in \(Q\), list its four signed positive-bond potentials as \(A_1,A_2,-A_3,-A_4\). The exponential-series remainder estimate used at CA-I 43967–43982 gives
\[
 \left|\partial(U^g)-1-i\eta(A_1+A_2-A_3-A_4)\right|
                   \le12\eta^2a^2.
\]
Consequently
\[
 |A_1+A_2-A_3-A_4|\le\eta F+12\eta a^2.                \tag{48}
\]
Let \(x\) be the lower corner. Every vertex of this plaquette is within \(\eta\) of \(x\) in the maximum norm. Thus every bond weight differs from \(\chi(x)\) by at most \(\eta/R\). It follows that
\[
 |\chi_1A_1+\chi_2A_2-\chi_3A_3-\chi_4A_4|
       \le\eta F+12\eta a^2+4\eta a/R.
\]
Apply the same exponential-series remainder bound to these four weighted potentials. This gives
\[
                 |\partial V-1|
           \le\eta^2(F+4a/R+24a^2).
\]
By \(R^2F\le1\), \(a^2=c_{\rm ax}^2R^2F^2\le c_{\rm ax}^2F\), proving (47). A plaquette crossing the boundary of \(Q\) has every potentially nonzero bond in its zero buffer. Its variables are all one. Plaquettes wholly outside have the same property. Finally, disjoint periodic copies have an identity buffer between them, so the same plaquette-by-plaquette argument applies on the torus. □

If \(Q\) is healed and lies in \(Y_4\), use \(F=\alpha_k\). A coupling ceiling after \(M\) pays (46) when \(R\) is a fixed multiple of \(M\). If \(4R\le102M\), the potential bound is at most half the \(\mathfrak a_{\max}\) used in Proposition 2. Every determining row whose complete carrier lies in the protected cube has the same datum as \(\bar U\), in the restricted gauge \(g\), by the exact locality and covariance at CA-I 43018–43027. The curvature factor \(C_{\rm ext}\) is explicit; this extension does not preserve the sharper datum parameter \(2\alpha_k\ell_p^2\) outside the protected cube. Nor does it prove that every outside readout has such a healed cube.

The outline has a related, sketched axial-extension test at SA 17585. It extends inward from an exterior surface and allows a factor of order \(M^2\). Lemma 12 instead preserves a prescribed inner germ, cuts off through a collar and records the quadratic error. P4's local cutoff at CA-I 46800–46828 extends a perturbation about an already given real background. Lemma 12 constructs a real field but does not claim P4's full background-class admission for it. OC can be used when a resulting minimal background belongs to OC's stated classes; its conclusion cannot be applied to the extension solely because it is real.

I next tried exact transfer by P7. Its source theorem begins at CA-I 58187, with its standing hypotheses at 58188–58218. In its proof, the transferred objects are sums of words with complete footprints, CA-I 58443–58470 and 58640–58669. P7 therefore identifies local words once their full data and geometry agree and the arguments are admitted. A word of a full inverse can leave the protected cube. It is not one of the words identified by this local agreement. The global minimisers at the original and extended data are not declared equal by P7. The terms leaving the cube must be estimated, not deleted.

There is enough scale gain to sum those terms, **if** the actual datum response is available. The following calculation includes the loss of half the rate when summing all changed rows, which (30) alone did not address.

**Lemma 13 (summed boundary response still has the required scale power).** Fix the actual determining system and a below-slot readout of level \(n\). Put \(s_x=\ell_{\mathfrak B}(\xi)\). Suppose \(D_t\), \(0\le t\le1\), is a piecewise \(C^1\) path of admitted real data with minimisers \(W_t\). Write
\[
 v_t(c)=i^{-1}\dot D_t(c)D_t(c)^{-1},\qquad
 f_2(t)=\eta^{-2}|\partial W_t(\xi)-1|,\qquad
 f_3(t)=|J(W_t)(\xi)|.
\]
The two readouts are used on their respective plaquettes and bonds. Assume they are absolutely continuous and, almost everywhere,
\[
 s_x^r|\dot f_r(t)|\le C_R\sum_c e^{-\mu d(x,c)}|v_t(c)|,
                    \qquad r=2,3.                      \tag{49}
\]
Here the metric is fixed; any moving metrics have already been compared to it. Suppose
\[
 |v_t(c)|\le C_v\alpha_k,\quad
 v_t(c)=0\ \hbox{unless }d(x,c)\ge\rho,\quad
 \sum_c e^{-\mu d(x,c)/2}\le c_\mu.                      \tag{50}
\]
Assume the geometry in Lemma 8 up to an exit at physical distance \(R\ge M\), with \(\rho\) at least that exit distance in the scaled metric. If
\[
 \frac{\mu M}{2M_1}\ge\log(2L),\qquad
 s_x\ge\ell_n/L,                                        \tag{51}
\]
then
\[
 \begin{split}
 |f_2(1)-f_2(0)|&\le C_*L^2\alpha_k\ell_n^{-1},\\
 |f_3(1)-f_3(0)|&\le C_*L^3\alpha_k\ell_n^{-2},\qquad
 C_*=C_RC_vc_\mu L^2/\log L.                            \tag{52}
 \end{split}
\]
All constants in (49)–(50) are assumed fixed before \(M\).

*Proof.* For a changing row,
\(e^{-\mu d(x,c)}\le e^{-\mu\rho/2}e^{-\mu d(x,c)/2}\).
Sum first, then integrate (49) in \(t\). The result is
\[
 |f_r(1)-f_r(0)|\le C_RC_vc_\mu\alpha_k s_x^{-r}
                                      e^{-\mu\rho/2}.    \tag{53}
\]
The path-length proof of Lemma 8, before its last inequality, gives with \(a_0=M_1\log L/M\)
\[
 \rho\ge a_0^{-1}\log(1+v),\qquad
 v=\frac{R\log L}{ML^2\ell_n}.
\]
Condition (51) implies \(\mu/(2a_0)\ge\log(2L)/\log L>1\). Hence
\[
 e^{-\mu\rho/2}\le(1+v)^{-1}\le v^{-1}
                \le\frac{L^2}{\log L}\ell_n.
\]
Insert this and the bound on \(s_x\) into (53). This proves both lines of (52). No number of changed rows appears. □

For \(\mu=\delta\), (51) is the existing \(\Phi2\). For a smaller proved response rate, it would be another lower floor on \(M\), after that rate is fixed. The half-rate summability in (50) must be available at that rate too; it is not inferred from a sum at a faster rate. A response theorem with such a rate and sum would fit the account's order. If a comparison solution uses at most half the \(K_b\) budget, its remaining half pays (52) once
\[
                         C_*\le\tfrac32 B_HK_b.          \tag{54}
\]
Since \(K_b=K_0M\), \(K_0=\frac\pi3(d-1)c_Qc_d(1+3L^2)204\), an early enlargement to \(B_H\ge 2C_* /(3K_0M_1)\) would suffice for every \(M\ge M_1\). More generally, if the velocity bound is \(C_vM\alpha_k\), with \(C_v\) still fixed before \(M\), the same proof multiplies (52) by \(M\). The budget then requires only \(B_H\ge2C_* /(3K_0)\), again an early choice. This allows a linear \(M\) loss of the kind already present in \(K_b\); a further power cannot be hidden in an early constant. In either calculation the proved response constants must be kept at their originally established values when enlarging the reported bound \(B_H\). This is conditional arithmetic. No value of \(C_R,C_v,c_\mu\), or response identity, is supplied by (54).

**Exact failure of Attack 9.** Lemma 12 constructs the comparison field on a covered local class. P7 transfers its matching, admitted local words, not the full minimiser. Lemma 13 proves that summing a genuine boundary response would retain the missing power. I did not construct the admitted same-system path with (49)–(50), or prove the requisite healed-cube and changed-row collar coverage for every outside consumer. The failed step is the transfer from the constructed comparison field to the original constrained problem. Enlarging the torus or declaring two local germs equal does not make that transfer exact.

## 13. Constant order, source checks and the remaining target

The extension constants \(c_{\rm ax},C_{\rm ext}\) depend only on \(d\). Its radius \(R\), when used as a fixed multiple of \(M\), is chosen with \(M\); (46) is then a final upper ceiling on \(\alpha_k\). For \(G\ne SU(2)\), the additional logarithm ceiling from §2 would also be needed. Nothing here infers the full target's regularity from the extension's curvature bound alone.

The constants and decay rate in a future application of Lemma 13 must first be proved uniformly for the actual constraints. They fix any enlargement of the response bound before \(M\) is chosen. Next choose \(M\) above the corresponding floor (51), and finally decrease the couplings. The ordering is the one at CA-I 43573–43584. Choosing a rate or a constant after learning the depth, domain, number of blocks or particular boundary tower would not prove Lemma RB. Lemma 11 is an exact identity with explicit hypotheses; it supplies no uniform constant by itself.

For this continuation the index rows and neighbouring rows were used before the bounded source readings. The additional comparisons were checked against CA-I 42740–42747 (logarithms), 42988–43027 (actual towers, locality and covariance), 43559–43595 (order and budgets), 43787–43809 and 43967–43982 (axial gauge and product remainder), 46053–46074 and 46111–46121 (the spaces of P4's operators and local-ball premise), 46800–46828 (perturbation cutoff), and 58187–58218, 58443–58470, 58640–58669 (P7's hypotheses and transferred ingredients). The related extension at SA 17585 was read in its preparation-stage context; it is a sketch, not an input used to discharge Lemma 12. MU, OC and PDA are used at their frozen scopes. The earlier source comparison with GEOH, DOM, ST1 and PR-lay is retained, in particular ST1's settlement requirement. No source has been promoted from a conditional statement to an all-consumer assertion.

These attacks do not produce three new assumptions to add to the outside proposition. Their admission, lift and collar premises describe possible proof obligations, not restrictions on the conclusion requested. The remaining statement is still the single Lemma RB of §4. Existence and the \(n\ge p\) case retain the conditional carrier-coverage implication recorded in §8; no all-consumer coverage has been inferred from PDA or from the name of a consumer.

## Result

**Open lemma** — Under exactly the hypotheses of CA-I `4.12:prop-reblocking-outside`, every actual outside consumer pair \((p,X'')\), with \(\mathfrak B=\mathfrak B_E(p,X'')\) and \(D=M_{\mathfrak B}\bar U\), admits the account's regular constrained minimiser at \(\varepsilon_1=2\alpha_k\ell_p^2\), and that minimiser satisfies both curvature/current cases of (20) on \(X''^{\sim2}\), with \(K_b=\frac\pi3(d-1)c_Qc_d(1+3L^2)204M\), uniformly in depth, domain and the actual boundary tower, in the account's order of constants.

Three new attacks leave this precise statement open. Attack 7 proves the exact induced-datum identity and common-row agreement, but does not identify the prescribed datum with that induced datum or admit a uniform path between them. Attack 8 proves the constraint-response formula, but P4's fluctuation operators have not been identified with its actual lift and Lagrange Hessian on every consumer. Attack 9 constructs a real cube extension and proves that a summed response would retain the required scale power, but does not admit the required comparison path or cover every changed boundary row and readout. None of these failures is a counterexample to re-blocking.

The two earlier rounds, including the inside implication and real-factor corollary with their stated qualifications, are preserved. The new hand results are Corollary 10 and Lemmas 11–13, with all conditional premises displayed. No computation discharges a mathematical step, no independent check is claimed, and this research text grants no status or proof of T0.
