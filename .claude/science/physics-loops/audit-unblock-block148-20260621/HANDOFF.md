# Handoff

Block 148 registers an audit-discoverable open-gate runner for `newton_derivation_note`.

## What Changed

- Added `scripts/newton_derivation_open_gate_probe.py`.
- Added cached output at `logs/runner-cache/newton_derivation_open_gate_probe.txt`.
- Added `Claim type`, `Status authority`, and `Runner` metadata to `docs/NEWTON_DERIVATION_NOTE.md`.
- Replaced stale machine-local artifact links in the touched note with repo-relative links.
- Regenerated audit ledger, queue, citation graph, and runner classification.

## Boundary

The target remains:

- `claim_type`: `open_gate`
- `audit_status`: `unaudited`
- `effective_status`: `unaudited`

The runner result is `SUMMARY: PASS=14 FAIL=0`, with class `B` and one assert in runner classification. This is an open-gate verifier only. It does not claim a retained Newtonian derivation, does not close the external-field persistent compact-object inertial-mass step, and does not run or apply audit verdicts.

## Reviewer Notes

The reviewer lane can cherry-pick or refresh this PR against fast-moving `main`; this branch intentionally does not chase main after PR creation.

If integrating manually, prefer source files and rerun:

```bash
bash docs/audit/scripts/run_pipeline.sh
python3 scripts/precompute_audit_runners.py --runners scripts/newton_derivation_open_gate_probe.py --push-mode none --allow-non-main
python3 docs/audit/scripts/audit_lint.py --strict
```

## Next Exact Action

After this PR is opened, continue the campaign by inspecting `mass_spectrum_derived_note` for a similarly narrow source-side runner/discoverability repair. Skip existing dirty PR maintenance unless the user explicitly asks for it.
