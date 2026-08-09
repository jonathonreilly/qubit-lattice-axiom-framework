# Historic intake: Translation-Eigenvalue Theorem on BZ Corners of Z_L^3

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

On the periodic cubic lattice Z_L^3 with L even, the eight BZ corner states |X_alpha>(x) = L^{-3/2} exp(i pi alpha . x) for alpha in {0,1}^3 are orthonormal simultaneous eigenstates of the three commuting unitary translations with T_mu |X_alpha> = (-1)^{alpha_mu} |X_alpha>, and the eight distinct sign triples exhaust the joint spectrum on the 8-dim BZ-corner subspace.

## Why pulled (supervisor triage decision of 2026-08-05, provenance not authority)

The reasons below are the supervisor's selection rationale; they carry no claim status and are not evidence about the original's validity.

Airtight BZ-corner simultaneous-eigenbasis theorem (70/70) — full 8-dim generalization.

## Provenance (pinned)

- Original path: `docs/TRANSLATION_EIGENVALUE_BZ_CORNERS_NOTE.md`
- Source commit: `2a002cb80cfebe4b8cf150ef75d4d99bb5c6e111`
- git blob: `2c216e6d9e93d271598b76a364debce120a6da05`
- sha256: `59373c40f447fc3e9c1685471faf03684baaa18ac2665f3c1e6f621484a0a85e`
- Archived original (byte-exact, sha256-verified at generation): [../../archive_unlanded/historic_intake_originals/branch07/2077_TRANSLATION_EIGENVALUE_BZ_CORNERS_NOTE.md](../../archive_unlanded/historic_intake_originals/branch07/2077_TRANSLATION_EIGENVALUE_BZ_CORNERS_NOTE.md)
- Lines: 74; runners named: historic runner (unpinned, not in this packet): `scripts/frontier_translation_eigenvalue_bz_corners​.py`
- Note: `.py` tokens in this wrapper's rendered fields are display-neutralized with a zero-width split for citation-graph hygiene (no current-tree runner may bind); the byte-exact original wording is pinned in the triage decisions/extraction JSONL files and in the archived original.

## Attached evidence (registered with, not as, this claim)

- none

## Triage extraction notes (2026-08-05/08, not from the original)

Written at triage/extraction time; NOT part of the pinned original, carries no authority, and is input for the future auditor only.

- Extraction verdict (triage compression; may reflect later context): AIRTIGHT (runner 70/70 PASS) — the full 8-dim generalization of the hw=1 translation result used by the three-generation observable theorem.
- Extraction scope (triage compression; may reflect later context): Pure math on Z_L^3 for L even; no downstream physics claim.
- Extraction red flags: none recorded
- Supersession (as known at extraction): Generalizes (does not supersede) the hw=1 restriction in THREE_GENERATION_OBSERVABLE_THEOREM_NOTE on main; flagged high-reusability.

## Audit fields

```yaml
audit_required_before_effective_retained: true
bare_retained_allowed: false
historic_intake: true
historic_claim_class: historic_theorem
intake_directive: owner_2026-08-05
```

Independent audit still required.
