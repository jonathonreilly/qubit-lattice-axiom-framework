# Historic intake: axiom-reconciliation - resume notes (2026-07-12)

Date: 2026-08-05
Authority: none
Audit: unset
Claim type: historic_status_note
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

Original verdict: Deliverables are committed TSVs under logs/runner-cache/recon_triage/; supervisor line-reviews every worker row before any edit lands.
Scope: Files whose load-bearing quotes or citations reference deleted or changed axiom content.


## Why pulled (supervisor decision, on the record)

Work order already surfaced to the owner: the axiom-reconciliation rescan index at TOTAL HARD=141 / SOFT_ONLY=740 / RETAINED_STATUS_HARD=8 (base 7b9260b85) - eight files with retained audit status hard-reference deleted or changed axiom text. The invalidation-pipeline gap; deliverable TSVs pinned under logs/runner-cache/recon_triage/.

## Provenance (pinned)

- Original path: `.claude/science/physics-loops/axiom-reconciliation/RESUME.md`
- Source commit: `2be2924f52bc045174d08df2841d100e300ecd0e`
- git blob: `1a605e1e1a9ff7c64bc4c98941120fbe6e3936b9`
- sha256: `485256eec2662d49ad5dce05840f0d2b2b9b827867355833edf21e086a57ec44`
- Lines: 40; runners named: scripts/axiom_reconciliation_rescan_2026_07_12.py

## Attached evidence (registered with, not as, this claim)

- none

## Cross-stratum flags

- Cross-stratum reference from packsci03 idx 10833 (`.claude/science/physics-loops/repo-state-scrub-20260725/phase1_registry_integrity.md`, decision PULL) — SYSTEMIC INTEGRITY MEASUREMENT: ALL THREE registered derivation obligations have machine records that MISMATCH their source notes (6 distinct mismatches); of 4 registered axiom/primitive surfaces ...; documents the mass invalidation event that destroyed 202 clean no-go audits; the no_go count's cause is STRUCTURAL (the route exists in code and was never wired). Recommended repair set R1+R3+R4+R5 costed in-pack. Companion to the recon-rescan gap pulled from packsci01.

## Flags carried

141 files carry hard references to deleted or changed axiom content, and 8 of them hold retained audit status - i.e. retained claims resting on axiom text that no longer exists, and the invalidation pipeline did not catch it.

## Audit fields

```yaml
audit_required_before_effective_retained: true
bare_retained_allowed: false
historic_intake: true
intake_directive: owner_2026-08-05
```

Independent audit still required.
