# The complete sixth-order bilinear return: bounded mixed channel and a node dichotomy

**Author conditional derivation, 2026-09-13. No independent review or audit.** The analytical proof was written before its small supporting checks; their results and limits are recorded in Section12. It does not evaluate the native node scalar, choose a Hamiltonian, derive Record formation, or establish an interacting phase.

## 1. Exact supplied domain and source boundary

Use the whole native CAR/Z2 dictionary and the weak-electric Hamiltonian, after its scalar subtraction,

\[
 H(u)=H_0+uV,\qquad V=\frac12\sum_{\{e,f\}:e\ne f,\ e\cap f\ne\varnothing}Z_eZ_f.
\]

Each unordered pair is counted once. Use the canonical pi-flux representative on the cubic antiperiodic tori L=4M, M>=32, its simple pure active Gaussian vacuum Omega_L, and its spectator space with the original physical parity. H=H_pi-E0>=0 is the active excitation generator; no uniform positive active gap is assumed. The fixed canonical ground cluster is isolated at every finite volume, as supplied by the endpoint/isolation theorems. Its isolation radius may shrink with volume. The result below concerns Taylor coefficients at u=0, not a uniform expansion at fixed nonzero u.

The supplied uniform flux stiffness says that, relative to this SAME E0, every noncanonical plaquette sector satisfies H_F-E0>=kappa k(F), where k(F) counts its bad faces. Either active parity is allowed by the spectator freedom, so this is a full-active inequality. Set delta=kappa>0 as a conservative common floor for all noncut local masks encountered below. A pure winding change has no such floor, but none of the bounded-support masks used below is a pure winding change. This last point is proved below, not inferred from the stiffness itself.

The source results already supply:

- the exact finite native closure and energy-dependent third-order star vertex O_v=(1/8)sum_(A disjoint C) R_C gamma_v R_A;
- uniformly rapidly quasi-local odd vacuum creators Y_v Omega=O_v Omega=chi_v;
- a smooth Majorana coefficient symbol D(k), with weighted coefficient convergence in the finite-volume limit;
- the real scalar node value D(0)=alpha I in the specified smooth doubled-cell gauge;
- a bounded, indeed absolutely summable, higher-odd singleton return after removing the actual one-particle part.

These are pinned conditional suppliers, not freshly audited claims. The full finiteL4 sixth coefficient is already in the source. The proposed extension here is the complete large-volume mixed-channel bound and its consequence for the full sixth bilinear symbol. The source pins and reading coverage are in BLOCK05_WORKING_PLAN.md and the source manifest to be completed with the checks.

## 2. Small cuts on every cubic torus L>=4

**Lemma.** If S is a vertex subset of C_L cubed, L>=4, with at most12 edges in its boundary, then S or its complement contains at most two vertices.

For any coordinate direction a, examine the L perpendicular two-dimensional slices. A nonconstant slice has at least four internal boundary edges. One elementary proof of this two-dimensional assertion: two mixed rows already give four horizontal boundary edges; one mixed row gives two horizontal edges and at least two vertical edges; no mixed row with a nonconstant slice gives at least two entire row boundaries, hence at least2L edges. Thus at most three slices in each direction are nonconstant. At least one slice in each direction is constant because L>=4.

Any two constant slices in different directions intersect, so their constant membership values agree. Comparing to one constant slice in another direction also shows that all constant slices in the same direction share that value b. Replace S by its complement if b=1. The resulting set A is contained in at most three coordinate values in each direction. Every coordinate line meeting A is therefore mixed, since three<L.

Let p_a be the number of lines parallel to a meeting A, equivalently the size of its projection onto the other two coordinates. Each contributes at least two boundary edges, so sum_a p_a<=6. The elementary discrete Loomis-Whitney inequality gives |A|^2<=p_1 p_2 p_3<=8, and hence |A|<=2.

