---
name: review-loop
description: Use when an LLM agent needs to run `/review-loop`, review branch changes, run parallel physics-specific reviewers, identify overclaims/imported values/support-only material, apply narrow honest fixes, verify audit-system compatibility without applying audit verdicts, and re-review only files changed by those fixes.
---

# Review Loop

## Skill Freshness

Before applying this skill, perform the repo skill freshness check described in
`docs/ai_methodology/skills/SKILL_FRESHNESS_CHECK.md`. If a newer version of
this `SKILL.md` exists on `origin/main`, follow that version for the current
task.

Run a local review/fix/re-review loop for this physics repo. This is not a
generic software review. Its job is to protect the live claim boundary:
retained/Nature-grade claims must have artifact support, imported values must
be explicit, and support-only results must not be promoted by prose.

## Model And Tool Boundary

Review-loop is a text/code/math review path. Run it with the user's configured
highest-tier Codex reviewer model and maximum available reasoning for this
repo (currently GPT-5.5 at extra-high/xhigh reasoning in the local Codex
configuration). Do not switch to lower-reasoning models for convenience, and
do not use image-generation, image-editing, presentation, document-rendering,
or visual-generation tools unless the user explicitly asks for a separate
visual artifact task.

If a run surfaces an image-generation model/tool error such as a stale
`gpt-image-*` tool configuration, treat it as a local Codex tooling/config
problem, not as part of review-loop. Do not retry the review by invoking
imagegen, changing the science-review model, or routing science review through
visual tooling.

