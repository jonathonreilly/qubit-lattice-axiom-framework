# Alternative radiation state and its conditional expansion prediction

**Date:** 2026-10-14
**Status:** proposed_retained
**Claim type:** bounded_theorem
**Actual current surface status:** conditional-support
**Primary runner:** [exponential_scalar_alternative_radiation_check.py](../scripts/exponential_scalar_alternative_radiation_check.py)

A candidate primordial scalar state must connect to measurable expansion,
and attraction must be checked with every scalar direction present. This
note derives an alternative radiation solution of a supplied action, proves
local stability in its complete six-dimensional limiting system, and derives
one physical expansion diagnostic. The state, action and actual gravity
calibration are not selected by observations here. No measured data are fitted.

## Complete supplied action and physical conventions

Use signature (-+++), phi=(u,x,y), and

    S=Q(k) integral sqrt(-ghat) [Rhat/2
      -K_AB ghat^{mu nu} partial_mu phi^A partial_nu phi^B-2Hv^2 U]
      +S_m[C ghat,matter], Q(k)=Q0(1+k), Q0>0, Hv>0.

For fixed 0<k<1/3 and nu>0, define

    a=(1-k)(1+3k)/4, alpha=sqrt(a), s=(1+k)/(k(1-3k)),
    E=exp(2alpha u), F=1+sE, J=1+(1-3a)sE,
    D=1+2(1+k)(x^2+y^2)/3,
    K=diag(J/F^2,(1+s)4k/(9FD),(1+s)k/(3FD)),
    C=(1+s)E/F,
    U=3/2+3s(E-1)^2/(2F^2)
      +(k/2)x^2 exp(-lambda_x u)+(k/3)y^2 exp(-lambda_y u)
      +nu(1+s)u^2/(2F^2),
    lambda_x=(1-k)/alpha, lambda_y=(1+k)/alpha.

The complete action, fields, universal matter metric, k,nu,Q0,Hv and matter
sector are model inputs. Framework unit, isotropy and realized-state premises
do not derive them. The restriction to a spatially flat classical homogeneous
geometry and ideal trace-free radiation is also explicit.

All densities below are dimensionful physical densities rho_phys. If a
dimensionless density rho_J=rho_phys/rho_unit is used, put
Rstar=rho_unit/(2Q Hv^2); then y_b^2=rho_phys/(2Q Hv^2)=Rstar rho_J.
The physical metric is g_J=C ghat, so dt_J=sqrt(C)dt_E and
N_J=N+log sqrt(C), where N=log a_E. Primes denote d/dN. A radiation fluid
has rho_phys proportional to exp(-4N_J), not exp(-4N) in general.

## Restricted branch selection from the equations

First test constant u and a constant finite nonzero ratio v=x/y in the
large-y limit, with q=(log|y|)'=-2 and h=H_E'/H_E=-2. At fixed u let
t=v^2, X=exp(-lambda_x u), Y=exp(-lambda_y u), and
B=(1+s)k/[2(1+k)F]. The limiting radial and mixed metric coefficients are

    G_ll=B(3+4t)/[3(1+t)], G_vl=4Bv/[3(1+t)],
    W=exp(2z)k(tX/2+Y/3), z=log(|y|/y_b).

The lowered radial, u and v equations require

    W/Hbar=G_ll,
    W_u/W=2B_u/B=-4alpha sE/F,
    W_v/W=2(G_vl+partial_v G_ll)/G_ll.

For v nonzero, the last equation gives X/Y=4(3+2t)/[3(3+t)]>1.
Since lambda_y-lambda_x=2k/alpha>0, this requires u>0. But the u equation is

    (3t lambda_x X+2lambda_y Y)/(3tX+2Y)=4alpha sE/F.

The left side is strictly below lambda_y while the right side is strictly
above lambda_y at u>0; lambda_y=4alpha s/(1+s). This contradiction excludes
only this finite nonzero mixed-ratio scaling ansatz. It does not classify
arbitrary histories, varying ratios or finite-field states.

