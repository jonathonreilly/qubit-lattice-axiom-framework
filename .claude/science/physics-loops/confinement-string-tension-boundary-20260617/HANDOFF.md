# Handoff

Branch: `codex/confinement-string-tension-boundary-20260617`

This PR repairs the source-side boundary for
`confinement_string_tension_note`.

What changed:

- The source note now states bounded-support status and removes retained-grade
  authority.
- The exact beta=6 arithmetic is preserved.
- Standard Yang-Mills confinement, Sommer-scale, EFT running, and
  phenomenological comparators are explicitly bounded imports.
- The runner now checks the source-status firewall and reports support rather
  than retained theorem closure.

Checks run:

- `python3 scripts/frontier_confinement_string_tension.py`
- `python3 scripts/cached_runner_output.py --refresh scripts/frontier_confinement_string_tension.py`
- `python3 -m py_compile scripts/frontier_confinement_string_tension.py`

Not done:

- No audit-loop run.
- No audit ledger, queue, publication, or front-door edits.
- No review-loop run; reviewer owns that step.
