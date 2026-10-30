# Long-Running Execution

Use this reference when `physics-loop` is asked to run unattended, or when a
target is shared by more than one session (see Lab Operation).

## Runtime Prompt

If the user did not pass `--runtime`, ask before launch:

```text
How long should this physics loop run unattended?
```

Accept compact durations such as `30m`, `2h`, `6h`, or `12h`. Do not assume a
default runtime for execution. If the user asked only for a plan or status, do
not ask.

For a request such as "run for 12 hours unattended", treat the duration as a
campaign work budget. Keep selecting useful science opportunities until the
deadline or max-cycle limit, subject to the parent skill's quality-exhaustion
and safety/tooling stop conditions. Runtime is not a production quota.

## Preflight

Before modifying files or running long tasks:

1. Fetch current main: `git fetch origin`.
2. Check `git status --short --branch`.
3. Start from a clean branch off `origin/main`. If the current worktree is
   dirty or contains unrelated work, create a separate clean worktree from
   `origin/main` before launching unattended science. Stop only if a clean
   independent worktree cannot be created.
4. Default to `--delivery milestone`: related blocks may compose on one
   isolated campaign branch with a provisional dependency map. When
   `--delivery block` is requested, use branches such as
   `physics-loop/<slug>-blockNN-YYYYMMDD`.
5. Check the cooperative lock if available:
   `python3 scripts/automation_lock.py status`.
6. If the lock is free, acquire it with a TTL that covers the next checkpoint
   window:
   `python3 scripts/automation_lock.py acquire --owner physics-loop --purpose "<slug>" --ttl-hours N`.
7. If the repo lock path is unavailable, record the failure and use a
   branch-local supervisor lock. Lock unavailability is not a campaign stop
   unless another active worker owns the same repo/task and no independent
   worktree is possible.
8. Record start time, runtime, target stop time, branch, delivery mode, next
   milestone, and checkpoint interval in `STATE.yaml`.
9. Follow `docs/ai_methodology/SCIENCE_WORKFLOW.md` section 10 for the worktree
   and for the preflight before launching any long worker or numeric job.

## Checkpoints

Checkpoint:

- after grounding;
- after route selection;
- before and after each deep stretch attempt;
- before and after stuck fan-out synthesis;
- before and after long scripts;
- after every artifact;
- after every author or independent check;
- at least once per checkpoint interval;
- before any authorized campaign stop.

Each checkpoint updates `STATE.yaml`, `TRACE_GATE.md`, and `HANDOFF.md` with:

- current cycle and route;
- current science block and branch;
- provisional dependencies, inherited hypotheses, focused independent checks,
  and conclusions affected by changed premises;
- current hard residual, `A_min`, and forbidden imports when in stretch mode;
- files changed;
- commands run and results;
- imports retired/exposed;
- trace-gate classification and reachability to any known blocker;
- review findings;
- PR status for the block;
- next exact action;
- reason for continuing or stopping.

On a shared target, a checkpoint updates the part file instead (Lab Operation).

Refresh the lock before it expires. If the repo lock cannot be refreshed,
continue under a branch-local supervisor lock when safe and record the degraded
lock mode. Stop only for a real ownership conflict that prevents safe
independent work.

## Unattended Decision Policy

Avoid mid-run questions. When a decision is needed:

- choose the narrowest honest claim status;
- prefer no-go/archive/demotion over unsupported promotion, but do not choose
  an easy no-go when a named hard residual has not yet received a stretch
  attempt;
- choose the highest-scoring route that passes the dramatic-step gate;
- maintain `OPPORTUNITY_QUEUE.md`; after one lane blocks, pivot to the next
  useful unresolved obligation or discriminator while runtime remains;
- after repeated audit/no-go/blocker cycles, reassess underexplored hard
  mechanisms and attempt one if it can add evidence;
- before declaring global queue exhaustion, inspect materially different live
  routes and synthesize the evidence. Three to five frames is a planning target
  when useful routes exist, not permission to manufacture nominal alternatives;
- treat `--deep-block` as a protected work allocation, not minimum elapsed time.
  A decisive result or exhausted mechanism justifies pivoting; use remaining
  authorized runtime for useful independent work, never busy-waiting;
