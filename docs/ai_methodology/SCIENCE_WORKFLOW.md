# Science workflow

The single operating map for research, review, audit and repair. It supplies
no physics premise and grants no scientific status. The goal is to build and
test a theory of everything; whether any candidate succeeds is an open
question. Optimize for resolved obligations and discriminating evidence, not
favorable verdicts, note counts or PR counts.

## 1. Read the task first

- Do what the user asked. A request to review prompts or procedures examines
  them; it does not launch a campaign, a PR drain or an audit.
- A skill is a maintained procedure, not proof that its rules are right and not
  permission to widen the task. Report real conflicts; do not invent approval
  gates.
- Read the entry point and only the references the chosen mode needs. Treat
  memory, old commands and earlier model conclusions as retrieval aids, never as
  proof. Use the configured model and the tools actually available.

## 2. Evidence rules (apply to everything)

1. **Keep claim types apart.** A proposed construction, an open proof
   obligation, a proved conditional implication, an empirical prediction and an
   independently checked result are different things. Label which one you have.
2. **Premises stay explicit.** Supplied dynamics, observable identifications,
   selectors and empirical values remain named premises until derived. A
   definition or formalization does not derive them.
3. **No new axioms without the owner.** New mathematics (definitions, lemmas,
   theorems, proofs from stated premises) is welcome and does not enlarge the
   physical axiom stack. Adopting a new framework axiom or physical primitive
   requires explicit owner approval.
4. **Never fabricate.** No invented logs, numbers or PASS lines. Do not tune a
   prefactor to a comparison target. An expected test constant must be justified
   independently of the code it tests.
5. **Predictions vs fits.** Separate predictions from calibration, fitted inputs
   and post hoc matches. Declare comparison criteria and uncertainty before
   looking at the result where possible; disclose prior exposure when not.
6. **Exact claims need exact statements.** Give domain, quantifiers, edge cases
   and a proof or exhaustive certificate. Numerical agreement does not prove a
   general theorem.
7. **Negative results are graded.** A failed search reports what was tried. An
   obstruction theorem rules out an explicitly quantified family by proof.
   Underdetermination needs witnesses or a proof under matching premises. No
   number of failed routes, and no failure to imagine a counterexample, proves
   impossibility. Resource exhaustion is operational, not physical, evidence.
8. **Independence means a different path.** An independent check uses a
   different derivation or implementation of the load-bearing step. Re-running
   the same calculation, or comparing outputs derived from the same expected
   constant, is not independent. During research, each new proof gets one
   independent check: another model reads it line by line and names the first
   failing step or confirms it. Hostile readings, panels and reviews of a
   review wait for the hardening pass (section 7). Adversarial checks challenge
   premises, domains, normalization and physical identification, not prose.
   Record disagreement instead of resolving it by majority.
9. **Literature first; build on published work.** Each route or proof step
   opens with one search, run far and wide, of the repo, open PRs and the
   literature for its statement and its method, recorded once in the target
   folder and reused: where it looked, the exact statements found, how close
   they are and whether the proof is accessible. Record a search that finds
   nothing too, so nobody repeats it. A lemma, repair or gate lane first reads
   the existing records, then runs a short targeted search, time-boxed to a
   small share of its budget; a search may run alongside a kill test. Use what
   is found and credit its authors by name; prefer filling a published open
   obligation over a new route. An independent derivation earns nothing;
   independent checking (rule 8) still applies, and using a result means
   verifying it (section 10). Novelty neither establishes nor discredits
   correctness.

## 3. Formal verification (Lean)

Lean is a targeted tool, not a blanket gate. Use it for a concrete risk: a
subtle domain restriction, a long dependency chain, hard edge cases, or a
critical lemma with heavy downstream reuse. Name the exact statement and risk.
Pending formalization must be visible downstream without blocking unrelated
research. Ordinary proofs still need mathematical checking.

When Lean evidence is used, record source revision, theorem and hypotheses,
toolchain and dependency versions, checker output and axioms used. Confirm the
formal statement matches the claim. `sorry`, admitted lemmas or a custom axiom
asserting the conclusion discharge nothing. A checked theorem proves its formal
statement, not its identification with physics. An applicable provider
Lean-verified theorem may be cited with its exact statement, assumptions and
provenance without a duplicate build; it does not cover companion results or
new repository bridges.

## 4. Current owner settings

