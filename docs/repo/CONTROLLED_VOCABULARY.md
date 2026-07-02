<!-- generated; do not edit by hand; source: docs/repo/controlled_vocabulary.yaml hash=d0fcd0cff651e8c0141f8fa7836d927de738e81104945743381654e129817352 -->
# Controlled Vocabulary

> **Front-door lookup:** Looking up a single term? Go to
> `docs/KEY_TERMINOLOGY.md` — flat A-Z index of
> every repo-canonical term with one-line definition and a pointer to
> the source-of-truth doc for each.

## Vocabulary Hierarchy

The repo has five language layers. This doc is the **operational** layer
(layer 3). Higher layers are sovereign for their domains; do not duplicate
their content here, and do not override their wording from here.

| Layer | Source-of-truth doc | Governs |
|---|---|---|
| 0. Front-door A-Z lookup | `docs/KEY_TERMINOLOGY.md` | Single-page A-Z index of every repo-canonical term with a one-line definition and a pointer to its source-of-truth doc. The reader entry-point above all layers below; an index, not an authority. New terms enter the index only after the source-of-truth doc accepts them. |
| 1. Framework substantive | `docs/MINIMAL_AXIOMS_2026-06-29.md` and `docs/audit/data/axiom_premise_nodes.json` | Framework axioms and explicitly approved primitive premise nodes the operational vocabulary uses: Lattice (`Z^3` with nearest-neighbor adjacency, standard translations, and proper cubic rotations), Qubit (the domain of local possibilities with full one-site algebraic presentation `M_2(ℂ)`; `Cl(3,0)` is equivalent notation, not extra primitive content; no possibility is privileged), Admissibility (one fixed nearest-neighbor rule, covariant under lattice translations and proper cubic rotations, by which the available possibilities are determined by, and vary with, the nearest-neighbor conditions at each site), Record (optional fixed locking of one available local possibility; readout value determined by record content alone; finite scalar additivity), the state/law qualification clauses, the definition of `A_min`, the status of prior `A3` / `A4` / `A5` as open gates rather than axioms, and registered primitive premise nodes such as the scale-reference and kinetic-isotropy primitives. Changes only when a framework-level science decision changes. |
| 2. External paper text | [`docs/ai_methodology/CANONICAL_FRAMING_PARAGRAPH_2026-04-25.md`](../ai_methodology/CANONICAL_FRAMING_PARAGRAPH_2026-04-25.md), [`docs/ai_methodology/AI_ACCOUNTABILITY_AND_DISCLOSURE_NOTE_2026-04-25.md`](../ai_methodology/AI_ACCOUNTABILITY_AND_DISCLOSURE_NOTE_2026-04-25.md) | Verbatim reusable disclosure paragraphs for papers, preprints, and talks. The framing paragraph is the short paper-facing form; the accountability disclosure is the longer package-level form. Both carry their own usage guidance (e.g. replacing `[repo URL]`, narrowing the tool list when only one was used). |
| 3. Operational (this doc) | `docs/repo/CONTROLLED_VOCABULARY.md` | Status taxonomy, claim-strength labels, audit-lane field enums, repair classes, filename conventions, archival paths, topic language, and paper-facing prose voice — the working vocabulary used inside the repo across ledgers, tables, notes, runners, skills, and PR descriptions. |
| 4. Methodology framing (adjacent) | `docs/AI_METHODOLOGY_NOTE_2026-04-25.md` | The curated front-door note for the methodology lane. Defines how to talk about the AI / methodology side at the project level. |

For a single-term lookup (layer 0), use `KEY_TERMINOLOGY.md`. For
framework axioms and approved primitive premise nodes (layer 1), cite
`MINIMAL_AXIOMS_2026-06-29.md` and
`docs/audit/data/axiom_premise_nodes.json` — do not redefine Lattice, Qubit,
Admissibility, Record, `Cl(3)`, `Z^3`, `A_min`, or registered primitives here. For external paper text
(layer 2), use the canonical framing paragraph and the accountability
disclosure verbatim — do not paraphrase. This doc governs layer 3 only.

---

