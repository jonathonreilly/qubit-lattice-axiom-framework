# Repo search

**ARGUED — scope.** At lane `2a12f2296448`, I searched Markdown and TeX on `origin/main@8b11ae2bb95e`, `pr/10114@f76f6c649cff`, `pr/10133@89faef229ff6`, `pr/10134@1e70c7211a2c` and `pr/10141@c73ad7b177d9`. Terms included large N/rank/colour with Wilson, gauge, gap and clustering in either order, Shen/Zhu, Knabe, trace polynomials, Langevin tangents, damped parallel transport, directional Hessian tails, Schwinger–Dyson concentration and triangular Haar shifts. The paired searches for a local trace-polynomial tangent criterion or a finite-time gauge factorization theorem returned no lines. Broad lists were capped. The target-specific prior was absent. The 8 November repo digest concerns older RG obligations. The task row names no further repo hit. The registry's tangent rows OA7 and S2 concern chart or constraint tangents. I found no other owner of the large-rank target.

- **ARGUED — strong coupling.** Main, `research/mass-gap/library/prior/gap-lit.md` §§B–C and `gap-crux-fp.md` at 229. The digest of Shen, R. Zhu and X. Zhu, arXiv:2204.12737, reports SU(N) exponential decay for a class of observables at inverse coupling below $1/[16(d-1)]$. Nissim, arXiv:2510.22788, reports a U(N) gap in the ’t Hooft regime. The digest gives no threshold for that result. Main’s `gap-crux-lit-cross.md` §§C4–C5 reports an all-coupling functional inequality in two dimensions and records its unsuccessful four-dimensional search. The local `prior/gap-lit-recent.md` at 166 reports Cao, Nissim and Sheffield, Theorem 1.2, giving a $U(N)$ Wilson-loop area bound for $\beta\le\beta_0(d)$ uniform in rank. Its observable differs from the connected correlations tested here. These literature reports are **UNVERIFIED** at theorem level here.
- **ARGUED — loop methods.** Main, `research/mass-gap/library/prior/gap-fullread-1.md` §9. Anderson and Kruczenski, arXiv:1612.08140, equations (11)–(23), retain products at finite rank. Equations (63)–(67) give a positive open-path Gram matrix. The reported four-dimensional truncations give numerical bounds. All five refs' `plaquette-bootstrap-closure-20260503/LITERATURE_BRIDGES.md` names Eguchi–Kawai reduction. Their `docs/YT_WARD_IDENTITY_DERIVATION_THEOREM.md` (125–138) gives two fermionic contact terms in a current divergence. I use trace splitting below. None of these passages supplies its signed tangent estimate.
- **ARGUED — closest geometric methods.** PRs 10114/10133, `ym4d-proof/parts/domains-support.md` at 14 and `normalized-return--global-history.md` at 59, give positive scaled Hessian and tail bounds for the ordinary-chart two-step density with fixed terminal identity, zero source and bounded coupling ratios. Its chart complement remains open. Their `COVARIANT_SOFT_BACKGROUND_ASTRA.md` (CB4) factors product Haar by a triangular tree gauge. I use that change-of-variables principle in Lemma 16. In this lane `gap-gamma2-astra.md` (G2) gives an integrated SU(2) curvature criterion and shows its equivalence to a Langevin gap under bounded Hessians. `gap-blockcrit-opus.md`, Theorem R, uses conditional block couplings at fixed SU(2). The criterion below is a finite polynomial inequality on the action of a colour tangent before a Gibbs average.
- **ARGUED — one-link matrix saddle.** Searches of the same five refs for finite-rank Wilson staples, truncated Haar matrices, Stiefel frames and Gross–Witten–Wadia returned no lines. Locally, `gap-face-exercise-fable.md` (N14) reports the solvable two-dimensional large-rank transition. `prior/gap-lit-grok-paths.md` §A.2 reports that two-dimensional loop bounds reproduce it. `prior/gap-lit-recent.md` at 165 credits Gross and Witten for the proposed transition. These attributions are **UNVERIFIED** at theorem level here. Section 7 uses the one-link matrix integral to test curvature of four-dimensional conditional Wilson laws.
- **CITED — account.** Sussman and Alpoge, with Claude and Codex, CA-I, Theorem 0 (2698–2713), excludes the mass gap from its conclusions. CA-III, Proposition `10.7:prop-clustering-mass-gap` (108223–108270), takes a gap and a one-dimensional vacuum as hypotheses for exponential reflected decay. The outline distinguishes the scalar constrained inverse from a physical gap (774–780) and gives a gapless spectral measure with polynomial decay (588–599, 31871–31882). Locators were `sa-index/chunk-01.md`, `chunk-29.md`, `obligations.md` and `ca-full/index.tsv` at the supplied source revision `31a47c543775`. No Balaban bound is imported.

**ARGUED — vector comparison.** FINISH 1702 credits Kopper–Magnen–Rivasseau, Propositions 2–3 and (207), for a large-flavour Gross–Neveu expansion, Gawędzki–Kupiainen for hierarchical closure, and Kupiainen's vector expansion via Kopper's secondary account. The reported bound $N>c\exp(50\pi\beta)$ is **UNVERIFIED** here. FINISH 1706–1707 and the purity crux card concern fixed-rank transport on the physical trajectory. This note tests which stability estimate the matrix law itself would need.

# A local large-rank test for the four-dimensional Wilson law

**PROVED here.** At $\lambda=1$ the actual Wilson law suppresses adverse curvature in a prescribed two-colour plane with probability at most $(1+e^N)^{-1}$ at threshold $\alpha=1/4$ (18). Theorem 14 includes mixed plaquettes, and (21) allows cyclically chosen colour planes. The local loop equations hold in every subsequential large-rank equilibrium saddle (13). The transfer gap follows conditionally from a single finite polynomial inequality (6). At low staple rank all colour directions contract with high conditional probability (23). For other exteriors a plane chosen after observing the same link expands with probability tending to one (24). **The order-one mass gap remains open.**

**GUESSED — target.** Use lattice spacing one and $I=[1,2]$. For every $\lambda=g^2N\in I$ there exist $N_0(\lambda)\ge2$, $m(\lambda)>0$, and $C(\lambda)<\infty$ such that on every periodic four-dimensional cube of side $M\ge3$, for all $N\ge N_0$, real local smooth gauge-invariant $F,H$ satisfy

$$
 |\operatorname{Cov}_{\mu}(F,H)|\le C(\lambda)D(F)D(H)e^{-m(\lambda)d(A,B)} .
$$

Here $A,B$ are their nonempty link supports, $d$ is graph distance joining links on a common plaquette, and $D(F)=\|F\|_\infty+L(F)$, where $L(F)$ sums the single-link gradient suprema in the metric below. Constants and the rate are uniform in $M,N$. The Wilson density is $\exp[(2N/\lambda)\sum_p\operatorname{Re}\operatorname{Tr}U_p]$ relative to independent Haar probabilities on $SU(N)$. Each unoriented plaquette occurs once. This fixes the factor two in the coupling. The interval tests bare order-one coupling. A running trajectory needs an additional scale argument.

**ARGUED — proof plan.** Transport a tangent vector along Wilson Langevin time. Keep its two matrix insertions when taking normalized traces. The exact generator on these expressions is its leading trace-splitting part plus $N^{-2}$ times a local remainder. Look for a quadratic form of bounded range in which the leading generator decreases energy. A strictly positive margin pays for the remainder. Locality then converts the decay in Langevin time into decay in lattice distance. The first test is whether an ordinary scalar trace weight can see a defect in two colour directions.

## 1. The exact tangent equation

**PROVED — Lemma 1 (transport at every coupling).** Write $\tau=\operatorname{Tr}/N$, $|v|^2=\tau(v^*v)$ and $E(v)=\sum_e|v_e|^2$. A tangent vector at $U_e$ is written $U_ev_e$ with $v_e^*=-v_e$ and $\tau v_e=0$. The link metric is $-N\operatorname{Tr}(vw)$, so the Riemannian length is $N|v_e|$. Let $l_e(F)$ be the supremum of the dual length of $d_eF$, and $L(F)=\sum_e l_e(F)$. Write $D_{e,X}$ for differentiation along $U_e\exp(tX)$, $(X_a)$ for a real orthonormal basis of this metric, and $D_v=\sum_eD_{e,v_e}$ with its coefficients frozen when it acts.

Let $h_{p,e}$ be the cyclic plaquette product ending in $U_e$. Reverse the plaquette first if needed so that $U_e$ occurs positively. Set $\pi(C)=(C-C^*)/2-\tau((C-C^*)/2)I$. The left-frame gradient of the log density, the generator and the semigroup are

$$
 b_e=-\frac2\lambda\sum_{p\ni e}\pi(h_{p,e}),\qquad
 \mathcal L=\sum_{e,a}D_{e,X_a}^2+D_b,\qquad P_t=\exp(t\mathcal L).
$$

Indeed the derivative of one real trace is $\operatorname{Re}\operatorname{Tr}(Xh_{p,e})$. Haar invariance gives $\mu(F\mathcal L H)=-\mu\langle\nabla F,\nabla H\rangle$ by integration by parts. The base is compact, smooth and finite dimensional.

On pairs $(U,v)$ let $Y_{e,a}$ differentiate $U_e\mapsto U_e\exp(tX_a)$ and $v_e\mapsto\exp(-tX_a/2)v_e\exp(tX_a/2)$. Define

$$
 \mathcal G_N=\sum_{e,a}Y_{e,a}^2+D_b+\partial_v[k],\qquad
 k_e=D_vb_e+[v_e,b_e]-v_e/2.                                      \tag{1}
$$

Here $D_b$ holds $v$ fixed and $\partial_v[k]$ differentiates the fibre in direction $k$. For each smooth $F$ and each $t\ge0$,

$$
 d(P_tF)_U(v)=\mathbb E_{U,v}\big[dF_{U_t}(v_t)\big].              \tag{2}
$$

*Proof.* The two basis contractions are

$$
 \sum_a X_a A X_a=-\tau(A)I+N^{-2}A,\qquad
 \sum_a\tau(X_aA)\tau(X_aB)=N^{-2}\{\tau(A)\tau(B)-\tau(AB)\}.       \tag{3}
$$

Take the Hermitian Hilbert–Schmidt basis of diagonal matrix units and the real and imaginary off-diagonal pairs divided by $\sqrt2$. Its entries satisfy $\sum_j(H_j)_{ik}(H_j)_{lm}=\delta_{im}\delta_{kl}$. Multiply by $i/\sqrt N$ and remove the normalized central direction $iI/N$. Entry contraction gives both formulas. In particular $\sum_a[X_a,[X_a,v]]=-2v$ on traceless matrices.

