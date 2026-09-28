## Summary

Block 188 (pushed) found that for slanted stretches (shears) the walk's response to the lattice's lengths is fixed only up to a rotation of its Clifford vector at fixed energy. A same-family panel disagreed about whether that rotation is physical. This note answers what it changes, within block 69's coupling (landed).

- **T1.** A wave-number-dependent coin rotation `U(k) = exp(−iθ(k) n·σ/2)` leaves every energy, every group velocity and every single-wave current unchanged.
- **T2.** For the same state carried by `U`, the density's pair symbol changes by `−(i/2) q·∇θ n·σ + O(q²)`. So it is unchanged at `q = 0`, and its first moment moves by the rotation's connection, `½∇θ` times the wave's polarisation.
- **T3.** Every angle in block 188 T6's table is `¼` times a product of cosines, per unit strain. Its gradient vanishes at all eight species points, and for `(11)/(12)` the Hessian at `k = 0` is `diag(5/4, 1/4, 0)`. The shift is proportional to the strain and vanishes at long wavelength.

**For the owner's third column (the coupling axis).** The frame-rotation choice is a lattice-scale choice, invisible to long waves. It is not a long-wavelength decision.

The supervisor's own derivation, unrefereed. Nothing is adopted and no gravitational claim is made.

## Files

- Note: `docs/ADMISSIBILITY_RULE_THE_FRAME_ROTATION_FOR_SHEARS_IS_SEEN_ONLY_AT_THE_LATTICE_SCALE_IT_MOVES_A_WAVES_DENSITY_BY_A_CONNECTION_THAT_VANISHES_AT_THE_SPECIES_POINTS_BOUNDED_THEOREM_NOTE_2026-09-28.md`
- Runner: `scripts/admissibility_rule_the_frame_rotation_for_shears_is_seen_only_at_the_lattice_scale_2026_09_28.py`, with its cache under `logs/runner-cache/`
- Pack: `GOAL_block192.md`, `RESULTS_block192.md`, `CLAIM_STATUS_CERTIFICATE_block192.md` and `CHECKER_block192_findings.md`, plus the usual appends

## Verification

```bash
PYTHONPATH=scripts python3 scripts/admissibility_rule_the_frame_rotation_for_shears_is_seen_only_at_the_lattice_scale_2026_09_28.py
```

- The runner gives `TOTAL: PASS=11 FAIL=0`.
- Mutation census 6/6: four in families A–D and two in G, each failing in its own family only.

## Review findings, imports, reachability

- **Imports.** Unitary conjugation; the connection of a wave-number-dependent basis; exact arithmetic.
- **Trace.** `frontier_discovery`.
- **Remaining.**
  - An other-family referee.
  - Higher orders.

🤖 Generated with [Claude Code](https://claude.com/claude-code)
