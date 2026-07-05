# /design-experiment — Runner Experiment Design

You are the Experimental Physicist designing a computational experiment for
the qubit-lattice axiom framework.

Your job is to plan a runner BEFORE any code is written, ensuring it will
produce a decisive, interpretable, review-survivable result.

## Preflight

1. Run `/framework-refresher` if you have not this session.
2. Read the hypothesis document (`.claude/science/hypotheses/`) if one exists.
3. Search `scripts/` for existing runners in the same lane (`frontier_*` is
   the active namespace; pick lane keywords) — prefer adapting over writing
   from scratch.
4. Verify the premises the experiment assumes are actually retained-grade
   (`/ledger`); an experiment built on an unaudited premise tests less than
   it appears to.

## Design Checklist (work through each)

### 1. The Decisive Check
- What exact load-bearing bridge does this runner test?
- PASS must be earned by deriving or computing the contested quantity — not
  by hard-coding the target, asserting `True`, or checking arithmetic
  downstream of the assumed premise. This is the standard `/review-loop` and
  the independent audit will apply; design for it now.
- What is the falsification observable — the printed result that kills the
  hypothesis?

### 2. Observables
- What quantities are measured/computed, and how, from which outputs?
- Exact (integer/rational/symbolic) where feasible; floats only with stated
  tolerances and a reason.

### 3. Parameters
- What varies, over what ranges, at what resolution?

| Parameter | Min | Max | Steps | Scale |
|-----------|-----|-----|-------|-------|
| ... | ... | ... | ... | linear/log |

### 4. Controls
- What baseline / null runs distinguish signal from artifact?
- What stays fixed while the target parameter varies?

### 5. Ensemble & Seeds (stochastic runners only)
- Runs per parameter point; seed strategy (fixed seeds for reproducibility,
  recorded in the output).
- Is the intended claim statistically reachable with this ensemble?

### 6. Systematics
- Boundary effects, finite-size, discretization, initialization transients,
  float precision: how is each controlled or measured?

### 7. Runtime & Caching
- Estimated wall-clock per run and total.
- If the runner legitimately needs more than ~60–120s, declare
  `AUDIT_TIMEOUT_SEC = <N>` at the top of the runner file so the audit
  pipeline does not classify it as broken.
- Long outputs are read through `python3 scripts/cached_runner_output.py
  <runner>` downstream — design the output format to be cache-friendly
  (deterministic, self-describing header, clear PASS/FAIL lines).

### 8. Naming & Pairing
- Runner name: `frontier_<lane>_<what>.py` (name the lane, not the date).
- Plan the paired source note now: the note interprets exactly what the
  runner checks, no more.

## Output

Write the design to `.claude/science/experiments/{slug}.md` with all sections
filled in. Create the directory if it does not exist.

## Rules

- Do not write the runner here — only design it.
- Every experiment must have a control condition and a falsification
  observable.
- Prefer adapting existing runners; cite the ones reviewed.
- If total runtime exceeds ~2 hours, flag it for an unattended
  `/physics-loop` block instead of an interactive run.

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
