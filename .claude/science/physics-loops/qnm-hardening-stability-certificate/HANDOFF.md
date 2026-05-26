# Handoff

## Block

`qnm_hardening_feasibility_note`

## Branch

`physics-loop/qnm-hardening-stability-certificate-20260526`

## PR

https://github.com/jonathonreilly/qubit-lattice-axiom-framework/pull/1949

## Claim movement

The previous audit objection asked for a dedicated hardening runner and note/log pair covering the `G = 0` null, fixed-field control, Born check, Nyquist exclusion, and refinement/threshold/window/damping stability bars.

This block adds that runner and finds a bounded negative boundary: apparent self-coupled minima exist in the finite reduced scans, but none survive as sub-Nyquist peaks. The row is reopened for independent audit as an open gate, not promoted locally.

After running the audit pipeline locally, the row is ready for independent re-audit:

- `audit_status`: `unaudited`
- `effective_status`: `unaudited`
- `runner_path`: `scripts/qnm_hardening_stability_certificate.py`
- `helper_runner_paths`: `['scripts/qnm_scaling.py']`
- `open_dependency_paths`: `[]`

## Remaining blockers

- Independent audit must decide whether the bounded negative hard-bar packet satisfies the row's open-gate scope.
- A future positive QNM claim would need stable sub-Nyquist peaks on a stronger control family.

## Verification

Run:

```bash
python3 scripts/qnm_hardening_stability_certificate.py
bash docs/audit/scripts/run_pipeline.sh
python3 docs/audit/scripts/audit_lint.py --strict
python3 scripts/vocab_lint.py --report-only docs/QNM_HARDENING_FEASIBILITY_NOTE.md scripts/qnm_hardening_stability_certificate.py .claude/science/physics-loops/qnm-hardening-stability-certificate/*.md
python3 scripts/render_controlled_vocabulary.py --check
python3 -m py_compile scripts/qnm_hardening_stability_certificate.py
python3 scripts/precompute_audit_runners.py --runners scripts/qnm_hardening_stability_certificate.py --allow-non-main --check-only
git diff --check
```

## Next exact action

After this PR is opened and mergeability is clean, continue the campaign with the highest-impact independent audited-conditional row not already covered by an open PR.
