# PR Backlog

## Block101

- Branch: `physics-loop/audit-unblock-block101-20260620`
- Base: `main`
- Status: pending feature-branch push
- PR URL: pending
- Title:
  `[physics-loop][review-loop] audit-unblock block101: bounded-support source measure trace prototype`

## Body

This PR unblocks the audit queue for
`post_record_source_measure_trace_normalization_prototype_2026-06-06` by
repairing source-side boundaries and current row-count checks.

### Source-Side Change

- `docs/POST_RECORD_SOURCE_MEASURE_TRACE_NORMALIZATION_PROTOTYPE_2026-06-06.md`
  now uses `**Claim type:** bounded_theorem`.
- The note and runner now use the current measure/weight subdivision snapshot:
  `16` `source_measure_or_rn_bridge` rows plus `10`
  `trace_normalization_reference` rows, `26` source/trace rows total.
- The existing boundaries remain: supplied finite semantics, no physical
  reference identification, no Record-derived measure/prior/source law/Born
  law/selector, no dial selection, and no audit verdict application.

### Target Before/After

- Before: `claim_type=positive_theorem`,
  `claim_type_author_hint_raw="methodology / positive theorem"`,
  `audit_status=audited_clean`, `effective_status=retained`.
- After: `claim_type=bounded_theorem`,
  `claim_type_provenance=author_hint`, `audit_status=unaudited`,
  `effective_status=unaudited`, `ready=true`.
- Prior audits are retained in `previous_audits`; they are not active for the
  new note/runner hashes.

### Verification

- `python3 -m py_compile scripts/frontier_post_record_source_measure_trace_normalization_prototype_2026_06_06.py`
- `python3 scripts/frontier_post_record_source_measure_trace_normalization_prototype_2026_06_06.py`
  - `SUMMARY: PASS=49 FAIL=0`
- `python3 scripts/precompute_audit_runners.py --runners scripts/frontier_post_record_source_measure_trace_normalization_prototype_2026_06_06.py --force --push-mode none --allow-non-main`
- `python3 scripts/audit_packet_script_deps.py`
- `bash docs/audit/scripts/run_pipeline.sh`
- `python3 docs/audit/scripts/audit_lint.py --strict`
  - `OK: no errors`

### Packet

- `.claude/science/physics-loops/audit-unblock-20260619/HANDOFF.md`
- `.claude/science/physics-loops/audit-unblock-20260619/TRACE_GATE.md`
- `.claude/science/physics-loops/audit-unblock-20260619/CLAIM_STATUS_CERTIFICATE.md`
- `.claude/science/physics-loops/audit-unblock-20260619/REVIEW_HISTORY.md`

### Boundaries

- No audit-loop run.
- No audit verdict applied or predicted.
- No push to `main`.
- No README, lane registry, active review queue, or source publication-control
  weaving.

