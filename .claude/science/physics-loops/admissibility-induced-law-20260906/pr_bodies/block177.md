## Summary

This harvests probe #8992 (a Claude Opus 5.5 worker, the supervisor's own model family). An other-family referee confirmed it in #9349 (`grok-4.6`). The note works within block 39's transit, as landed, for the full `L × L × L` box of aligned records.

- **T1.** A record at distance `d` from the outside can first move at move `d`. So the movable set grows by one layer per move.
- **T2.** `N₁ = 6L²` and `N₂ = 18L⁴ + 33L² − 24L`, split into `C(6L², 2) − 12L` arrangements with two displaced records and `36L² − 12L` with one. This is checked by exact enumeration for `L = 2..9`.
- **T3.** The arrangements with `T` displaced records number `[x^T](1+x)^{6(L−2)²}(1+2x)^{12(L−2)}(1+3x)⁸`. So `N_T = (6L²)^T/T! + O(L^{2T−2})`, with no `L^{2T−1}` term and no volume term.

This extends block 127's one-move census.

Nothing is adopted and no gravitational claim is made.

## Files

- Note: `docs/ADMISSIBILITY_RULE_A_JAMMED_BOX_OF_MOVING_RECORDS_REARRANGES_ONLY_FROM_ITS_SURFACE_ONE_LAYER_PER_MOVE_AND_ITS_REACHABLE_ARRANGEMENTS_HAVE_NO_VOLUME_TERM_BOUNDED_THEOREM_NOTE_2026-09-27.md`
- Runner: `scripts/admissibility_rule_a_jammed_box_of_moving_records_rearranges_only_from_its_surface_2026_09_27.py`, with its cache under `logs/runner-cache/`
- Pack: `GOAL_block177.md`, `RESULTS_block177.md`, `CLAIM_STATUS_CERTIFICATE_block177.md` and `CHECKER_block177_findings.md`, plus the usual appends

## Verification

```bash
PYTHONPATH=scripts python3 scripts/admissibility_rule_a_jammed_box_of_moving_records_rearranges_only_from_its_surface_2026_09_27.py
```

- The runner gives `TOTAL: PASS=11 FAIL=0` in about 3 s.
- Mutation census 6/6: four in families A–D and two in F, each failing in its own family only.

## Review findings, imports, reachability

- **Imports.** Breadth-first enumeration; generating functions; exact arithmetic.
- **Trace.** `frontier_discovery`.
- **Remaining.** Faceted shapes; the exact three-move polynomial; the dynamics' weights.

🤖 Generated with [Claude Code](https://claude.com/claude-code)
