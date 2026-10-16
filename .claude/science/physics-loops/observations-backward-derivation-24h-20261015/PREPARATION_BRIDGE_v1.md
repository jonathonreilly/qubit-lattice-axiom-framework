# Preparation removal by observed force-history coordinates

Status: exploratory conditional-support; root author, parent campaign continuation.
This is a measurement/preparation bridge for PR9637, not a derivation of its
physical action class or a new empirical result. Standard affine-state and
quadratic-output interpolation underlies the construction. It remains
commits-only until a substantive physical test or additional scientific result.

## Observation-first question and premises

Can calibrated moving-force records determine the response that would have
started at equilibrium without actually resetting the hidden state, waiting
for it to decay, or inserting its unknown initial value? Assume the same
quadratic one-hidden-coordinate candidate as PR9637, retaining k(x):

    T=M xdot^2/2+k xdot wdot+tau wdot^2/2,
    V=U+B w+C w^2/2, D=d xdot^2/2+nu xdot wdot+gamma wdot^2/2.

Coefficients are real smooth functions of x only. tau,C>0, M tau-k^2>0,
gamma>0 and d gamma-nu^2>=0. At the starting clamp x0 require an observable
underdamped mode with pole lambda=-Gamma/2+i omega, omega>0,
Gamma=gamma/tau, O=C/tau and n=G+nu lambda+k lambda^2!=0,
G=B'+C'w0, w0=-B/C. No externally forced hidden channel is allowed.

Each repetition has the same measured prescribed x(t) and common physical
coefficients; arbitrary hidden preparations may differ. Before its drive,
each repetition supplies a calibrated clamped-force prefix at x0. Its six
exponential components can be separated with an independent pole/phase/time
calibration and certified errors. A finite prefix with an ill-conditioned
design or a hidden fundamental zero does not satisfy this premise. Common
input, constant model and calibrated readout are experimentally testable
obligations, not deductions from interpolation.

No measured data enter the present calculation. PREPARATION_BRIDGE_PLAN_v1.json
fixes the synthetic model, histories, reserved preparations and tolerances
before generating outputs.

## 1. Why subtracting a decay baseline does not restore a rest response

