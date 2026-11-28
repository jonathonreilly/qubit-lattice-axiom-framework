# Four-dimensional port of all-mirror positivity
Provenance: Codex (GPT-6; exact runtime variant unavailable), max effort requested (runtime setting unavailable); checkout `194896662dd168529bcdf8c532a71b660d6ef20d`; Sussman–Alpoge source `31a47c543775`. Research text, not an audit; grants no status.

## 1. Check of Claude's Lemma S

Checked line by line by Codex, first failing step none, for the lemma itself. Source: `t0-skeleton.md`, Section 2, at this checkout. The adaptation definition agrees with YM3_I, lines 73363–73374.

1. Adaptation to a normal means an orthogonal direct sum. Thus orthogonal projection maps the period lattice onto its normal summand.
2. Adaptation to \(n=e_1-e_4\) makes its reflection preserve that lattice. This reflection swaps coordinates 1 and 4.
3. Full rank and adaptation give \(\Gamma\cap\mathbb Re_4=p\mathbb Ze_4\) and \(\Gamma\cap\mathbb Rn=q\mathbb Zn\), with positive integers \(p,q\).
4. Reflecting \(pe_4\) gives \(pe_1\in\Gamma\). Its projection onto \(\mathbb Rn\) is \(pn/2\). Hence \(p=2qk\), \(k\in\mathbb N\).
5. Projecting \(qn\) onto \(\mathbb Re_4\) gives \(-qe_4\in\Gamma\). Hence \(q=p\ell\), \(\ell\in\mathbb N\).
6. Substitution gives \(1=2k\ell\), impossible. No such adapted lattice exists.

The following consequence needs qualification. The lemma excludes this simultaneous **adaptation**, not every other finite-volume argument or joint limit. The selected proof below takes volume first. Necessity of that order for every possible construction does not follow from Lemma S.

Credit throughout: Ethan Sussman and Levent Alpoge, with Claude and Codex as authors of their text. Write Y3 for their `YM3/YM3_I.tex`, and SA for their `YM4_sketch_500.tex`, at the source commit above. The arguments below rebuild the cited lattice steps by hand. They use no RG input.

## 2. Fixed-spacing setting

Fix \(\beta\ge0\) and rescale the spacing to one. Let \(G=\mathrm{SU}(2)\) with normalized Haar measure, and \(\Omega=G^E\), with one variable per positive lattice bond. Reverse bonds carry inverses. Put \(a_p=1-\frac12\operatorname{tr}U_p\in[0,2]\). The kernel \(\gamma_B\) on finite \(B\subset E\) integrates its Haar variables with weight
\[
\exp\!\left[-\beta\sum_{p:p\cap B\ne\varnothing}a_p\right].
\tag{1}
\]
A DLR state satisfies \(\nu\gamma_B=\nu\). Periodic means invariant under a finite-index subgroup, hence under \(N\mathbb Z^4\) for some \(N\). Local functions below are continuous unless stated otherwise.

On a torus use one Haar variable per bond class. Write
\[
Z_\Gamma(\Phi)=\int e^{-\beta\sum_{p\bmod\Gamma}a_p+\Phi}\,dU_\Gamma,
\qquad d\mu_\Gamma^\Phi=Z_\Gamma(\Phi)^{-1}
e^{-\beta\sum_{p\bmod\Gamma}a_p+\Phi}\,dU_\Gamma.
\]
The notation \(\mu_\Gamma\) means \(\Phi=0\).

Here are the needed compactness facts (Y3 73102–73345). The countable product \(\Omega\) is compact metrizable. Freezing all but finitely many coordinates approximates any continuous function uniformly. Thus local integrals determine a law. The denominator of (1) is at least \(e^{-12\beta|B|}\): each bond meets six plaquettes. Kernels preserve local continuity. DLR equations and invariance under a **fixed** group are closed affine conditions on the compact space of laws.

For tori with shortest period tending to infinity, a fixed finite test and its interaction neighbourhood eventually embed without identifications. Integrating its bond variables then gives exactly (1). Passing these continuous equations to a weak limit proves DLR. This also applies to a fixed locally finite family of bounded local perturbations. Unperturbed cubic tori therefore give a translation-invariant DLR state. If the perturbation strength tends to zero, its normalized local density ratios lie in \([e^{-2\delta},e^{2\delta}]\), where \(\delta\) is the supremum of the perturbation meeting \(B\). Hence the kernels converge uniformly to (1).