This skill is **review only**. It may make branch/package hygiene changes that
allow the independent audit system to parse and queue claims, but it must not
apply audit verdicts, write `audited_clean`, or run the audit worker.
Audit results have a strict provenance boundary: review-loop must never land
PR-submitted audit verdicts, audit-status promotions/demotions, effective-status
changes, auditor transcripts, or `apply_audit.py` outputs as authority. Audits
come only from the independent post-landing audit loop. PRs may land source
repairs, runners, controlled-data dispatch sidecars, and explicit audit or
re-audit targeting metadata when those are review-clean; they may not carry the
answer to the audit they request.
It must not create or open pull requests. When reviewing an existing PR or
branch, review-loop either fixes/narrows that existing landing path and lands it
when requested, or rejects/closes it with a clear reason. Salvage, dependency
chain repair, audit queue regeneration, and parent re-audit gates are part of
that same landing path, not follow-up PRs.
Delete a closed PR's head branch **only when durable content actually landed** --
its reviewed content was salvaged to `main`, or it was merged. In that case run
`gh pr close <N> --delete-branch` (or `git push origin --delete <head>` after a
manual close) so stale heads do not accumulate on `origin` (review-loop closes
rather than merges, so GitHub's auto-delete-on-merge never fires). **Do NOT
delete the head branch when a PR is closed without landing its content** --
rejected as non-landable with nothing salvaged, or with salvage deferred to a
later pass: keep that branch as the working handle on the un-landed work. Never
delete a head that still backs another open PR, nor `main` or a protected
branch. (Closed PRs retain their commits either way; the live branch matters as
the recovery handle precisely when the content did not land.)
It auto-corrects status vocabulary and terminology so a PR follows repo
conventions by running `scripts/vocab_lint.py --fix` on all
branch-modified files before any landing gate. Vocabulary is canonical
in
[`docs/repo/controlled_vocabulary.yaml`](../../../repo/controlled_vocabulary.yaml)
(design in
[`VOCABULARY_HYGIENE_DESIGN.md`](../../../repo/VOCABULARY_HYGIENE_DESIGN.md)).
Routine local drift that has a non-link-aware rewrite rule, such as legacy
aliases and deprecated wording, is rewritten mechanically as part of the
same review commit; this is never a science blocker. Link-aware filename
suffix migrations and F-letter finding-label migrations are reported but
deferred to Cleanup-2 tooling. Genuinely new terms, pending link-aware
renames, or pending F-letter migrations that `vocab_lint` cannot
mechanically rewrite are recorded as
`prose_status: needs_human_vocab_decision` for the periodic
vocab-extension review; they do not block the landing. Review-loop
must not introduce new repo-wide axioms, new theory
language, new retained-surface claims, framework primitives, or new
foundational premises without explicit user approval. Imports are allowed for
bounded theorem surfaces when they are scoped, labelled, and
dependency-checked; repo-wide axiom additions and primitive additions are not
review-loop fixes.

Review-loop must keep accepted premise classes distinct. Repo-wide axioms and
explicitly approved framework primitives are registered in
`docs/audit/data/axiom_premise_nodes.json` and chain-satisfy dependencies
without making downstream rows `retained_bounded`. Tier-A admitted derivation
targets are registered in `docs/audit/data/tier_a_admissions.json` and
chain-satisfy only at `retained_bounded` until retired by a retained
derivation. Record is part of the approved `minimal_axioms` node in its narrow
permanent-record form, not a Tier-A admission; the older
`OBSERVABLE_PRINCIPLE_FROM_AXIOM_NOTE.md` parent is not an axiom-premise node.
The scale-reference primitive is the approved units primitive, not a Tier-A
admission or a bounded Planck import. The kinetic-isotropy primitive is the
approved structural OS0 kinetic-form isotropy `c_t = c_s`, not a Tier-A
admission or a bounded-status source; it supplies no dynamics, Lorentz-closure
theorem, absolute scale, spacing-ratio theorem, mass ratio, coupling, mixing
angle, phase, selector, readout bridge, probability rule, normalization rule,
or empirical match. New axioms and new primitives both require explicit owner
approval and a reviewed registry/policy update before review-loop may treat
them as accepted premises.
Before naming a changed dependency as an import, wall, Tier-A admission, or
bounded-status source, perform the primitive registry check in
`docs/ai_methodology/skills/PRIMITIVE_REGISTRY_CHECK.md`. In particular, if
the dependency is only the registered `scale_reference_primitive`, treat the
Planck scale reference as already granted units conversion and do not mark the
row `retained_bounded` on that basis. If the dependency is only the registered
`kinetic_isotropy_primitive`, treat `c_t = c_s` as already granted structural
kinetic-form isotropy and do not bound the row on that basis; audit only the
extra dynamics, closure theorem, observable, or empirical content actually
claimed. If the dependency is only the registered `realized_state_primitive`,
treat pointwise evaluation at the supplied realized state as already granted
and do not bound the row on that basis; audit only any averaging, typicality
or genericity predicate, weighting, or state-contingent value actually
claimed.

The framework baseline (per `MINIMAL_AXIOMS_2026-06-29.md`) is the four named
axioms Lattice, Qubit, Admissibility, and Record. Lattice is the cubic `Z^3`
lattice with nearest-neighbor adjacency, standard translations, and proper
cubic rotations about each site; no site is privileged, and sites are
distinguished by the supplied lattice structure alone. Qubit is the domain of
local possibilities with full one-site algebraic presentation `M_2(ℂ)`;
`Cl(3,0)` is equivalent notation, not extra primitive structure, and no
possibility is privileged; possibilities are distinguished by the supplied
algebraic structure alone.
Admissibility is one fixed finite-neighborhood rule, the same at every lattice
translate; for each site, the available possibilities are determined by, and
vary with, the nearest-neighbor conditions, consistent with local records. A
record, when present, locks exactly one admissible local possibility. A site
never carries more than one record; records are permanent. Only records are
readable; a readout value is
determined by record content alone;
finite scalar readout is additive over finite pairwise-disjoint record
collections. A state is a configuration of records. A law privileges no states:
its domain is a supplied condition, and where that condition holds it gives
exactly one answer. Additional
structures such as readout-context selection, decomposition, `K`/CPT
structure, sector-generation rules, weighting, normalization, probability,
measurement/decoherence dynamics, record-production dynamics, physical
persistence dynamics, occurrence rules, update laws, time metric,
within-sector data, occupancy rules, P2/modulus, log-det readouts,
source/action bridges, scale, local observability, law-admissibility or
transition relations, kinetic-branch selection, or arbitrary observable
identification remain compatible downstream targets, but require derivation,
bridge, explicit admission, or approved primitive registration before use as
load-bearing content. Do not
land new science under bare letter-number names such as `A1`, `A2`, `G1`,
or `R3`; those labels are overloaded with axioms, assumptions, Lie
types, lane stages, route codes, and branch blocks. Use the explicit
scientific name on live science surfaces; archival aliases belong
only in clearly historical work-history/archive material. Review-loop must
not treat the framework baseline as a
new axiom, new admitted premise, regulator interpretation, or optional
theory language. Correcting a PR back to this repo language is allowed. This
does not promote downstream science by itself: physical-species
identifications, `C_3`-breaking selectors, kinetic-branch selectors,
readout/scale/unit bridges, and empirical matches remain separate
bounded/open inputs unless they have their own retained-grade derivation and
independent audit closure.

The bar is intentionally high: if review-loop is doing its job, the later
fresh-context audit should be mostly confirmatory. Do not pass branches that
leave the audit lane to discover basic claim-boundary, dependency-graph,
status-vocabulary, or runner-validity defects. Do not lose durable science
when a PR fails that bar: before closing or rejecting a branch, run the
salvage pass below and preserve any narrow, runner-backed lemma that can be
made canonical without changing the science.
Review-loop is still not the audit loop: it must never apply verdicts or
describe its review as an audit. Its job is to decide whether source/tooling
math, claim boundaries, and repo language are honest enough to land and be
sent to the independent auditor afterward.
Non-science PRs require the same discipline: do not reject generated
audit/status or hygiene-only work just because it is not theorem science.
First decide whether it exposes a real audit-graph, cache, queue,
normalization, dependency-chain, or audit-readiness defect. If it does,
salvage the value into durable source, tooling, pipeline, or controlled-data
repairs and regenerate the generated surfaces from that repair.
Audit-dispatch manifests are a special non-science case. If a PR lands a
source note whose purpose is to request future re-audit, retagging, cascade
repair, or batch audit selection, review-loop is not done when the source note
lands. It must also make the request machine-visible by adding or updating a
supported dispatcher sidecar under `docs/audit/data/`, rerunning the audit
pipeline, and verifying the target appears in `docs/audit/AUDIT_DISPATCH_QUEUE.md`
or `docs/audit/data/audit_dispatch_queue.json`. The dispatch manifest is
target-selection metadata only; it must not be passed to auditors as evidence
and must not apply audit verdicts.

## Arguments

Parse:

- focus text: optional free-text review focus;
- `--max-iterations N`: optional cap, default `5`;
- `--no-fix`: review only, do not edit;
- `--no-commit`: fix locally but do not create iteration commits.

## Setup

1. Read the local review/governance surfaces before judging status:
   - `docs/repo/REVIEW_FEEDBACK_WORKFLOW.md`
   - `docs/repo/ACTIVE_REVIEW_QUEUE.md`
   - `docs/repo/CONTROLLED_VOCABULARY.md`
   - `docs/CANONICAL_HARNESS_INDEX.md`
   - `docs/audit/README.md`
   - `docs/ai_methodology/skills/PRIMITIVE_REGISTRY_CHECK.md`
   - `docs/audit/data/axiom_premise_nodes.json` and the source notes named by
     relevant primitive nodes
   - `docs/audit/data/tier_a_admissions.json`
   - `docs/publication/ci3_z3/` when publication-facing files changed
   - `docs/publication/ci3_z3/USABLE_DERIVED_VALUES_INDEX.md` when
     quantitative or imported-value claims changed
2. Determine the base ref:
   - prefer `origin/main` if present;
   - otherwise use `main`;
   - if the current branch is the base branch, use `HEAD~1`.
3. Compute the review base with `git merge-base HEAD <base-ref>`.
4. Build the original changed-file set from committed, staged, unstaged, and
   untracked changes. Do not review outside this set except interacting files
   that are also in this original set.
5. Record whether the worktree was initially clean. If it was dirty, do not
   auto-commit without explicit user permission unless the slash-command
   invocation clearly requested commit-producing fixes.
6. If the task is to review open/non-landed PRs, include all non-merged,
   non-draft PRs in the requested scope except PRs the user explicitly
   excluded. Draft PRs are out of scope: ignore them entirely and do not land
   them unless the user explicitly asks to inspect a draft PR without landing
   it. Closed-but-unmerged PR heads can be inspected with `gh pr view` and
   `git fetch origin pull/<N>/head:refs/tmp/pr-<N>`.

Useful commands:

```bash
git diff --name-only <base>...HEAD
git diff --name-only --cached
git diff --name-only
git ls-files --others --exclude-standard
git diff <base>...HEAD -- <files>
git diff --cached -- <files>
git diff -- <files>
```

For untracked files, include their full content or a concise new-file summary
in reviewer prompts.

## Stale PR Integration Guard

When landing one or more PRs, protect already-landed science before applying
any branch content. A PR branch may be based before another PR just landed, so
checking out whole files from that stale PR head can erase current-main source
science in shared files.

For every PR before integration:

```bash
git fetch origin main pull/<N>/head:refs/tmp/pr-<N>
pr_base=$(git merge-base origin/main refs/tmp/pr-<N>)
comm -12 \
  <(git diff --name-only "$pr_base"..origin/main | sort) \
  <(git diff --name-only "$pr_base"..refs/tmp/pr-<N> | sort)
```

If the overlap list is non-empty, or if earlier PRs have landed during the
same review-loop run, do **not** run `git checkout refs/tmp/pr-<N> -- <file>`
for those paths. Integrate the PR's delta against its merge base with a
three-way patch, rebase/merge, or cherry-pick source commits, then resolve any
conflicts by preserving both current-main science and the salvageable PR
science:

```bash
git diff --binary "$pr_base"..refs/tmp/pr-<N> -- <source paths> > /tmp/pr<N>.patch
git apply --3way /tmp/pr<N>.patch
```

Whole-file checkout from a PR head is allowed only when the file is new on the
PR or when `git diff --quiet "$pr_base"..origin/main -- <file>` proves current
`main` has not changed that path since the PR base. For every overlapped
source path, do a science-loss guard after integration: the current-main diff
from `pr_base` to `origin/main` must still be represented in the final file.
If that cannot be verified quickly, stop and treat it as a blocking integration
hazard rather than risking science loss.

Generated audit JSON/Markdown is a special case: do not hand-merge generated
files from stale PR heads. Resolve source files first, prefer the current
`origin/main` generated audit surface, then rerun the audit pipeline and strict
lint to regenerate it.

## Reviewer Fanout

On each iteration, set `files_to_review` to the files that changed since their
last clean review. On iteration 1, use all original changed files.

Run all applicable reviewers in parallel through the available agent/subagent
mechanism. If parallel agents are unavailable, run the same reviewer passes
locally and report that limitation.

### Required Reviewers

- `CodeRunnerReviewer`
  Review changed Python/scripts/log-producing code. Check syntax, decisive
  assertions, hard-coded targets, stale fixtures, literal `True` checks,
  hidden observations, reproducibility, paired runner/output agreement, and
  whether the runner actually tests the note's load-bearing bridge. If a
  runner checks audit-ledger dependency status, it must use the current
  retained-grade set (`retained`, `retained_bounded`, `retained_no_go`) rather
  than hard-coding stale expectations such as exactly `retained`.
  For math-bearing runners, PASS output is not enough. Extract every
  load-bearing formula, sign, factor, normalization, matrix identity,
  optimizer objective, and expected numeric value from the changed code and
  note, then verify them by an independent route before landing: manual
  derivation against the note, symbolic simplification, small-case exhaustive
  enumeration, a second implementation that does not share the same expression,
  or invariant/limit/property checks. Treat self-confirming tests, expected
  values generated by the same implementation under review, missing factor/sign
  checks, or stale reopened bug reports as blocking until the formula is
  corrected or the claim is demoted to a narrower supported boundary.

- `PhysicsClaimReviewer`
  Attack theorem notes, claims tables, publication surfaces, and prose. Check
  semantic bridges, selector assumptions, status labels, exact/bounded/support
  boundaries, and code/prose drift.

- `ImportSupportReviewer`
  Inventory every measured, fitted, literature, PDG, cosmological,
  normalization, boundary-condition, or convention input. Classify each as
  `zero-input structural`, `framework-derived`, `one computed lattice input`,
  `admitted normalization/boundary condition`, `standard/literature
  correction`, `observational comparator`, `support-only`, `insensitive
  nuisance`, or `unjustified import`. For a Nature-grade retention claim, every
  import must be derived, admitted with a narrow role, quantitatively
  insensitive, or the claim must be demoted.

- `NatureRetentionReviewer`
  Apply the hostile external-review bar. Ask whether the result can honestly
  be called retained/Nature-grade: no hidden unit identification, no structural
  redefinition, no imported selector, no unsupported first-principles claim,
  no unmatched observed target, and clear falsifiers/open gates. Output
  `RETAINED`, `RETAINED SUPPORT`, `BOUNDED`, `OPEN`, `NO-GO`, or `REJECT`.

- `NoGoDisciplineReviewer`
  Scrutinize negative claims with the same rigor as positive ones. Trigger
  this reviewer whenever changed content includes a `no_go`, `stretch_attempt`,
  `bounded_with_named_walls`, or derived-no-go-boundary artifact, or when any
  other reviewer in this fanout outputs `NO-GO` / `BOUNDED` / `OVERCLAIM` on
  a negative claim. The reviewer must invoke the `no-go-discipline` skill
  and walk N1-N8 against the branch content (see
  [`docs/ai_methodology/skills/no-go-discipline/SKILL.md`](../no-go-discipline/SKILL.md)):
  N1 alternative-route enumeration (≥5 distinct routes), N2
  wall-independence audit, N3 hidden-wall scan, N4 residual matching,
  N5 rhetoric audit (per-element / per-mode / per-block / lattice-wide
  resolutions), N6 partial-closure path scan (convention-reframe vs new
  axiom), N7 steelman, N8 cross-cycle echo. Output `PASS` (negative claim
  honestly scoped) or `FAIL` with the failing checklist items named and the
  narrowest demoted claim proposed (`partial-attempt-with-named-untested-routes`,
  `partial-narrowing`, `bounded-with-corrected-wall-count`, or
  `stretch-attempt-with-honest-residual`). The reviewer must not approve a
  no-go that has not been stress-tested against the framework's full
  authority surface — under-tested negative claims are at least as harmful
  as overclaimed positive ones because they foreclose investigation paths
  permanently.

- `LabelingConventionReviewer`
  Detect labeling/naming/convention content masquerading as a bounded
  theorem. Trigger whenever changed content includes a `bounded_theorem`
  candidate whose load-bearing claim is a labeling/naming/convention
  statement (parallel to the u/c/t mass-ordering convention or the
  e/μ/τ charged-lepton naming) rather than an algebraic claim with
  explicit named admissions. A labeling convention has no propositional
  content to admit, so `retained_bounded` grade does not apply — the
  grade is for algebraic claims with explicit named premises, not for
  stipulations about names.

  The right outcome is to split:
  (i) the algebraic core (if any) ships as a narrow `positive_theorem`
      or `bounded_theorem` with the algebraic premises explicit;
  (ii) the labeling content ships as a separate `meta` convention note,
       parallel to the No-Go Discipline Battery's labeling-vs-physics
       check in
       `docs/ai_methodology/skills/physics-claim-reviewer/SKILL.md`
       ("If labeling, the right outcome is a `meta` convention note").

  Output `PASS` if the candidate is genuinely algebraic with named
  admissions, `SPLIT-REQUIRED` if labeling content is bundled with
  algebraic content (ship the algebraic theorem narrow + the convention
  as a separate `meta` note), or `DEMOTE-TO-META` if the candidate is
  purely convention with no derivation. The reviewer must not approve a
  `bounded_theorem` whose load-bearing content is a labeling stipulation
  — conflating conventions with bounded theorems hides which premises
  are actually load-bearing and prevents downstream rows from cleanly
  identifying their dependency status. Downstream costs of the
  conflation: the bundled convention becomes an undischargeable
  "premise" that blocks the row from reaching retained-unbounded;
  downstream rows that cite the bundled bounded_theorem inherit an
  unstated convention dependency; the audit lane cannot cleanly verify
  "all premises retained" because the convention is not propositional
  content; and future agents may waste cycles trying to "prove" the
  convention as if it were derivable.

- `RepoGovernanceReviewer`
  Check placement and authority surfaces. Ensure live findings route through
  `docs/repo/ACTIVE_REVIEW_QUEUE.md`, long packets go under
  `docs/work_history/repo/review_feedback/`, publication edits update the
  relevant `docs/publication/ci3_z3/` surfaces, status wording follows
  `docs/repo/CONTROLLED_VOCABULARY.md`, and changed claim notes are compatible
  with the audit lane's propose/ratify split. Also verify that load-bearing
  dependencies are real markdown links that seed the citation graph, not just
  code-formatted file names in prose. Block ambiguous new science names such
  as bare `A1`, `A2`, `G1`, `R3`, `Route F`, or `Block 2` when they appear as
  titles, primary table labels, claim scopes, runner headlines, or review
  findings without an explicit scientific noun phrase. Block repo-wide axiom
  additions, nonstandard theory vocabulary, or new foundational claims unless
  the user explicitly approved that change; vocabulary corrections back to
  repo conventions are allowed.
  Block branch-local or draft-PR language from landing on repo-facing surfaces.
  Long-lived draft wording, PR-specific labels, campaign names, and branch-only
  framings must be translated into native repo vocabulary before merge
  (including language leaked from PR230 or any similar draft branch). If a
  scientific claim is otherwise salvageable, fix the vocabulary in the landing
  commit instead of rejecting the science.

### Optional Reviewer

Run `MethodologySkillReviewer` when files under `docs/ai_methodology/skills/`,
`docs/ai_methodology/`, or `.claude/commands/` changed. Check that the skill is
concise, triggerable from its frontmatter/command name, aligned with the AI
methodology lane, and not claiming physics authority.

## Reviewer Prompt

Use this prompt shape for each reviewer, filtered to only that reviewer's file
scope:

````text
Review the following physics-repo changes.

Files to review:
<files>

Diff/content:
```diff
<diff for only those files; include untracked file content separately>
```

Focus:
<focus text or "None specified">

Context:
- Base ref: <base-ref>
- Iteration: <N> of <max>
- Already reviewed and unchanged: <reviewed_files>
- Repo review surfaces: REVIEW_FEEDBACK_WORKFLOW, ACTIVE_REVIEW_QUEUE,
  CONTROLLED_VOCABULARY, CANONICAL_HARNESS_INDEX, docs/audit/README.md

Rules:
- Findings must cite file/line when possible.
- Separate bugs, overclaims, support-only demotions, imported-value problems,
  repo-governance problems, and nits.
- Do not require new science for wording problems.
- Do not approve retained/Nature-grade language if an import or bridge remains
  hidden.
- Do not apply audit verdicts. Review only whether the branch is ready for the
  independent audit worker.
- Do not approve new bare letter-number science names. Require explicit names
  from CONTROLLED_VOCABULARY, with shorthand only as a parenthetical alias.
- Do not approve a `NO-GO` or `BOUNDED with named walls` recommendation
  without running `no-go-discipline` N1-N8 against the branch content. An
  unscrutinized negative claim forecloses investigation paths permanently and
  is at least as harmful as an overclaimed positive.
````

## Consolidate Findings

Present one iteration summary:

```text
## Review Results (Iteration N)

### Code / Runner: PASS | RISK | FAIL
### Physics Claim Boundary: RETAINED | SUPPORT | BOUNDED | OPEN | REJECT
### Imports / Support: CLEAN | DISCLOSED | DEMOTE | FAIL
### Nature Retention: RETAINED | RETAINED SUPPORT | BOUNDED | OPEN | NO-GO | REJECT
### No-Go Discipline: PASS | FAIL | NOT APPLICABLE
### Labeling Convention: PASS | SPLIT-REQUIRED | DEMOTE-TO-META | NOT APPLICABLE
### Repo Governance: PASS | FIX | QUEUE | ARCHIVE
### Audit Compatibility: PASS | FIX | BLOCKED | NOT APPLICABLE
### Methodology Skill: PASS | FIX | SKIPPED
```

Classify every finding:

- `BUG`
- `OVERCLAIM`
- `NO_GO_OVERCLAIM`
- `IMPORTED_VALUE`
- `SUPPORT_ONLY_DEMOTION`
- `MISSING_ARTIFACT`
- `SEMANTIC_BRIDGE`
- `REPO_GOVERNANCE`
- `AUDIT_COMPATIBILITY`
- `NIT`
- `SALVAGE_CANDIDATE`
- `SALVAGE_REJECT`

Stop immediately when all applicable reviewers are clean.

## Salvage Pass

Run this pass before closing a PR, marking it non-landable, or discarding a
stretch/campaign packet. The goal is to preserve meaningful science without
lowering the review bar.

1. Inventory the branch into these buckets:
   - canonical source candidates: theorem/no-go/open-gate notes and paired
     runners;
   - useful negative results: failed routes that name a durable obstruction and
     have a runner or exact calculation;
   - support-only calculations: exact algebra or bookkeeping that may be useful
     as bounded support but not as retained/Nature-grade science;
   - audit/process hygiene: dependency-graph repairs, audit queue unlocks,
     stale runner-cache detection, generated-data normalization, cycle-break
     hygiene, and pipeline/tooling fixes that make audit results more reliable;
   - non-source material: claim-status certificates, handoffs, campaign state,
     generated audit files, expected audit verdicts, and branch-local logs.
2. For each source candidate, decide whether it can be salvaged with only
   review-level edits:
   - the claim can be narrowed to a canonical `claim_type`:
     `positive_theorem`, `bounded_theorem`, `no_go`, `open_gate`,
     `decoration`, or `meta`;
   - all imported physics, textbook machinery, observations, fitted values,
     and conventions are explicitly labelled;
   - the runner tests the actual load-bearing bridge, not just downstream
     arithmetic after the premise is assumed;
   - load-bearing dependencies can be represented as markdown links and
     non-load-bearing siblings can be kept out of the citation graph;
   - the salvage does not rely on a closed, unlanded, unaudited, or rejected
     sibling PR unless the dependency is copied in as a self-contained
     derivation and reviewed in the same salvage branch.
3. Do not salvage by papering over missing science. If the durable part is
   only an obstruction or failed route, salvage it as a narrow `open_gate` or
   `no_go` only when the runner directly supports that negative boundary.
4. Strip all non-source material from salvage branches:
   claim-status certificates, handoffs, campaign state, expected audit
   verdicts, `target_effective_status_*`, `audit_status = ...`, generated audit
   verdict payloads, and branch-local logs.
5. Prefer small salvage slices grouped by coherent topic. Split unrelated
   lemmas rather than bundling them only because they came from the same failed
   PR, but do not open follow-up PRs for those slices. Land them through the
   current requested landing path or report that the work cannot be landed yet.
6. Run the normal audit-system compatibility gate on every salvage slice.
   The resulting rows must remain `unaudited`; the independent audit lane owns
   all verdicts.
7. For audit/process hygiene, preserve the durable repair rather than the
   generated symptom. Land source/tooling/pipeline/controlled-data changes when
   they strengthen the repo or unblock auditing without changing science.
   Regenerate audit JSON/Markdown from the pipeline afterward only from the
   reviewed source repair on current `main`. Do not land PR-authored
   `effective_status`, `intrinsic_status`, `audit_status`, auditor-output,
   previous-audit, or expected-verdict edits as the authority for the change.
   Source repairs may intentionally invalidate a prior row hash and make a row
   visible for re-audit; that is allowed. The independent audit loop must still
   produce the verdict after landing.
8. If no salvage is possible, leave a concise PR comment or review summary
   saying why, for example: "runner only rechecks assumed premise",
   "claim depends on closed sibling", "noncanonical stretch packet with no
   theorem-grade boundary", or "overbroad theorem not supported by runner".

Salvageable examples:

- a parity/counting/no-go lemma with a decisive finite algebra runner;
- a conditional textbook lemma that is useful only when explicitly marked as
  bounded support;
- a negative route that conclusively rules out one proposed mechanism and
  narrows the remaining open gate;
- an audit-hygiene PR whose generated status change reveals a real durable
  graph/tooling/pipeline defect, salvaged as the underlying repair plus
  regenerated audit outputs.

Not salvageable without a new research task:

- branch-local certificates and handoffs with no source theorem;
- broad "closing derivations" whose runner assumes the missing bridge;
- expected audit verdicts or status-elevation packages;
- stretch-attempt notes that document research direction but do not define a
  canonical theorem/no-go/open-gate boundary.

## Fix Policy

If `--no-fix` was passed, do not edit.

Otherwise apply the narrowest honest fix:

1. Fix verified code bugs, broken reproduction commands, stale runner names,
   false PASS checks, and code/prose mismatches.
2. Demote overclaimed status when the artifact supports only support/bounded
   language.
3. Mark imported values explicitly; distinguish derived, admitted, fitted,
   measured, literature, boundary-condition, and insensitive nuisance inputs.
4. Add or repair paired runner/note references only when the artifact exists.
5. Make audit-system hygiene fixes only when they do not change the science:
   status-line tier labels, machine-local path removal, stale runner transcript
   refreshes, generated audit queue/ledger seeding, and discoverability wiring.
6. Rename ambiguous science shorthand to explicit repo vocabulary without
   changing the claim boundary. Examples: write `one-qubit operator algebra`
   (or equivalently `M_2(ℂ) ≅ Cl(3,0)`, `physical Cl(3) local algebra` as
   the real-algebra reading — all co-equal labels for the same retained
   algebra-isomorphism class), `Z^3 lattice`,
   `Koide Frobenius-equipartition condition`, or `Lie type A_1` instead of
   bare `A1` / `A2`.
7. Update `docs/repo/ACTIVE_REVIEW_QUEUE.md` for live unresolved findings.
8. Route detailed resolved packets to
   `docs/work_history/repo/review_feedback/` only when a long packet is needed.
9. When a PR is non-landable but salvageable, preserve only the durable
   note/runner content, make the claim boundary canonical, and land that source
   salvage through the current requested landing path. If the rejected branch
   contains substantial non-source packet material, use a clean temporary
   worktree for integration, but do not create or open a follow-up PR.

Skip:

- nits;
- suspected findings without evidence;
- ambiguous science gaps that need new derivation;
- attempts to paper over missing theorem steps with confident prose;
- repo-wide axiom additions, new theory terminology, or new foundational
  premises that lack explicit user approval;
- broad refactors unrelated to the finding.

## Audit-System Compatibility Gate

This gate is mandatory when a branch adds or edits source notes, runners,
claim tables, lane stubs, or publication/control-plane files.

The review loop must enforce the audit lane's propose/ratify split without
performing the independent audit:

**Audit-hash churn guard.** Non-semantic hygiene sweeps on audited source notes
can be scientifically harmless while still invalidating large parts of the
audit ledger, because note hashes are source-content hashes. Before landing any
branch that touches many existing claim-note files for formatting, link-target,
path, vocabulary, or other non-science cleanup, run the pipeline in validation
mode and inspect the `seed_audit_ledger.py` / `invalidate_stale_audits.py`
counts. If the change would reset or requeue already-audited rows solely due to
non-semantic churn, do not land the broad source sweep. Either narrow the PR to
non-ledger/non-claim surfaces, land a reviewed hash/canonicalization tooling
repair first, or ask for explicit user approval to spend the audit capacity.
Never trade a clean audit graph for cosmetic source-note churn without making
that cost explicit.

0. Before applying a PR, inventory any audit-status surface it touches:

```bash
git diff --name-only <pr-base>..refs/tmp/pr-<N> -- \
  docs/audit/AUDIT_LEDGER.md docs/audit/AUDIT_QUEUE.md docs/audit/data \
  'docs/publication/ci3_z3/*_EFFECTIVE_STATUS.md'
git diff <pr-base>..refs/tmp/pr-<N> -- docs/audit docs/publication/ci3_z3 \
  | grep -E 'audit_status|effective_status|audited_clean|audited_conditional|audited_failed|audited_renaming|audited_decoration|audited_numerical_match|previous_audits|audit_result|verdict'
```

Treat this output as a provenance review, not as a merge recipe. Strip
PR-submitted generated ledgers, queues, effective-status tables, auditor
transcripts, and audit verdict payloads before landing. The only acceptable
audit-lane changes from a PR are reviewed source/tooling repairs and
machine-readable audit/re-audit targeting metadata, such as dispatcher
sidecars, that do not assert a verdict. After applying the source repair, run
the local pipeline to verify the row is queued or re-queued as intended, then
restore generated audit outputs from `origin/main` before committing. Pipeline
regeneration of `docs/audit/data/`, `docs/audit/AUDIT_LEDGER.md`,
`docs/audit/AUDIT_QUEUE.md`, `docs/audit/MISSING_DERIVATION_PROMPTS.md`, and
`docs/publication/ci3_z3/*_EFFECTIVE_STATUS.md` is a VALIDATION step only;
framework PRs must never ship these files because the merge would overwrite
the audit lane's ratified state. The audit-loop run on `main` (nightly cron
plus `audit:` commits) is the sole channel for landing those outputs.

