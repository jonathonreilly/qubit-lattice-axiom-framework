lead: anthropic/claude-opus-5-5/max mac-mini-worker
lease_until: 2026-11-06T14:12Z

# CMP 109 (1.17) at complex pairs: a corrected statement and its proof

Draft for the owner. Not sent anywhere. Research text; it grants no status.

**Provenance.** Written by Claude Opus 5.5 (max effort), Mac mini worker, at commit cbb40eca5. It writes up `library/l17c.md` (Codex) and `library/b109.md` P19–P20 (Codex), with the repairs of `gates/l17c-gate.md` and `gates/p20-gate.md` (each one line-by-line reading by Claude). The mathematics is theirs. The presentation and compatibility/domain repairs are described in §9(8). As recorded on 2026-11-05: checked line by line by Codex (gates/wu-l17-gate.md, REVISE), repairs applied by Codex at checkout f5986aa06. The gate read the pre-repair draft; applying its repairs is not a new independent check or an audit.

**Sources.** Ethan Sussman and Levent Alpoge, with Claude and Codex as authors of their text, commit 31a47c543775. CA-I, CA-II, CA-III are `theorem_0_complete_account_raw_{I,II,III}.tex`; SA is `YM4_sketch_500.tex`. Numbers are source lines. Each passage quoted was read in a bounded excerpt of a copy fetched for this note.

**Credit.** Tadeusz Balaban, for the stage theorem this proof rests on: the critical-orbit theorem of CMP 102 (Theorem 1, its analytic continuation in §G, Proposition 9), which carries every member of the tower; and for the averaging and gauge constructions of CMP 98 and 99; the flat propagator bounds of CMP 89, 95, 96 and 99b; the regularity spaces and the sentence (1.17) of CMP 109. Sussman and Alpoge (with Claude and Codex): the two-rule hereditary class, the corrected budget and the real-point argument (SA Theorem 5(a), mechanism 8), and the small-exponential argument (SA (ER8)).

## 1. The statement in their account, and its status there

**The sentence.** CA-I 32599–32623 transcribes CMP 109 p. 263. Let \(\alpha_0'<\alpha_0\), \(\alpha_1'<\alpha_1\). Let \((\mathbf U,\mathbf J)\) satisfy conditions (i)–(iii) of Balaban's regularity spaces at level \(j\) on \(X\), with \(\alpha_0',\alpha_1'\) in place of \(\alpha_0,\alpha_1\). The averages obey \(|\partial\bar{\mathbf U}^p-1|<2\alpha_0'(L^p\xi)^2\), and CMP 102 Proposition 9 then gives, on \(\tilde X^{-2}\),
\[
|\partial U_n(M^{\boldsymbol\cdot}(\mathbf U))-1|<2B_3\alpha_0'\xi^2,\qquad
|J_n(M^{\boldsymbol\cdot}(\mathbf U))|<2B_3\alpha_0'(L^n\xi)^2 .\tag{1.17}
\]
The account reports Balaban's conclusion: for \(\alpha_0'\) sufficiently small these estimates imply condition (iv) (CA-I 32613–32614). These primes are the small radii of this sufficient condition. They are not the larger operator radii of CMP 116 (CA-I 32666–32670).

**The use.** `4.8:prop-small-pairs` (CA-I 34058–34218) assumes: "for every \((p,Z)\in\mathfrak T_j(X)\) and every \(\mathfrak r\in\mathfrak R\), the estimate [CMP 109 (1.17)] holds at complex pairs, as stated on [p. 263]", with \(M/L\) and \(LB^{(109)}\) (CA-I 34067–34072). Its budget `4.8:eq-small-pairs-1` is \(\alpha_1'\le\alpha_1\), \(2B_3\alpha_0'\le\alpha_0\) (CA-I 34061–34062). Step 2 (CA-I 34148–34166) applies the hypothesis at \((\mu\alpha_0',\mu\alpha_1')\), \(\mu=L^{-(j-p)}\), and obtains `4.8:eq-small-pairs-3`:
\[
|\partial U_n^{\mathfrak r}(Z;M^{\boldsymbol\cdot}(\mathbf U))-1|<2B_3\mu\alpha_0'\xi_p^2,\qquad
|J_n^{\mathfrak r}(Z;M^{\boldsymbol\cdot}(\mathbf U))|<2B_3\mu\alpha_0'(L^n\xi_p)^2\quad\text{on }Z^{\wr p}.
\]
The proposition has a proof conditional on this hypothesis.

It reaches T0 through `4.19:prop-clause-zero` (CA-I 56419–56439). Item (g), the one-power hereditary class, reads it through membership (e) of `4.8:prop-class-reproduction` (CA-I 34241–34403). Item (c), the coupling increment, reads it through `4.7:not-true-pairs` (CA-I 29522–29605) and `4.7:prop-coupling-increment` (CA-I 32412–32491). One more direct use is the step "(i)–(iii) imply (iv)" of `5.2:lem-polydisc-containment` (CA-II 4381–4384). That step applies the sentence at the target radii themselves.

**Status there.** CA-III chapter 13, "Statements used without proof in this account", list (3, continued): "the inclusion sentence [CMP 109 (1.17)], read at complex pairs · Chapter 4 · cited as printed at its use site" (CA-III 111326–111327). CA-I 166588–166589, in the published inputs of clause (0) of Theorem 0 ("Inputs used by statement", CA-I 166552–166563): "[CMP 109 (1.17)], the inclusion sentence, read at complex pairs — printed without proof; cited as printed". CA-I 32703–32706 also explicitly records the complex sufficient condition as stated without proof and cited as printed.

**The outline's form.** SA Theorem 5(a) (SA 9746–9753) states the bound with \(K^\sharp(\alpha_0'+\alpha_1'^2)\) in place of \(2B_3\alpha_0'\), and the budget "once \(K^\sharp(\alpha_0'+\alpha_1'^2)\le\alpha_0\)". SA mechanism 8 (SA 9899–9911) sketches the proof. SA (ER8) (SA 6586–6630) states the small-exponential lemma "for sufficiently small \(a_0,a_1\)".

**Our labels.** L17 (`b109.md` §11.1) and Q119 (`b119.md`) are this statement at complex pairs, with \(2B_3\alpha_0'\) alone.

## 2. What is wrong with the original form, and the correction

**The original form is unproved at complex pairs.** It asks for a bound linear in the curvature radius \(\alpha_0'\) alone, for every \(\alpha_1'\le\alpha_1\), with no relation between the two radii. Balaban's derivation goes through CMP 102 Proposition 9. That proposition bounds the continued minimizer by the size of the datum increment. At a complex pair, the increment that \(A'\) adds to the averages is linear in \(\alpha_1'\). In level-\(n\) units, with \(s=L^n\xi_p\), the direct estimate is \(C(\alpha_0's^2+\alpha_1's)\) (`b109.md` (108)). The clause needs \(s^2\) times a constant. The quotient keeps \(\alpha_1'/s\), which is unbounded as \(p-n\) grows. So the derivation does not give (1.17) at complex pairs. We know no proof. The other routes tried here each stop at a named step (`l17.md`, two rounds; `b109.md` §§11.3–11.4; `b119.md` §7, three routes). No counterexample is known. The original form is open: neither proved nor refuted. This note does not claim that Balaban's sentence is false.

**The hypotheses allow \(\alpha_1'^2\gg\alpha_0'\).** Take \(U=1\) and a constant, commuting, complex potential in one direction (`b109.md` §11.4). Every plaquette equals \(1\). So (i)–(iii) hold for every \(\alpha_0'>0\) at fixed \(\alpha_1'\). (Its tower curvature is zero, so it refutes nothing.) Hence the corrected bound below is weaker than (1.17) on part of the domain, and the budget must carry the square.

**The correction.** Replace the hypothesis of `4.8:prop-small-pairs` by Theorem A, which is proved below. Replace `4.8:eq-small-pairs-1` by the budget (B1), which is the outline's own Theorem 5(a) budget. The fresh admissions in the true-pair and polydisc arguments have unit real factor and are supplied by Lemma C. The generic small-pairs supplier is replaced by Corollary B under (B1), and real curvature-only estimates may be retained under their original hypotheses. Other complex memberships, including minimizer families over nontrivial real bases, retain their separate nesting, inheritance, gauge-transport or increment suppliers. The search found no further fresh application of the original complex (1.17) requiring an unbudgeted non-seed pair; it did find additional complex memberships, excluded assertions and downstream constant uses.