For completeness the needed inequality follows without a geometric theorem import. Let a_xy,b_xz,c_yz be the zero-one indicators of the three projections. Then

\[
 |A|\le\sum_{xyz}a_{xy}b_{xz}c_{yz}
 \le \|c\|_F\|a^Tb\|_F
 \le\|c\|_F\|a\|_F\|b\|_F
 =\sqrt{p_1p_2p_3}.
\]

The first inequality may overcount triples, which is in the correct direction. Cauchy-Schwarz proves the two matrix norm inequalities.

A mask of at most12 edges with zero elementary plaquette boundary is a cut in the large-volume domain L>=128. To see this, the mask is a closed Z2 one-cochain. Its period along a coordinate loop is the same for all L^2 parallel loops, since plaquette closure permits moving the loop. If that period is odd, every such edge-disjoint loop meets the mask, requiring at least L^2 edges. Since12<L^2, all periods vanish. Integrating the cochain from a base vertex then defines a vertex sign, whose coboundary is the mask. Thus a noncut mask of this size has a bad face. This argument keeps winding sectors separate and does not claim their uniform gap.

## 3. Why the first nonscalar vacuum coefficient is sixth and is quadratic

A word of n electric pairs toggles at most2n edges. A return to the canonical magnetic orbit is a cut delta S. Closing it into the fixed representative contributes

\[
 \prod_{v\in S}(-i\gamma_v\beta_v).
\]

All intervening active Hamiltonians and resolvents are even. Projection onto the definite-parity active vacuum kills odd |S|. Empty S is spectator-scalar; replacing S by its complement changes only the fixed total physical parity. The preceding lemma therefore leaves only two-vertex spectator bilinears through order6.

For n<=5, a two-vertex cut is possible by edge count only for adjacent centers, whose boundary has10 edges. At order5 each boundary edge would occur exactly once. Removing the internal edge, that boundary is the disjoint union of two five-edge stars: no triangle supplies a shared outer vertex. Pairing incident boundary edges cannot join the two components. Each component has an odd edge count, so five incident-edge pairs cannot use this boundary. Hence every returning coefficient through order5 is scalar. The same proof applies with arbitrary positive powers of any intermediate resolvent, or spectral derivatives, since neither operation changes edge support or active parity.

Let P retain the canonical active vacuum and physical spectator space, Q=I-P, and R=Q(E0-H0)^(-1)Q at fixed finite L. The canonical effective Hamiltonian is defined by the positive-overlap polar identification of its isolated spectral cluster with P. Its sixth nonscalar part is therefore precisely the nonscalar part of

\[
 PVRVRVRVRVRVP. \tag{3.1}
\]

Here is the normalization reason. Resolvent/contour expansion of the cluster projector and its polar normalization expresses every correction to the irreducible chain as a product of at least two returning blocks, with possible spectral derivatives. At total order6 each block has order at most5. Every such block is scalar by the preceding support/parity argument. The zeroth shifted energy vanishes on P, so a sixth-order normalization factor cannot multiply a nonzero zeroth energy. Thus these corrections affect only the scalar coefficient. Equivalently, the finite-energy Feshbach coefficients through order5 are scalar functions of the spectral parameter; replacing that parameter by the perturbed scalar energies and normalizing the wave operator cannot introduce a nonscalar order6 term. This is a finite-volume coefficient statement, with no all-active Schrieffer-Wolff gap assumption.

For same-sublattice centers the full sixth bilinear coefficient vanishes. In a bipartite active Fock frame, take black gamma real and white gamma imaginary. H_F, real-energy resolvents and the canonical active vacuum can be chosen real. For a same-sublattice pair gamma_v gamma_w is real. Its coefficient multiplying beta_v beta_w is then real, whereas Hermiticity demands a purely imaginary coefficient because beta_v beta_w is anti-Hermitian. These bilinears are linearly independent on the physical spectator parity space: the trace of a product of distinct grade2 monomials vanishes both with and without the full chirality insertion for N>=128^3. Thus there is no cancellation between different monomials that could evade this conclusion. Individual non-Hermitian ordered words need not vanish.

