# Historic intake: Diagnosis: T-kappa Sign Reversal in 3D Bogoliubov Quench

Date: 2026-08-05
Authority: none
Audit: unset
Claim type: historic_analysis
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

Original verdict: Hopping reduction compresses the bandwidth so the fitted T tracks energy per particle rather than radiation intensity; the onsite potential quench, which shifts eigenvalues like gravitational redshift, is the better analog.
Scope: Applies to the 3D spherical quench with tanh profiles at fixed sigma = 2.0.


## Why pulled (supervisor decision, on the record)

The sign diagnosis: the lane's headline T-vs-kappa observable measured bandwidth compression, not radiation — retracts the 3D quench's physical reading.

## Provenance (pinned)

- Original path: `docs/HAWKING_SIGN_DIAGNOSIS_NOTE.md`
- Source commit: `623e6bd163ba604cf6200fed9418bac12a192705`
- git blob: `60a41bf7e2268e2ba1d0bb8913ca10c3f075f578`
- sha256: `5969dc3ff44dcfdfafdc01719b4677b8835efd6f9ab1c586bc3ee43545ed34ca`
- Lines: 109; runners named: scripts/frontier_hawking_sign_diagnosis.py, scripts/frontier_hawking_3d_quench.py

## Attached evidence (registered with, not as, this claim)

- none

## Flags carried

Establishes that the lane's own headline observable was measuring the wrong quantity - kappa carries no independent geometric information at fixed sigma, being just a rescaled copy of quench strength.

## Audit fields

```yaml
audit_required_before_effective_retained: true
bare_retained_allowed: false
historic_intake: true
intake_directive: owner_2026-08-05
```

Independent audit still required.
