# Claim Status Certificate

## Target

- `claim_id`: `assumption_derivation_ledger`
- `note_path`: `docs/ASSUMPTION_DERIVATION_LEDGER.md`
- `claim_type`: `bounded_theorem`
- `criticality`: `critical`
- `transitive_descendants`: `880`
- `direct_in_degree`: `8`

## Repair

The source now binds only the directly cited R_conn authority slice:

```text
F_adj = dim(su(3)) / dim(M_3(C)) = 8/9.
```

The repaired note states that physical `R_conn`, physical `K_EW = 9/8`, and the
selector `kappa_EW = 0` remain conditional on a separate selector theorem or
exact disconnected-current coefficient computation.

The former package-wide table is removed from the row's binding scope.

## Queue Result

After the deterministic audit pipeline:

```text
audit_status: unaudited
effective_status: unaudited
ready: true
deps: [rconn_derived_note]
queue_reason: unaudited
```

This is the intended result: ready for independent re-audit, not retagged by
the author.
