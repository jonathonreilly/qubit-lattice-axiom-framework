# Static-Source I1 Green-Native Dependency Handoff

## Target

`static_source_readout_i1_accepted_premise_bridge_bounded_note_2026-05-27`

## Repair Summary

The I1 bridge still registers the static-source linear-response readout
convention as the admitted P1. This repair does not change that boundary.

The repair replaces the Green-kernel input M1. Instead of consuming
`G(r) -> 1/(4 pi |r|)` through the historical sibling Maradudin
accepted-premise bridge, the note and runner now consume the framework-local
`Z^3` graph-Laplacian Green theorem and its normalization certificate.

## Verification

```text
PYTHONPATH=scripts python3 scripts/static_source_readout_i1_accepted_premise_runner.py
python3 scripts/cached_runner_output.py --check-only scripts/static_source_readout_i1_accepted_premise_runner.py
python3 -m py_compile scripts/static_source_readout_i1_accepted_premise_runner.py
git diff --check
git diff --name-only -- docs/audit
```

Latest runner result: `TOTAL: PASS=55 FAIL=0`.
