# Independent derivation: analytic three-field fluid completion

This checks only the frozen handwritten candidate and its separately versioned
mode/frame clarification. It uses no parent implementation or empirical input.
The complete source identities are in `INPUT_FREEZE_v1.json` and
`AFFECTED_INPUT_FREEZE_v2.json`. All formulas below use c=1, the usual positive
Einstein coupling G_*, dimensionless fields, and fixed a, nu, H_v>0.

## 1. Action, exchange and units

Write A=exp(sqrt(a)u), alpha_A=partial_A ln A. V, sigma, r and the kinetic
norm T have dimensions inverse time squared. K, a, nu and the field coordinates
are dimensionless; H_v and the velocities have dimensions inverse time. The
note's logarithmic scale variable N is dimensionless. There is no implied
replacement of the fixed function D(x,y) by the evolving Hubble parameter.

Varying the scalar part of the supplied action gives

  box phi^A + Gamma^A_BC partial phi^B.partial phi^C
    = K^AB(V_B - 4piG_* alpha_B T_m).

With signature (-,+,+,+), pressureless T_m=-rho_m and radiation trace zero,
the homogeneous equation is

  D_t v^A + 3Hv^A + K^AB(V_B + alpha_B sigma)=0.

The positive source inside this equation is essential. Universal matter
coupling gives dot sigma=(-3H+sqrt(a) v_u)sigma. An independent physical way
to see that sign is to use rho_E=A^4 rho_J and a_J=A a_E: conserved Jordan
dust obeys rho_J proportional to a_J^-3, so rho_E is proportional to
A a_E^-3. Radiation instead gives rho_E proportional to a_E^-4. Hence
dot r=-4Hr even when u varies. Treating dust as separately conserved in the
Einstein frame would change this model and break the energy identity.

The flat-FLRW Einstein equations are

  3H^2 = 2(sigma+r) + T + 2V,
  dot H = -(sigma+4r/3)-T.

Multiplying the scalar equations by K_AB v^B, including the derivative of K,
gives dot(T/2)=-3HT-v.V_gradient-sqrt(a) sigma v_u. Adding dot V, dot sigma
and dot r leaves exactly

  E=T/2+V+sigma+r=3H^2/2,
  dot E=-3H(T+sigma+4r/3).

Omitting the dust mass-change term leaves an extra -sqrt(a) sigma v_u;
omitting its scalar force leaves the opposite extra term. The exact controls
detect both mutations. Positive G_* is the standard physical convention
needed for nonnegative physical densities to give nonnegative sigma and r.

## 2. Connection and full reconstructed trajectory

Let c=2(1+a)/3, D=1+c(x^2+y^2), A_x=4a/9, A_y=a/3. Direct metric
differentiation gives

  Gamma^i_jk = (1/2) K^il (partial_j K_lk + partial_k K_lj - partial_l K_jk).

There are no connections involving u. With d_i=partial_i D/D, the complete
nonzero x,y entries (and lower-index symmetries) are

  Gamma^x_xx=-d_x/2, Gamma^x_xy=-d_y/2,
  Gamma^x_yy=(A_y/A_x)d_x/2=3d_x/8,
  Gamma^y_yy=-d_y/2, Gamma^y_xy=-d_x/2,
  Gamma^y_xx=(A_x/A_y)d_y/2=2d_y/3.

All 27 entries of the three-field connection were checked, including zeros.
K is positive and real analytic at every finite real field value because
D>=1 and a>0. No claim of a uniform positive lower eigenvalue on the whole
unbounded field space is needed. A positive lower bound will be obtained on
each individual energy sublevel.

For Hbar=H_v sqrt(D), the proposed velocity is v=(0,-3Hbar x/2,-2Hbar y).
The corresponding densities are sigma=H_v^2 x^2 and r=H_v^2 y^2. Direct
substitution gives

  T=a(sigma+4r/3),
  V=3H_v^2/2+a sigma/2+a r/3,
  dot Hbar=-(1+a)(sigma+4r/3).

These satisfy both Einstein equations and both conservation laws. In the u
equation, V_u=-sqrt(a)H_v^2 x^2 cancels +sqrt(a)sigma exactly; no connection
or radiation trace term is missing.

