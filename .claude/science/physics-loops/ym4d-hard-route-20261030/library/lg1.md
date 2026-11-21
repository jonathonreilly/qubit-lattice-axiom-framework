# LG1. Lattice Gibbs states and all mirrors

Provenance: Codex, 2026-11-05; Phase A, pass 2 (distil), checkout 1724d326aee3af902e55c00bd248cf6ef6099e03. Research text, not an audit; grants no status. Not yet refereed as a whole part.

Credit: Ethan Sussman and Levent Alpoge, with Claude and Codex as authors of their text. Their pinned sources are `YM4_sketch_500.tex` (SA) and `YM3/YM3_I.tex` (Y3), commit `31a47c543775`. The finite Wilson reflection argument is due to Osterwalder and Seiler; the chessboard method is due to Fröhlich, Israel, Lieb and Simon. The polynomial proof of the square-root kernel below is the replacement in `am1-port.md` §6.

This distils LG1 in `ym4-assembly.md` §§4–5 and its row in `assembly-status.md`. The source notes are `am1-port.md` (whole), `t0-skeleton.md` (whole, using Lemma S), `d2-d4.md` (whole, using §2), and `parts/upper-chain.md`, Text Lemma 1.1. The two gate reports, read whole, are `gates/o4-check-1.md` and `gates/bridge-check.md`. They record earlier line-by-line checks by Claude; they are not a referee report on this assembled part.

## Definitions and order of choice

Work first at spacing one in dimension four. Let \(E\) contain the bonds \((x,x+e_\mu)\), and put \(\Omega=G^E\), \(G=SU(2)\), with product topology. A reversed bond carries \(U_{\bar b}=U_b^{-1}\). A plaquette is one geometric elementary square, counted once; its ordered boundary product is \(U_p\). Put
\[
 a_p=1-\tfrac12\operatorname{Re}\operatorname{tr}U_p,
 \qquad O_a(f)=\sum_p f(x(p))a_p,
\]
where \(x(p)\) is its barycentre. On the infinite lattice \(f\) has compact support. A function is **local** if it depends on finitely many bonds. Unless explicitly called Borel, local functions below are continuous.

An isometry \(r\) acts by \((r^*U)_b=U_{r b}\), using inverses for reversed orientations, and \(rF=F\circ r^*\). Its action on spatial tests is \(rf=f\circ r^{-1}\); \(\tau_v\) means this action for translation by \(v\). A vertex gauge acts by \((h\cdot U)_{xy}=h_xU_{xy}h_y^{-1}\).

For finite \(B\subset E\), the Wilson specification is
\[
 \gamma_BF(U)=
 \frac{\int F(V_B,U_{B^c})e^{-\beta\sum_{p:p\cap B\ne\varnothing}a_p(V_B,U_{B^c})}\,dV_B}
 {\int e^{-\beta\sum_{p:p\cap B\ne\varnothing}a_p(V_B,U_{B^c})}\,dV_B}.       \tag{1}
\]
Haar measures are probability measures. A **DLR state** is a law \(\nu\) with \(\nu\gamma_B=\nu\) for every finite \(B\). A **periodic state** is invariant under a finite-index translation subgroup, equivalently under \(N\mathbb Z^4\) for some positive integer \(N\). Write \(\mathcal G_{a,\beta}\) for the translation-invariant DLR class at spacing \(a\), and \(\mathcal G^P\) for the DLR class with fixed period group \(P=2\mathbb Z^4\) at unit spacing. Periodicity of a law does not mean that its configurations are periodic. A family of local perturbations is locally finite when each bond belongs to the supports of only finitely many indexed terms.

A period lattice \(\Gamma\subset\mathbb Z^4\) has finite index. On its torus, use one Haar variable per positive bond class and one plaquette term per class:
\[
 Z_\Gamma(\Phi)=\int e^{-\beta\sum_{p\bmod\Gamma}a_p+\Phi}\,dU_\Gamma,
 \qquad \mu_\Gamma^\Phi=Z_\Gamma(\Phi)^{-1}
 e^{-\beta\sum_{p\bmod\Gamma}a_p+\Phi}\,dU_\Gamma.              \tag{2}
\]
Here \(\Phi\) is real and bounded; omit it when zero. Quotient bonds retain their lattice labels, including the distinct parallel edges on a two-site periodic axis. Adapted auxiliary tori below have shortest nonzero period at least three and then tending to infinity.

Allowed normals and mirrors are
\[
 \mathcal N=\{e_\mu\}\cup\{e_\mu\pm e_\lambda:\mu<\lambda\},\quad
 q=|n|^2,\quad \theta_cx=x-2(n\cdot x-c)n/q.                 \tag{3}
\]
For \(q=1\), \(c\in\frac12\mathbb Z\); integer \(c\) gives a site mirror, noninteger \(c\) a bond mirror. For \(q=2\), \(c\in\mathbb Z\). The algebra \(\mathcal A_c^\pm\) consists of bounded Borel functions of all bonds whose two endpoints satisfy \(n\cdot x\ge c\) for the positive half, and \(n\cdot x\le c\) for the negative half. Put \(\Theta_cF=\overline{\theta_cF}\). **Reflection positivity** means \(\nu(\Theta_cF\,F)\ge0\) on the indicated half algebra.

The lattice \(\Gamma\) is **adapted** to \(n\) when
\[
 \Gamma=(\Gamma\cap n^\perp)\oplus\mathbb Z(Hn/q),\qquad H>0.       \tag{4}
\]
For the split tori used here \(H=2s\), \(s\in\mathbb N\), both cuts \(c,c+s\) are admissible, and the pure-normal generator is integral. Their closed half is the slab between those cuts. A **board** has cells with faces on coordinate bond mirrors. A cell function depends only on bonds wholly inside its open cell. Its copy in another cell is transported by the unique composition of board-face reflections carrying the original cell there, and conjugated for an odd number of reflections.

**Imports.** There is no scientific or RG import. The foundational mathematical tools are normalized Haar measure on a compact group, compactness of countable products and their probability laws, Riesz measure determination, Stone–Weierstrass, finite-dimensional spectral decomposition and the positive square root of a bounded positive operator, Fubini/Tonelli, conditional expectation with its \(L^2\) convergence, and Cauchy–Schwarz and Jensen. Their hypotheses are checked at their uses. In particular no all-state symmetry, torus representation of an arbitrary DLR state, or pressure differentiability is an import.

**Constants.** Fix \(d=4,G=SU(2)\). The odd block factor \(L\ge3\), when used, is IN1's row-2 choice. LG1 adds no floor to it. The remaining IN1 constants keep their stated order and do not enter this part. At the final physical-data stage choose \(a>0,\beta>0\), with no coupling ceiling required here. The notation \(\mu_{K,\ell,\beta}\) means (2) on the cubic torus with \(a=L^{-K}\) and \(\ell/a\) even. Boards \(l=L^j\ge a\), tori \(\ell=2L^m\), and an optional \(M=L^{m_0}\) use IN1's already chosen \(L,M\).

In each comparison fix the state, observable and mirror first. Choose its finite support, an integer enclosing-cube size \(r\ge1\), then a period \(N\), and then an even multiple \(h\in2N\mathbb N\) enclosing that support in the first slab. Keep \(t>0\) fixed while the volume index \(i\to\infty\), and only afterwards take \(t\downarrow0\). In the exchange argument fix the finite bond set and skew operator, choose a sufficiently sparse period, then fix nonzero \(\varepsilon\) small enough; take volume to infinity before \(\varepsilon\to0\). The constants \(48,12,10,8\) below are finite incidence bounds, independent of these choices. Approximation limits come after the relevant invariance has been established.

