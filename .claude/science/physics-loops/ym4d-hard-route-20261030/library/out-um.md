# Uniform bounds on the unmarked coupling increment under your lemma's four hypotheses

## Scope and inputs

This note supplies the uniform extraction argument at your starred step in `4.2:lem-unmarked`, CA-I 4084–4111.
It gives both bounds for every \(l\ge1\), using only the constructed prefix \(g_0,\ldots,g_{l-1}\).
All references to your account and outline use commit `31a47c543775`.
CA-I, CA-II and CA-III denote your complete account's three parts; line numbers refer to their TeX sources.
We keep your coefficient definition, `4.2:def-increment` (CA-I 3764–3847), and your order of constants.
The four hypotheses are exactly those at CA-I 4040–4058:

1. \(g_0,\ldots,g_{l-1}\in(0,\gamma]\), and steps \(1,\ldots,l-1\) have been performed along these couplings.
2. Your `4.20:thm-representation` bounds hold at scales below \(l\).
3. The actual unmarked output \(E_l^{\mathfrak A}\) satisfies Balaban's one-step small-field bounds at step \(l\).
4. Its actual remainder obeys CMP 116 (2.41), with its factor \(\epsilon:=\varepsilon_1^{\mathrm I}\).

The following analytic inputs remain inherited. Your account does not itself prove them, and this note does not prove them.
They are estimates of Tadeusz Balaban, cited by paper and equation number:

- CMP 109, pp. 272, 281–282: the extension (3.11)–(3.14), (4.2)–(4.5), and the \(B_3\) derivative estimate on p. 282.
- CMP 109 (4.35)–(4.37): the free-boundary response passage; the preceding derivative estimate retains the CMP 102b §G tree expansions.
- CMP 99b, Theorems 3.10 and 3.12: the walk expansions and exponential kernel bounds used in that passage.
  This includes the constrained inverse-covariance expansion and bounds (3.132), **printed without proof**, as your `4.5:rem-covariance-inverse-walks` records (CA-I 13142–13173).
- CMP 116 (2.41): the actual remainder bound in hypothesis 4; CMP 109 Theorem 3 supplies the cited one-step bounds in hypothesis 3.
- For your `4.5:lem-uniform-increment`: CMP 98 Propositions 2, 6 and 7, including averaging derivatives and locality;
  CMP 102b Theorem 1, Proposition 9, (172), (181), and the first-response/current bounds of (190);
  CMP 96 Lemma 2.1 hierarchy summations, with the required comparison of hierarchy distance and ordinary distance.
  Your CA-III 35577–35624 records that CMP 102b (189)–(190) is printed without proof. The first-response part remains an input here.

The actual representation, one-step bounds and family clauses must hold, including volume consistency and pointing.
Your `4.38:cor-volume-families` propagates these clauses conditionally on its operator, locality and covariance hypotheses (CA-I 60641–60718).
Your `4.8:prop-far-case` gives the domain implication from the increment estimate (CA-I 33839–33886).
We use its half-radius identity-background case, with both tower rules and all hereditary labels.
The working note retains the checked continuation of your increment estimate and its imported averaging and response bounds.
The argument below reproduces its application at that background; it does not assert admission for arbitrary backgrounds.
The one-step theorem uses the one-power hereditary class (CA-I 4136–4180).
This note does not construct these inputs, prove the marked estimate, or prove the full renormalisation step.
Your outline already proves the conditional Cauchy and moment argument (6700–6743; 12982–13021).
Here the task is its level-uniform application at the specified star, including both potential and current slots.

## Statement

Under the four hypotheses and inherited inputs above, constants fixed in your order satisfy
\[
 |\beta_l^{\mathfrak A}-\beta_l^0|\le C_{\rm rem}\varepsilon_1^{\mathrm I},
 \qquad |\beta_l^{\mathfrak A}|\le C_\beta\qquad(l\ge1).
\]
Here \(C_{\rm rem}\) is fixed before \(\varepsilon_1^{\mathrm I}\), and \(C_\beta\) before \(\gamma\).
Neither depends on \(l\). The proof gives both constants before \(\varepsilon_1^{\mathrm I}\).
The constant used only to identify a fixed-level torus limit may depend on \(l\); it does not enter these bounds.

## Proof

