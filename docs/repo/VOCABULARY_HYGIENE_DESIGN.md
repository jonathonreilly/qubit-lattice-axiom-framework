# Vocabulary Hygiene Design

> **Key terms used in this doc** are indexed A-Z at [docs/KEY_TERMINOLOGY.md](../KEY_TERMINOLOGY.md); each row points to the canonical source-of-truth doc.

**Status:** design proposal for vocabulary governance in this repo and
as a reference exemplar for AI-built physics repos. Companion to
[KEY_TERMINOLOGY.md](../KEY_TERMINOLOGY.md) and
[CONTROLLED_VOCABULARY.md](CONTROLLED_VOCABULARY.md). The implementation
work lives in a separate cleanup PR (see "Migration scope" below).

**Date:** 2026-05-18

## Goal

Vocabulary discipline for large AI-built physics research repos at agent
pacing. Two products:

1. Repo-canonical process vocabulary that survives drift across
   thousands of AI-authored docs.
2. Reference exemplar that other AI-physics projects can adopt.

The framework science (`Cl(3)` on `Z^3`) is the case study; the
*process* — including this vocabulary system — is the primary
methodological deliverable.

## Principles

1. **Vocabulary is disjoint from physics.** Physics primitives (`Cl(3)`,
   `Z^3`, `A_min`, `Axiom 1`, `Axiom 2`, `g_bare`, `u_0`, `M_Pl`, etc.)
   are *not* vocabulary terms. They live in
   [MINIMAL_AXIOMS_2026-05-03.md](../MINIMAL_AXIOMS_2026-05-03.md) and
   per-claim notes. Vocabulary governs *process labels only*: status,
   audit fields, repair classes, evidence terms, prose voice.

2. **No rot possibility.** The canonical vocabulary is a
   machine-readable structured-data file (YAML). Rendered docs
   ([CONTROLLED_VOCABULARY.md](CONTROLLED_VOCABULARY.md),
   [KEY_TERMINOLOGY.md](../KEY_TERMINOLOGY.md)) are *products*
   regenerated from the YAML, not authored alongside it. Lint
   mechanically enforces; manual edits to rendered docs are not
   permitted.

3. **The vocabulary is physics-native and AI-physics-native.** It is
   not derived from external standards. The terms below grew from doing
   AI-physics audits in this repo and naming the verdicts and failure
   modes the audit lane actually encountered. Specifically:

   - **Physics-native terms** encode audit verdicts on physics
     derivations: `audited_clean`, `audited_failed`,
     `audited_conditional` (with its required repair-class prefix),
     `(A)`–`(G)` load-bearing step classes,
     `claim_type ∈ {positive_theorem, bounded_theorem, no_go,
     open_gate, decoration, meta}`.
   - **AI-physics-native terms** encode catches for AI-generation
     failure modes observed in practice: `audited_renaming`
     (definition-as-derivation; load-bearing step class (E) or (F)),
     `audited_decoration` (algebraic corollary with no new content),
     `audited_numerical_match` (tuned-input dependence; step class (G)).
     These are the verdicts the audit lane needed in order to catch
     specific patterns AI agents produce at scale.
   - **Reviewer-independence tiers** (`weak` / `fresh_context` /
     `cross_family` / `strong` / `external`) extend standard
     peer-review independence with model-family-aware tiers
     (`fresh_context`, `cross_family`) for AI-built work. The human-
     reviewer tiers (`strong`, `external`) match standard scientific
     peer review.
   - **Process additions** in this design (`prose_status`,
     `prose_corrections`) encode the separation of physics verdicts
     from prose drift.

   The contribution of this design is to *codify, formalize, and
   mechanically enforce* a physics-native vocabulary that was
   previously distributed across docs and discipline. The vocabulary
   is offered as a transferable **exemplar** — other AI-built research
   repos may adopt its shape — but the legitimacy of each term is
   grounded in the audit work that produced it, not in conformance to
   any external standard.

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

## What the vocabulary covers

The vocabulary's authoritative substantive content already lives in
two places:

- [docs/audit/README.md](../audit/README.md) defines the audit-lane
  fields (`claim_type`, `claim_scope`, `audit_status`,
  `effective_status`, repair classes, independence tiers, load-bearing
  step classes).
