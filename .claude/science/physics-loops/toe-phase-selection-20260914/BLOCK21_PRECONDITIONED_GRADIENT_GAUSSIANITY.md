# A preconditioned finite-dimensional route to macroscopic Gaussianity

Personal proof candidate, 2026-09-15. This is an independently stated
analytic lemma being developed to attack the unproved Gaussianity part of
BLOCK21_FIXED_LAW_FULL_FLUX_BRIDGE_DERIVATION.md. It is not yet independently
checked. The source/covariance/state bridges for the actual gauge model
remain explicit. Standard preconditioned Langevin machinery is used; no
claim of novelty for that machinery is intended.

Primary motivation: Conlon and Dabkowski, *Extensions of the Brascamp-Lieb
Inequality and the Dipole Gas*, JSP192,101(2025), DOI10.1007/s10955-025-03478-x,
especially the preconditioned dynamics(4.2)-(4.3) and the third-derivative
argument(5.3)-(5.17). That paper states a scalar nearest-neighbor gradient
model. The lemma below replaces its pointwise nonlinearity by explicit
finite-dimensional operator assumptions, so applying it to a vector field
with extended carriers requires proving those assumptions.

## 1. Finite-dimensional assumptions

Let Gamma be a linear subspace of R^M. Let K be a real symmetric matrix
with kernel Gamma-perp and positive definite restriction K_Gamma to Gamma.
Use unnormalized coordinate ell^p norms in the ambient R^M. Assume

 ||K||_(2->2)<=k2, ||K||_(3->3)<=k3.

Self-adjointness gives ||K||_(3/2->3/2)=||K||_(3->3). Let R:R^M->R be C3
with, uniformly for all real omega,

 ||R''(omega)||_(p->p)<=delta, p=2,3,3/2,
 ||R'''(omega)[a,b]||_(3/2)<=M3 ||a||_3 ||b||_3.       (1)

In the second line, R'''[a,b] is a vector obtained by contracting two
arguments. Suppose k2 delta<1 and k3 delta<1. Define

 C3=k3/(1-k3 delta).

All hypotheses and constants are finite-dimensional, and may be supplied
uniformly for a family. The potential may contain interactions among many
coordinates. No independent-coordinate or scalar-field assumption is used.
Define on Gamma the tilted probability law

 mu_h(domega) proportional to
 exp[-(omega,K_Gamma^-1 omega)/2+R(omega)+(h,omega)] domega,
 F(h)=log integral_Gamma exp[-(omega,K_Gamma^-1 omega)/2
                              +R(omega)+(h,omega)] domega.             (2)

The Hessian in Gamma of the negative exponent is at least
(1/k2-delta)I. Hence(2) is proper for every real h, all linear exponential
moments exist, and F is smooth in h. R itself need not be convex. If R is
even, mu_0 is centered.

## 2. Claimed conclusion and why it is enough

For all real h and all ambient real a,b,c, the proposed bound is

 |D^3F(h)[a,b,c]|<=M3 C3^3 ||a||_3 ||b||_3 ||c||_3.   (3)

Taylor's theorem then gives

 |F(h)-F(0)-DF(0)[h]-D^2F(0)[h,h]/2|
 <=M3 C3^3 ||h||_3^3/6.                              (4)

Consequently, for a family with bounded M3 C3^3, suppose h_n^1,...,h_n^r
satisfy ||h_n^j||_3->0, and the covariance matrix of their centered linear
statistics under mu_0 converges to a finite matrix Sigma. Applying(4) to
every fixed real linear combination shows convergence of their real MGFs
to exp[t^T Sigma t/2], for all fixed t in R^r. This implies joint convergence
to N(0,Sigma). It establishes Gaussianity once the covariance converges;
it does not identify that covariance or ensure a unique limit.

A uniform covariance upper bound suffices to extract Gaussian subsequential
limits for a finite set of tests. That is weaker than the named Maxwell
limit and must not be substituted for covariance homogenization.