**Local bounds and scaled response.** Write \(E_l^{\mathfrak A}=G_l+R_l\), with \(G_l\) the actual Gaussian normaliser, and set \(\xi=L^{-l}\).
Let \(\mathcal B_l\) be your coefficient functional. Its linearity gives \(\beta_l^{\mathfrak A}-\beta_l^0=\mathcal B_l(R_l)\).
Hypotheses 3 and 4 give, in the localisation where each bound is stated,
\[
 \|E_l^{\mathfrak A}(X)\|_{U_l^c}\le E_0e^{-\kappa d_l(X)},\qquad
 \|R_l(X)\|_{U_l^c}\le A_R\epsilon e^{-\kappa d_l(X)}. \tag{1}
\]
These are complex-domain supremum bounds. Keep a specified pointing if the bound is already pointed.
The coefficient \(A_R\) includes every early factor in (2.41); a larger decay rate can be reduced to \(\kappa\).
The cutoff \(\delta_{l-1}/g_{l-1}\) enters only through the two ceilings supplying (1), CA-I 4171–4180.
In Balaban's normalisation set \(P_1=DPD^*\), \(R=1-P\), and
\[
 \mathcal N_{l,X}(A)=\max\{|A|_X,|\nabla^\xi A|_X,|P_1A|_X,|\Delta^\xi A|_X\},\qquad
 \mathcal N_{l,X}(H_l\delta_x)\le C_He^{-\sigma\operatorname{dist}(x,X)}. \tag{2}
\]
All stencil reads belong to the local norm; a fixed enlargement can be absorbed in its constants.
The imported \(B_3\) estimate and free-boundary passage give \(C_H,\sigma>0\) independent of \(l,X\).
At zero current, \(H_l=G_0Q^*(QG_0Q^*)^{-1}\), CMP 99b (3.126), on the homogeneous whole-lattice tower.
Its datum and output block lengths in step units are one. CA-I 58834–58855 identifies this with your limit.
For completeness, exhaust the free-boundary domain at fixed mesh, including the source and all local reads.
The value, gradient and Laplacian pass through finite stencils.
For \(P_1H_l\), first truncate read and walk lengths, pass common terms to the limit, then remove the truncations.
CMP 99b Theorems 3.10 and 3.12 give the exponential kernels of \(P_1(\square_0)\) and \(P_1\), through \(R=1-P\), (3.25).
Their domain-uniform majorant permits this passage and preserves the constants in (2), as required at CA-I 4100–4111.
The link tangent is \(i\xi H_l\delta_x\), and the admissible link radius also carries \(\xi\).
Their quotient has no inverse-mesh loss. The other three members of (2) are already scaled; a value-only estimate would not suffice.

**An absolute analytic ball, including every label.** At background one the imported extension is
\[
 \Xi_l(A)=\bigl(e^{i\xi A},(\Delta^\xi-P_1)A+F(1,A)\bigr),\qquad
 |F(1,A)|_X\le C_F\mathcal N_{l,X}(A)^2\quad(\mathcal N_{l,X}(A)\le1). \tag{3}
\]
Here \(F(1,0)=DF(1,0)=0\); the background term vanishes, and \(C_F\) is mesh independent.
This is your `4.5:lem-curvature-remainder` at the flat background (CA-I 14083–14132); its output hierarchy weights are one.
After the absolute radii, but before \(\epsilon\), choose \(a>0\) inside the analytic radius in (3), with
\[
 a<\min\{1,\alpha_2,\alpha_1/8,\alpha_0/(2C_{IV})\},\qquad 2a+C_Fa^2<\alpha_0/2. \tag{4}
\]
We check that \(\mathcal N_{l,X}(A)<a\) places \(\Xi_l(A)\) in \(U_l^c\), with its one-power hereditary reading.
Choose the real factor \(U=1\). Its curvature, cube-gauge potentials and real tower readouts vanish.
The complex potential and gradient are below \(a\); its plaquette deviation is below \(C_{14}a\xi^2<\alpha_0\xi^2\).
Here \(C_{IV}\ge4C_{14}\), as in your increment lemma, CA-I 16041 and 16216–16223.
The independently supplied current is below \(2a+C_Fa^2<\alpha_0\). Thus clauses (i)–(iii) hold.
For a hereditary label \((p,Z)\), put \(\mu=L^{p-l}\le1\), \(\xi_p=L^{-p}\), and \(A^\flat=\mu A|_Z\).
Then \(e^{i\xi A}=e^{i\xi_pA^\flat}\), \(|A^\flat|<\mu a\), and \(|\nabla^{\xi_p}A^\flat|<\mu^2a\le\mu a\).
Apply your increment estimate with cube letter \(M/L\), gauge constant \(LB^{109}\), and radii \((\mu\alpha_0,\mu\alpha_1,\mu a)\).
The unit background meets every half-radius premise. Its average is one.
The datum displacement has the required margin by the averaging bound and \(c_Q(\alpha_1+a)\le C_1\bar\varepsilon_1/2\).
The other ceilings decrease with \(\mu\); \((M/L)LB^{109}=MB^{109}\) preserves the cube-gauge ceiling before that decrease.
Both towers have collar at most \(R_1M_1\); the existing floors \(\delta_0M\ge32L\), \(M\ge2LR_1M_1\) suffice.
Their two-layer interior is \(Z^{\wr p}\). For every \(1\le n\le p\), both curvature and current readouts obey
\[
 |\Phi_i(e^{i\xi_pA^\flat})-\Phi_i(1)|\le\tfrac12 C_{IV}\mu aL^{2(n-p)}
 <\mu\alpha_0L^{2(n-p)},\qquad i=1,2. \tag{5}
\]
The readouts are \(\Phi_1=\eta_n^{-2}(\partial U_n-1)\), \(\Phi_2=J_n\), with \(\eta_n=L^{-n}\), and \(\Phi_i(1)=0\).
Multiplying the first inequality by \(L^{-2n}\) gives \(|\partial U_n-1|<\mu\alpha_0\xi_p^2\).
The second gives \(|J_n|<\mu\alpha_0(L^n\xi_p)^2\). The real-factor bounds are zero.
These are your clauses at CA-I 33058–33074 and 33119–33126, for both rules and every label, with the same \(a\).
Only values and gradients enter this tower argument; the two second-order norms separately control the current in (3).

