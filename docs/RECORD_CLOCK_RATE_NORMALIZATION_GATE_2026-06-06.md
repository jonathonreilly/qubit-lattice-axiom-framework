# Record Clock/Rate Normalization And Stable-Dial Gate

Date: 2026-06-06

Status: exact-support

actual_current_surface_status: exact-support
trace_class: direct_blocker_closure
reachability_to_target: partially_closes
conditional_surface_status: null
hypothetical_axiom_status: null
admitted_observation_status: null
proposal_allowed: false
proposal_allowed_reason: "The block supplies an exact gate for stable dial locations under supplied generators; it does not derive the physical generator, dial value, probability-origin bridge, or clock/rate unit."
audit_required_before_effective_retained: true
bare_retained_allowed: false

## Summary

This block turns the dynamics residual into a usable interface:

```text
stable dial location != Record-selected dial value != physical rate normalization.
```

The post-record layer carries realized information: finite histories and
counts. A dial probability distribution belongs to the production or ensemble
layer. Once a production generator is supplied, a dial location can be an
ordinary stationary/stable point of that generator. Record itself does not pick
which point.

The runner proves this in a finite three-atom record alphabet. For the
one-parameter dial

```text
pi(s) = (1, s, s^2) / (1 + s + s^2),
```

each positive sampled location `s = 1, 2, 3` admits an explicit reversible
Markov generator `Q(s)` with:

```text
Q(s) pi(s) = 0,
```

one zero eigenmode, and negative transverse eigenmodes. The stable location is
therefore available as a generator-fixed point without being selected by the
Record axiom.

## Runner

Runner:

```text
scripts/frontier_record_clock_rate_normalization_gate_2026_06_06.py
```

Cache:

```text
logs/runner-cache/frontier_record_clock_rate_normalization_gate_2026_06_06.txt
```

Scorecard:

```text
PASS=30 FAIL=0
```

## Exact Content

### Post-record counts are not probabilities

The runner checks a count update

```text
(2, 1, 0) -> (2, 1, 1)
```

and separates it from a normalized dial probability vector. The count update
is an integral realized-information update; it increases total count. It is
not a probability state.

### Supplied generators stabilize dial locations

For each positive dial sample `pi(s)`, the runner constructs a complete-graph
reversible generator in column convention:

```text
p'(t) = Q p(t).
```

The generator has nonnegative off-diagonal entries and zero column sums. It
stabilizes the supplied dial:

```text
Q pi = 0.
```

Distinct supplied generators stabilize distinct dial locations. This is the
framework-safe version of the user's constraint: do not select the dial from
Record alone; target a stable setting on the dial once a generator/functional
is supplied.

### Rate and clock remain separate

Scaling a generator by a positive constant preserves its stationary dial:

```text
Q pi = 0  =>  (c Q) pi = 0.
```

The stable location is unchanged, but the off-diagonal rates and nonzero
eigenvalues scale. A physical rate claim therefore still needs a clock/rate
unit.

The two-state semigroup check gives the same transition matrix from two
different rate/clock pairs:

```text
r = log(2)/2,  t = 1
r = log(2)/4,  t = 2
```

Both have the same dimensionless product `r t`. The transition kernel fixes
the product in this example, not the absolute physical rate and clock
separately.

## Dynamics Implication

This unlocks a cleaner dynamics target:

```text
pre-record probability interface
  -> supplied production kernel/generator
  -> stable dial location
  -> clock/rate normalization if physical rates are claimed
  -> post-record realized count/history update after an atom is written
```

The framework no longer needs to phrase a generation/Koide dial result as
"Record selects this value." The acceptable positive target is:

```text
given a derived or admitted production generator, the observed/candidate dial
location is a stable fixed point or attractor of that generator.
```

That is a weaker and better-typed claim. It separates the stable-location test
from the harder questions of deriving the generator, deriving the probability
origin, and assigning physical time/rate units.

## Boundaries

This block does not:

- derive a record-production kernel;
- derive a Born/IID or other pre-record probability-origin bridge;
- derive the physical generator or action;
- choose a Koide/generation dial value;
- derive a physical clock or rate unit;
- update repo-wide authority surfaces.

The result is an exact interface theorem for later dynamics packets, not a
physical dynamics closure by itself.