For i=x,y, lowering the velocity index gives v_i=-eta partial_i Hbar with
eta=a/(1+a). Consequently nabla_j v_i=-eta Hess(Hbar)_ij, where Hess is the
Levi-Civita Hessian for K, not an ordinary second derivative. It is symmetric.
For P=|v|_K^2/2, metric compatibility gives

  partial_i P = v^j nabla_i v_j = v^j nabla_j v_i = D_t v_i.

The middle equality is the load-bearing gradient property. On u=0,

  P+V = (3/2)Hbar^2-H_v^2(x^2+y^2).

Thus

  D_t v_i+3Hbar v_i+V_i
    =3(1-eta)Hbar partial_i Hbar-2H_v^2 q_i=0,

because Hbar partial_i Hbar=(2/3)(1+a)H_v^2 q_i. This proves both individual
covariant field equations, beyond the total energy equation. The independent
symbolic route also directly evaluates acceleration plus Gamma(v,v). A
second exact-rational route uses the coordinate momentum equation

  K_ii dot v_i + (partial_j K_ii)v_j v_i
  - (1/2)(partial_i K_jj)v_j^2 +3H K_ii v_i +V_i+alpha_i sigma=0,

with no Christoffel construction. Its 80 fixtures include pure dust, pure
radiation, both field signs and the zero-density vacuum. It verifies all three
components exactly. Removing the metric-derivative terms is detected in all
64 nonvacuum fixtures; the sixteen vacuum fixtures necessarily have zero
velocity and therefore cannot detect that mutation.

The stated initial-amplitude algebra gives H(N=0)=H0 and the expansion
coefficients m and Omega_gamma exactly. Real amplitudes require nonnegative
m and Omega_gamma and a positive remaining fraction. Zero amplitudes are the
allowed nonnegative-fluid boundary cases; strictly positive fluids require
both amplitudes nonzero. Their observational interpretation and the
conversion between measured gravitational units and G_* are not an empirical
calibration check performed here. No fluid amplitude follows from the action.

## 3. Compact sublevels and forward completeness

The key exact decomposition is

  V=H_v^2[3/2+(3a/8)x^2+(a/3)y^2+(nu/2)u^2]
    +2H_v^2(u-sqrt(a)/4)^2 x^2.

For an initial state of finite energy E0, define Q=E0/H_v^2-3/2>=0.
On its closed nonnegative-fluid sublevel E<=E0,

  u^2 <= 2Q/nu,
  x^2 <= 8Q/(3a),
  y^2 <= 3Q/a,
  D <= Dmax = 1+34(1+a)Q/(9a).

Therefore K >= kappa I with kappa=min(1,a/(3Dmax))>0 on that sublevel.
The same energy inequality gives

  |v|^2 <= 2H_v^2 Q/kappa,
  sigma+r <= H_v^2 Q,
  H_v <= H <= sqrt(2E0/3).

All eight state coordinates (three fields, three velocities, two densities)
are consequently bounded. The sublevel is closed, so it is compact in the
finite-dimensional state space. The square-root constraint determines a
smooth positive H there. K^{-1}, its derivatives, the potential derivatives
and the resulting proper-time vector field are smooth on a neighborhood of
this compact set. The apparent vanishing of K at infinite x or y is irrelevant
because a finite-energy trajectory cannot reach that region.

The density boundaries are invariant. More explicitly, along any solution,

  sigma(t)=sigma(0) exp[-3 integral_0^t H ds
                        +sqrt(a)(u(t)-u(0))],
  r(t)=r(0) exp[-4 integral_0^t H ds].

Thus nonnegative densities cannot cross to negative values. The nonincreasing
energy makes the compact sublevel forward invariant. Standard local
continuation then excludes finite future proper-time blowup: a maximal
solution confined to a compact subset of the smooth domain extends. This
is the missing explicit step between a Lyapunov inequality and forward
completeness, and it is available for the stated candidate.

These bounds use strict a>0, nu>0 and H_v>0 at fixed parameter values. They
are not uniform statements about a->0, nu->0 or H_v->0. In particular, nu=0
would restore a vacuum u flat direction and remove the stated coercive bound.

## 4. LaSalle and frame scope

