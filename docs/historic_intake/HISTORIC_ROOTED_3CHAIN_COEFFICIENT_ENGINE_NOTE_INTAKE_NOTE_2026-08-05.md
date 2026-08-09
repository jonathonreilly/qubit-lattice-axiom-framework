# Historic intake: Exact Rooted 3-Chain Coefficient Engine for the 3+1 Plaquette Program

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

Corrects an earlier boundary-shellable growth rule (which was false: a chain can need a cell across a temporarily internal face) and gives exact rooted counts through |V| = 5, e.g. N(5,22) = 421432, with root-launch grading showing only k = 1 and k = 3 sectors ({1: 562352, 3: 4292} at n = 5).

Original verdict: The rooted 3-chain engine is the right next gauge-side object, with exact counts and root-launch sectors through five cells.
Scope: Connected rooted 3-chains on the exact 3+1 lattice with q in dV, |V| <= 5; exact integer counts, not Monte Carlo.


## Why pulled (supervisor triage decision of 2026-08-05, provenance not authority)

The reasons below are the supervisor's selection rationale; they carry no claim status and are not evidence about the original's validity.

Corrects a FALSE prior enumeration rule (boundary-shellable growth) with exact rooted counts — correction on the record.

## Provenance (pinned)

- Original path: `docs/ROOTED_3CHAIN_COEFFICIENT_ENGINE_NOTE.md`
- Source commit: `60a264ba93427b648c4c01edb5b2437542b78eb5`
- git blob: `822742f636c68ede0e2faad1684164af75633c4a`
- sha256: `d3bff1b3872c37736871229ecbd15175a329b2244c807fea5ab3249c81b35875`
- Archived original (byte-exact, sha256-verified at generation): [../../archive_unlanded/historic_intake_originals/branch06/1834_ROOTED_3CHAIN_COEFFICIENT_ENGINE_NOTE.md](../../archive_unlanded/historic_intake_originals/branch06/1834_ROOTED_3CHAIN_COEFFICIENT_ENGINE_NOTE.md)
- Lines: 243; runners named: historic runner (unpinned, not in this packet): `scripts/frontier_rooted_3chain_coefficient_engine​.py`
- Note: `.py` tokens in this wrapper's rendered fields are display-neutralized with a zero-width split for citation-graph hygiene (no current-tree runner may bind); the byte-exact original wording is pinned in the triage decisions/extraction JSONL files and in the archived original.

## Attached evidence (registered with, not as, this claim)

- none

## Triage extraction notes (2026-08-05/08, not from the original)

Written at triage/extraction time; NOT part of the pinned original, carries no authority, and is input for the future auditor only.

- Extraction red flags: Records that a prior enumeration rule in the same lane was false, so any counts produced under it were wrong.
- Supersession (as known at extraction): Explicitly corrects an earlier exploratory version of this lane that grew chains only across boundary faces; the quotient version is idx 1755.

## Audit fields

```yaml
audit_required_before_effective_retained: true
bare_retained_allowed: false
historic_intake: true
historic_claim_class: historic_theorem
intake_directive: owner_2026-08-05
```

Independent audit still required.
