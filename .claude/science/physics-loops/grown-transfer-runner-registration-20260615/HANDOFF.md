# Handoff

This block repairs a source registration issue for the currently ready audit
row `grown_transfer_basin_targeted_repair_note_2026-06-04`.

Before this PR, the source note listed the targeted/sweep runner packet, but
the generated citation graph recorded `runner_path: null`. The note now has an
explicit primary-runner line for `scripts/GROWN_TRANSFER_BASIN_TARGETED.py`.
That runner imports `scripts/GROWN_TRANSFER_BASIN_SWEEP.py`, which imports the
grown-geometry helper, so the packet builder can expose the executable chain.

No audit verdicts or generated audit artifacts should be landed from this PR.
The reviewer should re-run the audit pipeline and then audit/review the ready
row through the normal loop.

Local disposable pipeline result:

- `citation_graph.json`, `audit_ledger.json`, and `audit_queue.json` all resolve
  the row's `runner_path` to `scripts/GROWN_TRANSFER_BASIN_TARGETED.py`.
- The generated helper runner paths are `scripts/GROWN_TRANSFER_BASIN_SWEEP.py`
  and `scripts/gate_b_grown_joint_package.py`.
- Generated audit files were restored before commit.
