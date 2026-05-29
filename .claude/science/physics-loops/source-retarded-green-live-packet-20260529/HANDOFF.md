# Handoff

This branch adds a fresh source-resolved retarded Green corrected packet. It
does not relabel the archived failed row.

Verification:

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

Next action: reviewer/auditor should inspect the new row
`source_resolved_retarded_green_corrected_packet_note_2026-05-29` and decide
whether/how to extract the science.
