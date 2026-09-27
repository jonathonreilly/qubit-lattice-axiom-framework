# Finite-path guide dependence and shared curvature covariance

Status: proposed_retained
Claim type: bounded_theorem
Date: 2026-09-27
Runner: [finite_path_guide_dependence_2026_09_27.py](../scripts/finite_path_guide_dependence_2026_09_27.py)

```yaml
actual_current_surface_status: conditional-support
target_claim_type: bounded_theorem
trace_class: upstream_support
target_claim_id: null
target_blocker_text: "The photon calculations need observable-specific sampling and extrapolation control before interpreting size trends."
source_of_blocker_text: user_goal
reachability_to_target: supports
artifact_role: theorem
next_trace_action: "Match the finite-time physical functional and control projection length, sampling covariance and truncation before a size extrapolation."
conditional_surface_status: "Exact finite-dimensional identities conditional on the supplied matrix, positive guide and ideal path algorithm."
hypothetical_axiom_status: null
admitted_observation_status: null
claim_type_reason: "The supplied model and algorithm are hypotheses; their framework derivation and physical identification are not asserted."
audit_required_before_effective_retained: true
bare_retained_allowed: false
```

## Target and imports

**Target.** For a supplied finite real symmetric stoquastic matrix and a
strictly positive guide, derive the stationary weighted-path endpoint-energy
functional, its finite-projection guide dependence, the corresponding
reversal-invariant event-cap functional, and the covariance cancellation when
two curvature estimates reuse the same middle-field observation.

Write H = D - A, with D diagonal, A symmetric, A(x,x)=0 and A(x,y)>=0.
The state set is finite. The guide psi(x)>0, segment duration Delta>0 and
segment count M>=1 are supplied; T=M Delta. Exact continuous-time proposal
rates, exact weights, and the specified accept/bounce operation are assumed.
For the ground-limit statement only, restrict to a connected component with
a nonzero ground overlap; a positive spectral gap and width bound are
additional hypotheses for the displayed quantitative bound.

| Input | Role and provenance | Open bridge |
| --- | --- | --- |
| H, psi, Delta, M | Supplied mathematical model and algorithm choices | No derivation of these choices from the framework is claimed |
| Finite matrix exponential and spectral decomposition | Standard finite-dimensional mathematics; the needed path identity is proved below | No physical interpretation follows from this machinery |
| Half-sum of endpoint local energies | Supplied estimator definition | Mapping to a measured physical observable remains separate |
| Curvature stencil and reuse of one observation | Supplied linear estimator design, analyzed exactly | Ground curvature, field-step error and physical photon identification remain open |
| Ideal stationarity and exact arithmetic | Conditions for the invariant-law expectation | Finite-run equilibration and implementation error require their own evidence |

The primitive registry was checked at base e37967e326c2bdb429bd3106d34158bd5420e9c0.
No registered units, kinetic-form or pointwise realized-state primitive is
needed by this finite-matrix theorem. No axiom or primitive is added. No
observation, fit or cubic-model output enters the proof.

## Obligation graph

The weighted-path identity follows from proposal reversibility and cancellation
of guide ratios, proved here. Integrating it gives the matrix exponential by
the finite Dyson expansion, justified here. Skew balance plus the rejection
flip proves invariance of the lifted chain, not convergence to it. Endpoint
averaging then gives the energy functional; spectral decomposition gives its
projection dependence. A path restriction invariant under reversal gives the
capped functional. Linear covariance algebra proves the shared-observation
cancellation. These are the proved obligations of the stated target.

For the downstream photon calculation, the strongest missing numerical step
is controlled convergence of the *same curvature functional* under projection
length and size, with observable-specific sampling and truncation error.
Connecting that functional to a physical preparation and detector is a further
open obligation. Neither obligation is used as a lemma of this theorem.

## Weighted paths and bounce invariance

Set q(x,y)=A(x,y) psi(y)/psi(x), lambda(x)=sum_y q(x,y), and
E_L(x)=(H psi)(x)/psi(x)=D(x)-lambda(x). The proposal jump process is
reversible for the unnormalized measure m(x)=psi(x)^2 because

    m(x) q(x,y) = psi(x) A(x,y) psi(y) = m(y) q(y,x).

Let omega have endpoints x,y, ordered jump times and piecewise constant state.
Its proposal density Q_x includes product(q) exp(-integral lambda dt).
Multiplying by exp(W), W=-integral E_L dt, therefore gives the identity

    m(x) Q_x(d omega) exp(W)
      = psi(x) psi(y) product(A along jumps) exp(-integral D dt) d(times).

