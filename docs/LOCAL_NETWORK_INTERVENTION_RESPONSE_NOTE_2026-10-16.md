# Conditional response to an identified local network intervention

Claim type: bounded_theorem

A calibrated change to one intermediate connection imposes a relation across
three full input/output responses. Its short-time response also identifies a
conditional path-access order. These tests are consequences of a supplied finite
linear action and physical channel contract. They do not derive that action,
quantum probabilities, a scalar potential, an initial state, or measured scales.

```yaml
target_claim_type: bounded_theorem
actual_current_surface_status: conditional-support
trace_class: upstream_support
target_claim_id: null
target_blocker_text: "focus on deriving the remaining assumptions rather than supplying them"
source_of_blocker_text: user_goal
reachability_to_target: supports
artifact_role: theorem
conditional_surface_status: "Exact finite-network response and deterministic bounds under the specified action, preparation, source, readout and intervention conditions."
hypothetical_axiom_status: "The candidate linear action and measurement contract are explicit conditions, not new framework axioms."
admitted_observation_status: "No empirical data input; all controls are synthetic."
claim_type_reason: "The algebraic conclusions require a specified finite positive stiffness and calibrated common response across interventions."
audit_required_before_effective_retained: true
bare_retained_allowed: false
next_trace_action: "Identify a realizable fixed-action source, local coupling intervention and readout; reserve test settings before comparing data."
```

## Target, proof obligations and scientific boundary

**Target.** For the finite positive symmetric stiffness, common source/readout
and rank-one intervention defined below, prove the three-setting full-response
identity, its deterministic measurement-error bound, and the impulse-response
leading order and remainder determined by the first accessible path moment.

| Obligation | Disposition |
|---|---|
| Observed/hidden elimination and initial forcing | Derived by differentiation and substitution |
| Same boundary response for two positive-spring graphs | Explicit orthogonal-similarity construction |
| Common-intervention full response | Derived by inverse multiplication |
| Three-setting relation and uncertainty | Derived algebraically and by triangle inequality |
| Accessible path order and finite-time remainder | Derived from convergent matrix series |
| Positive-spring graph-distance specialization | Proved by signed shortest-walk sums and bipartite parity |
| Physical action, local intervention and source/readout identification | Open, supplied conditions for these theorems |
| Actual data discrimination and initial-state preparation | Open; no fitted or independent-test data here |

The strongest missing physical step is a justified map from actual preparation,
forcing, connection changes and records to the common response in this theorem.
A tunable effective network alone does not supply that map. No target-equivalent
missing lemma is described as near closure. The intended consumer is a future
fixed-action environmental-response calculation in the scalar research program;
no existing framework claim is promoted or used as a mathematical premise here.

## Inputs, provenance and role

| Input | Role | Provenance | Remaining physical obligation |
|---|---|---|---|
| Finite real quadratic action and unit kinetic matrix | Candidate dynamics | Explicitly selected mathematical class | Derive or discriminate the action and physical coordinate/mass map |
| Positive constant stiffness | Stable finite domain | Theorem condition | Actual background and range of linear response |
| Fixed source/readout and initial preparation | Common measurement definition | Theorem condition | Independent apparatus and environmental calibration |
| Known rank-one direction and amplitude | Controlled intermediate intervention | Added single-edge potential in the example | Show what physical control changes and bound unwanted changes |
| Difference-error certificates and norm bound | Deterministic bounds | Supplied inequalities; exactly computed in synthetic controls | Obtain valid instrument and response certificates |
| Matrix inverses, Taylor series and graph walks | Mathematical tools | Re-derived below | No physical identification supplied by these tools |

The mathematics is reconstruction of standard finite linear-system and
rank-one inverse methods, not a novelty claim for projection-induced memory or
Sherman-Morrison algebra. The explicit diagnostic is kept separate from any
claim that an evolving network replaces quantum mechanics.

## Explicit candidate and observation contract

Assume a finite real network with unit kinetic matrix, time-independent positive
symmetric stiffness K, action L=(dot Q.dot Q-Q.K.Q)/2+f b.Q, and calibrated
linear readout c.Q. Unit kinetic normalization, finite linear dynamics, source,
readout, initial preparation and physical coordinates are supplied. They are
not derived from repo Records, a lattice or the measured scalar theory.
Positive graph springs and ground springs form a subclass. A graph may be a
physical candidate only after its sites and edges are independently identified.

