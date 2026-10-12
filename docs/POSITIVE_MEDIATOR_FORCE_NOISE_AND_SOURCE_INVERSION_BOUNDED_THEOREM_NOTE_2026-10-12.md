# Positive mediator force, vacuum noise, and source inversion

Date: 2026-10-12.
Claim type: bounded_theorem
Status: conditional-support
Audit authority remains the independent audit lane.

```yaml
actual_current_surface_status: conditional-support
target_claim_type: bounded_theorem
trace_class: frontier_discovery
target_claim_id: null
target_blocker_text: null
source_of_blocker_text: user_goal
reachability_to_target: unknown_frontier
artifact_role: theorem
next_trace_action: apply the common response to frozen source and noise data
conditional_surface_status: positive free scalar measures and declared source profiles
hypothetical_axiom_status: alternative physical candidate explicitly authorized for exploration
admitted_observation_status: no measured value fitted or inferred in this theorem packet
claim_type_reason: constructive joint approximation and conditional source-charge inverse
audit_required_before_effective_retained: true
bare_retained_allowed: false
```

Primary runner: [positive_mediator_inverse_2026_10_12.py](../scripts/positive_mediator_inverse_2026_10_12.py).
Inputs: [fixed diagnostic contract](../scripts/data/positive_mediator_inverse_2026_10_12.json).
Output: [content-pinned runner cache](../logs/runner-cache/positive_mediator_inverse_2026_10_12.txt).
Campaign: [handoff](../.claude/science/physics-loops/positive-response-milestone-20261012/HANDOFF.md).

## Target and physical meaning

**Target.** A supplied nonnegative scalar mass measure admits positive finite
local-field realizations with explicit simultaneous static/noise approximation
bounds; for a known measure with at least two masses, two exterior radii give
an injective two-component source-charge map under ordered radial profiles.

The observation-first question is concrete: when a candidate uses one mediator
to explain forces, what source information and fluctuation response accompany
it? This note constructs that forward map and its conditional inverse. It
does not identify the scalar with an observed gravitational wave or with all
gravity. No observation selects the spectral measure, state, or charges here.
The existing four-axiom framework is not a premise of this alternative model.

Three connected results are proved below: positive local approximation with
one force/noise measure; an explicit pair of finite and continuum responses;
and an injective two-radius source map with quantified long-range conditioning.
The numerical checks inspect those formulas. They are not the proofs or a
fit to an experiment.

## Premises, imports, and obligation graph

| Input | Role and provenance | Physical identification still open |
|---|---|---|
| Minkowski metric, canonical scalar action, external current | Supplied candidate dynamics; free-field normalization derived below | Matter currents, curved/interacting completion and cutoff |
| Finite positive Borel measure nu on nonnegative masses | Supplied common spectral response; normalization one unless stated | Selection from data or more basic dynamics |
| Centered free vacuum and Gaussian spatial profile of width a>0 | Supplied state and apparatus preparation | Actual state, source size, switching and detector filter |
| Gamma measure with s,ell>0 | Explicit example, not an observed distribution | Whether any sector uses it |
| Ordered core/mantle radial probabilities and known probe charge | Hypotheses of the inverse theorem | Real source profiles, couplings and correlated errors |
| Hermite interpolation, positive Laguerre quadrature, covariance identity | Mathematical tools, with needed remainder and sign arguments given here | No physical premise adoption implied |

The dependency graph is action/normalization -> static and vacuum kernels ->
positive quadrature/bins -> joint bounds. Independently, shell averaging ->
ordered form-factor ratio -> positive covariance -> nonzero determinant ->
explicit inverse and small-mass expansion. These mathematical steps are proved
here. The principal downstream physical obligation is a calibrated map from
measured counts, frequencies or accelerations to the stipulated current and
state, with backgrounds and nuisance covariance. That obligation is stronger
than evaluating the kernels and is not treated as proved.

## 1. One response measure and a finite local action

Use hbar=c=1 and metric signature (-,+,+,+). For masses mu_j>=0 and weights
w_j>0 with sum w_j=1, set Phi_N=sum_j sqrt(w_j) phi_j and supply

