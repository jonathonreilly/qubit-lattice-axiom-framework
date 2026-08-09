# Historic intake: Right-Handed Fermions from the 4D Taste Space

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

61/61 checks: C^8 has zero SU(2) singlets and no chirality operator (G5_3D squares to -I, eigenvalues +/-i), wedge^2(C^8) supplies e_R and d_R but not u_R (Y=+4/3 absent, needs degree 4); the 4D taste space C^16 splits by gamma_5 into C^8_L + C^8_R, and anomaly cancellation uniquely fixes u_R(+4/3), d_R(-2/3), e_R(-2), nu_R(0) with all six anomaly conditions PASS.

Original verdict: Right-handed fermions do not arise from a new graph-canonical derivation; they come from the 4D chirality structure with quantum numbers fixed by anomaly cancellation as in the SM itself.
Scope: Staggered lattice taste space in d=3 versus d=3+1; depends on frontier_su3_formal_theorem​.py and frontier_chiral_completion​.py (32/32 PASS).
Escape conditions (negative claims): The C^8 no-go is escaped by the temporal direction: adding it gives a proper involution gamma_5 and doubles the taste space.

## Why pulled (supervisor triage decision of 2026-08-05, provenance not authority)

The reasons below are the supervisor's selection rationale; they carry no claim status and are not evidence about the original's validity.

The right-handed terminal: C^8 has zero SU(2) singlets and no chirality operator — RH matter needs the 4D step; 61/61 with the charge-fixing concession.

## Provenance (pinned)

- Original path: `docs/RIGHT_HANDED_SECTOR_NOTE.md`
- Source commit: `6071b71655f19fcb3ea35e2cbb1e79fae219d0fc`
- git blob: `52380defce0ebfd042bf219623f8c641c1331e49`
- sha256: `56617d9194b6cd9a6e65bdbdcaa0023515b317d708424525069ebe93fae4d947`
- Archived original (byte-exact, sha256-verified at generation): [../../archive_unlanded/historic_intake_originals/branch06/1833_RIGHT_HANDED_SECTOR_NOTE.md](../../archive_unlanded/historic_intake_originals/branch06/1833_RIGHT_HANDED_SECTOR_NOTE.md)
- Lines: 153; runners named: historic runner (unpinned, not in this packet): `scripts/frontier_right_handed_sector​.py`; historic runner (unpinned, not in this packet): `scripts/frontier_su3_formal_theorem​.py`; historic runner (unpinned, not in this packet): `scripts/frontier_chiral_completion​.py`
- Note: `.py` tokens in this wrapper's rendered fields are display-neutralized with a zero-width split for citation-graph hygiene (no current-tree runner may bind); the byte-exact original wording is pinned in the triage decisions/extraction JSONL files and in the archived original.

## Attached evidence (registered with, not as, this claim)

- none

## Triage extraction notes (2026-08-05/08, not from the original)

Written at triage/extraction time; NOT part of the pinned original, carries no authority, and is input for the future auditor only.

- Extraction red flags: Concedes the right-handed charges are fixed by the same mechanism as in the SM (anomaly cancellation), i.e. not a first-principles lattice derivation.
- Supersession (as known at extraction): Resolves the codex gate-1 search negative; FAMILY TERMINAL for the right-handed-sector question, superseding the composite route.

## Audit fields

```yaml
audit_required_before_effective_retained: true
bare_retained_allowed: false
historic_intake: true
historic_claim_class: historic_theorem
intake_directive: owner_2026-08-05
```

Independent audit still required.
