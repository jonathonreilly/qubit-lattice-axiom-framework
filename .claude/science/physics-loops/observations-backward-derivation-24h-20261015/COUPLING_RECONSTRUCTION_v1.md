# Reconstructing a coupling from controlled histories

**Claim type:** bounded_theorem. **Status:** conditional-support; author
derivation, pending focused independent check. No empirical validation or
framework premise adoption. This continues the observation contract after the
three-hour neighborhood exploration; it is not a correction to its frozen report.

## Target and observational reason

The preceding adaptive model supplied a quadratic coupling. The next target is
to infer the shape of a coupling from source responses and test whether its two
directions can arise from a common interaction potential, without choosing a
hidden initial state. This addresses an actual remaining assumption rather than
another example with a selected polynomial.

Chen et al. report a mechanical 1:3 internal resonance, while their simplified
equation (1) uses a damped, linearly coupled 1:1 surrogate. A resonance ratio
therefore does not itself identify the microscopic coupling. Their experiment
motivates controlled response comparisons; it supplies no data to the theorem
below. [Primary source](https://arxiv.org/html/1612.00490v3).

Nonlinear elimination of a bath and estimation of state-dependent memory are
established subjects, including [Ayaz et al.](https://arxiv.org/abs/2202.01922)
and [Ge et al.](https://doi.org/10.1103/PhysRevLett.133.077301). Their abstracts
were inspected; their full proofs were not used. The new campaign calculation
is the explicit pulse/baseline inverse, with a conservative-interaction test
and its preparation/calibration limits. No broad literature novelty claim is
made for nonlinear memory, low-rank factorization, or reciprocal potentials.

Current main searched: `bbada1fe09b2d10d610560864d86b68c24a59713`.
The exact search and source disposition are in `COUPLING_ROUTE_INTAKE_v1.json`.
The 62 open PR heads are unchanged from the preceding intake. The previous
network blocks supply motivation, not logical premises of this derivation.

## Explicit conditional class and observation contract

Let q range over a connected real interval I. An intervention prescribes q(t).
When q is held at x, the conjugate measured source has the form

    f_x(t) = u(x) + a(x) w(t),
    tau w'' + gamma w' + C w = -b(q(t)),                 (1)

where tau,C>0, gamma>=0 and u,a,b are real C1 functions. No relation between
a and b is initially imposed. The local moving-coordinate force may be more
general: it need only reduce to u(x) on the measured constant segments, with
no additional delayed contribution there. The pulse edges themselves are not
used as force observations. The hidden equation has no impulsive coupling to
q' or q''. These are substantial model restrictions, to be tested, not derived
from the minimal lattice/record premises.

Each run can start with arbitrary, unrelated w and w'. No thermal distribution,
equilibrium preparation, typicality, or reset is imposed. Within a run the
physical coefficients and measurement map are fixed. The coordinate, time and
conjugate source must be independently identified. A common positive constant
force gain will cancel from the shape test; setting-dependent gain will not.

Put Omega2=C/tau and Gamma=gamma/tau. These two ratios must be established on
calibration/development histories, with uncertainty, before reserved tests.
Learning them is not deriving a physical scale. A perfectly steady baseline
cannot by itself identify them. The discussion below first treats them as
exact inputs and then bounds force errors; uncertain poles require a separate
propagation bound.

## 1. Predict a counterfactual baseline from the same run

Before the pulse, hold q=x. Then the force F obeys

    F'' + Gamma F' + Omega2 F = c_x,
    c_x = Omega2 u(x) - a(x)b(x)/tau.                  (2)

The unknown c_x is constant. Set X=(F,F',c_x)^T and

    T = [[0,1,0],[-Omega2,-Gamma,1],[0,0,0]],  e=(1,0,0).

For three pre-pulse times t_i<=0 define O with rows e exp(T t_i).
If O is invertible, the continuation with q held at x is exactly

    F_ref(t) = v(t) F_pre,
    v(t) = e exp(T t) O^{-1}.                         (3)

Proof: X'=TX follows from (2), so F_pre=OX(0). This does not require knowledge
of u,a,b,w(0),w'(0), or a shared starting state between trials. It does require
observability of this finite-dimensional baseline and a valid model over the
extrapolation window. Repeated poles are covered by the matrix exponential.
Aliased sample times can make O singular; a small determinant is not a reliable
numerical certificate. Condition and error amplification must be recorded.

With each pre-sample error <=epsilon_pre and post-sample error <=epsilon_post,

    |D_measured-D_true| <= epsilon_post
                             + ||v(t)||_1 epsilon_pre,             (4)

where D=f_after-F_ref. This bound excludes pole error, drift and pulse-shape
error; they cannot be hidden in measurement noise without separate bounds.

## 2. Exact finite pulse response, with preparation eliminated

At time0 change q from x to y, hold for duration h>0, then return to x.
The idealized jumps are a definition of this conditional probe. No claim of
finite actuator force at the jumps is made. Observe only t>h.

Let g solve g''+Gamma g'+Omega2 g=0 for t>0 with g(0)=0,g'(0)=1,
and let J_h(t)=integral_0^h g(t-s) ds. The difference of the actual hidden
trajectory and its same-run constant-x continuation has zero initial data.
Variation of constants gives

    D(x,y;t) = -a(x)[b(y)-b(x)] J_h(t)/tau.            (5)

Every hidden homogeneous contribution cancels because (3) reconstructs it
from that run's own pre-pulse observations. No two different trials have to
share an initial state. The proof works with damping, including critical and
overdamped cases; it does not infer damping from an undamped model.

This is also a falsifier: D(x,x;t)=0, and D/J_h must be independent of the
post-pulse time wherever J_h!=0. A response not satisfying this relation can
reflect additional modes, drift, input errors or an incorrect model class;
it does not by itself identify which cause failed.

For a physical transition q_actual(s) in place of the rectangular q_rect(s),
both returning to x by the observation time, the induced additional error is
bounded by

    |a(x)|/tau * integral |g(t-s)|
                         |b(q_actual(s))-b(q_rect(s))| ds.        (6)

If b is Lipschitz with independently valid constant L_b, replace the second
factor by L_b |q_actual-q_rect|. Neither L_b nor actuator fidelity is supplied
by the theorem. Readout settling or derivative coupling requires more terms.

## 3. Reconstruct two coupling shapes instead of choosing them

Fix h,t and a nonzero J=J_h(t). Let z be a reference pulse value. Define

    E(x,y)=D(x,y;t)-D(x,z;t)
          =-J a(x)[b(y)-b(z)]/tau.                    (7)

Choose r,y_star with E0=E(r,y_star)!=0. The data determine

    A(x)=E(x,y_star)/E0 = a(x)/a(r),
    B(y)=E(r,y)/E0 = [b(y)-b(z)]/[b(y_star)-b(z)].      (8)

Thus E=E0 A B: every two-by-two minor vanishes. Conversely, a kernel with
this factorization and D(x,x)=0 satisfies

    D(x,y)=E0 A(x)[B(y)-B(x)].                        (9)

This converse concerns the supplied pulse-response surface, not every possible
history or a unique hidden realization. It reconstructs relative shapes only.
Finite samples do not establish rank one on a continuum, and an anchor near
zero makes the inverse ill-conditioned. Different hidden modes with the same
coupling shape can share rank one; (7) does not count physical modes.

For estimated numerator N_hat, anchor E0_hat and bounds epsilon_N,epsilon_0,
if |E0_hat|>epsilon_0, an estimated ratio R_hat=N_hat/E0_hat obeys

    |R_hat-R| <= [epsilon_N+|R_hat| epsilon_0]
                            /[|E0_hat|-epsilon_0].                (10)

This follows by subtracting the two fractions. Common force gain cancels
from A,B; independent gain changes across x or y can counterfeit or destroy
the factorization and reciprocal-shape test.

## 4. Test for a reciprocal interaction rather than impose it

Within the restricted class with constant diagonal kinetic coefficients, a
common interaction potential exists after multiplying the hidden equation by
a positive constant lambda precisely when

    a(q)=lambda b'(q),  lambda>0.                    (11)

Necessity follows from equality of mixed potential derivatives. For sufficiency
take U'=u and

    V(q,w)=U(q)+lambda*C*w^2/2+lambda*b(q)*w.

Then V_q=u+a w and V_w=lambda C w+lambda b. If the moving q equation is
m q''+u+a w=f with m>0, this V and kinetic terms m q'^2/2 and
lambda tau w'^2/2 give that conservative core. A Rayleigh term
lambda gamma w'^2/2 gives the stated hidden damping. The clamped observations
alone do not establish the moving-q inertia, global potential stability or a
closed conservative system when gamma>0.

In terms of reconstructed shapes, (11) is equivalent to the existence of a
single nonzero constant kappa satisfying

    B(y)-B(x)=kappa integral_x^y A(s) ds  for all x,y in I,        (12)
    E0*kappa < 0,   provided J>0.                               (13)

Proof: writing a_r=a(r), d=b(y_star)-b(z), (11) gives
B'=a_r A/(lambda d)=kappa A. Conversely B'=kappa A gives
a/b'=a_r/(d kappa), a constant. Since E0=-J a_r d/tau,
E0*kappa=-J a_r^2/(tau lambda), proving the positivity equivalence.
At zeros of A the derivative of B must vanish too. A nonzero anchor guarantees
a_r and d are nonzero. Normalization fixes kappa as
1/integral_z^y_star A when this integral is nonzero, so kappa is not a free
point-by-point selector. J>0 holds in a sufficiently short positive-lag
window because g'(0)=1; an arbitrary late oscillatory window cannot use (13).

Equations (12)-(13) test reciprocal coupling without prescribing a polynomial.
Rank one alone is insufficient: a(q)=1+q and b(q)=q+q^3/3 on [0,1]
give a rank-one E but not a constant a/b'. A negative multiplier passes the
shape relation but fails (13). This excludes only a positive diagonal-mass
potential completion in the stated coordinates; velocity couplings,
non-diagonal metrics, feedback and larger hidden realizations remain outside.

For a frozen estimated kappa with error epsilon_kappa, shape errors
epsilon_A(s),epsilon_B and quadrature handled separately, the error in the
estimated residual of (12) is bounded by

    epsilon_B(y)+epsilon_B(x)+|kappa_hat| integral epsilon_A
     +epsilon_kappa [integral |A_hat|+integral epsilon_A].         (14)

This is a triangle-inequality bound, not a statistical confidence level.
Reserve coordinate pairs and pulse widths/times after development; passing a
finite selection does not fix untested coupling values or establish a theory.

## Physical interpretation and remaining work

The removal is narrowly defined: a selected coupling polynomial and hidden
preparation are unnecessary for this conditional inverse test. Observed shapes
would remain measured reconstructions, not first-principles laws. No actual
pulse-response dataset is supplied here. All executable controls are synthetic.

The calibrated coordinate/source pair, a finite-dimensional time-invariant
hidden response, pulse fidelity, one shared channel and stability remain
unresolved physical conditions. A reciprocal interaction does not determine
U, a global potential, absolute hidden normalization, quantum records or the
scalar-gravity measurement bridge. The approved scale-reference primitive is
a units convention, kinetic isotropy supplies structural graining, and the
realized-state primitive supplies pointwise evaluation; none supplies these
missing dynamics or measurements. Their current sources were read.

The same A and B can be compared across environments only when the coordinate,
source, pulse and instrument registration are justified. Different fitted
functions per environment would abandon the proposed common-coupling test.
An actual experiment must calibrate poles and transfer errors separately, use
development pulses for shape reconstruction, freeze its uncertainty region,
and then inspect reserved pulses. No source data have been assigned to an
independent test by this note.
