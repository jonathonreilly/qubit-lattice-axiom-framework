# Historic intake: g_* Reconciliation: 106.75 vs 110.75

Date: 2026-08-05
Authority: none
Audit: unset
Claim type: historic_erratum
Stratum: branch_only_never_mainlined
Era: april_pre_reset

Status: HISTORIC INTAKE under the 2026-08-05 owner directive (pull historic
science iff relevant and/or valuable; pulled items enter the ledger and are
audited). This wrapper registers a claim from the repo's unledgered history.
The wrapper asserts nothing beyond what the pinned original states; the
original's own scope, caveats and era conventions govern. Independent audit
required before any effective status.

## The claim (as stated by the original, supervisor-compressed)

Two different g_* values were in use; the 110.75 variant wrongly added 4 taste scalars to the thermal plasma even though those states have Planck-scale masses and are Boltzmann-suppressed by exp(-1.22e19/160) = 0 at T_EW, so g_*(thermal) = 28 + (7/8)(90) = 106.75 is correct while N_taste = 8 belongs only in the UV sphaleron CP source via the 8/3 enhancement.

Original verdict: Four scripts were corrected from 110.75 to 106.75; the ~3.6% shift is within theoretical uncertainties, so the fix is about consistency rather than accuracy.
Scope: Applies to all thermal quantities (rho, s, H, x_F, Omega_DM); the taste enhancement is a gauge-topology effect, not a thermal one.


## Why pulled (supervisor decision, on the record)

GSTAR erratum: 110.75 wrongly included Planck-mass states — real physics error corrected in four scripts, prior baryogenesis numbers invalidated.

## Provenance (pinned)

- Original path: `docs/GSTAR_RECONCILIATION_NOTE.md`
- Source commit: `9e168f764261d87f27b16b1b979090af07b7ef84`
- git blob: `ef5ad5c85c45f682d3b0fb6587ca3e8b079bde60`
- sha256: `3324dccaf7e729740736973ea37df5b658fc335e5d08ad27d42ec5c099da7ace`
- Lines: 89; runners named: scripts/frontier_gstar_reconciliation.py, scripts/frontier_dm_native_eta.py, scripts/frontier_dm_taste_enhanced_eta.py, scripts/frontier_dm_coupled_transport.py, scripts/frontier_dm_eta_derivation.py

## Attached evidence (registered with, not as, this claim)

- none

## Flags carried

Documents a real physics error that propagated into three baryogenesis scripts plus one derivation before being caught by adversarial audit.

## Audit fields

```yaml
audit_required_before_effective_retained: true
bare_retained_allowed: false
historic_intake: true
intake_directive: owner_2026-08-05
```

Independent audit still required.
