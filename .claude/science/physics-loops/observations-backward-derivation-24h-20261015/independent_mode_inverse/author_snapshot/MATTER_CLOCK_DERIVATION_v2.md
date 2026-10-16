# Scalar compatibility in matter-clock time

Root's personal supporting derivation, 2026-10-16. Conditional mathematics;
commits-only follow-up to PR9638, not a new empirical result or priority claim.

The preceding inverse required Einstein-frame expansion and response functions.
Actual cosmological redshifts compare matter clocks. Supplying the Einstein
clock map would conceal an additional unknown function. This calculation
eliminates that supplied map within the same action class, provided two
precisely defined response functions can be registered in matter time. Their
extraction is still an open physical obligation.

## Observational entry point and surviving premises

The conditional action is

    S = int sqrt(-gE)[M^2 R_E/2 - (dphi)^2/2 - V(phi)]
        - sum_i m_i int A(phi) ds_E,
    gJ = A(phi)^2 gE, M>0, A>0.

Matter is pressureless and universally conformal, with constant bare masses.
The background is spatially flat FLRW. These are supplied action/matter
premises, not derived framework axioms. Matter rods and clocks use gJ only
under the universal matter/clock hypothesis. Spatial environmental matching,
absolute scales, calibration and perturbative measurement extraction remain.

Set tau to matter proper time, d tau=A dt, aJ=A aE, and h=d ln(aJ)/d tau.
For comoving emission/reception and universal atomic standards, the observed
redshift is 1+z=aJ(o)/aJ(e). Equivalently, an Einstein-frame photon frequency
redshifts as aE^-1 while the local atomic frequency scales as A. Therefore
redshift alone does not measure H_E. The usual redshift-drift identity is
dz/dtau_o=(1+z)h_o-h_e, conditional on comoving sources and the FLRW/clock
model. Distances, peculiar motions, absolute h_o and clocks need their own
registration. No such observational dataset is fitted in this block.

The ideal input functions on a connected open matter-time interval I are

    h(tau), b(tau)=M A_phi/A,
    kappa(tau)=[V_phiphi + rho A_phiphi]/A^2,             (1)

where the field derivatives hold the conserved bare Einstein density rho
fixed, not the physical Jordan density. Kappa has units of inverse matter
time squared, but this dimensional conversion does NOT identify it with a
measured normal-mode pole, quasistatic fitted range, or the curvature of the
Jordan potential. The metric/matter perturbations and time-dependent field
normalization must still be included in that correspondence.

Take h,b of class C3 and kappa of class C1 for the polynomial reduction below.
These are sufficient conditions, not a claim of minimal regularity. Let

    x = (1/M) dphi/dtau, q=b x, A'/A=q,
    H_E=A(h-q), v_E=M A x,
    R = r_E/(M^2 A^2) = rho_J/F, F=M^2/A^2.             (2)

Primes below mean matter-time derivatives. The chart has x nowhere zero and
R>0. Scalar origin, constant A normalization and extensions beyond the sampled
field interval are not fixed by the three input functions.

## Deriving the matter-time compatibility system

Einstein Raychaudhuri and dust exchange are

    -2M^2 dot(H_E)=v_E^2+r_E,
    dot(r_E)=(-3H_E+b v_E/M)r_E.

Use dot=A d/dtau and (2), without an adiabatic/minimum approximation. They give

    R = 2b x' + r0(tau,x),
    r0 = 2b' x - 2h' - 2bhx + (2b^2-1)x^2,
    R' + (3h-2bx)R = 0.                                (3)

The differentiated Einstein scalar equation is

    ddot(v_E)+3H_E dot(v_E)+(3dot(H_E)+mu_E)v_E
        -3H_E(b/M)r_E=0, mu_E=A^2 kappa.

