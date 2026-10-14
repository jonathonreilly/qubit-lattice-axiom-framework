# Positive curvature permits regular radiation histories with explicit state choices

**Date:** 2026-10-14
**Status:** proposed_retained
**Claim type:** bounded_theorem
**Actual current surface status:** conditional-support
**Primary runner:** [exponential_scalar_curvature_loophole_check.py](../scripts/exponential_scalar_curvature_loophole_check.py)

The supplied action is defined in the
[future-confinement note](EXPONENTIAL_SCALAR_FUTURE_CONFINEMENT_BOUNDED_THEOREM_NOTE_2026-10-13.md).
This result tests the exact-flatness premise of the
[positive-radiation duration bound](EXPONENTIAL_SCALAR_RADIATION_PAST_BOUND_BOUNDED_THEOREM_NOTE_2026-10-14.md).
It is a classical reconstruction within that action; it does not derive the
action or select spatial geometry, matter content, scales or an initial state.


Direct reconstruction by /root of a classical closed-FLRW radiation/vacuum
solution within the supplied scalar action. This is not a new cosmological
mechanism or a selected history. It challenges the exact spatial-flatness
premise of the previous past-duration theorem.

The primary observational motivation is finite precision in spatial curvature,
not evidence that a particular nonflat history is realized. Planck2018 VI,
arXiv1807.06209v4, section7.3, Eq45b gives Omega_K=0.0007+/-0.0019 at68 percent
for its temperature/polarization/lensing plus BAO combination; Table4 gives
+/-0.0037 at95 percent. This is a minimal nonflat extension of base LambdaCDM.
These exposed development constraints do not establish exact zero curvature
and are not imported as a likelihood for this scalar model. No raw data fit.
Source: https://arxiv.org/html/1807.06209v4 .

## Same supplied action, changed geometry and chosen matter state

Let the spatial metric have constant positive curvature Kc>0 with
three-curvature6Kc/a_E^2. The scale factor need not be dimensionless, provided
Kc/a_E^2 has inverse-time-square units. Adopt the origin scalar solution
phi=dot(phi)=0, C=1, U=3/2 and only positive conserved isotropic radiation.
The scalar gradient vanishes and its radiation trace source vanishes, so the
scalar equation is satisfied for any allowed k,nu. This explicitly omits dust
and other observed matter; it is not a fit to our universe. Adding traceful
dust would generally move the scalar and require a new calculation.

Write h=Hv>0, Q>0 and rho_r=3Q D^2/a_E^4 with D>0. Einstein and physical
clocks coincide. The exact homogeneous equations are

    H^2=h^2+D^2/a^4-Kc/a^2,
    dot H=Kc/a^2-2D^2/a^4,
    X=a^2>0, dot X^2=4(h^2 X^2-Kc X+D^2).             (1)

The negative spatial-curvature term invalidates the flat theorem's positive
lower bound on H^2. No ghost or negative radiation density is inserted.
Spatial curvature and selection of this radiation-only scalar state remain
new/explicit hypotheses.

## Strict discriminant: a regular bouncing branch

Define Delta=Kc^2-4h^2D^2. If Delta>0, set

    Xplus=(Kc+sqrt(Delta))/(2h^2),
    Xminus=(Kc-sqrt(Delta))/(2h^2)>0.

The large-X branch admits the exact solution for every real t,

    X(t)=[Kc+sqrt(Delta)cosh(2h(t-tb))]/(2h^2).       (2)

It has X>=Xplus>0 and H(tb)=0 with dot H(tb)=sqrt(Delta)/Xplus>0. The past
is contracting and the future expanding; neither is selected by observing
expansion at one event alone. Radiation is bounded by3QD^2/Xplus^2.
For the physical FLRW metric,

    Ricci=12h^2,
    Kretschmann=24[h^4+D^4/X^4].                      (3)

Both are bounded. All field variables and positive densities in this chosen
homogeneous solution are regular at the bounce. On a complete S^3 spatial
section with this smooth a(t)>=amin>0 for t in R, causal geodesics are complete:
for a timelike geodesic with conserved spatial momentum magnitude P,
dtau/dt=(1+P^2/a^2)^(-1/2) has a positive lower bound; a null affine parameter
has dlambda/dt=a/P. Both integrals diverge at either infinite cosmic-time end.
This is a property of this exact homogeneous spacetime, not a proof of
inhomogeneous, nonlinear or quantum stability.