- [CONTROLLED_VOCABULARY.md](CONTROLLED_VOCABULARY.md) defines the
  surrounding operational vocabulary (publication-capture dispositions,
  claim-strength labels, filename rules, evidence terms, prose voice).

This design does **not** redefine those fields. The 8-value
`audit_status` enum, the 7 repair classes, the 5 independence tiers,
the (A)–(G) load-bearing step classes — all stay exactly as audit/README
defines them. They are physics-native and audit-grown; the audit lane
uses them productively today and the design has no reason to restructure
them.

What this design adds is:

1. A **machine-readable canonical source** ([`controlled_vocabulary.yaml`](controlled_vocabulary.yaml))
   so the human-readable docs become regenerable products.
2. Two **new ledger fields** (`prose_status`, `prose_corrections`) that
   separate vocabulary drift from physics verdicts.
3. A **vocab_lint tool** integrated into the substantive loops, so
   routine drift auto-corrects at commit time.
4. **Forbidden-pattern definitions** (legacy aliases, emergent
   filename suffixes, F-letter heading codes) with mechanical
   rewrite rules.
5. **Scope tags** identifying which surface each term governs and
   how transferable it is.

## Scope tags

Every term in the YAML carries a `scope_tag` identifying which surface
it governs. This determines transferability and migration
responsibility:

| Scope tag | Description | Transferable? |
|---|---|---|
| `core_process` | Pure process labels (e.g. `unaudited`, `audit_in_progress`, `prose_status` values). Repo-agnostic. | Yes — transferable unchanged to any AI-built research repo. |
| `audit_physics_process` | Verdicts on physics derivations encoding the AI-physics method (e.g. `audited_renaming`, `audited_decoration`, `audited_numerical_match`, `(A)`–`(G)` load-bearing step classes, the 7 repair classes). | Transferable to AI-physics repos facing the same generation failure modes. |
| `repo_physics_policy` | Policy on physics primitives; this repo only (e.g. axiom-naming rules, `A_min` definition, `Axiom*` prohibition). Authoritative source: [AXIOM_MINIMALITY_POLICY.md](../audit/AXIOM_MINIMALITY_POLICY.md). | Not transferable — every repo's axiom policy is its own. |
| `paper_voice` | Paper-facing prose voice rules. Authoritative source: [WRITING_VOICE_GUIDE_2026-04-25.md](../WRITING_VOICE_GUIDE_2026-04-25.md). | Stylistic — repo-specific. |
| `topic_local` | Topic-specific physics wording (BMV, boundary-law, branch-mediated entanglement, etc.). Lives in per-topic notes; Cleanup-2 moves these out of CV.md. | Not transferable — topic-specific to the framework. |

The transferability claim in the AI Methods section narrows
correspondingly: only `core_process` and `audit_physics_process`
transfer as exemplars to other AI-built research repos. The other three
tags are repo-specific.

## Out of scope for the vocabulary

These are **physics**, not vocabulary, and never appear in
[CONTROLLED_VOCABULARY.md](CONTROLLED_VOCABULARY.md) or
[KEY_TERMINOLOGY.md](../KEY_TERMINOLOGY.md):

- **Framework primitives.** `Cl(3)`, `Z^3`, `A_min`, `Axiom 1`,
  `Axiom 2`, `Axiom*`. Canonical home:
  [MINIMAL_AXIOMS_2026-05-03.md](../MINIMAL_AXIOMS_2026-05-03.md);
  policy: [AXIOM_MINIMALITY_POLICY.md](../audit/AXIOM_MINIMALITY_POLICY.md).
- **Physics quantities.** `g_bare`, `u_0`, `M_Pl`, `R_conn`, `alpha_s`,
  `v`, etc. Canonical home:
  [ASSUMPTION_DERIVATION_LEDGER.md](../ASSUMPTION_DERIVATION_LEDGER.md)
  for per-quantity status; per-claim notes for theorem-specific names.
- **Specific theorem / lane / observable names.** Live in their
  source notes; never in the vocabulary docs.
- **Topic-specific wording conventions** (BMV / boundary-law /
  branch-mediated-entanglement). These are *physics prose
  conventions*, not process vocabulary. Cleanup-2 moves them out of
  CONTROLLED_VOCABULARY.md into topic-scoped notes.

