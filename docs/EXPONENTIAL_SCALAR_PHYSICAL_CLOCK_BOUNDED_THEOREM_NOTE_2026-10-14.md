# Bounded physical past duration without a vacuum-scale calibration

**Date:** 2026-10-14
**Status:** proposed_retained
**Claim type:** bounded_theorem
**Actual current surface status:** conditional-support
**Primary runner:** [exponential_scalar_physical_clock_check.py](../scripts/exponential_scalar_physical_clock_check.py)

The [complete supplied action](EXPONENTIAL_SCALAR_FUTURE_CONFINEMENT_BOUNDED_THEOREM_NOTE_2026-10-13.md)
and [weak-source calibration theorem](EXPONENTIAL_SCALAR_PHYSICAL_PAST_BOUNDED_THEOREM_NOTE_2026-10-14.md)
remain explicit inputs. The [thermal-bath charge bound](EXPONENTIAL_SCALAR_THERMAL_BOUNCE_BOUNDED_THEOREM_NOTE_2026-10-14.md)
provides one conditional realization of the uniform charge premise below.

A joint energy-and-clock inequality removes a separately assumed global
conformal cap and a calibrated vacuum scale from a flat physical-duration
bound. It retains positive energy, a uniform coupling bound, a suitable matter
charge comparison and appropriate calibration. Its physical endpoint density
can be expressed using observed photons, but that does not establish the other
premises or measure a cosmic age. The action and initial history remain open.

## I. Physical-clock derivation

Direct author /root. This derives a conditional physical proper-time interval
bound using positive energy and the conformal coupling. It does not derive a
cosmic state, a measured gravity environment, matter conservation across all
real thermal epochs, or an age of the actual universe.

### Observational question and stated domain

The earlier positive-radiation comparison used a supplied vacuum scale Hv and
bounded A by a global field-space maximum. Can physical elapsed time instead
be bounded by the measured-clock density at one event and a proved coupling
constraint? A real application still needs the appropriate gravitational
normalization and matter history. No observed number is fitted here.

Take a regular connected spatially flat homogeneous Einstein-frame history with

    3Q H^2 = Q w_phi + V + rho_B,E + rho_o,
    w_phi=|dot phi|_K^2>=0, Q>0, V>=0, rho_o>=0.

The selected bath has rho_B,E>0. Let A>0, C=A^2, b=d ln A,
q=|b|_K^2<=qmax<1/3, and c=sqrt(3qmax)<1. Assume fixed Q and one fixed
qmax for this history. Physical clocks obey dt_J=A dt_E,
a_J=A a_E, H_J=(H+L)/A, L=dot A/A=b.dot phi.

The final event0 has H_J,0>0, positive bath density and finite field values.
For every earlier event in the interval assume the finite charge comparison

    D(t)=rho_B,E(t) a_E(t)^4 >= D0/R,       R>=1.       (1)

Separately conserved positive traceless radiation gives R=1. The proved
isolated fixed-entropy ideal photon/pair bath gives R=(11/4)^(1/3) even
through its finite-mass transition. More general matter requires its own
uniform past-to-final charge bound. A postulated R is an assumption unless
such a matter argument is provided. No monotone A is assumed.

### Expansion and clock control follow from the constraint

Cauchy-Schwarz and the positive-energy constraint give

    |L|<=sqrt(q w_phi)<=sqrt(3qmax)|H|=c|H|.           (2)

The bath makes H nonzero on every regular event. If H<0, then H+L<0,
contradicting positive H_J at the final event. Continuity of nonzero H
therefore forces H>0 throughout the connected interval. Also H+L>0,
so physical expansion is positive throughout. Set x=a_E/a_E,0 in (0,1]
for earlier events. Dividing (2) by positive H yields

    -c<=d ln A/d ln a_E<=c,
    A(t)<=A0 x^-c.                                  (3)

The upper past bound uses the lower logarithmic derivative -c. Reversing
integration endpoints would give a wrong clock estimate. This bound permits
A to grow toward the past; no global maximum of A has entered.

Equation (1) and Friedmann give

    rho_B,E(t)>=rho_B,E,0 x^-4/R,
    H(t)>=sqrt[rho_B,E,0/(3Q R)] x^-2.               (4)

For any earlier regular event with Einstein ratio x_i>0, physical duration is

    Delta t_J = integral_(x_i)^1 A(x)/(x H(x)) dx
       <= A0 sqrt[3Q R/rho_B,E,0]
                       (1-x_i^(2-c))/(2-c)
       <  A0 sqrt[3Q R/rho_B,E,0]/(2-c).             (5)

