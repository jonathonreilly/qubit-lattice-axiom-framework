# Handoff

This block targets a critical audited-conditional row by syncing the parent
microcausality note with the already-repaired finite-range bridge constants.

Changed source packet:

- `docs/AXIOM_FIRST_MICROCAUSALITY_LIEB_ROBINSON_THEOREM_NOTE_2026-05-01.md`
  now uses the bridge's repaired `J` branches (`|m| + 78`, `|m| + 78.5`,
  `|m| + 80`), overlap weights (`|m| + 296`, `|m| + 298`, `|m| + 300`),
  and `v_LR = 2 e q W R` convention.
- `scripts/axiom_first_microcausality_check.py` now validates the parent note
  against the bridge constants before running the finite-matrix LR checks.
- `logs/runner-cache/axiom_first_microcausality_check.txt` is refreshed through
  the repo cache utility and SHA-pinned to the edited runner.

Reviewer focus:

- Confirm that the parent note no longer asserts the stale bounded
  action-support/J-bound paragraph.
- Confirm that the runner guard is source-packet bookkeeping, not an audit
  verdict.
- Confirm that no generated audit data or ledger verdict file is included.

Remaining status:

Independent audit owns any effective status change.