\[
 S_N=\int d^4x\left[-\frac12\sum_j
 ((\partial\phi_j)^2+\mu_j^2\phi_j^2)+J\Phi_N\right]. \tag{1}
\]

Each finite member has positive free kinetic energy, a local second-order
equation, and a classical stress tensor. Its composite two-point function is
the weighted sum of free Klein-Gordon two-point functions. Consequently its
mass measure is nu_N=sum w_j delta_mu_j. An Einstein term or interacting
matter action can be supplied as an additional effective theory; neither is
derived by (1).

For any normalized positive nu, the static potential of two point charges is

\[
 V(r)=-\frac{g_Ag_B}{4\pi r}Y(r),\quad
 Y(r)=\int e^{-\mu r}d\nu(\mu),\quad
 H(r)=\int(1+\mu r)e^{-\mu r}d\nu(\mu). \tag{2}
\]

The inward force is g_A g_B H/(4 pi r^2). The retarded response, with the
Fourier convention exp(-i omega t), is
`chi_R(omega,k)=integral dnu/[k^2+mu^2-(omega+i0)^2]`.
For the spatial profile with Fourier transform exp(-a^2 k^2/2), write
`W_a^+(t)=integral_0^infinity j_a(omega) exp(-i omega t) domega`. Direct
on-shell integration of d^3k/[(2pi)^3 2 sqrt(k^2+mu^2)] yields

\[
 j_a(\omega)=\frac{1}{4\pi^2}\int_0^\omega
 \sqrt{\omega^2-\mu^2}\,
 e^{-a^2(\omega^2-\mu^2)}d\nu(\mu),\quad \omega>0. \tag{3}
\]

Thus force, retarded dynamics, and this specified vacuum correlation use the
same weights. Coupling to a prepared system supplies its influence functional
through that common current. Different temperature, nonequilibrium state or
readout are different physical inputs, not changes fixed by static force alone.

For

\[
 d\nu=\ell^s\mu^{s-1}e^{-\ell\mu}d\mu/\Gamma(s),
 \qquad Y=(1+r/\ell)^{-s},\quad
 H=Y[1+sr/(\ell+r)], \tag{4}
\]

the low-frequency coefficient follows by mu=omega u and dominated convergence:
`j_a(omega)/omega^(s+1) -> ell^s B(s/2,3/2)/(8pi^2 Gamma(s))`.
The mass decay in (4) does not remove large spatial momenta; the stated spatial
profile is a separate ultraviolet condition for local noise observables.

## 2. Positive local approximations on declared windows

Put x=ell mu and t=r/ell. Normalized generalized Laguerre quadrature gives
positive nodes x_j and weights w_j, integrating polynomials through degree
2N-1 against x^(s-1)exp(-x)/Gamma(s). The monic polynomial p_N has norm
`integral p_N^2 dnu_x=N! Gamma(N+s)/Gamma(s)`.
Hermite interpolation of a smooth f at its N simple nodes gives remainder
`f^(2N)(xi_x) p_N(x)^2/(2N)!`; integrating gives

\[
 0\le Y-Y_N\le B_N(s,t),\quad
 |H-H_N|\le(2N-1)B_N(s,t),\quad
 B_N=\frac{N!\Gamma(N+s)t^{2N}}{(2N)!\Gamma(s)}. \tag{5}
\]

The potential derivative is t^(2N)exp(-tx). For the force it is
`t^(2N)[tx-(2N-1)]exp(-tx)`, whose absolute value is at most
`(2N-1)t^(2N)` for x,t>=0. These bounds are absolute and window-specific.
The unbounded integration domain is harmless for the bound: the pointwise
Hermite remainder is integrable against the displayed polynomial norm.

A second positive construction gives a joint uniform bound without relying
on a high-order derivative. Partition [0,M] into bins of width h, use each
bin's exact probability at its midpoint, and put the tail probability p at
its conditional mean above M. Omit zero-weight bins and a zero-weight tail.
For the gamma measure that mean is finite.
For any positive measure the same bounds hold with any chosen tail atom
strictly above M. For 0<=r<=R and 0<=omega<=Omega<=M,

