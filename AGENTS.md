# AGENTS.md — agent instructions (canonical home: branch `ai/execution`)

Baseline for all automated executors (codex, subagents) working in this
repository, plus the dispatcher-side operating model. This file lives on the
standing `ai/execution` branch (never merges into main); read it from any
checkout without touching your working tree:

```bash
git fetch origin ai/execution --quiet
git show origin/ai/execution:AGENTS.md
```

Per-dispatch spec text adds to this file; it never overrides it. On any
conflict, the independent audit lane's rules and origin/main's checked-in
policy docs win.

## Anti-fabrication (mandatory)

- Never fabricate a numeric result, a runner output, or a PASS line. If a
  computation did not run, say so.
- Never fit a scalar prefactor to force a match with a target value; derive it
  or report the honest residual.
- Derive, don't hard-code: a runner must compute the claimed value, never embed
  the expected constant and compare it to itself.
- Report failures verbatim. A FAIL honestly reported is good work; a masked
  FAIL is fabrication.

## Runner discipline

- Runner stdout stays under 6000 characters.
- Print a final summary line `TOTAL: PASS=<n> FAIL=<n>`; a green claim requires
  FAIL=0.
- Check bounds at pass tolerances; do not print platform-dependent noise digits
  (1e-13…1e-19 tails) as if they were results.

## Scope limits

- No `git commit`, `git push`, or network access in analysis dispatches; edit
  only where the dispatch says.
- Never edit audit or ledger surfaces (effective-status data, queues, shards,
  grade fields). Audit status is set only by the independent audit lane.
- Use framework terms in prose and notes; no ad-hoc coinages or internal
  shorthand indices.

## Canonical sources

- Axioms: `git show origin/main:docs/MINIMAL_AXIOMS_2026-06-29.md` — a working
  tree can be stale; origin/main is the only status authority.
- Terminology: `docs/KEY_TERMINOLOGY.md` (same rule: read it from origin/main).

## Operating model (dispatcher side)

- Split of labor: the orchestrating session does problem selection,
  theorem/spec design, line-by-line review, landing, and memory; dispatched
  workers execute specs — note drafts, runner implementation, scratch
  computation, mechanical edits, panel lenses.
- Workers never choose targets and never touch governance or audit language.
- Review worker output line-by-line before landing anything; fabrication under
  pressure is a documented failure mode, and spot checks miss it.
- Prefer several narrow parallel lanes (typically 4–7) with sharp yes/no
  deliverables over one broad dispatch; work at compute speed, not human
  cadence.
- Memory budgets MULTIPLY across parallel runners (peak = per-runner ×
  concurrent agents): estimate before building; dense Fock representations are
  forbidden at 2^11 sites and above; on small-RAM hosts check actual free
  memory before each dispatch wave.
- Anything governance-sensitive gets adversarial verification (independent
  refuter lenses) before it is promoted.

## Surfaces on this branch

- `TOE_SCORECARD.md` — distance-to-goal map for positive closure (root-first
  DAG + bounded→positive restatement lever). Check its header sha against
  origin/main before relying on any line.
- `README.md` — the branch contract: never merges, direct pushes with
  `[skip ci]`, invisible to the audit citation graph by design.
