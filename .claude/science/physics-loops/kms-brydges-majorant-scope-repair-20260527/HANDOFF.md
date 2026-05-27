# Handoff

## Summary

This block narrows the KMS/Brydges row to scalar quadratic majorant ODE
algebra. It removes the external KMS theorem and framework bridge from the
binding claim.

## Changed Files

- `docs/KMS_FERMIONIC_BRYDGES_MAJORANT_EXTERNAL_NARROW_THEOREM_NOTE_2026-05-11.md`
- `scripts/frontier_kms_fermionic_brydges_majorant_external_narrow.py`
- `.claude/science/physics-loops/kms-brydges-majorant-scope-repair-20260527/`

## Verification

```bash
PYTHONPATH=scripts python3 scripts/frontier_kms_fermionic_brydges_majorant_external_narrow.py
python3 scripts/vocab_lint.py --report-only docs/KMS_FERMIONIC_BRYDGES_MAJORANT_EXTERNAL_NARROW_THEOREM_NOTE_2026-05-11.md scripts/frontier_kms_fermionic_brydges_majorant_external_narrow.py .claude/science/physics-loops/kms-brydges-majorant-scope-repair-20260527/*.md
bash docs/audit/scripts/run_pipeline.sh
git diff --check
```

## Reviewer Focus

- Confirm the KMS theorem is context only.
- Confirm the runner proves only scalar ODE algebra and boundary strings.
- Confirm no audit verdict was applied manually.
