# Procedures

Seven procedures cover the work. Pick one and read its file under
`procedures/`; it names anything else it needs and when. Each is a contract:
when it applies, what it takes, its steps, when it ends and what it may not
do. `RULES.md` governs all of them, and none grants standing except through
the records it names.

| Job | Read | Ends with |
|---|---|---|
| Attack a target | `procedures/research.md` | A milestone PR, a check request, or a budget stop |
| Hand a frozen piece to a worker | `procedures/dispatch.md` | Evidence returned to the lead |
| Decide whether a step is right | `procedures/check.md` | A check record |
| Put reviewed work on `main` | `procedures/land.md` | The work on `main`, or held with the reason |
| Certify a result for publication | `procedures/audit.md` | Audit records over one closure |
| Fix a named defect | `procedures/repair.md` | A source fix, or a justified request to recheck |
| Produce one document from existing records | `procedures/write.md` | A document with its own check request |

## The older skills

Each procedure ends with a table of step references. Those are files under
`skills/` and `.claude/commands/`, read only at the step that names them.
They predate the procedures: where one differs from `RULES.md` or from its
procedure, the newer file wins, and `SCIENCE_WORKFLOW.md` maps the older
status words.

A skill's own `SKILL.md` entry file is superseded by the procedure below. It
stays in place, unedited, because tooling still reads it.

| Procedure | Supersedes as entry point | Still read by tooling |
|---|---|---|
| `research` | `physics-loop`, `exercise`, `ai-physics-lane-builder`; the `physics-loop`, `exercise`, `pstack`, `autopilot` and `progress` commands | The axiom-baseline generator writes into `physics-loop/references/CLAIM_STATUS.md`; repair worker prompts name `physics-loop` |
| `dispatch` | `workhorse` and its command | A test opens the command file |
| `check` | `physics-claim-reviewer`; the gate in `no-go-discipline`; research gates | The audit dispatch allowlist names `no-go-discipline/SKILL.md` and `proof-search-governance.md` |
| `land` | `review-loop`, `reviewer-backpressure-integrator` and the `review-loop` command | `check_review_loop_skill_contract.py` pins the skill text, the landing shell and the command; tests execute that shell |
| `audit` | `audit-loop` | The skill file is hashed into every verdict's policy fingerprint and holds a generated block; the seat prompt is `docs/audit/AUDIT_AGENT_PROMPT_TEMPLATE.md` |
| `repair` | `science-fix-loop` | `science_fix_loop.py` embeds its worker prompts, and a test pins them |
| `write` | `densify`, `methodology-paper-synthesizer` and the `write-up` command | None found |

Seven commands remain the only home of their content and are step references
of `research`: `frontier`, `hypothesis`, `first-principles`,
`design-experiment`, `sweep`, `analyze` and `investigate-physics`. `ledger` is
a read-only lookup that `audit` relies on.

Removing an old entry file means changing the tooling in its row in the same
PR (`RULES.md` section 7). Copies of skills installed outside the repository
are written and checked by `sync_methodology_skills.py`; it does not install
`procedures/`, which are read from the checkout.