The right side is invariant under reversal. The internal guide factors have
telescoped; this is a pathwise equality, including the zero-jump path.
The sum over jump counts and integral over ordered times converges absolutely
in finite dimension, bounded by exp(T(max|D|+||A||)). The Dyson expansion of
exp(-T(D-A)) consequently gives the endpoint kernel G_T=exp(-T H).

The proposed path law is proportional to m(x0) times all segment proposal
densities times exp(sum W_j). A positive-direction move removes the first
segment and proposes a new last segment; its paired reverse-direction move
adds the reversed removed segment. Proposal reversibility cancels the base
path factors. The ratio of weighted target and proposal densities is
exp(W_new-W_removed), so the stated Metropolis acceptance is appropriate.

Lift to (path,direction) with half the target weight in each direction. Keep
direction on acceptance and reverse it on rejection. Accepted positive flux
equals the paired accepted negative flux. Incoming accepted flux at a path
in direction d is its target weight times the acceptance probability in
direction -d. Incoming rejection flux supplies the complementary probability
from direction -d. Their sum equals its target weight. Thus the lifted law
is invariant. This proves neither irreducibility nor a mixing-time bound.

## Endpoint energy and finite projection

With Z=psi^T G_T psi>0, the endpoint pair law is

    P_T(x,y) = psi(x) G_T(x,y) psi(y) / Z.

Both endpoint marginals equal psi(x)(G_T psi)(x)/Z. Their local-energy
half-sum has expectation

    E_psi(T) = psi^T H G_T psi / Z
             = -d log(Z)/dT
             = (exp(-T H/2)psi)^T H (exp(-T H/2)psi)
               / ||exp(-T H/2)psi||^2.

For eigenvalues E_n and overlaps c_n, the difference from a simple ground
energy E_0 with c_0 != 0 is

    E_psi(T)-E_0 = sum_(n>0) |c_n|^2 (E_n-E_0) exp(-T(E_n-E_0))
                    / (|c_0|^2 + sum_(n>0) |c_n|^2 exp(-T(E_n-E_0))).

It is nonnegative. Its T derivative is minus the variance of E_n under these
normalized spectral weights. If E_n-E_0>=g>0 for all excited states and
E_n-E_0<=B, then

    0 <= E_psi(T)-E_0
       <= B (||psi||^2-|c_0|^2) exp(-gT) / |c_0|^2.

This is a sufficient bound with supplied g, B and overlap. It does not supply
their volume dependence. For a degenerate ground space, replace |c_0|^2 by
the total overlap with that space and require a gap above it. For one state
there is no excited contribution. Reducible matrices retain the endpoint
identity; a particular run need not reach every component. Zero guides,
nonstoquastic or nonsymmetric matrices and infinite state spaces are outside
this claim. At T=0 the endpoint identity has the usual Rayleigh limit.

For the exact example H=[[0,-1],[-1,0]], the ground energy is -1.
At T=log(2)/2 the propagator is proportional to [[3,1],[1,3]]. Direct endpoint
averaging and the independent spectral formula give:

| Guide | Endpoint marginal | Local energies | Exact mean |
| --- | --- | --- | --- |
| (1,1) | (1/2,1/2) | (-1,-1) | -1 |
| (1,2) | (5/19,14/19) | (-2,-1/2) | -17/19 |

The finite-path difference is 2/19 under exact stationarity, without sampling
or population error. Independently, at T=log(2), the propagator
[[5/4,3/4],[3/4,5/4]] gives the second guide mean -35/37 and difference 2/37.
These are existence witnesses in a supplied two-state model, not estimates of
the bias in a cubic lattice calculation. They distinguish finite projection
from Markov equilibration. Guide agreement likewise need not prove projection
convergence: different guides may share the same spectral energy average.

## Reversal-invariant segment restrictions

If a proposal with more than J jumps in a segment is rejected, the invariant
path law is restricted to at most J jumps in each segment. This assumes
initialization satisfies the restriction and overflows produce rejection,
including the usual direction flip. The omitted proposal mass is rejection
mass, not a renormalized conditional proposal.

Let K_J(Delta) sum the physical weighted paths with that restriction. It is
symmetric and independent of psi. Its entries are nonnegative and diagonal
entries positive. Set C=K_J(Delta)^M. The endpoint law uses C in place of G_T,
and the half-sum expectation is

    E_cap = psi^T (H C + C H) psi / (2 psi^T C psi)
          = psi^T H C psi / (psi^T C psi).

