# Independent multi-mode derivation before author exposure

For this unit only MODE_INVERSE_NEUTRAL_CONTRACT_v1.json has been read.
Earlier action and response work is acknowledged context. No new author
plan, derivation, code or result has been opened. The derivation and planned
controls below are frozen before implementing or executing the controls.
All statements concern full linear perturbation equations, not nonlinear
finite-amplitude solutions or observational validation.

## Conventions and equations directly from the action

Use Einstein Newtonian gauge, with Fourier Laplacian -k^2:

    ds_E^2=-(1+2U)dt^2+a_E^2(1-2U) dX^2.

The equality of Einstein potentials follows from the nonzero-k traceless
Einstein equation: canonical scalar and pressureless dust have no linear
anisotropic stress. Write v=phi_dot, rho for the conserved bare dust rest
density, r=A rho, alpha=A_phi/A, and delta=delta rho/rho in this gauge.
Define the Einstein dust covariant velocity potential by u_i=partial_i v_d.
The original background equations are

    3M^2 H^2=v^2/2+V+r,
    -2M^2 Hdot=v^2+r,
    vdot+3Hv+V_phi+rho A_phi=0,
    rhodot=-3Hrho.

The original scalar, dust and Einstein linear equations in these conventions
are

    delta phiddot+3H delta phidot+(k^2/a_E^2+mu)delta phi
      =4v Udot-2S U-rho A_phi delta,
    mu=V_phiphi+rho A_phiphi, S=V_phi+rho A_phi,             (1)

    deltadot=3Udot+(k^2/a_E^2)v_d,
    v_ddot+alpha v v_d=-U-alpha delta phi,                  (2)

    Udot+HU=(v delta phi-r v_d)/(2M^2),                     (3)
    2[k^2 U/a_E^2+3H(Udot+HU)]
      =-[v delta phidot-v^2 U+V_phi delta phi
          +r(delta+alpha delta phi)]/M^2,                 (4)
    Uddot+4HUdot+(2Hdot+3H^2)U
      =[v delta phidot-v^2 U-V_phi delta phi]/(2M^2).       (5)

Here v_ddot in (2) means the first time derivative of the variable v_d;
it is not a second derivative. In executable controls it will be named
d(v_d)/dt to avoid that notation ambiguity.

These signs can be obtained without a response ansatz. Current conservation
uses sqrt(-g)rho u^0=a_E^3 rho(1+delta-3U). The covariant particle force is
u^nu nabla_nu u_i=-alpha(partial_i delta phi+v u_i), giving (2).
For the scalar, the first-order wave operator is

    delta(Box phi)=2U(vdot+3Hv)+4v Udot
                  -delta phiddot-3H delta phidot-k^2 delta phi/a_E^2.

Subtract the perturbation of V_phi+rho A_phi and use the background scalar
equation to obtain (1); derivatives defining mu hold bare rho fixed.
The scalar energy and pressure perturbations are respectively
v delta phidot-v^2 U+V_phi delta phi and
v delta phidot-v^2 U-V_phi delta phi; dust energy is r(delta+alpha delta phi).
The mixed Einstein components give (3)-(5). Independent controls will
compute their linearized geometry to check these signs.

## Matter-time observables and two recoverable background combinations

Use tau as background matter proper time, d tau=A dt, and the supplied
common spatial normalization for a_J=A a_E. Put K_i=k_i^2/a_J^2. A convention
such as a_J(tau_*)=1 must be accompanied by the corresponding registered
wave numbers. If the physical combination K_i is not registered, an extra
spatial-scale calibration must be retained.

From the independently supplied potentials define

    U_i=(PsiJ_i+PhiJ_i)/2, W_i=(PsiJ_i-PhiJ_i)/2.

With x=phi'/M, b=M alpha and y_i=delta phi_i/M, conformal transformation gives
W_i=b y_i. On a regular chart b nonzero and x nonzero, define

    q=bx=A'/A, g=x/b, u=h-q, x^2=qg>0,
    s=r/(M^2 A^2)=-2h'+2q'-2hq+2q^2-qg>0.               (6)

The source-free trace relation obtained from (5) is

    d_i=a U_i'+c U_i+e W_i'+f W_i,                       (7)
    d_i=2U_i''+8hU_i'+(4h'+6h^2)U_i,

    a=6q,
    c=4q'+8hq-2q^2-qg,
    e=g,
    f=g'+3(h-q)g-2h'+2q'-2hq+2q^2.                      (8)

