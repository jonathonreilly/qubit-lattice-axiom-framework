## Summary

This PR repairs the Planck coframe accepted-premise bridge by narrowing the daggered CAR statement to a compatible Hermitian Pauli-realization existence statement, B4'.

It addresses the audit blocker without adding a new axiom or Hermitian premise. The runner now includes a nonunitary-similarity boundary witness showing why the old fixed-inner-product daggered CAR claim was too broad.

## Changes

- Updates `docs/PLANCK_TARGET3_COFRAME_RESPONSE_ACCEPTED_PREMISE_BRIDGE_BOUNDED_NOTE_2026-05-26.md`.
- Updates `scripts/planck_target3_coframe_response_accepted_premise_runner.py`.
- Regenerates audit queue/ledger surfaces so the row is re-auditable.
- Adds the physics-loop handoff pack.

## Audit Queue

`bash docs/audit/scripts/run_pipeline.sh`:

- row: `planck_target3_coframe_response_accepted_premise_bridge_bounded_note_2026-05-26`
- status after edit: `unaudited`
- queue rank: 905
- ready: true
- open dependencies: none

No ledger verdict is manually retagged.

## Verification

```text
python3 -m py_compile scripts/planck_target3_coframe_response_accepted_premise_runner.py
PYTHONPATH=scripts python3 scripts/planck_target3_coframe_response_accepted_premise_runner.py
bash docs/audit/scripts/run_pipeline.sh
git diff --check
```
