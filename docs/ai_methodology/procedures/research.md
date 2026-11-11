# research

Attack one target until its critical-path obligations close, die or spend their
budget, with one session or many. `RULES.md` governs; this grants no standing.

## Use when

A target needs sustained work: a proof, a construction, a decisive computation
or a persistent wall. Not a frozen piece (`dispatch`) or a verdict (`check`).

## Takes

A goal, or a target to join (branch and folder). Before the first attempt
`GOAL.md` holds the target contract, kept neutral (it assumes no proof exists):

- the statement: quantifiers, domain, edge cases, and the weakenings and
  outcomes that do not count as closure;
- the `main` revision and each premise read: axiom, registered primitive,
  statement with its standing, or supplied condition;
- the search record, the exact missing obligation, and the consumer: the
  downstream question resolved, or "frontier, none yet", never an invented one;
- the decisive test and what counts as success, counterexample and inconclusive;
- the route chosen, why, what would reverse it, the date; budgets (run, attempt,
  checkpoint interval); binding caller limits (no commits, no PR).

## State

The folder `.claude/science/physics-loops/<slug>/` on the target branch, one
writer per file (`RULES.md` section 5). A solo target is one lead with one part.

| File | Writer | Holds |
|---|---|---|
| `GOAL.md` | Target lead | Contract, critical path, interfaces with producer and consumer, model floors, lease |
| `parts/<part>.md` | Part lead | The file below. `parts/<part>--<route>.md` is one attempt beside it, held by its session |
| `library/` | Each entry's author | Rebuilt published lemmas with credit; `lit-<topic>.md` search records |
| `checks/<statement>-<commit>.md` | Its checker | One check record |

```text
lead: <provider>/<model>/<effort> <session>
lease_until: <UTC time past your next checkpoint>
## State of attack
<formulation; hardest open obligation; routes tried and why failed; next action>
## Obligations
- open: <name> -> <consumer>
- argued: <name> given <premises> -> <consumer>
## Requests
- <part, interface or person>: <what is asked and what it blocks>
```

- List only critical-path obligations, named as in their check records (no
  spaces), as `open` or `argued`; `lab_ops.py status` computes the rest.
- Only leads hold leases, one per file: commit the two header lines and push. A
  rejected push or a conflict on a lease line means you lost. A session that
  cannot push holds none; its launcher does. Tasks and probes need none.
- To change another part or an interface, add a request to your own file; leads
  read requests at every stop and the target lead decides interfaces.

## Steps

1. **Ground.** Start with `lab_ops.py worktree-add`. Read the axioms and
   primitive registry from `origin/main`. At a fresh, recorded `main` commit,
   search for the statement itself, not only what contradicts it (`RULES.md`
   section 2, rule 7). Read each hit's proof and scope, not its title. Proved on
   matching premises: cite it and pick another target or repair its proof.
   Refuted at matching scope: its proof's escapes are the routes.
2. **Select.** Write the contract and critical path. Class routes by object,
   mechanism and terminal obligation, not artifact or session; rank by
   `SETTINGS.md`, Method defaults. Attempt only what could close, kill or
   isolate a critical-path obligation: a short standard proof that closes one
   is valuable, and a one-step variant that closes none is churn even when
   correct. A route ending at a lemma as strong as the target is blocked.
3. **Attempt.** Set the budget, then pick the unit: a sustained attempt on one
   obligation; a race of independent attempts under neutral briefs; a bounded
   task (`dispatch`); a probe with its decisive outcome stated first. Split only
   what can be frozen. A pass returns a lemma with its open steps named, a
   construction, a counterexample, or the exact missing lemma and failed step,
   never a status report. A part that keeps failing the same way gets the wall
   exercise; a map of attacks with nothing tried is not a result. Long and
   numeric jobs pass `lab_ops.py preflight`; numerics hold `numeric-lock`.
4. **Checkpoint.** Edit the part file, commit with the provenance trailer, and
   push with the command `lab_ops.py worktree-add` printed: after grounding,
   after selection, around long jobs, after each check, at each interval, before
   any stop. Between milestones a stop updates only the part file.