Put $J_F(U,v)=D_vF(U)$. At one link, $\sum_aD_{X_a}^2$ commutes with $D_v$. In the commutator the coefficients of $[X_a,v]$ are antisymmetric in the basis indices by trace cyclicity, whereas the anticommutators of the derivatives are symmetric. For the same reason $2\sum_aD_{X_a}D_{[X_a,v]}=\sum_aD_{[X_a,[X_a,v]]}$. Differentiating $J_F$ twice along $Y$ gives

$$
 \sum_{e,a}Y_{e,a}^2J_F=D_v\sum_{e,a}D_{e,X_a}^2F+\tfrac12 J_F .
$$

The vertical $-v/2$ cancels the last term. The differentiated drift is $D_v(D_bF)=D_b(D_vF)+D_{D_vb+[v,b]}F$. Thus $\mathcal G_N J_F=J_{\mathcal L F}$. The diffusion with generator (1) has a linear equation in $v$ over a compact base. The noise rotates each $v_e$. The remaining coefficients are bounded at fixed volume, so its length grows at most exponentially on bounded time intervals. Apply the diffusion chain rule to $J_{P_{t-s}F}(U_s,v_s)$. Its drift vanishes. Localizing at bounded fibre length and using this growth bound proves (2).

**PROVED — Lemma 2 (locality and finite-time factorization).** Set

$$
 J_{ef}=\frac2\lambda\,\#\{p:e,f\in p\},\quad
 K_t=\exp[t(J-\tfrac12 I)],\quad c_\rho=48e^\rho/\lambda-\tfrac12
 \quad(\rho\ge0).
$$

For every $N\ge2$, $M\ge3$, $\lambda>0$, and deterministic starting field $U$,

$$
 l_e(P_tF)\le\sum_f(K_t)_{ef}l_f(F),\qquad
 |\operatorname{Cov}_{P_T(U,\cdot)}(F,H)|
 \le L(F)L(H)e^{-\rho d(A,B)}\,2\int_0^T e^{2c_\rho t}\,dt.       \tag{4}
$$

In particular take real or imaginary parts of two normalized Wilson words of lengths $j,k$, with repeated links allowed. On $I$, for $0<\eta<1$ and $0\le T\le(1-\eta)\log N/c_0$, their covariance in this law has absolute value at most $jk/(c_0N^{2\eta})$. At fixed $T$ it is at most $jk(e^{2c_0T}-1)/(c_0N^2)$. These bounds are uniform in the starting matrices and the volume. $T$ is Langevin time.

*Proof.* Multiplication on either side by a unitary preserves $|v_e|$, and $\pi$ contracts its real Hilbert–Schmidt norm. Differentiate the four factors in $h_{p,e}$ to get $|D_vb_e|\le\sum_fJ_{ef}|v_f|$. The commutator in (1) and the horizontal rotations preserve each length. In a rotating frame the lengths satisfy the upper differential inequality

$$
 \frac{d^+}{dt}|v_e(t)|\le-\tfrac12|v_e(t)|+\sum_fJ_{ef}|v_f(t)|.
$$

At zero use the upper right derivative of the norm. Equivalently apply variation of constants in the rotating frame and take norms. Iteration of the positive integral inequality bounds the length vector by $K_t|v(0)|$. Apply (2) to a unit vector supported at $e$ to get the first bound of (4). Each row and column of $J$ sums to $48/\lambda$ since a link belongs to six four-link plaquettes. Each nonzero entry changes graph distance by at most one. Its power series gives $(K_{2t})_{ef}\le e^{-\rho d(e,f)}e^{2c_\rho t}$. Differentiate $P_s[(P_{T-s}F)(P_{T-s}H)]$ and integrate from zero to $T$. The derivative is $2P_s\langle\nabla P_{T-s}F,\nabla P_{T-s}H\rangle$. Apply the component bound twice and use $K_t^\mathsf{T}K_t=K_{2t}$. Each occurrence of a link in a normalized trace contributes at most $1/N$ to its dual gradient by Hilbert–Schmidt Cauchy–Schwarz. This gives the stated powers of $N$.

**ARGUED — use at order one.** Each fixed pair of normalized traces factorizes to the stated accuracy, even for times growing like $\log N$ at $\lambda=1$. Taking $T\to\infty$ at fixed $N$ in (4) loses the estimate. Equilibrium decay needs a bound that survives that limit.

## 2. Where the rank enters

**PROVED — Lemma 3 (finite-rank remainder).** A local density $q$ is a finite real linear combination of real or imaginary parts of products of normalized traces of words in $U_f,U_f^*,v_f,v_f^*$. Use specified link offsets from one lattice site. Each monomial has exactly two tangent letters across all its traces. Its length $d_w$ counts all matrix letters before differentiation. Put $Q=\sum_x q_x$, where $q_x$ is the translate. On actual finite matrices the generator satisfies the exact identity

$$
 \mathcal G_N Q=\sum_x(\mathcal G_0 q)_x+N^{-2}\sum_x(\mathcal R q)_x,\qquad
 \left|\sum_x(\mathcal R q)_x\right|\le D(q)\,E(v),\quad
 D(q)=2\sum_w|c_w|\,d_w^2 .                                       \tag{5}
$$

Here $c_w$ is the coefficient in the chosen expression for $q$. The subscript zero denotes the leading operator. Both operations in (5) are defined by the following finite rules. When different offsets stand for the same link on a small torus, identify them before differentiating.

*Proof.* Use (1). Its drift has an expression in unitary words and normalized traces with coefficients independent of rank. In particular the subtraction of the scalar part in $\pi$ stays in the leading operator. For $Y_{e,a}$, a unitary letter at that link contributes one insertion of $X_a$ with a sign and an order fixed by differentiation. A tangent letter contributes its commutator with $-X_a/2$, whose two coefficients have absolute values adding to one. Two differentiations give at most $d_w^2$ ordered choices of original letters counting coefficient mass. The second derivative can hit the first letter again. The inserted $X_a$ itself stays fixed. Sum only pairs at the same link.

If both insertions lie in one trace, use the first identity in (3). Its leading term splits the trace in two. Its other term has coefficient $N^{-2}$. If the insertions lie in different traces, use the second identity in (3). Both terms have coefficient of absolute size $N^{-2}$. Retain the terms of order one in $\mathcal G_0$ and their remaining coefficients in $\mathcal R$. Thus the latter coefficient mass on a monomial is at most $2d_w^2$. No repeated expansion in $1/N$ has been made.

For each resulting product, unitary letters have operator norm one. Two tangent letters in one trace have absolute contribution at most $|v_f||v_g|$ by trace Cauchy–Schwarz. For two traces apply Cauchy–Schwarz once to each trace. The bound is at most $(|v_f|^2+|v_g|^2)/2$. Sum over translates of these fixed offsets. Each tag contributes at most $E(v)$ before its factor $1/2$. This proves (5), including for tangent vectors concentrated in a single colour subspace.

**GUESSED — the one missing estimate, at each $\lambda\in[1,2]$.** Find a finite radius $R$, a density $q$ as above, and real numbers $0<a\le b<\infty$, $\delta>0$. Put $e_x=\sum_{i=1}^4|v_{(x,i)}|^2$. On the finite patch containing $q$, $\mathcal G_0 q$ and $e_0$, require the three local inequalities

$$
 q-ae_0\succeq0,\qquad be_0-q\succeq0,\qquad
               -\mathcal G_0 q-\delta e_0\succeq0.                 \tag{6}
$$

Here $p\succeq0$ has a concrete sufficient meaning. Give a finite identity writing $p$ as a sum of $\tau(P^*P)$ plus differences of translates along any of the four lattice axes. The matrix expressions $P$ are polynomials in the indicated letters and their scalar traces, linear in the tangent variables. Use unitary cancellation, the star and trace rules, and $\tau v_f=0$. Nonnegative real constants can be absorbed into the squares. The radius includes all terms of these identities. Take the offsets in $[-R,R]^4$. For $M>M_*=2R+5$ they lift from the torus without extra identifications. The bounded-diameter argument below covers the remaining cubes. Every proposed identity is finite and can be checked coefficient by coefficient. There is no bound here on the radius or the degree needed to find one. Its inputs are the local Wilson action and the matrix identities.

**PROVED — Theorem 4 (conditional equilibrium clustering).** At any $\lambda\in I$ for which (6) holds, the target in the opening holds, even for smooth observables without gauge invariance. For $M>M_*=2R+5$ one obtains the stronger gradient prefactor $C_*L(F)L(H)$. One choice of constants is

$$
 N_0=\max\{2,\lceil\sqrt{2D(q)/\delta}\rceil\},\quad
 \kappa=\delta/(4b),\quad m=\frac{\kappa}{c_1+\kappa},\quad
 C_*=\frac1{c_1}+\frac b{a\kappa},\qquad c_1=48\exp(1)/\lambda-\tfrac12 .
                                                                    \tag{7}
$$

Use $C=\max\{C_*,2\exp[m(8M_*+4)]\}$ for the stated all-volume bound. The order of choice is $\lambda$, the finite certificate, then $N_0,m,C$, then $N,M$ and the observables. For example, if estimates on a length scale $\xi\ge1$ gave $\sum_w|c_w|d_w^2\le A\xi^p$ and $\delta\ge a_0\xi^{-q_0}$, (7) would give $N_0\le\max\{2,\lceil2\sqrt{A/a_0}\,\xi^{(p+q_0)/2}\rceil\}$. Such coefficient and margin bounds are open.

*Proof.* Trace squares are nonnegative at every matrix size and lattice differences telescope. Thus $aE\le Q\le bE$. Equation (5) gives, for the ranks in (7),

$$
 \mathcal G_N Q\le-(\delta-D(q)/N^2)E\le-\delta Q/(2b).           \tag{8}
$$

This absorption is the use of large $N$ in the equilibrium argument. The diffusion chain rule and the bounded-time growth from Lemma 1 give $\mathbb E E(v_t)\le(b/a)e^{-2\kappa t}E(v)$. By (2) and Cauchy–Schwarz,
$\sup|\nabla P_tF|\le\sqrt{b/a}\,e^{-\kappa t}\sup|\nabla F|$ in the product Riemannian metric. Indeed its primal squared length is $N^2E(v)$, which cancels on both sides. At each finite $N,M$ the base has finite diameter and its Wilson mean is invariant. The gradient bound therefore gives uniform convergence of $P_tF$ to $\mu F$ as $t\to\infty$.

