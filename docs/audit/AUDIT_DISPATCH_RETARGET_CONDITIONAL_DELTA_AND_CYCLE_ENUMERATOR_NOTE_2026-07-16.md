# Audit-Lane Dispatch Retarget, Conditional Blocker-Delta Consolidation, and Cycle-Domain Unification — Design Note

**Date:** 2026-07-16
**Type:** meta
**Status:** proposed design note (spec-first; no implementation ships with this
note). Registered in
[`doc_authority_registry.json`](data/doc_authority_registry.json) as a Class D
proposal (`in_flight_pr`); it carries no process authority until an
owner-ratified transition, and no physics-premise weight in any class.
**Status authority:** independent audit lane only. This note sets no audit
verdict and promotes nothing. Verdict semantics, seat requirements,
criticality assignment, load-bearing scoring, and the premise registry are
untouched by every design below.
**Owner-ratification points:** each behavioral cutover (the
`publication_lane_interleave` flag, the `conditional_delta_gate` flag, and the
cycle-walk authority switch) requires an owner entry in the Ratification Log
(final section) before it is enabled. Shadow-mode emissions (reports and
additional generated files that affect no dispatch decision) require
review-loop landing only.

## 1. Measured problems (all figures measured 2026-07-16; not standing invariants)

1. **Dispatch order is publication-blind by design, and the publication gap
   is large.** The pending queue sorts by criticality → readiness →
   transitive-descendant reach → load-bearing score
   ([`compute_audit_queue.py`](scripts/compute_audit_queue.py) header lines
   8–13 and the sort at lines ~201–208); cycle-break targets are a separate
   generated side list, not a sort key. Load-bearing scoring deliberately
   refuses flagship/publication signals
   (`flagship_signal_used: false`,
   [`compute_load_bearing.py`](scripts/compute_load_bearing.py)) — a sound
   anti-gaming choice. Measured consequence: the publication tables cite 571
   non-retained-grade rows (260 critical, of which 243 are unaudited); 561 of
   the 571 sit in the pending queue at positions 4 through 1,573, competing
   with ~2,420 uncited pending rows. No throughput rate or time-to-clear
   figure is asserted here: the ledger's 476 applied-status rows are a
   surviving stock, not a post-reset flow (only 93 carry an audit date on or
   after 2026-06-29), and queue positions are selection-order facts, not
   duration estimates. Timing projections are exactly what the shadow
   simulation below exists to produce, under explicit selection and
   readiness assumptions.
2. **Conditional re-queue churn is real, and partially guarded already.**
   38.98% of verdict commits since 2026-07-08 are `audited_conditional`
   (313 of 803, by commit-subject count). These rows re-enter the pending
   queue by the recorded owner rule of 2026-06-15
   ([`compute_audit_queue.py`](scripts/compute_audit_queue.py) lines ~82–92:
   `audited_conditional` and non-archived `audited_failed` stay pending until
   driven terminal). At the dispatch boundary, main ALREADY carries a
   repetition guard: `awaiting_repair_since_conditional()` in
   [`orchestrate_audit_batch.py`](scripts/orchestrate_audit_batch.py)
   (lines ~173–247) suppresses re-audit of an archived conditional whose
   note/runner sources, dependency effective statuses, dependency
   claim type/scope, and axiom-premise note hashes have not moved, honors
   explicit invalidation reasons as a stronger re-audit signal, time-fences
   source changes against the verdict date, and provides a
   `--retarget-conditionals` escape hatch. This note does NOT claim unchanged
   conditionals are re-dispatched wholesale today, and does not claim the
   38.98% is mostly redundant; quantifying actual duplicate unchanged
   dispatches since that guard landed is a shadow-phase deliverable.
3. **Cycle counts diverge by node domain, not by code drift.** The DFS
   back-edge walk exists in three intentionally mirrored copies
   ([`compute_effective_status.py`](scripts/compute_effective_status.py),
   [`build_cycle_inventory.py`](scripts/build_cycle_inventory.py),
   `audit_lint.py`), and the mirrored implementations agree: the SAME walk
   yields 93 cycles on the full citation graph (~3,950 nodes) and 63 on the
   gated ledger-row domain (~3,755 rows). The stored 93
   (`cycle_inventory.json`) vs 63 (`effective_status_summary.json`)
   discrepancy is input-domain selection. The reported objects are DFS
   back-edge archaeology, not a canonical enumeration of all simple cycles,
   and that disclosure must survive any refactor.

