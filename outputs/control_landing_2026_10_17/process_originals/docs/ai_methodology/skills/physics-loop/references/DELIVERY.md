This is an active part of the physics-loop skill. Read it when the
entry point routes the current operation here, from the same source
revision. Repository paths in code remain relative to the repository.

## Science Delivery And PR Policy

For science loops, work on an isolated coherent campaign branch. The default
`--delivery milestone` supports continuous discovery, selective independent
checks, and PRs/audits at meaningful milestones. `--delivery block` opens a PR
for each review-ready coherent block. Neither mode permits merging science PRs
or pushing science directly to `main` as part of the author run.

A milestone is an independently reviewable theorem or construction, a decisive
empirical result, a scoped negative theorem, a repaired source defect, or a
synthesis that closes a named obligation. Open its PR when the evidence and
conformance requirements are satisfied, at an explicit user handoff request,
or at the end of the authorized budget if the work is review-ready. An
incomplete block, routine checkpoint, or exhausted runtime does not force a PR.

- Start science execution from current `origin/main` after `git fetch origin`.
- Use a dedicated branch namespace such as `physics-loop/<slug>-YYYYMMDD`.
- If the current worktree is dirty or not disposable, create a clean worktree
  from `origin/main` instead of mixing loop output with other changes.
- Treat each coherent major cycle as a **science block**. In milestone mode,
  related blocks may compose on one campaign branch with a recorded dependency
  map. In block mode, prefer `physics-loop/<slug>-blockNN-YYYYMMDD`.
- If a block depends on prior unmerged block output, create a stacked PR whose
  base is the prior block branch. If independent, base it on `main`.
- Commit coherent science artifacts to the dedicated campaign/block branch and push it to
  `origin`.
- Before each commit, run `scripts/vocab_lint.py --fix` on the files
  being committed. The repo's process vocabulary is canonical in
  [`docs/repo/controlled_vocabulary.yaml`](../../../../repo/controlled_vocabulary.yaml)
  (design in
  [`VOCABULARY_HYGIENE_DESIGN.md`](../../../../repo/VOCABULARY_HYGIENE_DESIGN.md));
  routine local drift with non-link-aware rewrite rules is auto-rewritten as
  part of the commit. Link-aware filename suffix migrations and F-letter
  finding-label migrations are reported but deferred to Cleanup-2 tooling.
  Genuinely new terms that the lint cannot mechanically fix are recorded in the
  vocab-extension queue
  ([`docs/repo/vocab_extension_queue.json`](../../../../repo/vocab_extension_queue.json))
  independent of audit rows; they do not block the physics block from
  landing. Vocabulary drift is never a stop condition for a physics loop.
- At a review-ready milestone (or each review-ready block in block mode), unless
  `--no-pr` was supplied, open the PR without waiting for campaign completion. Use
  `gh pr create` when authenticated; otherwise write `PR_BACKLOG.md` with
  exact commands and reasons PR creation failed.
- After opening a PR, verify it with `gh pr view` or `gh pr list`. If the PR is
  dirty against its intended base, update the branch or explicitly mark it as
  stacked in the PR body and `HANDOFF.md`.
- If PR creation or verification fails for network/auth reasons, write a
  complete `PR_BACKLOG.md` and continue the campaign if runtime remains.
  Missing GitHub access is a delivery degradation, not a science stop.
- PR titles must include `[physics-loop]`, the lane/block slug, the block's
  claim type, AND its honest status — two separate slots, each drawn from its
  own canonical enum. A claim type is not a status. The claim type is one of
  `positive_theorem`, `bounded_theorem`, `no_go`, `open_gate`, `decoration`,
  `meta` (the `target_claim_type` enum in CLAIM_STATUS.md); the status is one of `open`,
  `no-go`, `exact-support`, `bounded-support`, `conditional-support`,
  `demotion`, `candidate-retained-grade` (the `actual_current_surface_status`
  enum in CLAIM_STATUS.md). Never let one family stand in for the other: "exact theorem"
  and "bounded theorem" are claim-type phrasings, and a title that offers one
  of them where the status belongs states no status at all. A hybrid phrase
  spanning both families is the same defect (conformance spec section 3).
