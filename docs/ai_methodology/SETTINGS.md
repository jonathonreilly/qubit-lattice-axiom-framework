# Owner settings

The owner's current choices. They change more often than `RULES.md` and never
contradict it. A later explicit owner choice overrides this file; record it
here with its date. Each campaign's retrospective says which settings stay.

## Cadence and assurance

| Setting | Current choice | Since |
|---|---|---|
| Cadence | Continuous discovery on a dedicated candidate branch, selective independent checks, PRs at coherent milestones | 2026-09-07 |
| PR type | Regular PRs; draft only when the owner asks | 2026-09-07 |
| Landing review | One independent fast reviewer per coherent unit, at the depth that `skills/review-loop/scripts/review_depth.py` reads from the unit's delta: a scope read when the unit only adds working material, the full read for every other change (`procedures/land.md`, step 4). A depth may be raised with a recorded reason and is never lowered. Escalate only an unresolved mathematical or premise question, a disagreement or a failed decisive control, with its evidence, to the strongest reviewer. Measure: the start and end time on each reviewer report, by depth. The scope read is suspended until the owner decides if a unit that it landed is found to claim more, in a title, summary or status line, than its statements say. It is removed if scope reads prove no faster than full reads of units of similar size | 2026-11-10; reviewer and escalation since 2026-09-08 |
| Original mathematics | Authorized within the task | 2026-10-08 |
| Audit trigger | Only for a TOE candidate or a standalone proof the owner wants to publish, over that result's dependency closure. Routine research does not wait for audit | 2026-10-30 |
| Audit tier | The forensic tier, over the closure at a pinned commit (`docs/audit/README.md`) | 2026-10-30 |
| Questions for the owner | Axiom edits, public posts, spending and pace only | 2026-10-30 |
| PR checks | Hosted CI status on a PR is never waited on or reported; the landing gate is the gate. A session still reports any check it ran itself that failed | 2026-07-02, restated 2026-11-10 |
| Published work | Searched once per route or step and put on record; built on at once with credit as `argued`. A step the source proves in detail is a cited input, still `argued`, until the hardening pass re-derives it; a step it sketches or assumes is proved when the chain reaches it. Lanes go to steps the source sketches, assumes or gets wrong | 2026-11-04 |
| Checks during research | One line-by-line check of each new proof by another model, which names the first failing step or confirms it. Hostile readings, panels and reviews of a review run only in the hardening pass, once the candidate is complete | 2026-11-04 |
| Lane output | Closed proofs or explicit counterexamples; lanes run to closure; route choices recorded with reasons | 2026-11-02 |
| PR state | In force for every landing run with the loop `skills/review-loop/scripts/land_train.sh`, run as `skills/review-loop/references/LANDING.md` says, as changed on 2026-11-10: a landed PR shows as merged, and a PR closed without merging has nothing on `main`. A PR closed before that loop was in use may still have landed: read its landing record. Measure: the loop prints `MERGED` or `NOT_MERGED` for each carried PR. One `NOT_MERGED` line, or a dependent PR that GitHub closes when a landed head branch is deleted, suspends the setting until the owner decides | 2026-11-10 |
| Negative-claim packet | Decided: the N1 to N8 packet becomes a checker's aid and an obstruction is judged as a theorem about an explicit family. In force: the audit gate counts no routes or route classes; a passing N1 needs every listed route closed (gate) and the family stated with explicit quantifiers (auditor). Not yet in force: the audit gate still requires the packet, and landing still checks the N5 lines. The packet applies when a no-go claim is landed or made public; inside a target a failed attempt is recorded as a failed search, without a packet | 2026-11-10; scope 2026-11-04 |

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
  committed. The lane reads the digest first, ports what is proved instead of
  re-deriving it, and lists the prior results it used. Its own checkout may
  not hold `main` or the open PRs, so the digest is its map to them. The
  search runs over a plain-file copy of those sources with `grep`, bounded by
  path, never over git history (`git grep` on whole refs, `git log -p`, `-S`
  searches): on 2026-11-06 the lead machine ran out of memory with git
  processes holding about 29 GB while such searches were running; the panic
  report did not name the command. A lane that ran without a digest gets one
  afterwards, and its overlaps are recorded before it freezes.
