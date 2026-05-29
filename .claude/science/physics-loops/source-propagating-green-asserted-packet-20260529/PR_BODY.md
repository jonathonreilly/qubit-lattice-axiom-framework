## Summary

Repairs the existing unaudited source-resolved propagating Green pocket by
adding hard assertions to the registered runner and narrowing the note status
to bounded-support pending independent audit. It also removes non-load-bearing
sibling note links from the source-resolved Green dependency chain, leaving the
retained-bounded minimal source-driven probe as the load-bearing upstream
authority.

## Science Boundary

- no new axioms
- no observed target values
- no fitted selectors
- no external comparator
- no transverse transport or finite-speed field-equation claim
- no generated-family transfer claim
- no audit-ratified status claim

## Artifacts

- `docs/SOURCE_RESOLVED_PROPAGATING_GREEN_POCKET_NOTE.md`
- `docs/SOURCE_RESOLVED_EXACT_GREEN_POCKET_NOTE.md`
- `scripts/source_resolved_propagating_green_pocket.py`
- `.claude/science/physics-loops/source-propagating-green-asserted-packet-20260529/HANDOFF.md`
- `.claude/science/physics-loops/source-propagating-green-asserted-packet-20260529/TRACE_GATE.md`
- `.claude/science/physics-loops/source-propagating-green-asserted-packet-20260529/CLAIM_STATUS_CERTIFICATE.md`

## Verification

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
