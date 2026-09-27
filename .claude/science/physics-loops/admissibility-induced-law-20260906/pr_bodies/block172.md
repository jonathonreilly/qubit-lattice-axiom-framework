## Summary

This harvests probe #9212 (a Claude Opus 5.5 worker, the supervisor's own model family). An other-family referee confirmed it in #9338 (`grok-4.6`). The note works within block 117, as landed: the record gas, its chessboard frames and its wall-removing map.

- **T1.** Take a finite, face-connected region of `ℤ³` whose complement is also face-connected. Its wall is connected through shared edges, and each plaquette has 12 edge-neighbours. A cavity, or a touch at a corner only, would split it.
- **T2.** So the walls of area `k` around a site number at most `(k/4) r_k`, with `r_k = (12/(k − 1)) C(11k, k − 2)`. The radius is `10¹⁰/11¹¹ ≈ 0.035`, against block 117's `0.012`.
- **T3.** At `x₀ = 347/10000` the defect sum is at most `11/100`, using an exact supersolution; the attempt had 0.143. So:
  - the framed states have `⟨σ_x⟩ ≥ 39/50` and `≤ −39/50`;
  - without contents the chessboard holds for `g ≤ (347/10000)²`, which is `(347/120)² ≈ 8.36` times block 117's `9/62500`;
  - every content case scales by the same factor;
  - at block 117's own `x₀` the defect sum drops from 0.0897 to at most 4/10000.

Nothing is adopted and no gravitational claim is made.

## Files

- Note: `docs/ADMISSIBILITY_RULE_WALLS_OF_FILLED_REGIONS_ARE_CONNECTED_THROUGH_EDGES_SO_THE_RECORD_GAS_MAKES_THE_CHESSBOARD_UP_TO_A_BOND_COST_OF_347_OVER_10000_SQUARED_BOUNDED_THEOREM_NOTE_2026-09-27.md`
- Runner: `scripts/admissibility_rule_walls_of_filled_regions_are_connected_through_edges_so_the_record_gas_makes_the_chessboard_up_to_a_larger_bond_cost_2026_09_27.py`, with its cache under `logs/runner-cache/`
- Pack: `GOAL_block172.md`, `RESULTS_block172.md`, `CLAIM_STATUS_CERTIFICATE_block172.md` and `CHECKER_block172_findings.md`, plus the usual appends

## Verification

```bash
PYTHONPATH=scripts python3 scripts/admissibility_rule_walls_of_filled_regions_are_connected_through_edges_so_the_record_gas_makes_the_chessboard_up_to_a_larger_bond_cost_2026_09_27.py
```

- The runner gives `TOTAL: PASS=12 FAIL=0` in about 3 s.
- Mutation census 6/6: four in families A–D and two in F, each failing in its own family only.

## Review findings, imports, reachability

- **Imports.** Series inversion; breadth-first spanning trees; parity of ray crossings; exact arithmetic.
- **Trace.** `frontier_discovery`.
- **Remaining.** Block 117's half-filling window with contents; the walker's gap on the gas's arrangements.

🤖 Generated with [Claude Code](https://claude.com/claude-code)
