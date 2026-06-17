# Handoff

## What Changed

The parent anomaly theorem now treats
`ANOMALY_FORCES_TIME_ABJ_INCONSISTENCY_ACCEPTED_PREMISE_BRIDGE_BOUNDED_NOTE_2026-05-26.md`
as plain-text provenance for the separate accepted-premise companion, not as a
markdown dependency edge. The local P-ABJ premise remains explicit and external.

The runner now verifies the absence of that markdown child edge and the cache is
fresh with `TOTAL: PASS=88 FAIL=0`.

PR: https://github.com/jonathonreilly/qubit-lattice-axiom-framework/pull/4206

## What This Unlocks

After the citation graph and audit queue are rebuilt by the audit/review lane,
`anomaly_forces_time_theorem` should no longer wait on the conditional ABJ child
row as a one-hop dependency. It still remains a bounded theorem over declared
premises and requires independent audit.

## What Remains

- P-ABJ is not derived.
- P-HY, P-COMP, P-REC, and B-AXIS remain declared boundaries.
- Existing PRs #4191 and #4192 handle separate ABJ child-row repair/boundary
  work and are not duplicated here.

## Verification

- `python3 scripts/frontier_anomaly_forces_time.py` -> `TOTAL: PASS=88 FAIL=0`
- `python3 scripts/cached_runner_output.py --refresh scripts/frontier_anomaly_forces_time.py`
- `python3 scripts/cached_runner_output.py --check-only scripts/frontier_anomaly_forces_time.py` -> fresh
- `python3 -m py_compile scripts/frontier_anomaly_forces_time.py`
- source-edge grep on the parent note found no ABJ child markdown link
