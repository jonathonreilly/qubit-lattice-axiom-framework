# A sampled coupling test without selecting continuous hidden frequencies

**Claim type:** bounded_theorem. **Status:** conditional-support, author
derivation pending focused independent check. This extends the independently
checked `COUPLING_RECONSTRUCTION_v2.md`; its explicit class and physical
measurement limitations remain in force. No empirical dataset is used.

## The assumption being challenged

The first coupling inverse takes Omega2 and Gamma as calibrated inputs to
predict each run's unperturbed force. Can the same relative-coupling and
positive-interaction test be obtained from equally spaced observations without
choosing the continuous oscillator frequency or a Nyquist branch?

Yes within the same class, with an observable calibration recurrence and a
pulse of exactly one sampling interval. Only sampled dynamics are inferred.
Continuous frequencies remain ambiguous; the test below does not need them.
This is a constructive operational reduction, not a claim that sampling fixes
a microscopic timescale. Linear recurrences and exponential identification are
standard mathematics. The campaign contribution is their combination with the
pulse-end sign argument and the coupling inverse, not invention of those tools.

## 1. Infer a discrete recurrence from constant-coordinate observations

Let Delta>0 be the calibrated sample interval. Under a constant coordinate,
F obeys F''+Gamma F'+Omega2 F=c with Omega2>0 and Gamma>=0.
If r1,r2 are the two eigenvalues of the hidden homogeneous time-Delta map,
put s=r1+r2 and p=r1*r2. Both are real and p=exp(-Gamma Delta)>0.
The characteristic polynomial of the augmented affine state map is

    (z-1)(z^2-s*z+p).

Cayley-Hamilton therefore gives, including repeated poles,

    F[n+3] = (1+s)F[n+2] - (s+p)F[n+1] + p F[n].       (1)

Differences d[n]=F[n+1]-F[n] satisfy

    d[n+2] = s d[n+1] - p d[n].                        (2)

Two independent rows [d[n+1],-d[n]] determine (s,p). They may come from
one or several constant-coordinate calibration histories, with arbitrary and
different initial hidden states and offsets. There is no genericity premise:
the measured design must actually have rank2 with an adequate conditioning
margin. Steady or insufficiently excited records can fail it.

For five samples, form d0,...,d3 and H=d0*d2-d1^2. If H!=0,

    s=(d0*d3-d1*d2)/H,
    p=(d1*d3-d2^2)/H.                                (3)

Proof: solve the two-by-two system in (2); the determinant is H. Extra
calibration samples test the recurrence. A finite fit does not establish
that a continuous single-mode class is physically correct. The subsequent
coupling tests must use frozen calibrated coefficients, not refit each pulse.

## 2. Six settled samples eliminate the same-run baseline

Hold q=x for samples at -2Delta,-Delta,0-minus. At time0 set q=y; at
Delta return q=x. Let F2,F3,F4 be settled force samples at 2Delta,3Delta,
4Delta. No force measurement at either idealized jump is required.

The force that would have occurred at Delta with q kept at x is

    F_ref1=(1+s)F0-(s+p)F_minus1+p F_minus2.           (4)

On the post-pulse constant-x segment, solve (1) backward:

    F_actual1=[F4-(1+s)F3+(s+p)F2]/p.                 (5)

Here F_actual1 means the regular constant-coordinate force immediately after
returning to x, extrapolated from settled samples. Possible local force
impulses at the ideal jump are excluded, as in the parent. Hidden derivative
couplings and instrument settling must not contaminate the admitted samples.

Thus the observed difference D_end=F_actual1-F_ref1 is computable from six
samples using only s,p. Each trial reconstructs its own counterfactual baseline;
different trials need no shared hidden preparation. Very small p makes backward
extrapolation unstable, even though algebraic inversion exists.

For exact s,p and uniform pre/post force-error bounds,

    |error D_end| <= L_pre*epsilon_pre + L_post*epsilon_post,
    L_pre=|1+s|+|s+p|+p,
    L_post=[1+|1+s|+|s+p|]/p.                         (6)

This is the norm of the actual linear extrapolation. It does not include
coefficient error; a deterministic extension is given below.

## 3. The pulse-end sign is insensitive to frequency aliases

Let g solve the normalized impulse equation from the parent, and define
J_end=integral_0^Delta g(v)dv. Equation (5) of the parent yields

    D_end(x,y)=-J_end a(x)[b(y)-b(x)]/tau.             (7)

