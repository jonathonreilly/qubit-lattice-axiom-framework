# Block33: endpoint dependence of the visible static threshold

Personal author derivation, 2026-09-15. Independent review pending. This
uses the provisional all-real-source curvature and positive Fourier mixture
in PR8133, and the matched clock free-state/transfer construction in PR8140.
It is a supplied-model statement, not a dynamical-matter or axiom result.

## 1. The positive Fourier extension matters

On a free cubic box, write the source's positive current extension as

 w(x)=exp[-N^2(x,Gx)/(2beta)] chi(x),
 chi(x)=E_m exp[2pi i<n(m),N d1 G x>],
 T(s)=sum_(a in Lambda) w(a+s).                         (1)

The magnetic probability weights are positive and symmetric; the chosen odd
integer fillings n(m) define the all-real characteristic chi. Under the
source's stated smallness it is strictly positive everywhere, and V=-log w
satisfies D2 V<=N^2 a G, a=beta^-1+epsilon. Its Fourier transform is a
positive Gaussian mixture. Equation(5) of the pinned quantized-current
Poisson source therefore gives T(s)<=T(0) for EVERY real s, while positive
w gives T(s)>0. This all-real maximum is stronger than merely bounding the
physical discrete character values, and is an explicit load-bearing input.

Set

 f(J)=-log[T(J/N)/T(0)], J in the real conserved-current space.

It is nonnegative and C2. Gaussian growth and the bounded source derivatives
justify differentiating the periodized sums. In the shifted lattice measure,

 D2 log T = -E D2 V + Cov(DV) >= -N^2 a G,
 D2 f <= a G.                                          (2)

The covariance has a positive sign. This is a continuous interpolation of
the logarithmic character, not an all-tilt variance bound for integer currents.

## 2. A square-root comparison lemma

If f>=0 on a finite Euclidean space and D2 f<=A for a positive matrix A,
Taylor's upper bound at y=x-A^(-1)grad f(x) gives

 0<=f(y)<=f(x)-[grad f(x),A^(-1)grad f(x)]/2.

Thus |grad f|_(A^-1)^2<=2f. Applying this to sqrt(f+delta) and integrating
along a segment, then sending delta down to0, proves

 |sqrt(f(x))-sqrt(f(y))| <=sqrt[(x-y,A(x-y))/2].          (3)

Using (2) in (3), any two physical conserved integer currents satisfy

 |sqrt(-log W_N(J))-sqrt(-log W_N(K))|
                  <=sqrt[a(J-K,G(J-K))/2].              (4)

The same source and interpolation are used on both sides. No claim is made
that arbitrary real-current conventions have identical values; physical
integer characters do, and the one fixed interpolation proves their bound.

## 3. Two fixed spatial paths with the same endpoints

Let gamma and gamma' be finite integer spatial paths carrying the same
charge and having the same divergence. Their static rectangular currents
J_(gamma,T) and J_(gamma',T) have the same temporal sides. Their difference is

 Delta_T = b at time0 - b at timeT, b=gamma-gamma', d0*b=0.

For fixed T, pass (4) through the free-cubic limit using the source's strong
Green projection limit and the unique free-boundary state. On the infinite
four-dimensional lattice, translation invariance and Cauchy-Schwarz give

 (Delta_T,G Delta_T)<=4(b at time0,G b at time0),         (5)

which is finite and independent of T. Therefore

 |sqrt[-log W_gamma(T)/T]-sqrt[-log W_gamma'(T)/T]|
            <=sqrt[2a(b,Gb)/T].                         (6)

Each long-time rate exists by its positive transfer spectral measure.
Sending T to infinity proves that they are equal. Thus, within this matched
free state and these source hypotheses, the threshold reached by a finite
static path depends on the endpoint charge profile, not the chosen finite
path. In particular every such path shares the straight-path bound

 0<=E_(x,y,q)<=a q_eff^2 [G3(0)-G3((y-x))]              (7)

for any fixed endpoint displacement. The following general path calculation
supplies the corresponding Green limit, including non-coordinate paths.

Write a finite spatial current as eta, its divergence as rho=d0*eta, and
its three Fourier components as eta_hat(k). Put lambda=sum_i|exp(ik_i)-1|^2
and r=(lambda+2-sqrt(lambda(lambda+4)))/2. As in the rectangular calculation,
the temporal Green kernel is g_lambda(t)=r^|t|/sqrt(lambda(lambda+4)).
The temporal current contributes |rho_hat|^2 times the sum of g(t-s) for
0<=s,t<T. The two spatial caps contribute
2||eta_hat||^2(1-r^T)/sqrt(lambda(lambda+4)). Different orientations have
no cross term because the one-form Hodge Green is scalar in orientation.
Thus exactly

 E_eta(T)=T integral |rho_hat|^2/lambda
   +2 integral (1-r^T)/sqrt(lambda(lambda+4))
                   [||eta_hat||^2-|rho_hat|^2/lambda].   (7a)

All integrals use normalized measure on the three-torus. Fourier divergence
and Cauchy-Schwarz give |rho_hat|^2<=lambda||eta_hat||^2, so the remainder
is nonnegative. Since ||eta_hat||<=sum_e|eta_e|, it is at most
2||eta||_1^2 G4(0), uniformly in T. Therefore E_eta(T)/T decreases to
<rho,G3 rho>. For a pair rho=q(delta_y-delta_x), this is
2q^2[G3(0)-G3(y-x)], yielding (7). For any finite neutral external charge
profile the corresponding bound is E_rho<=a<rho,G3 rho>/2. These are
upper bounds; no equality for the physical interaction energy is inferred.

## 4. A limited common-sector consequence to review separately

For any finite linear combination O=sum_j c_j U_j of same-charge spatial
characters, finite-volume spectral Cauchy-Schwarz gives

 <O Omega,tau^T O Omega>
        <= [sum_j |c_j| sqrt(W_j(T))]^2.               (8)

Its two-time function has a limiting positive spectral measure: mixed
moments are free-state closed Wilson characters with temporal charge lines,
and finite positive matrix-valued spectral measures have consistent weak
limits. Equations(6),(8) imply that such an observable cannot have a smaller
visible threshold than the common path threshold; individual paths attain
it. Cancellations may give a larger threshold for a particular combination.

One can try to reconstruct the common space generated by these two-time
kernels and transfer polynomials. Block32 bounds inverse moments of every
finite combination by [sum_j |c_j|sqrt(K(j))]^2, so a zero-transfer atom is
absent on the generating vectors. Completing the matrix-moment construction
would give an injective positive contraction on that specifically generated
space. This paragraph remains a proposed construction obligation; it does
not silently identify that space with every infinite-volume charged sector
or reconstruct the complete interacting field algebra.

## 5. Checks still required

Challenge (2)-(4) on an explicit Gaussian times a positive cosine mixture,
using independently summed real and Fourier theta representations. Check
the nonnegative maximum, curvature sign and square-root inequality. Preserve
the separate high-energy inverse-moment result. Do not use a finite-spectrum
overlap tolerance as proof of path-independent infinite-volume support.


Subsequent author checkpoint: Block34 supplies the common matrix-moment
construction outlined in section4, and Block35 supplies a stronger
positive-Fourier path comparison valid for every beta>0 and finite N.
The square-root-log theorem remains a separate conditional source estimate.
Four theta fixtures agree between real and Fourier sums within8.9e-16,
nine time-separated-loop controls satisfy the uniform energy bound, and24
general-path Green fixtures agree with direct temporal-kernel sums. These
are personal finite checks; all infinite statements await independent review.
