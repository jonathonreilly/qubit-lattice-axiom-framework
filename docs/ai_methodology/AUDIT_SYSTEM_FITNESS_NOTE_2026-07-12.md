# Audit System Fitness Note — 2026-07-12

**Type:** meta

This owner-requested process review carries no science claim, audit verdict,
registry action, or policy authority. It assesses the audit and review system
against the eight elapsed days from 2026-07-04 through 2026-07-12.

## The question

Is the assurance system fit for purpose, where the purpose is: fast-moving
collaborative science (approximately 96 PRs merged over that eight-day
interval; axioms still occasionally change) whose claims must be right, with
the option of whole-lane certification at any commit?

## Quantitative state (2026-07-12)

All counts, rates, durations, and incident summaries below are repository or
operator snapshots as of 2026-07-12 unless stated otherwise.

- [Generated audit ledger](../audit/AUDIT_LEDGER.md): 3,737 rows; 380 with a
  retained-grade derived effective status (10.2%); 2,947 with pipeline-derived
  `effective_status: unaudited` (78.9%) after the cross-family regime reset and
  the 2026-07-12 packet-invalidation incident.
- Landing velocity: approximately 12 PRs/day from the 96-PR/eight-day
  snapshot. Peak audit throughput was approximately 16 rows/day by operator
  estimate, with heavy manual orchestration.
- Flagship-lane picture (rolling certification, first run): charged-lepton
  chain 31 blocking of 41; AC retirement basis 2 of 3; rule-universality
  grain 17 of 21; theta 1 of 1. These are 51 lane-blocker entries representing
  45 distinct rows because the lane closures overlap.

## What demonstrably caught real defects (evidence, this window)

1. **Hostile review-loop passes** before landing: the window's review records
   report a counterexample to a candidate sector-orbit partition statement,
   corrections to eraser-control and repeat-action statements, a narrowed
   candidate quotation, and nine findings on one PR.
2. **Independent cross-family re-derivation audits**: the operator record
   reports a false displayed Pauli-product formula and two hard-coded runner
   booleans in a foundational note that had previously passed twice.
3. **Owner review**: the operator record reports rejection of a
   "non-addition implies exclusion" inference.
4. **Content-hash invalidation** (premise-hash resets) after axiom edits.

## What caught nothing real while consuming the budget

The 2026-07-12 operator record reports no scientific finding from full-universe
N6/N8 candidate dispositions (68 to 1,711 candidates per row),
manifest-containment scans on theorem rows, repeated packet re-authoring
against live-rebuilt indexes, or the snapshot set-identity invalidation sweep.
That sweep invalidated 230 verdicts, including doubly confirmed cleans, within
hours; the operator record reports none restorable under the successor
snapshot schema.

The owner-approved decision is the
[two-tier assurance and rolling-certification design](../audit/README.md#two-tier-assurance-and-rolling-certification-2026-07-12-owner-approved):
forensic plumbing at no-go rows and pinned-commit certification runs,
content-bound structural assurance elsewhere, and rolling lane certification
instead of scheduled freezes. This note does not extend that policy.

## Findings and dispositions

**Throughput constraint (critical).** At the operator-estimated peak of 16
rows/day, the 2,947-row backlog represents roughly 184 audit days even if no
new rows arrive; uniform draining also does not prioritize lane certification.
Proposed disposition: use the existing lane `blocking` lists for lane-first
targeting and consider a first-class batch audit orchestrator with parallel
restricted-packet workers, pinned manifests, serialized application, and a
lane argument. The four current closures contain 51 blocking entries across
45 distinct rows. Operator size estimate: 1–2 infrastructure days.

**Lane-canary gap (high).** The 2026-07-12 hardening incident had green unit
tests but produced unattainable packets and invalidated 230 verdicts. Proposed
disposition, pending owner ratification in canonical guidance: add an
audit-lane-owned canary that exercises packet build, auditor-format checking,
application to a disposable fixture, pipeline regeneration, and invalidator
survival. Review-loop would verify recorded canary evidence; it would not run
the audit worker, apply a verdict, or treat this note as policy.

**Snapshot-schema succession (medium).** The incident shows that a schema
change without an explicit prior-era disposition can orphan verdict evidence.
Proposed disposition, pending owner ratification in canonical guidance: require
schema-change proposals to choose and test one disposition—migration,
grandfathering until content changes, or scheduled re-audit. This note does not
establish that requirement.

**Orchestration sharp edges (medium).** The operator record attributes worker
loss to launching and waiting inside one timed shell call; it also records
placeholder-file false positives, specification parentheticals copied into
notes, and two-hour transport-envelope expiry. Proposed disposition: capture
the reproduced failure modes in canonical audit-loop or workhorse guidance.
No operating rule is created here.

**Auditor-family concentration (medium).** Current passes use one auditor model
family; `cross_family` measures auditor-versus-author diversity, not diversity
within the auditor pool. Proposed disposition, pending owner ratification:
evaluate a family-diversity preference when another strong family is available
and use `auditor_reliability.json` as the tracking surface. Owner spot reviews
are additional evidence when they occur, not a required gate established here.

**Velocity instrumentation (low).** The snapshot has no coverage-trend or
time-to-terminal series. Proposed disposition: evaluate an append-only
`lane_certification_history.jsonl` emitted by the certification step with lane,
certified state, blocking count, head SHA, and timestamp. No implementation or
landing status is asserted here.

**Stacked and infrastructure review briefs (low).** Reviews in this window
needed hand-written stack-awareness and infrastructure checklists. Proposed
disposition: evaluate native review-loop guidance for both cases. This note
does not change the skill.

## Bottom line

The system is fit for purpose under the owner-approved two-tier calibration,
with throughput as the current operational risk: 45 distinct rows block the
four measured flagship closures at this snapshot. The canonical design
concentrates assurance on hostile review at landing, independent re-derivation
at audit, and forensic packets for permanent-foreclosure rows and
certification commits. This assessment does not predict completion or landing
of any follow-up.

## Proposed follow-ups (sized)

1. `orchestrate_audit_batch.py` — parallel fleet + serialized apply, lane
   argument (operator estimate: 1–2 days).
2. Canonical review-loop and audit-infrastructure guidance: canary evidence,
   schema-succession disposition, and stacked-change protocol (doc-only,
   small).
3. `lane_certification_history.jsonl` append in
   `compute_lane_certification.py` (operator estimate: tiny).
4. Family-diversity preference knob for flagship terminal cleans (small,
   contingent on a second strong family becoming available).