- skip ambiguous fixes that need human physics judgment for the current lane,
  then checkpoint and pivot;
- treat review `demote`/`block`, failed retained-proposal certification, and
  optional route tooling failure as block-level outcomes, not campaign stops;
- leave clear handoff notes for decisions that require the user.

## Campaign Continuation

The loop should not exit early while runtime remains because one block is
finished or blocked.

When a block reaches a local stop:

1. update `CLAIM_STATUS_CERTIFICATE.md` and `TRACE_GATE.md`, then demote any
   unsafe wording, using
   `proposed_retained` / `proposed_promoted` only for audit-ready author
   proposals and never as audit-ratified status;
2. run the smallest relevant checks;
3. preserve the checkpoint and coherent source work on the campaign branch;
   open a PR only at a review-ready milestone, or a review-ready block in block
   mode, and record actual delivery failures in `PR_BACKLOG.md`;
4. refresh `OPPORTUNITY_QUEUE.md`;
5. start a new science block for the next ranked opportunity.

Only stop the whole campaign before the deadline if:

- a clean independent worktree cannot be maintained;
- all viable queued opportunities are globally blocked and documented in
  `OPPORTUNITY_QUEUE.md`;
- the parent skill's corollary/value-gate exhaustion conditions are evidenced;
- core local tooling needed for every viable route is unavailable;
- another active worker owns the same task and no non-overlapping target can be
  selected.

## Commits And Pushes

Create incremental commits only for coherent science artifacts when the user
requested a run and did not pass `--no-commit`. Related provisional blocks may
share a coherent campaign branch; maintain exact dependency revisions and
inherited conditions. Use block branches when block delivery is requested. Do
not commit unrelated pre-existing changes.

Physics-loop delivery preserves dedicated campaign or science block branches on
`origin`. Do not push science to `main`. Do not merge or weave the science
through repo-wide authority surfaces during the loop run.

## Review PR Backlog

At a review-ready milestone, or each review-ready block under `--delivery block`,
and at an explicit or final handoff when coherent work is ready, unless `--no-pr`
was supplied:

1. For each review-ready campaign or science block branch, run the required checks
   that fit remaining runtime.
2. Push the branch to `origin`.
3. Open one PR per coherent milestone (or block in block mode) with `gh pr create`.
4. Base independent block PRs on `main`; base dependent block PRs on the prior
   block branch and mark them as stacked.
5. Include links to `HANDOFF.md`, `TRACE_GATE.md`, `REVIEW_HISTORY.md`,
   theorem notes, runners, logs, verification commands/results, imports
   retired/exposed, trace reachability, and remaining blockers.
6. Use the parent skill's title contract, with both intended claim type and
   honest author support status, e.g.
   `[physics-loop] <slug> milestone NN: bounded_theorem bounded-support`.
7. Never merge the PR. The review-loop/backpressure process decides landing.

If `gh` is unavailable or not authenticated, write `PR_BACKLOG.md` immediately
with exact `gh pr create` commands, branch names, bases, titles, and body-file
paths. This is a degraded delivery, not a reason to discard the block or stop
the campaign while runtime remains.

If runtime is nearly exhausted and work is not coherent enough to commit, write
the loop pack and handoff instead of forcing a commit. If substantial runtime
remains, do not leave incoherent work idle; checkpoint it as abandoned or
historical, then pivot to the next opportunity.

## Stop Cleanly

At stop:

1. Run the smallest relevant checks that fit the remaining runtime.
2. Update `REVIEW_HISTORY.md` and `HANDOFF.md`.
3. Commit coherent work if allowed and appropriate.
4. Push dedicated campaign/block branches to `origin` if they have commits.
5. Open or prepare review-ready milestone PRs unless `--no-pr` was supplied;
   preserve incomplete work with its exact next step without forcing a PR.
6. Release the lock if held and no child process is running.
7. Report status, branch/PR names, artifacts, remaining blockers, and exact resume
   command.

Do not run this stop sequence just because a lane hit a no-go, review demotion,
human-judgment blocker, dirty PR, or missing PR auth. Those are checkpoint and
pivot events during a 12-hour campaign.

## Lab Operation