## 3. The corrected statements

Notation is that of CA-I 32834–33070: towers \(\boldsymbol\Omega^{\mathfrak r}(Z)\) under the rules \(\mathfrak R=\{\mathfrak r_1,\mathfrak r_2\}\), the layered average \(M^{\boldsymbol\cdot}\), the current \(J_n^{\mathfrak r}\) in level-\(n\) units, the two-layer interior \(Z^{\wr p}\), the labels \(\mathfrak T_j(X)\), the tower clause \((\mathrm{iv})^{\mathfrak r}_{p,Z}[c]\) and the class \(U^{\Sigma^1}_j\). The constants and their order are in §7.

**Theorem A (corrected (1.17) at complex pairs).** There are constants \(K^\sharp\ge1\) and \(\bar\alpha_0',\bar\alpha_1'>0\) with the following property. They depend only on \(d=4\), \(N\), \(L\), \(\mathfrak M\), the flat constants F0, the averaging constants and the constants of the critical-orbit theorem. They do not depend on \(p,n,Z,\mathfrak r\), the torus, \(M\), \(B^{(109)}\), or \(\alpha_1'/\alpha_0'\). Let the gap number \(R_1\) obey R1 of §7, and let \(M\ge 2LR_1M_1\). Let \(p\ge1\), \(Z\in\mathbf D_{p-1}\), \(\mathfrak r\in\mathfrak R\), \(0<\alpha_0'\le\bar\alpha_0'\) and \(0<\alpha_1'\le\bar\alpha_1'\). Let \(\mathbf U=U'U\) on the bonds of \(Z\), with \(U\) \(G\)-valued, \(U'=e^{i\xi_pA'}\), and
\[
|\partial U-1|<\alpha_0'\xi_p^2,\quad |\partial\mathbf U-1|<\alpha_0'\xi_p^2,\quad |A'|,\ |\nabla^{\xi_p}_UA'|<\alpha_1'\quad\text{on }Z. \tag{A1}
\]
Then for \(n=1,\dots,p\) the analytic tower branch \(U_n^{\mathfrak r}(Z;M^{\boldsymbol\cdot}(\mathbf U))\) exists, and on \(Z^{\wr p}\)
\[
|\partial U_n^{\mathfrak r}(Z;M^{\boldsymbol\cdot}(\mathbf U))-1|<K^\sharp(\alpha_0'+\alpha_1'^2)\,\xi_p^2,\qquad
|J_n^{\mathfrak r}(Z;M^{\boldsymbol\cdot}(\mathbf U))|<K^\sharp(\alpha_0'+\alpha_1'^2)\,(L^n\xi_p)^2. \tag{A2}
\]
The same holds for \(U\) in place of \(\mathbf U\), with \(\alpha_1'=0\).

*Remarks.* (A1) is (1.11), (1.13) and the first inequality of (1.14) at level \(p\). The cube gauge (1.12) and the current bound \(|\mathbf J|<\gamma_0\) are not used (`p20-gate` F2); a consumer that has them loses nothing. For real data, \(U_n^{\mathfrak r}\) is the axial representative of the unique regular critical orbit. For complex data it is that representative's holomorphic continuation in the datum (§9, item 2). All bounds in (A1) use the complete read sets: local differences, currents and averages are read on their required stencils/carriers, including the outward rows.

**Corollary B (corrected `4.8:prop-small-pairs`).** In `4.8:prop-small-pairs`, replace the hypothesis at CA-I 34067–34072 by Theorem A, and `4.8:eq-small-pairs-1` by
\[
\alpha_1'\le\alpha_1,\qquad K^\sharp(\alpha_0'+\alpha_1'^2)\le\alpha_0,\qquad \alpha_0'\le\bar\alpha_0',\quad\alpha_1'\le\bar\alpha_1'. \tag{B1}
\]
Keep every other hypothesis. Then `4.8:eq-small-pairs-2` holds: \((\mathbf U,\mathbf J)\in U^{\Sigma^1}_j(X;\alpha_0,\alpha_1,\gamma_0)\). Its last paragraph, on the real minimal configurations of CMP 109 p. 263, holds with \(K^\sharp\alpha_0'\le\alpha_0\).

**Lemma C (seeds).** Let \(0<\alpha_0,\alpha_1\le1\) satisfy
\[
\alpha_0\le 4K^\sharp\bar\alpha_0',\qquad \alpha_1\le 2\bar\alpha_1'. \tag{C0}
\]
There is \(c_*>0\), depending only on \(K^\sharp\), \(d\) and \(N\), with the following property. Put \(r:=c_*\min(\alpha_0,\alpha_1)\). Let \(j\ge1\), \(X\in\mathbf D_{j-1}\), and let \(A\) be a \(\mathfrak g^c\)-valued bond field on \(X\) with \(|A|,|\nabla^{\xi_j}A|\le r\). Local differences, currents and averages use their complete required stencils/carriers, including the outward rows.

- (a) If \(|\mathbf J|\le r\), then \((e^{i\xi_jA},\mathbf J)\in U^{\Sigma^1}_j(X;\alpha_0,\alpha_1)\).
- (b) If \(|\partial^*\partial A|\le r\), then the true pair \((e^{i\xi_jA},J(e^{i\xi_jA}))\in U^{\Sigma^1}_j(X;\alpha_0,\alpha_1)\).
- (c) If \(X\in\mathbf D_j\), the pairs of (a) and (b) also lie in \(U^c_j(X,\alpha_0,\alpha_1)\).

The constant \(c_*\) does not depend on \(\alpha_0,\alpha_1\), \(j\), \(X\), the volume or the coupling. (C0) is the Stage-7 ceiling R2 of §7.

## 4. Proof of Theorem A

The inputs I1–I7 are stated where they are used; §8 lists each with its status. This is `b109.md` P19–P20, with the details recorded in `gates/p20-gate.md` §§2–4.

**Lemma 1 (real-point Taylor inequality; `b109.md` P19).** Let \(F\) be holomorphic on the ball of radius \(r\) of a complex normed space, with \(\|F\|\le H\) there, valued in a complex Banach space. Suppose \(w\mapsto w_R\) and \(w\mapsto w_I\), with \(w=w_R+iw_I\), have norm at most one. If \(t:=\|w\|\le r/2\), then
\[
\|F(w)\|\le\|F(w_R)\|+\|F(w_I)\|+\|F(0)\|+6Ht^2/r^2 .
\]

*Proof.* Write \(F(x)=F(0)+DF(0)x+R(x)\). On the complex line \(\zeta\mapsto F(\zeta x/\|x\|)\), \(|\zeta|<r\), Cauchy's estimate bounds the degree-\(m\) term of \(F\) at \(x\) by \(H(\|x\|/r)^m\). Summing over \(m\ge2\) gives \(\|R(x)\|\le H(\|x\|/r)^2/(1-\|x\|/r)\le2H\|x\|^2/r^2\) for \(\|x\|\le r/2\). This applies at \(x=w,w_R,w_I\), whose norms are at most \(t\). Since \(DF(0)\) is complex linear, \(DF(0)w=DF(0)w_R+iDF(0)w_I\). Hence
\[
F(w)=F(w_R)+iF(w_I)-iF(0)+R(w)-R(w_R)-iR(w_I),
\]
and the triangle inequality gives the claim. \(\square\)

**Setting.** Fix \(p,Z,\mathfrak r\) and \(1\le n\le p\). Put \(\eta:=\xi_p\), \(s:=L^n\xi_p=L^{n-p}\in(0,1]\) and \(\eta_n:=L^{-n}=\eta/s\). *Level-\(n\) units* rescale lengths by \(1/s\): the fine spacing becomes \(\eta_n\), a level-\(q\) block has length \(t_q:=L^{q-n}\le1\), and the top layer has scale \(1\). A field \(a\) at spacing \(\eta\) becomes \(w=sa\) at spacing \(\eta_n\), since \(e^{i\eta a}=e^{i\eta_nw}\). Its norm is \(\|w\|:=\max(\sup|w|,\sup|\nabla^{\eta_n}_Uw|)=\max(s|a|,s^2|\nabla^\eta_Ua|)\). By (A1), \(\|sA'\|\le s\alpha_1'\). Write \(U_r:=U\) and \(\mathbf U=e^{i\eta A'}U_r\). In level-\(n\) units the two bounds of (A2) read \(\eta_n^{-2}|\partial U_n^{\mathfrak r}-1|<K^\sharp(\alpha_0'+\alpha_1'^2)s^2\) and \(|J_n^{\mathfrak r}|<K^\sharp(\alpha_0'+\alpha_1'^2)s^2\).

**Step 1: the covariant curl of \(A'\) is small (SA 9905–9909).** Use the normalized Hilbert-Schmidt norm \(|X|=(\operatorname{tr}X^*X)^{1/2}\), with \(\operatorname{tr}1=1\), and reserve \(\|X\|_{\rm op}\) for operator norm. By CA-I 10306, \(|X|\le\|X\|_{\rm op}\le b|X|\), where \(b:=\sqrt N\). Let \(p\) be a plaquette with bonds \(b_1,b_2,b_3,b_4\) as in CA-I 10333–10345, so that \(\partial V(p)=V(b_1)V(b_2)V(b_3)^{-1}V(b_4)^{-1}\) and \((D_UA)(p)=\eta^{-1}(A_1+R(U_1)A_2-R(U_4)A_3-A_4)\). Move each exponential of \(\mathbf U\) to the first corner:
\[
\partial\mathbf U(p)=e^{X_1}e^{X_2}e^{X_3}e^{X_4}\,\partial U_r(p),\qquad
X_1=i\eta A_1',\ X_2=i\eta R(U_1)A_2',\ X_3=-i\eta R(U_1U_2U_3^{-1})A_3',\ X_4=-i\eta R(\partial U_r(p))A_4' .
\]
The transports are unitary, so \(\|X_\nu\|_{\rm op}\le b\eta|A'|\). The product's terms of total degree at least two sum in operator norm to at most \(e^{4b\eta|A'|}-1-4b\eta|A'|\le8b^2e^{4b}\eta^2|A'|^2\), using \(\eta\alpha_1'\le1\). Write \(P:=\partial U_r(p)\). The transports of \(A_3'\) and \(A_4'\) differ from those of \(D_{U_r}\) by \(R(P)\). For unitary \(P\), \(\|R(P)Y-Y\|_{\rm op}\le2\|P-1\|_{\rm op}\|Y\|_{\rm op}\le2b^2|P-1|\,|Y|\). The two discrepancies therefore cost at most \(4b^2\eta^3\alpha_0'\alpha_1'\). Hence
\[
\partial\mathbf U(p)\,\partial U_r(p)^{-1}=1+i\eta^2(D_{U_r}A')(p)+E,\qquad \|E\|_{\rm op}\le8b^2e^{4b}\eta^2\alpha_1'^2+4b^2\eta^3\alpha_0'\alpha_1'. \tag{4.1}
\]
Since \(\partial U_r(p)\) is unitary, \(\|\partial\mathbf U\,\partial U_r^{-1}-1\|_{\rm op}=\|\partial\mathbf U-\partial U_r\|_{\rm op}<2b\alpha_0'\eta^2\) by (A1). With (4.1) and \(|E|\le\|E\|_{\rm op}\), choose a larger fixed \(C_s=C_s(d,N)\) to obtain
\[
|D_{U_r}A'|\le C_s(\alpha_0'+\alpha_1'^2). \tag{4.2}
\]
Write \(A'=A_R+iA_I\) with \(A_R,A_I\) Hermitian. Because \(U_r\) is unitary, \(R(U_r)\) commutes with the adjoint, so \(D_{U_r}\) and \(\nabla_{U_r}\) commute with both projections. So \(|D_{U_r}A_R|,|D_{U_r}A_I|\le|D_{U_r}A'|\), and \(|A_R|,|A_I|,|\nabla_{U_r}A_R|,|\nabla_{U_r}A_I|<\alpha_1'\). Apply (4.1) to \(A_R\) and to \(A_I\). The real fields \(U_R:=e^{i\eta A_R}U_r\) and \(U_I:=e^{i\eta A_I}U_r\) are \(G\)-valued, and
\[
|\partial U_R-1|,\ |\partial U_I-1|\le C_s(\alpha_0'+\alpha_1'^2)\,\eta^2 . \tag{4.3}
\]
This uses only \(|A'|<\alpha_1'\) and the two curvature bounds, with no bound on \(\nabla A'\). The same enlarged \(C_s(d,N)\) covers (4.2)–(4.3); no depth, mesh, volume or radius-ratio dependence is introduced.

**Step 2: the datum increment is linear in \(\|w\|\), uniformly in depth.** For a complex field \(w\) define \(B(w)\) on the data sets of the tower by \(M^{\boldsymbol\cdot}(e^{i\eta_nw}U_r)=e^{iB(w)}M^{\boldsymbol\cdot}(U_r)\).

*I1 (averaging of a complex perturbation; CMP 98).* There are \(r_4>0\) and \(C_4\), depending on \(L\), \(\mathfrak M\) and the averaging constants only, such that \(B\) is holomorphic on \(\{\|w\|<r_4\}\) and \(\sup|B(w)|\le C_4\|w\|\) there, for every real \(U_r\) with \(|\partial U_r-1|\le\alpha_0'\eta^2\), \(\alpha_0'\le\bar\alpha_0'\).

The depth count is this. The straightened relative angles \(b_q\) of the level-\(q\) average obey the one-step inequality (`b109.md` (107); `a1-balaban.md` §3.5, actual-mean form §7.6)
\[
b_{q+1}\le L(1+C\alpha_0'\,t_q^2)\,b_q+C_Lb_q^2,\qquad b_0\le\eta_n|w| .
\]
Put \(\beta_q:=b_q/t_q\), so \(\beta_0\le|w|\). While \(\beta_q\le2|w|\), \(\beta_{q+1}\le\beta_q(1+C\alpha_0't_q^2+2C_L'|w|t_q)\). Since \(\sum_qt_q^2\le(1-L^{-2})^{-1}\) and \(\sum_qt_q\le(1-L^{-1})^{-1}\), the product of these factors is at most \(2\) once \(\alpha_0'\) and \(|w|\) are below fixed ceilings. By induction on \(q\) (first exit), \(\beta_q\le2|w|\) for all \(q\le n\). The endpoint (node) factors obey the same summable first-power bound (`b109.md` P15 (72), (74)–(77); `a1-balaban.md` (7.14)). So \(\sup|B(w)|\le C_4\|w\|\), with no factor depending on \(n\) or \(p\). Holomorphy holds because \(B\) is a finite composition of products, inverses and convergent logarithm series. A recursion on the plain angles with coefficient \(L\) would be false (endpoint sums of order \(dL\)); it is not used (`p20-gate` §3).

**Step 3: one holomorphic function and its crude bound.**

*I2 (holomorphic continuation; CMP 102 §G; `a1-balaban.md` §9.1).* There are \(r_B>0\), \(\varepsilon_{\rm adm}>0\) and \(C_2\) with the following property. Let \(V_0\) be a real layered datum of datum radius at most \(\varepsilon_{\rm adm}/2\). Then \(B\mapsto\Phi_{V_0}(B)\), the axial representative at the datum \(e^{iB}V_0\), is holomorphic on \(\{\sup|B|<r_B\}\). In level-\(n\) units, at every plaquette \(p\) and bond \(b\) of the top layer, \(\eta_n^{-2}|\partial\Phi_{V_0}(B)(p)-1|\) and \(|J(\Phi_{V_0}(B))(b)|\) are at most \(C_2(\varepsilon_{\rm adm}+\sup|B|)\) ((9.2), with the Euler-equation bound (9.1) for the current). For real \(B\) it is the representative of I3 at that datum.

Put \(r:=\min\{r_4,\ r_B/(2C_4)\}\) and \(V_0:=M^{\boldsymbol\cdot}(U_r)\). Fix one top-layer plaquette \(p\), or one top-layer bond \(b\). Define on \(\{\|w\|<r\}\)
\[
F(w):=\eta_n^{-2}\bigl(\partial\Phi_{V_0}(B(w))(p)-1\bigr)\quad\text{or}\quad F(w):=J\bigl(\Phi_{V_0}(B(w))\bigr)(b).
\]
By Steps 2–3, \(F\) is holomorphic and \(\|F\|\le H:=C_2(\varepsilon_{\rm adm}+r_B)\). This bound is crude; it has no factor \(\alpha_0'\). By definition of the analytic branch, \(U_n^{\mathfrak r}(Z;M^{\boldsymbol\cdot}(\mathbf U))=\Phi_{V_0}(B(sA'))\). So \(F(sA')\) is the quantity that (A2) bounds.

**Step 4: the three real points.**

*I3 (critical-orbit theorem at real data; CMP 102 Theorem 1; `a1-balaban.md` (8.2)).* There is \(B_1\) such that, for a real layered datum of radius \(\varepsilon\le\varepsilon_{\rm adm}\), on a tower whose gap obeys R1 of §7, the default problem has one regular critical orbit. In level-\(n\) units, at top-layer elements, its axial representative has \(\eta_n^{-2}|\partial U(p)-1|\le B_1\varepsilon\) and \(|J(U)(b)|\le B_1\varepsilon\). The bound is linear in \(\varepsilon\), and \(B_1\) is independent of depth, volume and datum.

*I4 (curvature of averages; CMP 98 (48); `a1-balaban.md` (3.6), §7.1).* If a real field has \(|\partial V-1|\le\delta\eta^2\) on \(Z\), with \(\delta\le\alpha_*\), then its level-\(q\) averages have plaquettes at most \(2\delta s^2t_q^2\), and \(2L^2\delta s^2t_q^2\) at a seam. Indeed (3.6) reads \(v_{m+1}\le L^2v_m+C(L^2v_m)^2\), and \(\delta\eta^2=\delta s^2L^{-2n}\). So the datum \(M^{\boldsymbol\cdot}(V)\) has radius at most \(C_3\delta s^2\), with \(C_3=2L^2\).

Apply I4 to \(U_r\), \(U_R\) and \(U_I\), with \(\delta=\alpha_0'\) and, by (4.3), \(\delta=C_s(\alpha_0'+\alpha_1'^2)\). The ceilings of §7 keep each datum radius below \(\varepsilon_{\rm adm}/2\). At \(w=sA_R\), the increment \(B(sA_R)\) is real, since \(e^{i\eta A_R}U_r\) is real; and \(\sup|B(sA_R)|\le C_4s\alpha_1'<r_B\). By orbit uniqueness and the unique axial gauge, \(\Phi_{V_0}(B(sA_R))\) is the real representative at the datum \(M^{\boldsymbol\cdot}(U_R)\). The same holds at \(sA_I\) and at \(0\). I3 then gives
\[
\|F(0)\|,\ \|F(sA_R)\|,\ \|F(sA_I)\|\le C_1(\alpha_0'+\alpha_1'^2)\,s^2,\qquad C_1:=B_1C_3\max\{1,C_s\}. \tag{4.4}
\]
Curvature and current norms are invariant under unitary gauges, so the choice of representative does not matter here.

**Step 5: conclusion.** The projections \(w\mapsto w_R,w_I\) have norm at most one for \(\|\cdot\|\): the adjoint preserves the matrix norm, and \(\nabla_{U_r}\) commutes with it. Here \((sA')_R=sA_R\) and \((sA')_I=sA_I\), and \(t:=\|sA'\|\le s\alpha_1'\le r/2\) by the ceiling \(\alpha_1'\le r/2\). Lemma 1 and (4.4) give
\[
\|F(sA')\|\le3C_1(\alpha_0'+\alpha_1'^2)s^2+6Hs^2\alpha_1'^2/r^2\le K(\alpha_0'+\alpha_1'^2)\,s^2,\qquad K:=3C_1+6H/r^2 .
\]
For the current this is the second bound of (A2) with \(K\). For the plaquette, multiply by \(\eta_n^2\) and use \(\eta_n^2s^2=\eta^2\): this is the first bound. Put \(K^\sharp:=2\max\{K,1\}\). Since \(\alpha_0'>0\), the bounds are strict with \(K^\sharp\). The constant \(K\) is built from \(B_1,C_3,C_s,C_2,\varepsilon_{\rm adm},r_B,r_4,C_4\). None of these depends on \(\alpha_1'/\alpha_0'\), \(p,n,Z,\mathfrak r\), the torus, \(M\) or \(B^{(109)}\).

**Step 6: the interior, and the real factor.** The bounds of Steps 3–5 hold at top-layer elements of \(\Omega_n^{\mathfrak r}(Z)\). By `4.8:eq-tower-rules-b` (CA-I 32921–32929), every point of \(Z\) at distance more than \(R_1M_1L^n\) steps from \(Z^c\) lies in \(\Omega_n^{\mathfrak r}(Z)\). A point of \(Z^{\wr p}\) lies at least two \(\pi_{p-1}\)-cubes, that is \(2ML^{p-1}\ge4R_1M_1L^p\ge4R_1M_1L^n\) steps, from \(Z^c\), by \(M\ge2LR_1M_1\). So \(Z^{\wr p}\), with the one-step stencils of the plaquettes and of the current, lies in the top layer. This is CA-I 34177–34189, for both rules. Finally, \(A'=0\) gives \(\mathbf U=U_r\), and the bound \(K^\sharp\alpha_0'\). \(\square\)

## 5. Proofs of Corollary B and Lemma C

**Proof of Corollary B.** Fix \((p,Z)\in\mathfrak T_j(X)\) and \(\mathfrak r\in\mathfrak R\), and put \(\mu:=L^{-(j-p)}\le1\). Step 1 of CA-I (34107–34145) is unchanged. By the change of units `4.8:eq-restriction-units-a` (I6), the pair obeys (A1) at level \(p\) on \(Z\) with the radii \((\mu\alpha_0',\mu\alpha_1')\): \(\alpha_0'\xi_j^2=\mu^2\alpha_0'\xi_p^2\le\mu\alpha_0'\xi_p^2\), and \(A'^\flat=\mu A'\) has \(|A'^\flat|=\mu|A'|\), \(|\nabla^{\xi_p}A'^\flat|=\mu^2|\nabla^{\xi_j}A'|\le\mu|\nabla^{\xi_j}A'|\). By (B1) and \(\mu\le1\), \(\mu\alpha_i'\le\bar\alpha_i'\). Theorem A at these radii replaces Step 2: on \(Z^{\wr p}\) the two bounds hold with the coefficient
\[
K^\sharp(\mu\alpha_0'+\mu^2\alpha_1'^2)\le\mu\,K^\sharp(\alpha_0'+\alpha_1'^2)\le\mu\alpha_0=\alpha_0L^{-(j-p)} . \tag{5.1}
\]
For \(U\), Theorem A gives \(K^\sharp\mu\alpha_0'\le\mu\alpha_0\) (Step 3). The geometry of Step 4 is part of Theorem A. So \((\mathrm{iv})^{\mathfrak r}_{p,Z}[\alpha_0L^{-(j-p)}]\) holds at every label and rule; this is \((\mathrm{iv})^{\Sigma^1}\). Conditions (i)–(iii) hold at \((\alpha_0,\alpha_1,\gamma_0)\) because \(\alpha_0'\le K^\sharp\alpha_0'\le\alpha_0\) and \(\alpha_1'\le\alpha_1\). Hence `4.8:eq-small-pairs-2`. \(\square\)

The new term \(\mu^2\alpha_1'^2\) is at most \(\mu\alpha_1'^2\). So the square has the one-power scaling of the class. The account's remark at CA-I 34211–34218 makes the same observation for a linear \(\alpha_1'\) term. What needed proof was the budget, not the scaling.

**Proof of Lemma C.** Norms on matrices are those of CA-I 10306; the operator norm is at most \(b:=\sqrt N\) times the normalized Hilbert-Schmidt norm used there.

*(C1) Plaquettes of a small exponential.* Let \(\xi\le1\), \(r\le1\) and \(|A|,|\nabla^\xi A|\le r\). With real factor \(1\), \(\partial e^{i\xi A}(p)=e^{i\xi A_1}e^{i\xi A_2}e^{-i\xi A_3}e^{-i\xi A_4}\). Its linear term is \(i\xi(A_1+A_2-A_3-A_4)=i\xi^2(D_1A)(p)\), and \(|D_1A|\le2\sup|\nabla^\xi A|\le2r\). The other terms are at most \(e^{4b\xi r}-1-4b\xi r\le8b^2\xi^2r^2e^{4b\xi r}\), which holds term by term in the exponential series. Since \(\xi,r\le1\),
\[
|\partial e^{i\xi A}-1|\le D\,r\,\xi^2,\qquad D:=\max\{2b+8b^2e^{4b},\,1+c_F\}. \tag{5.2}
\]
This also holds for complex \(A\). No inverse power of the spacing remains.

*(C2) The current of a true pair.* Apply `4.4:lem-current-remainder` (i) (I7) with \(U_0=1\), \(\mathsf c=0\) and \(\ell=1\). It gives \(|F(1,A)|\le c_F\max(|A|,|\nabla A|)^2\le c_Fr^2\). By `4.4:eq-current-remainder-1`, \(J(e^{i\xi A})=D_1^*D_1A+F(1,A)\), since \(J(1)=0\). If also \(|\partial^*\partial A|\le r\), where \(\partial^*\partial=D_1^*D_1\), then \(|J(e^{i\xi A})|\le(1+c_F)r\le Dr\).

*Choice.* Put \(c_*:=\min\{1/4,(16K^\sharp D)^{-1}\}\), and
\[
\alpha_0':=\frac{\alpha_0}{4K^\sharp},\qquad \alpha_1':=\min\Bigl\{\frac{\alpha_1}{2},\ \Bigl(\frac{\alpha_0}{4K^\sharp}\Bigr)^{1/2}\Bigr\}. \tag{5.3}
\]
Then (B1) holds. Indeed \(\alpha_1'\le\alpha_1\), and \(K^\sharp(\alpha_0'+\alpha_1'^2)\le K^\sharp\cdot2\alpha_0/(4K^\sharp)=\alpha_0/2\). By (C0), \(\alpha_0'\le\bar\alpha_0'\) and \(\alpha_1'\le\alpha_1/2\le\bar\alpha_1'\).

*Conditions (i)–(iii) at \((\alpha_0',\alpha_1',\alpha_0)\).* Take the decomposition \(U=1\), \(U'=e^{i\xi_jA}\). (i) holds: \(\partial1=1\), and the cube gauge of (1.12) is the trivial one, with potential \(0\). (ii) holds: \(r\le\alpha_1/4<\alpha_1/2\), and \(r^2\le c_*^2\alpha_0^2\le c_*\alpha_0\le\alpha_0/(16K^\sharp)<\alpha_0/(4K^\sharp)\), using \(\alpha_0\le1\). So \(r<\alpha_1'\). (iii) holds: by (5.2), \(|\partial e^{i\xi_jA}-1|\le Dr\xi_j^2\le Dc_*\alpha_0\xi_j^2\le\alpha_0'\xi_j^2/4\). In case (a), \(|\mathbf J|\le r\le\alpha_0/4<\alpha_0\). In case (b), by (C2), \(|J(e^{i\xi_jA})|\le Dr\le\alpha_0/(16K^\sharp)<\alpha_0\).

Corollary B at the radii (5.3) now gives (a) and (b), with \(\gamma_0=\alpha_0\).

*(c).* Let \(X\in\mathbf D_j\). The walls of \(\pi_j\) are walls of \(\pi_{j-1}\) (CA-I 32724–32730), so \(X\in\mathbf D_{j-1}\). Conditions (i)–(iii) of \(U^c_j(X,\alpha_0,\alpha_1)\) hold, by the last paragraph and monotonicity. Condition (iv) of \(U^c_j\) reads the tower of rule \(\mathfrak r_1\) at level \(j\) (CA-I 32559–32563, 32871–32875). Theorem A at \(p=j\), \(Z=X\), \(\mathfrak r=\mathfrak r_1\) and the radii (5.3) gives its bounds with coefficient \(\alpha_0/2<\alpha_0\) on \(X^{\wr j}\). For \(U=1\) the bounds are trivial. Finally \(\tilde X^{-2}\subset X^{\wr j}\). A point of \(\tilde X^{-2}\) lies in a \(\pi_j\)-cube \(Q\) with \(\tilde Q^2\subset X\). Its \(\pi_{j-1}\)-cube \(\square\) lies in \(Q\), and \(\tilde\square^2\) lies within \(2ML^{j-1}\le ML^j\) steps of \(Q\), so inside \(\tilde Q^1\subset X\). \(\square\)

**The constant \(c_T\) in the account.** In `4.7:eq-true-pairs-a` (CA-I 29529–29535), choose
\[
c_T:=\min\{c_T^\circ,\ 1/8,\ 1/C_{IV},\ c_*\}, \tag{5.4}
\]
once, and use it at every occurrence of the true-pair/polydisc constant. Unrelated constants with the same spelling are not reset (§6). The norm \(N_j(\mathsf Z)\) of `4.7:eq-true-pairs-1` is the value, first difference and second-order norm of \(A:=\ell_j\mathsf Z\) at spacing \(\xi_j\). So \(N_j(\mathsf Z)\le c_Tr_j\), \(r_j=\min(\alpha_{0,j},\alpha_{1,j})\), gives the hypotheses of Lemma C (b) and (c) at the running radii. The running radii obey (C0), since \(\alpha_{i,j}\le\alpha_i\) (CA-I 1667–1669) and \(\alpha_i\) obeys R2. This proves clauses (a) and (b) of `4.7:not-true-pairs` and replaces its free-prime step (CA-I 29557–29589). It also replaces the step "(i)–(iii) imply (iv)" of `5.2:lem-polydisc-containment` (CA-II 4381–4384), by Lemma C (a) and (c). That lemma has the same radius formula \(\mathfrak r_j=c_T\min(\alpha_{0,j},\alpha_{1,j})\) with one possibly smaller fixed \(c_T\). Its ratio \(\mathfrak t_j^{-2}=(\min\{\alpha_0,\alpha_1\}/\min\{C_0,C_1\})^2x_j(\log x_j)^{-2q}\) is unchanged: \(c_T\) cancels in this ratio only.

A smaller \(c_T\) changes fixed constants and radii, including \(C_\vartheta\) (CA-I 30028–30056), \(\widetilde K\) (29828–29865), \(C'\) (32284), \(C_\beta\) (CA-II 4721), \(C_{\mathfrak e}\) (CA-II 97071), \(C_\Pi\) (CA-III 90592), their descendants, and the Cauchy radius \(\xi_i^3c_Tr_i/(8d)\) of the coupling extraction (CA-I 32452–32491). For example,
\[
C_\beta=4B_3^2CS(\delta_1)\mathfrak r_\circ^{-2},\qquad
\mathfrak e_Q=\frac{C_{\mathfrak a}B_3M_Q}{c''c_T}\varepsilon',\qquad
C_{\mathfrak e}=C_wB_3\max\{2,C_{\mathfrak a}M_Q/(c''c_T)\},
\]
at CA-II 4721, 96412 and 97071, while \(C_\Pi=C_\beta\mathfrak r_\circ^2/(c_TC_*)^2\) (CA-III 90592) still depends on \(c_T\). The cancellation at CA-II 96444–96468 removes running field amplitudes, not \(c_T\). Fix the positive \(c_T\) and its dependent constants before the final \(\gamma\) choice (CA-I 32405–32409; CA-II 94857–94865). Fixed extraction and response constants may increase, requiring a smaller final coupling ceiling. Since \(q>p_0\), \(\vartheta(\gamma)\to0\) still supplies a one-sided small-coupling ceiling (CA-I 30051–30105). The powers of the coupling and logarithms are unchanged; this is not cancellation of all constants.

## 6. Every use of (1.17) in the account

The list, corrected by `gates/wu-l17-gate.md` §3, combines the inventory of `l17c.md` §6 with the referee's own search (`l17c-gate`, findings 2 and "Consumer list"): every `1.17`, the labels of the displays, every `c_T`, every `2B_3` and `B_3^2`, and every "(i)–(iii) imply (iv)", over CA-I, II and III. CMP 109 (1.17) occurs at 31 lines of CA-I and at CA-III 111326. Every other `1.17` is CMP 116, 122a, 122b or a decimal.

| Use | Pair | Supplied by |
|---|---|---|
| CA-I 34058–34218, `4.8:prop-small-pairs` | the supplier slot | Corollary B |
| CA-I 34811–34830, amplitude ceilings | the entry \(2B_3\alpha_0'\le\alpha_0\) at 34819 | replace by (B1) |
| CA-I 32599–32623, the sufficient condition | generic statement | replace the complex implication by Theorem A with (B1); retain the real \(2B_3\alpha_0'\) bound as a separate published input |
| CA-I 29522–29605, `4.7:not-true-pairs` | true pairs, \(U=1\), ball \(c_Tr_j\) | Lemma C (b), (c) with (5.4) |
| CA-I 32412–32500, `4.7:prop-coupling-increment` | polydisc of radius \(\xi^3c_Tr/(8d)\), through true pairs | the same |
| CA-I 34241–34403, `4.8:prop-class-reproduction`, membership (e); CA-I 34718, 34738–34741 | unit, true and small pairs; real backgrounds; orbit-form inputs | Lemma C for seeds; Corollary B under (B1) for small pairs; real estimates under their original hypotheses; separate orbit-form suppliers retained |
| CA-II 4333–4398, `5.2:lem-polydisc-containment` | \(e^{i\xi\mathcal A}\), independent current, ball \(\mathfrak r_j\) | Lemma C (a), (c) with (5.4) |
| CA-II 4599–4727, 94811–97192; CA-III 90585–90624 | through \(\mathfrak r_j\) | the same form of polydisc radius; the ratio \(\mathfrak t_j\) is unchanged; fixed extraction and response constants may increase |

The fresh admissions in the true-pair and polydisc arguments have unit real factor and are supplied by Lemma C. The generic small-pairs supplier is replaced by Corollary B under (B1), and real curvature-only estimates may be retained under their original hypotheses. Other complex memberships, including minimizer families over nontrivial real bases, retain their separate nesting, inheritance, gauge-transport or increment suppliers. The search found no further fresh application of the original complex (1.17) requiring an unbudgeted non-seed pair; it did find additional complex memberships, excluded assertions and downstream constant uses.

**Uses at real pairs** (\(\alpha_1'=0\); Theorem A gives \(K^\sharp\alpha_0'\), and the real bound \(2B_3\alpha_0'\) of CMP 102 Proposition 9 may be kept): the minimal configurations of CMP 109 p. 263 (CA-I 34087–34089, 34205–34208); CA-I 10750–10754, 36806–36905, 42198–42340, 43590–44380, 128551–128930; CA-II 99767–99813. The multilevel frozen-background conclusion at CA-I 128551–128930 retains the uniform-in-strata current hypothesis (b), 128807–128817 and 128923–128930. The reblocking proposition at CA-I 44127–44129 remains expressly incomplete at its marked step.

**The other memberships of class reproduction keep their own suppliers** (`l17c.md` §5, checked in `l17c-gate`). Near incoming pair: the assumed hereditary clause. Near product: the nesting identity of `4.13:lem-minimizer-unique` (CA-I 45162, proof outstanding there; our `mu.md`). Far incoming pair: restriction. Far product: the increment estimate, with its \(\alpha_2\) ceiling. Domain restriction: monotonicity. None of them applies (1.17) at the full target radii. The own-radius gauge of `4.13:lem-own-constant` (CA-I 45203, proof outstanding there; our `oc.md`) is met without (A2): seeds have \(U=1\), and real backgrounds use real CMP 98 averaging and CMP 102 gauges.

**Matches that are not fresh uses.** The larger primed operator radii of CMP 116 (CA-I 4384–4554, 5822–5908 and others); block-average and literal-frame curvature assertions (CA-I 13198–13255, 17523–17564, 18305–18346); straddling and shell clauses (10028–10092, 120111–120334); passages that name the (1.17) route and do not take it (15918–15961, 20150–20185, 34886–35045); and the units definition at 154551–154588. CA-I 117207–117328 supplies B'-ball/entry-conversion ceilings; 121282–121350 is a near-pair chain mentioning an alternative starting route. CA-I 154825–154863 excludes the general complex assertion; 155490–155511 rejects a linear-datum route. Their separate source inputs remain; this note supplies none of them.

**Other complex memberships.** CA-I 155275–155438 is a complex minimizer argument over a real base, not a real pair. At 155310–155316, \(W=e^{i\eta\mathcal H}U_0\) is complex. The real \(U_0\) supplies the real-factor conditions; 155388–155426 obtains the tower bounds through a separate nesting input. The \(2B_3\) comparison at 155421 is arithmetic after those bounds; Lemma C is not its supplier. CA-I 155940–156060 and 156177–156189 treat a complex minimizer family with unit base. Its clause (iv) uses N1 nesting at 156008–156033; the later cutoff-free constant calculation uses the same auxiliary radius. Nesting remains a separate premise. CA-I 35963–35971 transports a complex pair over an existing real factor with a \(c_T\)-sized perturbation. It preserves the tower condition because the relevant configuration is unchanged; this is not fresh admission by (1.17). The box-minimizer extension and nesting hypotheses in CA-II 94811–97192, including 96010–96026 and the core-estimate hypothesis at 96276 onward, also remain separate.

**Additional excluded assertions and separate inputs.** CA-I 40189–40212, especially 40194–40197, names smaller (i)–(iii) implying (iv) as a separate input; the openness argument neither derives nor uses it. CA-I 42545–42640 explains why proposed weakenings do not give the own-radius clause, and 42670–42688 declines an assertion about (1.17). Theorem A supplies neither excluded conclusion. Kernel membership at CA-I 144962–145024 and 145167–145182 reads separate CMP 109 regularity, with bounds containing \(2B_3\). Window minimizers and scale/rim thresholds at CA-I 148810–148832, 148885–148903, 149809–149888, 150005–150055, 150745–150755 and 151807–151919 retain their regularity, restriction, minimizer and response hypotheses. Theorem A does not supply that window machinery.

**Additional symbol and threshold records.** Complex-background and cutoff-free radius constants at CA-I 153616–153622, 154875–154918, 154959–154970, 155139–155150 and 156425–156447, and auxiliary coupling thresholds at 163946–163970, 164015–164026 and 164136–164183, use \(2B_3\) in definitions, substitutions and comparisons. They are not fresh applications of the sufficient-condition sentence; their background and threshold hypotheses remain. Other occurrences include near-case gauge ceilings (CA-I 33704–33723), real cube-gauge estimates and floors (36519–36546, 36678–36705, 37914–37943), real reblocking, datum-radius and running-constant comparisons, and CMP 102 or CMP 109 (3.38) estimates. CA-II includes remainder constants (43094–43139), the decimal \(1.2B_3\) (44456, 44514), base regularity (86147–86161), real regularity with explicit nesting (95984–96138), a local real minimizer (109508–109517), and a separately assumed support/comparison energy argument (119774–119847). CA-III 34805–34814, 35023–35038, 35364–35370, 36974–36999 and 37123–37140 concern real CMP 102 regularity, averaging and refinement. These do not supply general complex (1.17); unrelated large-field bounds also contain \(B_3^2\).

**Additional downstream \(c_T\) and radius consumers.** The downstream uses, including CA-I 29458–29466, 29640–29642, 29982–30012, 30562–30573, 31304–31457, 31605–31664, 31709, 31740–31756, 31833–31874 and 32242–32409, concern shift/simple-case radii, total-field ratios, fundamental shares, counterterm leftovers, smallness ceilings and extraction constants. Shrinking the true-pair/polydisc \(c_T\) can enlarge fixed constants or require a smaller final coupling ceiling. The downstream radius consumers also include the Cauchy second-derivative/kernel estimates at CA-III 81024–81032, 81041–81052, 81118 and 81155–81159, with \(4B_3^2\mathfrak r_j^{-2}\), in addition to the extraction record at 90585–90624.

**Unrelated \(c_T\) homonyms.** CA-I 70548 and 75590–75665 use term constants; 119041, 119386, 119406 and 124591 use a size constant; CA-II 81373 uses a moment-recursion constant. None is reset by (5.4).

## 7. Order of constants, and the two repairs

The following is a partial dependency order for this argument. It preserves the account's earlier floors and stages; it is not a replacement for its entire order of choice. Early block/parametrix sizes are distinct from the late cube size \(M\).

\(L\); \(\mathfrak M\) and the early block/parametrix choices; the F0, fixed decay/blocking and localization constants needed for R1; the Stage 5 choice of \(M_1\) and then \(R_1\) described below; the remaining early critical-orbit and averaging constants \(B_1,r_B,\varepsilon_{\rm adm},r_4,C_4,\alpha_*\); \(K^\sharp\), then \(\bar\alpha_1'\), then \(\bar\alpha_0'\); \(B^{(109)}\) before \(M\ge2LR_1M_1\) (CA-I 4434–4437); Stage 7 with **R2**; \(\alpha_2\); \(c_T\) by (5.4) and the constants built from it; the final \(\gamma\) ceiling after their inputs. All prior floors remain. The auxiliary radii (5.3) are chosen at each use, after the target radii.

The ceilings of Theorem A are \(\bar\alpha_1'\le r/2\), and \(C_3\max\{1,C_s\}(\bar\alpha_0'+\bar\alpha_1'^2)\le\min\{\alpha_*,\varepsilon_{\rm adm}/2\}\) together with the smallness used in Step 2. The square enters only as a ceiling on \(\bar\alpha_1'\). No relation between \(\alpha_0'\) and \(\alpha_1'\) is imposed (`p20-gate` §4). If \(K^\sharp\) were found to depend on \(M\) or \(B^{(109)}\), nothing would break: every use of \(K^\sharp\), through (B1), \(c_*\) and \(c_T\), comes after those letters (`l17c-gate` finding 4).

**R1. The gap number (`p20-gate` F1).** I2 and I3 hold on towers whose gap is at least a number fixed after the localization length of `a1-balaban.md` (6.3)–(6.5). By `a1-balaban-gate` D2 the gap must exceed four lengths, among them about \(6L\) times that localization length; all four read only \(L\), \(\mathfrak M\) and the F0 constants. Call the resulting gap number, in units of \(\mathfrak ML^q\), \(R_{D2}\). Rule \(\mathfrak r_1\) has gap \(R_1\mathfrak ML^q\) (CA-I 32877–32879). Rule \(\mathfrak r_2\) has gap \(M_1L^q\ge R_1\mathfrak ML^q\). So choose the account's \(R_1\ge R_{D2}\). The account only asks that \(R_1\) be "sufficiently large" (CA-I 32847–32851); R1 names one floor it must meet. The letter \(R_1\) denotes two constants here: `a1-balaban`'s localization factor and the account's gap number. Read as one constant, D2 cannot hold for \(\mathfrak r_1\).

*Stage 5 compatibility choice (repaired after `wu-l17-gate` §4).* The account lists \(R_1\) after \(M_1\), "chosen upward" (CA-I 1508–1511, 2063–2064), while CA-I 32851 requires \(R_1\le M_1/\mathfrak M\). After the fixed early estimates, define \(R_{\rm req}\) as the least power of \(L\) satisfying all earlier floors for \(R_1\), including \(R_1\ge L\), the kernel/summation floors (CA-I 13415–13417), and the D2 floor. Meet strict floors strictly. Their coefficients are fixed decay and blocking constants, not late amplitudes. Choose the Stage 5 power \(M_1\) to obey its old floors and
\[
M_1\ge\mathfrak M R_{\rm req}.
\]
Then choose \(R_1=R_{\rm req}\) at its recorded later position, or a power satisfying
\[
R_{\rm req}\le R_1\le M_1/\mathfrak M.
\]
This meets CA-I 32847–32851 and both tower-rule gaps. It does not permit arbitrary later increases of \(R_1\) with \(M_1\) frozen. Fix the remaining early constants, then \(B^{(109)}\) and the late \(M\) in that order. Impose R2 at Stage 7, then choose \(c_T\) and the final coupling ceiling after their inputs. Increasing late \(M\) does not force an increase of \(R_1\). This compatible choice has no cycle for the present argument; it does not establish the separately assumed uniform local-background operator bounds or the account's entire global order theorem.

**R2. The Stage-7 ceiling (`l17c-gate` finding 1).** Lemma C needs \(\alpha_0'=\alpha_0/(4K^\sharp)\le\bar\alpha_0'\) and \(\alpha_1'\le\alpha_1/2\le\bar\alpha_1'\). So add to the radii of Stage 7 (CA-I 1614–1629) the ceilings
\[
\alpha_0\le4K^\sharp\bar\alpha_0',\qquad \alpha_1\le2\bar\alpha_1'.
\]
Their letters are fixed before the radii, and the radii are chosen downward after \((L,B^{(109)},M)\) (CA-I 34811–34830). So there is no cycle. The running radii inherit R2 through \(\alpha_{i,j}\le\alpha_i\) (CA-I 1667–1669). Without R2, the auxiliary value \(\alpha_0/(4K^\sharp)\) need not lie below the available Theorem A ceiling, so this proof of the lemma over the advertised target-radius range is not justified. R2 supplies the missing domain restriction; no counterexample to seed inclusion is asserted. The outline states the same lemma "for sufficiently small \(a_0,a_1\)" (SA (ER8), 6586–6590).

**No square ceiling on the absolute radii.** The account chooses \(\alpha_1\) before \(\alpha_0\) (CA-I 1614–1615). A ceiling \(\alpha_1^2\le c\,\alpha_0\) would be a floor on the later \(\alpha_0\), so it is not used. The square is carried by the auxiliary radii (5.3) instead. A square ceiling on fixed fractions of the running radii would be an allowed Stage-8 \(\gamma\) ceiling, since \(\alpha_{1,n}^2/\alpha_{0,n}=(C_1^2/C_0)x_n^{-1/2}(\log x_n)^q\to0\) (`l17c.md` (15)); it is not needed.

## 8. Inputs, with their status in their account and in ours

"Checked" means one line-by-line reading by one other model, first failing step none. It is not an audit, and a checked result is still an implication from its named inputs.

| Input | Their account | Ours |
|---|---|---|
| Lemma 1, real-point Taylor inequality | SA mechanism 8 (SA 9899–9905), sketched, constant unnamed | `b109.md` P19 (Codex); checked by Claude (`p20-gate` §2) |
| Theorem A | not stated; the account assumes the stronger (1.17) (CA-I 34067–34072). Outline: SA Theorem 5(a), 9746–9753, sketched in mechanism 8; SA (ER7), 6571–6584, assumed | `b109.md` P20 (Codex); checked by Claude (`p20-gate`), with R1 |
| Corollary B, Lemma C, (5.4) | `4.8:prop-small-pairs` proved from the assumed (1.17); `4.7:not-true-pairs` and `5.2:lem-polydisc-containment` use it; SA (ER8), 6586–6630, is proved conditional on ER7; here it is implemented with explicit constants, the true-current specialization, and the account's consumer identifications | `l17c.md` §§2–3 (Codex); checked by Claude (`l17c-gate`, ADVANCE), with R2 |
| I1, averages of a complex perturbation, depth-uniform (Balaban CMP 98, Props 2, 4, 5) | not stated separately; the average bound is used as printed inside the (1.17) sentence (CA-I 32603–32606); CMP 98 locality is `4.6:lem-averaging-locality` (CA-I 24239), cited | `b109.md` P15 (72), (74)–(77), re-derived in `p20-gate` §3; `a1-balaban.md` §3.5, §7.6, (7.14), checked (FINISH row 81) |
| I2, holomorphic continuation in the datum, with the Euler-equation bound (Balaban CMP 102 §G) | `8.4:thm-minimiser-analyticity` (CA-II 85845), cited; (189)–(190) are `9.3:prop-second-variation` (CA-III 35577), printed without proof | `a1-balaban.md` §9.1, (9.1)–(9.2), given F0; checked by Claude on Codex (`a1-balaban-gate`, repair D3) |
| I3, critical-orbit theorem at real data, linear in the datum radius (Balaban CMP 102 Theorem 1) | `4.9:thm-minimal-orbit` (CA-I 35144), cited | `a1-balaban.md` §8, (8.2), given F0; checked (row 81), gap order D2 |
| I4, curvature of averages of a real field (Balaban CMP 98 (48), (54); CMP 102 (160)) | used as printed inside the (1.17) sentence (CA-I 32603–32606) | `a1-balaban.md` (3.6), §7.1; checked (row 81) |
| I5, flat package F0 (CMP 99b Theorems 3.1–3.3, (3.48), (3.132) at \(U=1\); proofs in CMP 89, 95, 96) | `5.8:prop-local-decay` (CA-II 54464), cited | `flat-port.md` §§2, 4–9 (Codex); checked by Claude (`flat-port-gate`, repairs W1–W3; row 95) |
| I6, tower rules and collar bound; change of units | `4.8:def-tower-rules` with `4.8:eq-tower-rules-b` (CA-I 32834–32936), proved; `4.8:thm-restriction-units` (CA-I 33276), proved | ported as cited; the uses here re-checked in `p20-gate` (interior) and `l17c-gate` ((3)–(4)) |
| I7, quadratic remainder in the current | `4.4:lem-current-remainder` (CA-I 10350), proved | ported as cited; the case \(U_0=1\) re-checked in `l17c-gate` |

Every check named in this table is one reading by Claude of a text written by Codex.

## 9. Scope limits carried from the gates

1. **The original form stays open.** (1.17) at complex pairs with \(2B_3\alpha_0'\) alone is neither proved nor refuted. Theorem A is weaker on part of the domain (§2). It suffices for the uses in §6 only.
2. **Which object \(U_n^{\mathfrak r}\) is** (`p20-gate` F4). Here it is the axial representative of the unique regular critical orbit, continued holomorphically. The account calls it "the axial-gauge minimiser" of CMP 102 Theorem 1 (CA-I 32896). The two agree when the minimal orbit is regular. That clause of CMP 102 Theorem 1 is cited, not rebuilt.
3. **Determining sets** (`p20-gate` F3). The proof is for the default determining sets, inward bonds free, with the outward rows (SA 9625; `b109.md` §11.1). This is the only convention `a1-balaban.md` covers (its §10). The kept-inward convention of CMP 96 and 119 is not covered. A consumer must read the tower in the default convention.
4. **F0 and the pointed core.** F0's proofs come from CMP 89, 95 and 96, ported once in `flat-port.md`, including the level-0 seam of `a1-balaban-gate` D1. The pointed-core admission (10.2) of `a1-balaban.md` is outside this note.
5. **Unused hypotheses** (`p20-gate` F2). Theorem A uses neither the cube gauge (1.12) nor the current bound. Dropping them makes it stronger and breaks nothing.
6. **Separate inputs, not supplied here.** `4.13:lem-minimizer-unique` and `4.13:lem-own-constant` (proof outstanding in the account; our `mu.md`, `oc.md` at their own stated scope); the near-case bound \(|u_j-1|<B_3^2O(1)M\alpha_0\) (CMP 109 (3.37), taken by statement); the literal-frame, block-average, straddling and shell assertions of §6; and the stage-background and re-minimization assertions excluded at CA-I 38108–38144.
7. **What does not follow.** The other items of clause (0), the other inputs of (g) and (c), and T0. This note does not use the stage theorem of CMP 122a (1.60)–(1.70) that the account assumes at CA-I 54986–54998. It changes no status in the account or in `library/port-map.md`.
8. **Kind** (FINISH, How we work, items 6 and 9). The corrected quadratic budget, the real-point mechanism, and the conditional small-exponential inclusion are already in the Sussman–Alpoge outline. This note writes out their mechanism using the repository's named CMP 102/averaging inputs, makes the constants and domain ceilings explicit, and reconciles the fresh seed admissions and constant choices with the complete account. The true-current and \(U^c_j\) specializations and the correction of the target-radius polydisc step are explicit consumer work. R1 and R2 are compatibility/domain repairs, not new estimates. This is a comparison with the cited texts and repository results, not a claim of global mathematical priority. The fresh admissions in the true-pair and polydisc arguments have unit real factor and are supplied by Lemma C. The generic small-pairs supplier is replaced by Corollary B under (B1), and real curvature-only estimates may be retained under their original hypotheses. Other complex memberships, including minimizer families over nontrivial real bases, retain their separate nesting, inheritance, gauge-transport or increment suppliers. The search found no further fresh application of the original complex (1.17) requiring an unbudgeted non-seed pair; it did find additional complex memberships, excluded assertions and downstream constant uses. Any offer to them would first need the five checks of item 6.

## Result

**Proof (an implication from named inputs; write-up of results already checked).** On I1–I7, in the default determining-set convention and on their complete read sets, with the corrected norm constants, R1 and R2, the argument proves Theorem A with an early fixed \(K^\sharp\) independent of the auxiliary-radius ratio, depth, mesh and volume as specified by those inputs.

Corollary B replaces the small-pairs implication under (B1).
Lemma C supplies the fresh unit-base true-pair and independent-current polydisc admissions at a radius of the same form \(c_T\min(\alpha_0,\alpha_1)\), with one possibly smaller fixed \(c_T\). Its dependent constants and the final coupling ceiling must be read at that choice. Other complex memberships retain their separate suppliers.

This supplies the corrected inclusion component along the stated clause-(0)(g) and true-pair-(c) paths; it proves neither the original curvature-only (1.17), the remaining clause-(0) inputs, nor T0. Minimality identification and the other scope restrictions of §9 remain attached. The pre-repair draft was checked line by line by Codex (gates/wu-l17-gate.md, REVISE), repairs applied by Codex on 2026-11-06; this repair pass grants no status.

## Change log — repairs applied by Codex, 2026-11-06

Gate references are to `gates/wu-l17-gate.md` at checkout `f5986aa06`. Original WU lines refer to the gate's 277-line draft (SHA-256 `f98fa5b69d6a8f0b58c04dcc2588dcedf6f09f5ffafd178734a00d45460a49e5`). Current WU lines locate the repaired text. This log records edits, not a new audit or status.

| Repair | Original WU line(s) | Current WU line(s) | Gate line(s) |
|---|---|---|---|
| Provenance and the prior REVISE outcome; distinguish repair application from a new independent check | 8, 277 | 8, 301 | 204 |
| Report Balaban's conclusion as paraphrase, not a freestanding quotation | 21 | 21 | 22 |
| State that the small-pairs proof is conditional on its hypothesis | 28 | 28 | 23 |
| Complete the CA-III locator and add the CA-I complex sufficient-condition status record | 32 | 32 | 15–16, 112 |
| Replace the universal seed-or-real claim with the gate's fresh-admission and separate-supplier inventory | 44, 212, 268 | 44, 218, 292 | 131–135, 194 |
| Carry complete stencils/carriers and outward rows into (A1) and Lemma C | 61, 73 | 61, 73 | 98 |
| Repair N: distinguish normalized Hilbert-Schmidt and operator norms, retain sqrt(N), correct (4.1), and enlarge the fixed constant for (4.2)–(4.3) | 98, 103, 105, 107, 115 | 98, 103, 105, 107, 115 | 72–96 |
| Replace trace-norm terminology by normalized Hilbert-Schmidt | 167 | 167 | 65 |
| Restrict the c_T reset to the true-pair/polydisc constant and preserve only its ratio cancellation | 193 | 193 | 129, 137–157 |
| Use an inclusive list of c_T-dependent constants, including C_beta, C_mathfrak e and descendants, and allow a smaller coupling ceiling | 195 | 195–201 | 137–157 |
| Attribute the corrected inventory and retain the real numerical bound as a separate published input | 199, 205 | 205, 211 | 100–108, 192 |
| Correct the small-pairs locator and separate its suppliers | 208 | 214 | 33, 131–135 |
| Repair the downstream radius/response table entry | 210 | 216 | 157–159 |
| Remove CA-I 155275–155438 from the real list; preserve frozen-background and reblocking limitations | 214, 218 | 220, 224–234 | 34, 117, 120 |
| Correct exclusions and add complex nesting, gauge transport, kernel/window inputs and symbol/threshold records | 218 | 224–234 | 113–122, 124, 127, 159 |
| Add downstream c_T/radius consumers with an inclusive list and distinguish unrelated homonyms | 218 | 224–234 | 123, 125, 129 |
| Make the displayed order partial, preserve early floors, distinguish early sizes, and choose B^(109) before M | 222, 224 | 238, 240 | 165–170 |
| Give the explicit R_req, Stage 5 M_1 floor and capped R_1 choice, retaining the limited scope | 230 | 246–254 | 172–184 |
| Replace the R2 failure claim by the missing-domain restriction; assert no counterexample | 236 | 260 | 169, 186 |
| Attribute ER8 as proved conditional on ER7, with the explicit consumer implementation here | 248 | 272 | 48, 190–192 |
| Replace the novelty statement by the gate's comparison and compatibility/domain wording | 268 | 292 | 196–198 |
| Replace Result with the conditional theorem, changed budget, possibly smaller c_T, separate suppliers and remaining limits | 272, 274, 275, 277 | 296, 298, 299, 301 | 200–204 |
