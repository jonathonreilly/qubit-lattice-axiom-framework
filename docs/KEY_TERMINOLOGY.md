<!-- generated; do not edit by hand; source: docs/repo/controlled_vocabulary.yaml hash=de0c15a28d0872427a798a7d0f9eb99389c46cac72ab4ed43d93ef2f8e48e700 -->
# Key Terminology

**Claim type:** meta

Single-page A-Z lookup of repo-canonical **process** terms (status,
audit fields, repair classes, evidence terms, prose voice). One line
per term, with a pointer to the canonical source-of-truth doc.

**Scope rule:** vocabulary is disjoint from physics. Physics
primitives (`Cl(3)`, `Z^3`, `A_min`, Lattice, Qubit, Admissibility, Record, `Axiom*`,
`g_bare`, `u_0`, `M_Pl`, `R_conn`, `alpha_s`, etc.) are **not** in this
index. They live in
`docs/MINIMAL_AXIOMS_2026-06-29.md` (which supersedes the 2026-06-05
Lattice/Quantum/Record memo) and per-claim notes. See
`docs/repo/VOCABULARY_HYGIENE_DESIGN.md`
for the principle.

**Authority:** this file is an *index*, not a *definition*. The
source-of-truth doc named in each row is the binding authority. This
file is a *generated product* of
[docs/repo/controlled_vocabulary.yaml](repo/controlled_vocabulary.yaml) +
[scripts/templates/KEY_TERMINOLOGY.md.template](../scripts/templates/KEY_TERMINOLOGY.md.template);
do not edit it directly. Run
`python3 scripts/render_controlled_vocabulary.py` after changing the
YAML or template.

**Hierarchy:** this is the front-door entry point above the four
governance layers in
`docs/repo/CONTROLLED_VOCABULARY.md §Vocabulary Hierarchy`.
Every vocab / policy / process doc in the repo references back here.

---

## A

