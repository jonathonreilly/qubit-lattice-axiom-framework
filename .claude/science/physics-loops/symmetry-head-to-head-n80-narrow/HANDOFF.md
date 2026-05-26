# Handoff

PR: pending

## What Changed

The head-to-head note now binds only the shared `N = 80` comparison between the
mirror dense boundary card and the sparse `Z2 x Z2` joint-validation card. The
runner now asserts retained-grade dependency status, confirms the `Z2 x Z2`
source scope excludes `N = 120`, and verifies the one-row comparison predicates.

## Verification

- `python3 scripts/symmetry_head_to_head.py`
- `python3 scripts/precompute_audit_runners.py --pr-diff origin/main`
- `bash docs/audit/scripts/run_pipeline.sh`
- `python3 docs/audit/scripts/audit_lint.py --strict`
- `python3 scripts/render_controlled_vocabulary.py --check`
- `python3 scripts/vocab_lint.py --report-only docs/SYMMETRY_HEAD_TO_HEAD_NOTE.md .claude/science/physics-loops/symmetry-head-to-head-n80-narrow/*.md`
- `python3 -m py_compile scripts/symmetry_head_to_head.py`
- `git diff --check`
