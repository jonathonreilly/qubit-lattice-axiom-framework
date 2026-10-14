# Deriving material response and a finite-history scalar inverse

Status: conditional support; specified local material, calibrated synthetic inverse.
Claim type: bounded_theorem. Scientific author: /root.
Primary runner: `scripts/exponential_scalar_dynamical_inverse_check.py`.

Particle conservation and a supplied compressional law replace an arbitrary
constant density response with a frequency-dependent response and its own initial
mode. The undivided two-mode equations then give a finite-window inverse that
eliminates unknown amplitudes and phases when measured features have full rank.
Neither construction selects the material, background, state or fundamental action.

Premises are the [complete supplied action](EXPONENTIAL_SCALAR_FUTURE_CONFINEMENT_BOUNDED_THEOREM_NOTE_2026-10-13.md),
the [local force normalization](EXPONENTIAL_SCALAR_LOCAL_RESPONSE_BOUNDED_THEOREM_NOTE_2026-10-13.md),
and the [stationary density/action inverse](EXPONENTIAL_SCALAR_DENSITY_INVERSE_BOUNDED_THEOREM_NOTE_2026-10-14.md).
Actual source controls, a valid scale/time window, and the measurement calibrations
remain open. These are conditional derivations, with no empirical fit or independent
observational test in this block.

## Deriving the density constraint from local material dynamics

Personally derived by /root. This is a conditional local nonrelativistic response
calculation, not a self-consistent cosmological or laboratory background. It asks
whether the prescribed p in the preceding action inverse follows from moving
matter. A compressional constitutive law and its sound speed remain inputs.
All later numerical examples will be exposed synthetic development controls.

### 1. Declared limit and independent variables

Use a frozen stationary scalar chi0 and density rhoE=A0 rhoStar0. The scalar
kinetic coefficient is -Q(partial chi)^2, beta=d ln A/d chi at the point, q=beta^2,
and M^2>0 is the fixed-particle Einstein mass squared. Define cR=rhoE/(2Q)>0.
Write X=delta chi and delta=delta nE/nE0=delta rhoStar/rhoStar0. Both are varied;
the scalar does not stipulate the density variation. A0 is constant in this
linearized patch, so all inverse lengths/frequencies transform by 1/A0 into
physical units and cR/A0^2=4 pi Gbare rhoJ in natural units.

We retain the leading nonrelativistic rest-mass source and scalar force. Inertial
mass density is rhoE, the prescribed linear compressional law is deltaP/rhoE=
v_s^2 delta, and 0<=v_s^2<<1. Contributions of pressure/internal energy to the
scalar trace and inertia, their conformal dependence, dissipative transport,
boundary supports, inhomogeneity and expansion are not included. The formulas
are exact for the specified quadratic model and leading order for such matter,
not an exact relativistic barotropic-fluid theorem. A measured sound speed would
be a calibration input; it is not derived from the scalar action.

Continuity and the particle force from -m_J integral A dsE give

 delta_dot+div v=0,
 v_dot=-v_s^2 grad delta-beta grad X-grad Psi.

Scalar variation at fixed particle data before linearization gives

 X_ddot-laplacian X+M^2 X=-cR beta delta.                 (1)

No p has been supplied. The coefficient M^2 includes the A second derivative in
the fixed-particle effective potential. In particular, it is not the p=3 mass.

Initially set Psi=0 (externally frozen metric), so the density equation is

 delta_ddot-v_s^2 laplacian delta=beta laplacian X.       (2)

A quadratic longitudinal displacement model verifies reciprocity. If delta=
-div xi, its kinetic and potential densities are

 L2=Q[X_dot^2-(grad X)^2-M^2 X^2]
       +rhoE |xi_dot|^2/2-rhoE v_s^2(div xi)^2/2
       +rhoE beta X div xi.

It is the rest-particle cross term plus the supplied compressional modulus;
variation gives (1),(2). It does not derive the modulus or neglect corrections
by pretending matter was pressureless at all orders.

### 2. Frequency-dependent density response and coupled poles

For wave number k>0 and Fourier convention exp(i k.x-i omega t), define x=k^2,
y=omega^2, a=x+M^2, b=v_s^2 x and g=cR q. The coupled equations are

 (a-y)X+cR beta delta=0,
 beta x X+(b-y)delta=0.

When b-y is nonzero, the driven density response with zero independent fluid
homogeneous perturbation is

 delta=-beta x X/(b-y),
 p_eff(omega,k):=delta ln rhoStar/delta ln A=-x/(b-y).    (3)

