# Lattice-Greens Maradudin Native Reroute Handoff

## Target

`lattice_greens_maradudin_asymptotic_accepted_premise_bridge_bounded_note_2026-05-27`

## Repair Summary

The source note no longer treats the Maradudin-Montroll-Weiss / Lawler /
Spitzer result as a load-bearing supplied premise. It now routes the legacy
bridge through the parent framework-local `Z^3` nearest-neighbor
graph-Laplacian Green-kernel proof, with textbook references kept as parallel
provenance.

The paired runner now checks that source contract and rejects the old
accepted-premise/admitted-import wording while replaying the symbol,
unit-flux, residual, and coefficient checks.

## Verification

```text
PYTHONPATH=scripts python3 scripts/lattice_greens_maradudin_asymptotic_accepted_premise_runner.py
python3 -m py_compile scripts/lattice_greens_maradudin_asymptotic_accepted_premise_runner.py
```

Latest runner result: `TOTAL: PASS=76 FAIL=0`.
