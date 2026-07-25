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

---

## PHASE 1 RESULT (2026-07-25): ROOT CAUSE IS AN EXCLUSION GLOB

Measured against `origin/main` @ `f865c14cd4`.

**It is not a missing lint. It is a LOCATION GATE.**
`docs/audit/data/excluded_source_patterns.txt:19` contains
`docs/work_history/**`, and `seed_audit_ledger.py:210-247
should_gate_node()` DROPS any matching node with no audit history.
A result written there can NEVER acquire a claim id, note hash,
runner pin, queue entry, or verdict — **regardless of quality**.

Proportion answering the owner's question:
**(c) pipeline gap enabling (a) never-entered = 647 : 0.**
The live `docs/*.md` surface is **100% registered**; there is ZERO
ordinary pipeline lag. Prediction confirmed and sharpened: the
missing rule is not "require registration" but **"refuse a
runner-bearing note under an excluded path."**

### COUNTS

- **647** of 4522 `docs/**.md` have no ledger row; **all 647**
  structurally gated by the glob; **0** are lag.
- **533** carry a result marker (446 under work_history, 430 dated
  2026-07); **470 name a runner that EXISTS on disk**.
- **1280** orphan runners (479 named by no markdown at all);
  **292** undeclared helpers.
- **95 terminal-verdict rows (58 `audited_clean`) name a runner
  their ledger row does not hash-pin.**
- Caches: 118 ledger-claimed runners with no cache, 31 stale, 1234
  orphan runners uncached.
- Triage: **TIER 1 = 70**, TIER 2 = 305, TIER 3 = 55.
- **One commit did most of it:** `9caad99bab` (2026-07-18,
  "archive: preserve TOE bridge campaign evidence through cycle335")
  added **417 notes + 469 runners** straight into the archive.
  `git log --follow --diff-filter=A` shows the archive was the
  **BIRTH LOCATION** — nothing was ever actually archived.

### SECOND, COMPOUNDING DEFECT

`build_citation_graph.py:129-133 RUNNER_SECTION_RE` **omits
`Verification`** — which is the DOMINANT house convention: **808
notes** use `## Verification` to name their runner, and **52 resolve
to `runner_path = None`**, including all four 2026-07-14 targets.
They are triply invisible: `Type: meta`, no ledger row, no runner.

### THE A-MATERIAL'S OWN RUNNERS ARE DEFECTIVE

Four asserted-but-not-gated items, and they are the load-bearing
constants: the `sign(b)` quotient is "gated" only by the VACUOUS
literal `{-1,1} == {sp.sign(v) for v in (-3,5)}`; common-frame
covariance is claimed but the runner checks only Hermiticity and
commutation; the active-edge phase is a hand-built `sp.diag(1,2)`;
and two gates are the same check twice. **~34% of that runner's 44
PASS lines are prose-needle greps on its own text.** So the existing
runners CANNOT serve as the note's runner — a new consolidated
runner is required.

### NEW RESULT (nowhere in the repo)

The band-minimum separator provably fails: `Z^3` is bipartite by
`x+y+z` parity, the sublattice relabeling gives `D A D = -A` hence
`spec(A) = -spec(A)`, so the `+J` and `-J` one-excitation bands are
IDENTICAL after the licensed energy shift (verified on P3/C4/Q3/K2,3,
with a non-bipartite triangle as the breaking mutation).
**Ground-sector degeneracy 1-vs-3 is the correct invariant.**

## PHASE 2 (dispatched): repair, cheapest-and-highest-value first

- **R1 tooling, zero churn:** `audit_lint` ERROR for "a `docs/**.md`
  naming an existing `scripts/*.py` under an excluded glob". Catches
  all 470, blocks regrowth, requeues 0 rows, risks 0 verdicts.
- **R2 tooling, 4 requeues (all `unaudited`, 0 verdicts risked):**
  teach `extract_runner` the `## Verification` heading, trying it
  LAST (measured gains=52, changes=0; merging it into the regex
  in place instead CORRUPTS 5 notes' runner_path).
- **R3 science, 0 requeues:** land the 2026-07-14 material as a
  claim-id'd note with a NEW consolidated runner carrying real gates
  (no vacuous literals, no prose-needle padding), the three dropped
  limitations stated, and ground-sector degeneracy as the invariant.
- **R4 (owner decision, NOT dispatched):** registering the remaining
  TIER-1 orphans (70) is a policy call about what `work_history/`
  is FOR — the exclusion glob may be deliberate. Flagged, not acted on.
