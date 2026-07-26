# Audit Lane

> **Key terms used in this doc** are indexed A-Z at [docs/KEY_TERMINOLOGY.md](../KEY_TERMINOLOGY.md); each row points to the canonical source-of-truth doc.

**Status:** infrastructure lane for `main`.
This lane does not produce physics claims. It audits existing ones.

## What this lane does

The publication package historically mixed author-facing status labels with
claim strength. The audit lane now separates those concerns: the auditor sets
`claim_type`, the auditor sets `audit_status`, and the pipeline derives
`effective_status` through the citation graph. Nothing presents as retained
to the outside world unless the scoped audit chain is clean.

The first repo-wide trace (CKM atlas) showed several failure modes that
self-declared tiers do not catch:

1. **Definition-as-derivation** — a new symbol is defined as a small-integer
   ratio, then "shown" to match data by name substitution.
2. **Conditional-on-open-work** — a `retained` note depends on a `support` or
   `open` note for the load-bearing identification step.
3. **Algebraic decoration** — many `retained` corollaries are consequences of
   a single upstream parameter choice and add no independent physical content.
4. **Stale narrative wrappers** — a failed wrapper frame remains easy to cite
   even after its audit verdict invalidates the global story.

The audit lane mechanizes detection of these patterns.

## Layout

```
docs/audit/
  README.md                          # this file
  FRESH_LOOK_REQUIREMENTS.md         # who may audit what, and how
  ALGEBRAIC_DECORATION_POLICY.md     # how to identify and prune decoration
  STALE_NARRATIVE_POLICY.md          # how to archive failed wrapper frames
  AUDIT_AGENT_PROMPT_TEMPLATE.md     # the prompt template for cold auditors
  AUDIT_LEDGER.md                    # ignored, materialized human-readable cache
  data/
    ledger/<id[:2]>/<id>.json        # tracked source of truth: one claim row per shard
    ledger_meta.json                 # tracked source of truth: top-level ledger metadata
    audit_ledger.json                # ignored materialized monolith cache
    citation_graph.json              # ignored generated doc -> cited-authorities cache
    source_path_aliases.json         # controlled: source-note renames preserving audit rows
    runner_classification.json       # ignored generated A/B/C/D cache
    audit_dispatch_queue.json        # generated: targeted re-audits normal queue will not surface
  scripts/
    build_citation_graph.py          # parse all .md docs into the graph
    seed_audit_ledger.py             # initialize ledger rows from claim notes
    classify_runner_passes.py        # classify runner outputs by check type
    compute_effective_status.py      # propagate audit results down the graph
    compute_audit_dispatch_queue.py  # render dispatcher sidecars into audit_dispatch_queue.json
    audit_lint.py                    # validate ledger consistency
```

Run `python3 docs/audit/scripts/ledger_io.py --materialize` before directly
using a legacy monolith reader. All ledger writers must call
`ledger_io.save_ledger()`; direct edits to the ignored monolith are refused.

## Scope-aware fields

The audit lane separates **classification** from **verdict**. Authors may
write whatever status prose they need inside source notes, but the retained
library is driven only by auditor-owned fields:

- `claim_type` — what kind of object the auditor says the row is:
  - `positive_theorem`
  - `bounded_theorem`
  - `no_go`
  - `open_gate`
  - `decoration`
  - `meta`
- `claim_scope` — the auditor's short, citeable statement of what was
  actually audited. This is required for applied audits.
- `audit_status` — what the audit found:
  - `unaudited`
  - `audit_in_progress`
  - `audited_clean`
  - `audited_renaming`
  - `audited_conditional`
  - `audited_decoration`
  - `audited_failed`
  - `audited_numerical_match`
- `effective_status` — derived, publication-facing status:
  - `retained` for `claim_type = positive_theorem` plus
    `audit_status = audited_clean` plus retained-grade dependencies.
  - `retained_no_go` for `claim_type = no_go` plus
    `audit_status = audited_clean` plus retained-grade dependencies.
  - `retained_bounded` for `claim_type = bounded_theorem` plus
    `audit_status = audited_clean` plus retained-grade dependencies.
  - `retained_pending_chain` for a clean theorem/no-go/bounded row whose
    upstream chain is not yet retained-grade.
  - `open_gate` for a clean open gate; this blocks retained propagation.
  - `decoration_under_<parent_claim_id>` for an audited decoration whose
    parent is retained-grade.
  - `meta` for non-claim infrastructure rows.
  - `audited_<failure_mode>` for terminal non-clean audit verdicts on active
    claims.

