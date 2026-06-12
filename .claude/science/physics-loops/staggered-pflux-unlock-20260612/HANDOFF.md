# Handoff

## What Changed

- FSB-K now routes its one-qubit single-ladder surface through current
  framework-native sources and the retained tensor-product/translation bridge,
  not through the old U4 qubit-reframe row.
- The P-FLUX composer now consumes the Z certificate as retained geometry and
  leaves FSB-K as the sole open condition C1.
- The composer runner recomputes the K1/K0 discriminating data and enforces the
  current ledger boundary: C1 unaudited, Z retained, no selection at current
  grades.

## Why It Matters

This is the highest-leverage available unlock because it turns the P-FLUX
selection path from "two open conditions plus stale U4 risk" into "one open
condition plus retained geometry." If FSB-K passes audit, the downstream
composer has a deterministic route to supply B-Z2 and retire B-BIT within the
licensed two-class surface.

## Remaining Work

- Audit/review FSB-K.
- Audit/review the kinetic-class forcing row if the goal is wholesale P-KIN
  closure rather than selection within the two-class surface.
- Do not land this as an audit verdict; the reviewer/auditor owns status.

## Verification

- `python3 scripts/frontier_axiom_first_fermionic_stefan_boltzmann_narrow.py`
  returned `TOTAL: PASS=18 FAIL=0`.
- `python3 scripts/p_flux_selection_via_fsb_k_check_2026_06_11.py`
  returned `TOTAL: PASS=16 FAIL=0`.