The literal quotient also requires a nonzero driven beta X. At beta=0 the
sectors decouple and this quotient is undefined, rather than a measured p.

For the stable bare acoustic resolvent, the retarded boundary prescription
replaces omega by omega+i0. A full coupled system with an exponentially growing
pole does not have a convergent real-frequency retarded transform. Its causal
initial-value response must instead use a Laplace/Bromwich contour to the right
of all growing poles, or the finite-time fundamental solution. This qualification
also applies when b<0 after the Jeans replacement below. The algebraic harmonic
determinant remains valid. For an initial-value problem the independent fluid
homogeneous solution must be added; division by b-y is not valid at the bare
acoustic pole. Therefore a local constant p is not
inferred from particle conservation. At high frequency p_eff tends to zero;
at zero frequency and v_s^2>0 it is -1/v_s^2, not +3. A constant physical-density
constraint p=3 needs separately controlled matter/geometry or a reservoir.
For dust the zero-frequency division is singular rather than a finite static
response. These statements apply to this freely moving specified material.

The scalar-only response has the frequency-dependent term

 a-y-g x/(b-y),

but the coupled determinant, valid also near b-y=0, is

 (a-y)(b-y)-g x=0.                                     (4)

A real canonical change delta=sqrt(x/cR) D makes the matrix in (X,D) symmetric,
with off-diagonal beta sqrt(cR x). Its two squared frequencies are

 y_+,-=(a+b +/- sqrt((a-b)^2+4g x))/2.                  (5)

For v_s^2>0, both are positive precisely when v_s^2(x+M^2)>g.
Equality gives a neutral mode; below it one coupled mode grows despite M^2>0.
With v_s=0 and g>0 there is a negative mode at each finite nonzero k; this is
scalar-mediated compression in a frozen patch, not proof of fast cosmological
instability. The growth rate gamma satisfies

 gamma^2=-v_s^2 x+g x/(x+M^2+gamma^2)<=g.

For a positive fixed-particle stationary branch, the previous identity supplies
M_J^2/g_J=2/B-3 with g_J=4 pi Gbare rhoJ q. Hence positivity of all k>0 modes in
this frozen-metric model is equivalent to

 B <= 2 v_s^2/(1+3v_s^2),                              (6)

where equality still has a positive frequency squared at each k>0, with the
smaller branch behaving as v_s^2 k^4/M^2 near k=0. In the strict case it
instead begins as (v_s^2-g/M^2) k^2. Both tend to zero as k tends to zero;
neither has a uniformly positive long-wave frequency gap. This uses 0<B<2/3, q>0 and finite masses; beta=0 is separate. It is a
leading nonrelativistic model criterion, not a measured material limit. The
all-k statement is a property of that ideal continuum: it establishes no actual
material/background scale window, and omitted NR corrections can shift a
near-neutral physical stability boundary.

### 3. Include leading tensor gravity without inventing a static universe

A uniform gravitating dust background in Minkowski space is not a solution of
the full field equations. To discuss subregion Jeans response one may retain
only the nonzero-k density perturbation in the leading Newtonian Poisson
constraint and subtract the homogeneous background. This local approximation
requires a domain/scale/time window compatible with the actual background; it
does not justify neglecting expansion at a Hubble-rate instability.

At a scalar stationary point V_E,chi=-rhoE beta. The linear rest-energy change
rhoE(delta+beta X) and scalar-potential change -rhoE beta X cancel in their X
parts. Thus, at this order and with scalar gradients quadratic,

 laplacian Psi=cR delta.

Pressure, metric-volume/time corrections and background curvature are beyond
this leading Newtonian patch. Then the density equation becomes

 delta_ddot+(v_s^2 x-cR)delta=-beta x X,

so (3)-(5) hold with b=v_s^2 x-cR. For M^2>0, v_s^2>0 there is one positive
threshold x_J at which a coupled frequency vanishes:

 v_s^2 x_J^2+[v_s^2 M^2-cR(1+q)]x_J-cR M^2=0,
 x_J=[cR(1+q)-v_s^2 M^2
       +sqrt([v_s^2 M^2-cR(1+q)]^2+4v_s^2 cR M^2)]/(2v_s^2).

The exact defining equation also gives

 cR/v_s^2 < x_J < cR(1+q)/v_s^2                       (7)

for q>0 and M^2>0; the limiting equalities require a decoupling or singular limit.
For x>x_J both frequencies are positive; below it one is negative. This model's
instability has

 gamma^2=cR-v_s^2 x+g x/(x+M^2+gamma^2)
           < cR(1+q) < (4/3)cR                       (8)