## 2. Publication-priority interleave lane

### 2a. Shadow artifacts (this phase; no dispatch change)

- [`render_publication_effective_status.py`](scripts/render_publication_effective_status.py)
  additionally emits a machine-readable
  `docs/audit/data/publication_gap.json`: one entry per distinct cited note
  whose `effective_status` is not retained-grade — `claim_id` (nullable),
  `criticality` (nullable), `effective_status`, `appearing_in`, and a raw
  `cited_path`. The five currently-unresolved cited paths (rows with no
  ordinary ledger identity) are carried with `claim_id: null` and an
  `unresolved: true` flag rather than dropped. Generated, pipeline-owned,
  never shipped by PRs.
- [`compute_audit_queue.py`](scripts/compute_audit_queue.py) additionally
  emits `docs/audit/data/audit_publication_lane.json` (a derived, generated
  file): the intersection of the pending queue with `publication_gap.json`
  ∪ the canonical primary cycle-break-target side list (NOT all cycle
  members — using every cycle member would silently broaden the existing
  one-target-per-cycle policy), each entry validated against the tracked
  manifest below, ordered by the FULL main-queue key (criticality rank,
  readiness, transitive-descendant reach, load-bearing score). **The
  existing `audit_queue.json` ordering is byte-unchanged in this phase.**
- Nightly shadow report (a section appended to the front-door status
  snapshot): lane size; overlap with the topological queue's top segment;
  the hypothetical next-24h dispatch set under interleave vs actual;
  **lane-membership additions and removals since the previous night, named
  per row**; and priority-displacement metrics (which topological rows a
  simulated interleave would defer, and for how long).

### 2b. Semantics and the gaming surface, stated honestly

- The lane is target selection only: no verdict rule, seat requirement,
  criticality, readiness definition, or score changes. `load_bearing_score`
  remains flagship-blind.
- Publication-table membership DOES become a dispatch-priority signal under
  the interleave — filtering is prioritization. The mitigation is
  governance, not denial: lane eligibility binds to a **tracked, reviewed
  manifest sidecar** `docs/audit/data/publication_lane_manifest.json`
  (schema: `frozen_commit`; `admitted` claim ids; `pending` adds/removals
  each with its first-shadow-report date; `activation_report` reference).
  The manifest is a controlled data file in the same review-landable class
  as dispatcher sidecars — NOT a derived queue cache, so membership,
  objection windows, and activation state survive fresh clones and nightly
  regeneration. The generated lane file is derived from and validated
  against it. Membership changes reach the manifest only through
  review-loop-landed edits, appear as named adds/removals in the nightly
  shadow report, and a newly added row becomes lane-eligible only after
  appearing in at least one report with no reviewer/owner objection — an
  explicit, visible surface against citing one's own note into priority.
  Cycle-derived entries (from the primary break-target side list) enter
  through the same manifest and the same delay.

### 2c. Cutover (owner-gated)

- Flag `publication_lane_interleave` (default off): when on, dispatch
  interleaves lane and topological rows ONLY within equal
  (criticality rank, readiness) bands — publication membership can reorder
  rows inside a band but can never lift a row above a higher criticality
  band or above a ready row from a blocked one. Inside a band, both streams
  retain transitive-descendant reach → load-bearing score as sub-keys;
  lane-first on exact ties; blocked (`ready: false`) rows are excluded from
  both streams before the merge. The interleave ratio within bands is an
  owner-changeable config constant.
- Cutover evidence: ≥5 nightly shadow reports; owner inspects lane
  composition, membership churn, displacement, and starvation (any critical
  topological row deferred beyond a stated bound under simulation).

## 3. Conditional blocker-delta consolidation

### 3a. What exists and what is missing

The dispatcher guard above already covers: own note-hash drift, dependency
effective-status/claim-type/claim-scope drift, axiom-premise note-hash drift,
explicit invalidation reasons, and a source-vs-verdict time fence. Missing or
scattered today:

- **Queue-level visibility:** the pending queue does not distinguish a
  conditional row the guard would skip from one it would dispatch; effort
  planning sees them identically.
