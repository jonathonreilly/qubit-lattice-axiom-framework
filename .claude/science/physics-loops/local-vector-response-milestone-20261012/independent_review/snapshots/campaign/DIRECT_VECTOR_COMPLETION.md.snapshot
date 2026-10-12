# A local positive-energy vector realization of the homogeneous static response

Status: conditional-support. Direct parent derivation, October12,2026.
This is a constructive escape from the earlier two-field kinetic restriction.
It matches a homogeneous linear static response, not the nonlinear field
operator used in the galaxy fits. Three vector components and a supplied
background direction are new candidate assumptions.

## Action, energy and propagation

Let e be a constant unit vector, 0<D<=N and alpha>0. Set mu=1/N and
beta=1/D-1/N>=0, and take three real fields u_i with Lagrangian density

    L = [alpha |u_t|² - mu sum_ij (partial_i u_j)²
         - beta (div u)²]/(8 pi G) - rho phi,
    phi=e.u,       physical scalar force=-grad phi.

This is the ordinary constant-coefficient vector-elasticity operator used
as an explicit mathematical realization. It does not identify space or
matter with a physical elastic substance. alpha, e, N and D are supplied;
there is no rotationally invariant dynamical equation for e in this packet.
The field has three canonical momenta and no auxiliary constraint:
pi_i=alpha u_t,i/(4 pi G). Variation gives

    alpha u_tt - mu Delta u - beta grad(div u) = -4 pi G rho e.

The source sign gives an attractive scalar potential in the isotropic static
limit. The positive field energy is

    E_field = (8 pi G)^-1 integral [alpha |u_t|²
                    + mu |grad u|² + beta (div u)²] dx.

It is conserved for source-free decaying data. With a supplied rho,
the local work term is -rho phi_t. Positivity of this field part does not
bound total matter-plus-interaction energy or supply a matter model.

The Fourier stiffness is B(k)=mu k² I+beta k k^T. Its two transverse
eigenvalues are mu k² and its longitudinal eigenvalue is (mu+beta)k².
There are three stable configuration modes, with positive kinetic energy:

    c_T²=mu/alpha=1/(alpha N),
    c_L²=(mu+beta)/alpha=1/(alpha D),       c_L>=c_T>0.

The local energy proves a domain of dependence with outer speed c_L. To see
the required flux estimate directly, put Q=mu|grad u|²+beta(div u)² and
T_n=mu partial_n u+beta n div u. For any test vector v, Cauchy-Schwarz in
the positive quadratic form gives

    |v.T_n|² <= [mu |v|²+beta(v.n)²] Q <= (mu+beta)|v|² Q.

The energy flux magnitude normal to n is |u_t.T_n|/(4 pi G), bounded by
c_L[alpha|u_t|²+Q]/(8 pi G). Integrating over a shrinking cone gives zero
energy outside the c_L domain of compact full-field data and compact sources.
Smooth compact data suffice; finite-energy weak limits retain the support
statement. A derivative of the local observable phi=e.u also remains local,
so its physical force has no instantaneous off-cone tail in this construction.
No assertion about compact phi alone with unspecified other initial fields
is needed. This distinction matters to comparison with the old constraint.

## Exact static linear response

For k!=0, let P_L=k k^T/k² and P_T=I-P_L. Then

    B^-1 = N P_T/k² + D P_L/k²,
    e.B^-1.e = [N k_perp² + D k_parallel²]/k^4.

Thus a static density has

    phi_hat = -4 pi G rho_hat [N k_perp²+D k_parallel²]/k^4.

This equals the homogeneous linear response of the earlier two-potential
static equations: Delta psi=4 pi G rho and Delta phi=div(M grad psi),
where M=N I+(D-N)e e^T. It includes the same anisotropy at every nonzero k,
not just along the distinguished axes.

The real-space scalar Green function is

    e.B^-1(x).e = [N+D+(N-D)(e.xhat)²]/(8 pi r),
    phi_point(x) = -G m [N+D+(N-D)(e.xhat)²]/(2r).