Thus the supremum of regular past physical duration is bounded by

    T_J,max <= sqrt[3Q R/(C0 rho_B,J,0)]/(2-c).       (6)

We used rho_B,E,0=C0^2 rho_B,J,0 and A0=sqrt(C0).
The bound does not require V to have a strictly positive floor or specify Hv.
It holds if an earlier chart boundary occurs at finite positive a_E as well;
it does not classify that boundary or prove an extension impossible. A supremum
can saturate the limiting inequality even though each finite interval is strict.
The positive final bath, charge control, spatial flatness and c<1 remain
substantive conditions. Positive spatial curvature changes Friedmann and is
outside this proof; previously found regular curved histories are not excluded.

The integral alone converges for c<2, but expansion/sign control used c<1.
This derivation does not claim the same theorem merely from c<2. For the
candidate supplied metric q=a/J<a, a=(1-k)(1+3k)/4 with0<k<1/3, choose
qmax=a. Then c=sqrt(3a)<1 is uniform over its finite field chart and positive
kinetic domain. Choosing this envelope is action algebra, not selecting a state.

### What a positive measured gravity normalization would add

Define G_bare,0=C0/(8piQ), and for a specified positive G_cal define
 gamma0=G_cal/G_bare,0>0. Equation(6) becomes the identity-bound

    T_J,max <= sqrt[3 R gamma0/(8pi G_cal rho_B,J,0)]/(2-c). (7)

The local laboratory coefficient and cosmological coefficient are not equated.
If the same-background weak-source calibration and an independently justified
error ceiling eta>=0 give gamma0<=(1+eta)(1+q0)<4(1+eta)/3, then

    T_J,max < sqrt[R(1+eta)/(2pi G_cal rho_B,J,0)]/(2-c)
            < sqrt[R(1+eta)/(2pi G_cal rho_B,J,0)].    (8)

The second inequality uses2-c>1. This removes C0 and Hv from that conditional
upper estimate. At different environmental backgrounds the previous principal
ceiling is gamma0<=(1+eta)(1+k)/C0; it does not cancel C0 and cannot be silently
replaced by Eq8. A real numerical age statement requires actual calibration
and a valid bath interval. Present radiation alone does not establish them.

### Controls and limits

For A constant (c=0) and a spatially flat pure-radiation model with V=0,
a_E proportional tosqrt(t_E), the sharp physical elapsed time to its zero-radius
boundary is A0 sqrt(3Q/rho_E0)/2. It equals Eq6 with R=1, and provides a
normalization control in the general action class. It is not an exact member
of the candidate with Hv>0; that candidate has a positive potential floor.
A constant-scalar radiation-plus-vacuum history instead has an elapsed time
below the same floor-free bound. Neither example proves a nonsingular origin.

Equations(3) and(4) are separate necessary envelopes and need not saturate
simultaneously in a scalar history: saturating the coupling-speed envelope
would require scalar kinetic energy, while saturation of the Friedmann lower
bound would leave no such energy. The bound is sufficient and is not claimed
optimal for c>0. Power-law envelope controls below verify its integration and
signs only; they are not passed off as complete solutions. No chosen six-state,
fixed-point past boundary, finite density cutoff, entropy selector, new scale
or empirical acceptance has been supplied by this argument.


### Stronger joint energy-and-clock inequality

The separate envelopes in Eq5 discard the energy cost of rapid conformal
motion. Keeping that cost gives a stronger state-independent estimate. For
qbar=qmax>0, Cauchy-Schwarz gives w_phi-L^2/qbar>=0. Substituting the flat
Friedmann constraint into the following exact identity yields

    (2H+L)^2-(4-3qbar)rho_B,E/(3Q)
      =(3qbar H+2L)^2/(3qbar)
       +(4-3qbar)(w_phi-L^2/qbar)/3
       +(4-3qbar)(V+rho_o)/(3Q) >=0.                 (9)

The previously proved H>0 and |L|<=cH imply2H+L>0, so the positive
square root may be taken. Define the positive geometric quantity
Phi=A a_E^2. Its physical-time derivative is

    dPhi/dt_J=a_E^2(2H+L)
       >=sqrt[(4-3qbar)D0/(3Q R)].                  (10)

No bound on A itself is used in Eq10. Integrating between any two regular
events in the specified past interval gives

    Delta t_J <= (Phi0-Phi_i) sqrt[3Q R/((4-3qbar)D0)]
              < Phi0 sqrt[3Q R/((4-3qbar)D0)],
    T_J,max <= sqrt[3Q R/(C0 rho_B,J,0)]/sqrt(4-3qbar). (11)

