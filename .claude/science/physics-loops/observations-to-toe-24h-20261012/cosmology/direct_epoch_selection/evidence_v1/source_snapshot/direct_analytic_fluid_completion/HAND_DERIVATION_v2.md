# Direct analytic dust/radiation completion — before execution

Parent derivation, 2026-10-13. All statements below are proposed exact
calculations pending independent check and implementation. This construction
changes the candidate assumptions explicitly. It is not a prediction of the
previous two-field action or a new fit to independent observations. Its aim
is to remove the fractional endpoint and neutral vacuum direction without
changing the already chosen ideal dust/radiation expansion.

## Action and parameters

Use the Einstein action [R-2K_AB(phi) partial phi^A.partial phi^B-4V]/(16piG*)
and universal matter metric A^2g, A=exp(sqrt(a)u). There are now three fields
phi=(u,x,y), with a>0, H_v>0 and nu>0. Flat FLRW, expanding branch, ideal
positive dust and separately conserved positive radiation are supplied.
Here expanding means H>0 in the Einstein frame.
Let sigma=4piG*rho_m and r=4piG*rho_r; rho here is Einstein mass-equivalent
energy density. The metric and potential are fixed functions of fields:

  D=1+(2/3)(1+a)(x^2+y^2),
  K=diag(1,4a/(9D),a/(3D)),
  V=H_v^2[3/2+f(u)x^2+(a/3)y^2+(nu/2)u^2],
  f(u)=a/2-sqrt(a)u+2u^2
      =2(u-sqrt(a)/4)^2+3a/8.

Every function is real analytic for finite real fields; K is strictly
positive. The x,y field geometry is curved, unlike the prior constant
canonical kinetic matrix. It supplies an explicit new interaction structure.
The additional radiation field and restoring coefficient nu are also new.
H_v is the supplied future energy scale, not a derived cosmological constant.
No temperature, particle species, entropy, matter abundance, primordial state
or quantum dynamics is created by this definition.

## Exact reconstruction of the supplied fluids

For any real x0,y0 and Einstein N=ln(scale factor), propose

  u=0, x=x0 exp(-3N/2), y=y0 exp(-2N),
  sigma=H_v^2 x^2, r=H_v^2 y^2,
  H=H_v sqrt(D),
  xdot=-(3/2)Hx, ydot=-2Hy.

On this trajectory A=1, so physical and Einstein clocks/scales agree.
Conservation is exactly sigmadot=-3Hsigma, rdot=-4Hr. The scalar kinetic norm
is T=K_AB phidot^A phidot^B=a(sigma+4r/3), and
V=3H_v^2/2+a sigma/2+a r/3. Thus

  3H^2=2(sigma+r)+T+2V,
  Hdot=-(1+a)(sigma+4r/3)=-(sigma+4r/3)-T.

The u equation has V_u=-sqrt(a)sigma, cancelling its matter source. Radiation
has vanishing trace and no direct u source. For the two remaining fields use
Hbar(x,y)=H_v sqrt(D), eta=a/(1+a). The proposed velocity obeys

  v_i=K_ij v^j=-eta partial_i Hbar,  i=x,y.

For its covariant derivative D_t v_i=-eta Hess(Hbar)_ij v^j. Let P=T/2;
then partial_i P=-eta Hess(Hbar)_ij v^j=D_t v_i. On the specified field
surface, P+V=(3/2)Hbar^2-H_v^2(x^2+y^2). Therefore

  partial_i(P+V)+3Hbar v_i
   =3(1-eta)Hbar partial_i Hbar-partial_i[H_v^2(x^2+y^2)]=0.

This is the full pair of covariant scalar equations, not just total energy
conservation. The metric used off trajectory remains D(x,y), never the actual
Hubble value substituted into the definition of K.

The Lagrangian has no m or radiation-amplitude coefficient. For a supplied
H0,m,Omega_gamma with m+Omega_gamma<1, choose
H_v^2=H0^2(1-m-Omega_gamma),
x0^2=3m/[2(1+a)(1-m-Omega_gamma)],
y0^2=3Omega_gamma/[2(1+a)(1-m-Omega_gamma)].
Those amplitudes are initial data set using exposed observations, not
predictions. The zero-neutrino photons-only calibration remains explicit.
The construction also accepts extra ideal radiation by altering that supplied
initial amplitude; it does not derive a neutrino abundance or mass transition.

## Homogeneous proper-time dynamics and energy