Foundational-premise dependencies are handled by
`docs/audit/scripts/premise_nodes.py`. Exactly two supplied premise types satisfy
chain closure without bounding a row: axioms and explicitly approved framework
primitives in `docs/audit/data/axiom_premise_nodes.json`. Derivation obligations,
historical admissions, governance decisions, and conventions do not satisfy a
dependency. They must earn retained-grade normally or leave the consumer
conditional/pending-chain.
- `prose_status` — vocabulary-drift status, orthogonal to `audit_status`. See
  `docs/repo/VOCABULARY_HYGIENE_DESIGN.md`. One of:
  - `clean` — no vocabulary drift detected by `vocab_lint`.
  - `auto_corrected` — routine drift mechanically rewritten by
    `vocab_lint --fix`; rewrites logged in `prose_corrections`.
  - `needs_human_vocab_decision` — genuinely new term that `vocab_lint`
    cannot mechanically rewrite; queued for periodic vocab-extension review.
  - `not_evaluated_pre_vocab_lint` — pre-Cleanup-1 row never linted under
    the new rules, or a newly seeded/source-drift row has not yet been
    linted under the new rules. Used as the seeder/backfill default.
  - `queue_backpressure_exceeded` — vocab-extension review queue is >50
    entries deep; new unresolved terms emit this until the queue is
    processed.

  `prose_status` does **not** propagate into `effective_status`. A
  non-clean prose_status never demotes a physics-clean row; a clean
  prose_status never promotes a physics non-clean row. Physics and
  vocabulary are reviewed by separate mechanisms.

- `prose_corrections` — list of `(rule_id, before, after)` tuples recording
  the mechanical rewrites `vocab_lint --fix` applied to the source note
  during the same audit cycle.

When an audit chain runs `vocab_lint --fix` on the source note before
applying the verdict, the resulting note-hash refresh and the
`prose_status` / `prose_corrections` write happen atomically via a
`pre_audit_prose_fix` envelope on the incoming audit blob:

```json
{
  "claim_id": "...",
  "verdict": "audited_clean",
  ...,
  "pre_audit_prose_fix": {
    "old_hash": "<row.note_hash before vocab_lint --fix>",
    "new_hash": "<note_hash after vocab_lint --fix>",
    "prose_status": "auto_corrected",
    "prose_corrections": [
      {"rule_id": "legacy_alias_strip", "before": "(legacy alias: A1)", "after": ""}
    ]
  }
}
```

`apply_audit.py` verifies `old_hash` matches the ledger's current
`note_hash`, then refreshes `note_hash` to `new_hash` before the
hash-drift check; without the envelope, running `vocab_lint --fix`
would immediately invalidate the audit. The envelope is the supported
atomic refresh path.

Generated audit data must not contain legacy source-status authority fields.
The graph builder may use old source-note status prose as a one-way migration
hint when seeding `claim_type`, but the ledger, queue, prompt, and rendered
audit surfaces are `claim_type` / `audit_status` / `effective_status` only.
`support` is not a claim class. Once a legacy support-labeled note has an
`audited_clean` verdict, it retains according to its ledger `claim_type` and
dependency closure; old source-note prose neither grants nor blocks retained
status.
Legacy critical rows whose confirmed clean cross-confirmation predates
`claim_type` may clear `claim_type_backfill_reaudit` with a restricted-input
audit that writes the scoped `claim_type`; missing `claim_type` fields in the
old confirmation summaries are migration debt, not a cross-confirmation
disagreement.

## Claim typing at authoring time

Every new source note under `docs/` must declare its claim class with an
explicit header line the graph builder can read:

```
**Type:** positive_theorem | bounded_theorem | no_go | open_gate | decoration | meta
```

