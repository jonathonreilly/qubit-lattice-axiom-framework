# Radiation saddle, weak coupling and the remaining initial state

**Date:** 2026-10-14
**Status:** proposed_retained
**Claim type:** bounded_theorem
**Actual current surface status:** conditional-support
**Primary runner:** [exponential_scalar_radiation_selection_check.py](../scripts/exponential_scalar_radiation_selection_check.py)

Observed present-day properties do not by themselves supply a primordial
scalar state. This conditional calculation asks whether the candidate's
ideal radiation solution can erase that freedom, and how an applicable
bound on the same coupling would limit its rate. The complete action and
initial state remain supplied; no actual observation likelihood is fitted.
The solution attracts within x=x'=0 but is a saddle when the transverse
scalar direction is restored.

## Complete supplied action


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


The action, universal matter metric, fields, k,nu,Q0,Hv and matter content
remain explicit model inputs. Framework unit/isotropy/realized-state premises
do not select them. All previous comparators and histories are exposed
development context. No independent observational test occurs here.

At the constant vacuum, F0=1+s, J0=a/k, K_u0=J0/(1+s)^2, and
d_u log sqrt(C)|0=sqrt(a)/(1+s). Thus the canonical vacuum coupling obeys
alpha_m^2=[d_u log sqrt(C)]^2/K_u0=k. Applying an observational bound to k
still requires its actual source, range, frame and environment hypotheses.

## Deriving the finite-k reduced equations

Take fixed 0<k<1/3, ideal trace-free radiation, x=x'=0 and the large positive
y regime, at bounded u and z=log(y/y_b). Let Rstar=1/(2Q Hv^2), y_b^2=Rstar rho_r, with rho_r the physical
Jordan-frame radiation density, and rho_r proportional to exp(-4N_J). Hold k fixed before taking this large-y limit; exchanging these limits is not assumed. Terms from the
constant and nu potential divided by radiation density vanish in this
reduction. It does not hold across the actual thermal/mass transitions or
late vacuum domination. Primes below mean d/dN, N=log a_E.

With ell=log y, p=u', q=ell', the remaining field metric and potential are

    A(u)=J/F^2, B(u)=(1+s)k/[2(1+k)F],
    W(u,z)=U_rad/y_b^2=(k/3) exp(2z-lambda_y u),
    C=(1+s)E/F, alpha_B=alpha/F,
    T=A p^2+B q^2,
    Hbar=H_E^2/(Hv^2 y_b^2)=2(C^2+W)/(3-T),
    h=H_E'/H_E=-4C^2/(3 Hbar)-T.

Here E=exp(2 alpha u), F=1+sE, J=1+(1-3a)sE and
lambda_y=4 alpha s/(1+s). A and B here are metric coefficients; the conformal square root is sqrt(C).
For d=2(1+k)/3, the exact ell kinetic coefficient at x=0 is
B_full=B*d*y^2/(1+d*y^2). Dividing the full potential and its gradients by
y_b^2 and substituting y=y_b exp(z) gives W, -lambda_y W and 2W for
U, partial_u U at fixed physical y, and partial_ell U respectively.
The discarded finite terms vanish on fixed bounded (u,z) sets for fixed k,nu.
The x=0 plane is invariant: partial_x U=partial_x K_uu=partial_x K_yy=0
there and the kinetic metric is diagonal. This is a restriction on initial
data, not a proof of attraction from arbitrary x.

