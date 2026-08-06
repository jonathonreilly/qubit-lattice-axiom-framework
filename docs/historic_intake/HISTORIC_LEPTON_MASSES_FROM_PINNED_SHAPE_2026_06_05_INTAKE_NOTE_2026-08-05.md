# Historic intake: Charged-lepton masses from the pinned shape (r=1/2, theta=2/9) plus one scale

Date: 2026-08-05
Authority: none
Audit: unset
Claim type: historic_theorem
Stratum: branch_only_never_mainlined
Era: unknown

Status: HISTORIC INTAKE under the 2026-08-05 owner directive (pull historic
science iff relevant and/or valuable; pulled items enter the ledger and are
audited). This wrapper registers a claim from the repo's unledgered history.
The wrapper asserts nothing beyond what the pinned original states; the
original's own scope, caveats and era conventions govern. Independent audit
required before any effective status.

## The claim (as stated by the original, supervisor-compressed)

With r=1/2 and theta=2/9 exactly, the sqrt-masses are {2.379438172, 0.040349908, 0.580211920} in units of a, giving m_e : m_mu : m_tau = 1 : 206.770316 : 3477.472837 against PDG 1 : 206.768285 : 3477.228307 — relative deviations 9.8e-6 (mu slot) and 7.0e-5 (tau slot). Exactly one free DOF remains (3 masses minus 2 ratio constraints), and setting it to PDG gives a^2 = 313.84 MeV.

Original verdict: The pinned shape reproduces the observed charged-lepton mass ratios to better than 7e-5, exact-modulo-imports; the overall scale is one free residual and is currently NOT pinnable.
Scope: Forward accounting only; r=1/2 and theta=2/9 remain the AC_phi_lambda Tier-A import and the scale remains the units-only scale_reference_primitive. PDG is a labelled comparator, not a derivation input for the shape.


## Why pulled (supervisor decision, on the record)

The pinned lepton shape reproduces mass ratios to 7e-5 — WITH the honest flag that theta = 2/9 is not the best-fit Brannen angle.

## Provenance (pinned)

- Original path: `docs/LEPTON_MASSES_FROM_PINNED_SHAPE_2026-06-05.md`
- Source commit: `a0d0e2f80bb5af45e43290d940423035aae5b45e`
- git blob: `4cd1ac1b1b61972f4f0527370cbb6451d72d96de`
- sha256: `a6afdfbd82ea560b86bfbb1978b9093b0eaab06490f95d0318e9169d3d7efaa4`
- Lines: 221; runners named: scripts/cl3_lepton_masses_from_pinned_shape_2026_06_05.py

## Attached evidence (registered with, not as, this claim)

- none

## Flags carried

Honestly reports that theta=2/9 is NOT the best-fit Brannen phase: theta_fit = 0.22222963 rad, residual +7.4e-6 rad (3.3e-5 relative), and Q_PDG - 2/3 = -6.2e-6 — both small but nonzero.

## Audit fields

```yaml
audit_required_before_effective_retained: true
bare_retained_allowed: false
historic_intake: true
intake_directive: owner_2026-08-05
```

Independent audit still required.
