# Historic intake: Slavnov-Taylor Identity Completion for Gauged Staggered Action

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

Derives the non-perturbative Slavnov-Taylor identity for the gauged staggered action from three exact ingredients (Ward {Eps,D_stag} = 2mI, bipartite {Eps,D_hop} = 0, G5 centrality), giving {Eps, Lambda_mu} = 0 and D[G5] = G5*D[I]; 26/26 PASS with errors 0.0 to 5.4e-16 across five masses and multiple random SU(3) configurations.

## Why pulled (supervisor triage decision of 2026-08-05, provenance not authority)

The reasons below are the supervisor's selection rationale; they carry no claim status and are not evidence about the original's validity.

The Slavnov-Taylor CLOSED declaration on an L=4 lattice — pulled WITH the flag; the Lane-4 closure claim beside 1801/1803's reframes for audit.

## Provenance (pinned)

- Original path: `docs/SLAVNOV_TAYLOR_COMPLETION_NOTE.md`
- Source commit: `ccab562ebde768c686cd884f8c8429266485f466`
- git blob: `3c168aa484fb99fb112940a7784e5a3cebf2ba36`
- sha256: `e4ad3852247d53ef34d794968da72c6549d06f5d9a2ad137b934f8328c4f1ce9`
- Archived original (byte-exact, sha256-verified at generation): [../../archive_unlanded/historic_intake_originals/branch06/1939_SLAVNOV_TAYLOR_COMPLETION_NOTE.md](../../archive_unlanded/historic_intake_originals/branch06/1939_SLAVNOV_TAYLOR_COMPLETION_NOTE.md)
- Lines: 176; runners named: historic runner (unpinned, not in this packet): `scripts/frontier_slavnov_taylor_completion​.py`; historic runner (unpinned, not in this packet): `scripts/frontier_renormalized_yt​.py`; historic runner (unpinned, not in this packet): `scripts/frontier_renormalized_yt_wildcard​.py`
- Note: `.py` tokens in this wrapper's rendered fields are display-neutralized with a zero-width split for citation-graph hygiene (no current-tree runner may bind); the byte-exact original wording is pinned in the triage decisions/extraction JSONL files and in the archived original.

## Attached evidence (registered with, not as, this claim)

- none

## Triage extraction notes (2026-08-05/08, not from the original)

Written at triage/extraction time; NOT part of the pinned original, carries no authority, and is input for the future auditor only.

- Extraction verdict (triage compression; may reflect later context): CLOSED: Lane 4 (y_t matching) is upgraded from BOUNDED to CLOSED with no remaining gaps in the lattice-level argument, leaving only ~1% SM RG uncertainty.
- Extraction scope (triage compression; may reflect later context): d=3 staggered lattice, L=4, arbitrary SU(3) gauge configurations; argument relies on G5 centrality, true only for odd d.
- Extraction red flags: Declares a lane CLOSED on the basis of an L=4 lattice and algebraic identities; the underlying y_t chain still imports alpha_s(M_Pl) as BOUNDED.
- Supersession (as known at extraction): Closes the single open item left by RENORMALIZED_YT_THEOREM_NOTE (idx 1802); FAMILY TERMINAL for the Lane 4 lattice-level argument.

## Audit fields

```yaml
audit_required_before_effective_retained: true
bare_retained_allowed: false
historic_intake: true
historic_claim_class: historic_theorem
intake_directive: owner_2026-08-05
```

Independent audit still required.
