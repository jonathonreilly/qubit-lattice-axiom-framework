# Vocabulary Hygiene Design

> **Key terms used in this doc** are indexed A-Z at [docs/KEY_TERMINOLOGY.md](../KEY_TERMINOLOGY.md); each row points to the canonical source-of-truth doc.

**Status:** design proposal for vocabulary governance in this repo and
as a reference pattern for AI-built physics repos. Companion to
[KEY_TERMINOLOGY.md](../KEY_TERMINOLOGY.md) and
[CONTROLLED_VOCABULARY.md](CONTROLLED_VOCABULARY.md). The implementation
work lives in a separate cleanup PR (see "Migration scope" below).

**Date:** 2026-05-18

## Goal

Vocabulary discipline for large AI-built research repos at agent
pacing. Two products:

1. Repo-canonical process vocabulary that survives drift across
   thousands of AI-authored docs.
2. Reference pattern other AI-physics projects can adopt.

The framework science (`Cl(3)` on `Z³`) is the case study; the
*process* — including this vocabulary system — is the primary
deliverable.

## Principles

1. **Vocabulary is disjoint from physics.** Physics primitives (`Cl(3)`,
   `Z³`, `A_min`, `Axiom 1`, `Axiom 2`, `g_bare`, `u_0`, `M_Pl`, etc.)
   are *not* vocabulary terms. They live in
   [MINIMAL_AXIOMS_2026-05-03.md](../MINIMAL_AXIOMS_2026-05-03.md) and
   per-claim notes. Vocabulary governs *process labels only*: status,
   audit fields, repair classes, evidence terms, prose voice.
2. **No rot possibility.** The canonical vocabulary is a
   machine-readable structured-data file (YAML). Rendered docs
   (CONTROLLED_VOCABULARY.md, KEY_TERMINOLOGY.md) are *products*
   regenerated from the YAML, not authored alongside it. Lint
   mechanically enforces; manual edits to rendered docs are not
   permitted.
3. **Conform to established standards where the domain matches;
   extend explicitly where AI-physics genuinely needs it.** The
   schema below is engineered for standards conformance, not
   nodding-toward-standards:
   - **Lifecycle** maps cleanly onto W3C recommendation-track values
     (`unaudited` ≡ Working Draft, `audit_in_progress` ≡ Candidate
     Recommendation, `audited_clean` ≡ Recommendation,
     `audited_retired` ≡ Retired with cause). AI-specific failure
     modes (renaming / decoration / numerical_match) are recorded in
     a separate `failure_mode` field, not by adding new lifecycle
     states.
   - **Grade** decomposes into the GRADE two-axis structure
     (`closure_status` × `chain_certainty`) rather than collapsing
     both into a one-dimensional enum. The conventional shorthand
     (`retained`, `retained_bounded`, `retained_pending_chain`, …)
     stays as labels for specific cells in the grid; the underlying
     model is GRADE-compatible.
   - **Defect classification** uses IEEE 1044-2009 anomaly
     classification multi-axes (`defect_type` × `defect_class` ×
     `severity`); our 7 existing categories map into them rather than
     replacing them. `compute_required` is correctly excluded as
     "not a defect, deferred verification".
   - **Independence tiers** are mostly novel; no widely-adopted
     standard for model-family-level reviewer-independence. These are
     explicitly tagged as AI-physics extensions.

   Every term that is *not* a standards conformance is tagged in the
   YAML with `ai_extension: true` and an `ai_extension_rationale`
   field. The transferability claim in the AI Methods section
   narrows correspondingly: the conformant parts transfer
   unchanged; the AI-physics extensions transfer only to repos
   facing the same generation-failure modes. See
   [VOCABULARY_HYGIENE_REVIEW_2026-05-18.md](VOCABULARY_HYGIENE_REVIEW_2026-05-18.md)
   §MAJOR 7 for the design discussion that drove this choice.
4. **Auto-correct, don't hard-fail.** audit-loop, review-loop, and
   physics-loop run `vocab_lint --fix` on touched files as a mechanical
   pre-commit step. Routine drift is rewritten **automatically, with
   each rewrite recorded in `prose_corrections`** for the audit trail
   (not silent — automatic and logged). Truly ambiguous cases surface
   as a *separate* `prose_status` field, never conflated with the
   physics `audit_status`.
5. **Agent pacing.** Routine vocabulary compliance is mechanical, not
   PR-bound. Only vocabulary *extensions* — genuinely new terms
   entering the canonical YAML — require a PR against the YAML.
   Existing-term drift is auto-corrected inline at agent speed.
6. **Physics verdict ≠ prose verdict.** Audit verdicts on physics are
   never set or blocked by vocabulary drift. A clean derivation with
   non-canonical prose lands as `(audit_status: audited_clean,
   prose_status: auto_corrected)`. The two concerns are recorded in
   separate fields and reviewed by separate mechanisms.

## The four vocabulary families

Each family conforms to an established standard where the domain
matches, with explicitly-tagged AI-physics extensions for the
generation failure modes the standards do not cover. The conformant
parts use standards-aligned values; the extensions are recorded as
separate orthogonal fields, not by inflating the standards enums.

### Lifecycle: W3C recommendation-track conformant

| `audit_status` value | Equivalent W3C value | Meaning |
|---|---|---|
| `unaudited` | Working Draft | Not yet audited |
| `audit_in_progress` | Candidate Recommendation | First clean audit; awaiting cross-confirmation |
| `audited_clean` | Recommendation | Endorsed; load-bearing step closes |
| `audited_retired` | Retired (with cause) | Terminal non-clean; specific cause in `failure_mode` |