For arbitrary fields, velocities and nonnegative sigma,r use

  3H^2=2(sigma+r+V)+T, H>0,
  D_t v^A+3H v^A+K^AB(V_B+alpha_B sigma)=0,
  alpha=(sqrt(a),0,0),
  sigmadot=(-3H+sqrt(a)udot)sigma, rdot=-4Hr.

Define E=T/2+V+sigma+r=3H^2/2. Direct differentiation gives

  Edot=-3H[T+sigma+4r/3] <=0.

This identity uses the cancellation between the scalar matter force and
matter mass change. It is not valid if one omits either coupling term.
V>=3H_v^2/2+(3a/8)H_v^2 x^2+(a/3)H_v^2 y^2+(nu/2)H_v^2 u^2.
Thus each finite initial energy sublevel bounds all fields. On that compact
field set, K has a positive lower eigenvalue, so it also bounds velocities;
nonnegative densities are bounded by E. H>=H_v and H is bounded above.
The smooth autonomous proper-time equations therefore have global forward
solutions in the physical expanding state domain. The density boundaries
sigma=0 or r=0 are invariant and must be represented without log singularities
when invoking this global statement.

LaSalle's invariant-set argument on this compact positive-energy sublevel
then gives convergence to the largest invariant subset with Edot=0. There
v=0,sigma=r=0. Invariance also requires grad V=0. V_x=2H_v^2 f(u)x and
V_y=(2a/3)H_v^2 y force x=y=0; then V_u=nu H_v^2 u forces u=0. Hence the
proposed conclusion is global future convergence, within this homogeneous
expanding positive-fluid model, to (u,x,y,v,sigma,r)=0 and H=H_v.
This is not stability of general inhomogeneous spacetime, quantum vacuum
selection, or attraction to the particular finite-time dust/radiation history.
All those stronger statements need separate work.
For unrestricted a>0 the physical-frame Hubble rate
H_J=A^(-1)(H+sqrt(a)udot) can transiently be negative. The compact energy
sublevel bounds u and hence bounds A above and away from zero, so physical
proper time is also future complete. The stated convergence implies
A -> 1 and H_J -> H_v; it does not assert expansion in both frames at every
intermediate time.

## Local future modes and the remaining history problem

At the vacuum, the canonical squared masses are
H_v^2*(nu,9/4,2). The free linear modes are

  u, nu != 9/4: C1 exp{[-3+sqrt(9-4nu)]H_v t/2}
                 +C2 exp{[-3-sqrt(9-4nu)]H_v t/2},
  u, nu = 9/4: (C1+C2 t) exp(-3H_v t/2),
  x: (C1+C2 t) exp(-3H_v t/2),
  y: C3 exp(-H_v t)+C4 exp(-2H_v t).

For nu>9/4 the u roots are a conjugate decaying pair. The exact radiation
trajectory uses the faster y mode. A generic smaller absolute perturbation
can contain the slower mode and grow relative to that exact trajectory.
Likewise the critical x mode can carry a polynomial factor. A vacuum
attractor does not select the observed matter/radiation trajectory, their
abundances or their primordial perturbations. The proposed construction
repairs regularity and the vacuum flat direction while retaining that clear
initial-history limitation.

## Explicit coordinate coefficients for implementation

Write A_x=4a/9,A_y=a/3 so K_ii=A_i/D. Let d_i=partial_i D/D. The only
nonzero x,y Christoffel coefficients are

  Gamma^x_xx=-d_x/2, Gamma^x_xy=-d_y/2,
  Gamma^x_yy=(3/4)d_x/2,
  Gamma^y_yy=-d_y/2, Gamma^y_xy=-d_x/2,
  Gamma^y_xx=(4/3)d_y/2.

All u Christoffels vanish. In Einstein-N coordinates p=dphi/dN,

  H^2=2(sigma+r+V)/(3-K_AB p^A p^B),
  h=-(sigma+4r/3)/H^2-K_AB p^A p^B,
  phi'=p,
  p'^A=-(3+h)p^A-Gamma^A_BC p^B p^C
        -K^AB(V_B+alpha_B sigma)/H^2,
  sigma'=(-3+sqrt(a)p_u)sigma, r'=-4r.

A finite proper-time state determines p=v/H with positive denominator.
Numerical positive-density logs are only a chart, not the global domain.
All dimensional numerical inputs will explicitly use H0 or H_v reference
units. No canonical port or N1-N8 packet PASS is inferred from this note.
