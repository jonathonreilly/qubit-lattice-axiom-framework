# Historic intake: Periodic Torus Audit - Shapiro Delay Fix Note

Date: 2026-08-05
Authority: none
Audit: unset
Claim type: meta
Stratum: branch_only_never_mainlined
Era: april_pre_reset

Status: HISTORIC INTAKE under the 2026-08-05 owner directive (pull historic
science iff relevant and/or valuable; pulled items enter the ledger and are
audited). This wrapper registers a claim from the repo's unledgered history.
The wrapper asserts nothing beyond what the pinned original states; the
original's own scope, caveats and era conventions govern. Independent audit
required before any effective status.

## The claim (as stated by the original, supervisor-compressed)

Fixes the single confirmed TRUE BUG: frontier_shapiro_delay​.py's 1D periodic ring driver used raw math.hypot for Hamiltonian hopping weights, giving the wraparound edge weight 1/(n-1) instead of 1/1; a _min_image_hypot helper is added and _build_L/_build_H updated.

## Why pulled (supervisor triage decision of 2026-08-05, provenance not authority)

The reasons below are the supervisor's selection rationale; they carry no claim status and are not evidence about the original's validity.

Real bug fixed in a published science runner (Shapiro-delay wraparound weight) — the periodic-torus audit closed at 0; audit work order on consumers.

## Provenance (pinned)

- Original path: `docs/PERIODIC_TORUS_AUDIT_SHAPIRO_DELAY_FIX_NOTE_2026-04-24.md`
- Source commit: `24c59e034ec99d92123a6f328333c105149c1d8b`
- git blob: `3202329b65c78fd2ad68715fd2668a91a8f6006b`
- sha256: `5e35f28f8790a70b4991840b1934a9db6c64ad4b3ec3730b0fd14830a3355f1a`
- Archived original (byte-exact, sha256-verified at generation): [../../archive_unlanded/historic_intake_originals/branch04/1259_PERIODIC_TORUS_AUDIT_SHAPIRO_DELAY_FIX_NOTE_2026-04-24.md](../../archive_unlanded/historic_intake_originals/branch04/1259_PERIODIC_TORUS_AUDIT_SHAPIRO_DELAY_FIX_NOTE_2026-04-24.md)
- Lines: 140; runners named: historic runner (unpinned, not in this packet): `scripts/frontier_shapiro_delay​.py`; historic runner (unpinned, not in this packet): `scripts/frontier_periodic_torus_diagnostics_audit​.py`
- Note: `.py` tokens in this wrapper's rendered fields are display-neutralized with a zero-width split for citation-graph hygiene (no current-tree runner may bind); the byte-exact original wording is pinned in the triage decisions/extraction JSONL files and in the archived original.

## Attached evidence (registered with, not as, this claim)

- `docs/PERIODIC_TORUS_AUDIT_BATCH_1_MANUAL_REVIEW_NOTE_2026-04-24.md` — Manual review of the 9 candidates.
- `docs/PERIODIC_TORUS_DIAGNOSTICS_CODE_AUDIT_NOTE_2026-04-24.md` — The systematic bug-recurrence scan.

## Triage extraction notes (2026-08-05/08, not from the original)

Written at triage/extraction time; NOT part of the pinned original, carries no authority, and is input for the future auditor only.

- Extraction verdict (triage compression; may reflect later context): The periodic-torus audit NEEDS_REVIEW count is now 0 (5/5 PASS), norm = 1.000000 across all three drivers, and the active-queue item is eligible for closure pending reviewer acceptance.
- Extraction scope (triage compression; may reflect later context): One inline fix using only math and indexing.
- Extraction red flags: Documents that a published Shapiro-delay runner carried a wraparound-weight bug.
- Supersession (as known at extraction): Closes the true bug identified in the batch-1 manual review (idx_pos 1258).

## Audit fields

```yaml
audit_required_before_effective_retained: true
bare_retained_allowed: false
historic_intake: true
historic_claim_class: historic_log_like
intake_directive: owner_2026-08-05
```

Independent audit still required.
