# Handoff

PR: https://github.com/jonathonreilly/cl3-lattice-framework/pull/1943

This block repairs `guard_reconciliation_note` with a narrow aggregate runner
certificate for `N=100, q=0.03`.

The wrapper executes `scripts/dense_prune_channel_count_guard.py` with
`DENSE_GUARD_LAYERS=100` and `DENSE_GUARD_QS=0.03`, then asserts that the
plain aggregate has flips and large gravity damage while the guarded aggregate
has zero flips, smaller gravity damage, preserved `eff_ch`, and fewer removed
nodes. Seed-level examples remain context only.

Generated audit state after the pipeline:

```text
audit_status=unaudited
effective_status=unaudited
claim_type=bounded_theorem
ready=true
open_dependency_paths=[]
```

Key cached rows:

```text
plain:   d_pur=+0.0094 d_grav=-3.2356 eff 5.005->2.447 flips=3
guarded: d_pur=-0.0039 d_grav=-0.1272 eff 5.159->5.056 flips=0
```
