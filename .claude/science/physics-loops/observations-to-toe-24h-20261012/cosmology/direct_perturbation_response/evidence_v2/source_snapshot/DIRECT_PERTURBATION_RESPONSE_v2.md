# What the reconstructed background predicts for matter and light

Direct parent derivation. Claim type: bounded_theorem. Actual surface status:
conditional-support. The two-field potential, m=.3 expansion, constant local
coupling and ideal weak dust are supplied as in direct_potential_reconstruction.
This note studies the existing candidate; it does not infer a unique potential
or quantum theory from an expansion curve.

## Linear equations with the density variable specified

Use Einstein proper time t, scale factor R, Fourier factor exp(i k.x), and

    ds_*^2=-(1+2P)dt^2+R^2(1-2P)dx^2.

Dust and homogeneous canonical scalars have no linear traceless spatial
stress, so the two Einstein scalar potentials agree. Set alpha=(sqrt(a),0),
v=dot phi=(0,dot chi), sigma=4pi G_*rho_*, and K=k/R>0. On the exact
background u=0, A=1, sigma=S, alpha.v=0. Define d as the contrast in Einstein
proper particle number, not Einstein rest-mass density. If f=delta phi and
zeta=alpha.f, then

    delta_*=d+zeta,     delta_J=d-3zeta,
    Psi_J=P+zeta,       Phi_J=P-zeta.                (1)

The first identity follows from rho_*=m A n_*; the second from n_J=A^-3 n_*.
Let Theta be the physical divergence of peculiar velocity. Number conservation
and the linear particle equation give

    dot d=-Theta+3dot P,
    dot Theta+2H Theta=K^2(P+zeta).                 (2)

The background mass-drift friction vanishes since alpha.v=0. Equivalently,
dot delta_J=-Theta+3dot Phi_J, with acceleration sourced by Psi_J.
This explicitly recovers physical-frame dust conservation.

Write g=grad V+alpha sigma and M=Hess V+sigma alpha alpha^T. Linearizing the
covariant scalar equation, including its lapse perturbation, gives

    ddot f+3H dot f+(K^2 I+M)f
        =4v dot P-2g P-alpha sigma d.              (3)

The added sigma alpha alpha^T follows from the perturbed rest mass at fixed
number; it is not an arbitrary choice of a mass matrix. The term -2gP includes
the perturbed lapse multiplying both the potential gradient and matter source.
In particular its u component vanishes on the exact background. Dropping the
matter part there would leave a spurious source.

The Einstein momentum and energy constraints respectively are

    dot P+H P=sigma Theta/K^2+v.f,                 (4)
    K^2 P+3H(dot P+HP)
        =-[sigma(d+zeta)+v.dot f-v^2P+grad V.f].  (5)

The cancellation sigma zeta+grad V.f=g.f is useful. These equations follow
with scalar energy density (v^2+2V)/(8pi G_*); no factor of two is absorbed
into a redefined field. They include scalar momentum and density responses,
unlike the earlier frozen local quadratic diagnostic.

## A closed system and its constraint propagation

Let N=ln R, h=dln H/dN, D=sigma/H^2, x=dot chi/H and Q=K^2/H^2. Primes in
this section denote N derivatives. Define w=f' and T=Theta/H. Along the
constructed background,

    h=-(1+a)D,  x=sqrt(aD),
    D'=(-3-2h)D, x'=(-3/2-h)x, Q'=-2(1+h)Q,
    g/H^2=(0,-3x/2),
    M/H^2=[[ (1+eta+a)D, 3sqrt(D) ],
            [ 3sqrt(D), 9/4+(3/2)(1+a)D ]].       (6)

The seven real first-order variables are (P,d,T,f_u,f_chi,w_u,w_chi):

    P'=-P+D T/Q+x f_chi,
    d'=-T+3P',
    T'=-(2+h)T+Q(P+sqrt(a)f_u),
    f'=w,
    w'=-(3+h)w-(Q I+M/H^2)f
        +4(0,x)P'-2(g/H^2)P-D alpha d.             (7)

The dimensionless energy constraint is

    C=(Q-x^2)P+D d+3D T/Q+x w_chi+(3/2)x f_chi=0. (8)

Differentiation using(6)-(7) gives the exact identity

    C'=(-3-2h)C.                                  (9)

Thus initially consistent data stay on the constraint surface; unscaled
H^2 C decays as R^-3 even for an off-constraint numerical control. This is a
useful algebraic cross-check of the coupled evolution. It does not test every
u-sector coefficient: C contains neither f_u nor w_u, so changing the u
acceleration leaves this identity unchanged. The direct covariant scalar
variation is needed to check that equation. This identity does not manufacture
an extra dynamical degree of freedom. The spatial trace equation is another
useful consistency check, also insensitive to a change of the u acceleration:

    P''+(4+h)P'+(3+2h)P
       =x w_chi-x^2P+(3/2)x f_chi+D sqrt(a) f_u.   (10)

It follows from(6)-(7). Equations(8)-(9) distinguish integration residuals
from physical modes. The proof and implementation concern k>0; the exactly
homogeneous problem is handled separately, not by dividing by Q=0.

## Short-wavelength matter response and an optical discriminator

For Q>>1, choose the slowly varying matter solution with time derivatives of
order H and no independently large homogeneous scalar waves. On a bounded
N interval with fixed candidate coefficients, (3) and the constraints give

    f_u=-sqrt(a)D d/Q+O(Q^-2 d),
    f_chi=O(Q^-2 d),
    P=-D d/Q+O(Q^-2 d),                            (11)

