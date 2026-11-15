# Owner settings

The owner's current choices. They change more often than `RULES.md` and never
contradict it. A later explicit owner choice overrides this file; record it
here with its date. Each campaign's retrospective says which settings stay.

## Cadence and assurance

| Setting | Current choice | Since |
|---|---|---|
| Cadence | Continuous discovery on a dedicated candidate branch, selective independent checks, PRs at coherent milestones | 2026-09-07 |
| PR type | Regular PRs; draft only when the owner asks | 2026-09-07 |
| PR base | Every PR is based on `main`, and its author never rebases it or keeps it current with `main`: `land` integrates reviewed commits in batches and meets any conflict once. A conflict sent back is fixed with a new commit, never by rewriting pushed history. A PR that needs another unlanded PR says `Depends on #<n>` and lands with it as one unit, or its commits go into that PR; it is not based on that PR's branch. This overrides the stacking advice in `physics-loop/references/DELIVERY.md` and `long-running-execution.md` | 2026-11-11 |
| Landing review | One independent fast reviewer per coherent unit, at the depth that `skills/review-loop/scripts/review_depth.py` reads from the unit's delta: a scope read when the unit only adds working material, the full read for every other change (`procedures/land.md`, step 4). A unit of one PR landed as it is uses the scripted run, `skills/review-loop/scripts/land_run.py`; the agent loop is for units that need fixes, salvage or several PRs. The scripted run is on trial: its first runs are review only, their tokens and results are compared with the agent loop's, and it is dropped if it passes a unit that the agent loop holds for a finding the reviewer could have seen. A depth may be raised with a recorded reason and is never lowered. Escalate only an unresolved mathematical or premise question, a disagreement or a failed decisive control, with its evidence, to the strongest reviewer. Measure: the start and end time on each reviewer report, by depth. The scope read is suspended until the owner decides if a unit that it landed is found to claim more, in a title, summary or status line, than its statements say. It is removed if scope reads prove no faster than full reads of units of similar size | 2026-11-10; reviewer and escalation since 2026-09-08; scripted run 2026-11-14 |
| Original mathematics | Authorized within the task | 2026-10-08 |
| Audit trigger | Only for a TOE candidate or a standalone proof the owner wants to publish, over that result's dependency closure. Routine research does not wait for audit | 2026-10-30 |
| Audit tier | The forensic tier, over the closure at a pinned commit (`docs/audit/README.md`) | 2026-10-30 |
| Questions for the owner | Axiom edits, public posts, spending and pace only | 2026-10-30 |
| PR checks | Hosted CI status on a PR is never waited on or reported; the landing gate is the gate. A session still reports any check it ran itself that failed | 2026-07-02, restated 2026-11-10 |
| Published work | Searched once per route or step and put on record; built on at once with credit as `argued`. A step the source proves in detail is a cited input, still `argued`. Its re-derivation waits for the hardening pass, except where `RULES.md` section 3 places a check earlier: a bridge that fixes an observable, dynamics, symmetry or normalization, or a step at an interface between parts, is checked before heavy work rests on it. A step the source sketches or assumes is proved when the chain reaches it. Lanes go to steps the source sketches, assumes or gets wrong | 2026-11-04 |
| Checks during research | One line-by-line check of each new proof by another model, which names the first failing step or confirms it. Like every check it attacks premises, domains, normalization and physical identification, and the checks that `RULES.md` section 3 places stay where it places them: before other work builds heavily on a step, at every interface between parts, at assembly, and early when a result matches a target unexpectedly well. What waits for the hardening pass is what goes beyond those: panels, reviews of a review, and a repeat hostile reading of a step that already has its check | 2026-11-04 |
| Lane output | Closed proofs or explicit counterexamples; lanes run to closure; route choices recorded with reasons | 2026-11-02 |
| Proof verification | A written proof lands with a check that could show it wrong. Under `docs/` that check is the note's primary runner: exact or finite instances of the statement, and at least one control that fails when the statement is perturbed. A note that says it needs no runner does not land there. A Lean certificate under `formalization/` is added where `RULES.md` section 3 names the risk, and the note and its runner name it. A run or a certificate is evidence that a checker reads. Neither is the proof, and neither changes standing (`RULES.md` sections 1 and 2) | 2026-11-13 |
| Research sections | Mathematics on a supplied model, in which no framework axiom enters, lands under `research/<program>/` as working material, with no ledger rows and no audit status (owner decision of 2026-11-07, recorded in PR 10141). Each part says how it is verified: Lean, a compute check, or none yet. A part with none is listed as an open obligation in its section's README. A folder of byte-identical copies may carry a `.gitattributes` file that turns off one whitespace check for named files. `research/README.md` lists the sections | 2026-11-07; verification line 2026-11-13 |
| PR state | In force for every landing run with the loop `skills/review-loop/scripts/land_train.sh`, run as `skills/review-loop/references/LANDING.md` says, as changed on 2026-11-10: a landed PR shows as merged, and a PR closed without merging has nothing on `main`. A PR closed before that loop was in use may still have landed: read its landing record. Measure: the loop prints `MERGED` or `NOT_MERGED` for each carried PR. One `NOT_MERGED` line, or a dependent PR that GitHub closes when a landed head branch is deleted, suspends the setting until the owner decides | 2026-11-10 |
| Negative-claim packet | In force: the N1 to N8 packet is a checker's aid that no gate requires, and an obstruction is judged as a theorem about an explicit family, recorded as `procedures/audit.md` step 5 says. A supplied packet is validated as before and must agree with the verdict; the audit gate counts no routes or route classes; landing no longer checks the five N5 runner-output lines. Measure: every later check or audit of an obstruction audited without a packet says whether its `claim_scope` ruled out more than its argument. One that the packet's checks would have caught suspends this setting until the owner decides. Inside a target a failed attempt is recorded as a failed search, without a packet | 2026-11-13; decided 2026-11-10; scope 2026-11-04 |