## 3. Proof through a finite-time preconditioned flow

On Gamma, starting at omega_0=0, consider the SDE

 d omega_t =[-omega_t+K grad R(omega_t)+K h]dt
             +sqrt(2K)dB_t.                          (5)

The noise and drift preserve Gamma. The density(2) is invariant by direct
integration by parts in Gamma: the drift equals K times the gradient of
its log density. Global boundedness of R'' makes the drift globally
Lipschitz. The positive Hessian lower bound in section1 supplies all
stationary moments. With synchronous Brownian noise, variation of
constants and Gronwall give

 ||omega_t-omega'_t||_p
 <=exp[-(1-kp delta)t]||omega_0-omega'_0||_p.

In particular the p=2 bound, applied with a stationary initial condition
having law mu_h, proves E omega_T^h -> E_mu_h omega as T tends to infinity.
This is for each finite dimension and fixed h. Neither a uniform bound
on the Brownian path nor a dimension-uniform mixing theorem is assumed.

For finite T the first source derivative v_a(t)=D_a omega_t^h obeys

 v_a(t)=(1-exp[-t])K a+integral_0^t exp[-(t-s)]
                    K R''(omega_s^h) v_a(s) ds.      (6)

The time-integral operator has norm at most k3 delta on the normed space
sup_(0<=t<=T)||v(t)||_3. Thus

 sup_(0<=t<=T)||v_a(t)||_3<=C3||a||_3.               (7)

