# Handoff

This stacked PR updates the R-MATTER residual-reduction note so the Weyl
thermal factor `2` is routed through the Dirac/Weyl dof repair packet instead
of being left as a raw textbook counting premise.

Review focus:

- Confirm the upstream Dirac/Weyl dependency is correctly treated as audit
  pending, not already retained.
- Confirm the note still exposes I12, R-RH, R-SPIN / thermal-inventory
  identification, and the neutral-singlet convention.
- Confirm no audit ledger or audit-result files are modified.

Verification:

```bash
PYTHONPATH=scripts python3 scripts/frontier_sm_gstar_r_matter_reduction_2026_05_29.py
python3 -m py_compile scripts/frontier_sm_gstar_r_matter_reduction_2026_05_29.py
python3 scripts/precompute_audit_runners.py --runners scripts/frontier_sm_gstar_r_matter_reduction_2026_05_29.py --check-only --push-mode=none
git diff --check
git diff -- docs/audit
```