for the supplied candidate q<1/3, finite k and M^2>0. Thus the local growing
rate cannot become arbitrarily larger than the tensor-gravity free-fall rate
under these premises. If that rate is comparable to the real background's
expansion/curvature rate, this frozen-patch calculation alone cannot decide
cosmological growth. A pressure-free medium has no finite Jeans wave number;
setting v_s=0 in a formula that divides by v_s^2 is invalid.

### 4. What is eliminated, what remains, and source comparison

The arbitrary constant p is replaced by a derived dispersive response for a
specified free compressional medium, together with its independent initial mode.
It is not universally eliminated for an unspecified laboratory. Preparing a
particular stationary scalar branch, choosing the matter constitutive law,
providing boundaries/supports, selecting initial perturbations, and establishing
a measured scale window remain separate assumptions. The ideal Gbare and B
inverse inputs have still not been measured. No new observational rejection or
statistical confidence level follows from (6)-(8).

As a development-stage convention check, Bean, Flanagan and Trodden,
https://arxiv.org/pdf/0709.1128v2, give particle-number conservation and conformal
force in Eqs.(2.12)-(2.13), and discuss the local Jeans interpretation and limits
of an adiabatic reduction. The mapping is their canonical field phi=sqrt(2Q)chi,
Planck mass squared Q and alpha=ln A, so 2Q alpha_phi^2=q. Their separate dark
sector phenomenology and strong-coupling exclusions are not imported. The
present dispersion and source-control formulas are derived above, not claimed
to discover that known instability mechanism for the first time.

Before execution: independently derive the quadratic Euler-Lagrange system,
canonical symmetry and determinant; test the divided versus undivided pole;
verify roots, static/high-frequency limits, both stability domains, Jeans
threshold and growth ceiling; compare exact matrix exponentials with direct
linear ODE integration on frozen synthetic stable and unstable cases. Preserve
all profiles and failure records. Deliberately altered force sign, kinetic
normalization, scalar mass prescription and gravity sign must trigger failures.
No synthetic example will be used to tune a measured density or coupling.

## Finite-window density inverse without prescribed initial amplitudes

Personally derived by /root. Conditional inverse inside the frozen nonrelativistic scalar/material model of the preceding material-dynamics derivation. It is not a fitted experiment or a fundamental action selection. All constitutive, gravity, geometry, stationarity and approximation premises of that source remain.

### 1. Calibrated inputs and an undivided observable equation

For k>0, x=k^2, cR=rhoE/(2Q)>0, q=beta^2>0, M^2>0, sound-speed squared v_s^2>0 and gravity flag h=0 or1, put a=x+M^2, b=v_s^2 x-h cR, g=cR q. The coupled equations are

    X_ddot+a X=-cR beta delta,
    delta_ddot+b delta=-beta x X.

Delta is the particle-number contrast per frozen Einstein proper volume. The physical density contrast is delta-3 beta X. Because every constant linear combination of these states satisfies the same eliminant, either contrast is eligible in the frozen model. An instrument's varying geometry/readout factor, background or projection must be included before using this fact. Wavenumber, clock, sound speed and tensor coefficient cR are supplied calibrations.

Eliminating X without setting any initial or homogeneous mode to zero gives

    delta^(4)+C2 delta_ddot+C0 delta=0,
    C2=a+b, C0=ab-g x.                                  (1)

The same equation holds for X and a time-independent linear readout of both. This polynomial equation loses no acoustic pole. It is not asserted during cosmological rolling or for a dispersive constitutive law.

### 2. Weak finite-window inversion

Use duration T>0, tau=t/T in[0,1], and readout f(tau). Choose test functions psi_j whose psi,psi',psi'',psi''' vanish at both boundaries. Four or two integrations by parts give

    I4_j+u2 I2_j+u0 I0_j=0,
    Ir_j=integral_0^1 f(tau) psi_j^(r)(tau) d tau,
    u2=T^2 C2, u0=T^4 C0.                              (2)

No derivative of observed f or endpoint initial state is supplied. For two tests let D have rows (I2_j,I0_j), and z have entries -I4_j. If det D!=0, u=D^-1 z. The rank condition concerns actual readout features, not a guaranteed preparation. Then

    M^2=C2-(1+v_s^2)x+h cR,
    q=[(x+M^2)(v_s^2 x-h cR)-C0]/(cR x).                (3)

This requires calibrated nonzero cR x. It does not determine the sign of beta, which changes with scalar orientation. Negative inferred M^2 or q could reject this restricted model only with valid error and approximation bounds. No empirical value is inferred here.

