# Parent direct thermal–matter history bridge — handwritten v1

Written before implementation or history inspection. This block tests whether
the earlier radiation-only thermal history and exact late dust history can
actually belong to one evolution of the same action. It does not join their
solutions by hand. The constants, auxiliary sector and initial scalar state
remain fixed throughout. Parent /root authors the reconstruction.

## 1. Observational inputs and additional premises

Retain the prescribed curvature/fluid action, nu=1, eta-zero a,s family and
primary b=k calibration; b=a is a separate diagnostic. Supply the previously
exposed H0=70 km/s/Mpc, pressureless-component density fraction Omega_d0=.3,
and photon temperature T0=2.72548 K. These set a reference normalization;
ending an evolution at T0 does not predict T0 or guarantee that actual H or
G equals its input reference. Omega_d0 labels the conserved dust component,
excluding the separately evolved neutrinos. It is not a newly fitted total
matter-density measurement.

Measured/exact electron mass, G_N, h, c and k_B use the preserved NIST table.
Three neutrino mass eigenstates each have two populated helicity/antiparticle
states and a decoupled zero-chemical-potential momentum distribution. A normal
ordering benchmark with lightest mass zero and two imported mass-squared
differences supplies the absolute masses. The ordering, zero lightest mass,
initial distribution and instantaneous decoupling are explicit assumptions;
oscillations do not measure that absolute mass choice. The precise versioned
source and numerical choices must be frozen before execution. A zero-neutrino-
mass comparison is an explicitly different matter assumption.

There is no baryon chemistry, recombination opacity, nuclear network, neutrino
collision term, primordial perturbation calculation or abundance/CMB fit here.
The pressureless component remains phenomenological; its particle identity and
mass generation are not derived. This is a background-history consistency test.

## 2. Jordan fluids and a physical temperature clock

Use m_e=hbar=c=k_B=1 for the dimensionless integrals. Photons and equilibrium
electron pairs share T, with the same independently checked FD gas as before.
Let rho_pl(T), P_pl(T), s_pl=(rho_pl+P_pl)/T, Sbar=s_pl/T^3, and
c_T=3(rho_pl+P_pl)/(T d rho_pl/dT). Only this plasma heats the photons.

Set Ti=10 and initially Tnu=Ti. With L=ln(Ti/T), conservation gives

    N_J(L)=L-(1/3)ln[Sbar(T)/Sbar(Ti)],
    Tnu=Ti exp(-N_J),       dN_J/dL=1/c_T.

For mass eigenvalue mu_i=m_nu_i/m_e, decoupled occupations depend on momentum,
not on the late particle energy:

    rho_nu_i = Tnu^4/pi^2 integral_0^infty dq q^2 sqrt(q^2+r_i^2)/(exp(q)+1),
    P_nu_i = Tnu^4/(3pi^2) integral dq q^4/[sqrt(q^2+r_i^2)(exp(q)+1)],
    tau_nu_i = Tnu^4 r_i^2/pi^2 integral dq q^2/[sqrt(q^2+r_i^2)(exp(q)+1)],
    r_i=mu_i/Tnu.

Thus tau_nu_i=rho_nu_i-3P_nu_i >=0 and
Tnu d rho_nu_i/dTnu=3(rho_nu_i+P_nu_i). The trace must enter the scalar source
when neutrinos become nonrelativistic. Replacing exp(q) by exp(sqrt(q²+r²))
would instead describe a replenished massive equilibrium gas and is wrong for
these frozen occupations. With mu_i=0 each state contributes 7pi²Tnu^4/120.

The separately conserved dust is rho_d=rho_di exp(-3N_J). Define total Jordan
rho=rho_d+rho_pl+sum rho_nu_i, P=P_pl+sum P_nu_i, tau=rho-3P.
All these densities are in the same m_e^4 energy-density unit.

## 3. SI normalization fixed before integrating

Let E_e=m_e c² and rho_unit=E_e^4/(hbar c)^3 in J/m³. The observed photon
temperature gives dimensionless Tf=k_B T0/E_e. The entropy formula fixes
Ntotal=N_J(Tf), independently of the scalar clock. Compute the supplied present
fluid values rho_pl(Tf), rho_nu(Tnu_f) before choosing the action constants.

    rho_crit0 = 3 c² H0²/(8pi G_N0),
    rho_d0 = Omega_d0 rho_crit0,
    rho_v0 = rho_crit0 - rho_d0 - rho_unit[rho_pl(Tf)+sum rho_nu_i(Tnu_f)],
    H_v² = 8pi G_N0 rho_v0/(3c²),
    Rstar = 3 rho_unit/[2(1+k)rho_v0],
    rho_di/rho_unit = (rho_d0/rho_unit) exp(3Ntotal).

