---
name: workhorse
description: "Use when a repo science command needs the owner-approved execution split: the supervising agent plans/specifies/reviews/lands, while a high-reasoning text worker executes bounded drafting, computation, extraction, or read-only panel lenses."
---

# Workhorse

## Skill Freshness

Before using this workflow, inspect its applicability and correctness and use
`docs/ai_methodology/skills/SKILL_FRESHNESS_CHECK.md` to select one consistent
source revision, including references. Ordinary operation uses current main;
a user-requested prompt review/test uses the identified candidate under review
without automatically executing the workflow or replacing it with old main text.

This skill defines the execution mechanism for repo science commands. It is a
coordination protocol, not a physics authority and not an audit lane.

## Execution Split

The supervising agent is the model running the current chat session, whichever
supported host or model family is in use. It owns target selection, synthesis,
review, and authorized delivery; the selected worker profile does not change
that responsibility.

Two worker profiles are available; use the one the user has configured and
the host actually provides.
Operational support — support-only evidence, NOT on `origin/main`: the
2026-08 campaign work-log (`STATE.yaml` and `REVIEW_HISTORY.md` under
`.claude/science/physics-loops/toe-time-expansion-20260802/` on the pack
branch `physics-loop/toe-close-pack-20260729`) records that window's Claude
workers block by block, including a checker refuting a supervisor-authored
primary, a worker catching a verdict-flipping rubric defect in its own
primary, and 3/3 pre-registered checker predictions on never-evaluated
windows. The profiles:

- **Host subagent worker** — a subagent of the host session (the host's
  agent or subagent tool), running the user's configured worker model (by
  default the session's configured model) at maximum available reasoning
  effort unless the user explicitly chose another effort. Pass the effort
  explicitly when the host allows it; where subagents inherit the session's
  effort, the session must be at that effort. Launched as background workers
  for bounded subtasks, each in its own durable worktree. The external-CLI
  start-hang/stdin failure modes below have not been observed with host
  subagents (no CLI stdin is involved at launch), but context exhaustion from oversized reads or tool output remains
  possible for any bounded-context worker: the bounded-read and
  incremental-delivery discipline applies to this profile too.
- **External CLI worker** — a separately launched text-reasoning CLI,
  preferably from another model family, when one is installed and configured
  locally (for example `codex exec`), at its maximum available reasoning
  effort. Verify the configured model and effort live against the local
  install and record them. Launch and reliability rules below.

Worker model choice: use the worker model and effort the user configured.
When the user has configured a worker tier below the supervising model, that
split concentrates the strongest model where its capability is load-bearing —
spec judgment, line-by-line review, and landing — and preserves the shared
capacity pool across a long window (parallel strongest-model workers would
burn the window's budget on the lane where discipline, not raw capability,
carries robustness). Per the campaign work-log cited above: the defects that
were caught in that window were caught by the verification structure,
including supervisor spec errors caught BY workers; that record says nothing
about defects that went undetected, and no completeness claim is made. The
supervising agent MAY escalate an individual block's worker or checker to the
strongest available model when that block's difficulty warrants it;
escalation is a profile fact and is disclosed in the ship note like any other.

Profile selection is the supervising agent's discretion, with one preference:
when both lanes are available, prefer primary and checker from different model
families to reduce one source of correlated error. Model-family difference
does not establish independence by itself: shared prompts, expected answers,
source code, and mathematical assumptions can still reproduce the same defect.
When only one family is available (quota, outage), the same-family setup is
admissible ONLY under the robustness conditions below, and every shipped
block must say plainly in the note, receipt, and PR whether its checker was
built by a different model family or in a separate context of the same
family (and say so if context separation cannot be established). A same-family
checker must use a distinct restricted-input context and independent checks;
label it same-family/fresh-context, never cross-family. If context separation
cannot be established, it cannot satisfy an independent confirmation gate. This
describes the checker pairing only; it is not an audit-independence grade —
audit rows use the controlled `independence` vocabulary in
`docs/repo/CONTROLLED_VOCABULARY.md`.

The `/workhorse` command is an adapter to this skill. Older science-command
boilerplate that pins a named model, vendor or tool for workers (for example a
Codex-first worker via `codex exec`) or prescribes a different execution
split defers to these profile and responsibility rules.

Never substitute an image, visual-generation, document-rendering, or
low-reasoning model for either profile. Disclose any substitution in the work
log and keep the supervising agent responsible for the result.

## Robustness Conditions (mandatory; load-bearing when primary and checker share a model family)

- Every substantive computational science block ships an independent checker
  spec'd to REFUTE, built on
  machinery disjoint from the primary's (different arithmetic route,
  different enumeration/allocation, no import of the primary — text/AST pins
  behind an import firewall).