\[
 |Y-Y_N|\le Rh/2+p,\quad
 |H-H_N|\le Rh/(2e)+p,\quad
 |j_a-j_{a,N}|\le\frac{\sqrt{\Omega h}}{4\pi^2}. \tag{6}
\]

For (2), derivatives in mu are bounded by r and r/e. Both tail integrals lie
between zero and p, giving the tail term p. For (3), let
`u_mu=sqrt((omega^2-mu^2)_+)` and `F(u)=u exp(-a^2u^2)`.
Then |F'|<=1 and |u_mu-u_eta|<=sqrt(2 omega |mu-eta|); inside a bin,
|mu-eta|<=h/2. The tail vanishes in both spectra for omega<=M. Integrating
the binwise bound proves (6). Taking M large and h small constructs finite
positive local models with arbitrarily small joint absolute error on any
fixed finite r/omega windows. Relative error at omega=0 is not part of (6).

### Explicit finite/continuum response pair

For s=ell=1, a=.25 and N=8, the Laguerre model gives
`Y(1)=.5-7.366755e-8` while `j_N(.1)=0`; the continuum has
`j(.1)=1.90653258e-4`. The finite gap begins at x_min≈.1702796323.
All quantities are dimensionless diagnostics in the selected units. They are
an explicit jointly computed response pair, with no apparatus sensitivity
or empirical exclusion asserted. N=16 and alternative bins are separate
positive realizations; (6) supplies a constructive accuracy choice.

## 3. Two-radius source-charge inversion

Let p_C(du),p_M(du) be normalized nonnegative radial source measures with
every core radius at most every mantle radius, and strict inequality on a set
of positive product measure. All radii are at most R. Set

\[
 F_i(\mu)=\int\frac{\sinh(\mu u)}{\mu u}dp_i(u),\quad
 K_i(r)=\int F_i(\mu)(1+\mu r)e^{-\mu r}d\nu(\mu),\ r>R. \tag{7}
\]

Angular integration of a spherical shell gives its exterior potential
`exp(-mu r)sinh(mu u)/(mu u r)`. Differentiating in r gives (7).
The removable value at mu u=0 is one. A finite nonzero positive nu and
strict exterior separation ensure the integrals and derivatives converge.

The logarithmic mass derivative of a shell factor is
`m(u,mu)=u coth(mu u)-1/mu`. Its u derivative is
`coth(z)-z csch(z)^2>0` for z>0: multiply by sinh(z)^2 and use
`sinh(2z)>2z`. The logarithmic derivatives F_i'/F_i are positively tilted
averages of m over the ordered supports. Thus q(mu)=F_C/F_M strictly
decreases on positive masses, with q(0)=1 and q(mu)<1 for mu>0.

Under the probability measure proportional to
`F_M(mu)(1+mu r)exp(-mu r)dnu`, differentiation gives

\[
 \frac{d}{dr}\frac{K_C}{K_M}
 =\operatorname{Cov}_r\left(q(\mu),-\frac{r\mu^2}{1+r\mu}\right)>0. \tag{8}
\]

Both arguments strictly decrease with mu; the identity
`2 Cov(f,g)=E[(f(X)-f(Y))(g(X)-g(Y))]` for independent copies proves strict
positivity when nu has at least two distinct support masses, including a
possible mass-zero atom. Hence for r1<r2 both strictly exterior,

\[
 D=K_C(r_1)K_M(r_2)-K_C(r_2)K_M(r_1)<0. \tag{9}
\]

Let f_C,f_M>0, f_C+f_M=1, be known source mass fractions, alpha_i be constant scalar
charge per mass within each component, and q_P be known nonzero probe charge
per mass. An isolated scalar acceleration obeys
`y(r)=4pi r^2 a(r)/(q_P M_source)=f_C alpha_C K_C+f_M alpha_M K_M`.
The exact inverse is

\[
 \alpha_C=\frac{y_1K_M(r_2)-y_2K_M(r_1)}{f_CD},\qquad
 \alpha_M=\frac{K_C(r_1)y_2-K_C(r_2)y_1}{f_MD}. \tag{10}
\]