where constants in the remainder may depend on the fixed coupling and the
chosen interval. Arbitrary free scalar-wave initial data need not obey this
closure; short wavelength alone is insufficient.

Consequently physical acceleration and curvature potentials are

    Psi_J=-(1+a)D d/Q+O(Q^-2 d),
    Phi_J=-(1-a)D d/Q+O(Q^-2 d),
    (Phi_J+Psi_J)/2=P.                             (12)

Since G_N=G_*(1+a), physical dust growth at leading order obeys

    d''+(2+h)d'-(1+a)D d=0,
    (1+a)D=(3/2)Omega_m(N),
    Omega_m(N)=m exp(-3N)/[m exp(-3N)+1-m].         (13)

This is the same growing-mode equation as the chosen flat dust-plus-constant
GR benchmark. Matching the background did not erase every gravitational
signature: the lensing strength in units of G_N is Sigma=1/(1+a), whereas
the acceleration strength is mu=1. The leading slip is (1-a)/(1+a), consistent
with the earlier local optical relation under its separate matching premises.
These are asymptotic response coefficients, not exact finite-k identities.

Define f_g=dln D_g/dln R for the regular growing solution of(13). With the
standard linear, scale-independent galaxy-tracing, velocity and projected
lensing bridges, the theoretical lensing/velocity ratio is

    E_G(z)=m/[(1+a)f_g(z)]                         (14)

to this leading short-wavelength order. One way to obtain it is to divide
-k^2(Phi_J+Psi_J) by 3H0^2 R^-1 f_g delta_J; delta_J=d+O(Q^-1 d).
Bias and amplitude cancellation additionally requires the same tracer and
correlated density mode in the lensing and velocity measurements. The observed
annular/projected statistic has a different operational definition; equation
(14) is its prediction only under the stated bridges and corrections.

For a=1/2499, the ratio to the same-m GR prediction is 2499/2500, a decrease
of .04 percent. This coupling was fixed in earlier working constraints, not
chosen using an E_G measurement. Such a small leading difference does not
by itself predict a detectable discrepancy in a finite survey.

## Homogeneous initial conditions and the future flat direction

The previous background integrations started exactly on the constructed
trajectory. They do not show unique attraction to it. The full potential has
a de Sitter family

    chi=chi_c, u=arbitrary constant, dot phi=0, sigma=0,
    H_*^2=2V_Lambda/3.                             (15)

At its u=0 member, the Hessian eigenvalues are 0 and (9/4)H_*^2. Linear
homogeneous scalar perturbations restricted to delta sigma=0 at this limiting
vacuum satisfy

    delta u=C1+C2 exp(-3H_*t),
    delta chi=(C3+C4 t)exp(-3H_*t/2).              (16)

If dust perturbations are admitted at the exact vacuum boundary,
delta sigma=delta sigma_0 exp(-3H_*t) additionally drives the u equation.
Its particular solution adds

    +sqrt(a)delta sigma_0 t exp(-3H_*t)/(3H_*)

to delta u. Direct substitution into
ddot(delta u)+3H_*dot(delta u)=-sqrt(a)delta sigma verifies the sign.
This decaying resonant term leaves the neutral displacement intact.

There is a neutral u displacement; the isolated point u=0 is not an
asymptotically attracting equilibrium among the full vacuum family. This
does not prove that every finite-dust perturbation has a large late-time
offset or that the background is catastrophically unstable. At each constant
u, the physical Hubble scale is H_*/A and the weak-body G_J is G_*A^2(1+a).
Thus the family cannot be identified with a single physical matter-calibrated
solution merely by ignoring A. Initial-condition selection remains an input.

For actual finite-time homogeneous controls, use state Y=(u,chi,v_u,v_chi,l),
where l=ln sigma, H=sqrt[(2sigma+v^2+2V)/3]. Its full nonlinear equations in
Einstein N are

    phi'=v/H,
    v'=-3v-(grad V+alpha sigma)/H,
    l'=-3+alpha.v/H.                               (17)

At arbitrary Y, the exact first variation uses

    delta H/H=[sigma delta l+v.delta v+grad V.delta phi]/(3H^2),
    delta(phi')=delta v/H-(v/H)(delta H/H),
    delta(v')=-3delta v-(Hess V delta phi+alpha sigma delta l)/H
                       +[(grad V+alpha sigma)/H](delta H/H),
    delta(l')=alpha.delta(phi').                   (18)

This includes the response of the Friedmann-determined Hubble rate. Comparing
it with symmetric nonlinear perturbations checks initial-condition sensitivity
without silently freezing H or the coupled field. Any numeric gain or drift
is tied to its chosen interval, normalization and perturbation fixture; it is
not a prior probability, full nonlinear stability theorem or empirical bound.
The logarithmic density coordinate covers sigma>0 and does not include the
exact vacuum boundary. The finite-time histories are compared at fixed
Einstein N, not automatically at equal physical redshift N_J=N+sqrt(a)u.

The principal scalar kinetic and gradient matrices remain positive identity
matrices and tensor waves retain the Einstein light cone. This rules out a
wrong-sign scalar kinetic or high-frequency scalar gradient term in this
specified classical action. It does not rule out dust gravitational growth,
long-wavelength coupled instabilities, isocurvature histories, or shortcomings
of the matter approximation. CMB initial conditions, radiation, nonlinear
structure, galaxy selection and a quantum origin of fluctuations remain open.
