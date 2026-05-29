# Handoff

This branch repairs the existing unaudited source-resolved propagating Green
pocket by adding hard assertions to the registered runner, narrowing the source
note away from branch-local retained language, and removing non-load-bearing
sibling links from the source-resolved Green dependency chain.

Verification:

```text
python3 -m py_compile scripts/source_resolved_propagating_green_pocket.py
python3 scripts/source_resolved_propagating_green_pocket.py
bash docs/audit/scripts/run_pipeline.sh
git diff --check
```

Key runner readout:

```text
zero-source dynamic shift: +0.000000e+00
propagating Green F~M exponent: 1.00
TOWARD rows: 4/4
mean |prop/inst| ratio: 1.420
mean |prop/green| ratio: 1.149
causal memory observable (prop - green): +1.197212e-03
ASSERTIONS: PASS
```

Audit queue readout after regeneration:

```text
source_resolved_exact_green_pocket_note: ready=true, rank=248, deps=[minimal_source_driven_field_probe_note]
source_resolved_propagating_green_pocket_note: ready=true, rank=249, deps=[minimal_source_driven_field_probe_note]
```

Next action: reviewer/auditor should inspect
`source_resolved_exact_green_pocket_note` and then
`source_resolved_propagating_green_pocket_note`.
