## Summary

This PR repairs `qnm_hardening_feasibility_note` by adding a dedicated QNM hard-bar certificate and updating the note to a bounded negative/open-gate boundary.

The new runner checks:

- `G = 0` null behavior;
- matched fixed-field scan after field relaxation;
- fixed-field three-source Born/Sorkin `I3/P`;
- Nyquist exclusion;
- threshold, window, damping, and refinement stability.

Result: apparent self-coupled absorption minima are found, but none survive as sub-Nyquist peaks on the tested bounded surfaces. This does not certify a positive QNM hardening law.

## Claim Boundary

Honest status: open gate / bounded negative boundary, not an audit verdict.

This branch does not:

- prove a positive QNM hardening law;
- derive a physical ringdown observable bridge;
- claim end-to-end nonlinear Born closure;
- introduce any new axiom;
- write an independent audit verdict.

After the local audit pipeline, the row is queued for independent re-audit:

- `claim_type`: `open_gate`
- `audit_status`: `unaudited`
- `effective_status`: `unaudited`
- `runner_path`: `scripts/qnm_hardening_stability_certificate.py`
- `helper_runner_paths`: `['scripts/qnm_scaling.py']`
- `open_dependency_paths`: `[]`

## Artifacts

- Source note: `docs/QNM_HARDENING_FEASIBILITY_NOTE.md`
- Runner: `scripts/qnm_hardening_stability_certificate.py`
- Runner cache: `logs/runner-cache/qnm_hardening_stability_certificate.txt`
- Loop handoff: `.claude/science/physics-loops/qnm-hardening-stability-certificate/HANDOFF.md`
- Review history: `.claude/science/physics-loops/qnm-hardening-stability-certificate/REVIEW_HISTORY.md`

## Verification

- `python3 scripts/qnm_hardening_stability_certificate.py`
- `bash docs/audit/scripts/run_pipeline.sh`
- `python3 docs/audit/scripts/audit_lint.py --strict`
- `python3 scripts/vocab_lint.py --report-only docs/QNM_HARDENING_FEASIBILITY_NOTE.md scripts/qnm_hardening_stability_certificate.py .claude/science/physics-loops/qnm-hardening-stability-certificate/*.md`
- `python3 scripts/render_controlled_vocabulary.py --check`
- `python3 -m py_compile scripts/qnm_hardening_stability_certificate.py`
- `python3 scripts/precompute_audit_runners.py --runners scripts/qnm_hardening_stability_certificate.py --allow-non-main --check-only`
- `git diff --check`

Known lint warning: this branch still sees the pre-existing lattice Green's Maradudin repair warning from the branch base; that row is handled by the separate lattice Green's certificate PR.
