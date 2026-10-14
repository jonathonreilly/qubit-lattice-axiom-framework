# Finite radiation history and its physical past boundary

**Date:** 2026-10-14
**Status:** proposed_retained
**Claim type:** bounded_theorem
**Actual current surface status:** conditional-support
**Primary runner:** [exponential_scalar_finite_history_check.py](../scripts/exponential_scalar_finite_history_check.py)

Local attraction in normalized variables does not by itself select an
initial state or a nonsingular history. For the supplied revised scalar
action, this note derives the finite-amplitude correction to the alternative
radiation state, proves a conditional local past-convergent curve, and shows
that its physical curvature diverges at a finite past proper time. The action,
past boundary condition, actual state and observed calibration remain inputs.
No observations are fitted or reserved data tested.

## Supplied action, domain and density convention

Use the complete action and coefficients in the companion
[alternative radiation note](EXPONENTIAL_SCALAR_ALTERNATIVE_RADIATION_BOUNDED_THEOREM_NOTE_2026-10-14.md):
Q integral sqrt(-gE)[R_E/2-K_AB partial(phi^A)partial(phi^B)-2Hv^2 U]
+S_m[C gE,matter], with phi=(u,x,y), Q=Q0(1+k)>0, Hv>0,
0<k<kc=3-2sqrt(2), and fixed finite nu>0. Restrict matter to ideal
trace-free radiation in a spatially flat classical homogeneous geometry,
and choose the expanding Einstein sheet H_E>0. These assumptions are not
derived from framework primitives or observations.

For clarity, a=(1-k)(1+3k)/4, alpha=sqrt(a), s=(1+k)/[k(1-3k)],
E=exp(2alpha u), F=1+sE, J=1+(1-3a)sE, d=2(1+k)/3, and

    K=diag(J/F^2,(1+s)4k/[9F(1+d(x^2+y^2))],
                    (1+s)k/[3F(1+d(x^2+y^2))]),
    C=(1+s)E/F,
    U=U0+(k/2)x^2 exp(-lambda_x u)+(k/3)y^2 exp(-lambda_y u),
    U0=3/2+3s(E-1)^2/(2F^2)+nu(1+s)u^2/(2F^2),
    lambda_x=(1-k)/alpha, lambda_y=(1+k)/alpha.

Let rho_phys be dimensionful physical radiation density and
y_b^2=rho_phys/(2Q Hv^2). If rho_J=rho_phys/rho_unit is instead
dimensionless, then y_b^2=Rstar rho_J with Rstar=rho_unit/(2Q Hv^2).
The clocks are dt_J=sqrt(C)dt_E and N_J=N+log sqrt(C), N=log a_E.
Radiation conservation is rho_phys proportional to exp(-4N_J).

The already derived alternative limiting state is

    E_x=(1-3k)/[3(1+k)], u_x=log(E_x)/(2alpha),
    C_x=(1-k)/(1+k), b=2k(1-k)/[(1+k)(1-3k)],
    H0=2C_x^2/[3(1-2b)], W_x=b H0,
    beta_x^2=2W_x exp(lambda_x u_x)/k.

The domain makes 0<b<1/2 and H0,W_x,beta_x positive. Each fixed k has
its own local neighborhood; no uniform endpoint limit is asserted.

## Full finite-amplitude equations

In either x-sign chart put eta=x^-2, ell=log|x|, w=y/x,
theta=2alpha(u-u_x), z=log(|x|/(beta_x y_b)), p=theta', q=ell'.
Primes denote d/dN. Pullback of the original three-field kinetic metric is

    A dtheta^2+Binf/(1+w^2+eta/d)
                         [dell^2+(3/4)(dw+w dell)^2],
    A=J/(4aF^2), Binf=(1+s)2k/[3(1+k)F].               (1)

