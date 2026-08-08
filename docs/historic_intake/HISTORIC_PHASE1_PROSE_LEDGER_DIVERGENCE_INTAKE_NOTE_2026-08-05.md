# Historic intake: Phase 1 — Prose/ledger status divergence: measurement, severity, churn cost

Date: 2026-08-05
Authority: none
Audit: unset
Claim type: historic_measurement
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

Original verdict: Divergence is real, large and load-bearing (89% of the 478 lines sit on true dependency edges) but it is a SYMPTOM whose proximate cause is the pipeline gap: audit_lint.py reads note bodies and never checks them for status claims, vocab_lint.py has no status vocabulary at all, and the prose_status field is inert (2876/3872 not_evaluated_pre_vocab_lint, 996 clean, and ZERO rows carry a single prose_corrections entry — the auto-correct-and-log mechanism in VOCABULARY_HYGIENE_DESIGN.md principle 4 has NEVER FIRED).
Scope: Status truth read only from tracked shards docs/audit/data/ledger/<id[:2]>/<id>.json; no prose status label trusted anywhere.
Escape conditions (negative claims): The churn guard does NOT bind this defect class — total cost is 4 requeued rows (0.5% of audited capital) and 0 retained verdicts — so the reason to prefer tooling is recurrence, not cost.

## Why pulled (supervisor decision, on the record)

SYSTEMIC INTEGRITY MEASUREMENT: of 3872 tracked ledger rows, 3100 (80.1%) are unaudited and 772 are audit capital; 478 status-attribution defect lines measured (a note labels a status the ledger does not back), 89% sitting on true dependency paths; the specified auto-correct-and-log mechanism has never run; the churn guard does NOT bind this defect class. Companion to the prose-vs-ledger drift finding pulled from packsci02.

## Provenance (pinned)

- Original path: `.claude/science/physics-loops/repo-state-scrub-20260725/phase1_prose_ledger_divergence.md`
- Source commit: `7d1b60b2f9648ee299fa050079afba04638cdcd3`
- git blob: `152c9a3374395617b51c990bdf67f3b0b0e58e2f`
- sha256: `ca4dacbb7501756dbfc6241625f73c16dcb6e8e6904a832797cc73db3b2dd8fd`
- Lines: 568; runners named: scripts/invalidate_stale_audits.py, scripts/seed_audit_ledger.py

## Attached evidence (registered with, not as, this claim)

- none

## Cross-stratum flags

- Attaches across strata to idx 10563 (`.claude/science/physics-loops/koide-mode-content-campaign-20260724/wave2_primitive_check.md`, stratum packsci02) — SYSTEMIC INTEGRITY MEASUREMENT: of 3872 tracked ledger rows, 3100 (80.1%) are unaudited and 772 are audit capital; 478 status-attribution defect lines measured (a note labels a status the ledger does not back), 89% sitting on true dependency paths; the specified auto-correct-and-log mechanism has never run; the churn guard does NOT bind this defect class. Companion to the prose-vs-ledger drift finding pulled from packsci02.

## Flags carried

a specified auto-correct-and-log mechanism has never fired once in the repo's history; and there is NO FIELD anywhere meaning 'this note's prose asserts a status contradicting the ledger'

## Audit fields

```yaml
audit_required_before_effective_retained: true
bare_retained_allowed: false
historic_intake: true
intake_directive: owner_2026-08-05
```

Independent audit still required.
