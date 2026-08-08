# Claim Status Certificate

```yaml
actual_current_surface_status: candidate-retained-grade
target_claim_type: positive_theorem
trace_class: direct_blocker_closure
reachability_to_target: closes
conditional_surface_status: null
hypothetical_axiom_status: null
admitted_observation_status: null
claim_type_reason: "An executable finite numerical claim: the supplied mixed-precision raw implementation completes at h = 0.125 and its live six-observable assertions pass."
audit_required_before_effective_retained: true
bare_retained_allowed: false
```

## Certificate checks

- Open imports for the claimed target: none.
- Observed or fitted target values used as proof inputs: none.
- Rounded cached targets used as proof inputs: none after this repair.
- Dependencies: the two supplied runner implementations and declared
  numerical protocols; no downstream ledger dependency is claimed.
- Runner checks dependency classes: it distinguishes raw generation from the
  support-only rescaled comparator and never uses the comparator to construct
  the raw row.
- Trace: direct closure of the exact noncompletion blocker.
- Review-loop disposition: pending.
- Independent audit required: yes.

The universal exact step-scale theorem fails the certificate and is excluded.
The candidate claim is only the finite implemented-row computation and live
pointwise comparison.