This file is the single repo-wide home for the **operational** vocabulary
layer: status taxonomy, audit-lane field enums, filename conventions,
axiom-naming **rules** (above the science decision in layer 1), archival
paths, topic language, and paper-facing prose voice. Other policy /
process docs in the repo cite this file for vocab rather than inlining
their own. If a sanctioned term, label, suffix, or wording is not listed
here and is not defined in the layer 1 or layer 2 sources above, it does
not exist for repo purposes — vocabulary additions require a PR against
this file before any note, runner, ledger row, status badge, or PR
description that uses them.

Goals:

- one taxonomy home for matrix / ledger / atlas / review / note / runner / script
  language
- separate publication-capture decisions from theorem-strength labels
- separate authoring vocabulary from audit-lane field enums
- avoid vague shorthand on live package surfaces
- prefer explicit protocol qualifiers over loose adjectives
- forbid new tags / classes / meta-framings on `claim_type: meta` notes
  and elsewhere; emergent vocabulary is a substantive defect even when
  the per-claim content is correct

## Vocabulary Families

There are five status families in this repo. Do not mix them casually.

1. publication-capture dispositions
2. claim-strength / release labels
3. audit-lane field vocabulary (claim_type / audit_status /
   effective_status / repair classes / independence tiers)
4. historical lane-board labels
5. historical discovery-log labels

If a file already has separate columns for `Status`, `Qualifier`, `Import
class`, or `Current publication decision`, keep one family per column
rather than collapsing everything into one hybrid phrase.

## Science Naming Rules

Landed science must use domain-explicit names. Do not introduce a bare
letter-number or route code as the primary name of a theorem, lane, source
note, runner headline, table row, or review finding when that code could also
mean an axiom, assumption, algebra type, branch block, route number, or
workstream index.

Examples of ambiguous primary names to avoid on new landed surfaces:

- `A1`, `A2`, `G1`, `R3`
- `Route F`, `Block 2`, `Origin B`
- `Step 1` or `Assumption 1` compressed to `S1` / `A1`

Use the scientific object as the name instead:

- `physical Cl(3) local algebra`, not bare `A1`
- `Lattice`, not bare `A2`
- `Koide Frobenius-equipartition condition`, not bare `A1`
- `Lie type A_1` or `SU(2) root-system check`, not bare `A1`
- `DM-eta Coleman-Weinberg residual`, not bare `G1`

**Canonical mathematical-object names are allowed.** Bare letter-number
forms that name an *established mathematical object* — `S^3` (3-sphere),
`S^2` (2-sphere), `U(1)` and `SU(N)` (gauge groups), `Z_3` / `Z_n`
(cyclic groups), `C_3` (cyclic / symmetry group), `A_n` / `D_n` /
`E_n` (Lie types), `I_3` (third isospin component), etc. — are the
canonical names for those objects and do not require domain-explicit
expansion. The rule above targets *code-like primary names that don't
reference an established mathematical object* (e.g. `A1` used as a
workstream label, `G1` used as a route code, `R3` used as a routing
index), not standard mathematical notation. If both readings are
plausible in context (e.g. `A_1` as Lie type vs. `A1` as
workstream-index abbreviation), spell out the mathematical reading
on first use (`Lie type A_1`) so the bare form is unambiguous.

Legacy shorthand may be preserved only as an alias after the explicit name,
for example: `Koide Frobenius-equipartition condition (legacy alias: A1)`.
If an existing file already uses a shorthand, new edits should define it on
first use and prefer the explicit name in headings, metadata, claim scopes,
review summaries, and publication/control-plane rows.

Axioms and assumptions must be written out as `Axiom 1`, `Assumption 1`, or a
descriptive premise name. Do not abbreviate them to `A1` on live science
surfaces.

### Meta-note vocabulary discipline

`claim_type: meta` notes (audit-prep, synthesis, fix-record, infrastructure
documentation) must use a plain `_NOTE_<YYYY-MM-DD>.md` filename suffix
and repo-canonical vocabulary in their content. The following emergent
patterns are vocabulary additions and forbidden until they appear in this
file:

