# Handoff

## Summary

This branch repairs the displayed PDG phase-gap arithmetic in the charged-lepton
Brannen/BAE `delta=2/9` open-gate note.

The paired runner already reports:

```text
delta_PDG = 0.222270487540236
delta_PDG - 2/9 = 0.000048265318014
```

The source note previously displayed `0.000047...`; this branch updates it to
`0.000048265...` and reiterates that the value is comparator arithmetic only.

## Verification

```bash
PYTHONPATH=scripts python3 scripts/frontier_lepton_brannen_bae_delta_two_ninths_open_gate.py
python3 scripts/cached_runner_output.py --check-only scripts/frontier_lepton_brannen_bae_delta_two_ninths_open_gate.py
git diff --check
```

Expected runner summary: `PASS=17 FAIL=0`.

## Remaining Open Gates

- Derive or admit `delta=2/9`.
- Derive or admit the `sqrt(2)` Brannen/BAE coefficient.
- Derive the dimensionful charged-lepton scale.
- Re-audit independently before any status change.
