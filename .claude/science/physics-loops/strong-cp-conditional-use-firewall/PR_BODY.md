## Summary

This PR repairs `strong_cp_operator_basis_and_mass_orientation_theorem_note_2026-05-19` by adding an explicit conditional-use firewall.

The note now says downstream uses inherit:

- the canonical Wilson single-plaquette real-positive-measure surface;
- the retained staggered-only determinant-positivity authority;
- the scalar-mass action-class boundary;
- the convention status of positive mass orientation inside the real scalar line.

## Claim Boundary

Honest status: bounded support, not an audit verdict.

This PR does not derive the selector boundaries from A1/A2 alone and does not promote `STRONG_CP_THETA_ZERO_NOTE.md`.

After the local audit pipeline:

- `claim_type`: `bounded_theorem`
- `audit_status`: `unaudited`
- `effective_status`: `unaudited`
- `open_dependency_paths`: `[]`

## Verification

- `bash docs/audit/scripts/run_pipeline.sh`
- `python3 docs/audit/scripts/audit_lint.py --strict`
- `python3 scripts/vocab_lint.py --report-only docs/STRONG_CP_OPERATOR_BASIS_AND_MASS_ORIENTATION_THEOREM_NOTE_2026-05-19.md .claude/science/physics-loops/strong-cp-conditional-use-firewall/*.md`
- `python3 scripts/render_controlled_vocabulary.py --check`
- `python3 -m py_compile scripts/frontier_strong_cp_operator_basis_real_2026_05_19.py`
- `python3 scripts/precompute_audit_runners.py --runners scripts/frontier_strong_cp_operator_basis_real_2026_05_19.py --allow-non-main --check-only`
- `git diff --check`
