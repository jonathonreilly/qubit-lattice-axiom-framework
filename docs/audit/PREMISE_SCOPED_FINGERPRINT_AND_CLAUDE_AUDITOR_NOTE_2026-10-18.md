# Premise-Scoped Audit Fingerprints and Clean-Room Claude Auditor Seats (2026-10-18)

**Claim type:** meta
**Status:** audit-tooling and process change note. It applies no audit verdict,
adds or amends no axiom or primitive, and carries no premise weight.

This note records two owner rulings made on 2026-10-18 and the tooling that
implements them, in the form `docs/ai_methodology/SCIENCE_WORKFLOW.md` section
9 asks of a rule change: the defect, the affected callers, the expected
decisions, and a realistic counterexample.

## Owner rulings

1. **Auditor independence.** The owner does not require a different model
   family, only that "the auditor itself is a clean fresh model or agent", and
   accepts Claude Opus 5.5 audits at medium effort. Recorded in
   `docs/audit/FRESH_LOOK_REQUIREMENTS.md` section 1.
2. **Axiom changes.** The axioms will change when the theory of everything
   needs it, so an audit must survive an edit to premise content it did not
   use. Recorded in `docs/audit/FRESH_LOOK_REQUIREMENTS.md` section 6.

## Defect 1: every premise byte edit re-opened every audit

`science_fingerprint_v2` embedded one repository-wide `framework_premise_epoch`
in every judgment. That epoch hashes the whole of `axiom_premise_nodes.json`,
the whole axiom memo (four axiom sections plus purpose, history and relation
commentary in one file), and the three primitive notes. Any byte change in any
of them changed every judgment's fingerprint. Each direct citer's dependency
entry also bound the memo's whole-file hash, and the pre-v2
`dep_axiom_premise_note_hash` check fired on the same edit.

Evidence on `main` at `584755767`: 2,506 ledger rows hold archived audits and
none hold a live verdict (`docs/repo/FRONT_DOOR_STATUS.md`: 0 applied
verdicts). For 822 of those rows the most recent archive was invalidated with
`legacy_framework_premise_epoch_changed` or
`science_changed:framework_premise_epoch`, the most common recorded reason.
`AXIOM_RESET_IMPACT_2026-06-29.md` records an earlier 251-row reset from one
memo change.

### Change

- **`science_fingerprint_v3`** (`docs/audit/scripts/audit_science_fingerprint.py`).
  A judgment's `premise_scope` is either `fail_closed`, which binds exactly what
  v2 bound, or `declared`. A declared judgment binds only the premise units
  named in its `premises_used`, plus every unit of a premise node it cites
  directly but did not name, plus each node's shared clauses. Each unit digest
  binds the node's registry membership and paths, its clause-map entry and the
  exact unit text. The registry's descriptive `note` is excluded because the
  axiom statements live only in the memo (README) and every axiom edit restates
  the whole node in that note. A premise dependency's whole-file hash is
  replaced by its scoped unit list.
- **Premise units** (`docs/audit/data/premise_clause_map.json`). The four
  sections under `## The Four Framework Axioms` are `minimal_axioms:lattice`,
  `:qubit`, `:admissibility` and `:record`. `## Qualification` is a shared
  clause bound with every `minimal_axioms` unit. Each approved primitive is one
  whole-note unit. Sections are located by their existing headings, so neither
  the memo nor the registry was edited: 819 runners declare the memo and 109
  declare the registry as `AUDIT_INPUT_PATHS`, and editing either would have
  staled those runner caches.
- **One comparator.** Every caller that compares against a stored baseline now
  uses `build_matching_science_fingerprint`. It rebuilds a v2 baseline under
  the exact v2 rule and a v3 baseline under the baseline's own recorded
  declaration, never the row's current field.
- **Declarations.** The auditor returns `premises_used` (prompt section 5 and
  the output schema enumerate the valid units). `apply_audit.py` validates it
  and stores it on the row. A seat that lands on a row already holding a
  judgment (a second critical seat, a re-audit) binds the union of every
  declaration, and any undeclared judgment makes the row fail closed.
  Invalidation archives the declaration with the
  judgment, restoration brings it back, and the frozen-judgment digest binds
  it only when present, so legacy digests are unchanged.
- **The legacy whole-note premise check** in `invalidate_stale_audits.py` is
  skipped for v3 baselines, which already bind premise drift.
- **Preview** (`docs/audit/scripts/premise_change_impact.py`). For a working
  tree holding a proposed edit, it lists the live judgments the edit would
  re-open, using the same comparator, with the downstream cascade and an
  estimated re-audit cost.

### Expected decisions

- A judgment declaring `["minimal_axioms:record"]` survives an edit to the
  Lattice section, to the memo's history or relation commentary, or to the
  registry note. It re-opens on an edit to the Record section, to
  Qualification, to the node's registry paths, or to the clause map entry.
- A judgment with no declaration re-opens on any premise byte edit, as before.
- A judgment declaring `[]` that cites no premise node survives every premise
  edit. If it cites a premise node directly, it binds all of that node's units.
