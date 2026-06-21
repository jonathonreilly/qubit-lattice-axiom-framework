# Summary

Registers a source-side open-gate runner for `newton_derivation_note`.

This PR keeps the Newton derivation note as `open_gate` / `unaudited` / `effective_status: unaudited`. The new wrapper verifies that the residual external-field generator-invariant inertial-mass step on a persistent compact-object family remains explicit, then executes the existing equivalence, composite-source additivity, and `top4` bridge runners as bounded support.

# Artifacts

- `docs/NEWTON_DERIVATION_NOTE.md`
- `scripts/newton_derivation_open_gate_probe.py`
- `logs/runner-cache/newton_derivation_open_gate_probe.txt`
- generated audit surfaces under `docs/audit/`
- branch-local handoff pack under `.claude/science/physics-loops/audit-unblock-block148-20260621/`

# Boundary

This is not a retained Newtonian derivation. It does not close the external-field persistent compact-object inertial-mass gate, does not apply audit verdicts, and does not update repo-wide lane/status authority surfaces.

The reviewer lane may update or cherry-pick this PR against fast-moving `main`; this branch is not intended to keep refreshing itself after opening.

# Verification

- `python3 scripts/newton_derivation_open_gate_probe.py` -> `SUMMARY: PASS=14 FAIL=0`
- `python3 scripts/precompute_audit_runners.py --runners scripts/newton_derivation_open_gate_probe.py --check-only --push-mode none --allow-non-main` -> cache fresh
- `python3 docs/audit/scripts/audit_lint.py --strict` -> strict lint OK
- `python3 -m py_compile scripts/newton_derivation_open_gate_probe.py scripts/equivalence_principle_harness.py scripts/composite_source_additivity_harness.py scripts/composite_source_additivity_2d_cross_family.py scripts/newton_derivation_top4_bridge_runner.py docs/audit/scripts/build_citation_graph.py docs/audit/scripts/seed_audit_ledger.py docs/audit/scripts/classify_runner_passes.py`
- `python3 scripts/precompute_audit_runners.py --pr-diff origin/main --check-only --push-mode none --allow-non-main` -> all relevant caches fresh
- `git diff --check`
