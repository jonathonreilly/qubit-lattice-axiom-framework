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

---

## PHASE 2 RESULT (2026-07-25): both repairs landed as PRs

**PR #5603 — the tooling fixes (R1 + R2).**
- R1: new `audit_lint` error `unregistered_runner_bearing_note`,
  detected via the citation graph's own runner attribution (no new
  regex surface, and it widens automatically with R2). Shipped with
  a **grandfather baseline** of 398 paths — firing on the existing
  population would have put 398 errors into `--strict` and hard-
  blocked every lane with no drain path. Drained entries surface as
  `..._baseline_stale` notices so **the list can only shrink**.
  The baseline deliberately lives in `docs/audit/scripts/`, NOT
  `docs/audit/data/`, because that directory is restored wholesale
  from origin/main before every PR and a baseline there would have
  each drain silently reverted. No env/flag bypass.
- R2: `## Verification` capture, tried LAST. Both phase-1 numbers
  re-verified on current main: LAST -> gains 52, losses 0, changes 0;
  merged in place -> changes 5 (five named notes corrupted).
- Churn: 4 rows re-seeded, **0 requeues** (audit queue
  byte-identical), **0 verdicts risked**, measured twice across 17
  intervening audit commits, identical both times.
- Gates: vocab_lint 0 violations; pipeline PASS; `audit_lint
  --strict` **exit 0**; `git diff --check` clean; 746 tests + 12 new.

**PR #5602 — the A-registration.**
`docs/COMMON_FRAME_PAIR_GENERATOR_EXCHANGE_CLASS_BOUNDED_THEOREM_NOTE_2026-07-25.md`
+ a NEW consolidated runner (**46/0**) + SHA-pinned cache. All three
limitations carried as claim content, and the note explicitly records
that the band-minimum separator FAILS (`Z^3` bipartite by `x+y+z`
parity, `D A D = -A`, `spec(A) = -spec(A)`). Churn: **0 requeues,
0 verdicts risked, 1 row added** (`unaudited`, `ready: true`).

Design decision worth keeping: the four 2026-07-14 sources are cited
in BACKTICKS, not markdown links — they are route inputs, not
evidence, every step is recomputed natively, and a markdown link
would seed a citation-graph edge to a row the seeder drops.

### CORRECTION TO MY OWN PHASE-1 NUMBER

I reported **470** runner-bearing excluded-path notes. Under the
precise rule actually shipped (no ledger row, not `never_gate`d,
graph-attributed runner existing on disk) the population is **398**.
My looser body-mention scan reproduces at 475 and sweeps in narrative
infrastructure (e.g. `review-loop/SKILL.md` naming `vocab_lint.py`).
The graph detector is the right one; my count was inflated.

### STILL OPEN (owner decisions, deliberately NOT acted on)

- **R4: register the 398 grandfathered notes.** This is a policy
  call about what `docs/work_history/` is FOR — the exclusion may be
  deliberate. The debt is now recorded and cannot grow.
- 7 pre-existing test failures (`NoGoDisciplineGateTest` x4,
  `FingerprintV1StampingTest` x3) reproduce identically on unmodified
  origin/main; they touch audit-verdict gates. Flagged, not touched.
- The 95 terminal-verdict rows (58 `audited_clean`) naming runners
  their ledger rows do not hash-pin — untouched, and the most
  alarming remaining item.

---

## WAVE 3 RESULT (2026-07-25): both integrity items are WORSE than measured

### 1. RUNNER PINNING — my phase-1 count was an UNDERCOUNT (PR #5609)

"Hash-pinned" means `audit_state_snapshot.runner_hash` (legacy
comparator fires ONLY when non-null) and `helper_runner_hashes` (the
comparator SKIPS the entire helper channel when absent).
`runner_sha256` and `cache_freshness` do NOT pin.

| snapshot state | rows | verdicts |
|---|---|---|
| names a runner, `runner_hash` null/absent | **78** | 77 clean |
| declares helpers, no `helper_runner_hashes` | **182** | 169 clean |

**Union: 223 rows — 209 `audited_clean`, 208 retained-grade.**
My phase-1 figure ("95 terminal / 58 clean") does not reproduce: the
true clean exposure is **209**, and phase 1 **missed the helper
channel entirely — which is the larger one.**

