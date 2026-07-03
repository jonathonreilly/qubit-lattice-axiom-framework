# Post-Record Model-Selection Firewall

**Date:** 2026-06-06
**Type:** exact no-go / selection firewall
**Claim type:** no_go
**Status:** no-go branch-local for deriving a canonical model, prior,
decision rule, or dial selection from finite post-record data and supplied
scores alone; audit_required_before_effective_retained=true;
bare_retained_allowed=false.
**Primary runner:**
[`scripts/frontier_post_record_model_selection_firewall_2026_06_06.py`](../scripts/frontier_post_record_model_selection_firewall_2026_06_06.py)
**Cached log:**
[`logs/runner-cache/frontier_post_record_model_selection_firewall_2026_06_06.txt`](../logs/runner-cache/frontier_post_record_model_selection_firewall_2026_06_06.txt)

## Result

Finite post-record data can support exact scoring once candidate laws are
supplied. The scoring layer still does not select a canonical model.

For a realized word `w*`, a supplied finite candidate family `M`, and supplied
laws `P_m`, the likelihood vector

```text
L(w*) = (P_m(w*))_{m in M}
```

is only a score vector. It does not contain:

- a prior over `M`;
- a loss function or decision threshold;
- a rule for ties;
- a rule for admissible candidate families;
- a rule for extending or excluding candidates;
- a physical interpretation of the probabilities.

Finite counterexamples show the obstruction:

1. The same likelihood vector can yield different posterior argmaxes under
   different supplied priors.
2. Maximum-likelihood scoring can tie without a supplied tie-breaker.
3. Adding an admissible-looking candidate that concentrates on the observed
   word can change the maximum-likelihood winner.
4. The same likelihood ratio can pass or fail depending on the supplied
   threshold.

Therefore post-record data plus supplied scores do not force a unique model,
candidate law, or generation/Koide dial location. They can only evaluate a
candidate under an explicitly supplied scoring and decision interface.
Equivalently: finite post-record scoring does not force a unique model.

## What this prunes

This prunes the route:

```text
post-record finite data
  + likelihood or p-value scores
  => canonical model / dial selection.
```

The valid route is conditional:

```text
post-record finite data
  + supplied candidate family
  + supplied model laws
  + supplied prior/loss/threshold/tie/admissibility rule
  => selected candidate under that supplied rule.
```

## What remains useful

The firewall does not weaken score interfaces. It makes their import boundary
explicit:

- finite likelihoods and p-values remain exact under supplied laws;
- model comparison remains possible under supplied rules;
- stable dial locations can be tested if a candidate law and stability
  criterion are supplied;
- no audit verdict or retained promotion follows from the scores alone.

## Status certificate

```yaml
actual_current_surface_status: no-go
trace_class: negative_route_pruning
reachability_to_target: prunes
conditional_surface_status: model selection remains conditional on supplied candidate, prior/loss/threshold/tie/admissibility rules
hypothetical_axiom_status: null
admitted_observation_status: null
proposal_allowed: false
proposal_allowed_reason: "This branch prunes score-to-selection overclaims; it does not propose retained status."
audit_required_before_effective_retained: true
bare_retained_allowed: false
```

## Runner certificate

The runner verifies:

- source-anchor boundaries for post-record data and probability residuals;
- exact likelihood vectors for finite supplied laws;
- posterior argmax reversal under different supplied priors;
- maximum-likelihood ties without a tie-breaker;
- family extension changes the maximum-likelihood winner;
- likelihood-ratio decisions depend on supplied thresholds;
- no model family, prior, decision rule, physical law, or generation/Koide dial
  is derived by Record.

Run:

```text
python3 scripts/frontier_post_record_model_selection_firewall_2026_06_06.py
```