**AI-physics extension** (orthogonal `failure_mode` field, only set
when `audit_status = audited_retired`): `null` (generic),
`renaming` (load-bearing step is class E/F), `decoration` (exact
algebraic corollary, no new content), `numerical_match` (tuned-input
dependence). These do not pollute the lifecycle enum; they record
*why* the row was retired.

**Dependency status** (orthogonal `dependency_status` field, graph-
state independent of lifecycle): `clean` (all deps retained),
`pending_chain` (deps not yet retained-grade), `failed_dep` (a dep
is `audited_retired`). The historical `audited_conditional` enum
value is replaced by `(audit_status: audited_clean,
dependency_status: pending_chain)` — physics-clean with deps
pending.

### Grade: GRADE two-axis conformant

GRADE has two dimensions: *recommendation strength* (Strong /
Conditional) × *evidence certainty* (High / Moderate / Low / Very
Low). We adopt the same two-axis structure with framework-specific
labels:

| Field | Values | GRADE-equivalent dimension |
|---|---|---|
| `closure_status` | `closed`, `bounded_closure`, `negative_closure`, `open` | Recommendation strength + direction |
| `chain_certainty` | `complete`, `pending_chain`, `failed_chain` | Evidence certainty (over the dependency graph) |

Conventional publication-facing labels (`retained`,
`retained_bounded`, `retained_no_go`, `retained_pending_chain`,
`open_gate`, ...) stay as shorthand for specific cells in the
2-axis grid, but they are derived from the underlying axes, not the
source of truth.

**AI-physics extension:** `chain_certainty` interprets GRADE
"evidence certainty" as dependency-graph completion rather than
empirical-evidence accumulation. The two-axis structure is
GRADE-conformant; the specific interpretation is the extension.

### Defect: IEEE 1044-2009 conformant

IEEE 1044-2009 anomaly classification uses multi-axis fields. We
adopt the same shape:

| IEEE 1044 axis | Values | Notes |
|---|---|---|
| `defect_type` | data / logic / interface / construction / documentation | Standard IEEE 1044 type taxonomy |
| `defect_class` | failure / error / problem | Standard IEEE 1044 class taxonomy |
| `severity` | critical / major / minor / negligible | Standard IEEE 1044 severity scale |

Our 7 historical repair classes map into the IEEE 1044 axes:

| Historical repair class | `defect_type` | `defect_class` | `severity` |
|---|---|---|---|
| `missing_dependency_edge` | `interface` | `error` | `major` |
| `dependency_not_retained` | `data` | `error` | `major` |
| `missing_bridge_theorem` | `logic` | `failure` | `critical` |
| `scope_too_broad` | `logic` | `error` | `minor` |
| `runner_artifact_issue` | `construction` | `problem` | `minor` |
| `compute_required` | n/a (not a defect) | `problem` | n/a (deferred verification) |
| `other` | `documentation` | `problem` | (must state why) |

The historical class names remain as derived labels; the underlying
ledger fields are IEEE 1044-conformant.

### Independence: novel AI-physics extension

No widely-adopted standard exists for multi-tier reviewer
independence at model-family granularity. The five values (`weak`,
`fresh_context`, `cross_family`, `strong`, `external`) are
explicitly novel.

| `independence` value | Meaning | AI-physics extension? |
|---|---|---|
| `weak` | Same model family, no clean-room | yes (model-family concept) |
| `fresh_context` | Same model family, restricted-context distinct session | yes |
| `cross_family` | Different model family from author | yes (model-family concept) |
| `strong` | Human reviewer with no prior involvement | no (standard peer review) |
| `external` | Off-repo reviewer | no (standard external review) |

The two non-extension values (`strong` and `external`) correspond
to standard peer-review independence tiers.

---

The full per-term inventory with definitions, equivalent-standard
pointers (where applicable), and AI-extension flags lives in
`docs/repo/controlled_vocabulary.yaml` (Cleanup-1 creates it).

## Out of scope for the vocabulary

These are **physics**, not vocabulary, and never appear in
CONTROLLED_VOCABULARY.md or KEY_TERMINOLOGY.md:

- **Framework primitives.** `Cl(3)`, `Z³`, `A_min`, `Axiom 1`,
  `Axiom 2`, `Axiom*`. Canonical home:
  [MINIMAL_AXIOMS_2026-05-03.md](../MINIMAL_AXIOMS_2026-05-03.md);
  policy:
  [AXIOM_MINIMALITY_POLICY.md](../audit/AXIOM_MINIMALITY_POLICY.md).
- **Physics quantities.** `g_bare`, `u_0`, `M_Pl`, `R_conn`, `alpha_s`,
  `v`, etc. Canonical home:
  [ASSUMPTION_DERIVATION_LEDGER.md](../ASSUMPTION_DERIVATION_LEDGER.md)
  for per-quantity status; per-claim notes for theorem-specific names.
- **Specific theorem / lane / observable names.** Live in their
  source notes; never in the vocabulary docs.
- **Topic-specific wording conventions** (BMV / boundary-law /
  branch-mediated-entanglement). These are *physics prose
  conventions*, not process vocabulary. Cleanup PR moves them out of
  CONTROLLED_VOCABULARY.md into topic-scoped notes.

The cleanup PR will strip any physics primitives currently embedded in
CONTROLLED_VOCABULARY.md and KEY_TERMINOLOGY.md.

## Machine-readable canonical source

