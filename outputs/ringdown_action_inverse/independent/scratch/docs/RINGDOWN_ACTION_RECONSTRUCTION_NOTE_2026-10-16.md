# Conditional action reconstruction from force response and ringdown

Claim type: bounded_theorem

Calibrated force records can determine coefficient functions inside a specified
quadratic hidden-mode action class. The inverse uses the complex linear-response
residue together with both ringdown harmonics. It reconstructs relative hidden
inertia, restoring and damping coefficients, coupling and a potential instead of
selecting their functions. The class itself and the physical measurement map
remain premises. The computations here use synthetic records only.

```yaml
target_claim_type: bounded_theorem
actual_current_surface_status: conditional-support
trace_class: upstream_support
target_claim_id: null
target_blocker_text: "focus on deriving the remaining assumptions rather than supplying them"
source_of_blocker_text: user_goal
reachability_to_target: supports
artifact_role: theorem
conditional_surface_status: "Reconstruction and realization of ideal rest-response and clamped-ringdown functions within a smooth reciprocal quadratic one-hidden-coordinate action class."
hypothetical_axiom_status: "The action, dissipation and measurement class are explicit candidate conditions; no framework axiom is adopted."
admitted_observation_status: "No measured data enter the runner; synthetic calibration, reconstruction and reserved preparations are separated."
claim_type_reason: "A constructive inverse with regularity, observability, force-calibration and class hypotheses."
audit_required_before_effective_retained: true
bare_retained_allowed: false
next_trace_action: "Bound rest-preparation and physical calibration errors; freeze the reconstructed functions before testing independent moving histories."
```

## Exact target and obligation graph

**Target.** On a connected regular coordinate interval, characterize and
construct the reciprocal quadratic action and Rayleigh functions that realize
specified ideal equilibrium dynamic stiffness and clamped force ringdowns,
up to the coordinate freedoms proved below.

| Obligation | Disposition |
|---|---|
| Held force and reciprocal response operator | Direct variation below |
| Eliminate unknown ringdown preparation | Residue/harmonic identities below |
| Recover relative hidden inertia | Complex second harmonic and integration below |
| Remove kinetic cross term | Explicit change of coordinates below |
| Recover remaining coefficient functions | Polynomial closure, static consistency and integration below |
| Realize the specified observation surface | Constructive sufficiency proof below |
| Remaining freedom in the regular class | Reconstruction comparison below |
| Finite-error propagation | Deterministic product/quotient bounds below |
| Physical action class and calibrated conjugate channels | Supplied; require independent experimental justification |
| Reliable continuum inference from noisy finite records | Open; the synthetic extractor supplies no such certificate |

The intended downstream consumer is environmental-response reconstruction in
the scalar research program. The strongest missing physical step is a validated
map from a real coordinate and force channel to this common response class.
There is no identification of the hidden coordinate with a gravitational field
or a quantum state in this theorem.

## Inputs, observation roles and prior art

The observation contract is a controlled coordinate x, the signed force R
required to impose it, a common time coordinate, a rest response Z=delta R/delta x,
and freely decaying force histories after preparation at fixed x. Force means
work conjugacy R dx, not an arbitrary detector output. Z is dynamic stiffness;
its reciprocal is the displacement/force susceptibility and has different poles.
These physical identifications must precede a candidate test.

| Input | Role | Provenance | Physical obligation |
|---|---|---|---|
| One real hidden coordinate and functions of x only | Candidate class | Declared here | Establish applicable modes and model discrepancy |
| Quadratic kinetic, potential and Rayleigh forms | Candidate class | Declared here | Test reciprocity and allowed nonlinearities |
| Force, coordinate and time normalization | Measurement | No empirical calibration supplied | Calibrate signs, phase, work and environment dependence |
| Rest linear response and full ringdown history | Ideal inference inputs | Synthetic records in runner | Bound rest contamination, bandwidth and readout errors |
| Smooth continuation and nonzero observable mode | Mathematical domain | Explicit hypotheses | Certify between-sample coverage and conditioning |
| Hidden unit and integration constants | Coordinate conventions | Proved freedoms below | A separately fixed physical hidden unit needs calibration |

The force/frequency relation is established prior art. Aspelmeyer, Kippenberg
and Marquardt, *Cavity optomechanics*, arXiv:1303.0733v1, Sec.III.A-B,
equations18-21, relate force to frequency pull within an adopted Hamiltonian.
Those sections were inspected; no full-review or experimental-data inspection
is claimed. Perkins and Bellan, *Phys. Plasmas*22,022108(2015),
DOI10.1063/1.4905635, discuss a classical Hellmann-Feynman theorem; only their
abstract and metadata were inspected. These are provenance, not proof inputs:
`https://arxiv.org/pdf/1303.0733v1` and
`https://authors.library.caltech.edu/records/jgh6r-1as74`.
The result below is proved directly. No broad literature-novelty claim is made.