The cleanup PR will strip any physics primitives currently embedded in
CONTROLLED_VOCABULARY.md and KEY_TERMINOLOGY.md.

## Machine-readable canonical source

A new file, [`docs/repo/controlled_vocabulary.yaml`](controlled_vocabulary.yaml),
is created by the cleanup PR as the single source of truth. Schema:

```yaml
schema_version: 1

# Fields are the canonical source of truth. The human-readable docs
# (CONTROLLED_VOCABULARY.md, KEY_TERMINOLOGY.md) regenerate from this
# file; manual edits to the rendered docs are not permitted.

# ---- Top-level layers (matching the Vocabulary Hierarchy in CV.md) ----
layers:
  - id: 0_front_door
    rendered_doc: docs/KEY_TERMINOLOGY.md
    governs: "Single-page A-Z index of every repo-canonical process term."
  - id: 1_framework_substantive
    source_of_truth: docs/MINIMAL_AXIOMS_2026-05-03.md
    governs: "Framework primitives. Out of scope for this vocabulary."
  - id: 2_external_paper_text
    source_of_truth:
      - docs/ai_methodology/CANONICAL_FRAMING_PARAGRAPH_2026-04-25.md
      - docs/ai_methodology/AI_ACCOUNTABILITY_AND_DISCLOSURE_NOTE_2026-04-25.md
    governs: "Verbatim disclosure paragraphs for papers / preprints / talks."
  - id: 3_operational
    rendered_doc: docs/repo/CONTROLLED_VOCABULARY.md
    governs: "Operational vocabulary used inside the repo (this doc's home layer)."
  - id: 4_methodology_framing
    source_of_truth: docs/AI_METHODOLOGY_NOTE_2026-04-25.md
    governs: "Curated front-door for the methodology lane."

# ---- Term families ----
term_families:

  claim_type:
    description: "What kind of object the auditor says the row is."
    authority: docs/audit/README.md
    scope_tag: audit_physics_process
    values:
      positive_theorem:  {definition: "Derived positive result."}
      bounded_theorem:   {definition: "Theorem with named bounds / admissions."}
      no_go:             {definition: "Negative-result theorem foreclosing a route."}
      open_gate:         {definition: "Clean open gate; blocks retained propagation."}
      decoration:        {definition: "Algebraic consequence of a parent claim with no new physical content."}
      meta:              {definition: "Non-claim infrastructure rows (audit-prep, synthesis, fix-records)."}

  audit_status:
    description: "Auditor's verdict on the row."
    authority: docs/audit/README.md
    scope_tag: audit_physics_process
    values:
      unaudited:
        definition: "Row has not been audited yet."
      audit_in_progress:
        definition: "First clean audit recorded; awaiting cross-confirmation per FRESH_LOOK_REQUIREMENTS §4."
      audited_clean:
        definition: "Derivation closes from cited inputs with no hidden premise. Load-bearing step must be class (A), (C), or genuine (D) over independent retained inputs."
      audited_renaming:
        definition: "Load-bearing step is a definition (class (E)) or symbol-identity assertion (class (F)). Catches definition-as-derivation: chain reduces to definition substitution."
        catches: "AI-generation failure mode: defining a new symbol as a target ratio, then 'showing' it matches data by name substitution."
      audited_conditional:
        definition: "Closure conditional on an unaudited dependency, open gate, retained-pending-chain row, unratified bridge, or premise not closed by cited authorities. Requires repair-class prefix in notes_for_re_audit_if_any."
      audited_decoration:
        definition: "Exact algebraic corollary of a parent claim with no independent comparator, falsifiability, compression, or new physical content."
        catches: "AI-generation failure mode: mass-producing algebraic consequences of one upstream parameter choice and presenting each as a separate retained theorem."
      audited_failed:
        definition: "Chain is wrong, stale relative to the runner, mismatches the observable, contradicts dependencies, or does not close on its own terms."
      audited_numerical_match:
        definition: "Result depends on a tuned/calibrated input or chosen scale/value rather than a structural theorem. Load-bearing step is class (G)."
        catches: "AI-generation failure mode: presenting a tuned-input match as a derivation."

  effective_status:
    description: "Publication-facing status, pipeline-derived from claim_type × audit_status × dependency closure. Not auditor-set."
    authority: docs/audit/README.md
    scope_tag: audit_physics_process
    values:
      retained:                    {definition: "claim_type=positive_theorem + audit_status=audited_clean + retained-grade deps."}
      retained_no_go:              {definition: "claim_type=no_go + audit_status=audited_clean + retained-grade deps."}
      retained_bounded:            {definition: "claim_type=bounded_theorem + audit_status=audited_clean + retained-grade deps."}
      retained_pending_chain:      {definition: "Clean theorem/no-go/bounded whose upstream chain is not yet retained-grade. Does not propagate retained status."}
      open_gate:                   {definition: "Clean open gate. Blocks retained propagation."}
      decoration_under_<parent>:   {definition: "Audited decoration boxed under a retained parent claim."}
      meta:                        {definition: "Non-claim infrastructure row."}
      audited_<failure_mode>:      {definition: "Terminal non-clean audit verdict on an active claim."}

  repair_class:
    description: "Required prefix in notes_for_re_audit_if_any for audited_conditional verdicts."
    authority: docs/audit/README.md
    scope_tag: audit_physics_process
    values:
      missing_dependency_edge: {definition: "Needed source note exists but is not wired as a direct dependency."}
      dependency_not_retained: {definition: "Direct dependency exists but is not retained-grade."}
      missing_bridge_theorem:  {definition: "Claim needs a new theorem for a carrier, readout, unit map, boundary condition, sector choice, normalization, or observable bridge."}
      scope_too_broad:         {definition: "Clean bounded core exists, but the current scope includes an unclosed extension."}
      runner_artifact_issue:   {definition: "Runner, log, classifier, threshold, import, or pass/fail accounting blocks closure despite local scope."}
      compute_required:        {definition: "Closure needs a completed long run, sliced runner, cached certificate, or independent derivation."}
      other:                   {definition: "None of the above fits; the note must state why."}

  independence:
    description: "Adversarial-review independence tier between auditor and author. auditor ≠ author required."
    authority: docs/audit/FRESH_LOOK_REQUIREMENTS.md
    scope_tag: audit_physics_process
    values:
      weak:
        definition: "Same model family or context restrictions cannot be established. Permitted for diagnostic review; not eligible to land audited_clean."
      fresh_context:
        definition: "Same model family, different auditor/session identity, restricted-input audit. Same-family clean-room tier for detecting context poisoning."
      cross_family:
        definition: "Different model family from author. Default cross-family auditor for this repo: best available full Codex GPT model at maximum reasoning."
      strong:
        definition: "Human reviewer with no prior involvement in the note."
      external:
        definition: "Off-repo reviewer with no project context. Only tier satisfying external-impact requirements; the audit lane does not produce these on its own."

  load_bearing_step_class:
    description: "The kind of step the load-bearing sentence or equation is. Determines the verdict gate."
    authority: docs/audit/AUDIT_AGENT_PROMPT_TEMPLATE.md
    scope_tag: audit_physics_process
    values:
      "(A)": {definition: "Algebraic identity check on existing inputs."}
      "(B)": {definition: "Cross-note input verification (reads value from another note)."}
      "(C)": {definition: "First-principles compute from the axioms (Cl(3) on Z^3 plus accepted normalizations) producing a number not present in any input."}
      "(D)": {definition: "External comparator check against PDG / lattice QCD / observation."}
      "(E)": {definition: "Definition (introduces a new symbol). Triggers audited_renaming."}
      "(F)": {definition: "Renaming (asserts symbol identity between two existing concepts). Triggers audited_renaming."}
      "(G)": {definition: "Numerical match at a tuned input scale. Triggers audited_numerical_match."}

  prose_status:
    description: "Vocabulary compliance of the source note. Separate from audit_status (physics)."
    authority: docs/repo/VOCABULARY_HYGIENE_DESIGN.md
    scope_tag: core_process
    values:
      clean:                          {definition: "No vocabulary drift detected by vocab_lint."}
      auto_corrected:                 {definition: "Routine drift mechanically rewritten by vocab_lint --fix; rewrites logged in prose_corrections."}
      needs_human_vocab_decision:     {definition: "Genuinely new term that vocab_lint cannot mechanically rewrite; queued for vocab-extension review."}
      not_evaluated_pre_vocab_lint:   {definition: "Pre-Cleanup-1 row never linted under the new rules. Used during backfill only."}
      queue_backpressure_exceeded:    {definition: "Vocab-extension review queue is >50 entries deep; new unresolved terms emit this until queue is processed."}

  prose_corrections:
    description: "List of (rule_id, before, after) tuples recording mechanical rewrites applied during the same audit cycle."
    authority: docs/repo/VOCABULARY_HYGIENE_DESIGN.md
    scope_tag: core_process

# ---- Scope tags ----
scope_tags:
  core_process:
    description: "Pure process labels transferable unchanged to other AI-built repos."
    examples: [unaudited, audit_in_progress, prose_status]
  audit_physics_process:
    description: "Verdicts on physics derivations encoding the AI-physics method."
    examples: [audited_renaming, audited_decoration, audited_numerical_match, load_bearing_step_class, repair_class]
  repo_physics_policy:
    description: "Policy on physics primitives; this repo only."
    examples: ["axiom naming policy", "A_min definition", "Axiom* prohibition"]
    governing_doc: docs/audit/AXIOM_MINIMALITY_POLICY.md
  paper_voice:
    description: "Paper-facing prose voice rules."
    governing_doc: docs/WRITING_VOICE_GUIDE_2026-04-25.md
  topic_local:
    description: "Topic-specific physics wording (BMV, boundary-law, etc.)."
    home: "Per-topic notes; not in CV.md after Cleanup-2."

# ---- Filename rules ----
filename_rules:
  meta_note_suffix: '_NOTE_<YYYY-MM-DD>.md'
  forbidden_suffixes:
    - '_HOSTILE_AUDIT_FINDINGS_NOTE_'   # 84 instances
    - '_DOWNSTREAM_FIX_NOTE_'           # 9 instances
    - '_FIX_RECORD_'
    - '_FINDINGS_MEMO_'
    - '_ADDENDUM_'
    - '_SURGICAL_REPAIR_'
    - '_AUDIT_BRIEF_'
    - '_STRETCH_ATTEMPT_NOTE_'          # 16 instances
    - '_REVIEW_PACKET_'                 # 5 instances
    - '_TERMINAL_SYNTHESIS_META_'       # 4 instances
    - '_SHARPENED_NOTE_'                # 4 instances
    - '_HOSTILE_REVIEW_'                # 7 instances
    - '_FRAMING_FIX_NOTE_'
    - '_ROUTING_CORRECTION_NOTE_'
    - '_OBJECTION_CLOSURE_NOTE_'
    - '_CAMPAIGN_PROGRESS_SYNTHESIS_'

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
    # with link-aware cross-doc reference updates.
    migration_strategy: per_file_mapping_with_link_check
    rationale: 'F-letter codes are forbidden; descriptive numbered findings replace them.'

# ---- Generated sections (renderer-facing) ----
# Each section name maps to which CV.md section it renders into.
# Required so the renderer can regenerate the full CV.md, not just a subset.
generated_sections:
  vocabulary_hierarchy:             {rendered_section: 'Vocabulary Hierarchy'}
  science_naming_rules:             {rendered_section: 'Science Naming Rules'}
  filename_taxonomy:                {rendered_section: 'Filename Taxonomy'}
  publication_capture_dispositions: {rendered_section: 'Publication-Capture Dispositions'}
  claim_strength_labels:            {rendered_section: 'Claim-Strength / Release Labels'}
  audit_lane_field_vocabulary:      {rendered_section: 'Audit Lane Field Vocabulary'}
  migration_legacy_wording:         {rendered_section: 'Migration / Legacy Wording'}
  historical_lane_board_labels:     {rendered_section: 'Historical Lane-Board Labels'}
  historical_discovery_log_labels:  {rendered_section: 'Historical Discovery-Log Labels'}
  column_rules:                     {rendered_section: 'Column Rules'}
  protocol_qualifiers:              {rendered_section: 'Protocol Qualifiers'}
  evidence_terms:                   {rendered_section: 'Evidence Terms'}
  hyphenation:                      {rendered_section: 'Hyphenation'}
  axiom_naming_out_of_scope:        {rendered_section: 'Axiom Naming (out of scope for this doc)'}
  stale_narrative_archival:         {rendered_section: 'Stale-Narrative Archival Vocabulary'}
  topic_language:                   {rendered_section: 'Topic-Local Language (note: scope_tag = topic_local; moves to topic notes in Cleanup-2)'}
  paper_voice:                      {rendered_section: 'Paper-Facing Prose Voice'}

scope:
  in_scope:
    - 'Process labels (audit_status, prose_status, repair_class, independence, load_bearing_step_class, etc.)'
    - 'Filename conventions'
    - 'Forbidden patterns'
  out_of_scope:
    - 'Framework primitives (live in MINIMAL_AXIOMS_2026-05-03.md)'
    - 'Physics quantities (live in ASSUMPTION_DERIVATION_LEDGER / per-claim notes)'
    - 'Topic-specific physics wording (lives in topic notes; not vocabulary)'
```

