# Handoff

## What Changed

This branch repairs the Noether onsite/internal row by making the load-bearing surface explicit:

```text
retained abstract bilinear continuity theorem
+ finite coefficient/Fock replay
```

The runner's staggered-form matrix is treated as an explicit finite coefficient exhibit. The physical staggered/Kawamoto-Smit realization gate remains open context and is no longer a markdown dependency edge of the source note.

## Verification

- `PYTHONPATH=scripts python3 scripts/audit_companion_lattice_noether_onsite_internal_2026_06_05.py`
  - `TOTAL: 14 PASS / 0 FAIL`
- `python3 scripts/precompute_audit_runners.py --runners scripts/audit_companion_lattice_noether_onsite_internal_2026_06_05.py --force --concurrency 1 --push-mode none --allow-non-main`
  - `ok 1`, `nonzero_exit 0`

## Boundaries

- No ledger edits.
- No audit verdict/status assertion.
- Does not derive the physical staggered-Dirac carrier.
- Does not derive a physical density/readout bridge beyond the finite Fock surface.
- Does not close site-mixing currents.
- Does not add or change axioms.
