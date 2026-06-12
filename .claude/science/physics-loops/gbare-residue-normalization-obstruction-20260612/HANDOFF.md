# Handoff

This PR repairs the audited-conditional `g_bare` same-1PI pinning row by making the missing bridge exact.

It adds an explicit residue-normalization multiplier `R(g_bare)` to the source note and runner. The proof shows:

- with the extra H_unit-residue normalization `R(g_bare)=1`, the existing algebra pins `g_bare=1`;
- without that bridge, the current retained packet also allows `R(g_bare)=g_bare^2`, which preserves canonical agreement and same-direction support while leaving `g_bare` arbitrary.

This is bounded support / negative route pruning, not a retained-positive promotion. The reviewer should extract the obstruction and keep downstream `g_bare=1` uses conditional unless a future theorem proves `R(g_bare)=1`.

Verification:

```text
python3 scripts/frontier_gbare_same_1pi_admitted_residue_repair.py
# PASS=43 FAIL=0

python3 scripts/precompute_audit_runners.py --runners scripts/frontier_gbare_same_1pi_admitted_residue_repair.py --allow-non-main
# ok 1, nonzero_exit 0
```
