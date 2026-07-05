# /sweep — Parameter Sweep Generator

You are the Computational Physicist generating systematic parameter sweeps
for the qubit-lattice axiom framework.

AI makes sweeps cheap: run the full scan, not spot checks. A sweep's value is
coverage plus reproducibility.

## Preflight

1. If running in a shared checkout, acquire the repo lock first:
   ```bash
   python3 scripts/automation_lock.py status
   ```
   - If held by another owner, STOP and report.
   - If free:
   ```bash
   python3 scripts/automation_lock.py acquire --owner pstack-sweep --purpose "generating sweep scripts" --ttl-hours 1
   ```
   (In a dedicated worktree with no concurrent writers, the lock may be
   skipped — say so.)

2. Identify the base runner and parameters:
   - Which script in `scripts/` is the starting point?
   - What parameters are swept, over what ranges?
   - Read the experiment design from `.claude/science/experiments/` if one
     exists.

## Generation Process

### 1. Analyze the Base Runner
- Read it fully. Identify tunable parameters (hardcoded values, argparse
  arguments, constants), the output format, and per-run runtime.

### 2. Design the Sweep

| Parameter | Values | Count |
|-----------|--------|-------|
| ... | [list or range] | N |

- Total combinations: N1 × N2 × ...; estimated total runtime.
- If > 2 hours total, warn and suggest reduction or an unattended
  `/physics-loop` block.

### 3. Generate the Sweep Script
Create `scripts/sweep_<lane>_<what>.py` that:
- Iterates all combinations; records parameter metadata with every result.
- Writes a structured log to `logs/{sweep_name}_{timestamp}.txt` with a
  header comment documenting the full parameter grid and seed strategy.
- Records random seeds explicitly; fixed seeds for reproducibility.
- Handles failures gracefully (log and continue), reports progress every
  ~10% of combinations.

### 4. Generate the Collector
Create `scripts/sweep_<lane>_<what>_collect.py` that:
- Parses the sweep log, aggregates a summary table, computes per-value
  statistics (mean, std, min, max), and identifies the strongest/weakest
  effect locations.

### 5. Dry Run
- Run the FIRST combination only; verify the collector parses the output.
- Fix issues before the full sweep.

## Output

- The runner and collector scripts; report total combinations, estimated
  runtime, and the launch command.
- Sweep scripts are exploration tooling: they support a claim but are not
  themselves the decisive artifact. If a sweep result becomes a claim, it
  needs its own paired note + decisive runner + cached output through
  `/review-loop`.

## Cleanup

Release the lock if acquired:
```bash
python3 scripts/automation_lock.py release --owner pstack-sweep
```

## Rules

- Never generate more than 1000 combinations without user approval.
- Always dry-run before the full sweep; every sweep must be reproducible
  (seeds and grid recorded in the log header).
- Name scripts descriptively by lane and content, never `sweep1.py`.
- Prefer adapting existing scripts over writing from scratch.

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
