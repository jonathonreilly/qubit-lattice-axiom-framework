# Historic intake: The measurement was right and the floor was a grid line: the deposition comparator re-audited — Cycle 920

Date: 2026-08-05
Authority: none
Audit: unset
Claim type: bounded_theorem
Stratum: branch_only_never_mainlined
Era: post_reset_2026_06_29

Status: HISTORIC INTAKE under the 2026-08-05 owner directive (pull historic
science iff relevant and/or valuable; pulled items enter the ledger and are
audited). This wrapper registers a claim from the repo's unledgered history.
The wrapper asserts nothing beyond what the pinned original states; the
original's own scope, caveats and era conventions govern. Independent audit
required before any effective status.

## The claim (as stated by the original, supervisor-compressed)

Independent re-implementation reproduces the never-checked deposition comparator exactly (22/22 quantities across three implementations) but shows the 0.20 theta floor it was read to support is a GRID ARTIFACT: the true crossing is theta = 0.140516818611 (bisected to 1e-14, joint fill monotone), 0.20 is merely the smallest of six hand-chosen thresholds above it with nothing swept in (0.1, 0.2), the criterion's namesake quantity cancels algebraically out of its own definition, and the sparse window rests on one event plus eleven structurally-zero cells.

## Why pulled (supervisor triage decision of 2026-08-05, provenance not authority)

The reasons below are the supervisor's selection rationale; they carry no claim status and are not evidence about the original's validity.

Exact re-implementation (22/22 reproduced) showing the 0.20 theta floor — load-bearing across the lineage — is a GRID ARTIFACT: the measurement was right and the floor was a grid line; correction against landed readings.

## Provenance (pinned)

- Original path: `docs/DEPOSITION_REPRODUCED_FLOOR_GRID_ARTIFACT_CYCLE920_BOUNDED_THEOREM_NOTE_2026-07-28.md`
- Source commit: `cca3e398f01ff4cc05ffb226a1ce766d6e5c637a`
- git blob: `690197848d7625d109b735f5844969551ef86842`
- sha256: `7d635142e8c4beaf66ca360fbae05f8db69910d94e68ea21b575055e7c7c7dce`
- Archived original (byte-exact, sha256-verified at generation): [../../archive_unlanded/historic_intake_originals/branch01/299_DEPOSITION_REPRODUCED_FLOOR_GRID_ARTIFACT_CYCLE920_BOUNDED_THEOREM_NOTE_2026-07-28.md](../../archive_unlanded/historic_intake_originals/branch01/299_DEPOSITION_REPRODUCED_FLOOR_GRID_ARTIFACT_CYCLE920_BOUNDED_THEOREM_NOTE_2026-07-28.md)
- Lines: 177; runners named: historic runner (unpinned, not in this packet): `../scripts/frontier_cycle920_deposition_independent_check_2026_07_28​.py`; historic runner (unpinned, not in this packet): `../scripts/frontier_cycle920_deposition_reaudit_2026_07_28​.py`; historic runner (unpinned, not in this packet): `frontier_cycle920_deposition_independent_check_2026_07_28​.py`; historic runner (unpinned, not in this packet): `frontier_cycle920_deposition_reaudit_2026_07_28​.py`
- Note: `.py` tokens in this wrapper's rendered fields are display-neutralized with a zero-width split for citation-graph hygiene (no current-tree runner may bind); the byte-exact original wording is pinned in the triage decisions/extraction JSONL files and in the archived original.

## Attached evidence (registered with, not as, this claim)

- `docs/DEPOSITION_CONSTANT_CONSTRAINT_MAP_2026-07-08.md` — Deposition-constant bracketing synthesis.
- `docs/DEPOSITION_PER_ACTIVITY_KAPPA_BOUNDED_NOTE_2026-07-08.md` — kappa(theta) yield measurement with the floor finding.

## Triage extraction notes (2026-08-05/08, not from the original)

Written at triage/extraction time; NOT part of the pinned original, carries no authority, and is input for the future auditor only.

- Extraction verdict (triage compression; may reflect later context): The measurement was right and the floor was a grid line.
- Extraction scope (triage compression; may reflect later context): Owner-directed mass-lane closure, window 2b; one premise of the Cycle-916 dictionary is corrected, not retracted.
- Extraction red flags: A load-bearing floor used across the lineage turns out to be an artifact of the swept grid; the criterion's namesake quantity cancels out of its own definition.
- Supersession (as known at extraction): Re-audits the 2026-07-08 deposition comparator and corrects the lineage's 0.20 floor reading.

## Audit fields

```yaml
audit_required_before_effective_retained: true
bare_retained_allowed: false
historic_intake: true
historic_claim_class: historic_bounded_theorem
intake_directive: owner_2026-08-05
```

Independent audit still required.
