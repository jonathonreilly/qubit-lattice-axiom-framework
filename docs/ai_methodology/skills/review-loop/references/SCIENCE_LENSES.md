# Scientific review lenses and findings

Required for every review and affected-fix confirmation. Read the Review depth section first: it says whether the unit gets a scope read or the full read. In a full read, apply every lens whose trigger matches the actual content; conditional triggers are mandatory. The [focused landing review depth](../SKILL.md#focused-landing-review-owner-directed-2026-09-08) governs report granularity, while complete argument reading and independent checks remain required.

## Review depth

Owner choice, 2026-11-10 (`docs/ai_methodology/SETTINGS.md`, Landing review).
Being on `main` means that a change was reviewed for honest scope and clean
integration. It grants no standing (`docs/ai_methodology/RULES.md`, sections 1
and 3). A landing read therefore has one of two depths. A script reads the
depth from the unit's delta:

```bash
python3 docs/ai_methodology/skills/review-loop/scripts/review_depth.py \
  --base origin/main <unit-head> [<unit-head> ...]
```

It prints `DEPTH scope` only when every changed path is working material:

| Path | Change that counts |
|---|---|
| `.claude/science/` | any |
| `research/` | any |
| `docs/<name>.md` | added |
| `logs/runner-cache/` | added |

Every other change gets the full read and prints `DEPTH full`. That covers a
changed, renamed or deleted file that `main` already holds outside the two
working folders. It also covers a new file anywhere else: rules, procedures,
commands, tools, tests, audit data, controlled data and publication surfaces.
New files under `scripts/` get the full read: a path alone cannot distinguish
a science runner from an operational tool.
One such path gives the whole unit the full read. If the script prints no
`DEPTH` line, the unit gets the full read. The table is the script's
`WORKING_MATERIAL` list, and the contract check fails when the two differ.

The reviewer or the lander may raise a unit to the full read and records the
reason. Nobody lowers a depth. Raise it when the owner or the request asks,
or when the text alone cannot settle a question of honest scope.

### Scope read

A scope read asks one question: does the text say more than the work shows?
Read every title, summary, status line and statement in the changed Markdown
files, with the premises and domain that each statement gives. Do not read
proofs, derivations, runner code or logs, except to find a number that the
text quotes. Report these as findings, and nothing else:

1. A title, summary or status line that claims more than the statements
   under it.
2. A statement that uses a premise, a domain limit, an imported value or a
   published result that it does not name. A published result is named with
   its authors and is `argued` unless a check record says more.
3. Words that grant standing or an audit verdict, or that call the work
   checked, retained, established or audited. The `proposed_` labels that
   the validators require are not such words.
4. A negative result that is worded beyond the family it rules out, or a
   failed search that is presented as an obstruction.
5. A fit, or a match found after the fact, that is presented as a
   prediction.
6. A quoted number or runner result that no committed log or cache shows.
7. A new axiom, primitive or framework premise.
8. An error that the reader sees while it reads. The reader does not search
   for errors by derivation.

Then list, apart from the findings, each statement that `RULES.md` section 3
says to check before other work builds on it: a bridge that fixes an
observable, a dynamics, a symmetry or a normalization; an interface between
parts; an assembly; a result that matches a target unexpectedly well. The
list holds nothing back from landing. The lander writes it on the PR.

Where a lens, a gate or another passage of this skill asks for more than this
list, it describes the full read. The source map, the pre-fix mechanics,
same-session acceptance of fixes, every gate of `AUDIT_COMPATIBILITY.md`
except gates 9 to 11, and the combined gate are the same at both depths.

A scope read files no check record and moves no standing. What it admits is
`argued`. It can admit a proof that has an error in it, a runner that does not
test its claim, and runner code that no reviewer has read. A check finds
those, where `RULES.md` section 3 says a check pays.

Report shape:

```text
## Scope read (iteration N)
Depth: scope (review_depth.py: <its "working material" line>)
Read: <n> Markdown files, <UTC start> to <UTC end>
### Scope: PASS | FIX | RAISE
Findings: <number from the list, file and line, the words at fault, the
narrowest fix>
Check before other work builds on it: <statement and file, or "none seen">
```

### Full read

The rest of this file describes the full read, together with gates 9 to 11 of
`AUDIT_COMPATIBILITY.md`. A full-read report states `Depth: full` and the
reason that `review_depth.py` printed or that the person who raised it gave.

## Reviewer Fanout

On each iteration, set `files_to_review` to the files that changed since their
last clean review. On iteration 1, use all original changed files.

Apply the relevant lenses in the default single fast-reviewer unit review.
Record their material conclusions in the concise unit report. Use an extra
strongest-configured-reviewer seat only for the unresolved question that needs it. The lens
names below identify responsibilities, not mandatory separate workers or
standalone reports. When independent agents are unavailable, report that
limitation; an author's self-review is not independent confirmation.

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
  Run adversarial mutation tests that corrupt each decisive formula, threshold,
  expected value, or assertion and confirm the runner fails for the intended
  reason; a runner that survives a load-bearing mutation does not validate it.

- `PhysicsClaimReviewer`
  Attack theorem notes, claims tables, publication surfaces, and prose. Check
  semantic bridges, selector assumptions, status labels, exact/bounded/support
  boundaries, and code/prose drift.

- `ProofObligationReviewer`
  Trigger when changed content claims a theorem, proof, derivation, reduction,
  or closure through a nontrivial intermediate lemma. Apply
  [`docs/ai_methodology/skills/physics-loop/references/proof-search-governance.md`](../../physics-loop/references/proof-search-governance.md).
  Reconstruct the exact target contract and proof-obligation graph; check
  hypothesis preservation, admissibility of constructed objects, boundary and
  degenerate cases, circular use of equivalent statements, and whether the
  strongest unresolved lemma is weaker than, equivalent to, or stronger than
  the target. Output `CLOSED`, `CONDITIONAL`, `EQUIVALENT-GAP`, or `FAIL`.
  An elegant reduction ending in a target-equivalent lemma is not near
  closure and must not receive proof-complete framing.

- `ImportSupportReviewer`
  Inventory every measured, fitted, literature, PDG, cosmological,
  normalization, boundary-condition, or convention input. Classify each as
  `zero-input structural`, `framework-derived`, `one computed lattice input`,
  `explicit normalization/boundary condition`, `standard/literature
  correction`, `observational comparator`, `support-only`, `insensitive
  nuisance`, or `unjustified import`. For a Nature-grade retention claim, every
  import must be derived, disclosed as a non-satisfying condition with a narrow role, quantitatively
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
  a negative claim. The reviewer answers the obstruction questions in
  [`docs/ai_methodology/procedures/check.md`](../../../procedures/check.md):
  is the family ruled out stated with explicit quantifiers, and does every
  title, summary and citing statement claim no more than that. An open
  admissible route inside the family fails the claim; an escape outside it
  refutes nothing. The N1-N8 prompts of the `no-go-discipline` skill
  ([`SKILL.md`](../../no-go-discipline/SKILL.md)) are an aid, never a
  requirement. Output `PASS` (negative claim honestly scoped) or `FAIL` with
  the failing question or the open route named and the narrowest honest
  claim proposed. Under-tested negative claims are at least as harmful as
  overclaimed positive ones because they foreclose investigation paths.

- `LabelingConventionReviewer`
  Detect labeling/naming/convention content masquerading as a bounded
  theorem. Trigger whenever changed content includes a `bounded_theorem`
  candidate whose load-bearing claim is a labeling/naming/convention
  statement (parallel to the u/c/t mass-ordering convention or the
  e/μ/τ charged-lepton naming) rather than an algebraic claim with
  explicit named conditions. A labeling convention has no propositional
  premise content, so `retained_bounded` grade does not apply — the
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
  conditions, `SPLIT-REQUIRED` if labeling content is bundled with
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
  `docs/work_history/repo/review_feedback/`, front-of-house edits update
  `docs/KEY_SCIENCE.md` without treating that index as status authority, status
  wording follows `docs/repo/CONTROLLED_VOCABULARY.md`, and changed claim notes
  are compatible with the audit lane's propose/ratify split. The deferred paper
  package under `archive/publication/ci3_z3/` is record-only; reject any stale PR
  that recreates its former live tree unless the owner explicitly authorizes an
  archive-promotion lane. Also verify that load-bearing dependencies are real
  markdown links that seed the citation graph, not just code-formatted file
  names in prose. Block ambiguous new science names such
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
  without answering the obstruction questions of `procedures/check.md`
  against the branch content. An unscrutinized negative claim forecloses
  investigation paths and is at least as harmful as an overclaimed positive.
- Do not approve proof-complete framing until the ProofObligationReviewer has
  reconstructed the obligation graph and ruled out target-equivalent missing
  lemmas, circular reductions, and uncovered edge cases.
````

## Consolidate Findings

Present one iteration summary:

```text
## Review Results (Iteration N)

### Code / Runner: PASS | RISK | FAIL
### Physics Claim Boundary: RETAINED | SUPPORT | BOUNDED | OPEN | REJECT
### Proof Obligations: CLOSED | CONDITIONAL | EQUIVALENT-GAP | FAIL | NOT APPLICABLE
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
- `PROOF_OBLIGATION`
- `EQUIVALENT_STRENGTH_GAP`
- `SEMANTIC_BRIDGE`
- `REPO_GOVERNANCE`
- `AUDIT_COMPATIBILITY`
- `NIT`
- `SALVAGE_CANDIDATE`
- `SALVAGE_REJECT`

Stop immediately when all applicable reviewers are clean.
