# Lattice-Greens Maradudin Native Reroute Handoff

## Target

`lattice_greens_maradudin_asymptotic_accepted_premise_bridge_bounded_note_2026-05-27`

Secondary same-lane cleanup:

`lattice_greens_1_over_r_from_heat_kernel_resolvent_theorem_note_2026-06-07`

## Repair Summary

The source note no longer treats the Maradudin-Montroll-Weiss / Lawler /
Spitzer result as a load-bearing supplied premise. It now routes the legacy
bridge through the parent framework-local `Z^3` nearest-neighbor
graph-Laplacian Green-kernel proof, with textbook references kept as parallel
provenance.

The paired runner now checks that source contract and rejects the old
accepted-premise/admitted-import wording while replaying the symbol,
unit-flux, residual, and coefficient checks.

The adjacent heat-kernel resolvent note also no longer describes its leading
term through accepted-premise textbook-import wording. Its summary and audit
registration now point to the stronger framework-native lattice-correction
theorem as the load-bearing leading-term route, while keeping the direct
local-CLT route open as an alternate proof.

## Verification

```text
PYTHONPATH=scripts python3 scripts/lattice_greens_maradudin_asymptotic_accepted_premise_runner.py
python3 -m py_compile scripts/lattice_greens_maradudin_asymptotic_accepted_premise_runner.py
python3 scripts/frontier_lattice_greens_1_over_r_from_heat_kernel_resolvent.py
python3 scripts/cached_runner_output.py --refresh scripts/frontier_lattice_greens_1_over_r_from_heat_kernel_resolvent.py
python3 -m py_compile scripts/frontier_lattice_greens_1_over_r_from_heat_kernel_resolvent.py
```

Latest runner result: `TOTAL: PASS=76 FAIL=0`.
Latest heat-kernel runner result: `TOTAL: PASS=20 FAIL=0`.
