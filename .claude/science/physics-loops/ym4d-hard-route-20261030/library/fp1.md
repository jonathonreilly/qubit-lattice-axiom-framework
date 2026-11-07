# FP1: The classical flat propagator package

Provenance: OpenAI Codex, Phase A pass 2 (distil), 2026-11-05; checkout `1724d326aee3af902e55c00bd248cf6ef6099e03`. Research text, not an audit; grants no status. The whole part has not yet been refereed. Credit Tadeusz Balaban for the flat propagator method, Karen Uhlenbeck for the small-energy gauge method, and Ethan Sussman and Levent Alpoge, with Claude and Codex as the authors of their text, for the plain-average, soft-contour, interpolation and Fourier constructions used below.

## Definitions and scope

All fields below have one real color, or its complexification, unless SU(2) is specified. At the identity the three SU(2) colors are orthogonal copies. Count each positive bond and each plaquette direction pair once.

**D1. Two coordinate conventions.** Raw cochains on an integer lattice use counting norms and
\[
 (df)_\mu(x)=f(x+e_\mu)-f(x),\qquad
 (da)_{\mu\nu}(x)=a_\mu(x)+a_\nu(x+e_\mu)-a_\mu(x+e_\nu)-a_\nu(x).
\]
On the spacing-\(n\) lattice, \(d_n\) has the same formula with step \(n\), without division by \(n\). Relabeling that lattice by its own units changes \(d_n\) to \(d\). For the separate scalar and seam estimates, physical spacing is \(\eta\), site and bond pairings are \(\eta^4\sum\), and \(D_\eta=\eta^{-1}d\). Adjoint symbols always refer to the stated pairings. Raw link logarithms and physical potentials are related by \(a=\eta A\).

**D2. Actual averages.** Fix odd \(L\ge3\), \(k\ge0\), and \(n=L^k\). Blocks are centered, disjoint cubes with \(n\) sites per axis. Tori have periods divisible by \(nL\); use the prescribed local formulas before periodizing, with multiplicities. A sufficient nonwrapping convention is at least three next-step blocks in each direction. The formulas and their image sums also define smaller compatible quotients when their coordinate multiplicities are retained.

For the raw straight average, site average and center restriction put
\[
 S_n a(y,\mu)=n^{-4}\sum_{x\in B_n(y)}\sum_{t=0}^{n-1}a_\mu(x+te_\mu),\quad
 q_nf(y)=n^{-4}\sum_{B_n(y)}f,
 \quad r_nf(y)=f(y).
\]
Let \(\gamma_{y,x}(a)\) be the arithmetic mean of the oriented sums along the prescribed coordinate-order shortest paths from \(y\) to \(x\) inside \(B_L(y)\), with their prescribed multiplicities. Define
\[
 (\mathsf G a)_{y,x}=\gamma_{y,x}(a)\quad(x\ne y),\qquad
 \sigma(a)(y)=L^{-4}\sum_{x\in B_L(y)}\gamma_{y,x}(a),\quad
 P_L=S_L-d_L\sigma.
\]
The plain \(k\)-step derivative is \(P^{[k]}\), the composition of these plain steps; \(P^{[0]}=I\). This is the derivative of the actual mean, not the straight average substituted as its definition.

**D3. Energy, pivots, covariance.** Define
\[
 E_k(a)=\min_{P^{[k]}w=a}\|dw\|^2.
 \tag{1}
\]
Existence is proved below. On the current lattice put \(h=(L-1)/2\). The direction-\(\mu\) pivot is the crossing bond from \(y+he_\mu\) to \(y+(h+1)e_\mu\). Let \(\iota\) insert nonpivot coordinates with zero pivots. Let \(h_0\) insert \(L^3\) times a row datum on its pivot. The inclusion
\[
 J=\iota-h_0P_L\iota
 \tag{2}
\]
retains every free coordinate and has range \(\ker P_L\). The precision and covariance are
\[
 \langle u,A_k^{\rm flat}u\rangle=E_k(Ju)+\|\mathsf GJu\|^2,
 \qquad C_k^{\rm flat}=(A_k^{\rm flat})^{-1}.
 \tag{3}
\]
The soft gauge coefficient in (3) is one. A fixed coefficient \(\lambda_g>0\) is allowed, with constants also depending on it. Haar Jacobians, counterterms, nonconstant weights and current corrections are not part of (3).

**D4. Kernel statements.** Distances for (3) are periodic bond distances in current lattice units. A first difference means a unit-step difference between existing coordinates of the same type. Equivalently use the bond covariance \(JC_k^{\rm flat}J^*\), whose indices include all bonds. A local Hölder quotient of exponent \(0<\alpha<1\) compares endpoints at distance at most a fixed current-scale radius; it divides their difference by that distance to the power \(\alpha\). The exponential uses the least source-output distance among the endpoints involved. These are discrete, current-scale estimates. They are not mesh-uniform pointwise bounds for a physical fine-mesh Green-function density.

**D5. Scalar compression.** On physical unit blocks with \(\eta=1/m\), let \(Q\) be the arithmetic site mean, with coarse counting pairing. Put
\[
 \Pi=Q^*Q,\qquad A_s=D_\eta^*D_\eta+\Pi,
 \qquad A_{s,D}=I_D^*A_sI_D,
 \tag{4}
\]
where \(I_D\) is zero extension from a site set \(D\). The block term in the compression remains the original \(\Pi\). Distances are ambient physical lattice distances, including periodic wraps.

