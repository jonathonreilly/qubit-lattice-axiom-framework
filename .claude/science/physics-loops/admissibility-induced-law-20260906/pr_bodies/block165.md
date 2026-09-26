## Summary

This harvests probe #9225 (a Claude Opus 5.5 worker, the supervisor's own model family). An other-family referee confirmed it in #9312 (a Grok worker). The note works within blocks 62, 101 and 124, all landed. Setting: block 62's cube kinetic family, with the frame's rotation rate included, at one wave vector and second order in the fields.

- **T1.**
  - The gradient relabelling in time is a symmetry iff `(M₁, M₂, M₃) = (0, c, −c)`, with the multiplier shifting by `(c/K)ζ''`.
  - The transverse one is a symmetry iff `(M, 2M, 0)`, `N = 0`, with no shift.
  - Both together allow only zero.
- **T2.** The frame's full rate has exactly four cube-invariant quadratic numbers. Blindness to coin rotations removes only the antisymmetric one, so block 124's count of two uses its stated metric premise. The landed note states that premise, so no correction is owed.
- **T3.** The survivor `(0, c, −c)` has one travelling transverse traceless pair, the gauge direction, drifting transverse relabellings, and a decoupled rotation block.

Nothing is adopted and no gravitational claim is made.

## Files

- Note: `docs/ADMISSIBILITY_RULE_IN_THE_CUBE_KINETIC_FAMILY_RELABELLINGS_IN_TIME_FIX_THE_KINETIC_SHAPE_AND_THE_FRAMES_FULL_RATE_HAS_FOUR_NUMBERS_OF_WHICH_BLINDNESS_REMOVES_ONE_BOUNDED_THEOREM_NOTE_2026-09-26.md`
- Runner: `scripts/admissibility_rule_in_the_cube_kinetic_family_relabellings_in_time_fix_the_kinetic_shape_2026_09_26.py`, with its cache under `logs/runner-cache/`
- Pack: `GOAL_block165.md`, `RESULTS_block165.md`, `CLAIM_STATUS_CERTIFICATE_block165.md` and `CHECKER_block165_findings.md`, plus the usual appends

## Verification

```bash
PYTHONPATH=scripts python3 scripts/admissibility_rule_in_the_cube_kinetic_family_relabellings_in_time_fix_the_kinetic_shape_2026_09_26.py
```

- The runner gives `TOTAL: PASS=11 FAIL=0` in about 13 s.
- Mutation census 6/6: four in families A–D and two in F, each failing in its own family only.

## Review findings, imports, reachability

- **Imports.** The variational derivative; invariant theory of the cube group; minors of a pencil; exact symbolic algebra.
- **Trace.** `frontier_discovery`.
- **Remaining.** Orders beyond the second; a field for the drifting transverse relabellings.

🤖 Generated with [Claude Code](https://claude.com/claude-code)