The omitted x-only chart must be examined separately. Reflection y->-y
makes y=y'=0 invariant. For ell=log|x| and large |x| its radial coefficient
is Bx=(1+s)2k/[3(1+k)F]. The u balance gives

    lambda_x=4alpha sE_x/(1+sE_x),
    E_x=(1-3k)/[3(1+k)], u_x=log(E_x)/(2alpha)<0,
    C_x=(1-k)/(1+k), b=Bx(u_x)=2k(1-k)/[(1+k)(1-3k)],
    Hbar_x=2C_x^2/[3(1-2b)], W_x=b Hbar_x.

Positive radiation and potential require b<1/2. Equivalently,

    0<k<k_c=3-2sqrt(2), Delta=1-6k+k^2>0.

At k=k_c there is no finite positive scaling coefficient. Define
beta_x^2=2W_x exp(lambda_x u_x)/k and z=log(|x|/(beta_x y_b)). These
normalizations follow from the scaling equations; they are not fitted.
Both signs of x are possible. No probability or sign-selection rule follows.

## Limiting equations and exact local stability

Let theta=2alpha(u-u_x), p=theta', q=ell', E=E_x exp(theta), and write

    A=J/(4aF^2), B=(1+s)2k/[3(1+k)F], C=(1+s)E/F,
    l=2/(1+3k), W=W_x exp(2z-l theta),
    T=A p^2+B q^2, Hbar=H_E^2/(Hv^2 y_b^2)=2(C^2+W)/(3-T),
    h=-4C^2/(3Hbar)-T.

The finite radial metric is B*d*x^2/(1+d*x^2), d=2(1+k)/3. Taking its
large-field limit, and taking the same limit of U/y_b^2 and its original
physical-field gradients at bounded u,z, gives

    theta'=p, z'=q+2+p/F,
    p'=-(3+h)p-(A_theta/2A)p^2+(B_theta/2A)q^2+lW/(A Hbar),
    q'=-(3+h)q-(B_theta/B)pq-2W/(B Hbar).                  (1)

In particular, N_J'=1+p/(2F); the p/F term in z' follows from the physical
radiation clock. Taking fixed k before the large-field limit is essential.
The constant and nu-dependent potential terms vanish in this normalization;
they remain part of the full action. No long-time tracking estimate for
finite fields follows merely from this pointwise limit.

At (theta,z,p,q)=(0,0,0,-2), the full constrained four-dimensional Jacobian
has characteristic polynomial

    P(lambda)=(lambda^2+lambda)^2+S_x(lambda^2+lambda)+P_x,
    n_x=5-7k-21k^2+7k^3,
    S_x=4n_x/[(1+k)(1-3k)(1+3k)],
    P_x=64k(1-k)^2 Delta/[(1+k)^2(1-3k)^2(1+3k)].        (2)

This includes derivatives of Hbar,h and the physical clock. The primary
runner differentiates one nonlinear flow constructor using coefficient jets
of the orders actually needed; those derivatives come from the displayed
action coefficients. Separate lowered-equation identities bind that same
constructor away from the fixed point, including terms invisible to a first
Jacobian. The polynomial is not inferred by fitting sampled eigenvalues.

For 0<k<k_c<1/5, n_x>69/25, and the positive denominator of S_x is
less than 1+k<6/5. Therefore S_x>46/5. Also Delta<1-3k and
(1-k)^2/(1+k)<1 imply 0<P_x/S_x<80/69. Since 46/5>320/69,
S_x^2-4P_x>0. The two roots r_i of r^2-S_x r+P_x=0 are positive.
Each factor lambda^2+lambda+r_i has strictly negative-real-part roots.

The missing scalar direction is w=y/x. Pulling back the original x,y metric
gives B/(1+w^2)[dell^2+(3/4)(dw+w dell)^2]. Retain the mixed inverse metric
when differentiating the potential. At the x-only point the normal equation is

    w''+w'+Omega^2 w=0,
    Omega^2=-2/3+(16/9)exp[-(lambda_y-lambda_x)u_x]>10/9. (3)

Reflection makes the normal block decouple to linear order. Its two roots
have real part -1/2. All six limiting eigenvalues therefore have negative
real parts at each fixed allowed k. Smoothness near the positive point gives
local asymptotic stability: for its full Jacobian M, the positive quadratic
form from integral_0^infinity exp(M^T t)exp(M t)dt has derivative
-|delta|^2+O(|delta|^3)<0 in a sufficiently small neighborhood. This proves
neither a common basin as k approaches an endpoint nor observed capture,
full-action attraction, a past boundary condition or a global history.