- Checker teeth must be demonstrated, not asserted: mutation probes or
  planted defects that the checker provably catches, and tamper tests that
  fail closed.
- The supervising agent reviews every worker diff line-by-line and
  hand-verifies the load-bearing mathematics of at least the central claim
  before accepting a block; cache terminals are verified against emitted
  certificates.
- Integrity gates never encode desired outcomes; findings are generated from
  computed values.
- These conditions are what make same-family worker/checker pairs admissible;
  they are good practice for cross-model pairs too.

For a pure proof or mechanical edit, use an appropriate independent proof
check or change validation instead of inventing a second numerical runner.
Record exactly what was checked and any limits on independence. A checker
should test the contested scientific step; matching prose or file hashes
alone establishes provenance, not that step's correctness.

## Neutral Execution Contract

The supervisor specifies the exact question, allowed premises, known evidence,
permitted files, resource limit, and a discriminating acceptance test. A proof
sketch may be supplied as a candidate, with its unproved steps labeled. Workers
must be allowed to refute the sketch, expose a spec error, or return a precise
remaining obligation. They must never be required to manufacture the result
the supervisor expects.

Separate software integrity from hypothesis outcome. Correct execution with
an honest counterexample or residual can satisfy the work assignment while
refuting the proposed physics. Do not prescribe a minimum PASS count or the
desired measured value as the worker's acceptance contract. Keep comparison
targets out of the computation that predicts them; disclose unavoidable prior
knowledge and reserve independent or held-out checks when applicable.

The supervising agent:

- reads current repo context and the relevant command/skill instructions;
- writes the task spec, allowed files, evidence bar, and stopping conditions;
- keeps claim-status, foundation/conditional, no-go, and audit boundaries
  current;
- reviews every worker diff line-by-line before accepting it;
- runs the appropriate repo checks;
- lands or rejects the work only through the lane that owns that decision.

The worker may:

- draft notes, runners, tables, or narrow repairs from the supervisor's spec;
- run scratch computations and structured extraction;
- execute panel lenses with read-only filesystem settings;
- report uncertainties, missing premises, and proposed demotions.

The worker must not:

- synthesize final verdicts that the supervising agent merely rubber-stamps;
- apply audit verdicts, effective-status changes, or retained promotions;
- add axioms, primitives, or any unregistered supplied-premise class;
- decide to land, merge, or close PRs;
- route science work through visual/image-generation tooling.

## Launch Checks

Before launching a long worker or any numeric job, run
`python3 scripts/lab_ops.py preflight` (`docs/ai_methodology/SCIENCE_WORKFLOW.md`
section 10). It refuses on low disk or memory, on a model outside the target's
floor and, for numeric jobs, on high load, a held numeric lock or a sandbox that
blocks `nice`. It reports what the sandbox allows, including memory limits, network
and push. A job with its own sandbox runs it again as its first command. Limits for
a particular machine are flags or environment variables, not rules here.

Report a job as launched until its first events have been seen, including the model
and effort it reports; only then report it as running. After that, silence alone is
not a hang (see Monitor + salvage below).

Before starting a numeric job, acquire
`python3 scripts/lab_ops.py numeric-lock acquire --holder <session/job> --ttl-hours <hours>`
and pin math-library threads to one. This is a cooperative expiring lease, not a
process mutex. Use a unique holder per job; the same holder can reacquire its own
lease. The default lease lasts two hours. The launcher must refresh with
`python3 scripts/lab_ops.py numeric-lock refresh --holder <session/job> --ttl-hours <hours>`
before expiry throughout the run. Choose a lease longer than the monitoring
interval; if renewal cannot be confirmed, pause or stop the job before expiry.
Release with `python3 scripts/lab_ops.py numeric-lock release --holder <session/job>` only after
the job has stopped. An expired lease does not stop a running process.

A sustained attempt (Lab Operation in
`docs/ai_methodology/skills/physics-loop/references/long-running-execution.md`) is
one session resumed in a loop with the tool's own resume command, for example
`codex exec resume <session> "<prompt>"`. Whoever launched it ends it, never the
session doing it. Resume with a neutral prompt, such as:

> Name the hardest remaining obligation. Try a route you have not tried. Log what
> failed and why. Label every step honestly. An honest gap is a valid state.

The neutral execution contract still holds at every resume: the session may refute
the target or report what is missing, and it is never told what result to produce.

## Host Subagent Launch (when using the host subagent profile)

