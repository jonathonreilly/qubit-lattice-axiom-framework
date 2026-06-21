## Summary

Adds and registers a bounded note-boundary verifier for `continuum_convergence_note`.

This is source-side audit-unblock work only. The target remains:

- `audit_status: unaudited`
- `effective_status: unaudited`
- `claim_type: bounded_theorem`

The new runner checks the note boundary, verifies the finite tail-stats dependency, verifies the transfer-norm discriminator dependency, and keeps the continuum/kernel-selection overclaims out of scope.

## Artifacts

- Source note: `docs/CONTINUUM_CONVERGENCE_NOTE.md`
- Runner: `scripts/continuum_convergence_note_probe.py`
- Runner cache: `logs/runner-cache/continuum_convergence_note_probe.txt`
- Loop pack: `.claude/science/physics-loops/audit-unblock-block145-20260621/`
- Generated surfaces:
  - `docs/audit/AUDIT_LEDGER.md`
  - `docs/audit/data/audit_ledger.json`
  - `docs/audit/data/audit_queue.json`
  - `docs/audit/data/citation_graph.json`
  - `docs/audit/data/runner_classification.json`

## Verification

- `python3 scripts/continuum_convergence_note_probe.py`
  - `SUMMARY: PASS=15 FAIL=0`
- `python3 scripts/lattice_3d_l2_tail_stats.py`
  - `SCORECARD PASS=32 FAIL=0`
- `python3 scripts/lattice_kernel_transfer_norm_probe.py`
  - p=1.50 ranked closest to measured-norm marginality; p=2.00 next
- `bash docs/audit/scripts/run_pipeline.sh`
  - completed with no invalidations
- `python3 scripts/precompute_audit_runners.py --runners scripts/continuum_convergence_note_probe.py --push-mode none --allow-non-main`
  - refreshed runner cache
- `python3 scripts/precompute_audit_runners.py --runners scripts/continuum_convergence_note_probe.py --check-only --push-mode none --allow-non-main`
  - all relevant caches fresh
- `python3 docs/audit/scripts/audit_lint.py --strict`
  - `3474 rows checked`; `139 notices`; `OK: no errors`
- `python3 -m py_compile scripts/continuum_convergence_note_probe.py scripts/lattice_3d_l2_tail_stats.py scripts/lattice_kernel_transfer_norm_probe.py docs/audit/scripts/build_citation_graph.py docs/audit/scripts/seed_audit_ledger.py docs/audit/scripts/classify_runner_passes.py`
  - pass
- `python3 scripts/precompute_audit_runners.py --pr-diff origin/main --check-only --push-mode none --allow-non-main`
  - all relevant caches fresh
- `git diff --check`
  - pass

## Audit Boundary

No audit verdicts are authored here. This PR did not run `audit-loop` or `docs/audit/scripts/apply_audit.py`; independent review/audit remains required.
