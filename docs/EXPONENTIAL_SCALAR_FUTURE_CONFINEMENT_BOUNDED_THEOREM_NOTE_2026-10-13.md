# Future confinement for the exponential scalar candidate

**Date:** 2026-10-13
**Status:** proposed_retained
**Claim type:** bounded_theorem
**Actual current surface status:** conditional-support
**Primary runner:** [exponential_scalar_future_confinement_check.py](../scripts/exponential_scalar_future_confinement_check.py)

The result is a sufficient future trapping and convergence theorem for the
explicit classical model below. It replaces a future compactness hypothesis
by a testable inequality on exact initial data. It does not derive this model
from the framework axioms, select the observed universe, establish compactness
of a preceding numerical history, or receive an effective audit status.

## Observation-driven question and premise boundary

The motivating observation is late accelerated expansion together with tight
local limits on additional gravitational forces. A candidate that reproduces
an expansion history must also have well-defined dynamics: positivity of a
kinetic metric alone does not prevent its trajectory from approaching a
finite-distance singular boundary. This note derives a sufficient dynamical
condition for avoiding that boundary. The action and its physical interpretation
remain explicit candidate assumptions; no observational likelihood enters the
proof and no observational acceptance follows from it.

| Input | Role and status |
|---|---|
| The complete action, three scalar fields, conformal matter metric | Explicit candidate definitions, not derived physical laws |
| 0<k<1/3, nu>0, Q0>0 and Hv>0 | Supplied model parameters and scales; the dimensionless scale hierarchy remains open |
| Expanding, spatially flat homogeneous classical sector | Scope of the differential-equation theorem |
| Global future conserved physical fluid, 0<=P_J<=rho_J/3 | Conditional physical hypothesis; defined for every future N_J |
| Exact finite initial data satisfying (1) | Sufficient basin condition; its realization is not selected |
| 0<nu<=6a | Additional condition for unique-vacuum convergence, not needed for trapping |

The registered unit reference, kinetic isotropy and realized-state premises
supply only their registered content. They do not specify this action, the
six scalar initial values, or the dimensionless vacuum/gravity hierarchy.
The author has not changed those premises or the framework axioms.

## Precise model and target

Adopt signature (-+++), phi=(u,x,y), and the candidate action

    S = Q(k) integral sqrt(-ghat) [Rhat/2
        - K_AB ghat^{mu nu} partial_mu phi^A partial_nu phi^B - 2 Hv^2 U]
        + S_m[C ghat, matter],
    Q(k)=Q0(1+k), Q0>0, Hv>0.

There is no factor 1/2 before K in this action. Let 0<k<1/3, nu>0,
a=(1-k)(1+3k)/4, alpha=sqrt(a), s=(1+k)/(k(1-3k)),
E=exp(2alpha u), F=1+sE, J=1+(1-3a)sE,

    K=diag(J/F^2,(1+s)4k/(9FD),(1+s)k/(3FD)),
    D=1+2(1+k)(x^2+y^2)/3,
    C=(1+s)E/F, alpha_B=alpha/F,
    U=3/2+3s(E-1)^2/(2F^2)
      +(k/2)x^2 exp(-lambda_x u)+(k/3)y^2 exp(-lambda_y u)
      +nu(1+s)u^2/(2F^2).

Here lambda_x=(1-k)/alpha and lambda_y=(1+k)/alpha, both positive. The action has
Q(k)=Q0(1+k), with supplied Q0>0 and Hv>0. Choose one fixed positive
density unit rho_unit, write rho_J and P_J for physical densities divided
by that unit, and set Rstar=rho_unit/[2Q(k)Hv^2]>0 in the corresponding
natural-unit normalization. The proof uses its positivity, not a particular
calibrated value. Matter is
universally coupled to C ghat. Assume an expanding spatially flat,
homogeneous classical solution, and a nonnegative physical fluid with a
smooth conserved density-pressure history defined for every N_J>=N_J0 and satisfying 0<=P_J<=rho_J/3 and
d rho_J/dN_J=-3(rho_J+P_J). A smooth equation of state with such a global future solution is also sufficient;
no dust/radiation scalar matching is required.
Use dimensionless Einstein proper time Hv t_hat, N=log a_hat,
v=dphi/d(Hv t_hat), p=dphi/dN, H=Hhat/Hv, and

    sigma=C^2 Rstar rho_J, pi=C^2 Rstar P_J, tau=sigma-3pi,
    T=K_AB p_A p_B,
    e=(K_AB v_A v_B)/2+U-3/2 >=0, Z=s e.

