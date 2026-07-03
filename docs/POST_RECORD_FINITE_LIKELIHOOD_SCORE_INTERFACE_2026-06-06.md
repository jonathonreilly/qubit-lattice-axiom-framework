# Post-Record Finite Likelihood-Score Interface

**Date:** 2026-06-06
**Type:** exact conditional score interface
**Claim type:** bounded_theorem
**Status:** exact-support branch-local for supplied finite model scoring;
model-family, prior, decision-rule, and dial-selection derivation remain open;
audit_required_before_effective_retained=true; bare_retained_allowed=false.
**Primary runner:**
[`scripts/frontier_post_record_finite_likelihood_score_interface_2026_06_06.py`](../scripts/frontier_post_record_finite_likelihood_score_interface_2026_06_06.py)
**Cached log:**
[`logs/runner-cache/frontier_post_record_finite_likelihood_score_interface_2026_06_06.txt`](../logs/runner-cache/frontier_post_record_finite_likelihood_score_interface_2026_06_06.txt)

## Result

The post-record layer gives a realized finite word. If a finite model family is
also supplied as normalized laws over the same word space, the framework has an
exact score interface.

For a finite record alphabet `O`, horizon `n`, supplied model index set `M`,
and supplied normalized laws

```text
P_m on O^n, for m in M,
```

the likelihood score of a realized word `w*` is

```text
L_m(w*) = P_m(w*).
```

For two supplied models with `L_j(w*) > 0`, the likelihood ratio is

```text
LR_ij(w*) = L_i(w*) / L_j(w*).
```

If a prior `pi` on the same supplied model list is also supplied, the Bayes
weight update is the exact finite normalization

```text
posterior_m(w*) = pi_m L_m(w*) / sum_k pi_k L_k(w*),
```

when the denominator is nonzero.

These scores compare supplied candidates. They do not choose the candidate
family, prior, decision threshold, observation protocol, physical probability
law, or dial.

## What this unlocks

This gives bounded and conditional audit lanes a precise model-score grammar:

```text
post-record realized word
  + supplied finite candidate laws
  + optional supplied prior or decision rule
  => exact likelihood vector, likelihood ratios, and conditional Bayes weights.
```

It is useful when several dynamics, instrument, or dial candidates have already
been supplied and the lane needs exact finite bookkeeping against realized
record data. A downstream row can then state which scoring or decision rule it
imports instead of hiding that rule inside the Record axiom.

## What remains outside

This note does not derive:

- the candidate model family;
- the prior over candidate models;
- a threshold, loss function, or decision rule;
- the observation protocol or horizon;
- a transition kernel, Markov property, stationarity, or independence;
- Born weights, an instrument, Hamiltonian, action, coupling, clock, or rate;
- a generation or Koide dial setting;
- any audit verdict or retained status.

## Status certificate

```yaml
actual_current_surface_status: exact-support
trace_class: upstream_support
reachability_to_target: supports
conditional_surface_status: finite model scoring remains conditional on supplied candidate laws and any supplied prior or decision rule
hypothetical_axiom_status: null
admitted_observation_status: null
proposal_allowed: false
proposal_allowed_reason: "This is a supplied-model score interface, not a derivation of the model family or a status promotion proposal."
audit_required_before_effective_retained: true
bare_retained_allowed: false
```

## Runner certificate

The runner verifies:

- source-anchor boundaries for post-record words/counts and probability-law
  residuals;
- supplied finite candidate laws normalize exactly;
- likelihood vectors are exact finite evaluations at the realized word;
- likelihood ratios are exact rational comparisons when denominators are
  nonzero;
- posterior weights normalize exactly when a prior and nonzero evidence are
  supplied;
- different supplied priors can change posterior ordering for the same data;
- zero-support denominator cases are guarded rather than turned into a
  canonical selection;
- Record does not derive the model family, prior, decision rule, Born law,
  Hamiltonian, clock, or generation/Koide dial.

Run:

```text
python3 scripts/frontier_post_record_finite_likelihood_score_interface_2026_06_06.py
```