Direct Euler-Lagrange variation gives the full moving equations

    tau wddot+(tau' xdot+gamma)wdot+Cw
       =-k xddot-k' xdot^2-B-nu xdot,                    (1)
    R=M xddot+M' xdot^2/2+k wddot-tau' wdot^2/2
       +U'+B'w+C'w^2/2+d xdot+nu wdot.                  (2)

The k' xdot wdot terms cancel in the visible equation; k' xdot^2
remains in the hidden equation. These terms must not be dropped by treating
an environmentally varying kinetic matrix as constant.

At x=x0 let wbar=w0+z(t), z=c exp(lambda t)+c* exp(lambda* t).
For x=x0+epsilon xi, w=wbar+epsilon eta, evaluate all coefficients at x0.
The exact first variation is

    tau etaddot+gamma etadot+C eta
       =-k xiddot-(nu+tau' zdot)xidot
        -(G+C'z+gamma' zdot+tau' zddot)xi,              (3)

    delta R=M xiddot+d xidot
      +[V_xx(x0,wbar)-tau'' zdot^2/2
                        +nu' zdot+k' zddot]xi
      +(G+C'z)eta+(nu-tau' zdot)etadot+k etaddot.       (4)

Even after subtracting the unperturbed Rbar(t), this response generally
depends on z and zdot. The linear response is time varying. A matched
baseline subtraction alone does not justify inserting the rest dynamic
stiffness. When c=0 these formulas reduce to the reciprocal rest response
with numerator G+nu s+k s^2, recovering the parent calculation.

## 2. Exact finite-drive dependence on preparation

For a fixed prescribed x(t), equation1 is an affine linear ODE in the two
hidden state variables. With initial deviation eta0=(z(0),zdot(0)), its solution
is y(t)=y_ref(t)+Phi(t)eta0, where y_ref starts from (w0(x0),0).
Existence/uniqueness on the observed finite interval and tau bounded away
from zero suffice. Equation2, after replacing wddot through equation1,
is a polynomial of degree at most two in y. Therefore, pointwise in time,

    R[x,eta0](t)=a0[x](t)+a1[x](t) eta01+a2[x](t) eta02
       +a3[x](t) eta01^2+a4[x](t) eta01 eta02
       +a5[x](t) eta02^2.                              (5)

The coefficients depend on the full coordinate history, but not on the
initial hidden preparation. This is exact for finite drives, not a small
drive or short-time truncation. It is a consequence of the supplied class;
observing a few successful examples cannot establish the class.

At the initial clamp the fundamental force coefficient is f=n c.
The real map from c to eta0=(2 Re c,2 Re(lambda c)) is invertible since
omega>0. Multiplication by the unknown nonzero n is also invertible.
Thus (Re f,Im f) is a measured homogeneous linear coordinate for preparation.
Its origin means rest without knowing n or w0. Only the fundamental is
used as a coordinate; nonlinear DC or second-harmonic power is not.

For an arbitrary fixed nonzero common scaling of f, let a=Re f, b=Im f and

    q(f)=(1,a,b,a^2,ab,b^2)^T.
    R[x,f](t)=q(f)^T alpha[x](t).                       (6)

The polynomial coefficients need not be identified to recover alpha0.

## 3. Rest-start response from an observable interpolation design

Collect N repetitions of one prescribed drive and their individually measured
prefix coordinates f_j. Let Q have columns q(f_j) and e0=(1,0,0,0,0,0)^T.
If real weights u satisfy

    Q u=e0,                                             (7)

then directly from equation6,

    sum_j u_j R[x,f_j](t)=alpha0[x](t)=R[x,0](t).        (8)

No hidden preparation is selected or supplied. The weights use measured
prefix coordinates only, not the candidate's coefficient functions, n or
actual initial states. At least one feasible moment representation is needed.
Six full-rank preparation columns are sufficient, but not necessary:
three distinct amplitudes on a line through the origin can also suffice.
More generally feasibility is e0 in the column space of Q. Equivalently every
quadratic polynomial vanishing on the sampled preparations must vanish at
the origin; this follows from the orthogonal-complement characterization of
a matrix column space.

If every preparation is nonzero, nonnegative normalized weights cannot work:
equation7 implies sum u_j |f_j|^2=0, which contradicts u_j>=0 and sum u_j=1.
The construction is a signed combination of measured force records. It does
not physically prepare a zero-energy state, assign negative probabilities or
synthesize all unknown observables.

Changing only phases at a fixed nonzero |f| also fails even with signed weights:
sum u_j |f_j|^2=|f|^2 sum u_j=|f|^2. This proves that phase cycling at one
amplitude cannot remove the general quadratic preparation term. Amplitude
variation or a directly observed zero is required for this broad class.
A six-point fit alone supplies no class check because it can interpolate six
arbitrary outputs. Additional preparations must be reserved to test equation6.

## 4. Response extraction with unmatched preparations

For each of the drives x_plus=x0+epsilon xi and x_minus=x0-epsilon xi,
form equation8 using its own arbitrary preparation ensemble and its own
measured weights. The ensembles need not share a single actual initial state.
Their centered difference estimates the rest linear response K[xi].

If R[x0+epsilon xi,0](t) is three times differentiable in epsilon with a
uniform third derivative bound B3(t) on [-|epsilon|,|epsilon|], then

    |(R_plus_zero-R_minus_zero)/(2epsilon)-K[xi]|
        <=epsilon^2 B3/6.                              (9)

This is Taylor's theorem. A pole/residue obtained from such responses still
needs its own finite-band and statistical/deterministic certificates.
Equation9 does not infer B3 from a finite set of epsilon values.

The method exchanges an unobserved reset/rest assumption for measured
prefix information, a feasible well-conditioned design, common drives and
the exact linear-hidden/quadratic-output class. It does not derive the initial
state of the universe or eliminate all physical preparation assumptions.

## 5. Deterministic feature and readout error bounds

For a square six-column design, suppose measured Qhat is invertible and
||Q-Qhat||_2<=eta. Let A=||Qhat^-1||_2, uhat=Qhat^-1 e0 and A eta<1.
The resolvent identity or Neumann-series bound gives

    ||u-uhat||_2 <= A eta ||uhat||_2/(1-A eta) = e_u.     (10)

For pointwise force errors |Rhat_j-R_j|<=e_Rj,

    |uhat^T Rhat-R[x,0]|
        <=sum_j |uhat_j| e_Rj + e_u ||R||_2.            (11)

Use ||R||_2<=||Rhat||_2+||e_R||_2 if only measured forces are bounded.
No independence of errors or preparations is assumed. Failed margins require
withholding a certified estimate; a pseudoinverse with a tiny singular value
does not restore the missing certificate.

A direct Frobenius bound for eta follows from measured a_j,b_j and radii
e_aj,e_bj. Each column error is bounded componentwise by

    0, e_a, e_b, 2|ahat|e_a+e_a^2,
    |ahat|e_b+|bhat|e_a+e_a e_b, 2|bhat|e_b+e_b^2.

Take the Euclidean norm of all these radii. Pole, clock and prefix extraction
errors must be propagated into e_a,e_b. For a known pole and prefix design H,
a least-squares coefficient error is bounded by ||H^+||_2 times the force-error
2-norm; model/pole errors add separately. Rank alone supplies no small error.

If the two synthesized forces have certified errors E_plus,E_minus,
add (E_plus+E_minus)/(2|epsilon|) to equation9. This exposes the practical
tradeoff: reducing drive amplitude improves Taylor truncation while amplifying
preparation/readout uncertainty. Input-history mismatch and actuator model
discrepancy must be included independently.

## Prior art and delivery scope

Berkane, Theodosis, Hamel and Dimarogonas, *State Estimation for Linear Systems
with Quadratic Outputs*, arXiv:2312.10684v1, describe known finite-dimensional
lifting of quadratic measurements of linear dynamics. The inspected portions
are the abstract/introduction and displayed quadratic-closure and lifting
equations12and20-22, not the complete appendices or an independent proof of
their observer theorem: https://arxiv.org/html/2312.10684v1.
That work is background; equations1-11are derived here. No novelty is claimed
for polynomial interpolation, state superposition or quadratic lifting.

The useful campaign contribution is exposing a measured replacement for the
specific equilibrium-preparation import in PR9637, its signed-weight/noise cost,
and the fixed-amplitude failure. Physical common-input reproducibility and
calibrated prefix/force data remain unsatisfied. This support block should not
be promoted as a new physical theory or an additional milestone merely because
its noiseless simulation succeeds.
