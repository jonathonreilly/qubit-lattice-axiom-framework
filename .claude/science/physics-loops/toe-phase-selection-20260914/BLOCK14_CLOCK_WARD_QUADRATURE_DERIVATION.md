# Uniform clock quadrature and discrete Ward residuals

Status: personal proof draft,2026-09-14. No independent review. This concerns
the finite-clock Villain gauge measure, not the native formation law or the
principal-flux penalty Hamiltonian. Its purpose is to identify the exact
finite-clock correction to a continuous-angle proof and a controlled bridge
when clock order is allowed to grow. Fixed-order infrared irrelevance remains
an additional obligation.

## 1. Positive conditional mixture

Let phi_b(u)=sum_{k in Z} exp[-b(u-2pi k)^2/2]. A single oriented link theta
in a finite plaquette complex has conditional weight

 P(theta)=prod_{j=1}^r phi_{b_j}(s_j theta+alpha_j), b_j>0, s_j in {+1,-1}.

Each incident plaquette must traverse this link once, with coefficient+/-1;
self-wrapping complexes with repeated incidence need separate treatment.
By evenness set c_j=s_j alpha_j, Gamma=sum_j b_j. Unwrap each factor and
write k_j=m+n_j with n_r=0. Put d_j=c_j-2pi n_j,
bar_d=Gamma^{-1}sum_j b_j d_j, and

 A_n=exp[-(1/2)sum_j b_j(d_j-bar_d)^2]>0.

Completing the square and summing m gives the EXACT identity

 P(theta)=sum_{n in Z^(r-1)} A_n phi_Gamma(theta+bar_d).

The residual quadratic form is positive definite on n_r=0, so sum_n A_n
converges. All derivatives converge locally uniformly by Gaussian tails.
For r=1 the mixture has a single term. Consequently the normalized continuous
conditional density is a positive mixture with weights A_n/sum_m A_m of
translates of a wrapped normal with precision Gamma. If p_hat(m)=(2pi)^-1 integral P(theta)e^-imtheta dtheta,

 p_hat(m)=p_hat(0) exp[-m^2/(2Gamma)] E_n[e^{im bar_d}],
 |p_hat(m)|<=p_hat(0) exp[-m^2/(2Gamma)].                 (1)

The background may be arbitrarily frustrated. No lower bound on min P and
no replacement of a random neighbor field by its mean occurs.

## 2. Uniform quadrature errors

Q_N F=N^-1 sum_{a=0}^{N-1}F(2pi a/N), Q_infty F=(2pi)^-1 integral F.
Fourier aliasing yields Q_NP=sum_{q in Z}p_hat(qN). Define

 epsilon_K(N,Gamma)=2 sum_{q>=1}exp[-(qN-K)^2/(2Gamma)], 0<=K<N.

Then |Q_NP/Q_infty P-1|<=epsilon_0. More generally, if
f(theta)=sum_{|k|<=K}f_hat(k)e^{iktheta},

 |Q_N(Pf)-Q_infty(Pf)|
 <=Q_infty P * ||f_hat||_1 * epsilon_K.                 (2)

The q=0 Fourier coefficient gives the continuous expectation exactly; for
q nonzero use |qN-k|>=|q|N-K and (1). This is an absolute error estimate,
not a relative estimate when the observable expectation is very small.

A closed geometric upper bound is obtained from q=1+n:
(qN-K)^2>=(N-K)^2+n(3N^2-2NK), n>=0. Therefore

 epsilon_K<=2 exp[-(N-K)^2/(2Gamma)]
              /[1-exp(-(3N^2-2NK)/(2Gamma))].           (3)

This bound only claims sufficiency. An r=1 translate at bar_d=0 saturates
epsilon_0 for the partition-function error.

## 3. Ward residual and its correction