An observed impulse response or transfer function measures a relation between
specified input/output channels. It need not expose every intermediate node.
The equations below give constraints for that declared experimental contract;
no new dataset, response spectrum or independent empirical test is supplied.

## Eliminating a neighborhood produces memory and initial-state forcing

Split Q=(q,x), K=[[a,b^T],[b,C]], with scalar observed q and C positive. Write

    q''+a*q+b^T*x=f,
    x''+C*x+b*q=0.

Duhamel's formula gives, for t>=0,

    x_h(t)=cos(sqrt(C)t)x0+C^(-1/2)sin(sqrt(C)t)v0,
    x(t)=x_h(t)-integral_0^t C^(-1/2)sin(sqrt(C)(t-s))b*q(s) ds.

Differentiating verifies the hidden equation and its two initial conditions.
Thus the exact observed equation is

    q''+a*q-integral_0^t M(t-s)q(s) ds=f-b^T*x_h(t),
    M(t)=b^T*C^(-1/2)sin(sqrt(C)t)*b.

The minus sign is fixed by elimination. No stochastic noise assumption was
needed: unknown initial neighbors give an unknown forcing function. Declaring
that forcing thermal, white, independent, stationary or zero adds information.
For zero initial data and Laplace z in the right half-plane,

    chi(z)=1/[z^2+a-b^T(z^2 I+C)^(-1)b].

