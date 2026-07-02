# /review-loop — Physics Review Loop

Run the repo-native physics review loop from:

`docs/ai_methodology/skills/review-loop/SKILL.md`

## Invocation

`/review-loop [focus] [--max-iterations N] [--no-fix] [--no-commit]`

## Required Behavior

1. Read the skill file above before acting.
2. Review only branch/local changes against `origin/main` or `main`.
3. Fan out the physics reviewers in parallel when the agent environment allows:
   `CodeRunnerReviewer`, `PhysicsClaimReviewer`, `ImportSupportReviewer`,
   `NatureRetentionReviewer`, `NoGoDisciplineReviewer` (when negative claims
   changed), `LabelingConventionReviewer` (when bounded-theorem candidates
   changed), `RepoGovernanceReviewer`, and optionally
   `MethodologySkillReviewer`.
4. Fix only verified, narrow findings. Demote overclaims instead of patching
   missing science with prose.
5. Enforce audit-system compatibility without running the independent audit:
   no bare `retained` / `promoted` status lines, seed changed claims through
   `docs/audit/scripts/run_pipeline.sh`, and require
   `python3 docs/audit/scripts/audit_lint.py --strict` to pass.
6. Treat review as the canonical science gate: the independent audit should be
   mostly confirmatory. Block PASS when a changed claim has missing graph
   dependencies, author-prewritten audit verdicts, stale retained-status
   assumptions, or a runner that does not test the load-bearing bridge.
7. For math-bearing runner/proof changes, do not trust PASS output alone:
   independently cross-check load-bearing formulas, signs, factors,
   normalizations, expected values, and edge cases before landing.
8. Before classifying a dependency as an import, wall, Tier-A admission, or
   bounded-status source, read
   `docs/ai_methodology/skills/PRIMITIVE_REGISTRY_CHECK.md`,
   `docs/audit/data/axiom_premise_nodes.json`, and any relevant primitive
   source note. The registered `scale_reference_primitive` grants the Planck
   scale reference as units conversion only; it is not a bounded Planck import.
   The registered `kinetic_isotropy_primitive` grants only structural OS0
   kinetic-form isotropy `c_t = c_s`; it is not a bounded import, Lorentz
   theorem, dynamics, scale, spacing-ratio theorem, selector, or empirical
   input. The registered `realized_state_primitive` grants only pointwise evaluation at a supplied law-admissible realized state; it does not supply a state, state-selection rule, measure, typicality or genericity assumption, weighting, probability rule, or any state-contingent value (quantities that vary across the law-admissible family remain registered data).
9. Re-review only files changed by the fix pass, plus interacting files that
   were already in the original changed-file set.
10. Before closing or rejecting a non-landable PR, run the skill's salvage pass:
   preserve any durable, runner-backed lemma in the same requested landing path
   with a canonical claim type, and explicitly reject only the pieces that
   cannot be salvaged without new science.
   Non-science audit/status or hygiene PRs still need a utility review:
   salvage durable audit-graph, cache, queue, normalization, dependency-chain,
   or audit-readiness repairs into source/tooling/pipeline changes and
   regenerate generated surfaces instead of rejecting them just because they
   are not theorem science.
11. Draft PRs are out of scope for `/review-loop`: ignore draft-status PRs and
   never land them unless the user explicitly asks for draft inspection without
   landing.
12. End with a concise report covering imports/support status, retained/bounded
   disposition, salvage disposition, audit-readiness, commits, checks, and
   remaining manual science.

## Non-Negotiables

- Every imported or measured value must be identified.
- Support-only results must not be promoted to retained claims.
- Source-note `Status:` lines may not contain bare `retained` or `promoted`;
  use `proposed_retained`, `proposed_promoted`, `support`, `bounded`, or
  `open`. The audit lane alone grants effective retained status.
- Authors and review packets must not prefill audit verdicts such as
  `target_audit_status: audited_clean`, `audit_status = audited_clean`, or
  `effective_status = retained`; say that audit status is set only by the
  independent audit lane and effective status is pipeline-derived.
- Load-bearing dependencies in changed claim notes must be markdown links that
  seed the citation graph. After the audit pipeline, changed claim rows must
  show the intended deps in `docs/audit/data/audit_ledger.json`.
- New landed science must use explicit repo naming from
  `docs/repo/CONTROLLED_VOCABULARY.md`. Do not approve bare overloaded labels
  such as `A1`, `A2`, `G1`, `R3`, `Route F`, or `Block 2` as theorem/lane
  names, table labels, claim scopes, runner headlines, or review findings.
  Use names such as `Qubit` / `site possibility` / `one-site possibility
  domain` (the local algebraic presentation fixed by
  `MINIMAL_AXIOMS_2026-06-29.md`, with `Cl(3,0)` as equivalent notation),
  `Lattice` / `Z^3 lattice`, `Admissibility` / `local constraint`,
  `Record` / fixed record readout,
  `Koide Frobenius-equipartition condition`, or `Lie type A_1`; the
  `M_2(ℂ)` / `Cl(3,0)` / qubit names are labels for the same one-site
  algebraic presentation. Keep shorthand only as a parenthetical legacy alias.
