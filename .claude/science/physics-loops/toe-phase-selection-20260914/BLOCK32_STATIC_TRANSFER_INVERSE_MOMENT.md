# Block32: a uniform inverse moment for a fixed static insertion

Personal proof proposal, 2026-09-15. It strengthens the supplied-clock static
transfer construction in PR8140 at8a71d7fa8a87a451e5c49df31d18986574d73610.
No physical law, photon or dynamical charged particle is selected.

## 1. A local Fourier comparison

In the notation of PR8140, T=V^(1/2) C V^(1/2), beta>0, and Omega_0 is
its normalized positive Perron vector, T Omega_0=lambda_0 Omega_0.
The one-link convolution in C has strictly positive Fourier coefficients

 c_k proportional sum_(r congruent k mod N) exp[-r^2/(2beta)],
 k in Z_N.                                              (1)

Let j be any integer spatial-link vector of finite support and U_j the
multiplication operator exp[2pi i j.a/N]. Fourier transformation makes C
diagonal with eigenvalues product_e c_(k_e); U_j shifts k by j. Hence

 U_j^* C^(-1) U_j <= K(j) C^(-1),
 K(j)=product_e max_(k in Z_N) c_k/c_(k+j_e).              (2)

This is a positive operator inequality, not a bound on individual matrix
entries. Each factor is finite, positive and at least1; edges with j_e=0
contribute1. For a simple length-R path with charge q, K(j)=kappa_q^R,
kappa_q=max_k c_k/c_(k+q). The choice of Fourier sign changes q to-q and
gives the same maximum since c_k=c_(-k).

U_j commutes with V and its inverse square root. Therefore

 U_j^* T^(-1) U_j <= K(j) T^(-1).

Taking the expectation in Omega_0 gives the volume-independent bound

 <U_j Omega_0,(T/lambda_0)^(-1) U_j Omega_0> <=K(j).       (3)

The comparison requires no source-curvature estimate or large-beta regime.
It is valid on every finite spatial box containing j, for every fixed finite
N and beta>0. K(j) can be extremely large and grows with path length; no
uniform bound in N or R is asserted. For a charge alias j=0 modN, K=1.

## 2. Removing the possible zero atom after the spatial limit

The finite path-insertion spectral law nu_(L,j) is supported on(0,1], and
(3) says integral lambda^(-1) nu_(L,j)(dlambda)<=K(j). The free-state
matching proof in PR8140 identifies its weak limit nu_j on[0,1]. For each
positive integer m the function min(m,1/lambda), assigned value m at0,
is bounded and continuous on[0,1]. Weak convergence and then monotone
convergence give

 integral_[0,1] lambda^(-1) nu_j(dlambda)<=K(j),          (4)

where the integrand is infinite at0. Consequently nu_j({0})=0. This is
stronger than merely knowing finitely many positive-time moments.

On the ENTIRE cyclic Hilbert space L2(nu_j), multiplication by
H_j=-log lambda is now a densely defined nonnegative self-adjoint operator,
and the transfer multiplication operator is exactly exp(-H_j). The vectors
cut off to lambda>=1/m give the required dense domain. Its semigroup is
strongly continuous by dominated convergence, and for the cyclic vector1

 <1,exp(H_j)1> <=K(j),
 <1,H_j^p 1> <=p! K(j), p a nonnegative integer.         (5)

The second inequality uses E^p<=p! exp(E) for E>=0. In particular the
continuous-time interpolation W_j(t)=integral exp(-tE) nu_j(dlambda)
has every finite one-sided time derivative at0, determined by these moments.
It extends analytically to Re t>-1 by (4), with derivatives justified on
compact subsets using the spare exponential margin. This interpolates the
same integer-time static correlation; no empirical continuous time is derived.

## 3. Compatibility with the static threshold bound

The source-curvature/Ginibre argument still supplies the stronger separation
bound for the bottom of this path-visible spectrum:

 0<=inf support(H_j)<= (beta^-1+epsilon) q_eff^2
                          [G3(0)-G3(R e1)].             (6)

Equation(4) controls the opposite, high-energy tail and removes the possible
infinite-energy component; it does not sharpen (6) into a Coulomb equality.
It does not prove that this cyclic space is an entire infinite-volume charged
sector, that all path choices have the same spectral threshold, or that the
full gauge theory's Hilbert space is reconstructed here. Those stronger
claims need their own compatibility and density arguments.

## 4. Required direct challenges

Use finite spatial-square transfer matrices from the existing direct-law
checker. Compare the measured inverse moment with K(j), and independently
verify the Fourier coefficient ratio and the conjugated inverse operator
inequality. Test charges0,1,N-1,N and nonconstant spatial V; omitting the
charge-dependent Fourier shift must be detected. A generic positive matrix
without the convolution/multiplication structure is not a proof of (2).


Completed personal challenge:30 finite insertion cases compare direct linear
solves, independently assembled Fourier ratios, whitened inverse operators
and spectral sums. Maximum relative inverse-moment discrepancy is below3e-14.
These finite floating checks do not replace the volume-independent proof.
