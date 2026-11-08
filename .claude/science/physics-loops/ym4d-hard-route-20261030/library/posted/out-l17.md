lead: anthropic/claude-opus-5-5/max mac-mini-worker
lease_until: 2026-11-07T00:05Z

# Balaban's sentence CMP 109 (1.17) at complex pairs: a tower bound with a quadratic budget, and its proof

Draft, not yet sent. This is research text. It claims no status.

**Who wrote this, and who checked what.** Claude distilled this note on 2026-11-06 from Codex's working derivation ([wu-l17.md](wu-l17.md)). Codex wrote the proofs of Proposition 1, Lemma 4, Corollary 2, Lemma 3 and the choice (5.4), and the repository derivations of the inputs listed in §8. Claude checked each of those component texts line by line, once each; the component checks and their repairs are listed with the suppliers in §8 and Appendix A. Codex checked the working note line by line and asked for repairs, which were applied; the repaired working note was not then checked again as a whole. Codex (gpt-6-astra) then checked this outward version line by line ([out-l17-check.md](../gates/out-l17-check.md)), and its edits are applied here. This records model review of a conditional argument. It is not a proof of Theorem 0, not a new check of every supplier derivation, not an audit and not a human review.

**Sources.** Your repository `ethanwsussman/Yang--Mills-LLM-experiment`, commit `31a47c543775`. CA-I, CA-II, CA-III are `theorem_0_complete_account_raw_{I,II,III}.tex`. "The outline" (SA) is `YM4_sketch_500.tex`. All numbers are source lines at that commit. Every passage cited was read in a copy fetched for this note.

**Credit.** Tadeusz Balaban, for every input: the averaging and gauge constructions of CMP 98 and 99, the flat propagator bounds of CMP 89, 95, 96 and 99b, the critical-orbit theorem of CMP 102 (Theorem 1, its continuation in §G, Proposition 9), and the regularity spaces and the sentence (1.17) of CMP 109. The two-rule hereditary class, the quadratic budget, the real-point argument (SA Theorem 5(a), mechanism 8) and the small-exponential argument with its auxiliary radii (SA (ER8)) are yours; this note uses them.

## 1. The use in your account, and its status

**The sentence.** CA-I 32599–32623 transcribes CMP 109 p. 263. Let $`\alpha_0'<\alpha_0`$, $`\alpha_1'<\alpha_1`$, and let $`(\mathbf U,\mathbf J)`$ satisfy (i)–(iii) of Balaban's regularity spaces at level $`j`$ on $`X`$, with $`\alpha_0',\alpha_1'`$ in place of $`\alpha_0,\alpha_1`$. The averages obey $`|\partial\bar{\mathbf U}^p-1|<2\alpha_0'(L^p\xi)^2`$, and CMP 102 Proposition 9 then gives, on $`\tilde X^{-2}`$,

```math
|\partial U_n(M^{\boldsymbol\cdot}(\mathbf U))-1|<2B_3\alpha_0'\xi^2,\qquad |J_n(M^{\boldsymbol\cdot}(\mathbf U))|<2B_3\alpha_0'(L^n\xi)^2 . \tag{1.17}
```

Balaban concludes that for $`\alpha_0'`$ sufficiently small these estimates imply condition (iv) (CA-I 32613–32614). These primed radii are not the larger operator radii of CMP 116 (CA-I 32666–32670).

**The use.** `4.8:prop-small-pairs` (CA-I 34058–34218) assumes that "for every $`(p,Z)\in\mathfrak T_j(X)`$ … and every $`\mathfrak r\in\mathfrak R`$, the estimate [CMP 109 (1.17)] holds at complex pairs, as stated on [p. 263]", with $`M/L`$ and $`LB^{(109)}`$ (CA-I 34067–34072). Its budget `4.8:eq-small-pairs-1` is $`\alpha_1'\le\alpha_1`$, $`2B_3\alpha_0'\le\alpha_0`$ (CA-I 34061–34062). Step 2 (CA-I 34147–34166) applies the hypothesis at $`(\mu\alpha_0',\mu\alpha_1')`$, $`\mu=L^{-(j-p)}`$, and gets `4.8:eq-small-pairs-3`. The proposition is proved from this hypothesis. It reaches Theorem 0 through `4.19:prop-clause-zero` (CA-I 56419–56439): item (g) through membership (e) of `4.8:prop-class-reproduction` (CA-I 34241–34403), and item (c) through `4.7:not-true-pairs` (CA-I 29522–29605) and `4.7:prop-coupling-increment` (CA-I 32412–32491). One more use is in `5.2:lem-polydisc-containment`: at CA-II 4378–4384 its proof takes the radii of the sufficient condition equal to the target radii and writes that "the estimates (i)--(iii) imply condition (iv)" (CA-II 4383). The small-pairs budget does not permit that invocation at equal radii. This is a gap in the inference, not a counterexample to the lemma.

**Status in your text.** The closing list of CA-III, "Statements used without proof in this account" (label `ch:13`, CA-III 111167), item "(3, continued) Further sentences cited as printed at their use sites, not counted among those above" (CA-III 111315–111316), lines 111326–111327:
`\item the inclusion sentence \cite[(1.17)]{B-CMP109}, read at complex pairs $\cdot$ Chapter~\ref{ch:4} $\cdot$ cited as printed at its use site`
CA-I 166588–166589, in the published statements of clause (0) ("Inputs used by statement", CA-I 166552):
`\item \cite[(1.17)]{B-CMP109}, the inclusion sentence, read at complex pairs --- printed without proof; cited as printed.`
CA-I 32703–32706 records the same for the complex sufficient condition and its special case.

## 2. What the outline already has, what is new, and why a change is needed

**Already in the outline.** SA Theorem 5(a) (SA 9746–9753) states the tower bound with $`K^\sharp(\alpha_0'+\alpha_1'^2)`$ in place of $`2B_3\alpha_0'`$, with the budget "once $`K^\sharp(\alpha_0'+\alpha_1'^2)\le\alpha_0`$". Mechanism 8 (SA 9899–9911) sketches its proof: the covariant curl of $`A'`$ is small, and a Taylor inequality uses three real points. (ER7) (SA 6571–6584) assumes a uniform tower estimate of this form. The near-zero core inclusion (ER8) (SA 6586–6630) is proved from (ER7), with the auxiliary radii of (5.3).

**What this note adds.** This note implements the outline's Theorem 5(a) and mechanism 8 in the complete account's notation. The quadratic budget is already stated at SA 9753, and the unit-base inclusion with these exact auxiliary radii is proved conditional on ER7 at SA 6586–6630 (radii at SA 6615–6627). The additions here are explicit constants, the current-remainder specialization, the consumer dictionary, the replacement of the equal-radius inference at CA-II 4378–4384, and compatibility checks for the choices of gap and target radii. Proposition 1 remains conditional on the input estimates listed in §8; Appendix A summarizes their derivations. This compares our text with the cited texts; it claims no priority.