**Both slots and the Cauchy estimate.** A local scalar term \(f\) is gauge invariant.
Its first derivative at \((1,0)\) vanishes separately in each potential and current slot.
Indeed, constant gauge invariance makes each linear form adjoint invariant; it vanishes on commutators, which span \(\mathfrak{sl}_N\).
Differentiating local gauge invariance then shows that its Hessian kills \((D\omega,0)\).
The Landau condition \(RD^*H_l=0\) gives \(D^*DH_l=(\Delta^\xi-P_1)H_l\).
Thus \(D\Xi_l(0)H_l\) is the actual potential/current response. Any axial representative differs by a pure gauge tangent.
The \(D^2\Xi_l\) chain-rule term is multiplied by the zero first derivative. Hence, as in CA-I 58823–58855,
\[
 D^2(f\circ\Xi_l)(0)[H_l\delta_x,H_l\delta_y]
 =D^2f(1,0)[\mathfrak h_\infty\delta_x,\mathfrak h_\infty\delta_y]. \tag{6}
\]
Suppose \(\|f(X)\|_{U_l^c}\le S e^{-\kappa d_l(X)}\). Set \(d_x=\operatorname{dist}(x,X)\), \(q_x=C_He^{-\sigma d_x}\), and likewise for \(y\).
On \(|s|<a/(4q_x)\), \(|t|<a/(4q_y)\), the field \(A=sH_l\delta_x+tH_l\delta_y\) has \(\mathcal N_{l,X}(A)<a/2\).
Every read and hereditary label of this local function lies in \(X\); distant-source coefficients need no global smallness.
The admitted bidisc and the two one-variable Cauchy formulas give
\[
 |D^2f(1,0)[\mathfrak h_\infty\delta_x,\mathfrak h_\infty\delta_y]|
 \le16C_H^2a^{-2}S e^{-\kappa d_l(X)-\sigma(d_x+d_y)}. \tag{7}
\]
Directional Cauchy introduces no count of fine bonds. For the remainder, \(S=A_R\epsilon\).

**Pointing and the coefficient identity.** Use (7) directly if (1) bounds the specified pointed terms.
For an unpointed bound, set \(w_X(z)=\mathbf1_{X\cap\mathbb Z^4}(z)/|X\cap\mathbb Z^4|\) and \(\widetilde f(X;\cdot,z)=w_X(z)f(X;\cdot)\).
Every domain contains unit-lattice sites. These field-independent weights are nonnegative, at most one, and sum to one.
They preserve (7) and the finite-sum coefficient. They need not bound each original pointed member.
Your family clause says the original pointed terms sum to the unpointed term (CA-I 60660).
Your volume-consistency clause gives common non-wrapping lifts (60641–60657); your conditional propagation uses CMP 116 (2.13) at 60709.
At fixed \(l\), your existence lemma supplies absolute convergence for the original pointing; the estimates below supply it for the auxiliary pointing.
Fubini therefore identifies their whole-lattice coefficients. Only the sum over the base point is identified, not each pointed tensor.
If localisation formulas assign different domains, use their identical finite-torus total \(\mathcal L_V(s,t)\) at the minimal pair over \(e^{i(s\delta_x+t\delta_y)}\):
\[
 \sum_{X,z}D^2f^{\rm pointed}_{l,V}(X;1,0,z)[\mathfrak h_V\delta_x,\mathfrak h_V\delta_y]
 =\partial_s\partial_t\mathcal L_V(0,0)
 =\sum_XD^2f^{\rm unpointed}_{l,V}(X;1,0)[\mathfrak h_V\delta_x,\mathfrak h_V\delta_y]. \tag{8}
\]
The first derivatives vanish, so the same chain-rule argument applies. Take the common-lift limit at each fixed \(x,y\).
CA-I 58780–58898 supplies fixed-\(l\) torus response and analyticity bounds for this passage.
For wrapping domains, (g3), CA-I 3754–3761, gives \(d_l(X)>\varsigma/(4M)-2\).
Reserve half the polymer decay and sum rooted domains; the \(\varsigma^4\) base points cost only volume.
Their contribution is at most \(C(l)S\varsigma^4e^{-\kappa(\varsigma/(4M)-2)/2}\to0\).
Here \(C(l)\) is free of \(\varsigma\) and may depend on \(l\). Non-wrapping terms have the common lifts already cited.
Thus (8) identifies the whole-lattice kernels before the second moment. Its convergence constant is not used below.
CMP 119 (3.38)–(3.42) concerns totals before localisation; CA-I 60660 is the termwise pointing identity used here.

