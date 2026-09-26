## Summary

This is programme T's lapse sector. It is the supervisor's own derivation and is unrefereed. It works within blocks 62, 101, 136 and 150, all landed, and builds on blocks 158 and 163, which are pushed. The question: relabellings in time whose clock profile varies in space, which only reading E requires. Do they need anything more of the walker's coupling?

- **T1.** A relabelling in time with profile `ξ⁰` moves the walker by its own smeared generator `exp(−iu·½{ξ⁰, H_s})`: the time shift together with the coin's boost, which is unitary. At first order the moved walker is exactly the walker with the new shift `u∇ξ⁰`.
- **T2.** At order strain times relabelling, on all 600 basis pairs:
  - the principal part carries the metric-raised gradient `g^{jk}∂_jξ⁰`, as the member's shift law says;
  - the remainder is exactly block 163's frame-rotation coupling of that shift.

  So no new term is needed.
- **T3.** Without block 163's coupling, 18 pairs fail. Two different relabellings demand the same coupling. Block 158's `(1/8)ε·C` does not enter at this order.

With blocks 158 and 163: at leading order in the spacing, the walker's coupling keeps every relabelling of both readings through first order in the strain. Nothing is adopted and no gravitational claim is made.

## Files

- Note: `docs/ADMISSIBILITY_RULE_RELABELLINGS_IN_TIME_WHOSE_CLOCK_PROFILE_VARIES_IN_SPACE_NEED_NO_NEW_TERM_THE_WALKERS_OWN_GENERATOR_MOVES_IT_AS_THE_MEMBERS_SHIFT_CHANGES_BOUNDED_THEOREM_NOTE_2026-09-26.md`
- Runner: `scripts/admissibility_rule_relabellings_in_time_whose_clock_profile_varies_in_space_need_no_new_term_2026_09_26.py`, with its cache under `logs/runner-cache/`
- Pack: `GOAL_block164.md`, `RESULTS_block164.md`, `CLAIM_STATUS_CERTIFICATE_block164.md` and `CHECKER_block164_findings.md`, plus appends to `HANDOFF.md`, `TRACE_GATE.md`, `REVIEW_HISTORY.md`, `STATE.yaml`, `OPPORTUNITY_QUEUE.md` and `APPROACH_REGISTRY.md`

## Verification

```bash
PYTHONPATH=scripts python3 scripts/admissibility_rule_relabellings_in_time_whose_clock_profile_varies_in_space_need_no_new_term_2026_09_26.py
```

- The runner gives `TOTAL: PASS=12 FAIL=0` in about 6 s.
- Mutation census 7/7: five mutations in families A–D, and two in F, each failing in its own family only.

## Review findings, imports, reachability

- **For a referee.** The premise that a relabelling in time acts as the smeared generator. The identity `[½{ξ⁰, H}, H] = ½[ξ⁰, H²]`. The sign convention of the shift.
- **Imports.** Commutators of differential operators; the product rule of the coin's matrices; polarization; exact arithmetic. The comparator's constraint algebra, as a comparator.
- **Trace.** `frontier_discovery`.
- **Remaining.** A background lapse and shift; second order in the strain; the lattice; an other-family referee.

🤖 Generated with [Claude Code](https://claude.com/claude-code)