This sharpens Eq6 because sqrt(4-c^2)>2-c for0<c<1. The qbar=0 case has
L=0 and follows directly with denominator2, without dividing by qbar in Eq9.
Neither this algebraic improvement nor saturation of its instantaneous square
constructs a scalar trajectory that saturates the integrated bound for qbar>0.
The c=0 pure-radiation normalization control remains valid.

With positive gamma0 as in Eq7,

    T_J,max <= sqrt[3R gamma0/(8pi G_cal rho_B,J,0)]/sqrt(4-3qbar). (12)

Within the same-background principal/error-ceiling regime used in Eq8,

    T_J,max < sqrt[R(1+eta)/(2pi G_cal rho_B,J,0)]/sqrt(4-3qbar)
             < sqrt[R(1+eta)/(6pi G_cal rho_B,J,0)].  (13)

The final strict inequality uses qbar<1/3. The action candidate has qbar=a(k),
so the positivity needed in Eq9 follows from its same fixed parameter domain.
Distinct calibration backgrounds still leave the unmeasured C0 factor; Eq13
is not adopted as a measured age bound. The stronger proof drops neither
flatness nor the supplied/derived matter-charge comparison. It eliminates
an independent Hv calibration and a separately assumed global conformal cap
from this conditional physical-clock comparison.

## II. Published-input normalization and its limit

The published aggregate CMB temperature is 2.72548 +/- 0.00057 K (Fixsen, Table2 and conclusion). CODATA2022 recommends G=6.67430(15)e-11 m^3 kg^-1 s^-2, with the parentheses denoting standard uncertainty. These values are read as calibration/development inputs; none were fitted to the scalar model and none constitutes an independent test of it.

Using the Planck blackbody law and exact SI definitions,

 u_gamma = pi^2 (k_B T)^4/(15 hbar^3 c^3),
 rho_gamma,mass = u_gamma/c^2,
 tau_ref = 1/sqrt(6 pi G_cal rho_gamma,mass).

This gives u_gamma=4.1746783808e-14 J/m^3, rho_gamma,mass=4.6449561344e-31 kg/m^3, and tau_ref=1310.846386 Gyr (Julian-year convention). The universal same-background bound in the preceding physical-clock theorem would be tau_ref sqrt[R(1+eta)] if all its premises hold for the selected interval and bath. The formula uses mass density in SI; inserting energy density directly would lose a factor c in the time.

The number is a normalization diagnostic, not a measured cosmic age or a universal upper age. The present CMB temperature does not establish a uniform past charge bound, spatial flatness through that interval, or equality of laboratory and cosmological response environments. In particular G's quoted measurement error is not eta: eta bounds the theory-to-experiment response approximation and remains unjustified. No present-day photon calibration selects the supplied scalar action, potential or vacuum scale.

The input +/-uncertainty rectangle gives tau_ref in [1310.283540,1311.409589] Gyr. This is deterministic sensitivity to those published input ranges, not a simultaneous confidence interval and not a fitted cosmological constraint. The weak numerical ceiling illustrates why the mathematical elimination of Hv and a global A cap does not by itself produce a useful measured early-history test.

Primary sources, accessed2026-10-14:
- Fixsen: https://arxiv.org/pdf/0911.1955 (Table2 p5, conclusion p6).
- NIST: https://physics.nist.gov/cuu/Constants/Table/allascii.txt (2022 table; G,c,h,k_B).

Saved inputs, source bytes/hashes, code, full outputs and dimensional controls accompany this note. The original clock proof and its independent seal are unchanged. Twelve direct checks cover SI dimensions, two blackbody routes, scaling, rectangle orientation and q-envelope samples; they are numerical/formula validation, not an empirical acceptance count.

## Computational and empirical scope

The primary runner checks57 exact and specified-history controls from the
clock derivation and12 SI/numerical controls for the published-input example.
The uniform theorem follows from its written square completion and interval
argument; it is not inferred from sampled parameter values. Five actual
altered original clock implementations and all source versions are preserved.
A separate independent proof check retains its own complete toy histories,
seven altered implementations and source-bound receipt; it is not a second
empirical dataset. The published temperature and G are calibration/development
inputs, and their errors are not a theory-response error bound eta.

No held-out observation, likelihood fit, actual environment construction,
state selector, global completeness claim or derived action/scale is supplied.
These proposed conditional results carry no formal audit verdict or main merge.
