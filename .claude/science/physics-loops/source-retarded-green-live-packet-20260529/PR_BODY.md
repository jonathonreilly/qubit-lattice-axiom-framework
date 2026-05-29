## Summary

Adds a fresh bounded-support source-resolved retarded Green corrected packet.
The archived source-resolved retarded row failed because its printed `ret/same`
column was actually `ret/inst`; this branch does not relabel that row. It
recomputes the same-site comparison directly from live helper functions and
submits the corrected finite packet as a new unaudited queue-ready row.

## Science Boundary

- no new axioms
- no observed target values
- no fitted selectors
- no external comparator
- no full retarded field equation claim
- no audit-ratified status claim

## Artifacts

- `docs/SOURCE_RESOLVED_RETARDED_GREEN_CORRECTED_PACKET_NOTE_2026-05-29.md`
- `scripts/source_resolved_retarded_green_corrected_packet_check.py`
- `.claude/science/physics-loops/source-retarded-green-live-packet-20260529/HANDOFF.md`
- `.claude/science/physics-loops/source-retarded-green-live-packet-20260529/TRACE_GATE.md`
- `.claude/science/physics-loops/source-retarded-green-live-packet-20260529/CLAIM_STATUS_CERTIFICATE.md`

## Verification

```text
python3 -m py_compile scripts/source_resolved_retarded_green_corrected_packet_check.py
python3 scripts/source_resolved_retarded_green_corrected_packet_check.py
bash docs/audit/scripts/run_pipeline.sh
git diff --check
```

Key runner readout:

```text
corrected mean ret/same ratio: 1.026
mean ret-same support delta: +0.000e+00
mean ret-same N_eff delta: +4.493e-02
exponents inst/same/ret: 1.00/1.00/1.00
TOWARD rows: 4/4
ASSERTIONS: PASS
```

Audit queue readout:

```text
claim_id: source_resolved_retarded_green_corrected_packet_note_2026-05-29
status: unaudited
ready: true
rank: 911
deps: []
```
