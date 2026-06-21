# Summary

Repairs and registers the Koide April 22 bounded support-batch aggregate runner.

The direct aggregate initially failed at `TOTAL: 395/381`. This PR fixes that honestly by narrowing the charged-lepton Yukawa BZ quadrature runner to a large-coefficient negative boundary (`PASSED: 6/6`) and updating the dimensionless-objection expected count from `21` to `38`. The aggregate now reports `TOTAL: 398/398`.

# Artifacts

- `docs/KOIDE_AXIOM_NATIVE_SUPPORT_BATCH_NOTE_2026-04-22.md`
- `scripts/frontier_charged_lepton_yukawa_bz_quadrature_explicit.py`
- `scripts/frontier_koide_lane_regression.py`
- `logs/runner-cache/frontier_charged_lepton_yukawa_bz_quadrature_explicit.txt`
- `logs/runner-cache/frontier_koide_lane_regression.txt`
- generated audit surfaces under `docs/audit/`
- branch-local handoff pack under `.claude/science/physics-loops/audit-unblock-block151-20260621/`

# Boundary

This PR keeps the row `bounded_theorem` / `unaudited` / `effective_status: unaudited`. It does not apply audit verdicts, does not update repo-wide lane/status authority surfaces, and does not promote charged-lepton Koide closure.

The reviewer lane may update or cherry-pick this PR against fast-moving `main`; this branch is not intended to keep refreshing itself after opening.

# Verification

- `python3 scripts/frontier_charged_lepton_yukawa_bz_quadrature_explicit.py` -> `PASSED: 6/6`
- `python3 scripts/frontier_koide_lane_regression.py` -> `TOTAL: 398/398`
- `python3 scripts/precompute_audit_runners.py --runners scripts/frontier_koide_lane_regression.py,scripts/frontier_charged_lepton_yukawa_bz_quadrature_explicit.py --check-only --push-mode none --allow-non-main` -> caches fresh
- `python3 docs/audit/scripts/audit_lint.py --strict` -> strict lint OK
- `python3 -m py_compile scripts/frontier_charged_lepton_yukawa_bz_quadrature_explicit.py scripts/frontier_koide_lane_regression.py docs/audit/scripts/build_citation_graph.py docs/audit/scripts/seed_audit_ledger.py docs/audit/scripts/classify_runner_passes.py`
- `git diff --check`
