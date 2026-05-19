# Vocabulary Hygiene Design — Consolidated Review

**Date:** 2026-05-18
**Status:** consolidated feedback on
[VOCABULARY_HYGIENE_DESIGN.md](VOCABULARY_HYGIENE_DESIGN.md) before
the cleanup PR ships.
**Reviewers:** Codex (full-model adversarial review, high reasoning,
read-only sandbox, gathered via `codex exec`) + first-party deep
review (Claude). The review is on the **design**, not the framework
science.

> **Pivot note (post-review, second iteration):** an earlier response
> to MAJOR 7 attempted to *adopt standards conformance* (W3C
> recommendation-track lifecycle, GRADE two-axis evidence grading,
> IEEE 1044-2009 anomaly classification) by restructuring the audit
> schema to map onto those standards. That response was itself wrong
> and has been reverted. The standards in question were chosen for
> recognizable lifecycle shapes, not because they address the same
> problem: W3C standardizes web specifications, GRADE grades clinical
> evidence quality, IEEE 1044 classifies software anomalies. None
> were designed for theorem-audit verdicts in an AI-built physics
> repo.
>
> The corrected response — applied in
> [VOCABULARY_HYGIENE_DESIGN.md](VOCABULARY_HYGIENE_DESIGN.md) — is to
> **drop external-standards mapping entirely**. The vocabulary is
> physics-native (audit verdicts on derivations, `(A)`–`(G)`
> load-bearing step classes, the 7 repair classes, the 8-value
> `audit_status` enum) and AI-physics-native (catches for specific
> AI-generation failure modes: `audited_renaming`,
> `audited_decoration`, `audited_numerical_match`). It grew from
> doing AI-physics audits in this repo; the legitimacy of each term is
> grounded in the audit work that produced it, not in conformance to
> any external standard. The vocabulary is offered as a transferable
> **exemplar** with explicit scope tags (`core_process`,
> `audit_physics_process`, `repo_physics_policy`, `paper_voice`,
> `topic_local`), not as derivative of W3C/GRADE/IEEE/etc.
>
> The 8-value `audit_status` enum stays exactly as
> [audit/README.md](../audit/README.md) defines it. The genuine
> additions are orthogonal `prose_status` / `prose_corrections` fields
> (for vocab-drift separation), the canonical YAML source-of-truth,
> the `vocab_lint --fix` mechanism, and the `scope_tags` taxonomy.
> The original "downgrade `equivalent_to` to `inspired_by`" line of
> response is **also superseded**: even loose analogy is dropped,
> because pointing at adjacent standards misleads readers about the
> vocabulary's actual provenance.

This is a "measure twice, cut once" gate. The design will propagate
across ~2,500 markdown files via the cleanup PR; ratifying it now and
finding it wrong later is expensive.

## Methodology

1. Codex was given the design doc, the modified SKILL.md files, the
   existing audit scripts (`apply_audit.py`, `audit_lint.py`), the
   AI methods §5a, and a structured adversarial-review prompt
   instructing it to find logical / structural / feasibility /
   convention / coverage / migration / rot issues. Output: 14 issues
   in BLOCKER / MAJOR / MINOR / NICE-TO-HAVE tiers with file/line
   citations and concrete fixes. Reasoning effort: `xhigh`.
2. First-party deep review ran in parallel (Claude) using the same
   design with direct access to `apply_audit.py` schema constraints
   and the live repo violation counts.
3. The findings overlap substantially; this document de-duplicates
   and consolidates them in one priority-ordered list.

## Scope of violations (corrected scope: ≥130 emergent-suffix notes)

The earlier "84 hostile-audit-findings notes" number undercounted.
Live counts (Codex + first-party combined sweep over `docs/`):

