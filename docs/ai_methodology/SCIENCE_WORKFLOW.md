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
   constant, is not independent. Adversarial checks challenge premises, domains,
   normalization and physical identification, not prose. Record disagreement
   instead of resolving it by majority.
9. **Check novelty, then judge on merit.** Search existing repo work and the
   literature to locate the real gap and avoid duplicating known results.
   Novelty neither establishes nor discredits correctness; prior publication is
   not a prerequisite.

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
| Formal audit | Runs only for a TOE candidate or a standalone proof the owner wants to publish, over that result's dependency closure. Routine research neither waits for it nor spends effort preserving audit state. Mechanical validation never invokes an auditor or grants status | 2026-10-30 |
| Landing review | One independent fast reviewer per coherent unit (owner's Codex choice: Astra low), escalating unresolved mathematical or premise questions to the strongest reviewer (Astra xhigh). The executable model contract lives in `skills/review-loop/SKILL.md` | 2026-09-08 |
| Original mathematics | Explicitly authorized within the user's task | 2026-10-08 |
| Literature lemmas | Rebuilt with credit; a citation is attribution only (section 10) | 2026-10-29 |
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
| Select | Exact target, current gap, alternative routes, decisive test | Current source and dependency snapshot; novelty search | Planning does not establish a claim |
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
Closest existing result and exact missing obligation:
New construction, proof mechanism, or discriminating test:
Success witness / counterexample / inconclusive outcome:
Downstream question this would resolve, or frontier-discovery value:
Next decision and condition for reopening an exhausted route:
```

Prioritize load-bearing gaps with plausible decisive tests, and keep materially
different routes open. Graph fanout is a prioritization signal, not a measure
of importance. Do not churn small variants because they package easily; a short
standard proof that closes a real obligation is valuable.

Report progress as concrete changes: a proved lemma, discharged hypothesis, new
falsifier, eliminated counterexample class, validated observable map, or
remaining terminal obligation. Never report a percentage of TOE completion. A
valid conditional theorem proves an implication, not that the world satisfies
its hypotheses.

Use the existing N1-N8 negative-claim packet contract honestly where required.
Its five-route minimum is a mechanical submission rule, not a completeness
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
- **Literature lemmas are rebuilt.** A step that needs a literature lemma rebuilds
  it as a library entry with credit to its authors. A citation is attribution and
  carries no weight in the argument; until the rebuild exists the step is an open
  obligation. Section 3 covers provider Lean-verified theorems.
- **Research gates grant nothing.** A research gate is the independent check of
  section 5, held at a fixed point in the Develop stage. Its signals (`advance`,
  `correct-no-advance`, `wrong`) and the obligation labels in a target folder
  steer research and nothing else. They are not a review PASS, an audit verdict
  or a status, and they stay out of ledger fields, PR titles, note status lines
  and audit packets. Landing still goes through review-loop, and audit stays
  independent of both.
- **Public claims.** A public claim needs one clean document, a line-by-line
  independent review of its whole dependency chain, and the owner's approval of
  the exact text. It states the actual standing of what it claims.
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