| Setting | Current choice | Since |
|---|---|---|
| Cadence | Continuous discovery on a dedicated candidate branch, selective independent checks, PRs at coherent milestones | 2026-09-07 |
| PR type | Regular PRs; draft only when the user asks | 2026-09-07 |
| Formal audit | Runs only for a TOE candidate or a standalone proof the owner wants to publish, over that result's dependency closure. Routine research does not wait for audit; preservation guards apply where affected live judgments exist. Mechanical validation never invokes an auditor or grants status | 2026-10-30 |
| Landing review | One independent fast reviewer per coherent unit (owner's Codex choice: Astra low), escalating unresolved mathematical or premise questions to the strongest reviewer (Astra xhigh). The executable model contract lives in `skills/review-loop/SKILL.md` | 2026-09-08 |
| Original mathematics | Explicitly authorized within the user's task | 2026-10-08 |
| Published work | Searched once per route or step and on record; built on at once with credit, labelled `unchecked`. A step the source proves in detail is a cited input until the hardening pass; lanes go to steps it sketches, assumes or gets wrong (section 2 rule 9, sections 7 and 10) | 2026-11-04 |
| Checks during research | One line-by-line check of each new proof by another model; hostile readings, panels and reviews of a review only in the hardening pass, once the candidate is complete | 2026-11-04 |
| Lane output | Closed proofs or explicit counterexamples; lanes run to closure; route choices recorded with reasons (section 7) | 2026-11-02 |
| Questions for the owner | Axiom edits, public posts, spending and pace only; scientific forks get probes (section 10) | 2026-10-30 |

A later explicit owner choice overrides this table. Deferring audit never
permits known false claims, unlabelled assumptions or fabricated evidence to
land as established results.

## 5. Research cadence

- Keep a coherent candidate on its own branch and checkpoint useful blocks there.
  Landing and audit are not prerequisites for the next exploratory step.
- Before substantial downstream work depends on a provisional result, check it
  independently, especially a bridge that fixes an observable, dynamics,
  symmetry, normalization, or a widely reused theorem. Such a check supports a
  research decision; it does not confer retained status.
- Deliver a PR at a coherent milestone or explicit handoff. Group lemmas that
  form one argument; avoid branches or PRs too large to review reliably.
- A candidate TOE is a connected proposed derivation with named gaps. Calling it
  established requires complete dependency and empirical validation.
- Review and audit drains run only when explicitly requested.

## 6. Stages and authority

| Stage | Work product | Completion evidence | Authority boundary |
|---|---|---|---|
| Select | Exact target, current gap, alternative routes, decisive test | Current source and dependency snapshot; written literature search; route choice with reason | Planning does not establish a claim |
| Develop | Source note and reproducible evidence on a branch | Proof obligations, honest scope, independent checks of load-bearing steps | Author proposes; no audit verdict or direct landing |
| Author check | Corrected packet and reproduction instructions | Mechanical checks actually run; omissions named | Self-check is not independent review |
| Review | Findings and fixes on a frozen source revision | Independent reviewer confirms the final content; integration gates pass | Review decides readiness and lands only within the requested scope |
| Audit | Verdict on landed, restricted evidence | Fresh-context mathematical examination plus authenticated evidence | Only the independent audit path writes verdicts |
| Repair | Source fix or justified re-audit request | Exact defect addressed; affected row requeueable | Repair cannot prewrite its own verdict |
| Synthesize | Candidate assembly or account of established results | Candidate: provisional dependency graph and gaps; established: audited closure | A summary cannot promote its sources |

Pipeline PASS, runner PASS, reviewer PASS and audit verdict answer different
questions; none substitutes for another. Audit is free to disagree with review.

For authorized backlog integration, a coherent argument may be reviewed as one
frozen unit across cumulative or dependent PRs, preserving each constituent's
source/head provenance and claim disposition. Run focused source, runner and
premise checks per unit, then one full mechanical pipeline, strict lint, and changed-evidence validation on the exact integrated
current-main candidate. Reuse identical successful validation only with
matching input, tool and scope receipts. Grouping confers no blanket approval;
the detailed contract and landing guards live in `skills/review-loop/SKILL.md`.
Drafts stay excluded unless draft triage is explicitly authorized; a
still-draft PR never lands and marking ready is not PASS. Owner-reserved
content stays excluded until released.

Skills by job: `skills/physics-loop/` sustained discovery, `skills/exercise/`
bounded investigation, `skills/workhorse/` scoped worker handoff,
`skills/review-loop/` independent review and authorized landing,
`skills/audit-loop/` independent audit, `skills/science-fix-loop/` repair, and
`skills/no-go-discipline/` for any negative claim. Other skills are supporting
operations, not mandatory stages.

## 7. Selecting work

Record this contract in the existing goal or handoff file (not a new packet):

```text
Target and quantified domain:
Current main revision and source/claim identifiers:
Accepted premises and separately supplied conditions:
Literature search record; closest published or repo result and exact missing obligation:
New construction, proof mechanism, or discriminating test:
Success witness / counterexample / inconclusive outcome:
Downstream question this would resolve, or frontier-discovery value:
Route chosen, why, and the evidence that would reverse it:
```

Prioritize load-bearing gaps with plausible decisive tests. Graph fanout is a
prioritization signal, not a measure of importance. Do not churn small variants
because they package easily; a short standard proof that closes a real
obligation is valuable.

**Route decisions.** Our route and a published one are both candidates, step by
step; neither is the default, and we follow theirs only where it is better.
Record each choice with its reason, the evidence that would reverse it and the
date, and revisit it whenever a result touches it. Both stay live, hardest open
step first, only while the evidence is open; the lead allocates budget by
evidence and may pause a lagging route with its reopen condition. Retire a route
only when a gate shows its hardest step fails or the other route closes that
step. A search for a shorter or simpler route, or one that removes a dependence,
is progress, not review; rerun the route comparison at each milestone.

**Methods.** Lay out the complete skeleton of the argument first, one line per
statement with its inputs and its state, then attack the step it is most likely
to die on; routine steps wait. Before proving a step, find and quote where the
sources treat it: proved, sketched or assumed. A step a source proves in detail
is a cited input until the hardening pass; lanes go to steps the sources
sketch, assume or get wrong, and a note claims that a source "assumes" or "does
not show" something only with the quoted passages that build it. Test machinery on a
ladder of easier models of the same step: what works there is the first
candidate, and what fails there is a cheap kill. For a standard, low-risk step,
write one full draft, distil it to a minimal proof, then gate it. Freeze what
passes its gate; it reopens only on a `wrong` signal, or when an input it reads
changes or is shown wrong. Independent lanes run in parallel across providers
and machines, and the lead keeps every available worker on the critical path; a
queue is serial only where one result feeds the next. Gates run alongside
downstream work, which stays provisional until its gate passes.

**Only closures count.** A lane's output is a closed proof with every step
written, or an explicit counterexample to a statement. Lists of gaps, unchecked
inputs and scope caveats are not results; give them one short paragraph at
most. Kill first: when unsure a statement is true, try the counterexample
before the long proof. A lane that reduces its target to a smaller statement
attacks it in the same session and hands off only when the budget is spent,
saying how far it got. After two successive reductions with no closure, it
stops and returns to the lead for a route re-evaluation: repeated narrowing
signals a wrong route. Notes hold the proof, the counterexample
or the exact point where the argument fails, without restating the setting.
Report progress as closures: lemmas proved and gated, hypotheses discharged,
statements killed, observable maps validated, and the terminal obligations that
remain. Never report a percentage of TOE completion. A valid conditional
theorem proves an implication, not that the world satisfies its hypotheses.

**Hardening.** Once a candidate argument is complete, run one hardening pass on
its consolidated document: re-derive the published steps it cites, run the
adversarial readings of premises, domains, normalization and identifications,
and review the whole chain line by line. Until then these readings wait; they
are not a step of every lane.

Use the existing N1-N8 negative-claim packet contract honestly where required:
when a no-go claim is landed or made public. Inside a target, a failed attempt
is recorded as a failed search (section 2, rule 7), without a packet. Its
five-route minimum is a mechanical submission rule, not a completeness
theorem. Never invent route families to meet it; a packet that cannot meet the
schema stays pending. Schema changes need coordinated validator, fixture and
auditor-prompt updates.

## 8. Where material belongs

- `origin/main`: scientific source, premise registries, audit tooling and
  audit-derived status. Verify current source before relying on old
  descriptions.
- `ai/execution`: planning and dispatcher instructions only. Orphan branch;
  never merges into `main`; its scorecard is an as-of planning aid.
- Science branches: proposals, evidence, handoffs and the working state of a
  shared target. Draft PRs stay outside review and landing unless explicitly in
  scope.
- `docs/ai_methodology/skills/` and `.claude/commands/`: current procedures and
  command adapters.
- `docs/work_history/`, `archive/` and dated campaign packs: history and
  recovery evidence, not the live queue.

Keep changes reviewable: isolate work, stage intended paths only, preserve
unpushed work on failure, and regenerate derived files with their owning tools.
Never copy generated files from a moving `origin/main` into a stale branch.

## 9. Changing this process

Agent prompts, skill bodies, command adapters and embedded worker/auditor
prompts are one interface. For each rule change, name the defect, affected
callers, expected decisions and a realistic counterexample. When a rule is
mechanically enforced (see `docs/audit/scripts/check_review_loop_skill_contract.py`
and `generate_skill_axiom_baselines.py`), change code and prose together and
run the tests. Platform system instructions are outside this repository's
control; report conflicts with them rather than claiming to override them.

Each change also states how it will be measured and what result reverts it. At
the end of a campaign, write one short retrospective in the target folder: for
each process change in force, what was measured and whether it stays. Revert by
PR what did not help. A lesson for all physics work goes through a PR here; a
lesson for one target stays in its folder.

## 10. Working as a lab

Several leads and workers, on several model providers and machines, may work one
target. State lives on pushed branches, not in sessions, and no rule assumes a
vendor. A target shared by more than one session follows Lab Operation in
`skills/physics-loop/references/long-running-execution.md`. These rules apply to
all work:

- **Forks get probes.** Ask the owner only about axiom edits (section 2, rule 3),
  public posts, spending and pace. A scientific fork gets parallel probes, each
  with its decisive outcome stated first; act on the result and report it. A
  failed probe is a failed search (section 2, rule 7), never a no-go. An action
  only a person can take, such as obtaining a source, is a request that names
  what it blocks; other work continues.
- **Verify what you build on.** Reading published work is not accepting it.
  Build on a published or outside-project statement at once, labelled
  `unchecked`, and verify it, in order of load and risk: re-derive it as a
  library entry credited to its source, labelled like our own work, and pass
  it through a research gate from another provider where one is available. A
  step the source proves in detail is re-derived in the hardening pass
  (section 7); a step it only sketches or assumes is proved here when the
  chain reaches it. A citation, and the source's own labels such as "proved", carry no
  weight. A step counts as a critical-path closure, lands or goes public only
  once everything it reads is verified. Section 3 covers provider Lean-verified
  theorems.
- **Research gates grant nothing.** A research gate is the independent check of
  section 5, held at a fixed point in the Develop stage. It redoes the argument
  to find errors and reports the explicit failure or confirms the step; it does
  not catalogue inputs unless one is false or unavailable. Its signals (`advance`,
  `correct-no-advance`, `wrong`) and the obligation labels in a target folder
  steer research and nothing else. They are not a review PASS, an audit verdict
  or a status, and they stay out of ledger fields, PR titles, note status lines
  and audit packets. Landing still goes through review-loop, and audit stays
  independent of both.
- **Public claims and outside projects.** A public claim needs one clean
  document, a line-by-line independent review of its whole dependency chain, and
  the owner's approval of the exact text. It states the actual standing of what
  it claims. A post to an outside project whose work we use carries only an
  actual error confirmed by a gate here, or a gated proof that visibly helps it,
  with the same approval; gaps, missing references and notation stay in our
  notes. Credit by name everyone whose work helped, including other providers'
  sessions.
- **Launching jobs.** Before a long worker or any numeric job, run
  `python3 scripts/lab_ops.py preflight`, which checks disk, memory, load, model
  floor and what the sandbox allows. A required check that cannot run is reported
  at launch, and the job is rerouted or the omission recorded. A job is launched,
  not running, until its first events have been seen, including the model and
  effort it reports. Run one numeric job per machine, under
  `lab_ops.py numeric-lock`. Details are in `skills/workhorse/SKILL.md`.
- **Sparse worktrees.** Start from `lab_ops.py worktree-add`, which checks out the
  shared rules plus the paths you name. Use a whole checkout only for work that
  needs one, such as the audit pipeline or a landing. Remove a worktree as soon as
  its work is pushed; `lab_ops.py worktree-remove` refuses unpushed work.
