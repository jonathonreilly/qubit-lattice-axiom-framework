# Removing the transport boundary for a fixed scalar background

Root-authored candidate derivation, frozen before its controls. It addresses
the explicit boundary function in METRIC_REDSHIFT_TRANSPORT_DERIVATION_v1.md.
It neither derives the canonical action class nor selects an action from
records. No new empirical input is introduced.

## Assumptions and target

Fix one compatible smooth background of the canonical one-scalar, universal
conformal dust action from the preceding checked inverse. Work on an open
spacetime product chart in matter proper time tau, observer-centered radius
r>0 and an angular patch, with a>0, positive dimensionless matter density
R>0 and b,x both nonzero. The repeated-cone strip contains such local product
charts even when it contains no coeval volume of the whole survey. All
derivatives below are at fixed spatial coordinate or fixed tau as indicated.

Use the registered, corrected radial redshift field Rz=-Psi+v_r and lensing
Weyl field P. Their input obligations are unchanged: distance and clock
registration, the null-time correction, calibrated full metric propagation,
and the appropriate angular sector must be established. The tracer velocity
is that of the same pressureless, universally coupled matter in the equations.
No velocity bias or non-gravitational force is silently allowed.

Question: for this fixed background, may an arbitrary transport boundary
function still change J while leaving P and Rz unchanged and satisfying all
the linear scalar/dust/Einstein equations? The proposed answer below is no
on this regular chart, even locally, without assuming global boundary decay.
The uncalibrated/noisy problem and different compatible backgrounds are
different questions and remain open.

## Reduce the complete equations, retaining sources

Let w=delta phi/M, q=bx, ell=h-q, G=x/b, and

    Fbar=-x_tau-3hx+2qx,
    nu=-(b_tau/b)-Ft/G.

Ct and Ft are the fixed-background pressure-trace coefficients from
MODE_TRACE_ROOT_DERIVATION_v1.md, not freely fitted additions in this lemma.
The trace equation implies

    w_tau=nu w+S,
    S=[2 P_tau_tau+(8h-6q)P_tau+(4h_tau+6h^2-Ct)P]/x.       (C1)

The Hamiltonian constraint and scalar equation, without any quasistatic
approximation, imply

    w_tau_tau+3ell w_tau-a^-2 Delta w+(kappa-b Fbar)w=H_P,
    H_P=(6b ell+4x)P_tau-2b a^-2 Delta P
         +(6b ell^2-bx^2-2Fbar)P.                         (C2)

Combining C1 and C2 gives an elliptic identity at each time,

    (Delta-Lambda)w=g,
    Lambda=a^2[nu_tau+nu^2+3ell nu+kappa-b Fbar],
    g=a^2[S_tau+(nu+3ell)S-H_P].                         (C3)

The matter momentum constraint is

    Z=[xw-2(P_tau+ell P)]/R, Vv=Z/a.

Thus Rz=-P-bw+partial_r Vv yields

    (partial_r-C)w=f,
    C=a R b/x,
    f=(a R/x)(Rz+P)+(2/x)partial_r(P_tau+ell P).           (C4)

All C,Lambda are constant in space on the fixed homogeneous background. They
may vary in time. In particular C is nonzero on the specified chart.

## A local formula from spatial compatibility

On observer-centered spheres

    [Delta,partial_r]w=(2/r^2)partial_r w
                       +(2/r^3)Delta_Omega w.

Apply Delta-Lambda to C4 and partial_r-C to C3 and subtract. Eliminating
radial derivatives with C4 gives

    D w=N,
    D=Lambda-C^2-C/r,
    N=(r/2)[(Delta-Lambda)f-(partial_r-C)g]
       -g+C f+partial_r f+f/r.                          (C5)

Hence w=N/D wherever D is nonzero. This uses derivatives of registered
fields; it is not a stable estimator asserted for finite noisy samples.
It reconstructs the hidden boundary response from compatibility rather than
choosing its value. Arbitrary input records may fail C1-C4 or the remaining
original equations; this is a necessary reconstruction with full residual
tests, not an existence theorem for arbitrary P,Rz.