A new file, `docs/repo/controlled_vocabulary.yaml`, is created by the
cleanup PR as the single source of truth. Schema:

```yaml
schema_version: 1

# Fields are the canonical source of truth. Conventional shorthand labels
# (retained / retained_bounded / etc.) are derived from cells in the
# field-value grid; they are not the source.

field_enums:

  # ---- Lifecycle (W3C-conformant) ----
  audit_status:
    description: "Where the row is in its review journey."
    standard_basis: "W3C recommendation-track lifecycle (https://www.w3.org/2021/Process-20211102/#rec-track)."
    values:
      unaudited:
        definition: "Row has not been audited yet."
        equivalent_to: "W3C Working Draft"
        ai_extension: false
      audit_in_progress:
        definition: "First clean audit recorded; awaiting cross-confirmation per FRESH_LOOK_REQUIREMENTS §4."
        equivalent_to: "W3C Candidate Recommendation"
        ai_extension: false
      audited_clean:
        definition: "Derivation closes from cited inputs with no hidden premise; ratified."
        equivalent_to: "W3C Recommendation"
        ai_extension: false
      audited_retired:
        definition: "Terminal non-clean verdict. Specific cause recorded in `failure_mode`."
        equivalent_to: "W3C Retired (with cause)"
        ai_extension: false

  # ---- Failure mode (AI-physics extension) ----
  # Orthogonal to audit_status. Only meaningful when audit_status = audited_retired.
  failure_mode:
    description: "Why a retired row was retired. AI-physics-specific subtypes."
    standard_basis: "No standard equivalent; AI-generation failure modes."
    ai_extension: true
    values:
      generic:
        definition: "Chain does not close on its own terms; no AI-specific subtype applies."
        ai_extension: false
      renaming:
        definition: "Load-bearing step is a definition (class E) or symbol-identity assertion (class F)."
        ai_extension: true
        ai_extension_rationale: "Definition-as-derivation is a known AI generation failure mode."
      decoration:
        definition: "Exact algebraic corollary of a parent claim with no new comparator / compression / structural integer."
        ai_extension: true
        ai_extension_rationale: "Catches mass-produced algebraic consequences of one upstream choice."
      numerical_match:
        definition: "Result depends on a tuned/calibrated input rather than a structural theorem (load-bearing step class G)."
        ai_extension: true
        ai_extension_rationale: "Catches tuned-input matches presented as derivations."

  # ---- Dependency status (orthogonal to lifecycle) ----
  dependency_status:
    description: "Pure graph-state of the dependency chain. Independent of audit_status."
    standard_basis: "Dependency-graph propagation; novel."
    ai_extension: true
    ai_extension_rationale: "Chain-of-trust state at AI-scale dependency graphs."
    values:
      clean:
        definition: "All direct dependencies are retained-grade."
        ai_extension: false  # graph state itself is standard
      pending_chain:
        definition: "Direct dependencies exist but are not yet retained-grade. Replaces historical `audited_conditional` enum value."
        ai_extension: true
      failed_dep:
        definition: "A direct dependency is `audit_status: audited_retired`."
        ai_extension: false

  # ---- Closure status (GRADE-conformant, first axis) ----
  closure_status:
    description: "Strength + direction of the closed claim."
    standard_basis: "GRADE recommendation strength × direction (https://www.gradeworkinggroup.org/)."
    values:
      closed:
        definition: "Positive theorem: full closure from retained inputs."
        equivalent_to: "GRADE Strong (positive direction)"
        ai_extension: false
      bounded_closure:
        definition: "Theorem with named bounds / admissions."
        equivalent_to: "GRADE Conditional (positive direction)"
        ai_extension: false
      negative_closure:
        definition: "Negative-result theorem (no-go)."
        equivalent_to: "GRADE Strong (negative direction)"
        ai_extension: false
      open:
        definition: "Not closed; open gate."
        equivalent_to: "GRADE: no recommendation."
        ai_extension: false

  # ---- Chain certainty (GRADE-conformant, second axis) ----
  chain_certainty:
    description: "Evidence certainty (GRADE second axis), interpreted as dependency-chain completion."
    standard_basis: "GRADE evidence certainty (high/moderate/low/very low)."
    ai_extension: true
    ai_extension_rationale: "We interpret 'evidence certainty' as dependency-graph completion rather than empirical-evidence accumulation. The two-axis structure is GRADE-conformant; the interpretation is the extension."
    values:
      complete:
        definition: "Entire dependency chain is retained-grade."
        equivalent_to: "GRADE High evidence certainty"
        ai_extension: false
      pending_chain:
        definition: "Some upstream dependency is not yet retained."
        equivalent_to: "GRADE Moderate/Low evidence certainty"
        ai_extension: false
      failed_chain:
        definition: "An upstream dependency is retired with cause."
        equivalent_to: "GRADE Very Low evidence certainty"
        ai_extension: false

  # ---- Defect taxonomy (IEEE 1044-2009 conformant) ----
  defect_type:
    description: "IEEE 1044-2009 defect type."
    standard_basis: "IEEE 1044-2009 (https://standards.ieee.org/ieee/1044/4607/)."
    values:
      data: { definition: "Data-related defect.", ai_extension: false }
      logic: { definition: "Logic/algorithmic defect.", ai_extension: false }
      interface: { definition: "Interface/integration defect.", ai_extension: false }
      construction: { definition: "Build/construction defect.", ai_extension: false }
      documentation: { definition: "Documentation defect.", ai_extension: false }

  defect_class:
    description: "IEEE 1044-2009 defect class."
    standard_basis: "IEEE 1044-2009."
    values:
      failure: { definition: "Service-blocking issue.", ai_extension: false }
      error:   { definition: "Recoverable mistake.",     ai_extension: false }
      problem: { definition: "Non-defect concern (e.g. deferred verification).", ai_extension: false }

  severity:
    description: "IEEE 1044-2009 severity."
    standard_basis: "IEEE 1044-2009."
    values:
      critical: { definition: "Blocks closure.", ai_extension: false }
      major:    { definition: "Significant impact.", ai_extension: false }
      minor:    { definition: "Local scope.",         ai_extension: false }
      negligible: { definition: "Cosmetic.",          ai_extension: false }

  # ---- Independence (mostly novel) ----
  independence:
    description: "Adversarial-review independence tier between auditor and author."
    standard_basis: "Partial: standard peer review (strong, external). Model-family tiers are novel."
    values:
      weak:
        definition: "Same model family, no clean-room. Not eligible to land audited_clean."
        ai_extension: true
        ai_extension_rationale: "Model-family is an AI-physics concept."
      fresh_context:
        definition: "Same model family, different auditor/session identity, restricted-input audit."
        ai_extension: true
        ai_extension_rationale: "Same-family clean-room review for context-poisoning detection."
      cross_family:
        definition: "Different model family from author."
        ai_extension: true
        ai_extension_rationale: "Model-family is an AI-physics concept."
      strong:
        definition: "Human reviewer with no prior involvement in the note."
        equivalent_to: "Standard independent peer review"
        ai_extension: false
      external:
        definition: "Off-repo reviewer with no project context."
        equivalent_to: "External peer review / venue review"
        ai_extension: false

  # ---- Prose status (Vocabulary-discipline separation) ----
  prose_status:
    description: "Vocabulary compliance of the source note. Separate from audit_status (physics)."
    standard_basis: "Novel; required by physics-versus-prose separation principle."
    ai_extension: true
    values:
      clean: { definition: "No vocabulary drift detected.", ai_extension: false }
      auto_corrected: { definition: "Routine drift mechanically rewritten by vocab_lint --fix; rewrites logged in prose_corrections.", ai_extension: false }
      needs_human_vocab_decision: { definition: "Genuinely new term that vocab_lint cannot mechanically rewrite; queued for vocab-extension review.", ai_extension: false }
      not_evaluated_pre_vocab_lint: { definition: "Pre-Cleanup-1 row never linted under the new rules. Used during backfill only.", ai_extension: false }
      queue_backpressure_exceeded: { definition: "Vocab-extension review queue is >50 entries deep; new unresolved terms emit this until queue is processed.", ai_extension: false }

# ---- Derived labels ----
# Publication-facing shorthand strings derived from the (closure_status,
# chain_certainty) grid. These are display labels, not source-of-truth.
derived_labels:
  retained:                 {closure: closed,          certainty: complete}
  retained_bounded:         {closure: bounded_closure, certainty: complete}
  retained_no_go:           {closure: negative_closure, certainty: complete}
  retained_pending_chain:   {closure: closed,          certainty: pending_chain}
  retained_bounded_pending: {closure: bounded_closure, certainty: pending_chain}
  open_gate:                {closure: open,            certainty: complete}
  audited_failed_chain:     {any closure,              certainty: failed_chain}

# ---- Aliases (deprecated → canonical mapping) ----
# Historical names that map into the new schema. Used by vocab_lint to
# auto-correct from old enum to new fields.
aliases:
  audited_renaming:
    canonical: "(audit_status: audited_retired, failure_mode: renaming)"
  audited_decoration:
    canonical: "(audit_status: audited_retired, failure_mode: decoration)"
  audited_numerical_match:
    canonical: "(audit_status: audited_retired, failure_mode: numerical_match)"
  audited_conditional:
    canonical: "(audit_status: audited_clean, dependency_status: pending_chain)"
  audited_failed:
    canonical: "(audit_status: audited_retired, failure_mode: generic)"
  # Historical repair classes → IEEE 1044 multi-axis
  missing_dependency_edge: { canonical: "(defect_type: interface, defect_class: error, severity: major)" }
  dependency_not_retained: { canonical: "(defect_type: data,      defect_class: error, severity: major)" }
  missing_bridge_theorem:  { canonical: "(defect_type: logic,     defect_class: failure, severity: critical)" }
  scope_too_broad:         { canonical: "(defect_type: logic,     defect_class: error, severity: minor)" }
  runner_artifact_issue:   { canonical: "(defect_type: construction, defect_class: problem, severity: minor)" }
  compute_required:        { canonical: "(defect_class: problem)" }   # not a defect
  other:                   { canonical: "(defect_type: documentation, defect_class: problem)" }

# ---- Rewrite rules (used by vocab_lint --fix) ----
rewrite_rules:
  - id: legacy_alias_strip
    pattern: '\s*\(legacy alias:\s*[A-Z][0-9A-Z]*\)'
    replacement: ''
    rationale: 'Aliasing creates rot. Use the canonical name only.'
    excluded_paths: ['docs/work_history/**', 'archive_unlanded/**']
  - id: hostile_audit_findings_suffix
    pattern: '_HOSTILE_AUDIT_FINDINGS_NOTE_(\d{4}-\d{2}-\d{2})\.md'
    replacement: '_NOTE_$1.md'
    rationale: 'New filename suffixes for meta notes are forbidden; use plain _NOTE_<date>.md.'
    requires_link_aware_rewrite: true   # cross-doc references must be updated atomically
  - id: downstream_fix_suffix
    pattern: '_DOWNSTREAM_FIX_NOTE_(\d{4}-\d{2}-\d{2})\.md'
    replacement: '_NOTE_$1.md'
    rationale: 'Same as above.'
    requires_link_aware_rewrite: true
  - id: f_letter_heading
    # NOTE: this rule is NOT a one-shot regex. F-letter migration requires
    # per-file mapping {F-A: <title>, F-B: <title>, ...} → {Finding 1: <title>, ...}
    # with link-aware cross-doc reference updates. See VOCABULARY_HYGIENE_REVIEW_2026-05-18.md BLOCKER 2.
    migration_strategy: per_file_mapping_with_link_check
    rationale: 'F-letter codes are forbidden; descriptive numbered findings replace them.'

filename_rules:
  meta_note_suffix: '_NOTE_<YYYY-MM-DD>.md'
  forbidden_suffixes:
    - '_HOSTILE_AUDIT_FINDINGS_NOTE_'
    - '_DOWNSTREAM_FIX_NOTE_'
    - '_FIX_RECORD_'
    - '_FINDINGS_MEMO_'
    - '_ADDENDUM_'
    - '_SURGICAL_REPAIR_'
    - '_AUDIT_BRIEF_'
    - '_STRETCH_ATTEMPT_NOTE_'  # 16 instances in repo
    - '_REVIEW_PACKET_'         # 5 instances
    - '_TERMINAL_SYNTHESIS_META_'  # 4 instances
    - '_SHARPENED_NOTE_'        # 4 instances
    - '_HOSTILE_REVIEW_'        # 7 instances

# ---- Scope tags (per MAJOR 6) ----
scope_tags:
  core_process:
    description: "Pure process labels transferable unchanged to other AI-built repos."
    examples: ['audit_status', 'prose_status', 'dependency_status']
  audit_physics_process:
    description: "Verdicts on physics derivations that encode the AI-physics method."
    examples: ['failure_mode', 'load_bearing_step_class', 'closure_status']
  repo_physics_policy:
    description: "Policy on physics primitives; this repo only."
    examples: ['axiom naming policy', 'A_min definition', 'Axiom* prohibition']
    governing_doc: 'docs/audit/AXIOM_MINIMALITY_POLICY.md'
  paper_voice:
    description: "Paper-facing prose voice rules."
    governing_doc: 'docs/WRITING_VOICE_GUIDE_2026-04-25.md'
  topic_local:
    description: "Topic-specific physics wording (BMV, boundary-law, etc.)."
    home: 'per-topic notes; not in CV.md after Cleanup-2'

scope:
  in_scope:
    - 'Process labels (audit_status, failure_mode, dependency_status, closure_status, chain_certainty, defect_*, independence, prose_status)'
    - 'Repair-class mappings'
    - 'Filename conventions'
  out_of_scope:
    - 'Framework primitives (live in MINIMAL_AXIOMS_2026-05-03.md)'
    - 'Physics quantities (live in ASSUMPTION_DERIVATION_LEDGER / per-claim notes)'
    - 'Topic-specific physics wording (lives in topic notes; not vocabulary)'

# ---- Generated sections (renderer-facing) ----
# Each section name maps to which CV.md section it renders into.
# Required for BLOCKER 3 (schema must regenerate the full CV.md, not just families).
generated_sections:
  vocabulary_hierarchy: { rendered_section: 'Vocabulary Hierarchy' }
  science_naming_rules: { rendered_section: 'Science Naming Rules' }
  filename_taxonomy: { rendered_section: 'Filename Taxonomy' }
  publication_capture_dispositions: { rendered_section: 'Publication-Capture Dispositions' }
  claim_strength_labels: { rendered_section: 'Claim-Strength / Release Labels' }
  audit_lane_field_vocabulary: { rendered_section: 'Audit Lane Field Vocabulary' }
  migration_legacy_wording: { rendered_section: 'Migration / Legacy Wording' }
  historical_lane_board_labels: { rendered_section: 'Historical Lane-Board Labels' }
  historical_discovery_log_labels: { rendered_section: 'Historical Discovery-Log Labels' }
  column_rules: { rendered_section: 'Column Rules' }
  protocol_qualifiers: { rendered_section: 'Protocol Qualifiers' }
  evidence_terms: { rendered_section: 'Evidence Terms' }
  hyphenation: { rendered_section: 'Hyphenation' }
  axiom_naming_out_of_scope: { rendered_section: 'Axiom Naming (out of scope for this doc)' }
  stale_narrative_archival: { rendered_section: 'Stale-Narrative Archival Vocabulary' }
  topic_language: { rendered_section: 'Topic-Local Language (note: scope_tag = topic_local; will move to topic notes in Cleanup-2)' }
  paper_voice: { rendered_section: 'Paper-Facing Prose Voice' }
```