A single exact normal-frequency readout obeys f''=-Omega^2 f in tau, so I2_j=-Omega^2 I0_j for every admissible test. D then has rank at most1 even with unlimited precision or more kernels. Both excitation and readout observability matter. A two-mode history can supply enough information without fitting its unknown phases/amplitudes; this is conditional on the measured rank, not a selected initial state.

### 3. Deterministic error certificate

Suppose |fhat-f|<=epsilon on the window, and Kr_j bounds integral |psi_j^(r)|. Then |Ihat_rj-I_rj|<=epsilon Kr_j. In infinity norm define

    d=epsilon max_j(K2_j+K0_j), e=epsilon max_j K4_j,
    eta=||Dhat^-1||_infinity d.

If Dhat is invertible and eta<1, the true D is invertible and

    ||uhat-u||_infinity
    <= ||Dhat^-1||_infinity (e+d||uhat||_infinity)/(1-eta). (4)

This follows from the Neumann inverse bound and D(u-uhat)=(z-zhat)+(Dhat-D)uhat. The uniform error, exact model and controlled integrals are premises. Instrument drift, finite sampling, quadrature and approximation errors need their own bounds before this describes an experiment. It is not a statistical confidence region or automatically informative.

For bound E in(4), with b,cR,x,T held at their exact calibrated values,

    |Mhat^2-M^2|<=E/T^2,
    |qhat-q|<=[|b|/T^2+1/T^4] E/(cR x).                 (5)

Calibration uncertainty must be propagated separately. For psi=P(tau)cos(w tau), P=tau^4(1-tau)^4, a conservative analytic kernel bound is

    Kr<=sum_(l=0)^r binomial(r,l)|w|^(r-l)
             sum_n |coefficient_n(P^(l))|/(n+1).       (6)

The triangle inequality, bounded sin/cos and integral tau^n=1/(n+1) prove it. For w=0 only l=r contributes. Floating displays of the symbolic envelope are not outward interval certificates.

### 4. Frozen synthetic protocol and empirical separation

Before execution freeze calibration k=8, T=3, cR=1, v_s^2=0.04, M^2=4, q=0.2, h=1 and kernels w=0,8pi. Use three distinct small two-mode amplitude/phase choices and an explicit single-mode failure. Reserve k=11 with new amplitudes as a synthetic prediction control: infer M^2,q at k=8, then check predicted coefficients at k=11. Do not tune the theory with that control. Preserve ill-conditioning or failed inverses if they occur.

Use exact identities, high-precision quadrature, separate double-precision Gaussian quadrature, and a bounded additive sinusoidal readout error. Actual altered integration sign, time scaling, gravity sign and mass prescription must trigger failures. Save full mock readout samples, features, inferred coefficients, conditioning, predicted residuals and failures. Neither calibration nor the reserved synthetic control is an independent empirical test. No density data or apparatus likelihood has been acquired.

## Validation and recovery

The canonical runner retains the exact checked proof bodies with only isolated
global/function renaming. It executes99 local-dynamics controls and126 weak-inverse
controls, preserving complete outputs and optional full profiles with `--profiles`.
Original synthetic profiles, failed first executions, their narrow numerical repairs,
20 causal-domain and8 long-wave controls, and actual altered-program probes are in
the [recovery archive](work_history/physics/revised-scalar-dynamical-inverse-20261014/README.txt).

Independent hand implementations use distinct matrices, states, kernels and moment
methods:119 local-response controls and200 finite-window inverse controls, with
seven actual altered-program probes for each. Their full reports, source bindings
and failures remain separate from author output. These counts are checks within
specified models, not separate experiments or formal audit grades.

The first dynamics execution93/6 exposed inadequate absolute resolution for tiny
ODE energies. The repaired execution99/0 retains its cases and acceptance threshold
while tightening integration accuracy. The first weak inverse123/3 preserved a
symbol-identity comparison error and high-derivative double-quadrature cancellation;
its repair126/0 retains the primary derivative-free inverse and uses known analytic
mock derivatives only in a separate synthetic quadrature control. Neither repair
licenses differentiating unknown experimental data. Full original programs, streams,
profiles and exact diffs are recoverable.

A two-mode state is not sufficient by itself: the actual readout or test functions
can annihilate a mode. Extra residual/prediction checks are needed to challenge the
model, and finite sampling, quadrature, solve error and uncertain calibrations require
their own budgets. The reserved wavenumber is a same-model synthetic prediction
control, not a held-out observation. Initial realization, environmental preparation,
constitutive law, absolute scales, and action selection remain unretired assumptions.
