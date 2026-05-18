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
3. **Standard convention basis (inspired-by, not standards-conformant).**
   Each term family is inspired by an established convention without
   claiming faithful adaptation: W3C-style lifecycle for the
   audit-status journey; GRADE-spirit closure-status grading for
   theorem strength (one-axis, not the full GRADE *recommendation
   strength × evidence certainty* matrix); ISTQB / IEEE 1044-spirit
   anomaly / defect taxonomy for repair classes; multi-reviewer
   adversarial-review independence tiers (mostly novel). AI-physics
   extensions to each family are explicitly tagged and motivated.
   None of these are standards-conformant uses; the cited conventions
   are reference points, not authorities. See the consolidated review
   [VOCABULARY_HYGIENE_REVIEW_2026-05-18.md](VOCABULARY_HYGIENE_REVIEW_2026-05-18.md)
   §MAJOR 7 for why this matters.
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

| Family | Purpose | Standard-convention basis | AI-physics extensions |
|---|---|---|---|
| **Lifecycle** | Where a claim is in its review journey | W3C lifecycle (Working Draft → Candidate Recommendation → Recommendation → Retired); ISO/IEC 25010-style quality lifecycle | `audit_in_progress` (cross-confirmation gate); `audited_renaming` / `audited_decoration` / `audited_numerical_match` (AI-specific failure modes) |
| **Grade** | How strong a closed claim is | GRADE / Cochrane evidence-grading conventions (high / moderate / low / very low) adapted for theorem strength | `retained_pending_chain` (clean claim with non-retained dependencies — common in chain-of-trust contexts at AI scale) |
| **Defect** | Why a non-clean claim failed | ISTQB / IEEE 1044 software-defect taxonomy adapted for AI-generated derivations | All 7 repair classes are AI-physics extensions specific to mechanism failures (`missing_bridge_theorem`, `compute_required`, etc.) |
| **Independence** | How adversarial the audit was | Adversarial-review literature; multi-reviewer independence tiers | Model-family-level `fresh_context` and `cross_family` (same author family, restricted-context audit; different family) |

