## Summary

This harvests probe #9304 (a Claude Opus 5.5 worker, the supervisor's own model family). An other-family referee confirmed it in #9329 (`grok-4.6`). The referee kept the occupation probability as `w/(1 + w)`, which enlarges the regions. The note works within block 126's law with vacancies at its neutral scales.

- **T1.** Given the rest, the weight at a site is at most `F₆(β) = (β/sinh β)⁶ sinh(6β)/(6β)` on the sphere and at most `G(tanh β) = (1 + t)⁶ + (1 − t)⁶` on the two-valued menu. Six aligned neighbours attain both.
- **T2.** There is no long-range order, and the structure factor is bounded, for `z < 1/(4F₆(β))` on the sphere and for `z < 1/(4G(tanh β))` on the two-valued menu. The second region contains `z < 1/256`, and so block 153's `1/320` (#9285).
- **T3.** The sphere's threshold tends to `1/4` at small `β` and to `3/(64β⁵)` at large `β`.

The window between low and high density, and the sphere at high density, stay open.

Nothing is adopted and no gravitational claim is made.

## Files

- Note: `docs/ADMISSIBILITY_RULE_AT_THE_NEUTRAL_SCALE_MOVING_RECORDS_HAVE_NO_LONG_RANGE_ORDER_AT_LOW_DENSITY_ON_BOTH_MENUS_AND_THE_SPHERE_THRESHOLD_FALLS_AS_BETA_TO_MINUS_FIVE_BOUNDED_THEOREM_NOTE_2026-09-26.md`
- Runner: `scripts/admissibility_rule_at_the_neutral_scale_moving_records_have_no_long_range_order_at_low_density_on_both_menus_2026_09_26.py`, with its cache under `logs/runner-cache/`
- Pack: `GOAL_block168.md`, `RESULTS_block168.md`, `CLAIM_STATUS_CERTIFICATE_block168.md` and `CHECKER_block168_findings.md`, plus the usual appends

## Verification

```bash
PYTHONPATH=scripts python3 scripts/admissibility_rule_at_the_neutral_scale_moving_records_have_no_long_range_order_at_low_density_on_both_menus_2026_09_26.py
```

- The runner gives `TOTAL: PASS=18 FAIL=0` in about 10 s.
- Mutation census 6/6: four in families A–D and two in F, each failing in its own family only.

## Review findings, imports, reachability

- **Imports.** Bernstein-basis certificates; sequential domination by independent occupation; the self-avoiding path bound; exact arithmetic.
- **Trace.** `frontier_discovery`.
- **Remaining.** An exploration with conditional neutrality for the window; the sphere at high density; the torus separation lemma.

🤖 Generated with [Claude Code](https://claude.com/claude-code)