The cleanup PR creates this file, populates it from the existing
content of CONTROLLED_VOCABULARY.md + audit/README field enums +
FRESH_LOOK_REQUIREMENTS independence tiers, and writes a renderer that
regenerates CONTROLLED_VOCABULARY.md + KEY_TERMINOLOGY.md from it.
Going forward, manual edits to the rendered docs are not permitted; all
changes flow through the YAML.

## Auto-correct mechanism

A new lint, `scripts/vocab_lint.py`:

```
Usage:
  scripts/vocab_lint.py [--fix] [--report-only] [--report-path PATH] <files...>

Behavior:
  - Reads docs/repo/controlled_vocabulary.yaml
  - For each input file:
    - Apply detection rules (rewrite_rules, filename_rules)
    - With --fix: apply mechanical rewrites; report what was changed
    - Without --fix: list violations to stdout
  - Writes a prose_status.json artifact recording per-file:
      { "path": str,
        "violations": [ { "rule_id": str, "before": str, "after": str | null } ],
        "auto_corrected": int,
        "needs_human_vocab_decision": int }
  - Exit code: 0 if clean (or all violations auto-fixed); 1 if any violations
    remain that could not be auto-rewritten
```

Mechanical rewrites are automatic; each rewrite is logged in
`prose_corrections` for the audit trail (automatic, not silent).
Violations that the YAML does not know how to rewrite mechanically are
flagged as `needs_human_vocab_decision` — they do not block the
commit, but they record a `prose_status` entry that batches into a
periodic vocab-extension review.

