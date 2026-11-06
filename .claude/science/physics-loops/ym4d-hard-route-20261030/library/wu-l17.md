lead: anthropic/claude-opus-5-5/max mac-mini-worker
lease_until: 2026-11-06T14:12Z

# CMP 109 (1.17) at complex pairs: a corrected statement and its proof

Draft for the owner. Not sent anywhere. Research text; it grants no status.

**Provenance.** Written by Claude Opus 5.5 (max effort), Mac mini worker, at commit cbb40eca5. It writes up `library/l17c.md` (Codex) and `library/b109.md` P19–P20 (Codex), with the repairs of `gates/l17c-gate.md` and `gates/p20-gate.md` (each one line-by-line reading by Claude). The mathematics is theirs. New here: the presentation, and one remark on the order of choice (§7, R1, marked). This document as a whole has not been read by another model.

**Sources.** Ethan Sussman and Levent Alpoge, with Claude and Codex as authors of their text, commit 31a47c543775. CA-I, CA-II, CA-III are `theorem_0_complete_account_raw_{I,II,III}.tex`; SA is `YM4_sketch_500.tex`. Numbers are source lines. Each passage quoted was read in a bounded excerpt of a copy fetched for this note.

**Credit.** Tadeusz Balaban: the critical-orbit theorem of CMP 102 (Theorem 1, its analytic continuation in §G, Proposition 9), which carries every member of the tower; the averaging and gauge constructions of CMP 98 and 99; the flat propagator bounds of CMP 89, 95, 96 and 99b; the regularity spaces and the sentence (1.17) of CMP 109. Sussman and Alpoge (with Claude and Codex): the two-rule hereditary class, the corrected budget and the real-point argument (SA Theorem 5(a), mechanism 8), and the small-exponential argument (SA (ER8)).

## 1. The statement in their account, and its status there

**The sentence.** CA-I 32599–32623 transcribes CMP 109 p. 263. Let \(\alpha_0'<\alpha_0\), \(\alpha_1'<\alpha_1\). Let \((\mathbf U,\mathbf J)\) satisfy conditions (i)–(iii) of Balaban's regularity spaces at level \(j\) on \(X\), with \(\alpha_0',\alpha_1'\) in place of \(\alpha_0,\alpha_1\). The averages obey \(|\partial\bar{\mathbf U}^p-1|<2\alpha_0'(L^p\xi)^2\), and CMP 102 Proposition 9 then gives, on \(\tilde X^{-2}\),
\[
|\partial U_n(M^{\boldsymbol\cdot}(\mathbf U))-1|<2B_3\alpha_0'\xi^2,\qquad
|J_n(M^{\boldsymbol\cdot}(\mathbf U))|<2B_3\alpha_0'(L^n\xi)^2 .\tag{1.17}
\]
"For \(\alpha_0'\) sufficiently small these estimates imply condition (iv)." These primes are the small radii of this sufficient condition. They are not the larger operator radii of CMP 116 (CA-I 32666–32670).

**The use.** `4.8:prop-small-pairs` (CA-I 34058–34218) assumes: "for every \((p,Z)\in\mathfrak T_j(X)\) and every \(\mathfrak r\in\mathfrak R\), the estimate [CMP 109 (1.17)] holds at complex pairs, as stated on [p. 263]", with \(M/L\) and \(LB^{(109)}\) (CA-I 34067–34072). Its budget `4.8:eq-small-pairs-1` is \(\alpha_1'\le\alpha_1\), \(2B_3\alpha_0'\le\alpha_0\) (CA-I 34061–34062). Step 2 (CA-I 34148–34166) applies the hypothesis at \((\mu\alpha_0',\mu\alpha_1')\), \(\mu=L^{-(j-p)}\), and obtains `4.8:eq-small-pairs-3`:
\[
|\partial U_n^{\mathfrak r}(Z;M^{\boldsymbol\cdot}(\mathbf U))-1|<2B_3\mu\alpha_0'\xi_p^2,\qquad
|J_n^{\mathfrak r}(Z;M^{\boldsymbol\cdot}(\mathbf U))|<2B_3\mu\alpha_0'(L^n\xi_p)^2\quad\text{on }Z^{\wr p}.
\]
The proposition has no status sentence. So it is proved from this hypothesis.