At an isolated positive radius with D=0, partial_r D=C/r^2 is nonzero. If a
smooth compatible solution exists then N=0 there and differentiating C5
gives w=(partial_r N)/(partial_r D) at that point. Nearby regular charts or
this limit determine it; a freely chosen boundary value is not introduced.
Noise and derivative amplification can be severe near that radius.

## Uniqueness without selecting a boundary or an initial scalar state

Take the difference of two linear solutions with the same background and
the same P and Rz on an open chart. Their difference obeys C3-C4 with f=g=0.
C5 gives D delta w=0. Since C!=0, D cannot vanish on any open radial interval.
It vanishes at at most one radius at each time. Therefore delta w=0 on the
complement, and continuity gives zero also at any exceptional radius.
Consequently delta J=b delta w=0; the momentum and Hamiltonian constraints
also fix the corresponding dust velocity potential and density perturbation
up to the already declared homogeneous velocity-potential convention.

An alternative direct proof uses C1 to separate delta w=S0(tau)Y(x). The
spatial equations then require partial_r Y=C Y and Delta Y=Lambda Y. On a
nonzero patch this forces constant C,Lambda in time and Y=exp(Cr)F(n). The
equation [(C^2-Lambda)r^2+2Cr]F+Delta_Omega F=0 for an open r interval implies
C=0, contradicting the regular chart. The commutator proof avoids requiring
that separation or any global boundary condition.

For ideal full-sky data one can apply the same reasoning separately to any
recovered ell,m sector, including ell>=2. Homogeneous coefficients, radial
derivatives and the angular Laplacian preserve that sector. This does not
repair missing modes, finite-mask leakage or the data-to-P,Rz calibration.

## Constructed full-equation check and limitations

In the previously checked A=exp(phi), V=(3/2)exp(-2phi), aE=t, phi=ln t,
rho=t^-3 background, a=2tau, h=1/tau, b=1, x=1/(2tau), R=1/(4tau^2),
kappa=7/(4tau^2), Fbar=-1/(2tau^2). Then

    nu=-3/(2tau), C=1, Lambda=15, D=14-1/r.

The prior purely kinematic transport-null family is not automatically a
field solution. The nonzero fixed-action lensing-null possibility would
need w proportional to exp(-3eta)Y(x), Delta Y=15Y and partial_r Y=Y. Those
conditions are incompatible on an open spherical annulus. No restriction to
real Fourier k or global normalizability is needed for this argument.

This retires a chosen transport boundary only conditional on a fixed
compatible background, the universal action and ideal registered records.
It does not prove action/background uniqueness, produce an observed scalar
detection, derive distance or clock calibration, establish derivative error
bounds, or determine the origin/probability of initial perturbations. It is
a local observability statement for the declared linear system. No priority
claim is made relative to characteristic or overdetermined inverse problems.

## Pre-execution control protocol

1. Check the spherical commutator and C5 for a completely arbitrary smooth
   w by defining f=w_r-Cw and g=Delta w-Lambda w; C,Lambda independent of r.
   Use both symbolic functions and polynomial angular fixtures.
2. Independently substitute the original fixed-background trace, Hamiltonian,
   momentum and scalar equations to verify C1-C4, including all signs and a.
3. Reuse the earlier original-equation power-mode family only as a known
   constructed witness. Use m=1/5 and a regular ell=2 radial Helmholtz field
   with k^2=728/75; verify source construction and w=N/D, including the
   compatible exceptional-radius limit r=1/14. Do not call this a data fit.
4. Nonzero omission witnesses: drop the spherical 2/r term, change the
   commutator sign, or choose an arbitrary kinematic transport null field
   and test the fixed-action scalar/trace identities.
5. Record all failures and preserve v1 before any correction. Seek a focused
   independent check before using this lemma downstream. No observations.
