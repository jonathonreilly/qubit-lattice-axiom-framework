# Local scalar response and its energy cost away from the vacuum

**Date:** 2026-10-13
**Status:** proposed_retained
**Claim type:** bounded_theorem
**Actual current surface status:** conditional-support
**Primary runner:** [exponential_scalar_local_response_check.py](../scripts/exponential_scalar_local_response_check.py)

The observation-driven question is whether an expansion-compatible scalar
background can also yield sufficiently weak additional local gravity.
Instead of specifying the present field to be its vacuum or inserting a
screening factor, this note derives the background-dependent coupling and
its necessary scalar-energy cost from one explicit candidate action.
It proves exact identities and statements for the specified linear local
operator; finite-distance matching to an actual astronomical system remains
open. No empirical acceptance, framework derivation or effective audit grade
is asserted.

## Complete candidate model and premises

Use signature (-+++), phi=(u,x,y), and

    S=Q(k) integral sqrt(-ghat) [Rhat/2
      -K_AB ghat^{mu nu} partial_mu phi^A partial_nu phi^B-2Hv^2 U]
      +S_m[C ghat,matter], Q(k)=Q0(1+k), Q0>0, Hv>0.

For fixed 0<k<1/3 and nu>0, put

    a=(1-k)(1+3k)/4, alpha=sqrt(a), s=(1+k)/(k(1-3k)),
    E=exp(2alpha u), F=1+sE, J=1+(1-3a)sE,
    D=1+2(1+k)(x^2+y^2)/3,
    K=diag(J/F^2,(1+s)4k/(9FD),(1+s)k/(3FD)),
    C=(1+s)E/F,
    U=3/2+3s(E-1)^2/(2F^2)
      +(k/2)x^2 exp(-lambda_x u)+(k/3)y^2 exp(-lambda_y u)
      +nu(1+s)u^2/(2F^2),
    lambda_x=(1-k)/alpha, lambda_y=(1+k)/alpha.

All finite fields have K positive definite and C>0. The complete action,
three fields, universal physical metric, k, nu, Q0 and Hv are supplied
candidate inputs. The registered unit reference, isotropy and realized-state
premises do not select them. The scalar energy used below is defined in
Einstein proper time by v=dphi/d(Hv t_E) and

    e=K_AB v^A v^B/2+U-3/2, Z=s e.

The coupling and energy identities need no particular homogeneous fluid
history. The local readout additionally requires a weak nonrelativistic
source with negligible pressure and stress, a frozen
background on its length/time scales, control of masses/mixing and
cosmological time dependence, and a perturbation decaying to that background.
The finite-body statements apply to a locally flat, prescribed conserved
rest-density profile. They are not a full post-Newtonian or nonlinear
stellar calculation. Natural units are used for the action; spatial
source equations display the c^2 conversion when rho is a mass density.

## Principal weak-source response

Use the action above, with A=sqrt(C) and Gstar=1/(8 pi Q). The scalar action has
normalization -2 K_AB partial(phi^A)partial(phi^B) inside 1/(16 pi Gstar).
At any finite background b=(u,x,y), the matter covector is

    alpha_A = partial_A log A = (sqrt(a)/F,0,0).

Its squared field-metric norm, not a chosen field coordinate, controls the
leading weak-source strength:

    g = alpha_A K^{AB} alpha_B = a/J > 0.                 (1)

There is no x,y dependence in (1). In a locally frozen background, the
principal static equation in Einstein coordinates is

    Delta delta_phi^A = 4 pi Gstar K^{AB} alpha_B rho_E/c^2.

For an isolated weak nonrelativistic source with negligible pressure and
stress, negligible mass/mixing and time-dependent
terms on the tested length scale, and a perturbation decaying to that
background, its monopole is delta_phi^A=-alpha^A Ustar. At constant A_b,
M_E=A_b M_J and r_J=A_b r_E, so Ustar=Gstar C_b M_J/(r_J c^2).
Conformal multiplication of the Einstein metric then gives

    Phi_J=Ustar(1+g), Psi_J=Ustar(1-g),
    G_loc=Gstar C_b(1+g), gamma_eff-1=-2g/(1+g).          (2)

This is a conditional short-distance/long-range weak-source coefficient,
not a reconstructed Cassini light-time likelihood. A rolling background
need not be a critical point of U. Potential Hessians, background velocities,
metric constraints, environmental profiles and finite-source corrections
must be controlled before (2) becomes a finite-distance prediction for a
particular cosmological history. No vacuum mass is substituted at non-vacuum
points. The principal response itself follows from the action without a
vacuum choice; the omitted-terms estimate is not proved here.