### Integration in the substantive loops

**audit-loop**: before writing an audit verdict, run `vocab_lint --fix`
on the source note being audited.

- Auto-corrected drift records as `prose_status: auto_corrected` on
  the row, with a list of mechanical rewrites in
  `prose_corrections`.
- A physics `audited_clean` remains clean even if prose had drift;
  the prose-status is recorded *separately*, never blocking the
  physics verdict.
- A genuinely new term that the YAML cannot mechanically rewrite
  records as `prose_status: needs_human_vocab_decision` and queues
  for a vocab-extension review, but does not block the physics
  verdict.

**review-loop**: already has "It may correct status vocabulary and
terminology so a PR follows repo conventions" (see the existing
review-loop SKILL.md line 28). Formalize this as `vocab_lint --fix` on
all branch-modified files before any landing gate.

**physics-loop**: run `vocab_lint --fix` on any source note authored
during the loop, before committing the loop checkpoint.

This shifts vocabulary compliance from agent discipline (fallible) to
loop mechanism (always-on).

## Physics ≠ Prose: ledger field schema

The audit ledger row gains two new fields, both written by the
audit-loop:

- `prose_status`: one of `clean`, `auto_corrected`,
  `needs_human_vocab_decision`.
- `prose_corrections`: list of `(rule_id, before, after)` tuples
  recording mechanical rewrites applied during this audit.