1. Source-note `Status:` prose is not an audit authority. New or touched claim
   notes should use `Type:` / `Claim type:` metadata for intended audit
   classification.
2. If a no-go/firewall is intended to be theorem-grade, use
   `claim_type = no_go`; do not rely on support-style prose and expect audit
   ratification.
3. Keep disclaimers such as "This is not charged-lepton mass closure" outside
   audit metadata fields.
4. Do not prefill or recommend a verdict in author/review surfaces. Wording
   such as `target_audit_status: audited_clean`, `audit_status =
   audited_clean`, `effective_status = retained`, or "can land audited_clean"
   is not review-loop compatible. Use wording like `audit_status_authority:
   independent audit lane only` and "effective status is pipeline-derived
   after audit ratification and dependency closure."
5. Changed claim notes that cite load-bearing authorities must use markdown
   links, for example
   ``[`GRAPH_FIRST_SU3_INTEGRATION_NOTE.md`](GRAPH_FIRST_SU3_INTEGRATION_NOTE.md)``.
   Code-formatted names such as `` `GRAPH_FIRST_SU3_INTEGRATION_NOTE.md` `` do
   not seed graph dependencies and are not enough.
6. Run the audit pipeline after review fixes:

```bash
bash docs/audit/scripts/run_pipeline.sh
python3 docs/audit/scripts/audit_lint.py --strict
git diff --check
```