5. **Request a check.** Where `RULES.md` section 3 says a check pays, add a
   request naming the statement, its commit and its consumer; `check` runs it.
   Downstream work continues as `argued`; with no checker available, do
   independent work or a small conditional probe rather than build further on
   it. A `right` check that shrinks no open obligation closes nothing.
6. **Deliver.** A milestone is a reviewable theorem or construction, a decisive
   empirical result, a scoped obstruction, a repaired defect, or a synthesis
   closing a named obligation. First answer the pre-PR questions
   (`DISCOVERY.md`, step 8); a failed answer means no PR, not an easier one. Cut
   the PR on its own branch, pass the conformance spec section by section, list
   each statement with its computed standing, and verify it once open. From the
   third PR of one family in a run, hold it unless plainly new. A PR that cannot
   be opened becomes a request with its exact commands.

## Unattended runs

- Runtime is a work budget: spend it while a useful route remains, and never
  wait or make attempts, routes or PRs to fill it. If execution is wanted and
  none was given, ask before launch; there is no default. Checkpoint by pushing
  at least every 30 minutes, or the interval in `GOAL.md`.
- Do not ask mid-run. A fork gets probes and a recorded decision; an action only
  a person can take becomes a request (`RULES.md` section 4). Take no easy
  obstruction while a named hard obligation has had no sustained attempt. Stay
  at the role's row in `SETTINGS.md` and the target's model floor.
- A local stop is not a stop: an attempt at an exit, a `wrong` check, a failed
  or dirty PR, an unavailable source. Record it and take the next obligation.
- Stop the run only when the budget or cycle cap is spent; the target closed and
  nothing further was asked; the worktree, or tooling every viable route needs,
  is gone; a live lease holds the target and no separate part exists; every
  viable obligation is blocked, by a ranking refreshed in that checkpoint; or
  only churn remains. Before the last two, look for materially different frames,
  inventing none; a churn stop names the hardest unattempted obligation.
- Clean stop: smallest relevant checks; next action and reason in the part file;
  push; numeric lock released; `lab_ops.py worktree-remove`; report.

## Ends

An attempt has three exits: the obligation follows from statements already in
the target; a counterexample in the actual setting; a budget stop with a dated
log of routes tried. Whoever launched it ends it, never the session doing it. A
conditional result with a new named lemma is a checkpoint; extend a budget only
while premises close or new routes are tried. A plan ends after step 2; a run
ends, pushed, with a milestone PR, a check request or a budget stop.

## Never

- Lands on `main`, merges, or force-pushes a target branch.
- Adopts an axiom or primitive; an axiom change is named only as a price.
- Writes standing, audit data, ledger or queue files, or weaves results into the
  README, registries or publication tables; propose weaving as a request.
- Edits a file it does not hold, or takes a live lease or another's lock.

## Step references

Bare names: `docs/ai_methodology/skills/physics-loop/references/`. Read each
only at its step, at this revision; if one cannot be read, hold the step and
say so. All predate this file: a loop-pack file they name is now the part file,
and `RULES.md` wins any difference, status words too.

| Step | File on `main` | Why |
|---|---|---|
| 1 | `DISCOVERY.md` steps 2-4; `assumption-import-audit.md`; `literature-bridge-protocol.md`; `../../PRIMITIVE_REGISTRY_CHECK.md` | Search commands and outcomes; classing premises; search records |
| 2 | `proof-search-governance.md`; `route-patterns.md`; `.claude/commands/`: `frontier`, `hypothesis`, `first-principles` | Contract, families, strength test; churn; picking, framing and deriving a target |
| 3 | `long-running-execution.md`, Lab Operation; `../../exercise/SKILL.md`; `DISCOVERY.md`, Deep Work Rules | Units, leases, handover, disagreement; the wall exercise; fan-out when stuck |
| 3 | `.claude/commands/`: `design-experiment`, `sweep`, `analyze`, `investigate-physics` | Runner design, sweeps, reading output, anomalies |
| 6 | `DELIVERY.md`; `CLAIM_STATUS.md`; `../../../REVIEW_LOOP_PR_CONFORMANCE_SPEC.md` | Branching, forbidden outputs, PR fields validators require; conformance |
| Runs | `CAMPAIGN.md`; `long-running-execution.md` up to Stop Cleanly | Third-PR evaluator brief; continuation and stop detail |
