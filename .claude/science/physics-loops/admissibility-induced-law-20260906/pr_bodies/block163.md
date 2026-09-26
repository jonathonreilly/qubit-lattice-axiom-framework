## Summary

This is programme T in time, the shift sector. It is the supervisor's own derivation and is unrefereed. It works within blocks 54, 62, 65, 136 and 138, all landed, and builds on block 158, which is pushed. Block 158 settled the walker's coupling for relabellings fixed in time. Here the relabellings vary in time. The coin, turning to keep the frame the lengths' own, then turns at a changing rate.

- **T1.** At first order the moved walker is off by exactly `¼σ·curl ξ̇`. So the walker needs `¼σ·curl N`, the spin part of block 138's symmetric momentum coupled to the shift. The landed momentum's spin term is forced, not chosen.
- **T2.** At order strain times relabelling, the coin's coupling to the frame's rotation rate relative to the shift's flow, `¼σ_c ε_cab (e(∂_t + L_N)E)_ab`, restores consistency on all basis pairs (29040 exact equations).
- **T3.** Over 636 couplings the rank is 635, and the kernel is the scalar expansion rate. That rate is odd under time reversal, so with time reversal the coupling is unique.
- **T4** (v2). The comparator's connection along the time direction of the time-gauge tetrad, computed from the 3+1 metric at a point, has the rotation part `antisym(e(∂_t − L_N)E)`. With the note's sign of `N` that is T2's coupling, so the coupling is the comparator's.

Spatial relabellings that vary in time are required under both readings of relabellings in time. The lapse sector is left open. Nothing is adopted and no gravitational claim is made.

## Files

- Note: `docs/ADMISSIBILITY_RULE_RELABELLINGS_THAT_VARY_IN_TIME_MAKE_THE_WALKERS_COIN_TURN_WITH_ITS_FRAME_THE_SPIN_COUPLES_TO_THE_SHIFTS_VORTICITY_AND_THE_FRAMES_ROTATION_RATE_BOUNDED_THEOREM_NOTE_2026-09-26.md`
- Runner: `scripts/admissibility_rule_relabellings_that_vary_in_time_make_the_walkers_coin_turn_with_its_frame_2026_09_26.py`, with its cache under `logs/runner-cache/`
- Pack: `GOAL_block163.md`, `RESULTS_block163.md`, `CLAIM_STATUS_CERTIFICATE_block163.md` and `CHECKER_block163_findings.md`, plus appends to `HANDOFF.md`, `TRACE_GATE.md`, `REVIEW_HISTORY.md`, `STATE.yaml`, `OPPORTUNITY_QUEUE.md` and `APPROACH_REGISTRY.md`

## Verification

```bash
PYTHONPATH=scripts python3 scripts/admissibility_rule_relabellings_that_vary_in_time_make_the_walkers_coin_turn_with_its_frame_2026_09_26.py
```

- The runner gives `TOTAL: PASS=12 FAIL=0` in about 45 s.
- Mutation census 7/7: five mutations in families A–E, and two in F, each failing in its own family only.

## Review findings, imports, reachability

- **For a referee.**
  - The moved walker's time-derivative term `i∂_t(UΦ)(UΦ)⁻¹`.
  - The shift's sign convention, which is declared in the note.
  - The claim that the kernel is the expansion rate.
- **Imports.** The product rule of the coin's matrices; derivatives along vector fields on half-densities; polarization; exact linear algebra. The spinor's connection along time and the symmetric momentum, as comparators.
- **Trace.** `frontier_discovery`.
- **Remaining.** The lapse sector (reading E); a background shift; second order in the strain; an other-family referee.

🤖 Generated with [Claude Code](https://claude.com/claude-code)