The known graph-cycle warning is acceptable. Any strict-lint error blocks a
review-loop PASS.

**`note_hash` drift is a notice for non-retained rows, an error only for
retained-grade rows.** `note_hash` is a *source-content* hash, not an audit
verdict. When a review fix edits a claim note, its `note_hash` drifts from the
seeded value; `audit_lint.py` reports this drift as a non-blocking
`note_hash_drift_reaudit_pending` **notice** when the row is not retained-grade
(`unaudited` / `audited_conditional` / pending), because re-audit is simply
pending and the audit-lane re-seed refreshes the hash. Such a notice does **not**
block review-loop PASS and must **not** be "fixed" by committing audit-lane
ledger churn (that is the forbidden pipeline-output commit). A `note_hash`
mismatch on a **retained-grade** row (`retained` / `retained_bounded` /
`retained_no_go`) stays a hard **error**: an edited retained note laundered past
a stale ratification is a real integrity violation. Resolve it by re-auditing
(the audit lane re-seeds and archives the prior verdict) or by demoting the edit
per the audit-hash churn guard — never by refreshing the hash while keeping the
retained verdict.

**Stuck-row repair requeue gate.** Terminal non-clean rows
(`audited_conditional` / `audited_renaming` / `audited_failed` /
`audited_numerical_match`) re-enter the audit queue only through their own
note or paired-runner hash drift, an upstream `deps_changed` invalidation, or
a dispatcher-sidecar re-audit target. Dependent-side edits never reschedule
the stuck row. When a branch's stated purpose is repairing such a row (the PR
title/body names the row or quotes its audit repair target):

