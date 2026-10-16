# Relative coupling reconstruction from sampled clamped responses

Claim type: bounded_theorem

A finite pulse protocol reconstructs relative coupling functions and tests their
compatibility with a common potential. Each trial uses its own observed history;
no hidden initial state is assigned. A sampled calibration recurrence replaces
the choice of continuous oscillator frequencies. The result is conditional on
the response class and measurement contract below. All executable examples are
synthetic; no physical action or quantum outcome law is inferred from data here.

```yaml
target_claim_type: bounded_theorem
actual_current_surface_status: conditional-support
trace_class: upstream_support
target_claim_id: null
target_blocker_text: "focus on deriving the remaining assumptions rather than supplying them"
source_of_blocker_text: user_goal
reachability_to_target: supports
artifact_role: theorem
conditional_surface_status: "Relative coupling functions, a reciprocal-potential criterion and deterministic error bounds for one passive hidden coordinate under calibrated clamped pulses."
hypothetical_axiom_status: "The response equations are candidate-class conditions; no framework axiom is adopted."
admitted_observation_status: "No empirical input; published experiments motivate a future protocol and synthetic controls check mathematics."
claim_type_reason: "The mathematical inverse depends on a specified passive hidden response and physically registered source, coordinate and time."
audit_required_before_effective_retained: true
bare_retained_allowed: false
next_trace_action: "Identify an actual clamped source/coordinate channel and error budget; freeze calibration and shape reconstruction before reserved pulse tests."
```

## Exact target and proof obligations

**Target.** In the scalar clamped-response class defined below, a rank2 sampled
calibration and a nonzero centered pulse anchor determine normalized coupling
shapes, eliminate each run's arbitrary hidden preparation, and give a necessary
and sufficient shape/sign criterion for the stated positive constant-mass
potential completion, with deterministic propagation of certified errors.

| Obligation | Disposition |
|---|---|
| Constant-clamp affine oscillator equation | Derived directly from the class |
| Sampled recurrence and measured calibration | Derived by the characteristic polynomial and a two-by-two inverse |
| Six-sample same-run pulse difference | Derived by forward and backward recurrence |
| Pulse-end nonnegative response integral | Proved by a dissipating quadratic energy |
| Relative shapes and common-potential criterion | Derived by factorization and mixed derivatives |
| Force, calibration, ratio and shape error bounds | Derived by induced norms and triangle inequalities |
| Physical source/coordinate identification, pulse fidelity and model class | Supplied conditions requiring experimental justification |
| Continuous shape coverage, moving-coordinate dynamics and absolute scales | Open physical/inference work beyond this result |

The strongest missing physical step is a validated map from controlled physical
coordinates, conjugate force records and actuator changes to this single common
response model. This is not characterized as near closure. A future environmental
response calculation in the scalar program is the intended consumer, after that
map is established. No existing framework claim is promoted by this note.

## Observational motivation, prior art and inputs