**Why the printed derivation does not give (1.17) at complex pairs.** The sentence asks for a bound linear in $`\alpha_0'`$ alone, for every $`\alpha_1'\le\alpha_1`$. Balaban's derivation goes through CMP 102 Proposition 9, which bounds the continued minimizer by the size of the datum increment. At a complex pair, the increment that $`A'`$ adds to the averages is linear in $`\alpha_1'`$. In level-$`n`$ units, with $`s=L^n\xi_p`$, the direct estimate is $`C(\alpha_0's^2+\alpha_1's)`$. The clause needs a constant times $`s^2`$, and the quotient keeps $`\alpha_1'/s`$, which is unbounded as $`p-n`$ grows. We know no proof of the original form, and no counterexample. It is open. We do not claim that Balaban's sentence is false. The hypotheses also allow $`\alpha_1'^2\gg\alpha_0'`$: take $`U=1`$ and a constant, commuting, complex potential in one direction. Every plaquette equals $`1`$, so (i)–(iii) hold for every $`\alpha_0'>0`$ at fixed $`\alpha_1'`$. (Its tower curvature is zero, so it refutes nothing.) The quadratic budget is sufficient for this argument. Failure of the direct linear estimate does not refute the printed curvature-only claim or prove that a quadratic term is necessary in every proof. Your outline already explains this loss of scale (SA 9911), and your account records the potential-sized limitation (CA-I 15942–15951, 155492–155507).

## 3. The statements

Notation is that of CA-I 32834–33070: towers $`\boldsymbol\Omega^{\mathfrak r}(Z)`$ under the rules $`\mathfrak R=\{\mathfrak r_1,\mathfrak r_2\}`$, the layered average $`M^{\boldsymbol\cdot}`$, the current $`J_n^{\mathfrak r}`$ in level-$`n`$ units, the two-layer interior $`Z^{\wr p}`$, the labels $`\mathfrak T_j(X)`$, the tower clause $`(\mathrm{iv})^{\mathfrak r}_{p,Z}[c]`$ and the class $`U^{\Sigma^1}_j`$. The constants and their order are in §7.

**Scope and inputs.** The supplied derivations are checked here for SU(2), with the default convention that omits inward bonds. The notation retains $`N`$ to display matrix-norm dependence; no checked extension of the input package to general SU(N) is claimed. All statements inherit the account's tower, collar and admissible-torus hypotheses, including the earlier $`L`$ and $`R_1`$ floors (CA-I 32925; SA 9658). Proposition 1 is an implication from the uniform averaging, continued-current, real critical-orbit, real-average-curvature and flat estimates specified in §8. The identification with the published minimal configuration remains the cited identification described in §9.

**Proposition 1 (the outline's quadratic tower bound at complex pairs).** There are constants $`K^\sharp\ge1`$ and $`\bar\alpha_0',\bar\alpha_1'>0`$ with the following property. They depend only on $`d=4`$, $`N`$, $`L`$, $`\mathfrak M`$ and the constants of the flat bounds, the averaging bounds and the critical-orbit theorem. They do not depend on $`p,n,Z,\mathfrak r`$, the torus, $`M`$, $`B^{(109)}`$, or $`\alpha_1'/\alpha_0'`$. Let the gap number $`R_1`$ obey the gap-number floor of §7, and let $`M\ge 2LR_1M_1`$. Let $`p\ge1`$, $`Z\in\mathbf D_{p-1}`$, $`\mathfrak r\in\mathfrak R`$, $`0<\alpha_0'\le\bar\alpha_0'`$ and $`0<\alpha_1'\le\bar\alpha_1'`$. Let $`\mathbf U=U'U`$ on the bonds of $`Z`$, with $`U`$ $`G`$-valued, $`U'=e^{i\xi_pA'}`$, and

```math
|\partial U-1|<\alpha_0'\xi_p^2,\quad |\partial\mathbf U-1|<\alpha_0'\xi_p^2,\quad |A'|,\ |\nabla^{\xi_p}_UA'|<\alpha_1'\quad\text{on }Z. \tag{3.1}
```

Then for $`n=1,\dots,p`$ the analytic tower branch $`U_n^{\mathfrak r}(Z;M^{\boldsymbol\cdot}(\mathbf U))`$ exists, and on $`Z^{\wr p}`$

```math
|\partial U_n^{\mathfrak r}(Z;M^{\boldsymbol\cdot}(\mathbf U))-1|<K^\sharp(\alpha_0'+\alpha_1'^2)\,\xi_p^2,\qquad |J_n^{\mathfrak r}(Z;M^{\boldsymbol\cdot}(\mathbf U))|<K^\sharp(\alpha_0'+\alpha_1'^2)\,(L^n\xi_p)^2. \tag{3.2}
```

The same holds for $`U`$ in place of $`\mathbf U`$, with $`\alpha_1'=0`$.

*Remarks.* (3.1) is CMP 109 (1.11), (1.13) and the first inequality of (1.14) at level $`p`$. The cube gauge (1.12) and the current bound $`|\mathbf J|<\gamma_0`$ are not used; a consumer that has them loses nothing. For real data, $`U_n^{\mathfrak r}`$ is the axial representative of the unique regular critical orbit. For complex data it is the holomorphic continuation of that representative in the datum (§9). All bounds in (3.1) are read on the complete read sets: local differences, currents and averages use their full stencils and carriers, outward rows included.

**Corollary 2 (`4.8:prop-small-pairs` under the quadratic budget).** In `4.8:prop-small-pairs`, replace the hypothesis at CA-I 34067–34072 by Proposition 1, and `4.8:eq-small-pairs-1` by

```math
\alpha_1'\le\alpha_1,\qquad K^\sharp(\alpha_0'+\alpha_1'^2)\le\alpha_0,\qquad \alpha_0'\le\bar\alpha_0',\quad\alpha_1'\le\bar\alpha_1'. \tag{3.3}
```

Keep every other hypothesis. Then `4.8:eq-small-pairs-2` holds: $`(\mathbf U,\mathbf J)\in U^{\Sigma^1}_j(X;\alpha_0,\alpha_1,\gamma_0)`$. Its last paragraph, on the real minimal configurations of CMP 109 p. 263, holds with $`K^\sharp\alpha_0'\le\alpha_0`$.

**Lemma 3 (unit-base seeds).** Let $`0<\alpha_0,\alpha_1\le1`$ obey the Stage-7 ceilings

```math
\alpha_0\le 4K^\sharp\bar\alpha_0',\qquad \alpha_1\le 2\bar\alpha_1'. \tag{3.4}
```

There is $`c_*>0`$, depending only on $`K^\sharp`$, $`d`$ and $`N`$, with the following property. Put $`r:=c_*\min(\alpha_0,\alpha_1)`$. Let $`j\ge1`$, $`X\in\mathbf D_{j-1}`$, and let $`A`$ be a $`\mathfrak g^c`$-valued bond field on $`X`$ with $`|A|,|\nabla^{\xi_j}A|\le r`$, read on the complete stencils and carriers of every difference, current and average, including outward rows.
- (a) If $`|\mathbf J|\le r`$, then $`(e^{i\xi_jA},\mathbf J)\in U^{\Sigma^1}_j(X;\alpha_0,\alpha_1)`$.
- (b) If $`|\partial^*\partial A|\le r`$, then the true pair $`(e^{i\xi_jA},J(e^{i\xi_jA}))\in U^{\Sigma^1}_j(X;\alpha_0,\alpha_1)`$.
- (c) If $`X\in\mathbf D_j`$, the pairs of (a) and (b) also lie in $`U^c_j(X,\alpha_0,\alpha_1)`$.

The constant $`c_*`$ does not depend on $`\alpha_0,\alpha_1`$, $`j`$, $`X`$, the volume or the coupling.

**The choice of $`c_T`$.** In `4.7:eq-true-pairs-a` (CA-I 29529–29535), take $`c_T`$ as in (5.4) below. Then Lemma 3 gives `4.7:not-true-pairs` (a), (b) and the polydisc step of `5.2:lem-polydisc-containment` (§5).

## 4. Proof of Proposition 1

Each input is named where it is used. §8 gives the Balaban result behind each one, and its status.

**Lemma 4 (real-point Taylor inequality).** Let $`F`$ be holomorphic on the ball of radius $`r`$ of a complex normed space, valued in a complex Banach space, with $`\|F\|\le H`$ there. Suppose $`w\mapsto w_R`$ and $`w\mapsto w_I`$, with $`w=w_R+iw_I`$, have norm at most one. If $`t:=\|w\|\le r/2`$, then $`\|F(w)\|\le\|F(w_R)\|+\|F(w_I)\|+\|F(0)\|+6Ht^2/r^2`$.

*Proof.* Write $`F(x)=F(0)+DF(0)x+R(x)`$. On the complex line $`\zeta\mapsto F(\zeta x/\|x\|)`$, $`|\zeta|<r`$, Cauchy's estimate bounds the degree-$`m`$ term of $`F`$ at $`x`$ by $`H(\|x\|/r)^m`$. The sum over $`m\ge2`$ gives $`\|R(x)\|\le H(\|x\|/r)^2/(1-\|x\|/r)\le2H\|x\|^2/r^2`$ for $`\|x\|\le r/2`$. This applies at $`x=w,w_R,w_I`$, whose norms are at most $`t`$. Since $`DF(0)`$ is complex linear, $`DF(0)w=DF(0)w_R+iDF(0)w_I`$. Hence $`F(w)=F(w_R)+iF(w_I)-iF(0)+R(w)-R(w_R)-iR(w_I)`$, and the triangle inequality gives the claim. $`\square`$

**Setting.** Fix $`p,Z,\mathfrak r`$ and $`1\le n\le p`$. Put $`\eta:=\xi_p`$, $`s:=L^n\xi_p=L^{n-p}\in(0,1]`$ and $`\eta_n:=L^{-n}=\eta/s`$. *Level-$`n`$ units* rescale lengths by $`1/s`$: the fine spacing becomes $`\eta_n`$, a level-$`q`$ block has length $`t_q:=L^{q-n}\le1`$, and the top layer has scale $`1`$. A field $`a`$ at spacing $`\eta`$ becomes $`w=sa`$ at spacing $`\eta_n`$, since $`e^{i\eta a}=e^{i\eta_nw}`$. Its norm is $`\|w\|:=\max(\sup|w|,\sup|\nabla^{\eta_n}_Uw|)=\max(s|a|,s^2|\nabla^\eta_Ua|)`$. By (3.1), $`\|sA'\|\le s\alpha_1'`$. Write $`U_r:=U`$, so $`\mathbf U=e^{i\eta A'}U_r`$. In level-$`n`$ units the two bounds of (3.2) read $`\eta_n^{-2}|\partial U_n^{\mathfrak r}-1|<K^\sharp(\alpha_0'+\alpha_1'^2)s^2`$ and $`|J_n^{\mathfrak r}|<K^\sharp(\alpha_0'+\alpha_1'^2)s^2`$.

**Step 1: the covariant curl of $`A'`$ is small (SA 9905–9909).** Use the normalized Hilbert-Schmidt norm $`|X|=(\operatorname{tr}X^*X)^{1/2}`$, $`\operatorname{tr}1=1`$, and write $`\|X\|_{\rm op}`$ for the operator norm. By CA-I 10306, $`|X|\le\|X\|_{\rm op}\le b|X|`$, with $`b:=\sqrt N`$. Let $`p`$ be a plaquette with bonds $`b_1,\dots,b_4`$ as in CA-I 10333–10345, so $`\partial V(p)=V(b_1)V(b_2)V(b_3)^{-1}V(b_4)^{-1}`$ and $`(D_UA)(p)=\eta^{-1}(A_1+R(U_1)A_2-R(U_4)A_3-A_4)`$. Move each exponential of $`\mathbf U`$ to the first corner:

```math
\partial\mathbf U(p)=e^{X_1}e^{X_2}e^{X_3}e^{X_4}\,\partial U_r(p),\quad X_1=i\eta A_1',\ X_2=i\eta R(U_1)A_2',\ X_3=-i\eta R(U_1U_2U_3^{-1})A_3',\ X_4=-i\eta R(\partial U_r(p))A_4'.
```

The transports are unitary, so $`\|X_\nu\|_{\rm op}\le b\eta|A'|`$. The terms of the product of total degree at least two sum in operator norm to at most $`e^{4b\eta|A'|}-1-4b\eta|A'|\le8b^2e^{4b}\eta^2|A'|^2`$, since $`\eta\alpha_1'\le1`$. Write $`P:=\partial U_r(p)`$. The transports of $`A_3'`$ and $`A_4'`$ differ from those of $`D_{U_r}`$ by $`R(P)`$. For unitary $`P`$, $`\|R(P)Y-Y\|_{\rm op}\le2\|P-1\|_{\rm op}\|Y\|_{\rm op}\le2b^2|P-1|\,|Y|`$. So the two differences cost at most $`4b^2\eta^3\alpha_0'\alpha_1'`$. Hence

```math
\partial\mathbf U(p)\,\partial U_r(p)^{-1}=1+i\eta^2(D_{U_r}A')(p)+E,\qquad \|E\|_{\rm op}\le8b^2e^{4b}\eta^2\alpha_1'^2+4b^2\eta^3\alpha_0'\alpha_1'. \tag{4.1}
```

Since $`\partial U_r(p)`$ is unitary, $`\|\partial\mathbf U\,\partial U_r^{-1}-1\|_{\rm op}=\|\partial\mathbf U-\partial U_r\|_{\rm op}<2b\alpha_0'\eta^2`$ by (3.1). With (4.1) and $`|E|\le\|E\|_{\rm op}`$, a larger fixed $`C_s=C_s(d,N)`$ gives

```math
|D_{U_r}A'|\le C_s(\alpha_0'+\alpha_1'^2). \tag{4.2}
```

Write $`A'=A_R+iA_I`$ with $`A_R,A_I`$ Hermitian. Because $`U_r`$ is unitary, $`R(U_r)`$ commutes with the adjoint, so $`D_{U_r}`$ and $`\nabla_{U_r}`$ commute with both projections. So $`|D_{U_r}A_R|,|D_{U_r}A_I|\le|D_{U_r}A'|`$, and $`|A_R|,|A_I|,|\nabla_{U_r}A_R|,|\nabla_{U_r}A_I|<\alpha_1'`$. Apply (4.1) to $`A_R`$ and to $`A_I`$. The real fields $`U_R:=e^{i\eta A_R}U_r`$ and $`U_I:=e^{i\eta A_I}U_r`$ are $`G`$-valued, and

```math
|\partial U_R-1|,\ |\partial U_I-1|\le C_s(\alpha_0'+\alpha_1'^2)\,\eta^2 . \tag{4.3}
```

This uses only $`|A'|<\alpha_1'`$ and the two curvature bounds, with no bound on $`\nabla A'`$. The same $`C_s(d,N)`$ covers (4.2)–(4.3); it does not depend on depth, mesh, volume or the radius ratio.

**Step 2: the datum increment is linear in $`\|w\|`$, uniformly in depth.** For a complex field $`w`$ define $`B(w)`$ on the data sets of the tower by $`M^{\boldsymbol\cdot}(e^{i\eta_nw}U_r)=e^{iB(w)}M^{\boldsymbol\cdot}(U_r)`$.

*The averaging bound (Balaban CMP 98, Propositions 2, 4, 5; Appendix A.1).* There are $`r_4>0`$ and $`C_4`$, depending on $`L`$, $`\mathfrak M`$ and the averaging constants only, such that $`B`$ is holomorphic on $`\{\|w\|<r_4\}`$ and $`\sup|B(w)|\le C_4\|w\|`$ there, for every real $`U_r`$ with $`|\partial U_r-1|\le\alpha_0'\eta^2`$, $`\alpha_0'\le\bar\alpha_0'`$.

The depth count is this. The straightened relative angles $`b_q`$ of the level-$`q`$ average obey $`b_{q+1}\le L(1+C\alpha_0't_q^2)b_q+C_Lb_q^2`$, $`b_0\le\eta_n|w|`$. Put $`\beta_q:=b_q/t_q`$, so $`\beta_0\le|w|`$. While $`\beta_q\le2|w|`$, $`\beta_{q+1}\le\beta_q(1+C\alpha_0't_q^2+2C_L'|w|t_q)`$. Since $`\sum_qt_q^2\le(1-L^{-2})^{-1}`$ and $`\sum_qt_q\le(1-L^{-1})^{-1}`$, the product of these factors is at most $`2`$ once $`\alpha_0'`$ and $`|w|`$ are below fixed ceilings. By induction on $`q`$ (first exit), $`\beta_q\le2|w|`$ for all $`q\le n`$. The endpoint (node) factors obey the same summable first-power bound. So $`\sup|B(w)|\le C_4\|w\|`$, with no factor that depends on $`n`$ or $`p`$. $`B`$ is holomorphic because it is a finite composition of products, inverses and convergent logarithm series. A recursion on the plain angles with coefficient $`L`$ would be false (the endpoint sums are of order $`dL`$); it is not used.

**Step 3: one holomorphic function and its crude bound.**

*The continuation bound (Balaban CMP 102 §G; Appendix A.2).* There are $`r_B>0`$, $`\varepsilon_{\rm adm}>0`$ and $`C_2`$ with the following property. Let $`V_0`$ be a real layered datum of datum radius at most $`\varepsilon_{\rm adm}/2`$. Then $`B\mapsto\Phi_{V_0}(B)`$, the axial representative at the datum $`e^{iB}V_0`$, is holomorphic on $`\{\sup|B|<r_B\}`$. In level-$`n`$ units, at every top-layer plaquette $`p`$ and bond $`b`$, $`\eta_n^{-2}|\partial\Phi_{V_0}(B)(p)-1|`$ and $`|J(\Phi_{V_0}(B))(b)|`$ are at most $`C_2(\varepsilon_{\rm adm}+\sup|B|)`$. For real $`B`$ it is the representative of the orbit bound (Step 4) at that datum.

Put $`r:=\min\{r_4,\ r_B/(2C_4)\}`$ and $`V_0:=M^{\boldsymbol\cdot}(U_r)`$. Fix one top-layer plaquette $`p`$ or one top-layer bond $`b`$, and define on $`\{\|w\|<r\}`$

```math
F(w):=\eta_n^{-2}\bigl(\partial\Phi_{V_0}(B(w))(p)-1\bigr)\quad\text{or}\quad F(w):=J\bigl(\Phi_{V_0}(B(w))\bigr)(b).
```

By Steps 2–3, $`F`$ is holomorphic and $`\|F\|\le H:=C_2(\varepsilon_{\rm adm}+r_B)`$. This bound is crude: it has no factor $`\alpha_0'`$. By definition of the analytic branch, $`U_n^{\mathfrak r}(Z;M^{\boldsymbol\cdot}(\mathbf U))=\Phi_{V_0}(B(sA'))`$. So $`F(sA')`$ is the quantity that (3.2) bounds.

**Step 4: the three real points.**

*The orbit bound (Balaban CMP 102 Theorem 1).* There is $`B_{\rm o}`$ (our constant, not the $`B_1`$ of CA-I 1510) such that, for a real layered datum of radius $`\varepsilon\le\varepsilon_{\rm adm}`$, on a tower whose gap obeys the gap-number floor of §7, the default problem has one regular critical orbit. In level-$`n`$ units, at top-layer elements, its axial representative has $`\eta_n^{-2}|\partial U(p)-1|\le B_{\rm o}\varepsilon`$ and $`|J(U)(b)|\le B_{\rm o}\varepsilon`$. The bound is linear in $`\varepsilon`$, and $`B_{\rm o}`$ does not depend on depth, volume or datum.

*The curvature bound for averages (Balaban CMP 98 (48), (54); CMP 102 (160)).* If a real field has $`|\partial V-1|\le\delta\eta^2`$ on $`Z`$, with $`\delta\le\alpha_*`$, then its level-$`q`$ averages have plaquettes at most $`2\delta s^2t_q^2`$, and $`2L^2\delta s^2t_q^2`$ at a seam. Indeed the plaquette recursion is $`v_{m+1}\le L^2v_m+C(L^2v_m)^2`$, and $`\delta\eta^2=\delta s^2L^{-2n}`$. So the datum $`M^{\boldsymbol\cdot}(V)`$ has radius at most $`C_3\delta s^2`$, with $`C_3=2L^2`$.

Apply the curvature bound to $`U_r`$, $`U_R`$ and $`U_I`$, with $`\delta=\alpha_0'`$ and, by (4.3), $`\delta=C_s(\alpha_0'+\alpha_1'^2)`$. The ceilings of §7 keep each datum radius below $`\varepsilon_{\rm adm}/2`$. At $`w=sA_R`$ the increment $`B(sA_R)`$ is real, since $`e^{i\eta A_R}U_r`$ is real, and $`\sup|B(sA_R)|\le C_4s\alpha_1'<r_B`$. By orbit uniqueness and the unique axial gauge, $`\Phi_{V_0}(B(sA_R))`$ is the real representative at the datum $`M^{\boldsymbol\cdot}(U_R)`$. The same holds at $`sA_I`$ and at $`0`$. The orbit bound then gives

```math
\|F(0)\|,\ \|F(sA_R)\|,\ \|F(sA_I)\|\le C_{\rm R}(\alpha_0'+\alpha_1'^2)\,s^2,\qquad C_{\rm R}:=B_{\rm o}C_3\max\{1,C_s\}. \tag{4.4}
```

Curvature and current norms are invariant under unitary gauges, so the choice of representative does not matter here.

**Step 5: conclusion.** The projections $`w\mapsto w_R,w_I`$ have norm at most one for $`\|\cdot\|`$: the adjoint preserves the matrix norm, and $`\nabla_{U_r}`$ commutes with it. Here $`(sA')_R=sA_R`$, $`(sA')_I=sA_I`$, and $`t:=\|sA'\|\le s\alpha_1'\le r/2`$ by the ceiling $`\alpha_1'\le r/2`$. Lemma 4 and (4.4) give

```math
\|F(sA')\|\le3C_{\rm R}(\alpha_0'+\alpha_1'^2)s^2+6Hs^2\alpha_1'^2/r^2\le K(\alpha_0'+\alpha_1'^2)\,s^2,\qquad K:=3C_{\rm R}+6H/r^2 .
```

For the current this is the second bound of (3.2) with $`K`$. For the plaquette, multiply by $`\eta_n^2`$ and use $`\eta_n^2s^2=\eta^2`$: this is the first bound. Put $`K^\sharp:=2\max\{K,1\}`$. Since $`\alpha_0'>0`$, the bounds are strict with $`K^\sharp`$. $`K`$ is built from $`B_{\rm o},C_3,C_s,C_2,\varepsilon_{\rm adm},r_B,r_4,C_4`$. None of these depends on $`\alpha_1'/\alpha_0'`$, $`p,n,Z,\mathfrak r`$, the torus, $`M`$ or $`B^{(109)}`$.

**Step 6: the interior, and the real factor.** Steps 3–5 hold at top-layer elements of $`\Omega_n^{\mathfrak r}(Z)`$. By `4.8:eq-tower-rules-b` (CA-I 32921–32929), every point of $`Z`$ at distance more than $`R_1M_1L^n`$ steps from $`Z^c`$ lies in $`\Omega_n^{\mathfrak r}(Z)`$. A point of $`Z^{\wr p}`$ lies at least two $`\pi_{p-1}`$-cubes, that is $`2ML^{p-1}\ge4R_1M_1L^p\ge4R_1M_1L^n`$ steps, from $`Z^c`$, by $`M\ge2LR_1M_1`$. So $`Z^{\wr p}`$, with the one-step stencils of the plaquettes and of the current, lies in the top layer. This is CA-I 34177–34189, for both rules. Finally, $`A'=0`$ gives $`\mathbf U=U_r`$ and the bound $`K^\sharp\alpha_0'`$. $`\square`$

## 5. Proofs of Corollary 2 and Lemma 3, and the choice of $`c_T`$

**Proof of Corollary 2.** Fix $`(p,Z)\in\mathfrak T_j(X)`$ and $`\mathfrak r\in\mathfrak R`$, and put $`\mu:=L^{-(j-p)}\le1`$. Step 1 of CA-I 34107–34145 is unchanged. By the change of units `4.8:eq-restriction-units-a` (`4.8:thm-restriction-units`, CA-I 33276), the pair obeys (3.1) at level $`p`$ on $`Z`$ with the radii $`(\mu\alpha_0',\mu\alpha_1')`$: $`\alpha_0'\xi_j^2=\mu^2\alpha_0'\xi_p^2\le\mu\alpha_0'\xi_p^2`$, and $`A'^\flat=\mu A'`$ has $`|A'^\flat|=\mu|A'|`$, $`|\nabla^{\xi_p}A'^\flat|=\mu^2|\nabla^{\xi_j}A'|\le\mu|\nabla^{\xi_j}A'|`$. By (3.3) and $`\mu\le1`$, $`\mu\alpha_i'\le\bar\alpha_i'`$. Proposition 1 at these radii replaces Step 2: on $`Z^{\wr p}`$ the two bounds hold with the coefficient

```math
K^\sharp(\mu\alpha_0'+\mu^2\alpha_1'^2)\le\mu\,K^\sharp(\alpha_0'+\alpha_1'^2)\le\mu\alpha_0=\alpha_0L^{-(j-p)} . \tag{5.1}
```

For $`U`$, Proposition 1 gives $`K^\sharp\mu\alpha_0'\le\mu\alpha_0`$ (Step 3). The geometry of Step 4 is part of Proposition 1. So $`(\mathrm{iv})^{\mathfrak r}_{p,Z}[\alpha_0L^{-(j-p)}]`$ holds at every label and rule; this is $`(\mathrm{iv})^{\Sigma^1}`$. Conditions (i)–(iii) hold at $`(\alpha_0,\alpha_1,\gamma_0)`$ because $`\alpha_0'\le K^\sharp\alpha_0'\le\alpha_0`$ and $`\alpha_1'\le\alpha_1`$. Hence `4.8:eq-small-pairs-2`. $`\square`$

The new term $`\mu^2\alpha_1'^2`$ is at most $`\mu\alpha_1'^2`$, so the square has the one-power scaling of the class. Your remark at CA-I 34211–34218 makes the same point for a linear $`\alpha_1'`$ term. What needed proof was the budget, not the scaling.

**Proof of Lemma 3.** Matrix norms are those of CA-I 10306; the operator norm is at most $`b:=\sqrt N`$ times the normalized Hilbert-Schmidt norm.

*Plaquettes of a small exponential.* Let $`\xi\le1`$, $`r\le1`$ and $`|A|,|\nabla^\xi A|\le r`$. With real factor $`1`$, $`\partial e^{i\xi A}(p)=e^{i\xi A_1}e^{i\xi A_2}e^{-i\xi A_3}e^{-i\xi A_4}`$. Its linear term is $`i\xi(A_1+A_2-A_3-A_4)=i\xi^2(D_1A)(p)`$, and $`|D_1A|\le2\sup|\nabla^\xi A|\le2r`$. The other terms are at most $`e^{4b\xi r}-1-4b\xi r\le8b^2\xi^2r^2e^{4b\xi r}`$, term by term in the exponential series. Since $`\xi,r\le1`$,

```math
|\partial e^{i\xi A}-1|\le D\,r\,\xi^2,\qquad D:=\max\{2b+8b^2e^{4b},\,1+c_F\}. \tag{5.2}
```

This also holds for complex $`A`$. No inverse power of the spacing remains.

*The current of a true pair.* Apply `4.4:lem-current-remainder` (i) (CA-I 10350) with $`U_0=1`$, $`\mathsf c=0`$ and $`\ell=1`$. It gives $`|F(1,A)|\le c_F\max(|A|,|\nabla A|)^2\le c_Fr^2`$. By `4.4:eq-current-remainder-1`, $`J(e^{i\xi A})=D_1^*D_1A+F(1,A)`$, since $`J(1)=0`$. If also $`|\partial^*\partial A|\le r`$, where $`\partial^*\partial=D_1^*D_1`$, then $`|J(e^{i\xi A})|\le(1+c_F)r\le Dr`$.

*Choice.* Put $`c_*:=\min\{1/4,(16K^\sharp D)^{-1}\}`$, and

```math
\alpha_0':=\frac{\alpha_0}{4K^\sharp},\qquad \alpha_1':=\min\Bigl\{\frac{\alpha_1}{2},\ \Bigl(\frac{\alpha_0}{4K^\sharp}\Bigr)^{1/2}\Bigr\}. \tag{5.3}
```

Then (3.3) holds. Indeed $`\alpha_1'\le\alpha_1`$, and $`K^\sharp(\alpha_0'+\alpha_1'^2)\le K^\sharp\cdot2\alpha_0/(4K^\sharp)=\alpha_0/2`$. By (3.4), $`\alpha_0'\le\bar\alpha_0'`$ and $`\alpha_1'\le\alpha_1/2\le\bar\alpha_1'`$.

*Conditions (i)–(iii) at $`(\alpha_0',\alpha_1',\alpha_0)`$.* Take the decomposition $`U=1`$, $`U'=e^{i\xi_jA}`$. (i) holds: $`\partial1=1`$, and the cube gauge of (1.12) is the trivial one, with potential $`0`$. (ii) holds: $`r\le\alpha_1/4<\alpha_1/2`$, and $`r^2\le c_*^2\alpha_0^2\le c_*\alpha_0\le\alpha_0/(16K^\sharp)<\alpha_0/(4K^\sharp)`$, since $`\alpha_0\le1`$; so $`r<\alpha_1'`$. (iii) holds: by (5.2), $`|\partial e^{i\xi_jA}-1|\le Dr\xi_j^2\le Dc_*\alpha_0\xi_j^2\le\alpha_0'\xi_j^2/4`$. In case (a), $`|\mathbf J|\le r\le\alpha_0/4<\alpha_0`$. In case (b), by the current bound, $`|J(e^{i\xi_jA})|\le Dr\le\alpha_0/(16K^\sharp)<\alpha_0`$. Corollary 2 at the radii (5.3) now gives (a) and (b), with $`\gamma_0=\alpha_0`$.

*(c).* Let $`X\in\mathbf D_j`$. The walls of $`\pi_j`$ are walls of $`\pi_{j-1}`$ (CA-I 32724–32730), so $`X\in\mathbf D_{j-1}`$. Conditions (i)–(iii) of $`U^c_j(X,\alpha_0,\alpha_1)`$ hold, by the last paragraph and monotonicity. Condition (iv) of $`U^c_j`$ reads the tower of rule $`\mathfrak r_1`$ at level $`j`$ (CA-I 32559–32563, 32871–32875). Proposition 1 at $`p=j`$, $`Z=X`$, $`\mathfrak r=\mathfrak r_1`$ and the radii (5.3) gives its bounds with coefficient $`\alpha_0/2<\alpha_0`$ on $`X^{\wr j}`$. For $`U=1`$ the bounds are trivial. Finally $`\tilde X^{-2}\subset X^{\wr j}`$: a point of $`\tilde X^{-2}`$ lies in a $`\pi_j`$-cube $`Q`$ with $`\tilde Q^2\subset X`$; its $`\pi_{j-1}`$-cube $`\square`$ lies in $`Q`$, and $`\tilde\square^2`$ lies within $`2ML^{j-1}\le ML^j`$ steps of $`Q`$, so inside $`\tilde Q^1\subset X`$. $`\square`$

**The choice of $`c_T`$.** In `4.7:eq-true-pairs-a` (CA-I 29529–29535), choose once

```math
c_T:=\min\{c_T^\circ,\ 1/8,\ 1/C_{IV},\ c_*\}, \tag{5.4}
```

and use it at every occurrence of the true-pair and polydisc constant. Unrelated constants with the same name are not reset (Appendix B). The norm $`N_j(\mathsf Z)`$ of `4.7:eq-true-pairs-1` is the value, first-difference and second-order norm of $`A:=\ell_j\mathsf Z`$ at spacing $`\xi_j`$. So $`N_j(\mathsf Z)\le c_Tr_j`$, $`r_j=\min(\alpha_{0,j},\alpha_{1,j})`$, gives the hypotheses of Lemma 3 (b) and (c) at the running radii. The running radii obey (3.4), since $`\alpha_{i,j}\le\alpha_i`$ (CA-I 1667–1669) and $`\alpha_i`$ obeys the Stage-7 ceilings. This proves (a) and (b) of `4.7:not-true-pairs` and replaces its free-prime step (CA-I 29557–29589). It also replaces the equal-radius inference of `5.2:lem-polydisc-containment` (CA-II 4378–4384) by Lemma 3 (a) and (c). That lemma keeps its radius formula $`\mathfrak r_j=c_T\min(\alpha_{0,j},\alpha_{1,j})`$, with one possibly smaller fixed $`c_T`$. Its ratio $`\mathfrak t_j^{-2}=(\min\{\alpha_0,\alpha_1\}/\min\{C_0,C_1\})^2x_j(\log x_j)^{-2q}`$ does not change: $`c_T`$ cancels in this ratio only.

A smaller $`c_T`$ changes fixed constants and radii: $`C_\vartheta`$ (CA-I 30028–30056), $`\widetilde K`$ (29828–29865), $`C'`$ (32284), $`C_\beta=4B_3^2CS(\delta_1)\mathfrak r_\circ^{-2}`$ (CA-II 4721), $`\mathfrak e_Q=C_{\mathfrak a}B_3M_Q\varepsilon'/(c''c_T)`$ (CA-II 96412), $`C_{\mathfrak e}=C_wB_3\max\{2,C_{\mathfrak a}M_Q/(c''c_T)\}`$ (CA-II 97071), $`C_\Pi=C_\beta\mathfrak r_\circ^2/(c_TC_*)^2`$ (CA-III 90592), their descendants, and the Cauchy radius $`\xi_i^3c_Tr_i/(8d)`$ of the coupling extraction (CA-I 32452–32491). The cancellation at CA-II 96444–96468 removes running field amplitudes, not $`c_T`$. Fix $`c_T`$ and its dependent constants before the final $`\gamma`$ choice (CA-I 32405–32409; CA-II 94857–94865). Fixed extraction and response constants may grow, so the final coupling ceiling may be smaller. Since $`q>p_0`$, $`\vartheta(\gamma)\to0`$ still gives a one-sided small-coupling ceiling (CA-I 30051–30105). The powers of the coupling and of the logarithms do not change.

## 6. Uses of (1.17) in your account

| Use | Pair | Supplied by |
|---|---|---|
| CA-I 34058–34218, `4.8:prop-small-pairs` | the supplier slot | Corollary 2 |
| CA-I 34811–34830, amplitude ceilings | the entry $`2B_3\alpha_0'\le\alpha_0`$ at 34819 | replace by (3.3) |
| CA-I 32599–32623, the sufficient condition | generic statement | complex case: Proposition 1 with (3.3); keep the real $`2B_3\alpha_0'`$ bound as a separate published input |
| CA-I 29522–29605, `4.7:not-true-pairs` | true pairs, $`U=1`$, ball $`c_Tr_j`$ | Lemma 3 (b), (c) with (5.4) |
| CA-I 32412–32500, `4.7:prop-coupling-increment` | polydisc of radius $`\xi^3c_Tr/(8d)`$, through true pairs | the same |
| CA-I 34241–34403, `4.8:prop-class-reproduction` (e); CA-I 34718, 34738–34741 | unit, true and small pairs; real backgrounds; orbit-form inputs | Lemma 3 for seeds; Corollary 2 under (3.3) for small pairs; real estimates under their own hypotheses; orbit-form suppliers kept |
| CA-II 4333–4398, `5.2:lem-polydisc-containment` | $`e^{i\xi\mathcal A}`$, independent current, ball $`\mathfrak r_j`$; equal-radius inference at 4378–4384 | Lemma 3 (a), (c) with (5.4), the reduced radii of your ER8 |
| CA-II 4599–4727, 94857–94865, 96280–96304, 96404–96468, 97064–97075; CA-III 90585–90624 | through $`\mathfrak r_j`$ | same form of radius; $`\mathfrak t_j`$ unchanged; fixed extraction and response constants may grow |

The fresh admissions in the true-pair and polydisc arguments have unit real factor, and Lemma 3 supplies them. Corollary 2 under (3.3) replaces the generic small-pairs supplier. Uses at real pairs keep their hypotheses: there $`\alpha_1'=0`$, Proposition 1 gives $`K^\sharp\alpha_0'`$, and the real bound $`2B_3\alpha_0'`$ of CMP 102 Proposition 9 may be kept. Other complex memberships, including minimizer families over nontrivial real bases, keep their own nesting, inheritance, gauge-transport or increment suppliers. Our search found no other fresh use of complex (1.17) that needs an unbudgeted pair with a nontrivial real factor. It found further complex memberships, excluded assertions and downstream uses of constants; Appendix B lists them.

## 7. Order of constants: the gap-number floor and the Stage-7 ceilings

This partial order is enough for the argument. It keeps the earlier floors and stages of the account, and it does not replace the whole order of choice. Early block and parametrix sizes are distinct from the late cube size $`M`$. The order: $`L`$; $`\mathfrak M`$ and the early block and parametrix choices; the flat, decay, blocking and localization constants that the gap-number floor reads; the Stage-5 choice of $`M_1`$, then $`R_1`$ (below); the other early orbit and averaging constants $`B_{\rm o},r_B,\varepsilon_{\rm adm},r_4,C_4,\alpha_*`$; $`K^\sharp`$, then $`\bar\alpha_1'`$, then $`\bar\alpha_0'`$; $`B^{(109)}`$ before $`M\ge2LR_1M_1`$ (CA-I 4434–4437); Stage 7 with the Stage-7 ceilings; $`\alpha_2`$; $`c_T`$ by (5.4) and the constants built from it; the final $`\gamma`$ ceiling. The auxiliary radii (5.3) are chosen at each use, after the target radii. The ceilings of Proposition 1 are $`\bar\alpha_1'\le r/2`$, with $`r`$ of Step 3, and $`C_3\max\{1,C_s\}(\bar\alpha_0'+\bar\alpha_1'^2)\le\min\{\alpha_*,\varepsilon_{\rm adm}/2\}`$, with the smallness of Step 2. The square enters only as a ceiling on $`\bar\alpha_1'`$; no relation between $`\alpha_0'`$ and $`\alpha_1'`$ is imposed. If $`K^\sharp`$ depended on $`M`$ or $`B^{(109)}`$, nothing would break: every use of $`K^\sharp`$, through (3.3), $`c_*`$ and $`c_T`$, comes after those letters.

**The gap-number floor.** The continuation and orbit bounds hold on towers whose gap exceeds four lengths fixed after $`L`$ and the flat constants ([a1-balaban-gate.md](../gates/a1-balaban-gate.md), lines 128–134, with its references into [a1-balaban.md](a1-balaban.md)). Let $`R_D`$ be a fixed $`L`$-power satisfying all four separation requirements of that gap-order calculation: the summability gap, the auxiliary-parametrix collar plus its stencil, the localization/reset collar, and twice the descent collar. These are fixed after $`L`$ and the flat-package constants, before $`M_1`$ and the field radii; the parametrix side used in this calculation is not the later lattice parameter $`M`$. (That derivation also writes a localization factor $`R_1`$; it is a different constant from your gap number.) Rule $`\mathfrak r_1`$ has gap greater than $`R_1\mathfrak ML^q`$ (CA-I 32877), and rule $`\mathfrak r_2`$ has gap at least $`M_1L^q\ge R_1\mathfrak ML^q`$ (CA-I 32882). The account asks that $`R_1`$ be "a sufficiently large positive integer" (CA-I 32847–32851), lists $`R_1`$ after $`M_1`$, "chosen upward" (CA-I 1508–1511, 2063–2064), and requires $`R_1\le M_1/\mathfrak M`$ (CA-I 32851). Let $`R_{\rm req}`$ be the least $`L`$-power at least $`R_D`$ and every earlier floor for $`R_1`$ ($`R_1\ge L`$, $`R_1\ge 4d`$, the kernel and summation floors at CA-I 13415–13417; strict floors strictly). Choose $`M_1`$ at least $`\mathfrak MR_{\rm req}`$, then choose an $`L`$-power $`R_1`$ with $`R_{\rm req}\le R_1\le M_1/\mathfrak M`$. This meets both the supplier's lower bound and the account's upper bound. It implements the order already described at SA 9916. A larger late $`M`$ does not force a larger $`R_1`$, and $`R_1`$ may not grow later with $`M_1`$ frozen. These choices do not supply the separately assumed uniform local-background operator bounds used in other applications.

**The Stage-7 ceilings.** Lemma 3 needs $`\alpha_0/(4K^\sharp)\le\bar\alpha_0'`$ and $`\alpha_1/2\le\bar\alpha_1'`$. So add (3.4) to the radii of Stage 7 (CA-I 1614–1629). Its letters are fixed before the radii, and the radii are chosen downward after $`(L,B^{(109)},M)`$ (CA-I 34811–34830), so there is no cycle. The running radii inherit (3.4) through $`\alpha_{i,j}\le\alpha_i`$ (CA-I 1667–1669). Without (3.4), the proof of Lemma 3 does not cover the whole target-radius range. We assert no counterexample to the seed inclusion. The outline states the lemma "for sufficiently small $`a_0,a_1`$" (SA 6586–6590). We add no square ceiling on the absolute radii: the account chooses $`\alpha_1`$ before $`\alpha_0`$ (CA-I 1614–1615), so $`\alpha_1^2\le c\,\alpha_0`$ would be a floor on the later $`\alpha_0`$. The auxiliary radii (5.3) carry the square instead.

## 8. Inputs: the Balaban results your account cites, and what it prints

| Input used here | Balaban result your account cites | What your account prints | Our derivation |
|---|---|---|---|
| Averaging bound: averages of a complex perturbation of a real field, uniform in depth | CMP 98, Propositions 1–7 (CA-I 166568) | **Not printed in this form.** The average bound is used inside the (1.17) sentence (CA-I 32603–32606); `4.6:lem-averaging-locality` (CA-I 24239) gives block locality, not this bound | Appendix A.1; checked by Claude |
| Continuation bound: holomorphy in the datum, with the current of the continued configuration | CMP 102 Theorem 1, Proposition 9, (190) (CA-I 166573; CA-II 85845) | `8.4:thm-minimiser-analyticity` (CA-II 85845) prints analyticity and first-derivative decay. **It prints no current bound for the continuation.** (189)–(190) are `9.3:prop-second-variation` (CA-III 35577), printed without proof | Appendix A.2; checked by Claude |
| Orbit bound: one regular critical orbit, linear in the datum radius | CMP 102 Theorem 1, (7)–(9) (CA-I 166573) | `4.9:thm-minimal-orbit` (CA-I 35144), cited | rebuilt on the flat bounds; checked by Claude |
| Curvature bound for averages of a real field | CMP 98 (48), (54); CMP 102 (160) | used inside the (1.17) sentence (CA-I 32603–32606) | the plaquette recursion of Step 4; checked by Claude |
| Flat bounds | CMP 99b Theorems 3.1–3.3, (3.48), (3.132) at $`U=1`$, proofs in CMP 89, 95, 96 (CA-I 166571) | `5.8:prop-local-decay` (CA-II 54464), cited | rebuilt in the default convention; checked by Claude, with repairs |
| Tower rules, collar bound, change of units | yours | `4.8:def-tower-rules`, `4.8:eq-tower-rules-b` (CA-I 32834–32936), `4.8:thm-restriction-units` (CA-I 33276), proved | used as proved; the uses here rechecked by Claude |
| Quadratic remainder of the current | yours | `4.4:lem-current-remainder` (CA-I 10350), proved | used as proved; the case $`U_0=1`$ rechecked by Claude |

The definitions are those of CMP 109: the regularity spaces (1.11)–(1.14) and the current (1.8), as your account transcribes them (CA-I 32498–32623). The repository derivations and their checks are identified separately from the complete-account results used as cited inputs (the last two rows). Each "checked by Claude" is one line-by-line reading of a Codex text, first failing step none after the stated repairs. Model checks retain every named hypothesis and are not independent certification of those inputs.

## 9. Scope and limits

1. **The original form stays open.** (1.17) at complex pairs with $`2B_3\alpha_0'`$ alone is neither proved nor refuted here. Proposition 1 is weaker on part of the domain (§2). It is enough for the uses in §6 only.
2. **Determining sets.** The proof is for the default determining sets: inward bonds free, outward rows kept (SA 9607–9625). Our derivations cover only this convention. They do not cover the kept-inward convention of CMP 96 and 119. A consumer must read the tower in the default convention.
3. **Group: SU(2) only, as checked.** Balaban states his results for a semisimple compact $`G\subset U(N)`$ (CMP 109, pp. 251–252 and 259). Our derivations of the inputs are written for $`G=SU(2)`$. The line that shows it is in the one-step bound of the averaging derivation (Appendix A.1): "Summing over the three color coordinates bounds the sum of matrix norms by a fixed color factor." The flat bounds are color-blind at $`U=1`$. The steps that are not inputs (Step 1, Lemma 4, Steps 5–6, and (5.2) and the current bound in Lemma 3) use only unitarity and $`b=\sqrt N`$. For $`N\ge3`$ the result rests on Balaban's statements as printed, not on a derivation we checked.
4. **Which object $`U_n^{\mathfrak r}`$ is.** Here it is the axial representative of the unique regular critical orbit, continued holomorphically. Your account calls it "the axial-gauge minimiser" of CMP 102 Theorem 1 (CA-I 32896). The two agree when the minimal orbit is regular. We cite that clause of CMP 102 Theorem 1; we did not rebuild it.
5. **Not supplied here.** `4.13:lem-minimizer-unique` and `4.13:lem-own-constant` (proof outstanding in your account); the near-case bound $`|u_j-1|<B_3^2O(1)M\alpha_0`$ (CMP 109 (3.37)); the literal-frame, block-average, straddling and shell assertions of Appendix B; the stage-background and re-minimization assertions excluded at CA-I 38108–38144; and the pointed-core admission of our derivation of CMP 102.
6. **What does not follow.** The other items of clause (0), the other inputs of (g) and (c), and Theorem 0. This note does not use the stage theorem of CMP 122a (1.60)–(1.70) that your account assumes at CA-I 54986–54998.

## Appendix A. Summaries of the two uniform input estimates

This appendix summarizes the input derivations; it is not a standalone derivation of the flat inverse or every contraction estimate. For the averaging input see [b109.md](b109.md), P15, (72), (74)–(77), and [a1-balaban.md](a1-balaban.md), §§3.5, 7.6, (7.14). For the continued-current input see [a1-balaban.md](a1-balaban.md), §9.1, (9.1)–(9.2), conditional on the flat package. The real-orbit and real-average inputs are at its §8, (8.2), and §7.1, (3.6), respectively. The flat package is [flat-port.md](flat-port.md), §§2, 4–9. The geometry, unit-change and current-remainder inputs are the cited complete-account results. The proof in §§4–5 uses these estimates with their stated domains and uniformity; it does not discharge them anew. Some parametrix estimates in those derivations were followed as sketches rather than rederived constant by constant ([a1-balaban-gate.md](../gates/a1-balaban-gate.md), line 158). Codex derived both inputs in our repository; Claude checked both line by line. Credit: Balaban, CMP 98, pp. 24–26 and 34–42, (48)–(54), (110)–(126), and CMP 102 §G, (170)–(177); the outline's contour mean (QC1)–(QC7), SA 7963–8053, and averaging recursion (PX141)–(PX154), SA 11507–11640. Much of A.1 follows those passages (in particular SA 11510–11597); it is included as exposition, with the repository's curvature-to-local-gauge and read-set checks.

**A.1 Averages of a complex perturbation, uniformly in depth (the averaging bound of Step 2).** *One step.* In raw link coordinates let $`F_W(a)`$ be the logarithm of the straightened actual mean of $`e^{ia}W`$, and $`u_W(a)`$ its endpoint (node) factor. Each path has at most $`CL`$ links. On a fixed small matrix ball, $`\log(e^Xe^{-Z})=X-Z+E(X,Z)`$ with $`|E|\le C(|X|+|Z|)^2`$ and $`|D_ZE|\le C(|X|+|Z|)`$, by the convergent series of exp and log. So the contour mean $`Z=\bar X+\operatorname{mean}E(X_i,Z)`$ is a contraction on $`|Z|\le2\sup|X_i|`$. Its fixed point is unique and holomorphic (Cauchy's formula on the iterates), with constants free of the number of paths. Hence $`F_W`$ and $`u_W`$ are holomorphic on $`\|\log W/i\|_\infty+\|a\|_\infty<c/L`$. At $`W=1`$, $`a=0`$, the derivatives of the two node factors cancel the endpoint terms of the contour, so $`D_aF_1(0)=S_L`$, the straight-segment row, with row sum $`L`$ and column sum $`L^{-3}`$. Two Cauchy circles give $`\|D_aF_W(a)-S_L\|_{\rm row}\le C_L\delta L`$ and $`\|D_aF_W(a)-S_L\|_{\rm col}\le C_L\delta L^{-3}`$, $`\delta=\|\log W/i\|_\infty+\|a\|_\infty`$. This step sums the scalar coefficients over the three color coordinates; there SU(2) enters. Also $`|u_W(a)-1|\le C_L\|a\|_\infty`$. At a real reference whose plaquettes are at most $`\alpha t_q^2`$, moving the transports of the segment around its elementary squares costs the plaquette errors. So the linear part has norm at most $`L(1+C\alpha t_q^2)`$, and the remainder is at most $`C_L`$ times the squared angle.

*Reference gauge.* The one-step formulas need the real reference to be small in value in a local gauge. A coordinate-tree gauge on each enlarged double block gives this from curvature alone: a link moves to the tree through at most $`dL`$ conjugated plaquettes, and $`\prod_iW_i-1=\sum_i(\prod_{h<i}W_h)(W_i-1)`$, with unitary factors, bounds its distance from $`1`$ by the sum of the plaquette errors.

*Depth.* Put $`a_0=\eta_nw`$, $`a_{q+1}=F_{W_q}(a_q)`$, $`W_q=M^q(U_r)`$. The exact straightening identity gives $`M^q(e^{i\eta_nw}U_r)=(e^{ia_q}W_q)^{v_q}`$, $`v_{q+1}=v_q|_{\rm next}\,u_{W_q}(a_q)`$. Divide the one-step bound by $`t_{q+1}=Lt_q`$: this is the recursion for $`\beta_q=\|a_q\|/t_q`$ in Step 2, and first exit gives $`\|a_q\|\le2|w|t_q`$. Then $`|u_{W_q}(a_q)-1|\le2C_L|w|t_q`$. Since $`\sum_qt_q\le(1-L^{-1})^{-1}`$, the product gives $`|v_q-1|+|v_q^{-1}-1|\le C|w|`$. On each data set $`e^{iB(w)}`$ is a product of $`v_q`$, $`e^{ia_q}`$ and a conjugated inverse node factor. So $`\sup|B(w)|\le C_4\|w\|`$, with no factor that depends on $`n`$ or $`p`$. Every map is a finite composition of products, inverses and convergent series, so $`B`$ is holomorphic. No positivity is used, so complex $`w`$ is allowed.

**A.2 The current of the holomorphic continuation (the continuation bound of Step 3).** Let $`U_0`$ be the real critical representative at a real datum $`V_0`$ inside the admissible radius. Its first variation vanishes on the tangent fibre; this does not say $`J(U_0)=0`$. For $`V=e^{iB}V_0`$, the exact reduced-datum map, outward factors included, has norm at most $`C_L\|B\|_\infty`$ on a fixed complex ball. In the chart of the real problem the constant fibre term now vanishes. The unknown $`A(B)`$ is the fixed point of the same contraction, uniformly on $`\|B\|_\infty<r_B`$. The iterates are holomorphic, the error after $`m`$ steps is $`2^{-m}`$ times the first error, and the uniform limit is holomorphic. This gives $`\|A(B)\|_X\le C\|B\|_\infty`$, for the value and the first difference in local units.

*The current.* The holomorphically extended constrained Euler residual is holomorphic in the datum $`B`$ and vanishes for real $`B`$, where the representative is critical. The identity theorem on the connected datum ball therefore gives the same equation for complex $`B`$. Subtract the Euler equation at $`B=0`$ from the one at $`B`$. All constant force terms cancel. The remaining linear forcing is $`O(B)`$, and every nonlinear term contains $`A(B)`$. The flat bounds invert the linear part, so $`|D^*DA(B)|_{-3}+|\Delta_{U_0}A(B)|_{-3}\le C\|B\|_\infty`$. This second-order bound does not come from Cauchy differentiation of a value bound. *The representative.* The axial gauge is an explicit recursive map: node values are $`1`$, each child gauge comes from one contour transport, and every non-node has one parent. Relative to $`U_0`$, a gauge factor at scale $`t\le s`$ differs from $`1`$ by at most $`C\|B\|_\infty t/s`$ (A.1). So the product of the conjugators has norm and inverse norm at most $`\exp(C\|B\|_\infty/(1-L^{-1}))`$. Conjugation gives $`\Phi_{V_0}(B)`$ with $`M_{\mathbf B}\Phi_{V_0}(B)=e^{iB}V_0`$ and $`\max\{\sup_p\eta^{-2}\mathsf L(p)^2|\partial\Phi(p)-1|,\ \sup_b\mathsf L(b)^3|J(\Phi)(b)|\}\le C(\varepsilon_1+\|B\|_\infty)`$. Here $`J`$ is the current of CMP 109 (1.8) (CA-I 32903–32912), and $`\varepsilon_1\le\varepsilon_{\rm adm}`$ is the datum radius. In level-$`n`$ units $`\mathsf L=1`$ at top-layer elements, which gives the continuation bound with $`C_2=C`$. On real overlaps the representatives agree by orbit uniqueness and the unique axial gauge; on complex overlaps, by the identity theorem.

## Appendix B. Search record

**Search.** CA-I, II and III, for every `1.17`, the labels of the displays, every `c_T`, every `2B_3` and `B_3^2`, and every "(i)--(iii) imply" (CA-II 4383 reads "the estimates (i)--(iii) imply condition (iv)"). CMP 109 (1.17) is cited by label at 31 lines of CA-I and at CA-III 111326; CA-II 4381–4384 uses it without the label. Every other `1.17` is CMP 116, 122a, 122b or a decimal.

**Uses at real pairs** ($`\alpha_1'=0`$): CA-I 34087–34089 and 34205–34208 (the minimal configurations of CMP 109 p. 263); 10750–10754, 36806–36905, 42198–42340, 43590–44380, 128551–128930; CA-II 99767–99813. CA-I 128551–128930 keeps its uniform-in-strata current hypothesis (b) (128807–128817, 128923–128930). The reblocking proposition at CA-I 44127–44129 stays incomplete at its marked step.

**Other memberships of class reproduction keep their suppliers.** Near incoming pair: the assumed hereditary clause. Near product: the nesting identity of `4.13:lem-minimizer-unique` (CA-I 45162, proof outstanding there). Far incoming pair: restriction. Far product: the increment estimate, with its $`\alpha_2`$ ceiling. Domain restriction: monotonicity. None applies (1.17) at the full target radii. The own-radius gauge of `4.13:lem-own-constant` (CA-I 45203, proof outstanding there) is met without (3.2): seeds have $`U=1`$, and real backgrounds use real CMP 98 averaging and CMP 102 gauges.

**Matches that are not fresh uses.** CMP 116 operator radii (CA-I 4384–4554, 5822–5908 and others); block-average and literal-frame curvature (13198–13255, 17523–17564, 18305–18346); straddling and shell clauses (10028–10092, 120111–120334); passages that name the (1.17) route and do not take it (15918–15961, 20150–20185, 34886–35045); the units definition (154551–154588); B'-ball and entry-conversion ceilings (117207–117328); a near-pair chain with another starting route (121282–121350); the excluded general complex assertion (154825–154863); a rejected linear-datum route (155490–155511).

**Other complex memberships, with separate suppliers.** CA-I 155275–155438, a complex minimizer over a real base ($`W=e^{i\eta\mathcal H}U_0`$, 155310–155316), with tower bounds from a nesting input (155388–155426); the $`2B_3`$ comparison at 155421 is arithmetic after them. CA-I 155940–156060 and 156177–156189, a complex minimizer family with unit base, with N1 nesting at 156008–156033. CA-I 35963–35971, a complex pair moved over an existing real factor by a $`c_T`$-sized perturbation; the configuration does not change. CA-II 94811–97192 (with 96010–96026 and the core-estimate hypothesis from 96276), box-minimizer extension and nesting. Lemma 3 supplies none of these.

**Excluded assertions and separate inputs.** CA-I 40189–40212 (40194–40197); 42545–42640 and 42670–42688; kernel membership 144962–145024, 145167–145182; window minimizers and thresholds 148810–148832, 148885–148903, 149809–149888, 150005–150055, 150745–150755, 151807–151919. **Symbol and threshold records** ($`2B_3`$ in definitions and comparisons): CA-I 33704–33723, 36519–36546, 36678–36705, 37914–37943, 153616–153622, 154875–154918, 154959–154970, 155139–155150, 156425–156447, 163946–163970, 164015–164026, 164136–164183; CA-II 43094–43139, 44456, 44514, 86147–86161, 95984–96138, 109508–109517, 119774–119847; CA-III 34805–34814, 35023–35038, 35364–35370, 36974–36999, 37123–37140. Unrelated large-field bounds also contain $`B_3^2`$.

**Downstream $`c_T`$ and radius consumers.** CA-I 29458–29466, 29640–29642, 29982–30012, 30562–30573, 31304–31457, 31605–31664, 31709, 31740–31756, 31833–31874, 32242–32409; CA-III 81024–81032, 81041–81052, 81118, 81155–81159 (with $`4B_3^2\mathfrak r_j^{-2}`$) and 90585–90624. **Unrelated $`c_T`$ homonyms, not reset by (5.4):** CA-I 70548 and 75590–75665 (term constants); 119041, 119386, 119406, 124591 (a size constant); CA-II 81373 (a moment-recursion constant).