| Pattern | Count |
|---|---:|
| `_HOSTILE_AUDIT_FINDINGS_NOTE_` | 84 |
| `_STRETCH_ATTEMPT_NOTE_` | 16 |
| `_DOWNSTREAM_FIX_NOTE_` | 9 |
| `_HOSTILE_REVIEW_*` | 7 |
| `_REVIEW_PACKET_` | 5 |
| `_TERMINAL_SYNTHESIS_META_` | 4 |
| `_SHARPENED_NOTE_` | 4 |
| `_FRAMING_FIX_NOTE_` | 1 |
| `_ROUTING_CORRECTION_NOTE_` | 1 |
| `_OBJECTION_CLOSURE_NOTE_` | 1 |
| `_CAMPAIGN_PROGRESS_SYNTHESIS_` | 1 |
| **Total emergent-suffix** | **≥132** |
| Bare-letter-number primary names (mixed; some legitimate) | 51 |
| `(legacy alias: X)` occurrences | 45 |
| Files with at least one `### F-A —`/`F-B`/`F-C` heading | 9 |
| `Status authority:` phrase occurrences (probably mostly legitimate) | 555 |
| `support tier`/`support-tier` occurrences (deprecated wording) | 60 |

Codex's local count gave 93 forbidden filenames; first-party broader
sweep across all `docs/` gave ≥132. The cleanup PR will need to
operate over the broader set.

## Consolidated issues

Each issue tagged with severity, summary, the specific concern, and
the recommended fix. Source: `[Codex]` for Codex-only findings,
`[FP]` for first-party-only, `[Both]` when independently raised by
both reviewers.

---

### BLOCKER 1: Ledger / note-hash / apply-audit integration is broken `[Both]`

The audit-loop SKILL.md says: run `vocab_lint --fix` on the source
note, write `prose_status` + `prose_corrections` on the audit row.

Two concrete problems:
1. `apply_audit.py` rejects any audit whose source note hash changed
   since ledger seeding (`apply_audit.py:610`). Running `--fix` on
   the source note immediately invalidates the audit before it can
   apply. The note_hash mechanism is from
   [FRESH_LOOK_REQUIREMENTS.md §6](../audit/FRESH_LOOK_REQUIREMENTS.md).
2. `apply_audit.py`'s `REQUIRED_FIELDS` is a closed set
   (`apply_audit.py:41`). `prose_status` and `prose_corrections` are
   not in it, and `ALLOWED_VERDICTS` doesn't include the new prose
   verdicts. Schema migration is required.

The SKILL.md changes shipped in this PR tell agents to do things
that the tooling rejects. As-shipped, the new audit-loop rule fails
at the validator.

**Fix (cleanup PR must do this BEFORE the sweep):** define the exact
order of operations. Options:
- Run `vocab_lint --fix` *before* `seed_audit_ledger.py` runs, so
  the seeded hash is the post-fix hash.
- Add a `pre_audit_prose_fix` envelope to `apply_audit.py` that
  carries `{old_hash, new_hash, prose_status, prose_corrections}`
  and atomically refreshes `note_hash`.
- Add `prose_status` / `prose_corrections` to `REQUIRED_FIELDS` and
  to the `audit_lint.py` schema check.

Either choice must update `apply_audit.py`, `audit_lint.py`, the
renderer, tests, and `AUDIT_AGENT_PROMPT_TEMPLATE.md` atomically in
the cleanup PR. Until then, the SKILL.md changes are
forward-looking and should be marked as such.

---

### BLOCKER 2: Rewrite rules are not safe for mechanical sweep `[Codex]`

The YAML sketch rewrites:
```
^### F-([A-Z]) — <title>   →   ### Finding \1: <title>
```
This is wrong on three counts:
1. The output is `Finding C`, not the proposed `Finding N` (numbered
   sequentially).
2. It misses inline cross-references like
   `hostile audit F-C finding (PR #1262)` in source notes (e.g.
   [ANOMALY_FORCES_TIME_THEOREM.md:92](../ANOMALY_FORCES_TIME_THEOREM.md))
   and downstream-fix notes that reference upstream `F-B` /
   `F-C` (e.g.
   [DT1_TIME_DIMENSION_PROOF_WALK_DOWNSTREAM_FIX_NOTE_2026-05-17.md:34](../DT1_TIME_DIMENSION_PROOF_WALK_DOWNSTREAM_FIX_NOTE_2026-05-17.md)).
3. Filename + heading + cross-reference + runner-assertion rewrites
   must happen *atomically* per file. Regex-only migration breaks
   cross-doc references.

**Fix:** two-phase migration:
- Phase 1: build a per-file mapping `{F-A → Finding 1: <title>,
  F-B → Finding 2: <title>, …}` with descriptive titles preserved
  from the original headings.
