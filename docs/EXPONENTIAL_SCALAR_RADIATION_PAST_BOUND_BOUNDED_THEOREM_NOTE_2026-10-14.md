# Positive radiation bounds regular past duration

**Date:** 2026-10-14
**Status:** proposed_retained
**Claim type:** bounded_theorem
**Actual current surface status:** conditional-support
**Primary runner:** [exponential_scalar_radiation_past_bound_check.py](../scripts/exponential_scalar_radiation_past_bound_check.py)

The complete supplied action is defined in the
[future-confinement note](EXPONENTIAL_SCALAR_FUTURE_CONFINEMENT_BOUNDED_THEOREM_NOTE_2026-10-13.md).
This note bounds regular past duration without a specified scalar initial
point. It neither selects an initial state nor derives the action.

## Observation and premise boundary

Fixsen's primary reanalysis reports a nonzero microwave background temperature,
with combined estimate 2.72548 +/- 0.00057 K. Only the existence of positive
radiation motivates this calculation; the temperature is not converted to a
fitted density or used to calibrate this model. Source accessed directly:
[Fixsen2009, v2](https://arxiv.org/abs/0911.1955) (DOI10.1088/0004-637X/707/2/916).
This is exposed development evidence, not a held-out test of the result.

Adopt the full exponential action and physical metric of the canonical future
confinement note. Let physical dimensionful Einstein proper time be t_E,
physical proper time dt_J=A dt_E, A=sqrt(C)>0, and a_J=A a_E. Here Q>0,
H_v>0, 0<k<1/3, nu>0 remain supplied. Spatial flatness, homogeneous classical
evolution, the expanding sheet, and nonnegative other Einstein matter densities
are hypotheses. A separately conserved, isotropic massless component exists
throughout the past interval under consideration, with rho_r,J>0 and P_r,J=rho_r,J/3.
Collisions that preserve its total radiation energy do not change its background
conservation law; energy transfer into or out of this component does. Present
CMB detection does not establish these hypotheses for arbitrarily early times.

The canonical action gives K positive, U>=3/2 and

    3 Q H_E^2 = Q |dot(phi)|_K^2 + 2 Q H_v^2 U + rho_E,total.

Write a_k=(1-k)(1+3k)/4, s=(1+k)/(k(1-3k)), E=exp(2 sqrt(a_k) u),
F=1+sE and J=1+(1-3a_k)sE. Existing algebra from the future-confinement
result gives

    C=(1+s)E/F < Cmax=(1+s)/s,
    |grad ln A|_K^2=a_k/J < a_k < 1/3,
    1-3a_k=(1-3k)^2/4.

These are reused identities, not newly selected couplings. The Friedmann
constraint implies |dot(phi)|_K^2<3H_E^2. With b=d ln A and
eta_k=1-sqrt(3a_k)>0, Cauchy-Schwarz gives throughout a regular interval

    H_J=(H_E+b.dot(phi))/A >= eta_k H_E/A
        >= eta_k H_E/sqrt(Cmax)>0.                         (1)

The strictly expanding Einstein sheet cannot change sign since H_E^2>=H_v^2>0.
Thus no physical homogeneous bounce occurs within these premises and regular
field chart. This clock inequality was already established in the earlier
future theorem; its use below is the new application.

## Radiation comparison without a prescribed scalar state

Conformal density conversion and physical conservation give

    rho_r,E=A^4 rho_r,J,
    rho_r,J a_J^4=constant,
    rho_r,E a_E^4=constant.                               (2)

At a chosen regular event0 define a0=a_E(t0)>0, rho0=rho_r,E(t0)>0 and
D=a0^2 sqrt(rho0/(3Q))>0. Let X=a_E^2, X0=a0^2. Positivity in the constraint
then yields

    H_E^2 >= H_v^2 + D^2/a_E^4,
    dot X = 2 X H_E >= 2 sqrt(H_v^2 X^2+D^2).              (3)

Define T(X)=asinh(H_v X/D)/(2H_v). It obeys

    dT/dX = 1/[2 sqrt(H_v^2 X^2+D^2)],
    dT/dt_E >= 1.

Integrating from any earlier regular time t to t0 gives

    t0-t <= T(X0)-T(X(t)) < Tstar,
    Tstar = asinh(H_v sqrt(3Q/rho0))/(2H_v).              (4)

The supremum of regular past Einstein proper duration is at most Tstar, and

    past physical proper duration <= sqrt(Cmax) Tstar.    (5)

A weaker bound follows from asinh z<=z:

    Tstar <= (1/2) sqrt(3Q/rho0).

No finite scalar initial point, bounded earlier scalar history, normalized
radiation fixed point, prescribed scalar kinetic energy, or perturbation state
was used. The scale-factor normalization cancels from Tstar. In terms of
rho_r,J0 the density is rho0=C0^2 rho_r,J0. Q, H_v and C0 remain uncalibrated;
(4)-(5) are not a numerical age prediction. There is no uniform positive margin
in k as k approaches1/3, and no finite radiation bound when rho0=0.

## What the endpoint conclusion does and does not establish

Equations (4)-(5) exclude an arbitrarily long regular past interval satisfying
all the stated homogeneous premises. They do not select an endpoint state or
by themselves prove that a field-chart boundary encountered earlier has divergent
curvature. They do not prohibit an extension that changes the premises, and
are not a general geodesic-incompleteness theorem for all spacetimes.

If the regular branch continues backward until a_E tends to0, (2) makes
rho_r,E diverge, (3) makes H_E diverge, and (1) makes H_J diverge. For a smooth
spatially flat FLRW metric its Kretschmann scalar is

    R_abcd R^abcd = 12[(dot H_J+H_J^2)^2+H_J^4] >=12H_J^4.

Thus that particular endpoint has divergent physical curvature. This conditional
curvature conclusion must not be applied to an earlier chart endpoint with
finite a_E using the comparison inequality alone.

There is an exact saturating Einstein comparison solution within this action:
phi=0, dot(phi)=0, C=1, U=3/2, only radiation present. Its trace source is zero,
so the scalar equations remain satisfied. For t_E>t_B,

    a_E^2=(D/H_v) sinh[2H_v(t_E-t_B)],
    H_E=H_v coth[2H_v(t_E-t_B)].                           (6)

Here t0-t_B=Tstar, t_J=t_E, and curvature diverges as t approaches t_B.
The physical bound (5) is generally loose because Cmax>1 while this solution
has C=1. This is one unselected exact solution, not a proof all scalar histories
reach that endpoint or a claim the observations choose it.

With rho_r=0 the separate exact phi=0 vacuum has a_E=exp(H_v t_E), constant
curvature24H_v^4 and unbounded comoving past proper time in its flat patch.
It violates the strict radiation premise, so it is not a counterexample to
(4). It does disprove an overbroad conclusion that every candidate history
must have divergent curvature. No global extension statement is inferred from
this coordinate example.

## Assumption accounting

Retired within this comparison: a separately imposed bounded past scalar
trajectory or chosen radiation past fixed point is unnecessary to bound regular
past duration. Surviving: the supplied action/positive potential, coupling and
parameter domain, homogeneous spatial flatness, classical field chart, universal
physical metric, nonnegative other densities, and conserved positive radiation
over the interval. These conditions are not derived merely by detecting a CMB.
No state selection, finite regular origin, matter sector, dimensional hierarchy,
empirical acceptance or TOE follows. The comparison identifies a conflict for
any proposed infinite regular past that insists on keeping all those conditions.

## Verification and remaining physical work

The direct executable checks exact action/clock/conservation identities, the
comparison antiderivative and the action-compatible saturation solution. Its
positive-extra-density quadratures are comparison functions, not full scalar
orbits. The origin radiation solution has finite Ricci scalar12Hv^2 while its
Kretschmann invariant diverges, so Ricci scalar alone is not a sufficient test.
The companion independent proof uses distinct exact parameters and checks the
full lapse normalization, trace source, saturation, limits and endpoint logic.
All counts describe controls; they do not replace the stated sign-domain and
continuation reasoning. Prior sources, code, failures and independent receipts
are recoverable from the accompanying history archive.

The bound is finite for each fixed regular event with positive radiation.
There is no uniform calibrated age over unknown Q, Hv or C0 approaching zero,
or radiation density approaching zero. Observation has motivated a premise
that can be challenged by a forward physical model; it has not proved its
validity throughout the earliest universe. No formal audit or effective
retained grade is assigned by these checks.
