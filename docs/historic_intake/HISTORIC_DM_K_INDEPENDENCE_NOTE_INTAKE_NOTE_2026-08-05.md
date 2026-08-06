# Historic intake: DM Relic Density: Independence from Spatial Curvature k

Date: 2026-08-05
Authority: none
Audit: unset
Claim type: historic_theorem
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

Original verdict: Removes the k = 0 flatness bounded assumption from the DM chain; the other bounded assumptions (g_bare = 1, Stosszahlansatz) are unchanged.
Scope: Freeze-out temperatures T_F > 1 MeV in the radiation era, curvature entering only through H.


## Why pulled (supervisor decision, on the record)

k-independence theorem: curvature term 1.2e-29 of radiation at T_F — removes the k=0 bounded input exactly.

## Provenance (pinned)

- Original path: `docs/DM_K_INDEPENDENCE_NOTE.md`
- Source commit: `35b14de168ffbc3a270437c71f9265bd7fe4ece0`
- git blob: `5209addd8f606d540e357fdaef20e244d18e215b`
- sha256: `4dff5f30cc7f16286de5545628fc5c97d5aba605a7b404bc847a93937db945be`
- Lines: 63; runners named: scripts/frontier_dm_k_independence.py, scripts/frontier_dm_friedmann_from_newton.py

## Attached evidence (registered with, not as, this claim)

- none

## Flags carried

none recorded

## Audit fields

```yaml
audit_required_before_effective_retained: true
bare_retained_allowed: false
historic_intake: true
intake_directive: owner_2026-08-05
```

Independent audit still required.
