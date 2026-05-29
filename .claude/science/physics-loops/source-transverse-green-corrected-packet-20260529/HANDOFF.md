# Handoff

This branch adds a fresh source-resolved transverse Green corrected boundary
packet. It does not relabel the archived failed row.

Verification:

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

Next action: reviewer/auditor should inspect the new row
`source_resolved_transverse_green_corrected_boundary_note_2026-05-29`.
