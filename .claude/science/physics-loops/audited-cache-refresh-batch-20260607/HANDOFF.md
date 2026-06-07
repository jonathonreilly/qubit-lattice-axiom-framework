# Handoff

Branch: `physics-loop/audited-cache-refresh-batch-20260607`

This branch refreshes 18 audited runner caches that were `sha_mismatch` and not
covered by open PRs. It edits only cache files plus this loop pack.

No audit verdict files were edited. No source notes or runner sources were
changed. No retained status movement is claimed.

Withheld target:

- `scripts/frontier_observable_principle_p1_bridge_operator_algebraic_external_narrow.py`
  should be repaired separately because its process exits successfully but its
  internal scorecard reports `TOTAL: PASS=28, FAIL=1`.

Next action: open the cache-refresh PR, then continue on missing-runner rows
or the withheld observable-principle repair.
