# Post-Record Finite-Null Audit Interface

**Date:** 2026-06-06
**Type:** exact conditional audit interface
**Claim type:** bounded_theorem
**Status:** exact-support branch-local for the supplied finite-null audit
interface; null-law, statistic, threshold, and model-selection derivation remain
open; audit_required_before_effective_retained=true;
bare_retained_allowed=false.
**Primary runner:**
[`scripts/frontier_post_record_finite_null_audit_interface_2026_06_06.py`](../scripts/frontier_post_record_finite_null_audit_interface_2026_06_06.py)
**Cached log:**
[`logs/runner-cache/frontier_post_record_finite_null_audit_interface_2026_06_06.txt`](../logs/runner-cache/frontier_post_record_finite_null_audit_interface_2026_06_06.txt)

## Result

The post-record layer gives realized finite words. If an audit lane also
supplies a finite null law over those words, the framework has an exact finite
audit interface.

For a finite record alphabet `O`, a fixed horizon `n`, a supplied normalized
null law `P` on `O^n`, and an ordered finite statistic

```text
T: O^n -> S,
```

define the one-sided finite-null p-value of a realized word `w*` by

```text
p_T(w*) = P({w in O^n : T(w) >= T(w*)}).
```

Then, for `W` sampled from the supplied null law,

```text
P(p_T(W) <= alpha) <= alpha
```

for every `alpha` in `[0,1]`. The discreteness makes this conservative in
general, but it is exact: the p-value is a finite sum of supplied null
probabilities over a finite record-word set.

The supplied law may be a finite-history law from a supplied transition kernel,
an instrument model, or any explicitly normalized finite null. The record layer
does not supply that law.

## What this unlocks

This gives bounded and conditional audit lanes a precise grammar. The
null-law, statistic, threshold, and model-selection derivation remain open.

```text
post-record realized word
  + supplied finite null law
  + supplied finite statistic and threshold
  => exact conservative finite p-value / audit flag under that null.
```

It is useful for rows that already have a candidate stochastic model and need
to ask whether realized post-record data are compatible with that supplied
model. It also gives model-comparison work a clean place to attach likelihoods
or p-values without pretending that the record axiom selected the model.

## What remains outside

This note does not derive:

- the finite null law;
- the transition kernel, Markov property, or stationarity;
- the statistic, tail direction, threshold, or model-selection rule;
- independence, exchangeability, ergodicity, typicality, or a clock rate;
- Born weights, an instrument, Hamiltonian, action, or coupling;
- a generation or Koide dial setting;
- any audit verdict or retained status.

## Status certificate

```yaml
actual_current_surface_status: exact-support
trace_class: upstream_support
reachability_to_target: supports
conditional_surface_status: finite audit validity remains conditional on a supplied null law, statistic, and threshold
hypothetical_axiom_status: null
admitted_observation_status: null
proposal_allowed: false
proposal_allowed_reason: "This is a supplied-null audit interface, not a derivation of the null law or a status promotion proposal."
audit_required_before_effective_retained: true
bare_retained_allowed: false
```

## Runner certificate

The runner verifies:

- source-anchor boundaries for post-record words/counts and probability-law
  residuals;
- supplied finite null laws normalize exactly;
- supplied Markov kernels normalize their finite-history laws exactly;
- finite-null p-values are exact finite sums;
- the p-values are conservative under the supplied null by enumeration;
- the same realized word can have different audit outcomes under different
  supplied nulls;
- flags under a threshold are conditional on the supplied null and threshold;
- Record does not derive the null law, statistic, threshold, Born law,
  Hamiltonian, clock, or generation/Koide dial.

Run:

```text
python3 scripts/frontier_post_record_finite_null_audit_interface_2026_06_06.py
```
