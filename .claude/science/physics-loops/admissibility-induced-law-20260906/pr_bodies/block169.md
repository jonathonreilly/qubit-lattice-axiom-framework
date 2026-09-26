## Summary

This harvests probe #9158 (a Claude Opus 5.5 worker, the supervisor's own model family). An other-family referee confirmed it in #9325 (`grok-4.6`). The note works within block 95's records, as landed, with a supplied clause: the clock field relaxes towards the records at rate `Γ`, `du/dt = Γ w (Mu + λ(n − n̄))`. Everything is on finite tori, under two stated assumptions: A0 (well-posedness) and A1 (differentiability at `λ = 0`).

- **T1.** `Σ 1/w` is conserved. For a fixed configuration the field settles to the slaved field.
- **T2.** At `a = 1`, `W = 1`, two records' separation jumps as the simple random walk on the torus minus the origin, at every `Γ` and `λ`. So the pair law is set by the mean sojourn times.
- **T3** (given A1). At first order in `λ`, the mean field given the records is `γ = 2Γ/(2Γ + 1)` times the slaved field. The pair law is block 95's with `λ → γλ`; on ring 6 the weights are `−1/3, 1/6, 1/3` times `γλ`.
- **T4, T5** (given A0). At finite `Γ` there is no stationary product law and no reversible stationary law.

Nothing is adopted and no gravitational claim is made.

## Files

- Note: `docs/ADMISSIBILITY_RULE_A_CLOCK_THAT_FOLLOWS_THE_RECORDS_LATE_KEEPS_THEIR_PAIR_LAW_AT_FIRST_ORDER_WITH_THE_COUPLING_SCALED_BY_TWO_GAMMA_OVER_TWO_GAMMA_PLUS_ONE_BOUNDED_THEOREM_NOTE_2026-09-26.md`
- Runner: `scripts/admissibility_rule_a_clock_that_follows_the_records_late_keeps_their_pair_law_at_first_order_2026_09_26.py`, with its cache under `logs/runner-cache/`
- Pack: `GOAL_block169.md`, `RESULTS_block169.md`, `CLAIM_STATUS_CERTIFICATE_block169.md` and `CHECKER_block169_findings.md`, plus the usual appends

## Verification

```bash
PYTHONPATH=scripts python3 scripts/admissibility_rule_a_clock_that_follows_the_records_late_keeps_their_pair_law_at_first_order_2026_09_26.py
```

- The runner gives `TOTAL: PASS=16 FAIL=0` in about 1 s.
- Mutation census 7/7: five in families A–E and two in F, each failing in its own family only.

## Review findings, imports, reachability

- **Imports.** Dynkin's formula (under A0); LaSalle's invariance principle; the symmetric exclusion process; exact arithmetic.
- **Trace.** `frontier_discovery`.
- **Not ported.** The one-record rate, the rate-weighted identity and the direct simulation.
- **Remaining.** A0 and A1; the second order in `λ`.

🤖 Generated with [Claude Code](https://claude.com/claude-code)