## Method defaults (2026-11-02; skeleton, sources, passes and hardening 2026-11-04; prior digest 2026-11-06)

These are how the owner wants hard targets attacked. Only the owner changes
them.

- **Skeleton first, hardest step first.** Lay out the whole argument first,
  one line per statement with its inputs and its state, then attack the step
  it is most likely to die on. Routine steps wait. The skeleton is our own: an
  assembly overview of named parts, each with its main statement, imported
  hypotheses, dependencies and sources. Published work enters as a credited
  input. It is never a frame that we patch one gap at a time.
- **Prior work digest.** The repo search is enforced, not remembered. Before a
  lane starts, a cheap reading model writes `prior/<lane>.md` in the target
  folder: what the repo already proves on the target (`main`, every open
  science PR, other branches' libraries, the target folder), failed attempts
  and their failing step, overlaps, missed inputs and consumers, each with
  path, line and a short quote. A lane, referee included, is launched through
  `lab_ops.py preflight --lane <lane>`, which refuses it until the digest is
  committed as a regular file. So the digest is prepared and committed before
  every lane; what differs is when the lane opens it. A port, proof, repair,
  check or referee lane reads it first, ports what is proved instead of
  re-deriving it, and lists the prior results it used. A lane run for a fresh
  view, which is a direction document or a wall exercise, first opens only
  the target statement, the definitions and the statements of results it may
  cite. It writes its own approaches to disk, then opens the digest and the
  rest, calls nothing new before that, and records what the digest changed
  (the exercise skill gives its own order). A lane's checkout may not hold
  `main` or the open PRs, so the digest is its map to them. The
  search runs over a plain-file copy of those sources with `grep`, bounded by
  path, never over git history (`git grep` on whole refs, `git log -p`, `-S`
  searches): on 2026-11-06 the lead machine ran out of memory with git
  processes holding about 29 GB while such searches were running; the panic
  report did not name the command. A lane that ran without a digest gets one
  afterwards, and its overlaps are recorded before it freezes.
- **Sources first.** Before proving a step, find and quote where the sources
  treat it: proved, sketched or assumed. A step a source proves in detail is
  a cited input; the row "Published work" says when it is checked. Lanes go
  to steps the sources sketch, assume or get wrong, and a note says a source
  "assumes" or "does not show" something only with the quoted passages that
  build it.
- **Three passes.** Every part, hard or routine, goes through three passes.
  One long session, on the provider that drafts best, writes the full
  argument at length, with no brevity limit. A second session, on the other
  provider, distils it to a minimal proof and lists every definition it had
  to infer. A fresh session of the first provider, never the provider that
  wrote the distilled text, reads the whole distilled part line by line,
  once. Keep the status of each step, proved or outstanding, in the text of
  the part, not in a separate per-lane log.
- **Hardening.** Once a candidate argument is complete, run one hardening pass
  on its consolidated document: re-derive the published steps it cites that
  have no check yet, read premises, domains, normalization and
  identifications adversarially across the whole chain, and review the chain
  line by line. This pass adds to the checks that `RULES.md` section 3 places
  during research and replaces none of them. Panels, reviews of a review and
  repeat hostile readings are not a step of every lane; they wait for this
  pass.
- **Kill first.** When unsure a statement is true, try the counterexample
  before the long proof.
- **Ladder.** Test machinery on easier models of the same step. What works
  there is the first candidate; what fails there is a cheap kill.
- **Reductions.** A lane that reduces its target to a smaller statement attacks
  that in the same session. After two successive reductions with no closure it
  returns to the lead for a route re-evaluation.
- **Freeze.** A step that is `checked` reopens only on a `wrong` check or when
  something it reads changes.
- **Two routes.** Our route and a published one are both candidates, step by
  step; neither is the default. Both stay live, hardest open step first,
  while the evidence is open. The lead allocates budget by evidence and may
  pause a lagging route with its reopen condition. Retire one only when a
  check shows its hardest step fails or the other route closes that step. A
  search for a shorter or simpler route, or one that removes a dependence, is
  progress, not review; rerun the route comparison at each milestone.
- **Literature budget.** A route or proof step opens with one wide search. A
  lemma, repair or check lane reads the existing search records first, then
  runs a short targeted search, time-boxed to a small share of its budget.
  Prefer filling a published open obligation to opening a new route.
- **Parallel by default.** Independent lanes run in parallel across providers
  and machines, and the lead keeps every available worker on the critical
  path. A queue is serial only where one result feeds the next. Checks run
  alongside downstream work, which stays `argued` until its check passes.
- **Notes.** A note holds the proof, the counterexample or the exact point
  where the argument fails, without restating the setting. Gaps, unchecked
  inputs and scope caveats get one short paragraph at most.
- **Selection.** Prioritize load-bearing gaps with a plausible decisive test.
  Graph fanout is a signal, not importance. Do not churn small variants
  because they package easily.

## Models by role

The only place where the rules and procedures prescribe a model. A role
names a tier, never a model id. A tier is a position in a provider's range,
and the "Now" column is the model that held it on the date shown.

| Tier | Position it holds | Now | Resolved |
|---|---|---|---|
| Anthropic top | Anthropic's strongest reasoning model | `claude-fable-5-2` | 2026-11-12 |
| Anthropic second | The next Anthropic model down | `claude-opus-5-5` | 2026-11-12 |
| OpenAI top | OpenAI's frontier reasoning model in Codex | `gpt-6-astra` | 2026-11-12 |
| OpenAI workhorse | OpenAI's current workhorse model in Codex | `gpt-6.1-sol` | 2026-11-12 |
| OpenAI cheap | OpenAI's fast, low-cost model in Codex | `gpt-6-luna` | 2026-11-12 |

Keeping the tiers current is a lead's job, done without asking the owner
(owner, 2026-11-12):

- A newer version of the same family takes the tier on the day a lead sees it
  available on the machines that run the role. The lead changes the row and
  its date in a PR. A successor in a reading tier first passes a reading test
  with a known answer (owner, 2026-11-05).
- A model of another family takes a tier only when its provider presents it
  as that position. The PR quotes the provider.
- A row stays on the older model only with recorded evidence that the newer
  one does that role worse.
- `python3 scripts/lab_ops.py models` reads the tier table. It reports a tier
  for which a model list on the machine has a newer version of the same
  family, and a tier resolved more than 30 days ago. It reads the Codex model
  list, and `--known <ids>` adds the ids a session's own environment lists.
  `doctor` prints the same findings at the start of a session.
- An effort level is the provider's word. A new level above one named below
  is a spending choice and stays with the owner.

A target sets its own floor with `model_floor <role>: <model>@<effort>` lines
in its `GOAL.md`, and `lab_ops.py preflight` refuses a launch below that
floor. The role table is the default a lead copies into a new target, with
each tier written as its current model. Proof-critical checks use the
strongest suitable reasoning available. If a named model is not available,
say so and record what was used; never substitute silently.

| Role | Tier and effort | Since |
|---|---|---|
| Direction: approach, skeleton, restatement, route choice | Anthropic top, high. A program's direction document is authored at max. Its author starts from the goal and the primary object and writes its own approaches before it opens any plan, route list or digest (method default "Prior work digest"). It attacks the crux statement, not the entry lemma. The strongest model never reviews a weaker model's direction work | 2026-11-09; direction document 2026-11-10 |
| Hard proofs | Anthropic top, medium, once a direction names the statement, domain, route and stop conditions | 2026-11-09 |
| Ports and routine steps | Anthropic second, effort by the step; never at max to write a hard proof | 2026-11-09 |
| Distilling a part, the second of the three passes | OpenAI top, effort by the step | 2026-11-04; tier set by a lead 2026-11-12 |
| Checker | Never the model that wrote the text under check, and from another provider where one is available. In the three passes that is Anthropic second reading a part that OpenAI top distilled. A step that Anthropic second wrote goes to OpenAI top at max, while Codex has capacity. A checker from the author's provider works in a separate context from restricted inputs and is labelled so (`RULES.md` section 3) | 2026-11-09 |
| Decision lanes and proof-tree sketches | OpenAI top, max. Max on that tier is for physics only | 2026-10-30; 2026-11-08; 2026-11-09 |
| Bulk reading, source search and digests | OpenAI workhorse for comprehension reads; OpenAI cheap for mechanical extraction, and for bulk reading when Codex usage runs low. Spot-check each list against one known answer. Neither writes a proof or a verdict | 2026-11-05; 2026-11-09 |
| Consolidation, editorial and coordination work | Any tier, no higher than high | 2026-10-30 |
| Lead, worker and any role not listed | The model running the session. A lead may raise one block's worker or checker to the strongest available model and records it | |
| Landing reviewer, fast | OpenAI top, low (the owner's Codex choice), from a different model family than the author when one is available | 2026-09-08 |
| Landing reviewer, escalation | OpenAI top, xhigh | 2026-09-08 |
| Auditor | The seat `codex_audit_runner.py` is configured to launch; the runner records what it used | |

Two scripts still pass a model and effort of their own, which overrides the
configured one: `science_fix_loop.py` and `classify_missing_derivations.py`.
Change the value there until they read this table.

Each machine runs Codex on its own account with its own weekly limit.
`lab_ops.py preflight` reports the use of the account on the machine it runs
on, and refuses a Codex lane when that account is spent (2026-11-13).

## Budgets

| Budget | Value | Note |
|---|---|---|
| `AGENTS.md` | 30 lines | Entry file |
| `RULES.md` | 200 lines | Always read |
| A procedure's core | 150 lines | Mechanics live in scripts and step references |
| Numeric jobs | One per machine, under `lab_ops.py numeric-lock` | |
| Checkpoint interval, unattended | 30 minutes unless `GOAL.md` sets another | Push at each |
| PRs per campaign | No count cap; each PR passes the pre-PR questions | Owner, 2026-06-11 |