- **archive_unlanded/** — canonical recovery surface for failed-narrative source notes. Path form `archive_unlanded/<cluster-tag>/`. → [docs/audit/STALE_NARRATIVE_POLICY.md](audit/STALE_NARRATIVE_POLICY.md), `docs/repo/CONTROLLED_VOCABULARY.md §Stale-Narrative Archival Vocabulary`
- **audit_in_progress** — `audit_status` value: a first clean audit on a critical claim awaiting cross-confirmation; not yet `audited_clean`. → [docs/audit/README.md](audit/README.md)
- **audit_status** — auditor-set field; one of `unaudited`, `audit_in_progress`, `audited_clean`, `audited_renaming`, `audited_conditional`, `audited_decoration`, `audited_failed`, `audited_numerical_match`. → [docs/audit/README.md](audit/README.md), `docs/repo/CONTROLLED_VOCABULARY.md §Audit Lane Field Vocabulary`
- **audited_clean** — `audit_status` verdict; derivation closes from cited inputs with no hidden premise. Load-bearing step must be class `(C)` or genuine `(A)` over independent retained inputs. → [docs/audit/AUDIT_AGENT_PROMPT_TEMPLATE.md](audit/AUDIT_AGENT_PROMPT_TEMPLATE.md)
- **audited_conditional** — `audit_status` verdict; depends on an unaudited dependency, open gate, retained-pending-chain row, unratified bridge, or premise not closed by cited authorities. Requires repair-class prefix in `notes_for_re_audit_if_any`. → [docs/audit/README.md](audit/README.md)
- **audited_decoration** — `audit_status` verdict; exact algebraic corollary of a parent claim with no independent comparator, falsifiability, compression, or new physical content. → [docs/audit/ALGEBRAIC_DECORATION_POLICY.md](audit/ALGEBRAIC_DECORATION_POLICY.md)
- **audited_failed** — `audit_status` verdict; chain is wrong, stale relative to runner, mismatches the observable, contradicts dependencies, or does not close on its own terms. → [docs/audit/AUDIT_AGENT_PROMPT_TEMPLATE.md](audit/AUDIT_AGENT_PROMPT_TEMPLATE.md)
- **audited_numerical_match** — `audit_status` verdict; result depends on a tuned/calibrated input or chosen scale rather than a structural theorem. Load-bearing step in class `(G)`. → [docs/audit/AUDIT_AGENT_PROMPT_TEMPLATE.md](audit/AUDIT_AGENT_PROMPT_TEMPLATE.md)
- **audited_renaming** — `audit_status` verdict; load-bearing step defines a new symbol (class `(E)`) or asserts symbol identity between existing concepts (class `(F)`). Chain reduces to definition substitution, not derivation. → [docs/audit/AUDIT_AGENT_PROMPT_TEMPLATE.md](audit/AUDIT_AGENT_PROMPT_TEMPLATE.md)
- **auditor** — agent / human / session that performed the audit. Must not equal `author`. → [docs/audit/FRESH_LOOK_REQUIREMENTS.md](audit/FRESH_LOOK_REQUIREMENTS.md)
- **auditor_family** — model family of the auditor (e.g. `codex-gpt-5.6`, `claude-opus-4.x`, `human`). Used to enforce cross-family independence. → [docs/audit/FRESH_LOOK_REQUIREMENTS.md](audit/FRESH_LOOK_REQUIREMENTS.md)
- **author** — agent / human / session that produced the source note. → [docs/audit/FRESH_LOOK_REQUIREMENTS.md](audit/FRESH_LOOK_REQUIREMENTS.md)
- **auto_corrected** — `prose_status` value: vocabulary drift was mechanically rewritten by `vocab_lint --fix` during the loop. Recorded in `prose_corrections` for audit trail. → `docs/repo/VOCABULARY_HYGIENE_DESIGN.md`

## B

- **bounded** — publication-capture disposition: live captured family outside the main paper core with explicit caveats. Also a claim-strength family (`bounded_theorem`, `bounded companion`, `bounded support theorem`, etc.). → `docs/repo/CONTROLLED_VOCABULARY.md §Publication-Capture Dispositions`, `§Claim-Strength / Release Labels`
- **bounded_theorem** — `claim_type` value: theorem with named bounds / admissions; can earn `effective_status: retained_bounded` after clean audit + retained-grade deps. → [docs/audit/README.md](audit/README.md)
- **boxing** — decoration handling: rolling up an `audited_decoration` cluster into a single corollary line under the parent claim's row. → [docs/audit/ALGEBRAIC_DECORATION_POLICY.md](audit/ALGEBRAIC_DECORATION_POLICY.md)

## C

- **(C)** — load-bearing step class: first-principles compute from the framework axioms producing a number not present in any input. The only derivation class consistent with `audited_clean` for compute steps. → [docs/audit/AUDIT_AGENT_PROMPT_TEMPLATE.md](audit/AUDIT_AGENT_PROMPT_TEMPLATE.md)
- **claim_scope** — auditor-set field: short citeable statement of exactly what was audited. Required for applied audits. → [docs/audit/README.md](audit/README.md)
- **claim_type** — auditor-set field: one of `positive_theorem`, `bounded_theorem`, `no_go`, `open_gate`, `decoration`, `meta`. → [docs/audit/README.md](audit/README.md), `docs/repo/CONTROLLED_VOCABULARY.md §Audit Lane Field Vocabulary`
- **clean** — `prose_status` value: no vocabulary drift detected by `vocab_lint`. → `docs/repo/VOCABULARY_HYGIENE_DESIGN.md`
- **closure** — evidence term: use only when the load-bearing claim is actually closed. Avoid for witness, protocol, `bounded-retained`, or `conditional / support`. → `docs/repo/CONTROLLED_VOCABULARY.md §Evidence Terms`
- **companion** — evidence term: bounded supporting lane attached to a stronger package. → `docs/repo/CONTROLLED_VOCABULARY.md §Evidence Terms`
- **compute_required** — repair class: closure needs a completed long run, sliced runner, cached certificate, or independent derivation. Runner timeout alone is not evidence; it is a `compute_required` blocker. → [docs/audit/README.md](audit/README.md), [docs/audit/FRESH_LOOK_REQUIREMENTS.md §Long-running runner rule](audit/FRESH_LOOK_REQUIREMENTS.md)
- **conditional / support** — claim-strength label: useful positive package whose load-bearing step is still conditional, imposed, or support-only. → `docs/repo/CONTROLLED_VOCABULARY.md §Claim-Strength / Release Labels`
- **controlled_vocabulary.yaml** — (cleanup PR) machine-readable canonical source for all process vocabulary. Rendered docs (CV.md, KEY_TERMINOLOGY.md) regenerate from it; manual edits to rendered docs are not permitted. → `docs/repo/VOCABULARY_HYGIENE_DESIGN.md`
- **CONTROLLED_VOCABULARY.md** — the operational vocabulary layer (status taxonomies, claim-strength labels, audit-lane field enums, filename conventions, archival paths, topic language, prose voice). One layer below this index. → `docs/repo/CONTROLLED_VOCABULARY.md`
- **criticality** — graph-topology measure (`critical` / `high` / `medium` / `leaf`) set by transitive-descendant count, not by author-declared flagship status. Critical claims require cross-confirmation. → [docs/audit/FRESH_LOOK_REQUIREMENTS.md](audit/FRESH_LOOK_REQUIREMENTS.md)
- **cross-confirmation** — required second-auditor pass for `criticality: critical` claims before `audited_clean` lands. Disagreements promote to judicial third auditor or five-judge panel. → [docs/audit/FRESH_LOOK_REQUIREMENTS.md](audit/FRESH_LOOK_REQUIREMENTS.md)
- **cross_family** — `independence` tier: auditor model family differs from author's. The default cross-family auditor for this repo is the best available full Codex GPT model at maximum reasoning. → [docs/audit/FRESH_LOOK_REQUIREMENTS.md](audit/FRESH_LOOK_REQUIREMENTS.md)

## D

- **(D)** — load-bearing step class: external comparator check against PDG / lattice QCD / observation. → [docs/audit/AUDIT_AGENT_PROMPT_TEMPLATE.md](audit/AUDIT_AGENT_PROMPT_TEMPLATE.md)
- **decoration** — `claim_type` and `audit_status` value: algebraic consequence of a parent claim with no new comparator, compression, or structural integer. Not a separate retained row. → [docs/audit/ALGEBRAIC_DECORATION_POLICY.md](audit/ALGEBRAIC_DECORATION_POLICY.md)
- **dependency_not_retained** — repair class: direct dep exists but is not retained-grade. → [docs/audit/README.md](audit/README.md)
- **derivation class** — see *load-bearing step class*. → [docs/audit/AUDIT_AGENT_PROMPT_TEMPLATE.md](audit/AUDIT_AGENT_PROMPT_TEMPLATE.md)
- **derived** — claim-strength label: current-main downstream result from retained structure + named bridge/import assumptions. Safe to quote, but not the same as zero-input retained closure. → `docs/repo/CONTROLLED_VOCABULARY.md §Claim-Strength / Release Labels`
- **diagnostic** — evidence term: instrument / readout used for triage or debugging. → `docs/repo/CONTROLLED_VOCABULARY.md §Evidence Terms`

## E

- **(E)** — load-bearing step class: definition (introduces a new symbol). Triggers `audited_renaming`. → [docs/audit/AUDIT_AGENT_PROMPT_TEMPLATE.md](audit/AUDIT_AGENT_PROMPT_TEMPLATE.md)
- **effective_status** — pipeline-derived field; the publication-facing status computed from `claim_type` + `audit_status` + citation-graph dependency closure. Values include `retained`, `retained_no_go`, `retained_bounded`, `retained_pending_chain`, `open_gate`, `decoration_under_<parent>`, `meta`, `audited_<failure_mode>`. Do not write to this field directly. Does not factor `prose_status` — physics drives effective status; prose is recorded separately. → [docs/audit/README.md](audit/README.md)
- **external** — `independence` tier: off-repo reviewer with no project context. Only tier satisfying external-impact requirements; the audit lane does not produce these on its own. → [docs/audit/FRESH_LOOK_REQUIREMENTS.md](audit/FRESH_LOOK_REQUIREMENTS.md)

## F

- **(F)** — load-bearing step class: renaming (asserts symbol identity between two existing concepts). Triggers `audited_renaming`. → [docs/audit/AUDIT_AGENT_PROMPT_TEMPLATE.md](audit/AUDIT_AGENT_PROMPT_TEMPLATE.md)
- **Finding N** — canonical heading form for discrete findings inside a `claim_type: meta` audit-prep note: `### Finding N: <descriptive title>`. Explicit numbering with descriptive titles only; F-letter codes are forbidden. → `docs/repo/VOCABULARY_HYGIENE_DESIGN.md §Canonical structures for emerging needs`
- **fresh_context** — `independence` tier: same model family, different auditor/session identity, restricted-input audit. Same-family clean-room tier. → [docs/audit/FRESH_LOOK_REQUIREMENTS.md](audit/FRESH_LOOK_REQUIREMENTS.md)
- **frontier_*** — script filename prefix: active frontier or later-stage retained runners; the current default namespace. → `docs/repo/CONTROLLED_VOCABULARY.md §Filename Taxonomy`
- **frozen-out** — publication-capture disposition: intentionally excluded from the main paper while still recorded. → `docs/repo/CONTROLLED_VOCABULARY.md §Publication-Capture Dispositions`

## G

- **(G)** — load-bearing step class: numerical match at a tuned input scale. Triggers `audited_numerical_match`. → [docs/audit/AUDIT_AGENT_PROMPT_TEMPLATE.md](audit/AUDIT_AGENT_PROMPT_TEMPLATE.md)

## H

- **helper_runner_paths** — audit-ledger field: transitive set of helper `scripts/*.py` paths the audit packet must include alongside the primary runner. A non-empty list with a missing helper is a `runner_artifact_issue`, not a chain failure. → [docs/audit/AUDIT_AGENT_PROMPT_TEMPLATE.md](audit/AUDIT_AGENT_PROMPT_TEMPLATE.md)

## I

- **independence** — auditor independence tier (`weak`, `fresh_context`, `cross_family`, `strong`, `external`); enforces that author ≠ auditor. → [docs/audit/FRESH_LOOK_REQUIREMENTS.md](audit/FRESH_LOOK_REQUIREMENTS.md)

## K

- **KEY_TERMINOLOGY.md** — this file; the front-door A-Z index above the four governance layers in CONTROLLED_VOCABULARY.md's Vocabulary Hierarchy. (Cleanup PR: becomes a generated product of `controlled_vocabulary.yaml`.) → `docs/KEY_TERMINOLOGY.md`

## L

- **lattice_*** — script filename prefix: older major lattice program runners still on `main`. → `docs/repo/CONTROLLED_VOCABULARY.md §Filename Taxonomy`
- **load-bearing step** — the single sentence or equation in a source note that does the actual work; the step that, if removed, would break the chain from cited inputs to the conclusion. → [docs/audit/AUDIT_AGENT_PROMPT_TEMPLATE.md §4](audit/AUDIT_AGENT_PROMPT_TEMPLATE.md), [docs/audit/FRESH_LOOK_REQUIREMENTS.md](audit/FRESH_LOOK_REQUIREMENTS.md)
- **load-bearing step class** — one of `(A)` through `(G)` describing the kind of step the load-bearing sentence is. Determines the verdict gate. → [docs/audit/AUDIT_AGENT_PROMPT_TEMPLATE.md §4](audit/AUDIT_AGENT_PROMPT_TEMPLATE.md)

## M

- **main closure package** — claim-strength label: package-level main-paper closure claim; stronger than support, not automatically the retained quantitative paper core. → `docs/repo/CONTROLLED_VOCABULARY.md §Claim-Strength / Release Labels`
- **meta** — `claim_type` value: non-claim infrastructure rows (audit-prep notes, synthesis catalogues, fix-records). Cannot promote to non-meta `claim_type` via re-classification. Filename suffix for `meta` notes must be a plain `_NOTE_<YYYY-MM-DD>.md`; new suffixes are forbidden. → [docs/audit/README.md](audit/README.md), `docs/repo/CONTROLLED_VOCABULARY.md §Science Naming Rules`
- **mirror_*** — script filename prefix: older mirror-program runners still on `main`. → `docs/repo/CONTROLLED_VOCABULARY.md §Filename Taxonomy`
- **missing_bridge_theorem** — repair class: claim needs a new theorem for a physical carrier, readout, unit map, boundary condition, sector choice, normalization, or observable bridge. → [docs/audit/README.md](audit/README.md)
- **missing_dependency_edge** — repair class: a needed source note or authority exists or is named, but is not wired as a direct dependency for the audited claim. → [docs/audit/README.md](audit/README.md)

## N

- **needs_human_vocab_decision** — `prose_status` value: vocabulary drift detected but `vocab_lint` could not mechanically rewrite it (genuinely new term). Does not block physics verdict; queues for periodic vocab-extension review. → `docs/repo/VOCABULARY_HYGIENE_DESIGN.md`
- **not_evaluated_pre_vocab_lint** — `prose_status` value: pre-Cleanup-1 row, newly seeded row, or source-drift row not yet linted under the new rules. Seeder/backfill default; cleared when the row is next linted. → `docs/repo/VOCABULARY_HYGIENE_DESIGN.md`
- **no_go** — `claim_type` value: negative result that closes off otherwise-tempting alternative routes. Can earn `effective_status: retained_no_go` after clean audit. No-go verdicts require the No-Go Discipline gate (N1-N8 checks) before recording. → [docs/audit/README.md](audit/README.md), [docs/ai_methodology/skills/no-go-discipline/SKILL.md](ai_methodology/skills/no-go-discipline/SKILL.md)
- **no_go_discipline.status** — structured N1-N8 gate outcome: `PASS` only when every required record closes with no unresolved item; otherwise `FAIL`, which forbids `audited_clean`. → [docs/ai_methodology/skills/no-go-discipline/SKILL.md](ai_methodology/skills/no-go-discipline/SKILL.md), `docs/repo/CONTROLLED_VOCABULARY.md §Audit Lane Field Vocabulary`
- **no_go_discipline.demotion** — required conservative disposition for a failed no-go gate: `partial-attempt-with-named-untested-routes`, `partial-narrowing`, `bounded-with-corrected-wall-count`, or `stretch-attempt-with-honest-residual`. → [docs/ai_methodology/skills/no-go-discipline/SKILL.md](ai_methodology/skills/no-go-discipline/SKILL.md), `docs/repo/CONTROLLED_VOCABULARY.md §Audit Lane Field Vocabulary`
- **no_go_discipline_packet_missing** — controlled invalidation reason: a clean negative-boundary audit predates the structured N1-N8 packet and must return to fresh audit before remaining authoritative. → [docs/audit/scripts/invalidate_stale_audits.py](audit/scripts/invalidate_stale_audits.py), `docs/repo/CONTROLLED_VOCABULARY.md §Audit Lane Field Vocabulary`
- **note_hash** — audit-ledger field: SHA of source note at time of audit. Note edits auto-reset the row to `unaudited` and require re-audit. → [docs/audit/FRESH_LOOK_REQUIREMENTS.md](audit/FRESH_LOOK_REQUIREMENTS.md)
- **notes_for_re_audit_if_any** — audit-ledger field for `audited_conditional`. Must be prefixed with exactly one repair class (`missing_dependency_edge`, `dependency_not_retained`, `missing_bridge_theorem`, `scope_too_broad`, `runner_artifact_issue`, `compute_required`, `other`). → [docs/audit/README.md](audit/README.md)

## O

- **observational-pin** — compound adjective for an observational anchor. The noun form is `observational pin` (no hyphen). → `docs/repo/CONTROLLED_VOCABULARY.md §Hyphenation`
- **open** — publication-capture disposition: live gate / blocker not yet closed. → `docs/repo/CONTROLLED_VOCABULARY.md §Publication-Capture Dispositions`
- **open_gate** — `claim_type` and `effective_status` value: clean open gate; blocks retained propagation downstream. → [docs/audit/README.md](audit/README.md)
- **open main gate** — claim-strength label: still-open main closure target. → `docs/repo/CONTROLLED_VOCABULARY.md §Claim-Strength / Release Labels`
- **other** — repair class: catch-all when none of the six specific classes fit; must state why. → [docs/audit/README.md](audit/README.md)

## P

- **positive_theorem** — `claim_type` value: derived positive result. Can earn `effective_status: retained` after clean audit + retained-grade deps. → [docs/audit/README.md](audit/README.md)
- **primary_break_target** — audit-queue field: the node in a citation cycle designated for audit-induced cycle-break. → [docs/audit/AUDIT_QUEUE.md](audit/AUDIT_QUEUE.md), `docs/audit/data/audit_queue.json`
- **promoted** — publication-capture disposition: main-paper publication-core family carried in the current paper package. → `docs/repo/CONTROLLED_VOCABULARY.md §Publication-Capture Dispositions`
- **promoted quantitative package** — claim-strength label: quantitative package strong enough for the current main-paper surface. → `docs/repo/CONTROLLED_VOCABULARY.md §Claim-Strength / Release Labels`
- **proposed_promoted** — author-side migration value on source-note `Status` lines; awaits audit ratification before becoming `promoted` via `effective_status`. → [README.md "Audit status note"](../README.md), `docs/repo/CONTROLLED_VOCABULARY.md §Migration / Legacy Wording`
- **proposed_retained** — author-side migration value on source-note `Status` lines; awaits audit ratification before becoming `retained` via `effective_status`. → [README.md "Audit status note"](../README.md), `docs/repo/CONTROLLED_VOCABULARY.md §Migration / Legacy Wording`
- **prose_corrections** — audit-ledger field: list of `(rule_id, before, after)` tuples recording mechanical rewrites applied by `vocab_lint --fix` during the audit. → `docs/repo/VOCABULARY_HYGIENE_DESIGN.md`
- **prose_status** — audit-ledger field: one of `clean`, `auto_corrected`, `needs_human_vocab_decision`, `not_evaluated_pre_vocab_lint`, `queue_backpressure_exceeded`. Separate from `audit_status`; physics and prose verdicts never conflate. → `docs/repo/VOCABULARY_HYGIENE_DESIGN.md`
- **protocol** — evidence term: specific constructed experimental / computational setup. → `docs/repo/CONTROLLED_VOCABULARY.md §Evidence Terms`
- **pruning** — decoration handling: removing a decoration cluster entirely when all four conditions hold (>10 members, no `(D)` checks, no load-bearing usage by non-decoration claims, no external citations). → [docs/audit/ALGEBRAIC_DECORATION_POLICY.md](audit/ALGEBRAIC_DECORATION_POLICY.md)

## Q

- **queue_backpressure_exceeded** — `prose_status` value: vocab-extension review queue is >50 entries deep; new unresolved terms emit this until the queue is processed. → `docs/repo/VOCABULARY_HYGIENE_DESIGN.md`

## R

- **repair class** — see `notes_for_re_audit_if_any`. One of `missing_dependency_edge`, `dependency_not_retained`, `missing_bridge_theorem`, `scope_too_broad`, `runner_artifact_issue`, `compute_required`, `other`. → [docs/audit/README.md](audit/README.md)
- **retained** — three meanings, all auditor-ratified, never author-declared: (a) publication-capture disposition for the live retained family; (b) claim-strength label family (`retained corollary`, `retained support theorem`, etc.); (c) `effective_status` value for a clean `positive_theorem` plus retained-grade deps. Source notes use `proposed_retained` until audit ratifies. → [docs/audit/README.md](audit/README.md), `docs/repo/CONTROLLED_VOCABULARY.md`
- **retained_bounded** — `effective_status` value: clean `bounded_theorem` + retained-grade deps. → [docs/audit/README.md](audit/README.md)
- **retained_no_go** — `effective_status` value: clean `no_go` + retained-grade deps. → [docs/audit/README.md](audit/README.md)
- **retained_pending_chain** — `effective_status` value: clean theorem/no-go/bounded row whose upstream chain is not yet retained-grade. Does not propagate retained status downstream. → [docs/audit/README.md](audit/README.md)
- **runner_artifact_issue** — repair class: runner, log, classifier, threshold, import, or pass/fail accounting problem blocks closure despite otherwise local scope. → [docs/audit/README.md](audit/README.md)

## S

- **salvage note** — required artifact when a wrapper note fails an audit but some sub-observations survive. States what failed, what survived, and the wrapper's archive recovery path. Must not restate the failed global conclusion. → [docs/audit/STALE_NARRATIVE_POLICY.md](audit/STALE_NARRATIVE_POLICY.md)
- **scope_too_broad** — repair class: a clean bounded core exists, but the current claim scope includes an unclosed extension. → [docs/audit/README.md](audit/README.md)
- **strong** — `independence` tier: human auditor with no prior involvement in the note. → [docs/audit/FRESH_LOOK_REQUIREMENTS.md](audit/FRESH_LOOK_REQUIREMENTS.md)
- **support** — **not a claim class.** Legacy source-note prose only; once a note has an `audited_clean` verdict, retention follows from `claim_type` + dependency closure, not from "support" labelling. → [docs/audit/README.md](audit/README.md)

## U

- **unaudited** — `audit_status` value: row has not been audited yet. → [docs/audit/README.md](audit/README.md)

## V

- **verdict** — the `audit_status` value chosen by the auditor. Audit-loop ties between `audited_clean` and any non-clean verdict are broken in favour of the non-clean choice. → [docs/audit/AUDIT_AGENT_PROMPT_TEMPLATE.md §7 Tie-breaking](audit/AUDIT_AGENT_PROMPT_TEMPLATE.md)
- **vocab_lint** — (cleanup PR) `scripts/vocab_lint.py`; mechanical pre-commit linter that detects vocabulary drift and applies canonical rewrites via `--fix`. Integrated into audit-loop, review-loop, physics-loop. → `docs/repo/VOCABULARY_HYGIENE_DESIGN.md §Auto-correct mechanism`

## W

- **wave_*** — script filename prefix: older wave-program runners still on `main`. → `docs/repo/CONTROLLED_VOCABULARY.md §Filename Taxonomy`
- **weak** — `independence` tier: same model family or context restrictions cannot be established. Permitted for diagnostic review, not eligible to land `audited_clean`. → [docs/audit/FRESH_LOOK_REQUIREMENTS.md](audit/FRESH_LOOK_REQUIREMENTS.md)
- **witness** — evidence term: bounded positive signal on a stated protocol. Use *only* when the protocol is stated; do not upgrade to `proof` or `closure`. → `docs/repo/CONTROLLED_VOCABULARY.md §Evidence Terms`

---

## Adding new terms (agent pacing)

Routine vocabulary drift (legacy aliases, deprecated wording, forbidden
filename suffixes) is **auto-corrected** by `vocab_lint --fix` running
inside audit-loop / review-loop / physics-loop. Agents do not open PRs
for routine rewrites.

Genuinely new vocabulary requirements (terms `vocab_lint` cannot
mechanically rewrite) surface as `prose_status:
needs_human_vocab_decision` on the audit row. They do not block the
physics verdict. They batch into a periodic vocab-extension review:
either (a) accepted, with a PR against
[`docs/repo/controlled_vocabulary.yaml`](repo/controlled_vocabulary.yaml)
and a regenerated CV.md + KEY_TERMINOLOGY.md (regeneration ships in
Cleanup-1b), or (b) rejected, with a `--fix` sweep replacing the new
term with the canonical form.

See `docs/repo/VOCABULARY_HYGIENE_DESIGN.md`
for the full design.

## Forbidden patterns

- **Physics primitives** in this index or in CONTROLLED_VOCABULARY.md.
  Vocabulary is disjoint from physics. Physics primitives live in
  MINIMAL_AXIOMS / per-claim notes.
- **"legacy alias: X"** anywhere on live science surfaces. Aliasing
  rots; use the canonical name only.
- **New filename suffixes** for `claim_type: meta` notes
  (`_HOSTILE_AUDIT_FINDINGS_NOTE_`, `_DOWNSTREAM_FIX_NOTE_`,
  `_FIX_RECORD_`, `_FINDINGS_MEMO_`, `_ADDENDUM_`, etc.). Use plain
  `_NOTE_<YYYY-MM-DD>.md`.
- **F-letter / coded finding labels** inside notes (`### F-A —`,
  `### F-B —`, etc.). Use `### Finding N: <descriptive title>` with
  explicit numbering.
- **New finding-class names** (`framing-fix`, `routing correction`,
  `tier over-claim`, `admission-inheritance`, `audit-prep input`).
- **New repair-class names** beyond the seven listed under *repair
  class* above.
- **Audit verdicts that conflate physics with prose.** Use
  `audit_status` for physics, `prose_status` for vocab. The two are
  separate fields by construction; `prose_status` does not propagate
  into `effective_status`.

See `docs/repo/VOCABULARY_HYGIENE_DESIGN.md §Forbidden patterns`
for the binding list. The cleanup PR mechanically removes any
remaining instances.