Every DLR state is gauge invariant. A gauge change at one vertex preserves Haar measure on its eight incident bonds and all plaquette traces. Apply its DLR equation, then compose finitely many such changes. An arbitrary gauge change acts on a local test through finitely many vertices. Averaging over those vertices gives a gauge-invariant local test with the same expectation. Consequently two DLR states equal on gauge-invariant local tests are equal.

## 3. Crossing kernels and split tori

This ports Y3 IV-16-26, using SA 2773–2883. Allowed normals are \(e_\mu\) and \(e_\mu\pm e_\lambda\). Mirror heights are \(c\in\frac12\mathbb Z\) for the former and \(c\in\mathbb Z\) for the latter. Write
\[
\theta_c x=x-\frac{2(n\cdot x-c)n}{|n|^2}.
\]
Use an adapted torus \(\Gamma=T\oplus\mathbb Z(Ln/|n|^2)\), \(T\subset n^\perp\), with large shortest period. Its two cuts have heights \(c,c+L/2\). A test in a closed half uses bonds with both endpoints there.

For unit-quaternion coordinates, multiplication gives \(\frac12\operatorname{tr}(gh^{-1})=s(g)\cdot s(h)\). Thus the Wilson kernel is
\[
k(g,h)=e^{-\beta}e^{\beta s(g)\cdot s(h)}
=e^{-\beta}\sum_{r\ge0}\frac{\beta^r}{r!}
 \sum_{i_1,\ldots,i_r=1}^4
 \prod_j s_{i_j}(g)\prod_j s_{i_j}(h).
\tag{2}
\]
This is a positive Gram expansion. The absolute coefficient sum is \(e^{3\beta}\); each feature is bounded by one. Finite products and Haar averages therefore permit termwise integration.

At a coordinate site cut, no plaquette meets both strict sides. Condition on the bonds in the cut. The two remaining actions are reflected copies, giving an integral of absolute squares.

At a diagonal cut, reduce by a signed permutation to \(n=e_1+e_2\). The only crossing plaquettes have heights \(c-1,c,c,c+1\), in the \((1,2)\) plane. Orient their two paths between the cut vertices identically. Their weight is \(k(P_+,P_-)\), and reflection exchanges the paths. Apply (2). All other plaquettes lie in closed halves. The cut bonds, in directions 3 and 4, are fixed and remain conditioning variables.