Differentiate $\mu[(P_tF)(P_tH)]$ and use integration by parts. The covariance equals $2\int_0^\infty\mu\langle\nabla P_tF,\nabla P_tH\rangle\,dt$. Put $r=d(A,B)$. Up to a time $T$ the locality calculation in (4) bounds the integral by $L(F)L(H)e^{-r+2c_1T}/c_1$. Beyond $T$ the gradient contraction bounds it by $L(F)L(H)(b/(a\kappa))e^{-2\kappa T}$. Choose $T=r/[2(c_1+\kappa)]$. The exponents agree and give (7). For $3\le M\le M_*$ the graph diameter is at most $8M_*+4$. A transverse unit translation of an edge is one graph step, a longitudinal translation costs two via a perpendicular edge, and one step changes the orientation at a fixed basepoint. Translating in four coordinates gives the stated crude bound. Now use $|\operatorname{Cov}(F,H)|\le2\|F\|_\infty\|H\|_\infty$. This extension requires no information about large-rank mixing on a small periodic cube.

**PROVED — physical transfer consequence of Theorem 4.** If (6) holds, the Wilson transfer matrix on every fixed spatial torus of side $M>M_*$ has normalized nonvacuum spectrum in $[0,e^{-m}]$ for all $N\ge N_0$. Also, every subsequential infinite-volume periodic Gibbs limit at a fixed such rank inherits the local clustering estimate by weak convergence on continuous cylinder functions.

*Proof.* The large-volume proof also works on a rectangular time-periodic box with all four periods greater than $M_*$. Its local stencils, row sums and telescoping sums are the same. On a spatial slice let $X,Y$ be the link fields, $V_s$ the sum of spatial log plaquette weights, and $h$ a collection of site gauge matrices with product Haar probability. The time step has kernel

$$
 T(X,Y)=e^{[V_s(X)+V_s(Y)]/2}
  \int\exp\!\left[(2N/\lambda)\sum_e
       \operatorname{Re}\operatorname{Tr}\big(X_e(h\cdot Y)_e^*\big)\right]\,dh,
 \quad (h\cdot Y)_{xy}=h_xY_{xy}h_y^* .
$$

Multiplying these kernels around the time circle gives the Wilson weight after integrating its temporal links. Expansion of the exponential of the real matrix inner product in tensor powers gives a sum of positive Gram kernels before gauge averaging. This operator commutes with the gauge-average projection by simultaneous left and right unitary invariance. Their product is positive, and the two spatial multipliers preserve positivity. The kernel is smooth, symmetric and strictly positive pointwise. The operator is compact. Its top eigenfunction $\psi_0$ can be taken positive by replacing a real maximizing vector by its absolute value. The integral equation then makes it strictly positive everywhere. A second real top eigenvector orthogonal to it would change sign and strictly increase its Rayleigh quotient on taking the absolute value, a contradiction.

For any normalized real eigenfunction $\psi_j$ of positive nonvacuum eigenvalue $t_j$, take $F=\psi_j/\psi_0$ with $\|\psi_0\|_2=1$. It is smooth and gauge invariant by the kernel equation. In the infinite time-cylinder limit the one-slice mean is zero and its two-slice correlation at integer time $n$ is $(t_j/t_0)^n$. To see the limit, insert the multipliers $F$ in the periodic trace $\operatorname{Tr}(F T^n F T^{P-n})/\operatorname{Tr}(T^P)$ and let $P\to\infty$. The normalized long power converges in trace norm to the top projection since $T$ is Hilbert–Schmidt and all other eigenvalues are strictly smaller. At time period $P\ge2n$ the link graph distance between the two spatial slices is at least $n$. Theorem 4 bounds this correlation by $C_*L(F)^2e^{-mn}$. Take $n$th roots and let $n\to\infty$. This proves the spectral bound independently of the size of $L(F)$. The bounded-diameter argument gives clustering on the remaining cubes. The cylinder spectral bound uses spatial sides greater than $M_*$.

**PROVED — a separation test.** Static spatial clustering by itself cannot imply a rank-uniform tangent contraction. For example, on any lattice take independent circle variables with one-site weight $\exp(K\cos(2\theta))$ and unit-metric reversible Langevin dynamics. Disjoint-site covariances vanish at every $K$. Choose a smooth $f$ with $f(\theta+\pi)=-f(\theta)$, equal to $1$ near zero and $-1$ near $\pi$, with transitions only where $\cos(2\theta)\le-1/2$. Its mean is zero. The Rayleigh quotient is the ratio of the integrals of $|f'|^2$ and $f^2$ with this weight. Its numerator is at most $2\pi\|f'\|_\infty^2e^{-K/2}$. Its denominator is at least a fixed length times $e^{K/2}$ from a neighbourhood of zero. The gap tends to zero. A uniform gradient contraction as in Theorem 4 would force a positive lower bound, by applying it for arbitrarily long times to the first nonconstant eigenfunction on this compact circle. Thus the method imposes additional dynamics. This example distinguishes the properties as general criteria. The finite-time Wilson estimate (4) and the matrix tests below are unconditional.

## 3. Two colours defeat scalar weights

**PROVED — Lemma 5 (a necessary test at $\lambda=1$).** No choice $Q=\sum_e a_e(U)|v_e|^2$ with $a_e$ fixed local polynomials in normalized unmarked traces can satisfy (6) when $0<\lambda\le24$. The coefficients may depend on $\lambda$. The lower ellipticity bound must be positive and independent of rank. A trace in this statement can contain any fixed finite word.

*Proof.* Work on one fixed torus larger than the proposed patch. Mark one link $e$. For $n=N-2\ge2$ put any $W_f\in SU(n)$ in the upper block of each link. Put $I_2$ in the lower block except on $e$, where it is $-I_2$. Both choices have determinant one. Take $v_f=0$ off $e$ and take $v_e$ supported on a traceless skew matrix in the lower block. Scale it so that $E=1$. All six $h_{p,e}$ are $-I_2$ there. Since the distinguished link occurs last, $D_v h_{p,e}=h_{p,e}v_e=-v_e$. Thus $D_v b_e=(12/\lambda)v_e$. The lower block of $b_e$ is scalar. The rotations in (1) preserve each $|v_f|^2$, and the derivative of a quadratic term at $v_f=0$ vanishes. Hence at these fields

$$
 \mathcal G_N Q=\mathcal L_N a_e+(24/\lambda-1)a_e.                \tag{9}
$$

For any fixed unmarked word, its normalized trace on the embedded field is $(n/N)\tau_n(w(W))+(2/N)s_w$ with $|s_w|\le1$. Its difference from the rank-$n$ trace is at most $4/N$. Products of a fixed number of these bounded factors have error $O(1/N)$. Apply the contraction rules of Lemma 3 with zero tangent letters to $a_e$. The leading expression for $\mathcal L a_e$ is one fixed polynomial at both ranks, including the scalar subtraction in $b$. Its finite-rank remainder is bounded by a fixed coefficient sum. Consequently $\mathcal L_Na_e(U)=\mathcal L_n a_e(W)+O(1/N)$, uniformly in $W$. Integrate $W$ against the actual rank-$n$ Wilson law at the same $\lambda$ on this torus. Its stationarity kills the rank-$n$ generator exactly. Ellipticity gives $a_e\ge a$ pointwise. The average of (9) has lower limit at least $(24/\lambda-1)a$ for $\lambda\le24$. Equation (8) would bound it by $-\delta/2$ for all sufficiently large $N$. This is the contradiction. Large rank can hide curvature in a subspace carrying only $2/N$ of the normalized trace.

**PROVED — the linear Gauss constraint does not remove the test.** On an even torus put $z_{x,i}I_2$ in the lower block, $z_{x,i}=(-1)^{\sum_{j<i}x_j}$. Each plaquette then has lower sign $-1$. Put $v_{x,i}=(-1)^{\sum_jx_j}a_iX$ in that block, with $a=(1,-1,0,0)$ and $X\in\mathfrak{su}(2)$ nonzero. Its covariant lattice divergence is zero because the lower adjoint transports are the identity and $\sum_i a_i=0$. It is therefore orthogonal to infinitesimal gauge transformations.

On lower traceless tangents the second Wilson variation divided by $N^2$ is $(2/\lambda)\sum_p|(dv)_p|^2$, where $d$ is the oriented lattice curl. Each central plaquette contributes the square of the signed sum of its velocities. Polarization gives $D_v b=(2/\lambda)d^*dv$ in the lower block, and direct differentiation produces no other component. For this alternating mode each forward difference multiplies by $-2$. In the curl square the resulting matrix on $a$ is $a_i\mapsto4\sum_j(a_i-a_j)=16a_i$. Hence $D_vb=(32/\lambda)v$. Normalize $E=1$. In the upper-block averaging argument of Lemma 5, the fixed weights $|v_e|^2$ now sum to one, and the scalar growth factor becomes $64/\lambda-1$. The same contradiction excludes the scalar weights through $\lambda=64$ even if this test is required only on divergence-free tangents. This test enforces the linear Gauss constraint. Realization as gradients of gauge-invariant scalars at the reducible field would be a further restriction.

**PROVED — Lemma 6 (a matrix test at order one and its counterexample).** There is one finite trace polynomial, with constants independent of rank, which gives $\mathcal G_N Q\le-E/4$ on both the preceding two-colour configuration and its positive-sign version, for every $\lambda\in[1,2]$ and every upper block $W$. Changing one distant lower-block link can give $\mathcal G_N Q\ge(24/\lambda-1)E$ instead.

*Construction.* For each link $e$ choose a plaquette $\sigma_e$ and an edge-simple rectangle $\gamma_e$ of length $s=1024$, sharing only $e$. Use a $1$ by $511$ rectangle in a different coordinate plane and translate these choices. Take $M>1026$ for this test. Base both holonomies at the head of $e$ with $U_e$ last. Write

$$
 P_e=(I-h_{\gamma_e})(I-h_{\sigma_e})v_e,\quad
 \epsilon=1/128,\qquad Q=\sum_e (|v_e|^2+\epsilon |P_e|^2).
$$

Here $|P|^2=\tau(P^*P)$. Thus $E\le Q\le(1+16\epsilon)E$. Use the one marked tangent of Lemma 5. Off the marked link every quadratic term and its generator vanish at this point, by (1).

*Negative sign.* Both holonomies act as $-I$ on the marked subspace. Therefore $P_e=4v_e$, and $|P_e|^2=16E$ attains its maximum with $|v_e|$ fixed. The base drift has zero first derivative there. Every horizontal second derivative is nonpositive, since its curve preserves $|v_e|$. On each of the $s-1$ exclusive rectangle links, the varying expression is exactly

$$
 |P_e|^2=8E-8\operatorname{Re}\tau(v_e^* h_{\gamma_e}v_e).
$$

Its horizontal Laplacian is $-8(1-N^{-2})E$ there by (3), since the link occurs once. The vertical drift on the marked tangent is $(12/\lambda-1/2)v_e$. Together these give

$$
 \frac{\mathcal G_NQ}{E}\le
 (24/\lambda-1)(1+16\epsilon)-8\epsilon(s-1)(1-N^{-2})<-1
$$

on $I$ already using $1-N^{-2}\ge3/4$. All bounds permit arbitrary unitary upper-block fields in the construction.

