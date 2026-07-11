# /pstack — Physics Science Stack Index

You are running PStack — the physics science stack for the qubit-lattice
axiom framework (four axioms: Lattice, Qubit, Admissibility, Record; see
`/framework-refresher`).

## Available Skills

### Orientation
| Skill | Role | What It Does |
|-------|------|-------------|
| `/framework-refresher` | Orientation | Load the current axioms, approved primitives, open obligations, vocabulary, and standing discipline before any physics work |
| `/ledger` | Status Lookup | Verify a claim's audit-ratified `effective_status` on `origin/main` before citing or building on it |

### Research Direction
| Skill | Role | What It Does |
|-------|------|-------------|
| `/hypothesis` | Research Director | Frame a falsifiable research question with a premise ledger and claim-type forecast |
| `/theory-review` | Theoretical Physicist | Check a hypothesis for axiom compliance, consistency, falsifiability, minimality, and claim-type fit |

### Experiment Design
| Skill | Role | What It Does |
|-------|------|-------------|
| `/design-experiment` | Experimental Physicist | Plan a runner around its decisive check, controls, and falsification observable |
| `/sweep` | Computational Physicist | Generate reproducible parameter sweep + collector scripts |

### Analysis & Validation
| Skill | Role | What It Does |
|-------|------|-------------|
| `/analyze` | Data Analyst | Analyze runner/sweep output against the hypothesis prediction |
| `/validate` | Reproducibility Officer | Robustness battery — independent-route math checks for exact runners; seeds/sensitivity/finite-size/cherry-pick for stochastic ones |
| `/sanity` | Senior Skeptic | Adversarial review: model consistency, scale, symmetry, limits, artifacts, bugs, hostile-reviewer semantic-bridge test |
| `/investigate-physics` | Detective Physicist | 4-phase anomaly investigation: characterize, hypothesize (bug/artifact/genuine), discriminate, resolve |

### Derivation & Negative Claims
| Skill | Role | What It Does |
|-------|------|-------------|
| `/first-principles` | First-Principles Theorist | Derive a target from axioms + approved primitives + retained theorems only |
| `/exercise` | Wall Breaker | Structured exercise suite against a stuck wall/blocker (repo-native skill) |
| `/no-go-gate` | Negative-Claim Gate | N1–N8 discipline before any no-go / walls-naming claim ships |

### Documentation & Strategy
| Skill | Role | What It Does |
|-------|------|-------------|
| `/write-up` | Scientific Writer | Archival summary of a completed investigation, in the repo voice |
| `/progress` | Research Manager | Periodic retrospective: claim-state movement, dead ends, pipeline health |
| `/frontier` | Research Strategist | Frontier map: lane census, blocker fanout, ranked highest-value gaps |
| `/autopilot` | Lab Operations | Status dashboard: locks, active loops, open PRs, audit backlog |

### Loops & Gates (repo-native skills)
| Skill | Role | What It Does |
|-------|------|-------------|
| `/physics-loop` | Physics Loop Lead | Long-running stateful loop on a hard lane: route portfolios, trace gates, V1–V5/N1–N8 gates, checkpoints, one review PR per science block |
| `/review-loop` | Review Board | Pre-landing gate: parallel physics reviewers, narrow honest fixes, audit-system compatibility without applying verdicts |

## Science Pipeline

```
/framework-refresher
        |
/hypothesis --> /theory-review --> /design-experiment --> [build runner] --> [run]
                                          |
                                       /sweep (if parameter scan)
                                          v
                               /analyze --> /validate --> /sanity
                                          |
                       /first-principles (derive)   /investigate-physics (anomalies)
                       /no-go-gate (negative claims)
                                          v
                                      /write-up
                                          v
                  distill to landing shape: 1 note (docs/) + 1 runner (scripts/)
                            + 1 cached output (logs/runner-cache/)
                                          v
              science branch off origin/main --> PR --> /review-loop (gate)
                                          v
                 independent audit lane ratifies on main (not run from here)
```

Side channels (run anytime): `/frontier`, `/progress`, `/ledger`,
`/autopilot`, `/exercise`, `/physics-loop` for campaigns.

## Core Principles

1. **Exhaust the Parameter Space** — AI makes sweeps cheap. Run the full
   scan, not spot checks.
2. **Import Discipline** — Derive from approved axioms and approved primitive
   registry entries when making framework claims; use known physics and
   literature only as disclosed comparators, targets, or external context that
   does not satisfy a framework dependency.
   Registered primitives, including the scale-reference and kinetic-isotropy
   primitives, are not bounded imports; unregistered primitives are not
   granted. The kinetic-isotropy primitive supplies only structural OS0
   kinetic-form isotropy `c_t = c_s`, not dynamics, Lorentz closure, scale,
   selector, or empirical content.
3. **Nature Decides** — Artifacts are ground truth. When theory and a
   verified runner disagree, investigate the runner first, then the theory.
4. **The Ledger Is Authoritative** — `docs/audit/data/audit_ledger.json` on
   `origin/main` is the only source of retained-grade status. Note headers,
   memory, and prose go stale.
5. **Propose, Never Ratify** — Author-side surfaces use `proposed_*` /
   `support` / `bounded` / `open` vocabulary. Audit verdicts come only from
   the independent audit lane; nothing in this stack runs it.
6. **Negative Claims Are Claims** — A no-go forecloses routes permanently;
   it passes `/no-go-gate` (N1–N8) or it does not ship.

## Lock & Worktree Protocol

Prefer a dedicated git worktree on a science branch off `origin/main` for any
work that mutates files — concurrent sessions race a shared checkout. When
running compute or mutations in a shared checkout, use the cooperative lock:

```bash
python3 scripts/automation_lock.py acquire --owner pstack-{skill} --purpose "{description}" --ttl-hours N
python3 scripts/automation_lock.py release --owner pstack-{skill}
```

Read-and-think skills (hypothesis, theory-review, sanity, first-principles,
write-up, progress, frontier, ledger, pstack) need no lock.

## Output Directory

PStack working documents live in `.claude/science/` (branch-local; the audit
citation graph scans `docs/` only, so working notes here never pollute it):

```
.claude/science/
  hypotheses/        experiments/       analyses/
  validations/       sanity/            investigations/
  derivations/       write-ups/         progress/
  frontier/          theory-reviews/    exercises/
  physics-loops/     research-lanes/
```

Working documents do not land on `main`. Landable science is distilled to
the note + runner + cache shape and goes through a science-branch PR and
`/review-loop`.

Print this index when invoked. Ask the user which skill to run.

## Execution Mechanism (standing — 2026-06-12)

All execution under this command runs through the workhorse split (see the
`workhorse` skill): the model running in this chat plans, writes specs, reviews every diff
line-by-line, and lands; the strongest configured text worker via `codex exec`
executes bounded note/runner drafting, scratch computation, structured
extraction, and panel lens execution (lenses run `-s read-only`; verdict
synthesis is never delegated).
No-go planning discipline applies: read the actual no-go note's primary text
and plan against its exact audited scope, never its title or a secondary
summary; if work reveals no-go language broader than its audited
`claim_scope`, queue a narrowing repair PR. Where this command references
review-loop or audit steps, those lanes are owner-operated (standing rule
2026-06-11): prepare the PR/review surface and hand off; never run them.
