# Review History

## 2026-05-26 review-loop pass

Disposition: PASS WITH OPEN-GATE CLAIMS for PR handoff.

Parallel subagents were not used because the available subagent tool only
authorizes spawning when the user explicitly asks for delegation. The required
reviewer roles were run locally against the branch diff.

Reviewer summary:

- Code / Runner: PASS. The runner is deterministic, imports the existing QNM
  helper directly, checks G=0/null behavior, fixed-field Born/Sorkin error,
  Nyquist exclusion, threshold/window/damping/refinement stability, and asserts
  the negative boundary.
- Physics Claim Boundary: OPEN. The source note does not claim a positive QNM
  law and states that the apparent minima are Nyquist-unsafe on the tested
  bounded surface.
- Imports / Support: DISCLOSED. No observed QNM values, literature values,
  fitted targets, or new axioms are used.
- Nature Retention: OPEN. A future positive claim would need stable
  sub-Nyquist peaks and a stronger physical-observable bridge.
- Repo Governance: PASS. The row is reopened as `unaudited`, not locally
  assigned a verdict; `scripts/qnm_scaling.py` is recorded as a helper.
- Audit Compatibility: PASS with one unrelated warning inherited from the
  branch base: the lattice Green's Maradudin import warning is repaired by a
  separate open PR.

Checks performed:

- `python3 scripts/qnm_hardening_stability_certificate.py`
- `bash docs/audit/scripts/run_pipeline.sh`
- `python3 docs/audit/scripts/audit_lint.py --strict`
- `python3 scripts/vocab_lint.py --report-only docs/QNM_HARDENING_FEASIBILITY_NOTE.md scripts/qnm_hardening_stability_certificate.py .claude/science/physics-loops/qnm-hardening-stability-certificate/*.md`
- `python3 scripts/render_controlled_vocabulary.py --check`
- `python3 -m py_compile scripts/qnm_hardening_stability_certificate.py`
- `python3 scripts/precompute_audit_runners.py --runners scripts/qnm_hardening_stability_certificate.py --allow-non-main --check-only`
- `git diff --check`
