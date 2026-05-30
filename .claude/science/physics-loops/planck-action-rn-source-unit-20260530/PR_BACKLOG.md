# PR Backlog

Prepared branch:

```text
physics-loop/planck-action-rn-source-unit-20260530
```

Suggested base:

```text
physics-loop/log-selection-source-boundary-20260530
```

Suggested title:

```text
[physics-loop] Planck-action RN source-unit bridge bounded-support
```

Suggested body should include:

- note: `docs/SOURCE_MEASURE_PLANCK_ACTION_RN_SOURCE_UNIT_BRIDGE_NOTE_2026-05-30.md`
- runner: `scripts/frontier_source_measure_planck_action_rn_source_unit_bridge.py`
- output: `outputs/source_measure_planck_action_rn_source_unit_bridge_2026-05-30.json`
- verification: runner PASS=45 FAIL=0, py_compile, diff-check
- status: bounded support / upstream support, not Y_T closure