The Fourier identity follows also from F^-1(1/k²)=1/(4 pi r) and
F^-1(1/k^4)=-r/(8 pi), with the decaying anisotropic inverse specified.
It is a fundamental-solution statement; distributions at the origin are
handled by the Fourier definition. In the isotropic case D=N it reduces to
phi=-Gm N/r as required.

## Retarded response and the cancellation outside the wavefront

For a unit vector force source in the equation alpha u_tt+B u=f, the
retarded tensor in Fourier space is

    G_hat(k,t)=H(t)/alpha [P_T sin(c_T k t)/(c_T k)
                         +P_L sin(c_L k t)/(c_L k)].

Consequently the observable driven along e has two nonnegative spectral
weights, sin²(theta) and cos²(theta), where theta is the angle between e and
k. Equivalently its frequency response has denominators
mu k²-alpha(omega+i0)² and (mu+beta)k²-alpha(omega+i0)². At zero frequency
their sum is exactly the previous static susceptibility. At finite frequency
it is generally different from the old constrained scalar's single branch
omega²=k^4/(alpha [N k_perp²+D k_parallel²]). Both branches share the old
axis speeds, but not its intermediate-angle dispersion.

For r>0, n=x/r, the full retarded tensor is

    G_ij(x,t) = 1/(4 pi alpha) {
        (delta_ij-n_i n_j) delta(t-r/c_T)/(c_T² r)
        + n_i n_j delta(t-r/c_L)/(c_L² r)
        + (3 n_i n_j-delta_ij) t/r³
                    [H(t-r/c_L)-H(t-r/c_T)] }.

The last term lies between the two wavefronts and is necessary. Omitting
it gives the wrong Fourier/static response. Although P_L and P_T separately
are nonlocal spatial projections, their retarded combination vanishes for
t<r/c_L; the real tensor makes the cancellation explicit. For t<0 it is
zero as well. The source response is u=-4 pi G G_ret*(rho e).

One derivation writes G=alpha^-1[I g_T+partial_i partial_j h], where
g_c=delta(t-r/c)/(4 pi c² r) and Delta h=g_L-g_T. For fixed t>0 the
two shells each integrate to t. Thus h'=0 beyond the outer shell, and
h'=-t/(4 pi r²) between the shells. Radial differentiation gives the two
surface terms and the displayed intervening term, with no outer support.

The time integral recovers B^-1(x). After contraction with e, integration of
the intervening term gives
(3cos²(theta)-1)(1/c_T²-1/c_L²)/(8 pi alpha r), which combines with the
two shell integrals to give [N+D+(N-D)cos²(theta)]/(8 pi r).
This is a direct causal-to-static bridge, not inference from a group velocity.

## What changed and what remains unbuilt

The old two-scalar classification fixed the spatial action and allowed only
a constant two-field time Hessian. This construction replaces that action
with three propagating local components and couples the source to e.u.
It is outside that proved restriction. It provides a constructive example
of why the old result did not exclude all causal realizations of the static
linear susceptibility.

For N=D, beta=0 and c_L=c_T: the intervening term cancels, all three fields
obey the same wave equation and only the e component is sourced/read out.
As D approaches zero with N and alpha fixed, c_L diverges. There is no
uniform finite-speed or uniformly bounded-coefficient D=0 limit. The new
nine-source D optima touch zero and are not covered by this strict D>0 model.

The original two frozen response vectors have D>0 at all ramp limits. They
can supply illustrative homogeneous coefficients if alpha=c_s^-2 is chosen;
this does not reconstruct a nonlinear vector law. Choosing e parallel to a
background gravitational field, choosing N,D as functions of its magnitude,
or eliminating a dynamical e changes the variational equations and introduces
new terms. None is silently performed here. There is no proof that the
nonlinear static QUMOND equation, its galaxy fits, or its solar calibration
follows from this action. The earlier empirical failures remain failures.

The observational target is now sharper: any such completion must account
for extra propagating modes and its background direction while recovering
the source-dependent static response. No mode is identified with measured
tensor radiation or light, and c_s is not calibrated. A nonlinear source and
matter/metric coupling, background formation, lensing, cosmology and quantum
interaction completion remain open. This packet is conditional constructive
mathematics, not a TOE or an empirical detection.