The two scalar numerator terms agree by transposition; commutation is not
required. In general C does not commute with H, so the uncapped derivative
and projected-Rayleigh representations have not been established for E_cap.
For example H=[[0,-1],[-1,1]], J=0, Delta=log(2), M=2 gives
C=diag(1,1/4). For psi=(1,2), endpoint averaging gives -3/4, whereas the
Rayleigh quotient of sqrt(C)psi is -1/2. The cap-zero chain is reducible;
this is a statement about the declared invariant ensemble, not equilibration.
Zero observed overflow is a diagnostic, not a bound on omitted path weight.

## Shared curvature observation

Consider two estimators chi_a=c(15 X_a-16 Y+Z_a) and
chi_b=c(15 X_b-16 Y+Z_b), using literally the same random variable Y.
For the variance statements assume finite second moments, as holds for
energy averages on the supplied finite state space; c is a fixed real number.
Then, for every outcome,

    chi_a-chi_b = c(15(X_a-X_b)+Z_a-Z_b).

For V=(X_a,X_b,Z_a,Z_b) and w=(15,-15,1,-1), the exact variance is
c^2 w^T Cov(V) w. If these four variables are mutually independent, this
reduces to c^2[225(Var X_a+Var X_b)+Var Z_a+Var Z_b]. It contains no Y term,
even if Y is correlated with them. Under the additional independence of Y,
adding the two individual variances instead overcounts by 512 c^2 Var(Y).
The general covariance formula remains valid when any independence fails.
This algebra validates no estimated block variance, normal tail or effective
sample size. The runner independently enumerates a five-variable sign space.

For N>0, h!=0 and c=1/(9 N h^2), the same identity applies to the
three-field energy stencil.
The stencil is a supplied finite-difference observable; it is not itself a
proof of the h->0 susceptibility or a photon dispersion. Energy projection
bounds must be propagated with the absolute stencil weights, including their
h^-2 amplification, before they bound its curvature error.

## Source interpretation and review record

The motivating source review concerns PR9352 at
`73f2ed7e46f0d4a4ff320c7d462c2fce701d7e7d` and PR9328 at
`4fa11f9aefa9dac4413be73f237cc65b22221ffa`, refreshed 2026-09-27.
These are provenance, not mathematical premises or runner inputs. The full
source arguments, runners and caches were inspected at those exact revisions.
Their reported finite diagnostics are not recomputed by this note.

The PR9352 implementation uses an endpoint half-sum, path length 40, a
512-event segment cap and one reused middle-field estimate in its guide
comparison. The idealization above therefore exposes two separate issues:
finite-length guide dependence persists at stationarity, and the shared
middle term cancels in the difference. A guide split alone does not identify
population error or establish underestimated block variance. The two-state
example does not apportion the observed cubic-model split among its causes.
This note does not edit or replace either source PR, erase its finite
diagnostics, or select one guide as physically correct.

A fixed-population projector also needs matched finite-time boundary states
and readout functionals before guide comparisons isolate population error.
Here is the finite-matrix identity: with Psi=diag(psi) and initial particle
law mu_0, exact infinite-population evolution has density
mu_t=Psi exp(-tH) Psi^-1 mu_0. Indeed, for row proposal generator Q with
off-diagonal q and diagonal -lambda, the weighted forward generator is
Q^T-diag(E_L)=-Psi H Psi^-1. Its mixed local-energy expectation is
psi^T H exp(-tH) Psi^-1 mu_0 / (psi^T exp(-tH) Psi^-1 mu_0), obtained by
summing E_L against mu_t. For mu_0 proportional to psi^2 it equals the
uncapped endpoint target at the same t. Fixed mu_0 under a guide change
generally changes both physical boundaries. Time-averaged estimates introduce
their specified time weighting as another distinction.

Before seeing the primary derivation, an independent reconstruction obtained
the same path law and bounce argument, used the different log(2) two-state
example, and enumerated a restricted two-segment example. After freezing those
results, comparison reconciled the two times and checked the shared-variable
covariance. The current public runner adds exact finite balance and
noncommuting-cap checks. These checks establish selected identities and
examples; they are not an audit verdict or a large-lattice simulation.

The paired [runner](../scripts/finite_path_guide_dependence_2026_09_27.py)
uses rational arithmetic and no external scientific input. Its canonical
[cache](../logs/runner-cache/finite_path_guide_dependence_2026_09_27.txt)
binds this note and its runner source. There are no helper runners. General
identities are proved in the note; finite checks do not replace those proofs.
Independent audit and the shared integrated landing gates remain required.

The downstream consumer is the photon observable and extrapolation work.
Preparation, dynamics, measured observable and calibrated comparison are not
connected by this result. No mass, cosmological number or physical photon
claim inherits a new evidential status from it.
