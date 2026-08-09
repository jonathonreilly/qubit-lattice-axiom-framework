# Historic intake: Phase 1 — Prose/ledger status divergence: measurement, severity, churn cost

Date: 2026-08-05
Authority: none
Audit: unset
Claim type: bounded_theorem
Stratum: pack_science_family
Era: post_reset_2026_06_29

Status: HISTORIC INTAKE under the 2026-08-05 owner directive (pull historic
science iff relevant and/or valuable; pulled items enter the ledger and are
audited). This wrapper registers a claim from the repo's unledgered history.
The wrapper asserts nothing beyond what the pinned original states; the
original's own scope, caveats and era conventions govern. Independent audit
required before any effective status.

## The claim (as stated by the original, supervisor-compressed)

Of 3872 tracked ledger rows, 3100 (80.1%) are unaudited and 772 (19.9%) are audit capital. Measured 478 status-attribution defect lines (a note labels a NAMED OTHER note with a status stronger than that note's live status) across 176 distinct citing notes and 203 distinct mislabelled targets, plus 26 self-over-claim notes. Mutually circular pairs: ZERO. Rows requeued if EVERY defect is fixed: 4. Retained-grade verdicts put at risk: 0.

## Why pulled (supervisor triage decision of 2026-08-05, provenance not authority)

The reasons below are the supervisor's selection rationale; they carry no claim status and are not evidence about the original's validity.

SYSTEMIC INTEGRITY MEASUREMENT: of 3872 tracked ledger rows, 3100 (80.1%) are unaudited and 772 are audit capital; 478 status-attribution defect lines measured (a note labels a status the ledger does not back), 89% sitting on true dependency paths; the specified auto-correct-and-log mechanism has never run; the churn guard does NOT bind this defect class. Companion to the prose-vs-ledger drift finding pulled from packsci02.

## Provenance (pinned)

- Original path: `.claude/science/physics-loops/repo-state-scrub-20260725/phase1_prose_ledger_divergence.md`
- Source commit: `7d1b60b2f9648ee299fa050079afba04638cdcd3`
- git blob: `152c9a3374395617b51c990bdf67f3b0b0e58e2f`
- sha256: `ca4dacbb7501756dbfc6241625f73c16dcb6e8e6904a832797cc73db3b2dd8fd`
- Archived original (byte-exact, sha256-verified at generation): [../../archive_unlanded/historic_intake_originals/packsci03/10832_phase1_prose_ledger_divergence.md](../../archive_unlanded/historic_intake_originals/packsci03/10832_phase1_prose_ledger_divergence.md)
- Lines: 568; runners named: historic runner (unpinned, not in this packet): `scripts/invalidate_stale_audits​.py`; historic runner (unpinned, not in this packet): `scripts/seed_audit_ledger​.py`
- Note: `.py` tokens in this wrapper's rendered fields are display-neutralized with a zero-width split for citation-graph hygiene (no current-tree runner may bind); the byte-exact original wording is pinned in the triage decisions/extraction JSONL files and in the archived original.

## Attached evidence (registered with, not as, this claim)

- none

## Cross-stratum flags (inert text; machine-readable relations in the audit fields)

- Attaches across strata to idx 10563 (`.claude/science/physics-loops/koide-mode-content-campaign-20260724/wave2_primitive_check.md`, stratum packsci02) — SYSTEMIC INTEGRITY MEASUREMENT: of 3872 tracked ledger rows, 3100 (80.1%) are unaudited and 772 are audit capital; 478 status-attribution defect lines measured (a note labels a status the ledger does not back), 89% sitting on true dependency paths; the specified auto-correct-and-log mechanism has never run; the churn guard does NOT bind this defect class. Companion to the prose-vs-ledger drift finding pulled from packsci02.

## Triage extraction notes (2026-08-05/08, not from the original)

Written at triage/extraction time; NOT part of the pinned original, carries no authority, and is input for the future auditor only.

- Extraction verdict (triage compression; may reflect later context): Divergence is real, large and load-bearing (89% of the 478 lines sit on true dependency edges) but it is a SYMPTOM whose proximate cause is the pipeline gap: audit_lint​.py reads note bodies and never checks them for status claims, vocab_lint​.py has no status vocabulary at all, and the prose_status field is inert (2876/3872 not_evaluated_pre_vocab_lint, 996 clean, and ZERO rows carry a single prose_corrections entry — the auto-correct-and-log mechanism in VOCABULARY_HYGIENE_DESIGN.md principle 4 has NEVER FIRED).
- Extraction scope (triage compression; may reflect later context): Status truth read only from tracked shards docs/audit/data/ledger/<id[:2]>/<id>.json; no prose status label trusted anywhere.
- Extraction escape conditions (negative claims; triage compression): The churn guard does NOT bind this defect class — total cost is 4 requeued rows (0.5% of audited capital) and 0 retained verdicts — so the reason to prefer tooling is recurrence, not cost.
- Extraction red flags: a specified auto-correct-and-log mechanism has never fired once in the repo's history; and there is NO FIELD anywhere meaning 'this note's prose asserts a status contradicting the ledger'
- Supersession (as known at extraction): Corrects the campaign brief's own framing: the campaign cited '44 mutually circular contradictions' but measured circular pairs are ZERO. Notes that prose_status is scoped to vocabulary drift by docs/audit/README.md:108-124 and explicitly does not propagate into effective_status.

## Audit fields

```yaml
audit_required_before_effective_retained: true
bare_retained_allowed: false
historic_intake: true
historic_claim_class: historic_measurement
intake_directive: owner_2026-08-05
cross_reference:
- "HISTORIC_WAVE2_PRIMITIVE_CHECK_INTAKE_NOTE_2026-08-05.md"
```

Independent audit still required.
