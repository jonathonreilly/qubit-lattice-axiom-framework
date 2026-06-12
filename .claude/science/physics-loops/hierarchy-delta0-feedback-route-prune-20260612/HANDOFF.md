# Handoff

This PR source-repairs the hierarchy DELTA0 magnitude open gate by recording one existing route-pruning result.

PR: https://github.com/jonathonreilly/qubit-lattice-axiom-framework/pull/3720

It does not close the gate. It records that ordinary mean-field link feedback is refuted as the supplier for the `alpha_s`-per-decoupling attachment rule, and leaves the three surviving route families explicit.

Verification:

```text
PYTHONPATH=scripts python3 scripts/frontier_hierarchy_alpha_lm_magnitude_delta0_open_gate.py
# PASS=32 FAIL=0

python3 scripts/precompute_audit_runners.py --runners scripts/frontier_hierarchy_alpha_lm_magnitude_delta0_open_gate.py --allow-non-main
# ok 1, nonzero_exit 0
```