- PR bodies must link the block's `HANDOFF.md`, `TRACE_GATE.md`, notes,
  runners, verification commands/results, review findings, imports
  retired/exposed, trace reachability, and remaining blockers.
- Do not merge, push science to `main`, or update repo-wide authority surfaces
  as part of the science run.

### Provisional Composition And Selective Checks

Discovery may build on unmerged or unaudited lemmas. Record each premise's
exact source revision, hypotheses, proof gaps, author checks, independent check
state, and dependents in the campaign pack. Derived consequences inherit every
unresolved condition; a coherent branch, passing runner, or reviewer agreement
does not make them retained framework authority.

Before extensive downstream reuse of a load-bearing provisional result, obtain
a focused independent check of its contested step. Prioritize high-fanout
dependencies, physical-identification bridges, unexpected matches, and changes
whose failure would invalidate substantial work. If the check is unavailable,
checkpoint the dependency and continue independent work or a small explicitly
conditional probe. Do not deepen a large unverified dependency chain.

Formal review and audit are milestone activities, or targeted checks requested
for a critical dependency; formal audit of every leaf is not a prerequisite for
exploration. The independent audit lane alone ratifies status after landing.
When a premise changes or fails, mark its provisional descendants affected and
recheck them before carrying their conclusions forward.

**Conformance gate — verify before the PR is opened, not after review says
so.** A block PR is not ready to request review until it has been checked,
section by section, against
`docs/ai_methodology/REVIEW_LOOP_PR_CONFORMANCE_SPEC.md`: 1 self-containment,
2 cache and execution discipline, 3 claim-scope honesty, 4 negative claims and
the N-gate, 5 proof obligations, 6 runner validity, 7 packet completeness,
8 links and citation graph, 9 note structure, 10 the propose/ratify boundary,
11 sourced facts and counts, 12 the pre-review gates. Every MUST in that
document is a generation-time requirement of this skill; failing one is a
defect to fix before the PR exists, not a finding to receive. Record the pass
in `REVIEW_HISTORY.md`, naming each section deliberately not applicable to the
block and why — an unrun section is not a passed section. That document
restates rules owned elsewhere and cites each owner: where it and a cited
skill, script, or vocabulary file disagree, the cited authority wins and the
disagreement is a defect in the spec, to be reported in `HANDOFF.md` rather
than followed.

Allowed science-branch output:

- theorem/support/no-go notes;
- scripts/runners and paired outputs needed to inspect the result;
- branch-local loop state under `.claude/science/physics-loops/`;
- review history and handoff notes for later integration.

Forbidden science-branch output (the audit lane is sole authority over
these; a framework PR that ships them overwrites ratified audit state at
merge):

- `docs/audit/data/` (any file, except the single citation-graph manifest
  carve-out stated below);
- `docs/audit/AUDIT_LEDGER.md`, `docs/audit/AUDIT_QUEUE.md`,
  `docs/audit/MISSING_DERIVATION_PROMPTS.md`;
- `docs/publication/ci3_z3/*_EFFECTIVE_STATUS.md` and
  `docs/publication/ci3_z3/PUBLICATION_AUDIT_DIVERGENCE.md`.

`bash docs/audit/scripts/run_pipeline.sh` may be invoked for validation
(to confirm the source repair is ingested and the runner row queued or
re-queued as intended), but the regenerated outputs above must be dropped
before commit. Drop by restoring the branch's OWN committed state, never by
importing another ref: `git checkout origin/main -- <paths>` writes the index
as well as the working tree, so on a stale or stacked branch — the normal case
under the parallel landing contract — it silently STAGES current-`main`'s
deltas on those generated surfaces relative to your HEAD.

