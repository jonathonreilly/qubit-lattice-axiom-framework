# Handoff

## Summary

This PR repairs the conditional Koide APS fixed-locus row by taking the audit's
allowed narrowing route: the row now claims only the closed A/B theorem.

Claim retained in scope:

- C3[111] fixed-locus structure forces `p=3`;
- transverse weights are `(1,2)`;
- `(1,2)` is the unique trace-free pair;
- local density `L_3(1,2) = 2/9`.

Removed from claim scope:

- local ABSS applicability;
- global `Cl(3)/Z^3 -> PL S^3 x R`;
- parent APS block-by-block closure.

Those are kept only as boundary diagnostics and future bridge work.

## Verification

```text
python3 scripts/audit_companion_koide_aps_c3_fixed_locus_weights_2026_06_05.py
TOTAL: 25 PASS / 0 FAIL
```

```text
python3 scripts/precompute_audit_runners.py --runners scripts/audit_companion_koide_aps_c3_fixed_locus_weights_2026_06_05.py --check-only --allow-non-main
All relevant caches are fresh.
```

## Boundaries

- No new axioms.
- No audit ledger/result edits.
- No parent-row promotion.
- Global PL S3 x R identification remains open frontier work.