For every Omega2>0, Gamma>=0 and Delta>0, J_end>=0. To prove it, put
z(t)=1-Omega2*integral_0^t g(v)dv. Then

    z''+Gamma z'+Omega2 z=0, z(0)=1, z'(0)=0,
    d[(z'^2+Omega2 z^2)/2]/dt=-Gamma z'^2<=0.

Hence z(t)<=1 and J_end=(1-z(Delta))/Omega2>=0. For Gamma>0 the inequality
is strict at every Delta>0: nonzero initial acceleration causes positive
integrated dissipation on any such interval. For Gamma=0,
J_end=[1-cos(sqrt(Omega2)*Delta)]/Omega2, with zeros at complete periods.
No damping regime or frequency upper bound was selected in this proof.

An observed nonzero anchor E0 in the parent inverse already excludes J_end=0
within this class. Therefore J_end>0 on the anchored data and the positive
reciprocal-potential criterion is still

    B(y)-B(x)=kappa integral_x^y A(v)dv, E0*kappa<0.    (8)

One can reconstruct and challenge relative a,b from (7)-(8) without choosing
a coupling polynomial, a hidden initial state, continuous frequency aliases,
or the absolute value of J_end. Those unknown magnitudes remain in the overall
coupling scale. They have not been derived by cancellation.

The sign proof is specific to a pulse-end difference. At a general later lag
the integrated impulse response can be negative; substituting a late force
sample for the extrapolated pulse end would invalidate this inference.

## 4. Calibration-error propagation and test separation

Write the exact calibration system X theta=y, theta=(s,p). Let measured
X_hat,y_hat have induced infinity-norm errors at most epsilon_X,epsilon_y,
and theta_hat=X_hat^{-1} y_hat for a square rank2 selection. If

    eta=||X_hat^{-1}||_infinity epsilon_X < 1,

then the Neumann inverse bound and
X(theta-theta_hat)=(y-y_hat)-(X-X_hat)theta_hat give

    ||theta-theta_hat||_infinity <=
      ||X_hat^{-1}||_infinity/(1-eta)
                    *[epsilon_y+epsilon_X||theta_hat||_infinity]. (9)

With each original force-sample error <=epsilon_cal, each difference error is
<=2epsilon_cal, so epsilon_X=4epsilon_cal and epsilon_y=2epsilon_cal suffice.
This is deterministic and retains correlations conservatively; it is not an
independent-noise likelihood. Additional rows can be used with an explicitly
bounded solver instead of claiming (9) for arbitrary least squares.

For pole coefficient error <=epsilon_theta and |F_i|<=M over the six true
pulse samples, with all interpolation points satisfying p>=p_min>0 and
|s|<=S, derivatives of (4)-(5) give

    |coefficient error D_end| <= M*epsilon_theta *
         [2/p_min+4+(2+S)/p_min^2].                   (10)

Indeed the s derivative is (F2-F3)/p-F0+F_minus1, bounded by
M(2/p_min+2). The p derivative is
-[F4-(1+s)F3]/p^2+F_minus1-F_minus2, bounded by
M[(2+S)/p_min^2+2]. The mean-value integral proves (10). Add (6), evaluated
at the estimated coefficients, for pulse measurement errors; M bounds the
true samples. Timing error, drift and pulse-shape errors remain separate.

Development/calibration histories determine a single uncertainty region for
s,p and verify rank. Separate development pulses reconstruct A,B. Freeze all
regions, pulse selection and error budgets before evaluating reserved pulses
and coordinate pairs. Data with an unbounded denominator margin, uncertain
force sign, hidden control-dependent gains or unmodeled transitions do not
meet this contract.

## What is and is not resolved

The previously supplied continuous poles can be replaced by an experimentally
testable discrete recurrence for this protocol. No microscopic frequency is
selected, and no state is assigned. Positive hidden mass/stiffness and
nonnegative damping, the response class, actual coordinate/source/time
registration, finite-pulse fidelity and continuum coverage remain conditions.
Rank failure is an inconclusive identification attempt, not a disproof of
the physical model. Passing finite tests is not a unique action derivation.

The reconstructed reciprocal interaction is a candidate common force core,
not a complete gravitational action or a derivation of quantum outcomes.
The scalar campaign can reuse the method only after establishing its physical
observable/source bridge. All executable examples here are synthetic.