*Positive sign.* Put $+I_2$ on the marked link too. Then $(I-h_{\sigma_e})v_e=P_e=0$ and $\mathcal G_NE=(-1-24/\lambda)E$. The contribution from $|P_e|^2$ is $2\sum_{f,a}|Y_{f,a}P_e|^2$. Differentiating the long loop contributes zero. On each of the three short-loop links other than $e$, the sum over $a$ is at most $4E$, since $\sum X_a^*X_a=(1-N^{-2})I$ and $\|I-h_{\gamma_e}\|_{\rm op}\le2$. On $e$ there is also the rotation of $v_e$. Its summed squared length is $E/2$ by $\sum_a[X_a,[X_a,v_e]]=-2v_e$. The triangle inequality in the direct sum over $a$ bounds the square before multiplication by $I-h_{\gamma_e}$ by $(1+\sqrt2)^2E\le9E$. Thus $2\sum|Y P_e|^2\le2(3\cdot4+36)E=96E$. The choice of $\epsilon$ gives the claimed bound.

*Counterexample.* Restore $-I_2$ at $e$ and flip the lower sign at one distant exclusive link of $\gamma_e$, outside all plaquettes of $e$. The six local plaquettes still act as $-I_2$, while $h_{\gamma_e}$ now acts as $+I_2$. Hence $P_e=0$. A squared norm at zero has nonnegative diffusion generator, and (9) with unit weight gives $\mathcal G_NE=(24/\lambda-1)E$. This holds at arbitrarily large rank. By (5) the proposed $q$ also fails the leading inequality in (6). Thus the tested matrix weight reads the two colours, but its sign can be reversed by an independent exterior link. The counterexample concerns this weight only.

## 4. Which matrix direction carries positive curvature

**PROVED — Lemma 7 (a bound on the full Wilson Hessian).** For each incidence $e\in p$ put

$$
 u_{pe}=\Pi_0[(I-h_{p,e})v_e],\qquad \Pi_0 A=A-\tau(A)I,\qquad
 S=\sum_{p,e\in p}|u_{pe}|^2 .
$$

For every field, every tangent, every rank and every $\lambda>0$,

$$
 \mathcal G_NE\le -E+\frac{32\sqrt6}{\lambda}\sqrt{ES}
       \le-\tfrac34 E+\frac{6144}{\lambda^2}S.                     \tag{10}
$$

*Proof.* Along the product geodesic $U_e(t)=U_e\exp(tv_e)$, write an oriented plaquette as $h\exp(tA_1)\cdots\exp(tA_4)$. Each $A_i$ is the signed tangent conjugated by the remaining path to the base of $h$. Explicitly for a factor $L_i(t)=L_i\exp(tX_i)$ and suffix $C_i=L_{i+1}\cdots L_4$, use $A_i=C_i^{-1}X_iC_i$. For an inverse link $X_i=-U_ev_eU_e^*$. The second derivative of its real normalized trace is $\operatorname{Re}\tau$ applied to

$$
 h\left(\sum_i A_i^2+2\sum_{i<j}A_iA_j\right).
$$

With $h$ replaced by the identity it is $-|\sum_i A_i|^2$. In the difference, $\tau((h-I)A_i A_j)$ sees only $\Pi_0[(h-I)A_i]$ since $\tau A_j=0$. The latter matrix has norm $|u_{pe_i}|$. For a reversed occurrence this follows also from $|(h^{-1}-I)v|=|(h-I)v|$ and $\tau((h^{-1}-I)v)=-\overline{\tau((h-I)v)}$ for skew $v$. Bound the difference on $p$ by $2(\sum_{e\in p}|u_{pe}|)(\sum_{f\in p}|v_f|)$. Summing and applying Cauchy–Schwarz costs $8\sqrt{6ES}$ since six plaquettes meet each link. The second derivative of the log Wilson density divided by $N^2$ is $\sum_e\operatorname{Re}\tau(v_e^*D_vb_e)$. Its factor relative to the real normalized plaquette trace is $2/\lambda$. In (1) there is a further factor two on differentiating $E$. The rotations and commutator preserve length. This gives the first bound. Complete the square for the second.

**PROVED — Lemma 8 (an adjoint transport which survives every change of centre signs).** For each $e$ choose one edge-simple rectangle $\gamma_e$ through $e$ of even perimeter $s=2^{36}$. Take $M>s+2$ for this test. Set $T_e=\operatorname{Ad}_{h_{\gamma_e}}$, $\epsilon=2^{-22}$ and

$$
 B_{pe}=\tfrac14|u_{pe}+T_e u_{pe}|^2,\qquad
 Q=E+\epsilon\sum_{p,e\in p} B_{pe}.                               \tag{11}
$$

Then $E\le Q\le(1+24\epsilon)E$. For every $N\ge2$, $\lambda\in I$, if $T_eu_{pe}=u_{pe}$ at the field and tangent in question for every incidence, then $\mathcal G_NQ\le-E/2$ **at that point**. In particular this holds with arbitrary Wilson matrices in an upper block, arbitrary central signs in any even-dimensional lower block, and all $v_e$ supported and traceless in that lower block. The signs can vary from link to link. No invariance of this class under the diffusion is being used.

*Proof.* The identity $B_{pe}=|u_{pe}|^2-|u_{pe}-T_eu_{pe}|^2/4$ gives a sign when the two matrices agree. At such a point only sums of squared horizontal derivatives contribute to the generator of the subtracted square. At a link of $\gamma_e$ outside $p$, $u_{pe}$ is fixed. Differentiating $T_eu_{pe}$ is a conjugate of a commutator with an orthonormal basis. By (3),
$\sum_a|[X_a,u]|^2=2(|u|^2-|\tau u|^2)=2|u|^2$ for every traceless complex matrix $u$. Each exclusive link therefore subtracts $|u_{pe}|^2$ from $\mathcal G_N B_{pe}$, including the factor two for the generator of a squared norm. There are at least $s-4$ such links. All other subtracted terms have the same sign. Hence

$$
 \mathcal G_N\sum B_{pe}\le\mathcal G_NS-(s-4)S .
$$

For clarity, $|\mathcal G_NS|\le 2^{19}E$ on $I$ without any return assumption. Expand $|\Pi_0[(I-h)v]|^2=|(I-h)v|^2-|\tau((I-h)v)|^2$. The coefficient mass is at most 8 per incidence, with length at most 10. There are 24 incidences per site. On one monomial of length $d$, contracting the two horizontal insertions costs at most $2d^2$ in absolute coefficient mass, by (3). A drift insertion costs at most $145d$ on $I$. Indeed the coefficient mass of $b_e$ is at most $24/\lambda$, that of $D_vb_e$ at most $96/\lambda$, and that of $[v_e,b_e]$ at most $48/\lambda$. The last fibre coefficient is $1/2$. The translation estimate at the end of Lemma 3 now gives the bound since $192(200+1450)<2^{19}$. In (10), $\epsilon\,2^{19}=1/8$ and $\epsilon(s-4)>6144$. These inequalities prove the assertion. On the stated block configurations all lower holonomies are scalar and each marked $u$ stays inside this block, so the hypothesis holds.

**PROVED — the remaining colour misalignment can occur.** Take the same single defective link and traceless two-colour tangent as in Lemma 5, now $v_e$ proportional in the lower block to $i\,\mathrm{diag}(1,-1)$. Set one distant exclusive link of $\gamma_e$, outside all six plaquettes of $e$, to have lower block

$$
 R=\begin{pmatrix}0&1\\-1&0\end{pmatrix}.
$$

It conjugates $v_e$ to $-v_e$. At all six incidences $u_{pe}=2v_e$ and $T_eu_{pe}=-u_{pe}$. Every added square in (11) vanishes. Its generator is nonnegative there. Thus $\mathcal G_N Q\ge(24/\lambda-1)E$. This exact configuration disproves (6) for (11) as $N$ grows. Lemma 8 repairs the centre-sign failure of Lemma 6, even for many defective links and simultaneous tangent directions. A single noncentral transport still defeats it. Equation (10) locates what a successful weight must control without assuming colour alignment.

## 5. What the actual equilibrium saddle equations control

**PROVED — Lemma 9 (conditional concentration of the loop equation).** Fix a positive link $e$ and a real or imaginary part $F$ of a normalized Wilson word of length $j\ge1$. Let $A=\mathcal L_eF$, using only the Laplacian and drift at $e$. Let $A_0$ be its leading expression obtained from (3) as in Lemma 3. Fix all other links and denote the conditional Wilson probability by $\mu_e$. For every exterior, $z>0$, rank and volume,

$$
 \mu_e\{|A_0|>z+2j^2/N^2\}
 \le 2\exp[-N^2z^2/(2K_j)],\qquad
 K_j=j(j+4)(2j^2+24j/\lambda).                                    \tag{12}
$$

*Proof.* Conditional integration by parts gives $\mu_e A=0$ and

$$
 \mu_e[A\exp(tA)]
 =-t\,\mu_e[\exp(tA)\langle\nabla_e F,\nabla_e A\rangle].
$$

The dual gradient of $F$ is at most $j/N$. The polynomial for $A$ has length at most $j+4$ and coefficient mass at most $2j^2+24j/\lambda$ by the same two insertions and the bound on $b_e$. A product of traces of total length $d$ has dual gradient at most $d/N$, by the product rule and the unitary norm bound. Thus $|\langle\nabla_e F,\nabla_e A\rangle|\le K_j/N^2$. Integration of the logarithmic moment bound from zero gives $\mu_e\exp(tA)\le\exp(t^2K_j/(2N^2))$ for real $t$. Apply Markov's inequality to $A$ and $-A$ and optimize $t$. Finally $|A-A_0|\le2j^2/N^2$ holds pointwise by (3). This proves (12) without an assumption on the exterior distribution.

**PROVED — Theorem 10 (exponentially small connected sets of violations at order one).** At each positive link $e$ choose one incident plaquette by a fixed orientation rule. Use $F_e=\operatorname{Re}\tau h_{p(e),e}$ in (12). Put $h=h_{p(e),e}$. The scalar leading residual is explicitly $A_{0,e}=-\operatorname{Re}\tau h+\operatorname{Re}\tau(hb_e)$. Call $e$ bad if $|A_{0,e}|>z+1/N^2$. For every $\lambda>0$, $M\ge3$, $z>0$ and

$$
 N\ge\max\{2,\lceil\sqrt{2(1+24/\lambda)(\log 2+19\log 36)}/z\rceil\},
$$

the probability in the **equilibrium Wilson law** of a path of distinct bad links of length $r$ from any fixed link is at most $2^{-r}$ for all integers $r\ge0$. Length counts graph steps. This statement concerns the displayed local polynomial. For example at the identity field its leading value is $-1$, so a small fixed tolerance is a substantive test.

