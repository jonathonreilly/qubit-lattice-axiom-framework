# Radiation and dust era selection in the analytic candidate

Parent calculation, before execution, 2026-10-13. This block asks whether
nearby homogeneous histories approach the particular fluid scaling curve
that was constructed from the exposed expansion benchmark. It imports the
explicit three-field action in direct_analytic_fluid_completion, whose
homogeneous proof has been independently checked. Its implementation review
is still pending. No new empirical sample or likelihood is supplied here.

## Quantities and limiting domains

Write Omega=a/(1+a), d=1/(1+a), c=2(1+a)/3 and
f(u)=a/2-sqrt(a)u+2u^2, with fixed a,nu,H_v>0.
The dust limit takes x>0 large, y/x -> 0, r/(H_v^2 x^2) -> 0,
with finite u and u_N. Then K_xx x^2 tends to beta_m=2a/[3(1+a)].
The radiation limit takes y>0 large, x/y -> 0,
sigma/(H_v^2 y^2) -> 0 and uses beta_r=a/[2(1+a)].
These are limiting autonomous systems. They are not exact finite-x or
finite-y reductions, uniform theorems through equality, or global attraction
to the observed cosmological history. The supplied nu restoring term remains
in the full theory but is suppressed relative to H^2 in these limits.

## Dust-dominated limiting system

Use U=u/sqrt(a), V=U_N, P=(ln x)_N, W=sigma/(H_v^2 x^2)>0.
Let F=H^2/(H_v^2 x^2), h=H_N/H. Then

  f/a=1/2-U+2U^2,
  F=2[W+a(1/2-U+2U^2)]/[3-aV^2-beta_m P^2],
  h=-W/F-aV^2-beta_m P^2,
  U_N=V,
  V_N=-(3+h)V-[-1+4U+W]/F,
  P_N=-(3+h)P-2a(1/2-U+2U^2)/(beta_m F),
  W_N=W[-3+aV-2P].

The constructed scaling equilibrium is E0=(U,V,P,W)=(0,0,-3/2,1).
There is a second positive-density scaling equilibrium
E1=(-1/2,0,-3/2,3). Their F values are c and 3c. Thus an amplitude relation
between the dust field and dust fluid is a dynamical question even though
both limiting histories have the same expansion power law. These two
solutions are explicitly found, without claiming this list exhausts all
fixed points or trajectories of the limiting system.

The proposed E0 Jacobian is

  [[0,1,0,0],
   [-6d,-3/2,0,-3d/2],
   [9d/2,0,-3/2,9d/4],
   [0,a,-2,0]].

With z=lambda(lambda+3/2), its characteristic polynomial is

  z^2+[(21+3a)/2]d z+(27/2)d^2.

The two z roots are negative: their sum is negative, their product positive,
and their discriminant is [(21+3a)^2/4-54]d^2>0. For either z<0, both
roots of lambda^2+(3/2)lambda-z have negative real part. Hence E0 is a
linear sink of the four-dimensional limiting system for every fixed a>0.
This is a local limiting-system conclusion; nonlinear finite-era attraction
requires a separately controlled comparison.

For E1 the proposed Jacobian is

  [[0,1,0,0],
   [-2d,-3/2,0,-d/2],
   [9d/2,0,-3/2,3d/4],
   [0,3a,-6,0]].

Its characteristic polynomial is

  z^2+[(13+3a)/2]d z-(9/2)d^2.

One z root is positive, so one lambda root is positive. This explicit
unstable direction is about E1 in the limiting model; it does not disprove
the full action's global future homogeneous vacuum convergence.

## Radiation-dominated limiting subspace

Restrict to vanishing dust and x, u_N=0, with a fixed finite u; the u
restoring term is negligible in this asymptotic reduction. Let
P=(ln y)_N, W=r/(H_v^2 y^2). The radial system is

  F=2(W+a/3)/(3-beta_r P^2),
  h=-(4/3)W/F-beta_r P^2,
  P_N=-(3+h)P-2a/(3 beta_r F),
  W_N=W(-4-2P).

At P=-2,W=1,F=c, the proposed Jacobian is

  [[-1,2/(1+a)],[-2,0]],

with lambda=(-1 +/- sqrt(16Omega-15))/2. These modes have negative real
part for every fixed a>0. The separate u modes in this reduced radiation
limit are a constant and exp(-N). Thus this radial sink alone does not fix
the conformal field value. That value must be propagated through the later
full coupled evolution.

## Transverse field checks at the constructed limits

At the radiation point with u=0, a small x obeys

  x_NN+5x_N+(21/4)x=0,

whose roots are -3/2 and -7/2. The first is the constructed dust-field
scaling; the second decays faster as N increases. At the dust E0 point,
a small y obeys

  y_NN+(9/2)y_N+5y=0,

with roots -2 and -5/2. These equations include the limiting connection
terms of the curved metric. Removing those terms changes both polynomials.
They refer to field amplitudes; matter/radiation density perturbations and
the chosen amplitudes still have to be treated in the full coupled system.

The next decisive checks are symbolic differentiation of the two systems,
actual full-equation convergence toward these limits, and frozen disturbed
finite-era integrations. Positive eigenvalues or failures will be retained.
No numerical result or independent check is asserted by this draft.