- **Channels not yet compared:** helper-runner paths/hashes
  (`helper_runner_hashes` is snapshotted by
  [`apply_audit.py`](scripts/apply_audit.py) but not compared); runner-cache
  / artifact / classifier state (the active review queue records that cache
  freshness keys only on runner-source SHA); packet/prompt/gate policy
  versions; premise-registry epoch.
- **No versioned snapshot schema:** legacy snapshots with a present-but-
  incomplete field set are indistinguishable from complete ones. Measured
  on the owner-ruled eligible set — 54 rows: 46 `audited_conditional` plus
  8 non-archived `audited_failed` — all carry `dep_effective_status`, but 3
  lack dependency type/scope/axiom baselines, and of the 13 with current
  helper runners, 12 lack `helper_runner_hashes`.
- **Targeting-stream union:** policy-driven targeting outputs (e.g.
  `no_go_index_growth_targets.json`) are not consumed by the ordinary
  dispatcher sidecar path.

### 3b. Proposal — one versioned blocker-environment fingerprint

- Define `blocker_fingerprint_v1`: the complete, versioned set of compared
  channels (everything the guard compares today + helper-runner
  paths/hashes + runner-cache/artifact/classifier state + policy/gate/prompt
  versions + premise-registry epoch). One shared routine computes
  delta-liveness from a shard's snapshot + the current pipeline state and
  returns the changed-channel list.
- The orchestrator guard and the queue both call it: the queue renders a
  visible parked-awaiting-blocker-change bucket (rows in the owner-ruled
  pending set — `audited_conditional` and non-archived `audited_failed` —
  whose fingerprint shows no movement), with per-row blocking-channel lists;
  parking recomputes every pipeline run and un-parks automatically on any
  channel change. Nothing is hidden or dropped.
- **Version-by-version validation matrix (one unambiguous rule per case):**
  (i) snapshot absent or carrying no schema-version marker (all legacy
  rows) → dispatch-open with a visible migration counter and reason; its
  next verdict stamps a complete v1 snapshot. (ii) snapshot marked v1 but
  incomplete or structurally invalid → loud pipeline failure (a v1 writer
  that omits a required baseline is a bug, never a silent fail-open).
  Fail-open for the legacy branch is correct: the cost is bounded duplicate
  review effort, while fail-closed parking on an invisible channel would
  silently strand a stale authority. The matrix is regression-tested per
  version and per missing-field case.