It reaches T0 through `4.19:prop-clause-zero` (CA-I 56419–56439). Item (g), the one-power hereditary class, reads it through membership (e) of `4.8:prop-class-reproduction` (CA-I 34241–34403). Item (c), the coupling increment, reads it through `4.7:not-true-pairs` (CA-I 29522–29605) and `4.7:prop-coupling-increment` (CA-I 32412–32491). One more direct use is the step "(i)–(iii) imply (iv)" of `5.2:lem-polydisc-containment` (CA-II 4381–4384). That step applies the sentence at the target radii themselves.

**Status there.** CA-III chapter 13, "Statements used without proof in this account", list (3, continued): "the inclusion sentence [CMP 109 (1.17)], read at complex pairs · Chapter 4 · cited as printed at its use site" (CA-III 111326). CA-I 166588–166589: "printed without proof; cited as printed".

**The outline's form.** SA Theorem 5(a) (SA 9746–9753) states the bound with \(K^\sharp(\alpha_0'+\alpha_1'^2)\) in place of \(2B_3\alpha_0'\), and the budget "once \(K^\sharp(\alpha_0'+\alpha_1'^2)\le\alpha_0\)". SA mechanism 8 (SA 9899–9911) sketches the proof. SA (ER8) (SA 6586–6630) states the small-exponential lemma "for sufficiently small \(a_0,a_1\)".

**Our labels.** L17 (`b109.md` §11.1) and Q119 (`b119.md`) are this statement at complex pairs, with \(2B_3\alpha_0'\) alone.

## 2. What is wrong with the original form, and the correction

**The original form is unproved at complex pairs.** It asks for a bound linear in the curvature radius \(\alpha_0'\) alone, for every \(\alpha_1'\le\alpha_1\), with no relation between the two radii. Balaban's derivation goes through CMP 102 Proposition 9. That proposition bounds the continued minimizer by the size of the datum increment. At a complex pair, the increment that \(A'\) adds to the averages is linear in \(\alpha_1'\). In level-\(n\) units, with \(s=L^n\xi_p\), the direct estimate is \(C(\alpha_0's^2+\alpha_1's)\) (`b109.md` (108)). The clause needs \(s^2\) times a constant. The quotient keeps \(\alpha_1'/s\), which is unbounded as \(p-n\) grows. So the derivation does not give (1.17) at complex pairs. We know no proof. Three further routes stop at named steps (`b109.md` §§11.2–11.4, `b119.md` §7). No counterexample is known. The original form is open: neither proved nor refuted. This note does not claim that Balaban's sentence is false.

**The hypotheses allow \(\alpha_1'^2\gg\alpha_0'\).** Take \(U=1\) and a constant, commuting, complex potential in one direction (`b109.md` §11.4). Every plaquette equals \(1\). So (i)–(iii) hold for every \(\alpha_0'>0\) at fixed \(\alpha_1'\). (Its tower curvature is zero, so it refutes nothing.) Hence the corrected bound below is weaker than (1.17) on part of the domain, and the budget must carry the square.

**The correction.** Replace the hypothesis of `4.8:prop-small-pairs` by Theorem A, which is proved below. Replace `4.8:eq-small-pairs-1` by the budget (B1), which is the outline's own Theorem 5(a) budget. This suffices because every complex pair at which the account applies (1.17) is a seed: real factor \(U=1\), and fields bounded by a fixed multiple of \(\min(\alpha_0,\alpha_1)\). For a seed the auxiliary radii can be chosen so that the square costs nothing (Lemma C). Every other use is at a real pair, where \(\alpha_1'=0\) (§6).

## 3. The corrected statements

Notation is that of CA-I 32834–33070: towers \(\boldsymbol\Omega^{\mathfrak r}(Z)\) under the rules \(\mathfrak R=\{\mathfrak r_1,\mathfrak r_2\}\), the layered average \(M^{\boldsymbol\cdot}\), the current \(J_n^{\mathfrak r}\) in level-\(n\) units, the two-layer interior \(Z^{\wr p}\), the labels \(\mathfrak T_j(X)\), the tower clause \((\mathrm{iv})^{\mathfrak r}_{p,Z}[c]\) and the class \(U^{\Sigma^1}_j\). The constants and their order are in §7.

