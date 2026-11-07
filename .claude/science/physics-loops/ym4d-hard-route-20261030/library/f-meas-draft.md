# F-measure and F-contour of ST1: pass 1 (long draft)

Provenance: Claude (Opus 5.5), pass 1 (long draft), 2026-11-04, in the clone at commit `57d99099f`. Method: Claude drafts at length, Codex distils, a fresh session referees, then the part is frozen. This is research text, not an audit. It grants no status. Not yet checked by the other model.

Credits. SA denotes the four-dimensional outline `YM4_sketch_500.tex`, CA-I its complete account I, and Y3 the three-dimensional manuscript `YM3_I.tex`, all at `31a47c543775`, by Ethan Sussman and Levent Alpoge, with Claude and Codex as authors of their text. The averaging, the backgrounds, the pivot elimination, the conditional Gaussian, the strip method and the large-field stages are Tadeusz Bałaban's (CMP 99, 109, 116, 119, 122). Jonathan Dimock's expositions of Bałaban's renormalization group are acknowledged for the general structure. Bałaban's papers are not in the supplied source folder; they are read here only through the CA-I and SA lines quoted. Source line numbers refer to the files in the scratch folder `sa/`.

Targets (st1-r3.md lines 872 and 898, Corollary 14′ at line 1052, Result at 1122):

* **F-measure.** Identify the exact fibre-chart measure of Proposition F3 with the stage measure already stored by Bałaban, SA and CA-I. Every stored density and test must be retained.
* **F-contour.** Supply the exact conditional-mean contour, its containment in the tube, and the exact-cutoff deformation used by the conditional-mean estimate.

Status tags: **[proved]** means proved here from the stated inputs. **[input]** means a hypothesis, with its source. **[Outstanding]** means not proved here. **[counterexample]** means a proved failure of a stated claim under stated conditions.

---

## 0. Result

**F-measure is proved** (Theorem FM, Section 2). Four facts are proved:

1. The fibre measure \(\nu_W\) of F3 is the continuous disintegration of bare Haar measure along the stage average \(F\). So it is the actual conditional law of the removed rows given the new datum (Proposition FM2, Corollary FM3).
2. Bałaban's collar variable \(B_j\), as CA-I 81735–81756 transcribes his (1.53) and (1.60), is the free coordinate \(B\) of Theorem F4 at the reference \(V^{(j)}\). The chart is unique (Lemma FM4). A different reference changes \(B\) by an explicit per-row map with an explicit Jacobian (Lemma FM5).
3. The CA-I stage display (54291–54300) equals the fibre-chart integral exactly. This holds when \(z^{(j)},E_0^{(j)},\mathbb P^{(j)},\mathfrak K^{(n)}\) carry the explicit values (FM-def). In particular \(\mathbb P^{(j)}\) contains the relative chart Jacobian, pivot Haar factors included, as SA 7487 states for the main step. The rim fluctuation integral is retained unchanged, with its stored density.
4. The relative Jacobian is not identically one (Proposition FM7). So a presentation that drops it is not exact.

**F-contour: a counterexample as frozen, and a proof after one convention change** (Section 3).

* The stage fibre carries zero modes of the Wilson Hessian, along the block gauge directions (Lemma FC4). So the stage Gaussian must contain the stored block-axial gauge exponent of SA 7178–7181. Its exact centre is then the mean-contour axial point of the reference orbit (Lemma FC5).
* **[counterexample]** st1-r3 fixes the canonical representative by combs (st1-r3 line 41). In that convention the exact conditional mean in ST-test coordinates has size at least \((|F_p|/2-h_j)/g_j\) on one free row of every new-member block. Here \(F_p\) is the logarithm of a level-\(j\) plaquette of the new background in that block (Proposition FC6, an exact computation). The required mean bound \(|m|<\mathfrak b=\delta'_j/g_j\) therefore fails at every stage with \(|F_p|\ge2(\delta'_j+h_j)\). Nothing in ST1's declared inputs excludes such a stage.
* **[proved]** SA 9669–9676 and `a1-balaban.md` line 2501 allow the mean-contour axial representative instead. Amendment CV runs ST1 with it. Lemma CV checks every use of the comb convention in st1-r3. Under CV, Theorem FC proves the remaining items:
  * the exact cutoff is a product of centred balls in its own coordinates;
  * the stage integral over that fixed real domain is the holomorphic continuation of the real stage integral;
  * the exact conditional mean is \(m=g_j^{-1}i^{-1}\operatorname{Log}(VV^{\sharp-1})|_{\mathfrak F}\), with real reference \(m_{\rm r}=0\) and \(|m|\le\varepsilon_{\mathbf m}\mathfrak b\) at every datum in use, real or complex, uniformly in switches and independent currents;
  * the deformed contour lies in the tube \(\mathcal T_j\);
  * the bump deformation of Y3 52091–52134 is valid for this exact cutoff.
  The complex mean bound needs no complex localization hypothesis. It follows from real LOC by the three-lines theorem (Lemma FC7).

**First remaining Outstanding statement.** None inside F-measure or F-contour, under Amendment CV. CV changes a definition in the frozen st1-r3, so st1-r3 must reopen on it. Lemma CV is this draft's claim that the change costs nothing elsewhere in ST1. It must be refereed. The precision hypotheses of the conditional-mean estimate itself (Y3 51907–51926: a real positive reference precision and \(\hat\varepsilon\)-closeness) are not part of F-contour. They belong to the consumer, NL1/LF1 (Section 3.6).

**Constants.** Every constant used is fixed before \(\kappa\) and independent of \(M,\bar\kappa\). \(M\) enters only through \(R_\sharp\ge MR_t/4\), as a lower bound. The table is in Section 4.

No step uses a computation. Every argument is finite-dimensional real or complex analysis: changes of variables, Tonelli/Fubini, the contraction and implicit-function statements of F2, Cauchy's theorem along line segments, the identity theorem, and Hadamard's three-lines theorem.

---

## 1. Setting and the stored objects

### 1.1 The stage (recalled from st1-r3)

