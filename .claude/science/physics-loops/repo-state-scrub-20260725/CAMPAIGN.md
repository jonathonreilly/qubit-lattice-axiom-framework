# CAMPAIGN: repo-state scrub — diagnose the governance failure, then repair

Opened 2026-07-25 at owner direction. Durable state; readable cold.

## Why

Two consecutive science campaigns burned a wave each REDISCOVERING
material that already existed in the repo. Root-cause evidence
collected so far:

- Runner-gated results (Schur-Weyl commutant, sign-of-b analysis, the
  ground-sector invariant, a three-site eta counterexample) sit in
  `docs/work_history/repo/review_feedback/` as **unowned prose with
  no claim id and no ledger row**; one is explicitly marked
  "Authority: none". Two repo runners compute them.
- 44 mutually circular prose/ledger contradictions across 14 claim
  ids in ONE lane; ~75 rows / 279 lines corpus-wide.
- 438 `no_go` rows: 437 `unaudited`, 1 `audited_conditional`,
  **0 retained anywhere in the repo**.
- A registered derivation obligation whose own `## Exact target` and
  whose machine registry entry OMIT a conjunct that the note's
  re-audit notes treat as binding; `audit_lint.py:693-706` never
  reconciles them.
- The parent-shaped gate `MINIMAL_AXIOMS_2026-06-29.md:170`
  ("source/action and physical-observable identification") is
  **UNREGISTERED** — no node, no ledger row, no closure criterion.
- Runner caches with `cache_freshness: "missing"` and helper runners
  not linked from their notes (one such was repaired this week and
  had caused a prior audit round to fail).

## The diagnostic question the owner asked

Is the failure (a) science never ENTERING the audit pipeline
(missing registration/capture), (b) prose/ledger DIVERGENCE (stale or
false status labels), (c) PIPELINE GAPS (the lint does not check the
things that would have caught this), (d) obligation/registry
integrity, or (e) some combination — and in what proportions?

Phase 1 MEASURES this. Phase 2 repairs, in prioritized batches.

## Hard constraints on any repair

1. **PRs cannot land audit data.** Science/fixes only; restore
   `docs/audit/data/`, `AUDIT_LEDGER.md`, `AUDIT_QUEUE.md`,
   `MISSING_DERIVATION_PROMPTS.md`, and
   `docs/publication/ci3_z3/*_EFFECTIVE_STATUS.md` from origin/main
   before committing. Pipeline runs are VALIDATION ONLY.
2. **Never set or predict an audit verdict.** Repairs make rows
   correct and auditable; the audit lane alone grades them.
3. **AUDIT-HASH CHURN GUARD IS THE MAIN RISK.** Note hashes are
   source-content hashes. A mass cosmetic sweep over audited claim
   notes would requeue large parts of the ledger for nothing. Every
   repair batch must state, BEFORE landing: how many rows it
   requeues, how many verdicts it risks, and why the trade is worth
   it. Prefer repairs that touch NON-audited rows, or that are
   genuine science corrections (a note asserting a false status IS a
   science correction), or that are tooling changes rather than
   content churn.
4. **A tooling fix beats a content sweep.** If `audit_lint` can be
   taught to CATCH a defect class, that is worth more than
   hand-fixing today's instances, and it costs zero audit churn.
5. No new axioms, primitives, or vocabulary. Do not invent status
   values.

## STATUS LOG

- **Wave 0 (2026-07-25).** Phase 1 diagnosis dispatched: five
  measurement briefs (unregistered science; prose/ledger divergence;
  pipeline gap analysis; runner/cache hygiene; obligation/registry
  integrity). Each must return COUNTS and a prioritized, batched
  repair plan with churn cost per batch.
  **Supervisor prediction, recorded before results:** the dominant
  failure is (c) PIPELINE GAPS enabling (a) — i.e. nothing in the
  toolchain requires that a result with a runner be registered as a
  claim, so `work_history/` became a write-only sink for real
  science. I expect prose/ledger divergence (b) to be large in COUNT
  but low in severity (mostly stale labels on rows nobody cites),
  and obligation/registry integrity (d) to be small in count but
  high in severity. If that is right, the highest-value repair is a
  LINT RULE plus a one-time registration pass over the genuinely
  load-bearing orphans — not a mass prose sweep, which would burn
  audit capacity for cosmetics.
