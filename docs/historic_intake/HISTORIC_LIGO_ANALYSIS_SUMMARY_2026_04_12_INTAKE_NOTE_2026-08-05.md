# Historic intake: LIGO Echo Analysis - Complete Summary

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

Across 73 BBH events with zero free parameters (t_echo = (2R_S/c) ln(R_S/l_Planck), Kerr-corrected), all searches are null: the initial 3.0 sigma at 122 ms was a PSD artifact removed by proper 16 kHz whitening, and the 48-event stack gives 0.41 sigma frozen-star / 1.29 sigma Abedi. Four independent amplitude lanes explain why — absorption R ~ exp(-0.71e38), thermal R ~ 1e-6, no frequency shift, tunneling T ~ 1e-(1e41).

Original verdict: The null echo result is a ZERO-PARAMETER PREDICTION of the framework, not a failure — the evanescent barrier makes the f ~ 1 surface an effectively perfect absorber, so ringdown frequency, damping time and post-merger all match GR.
Scope: Gravitational-wave echo observables only; the framework's distinctive predictions are relocated to short-range gravity below ~38 microns, Lambda ~ 1/a^2, 3 generations = 3 dimensions, exact Born I_3 = 0, and d=3 selection.


## Why pulled (supervisor triage decision of 2026-08-05, provenance not authority)

The reasons below are the supervisor's selection rationale; they carry no claim status and are not evidence about the original's validity.

LIGO 73-event NULL as a zero-parameter prediction: the initial 3.0 sigma was a PSD artifact; four bug fixes recorded — the echo lane's observational terminal (joins 3611/657/416 at audit).

## Provenance (pinned)

- Original path: `docs/LIGO_ANALYSIS_SUMMARY_2026-04-12.md`
- Source commit: `73f2c0d99de03c4ae48a8e3450a3a7edae7d1fe5`
- git blob: `32797dc7dd0a04c513e9fd8d421f65afacee82ef`
- sha256: `a5d50b790a89eab6fe33a6d76ce1849c4052907510c08dd141c46758055362e9`
- Archived original (byte-exact, sha256-verified at generation): [../../archive_unlanded/historic_intake_originals/branch04/1106_LIGO_ANALYSIS_SUMMARY_2026-04-12.md](../../archive_unlanded/historic_intake_originals/branch04/1106_LIGO_ANALYSIS_SUMMARY_2026-04-12.md)
- Lines: 97; runners named: historic runner (unpinned, not in this packet): `scripts/gw_echo_full_catalog(.py)`; historic runner (unpinned, not in this packet): `scripts/gw_echo_matched_filter(.py)`; historic runner (unpinned, not in this packet): `scripts/gw_echo_amplitude_prediction(.py)`; historic runner (unpinned, not in this packet): `scripts/frontier_echo_absorption_mechanism(.py)`; historic runner (unpinned, not in this packet): `scripts/frontier_echo_thermal_reflectivity(.py)`; historic runner (unpinned, not in this packet): `scripts/frontier_echo_frequency_shift(.py)`; historic runner (unpinned, not in this packet): `scripts/frontier_echo_lattice_tunneling(.py)`

## Attached evidence (registered with, not as, this claim)

- none

## Flags carried

Records four separate bug fixes (epsilon formula, Kerr spin parameter, background estimation) each of which changed the picture, and an initial 3 sigma claim that turned out to be an artifact. Does not reproduce Abedi et al.'s 2.9 sigma.

## Audit fields

```yaml
audit_required_before_effective_retained: true
bare_retained_allowed: false
historic_intake: true
historic_claim_class: historic_measurement
intake_directive: owner_2026-08-05
```

Independent audit still required.