On the compact forward-invariant sublevel, dot E=0 requires v=0 and
sigma=r=0, since K>0 and H>0. An orbit confined to this zero-dissipation set
also needs grad V=0. Since

  V_x=2H_v^2 f(u)x,  f(u)>=3a/8>0,
  V_y=(2a/3)H_v^2 y,

it must have x=y=0. Then V_u=nu H_v^2 u forces u=0. The largest invariant
subset is exactly the single vacuum state. LaSalle therefore gives convergence
of every finite physical homogeneous Einstein-expanding state to that vacuum,
and H->H_v. This argument does not require V to be globally convex. Its
coercivity and unique stationary point, together with dissipation, suffice.

The conformal factor satisfies fixed sublevel bounds

  exp[-sqrt(2aQ/nu)] <= A <= exp[sqrt(2aQ/nu)].

Consequently physical proper time t_J=integral A dt also extends to infinity.
The physical Hubble parameter is H_J=(H+sqrt(a)v_u)/A. At the limiting
vacuum A->1 and v_u->0, so H_J->H_v. Einstein expansion need not imply
physical expansion at every earlier time: for a=nu=H_v=1, fields and
densities zero and v=(-3,0,0), the constraint gives H=2 while A=1 and
H_J=-1. This exact admissible counterexample is preserved in the rational
controls. The separately frozen v2 note explicitly states this distinction.

This is a homogeneous proper-time completeness result. It is not a theorem
of geodesic completeness or stability for arbitrary inhomogeneous spacetime,
nor a quantum, entropy or primordial-selection result.

## 5. Future modes and the original omission

At the vacuum K0=diag(1,4a/9,a/3). Canonical normalization therefore gives

  K0^{-1} Hess(V)_0 = H_v^2 diag(nu,9/4,2).

The connection terms are quadratic in velocity and vanish in the linearized
vacuum equations. Each free field obeys ddot z+3H_v dot z+m_z^2 z=0.
For nu not equal to 9/4 the two u exponents in the note are correct. At the
permitted value nu=9/4 the displayed v1 exponentials coincide and have zero
Wronskian, so they do not span the two initial data. The missing solution is
t exp(-3H_v t/2). The correct critical solution is
(C1+C2 t)exp(-3H_v t/2). The original failed source assertion is retained;
v2 states this critical case explicitly. Its corrected Wronskian is
exp(-3H_v t)>0. The x and y formulas in v1 are already correct.

The word “free” matters. In the full linear homogeneous system, density
perturbations satisfy delta sigma=sigma0 exp(-3H_v t),
delta r=r0 exp(-4H_v t). Dust drives u through -sqrt(a)delta sigma, with
particular solution

  u_part=-sqrt(a)delta sigma/(nu H_v^2).

This is nonresonant for every nu>0, including nu=9/4. The linear Hubble
perturbation is (delta sigma+delta r)/(3H_v). These forcing terms do not
invalidate the note's explicitly free mode list or the nonlinear convergence
proof. All field modes decay, including the critical t factor.

The selected exact y trajectory uses exp(-2H_v t). A generic additional
exp(-H_v t) mode decays absolutely but its ratio to that trajectory grows
as exp(H_v t). The critical x polynomial likewise permits relative drift.
The global vacuum attractor therefore does not select the calibrated
finite-time history, fluid amplitudes or primordial perturbations.

## 6. N-coordinate chart

Substituting v=Hp in the proper-time constraint gives

  H^2=2(sigma+r+V)/(3-K_AB p^A p^B).

For every finite physical proper-time state, the denominator equals
2(sigma+r+V)/H^2>0. On a fixed energy sublevel it is bounded below by
9H_v^2/(2E0)>0. Since dot v=H^2(p'+h p), where h=dot H/H^2, the exact
pullback is

  h=-(sigma+4r/3)/H^2-K_AB p^A p^B,
  p'^A=-(3+h)p^A-Gamma^A_BC p^B p^C
        -K^AB(V_B+alpha_B sigma)/H^2.

The supplied density equations follow by division by H. Because H>=H_v,
N also increases without an upper finite-time endpoint along a future-complete
trajectory. Log-density variables exclude the invariant zero-density boundary
and cannot by themselves support the global theorem. The note makes that
restriction correctly.