- new filename suffixes such as `_HOSTILE_AUDIT_FINDINGS_NOTE_`,
  `_DOWNSTREAM_FIX_NOTE_`, `_SURGICAL_FIX_RECORD_`, `_FINDINGS_MEMO_`,
  `_FIX_RECORD_`, `_AUDIT_BRIEF_`, `_ADDENDUM_`
- new within-note labelling schemes such as `F-A` / `F-B` / `F-C`
  "Finding F-letter" headings
- new finding-class names such as `framing-fix`, `routing correction`,
  `tier over-claim`, `admission-inheritance`, `audit-prep input`
- new authority-role phrases such as
  `Status authority: independent audit lane only` as a load-bearing role
- new repair-class names beyond the seven listed in "Audit Lane Field
  Vocabulary" below
- new "X is a Y" meta-framings that imply a class or parent-framing
  cross-reference for a collection of not-yet-shipped sub-PRs

The reviewer rejects custom tags / classes / meta-framings even when the
underlying per-claim work is correct. Ship narrow content one identity at a
time, mirroring an existing canonical template, with no new vocabulary.

## Filename Taxonomy

### Script filename prefixes

- `frontier_*`
  - active frontier or later-stage retained runners
  - this is the current default namespace
- `mirror_*`, `lattice_*`, `gate_b_*`, `source_resolved_*`, `wave_*`
  - older major programs that are still important on `main`
- everything else
  - usually lane-specific historical or exploratory runners

Lane-specific prefixes are preferred when creating new frontier runners:
`frontier_staggered_*`, `frontier_two_field_*`, `frontier_emergent_geometry_*`,
etc. Pick a prefix that names the lane, not the date or the author.

### Note filename rules

- New retained notes should be explicit about the runner they interpret
  in the filename when feasible.
- New strategy or synthesis notes should not silently replace retained
  notes; if the synthesis is forward-looking it lands at
  `claim_type: meta` with the `_NOTE_<YYYY-MM-DD>.md` plain suffix.
- Historical lanes should not be renamed just to fit the current
  taxonomy. They should be indexed in the lane board and registry
  instead. If a lane is historical, mark that in the lane board and
  registry rather than renaming dozens of files.

### Reserved filename suffixes

See "Meta-note vocabulary discipline" above for the list of forbidden
emergent suffixes. The only sanctioned form for new audit-prep / meta
notes is `<DOMAIN>_NOTE_<YYYY-MM-DD>.md`.

## Publication-Capture Dispositions

Use these on publication-control-plane surfaces such as
`PUBLICATION_MATRIX.md`.

| Label | Use |
|---|---|
| `retained` | live retained family on the current paper-authority surface |
| `promoted` | main-paper publication-core family carried directly in the current paper package |
| `bounded` | live captured family kept outside the main paper core with explicit caveats |
| `open` | live gate / blocker that is not yet closed |
| `frozen-out` | intentionally excluded from the main paper while still recorded |

These are package-capture decisions, not generic adjectives.

## Claim-Strength / Release Labels

Use these on notes, claims tables, quantitative tables, and runner summaries.

