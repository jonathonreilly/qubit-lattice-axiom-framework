# Summary

Registers a source-side bounded runner for `dm_eta_g1_fierz_channel_narrative_correction_note_2026-05-27`.

The new wrapper checks the note's bounded narrative-correction scope, verifies that the adjoint-channel overclaim remains explicitly removed, and executes the Coleman-Weinberg support runner (`PASS = 17, FAIL = 0`). The wrapper itself reports `SUMMARY: PASS=9 FAIL=0`.

# Artifacts

- `docs/DM_ETA_G1_FIERZ_CHANNEL_NARRATIVE_CORRECTION_NOTE_2026-05-27.md`
- `scripts/dm_eta_g1_fierz_channel_narrative_correction_probe.py`
- `logs/runner-cache/dm_eta_g1_fierz_channel_narrative_correction_probe.txt`
- generated audit surfaces under `docs/audit/`
- branch-local handoff pack under `.claude/science/physics-loops/audit-unblock-block150-20260621/`

# Boundary

This PR keeps the row `bounded_theorem` / `unaudited` / `effective_status: unaudited`. It does not apply audit verdicts, does not update repo-wide lane/status authority surfaces, and does not promote the DM-eta lane.

I also inspected the higher-priority Koide support-batch candidate, but its integrated regression currently exits nonzero (`TOTAL: 395/381`), so this PR does not attempt to paper over that broader issue.

# Verification

- `python3 scripts/dm_eta_g1_fierz_channel_narrative_correction_probe.py` -> `SUMMARY: PASS=9 FAIL=0`
- `python3 scripts/precompute_audit_runners.py --runners scripts/dm_eta_g1_fierz_channel_narrative_correction_probe.py --check-only --push-mode none --allow-non-main` -> cache fresh
- `python3 docs/audit/scripts/audit_lint.py --strict` -> strict lint OK
- `python3 -m py_compile scripts/dm_eta_g1_fierz_channel_narrative_correction_probe.py scripts/frontier_dm_eta_g1_coleman_weinberg_2026_05_06.py docs/audit/scripts/build_citation_graph.py docs/audit/scripts/seed_audit_ledger.py docs/audit/scripts/classify_runner_passes.py`
- `git diff --check`