This holds for every noise realization and every T. A second derivative
w_bc(t)=D_bD_c omega_t^h obeys

 w_bc(t)=integral_0^t exp[-(t-s)] K
   [R''(omega_s^h)w_bc(s)+R'''(omega_s^h)[v_b(s),v_c(s)]] ds.            (8)

The same contraction in ell^(3/2), using self-adjointness of K and(1),(7),
gives

 sup_(0<=t<=T)||w_bc(t)||_(3/2)
 <=M3 C3^3 ||b||_3 ||c||_3.                          (9)

Finite-time source differentiation follows from the usual difference-
quotient equations for a finite-dimensional SDE with additive noise and
C2 drift. Here it is simply differentiation of a random integral equation;
(1),(7),(9) supply deterministic bounds on the derivatives. Thus, putting
m_T(h)=E omega_T^h, Holder gives

 |D_bD_c(a,m_T(h))|<=M3 C3^3||a||_3||b||_3||c||_3.

To pass this bound to stationarity, no interchange of an infinite-time
limit with a derivative is needed. Integrate the displayed bound over a
source rectangle h+s b+t c,0<=s<=u,0<=t<=v. The resulting four-term
finite-difference bound passes to the limit T->infinity because each
m_T at a rectangle corner converges to m(h)=E_mu_h omega. Divide by uv
and let u,v decrease to zero. The function m(h)=DF(h) is already smooth
by the proper Gaussian tails in(2), so its mixed derivative has the same
bound. This is(3).

This finite-time argument replaces the draft's unnecessary stationary
pullback differentiation. It makes the limiting step explicit and does
not assume convergence of derivatives of stationary stochastic solutions.

## 4. Checkable sufficient conditions for extended carrier interactions

Suppose R has an absolutely convergent rank-one interaction expansion

 R(omega)=sum_lambda r_lambda(u_lambda dot omega),

with derivatives through order3 convergent on bounded sets. Assume
|r_lambda''|<=b_lambda and |r_lambda'''|<=b_lambda (different bounds can
also be used). Set

 delta=sup_i sum_lambda b_lambda |u_lambda,i| ||u_lambda||_1,
 M3=sup_i sum_lambda b_lambda |u_lambda,i| ||u_lambda||_1^2.             (10)

The absolute Hessian has row and column sums at most delta, so its norm
on every ell^p,1<=p<=infinity, is at most delta. For the third derivative
let T_ijk=sum_lambda b_lambda|u_i u_j u_k|. Each one-index marginal sum
of this nonnegative symmetric tensor is at most M3. Holder on the measure
T_ijk, followed by summing the marginal, gives

 sum_ijk T_ijk |a_i b_j c_k|<=M3||a||_3||b||_3||c||_3.

Duality proves the bilinear bound in(1). This argument retains the entire
carrier index and total variation; regrouping disconnected net charges is
not needed. A sine/cosine polymer term has the required bounded real
second and third derivatives, with the frequency included in u_lambda.

Uniform small Hessian norm alone is not enough. For example let K=I_M,
a_M=M^-1/2(1,...,1), R(omega)=zeta cos(a_M dot omega),0<zeta<1. The
normalized collective coordinate a_M dot omega has the same non-Gaussian
one-dimensional density proportional to exp[-z^2/2+zeta cos z] for every M.
Its test has ||a_M||_3^3=M^-1/2->0, but M3 in(10) grows as zeta sqrt(M).
The hypotheses correctly refuse to infer a Gaussian limit for this model.
A dimensional Hessian bound cannot replace the uniform third-order
influence condition.

## 5. Intended three-form application and input map

For the block21 auxiliary measure choose the local Hodge derivative
Dcal phi=(d_2*phi,d_3 phi), so Dcal*Dcal=H. Let

 omega=beta^-1/2 Dcal phi,
 K=Dcal(G-cI)Dcal*, Gamma=range(Dcal).

This K is positive on Gamma, has k2<=1 and the nonzero spectrum in
[1-c||H||,1]. The Gaussian pushforward of phi~N(0,beta(G-cI)) is gamma_K.
Every closed charge with a declared local integer filling q=d_2 n obeys

 2pi(q,phi)=2pi sqrt(beta)(n,omega_first).

Thus the carrier-preserving expansion of log Theta_c gives an extension
R(omega) by cosine terms, provided its total variation and the local
filling norms are checked for all carriers. Its Hessian condition and
third-order condition must be established in the explicit form(10), not
inferred from a quadratic-form estimate alone.

The needed uniform k3 bound is an ell^3 Hodge/Riesz projection estimate
on the chosen free-box boundary family. The scalar periodic CZ estimate
in Conlon-Dabkowski Theorem3.1 suggests it, but that statement must not be
silently applied to a different finite boundary condition. The local term
-c Dcal Dcal* is uniformly bounded in every ell^p; the real obligation is
Dcal G Dcal*. A reflected-periodic construction or direct discrete CZ
proof should address it.

For a two-form test h_a in block21,

 beta^-1/2(phi,d_2 h_a)=(h_a,omega_first).

Only the first block of the ambient source is used. Four-dimensional
cell-average sources obey ||h_a||_3^3=O(a^2). Therefore, IF k3 and(10) are
uniform with k3 delta<1, the log-MGF remainder for this actual auxiliary
observable is O(a^2), uniformly in volume, at fixed sufficiently large
beta. This would remove Gaussianity as a separate assumption in block21;
its covariance homogenization, state matching and finite-clock electric
current obligations would remain.

The following sections supply the reflection, carrier and periodic
projection derivations. The separate reflection/positive-integral runner
challenges finite geometry and the third-derivative estimate, including
the collective-coordinate control. Those calculations are not an
independent review of the analytic proofs. Covariance identification and
the physical-state bridge remain separate obligations.

## 6. Free-cube reflection removes the boundary mismatch

There is an explicit reflection that intertwines both d and d* for the
free cubical boundary convention. In one dimension put N=L+1, with N
vertices0,...,N-1 and N-1 edges0,...,N-2. Extend to the periodic cycle
of length2N. For vertex data f define

 (E0 f)(x)=f(x),0<=x<N;
 (E0 f)(x)=f(2N-1-x),N<=x<2N.

For edge data g define

 (E1 g)(x)=g(x),0<=x<N-1;
 (E1 g)(N-1)=(E1 g)(2N-1)=0;
 (E1 g)(x)=-g(2N-2-x),N<=x<2N-1.

For delta f(x)=f(x+1)-f(x) and its unweighted adjoint, direct substitution
at interior and endpoint coordinates gives

 delta_per E0=E1 delta_free,
 delta_per* E1=E0 delta_free*.                       (11)

Each input value occurs twice with the same absolute value, so
||Ej f||_p=2^(1/p)||f||_p. Tensor the extensions along the d coordinate
axes, choosing E1 on axes contained in the cell orientation and E0 on the
other axes. The usual alternating cochain signs occur identically in the
periodic and free differentials. Thus for every degree r,

 d_per E_r=E_(r+1) d_free,
 d_per* E_r=E_(r-1) d_free*,
 ||E_r f||_p=2^(d/p)||f||_p.                         (12)

For r>=1 the extension has zero mean in at least one coordinate direction,
because it is odd in an edge direction. Hence H_per^+ E_r=E_r H_free^-1;
there is no imported harmonic zero mode. Apply(12) also to the direct sum
of degree2 and degree4 outputs of Dcal. It follows that the free Hodge
projection Dcal H_free^-1 Dcal* is the restriction, by this isometric-up-
to-a-common-factor embedding, of Dcal_per H_per^+ Dcal_per*. Its ell^p
norm is therefore bounded by the periodic projection norm, with no factor
that grows with L.

The remaining analytic input is the standard periodic scalar second-order
Riesz bound, uniformly in the period, for

 delta_mu H_0,per^+ delta_nu* on ell^p,1<p<infinity.  (13)

Under this standard CZ input, each matrix entry of the degree3 Hodge
projection is a sum of at most4 shifted copies of operators(13). There
are7 output components (six two-form components and one four-form
component). If each scalar entry has bound kappa_p, a deliberately loose
coordinate-norm bound for the whole projection is28 kappa_p. Forward and
backward differences differ only by signs and translations, which are
ell^p isometries. The zero Fourier mode is assigned zero. The local
correction c Dcal Dcal* has norm at most64c in every ell^p, since Dcal has
row and column absolute sums at most8. In particular one may take

 k3 <=28 kappa_3+64c,                               (14)

uniformly in every free four-cube. Only finiteness matters for choosing a
sufficiently large fixed beta.

Source caution: the published Conlon-Dabkowski page14 was visually checked.
Its displayed Theorem3.1/eq(3.17) omits the inverse on the Laplacian; the
surrounding eqs(3.16),(4.2),(4.3) use the inverse. The literal displayed
operator cannot have the asserted limiting norm1 at p=2. We therefore
record(13) as the correctly specified standard CZ input rather than
importing the misprinted formula. Section8 gives a direct proof of that
input. Both that proof and the reflection argument(11)-(12) remain subject
to independent mathematical review.

## 7. Carrier bounds in the operator form needed above

Keep every cluster C with its full carrier and total individual charge
mass S, as in block15 and the free-cube boundary extension in block17.
Let a_C be its real source-independent coefficient, so pairing charge
reversal allows the real representation

 R(omega)=sum_C a_C cos[2pi sqrt(beta)(n_C,omega_first)].

The sum here still runs over the original paired cluster index; it does
not aggregate clusters by net charge. Assume the previously stated
carrier and local-filling estimates, with d=4:

 sum_(C:x in U(C),S(C)=S)|a_C|<=R_t exp[-tS/2],
 ||n_C||_infinity<=d S,
 #support(n_C)<=K0 S^d, K0=2^d 6^d,
 #possible carrier anchors within a filling box at y<=C1 S^d,
 C1=2^d 11^d.

These imply ||n_C||_1<=d K0 S^(d+1). Substituting
u_C=2pi sqrt(beta)n_C into(10), and summing over anchors before clusters,
gives the explicit bounds

 delta <=(2pi)^2 beta d^2 K0 C1 R_t
                   sum_(S>=1) S^(2d+2)exp[-tS/2]
        = beta epsilon_t,

 M3 <=(2pi)^3 beta^(3/2) d^3 K0^2 C1 R_t
                   sum_(S>=1) S^(3d+3)exp[-tS/2].     (15)

Both are uniform in volume and real omega. The mass reserve proves
absolute convergence of all derivatives involved. Delta tends to zero
exponentially in beta; M3 is finite for each fixed beta in the expansion
regime and also tends to zero as beta grows. M3 need not be small to apply
the lemma: only k3 delta<1 is a contraction requirement.

If(13) and the provisional carrier estimates pass their required checks,
there exists a finite beta0 such that for every fixed beta>=beta0 the
actual auxiliary linear sources have Gaussian log-MGF remainder bounded
by const(beta)||h_a||_3^3=O_beta(a^2). This is a specific reduction of the
Gaussianity obligation to checked operator and carrier estimates. A
Maxwell covariance limit and the free/periodic state match are still not
proved by this argument.

## 8. Direct derivation of the correctly specified periodic Riesz bound

Here is a proof route for(13) that does not rely on the misprinted display.
For m>0 on Z^d write delta_j(k)=exp(i k_j)-1 and
lambda(k)=sum_j |delta_j(k)|^2. The scalar multiplier is

 M_mu,nu,m(k)=delta_mu(k) conjugate(delta_nu(k))/(lambda(k)+m^2),
 k in [-pi,pi]^d.                                    (16)

Its absolute value is at most1, hence its ell2 norm is at most1 by
Plancherel. In a fixed coordinate chart around0, differentiation of the
rational expression, using lambda(k) comparable to |k|^2, shows

 |partial^alpha M_mu,nu,m(k)|<=C_(alpha,d)|k|^(-|alpha|), k!=0,          (17)

uniformly in m>0. Each derivative either differentiates a smooth numerator
vanishing quadratically or a denominator bounded below by const|k|^2+m^2;
rescaling k=r u on an annulus r/2<=|k|<=2r makes all such derivatives
uniformly bounded in m/r. Away from0 the bounds are uniformly smooth.

Use a smooth dyadic partition of unity into annuli of radii r=2^-j near0
and finitely many smooth periodic coordinate charts away from0. A localized
multiplier on an r-annulus has derivatives of order n bounded in L1 by
C r^(d-n). Repeated integration by parts in its compact coordinate chart
therefore bounds its Fourier coefficient K_r(x) by

 |K_r(x)|<=C r^d(1+r|x|)^(-d-2).

The same argument after differentiating the Fourier transform with respect
to its real argument gives C r^(d+1)(1+r|x|)^(-d-2). Integrating this latter
bound along the segment from x to x-y, with |x|>=2|y|, yields the difference
bound C |y| r^(d+1)(1+r|x|)^(-d-2). The finitely many away-from-zero
charts satisfy the same estimates with r comparable to1. Summing over
annuli gives the uniform kernel estimates

 |K_m(x)|<=C(1+|x|)^(-d),
 |K_m(x-y)-K_m(x)|<=C |y|(1+|x|)^(-d-1), |x|>=2|y|.                  (18)

In particular the discrete Hormander sum over |x|>=2|y| of the second
absolute difference is bounded by a dimension-dependent constant. The
case y=0 is zero. These estimates also follow as limits of finite annular
sums; their ell2 multiplier norms are uniformly bounded by the finite
overlap of the partition.

For clarity, the standard discrete Calderon-Zygmund step can be carried
out on dyadic cubes in Z^d. Given a summable function f and threshold a>0,
choose maximal dyadic cubes Q whose average |f| exceeds a. Their total
cardinality is at most ||f||1/a, and each cube average is at most2^d a.
Write f=g+sum_Q b_Q, with g equal to the cube average on each Q and f
elsewhere. Then ||g||infinity<=2^d a, ||g||1<=||f||1, each b_Q has zero
sum, and sum_Q||b_Q||1<=2||f||1. The ell2 bound controls the exceptional
set for Tg by const||f||1/a. Outside fixed enlargements of the cubes,
subtract the kernel value at a chosen cube center and use the Hormander
sum in(18) to get

 sum_(outside enlarged cubes)|T sum_Q b_Q|<=C||f||1.

The enlarged cubes themselves also have cardinality at mostC||f||1/a.
Chebyshev's inequality proves a uniform weak(1,1) bound. Marcinkiewicz
interpolation with the ell2 bound gives a uniform strong ell^(3/2) bound.
The adjoint swaps mu and nu and obeys the same bounds, so duality gives
a uniform strong ell3 bound. This argument uses the standard interpolation
inequality between weak(1,1) and strong(2,2), not an assumption about the
unknown gauge measure.

For fixed m>0 the multiplier(16) is smooth on the whole torus and its
kernel is absolutely summable. Periodizing that kernel on a finite cycle
product gives the corresponding finite-period multiplier. Its ellp norm
is no larger than the infinite-lattice norm: first truncate the summable
kernel, apply the infinite-lattice operator to a periodic test repeated
on an increasing union of periods, divide the pth power norm by the
number of periods, and let the union grow. Finite kernel range makes the
boundary fraction vanish. Then remove the kernel cutoff using its ell1
tail. Finally let m decrease to zero on the fixed finite torus. Each
nonzero Fourier mode converges to the multiplier with denominator lambda;
the zero mode remains zero. Finite-dimensional norm convergence preserves
the same uniform bound. This proves(13), in particular at3 and3/2, with
finite constants depending only on dimension and exponent.

The proof checks the inverse, the zero mode, the mass-uniform derivatives,
and the finite-period transfer separately. The earlier reflection proof
then supplies the intended free-cube estimate; it does not assume that
an arbitrary boundary-value projection enjoys the same bound.

## 9. Exact finite-volume flux Gaussian remainder, before homogenization

The previous sections give a stronger intermediate target than simply
removing T in a scaling limit. Let T_r=(I-cH_r)^-1 on degree-r free-cube
cochains. The cochain identities imply

 T_3 d_2=d_2 T_2.

Each H_r is the tensor sum of one-dimensional Dirichlet/Neumann scalar
Laplacians on its orientation component. Its absolute row and column
sums are at most4d, so c=1/(8d) gives ||T_r||_(p->p)<=2 for every p.
Consequently the exact real tilt in block21 is

 -beta^-1/2(phi,T_3 d_2 h)=-(T_2 h,omega_first).

Apply(4) to that source. The quadratic term combines with the explicit
Gaussian prefactor in the exact flux identity to give precisely the
actual finite-volume covariance of X, by equation(6) in the full-flux
note. Thus, conditional only on the explicitly recorded carrier estimates
and the present proof steps, at every sufficiently large fixed beta,

 |log E exp[i(h,X)]+Var(h,X)/2|
 <=(4/3) M3 C3^3 ||h||_3^3                         (19)

uniformly over all finite free four-cubes and real two-form sources h.
The logarithm is real and well-defined because the exact characteristic
is a positive Gaussian prefactor times a positive real MGF. The factor
4/3 is 2^3/6. No Gaussian limit or covariance limit has been assumed in
deriving(19).

For smooth macroscopic cell-average sources, ||h_a||3^3=O(a^2). Together
with the centered full-flux MGF domination, this makes every covariance-
convergent finite-dimensional subsequence Gaussian. It does not fix the
covariance kernel, prove that all subsequences agree, or identify the
physical angle-state limit. In particular(19) cannot by itself replace
the remaining covariance homogenization with a guessed Maxwell tensor.
The finite-clock model remains outside the Haar-unfolding hypothesis.
