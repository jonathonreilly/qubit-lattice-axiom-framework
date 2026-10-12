# A minimal matter coupling makes the linear response radiatively testable

Direct parent derivation, October 12, 2026. Conditional candidate extension;
no empirical fit or relativistic gravitational theory is claimed.

## Premises and energy exchange

Take the already checked constant vector action with G>0, alpha>0,
0<D<=N, constant unit e, mu=1/N, beta=1/D-1/N and phi=e.u. Add matter
with positive inertial masses, L_m=sum m v²/2, and coupling -integral rho phi.
Smooth finite mass profiles are assumed when discussing self energy; point
centres describe exterior multipoles only. This is a new nonrelativistic
matter assumption, not something established by the static susceptibility.

Matter then obeys m a=-m grad phi. With J the mass current and
rho_t+div J=0, integration by parts gives

    dE_field/dt = -integral rho phi_t,
    dT/dt = -integral J.grad phi,
    d(integral rho phi)/dt = integral rho phi_t + integral J.grad phi.

Thus field + kinetic + interaction energy is conserved for an isolated
regularized system. The positive field energy alone does not bound the full
Hamiltonian below. In the static limit E_field=-integral rho phi/2;
eliminating the field gives the usual half-counted interaction energy.

## Conservative equatorial orbit and a vertical test

The pair potential is

    U(R) = -G m1 m2 [N+D+(N-D)(e.Rhat)²]/(2R).

It is even in R and translation invariant. Its force need not be central;
the fixed e supplies an external orientation, so full rotational invariance
is not asserted. In the plane perpendicular to e the force is central and

    G_eq = G(N+D)/2,
    Omega² = G_eq (m1+m2)/a³,
    E_orbit = -G_eq m1 m2/(2a).

For relative vertical displacement z at fixed cylindrical radius a,

    U(a,z) = -G m1 m2 (N+D)/(2a)
              +G m1 m2 (3D-N)z²/(4a³)+O(z^4).

Therefore the leading vertical frequency is

    nu_z² = G(m1+m2)(3D-N)/(2a³),
    nu_z²/Omega² = (3D-N)/(N+D).

An equatorial circular orbit is vertically restoring for N<3D, marginal
at N=3D at this order, and linearly unstable for N>3D. This is a statement
about this fixed-direction matter model, not all gravity completions.

## Leading radiation from the independently fixed source

Let I_ij=integral rho x_i x_j and d_i=integral rho x_i. Work with a compact
slow source, a Omega/min(c_T,c_L)<<1, weak damping and a wave zone much
larger than both wavelengths. Total source mass is conserved. The leading
conservative centre of mass is at rest, so d_i is constant at that order.
Equal-mass antipodal circular sources give an exact zero dipole by symmetry.
We do not assert exact constancy of the matter centre alone at all orders
when momentum can reside in the field.

At a nonzero fixed Fourier frequency the full Green tensor's two front
terms are O(1/r). Its intervening term is O(1/r²): its time integral has
endpoints proportional to r, divided by r³, and integration by parts costs
one nonzero frequency. The DC field is different and must retain that
intervening contribution; discarding it in a static calculation is wrong.
The radiative pieces for direction n are consequently

    u_s = -G/(2 alpha r c_s^4) P_s(n)e n_i n_j I''_ij(t-r/c_s),
    s = T,L;  c_T²=1/(alpha N), c_L²=1/(alpha D).

This follows by Taylor-expanding the retarded density integral:
integral rho(x,t-r/c+n.x/c)dx = M+n.d'/c+n_i n_j I''_ij/(2c²)+...
Its first two terms have no leading radiative time derivative under the
stated conservation assumptions. The trace of I must not be removed
without cause; its derivative vanishes for the circular example below.

The radial energy flux is

    S.n = alpha/(4 pi G) [c_T |u_t,T|²+c_L |u_t,L|²]+o(r^-2).

The two projectors are orthogonal even at different retarded times. The
leading positive, time-averaged power per solid angle is

    dP/dOmega = G/(16 pi alpha) {
      [1-(e.n)²] <(n_i n_j I'''_ij)²>/c_T^7
          +(e.n)² <(n_i n_j I'''_ij)²>/c_L^7 }.

Periodic averaging makes the separate retarded origins immaterial. This
is a leading multipole result, not the exact power at arbitrary speed or
an assumption that these fields are the observed tensor waves.

## Circular source and a fixed comparison

For separation a, reduced mass m_red and an orbit in the xy plane with e=z,

    <(n_i n_j I'''_ij)²> = 8 m_red² a^4 Omega^6 sin^4(theta).

The two exact angular integrals are
integral sin^6(theta)dOmega=64 pi/35 and
integral cos²(theta)sin^4(theta)dOmega=32 pi/105. Therefore

    P_vec = G m_red² a^4 Omega^6/alpha
                [32/(35 c_T^7)+16/(105 c_L^7)].

In this adiabatic circular approximation, P_orb dot/P_orb=-3P_vec/(2|E_orbit|).
This energy-balance relation uses the explicitly supplied matter/clock
model; a pulsar arrival-time prediction requires much more.

For a comparison only, supply the usual leading GR circular quadrupole
formula for the same trajectory, inertial masses and equatorial static
calibration: P_GR=(32/5)G_eq m_red² a^4 Omega^6/c_EM^5. This formula is
not used to derive P_vec. Put q=N/D>=1; then

    P_vec/P_GR = (c_EM/c_L)^5 (6q^(7/2)+1)/(21(q+1)).

If the extra calibration c_L=c_EM is made, the isotropic q=1 result is1/6.
Equality with the GR comparator requires 6q^(7/2)+1=21(q+1), with a
unique q>1: its ratio has positive derivative for q>=1. The runner brackets
the root using the exact polynomial 6x^7-21x²-20 with x=sqrt(q). Matching
this one comparator consumes a calibration; it is not a successful test.
It also fixes unequal wave speeds, a polar/equatorial static-potential
ratio 2q/(q+1), and vertical-frequency ratio (3-q)/(1+q).

## Observational boundary

Binary-pulsar timing motivates radiation as an independent constraint on a
static reconstruction. The 2016 primary analysis of PSR B1913+16 reports
an orbital-decay comparison close to its GR prediction, but the masses,
timing delays and Galactic correction are part of that interpretation.
See the source ledger. No published mass or corrected ratio is fitted or
tested here; that binary is eccentric and strongly self-gravitating, while
this calculation uses a weak circular example. No sigma exclusion follows.

The model still lacks relativistic matter, clock and light propagation,
strong-body sensitivities, a dynamical background direction, nonlinear
response, lensing and a tensor-radiation identification. Those are explicit
targets. The useful gain is a linked set of conservative and radiative
predictions from one new matter coupling, rather than separate fitted laws.