## Exact relation to the future energy variable

Let s=(1+k)/(k(1-3k)), alpha=sqrt(a), chi=s(C-1). Then

    chi=s(E-1)/(1+sE), -s<chi<1,
    E=(1+chi/s)/(1-chi),
    g=k(1-chi)/(1-3k chi),
    dg/dchi=-k(1-3k)/(1-3k chi)^2 < 0.                  (3)

All finite real fields lie in this domain. The positive scalar energy is
e=K_AB v^A v^B/2+U-3/2, where v=dphi/d(Hv t_E), and Z=s e. Positivity of
the other potential and kinetic terms gives the exact necessary inequality

    Z >= 3 chi^2/2.                                    (4)

Consequently Z<=Zstar<3/2 implies |chi|<=w=sqrt(2 Zstar/3)<1 and

    k(1-w)/(1-3k w) <= g <= k(1+w)/(1+3k w).             (5)

The previous future theorem supplies one sufficient way to stay in this
region. It is not a necessary condition for a viable physical history.
Failing that theorem's criterion cannot be treated as an exclusion.

If (2) applies and an observation requires g<=b, with 0<b<k<1/3, then

    chi >= chi_req=(k-b)/(k(1-3b)) in (0,1),
    u >= log[(1+chi_req/s)/(1-chi_req)]/(2 alpha),
    Z >= 3 chi_req^2/2.                                 (6)

For k<=b there is no positive universal energy floor from this argument:
the vacuum already has g=k. In particular, squaring a negative chi_req to
claim a positive lower bound would be an error. For 0<nu<=6a a sharper
bound follows from monotonicity of U(u,0,0) for u>0:

    Z >= 3 chi_req^2/2
       + nu s u_req^2(1-chi_req)^2/[2(1+s)].             (7)

Other fields and kinetic energy cannot lower (7). For completeness, put
t=2alpha u. The sign of U_u(u,0,0) is the sign of
G(t)=12a(exp(t)-1)+nu t(1-t)+nu t/(s exp(t)). For t>0,
exp(t)-1>=t+t^2/2 gives
G(t)>=(12a+nu)t+(6a-nu)t^2+nu t/(s exp(t))>0 when 0<nu<=6a.
This proves the required monotonicity of the total potential on that line,
not of each separate summand.
As b/k becomes small at fixed k, the necessary lower bound approaches the
finite-field boundary energy 3/2. This is an energy cost of suppressing
the coupling by the background, not a proof that such a state is impossible.

An experimental b must come from an applicable finite-distance readout
and a stated uncertainty treatment. This theorem does not supply an
observational likelihood or an experimental acceptance threshold.

## An exact local-gravity cancellation, not absence of a scalar force

Since Q(k)=Q0(1+k), put G0=1/(8 pi Q0). The conditional coefficient in (2)
satisfies exactly

    R_G=G_loc/G0=C(1+g)/(1+k)
       =1-B chi^2/(1-3k chi),
    B=4k^2(1-3k)/(1+k)^2.                              (8)

Thus 0<R_G<=1, with equality only at u=0. The first derivative there
vanishes even though g=k remains nonzero. This explains why near agreement
of the inferred Newton strength alone cannot establish a small light-time
deviation. At fixed compact chi as k->0, R_G-1 is O(k^2) while g is O(k).
The assertion is not uniform near the moving lower boundary chi=-s.

For a homogeneous history p_u=du/dN and N_J=N+log A, differentiation gives

    chi_u=2 alpha (s+chi)(1-chi)/(1+s),
    d log R_G/dN_J = [-B chi(2-3k chi)/(1-3k chi)^2]
                    chi_u p_u/[R_G(1+alpha_B p_u)],
    alpha_B=alpha(1-chi)/(1+s).                         (9)

Equation (9) requires 1+alpha_B p_u nonzero; a forward physical clock
requires it to be positive. This is a derivative of the conditional
coefficient, not a complete prediction for an environmental measurement of dot G. No mass or time
calibration is needed to evaluate the dimensionless expression (9).

## The density-feedback sign throughout the trapped region

The u-coordinate lines at fixed x,y are field-space geodesics, since K_u
depends only on u and the kinetic metric is diagonal. Along them choose
dvarphi/du=sqrt(K_u). Then alpha_m=d log A/dvarphi=sqrt(g), and

    beta_m=dalpha_m/dvarphi
          =-[1+k+k(1-3k)chi]/(1-3k chi)^2,
    (1/A) d^2 A/dvarphi^2 = beta_m+g
          =-(1-k chi)(1+3k chi)/(1-3k chi)^2.           (10)

