# Historic intake: PMNS Angle-Triple Selector Closure Theorem

Date: 2026-08-05
Authority: none
Audit: unset
Claim type: positive_theorem
Stratum: branch_only_never_mainlined
Era: april_pre_reset

Status: HISTORIC INTAKE under the 2026-08-05 owner directive (pull historic
science iff relevant and/or valuable; pulled items enter the ledger and are
audited). This wrapper registers a claim from the repo's unledgered history.
The wrapper asserts nothing beyond what the pinned original states; the
original's own scope, caveats and era conventions govern. Independent audit
required before any effective status.

## The claim (as stated by the original, supervisor-compressed)

States the three identities as a theorem with unique A-BCC-basin solution (m_*, delta_*, q_+*) = (2/3, 0.9330511, 0.7145018) in the chamber interior q_+ + delta > sqrt(8/3), giving all three PMNS angles within NuFit 5.3 NO 1 sigma with zero PMNS observational inputs; the exact scalar relations SELECTOR^2 = 2/3 and 2 SELECTOR/sqrt3 = 2 sqrt2/3 = E2 are verified.

## Why pulled (supervisor triage decision of 2026-08-05, provenance not authority)

The reasons below are the supervisor's selection rationale; they carry no claim status and are not evidence about the original's validity.

The 'retained-forced, zero PMNS observational inputs' selector claim — pulled WITH the flag that it lists T2K-grounded inputs, against 1588/1590's failures; the contradiction set goes to audit.

## Provenance (pinned)

- Original path: `docs/PMNS_SELECTOR_CLOSURE_THEOREM_NOTE_2026-04-21.md`
- Source commit: `1a7f2e021e83ee881504fceee2668af8e0564aa3`
- git blob: `4d17fe9bbc4103fd1dd108d79419a9838ef8dab2`
- sha256: `e7514b318cc9cd4804e73ccc47c5ca3aade03a444da09afa32c70cead6aa0ce7`
- Archived original (byte-exact, sha256-verified at generation): [../../archive_unlanded/historic_intake_originals/branch05/1581_PMNS_SELECTOR_CLOSURE_THEOREM_NOTE_2026-04-21.md](../../archive_unlanded/historic_intake_originals/branch05/1581_PMNS_SELECTOR_CLOSURE_THEOREM_NOTE_2026-04-21.md)
- Lines: 237; runners named: historic runner (unpinned, not in this packet): `scripts/frontier_pmns_selector_closure​.py`
- Note: `.py` tokens in this wrapper's rendered fields are display-neutralized with a zero-width split for citation-graph hygiene (no current-tree runner may bind); the byte-exact original wording is pinned in the triage decisions/extraction JSONL files and in the archived original.

## Attached evidence (registered with, not as, this claim)

- `docs/PMNS_SELECTOR_CLOSURE_PROPOSAL_README_2026-04-21.md` — Proposal form of the selector closure.

## Triage extraction notes (2026-08-05/08, not from the original)

Written at triage/extraction time; NOT part of the pinned original, carries no authority, and is input for the future auditor only.

- Extraction verdict (triage compression; may reflect later context): The I5 PMNS angle-triple selector gate is retained-forced.
- Extraction scope (triage compression; may reflect later context): Six retained inputs including the affine Hermitian chart, SELECTOR = sqrt6/3, Q_Koide = 2/3, sigma_hier = (2,1,0) and the A-BCC basin - the last of which the note itself says is observationally grounded via T2K CP-phase exclusion.
- Extraction red flags: Title-vs-content: claims 'retained-forced' and 'zero PMNS observational inputs' while listing the A-BCC basin (T2K-grounded) and sigma_hier as inputs, and while the iter chain shows the identities were selected by agreement with PDG angles.
- Supersession (as known at extraction): Theorem-form companion of the proposal README; both rest on the iter-10 identity triple.

## Audit fields

```yaml
audit_required_before_effective_retained: true
bare_retained_allowed: false
historic_intake: true
historic_claim_class: historic_retained_forced_closure_of_the_i5_gate
intake_directive: owner_2026-08-05
```

Independent audit still required.
