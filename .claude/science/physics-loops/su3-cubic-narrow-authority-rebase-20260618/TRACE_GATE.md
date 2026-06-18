# Trace Gate

```yaml
trace_class: direct_blocker_closure
target_claim_id: su3_cubic_anomaly_cancellation_theorem_note_2026-04-24
target_blocker_text: "Local SU(3)^3 trace appeared to import broad one-generation matter closure and broad hypercharge uniqueness instead of narrow colour-sector suppliers."
source_of_blocker_text: user_goal
reachability_to_target: partially_closes
artifact_role: theorem
next_trace_action: "Independent reviewer/auditor should check whether the row's local proof inputs are now the narrow colour-sector suppliers rather than the broad full-closure parents."
```

This block moves the source-side dependency boundary for the local SU(3)^3
trace. It does not close full one-generation matter closure, branch selection,
chirality/time selection, or hypercharge uniqueness.

## Commands run

```bash
python3 scripts/frontier_su3_cubic_anomaly_cancellation.py
python3 scripts/cached_runner_output.py scripts/frontier_su3_cubic_anomaly_cancellation.py --refresh
```

## Results

- SU(3)^3 source-side verifier: `TOTAL: PASS=42, FAIL=0`
- Runner cache refresh: `status: ok`