| Label | Use |
|---|---|
| `retained` | theorem-grade closure on the retained authority surface |
| `derived` | current-main downstream result obtained from retained structure plus named bridge/import assumptions; safe to quote, but not the same as zero-input retained closure |
| `retained corollary` | safe retained consequence of a retained theorem/action surface |
| `retained support theorem` / `retained support` | exact retained support result that is reusable but not itself the manuscript headline |
| `retained support batch` | coherent retained batch of support theorems/tools carried together for atlas, reviewer, or support-package reuse |
| `retained exact theorem` / `retained exact companion` | exact retained theorem/companion variant used when exactness itself is part of the safe statement |
| `retained structural theorem` / `retained exact structural theorem` | retained exact structural law on the framework/package surface |
| `retained support tool` | reusable retained tool/subderivation that supports other lanes without itself being the manuscript headline |
| `retained framework statement` / `retained positioning` / `retained quantitative lane` | retained package-authority framing labels for front-door/control-plane use |
| `retained action-surface closure` / `retained restricted theorem` / `retained restricted support` / `retained evaluated theorem` | retained exact-result variants where the constrained surface/class/evaluation matters |
| `retained positive` / `retained partial positive` | retained positive lane result used mainly on atlas/toolbox surfaces rather than as the headline theorem |
| `exact support theorem` / `exact support` | accepted exact-support variant when exactness itself is material to the safe statement; use with the same non-headline semantics as retained support, and keep bridge/import qualifiers explicit |
| `exact support batch` | coherent exact batch of support theorems/tools carried together for atlas or reviewer reuse |
| `exact structural theorem` / `exact algebraic identity` / `exact subderivation` | accepted exact-result specializations for atlas / theorem-bank rows when the mathematical role matters |
| `exact boundary theorem` / `exact reduction theorem` | accepted exact-result specializations for atlas / theorem-bank rows when the mathematical role is an open-lane boundary or a compression/reduction statement |
| `exact current-stack theorem` / `exact current-bank theorem` / `exact current-bank reduction` / `exact current-bank no-go theorem` | accepted exact-result specializations for current-stack/current-bank closeout rows on atlas and reviewer surfaces |
| `exact negative boundary` / `exact negative closeout` / `exact post-selector reduction` | accepted exact-result specializations for explicit no-go/closeout/post-selector roles on atlas and reviewer surfaces |
| `exact support/boundary theorem` | accepted mixed exact-role label when a row simultaneously contributes a reusable exact support input and an exact open-lane boundary statement |
| `exact support tool` | reusable exact tool/subderivation that supports other lanes without being the headline claim |
| `bounded support theorem` / `bounded support note` / `bounded support tool` | bounded supporting result/tool carried for atlas, reviewer, or secondary-lane use; not a main closure claim |
| `bounded support batch` | coherent bounded batch of support tools/calculations carried for atlas or reviewer reuse |
| `promoted quantitative package` | quantitative package strong enough for the current main-paper surface |
| `bounded companion` | live bounded supporting lane outside the main paper core |
| `bounded secondary lane` | live bounded lane worth carrying, but clearly secondary to the main package |
| `bounded frontier` / `bounded negative boundary` / `bounded Route 2 build candidate` | bounded frontier/result classes kept for ongoing design work rather than current-package promotion |
| `main closure package` | package-level main-paper closure claim on the current review/package surface; stronger than support, but not automatically the retained quantitative paper core |
| `conditional` / `support` | useful positive package whose load-bearing step is still conditional, imposed, or support-only |
| `open main gate` | still-open main closure target |
| `historical` / `diagnostic` | preserved for audit/history/instrumentation, not live evidence |
| `historical support` / `provenance` / `exact transport provenance` | provenance-only rows kept for route history, reviewer handoff, or closure bookkeeping rather than live promotion |
| `negative-result` | useful negative or no-go result |
| `negative-result` / `support` | negative/no-go result that is also a reusable support/pruning surface |
| `inconclusive` | signal exists but interpretation is not frozen |

Allowed composite forms should be built from the labels above and kept narrow:

- `retained exact theorem`
- `retained exact companion`
- `retained structural theorem`
- `retained exact structural theorem`
- `retained corollary`
- `retained support theorem`
- `retained support batch`
- `retained support tool`
- `exact support theorem`
- `exact support batch`
- `exact structural theorem`
- `exact algebraic identity`
- `exact subderivation`
- `exact boundary theorem`
- `exact reduction theorem`
- `exact current-stack theorem`
- `exact current-bank theorem`
- `exact current-bank reduction`
- `exact current-bank no-go theorem`
- `exact negative boundary`
- `exact negative closeout`
- `exact post-selector reduction`
- `exact support/boundary theorem`
- `exact support tool`
- `bounded support theorem`
- `bounded support note`
- `bounded support tool`
- `bounded support batch`
- `bounded companion prediction`
- `bounded frontier`
- `bounded negative boundary`
- `bounded Route 2 build candidate`
- `main closure package`
- `promoted quantitative package`
- `open main gate`

Avoid minting new slash-composites when a nearby qualifier/import column can carry the caveat instead.

Role-specialized variants are acceptable when the cell begins with one of the
accepted base labels above and the trailing noun names the mathematical role
or control-plane role of the row, for example:

- `retained framework statement`
- `retained quantitative lane`
- `retained action-surface closure`
- `retained restricted theorem`
- `exact structural theorem`
- `exact algebraic identity`
- `exact subderivation`
- `retained support tool`
- `retained support batch`
- `exact support tool`
- `exact support batch`
- `exact boundary theorem`
- `exact reduction theorem`
- `exact current-stack theorem`
- `exact current-bank theorem`
- `exact current-bank no-go theorem`
- `exact negative boundary`
- `exact negative closeout`
- `exact post-selector reduction`
- `historical support / provenance`

Do not mix a publication-capture disposition with a claim-strength label in
the same cell unless the file explicitly allows hybrid narrative decisions.

Short scope qualifiers may follow an accepted label when they state where the
claim lives, for example:

- `exact boundary theorem on open gate`
- `exact reduction theorem outside main core`
- `exact support theorem on the bounded charged-lepton package`
- `exact support theorem with bounded downstream reuse`
- `retained support theorem on the current package surface`

Do not use `reviewed` or `reviewer-tested` as status labels. Those are review
process adjectives, not controlled-vocabulary claim-strength labels. Carry
review context in prose, placement, or authority notes instead.

## Audit Lane Field Vocabulary

These enums govern the audit ledger rows in
`docs/audit/data/audit_ledger.json`, the rendered surface
`docs/audit/AUDIT_LEDGER.md`, and the audit pipeline's derived outputs.
Authors may write whatever status prose they need inside source notes,
but the retained library is driven only by these auditor-owned fields.
The audit-lane process and workflows live in `docs/audit/README.md`,
`docs/audit/FRESH_LOOK_REQUIREMENTS.md`, and the audit-loop skill; the
enums themselves live here.

### `claim_type` (auditor-set)

What kind of object the auditor says the row is. Exactly one of:

- `positive_theorem`
- `bounded_theorem`
- `no_go`
- `open_gate`
- `decoration`
- `meta`

`meta` is used for non-claim infrastructure rows (audit-prep notes,
synthesis catalogues, infrastructure documentation). `meta` rows must
not promote to non-meta claim types via re-classification — these notes
are by design out-of-band.

### `claim_scope` (auditor-set)

The auditor's short, citeable statement of exactly what was audited.
Required for applied audits. Prose, not enum.

### `audit_status` (auditor-set)

What the audit found. Exactly one of:

- `unaudited`
- `audit_in_progress`
- `audited_clean`
- `audited_renaming`
- `audited_conditional`
- `audited_decoration`
- `audited_failed`
- `audited_numerical_match`

### `effective_status` (derived by pipeline)

Publication-facing status derived from `claim_type` plus
`audit_status` plus the citation-graph closure of dependencies. The
pipeline computes this; do not write to it directly. Possible values:

- `retained` — `claim_type = positive_theorem` plus
  `audit_status = audited_clean` plus retained-grade dependencies
- `retained_no_go` — `claim_type = no_go` plus
  `audit_status = audited_clean` plus retained-grade dependencies
- `retained_bounded` — `claim_type = bounded_theorem` plus
  `audit_status = audited_clean` plus retained-grade dependencies
- `retained_pending_chain` — clean theorem/no-go/bounded row whose
  upstream chain is not yet retained-grade
- `open_gate` — clean open gate; blocks retained propagation
- `decoration_under_<parent_claim_id>` — audited decoration whose
  parent is retained-grade
- `meta` — non-claim infrastructure rows
- `audited_<failure_mode>` — terminal non-clean audit verdicts on active
  claims

Generated audit data must not contain legacy source-status authority
fields. The graph builder may use old source-note status prose as a
one-way migration hint when seeding `claim_type`, but the ledger, queue,
prompt, and rendered audit surfaces are
`claim_type` / `audit_status` / `effective_status` only. `support` is
not a claim class.

### Conditional repair classes

For every `audited_conditional` result, the auditor must make the next
repair lane sortable by prefixing `notes_for_re_audit_if_any` with
exactly one of these seven classes:

- `missing_dependency_edge` — a needed source note or authority exists
  or is named, but is not wired as a direct dependency for the audited
  claim
- `dependency_not_retained` — a direct dependency exists but is not
  retained grade
- `missing_bridge_theorem` — the claim needs a new theorem for a
  physical carrier, readout, unit map, boundary condition, sector
  choice, normalization, or observable bridge
- `scope_too_broad` — a clean bounded core exists, but the current claim
  scope includes an unclosed extension
- `runner_artifact_issue` — a runner, log, classifier, threshold,
  import, or pass/fail accounting problem blocks closure despite
  otherwise local scope
- `compute_required` — closure needs a completed long run, sliced
  runner, cached certificate, or independent derivation
- `other` — use only when none of the above fits, and state why

After the class, the auditor names the cheapest next repair action.

### Independence tiers

`auditor` must not equal `author`. Strength tiers for the `independence`
field on an audit row:

- `independence: weak` — same model family, or a session whose context
  restrictions cannot be established. Permitted for diagnostic review,
  not eligible to land `audited_clean`
- `independence: fresh_context` — same model family, different
  auditor/session identity, restricted-input audit. Same-family
  clean-room tier for detecting context poisoning without claiming
  cross-family review
- `independence: cross_family` — different model family from the author
- `independence: strong` — human auditor with no prior involvement in
  the note
- `independence: external` — off-repo reviewer with no project context;
  the audit lane does not produce these on its own

### `auditor_family`

The model family of the auditor (e.g., `codex-gpt-5.5`, `codex-gpt-5.6`,
`claude-opus-4.x`, `human`). Used to enforce cross-family independence.
The designated cross-family auditor for this repo is the best available
full Codex GPT model at maximum reasoning; see
`docs/audit/FRESH_LOOK_REQUIREMENTS.md` for the auto-selection rule.

### Load-bearing step classes

When the auditor records the kind of step the load-bearing sentence /
equation is, pick exactly one of:

- `(A)` algebraic identity check on existing inputs
- `(B)` cross-note input verification (reads value from another note)
- `(C)` first-principles compute from the axiom (`Cl(3)` on `Z^3` plus
  accepted normalizations) producing a number not present in any input
- `(D)` external comparator check against PDG / lattice QCD / observation
- `(E)` definition (introduces a new symbol)
- `(F)` renaming (asserts symbol identity between two existing concepts)
- `(G)` numerical match at a tuned input scale

## Migration / Legacy Wording

The repo is migrating from author-declared `retained` / `promoted`
language to the audit-lane propose / ratify vocabulary. Source-note
`Status` lines now use:

- `proposed_retained` — author proposes retained-grade; awaits audit ratification
- `proposed_promoted` — author proposes promoted-grade; awaits audit ratification

The canonical audit-ratified surface is
[docs/audit/AUDIT_LEDGER.md](../audit/AUDIT_LEDGER.md). Legacy
publication summaries may still use manuscript shorthand, but those rows
should be read as proposed until the audit ledger marks them clean.

New notes must use `proposed_retained` / `proposed_promoted` on author
side and rely on the pipeline's `effective_status` for the
publication-facing label. Do not bare-declare `retained` on a source
note.

## Historical Lane-Board Labels

Use these only on Historical repo-map surfaces such as `LANE_STATUS_BOARD.md` and the lane registry.

| Label | Use |
|---|---|
| `primary-retained` | current best-supported lane in the historical lane-board sense |
| `retained-companion` | real, replayable companion lane, but not the single default entrypoint |
| `open-blocker` | active blocker limiting the historical lane claim boundary |
| `exploratory-reopen` | partially positive lane worth more work, but not promoted |
| `historical-control` | historical comparison/control lane |
| `historical-retained` | older retained major program, no longer the default |
| `historical-bounded` | scientifically useful historical work, no longer the lead lane |
| `historical-blocked` | diagnosed dead-end or mechanism-level blocker |

## Historical Discovery-Log Labels

Use these only on Historical discovery / paper-seed ledgers such as `POTENTIAL_PUBLICATION_DISCOVERIES_LOG.md`.