Delta>0 alone does not select this branch. The separate allowed small-X
branch0<X<=Xminus reaches radiation-curvature singularities. The nonsingular
branch and its time orientation/history are still initial-state choices.

## Critical and excluded limits

At Delta=0, Xm=Kc/(2h^2)=D/h. There is an exact Einstein-static state X=Xm,
and an always-expanding solution

    X(t)=Xm+B exp(2h(t-t0)), B>0.                    (4)

This solution is regular for every real t, approaches the static radius in
the past and expands in the future. It has H>0 at every finite time, so it
shows that abandoning spatial flatness alone can defeat the prior regular
past-duration conclusion without a contracting era. The exact discriminant
relation is an added tuning, not dynamically selected. Equation(4) is not
obtained by simply setting Delta=0 at a fixed bounce time in(2); that limit
only gives the static solution. The homogeneous scale-factor equation has
perturbations about Xm obeying delta X_ddot=4h^2 delta X, so the critical
state does not supply unrestricted homogeneous attraction.

For Delta<0, the quadratic in(1) has no turning point; an expanding positive
radiation branch reaches X=0 in finite past time with divergent curvature.
For Delta>0 the large-X and small-X branches must still be distinguished.
For D=0, outside the strict positive-radiation premise, (2) reduces to the
usual complete closed de Sitter solution a=sqrt(Kc)cosh(h(t-tb))/h.
None of these limits changes the specified domain of the flat theorem.

## Observable requirements and why this is not yet a hot-universe model

At an expanding event H0>0, define fractions in this very model,

    L=h^2/H0^2, r=D^2/(a0^4 H0^2), d=Kc/(a0^2 H0^2)>0.

The constraint is L+r-d=1, and Delta>=0 implies d^2>=4Lr. On the regular
large-X or critical upper branch L>r at a finite expanding event, so

    r <= [(1+d)-sqrt(1+2d)]/2.                        (5)

For small d this is r<=d^2/4+O(d^3). Thus tiny present curvature requires a
quadratically tiny radiation fraction in this simple class. These fractions
involve the supplied Q,h and physical calibration; they are not automatically
the best-fit LambdaCDM fractions in the Planck paper. With the usual curvature
convention d=-Omega_K, this branch has negative Omega_K. For a purely illustrative
d<=0.003, equation(5) requires r<=2.24327520666367e-6 (rounded outward). This number is a conditional
algebraic benchmark, not a confidence-level exclusion of the scalar theory.

More directly, along the entire regular branch

    rho_r/(3Qh^2)=D^2/(h^2X^2)<=D^2/(h^2Xplus^2)<1

for Delta>0, and <=1 on the critical upper branch. The positive constant
vacuum component always exceeds the radiation component. This exact class
has no radiation-dominated hot era. Combining it with a real hot-universe
history would require changes to the chosen scalar trajectory, potential
energy history or matter content and a forward observational calculation.
Those changes cannot be counted as already derived from this example.

## Assumption accounting

The previous finite-duration result is conditional on spatial flatness; it is
not a universal singularity theorem for the supplied action. Positive spatial
curvature admits explicit regular positive-radiation histories in that action.
This removes a too-broad no-go statement, not the need to select geometry,
matter, parameters or initial state. The observed near-flatness likelihood is
model conditional; no numerical fit or empirical acceptance is claimed here.
The absence of a radiation-dominated era and omitted dust are substantive
limits of this exact loophole. It is a route to test, not a completed TOE.

## Verification and empirical separation

The direct checker verifies the supplied action at the constant scalar origin,
both Friedmann equations, radiation conservation, large/small/critical and
negative-discriminant branches, curvature invariants, finite endpoints and the
present-event fraction bound. It passes 81 controls, including exact identities
and three explicit synthetic parameter choices. The general causal-completeness
claim follows from the global radius bound and geodesic integrals stated above;
finite sample checks alone would not prove it. Three altered implementations
are actually executed and rejected: wrong bounce frequency, wrong critical
exponent and wrong fractional discriminant. These controls are mathematical
consistency checks, not measurements or additional observational evidence.

The Planck result is exposed development context; d<=0.003 is an illustrative
condition, not a posterior or fit imported into this scalar model. No raw-data
likelihood, held-out observational test, hot-universe reconstruction, quantum
completion or stability theorem is supplied. In particular, H-normalized
fractions diverge at a bounce; the no-radiation-dominance statement compares
positive energy densities and remains well defined there.
