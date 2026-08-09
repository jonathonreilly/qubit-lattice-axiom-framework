# Historic intake: Universal Radial Shell Profile for the Strong-Field Matching Law

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

At cutoff radius R = 4 the charge-normalized shell-radial average k_shell(r) = sigma_rad(r)/Q is identical to machine precision across the exact local O_h source family and the exact finite-rank source family, agreeing on all twelve shared shell radii (sqrt(10) through 5), so sigma_rad = Q k_shell with one universal kernel.

Original verdict: The radial sewing-shell profile is universal rather than family-dependent, narrowing the strong-field problem to interpreting one kernel; it does not close the continuum/effective-stress interpretation, the nonlinear 4D theorem, or theorem-grade control of the anisotropic correction.
Scope: The two exact source families present on the codex/review-active branch at R = 4.


## Why pulled (supervisor triage decision of 2026-08-05, provenance not authority)

The reasons below are the supervisor's selection rationale; they carry no claim status and are not evidence about the original's validity.

Shell-radial universality: k_shell identical to machine precision across both exact source families — with the two-family caveat flagged.

## Provenance (pinned)

- Original path: `docs/UNIVERSAL_SHELL_PROFILE_NOTE.md`
- Source commit: `83def234b7eddc1d23f284af42390ea852440421`
- git blob: `ee81764b31fb371462aac50daf70df84318bb62e`
- sha256: `1240b882b987c13dcaa6ffdf7d7e5842e32491411840d8172ad3a1b3e0ebbaa0`
- Archived original (byte-exact, sha256-verified at generation): [../../archive_unlanded/historic_intake_originals/branch07/2093_UNIVERSAL_SHELL_PROFILE_NOTE.md](../../archive_unlanded/historic_intake_originals/branch07/2093_UNIVERSAL_SHELL_PROFILE_NOTE.md)
- Lines: 107; runners named: historic runner (unpinned, not in this packet): `scripts/frontier_universal_shell_profile​.py`
- Note: `.py` tokens in this wrapper's rendered fields are display-neutralized with a zero-width split for citation-graph hygiene (no current-tree runner may bind); the byte-exact original wording is pinned in the triage decisions/extraction JSONL files and in the archived original.

## Attached evidence (registered with, not as, this claim)

- none

## Triage extraction notes (2026-08-05/08, not from the original)

Written at triage/extraction time; NOT part of the pinned original, carries no authority, and is input for the future auditor only.

- Extraction red flags: Universality is demonstrated across only two source families at a single cutoff radius R = 4, so 'universal' is scoped narrower than the title suggests.
- Supersession (as known at extraction): Removes the family-dependence ambiguity left by the earlier sewing-shell results; the successor target is deriving k_shell from microscopic lattice dynamics.

## Audit fields

```yaml
audit_required_before_effective_retained: true
bare_retained_allowed: false
historic_intake: true
historic_claim_class: historic_bounded_result
intake_directive: owner_2026-08-05
```

Independent audit still required.
