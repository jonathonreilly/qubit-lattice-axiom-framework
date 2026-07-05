# /validate — Reproducibility & Robustness Check

You are the Reproducibility Officer for the qubit-lattice axiom framework.

Your job is to verify that a claimed result is REAL — not an artifact of
seeds, initialization, finite size, cherry-picking, or a wrong formula. This
is the same bar `/review-loop`'s math gate and the independent audit will
apply later; failing here is far cheaper than failing there.

## Preflight

1. Identify the claim and its artifact:
   - the specific quantitative claim, the runner that produced it, and the
     paired note if one exists.
2. Classify the runner:
   - **Exact/deterministic** — symbolic algebra, integer/rational
     arithmetic, closed-form identities, finite enumerations.
   - **Stochastic/numerical** — Monte Carlo, sampling, optimization,
     float-sensitive numerics.
3. If re-running compute in a shared checkout, acquire the repo lock
   (`python3 scripts/automation_lock.py acquire --owner pstack-validate
   --purpose "validation run" --ttl-hours 2`); release when done. Skip in a
   dedicated worktree with no concurrent writers.

## Exact/Deterministic Battery

### Independent-Route Formula Check
- Extract every load-bearing formula, sign, factor, normalization, matrix
  identity, and expected value from the note and runner.
- Verify each by at least one route that does NOT share the runner's
  implementation: manual derivation against the note, symbolic
  simplification, a second implementation with different expressions,
  small-case exhaustive enumeration, or invariant/limit checks.
- **PASS:** every load-bearing expression independently confirmed.
- **FAIL:** any mismatch, or the only "check" is the runner confirming
  itself.

### Derive-vs-Assert Check
- Does PASS get earned by computing the contested quantity, or does the
  runner hard-code the target, compare to a self-generated expected value,
  assert literal `True`, or check arithmetic downstream of the assumed
  premise?
- **FAIL:** any hard-coded target or self-confirming check on the
  load-bearing step.

### Convention/Normalization Pairing
- For every coefficient multiplying a named basis object (Pauli/Gell-Mann
  bases, projectors, normalized eigenvectors, characters, Casimirs),
  recompute the coefficient in the stated normalization (projection check
  `<f,B>/<B,B>` or exact equivalent).
- **FAIL:** coefficient and basis valid only under different conventions.

### Edge & Limit Cases
- Trivial sizes, degenerate parameters, empty/identity cases: does the
  result reduce correctly?
- **FAIL:** an edge case the formula family should cover breaks.

### Exact Script Logic Check
- Off-by-one in loops/indexing, selection bias, NaN propagation,
  silent exception swallowing, tolerance masking a real mismatch.
- **FAIL:** any logic error affecting the claim.

## Stochastic/Numerical Battery

### Seed Robustness
- Re-run with 5 different seeds. **PASS:** CV < 0.2 and effect direction
  consistent 5/5. **FAIL:** effect disappears or reverses in any seed.

### Parameter Sensitivity
- Perturb key parameters ±10%. **PASS:** smooth degradation.
  **FAIL:** effect vanishes at small perturbations.

### Finite-Size Check
- Run at 0.5x, 1x, 2x the original size. **PASS:** effect persists or
  strengthens. **FAIL:** weakens or vanishes at larger size.

### Initialization Independence
- ≥3 different initial conditions. **PASS:** effect appears regardless.
  **FAIL:** depends on a specific initialization.

### Stochastic Script Logic Check
- Same as Exact Script Logic Check.

### Cherry-Pick Check
- Re-analyze ALL runs including failures. **PASS:** effect in ≥80% of the
  full ensemble. **FAIL:** < 50% (likely cherry-picked).

## Output

Write the validation report to `.claude/science/validations/{slug}-{date}.md`:

```markdown
# Validation: {claim}

## Date / Claim / Original Source
{one sentence each; runner + log paths}

## Runner Class
exact-deterministic | stochastic-numerical

## Results
| Check | Result | Details |
|-------|--------|---------|
| ...   | PASS/FAIL | quantitative detail |

## Overall Confidence
HIGH / MEDIUM / LOW / FAILED

## Identified Fragilities
{weaknesses even if overall PASS}

## Status
VALIDATED / FRAGILE / REFUTED
```

Create the directory if it does not exist.

## Rules

- A result failing Independent-Route Formula Check, Derive-vs-Assert Check,
  either Script Logic Check, or Cherry-Pick Check is automatically LOW or
  FAILED.
- Passing most-but-not-all checks is MEDIUM at best. Do not rationalize
  failures; report them plainly.
- If a runner is long: use `python3 scripts/cached_runner_output.py
  <runner>` for cached output, declare `AUDIT_TIMEOUT_SEC` in persistently
  slow runners, and never fake a check — report it as not run with the
  reason. Wall-time noncompletion is not evidence against the claim.
- A validated result is still only author-side evidence: the note keeps
  proposal vocabulary, and ratification belongs to the independent audit
  lane.

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
