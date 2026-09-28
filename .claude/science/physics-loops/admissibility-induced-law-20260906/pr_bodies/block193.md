## Summary

The coupling axis of the owner's third column asks how the walk responds when the lattice stretches with its sites held. A same-family panel (2026-09-28) proposed testing the owner's own reading, that records are the grain: a stretch with sites held would mean fewer records on the same sites. The panel pre-registered five outcomes: the frame class, the free-particle class, a relabelling, a speed-up, or neither.

This note computes the answer for an ordered pattern of sites with no record, under two supplied rules for the walker at such a site: R1 (no amplitude there) and R3 (hop to the next record).

- **T1.** The eight species' long waves are the taste cube `Σ_a q_a X_a ⊗ σ_a` on the parity classes. Under R1 a vacancy deletes its class's corner.
  - This holds at first order for any period lattice in `2Z³`, under the stated kernel condition.
  - For period 2 it is exact at every wave number, with `q_a = sin(Q_a/2)`.
- **T2.** For all 256 sets of deleted corners, along every axis each long-wave speed is exactly `1` or `0`.
  - All but 24 sets factor into subspace speeds of exactly one: a wave moves at full speed along a line, within a plane, or in all of space, or it is frozen.
  - The 24 form one class, a path turning through all three axes, which slows oblique waves only.
  - Everything is frozen first by the four classes of one sublattice.
- **T3.** In the checked period-4 cells the exact flat bands number twice the sublattice imbalance. With period 3, one vacancy per cell removes every species' zero-energy doublet.
- **T4.** R3 is a relabelling, so the long waves move at the mean spacing, above one.
- **T5.** Random missing records at first order in their density: one vacancy's T-matrix is local and coin-scalar, `−(E ḡ(E))⁻¹`, exact on the 4³ torus. The averaged energies depend only on the bare energy, their relative shift is not one number, and inside the band they are damped. A stretch does none of this.

**Outcome: neither.** Missing records do not act on the walk as a stretch under either rule, so the coupling-axis question stays the owner's, about the member's lengths as a supplied field.

The supervisor's own derivation, unrefereed. Nothing is adopted and no gravitational claim is made.

## Files

- Note: `docs/ADMISSIBILITY_RULE_A_CRYSTAL_OF_MISSING_RECORDS_DOES_NOT_STRETCH_THE_WALK_ALONG_EVERY_AXIS_A_LONG_WAVE_KEEPS_SPEED_ONE_OR_STOPS_BOUNDED_THEOREM_NOTE_2026-09-28.md`
- Runner: `scripts/admissibility_rule_a_crystal_of_missing_records_does_not_stretch_the_walk_2026_09_28.py`, with its cache under `logs/runner-cache/`
- Pack: `GOAL_block193.md`, `RESULTS_block193.md`, `CLAIM_STATUS_CERTIFICATE_block193.md` and `CHECKER_block193_findings.md`, plus the usual appends

## Verification

```bash
PYTHONPATH=scripts python3 scripts/admissibility_rule_a_crystal_of_missing_records_does_not_stretch_the_walk_2026_09_28.py
```

- The runner gives `TOTAL: PASS=25 FAIL=0` in about 16 s.
- Mutation census 9/9, each failing in its own family only.

## Review findings, imports, reachability

- **Imports.** The parity-class transform; degenerate first-order perturbation theory; the sublattice zero-mode count, used as a named comparator; the concentration expansion of the averaged resolvent; the coarea formula; the block-matrix inverse; exact linear algebra over the Gaussian rationals.
- **Trace.** `frontier_discovery`.
- **Remaining.**
  - An other-family referee.
  - Random patterns beyond first order in their density.
  - The member's coupling to a diluted walk.

🤖 Generated with [Claude Code](https://claude.com/claude-code)
