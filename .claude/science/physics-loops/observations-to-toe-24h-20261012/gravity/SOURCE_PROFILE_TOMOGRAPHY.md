# Constructive recovery of layered source charges

Status: conditional-support; frontier discovery. This is a mathematical inverse
map inside the shared positive scalar mechanism. It is not a reconstruction of
Earth's scalar charge from existing data. The distinction between exact rank and
conditioning is essential.

## Supplied source and response

Consider two spherically symmetric source components C and M with positive mass
fractions f_C,f_M. Their normalized radial mass measures are p_C(du),p_M(du).
Every core radius is smaller than every mantle radius, apart from a possible
common boundary of zero mass. Each component has one constant scalar charge per
unit mass alpha_C or alpha_M. These can have either sign. The common mediator
measure nu is nonnegative, finite, nonzero and known; its support includes at
least two distinct masses. Units are hbar=c=1 and mu is inverse length.

For r outside the source, define

`F_i(mu)=integral sinh(mu*u)/(mu*u) p_i(du)`,

`K_i(r)=integral F_i(mu) (1+mu*r) exp(-mu*r) nu(dmu)`.

The scalar acceleration divided by its known bare GM/r^2 and probe charge is

`A(r)=f_C alpha_C K_C(r)+f_M alpha_M K_M(r)`.

This is an assumed measurable source-amplitude map. A differential acceleration
actually contains a test-charge contrast: if that contrast is unknown or zero,
two reported null accelerations do not directly supply A(r). Metric terms,
orbital reference normalization, source multipoles and detector transfer must
also be resolved before using this idealized inverse map on an experiment.

## Strict radial ordering and a two-radius inverse

For mu>0, the logarithmic mu derivative of the shell factor is

`partial_mu log[sinh(mu*u)/(mu*u)] = u*coth(mu*u)-1/mu`.

It increases strictly with u>0: writing z=mu*u, the needed inequality is
`sinh(z)cosh(z)>z`. Averaging this derivative with each component's positive
shell-factor weights shows that

`R(mu)=F_C(mu)/F_M(mu)`

decreases strictly with mu>0, with its continuous limit R(0)=1. Radial ordering
of the actual component supports, not just different mean radii, is used here.

At fixed exterior r, normalize the positive measure

`p_r(dmu) proportional to F_M(mu)(1+mu*r)exp(-mu*r)nu(dmu)`.

Then K_C/K_M=E_p[R] and differentiation gives

`partial_r(K_C/K_M) = Cov_p(R(mu), L_r(mu))`,

`L_r(mu)=partial_r log[(1+mu*r)exp(-mu*r)]
        = -r*mu^2/(1+mu*r)`.

For r>0 both R and L_r decrease strictly in mu. Their covariance equals
one half the double integral of
`[R(mu)-R(lambda)][L_r(mu)-L_r(lambda)]`; it is strictly positive when the
measure has at least two distinct masses. All derivatives are dominated for
exterior r because source support is bounded. Thus K_C/K_M increases strictly
with r.

At any two distinct exterior radii r1<r2,

`D=K_C(r1)K_M(r2)-K_C(r2)K_M(r1)<0`.

The charges are constructively recovered by

`alpha_C=[A(r1)K_M(r2)-A(r2)K_M(r1)]/(f_C D)`,

`alpha_M=[K_C(r1)A(r2)-K_C(r2)A(r1)]/(f_M D)`.

This is a positive injectivity result for the stated linear inverse problem.
For a single mass, including a massless pole, K_C/K_M is constant and D=0:
one can cancel the integrated source while leaving both component charges
nonzero. The multi-mass hypothesis changes that specific inverse map.

The result also does not hold as stated for overlapping or well-mixed component
profiles, mass-dependent matter-coupling directions, unknown spectral measure,
screening, or an arbitrary nonspherical instrument response. Those are distinct
model choices, not failures of the displayed conditional calculation.

## Stable gamma-measure shell formula

For nu(dmu)=ell exp(-ell*mu)dmu, put L=ell+r and z=u/L. Direct mass integration
gives the point-normalized shell potential and force factors

`P(r,u)=ell/L * atanh(z)/z`,

`K(r,u)=ell/L * [atanh(z)/z + (r/L)/(1-z^2)]`.

The ratio at z=0 is one. The expression follows by integrating the difference
of exp[-mu(r-u)] and exp[-mu(r+u)]; it is finite for r>u. It explicitly retains
the source radius rather than replacing its composition by one averaged charge.

For a uniform ball of radius R, a numerically stable positive series is

`K_ball(r,R)=ell/L sum_{n>=0} (R/L)^(2n)
            * [1/(2n+1)+r/L] * 3/(2n+3)`.

A uniform mantle between R_C and R is obtained by subtracting the core volume
integral and dividing by the mantle volume. No density or isotope uncertainty is
encoded in the word uniform: it is an explicit model assumption.

## Conditioning and the observational obligation

Let M have rows (f_C K_C(r_i), f_M K_M(r_i)). For known kernels and a supplied
source-amplitude covariance Sigma_A, the linear covariance is
`Sigma_alpha=M^(-1) Sigma_A M^(-T)`. Errors in the kernels are additional
nuisances. Even though det(M) is nonzero, its smallest singular value can be
extremely small in a long-range regime; exact uniqueness need not yield a useful
constraint from noisy data.

The frozen synthetic calculation uses a uniform Fe-like core with mass fraction
.32, a uniform outer component with fraction .68, core radius .55R, R=6.371e6 m,
and r/R=1, (R+710000)/R, 2. The outer-surface value is the exterior limiting
value. ell is 1e7,1e9,1e11,1e13 m. These geometry choices are supplied diagnostic
inputs, not Earth tomography or an experimental likelihood. The condition number
uses the dimensionless source amplitudes as defined above, with no implicit
reweighting by measurement precision. Independent proof/check is pending.
