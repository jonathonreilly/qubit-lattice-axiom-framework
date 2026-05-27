## Summary

PR: https://github.com/jonathonreilly/qubit-lattice-axiom-framework/pull/2070

Repairs `assumption_derivation_ledger` by narrowing it from a broad package
status table to the one directly supported authority slice:

```text
F_adj = dim(su(3)) / dim(M_3(C)) = 8/9.
```

The repaired note keeps physical `R_conn`, physical `K_EW = 9/8`, and the
selector `kappa_EW = 0` behind the existing selector/readout boundary from
`RCONN_DERIVED_NOTE.md`. It removes the old package-wide status rows from this
row's binding claim rather than adding unsupported one-hop authority.

## Audit Surface

- Target row: `assumption_derivation_ledger`
- Dependency surface: `rconn_derived_note`
- After pipeline: `audit_status=unaudited`, `effective_status=unaudited`,
  `ready=true`
- No new axiom, selector, fitted convention, or audit verdict.

## Verification

```text
python3 scripts/vocab_lint.py --report-only docs/ASSUMPTION_DERIVATION_LEDGER.md
python3 scripts/rconn_matching_rule_nogo_certificate.py
bash docs/audit/scripts/run_pipeline.sh
git diff --check
```