- Phase 2: rewrite headings, intra-doc references, markdown links,
  runner assertions, and source-note provenance citations together
  as a single atomic commit per file (or per cluster).
- Provenance preservation: allow a controlled historical footnote
  (`formerly F-C in PR #1262`) on each migrated finding so audit-prep
  history is preserved without keeping the F-letter taxonomy alive.

---

### BLOCKER 3: YAML schema is too small to regenerate current CV `[Codex]`

The design's YAML sketch has four families (lifecycle / grade /
defect / independence). The current CV has five status families plus:
- column rules per surface
- filename prefixes (frontier_*, mirror_*, …)
- archival vocabulary (`archive_unlanded/<tag>/`)
- evidence terms (protocol / witness / diagnostic / companion /
  closure)
- hyphenation rules
- paper-facing prose voice
- topic-local language (BMV, boundary-law, branch-mediated
  entanglement, historical retirement)

A four-family schema can't render this document faithfully. The
cleanup PR will either lose content during regeneration or
regenerate to a different (incomplete) CV.

**Fix:** expand the schema before any rendering. Required nodes:
`layers`, `term_families`, `field_enums`, `allowed_composites`,
`context_rules`, `filename_rules`, `rewrite_rules`,
`generated_sections`, `scope_tags`, `aliases`, `deprecations`,
`examples`. Require a renderer golden test (rendered output ≡
current CV after any compatibility migration).

---

### MAJOR 4: "No rot possibility" claim is overstated `[Both]`