Its determinant in(theta,ell,w) is(3/4)A[Binf/(1+w^2+eta/d)]^2.
The reflection y->-y makes w=w'=0 invariant. On this plane set

    B=Binf/(1+eta/d), l=2/(1+3k), Z=beta_x^2 exp(2z),
    Wq=W_x exp(2z-l theta), W=Wq+eta Z U0,
    T=A p^2+B q^2, Hbar=H_E^2/(Hv^2 y_b^2)=2(C^2+W)/(3-T),
    h=H_E'/H_E=-4C^2/(3Hbar)-T.

Use H_E=+Hv*y_b*sqrt(Hbar), with y_b>0. This sheet fixes the physical
time orientation of the theorem. Since N_J'=1+p/(2F)>0 locally, H_J>0
also. On the contracting sheet the same N->-infinity limit would instead
be a physical future boundary; no expanding-state selector is derived here.

The physical ell derivative at fixed u and radiation is
(partial_z-2eta partial_eta)W=2Wq. The complete radial force therefore
contains2Wq, not2W. Also Gamma^ell_ell,ell=eta/(d+eta). Direct variation gives

    theta'=p, z'=q+2+p/F, eta'=-2q eta,
    p'=-(3+h)p-A_theta p^2/(2A)+B_theta q^2/(2A)
                            +(lWq-eta Z U0_theta)/(A Hbar),
    q'=-(3+h)q-(B_theta/B)pq-eta q^2/(d+eta)-2Wq/(B Hbar). (2)

The clock term p/F in z' is fixed by physical radiation conservation.
Inserting the full potential in the old limiting radial force while omitting
the eta connection would give different, incorrect finite equations.

## New direction and conditional local past convergence

The eta=0 equilibrium is(theta,z,p,q)=(0,0,0,-2). Let M be its four-state
Jacobian on the invariant plane. The companion note derives

    det(lambda I-M)=(lambda^2+lambda)^2+Sx(lambda^2+lambda)+Px,
    Sx=4(5-7k-21k^2+7k^3)/[(1+k)(1-3k)(1+3k)],
    Px=64k(1-k)^2(1-6k+k^2)/[(1+k)^2(1-3k)^2(1+3k)].

There Sx>46/5,0<Px/Sx<80/69, and all four roots have negative real
parts. The two transverse ratio roots solve lambda^2+lambda+Omega^2=0,
Omega^2=-2/3+(16/9)exp[-(lambda_y-lambda_x)u_x]>10/9; they too are stable.
These are previously checked fixed-k limiting results, not new full-history
convergence claims.

At the equilibrium let A0=A(0), r=1/(1+3k), D0=3-4b and

    v0=beta_x^2 U0(u_x)/H0, v1=beta_x^2 U0_theta(u_x)/H0,
    j=(2v0-4b/d)/D0.

Differentiating the full constraint and forces gives, for
X=(theta,z,p,q+2),

    X'=M X+f eta+O((|X|+|eta|)^2),
    f=(0,0,[2rb(1/d-j)-v1]/A0,4v0-6/d),
    eta'=4eta+O(eta |X|).                            (3)

The new eigenvalue is+4. Reflection forbids linear forcing of the odd normal
variables by eta or a plane variable. The full seven-state extension thus
has six stable directions and one unstable direction, a hyperbolic saddle.

This extension is smooth in an open neighborhood through eta=0: (1) stays
positive,3-T stays positive, the normalized full potential is smooth, and
C^2+W and N_J'=1+p/(2F) remain positive after restricting the neighborhood.
Mathematically negative eta is allowed in that extension only; it is not a
physical squared inverse field. The local smooth unstable-manifold theorem
then gives a one-dimensional manifold tangent to the+4 eigenspace. Its eta
component is nonzero, so it is a smooth graph over eta. Uniqueness and the
invariant plane put its germ inside w=w'=0.