All quantities at the start of the future interval carry subscript0.
Define

    Cmax=(1+s)/s, S=sigma0 sqrt(Cmax/C0),
    Phi(Z)=3[sqrt(2Z/3)-log(1+sqrt(2Z/3))].

Theorem: if

    Phi(Z0)+s k S^2/72 < Phi(3/2)=3(1-log 2),                 (1)

then the future solution stays in a compact subset of the finite scalar
chart and extends to every N>=N0. If also 0<nu<=6a, it converges to
(u,x,y,p)=(0,0,0,0), with H^2->1 and C->1. In particular nu=1
satisfies this extra condition throughout 0<k<1/3. The condition is
sufficient; no necessity or full basin-volume claim is made.

## Exact energy and matter bounds

The action's equations give

    3H^2=2(e+3/2+sigma),
    e'=-3H^2 T-alpha_B tau p_u,                              (2)
    N_J'=1+alpha_B p_u,
    sigma'=-3(sigma+pi)+alpha_B tau p_u.

Primes in (2) mean d/dN. The energy identity follows by contracting the
covariant scalar equation with v; the connection terms cancel the metric
derivative in d(K v^2)/dt. H^2>=1. Also T<3, because U>0 and sigma>=0
in the Friedmann constraint. Since alpha_B^2/K_u=a/J<=a<1/3,

    N_J' >= 1-sqrt(3a)>0.                                  (3)

Thus the physical clock remains oriented; it is a consequence here, not a
separate global chart assumption. Integrating physical fluid conservation,
and using N_J-N_J0=N-N0+(1/2)log(C/C0), gives

    sigma <= sigma0 sqrt(C/C0) exp(-3(N-N0))
          <= S exp(-3(N-N0)).                              (4)

Only nonnegative pressure, the conformal coupling, and the global C<Cmax
bound enter this step. In particular no monotonicity of the matter trace
itself is assumed.

## Coupling bound from the same potential

Introduce chi=s(C-1)=s(E-1)/F. This is a new variable, not the transverse
field x. Direct algebra gives

    U_vac-3/2=3chi^2/(2s),
    a/J=k(1-chi)/(1-3k chi),                                (5)
    -s<chi<1.

Here U_vac denotes just 3/2+3s(E-1)^2/(2F^2). Because all other
potential terms and kinetic energy are nonnegative,
|chi|<=sqrt(2Z/3)=w. The rational expression in (5) decreases in chi
for 0<k<1/3, so

    alpha_B^2/K_u <= k(1+w)/(1+3kw) <= k(1+w).              (6)

With |tau|<=sigma, maximizing -3H^2 t^2+sigma sqrt(a/J) t over
t=sqrt(T)>=0 bounds (2) by

    Z' <= s k sigma^2(1+w)/(12H^2).

Phi'(Z)=1/(1+sqrt(2Z/3)), including its continuous value1 at Z=0.
Equations (4) and H^2>=1 therefore imply, on any interval of existence,

    Phi(Z(N)) <= Phi(Z0)+s k S^2(1-exp(-6(N-N0)))/72.
                                                                    (7)

No assumption that Z was already confined is used to obtain (7).
Under (1), let Zstar=Phi^{-1}(Phi(Z0)+s k S^2/72)<3/2 and
wstar=sqrt(2Zstar/3)<1. Then Z<=Zstar and |chi|<=wstar for all
future times on which the solution exists.

## Continuation and avoidance of the finite-distance boundary

s>1. Solving chi for E yields

    E=(1+chi/s)/(1-chi),
    (1-wstar/s)/(1+wstar) <= E <= (1+wstar/s)/(1-wstar).