Its complete matter-time form, after dividing by M A^3, is

    K := x'' + 3h x'
       + [3h'+kappa-2(b'x+b x')+6hbx-4b^2 x^2]x
       -3b(h-bx)R = 0.                                 (4)

No acceleration, dust energy exchange or conformal derivative is omitted.
Equations (3),(4), x!=0 and R>0 are the exact compatibility system within
the supplied action. It does not require an independently chosen A(tau).

For sufficiency construct, for any A0>0 and scalar origin phi0,

    A=A0 exp(int bx d tau), phi=phi0+M int x d tau,
    t=int d tau/A, aE=aJ/A, r_E=M^2 A^2 R,
    rho=r_E/A,
    V=M^2 A^2[3(h-bx)^2-x^2/2-R].                       (5)

Equation (3) implies rho*aE^3 is a positive constant, so the particle source
has exactly the prescribed bare-dust form. The logarithmic field derivative
of A is b/M. Raychaudhuri and Friedmann hold by construction. Differentiating
Friedmann, using Raychaudhuri and dust exchange, and dividing by v_E!=0 gives
the ORIGINAL scalar equation. Its derivative and (4) then give precisely
mu_E=A^2 kappa, without retaining an unfixed affine-force constant. The inverse
function theorem gives local A(phi),V(phi) on the sampled monotonic interval.
Conversely, any history from the action obeys (3),(4). This also explains why
the chosen A0 is an unresolved normalization rather than a derived scale.

## A first-order reduction and its explicit excluded set

Treat tau and x as independent arguments and write (4) as

    K = x'' + B1(tau,x)x' + B0(tau,x),
    B1 = 3h-2bx-6b^2(h-bx),
    B0 = [3h'+kappa-2b'x+6hbx-4b^2x^2]x
         -3b(h-bx)r0.

Let D denote the left side of the dust equation in (3). Direct elimination
of x'' gives D-2bK=C x'+N, where

    C = 2b' + partial_x r0 + 2b(3h-2bx) - 2b B1
      = -2[(6b^4-2b^2+1)x + b(1-6b^2)h - 2b'],
    N = partial_tau r0 + (3h-2bx)r0 - 2b B0.            (6)

All partial time derivatives hold x fixed. C is affine and N at most cubic
in x. The coefficient 6b^4-2b^2+1 is strictly positive for real b, so the
excluded C=0 set has one x value at each time. It need not be physically
inadmissible; histories there must be examined through (3),(4) and are not
classified by the division below.

On a whole chart where C!=0, define G=-N/C. A C2 history is compatible iff

    x'=G, x!=0, R=2bG+r0>0, Q(tau,x)=0                 (7)

throughout I, with

    Q = -N_tau C^2 + N C_tau C + N N_x C - N^2 C_x
        -B1 N C^2 + B0 C^3.                            (8)

Indeed, Q=C^3[G_tau+G_x G+B1 G+B0]. Thus (7) enforces K=0;
D-2bK=0 then enforces dust. The converse follows from (6). This remains
valid at b=0 as long as C!=0; no division by b was made.

Q has degree at most six in x. Its degree-six coefficient is

    8b^2(6b^2-1)(12b^2-7)(6b^4-2b^2+1).               (9)

If Q is nonzero at some interior time, each admissible root there determines
at most one full solution by local uniqueness of G away from C=0. Therefore
there are at most six scalar-velocity histories x(tau) on this regular chart.
This count does not include the continuous A0 normalization freedom, scalar
origin or extensions of the reconstructed action. If the coefficient
in (9) vanishes, lower coefficients may still bound the count; their vanishing
does not itself prove a continuum. No classification of identically zero Q
or singular C histories is claimed here. Nor is six proved sharp. This result
uses stronger derivative information than the earlier Einstein-time inverse.

Under scalar reflection x->-x,b->-b,b'->-b', C reverses sign and N is unchanged,
so G reverses sign after accounting for the x argument; the full equations
must be transformed, not a potential energy sign. A strictly positive B=b^2
on the entire interval supplies a global
orientation convention; coupling zeros need separate treatment.

## Constructed checks and residual scale

The earlier exact Einstein history M=1,H_E=1/t,phi=ln t,A=t,V=3/(2t^2),
r_E=t^-2 gives tau=t^2/2, aJ=2tau. Hence

    h=1/tau, b=1, kappa=7/(4tau^2),
    x=1/(2tau), R=1/(4tau^2).                          (10)

It is off a density minimum and satisfies the new system. Further checks
use forward power-law models, a non-power-law changing coupling, uncoupled
ambiguity and direct action/frame identities. All are synthetic controls,
not fits, validation sets or evidence for a physical scalar.

For fixed h,b,kappa and a surviving x, changing A0 by c>0 leaves all three
input functions and x,R unchanged. At the same matter time it gives

    A_new=c A, F_new=F/c^2, rhoJ_new=rhoJ/c^2,
    V_new(phi)=c^2 V(phi), rho_new=c rho,
    H_E,new=c H_E, v_E,new=c v_E, mu_E,new=c^2 mu_E.      (11)

Bare-density normalization changes consistently. These are separate possible
physical calibrations within this inverse, not a claim that every fixed-unit
physical measurement is invariant. An independently calibrated rhoJ and the
inferred R would fix F=rhoJ/R. Neither rhoJ nor F is automatically supplied
by an expansion curve or by fitting a response pole.

## Physical routes checked against primary literature

Reconstruction and frame transformation are established prior art; no general
novelty claim is made. Tsujikawa [0705.1032v4](https://arxiv.org/abs/0705.1032v4),
section V, distinguishes the force potential from the Einstein metric potential
and relates dust growth in the two frames. Its equations (76) give the standard
time/scale/density relations. The rendered equation (73) uses a conformal-factor
notation inconsistent with those relations; our metric transformation is
derived directly from gJ=A^2gE instead of copying that display.

Amendola et al. [1210.0439v2](https://arxiv.org/abs/1210.0439v2), sections II–V,
start with galaxy position/velocity/shape correlations. Their ratios remove an
unknown perturbation normalization, while their slip reconstruction retains
FLRW, matter, bias and scale-regime assumptions. They explicitly distinguish
growth-rate information from its missing initial condition and matter-density
normalization. A claim that a published growth summary directly provides b or
kappa would bypass that correspondence. Their b for galaxy bias is unrelated
to this note's scalar b.

Dalang, Fleury and Lombriser [1912.06117v3](https://arxiv.org/abs/1912.06117v3),
equations (56),(69), derive geometric-optics tensor transport with local Planck
coefficients at emission and reception. In the corresponding regime the
standard-siren distance ratio is sqrt(F_observer/F_source), with local endpoint
values. Equating those to a homogeneous cosmic F is an additional environmental
assumption; screened endpoints can share F despite interior variation. This
is a known limitation, not a new all-probe no-go. Wave-generation calibration,
scalar radiation and the geometric-optics domain also remain conditions.

The mathematical contribution here is a directly checked compatibility system
in matter-clock variables, not a completed measurement pipeline. Next work must
derive the coupled perturbation/readout map before inserting an observed slip,
growth spectrum or normal-mode pole for the response functions in (1).

## Independently found singular-chart witness

The focused checker independently constructed a positive-dust history lying
entirely on the excluded C=0 chart. Root read the frozen action-first proof
and checked the witness directly after that exposure. In stipulated M=1
reference units, for Einstein t>0 take

    H_E=12/(17t), phi=(4/17)ln(t), A=t^(2/17),
    r_E=392/(289t^2), V=32/(289t^2),
    tau=(17/19)t^(19/17).

Then h=14/(19tau), b=1/2, x=4/(19tau),
R=392/(361tau^2), kappa=2410/(361tau^2). The original
action equations, direct matter-time system and C=N=0 hold. It is a valid
conditional action/history, not an observational fit. Dividing by C would
discard it, so the regular-chart count must not be applied globally.
The independent proof also gives varying-coupling and uncoupled controls.
This witness is attributed to that focused check; it was not in root's
pre-exposure control set.

The v1 note,55root controls and original source bindings remain immutable.
This v2 narrows the wording of the finite count and appends the independently
found witness; it does not change the regular-chart equations.
