# Historic intake: Wilson-Kernel Two-Band Identity Test — Zone Obstruction Removed, O(a) Speed Artifact Measured, And The Volume Wall Demonstrated Directly

Date: 2026-08-05
Authority: none
Audit: unset
Claim type: no_go
Stratum: branch_only_never_mainlined
Era: post_reset_2026_06_29

Status: HISTORIC INTAKE under the 2026-08-05 owner directive (pull historic
science iff relevant and/or valuable; pulled items enter the ledger and are
audited). This wrapper registers a claim from the repo's unledgered history.
The wrapper asserts nothing beyond what the pinned original states; the
original's own scope, caveats and era conventions govern. Independent audit
required before any effective status.

## The claim (as stated by the original, supervisor-compressed)

Executing the staggered no-go's named Wilson escape removes the zone obstruction (band origins (k*_1, k*_2) = (0,0) at every gated point, volume-stable) and gets four of eight gated points fully valid at N=8 with identity ratios 1.042-1.254, but the purpose-built N=10 volume spot at the best point refutes convergence: ratio_I moves 1.042 -> 2.211 (drift 1.17 against tolerance 0.10) and c21 0.863 -> 0.652, with N=10 band-2 failing the own-frame rise condition. The Wilson O(a) speed artifact is measured separately (c_1^2 = 1.12-1.19 at m=0.2, 1.25-1.39 at m=0.4, relaxing to 0.92/0.94 at strong coupling).

Original verdict: The ED route to the two-band identity test is closed on both kernels: the wall is spectral density versus volume, and near-1 identity values at a single volume are finite-size accidents.
Scope: d = 1 gauged Wilson comparator at ED-reachable sizes (N <= 10 Wilson, N <= 16 staggered) with these operator tags; the identity itself is untested, not refuted.
Escape conditions (negative claims): Three named escapes: (a) tensor-network/DMRG at N ~ 40-100, called THE route; (b) fit-free identity observables (form-factor/boost matrix elements) needing only P = 0 states; (c) smeared variational tag bases to push the mixing scale down at fixed volume.

## Why pulled (supervisor triage decision of 2026-08-05, provenance not authority)

The reasons below are the supervisor's selection rationale; they carry no claim status and are not evidence about the original's validity.

Two-kernel two-band terminal: the wall is exponential ED cost, not physics — three named escapes (DMRG etc.); own steelman rejected on the record.

## Provenance (pinned)

- Original path: `docs/WILSON_TWO_BAND_MASS_ENERGY_EQUIVALENCE_IDENTITY_NOTE_2026-07-08.md`
- Source commit: `547c3c4e477173636b1469798967ed0500f13aac`
- git blob: `881b59d547ebda83073e77e2f3e41b0e61696fbd`
- sha256: `8b33916e9223539bfbcc4c3622fe58b63ec2b8211191da3c01c39173b6b1abbf`
- Archived original (byte-exact, sha256-verified at generation): [../../archive_unlanded/historic_intake_originals/branch07/2128_WILSON_TWO_BAND_MASS_ENERGY_EQUIVALENCE_IDENTITY_NOTE_2026-07-08.md](../../archive_unlanded/historic_intake_originals/branch07/2128_WILSON_TWO_BAND_MASS_ENERGY_EQUIVALENCE_IDENTITY_NOTE_2026-07-08.md)
- Lines: 186; runners named: historic runner (unpinned, not in this packet): `scripts/wilson_two_band_identity_own_frame_2026_07_08(.py)`

## Attached evidence (registered with, not as, this claim)

- `docs/WILSON_STAGGERED_DOBRUSHIN_CERTIFICATE_BOUNDARY_CRITICAL_SCALING_NO_GO_2026-07-12.md` — Dobrushin sharpening + necessity bound.

## Flags carried

Records and rejects its own steelman (gating the four valid N=8 points would 'launder finite-size accidents into a claim') and documents two supervisor spec bugs from run 1 (cache print tolerance; an O(a^2) artifact gate applied to an O(a) kernel).

## Audit fields

```yaml
audit_required_before_effective_retained: true
bare_retained_allowed: false
historic_intake: true
historic_claim_class: historic_no_go
intake_directive: owner_2026-08-05
```

Independent audit still required.
