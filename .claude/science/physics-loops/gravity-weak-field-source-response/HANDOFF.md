# Handoff

## Science Move

Created a new weak-field source-response bridge for the gravity clean chain.
The theorem uses the quadratic source action

```text
A[phi;rho] = 1/2 <phi,H phi> - <P0 rho,phi>
```

on `H=-Delta_lat` to derive the Euler equation `H phi=P0 rho`, the Green
solution `phi=G0 P0 rho`, and therefore `L^{-1}=G0` on the neutral weak-field
sector. It also proves that the unique local phase-invariant normalized
quadratic density is `rho=|psi|^2`, and that a test source coupled by the same
source action has first-order response `S=L(1-phi)`.

## Verification

- `PYTHONPATH=scripts python3 scripts/frontier_gravity_weak_field_source_response_bridge_2026_06_11.py`
  -> `TOTAL: PASS=38 FAIL=0`
- `python3 scripts/precompute_audit_runners.py --runners scripts/frontier_gravity_weak_field_source_response_bridge_2026_06_11.py --force --push-mode=none`
  -> OK
- `bash docs/audit/scripts/run_pipeline.sh`
  -> pass; cycles 0; ready rows 26
- `python3 docs/audit/scripts/audit_lint.py --strict`
  -> OK, notices only
- `git diff --check`
  -> pass

Generated audit/status/publication outputs were restored before commit.

## Audit Routing

Pipeline showed the new bridge row as:

```text
gravity_weak_field_source_response_bridge_bounded_theorem_note_2026-06-11
audit_status: unaudited
effective_status: unaudited
criticality: critical
notes_for_re_audit_if_any: None
```

`gravity_clean_derivation_note` also reset to `unaudited` with no
`notes_for_re_audit_if_any`, but it depends on this new bridge. The correct
audit order is bridge first, then the consumer.