Default valid combinations:

| `audit_status` (physics) | `prose_status` (vocab) | Meaning |
|---|---|---|
| `audited_clean` | `clean` | Both clean. Standard happy path. |
| `audited_clean` | `auto_corrected` | Physics fine; vocab drift was auto-fixed mechanically. |
| `audited_clean` | `needs_human_vocab_decision` | Physics fine; vocab introduces a new term that needs a YAML extension decision. Does not block landing. |
| `audited_conditional` | `clean` | Physics dependency issue; vocab fine. |
| `audited_failed` | `clean` | Physics failure; vocab fine. |
| (any non-clean physics) | (any prose) | Physics verdict is independent; prose status is recorded for the same audit cycle. |

A non-clean physics verdict is *never* caused by vocabulary drift
alone. A genuinely new vocabulary requirement is *never* expressed as a
physics non-clean verdict.

## Agent pacing rule

The previous "vocabulary additions require a PR against
CONTROLLED_VOCABULARY.md before any note that uses them is auditable as
clean" rule is replaced by:

1. **Routine drift (rewrite_rules applies):** mechanical rewrite at
   commit time inside the loop. No PR. No ceremony. Agent commits the
   rewritten file as part of normal work.
2. **Genuinely new term (rewrite_rules cannot fix mechanically):**
   agent commits the note with the new term. `prose_status:
   needs_human_vocab_decision` records on the row.
   `prose_corrections` lists the new terms for the periodic
   vocab-extension review. Physics audit proceeds independently.
3. **Vocab-extension review:** a human (or a scheduled agent task)
   periodically reviews the queued `needs_human_vocab_decision` rows,
   either: (a) accepts the new term and lands a PR against
   `controlled_vocabulary.yaml`, or (b) rejects and the queued rows
   are re-corrected to canonical form via a `--fix` sweep.

This matches autonomous-agent pacing while preserving auditable
history.

## Forbidden patterns (after cleanup PR)

- **"legacy alias: X"** anywhere on live science surfaces. Aliases rot;
  use the canonical name only.
- **Physics primitives** in CONTROLLED_VOCABULARY.md or
  KEY_TERMINOLOGY.md.
- **Paraphrased indexes** that can drift from the canonical YAML. The
  rendered docs are products of the YAML.
- **New filename suffixes** for `claim_type: meta` notes. Canonical
  form is `_NOTE_<YYYY-MM-DD>.md`.
- **F-letter or other ad-hoc finding-label schemes** within notes.
  Canonical form is `### Finding N: <descriptive title>` with explicit
  numbering.
- **Audit verdicts that conflate physics with prose.** Use
  `audit_status` for physics, `prose_status` for vocab.

## Canonical structures for emerging needs

These sanctioned shapes meet the needs that the 84-note 2026-05-17 wave
was meeting, but without new vocabulary or new filename suffixes.

### Audit-prep note with multiple findings

Plain `<TOPIC>_NOTE_<YYYY-MM-DD>.md`. Structure:

```markdown
# <Topic> — Audit-Prep Notes

**Claim type:** meta
**Status authority:** independent audit lane only.

## Finding 1: <Descriptive Title>

**Symptom:** ...
**Evidence:** ...
**Recommended source-note repair:** ...
**What this does NOT establish:** ...

## Finding 2: <Descriptive Title>

(same sub-structure)

## Finding N: <Descriptive Title>

(same sub-structure)
```