The full per-term inventory with definitions, inspired_by pointers,
and AI-extension flags lives in
`docs/repo/controlled_vocabulary.yaml` (cleanup PR creates it).

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
families:
  lifecycle:
    convention: "W3C lifecycle adapted for theorem audit"
    convention_reference: "https://www.w3.org/2021/Process-20211102/#rec-track"
    terms:
      unaudited:
        definition: "Row has not been audited yet."
        inspired_by: "W3C Working Draft"
        ai_extension: false
        deprecated: false
        deprecated_replacement: null
      audit_in_progress:
        definition: "First clean audit on a critical claim awaiting cross-confirmation."
        inspired_by: "W3C Candidate Recommendation"
        ai_extension: true
        ai_extension_rationale: "Cross-confirmation gate for AI-authored derivations."
      audited_clean:
        definition: "Derivation closes from cited inputs with no hidden premise."
        inspired_by: "W3C Recommendation"
        ai_extension: false
      audited_renaming:
        definition: "Load-bearing step defines a new symbol or asserts symbol identity."
        ai_extension: true
        ai_extension_rationale: "Catches definition-as-derivation, a known AI generation failure mode."
      audited_decoration:
        definition: "Exact algebraic corollary of a parent claim with no independent comparator, compression, or new structural integer."
        ai_extension: true
        ai_extension_rationale: "Catches mass-produced algebraic consequences of one upstream choice."
      audited_conditional:
        definition: "Depends on an unaudited dependency, open gate, or unratified bridge."
        inspired_by: "W3C Candidate Recommendation pending dependency"
        ai_extension: false
      audited_numerical_match:
        definition: "Result depends on a tuned/calibrated input rather than a structural theorem."
        ai_extension: true
        ai_extension_rationale: "Catches tuned-input matches presented as derivations."
      audited_failed:
        definition: "Chain does not close on its own terms."
        inspired_by: "W3C Retired (with cause)"
        ai_extension: false

  grade:
    convention: "GRADE / Cochrane evidence-grading adapted for theorem strength"
    convention_reference: "https://www.gradeworkinggroup.org/"
    terms:
      retained:
        definition: "Theorem-grade closure on the retained authority surface."
        inspired_by: "GRADE High (structural-theorem qualifier)"
        ai_extension: false
      retained_bounded:
        definition: "Theorem-grade closure with named bounds / admissions."
        ai_extension: false
      retained_no_go:
        definition: "Theorem-grade negative result."
        ai_extension: false
      retained_pending_chain:
        definition: "Clean theorem/no-go/bounded row whose upstream chain is not yet retained-grade."
        ai_extension: true
        ai_extension_rationale: "Chain-of-trust state common at AI-scale dependency graphs."
      # ... derived, bounded, open, frozen-out, promoted, ...

  defect:
    convention: "ISTQB / IEEE 1044 defect taxonomy adapted for AI-generated derivations"
    convention_reference: "https://www.istqb.org/"
    terms:
      missing_dependency_edge:
        definition: "A needed source note exists but is not wired as a direct dependency."
        inspired_by: "ISTQB Defect — missing reference"
        ai_extension: false
      dependency_not_retained:
        definition: "A direct dependency exists but is not retained-grade."
        ai_extension: true
        ai_extension_rationale: "Chain-of-trust failure specific to retained-grade propagation."
      missing_bridge_theorem:
        definition: "Claim needs a new theorem for a physical carrier, readout, unit map, etc."
        ai_extension: true
        ai_extension_rationale: "Common AI-generation gap: chain skips a load-bearing bridge."
      scope_too_broad:
        definition: "Clean bounded core exists, but current scope includes an unclosed extension."
        inspired_by: "ISTQB Defect — overclaim"
        ai_extension: false
      runner_artifact_issue:
        definition: "Runner, log, classifier, threshold, import, or pass/fail accounting blocks closure."
        inspired_by: "ISTQB Defect — test/build artifact"
        ai_extension: false
      compute_required:
        definition: "Closure needs a completed long run, sliced runner, or independent derivation."
        ai_extension: true
        ai_extension_rationale: "AI agents work faster than long-running computations; this state preserves audit honesty without blocking on compute."
      other:
        definition: "Catch-all when none of the above fits; must state why."
        ai_extension: false

  independence:
    convention: "Adversarial-review independence tiers adapted for AI model families"
    convention_reference: "Standard multi-reviewer adversarial review literature"
    terms:
      weak:
        definition: "Same model family, no clean-room. Not eligible to land audited_clean."
        ai_extension: false
      fresh_context:
        definition: "Same model family, different auditor/session identity, restricted-input audit."
        ai_extension: true
        ai_extension_rationale: "Clean-room same-family review for catching context poisoning without claiming cross-family independence."
      cross_family:
        definition: "Different model family from author."
        ai_extension: true
        ai_extension_rationale: "Adversarial-review independence at the model-family level."
      strong:
        definition: "Human auditor with no prior involvement in the note."
        inspired_by: "Standard independent peer review"
        ai_extension: false
      external:
        definition: "Off-repo reviewer with no project context."
        inspired_by: "External peer review / venue review"
        ai_extension: false

