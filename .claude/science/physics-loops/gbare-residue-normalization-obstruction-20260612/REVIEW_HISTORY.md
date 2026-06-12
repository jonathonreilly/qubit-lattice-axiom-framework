# Review History

Self-review:

- Checked that the patch does not claim retained `g_bare=1`.
- Checked that no audit result files are edited.
- Verified the runner and refreshed its cache.

Commands:

```text
python3 scripts/frontier_gbare_same_1pi_admitted_residue_repair.py
python3 scripts/precompute_audit_runners.py --runners scripts/frontier_gbare_same_1pi_admitted_residue_repair.py --allow-non-main
```