- `retained`, `retained_bounded`, and `retained_no_go` are the retained-grade
  dependency statuses. Reviewers must reject stale exact-status checks that
  require only `effective_status = retained` when bounded/no-go retained
  grades are valid.
- Approved primitives listed in `docs/audit/data/axiom_premise_nodes.json`
  chain-satisfy dependencies without making rows `retained_bounded`. Do not
  call the registered `scale_reference_primitive` a Planck import, Tier-A
  admission, missing premise, no-go wall, or bounded-status source. Do not
  grant it more than `docs/SCALE_REFERENCE_PRIMITIVE_NOTE.md` declares. Do not
  call the registered `kinetic_isotropy_primitive` a Tier-A admission, missing
  premise, no-go wall, bounded-status source, Lorentz theorem, dynamics, scale,
  spacing-ratio theorem, selector, or empirical input; do not grant it more
  than `docs/KINETIC_ISOTROPY_PRIMITIVE_NOTE_2026-06-09.md` declares. Do not
  call the registered `realized_state_primitive` a Tier-A admission, missing
  premise, no-go wall, bounded-status source, state-selection rule, measure,
  typicality assumption, weighting, or value source; do not grant it more
  than `docs/REALIZED_STATE_PRIMITIVE_NOTE_2026-06-11.md` declares.
- `/review-loop` must not apply audit verdicts. It prepares
  audit-compatible review surfaces and reports which proposed claims require
  the independent audit worker.
- `/review-loop` is review, not audit. It may run the compatibility pipeline
  and strict lint, but it must not claim an audit verdict, apply auditor
  results, or describe its review as an audit.
- `/review-loop` must not create or open pull requests. If science is
  salvageable, land the source-only salvage and dependency-chain/audit-queue
  repairs as part of the current landing path; otherwise close or reject the
  existing PR with a clear reason.
- A PR whose purpose is repairing a stuck terminal ledger row
  (`audited_conditional` / `audited_renaming` / `audited_failed` /
  `audited_numerical_match`) must leave that row requeue-able: the row's own
  note or paired runner must change in the PR, or the PR must ship
  machine-readable re-audit targeting metadata (a dispatcher sidecar) naming
  the row. Dependent-side edits alone never reschedule the stuck row. When
  the audit-named repair is dependent-side only (for example, narrowing
  dependents' citing sentences), add a dated downstream-hygiene line to the
  stuck row's own note boundary as part of the landing — a source-side fact,
  no grade language. Verify with the validation pipeline that the row
  re-enters the queue, then restore generated audit outputs per the
  pipeline-output-stripped gate.
- `/review-loop` must ignore draft-status PRs. Drafts are not candidates for
  landing, review-loop comments, or salvage unless the user explicitly asks for
  draft inspection without landing.
- When integrating PRs, `/review-loop` must not checkout whole files from a
  stale PR head over current `main`. Compute the PR merge base, detect overlap
  between files changed on current `main` and files changed by the PR, and use
  three-way patch/rebase/merge/cherry-pick integration for overlapping paths.
  Whole-file checkout is allowed only for new paths or paths proven unchanged
  on current `main` since the PR base.
- The repo baseline is the four named axioms in
  `MINIMAL_AXIOMS_2026-06-29.md`: Lattice, Qubit, Admissibility, and Record.
  Name them explicitly; do not compress them to bare `A1` / `A2` / `A3` /
  `A4` labels. Do not classify that baseline as a new admitted premise,
  regulator interpretation, or optional theory language. Do not let that
  baseline silently promote separate species identifications, selectors,
  probability or occurrence rules, K/CPT or central-sector structure,
  P2/modulus, log-det structure, source/action bridges, empirical matches, or
  parent theorem/status surfaces.
- Nature-grade retention requires derived or explicitly admitted inputs,
  decisive artifact support, clear falsifiers, and no hidden semantic bridge.
- Math-bearing runners require independent formula review: PASS lines do not
  establish that the runner's expression, sign, factor, normalization, or
  expected value is correct.
- Branch-local or draft-PR vocabulary, including language leaked from PR230 or
  similar long-lived drafts, must be translated to native repo language before
  landing.
- Closing a PR must not discard durable science. Salvage narrow
  theorem/no-go/open-gate lemmas into canonical source-only landing commits
  when the runner directly supports the narrowed claim and no audit
  verdict/status language is carried over.
- Closing a PR must not discard durable audit-process value either. A generated
  audit/status diff can be evidence of a real repo defect; land the underlying
  source/tooling/pipeline repair when it strengthens auditability, but never
  treat hand-authored generated status as the authority.
- Delete a closed PR's head branch **only if durable content actually landed**
  (salvaged to `main`, or merged): then `gh pr close <N> --delete-branch`, so
  stale heads don't accumulate (review-loop closes rather than merges, so
  auto-delete-on-merge never fires). **Do not delete the branch when a PR is
  closed without landing its content** (rejected / nothing salvaged / salvage
  deferred) -- keep it as the handle on the un-landed work. Never delete a head
  that still backs another open PR, nor `main`.
- Live unresolved review findings belong in `docs/repo/ACTIVE_REVIEW_QUEUE.md`.
- Long historical packets belong in `docs/work_history/repo/review_feedback/`.