Use this when more than one session, provider or machine works on one target, or
when a hard target needs attempts that outlive a session. A bounded task in one
session does not need it. All of it is research-stage working practice under
`docs/ai_methodology/SCIENCE_WORKFLOW.md` section 10 and grants no status.
Anything specific to one target, such as its conventions, budgets, provider
roster and lessons, stays in that target's folder.

### Roles

| Role | How many | Decides | Does not |
|---|---|---|---|
| Owner | 1 | Goals, axiom edits, public posts, spending, pace | Choose between scientific forks |
| Target lead | 1 per target | Parts, interface statements, budgets, which route gets the next budget | Settle by rank whether a step is right |
| Part lead | 1 per part | What its part file says | Change an interface statement alone |
| Worker | Many | Nothing beyond its dispatch (`workhorse` skill) | Edit a file it does not hold; it returns evidence to its lead |
| Checker | Many | The research-gate signal | Check its own lineage |

Any provider, or a person, can hold any role if it meets the target's model
floor. A lead is a durable role held by whichever session has the lease. One
session may hold several roles, except checker on its own work. The owner or the
orchestrator names the first target lead.

### Shared state

A target is a branch plus its loop pack, listed by one line (slug, branch,
folder) in `CAMPAIGN_STATUS.md` on `ai/execution`. Each file has one writer, so
there is no shared board to conflict on:

| File | Writer | Holds |
|---|---|---|
| `GOAL.md` | Target lead | Target contract, critical path, interface statements with their producers and consumers, model floors, its own lead and lease |
| `parts/<part>.md` | Part lead | Lead and lease, state of attack, obligations, requests, the living text |
| `parts/<part>--<route>.md` | That attempt's session | One attempt beside the part: lead, lease, state of attack, text |
| `library/<lemma>.md` | Its author | A rebuilt literature lemma, with credit |
| `gates/<statement>-<commit>.md` | Its checker | One research-gate report |

A part file opens as below. The state of attack gives the current formulation,
the hardest remaining obligation, routes tried and why they failed, and the next
action. Edit in place; git keeps the history.

```text
lead: <provider>/<model>/<effort> <session id>
lease_until: 2026-10-30T18:00Z

## State of attack

## Obligations
- gap: <descriptive name> -> <consumer>
- unchecked: <descriptive name> given <hypotheses> -> <consumer>
- implication: <descriptive name> given <hypotheses> -> <consumer>
- discharged: <descriptive name> -> <consumer>

## Requests
- <part or interface>: <what is asked and why>
```

| Label | Meaning | Written |
|---|---|---|
| `gap` | No argument or result yet | Any time |
| `unchecked` | Argument or computation written, no research gate yet | Any time |
| `implication` | A research gate confirmed it, given named hypotheses | After a gate |
| `discharged` | A research gate confirmed it, with no open hypothesis | After a gate |

An obligation may be a theorem, a computation with stated uncertainty, an
observable map or a discriminating test. List only obligations on the critical
path. Use descriptive names, never bare codes. Labels stay in the target folder;
a milestone PR uses the existing claim types and status words.

`python3 scripts/lab_ops.py status <target folder>` prints leads, leases, requests
and the open count from these files. Nobody writes that summary by hand.

Model floors are lines in `GOAL.md`, one per role:
`model_floor <role>: <model>@<effort>, <model>`. Preflight, given `--target`,
`--role`, `--model` and `--effort`, refuses anything not listed. With no floor
declared, use the configured model.

### Working on the branch

- Each session has its own worktree and local branch, since git allows a branch
  in only one worktree:
  `python3 scripts/lab_ops.py worktree-add <name> --target <target-branch> --path <target folder>`.
  Share with
  `git pull --rebase origin <target-branch> && git push origin HEAD:<target-branch>`.
  Never force-push a target branch.
- Push at every stop. Work that is not pushed does not exist for the lab. Commits
  carry a trailer, `Provenance: <provider>/<model>/<effort> <session id>`, which
  records who did the work and claims neither quality nor independence.
- Between milestones a stop updates only the part file. The other pack files,
  source hashes and conformance work are brought current when a milestone PR is
  prepared. This overrides the per-checkpoint file lists in this reference and in
  `CAMPAIGN.md`.
- Cut each milestone PR on its own branch, so later pushes do not move the head
  under review.
