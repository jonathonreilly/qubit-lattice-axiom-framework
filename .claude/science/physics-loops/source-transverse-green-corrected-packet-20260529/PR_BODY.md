## Summary

Adds a fresh bounded-support source-resolved transverse Green corrected
boundary packet. The archived transverse row failed because the live runner
contradicts the positive `trans - same` headline and its printed `trans/same`
column is actually `trans/inst`. This branch recomputes the ratios directly
and submits only the checked finite boundary as a new unaudited row.

## Science Boundary

- no new axioms
- no observed target values
- no fitted selectors
- no external comparator
- no positive same-site centroid-correction claim
- no full transverse field-equation claim
- no audit-ratified status claim

## Artifacts

- `docs/SOURCE_RESOLVED_TRANSVERSE_GREEN_CORRECTED_BOUNDARY_NOTE_2026-05-29.md`
- `scripts/source_resolved_transverse_green_corrected_boundary_check.py`
- `.claude/science/physics-loops/source-transverse-green-corrected-packet-20260529/HANDOFF.md`
- `.claude/science/physics-loops/source-transverse-green-corrected-packet-20260529/TRACE_GATE.md`
- `.claude/science/physics-loops/source-transverse-green-corrected-packet-20260529/CLAIM_STATUS_CERTIFICATE.md`

## Verification

```text
python3 -m py_compile scripts/source_resolved_transverse_green_corrected_boundary_check.py
python3 scripts/source_resolved_transverse_green_corrected_boundary_check.py
bash docs/audit/scripts/run_pipeline.sh
git diff --check
```

Key runner readout:

```text
mean trans/inst ratio: 1.162
corrected mean trans/same ratio: 0.990
mean trans-same centroid shift: -8.676e-05
mean support-fraction delta: +0.000e+00
mean N_eff delta: +3.697e-03
exponents inst/same/trans: 1.00/1.00/1.00
TOWARD rows: 4/4
ASSERTIONS: PASS
```