Fix an operation of level \(t\), a passing stage of level \(j\) in a class component \(X\), and write \(g=g_j\), \(\delta'=\delta'_j\), \(\mathfrak b=\delta'/g\). As in st1-r3 Lemma 12 (line 776), \(M_-,M_+\) are the determining maps before and after the stage. \(M_+\) enlarges member \(j+1\). The removed rows are \(\mathfrak E=\Gamma^{\rm rm}\) (level \(j\)), the added rows \(\mathfrak C=\Gamma^{\rm ad}\) (level \(j+1\)), the pivots \(b_0(c)\in\mathfrak E\), and the free rows \(\mathfrak F=\mathfrak E\setminus\{b_0(c)\}\). Retained rows are fixed. \(F=(F_c)_{c\in\mathfrak C}\) averages removed rows into added rows, and \(M_+=F\circ M_-\) with \(\ker DM_-\subset\ker DM_+\) (st1-r3 (67)).

**Pivots** (SA 8167–8176). For \(c=(y,y+Le_\mu)\) and \(h=(L-1)/2\), the pivot is \(b_0(c)=(y+he_\mu,y+(h+1)e_\mu)\). It crosses from \(B(y)\) to \(B(y')\). Internal contours stay inside one block. Only \(b_0(c)\) among the pivots occurs in \(q_{V,c}\). Thus a row with both endpoints inside one block is never a pivot.

**New-member blocks.** Call \(B(y)\), \(y\in\mathbb T^{(j+1)}\), a new-member block when \(B(y)\subset\Omega^+_{j+1}\setminus\Omega^-_{j+1}\). Members are unions of aligned blocks (GEO, st1-r3 line 126). Every level-\(j\) bond with an endpoint in a new-member block is then a removed row or not a row. Indeed, such a bond has an endpoint in \(\Omega^+_{j+1}\), so it is not a row of \(M_+\). If it was a row of \(M_-\), it is removed. Every non-centre site of a new-member block is therefore a node of \(M_-\) and not a node of \(M_+\): higher-level rows end at level-\((j+1)\) sites, and lower-level rows do not reach \(\Omega_j\)'s interior.

**The chart** (st1-r3 F2, line 825; SA QC19–QC24, 8221–8299). These are \(q_V,K_V,h_V,\mathsf C_V,R_V\), the fixed point \(d\), \(\Psi_V(t)=t-h_Vd(t)\), the graph \(a_V(u)=\Psi_V(\mathsf C_Vu)\), and the radii \(r_1,r_u,r_{\rm sol}\) with constant \(C_{\rm ch}\). Two structural facts are used repeatedly.

* (S1) Each \(d(c)\) depends only on \(t(b_0(c))\) and the free entries of its double block (SA 8283–8285). Hence the pivot block of \(D\Psi_V\) is block diagonal over \(c\), with \(3\times3\) blocks \(I_3-J_c^{-1}\partial_{t(b_0(c))}d(c)\). The free block of \(D\Psi_V\) is the identity (SA 8344–8347).
* (S2) Every derivative bound in F2 holds with the same constants at every reference in the admitted complex reference ball. Gauge condition numbers are charged as in SA 8373–8377.

**The measure** (st1-r3 F3, line 849). Put \(Q(a)=\tfrac12\operatorname{tr}a^2\) and \(S(z)=(\sin\sqrt z/\sqrt z)^2\), an entire function. Then
\[
 d\nu_W(B)=(\sigma_Hg^3)^{|\mathfrak F|}\Big[\prod_c(\det J_c)^{-1}\Big]\det D\Psi_V(\mathsf C_VgB)\prod_{b\in\mathfrak E}S(Q(a_V(gB)(b)))\,dB, \tag{F3}
\]
with \(V\) any real reference in the fibre over \(W\), and (F0) of st1-r3.

**The datum map** (st1-r3 F4, line 874). \(U_+\) is the canonical continued background of the new datum \(D_+\), \(V=M_-(U_+)\), \(D_{\rm old}(B)=e^{ia_V(gB)}V\) on \(\mathfrak E\), and \(\mathcal T_j=\{g\|B\|_\infty<C_{\rm tube}\delta'\}\) with \(C_{\rm tube}=9/4\).

**ST-test** (st1-r3 line 152). Every free removed row is tested against \(V^\sharp=M_-(U^\sharp_+)\) at \(\delta'\). Every removed row, pivots included, lies within \(r_{\rm sol}/4\) of \(V^\sharp\). The reference is formed from data in \(X^\sharp\) by a specified local boundary rule. Here
\[
 h_j:=\max_{b\in\mathfrak E}|i^{-1}\operatorname{Log}(V^\sharp(b)V(b)^{-1})|.
\]

Norms: for traceless \(X\in\mathfrak{su}(2)\), the operator norm is \(|X|=\sqrt{Q(X)}\). For complex \(X=Y+iZ\), \(|X|\le|Y|+|Z|\).

### 1.2 What the sources store (quoted by line)

* **Two layers.** SA 17499 says a step acts at the level of measures by positive kernels. Every formula (Gaussian weights, Jacobians, expansions) "only recasts an integrand in another form". The formulas are formed on the supports and "there coincide with the measures".
* **Stored operation of a step.** SA 7133–7136 and 17531: the one-step operation \(\mathbf T^{(j)}\) is a Haar integral over \(V_j\) on \(\Omega^c_{j+1}\) with the delta function \(\delta(\mathcal M(V_j)V_{j+1}^{-1})\), the gauge factor \(\mathfrak G_j\), tests \(\chi\chi^c\), the factor \(z^{(j)}\), and a Lebesgue integral \(\int dA'\) over the stored field on \(\Omega_{j+1}\setminus\Lambda_{j+1}\) with tests and a Gaussian weight.
* **The gauge factor.** SA 7178–7181: block axial means \(V(y,x)=\mathbf 1\) on the averaged contour variables. It is imposed softly by
  \(\mathfrak G_k(V;P'')=\prod_{y\in P''}\prod_{x\in B(y)\setminus y}z_{\mathfrak G}^{-1}\mathbf 1\{|V(y,x)-\mathbf 1|<\varepsilon_k\}e^{-x_k(1-\frac12\operatorname{Re}\operatorname{tr}V(y,x))}\).
  SA 7595: \(\mathfrak G_k\) is inserted before the fluctuation test that determines \(\Omega_{k+1}\).
* **The main-step coarea identity and the Jacobian convention.** SA 7481–7487 give the local coarea identity, with factor \(z^{(k)}\) and exponent \(\operatorname{Tr}\log(1-\mathsf h\,\partial\tilde D)+\sum_b\log\sigma_{\rm H}(\mathcal A(b))\). After division by \(\sigma_{\rm H}(0)\), SA 7487 says the Jacobians "are included in \(\mathbb P^{(k)}\)". The factor \(\sigma_{\rm H}(0)\), once per non-pivot bond, is absorbed into the constant of the step. SA 7496 puts \(\log\sigma_{\rm H}(0)-\tfrac12(N^2-1)\log x_k\) per non-pivot bond into \(\mathsf E^{(k)}\).
* **The expansion with gauge fixing.** SA 7604: \(x_k[A(U_k(V_k))+\mathrm{GF}_k(V_k)]=x_kA(U_{k+1})+\frac12\langle B,\Delta^{(k)}B\rangle+\sum_bO(g_k|B|^3)\). There is no linear term. SA 9676: the block axial gauge through which \(V^{\rm bg}_k\) is defined "is formed with the mean".
* **The two axial representatives.** SA 9667 defines the axial gauge outside the nodes by comb transports \((\mathcal M^nU)(\Gamma_{z,x})=\mathbf 1\), where \(z\) is the centre of \(x\)'s block. SA 9669–9676: using the averaged contour variable \((\mathcal M^nU)(z,x)\) instead gives a second gauge of the same kind, with exactly one element per orbit. The two representatives differ by an element of \(\mathcal G^{\rm res}\). `a1-balaban.md` line 2501: the contour variable "can be either the comb or the actual mean". `p81-crit-draft.md` §4.3 records the same.
* **The stage recursion.** CA-I 54280: the density at stage \(n\) is \(\exp A^{(n)}(U^{(n)}_k)\). CA-I 54283–54285 split off the constant-coupling Wilson term \(-g_j^{-2}A\). CA-I 54287–54300 (Bałaban (1.60)) give the display
  \[
  \chi^{(n+1)}_k e^{A^{(n)}(U^{(n+1)}_k,A_j=0)+E^{(j)}_0}
  \int dA_j\,\chi^{(j)}e^{-\frac12\langle A_j,C^*\Delta^{(j)}_{\Lambda_{j+1}}CA_j\rangle}
  \,z^{(j)}\!\int dB_j\,\chi'^{(j)}e^{-\frac12\langle B_j,C^*\Delta^{(j)}CB_j\rangle+\mathbb P^{(j)}+\mathfrak K^{(n)}}. \tag{1.60}
  \]
  CA-I 54301–54311 define \(\mathfrak K^{(n)}\) exactly, as the increment of \(\mathfrak E^{(n)}-W^{(n)}\) between the shifted background and \((U^{(n+1)}_k,A_j=0)\). CA-I 54289–54290 say only that expanding \(-g_j^{-2}A\) to second order produces the Gaussian forms, the remainder \(\mathbb P^{(j)}\) and the normalisations.
* **Integration variables.** CA-I 74314–74320: the bonds of integration of stage \(n+1\) are \((\Omega^c_{j+1}\setminus Z''_{j+1})^{(j)*}\), carrying \(B_j\). The rim \(Z_{j+1}\cap\Omega_{j+1}\cap Z\) carries \(A_j\).
* **Bałaban's collar variable.** CA-I 81735–81741 quote Bałaban (1.53): \(V'_j=V_j(V^{(j)})^{-1}\), \(V^{(j)}=M_j(U^{(n+1)}_k)\), \(B'_j=(1/i)\log V'_j\). The delta functions are linearized and removed with the operator \(C\), and then \(B'_j=g_jB_j\). CA-I 81750–81756: the stage terms are evaluated at \(U^{(n)}_k(\exp i[g_jCB_j-h\tilde D(g_jCB_j)]V^{(j)})\). CA-I 81829: on the bonds where \(B_j\) is independent, \((CB_j)(b)=B_j(b)\).
* **Y3 templates.** Y3 46258–46387 (Proposition II-26-53/55) give the integrated coarea identity with all Haar factors. Y3 51884–51936 give the Gaussian structure with conditional mean and its hypotheses. Y3 51984–52015 give the contour estimate. Y3 52091–52134 give the bump deformation with a fixed boundary.

### 1.3 Inputs

All inputs of st1-r3 §2 are retained: GEO, CH, A1/F0/REG, P82°–M1 with (15), OPS/SLICE/UNQ, DR, ST-test, LOC, RUN, RUN-low. Three further items are used.

* **GEO-slot [input].** The CA-I integration bonds of \(B_j\) (CA-I 74315) are exactly the free removed rows \(\mathfrak F\) of st1-r3, and the CA-I rim bonds (74318–74320) carry the stored slots integrated at this stage. This matches the two row sets of two descriptions of one geometry. The correspondence of CA-I's region sets with st1-r3's row sets (CA-I 53758–53814) is not re-derived here.
* **ST-test^hol [input; design specification].** ST-test's local boundary rule is holomorphic in the new datum. One example: copy \(D_+\) on \(X^\sharp\) and a fixed real datum outside. The reference \(U^\sharp_+\) is the canonical representative of the localized datum, in the same convention as \(U_+\). This only completes "a specified local boundary rule" of st1-r3 line 152.
* **Amendment CV [definition change; Section 3.4].** The canonical representative uses the mean contour variable, not the comb.

---

## 2. F-measure

### 2.1 Haar measure and the group delta

**Lemma FM1 (exponential coordinates) [proved; standard].** For \(W_0\in SU(2)\), the map \(a\mapsto e^{ia}W_0\), \(|a|<\pi\), is a real-analytic diffeomorphism onto \(SU(2)\setminus\{-W_0\}\). Haar measure there is \(\sigma_HS(Q(a))\,d^3a\), with a fixed \(\sigma_H>0\). With \(\delta_G\) normalized by \(\int dX\,\delta_G(XY^{-1})f(X)=f(Y)\) for Haar \(dX\), one has \(\delta_G(e^{iv}Y\,Y^{-1})=\sigma_H^{-1}\delta_{\mathbb R^3}(v)\) near \(v=0\).

*Proof.* Right invariance reduces to \(W_0=\mathbf 1\). \(SU(2)\) is the unit sphere \(S^3\subset\mathbb H\). For \(|a|=r\), \(e^{ia}\) lies at geodesic distance \(r\) from \(\mathbf 1\) along the direction \(a/r\). The volume form in geodesic polar coordinates is \(\sin^2r\,dr\,d\Omega_2\), and \(r^2dr\,d\Omega_2=d^3a\). So the density is \((\sin r/r)^2=S(Q(a))\), up to the constant \(\sigma_H\). The delta statement follows: \(\int\sigma_HS(Q(v))d^3v\,\sigma_H^{-1}\delta(v)f=S(0)f=f\). SA 8314–8318 state the same normalization. ∎

### 2.2 The fibre measure is the conditional law

**Proposition FM2 (fixed-reference coarea) [proved; 4D port of Y3 46302–46386].** Let \(V_0\) be a real reference in the CH chart, with \(W_0=F(V_0)\). Write \(\Psi_0,\mathsf C_0,h_0,K_0,R_0\) for the F2 maps at \(V_0\), and \(\mathcal B_0=\{(u,v):\|\mathsf C_0u+h_0v\|_\infty<r_1\}\). Put
\[
 \Lambda_0(u,v)=e^{i\Psi_0(\mathsf C_0u+h_0v)}V_0\ \text{on }\mathfrak E .
\]
1. \(F(\Lambda_0(u,v))=e^{iv}W_0\) and \(\Lambda_0(u,v)|_{\mathfrak F}=e^{iu}V_0|_{\mathfrak F}\).
2. On a neighbourhood \(\mathcal B'_0\subset\mathcal B_0\) of zero, \(\Lambda_0\) is a real-analytic diffeomorphism onto an open set \(\mathcal O_0\subset SU(2)^{\mathfrak E}\).
3. For every Borel \(\Upsilon\ge0\) on \(SU(2)^{\mathfrak E}\) vanishing off \(\mathcal O_0\),
\[
 \int\Upsilon(D)\prod_{b\in\mathfrak E}dD(b)=\int_{SU(2)^{\mathfrak C}}\prod_cdW(c)\ \mu^{(0)}_W[\Upsilon], \tag{2.1}
\]
\[
 \mu^{(0)}_W[\Upsilon]=\sigma_H^{|\mathfrak F|}\prod_c\frac{(\det J_c(V_0))^{-1}}{S(Q(v_c))}\int du\,\det D\Psi_0(\mathsf C_0u+h_0v)\prod_{b\in\mathfrak E}S(Q(a(b)))\,\Upsilon(\Lambda_0(u,v)), \tag{2.2}
\]
where \(W=e^{iv}W_0\) and \(a=\Psi_0(\mathsf C_0u+h_0v)\).

*Proof.* (1) By F2, \(q_{V_0}(\Psi_0(t))=K_0t\) on the contraction ball. With \(t=\mathsf C_0u+h_0v\), we have \(K_0t=v\), because \(K_0\mathsf C_0=0\) and \(K_0h_0=I\). By the definition of \(q_{V_0}\), \(F_c(e^{ia}V_0)=e^{iq_{V_0,c}(a)}F_c(V_0)\). This proves the first identity. \(\Psi_0\) changes only pivot values (SA 8278). \((\mathsf C_0u)|_{\mathfrak F}=u\) and \((h_0v)|_{\mathfrak F}=0\). This proves the second.

(2) The linear map \(L_0:(u,v)\mapsto\mathsf C_0u+h_0v\) is block lower triangular in the (free, pivot) splitting. Its blocks are \(I\) and \(J^{-1}=\operatorname{diag}(J_c^{-1})\). It is therefore invertible, with determinant \(\prod_c(\det J_c)^{-1}\), and with inverse \(t\mapsto(t|_{\mathfrak F},K_0t)\). By F2, \(\|D\Psi_0-I\|\le CL^5\|t\|<1/2\) on the ball, so \(\Psi_0\) is a local diffeomorphism. SA 8279–8281 give the inverse \(\Psi_0^{-1}(a)=a+h_0R_0(a)\) on a smaller neighbourhood, by uniqueness of the fixed point. Hence \(\Psi_0\) is injective there. By FM1, the exponential is a diffeomorphism row by row. The composite is injective with invertible differential, so it is a diffeomorphism onto its open image. Take \(\mathcal B'_0\) to be the corresponding neighbourhood.

(3) By FM1, \(\prod_{\mathfrak E}dD(b)=\sigma_H^{|\mathfrak E|}\prod_{\mathfrak E}S(Q(a(b)))\,da\). Next, \(da=\det D\Psi_0(t)\,dt\), and \(\det D\Psi_0>0\). Indeed, by (S1) it is a product of \(3\times3\) determinants of matrices within \(1/2\) of \(I_3\) in operator norm, each joined to \(I_3\) by a segment of invertible matrices. Then \(dt=\prod_c(\det J_c)^{-1}du\,dv\). At a real reference \(J_c\) lies within half of \(L^{-3}I_3\) in a local unitary frame (SA 8209–8218, 8323–8328). The adjoint frame changes have determinant one, so \(\det J_c>0\). By FM1 on \(SU(2)^{\mathfrak C}\), \(dW=\sigma_H^{|\mathfrak C|}\prod_cS(Q(v_c))\,dv\). Tonelli over \((u,v)\) and \(|\mathfrak E|-|\mathfrak C|=|\mathfrak F|\) give (2.1)–(2.2). No finiteness is needed for Tonelli. ∎

**Corollary FM3 (F3 is the conditional law) [proved].** Let \(W\mapsto V_W\) be a continuous family of real in-fibre references in the chart, \(F(V_W)=W\). The stage's \(W\mapsto V_{M_+(\Phi(W))}\) is real-analytic. Then for every admitted \(W\), the measure \(\nu_W\) of (F3), pushed to \(SU(2)^{\mathfrak E}\) by \(B\mapsto e^{ia_{V_W}(gB)}V_W\), equals \(\mu^{(0)}_W\) whenever \(W\) lies in the image region of a chart \(\Lambda_0\). In particular \(\nu_W\) does not depend on the in-fibre reference. The family \((\nu_W)\) is the unique disintegration of Haar measure along \(F\) that is continuous in \(W\) on continuous compactly supported test functions. So (F0) at \(W=D_+\) is the actual conditional law of the removed rows given the new datum.

*Proof.* Fix \(W_1\) and take \(V_1:=V_{W_1}\) as the reference of a second chart \(\Lambda_1\).

(a) At \(v=0\), \(\Lambda_1(u,0)=e^{ia_{V_1}(u)}V_1\) is the graph of F2, and \(S(Q(0))=1\). So (2.2) at \(W=W_1\) is (F3) at \(W_1\), after \(u=gB\) and \(du=g^{3|\mathfrak F|}dB\).

(b) Let \(\Upsilon\) be continuous with compact support in \(\mathcal O_0\cap\mathcal O_1\). For \(i=0,1\), \(W\mapsto\mu^{(i)}_W[\Upsilon]\) is continuous, by dominated convergence: the integrand is continuous in \((u,v)\) with compact support. Apply (2.1) to \(\Upsilon\cdot(f\circ F)\), with \(f\ge0\) continuous on \(SU(2)^{\mathfrak C}\). Since \(f(F(\Lambda_i(u,v)))=f(W)\), this gives \(\int dW\,f(W)(\mu^{(0)}_W-\mu^{(1)}_W)[\Upsilon]=0\) for all such \(f\). A continuous function orthogonal to every continuous \(f\) against Haar measure, which has a positive continuous density in charts, vanishes identically. So \(\mu^{(0)}_W[\Upsilon]=\mu^{(1)}_W[\Upsilon]\) for every \(W\), in particular at \(W_1\).

(c) Two Radon measures on an open subset of a manifold that agree on \(C_c\) are equal (Riesz). This gives equality on the overlap. Cover the chart region by finitely many such charts. Uniqueness among continuous disintegrations is (b). ∎

*Remark.* For merely Borel \(\Upsilon\), a disintegration is determined only for almost every \(W\). The formula (F3) selects the version that is continuous on continuous test functions. This is the version the stored formula uses, because SA 8342–8343 interpret the group delta "by this change of coordinates", and that change is (F3). No almost-everywhere-to-everywhere inference is made.

### 2.3 Uniqueness of the coordinates and change of reference

**Lemma FM4 (the chart is determined by its reference and its free set) [proved].** Fix a real or complex reference \(V\) in the chart, and the pivot set of SA 8167–8169.

(i) Let \(C:\mathbb C^{3|\mathfrak F|}\to\mathbb C^{3|\mathfrak E|}\) be linear, with \((Cu)|_{\mathfrak F}=u\) and \(K_VCu=0\). Then \(C=\mathsf C_V\).

(ii) Let \(a\) solve \(q_V(a)=0\) with \(a|_{\mathfrak F}=u\), \(\|a\|<r_{\rm sol}\), \(\|u\|<r_u\). Then \(a=a_V(u)\).

*Proof.* (i) \(Cu-\iota u\) is supported on pivots, and \(K_V(Cu-\iota u)=-K_V\iota u\). The pivot block of \(K_V\) is \(\operatorname{diag}(J_c)\), which is invertible. So \(Cu-\iota u=-h_VK_V\iota u\), and \(C=\iota-h_VK_V\iota=\mathsf C_V\) by (QC19). This is `shift-map.md` (32), credited there. (ii) is the converse in F2 (SA 8297–8299). ∎

**Lemma FM5 (change of free reference) [proved].** Let \(V\) be a real in-fibre reference and \(V'\) any real reference with \(|i^{-1}\operatorname{Log}(V'(b)V(b)^{-1})|<r_u/4\) on \(\mathfrak F\). \(V'\) need not lie in the fibre. Define \(B'\) on free rows by \(D(b)=e^{igB'(b)}V'(b)\), \(|gB'(b)|<\pi\), and
\[
 u(B')(b)=i^{-1}\operatorname{Log}(e^{igB'(b)}V'(b)V(b)^{-1}).
\]
Then, on the set where \(\|u(B')\|<r_u\),
\[
 d\nu_W=(\sigma_Hg^3)^{|\mathfrak F|}\prod_{b\in\mathfrak F}S(g^2Q(B'(b)))\ \Pi_V(u(B'))\,dB', \tag{2.3}
\]
\[
 \Pi_V(u):=\prod_c(\det J_c(V))^{-1}\,\det D\Psi_V(\mathsf C_Vu)\prod_cS(Q(a_V(u)(b_0(c)))) .
\]

*Proof.* Split (F3) as the free factor \(\prod_{\mathfrak F}\sigma_HS(Q(u(b)))\,d^3u(b)\) times \(\Pi_V(u)\). By FM1 at \(W_0=V(b)\), the free factor is the product of the Haar measures \(dD(b)\) on free rows. By FM1 at \(W_0=V'(b)\), the same Haar measure equals \(\sigma_Hg^3S(g^2Q(B'(b)))\,d^3B'(b)\). Both charts cover the relevant set of \(D(b)\), since all logarithms are below \(\pi\). ∎

**Lemma FM6 (Bałaban's collar variable) [proved, given GEO-slot].** On the free rows, CA-I's \(B_j\) (81735–81756, 81829) equals \(g^{-1}i^{-1}\operatorname{Log}(V_jV^{(j)-1})\) with \(V^{(j)}=M_j(U^{(n+1)}_k)\). The CA-I configuration \(\exp i[g_jCB_j-h\tilde D(g_jCB_j)]V^{(j)}\) is \(e^{ia_{V^{(j)}}(gB_j)}V^{(j)}\). Hence:
1. If \(U^{(n+1)}_k\) is the representative \(U_+\) of Theorem F4, then \(B_j=B\) exactly.
2. Otherwise \(U^{(n+1)}_k=U_+^w\) with \(w\in\mathcal G^{\rm res}(M_+)\). Then \(V^{(j)}=V^{w}\) is another in-fibre reference, and \(B_j\) and \(B\) are related by the per-row map of FM5, with Jacobian (2.3).

*Proof.* By CA-I 81829, \(B'_j=g_jB_j\) on independent bonds, and \(B'_j\) is the logarithm relative to \(V^{(j)}\) by (1.53) as quoted at 81737. By FM4(i), the operator \(C\) with which "the δ-functions are removed" is \(\mathsf C_{V^{(j)}}\), since it keeps free values and solves the linearized constraint. The map \(\tilde D\) of SA 7481 is the unique small solution of \(\mathcal Q_1(L(\mathcal A'-\mathsf h\tilde D))=LQ\mathcal A'\). With \(K_Vh_V=I\), this is the fixed-point equation \(d=R_V(t-h_Vd)\) of F2. So \(g_jCB_j-h\tilde D(g_jCB_j)=\Psi_{V^{(j)}}(\mathsf C_{V^{(j)}}gB_j)=a_{V^{(j)}}(gB_j)\). For (2): \(U^{(n+1)}_k\) is a regular critical background of the datum \(D_+\) for \(M_+\). By uniqueness of the regular critical orbit (st1-r3 Lemma 5), it equals \(U_+^w\) with \(w\) residual. The average is covariant, so \(M_-(U_+^w)=M_-(U_+)^{w}\). Since \(w=\mathbf 1\) at \(M_+\) nodes, \(F(V^w)=F(V)^{w}=D_+\). ∎

### 2.4 The stage identification

Let \(\mathfrak r\) be the rim slots integrated at the stage (GEO-slot), with real coordinates \(\mathfrak a\in\mathbb R^{3|\mathfrak r|}\). The **stage integrand** is a Borel function
\[
 \Theta(\mathfrak a,D)=\Xi(\mathfrak a,D)\,e^{\mathcal A(\mathfrak a,D)}\ge0 .
\]
Here \(\Xi\ge0\) collects every indicator-type stored factor: the tests and gauge indicators of the stored step, the older tests, the rim test \(\chi^{(j)}\), and the outer test \(\chi^{(n+1)}_k\). \(\mathcal A\) is the total exponent on \(\operatorname{supp}\Xi\). It contains the stage-\(n\) action \(A^{(n)}\) at the stage-\(n\) configuration, the stored rim Gaussian exponent and its normalizer, and the smooth stored gauge-fixing exponents \(-x_j(1-\frac12\operatorname{tr}D(y,x))\). Retained rows, older stored coordinates and \(D_+\) are parameters. The passing test is \(\chi_\sharp\) (ST-test). Write \(\mathcal A=\mathcal W+\mathcal K\), where \(\mathcal W=-g_j^{-2}A\) is the constant-coupling Wilson part at the stage background \(\Phi_-(D)\) (CA-I 54283–54285) and \(\mathcal K\) is the rest.

**Definitions (FM-def).** Choose any symmetric bilinear forms \(S_{\mathfrak a}\) on the rim slots and \(S_B\) on \(\mathbb C^{3|\mathfrak F|}\). Put \(D(B)=e^{ia_V(gB)}V\), and:
\[
\begin{gathered}
 z^{(j)}:=\prod_c(\det J_c(V))^{-1},\qquad E^{(j)}_0:=|\mathfrak F|\log(\sigma_Hg^3),\\
 J_{\rm rel}(B):=\sum_c\log\det\bigl(I_3-J_c^{-1}\partial_{t(b_0(c))}d(c)\bigr)\big|_{t=\mathsf C_VgB}+\sum_{b\in\mathfrak E}\log S\bigl(Q(a_V(gB)(b))\bigr),\\
 \mathfrak K^{(n)}(\mathfrak a,B):=\mathcal K(\mathfrak a,D(B))-\mathcal K(0,V),\\
 \mathbb P^{(j)}(\mathfrak a,B):=\mathcal W(\mathfrak a,D(B))-\mathcal W(0,V)+\tfrac12\langle\mathfrak a,S_{\mathfrak a}\mathfrak a\rangle+\tfrac12\langle B,S_BB\rangle+J_{\rm rel}(B).
\end{gathered}
\]
All logarithms are principal. The arguments lie within \(1/2\) of \(1\): by (S1) and F2, each \(3\times3\) block is within \(CL^5\|t\|<1/2\) of \(I_3\), and \(|S(Q(a))-1|\le Q(a)\le\|a\|^2\). So \(J_{\rm rel}\) is holomorphic and \(J_{\rm rel}(0)=0\). Then \(\det D\Psi_V(\mathsf C_VgB)\prod_{\mathfrak E}S(Q(a))=e^{J_{\rm rel}(B)}\), by (S1).

\(\mathfrak K^{(n)}\) is CA-I's definition (54301–54311), written in these coordinates. \(\mathbb P^{(j)}\) is the remainder of the constant-coupling Wilson term, plus the relative chart Jacobian, as SA 7487 prescribes for the main step.

**Theorem FM (stage identification) [proved].** Assume the inputs of st1-r3 used by F2–F4, GEO-slot, and that \(\operatorname{supp}\chi_\sharp\) lies in the F2 chart of \(V\). F4 and its ST-test proof give this. Let
\[
 \mathcal I[\Theta](D_+):=\int d\mathfrak a\int\prod_{b\in\mathfrak E}dD(b)\prod_{c}\delta_G\bigl(F_c(D)D_+(c)^{-1}\bigr)\chi_\sharp(D)\Theta(\mathfrak a,D),
\]
with the inner integral defined by (F3) and Corollary FM3. Then:

(a) **Chart form.** \(\mathcal I[\Theta](D_+)=\int d\mathfrak a\int\chi_\sharp\Theta(\mathfrak a,D(B))\,d\nu_{D_+}(B)\).

(b) **Measure level.** For every Borel \(f\ge0\) supported in the admitted datum region,
\(\int f(D_+)\mathcal I[\Theta](D_+)\prod_cdD_+(c)=\int d\mathfrak a\int f(F(D))\chi_\sharp\Theta(\mathfrak a,D)\prod_bdD(b)\).
So summing over histories recovers the stored Haar integral; this is SA 17499's statement that the formula coincides with the measure on the support.

(c) **The display.** With the definitions (FM-def),
\[
 \mathcal I[\Theta](D_+)=e^{\mathcal A(0,V)+E^{(j)}_0}\int d\mathfrak a\,e^{-\frac12\langle\mathfrak a,S_{\mathfrak a}\mathfrak a\rangle}\,z^{(j)}\!\int dB\,\chi_\sharp(D(B))\,\Xi(\mathfrak a,D(B))\,e^{-\frac12\langle B,S_BB\rangle+\mathbb P^{(j)}+\mathfrak K^{(n)}} . \tag{2.4}
\]
This is CA-I's display (1.60) in these coordinates. Its outer factor \(e^{A^{(n)}(U^{(n+1)}_k,A_j=0)+E^{(j)}_0}\) is \(e^{\mathcal A(0,V)+E^{(j)}_0}\). Its characteristic functions are \(\Xi\) and \(\chi_\sharp\), with \(\chi'^{(j)}\) replaced by the stage's actual passing test. Its \(B_j\) is \(B\) when \(V^{(j)}=V\) (FM6); otherwise apply FM5. Every stored density and test is retained: \(\Xi\), the stored rim weight inside \(\mathcal A\), the gauge factors, \(z^{(j)}\), and the full chart Jacobian (\(E^{(j)}_0\), \(z^{(j)}\), \(J_{\rm rel}\)).

(d) **The failing piece.** The complementary operation \(\int\cdots(1-\chi_\sharp)\Theta\) is not transformed. It keeps its stored form, as SA 17654 requires for drop-outs.

*Proof.* (a) is (F0) of st1-r3, valid by Corollary FM3, with \(\omega\) the \(\mathfrak a\)-dependent density \(\Theta(\mathfrak a,\cdot)\). Tonelli puts the Lebesgue rim integral outside. The rim variables are not constrained by the delta functions, and they are already Lebesgue coordinates in the stored operation (SA 7136, 17531), so no change of variables acts on them.

(b) Apply (2.1) on each chart of a finite cover, with \(\Upsilon=f\circ F\cdot\chi_\sharp\Theta(\mathfrak a,\cdot)\). Use FM3 to replace \(\mu^{(0)}_W\) by \(\nu_W\), then Tonelli in \(\mathfrak a\). A partition of unity subordinate to the cover handles overlaps.

(c) Insert (F3) into (a). The density is \((\sigma_Hg^3)^{|\mathfrak F|}z^{(j)}e^{J_{\rm rel}(B)}\). Then \(\Theta=\Xi e^{\mathcal A}\), and \(\mathcal A(\mathfrak a,D(B))=\mathcal A(0,V)+[\mathcal W(\mathfrak a,D(B))-\mathcal W(0,V)]+\mathfrak K^{(n)}\). Adding and subtracting the two quadratic forms gives (2.4) identically. Nothing is estimated; (2.4) is exact for every choice of \(S_{\mathfrak a},S_B\). The pairing of names with CA-I is FM6 and GEO-slot.

(d) holds by definition: the failing piece is a different integral, and none of (a)–(c) touches it. ∎

**Proposition FM7 (the relative Jacobian is not one) [proved].** Let \(\mathbb P_0\) be \(\mathbb P^{(j)}\) with the pivot Haar terms \(\sum_c\log S(Q(a_V(gB)(b_0(c))))\) removed. Then (2.4) with \(\mathbb P_0\) in place of \(\mathbb P^{(j)}\) is false for some Borel \(\Theta\ge0\) supported in the chart.

*Proof.* The ratio of the two integrands is \(\prod_cS(Q(a_V(gB)(b_0(c))))\). By F2, \(a_V(u)(b_0(c))=-J_c^{-1}(K_V\iota u)(c)+O(\|u\|^2)\). The linear map \(u\mapsto(K_V\iota u)(c)\) is nonzero. To see this at \(V=\mathbf 1\), take \(c=(y,y+Le_\mu)\) and the free bond \(b=(z,z+e_\mu)\) on the line through \(y\) parallel to \(e_\mu\), with \(y_\mu\le z_\mu<y_\mu+h\). By (QC15), \((K_I\iota e_b)(c)\) is a sum of two terms. The first comes from \(\sigma(y)\): every contour from \(y\) that contains \(b\) crosses it positively, so this term is \(\ge0\). The second comes from the middle sum: \(b\) lies on the straight segment \([x,x']\) from \(x=y\), so this term is \(\ge L^{-4}\). The term \(\sigma(y')\) does not read \(b\), since internal contours stay in \(B(y')\). So the coefficient, a scalar times \(I_3\), is at least \(L^{-4}\). Here \(B(y)\) is taken to be the new-member block of \(c\), so that \(b\) is a free removed row. If instead \(B(y')\) is the new-member block, use the mirror bond in \(B(y')\) with \(y'_\mu-h\le z_\mu<y'_\mu\). Contours from \(y'\) cross it negatively, and \(\sigma(y')\) enters (QC15) with a minus sign, so that term is again \(\ge0\). The segment from \(x=y\) still covers it, since \(z_\mu<y_\mu+L\). The coefficient stays nonzero at nearby \(V\) by continuity. So the zero set of the real-analytic map \(u\mapsto a_V(u)(b_0(c))\) near \(0\) lies in a submanifold of codimension at least one, which has measure zero. Off it, \(0<S(Q(a))<1\), since \((\sin r/r)^2<1\) for \(0<r<\pi\). Take \(\Theta\) to be the indicator of a small ball in \(B\) where this holds: the two sides differ by a strictly positive amount. ∎

**Status of F-measure.** Proved, under the inputs of st1-r3 used by F2–F4 and GEO-slot. FM-def fixes the values of \(z^{(j)},E^{(j)}_0,\mathbb P^{(j)},\mathfrak K^{(n)}\). Here \(\mathfrak K^{(n)}\) is CA-I's own definition, and \(\mathbb P^{(j)}\) is the remainder that SA 7487 describes. Bałaban's own definitions in CMP 122a are not read here. If his \(\mathbb P^{(j)}\) omitted the chart Jacobian, his display would not be exact, by FM7. The draft does not say that it does.

---

## 3. F-contour

### 3.1 The exact cutoff in its own coordinates

Write \(\eta(b):=i^{-1}\operatorname{Log}(V(b)V^\sharp(b)^{-1})\) for \(b\in\mathfrak E\), so that \(V(b)=e^{i\eta(b)}V^\sharp(b)\) and \(|\eta|\le h_j\). For free rows define the **test coordinates**
\[
 B^\sharp(b):=g^{-1}i^{-1}\operatorname{Log}(D(b)V^\sharp(b)^{-1}),\qquad
 u(B^\sharp)(b)=i^{-1}\operatorname{Log}\bigl(e^{igB^\sharp(b)}e^{-i\eta(b)}\bigr),\qquad
 m(b):=\eta(b)/g . \tag{3.1}
\]
Then \(u(m)=0\), so \(B^\sharp=m\) is the point \(D=V\).

**Lemma FC1 (the exact test is a product of centred balls) [proved].** Assume \(h_j\le\delta'/8\) (F6) and the \(\gamma\)-ceiling
\[
 \tfrac98C_{\rm ch}L^4\delta'+\tfrac18\delta'<\tfrac14r_{\rm sol},\qquad \tfrac98\delta'<r_u . \tag{3.2}
\]
On the fibre over \(D_+\), the passing set of ST-test equals the set of chart points \(D=e^{ia_V(u)}V\) whose test coordinates lie in
\[
 \mathsf D_{\mathfrak b}:=\{B^\sharp\in(\mathbb R^3)^{\mathfrak F}:\ |B^\sharp(b)|<\mathfrak b\ \ \forall b\in\mathfrak F\}.
\]
On the chart, \(\chi_\sharp(D)=\prod_{b\in\mathfrak F}\mathbf 1\{|B^\sharp(b)|<\mathfrak b\}\) exactly.

*Proof.* Free part: for \(|gB^\sharp|<\pi\), \(i^{-1}\operatorname{Log}(D(b)V^\sharp(b)^{-1})=gB^\sharp(b)\). So the free test \(|\cdot|<\delta'\) is \(|B^\sharp(b)|<\mathfrak b\).

Pivot part, forward direction. On a chart point with free test passed, the triangle inequality for the bi-invariant distance gives \(|u(b)|<\delta'+h_j\le\frac98\delta'<r_u\) on free rows. F2 gives \(\|a_V(u)\|\le C_{\rm ch}L^4\cdot\frac98\delta'\). Every pivot has logarithm relative to \(V^\sharp\) below \(C_{\rm ch}L^4\frac98\delta'+h_j<r_{\rm sol}/4\) by (3.2). So the pivot clause holds automatically.

Converse. A real fibre point passing both clauses has logarithms relative to \(V\) below \(\frac98\delta'\) on free rows and below \(r_{\rm sol}/4+h_j<r_{\rm sol}/2\) on all rows. By the converse of F2 it is a chart point. This is the argument of F4. ∎

**Proposition FC2 (the stage integral on a fixed real domain) [proved].** At real data,
\[
 \mathcal I[\Theta](D_+)=(\sigma_Hg^3)^{|\mathfrak F|}\int d\mathfrak a\int_{\mathsf D_{\mathfrak b}}dB^\sharp\prod_{b\in\mathfrak F}S(g^2Q(B^\sharp(b)))\,\Pi_V(u(B^\sharp))\,\Theta\bigl(\mathfrak a,e^{ia_V(u(B^\sharp))}V\bigr). \tag{3.3}
\]
Let \(\mathcal T^\sharp_\rho:=\{B^\sharp\in(\mathbb C^3)^{\mathfrak F}:|\operatorname{Re}B^\sharp(b)|+|\operatorname{Im}B^\sharp(b)|<\rho\}\). Suppose the integrand extends holomorphically in \((B^\sharp,D_+)\) to \(\mathcal T^\sharp_{2\mathfrak b}\times\mathcal D_{\rm use}\), where \(\mathcal D_{\rm use}\) is the connected complex datum domain in use, and is bounded there; Lemma FC8 places this extension inside F4's tube. Then the right side of (3.3), with the same fixed real domain \(\mathsf D_{\mathfrak b}\), is holomorphic on \(\mathcal D_{\rm use}\). It is the unique holomorphic continuation of the real stage integral.

*Proof.* (3.3) is FM5 with \(V'=V^\sharp\), together with Theorem FM(a) and FC1. The domain is a fixed compact set, and the integrand is jointly holomorphic and bounded. Holomorphy of the integral follows by differentiation under the integral sign: Cauchy estimates give a locally uniform bound on the parameter derivative. Uniqueness: two holomorphic functions on the connected \(\mathcal D_{\rm use}\) that agree on its real points agree everywhere. The real points form an open subset of \(\mathbb R^n\subset\mathbb C^n\) there. Real and complex derivatives coincide at real points, so all Taylor coefficients at a real point agree, and connectedness gives agreement everywhere. ∎

*Remark.* In F4's coordinate \(B\) (relative to \(V\)), the cutoff is \(\chi_\sharp(e^{ia_V(gB)}V)\). This is not a product of centred balls (st1-r3 line 899), and it is undefined at complex data. In \(B^\sharp\) the same cutoff is the fixed real set \(\mathsf D_{\mathfrak b}\). This removes the "exact cutoff" objection of st1-r3 line 899 without changing the test.

### 3.2 The Gaussian part and its centre

Let \(\mathcal S(D):=S_{\Omega_0}(\Phi_-(D))\). This is the Wilson functional of st1-r3 §1 at the stage background, with the normalization for which st1-r3's backgrounds are critical. Let \(\kappa_j>0\) be the coefficient with which it enters the constant-coupling term. Any plaquettes of Bałaban's \(A\) outside \(\Omega_0\), and any difference between his plaquette function (B-CMP109 (0.1), not read here) and \(\kappa_j\) times st1-r3's, are put into \(\mathcal K\). This is allowed because (2.4) is exact for any split.

**Lemma FC3 (fibre criticality) [proved].** The function \(B\mapsto\mathcal S(e^{ia_V(gB)}V)\) has zero derivative at \(B=0\), at every real datum \(D_+\) and at every complex datum in the admitted connected chart.

*Proof.* Real data first. For real \(B\), \(s\mapsto U(s):=\Phi_-(e^{ia_V(sgB)}V)\) is a real-analytic curve of regular critical backgrounds for \(M_-\) (Lemma 5 of st1-r3). By (67) and F2, \(M_+(U(s))=F(e^{ia_V(sgB)}V)=F(V)=D_+\). So \(U'(0)\in\ker DM_+(U(0))\).

\(U_+\) is critical for \(M_+\). By (67) it is critical for \(M_-\) with datum \(V\). By uniqueness of the regular critical orbit, \(U(0)=U_+^w\) with \(w\in\mathcal G^{\rm res}(M_-)\). Such \(w\) preserves the \(M_-\) datum, hence the \(M_+\) datum. The map \(U\mapsto U^w\) sends the \(M_+\)-fibre of \(D_+\) to itself and preserves \(S_{\Omega_0}\). So \(U_+^w\) is critical on that fibre: the first variation of \(S_{\Omega_0}\) vanishes on \(\ker DM_+(U_+^w)\). Hence \(\frac d{ds}\mathcal S|_{s=0}=dS_{\Omega_0}(U(0))[U'(0)]=0\).

Complex data. The derivative at \(B=0\) is a holomorphic function of the datum on the connected chart (Lemma 5, F2). It vanishes at real data, so it vanishes identically, by the argument of FC2. ∎

**Lemma FC4 (block-gauge zero modes) [proved].** Let \(x\) be a non-centre site of a new-member block \(B(y)\) whose eight incident level-\(j\) bonds lie in \(B(y)\); such sites exist for \(L\ge3\). For \(\lambda\in\mathfrak{su}(2)\), let \(u_s=e^{is\lambda}\) at \(x\) and \(\mathbf 1\) elsewhere. Then:
1. \(s\mapsto V^{u_s}\) stays in the fibre.
2. \(\mathcal S(V^{u_s})=\mathcal S(V)\).
3. The tangent \(\xi\) of this curve has nonzero free coordinates when \(\lambda\ne0\), and the Hessian of \(B\mapsto\mathcal S(e^{ia_V(gB)}V)\) at \(0\) annihilates the corresponding \(B\)-vector.

So a stage Gaussian built from the Wilson part alone is degenerate. Y3's real-reference hypothesis \(S_{\rm r}\ge\gamma_{\rm r}>0\) (Y3 51911) fails for it.

*Proof.* (1) \(x\) is not a coarse site, so \(F(V^{u_s})=F(V)\) by covariance of (5). \(u_s\) changes no retained row: all bonds at \(x\) are removed rows (§1.1). (2) \(M_-\) is covariant, and \(x\) is an \(M_-\) node. The regular critical orbit of \(V^{u_s}\) is the \(\tilde u_s\)-image of that of \(V\), by uniqueness. \(S_{\Omega_0}\) is gauge invariant. (3) The tangent on a bond \(b\) with \(b_-=x\) is \(\lambda\), and on \(b_+=x\) it is \(-\operatorname{Ad}(V(b))\lambda\). These bonds are internal to \(B(y)\), so they are not pivots (SA 8169–8171). A tangent of the fibre is determined by its free coordinates, through the graph of F2. For the Hessian, let \(f\) be the function on the fibre and \(R_s\) the gauge action. Then \(f(R_s(D))=f(D)\) for \(D\) near \(V\). Differentiate in \(s\) at \(0\), and in \(D\) along any tangent \(v\): \(\operatorname{Hess}f_V(\xi,v)+df_V(\partial_s\partial_vR)=0\). Since \(df_V=0\) by FC3, \(\operatorname{Hess}f_V(\xi,\cdot)=0\). ∎

Hence the stage Gaussian must contain a gauge-fixing exponent on the collar. The stored one is SA's \(\mathfrak G_j\) (SA 7181 with \(k=j\); stored by \(\mathbf T^{(j)}\), SA 17531; inserted before \(\Omega_{j+1}\) is determined, SA 7595). Its smooth part is
\[
 \Gamma(D):=x_j\sum_{(y,x)}\bigl(1-\tfrac12\operatorname{tr}D(y,x)\bigr),
\]
summed over the pairs of the new-member blocks that carry \(\mathfrak G_j\). Here \(D(y,x)\) is the averaged contour of the level-\(j\) field inside \(B(y)\). For \(SU(2)\), \(\operatorname{Re}\operatorname{tr}=\operatorname{tr}\), so \(\Gamma\) is holomorphic. Pairs of other blocks do not read removed rows: internal contours stay in one block (SA 8171), and a block outside the new member contains no removed row with both endpoints in it. Put
\[
 \mathcal E(D):=-\kappa_j\mathcal S(D)-\Gamma(D).
\]

**Lemma FC5 (the centre is the mean-axial point) [proved].** Let \(V\) be any real in-fibre reference. Define \(u(x):=V(y,x)\) for non-centre sites \(x\) of new-member blocks \(B(y)\), and \(u=\mathbf 1\) elsewhere. Put \(V_{\rm ax}:=V^u\). Then:
1. \(V_{\rm ax}\) is in the fibre and agrees with \(V\) on retained rows.
2. \(V_{\rm ax}(y,x)=\mathbf 1\) for all such \(x\).
3. \(V_{\rm ax}=M_-(U_+^{\tilde u})\) for a real \(\tilde u\in\mathcal G^{\rm res}(M_+)\).
4. \(d\mathcal E\) restricted to the fibre vanishes at \(V_{\rm ax}\).
5. If \(V\) itself has \(V(y,x)=\mathbf 1\) on these blocks, then \(V_{\rm ax}=V\).

*Proof.* Since \(u=\mathbf 1\) at coarse sites, SA 7666 gives \(V^u(y,x)=V(y,x)u(x)^{-1}=\mathbf 1\). This is (2). By §1.1, \(u\) acts only on removed rows, and \(F\) is unchanged. This is (1). For (3), extend \(u\) to fine sites by \(\mathbf 1\). It is \(\mathbf 1\) at every \(M_+\) node. For (4): \(\mathcal S\) is critical at \(V\) (FC3) and invariant along the block-gauge orbit (FC4(2)). With \(R_u(D)=D^u\), we have \(f\circ R_u=f\) on the fibre, so \(df_{V^u}\circ dR_u=df_V=0\). Further, \(\Gamma\ge0\) on real data, because \(|\frac12\operatorname{tr}X|\le1\) for \(X\in SU(2)\). The terms reading removed rows vanish at \(V_{\rm ax}\), and the others are constant on the fibre. So \(V_{\rm ax}\) is a local minimum of the smooth function \(\Gamma\) on \(SU(2)^{\mathfrak E}\), and \(d\Gamma=0\) there. (5) is immediate. ∎

**Definition (canonical stage Gaussian; exact conditional mean).** Let \(V_{\rm ax}\) be as in FC5, and \(B_{\rm ax}\) the F4 coordinate relative to \(V_{\rm ax}\). The canonical stage precision is \(S:=\) the Hessian at \(0\) of \(B_{\rm ax}\mapsto-\mathcal E(e^{ia_{V_{\rm ax}}(gB_{\rm ax})}V_{\rm ax})\). This is complex symmetric at complex data. It is the \(\frac12\langle B,\Delta^{(j)}B\rangle\) of SA 7604 at the stage, with \(\mathrm{GF}\) included. By FC3, FC5 and Taylor's formula, the expansion of \(-\mathcal E\) about \(V_{\rm ax}\) has no linear term. The **exact conditional mean** in test coordinates is the test coordinate of the centre:
\[
 m_{\rm ax}(b):=g^{-1}i^{-1}\operatorname{Log}\bigl(V_{\rm ax}(b)V^\sharp(b)^{-1}\bigr),\qquad b\in\mathfrak F .
\]
Every other non-quadratic part of the exponent, including the rim-slot terms, goes into the holomorphic factor \(G\) of the consumer's estimate. This is the split of Y3 51938–51948 with no auxiliary field.

*Remark (rim slots).* CA-I 54280 says the stage-\(n\) density is \(\exp A^{(n)}(U^{(n)}_k)\), a function of the stage background. In st1-r3 the background depends only on the determining datum, and rim slots are stored slots, not determining rows (st1-r3 line 26). So the stored rim forms are quadratic in the rim slots, with coefficients evaluated at the current background (SA 17558). They contribute no term linear in \(B\) at zero rim slot and no bilinear rim–\(B\) term. Their \(B\)-dependence is a carriage term in \(G\). Bounding it is the consumer's task, not F-contour's. If a Wilson weight read the rim slots bilinearly with \(B\), the mean would acquire \(-S^{-1}R^{\mathsf T}\mathfrak a\), as in `shift-map.md` (16)–(17). This draft does not use that reading.

### 3.3 The comb convention: the counterexample

**Proposition FC6 (exact defect of the comb reference) [proved; counterexample to the mean bound].** Let \(U_+\) be the comb-axial representative (SA 9667, the convention of st1-r3 line 41), and \(V=M_-(U_+)\). Take a new-member block \(B(y)\) and its plaquette \(p=(y,y+e_1,y+e_1+e_2,y+e_2)\) at level \(j\). Write \(e^{iF_p}:=\partial V(p)\) with \(F_p\) in the small branch. Then there is a free removed row \(b''\) of \(B(y)\) with
\[
 i^{-1}\operatorname{Log}\bigl(V_{\rm ax}(b'')V(b'')^{-1}\bigr)=\mp F_p/2 .
\]
Consequently the exact conditional mean of the canonical stage Gaussian, in the coordinates of ST-test with \(V^\sharp\) comb-axial, obeys
\[
 |m_{\rm ax}(b'')|\ge(|F_p|/2-h_j)/g . \tag{3.4}
\]
Whenever \(|F_p|\ge2(\delta'_j+h_j)\), the actual mean lies outside the test ball \(|B^\sharp(b'')|<\mathfrak b\). Then Y3's mean hypothesis \(\theta_{\mathbf m}+\varepsilon_{\mathbf m}<1\) (Y3 51928–51933) fails for the actual conditional mean, and so does F5's requirement (st1-r3 line 898).

*Proof.* Write \(b_1=(y,y+e_1)\), \(b_2=(y,y+e_2)\), \(b'=(y+e_2,y+e_1+e_2)\), \(b''=(y+e_1,y+e_1+e_2)\). All four bonds are internal to \(B(y)\), hence free removed rows (§1.1, SA 8169). The non-centre sites are non-nodes of \(M_+\) with parent \(y\). SA 9667 sets the comb transport of \(\mathcal M^jU_+=V\) from \(y\) to each of them equal to \(\mathbf 1\).

The comb path from \(y\) to \(y+e_\mu\) is the single bond. So \(V(b_1)=V(b_2)=\mathbf 1\). The comb path to \(y+e_1+e_2\) is one of \(b_2b'\) and \(b_1b''\), depending on the comb order. Take it to be \(b_2b'\); the other case exchanges the roles and the sign. Then \(V(b')=\mathbf 1\), and \(\partial V(p)=V(b_1)V(b'')V(b')^{-1}V(b_2)^{-1}=V(b'')\), so \(V(b'')=e^{iF_p}\).

The averaged contour \(V(y,y+e_1+e_2)\) is the mean of the two shortest paths, \(\operatorname{av}(e^{iF_p},\mathbf 1)\). The element \(W=e^{iF_p/2}\) solves \(\operatorname{Log}(e^{iF_p}W^{-1})+\operatorname{Log}(W^{-1})=iF_p/2-iF_p/2=0\), and the solution is unique in the small branch (st1-r3 Lemma 3). So \(u(y+e_1+e_2)=e^{iF_p/2}\) and \(u(y+e_1)=V(b_1)=\mathbf 1\). This is exact; no commutation beyond the one-parameter group \(e^{isF_p}\) is used. Then
\[
 V_{\rm ax}(b'')=u(y+e_1)V(b'')u(y+e_1+e_2)^{-1}=e^{iF_p/2},
\]
and \(i^{-1}\operatorname{Log}(V_{\rm ax}(b'')V(b'')^{-1})=-F_p/2\).

For (3.4), the triangle inequality for the bi-invariant distance gives \(|g\,m_{\rm ax}(b'')|\ge|F_p|/2-|i^{-1}\operatorname{Log}(V(b'')V^\sharp(b'')^{-1})|\ge|F_p|/2-h_j\). Here LOC measures the discrepancy in a common gauge, and both references are comb-axial.

Consequence. By FC5 the centre is \(V_{\rm ax}\) whenever \(\Gamma\) is in the Gaussian. Without \(\Gamma\), the Gaussian is degenerate (FC4). A third split keeps only the quadratic part of \(\Gamma\) in the Gaussian. Its linear part \(\ell\) then sits in \(G\), with \(|\ell(b'')|\) of order \(x_jg\,|F_p|\sim|F_p|/g\). On the tube, \(|e^{\ell\cdot B^\sharp}|\) is as large as \(e^{c|F_p|\mathfrak b/g}\), not bounded uniformly. So no split meets Y3's hypotheses. ∎

*Size.* The stage tests allow level-\(j\) curvature up to order \(\varepsilon_j\) (SA 17612–17624; st1-r3 (58)). Since \(\varepsilon_j/\delta'_j=(A_0/A_1)\ell_j^{p_0-p_1}\to\infty\), the condition \(|F_p|\ge2(\delta'_j+h_j)\) is compatible with every declared bound. No admitted history is constructed here, so (3.4) is a counterexample to the claimed inequality under a stated, admissible-looking condition. It is not a proof that such a history exists. The mechanism is the one st1-r3 line 41 records: comb and averaged conventions "are not identified". SA 9676 already forms the block axial gauge of \(V^{\rm bg}\) with the mean.

### 3.4 Amendment CV and its port

**Amendment CV (definition).** In st1-r3, replace "The canonical background representative uses combs in order (4,3,2,1)" (line 41) by: the canonical background representative is the axial element of SA 9669–9676, with the averaged contour variable \((\mathcal M^nU)(z,x)\) in place of the comb transport. The tower readout, stored transports and ST-test's \(U^\sharp_+\) use the same element.

**Lemma CV (st1-r3 is unchanged in substance under CV) [proved, for each listed use].** The comb convention appears in st1-r3 at lines 41, 128, 276–277, 339, 345, 581 and 1064, and nowhere else (text search for "comb" and "axial"). Under CV:

1. **Lines 41, 1064** (the definition). Replaced as above.
2. **Lines 128, 345** (A1/F0/REG and Lemma 5). SA 9669–9676: the mean-contour gauge has exactly one element per orbit, related to the comb element by \(\mathcal G^{\rm res}\). `a1-balaban.md` 2495–2505 constructs the axial element with "either the comb or the actual mean". The construction uses only locality in \(B(z)\), covariance and the value \(\mathbf 1\) at the zero field (SA 9670–9673). The holomorphic chart is the same contraction with the mean in place of the comb transport. The Federbush mean is holomorphic on its small branch, with Lipschitz bounds uniform in the number \(N\le24\) of paths (st1-r3 Lemma 3, line 274). The conjugator bound of `a1-balaban.md` §9.1 holds with the same proof. REG reads only the orbit and its local gauges (`p82.md`, P81 (8.2) and §3.8), which do not depend on the representative.
3. **Lines 276–277** (Lemma 3). The comb gauge there is an auxiliary real gauge \(g(x)=U(P(x))\) used to bound potentials by curvature. It is not the canonical representative. Unchanged.
4. **Line 339** (LEV). LEV pins the averaged stored transports (line 339: "the convention chosen in (28)"). Unchanged. Under CV the canonical and stored conventions coincide on block contours.
5. **Line 581** (Lemma 8). The recursion \(u_B(x)=u_B(z)(\mathcal M^nW_B)(z,x)\) now uses the mean of at most \(4!\) path products, each of at most \(2(L-1)\) bonds. By Lemma 3's contraction \(|X|\le2\max|w_i|\), each mean is bounded by twice the bound for a single path. The display after line 581 holds with \(C_u\) replaced by \(2C_u\), a constant depending only on \(L\), fixed in row 2.
6. **(15), DR and Lemma 6, used throughout.** Each is stated at an arbitrary real regular critical base \(U_0\) and its datum \(V=M(U_0)\) (st1-r3 lines 129–143, 364). None refers to the choice of representative. Under CV the base is the mean representative, which is a real regular critical base, so each applies as stated, with the same constants. Within one base, the target representative enters only the gauge \(u_B\) of (34). The response \((H,K)\) is fixed by \(q(H)=b_V(B)\) and \(RD^{\mathsf T}H=0\). Changing the target by \(w\in\mathcal G^{\rm res}(M_-)\) replaces \(u_B\) by \(u_Bw\), and leaves \(H,K\) and \(u_B\) at tops unchanged, since \(w=\mathbf 1\) at nodes. One caution. The comb and mean bases of the same \(M_+\)-orbit differ by a gauge that is residual for \(M_+\) but not for \(M_-\). So, for the old system, they are different bases with different data \(V\). Under CV only the mean base is used, so no transfer between them is needed or claimed.

*Proof.* Each item is shown in its line. Items 2 and 6 use only the cited covariance and uniqueness statements. ∎

Under CV, FC5(5) applies: the canonical \(V=M_-(U_+)\) satisfies \(V(y,x)=(\mathcal M^jU_+)(y,x)=\mathbf 1\) on every new-member block. Every non-centre site is an \(M_+\) non-node with parent \(y\) (§1.1). So \(V_{\rm ax}=V\). At complex data the identity \(V(y,x)=\mathbf 1\) continues holomorphically, so \(\Gamma\) has zero linear term there as well. In particular \(m_{\rm ax}=m=\eta/g\), as in (3.1).

### 3.5 The mean bound, the tube, and the deformation (under CV)

**Lemma FC7 (mean bounds at real and complex data) [proved].** Fix \(\varepsilon_{\mathbf m}=1/16\), \(\vartheta_*=1/4\), \(d_*=1-\vartheta_*=3/4\). Assume CV, ST-test^hol, and LOC at every real datum of the admitted real raw-datum chart, as F6 uses it. After a ceiling on \(\gamma\), at every datum in use (real, or complex with raw imaginary part \(\|Y\|_\infty\le y_{\rm use}\)):
\[
 m_{\rm r}:=0,\qquad |m(b)|\le\varepsilon_{\mathbf m}\mathfrak b\ \ (b\in\mathfrak F),\qquad\theta_{\mathbf m}=0 .
\]
The bound is uniform in the decoupling switches and in the independent current, since \(m\) depends on neither.

*Proof.* Real data. By F6 under LOC, \(h_j\le C'_Fe^{-aR_\sharp}S_4(a)\) with \(a=\min(1,\theta_4/2)\).

Complex data. Write \(D_+=e^{i(X+iY)}D^{\rm r}\) with \(D^{\rm r}\) real and \(X,Y\) real raw logarithms. Put \(D(\zeta)=e^{i(X+\zeta Y)}D^{\rm r}\) for \(\zeta\) in the disc \(|\zeta|<\rho_1:=r_B/(2\|Y\|_\infty)\). Assume \(\|X\|_\infty<r_B/2\); this is a choice of \(D^{\rm r}\). Then \(D(\zeta)\) lies in the admitted chart. For real \(\zeta\), \(D(\zeta)\) is real and admitted, so LOC gives \(|\eta(D(\zeta))(b)|\le h_{\mathbb R}:=C'_Fe^{-aR_\sharp}S_4(a)\). On the whole disc \(|\eta|\le M_1:=2r_{\rm sol}\), since both references lie in the chart. By ST-test^hol, \(\zeta\mapsto\eta(D(\zeta))(b)\) is holomorphic. Apply Hadamard's three-lines theorem to \(\log\) of this function on the upper half-disc. The map \(w=(\rho_1+\zeta)/(\rho_1-\zeta)\) sends the diameter to the positive real axis and the semicircle to the positive imaginary axis, and \(\log w\) sends the quadrant to the strip \(0<\operatorname{Im}<\pi/2\). Using \(\rho'_1<\rho_1\) for continuity up to the boundary, the theorem gives at \(\zeta=i\):
\[
 |\eta(D_+)(b)|\le h_{\mathbb R}^{1-\vartheta}M_1^{\vartheta},\qquad \vartheta=\tfrac4\pi\arctan(1/\rho'_1)\le\tfrac{8\|Y\|_\infty}{\pi r_B}+o(1).
\]
The raw imaginary part of a datum in use is at most \(y_{\rm use}\le C_Qr_1(i)\) (AV/CURV, st1-r3 line 127), and \(r_1(i)\to0\) as \(\gamma\to0\). After a ceiling, \(\vartheta\le1/2\). Then \(|\eta|\le M_1^{1/2}(C'_FS_4(a))^{1/2}e^{-aR_\sharp/2}\).

The ceiling. \(R_\sharp\ge MR_t/4\ge c_N\ell_t^r/4\) with \(r>1\). As in F6, \(e^{-c\ell_t^r}/(\varepsilon_{\mathbf m}A_1g_j\ell_j^{p_1})\to0\) uniformly over the stage window, since \(g_j^{-1}=\theta_j^{1/2}\le e^{\ell_j/2}\) and \(\ell^r\gg\ell\). Impose the supremum at most \(1\). Then \(|m|=|\eta|/g\le\varepsilon_{\mathbf m}\delta'/g=\varepsilon_{\mathbf m}\mathfrak b\). Uniformity: \(m\) is a function of \(V\) and \(V^\sharp\) only. These are functions of the data, not of the Gaussian's decoupling switches or the independent current. ∎

*Remark.* The same proof gives the absolute bound \(|m|\le|\eta|/g\to0\), because \(e^{-c\ell^r}g^{-1}\to0\). So even the undeformed real contour leaves only the factor \(e^{c_{\rm r}\|\operatorname{Im}m\|^2}=e^{o(1)|\mathfrak F|}\) of Y3 (II-117-47).

**Lemma FC8 (containment) [proved].** Assume \(h\le\delta'/8\) (FC7) and the \(\gamma\)-ceiling \(2C_\ell\delta'\le1/2\), where \(C_\ell\) is the constant of st1-r3 (24). Then \(B^\sharp\in\mathcal T^\sharp_{2\mathfrak b}\) implies \(\|u(B^\sharp)\|_\infty<\frac94\delta'\). So the corresponding \(B=u/g\) lies in F4's tube \(\mathcal T_j\). In particular Y3's tube \(\{|\operatorname{Re}|+|\operatorname{Im}|<\mathfrak b\}\) lies in \(\mathcal T_j\), with a factor-two margin for Cauchy estimates.

*Proof.* \(|igB^\sharp|\le g(|\operatorname{Re}B^\sharp|+|\operatorname{Im}B^\sharp|)<2\delta'\) and \(|-i\eta|\le h\). By (24),
\[
 |u|\le|gB^\sharp|+h+C_\ell|gB^\sharp|h<2\delta'+\tfrac18\delta'+\tfrac18\delta'=\tfrac94\delta' .
\]
∎

**Proposition FC9 (exact-cutoff deformation) [proved; 4D port of Y3 52091–52134].** Let \(\Phi\) be holomorphic on a neighbourhood of the closure of \(\mathcal T^\sharp_{\mathfrak b}\) and bounded there. Put \(\nu:=\operatorname{Im}m\), with \(|\nu(b)|\le\varepsilon_{\mathbf m}\mathfrak b\). Let \(r_1=1-\frac34d_*\), \(r_2=1-\frac14d_*\), \(h(v)=\min\{1,\max\{0,2d_*^{-1}(r_2-v)\}\}\), \(\phi(\beta)=h(|\beta|/\mathfrak b)\), and
\[
 \Theta_\nu(\beta)(b)=\beta(b)+i\phi(\beta(b))\nu(b),\qquad J_b=1+i\langle\nu(b),\nabla\phi(\beta(b))\rangle .
\]
Then \(\Theta_\nu(\mathsf D_{\mathfrak b})\subset\mathcal T^\sharp_{\mathfrak b}\), \(|J_b|\le e^{2\varepsilon_{\mathbf m}^2/d_*^2}\), and
\[
 \int_{\mathsf D_{\mathfrak b}}\Phi(\beta)\,d\beta=\int_{\mathsf D_{\mathfrak b}}\Phi(\Theta_\nu(\beta))\prod_{b\in\mathfrak F}J_b(\beta)\,d\beta . \tag{3.5}
\]
On the bulk \(|\beta(b)|\le r_1\mathfrak b\), \(\operatorname{Im}(\Theta_\nu(\beta)-m)=0\). The exact boundary of the test is untouched: \(\Theta_\nu=\mathrm{id}\) where \(|\beta(b)|\ge r_2\mathfrak b\).

*Proof.* Containment. Where \(\phi\ne0\), \(|\beta|<r_2\mathfrak b\), so \(|\operatorname{Re}|+|\operatorname{Im}|<r_2\mathfrak b+\varepsilon_{\mathbf m}\mathfrak b\le\mathfrak b\), because \(\varepsilon_{\mathbf m}=1/16\le d_*/4\). Where \(\phi=0\), the point is real with \(|\beta|<\mathfrak b\).

Jacobian bound. \(\langle\nu,\nabla\phi\rangle\) is real, and \(|\nabla\phi|\le2/(d_*\mathfrak b)\). So \(|J_b|=\sqrt{1+\langle\nu,\nabla\phi\rangle^2}\le e^{\langle\nu,\nabla\phi\rangle^2/2}\le e^{2\varepsilon_{\mathbf m}^2/d_*^2}\).

The identity, one bond at a time. Order \(\mathfrak F\) as \(b_1,\dots,b_N\). Suppose bonds \(b_1,\dots,b_{k-1}\) are already deformed, and let \(\Phi_k\) be the resulting integrand. It is holomorphic in \(\beta(b_k)\), on a neighbourhood of the closed region below, for all fixed remaining real values, by composition. If \(\nu(b_k)=0\) there is nothing to do. Otherwise choose orthonormal coordinates on \(\mathbb R^3\) with \(\nu(b_k)=|\nu|e_1\). Fix \((x_2,x_3)\) with \(\rho^2=x_2^2+x_3^2<\mathfrak b^2\), and put \(a=\sqrt{\mathfrak b^2-\rho^2}\). For \(s\in[0,1]\) let \(\gamma_s(x_1)=x_1+is|\nu|\,h\bigl(\sqrt{x_1^2+\rho^2}/\mathfrak b\bigr)\), \(x_1\in[-a,a]\). This is piecewise \(C^1\) in \(x_1\), smooth in \(s\), and \(\gamma_s(\pm a)=\pm a\), since \(\phi=0\) near \(|\beta|=\mathfrak b\). Every point lies in the convex slice of \(\mathcal T^\sharp_{\mathfrak b}\) shown above. With \(f=\Phi_k(\cdot,x_2,x_3)\),
\[
 \frac{d}{ds}\int_{-a}^af(\gamma_s)\gamma_s'\,dx_1=\int_{-a}^a\partial_{x_1}\bigl[f(\gamma_s)\,\partial_s\gamma_s\bigr]dx_1=\bigl[f(\gamma_s)\partial_s\gamma_s\bigr]_{-a}^{a}=0 .
\]
The first equality uses \(f'(\gamma_s)\partial_s\gamma_s\gamma_s'+f(\gamma_s)\partial_s\gamma'_s=\partial_{x_1}[f(\gamma_s)\partial_s\gamma_s]\) on each \(C^1\) piece. The pieces telescope by continuity, and \(\partial_s\gamma_s=0\) at \(\pm a\). Hence the real line integral equals the integral along \(\gamma_1\), whose derivative is \(J_{b_k}\). Integrate over \((x_2,x_3)\) by Fubini: the integrands are bounded and Borel on a bounded set. Iterate over the \(N\) bonds.

Bulk. Where \(\phi=1\), \(\operatorname{Im}\Theta_\nu=\nu=\operatorname{Im}m\). ∎

**Theorem FC (F-contour, under CV) [proved].** Assume the declared inputs of st1-r3, Amendment CV, ST-test^hol, real LOC, GEO-slot, and the \(\gamma\)-ceilings (3.2), FC7 and FC8. At every passing stage:

1. **Exact cutoff.** In the test coordinates \(B^\sharp\), the passing set is exactly \(\mathsf D_{\mathfrak b}\) (FC1).
2. **Fixed-domain continuation.** The stage integral is (3.3) over \(\mathsf D_{\mathfrak b}\). It is the unique holomorphic continuation of the real stage integral to the data in use (FC2).
3. **Exact conditional mean.** The canonical stage Gaussian, the Hessian of the Wilson part plus the stored block-axial gauge exponent, has no linear term at \(V\) (FC3, FC5, CV). Its exact centre in test coordinates is \(m=\eta/g\). The real reference is \(m_{\rm r}=0\), and \(|m|\le\varepsilon_{\mathbf m}\mathfrak b\) at all data in use, uniformly in switches and independent currents (FC7). In Y3's notation this gives \(\theta_{\mathbf m}=0\) and \(\varepsilon_{\mathbf m}=1/16\), so \(\theta_{\mathbf m}+\varepsilon_{\mathbf m}\le\vartheta_*=1/4\).
4. **Containment.** \(\mathcal T^\sharp_{2\mathfrak b}\) lies in F4's tube \(\mathcal T_j\) (FC8). Hence the integrand of (3.3) is holomorphic and bounded there by F4, Lemma 12, Theorem 14 and CI.
5. **Deformation.** The exact-cutoff deformation (3.5) holds for this integrand (FC9).

*Proof.* Combine the cited results. Item 4 needs \(\mathcal T^\sharp_{2\mathfrak b}\) inside F4's tube, so that F4's holomorphic map, (70) and the Theorem 14 composition apply. The remaining premises (regularity and uniqueness balls, source threshold, CI) are st1-r3's own. ∎

### 3.6 What F-contour does not contain

* The conditional-mean estimate itself, Y3 Proposition II-117-69 ported, together with its hypotheses: a real reference precision \(S_{\rm r}\ge\gamma_{\rm r}\), and \(\|S-S_{\rm r}\|\le\hat\varepsilon\) on the decoupling polydisc (Y3 51907–51926). FC4 shows these can hold only with the gauge exponent included. Their proof for the canonical \(S\) belongs to NL1/LF1 and OPS.
* The bound \(F_0\) on the holomorphic factor \(G\). This includes \(\mathfrak K^{(n)}\), the Wilson remainder, \(J_{\rm rel}\), the carriage terms of the rim forms, and the recentring correction \(R_\beta:=\frac12\langle B^\sharp-m,S(B^\sharp-m)\rangle-\frac12\langle\beta,S\beta\rangle\), where \(\beta=u(B^\sharp)/g\). For the last term, (24) gives \(|\beta-(B^\sharp-m)|\le C_\ell|gB^\sharp||\eta|/g\). With \(s_1\) a row-sum bound for \(S\), this yields \(|R_\beta|\le18C_\ell s_1|\mathfrak F|\mathfrak b^2h\) on \(\mathcal T^\sharp_{2\mathfrak b}\). This is an extensive rate that tends to zero, of the kind Y3's \(e^{c_{\rm mn}u_0N_{\rm I}}\) absorbs. It is recorded, not consumed.
* Main steps. The main-step conditional mean, linear in the stored exterior field, and the strip coordinates remain st1-r3's "main-step coordinate/source supply" (line 918).

---

## 4. Constants

| Constant | Where | Fixed at | Before \(\kappa\)? | Independent of \(M,\bar\kappa\)? |
|---|---|---|---|---|
| \(\sigma_H\) | FM1 | absolute | yes | yes |
| \(C_{\rm ch},c_{\rm ch},r_1,r_u,r_{\rm sol}\) | F2 (SA QC18–QC24) | row 2, depend on \(L\) | yes | yes |
| \(C_{\rm tube}=9/4\) | F4 | absolute | yes | yes |
| \(C_\ell\) | st1-r3 (24) | absolute | yes | yes |
| \(\varepsilon_{\mathbf m}=1/16\), \(\vartheta_*=1/4\), \(d_*=3/4\), \(r_1=7/16\), \(r_2=13/16\) | FC7, FC9 | absolute | yes | yes |
| \(2C_u\) | Lemma CV item 5 | row 2, depends on \(L\) | yes | yes |
| \(M_1=2r_{\rm sol}\), \(\rho_1=r_B/(2\|Y\|)\) | FC7 | from row 2/3 radii | yes | yes |
| \(C'_F,a,S_4(a)\) | F6 | row 2 (with (15), Lemma 2) | yes | yes |
| ceilings (3.2), \(2C_\ell\delta'\le\frac12\), \(\vartheta\le\frac12\), FC7's \(e^{-c\ell^r}\le\varepsilon_{\mathbf m}\delta'\) | FC1, FC7, FC8 | row 10: ceilings on \(\gamma\) | n/a (chosen last) | yes |
| \(R_\sharp\ge MR_t/4\) | LOC, F6, FC7 | \(M\) used only as a lower bound | n/a | \(M\) enters only as a lower bound |

No constant fixed before \(\kappa\) reads \(b_f\), \(C_0,C_1\) or \(A_0,A_1\). The ratios \(\varepsilon_j/\delta'_j\) and \(r_1(i)/r_B\) enter only the \(\gamma\)-ceilings and the counterexample's size remark.

---

## 5. Effect on st1-r3 (for the distiller)

1. Replace "Outstanding F-measure" (line 872) by Theorem FM, Corollary FM3 and Proposition FM7. Corollary 14′'s premise "the F-measure identification for every stage presentation being called actual" becomes a consequence, given GEO-slot and FM-def.
2. Replace Lemma F5 and "Outstanding F-contour" (lines 895–899) by Section 3. In the frozen comb convention, F-contour is false whenever \(|F_p|\ge2(\delta'_j+h_j)\) on a new-member block (FC6). Under Amendment CV, Theorem FC proves it. Corollary 14′'s premise "F-contour's bounds and exact-cutoff deformation" then becomes a consequence of CV, ST-test^hol and real LOC.
3. CV requires st1-r3 to reopen at line 41, with Lemma CV checked by the referee. PR-lay already fixes its representative block axial on active blocks (`pr-lay.md` line 60), which is consistent with CV.
4. CI remains Outstanding, owned by NL1/LF1. Nothing here touches it.

---

## 6. Source checks

Each passage was read in a bounded range in `sa/` at `31a47c543775`. Only short phrases are quoted; everything else is paraphrased with its line numbers.

| Passage | Used for |
|---|---|
| SA 7133–7139, 17528–17534 | stored operation \(\mathbf T^{(j)}\): Haar \(dV_j\) with delta on \(\Omega^c_{j+1}\), \(\mathfrak G_j\), tests, \(z^{(j)}\), Lebesgue \(dA'\) with Gaussian |
| SA 7178–7182, 7595, 7660–7666 | block axial gauge factor, its insertion order, Faddeev–Popov identity and \(V^u(y,x)=V(y,x)u(x)^{-1}\) |
| SA 7479–7499 | main-step coarea identity; Jacobians included in \(\mathbb P^{(k)}\); \(\sigma_{\rm H}(0)\) and \(-\frac12(N^2-1)\log x_k\) in the constant |
| SA 7597–7614 | node-free step; expansion with \(\mathrm{GF}_k\) without linear term; conditional Gaussian |
| SA 8165–8240, 8257–8299, 8308–8380 | pivots crossing faces; (QC15)–(QC20); chart and converse; QC25 and holomorphic continuation; condition numbers |
| SA 9664–9677 | comb-axial and mean-axial representatives; the block axial gauge of \(V^{\rm bg}\) formed with the mean |
| SA 17396 | stage tests imply the stored step's tests, including gauge indicators |
| SA 17499–17514, 17516–17558, 17585, 17612–17654 | measure/formula layers; strip; stored and integrated variables; carriage; stage description; stage curvature bounds; drop-out retention |
| CA-I 54226–54335 | stage recursion, (1.60) display, \(\mathfrak K^{(n)}\) definition, fluctuation integral |
| CA-I 74309–74320 | bonds of integration of \(B_j\) and \(A_j\) |
| CA-I 78470–78591 | rotated presentation; the five kinds of arguments, including rim slots and arrested collar variables |
| CA-I 81735–81845 | Bałaban (1.53) quoted; the collar chart \(b(\mathsf B)=g_jC\mathsf B-h\tilde D(g_jC\mathsf B)\); free bonds \((CB_j)(b)=B_j(b)\) |
| Y3 46258–46395 | integrated coarea with all Haar factors (template for FM2) |
| Y3 51852–51936, 51938–52015, 52016–52200 | Gaussian structure with conditional mean; contour estimate; bump deformation with fixed boundary |
| `a1-balaban.md` 2495–2510; `p81-crit-draft.md` 150–158, 198–202 | either contour variable for the axial element |
| `shift-map.md` §§6, 7, 9, 10 | uniqueness of the embedding (32); two slot types; conditional-mean algebra (16)–(17) |
| `pr-lay.md` 58–64 | block axial representative on active blocks |

---

## Result

**F-measure: proved.** The F3 fibre measure is the continuous disintegration of bare Haar measure along the stage average, so it is the actual conditional law (FM2, FM3). Bałaban's collar coordinate is F4's coordinate at Bałaban's reference (FM4, FM6), or differs from it by the explicit map of FM5. The CA-I stage display (1.60) equals the fibre-chart integral exactly, with explicit normalizations and with \(\mathbb P^{(j)}\) containing the full relative chart Jacobian, pivot Haar factors included, as SA 7487 says. The rim integral and every stored density and test are retained, and the failing piece is untouched (Theorem FM). Dropping the pivot Haar factors makes the display false (FM7).

**F-contour: counterexample as frozen; proved under Amendment CV.** The Wilson Hessian on the stage fibre has block-gauge zero modes (FC4). So the stage Gaussian must include SA's stored block-axial gauge exponent, and its exact centre is the mean-axial point (FC5). With st1-r3's comb representative, the exact conditional mean in ST-test coordinates is at least \((|F_p|/2-h_j)/g_j\) on a free row of each new-member block. So the mean bound fails whenever a level-\(j\) plaquette there has \(|F_p|\ge2(\delta'_j+h_j)\) (FC6, an exact computation). Under CV, the mean-contour representative that SA 9669–9676 and A1 §9.1 allow, the centre is \(V\) itself. In ST-test's own coordinates the exact cutoff is a product of centred balls, and the stage integral over that fixed domain is the unique holomorphic continuation. The exact mean is \(m=\eta/g\), with \(m_{\rm r}=0\) and \(|m|\le\frac1{16}\mathfrak b\) at all data in use, by real LOC and the three-lines theorem. The deformed contour lies in \(\mathcal T_j\), and the bump deformation is valid for the exact cutoff (Theorem FC).

**First remaining Outstanding statement.** None inside the two items, under CV. The open points are external or definitional:
* CV changes st1-r3 line 41 and must be refereed with Lemma CV.
* GEO-slot and ST-test^hol are stated inputs.
* The conditional-mean estimate's precision hypotheses and the \(G\)-bound belong to NL1/LF1.
* CI is unchanged.

All mathematical steps are written arguments, and no computation discharges a step. This is research text, not an audit. It grants no status, and it is **not yet refereed**.
