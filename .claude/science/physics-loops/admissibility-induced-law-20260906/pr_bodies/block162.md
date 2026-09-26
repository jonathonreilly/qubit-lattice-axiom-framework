## Summary

This harvests probe #9175 (a Claude Opus 5.5 worker, the supervisor's own model family). An other-family referee confirmed it in #9311 (a Grok worker). The note works within block 116's held-wall law, which is landed. Block 116 found that forming one record keeps the ledger only at a price. This note asks whether a rule of fixed radius, using only data near the record, can set that price.

- **T1.** The ledger is the total effective source: `Λ = Σ Kφ = Q`, `E' = Q/φ'_y`, and the post-event field is `kQ g(·, y)`.
- **T2.** Records only: the response at the record's site grows with the box. So one amplitude placed in two boxes has identical window data and different prices, for every radius.
- **T3.** Amplitude sourcing: add a charged cage of total charge 1 just outside the window, with zero field inside. Every window datum stays the same, and the ledger moves by the cage's charge.
- **T4.** A point-equivalent source (`s − Qδ_y = (1 − A)f` with `f` finite) has the exact local price `Q/(φ_y + k f_y)`. Block 116's star is such a source. The distance-two cross is not, as a discrete harmonic quartic shows.

So the formation price depends on the whole lattice under either reading, except for point-like sources. Nothing is adopted and no gravitational claim is made.

## Files

- Note: `docs/ADMISSIBILITY_RULE_NO_LOCAL_RULE_OF_ANY_FIXED_RADIUS_SETS_THE_PRICE_OF_FORMING_A_RECORD_UNDER_EITHER_READING_AND_A_POINT_EQUIVALENT_SOURCE_HAS_AN_EXACT_LOCAL_PRICE_BOUNDED_THEOREM_NOTE_2026-09-26.md`
- Runner: `scripts/admissibility_rule_no_local_rule_of_any_fixed_radius_sets_the_price_of_forming_a_record_2026_09_26.py`, with its cache under `logs/runner-cache/`
- Pack: `GOAL_block162.md`, `RESULTS_block162.md`, `CLAIM_STATUS_CERTIFICATE_block162.md` and `CHECKER_block162_findings.md`, plus appends to `HANDOFF.md`, `TRACE_GATE.md`, `REVIEW_HISTORY.md`, `STATE.yaml`, `OPPORTUNITY_QUEUE.md` and `APPROACH_REGISTRY.md`

## Verification

```bash
PYTHONPATH=scripts python3 scripts/admissibility_rule_no_local_rule_of_any_fixed_radius_sets_the_price_of_forming_a_record_2026_09_26.py
```

- The runner gives `TOTAL: PASS=12 FAIL=0` in about 10 s.
- Mutation census 7/7: five mutations in families A–E, and two in F, each failing in its own family only.

## Review findings, imports, reachability

- **For a referee.** The cage's uniqueness certificate (the eigenvalue bound). The locality of `f` in T4.
- **Imports.** The discrete maximum principle; summation by parts with harmonic polynomials; the eigenvalue bound; exact rational linear algebra.
- **Trace.** `frontier_discovery`.
- **Remaining.** Window-confined sources that are not point-equivalent; crowds of records; the delayed law.

🤖 Generated with [Claude Code](https://claude.com/claude-code)