As k tends to zero, (2) becomes lambda(lambda+1)(lambda^2+lambda+20).
Its zero root is simple, with lambda_slow=-(16/5)k+O(k^2). Linear relaxation
still requires a time of order 5/(16k) Einstein e-folds. No actual radiation
duration, initial amplitude or nonlinear erasure tolerance is supplied by this
asymptotic statement. The state remains an unselected conditional solution.

## A specified physical expansion readout

On this constant-u branch, H_J^2=H_E^2/C_x=Hbar_x rho_phys/(2Q C_x).
The reference gravity must identify a particular readout. In the stipulated
C=1 constant vacuum, the norm of grad log sqrt(C) in K is k. For a weak
nonrelativistic point source, negligible curvature and range suppression,
and an unsuppressed dynamical-force readout, the tensor contribution
1/(8pi Q) and scalar factor 1+k give G_vac=1/(8pi Q0). A known-mass ideal
lensing readout instead gives the tensor value 1/[8pi Q0(1+k)]. Finite-body
charge, environment and actual applicability are not inferred here.

Using only the specified vacuum dynamical reference, put

    R_H=H_J^2/[(8pi G_vac/3)rho_phys]
       =(1-k)(1-3k)/[(1+k)(1-6k+k^2)].                 (4)

Q0 and Hv cancel from this one conditional ratio. Their values and the actual
measured-gravity bridge remain open. The exact identities

    R_H-1=k(1+8k-k^2)/[(1+k)Delta]>0,
    R_H'=[1+16k-38k^2+8k^3-3k^4]/[(1+k)^2 Delta^2]>0

show strict increase from 1 to infinity on the physical branch. For the last
sign, write the numerator as (1-3k^4)+k(16-38k)+8k^3 and use k<1/5.
Thus an applicable exact ratio R_H>1 identifies one k in this interval;
other algebraic roots outside this interval are not physical inverse choices.
An unknown gravity calibration gamma=8pi Q0 G_cal instead measures R_H/gamma,
which cannot identify k alone. No experimental likelihood or exclusion is
claimed, especially for values with uncertainty or non-ideal radiation.

The small-k expansion is R_H=1+k+13k^2+O(k^3). The Einstein scalar energy
fraction is 2b, which is different from R_H-1. Both the physical clock and
the specified gravity reference matter. The coupling norm on the x-only
branch is 3k(1-k)/(1+3k), but a norm by itself is not a derived measured
PPN coefficient or a complete local response of a rolling environment.

## Evidence and assumptions still required

The exact action reduction, branch equations, constrained Jacobian, normal
metric, sign certificates and physical ratio are checked by the primary
runner. Seven high-precision spectra are implementation examples, not the
all-k proof or observations. Independent work reconstructs the Jacobian from
the original action in different coordinates, and bounds finite-field
normal-ratio acceleration differences for nu=1 pointwise at six couplings
and two fixed normal states. Those bounds
are not trajectory shadowing. The recovery archive preserves original
timeouts and separate repairs instead of presenting them as clean reruns.

The independent physical-readout check preserves an original symbolic
representation failure and its separate domain-justified repair. Later
correspondence checks clarify the dynamical gravity readout and dimensionful
density notation without changing or rerunning the equations. Canonical
source/runner correspondence is checked separately from these derivations.

That correspondence identified two missed damaged-runner controls in the
first canonical version: a changed z exponent in W and a cubic theta factor
in B both passed. Direct bindings of the implemented B,C,W to the original
action and its potential gradients were added, and the W jet now uses its
actual derivatives. The original 83/0 output and missed controls are retained;
they are not presented as covering those previously unchecked alterations.

The mixed constant-ratio candidate is rejected within its exact ansatz. The
x-only limiting radiation branch survives this local mathematical test. The
action and potential choice, k and nu, absolute scales, initial state,
finite history, fluid content and actual gravity/environment matching remain
inputs or gaps. No newly assumed selector is counted as a derivation. A future
empirical study must establish calibration and regime, infer parameters from
declared calibration data, then freeze them before testing other observations.
