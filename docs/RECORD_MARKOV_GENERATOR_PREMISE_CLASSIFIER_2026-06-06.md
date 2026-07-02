# Record Markov-Generator Premise Classifier

**Date:** 2026-06-06
**Claim type:** exact-support, stacked on the Markov-generator embeddability
boundary
**Runner:** [`scripts/frontier_record_markov_generator_premise_classifier_2026_06_06.py`](../scripts/frontier_record_markov_generator_premise_classifier_2026_06_06.py)
**Cached output:** [`logs/runner-cache/frontier_record_markov_generator_premise_classifier_2026_06_06.txt`](../logs/runner-cache/frontier_record_markov_generator_premise_classifier_2026_06_06.txt)
(`SCORECARD: PASS=22 FAIL=0`)

## Source boundary (2026-06-12)

**Boundary:** premise taxonomy / finite example support. Effective status is
audit-derived; this source records only the claim boundary.

The runner computes the displayed two-state stochasticity, generator, and
embedding checks, but the classifier levels and gates are introduced as a
premise map rather than derived from cited retained inputs or first-principles
framework dynamics.

This note may be cited for Markov-generator premise discipline and for the
checked finite examples. It may not be cited as a retained derivation of a
production kernel, clock, rate unit, Born/IID bridge, or physical dynamics law.

```yaml
actual_current_surface_status: exact-support
trace_class: direct_blocker_closure
reachability_to_target: partially_closes
conditional_surface_status: null
hypothetical_axiom_status: null
admitted_observation_status: null
proposal_allowed: false
proposal_allowed_reason: "This classifier enumerates premise gates for record dynamics. It does not derive a kernel, generator, clock, rate unit, Born/IID bridge, or dial selection."
audit_required_before_effective_retained: true
bare_retained_allowed: false
```

## Scope

This branch stacks on
`RECORD_MARKOV_GENERATOR_EMBEDDABILITY_BOUNDARY_2026-06-06.md`, which separates
a discrete stochastic production kernel from a continuous-time Markov rate law.
The classifier adds a reusable premise map for later dynamics claims.

The key distinction is:

```text
post-record information is not a probability law.
```

After a record has been written, the site carries realized information. A
future-record probability law needs an additional production kernel, and a
pre-record probability interface needs a Born/IID or equivalent bridge. A
continuous-time dynamics claim then needs still more: embeddability, a supplied
generator, a clock interval, and a rate/unit normalization.

## Premise Levels

The runner classifies a dynamics claim into these levels:

| Level | Licensed by | Still missing |
|---|---|---|
| `post-record-information-only` | realized record atoms | future-record probabilities |
| `production-kernel-model` | a stochastic next-record kernel | Born/IID bridge, Markov generator or embeddability proof |
| `Markov-semigroup-model` | a valid generator and clock interval | physical rate/unit normalization |
| `physical-rate-model` | generator, clock interval, rate unit, and probability-origin bridge | downstream physics interpretation still depends on the specific model |

The runner checks the exact kernels from the embeddability boundary:

- `P_lazy` is stochastic and embeddable after a generator is supplied.
- `P_swap` is stochastic but determinant-obstructed for finite bounded
  continuous-time Markov generation.
- `P_reset` is stochastic but singular, so exact finite-time reset needs a
  sink/asymptotic/unbounded premise rather than a finite bounded generator.

## Classifier Consequences

The classifier gives later record-dynamics PRs a simple audit rule:

- record append/count dynamics can talk about realized information;
- probability over future records requires a production kernel;
- pre-record probability requires a probability-origin bridge;
- continuous-time rates require embeddability and a generator;
- physical rates require a clock/rate normalization.

This is where the pre-record/post-record distinction matters. A qubit or
pre-record state can carry probabilities. A post-record site carries realized
information. Dynamics must say which side of that interface it is using.

## Non-Claims

This branch does not:

- derive the production kernel;
- derive Born probabilities or IID assumptions;
- derive a continuous-time Markov generator;
- derive a physical clock or rate unit;
- prove finite-time exact reset from a bounded generator;
- select or fix any Koide/generation dial location;
- update repo-wide authority surfaces.
