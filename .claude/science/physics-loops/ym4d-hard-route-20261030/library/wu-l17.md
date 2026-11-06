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

The inputs I1–I7 are stated where they are used; §5 lists each with its status. This is `b109.md` P19–P20, with the details recorded in `gates/p20-gate.md` §§2–4.

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

**Step 1: the covariant curl of \(A'\) is small (SA 9905–9909).** Let \(p\) be a plaquette with bonds \(b_1,b_2,b_3,b_4\) as in CA-I 10343–10346, so that \(\partial V(p)=V(b_1)V(b_2)V(b_3)^{-1}V(b_4)^{-1}\) and \((D_UA)(p)=\eta^{-1}(A_1+R(U_1)A_2-R(U_4)A_3-A_4)\). Move each exponential of \(\mathbf U\) to the first corner:
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

*I4 (averaging of a complex perturbation; CMP 98).* There are \(r_4>0\) and \(C_4\), depending on \(L\), \(\mathfrak M\) and the averaging constants only, such that \(B\) is holomorphic on \(\{\|w\|<r_4\}\) and \(\sup|B(w)|\le C_4\|w\|\) there, for every real \(U_r\) with \(|\partial U_r-1|\le\alpha_0'\eta^2\), \(\alpha_0'\le\bar\alpha_0'\).

The depth count is this. The straightened relative angles \(b_q\) of the level-\(q\) average obey the one-step inequality (`b109.md` (107); `a1-balaban.md` §3.5, actual-mean form §7.6)
\[
b_{q+1}\le L(1+C\alpha_0'\,t_q^2)\,b_q+C_Lb_q^2,\qquad b_0\le\eta_n|w| .
\]
Put \(\beta_q:=b_q/t_q\), so \(\beta_0\le|w|\). While \(\beta_q\le2|w|\), \(\beta_{q+1}\le\beta_q(1+C\alpha_0't_q^2+2C_L'|w|t_q)\). Since \(\sum_qt_q^2\le(1-L^{-2})^{-1}\) and \(\sum_qt_q\le(1-L^{-1})^{-1}\), the product of these factors is at most \(2\) once \(\alpha_0'\) and \(|w|\) are below fixed ceilings. By induction on \(q\) (first exit), \(\beta_q\le2|w|\) for all \(q\le n\). The endpoint (node) factors obey the same summable first-power bound (`b109.md` P15 (72), (74)–(77); `a1-balaban.md` (7.14)). So \(\sup|B(w)|\le C_4\|w\|\), with no factor depending on \(n\) or \(p\). Holomorphy holds because \(B\) is a finite composition of products, inverses and convergent logarithm series. A recursion on the plain angles with coefficient \(L\) would be false (endpoint sums of order \(dL\)); it is not used (`p20-gate` §3).

**Step 3: one holomorphic function and its crude bound.**

*I2 (holomorphic continuation; CMP 102 §G; `a1-balaban.md` §9.1).* There are \(r_B>0\), \(\varepsilon_{\rm adm}>0\) and \(C_2\) with the following property. Let \(V_0\) be a real layered datum of datum radius at most \(\varepsilon_{\rm adm}/2\). Then \(B\mapsto\Phi_{V_0}(B)\), the axial representative at the datum \(e^{iB}V_0\), is holomorphic on \(\{\sup|B|<r_B\}\). In level-\(n\) units, at every plaquette \(p\) and bond \(b\) of the top layer, \(\eta_n^{-2}|\partial\Phi_{V_0}(B)(p)-1|\) and \(|J(\Phi_{V_0}(B))(b)|\) are at most \(C_2(\varepsilon_{\rm adm}+\sup|B|)\) ((9.2), with the Euler-equation bound (9.1) for the current). For real \(B\) it is the representative of I1 at that datum.

Put \(r:=\min\{r_4,\ r_B/(2C_4)\}\) and \(V_0:=M^{\boldsymbol\cdot}(U_r)\). Fix one top-layer plaquette \(p\), or one top-layer bond \(b\). Define on \(\{\|w\|<r\}\)
\[
F(w):=\eta_n^{-2}\bigl(\partial\Phi_{V_0}(B(w))(p)-1\bigr)\quad\text{or}\quad F(w):=J\bigl(\Phi_{V_0}(B(w))\bigr)(b).
\]
By Steps 2–3, \(F\) is holomorphic and \(\|F\|\le H:=C_2(\varepsilon_{\rm adm}+r_B)\). This bound is crude; it has no factor \(\alpha_0'\). By definition of the analytic branch, \(U_n^{\mathfrak r}(Z;M^{\boldsymbol\cdot}(\mathbf U))=\Phi_{V_0}(B(sA'))\). So \(F(sA')\) is the quantity that (A2) bounds.

**Step 4: the three real points.**

*I1 (critical-orbit theorem at real data; CMP 102 Theorem 1; `a1-balaban.md` (8.2)).* There is \(B_1\) such that, for a real layered datum of radius \(\varepsilon\le\varepsilon_{\rm adm}\), on a tower whose gap obeys R1 of §7, the default problem has one regular critical orbit. In level-\(n\) units, at top-layer elements, its axial representative has \(\eta_n^{-2}|\partial U(p)-1|\le B_1\varepsilon\) and \(|J(U)(b)|\le B_1\varepsilon\). The bound is linear in \(\varepsilon\), and \(B_1\) is independent of depth, volume and datum.

*I3 (curvature of averages; CMP 98 (48); `a1-balaban.md` (3.6), §7.1).* If a real field has \(|\partial V-1|\le\delta\eta^2\) on \(Z\), with \(\delta\le\alpha_*\), then its level-\(q\) averages have plaquettes at most \(2\delta s^2t_q^2\), and \(2L^2\delta s^2t_q^2\) at a seam. Indeed (3.6) reads \(v_{m+1}\le L^2v_m+C(L^2v_m)^2\), and \(\delta\eta^2=\delta s^2L^{-2n}\). So the datum \(M^{\boldsymbol\cdot}(V)\) has radius at most \(C_3\delta s^2\), with \(C_3=2L^2\).

Apply I3 to \(U_r\), \(U_R\) and \(U_I\), with \(\delta=\alpha_0'\) and, by (4.3), \(\delta=C_s(\alpha_0'+\alpha_1'^2)\). The ceilings of §7 keep each datum radius below \(\varepsilon_{\rm adm}/2\). At \(w=sA_R\), the increment \(B(sA_R)\) is real, since \(e^{i\eta A_R}U_r\) is real; and \(\sup|B(sA_R)|\le C_4s\alpha_1'<r_B\). By orbit uniqueness and the unique axial gauge, \(\Phi_{V_0}(B(sA_R))\) is the real representative at the datum \(M^{\boldsymbol\cdot}(U_R)\). The same holds at \(sA_I\) and at \(0\). I1 then gives
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
