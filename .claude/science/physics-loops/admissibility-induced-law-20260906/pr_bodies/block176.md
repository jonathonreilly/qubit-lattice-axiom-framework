## Summary

This is the supervisor's own derivation, written after block 173; no other model family has checked it. The note works within blocks 59, 60 and 69, all landed, and the principal-symbol ray model. Block 173 (pushed) is placement.

- **T1.** Every odd coupling of reach at most three with long-wave speed `w/ℓ` has the symbol `ℓs = sin k(1 − q sin² k)`, fixed by one number `q(ℓ)`. The frame is `q = 0`; block 69's linear completion is `q = 1 − ℓ`.
- **T2.** For `q ∈ [−1/6, 2/3]` no wave in any direction outruns `w/ℓ`. For `q < −1/6`, waves near the axes do.
- **T3.** In the same range the bending factor `A` is at most 1, and for `q < −1/6` it exceeds 1. With `ρ ∈ [0, 1]`, every ray crossing the gradient bends at most `R` times the fall.
- **T4.** The completion `q = (1 − ℓ)/√(1 + 36(ℓ − 1)²)` agrees with block 69 at first order in the strain and meets both conditions at every stretch.

So block 173's flag concerns one completion, not block 69's coupling.

Nothing is adopted and no gravitational claim is made.

## Files

- Note: `docs/ADMISSIBILITY_RULE_A_REACH_THREE_COUPLING_KEEPS_ONE_SPEED_LIMIT_IFF_ITS_STRETCH_NUMBER_STAYS_ABOVE_MINUS_ONE_SIXTH_AND_A_SMOOTH_COMPLETION_OF_BLOCK_69_DOES_BOUNDED_THEOREM_NOTE_2026-09-27.md`
- Runner: `scripts/admissibility_rule_a_reach_three_coupling_keeps_one_speed_limit_iff_its_stretch_number_stays_above_minus_one_sixth_2026_09_27.py`, with its cache under `logs/runner-cache/`
- Pack: `GOAL_block176.md`, `RESULTS_block176.md`, `CLAIM_STATUS_CERTIFICATE_block176.md` and `CHECKER_block176_findings.md`, plus the usual appends

## Verification

```bash
PYTHONPATH=scripts python3 scripts/admissibility_rule_a_reach_three_coupling_keeps_one_speed_limit_iff_its_stretch_number_stays_above_minus_one_sixth_2026_09_27.py
```

- The runner gives `TOTAL: PASS=12 FAIL=0` in about 1 s.
- Mutation census 7/7: five in families A–E and two in F, each failing in its own family only.

## Review findings, imports, reachability

- **Imports.** Trigonometric identities; elementary bounds for quadratics; series and limits; exact arithmetic.
- **Trace.** `frontier_discovery`.
- **Remaining.** An other-family referee; what fixes the completion; couplings of longer reach.

🤖 Generated with [Claude Code](https://claude.com/claude-code)
