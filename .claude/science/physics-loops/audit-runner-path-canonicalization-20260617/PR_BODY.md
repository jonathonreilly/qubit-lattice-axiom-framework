## Summary

This PR repairs audit-runner path handling for stale row metadata:

- canonicalizes row runner paths before `codex_audit_runner.py` renders
  `{{RUNNER_PATH}}` or reads runner source;
- canonicalizes helper runner paths before source embedding;
- applies the same normalization in `audit_packet_script_deps.py` before
  deciding a row's runner is missing;
- adds a guard runner showing the current 55 `missing_runner_file` inventory
  entries resolve to checked-in `scripts/*.py` paths.

## Audit Boundary

No audit verdicts, ledgers, queues, or generated audit-result files are edited.
This is source-side tooling hygiene so later audit packet construction can see
the runners already present in the checkout.

## Checks

- `python3 scripts/audit_runner_path_canonicalization_guard_2026_06_17.py`
- `python3 scripts/cached_runner_output.py --check-only scripts/audit_runner_path_canonicalization_guard_2026_06_17.py`
- `python3 -m py_compile scripts/codex_audit_runner.py scripts/audit_packet_script_deps.py scripts/audit_runner_path_canonicalization_guard_2026_06_17.py`
- `git diff --check`
- `git diff --name-only -- docs/audit docs/publication/ci3_z3 docs/repo/FRONT_DOOR_STATUS.md` (empty)