- Spawn one background subagent per independent bounded subtask, each pointed
  at its own durable
  worktree (never a tmp path — reboots purge tmp; the 2026-08-02 campaign
  interruption is the precedent), with the block spec inline in the prompt.
- The spec carries the same bounds as an external CLI worker spec: named read caps, exact
  deliverable filenames, incremental file writes, no docs/ edits
  except deliverable paths the spec names exactly (a note draft assigned
  under the worker contract is such a deliverable), no pushes (the
  supervisor pushes after review), raw final report with a line cap.
- Analysis workers do not commit. The supervisor owns commits and pushes after
  review unless the task explicitly authorizes a different non-analysis worker
  contract. Preserve work incrementally in the durable worktree; a certified
  run must identify the exact source it executed, even before a commit exists.

## External CLI Worker Launch & Reliability (REQUIRED when using that profile)

On the local `codex exec` setup, CLI workers hang or silently fail to deliver
in two confirmed ways. Both have a fix; apply all of the following every time.
For another CLI, apply the same rules with that tool's equivalent options
(closed stdin, prompt from a spec file, captured log and final message) and
record the exact command, model and effort. If no external CLI worker is
available, use the host subagent profile and record that provenance.

**Launch recipe (`codex exec` example) — close stdin and capture output:**

```bash
codex exec -s workspace-write -C "<repo-abs-path>" \
  -o /tmp/<task>_lastmsg.txt "$(cat /tmp/<task>_spec.md)" \
  < /dev/null > /tmp/<task>_full.log 2>&1 &
```

- `< /dev/null` is MANDATORY. With the prompt passed as an argument, `codex exec`
  still reads stdin to append it as a `<stdin>` block; a backgrounded job's stdin
  never reaches EOF, so the worker can block forever on
  `"Reading additional input from stdin..."` at 0% CPU with zero output. Closing
  stdin gives immediate EOF and prevents the start-hang.
- Pass the prompt as the argument (`"$(cat spec)"`); write the spec to a file first.

**Bound the reads — this is the #1 cause of "ran but never delivered":**

- Name the EXACT files the worker may read (≤ ~5). A worker told to "read the
  closure note + the ledger" dumps the multi-thousand-row `audit_ledger.json` into
  its context, exhausts it, and ends mid-reasoning having written nothing.
- NEVER instruct it to "read the ledger / read everything." For audit status, grep
  specific rows only: `git show "origin/main:docs/audit/data/ledger/<first-2-chars>/<claim_id>.json"` (the ledger is sharded per claim; the monolithic audit_ledger.json is an untracked local cache materialized by the pipeline).
- Tell it to WRITE THE DELIVERABLE INCREMENTALLY (write the output file as it goes,
  not held for a single final message) and to produce ONE focused deliverable plus
  a short stdout summary. Keep the task small and specific.

**Monitor + salvage (supervisor owns the result):**

- Track the task handle/PID returned by your own launch and its bounded deadline.
  Local 0% CPU, a quiet log, and an empty final-output file do not establish a
  hang: reasoning may happen remotely and final output may be buffered.
- On an explicit tool failure or expired task deadline, inspect the owned
  worker's status, checkpoint any existing artifacts, then interrupt that worker
  if needed. Revalidate recovered files before using them. Do not kill other
  sessions' processes or treat an incomplete transcript as a completed proof.
  The supervising agent remains responsible for completing or honestly routing
  the task.
- A tight, bounded spec (named files, incremental writes, one deliverable) is what
  makes the worker succeed; an open-ended "go read and figure it out" is what makes
  it hang or over-read.

## No-Go And Narrowing Discipline

When a task touches a no-go, obstruction, impossibility, or negative boundary,
read the actual primary note and its audited `claim_scope`. Plan against that
scope, not the title, reputation, or a secondary summary. If the prose is
broader than the audited support, queue or make a narrowing repair instead of
working around the mismatch silently.

## Lane Hand-Off

Science workers prepare source artifacts and author checks. A physics-loop
supervisor may compose related provisional blocks on one coherent campaign
branch, recording inherited hypotheses and gaps. Obtain a focused independent
check before extensive downstream reuse of a critical provisional result.
Default to milestone PRs; the user may request `--delivery block`. Formal audit
of each intermediate lemma is not a prerequisite for exploration.
The supervisor may prepare a PR, runner cache, or audit targeting metadata and
hands it to a fresh review-loop for independent review. Author checks never
substitute for that review. The supervisor runs review/landing or audit
orchestration only when the user's task authorizes that lane, including an
explicit repair-and-re-audit campaign; it need not ask again for an already
authorized step. Independent audit seats and verdict application remain owned
by audit-loop and cannot be performed by the science author as self-audit.