## Hand proofs

**Lemma 1 (finite cutoff and observable support).** Formula (2) at \(\Phi=0\) defines a probability measure. It is gauge invariant and invariant under all isometries of its quotient. For every lattice isometry,
\[
 O_a(f)\circ r^*=O_a(rf).
\]
If \(f\) vanishes outside an open side of a coordinate bond mirror, \(O_a(f)\) uses only bonds in that side.

*Origin:* `am1-port.md` §2; `upper-chain.md` Text §0 and Lemma 1.1; SA 238–294, 6913. The support and covariance statements are made explicit here.

*Proof.* Eigenvalues of \(U_p\in SU(2)\) are \(e^{it},e^{-it}\), so \(0\le a_p\le2\). Thus, with \(N_P\) plaquettes,
\[
 e^{-2\beta N_P}\le Z_\Gamma(0)\le1.
\]
Haar invariance and cancellation of vertex gauges along a loop prove gauge invariance. Relabelling bonds, and inverting reversed bonds, preserves Haar measure and permutes plaquette actions. It proves isometry invariance. Isometries also carry barycentres exactly to barycentres; reindexing the finite observable sum proves covariance.

For the support assertion rescale \(a=1\) and let the mirror be \(x_\mu=k+1/2\). A plaquette with a \(\mu\)-edge has barycentre height in \(\mathbb Z+1/2\). If that height is strictly above the mirror, its lowest vertex is at least \(k+1\). A plaquette without a \(\mu\)-edge has all vertices at its integer barycentre height, again at least \(k+1\). Reflection proves the other side. The open-side condition matters: a plaquette centred on the mirror can cross it. \(\square\)

**Lemma 2 (DLR compactness, limits and gauge invariance).** The kernels (1) preserve continuous local functions. The DLR class, and its subclass invariant under any fixed translation subgroup, are compact convex sets. Weak limits of torus laws with shortest period tending to infinity are DLR states. Cubic torus limits give nonempty \(\mathcal G_{a,\beta}\). Every DLR state is gauge invariant, and equality on gauge-invariant local functions determines it.

These limit statements also hold for a fixed periodic locally finite family of bounded continuous local perturbations, with uniform finite range, and when its scalar strength tends to zero.

*Origin:* `am1-port.md` §2; `o4-check-1.md` §1; SA 418–469, 4486–4495; Y3 73102–73345.

*Proof.* Enumerate the bonds and metrize \(\Omega\) with summable coordinate weights. Compactness of \(G\) gives compact metrizability. Freezing the coordinates after the first \(n\) gives uniform approximation of continuous functions by local ones. Their integrals determine laws. Probability laws on this compact metric space form a compact metrizable space: diagonal selection on a countable dense subset of \(C(\Omega)\) gives a positive normalized limiting functional, represented by Riesz.

Each bond meets six plaquettes. The denominator of (1) is at least \(e^{-12\beta|B|}\). The numerator and denominator are continuous in finitely many external coordinates, by integration on a finite compact product. The DLR equations and fixed-group invariance equations are closed affine conditions, proving compact convexity. Equality on continuous local functions extends to equality of the two laws \(\nu\gamma_B,\nu\), hence to Borel tests. Properness, \(\gamma_B(HF)=H\gamma_BF\) for exterior \(H\), gives the conditional interpretation.

For a fixed finite test and resampling set, include their interaction neighbourhood in one finite region. It embeds injectively in every sufficiently large torus. Integration over the resampling variables gives exactly its infinite-lattice conditional identity on this test. Continuity passes the identity to every weak limit. The same argument applies to the periodic perturbation families: each finite set meets finitely many terms, and their finite quotient is precisely the torus perturbation. Cubic unperturbed tori are translation invariant, so their limits belong to \(\mathcal G_{a,\beta}\).

If the perturbation meeting \(B\) changes by at most \(\delta\), the normalized kernel density ratio is in \([e^{-2\delta},e^{2\delta}]\). Therefore the kernels converge uniformly on bounded tests as the strength tends to zero. This proves the last assertion.

A gauge transformation at one vertex acts on its eight incident bonds, preserves their Haar measure and every action term. Apply the DLR equation there. Composing such transformations proves finite-support gauge invariance. Any fixed local test reads only finitely many vertex gauges, which proves invariance under arbitrary gauge transformations. Averaging a local test over the gauges at its endpoints gives a gauge-invariant local test with the same integral in every DLR state. Equality on these averages determines the law. \(\square\)

**Lemma 3 (positive crossing kernels and finite-torus mirrors).** Wilson laws on split tori are invariant and reflection positive on both full closed-half Borel algebras at their cuts. This includes site and bond cuts on cubic tori with an even number of sites per axis. Multiplication by \(e^{E+\theta_cE}\), for bounded real half-space \(E\), preserves these properties.

*Origin:* `am1-port.md` §3 and `upper-chain.md` Lemma 1.1; `o4-check-1.md` §1. The latter lemma alone covers only site cuts, as `bridge-check.md` §4 corrects. SA 2773–2883; Y3 73375–73500.

*Proof.* Write \(g\) as a unit quaternion \(s(g)\in S^3\). Quaternion multiplication gives
\[
 \tfrac12\operatorname{tr}(gh^{-1})=s(g)\cdot s(h),\qquad
 k(g,h)=e^{-\beta}e^{\beta s(g)\cdot s(h)}
 =e^{-\beta}\sum_{m\ge0}\frac{\beta^m}{m!}
   \sum_{i_1,\ldots,i_m=1}^4 s_{i_1}(g)\cdots s_{i_m}(g)
                               s_{i_1}(h)\cdots s_{i_m}(h).       \tag{5}
\]
All coefficients are nonnegative; their sum is \(e^{3\beta}\), and each feature is bounded by one. Thus this Gram expansion, its finite products and their Haar averages converge absolutely uniformly.

Partition bonds into the two interiors, the bonds on the cuts and the crossing bonds. Reflection exchanges interior variables and fixes cut variables, modulo periods. At a coordinate site cut no plaquette meets both strict sides. Conditional on the cut variables the weight factors into a boundary weight and two reflected half weights.

For a diagonal cut take \(n=e_1+e_2\); signed permutations give the other cases. A bond changes height by at most one. The crossing plaquettes are exactly those in the \((1,2)\) plane with heights \(c-1,c,c,c+1\). Split each into two paths \(P_+,P_-\) between the cut vertices with the same orientation. Its factor is \(k(P_+,P_-)\). Formula (5) separates the paths into positive Gram features. Other plaquettes lie in closed halves. Bonds lying in the mirror point in directions 3 or 4 and remain conditioning variables.

