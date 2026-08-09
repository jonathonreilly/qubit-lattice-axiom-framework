# Historic intake: Flavor - the e-mu gap dissolves; the value consolidates to r=1/2 (off-diag/diag)

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

Decomposing the generation Yukawa as Y = a I + b C + b-bar C^2 gives Q = 1/3 + (2/3) r with r = |b|^2/a^2 exactly and theta-independently (verified for r in {0, 1/4, 1/2, 1} and all theta), so the e-mu splitting is set entirely by the Q-orthogonal phase theta and contributes nothing to the value, which consolidates to the single ratio r = 1/2.

## Why pulled (supervisor triage decision of 2026-08-05, provenance not authority)

The reasons below are the supervisor's selection rationale; they carry no claim status and are not evidence about the original's validity.

Exact consolidation: Q = 1/3 + (2/3)r theta-independently — the e-mu gap was a phantom; the target is one condensate ratio.

## Provenance (pinned)

- Original path: `docs/FLAVOR_YUKAWA_DIAG_OFFDIAG_CONSOLIDATION_NOTE_2026-05-29.md`
- Source commit: `4bbf156e6bb0a81ca437fc3020cb5638fc812371`
- git blob: `fa3bbd927ce8603ace2037723a37b42d7ee942a8`
- sha256: `be87e3ba083cd94851bdfedfb22eb24462041811b731dc71238a40ea2eefd718`
- Archived original (byte-exact, sha256-verified at generation): [../../archive_unlanded/historic_intake_originals/branch02/498_FLAVOR_YUKAWA_DIAG_OFFDIAG_CONSOLIDATION_NOTE_2026-05-29.md](../../archive_unlanded/historic_intake_originals/branch02/498_FLAVOR_YUKAWA_DIAG_OFFDIAG_CONSOLIDATION_NOTE_2026-05-29.md)
- Lines: 63; runners named: historic runner (unpinned, not in this packet): `scripts/flavor_yukawa_diag_offdiag_consolidation_2026_05_29​.py`
- Note: `.py` tokens in this wrapper's rendered fields are display-neutralized with a zero-width split for citation-graph hygiene (no current-tree runner may bind); the byte-exact original wording is pinned in the triage decisions/extraction JSONL files and in the archived original.

## Attached evidence (registered with, not as, this claim)

- none

## Triage extraction notes (2026-08-05/08, not from the original)

Written at triage/extraction time; NOT part of the pinned original, carries no authority, and is input for the future auditor only.

- Extraction verdict (triage compression; may reflect later context): The e-mu gap was a phantom; the irreducible target is the single vacuum condensate ratio |b|^2/a^2 = 1/2, now anchored in the full operator rather than an isolated toy.
- Extraction scope (triage compression; may reflect later context): Reconnects the Jahn-Teller (diagonal, C_3-breaking) and Brannen (off-diagonal, C_3-symmetric) pictures as the two parts of one Yukawa; both a and b are vacuum/condensate quantities.
- Extraction red flags: none recorded
- Supersession (as known at extraction): Resolves gap (ii) of FLAVOR_JAHN_TELLER_CUBIC_BREAKING (idx 483) and feeds FLAVOR_GAP_EQUATION_COMPETING_ORDERS (idx 482).

## Audit fields

```yaml
audit_required_before_effective_retained: true
bare_retained_allowed: false
historic_intake: true
historic_claim_class: historic_analysis
intake_directive: owner_2026-08-05
```

Independent audit still required.