- **Snapshot projection, defined:** the fingerprint always reads the LATEST
  APPLICABLE ARCHIVED verdict snapshot (`previous_audits[-1]`, matching the
  existing guard's projection), never a live mid-edit snapshot.
- All canonical targeting streams (dispatcher sidecars, invalidation
  reasons, no-go index-growth targets, `--retarget-conditionals`) union into
  dispatch-liveness ahead of the fingerprint; the fingerprint can only park,
  never veto an explicit targeting signal.
- **This is a dispatch-policy amendment**, not neutral machinery: it narrows
  when the owner-ruled pending set is offered for dispatch. It therefore
  requires its own Ratification Log entry (below) referencing the 2026-06-15
  owner rule it amends. `audited_renaming` and `audited_numerical_match` are
  outside this design: the ordinary pending queue does not dispatch them
  today, and making them dispatch-eligible would be a separate ratified
  change.

### 3c. Shadow phase and cutover (owner-gated)

- Shadow: the queue emits per-row would-park reporting plus the summary
  count; dispatch unchanged. Deliverables before any cutover: (i) measured
  duplicate-unchanged-dispatch counts since the existing guard landed;
  (ii) channel-mutation tests — for EVERY fingerprint channel, a test that
  mutates only that channel and shows the row un-parks; (iii) ≥5 nightly
  reports with owner spot-checks of ≥3 parked rows for wrongly-parked cases.
  A wrongly-parked row found through any channel not in v1 blocks cutover
  until that channel is added and versioned.
- Flag `conditional_delta_gate` (default off): when on, parked rows are not
  offered for dispatch (explicit targeting signals still override).
- **Consumer coverage (both flags):** dispatch selection has more than one
  consumer today — the documented top-of-queue driver
  `scripts/codex_audit_runner.py` (loads and slices `audit_queue.json`,
  ready-only by default, skips live conditional/failed rows outside an
  explicit re-audit role) and the batch orchestrator
  [`orchestrate_audit_batch.py`](scripts/orchestrate_audit_batch.py)
  (explicit lane/claim lists; sorted-set iteration; invokes the existing
  conditional guard on its own path). A cutover that flips only one consumer
  is not a cutover. Implementation must either centralize top-of-queue
  selection and audit-role classification in one shared routine both
  consumers call, or update every named consumer, with end-to-end tests
  through BOTH command paths covering explicit-target override, readiness
  precedence, and the fingerprint. Fingerprint-open nonterminal rows must be
  routed through a real re-audit dispatch role (so the promised
  v1-stamping "next verdict" can actually occur), not left in a role no
  consumer dispatches.

## 4. Cycle-domain unification

### 4a. Change

- Extract the DFS color walk into one shared module
  `docs/audit/scripts/cycle_walk.py` with deterministic node ordering, plus a
  canonical adjacency constructor for each of the two legitimate domains:
  the full citation graph (inventory/lint archaeology) and the gated
  ledger-row domain (effective-status accounting).
- Every consumer imports the shared walk AND labels its number with its
  domain. Generated surfaces (front door, inventory, queue cycle-break side
  list, effective-status summary) each state their domain explicitly; the
  front door reports both labeled counts. The pipeline gains the invariant:
  same-domain results agree across all consumers by NORMALIZED CYCLE
  SIGNATURE (sorted canonical node lists), not by count alone (mismatch
  fails the run).
  The DFS-archaeology disclosure (not a canonical simple-cycle enumeration)
  is carried on every surface that reports a count.
- The inventory additionally reports strongly-connected-component membership
  stats (component sizes, per-component cycle counts). Measured 2026-07-16
  for orientation, with topology-metric wording only: the dominant
  theta/koide/strong-CP family sits in a 127-node SCC; a separate two-node
  quark-CP-carrier pair's nodes carry a maximum transitive-descendant score
  of 759 (a reach metric; no claim that the pair causally creates that
  reach).

### 4b. Phasing (fixes the ordering, keeps legacy authoritative until switch)

1. **Shadow:** `cycle_walk.py` lands alongside the legacy inline copies;
   legacy callers remain authoritative; a nightly side-by-side section
   reports legacy vs shared-walk counts per domain.
2. **Switch (owner-logged):** after ≥3 clean side-by-side nights, an
   owner-approved Ratification Log entry names the exact switch (config
   value or commit) that makes the shared walk authoritative. Cycle-break
   target lists may change at this point — that is a dispatch-surface
   change and is why the switch is owner-logged.
3. **Rollback soak, then deletion + invariant:** the legacy copies remain
   in place (unused but restorable by reverting the switch) for a stated
   soak window after the switch; only after a clean soak are the inline
   copies deleted and the same-domain signature invariant enforced in the
   pipeline.

## 5. Explicitly out of scope (named follow-ups)

- **Dual-family audit seating** (second seat on critical/high cleans from a
  different model family; judicial third-pass staffing): a policy change to
  seat requirements — the deepest trust-boundary item on the roadmap — to be
  drafted as its own owner-approval document. Nothing here alters seat
  rules.
- Any change to `load_bearing_score`, criticality assignment, premise
  registry, N1–N8 packet requirements, or verdict vocabulary.
- Publication-table content: the lane consumes the gap; it does not edit
  tables.
- Dispatch eligibility for `audited_renaming` / `audited_numerical_match`.

## 6. Ratification Log

Owner approvals are recorded here by dated edit. Entry schema (every field
required): `date`; `switch` (exact flag/config/commit identifier and value,
including any ratio or threshold); `evidence` (artifact paths and the commit
hash they were produced at); `approval_source`; `decision`; and
`rollback_condition`. This log records decisions; it is a historical record
in the manner of the axiom-policy approval log and carries no premise or
interpretive weight of its own. At implementation time, every enabled flag
or config value must bind mechanically to an owner-ratified entry on an
authoritative config surface (Class E per the document-authority policy);
this Class D note's log is the decision record, never the machine authority.
Implementation must also verify the generic Class D fence: a Class D
proposal note must not chain-satisfy any citation-graph dependency edge.

- (none yet — note proposed 2026-07-16; shadow-mode implementation may land
  after this note passes review-loop; no cutover switch may be flipped
  before its entry appears here.)