```bash
python3 - <<'PY_CLEAN'
from pathlib import Path
import sys
sys.path.insert(0, "scripts")
from science_fix_loop import publication_changed_paths, strip_generated_audit_outputs
root = Path.cwd()
strip_generated_audit_outputs(root, publication_changed_paths(root))
PY_CLEAN
```

The one carve-out is `docs/audit/data/citation_graph_manifest.json`, and it is
conditional, proactive, and commit-time. The trigger is graph TOPOLOGY, not
markdown links alone: `docs/audit/scripts/build_citation_graph.py` registers
every non-skipped `docs/**/*.md` file as a graph node BEFORE it extracts any
edge, so a new note carrying only backticked provenance references is still a
new node, and `docs/audit/scripts/write_citation_graph_manifest.py` requires
acknowledgment for every added, removed, or rewired node. When the block's own
commits add or remove any graph node — including a note with zero markdown
links — or rewire any dependency edge, a refreshed manifest MUST co-land with
the block, or the enforced stage-18 guard blocks every subsequent pipeline run
on `main` until someone else lands the acknowledgment. Regenerate it
deterministically on the proposed tree *after* the drop above, read the
stage-18 delta against the tracked manifest before staging, then stage that
one path: acknowledgment is assertion that every added, removed, or rewired
node and edge is intended. Never hand-merge or hand-edit it, and stage it only
when the block's commits actually change graph topology — when they change
none, the correct staged set contains no manifest at all
(`docs/ai_methodology/skills/review-loop/SKILL.md` landing rule; conformance
spec section 8).

```bash
# Only when the block's commits add/remove a graph node or rewire an edge:
python3 docs/audit/scripts/run_citation_graph_build.py
python3 docs/audit/scripts/write_citation_graph_manifest.py
git add docs/audit/data/citation_graph_manifest.json
# Second line of defense: the staged set must be exactly the intended source
# paths plus, at most, the one manifest path.
git status --porcelain
```

Do not weave science results through `README`, `docs/repo/LANE_REGISTRY.yaml`,
`docs/work_history/repo/LANE_STATUS_BOARD.md`, publication matrices,
canonical-harness indexes, active review queues, or methodology docs during the
science run unless the user's task is explicitly a skill/governance update.
Record proposed weaving in `HANDOFF.md` for the later review process.

## Loop Pack

Create or update a durable pack under:

```text
.claude/science/physics-loops/<slug>/
  STATE.yaml
  GOAL.md
  ASSUMPTIONS_AND_IMPORTS.md
  ROUTE_PORTFOLIO.md
  APPROACH_REGISTRY.md
  OPPORTUNITY_QUEUE.md
  NO_GO_LEDGER.md
  LITERATURE_BRIDGES.md
  ARTIFACT_PLAN.md
  TRACE_GATE.md
  CLAIM_STATUS_CERTIFICATE.md
  REVIEW_HISTORY.md
  HANDOFF.md
  PR_BACKLOG.md
```

Legacy packs under `.claude/science/frontier-workstreams/<slug>/` may be read
for resume/migration, but new loop state should use `physics-loops`.

Use `STATE.yaml` as the resume surface: current goal, delivery mode, next
milestone, provisional dependency/check state, target status, runtime,
cycle/block count, active route, approach-family coverage, strongest unresolved
proof obligation, hard residual being attacked, files touched, open imports,
no-go routes, trace-gate classification, review findings, PR status, next exact
action, and stop condition.

For theorem, multi-step bridge, or hard-reduction targets, write the exact
target contract in `GOAL.md` and maintain `APPROACH_REGISTRY.md` using
[`references/proof-search-governance.md`](proof-search-governance.md).
Keep mathematical approach families separate from artifact types recorded in
`ROUTE_PORTFOLIO.md`.