Write the remaining nonscalar term as

\[
 Q_6=\sum_{v<w} b_{vw}\,i\beta_v\beta_w
     =\frac i4\sum_{vw}B_{vw}\beta_v\beta_w,\qquad B_{vw}=2b_{vw},
\]

with real antisymmetric B. This fixes the normalization used below.

## 4. Complete words for a distant pair and their two channels

Take distinct opposite-sublattice v,w at graph distance at least3. Their six-edge stars are disjoint and have no common outer vertex. Their cut has12 boundary edges. Every order6 word for this cut therefore uses each edge exactly once. Each incident pair lies in one star. There are15 pair partitions of each star,225 pair sets, and6!=720 orders per set.

A proper prefix has even numbers of used edges in each star. The graph left after deleting v,w is connected in the large cubic torus. Choose a horizontal plane whose height avoids both deleted vertices. From any surviving site, one of its four horizontal neighbor columns avoids the two deleted coordinate columns; use that neighbor, travel vertically to the chosen plane, and connect within the plane. This supplies an explicit avoiding path. A cut contained in the two stars is therefore, up to complement, empty, either singleton, or the full two-vertex cut. No proper prefix is empty or full because all edges are used once. A singleton prefix occurs exactly when the first three insertions complete one star. There are2*(3!)^2=72 such orders per pair set. The other648 orders have a noncut mask at all five proper prefixes. Thus there are16200 singleton-middle and145800 mixed orders per distant pair.

The singleton orders sum EXACTLY to the second-order return through the actual third-order vertices, with the retained odd active excitation inverse. This is the source's vertex identity, now with its entire complementary family retained. In particular no individual active inverse is bounded by the wrong-flux gap.

Every mixed proper-prefix Hamiltonian has the floor delta from Section1. In the unreduced-link representative write its active Hamiltonian as

\[
 H_{F_j}-E0=H+B_{v,j}+B_{w,j},\qquad j=1,\ldots,5.
\]

Each B is an even bounded quadratic operator on its own one-star support; reversing a link changes only that link term. A completed local star is allowed among these B's. It need not itself have a gap: only the combined proper-prefix Hamiltonian must, and does, retain another nontrivial flux defect.

In canonical endpoint order, the cut closure of two vertices is +gamma_v gamma_w beta_v beta_w. The mixed coefficient therefore uses

\[
 b^{\rm mix}_{vw}=-\frac{i}{64}\sum_{\rm mixed\ words}
 \langle\gamma_v\gamma_w R_{F_5}R_{F_4}R_{F_3}R_{F_2}R_{F_1}\rangle,
 \quad R_F=-(H+B_F)^{-1}. \tag{4.1}
\]

The five negative inverse signs are INCLUDED in R_F. Reversing a word and applying its gauge return ensures the summed coefficient is real and antisymmetric; one may equivalently take the Hermitian antisymmetric part of the displayed oriented kernel. The same convention reproduces the source singleton b=-2alpha^2 K/omega^2 on the flat finiteL4 example. The small checks below must verify this sign separately.

## 5. A uniform two-impurity cocycle factorization

Let tau_t(A)=e^(-itH)A e^(itH), and define

\[
 U_X(t)=e^{-it(H+B_X)}e^{itH}.
\]

The finite-range quadratic H has the usual graded propagation bound, derived directly by its one-particle hopping-path expansion. For bounded even fixed-star perturbations a distance R apart this gives

\[
 \|[\tau_{-r}(B_X),\tau_{-s}(B_Y)]\|
 \le C\exp(v|r-s|-\mu R). \tag{5.1}
\]

All constants are independent of total volume and seam signs; fixed star size and hopping enter them. Cap this by2||B_X||||B_Y|| when useful.

