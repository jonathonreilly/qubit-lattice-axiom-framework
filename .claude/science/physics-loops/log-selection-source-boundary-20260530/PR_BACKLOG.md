# PR Backlog

Prepared branch:

```text
physics-loop/log-selection-source-boundary-20260530
```

Suggested PR title:

```text
[physics-loop] log-selection source boundary no-go
```

Suggested base:

```text
main
```

Suggested body should include:

- note: `docs/SOURCE_MEASURE_LOG_SELECTION_BOUNDARY_THEOREM_NOTE_2026-05-30.md`
- runner: `scripts/frontier_source_measure_log_selection_boundary.py`
- output: `outputs/source_measure_log_selection_boundary_2026-05-30.json`
- verification: runner PASS=57 FAIL=0, py_compile, diff-check
- dependency warning: downstream source-measure drafts remain draft until the
  separate physical source-unit/log-selection premise or same-source response
  evidence is supplied.
