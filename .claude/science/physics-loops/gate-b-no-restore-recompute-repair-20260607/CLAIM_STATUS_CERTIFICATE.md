# Claim Status Certificate

actual_current_surface_status: bounded-support
trace_class: direct_blocker_closure
reachability_to_target: closes
conditional_surface_status: null
hypothetical_axiom_status: null
admitted_observation_status: null
proposal_allowed: false
proposal_allowed_reason: "The repair closes a runner-artifact blocker for a bounded one-seed replay, not an audit-ratified retained proposal."
audit_required_before_effective_retained: true
bare_retained_allowed: false

Verification:

```text
python3 scripts/gate_b_no_restore_joint_package.py --recompute --write-certificate
# recompute certificate written

python3 scripts/gate_b_no_restore_joint_package.py
# SCORECARD PASS=8 FAIL=0

python3 scripts/precompute_audit_runners.py --runners scripts/gate_b_no_restore_joint_package.py --force --push-mode=none
# OK
```

No `docs/audit/**` files are changed.
