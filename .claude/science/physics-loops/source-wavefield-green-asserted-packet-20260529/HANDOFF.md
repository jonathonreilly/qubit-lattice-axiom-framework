# Handoff

This branch repairs the existing unaudited source-resolved wavefield Green
pocket by adding hard assertions to the registered runner, narrowing the source
note away from branch-local retained language, and removing non-load-bearing
sibling links from the dependency graph.

Verification:

```text
python3 -m py_compile scripts/source_resolved_wavefield_green_pocket.py
python3 scripts/source_resolved_wavefield_green_pocket.py
bash docs/audit/scripts/run_pipeline.sh
git diff --check
```

Key runner readout:

```text
zero-source same-site shift: +0.000000e+00
zero-source wavefield shift: +0.000000e+00
wavefield F~M exponent: 0.99
TOWARD rows: 4/4
mean absolute detector phase lag: 1.457 rad
mean detector overlap with same-site baseline: 0.827
mean |wave/same| ratio: 33.732
ASSERTIONS: PASS
```

Audit queue readout after pipeline regeneration:

```text
source_resolved_wavefield_green_pocket_note
rank: 244
ready: true
queue_reason: unaudited
criticality: high
deps: [minimal_source_driven_field_probe_note]
```

Next action: reviewer/auditor should inspect
`source_resolved_wavefield_green_pocket_note`.
