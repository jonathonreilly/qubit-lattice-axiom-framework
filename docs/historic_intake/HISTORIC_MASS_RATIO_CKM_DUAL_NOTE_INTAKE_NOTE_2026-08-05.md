# Historic intake: Fermion Mass Ratios from the CKM Dual

Date: 2026-08-05
Authority: none
Audit: unset
Claim type: bounded_theorem
Stratum: branch_only_never_mainlined
Era: april_pre_reset

Status: HISTORIC INTAKE under the 2026-08-05 owner directive (pull historic
science iff relevant and/or valuable; pulled items enter the ledger and are
audited). This wrapper registers a claim from the repo's unledgered history.
The wrapper asserts nothing beyond what the pinned original states; the
original's own scope, caveats and era conventions govern. Independent audit
required before any effective status.

## The claim (as stated by the original, supervisor-compressed)

Seven charged-fermion mass ratios expressed as powers of alpha_s(v) = 0.1033 with exponents from four exact framework integers (C_F = 4/3, T_F = 1/2, N_c = 3, n_pair = 2). Down-type (retained): m_d/m_s = alpha_s/2 = 0.05165 (+3.3%), m_s/m_b = [alpha_s/sqrt(6)]^(6/5) = 0.02239 (+0.2%), m_d/m_b = 0.001156 (+3.5%). Up-type (bounded): m_c/m_t = 0.007463 (+1.5%), m_u/m_c = 0.001735 (+2.0%). Leptons (bounded): m_mu/m_tau = alpha_s^(5/4) = 0.05857 (-1.5%), m_e/m_mu = alpha_s^(7/3) = 0.005007 (+3.5%).

Original verdict: All match at the few-percent level (23/23, 15/15, 14/14 PASS); down-type is retained at the promoted CKM atlas bar, up-type and leptons are bounded.
Scope: No observed masses used as derivation inputs; the up-type inter-sector relations (m_c m_b = m_s m_t/N_c, 2 m_u m_b^2 = m_d m_s m_t) and the lepton exponents 5/4 and 7/3 are empirically discovered patterns with exact framework-constant labels, not first-principles derivations.


## Why pulled (supervisor triage decision of 2026-08-05, provenance not authority)

The reasons below are the supervisor's selection rationale; they carry no claim status and are not evidence about the original's validity.

Seven charged-fermion mass ratios as powers of alpha_s(v) with exponents from four exact integers (23/23, 15/15, 14/14) — costs disclosed.

## Provenance (pinned)

- Original path: `docs/MASS_RATIO_CKM_DUAL_NOTE.md`
- Source commit: `7f869e3f3cccb35a67b1231d37dc84ecf7e938a4`
- git blob: `61cba502bbb219790d3c62266f55bbf05a965776`
- sha256: `e3197ae7d485f9af92cf816cd1afbe44f3f2e8d9ffc32ca1cfa3541064f8f305`
- Archived original (byte-exact, sha256-verified at generation): [../../archive_unlanded/historic_intake_originals/branch04/1136_MASS_RATIO_CKM_DUAL_NOTE.md](../../archive_unlanded/historic_intake_originals/branch04/1136_MASS_RATIO_CKM_DUAL_NOTE.md)
- Lines: 190; runners named: historic runner (unpinned, not in this packet): `scripts/frontier_mass_ratio_ckm_dual(.py)`; historic runner (unpinned, not in this packet): `scripts/frontier_mass_ratio_up_sector(.py)`; historic runner (unpinned, not in this packet): `scripts/frontier_mass_ratio_lepton_sector(.py)`

## Attached evidence (registered with, not as, this claim)

- none

## Flags carried

Two disclosed costs: the m_s/m_b agreement is scale-convention dependent (+0.2% at PDG mixed scales but -11% when both are run to mu = m_b, stated as an open question); and leptons are color singlets with no derived mechanism connecting alpha_s to their masses, with the predicted masses degrading the Koide match from 0.001% to 0.18%.

## Audit fields

```yaml
audit_required_before_effective_retained: true
bare_retained_allowed: false
historic_intake: true
historic_claim_class: historic_theorem
intake_directive: owner_2026-08-05
```

Independent audit still required.