Let J(theta)=-P'(theta)/P(theta). In the isotropic four-dimensional Villain
gauge model r=6 and J= sqrt(beta) sum_{p incident e} s_p Y_p, where
Y_p=-phi_beta'(dtheta_p)/(sqrt(beta) phi_beta(dtheta_p)) is the actual
bounded score. The continuous conditional Ward identity is
E_infty[f'-J f]=0. For the clock measure the numerator is Q_N[(Pf)'], hence

 E_N[f'-J f]= [sum_{q !=0} i qN (Pf)_hat(qN)] / Q_NP.   (4)

For epsilon_0<1 and f bandlimited as above,

 |E_N[f'-J f]|
 <= ||f_hat||_1 D_K/(1-epsilon_0),
 D_K=2N sum_{q>=1}q exp[-(qN-K)^2/(2Gamma)].             (5)

With rho=exp[-(3N^2-2NK)/(2Gamma)],
D_K<=2N exp[-(N-K)^2/(2Gamma)]/(1-rho)^2.
In particular |E_N J|<=D_0/(1-epsilon_0). The sign in the exact f=1
identity is E_N J= -sum_{q !=0} iqN p_hat(qN)/Q_NP.
This conditional mean need not vanish. The local correction
R_e(theta_other)=E_N[J_e|theta_other] produces the exact conditional
mean-zero variable J_e-R_e. Its existence alone is not a long-distance
Gaussian theorem. Nor may R_e simply be discarded at fixed N,beta because
it is exponentially small in N^2/beta.

For a source f not bandlimited, (4) remains exact under sufficient Fourier
summability, but (5) must be replaced by the full convolution sum. We do not
apply a finite-frequency bound to exponentials of nonlinear scores by fiat.

## 4. Full lattice comparison without a volume-exponential loss

Uncoupled integrated links compare exactly for frequencies |j_e|<N and
may be removed first. Let E be the number of remaining integrated links,
Gamma_e=sum_{p incident e}b_p, and
Gamma_*=max_e Gamma_e. Clock and U(1) models use the same positive Villain
plaquette product and normalized a priori one-link measures; no gauge fixing
is needed in finite volume. Fix or integrate boundary links consistently.
Assume Gamma_*>0 and epsilon_0(N,Gamma_*)<1. Define the E+1 hybrid measures
by replacing one link measure at a time from Haar to N-clock. The conditional
bounds are uniform over the remaining links, regardless of whether those
links are clock or continuous.

Write Z_i,A_i for unnormalized partition function and Fourier-character
numerator at hybrid i, F_j(theta)=exp[i sum_e j_e theta_e], |j_e|<=K<N.
Integrating the one changed link and then the positive measure of the rest,

 |Z_i-Z_{i-1}|<=epsilon_0 Z_{i-1},
 |A_i-A_{i-1}|<=epsilon_K Z_{i-1},
 |A_{i-1}|<=Z_{i-1}.

It follows by a one-step ratio estimate and telescoping that

 |<F_j>_clock-<F_j>_U(1)|
 <=min[2, E*(epsilon_K+epsilon_0)/(1-epsilon_0)].        (6)

The partition functions separately obey
 (1-epsilon_0)^E <=Z_clock/Z_U(1)<=(1+epsilon_0)^E.      (7)

For a finite Fourier polynomial F, sum (6) with its coefficient absolute
values. It also extends to absolutely convergent Fourier series with the
corresponding mode-dependent bound summed, when finite, using the trivial
bound2 for any mode whose link frequency is at least N. This does not
assert total-variation closeness of atomic and continuous angle measures.
Gauge-invariant integer Wilson characters are included in (6), with max
link charge K. A relative Wilson ratio still requires the absolute error
small compared with the denominator: (6) alone does not supply that.

A useful sufficient family, with delta>0 fixed, is

 N-K >= sqrt[2 Gamma_* (1+delta) log E],

provided rho is bounded away from1. Then E epsilon_K ->0 (E->infinity),
while E epsilon_0<=E epsilon_K. For example fixed Gamma_*, fixed K and
N=ceil[K+sqrt(2 Gamma_* (1+delta) log(2E))] works. At fixed beta this costs
clock order of order sqrt(log E), but transfers only those U(1) conclusions
whose observables and absolute error tolerances meet (6). It does not prove
an intrinsic continuum limit for fixed clock order.

For local force residuals (5), the extra factor N and any number of tested
links must also be included. A volume sum E D_K ->0 follows, for example,
from the same family at fixed Gamma_*,K and delta>0 because N~sqrt(log E).
The total local Fourier frequency of an observable, not merely a nominal
charge label, controls which estimate applies.

## 5. Sharp distinctions and elementary controls

For r=1, theta shift c nonzero, the conditional force generally has a
nonzero mean because the trapezoidal derivative has nonzero aliases.
At N=2,c=pi/2 the symmetry can force this mean back to zero; use a generic
shift such as c=0.37 to test it. Some symmetric backgrounds have zero mean;
there is no uniform nonzero lower bound.

At r=1,c=0, the clock expectation of e^{iN theta} is exactly1. The U(1)
expectation is exp[-N^2/(2Gamma)], which may be arbitrarily small. Thus an
unrestricted Fourier/Wilson observable comparison cannot follow from a
small epsilon_0. The K<N condition and shifted Gaussian tail matter.

A positive product of strongly concentrated factors can make min P tiny.
The mixture estimate avoids dividing by that minimum, retaining the natural
alias exponent N^2/(2Gamma). Its weakness for fixed N as E grows remains
real for this uniform telescoping proof. It is not evidence that the actual
fixed-clock Coulomb phase is absent.

## 6. Relation to the fixed-law research target

Driver1987 uses Haar integration by parts on closed-test current observables.
Equations(4)-(5) display precisely the finite-clock replacement. Its current
limit is not imported here as a theorem identifying the full photon field. The next nontrivial step is control of the connected
physical-score correlations or a renormalization argument proving the
alias operators irrelevant, not silently reinstating Haar differentiation.

Dario-Wu, Massless Phases for the Villain Model in d>=3, author PDF dated
March27,2023, section3pp16-36, maps a low-temperature rotator Coulomb gas
through a one-step Gaussian split and cluster expansion to a small gradient
perturbation of a vector Gaussian field, then studies a Helffer-Sjostrand
operator. That does not directly treat a finite-clock gauge field with both
electric and magnetic defects. Its connected-defect method is a promising
next construction, with a fresh representation and hypotheses to prove.

[Driver1987, author-hosted paper](https://mathweb.ucsd.edu/~bdriver/DRIVER/Papers/Drivers_Papers/A1-U%281%29_4-Lattice.pdf)
[Dario-Wu2023, author-hosted manuscript](https://pauldario.pages.math.cnrs.fr/webpage-of-paul-dario/Villain3D__short_version_.pdf)
