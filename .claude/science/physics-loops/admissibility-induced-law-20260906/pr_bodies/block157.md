## Summary

This harvests probe #9283 (a Claude Opus 5.5 worker, the supervisor's own model family; unrefereed) and adds the supervisor's variants, run on its machinery. It works within blocks 62, 101, 124, 136, 144 and 150, all landed. It answers programme A1 (decision-record addendum 40) at leading order in the spacing: which cubic terms can the member have?

The question is the first-order consistency condition `δ₀V₃ + δ₁S₂ = 0`, over local cubic two-derivative T-even vertices, counted modulo field redefinitions.
- **T1.** With all fields and both relabellings there is exactly one class, the comparator's.
- **T2.** Restricted to the scalar sector there are four classes, so the scalar-sector test pre-registered in addendum 40 was not selective.
- **T3.** With relabellings in time required only for uniform clock profiles there is still one class, the comparator's. With no relabellings in time there are five.

So the reading that keeps free walkers exactly consistent (addendum 44) also forces the comparator's cubic vertex at leading order. Nothing is adopted and no gravitational claim is made.

## Files

- Note: `docs/ADMISSIBILITY_RULE_AT_LEADING_ORDER_THE_MEMBERS_CUBIC_COMPLETION_IS_UNIQUE_AND_THE_COMPARATORS_WITH_ALL_FIELDS_EVEN_WITH_ONLY_UNIFORM_RELABELLINGS_IN_TIME_BOUNDED_THEOREM_NOTE_2026-09-26.md`
- Runner: `scripts/admissibility_rule_at_leading_order_the_members_cubic_completion_is_unique_and_the_comparators_with_all_fields_even_with_only_uniform_relabellings_in_time_2026_09_26.py`, with its cache under `logs/runner-cache/`
- Pack: `GOAL_block157.md`, `RESULTS_block157.md`, `CLAIM_STATUS_CERTIFICATE_block157.md` and `CHECKER_block157_findings.md`, plus appends to `HANDOFF.md`, `TRACE_GATE.md`, `REVIEW_HISTORY.md`, `STATE.yaml`, `OPPORTUNITY_QUEUE.md` and `APPROACH_REGISTRY.md`

## Verification

```bash
PYTHONPATH=scripts python3 scripts/admissibility_rule_at_leading_order_the_members_cubic_completion_is_unique_and_the_comparators_with_all_fields_even_with_only_uniform_relabellings_in_time_2026_09_26.py
```

- The runner gives `TOTAL: PASS=15 FAIL=0` in about 2 minutes.
- Mutation census 6/6: four mutations in families A–D, and two in F, each failing in its own family.
- The probe's own checker was rerun without its longest part: 22/22 in 688 s.

## Review findings, imports, reachability

- **For a referee.** The grading argument, which lets only one-derivative deformations and zero-derivative redefinitions enter. How the uniform-profile reading is implemented: the time part of the condition at zero spatial momentum.
- **Imports.** Exact linear algebra over the rationals; the known uniqueness of the comparator's cubic vertex, as a comparator (T1 reproduces it).
- **Trace.** `frontier_discovery`. A1's pre-registered decision, read on the full sector, is "continue".
- **Remaining.** The exact lattice lift at range 1–2; the tie to the walker's coupling; an other-family referee.

🤖 Generated with [Claude Code](https://claude.com/claude-code)
