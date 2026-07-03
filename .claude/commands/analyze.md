# /analyze — Result Analysis & Interpretation

You are the Data Analyst interpreting runner and sweep output for the
qubit-lattice axiom framework.

## Preflight

1. Identify what to analyze:
   - If the user specifies a log or runner, use that.
   - Otherwise find the most recent relevant output in `logs/` or
     `logs/runner-cache/` (read expensive runners through
     `python3 scripts/cached_runner_output.py <runner>` rather than
     re-executing them).
   - Read the hypothesis doc (`.claude/science/hypotheses/`) and experiment
     design (`.claude/science/experiments/`) if they exist.
2. No lock is needed to read logs and write analysis documents. If the
   analysis requires re-running compute in a shared checkout, follow the
   lock protocol in `/pstack` first.

## Analysis Steps

### 1. Data Extraction
- Extract observables, parameter values, and metadata from the target
  output. Report: N data points, ranges covered, missing/failed runs.

### 2. Statistical Summary
For each observable: mean, median, std, min/max, distribution shape,
outliers (> 3 sigma). For exact (integer/rational/symbolic) outputs, state
exactness explicitly instead of fabricating error bars.

### 3. Trend Detection
- Systematic change with the swept parameter? Monotonic, peaked,
  oscillatory? Effect size relative to noise? Threshold behavior?

### 4. Anomaly Flagging
- Broken monotonicity or symmetry, jumps, variance explosions, NaN/inf,
  failed runs. Anything flagged here feeds `/investigate-physics` — do not
  interpret an anomaly before it is investigated.

### 5. Hypothesis Verdict
Compare to the prediction in the hypothesis document:
- **SUPPORTED** — matches prediction within stated criteria.
- **REFUTED** — contradicts prediction beyond stated threshold.
- **AMBIGUOUS** — neither; state what additional data would resolve it.
- **INSUFFICIENT** — not enough data; state what is needed.

These are working-doc verdicts about the hypothesis. They are not claim
statuses: landing language stays in author-side vocabulary
(`proposed_*` / `support` / `bounded` / `open`) and audit verdicts belong to
the audit lane alone.

### 6. Follow-Up Recommendations
- Next experiment; narrow/widen/shift ranges; new observables needed.

## Output

Write the analysis to `.claude/science/analyses/{slug}-{date}.md` with all
sections above. Create the directory if it does not exist.

## Rules

- Quote specific numbers from the logs — no vague claims.
- Distinguish statistical significance from practical significance.
- If the data is ambiguous, say so. Do not force a verdict.
- Interpret in framework vocabulary (sites, qubits, operators, sectors,
  records, named lanes). Known-physics values may appear only as disclosed
  comparators with their source named; flag any imported number that the
  interpretation silently leans on.
- An exciting match to a known constant is a comparator observation, not a
  derivation — say which one it is.

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
