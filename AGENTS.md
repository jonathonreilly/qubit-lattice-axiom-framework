# AGENTS.md — executor guardrails

Baseline for all automated executors (codex, subagents) working in this
repository. Per-dispatch spec text adds to this file; it never overrides it.

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