In particular there is no explicit K_i in this necessary relation.
To derive it, convert (5) to matter time and use
x y_i'=g W_i'-g(b'/b)W_i and
V_phi/(M A^2)=-x'-(3h-2q)x-b s.
The b'/b terms cancel to the displayed coefficients.

Stack the four columns (U_i',U_i,W_i',W_i). If their rank is four on an open
chart, the real common coefficient vector is uniquely determined. For
complex Fourier data, real and imaginary parts may be stacked; reality of
the recovered coefficients remains a test. Set q=a/6 and g=e and require
both remaining formulas in (8), as well as every additional mode row.
A rank-deficient chart does not by itself prove non-identifiability; other
equations or more modes could supply information. Rank four is a sufficient,
checkable chart hypothesis, not a preferred initial-mode assumption.

## Full compatibility test and reconstruction

The trace fit alone is not sufficient. After solving (7), require qg>0,
s>0 and background dust transport

    s'=(2q-3h)s.                                        (9)

Choose a constant orientation sign sigma and set

    x=sigma sqrt(qg), b=q/x, y_i=W_i/b,
    F=-x'-(3h-2q)x,
    kappa=[F'+2qF+3b u s]/x
          =-x''/x-3h x'/x-3h'+2q'-6hq+4q^2+3u s/g.     (10)

The lower-derivative curvature formula is justified only after (9):
Friedmann, Raychaudhuri and dust transport recover the original background
scalar equation, so F=S/(M A^2). It is not an inserted pole or free potential
curvature. For A0>0 and phi0, reconstruct

    A=A0 exp(int q d tau), phi=phi0+M int x d tau,
    a_E=a_J/A, r=M^2 A^2s, rho=r/A,
    V=M^2 A^2[3u^2-x^2/2-s].                            (11)

For each supplied mode define the matter covariant velocity potential
V_i=A v_di and the bare-density contrast from the metric constraints:

    V_i=[x y_i-2(U_i'+uU_i)]/s,
    delta_i=-[2K_i U_i+6u(U_i'+uU_i)
              +x y_i'-x^2 U_i+F y_i]/s.                (12)

These formulas enforce the momentum and Hamiltonian constraints; the
Hamiltonian simplification uses V_phi/(M A^2)=F-b s.
The physical Jordan contrast is deltaJ_i=delta_i-3W_i.

Retain, rather than assume, the remaining full equations:

    V_i'=-U_i-W_i,                                     (13)
    delta_i'=3U_i'+K_i V_i,                            (14)
    y_i''+(3h-2q)y_i'+(K_i+kappa)y_i
       -4xU_i'+2F U_i+b s delta_i=0.                    (15)

The Jordan version of (14) is
deltaJ_i'=3PhiJ_i'+K_i V_i. Equation (13) follows from the particle action
in matter time. Given (9) and (12), (7) is equivalent to (13); that redundancy
does not eliminate (14) or (15). Bianchi identities make additional
relations redundant once the full system holds, but every displayed
residual will be checked for the exact fixtures.

Necessity follows from the original equations. Conversely, (6)-(15) construct
a common local action/background and perturbations satisfying the original
scalar, dust and all scalar Einstein equations: zero anisotropic stress,
both constraints, trace pressure, and the original scalar/dust evolution.
This is a complete compatibility test on the regular chart, not a claim
that any full-rank potential data are physically realizable.

For a convenient sufficient classical regularity, take h in C3 and all
potential functions in C4, with the rank nonzero on the chart. Then q,g
are C2 and the derivatives in (8)-(15) exist. These conditions need not be
minimal. The supplied wave-number normalization gives K_i'=-2hK_i.
No division by a vanishing rank determinant, b, x, qg or s is licensed.

The two choices of sigma reverse x,b,y and reflect the canonical field,
leaving observable potentials and kappa unchanged. A0 remains continuous:
A,V,r,rho rescale as lambda,lambda^2,lambda^2,lambda while tau, h,
U,W,q,g,b,kappa, delta and V_i remain fixed. With fixed a_J normalization,
rho_* rescales as lambda^-2. Field origin and off-chart extensions are
also undetermined. Independent density/Planck calibration could fix A0.
The ideal metric modes alone do not do so.

## Full-equation rank witness with distinct wave numbers

Use the exact Einstein background in fixed reference units

    M=1, H_E=1/t, phi=ln t, A=t,
    r=t^-2, rho=t^-3, V=3/(2t^2),
    tau=t^2/2, a_J=2tau.

Thus h=1/tau, b=1, x=q=g=1/(2tau), s=1/(4tau^2),
u=1/(2tau), F=-1/(2tau^2), kappa=7/(4tau^2).
These values are forward truth, not inputs to the inverse coefficient solve.

For D=tau d/dtau and K=L/tau^2, the trace and scalar equations after
constraint reconstruction reduce to

    (8D^2+12D+3)U-(2D+3)y=0,
    (4D^2+2D+4L+9)y-(20D+8L+9)U=0.                     (16)

For any 0<m(m+1)<3/8 choose

    U=tau^m, W=y=Y(m)tau^m,
    Y(m)=(8m^2+12m+3)/(2m+3),
    L(m)=m(m+1)[8m(m+1)+9]/[3-8m(m+1)]>0,
    k^2=4L.

The characteristic determinant is

    4[8z^2+(8L+9)z-3L], z=m(m+1).

The remaining original-equation variables are

    V_i=(2Y-8m-4)tau^(m+1),
    delta_i=[-(8L+5)-12m+(2-2m)Y]tau^m.                 (17)

They satisfy both dust equations, both metric constraints, the trace and
scalar equation. Choose the four distinct rational exponents

    m=1/8, 1/6, 1/5, 1/4.

They give distinct positive wave numbers and four legitimate full linear
modes. At tau=1 the response matrix has rows (m,1,mY,Y). Its determinant is

    96 product_{i<j}(m_j-m_i) / product_i(2m_i+3),        (18)

which is strictly positive in that ordering. At general tau it is multiplied
by tau^(sum m_i-2), so rank four persists. Independent execution will check
this expression, all original residuals, and recover the coefficient vector
(3/tau,5/(4tau^2),1/(2tau),3/(4tau^2)) directly from the ideal data.
It will then reconstruct b and kappa without taking either as an inverse input.

An arbitrarily small common amplitude epsilon preserves rank and all
linear equations. On any bounded open interval such as (1/2,2), choose
epsilon small enough for the perturbations and density contrasts to remain
small. This asserts exact first-order consistency, not a finite-amplitude
nonlinear solution or an empirical mode selection.

## Necessary-only counterexample and exceptional obstruction

Keep exactly those four potential histories and h but replace each supplied
L_i by L_i+1. The same full-rank trace fit and physical background still pass,
because (7) contains no K_i. Yet after the constraints are reconstructed,
the scalar residual changes by

    (Y_i-2)tau^(m_i-2),

and bare dust-continuity residual by

    (4-2Y_i)tau^(m_i-1).

They are nonzero for the chosen modes. This gives an explicit ideal input
set accepted by the necessary elimination but rejected by the complete
compatibility test. It is not claimed to be physical forward data.

There is no unconditional global inverse. For example set A=1, b=0,
phi=0, V(phi)=mu0 phi^2/2 with arbitrary mu0>0, and take a dust background

    h=2/(3tau), s=4/(3tau^2), a_J=tau^(2/3).

Choose scalar perturbations y=0. For any k nonzero,

    U=constant, W=0, V_i=-tau U,
    delta_i=-[2+(3/2)k^2 tau^(2/3)]U

satisfy the full original linear equations for every mu0. Thus the same
registered matter potentials and background admit arbitrary positive
kappa=mu0 in different potentials, even with A fixed. The regular inverse
chart fails here because b=x=0 and its slip columns vanish. This is an
explicit physical linear-mode obstruction, not just a low-rank heuristic.
Isolated coupling zeros, scalar turning points, missing mode excitation and
zero-density charts require separate treatment; none are classified by
dividing the regular formulas.

## Frozen executable-control plan

The independent program will check linearized Einstein geometry and the
scalar wave operator from metric expansion; original current/particle-force
transformations; the trace coefficient elimination; the exact regular
background; the distinct-k power modes and all full constraints/evolution;
the determinant formula and data-only recovery; the wrong-K counterexample;
normalization/orientation; and the mass-blind stationary scalar family.
It will use bounded bytecode-disabled execution and retain any actual
failure. Shared symbolic software does not count as independent-CAS evidence.
No observations, survey summaries, empirical arrays or author code enter.
