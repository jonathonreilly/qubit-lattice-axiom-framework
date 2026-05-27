# Handoff

## What Changed

- Replaced the broad `docs/ASSUMPTION_DERIVATION_LEDGER.md` package table with
  a narrow R_conn/F_adj authority slice.
- Kept only the one-hop dependency already declared by the row:
  `docs/RCONN_DERIVED_NOTE.md`.
- Preserved the current science boundary: `F_adj = 8/9` is exact algebra;
  physical `R_conn` and `K_EW = 9/8` are not unconditional claims.
- Re-ran the audit pipeline, which reset the changed row to `unaudited` and put
  it in the queue with `ready: true`.

## Review Focus

Check that the repaired row does not make package-wide status claims and does
not imply a physical EW-current selector. The intended re-audit question is
whether this reduced row is now valid as a bounded support/status note under
its one-hop dependency.

## Verification

```text
python3 scripts/vocab_lint.py --report-only docs/ASSUMPTION_DERIVATION_LEDGER.md
python3 scripts/rconn_matching_rule_nogo_certificate.py
bash docs/audit/scripts/run_pipeline.sh
```
