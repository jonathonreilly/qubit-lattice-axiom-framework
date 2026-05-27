# Handoff

This block repairs the DM leptogenesis PMNS transport interval witness row.

What changed:

- The primary runner now carries its own narrow compatibility layer for
  `canonical_h`, active-packet diagonalization, and the one-column transport
  functional.
- Stale imports from the raw-interface / active-projector / flavor-column helper
  stack were removed from the primary runner.
- The source note now states that the `eta/eta_obs = 1` point is an interpolated
  diagnostic against `ETA_OBS`, not a physical selector or full-stack closure.
- The runner cache was refreshed and the audit pipeline queues the row as
  `unaudited`, `ready: true`.

Reviewer checks to repeat:

```bash
python3 scripts/cached_runner_output.py --check-only --tail-chars 1200 scripts/frontier_dm_leptogenesis_pmns_transport_extremal_source_candidate.py
bash docs/audit/scripts/run_pipeline.sh
python3 docs/audit/scripts/audit_lint.py --strict
git diff --check
python3 scripts/render_controlled_vocabulary.py --check
python3 scripts/vocab_lint.py --report-only docs/DM_LEPTOGENESIS_PMNS_TRANSPORT_EXTREMAL_SOURCE_CANDIDATE_NOTE_2026-04-16.md .claude/science/physics-loops/dm-pmns-transport-runner-repair-20260527
bash docs/audit/scripts/pre_commit_audit_check.sh
```

Remaining science:

- Audit must decide whether the repaired row is clean bounded support or
  numerical-match style support because the root is normalized against `ETA_OBS`.
- The physical off-seed selector law remains open.
- Full-stack DM/PMNS closure remains open.