The Einstein constraint is (3-T)Hbar=2(C^2+W). Radiation supplies
rho_E=C^2 rho_r and P_E=rho_E/3, giving the displayed h. Its scalar trace
force vanishes. With ell=log y, the lowered scalar equations are

    A[p'+(3+h)p]+(A_u/2)p^2-(B_u/2)q^2-lambda_y W/Hbar=0,
    B[q'+(3+h)q]+B_u p q+2W/Hbar=0.

Finally N_J=N+log sqrt(C), so (log y_b)'=-2(1+alpha_B p).
These identities give

    u'=p,
    z'=q+2+2 alpha_B p,
    p'=-(3+h)p-(A_u/(2A))p^2+(B_u/(2A))q^2
        +lambda_y W/(A Hbar),
    q'=-(3+h)q-(B_u/B)pq-2W/(B Hbar).                 (1)

In particular, the 2 alpha_B p term in z' must not be omitted: y_b scales
with the physical scale factor, not the Einstein scale factor. The
potential derivative in p' holds physical y fixed before expressing its
ratio to y_b^2. Equation (1) is smooth in the open positive chart T<3.

The ideal fixed point is (u,z,p,q)=(0,0,0,-2). There C=1,
B=k/[2(1+k)], T=2k/(1+k)<3, Hbar=2(1+k)/3 and h=-2.
This note analyzes local attraction, not a global basin or uniqueness of
all radiation solutions.

## Exact spectrum and a local nonlinear consequence

Differentiating all of (1), including Hbar, h, and z', gives the characteristic
polynomial

    P_lambda=(lambda^2+lambda)^2+S(lambda^2+lambda)+P,
    D=(1+k)(1-3k)^2,
    n=-3k^3+10k^2+k+4,
    S=4n/D, P=16k/[(1+k)(1-3k)].                     (2)

This polynomial is an exact consequence of the reduced flow, not a fit to
numerical eigenvalues. Write

    r_small=2P/[S+sqrt(S^2-4P)],
    r_large=(S+sqrt(S^2-4P))/2.

For 0<k<1/3, n>4, D>0, and n-4D=k(21-2k-39k^2)>16k>0, so S>16.
Also P/S=4k(1-3k)/n<1/12. These inequalities imply
S^2-4P>0, 0<r_small<1/6<1/4, and r_large>16-1/6>1/4.
The four eigenvalues are therefore

    (-1+sqrt(1-4 r_small))/2,
    (-1-sqrt(1-4 r_small))/2,
    (-1+i sqrt(4 r_large-1))/2,
    (-1-i sqrt(4 r_large-1))/2.                       (3)

Their real parts are strictly negative for every finite k in this open
range. Since (1) is smooth near the fixed point, it is locally
asymptotically stable for each fixed k. To make the nonlinear inference
explicit: if M is its Jacobian, the integral
P_L=integral_0^infinity exp(M^T t) exp(M t) dt is positive definite and
M^T P_L+P_L M=-I. Writing (1) in displaced coordinates as w'=Mw+O(|w|^2)
gives d(w^T P_L w)/dN=-|w|^2+O(|w|^3)<0 in a sufficiently small
neighborhood. No uniform neighborhood as k->0, finite capture time or
global attraction has been established.

## A slowly selected state is not an observed initial-state derivation

The eigenvalue closest to zero has the expansion

    lambda_slow=-k+(35/16)k^2+(869/128)k^3+O(k^4).     (4)

The analytic root exists near k=0 because the zero eigenvalue of (2) at
k=0 is simple. Thus the radiation-only linear relaxation time in Einstein
e-folds diverges as 1/k. The other real eigenvalue tends to -1 and the
oscillating pair tends to (-1+-3i sqrt(7))/2, as follows directly from P_lambda at k=0. Already at the linearized slow-mode level,
the long-time and weak-coupling limits do not commute. The local nonlinear
stability argument does not establish a common basin for exchanging
limits of nonlinear solutions.

Compute the exact rate at the already used candidate values k=1e-6,1e-5,
.001,.01,.1,.3,.32. An illustrative 24 Einstein e-fold evolution of the
linear slow eigenmode is exp(24 lambda_slow), not a simulation of the
actual thermal history. At weak k this interval is much shorter than
the relaxation time. It cannot justify erasing the initial-state freedom.

The action-to-flow reduction and spectrum have also been checked independently. The full
observed state, an allowed basin, parameter k, the matter content and the
action remain open inputs. Finite-k local asymptotic stability retires
neither the initial-state assumption nor the cosmological-to-local bridge.

## All-coupling rate bound and conditional observation link

Take the hypotheses of the finite-k radiation reduction above: the supplied action,
fixed 0<k<1/3, ideal trace-free large-positive-y radiation at bounded u,z,
x=x'=0, and perturbations in the local neighborhood of its ideal fixed point.
Time N is the Einstein e-fold variable. The real slow eigenvalue lambda_s lies
in (-1/2,0), and its exact characteristic polynomial is

    P(lambda)=(lambda^2+lambda)^2+S(lambda^2+lambda)+P0,
    D=(1+k)(1-3k)^2,
    n=-3k^3+10k^2+k+4,
    S=4n/D, P0=16k/[(1+k)(1-3k)].

The checked factorization is P(lambda)=(lambda^2+lambda+r_s)
(lambda^2+lambda+r_l), with 0<r_s<1/6 and r_l>16-1/6.
Direct substitution now yields the exact identity

    P(-k)=-k^2 L(k)/D,
    L(k)=35+43k-66k^2+14k^3+15k^4-9k^5.

On 0<k<1/3,

    L(k)>35-66/9-9/243=746/27>0.

Thus P(-k)<0. The large-root factor at lambda=-k is positive, because
k^2-k>=-1/4 and r_l>16-1/6. Therefore r_s<k-k^2. The function t-t^2
is strictly increasing on 0<t<1/2. Since t=-lambda_s is the small positive
solution of t-t^2=r_s and k<1/3, it follows that

    0<-lambda_s<k,     tau_relax=1/(-lambda_s)>1/k.       (5)

This is an all-k inequality within the open candidate range, not a truncated
small-k expansion. For a nonzero component along the linear slow eigenmode,
its amplitude ratio over a prescribed DeltaN>0 is exp(lambda_s DeltaN).
Consequently, if an APPLICABLE independent physical constraint establishes
0<k<=b<1/3, then

    exp(lambda_s DeltaN)>exp(-b DeltaN),
    tau_relax>1/b.                                      (6)

The local vacuum bridge yields alpha_m^2=k only in the stipulated vacuum and
when its actual experimental range/source/readout assumptions are applicable.
A constraint on another environment's coupling g is not automatically a bound
on k. No Cassini timing model, cosmic-to-local matching, fixed initial amplitude
or nonlinear/global relaxation bound is supplied by this argument.

For orientation only, insert the already exposed development proxy b=1/79999
used earlier in the campaign, and DeltaN=24. Equation (6) then gives relaxation
longer than 79999 Einstein e-folds and slow-mode amplitude retention above
exp(-24/79999). This is not a new extraction or confidence interval from an
experiment. The exact conditional formula (6), with a bound established by an
appropriate forward model, is the scientific result.

A preassigned DeltaN is not a derived cosmic duration, and a pure slow-mode
calculation is not a thermal-history integration. Initial data can have zero
slow-mode projection. Actual massive/thermal traces, transitions, finite-y
corrections, nonlinear excursions and other possible attractors can change the
history. The result rules out claiming rapid linear erasure from this specific
ideal attractor under weak k; it does not rule out every initial-state mechanism.
The initial state remains an open input of the current candidate.

## Restoring the transverse field: an unstable normal direction

The restriction x=x'=0 has not been selected by the local stability proof.
To test it, let v=x/y and ell=log y, with y large and positive. The complete
supplied action gives the limiting field metric and potential

    ds_field^2=A du^2+B/(1+v^2)[(4/3)(dv+v d ell)^2+d ell^2],
    W=exp(2z)[(k/2)v^2 exp(-lambda_x u)+(k/3)exp(-lambda_y u)].

This follows by x=v*y and dx=y(dv+v d ell), keeping the mixed kinetic term.
The previous solution has v=v'=0. Reflection x->-x ensures that the normal
linear block decouples from (u,z,p,q). Perturbations of Hbar, h and the even
scalar stress have no first-order normal part.

At the radiation point, the full physical x equation to first normal order is

    x''+(3+h-2q)x'+[(3/4)q^2+Hv^2 k/(K_xx H_E^2)]x=0,
    K_xx=2k/[3(1+k)y^2], q=-2, h=-2,
    Hv^2 k/(K_xx H_E^2)=9/4.

The mixed connection Gamma^x_xy=-1/y and normal connection
Gamma^x_yy=(3/4)x/y^2 give x''+5x'+(21/4)x=0. Its roots are -3/2 and -7/2.
Since y scales as exp(-2N), this is equivalently

    v''+v'-(3/4)v=0,   lambda_normal=+1/2,-3/2.        (7)

The transformed metric provides a direct check: Gamma^v_ell_ell=-v/4+O(v^3),
so its q^2 term contributes -v. The mixed inverse-metric potential force
contributes +v/4; dropping its off-diagonal term gives the wrong result.
The friction term is v'. Thus the unstable root holds for every fixed k in
the stated open interval. It is not inferred from numerical trajectories.

Decay of x by itself does not restore attraction: at u=0 the ratio of the
x and y potential contributions is (3/2)v^2, which grows along the positive
normal mode. The all-field autonomous large-y fixed point has five stable
and one unstable linear directions. It is a hyperbolic saddle. Its local
stable manifold has dimension five; convergence while remaining in a local
neighborhood requires data on that manifold. The invariant x=x'=0 plane is
one subset, not necessarily the entire manifold. Canceling the linear growing
coefficient is only its tangent condition; no nonlinear manifold equation or
probability measure on initial data is supplied.

This rejects generic local attraction to this particular full-field radiation
point as a derivation of the imposed initial-state restriction. It leaves the
four-dimensional stable result and conditional slow-mode bound intact on
their stated plane. It does not rule out other fixed points, finite-y effects,
thermal traces, different histories or other selection mechanisms.

## Executed evidence and surviving assumptions

The primary runner differentiates the supplied action, takes its large-y
limits, checks the lowered equations and clock conversion, computes the full
Jacobian and characteristic polynomial, verifies the exact sign and series
identities, and compares seven 80-digit matrix spectra with the analytic
roots. It also reconstructs the transverse metric, connections and normal
Jacobian from the action and checks the physical-field versus ratio clocks. These are exposed mathematical development examples. They establish
no empirical likelihood, confidence level or independent observational test.

Independent checks derive the equations from the full action, use different
phase variables for the Jacobian, compare 24 off-orbit full-action/reduced
flows, and certify slow roots at six rational k values by Sturm counts and
rational bisection. The independent rate proof also uses the sign change
P(-k)<0<P(0) and the unique root in (-1/2,0). Its original JSON serialization
failure is preserved alongside the correction; no source equation changed.
The earlier scope correction restricted the noncommuting-limits statement to
the linear slow factor. Both original sources and receipts are recoverable.

A finite-chart example with k=1/10 and E=106360/7 has local coupling
g=a/J=1/100000<1/79999<k. This is a pointwise algebraic example, not a
constructed physical environment. It demonstrates why a non-vacuum g limit
cannot simply be substituted for k. A pure fast eigenmode likewise violates
any attempted extension of the slow-component retention inequality to every
state norm. The mathematical controls expose those two overclaims directly.

The action, parameter values, positive chart, invariant plane, radiation
idealization, initial slow amplitude and observational bridge remain explicit
assumptions. The fixed-k local attraction within x=0 follows from these premises. The
transverse saddle excludes generic attraction to this radiation point. The
calculation does not establish finite capture, a common nonlinear
basin as k tends to zero, full-action tracking through radiation dilution,
thermal transitions, a full past history, or selection of the observed state.
No framework primitive or proposed selector is counted as retiring those
imports. This result narrows what the current candidate can explain by itself.
