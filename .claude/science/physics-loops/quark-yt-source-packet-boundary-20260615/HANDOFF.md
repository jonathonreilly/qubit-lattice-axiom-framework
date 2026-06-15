# Handoff

This PR is a clean source-side replacement for the quark/YT parts of old dirty
repair work. It does not include audit-result files.

## Verification

```bash
python3 scripts/frontier_quark_route2_source_domain_bridge_no_go.py
python3 scripts/frontier_yt_boundary_bc_transfer_uniqueness.py
python3 scripts/precompute_audit_runners.py --runners scripts/frontier_quark_route2_source_domain_bridge_no_go.py,scripts/frontier_yt_boundary_bc_transfer_uniqueness.py --force --push-mode none
python3 scripts/precompute_audit_runners.py --runners scripts/frontier_quark_route2_source_domain_bridge_no_go.py,scripts/frontier_yt_boundary_bc_transfer_uniqueness.py --check-only
python3 docs/audit/scripts/audit_lint.py --strict
git diff --check
```

Expected runner scorecards:

- `TOTAL: PASS=104, FAIL=0`
- `Counts: 29 PASS, 0 FAIL`

## Reviewer Notes

- Treat this as bounded-support/source-boundary cleanup.
- Do not infer retained promotion from the branch.
- If accepted, the audit lane can re-evaluate the affected conditional rows.
