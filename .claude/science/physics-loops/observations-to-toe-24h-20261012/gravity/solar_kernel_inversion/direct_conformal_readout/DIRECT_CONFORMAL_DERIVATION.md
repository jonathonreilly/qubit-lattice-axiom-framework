# Conformal clocks, light and matter: an explicit conditional completion

Status: conditional-support. Direct parent authorship, October 13, 2026 UTC.
This is a new candidate coupling, not a framework axiom, empirical fit, or
derivation of general relativity. The earlier scalar-force mechanics did not
specify an optical observable. Here the added metric supplies that missing
definition and makes a separate light-bending question decidable.

## Premises and source change

Keep the homogeneous preferred-coordinate vector action

    L_field = [alpha |u_t|^2 - mu |grad u|^2 - beta(div u)^2]/(8 pi G),
    phi = e.u,  |e|=1,  mu=1/N, beta=1/D-1/N,
    alpha,G>0, 0<D<=N.

Supply the physical matter metric g~=A^2 eta, A=exp(phi/c^2), with
eta=diag(-1,1,1,1), x^0=ct, and c the electromagnetic limiting speed.
The field action remains a preferred-coordinate action; this prescription
does not make it generally covariant. Supply structureless massive particles
with L_a=-m_a c^2 A(x_a) sqrt(1-v_a^2/c^2), and four-dimensional minimally
coupled vacuum Maxwell electromagnetism. No cosmological boundary condition,
composite-body screening, cavity optics or material suspension is supplied.

For gamma_v=(1-v^2/c^2)^(-1/2), direct variation and the Legendre transform give

    p_a = m_a A gamma_v v_a,
    H_a = m_a c^2 A gamma_v
        = sqrt(c^2 |p_a|^2 + m_a^2 c^4 A^2),
    -partial L_a/partial phi = m_a A/gamma_v.

Consequently the field equation becomes

    alpha u_tt - mu Delta u - beta grad div u = -4 pi G e rho_A,
    rho_A(x,t) = sum_a (m_a A(x_a)/gamma_va) delta^3(x-x_a).

This source is not exactly conserved rest-mass density. The old arbitrary
mass-conserved quadrupole calculation cannot be inherited to all orders.
Expansion for |phi|/c^2<<1 and |v|/c<<1 gives
L_a=-m_a c^2 + m_a v_a^2/2 - m_a phi + higher orders: the earlier reciprocal
Newtonian coupling is recovered only at this order. Even small corrections
to a source can contribute at the leading radiative order of a noncircular
system; no pulsar prediction is carried over here without recalculation.

For configurations on which the indicated energy and boundary terms are
finite, the time-translation Hamiltonian is

    H_total = E_field + sum_a sqrt(c^2 p_a^2+m_a^2 c^4 exp(2 phi_a/c^2)),
    E_field = integral [alpha |u_t|^2+mu |grad u|^2+beta(div u)^2]/(8 pi G).

It is nonnegative. Along a particle trajectory,
dH_a/dt=(m_a A/gamma_va) partial_t phi(x_a,t). This cancels the field work
-integral rho_A partial_t phi. Thus H_total is conserved for a closed system
with vanishing boundary flux, or obeys the corresponding flux balance.
This is an algebraic conditional improvement over the unbounded linearized
interaction Hamiltonian; it does not establish global existence, coercivity,
stability, or finite self-energy of point sources. Literal point particles
generically make field self-energy singular. Smooth source regularization or
an extended-body action needs its own definition. Free Maxwell energy can
be added and is positive in these coordinates, by the cancellation below.

## Light and local curvature

In four dimensions sqrt(-g~)=A^4 and g~^(mu nu)=A^-2 eta^(mu nu), so the
Maxwell action density sqrt(-g~) g~^(mu alpha)g~^(nu beta)F_mu nu F_alpha beta
is exactly its flat-coordinate value. A clock measures
d tau=A sqrt(1-v^2/c^2) dt. Light paths obey |dx/dt|=c. More explicitly,

    Gamma^mu_ab = delta^mu_a psi_,b + delta^mu_b psi_,a
                 - eta_ab eta^(mu nu) psi_,nu,   psi=phi/c^2.

For a null tangent k, Gamma^mu_ab k^a k^b=2 k^mu(k.grad psi), parallel to k.
It changes affine parametrization but not the unparameterized null curve.
Thus this metric alone cannot deflect an asymptotically straight light ray,
even for an inhomogeneous static phi. This holds for the conformal ansatz;
it is not a no-go for other metric completions of the vector field.

At first order h_00=-2psi, h_ij=2psi delta_ij, h_0i=0. With the curvature
convention for which relative geodesic acceleration is -c^2 R_0i0j X_j,

    R_0i0j = partial_i partial_j psi - delta_ij psi_tt/c^2,
    T_ij = delta_ij psi_tt - c^2 partial_i partial_j psi.

