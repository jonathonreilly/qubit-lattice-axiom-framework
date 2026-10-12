# Finite local scalar construction with joint approximation guarantees

Status: conditional-support. This extends the explicitly hypothetical common
scalar mechanism; no parameter here is fitted to a physical observation. The
finite-field construction closes a locality/stress-tensor definition gap for
each finite member, not for an interacting infinite continuum.

## Canonical realization

For positive masses mu_j and weights w_j with sum w_j=1, supply N canonical real
scalar fields and a common current J built from explicitly chosen matter
operators. In a supplied Lorentzian metric with signature (-,+,+,+), take

`S = integral sqrt(-g) [M_Pl^2 R/2 + L_matter
     - 1/2 sum_j (g^ab partial_a phi_j partial_b phi_j + mu_j^2 phi_j^2)
     + J sum_j sqrt(w_j) phi_j] d^4x`.

The composite Phi_N=sum sqrt(w_j)phi_j has the positive atomic spectral measure
sum w_j delta(mu-mu_j). This is a local, second-order finite-field effective
action with a defined classical stress tensor and a positive free Minkowski
vacuum. It has the static, retarded and Gaussian noise formulas already derived,
all using the same atomic measure. It does not independently choose a noise
amplitude after calibrating a force. Interactions can change the free spectral
function; the free construction is the leading stipulated weak-coupling sector.
Renormalization, cutoff control and the physical matter action are additional
obligations. Supplying an Einstein term and a matter action does not derive them.

For the gamma measure, use x=ell*mu and t=r/ell. Positive generalized Laguerre
quadrature with weight x^(s-1) exp(-x)/Gamma(s) gives nodes x_j, weights w_j,
and physical masses mu_j=x_j/ell. Thus N is a resolution choice and s,ell are
shared spectral parameters; the N weights are not independent empirical fits.

## Static error from a positive Hermite remainder

For monic generalized Laguerre polynomial p_N, the normalized squared norm is
`integral p_N(x)^2 dnu_x = N! Gamma(N+s)/Gamma(s)`.
Hermite interpolation at the N simple nodes gives pointwise remainder
`f^(2N)(xi_x) p_N(x)^2/(2N)!`. Integration proves, for t>=0,

`0 <= (1+t)^(-s) - sum_j w_j exp(-t*x_j) <= B_N(s,t)`,

`B_N(s,t)=t^(2N) N! Gamma(N+s)/[(2N)! Gamma(s)]`.

For the radial force kernel f=(1+t*x)exp(-t*x), the even derivative is
`t^(2N)[t*x-(2N-1)]exp(-t*x)`. Its absolute value is at most
`(2N-1)t^(2N)`, so the force-factor error is at most `(2N-1)B_N`.
These bounds can be poor at large t; no accuracy outside a declared radius
window follows from a small error near one radius.

## Why static agreement is insufficient for vacuum spectra

With the Gaussian spatial profile already fixed, define W_a(T)=integral j_a(w)
exp(-iwT)dw. The finite spectrum is

`j_N(w)=sum_{mu_j<w} w_j sqrt(w^2-mu_j^2)
         exp[-a^2(w^2-mu_j^2)]/(4 pi^2)`.

The continuum j(w) is strictly positive at every w>0; every finite construction
above has j_N(w)=0 below its smallest mass. Therefore a good potential
approximation on a bounded radius window does not imply a uniform relative
approximation to the noise at all low frequencies. This explicit discrepancy
is an experimental discriminator only if an apparatus can resolve its absolute
size with independently known coupling/state/backgrounds.

## Positive bins give joint absolute error control

A second construction partitions 0<=mu<=M into equal bins of width h, puts
each bin's exact gamma probability at its midpoint, and puts all remaining
probability at the conditional mean above M. Every weight is positive and
their sum is one. Let p_tail=nu((M,infinity)). For all 0<=r<=R,

`|Y_N(r)-Y(r)| <= R*h/2 + p_tail`,

`|F_N(r)-F(r)| <= R*h/(2e) + p_tail`.

The first bound follows from |partial_mu exp(-mu*r)|<=r. The second uses
`|partial_mu[(1+mu*r)exp(-mu*r)]|<=r/e`. For a tighter pointwise tail term
replace p_tail by p_tail exp(-Mr) or p_tail(1+Mr)exp(-Mr), respectively.

For 0<=w<=Omega<=M the tail is absent from both local noise spectra. Write
u_mu=sqrt((w^2-mu^2)_+) and H(u)=u exp(-a^2u^2). The elementary inequalities
`|H'(u)|<=1` and
`|u_mu-u_nu|<=sqrt(2*w*|mu-nu|)` imply the uniform bound

`|j_N(w)-j(w)| <= sqrt(Omega*h)/(4 pi^2)`.

This is a simultaneous static/noise approximation with explicit positive
local realization and controlled absolute error. It is conservative and
does not provide relative control near w=0. Nor does it give a full-band
clock-visibility error without bounding the frequency tail and the actual
control filter. Numerical convergence is reported separately from these
analytic guarantees.

## Frozen experiment and scope

FINITE_LOCAL_CONTRACT.json fixes synthetic parameter grids before running
finite_local_probe.py. Runtime contains hashes, complete results and logs.
The mathematical hypothesis class includes a prescribed vacuum and Gaussian
apparatus smearing; the spectral measure and shared current remain physical
assumptions. No unique TOE, matter representation, cosmology, or observed
constant is selected by this construction.
