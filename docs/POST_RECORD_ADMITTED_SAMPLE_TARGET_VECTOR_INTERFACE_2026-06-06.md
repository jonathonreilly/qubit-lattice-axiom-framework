# Post-Record Admitted Sample Target Vector Interface

**Date:** 2026-06-06
**Type:** exact support / admitted observation interface
**Claim type:** bounded_theorem
**Status:** bounded-support interface for admitted finite post-record samples;
audit_required_before_effective_retained=true; bare_retained_allowed=false.
**Status authority:** source-side type boundary only; this packet does not apply
or predict an audit verdict.
**Primary runner:**
[`scripts/frontier_post_record_admitted_sample_target_vector_interface_2026_06_06.py`](../scripts/frontier_post_record_admitted_sample_target_vector_interface_2026_06_06.py)
**Cached log:**
[`logs/runner-cache/frontier_post_record_admitted_sample_target_vector_interface_2026_06_06.txt`](../logs/runner-cache/frontier_post_record_admitted_sample_target_vector_interface_2026_06_06.txt)

## Result

The target-vector firewall has a positive admitted-observation interface:

```text
supplied finite post-record sample plus supplied statistic set
  + exact counting
  => admitted empirical target vector
```

The sample is admitted observation data, not a probability law. The words carry
realized post-record information. They do not carry internal probability.

Weights and selection rules remain supplied. The empirical target vector can be
used by a supplied rule, but the sample alone does not select a production
kernel.

## Example

For the admitted four-word sample:

```text
AA, AB, BA, BA
```

the empirical vector for endpoint `A -> B`, endpoint `B -> A`, and
second-is-`B` is exactly:

```text
endpoint_ab = 1/4
endpoint_ba = 1/2
second_is_b = 1/4
```

## Status certificate

```yaml
actual_current_surface_status: exact-support
trace_class: upstream_support
reachability_to_target: supports
conditional_surface_status: "admitted finite post-record samples yield exact empirical vectors for supplied statistic sets"
hypothetical_axiom_status: null
admitted_observation_status: "sample is admitted observation data, not a derived probability law"
proposal_allowed: false
proposal_allowed_reason: "This branch defines an admitted-sample interface and does not derive weights, rules, kernels, or audit verdicts."
audit_required_before_effective_retained: true
bare_retained_allowed: false
```

## Boundaries

- Does not edit `docs/audit/data`.
- Does not apply or predict audit verdicts.
- Does not promote any row.
- Does not turn a sample into a probability law.
- Does not derive selection weights or rules from the sample.
- Does not select a production kernel from sample data alone.
- Does not derive a Born law from Record.
- Does not select or force a generation/Koide dial location.
- Does not turn stable settings into selected dials.

## Runner certificate

The runner verifies:

- source anchors in this note, the target-vector firewall, and the supplied
  kernel selection-rule interface;
- admitted sample status is explicit;
- post-record sample words are realized tuples, not probability carriers;
- atom counts and empirical statistic vectors are exact;
- empty samples, missing statistic sets, and unknown statistics are blocked;
- no audit verdict, audit-data write, retained/promoted claim,
  sample-as-law, sample-derived weights/rules, sample-alone kernel selection,
  Born-law derivation, stable-setting dial selection, or generation/Koide
  selection flag is set.

Run:

```text
python3 scripts/frontier_post_record_admitted_sample_target_vector_interface_2026_06_06.py
```