The cleanup PR creates this file, populates it from the existing
content of [audit/README.md](../audit/README.md) field enums,
[FRESH_LOOK_REQUIREMENTS.md](../audit/FRESH_LOOK_REQUIREMENTS.md)
independence tiers, and the surrounding sections of
[CONTROLLED_VOCABULARY.md](CONTROLLED_VOCABULARY.md), then writes a
renderer that regenerates CONTROLLED_VOCABULARY.md + KEY_TERMINOLOGY.md
from it. Going forward, manual edits to the rendered docs are not
permitted; all changes flow through the YAML.

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
  - Exit code: 0 if clean (or all violations auto-fixed); 1 if any
    violations remain that could not be auto-rewritten
```

Mechanical rewrites are automatic; each rewrite is logged in
`prose_corrections` for the audit trail (automatic, not silent).
Violations that the YAML does not know how to rewrite mechanically are
flagged as `needs_human_vocab_decision` — they do not block the
commit, but they record an entry in the file-level vocab-extension
queue that batches into a periodic review.

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

**review-loop**: already auto-corrects status vocabulary and
terminology so a PR follows repo conventions (see review-loop SKILL.md
line 28). Formalize this as `vocab_lint --fix` on all branch-modified
files before any landing gate.

**physics-loop**: run `vocab_lint --fix` on any source note authored
during the loop, before committing the loop checkpoint.

This shifts vocabulary compliance from agent discipline (fallible) to
loop mechanism (always-on).

## Physics ≠ Prose: ledger field schema

The audit ledger row gains two new fields, both written by the
audit-loop:

- `prose_status`: one of `clean`, `auto_corrected`,
  `needs_human_vocab_decision`, `not_evaluated_pre_vocab_lint`,
  `queue_backpressure_exceeded`.
- `prose_corrections`: list of `(rule_id, before, after)` tuples
  recording mechanical rewrites applied during this audit.

Valid combinations:

| `audit_status` (physics) | `prose_status` (vocab) | Meaning |
|---|---|---|
| `audited_clean` | `clean` | Both clean. Standard happy path. |
| `audited_clean` | `auto_corrected` | Physics fine; vocab drift was auto-fixed mechanically. |
| `audited_clean` | `needs_human_vocab_decision` | Physics fine; vocab introduces a new term that needs a YAML extension decision. Does not block landing. |
| `audited_conditional` | (any) | Physics dependency issue; vocab status independent. |
| `audited_renaming` | (any) | Physics: load-bearing step is class (E)/(F). Vocab status independent. |
| `audited_decoration` | (any) | Physics: algebraic corollary. Vocab status independent. |
| `audited_numerical_match` | (any) | Physics: tuned-input dependence. Vocab status independent. |
| `audited_failed` | (any) | Physics failure; vocab status independent. |

A non-clean physics verdict is *never* caused by vocabulary drift
alone. A genuinely new vocabulary requirement is *never* expressed as a
physics non-clean verdict.

`prose_status` does **not** propagate into `effective_status`.
`effective_status` is derived from `claim_type` + `audit_status` +
dependency-chain closure only. The physics-versus-prose separation is
preserved by construction: a non-clean `prose_status` cannot demote a
physics-clean row's `effective_status`, and a `prose_status: clean`
does not promote it.

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
   `vocab_extension_queue.json` (a separate file-level queue) lists
   the new terms with their file paths and line numbers. Physics audit
   proceeds independently.
3. **Vocab-extension review:** weekly batch OR 10+ queued entries,
   whichever comes first. The repo nightly audit cron at `0 6 * * *`
   UTC posts the current queue as a single comment or issue; a human
   reviewer or scheduled agent then batches the accepted terms into one
   PR against `controlled_vocabulary.yaml`. **Backpressure:** if the
   queue exceeds 50 entries, audit-loop and review-loop emit
   `prose_status: queue_backpressure_exceeded` instead of
   `needs_human_vocab_decision` so the absence of review is visible on
   every new row.

This matches autonomous-agent pacing while preserving auditable
history.

## Forbidden patterns (after cleanup PR)

- **"legacy alias: X"** anywhere on live science surfaces. Aliases rot;
  use the canonical name only. (Excluded paths: `docs/work_history/**`,
  `archive_unlanded/**`.)
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

The cleanup is split into two PRs. Cleanup-1 is schema + tooling +
generated docs (low-risk). Cleanup-2 is the per-file migration sweep
(judgment-required).

### Cleanup-1 (schema + tooling; low-risk, ships first)

1. **Create [`docs/repo/controlled_vocabulary.yaml`](controlled_vocabulary.yaml)**
   populated from the existing field definitions in
   [audit/README.md](../audit/README.md),
   [FRESH_LOOK_REQUIREMENTS.md](../audit/FRESH_LOOK_REQUIREMENTS.md),
   and [CONTROLLED_VOCABULARY.md](CONTROLLED_VOCABULARY.md). The
   8-value `audit_status`, 7 repair classes, 5 independence tiers, and
   (A)–(G) load-bearing step classes are copied across with their
   existing semantics — **no enum restructure**. Required:
   `schema_version: 1`, `scope_tag` on every term, `authority` link to
   the source-of-truth doc, `catches` field on the three
   AI-physics-native verdicts (`audited_renaming`,
   `audited_decoration`, `audited_numerical_match`).

2. **Schema migration in `apply_audit.py` and `audit_lint.py`:**
   - Add new fields: `prose_status`, `prose_corrections`.
   - Add a `pre_audit_prose_fix` envelope that carries `{old_hash,
     new_hash, prose_status, prose_corrections}` and atomically
     refreshes `note_hash` after a vocab_lint --fix run. This resolves
     the integration issue where running `--fix` on the source note
     would otherwise invalidate the audit before it could apply.
   - `prose_status` backfill: use
     `not_evaluated_pre_vocab_lint`, not `clean`, until each row is
     actually linted.

3. **Add `scripts/vocab_lint.py`** with `--fix`, `--report-only`,
   `--report-path` modes. Reads the YAML, applies the rewrite_rules
   and filename_rules, writes a per-file
   `prose_status.json` artifact. **Link-aware mode required** for
   filename renames (rewrites cross-doc references in the same
   commit). F-letter migration uses
   `migration_strategy: per_file_mapping_with_link_check`, not a
   one-shot regex.

4. **Add `scripts/render_controlled_vocabulary.py`** as the
   deterministic renderer. Inputs:
   [`controlled_vocabulary.yaml`](controlled_vocabulary.yaml).
   Outputs: regenerated
   [CONTROLLED_VOCABULARY.md](CONTROLLED_VOCABULARY.md) and
   [KEY_TERMINOLOGY.md](../KEY_TERMINOLOGY.md) with
   `<!-- generated; do not edit by hand; source:
   docs/repo/controlled_vocabulary.yaml hash=<sha256> -->` headers.
   Golden-test required: the rendered output must equal a
   compatibility-adjusted version of the current CV.md after
   regeneration.

5. **CI gate:** `.github/workflows/audit.yml` (or equivalent) runs
   `vocab_lint --report-only` and `render_controlled_vocabulary.py
   --check` on every PR. Failure if any unhandled drift or render
   diff exists.

6. **Vocab-extension queue file:**
   `docs/repo/vocab_extension_queue.json` created and surfaced
   through the nightly audit cron. File-level (independent of audit
   rows), so queue entries from review-loop / physics-loop are not
   dropped on the floor when no audit row exists yet.

7. **Wire `vocab_lint --fix`** into audit-loop, review-loop, and
   physics-loop pre-commit gates. Remove the "forward-looking"
   markers from the three SKILL.md files since the tooling now exists.

8. **Update [audit/README.md](../audit/README.md)** with the new
   field semantics, the `note_hash` refresh behavior, and the
   `prose_status` separation.

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

3. **Remove all 45 `(legacy alias: X)` instances** on live science
   surfaces by replacing the alias-wrapped form with the canonical
   name everywhere (with excluded paths in `docs/work_history/` and
   `archive_unlanded/` per the YAML's `excluded_paths`).

4. **Update all references** from `MINIMAL_AXIOMS_2026-04-11.md`
   (superseded 2026-05-03) to `MINIMAL_AXIOMS_2026-05-03.md`.

5. **Strip remaining physics primitives** from
   CONTROLLED_VOCABULARY.md and KEY_TERMINOLOGY.md if any remain
   after re-render.

6. **Move topic-specific physics wording** (BMV / boundary-law /
   branch-mediated entanglement / historical retirement language)
   out of CONTROLLED_VOCABULARY.md into topic-scoped notes. Update
   `scope_tag: topic_local` entries in the YAML accordingly.

7. **Re-audit cascade:** the ≥132 migrated notes will have
   `note_hash` changes; without intervention this resets their audit
   rows to `unaudited` per FRESH_LOOK_REQUIREMENTS §6. Use the
   cleanup-only `pre_audit_prose_fix` envelope (Cleanup-1 #2) to
   carry vocabulary-only `note_hash` changes atomically without
   resetting the verdict.

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

**The methodological claim:**

The vocabulary is *physics-native* (audit verdicts on derivations,
load-bearing step classes, repair classes, claim types) and
*AI-physics-native* (catches for specific AI-generation failure modes:
`audited_renaming` for definition-as-derivation, `audited_decoration`
for algebraic corollaries with no new content, `audited_numerical_match`
for tuned-input dependence). It emerged from doing AI-physics audits
in this repo and is offered as a transferable **exemplar** to other
AI-built research repos, with explicit scope:

- `core_process` terms transfer unchanged.
- `audit_physics_process` terms transfer to AI-physics repos facing the
  same generation failure modes.
- `repo_physics_policy`, `paper_voice`, and `topic_local` terms are
  repo-specific and do not transfer.

The transferability is a methodological claim, not a
standards-conformance claim. The vocabulary is not derived from any
adjacent standard — those address different problems (web
specifications, clinical guidelines, software defects, etc.). The
legitimacy of each term is grounded in the audit work that produced
it.

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
> with repo size. The `Cl(3) × Z^3` framework is the reference case;
> the mechanism transfers as an exemplar to AI-built research repos
> meeting the structural preconditions listed in
> [AI_METHODOLOGY_NOTE_2026-04-25.md §5a](../AI_METHODOLOGY_NOTE_2026-04-25.md).

**Empirical anchor:** the 2026-05-17 wave of 83 ad-hoc note-type
suffix + F-letter findings notes is the case study. Discipline-based
governance (the existing "no new vocab" rule) caught it only after the
fact, and only through human review; mechanism-based governance would
have auto-corrected each note as it was committed.

## What this design intentionally does NOT do

- Does not write the YAML itself (cleanup PR).
- Does not implement `vocab_lint.py` (cleanup PR).
- Does not migrate the ≥132 emergent-suffix notes (cleanup PR).
- Does not restructure the existing 8-value `audit_status` enum or
  the 7 repair classes or the 5 independence tiers — these are
  physics-native and audit-grown; the audit lane uses them
  productively today and there is no reason to change them.
- Does not extend vocabulary into physics-specific surfaces (BMV,
  boundary-law, etc. — cleanup PR moves those out of CV.md).
- Does not change the publication-side prose voice
  ([WRITING_VOICE_GUIDE_2026-04-25.md](../WRITING_VOICE_GUIDE_2026-04-25.md)
  remains separate).

## Resolved design decisions

These were "open questions" in earlier drafts; they are now decided
defaults for Cleanup-1 to implement.

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