| Label | Use |
|---|---|
| `retained` | historically important retained discovery |
| `bounded-retained` | bounded positive result preserved on `main`, worth paper planning, but not a retained theorem-grade closure |
| `methodological` | important measurement / methodology / audit contribution |
| `negative-result` | strong structural no-go or narrowing result |
| `exploratory-lead` | quantitatively interesting lead worth preserving, not yet frozen |

## Column Rules

- `PUBLICATION_MATRIX.md`
  - use publication-capture dispositions for capture decisions
  - `Current publication decision` cells should begin with one of `retained`, `promoted`, `bounded`, `open`, `frozen-out`; a short placement note may follow after a semicolon
- `CLAIMS_TABLE.md, QUANTITATIVE_SUMMARY_TABLE.md, DERIVATION_ATLAS.md`
  - use claim-strength / release labels
  - accepted role-specialized variants may be used when they begin with the primary claim-strength label
- `FULL_CLAIM_LEDGER.md`
  - may begin with either a publication-capture disposition or a claim-strength label because it narrates package decisions row-by-row
  - avoid ad hoc hybrids; if a row begins with one family, keep any second-family qualifier short and explanatory
  - on mixed audit rows, the cell should begin with the primary label from the family being used; a short explanatory qualifier may follow after a semicolon
  - accepted ledger-style hybrids include forms such as `promoted exact companion`, `promoted restricted theorem`, `promoted retained closure`, `promoted retained support batch`, and `promoted retained action-surface closure`
- `docs/audit/AUDIT_LEDGER.md, docs/audit/data/audit_ledger.json`
  - use audit-lane field vocabulary only
  - rows are written by the audit pipeline / `apply_audit.py`; do not hand-edit
- `LANE_STATUS_BOARD.md`
  - use historical lane-board labels
- `POTENTIAL_PUBLICATION_DISCOVERIES_LOG.md`
  - use historical discovery-log labels

Do not use row prose like `Retained ...` when the row status is `bounded-retained`.

## Protocol Qualifiers

These are qualifiers, not standalone status labels:

- `review surface`
- `current package grade`
- `strict/native map`
- `exact-target strict/native map`

They can appear in prose or qualifier/import columns, but they should not replace the primary status label.

## Evidence Terms

Prefer these nouns:

- `protocol`: a specific constructed experimental/computational setup
- `witness`: a bounded positive signal on a stated protocol
- `diagnostic`: an instrument/readout used for triage or debugging
- `companion`: a bounded supporting lane attached to a stronger package
- `closure`: use only when the load-bearing claim is actually closed

Avoid vague upgrades like:

- `proof` when the surface is only a witness or protocol
- `closure` when the status is really `bounded-retained` or `conditional / support`

## Hyphenation

- prefer `observational-pin as a compound adjective`
- prefer `observational pin only as a noun phrase`

## Axiom Naming (out of scope for this doc)

Axiom names (`A_min`, `Axiom 1`, `Axiom 2`, `Axiom*`) are **physics
primitives**, not process vocabulary. Per
`VOCABULARY_HYGIENE_DESIGN.md`, vocabulary
is disjoint from physics. The canonical home for these names and the
policy governing their use is:

- `docs/MINIMAL_AXIOMS_2026-06-29.md` — the framework axioms themselves (Lattice, Qubit, Admissibility, Record, definition of A_min); supersedes `MINIMAL_AXIOMS_2026-06-05.md`
- `docs/audit/data/axiom_premise_nodes.json` — explicitly approved primitive premise nodes such as `scale_reference_primitive` and `kinetic_isotropy_primitive`
- [`docs/audit/AXIOM_MINIMALITY_POLICY.md`](../audit/AXIOM_MINIMALITY_POLICY.md) — the binding rules around proposing extensions (`Axiom*`)

Do not redefine, alias, or document these names here.

## Stale-Narrative Archival Vocabulary

When a wrapper note's narrative frame fails an audit, archival uses
fixed path and content vocabulary.

### Archive path

`archive_unlanded/<cluster-tag>/` — the canonical recovery surface for failed-narrative source notes. The cluster-tag is a short stable noun
phrase for the wrapper cluster (e.g. `koide-q-v6-cluster`, `route-2-exhaustion-failed-cluster`).