*Proof.* The selected plaquette admits a sharper constant than the all-word bound. Here $A_e=\mathcal L_eF_e=A_{0,e}+F_e/N^2$ exactly, by $\sum_a X_a^2=-(1-N^{-2})I$. At fixed exterior, $D_{e,X}h_{q,e}=h_{q,e}X$ for every incident plaquette. The orthogonal projection $\pi$ gives $|b_e|\le12/\lambda$ and $|D_{e,X}b_e|\le(12/\lambda)|X|$. Differentiating $\operatorname{Re}\tau(hb_e)$ therefore costs at most $(24/\lambda)|X|$. The two dual gradient bounds in the proof of (12) are now $1/N$ and $(1+24/\lambda)/N$. Thus the conditional bad probability is at most $p=2\exp[-N^2z^2/(2(1+24/\lambda))]$. Its event depends only on the link and the links on its incident plaquettes. The link graph has degree at most 18. Greedily select at least $(r+1)/19$ pairwise nonadjacent links on a specified path. The events for all other selected links are measurable off the link being tested. Successive conditional integrations therefore bound the joint probability by $p^{(r+1)/19}$. At most $18^r$ paths start at the root. The rank bound gives $18p^{1/19}\le1/2$, which proves the result. A union over a prescribed finite set of word tests at each link also follows by adding their conditional failure probabilities and counting their enlarged neighbourhoods.

**ARGUED — relation to the missing estimate.** The equilibrium law obeys the matrix loop equations to accuracy $O(1/N)$ in each fixed normalized-trace test, uniformly even after the exterior is fixed. There is no estimate here for how many different tangent responses can obey the same trace tests. In Lemma 5 the two-colour block changes each fixed unmarked trace polynomial by $O(1/N)$ while it changes the sign of tangent growth.

**PROVED — a contact identity.** If $H$ does not read $e$, then $\mu(A_eH)=0$ by conditional integration. Consequently $\operatorname{Cov}(A_{0,e},H)=-N^{-2}\operatorname{Cov}(F_e,H)$. Applying this twice to separated non-neighbouring roots gives $\operatorname{Cov}(A_{0,e},A_{0,f})=N^{-4}\operatorname{Cov}(F_e,F_f)$. Replacing the target by covariance decay of the residuals would be equivalent at fixed rank. Theorem 10 controls connected sets of large residuals and leaves (6) to be proved.

**PROVED — Lemma 11 (a specified colour direction, with a sharp quantifier).** In (12) one can test a rank-$k$ subspace, $1\le k\le N$, by taking

$$
 F=\operatorname{Re}\frac1k\operatorname{Tr}(P W)
 \quad\hbox{or}\quad \operatorname{Im}\frac1k\operatorname{Tr}(P W).
$$

Here $P$ is any orthogonal rank-$k$ projection, possibly chosen as a measurable function of all the exterior links. The word $W$ has length $j$. Hold $P$ fixed when applying $\mathcal L_e$. The same bound (12) holds with $Nk$ in place of $N^2$ in the exponential and the same shift $2j^2/N^2$. In particular a specified two-colour probe has exponential concentration in $N$ at $\lambda=1$.

*Proof.* Insert $C=(N/k)P$ once in the trace. For any unitary word $V$, $|\tau(CV)|\le1$ by the trace norm of $C$. Its Hilbert–Schmidt length in the normalized trace is $\sqrt{N/k}$. In differentiating a product of traces with this one insertion, an insertion of a unit tangent in the marked trace costs at most $1/\sqrt{Nk}$ by Cauchy–Schwarz. In another trace it costs at most $1/N$. In (3) each resulting term still has just one $C$. The earlier coefficient bounds and the pointwise remainder therefore hold with no change. Both dual gradients in the conditional integration by parts carry $1/\sqrt{Nk}$. This proves the assertion. Only integration in $U_e$ was used, so exterior-dependent choices of $P$ need no regularity.

For even $N$ no uniform operator-norm version with a vanishing error can hold for all exteriors. Fix the six three-link staples so that three are $I$ and three are $-I$. They can be prescribed independently by one exclusive link on each path, and $-I\in SU(N)$. Their sum is zero. The conditional law of $U_e$ is Haar at every $\lambda$. Take a plaquette with positive staple, so $h=U_e$ in this exterior. Its entrywise leading one-link equation has residual $-h$, of operator norm one for **every** $U_e$. A rank-one eigenprojection chosen after seeing $U_e$ reads a complex diagonal entry of modulus one. This explains exactly why the exterior can choose the probe but the updated link cannot. The example holds at the target coupling without taking a strong-coupling limit.

**PROVED — Corollary 12 (an equilibrium matrix saddle exists on local words).** Fix any $\lambda>0$. Take any sequences $N_j\to\infty$, $M_j\to\infty$ and draw one periodic Wilson field at each pair. The distributions of all its normalized word traces have subsequential limits. Every such limit is carried by positive normalized tracial functionals satisfying all the local leading Wilson equations

$$
                   (\mathcal L_{0,e}F)(t)=0                         \tag{13}
$$

simultaneously for every finite word $F$ and every link $e$. Here $t$ assigns a moment to each word, and a product of traces in $\mathcal L_{0,e}F$ is evaluated as the product of the corresponding moments of that **same** $t$.

*Proof.* Label the countably many finite words in the oriented edges of $\mathbb Z^4$ and their inverses. Reduce their offsets modulo $M_j$ to evaluate them. The vector of their normalized traces lies in a countable product of closed unit disks, a compact metric space. Probability laws on it have weakly convergent subsequences. Cyclicity, the unit and adjoint rules, and positivity of $\tau(P^*P)$ for word polynomials with rational complex coefficients pass to the limit on a closed set of full measure. Density of those coefficients gives positivity for every finite polynomial. Each chosen local stencil stops wrapping as $M_j$ grows. Its leading equation is a continuous polynomial of finitely many coordinates, obtained from (3). Inequality (12), integrated in the exterior, sends its residual in probability to zero. Its limit must be zero almost surely. Intersect these full-measure events over the countable real and imaginary word tests and the links. This proves (13). Evaluating products after averaging the coordinates of different solutions can change (13).

**ARGUED — replacement for the vector saddle.** The object constructed here is a law on tracial states of link matrices. It retains closed words, their products, and the equations which split one trace into two. The marked words of Lemma 3 describe the response to a colour perturbation. Corollary 12 does not require uniqueness or equilibrium factorization. To select a massive phase, these stationary equations need a stability estimate on the marked response. Equation (6) specifies one such estimate and (8) gives the finite-rank price.

**PROVED — Lemma 13 (a signed step in the Wilson law).** Fix $\lambda\in[1,2]$, $N\ge2$, any volume and any nonempty set $B$ of links. Fix the exterior and a tangent $v$ supported in $B$, chosen using only that exterior. Sample $U_B$ from its actual conditional Wilson law, then evolve the full lifted diffusion (1), including all exterior links. For $0\le t\le2^{-22}$,

$$
              \mathbb E E(v_t)\le(1-t/2)E(v).                     \tag{14}
$$

The initial conditional average has a stronger exact sign. If $\Phi$ denotes the full Wilson log weight, then

$$
 \mathbb E[\mathcal G_NE(U,v)]
       =-E(v)-2N^{-2}\mathbb E[(D_v\Phi)^2].                       \tag{15}
$$

*Proof.* Right translation on the product of links in $B$ preserves its Haar measure. Along this translation $v$ is constant. Integrate $D_v[(D_v\Phi)e^\Phi]$ in this conditional product to get $\mathbb E D_v^2\Phi=-\mathbb E(D_v\Phi)^2$. Now $D_v^2\Phi/N^2=\sum_e\operatorname{Re}\tau(v_e^*D_vb_e)$, which proves (15) by (1). This sign includes plaquettes crossing the boundary of $B$.

For an explicit time, expand $\mathcal G_NE=-E+2\sum_e\operatorname{Re}\tau(v_e^*D_vb_e)$. Its coefficient mass per site is at most $4+768/\lambda<2^{10}$ and its word lengths are at most six. Applying the drift and diffusion count in Lemma 8 once gives $|\mathcal G_N^2E|\le2^{20}E$ since $2\cdot6^2+145\cdot6<2^{10}$. Lemma 2 bounds $E(v_t)\le e^{95t}E(v)$ pathwise on $I$, using the squared $\ell^2$ bound on $K_t$. Integrate the generator twice from the random initial field. The Taylor remainder after (15) is at most $2^{19}t^2e^{95t}E(v)$. For the stated times $95t\le1/2$ and $e^{95t}\le2$. This proves (14). After one step the transported direction depends on the updated links in $B$. Applying (14) a second time to that direction would require a new premise. The estimate is in Langevin time and carries no equilibrium spatial decay rate by itself.

## 6. A large-rank estimate on the actual curvature

**PROVED — Theorem 14 (conditional curvature tail in four dimensions).** Make the same exterior choice as in Lemma 13. Put $T=\sum_e\operatorname{Tr}(v_e^*v_e)>0$, $V=\max_e\|v_e\|_{\rm op}$ and $r_v=T/V^2$. For every $\lambda>0$ and $\alpha>0$ the conditional Wilson law obeys

$$
 \Pr\{D_v^2\Phi\ge\alpha NT\mid U_{B^c}\}
 \le 2\exp[-\lambda\alpha^2 N r_v/512].                            \tag{16}
$$

In particular the probability that $\mathcal G_NE>-E/2$ is at most $2\exp[-\lambda N r_v/8192]$. This includes the mixed Hessian terms from all plaquettes meeting the support. At $\lambda=1$ an adverse response in even a specified two-colour plane is exponentially unlikely in $N$. One may select among $K$ exterior-specified tests after seeing the field by multiplying the largest failure bound by $K$.

*Proof.* Translate every active link by $U_e\exp(sv_e)$, holding the exterior fixed. This map and its inverse preserve product Haar measure in $B$. The fourth derivative of the log weight on this path satisfies

$$
              |D_v^4\Phi|\le 768 N V^2 T/\lambda .                  \tag{17}
$$

For each plaquette there are $4^4$ ordered choices of the factors for the four derivatives. In any term, bound the first two chosen insertions by their unnormalized Hilbert–Schmidt norms and the other two by $V$. Split the cyclic trace between the first two insertions and apply Hilbert–Schmidt Cauchy–Schwarz, also when the factors repeat. Unitary multipliers and the signs from inverse links preserve these bounds. With $T_e=\operatorname{Tr}(v_e^*v_e)$ the product costs at most $V^2(T_i+T_j)/2$. Summing over all ordered quadruples gives $64V^2\sum_{e\in p}T_e$ on one plaquette. Six plaquettes share an edge and the coefficient in $\Phi$ is $2N/\lambda$. This proves (17).