Use `OPPORTUNITY_QUEUE.md` in campaign mode. Rank candidate science targets by
the evidence they could add to the user's objective:

- the exact unresolved proof obligation, empirical discriminator, or reusable
  construction and its path to a named downstream physical target;
- expected reduction of uncertainty or retirement of a load-bearing import,
  including a counterexample or a properly scoped negative result;
- verified downstream obligations unlocked, prioritizing shared upstream
  bottlenecks over extra instances of already established results;
- the first decisive check, estimated work and review cost, and available
  computation;
- premise risk, invalidation blast radius, branch size, and overlap with work
  already active or awaiting review.

Use qualitative estimates with reasons, not invented success probabilities.
Distinguish scientific dependency edges from mere citations when estimating
downstream value. A high row count, easier retained label, positive answer, or
new filename does not by itself move the TOE objective. Preserve an exploratory
route when it offers a concrete discriminator even if its chance of closure is
uncertain. Re-rank after new evidence rather than forcing a positive outcome.

Use `CLAIM_STATUS_CERTIFICATE.md` for every science block. It must record the
actual current-surface status, any conditional/hypothetical status, dependency
classes, open imports, review-loop disposition, the intended audit
`claim_type`, trace-gate classification, and whether independent audit remains
required.

Use `TRACE_GATE.md` for every coherent science block. It answers the
reachability question: "If this artifact is true, what exact claim, blocker,
import, or frontier surface does it move?" This is not a demand that all
frontier work already have a downstream consumer; it is a demand not to pretend
that frontier-only work closes a known lane.

Required trace-gate fields:

```yaml
trace_class: direct_blocker_closure|upstream_support|negative_route_pruning|frontier_discovery|methodology
target_claim_id: null|...
target_blocker_text: null|"..."
source_of_blocker_text: null|audit_ledger|review_loop|handoff|user_goal|frontier_question
reachability_to_target: closes|partially_closes|supports|prunes|unknown_frontier|none
artifact_role: theorem|runner_certificate|literature_bridge|no_go|demotion|tooling|frontier_probe
next_trace_action: "..."
```

Trace rules:

- `direct_blocker_closure` requires an exact quoted blocker or import and a
  concrete statement of how the artifact retires it.
- `upstream_support` must name the downstream consumer that could use it, or
  explicitly say the consumer is not yet known.
- `negative_route_pruning` must state which route is pruned and why the no-go
  applies to that route rather than a broader family.
- `frontier_discovery` is valid pure science output. It may have
  `target_claim_id: null`, `target_blocker_text: null`, and
  `reachability_to_target: unknown_frontier`, but the PR/body/handoff must not
  claim it closes, promotes, or retires any existing lane.
- Any retained-positive or promoted-positive proposal must have trace class
  `direct_blocker_closure` or a fully enumerated chain of trace entries whose
  last entry is `direct_blocker_closure`.

## Final Report

Report:

- loop slug and target;
- delivery mode, milestones reached, and provisional dependencies awaiting
  focused independent checks or formal audit;
- remote science branch;
- runtime used and cycles completed;
- scientific evidence gained: strongest proved result, counterexample,
  discriminator, import retired, or uncertainty reduced, with exact paths;
- claim-state movement achieved, separating author proposals, landed work,
  independent review, and audit-ratified status;
- trace-gate classification and whether the artifact reaches a known blocker
  or is frontier-only;
- imports retired or newly exposed;
- mathematical approach families explored and underexplored;
- strongest rigorously proved lemma plus the exact remaining proof obligation
  and its strength relation to the target;
- artifacts created and checks run;
- review-loop findings and disposition;
- commits and PRs created, if any;
- PRs that could not be opened, with exact recovery commands;
- remaining Nature-grade blockers;
- exact next action from `HANDOFF.md`.

Do not claim Nature-grade closure unless the assumptions/import ledger,
decisive artifact, and review-loop disposition all support it.
