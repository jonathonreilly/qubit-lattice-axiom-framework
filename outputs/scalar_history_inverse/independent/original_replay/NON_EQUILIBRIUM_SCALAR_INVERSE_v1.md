# Scalar history constrained without minimum tracking

Author: root, 2026-10-16. Conditional mathematical development; no empirical
validation, framework-premise adoption, or formal audit status.

## Question and prior art

Can expansion and scalar response functions constrain an initial scalar
history without supplying a density-dependent minimum or a potential shape?
The answer below is conditional on an explicit action class and registered
functions. It replaces a continuous initial-velocity choice by at most six
candidates when the coupling is nonzero somewhere on a monotonic chart.
Some or all candidates can fail the full-history consistency test. This is
not a general uniqueness claim or a measurement of those functions.

Reconstruction is established prior art. Brax, Davis and Li,
[1111.6613v4](https://arxiv.org/abs/1111.6613v4), equations (6)–(10), and
Brax et al., [1203.4812v2](https://arxiv.org/abs/1203.4812v2), equations
(108)–(111), reconstruct a potential and coupling from mass/coupling functions
along a minimum; their displayed integral uses A approximately 1. The latter's
sections II.C–D state further assumptions about kicks, initial proximity,
large mass and slow variation. They do not establish a universal initial-state
selector. Boisseau et al., [gr-qc/0001066v1](https://arxiv.org/abs/gr-qc/0001066v1),
already reconstruct scalar-tensor functions using expansion and matter growth
without minimum tracking, with boundary, matter and perturbation conditions.
Our inverse variables and finite-candidate test differ; priority for the
algebraic reduction below has not been established. Standard background
reconstruction itself is not presented as a new result.

## Explicit model and input contract

Take units c=hbar=1, signature (-,+,+,+), a known positive reduced Planck
mass M, a spatially flat homogeneous Einstein-frame metric, one canonical
scalar, and pressureless particles universally coupled to A(phi)^2 g:

    S = integral sqrt(-g)[M^2 R/2 - (d phi)^2/2 - V(phi)]
        - sum_i m_i integral A(phi) ds_i .                 (1)

A is positive. The metric, canonical kinetic term, matter content,
universality, absence of radiation/curvature, and normalization are supplied
conditions. They have not been derived from the repository axioms or data.
No quantum or global stability conclusion follows.

Let t be registered Einstein proper time on a connected open interval I.
The proposed input functions are H(t) of class C3, alpha(t) of class C1,
and mu(t) continuous, where on a candidate history

    alpha(t) = [A_phi/A](phi(t)) = beta(t)/M,
    mu(t) = [V_phiphi + rho A_phiphi](phi(t)).             (2)

The derivative in mu holds the conserved bare-rest-mass density rho fixed.
It is not automatically a fitted pole mass, a Jordan-frame mass, a screened
body charge, or a full coupled cosmological perturbation eigenfrequency.
Its observational extraction remains an independent obligation. Likewise,
H measured with matter clocks is not automatically Einstein-frame H.
Signed alpha is assumed; an observation of beta squared alone is weaker.

The background particle number density scales as a^-3. With the bare masses
in (1), rho=rho_* a^-3, rho_*>0, and the actual Einstein-frame dust energy
density is r=A rho. Distinguish r from rho and from the Jordan density
rho_J: r=A^4 rho_J, rho=A^3 rho_J. These relations follow from the conformal
volume, proper time and particle energy, not a shorthand identification of
the densities. The numerical normalization of a and rho_* is supplied if
one wishes to reconstruct A absolutely. The product r does not require that
split. A positive rescaling of rho_* reciprocally rescales A, with a
corresponding bare-mass convention; it is not fixed by H,alpha,mu alone.

The theorem is on histories v=phi_dot nowhere zero and r>0 on I. Thus phi
has a single-valued inverse on its sampled range. Stationary points,
repeated field values, vacuum endpoints, spatial profiles, multiple fields,
additional fluids and action extensions are outside this theorem.

## Background equations from the supplied action

The particle action gives r=A rho, hence

    rho_dot = -3H rho,
    r_dot = (-3H + alpha v) r.                            (3)

Einstein and scalar equations are

    3M^2 H^2 = v^2/2 + V + r,
    -2M^2 H_dot = v^2 + r,
    v_dot + 3H v + V_phi + rho A_phi = 0.                 (4)

The source in the last equation is alpha r. This fixes both the density
convention and the M factor when beta=M alpha is used. The formulas below
retain scalar acceleration, dust exchange and both Einstein constraints.

Define functions determined by the input expansion:

    D = -2M^2 H_dot,  E = D_dot,  F = D_ddot,
    S = E + 3H D.                                        (5)

Every admissible history has D>0, r=D-v^2>0 and

    v_dot = G(t,v)
          = [S - alpha D v - 3H v^2 + alpha v^3]/(2v).    (6)

Indeed, differentiating r=D-v^2 and using (3) yields (6). The potential
along any such history is fixed by the first constraint:

    V(t) = 3M^2 H^2 - D + v^2/2.                         (7)

There is no freely additive potential constant once the complete H and
the stated matter class are fixed; adding another cosmological component
would change that premise and this conclusion.

Differentiate the scalar equation, with rho_dot=-3H rho:

    v_ddot + 3H v_dot + (3H_dot+mu)v - 3H alpha r = 0.    (8)

The mu appearing here is exactly the fixed-rho curvature (2). Therefore

    G_t + G_v G + 3H G + (3H_dot+mu)v
        - 3H alpha(D-v^2) = 0.                          (9)

Here G_t holds its second argument v fixed. No small acceleration, large
mass, minimum tracking or A approximately 1 approximation was used.

## Explicit polynomial and finite-candidate theorem

For v != 0, multiply (9) by 4v^3. The resulting polynomial P(t,v) is

    P = 2 alpha^2 v^6
      + (9H alpha + 2 alpha_dot) v^5
      + (-2D alpha^2 - 9H^2 + 6H_dot + 4mu) v^4
      + (-12DH alpha - 2D alpha_dot - E alpha) v^3
      + (18DH^2 + 6D H_dot + 2F + 12EH) v^2
      + (3D^2 H alpha + DE alpha) v
      - (3DH+E)^2.                                      (10)

**Conditional compatibility statement.** A C2 history v on I is compatible
with the supplied background and response inputs if and only if

    v != 0,  D-v^2 > 0,  v_dot=G(t,v),  P(t,v)=0          (11)

throughout I. Compatible means that some C2 functions A>0 and V on the
sampled field interval satisfy (1)–(4), with the prescribed alpha and mu.
Given rho_* and a normalization, these functions are obtained as

    phi(t) = phi_0 + integral v dt,
    A(phi(t)) = [D(t)-v(t)^2]/[rho_* a(t)^-3],
    V(phi(t)) = 3M^2 H(t)^2 - D(t) + v(t)^2/2.            (12)

They are fixed on that interval up to the arbitrary scalar origin phi_0.
Extension outside the sampled interval is not determined. If rho_* is not
fixed, the normalization freedom of A remains.

Necessity was derived above. For sufficiency, (6) implies (3), so the
logarithmic field derivative of the constructed A is alpha. Equations (7)
and r=D-v^2 supply both Einstein equations. Differentiate the first
Einstein equation and substitute the second and (3); division by v != 0
gives the scalar equation. Differentiating that equation identifies the
actual fixed-rho curvature with the mu in (8), because (9) holds and v != 0.
The inverse function theorem supplies C2 A(phi),V(phi) on the monotonic
sampled field interval. This establishes sufficiency without dropping an
integration constant from the differentiated scalar equation: the original
equation was recovered first from the Einstein constraints.

**Finite-candidate corollary.** If alpha(t_*) != 0 at any t_* in I, (10)
is a nonzero degree-six polynomial at t_*, hence there are at most six real
candidate velocities there. Only roots in
(-sqrt(D),0) union (0,sqrt(D)) are admissible. G is locally Lipschitz in v
away from zero. Thus each root determines at most one solution of (6), and
there are at most six compatible histories on the entire connected I.
Some or all initial roots may fail P=0 later, positivity, or continuation.
Instantaneous roots alone are not solutions, and six is an upper bound,
not a sharp count established here. If a polynomial is nonzero even with
alpha=0, its actual degree similarly bounds the candidates. Degenerate
zero polynomials require separate analysis.

This conditionally removes a *continuous freely chosen initial velocity*
from an ideal inverse with all three functions supplied. It does not select
one history in general, infer a physical initial state from current data,
or supply the input functions, action class or calibration.

## Exact non-equilibrium fixture and root filtering

These are constructed mathematical controls, not fitted cosmology. Set
M=1, t>0, H=1/t, alpha=1 and mu=7/t^2. A compatible solution is

    a=t, rho_*=1, phi=ln(t), v=1/t,
    r=1/t^2, A=exp(phi), V=(3/2) exp(-2phi).              (13)

The scalar force V_phi+rho A_phi=-2/t^2 is nonzero, balancing
v_dot+3Hv=2/t^2. This solution does not sit at a minimum.
The exact curvature is V_phiphi+rho A_phiphi=7/t^2.

Writing c=tv, the polynomial becomes

    t^6 P = (c-1)(2c^5+11c^4+20c^3+4).                  (14)

Any continuous root branch has constant c since the root set of this fixed
nonzero polynomial is finite. The differential constraint reduces to

    t^2 [G(t,c/t) + c/t^2] = (c-1)(c^2-2)/(2c).        (15)

The exact greatest common divisor of the polynomial in (14) and the
numerator in (15) is c-1. Therefore only v=1/t survives on an interval.
A second physical real instantaneous root near c=-0.66561063 is a false
candidate; its failure is dynamical, not a positivity cut. Substitution of
the minimum-trajectory formula 3H alpha r/mu gives 3/(7t), which is not
this actual history. This is a control of the approximation's missing
premise, not a counterexample to the cited results under their hypotheses.

## Exact degeneracy when the extra information is absent

For M=1, t>0, choose any constant 0<c^2<4/3 and set

    H=2/(3t), alpha=0, mu=2/t^2,
    phi=c ln(t/t_0)+phi_0, v=c/t,
    r=(4/3-c^2)/t^2,
    V=(c^2/(2t_0^2)) exp[-2(phi-phi_0)/c].               (16)

Choose a=(t/t_0)^(2/3) and any fixed rho_*>0, then
A=(4/3-c^2)/(rho_* t_0^2) is a positive constant. All background equations
and the curvature condition hold. The polynomial (10) vanishes identically
in v for these inputs. Distinct c magnitudes give different canonical
potential slopes, matter fractions and kinetic histories with exactly the
same H,alpha,mu. They are not just field translations. Fixing both a physical
dust normalization and the corresponding A normalization would distinguish
them; neither is part of this three-function inverse. This is the familiar
scaling family used as a counterexample, not a new cosmological model.

## Measurement, stability and uncertainty boundary

Matter clocks obey dt_J=A dt and a_J=A a, so
H_J=(H+alpha v)/A. Observed redshifts are a_J(t_o)/a_J(t_e)-1 under the
supplied universal matter/clock model. Feeding a measured H_J directly into
(5) would silently add a frame identification. Likewise, converting local
force ranges to mu(t) across cosmic and laboratory environments requires
registered scalar backgrounds and source response; equal dust density does
not enforce equal scalar state away from a minimum. The seven unopened
Fuchs traces are not a substitute for this missing cosmic input.

The highest expansion derivative in (10) is H''' through F. Exact functions
and exact roots are ideal input assumptions. No uncertainty, derivative
estimator, statistical coverage or root conditioning has yet been supplied.
No stable numerical inference follows from a finite algebraic root count.
Near v=0 or multiple roots the inverse can be singular. Even mu>0 is only
local fixed-density curvature, not full metric/matter stability or a global
bounded potential/history. A positive canonical kinetic term addresses its
own ghost sign only; no full perturbation theorem is asserted.

Remaining assumptions: action and matter class, normalization, registered
Einstein time/expansion, signed coupling and fixed-density curvature,
common sampled field chart, and real measurement extraction. Potential shape
and minimum tracking are not inserted in the compatibility calculation.
