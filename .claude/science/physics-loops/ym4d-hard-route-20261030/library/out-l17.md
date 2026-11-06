lead: anthropic/claude-opus-5-5/max mac-mini-worker
lease_until: 2026-11-07T00:05Z

# Balaban's sentence CMP 109 (1.17) at complex pairs: a tower bound with a quadratic budget, and its proof

Draft for the owner. Nothing here is sent. This is research text. It claims no status.

**Who wrote this, and who checked what.** Claude Opus 5.5 (max effort) wrote this note on 2026-11-06. It distils one of our working notes (commit 9b22b3704 of our repository, LINK). Codex wrote the proofs of Proposition 1, Lemma 4, Corollary 2, Lemma 3 and the choice (5.4), and our derivations of the inputs (Appendix A). Claude checked each of these texts line by line, in one reading each. For Proposition 1 and Lemma 4 the first failing step was none. For Lemma 3 it was the claim that the auxiliary radii obey the ceilings of Proposition 1; the Stage-7 ceilings of §7 repair it. Claude wrote the working note. Codex checked it line by line in one reading and asked for repairs; the first was the matrix-norm comparison in (4.1). Codex applied them, and no model has read the repaired text again. Nobody has checked this distilled note. A check is one reading by one model. It is not an audit and not a human review.

**Sources.** Ethan Sussman and Levent Alpoge, with Claude and Codex as authors of their text: repository `ethanwsussman/Yang--Mills-LLM-experiment`, commit `31a47c543775`. CA-I, CA-II, CA-III are `theorem_0_complete_account_raw_{I,II,III}.tex`. "The outline" (SA) is `YM4_sketch_500.tex`. All numbers are source lines at that commit. Every passage cited was read in a copy fetched for this note.

**Credit.** Tadeusz Balaban, for every input: the averaging and gauge constructions of CMP 98 and 99, the flat propagator bounds of CMP 89, 95, 96 and 99b, the critical-orbit theorem of CMP 102 (Theorem 1, its continuation in §G, Proposition 9), and the regularity spaces and the sentence (1.17) of CMP 109. Sussman and Alpoge, with Claude and Codex: the two-rule hereditary class, the quadratic budget and the real-point argument (SA Theorem 5(a), mechanism 8), and the small-exponential argument with its auxiliary radii (SA (ER8)).

## 1. The use in your account, and its status

**The sentence.** CA-I 32599–32623 transcribes CMP 109 p. 263. Let \(\alpha_0'<\alpha_0\), \(\alpha_1'<\alpha_1\), and let \((\mathbf U,\mathbf J)\) satisfy (i)–(iii) of Balaban's regularity spaces at level \(j\) on \(X\), with \(\alpha_0',\alpha_1'\) in place of \(\alpha_0,\alpha_1\). The averages obey \(|\partial\bar{\mathbf U}^p-1|<2\alpha_0'(L^p\xi)^2\), and CMP 102 Proposition 9 then gives, on \(\tilde X^{-2}\),
\[ |\partial U_n(M^{\boldsymbol\cdot}(\mathbf U))-1|<2B_3\alpha_0'\xi^2,\qquad |J_n(M^{\boldsymbol\cdot}(\mathbf U))|<2B_3\alpha_0'(L^n\xi)^2 . \tag{1.17}\]
Balaban concludes that for \(\alpha_0'\) sufficiently small these estimates imply condition (iv) (CA-I 32613–32614). These primed radii are not the larger operator radii of CMP 116 (CA-I 32666–32670).

**The use.** `4.8:prop-small-pairs` (CA-I 34058–34218) assumes that "for every \((p,Z)\in\mathfrak T_j(X)\) … and every \(\mathfrak r\in\mathfrak R\), the estimate [CMP 109 (1.17)] holds at complex pairs, as stated on [p. 263]", with \(M/L\) and \(LB^{(109)}\) (CA-I 34067–34072). Its budget `4.8:eq-small-pairs-1` is \(\alpha_1'\le\alpha_1\), \(2B_3\alpha_0'\le\alpha_0\) (CA-I 34061–34062). Step 2 (CA-I 34147–34166) applies the hypothesis at \((\mu\alpha_0',\mu\alpha_1')\), \(\mu=L^{-(j-p)}\), and gets `4.8:eq-small-pairs-3`. The proposition is proved from this hypothesis. It reaches Theorem 0 through `4.19:prop-clause-zero` (CA-I 56419–56439): item (g) through membership (e) of `4.8:prop-class-reproduction` (CA-I 34241–34403), and item (c) through `4.7:not-true-pairs` (CA-I 29522–29605) and `4.7:prop-coupling-increment` (CA-I 32412–32491). One more use is the step "(i)–(iii) imply (iv)" of `5.2:lem-polydisc-containment` (CA-II 4381–4384). It applies the sentence at the target radii themselves.

**Status in your text.** CA-III chapter 13, list "(3, continued) Further sentences cited as printed at their use sites" (CA-III 111316–111317), lines 111326–111327:
`\item the inclusion sentence \cite[(1.17)]{B-CMP109}, read at complex pairs $\cdot$ Chapter~\ref{ch:4} $\cdot$ cited as printed at its use site`
CA-I 166588–166589, in the published statements of clause (0) ("Inputs used by statement", CA-I 166552):
`\item \cite[(1.17)]{B-CMP109}, the inclusion sentence, read at complex pairs --- printed without proof; cited as printed.`
CA-I 32703–32706 records the same for the complex sufficient condition and its special case.

## 2. What the outline already has, what is new, and why a change is needed

**Already in the outline.** SA Theorem 5(a) (SA 9746–9753) states the tower bound with \(K^\sharp(\alpha_0'+\alpha_1'^2)\) in place of \(2B_3\alpha_0'\), with the budget "once \(K^\sharp(\alpha_0'+\alpha_1'^2)\le\alpha_0\)". Mechanism 8 (SA 9899–9911) sketches its proof: the covariant curl of \(A'\) is small, and a Taylor inequality uses three real points. (ER7) (SA 6571–6584) assumes a uniform tower estimate of this form. The near-zero core inclusion (ER8) (SA 6586–6630) is proved from (ER7), with the auxiliary radii of (5.3).

**New here.** (1) A proof of the tower bound (Proposition 1) from Balaban's results, with constants free of depth, volume and \(\alpha_1'/\alpha_0'\). (2) The complete account still uses the linear budget \(2B_3\alpha_0'\le\alpha_0\) (CA-I 34061–34062 and 34819); Corollary 2 replaces it. (3) Lemma 3, the seed inclusions that the true-pair and polydisc arguments need, with the true current and with \(U^c_j\), and one choice of \(c_T\), (5.4). (4) A replacement for the polydisc step CA-II 4381–4384. (5) Two order-of-constants conditions, the gap-number floor and the Stage-7 ceilings (§7).