- **Sources first.** Before proving a step, find and quote where the sources
  treat it: proved, sketched or assumed. A step a source proves in detail is
  a cited input until the hardening pass. Lanes go to steps the sources
  sketch, assume or get wrong, and a note says a source "assumes" or "does
  not show" something only with the quoted passages that build it.
- **Three passes.** Every part, hard or routine, goes through three passes.
  One long session, on the provider that drafts best, writes the full
  argument at length, with no brevity limit. A second session, on the other
  provider, distils it to a minimal proof and lists every definition it had
  to infer. A fresh session of the first provider, never the provider that
  wrote the distilled text, reads the whole distilled part line by line,
  once. Keep the status of each step, proved or outstanding, in the text of
  the part, not in a separate per-lane log.
- **Hardening.** Once a candidate argument is complete, run one hardening pass
  on its consolidated document: re-derive the published steps it cites, run
  the adversarial readings of premises, domains, normalization and
  identifications, and review the whole chain line by line. Until then these
  readings wait; they are not a step of every lane.
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

The only place where the rules and procedures prescribe a model. A target
sets its own floor with `model_floor <role>: <model>@<effort>` lines in its
`GOAL.md`, and `lab_ops.py preflight` refuses a launch below that floor. This
table is the default a lead copies into a new target. Proof-critical checks
use the strongest suitable reasoning available. If a named model is not
available, say so and record what was used; never substitute silently.

| Role | Model and effort | Since |
|---|---|---|
| Direction: approach, skeleton, restatement, route choice | `claude-fable-5-2`, high. A program's direction document is authored at max from the goal and the primary object alone, before its author reads any plan, route list or literature digest, and it attacks the crux statement, not the entry lemma. The strongest model never reviews a weaker model's direction work | 2026-11-09; direction document 2026-11-10 |
| Hard proofs | `claude-fable-5-2`, medium, once a direction names the statement, domain, route and stop conditions | 2026-11-09 |
| Ports and routine steps | `claude-opus-5-5`, effort by the step; never at max to write a hard proof | 2026-11-09 |
| Checker | A model that did not write the proof: `claude-opus-5-5` for a hard proof, `gpt-6-astra` at max for a step that Opus wrote, while Codex has capacity. A checker from the author's provider works in a separate context from restricted inputs and is labelled so (`RULES.md` section 3) | 2026-11-09 |
| Decision lanes and proof-tree sketches | `gpt-6-astra`, max, which is for physics only | 2026-10-30; 2026-11-08; 2026-11-09 |
| Bulk reading, source search and digests | `gpt-6.1-sol` for comprehension reads; `gpt-6-luna` for mechanical extraction, and for bulk reading when Codex usage runs low; not `gpt-6-sol`. Spot-check each list against one known answer. Neither writes a proof or a verdict | 2026-11-05; 2026-11-09 |
| Consolidation, editorial and coordination work | No higher than high | 2026-10-30 |
| Lead, worker and any role not listed | The model running the session. A lead may raise one block's worker or checker to the strongest available model and records it | |
| Landing reviewer, fast | Astra, low (the owner's Codex choice), from a different model family than the author when one is available | 2026-09-08 |
| Landing reviewer, escalation | Astra, xhigh | 2026-09-08 |
| Auditor | The seat `codex_audit_runner.py` is configured to launch; the runner records what it used | |

Two scripts still pass a model and effort of their own, which overrides the
configured one: `science_fix_loop.py` and `classify_missing_derivations.py`.
Change the value there until they read this table.

## Budgets

| Budget | Value | Note |
|---|---|---|
| `AGENTS.md` | 30 lines | Entry file |
| `RULES.md` | 200 lines | Always read |
| A procedure's core | 150 lines | Mechanics live in scripts and step references |
| Numeric jobs | One per machine, under `lab_ops.py numeric-lock` | |
| Checkpoint interval, unattended | 30 minutes unless `GOAL.md` sets another | Push at each |
| PRs per campaign | No count cap; each PR passes the pre-PR questions | Owner, 2026-06-11 |