1. Verify the stuck row itself will requeue: its note or paired runner
   changes on the branch, or the branch ships dispatcher-sidecar targeting
   metadata naming the row.
2. If the audit-named repair is dependent-side only (for example, narrowing
   dependents' citing sentences to the audited scope), add a dated
   downstream-hygiene line to the stuck row's own note boundary as part of
   the landing: a one-line source-side record of what changed downstream
   (date + what was narrowed + PR number), with no grade or verdict
   language. The hash drift re-enters the row into the ordinary queue and
   the re-auditor (or second auditor) sees the recorded condition.
3. Run the validation pipeline and confirm the row is queued or re-queued as
   intended, then restore generated audit outputs per the
   pipeline-output-stripped gate below.
4. Repair-PR review checklist: the audit repair target is quoted verbatim
   (from `verdict_rationale` / `notes_for_re_audit_if_any`) in the PR body;
   a sibling-runner pin sweep was done before every note edit (grep
   `scripts/` for runners pinning the edited sentences); no authored grade
   language anywhere; no `docs/audit/data/` content beyond
   dispatcher-sidecar targeting metadata.

7. **Pipeline-output-stripped PASS gate (hard).** After running the pipeline
   for validation, the framework PR must NOT land any pipeline-regenerated
   audit-lane or effective-status surface. The independent audit lane is the
   sole authority for these files; a framework PR that ships them creates a
   dual-source-of-truth and overwrites the audit lane's ratified state at
   merge. The following must hold for review-loop to issue PASS:

```bash
# Must produce no output. Any change here means the working tree has
# pipeline-regenerated audit-lane outputs left over from validation;
# drop them (see below) before recommitting.
git status --porcelain docs/audit/AUDIT_LEDGER.md \
                       docs/audit/AUDIT_QUEUE.md \
                       docs/audit/data \
                       docs/publication/ci3_z3/PUBLICATION_AUDIT_DIVERGENCE.md \
                       docs/publication/ci3_z3/CLAIMS_TABLE_EFFECTIVE_STATUS.md \
                       docs/publication/ci3_z3/DERIVATION_ATLAS_EFFECTIVE_STATUS.md \
                       docs/publication/ci3_z3/PUBLICATION_MATRIX_EFFECTIVE_STATUS.md \
                       docs/publication/ci3_z3/FULL_CLAIM_LEDGER_EFFECTIVE_STATUS.md \
                       docs/publication/ci3_z3/USABLE_DERIVED_VALUES_INDEX_EFFECTIVE_STATUS.md \
                       docs/publication/ci3_z3/RESULTS_INDEX_EFFECTIVE_STATUS.md \
                       docs/publication/ci3_z3/QUANTITATIVE_SUMMARY_TABLE_EFFECTIVE_STATUS.md \
                       docs/publication/ci3_z3/DERIVATION_VALIDATION_MAP_EFFECTIVE_STATUS.md
```

If this command prints any lines, BLOCK PASS and instruct the operator to
DROP the regenerated files before recommitting:

```bash
git checkout origin/main -- docs/audit/data/ \
                            docs/audit/AUDIT_LEDGER.md \
                            docs/audit/AUDIT_QUEUE.md \
                            docs/audit/MISSING_DERIVATION_PROMPTS.md \
                            'docs/publication/ci3_z3/*_EFFECTIVE_STATUS.md' \
                            docs/publication/ci3_z3/PUBLICATION_AUDIT_DIVERGENCE.md
git clean -fd -- docs/audit/data/
```

The pipeline is run for VALIDATION only — to confirm the source repair is
ingested and the runner row is queued or re-queued as intended. The
audit-loop pipeline run on `main` (nightly cron + `audit:` commits) is the
sole channel for landing the regenerated outputs. Framework PRs that ship
these files force a destructive overwrite of ratified audit state at merge
time and have been an active source of broken-row regressions.

8. **Repository-portable links PASS gate (hard).** Markdown link targets on
   branch-modified `.md` files must be repo-relative or web URLs. Absolute
   local paths such as `/Users/<name>/...`, `/home/<name>/...`,
   `/private/tmp/...`, `/tmp/...`, `/var/...`, `/opt/...`, or `file://...`
   inside a markdown link target are non-portable: they break for other
   developers, CI runners, fresh clones, and independent reviewers.

```bash
# Must produce no output. Scans branch-modified markdown for local absolute
# paths inside markdown link targets.
git diff --name-only origin/main...HEAD -- '*.md' \
  | xargs -I{} grep -nE '\]\((/Users/|/home/|/private/|/tmp/|/var/|/opt/|file://)' {} 2>/dev/null
```

If this command prints lines for files the branch is already modifying for
source, runner, methodology, or review reasons, rewrite the offending link
targets before PASS. The usual mechanical fix is to preserve the display text
and replace the target with a `../` chain relative to the source file's
directory, e.g. in `docs/SOURCE_RESOLVED_FOO_NOTE.md` rewrite
`(/Users/me/Projects/Physics/scripts/foo.py)` to `(../scripts/foo.py)`.

This gate prevents new non-portable links from landing; it is not a license for
large standalone cosmetic sweeps over audited claim notes. If the PR's only
purpose is to rewrite existing local-path links across many audited source
notes, apply the audit-hash churn guard above before landing any broad cleanup.

9. **No-Go Discipline PASS gate (hard).** Before issuing review-loop PASS,
   identify any artifact on the branch that ships a negative claim:

```bash
# Source notes whose claim_type is no_go, or whose Status / Type line
# names walls / admissions / "conditional on" content
git diff --name-only origin/main...HEAD -- 'docs/*NO_GO*.md' 'docs/*BOUNDED*.md' \
                                           'docs/*STRETCH_ATTEMPT*.md' \
                                           'docs/*OBSTRUCTION*.md'
# Audit-data rows whose verdict_rationale or claim_type record walls
git diff origin/main...HEAD -- docs/audit/data/audit_ledger.json \
  | grep -E '"claim_type": "no_go"|"verdict_rationale".*wall|"verdict_rationale".*admission'
# Any source note touched on this branch whose body contains negative-claim shape
git diff origin/main...HEAD -- 'docs/*.md' \
  | grep -E 'structurally undecidable|no retained primitive|requires new axiom|cannot be derived from A_min|conditional on .* walls?'
```

For every match, the NoGoDisciplineReviewer must output `PASS` (N1-N8 walk
complete and no failure condition hit) before review-loop issues PASS. A
`FAIL` from NoGoDisciplineReviewer blocks PASS regardless of how other
reviewers voted. An unscrutinized no-go that ships through review cements
the overclaim at audit time and forecloses investigation paths permanently.

If NoGoDisciplineReviewer outputs FAIL, apply the narrowest honest fix per
Fix Policy step 2 (demote to a narrower honest claim that passes N1-N8) and
re-review. Do not weaken the gate to PASS the branch.

This gate is independent of the Pipeline-clean PASS gate above; both must
pass for review-loop to issue PASS.

10. **Math-runner independent-check PASS gate (hard).** Before issuing
review-loop PASS for any branch that changes a runner, proof script, numeric
constant, matrix construction, optimizer, expected value, or note formula,
record the independent math check used by `CodeRunnerReviewer`. At least one
check must not share the same implementation path as the changed runner:
manual formula derivation, symbolic/algebraic reduction, finite toy-case
enumeration, independent recomputation, or invariant/limit tests. A runner
that merely computes its own target and prints PASS is not a proof that the
formula is correct. If an issue was reopened because the runner's math was
wrong, treat the whole formula family as suspect until the changed expression
and any reused helpers are cross-checked.

11. **Native-language PASS gate (hard).** Changed repo-facing text must use
controlled, native repo vocabulary. Run `scripts/vocab_lint.py --fix` on all
branch-modified files before landing, then inspect changed headings, metadata,
runner banners, claim scopes, table labels, and review comments for
branch-local/draft language that the linter cannot know about. PR-specific
labels, draft-branch vocabulary, campaign names, and noncanonical theory
phrases must be rewritten into repo-native language or explicitly deferred in
`docs/repo/ACTIVE_REVIEW_QUEUE.md`; do not land them silently.

The review loop must not run `docs/audit/scripts/apply_audit.py` and must not
write `audit_status`, `audited_clean`, or other audit verdicts. If the branch
introduces retained-grade `claim_type` rows, report those claim IDs in the
final report as requiring the independent audit worker.
When a source repair changes a note or runner for a previously audited row,
the local result is `note_hash`/runner-hash drift plus queue/dispatch
visibility for independent re-audit. For a non-retained row this drift is a
benign `note_hash_drift_reaudit_pending` notice (see the Audit-System
Compatibility Gate) — it does not block strict lint and must not be repaired by
committing ledger churn. For a retained-grade row the drift is a strict error
that must be resolved by re-audit, not laundered. In all cases, do not preserve,
copy, or author a fresh `previous_audits` entry, `audit_status`, or verdict
rationale from the PR branch; the independent audit lane (nightly cron +
`audit:` commits) is the sole channel that refreshes the hash and re-ratifies.

After the pipeline, inspect the changed claim rows in
`docs/audit/data/audit_ledger.json`:

- `claim_type` must match the intended class (`positive_theorem`,
  `bounded_theorem`, `no_go`, `open_gate`, `decoration`, or `meta`).
- `audit_status` must remain `unaudited` unless the branch is only carrying
  already-audited history from `origin/main`.
- `effective_status` must be pipeline-derived, not hand-authored.
- New theorem/no-go/bounded rows with declared load-bearing authorities must
  have non-empty `deps` matching the markdown-linked authorities.
- Dependencies asserted as retained-grade must currently have
  `effective_status` in `{retained, retained_bounded, retained_no_go}`. Open
  gates, `unaudited`, `audit_in_progress`, `retained_pending_chain`, and
  terminal non-clean audit statuses are blockers for retained-grade claims.

Useful review-only inventory:

```bash
python3 - <<'PY'
import json, subprocess
changed = set()
for cmd in (
    ["git", "diff", "--name-only", "HEAD"],
    ["git", "diff", "--name-only", "--cached"],
):
    changed.update(subprocess.check_output(cmd, text=True).splitlines())
try:
    changed.update(subprocess.check_output(
        ["git", "diff", "--name-only", "origin/main...HEAD"], text=True
    ).splitlines())
except Exception:
    pass
rows=json.load(open("docs/audit/data/audit_ledger.json"))["rows"]
for cid,row in rows.items():
    if row.get("note_path") in changed:
        print(cid, row.get("claim_type"), row.get("audit_status"),
              row.get("effective_status"), row.get("deps"),
              row.get("note_path"))
PY
```

If generated audit files conflict while integrating current `origin/main`, do
not hand-merge generated JSON/Markdown. Resolve source files, prefer the
current remote generated audit files, then rerun `run_pipeline.sh` and strict
lint so the generated surface is rebuilt from source.

## Smoketest

After fixes, run the smallest relevant checks:

- `python3 -m py_compile <changed .py files>` for changed Python files;
- changed paired runners directly when they are expected to be short;
- for changed math-bearing runners, independently verify formulas/constants
  before trusting PASS output: compare note equations to code line by line,
  check signs/factors/normalizations, run a second implementation or symbolic
  simplification when practical, and add finite edge-case or invariant checks
  when they would have caught the suspected class of error;
- if many changed runners are part of the branch, execute all practical
  changed runners with a bounded timeout, then rerun any timeout once with a
  longer timeout before classifying it as slow rather than broken;
- any reproduction commands named in changed notes when practical;
- publication/control-plane consistency checks by reading changed tables and
  nearby authority surfaces.
- `bash docs/audit/scripts/run_pipeline.sh` and
  `python3 docs/audit/scripts/audit_lint.py --strict` when claim notes or
  governance/publication surfaces changed.

If a runner is long, stochastic, or requires unavailable data, do not fake the
check. Report it as not run with the reason.

## Re-Review Tracking

Never re-review unchanged files.

After each fix pass:

1. Identify files modified by the fix pass.
2. If committing is allowed, create one iteration commit:
   `fix: address physics review findings (iteration N)`.
3. Set `files_to_review` to the files modified by the fix pass.
4. Add interacting files only if they are also in the original changed-file
   set. Find interactions through imports, runner/note pairs, canonical harness
   rows, publication tables, and explicit cross-links.
5. Loop until clean, no files changed, or max iterations reached.

## Final Report

Report:

- iterations run;
- files reviewed;
- total findings, fixed findings, skipped findings;
- import/support inventory summary;
- final claim-strength disposition;
- audit-compatibility status and proposed claim IDs needing independent audit;
- commits created;
- checks run and checks skipped;
- remaining issues with disposition;
- recommendation: `PASS`, `PASS WITH BOUNDED CLAIMS`, or `NEEDS MANUAL SCIENCE`.

Do not claim Nature readiness. Say whether the branch meets this repo's
Nature-grade retention bar or exactly what remains open.
