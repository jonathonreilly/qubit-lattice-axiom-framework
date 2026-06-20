# PR Body

## Summary

This PR unblocks audit-packet completeness infrastructure. The audit citation
graph now treats `_frontier_loader.load_frontier(..., "X.py")` dynamic loads
as helper runner sources, including both positional and `filename=` keyword
forms.

This is not a source science claim, not an audit verdict, and not
retained-status work. It only makes packet construction see the helper paths
that queued runners already load dynamically.

## Audit-unblock impact

Before the patch, the diagnostic resolver found queued helper dependencies
that were not represented in `helper_runner_paths`. After the patch, the
queued parity check is zero:

- `queue_deps_not_in_helper_runner_paths = 0`
- `ledger_deps_not_in_helper_runner_paths = 3`

The remaining three ledger mismatches are terminal non-queued rows:
`causal_propagating_field_note`, `portable_card_extension_note`, and
`shapiro_five_family_portability_note`. Each is already `audited_failed` /
`retained_no_go` and is not in the audit queue.

The packet dependency diagnostic still reports `387 / 1579` pending claims
with helper imports. Those queued helper paths are now visible in
`helper_runner_paths` for packet builders instead of being silently omitted by
the graph parser.

## Boundary

- No audit-loop run.
- No audit verdicts applied.
- No effective-status promotion.
- No source science claim added.
- Generated audit/publication artifacts are pipeline outputs from current
  main state.
- Repo automation lock remains unavailable with the known `/Users/jonreilly`
  permission failure; this block used a degraded branch-local lock.

## Verification

- `python3 -m py_compile docs/audit/scripts/build_citation_graph.py docs/audit/scripts/tests/test_audit_pipeline.py`
- `python3 -m unittest docs.audit.scripts.tests.test_audit_pipeline.BuildCitationGraphParserTest`: 6 tests OK
- `bash docs/audit/scripts/run_pipeline.sh`: complete; strict lint reported 139 notices, 0 errors
- `python3 scripts/audit_packet_script_deps.py`: pending claims with helper imports 387 / 1579
- parity check: `queue_deps_not_in_helper_runner_paths = 0`; `ledger_deps_not_in_helper_runner_paths = 3` terminal non-queued rows
- `python3 docs/audit/scripts/audit_lint.py --strict`: 139 notices, 0 errors
- `git diff --check`
- post-commit generated-clean check: clean
