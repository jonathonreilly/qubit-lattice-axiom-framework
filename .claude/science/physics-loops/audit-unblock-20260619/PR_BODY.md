# PR Body

## Summary

This PR unblocks the ready audit row for
`koide_q_delta_linking_relation_theorem_note_2026-04-20`.

On current `origin/main`, direct execution of
`scripts/frontier_koide_q_delta_formal_ratio_repair.py` failed its citation
firewall because the auto-generated `docs/repo/FRONT_DOOR_STATUS.md` queue
snapshot listed the ready row without a formal/open context marker. The runner
reported `TOTAL: PASS=107 FAIL=1` even though the committed cache was stale at
`TOTAL: PASS=106 FAIL=0`.

The fix keeps the bounded claim boundary narrow:

- `docs/KOIDE_Q_DELTA_LINKING_RELATION_THEOREM_NOTE_2026-04-20.md` now states
  that generated queue snapshots are not source-claim citations for this
  firewall.
- `scripts/frontier_koide_q_delta_formal_ratio_repair.py` skips
  `docs/repo/FRONT_DOOR_STATUS.md`, matching the existing generated-surface
  exclusions.
- The target runner cache was refreshed and now records
  `TOTAL: PASS=106 FAIL=0`.

After rebasing onto current `main` at `678b38ce7`, the branch is intentionally
narrowed to the source firewall repair, the refreshed target runner cache, and
the branch-local loop packet. Generated audit, publication, and front-door
surfaces are excluded from this PR.

## Boundary

- No audit-loop run.
- No audit verdicts applied.
- No effective-status promotion.
- This is a source-side runner/firewall repair for an already-ready unaudited
  bounded row.

## Current queue snapshot

- claim_type: `bounded_theorem`
- audit_status: `unaudited`
- effective_status: `unaudited`
- criticality: `critical`
- load_bearing_score: `13.34`
- direct_in_degree: `10`
- transitive_descendants: `323`
- deps: `[]`
- ready: `true`

## Verification

- `python3 -m py_compile scripts/frontier_koide_q_delta_formal_ratio_repair.py`
- Direct runner before patch: `TOTAL: PASS=107 FAIL=1`
- `python3 scripts/frontier_koide_q_delta_formal_ratio_repair.py` -> `TOTAL: PASS=106 FAIL=0`
- `python3 scripts/precompute_audit_runners.py --runners scripts/frontier_koide_q_delta_formal_ratio_repair.py --check-only --push-mode none --allow-non-main` -> `fresh: 1`, `stale to refresh: 0`, `missing on disk: 0`
- `python3 scripts/precompute_audit_runners.py --pr-diff origin/main --check-only --allow-non-main` -> `fresh: 1`, `stale to refresh: 0`, `missing on disk: 0`
- `python3 -m py_compile scripts/frontier_koide_q_delta_formal_ratio_repair.py scripts/precompute_audit_runners.py scripts/runner_cache.py` -> OK
- `git diff --check` -> OK
