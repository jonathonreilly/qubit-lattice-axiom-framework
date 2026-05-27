# Handoff

## Summary

This PR repairs the DM neutrino bosonic normalization bridge row by narrowing
it to what the retained X1/X2 authorities and exact C16 matrix algebra actually
support.

## Claim Movement

- Before: the note treated the non-Hermitian raw bridge `Y` as if X1's
  real-symmetric source-domain theorem applied to it, and it promoted the
  resulting Frobenius ratio into a physical `y_nu/g_weak` readout.
- After: the note applies X1 only to the real-symmetric Hermitian completion
  `Gamma_1 = Y + Y^dagger`, keeps `Y` as a nilpotent diagnostic, and records
  `sqrt(Tr(Y^dagger Y)/Tr(Gamma_1^dagger Gamma_1)) = 1/sqrt(2)` as the exact
  raw-to-completion finite-block ratio.
- Remaining: a separate readout bridge is still needed before the physical
  `y_nu/g_weak` interpretation can be used.

## Verification

- `python3 scripts/audit_companion_dm_neutrino_bosonic_normalization_observable_principle_bridge_exact_2026_05_16.py`
- `python3 scripts/vocab_lint.py --report-only docs/DM_NEUTRINO_BOSONIC_NORMALIZATION_OBSERVABLE_PRINCIPLE_BRIDGE_NARROW_THEOREM_NOTE_2026-05-16.md`
- `bash docs/audit/scripts/run_pipeline.sh`
- `git diff --check`

## Next Action

Open as a draft PR. If review accepts the scope repair, independent audit can
re-audit the row as a bounded finite-block support theorem while leaving the
physical readout gap open.