**Theorem A (corrected (1.17) at complex pairs).** There are constants \(K^\sharp\ge1\) and \(\bar\alpha_0',\bar\alpha_1'>0\) with the following property. They depend only on \(d=4\), \(N\), \(L\), \(\mathfrak M\), the flat constants F0 and the constants of the critical-orbit theorem. They do not depend on \(p,n,Z,\mathfrak r\), the torus, \(M\), \(B^{(109)}\), or \(\alpha_1'/\alpha_0'\). Let \(M\ge 2LR_1M_1\). Let \(p\ge1\), \(Z\in\mathbf D_{p-1}\), \(\mathfrak r\in\mathfrak R\), \(0<\alpha_0'\le\bar\alpha_0'\) and \(0<\alpha_1'\le\bar\alpha_1'\). Let \(\mathbf U=U'U\) on the bonds of \(Z\), with \(U\) \(G\)-valued, \(U'=e^{i\xi_pA'}\), and
\[
|\partial U-1|<\alpha_0'\xi_p^2,\quad |\partial\mathbf U-1|<\alpha_0'\xi_p^2,\quad |A'|,\ |\nabla^{\xi_p}_UA'|<\alpha_1'\quad\text{on }Z. \tag{A1}
\]
Then for \(n=1,\dots,p\) the analytic tower branch \(U_n^{\mathfrak r}(Z;M^{\boldsymbol\cdot}(\mathbf U))\) exists, and on \(Z^{\wr p}\)
\[
|\partial U_n^{\mathfrak r}(Z;M^{\boldsymbol\cdot}(\mathbf U))-1|<K^\sharp(\alpha_0'+\alpha_1'^2)\,\xi_p^2,\qquad
|J_n^{\mathfrak r}(Z;M^{\boldsymbol\cdot}(\mathbf U))|<K^\sharp(\alpha_0'+\alpha_1'^2)\,(L^n\xi_p)^2. \tag{A2}
\]
The same holds for \(U\) in place of \(\mathbf U\), with \(\alpha_1'=0\).

*Remarks.* (A1) is (1.11), (1.13) and the first inequality of (1.14) at level \(p\). The cube gauge (1.12) and the current bound \(|\mathbf J|<\gamma_0\) are not used (`p20-gate` F2); a consumer that has them loses nothing. For real data, \(U_n^{\mathfrak r}\) is the axial representative of the unique regular critical orbit. For complex data it is that representative's holomorphic continuation in the datum (scope S2 in §8).

**Corollary B (corrected `4.8:prop-small-pairs`).** In `4.8:prop-small-pairs`, replace the hypothesis at CA-I 34067–34072 by Theorem A, and `4.8:eq-small-pairs-1` by
\[
\alpha_1'\le\alpha_1,\qquad K^\sharp(\alpha_0'+\alpha_1'^2)\le\alpha_0,\qquad \alpha_0'\le\bar\alpha_0',\quad\alpha_1'\le\bar\alpha_1'. \tag{B1}
\]
Keep every other hypothesis. Then `4.8:eq-small-pairs-2` holds: \((\mathbf U,\mathbf J)\in U^{\Sigma^1}_j(X;\alpha_0,\alpha_1,\gamma_0)\). Its last paragraph, on the real minimal configurations of CMP 109 p. 263, holds with \(K^\sharp\alpha_0'\le\alpha_0\).

**Lemma C (seeds).** Let \(0<\alpha_0,\alpha_1\le1\) satisfy
\[
\alpha_0\le 4K^\sharp\bar\alpha_0',\qquad \alpha_1\le 2\bar\alpha_1'. \tag{C0}
\]
There is \(c_*>0\), depending only on \(K^\sharp\), \(d\) and \(N\), with the following property. Put \(r:=c_*\min(\alpha_0,\alpha_1)\). Let \(j\ge1\), \(X\in\mathbf D_{j-1}\), and let \(A\) be a \(\mathfrak g^c\)-valued bond field on \(X\) with \(|A|,|\nabla^{\xi_j}A|\le r\).

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

**Step 1: the covariant curl of \(A'\) is small (SA 9905–9909).** Let \(p\) be a plaquette with bonds \(b_1,b_2,b_3,b_4\) as in CA-I 10333–10345, so that \(\partial V(p)=V(b_1)V(b_2)V(b_3)^{-1}V(b_4)^{-1}\) and \((D_UA)(p)=\eta^{-1}(A_1+R(U_1)A_2-R(U_4)A_3-A_4)\). Move each exponential of \(\mathbf U\) to the first corner:
\[
\partial\mathbf U(p)=e^{X_1}e^{X_2}e^{X_3}e^{X_4}\,\partial U_r(p),\qquad
X_1=i\eta A_1',\ X_2=i\eta R(U_1)A_2',\ X_3=-i\eta R(U_1U_2U_3^{-1})A_3',\ X_4=-i\eta R(\partial U_r(p))A_4' .
\]
The transports are unitary, so \(\|X_\nu\|\le\eta|A'|\). The terms of the product with two or more factors \(X_\nu\) sum to at most \(e^{4\eta|A'|}-1-4\eta|A'|\le C\eta^2|A'|^2\), using \(\eta\alpha_1'\le1\). The transports of \(A_3'\) and \(A_4'\) differ from those of \(D_{U_r}\) by \(R(\partial U_r(p))\). Since \(\|R(P)Y-Y\|\le2\|P-1\|\|Y\|\) for unitary \(P\), this costs at most \(C\eta|A'|\,\alpha_0'\eta^2\). Hence
\[
\partial\mathbf U(p)\,\partial U_r(p)^{-1}=1+i\eta^2(D_{U_r}A')(p)+E,\qquad \|E\|\le C\eta^2\alpha_1'^2+C\eta^3\alpha_0'\alpha_1'. \tag{4.1}
\]
Since \(\partial U_r(p)\) is unitary, \(\|\partial\mathbf U\,\partial U_r^{-1}-1\|=\|\partial\mathbf U-\partial U_r\|<2\alpha_0'\eta^2\) by (A1). With (4.1),
\[
|D_{U_r}A'|\le C_s(\alpha_0'+\alpha_1'^2). \tag{4.2}
\]
Write \(A'=A_R+iA_I\) with \(A_R,A_I\) Hermitian. Because \(U_r\) is unitary, \(R(U_r)\) commutes with the adjoint, so \(D_{U_r}\) and \(\nabla_{U_r}\) commute with both projections. So \(|D_{U_r}A_R|,|D_{U_r}A_I|\le|D_{U_r}A'|\), and \(|A_R|,|A_I|,|\nabla_{U_r}A_R|,|\nabla_{U_r}A_I|<\alpha_1'\). Apply (4.1) to \(A_R\) and to \(A_I\). The real fields \(U_R:=e^{i\eta A_R}U_r\) and \(U_I:=e^{i\eta A_I}U_r\) are \(G\)-valued, and
\[
|\partial U_R-1|,\ |\partial U_I-1|\le C_s(\alpha_0'+\alpha_1'^2)\,\eta^2 . \tag{4.3}
\]
This uses only \(|A'|<\alpha_1'\) and the two curvature bounds, with no bound on \(\nabla A'\).

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

**Proof of Lemma C.** Norms on matrices are those of CA-I 10306; the operator norm is at most \(b:=\sqrt N\) times the trace norm used there.

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
once, and use it at every occurrence. The norm \(N_j(\mathsf Z)\) of `4.7:eq-true-pairs-1` is the value, first difference and second-order norm of \(A:=\ell_j\mathsf Z\) at spacing \(\xi_j\). So \(N_j(\mathsf Z)\le c_Tr_j\), \(r_j=\min(\alpha_{0,j},\alpha_{1,j})\), gives the hypotheses of Lemma C (b) and (c) at the running radii. The running radii obey (C0), since \(\alpha_{i,j}\le\alpha_i\) (CA-I 1667–1669) and \(\alpha_i\) obeys R2. This proves clauses (a) and (b) of `4.7:not-true-pairs` and replaces its free-prime step (CA-I 29557–29589). It also replaces the step "(i)–(iii) imply (iv)" of `5.2:lem-polydisc-containment` (CA-II 4381–4384), by Lemma C (a) and (c). That lemma's radius \(\mathfrak r_j=c_T\min(\alpha_{0,j},\alpha_{1,j})\) and its ratio \(\mathfrak t_j^{-2}=(\min\{\alpha_0,\alpha_1\}/\min\{C_0,C_1\})^2x_j(\log x_j)^{-2q}\) are unchanged; \(c_T\) cancels.

A smaller \(c_T\) changes only constants that are fixed before \(\gamma\): \(C_\vartheta\) (CA-I 30028–30056), \(\widetilde K\) (29828–29865), \(C'\) (32284), \(C_\Pi\) (CA-III 90592), and the Cauchy radius \(\xi_i^3c_Tr_i/(8d)\) of the coupling extraction (CA-I 32452–32491). Each is fixed before \(\gamma\) (CA-I 32405–32409; CA-II 94857–94865). Since \(q>p_0\), \(\vartheta(\gamma)\to0\) as before (CA-I 30051–30105). No exponent changes, and no lower bound on the coupling appears (`l17c-gate`, step "c_T and its consumers").

## 6. Every use of (1.17) in the account

The list combines the inventory of `l17c.md` §6 with the referee's own search (`l17c-gate`, findings 2 and "Consumer list"): every `1.17`, the labels of the displays, every `c_T`, every `2B_3` and `B_3^2`, and every "(i)–(iii) imply (iv)", over CA-I, II and III. CMP 109 (1.17) occurs at 31 lines of CA-I and at CA-III 111326. Every other `1.17` is CMP 116, 122a, 122b or a decimal.

| Use | Pair | Supplied by |
|---|---|---|
| CA-I 34058–34218, `4.8:prop-small-pairs` | the supplier slot | Corollary B |
| CA-I 34811–34830, amplitude ceilings | the entry \(2B_3\alpha_0'\le\alpha_0\) at 34819 | replace by (B1) |
| CA-I 32599–32623, the sufficient condition | generic statement | state it as Theorem A with (B1); its real case is unchanged |
| CA-I 29522–29605, `4.7:not-true-pairs` | true pairs, \(U=1\), ball \(c_Tr_j\) | Lemma C (b), (c) with (5.4) |
| CA-I 32412–32500, `4.7:prop-coupling-increment` | polydisc of radius \(\xi^3c_Tr/(8d)\), through true pairs | the same |
| CA-I 34241–34403, `4.8:prop-class-reproduction`, membership (e); CA-I 34714, 34738 | unit, true and small pairs; real backgrounds | Lemma C; Theorem A at \(\alpha_1'=0\) |
| CA-II 4333–4398, `5.2:lem-polydisc-containment` | \(e^{i\xi\mathcal A}\), independent current, ball \(\mathfrak r_j\) | Lemma C (a), (c) with (5.4) |
| CA-II 4599–4688, 94811–97192; CA-III 90585–90624 | through \(\mathfrak r_j\) | radius only; \(c_T\) cancels |

Every complex pair here has \(U=1\) and a field of size at most a fixed multiple of \(\min(\alpha_0,\alpha_1)\). That is why the square costs nothing: \(r^2\le r\min(\alpha_0,\alpha_1)\le\alpha_0r\).

**Uses at real pairs** (\(\alpha_1'=0\); Theorem A gives \(K^\sharp\alpha_0'\), and the real bound \(2B_3\alpha_0'\) of CMP 102 Proposition 9 may be kept): the minimal configurations of CMP 109 p. 263 (CA-I 34087–34089, 34205–34208); CA-I 10750–10754, 36806–36905, 42198–42340, 43590–44380, 128551–128930, 155275–155438; CA-II 99767–99813.

**The other memberships of class reproduction keep their own suppliers** (`l17c.md` §5, checked in `l17c-gate`). Near incoming pair: the assumed hereditary clause. Near product: the nesting identity of `4.13:lem-minimizer-unique` (CA-I 45162, proof outstanding there; our `mu.md`). Far incoming pair: restriction. Far product: the increment estimate, with its \(\alpha_2\) ceiling. Domain restriction: monotonicity. None of them applies (1.17) at the full target radii. The own-radius gauge of `4.13:lem-own-constant` (CA-I 45203, proof outstanding there; our `oc.md`) is met without (A2): seeds have \(U=1\), and real backgrounds use real CMP 98 averaging and CMP 102 gauges.

**Matches that are not uses.** The larger primed operator radii of CMP 116 (CA-I 4384–4554, 5822–5908 and others); block-average and literal-frame curvature assertions (CA-I 13198–13255, 17523–17564, 18305–18346); straddling and shell clauses (10028–10092, 120111–120334); passages that name the (1.17) route and do not take it (15918–15961, 20150–20185, 34886–35045, 117207–117328, 121282–121350); and definitions that fix units (154551–154588, 154825–154863, 155490–155511). These were separate inputs under the old (1.17) too. This note supplies none of them.

## 7. Order of constants, and the two repairs

The order, with every letter chosen after those before it:

\(L\); \(\mathfrak M\); the F0 constants; the critical-orbit constants \(B_1,r_B,\varepsilon_{\rm adm}\), its localization length and its gap number \(R_{D2}\); **\(R_1\ge R_{D2}\) (R1)**; \(M_1=R_\star'\mathfrak M\) with \(R_\star'\ge R_1\); the averaging constants \(r_4,C_4,\alpha_*\); \(K^\sharp\), then \(\bar\alpha_1'\), then \(\bar\alpha_0'\); \(M\ge2LR_1M_1\) and \(B^{(109)}\); Stage 7 with **R2**; \(\alpha_2\); \(c_T\) by (5.4) and the constants built from it; \(\gamma\) last. The auxiliary radii (5.3) are chosen at each use, after the target radii.

The ceilings of Theorem A are \(\bar\alpha_1'\le r/2\), and \(C_3\max\{1,C_s\}(\bar\alpha_0'+\bar\alpha_1'^2)\le\min\{\alpha_*,\varepsilon_{\rm adm}/2\}\) together with the smallness used in Step 2. The square enters only as a ceiling on \(\bar\alpha_1'\). No relation between \(\alpha_0'\) and \(\alpha_1'\) is imposed (`p20-gate` §4).

**R1. The gap number (`p20-gate` F1).** I2 and I3 hold on towers whose gap is at least a number fixed after the localization length of `a1-balaban.md` (6.3)–(6.5). By `a1-balaban-gate` D2 the gap must exceed four lengths; the largest is about \(6L\) times that localization length, in units of \(\mathfrak M L^q\). Call this gap number \(R_{D2}\); it reads only \(L\), \(\mathfrak M\) and the F0 constants. Rule \(\mathfrak r_1\) has gap \(R_1\mathfrak ML^q\) (CA-I 32877–32879). Rule \(\mathfrak r_2\) has gap \(M_1L^q\ge R_1\mathfrak ML^q\). So choose the account's \(R_1\ge R_{D2}\). The account only asks that \(R_1\) be "sufficiently large" (CA-I 32847–32851); R1 names one floor it must meet. The letter \(R_1\) denotes two constants here: `a1-balaban`'s localization factor and the account's gap number. Read as one constant, D2 cannot hold for \(\mathfrak r_1\).

*Remark (this note; not read by another model).* The account's Stage 5 lists \(R_1\) after \(M_1\), "chosen upward" (CA-I 1508–1511, 2063–2064), while CA-I 32851 asks \(R_\star'=M_1/\mathfrak M\ge R_1\). Read literally, \(M_1\) then caps \(R_1\). So the floor of R1 must also be placed on \(M_1\): add \(M_1\ge R^{\min}_1\mathfrak M\) to Stage 5, where \(R^{\min}_1\) is the least power of \(L\) meeting the floors on \(R_1\). It reads only earlier letters, so no cycle arises.

**R2. The Stage-7 ceiling (`l17c-gate` finding 1).** Lemma C needs \(\alpha_0'=\alpha_0/(4K^\sharp)\le\bar\alpha_0'\) and \(\alpha_1'\le\alpha_1/2\le\bar\alpha_1'\). So add to the radii of Stage 7 (CA-I 1614–1629) the ceilings
\[
\alpha_0\le4K^\sharp\bar\alpha_0',\qquad \alpha_1\le2\bar\alpha_1'.
\]
Their letters are fixed before the radii, and the radii are chosen downward after \((L,B^{(109)},M)\) (CA-I 34811–34830). So there is no cycle. The running radii inherit R2 through \(\alpha_{i,j}\le\alpha_i\) (CA-I 1667–1669). Without R2 the lemma fails as stated in `l17c.md` (line 192): for \(\alpha_0\) near \(1\), \(\alpha_0/(4K^\sharp)\) can exceed \(\bar\alpha_0'\). The outline states the same lemma "for sufficiently small \(a_0,a_1\)" (SA (ER8), 6586–6590).

**No square ceiling on the absolute radii.** The account chooses \(\alpha_1\) before \(\alpha_0\) (CA-I 1614–1615). A ceiling \(\alpha_1^2\le c\,\alpha_0\) would be a floor on the later \(\alpha_0\), so it is not used. The square is carried by the auxiliary radii (5.3) instead. A square ceiling on fixed fractions of the running radii would be an allowed Stage-8 \(\gamma\) ceiling, since \(\alpha_{1,n}^2/\alpha_{0,n}=(C_1^2/C_0)x_n^{-1/2}(\log x_n)^q\to0\) (`l17c.md` (15)); it is not needed.

## 8. Inputs, with their status in their account and in ours

"Checked" means one line-by-line reading by one other model, first failing step none. It is not an audit, and a checked result is still an implication from its named inputs.

| Input | Their account | Ours |
|---|---|---|
| Lemma 1, real-point Taylor inequality | SA mechanism 8 (SA 9899–9905), sketched, constant unnamed | `b109.md` P19 (Codex); checked by Claude (`p20-gate` §2) |
| Theorem A | not stated; the account assumes the stronger (1.17) (CA-I 34067–34072). Outline: SA Theorem 5(a), 9746–9753, sketched in mechanism 8; SA (ER7), 6571–6584, assumed | `b109.md` P20 (Codex); checked by Claude (`p20-gate`), with R1 |
| Corollary B, Lemma C, (5.4) | `4.8:prop-small-pairs` proved from the assumed (1.17); `4.7:not-true-pairs` and `5.2:lem-polydisc-containment` use it; SA (ER8), 6586–6630, sketched | `l17c.md` §§2–3 (Codex); checked by Claude (`l17c-gate`, ADVANCE), with R2 |
| I1, averages of a complex perturbation, depth-uniform (Balaban CMP 98, Props 2, 4, 5) | not stated separately; the average bound is used as printed inside the (1.17) sentence (CA-I 32603–32606); CMP 98 locality is `4.6:lem-averaging-locality` (CA-I 24239), cited | `b109.md` P15 (72), (74)–(77), re-derived in `p20-gate` §3; `a1-balaban.md` §3.5, §7.6, (7.14), checked (FINISH row 81) |
| I2, holomorphic continuation in the datum, with the Euler-equation bound (Balaban CMP 102 §G) | `8.4:thm-minimiser-analyticity` (CA-II 85845), cited; (189)–(190) are `9.3:prop-second-variation` (CA-III 35577), printed without proof | `a1-balaban.md` §9.1, (9.1)–(9.2), given F0; checked by Claude on Codex (`a1-balaban-gate`, repair D3) |
| I3, critical-orbit theorem at real data, linear in the datum radius (Balaban CMP 102 Theorem 1) | `4.9:thm-minimal-orbit` (CA-I 35144), cited | `a1-balaban.md` §8, (8.2), given F0; checked (row 81), gap order D2 |
| I4, curvature of averages of a real field (Balaban CMP 98 (48), (54); CMP 102 (160)) | used as printed inside the (1.17) sentence (CA-I 32603–32606) | `a1-balaban.md` (3.6), §7.1; checked (row 81) |
| I5, flat package F0 (CMP 99b Theorems 3.1–3.3, (3.48), (3.132) at \(U=1\); proofs in CMP 89, 95, 96) | `5.8:prop-local-decay` (CA-II 54464), cited | `flat-port.md` §§2, 4–9 (Codex); checked by Claude (`flat-port-gate`, repairs W1–W3; row 95) |
| I6, tower rules and collar bound; change of units | `4.8:def-tower-rules` with `4.8:eq-tower-rules-b` (CA-I 32834–32936), proved; `4.8:thm-restriction-units` (CA-I 33276), proved | ported as cited; the uses here re-checked in `p20-gate` (interior) and `l17c-gate` ((3)–(4)) |
| I7, quadratic remainder in the current | `4.4:lem-current-remainder` (CA-I 10350), proved | ported as cited; the case \(U_0=1\) re-checked in `l17c-gate` |

Both models' checks of this chain were done by Claude on Codex texts. P19, P20 and L17C were written by Codex.

## 9. Scope limits carried from the gates

1. **The original form stays open.** (1.17) at complex pairs with \(2B_3\alpha_0'\) alone is neither proved nor refuted. Theorem A is weaker on part of the domain (§2). It suffices for the uses in §6 only.
2. **Which object \(U_n^{\mathfrak r}\) is** (`p20-gate` F4). Here it is the axial representative of the unique regular critical orbit, continued holomorphically. The account calls it "the axial-gauge minimiser" of CMP 102 Theorem 1 (CA-I 32896). The two agree when the minimal orbit is regular. That clause of CMP 102 Theorem 1 is cited, not rebuilt.
3. **Determining sets** (`p20-gate` F3). The proof is for the default determining sets, inward bonds free, with the outward rows (SA 9625; `b109.md` §11.1). This is the only convention `a1-balaban.md` covers (its §10). The kept-inward convention of CMP 96 and 119 is not covered. A consumer must read the tower in the default convention.
4. **F0 and the pointed core.** F0's proofs come from CMP 89, 95 and 96, ported once in `flat-port.md`, including the level-0 seam of `a1-balaban-gate` D1. The pointed-core admission (10.2) of `a1-balaban.md` is outside this note.
5. **Unused hypotheses** (`p20-gate` F2). Theorem A uses neither the cube gauge (1.12) nor the current bound. Dropping them makes it stronger and breaks nothing.
6. **Separate inputs, not supplied here.** `4.13:lem-minimizer-unique` and `4.13:lem-own-constant` (proof outstanding in the account; our `mu.md`, `oc.md` at their own stated scope); the near-case bound \(|u_j-1|<B_3^2O(1)M\alpha_0\) (CMP 109 (3.37), taken by statement); the literal-frame, block-average, straddling and shell assertions of §6; and the stage-background and re-minimization assertions excluded at CA-I 38108–38144.
7. **What does not follow.** The other items of clause (0), the other inputs of (g) and (c), and T0. This note changes no status in the account or in `library/port-map.md`.
8. **Kind** (FINISH, How we work, items 6 and 9). Theorem A is a proof of a step the outline sketches (SA Theorem 5(a), mechanism 8). The correction moves the account's (1.17) use to its own outline's budget (`l17c-gate` finding 3). New against their text: the written proof of Theorem 5(a) from the rebuilt CMP 102, the check that every complex use is a seed or real, the step "(i)–(iii) imply (iv)" at the target radii (CA-II 4381–4384) replaced by Lemma C, and the order repairs R1 and R2. Any offer to them would first need the five checks of item 6.

## Result

**Proof (an implication from named inputs; write-up of results already checked).** On the inputs I1–I7 of §8, in the default convention, with R1 and R2 in the order of constants:

- **Theorem A:** at complex pairs, both tower rules, every depth, domain and volume, \(|\partial U_n^{\mathfrak r}-1|<K^\sharp(\alpha_0'+\alpha_1'^2)\xi_p^2\) and \(|J_n^{\mathfrak r}|<K^\sharp(\alpha_0'+\alpha_1'^2)(L^n\xi_p)^2\) on \(Z^{\wr p}\), with an early \(K^\sharp\) independent of \(\alpha_1'/\alpha_0'\).
- **Corollary B and Lemma C:** `4.8:prop-small-pairs` holds with the budget \(\alpha_1'\le\alpha_1\), \(K^\sharp(\alpha_0'+\alpha_1'^2)\le\alpha_0\); every complex seed of the account (true pairs, small pairs, the polydiscs of `4.7` and `5.2`) is admitted at the unchanged radius \(c_T\min(\alpha_0,\alpha_1)\), with \(c_T\le c_*\).

So the (1.17) input of clause (0)(g), and of (c) through true pairs, is supplied in corrected form. **Open:** the original \(2B_3\alpha_0'\)-only (1.17) at complex pairs (not needed by any use found); the scope items 2–4 and 6 of §9; everything else in clause (0) and T0. This write-up has not been read by another model.
