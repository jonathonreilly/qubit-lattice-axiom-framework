## Summary

Blocks 135 and 136 (landed) kept the two-step content's symmetric books, and met the member's identity exactly for every state iff `α = K/4`. Both needed averages: the energy over the eight body-diagonal neighbours, and block 120's transverse average in the stress. Both also found the unaveraged realisation or momenta failing. This note shows the averages are not needed with block 179's placement.

- **T1.** The plain site energy `e = Re ψ†Hψ` has current exactly `P^s`, block 179's unaveraged two-step momentum density. So the energy current is the momentum density.
- **T2.** `P^s` has exactly the symmetric current `K^s` (block 179, re-checked).
- **T3.** Hence `ë = Σ_aj ∇̄_a∇̄_jK^s_aj` for every state, all species and both branches. These are matrix-symbol identities; at an exact pair both sides are `−96/625`.
- **T4.** With the plain site energy sourcing the clock and `K^s` as the stress, block 135's member demand holds for every state iff `α = K/4`. The averaged identities of blocks 135 and 136 are these, averaged.

The supervisor's own derivation, unrefereed. Nothing is adopted and no gravitational claim is made.

## Files

- Note: `docs/ADMISSIBILITY_RULE_SYMMETRIC_BOOKS_WITHOUT_AVERAGING_THE_PLAIN_SITE_ENERGY_MEETS_THE_MEMBERS_IDENTITY_EXACTLY_WITH_A_SYMMETRIC_TWO_STEP_STRESS_BOUNDED_THEOREM_NOTE_2026-09-27.md`
- Runner: `scripts/admissibility_rule_symmetric_books_without_averaging_2026_09_27.py`, with its cache under `logs/runner-cache/`
- Pack: `GOAL_block181.md`, `RESULTS_block181.md`, `CLAIM_STATUS_CERTIFICATE_block181.md` and `CHECKER_block181_findings.md`, plus the usual appends

## Verification

```bash
PYTHONPATH=scripts python3 scripts/admissibility_rule_symmetric_books_without_averaging_2026_09_27.py
```

- The runner gives `TOTAL: PASS=13 FAIL=0` in about 3 s.
- Mutation census 7/7: five in families A–E and two in F, each failing in its own family only.

## Review findings, imports, reachability

- **Imports.** Symbols of local forms; summation by parts; exact arithmetic.
- **Trace.** `frontier_discovery`.
- **Remaining.**
  - An other-family referee.
  - The member's full field equations with `K^s`.
  - Rates and varying frames.

🤖 Generated with [Claude Code](https://claude.com/claude-code)