Diagonalizing C makes the self-energy a sum of nonnegative modal weights over
z^2+omega_j^2. A fitted memory law therefore has a specific admissibility class
under this candidate. The Schur condition a>b^T C^(-1)b ensures positivity of
the full stiffness. The apparent temporal nonlocality disappears when x is
retained, but this is ordinary coarse-grained dynamics, not a replacement for
quantum interference. Projection-induced memory is known prior art; see
[Mori1965](https://doi.org/10.1143/PTP.33.423), whose abstract was consulted.
No theorem or fluctuation-dissipation premise from that article is imported.

## Even a complete endpoint response need not identify physical adjacency

Take K=[[4,-1,0],[-1,5,-1],[0,-1,6]], observe/force e0, and let O fix e0 while
rotating the two hidden coordinates by [[3/5,-4/5],[4/5,3/5]]. Then K'=O K O^T
has exactly the same e0^T(z^2 I+K)^(-1)e0 for every invertible z.
K is a chain; K' has all three nonzero negative pair off-diagonals. Both have
positive row sums and are realizable as positive springs plus positive ground
springs with unit masses. They differ in adjacency in their declared nodal
coordinates yet have identical measured boundary response. The proof is direct
orthogonal similarity with Oe0=e0. No numerical spectral fit is involved.

An effective chain or a count of observable normal modes can be useful without
being a reconstruction of microscopic adjacency. Extra channels, known spatial
coordinates, source access or controlled interior interventions can break some
of this ambiguity. We do not claim all such information is insufficient.

## A common interior intervention gives a stronger observable constraint

Now restore arbitrary input b and readout c. At fixed z let A=z^2 I+K0 and
R=A^(-1). Suppose the ONLY change across environments is a calibrated stiffness
term theta*w*w^T, with fixed known direction w. For a single spring between
nodes i,j, w=e_i-e_j and the added potential is theta*(Q_i-Q_j)^2/2.
The same source, readout, background and linear response definition must hold.
Require A and A+theta*w*w^T invertible; stability also requires an admissible
Ktheta if interpreted dynamically. Define

    gtheta=c^T(A+theta*w*w^T)^(-1)b,
    Delta(theta)=g0-gtheta,
    H=(c^T R w)(w^T R b), J=w^T R w.

Multiplication by A+theta*w*w^T verifies the standard rank-one inverse formula
and gives

    Delta(theta)=theta*H/(1+theta*J).

This uses transpose bilinear products even for complex z, not Hermitian norms.
No positivity of H is asserted for different source/readout channels. This is
established Sherman-Morrison algebra, not a novel identity. The relation holds
for the full response, without isolating one mode or discarding a background.
For nonzero theta and H, theta/Delta(theta)=1/H+theta*J/H is affine in theta.
For any three calibrated theta1,theta2,theta3 the division-free necessary test is

    Rtest = theta2*(theta3-theta1)*Delta1*Delta3
          - theta3*(theta2-theta1)*Delta1*Delta2
          + theta1*(theta2-theta3)*Delta2*Delta3 = 0.

This polynomial remains true at blind channels H=0, including Delta=0, where
it carries no identifying power. Distinct nonzero settings are needed for a
useful test; near-zero responses make the divided version unstable. Passing
this test is necessary within the contract, not sufficient to prove a rank-one
physical intervention: invisible additional changes and special degeneracies
can also pass. A generic rank-two perturbation can fail it, as the controls show.
If theta or the background/readout is freely refitted for each environment, the
cross-environment claim has changed and this test loses its intended force.

## Deterministic measurement-error certificate

Let measured complex differences be d_i, with certified |Delta_i-d_i|<=epsilon_i.
For each product define

    B_ij=epsilon_i*|d_j|+epsilon_j*|d_i|+epsilon_i*epsilon_j.

Triangle inequality gives |Delta_i Delta_j-d_i d_j|<=B_ij, hence

    |Rtest(d)| <= |theta2*(theta3-theta1)| B_13
                 + |theta3*(theta2-theta1)| B_12
                 + |theta1*(theta2-theta3)| B_23

under the model. The differences share a baseline measurement; this deterministic
bound permits arbitrary correlated errors. It assumes exact or independently
certified theta values; errors in theta require extra terms. It does not infer
error bars from data or turn an error certificate into a statistical confidence
statement. A violation beyond valid errors rejects this specific common-response
contract; it does not by itself identify which physical premise failed.

## What can actually be pursued

This yields a conditional research protocol: identify
input/readout physically, characterize preparation and memory, calibrate one
local coupling perturbation, then compare several settings using one shared
response model and a reserved test setting. Calibration/development settings
must be labeled before independent tests. We have derived an observable
constraint of a candidate, not its action, scale, initial state or measurement
identification. Those intervention premises are separate from an endpoint-only scalar reconstruction. The useful next step is an actual fixed-action
response calculation with justified source/environment/readout, rather than
calling an adjustable network or a fitted memory kernel a derivation.

## Exact response order within the declared candidate

Let K be a positive real symmetric stiffness matrix, e a unit coordinate at the
observed and driven node, and w the fixed direction of a calibrated intervention
Ktheta=K+theta*w*w^T, also positive. Initial data are zero and the input is an
ideal impulse at e. Denote by h0(t),htheta(t) the scalar displacement responses.
Define d as the smallest nonnegative integer for which

    mu_d = w^T K^d e != 0.

If no such integer exists, the observed Krylov space is orthogonal to w and the
intervention is invisible in this input/output channel for every time. A finite
matrix needs only its first dimension-many powers to decide that exact condition,
by its characteristic polynomial. This is a conditional algebraic statement,
not a stable numerical test from noisy data.

For finite d and nonzero theta, the rank-one identity of the preceding response derivation and the Neumann
series R(z)=sum_(n>=0)(-1)^n K^n z^(-2n-2), at sufficiently large real z, give

    g0(z)-gtheta(z) = theta*mu_d^2*z^(-4d-4)+O(z^(-4d-6)).

Indeed e^T R w and w^T R e both first appear at order z^(-2d-2), their signs
square to one, and the denominator 1+theta*w^T R w starts at one. Equivalently,
using the convergent impulse-response series

    hK(t)=sum_(n>=0)(-1)^n*(e^T K^n e)*t^(2n+1)/(2n+1)!,

all earlier difference coefficients vanish and

    h0(t)-htheta(t)=theta*mu_d^2*t^(4d+3)/(4d+3)!+O(t^(4d+5)).

This follows by matching the convergent resolvent series, or differentiating
finite-dimensional analytic response, not by an unqualified asymptotic inverse
Laplace transform. The result detects the degree of access to the changed
connection through this channel; it does not assign a microscopic coordinate
system or derive the network dynamics.

## When the algebraic order is graph distance

For a connected positive-spring graph, K has off-diagonal entries -k_ij<0 on
edges and zero otherwise, with positive grounding sufficient for K>0. For an
edge w=e_i-e_j, let d_i,d_j be distances from the observed vertex to its ends.
Below min(d_i,d_j), the corresponding matrix powers vanish: a walk cannot
traverse the graph in fewer steps. If d_i<d_j, the first contributing walks all
reach i at d_i and contain no diagonal stay or detour; their weights share sign
(-1)^d_i and are strictly positive in magnitude. Thus mu_d is nonzero at d=d_i.
The analogous claim holds when j is nearer. If the endpoints have equal distance,
their two weighted sums can cancel; graph distance alone then does not fix d.

On a bipartite graph, the distances to the ends of an edge have opposite parity
and differ by at most one, so they differ by exactly one. Hence the cancellation
case is absent for this single-edge perturbation with positive springs. A finite
connected subgraph of the cubic nearest-neighbor graph is an example, but the
classical spring action and readout remain extra premises beyond repo adjacency.
For edge distance d=0,1,2 the earliest response difference is respectively
order t^3,t^7,t^11. These are orders of small amplitudes, not hard propagation
delays. The continuous-time finite oscillator model has analytic tails and does
not by itself establish a relativistic light cone.

## A finite-time remainder certificate

Let M=max(||K||_2,||Ktheta||_2)>0. With m=2d+2, the first omitted term has degree
2m+1=4d+5. Each matrix moment difference is at most 2 M^n. Therefore for real t

    |h0(t)-htheta(t)-theta*mu_d^2*t^(4d+3)/(4d+3)!|
      <= 2*M^(2d+2)*|t|^(4d+5)/(4d+5)! * cosh(sqrt(M)*|t|).

The bound follows by summing absolute Taylor terms and using
(4d+5+2r)! >= (4d+5)!*(2r)!. It is conservative but valid for all finite t under
the fixed matrices. It supplies no apparatus error certificate, impulse
bandwidth, minimum detectable signal or derivative estimate. Those must be
separately calibrated before inferring d from observations.

## Useful falsification and remaining ambiguity

The chain/triangle pair above has identical original boundary response.
Applying the same physically labeled hidden-edge direction w=(0,1,-1) changes
the leading coefficient: in the chain mu1=-1; in the rotated network mu1=1/5.
Their intervention responses thus differ by a factor 25 at the leading order,
even though their unperturbed endpoint responses agree exactly. If instead w
is also rotated by O, the equivalence persists: physical identification of the
intervention is precisely the extra information doing the work.

This gives a concrete observations-backward route: calibrated perturbations at
intermediate locations can constrain accessible path depth and distinguish
some networks hidden by endpoint equivalence. It does not prove that the actual
world is such a network, select its action, or remove the need for a physical
measurement map. Time-varying/adaptive K, nonlinear responses, unknown masses
and unmeasured channels require a new derivation of the response contract;
choosing their dynamics after seeing a discrepancy would be model development.

## Scope of the witnesses and broader alternatives

The two positive-spring matrices and the symmetric invisible-edge example are
explicit existence witnesses. They do not close other reconstruction routes.
Additional independently calibrated channels, known geometry, time-dependent
interventions, nonlinear probes and preparation control are distinct routes
left open. The present algebra neither excludes evolving networks nor proves
an obstruction for every physical realization. Its quantified bounds apply
only to the displayed finite matrices and stated response conditions. No
general no-go classification or independent wall count is requested.

## Reproduction and review record

Primary runner: `scripts/local_network_response.py`.
Its imported helper is `scripts/local_network_response_math.py`; it is imported
normally so packet discovery can include the actual mathematical helper.

    python3 scripts/local_network_response.py
    python3 scripts/local_network_response.py --json

Both run the same synthetic controls. The default output additionally states
which finite resolutions were checked and that infinite-lattice dynamics were
not executed. Neither invocation reads empirical data. Integrity reads bind
this note and the mathematical helper; the canonical cache envelope binds the
runner and declared inputs. The 120-second timeout is declared in both files.

The author work preserves the original derivations and independent source
checks in the campaign checkpoint. This canonical integration receives its own
same-session check of the final source, imports, interacting conclusions and
runner, with the immutable evidence in `outputs/local_network_response/`.
Any source correction is reviewed before publication; a successful computation
or source review does not apply an audit verdict. Shared integrated-main landing
validation remains a separate prerequisite to any later authorized merge.