The positive reference-vacuum branch rho_v0>0 is required. This uses the
conditional local bridge G_N0=(1+k)/[8pi(q+zeta)] in natural units. Its SI
equivalent gives exactly the displayed Rstar. It is a calibration of H_v and
q+zeta; neither scale is explained. All gas and dust expressions below use
dimensionless rho/rho_unit. The GR comparison has the identical supplied
Jordan fluids and constant input G_N0:

    H_GR²/H_v² = 1 + 2(1+k)Rstar rho/3.

At Tf this reference equals H0²/H_v² by construction. The actual theory may
differ. The late diagnostic G_N ratio uses the same previously qualified
weak-body/light-scalar/local-background bridge; no apparatus test is supplied.

## 4. Full fixed-action dynamics, including both tracking fields

In Einstein Hhat_v=H_v/sqrt(1+s) units, use the already checked finite-field
K(u,x,y), its full coordinate derivatives, U and U_i. Let phi=(u,x,y),
p^i=dphi^i/dNhat, B=exp(sqrt(a)u)/sqrt(F), C_B=(1+s)B², alpha_B=sqrt(a)/F.

    sigma=C_B² Rstar rho,       pi_f=C_B² Rstar P,
    Qkin=K_ij p^i p^j,
    H²=2(sigma+U)/(3-Qkin),
    h=H'/H=-(sigma+pi_f)/H²-Qkin,
    p'^i=-(3+h)p^i-Gamma^i_jl p^j p^l
          -K^ij[U_j+delta_ju alpha_B(sigma-3pi_f)]/H²,
    N_J'=1+alpha_B p_u,       dNhat/dL=1/[c_T N_J'].

The Einstein energy exchange is
sigma'=-3(sigma+pi_f)+alpha_B p_u(sigma-3pi_f). It cancels scalar trace work.
The physical positive-clock/Friedmann branch requires N_J'>0, H²>0 and
3-Qkin>0; failures must be recorded, not regularized into a chosen solution.

Both tracking fields are dynamical. Their initially small dust/radiation ratio
does not justify removing x from the u equation: the prescribed u²x²/b
coefficient and small transverse kinetic coefficient may amplify its effect.
In particular, the earlier x=0 thermal trajectory is not evidence for the
actual evolution of a universe containing conserved dust.

For numerical range use prescribed time-dependent positive scales

    sx=x_i exp(-3N_J/2),        sy=y_i exp(-2N_J),
    X=x/sx, Y=y/sy, vx=p_x/sx, vy=p_y/sy.

The six variables are (u,X,Y,p_u,vx,vy). Neither X nor Y is restricted positive;
this chart permits field zero crossings without a logarithmic singularity.
Before changing to L, their Nhat derivatives are

    u'=p_u,
    X'=vx+(3/2)N_J' X,       Y'=vy+2N_J' Y,
    p_u'=acc_u,
    vx'=acc_x/sx+(3/2)N_J' vx,
    vy'=acc_y/sy+2N_J' vy.

Divide the whole six-component vector by c_T N_J' for temperature evolution.
Here acc is the original full coordinate acceleration above, evaluated before
rescaling. This change of variables adds no field potential or matter force.

## 5. Supplied initial state, readouts and planned tests

At Ti set u=p_u=0, x_i²=Rstar rho_di, and
y_i²=Rstar[rho_pl(Ti)+sum rho_nu_i(Ti)], with X=Y=1, vx=-3/2, vy=-2.
This matches the chosen ideal-fluid orbit algebraically in its energy at the
initial instant, not its evolution when the gas has a trace. The finite
electron and neutrino traces are retained from that instant onward.
For an x=0 diagnostic use x=p_x=0 and a harmless fixed sx=1; label its missing
dust component rather than interpreting it as the same initial universe.

    H_J²/H_v² = H²(N_J')²/C_B,
    G_N/G_N0 = C_B(1+a/J)/(1+k),
    Nhat=N_J-ln(B/B_i).

Elapsed physical age since Ti is the positive integral

    H_v Delta t_J = integral dL sqrt(C_B)/[H c_T N_J'].

A numerical quadrature over a computed trajectory is not an independent ODE
solution or a prediction of the pre-Ti age.

Freeze full histories, selected tighter repeats and changed matter/initial
conditions before their output. Check dimensional normalization, decoupled
neutrino identities, entropy-clock derivatives, the full scalar-coordinate
transformation, generic off-trajectory energy conservation, exact massless
dust/radiation orbit controls and physical-clock readouts. Retain all fields,
fluid components, constraints, kinetic/clock margins and sample extrema.
Report whether thermal/neutrino trace evolution actually approaches the late
u=0 family; do not retune b, H_v, initial field amplitudes or G_N after seeing
the result. Observation-calibrated inputs remain separate from any later
independent empirical comparison.
