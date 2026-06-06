# Artifact Plan

Artifacts:

- Parent note repair:
  `docs/YT_WARD_IDENTITY_DERIVATION_THEOREM.md`
- Runner prose alignment:
  `scripts/frontier_yt_ward_identity_derivation.py`
- Cache refresh:
  `logs/runner-cache/frontier_yt_ward_identity_derivation.txt`
  `logs/runner-cache/audit_companion_yt_ward_identity_dependencies_registered_bound_2026_06_05.txt`
- Loop certification packet:
  `.claude/science/physics-loops/yt-ward-deps-wire-20260606/`

Verification plan:

```bash
python3 -m py_compile scripts/frontier_yt_ward_identity_derivation.py scripts/audit_companion_yt_ward_identity_dependencies_registered_bound_2026_06_05.py
python3 scripts/frontier_yt_ward_identity_derivation.py
python3 scripts/audit_companion_yt_ward_identity_dependencies_registered_bound_2026_06_05.py
python3 scripts/precompute_audit_runners.py --runners scripts/frontier_yt_ward_identity_derivation.py,scripts/audit_companion_yt_ward_identity_dependencies_registered_bound_2026_06_05.py --force --allow-non-main --push-mode none
git diff --check
git diff -- docs/audit --exit-code
```
