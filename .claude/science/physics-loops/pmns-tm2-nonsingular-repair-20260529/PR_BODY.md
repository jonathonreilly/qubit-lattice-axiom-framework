## Summary

This PR repairs the audited conditional PMNS TM2 row by narrowing the maximal-CP consequence to the nonsingular phase chamber `c12*s12*s13 != 0`.

It addresses the exact audit blocker: at `sin^2(theta_13)=2/3`, TM2 gives `c12=0`, so the CP equation is satisfied for any `delta_CP` and maximal CP is not forced.

## Changes

- Updates `docs/PMNS_TM2_RESIDUAL_CONSEQUENCE_BOUNDED_NOTE_2026-05-26.md` to state the nonsingular chamber explicitly.
- Updates `scripts/pmns_tm2_residual_consequence_runner.py` with endpoint and divisor checks.
- Regenerates audit queue/ledger surfaces so the row is re-auditable.
- Adds the physics-loop handoff pack.

## Audit Queue

`bash docs/audit/scripts/run_pipeline.sh`:

- row: `pmns_tm2_residual_consequence_bounded_note_2026-05-26`
- status after edit: `unaudited`
- queue rank: 907
- ready: true
- open dependencies: none

No ledger verdict is manually retagged.

## Verification

```text
python3 -m py_compile scripts/pmns_tm2_residual_consequence_runner.py
PYTHONPATH=scripts python3 scripts/pmns_tm2_residual_consequence_runner.py
bash docs/audit/scripts/run_pipeline.sh
git diff --check
```