## Candidate class and exact held-force equation

Let all coefficient functions be sufficiently smooth and real on a connected
open interval I. A prime denotes an x derivative. Assume

    T = M(x) xdot^2/2 + k(x) xdot wdot + tau(x) wdot^2/2,
    V = U(x) + B(x) w + C(x) w^2/2,
    D = d(x) xdot^2/2 + nu(x) xdot wdot + gamma(x) wdot^2/2.

D is the Rayleigh function. Equations are Euler-Lagrange for T-V plus
velocity derivatives of D. Only x has an externally applied force. Require

    tau>0, C>0, M tau-k^2>0, gamma>0, d gamma-nu^2>=0,
    Gamma=gamma/tau, O=C/tau>Gamma^2/4,
    lambda=-Gamma/2+i omega, omega=sqrt(O-Gamma^2/4)>0.

At a clamp, w0=-B/C and z=w-w0 satisfies
tau zddot+gamma zdot+Cz=0, so z=c exp(lambda t)+c*exp(lambda* t).
The complex coefficient c represents arbitrary real initial position and
velocity; no common initial preparation or distribution is chosen.
Direct variation of the visible equation at xdot=xddot=0 gives

    R=R0+Gz+k zddot+nu zdot+C' z^2/2-tau' zdot^2/2,
    R0=U'+B'w0+C'w0^2/2, G=B'+C'w0.                         (1)

In particular d/dt(T_xdot)=k wddot, whereas T_x includes
tau' wdot^2/2; this fixes the negative inertia-gradient sign.
The k' and M' terms vanish only because x is held.

Expand the force in its six independent real exponential components:

    R(t)=R0+f exp(lambda t)+f*exp(lambda* t)+h exp(-Gamma t)
             +g exp(2lambda t)+g*exp(2lambda* t),
    N(s)=G+nu s+k s^2,
    f=N(lambda)c,
    h=(C'-tau'O)|c|^2=tau O'|c|^2,
    g=(C'-tau'lambda^2)c^2/2.                               (2)

The six real functions are linearly independent on any open time interval
because their complex exponents are distinct under Gamma>0 and omega>0.
For fitted real cosine/sine amplitudes a_cos,a_sin, f=(a_cos-i a_sin)/2;
the same convention applies to g. The theorem requires nonzero excitation f.

## Rest response and observable invariants

Linearize at the rest equilibrium (x,w0). For visible and hidden perturbations
xi,eta, reciprocity gives

    tau(s^2+Gamma s+O)eta=-N(s)xi,
    delta R=P(s)xi+N(s)eta, P(s)=M s^2+d s+V_xx(x,w0).

Therefore

    Z(s)=P(s)-N(s)^2/[tau(s^2+Gamma s+O)],
    rho=Res_lambda Z=-N(lambda)^2/[tau(2lambda+Gamma)].      (3)

Require N(lambda)!=0. The residue removes the analytic visible-load polynomial.
Rest preparation belongs to this independent calibration; cancellation of c
in the subsequent ringdown calculation does not remove it.

Define measured-feature combinations

    K=|(2lambda+Gamma)rho|,
    Q=K h/|f|^2,
    S=-2(2lambda+Gamma)rho g/f^2,
    L=O-lambda^2=2omega^2+i Gamma omega,
    r=(S-Q)/L.