At any point of the event in (16), the average of the log weights at shifts $+s$ and $-s$ exceeds the current log weight by at least $NT(\alpha s^2/2-32s^4V^2/\lambda)$, by Taylor's formula with a bounded fourth derivative. Set $s^2=\lambda\alpha/(128V^2)$. At least one sign increases the log weight by $\lambda\alpha^2Nr_v/512$. Partition the event by a winning sign, using a fixed tie rule. Translate each part separately and bound its new integral by the full conditional partition function. Division by that same positive partition function proves (16). Since $\mathcal G_NE/E=-1+2D_v^2\Phi/(NT)$, the stated instance uses $\alpha=1/4$.

**PROVED — Corollary 15 (an exact sign reversal and a path bound).** At one link take $v=i(P_+-P_-)$ for orthogonal projections of the same rank and let $k=\operatorname{Tr}(P_++P_-)>0$. Keep the projections fixed by the exterior. For every $\lambda>0$ and $\alpha>0$,

$$
       \Pr\{D_v^2\Phi\ge\alpha Nk\mid U_{\ne e}\}\le (1+e^{2\alpha Nk})^{-1}.
                                                                    \tag{18}
$$

For a fixed choice of these planes at every link, the probability of a self-avoiding path of length $n$ from a specified link on which every link violates this threshold is at most $18^n\exp[-2\alpha Nk(n+1)/19]$ if the ranks are at least $k$. This gives exponential spatial decay of these adverse-curvature paths for $2\alpha Nk>19\log18$.

*Proof.* On each right orbit of the circle $\exp(sv)$, the action is $c+a\cos(s-\varphi)$ with $a\ge0$. Indeed the eigenvalues of the acting matrix are $1,e^{is},e^{-is}$ and all six incident terms are linear in $U_e$ in the chosen orientation. The half-turn is the determinant-one involution $U_e\mapsto U_e(I-2P_+-2P_-)$. It changes $D_v^2\Phi=-a\cos(s-\varphi)$ to its negative and raises $\Phi$ by exactly $2D_v^2\Phi$. If $\nu$ is the conditional distribution of this curvature, Haar invariance gives $\nu(-dx)=e^{2x}\nu(dx)$. For $x\ge\alpha Nk$ the image event is disjoint and has at least $e^{2\alpha Nk}$ times the original mass. This proves (18). The same exact sign reversal holds for simultaneous balanced probes, fixed by the exterior, on any family of links of which no two share a plaquette: each changing plaquette then has only the first harmonic. The path bound follows by the nonadjacent selection in Theorem 10. Fixed plane choices may also read the other links in their own plaquette star, because those reads still allow the same conditional integrations.

**PROVED — simultaneous adaptive bound for one link.** For $\lambda\in[1,2]$ and $N\ge384$, set $k_0=2\lfloor N/2\rfloor$. Conditional on any exterior, the probability that **there exists** a single-link tangent with $r_v\ge(1-1/384)N$ and $\mathcal G_NE\ge-E/2$ is at most

$$
                        (1+\exp[Nk_0/4])^{-1}.
$$

The tangent can be chosen after reading the updated matrix. This statement covers arbitrary skew traceless tangents in the indicated class.

*Proof.* Set $K=(1/2)\sum_{p\ni e}(h_{p,e}+h_{p,e}^*)$, so $\|K\|_{\rm op}\le6$. For a one-link tangent write $W=v^*v/\operatorname{Tr}(v^*v)$. Then $D_v^2\Phi/(NT)=-(2/\lambda)\operatorname{Tr}(WK)$ by a second derivative at that link. The matrix $W$ has trace one and $0\le r_vW\le I$. Thus $I/N$ is a convex combination of $W$ with weight $r_v/N$ and another density matrix (at $r_v=N$ it equals $W$). It follows that $\|W-I/N\|_1\le2(1-r_v/N)$. For one fixed balanced rank-$k_0$ probe with support $P_0$, the same argument gives $\|P_0/k_0-I/N\|_1\le2/N$. The two normalized curvatures differ by at most $(24/\lambda)(1/384+1/N)\le1/8$. Therefore any probe in the stated class with normalized curvature at least $1/4$ forces the fixed probe's curvature to be at least $1/8$. Apply (18) to that fixed probe. This uses neither a net of directions nor a bound on how the tangent was selected. Theorem 20 treats an adaptive two-colour plane. The mixed-link Hessian for the transported tangent is still uncontrolled.

**ARGUED — the limit of this gain.** Equations (14) and (16) control the signed response over a short Langevin step and under two opposite displacements at order-one coupling. The result above also permits fully adaptive one-link probes of high effective rank. In (2), the direction after one evolution step depends on these same links. A volume-uniform estimate for that dependence is missing. The concrete exterior rotation in Lemma 8 defeats a pointwise attempt to remove it. Neither a one-step gain nor the absence of long adverse paths in fixed planes proves exponential decay for the physical observable.

**PROVED — Lemma 16 (cost of choosing the direction from the updated links).** On a block with exterior fixed, allow a tangent $v(U)$ supported in the block to depend on its own interior. Always take $D_v^2\Phi$ with $v$ frozen at the sampled point. Suppose $T(U)\ge T_0>0$ and $V(U)\le V_0$. Let $F_s(U)_e=U_e\exp(sv_e(U))$. If the pushforwards of product Haar under $F_s,F_{-s}$ have densities at most $J$, the proof of Theorem 14 gives

$$
 \Pr\{D_v^2\Phi\ge\alpha NT(U)\}
 \le 2J\exp[-\alpha s^2 NT_0/4],\qquad
 0<s^2\le\lambda\alpha/(128V_0^2).                                 \tag{19}
$$

Indeed each winning shift raises the action by at least the exponent in (19). The integral of its translated weight costs at most $J$ times the original partition function.

Two classes admit explicit bounds. First, order the active links. At each link choose right or left multiplication by the exponential of a matrix depending only on the exterior and the earlier links. For a left multiplication take the matching right-frame tangent $v_e=U_e^*w_eU_e$. Integration in reverse order shows $J=1$ for both shifts. A probe can in this way read every earlier updated link. This is the triangular integration principle used for Gaussian coordinates in the lane's Lemma 7 of [in1.md](in1.md), here applied to the two Wilson shifts.

Second, suppose $v$ is smooth. In left frames let $D v$ be its derivative as a map into the fixed product Lie algebra. Assume operator norm at most $L$ and real rank at most $h$ at every point. For $0<s$ and $sL<1$ take $J=(1-sL)^{-h}$. If the directed graph $f\to e$ of permitted derivative blocks $D_f v_e$ has no cycle of length less than $g$, one can instead take

$$
             \log J\le \frac{h(sL)^g}{g(1-sL)}.                     \tag{20}
$$

A self-read counts as a cycle of length one. In particular a fixed finite number of normalized trace coordinates can be read without a rank-sized Jacobian cost if $L$ stays bounded, since $h$ is then at most the number of coordinates.

*Proof of the Jacobian bounds.* The left-frame differential of $F_s$ at a velocity $y$ is the blockwise isometry $Oy=(\operatorname{Ad}_{\exp(-s v_e)}y_e)_e$, plus $sB\,Dv[y]$. Here $B$ is block diagonal with each block the integral of $\operatorname{Ad}_{\exp(-t s v_e)}$ for $0\le t\le1$, of norm at most one. This follows by differentiating the matrix exponential under its integral formula. Thus the relative Jacobian is $\det(I+sA)$ where $A=O^{-1}BDv$, with rank at most $h$ and norm at most $L$. Its absolute value is at least $(1-sL)^h$ by the eigenvalue product. If two images agree, left invariance bounds the distance between their preimages by $s\|v(x)-v(y)\|\le sL\,d(x,y)$. Since $sL<1$, the two preimages agree. The distance estimate uses the same contraction formula for the derivative of the exponential. The invertible derivative makes the image open, and compactness makes it closed. Thus a change of variables gives the density bound. In (20) block diagonality preserves the directed graph. The trace of $A^j$ vanishes for $1\le j<g$, since a contributing sequence of blocks must close. The other traces have absolute value at most $h L^j$ by the eigenvalue bound. Apply the convergent power series for $\log\det(I+sA)$ and sum the tail. All determinant traces here are ordinary real traces of tangent operators.

**PROVED — Corollary 17 (a nonabelian cycle of adaptive probes).** Choose $m\ge3$ distinct links in a directed cycle and fixed traceless skew matrices $Z_j$ with $k$ nonzero eigenvalues, all of modulus one. Set $v_j=U_{j-1}Z_jU_{j-1}^*$ cyclically, and set other tangents to zero. In particular the four links of a plaquette can be used. Uniformly in all exteriors, volumes and $\lambda\in[1,2]$,

$$
             \Pr\{\mathcal G_NE\ge-E/2\}\le 2\exp[-Nmk/2^{23}].     \tag{21}
$$

Equations (14) and (15) also hold for this field-dependent initial direction.

*Proof.* Here $T=mk$, $V=1$, $L\le2$. Each nonzero derivative block is a conjugated commutator with $Z_j$. Its real rank is at most $2Nk$ since matrices acting within the kernel of $Z_j$ commute with it. For $k=N$ the bound follows directly from the dimension. Thus $h\le2Nmk$. Use (19) with $\alpha=1/4$, $s=1/512$, and (20) with $g=3$. The action gain is $s^2Nmk/16$. The log Jacobian costs at most $(32/3)Nmk\,s^3$, at most half the gain. This proves (21). Moreover $\log|\det DF_s|=O(s^3)$ at zero on this finite compact block. Differentiate the exact identity $\int e^{\Phi(F_sU)}|\det DF_s|\,dU=\int e^\Phi dU$ twice at zero. The Jacobian contributes neither a first nor a second derivative, so the square identity (15) survives. Since $E$ is constant on the block, the same bounded-time Taylor argument proves (14).

**PROVED — reciprocal reads are a real cost.** For a smooth field with no self-reads, the second-order Jacobian term is exactly $-\operatorname{Tr}_{\mathbb R}((Dv)^2)s^2/2$ in $\log|\det DF_s|$. The linear trace vanishes for all $s$ by the zero diagonal blocks. Hence after conditional integration (15) acquires the extra term $2N^{-2}\mathbb E\operatorname{Tr}_{\mathbb R}((Dv)^2)$. Here $-E(v)$ in (15) is replaced by $-\mathbb E E(v)$ if the energy varies. Only mutually dependent pairs contribute to the new term. Its sign can be positive. At $U_e=U_f=I$ take $v_e=U_f ZU_f^*$ and $v_f=-U_e ZU_e^*$ with $Z=i(P_+-P_-)$ as in Corollary 15, of total rank $k$. The two derivative blocks are $-\operatorname{ad}_Z$ and $+\operatorname{ad}_Z$. Diagonalize $Z$ with imaginary entries $iz_j$. Then $-\operatorname{Tr}_{\mathbb R}(\operatorname{ad}_Z^2)=\sum_{i,j}(z_i-z_j)^2=2Nk$. The trace for the pair is $4Nk$. This reaches the scale of the curvature gain in the shift argument. On the same plaquette the drift at $e$ reads $f$ and the drift at $f$ reads $e$. This reciprocal pair enters at second order. No uniform bound on the resulting signed response of the true transported tangent is proved here.

