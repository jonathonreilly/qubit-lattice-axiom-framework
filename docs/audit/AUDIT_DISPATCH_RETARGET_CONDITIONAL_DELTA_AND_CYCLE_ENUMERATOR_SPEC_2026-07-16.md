# Audit-Lane Dispatch Retarget, Conditional Delta Gate, and Single Cycle Enumerator — Design Spec

**Date:** 2026-07-16
**Type:** meta
**Status:** proposed design spec (spec-first; no implementation ships with this
note). Audit status authority is unchanged: verdicts are minted only by the
independent audit lane via
[`apply_audit.py`](scripts/apply_audit.py); nothing in this spec touches
verdict semantics, seat requirements, or the premise registry.
**Status authority:** independent audit lane only. This note sets no audit
verdict and promotes nothing.
**Owner-ratification points:** every behavioral cutover below (S1-C, S2-C,
S3-C) requires an explicit owner approval recorded in the Ratification Log
(section 6) before the corresponding flag is enabled. Shadow-mode emissions
(reports and additional generated files that affect no dispatch decision)
require review-loop landing only.

## 1. Problem statement (measured 2026-07-16)

Three measured defects in the audit-lane machinery, from the 2026-07-16 full
repo audit:

1. **Dispatch spends effort where publication does not need it.** The queue
   orders by criticality → readiness → cycle-break → load-bearing score
   ([`compute_audit_queue.py`](scripts/compute_audit_queue.py) header, lines
   9–13) and deliberately refuses flagship/publication importance as a signal
   (`flagship_signal_used: false` in
   [`compute_load_bearing.py`](scripts/compute_load_bearing.py) — a sound
   anti-gaming choice for *soundness* ordering). Consequence: the 571
   publication-cited non-retained rows (243 critical) drain in whatever order
   topology dictates, while ~2,300 uncited rows compete for the same audit
   capacity. At the observed net rate (~28 verdicts/day, bursty), the
   publication surface stays non-retained for months longer than necessary.
2. **Conditional churn.** ~39% of recent verdicts are `audited_conditional`
   (313 of 803 verdict commits since 2026-07-08) — non-terminal rows that
   re-enter the queue and are re-audited even when nothing they depend on has
   changed since the verdict.
