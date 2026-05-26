# Summary

This PR repairs `higgs_mechanism_note` by adding an explicit conditional-use
firewall: the mechanism-level runner is diagnostic only under the admitted
scalar/Coleman-Weinberg/bare-parameter bridge.

No new axiom, retained verdict, exact Higgs-mass closure, or substrate
derivation is claimed.

# Claim movement

- `higgs_mechanism_note`
  - `claim_type`: `bounded_theorem`
  - `audit_status`: `unaudited`
  - `effective_status`: `unaudited`
  - `open_dependency_paths`: `[]`
  - audit queue: ready, unblocked, critical

# Verification

- `bash docs/audit/scripts/run_pipeline.sh`
- `python3 docs/audit/scripts/audit_lint.py --strict`
- `python3 scripts/vocab_lint.py --report-only docs/HIGGS_MECHANISM_NOTE.md`
- `python3 scripts/render_controlled_vocabulary.py --check`
- `python3 scripts/precompute_audit_runners.py --runners scripts/frontier_higgs_mass_derived.py --allow-non-main --check-only`
- `git diff --check`