For psi=f(t-n.x/c_s), |n|=1, define gamma_s=c/c_s. Then

    T = (I-gamma_s^2 n n^T) f''.

The transverse block is proportional to the transverse identity and has no
trace-free part. At c_s=c the longitudinal eigenvalue vanishes: this is a
breathing tide. At c_s!=c the transverse coefficient 1 and longitudinal
coefficient 1-gamma_s^2 are linked, not independently selectable. A sum of
the two same-direction candidate modes keeps zero transverse trace-free
projection. This physical tide includes the metric contribution absent
from the earlier simultaneous Euclidean endpoint displacement.

## Optical round trip at all arm frequencies, first order in amplitude

Assume freely moving beam splitter and ideal reflecting endpoint, an equal
unperturbed arm length L, negligible photon backreaction and harmonic
particular endpoint trajectories. A returned pulse defines the elapsed
proper time on the beam splitter clock. This timing observable avoids any
assumption about an actual interferometer's cavity and electronics.

For complex psi=Psi exp(-i omega t+i omega n.x/c_s), omega>0, the first-order
coordinate equation is xi_tt=-c^2 grad psi and its particular solution is

    xi = i n c^2 psi/(omega c_s).

Zero-position/velocity initial conditions add homogeneous displacement and
velocity terms; those transients are not part of this frequency response.
Let a be the unit arm direction, mu_a=n.a, base position x and mirror
position x+La. To first order, transverse endpoint displacements do not
change the ray's Euclidean path length. At fixed return coordinate time t,
the sum of outgoing and incoming null-flight equations gives

    delta T_a = a.[2 xi_m(t-L/c)-xi_b(t)-xi_b(t-2L/c)]/c.

The splitter's elapsed proper time includes its conformal clock rate:

    delta tau_a = delta T_a + integral_(t-2L/c)^t psi_b(t') dt'.

Velocity time dilation is second order. Set x_f=omega L/c and use
sinc(x)=sin(x)/x. Normalizing by the unperturbed round-trip time,

    c delta tau_a/(2L) = H_a psi_b(t),
    H_a = exp(i x_f) sinc(x_f)
        + i gamma_s mu_a/(2 x_f)
          [2 exp(i x_f(1+gamma_s mu_a))-1-exp(2i x_f)].

This expression is linear in field amplitude, not a finite-amplitude exact
geodesic solution. It is otherwise unrestricted in omega L/c. For equal
arms a,b, the difference H_a-H_b cancels the common clock term. Limiting
relations are

    H_a -> 1-gamma_s^2 mu_a^2                 as x_f->0,
    H_a = exp(i x_f)sinc(x_f)                if mu_a=0,
    H_a = 0                                 if gamma_s=1, mu_a=+/-1,
    H_a-H_b -> -gamma_s^2 (mu_a^2-mu_b^2).

The small-arm relation is the twice-integrated local curvature tide with
the same particular-motion convention. In the luminal parallel/perpendicular
pair the difference is -exp(i x_f)sinc(x_f). The earlier simultaneous
mechanical arm difference is -exp(i x_f/2)sinc(x_f/2); it is not the optical
response at finite frequency. For example the optical response vanishes at
x_f=pi, while that mechanical response does not.

The two candidate speeds require superposing two copies of this response
with their own phases and waveforms. A pure-polarization GR-template Bayes
factor cannot be assigned to that signal without a new source and likelihood.

## Verification and observation boundary

The paired runner derives the particle source/Legendre identities and linear
curvature symbolically. It independently solves both geometric null-flight
root equations in three dimensions and integrates the splitter's full
proper-clock functional along first-order particular trajectories. The
comparison uses a frozen grid of amplitudes, directions, speeds and arm
frequencies. Those trajectories have O(psi^2) dynamical error, so the
comparison verifies the first-order response, not a nonlinear solution.
All failures and coefficient/scaling controls must remain visible.

Observed solar radio-wave bending motivates a decisive limitation of this
completion. Fomalont et al., arXiv:0904.3992, estimate a near-unit PPN gamma
from a multi-frequency VLBA analysis. Their published parameter fit is not
a likelihood for this candidate and its uncertainty is not transferred.
The exact straight-null-path result nevertheless leaves this completion
without the observed gravitational light-bending mechanism. A nonconformal
spatial/temporal metric relation or another optical mechanism is required.
The next constructive task is to derive such an extension and test its
linked consequences, rather than hiding the failed conformal bridge.

No parameters were fitted and no observation was held out for this block.
All empirical inputs are exposed model-development constraints. No full
TOE, Einstein dynamics, tensor wave response, or data exclusion is claimed.