**Structural root:** `FINGERPRINT_STAMP_VERDICTS =
{audited_conditional, audited_failed}` — **a CLEAN verdict has never
received a v1 fingerprint. Zero of 450 `audited_clean` rows carry
one.** Single cause for all 223: audited before the writer recorded
the field (`runner_hash` added 2026-05-16, `helper_runner_hashes`
2026-07-15). Cache-never-generated: 0. Parse-invisible: 0.

**37 ACTIVE integrity failures** (1 primary + 36 helper), 186 latent.
The smoking gun: `dm_lepton_synthesis_note_2026-04-19` —
`audited_clean`, `effective_status: retained` — names a runner
REWRITTEN 2026-07-12 ("narrow to supplied-input S_3 selection
table", withdrawing four observational-closure phrases and admitting
three external inputs). **Its sibling row cites the SAME runner, was
re-audited, and is `audited_conditional`. This row kept `retained`
purely because it pins nothing.** Helper channel: 40 rows drifted,
ALL substantive, 36 clean, 35 retained-grade.

Repair is tooling-only: a writer gate refusing to stamp a terminal
verdict that leaves a named runner unbound, plus a shrink-only
baseline recording each runner's sha AT BASELINE TIME so the legacy
population is FROZEN — further movement raises instead of passing
silently. **Snapshot back-fill REFUSED**: writing today's sha would
assert the auditor saw current content, which is exactly what the
missing pin makes unknowable, and would erase the 44 measured drifts.

### 2. NO-GO RETENTION — neither structural nor backlog. The verdicts
are MADE, then DESTROYED. (PR #5607)

439 no_go rows, **0 `retained_no_go`** — but
`compute_effective_status.py:41` maps `no_go -> retained_no_go` and
**the promotion rule works**. 53 audit commits landed `audited_clean`
on currently-no_go rows in 14 days, in cross-confirmed pairs. All
read `unaudited` today.

**187 archived clean no_go verdicts were reset by a
`no_go_discipline_packet_*` reason. Median lifetime 35 days; 27 under
a day; shortest 32 MINUTES.**
`spatial_cubic_time_anisotropy_gate_no_go` (critical, in-degree 12,
741 descendants) has been minted clean **four times** — once by a
five-judge judicial panel — and reads `unaudited`.

Three mechanisms, each traced to a line:
1. **No dispatch selector will ever feed a no_go row.**
   `AUDITABLE_TYPES = {positive_theorem, bounded_theorem, open_gate}`.
   The batch drainer produced ~1100 of 1108 verdicts in 14 days and
   **can never produce a no-go one**; only a canary remains, ONE row
   per loop pass against 140 ready rows.
2. A development-tier verdict on a no_go row is **auto-reset** —
   162 instances, including the judicial-panel verdict.
3. A verdict WITH a packet is authenticated **against a moving
   target**: the required field set grew with the tag unchanged, so
   **zero shards contain `verified_values`** and replaying all 30
   archived clean forensic packets returns malformed **30/30**. And
   invalidation compared authority status by EQUALITY, so a
   dependency STRENGTHENING (`meta -> retained`) invalidated the
   citing no-go verdict. **Draining the backlog was deleting the
   foreclosures that cited it.**

**Consequence:** the ten most-cited foreclosures are all `critical`
and all `unaudited`, and because the resets STRIP `claim_scope`,
**the live ledger no longer records what any of them forecloses** —
scopes had to be recovered from `previous_audits`. One row with
in-degree 29 and 726 descendants has no recorded scope at all.

Repair (0 churn): rank-decrease-only forensic invalidation matching
the dev tier; a shared writer/reader contract for the evidence
snapshot plus the test that would have caught the breaking change;
and repair of the 4 `NoGoDisciplineGateTest` N7 cases, which were
patching `REPO_ROOT` to a bare tempdir and **asserting the FAILURE
path of the very mechanism a forensic no-go packet depends on**.

**COLLISION WARNING:** those 4 tests overlap with the separately
started owner task on the 7 pre-existing audit-gate test failures.