Numbered explicit findings with descriptive titles. No filename suffix
encoding the role; no letter-code labels.

### Downstream surgical-fix note

Plain `<TOPIC>_NOTE_<YYYY-MM-DD>.md`. Structure:

```markdown
# <Topic> — Fix Record

**Claim type:** meta

## What changed
- modification 1: ...
- modification 2: ...

## Why
References specific findings from the audit-prep note, by title (e.g.
"Addresses Finding 1: <Title> of <PARENT_NOTE>_NOTE_<DATE>.md").

## What this does NOT establish
```

No filename suffix encoding the role. Cross-references by exact title
and filename.

## Migration scope (two cleanup PRs)

Per the consolidated review's MAJOR 10, the cleanup is split into two
PRs. Cleanup-1 is schema + tooling + generated docs (low-risk).
Cleanup-2 is the per-file migration sweep (judgment-required).

### Cleanup-1 (schema + tooling; low-risk, ships first)

1. **Create `docs/repo/controlled_vocabulary.yaml`** with the
   conformant schema specified above (W3C-conformant `audit_status`,
   GRADE-conformant `closure_status` × `chain_certainty`,
   IEEE 1044-conformant `defect_type` × `defect_class` × `severity`,
   AI-physics-extension fields tagged). Required: `schema_version: 1`,
   all `equivalent_to` standard references, `ai_extension` flags with
   rationale, `aliases` mapping historical enum values to the new
   schema cells.
2. **Schema migration in `apply_audit.py` and `audit_lint.py`:**
   - Add new fields: `failure_mode`, `dependency_status`,
     `closure_status`, `chain_certainty`, `defect_type`,
     `defect_class`, `severity`, `prose_status`,
     `prose_corrections`.
   - Replace flat `ALLOWED_VERDICTS` enum with the W3C-conformant
     4-value `audit_status` + orthogonal `failure_mode`.
   - Add a `pre_audit_prose_fix` envelope that atomically refreshes
     `note_hash` after a vocab_lint --fix run, per BLOCKER 1.
   - Backfill existing ledger rows from old enum values to the new
     schema using the `aliases` map. Specifically:
     - `audited_renaming` → `(audit_status: audited_retired,
       failure_mode: renaming)`
     - `audited_decoration` → `(audit_status: audited_retired,
       failure_mode: decoration)`
     - `audited_numerical_match` → `(audit_status: audited_retired,
       failure_mode: numerical_match)`
     - `audited_conditional` → `(audit_status: audited_clean,
       dependency_status: pending_chain)`
     - `audited_failed` → `(audit_status: audited_retired,
       failure_mode: generic)`
   - `prose_status` backfill: use
     `not_evaluated_pre_vocab_lint`, not `clean`, until each row is
     actually linted.
3. **Add `scripts/vocab_lint.py`** with `--fix`, `--report-only`,
   `--report-path` modes. Reads the YAML, applies the rewrite_rules
   and filename_rules, writes a per-file
   `prose_status.json` artifact. **Link-aware mode required** for
   filename renames (rewrites cross-doc references in the same
   commit, per BLOCKER 2). F-letter migration uses
   `migration_strategy: per_file_mapping_with_link_check`, not a
   one-shot regex.
4. **Add `scripts/render_controlled_vocabulary.py`** as the
   deterministic renderer. Inputs: `controlled_vocabulary.yaml`.
   Outputs: regenerated `CONTROLLED_VOCABULARY.md` and
   `KEY_TERMINOLOGY.md` with `<!-- generated; do not edit by hand;
   source: docs/repo/controlled_vocabulary.yaml hash=<sha256> -->`
   headers. Golden-test required: the rendered output must equal a
   compatibility-adjusted version of the current CV.md after
   regeneration.
5. **CI gate:** `.github/workflows/audit.yml` (or equivalent) runs
   `vocab_lint --report-only` and `render_controlled_vocabulary.py
   --check` on every PR. Failure if any unhandled drift or render
   diff exists.
6. **Vocab-extension queue file:**
   `docs/repo/vocab_extension_queue.json` created and surfaced
   through nightly audit cron. Per the resolved cadence decision.
7. **Wire `vocab_lint --fix`** into audit-loop, review-loop, and
   physics-loop pre-commit gates. Remove the "forward-looking"
   markers from the SKILL.md files since the tooling now exists.
8. **Update `audit/README.md`** with the new field semantics, the
   `note_hash` refresh behavior, and the `prose_status` separation.

### Cleanup-2 (migration sweep; judgment-required, ships after Cleanup-1)

1. **Per-file F-letter → Finding-N migration** using the
   `per_file_mapping_with_link_check` strategy. For each of the 9
   files with F-letter headings: build `{F-A: <existing title>,
   F-B: <existing title>, …}` map; rewrite headings, intra-doc
   references, markdown links, runner assertions, and source-note
   provenance citations atomically. Preserve historical reference via
   `formerly F-C in PR #1262` footnote on each migrated finding.
2. **Filename renames** for the ≥132 emergent-suffix notes (84
   `_HOSTILE_AUDIT_FINDINGS_NOTE_` + 16 `_STRETCH_ATTEMPT_NOTE_` + 9
   `_DOWNSTREAM_FIX_NOTE_` + 7 `_HOSTILE_REVIEW_*` + 5
   `_REVIEW_PACKET_` + 4 `_TERMINAL_SYNTHESIS_META_` + 4
   `_SHARPENED_NOTE_` + 4 one-offs). Use
   `vocab_lint --fix --link-aware`; commit one cluster at a time
   with a link-checker run after each commit.
