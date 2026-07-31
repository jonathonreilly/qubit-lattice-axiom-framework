# Artifact Plan

- Align cached runner-output transport with `RUNNER_STDOUT_CHAR_LIMIT`.
- Add a 20,000-character override for the exact Koide target/authority pair.
- Add a regression test using the real target row, authority bytes, runner
  cache, and evidence manifest.
- Add a dated transport-only record to the target note so its own hash drift
  requeues the exact terminal non-clean row without an audit-owned sidecar.
- Confirm every load-bearing evidence role is free of clipping markers.
- Run the unchanged primary runner and verify cache freshness.
- Run review-loop and hand off to independent audit without editing
  auditor-owned ledger outputs.