**D6. Default seam.** A scalar pillar partition has aligned scales \(s_j=\eta L^j\). A bare site is a singleton pillar. \(Q'\) averages sites over their assigned pillars. The physical vector row of length \(s=n\eta\) is
\[
 Q_cA=n^{-5}\sum_{v\in B_n(c_-)}\sum_{t<n}A_\mu(v+t\eta e_\mu),
 \qquad K_c=sQ_c.
 \tag{5}
\]
Retain the interior and outward rows of each layer, and omit inward rows. In particular a bare row has both endpoints bare. Each outward endpoint block is a union of complete finer pillars. The Landau projection here is
\(R=\operatorname{proj}_{\Delta\ker Q'}\), \(\Delta=D_\eta^*D_\eta\).
It is not \(I-Q'^*Q'\), and neither projection is the soft contour matrix \(\mathsf G\). The seam assertion proved in Lemma 8 is the default algebra and the one/two-scale coercivity needed at level zero. Any many-layer use also needs its stated separated local-model geometry; it does not follow from a choice of notation for \(R\).

**D7. Local gauge and quadratic seam.** Lemma U concerns a real SU(2) field on a contractible box with integer side lengths \(1\le n_i\le2n_j\). All gauges on that box are allowed. Plaquette angles are principal group logarithms, measured in the invariant norm. Its gradient norm includes differences of parallel bonds and the squared normal-bond values at both boundary faces. The quadratic estimate (LC) concerns the entire affine raw fibre \(P^{[k]}A=v\), without retained fine-boundary or chart restrictions. Its distances are in top units \(n\), and its shell is defined in Lemma 11.

## Order of constants and imports

The order is the one in [in1.md](in1.md), “Constant order”, including Amendment 1. First fix the requested margins and Hölder exponents (row 1). Choose the scale-independent geometry and odd \(L\) in row 2. The standalone theorem needs only \(L\ge3\); when inserted into IN1 its row-2 floors additionally read \(L>4C_h^{\rm WF}C_h^{\rm UM}c_\ell(1+4\beta_s)\), \(L>L_0^\natural\), and \(L^2\ge6\sqrt2\lambda_a\), with those earlier geometric constants supplied by IN1's other packages. They are not extra scientific imports into this proof. Then choose the flat constants: the scalar constants, interpolation bound 256, local pivot bounds, \(c(L)\), uniform symbol strip and its bound, a smaller inverse strip, and the resulting kernel rate. Fix the gauge Taylor/Sobolev constants before its small-energy threshold. The absolute constants of (LC) can be fixed before \(L\).

If the separated local-model extension is used, row 3 contains its one/two-scale constants, local walk size \(M_1\), returned decay rates, reset/separation scale \(R_1\), and \(\rho=R_1M_1\). A rate obtained from a walk is chosen after that walk's size; a provisional local rate can be chosen before it. Increase \(R_1\) afterwards to pay the read sets and scale summations. None of these quantities is IN1's later nonlinear collar size \(M\). All precede H-M, \(\kappa,\bar\kappa,M\), the final small-coupling ceiling and the torus/cutoff choice (rows 4–10). No early constant here reads those later choices.

There is no import from another assembly part. The proof uses the explicitly defined flat operators and the elementary arguments below. In particular it imports neither PR1 nor a nonlinear background theorem. The optional identification of (1) with a nonlinear background Hessian requires an exact twice differentiable constrained stationary lift. It is not needed to define or prove this classical theorem. The brick geometry qualifications at the end are not assumed for the uniform torus theorem.

**Theorem 1 (FP1, with the scopes made explicit).** For (1)–(3), with the constants chosen in the stated order, uniformly in \(k\) and compatible tori, including real flat holonomies in the prescribed block axial representative:

1. \(c(L)I\le A_k^{\rm flat}\le C L^8 I\), and \(\|da\|^2\le E_k(a)\le256\|da\|^2\) in current units. Here \(C\) is absolute for gauge coefficient one.
2. The precision and constrained covariance have exponentially decaying kernels, including their first and local Hölder differences. Periodization and unitary flat holonomies preserve these bounds. Restrictions to sets of free coordinates preserve the gap and give exponentially decaying conditional covariance kernels.
3. The default level-zero seam identities and one/two-scale energy bound of Lemma 8 hold. The real small-total-energy box gauge of Lemma 10 and the unrestricted quadratic estimate (LC) of Lemma 11 hold on their stated domains.
4. The scalar block estimate, scalar resolvent decay and Dirichlet compressions of Lemmas 2–3 hold uniformly in the fine mesh and volume.

*Proof.* Lemmas 2–11 prove the four clauses. Their hypotheses are part of the statement through D1–D7. The optional several-layer and background identifications discussed below are not consequences of this theorem. \(\square\)

## Scalar block estimates

**Lemma 2 (normalization, block gap and scalar Gram inverse).** With D5,
\[
 QQ^*=I,\quad \Pi^2=\Pi=\Pi^*,\quad
 \|(I-\Pi)f\|^2\le\tfrac14\|D_{\eta,N}f\|^2,
 \quad A_s\ge I,
 \quad Q A_s^{-2}Q^*\ge c_s I>0.
 \tag{6}
\]
Here \(D_{\eta,N}\) uses only the intrinsic nonwrapping bonds of each block. The constants are mesh and volume independent.

*Source:* `flat-port.md` §§4–5; `gates/flat-port-gate.md` §§4–5 verdicts. The sharper unit-block constant and explicit lift are SA 605–845, checked directly for this distillation.

*Proof.* Evaluating the two pairings shows \(Q^*u=u(B)\) on block \(B\). Thus \(QQ^*=I\), and orthogonal splitting gives \(\|f\|^2=\|(I-\Pi)f\|^2+\|Qf\|^2\). On a path of \(m\) sites the vectors
\(v_j(x)=\cos(\pi j(x+1/2)/m)\), \(0\le j<m\), have eigenvalues \(4\sin^2(\pi j/(2m))\). The cosine addition identity verifies the interior equation and both endpoint equations. Distinct eigenvalues give an orthogonal basis. Tensoring gives the block spectrum. Its first nonzero physical eigenvalue is \(4\eta^{-2}\sin^2(\pi/(2m))\ge4\), since \(\sin t\ge2t/\pi\) on \([0,\pi/2]\). For \(m=1\), \(I-\Pi=0\). Adding ambient bonds increases the energy, which proves \(A_s\ge I\).

For \(m\ge2\), put \(\phi_m(j)=16\prod_{i=1}^4\sin^2(\pi(j_i+1/2)/m)\), separately on each block. The geometric sum of the \(m\)-th roots of unity makes its mean one. The map \(Tu=\phi_m u(B)\) satisfies \(QT=I\), \(\|T\|\le16\). Interior second physical differences of each sine-square factor are bounded by \(2\pi^2\). At block endpoints the factor is at most \(\pi^2\eta^2/4\), canceling the \(\eta^{-2}\) in a difference crossing the face. Each site reads only its block and eight face neighbors. Squaring and summing proves \(\|A_sT\|\le C_s\). For \(m=1\), take \(T=I\); the unit Laplacian norm is at most 16. Now
\[
 \|u\|^2=\langle A_s^{-1}Q^*u,A_sTu\rangle
 \le C_s\|A_s^{-1}Q^*u\|\|u\|,
\]
which proves the Gram lower bound with \(c_s=C_s^{-2}\).

In plain coordinates the unitary is \(f\mapsto\eta^2f\); the conjugated averaging entries are \(\eta^2\). Keeping entries \(\eta^4\) with a plain adjoint instead gives \(\bar Q\bar Q^*=\eta^4I\). That matrix is not an orthogonal projection without the factor \(\eta^{-4}\). \(\square\)

**Lemma 3 (scalar decay and compression).** There is an absolute \(t_s>0\) such that, for any site sets \(X,Y\subset D\),
\[
 \|1_X A_{s,D}^{-1}1_Y\|\le2e^{-t_s\operatorname{dist}_\eta(X,Y)}.
 \tag{7}
\]
The full torus is included by taking \(D\) to be all sites.

*Source:* the scalar energy/conjugation mechanism of `flat-port.md` §§4–5 and its gate; SA 922–1144 supplies the precise arbitrary-site compression statement. This proof has been carried over and checked here.

*Proof.* For a real ambient weight \(w\) with \(|w(x)-w(y)|\le\eta\) on neighbors, conjugate by \(M_t=e^{tw}\). On an edge write \(a=e^{t(w_x-w_y)}-1\), \(b=e^{-t(w_x-w_y)}-1\). The off-diagonal error is \(-\eta^2(a\bar u_xv_y+b\bar u_yv_x)\). Use the exact identity
\[
 a\bar u_xv_y+b\bar u_yv_x
 =a(\bar u_x-\bar u_y)v_y+b\bar u_y(v_x-v_y)+(a+b)\bar u_yv_y.
\]
For \(|t|\le1\), \(|a|,|b|\le e|t|\eta\) and \(|a+b|\le et^2\eta^2\). Cauchy–Schwarz, with four incoming edges per site, bounds the error by
\(2e|t|(\|Du\|\|v\|+\|u\|\|Dv\|)+4et^2\|u\|\|v\|\).
The block projection error has row and column sums at most \(4e^4|t|\), because each row has mass one and block diameter at most four. Weighted Cauchy–Schwarz proves the Schur bound from these two sums. With \(C_s'=8e+4e^4\), (6) gives
\[
 \|A_s^{-1/2}(M_tA_sM_t^{-1}-A_s)A_s^{-1/2}\|
 \le C_s'(|t|+t^2).
\]
Take \(t_s=\min(1,(4C_s')^{-1})\). Factoring through \(A_s^{1/2}\) and summing the geometric inverse series gives a conjugated inverse norm at most two. Set \(w(x)=\operatorname{dist}_\eta(x,Y)\) to obtain (7).

For a compression, zero extension preserves the energy lower bound and commutes with the weight. The entire relative error estimate restricts to zero-extended test vectors. The same inverse series therefore applies with identical constants. No averaging over surviving sites, intrinsic distance through holes, or pointwise physical Green-density estimate was used. \(\square\)

## The uniform classical precision

**Lemma 4 (plain fibres, curvature and the factor 256).** The minimum in (1) exists, and
\[
 E_k(a)=\min_{S_nw=a}\|dw\|^2,\qquad
 \|da\|^2\le E_k(a)\le256\|da\|^2.                 \tag{8}
\]

*Source:* `flat-port.md` §10, correction W2 of `gates/flat-port-gate.md`; `seam-quadratic-c.md` §2 and `gates/share-check-199fac1cb.md` §(a). Direct source checks: SA 8396–8664 and 8776–9060 (CF/WI and FX1–FX3).

*Proof.* Telescoping a gradient gives \(S_nd=d_nq_n\). At one step \(\sigma(df)=q_Lf-r_Lf\); hence \(P_Ld=d_Lr_L\). Straight averages compose. Applying these two identities inductively yields a linear scalar functional \(\psi_k\) with
\[
 P^{[k]}w=S_nw+d_n\psi_k(w),\qquad P^{[k]}df=d_nr_nf.
 \tag{9}
\]
If \(P^{[k]}w=a\), add a gradient \(df\) with \(q_nf=\psi_k(w)\); then \(S_n(w+df)=a\). Conversely, if \(S_nw=a\), add \(df\) with \(r_nf=-\psi_k(w)\). Both site maps are onto, both changes preserve curvature, and these are the two separate directions of the equality in (8). No bound on either correcting gradient is claimed.

Telescoping an averaged plaquette defines \(\mathcal C_n\) by \(d_nS_n=\mathcal C_nd\). Its coefficients are nonnegative; their row sum is \(n^2\) and column sum \(n^{-2}\). The latter follows by summing the two longitudinal tents and the two transverse block indicators. Weighted Cauchy–Schwarz gives \(\|\mathcal C_n\|\le1\), proving the lower bound.

Here is an onto lift with controlled curvature. For a coarse \(j\)-cochain let \(I_j\) be the tensor interpolant with factor \(n^{-1}1_{[0,n)}\) in each of its \(j\) form directions and the hat \((1-|t|/n)_+\) in its other directions. Summing translates of the hats gives one. The difference of a hat is the difference of the two adjacent intervals divided by \(n\); therefore
\(dI_0=I_1d_n\) and \(dI_1=I_2d_n\). The absolute row and column sums of \(I_2\) are \(n^{-2},n^2\), so \(\|I_2\|\le1\).

In each direction, averaging the interpolant yields the convolution
\[
 T_n=a_0+a_1(\tau+\tau^{-1}),\quad
 a_0=\tfrac34+\tfrac1{4n^2},\quad a_1=\tfrac18(1-n^{-2}).
\]
For example the off-center weight is the sum of the triangular sequence of overlap lengths, divided by \(n^2\); it is \((n^2-1)/(8n^2)\), and the weights sum to one. The same count applies to a longitudinal interval and a transverse hat. Thus \(S_nI_1=\mathcal T_n:=\prod_{\nu=1}^4T_{n,\nu}\) componentwise. Each one-dimensional symbol lies in \([1/2,1]\), giving \(\|\mathcal T_n^{-1}\|\le16\). The convolution commutes with \(d_n\). Consequently \(w=I_1\mathcal T_n^{-1}a\) satisfies \(S_nw=a\) and
\(\|dw\|\le16\|d_na\|\). This proves the upper bound after relabeling the coarse lattice. On a finite torus the affine fibre is nonempty and its curvature image is a closed affine subspace of a finite-dimensional space. Orthogonal projection onto that image attains the minimum; a preimage attains (1). The fine gauge kernel need not be removed to make this argument. \(\square\)

**Lemma 5 (soft gap in the actual pivot coordinates).** In (3),
\[
 c(L)I\le A_k^{\rm flat}\le C L^8 I.             \tag{10}
\]

*Source:* `flat-port.md` §10 and its gate; SA 8665–8776 (soft-contour argument), with the pivot formulas in 8396–8461.

*Proof.* The selected pivot appears in its own plain row with coefficient \(L^{-3}\), in no other row, and in no internal contour. The straight coefficient is \(L^{-3}\) by the centered tent count; the contour correction reads only internal bonds. Thus \(P_Lh_0=I\), (2) is an inclusion onto \(\ker P_L\), and \(\|Ju\|\ge\|u\|\).

In one \(L\)-cell, with arbitrary Bloch phase \(p\), consider
\(B(p)=J(p)^*[d(p)^*d(p)+\mathsf G^*\mathsf G]J(p)\).
If its quadratic value vanishes, the field is closed and every averaged internal path integral is zero. Closedness makes all such path integrals to an endpoint equal, since their differences bound plaquettes within the block. Hence the field is zero on internal bonds. Plaquettes crossing a face then make all crossing bonds in a fixed direction equal to a number \(b_\mu\) on that face. Their plain row is \(b_\mu\); the constraint makes it zero. Thus the field, and then its free coordinates, vanish. This argument includes complex fields and every unitary phase. The finite matrix \(B(p)\) is continuous on the compact phase torus and positive definite at each phase. Its least eigenvalue has a positive minimum \(c(L)\). Bloch decomposition and Lemma 4 give the lower bound for every \(k\) and volume.

For the upper bound, absolute row sums of \(P_L\) are at most \(5L\). Its column sums are bounded by an absolute constant: the straight tents give \(O(L^{-3})\), and an internal bond enters at most \(O(L^4)\) contour paths, each with the factor \(L^{-4}\), in only a fixed number of neighboring rows. Multiplication by the pivot insertion \(L^3\) gives row and column bounds \(CL^4,CL^3\) for \(J\), and in particular \(\|J\|^2\le CL^8\). The contour matrix has row sum at most \(4L\) and column sum at most \(CL^4\). Since \(\mathsf GJ=\mathsf G\iota\), its squared norm costs only \(CL^5\), without another pivot factor. Finally \(\|d\|^2\le24\) by Cauchy–Schwarz on each plaquette and counting incidences. Apply Lemma 4 to \(Ju\) to obtain the upper bound. \(\square\)

**Lemma 6 (uniform holomorphic symbol).** The matrix symbol of \(E_k\) extends to a fixed complex strip, with a bound independent of \(n=L^k\). The pivot precision and its inverse extend to a smaller strip with bounds depending only on \(L\).

*Source:* the kernel conclusion of `flat-port.md` §10 and its gate, made explicit by SA 9060–9583 (FX4–FX31). This carries the source's exact cancellation, rather than replacing it by a real-axis spectral gap argument.

*Proof.* Use a unitary Bloch transform, \(p\in[-\pi,\pi]^4\), aliases \(\xi_m=(p+2\pi m)/n\), and \(m\in I_n^4\), \(I_n=\{-(n-1)/2,\ldots,(n-1)/2\}\). With
\(b_n(z)=\sin(nz/2)/(n\sin(z/2))\), the straight filter is
\(s_{\mu,n}(\xi)=n e^{i(n-1)\xi_\mu/2}\bigl(\prod_\nu b_n(\xi_\nu)\bigr)b_n(\xi_\mu)\).
The coarse transform of the average is \(n^{-2}\sum_m s_{\mu,n}(\xi_m)\widehat w_\mu(\xi_m)\). The auxiliary Feynman form \(\|dw\|^2+\|d^*w\|^2\) has symbol \(\lambda(\xi)I\), \(\lambda=4\sum\sin^2(\xi_\nu/2)\). Minimizing this positive form at \(p\ne0\) gives a diagonal coarse covariance \(D_n\). Define its analytic continuation by
\[
 q_{\nu,m}=\frac{\sin((p_\nu+2\pi m_\nu)/2)}{n\sin((p_\nu+2\pi m_\nu)/(2n))},\quad
 f_{\mu,m}=\Bigl(\prod_\nu q_{\nu,m}^2\Bigr)q_{\mu,m}^2,\quad
 s_{n,m}=4n^2\sum_\nu\sin^2\frac{p_\nu+2\pi m_\nu}{2n},\quad
 D_{\mu,n}=\sum_m\frac{f_{\mu,m}}{s_{n,m}}.       \tag{11}
\]
Removable ratios have their limiting values. On the real axis this is \(n^{-4}\sum|s_{\mu,n}|^2/\lambda\). Off that axis use the product of the filters at opposite frequencies, not complex conjugation.

Write \(t_\mu^\pm=e^{\pm ip_\mu}-1\). A fine Hodge decomposition subtracts a gradient to make a field divergence free; the straight average changes by a coarse gradient. Conversely every coarse gradient lifts, since \(q_n\) is onto. The curl minimum therefore equals
\(\min_z(a+t^+z)^*D_n^{-1}(a+t^+z)\): one inequality uses the divergence-free representative, the other gradient-corrects a Feynman minimizer back to the desired coarse field. Solving this scalar minimum yields
\[
 \mathcal E_n=D_n^{-1}-
 \frac{D_n^{-1}t^+(t^-)^{\mathsf T}D_n^{-1}}
 {(t^-)^{\mathsf T}D_n^{-1}t^+}.                 \tag{12}
\]
The real zero mode has value zero, because its constant fine lift is \(a/n\).

We check a uniform complex neighborhood. For \(|\Re p_\nu|<\pi+\rho\), \(|\Im p_\nu|<\rho\), with fixed sufficiently small \(\rho\),
\[
 |q_{\nu,m}|\le C(1+|m_\nu|)^{-1},\qquad
 \Re s_{n,m}\ge c(1+|m|^2)\quad(m\ne0).
\]
Indeed \(|\sin(x+iy)|^2=\sin^2x+\sinh^2y\); the real noncentral argument stays away from zero by \(c|m_\nu|/n\) and away from the other sine zeros. The imaginary displacement changes \(\Re(4n^2\sin^2)\) by at most \(C\rho^2\). The central ratios are bounded sinc quotients. The remainder
\(R_\mu=\sum_{m\ne0} f_{\mu,m}/s_{n,m}\)
is consequently bounded by the summable majorant
\(C(1+|m|^2)^{-1}\prod_\nu(1+|m_\nu|)^{-2}\).
It and its fixed-order derivatives on smaller boxes are bounded uniformly in \(n\).

Near zero put \(s=s_{n,0}\), \(Q_0=\prod q_{\nu,0}^2\), \(f_\mu=Q_0q_{\mu,0}^2\), and \(h_\mu=(f_\mu+sR_\mu)^{-1}\), \(H=\operatorname{diag}h_\mu\). These are uniformly holomorphic and bounded. The exact identity
\[
 \sum_\mu\frac{t_\mu^+t_\mu^-}{f_\mu}=\frac{s}{Q_0}
\]
follows by canceling the numerator sine squares. Hence
\[
 \sum_\mu t_\mu^+t_\mu^-h_\mu=s\mathcal J,\qquad
 \mathcal J=Q_0^{-1}-\sum_\mu\frac{t_\mu^+t_\mu^-R_\mu h_\mu}{f_\mu},
 \qquad
 \mathcal E_n=sH-\frac{Ht^+(t^-)^{\mathsf T}H}{\mathcal J}.       \tag{13}
\]
Since \(\mathcal J(0)=1\), the last expression is holomorphic and \(O(|p|^2)\) on a fixed neighborhood. It cancels the entire complex zero cone of \(s\), not only the real zero momentum.

On the remaining real compact set \(|p|\ge r>0\), the central term in (11) gives \(c_D\le D_\mu\le C_r\), and \((t^-)^{\mathsf T}D^{-1}t^+\ge c_r\). The preceding alias bounds, and \(\Re s\ge cr^2-C|\Im p|^2\), give uniform analytic derivative bounds nearby. Shrinking the imaginary width keeps these denominators separated from zero. Formula (12) agrees with (13) on overlaps. Alias reindexing makes the glued symbol periodic, so it is uniformly bounded on a fixed strip.

Fold the current lattice into its \(L\)-cells. The finite Fourier change of basis has entries \(L^{-2}e^{i(P+2\pi j)\cdot r/L}\); its inverse has the opposite exponent, also for complex \(P\). Folding \(\mathcal E_n\) and adjoining the finite-range \(\mathsf G\) gives
\[
 A_n(P)=J(-P)^{\mathsf T}
       [\mathcal E_n^{\rm cell}(P)+\mathsf G(-P)^{\mathsf T}\mathsf G(P)]J(P).
\]
This is bounded on an \(L\)-dependent strip, uniformly in \(n\). Cauchy's estimate bounds its first derivatives there by \(M_A(L)\). Reduce the width until its variation from real \(P\) is less than \(c(L)/2\). Lemma 5 and the geometric inverse series then give a holomorphic inverse bounded by \(2/c(L)\). \(\square\)

**Lemma 7 (kernels, quotients and conditioning).** Clause 2 of Theorem 1 holds, with constants depending only on the choices already made.

*Source:* `flat-port.md` §10 and its gate; SA 9432–9583. The conditional inverse argument is also the explicit Schur argument of `flat-port.md` §5, applied here to fixed-scale free coordinates.

*Proof.* Fourier inversion of a bounded periodic symbol in a strip gives its kernel. Shift the \(\nu\)-contour by \(i\delta\operatorname{sgn}(x_\nu-y_\nu)\); periodicity cancels the vertical faces. Lemma 6 yields \(C_Le^{-\delta_L|x-y|_1}\) for precision and inverse. Fixed-range multiplication by \(J,J^*\) preserves this estimate on bond coordinates. Unit differences are finite sums of shifted kernels. For a local Hölder quotient, the denominator is at least one, and the numerator is bounded by the two kernel estimates with their least endpoint distance. This proves exactly D4, without a fine-mesh density assertion.

A torus kernel is the absolutely convergent sum over periodic images. Twists multiply those images by unitary factors. Sum absolute values to get the same bound in the torus distance, with a constant independent of its integer periods. The image sum need not equal a single lifted infinite-volume entry. A real flat background can be put in the specified block axial representative: it is gauge-trivial on the cover, and its commuting adjoint holonomies diagonalize unitarily into phases. The preceding twisted calculation applies to each component. Under a different site gauge, compare differences covariantly; an ordinary difference of arbitrarily rotating frames is not the statement just proved.

For a set \(F\) of free coordinates, zero extension gives \(A_F\ge c(L)I\). Its entries retain the exponential bound. Conjugate by \(e^{\theta d(x,y_0)}\). The absolute row and column sums of the change are bounded by
\(C_L\theta\sum_{r\ge0}(r+1)^4e^{-(\delta_L-\theta)r}\), uniformly in \(F\) and the torus. For \(\theta\) small this is less than \(c(L)/2\). The inverse series bounds the conjugated inverse by \(2/c(L)\), which proves exponential decay of \(A_F^{-1}\). This is conditioning by fixing complementary coordinates. Conditioning by a general nonlocal linear constraint is not asserted to preserve this kernel bound. \(\square\)

## The default level-zero seam

**Lemma 8 (seam algebra and two-scale coercivity).** In D6, \(QD\lambda=0\) whenever \(Q'\lambda=0\). In the periodic two-scale model described below, including fine mesh equal to the smaller row scale,
\[
 \|A\|_2^2+\|\nabla A\|_2^2
 \le C_L\bigl(\|CA\|_2^2+\|RD^*A\|_2^2+M_Q(A)\bigr),       \tag{14}
\]
where the smaller physical row scale is normalized to one, \(C\) is physical curl, and \(M_Q(A)=\sum_c a_c s_c^2|Q_cA|^2\) is a counting sum with fixed positive upper and lower bounds on \(a_c\). Equivalently its coefficient is \(a_cs_c^{-2}\) in the top pairing \(\sum_c s_c^4\bar u_cv_c\). The model marks a union of aligned \(L\)-blocks of the unit coarse lattice. Outside them retain only bonds whose two endpoints are outside; within and outward from them retain the length-\(L\) rows, orienting a boundary row outward and counting it once.

*Source:* `flat-port.md` §§2–3, 6–7 and `gates/flat-port-gate.md`. This is the Landau default-seam argument, not the different block-average projection of `fan-ext.md`.

*Proof.* Telescoping (5) gives
\(Q_cD\lambda=s_c^{-1}(\operatorname{Av}_{c_+}\lambda-\operatorname{Av}_{c_-}\lambda)\).
Each endpoint average is over a complete pillar or a union of complete pillars, so it vanishes. A bare bond with one endpoint inside a larger pillar would violate the assertion: take opposite nonzero scalar values at two sites of that pillar and zero elsewhere. Its pillar average is zero but the gradient on that inward bond is nonzero. This explains the omission in the definition.

For completeness the associated column estimate, in the physical adjoint convention, is
\[
 \sum_c|K(c,b)|\le\frac{\eta^4s_b^{-3}}{1-L^{-3}},\qquad
 \sup_b s_b^3|(K^*\omega)(b)|\le(1-L^{-3})^{-1}\|\omega\|_\infty.       \tag{15}
\]
Here \(s_b\) is the maximum pillar scale of the two endpoints of \(b\). A smaller retained row cannot read \(b\): its double block is a union of two complete blocks outside the next layer, so neither endpoint could lie in a larger pillar. At a fixed contributing scale a column receives at most \(\eta^4s^{-3}\) from the longitudinal tents and transverse partition; sum the geometric series starting at \(s_b\). In (15), \(K^*\) uses counting rows and the physical fine pairing, and hence contributes \(\eta^{-4}\). It is not the adjoint for the top-volume pairing of (14).

We prove (14) first at a single row scale. Let the fine spacing be \(h=1/m\), coarse momentum \(\vartheta\), fine aliases \(p_\ell=\vartheta+2\pi\ell\), and
\[
 d_\mu(p)=h^{-1}(e^{ihp_\mu}-1),\quad \omega(p)=\sum|d_\mu(p)|^2,
 \quad q_\ell=m^{-4}\sum_{x\in B}e^{ip_\ell\cdot x}.
\]
The vector average coefficient is \(q_{\mu,\ell}=q_\ell(e^{i\vartheta_\mu}-1)/d_\mu(p_\ell)\), with geometric-sum limiting values. Parseval of the block indicator, the sine formula for its sum, and \(1-\cos t\le t^2/2\) respectively give
\[
 \sum|q_\ell|^2=1,\quad |q_0|\ge(2/\pi)^4,\quad
 \sum_{\ell\ne0}|q_\ell|^2\le C|\vartheta|^2.
\]
Jensen and the tent column sum give \(\|Q\|\le1\). On nonzero aliases \(\omega\ge c\); on the central one it is comparable to \(|\vartheta|^2\).

For \(\vartheta\ne0\), \(I-R\) projects onto \(v_\ell=\bar q_\ell/\omega_\ell\). Put \(B=\sum|v_\ell|^2\), \(g_\ell=d(p_\ell)v_\ell\), and let \(W\) multiply by \(\omega_\ell\). The energy is exactly
\[
 \|W^{1/2}A\|^2-|\langle g,A\rangle|^2/B+a\|QA\|^2.       \tag{16}
\]
Since \(\|W^{-1/2}g\|^2=B\), its first two terms are the squared \(W\)-norm orthogonal to \(z_\ell=d(p_\ell)\bar q_\ell/\omega_\ell^2\). Moreover \(Qz=(e^{i\vartheta}-1)B\). Away from zero, \(|Qz|^2/B\ge c>0\); decomposing along \(z\), and using \(\|Q\|\le1\), proves coercivity there. Near zero the high-alias squared norm of \(W^{-1/2}g/\sqrt B\) is \(O(|\vartheta|^6)\). Expanding the square in (16) and applying \(2ab\le a^2/4+4b^2\) gives
\[
 E(A)\ge\tfrac12\|W^{1/2}A_h\|^2-C|\vartheta|^8|A_0|^2+a\|QA\|^2.
\]
The central vector-average coefficients are bounded below, so
\(|A_0|^2\le C(\|QA\|^2+\|A_h\|^2)\); choose the neighborhood small enough to absorb the negative term. At zero, \(D(I-R)=0\), the row average reads the constant vector mode, and all other modes have the gap. This proves the single-scale \(H^1\) bound uniformly in mesh and volume.

Let \(q,q'\) be its vector and scalar averages, and \(H\) its Landau lift. A bounded right inverse for \(q\) sets only the central alias, dividing by \(q_{\mu,0}\), whose modulus is at least \((2/\pi)^5\). Minimizing the positive form at fixed row value gives
\(qHB=B\), \(R_sD^*HB=0\), \(\|HB\|_{H^1}\le C\|B\|\), where \(R_s=\operatorname{proj}_{\Delta\ker q'}\).

Write the mixed scalar map as \(P_sq'\), with \(P_s\) identity outside marked blocks and their mean inside. Let \(H'\omega\) minimize \(\|\Delta\lambda\|^2\) at \(q'\lambda=\omega\). Block Poincaré makes \(\Delta\) injective on \(\ker q'\), so this is unique. Orthogonality of the minimum gives
\[
 R=R_s+R_+,\quad\operatorname{ran}R_+=\Delta H'(\ker P_s),\quad R_sR_+=0.
\]
For \(B=qA\), solve \(\Delta\lambda_s=R_sD^*A\), \(q'\lambda_s=0\), and decompose
\(A=HB+a+D\lambda_s\), with \(qa=0\), \(R_sD^*a=0\).
The curl of \(HB\) is orthogonal to that of \(a\) by stationarity. The single-scale bound controls \(a\) by its curl, and scalar Poincaré controls \(D\lambda_s\) in \(H^1\) by \(R_sD^*A\). Averaged Stokes and Jensen give \(\|C_1B\|\le\|CA\|\).

Put \(B\) in strict tree gauge in each marked block, subtracting \(D_1\omega\) with \(P_s\omega=0\), and call it \(B_{\rm ax}\). Mixed rows are unchanged by the first paragraph. An internal bond in tree gauge is the integral of at most \(3L\) plaquettes. A face bond minus its averaged crossing path is a loop in the adjacent double block: project its at most 18 coordinate segments successively onto coordinate faces. This fills it by at most 72 rectangles of area at most \(4L^2\), with bounded multiplicity. Cauchy–Schwarz, then summing the \(L^3\) face bonds, bounds their squares by \(C L^5\) times the local curl energy plus \(2L^3\) times the squared dimensionless face row. At an unmarked neighbor the root paths need not vanish, but each consists of at most \(4L\) retained bare bonds; Cauchy–Schwarz pays them with the bare mass. Bounded neighbor overlap proves
\(\|B_{\rm ax}\|^2\le C_L(\|C_1B\|^2+M_Q(A))\).

Uniqueness of the single-scale minimizer gives \(HD_1\omega=DH'\omega\): the latter has the right row, zero curl and vanishing \(R_sD^*\). Thus \(A''=HB_{\rm ax}+a\) is bounded in \(H^1\) by the right side of (14), and
\(\Delta H'\omega=R_+D^*(A-A'')\) has the same bound. Since \(P_sq'H'\omega=0\), scalar Poincaré on pillars of size at most \(L\), paired with \(\Delta H'\omega\), controls \(DH'\omega\) in \(H^1\). Reassemble \(A=A''+DH'\omega+D\lambda_s\) to obtain (14). Nothing excludes \(h=1\), which is the level-zero seam. \(\square\)

## A finite-range primitive

**Lemma 9 (chain contraction in the straight-average kernel).** For odd \(B\ge3\) there are tensor chain maps \(R,T\) with \(R_1=S_B\), \(R_2=\mathcal C_B\), \(RT=I\), and a homotopy \(\mathfrak h\) such that
\[
 d\mathfrak h+\mathfrak h d=I-TR,\quad R\mathfrak h=0,
 \quad\|\mathfrak hG\|^2\le c_HB^2\|G\|^2,
 \quad\|T_2\|^2\le324,                            \tag{17}
\]
where \(c_H=24(222+32\sqrt6+24\sqrt2)<8024\). Its range is less than two top units in the maximum norm. Consequently, if \(dG=0\) and \(\mathcal C_BG=0\), then \(H=\mathfrak hG\) obeys \(dH=G\), \(S_BH=0\), and
\(\|H|_A\|^2\le c_HB^2\|G|_{A^{+2}}\|^2\).

*Source:* `seam-quadratic-c.md` §§3–4 and `gates/share-check-199fac1cb.md` §(a). The following definitions and proof include the periodic constant mode.

*Proof.* In one dimension set \(B=2m+1\), \(I(y)=y+[-m,m]\),
\[
 R^0f(y)=B^{-1}\sum_{I(y)}f,\qquad
 R^1a(y)=B^{-1}\sum_{x\in I(y)}\sum_{s=0}^{B-1}a(x+s).
\]
Put \(\Lambda(t)=(1-|t|/B)_+\), \(\beta(t)=B(m+1)^{-1}(1-|t|/(m+1))_+\), \(g=m(m+1)/(2B^2)<1/8\), and define
\[
 \zeta_y(t)=\Lambda(t-y)+g[2\beta(t-y)-\beta(t-y-B)-\beta(t-y+B)],
\]
\[
 \eta_y(t)=B^{-1}1_{[y,y+B)}(t)+g[\Delta\beta(t-y-B)-\Delta\beta(t-y)],
 \quad T^0u=\sum_y\zeta_yu_y,\quad T^1v=\sum_y\eta_yv_y.
\]
Here \(\Delta f(t)=f(t+1)-f(t)\) only in these one-dimensional formulas. Define
\[
 (ha)(x)=\sum_y\zeta_y(x)B^{-1}\sum_{x''\in I(y)}\int_{x''}^{x}a,
\]
where the integral is the oriented finite bond sum.

Telescoping gives \(R^1d=d'R^0\). The mean of \(\Lambda\) on its center block is \(1-2g\) and on each neighboring block is \(g\); the mean of \(\beta\) on its block is one. Hence \(R^0T^0=I\). The translates of \(\zeta\) reproduce both constants and the affine coordinate: the correction has zero zeroth and first translate moments. Differencing \(\sum_{y\ge y_0+B}\zeta_y\) gives \(\eta_{y_0}\). Summation by parts therefore proves \(dT^0=T^1d'\), and then \(R^1T^1=I\) on coarse gradients. On a circle constants also satisfy this: affine reproduction on the cover gives \(T^1 1=1/B\) and \(R^1(1/B)=1\).

For a primitive \(d\phi=a\) on the cover, \(ha=\phi-T^0R^0\phi\). Thus \(hd=I-T^0R^0\), \(dh=I-T^1R^1\), and \(R^0h=0\). If \(a\) is periodic, its primitive changes by a constant over one period; constant reproduction cancels that change in \(ha\), so the identities descend to circles.

Absolute row/column sums of \(R^0,R^1,T^0,T^1,h\) are respectively bounded by
\((1,B^{-1})\), \((B,1)\), \((2,3B/2)\), \((3/B,2)\), \((4B,6B)\).
For the first two these are the partition and tent sums. For \(T^0\) use \(\sum|\zeta_y|\le1+4g\|\beta\|_\infty<2\) and \(\sum|\zeta_y(t)|\le B(1+4g)<3B/2\). For \(T^1\), use \(|\Delta\beta|<4/B\) and total variation \(2\|\beta\|_\infty<4\). For \(h\), each path has length below \(2B\); a fixed input bond meets at most four contributing center blocks. These counts also give range below \(2B\). Schur's inequality yields the squared norm bounds \(B^{-1},B,3B,6/B,24B^2\), and \(\|T^0R^0\|^2\le3\), \(\|T^1R^1\|^2\le6\).

Tensor the chain maps in four axes. On a component indexed by the set of form directions \(S\), define
\[
 \mathfrak h=\sum_{i\in S}(-1)^{|\{j\in S:j<i\}|}
 (TR)_{<i}\otimes h_i\otimes I_{>i}.
\]
In \(d\mathfrak h+\mathfrak h d\), terms in different axes cancel by the displayed signs and the chain-map identity. The same-axis terms are \((TR)_{<i}(I-TR)_iI_{>i}\); they telescope to \(I-TR\). Every term in \(R\mathfrak h\) contains \(R^0h=0\). On a two-form component \((\mu,\nu)\), the two summands have norm at most \(\sqrt{24}B[3^{(\mu-1)/2}+\sqrt6\,3^{(\nu-2)/2}]\). Cauchy–Schwarz over the six components gives exactly the constant in (17). Also \(\|T_2\|^2\le(6/B)^2(3B)^2=324\). Locality follows coordinate by coordinate. Apply the identity to closed \(G\) with \(RG=0\); restricting its input to the read neighborhood proves the last assertion. \(\square\)

## The two local geometric estimates

**Lemma 10 (U: small-energy lattice gauge).** There are absolute \(\epsilon_U,C_U>0\) such that, on the box of D7, \(\|\theta(U)\|_2\le\epsilon_U\) implies the existence of a gauge with principal bond logarithms \(a\) satisfying
\[
 \operatorname{div}a=0,\quad \|\nabla a\|_2^2\le4\|\theta\|_2^2,
 \quad \|a\|_4+N^{-1}\|a\|_2+\|a\|_\infty\le C_U\|\theta\|_2,
 \quad N=\max n_i.                                  \tag{18}
\]
Here \(\operatorname{div}a(x)=\sum_\mu[a_\mu(x)-a_\mu(x-e_\mu)]\), with absent bonds zero, and \(\nabla\) includes the boundary term specified in D7. No boundary gauge is fixed.

*Source:* `lattice-uhlenbeck.md`, Lemma U, Steps 1–5; `gates/share-check-199fac1cb.md` §(c) and its unit-cube seed repair. The Sobolev input is `lattice_sobolev_box_gauge.md` §1; its proof is included here, so it is not an unnamed import. Neither shell-fill Lemma F nor RF of the former note is used.

*Proof.* Reflect across the site midplanes \(x_\mu=-1/2,n_\mu+1/2\): tangential components are even, normal components odd, and crossing bonds zero. This gives a one-form on a torus of periods \(2(n_\mu+1)\). Its Fourier identity is
\(\|da\|^2+\|d^*a\|^2=\|\nabla a\|^2\); the contraction uses the conjugate difference symbol. Reflected crossing plaquettes have zero curl. Divide the reflected identity by 16 to obtain on the box
\[
 \|\nabla a\|^2=\|da\|^2+\|\operatorname{div}a\|^2.       \tag{19}
\]
Normal differences next to the zero crossing bonds give exactly the two boundary terms, including their multiplicities when the side is one.

We recall a short proof of the needed Sobolev bound. For finitely supported \(w\ge0\) on \(\mathbb Z^4\), each coordinate-line telescoping bound gives \(w(x)\le g_i(x_{\widehat i})=\sum_t|d_iw(x+te_i)|\). The discrete product inequality
\(\sum_x\prod_i g_i(x_{\widehat i})^{1/3}\le\prod_i(\sum g_i)^{1/3}\)
follows by successive Hölder inequalities. More explicitly in dimension \(d\), first sum in the last variable using Hölder on the \(d-1\) factors that depend on it; apply Hölder with exponents \(d-1,(d-1)/(d-2)\) to separate the remaining last factor, then the dimension-\(d-1\) inequality to the others. Dimension two is the product of two sums. This proves the displayed dimension-four inequality by induction. Hence \(\|w\|_{4/3}\le\prod_i\|d_iw\|_1^{1/4}\). Put \(w=|u|^3\), use
\(|a^3-b^3|\le\tfrac32(a^2+b^2)|a-b|\), and Cauchy–Schwarz. Dividing by \(\|u\|_4^2\), followed by arithmetic–geometric means, gives
\(\|u\|_4\le\tfrac32\|\nabla u\|_2\).
Cut off a periodic lift on three period cells per axis. The cutoff derivative costs \(CN^{-1}\|u\|_2\), absorbed for mean-zero \(u\) by the Fourier gap \(cN^{-2}\). Comparable periods suffice. Each reflected normal component has mean zero. Thus
\(\|a\|_4+N^{-1}\|a\|_2\le C_S\|\nabla a\|_2\).
Also, solving \(\operatorname{div}dw=f\) with even reflection and zero mean gives
\(\|\nabla dw\|_2=\|f\|_2\), \(\|dw\|_4\le C_S\|f\|_2\).

Let \(X=\|\nabla a\|_2\), \(\Theta=\|\theta\|_2\). In a fixed small logarithm chart, Taylor's formula for the four-factor product gives
\(|\theta_p-(da)_p|\le C\sum_{b\in p}|a_b|^2\), so (19) yields
\[
 X^2\le(\Theta+C_1X^2)^2+\|f\|_2^2,\qquad f=\operatorname{div}a.       \tag{20}
\]
Flow along the infinitesimal gauge generated by \(w\) solving \(\operatorname{div}dw=f\). In invariant Lie-algebra coordinates its derivative is
\(\dot a=[w,a]-J(a)dw\), with \(J(0)=I\), \(|J(a)-I|\le C|a|\), and bounded derivative on the chart. The divergence satisfies
\(\dot f=[w,f]-f+E\), where the product rule and the preceding estimates give
\[
 \|E\|_2\le C(\|dw\|_4\|a\|_4+
 \|a\|_\infty\|\nabla dw\|_2+\|\nabla a\|_4\|dw\|_4)
 \le CX\|f\|_2.
\]
Neighbor shifts preserve these norms, and \(\|\nabla a\|_4\le\|\nabla a\|_2\) in counting units. The rotation term is orthogonal to \(f\). Choose \(X_0\) after \(C_S,C_1,C\), small enough that the chart remains valid and \((\|f\|_2^2)'\le-\|f\|_2^2\) whenever \(X\le X_0\). If initially \(X\le X_0/2\) and \(\Theta+\|f\|\le X_0/8\), (20) rules out a first crossing of \(X_0\); absorbing \(C_1X^2\) gives \(X\le2(\Theta+\|f(0)\|)\). The flow exists for all time in this finite-dimensional chart. Compactness of the finite gauge orbit supplies a convergent subsequence as \(f\to0\). At its limit (20) gives \(X\le2\Theta\). No uniform bound on \(w\) itself was used.

To enter this small branch, start on the unit four-cube, not on a point followed by noncomparable slabs. Strict coordinate-tree gauge makes each of its 32 links either zero or a holonomy around a loop filled by at most three unit plaquettes. The invariant distance of a product is at most the sum of distances of its factors, so \(X+\|f\|\le C\Theta\) there. Choose \(\epsilon_U\) small enough to apply the flow. Grow by adding a layer in a shortest unfinished direction; all four sides stay between one and twice the shortest side. Extend the gauge to make the new normal links the identity. A new tangential link differs from its old parallel link by the adjacent plaquette holonomy, so smoothness of log on the chart bounds their logarithm difference by \(C|\theta_p|\). In (19), an old normal boundary value becomes the difference to a new zero link. The new tangential layer duplicates at most one old face layer, plus the plaquette errors. Each error enters only a fixed number of differences. Consequently
\(X_{\rm initial}^2\le3X_{\rm old}^2+C\Theta^2\), and the new divergence is bounded by \(C\Theta\): on the new face its old tangential part equals an old normal boundary value, while its remaining terms are plaquette errors. Reduce \(\epsilon_U\) once to meet the flow's initial conditions at every step. Each step resets \(X\le2\Theta\), so the number of layers never multiplies a constant. Sobolev and \(\|a\|_\infty\le\|a\|_4\) complete (18). A bondless point needs no gauge estimate and no expression involving \(N^{-1}\). \(\square\)

**Lemma 11 (LC: unrestricted quadratic gluing and its shell inequality).** Let \(P^{[k]}A_*=P^{[k]}A_t=v\), where \(A_*\) minimizes (1), and let \(r\ge1\) in top units \(B=L^k\). For a set \(D\) of fine sites, write
\(D^{+s}=\{x:d_\infty(x,D)\le s\}\),
\(D^{-s}=\{x:d_\infty(x,D^c)>s\}\), and
\(S_s(D)=D^{+s}\setminus D^{-s}\).
Plaquette restrictions mean restrictions by base point. There is a competitor \(X_D\) in the same entire affine fibre such that
\[
 dX_D=(1-\chi)dA_*+\chi dA_t+\mathcal R,\qquad
 \|\mathcal R\|^2\le\frac{2c_R}{r^2}
       (\|dA_*\|_{S_{r+5}(D)}^2+\|dA_t\|_{S_{r+5}(D)}^2),       \tag{21}
\]
with \(c_R=62256c_H<5\cdot10^8\). In addition, writing \(E_A(F)=\sum_{p:\,\mathrm{base}(p)\in F}|dA(p)|^2\),
\[
 E_{A_*}(D)-E_{A_t}(D)\le
 \left(1+\frac{\sqrt{2c_R}}r\right)^2
 [E_{A_*}(S_{r+5}(D))+E_{A_t}(S_{r+5}(D))].       \tag{22}
\]
The constants are independent of \(L,k\), volume and shape. For \(k=0\) the fibre has a single field, and the assertions are trivial.

*Source:* `seam-quadratic-c.md` §§2–6 and `gates/share-check-199fac1cb.md` §(a). Lemma 9 supplies its only nontrivial construction. The shifted discrete product rule and the enlarged shell are retained.

*Proof.* Suppose \(B\ge3\). Set \(G=dA_t-dA_*\). Lemma 4 gives \(dG=0\), \(\mathcal C_BG=0\), so Lemma 9 gives \(H=\mathfrak hG\), \(dH=G\), \(S_BH=0\). On the ambient periodic cover put
\(\chi(z)=\operatorname{clamp}(2-2d_\infty(z,D^{-r})/r,0,1)\), or zero if \(D^{-r}\) is empty. Read it at bond and plaquette bases. It has Lipschitz constant \(2/r\), equals one on \(D^{-r}\) and zero off \(D^{+r}\).

Let \(Z=(I-T_1S_B)(\chi H)\). Then \(S_BZ=0\). With \(\psi_k\) from (9), choose any scalar right inverse \(E\) of center restriction and put
\(X_D=A_*+Z-dE\psi_k(Z)\).
By (9) it has exactly the desired plain datum. The possibly large correcting gradient changes no curvature. The chain-map identity gives
\[
 \mathcal R=[d,\chi]H-T_2d'S_B(\chi H),\quad
 [d,\chi]H_{\mu\nu}(z)=
 (\chi(z+e_\mu)-\chi(z))H_\nu(z+e_\mu)
 -(\chi(z+e_\nu)-\chi(z))H_\mu(z+e_\nu).       \tag{23}
\]
In particular the shifted link values cannot be replaced by unshifted ones.

Let \(\mathrm{Tr}=\{z:r/2<d_\infty(z,D^{-r})<r\}\), using continuous points when locating a change of \(\chi\). A nonzero fine difference of \(\chi\) has its segment meet this transition. A row of \(S_B\) reads bond bases within one top unit of its midpoint \(c_*\). Since \(S_BH=0\), replace \(\chi\) in that row by \(\chi-\chi(c_*)\); it vanishes unless the row meets a transition. The coarse curl and \(T_2\) put the defect output within four top units of \(\mathrm{Tr}\). The contributing rows read \(H\) within \(2+1/B\) of the transition, and \(H\) reads \(G\) less than two further units away. Thus the actual input set lies within \(4+1/B<5\) of \(\mathrm{Tr}\). It lies in \(S_{r+5}(D)\): the outer containment is immediate. For the inner containment, suppose an input site \(u\) had distance greater than \(r+5\) from \(D^c\). A nearby transition point \(z\) is within \(4+1/B\); round \(z\) to a fine site \(x\), costing at most \(1/(2B)\). Then \(d(x,D^c)>r\), so \(x\in D^{-r}\), whereas \(d(z,D^{-r})\le1/(2B)<r/2\), a contradiction. This also fixes the fine-site/continuous-cutoff endpoint convention.

Each bond appears in at most three terms of each orientation in (23), giving
\(\|[d,\chi]H\|^2\le24\|H\|^2/(r^2B^2)\) on its read set. The nonnegative row and column sums of \(S_B\) are \(B,B^{-3}\); also \(|\chi_b-\chi(c_*)|\le2/r\) on its support. Thus
\(\|S_B(\chi H)\|^2\le4\|H\|^2/(r^2B^2)\) on its read set. The coarse curl norm squared is at most 24, and \(\|T_2\|^2\le324\). Squaring the sum in (23) with factor two gives
\[
 \|\mathcal R\|^2\le
 \frac{48+2\cdot324\cdot24\cdot4}{r^2B^2}\|H\|_{A_2}^2
 \le\frac{62256c_H}{r^2}\|G\|_{S_{r+5}(D)}^2,
\]
where \(A_2\) consists of read bonds within three top units of the transition. Lemma 9 supplies the second inequality. Finally \(|G|^2\le2|dA_*|^2+2|dA_t|^2\), proving (21).

Split plaquettes into \(I=D^{-(r+5)}\), the shell, and \(O=(D^{+(r+5)})^c\). The competitor curvature equals \(dA_t\) on \(I\) and \(dA_*\) on \(O\). Minimality cancels the latter exterior energy. On the shell use convexity for \((1-\chi)dA_*+\chi dA_t\) and
\(|u+v|^2\le(1+\varepsilon)|u|^2+(1+1/\varepsilon)|v|^2\).
Moving from \(I\) to \(D\) costs at most one additional \(A_*\) shell energy. This gives the coefficient
\((1+\varepsilon)+(1+1/\varepsilon)2c_R/r^2\), minimized at \(\varepsilon=\sqrt{2c_R}/r\), which is (22). This proof does not preserve extra fine-boundary data, a fixed parent gauge, or a complex chart radius. \(\square\)

## Gate qualifications and supplied definitions

The four numbered assertions in the skeleton are the theorem distilled here. Its parenthetical name “F0–F5” must not enlarge those assertions to every mixed-sequence density estimate, changing-sequence comparison, or chart identification appearing elsewhere under those labels. Lemmas 4–7 prove the uniform plain/soft-contour theorem directly; Lemma 8 proves its separate default level-zero seam. The alternative brick proofs in `fan-ext.md` and `fd-local.md` are therefore not additional premises of these lemmas. Their gates' restrictions survive as follows.

* `flat-port-gate.md`, W1: whenever the mixed-scale regularity argument takes a local cube of radius comparable to \(m/L\), the usual estimate requires radius at least \(16\eta\). At the remaining finitely many small mesh levels use \(|u(x)|\le\eta^{-2}\|u\|_{2,\{x\}}\) and finite neighbor differences, paying the bounded scale ratio. No small cube is silently treated as a continuum-sized cube. D4 and Lemma 7 only assert current-lattice differences.
* The same gate's W2 is proved in both directions in (9); it is not an equality of the averaging maps. Its W3 is the off-center truncated-kernel correction: a sum of \(DD^*G\) outside a radius-\(4h\) ball centered \(h\) away from the evaluation point is the full cutoff sum minus that ball sum. Summation by parts turns the latter into a boundary sum of \(DG\); its distance is at least \(3h\), and the surface count \(O(h^3)\) cancels \(|DG|=O(h^{-3})\). Thus the coefficient multiplying the change of the subtracted Hölder constant is bounded. This is a repair for that auxiliary Schauder proof, not an imported finer interpretation of Lemma 7.
* `share-check-199fac1cb.md`, §(c): Lemma 10 starts at a unit four-cube. The zero-site start with a claim of comparable sides at all intermediate stages is replaced. The gate checks U only; the shell-fill F/RF claims are not consequences of U alone. Its §(a) restricts LC to the unrestricted flat affine fibre; (21) retains this restriction, the shifted product rule, and the shell radius \(r+5\).
* `fan-ext-73b09692a.md`, D1–D2: its extension charts have radius \(b/64\), not \(b/8\). A tenfold chart at scale \(Rs_{\ell+1}\) therefore needs \(t_{\rm brick}\ge1280RL\). The staggered brick tiling requires torus periods divisible by \(b\) in coordinate 1 and \(2b\) in coordinates 2–4 (the stronger \(8b\) convention suffices). These are different compatibility conditions from D2's uniform block lattice.
* The same gate's D3: **Outstanding for the brick-chart extension.** Its chart kernel formula (8.6) additionally needs proof that the specified coordinates identify the quotient classes, and that their source functionals annihilate \(D(\ker r_N)\). The gate rechecked the latter at flat fields but did not rebuild the former. It remains an implication with both hypotheses displayed, not a theorem supplied by (14) or by the uniform pivot chart (2). Its projection \(P_N=I-r_N^*(r_Nr_N^*)^{-1}r_N\) is different from D6's Landau projection. D4's very large sufficient floor \(L\ge4K_b\) is not a necessary scale threshold; the local count there only uses \(L\ge32\).
* `fd-local-00f9df685.md`, D1–D4: the several-jump cover needs an early, scale-independent patch constant \(R\), an \(L\)-independent one-jump constant \(C_0\), and \(t_{\rm brick}\ge10^4RL^2\). It also needs complete families on common tilings with the collar
  \(F_\ell+[-t_{\rm brick}s_\ell/4,t_{\rm brick}s_\ell/4]^4\subset F_{\ell+1}\).
  This suffices for the one-jump-per-enlarged-patch cover and its conditional flat IMS estimate \(\|H/h\|^2\le16C_0E(H)\); it does not identify all consumer data with that domain. The gate closes the collar check for complete \(6t_{\rm brick}\) families and explains that the top collar is vacuous when all top parents are fixed. **Outstanding for arbitrary consumer families:** lateral closure where a new family joins an older layer. No assertion of automatic closure is made here. The strengthened brick bound can be imposed directly after \(L\), or paid by the later small-field ceiling when the supplier's fill-radius constants are fixed. The corrected \(b/64\) radius, rather than the older \(b/8\), is used for fans. D5's overloaded brick-side symbol is renamed \(t_{\rm brick}\) here; any rate parameter reading that side must be chosen afterwards.

The gates do not establish curved \((\mathrm{LC}_U)\). That estimate remains **Outstanding outside FP1**, as do nonlinear stationary-lift and enlarged complex-domain conclusions. No negative or impossibility theorem about those extensions is claimed. A bound with an \(L\)-dependent exponent must not be relabeled as an absolute fast rate required by another assembly part; Theorem 1 permits its displayed dependence on \(L\).

Definitions supplied or made explicit for this distillation are exactly: the raw versus physical cochain pairings (D1); the translated contour family, compatible quotient convention and all three site/vector maps (D2); the attained variational energy, pivot embedding, gauge coefficient and inverse (D3); the distance, difference and local Hölder conventions (D4); the zero-extension meaning of scalar Dirichlet compression (D5); the no-inward row geometry, row-mass normalization and actual Landau projection (D6 and Lemma 8); the box boundary gradient and unrestricted fibre (D7); the alias continuation with opposite-frequency factors (Lemma 6); conditioning as a coordinate compression (Lemma 7); the tensor chain contraction and oriented path integral (Lemma 9); and the base-point shell, continuous cutoff and curvature defect (Lemma 11). Symbols introduced only inside a proof are defined there. No new physical axiom or physical identification is supplied.

## Result

Theorem 1 proves the skeleton's four explicit FP1 conclusions with their domains stated: the unweighted uniform flat precision and covariance, the factor-256 curl comparison, the default level-zero seam, the real small-total-energy box gauge, the unrestricted quadratic shell estimate, and the mesh-uniform scalar gap and compressed resolvent estimate. The proof imports no other assembly part. It uses the elementary finite-dimensional Fourier, projection, Taylor, Sobolev and chain-homotopy arguments written above. Named methods are credited in the provenance; neither a gate verdict nor a numerical run is a proof premise.

Corrections made in this distillation are: separate physical/counting adjoints and the Landau/soft-contour/brick projections; spell out the two plain/straight fibre corrections; keep the physical scalar block projection under compression; retain the entire complex-cone cancellation and opposite-frequency convention; state precisely the discrete Hölder and coordinate-conditioning scopes; treat zero depth and bondless boxes separately; replace U's initial point by the unit-cube seed; retain LC's shifted product, periodic harmonic mode, unrestricted correcting gauge and enlarged shell; specify shell-distance endpoint conventions; and carry forward all the W1–W3 and brick/family qualifications listed above. The skeleton's shorthand package name is restricted to its explicit four assertions, without importing additional mixed-sequence or brick-chart conclusions by that name. Those extension obligations are marked **Outstanding** where they arise; none is used to prove Theorem 1.

Source record: all five FP1 library notes and all four cited checks were read whole at checkout `1724d326a`. The additional Sobolev input was read in its relevant bounded section, and IN1's constant-order table and amendment were read. The SA index README, the neighboring scalar, A2/A3 and flat-package chunk rows, and their obligation entries were used to locate the source. The outline was read in bounded excerpts covering 605–1149, 3835–3897, and 8396–9583, including every outline formula used here. No quoted CA-I/II/III or YM3 line enters a proof. The requested CA-I file was fetched once but supplies no theorem or premise here; no other account file was needed. Published-paper names in the source notes are attribution, not unverified imported theorem statements.

Reproducible upstream identity: Ethan Sussman and Levent Alpoge, with Claude and Codex as the authors of their text, commit `31a47c543775`; [outline](https://raw.githubusercontent.com/ethanwsussman/Yang--Mills-LLM-experiment/31a47c543775/YM4_sketch_500.tex), SHA-256 `d7f77d4da3eb23038250c52468a341281d9ba86b4af21d3371d208a2537d4b6f`; [CA-I](https://raw.githubusercontent.com/ethanwsussman/Yang--Mills-LLM-experiment/31a47c543775/theorem_0_complete_account_raw_I.tex), SHA-256 `4cb5cb5e0af8dbddbee207926621300350e018c6cf1d6567a753167ce10e6e93`. Retrieval, text search and file checks are bookkeeping only. No computer-assisted mathematical step was used. This is research text, grants no status, and **has not yet been refereed as a whole part**.

## Change log (pass 3 fixes, lead, 2026-11-05)

Applied the findings of `gates/fp1-gate.md` (Claude fresh session, first failing step none):
1. Lemma 4's source: FX1-FX3 are at outline lines 9081-9128.
2. Lemma 5: Schur's test gives ||J||^2 <= C L^7; the stated C L^8 is true, not sharp.
3. Lemma 6: s and h each carry more than one meaning; read from context (rename at hardening).
4. Lemma 10: the sentence about a bondless point is outside D7's domain (sides >= 1) and is withdrawn.
5. Scope: at current scale the Holder clause follows from the kernel bound; it is not a fine-mesh Holder estimate, and PR1's clause (H) cannot cite FP1(2) for that.
6. The brick one-jump and several-jump checks listed in ym4-assembly section 5 are not used by FP1 and do not count toward its status.

**Status: frozen**, importing no other assembly part. Reopens only on a `wrong` signal.