Chen et al. report a mechanical 1:3 internal resonance, while their simplified
equation (1) uses a linearly coupled 1:1 surrogate. This motivates determining
coupling from controlled responses rather than selecting its power from a
resonance label. Their main text and equation were read; no experimental records
from that study enter this calculation. See
[Chen et al.](https://arxiv.org/html/1612.00490v3).

Nonlinear elimination and state-dependent memory are established subjects:
[Ayaz et al.](https://arxiv.org/abs/2202.01922) and
[Ge et al.](https://doi.org/10.1103/PhysRevLett.133.077301) provide relevant prior
art. Their abstracts were consulted; the Ayaz introduction was also inspected.
No proof or fluctuation-dissipation premise is imported from them. Exponential
recurrences, response factorization and mixed-derivative integrability are
standard tools. The calculation here combines them into the explicit pulse
protocol; it makes no broad literature novelty claim.

| Input | Role | Provenance | Physical obligation |
|---|---|---|---|
| One linear hidden coordinate, positive inertia/stiffness, nonnegative damping | Response class | Explicit candidate assumption | Test its applicability and residual modes |
| Arbitrary real C1 functions u,a,b on a connected interval | Coupling class | Theorem domain | Infer shapes on a justified domain; no polynomial is imposed |
| Registered q, conjugate source and sample interval | Measurement definition | Explicit observational contract | Independent calibration and error certificates |
| Piecewise constant pulse and unchanged coefficients within a trial | Intervention | Idealized protocol | Bound transition, drift and instrument errors |
| Rank2 calibration, positive p and nonzero anchor margins | Inverse conditions | Checked from calibration and response | Establish conditioning with uncertainty |
| Positive constant diagonal kinetic coefficients for potential completion | Restricted action class | Explicit conditional interpretation | Moving-coordinate dynamics and global stability remain to be established |

## Conditional response and observation contract

For q in a connected real interval I, the intervention prescribes q(t). On each
measured segment with q held at x, suppose

    F_x(t)=u(x)+a(x)w(t),
    tau*w''+gamma*w'+C*w=-b(q(t)),                    (1)

with tau,C>0, gamma>=0, and real C1 functions u,a,b. No relation between a and b
is imposed. Write Omega2=C/tau>0 and Gamma=gamma/tau>=0. The local moving-q force
need only reduce to u(x) on held segments, with no extra delayed force there.
The hidden equation has no impulsive q' or q'' coupling. The idealized pulse
edges are not force observations; actuator and readout settling require their
own physical accounting. Coefficients and readout are fixed within each trial
and shared over the ensemble of pulses being compared.

Each trial may start with arbitrary and unrelated w,w'. No equilibrium,
thermal distribution, reset or common hidden preparation is used. A common
positive force gain cancels from relative shapes and preserves the sign test.
Setting-dependent gains require separate calibration. The source must be the
force conjugate to the declared q coordinate for the action interpretation.

## Calibrate sampled dynamics without selecting continuous frequencies

On a constant-x interval, direct substitution gives

    F''+Gamma*F'+Omega2*F=c_x,
    c_x=Omega2*u(x)-a(x)b(x)/tau.                     (2)

Let Delta>0 be the calibrated sample spacing. If r1,r2 are the eigenvalues of
the homogeneous time-Delta map, define s=r1+r2 and p=r1*r2=exp(-Gamma*Delta)>0.
The affine augmented map has characteristic polynomial (z-1)(z^2-s*z+p).
Cayley-Hamilton therefore gives, including repeated poles,

    F[n+3]=(1+s)F[n+2]-(s+p)F[n+1]+p*F[n].            (3)

Differences d[n]=F[n+1]-F[n] obey d[n+2]=s*d[n+1]-p*d[n]. Two independent
rows [d[n+1],-d[n]] determine (s,p). The rows can come from different constant
calibration histories, with different states and offsets. The measured rank
and conditioning must be demonstrated; generic excitation is not silently
assumed. With five samples, H=d0*d2-d1^2 and, if H!=0,

    s=(d0*d3-d1*d2)/H, p=(d1*d3-d2^2)/H.              (4)

These formulas follow by solving the two-by-two system. Extra calibration
samples test the recurrence before its coefficients are frozen. A steady record
gives zero differences and no rank2 design. Continuous underdamped frequencies
omega_d and omega_d+2*pi/Delta can have the same s,p; the protocol uses the
sampled coefficients and leaves those continuous aliases unselected.

## Six settled samples reconstruct the pulse-end difference

Hold q=x for the samples at -2Delta,-Delta,0-minus. At time0 change to y; at
Delta return to x. Record settled forces F2,F3,F4 at 2Delta,3Delta,4Delta.
Using (3), the force at Delta in the continuation that kept q=x would be

    F_ref1=(1+s)F0-(s+p)F_minus1+p*F_minus2.            (5)

On the post-pulse constant-x segment the same recurrence, solved backward, gives

    F_actual1=[F4-(1+s)F3+(s+p)F2]/p.                  (6)

Here F_actual1 denotes the regular force just after returning to x, extrapolated
from settled samples, not a measured impulse. Define D(x,y)=F_actual1-F_ref1.
This reconstructs each trial's own hidden homogeneous continuation, so unknown
preparation cancels. Small positive p can greatly amplify measurement errors.

Let g solve g''+Gamma*g'+Omega2*g=0 with g(0)=0,g'(0)=1. The difference between
the actual hidden path and its constant-x continuation has zero initial state.
Variation of constants gives

    D(x,y)=-a(x)[b(y)-b(x)]*J/tau,
    J=integral_0^Delta g(v)dv.                        (7)

This also supplies the null-pulse identity D(x,x)=0.

## Pulse-end positivity without a Nyquist-branch choice

Put z(t)=1-Omega2*integral_0^t g(v)dv. Integrating the equation for g, or
differentiating and checking initial conditions, shows

    z''+Gamma*z'+Omega2*z=0, z(0)=1, z'(0)=0,
    d[(z'^2+Omega2*z^2)/2]/dt=-Gamma*z'^2<=0.

Consequently z(t)<=1 and J=(1-z(Delta))/Omega2>=0. For Gamma>0 and Delta>0,
nonzero initial acceleration gives strictly positive integrated dissipation,
hence J>0. For Gamma=0, J=[1-cos(sqrt(Omega2)*Delta)]/Omega2, with zeros at
complete periods. An exact nonzero pulse anchor already implies J!=0 within
(1), so its J is positive. No upper bound on continuous frequency was needed.

The statement is specific to the extrapolated pulse end. For example, an
undamped oscillator with Omega2=4, Delta=.35 has negative integral response at
the later time t=2. That explicit witness explains why a late raw force sample
is not substituted into (7). Active negative damping is outside (1).

## Infer relative coupling shapes and test a common potential

Choose a reference pulse value z0 and define

    E(x,y)=D(x,y)-D(x,z0)=-J*a(x)[b(y)-b(z0)]/tau.

For an anchor E0=E(r,y_star)!=0, define

    A(x)=E(x,y_star)/E0=a(x)/a(r),
    B(y)=E(r,y)/E0=[b(y)-b(z0)]/[b(y_star)-b(z0)].     (8)

Thus E=E0*A*B. Its two-by-two minors vanish. Conversely, that factorization
plus D(x,x)=0 gives D(x,y)=E0*A(x)[B(y)-B(x)] on the stated response surface.
The converse concerns this pulse surface, not a unique realization of every
history. A finite grid only checks its sampled values; multiple hidden modes
with proportional coupling can share a factorized surface. A continuum claim
requires continuum regularity and coverage, not an implicit interpolation law.

Within the constant positive diagonal kinetic class, multiply the hidden
equation by a positive constant lambda. The force pair has a common potential
exactly when a(q)=lambda*b'(q): necessity follows by equality of mixed
derivatives, and sufficiency follows by constructing U'=u and

    V(q,w)=U(q)+lambda*C*w^2/2+lambda*b(q)*w.           (9)

If the moving q equation additionally is m*q''+u+a*w=f, m>0, the kinetic
terms m*q'^2/2 and lambda*tau*w'^2/2 give that conservative core. Rayleigh
function lambda*gamma*w'^2/2 accounts for the stated hidden damping. Clamped
measurements alone do not establish the moving-q kinetic law or global
potential stability.

The equivalent observable shape/sign conditions are

    B(y)-B(x)=kappa*integral_x^y A(v)dv for every x,y in I,
    E0*kappa<0,                                      (10)

for one constant kappa!=0. To see the equivalence, put a_r=a(r) and
d=b(y_star)-b(z0). Then B'=a_r*A/(lambda*d), so kappa=a_r/(lambda*d).
Conversely B'=kappa*A gives a=lambda*b' with lambda=a_r/(d*kappa).
Since E0=-J*a_r*d/tau, E0*kappa=-J*a_r^2/(tau*lambda), fixing its sign.
Zeros of A are covered: B' must vanish there. Normalization fixes
kappa=1/integral_z0^y_star A when the integral is nonzero, rather than choosing
a different multiplier at each coordinate.

The explicit functions a=1+q, b=q+q^3/3 on [0,1] give factorized responses
whose a/b' varies; they are a comparison case with a nonzero shape residual.
A negative multiplier gives the same shape equality with the opposite sign.
These are specific controls, not an exhaustion of velocity couplings,
non-diagonal kinetic forms, feedback or larger hidden realizations.

## Certified measurement and calibration errors

For fixed exact s,p and uniform bounds epsilon_pre,epsilon_post on the three
pre and three post samples, the six linear weights in (5)-(6) give

    |error D| <= L_pre*epsilon_pre+L_post*epsilon_post,
    L_pre=|1+s|+|s+p|+p,
    L_post=[1+|1+s|+|s+p|]/p.                        (11)

For calibration, write X*theta=y, theta=(s,p), with measured X_hat,y_hat and
induced infinity-norm errors epsilon_X,epsilon_y. If
eta=||X_hat^-1||_infinity*epsilon_X<1, then

    ||theta-theta_hat||_infinity <=
      ||X_hat^-1||_infinity/(1-eta)
       *[epsilon_y+epsilon_X*||theta_hat||_infinity], (12)

where theta_hat=X_hat^-1*y_hat. Subtract the two equations and apply the
Neumann inverse bound to obtain (12). If every original calibration force
sample has error <=epsilon_cal, epsilon_X=4*epsilon_cal and
epsilon_y=2*epsilon_cal suffice. Shared differences may be correlated; the
bound does not assume independent noise. Formula (12) is for the square
rank2 selection, not an arbitrary least-squares solver.

For |delta s|,|delta p|<=epsilon_theta, true pulse samples bounded by M,
and the entire connecting coefficient segment satisfying p>=p_min>0, |s|<=S,

    |coefficient error D| <= M*epsilon_theta
                        *[2/p_min+4+(2+2*S)/p_min^2]. (13)

Indeed the s derivative is (F2-F3)/p-F0+F_minus1; the p derivative is
-[F4-(1+s)F3+s*F2]/p^2+F_minus1-F_minus2. Their absolute bounds and a
mean-value integral give (13). Add (11) evaluated at estimated s,p for sample
errors; M in (13) bounds the true samples. The p margin must hold under the
full uncertainty region, not merely at a fitted value.

If R_hat=N_hat/E0_hat, with errors epsilon_N,epsilon_0 and
|E0_hat|>epsilon_0, subtracting fractions gives

    |R-R_hat| <= [epsilon_N+|R_hat|*epsilon_0]
                                  /[|E0_hat|-epsilon_0].        (14)

This propagates the pulse errors to A and B. For a frozen kappa estimate and
shape bounds, the error in the residual of the integral relation (10) is at most

    epsilon_B(x)+epsilon_B(y)+|kappa_hat|*integral_S epsilon_A
      +epsilon_kappa*(integral_S |A_hat|+integral_S epsilon_A),   (15)

where S=[min(x,y),max(x,y)] uses increasing integration limits. This follows
by adding and subtracting kappa_hat*integral A and applying the triangle
inequality. The signal integral in (10) is oriented; error integrals are not.
Quadrature, kappa inference, drift, timing and pulse-shape errors need separate
certificates. These deterministic bounds are not confidence levels.

For a smoothed actual pulse that returns to x before post observations, the
extra force at a specified post time is bounded by
|a(x)|/tau times the integral of |g(t-s)|*|b(q_actual)-b(q_rectangle)|.
This follows from the same zero-initial-state convolution. Using a Lipschitz
constant for b requires that constant to be independently justified. The six
sample extrapolation must propagate such errors at its actual observation
times. Neither actuator fidelity nor a Lipschitz constant is derived here.

## Test separation and interpretation

Calibration histories identify and check one uncertainty region for s,p.
Development pulses reconstruct A,B and establish anchor and quadrature margins.
Freeze these choices, selection rules and error budgets before examining
reserved histories, coordinate pairs and additional pulse intervals. The
executable reserved examples are synthetic, not independent empirical tests.
An observed residual must be compared with all applicable model and instrument
errors before attributing it to a physical failure.

Selected coupling polynomials, assigned hidden initial states and chosen
continuous frequency aliases are unnecessary for this conditional protocol.
The inferred shapes would still be measured reconstructions. Absolute hidden
normalization, U, physical scales, the action class and its scalar-gravity or
quantum-record interpretation remain open. No new primitive or no-go against
alternative dynamics is proposed.

## Computation and review record

Primary runner: `scripts/sampled_coupling_inverse.py`, importing
`scripts/sampled_coupling_math.py`. Run through the repository cache envelope
with its declared120second timeout. The note and imported helper are declared
integrity inputs. No external scientific data file is read.

The exploratory first sampled derivation omitted s*F2 in the p derivative.
Its failed symbolic control exposed the error; equation (13) includes the
corrected term and bound. The earlier shape-error bound was clarified to use
unoriented error integrals. Original failures are preserved in the research
checkpoint; this standalone note supplies the corrected derivation in full.

Focused independent source checks and scratch mutations are recorded in the
paired output directory and milestone review history. They are not formal
audit verdicts. Shared integrated landing pipeline, strict lint and changed
evidence validation remain required before any later landing. No helper
registry edit is required because the primary normally imports its helper.