These are strictly positive finite constants, so u is bounded on both sides.
The nonnegative transverse potential terms bound x and y separately; their
coefficients have positive minima on this u interval. Consequently K is
positive with a uniform lower bound on the resulting compact field box.
The kinetic bound K v^2<=2e<=2Zstar/s bounds v. The Friedmann equation,
(4), and H>=1 bound both H and p=v/H. The assumed smooth fluid history has
no finite-N singularity. The first-order equations are smooth on a slightly
larger finite-state region. Ordinary local continuation then excludes a finite
future maximal N. Equation (3) also makes N_J grow without bound.

This is a trapping result for the dynamical solution. It does not make the
target-space metric geodesically complete or remove its singular endpoint.
It avoids that endpoint by an action-derived energy inequality under (1).

## Convergence for the declared nu range

Retaining half the dissipation when applying Young's inequality to (2) gives

    e' <= -(3/2)H^2 T + sigma^2(a/J)/(6H^2).

The last term is integrable by the compactness and density bounds. Since
e>=0, integral T dN is finite. The compact smooth equations give bounded
p' and positive uniformly bounded K, so p tends to0: otherwise bounded p'
would produce disjoint fixed-width excursions with divergent integral T.

Every accumulation point of the compact field trajectory must have grad U=0.
Indeed sigma,pi and p tend to0. If grad U were nonzero at an accumulation
point, continuity of the force and the fact p->0 would keep a component of
p' bounded away from0 for a fixed short interval near that point. Integrating
over that interval contradicts p->0. This uses no uncontrolled infinite-time
interchange with k->0; k is fixed throughout.

The x and y equations at a critical point force x=y=0. On that line put
t=2alpha u. The sign of U_u is the sign of

    G(t)=12a(exp(t)-1)+nu t(1-t)+nu t/(s exp(t)).

For t<0 all three terms are negative. For t>0, exp(t)-1>=t+t^2/2
implies G(t)>=(12a+nu)t+(6a-nu)t^2+nu t/(s exp(t))>0
when 0<nu<=6a. Thus the sole critical point is u=x=y=0. Every
accumulation point is this point, so the whole trajectory converges there.
The Friedmann and conformal formulas give the stated limiting H and C.

## What this retires and what remains

Condition (1) supplies a sufficient future compact-history
condition in place of an unexplained compactness assumption for this class.
It does not show that all early-time states enter this region, select the
present observed state, determine k/nu/Hv, or derive the action. Evaluating
(1) on floating-point endpoints is a diagnostic; it does not certify that
the preceding computed history lies in a rigorously bounded numerical error
enclosure. Any exact endpoint chosen within the strict region does satisfy
the mathematical theorem. The actual dark-energy value remains supplied
through Hv. No inhomogeneous/quantum stability or empirical acceptance follows.

## Dependency order, evidence and remaining work

The proof dependencies are: the declared action and conformal conservation
law imply (2); positivity and the Friedmann constraint imply clock orientation
and (4); the same potential and metric imply (5)-(6); Young's inequality and
the integrable density bound give (7); the strict energy margin gives a compact
state region and continuation; dissipation plus the extra nu bound gives the
unique limiting vacuum. The argument does not use observational fitted numbers,
a numerical trajectory, or a theorem about a different scalar action.

The companion runner independently checks exact algebraic steps and non-orbit
energy identities. These checks support the handwritten proof; finitely many
checks do not replace its continuation or convergence argument. The campaign's
18 two-solver future continuations are development diagnostics from specified
stored decimal initial data, not an error enclosure of the earlier cosmological
history. Their limiting k=0 cases are separate diagnostics; this theorem keeps
0<k<1/3 fixed. No uniform k->0 infinite-time limit is claimed.

The strict nu condition matters. Increasing nu outside the stated convergence
range can create other stationary points; the trapping proof still only gives
compactness there. An independent focused check and preserved failed attempts
are packaged with the campaign evidence. No formal audit has been run, and
no retained grade is assigned here.

The next physical bridge is the local force and its range around finite matter
sources. Convergence of a cosmological trajectory to u=x=y=0 does not by itself
imply that its scalar force vanishes or passes a local observation test.
