# Matter vacuum corrections and the analytic cosmological candidate

Parent derivation before execution, 2026-10-13. This is conditional support
inside the observations-first campaign. The starting observations are the
measured electron mass and gravitational normalization, alongside the already
exposed photon temperature. H0=70 km/s/Mpc and m=0.3 remain supplied benchmark
parameters. None of them is newly predicted. This block asks how a known
massive matter sector changes the previously constructed cosmological action.
It does not equate an unrenormalized loop contribution with an observed
cosmological constant or infer exclusion from a naturalness estimate.

## Explicit quantum and frame assumptions

Use the prior Einstein action
S_g=integral sqrt(-g)[M_E^2 R/2-M_E^2 K_AB partial phi^A.partial phi^B
                    -2M_E^2 V],
with M_E^2=1/(8pi G*), phi=(u,x,y), A=exp(sqrt(a)u), and physical matter
metric g_J=A^2 g. Matter masses and dimensionless couplings are constant in
Jordan units. We integrate matter fluctuations only on a classical external
metric. Internal gravitons, u/x/y quanta and their mixed loops are excluded.
Assume a Jordan diffeomorphism invariant regulator, measure and counterterms
so that the matter effective action is a functional of g_J alone. This is a
specified quantization prescription, not a derived ultraviolet theory.

Its local derivative expansion at zero derivatives has the form

  Gamma_m^(0)=-integral sqrt(-g_J) rho_J
            =-integral sqrt(-g) A^4 rho_J.

Here rho_J is the total renormalized matter vacuum coefficient in the
specified scheme and scale. Therefore

  delta V=C exp(4sqrt(a)u), C=rho_J/(2M_E^2).

All its field derivatives are correlated: d_u^n delta V=(4sqrt(a))^n delta V.
One Jordan vacuum counterterm has the same entire field dependence. Choosing
the renormalized coefficient rho_J=0 removes this zero-derivative term and
all these derivatives. This is one operator-level renormalization condition;
it is not independent tuning of every Taylor coefficient. It also does not
explain why that condition holds or why the supplied H_v is small. Higher
derivative terms and gravitational/scalar quantum loops are not removed.

The finite polynomial potential of the classical candidate does not contain
this exponential operator. The effective action must admit it and the
corresponding counterterm when matter is quantized. Keeping only a constant
Einstein-frame subtraction at u=0 would leave C(A^4-1), including its nonzero
u tadpole and mass. A statement about cancellation only at u=0 is therefore
weaker than cancellation of the full covariant matter-vacuum operator.

## Free Dirac benchmark and scale matching

For one free Dirac field in four dimensions, use the MS-bar finite part

  rho_1,J(mu_J)=-m_e^4/(16pi^2)[ln(m_e^2/mu_J^2)-3/2].

It follows by integrating the mass derivative of the Euclidean determinant
-2 mu^(2epsilon) integral d^(4-2epsilon)p/(2pi)^(4-2epsilon)
ln(p^2+m_e^2), with the MS-bar pole removed. The free-field mass is held
fixed in this benchmark. At mu_J=m_e the displayed finite part is
+3m_e^4/(32pi^2). Its absolute value and sign are scheme dependent; it is
not itself an observable vacuum density. In particular it vanishes at
mu_J=m_e exp(-3/4), which does not remove the running counterterm.

  d rho_1,J/d ln(mu_J)=m_e^4/(8pi^2),
  d rho_ct,J/d ln(mu_J)=-m_e^4/(8pi^2)

makes rho_1,J+rho_ct,J scale independent in this free one-loop example.

For a constant background u, m_e,E=A m_e,J. Matched physical scales obey
mu_E=A mu_J, and the determinant finite part is then A^4 rho_1,J(mu_J).
If one instead fixes the same numerical mu in Einstein units, the naive
finite part differs by

  rho_1,E(fixed mu)-A^4 rho_1,J(mu)
       =-A^4 m_e^4 ln(A)/(8pi^2).

Representing the same Jordan-defined theory in that convention requires the
opposite finite local matching term. We do not silently drop it or assume
that two different measure/counterterm prescriptions define the same theory.
For nonconstant fields the full pulled-back effective action, including
derivative operators and the measure, must be transformed consistently.

## Canonical mass normalization and the observation scale

At the classical vacuum phi=0, the canonical u field is
varphi_u=sqrt(2)M_E u. Define rho_target=3M_E^2 H_v^2, which is the supplied
future vacuum density of the original action, and R=rho_J/rho_target. Then

  delta V/H_v^2=3R/2,
  delta V_u/H_v^2=6sqrt(a)R,
  delta m_u^2/H_v^2=delta V_uu/H_v^2=24aR.

The last coefficient follows from delta m_u^2=8a rho_J/M_E^2. It is a
mass correction evaluated at the OLD origin, which generally ceases to be
stationary; it is not automatically the mass at the new vacuum. No bound
on a follows without extra assumptions about counterterms and measurements.