**Rooted sums and constants.** Put \(\rho=\tfrac14\min\{\sigma,\kappa/M\}>0\).
Your counting and diameter bounds (CA-I 3740–3761, 58877–58898) give, with fixed endpoint/cube constant \(c_d\),
\[
 \sum_{X\ni z}e^{-\kappa d_l(X)/2}\le K_0,\qquad
 |x-z|+|y-z|\le d_x+d_y+2Md_l(X)+4c_dM.
\]
Consequently \(e^{-\kappa d_l(X)-\sigma(d_x+d_y)}\le e^{4c_dM\rho}e^{-\rho(|x-z|+|y-z|)}e^{-\kappa d_l(X)/2}\).
Summing (7), rooted at \(z\), gives \(|\widehat\Pi_f(x,y,z)|\le C_*S e^{-\rho(|x-z|+|y-z|)}\), where \(C_*=16C_H^2a^{-2}K_0e^{4c_dM\rho}\).
Set \(S_\rho=\sum_ve^{-\rho|v|}\) and \(T_\rho=\sum_v|v|^2e^{-\rho|v|}\), with \(v\in\mathbb Z^4\).
Both are finite: a sup-norm ball has \((2n+1)^4\) sites, and \(n^me^{-\rho n}\le m!(2/\rho)^me^{-\rho n/2}\) reduces the shell bounds to geometric series.
For bond origins \(x=u,y=0\), endpoint costs already lie in \(c_d\), and
\[
 \sum_{u,z}|u|^2e^{-\rho(|u-z|+|z|)}
 \le2\sum_{u,z}(|u-z|^2+|z|^2)e^{-\rho(|u-z|+|z|)}=4S_\rho T_\rho.
\]
This proves absolute convergence and every required interchange. Since \(|u_\mu u_\nu|\le|u|^2\), your coefficient satisfies
\[
 |\mathcal B_l(f)|\le C_{\rm ext}S,\qquad C_{\rm ext}=4C_NC_*S_\rho T_\rho,\qquad
 C_{\rm rem}=C_{\rm ext}A_R,\quad C_\beta=C_{\rm ext}E_0. \tag{9}
\]
Here \(C_N\) is only the fixed colour contraction; it can be omitted for an individual normalised colour component.
Apply (9) to \(R_l\) and \(E_l^{\mathfrak A}\) to obtain both stated bounds.
Choose response, averaging and increment constants first, then the counting floors for \(\kappa\), then \(M\), then the absolute radii and \(a\).
Your Stage 7 fixes \(E_0\), \(\alpha_4\) and determined constants before \(\varepsilon_1^{\mathrm I}\) (CA-I 1614–1636).
CA-II 3296–3306 gives \(C_3=4(L+2)^4O(1)E_0C_1^{116}\alpha_4^{-1}\alpha_6^{-1}M^{\bar q}e^{C_2^{116}\kappa_1}\).
Every factor precedes \(\epsilon\); the additional \(\alpha_6^{-1}\) in CA-II 3443–3456 does too. Thus \(A_R\) and (9) precede \(\epsilon\).
Now impose \(\epsilon\le c_0/(2C_{\rm rem})\), and then choose \(\gamma\) with the one-step ceilings.
No inverse running radius, coupling, or fine-bond count enters (9). No step uses the next coupling \(g_l\).
For your flow consumer, the supplied one-loop interval bound gives \(\sum_{l=i+1}^n\beta_l^{\mathfrak A}\ge(n-i)c_0-2c_2-(n-i)C_{\rm rem}\epsilon\ge\tfrac12(n-i)c_0-2c_2\) (CA-I 4015–4030).

## Who wrote and checked this

Codex wrote the full working note. A fresh Claude session checked it line by line and found no failing step.
It asked for three citation repairs; they are applied here and in the working note.
Codex wrote this outward version and read it against the repaired working note. Claude (Opus 5.5) then read it against that note and every cited line of your account and outline; the statement, scope, constants and inputs match.
This is research text, not an audit; it grants no status. No computer-assisted step discharges an input.

[Full working note](um.md)