In the interaction picture V_X(t)=e^(itH)e^(-it(H+B_X)), the generator is G_X(s)=tau_(-s)(B_X). Compare V_(X+Y) to V_X V_Y. The latter has generator G_X(s)+V_X(s)G_Y(s)V_X(s)^*. By unitary Duhamel,

\[
 \|V_{X+Y}(t)-V_X(t)V_Y(t)\|
 \le\int_0^{|t|}ds\int_0^sdr\,
       C e^{v(s-r)-\mu R}
 \le \tfrac C2 |t|^2 e^{v|t|-\mu R}. \tag{5.2}
\]

For negative t reverse the parameter direction; the same norm estimate holds. Conjugating by e^(-itH) gives the identical bound for U_(X+Y)-U_X U_Y. Norm2 is also an upper bound, since both terms are unitary. This proof does not assume commuting impurities or multiply an extensive Hamiltonian norm into the estimate.

A single U_X(t), and tau_s(U_X(t)), has even unitary local approximants in a ball of radius r about X with error bounded by C exp(c(|s|+|t|)-mu r). For example truncate the propagated local generator in the interaction-picture differential equation, choosing Hermitian even truncations, and integrate its propagation error. Polynomial time factors can be absorbed by increasing c. The same statement for gamma_X times finitely many such factors gives odd norm-one approximants. These facts also follow directly from the quadratic propagation estimate and unitary Duhamel, without a gapped reference vacuum.

## 6. Factor every mixed integrand into two odd families

Use the SAME smooth odd inverse filter as the uniform star theorem: f(x)=-1/x for x>=delta, with Fourier representation f(x)=integral w(t)e^(-itx)dt and every absolute time moment of w finite. It also agrees with -1/x on x<=-delta, but only its positive spectral action is needed here. The filter does not impose an active gap.

Since H Omega=0, the product of five resolvents has the exact vacuum identity

\[
 R_{F_5}\cdots R_{F_1}\Omega
 =\int_{\mathbb R^5}\!\prod_{j=1}^5w(t_j)\,
    \prod_{j=5,\ldots,1}^{\rm ordered}
        \tau_{s_j}(U_{F_j}(t_j))\,\Omega\,d^5t,
 \quad s_j=\sum_{\ell>j}t_\ell. \tag{6.1}
\]

The product is ordered from5 down to1. This follows successively from R_F X Omega=integral w(t)U_F(t)tau_t(X)Omega. Every factor is unitary, so the integral is a norm-convergent Bochner integral bounded by M0^5.

For each word label a (its two local pair partitions and its mixed shuffle), split U_Fj into U_vj U_wj by (5.2). Reorder the resulting factors, and move gamma_w past the even v-factors. Keeping the local chronological order gives

\[
 \gamma_v\gamma_w\prod_{j=5,\ldots,1}\tau_{s_j}(U_{F_j}(t_j))
   =X_v^a(\mathbf t)Y_w^a(\mathbf t)+E_{vw}^a(\mathbf t),
\]

\[
 X_v^a=\gamma_v\prod_{j=5,\ldots,1}\tau_{s_j}(U_{v,j}(t_j)),
 \qquad
 Y_w^a=\gamma_w\prod_{j=5,\ldots,1}\tau_{s_j}(U_{w,j}(t_j)). \tag{6.2}
\]

Both X and Y are ODD unitaries. All crossings involved even factors, except an odd gamma crossing an even factor, so the distant graded reordering sign is plus. Disjoint local approximants commute at these crossings. Their approximation errors and (5.2) give, with S=sum_j|t_j|,

\[
 \|E_{vw}^a(\mathbf t)\|
 \le\min\{2,C e^{cS-\mu R}\}. \tag{6.3}
\]

There are a fixed finite number of crossings. Using a larger C,c includes their polynomial time factors and fixed support radii. The two exact products being compared are unitary, which justifies the cap2 for their total difference.

