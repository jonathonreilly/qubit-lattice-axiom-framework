# Review History

- Before edit:
  - `extract_runner(...) -> None`
  - `cached_runner_output --check-only` reported missing cache.
- Runner direct execution:
  - `RESULT: 18 PASS, 0 FAIL`
- After edit:
  - `extract_runner(...) -> scripts/frontier_dm_neutrino_weak_vector_theorem.py`
  - cache refresh wrote a v1 cache with `exit_code: 0`.
- Full pipeline:
  - `audit_lint` errors: 0.
  - hard invalidations: 7, all downstream of the intentionally edited
    `dm_neutrino_weak_vector_theorem_note_2026-04-15` row.