3. **Remove all 45 `(legacy alias: X)` instances** by replacing the
   alias-wrapped form with the canonical name everywhere (with
   excluded paths in `docs/work_history/` and `archive_unlanded/`
   per the YAML's `excluded_paths`).
4. **Update all references** from `MINIMAL_AXIOMS_2026-04-11.md`
   (superseded 2026-05-03) to `MINIMAL_AXIOMS_2026-05-03.md`.
5. **Strip remaining physics primitives** from
   CONTROLLED_VOCABULARY.md and KEY_TERMINOLOGY.md if any remain
   after re-render. (Most should already be gone after this PR's
   strip.)
6. **Move topic-specific physics wording** (BMV / boundary-law /
   branch-mediated entanglement / historical retirement language)
   out of CONTROLLED_VOCABULARY.md into topic-scoped notes. Update
   `scope_tag: topic_local` entries in the YAML accordingly.
7. **Re-audit cascade:** the ≥132 migrated notes will have
   `note_hash` changes; this resets their audit rows to
   `unaudited` per FRESH_LOOK_REQUIREMENTS §6. Document the
   re-audit workload explicitly; either prioritize the highest-leverage
   ones or use the cleanup-only `pre_audit_prose_fix` envelope to
   avoid the cascade.
8. **Final `vocab_lint --report-only`** pass across the whole repo
   as a CI gate. Zero violations required to land Cleanup-2.

The cleanup is large but split. Cleanup-1's tooling lands first
behind the CI gate; Cleanup-2 then operates against a working
toolchain rather than building it as it goes.

## AI methods section

This vocabulary-hygiene system is itself a named element of the
AI-physics method, alongside audit-loop / review-loop / physics-loop
and the four governance docs. The methodology paper and the AI
methodology note both reference this design as a transferable pattern.

**Argument for the methods section:**

> At repo scale (thousands of AI-authored docs, parallel agent pacing),
> discipline-based vocabulary control fails: agents drift, emergent
> terminology compounds, and per-PR coordination becomes a synchronous
> bottleneck that the autopilot will not respect. Mechanism-based
> vocabulary control — a machine-readable canonical source, an
> auto-correcting lint integrated into the substantive loops, and a
> strict physics-versus-prose separation in audit verdicts — keeps a
> large AI-built repo navigable without imposing PR-pacing on every
> agent. The cost of the mechanism is small (one YAML, one lint
> script, one separate audit field) and the rot it prevents scales
> with repo size. The CL(3)×Z³ framework is the reference case; the
> mechanism transfers.

**Empirical anchor:** the 2026-05-17 wave of 83 ad-hoc note-type
suffix + F-letter findings notes is the case study. Discipline-based
governance (the existing "no new vocab" rule) caught it only after the
fact, and only through human review; mechanism-based governance would
have auto-corrected each note as it was committed.

## What this design intentionally does NOT do

- Does not write the YAML itself (cleanup PR).
- Does not implement `vocab_lint.py` (cleanup PR).
- Does not migrate the 84 emergent-suffix notes (cleanup PR).
- Does not extend vocabulary into physics-specific surfaces (BMV,
  boundary-law, etc. — cleanup PR moves those out of CV.md).
- Does not change the publication-side prose voice
  ([WRITING_VOICE_GUIDE_2026-04-25.md](../WRITING_VOICE_GUIDE_2026-04-25.md)
  remains separate).

## Resolved design decisions

These were "open questions" in earlier drafts; they are now decided
defaults for Cleanup-1 to implement. The companion review document
[VOCABULARY_HYGIENE_REVIEW_2026-05-18.md](VOCABULARY_HYGIENE_REVIEW_2026-05-18.md)
addresses the BLOCKERs and MAJORs raised during adversarial review.

1. **Renderer placement: `scripts/render_controlled_vocabulary.py`.**
   The renderer lives in `scripts/` alongside `vocab_lint.py`. The
   vocabulary system is orthogonal to the audit lane and should not
   sit under `docs/audit/scripts/`. Both the renderer and the lint
   are general-purpose repo tooling.
2. **YAML schema versioning: `schema_version: 1`.** Required at the
   top of `controlled_vocabulary.yaml`. Future migrations bump the
   integer and add a migration script under
   `scripts/migrations/vocab_schema_vN_to_vN+1.py`.
3. **`prose_status` does NOT propagate into `effective_status`.**
   `effective_status` is derived from `claim_type` + `audit_status` +
   dependency-chain closure only. The physics-versus-prose separation
   is preserved by construction: a non-clean `prose_status` cannot
   demote a physics-clean row's `effective_status`, and a
   `prose_status: clean` does not promote it.
4. **Vocab-extension review cadence: weekly batch OR 10+ queued
   entries, whichever comes first.** The repo nightly audit cron at
   `0 6 * * *` UTC can be extended with a "vocab-extension-queue
   summary" step that posts the current queue as a single comment or
   issue; a human reviewer or scheduled agent then batches the
   accepted terms into one PR against `controlled_vocabulary.yaml`.
   Backpressure: if the queue exceeds 50 entries, audit-loop and
   review-loop start emitting `prose_status:
   queue_backpressure_exceeded` instead of
   `needs_human_vocab_decision` so the absence of review is visible
   on every new row.

Cleanup-1 implements these decisions; Cleanup-2 sweeps the repo
against the resulting tooling.
