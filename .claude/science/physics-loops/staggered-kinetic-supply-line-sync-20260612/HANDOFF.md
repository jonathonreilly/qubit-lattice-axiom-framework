# Handoff

## What Changed

This branch updates three staggered/Noether consumer notes to expose the
current kinetic supply line on main:

```text
kinetic-class forcing
  -> P-SD discharged on K1
  -> P-KIN reduced to P-FLUX
  -> P-FLUX conditionally selected by FSB-K + retained Z
```

It adds a verifier and cached output checking that the source notes,
supplier caches, and status firewalls all agree.

## What This Unlocks

The old audit blocker was too broad: "derive P-KIN/P-SD" or "close the
full carrier." After this branch, re-audit can focus on the sharper
remaining chain: supplier audits plus FSB-K for P-FLUX.

## What This Does Not Do

- It does not edit audit ledgers.
- It does not claim retained closure.
- It does not remove the FSB-K condition.
- It does not promote Noether, Kawamoto-Smit, or the realization gate.

## Verification

- `python3 scripts/staggered_dirac_kinetic_supply_line_sync_2026_06_12.py`
  -> `TOTAL: PASS=53 FAIL=0`
- `python3 scripts/precompute_audit_runners.py --runners scripts/staggered_dirac_kinetic_supply_line_sync_2026_06_12.py --force --concurrency 1 --push-mode none --allow-non-main`
  -> `ok 1`

## Next Exact Action

If this PR passes review, audit can reconsider the consumer rows against
the sharper dependency chain. The highest leverage next science work is
the FSB-K condition, because it is the remaining conditional leg in the
P-FLUX selector.
