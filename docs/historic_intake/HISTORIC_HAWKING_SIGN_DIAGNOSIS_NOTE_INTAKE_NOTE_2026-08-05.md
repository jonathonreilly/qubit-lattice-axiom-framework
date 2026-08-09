# Historic intake: Diagnosis: T-kappa Sign Reversal in 3D Bogoliubov Quench

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

Five hypotheses tested to explain why T versus kappa has slope -0.43 (R^2 = 0.98) while T versus 1/R_h is positive: kappa is computed exactly (R^2 = 1.000000), the spectrum is approximately thermal, the sign is negative at L = 8, 10, 12 and in the weak-quench regime - and H5 finds the cause, since replacing the hopping reduction with an onsite potential quench flips the slope to +0.48 (R^2 = 0.92), the correct Hawking sign.

## Why pulled (supervisor triage decision of 2026-08-05, provenance not authority)

The reasons below are the supervisor's selection rationale; they carry no claim status and are not evidence about the original's validity.

The sign diagnosis: the lane's headline T-vs-kappa observable measured bandwidth compression, not radiation — retracts the 3D quench's physical reading.

## Provenance (pinned)

- Original path: `docs/HAWKING_SIGN_DIAGNOSIS_NOTE.md`
- Source commit: `623e6bd163ba604cf6200fed9418bac12a192705`
- git blob: `60a41bf7e2268e2ba1d0bb8913ca10c3f075f578`
- sha256: `5969dc3ff44dcfdfafdc01719b4677b8835efd6f9ab1c586bc3ee43545ed34ca`
- Archived original (byte-exact, sha256-verified at generation): [../../archive_unlanded/historic_intake_originals/branch02/674_HAWKING_SIGN_DIAGNOSIS_NOTE.md](../../archive_unlanded/historic_intake_originals/branch02/674_HAWKING_SIGN_DIAGNOSIS_NOTE.md)
- Lines: 109; runners named: historic runner (unpinned, not in this packet): `scripts/frontier_hawking_sign_diagnosis​.py`; historic runner (unpinned, not in this packet): `scripts/frontier_hawking_3d_quench​.py`
- Note: `.py` tokens in this wrapper's rendered fields are display-neutralized with a zero-width split for citation-graph hygiene (no current-tree runner may bind); the byte-exact original wording is pinned in the triage decisions/extraction JSONL files and in the archived original.

## Attached evidence (registered with, not as, this claim)

- none

## Triage extraction notes (2026-08-05/08, not from the original)

Written at triage/extraction time; NOT part of the pinned original, carries no authority, and is input for the future auditor only.

- Extraction verdict (triage compression; may reflect later context): Hopping reduction compresses the bandwidth so the fitted T tracks energy per particle rather than radiation intensity; the onsite potential quench, which shifts eigenvalues like gravitational redshift, is the better analog.
- Extraction scope (triage compression; may reflect later context): Applies to the 3D spherical quench with tanh profiles at fixed sigma = 2.0.
- Extraction red flags: Establishes that the lane's own headline observable was measuring the wrong quantity - kappa carries no independent geometric information at fixed sigma, being just a rescaled copy of quench strength.
- Supersession (as known at extraction): Diagnoses and effectively retracts the physical reading of the 3D quench (idx 671): the Fermi-Dirac T is NOT the Hawking temperature for hopping quenches, and future work should use potential-based or bandwidth-preserving quenches.

## Audit fields

```yaml
audit_required_before_effective_retained: true
bare_retained_allowed: false
historic_intake: true
historic_claim_class: historic_analysis
intake_directive: owner_2026-08-05
```

Independent audit still required.
