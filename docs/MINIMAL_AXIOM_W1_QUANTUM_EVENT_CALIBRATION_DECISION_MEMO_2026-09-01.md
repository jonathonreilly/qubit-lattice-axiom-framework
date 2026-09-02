# Owner decision memo — quantum-event calibration for W1

Date: 2026-09-01

## Decision exposed by Block 42

The current axioms require a nearest-neighbor-conditioned probability
distribution but deliberately do not specify its values. Exact physical
repeatability can force a binary qubit writer to be sharp, yet it leaves a
global Record-label orientation. The current Record wording does not orient
that label and does not itself imply operational repeatability.

If the intended framework meaning is that quantum possibilities are the
alternatives of the local quantum state and Record content is calibrated to
the corresponding quantum event, the smallest support-calibration clause is:

> For every registered binary rank-one projective context `C=(P,Q)`, `Q=I-P`,
> fix the exhaustive Record events `R_P,R_Q` and their Record-to-block coding
> independently of the response probabilities. Conditional on an eligible
> formation event `F`, exactly one of `R_P,R_Q` occurs. If `Pr(F|C,rho)>0` and
> `rho` is supported in `ran(P)`, then `Pr(R_P|F,C,rho)=1`, and likewise for
> `Q`.

This sentence fixes the `lambda=+1` orientation only after the response has
independently been shown affine. It does not define arbitrary probabilities,
formation locations, rates, histories, frequencies, or a CP state-update law.

For a foundation-level derivation of the affine conditional probability as
well, a separate sentence must explicitly survive the conditioning on Record
formation:

> Within every such context, probabilities of Record content conditional on
> Record formation depend only on the prepared one-site density possibility
> and are affine in it. For `rho=t rho_0+(1-t)rho_1`, the conditional response
> obeys `q_P(rho)=t q_P(rho_0)+(1-t)q_P(rho_1)`. A recorded preparation
> randomizer and a direct preparation representing the same `rho` must give
> the same conditional content law whenever it is defined.

This is not the same as adding probabilities of disjoint outcome Records.
It constrains how conditional content probabilities respond to two preparation
procedures that represent the same local quantum possibility.

The conditioning language is load-bearing. If `x=Tr(P rho)`, the affine joint
probabilities `Pr(F)=(1+x)/2`, `Pr(F and R_P)=x`, and
`Pr(F and R_(I-P))=(1-x)/2` obey endpoint calibration but give the nonlinear
conditional probability `Pr(R_P|F)=2x/(1+x)`. Thus merely saying that the
unconditioned preparation is a convex mixture does not prevent formation
selection bias.

Equal formation rates on the randomizer branches are a sufficient
calibration-grade apparatus check in an affine joint-effect model. They are not
equivalent to conditional affinity in full generality, and making formation
neutral for every process would wrongly ban legitimate state-dependent
heralding.

With explicit conditional affinity, the conclusion is direct. For each fixed
binary rank-one PVM `{P,I-P}`, an affine probability on the qubit density
matrices has the form `Tr(E_P rho)` for an effect `E_P`. Support calibration
at `P` and `I-P`, together with positivity of `E_P` and `I-E_P`, forces
`E_P=P`. Thus the two sentences yield `Pr(R_P|F,rho)=Tr(P rho)` for this
binary-projective scope without needing cubic covariance or repeatability.
They do not determine the post-Record state update.

Two alternative closure packages must therefore remain separate:

- conditional content affinity plus support-faithful calibration yields the
  binary-projective Born probability law, without an update instrument;
- exact operational repeatability plus independently oriented Record-to-state
  or Record-to-event coding yields the sharp reduced CP instrument.

Neither package follows from the current four axioms.

The repository also contains an exact effect-Gleason theorem: normalized,
noncontextual POVM additivity on all one-qubit effects forces trace form. That
route is mathematically broader but requires the additional physical claim
that supplied quantum effects are the same events whose probabilities are
inferred from Records. Its audit-ledger status is currently `unaudited`. It
must not be imported as if ordinary coarse-graining of already formed Records
had established all POVM-effect equivalences.

## Choices

| choice | consequence |
|---|---|
| keep current axioms | W1 remains a candidate-law or empirical-selection obligation |
| register support calibration only | selects orientation within a separately supplied affine response class; conditional affinity and the CP update remain open |
| register both in a scoped primitive | makes the Born-oriented one-qubit binary-projective conditional probability bridge a supplied foundation premise, subject to independent audit of its consequences; the CP update, arbitrary effects, and higher dimensions remain outside this result |

## Recommendation status

Do not edit the governing minimal-axiom memo. It has 539 direct and 2,218
transitive consumers, so changing its premise hash would force a broad re-audit
and would globalize ideal calibration across processes that may legitimately
use state-dependent heralding. If the owner confirms the intended calibrated-
event ontology, prefer a narrowly named approved primitive such as
`binary_projective_quantum_record_calibration`, containing exactly the two
scoped clauses above and consumed only by quantum Record/Born claims. This is a
physics postulate, not a derivation or free premise. Do not describe it as
deriving the sharp repeatable instrument: the latter still needs operational
repeatability or a microscopic update theorem.
