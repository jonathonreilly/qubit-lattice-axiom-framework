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

## 3. Proof through a stationary preconditioned flow

On Gamma consider the SDE

 d omega_t =[-omega_t+K grad R(omega_t)+K h]dt
             +sqrt(2K)dB_t.                          (5)

The noise and drift preserve Gamma. The density(2) is invariant by direct
integration by parts in Gamma: the drift equals K times the gradient of
its log density. The uniform Hessian lower bound in section1, or synchronous
coupling with k2 delta<1, gives uniqueness of its invariant law and
convergence from finite initial data. No limit uniform in the number of
coordinates is needed to identify this finite-dimensional invariant law.

For two solutions with the same Brownian path, variation of constants and
Gronwall give contraction at least exp[-(1-kp delta)t] in ell^p for each
p=2,3,3/2. This is a bound on differences; the Brownian path itself is not
assumed uniformly bounded for all time.

Use a two-sided Brownian path and the stationary pullback solution. Its
first derivative v_a(t)=D_a omega_t^h with respect to the source h solves

 v_a(t)=K a+integral_(-infinity)^t exp[-(t-s)]
                    K R''(omega_s^h) v_a(s) ds.      (6)

The time-integral operator is a contraction in the norm sup_t||v(t)||_3,
with norm at most k3 delta. Thus it has a unique bounded solution and

 sup_t||v_a(t)||_3<=C3||a||_3.                       (7)

This bound holds for each noise realization. Differentiate once more:
w_bc(t)=D_bD_c omega_t^h satisfies

 w_bc(t)=integral_(-infinity)^t exp[-(t-s)] K
   [R''(omega_s^h)w_bc(s)+R'''(omega_s^h)[v_b(s),v_c(s)]] ds.            (8)

The same contraction in ell^(3/2), using self-adjointness of K, and(1),(7)
gives

 sup_t||w_bc(t)||_(3/2)<=M3 C3^3 ||b||_3 ||c||_3.     (9)

The source derivatives can be justified by finite-past solutions followed
by pullback. First and second variations obey the same uniform bounds.
Contraction forgets the initial condition, and the continuity of R'' and
R''' plus dominated convergence transfers the variation equations to the
stationary solution. Equivalently, difference quotients in(6),(8) converge
by the contraction estimate. This argument uses C3 regularity and the
uniform bounds(1), not a formal derivative of an unspecified infinite law.

Since DF(h)[a]=E(a,omega_0^h), equations(7),(9) justify differentiation
under this expectation twice. Therefore

 D^3F(h)[a,b,c]=E(a,w_bc(0)).

Holder with exponents3 and3/2 proves(3). The constants contain no hidden
factor of the dimension M.

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

## 5. Intended three-form application and still-unchecked inputs

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

Next checks: challenge(3) with finite positive integrations and the
collective-coordinate control; derive the free-cube ell^3 projection bound
and explicit carrier derivative estimates; then reassess the covariance
identification rather than promoting a conditional chain prematurely.

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
record(13) as the correctly specified standard CZ input, with an additional
source/proof check outstanding, rather than importing the misprinted
formula. The reflection argument(11)-(12) is explicit and independent of
that typography issue.

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
