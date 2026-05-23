# Artifact Plan

## Source Artifacts

- Patch `docs/GAUGE_VACUUM_PLAQUETTE_LOCAL_ENVIRONMENT_FACTORIZATION_THEOREM_NOTE.md`
  with an explicit bridge lemma for temporal-gauge mixed-kernel convolution and
  marked/non-marked compression.
- Patch `scripts/frontier_gauge_vacuum_plaquette_local_environment_factorization.py`
  so the runner checks the bridge-specific facts rather than only the final
  local factor.

## Verification

- `python3 -m py_compile scripts/frontier_gauge_vacuum_plaquette_local_environment_factorization.py`
- `python3 scripts/frontier_gauge_vacuum_plaquette_local_environment_factorization.py`
- `bash docs/audit/scripts/run_pipeline.sh`
- `python3 docs/audit/scripts/audit_lint.py --strict`
- `git diff --check`

Generated audit/publication surfaces are verification byproducts only for this
science branch and should not be committed unless the landing reviewer chooses
to regenerate them on current `main`.