Its positive-eta half is one local orbit up to N translation in each x-sign
chart. This uniqueness concerns orbits that remain near and converge to this
point sufficiently far backward. It does not assert a global no-return
property, global continuation, or selection of this past point by the action
or observations. Requiring that particular past limit is still a boundary
premise. Finite-duration histories need not lie on this curve.

The tangent is X=h1 eta+O(eta^2), where

    (4I-M)h1=f, det(4I-M)=400+20Sx+Px>584.            (4)

The tangent is unique. Source-level smoothness and hyperbolicity supply
existence; finite numerical tangent residuals are consistency controls, not
a validated global construction of the manifold. The theorem invoked is the
local smooth unstable-manifold theorem, obtained by time reversal of the
stable-manifold theorem; its hypotheses are checked above.

## Finite proper time and diverging physical curvature

Along the positive branch eta'=4eta+O(eta^2), theta,z,p=O(eta), and
C=C_x[1+O(eta)]. Since y_b^2=1/(beta_x^2 eta exp(2z)),

    H_E^2=Hv^2 H0/(beta_x^2 eta)[1+O(eta)],
    rho_phys=2Q Hv^2/(beta_x^2 eta)[1+O(eta)],
    Delta t_E=beta_x sqrt(eta)/(2Hv sqrt(H0))[1+O(eta)],
    Delta t_J=beta_x sqrt(C_x eta)/(2Hv sqrt(H0))[1+O(eta)]. (5)

Both past proper times are finite. With L=N_J'=1+p/(2F),
H_J=H_E L/sqrt(C), and direct clock conversion gives

    h_J=(dH_J/dt_J)/H_J^2=[h+L'/L-(L-1)]/L -> -2.

In the physical flat FLRW metric, contraction of the orthonormal Riemann
components gives

    K_J=12H_J^4[1+(1+h_J)^2] ~24H_J^4
                                      ~3/[2(Delta t_J)^4]. (6)

It diverges, as does the Einstein-frame contraction. The leading Ricci
coefficient6(2+h_frame) cancels; that cancellation does not make the physical
curvature bounded. Normalized past convergence therefore supplies neither
a nonsingular physical history nor justification for arbitrarily high
curvature use of this classical action.

The companion weak-k mode has lambda_slow=-(16/5)k+O(k^2). In the constant
limiting model, one e-fold of slow-mode decay takes Delta N=5/(16k)+O(1).
Combining eta'~4eta gives a formal log density contrast5/(4k)+O(1).
The expression exp[5/(4k)] denotes only its leading exponent. It is not a
relative-error approximation, observed erasure bound, or proof that a
finite-amplitude trajectory tracks the limiting model for O(1/k) e-folds.

## Evidence, limits and recovery

The discovery checker directly derived the finite metric and physical force,
differentiated the constrained equations, contracted FLRW curvature, and
checked12 synthetic(k,nu) combinations at70-digit arithmetic. Its67/0
conditions and four actual damaged controls are preserved. A separate
independent action reconstruction passed167/0 with six actual damaged
equations rejected. It includes original-coordinate finite-field controls
at24 points and a source-specific proof of the manifold hypotheses.
The independent checker identified the dimensionless/dimensionful density
ambiguity in the first source; the preserved second source clarified it,
with15/0 narrow correspondence checks and no altered dynamics.

The canonical primary runner checks132 conditions, including separate
complete-action coefficient and gradient bindings, generic lowered equations,
the same finite-flow constructor used in its numerical derivatives, and the
physical clock conversion. Its execution does not replace or relabel the
earlier independent results. Discovery, correction, numerical controls and
review records are stored in the accompanying recovery archive; the archive's
README identifies final source correspondence, exact scope and extraction
verification.

The load-bearing inputs still include the complete action, k,nu,Q0,Hv,
ideal radiation, flat homogeneous geometry and the selected past-limit rule.
Neither actual initial conditions, bounded physical past, absolute scales,
measured gravity nor a TOE follows. Matter transitions and mixed histories
are separate later work. No formal audit verdict or merge is supplied here.