`seed_audit_ledger.default_claim_type_for` resolves the seeded `claim_type`
in this precedence order (the auditor always owns the final value):

1. `data/meta_source_patterns.txt` — curated per-file registry for
   catalog/index/infrastructure docs (e.g. `docs/CANONICAL_HARNESS_INDEX.md`);
   applies even over author hints.
2. The explicit `Type:` / `Claim type:` header, else the legacy
   Status-line migration hint.
3. Infrastructure directory families
   (`seed_audit_ledger.INFRA_META_PATH_PREFIXES`: `docs/repo/`,
   `docs/work_history/`, `docs/lanes/`, `docs/publication/`,
   `docs/ai_methodology/` — the same families as
   `data/excluded_source_patterns.txt`): hint-less notes under these paths
   seed as `meta` (documentation, not claims).
4. Fallback: `positive_theorem` with provenance `default_positive_theorem`.

Tier 4 is visible debt, not a hidden state: `audit_lint.py` warns on every
such row (`claim_type_defaulted`), and `pre_commit_audit_check.sh` (via
`check_staged_claim_typing.py`) refuses staged notes that would enter or
stay in the defaulted class, so the legacy backlog can only shrink.

`meta` deserves care in both directions: meta rows are never queued for
audit and chain-satisfy their dependents as stable context, so `meta` is
reserved for documents that carry no claim any dependent could consume as
evidence.

Exclusion is history-preserving: a ledger row whose path matches
`data/excluded_source_patterns.txt` is dropped at the next seeding run
only when it is an unaudited unknown — no terminal or in-flight
`audit_status` and no archived `previous_audits` (lint notice
`excluded_path_row_pending_drop` until then; the seeder also strips the
dropped row's ids from dependents' dep lists, so no dangling edges).
Rows carrying audit history are never auto-dropped — retroactive
exclusion must not erase audit evidence; they stay in the ledger,
surface as `excluded_path_row_grandfathered` lint notices, and retiring
them is an owner/audit-lane decision. Exact paths in
`data/never_gate_source_paths.txt` always stay.

### Draining the `claim_type_defaulted` backlog

The `claim_type_defaulted` lint warning list is the worklist; the
pre-commit gate stops regrowth. Per row, in order of preference:

1. **Infrastructure/doc rows** — covered by the meta tiers above or by
   exclusion; nothing to do beyond the next seeding run.
2. **Claim notes whose own text states the class** — add the matching
   `Type:` header. This is an author hint only: the auditor confirms the
   type at audit, and a header must describe the note as written, never
   retype content to fit a desired class.