- Adding an unmapped `###` subsection under the axiom section makes every
  scoped fingerprint fail closed with an error until the clause map names it.
- A stored v2 baseline is compared under the exact v2 rule.

### Realistic counterexamples and their guards

- **Under-declaration.** An auditor omits a unit the argument used. An edit to
  that unit then leaves the audit standing. Guards: the prompt tells auditors
  to include a unit when unsure; a directly cited premise node is always bound;
  critical rows bind the union of two independent seats; runners that read the
  memo still bind its bytes; and the risk is limited to the content of one
  axiom section, which the same auditor already judged the whole derivation
  against.
- **Normative content outside a clause.** If commentary in the memo carried
  premise weight, an edit to it would not re-open scoped audits. Guards: the
  README says the axiom statements live only in the axiom sections;
  Qualification, the only other governing section, is shared; and the
  container guard rejects a new unmapped axiom subsection.

### Known limits (unchanged by this note)

- 694 of 5,383 non-meta rows have a runner that declares the memo as an input.
  Those rows still re-open on any memo byte edit through
  `science_changed:runner_or_declared_input`, because their evidence reads the
  file.
- The forensic no-go evidence manifest binds each cited authority's exact
  text, so a no-go row citing `minimal_axioms` still re-opens on any memo edit.
- `dependency_policy_epoch` is still repository-wide. A change to a governed
  policy source still re-opens every judgment.

## Defect 2: only Codex could land a clean audit

`FRESH_LOOK_REQUIREMENTS.md` recorded every Claude audit as `weak`, because
most notes are Claude-authored. That rule blocked a clean-room Claude seat as
well as the authoring session.

### Change

- `scripts/codex_audit_runner.py --auditor-backend claude` sends the rendered
  restricted prompt as the entire content of one stateless Claude API request
  (no system prompt, tools, history or file access), with structured output
  bound to the same verdict schema. It logs the request's SHA-256 and records
  `auditor_model` and `auditor_family` from the model that actually served the
  reply. Server-side refusal fallback (`fallbacks: "default"`) is enabled, so a
  declined request may be served by another Claude model; that model is what
  gets recorded.
- Independence for a Claude seat is `fresh_context`, or `cross_family` when the
  row's recorded `author_family` is a non-Claude family. A prior Codex verdict
  is not treated as evidence of authorship. Second seats follow the existing
  same-family rule, and critical rows still need two matching seats.
- Effort is by criticality: `medium` for leaf and medium rows, `high` for high,
  `xhigh` for critical. `--claude-effort` forces one level. The Codex xhigh
  rule is unchanged.
- Requests are synchronous, not batched: the forensic tier requires a trusted
  manifest issued within two hours of apply.
- Credit handling: keys come from the environment variables named by
  `--claude-key-env` (default `ANTHROPIC_AUDIT_KEY_BUSINESS`, then
  `ANTHROPIC_AUDIT_KEY_PERSONAL`), tried in order, so list the soonest-expiring
  credits first. A key that reports an exhausted credit balance, or fails
  authentication, is retired for the run. When every key is retired, or
  `--claude-max-spend-usd` is reached, the run stops cleanly and rows not
  reached stay queued for the next run. Keys are never logged; only the
  variable name is.

### Expected decisions

- A first-pass Claude seat on a Claude-authored or unattributed row records
  `fresh_context` and may land `audited_clean` (critical rows go to
  `awaiting_cross_confirmation`).
- Two Claude seats with matching tuples confirm a critical row. A Claude seat
  and a Codex seat may also pair.
- An interactive or agent Claude session, or any session with repository or
  authoring context, still records `weak`.

### Realistic counterexample and guard

- **Same-family blind spot.** A Claude seat may share the authoring model's
  systematic error where a different family would catch it. The owner accepted
  this. The guard that remains is that no seat sees the authoring context or
  prior verdicts. The Codex lane stays available for any row that warrants a
  cross-family check.

## Affected callers

`audit_science_fingerprint.py`, `apply_audit.py`, `invalidate_stale_audits.py`,
`restore_overaggressively_invalidated_audits.py`, `compute_audit_queue.py`,
`audit_lint.py`, `scripts/codex_audit_runner.py`, `AUDIT_AGENT_PROMPT_TEMPLATE.md`,
`FRESH_LOOK_REQUIREMENTS.md`, `skills/audit-loop/SKILL.md`, and the new
`premise_clause_map.json` and `premise_change_impact.py`. The Codex batch
drainer (`orchestrate_audit_batch.py`) is unchanged and remains Codex-only.

## Rollout

The governed policy sources changed, so `dependency_policy_epoch.json` moves to
`dependency_policy_v4`. With 0 live verdicts on `main`, that epoch move
re-opens nothing. `legacy_science_epoch_baseline.json` is deliberately not
refreshed. `SCIENCE_WORKFLOW.md` section 4 still lists formal audit as
deferred; starting audit runs is a separate owner decision.