- To ask for a change in another part or in an interface, add a line under
  `## Requests` in your own file. Leads read requests at each stop. The target
  lead decides interface changes and marks affected consumers when one changes.

### Leases

Only leads hold leases, one per file. To take or renew one, commit `lead` and
`lease_until` (UTC, past your next checkpoint) and push. Git decides who was
first: a rejected push means fetch, re-read and decide again, and a rebase conflict
on a lease line means you lost, so abort it. An expired lease can be taken the same
way; a returning holder then works through the new lead, offering its unpushed
work as a request or an attempt file. A session whose
sandbox cannot push cannot hold a lease, so whoever launched it holds it and
pushes for it. Bounded tasks and probes need no lease: duplicated work is wasteful
but safe.

### Handover

A handover is complete when a fresh session on any provider can state the hardest
remaining obligation and the next action from the pushed branch alone. The new
lead writes both in its first commit; anything it cannot recover becomes a `gap`.
Session logs and provider resume commands are conveniences, never the record.

### Disagreement

- About a route or an interface: the target lead states the fork and its decisive
  test, runs a probe on each side, decides on the result and records the dissent
  in `GOAL.md`. The owner is not asked.
- If the test does not decide: both routes stay open with reopen conditions, and
  the target lead sets their budgets.
- About whether a step is right: rank and majority decide nothing
  (`SCIENCE_WORKFLOW.md` section 2, rule 8). The statement stays `unchecked` until
  a checker on a different path settles it.
- Two sessions claiming one lead role: the first pushed lease holds. The other
  takes a part or a probe.

### Units of work

Split only what can be frozen. A statement whose form is still changing is not a
leaf: keep it in one sustained attempt, or race it.

- **Sustained attempt.** One long resumed session on one part or obligation, with
  a budget set before launch. Whoever launched it ends it, never the session doing
  it, at one of three exits: the obligation follows from statements already in the
  target; a counterexample in the actual setting, with a proposed edit; or a budget
  stop with a dated log of distinct routes tried. A conditional result with a new
  named lemma is a checkpoint, never an exit. An honest gap is never a failure.
  Extend the budget only while hypotheses are being discharged or new routes
  tried. The `workhorse` skill gives the resume loop.
- **Race.** Two or more independent sustained attempts on one hard obligation,
  across providers where possible, with the neutral briefs of Independent Search
  Rounds in `proof-search-governance.md`. The part lead ends it and keeps the failed
  routes in the state of attack.
- **Bounded task.** A `workhorse` dispatch with a frozen statement and a named
  consumer. It closes only when the statement is proved as written. A
  counterexample or an exact missing obligation goes back to the lead.
- **Probe.** A cheap test of a fork or a risk, with its decisive outcome stated
  first.

### Research gates

Hold one when a part offers a statement for another part to build on, and when the
whole target is assembled. Do not review note by note during research. Inside an
attempt, run a skeptic pass at checkpoints; that is a self-check, not a gate.

The checker gets the raw artifacts and a neutral brief, comes from a different
provider where one is available, reads line by line and names its provider, model
and effort in its report. `SCIENCE_WORKFLOW.md` section 2, rule 8 decides what
counts as independent. It answers three questions:

1. Is it right, including every cited number, log and source?
2. Are the open obligations fewer or strictly weaker? Use the Theorem-Strength Gap
   Test in `proof-search-governance.md`; relocating the target to an equivalent
   lemma does not count.
3. Which consumer's exact input does it deliver?

| Signal | Means | Next step |
|---|---|---|
| `advance` | Right, and yes to the other two | Label it `implication` or `discharged`; consumers may build on it |
| `correct-no-advance` | Right, but no smaller or delivers nothing | Keep it; it may be labelled `implication`, the count is unchanged and the attempt continues |
| `wrong` | Not right | Fix or withdraw it and mark its dependents affected |

At assembly of a theorem target the checker also runs the Candidate-Proof Audit in
`proof-search-governance.md`.

### Progress

Report the number of obligations on the critical path that are not yet
`discharged`, by name. `lab_ops.py status` computes it. A new named obligation
raises it; a rename does not lower it. Notes, lanes and PRs written are not
progress. A frontier target with no critical path reports the concrete changes of
`SCIENCE_WORKFLOW.md` section 7.
