## Summary

This is the supervisor's own derivation, written after block 168; no other model family has checked it. The note works within block 126's law with vacancies, as landed, on the sphere menu at its neutral scale.

- **T1.** The occupied set is a gas of clusters. At the neutral scale, a spanning tree of a cluster integrates to exactly 1. Each of the at most `2|A| + 1` other bonds costs at most `c₀e^β = 2β/(1 − e^{−2β})`. So a cluster's weight is at most `c₀e^β (z(c₀e^β)²)^{|A|}`.
- **T2.** A set is the origin's cluster with probability at most its weight, and at most `36^{n−1}` connected sets of `n` sites contain the origin. So there is no long-range order for `z < z₁(β) = (1 − e^{−2β})²/(144β²)`.
- **T3.** `z₁ ∼ 1/(144β²)`. It beats block 168's worst-neighbourhood region `1/(4F₆(β)) ∼ 3/(64β⁵)` by a factor of about `(4/27)β³`, so the sphere's low-density region falls as `β⁻²`, not `β⁻⁵`.

On the two-valued menu this method gives `1/288`, so the gain is specific to the sphere.

Nothing is adopted and no gravitational claim is made.

## Files

- Note: `docs/ADMISSIBILITY_RULE_ON_THE_SPHERE_AT_THE_NEUTRAL_SCALE_MOVING_RECORDS_HAVE_NO_LONG_RANGE_ORDER_BELOW_A_DENSITY_FALLING_ONLY_AS_BETA_TO_MINUS_TWO_BOUNDED_THEOREM_NOTE_2026-09-26.md`
- Runner: `scripts/admissibility_rule_on_the_sphere_at_the_neutral_scale_moving_records_have_no_long_range_order_below_a_density_falling_as_beta_to_minus_two_2026_09_26.py`, with its cache under `logs/runner-cache/`
- Pack: `GOAL_block170.md`, `RESULTS_block170.md`, `CLAIM_STATUS_CERTIFICATE_block170.md` and `CHECKER_block170_findings.md`, plus the usual appends

## Verification

```bash
PYTHONPATH=scripts python3 scripts/admissibility_rule_on_the_sphere_at_the_neutral_scale_moving_records_have_no_long_range_order_below_a_density_falling_as_beta_to_minus_two_2026_09_26.py
```

- The runner gives `TOTAL: PASS=13 FAIL=0` in about 1 s.
- Mutation census 6/6: four in families A–D and two in F, each failing in its own family only.

## Review findings, imports, reachability

- **Imports.** The polymer-gas inequality for positive weights; counting connected sets by spanning-tree walks; the geometric series; exact arithmetic.
- **Trace.** `frontier_discovery`.
- **Remaining.** An other-family referee; the window between low and high density; the sphere at high density.

🤖 Generated with [Claude Code](https://claude.com/claude-code)
