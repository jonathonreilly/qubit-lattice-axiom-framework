# Historic intake: DM Relic Density: Independence from Spatial Curvature k

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

The curvature term k/a^2 is 1.2e-29 of the radiation term at T = 40 GeV, so for k in {-1,0,+1} and any T_F > 1 MeV, |Omega_DM(k) - Omega_DM(0)|/Omega_DM(0) < 10^-20; the x_F solver returns identical values for k=0 and k=+1 to machine precision.

## Why pulled (supervisor triage decision of 2026-08-05, provenance not authority)

The reasons below are the supervisor's selection rationale; they carry no claim status and are not evidence about the original's validity.

k-independence theorem: curvature term 1.2e-29 of radiation at T_F — removes the k=0 bounded input exactly.

## Provenance (pinned)

- Original path: `docs/DM_K_INDEPENDENCE_NOTE.md`
- Source commit: `35b14de168ffbc3a270437c71f9265bd7fe4ece0`
- git blob: `5209addd8f606d540e357fdaef20e244d18e215b`
- sha256: `4dff5f30cc7f16286de5545628fc5c97d5aba605a7b404bc847a93937db945be`
- Archived original (byte-exact, sha256-verified at generation): [../../archive_unlanded/historic_intake_originals/branch02/367_DM_K_INDEPENDENCE_NOTE.md](../../archive_unlanded/historic_intake_originals/branch02/367_DM_K_INDEPENDENCE_NOTE.md)
- Lines: 63; runners named: historic runner (unpinned, not in this packet): `scripts/frontier_dm_k_independence​.py`; historic runner (unpinned, not in this packet): `scripts/frontier_dm_friedmann_from_newton​.py`
- Note: `.py` tokens in this wrapper's rendered fields are display-neutralized with a zero-width split for citation-graph hygiene (no current-tree runner may bind); the byte-exact original wording is pinned in the triage decisions/extraction JSONL files and in the archived original.

## Attached evidence (registered with, not as, this claim)

- none

## Triage extraction notes (2026-08-05/08, not from the original)

Written at triage/extraction time; NOT part of the pinned original, carries no authority, and is input for the future auditor only.

- Extraction verdict (triage compression; may reflect later context): Removes the k = 0 flatness bounded assumption from the DM chain; the other bounded assumptions (g_bare = 1, Stosszahlansatz) are unchanged.
- Extraction scope (triage compression; may reflect later context): Freeze-out temperatures T_F > 1 MeV in the radiation era, curvature entering only through H.
- Extraction red flags: none recorded
- Supersession (as known at extraction): Retires check 11 (k=0 flatness) of frontier_dm_friedmann_from_newton​.py.

## Audit fields

```yaml
audit_required_before_effective_retained: true
bare_retained_allowed: false
historic_intake: true
historic_claim_class: historic_theorem
intake_directive: owner_2026-08-05
```

Independent audit still required.