3. **Evidence-adjacent catalogs** (package READMEs, `*_ledger` /
   `*_packet` summaries with citers) — do **not** register these as meta
   first; meta chain-satisfies dependents unaudited, so premature meta
   typing launders evidence edges. Apply the dependency-honesty protocol
   (precedent: PR #4780): read each citing note, rewire edges that
   consume evidence to the underlying evidence notes, demote navigation
   references to backticked context — and only when no dependent
   consumes the catalog as evidence, register it in
   `data/meta_source_patterns.txt`.

## The hard rules

1. **Retained grade is audit-only.** The audit lane may grant
   `effective_status = retained`, `retained_no_go`, or `retained_bounded`
   only from `claim_type + audited_clean + retained-grade dependencies`.
   Author labels and source-note status prose do not promote rows.

2. **Open gates block propagation.** `open_gate`, `unaudited`,
   `audit_in_progress`, `retained_pending_chain`, and terminal non-clean
   audit verdicts are not retained-grade dependencies.

3. **No self-audit.** The auditor of a claim must not share identity with
   the claim's author. The best available full Codex GPT model at maximum
   reasoning is the designated independent auditor for this repo (see
   `FRESH_LOOK_REQUIREMENTS.md`); using a different model family from the one
   that produced most existing notes satisfies the cross-family condition,
   while same-family confirmation must be recorded as `fresh_context` from a
   distinct restricted-input session.

4. **Decoration must be boxed.** Claims tagged `audited_decoration` cannot
   appear as separate retained rows in the publication-facing tables; they
   roll up under their parent claim. See `ALGEBRAIC_DECORATION_POLICY.md`.

5. **Publication tables consume effective status.** Public tables must read
   `effective_status` from the audit ledger or an artifact derived from it,
   not source-note status prose.

6. **Runner timeout is not a verdict.** A wall-time timeout, missing stdout,
   or noncompletion of a long-running runner is not evidence that the
   scientific claim is wrong, conditional, or failed. If the load-bearing
   step cannot be judged without that run, the row remains pending with a
   compute-required blocker or is skipped in the current audit loop until a
   completed log, faster/sliced runner, cached certificate, or independent
   derivation is supplied. A terminal non-clean verdict may cite concrete
   runner evidence such as a completed mismatch or an executable/import error,
   but not mere long compute.

   This rule is retroactive as an audit policy check. A legacy terminal
   non-clean row whose primary rationale is only wall-time exhaustion,
   missing stdout, or another compute-budget limit must be treated as a
   policy-repair/re-audit candidate, not as settled scientific evidence. Do
   not mechanically reset rows that also contain an independent substantive
   blocker; repair those by re-auditing the actual blocker under the current
   restricted-input process.

## Workflow

### Mechanical phase (cron-able)

```bash
python3 docs/audit/scripts/build_citation_graph.py
python3 docs/audit/scripts/seed_audit_ledger.py
python3 docs/audit/scripts/classify_runner_passes.py   # optional, slow
python3 docs/audit/scripts/compute_effective_status.py
python3 docs/audit/scripts/audit_lint.py
```

This (a) keeps the graph in sync with the docs, (b) seeds new claim notes as
`unaudited`, (c) classifies runner PASSes by check type, (d) recomputes
`effective_status` everywhere, (e) lints for cycles, dangling citations, and
inconsistent inheritance.

### Audit phase (per claim, semi-automated)

For each `unaudited` claim, an audit agent is spawned with
`AUDIT_AGENT_PROMPT_TEMPLATE.md`. The agent receives only:

- the source note,
- the source note's directly cited authorities (one hop),
- the rubric,
- the runner's classification breakdown.

The agent does **not** receive the broader publication framing or the
publication-facing claim status. That is the "fresh look" requirement. The
agent returns a fill of the audit row.

Live primary and independent-helper stdout use a named 20,000-character
per-section budget. Oversized output retains both its header and tail through
deterministic head+tail clipping; the clipping marker remains load-bearing
evidence, so an `audited_clean` verdict is still forbidden until the complete
needed evidence fits. The overall prompt keeps its separate 1,000,000-character
soft transport limit.

If the primary runner is load-bearing but does not complete inside the
current audit budget, the audit is not applied as `audited_conditional` or
`audited_failed` for that reason alone. The loop records a local
`compute_required` skip, or tooling records `audit_in_progress` with a
compute blocker when supported, and then continues to the next ready row.
Rows skipped this way need a completed run artifact, reduced deterministic
runner, or proof-level replacement before re-audit.

For every `audited_conditional` or `audited_renaming` result, the auditor
must make the repair lane machine-sortable by prefixing
`notes_for_re_audit_if_any` with one repair class:

- `missing_dependency_edge` — a needed source note or authority exists or is
  named, but is not wired as a direct dependency for the audited claim.
- `dependency_not_retained` — a direct dependency exists but is not retained
  grade.
- `missing_bridge_theorem` — the claim needs a new theorem for a physical
  carrier, readout, unit map, boundary condition, sector choice,
  normalization, or observable bridge.
- `scope_too_broad` — a clean bounded core exists, but the current claim scope
  includes an unclosed extension.
- `runner_artifact_issue` — a runner, log, classifier, threshold, import, or
  pass/fail accounting problem blocks closure despite otherwise local scope.
- `compute_required` — closure needs a completed long run, sliced runner,
  cached certificate, or independent derivation.
- `other` — none of the above fits; the note must state why.

After the class, the auditor names the cheapest next repair action. Examples:
add an explicit citation/dependency edge, audit a named dependency first,
create/open a bridge theorem, split a clean bounded core from a conditional
extension, or repair/slice a runner. The audit lane surfaces these repairs; it
does not perform them unless explicitly asked.

When the cheapest repair action is dependent-side (for example, narrowing
downstream citing sentences to the audited scope), the named action must also
include adding a dated downstream-hygiene line to the audited note's own
boundary. Terminal rows re-enter the audit queue only through their own
note/runner hash drift or a dispatcher sidecar; a dependent-side repair that
never touches the stuck row itself satisfies the audit's condition without
ever rescheduling the row for re-audit.

For high-stakes claims (`criticality = critical` by transitive-descendant
count; the audit lane does not use author-declared flagship status), a second independent
agent runs the same audit; the two must agree before `audited_clean` lands.
If two validator-clean, applyable audits disagree, the next step is a governed
five-judge panel. Five fresh judges read the restricted source packet and both
audit arguments, vote on the complete scientific tuple, and explain the error
in any position they reject. At least three matching votes are required. No
majority, a majority for neither, or an unapplyable majority launches another
fresh five-judge panel with all prior outcomes in context. Contract-invalid
seats are reseated before a panel; they are not scientific disagreements. The
ledger keeps legacy `third_audit` storage fields for the representative panel
judgment, but a single third auditor has no authority to resolve disagreement.
The apply gate requires an invocation-bound `judicial_panel_record_v1` carrying
five distinct valid votes, the current source/seat fingerprint, and a matching
3-of-5 complete-tuple majority before it writes that legacy projection.

### Pruning phase (per decoration cluster)

When a claim is marked `audited_decoration`, the pruning policy
(`ALGEBRAIC_DECORATION_POLICY.md`) decides whether it gets:

- **Boxed** as a corollary inside its parent note, or
- **Removed** if it adds no falsifiability and no compression.

## Reading the publication package after audit

External readers should read `effective_status`. The audit ledger is the
canonical surface for claim strength.

## What this lane is not

- Not a physics result.
- Not a replacement for peer review (it is the strongest internal check that
  is feasible without external reviewers; external review remains the
  separate, missing ingredient for actual disciplinary impact).
- Not a re-derivation of the physics — the audit checks whether the existing
  derivations close, not whether alternative derivations exist.

## Two-Tier Assurance And Rolling Certification (2026-07-12, owner-approved)

The lane runs two assurance tiers:

- **Development tier (default).** Verdicts bind to claim content (note,
  runner, and premise hashes) and survive unrelated repository growth. Every
  audit still requires independent cross-family re-derivation at xhigh and
  the two-pass cross-confirmation flow on critical rows. Wall-naming
  positive/bounded rows apply the No-Go Discipline as auditor judgment, and
  any supplied N1-N8 packet is validated structurally (no manifest-backed
  containment, live-stdout, or full-universe disposition plumbing).
- **Forensic tier.** Mandatory for `claim_type: no_go` rows and no-go-named
  source files (foreclosure is permanent), and for freeze/certification runs
  (`AUDIT_FORENSIC_MODE=1`),
  which force the full heavyweight regime lane-wide against a pinned commit:
  authenticated evidence transport, verbatim-contained route evidence, live
  runner-stdout citation, and complete index dispositions with authenticated
  omitted-tail summaries.

**Rolling certification** replaces scheduled freezes: the pipeline
continuously reports, per flagship lane
(`docs/audit/data/lane_certification_config.json` →
`docs/audit/data/lane_certification.json`), whether every configured scientific
root claim and their combined transitive dependency closure are chain-satisfying
against the current state. Retained-grade rows, decorations of retained parents,
and registered accepted premises satisfy the marker; metadata does not.
Certification is a state the repository re-enters as audit throughput
catches up; a marker rolling back after an axiom or source change is the
honest coordination signal for collaborators, not an error. If a publication
or replication request ever needs a citable artifact, snapshot the lane's
currently-certified commit and run the forensic tier over its closure there.
Some configured roots intentionally name unresolved scientific `open_gate`
obligations. Those lanes remain uncertified until source-level science retires
or replaces the open root; audit throughput alone cannot certify an open gate,
and substituting an already-retained surrogate would hide the live obligation.