Use exact h,c and measured m_e,G_N from the pinned NIST CODATA 2022 table.
The imported weak-field normalization G_N=(1+a)G* implies
M_E^2=(1+a)M_N^2. It is used as an input bridge, not established anew for
the cosmological action. In SI energy units,

  M_E,energy^2=(1+a) hbar c^5/(8pi G_N),
  rho_loop,SI=3(m_e c^2)^4/[32pi^2(hbar c)^3] at mu_J=m_e,
  rho_target,SI=3M_E,energy^2(hbar H_v)^2/(hbar c)^3
               =3(1+a)c^2 H_v^2/(8pi G_N),
  H_v=H0 sqrt(1-m-Omega_gamma).

Omega_gamma is the existing exposed photons-only thermal calibration.
The mass uncertainty is propagated as a measurement uncertainty; uncertainty
in the counterterm, cosmological model or renormalization convention is not
a Gaussian measurement error. No likelihood, refit or independent test is
claimed by this scale comparison.

## Full nonlinear response to a positive residual coefficient

Now take the EXTRA ASSUMPTION C>=0 as a real specified residual coupling,
keeping the other classical potential parameters fixed. This is a different
conditional model. The positive electron MS-bar term with zero counterterm
is one illustrative member, not a physical prediction.

For C>0, the unique stationary point has x=y=0 and u=u_v<0, where

  nu H_v^2 u_v+4sqrt(a)C exp(4sqrt(a)u_v)=0.
  w=W_0(16a C/(nu H_v^2))=W_0(24aR/nu),
  u_v=-w/(4sqrt(a)), A_v=exp(-w/4).

For C=0 take w=u_v=0. Direct substitution gives

  V_min/H_v^2=3/2+nu(w^2+2w)/(32a),
  H_E,v^2/H_v^2=1+nu(w^2+2w)/(48a),
  H_J,v/H_v=(H_E,v/H_v)/A_v,
  m_u,v^2/H_v^2=nu(1+w),
  m_x,v^2/H_v^2=9/4+9w/(8a)+9w^2/(16a^2),
  m_y,v^2/H_v^2=2.

These scalar masses use the metric K at x=y=0. Mixed derivatives vanish at
that point. The physical Jordan tensor Planck coefficient is M_E^2/A_v^2.
Thus the ratio of the tensor gravitational coefficient to its u=0 value is
A_v^2; this alone is not a Cavendish prediction, which also needs scalar
ranges and a source/readout calculation. A large u displacement cannot be
interpreted as vacuum relaxation while silently keeping that gravitational
normalization fixed.

The prior global homogeneous convergence proof extends for each fixed C>=0.
The extra exponential is nonnegative, leaving the original coercive lower
bound on fields and a positive energy floor. Energy still obeys
Edot=-3H[T+sigma+4r/3], with the same matter-exchange cancellation. Compact
energy sublevels bound fields, velocities and densities and keep H>=H_v.
At the zero-dissipation invariant set, x=y=0 follows from f(u)>0 and a>0.
The remaining function nu H_v^2 u+4sqrt(a)C exp(4sqrt(a)u) is strictly
increasing from negative to positive values and has exactly one zero.
LaSalle therefore yields convergence to this shifted vacuum for arbitrary
finite homogeneous initial states on the expanding positive-fluid branch.
The argument does not prove spacetime stability or select a cosmological
history. For C<0 the exponential need not preserve the coercive bound, and
that extension is not asserted.

## A derivative operator that remains outside the cancellation

An induced Jordan curvature term zeta/2 integral sqrt(-g_J) R_J becomes,
for s=ln A,

  zeta/2 integral sqrt(-g) A^2[R-6 Box s-6(partial s)^2]
  = integral sqrt(-g)[zeta A^2 R/2+3zeta A^2(partial s)^2]
    + boundary term.

The integration by parts is necessary. This operator changes the scalar
and gravitational derivative terms; a vacuum counterterm does not cancel
it. We do not assign a numerical zeta from the electron determinant here.
Curvature-squared terms, finite-temperature effects, higher-loop matter
interactions and dynamical gravity/scalar loops also remain outside the
free zero-derivative calculation.

## Source roles and next checks

The electron table is measured calibration. The analytic action and its
homogeneous proof are inherited from the parent's earlier checked block.
The determinant prescription is an explicitly imported QFT convention,
re-derived by the mass derivative above. Burgess (2013), sections 1.3-1.4,
provides context for distinguishing renormalized vacuum energy from technical
naturalness; this block does not use a literature estimate as a prediction.

The new work here is the candidate-specific operator, normalization,
nonlinear stationary solution and scoped extension of its energy argument.
Before drawing numerical conclusions, freeze the measured/imported inputs,
scheme, parameter grids, tolerances and complete source. Compare determinant
identities, independent SI forms, operator derivatives, scale running,
Lambert-W stationary solutions against an independent monotone root,
canonical masses and the curvature integration-by-parts identity. All
initial assumptions, failed checks and independent findings must remain
visible.