Codex / FP both observed: rendered drift is only impossible if
generation is enforced. The design currently leaves renderer
placement, schema versioning, regeneration cadence, and CI gates as
open questions ([VOCABULARY_HYGIENE_DESIGN.md §"Open design
questions"](VOCABULARY_HYGIENE_DESIGN.md)).

Specific gaps:
- No `schema_version` field in the YAML schema.
- No deterministic renderer specified.
- No CI gate that fails if `render(YAML) ≠ on-disk CV.md`.
- No hash/source-stamp in the generated CV.md / KEY_TERMINOLOGY.md
  headers.

**Fix:** add `schema_version` to YAML; deterministic
`scripts/render_controlled_vocabulary.py`; generated-file headers
with the source YAML hash; CI gate that rebuilds and diffs.

---

### MAJOR 5: prose_status queuing is underspecified outside audit-loop `[Codex]`

The design records new vocab terms as `prose_status:
needs_human_vocab_decision` on audit ledger rows. But:
- review-loop touches branch files *before* any audit row exists.
- physics-loop's SKILL.md currently says terms are recorded "on any
  audit row they touch later"
  ([physics-loop/SKILL.md:95](../ai_methodology/skills/physics-loop/SKILL.md))
  — but the linked-later-row may never exist.

Queue entries are dropped on the floor.

**Fix:** create `docs/repo/vocab_extension_queue.json` (or similar)
as a *file-level* queue independent of audit rows. `vocab_lint`
appends unresolved terms with file path + line numbers + context;
audit rows reference queue entry IDs when they apply later.

---

### MAJOR 6: Physics/process boundary is not actually sharp `[Both]`

Both reviewers raised this. The design says "vocabulary is disjoint
from physics" but several boundary cases break the rule:

- `audited_renaming` / `audited_decoration` / `audited_numerical_match`
  are *physics-evaluation outcomes* — the auditor judges that the
  load-bearing step is a renaming / decoration / tuned match. That's
  a physics judgment, not a prose label.
- BMV / boundary-law / branch-mediated entanglement sections in CV
  are topic-local wording rules for physics surfaces. The design
  says they move out; the design itself doesn't define where.
- `(A)`-`(G)` derivation classes are physics judgments wearing
  process-vocab clothing.

**Fix:** introduce explicit scope tags on every term. Codex proposed:
- `core_process` — purely process labels (e.g. `unaudited`,
  `audit_in_progress`, `prose_status` values)
- `audit_physics_process` — verdicts on physics derivations that
  encode the AI-physics method (e.g. `audited_renaming`,
  `audited_decoration`, derivation classes A-G)
- `repo_physics_policy` — policy on physics primitives (axiom
  naming, A_min, Axiom*)
- `paper_voice` — prose voice rules
- `topic_local` — topic-specific wording (BMV, boundary-law)

Only `core_process` is transferable unchanged to other AI-physics
repos. The transferability claim in the AI Methods section should
narrow accordingly.

---

### MAJOR 7: Standard-convention claims are too strong `[Both]`

Both reviewers independently flagged: my "equivalent_to" mappings
are aspirational, not faithful. Specifically:

- **W3C** Candidate Recommendation is "technically complete document
  after wide review, used for implementation experience"; not "first
  clean audit awaiting confirmation". My mapping conflates two
  different process meanings.
- **GRADE** has two dimensions: *strength of recommendation*
  (Strong / Conditional) × *quality of evidence* (High / Moderate /
  Low / Very Low). My one-dimensional `retained` → "High" collapses
  this. The framework's `retained` is closer to "closed/ratified
  derivation" than "high-certainty evidence".
- **IEEE 1044** classifies software anomalies and data items, not
  theorem repair classes. The mapping is more "inspired by" than
  "adapted from".
- **Independence tiers** aren't from a single named standard; they
  are mostly novel (especially `cross_family` / `fresh_context`).

There is also a **MINOR typo** (issue 12): the design body
references "IEEE 1990" once and "IEEE 1044" elsewhere. They are
different standards (1990 = software engineering terminology
glossary; 1044 = anomaly classification). Pick one or remove.

**Fix:** replace every `equivalent_to:` field in the YAML schema
with `inspired_by:` / `analogous_to:` plus a sentence stating the
divergence. For GRADE specifically: either split `closure_status`
(novel) from `evidence_certainty` (GRADE-aligned), or drop the GRADE
reference entirely.

---

### MAJOR 8: Alias stripping is unsafe and internally inconsistent `[Codex]`

The design forbids `(legacy alias: X)` after cleanup
([KEY_TERMINOLOGY.md §Forbidden patterns](../KEY_TERMINOLOGY.md)).
But:
- CV.md §Science Naming Rules currently *permits* aliases for legacy
  shorthand on first-use definition.
- review-loop SKILL.md repeats that allowance.
- The proposed regex catches only the parenthetical form
  `(legacy alias: A1)`; it misses backticked variants and plurals
  (e.g. `legacy aliases A1/A2` in
  [AXIOM_FIRST_CPT_THEOREM_STRETCH_NOTE_2026-04-29.md:254](../AXIOM_FIRST_CPT_THEOREM_STRETCH_NOTE_2026-04-29.md)).

The design is forbidding what CV.md still permits.

**Fix:** decide the policy first.
- If aliases are forbidden on live surfaces: define exclusions for
  historical / raw / `docs/work_history/` / `archive_unlanded/`
  paths. Update CV.md and review-loop SKILL.md to match. Use a
  contextual alias map rather than blanket regex.
- If aliases are permitted in defined contexts: keep them, with a
  rule that aliases must be paired with the canonical name on
  first use. This is closer to what CV.md actually says today.

---

### MAJOR 9: Coverage narrower than repo's agent surface `[Both]`

Both reviewers flagged the coverage gap. The design integrates
`vocab_lint --fix` into audit-loop / review-loop / physics-loop.
But drift enters from:
- Direct git commits (humans editing in IDE)
- GitHub UI edits
- `AUTOPILOT_PROTOCOL.md` science workers (a separate loop)
- `AUTOPILOT_JANITOR_PROTOCOL.md`
- Cron jobs (audit nightly refresh)
- Other skills (`ai-physics-lane-builder`,
  `methodology-paper-synthesizer`, `no-go-discipline`,
  `physics-claim-reviewer`, `reviewer-backpressure-integrator`)
- The audit ledger JSON itself (`audit_ledger.json`)
- Python scripts that emit vocabulary strings

**Fix:** add a **CI gate** that runs `vocab_lint --report-only`
against defined path classes on every PR. Plus a pre-commit hook
for changed files. Plus extend the lint to scan JSON / YAML /
Python string literals where vocabulary fields are serialized
(claim_type, audit_status, etc. in the ledger and in scripts).

---

### MAJOR 10: Cleanup PR is described as "large and mechanical"; parts require judgment `[Both]`

The cleanup PR scope in the design says "intentionally large and
mechanical." But:
- F-letter → descriptive-title renames require choosing titles
  (BLOCKER 2).
- Cross-doc reference repair requires per-file judgment.
- Hostile-audit-findings notes encode real audit findings that must
  be preserved (corrected routings, runner verifications, stale
  tier descriptors). A naive sweep can lose semantic content.

**Fix:** split cleanup into at least two PRs:
- **Cleanup-1 (schema + tooling + generated docs):** YAML schema,
  `vocab_lint.py`, renderer, schema migration for `prose_status`,
  ledger backfill mode, regenerated CV.md + KEY_TERMINOLOGY.md.
  Mechanical, low-risk.
- **Cleanup-2 (migration sweep):** the per-file F-letter → Finding-N
  migration, filename renames, cross-doc reference updates,
  content-preservation tests, link-checker. Slower, careful,
  reviewable per cluster.

---

### MAJOR 11: prose_status backfill as `clean` is misleading `[Codex]`

The design migration scope says: backfill existing audit ledger
rows as `prose_status: clean`. But:
- Pre-cleanup rows were never linted under the new rules.
- They may have unresolved drift that the new lint *would* catch.
- Marking them `clean` falsifies the prose-status signal.

**Fix:** use `prose_status: not_evaluated_pre_vocab_lint` for
backfill, OR run the real lint over every existing source note and
backfill from that report.

---

### MAJOR 12: Bare-letter-number rule needs nuance `[FP]`

51 docs/ files start with bare letter-number prefixes:
- `S3_*` (24) — refer to S³ topology; legitimate physics
- `A3_*` (17) — refer to the rolled-back A3 axiom wave; mixed
- `Z3_*` (2), `U0_*` (2), `Z2_*` (1), `S1_*` (1), `I3_*` (1),
  `C3_*` (2), `U1_*` (1)

The current CV.md §Science Naming Rules forbids "bare letter-number
codes" as primary names, but several of these are *domain-correct*
mathematical-object names (S³, U(1), Z_3, C_3 are standard).

**Fix:** the rule should distinguish two cases:
- *Abbreviations of established mathematical objects* (S³, U(1),
  Z_3, C_3, etc.) — allowed as primary names because they are the
  canonical mathematical name.
- *Code-like primary names without a domain-explicit referent*
  (`A1`, `G1`, `R3` without explicit Axiom 1, etc. in scope) —
  forbidden as before.

Update CV.md §Science Naming Rules with this distinction.

---

### MINOR 13: IEEE 1990 vs IEEE 1044 typo `[Codex]`

`VOCABULARY_HYGIENE_DESIGN.md` §Principles mentions "IEEE 1990
review vocabulary"; the families table says "IEEE 1044". Different
standards. Pick one or remove.

**Fix:** delete "IEEE 1990" or replace with a citation that
matches. IEEE 1044-2009 is the closer match for the defect-class
intent.

---

### MINOR 14: "Silent" auto-correction is wrong operator language `[Codex]`

The design says routine drift is "rewritten silently". But the
design *also* says corrections are logged in `prose_corrections`,
and audit ledger rows reflect them. They are automatic, not silent.

**Fix:** rewrite all "silent" / "silently" references in the design
and SKILL.md updates to "automatic, logged" (or
"auto-corrected; logged in prose_corrections").

---

### NICE-TO-HAVE 15: Transferability claims need preconditions `[Codex]`

The AI Methods §5a claims the mechanism transfers to "any AI-built
research repo above some scale". It really transfers only to repos
with:
- A structured claim ledger (audit ledger JSON or equivalent)
- Controlled / generated docs (renderer pattern)
- CI gates that enforce regeneration
- Agents that respect pre-commit hooks
- A central source-of-truth for vocab (YAML or equivalent)

**Fix:** state these preconditions explicitly in §5a. Repos
without them get a different (less mechanical) version of the same
discipline.

---

## Top priorities

Codex's top-5 + first-party's top concerns, merged in priority order:

1. **Fix the ledger / hash / apply_audit integration before any cleanup
   sweep** (BLOCKER 1). The current SKILL.md tells agents to do
   things the tooling rejects. Either revise the SKILL.md to be
   forward-looking ("once cleanup-1 lands…") or block cleanup-1 from
   landing until the schema migration is part of it.
2. **Replace regex-only migration with a link-aware, heading-aware
   plan with tests** (BLOCKER 2). Build per-file `{F-letter → Finding
   N: <title>}` mappings first; then atomic per-file rewrites.
3. **Expand the YAML schema so it can actually render the current
   CV** (BLOCKER 3). Four families is insufficient. Add: `layers`,
   `term_families`, `field_enums`, `allowed_composites`,
   `context_rules`, `filename_rules`, `rewrite_rules`,
   `generated_sections`, `scope_tags`, `aliases`, `deprecations`,
   `examples`.
4. **Deterministic renderer + CI diff gate** (MAJOR 4). Without it,
   the "no rot" claim is aspirational.
5. **Drop external-standards mapping entirely** (MAJOR 7; second
   iteration). The earlier "downgrade to `inspired_by`" response and
   the subsequent "adopt conformance" response are both superseded.
   The vocabulary is physics-native + AI-physics-native; the
   adjacent standards (W3C web specs, GRADE clinical evidence
   grading, IEEE 1044 software anomalies) address different problems
   and pointing at them misleads readers about the vocabulary's
   provenance. Frame each term by what it does in this repo, with a
   `scope_tag` identifying transferability. (This also removes the
   IEEE 1990 vs 1044 typo issue by removing the IEEE references.)
6. **Split cleanup PR into Cleanup-1 (schema/tooling) and Cleanup-2
   (migration sweep)** (MAJOR 10). The sweep needs the tooling
   landed first.
7. **Define scope tags** (MAJOR 6). `core_process` vs
   `audit_physics_process` vs `repo_physics_policy` vs `paper_voice`
   vs `topic_local`. Narrow the transferability claim to
   `core_process` only.
8. **CI gate + queue file for unresolved terms** (MAJOR 5, 9).
   `docs/repo/vocab_extension_queue.json` independent of audit rows;
   `vocab_lint --report-only` as a CI gate over defined path classes.

The remaining MAJORs / MINORs are smaller-blast-radius fixes that
fold into the Cleanup-1 PR naturally.

## Recommended PR sequencing

| PR | Contents | Blocked by |
|---|---|---|
| This PR (current, #1529) | Design doc + KEY_TERMINOLOGY + auto-correct SKILL.md updates + AI Methods §5a + **this review document** | Address the in-design fixes below before merge: standards language downgrade, IEEE typo, "silent" → "automatic, logged", and add a clear "this is forward-looking; tooling lands in Cleanup-1" marker to the SKILL.md changes |
| Cleanup-1 | YAML schema (expanded per BLOCKER 3), `vocab_lint.py`, renderer, `prose_status` field migration in `apply_audit.py` + `audit_lint.py`, regenerated CV.md + KEY_TERMINOLOGY.md, scope tags, queue file, CI gate, content-preservation tests | This PR landing |
| Cleanup-2 | Per-file F-letter → Finding migration sweep with link-checker, filename renames, alias resolution, the actual lint --fix over the repo | Cleanup-1 landing + a green CI run with the new tooling |

## In-this-PR fixes (small, can ship without blocking)

Before merging #1529, apply:
1. Downgrade `equivalent_to` → `inspired_by` throughout
   VOCABULARY_HYGIENE_DESIGN.md.
2. Drop IEEE 1990 from the principles list; keep IEEE 1044 with
   "inspired by" framing.
3. Replace "silently" / "silent" with "automatic, logged" in the
   design and all three SKILL.md changes.
4. Mark the SKILL.md changes as **forward-looking** with explicit
   "Effective once Cleanup-1 lands; before then, follow the existing
   verdict rules."
5. Add the transferability preconditions to AI_METHODOLOGY_NOTE §5a.
6. Add the bare-letter-number nuance to CV.md §Science Naming Rules.
7. Resolve the four open design questions at the bottom of
   VOCABULARY_HYGIENE_DESIGN.md or mark them MUST-RESOLVE-FOR-CLEANUP-1.

Everything else defers to Cleanup-1 / Cleanup-2.

## What we got right

- Vocabulary disjoint from physics (with the scope-tag refinement
  from MAJOR 6).
- Auto-correct as mechanism over discipline.
- Physics-verdict vs prose-verdict separation (with the queueing
  fix from MAJOR 5).
- Agent pacing principle.
- Forward-looking design rather than retroactive enforcement.
- Identifying the failure mode and naming it as transferable.

The direction is right; the design needs the refinements above
before the cleanup PRs can safely propagate it across the repo.