3. **Cycle-count divergence.** The citation-cycle walk exists as three
   deliberately mirrored inline copies —
   [`compute_effective_status.py`](scripts/compute_effective_status.py)
   (lines ~197–257), [`build_cycle_inventory.py`](scripts/build_cycle_inventory.py)
   (whose docstring says it "intentionally mirrors the inline cycle
   detection"), and `audit_lint.py` — and the copies have drifted: the
   inventory reports 93 cycles while the effective-status summary reports 63.
   The front door, the queue's cycle-break targets, and the inventory
   therefore disagree about the same graph.

## 2. S1 — Publication-priority interleave lane

### S1-A Shadow artifact (this phase)

- [`render_publication_effective_status.py`](scripts/render_publication_effective_status.py)
  additionally emits a machine-readable
  `docs/audit/data/publication_gap.json`: one entry per distinct cited note
  whose `effective_status` is not retained-grade — `claim_id`, `criticality`,
  `effective_status`, `appearing_in` (the same row set the divergence report
  renders; today that is the 571). Generated, pipeline-owned, never shipped by
  PRs.
- [`compute_audit_queue.py`](scripts/compute_audit_queue.py) additionally
  emits `docs/audit/data/audit_publication_lane.json`: the intersection of
  the pending queue with `publication_gap.json` ∪ current cycle members,
  ordered by (readiness, load_bearing_score). **The existing
  `audit_queue.json` ordering is byte-unchanged in this phase.**
- Nightly shadow report (appended section in the front-door status snapshot):
  lane size, overlap with the top-N of the topological queue, and the
  hypothetical next-24h dispatch set under interleave vs actual.

### S1-B Semantics

- The lane is **target selection only**. It changes *which* pending rows are
  offered to auditors first; it changes no verdict rule, no dual-seat
  requirement, no criticality, and no readiness definition. Soundness
  ordering (criticality/readiness) remains the tie-breaker *within* the lane.
- Anti-gaming boundary preserved: `load_bearing_score` computation remains
  flagship-blind. Publication citation is used only to *filter* the pending
  set into the lane, never to raise a row's score, criticality, or grade.

### S1-C Cutover (owner-gated)

- Flag `publication_lane_interleave` (default off) in the batch orchestrator:
  when on, dispatch alternates 1:1 between `audit_publication_lane.json` and
  the topological queue, de-duplicated, lane-first on ties. Ratio is a
  constant in the orchestrator config, owner-changeable.
- Cutover evidence required: ≥5 nightly shadow reports; owner inspects lane
  composition and starvation metrics (does any critical topological row wait
  >N days under simulated interleave).

## 3. S2 — Conditional dependency-delta gate

### S2-A Mechanism

Verdict-time shards already record the inputs this gate needs:
`audit_state_snapshot.dep_effective_status` (plus `deps`, `runner_hash`,
`dep_claim_scope`) is captured when a verdict is applied. A terminal-non-clean
row (`audited_conditional` / `audited_renaming` / `audited_numerical_match`)
is **delta-live** iff at least one of:

1. its own `note_hash` or paired `runner_hash` drifted;
2. any recorded dependency's current `effective_status` differs from the
   snapshot's `dep_effective_status` value (or its `deps` set changed);
3. a dispatcher sidecar names it (existing re-audit targeting mechanism);
4. its snapshot lacks `dep_effective_status` entirely (legacy verdicts:
   fail-open — such a row stays dispatchable, and its next verdict stamps a
   complete snapshot, after which the gate applies).

Rows that are not delta-live are **parked**: they remain in the ledger and in
a new visible queue bucket `conditional_parked` (with the blocking dependency
list rendered), but are not offered for dispatch. Parking is recomputed every
pipeline run from current statuses — a dependency status change un-parks
automatically. Nothing is dropped or hidden: the queue markdown renders the
parked bucket with counts and per-row blocking reasons.

### S2-B Shadow artifact (this phase)

`compute_audit_queue.py` computes delta-liveness and emits it as a *report
field only* (`would_park: true/false` per conditional row + a summary count in
the front-door snapshot). Dispatch is unchanged.

### S2-C Cutover (owner-gated)

Flag `conditional_delta_gate` (default off): when on, parked rows are excluded
from dispatch offers. Cutover evidence: ≥5 nightly shadow reports; owner
inspects the would-park list (expected to absorb most of the 39% churn) and
spot-checks ≥3 parked rows for a wrongly-parked case (a row whose blocking
condition changed through a channel the snapshot does not see — if any such
channel is found, it must be added to the delta definition before cutover).

## 4. S3 — Single cycle enumerator

### S3-A Change

- Extract the DFS color walk into one shared module
  `docs/audit/scripts/cycle_walk.py` (the exact walk currently inlined in
  `compute_effective_status.py`, with deterministic node ordering).
- `compute_effective_status.py`, `build_cycle_inventory.py`, and
  `audit_lint.py` import it; their inline copies are deleted.
- The pipeline gains an invariant: `cycles_detected`
  (effective-status summary) must equal `cycle_count` (inventory); mismatch
  fails the run loudly. The 93-vs-63 discrepancy is resolved by construction,
  and whichever count the unified walk yields becomes the single reported
  number everywhere (front door, queue, inventory).
- The inventory additionally reports strongly-connected-component membership
  stats (component sizes, per-component cycle counts) to support targeted
  lemma-extraction on the dominant theta/koide/strong-CP component — the
  audit found one component drags up to 759 transitive descendants through a
  single length-2 citation pair.

### S3-B Risk and cutover

Unifying the walk *changes reported cycle counts and cycle-break target
lists* (that is the point). This is a generated-surface change with no
verdict semantics; it lands like any tooling repair (review-loop, pipeline
validation), with one nightly side-by-side report (old counts vs unified
count) before the old code paths are deleted. Deletion is the S3-C cutover
and is owner-gated only in the weak sense that the side-by-side report must
be in the nightly log for owner inspection; no policy constant changes.

## 5. Explicitly out of scope (named follow-ups)

- **Dual-family audit seating** (second seat on critical/high cleans from a
  different model family; judicial third-pass staffing): this is a *policy*
  change to seat requirements — the deepest trust-boundary change on the
  roadmap — and will be drafted as its own owner-approval document. Nothing
  in S1–S3 alters seat rules.
- Any change to `load_bearing_score`, criticality assignment, premise
  registry, N1–N8 packet requirements, or verdict vocabulary.
- Publication-table content: S1 consumes the gap; it does not edit tables.

## 6. Ratification Log

Owner approvals for S1-C, S2-C, and S3-C cutovers are recorded here by dated
edit, mirroring the practice of
[`AXIOM_MINIMALITY_POLICY.md`](AXIOM_MINIMALITY_POLICY.md) section 6.

- (none yet — spec proposed 2026-07-16; shadow-mode implementation may land
  after this spec passes review-loop; no cutover flag may be enabled before
  its entry appears here.)