At a coordinate bond cut, integrate the normal crossing bonds. For the tangential bonds in the adjacent layers the resulting kernel is
\[
\int k_S(u,w\cdot u')\,dw,\qquad
k_S=\prod_{b\in S}k(u_b,u'_b).
\]
Simultaneous vertex gauge action preserves \(k_S\). Its single Haar average equals the double average, by changing variables in the gauge group. Thus each product feature in (2) is Haar-averaged on both arguments. The resulting kernel is again positive Gram. The two cuts use disjoint crossing bonds.

In all cases the unnormalized reflection form is
\[
\int W_0(Y)\sum_\alpha c_\alpha
 \left|\int F(Y,U_+)W_+(Y,U_+)\Phi_\alpha(U_+)\,dU_+\right|^2dY\ge0.
\tag{3}
\]
Here \(c_\alpha\ge0\); the uniform bounds above justify the sums. This proves RP for every bounded half test, including nongauge-invariant tests. Reflection also preserves the Haar variables and action. A real perturbation \(E+\theta_cE\), supported in the two halves, preserves both properties: replace \(F\) in (3) by \(Fe^E\).

The fourth dimension adds tangential bonds and plaquettes only. It adds a second fixed tangential direction at a diagonal cut. The four quaternion coordinates in (2) belong to \(G\), and do not change with the lattice dimension.

## 4. Lower tangent and folding

Let \(\Gamma\subset Q\) be period groups, \(D\) a site transversal of \(\Gamma\), and \(\nu\) a \(Q\)-periodic DLR state. Set
\[
\mathbb A=\sum_{v\in Q/\Gamma}\tau_vA,\quad m=[Q:\Gamma],\quad
\partial_rD=\{x\in D:\exists w\in\mathbb Z^4,\ |w|_\infty\le r,\ x+w\notin D\}.
\]
If the support of real \(A\) lies in \(x_0+[0,r]^4\), with \(x_0\in\mathbb Z^4\) and integer \(r\ge1\), then
\[
\log\frac{Z_\Gamma(t\mathbb A)}{Z_\Gamma(0)}
\ge tm\nu(A)-\{48\beta+2|t|\|A\|_\infty(2r-1)^4\}|\partial_1D|.
\tag{4}
\]
This is Y3 IV-14-20 in dimension four.

To prove it, integrate the bonds anchored in \(D\). Interior plaquettes agree with the torus action. For each coordinate pair, three plaquettes meet the positive bonds from a site. Hence at most \(18|\partial_1D|\) noninterior plaquettes meet these bonds. At most \(6|\partial_1D|\) torus plaquettes lack an interior representative. The action difference lies in an interval of length at most \(2\beta(18+6)|\partial_1D|\). Comparing normalized densities costs \(48\beta|\partial_1D|\).

Keep the \(m_{\rm in}\) source copies wholly supported on these bond variables. Conditional Jensen gives the expectation of their sum as a lower bound for the conditional log partition ratio. Integrate this bound against \(\nu\). DLR and periodicity give \(tm_{\rm in}\nu(A)\). Adding omitted terms costs at most \(|t|\|A\|_\infty(m-m_{\rm in})\); replacing \(m_{\rm in}\) by \(m\) costs the same. Assign each omitted class its unique anchor \(x_0+v\) in \(D\). This anchor lies in \(\partial_rD\). A path to its first exit, using at most \(r\) steps of sup norm one, gives
\[
m-m_{\rm in}\le|\partial_rD|\le(2r-1)^4|\partial_1D|.
\]
This proves (4), without differentiability of pressure or any torus representation of \(\nu\).

For folding, let the height period be \(2Mh\). Write \(v_h=hn/|n|^2\), and take \(h\) even with \(v_h\) integral. The first slab is \([c,c+h]\) in height. The maps
\[
w_{2k+1}=\tau_{2kv_h},\qquad w_{2k}=\theta_{c+kh}
\]
place its profile in successive slabs. For a positive profile \(f\), define
\[
b(f)=\left[\mu_\Gamma\!\left(\prod_{j=1}^{2M}w_jf\right)\right]^{1/(2M)}.
\]
For finitely many profiles with positive infima, maximize the ratio of a filled-board integral to the product of its \(b\)'s. Reflection Cauchy–Schwarz from (3) bounds the square of this ratio by the ratios of its two reflected fillings. The denominators multiply correctly: every original factor occurs twice. Therefore both reflections of a maximizer maximize.

Choose a maximizer with a longest constant cyclic run. If its length is at most \(M\), reflect the half ending with that run; the run doubles. If its length exceeds \(M\), reflecting a half inside it gives a constant filling. Thus a maximizer is constant, with ratio one. This proves the one-direction chessboard inequality for every \(M\).

Let \(A_T\) sum the tangential translates in one slab. Define
\[
\mathbb A^{u}=\sum_{j=1}^{2M}\tau_{(j-1)v_h}A_T,\qquad
\mathbb A^{f}=\sum_{j=1}^{2M}w_jA_T.
\]
The unfolded profiles alternate between \(f=e^{tA_T}\) and \(\vartheta f\), where \(\vartheta=\theta_{c+h/2}\). Translation by \(v_h\) carries the full fold of one into the other. Their \(b\)'s are equal. The chessboard bound gives
\[
Z_\Gamma(t\mathbb A^u)\le Z_\Gamma(t\mathbb A^f).
\tag{5}
\]
The folded source is \(E+\theta E\) at every slab wall. Its measure is therefore RP and invariant there. Tangential translations also preserve it. All folded terms have the same expectation. This ports Y3 IV-16-31; the proof itself has no dimension-dependent step.

## 5. Comparison at a diagonal mirror: IV-29-40

Fix a periodic state \(\nu\) and a real local \(A\) in the closed positive half. Choose a nonempty finite bond support \(B_A\) there, also when \(A\) is constant. Choose \(N\) with period \(N\mathbb Z^4\). Choose \(h\in2N\mathbb N\), large enough to contain \(B_A\) in the first slab. For \(n=e_1+e_2\), set
\[
T=N\{\mathbb Z(e_1-e_2)\oplus\mathbb Ze_3\oplus\mathbb Ze_4\},
\quad Q=T\oplus\mathbb Zv_h,\quad
\Gamma_i=iT\oplus\mathbb Z(2iv_h),\qquad i\ge3.
\tag{6}
\]
Here \(Q\subset N\mathbb Z^4\), \(\iota=[\mathbb Z^4:Q]=N^3h\), and \([Q:\Gamma_i]=2i^4\). Since \(\Gamma_i\subset i\mathbb Z^4\), its shortest nonzero period has sup norm at least \(i\). A site transversal is
\[
0\le x_1-x_2<2iN,\quad 0\le x_1+x_2<2ih,\quad
0\le x_3,x_4<iN.
\tag{7}
\]
The first two coordinates have equal parity. Reduction by their even periods preserves parity and yields exactly one representative. Thus \(|D_i|=2i^4N^3h\). A displacement of sup norm one changes either diagonal coordinate by at most two. Counting four boundary layers for each, and two for each remaining coordinate, gives
\[
\frac{|\partial_1D_i|}{|D_i|}
\le \frac6{iN}+\frac2{ih}.
\tag{8}
\]
Each diagonal layer has equal size by parity. In the coordinate case take \(T=N\mathbb Z^3\) in the tangent directions and normal interval \([0,2ih)\). The same index and the bound (8) hold. Signed permutations cover every other diagonal.

Use \(A_T=\sum_{v\in T/iT}\tau_vA\), \(m=2i^4\). Apply (4), then (5), then Jensen in the **folded** measure \(\mu_{i,t}\), with \(t>0\):
\[
\begin{aligned}
tm\nu(A)-\{48\beta+2t\|A\|_\infty(2r-1)^4\}|\partial_1D_i|
&\le \log\frac{Z_{\Gamma_i}(t\mathbb A^u)}{Z_{\Gamma_i}(0)}\\
&\le \log\frac{Z_{\Gamma_i}(t\mathbb A^f)}{Z_{\Gamma_i}(0)}
\le tm\mu_{i,t}(A).
\end{aligned}
\tag{9}
\]
The last inequality is \(-\log\mu_{i,t}(e^{-t\mathbb A^f})\le t\mu_{i,t}(\mathbb A^f)\). Wall and tangential symmetries give \(\mu_{i,t}(\mathbb A^f)=m\mu_{i,t}(A)\). The error after division by \(tm\) is
\[
\iota\{48\beta/t+2\|A\|_\infty(2r-1)^4\}
\left(\frac6{iN}+\frac2{ih}\right)\longrightarrow0.
\]

Keep \(t\) fixed first. The infinite folded family has indices \((j,v)\in\mathbb Z\times T\), functions \(t\,w_j\tau_vA\), and their transported supports. A bond occurs in at most \(2|B_A|\) supports. Translation by \(g_\perp+2ikv_h\in\Gamma_i\) acts as \((j,v)\mapsto(j+2ik,v+g_\perp)\). Its quotient has \(2i\cdot i^3\) terms, precisely the finite source in (9).

Section 2 therefore gives a perturbed DLR limit \(\nu_t\). It retains period \(T\oplus\mathbb Z(2v_h)\), mirror invariance, and RP on continuous local half tests. Each such test eventually lies in the torus half. Equation (9) gives \(\nu(A)\le\nu_t(A)\). Now take a subsequential limit as \(t\downarrow0\). Uniform local kernel convergence gives an unperturbed periodic DLR state \(\nu_0\) with
\[
\nu(A)\le\nu_0(A),\qquad \nu_0\text{ invariant and RP at the chosen mirror}.
\tag{10}
\]
The bounded Borel extension is proved in Section 8. No common period for all DLR states has been assumed here.

The exact dimensional changes from Y3 78688–78808 are: tangent rank \(2\to3\), term count \(2i^3\to2i^4\), and boundary/volume bound \(4/(iN)+2/(ih)\to6/(iN)+2/(ih)\). In (4), \(24\to48\) and exponent \(3\to4\). All limits retain the same order.

## 6. Adjacent-layer exchange

We rebuild the input to IV-54-16: Y3 IV-29-15, IV-29-28 and IV-29-36 (78336–78684). Assume \(\beta>0\). Time is direction 4; spatial layers now have dimension three.

**Strict kernel and square root.** Let \(K\) have kernel (2) on \(L^2(G)\). The following polynomial argument replaces the character calculation in Y3. Let \(\mathcal P_r\) be polynomials in the four quaternion coordinates of degree at most \(r\), restricted to \(S^3\), and \(\mathcal P_{-1}=0\). Convolution preserves \(\mathcal P_r\): in
\[
(Kf)(g)=\int k(z,1)f(z^{-1}g)\,dz
\]
the product \(z^{-1}g\) is linear in the coordinates of \(g\). Symmetry of \(K\) therefore preserves \(\mathcal W_r=\mathcal P_r\ominus\mathcal P_{r-1}\). The polynomial algebra is uniformly dense by Stone–Weierstrass: it contains constants, is self-adjoint, and separates points.

Expansion (2) gives
\(\langle f,Kf\rangle=\sum_I a_I|\langle s_I,f\rangle|^2\), with every \(a_I>0\). If this vanishes, every polynomial moment vanishes, so \(f=0\). Thus the finite real symmetric restriction to each \(\mathcal W_r\) has strictly positive eigenvalues. In particular, \(K\) maps every \(\mathcal P_r\) onto itself.

Its square root has a continuous kernel. Normalized Haar is normalized sphere measure: quaternion multiplication is orthogonal and preserves that measure. The positive rank-one series (2) has total trace
\[
e^{-\beta}\sum_{m\ge0}\frac{\beta^m}{m!}
 \int_{S^3}\left(\sum_{j=1}^4s_j^2\right)^m ds=1.
\]
On \(\mathcal W_r\), all features of degree less than \(r\) vanish after projection. Hence its trace is at most
\[
T_r=e^{-\beta}\sum_{m\ge r}\frac{\beta^m}{m!}
\le\frac{\beta^r}{r!}.
\]
The space \(\mathcal W_r\) is invariant under \(O(4)\) on the internal sphere. For any orthonormal basis \(e_{rj}\), transitivity makes \(\sum_j|e_{rj}(s)|^2=\dim\mathcal W_r\). Choose real eigenvectors with eigenvalues \(\lambda_{rj}\). The kernel block of \(K^{1/2}\) is bounded in absolute value by
\[
(\dim\mathcal W_r)\sqrt{T_r}
\le {r+4\choose4}\frac{\beta^{r/2}}{\sqrt{r!}}.
\]
This series converges: its successive-term ratio tends to zero. Thus the eigenfunction series for the root kernel \(q\) converges uniformly. It is real symmetric, and convolution gives \(k\). Tensor products give \(Q_S=K_S^{1/2}\), with continuous kernel \(q_S\) and
\[
\langle q_u,q_{u'}\rangle=k_S(u,u'),\qquad \|q_u\|_2=1.
\tag{11}
\]
Both operators are invertible on every \(\bigotimes_{b\in S}\mathcal P_{r_b}\). Therefore a finite measure on \(G^S\times Y\), with \(Y\) compact metrizable, annihilating \((K_S\varphi)(u)\chi(y)\) is zero, when \(\varphi\) ranges over polynomials and \(\chi\) over a dense subalgebra of \(C(Y)\). Indeed, their products are dense in the continuous functions on that compact product.

**Transfer insertion.** Write \(u_t\) for spatial bonds and \(w_t(x)\) for bonds from layer \(t\) to \(t+1\). A vertical plaquette has weight \(k(u_t(b),(w_t\cdot u_{t+1})(b))\). For bounded \(X\) on \(L^2(G^S)\), put
\[
A_X(u,u')=\frac{\langle q_u,Xq_{u'}\rangle}{k_S(u,u')}.
\tag{12}
\]
It is continuous, \(A_1=1\), and \(\|A_X\|_\infty\le e^{2\beta|S|}\|X\|\). It preserves reality and tensor products on disjoint bond sets.

On a spatial torus let \(P\) be vertex gauge averaging, \(E=e^{-\beta V}\) multiplication by the spatial Wilson weight, and \(Q=K^{1/2}\) for all spatial bonds. Simultaneous gauge covariance makes \(Q\) commute with \(P\); gauge invariance of \(V\) makes \(E\) commute with \(P\). Thus
\[
M=QPEQ=(E^{1/2}PQ)^*(E^{1/2}PQ)\ge0
\]
is trace class. Replacing each selected vertical kernel by \(QX_tQ\), integrating \(w_t\), and then the cyclic spatial variables gives
\[
Z(0)=\operatorname{Tr}M^s,\qquad
\mu\!\left(\prod_t A_{X_t}^{(t)}\right)
=\frac{\operatorname{Tr}(X_1M\cdots X_sM)}{\operatorname{Tr}M^s},
\qquad
\left|\mu\!\left(\prod_t A_{X_t}^{(t)}\right)\right|\le\prod_t\|X_t\|.
\tag{13}
\]
Here disjoint insertions in a layer are tensored, with the identity elsewhere. More explicitly the integrated kernels are \(EQX_tQP\); cycling the first \(EQ\) to the end gives the displayed trace. Each cycle has two Hilbert–Schmidt factors, so these operations are valid.

Here is a hand proof of the trace bound used in (13), following Y3 IV-3-35. A zero factor is immediate. Otherwise, for \(2s\) Hilbert–Schmidt factors, normalize \(\operatorname{Tr}|B_j|^{2s}=1\). Maximize the trace modulus among length-\(2s\) words in these factors and their adjoints. Alternating words have trace one, so the maximum is positive. Splitting a word into equal halves gives
\[
|\operatorname{Tr}(XY)|^2\le\operatorname{Tr}(XX^*)\operatorname{Tr}(Y^*Y).
\]
Both reflected words of a maximizer maximize. Choose one with a longest cyclic string alternating \(B,B^*\). If its length is at most \(s\), end that string at the half boundary and reflect. It doubles. If longer, reflect a half within it. Thus a maximizing word alternates throughout and has trace one. Rescaling proves trace Hölder. Apply it to the \(2s\) factors \(X_tM^{1/2},M^{1/2}\). Their norms are bounded using
\[
M^{1/2}X_t^*X_tM^{1/2}\le\|X_t\|^2M.
\]
For positive \(C\le D\), \(\operatorname{Tr}C^s\le\operatorname{Tr}D^s\): use an eigenbasis of \(C\), then scalar Jensen in an eigenbasis of \(D\). This proves (13).

**Exchange for an arbitrary periodic state.** Let \(D\) be a bounded real skew-adjoint operator. For real \(\varepsilon\), \(X_\varepsilon=e^{\varepsilon D}\) is real unitary. The operator exponential remainder and (12) give
\[
\phi_\varepsilon=\log A_{X_\varepsilon}^{(t)}
=\varepsilon A_D^{(t)}+O(\varepsilon^2)
\quad\text{uniformly},
\tag{14}
\]
with \(A_{X_\varepsilon}^{(t)}\in[1/2,3/2]\) for small \(\varepsilon\).

Choose a period \(N\) of \(\nu\), enlarged so spatial translates of \(S\) by \(N\mathbb Z^3\) are disjoint. On the torus \((iN)\mathbb Z^4\), the array of \(\phi_\varepsilon\) has \(i^4\) copies: \(i^3\) per selected height. Equation (13) bounds its partition ratio by one. Equation (4) then gives \(0\ge i^4\nu(\phi_\varepsilon)-C_\varepsilon i^3\). Send \(i\to\infty\), with \(\varepsilon\) fixed; use both signs in (14). It follows that \(\nu(A_D^{(t)})=0\).

For a real antisymmetric polynomial \(\Phi(u,u')\), divide its finite eigenfunction coefficients by \(\sqrt{\lambda_\alpha\lambda_{\alpha'}}\). The result is the kernel of a finite-rank real skew-adjoint \(D\), with \(\langle q_u,Dq_{u'}\rangle=\Phi(u,u')\). Approximate the continuous antisymmetric function \(k_S(u,u')[H(u,u')-H(u',u)]\) by real antisymmetric polynomials. Since \(k_S\ge e^{-2\beta|S|}\), division preserves uniform convergence. Therefore
\[
\nu H(u_t|_S,(w_t\cdot u_{t+1})|_S)
=\nu H((w_t\cdot u_{t+1})|_S,u_t|_S)
\tag{15}
\]
for every continuous \(H\), also complex by linearity. Enlarging \(S\) determines the joint law of the two entire layers.

The group-kernel argument is dimension independent. The changes in this transfer proof are spatial dimension \(2\to3\), copies per selected height \(i^2\to i^3\), and surface/volume orders \(i^2/i^3\to i^3/i^4\).

## 7. Temporal gauge, two-layer determination, common periods

This ports Y3 IV-54-9, IV-54-13 and IV-54-16 (78814–78969). Fix \(t_0\) and define vertex gauges, in both time directions, by
\[
\widehat w_{t_0}=1,\qquad
\widehat w_{t+1}=\widehat w_tw_t,\qquad
\widetilde u_t=\widehat w_t\cdot u_t.
\]
Each coordinate uses finitely many original bonds. This continuous map sets vertical bonds to one. Every gauge-invariant local \(F\) equals \(F(U[\widetilde u])\), where \(U[\widetilde u]\) has these horizontal layers and unit vertical bonds.

Let \(V_S\) sum the spatial plaquettes meeting finite \(S\). In three spatial dimensions each bond meets four such plaquettes, so \(0\le V_S\le8|S|\). The conditional layer density before normalization is
\[
k_S(\widetilde u_{t-1}|_S,v)\,
e^{-\beta V_S(v\vee\widetilde u_t|_{S^c})}\,
k_S(v,\widetilde u_{t+1}|_S).
\tag{16}
\]
It and its Haar integral lie in \([e^{-12\beta|S|},1]\). Integrating only the original horizontal bonds \(S\) at height \(t\) leaves every \(\widehat w_j\) fixed. The Haar-preserving change \(v=\widehat w_t\cdot U_S\) turns the DLR kernel exactly into (16): one vertical plaquette above and below each bond, plus the spatial plaquettes. Thus the temporal image obeys the layer equations.

The symmetry \(k_S(u,v)=k_S(v,u)\) makes these equations covariant under \((R_m\widetilde u)_t=\widetilde u_{m-t}\). If the image law is \(R_{2t_0+1}\)-invariant, then the original state is invariant under the bond mirror at \(t_0+1/2\). Indeed, reflecting \(U[\widetilde u]\) gives \(U[R_{2t_0+1}\widetilde u]\). The two DLR states agree on gauge-invariant local functions, so Section 2 makes them equal. This proves the port of IV-54-9.

**Two-layer determination.** Suppose two layer laws obey (16) and agree on entire layers \(m,\ldots,n\), \(m<n\). To extend agreement, set
\[
u'=\widetilde u_{n+1}|_S,\quad v=\widetilde u_n|_S,\quad
c=(\widetilde u_n|_{S^c},\widetilde u_{n-1},\ldots,\widetilde u_m),
\]
\[
\Phi(v;c)=k_S(\widetilde u_{n-1}|_S,v)e^{-\beta V_S(v\vee\widetilde u_n|_{S^c})},
\quad N(u',c)=\int k_S(v,u')\Phi(v;c)\,dv.
\]
These are continuous local functions with \(\Phi\ge e^{-10\beta|S|}\), \(N\ge e^{-12\beta|S|}\). If \(\rho_i'\) is the marginal on \((u',c)\), put \(\sigma_i=N^{-1}\rho_i'\). The layer equation says, for the joint marginal \(\rho_i\),
\[
\rho_i(\psi)=\int d\sigma_i(u',c)\int
k_S(v,u')\Phi(v;c)\psi(u',v,c)\,dv.
\tag{17}
\]
It applies to these marginals because the replacement at \((S,n)\) changes neither \(u'\) nor \(c\).

Take \(\psi=\varphi(v)\chi(c)/\Phi(v;c)\), with \(\varphi\) polynomial and \(\chi\) continuous local. This test depends only on the already equal layers; \(n-1\ge m\) is essential. Subtraction in (17) gives
\[
\int (K_S\varphi)(u')\chi(c)\,d(\sigma_1-\sigma_2)=0.
\]
Section 6's measure injectivity applies on the compact countable product of \(c\)-coordinates, so \(\sigma_1=\sigma_2\). Equation (17) then gives equality on these marginals. Enlarge \(S\) to contain any requested finite test in layer \(n+1\); this extends agreement. Reflection covariance gives extension to \(m-1\). Iteration covers every finite block, whose cylinder functions determine the law. This proves IV-54-13 in four dimensions.

For a periodic Wilson state, its temporal layers at \(t_0,t_0+1\) are \(u_{t_0},w_{t_0}\cdot u_{t_0+1}\). Equation (15) exchanges their joint law. The temporal law and its reflected law obey (16) and agree on those two layers. Determination and IV-54-9 therefore give bond reflection invariance of the original state. Apply the same argument to each coordinate permutation of that state; these are still periodic DLR states.

Composing bond reflections at \(1/2\) and \(3/2\) gives translation by two. Thus every periodic state is \(2\mathbb Z^4\)-invariant. Conversely, this fixed group has finite index. Section 2 now proves that the periodic DLR states form a nonempty compact convex class \(\mathcal G^P\), with \(P=2\mathbb Z^4\). This is IV-54-16.

Here the numerical changes from Y3 are
\[
V_S\le4|S|\ \longrightarrow\ 8|S|,\qquad
\Phi\ge e^{-6\beta|S|}\ \longrightarrow\ e^{-10\beta|S|},\qquad
N,\text{ layer weight}\ge e^{-8\beta|S|}
\ \longrightarrow\ e^{-12\beta|S|}.
\]
The determination argument otherwise stays unchanged. At \(\beta=0\), DLR directly fixes every finite marginal to product Haar, so all stated symmetries hold without injectivity.

## 8. Separation and all-mirror invariance: IV-54-17

Fix an admissible mirror. Let \(\mathcal R\subset\mathcal G^P\) consist of states RP there on continuous local positive-half tests. It is nonempty by (10) with \(A=0\). Each condition \(\rho(\overline{\theta F}F)\in[0,\infty)\) is closed and affine. Hence \(\mathcal R\) is compact convex.

Suppose \(\nu\notin\mathcal R\). Some finite vector of real continuous test integrals separates \(\nu\) from \(\mathcal R\). Otherwise compactness and the finite intersection property would give a member agreeing on all tests. In that finite-dimensional convex compact image, let \(p\) be nearest to the vector \(x\) of \(\nu\). Minimizing squared distance along segments gives \((x-p)\cdot(y-p)\le0\). Thus the real linear combination \(f\) of those tests has a strict gap. Uniformly approximate \(f\) by a real local \(A_0\), retaining the gap.

Translate its finite support into the positive half by \(v=2kn\), \(k\) large. Every state in \(\mathcal G^P\) has this period. The strict gap persists for \(A=\tau_vA_0\). But (10) supplies \(\nu_0\in\mathcal R\) with \(\nu(A)\le\nu_0(A)\), a contradiction. Therefore every periodic state is RP at this mirror. This uses the common period, not a presumed torus approximation of \(\nu\).

Positivity makes \(B(F,G)=\nu(\overline{\theta F}G)\) Hermitian: expand \(B(F+zG,F+zG)\) for \(z=1,-1,i,-i\). Taking one entry equal to one gives \(\nu(F)=\nu(\theta F)\) on the positive half. For arbitrary local \(F_0\), translate by the same normal period \(v\). The identity \(\theta\tau_v=\tau_{-v}\theta\) and invariance under both translations give \(\nu(F_0)=\nu(\theta F_0)\). Hence \(\theta_*\nu=\nu\) as laws.

Now let \(F\) be any bounded Borel function of all bonds in the closed positive half. Finite-coordinate conditional expectations converge to \(F\) in \(L^2(\nu)\), since cylinders generate that sigma-algebra. Continuous functions are dense for each finite compact marginal. Thus choose continuous local half tests \(F_j\to F\) in \(L^2(\nu)\). Reflection invariance gives the same convergence for their reflections. Cauchy–Schwarz yields
\[
|B(F_j,F_j)-B(F,F)|
\le \|F_j-F\|_2(\|F_j\|_2+\|F\|_2)\longrightarrow0.
\]
RP passes to \(F\). Reflecting the tests gives RP on the negative half. This also completes the bounded Borel assertion in (10).

There are four coordinate and twelve diagonal normal families. Adjacent site and bond mirrors generate unit translations. Coordinate site mirrors give sign changes; \(x_\mu=x_\lambda\) gives coordinate exchanges. Therefore every periodic state is invariant under \(\mathbb Z^4\rtimes W_4\). The periodic class equals the translation-invariant DLR class and contains every cubic torus-limit state. Separation and the Borel extension have no dimension-dependent step; the symmetry group changes from \(W_3\) to \(W_4\).

## Result

Lemma S is checked line by line by Codex, first failing step none. Its subsequent volume-first conclusion is stronger than the lemma proves.

For every fixed spacing \(a>0\) and \(\beta\ge0\), the arguments above prove the four-dimensional versions of Y3 IV-29-40, IV-54-16 and IV-54-17. Every periodic SU(2) Wilson DLR state is invariant under \(a\mathbb Z^4\rtimes W_4\), and is RP on the bounded Borel algebras of both closed halves at every admissible coordinate or diagonal mirror. The proofs restore \(a\) by multiplying every spatial coordinate and period by \(a\).

This supplies research proofs for skeleton nodes S1c and S1g, including their lattice inputs. Proved here by Codex, not yet checked by the other model. This reads no RG rank and proves no continuum statement. It grants no retained status.