**PROVED — Lemma 18 (the actual reciprocal Wilson derivative).** Let distinct links $e,f$ share exactly one plaquette $p$. Use the left frames of Lemma 1 and set $H=(h+h^*)/2$ for $h=h_{p,e}$. The real tangent trace of the reciprocal derivative blocks of the **Wilson drift itself** is

$$
 \operatorname{Tr}_{\mathbb R}(D_f b_e\,D_e b_f)
 =\frac4{\lambda^2}\left[
 \frac{N^2}{2}\{1+\operatorname{Re}[(\tau h)^2]\}
             -2\tau(H^2)+(\tau H)^2\right].                        \tag{22}
$$

Thus this part of the leading cost is an explicit scalar plaquette expression. Its remainder inside the brackets has absolute value at most two. At $h=I$ the exact cost is $4(N^2-1)/\lambda^2$. A sign or rank gain for an individual reciprocal pair cannot be assigned from counting two different links.

*Proof.* The two link derivatives commute on scalar functions. Differentiate the Wilson gradient pairing to obtain $D_e b_f=(D_f b_e)^*$ in the real link metrics. In the one common plaquette, differentiating $h$ inserts $\pm X$ between two unitary factors $A,B$ with $AB=h$. Since $A X B=(\operatorname{Ad}_A X)h$, the required trace is $4/\lambda^2$ times the squared real Hilbert–Schmidt norm of $X\mapsto\pi(Xh)$ on the Lie algebra. For one basis element from (3),

$$
 |\pi(X_a h)|^2=
 \tfrac12\{|X_a h|^2-\operatorname{Re}\tau(X_a h X_a h)\}
       -(\operatorname{Im}\tau(X_a h))^2 .
$$

The three sums over $a$ on the right use
$\sum|X_a h|^2=1-N^{-2}$,
$\sum\tau(X_a h X_a h)=-(\tau h)^2+N^{-2}\tau(h^2)$, and
$\sum(\operatorname{Im}\tau(X_a h))^2=N^{-2}[\tau(H^2)-(\tau H)^2]$,
the last by applying (3) to the Hermitian matrix $H$. Multiply by $N^2$ to convert normalized squared length to link-metric squared length and use $2\tau(H^2)=1+\operatorname{Re}\tau(h^2)$. As a second algebra check, diagonalize $h$ with phases $\theta_j$. On the real off-diagonal pair $i,j$ the map multiplies squared length by $\cos^2[(\theta_i+\theta_j)/2]$. On the diagonal it is the compression of $\operatorname{diag}(\cos\theta_j)$ to the traceless hyperplane. Their squared Hilbert–Schmidt norms sum to (22) after multiplication by $4/\lambda^2$. This evaluates a drift derivative. The derivative of the tangent after an arbitrary time also depends on its history.

## 7. What happens when one link chooses its own colour plane

**PROVED — Theorem 19 (all tangent directions for a low-rank staple).** Fix $\lambda\in[1,2]$, a link $e$, and its exterior. Absorb the Wilson coefficient in the staple matrix $A=(2/\lambda)\sum_{p\ni e} A_p$, where $h_{p,e}=A_pU_e$. The conditional density of $U=U_e$ is proportional to $\exp[N\operatorname{Re}\operatorname{Tr}(AU)]$. Suppose $\operatorname{rank}A=r\ge1$ and $N>2r$. Set $\varepsilon=2^{-14}$. Except on an event of conditional probability at most

$$
 \exp\!\left[48r^2+2r^2\log(128\sqrt r/\varepsilon)
                  -(N-2r)\varepsilon^2/8\right],                    \tag{23}
$$

every tangent $v$ supported on this link satisfies $\mathcal G_NE(v)\le-E(v)/62$ at once. It may be chosen after observing $U$. For $r=0$ the exact result is $-E(v)$. Thus the rank needed at a prescribed error probability grows at most as a constant times $r^2\log(2r)$ plus a constant times the logarithm of the inverse error. The estimate is uniform over all exteriors of the stated rank and all volumes.

*Reduction to a small matrix.* Write a singular value decomposition for $A$. Since $r<N$, adjust phases on its kernel and cokernel so that both unitary factors are special unitary. Absorb them by left and right Haar translations of $U$, conjugating its tangent at the same time. We can now use $A=\operatorname{diag}(S,0)$ with $S=\operatorname{diag}(s_1,\ldots,s_r)$ and $0<s_i\le12$. Write $Z$ for the first $r$ rows and columns of $U$.

Under unweighted Haar the density of $Z$, relative to flat complex matrix volume, is proportional to $\det(I-ZZ^*)^{N-2r}$ on $\|Z\|_{\rm op}<1$. Here is a derivation. The first $r<N$ columns form a uniform orthonormal frame. Haar on $U(N)$ gives the same columns, since multiplication of its last column by the inverse determinant gives a left $SU(N)$-invariant probability on $SU(N)$. The next column is uniform on the unit sphere in the orthogonal complement of the previous columns. The first $r$ coordinates from a uniform complex sphere in dimension $d>r$ have density proportional to $(1-\|y\|^2)^{d-r-1}$. Indeed the parts of a radial complex Gaussian in $r$ and $d-r$ coordinates have independent squared radii with densities proportional to $t^{r-1}e^{-t}$ and $t^{d-r-1}e^{-t}$. Changing to their sum and ratio and integrating the radius gives the stated ball density. After $j-1$ columns the projection onto the first $r$ rows of the remaining orthogonal complement has Gram matrix $C_{j-1}=I-\sum_{i<j} z_i z_i^*$ for the truncated columns $z_i$. Thus $z_j$ has the law of $C_{j-1}^{1/2}y$ with $d=N-j+1$. The complex change of variables costs $(\det C_{j-1})^{-1}$. The identity $\det C_j=\det C_{j-1}(1-z_j^*C_{j-1}^{-1}z_j)$ gives by induction the joint density proportional to $(\det C_j)^{N-r-j}$. Taking $j=r$ proves the formula.

*Stability at the saddle.* Define
$F(Z)=\operatorname{Re}\operatorname{Tr}(SZ)+\log\det(I-ZZ^*)$ and $C=\operatorname{diag}(c_i)$ by $s_i=2c_i/(1-c_i^2)$, $0\le c_i<15/16$. The bound on $c_i$ follows by substituting $15/16$ and using $s_i\le12$. At $C$ the derivative of $F$ vanishes. Indeed the log determinant equals $\log\det B(Z)$ for the Hermitian block matrix with diagonal blocks $I,I$ and upper right block $Z$. Its derivative at $C$ is $-2\operatorname{Re}\operatorname{Tr}[C(I-C^2)^{-1}dZ]$. Along an affine path with velocity $Y$, the negative second derivative is $\|B^{-1/2}dB[Y]B^{-1/2}\|_{\rm HS}^2$. Here $\|\cdot\|_{\rm HS}$ uses the ordinary unnormalized trace. Since $0<B\le2I$, this is at least $\|Y\|_{\rm HS}^2/2$. If $\|Z-C\|_{\rm HS}\le1/32$, it is at most $2048\|Y\|_{\rm HS}^2$ since $B\ge I/32$. Integration on the segment from $C$ gives a loss $F(C)-F(Z)\ge\|Z-C\|_{\rm HS}^2/4$ everywhere and a loss at most $1024\|Z-C\|_{\rm HS}^2$ on that small ball.

The density with the Wilson weight is proportional to $e^{(N-2r)F(Z)}e^{2r\operatorname{Re}\operatorname{Tr}(SZ)}$. The ratio of the largest to smallest value of the last factor is at most $e^{48r^2}$. Bound the integral outside the $\varepsilon$ ball about $C$ by its largest exponential times the volume of the ball of radius $\sqrt r$ about zero. Bound the full integral below using the ball of radius $\varepsilon/128$ about $C$. Their real dimension is $2r^2$. The two loss bounds give (23).

*All colours at once.* Put $R_Z=(I-ZZ^*)^{1/2}$. A rotation on the remaining $N-r$ coordinates puts the nonzero part of $H=(AU+U^*A^*)/2$ in the form

$$
 \frac12\begin{pmatrix}SZ+Z^*S&SR_Z\\ R_ZS&0\end{pmatrix}.
$$

Indeed the first $r$ rows outside $Z$ have product with their adjoint equal to $R_Z^2$. At $Z=C$ the two eigenvalues for colour $i$ are $s_i(c_i\pm1)/2$. The least is at least $-15/31$, since $s_i(1-c_i)/2=c_i/(1+c_i)$. For $\|Z-C\|_{\rm HS}\le\varepsilon$, one has $\|R_Z-R_C\|_{\rm op}\le8\varepsilon$. To see this, solve $R_Z X+X R_C=C^2-ZZ^*$ by integrating $e^{-tR_Z}(C^2-ZZ^*)e^{-tR_C}$ from zero to infinity. Both square roots exceed $I/8$ and the right side has norm at most $2\varepsilon$. The Hermitian block matrix changes in operator norm by at most $12\varepsilon+48\varepsilon$. For every nonzero one-link tangent its normalized curvature is $D_v^2\Phi/(NT)=-\operatorname{Tr}(v^*v H)/T$, where $T=\operatorname{Tr}(v^*v)$. Hence $\mathcal G_NE/E\le-1/31+120\varepsilon\le-1/62$. This proves the simultaneous statement. No prevalence of low-rank staples in the Wilson lattice has been assumed or proved.

**PROVED — Theorem 20 (an adaptive two-colour perturbation really expands).** For every $\lambda\in[1,2]$, every $M\ge3$, and every even $N\ge8192$, there are exteriors for which the conditional Wilson probability that some balanced two-colour tangent on one link satisfies $\mathcal G_NE\ge E/20$ is at least

$$
 1-\min\{1,\exp[-2^{-32}N^2+N(\log N+7)]\}.                       \tag{24}
$$

Thus the probability of expansion tends to one for these exteriors. Corollary 15 suppresses expansion exponentially for each prescribed plane in exactly the same law. Corollary 21 shows that the expansion persists for a positive Langevin time, when that plane provides the initial tangent.

