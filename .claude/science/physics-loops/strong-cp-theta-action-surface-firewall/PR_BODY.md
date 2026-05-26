# Summary

This PR repairs `strong_cp_theta_zero_note` by making the prior audit boundary
explicit: the result is `theta_eff = 0` only on the explicitly theta-free
Wilson-plus-staggered scalar-mass surface tested by the runner.

No new axiom, retained verdict, or all-formulations strong-CP solution is
claimed.

# Claim movement

- `strong_cp_theta_zero_note`
  - `claim_type`: `bounded_theorem`
  - `audit_status`: `unaudited`
  - `effective_status`: `unaudited`
  - `open_dependency_paths`: `[]`
  - audit queue: ready, unblocked, critical

# Artifacts

- `docs/STRONG_CP_THETA_ZERO_NOTE.md`
- `scripts/frontier_strong_cp_theta_zero.py`
- `logs/runner-cache/frontier_strong_cp_theta_zero.txt`
- `.claude/science/physics-loops/strong-cp-theta-action-surface-firewall/HANDOFF.md`

# Verification

- `python3 scripts/frontier_strong_cp_theta_zero.py`
- `bash docs/audit/scripts/run_pipeline.sh`
- `python3 docs/audit/scripts/audit_lint.py --strict`
- `python3 scripts/vocab_lint.py --report-only docs/STRONG_CP_THETA_ZERO_NOTE.md .claude/science/physics-loops/strong-cp-theta-action-surface-firewall/*.md`
- `python3 scripts/render_controlled_vocabulary.py --check`
- `python3 -m py_compile scripts/frontier_strong_cp_theta_zero.py`
- `python3 scripts/precompute_audit_runners.py --runners scripts/frontier_strong_cp_theta_zero.py --allow-non-main --check-only`
- `git diff --check`