For each p, split the integral into S<=eta R and S>eta R, choosing c eta<mu/2. The first part is exponentially small times M0^5. On the second use the absolute p-th moment of the product filter. Thus the integrated remainder kernel satisfies

\[
 |e^a_{vw}|\le C_p(1+R)^{-p} \quad\text{for every fixed }p, \tag{6.4}
\]

uniformly in L. Taking p>3 gives a uniform Schur bound and an absolutely summable remainder. No assertion about decay of ordinary vacuum correlations has been used.

## 7. Graded Gram bounds control the factored kernel

Fix a word label and time tuple. Extend the local definitions of X_v,Y_v to all lattice centers, with their finitely many internal magnetic types. This extension is a mathematical family; near-coincident centers will be corrected separately. Its definition at one center does not depend on the second center's position.

Odd unitary approximants within radius r have an error Ce^(cS-mu r). For distant centers use two disjoint r<R/3 balls; their graded anticommutator is zero. At short distances use norm2. Consequently

\[
 \|\{X_v,X_w^*\}\|\le\min\{2,C e^{cS-\mu' d(v,w)}\}.
\]

There are O((1+r)^3) sites in a radius-r ball on all the finite tori and in the infinite lattice. Split its row sum at r0=C0(1+S). The inner sum is O((1+S)^3), and the outer exponential tail is of the same or smaller order. Hence

\[
 \sup_v\sum_w\|\{X_v,X_w^*\}\|\le C(1+S)^3, \tag{7.1}
\]

and the same bound holds for Y, their adjoints, and finitely many internal types.

For A=sum_v a_v X_v^* one has A^*A<=\{A^*,A\} as positive operators. Thus

\[
 \|A\Omega\|^2\le\|A\|^2
 \le\|\{A^*,A\}\|
 \le C(1+S)^3\sum_v|a_v|^2. \tag{7.2}
\]

The last step is the Schur estimate applied to the nonnegative anticommutator majorant. Define V_X e_v=X_v^*Omega and V_Y e_w=Y_w Omega. Their norms are at most C^(1/2)(1+S)^(3/2). The factored matrix is exactly

\[
 N_{vw}(\mathbf t)=\langle X_vY_w\rangle=(V_X^*V_Y)_{vw},
 \qquad \|N(\mathbf t)\|_{\ell^2\to\ell^2}\le C(1+S)^3. \tag{7.3}
\]

This uses a non-Hermitian odd-family Gram estimate, not a positive-state assumption for a transition functional. It holds in any reference state represented by Omega. Gaussian clustering, an active spectral gap and a pointwise correlation decay are unnecessary.

Integrating (7.3) against product_j|w(t_j)| gives a finite, volume-independent bound. Add (6.4) and the finite number of mixed word labels. Removing a fixed finite set of relative displacements from this extended kernel changes its norm by a bounded finite-range matrix, since its entries are uniformly bounded by M0^5. Therefore the ACTUAL complete distant mixed sixth-order kernel has uniformly bounded l2 operator norm.

## 8. Near centers and the complete mixed channel

Only finitely many relative center placements have distance less3. Same-sublattice terms vanish after the Hermitian sum by Section3. For adjacent centers the ten cut edges occur oddly in twelve occurrences. Either one boundary edge occurs three times or one nonboundary edge occurs twice. The triple-boundary option cannot pair two odd disconnected boundary stars. A repeated nonboundary bridge can contribute only if it connects their incidence components. Both endpoints then lie in the fixed union of the two stars, so the number of possible bridges and words is bounded independently of volume. The source's literal large-torus census has one internal and four square bridges; the boundedness argument only needs finiteness and does not rely on that exact census.

No proper prefix of a nonscalar adjacent word is empty: consuming at least two insertions with zero net mask would leave at most eight occurrences for a ten-edge target. A proper even two-vertex cut is also impossible: every proper prefix has at most5 insertions, and Section3 excludes a two-vertex cut with that many incident pairs by edge count and incidence parity. This is a combinatorial exclusion before any vacuum projection. A singleton return can occur only after exactly three insertions: it requires at least six occurrences, and its symmetric difference with the target is the other singleton, also requiring six. Both halves must therefore be exact three-pair stars.

Consequently the only non-gapped proper cuts are again the singleton middle cuts already included in the actual star-vertex return. Every remaining proper prefix is a noncut local mask of at most10 edges, so its full-active inverse norm is at most1/delta. Each mixed word has magnitude at mostdelta^(-5)/64. The number of words and near neighbors is uniformly finite, giving a uniform Schur bound for the actual near mixed correction.

Combining Sections4-8 proves the proposed bound

\[
 \sup_L\|B_L^{\rm mix}\|_{\ell^2\to\ell^2}<\infty. \tag{8.1}
\]

It is a bound on the sum of EVERY mixed order6 word contributing a spectator bilinear, with its actual loss-free resolvents and native closure. No scalar sixth energy is evaluated. The constants are existence bounds from the supplied stiffness, local hopping and inverse-filter moments; no practical numerical value is asserted.

## 9. Thermodynamic mixed kernel and the actual linear singleton

For each fixed pair of centers, the mixed entries converge as L grows. In (6.1), truncate the time tuple to a compact box; finite-range local dynamics, local perturbation cocycles and the canonical local vacuum state converge there. The common product-filter tails then remove that truncation. This is the same local-CAR identification as the thermodynamic star source, with finitely many additional fixed local perturbations. Its use does not globally embed a finite periodic Fock space into the infinite one.

The common operator bound (8.1) and convergence on finitely supported test sequences define a bounded infinite mixed operator. Magnetic covariance of the complete word sum gives a fixed-cell translation-invariant matrix kernel. The discrete Fourier transform therefore represents it by an essentially bounded matrix multiplier. This is an L-infinity symbol bound; no continuous or differentiable mixed symbol is asserted. Centered zero extensions converge weakly on test sequences. Strong norm convergence of whole finite operators is not asserted.

For the singleton channel define

\[
 T_{vw}=\langle\chi_v,H^{-1}\chi_w\rangle,
 \qquad\chi_v=O_v\Omega.
\]

The actual vertex is -i O_v beta_v. Anticommuting its spectator through the other odd active vertex, and using the NEGATIVE active excitation resolvent, gives the total ordered singleton expression

\[
 -\sum_{vw}T_{vw}\beta_v\beta_w.
\]

Its scalar diagonal can be discarded when discussing nonscalar coefficients. Since T is Hermitian,

\[
 b_{vw}^{\rm single}=-2\operatorname{Im}T_{vw},\qquad
 B^{\rm single}=2i(T-T^T). \tag{9.1}
\]

Transpose here is a matrix transpose in REAL-SPACE Majorana coordinates, not an adjoint. In Bloch form it becomes T(-k)^T. The anti-linear physical Majorana reality convention must be transported if the Bloch gauge is changed.

Decompose chi into its actual one-particle and higher-odd vacuum transitions. H preserves excitation number, so their cross terms vanish. The source already proves that the higher-odd T has summable rows and a bounded continuous Fourier multiplier. Thus the only possible unbounded sixth bilinear symbol comes from T1.

Let Gamma map a Majorana coefficient vector e_j to gamma_j Omega. In a fixed canonical quadratic frame h=iK, omega=|h|, one has

\[
 \Gamma^*\Gamma=I+h/\omega,
 \qquad H\Gamma=\Gamma h.
\]

The first formula follows from the pure Gaussian vacuum covariance; the second follows directly from [H,gamma_j]=-i sum_l K_jl gamma_l. The right side of the first formula is twice the positive-frequency projection, so the apparent negative-frequency inverse below has no negative spectral weight. If D maps center coefficients to the actual one-particle Majorana coefficient family, then

\[
 T_1(k)=D(k)^*\frac{I+h(k)/\omega(k)}{\omega(k)}D(k). \tag{9.2}
\]

All normalizations are in the source convention {gamma_i,gamma_j}=2delta_ij. For a flat source with D=alpha I, (9.1)-(9.2) give b_vw=-2alpha^2 K_vw/omega^2, exactly the source finiteL4 singleton coefficient. This is a normalization check; the L4 value is not imported as an infinite node value.

## 10. The complete conditional node dichotomy

Use the source's smooth doubled-cell Majorana gauge, which is the identity at the node and respects the Majorana reality relation. Its active symbol is

\[
 h(k)=4t_{\rm hop}\sum_{a=1}^3\sin(k_a/2)\Gamma_a,
 \quad \omega(k)=4|t_{\rm hop}|\sqrt{\sum_a\sin^2(k_a/2)},
\]

where the three real symmetric Clifford matrices anticommute and square to I. In particular h(-k)^T=-h(k), omega is even, and omega(k) is comparable to |k| near zero. The source's actual smooth transition family has

\[
 D(k)=\alpha I+O(|k|),\qquad \alpha\in\mathbb R.
\]

Therefore (9.2), with bounded first derivatives of D, gives

\[
 T_1(k)=\alpha^2\left[\frac I\omega+\frac h{\omega^2}\right]+O(1).
\]

The remainder is uniformly bounded on a punctured node neighborhood, without assigning a projector at k=0. Applying the real-space transpose operation cancels the scalar I/omega term and doubles the odd h/omega^2 term. After adding the bounded higher-odd and mixed channels,

\[
 B_6(k)=\frac{4i\alpha^2h(k)}{\omega(k)^2}+R_6(k),
 \qquad R_6\in L^\infty \text{ near the node}. \tag{10.1}
\]

Equivalently the Hermitian spectator symbol is

\[
 iB_6(k)=-\frac{4\alpha^2h(k)}{\omega(k)^2}+iR_6(k). \tag{10.2}
\]

The L-infinity assertion is in essential supremum. A bounded measurable mixed remainder cannot cancel the displayed singularity on any positive-measure punctured cone. In particular, if alpha!=0,

\[
 \|iB_6(k)\|=\frac{4\alpha^2}{\omega(k)}+O(1)
\]

almost everywhere near the node. The complete sixth bilinear is an unbounded one-particle multiplier, even though each real-space row still has finite l2 norm. It has not become an infinite energy density or a contradiction: |k|^(-1) is locally integrable and square integrable in three dimensions.

If alpha=0, D(k)=O(|k|), so T1(k)=O(|k|). The higher-odd and mixed multipliers remain bounded. Thus the COMPLETE infinite sixth bilinear multiplier is bounded in this alternative. Neither alternative evaluates alpha, and no implication from a nonzero finite-volume transition norm to alpha!=0 is used.

For finite volumes, weighted coefficient convergence ensures D_L(k_L)->alpha I at every sequence of smallest antiperiodic momenta k_L->0, and likewise at -k_L. Uniform coefficient norms give a one-particle upper bound C/omega_min,L=O(L), while the mixed and higher-odd bounds are uniform. If alpha!=0, the antisymmetric leading expression at these momenta has norm (4alpha^2+o(1))/omega_min,L. Hence

\[
 cL\le\|B_{6,L}\|\le CL
\]

for all sufficiently large allowed L, with c>0. Here omega_min,L=4|t_hop|sqrt(3) sin(pi/L) in the folded convention.

There is a necessary limit distinction when alpha=0: the source gives convergence of D_L but no quantitative nodal rate sufficient to bound D_L(k_L)/|k_L| uniformly. Therefore boundedness of the infinite multiplier does NOT by itself imply a uniform bound on the finite norms in the alpha=0 case. The proved finite conclusion there is at most o(L), together with the general O(L) envelope. A stronger finite bound needs a finite-size nodal estimate. This limitation is retained rather than silently exchanging limits.

## 11. What this result changes, and what it leaves open

The mixed sixth histories are not negligible in magnitude: on finiteL4 the source's mixed contribution dominates the singleton coefficient. The new proposed bound concerns their infrared operator class. It allows an exact conditional leading singular symbol for the COMPLETE sixth bilinear without computing145800 mixed words at every separation.

If the native alpha is nonzero, uniform elimination of the active vacuum cannot be justified by treating its sixth bilinear coefficient as a bounded perturbation of the gapless active symbol. A joint active/spectator treatment or another controlled reorganization remains available. This is a requirement on that approximation scheme, not an axiom no-go. The coefficient alone does not prove a resummed mass, spectral gap, transport law, or interacting phase.

If alpha is zero, the singularity is absent at this order; the bounded residual still needs actual evaluation and higher-order control. Neither outcome selects the supplied Hamiltonian or the canonical Gaussian preparation. Record formation, conditional locality, renewal and physical observable maps retain their separate obligations.

The small checks and the author proof review are recorded below. Every displayed new theorem remains author conditional-support pending external review. Existing source theorems retain their own conditional status and provenance.


## 12. Same-agent checks, proof review and literature attribution

The literal L8 geometry checker independently builds stars, square faces and incidence matchings from coordinates. It enumerates162000 distant-pair words and187920 adjacent-pair words. Distant counts are16200 singleton and145800 mixed; adjacent counts are16200 singleton and171720 mixed, including all four external bridges. Their proper mask counts are1022 and1534. Every noncut proper prefix has at least six bad faces in these two fixtures. All29 named geometry groups passed; the349920 words are coverage, not349920 independent tests. Runtime0.51s, maximum resident memory20414464bytes. This checks local combinatorics on L8; it is outside the uniform spectral domain and supplies no spectral extrapolation.

The separate small algebra checker passed53 groups. The exact2-active/2-spectator CAR fixture at omega=7/3, alpha=5/4 gives b=-75/56 and B01=-75/28. Positive instead of negative excitation inverse, half the bilinear coefficient, and adjoint instead of real-space transpose each fail the actual identity. Non-Hermitian odd-unitary Gram maps are checked directly against the state contraction; an incorrect adjoint and ordinary odd commutator are discriminated. Exact coupled cocycle jets first differ at order3, with Frobenius squared coefficient16/2025; deleting the intervening coupling makes all checked jets equal through degree5. Numerical exponentials at times+/-0.1,+/-0.2 satisfy the conservative Duhamel bound. The five-cocycle suffix-time identity has residual2.22e-16, whereas omitting the common dynamics gives error0.03433 and using prefix rather than suffix times gives0.01116. The8-component Clifford symbol check uses an explicitly synthetic smooth D; it does not evaluate native alpha. Runtime0.87s, maximum resident memory95502336bytes.

The proof review traced: all small cuts; winding exclusion; scalar folded blocks; native two-vertex closure; singleton denominator parity; all648 mixed shuffles; full-active wrong-flux floor; exact right-to-left cocycle times; odd rather than even endpoint families; Gram adjoints; summable error versus bounded main kernel; real-space transpose in Bloch space; and the missing finite-size nodal rate when alpha=0. The latter caveat was kept explicitly. No claim of independent review is made: both checkers and this proof were authored in the same campaign.

The general Duhamel and quasi-local integral methods are established mathematical machinery. Primary-source verification used Nachtergaele, Sims and Young, [Quasi-Locality Bounds for Quantum Lattice Systems, Part I](https://arxiv.org/html/1810.02428), Section2.3.2, Proposition2.6 and its proof (v2). The paper primarily treats commuting disjoint-site algebras and explicitly points to its fermionic companion; its bosonic locality is not silently used for odd operators here. The present graded estimates follow from the supplied quadratic CAR hopping-path bound, with the odd Gram step written explicitly. No historical-priority claim is made. The new repository-facing composition is the complete native mixed-return bound and its conditional node consequence.