**Why the printed derivation does not give (1.17) at complex pairs.** The sentence asks for a bound linear in \(\alpha_0'\) alone, for every \(\alpha_1'\le\alpha_1\). Balaban's derivation goes through CMP 102 Proposition 9, which bounds the continued minimizer by the size of the datum increment. At a complex pair, the increment that \(A'\) adds to the averages is linear in \(\alpha_1'\). In level-\(n\) units, with \(s=L^n\xi_p\), the direct estimate is \(C(\alpha_0's^2+\alpha_1's)\). The clause needs a constant times \(s^2\), and the quotient keeps \(\alpha_1'/s\), which is unbounded as \(p-n\) grows. We know no proof of the original form, and no counterexample. It is open. We do not claim that Balaban's sentence is false. The hypotheses also allow \(\alpha_1'^2\gg\alpha_0'\): take \(U=1\) and a constant, commuting, complex potential in one direction. Every plaquette equals \(1\), so (i)–(iii) hold for every \(\alpha_0'>0\) at fixed \(\alpha_1'\). (Its tower curvature is zero, so it refutes nothing.) So the budget must carry the square.

## 3. The statements

Notation is that of CA-I 32834–33070: towers \(\boldsymbol\Omega^{\mathfrak r}(Z)\) under the rules \(\mathfrak R=\{\mathfrak r_1,\mathfrak r_2\}\), the layered average \(M^{\boldsymbol\cdot}\), the current \(J_n^{\mathfrak r}\) in level-\(n\) units, the two-layer interior \(Z^{\wr p}\), the labels \(\mathfrak T_j(X)\), the tower clause \((\mathrm{iv})^{\mathfrak r}_{p,Z}[c]\) and the class \(U^{\Sigma^1}_j\). The constants and their order are in §7.

**Proposition 1 (tower bound at complex pairs, with a quadratic budget).** There are constants \(K^\sharp\ge1\) and \(\bar\alpha_0',\bar\alpha_1'>0\) with the following property. They depend only on \(d=4\), \(N\), \(L\), \(\mathfrak M\) and the constants of the flat bounds, the averaging bounds and the critical-orbit theorem. They do not depend on \(p,n,Z,\mathfrak r\), the torus, \(M\), \(B^{(109)}\), or \(\alpha_1'/\alpha_0'\). Let the gap number \(R_1\) obey the gap-number floor of §7, and let \(M\ge 2LR_1M_1\). Let \(p\ge1\), \(Z\in\mathbf D_{p-1}\), \(\mathfrak r\in\mathfrak R\), \(0<\alpha_0'\le\bar\alpha_0'\) and \(0<\alpha_1'\le\bar\alpha_1'\). Let \(\mathbf U=U'U\) on the bonds of \(Z\), with \(U\) \(G\)-valued, \(U'=e^{i\xi_pA'}\), and
\[ |\partial U-1|<\alpha_0'\xi_p^2,\quad |\partial\mathbf U-1|<\alpha_0'\xi_p^2,\quad |A'|,\ |\nabla^{\xi_p}_UA'|<\alpha_1'\quad\text{on }Z. \tag{3.1}\]
Then for \(n=1,\dots,p\) the analytic tower branch \(U_n^{\mathfrak r}(Z;M^{\boldsymbol\cdot}(\mathbf U))\) exists, and on \(Z^{\wr p}\)
\[ |\partial U_n^{\mathfrak r}(Z;M^{\boldsymbol\cdot}(\mathbf U))-1|<K^\sharp(\alpha_0'+\alpha_1'^2)\,\xi_p^2,\qquad |J_n^{\mathfrak r}(Z;M^{\boldsymbol\cdot}(\mathbf U))|<K^\sharp(\alpha_0'+\alpha_1'^2)\,(L^n\xi_p)^2. \tag{3.2}\]
The same holds for \(U\) in place of \(\mathbf U\), with \(\alpha_1'=0\).

*Remarks.* (3.1) is CMP 109 (1.11), (1.13) and the first inequality of (1.14) at level \(p\). The cube gauge (1.12) and the current bound \(|\mathbf J|<\gamma_0\) are not used; a consumer that has them loses nothing. For real data, \(U_n^{\mathfrak r}\) is the axial representative of the unique regular critical orbit. For complex data it is the holomorphic continuation of that representative in the datum (§9). All bounds in (3.1) are read on the complete read sets: local differences, currents and averages use their full stencils and carriers, outward rows included.

**Corollary 2 (`4.8:prop-small-pairs` under the quadratic budget).** In `4.8:prop-small-pairs`, replace the hypothesis at CA-I 34067–34072 by Proposition 1, and `4.8:eq-small-pairs-1` by
\[ \alpha_1'\le\alpha_1,\qquad K^\sharp(\alpha_0'+\alpha_1'^2)\le\alpha_0,\qquad \alpha_0'\le\bar\alpha_0',\quad\alpha_1'\le\bar\alpha_1'. \tag{3.3}\]
Keep every other hypothesis. Then `4.8:eq-small-pairs-2` holds: \((\mathbf U,\mathbf J)\in U^{\Sigma^1}_j(X;\alpha_0,\alpha_1,\gamma_0)\). Its last paragraph, on the real minimal configurations of CMP 109 p. 263, holds with \(K^\sharp\alpha_0'\le\alpha_0\).

**Lemma 3 (unit-base seeds).** Let \(0<\alpha_0,\alpha_1\le1\) obey the Stage-7 ceilings
\[ \alpha_0\le 4K^\sharp\bar\alpha_0',\qquad \alpha_1\le 2\bar\alpha_1'. \tag{3.4}\]
There is \(c_*>0\), depending only on \(K^\sharp\), \(d\) and \(N\), with the following property. Put \(r:=c_*\min(\alpha_0,\alpha_1)\). Let \(j\ge1\), \(X\in\mathbf D_{j-1}\), and let \(A\) be a \(\mathfrak g^c\)-valued bond field on \(X\) with \(|A|,|\nabla^{\xi_j}A|\le r\), read on the complete stencils.
- (a) If \(|\mathbf J|\le r\), then \((e^{i\xi_jA},\mathbf J)\in U^{\Sigma^1}_j(X;\alpha_0,\alpha_1)\).
- (b) If \(|\partial^*\partial A|\le r\), then the true pair \((e^{i\xi_jA},J(e^{i\xi_jA}))\in U^{\Sigma^1}_j(X;\alpha_0,\alpha_1)\).
- (c) If \(X\in\mathbf D_j\), the pairs of (a) and (b) also lie in \(U^c_j(X,\alpha_0,\alpha_1)\).

The constant \(c_*\) does not depend on \(\alpha_0,\alpha_1\), \(j\), \(X\), the volume or the coupling.

**The choice of \(c_T\).** In `4.7:eq-true-pairs-a` (CA-I 29529–29535), take \(c_T\) as in (5.4) below. Then Lemma 3 gives `4.7:not-true-pairs` (a), (b) and the polydisc step of `5.2:lem-polydisc-containment` (§5).

