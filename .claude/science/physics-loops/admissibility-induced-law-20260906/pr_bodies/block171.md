## Summary

This harvests probe #9122 (a Claude Opus 5.5 worker, the supervisor's own model family). An other-family referee confirmed it in #9336 (`grok-4.6`). The note works within blocks 110 and 95, both landed.

- **T1.** Records that cross at the member's factor `√(w_x w_y)/(χ_x χ_y)`, with block 95's heat-bath factor, have `π ∝ W` for every fixed clock and length field. The same holds at first order for fields that follow the records with even kernels. So these records do not gather in their own field; timing by the leaving site gives `W/Π w` instead.
- **T2.** Records are a process, not an energy, so the member's two charges need a supplied clause for a record's `(e, τ)`. Two clauses have block 110's homogeneity. On the same three records and fields, rest only gives `P − Q = −117/3280` and the activity at the crossing factor gives `+3893397/2555120`.
- **T3.** Under the activity clause at weak field, `P/Q = 1 + μ⟨B⟩/(mN + μ⟨B⟩/2) > 1` whenever a record can move. The exact values are `251/101` and `121/49` under the uniform law, and exact values of about 2.43 and 2.34 under the clocked gas's law. `P = Q` needs a hop energy that vanishes with the field.

Nothing is adopted and no gravitational claim is made.

## Files

- Note: `docs/ADMISSIBILITY_RULE_MOVING_RECORDS_CARRY_NO_ENERGY_SO_THEIR_TWO_CHARGES_NEED_A_SUPPLIED_CLAUSE_AND_UNDER_THE_ACTIVITY_CLAUSE_THEY_NEVER_BALANCE_AT_WEAK_FIELD_BOUNDED_THEOREM_NOTE_2026-09-27.md`
- Runner: `scripts/admissibility_rule_moving_records_carry_no_energy_so_their_two_charges_need_a_supplied_clause_2026_09_27.py`, with its cache under `logs/runner-cache/`
- Pack: `GOAL_block171.md`, `RESULTS_block171.md`, `CLAIM_STATUS_CERTIFICATE_block171.md` and `CHECKER_block171_findings.md`, plus the usual appends

## Verification

```bash
PYTHONPATH=scripts python3 scripts/admissibility_rule_moving_records_carry_no_energy_so_their_two_charges_need_a_supplied_clause_2026_09_27.py
```

- The runner gives `TOTAL: PASS=13 FAIL=0` in about 1 s.
- Mutation census 6/6: four in families A–D and two in F, each failing in its own family only.

## Review findings, imports, reachability

- **Imports.** Detailed balance; the mean-zero inverse of the torus Laplacian; exact enumeration; exact arithmetic.
- **Trace.** `frontier_discovery`.
- **Remaining.** The member solved self-consistently with record sources; a record virial for a hop energy that vanishes with the field; the owner's clause.

🤖 Generated with [Claude Code](https://claude.com/claude-code)
