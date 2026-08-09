# Historic intake: Frozen Stars: Compact Object Predictions

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

Five probes of self-consistent Hartree frozen stars: 3D scaling gives M_Ch ~ 1.9 M_sun matching the observed NS limit, R_frozen/R_s can be as low as ~0.05 (20x more compact than a black hole) with no horizon, QNMs are discrete rather than a continuous overtone series, post-merger echoes are predicted, and the surface temperature is ~70x T_Hawking (4e-7 K for 10 M_sun).

Original verdict: The lattice framework predicts a fundamentally different collapse endpoint than GR - no horizons, a Planck-scale surface, and several observable differences (GW echoes, thermal emission, EHT shadow).
Scope: 1D lattice model missing 3D geometry (angular momentum, centrifugal barrier, radiation pressure); N_crit scaling rests on only two collapse data points; temperature estimates depend on identifying lattice units with Planck units.


## Why pulled (supervisor triage decision of 2026-08-05, provenance not authority)

The reasons below are the supervisor's selection rationale; they carry no claim status and are not evidence about the original's validity.

FROZEN STARS founding claim (M_Ch ~ 1.9 M_sun, no-horizon endpoint) — cross-flagged at intake with the echo post-hoc zeroing (416), the search (657) and the 3080/3091 attacks.

## Provenance (pinned)

- Original path: `docs/FROZEN_STARS_NOTE.md`
- Source commit: `20c77d40dc98abf40437c3be9225291ef9ae0ba9`
- git blob: `96329080aa3280bc5efe8816bfb6d90dd4b74222`
- sha256: `079bb05a675decf114ee3de844f90ad529414570d5ddb22963e06bbcd5f3a8e7`
- Archived original (byte-exact, sha256-verified at generation): [../../archive_unlanded/historic_intake_originals/branch02/515_FROZEN_STARS_NOTE.md](../../archive_unlanded/historic_intake_originals/branch02/515_FROZEN_STARS_NOTE.md)
- Lines: 153; runners named: historic runner (unpinned, not in this packet): `scripts/frontier_frozen_stars​.py`
- Note: `.py` tokens in this wrapper's rendered fields are display-neutralized with a zero-width split for citation-graph hygiene (no current-tree runner may bind); the byte-exact original wording is pinned in the triage decisions/extraction JSONL files and in the archived original.

## Attached evidence (registered with, not as, this claim)

- none

## Triage extraction notes (2026-08-05/08, not from the original)

Written at triage/extraction time; NOT part of the pinned original, carries no authority, and is input for the future auditor only.

- Extraction red flags: Self-listed caveats include a poorly constrained N_crit scaling (2 points) and a 1D model; the echo prediction it advertises as detectable is nullified by a sibling note.
- Supersession (as known at extraction): Its headline post-merger echo prediction is later given amplitude ZERO by ECHO_PREDICTION_RESOLVED_2026-04-12 (idx 416) via the evanescent barrier.

## Audit fields

```yaml
audit_required_before_effective_retained: true
bare_retained_allowed: false
historic_intake: true
historic_claim_class: historic_measurement
intake_directive: owner_2026-08-05
```

Independent audit still required.
