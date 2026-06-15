# Handoff

## What changed

The P-FLUX / FSB-K composer note and runner were synchronized to current main, where FSB-K is now `audited_clean` / `retained_bounded` and the Z certificate is retained.

The repair removes the stale "C1 unaudited / no selection today" framing and replaces it with:

- C1 is consumed at current `retained_bounded` grade.
- The source-side selection is active within the licensed two-class K0/K1 surface.
- The composer row's own verdict and effective status remain audit-owned.

## Why this matters

The audit blocker for the composer was that FSB-K needed to reach retained grade with the realized-kernel quantifier and FSB-CL intact. Current main now has that upstream grade. This PR makes the source artifact re-auditable against that new fact without editing audit data.

## Verification

`python3 scripts/p_flux_selection_via_fsb_k_check_2026_06_11.py`

Result: `TOTAL: PASS=16 FAIL=0`

`PYTHONPATH=scripts python3 scripts/precompute_audit_runners.py --runners scripts/p_flux_selection_via_fsb_k_check_2026_06_11.py --check-only --allow-non-main`

Result: all relevant caches fresh.