The two charges recovered here are conditioned on known nu, profiles, mass
fractions and q_P, and on subtraction of other forces. For an unknown probe
coupling the measured combinations are products. A differential experiment
with zero probe-charge contrast supplies zero of this specific differential
signal even if source fields are present.

Exact single-mass and equal-profile controls have D=0; coincident radii and
zero source fractions also remove this two-column inverse. Signed weights,
unordered profiles, mass-dependent material couplings, nonlinear screening and
unknown source/probe profiles are separate hypothesis classes. No conclusion
about their inverse maps is asserted here.

## 4. Conditioning and a resolved numerical example

For fixed geometry and a gamma family scaled to large ell, write
`Delta_a2=<u^2>_M-<u^2>_C>0`. Taylor expansion of (7)-(8) gives

\[
 |D|\sim\frac{\Delta_{a2}(r_2^2-r_1^2)}{12}
 \operatorname{Var}(\mu^2),\quad
 \operatorname{Var}(\mu^2)=\frac{2s(s+1)(2s+3)}{\ell^4}. \tag{11}
\]

The first relation follows from q=1-Delta_a2 mu^2/6+O(mu^4) and
`partial_r log[(1+mu r)exp(-mu r)]=-r mu^2+O(mu^3)`.
Gamma moments and the finite fixed source support justify this asymptotic
expansion. For the matrix whose rows are `(f_C K_C,f_M K_M)`,

\[
 \kappa_2\sim\frac{12(f_C^2+f_M^2)\ell^4}
 {f_Cf_Ms(s+1)(2s+3)\Delta_{a2}(r_2^2-r_1^2)}. \tag{12}
\]

Use the synthetic spherical geometry R=6371000 m, core radius .55R,
f_C=.32,f_M=.68, uniform density within each component, s=1, and
radii R and R+710000 m. The first radius is a surface limit, where this
exponentially decaying gamma measure controls derivatives separately.
It is not substituted into the general arbitrary-measure r>R theorem.

| ell (m) | D of the mass-fraction-weighted matrix | kappa_2 |
|---:|---:|---:|
| 1e7 | -5.141127411e-4 | 1.701379621e3 |
| 1e9 | -6.8073091e-11 | 1.659270903e10 |
| 1e11 | -7.0556156e-19 | 1.600994232e18 |
| 1e13 | -7.0581553e-27 | 1.600418167e26 |

This is exact rank with increasingly poor conditioning. The displayed
condition number uses the specified row normalization and source parameters;
an experiment needs noise whitening and parameter scales before turning it
into a precision requirement. No terrestrial source-charge estimate is made.

For independent evaluation, the uniform ball has
`F_ball(mu)={}_0F_1(;5/2;mu^2 R^2/4)`. At s=1, beta=1+r/ell,
z=[R/(ell+r)]^2, mass integration gives

\[
 K_{ball}=\frac{{}_2F_1(1/2,1;5/2;z)}{\beta}
 +\frac{r/\ell}{\beta^2}{}_2F_1(1,3/2;5/2;z). \tag{13}
\]

Alternatively average the elementary shell kernel
`ell/(ell+r)[atanh(v)/v + (r/(ell+r))/(1-v^2)]`, v=u/(ell+r),
over radius. These radial and mass-space formulas supply separate numerical
checks. High precision is essential for the smallest determinants.

## Verification and scope

The primary runner uses the fixed contract to independently
compare a finite mass-matrix resolvent to its spectral sum, check the
quadrature and bin bounds, compute the explicit response pair, and compare
source kernels by shell integration and mass-space hypergeometric evaluation.
It prints each check family and a total. Mutation probes and source-bound
independent review are recorded in the linked campaign packet, together with
their exact file hashes. The runner cache records actual execution; it is
not an audit verdict or a substitute for the proofs above.

The construction supplies a common force/noise model and a conditional source
inverse. Its matter operators, state selection, spectral parameters, actual
apparatus transfer functions and statistical inference remain scientific
inputs to future tests. A complete gauge/matter/cosmological architecture is
not claimed. No measured constant, unique theory of everything, adopted
physical premise, or retained-grade status is established by this note.
