# Historic intake: V and SM Masses Derived from Framework CW Potential

Date: 2026-08-05
Authority: none
Audit: unset
Claim type: historic_bounded_result
Stratum: branch_only_never_mainlined
Era: april_pre_reset

Status: HISTORIC INTAKE under the 2026-08-05 owner directive (pull historic
science iff relevant and/or valuable; pulled items enter the ledger and are
audited). This wrapper registers a claim from the repo's unledgered history.
The wrapper asserts nothing beyond what the pinned original states; the
original's own scope, caveats and era conventions govern. Independent audit
required before any effective status.

## The claim (as stated by the original, supervisor-compressed)

Claims to close five imports (v, M_W, M_Z, m_b, m_c, alpha_s(M_Z)) from Cl(3)-on-Z^3: with a taste threshold at M_taste ~ 1.4e15 GeV the derived sin^2(theta_W)(M_Z) = 0.2308, alpha_s(M_Z) = 0.1182, alpha_em(M_Z) = 0.0078 and g_2(M_Z) = 0.652 all land within 0.2% of PDG (Grade A), while mass ratios are only order-of-magnitude (m_b/m_t 0.010 vs 0.024, m_c/m_t 9.5e-5 vs 7.4e-3) and the absolute VEV from v = M_Pl exp(-8 pi^2/(N_taste y_t^2)) with N_taste=16, y_t(M_Pl)=0.439 gives exponent 25.6 and v ~ 5e7 GeV, five orders too high (Grade D; the needed exponent is ~38).

Original verdict: The STRUCTURAL derivation chain is complete — every import closed by a framework calculation — but the numerical value of v is off by five orders and the remaining work is named as calculations, not new physics.
Scope: 1-loop CW with SM RGE running plus a taste threshold; 10 structural checks pass.


## Why pulled (supervisor decision, on the record)

The April V_* head claim ('every import closed') WITH its title flag — the era's electroweak-scale derivation claim for audit.

## Provenance (pinned)

- Original path: `docs/V_AND_MASSES_DERIVED_NOTE.md`
- Source commit: `e9868b5045af40e16b179a2568a5decc83ffe26b`
- git blob: `ef1b425e6f3111c766d6fb6744b97f5fb5a88e4c`
- sha256: `e0c8f2f3003fd23905106ae0307ce7c77171913ff9687ab25f66f3c11314cdd6`
- Lines: 139; runners named: scripts/frontier_v_and_masses_derived.py

## Attached evidence (registered with, not as, this claim)

- none

## Flags carried

Title says masses are 'Derived' while the note's own grades put v at D (five orders high) and the b/c mass ratios at 'right order' only; the alpha_s(M_Z) row appears twice with conflicting values (0.1182 Grade A vs 0.095 via derived thresholds, 20% off).

## Audit fields

```yaml
audit_required_before_effective_retained: true
bare_retained_allowed: false
historic_intake: true
intake_directive: owner_2026-08-05
```

Independent audit still required.
