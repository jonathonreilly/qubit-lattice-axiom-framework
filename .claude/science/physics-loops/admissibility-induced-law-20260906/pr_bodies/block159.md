## Summary

This harvests probe #9202 (a Claude Opus 5.5 worker, the supervisor's own model family). An other-family referee confirmed it in #9294 (a Grok worker). The note works within blocks 55, 60 and 110, all landed. It asks whether rays singling out the curvature member is really a property of static bending.

Setting: block 60's weight-one static field energies of rates and lengths, at long wavelength, around a spherical body.

- **T1.** The comparator's second-order bend holds exactly on the plane `4A₁ − 2C₁ − 6D₁ = 3` of third-order jets (charges agreeing, `σ = 1`). The curvature member `(1, 1/2, 0)` is one point of that plane; constant coefficients give `5/2`. Each further order adds one linear condition on the next jet.
- **T2.** Bilinear members match the comparator's index at every order, capture included, iff `ℓf = ((1 + g)/2)³`. That gives one member for every `g`. Among power laws, only the curvature member matches.
- **T3.** The named clauses leave the jet free. Weight one, a variational ledger, the wall term `A(0)L₁`, and blindness to the coin's axes all do.
- **T4** (conditional on block 157, which is pushed and unrefereed). With the metric `e^{2λ}δ` and the lapse `e^u`, the comparator's static density is exactly the curvature member at every order. No zero-derivative redefinition keeps the member's transformation laws. So block 157's unique cubic completion lands on the jet `(1, 1/2, 0)`.

So static bending does not single out the curvature member, and relabelling consistency with all fields does. Nothing is adopted and no gravitational claim is made.

## Files

- Note: `docs/ADMISSIBILITY_RULE_STATIC_BENDING_DOES_NOT_SINGLE_OUT_THE_MEMBER_A_PLANE_OF_JETS_BENDS_LIKE_THE_COMPARATOR_AND_BILINEAR_MEMBERS_MATCH_ITS_INDEX_AT_EVERY_ORDER_BOUNDED_THEOREM_NOTE_2026-09-26.md`
- Runner: `scripts/admissibility_rule_static_bending_does_not_single_out_the_member_2026_09_26.py`, with its cache under `logs/runner-cache/`
- Pack: `GOAL_block159.md`, `RESULTS_block159.md`, `CLAIM_STATUS_CERTIFICATE_block159.md` and `CHECKER_block159_findings.md`, plus appends to `HANDOFF.md`, `TRACE_GATE.md`, `REVIEW_HISTORY.md`, `STATE.yaml`, `OPPORTUNITY_QUEUE.md` and `APPROACH_REGISTRY.md`

## Verification

```bash
PYTHONPATH=scripts python3 scripts/admissibility_rule_static_bending_does_not_single_out_the_member_2026_09_26.py
```

- The runner gives `TOTAL: PASS=16 FAIL=0` in about 20 s.
- Mutation census 7/7: five mutations in families A–E, and two in F, each failing in its own family only.

## Review findings, imports, reachability

- **For a referee.**
  - The long-wave reduction is assumed.
  - T4's use of block 157 is by exclusion: two vertices consistent with the same laws differ by a strictly invariant vertex, and block 157 T1 found no such class.
- **Imports.** Series solutions of radial equations; the ray invariant of a spherical index; the comparator's isotropic exterior index, as a comparator.
- **Trace.** `frontier_discovery`.
- **Remaining.** An other-family referee of block 157; the exact lattice exterior.

🤖 Generated with [Claude Code](https://claude.com/claude-code)
