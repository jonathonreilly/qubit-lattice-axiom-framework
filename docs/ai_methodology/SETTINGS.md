# Owner settings

The owner's current choices. They change more often than `RULES.md` and never
contradict it. A later explicit owner choice overrides this file; record it
here with its date. Each campaign's retrospective says which settings stay.

## Cadence and assurance

| Setting | Current choice | Since |
|---|---|---|
| Cadence | Continuous discovery on a dedicated candidate branch, selective independent checks, PRs at coherent milestones | 2026-09-07 |
| PR type | Regular PRs; draft only when the owner asks | 2026-09-07 |
| Landing review | One independent fast reviewer per coherent unit; unresolved mathematical or premise questions escalate to the strongest reviewer | 2026-09-08 |
| Original mathematics | Authorized within the task | 2026-10-08 |
| Audit trigger | Only for a TOE candidate or a standalone proof the owner wants to publish, over that result's dependency closure. Routine research does not wait for audit | 2026-10-30 |
| Audit tier | The forensic tier, over the closure at a pinned commit (`docs/audit/README.md`) | 2026-10-30 |
| Questions for the owner | Axiom edits, public posts, spending and pace only | 2026-10-30 |
| Published work | Searched once per route or step and put on record; built on at once with credit as `argued`; verified in parallel | 2026-11-02 |
| Lane output | Closed proofs or explicit counterexamples; lanes run to closure; route choices recorded with reasons | 2026-11-02 |
| PR state | Decided: a landed PR shows as merged and a closed PR means nothing from it is on `main`. Not yet in force: `land` still pushes the reviewed commits and closes the PR, and its contract check requires that. Until both change, read a PR's landing record | 2026-11-10 |
| Negative-claim packet | Decided: the N1 to N8 packet becomes a checker's aid and an obstruction is judged as a theorem about an explicit family. In force: the audit gate counts no routes or route classes; a passing N1 needs every listed route closed (gate) and the family stated with explicit quantifiers (auditor). Not yet in force: the audit gate still requires the packet, and landing still checks the N5 lines | 2026-11-10 |

## Method defaults (2026-11-02)

These are how the owner currently wants hard targets attacked. A target may
depart from one by recording why in its `GOAL.md`.

- **Skeleton first, hardest step first.** Lay out the whole argument, then
  attack the step it is most likely to die on. Routine steps wait. For a
  standard, low-risk step write one full draft, distil it to a minimal proof,
  then have it checked.
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
  check shows its hardest step fails or the other route closes that step.
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
| Lead: selection, design, line review, delivery | The model running the session | |
| Worker | The worker model the owner configured, by default the session's, at maximum available reasoning effort unless the owner chose another. A lead may raise one block's worker or checker to the strongest available model and records it | |
| Checker | A different model family from the author where one is available. A same-family checker works in a separate context from restricted inputs and is labelled so (`RULES.md` section 3) | |
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