Substitution of (2)-(3), using K=|N(lambda)|^2/tau, proves

    Q=O', S=O'+(tau'/tau)(O-lambda^2), r=tau'/tau real.      (4)

Thus the harmonic phase supplies the relative hidden-inertia gradient. The
initial amplitude and phase cancel exactly. A power spectrum containing only
|g| does not supply S. Independent preparation repeats should yield the same
Q,S at the same x. Time-origin changes multiply numerator and denominator by
the same factors, so Q,S are unchanged.

The first equation can be tested without estimating a point derivative:
O(b)-O(a)=integral_a^b Q dx. If a separately justified Lipschitz bound L_Q
and midpoint error radii e_Qi are available on widths h_i, then

    |integral Q-sum_i h_i Qhat_i|
       <=sum_i h_i e_Qi+L_Q sum_i h_i^2/4.                 (5)

This follows by integrating L_Q|x-midpoint| on each bin. Endpoint O,
coordinate and time errors must also be added. Such a smoothness bound is
an additional certificate; it is not obtained from a finite grid by assumption.

## Coordinate freedom and explicit reconstruction

The kinetic cross term need not be supplied as zero. Set w=v+F(x),
F'=-k/tau. Substitution in the three quadratic forms gives

    k_new=0, tau_new=tau, C_new=C, gamma_new=gamma,
    M_new=M-k^2/tau,
    nu_new=nu-gamma k/tau,
    d_new=d-2nu k/tau+gamma k^2/tau^2,
    B_new=B+CF, U_new=U+BF+CF^2/2,
    w0_new=w0-F, G_new=G-Ck/tau.                          (6)

Both velocity matrices transform by invertible congruence; their positivity
is preserved. The visible equation changes by F' times the hidden equation,
which is zero on solutions with no hidden external force. At a clamp,
N_new(s)=N(s)-k(s^2+Gamma s+O), hence N_new(lambda)=N(lambda).
The observable force and its coefficients are unchanged. This is a proved
coordinate freedom in the stated class, not a proposed physical selector.
No environment-dependent hidden rescaling is used; that could introduce
hidden-coordinate dependence into the kinetic metric.

The following construction uses the k=0 chart.

1. Check Q=O' and real r. Choose a reference x_* and tau_*>0, and integrate

       tau=tau_* exp(integral_(x_*)^x r du), C=tau O,
       gamma=tau Gamma.                                    (7)

2. Choose one continuous square root

       n^2=-tau(2lambda+Gamma)rho,
       nu=Im(n)/omega, G=Re(n)-nu Re(lambda), N(s)=G+nu s.   (8)

   The nonzero argument has a smooth square-root branch on an interval.
   Its two choices differ by an overall reflection. Arbitrary pointwise sign
   choices do not define this continuous construction.

3. Compute P=Z+N^2/[tau(s^2+Gamma s+O)]. Require a real polynomial
   of degree at most two, P=M s^2+d s+P0. Require M>0,
   d gamma-nu^2>=0 and

       P0=R0'+G^2/C, equivalently Z(0)=R0'.                 (9)

   R0' is the derivative along the equilibrium curve, not at fixed hidden w.
   Exact knowledge of this polynomial identity is stronger than one fitted
   pole/residue or a finite set of frequencies.

4. Integrate w0'=-G/C and E'=R0. Set

       B=-Cw0, U=E+Cw0^2/2,
       V(x,w)=E(x)+C(x)[w-w0(x)]^2/2.                    (10)

All functions in this representative action and Rayleigh function have now
been reconstructed from the ideal observation functions and integration
constants. If the physical unit of w is independently fixed, tau_* still needs
calibration. Its arbitrary choice here expresses hidden-coordinate units.

## Sufficiency and remaining freedoms

Suppose the smooth observation functions satisfy (4), (7)-(9), positivity,
nondegeneracy and the full six-function ringdown closure. The construction has
equilibrium w0 and holding force E'=R0. At fixed hidden coordinate,
V_xx=R0'+Cw0'^2=R0'+G^2/C. Its rest dynamic stiffness is exactly Z by (9).
Its hidden poles equal lambda,lambda*. For each ringdown infer c=f/n. Then

    h_pred=tau O'|f/n|^2=h,
    g_pred=tau[O'+r(O-lambda^2)](f/n)^2/2=g.

The fundamental term and static offset agree by construction, proving
realization of every specified ringdown. This proves necessary and sufficient
compatibility on the stated ideal response/ringdown observation surface.
Arbitrary moving histories are additional experiments, not included in this
sufficiency assertion.

For any two compatible representatives in the k=0 chart, (4) fixes the same r,
so their tau functions differ only by a positive constant. Equation (8) fixes
G,nu up to that constant hidden unit and one reflection; (9) fixes M,d;
(10) fixes w0,E up to a hidden translation and additive potential constant.
Equation (6) restores arbitrary kinetic cross terms as the described hidden
translation depending on x. This comparison is restricted to the connected
regular class. It makes no uniqueness claim for other action classes.

Gamma=0, omega=0, rho=0, f=0 and disconnected intervals are outside this
theorem. As Gamma tends to zero the h term approaches the constant term and
extraction can become ill-conditioned. Nonquadratic hidden potentials, extra
modes, stochastic forcing, delayed operators and hidden-dependent kinetic
metrics have not been reconstructed here.

## Calibration covariance and certified errors

For a smooth one-to-one visible relabeling y=j(x), j'!=0, transform the
conjugate force as R_y=R_x/j'. Differentiating about rest gives

    Z_y=Z_x/(j')^2-R0 j''/(j')^3,
    rho_y=rho_x/(j')^2, (f_y,h_y,g_y)=(f,h,g)/j',
    (Q_y,S_y,r_y)=(Q,S,r)/j'.                              (11)

The equilibrium correction is analytic in frequency, so it does not change
the pole residue. Integration yields the same inertia and potential after
coordinate change. A sensor relabeling with an unchanged force channel is
a different measurement operation. Environment-dependent clock errors also
require independent calibration.

All following quantities are bounds on the **true** features, with independently
valid error radii. Let |lambda|<=Lmax, |Gamma|<=Gmax, |rho|<=Pmax,
Fmin<=|f|<=Fmax with Fmin>0, |h|<=Hmax, K<=Kmax and |g|<=G2max.
Put a=2lambda+Gamma, |a|<=Amax and e_a=2e_lambda+e_Gamma. Product and
modulus triangle inequalities give

    e_K=(2Lmax+Gmax)e_rho+Pmax e_a+e_a e_rho,
    e_D=2Fmax e_f+e_f^2, Dmin=Fmin^2,
    e_N=Kmax e_h+Hmax e_K+e_K e_h.

Require e_D<Dmin. The standard quotient identity then gives

    e_Q=e_N/(Dmin-e_D)+Kmax Hmax e_D/[Dmin(Dmin-e_D)],
    e_numS=2[(Amax+e_a)(Pmax+e_rho)(G2max+e_g)-Amax Pmax G2max],
    e_S=e_numS/(Dmin-e_D)
          +2Amax Pmax G2max e_D/[Dmin(Dmin-e_D)].           (12)

The complex denominator f^2 has the same modulus lower bound and perturbation
bound e_D. Let |L|>=Lmin, |S-Q|<=Wmax, and
e_L=e_O+2Lmax e_lambda+e_lambda^2<Lmin. A second quotient bound yields

    e_r=(e_S+e_Q)/(Lmin-e_L)
          +Wmax e_L/[Lmin(Lmin-e_L)].                      (13)

A compatible true model obeys |Im(rhat)|<=e_r. The log-inertia error is at
most the normalization error plus the **unsigned** path integral of e_r from
x_* to x, with coordinate/interpolation errors added. This remains valid for
x<x_*. A continuous square-root branch must separately be certified:
delta n=delta(n^2)/(nhat+n) displays the required branch/conditioning margin.
No independence of the feature errors was used.

These inequalities propagate certificates; noiseless fitting does not create
them. Finite-band analytic continuation, isolated-mode inference, instrument
phase, rest preparation and force calibration are open empirical obligations.

## Executable evidence and separation of roles

Primary runner: `scripts/ringdown_action_inverse.py`; imported computation:
`scripts/ringdown_action_math.py`. The proof is above and the helper derives
held equations symbolically from T,V,D. Synthetic frequency records come from
the two-coordinate linear equation matrix; time records come from a separate
ODE integration. A rational fit receives only the frequency records, then an
exponential fit receives the force records. Generator parameters enter only
generation and verification comparisons, not either extractor.

The first calculation separates three development environments from three
reserved synthetic environments/preparations. The function reconstruction
then uses 61 synthetic environments on [-0.8,1]; these are development data,
including environments used in the earlier step. It sets tau(-0.8)=1 as a
unit convention. Three additional initial states at existing environments
use their first 60 samples only to fit preparation; their later 541 samples
test prediction with frozen coefficient functions. They are synthetic tests,
not independent physical data. The static-slope check uses the generator's
analytic derivative as verification, not as a certificate inferred from data.

Rejection witnesses are explicit altered channels: quadratic output-only force
epsilon z^2 shifts Q by 2epsilon/tau; a cubic output adds exponents outside
the six-function closure; altered second-harmonic phase violates real r;
altered static slope or polynomial mass/damping violates (9) or positivity.
These are constructed examples, not exhaustive rejection theorems. Readout
distortion can imitate such residuals. Passing a finite test does not uniquely
select an action class.

The runner records every predicate and its detailed numerical evidence in
`outputs/ringdown_action_inverse/controls.json`. The canonical cache is produced
through `scripts/runner_cache.py`, with declared timeout120seconds. No measured
dataset is read. Package-local note/runner/helper hashes are integrity reads.
Symbolic proofs, separately integrated synthetic trajectories and focused
independent recomputation supply distinct checks; the proof does not rest on
the control count.

## Review record

This is an additive conditional theorem, replacing no current-main science.
The exploratory common-action runner initially failed a representation test
because an unsimplified SymPy residue retained cancelling polynomial symbols.
Its mathematical residue identity passed; simplifying before inspecting free
symbols corrected the predicate. The original failure and correction are
preserved in the campaign branch at b37b3432e3993cea4e428fc3201c95e33311e94f.
Focused checks of the exploratory derivations found no material discrepancy
within their hypotheses. The final canonical unit requires its own source-bound
check; neither those checks nor this note apply an audit verdict.

No external helper registry entry is required: the primary runner imports its
complete computation. Citation-policy code and authority files are unchanged;
the generated manifest must acknowledge this one new note. Shared integrated
current-main pipeline, strict lint and changed-evidence landing gates remain
pending. No science merge is authorized by this packet.
