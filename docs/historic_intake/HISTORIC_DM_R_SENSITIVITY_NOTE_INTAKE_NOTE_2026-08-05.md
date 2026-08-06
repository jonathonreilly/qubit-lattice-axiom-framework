# Historic intake: R = Omega_DM / Omega_b : Sensitivity to Transport Parameters

Date: 2026-08-05
Authority: none
Audit: unset
Claim type: historic_no_go
Stratum: branch_only_never_mainlined
Era: april_pre_reset

Status: HISTORIC INTAKE under the 2026-08-05 owner directive (pull historic
science iff relevant and/or valuable; pulled items enter the ledger and are
audited). This wrapper registers a claim from the repo's unledgered history.
The wrapper asserts nothing beyond what the pinned original states; the
original's own scope, caveats and era conventions govern. Independent audit
required before any effective status.

## The claim (as stated by the original, supervisor-compressed)

The hypothesis that R depends on eta only logarithmically is falsified: eta is exactly proportional to the transport prefactor P = D_q T/(v_w L_w T) and R exactly inversely proportional to eta, so dR/R = |dP/P| with no logarithmic suppression - giving dR/R = 66% (D_q T), 300% (v_w), 62% (L_w T) and 653% combined, versus <10% from all other sources.

Original verdict: R remains an O(1) framework prediction but is NOT derived to 10% precision; the transport lane does not close from insensitivity.
Scope: Uses the framework's own central transport values (D_q T = 3.1, v_w = 0.014, L_w T = 13) with their stated bands; the dominant v_w spread comes from T_n/T_c in [0.95, 0.99].
Escape conditions (negative claims): The negative is escapable by narrowing the transport bands: pinning T_n/T_c from the framework V_eff (collapsing v_w from 8x to ~1.5x), NLO ladder-resummed D_q T, or accepting an O(1) prediction; the note notes eta = eta_obs crosses at v/T ~ 0.52, inside the 0.56 +/- 0.05 band.

## Why pulled (supervisor decision, on the record)

Definitive sensitivity no-go: eta exactly proportional to the transport prefactor, R NOT derived to 10% — falsifies the insensitivity hypothesis its siblings lean on; 40x tension at central values; escapes priced.

## Provenance (pinned)

- Original path: `docs/DM_R_SENSITIVITY_NOTE.md`
- Source commit: `52efc7b06fa0487bda853cfc98a0f169cf698747`
- git blob: `19cdeff1ad9e5687add65286c1f4919627f10a41`
- sha256: `f4ebabc026909745d2ba9c072019895c6e7cade082e8ccd2006c18e8860114eb`
- Lines: 179; runners named: scripts/frontier_dm_r_sensitivity.py

## Attached evidence (registered with, not as, this claim)

- `docs/DM_TRANSPORT_DERIVED_NOTE.md` — Transport-closed claim whose insensitivity finding 402 directly contradicts — pair to audit.
- `docs/DM_VW_DERIVATION_NOTE.md` — v_w derivation claiming NOT IMPORTED while using imported R_NP — flag carried.
- `docs/ETA_FROM_FRAMEWORK_NOTE.md` — Six-input eta scorecard; its insensitivity framing is what 402 falsifies.

## Flags carried

At the framework's own central transport values eta ~ 2.4e-7, about 400x larger than eta_obs = 6.1e-10, giving R ~ 0.01 rather than ~5.

## Audit fields

```yaml
audit_required_before_effective_retained: true
bare_retained_allowed: false
historic_intake: true
intake_directive: owner_2026-08-05
```

Independent audit still required.