### Salvage-note required content

When a wrapper note fails but some sub-observations survive, the salvage
note must state:

- what failed (the wrapper's load-bearing claim that the audit invalidated)
- what survived (the durable structural observations that remain)
- the source wrapper's archive recovery path

The salvage note must not restate the failed global conclusion.

### Banned archival wording

- describing the archived wrapper as "deprecated" or "obsolete" — imply a deliberate retirement decision; `audit_status: audited_failed` is the canonical record, no additional adjective needed
- describing the archived wrapper as "still useful" — unless the sentence also states exactly for what it is still useful

The associated workflow rules live in
`docs/audit/STALE_NARRATIVE_POLICY.md`. Vocabulary lives here.

## Branch-Entanglement / BMV Language

Preferred terms for the current staggered branch-entanglement lane:

- `branch-mediated entanglement`
- `externally imposed geometry/source-branch protocol`
- `fixed-adjacency two-branch protocol`
- `branch-mediated entanglement witness`

Only call something a `BMV witness` when the surface closes the stronger
mediator-side requirements, including:

- branch/mediator structure is generated by the relevant physical degrees of
  freedom, not inserted externally
- the mediator-null / LOCC-exclusion logic is implemented at the claimed level

For the current live branch-entanglement package, say explicitly:

- `not a self-generated mediator-branch BMV witness`
- `not a mediator-null / LOCC-exclusion closure`

Avoid as the primary descriptor on live package surfaces:

- `toy`
- `toy model`
- `toy witness`
- `BMV-like evidence`

Those are acceptable only in historical commentary where the sentence also says
what the protocol is missing.

## Boundary-Law Language

For the live boundary-law lane, prefer:

- `Dirac-sea boundary-law probe`
- `many-body-style boundary-law result`
- `bounded boundary-law package`

Avoid calling historical transfer-entropy scripts:

- `area law`
- `subsystem entanglement measurement`

unless the measured object actually matches that wording.

## Historical Retirement Language

When an old runner is no longer live evidence, prefer:

- `retired as evidence`
- `historical / diagnostic`
- `historical exploratory predecessor`

Avoid ambiguous phrasing like:

- `still useful`

unless the sentence also states exactly for what it is still useful.

## Paper-Facing Prose Voice

The target voice for paper-facing prose, curated methodology prose, repo
instructions, and new synthesis is Feynman-like in the useful sense:
plain, physical, concrete, curious, and hard to fool. Do not imitate
quirks or make the prose performative. Use the attitude.

Do not rewrite raw captures or historical dated notes just to polish the
voice; those files are evidence of the work as it happened.

### The rule

Explain what we are doing as if the reader is smart, skeptical, and busy.

Say the simple physical question first. Then say what was checked. Then say
what did not close.

### Use this voice

- Start from the physical question, not from the institutional framing.
- Prefer short sentences when the idea is hard.
- Explain why a result is surprising or useful in ordinary language before listing the machinery.
- Put equations after the idea they express.
- Say "we find", "we check", "we keep", and "we do not claim" when those are the honest verbs.
- Treat negative results as information.
- Keep the reader close to the object: lattice, operator, runner, eigenvalue, projector, source, bridge.

### Avoid this voice

- "broad exact backbone"
- "methodological innovation"
- "transformative framework"
- "groundbreaking result"
- "paradigm"
- "comprehensive package" unless the sentence immediately says what is inside
- "already closed" without naming the exact surface
- any sentence whose main job is to sound important

### Decoration-pruning tone

When pruning algebraic decoration, the tone is "claim-surface management",
not "criticism of the algebra itself". The identities are real; what's
being pruned is the count of separately-retained rows. A package that
presents 25 separate retained theorems where 3 distinct claims exist is
harder to review, harder to falsify, and harder to take seriously as an
external reader. Pruning improves signal density of the publication
package. Use that framing in prose.

### Paragraph test

For each paragraph, ask:

1. What is the question?
2. What is the object being calculated?
3. What is the support surface?
4. What is still open?

If the paragraph does not answer at least one of these, cut it or move
it to a ledger.
