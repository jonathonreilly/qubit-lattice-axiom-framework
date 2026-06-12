# Handoff

## Summary

This PR repairs the audited-conditional reconstructed-H microcausality bridge row by narrowing the
source artifact to the result it actually proves: an axis-kernel support theorem for
`H_axis(x)=H(x,0,0)` on the free `U=1`, `m > 0` surface.

## Changed

- Replaced broad "free surface closes the finite-range-H step" wording with axis-kernel support.
- Removed stale parent Lieb-Robinson constant language from the claimed theorem.
- Weakened the rate claim to a positive axis strip bound.
- Updated the verifier and cache to state the same scope.

## Verification

```bash
python3 scripts/reconstructed_h_quasilocal_microcausality_bridge_runner.py
python3 scripts/precompute_audit_runners.py --runners scripts/reconstructed_h_quasilocal_microcausality_bridge_runner.py --force --concurrency 1 --push-mode none --allow-non-main
```

Results:

- `PASS=8 FAIL=0`
- runner cache refreshed successfully

## Boundaries

- No audit ledger edits.
- No new axiom.
- No retained-status claim.
- Full off-axis/free d-dimensional and interacting quasi-locality remain open.

PR: pending
