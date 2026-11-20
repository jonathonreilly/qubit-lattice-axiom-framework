# Repo search

**GUIDE.** Row 1290, research at `32900f4f0`. The lead's November 8 search found bounded soft-route results and copies of hard-route work. I checked the closest sources on the fetched heads. PR 10114 gives a one-step Wilson plaquette witness at every finite positive coupling and physical-time contraction for its bare parameter up to $1/32$. Grok's PR 10133 leaves the crossover estimate CW and source transport MG2 open. PR 10134 distinguishes a nonempty excited space, a positive threshold and Yang–Mills identification. PR 10141 estimates a constrained classical quadratic form. On main, Theorem ZD-c relates the periodic thermal criterion to a volume-dependent energy and a state-counting bound. These results leave a physical weak-coupling estimate to prove. [Lead's search](prior/repo-search-2026-11-08.md)

**GUIDE.** In the soft-route folder I checked `f76f6c649c:MASS_GAP_LOCAL_BLOCK_ASTRA.md` 4–14 and 106–149, and `89faef229f:MASS_GAP_CROSSOVER_REDUCTION.md` 77–86. The remaining sources are `1e70c7211a:library/mass-gap-interface.md` I1–I5 in the hard-route folder, `a2f6a430e2:research/ym4d/library/fp1.md` 299–315, and `8b11ae2bb9:research/mass-gap/library/gap-phys-seed.md` 305–329. The target-specific prior digest is absent. The open registry has no entry under the physical mass gap or singlet thermal trace. Row 1283 gives its author’s finite-cutoff reduction (40) to a rank-one approximation on selected endpoints. It leaves an absolute, order-one remainder to control. [Row 1283](gap-solve32-astra62.md)

**GUIDE.** Ethan Sussman and Levent Alpoge, with Claude and Codex as authors of their text, distinguish scalar reconstruction from identification of the full theory. Their outline allows a continuous energy measure down to zero under polynomial clustering. Their complete account explicitly excludes a mass gap from its assertion. The index entries in chunks 01 and 29 and the obligations at 588–599 and 31871–31882 locate this distinction. Row 1218 records a conditional propagation of a full thermal estimate by Deep Bhattacharjee, Ushashi Bhattacharya, James Montgomery Lockwood, Tristan Romanov, Ikailo John Sessford and Sanjeevan Singha Roy. It also records conditional cube-relaxation and spectral criteria. I use the reading for their scope. [Outline, 31858–31882](https://github.com/ethanwsussman/Yang--Mills-LLM-experiment/blob/31a47c543775/YM4_sketch_500.tex#L31858-L31882) · [Complete account I, 2704–2712](https://github.com/ethanwsussman/Yang--Mills-LLM-experiment/blob/31a47c543775/theorem_0_complete_account_raw_I.tex#L2704-L2712) · [Published-work reading](prior/gap-onebound-read-sol.md)

## Physical target

**OPEN.** Construct a nontrivial four-dimensional continuum $\mathrm{SU}(2)$ Yang–Mills vacuum theory with the Jaffe–Witten properties. Prove that its physical Hamiltonian satisfies $\ker H=\mathbb C\Omega$ and $\operatorname{spec}(H|_{\Omega^\perp})\subset[\Delta,\infty)$ for a common $\Delta>0$. I start with the interacting, gauge-invariant transfer on a periodic spatial cube. The question is what suppresses singlet excitations at a fixed physical time as the cutoff is removed.

**GUIDE.** I will test whether a slow physical state has small *total* variation in the time-zero Wilson vacuum. Row 1236 bounds its relative gradient on each spatial link separately, by differentiating the transfer into a static-charge sector. Summing its estimate costs the spatial volume. A dimension-independent comparison would allow a Poincaré estimate for the time-zero vacuum to control every excitation at once. I will use the two ends of a single time step and the actual vacuum weight. [Earlier one-link estimate (11)](gap-solve27-astra62.md)

## Total variation of a slow state on a two-slice observable

**GUIDE.** Use the Osterwalder–Seiler and Lüscher transfer in temporal gauge. A point \(x\) of \(M=(S^3)^m\) gives the unit quaternions on the \(m=3n^3\) spatial bonds. Write \(D=4m\) and use probability Haar measure on \(M\). Put \(v(x)=\exp[-V(x)/2]\), where \(V=\beta\sum_{p\ {\rm spatial}}(1-\tfrac12\operatorname{tr}x_p)\). The transfer has symmetric kernel \(v(x)\exp[-\beta |x-y|^2/2]v(y)\). Spatial gauge transformations act on both slices by orthogonal maps. Restriction to gauge-invariant functions implements the temporal gauge average. Flat centre flips may also be projected out. Positivity of the electric convolution and its normalization are given by GL3 and GL8. [Ethan Sussman and Levent Alpoge, with Claude and Codex, outline 2195–2213 and 2313–2335](https://github.com/ethanwsussman/Yang--Mills-LLM-experiment/blob/31a47c543775/YM4_sketch_500.tex#L2195-L2213)

**GUIDE.** Denote the normalized positive vacuum eigenfunction by \(\psi\), its probability law by \(\nu(dx)=\psi(x)^2dx\), and the reversible vacuum Markov operator by \(P\). Its one-step joint law \(J(dx\,dy)\) is proportional to \(v(x)\psi(x)e^{-\beta|x-y|^2/2}v(y)\psi(y)\,dx\,dy\). Write \(X,Y\) for this pair. Row 947, Theorem BR, interpolates \(J\) by an ambient Brownian bridge. It already deduces a physical spectral bound from Poincaré inequalities for the interpolated laws. I use its midpoint identity B3. With \(\sigma^2=(4\beta)^{-1}\), define
\[
 W=(X+Y)/2,\qquad Z=W+\sigma G,\qquad G\sim N(0,I_D)
\]
with \(G\) independent of the pair. Write \(\omega\) for the law of \(W\), \(\eta\) for that of \(Z\). Given \(Z=z\), the two endpoints are independent with the same law, proportional to \(v(x)\psi(x)e^{-\beta|x-z|^2}dx\). This follows by completing squares. The new question concerns the arithmetic midpoint \(W\) *before* this Gaussian increment. [Row 947, §§5 and 7](gap-fc-max.md)

**PROVED.** Define \(R f(z)=\mathbb E[f(X)\mid Z=z]\). Its adjoint is conditional expectation in the other direction. The preceding conditional independence gives \(P=R^*R\). On \(L^2(\eta)\) put \(K=RR^*\). In either gauge sector the nonzero eigenvalues of \(K\) and \(P\) agree, including multiplicity. Indeed \(r^{-1/2}R\) and \(r^{-1/2}R^*\) are inverse isometries on their respective \(r\)-eigenspaces. The conditional expectations intertwine every simultaneous gauge or centre symmetry. All subsequent forms may be restricted to invariant scalar functions.

**PROVED.** For a bounded \(g\) define \(A g(w)=\mathbb E_G[g(w+\sigma G)]\). With \(\mathcal E(g)=\langle g,(I-K)g\rangle_\eta\), conditional variance gives the exact splitting
\[
 \mathcal E(g)=
 \mathbb E\operatorname{Var}_G(g(W+\sigma G))
 +\mathbb E\operatorname{Var}(Ag(W)\mid X).                              \tag{1}
\]
Indeed the left side is \(\mathbb E\operatorname{Var}(g(Z)\mid X)\). First expose \(Y\) as well and then average it out. The first term has an expansion in all ambient directions. For the probabilists' Hermite polynomials \(H_\alpha\), differentiation of the Gaussian kernel gives
\(\mathbb E_G[g(w+\sigma G)H_\alpha(G)]=\sigma^{|\alpha|}\partial^\alpha Ag(w)\).
Their orthogonality with squared norms \(\alpha!\) follows by multiplying the generating functions \(e^{t\cdot G-|t|^2/2}\) and comparing coefficients in \(e^{t\cdot s}\). For completeness, a Gaussian-square-integrable function orthogonal to all polynomials has an entire Gaussian Laplace transform with every derivative zero at the origin. On imaginary arguments it is the Fourier transform of its finite signed or complex Gaussian-weighted measure, hence that measure vanishes. Thus
\[
 \mathcal E(g)=
 \sum_{k\ge1}\frac{\sigma^{2k}}{k!}
       \int\|\nabla^k Ag\|_{\rm HS}^2\,d\omega
       +\mathbb E\operatorname{Var}(Ag(W)\mid X).                         \tag{2}
\]
Here the norm sums every ordered \(k\)-tuple of ambient directions. Monotone convergence applies to the nonnegative series. The equalities also hold in the Gaussian coefficient sense for \(g\in L^2(\eta)\), by truncation and conditional \(L^2\) convergence. Finite spectral bands away from zero consist of bounded functions on the \(Z\) side because \(P\) has a smooth kernel on the compact slice, its bands there are finite dimensional, and \(R\) preserves boundedness.

**PROVED.** If \(g\) is centered, \(\|g\|_\eta=1\), and supported spectrally in \([1-\delta,1]\) for \(K\), its representative \(h=Ag\) on the unnoised midpoint satisfies
\[
  1-\delta\le\|h\|_\omega^2\le1,\qquad
  \int |\nabla h|^2\,d\omega\le4\beta\delta,\qquad
  \mathbb E\operatorname{Var}(h(W)\mid X)\le\delta.                      \tag{3}
\]
The mean of \(h\) is zero. Its squared norm loss is exactly the first term of (1). The gradient bound uses \(k=1\) of (2). The bound concerns all \(12n^3\) directions together and every superposition in the band. At physical energies at most \(E\), take \(\delta=1-e^{-aE}\le aE\). At \(\beta=O(\log(1/a))\) the total squared gradient tends to zero. This estimates variation on \(\omega\). Row 1236 estimates gradients on \(\nu\). Moving the gradient bound between these two measures is a further problem.

**OPEN.** A sufficient condition for a physical gap is a bound on the centered variance under \(\omega\) by \(C_a\int|\nabla h|^2\,d\omega\) for invariant \(h=Ag\). Indeed (1)–(2) would give \(\|g\|^2\le(1+4\beta C_a)\mathcal E(g)\) for centered \(g\). The required scale is \(C_a=O((a\beta)^{-1})\), uniformly as spatial volume grows. The operator comparison also passes to neutral excitations individually without a thermal count. The following steps test the missing inequality in the actual two-slice law.

## How much of a slow state the midpoint radii can carry

**PROVED.** Fix any \(k\) distinct links \(I\) on the slice. Their positions and \(n\) are unrestricted. Write \(R_I=(|Z_e|:e\in I)\). Let \(\beta\ge1\) and \(0\le\delta\le1/2\). For any centered, unit vector \(f\) in the \([1-\delta,1]\) band of \(P\) and any Borel \(b(R_I)\) of squared norm at most one,
\[
 |\mathbb E[\overline{f(X)}b(R_I)]|
       \le C\big[(k/\beta)^{1/4}+\sqrt\delta\big].                       \tag{4}
\]
There is no bound on the supremum of \(b\). In particular it can be a normalized indicator of an arbitrarily rare set. The same bound, times \((1-\delta)^{-1/2}\), holds for the projection from the centered band of \(K\) onto the radial readings. This last assertion uses the isometry \(R P^{-1/2}\) on the band.

**PROVED.** Put \(A_e=1-X_e\cdot Y_e\). For an endpoint event \(B\), let \(P_B\) denote the one-step kernel of \(P\) with its integrand multiplied by \({\bf1}_B(X,Y)\). The electric multiplier comparison in row 1149 and the half-coupling proof in row 1236 give
\[
 \left\|P_{\exp(\beta A_e/2)}\right\|\le C_0 .
\]
Here and below subscripts that are nonnegative functions denote kernel insertions. Indeed the unnormalized half-coupling factor costs \(z_{\beta/2}/z_\beta\), where \(z_b=\int e^{-b(1-w(u))}du\asymp(1+b)^{-3/2}\). The normalized convolution at \(\beta/2\) is below the one at \(\beta\) in positive-operator order, since all normalized spin multipliers increase with coupling. Tensoring, taking the magnetic sandwich and conjugating by the vacuum preserve the bound. This proof uses the unprojected positive kernel, so absolute values can be taken before applying it. [Row 1149, (16)](gap-solve4-astra62.md) · [Row 1236, proof of (3)](gap-solve27-astra62.md)

**PROVED.** Given \(0<u\le1\), define \(B=\{\beta\sum_{e\in I} A_e^2>u\}\). The inequality \(\beta A^2\le C\beta^{-1}e^{\beta A/2}\) gives \(\|P_B\|\le C k/(\beta u)=:b_0\), by pointwise kernel domination applied to absolute values. In particular \(J(B)\le b_0\). If \(p=\mathbb E[|f(X)|^2{\bf1}_B]\), insert \(f(Y)\) in the second factor. Reversibility gives \(\mathbb E|f(X)-f(Y)|^2\le2\delta\). Cauchy–Schwarz then gives
\[
 p\le b_0+\sqrt{2\delta p},\qquad \sqrt p\le\sqrt{b_0}+\sqrt{2\delta}.    \tag{5}
\]
This controls the exceptional set in every slow state, including states with an unbounded ratio to the vacuum along the sequence.

**PROVED.** Conditional on \(X,Y\), the observed radii have product law \(Q_s\), with \(s_e=|W_e|=\sqrt{1-A_e/2}\). Each factor is the norm of a four-dimensional Gaussian with mean \(s_e(1,0,0,0)\) and covariance \(\sigma^2I_4\). On \(B^c\), \(\sum(1-s_e)^2\le u/(4\beta)\), since \(1-s_e=A_e/[2(1+s_e)]\). For any two good vectors \(s,t\), the squared \(L^2(Q_t)\) norm of \(dQ_s/dQ_t-1\) is at most \(e^{4u}-1\). For the full Gaussians the exact value is \(e^{|s-t|^2/\sigma^2}-1\), by completing squares. Passing to norms conditions their likelihood ratio and decreases its squared norm. Let \(\bar Q\) be the conditional mixture on \(B^c\). Convexity of the reciprocal in the density denominator gives \(\chi^2(Q_s\Vert\bar Q)\le e^{4u}-1\). If \(b_0\le1/2\), \(\|b\|_{L^2(\bar Q)}\le\sqrt2\), because the full observation law dominates \(J(B^c)\bar Q\). Thus the conditional mean of \(b\) on every good pair differs from \(c_b=\bar Q(b)\) by at most \(C\sqrt u\). In the pairing with \(f(X)\) subtract \(c_b\), using \(\mathbb E f=0\). The good contribution costs at most \(C\sqrt u\). The bad contribution costs at most \((1+\sqrt2)\sqrt p\) by (5) and the full \(L^2\) normalization. Taking \(u=\sqrt{k/\beta}\) proves (4) when \(k/\beta\) is sufficiently small. Cauchy–Schwarz covers its remaining range after enlarging \(C\).

**PROVED.** If the \(k\) observed spatial links form a forest, (4) holds for *every* normalized Borel function of their full four-component \(Z_e\), in the gauge-invariant band. Simultaneous vertex gauge rotations preserve the triple law and the factor \(f(X)\). Average the observation over independent Haar vertex rotations. In each tree expose one root frame and then each fresh child frame. Conditional on the lengths, this average gives independent uniform directions on its edges. The averaged observable is a function of \(R_I\), of no larger squared norm. Zero vectors have probability zero under the added Gaussian. In the weak-coupling limit, every such observation on \(k=o(\beta)\) forest links has vanishing projection on the centered bounded-physical-energy band. Cycles and collective readings on larger sets are still available to a physical state.

## Histories of a single radial probe per time step detect the finite-cube edge

**PROVED.** Fix \(n\ge4,\ \beta>0\) and *one* number \(t>0\). At each chosen time step and spatial link \(e\) allow the single insertion \(b_e=\exp(-t|Z_e|^2)\). Use independent bridge noise at successive cuts. Along with unmarked steps, arbitrary finite words of these insertions have dense vacuum span in the gauge-invariant, spatial-centre-neutral Hilbert space. This assertion uses the finite-cube plaquette generation theorem of row 1246, (4). Its generators include individual spatial plaquettes. Here each insertion is on one electric bond and its strength is fixed. [Plaquette generation, including the three periodic seams](gap-solve28-astra62.md)

**PROVED.** In one step integrate the Gaussian. The conditional mean is
\[
 (1+t/(2\beta))^{-2}
 \exp\!\left[-\frac{t(1+X_e\cdot Y_e)}{2(1+t/(2\beta))}\right].         \tag{6}
\]
Up to a positive scalar this changes just that bond's electric coupling from \(\beta\) to \(\beta'=\beta/(1+t/(2\beta))\). Returning from temporal gauge gives the same local insertion on the corresponding temporal plaquette. Let \(C\) be the product of the mass-one electric convolutions at \(\beta\), \(M_v\) multiplication by the magnetic half weight \(v\), and \(\lambda=\|M_v C M_v\|\). The latter normalization includes the one-bond mass factors. Put \(B=C^{1/2}M_v/\sqrt\lambda\). The unmarked and singly marked transfers, up to known positive scalars for the marks, are \(B^*B\) and \(B^*L_eB\). The multiplier of \(L_e\) on link dimension \(d=1,2,\ldots\) is
\[
 l_d=\frac{I_d(\beta')/I_1(\beta')}{I_d(\beta)/I_1(\beta)} .
\]
These numbers strictly decrease with \(d\). Their adjacent quotient is the ratio of \(I_{d+1}/I_d\) at \(\beta'\) and \(\beta\), strictly below one by the variance proof in row 1149. In particular \(0<L_e\le I\) in form sense and every link-spin projection can be recovered from its bounded Borel calculus.

**PROVED.** Work on the neutral gauge-invariant space. Both \(B\) and \(B^*\) have zero kernel since \(C\) has strictly positive multipliers and \(v\) has a positive minimum at fixed volume. The polar isometry of \(B\) is therefore unitary. In its representation the generators are \(F=BB^*\) and \(F^{1/2}L_eF^{1/2}\). Their von Neumann algebra contains \(L_e\). Multiply the latter generator on both sides by \((F+\epsilon I)^{-1/2}\) and let \(\epsilon\downarrow0\). The flanking contractions \(F^{1/2}(F+\epsilon I)^{-1/2}\) tend strongly to \(I\). Thus the algebra contains the electric spin projections on every edge and \(C\) itself. From \(F=C^{1/2}M_v^2 C^{1/2}/\lambda\), the same bounded strong-limit argument recovers \(M_v^2\). Its logarithm recovers multiplication by \(V\).

**PROVED.** The spin projections on \(e\) give the unitary link sign change, with eigenvalue \((-1)^{d-1}\) on dimension \(d\). Write \(S_\xi\) for the simultaneous changes with signs \(\xi_e=\pm1\). For a spatial elementary plaquette \(p\),
\[
 2^{-m}\sum_{\xi}\left(\prod_{e\in\partial p}\xi_e\right)
              S_\xi V S_\xi^*=-\beta M_{w_p},\qquad
               w_p=\tfrac12\operatorname{tr} X_p .                       \tag{7}
\]
Indeed the spatial plaquettes have distinct four-edge supports on this cube. Independent sign averaging kills the constant and all other plaquette characters. This gives the individual spatial multipliers required by row 1246. Its proof of (4), using the single-link heat operators and these multipliers, obtains multiplication by every bounded function on the neutral configuration quotient, up to Haar-null sets. Its exceptional-coupling issue for an *unmarked* electric operator does not arise with the distinct \(l_d\) above.

**PROVED.** The transformed vacuum is \(B\psi\), of norm one. Applying \(C^{1/2}\) gives \(\sqrt\lambda\,M_v^{-1}\psi\), strictly positive everywhere. Multiplying that vector by bounded invariant functions gives a dense subspace, by truncating the ratio of any desired vector to it. Hence the vacuum is cyclic. For bounded self-adjoint generators the closed word span is reducing for each generator, so it equals the von Neumann algebra's vacuum span. Products of the generators are exactly ordered steps of (6) with at most one probe on any one cut. This is also a statement using just the corresponding fixed coupling change on temporal plaquettes of the original Wilson law.

**OPEN.** At fixed cutoff, a common exponential decay rate for correlations of all centered words across an unmarked interval would bound the neutral spectral edge. Indeed any word with nonzero projection on energies below the proposed rate violates its own bound at sufficiently large separation. Cyclicity ensures such a word exists whenever that spectral projection is nonzero. The strong limits in the proof of (7) have no cutoff-uniform control on word lengths or coefficients. Equation (4) leaves room for a low state detected only by increasingly many readings or by a word whose overlap tends to zero.

## What happens when the Gaussian resolution is changed

**PROVED.** Replace \(\sigma^2\) on one link by \(\tau>0\), retaining the same endpoint Wilson law and putting \(Z_\tau=W+\sqrt\tau G\). There is a sharp threshold for a nonnegative reading to give a positive semidefinite one-step insertion on the physical neutral space. All nonnegative bounded radial readings have this property precisely when \(\tau\ge1/(4\beta)\). This is a statement about quadratic forms of the marked transfer.

**PROVED.** In Haar coordinates, the kernel density marked by \(Z_{\tau,e}=z\) on that link is a positive scalar depending on \(z\), times the following factor, with the usual other electric bonds and magnetic halves:
\[
 e^{z\cdot x_e/(2\tau)}
     e^{(\beta-1/(4\tau))x_e\cdot y_e}
 e^{z\cdot y_e/(2\tau)}.                                                 \tag{8}
\]
It follows by expanding \(|z-(x_e+y_e)/2|^2\). If the middle coefficient is nonnegative, the middle convolution is positive semidefinite by GL3, including the constant kernel at zero. The factors at the two ends in (8) are identical multipliers. Integration against a nonnegative reading preserves positivity, also after restriction to the physical sector. This proof allows joint nonnegative readings on arbitrarily many links at or above the threshold.

**PROVED.** Below the threshold let \(\gamma=\beta-1/(4\tau)<0\). At \(z=0\) the marked convolution on \(e\) is the positive convolution at \(|\gamma|\) followed by the single-link sign flip. Choose a spatial elementary plaquette \(p\) containing \(e\). The trial vector \(v^{-1}w_p\) is gauge invariant and centre neutral. Removing the two magnetic multipliers in its quadratic form leaves \(w_p\), of pure fundamental spin on each of its four edges and constant in the other coordinates. The marked quadratic form is strictly negative because the factor on \(e\) is negative in that spin, and all other factors are positive. The density of this quadratic form is continuous in \(z\) by compactness of both slices. Integration over a small positive-radius ball about zero is therefore still negative. The indicator of the ball is an ordinary nonnegative radial observation in the original probability experiment.

**PROVED.** At the threshold, pin \(Z_e=0\) on a set \(S\) of edges of one time cut. A pin here means a joint Lebesgue **density** at zero. Formula (8) gives ordinary deletion of the electric factors on \(S\), times an explicit scalar per pin. The density is also the limit of ball probabilities divided by their Lebesgue volumes, by continuity at fixed cutoff. After removal of the everywhere positive magnetic halves, the cut has rank one in the neutral physical space if and only if the complementary spatial graph is a forest. Deleted electric factors integrate their link variables against Haar. On a forest the vertex gauges act transitively on all assignments, so the invariant part of the range consists of constants. If the complement has a simple cycle \(C\), its adjoint loop character is a nonconstant gauge- and centre-invariant function. It has pure spin one on every cycle edge, hence strictly positive electric eigenvalue. Along with constants it survives deletion. Magnetic multiplication is invertible at fixed cutoff and preserves rank. A spanning tree therefore gives an exact rank-one cut with \(m-(n^3-1)=2n^3+1\) pins. This is the minimum among exact zero pins of this type.

**PROVED.** This gives a direct test of the thermal bound with the same ordinary Wilson coupling in every sampled ensemble. For a spanning-tree complement \(S\), denote the preceding vector density at one specified cut in period \(j\) by \(d_j\). Denote the joint density at cuts separated by \(j\) in period \(2j\) by \(d_{2j}^{(2)}\). Use either the ordinary gauge-invariant transfer \(T\) or its neutral restriction on *both* periods. The latter periodic integral averages the spatial centre seam signs at the temporal closure. Use the transported endpoints in defining the reading across such a seam, or put the seam on an unobserved cut. With \(j\ge2\),
\[
       \frac{d_{2j}^{(2)}}{d_j^2}
            =\frac{(\operatorname{Tr}T^j)^2}{\operatorname{Tr}T^{2j}}.     \tag{9}
\]
Indeed replacing one transfer step by the pinned step inserts \(c\,|v\rangle\langle v|\) with the same scalar \(c>0\) in both experiments. The one-pin numerator before normalization is \(c\langle v,T^{j-1}v\rangle\). The two-pin numerator is its square by the rank-one identity. Both denominators are the unmodified partition functions. Formula (9) uses the established thermal doubling criterion of Theorem ZD-c and row 1218. The new representation has a sharp noise threshold and an exact minimum number of pins.

**OPEN.** Bounds (4)–(5) do not control (9). The minimum number of observations in the rank-one cut is extensive in the spatial volume, and (9) takes their joint density at a specified value. To prove the full thermal criterion one needs the log of (9) strictly below its threshold on the required physical shapes. The individual pin probabilities cancel algebraically and give no such upper bound.

## A fixed spatial patch, including its cycles

**PROVED.** Let \(n_j\) be even and tend to infinity. Take \(\beta_j\to\infty\) with \(\beta_j\le B\log n_j\), and any \(\delta_j\downarrow0\). On the vacuum cylinder let \(I\) be the edges of any fixed finite spatial patch embedded by translation. Write \(\mathcal B_I\) for *all* square-integrable observations of the four-component \(Z_e,\ e\in I\), at the critical bridge variance. Then
\[
 \lim_{j\to\infty}\,
 \sup_{\substack{f\perp1,\;\|f\|_\nu=1,\; f\ {\rm gauge\ invariant}\\
                  {\bf1}_{[1-\delta_j,1]}(P)f=f}}
 \ \sup_{\substack{b\in\mathcal B_I\\\|b\|_\eta\le1}}
      |\mathbb E[\overline{f(X)}b(Z_I)]|=0.                              \tag{10}
\]
An empty centered band contributes zero. The patch may contain elementary plaquettes and intersecting loops. The observations, their norms before normalization, and the states can all depend on the cutoff. The inputs for the weak-coupling comparison below are the open-box estimates of rows 1151 and 1231. [Wilson box comparison, (22b) and (24)](gap-solve5-astra62.md) · [Joint curl comparison, (1), (8) and (9)](gap-solve26-astra62.md)

**PROVED.** Average \(b\) over vertex gauges. This preserves its pairing and decreases its norm. Enclose \(I\) in a fixed rectangular box and fix a rooted tree of the lower spatial slice in that box. A gauge transformation \(g\) setting the tree links to one gives
\[
 D_e=\sqrt\beta\big((gX)_e/2+(gY)_e/2-1\big),\qquad e\in I,
\]
where \(1\) is the identity quaternion. Use temporal gauge on this step. In spacetime coordinates the upper edge has a temporal transport down at both ends. Thus \((gX)_e\) and \((gY)_e\) are based loop products at the lower root. The common root conjugation has no effect on the averaged observation. The conditional mean of the reading is \(a_\beta(D)\), where
\[
 b_\beta^*(u)=b({\bf1}+u/\sqrt\beta),\qquad
 a_\beta(d)=\mathbb E_G b_\beta^*(d+G/2).
\]
Here \(G\) has \(4|I|\) independent standard real coordinates. Multiplication of the noise by the endpoint gauges preserves this conditional Gaussian law.

**PROVED.** There are constants depending only on the patch such that
\[
 \big(\mathbb E |f(X)|^2{\bf1}_{|D|>H}\big)^{1/2}
     \le C_I(e^{-c_I H^2}+\sqrt{\delta_j}) \quad(H\ge1).                \tag{11}
\]
For the spatial loops of the lower box, express each as a product of finitely many conjugated unit plaquettes or their inverses. For instance, commute adjacent coordinate steps by unit squares to reduce a closed word to cancelling steps, in a fixed containing box. The sum of the chords of these plaquettes bounds the chord of the loop. Also \(|(gY)_e-(gX)_e|^2=2A_e\). Consequently \(|D|>H\) forces a member of a fixed finite collection of lower spatial or connecting electric plaquettes to satisfy \(\beta(1-w_p)>c_I H^2\). For an electric plaquette the kernel bound used in (5) is now \(C e^{-c_I H^2/2}\).

**PROVED.** For the spatial plaquette write \(E=\{\beta(1-w_p)>u\}\). On the gauge-invariant space use the vacuum-normalized transfer \(U\) in Haar coordinates. The trace of \(({\bf1}_E U^2{\bf1}_E)^l\), divided by \(\operatorname{Tr} U^{2l}\), is the Wilson probability that \(E\) holds on every other slice. The marked-plaquette estimate (9) of row 1155 gives a bound \(C^l e^{-cul}\) on this probability. It applies on rectangular periodic lattices. One may use a common coordinate of the marked spatial faces as transfer time, halve their couplings, then apply Schatten Hölder around that circle. The normalized electric factors decrease in operator order and each changed normalizer costs a fixed constant. At fixed spatial volume \((\operatorname{Tr}U^{2l})^{1/l}\to1\) by positive trace class and vacuum normalization. Taking \(l\)-th roots gives \(\|{\bf1}_E U^2{\bf1}_E\|\le C e^{-cu}\). Since \(U^2\succeq(1-\delta_j)^2{\bf1}_{[1-\delta_j,1]}(U)\), the probability under \(|f|^2\nu\) is at most \(Ce^{-cu}/(1-\delta_j)^2\). Summing over the fixed collection proves (11). The same estimate holds for the vacuum with \(\delta_j=0\). [Marked-face estimate, row 1155](gap-solve7-astra62.md)

**PROVED.** After smoothing, the local tests are precompact on each fixed ball. Indeed the vacuum density of \(D+G/2\) on \(\mathbb R^{4|I|}\) is at least \(c_I\exp[-2(|u|+H_0)^2]\), by restricting \(D\) to a ball of fixed radius \(H_0\) and positive probability from (11). The squared norm of \(b_\beta^*\) in this density is at most one. For \(|d|\le H+1\), Cauchy–Schwarz with that weight bounds both \(a_\beta(d)\) and its first derivatives by \(C_{I,H}\). The required integrals are bounded by a polynomial in \(|u|\) times \(\exp[-4|u-d|^2+2(|u|+H_0)^2]\), which is integrable uniformly on the given ball. Multiply \(a_\beta\) by a radial Lipschitz cutoff equal to one on \(|d|\le H\) and zero on \(|d|\ge H+1\). The resulting functions have a uniformly convergent subsequence for each fixed \(H\), with bounded Lipschitz, root-conjugation-invariant limit \(a_H\). Replacing the original observation in its pairing with \(f(X)\) by the clipped conditional mean costs at most the right side of (11). Indeed the error is \(\mathbb E[\bar f(X)(1-\chi_H(D))b(Z_I)]\). This truncation also covers observations concentrated on very unlikely values.

**PROVED.** For fixed \(H\) and any fixed list of integer time shifts, the first and second moments of the resulting \(a_H(D)\) readings converge to those of bounded local functions of three copies of the infinite unit-lattice Gaussian curl. Here is the use of the finite-window comparison. In the lower tree frame each relevant loop is a product of finitely many transported plaquettes. The error in replacing a product minus one by the sum of its factors minus one is bounded by the sum of pairwise products of their chords, by telescoping twice. The mean error after multiplying by \(\sqrt\beta\) is \(O_I(\beta^{-1/2})\), by the marked-face moment above and Cauchy–Schwarz. The real parts of the individual differences have the same bound. The remaining imaginary terms are fixed finite sums of based, transported spatial and electric curvatures, with signs and the factors \(1/2\) in \(D\).

**PROVED.** On a periodic cylinder of time length \(M\ge n\) tile by open four-dimensional boxes of side \(h=\lceil\beta^{1/16}\rceil\). Translation invariance permits averaging the test over its anchor. The fixed windows and paths miss the interiors for a fraction \(O_I(1/h+h/n)\) of anchors for each window. In a good interior box all tree-gauge link logarithms are at most \(h^{-7/2}\). The bounded-length transports may be omitted at mean cost \(O_I(h^{-7/2})\) on the rescaled curls. Row 1231, (8), bounds the sum of squared errors in replacing plaquette imaginary parts by their linear curls by \(C h^{-2}\sum_p(1-w_p)\). Thus the translated mean error on rescaled curvatures is \(O_I(h^{-1})\). The tests at distinct roots are separately conjugation invariant. Each can therefore use its own box frame. Bad boxes cost \(O_I(e^{-c\beta/h^8})\) in the translated bounded test, as in row 1151's (24).

**PROVED.** The completed array of linear curls in row 1151 has relative entropy at most \(C n^3 M\,\Delta_h\) against the product diluted open-box Gaussians, where \(\Delta_h=(\log\beta)(1/h+h/n)\). For fixed finitely many curvatures and bounded Lipschitz test, its translated average is \(C_{I,H}/\sqrt{n^3 M}\)-Lipschitz as a function of the reference normals. Indeed the fixed linear combinations have bounded sums of absolute coefficients, every shift preserves the counting norm, and the diluted curl projection has bounded operator norm. The entropy and Gaussian exponential-moment inequality in the proof of (24) costs \(C_{I,H}\sqrt{\Delta_h}\). The nested-projection coupling of row 1231, (1), changes open-box curls to the periodic exact curls at mean cost \(O_{I,H}(\sqrt{1/h+h/n})\), including the dilution and omitted faces. These arguments apply to a product of two clipped readings with possibly different roots, since it too is bounded Lipschitz. This verifies the extension to the finite based loops used here. The estimates are uniform in \(M\). First let \(M\to\infty\) at fixed \(n,\beta\), using the simple transfer vacuum, and then let \(j\to\infty\). The finite Gaussian covariances converge by Fourier sums to the infinite lattice projection. Its symbol is bounded and continuous except at zero, with the zero-frequency value set to zero. This also justifies the iterated time-integral and spatial-sum limit. The local Wilson box method used here is based on Sourav Chatterjee's weak-coupling work. The free exact-curl symbol is due here to Ethan Sussman and Levent Alpoge, with Claude and Codex as authors of their text. [Outline, 1733–1762](https://github.com/ethanwsussman/Yang--Mills-LLM-experiment/blob/31a47c543775/YM4_sketch_500.tex#L1733-L1762)

**PROVED.** In that Gaussian law cross covariances of two fixed windows tend to zero as their time separation tends to infinity. Each covariance is a finite sum of Fourier coefficients of the bounded projection symbol. Approximation in \(L^1\) by trigonometric polynomials proves this decay. Joint Gaussian characteristic functions thus factor in the limit. The covariance of the bounded continuous clipped readings tends to zero, including for complex readings with conjugation in the first factor. Hence the variance of the average of \(m_0\) successive centered readings tends to zero as \(m_0\to\infty\), by expanding the square and taking the Cesàro mean of the covariances.

**PROVED.** Return to a subsequence of potential violations of (10) and fix \(H\). Use the compactness above to obtain the clipped limit \(a_H\). For fixed \(m_0\) replace the pairing of \(f(X_0)\) with the centered clipped reading at step zero by its pairing with the average of the next \(m_0\) centered, translated readings. At shift \(s\) the error tends to zero with \(j\) by stationarity and
\[
 \mathbb E|f(X_s)-f(X_0)|^2
     =2\langle f,(I-P^s)f\rangle_\nu\le2s\delta_j .
\]
The clipped functions are bounded at fixed \(H\). Cauchy–Schwarz bounds the last pairing by the square root of the average's variance, whose limit was just computed for each fixed \(m_0\). Now let \(m_0\to\infty\). The original limsup is at most \(C_I e^{-c_I H^2}\) by (11). This bound holds for each \(H\), even though the convergent subsequence and its clipped limit can depend on \(H\). Sending \(H\to\infty\) rules out the violation. This completes (10). The order of limits makes no assertion of Gaussian behaviour at positive physical time or distance.

**OPEN.** Equation (10) removes an entire normalized microscopic observation space at a time, including arbitrary cutoff-dependent tests of local cycles. A fixed physical spatial cube has an increasing number of these patches. Projection onto each of their individual observation spaces does not estimate projection onto functions of their joint readings. In (9) the cut uses precisely such a joint reading.

## Trying to estimate the thermal ratio on the original Wilson measure

**GUIDE.** Row 1151, (26), already identifies a one-period squared probability divided by a two-period joint probability with the purity, using its empty electric diagram. I use that underlying identity. Here deletion is realized by positive functions on a single observed layer. One can then calculate the cost of a second-moment estimate in the actual Wilson measure. [Empty-diagram identity, row 1151](gap-solve5-astra62.md)

**PROVED.** A change of one electric coupling from \(\beta\) to \(\beta-\kappa\), with \(\kappa>0\), can be implemented by one bounded nonnegative radial mark at variance \(\tau<1/(4\kappa)\). In fact for \(t=2\kappa/(1-4\kappa\tau)\),
\[
 \mathbb E[e^{-t|Z_{\tau,e}|^2}\mid X,Y]
       =(1+2t\tau)^{-2}\exp[-\kappa(1+X_e\cdot Y_e)].                  \tag{12}
\]
At equality in the variance threshold the zero density gives the same change. Above that variance even signed, square-integrable single-link radial marks cannot implement this change exactly up to a nonzero constant. This includes complete deletion (\(\kappa=\beta\)) and reversal (\(\kappa=2\beta\)).

**PROVED.** For the last assertion let \(b\) be the mark on \(\mathbb R^4\) and \(h(w)=\int b(z)\phi_\tau(z-w)\,dz\), where \(\phi_\tau\) is the centered four-dimensional Gaussian density. The actual one-link marginal of \(Z_\tau\) has density at least \((2\pi\tau)^{-2}\exp[-(|z|+1)^2/(2\tau)]\) since \(|W_e|\le1\). Square integrability in this marginal makes \(h(s e_1)\) entire for \(s\in\mathbb C\), by Cauchy–Schwarz with a Gaussian tail for \(s\) in any compact set. A radial \(b\) gives radial \(h\). The target multiplier on every possible chord midpoint is \(c\,e^{-2\kappa |w|^2}\), with \(c\ne0\). The same necessity holds if the transfer identity is only required on the neutral physical space. After removal of the invertible magnetic halves, test the character in each spin of a fixed elementary spatial plaquette containing \(e\). Other bond multipliers are positive and cancel. This determines every one-link central convolution coefficient, hence its kernel by character completeness. The resulting identity on \(0<|w|<1\) extends in \(s\) by analyticity. But
\[
 e^{-y^2/(2\tau)}h(iy e_1)
      =\int b(z)\phi_\tau(z)e^{iy z_1/\tau}\,dz\longrightarrow0 .
\]
The integrand without the phase is in \(L^1\). Approximation by compactly supported step functions proves the limit. For the desired multiplier the left side is \(c e^{(2\kappa-1/(2\tau))y^2}\). This also rules out an \(L^2\) mark at equality, where the point density works. Thus the cyclic recovery above can encounter an unbounded inverse even at a fixed finite cube.

**PROVED.** The exact ratio (9) can be very ill conditioned for reasons unrelated to the existence of a physical gap. On an even cube choose a vertex sign \(s_{x,y,z}=t_x(-1)^{y+z}\), where \(t_x=-1\) at \(x=0\) and \(+1\) elsewhere. Let \(S\) consist of bonds whose two vertex signs differ. It contains all transverse bonds and two cross sections of longitudinal bonds, so \(k=|S|=2n^3+2n^2\). Its complement is a union of longitudinal paths and isolated vertices. In the true periodic Wilson law put
\[
 L=\exp[-\beta\textstyle\sum_{e\in S} w_e]
\]
at one specified cut, where \(w_e\) is the half-trace of its temporal plaquette. This is the deletion insertion with deterministic scalar chosen in the \(e^{\beta w_e}\) convention. The rank-one calculation of (9) applies to the one-period mean of \(L\) and the two-period mean of its product at opposite cuts.

**PROVED.** For every configuration of *all spatial links*, \(\mathbb E[L^2\mid{\rm spatial\ history}]=1\) exactly. Multiply the temporal vertex links at the specified cut by \(s_{x,y,z}\). Product Haar is preserved and precisely the selected terms in the electric exponent reverse sign. No other temporal layer changes. Thus \(L^2\) is the conditional likelihood ratio of this invertible change of variables. It also works in each fixed temporal closure by a spatial centre flip. In contrast,
\[
 e^{-\beta k}\le\mathbb E L
       \le e^{-\beta k} z_\beta^{-k},\qquad
 \log\frac{\mathbb E L^2}{(\mathbb E L)^2}
       =2\beta k+O(k\log(1+\beta)).                                      \tag{13}
\]
The lower bound is pointwise. For the upper bound use
\(L=e^{-\beta k}\exp(\beta\sum_{e\in S} A_e)\).
In the mass-one convention deleting \(S\) costs \(z_\beta^{-k}\) and replaces those convolutions by their constant projections. The resulting positive operator is below the original transfer, also after the magnetic sandwich. Trace it against the remaining positive power in the ordinary or neutral sector. This proves (13) at every period at least two. The relative second moment of a single deletion therefore grows exponentially in \(\beta n^3\). An estimator obtained by adding independent observation noise as in (12) and normalizing its conditional mean to \(L\) has at least this relative second moment by conditional Jensen. Formula (13) is an analytic result for the original measure. It does not give the connected ratio in (9).

**PROVED.** Integrating the temporal links exactly removes one part of this large fluctuation. Set \(r=m-k\), \(a(g)=1-\operatorname{Re} g\), and
\[
 I_\beta(X,Y)=\int\exp[-\beta\sum_{e=xy}a(X_e g_yY_e^{-1}g_x^{-1})]\prod_x dg_x .
\]
Here the two slice fields are in arbitrary vertex frames. Given them, the normalized conditional deletion amplitude is
\[
 H(X,Y)=\mathbb E[L\mid X,Y]
     = e^{-\beta k}\,\frac{z_\beta^{\,r}}{I_\beta(X,Y)}.                 \tag{14}
\]
To see this, integrate the retained electric factors along their forest from its leaves. Every retained edge contributes \(e^\beta z_\beta\) in the positive-exponent convention. Divide by \(e^{\beta m}I_\beta\). In a twisted period use the appropriately transported field \(Y\) at the closure. One has \(0<H\le1\) from conditional Cauchy–Schwarz and the exact second moment. Since temporal layers are conditionally independent given the spatial history, (14) can be substituted at both deleted cuts in (9). This leaves precisely a correlation of *scalar* orbit integrals at separation \(j\). The local independent sign change already accounts for the temporal-colour likelihood fluctuation.

**OPEN.** A pointwise typical approximation to \(\log I_\beta\) with an error \(O(n^3)\), as in row 1283, (38), cannot determine the order-one difference of the log averages of (14) in one and two periods. Even discarding most configurations under the original law would require a bound under the deletion tilt. Neither (10) nor the exact conditional second moment supplies that bound.

## A sharp moment obstruction after integrating the temporal gauge

**PROVED (15).** Take an even spatial torus of side \(n\), a time circle of length \(N=n=2j\), and the ordinary periodic Wilson measure. Put \(m=3n^3\). At a cut \(t\) let \(B_t=I_\beta(X_t,X_{t+1})^{-1}\), with \(I_\beta\) as in (14), in deficit normalization so that \(I_\beta\le1\). Let \(B\) denote either \(B_0\) or \(B_0B_j\), and let \(q=1\) or \(2\) respectively. Then
\[
  0\le \log\mathbb E B^p\le -pq m\log z_\beta
                  \qquad(0\le p\le1).
\]
For each fixed \(p>1\) there are \(c_p,C_p>0\) such that for all sufficiently large even \(n\) and sufficiently large \(\beta\),
\[
 c_p\beta n^3\ \le\
 \log \frac{\mathbb E B^p}{(\mathbb E B)^p}
 \ \le\ C_p\beta n^3.                                           \tag{15}
\]
The same assertions hold for the measure representing the center-neutral trace, taking the center-twist seam away from the listed cuts. Thus the distinction between the first moment and every fixed higher moment survives exact integration over the temporal gauge variables. Multiplying each \(B_t\) by the deterministic factor in (14) has no effect on the normalized moment in (15).

**PROVED (the first-moment bound).** Write \(T=M_v C_\beta M_v\) for the mass-one transfer on a slice and \(T_0=|v\rangle\langle v|\) for the transfer in which all cut bonds have been replaced by Haar projection. The Fourier eigenvalues of the one-link mass-one convolution are positive, with value one on constants. Hence \(0\le T_0\le T\), also after restriction to the gauge-invariant and center-neutral spaces. Multiplication of the orbit kernel by \(B_t\) inserts \(z_\beta^{-m} T_0\). At one cut, sandwich the operator inequality by \(T^{(N-1)/2}\) and take a trace. At two opposite cuts, \(0\le A=T^{(j-1)/2}T_0T^{(j-1)/2}\le T^j\) gives \(\operatorname{Tr} A^2\le\operatorname{Tr}T^{2j}\) by eigenvalue monotonicity. This proves the bound for \(p=1\). Concavity gives the bound below one. For every cut \(1\le B_t\le e^{2\beta m}\), which gives the upper bound above one. Here \(-\log z_\beta=O(\log(1+\beta))\) as \(\beta\to\infty\).

**PROVED (an orbit-distance lower bound).** Use the unit quaternion realization of \(SU(2)\) and three orthogonal imaginary units \(a_i\). On a spatial box of \(b^3\) vertices set \(X_{z,i}=1,\ Y_{z,i}=Y_i=\exp(\epsilon a_i)\). Uniformly over all vertex gauges \(g_z\),
\[
 \sum_{(z,z+\hat i)\ {\rm internal}}
       \tfrac12|g_{z+\hat i}-g_zY_i|^2
       \ \ge\ \sin^2\epsilon\,b^3-Cb^2.                         \tag{16}
\]
Extend \(g\) by zero. The quadratic form on the full lattice has Fourier symbol with lowest eigenvalue bounded below by
\[
  3-\cos\epsilon\sum_i\cos k_i-
             \sin\epsilon\sqrt{\sum_i\sin^2 k_i}
   \ \ge\ 3-\sqrt{9-6\sin^2\epsilon}\ \ge\ \sin^2\epsilon
       \qquad (0<\epsilon<\pi/2).
\]
Indeed the three right multiplications by \(a_i\) are skew orthogonal and anticommute. After complexification the square of the corresponding Hermitian sine term is \(\sum_i\sin^2 k_i\) times the identity. Cauchy–Schwarz and \((\sum_i\cos k_i)^2\le3\sum_i\cos^2 k_i\) give the displayed bound. The zero extension adds only \(O(b^2)\) links of energy \(1/2\). Conversely the actual temporal links \(g_z=\exp(z_1\epsilon a_1)\) have zero deficit in direction one and \(1-\cos\epsilon\) per edge in each other direction. Thus crossing the stated pair of slices in the Wilson action costs at most \(2(1-\cos\epsilon)b^3+O(b^2)\). The leading coefficients in these two estimates agree at order \(\epsilon^2\).

**PROVED (a localized Wilson history).** Let \(s=\lceil1/\epsilon\rceil\). In a spacetime box with \(b^3\) spatial vertices and times \(0,\ldots,s+1\), use the preceding pair at times \(0,1\). At times \(t=1,\ldots,s+1\), use the spatial connections
\[
  Y_i(t)=\exp\big(\epsilon(s+1-t)a_i/s\big).
\]
Use the helical temporal links just constructed at the cut \(0,1\), and identity temporal links above it. Set every edge tangent to the boundary of the spacetime box to the identity. The time faces already have identity tangential links. The lateral adjustment affects \(O(sb^2)\) plaquettes, of deficit at most two each. Each ramp step has electric cost \(O((\epsilon/s)^2)\) per site. For distinct quaternionic axes the spatial commutator at angle \(\alpha\) has deficit \(2\sin^4\alpha\), by direct multiplication. Thus the total dimensionless action of this template is at most
\[
 [2(1-\cos\epsilon)+C(\epsilon^2/s+s\epsilon^4)]b^3+Csb^2.     \tag{17}
\]
On the interior spatial cube (16) still gives a lower bound \(\sin^2\epsilon\,b^3-Cb^2\) on crossing the first cut, since a fixed number of boundary layers costs \(O(b^2)\).

**PROVED (inserting the history without a volume-dependent normalization).** Tile with \(\lfloor n/b\rfloor^3\) disjoint spatial vertex cubes in the same slab. Write \(V_b=b^3\lfloor n/b\rfloor^3\ge n^3/8\) for \(n\ge2b\), and take \(j>s+2\). In each spacetime box choose a spanning tree extending a tree of the connected boundary graph, rooted on the boundary. First put the template in tree gauge. Its gauge matrices on the boundary are identities, so all boundary tangents and all tree links of this transformed template are identities. For a given Wilson configuration, fix tree gauge using its actual tree links. On the complementary edges multiply the true tree-gauge links on the left by the tree-gauge template links, then undo the true gauge transformation. This map keeps every tree link and every boundary tangent fixed. Conditional on the tree links it is a product of Haar-preserving translations on independent coordinates of the reference product Haar measure. It is therefore a Haar-preserving bijection. A plaquette crossing a box boundary can use only boundary-tangent edges of that box. Its action stays fixed under this map.

**PROVED (typical input boxes).** Fix \(b,s\) and a chord tolerance \(\eta>0\). A good input box has each of its tree-gauge links within \(\eta\) of the identity. Each such link is a loop holonomy given by its two tree paths and the link itself. Each of these finitely many loops bounds a fixed word of conjugates of elementary plaquettes and their inverses in the contractible box. The triangle inequality in the bi-invariant chord norm, Cauchy–Schwarz and \(|1-U|^2=2(1-\operatorname{Re}U)\) reduce its mean squared distance from one to \(C_{b,s}/\beta\) by the periodic marked-plaquette bound of row 1155, (9) there. Thus the probability that a specified box is bad is at most \(C_{b,s,\eta}/\beta\). For fixed \(\eta'>0\) the probability that the fraction of bad boxes is at most \(\eta'\) is at least \(1/2\) once \(\beta\) is sufficiently large, by Markov's inequality. No independence of the boxes enters. On good boxes the image configuration, after fixed and true tree gauges are undone as appropriate, is within \(\eta\) per link of the template in a common frame. Both the plaquette action and the infimum over temporal gauges of a regional cut deficit are invariant under changes of the spatial frames. A plaquette varies by at most \(4\eta\) and a cut summand comparing two spatial links by at most \(2\eta\), uniformly in the temporal gauges.

**PROVED (cost and payoff).** Let \(U'\) be the image, \(\mathscr S\) the sum of all spacetime plaquette deficits without \(\beta\), and \(d'\) the minimum gauge-aligned deficit on the distinguished first cut of \(U'\). On the preceding event, dropping nonnegative terms outside the good cores and minimizing separately in each core gives
\[
 d'\ \ge\ [(1-\eta')\sin^2\epsilon-C/b-C\eta]V_b.
\]
Subtracting the nonnegative initial box action on good boxes, bounding bad-box action by \(Cs b^3\), and using (17) gives
\[
 \mathscr S(U')-\mathscr S(U)\ \le\
 [2(1-\cos\epsilon)+C(\epsilon^2/s+s\epsilon^4+s/b+s\eta+s\eta')]V_b .
\]
For a fixed \(p>1\), the surplus
\[
 p\sin^2\epsilon-2(1-\cos\epsilon)
   =(1-\cos\epsilon)[p(1+\cos\epsilon)-2]
\]
is asymptotic to \((p-1)\epsilon^2\). The ramp cost is \(O(\epsilon^3)\). Choose \(\epsilon\) small enough, then \(b\) large enough, then \(\eta,\eta'\) small enough that \(p d'-(\mathscr S(U')-\mathscr S(U))\ge c'_p n^3\). These choices precede both lattice limits. In deficit normalization \(I_\beta(X',Y')^{-p}\ge e^{p\beta d'}\). The Haar change of variables in the full Wilson integral now gives \(\mathbb E B_0^p\ge\tfrac12e^{c'_p\beta n^3}\). For two cuts use \(B_j^p\ge1\). For the neutral trace, place the center-twist closure outside the slab and away from both cuts. Its positive path-integral representation is the sum over the eight flat twists with nonnegative weights. Each twisted partition function is at most the ordinary one by the unitary trace bound, so the ordinary component has probability at least \(1/8\). The lower estimate persists. Finally \(p\log\mathbb E B=O_p(n^3\log(1+\beta))\), which proves (15).

**PROVED (approach to the threshold).** For \(1<p\le2\) one can take the lower rate in (15) to be \(c(p-1)^3\) with absolute \(c>0\), allowing the lower cutoffs on \(n,\beta\) to depend on \(p\). In fact take \(\epsilon=c_0(p-1)\) for a sufficiently small absolute \(c_0\). The positive term then dominates both the ramp error \(C\epsilon^3\) and the \(O(\epsilon^4)\) error in the cut surplus. Choose the remaining box and chart tolerances to lose at most half that margin, as above. This order of limits gives no uniform estimate at \(p=1\).

## Controlling the fully deleted cut from its two open boundaries

**PROVED (curvature controls spatial orbit distance).** Write \(v_3=n^3\) and \(S_{\rm mag}(X)=\sum_{p\ {\rm spatial}}(1-w_p(X))\). For two arbitrary \(SU(2)\) connections on the spatial torus and every integer \(2\le b\le n/8\),
\[
 d(X,Y):=\min_g D_{XY}(g)\le
 C\{v_3/b^2+b^2[S_{\rm mag}(X)+S_{\rm mag}(Y)]\}.                      \tag{18}
\]
Both fields may have nontrivial holonomies. The alignment uses unit quaternions on the whole torus. The axial-path plaquette identity is also used in row 1151 for thin rectangles, and in row 1283 for transported colours. Here overlapping paths are needed to give the \(b^{-2}\) term. [Thin-strip estimates, §3](gap-solve5-astra62.md) · [Transported fields, (19)](gap-solve32-astra62.md)

**PROVED (construction of the gauges).** On an edge \(e=zz'\) put \(O_e q=X_e qY_e^{-1}\), transporting from \(z'\) to \(z\) in \(\mathbb R^4\). Then \(D_{XY}(g)=\frac12\sum_e|g_z-O_e g_{z'}|^2\). Use a nonnegative scalar bump \(\phi\) of squared counting norm one supported in the cube \([-b,b]^3\), with
\(\sum_r|\phi(r+\hat i)-\phi(r)|^2\le C/b^2\). For example take the normalized product of the three tents \((1-|r_i|/b)_+\). For every vertex \(\alpha\) take an independent standard Gaussian quaternion \(\xi_\alpha\). Let \(P_{\alpha,z}\) transport from \(\alpha\) to \(z\) along the ordered coordinate path, using the local signed lifts within distance \(b+1\) of any contributing offset. Define
\[
 H_z=\sum_\alpha\phi(z-\alpha)P_{\alpha,z}\xi_\alpha,\qquad
 g_z=H_z/|H_z|.
\]
Each \(H_z\) is standard Gaussian in four dimensions. The event that any \(H_z=0\) is null. For the jointly Gaussian \(U=H_z-O_eH_{z'}\), regress \(U=A H_z+\zeta\), with centered \(\zeta\) independent of \(H_z\). The inequality for normalizing two nonzero vectors gives
\[
 \mathbb E|g_z-O_e g_{z'}|^2
 \le4\mathbb E\frac{|U|^2}{|H_z|^2}
 \le 2\mathbb E|U|^2 .
\]
Indeed the two terms in the middle expectation are \(\|A\|_{\rm HS}^2/4\) and \(\mathbb E|\zeta|^2/2\). The latter identity follows by a one-variable radial Gaussian integral. The regression uses only orthogonality and joint Gaussianity and is valid for singular covariances of the pair.

**PROVED (sum of the path errors).** In the Gaussian energy, independence gives the sum over \(\alpha\) of squared Hilbert–Schmidt norms of the coefficient differences. Split each into the scalar bump difference and \(\phi(z'-\alpha)(P_{\alpha,z}-O_eP_{\alpha,z'})\). The scalar contribution over all edges is at most \(Cv_3/b^2\). The path discrepancy is a loop formed from the two ordered paths and a single edge. Sliding that edge through the later coordinate steps cancels the paths with at most \(C b\) unit plaquettes. The square of the discrepancy of the orthogonal transports is at most \(Cb\) times the sum of the two connections' plaquette deficits on this strip. This follows by telescoping in the bi-invariant chord norm, first for each quaternionic transport, then for its left and right actions on \(\mathbb R^4\). For a fixed offset \(z'-\alpha\) and direction \(i\), translation over \(z\) counts at most \(Cb\) translates of plaquette sums, with multiplicity. The squared bump weights sum to one over all offsets. Hence the remaining sum is bounded by \(Cb^2(S_{\rm mag}(X)+S_{\rm mag}(Y))\). The infimum is bounded by the expectation of this trial energy. This proves (18) by Gaussian integration, without generating samples.

**PROVED (a spacetime collar estimate).** At a deleted cut let \(S_{\rm col}\) be the sum of plaquette deficits in the first \(b+1\) intact layers on *each* side, including their spatial plaquettes. Take the slab lengths larger than \(2b+3\). For any configuration of actual interior links,
\[
             d(X,Y)\le C(v_3/b^2+bS_{\rm col}).                         \tag{19}
\]
The square root of \(2d\) is the product chord distance on spatial configurations minimized over the compact group of isometric vertex gauges. It satisfies the triangle inequality on orbits. At depths \(t=1,\ldots,b\) on either side, use the genuine temporal parallel transports between that end and the cut. In their common frame a single time difference has squared chord cost twice the sum of that layer's electric deficits. Telescoping over \(t\) steps and Cauchy–Schwarz bound \(d\) between the end and the depth-\(t\) slice by \(b S_{\rm col}\). On each side choose a depth with magnetic cost at most \(S_{\rm col}/b\). Apply (18) to the two chosen slices, then use the orbit triangle inequality and the three-term squared bound. The argument also applies after a flat centre flip on one side, by flipping its entire collar. Every individual plaquette deficit there is preserved.

**PROVED (open-cylinder exponential moment).** Put \(Q=B\,P/\mathbb E_P B\), where \(P\) here denotes the periodic probability measure in (15). Quantities depending only on the spatial fields have under \(Q\) the law of the open slab obtained by deleting the designated cut, or of two independent open slabs for two opposite deletions. Indeed the factors \(I_\beta\) cancel exactly. Restore the undeleted temporal links by their ordinary conditional laws. The resulting open slabs have the original Wilson weights at every intact plaquette, including the full spatial weights at each boundary. This last detail follows either by multiplying all magnetic half weights, including those in \(T_0\), or by deleting just the selected electric terms in the original path integral. For the neutral mixture a flat twist may be placed on a deleted seam. Its choice then leaves the open-slab weight unchanged. The spatial observable \(B\) evaluated *under* this law still uses the correctly twisted fields if the twist is on its own cut.

**PROVED.** For either one or two cuts, the union of the adjacent collars in (19) has
\[
       \mathbb E_Q \exp(c\beta S_{\rm col,tot})\le \exp(C b v_3),\qquad
       \mathbb E_Q S_{\rm col,tot}\le C b v_3/\beta.                    \tag{20}
\]
Take collars disjoint within each slab. This is the marked-plaquette proof on the open cylinder given by row 1151, (6), there for boundary faces. Its argument works also for the interior collar. Every marked face has a spatial direction. For faces assigned to a common direction, rotate it into the transfer direction. Homogeneity around this spatial circle, including both free walls, gives identical unmarked layers. Halving the marked electric couplings decreases each mass-normalized layer in positive-operator order, at scalar cost at most \(C\) per face. Schatten Hölder around the circle and eigenvalue monotonicity give the unmarked partition function times this total scalar cost. Apply ordinary Hölder to the three groups, absorbing the fixed exponent in \(c>0\). There are at most \(C b v_3\) faces, and Jensen gives the second bound. The same proof at a boundary, applied to a *single* spatial face, costs an absolute constant, hence \(\mathbb E_Q S_{\rm mag}(\text{one end})\le C v_3/\beta\). [Open-boundary estimate and rotated transfer proof, row 1151](gap-solve5-astra62.md)

**PROVED (the critical tilt).** Uniformly at \(\beta\ge 2\) and \(n\ge 16\lceil\beta^{1/4}\rceil\), the ordinary and neutral measures of (15) obey
\[
 \begin{split}
 D(Q\Vert P)&\le \mathbb E_Q\log B\le C v_3\sqrt{\beta}
                                      +C v_3\log(1+\beta),\\
 D(P\Vert Q)&\le \log\mathbb E_P B\le C v_3\log(1+\beta).
 \end{split}                                                            \tag{21}
\]
In this display the measures may be taken on spatial histories and the twist. The assertions are unchanged by adding intact temporal links by the same conditional rule. Row 1283, (38), gives the deterministic upper bound \(-\log I_\beta\le\beta d+C v_3\log(1+\beta)\) for every pair of fields. To apply it under the fully deleted tilt, take \(b=\lceil\beta^{1/4}\rceil\) in (18) and use the single-end first moment following (20). This yields \(\mathbb E_Q d\le C v_3/\sqrt\beta\) at each deleted cut. Finally \(B\ge1\) and \(dQ/dP=B/\mathbb E_P B\) give the two relative entropy bounds. [Uniform orbit-volume bound, (38)](gap-solve32-astra62.md)

**PROVED (cubic onset of the higher moments).** For some absolute \(h_0,c,C>0\), for every fixed \(0<h\le h_0\) one has
\[
 c h^3
 \ \le\ \liminf_{n,\beta\to\infty}
  \frac{1}{\beta v_3}\log\frac{\mathbb E_P B^{1+h}}{(\mathbb E_P B)^{1+h}}
 \ \le\ \limsup_{n,\beta\to\infty}
  \frac{1}{\beta v_3}\log\frac{\mathbb E_P B^{1+h}}{(\mathbb E_P B)^{1+h}}
 \ \le\ C h^3.                                                          \tag{22}
\]
The limits are over the even cubes and periods of (15), with one or both cuts and either sector there. The lower bound is the construction after (17). For the upper bound write the normalized moment as \(\mathbb E_Q B^h/(\mathbb E_P B)^h\). Apply the deterministic upper bound of (38) of row 1283 at each cut, followed by (19). For any admissible \(b\) this gives
\[
 h\log B\le C h v_3\log(1+\beta)+ C\beta h v_3/b^2+
                                      C\beta h b S_{\rm col,tot}.
\]
Choose \(b=\lfloor c_0/h\rfloor\), with \(c_0\) small enough for (20) and \(h_0\) small enough that \(b\ge2\) and \(b\ge c_0/(2h)\). Once \(n\) is large at fixed \(h\) the collars fit. The log expectation is at most \(C h v_3\log(1+\beta)+C\beta h^3v_3+C v_3/h\). Division by \(\beta v_3\) and passage to the stated limits prove (22). Equations (18)–(22) give estimates in the exactly deleted ensemble, where (20) applies to the two exposed boundaries.

**PROVED (a better first derivative at the deleted boundary).** There is a further gain in (21) which uses the Wilson boundary law. For \(n\ge 16\lceil\beta^{1/3}\rceil\) one has
\[
          \mathbb E_Q\log B\le C v_3[\beta^{1/3}+\log(1+\beta)].          \tag{23}
\]
In the two ordered paths in the proof of (18), sliding the extra coordinate step through each later straight segment sweeps one rectangle of width one. There are at most two such rectangles in three dimensions, of lengths at most \(b+1\). Opposite signed steps and inverse orientations only conjugate or invert the corresponding factors. The squared norm of the transport discrepancy is therefore bounded by \(C\) times the sum of these rectangles' deficits in the two individual spatial fields. For either end of an open Wilson slab, row 1151, (4), gives \(\mathbb E(1-w_{1\times l})\le C l/\beta\) for \(l<n\) by the charged-transfer reflection-positivity argument for rectangles due to Bachas. This estimate remains true for a flat twist because each rectangle is contractible. Use it **before** bounding the strip by its constituent plaquettes in the Gaussian trial. The bump energy costs \(C v_3/b^2\) and the transport part now costs \(C v_3 b/\beta\). Choosing \(b=\lceil\beta^{1/3}\rceil\) gives \(\mathbb E_Q d\le C v_3\beta^{-2/3}\). Apply (38) of row 1283 as in (21). The proof needs only the one-end marginals and works also when the two ends belong to independent slabs. [Boundary rectangle bound, row 1151](gap-solve5-astra62.md)

**PROVED (relative truncation at the first moment).** For sufficiently large \(\beta\) and slab sizes exceeding \(C\beta^{1/4}\), there is an absolute \(K\) such that
\[
 \frac{\mathbb E_P[B\,{\bf1}_{\log B>K\sqrt{\beta}\,v_3}]}
      {\mathbb E_P B}
        \le \exp(-c\beta^{1/4}v_3).                                     \tag{24}
\]
Take \(h=\beta^{-1/4}\) and \(b=\lfloor c_0/h\rfloor\) in the *finite-volume* upper estimate before (22). It gives \(\log\mathbb E_Q e^{h\log B}\le C\beta^{1/4}v_3+C h v_3\log(1+\beta)\). Markov's exponential inequality gives (24). For the period \(j\) with one cut and the period \(2j\) with two opposite cuts the proof uses the same local estimates and only requires the indicated collar sizes. Thus replacing each \(B_t\) in (9), (14) by the bounded mark \(\min(B_t,\exp(K\sqrt\beta\,v_3))\) changes the log ratio by \(O(e^{-c\beta^{1/4}v_3})\). If clipping alters a product, its positive factors imply that the original product exceeds the cutoff. The relative loss is bounded by (24) before taking either logarithm. This controls the cutoff error even where the rank-one events in (9) have very small probabilities.

**PROVED (a smaller truncation for an order-one question).** Given any positive \(A_\beta\to\infty\), (23) and ordinary Markov also allow a cap \(\exp(A_\beta v_3[\beta^{1/3}+\log(1+\beta)])\) in the previous log ratio, with error \(O(1/A_\beta)\) when its spatial size condition holds. Both truncations control relative first moments of the ordinary ensemble by estimating tails under the *deleted* ensemble. They leave a two-period expectation of two bounded but collective spatial observables to evaluate.

## Can the first moment be reached by positive interpolation after gauge averaging?

**GUIDE.** Let \(\mu\) be the joint law of the ordered ends \((X,Y)\) of one exactly opened slab of length \(j-1\), including the two magnetic end weights. Two opened slabs have law \(\mu\otimes\mu\). For the ordinary trace, use \(K=I_\beta\). For the neutral trace one may first average \(I_\beta(X,sY)\) over the eight flat centre signs in \(s\) to obtain \(K\). The latter choice inserts the centre projection at each sewing, which is harmless since it commutes with the intervening transfer and is idempotent. With independent \((X_i,Y_i)\sim\mu\), define
\[
 J(u)=2\log\mathbb E_\mu K(X,Y)^u-
       \log\mathbb E_{\mu\otimes\mu}
          [K(X_1,Y_2)^u K(X_2,Y_1)^u],\qquad 0\le u\le1.                \tag{25}
\]
All these finite-volume integrals exist and are positive. The endpoints give \(J(0)=0\) and \(J(1)=\log[(\operatorname{Tr}T^j)^2/\operatorname{Tr}T^{2j}]\) by sewing the same slabs in the two possible ways. For neutral sewing, the open-slab law can be taken from the ordinary cylinder, with the projections made on its seams.

**PROVED.** Equations (18) and (23) apply to both kinds of pair in (25), with the same fixed end marginals. They give \(|J(u)|\le C u v_3[\beta^{1/3}+\log(1+\beta)]\) when \(n\ge16\lceil\beta^{1/3}\rceil\), by Jensen and \(K\le1\). For the averaged kernel use convexity of \(-\log\) and apply the estimate separately at every flat twist. At the true endpoint the required bound is of order one. I test the possible improvement by operator interpolation in \(u\).

**PROVED (loss of positivity at every finite coupling).** On any fixed spatial cube \(n\ge4\), for every \(\beta>0\), the kernel \(K(X,Y)^u\) fails to be positive semidefinite for every positive irrational \(u\). It also fails for all sufficiently small positive \(u\), including rational \(u\), on an interval that can depend on \(n,\beta\). This applies to both choices of \(K\) in (25). For the neutral choice the power is taken *after* centre averaging. A positive magnetic sandwich preserves the failure since its multiplication operator has a bounded inverse at fixed cutoff. In particular the integrals in (25) cannot be controlled along a real interval by treating these particular fractional powers as positive transfer operators.

**PROVED (real and complex diagonal).** Write a spatial configuration as a real vector of \(m\) four-component link quaternions. Let \(\Gamma\) be the compact group of vertex gauge rotations, enlarged by flat sign flips for the neutral choice. It acts by real orthogonal matrices on these \(4m\) coordinates. The kernel is \(K(x,y)=e^{-\beta m}\int_\Gamma e^{\beta x\cdot \gamma y}\,d\gamma\). Vary just one link from the identity as \(U(t)=\cos t+a_1\sin t\), all other links being the identity, to get \(x(t)\). The function \(K(t,s)=K(x(t),x(s))\) extends to an entire function of the two complex parameters by the bilinear dot product. In particular
\[
 K(t,\bar t)=e^{-\beta m}\sum_{\ell\ge0}
    \frac{\beta^\ell}{\ell!}\|\operatorname{Proj}_{\Gamma}x(t)^{\otimes\ell}\|^2
 \ \ge e^{-\beta m}.                                                     \tag{26}
\]
Termwise integration is justified by the exponential series on compact parameter sets. Averaging tensor powers of \(\gamma\) projects orthogonally onto their invariant tensors.

**PROVED (an off-diagonal zero).** There is a nonconstant entire function \(F\) with \(K(t,0)=F(\cos t)\) and
\[
              |F(c)|\le C_{n,\beta}\exp(C_\beta\sqrt{1+|c|}).
\]
For real \(c=\cos t,\ l=\sin t\), conjugation about a perpendicular axis reverses \(l\) and fixes the rest of the configuration. This symmetry also holds after averaging centre signs. To bound the continuation, integrate the vertex spin at one endpoint of the varied bond first, fixing the other spins. Its factor is the spherical average of \(e^{\beta q\cdot (A+cB_1+lB_2)}\), with \(A\) real and of norm at most five, and \(B_1,B_2\) real and orthonormal. The signs may change these vectors. The other factors have a fixed finite-volume bound. If \(c^2+l^2=1\), the bilinear square of \(A+cB_1+lB_2\) is bounded in modulus by \(C(1+|c|+|l|)\). For any complex vector \(w\), the spherical average of its exponential has only even powers. The coefficient of degree \(2r\) is \(\beta^{2r}\mathbb E q_1^{2r}(w\cdot w)^r/(2r)!\), first on real vectors by invariance and then by polynomial identity. Its modulus is bounded by \(e^{\beta\sqrt{|w\cdot w|}}\). Conjugation symmetry holds also for complex \(c,l\) by changing variables in the same integral. The resulting entire even function of \(l\) is entire in \(c,l^2\) by its local power series (or its globally convergent power series in \(l\)). Substituting \(l^2=1-c^2\) gives the stated entire \(F\).

**PROVED (nonconstancy, including after centre projection).** Integrate the varied link \(U\) of \(x\) against \(\operatorname{Re}U\) on \(SU(2)\) with the other configuration fixed to the identity. For a fixed sign choice \(\sigma\) this integrates its exponential factor to \(a_\beta\sigma_e(g_z\cdot g_{z'})\) for some \(a_\beta>0\), by spherical symmetry and \(\int q_1e^{\beta q_1}\,dq>0\). Expand the remaining edge factors as powers of \(\beta \sigma_b(g_i\cdot g_k)\). After sign averaging each sign monomial contributes zero or one, also in the ordinary case where all signs are one. After expanding dot products in real coordinates, each product Haar sphere moment vanishes on any odd coordinate power and is positive on even powers. Hence every surviving contribution is nonnegative. Choose one power on each edge of the other three sides of an elementary plaquette containing \(e\), and zero elsewhere. Its sign around the plaquette is one for every flat twist, and using the same real coordinate at all four vertices contributes strictly positively. The entire fundamental coefficient is therefore positive. Class invariance identifies this one-link integral with the coefficient of the function \(F(\operatorname{Re}U)\), which could not be positive for a constant \(F\).

**PROVED.** If this nonconstant \(F\) had no zero, it would have an entire logarithm \(G\), by integration of \(F'/F\) on the plane. The upper growth bound gives \(\operatorname{Re}G(c)\le C_{n,\beta}+C_\beta\sqrt{1+|c|}\). On a circle of radius \(R\) about any \(c_1\), the first Fourier coefficient of \(\operatorname{Re}G\) bounds \(|G'(c_1)|\) by \(2[\sup\operatorname{Re}G-\operatorname{Re}G(c_1)]/R\) by subtraction of the supremum and the mean-value formula. Sending \(R\) to infinity would make \(G\) constant. Thus \(F\) has a zero \(c_*\) of some finite multiplicity \(k\ge1\). Real \([-1,1]\) has strictly positive integral, so a complex lift \(c_*=\cos t_*\) has \(\sin t_*\ne0\). The zero of \(K(t,0)\) at \(t_*\) has the same order \(k\).

**PROVED (integer multiplicity forced by a positive kernel).** Positivity on the physical \(L^2\) space would make all real-point Gram matrices of \(K^u\) positive semidefinite. Indeed approximate point masses by Haar densities on shrinking neighborhoods and use continuity, averaging these tests over \(\Gamma\) since the kernel is separately invariant. Along the real \(t\)-curve this gives a Hilbert-space Gram map \(v(t)\). It continues holomorphically along any fixed path from \(0\) to \(t_*\). Here are the details needed for that continuation. By (26), near every conjugate diagonal \((z,\bar z)\) there is a holomorphic branch of \(K(t,s)^u\) which is positive on the nearby conjugate diagonal. On a sufficiently small real interval about zero its Taylor coefficient matrix is positive because the finite difference quotients representing the two derivatives are limits of positive Gram matrices after the appropriate factorials. Realize that coefficient matrix by vectors \(v_r\). Cauchy estimates bound \(\|v_r\|\) by \(C R^{-r}\) on a smaller polydisc of radius \(R\). Thus \(\sum_{r\ge0}v_r t^r\) is a Gram map on a complex disc, with inner products given by the branch at \((t,\bar s)\). It agrees with the real Gram map up to an isometry on the span.

**PROVED.** Along a compact path the conjugate-diagonal branches have a common positive local radius, by compactness, continuity and (26). In any existing disc the squared norm of each Taylor coefficient of the map about \(z\) is the matching double coefficient of its kernel at \((z,\bar z)\). The same Cauchy estimate therefore extends the vector power series to a disc of the available radius, and the kernel identity there follows by the Taylor series. In overlapping discs the branch agrees on the conjugate diagonal, where it is the positive value, hence agrees throughout a neighborhood by its power series. Finitely many overlapping discs continue the map along the path. In particular its scalar pairing \(f(t)\) with \(v(0)\), taken holomorphic in \(t\), continues to a neighborhood of \(t_*\) and starts as \(K(t,0)^u\). The analytic identity \(K(t,0) f'(t)=u\,\partial_tK(t,0) f(t)\) continues along the same path. Comparing orders at \(t_*\) gives \({\rm ord}_{t_*} f=u k\), since the continued \(f\) is not identically zero. This is impossible for irrational \(u\) or \(0<u<1/k\). This proves the loss of positivity claimed above. Formula (25) still gives a scalar interpolation by positive weights.

## The remaining physical estimate

**PROVED.** There is an exact signed expression for the unestimated term. Tilt the one-slab and crossed two-slab laws of (25) by their displayed integrands and normalize them, writing the resulting expectations as \(\mathbb E_{{\rm one},u}\) and \(\mathbb E_{{\rm cross},u}\). At each finite cutoff \(\log K\) is bounded and differentiation under the integral gives
\[
 J(1)=\int_0^1
 \left[2\mathbb E_{{\rm one},u}\log K(X,Y)
 -\mathbb E_{{\rm cross},u}
       \{\log K(X_1,Y_2)+\log K(X_2,Y_1)\}\right]du.                    \tag{27}
\]
The signed interpolation for changing the underlying plaquette couplings already appears in row 1151, (28). Equation (27) changes the scalar orbit kernel after integration over the temporal gauge. At \(u=0\) the first expectation uses the actual joint law of the two open ends, and the individual crossed pairs in the second expectation have product end marginals. Even their difference at this endpoint needs joint information to improve on the extensive estimate (23). [Earlier interpolation in the plaquette couplings](gap-solve5-astra62.md)

**OPEN.** To use the published full thermal criterion, one needs \(J(1)\le y_0 V(s)/(2(96T_0)^3)\) for the spatial shapes \(2T_0\le s_i<48T_0\) in its weak-coupling window, with \(j=T_0\) and the other quantifiers of A-B** in row 1218. For these shapes the required bound stays of order one. Equation (24) bounds the error incurred by clipping the marks on physical cubes. Equation (22) quantifies the cost of replacing their first moments by an absolute higher moment. Neither estimates the signed difference in (27) at that scale. The other route, (3), still needs a Poincaré bound for the collective spatial midpoint law. Even a spectral estimate in one of these formulations requires a construction and identification of a nontrivial continuum Yang–Mills theory. [Full thermal criterion A-B**](prior/gap-onebound-read-sol.md) · [The lane's continuum obligation](../parts/gap.md)

RESULT — OPEN. Row 1290. The analytic arguments give a total-gradient bound for slow lattice states, a cubic onset of higher moments for the gauge-integrated deleted cut, and a relative truncation estimate for its first moments. The physical singlet thermal bound and the nontrivial continuum construction remain open. The four-dimensional SU(2) Jaffe–Witten mass gap is unproved here. This research note grants no status.