At a coordinate bond cut, the half test does not use the crossing bonds. Their integration gives, for adjacent tangential layer variables \(u,u'\),
\[
 \int k_S(u,w\cdot u')\,dw,\qquad
 k_S(u,u')=\prod_{b\in S}k(u_b,u'_b),\quad
 (w\cdot u')_{xy}=w_xu'_{xy}w_y^{-1}.                       \tag{6}
\]
Simultaneous gauge transformation leaves \(k_S\) invariant. Haar invariance therefore replaces this single average by independent averages in both arguments. Averaging each feature of (5) in both arguments leaves a positive Gram expansion. The crossing bonds at the two cuts are disjoint. In every case the unnormalized reflection form is consequently
\[
 \sum_\alpha c_\alpha\int W_0(Y)
  \left|\int F(Y,U_+)W_+(Y,U_+)\Phi_\alpha(U_+)\,dU_+\right|^2dY\ge0,
 \qquad c_\alpha\ge0.                                      \tag{7}
\]
The summable feature bounds justify the integrations. No gauge invariance of \(F\) is needed. Relabelling proves reflection invariance. Replacing \(F\) in (7) by \(Fe^E\) proves the perturbation claim. Reflection interchanges the two half algebras. The coordinate argument also works on the labelled two-site quotient: its two cuts use distinct crossing edges. \(\square\)

**Lemma 4 (complex chessboard).** On a split torus with \(2s\) consecutive slabs and RP at every slab-wall pair, let \(F_j\) be bounded complex reference-slab functions and \(F_j^{[k]}\) their conjugated reflection copies. Then
\[
 \left|\mu\!\left(\prod_{j=1}^{2s}F_j^{[j]}\right)\right|
 \le\prod_{j=1}^{2s}
       \mu\!\left(\prod_{k=1}^{2s}F_j^{[k]}\right)^{1/(2s)}.
\]
On a cubic board with an even number of cells per axis, define
\[
 p_{l,\ell}(F)=\mu_\ell\!\left(\prod_C F^{[C]}\right)^{1/N_b},
 \qquad N_b=(\ell/l)^4.
\]
Then
\[
 \left|\mu_\ell\prod_C F_C\right|\le\prod_Cp_{l,\ell}(F_C),\quad
 p(F+G)\le p(F)+p(G),\quad p(zF)=|z|p(F),\quad
 p(\bar F)=p(F),\quad p(1)=1.                               \tag{8}
\]
All roots here are nonnegative real roots.

*Origin:* `am1-port.md` §4 and `d2-d4.md` §2; `o4-check-1.md` §1 and `bridge-check.md` §1. SA 2885–2942, 23640–23707; Y3 73667–73782.

*Proof.* A fully disseminated slab product is \(\Theta H\,H\) at opposite walls, so its expectation is nonnegative. Transport all profiles to one reference slab, retaining labels. Normalize each occurrence of profile \(j\) by \((Z_j^{\rm dis}+\epsilon)^{1/(2s)}\), where \(Z_j^{\rm dis}\) is its disseminated expectation and \(\epsilon>0\). Among finitely many fillings choose a maximum absolute normalized expectation. Reflection Cauchy–Schwarz bounds its square by the product of the two reflected half-fillings. Their normalization factors together reproduce the original factors twice. Both reflected expectations are nonnegative and at most the maximum, so both maximize if the maximum is positive.

Choose a maximizer with the longest constant cyclic run. For run length at most \(s\), retain a half starting at that run; reflection doubles it. Once the run contains a half, reflect that half to get a constant filling. Thus a constant filling maximizes. Its normalized expectation is \(Z_j^{\rm dis}/(Z_j^{\rm dis}+\epsilon)\le1\). The zero maximum is immediate. Let \(\epsilon\downarrow0\), including vanishing disseminated integrals. This proves the one-direction bound without a power-of-two restriction.

Apply it successively in the four coordinate directions. Reflections in different directions commute and copy the preceding patterns literally, giving exponent \(1/N_b\) for each original profile. Expanding the dissemination of \(F+G\), then using that bound on every term, gives \((p(F)+p(G))^{N_b}\) as an upper bound and proves the triangle inequality. Half of the copies are conjugated, proving absolute homogeneity. Conjugating the nonnegative full expectation proves conjugation invariance. The last assertion is normalization of \(\mu_\ell\). \(\square\)

**Lemma 5 (lower tangent).** Let \(\Gamma\subset Q\subset\mathbb Z^4\) be period groups and \(D\) a site transversal of \(\Gamma\). Let \(\nu\) be a \(Q\)-invariant DLR state and \(A\) real local, with bond support in \(x_0+[0,r]^4\), \(x_0\in\mathbb Z^4,r\in\mathbb N\). Set
\[
 \mathbb A=\sum_{v\in Q/\Gamma}\tau_v A,\quad m=[Q:\Gamma],\quad
 \partial_rD=\{x\in D:x+w\notin D\text{ for some }w\in\mathbb Z^4,
                                      |w|_\infty\le r\}.
\]
For every real \(t\),
\[
 \log\frac{Z_\Gamma(t\mathbb A)}{Z_\Gamma(0)}
 \ge tm\nu(A)-\{48\beta+2|t|\|A\|_\infty(2r-1)^4\}|\partial_1D|.    \tag{9}
\]

*Origin:* `am1-port.md` §4; `o4-check-1.md` §1; SA 2127–2190, 2944–2991; Y3 73576–73665.

*Proof.* Integrate the positive bonds anchored in \(D\). Interior plaquettes agree with their torus representatives. For each of six coordinate planes, three plaquettes meet the positive bonds from a site. Hence at most \(18|\partial_1D|\) noninterior plaquettes meet these bonds. At most \(6|\partial_1D|\) torus plaquettes have no interior representative. The difference of the two actions has oscillation at most \(2\beta(18+6)|\partial_1D|\). Comparing normalized densities therefore costs at most \(48\beta|\partial_1D|\).

Retain the \(m_{\rm in}\) source classes with a representative wholly supported on the integrated bonds. Conditional Jensen bounds their conditional log exponential moment below by their conditional mean. Integrating against \(\nu\), DLR and \(Q\)-invariance give \(tm_{\rm in}\nu(A)\). Adding omitted terms and then replacing \(m_{\rm in}\) by \(m\) cost at most \(2|t|\|A\|_\infty(m-m_{\rm in})\).

Assign each omitted class its unique anchor from \(x_0+v+\Gamma\) in \(D\). These anchors are distinct and lie in \(\partial_rD\). From each follow a path of at most \(r\) steps of sup norm one to its first exit. Its last point inside lies in \(\partial_1D\), within sup distance \(r-1\) of the anchor. Thus \(|\partial_rD|\le(2r-1)^4|\partial_1D|\), proving (9). \(\square\)

**Lemma 6 (strict convolution and a continuous square-root kernel).** Use inner products antilinear in the first entry. For \(\beta>0\), the operator \(K\) with kernel (5) on \(L^2(G)\) is positive, injective and trace class. Its positive square root has a real continuous symmetric kernel \(q\). For finite \(S\), let \(K_S=\bigotimes_{b\in S}K\), \(Q_S=K_S^{1/2}\) and let \(q_S\) be its product kernel. Then
\[
 \langle q_u,q_{u'}\rangle=k_S(u,u'),\qquad \|q_u\|_2=1,
 \quad q_u=q_S(u,\cdot).                                    \tag{10}
\]
Both \(K_S,Q_S\) map every tensor product of finite-degree polynomial spaces onto itself and commute with every simultaneous vertex gauge action. If a finite complex measure on \(G^S\times Y\), \(Y\) compact metrizable, annihilates all \((K_S\varphi)(u)\chi(y)\), with polynomial \(\varphi\) and \(\chi\) in a uniformly dense subalgebra of \(C(Y)\), it is zero.

*Origin:* `am1-port.md` §6; `o4-check-1.md` §1, including its missing-commutation correction. Y3 78336–78494 supplies the character-based analogue; the polynomial argument here is the checked note's own proof.

*Proof.* Let \(\mathcal P_r\), \(r\ge0\), be the real-coordinate polynomials of degree at most \(r\) on \(S^3\), complexified. Set \(\mathcal P_{-1}=0\) and \(\mathcal W_r=\mathcal P_r\ominus\mathcal P_{r-1}\). Convolution gives
\[
 (Kf)(g)=\int k(z,1)f(z^{-1}g)\,dz.
\]
Quaternion multiplication is linear in \(g\), so \(K\mathcal P_r\subset\mathcal P_r\). Symmetry makes each \(\mathcal W_r\) invariant. Coordinate polynomials contain constants, are self-adjoint and separate points; Stone–Weierstrass gives uniform density. Expansion (5) yields a sum of positive multiples of squared polynomial moments for \(\langle f,Kf\rangle\). All coefficients are strictly positive when \(\beta>0\). Vanishing therefore implies \(f=0\). Each finite-dimensional real symmetric restriction to \(\mathcal W_r\) has strictly positive eigenvalues.

Normalized sphere measure is Haar measure, since quaternion multiplication preserves it. The sum of the traces of the positive rank-one terms in (5) is
\[
 e^{-\beta}\sum_{m\ge0}\frac{\beta^m}{m!}
 \int_{S^3}\left(\sum_{j=1}^4s_j^2\right)^m ds=1.
\]
Thus the series converges in trace norm and \(K\) has trace one. Projecting to \(\mathcal W_r\) kills all features of degree below \(r\). Its trace is at most
\[
 T_r=e^{-\beta}\sum_{m\ge r}\frac{\beta^m}{m!}\le\frac{\beta^r}{r!};
\]
the last inequality uses \((r+j)!\ge r!j!\).

The space \(\mathcal W_r\) is invariant under \(O(4)\) acting on the internal sphere. For any orthonormal basis its diagonal reproducing kernel is constant by transitivity, hence equals \(\dim\mathcal W_r\). Choose a real eigenbasis \(e_{rj}\) of \(K\) there. Cauchy–Schwarz bounds the absolute value of the square-root kernel block by
\[
 \left|\sum_j\sqrt{\lambda_{rj}}e_{rj}(s)e_{rj}(s')\right|
 \le(\dim\mathcal W_r)\sqrt{T_r}
 \le {r+4\choose4}\frac{\beta^{r/2}}{\sqrt{r!}}.               \tag{11}
\]
The successive-term ratio of the last series tends to zero. Uniform convergence gives a real continuous symmetric kernel for \(K^{1/2}\). Convolving two root kernels gives the kernel of \(K\); equality, initially in \(L^2\), holds everywhere by continuity and full support of Haar measure. Tensor products give (10), since \(k_S(u,u)=1\).

Simultaneous endpoint gauges preserve \(k_S\) and product Haar measure. Thus \(K_S\) commutes with their unitary pullbacks. Conjugating its positive root by any such unitary gives another positive square root of \(K_S\); uniqueness gives commutation for \(Q_S\), and hence for the Haar projection. This supplies the gate's omitted sentence.

The finite polynomial restrictions of \(K_S,Q_S\) have positive spectra and are onto. Their products with the specified \(\chi\)'s are uniformly dense in \(C(G^S\times Y)\), again by Stone–Weierstrass. A finite measure annihilating them annihilates every continuous function and is zero. \(\square\)

**Lemma 7 (transfer insertions and adjacent-layer exchange).** Use direction 4 as time; spatial bonds lie in a three-dimensional time slice. Write \(u_t\) for the spatial bonds in layer \(t\), and \(w_t(x)\) for the vertical bond from \(t\) to \(t+1\). For finite spatial \(S\) and bounded \(X\) on \(L^2(G^S)\), set
\[
 A_X(u,u')=\frac{\langle q_u,Xq_{u'}\rangle}{k_S(u,u')},\qquad
 A_X^{(t)}=A_X(u_t|_S,(w_t\cdot u_{t+1})|_S).                \tag{12}
\]
These are continuous, \(A_1=1\), and \(\|A_X\|_\infty\le e^{2\beta|S|}\|X\|\). They preserve reality and tensor products on disjoint sets. On a spatial torus, with all spatial bonds denoted by \(S_0\), let \(P\) be vertex gauge averaging, \(E\) multiplication by the spatial Wilson weight, and
\[
 Q=K_{S_0}^{1/2},\qquad M=QPEQ.
\]
On a torus with \(s\ge3\) time layers, disjoint insertions in each layer tensor to \(X_t\), and
\[
 Z(0)=\operatorname{Tr}M^s,\qquad
 \mu\!\left(\prod_t A_{X_t}^{(t)}\right)
 =\frac{\operatorname{Tr}(X_1M\cdots X_sM)}{\operatorname{Tr}M^s},
 \qquad \left|\mu\!\left(\prod_t A_{X_t}^{(t)}\right)\right|
 \le\prod_t\|X_t\|.                                        \tag{13}
\]
Every periodic DLR state at \(\beta>0\) satisfies, for continuous \(H\),
\[
 \nu H(u_t|_S,(w_t\cdot u_{t+1})|_S)
 =\nu H((w_t\cdot u_{t+1})|_S,u_t|_S).                       \tag{14}
\]

*Origin:* `am1-port.md` §6; `o4-check-1.md` §1. Y3 78496–78685 and its trace lemma 71563–71603; SA 2313–2452 gives a related gauge-equivariant insertion argument.

*Proof.* Equation (10), continuity of \(u\mapsto q_u\) in \(L^2\), and \(k_S\ge e^{-2\beta|S|}\) give the first assertions. A vertical plaquette has weight
\[
 k(u_t(b),(w_t\cdot u_{t+1})(b)),\quad
 (w_t\cdot u_{t+1})_{xy}=w_t(x)u_{t+1,xy}w_t(y)^{-1}.
\]
Multiplication by (12) replaces its product kernel by that of \(QX_tQ\). Integrating the vertical variables gives the kernel of \(EQX_tQP\). Integrating the cyclic layer variables gives the trace of their product. Cycling the first \(EQ\) to the end gives the numerator in (13), since \(P\) commutes with \(E,Q\). The cyclic operations are legitimate: \(Q\) is Hilbert–Schmidt, and the products have two such factors and otherwise bounded factors. Also
\[
 M=(E^{1/2}PQ)^*(E^{1/2}PQ)\ge0
\]
is trace class. Empty insertions give the positive denominator.

Here is the trace estimate used in (13). For \(2s\) Hilbert–Schmidt factors \(B_j\), normalize each nonzero factor to \(\operatorname{Tr}|B_j|^{2s}=1\). Maximize trace modulus among words of length \(2s\) in these factors and their adjoints. Alternating words have trace one. Writing a word as \(XY\) with equal halves, Hilbert–Schmidt Cauchy–Schwarz gives
\[
 |\operatorname{Tr}XY|^2\le\operatorname{Tr}(XX^*)\operatorname{Tr}(Y^*Y).
\]
Both reflected words of a maximizer therefore maximize. Choose a maximizing word with the longest cyclic string alternating one operator and its adjoint. If that string has length at most \(s\), put its end at the half boundary and reflect that half: the alternating string doubles. If it is longer, reflect a half contained in it. Thus an entirely alternating word maximizes, with trace one. Undoing normalization proves
\[
 |\operatorname{Tr}(B_1\cdots B_{2s})|
 \le\prod_j(\operatorname{Tr}|B_j|^{2s})^{1/(2s)}.
\]
Zero factors give zero directly. Apply this to \(X_tM^{1/2},M^{1/2}\). For positive compact \(C\le D\), an eigenbasis of \(C\), scalar Jensen in an eigenbasis of \(D\), and summation show \(\operatorname{Tr}C^s\le\operatorname{Tr}D^s\). Applied to
\(M^{1/2}X_t^*X_tM^{1/2}\le\|X_t\|^2M\), it proves the last inequality of (13).

Now let \(D\) be bounded, real and skew-adjoint. The real unitary \(X_\varepsilon=e^{\varepsilon D}\) has norm one, and the operator-exponential remainder in (12) gives
\[
 A_{X_\varepsilon}^{(t)}\in[1/2,3/2],\qquad
 \phi_\varepsilon:=\log A_{X_\varepsilon}^{(t)}
 =\varepsilon A_D^{(t)}+O(\varepsilon^2)                    \tag{15}
\]
uniformly for sufficiently small real \(\varepsilon\). Choose a period \(N\ge3\) of \(\nu\) so large that translates of \(S\) by \(N\mathbb Z^3\) are disjoint. On the side-\(iN\) torus the array of \(\phi_\varepsilon\) over \(N\mathbb Z^4/(iN)\mathbb Z^4\) has \(i^4\) terms. There are \(i^3\) disjoint spatial insertions at each selected height. Disjointness modulo the torus follows from disjointness under \(N\mathbb Z^3\). Formula (13) bounds the partition ratio by one. Enclose the support in a fixed integer cube and use (9):
\[
 0\ge i^4\nu(\phi_\varepsilon)-C_\varepsilon i^3.
\]
Send \(i\to\infty\) with \(\varepsilon\) fixed. Equation (15) for both signs, followed by \(\varepsilon\to0\), gives \(\nu(A_D^{(t)})=0\).

A real antisymmetric polynomial \(\Phi(u,u')\) belongs to a finite tensor polynomial space from Lemma 6. Expand in a real eigenbasis and divide each coefficient by \(\sqrt{\lambda_\alpha\lambda_{\alpha'}}\). The resulting finite-rank operator \(D\) is real skew-adjoint and satisfies \(\langle q_u,Dq_{u'}\rangle=\Phi(u,u')\). For real continuous \(H\), approximate
\(k_S(u,u')[H(u,u')-H(u',u)]\) by real antisymmetric polynomials. This follows by polynomial density and then antisymmetrization. Division by the positive lower bound for \(k_S\) preserves uniform convergence. The preceding zero expectations give (14). Complex linearity covers complex \(H\). \(\square\)

**Lemma 8 (temporal gauge and determination by two layers).** Temporal-gauge images of DLR states obey the layer equations (16) below. Two laws obeying those equations at \(\beta>0\) and agreeing on two consecutive entire layers agree on every layer. Consequently every periodic Wilson DLR state is invariant under all coordinate bond reflections and under \(2\mathbb Z^4\). The periodic class equals \(\mathcal G^P\), and is nonempty, compact and convex.

*Origin:* `am1-port.md` §7; `o4-check-1.md` §1; Y3 78814–78967, Lemmas IV-54-9, IV-54-13 and Proposition IV-54-16.

*Proof.* Fix \(t_0\). Recursively, in both time directions, set
\[
 \widehat w_{t_0}=1,\quad \widehat w_{t+1}=\widehat w_tw_t,
 \qquad \widetilde u_t=\widehat w_t\cdot u_t.
\]
Each coordinate uses finitely many original bonds, so the map is continuous. It sets every vertical bond to one. Gauge-invariant local \(F\) satisfies \(F(U)=F(U[\widetilde u])\), where \(U[\widetilde u]\) has these spatial layers and unit vertical bonds.

For finite spatial \(S\), let \(V_S\) be the sum of spatial plaquette actions meeting \(S\). A spatial bond meets four such plaquettes, so \(0\le V_S\le8|S|\). The unnormalized layer kernel is
\[
 k_S(\widetilde u_{t-1}|_S,v)
 e^{-\beta V_S(v\vee\widetilde u_t|_{S^c})}
 k_S(v,\widetilde u_{t+1}|_S).                              \tag{16}
\]
Its value and its Haar integral are between \(e^{-12\beta|S|}\) and one. The normalized layer kernel replaces \(\widetilde u_t|_S\) by \(v\) with this density and holds every other coordinate fixed. A layer law obeys the layer equations when it is fixed by each such kernel on continuous local tests. Integrating only the original horizontal bonds \(S\) at height \(t\) leaves all \(\widehat w_j\) fixed. The Haar-preserving substitution \(v=\widehat w_t\cdot U_S\) turns the conditional density into (16): there is one vertical plaquette above and below each bond and the spatial terms \(V_S\). This proves the layer equations.

Symmetry of \(k_S\) makes the equations covariant under \(R_m\widetilde u=(\widetilde u_{m-t})_t\). If the image law is \(R_{2t_0+1}\)-invariant, reflection of \(U[\widetilde u]\) is \(U[R_{2t_0+1}\widetilde u]\). The original state and its bond-reflected state therefore agree on gauge-invariant local tests. Both are DLR states by covariance of (1), so Lemma 2 makes them equal.

For determination, suppose two layer laws agree on layers \(m,\ldots,n\), \(m<n\). For finite \(S\) set
\[
 u'=\widetilde u_{n+1}|_S,\quad v=\widetilde u_n|_S,\quad
 c=(\widetilde u_n|_{S^c},\widetilde u_{n-1},\ldots,\widetilde u_m),
\]
\[
 \Phi(v;c)=k_S(\widetilde u_{n-1}|_S,v)
              e^{-\beta V_S(v\vee\widetilde u_n|_{S^c})},\qquad
 N(u',c)=\int k_S(v,u')\Phi(v;c)\,dv.
\]
Here \(c\) ranges over a compact countable product. These functions are continuous and local, with \(\Phi\ge e^{-10\beta|S|}\) and \(N\ge e^{-12\beta|S|}\). If \(\rho_i'\) is the marginal on \((u',c)\), put \(\sigma_i=N^{-1}\rho_i'\), a finite measure. The layer equation for the joint marginal \(\rho_i\) is
\[
 \rho_i(\psi)=\int d\sigma_i(u',c)\int k_S(v,u')\Phi(v;c)
                                      \psi(u',v,c)\,dv.        \tag{17}
\]
The replacement changes neither \(u'\) nor \(c\), which justifies this marginal equation. Take \(\psi=\varphi(v)\chi(c)/\Phi(v;c)\), with \(\varphi\) polynomial and \(\chi\) continuous local. This is a continuous local test on the already equal layers; \(n-1\ge m\) is essential. Subtraction gives
\[
 \int (K_S\varphi)(u')\chi(c)\,d(\sigma_1-\sigma_2)=0.
\]
Lemma 6 gives \(\sigma_1=\sigma_2\), and (17) gives equality on these marginals. Enlarge \(S\) to contain any specified finite test in layer \(n+1\). This extends agreement to \(m,\ldots,n+1\). Reflection covariance gives extension to \(m-1\). Iteration determines all continuous cylinder integrals, hence the whole law.

For periodic \(\nu\), the two layers at the temporal-gauge base are \(u_{t_0}\) and \(w_{t_0}\cdot u_{t_0+1}\). Lemma 7 exchanges their joint law, first on finite supports and then on the entire layers by measure determination. The temporal law and its reflected law obey (16) and agree on these two layers. Determination and the preceding gauge argument prove bond-reflection invariance. Apply the same proof to coordinate permutations of \(\nu\), which remain periodic DLR states. Composing bond reflections at \(1/2\) and \(3/2\) yields translation by two. Thus every periodic state is in \(\mathcal G^P\); the converse follows because \(P\) has finite index. Lemma 2 gives nonemptiness, compactness and convexity. \(\square\)

**Lemma 9 (comparison at a prescribed mirror).** For every periodic Wilson DLR state \(\nu\), admissible mirror and real local \(A\) in its closed positive half, there is a periodic Wilson DLR state \(\nu_0\), invariant and RP there on continuous local half tests, with \(\nu(A)\le\nu_0(A)\).

*Origin:* `am1-port.md` §§4–5; `o4-check-1.md` §1, including its omitted choice of \(r\). SA 2993–3114; Y3 78688–78808, Proposition IV-29-40.

*Proof.* Choose a nonempty finite support \(B_A\) in the half, even for constant \(A\). Choose an integer cube \(x_0+[0,r]^4\) containing all its bonds. This explicitly supplies \(r\) in (9). Fix a period \(N\) of \(\nu\), then \(h\in2N\mathbb N\) large enough for the support to lie in \(c\le n\cdot x\le c+h\). Put \(v_h=hn/q\). For \(n=e_1+e_2\), use
\[
 T=N\{\mathbb Z(e_1-e_2)\oplus\mathbb Ze_3\oplus\mathbb Ze_4\},
 \quad Q=T\oplus\mathbb Zv_h,\quad
 \Gamma_i=iT\oplus\mathbb Z(2iv_h),\quad i\ge3.             \tag{18}
\]
Then \(Q\subset N\mathbb Z^4\), \(\iota=[\mathbb Z^4:Q]=N^3h\), and \([Q:\Gamma_i]=2i^4\). A site transversal is
\[
 0\le x_1-x_2<2iN,\quad0\le x_1+x_2<2ih,\quad
 0\le x_3,x_4<iN.                                         \tag{19}
\]
The first two coordinates have equal parity. Reduction modulo their even periods preserves parity and gives unique representatives, so \(|D_i|=2i^4N^3h\). Each diagonal coordinate has four possible boundary layers under a displacement of sup norm at most one. Each remaining coordinate has two. The equal-parity count gives equal sizes to those layers. Thus
\[
 \frac{|\partial_1D_i|}{|D_i|}\le\frac6{iN}+\frac2{ih}.      \tag{20}
\]
For a coordinate normal take \(T=N\mathbb Z^3\) in the tangent directions and the normal interval \([0,2ih)\). The same index holds; its sharper bound is \(6/(iN)+1/(ih)\), so (20) applies. Signed permutations give all other normals. Since \(\Gamma_i\subset i\mathbb Z^4\), shortest periods tend to infinity.

Let \(A_T=\sum_{v\in T/iT}\tau_vA\) and use slabs numbered \(j=1,\ldots,2i\). Their copying maps are
\[
 w_{2k+1}=\tau_{2kv_h},\qquad w_{2k}=\theta_{c+kh},\qquad
 \vartheta=\theta_{c+h/2}.
\]
Define the unfolded and folded arrays
\[
 \mathbb A^u=\sum_{j=1}^{2i}\tau_{(j-1)v_h}A_T,
 \qquad \mathbb A^f=\sum_{j=1}^{2i}w_jA_T.                   \tag{21}
\]
In reference-slab coordinates the unfolded exponential profiles alternate between \(f=e^{tA_T}\) and \(\vartheta f\). Translation by \(v_h\) takes the full fold of one to that of the other: \(\tau_{v_h}w_j=w_{j+1}\vartheta\). Their disseminated expectations agree. Lemma 4 gives \(Z(t\mathbb A^u)\le Z(t\mathbb A^f)\).

The folded source is \(E+\theta E\) at every slab wall, by dividing its slab indices into two reflected halves. Any coincident boundary copies can be shared with half weight. Lemma 3 gives mirror invariance and RP; tangential translations also preserve the law \(\mu_{i,t}\). These symmetries make all \(m=2i^4\) source terms have expectation \(\mu_{i,t}(A)\). For fixed \(t>0\), Lemma 5, folding and Jensen in the folded measure give
\[
 \begin{split}
 tm\nu(A)-[48\beta+2t\|A\|_\infty(2r-1)^4]|\partial_1D_i|
 &\le\log\frac{Z(t\mathbb A^u)}{Z(0)}\\
 &\le\log\frac{Z(t\mathbb A^f)}{Z(0)}
 \le tm\mu_{i,t}(A).                                      \tag{22}
 \end{split}
\]
Indeed the last inequality is \(-\log\mu_{i,t}(e^{-t\mathbb A^f})\le t\mu_{i,t}(\mathbb A^f)\). After division by \(tm\), the error is at most
\[
 \iota[48\beta/t+2\|A\|_\infty(2r-1)^4]
                 [6/(iN)+2/(ih)]\longrightarrow0.
\]

For the volume limit use the one fixed infinite family indexed by \((j,v)\in\mathbb Z\times T\), with terms \(t w_j\tau_vA\) and supports \(w_j(B_A+v)\). A bond belongs to at most \(2|B_A|\) supports. Translation by \(g_\perp+2ikv_h\in\Gamma_i\) sends \((j,v)\) to \((j+2ik,v+g_\perp)\); its quotient has \(2i\cdot i^3\) terms, exactly (21). Lemma 2 therefore gives a perturbed DLR subsequential limit \(\nu_t\), with period \(T\oplus\mathbb Z(2v_h)\). A finite positive-half test fits inside the corresponding torus half for large \(i\). Thus invariance and RP pass to \(\nu_t\), and (22) gives \(\nu(A)\le\nu_t(A)\).

Now take a subsequential limit as \(t\downarrow0\). The local perturbation is uniformly \(O(t)\), so Lemma 2 makes its limit \(\nu_0\) an unperturbed DLR state with the same finite-index period. The expectation inequality, invariance and RP pass to this limit. Lemma 8 upgrades its period to \(P\). The volume-first order within this argument is required by the \(1/t\) error in (22). \(\square\)

**Theorem 10 (all mirrors for every periodic state).** Every periodic Wilson DLR state at \(\beta>0\) is invariant and reflection positive at every admissible mirror (3), on both full bounded Borel half algebras. It is invariant under \(\mathbb Z^4\rtimes W_4\), where \(W_4\) is the signed permutation group. The periodic class equals \(\mathcal G_{1,\beta}\).

*Origin:* `am1-port.md` §8; `o4-check-1.md` §1; SA 3116–3176; Y3 78969–79035, Proposition IV-54-17.

*Proof.* Fix a mirror and let \(\mathcal R\subset\mathcal G^P\) be the class RP there on continuous local positive-half tests. Lemma 9 with \(A=0\) gives nonemptiness. Each condition \(\rho(\overline{\theta F}F)\in[0,\infty)\) is closed and affine in \(\rho\). Lemma 8 therefore makes \(\mathcal R\) compact convex.

Suppose \(\nu\notin\mathcal R\). Some finite collection of real continuous test integrals separates it from \(\mathcal R\): otherwise compactness and the finite intersection property would produce a member agreeing on every continuous function. In the resulting finite-dimensional compact convex set, let \(p\) be the nearest point to the vector \(x\) of \(\nu\)'s integrals. Minimizing squared distance along a segment gives \((x-p)\cdot(y-p)\le0\). The corresponding real continuous test therefore has strictly larger \(\nu\)-expectation than all members of \(\mathcal R\). Approximate it uniformly by a real local \(A_0\), retaining the strict gap.

Translate its support into the positive half by \(v=2kn\), \(k\) sufficiently large. All states in \(\mathcal G^P\) have this period, so the gap remains for \(A=\tau_vA_0\). Lemma 9 supplies \(\nu_0\in\mathcal R\) with \(\nu(A)\le\nu_0(A)\), a contradiction. Thus every periodic state is RP on continuous local half tests.

Positivity makes \(B(F,G)=\nu(\overline{\theta F}G)\) Hermitian: expand its diagonal at \(F+zG\) for \(z=1,-1,i,-i\). Taking one entry equal to one gives \(\nu(F)=\nu(\theta F)\) in the positive half. For arbitrary local \(F_0\), translate by the same type of normal period \(v\). Since \(\theta\tau_v=\tau_{-v}\theta\), invariance under both periods extends that equality to \(F_0\). Continuous local tests determine the law, so \(\theta_*\nu=\nu\).

For bounded Borel \(F\) in the entire positive-half algebra, conditional expectations onto increasing finite coordinate sets converge in \(L^2(\nu)\). Continuous functions are dense in \(L^2\) for each finite compact marginal. Combining these approximations gives continuous local half tests \(F_j\to F\) in \(L^2(\nu)\). Reflection invariance gives the same convergence after reflection. Hence
\[
 |B(F_j,F_j)-B(F,F)|
 \le\|F_j-F\|_2(\|F_j\|_2+\|F\|_2)\longrightarrow0.
\]
RP passes to the full Borel algebra. Reflection gives the negative half.

There are four coordinate and twelve diagonal normal families. Composing adjacent site and bond reflections gives unit translations. Coordinate site mirrors give sign changes, and \(x_\mu=x_\lambda\) gives coordinate exchanges. These generate \(\mathbb Z^4\rtimes W_4\). Translation-invariant states are periodic by definition; the converse has just been proved. \(\square\)

**Lemma 11 (all-state chessboard domination).** Fix \(a=L^{-K},\beta>0\) and \(l=L^j\ge a\). Choose a board whose faces are bond mirrors. For every periodic Wilson DLR state \(\rho\), finite set of occupied cells, bounded Borel cell functions \(F_C\), and every compatible sequence \(\ell_k=2L^{m_k}\to\infty\),
\[
 \left|\rho\!\left(\prod_C F_C\right)\right|
 \le\liminf_k\prod_Cp_{l,\ell_k}(F_C).                       \tag{23}
\]
If needed, restrict to \(m_k\ge m_0\) for the already fixed localization size \(M=L^{m_0}\). This is a cofinal restriction.

*Origin:* `d2-d4.md` §2; `bridge-check.md` §1. Theorem 10 supplies its essential S1g input, whose omission from the old skeleton's dependency row the gate corrects. SA 23709–23766, ST3–ST4.

*Proof.* For bounded real one-cell \(H\), sum its \(N_b\) mirror copies in a large cube of side \(\ell\). Theorem 10 gives expectation \(N_b\rho(H)\). Conditional Jensen and DLR bound it by the supremum of the conditional log exponential moment over external configurations. Integrate positive bonds anchored at the \(n^4\) cube sites, \(n=\ell/a\). The source factors do not use crossing bonds and agree exactly with their torus counterparts. The action comparison in Lemma 5 has no omitted-source cost here and is at most
\[
 48\beta|\partial_1D|\le384\beta n^3,
\]
since at most eight boundary layers occur. Thus
\[
 \rho(H)\le\log p_{l,\ell}(e^H)
                  +384\beta l^4a^{-3}\ell^{-1}.             \tag{24}
\]
This is uniform in the exterior, at fixed \(a,\beta,l\).

For real bounded \(G\), choose \(0<t<(2\|G\|_\infty)^{-1}\), with the zero function immediate, and put \(H=\log(1+tG)\). For \(|x|\le1/2\), integration of \((\log(1+x)-x)'=-x/(1+x)\) gives \(\log(1+x)\ge x-x^2\). Lemma 4 gives \(p(1+tG)\le1+tp(G)\), and \(\log(1+y)\le y\) for \(y\ge0\). Consequently
\[
 \rho(G)\le p_{l,\ell}(G)+t\|G\|_\infty^2
                    +384\beta l^4a^{-3}\ell^{-1}/t.
\]
Take \(\ell_k\to\infty\) before \(t\downarrow0\). This proves the one-cell inequality with a lower limit along any compatible sequence. For complex \(F\), choose its expectation's phase \(\phi\) and use
\(p(\operatorname{Re}(e^{-i\phi}F))\le p(F)\), a consequence of (8).

Enclose all occupied cells strictly inside a larger aligned cell whose side is \(L^k l\), with \(k\ge0\) sufficiently large. Such a cell exists by enlarging the side while keeping a fine-cell centre as its centre; its faces remain fine-board faces. The one-cell inequality applies to \(G=\prod_CF_C\). Disseminate that coarse cell on each sufficiently large torus and apply (8) on the fine board. Each original profile occurs once per coarse cell; the remaining fine cells carry one. Taking the coarse-cell root gives
\(p_{\rm coarse,\ell}(G)\le\prod_Cp_{l,\ell}(F_C)\), proving (23). No source estimate or perturbed-state hypothesis enters this proof. \(\square\)

**Lemma 12 (Lemma S: incompatible adaptations).** No full-rank period lattice \(\Gamma\subset\mathbb Z^4\) is adapted, in the sense of (4), to both \(e_4\) and \(e_1-e_4\).

*Origin:* `t0-skeleton.md` §2, checked in `am1-port.md` §1; `o4-check-1.md` §1 preserves the qualification below. Adaptation is Y3 73363–73374.

*Proof.* Adaptation makes orthogonal projection onto either normal line map \(\Gamma\) onto its intersection with that line. Write those intersections as \(p\mathbb Ze_4\) and \(q\mathbb Z(e_1-e_4)\), with positive integers \(p,q\). Reflection in the second normal preserves \(\Gamma\) and swaps coordinates 1 and 4. Thus \(pe_1\in\Gamma\). Its projection onto the second line is \(p(e_1-e_4)/2\), so \(p=2qk\) for a positive integer \(k\). Projecting \(q(e_1-e_4)\) onto \(\mathbb Re_4\) gives \(-qe_4\in\Gamma\), so \(q=pj\) for a positive integer \(j\). These imply \(1=2kj\), impossible. \(\square\)

This excludes simultaneous adaptation, not every possible finite-volume argument or joint limit. Volume-first is the route used here to obtain infinite-volume states; it is not a necessity theorem about all constructions.

**Theorem 13 (LG1).** Fix \(d=4,G=SU(2)\), an odd block factor \(L\ge3\), \(a>0\) and \(\beta>0\), in the order above. Then the six clauses of the LG1 skeleton hold:

1. **Finite cutoff.** The cubic Wilson law \(\mu_{K,\ell,\beta}\), when \(a=L^{-K}\), is a probability measure. Barycentre observables obey \(O_a(f)\circ r^*=O_a(rf)\) for every lattice isometry (on a quotient, every isometry of that quotient). If \(f\) is supported in an open side of a coordinate bond mirror, its observable uses bonds in that side.
2. **DLR.** At fixed \(a,\beta\), periodic lifts of torus laws with diverging shortest periods have DLR weak limits. The translation-invariant class \(\mathcal G_{a,\beta}\) is nonempty compact convex, and its finite-bond conditional kernels preserve continuous local functions.
3. **Torus positivity and chessboards.** Cubic tori with an even number of sites per axis have RP at every coordinate site and bond mirror pair. The one-direction and four-direction chessboard estimates hold in their complex form (8). Their all-state consequence is (23), with no RG hypothesis.
4. **Common period.** Every periodic Wilson DLR state is invariant under coordinate bond reflections and translations by \(2a\mathbb Z^4\).
5. **All mirrors.** Every such state is invariant and RP on both full bounded Borel half-space bond algebras at all coordinate site, coordinate bond and diagonal lattice mirrors. In physical coordinates, coordinate heights belong to \((a/2)\mathbb Z\) and diagonal heights to \(a\mathbb Z\), using the unnormalized normals (3). Compositions give invariance under \(a\mathbb Z^4\rtimes W_4\). The periodic class equals \(\mathcal G_{a,\beta}\).
6. **Lemma S.** No lattice period group is adapted to both normals \(e_4\) and \(e_1-e_4\).

*Origin:* The LG1 entry of ym4-assembly.md §§4–5, assembled from the note and gate origins recorded in Lemmas 1–12.

*Proof.* At unit spacing the clauses are Lemmas 1–4, 8, 11–12 and Theorem 10. Multiplication of every spatial coordinate and period by \(a\) gives the stated general spacing. The block factor is used only to specify compatible boards and cutoffs, not in the Gibbs-state arguments. No first-passage or renormalisation-group result is read. \(\square\)

The same conclusions hold at \(\beta=0\). In that case (1) fixes every finite marginal to product Haar. This unique state is isometry invariant and RP: condition on any mirror bonds, and the independent reflected halves give an integral of squares. All finite-measure and chessboard proofs above already allow zero coupling. The strict-injectivity argument is needed only for \(\beta>0\).

## Source record and definitions supplied

All external source files below are at `31a47c543775`, credited above. Each was fetched once. Reads were bounded excerpts, not whole files. The outline objects were located first through `sa-index/README.md`, neighbouring rows of chunks 01–04, 06 and 22, and the corresponding entries of `obligations.md`.

| Source | Passages checked for this part | Use |
|---|---|---|
| SA, `/tmp/sa_ym4.tex` | 229–294; 418–469; 2084–2194; 2313–2453; 2698–3194; 4429–4440; 4486–4500; 6905–6915; 23640–23766 | Finite foundations, lower tangent, insertion comparison, full split-torus/folding/separation argument, G1 and DLR definitions, barycentre conventions, ST1–ST4. The outline gives detailed proofs for these lattice steps; its common-period continuation is not the route copied here. |
| Y3, `/tmp/sa_YM3_I.tex` | 71563–71632; 73102–73800; 78336–79037 | Trace inequality; DLR and adapted periods; lower tangent and folding; transfer insertions; prescribed-mirror comparison; temporal gauge and two-layer determination; common period and all mirrors. These are detailed proofs. The changes of dimension are displayed in the hand proofs above. |
| CA-I, `/tmp/sa_ca_I.tex` | Fetched as requested; no passage used or quoted | No CA input is needed for LG1. CA-II and CA-III are not used. |

The definitions supplied or made explicit in this distillation are:

1. The action of isometries on configurations, observables and tests, with inverses on reversed bonds; the open-side condition for the barycentre support assertion.
2. The distinction between a periodic law and a periodic configuration, the translation-invariant class \(\mathcal G_{a,\beta}\), and the fixed-period class \(\mathcal G^P\).
3. The precise DLR kernel, normalized Haar convention, locally finite perturbation family, and finite-quotient convention, including labelled edges on a two-site axis.
4. The unnormalized mirror normals, their admissible heights, both full closed-half Borel algebras, and the antilinear reflection \(\Theta_c\).
5. Adaptation and split-torus height periods; open-cell bond algebras, conjugated dissemination and its seminorm; \(N_b\) distinct from the state period \(N\).
6. The source support \(B_A\), enclosing cube \(x_0+[0,r]^4\), site transversal, boundary layers, unfolded/folded arrays, and their index action.
7. Polynomial spaces, root-kernel vectors, layer operators, temporal-gauge coordinates and normalized layer equations, with each operator's domain stated at its use.

## Result

LG1 proves all six skeleton clauses at fixed spacing, with the explicit open-side support convention in clause 1. It also proves complex all-state chessboard domination and the product-Haar endpoint \(\beta=0\). Its only imports are the foundational mathematical tools listed above. It has no RG, small-coupling, continuum-limit or all-state-symmetry premise.

Corrections and completions made during distillation:

- Chose the integer support-cube size \(r\) before applying the folding estimate, as required by `o4-check-1.md`.
- Proved explicitly that gauge commutation of \(K_S\) implies gauge commutation of its positive root and the gauge projection.
- Kept the gate's distinction between site-plane RP in `upper-chain.md` Lemma 1.1 and the crossing-kernel proof needed for bond-plane chessboards. Finite chessboard positivity is proved here, not left as an input.
- Kept all-state reflection invariance as an explicit dependency of (23), proved by Theorem 10. No D1 premise from the later sections of `d2-d4.md` is imported into this lattice result. That gate's nonnegative-bump correction concerns the later mean-difference proof, which is not a statement of LG1.
- Restricted the barycentre support sentence to an open half, stated the admissible mirror heights and full Borel algebras, and retained the distinction between lattice and quotient isometries.
- Gave an explicit harmless boundary constant 384 in (24), derived from the checked incidence count, and separated the board cell count from the state period.
- Kept Lemma S's corrected scope: simultaneous adaptation is impossible; necessity of volume-first for every construction does not follow.
- Made the foundational imports, all finite-volume embedding conditions, and the volume-before-source limits explicit. LG1 imposes no additional condition on IN1's constant order.

No mathematical step of this assembled fixed-lattice argument is left **Outstanding**. All proof steps above are hand arguments; retrieval, searches and file bookkeeping discharge none of them. This is a distillation of checked research notes, **not yet refereed as a whole part**. It grants no scientific or audit status and proves no continuum Yang–Mills existence theorem.

## Change log (pass 3 fixes, lead, 2026-11-05)

Applied the findings of `gates/lg1-gate.md` (Claude fresh session, first failing step none):
1. Lemma 1's origin: upper-chain Text section 0 uses the dyadic corner field, not barycentres; it supports only the finite-measure bound.
2. Lemma 7: "P commutes with E, Q" is used one line later, to write M as a product with its adjoint, not in the cycling step.
3. Lemma 9: the sentence about coincident boundary copies shared with half weight is withdrawn; each folded term lies in one closed half.
4. Board copies: the composition of reflections is unique as a group element, not as a word; the conjugation parity is well defined.

**Status: frozen.** Reopens only on a `wrong` signal.