*Realization on the four-dimensional lattice.* Put $\gamma=3/4$. Set three of the six staples $A_p$ equal to a special unitary diagonal matrix with half its entries $e^{i\phi}$ and half $e^{-i\phi}$. Set the other three to its adjoint, with $\cos\phi=\lambda/16$. Each staple has its own parallel link across its plaquette. Assign these six links separately, using inverses as required, with all other exterior links equal to $I$. This gives $A=\gamma I$ in Theorem 19. Under this conditional law the observed matrix has density proportional to $e^{\gamma N\operatorname{Re}\operatorname{Tr}U}$. If two eigenvalues of $U$ have real parts at most $-7/10$, take $v=i(P_1-P_2)$ on the two eigenvectors. Then $D_v^2\Phi/(NT)\ge21/40$, so $\mathcal G_NE/E\ge1/20$.

*An angular estimate with explicit error.* First take the same tilt on $U(N)$. Write $z_j=e^{i\theta_j}$ and use uniform angle probability $d\ell=d\theta/(2\pi)$. The unnormalized joint law of the eigenangles relative to $d\ell^N$ has density

$$
 \exp\!\left[\gamma N\sum_j\cos\theta_j\right]\prod_{i<j}|z_i-z_j|^2 .
$$

For completeness, diagonalization on the distinct-eigenvalue set separates the diagonal derivatives $i z_j\,d\theta_j$ from the off-diagonal eigenbasis derivatives with entries $(z_i-z_j)X_{ij}$. Each off-diagonal complex coordinate gives the squared modulus in the volume element. Repeated eigenvalues form a lower-dimensional set, by the same diagonalization with the increased stabilizer dimension. The eigenbasis volume and permutation factors cancel in probability ratios.

The comparison density relative to $d\ell$ is $\rho(\theta)=1+\gamma\cos\theta$. This is the full-support one-matrix saddle from the two-dimensional calculation credited in the repo search. Only one angular consequence is used here. Write $u_j=N^{-1}\sum_i z_i^j$ and $\rho_j=\int e^{ij\theta}\rho(\theta)\,d\ell$, so $\rho_1=\gamma/2$ and $\rho_j=0$ for $j>1$. The integral of the displayed joint weight is at least $\exp[N^2\gamma^2/4-N\log2]$. Indeed change the product integration to independent angles of density $\rho$ and apply Jensen's inequality to the logarithm. The field term then has mean $N^2\gamma^2/2$. The interaction mean is $-N(N-1)\gamma^2/4$, and the entropy cost is at most $N\log2$ because $\rho\le2$. The interaction follows by integrating $\log|1-t e^{ix}|=-\sum_{j\ge1}t^j\cos(jx)/j$ and taking $t\uparrow1$. The logarithmic singularity is integrable, since for $t\ge1/2$ the modulus is at least $\sqrt 2|\sin(x/2)|$ and at most two.

Suppose at most one eigenangle has $\cos\theta\le-3/4$. Take $f=[(1-\cos\theta)/2]^{128}$. Its empirical mean is at most $1/N+(7/8)^{128}<1/N+2^{-16}$. Its $\rho$ mean is at least $(1-\gamma)\binom{256}{128}/4^{128}\ge1/(4\cdot257)>2^{-11}$. Here the central binomial coefficient is the largest of the 257 coefficients, and $(8/7)^8>2$. The absolute Fourier coefficients of $f$ sum to at most one by multiplying the three-term Fourier polynomial for $(1-\cos\theta)/2$. For $N\ge8192$, some $1\le j\le128$ must therefore have $|u_j-\rho_j|\ge2^{-12}$.

Set $t=1-1/N$. Since $|1-z|^2\le t^{-1}|1-tz|^2$ for $|z|=1$, the log of the joint weight is bounded above by

$$
 N^2\!\left(\frac{\gamma^2}{4t}
      -t|u_1-\gamma/(2t)|^2-\sum_{j\ge2}\frac{t^j}{j}|u_j|^2\right)
      -N\log(1-t)-\frac{N(N-1)}2\log t .
$$

This follows by summing the convergent logarithm series over all ordered pairs, subtracting the $N$ diagonal terms and completing one square. On the angular event, the square or sum subtracts at least $2^{-32}$. Indeed $t^j\ge1-j/N\ge1/2$ for $j\le128$, and $|\gamma/(2t)-\rho_1|<2^{-13}$. Also $-\log t\le1/(N-1)$ and $N^2\gamma^2(1/t-1)/4\le N/2$. Integrate this upper bound over a set of angle volume at most one and use the denominator bound. The $U(N)$ probability of the event is at most $\exp[-2^{-32}N^2+N(\log N+2)]$.

*Return to $SU(N)$.* For $V$ Haar on $SU(N)$ and independent $\theta$ uniform on $(-\pi/N,\pi/N]$, the matrix $e^{i\theta}V$ is Haar on $U(N)$. Translation of the phase interval modulo $2\pi/N$ is absorbed by a central element of $SU(N)$, which proves invariance. The two log tilts differ by at most $\gamma\pi N$. A real part of an eigenvalue changes by at most $\pi/N<1/20$. If $V$ has at most one eigenvalue with real part $\le-7/10$, every corresponding $e^{i\theta}V$ has at most one with real part $\le-3/4$. Comparing both numerators and denominators costs at most $e^{2\gamma\pi N}\le e^{5N}$. This proves (24).

The effect persists on an open set of exteriors at each such $N,M$. For $\|A-\gamma I\|_{\rm op}<2^{-35}$, any one-link log density changes by at most $2^{-35}N^2$ before normalization. The exceptional probability in (24) is then at most $\exp[-2^{-33}N^2+N(\log N+7)]$, and the same selected plane has $\mathcal G_NE>E/25$ on the complementary event. The size of this exterior set in the full four-dimensional equilibrium law is unknown. The result tests an instantaneous conditional sign. A weighted contraction over time as in (6) permits this event.

**PROVED — Corollary 21 (opposite signs after a positive Langevin time).** Sample the updated link in its conditional Wilson law. Choose a measurable tangent there with deterministic $E(v)>0$, then evolve all links by (1). Let $0<t\le2^{-30}$. For a low-rank staple as in Theorem 19 with the right side of (23) at most $1/4096$, every such choice obeys

$$
                    \mathbb E E(v_t)\le(1-t/200)E(v).
$$

For the exact scalar-staple exterior in Theorem 20, for every even $N\ge8192$ with $2^{-32}N^2-N(\log N+7)\ge7\log2$, one can instead choose a balanced two-colour tangent with

$$
                    \mathbb E E(v_t)\ge(1+t/80)E(v).               \tag{25}
$$

*Proof.* The one-link identity $\mathcal G_NE/E=-1-2\operatorname{Tr}(v^*vH)/T$ and $\|H\|_{\rm op}\le12$ give an upper bound of $23$. In the first case the mean initial rate is at most $-1/62+24/4096<-1/124$. In the second case use the two eigenvectors in the proof of (24) when they exist, breaking ties using a fixed basis. Else use a fixed two-colour plane. Its norm is the same on both events. Here $\|H\|_{\rm op}\le3/4$, so the rate is always at least $-5/2$. Its mean is at least $1/20-(51/20)/128>1/40$. The uniform second-order remainder from Lemma 13 is at most $2^{19}t^2 e^{95t}E(v)\le tE(v)/1024$. That bound holds at every initial field and tangent separately. It applies to the measurable selection before the evolution starts. The stated finite-time inequalities follow. The expanding initial rule uses the current matrix. The distribution of a direction brought in by the real tangent flow is a separate question.

## 8. Coupling range, comparison groups and the SU(2) target

**PROVED — coupling scale.** With $\beta_{\rm tr}=2/\lambda$ the coefficient of one real plaquette trace is $N\beta_{\rm tr}$. The absolute-drift test in Lemma 2 has $c_0<0$ only for $\beta_{\rm tr}<1/48$, or $\lambda>96$. This is the same numerical window reported for SU(N) in the repository's Shen–Zhu–Zhu digest in its $\beta N$ convention. It is a sufficient window. The target $1\le\lambda\le2$ has $1\le\beta_{\rm tr}\le2$. Lemmas 2, 9, 11 and 13 and Theorems 10 and 14 hold there without a strong-coupling series. Equations (5) and (8) give the exact rank cost if the leading signed estimate (6) holds. **No enlargement of the proved equilibrium mass-gap range follows from this note.**

**PROVED — the high-charge abelian test.** On a circle the brackets in Lemmas 1 and 8 vanish. The calculation that gave $-v/2$ in (1) gives zero, and $\operatorname{Ad}_h u=u$ has zero angular derivative. Thus even perfect return gives no negative term from an exclusive link in (11). Also, for nonzero integer $q$, $\theta\mapsto q\theta\bmod 2\pi$ pushes Haar measure to Haar measure, by splitting the integral into $|q|$ equal intervals. Applied independently to the links in a U(1) Wilson law built with character $e^{iq\theta}$, this map gives exactly the charge-one Wilson law at the same action coefficient for observations of these powered links. Large charge supplies neither more colour directions nor the factor $Nk$ in (18) at matched action strength.

**PROVED — small rank.** Estimates and identities (1)–(5), (14) and (18) hold for $SU(2)$. In (8) the available error estimate there is $D(q)/4$. A positive margin at sufficiently large rank supplies no comparison of that number with $\delta$. At rank 2 with $k=2$ and $\alpha=1/4$, (18) gives $(1+e^2)^{-1}$ for one link. The resulting path bound still has branching factor $18(1+e^2)^{-1/19}>1$. A putative monotonicity under $SU(2)\hookrightarrow SU(N)$ is no input here. The embedded subgroup has Haar measure zero for $N>2$, by its lower real dimension, and the Wilson action also changes its coefficient with rank.

**CITED — precise consumer.** The theorem **GapChain.Offset.su2_fixed_observable_gap_of_infinite_passing** in the pinned lane's [Offset.lean](../lean/gapchain/GapChain/Offset.lean#L701) uses an infinite set of passing cutoffs. The threshold in [PurIo.lean](../lean/gapchain/GapChain/PurIo.lean#L25) is $457/625$ at $u=\mathrm{side}/512$ in the SU(2) neutral-sector purity. **ARGUED — consequence.** Even proving (6) on $[1,2]$ would give a separate fixed-spacing theorem. Bound (18) holds at every bare $\lambda>0$ because a single Wilson link has only the first harmonic on the chosen circle. A blocked action would have to preserve this comparison or control its higher harmonics. Bound (16) for mixed plaquettes uses the product $\lambda N r_v$. Neither estimate supplies the running action or a rate in physical units. The SU(2) purity test additionally sees the multiplicities in the whole neutral trace. This work supplies local algebra and signed Wilson estimates that can be tested at rank 2. It supplies no interpolation in rank or infinite set of passing cutoffs.

**Research status.** FINISH row 1709, Codex author. PROVED means a hand argument in this note. The finite-rank identities, concentration bounds and opposite finite-time signs in Corollary 21 use hand proofs. The existence of a positive local form satisfying (6) at the target coupling is GUESSED. The conditional theorem has an explicit mass rate only after that form is supplied. No Lean check or independent proof review was run. This research note grants no status.
