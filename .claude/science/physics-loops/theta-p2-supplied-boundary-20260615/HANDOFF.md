# Handoff

This PR keeps the determinant/readout algebra but makes the source boundary
auditable:

- W2 is a supplied/quarantined premise.
- The action-level `arg det` reduction is supplied, not derived.
- Multi-plaquette, source-insertion, physical-outside-class, and
  non-registrable readouts are not excluded.
- Runner count is updated to `TOTAL: PASS=40 FAIL=0`.

Verification:

```bash
python3 scripts/frontier_theta_p2_determinant_readout_exhaustion_bridge_2026_06_11.py
python3 scripts/precompute_audit_runners.py --runners scripts/frontier_theta_p2_determinant_readout_exhaustion_bridge_2026_06_11.py --force --push-mode none
python3 scripts/precompute_audit_runners.py --runners scripts/frontier_theta_p2_determinant_readout_exhaustion_bridge_2026_06_11.py --check-only
python3 docs/audit/scripts/audit_lint.py --strict
git diff --check
```

Strict lint reports notices only, including the expected non-retained note-hash
drift notice. Audit reseeding/verdict handling remains audit-lane work.
