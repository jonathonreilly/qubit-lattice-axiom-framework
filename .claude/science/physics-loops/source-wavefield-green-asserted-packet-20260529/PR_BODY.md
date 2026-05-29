## Summary

Repairs the existing unaudited source-resolved wavefield Green pocket by adding
hard assertions to the registered runner and narrowing the note status to
bounded-support pending independent audit. It also removes non-load-bearing
sibling note links, leaving the retained-bounded minimal source-driven probe as
the load-bearing upstream authority.

## Science Boundary

- no new axioms
- no observed target values
- no fitted selectors
- no external comparator
- no continuum retarded-gravity claim
- no generated-family transfer claim
- no audit-ratified status claim

## Artifacts

- `docs/SOURCE_RESOLVED_WAVEFIELD_GREEN_POCKET_NOTE.md`
- `scripts/source_resolved_wavefield_green_pocket.py`
- `.claude/science/physics-loops/source-wavefield-green-asserted-packet-20260529/HANDOFF.md`
- `.claude/science/physics-loops/source-wavefield-green-asserted-packet-20260529/TRACE_GATE.md`
- `.claude/science/physics-loops/source-wavefield-green-asserted-packet-20260529/CLAIM_STATUS_CERTIFICATE.md`

## Verification

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
