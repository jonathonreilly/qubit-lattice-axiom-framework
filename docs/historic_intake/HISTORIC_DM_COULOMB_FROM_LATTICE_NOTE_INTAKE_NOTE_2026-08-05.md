# Historic intake: Coulomb Potential from the Lattice Green's Function

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

V(r) = -C_F alpha_s / r is the far-field limit of the Z^3 lattice Laplacian Green's function G(r) = 1/(4 pi |r|) + O(1/|r|^3), so it is a native lattice observable, not a one-gluon-exchange import; 26/26 on-axis points at r in [5,30] agree to <3%, 5/5 off-axis to <0.5%, PASS=61 FAIL=0.

Original verdict: DERIVED - moves V(r) from IMPORTED to NATIVE (IMPORTED count 2 -> 1); sigma_v = pi alpha^2/m^2 stays imported and sigma_v is not closed.
Scope: Weak coupling only (alpha_s = 0.092) where single-gluon exchange dominates the static potential; standard 6-point lattice Laplacian.


## Why pulled (supervisor triage decision of 2026-08-05, provenance not authority)

The reasons below are the supervisor's selection rationale; they carry no claim status and are not evidence about the original's validity.

V(r) = -C_F alpha_s/r derived as the far-field lattice Green's function — an import moved to native with the sigma_v residual honest.

## Provenance (pinned)

- Original path: `docs/DM_COULOMB_FROM_LATTICE_NOTE.md`
- Source commit: `f754d91dd20bff48f072ee64bd1ddb78ed031719`
- git blob: `82aaf8c8330db98c0b5aeef885f7de3e6e19ba11`
- sha256: `32de873c3e8bd0a8eeaf562b32274e8f442fc0862ed791a65e0971d638f5332c`
- Archived original (byte-exact, sha256-verified at generation): [../../archive_unlanded/historic_intake_originals/branch02/344_DM_COULOMB_FROM_LATTICE_NOTE.md](../../archive_unlanded/historic_intake_originals/branch02/344_DM_COULOMB_FROM_LATTICE_NOTE.md)
- Lines: 124; runners named: historic runner (unpinned, not in this packet): `scripts/frontier_dm_coulomb_from_lattice​.py`
- Note: `.py` tokens in this wrapper's rendered fields are display-neutralized with a zero-width split for citation-graph hygiene (no current-tree runner may bind); the byte-exact original wording is pinned in the triage decisions/extraction JSONL files and in the archived original.

## Attached evidence (registered with, not as, this claim)

- none

## Triage extraction notes (2026-08-05/08, not from the original)

Written at triage/extraction time; NOT part of the pinned original, carries no authority, and is input for the future auditor only.

- Extraction red flags: none recorded
- Supersession (as known at extraction): none recorded

## Audit fields

```yaml
audit_required_before_effective_retained: true
bare_retained_allowed: false
historic_intake: true
historic_claim_class: historic_derived
intake_directive: owner_2026-08-05
```

Independent audit still required.
