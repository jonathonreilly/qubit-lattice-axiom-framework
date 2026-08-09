# Historic intake: axiom-reconciliation - resume notes (2026-07-12)

Date: 2026-08-05
Authority: none
Audit: unset
Claim type: meta
Stratum: pack_science_family
Era: post_reset_2026_06_29

Status: HISTORIC INTAKE under the 2026-08-05 owner directive (pull historic
science iff relevant and/or valuable; pulled items enter the ledger and are
audited). This wrapper registers a claim from the repo's unledgered history.
The wrapper asserts nothing beyond what the pinned original states; the
original's own scope, caveats and era conventions govern. Independent audit
required before any effective status.

## The claim (as stated by the original, supervisor-compressed)

Campaign state for the axiom-reconciliation rescan: a regenerable index at TOTAL HARD=141 SOFT_ONLY=740 RETAINED_STATUS_HARD=8 at base commit 7b9260b85, with 30 codex batches classifying the 141 hard files into a frozen five-class rubric (REKEY / CONTENT-FLIP / REOPENED-WALL / HISTORICAL-OK / DELIBERATE-OLD-TEXT, severity tie-break flip/wall > rekey > historical).

## Why pulled (supervisor triage decision of 2026-08-05, provenance not authority)

The reasons below are the supervisor's selection rationale; they carry no claim status and are not evidence about the original's validity.

Work order already surfaced to the owner: the axiom-reconciliation rescan index at TOTAL HARD=141 / SOFT_ONLY=740 / RETAINED_STATUS_HARD=8 (base 7b9260b85) - eight files with retained audit status hard-reference deleted or changed axiom text. The invalidation-pipeline gap; deliverable TSVs pinned under logs/runner-cache/recon_triage/.

## Provenance (pinned)

- Original path: `.claude/science/physics-loops/axiom-reconciliation/RESUME.md`
- Source commit: `2be2924f52bc045174d08df2841d100e300ecd0e`
- git blob: `1a605e1e1a9ff7c64bc4c98941120fbe6e3936b9`
- sha256: `485256eec2662d49ad5dce05840f0d2b2b9b827867355833edf21e086a57ec44`
- Archived original (byte-exact, sha256-verified at generation): [../../archive_unlanded/historic_intake_originals/packsci01/10253_RESUME.md](../../archive_unlanded/historic_intake_originals/packsci01/10253_RESUME.md)
- Lines: 40; runners named: historic runner (unpinned, not in this packet): `scripts/axiom_reconciliation_rescan_2026_07_12​.py`
- Note: `.py` tokens in this wrapper's rendered fields are display-neutralized with a zero-width split for citation-graph hygiene (no current-tree runner may bind); the byte-exact original wording is pinned in the triage decisions/extraction JSONL files and in the archived original.

## Attached evidence (registered with, not as, this claim)

- none

## Cross-stratum flags (inert text; machine-readable relations in the audit fields)

- Cross-stratum reference from packsci03 idx 10833 (`.claude/science/physics-loops/repo-state-scrub-20260725/phase1_registry_integrity.md`, decision PULL) — SYSTEMIC INTEGRITY MEASUREMENT: ALL THREE registered derivation obligations have machine records that MISMATCH their source notes (6 distinct mismatches); of 4 registered axiom/primitive surfaces ...; documents the mass invalidation event that destroyed 202 clean no-go audits; the no_go count's cause is STRUCTURAL (the route exists in code and was never wired). Recommended repair set R1+R3+R4+R5 costed in-pack. Companion to the recon-rescan gap pulled from packsci01.

## Triage extraction notes (2026-08-05/08, not from the original)

Written at triage/extraction time; NOT part of the pinned original, carries no authority, and is input for the future auditor only.

- Extraction verdict (triage compression; may reflect later context): Deliverables are committed TSVs under logs/runner-cache/recon_triage/; supervisor line-reviews every worker row before any edit lands.
- Extraction scope (triage compression; may reflect later context): Files whose load-bearing quotes or citations reference deleted or changed axiom content.
- Extraction red flags: 141 files carry hard references to deleted or changed axiom content, and 8 of them hold retained audit status - i.e. retained claims resting on axiom text that no longer exists, and the invalidation pipeline did not catch it.
- Supersession (as known at extraction): Records that the 8 hard files WITH RETAINED AUDIT STATUS are an INVALIDATION-PIPELINE GAP to be flagged to the audit lane.

## Audit fields

```yaml
audit_required_before_effective_retained: true
bare_retained_allowed: false
historic_intake: true
historic_claim_class: historic_status_note
intake_directive: owner_2026-08-05
cross_reference:
- "HISTORIC_PHASE1_REGISTRY_INTEGRITY_INTAKE_NOTE_2026-08-05.md"
```

Independent audit still required.