rewrite_rules:
  # Each rule: detect pattern, replace with canonical, optionally with a note
  - id: legacy_alias_strip
    pattern: '\s*\(legacy alias:\s*[A-Z][0-9A-Z]*\)'
    replacement: ''
    rationale: 'Aliasing creates rot. Use the canonical name only.'

  - id: support_to_retained_pending_chain
    pattern: '\bsupport tier\b'
    replacement: 'retained_pending_chain'
    rationale: '\'support\' is not a claim class; retained_pending_chain is the chain-not-retained case.'

  - id: hostile_audit_findings_suffix
    pattern: '_HOSTILE_AUDIT_FINDINGS_NOTE_(\d{4}-\d{2}-\d{2})\.md'
    replacement: '_NOTE_$1.md'
    rationale: 'New filename suffixes for meta notes are forbidden; use plain _NOTE_<date>.md.'

  - id: downstream_fix_suffix
    pattern: '_DOWNSTREAM_FIX_NOTE_(\d{4}-\d{2}-\d{2})\.md'
    replacement: '_NOTE_$1.md'
    rationale: 'Same as above.'

  - id: f_letter_heading
    pattern: '^### F-([A-Z]) — '
    replacement: '### Finding \1: '
    rationale: 'F-letter codes are forbidden; use descriptive numbered findings.'

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

scope:
  in_scope:
    - 'Process labels (status, audit fields, repair classes, evidence terms)'
    - 'Prose-voice rules and hyphenation'
    - 'Filename conventions'
  out_of_scope:
    - 'Framework primitives (live in MINIMAL_AXIOMS)'
    - 'Physics quantities (live in ASSUMPTION_DERIVATION_LEDGER / per-claim notes)'
    - 'Topic-specific physics wording (lives in topic notes; not vocabulary)'
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

## Migration scope (cleanup PR)

The companion cleanup PR will:

1. **Create `docs/repo/controlled_vocabulary.yaml`** from the existing
   content of CONTROLLED_VOCABULARY.md + audit/README field enums +
   FRESH_LOOK_REQUIREMENTS independence tiers. Populate with
   `inspired_by`, `ai_extension`, and `convention_reference` fields
   per the schema above.
2. **Add `scripts/vocab_lint.py`** implementing `--fix` and
   `--report-only` modes against the YAML's rewrite_rules and
   filename_rules.
3. **Wire `vocab_lint --fix`** into audit-loop, review-loop, and
   physics-loop pre-commit gates (skill-level rule + scripted pre-commit
   hook).
4. **Regenerate** CONTROLLED_VOCABULARY.md and KEY_TERMINOLOGY.md from
   the YAML via a small renderer script. Mark both as `<!-- generated; do
   not edit by hand -->` at the top.
5. **Sweep the repo** with `vocab_lint --fix` to apply all canonical
   rewrites in one pass. Commit the rewrites as a single sweep commit.
6. **Migrate ~84 hostile-audit-findings + downstream-fix notes** to the
   canonical structures defined in "Canonical structures for emerging
   needs" above. Filename change + F-letter heading change. The
   per-finding content is preserved; only the wrapping is rewritten.
7. **Remove all "legacy alias: X" instances** by replacing the
   alias-wrapped form with the canonical name everywhere.
8. **Update all references** from `MINIMAL_AXIOMS_2026-04-11.md`
   (superseded 2026-05-03) to `MINIMAL_AXIOMS_2026-05-03.md`.
9. **Strip physics primitives** from CONTROLLED_VOCABULARY.md and
   KEY_TERMINOLOGY.md (any `A_min` / `Axiom 1` / `Axiom 2` / `Axiom*`
   / `Cl(3)` / `Z³` / `g_bare` / `u_0` / `M_Pl` entries). They move to
   MINIMAL_AXIOMS sole authority.
10. **Move topic-specific physics wording** (BMV / boundary-law /
    branch-mediated entanglement / historical retirement language) out
    of CONTROLLED_VOCABULARY.md and into topic-scoped notes. These are
    physics prose conventions, not process vocabulary.
11. **Extend the audit ledger schema** to add `prose_status` and
    `prose_corrections` fields. Backfill `prose_status: clean` on
    existing rows; document the new fields in audit/README.md.
12. **Verify zero violations** remain via final `vocab_lint
    --report-only` pass on the whole repo. CI gate.

The cleanup PR is intentionally large and mechanical. Once it lands,
the maintenance cost falls to near zero: agents auto-correct in their
loops, the YAML is the only edit surface for vocabulary, and the
rendered docs stay in sync by construction.

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