For every |chi|<1 and 0<k<1/3 this expression is strictly negative.
Therefore the negative density-mass feedback found at the vacuum does
not disappear by moving within the energy region Z<3/2. Holding conserved
Einstein-coordinate rest density rho0 fixed, rho_E=A_b rho0, gives the
one-direction, locally frozen linear prescribed-source problem

    (Delta-mu^2+4 pi Gstar rho_E eta/c^2) delta_varphi
       =4 pi Gstar alpha_m rho_E/c^2,
    eta=-(beta_m+g)>0.                                 (11)

Here a nonnegative mu^2 is a specified operator coefficient; (11) does not
assert that the full coupled cosmological perturbations have one such
mass. Taking mu=0 is the principal approximation. Pressure, gravity and
source redistribution are omitted, as in the earlier finite-source block.

For that scalar operator assume rho_E is nonnegative, bounded and compactly
supported on R^3. On L-infinity(R^3), define

    (T_mu f)(r)=(Gstar/c^2) integral d^3r_prime rho_E(r_prime)
        exp(-mu|r-r_prime|) f(r_prime)/|r-r_prime|.

Its norm is at most q=sup_r (T_0 1)(r)<infinity. With the boundary condition
delta_varphi->0 as |r|->infinity and eta q<1, the solution is

    delta_varphi=-alpha_m sum_(n>=0) eta^n T_mu^(n+1) 1,
    ||delta_varphi||_infinity <= alpha_m q/(1-eta q).    (12)

Its field amplitude and effective source are enhanced relative to the
no-feedback problem. This says nothing about arbitrary force-vector
ordering, the omitted terms, or all nonlinear compact objects. In the mu=0 limit, for a
uniform ball let Phi=Gstar M_E/(Rc^2) and z=sqrt(3 eta Phi), with
M_E=integral rho_E d^3r evaluated at the prescribed background. Then

    delta_varphi_in/alpha_m=(1/eta)[1-sin(zr/R)/((zr/R)cos z)],
    delta_varphi_out=-alpha_m Gstar M_E F_body/(r c^2),
    F_body=3(tan z-z)/z^3=1+(6/5)eta Phi+O(Phi^2).      (13)

The same derivative-sign argument fails sufficiently far outside the
trapped region. Equation (10) changes sign at chi=-1/(3k), corresponding
to E=2k/(1+k). No blanket no-screening theorem is claimed.

## Vacuum mass and range are consequences of the same action

At u=x=y=0 the potential is critical, C=1 and the covariant Hessian equals
the coordinate Hessian. The linear Einstein-time squared mass frequencies
are the eigenvalues of Hv^2 K^{-1} Hess(U). The matrices are diagonal there,
giving

    m_u^2/Hv^2=4[3(1+k)+nu]/(1-3k),
    m_x^2/Hv^2=9/4, m_y^2/Hv^2=2.

Only u has a linear matter coupling. Thus its vacuum inverse length is
mu=m_u/c. For nu=1 and small k, m_u is approximately 4Hv, so a cosmological
calibration of Hv gives a cosmological vacuum range for that parameter
choice. The ratio m_u/Hv is unbounded if nu grows or k approaches 1/3;
no uniform range statement holds over the entire model domain. The mass
formula does not derive Hv or the present state. These vacuum masses
must not be substituted for the full coupled perturbation operator on a
rolling, non-vacuum background. Likewise (10) gives beta_m=-(1+k) and
eta=1 at the vacuum without a supplied local screening parameter.

## Evidence and unresolved physical assumptions

The primary runner differentiates the complete coupling and metric, checks
the exact identities, vacuum Hessian and massless sphere matching, and
checks action derivatives at independent arbitrary high-precision points.
The handwritten domain, monotonicity and positive-operator arguments are
essential; finite numerical checks do not replace them. Preserved campaign
evidence includes prior vacuum body solvers and the new evaluation of all
ten already exposed finite-k cosmological endpoints. None is a blind
observational test or a certified full-history error enclosure.

The result supplies state-dependent formulas and a necessary energy cost
instead of assuming a vacuum background or inserting a force-suppression
factor. It does not derive the action, k, nu, the scale hierarchy, the
observed initial state, or cosmological/environmental matching. A field
outside the sufficient trapped region is not excluded by this result.
A short-distance coefficient is not automatically an experimentally fitted
PPN parameter or a measured time variation of Newton's constant.
