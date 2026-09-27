## Summary

Block 147 (landed) worked the zero-of-energy row: a closed lattice that sees the filled sea bounces at `ℓ = I/m₀` for every positive source, or cannot move. It used the frame `H/ℓ`, so the sea's energy per site was `−I/ℓ`, which diverges as the lattice shrinks. Block 120 (landed) excluded the frame as a source for non-uniform modes. This note redoes block 147 within its own homogeneous model, with the walk stretched by the free-particle rule of blocks 184 and 185 (pushed).

- **T1.** Every wave's energy is nonincreasing in `ℓ`, strictly where it moves, and at most `√(3 + μ²)`. So the sea's energy per site is nondecreasing and bounded, with no divergence as the lattice shrinks.
- **T2.** On block 147's side-4 torus every label is a fixed point of the rule. The walk does not change, and `m_sea = −(3 + 3√2 + √3)/8` at every length. The frame's turn does not occur: with `m₀ > I` the lattice moves at every length, and with `m₀ < I` at none.
- **T3.** On side 6 at `ℓ = 1`, every moving wave has `|v|² = 1/4`, and the sea's pressure ratio is `1/12`.
- **T4.** A turn needs `m₀ < −m_sea(0⁺)`, a finite value in `[I, √(3 + μ²)]` (necessary, not sufficient). Otherwise a contracting branch reaches `ℓ → 0` in finite time. An expanding branch with a positive source reaches the rule's end at `√2` in finite time.

**For the owner's third column (the zero-of-energy row).** Under the member's own coupling, completed by the free-particle rule, the bounce is no longer automatic: it needs a small enough source.

The supervisor's own derivation, unrefereed. Nothing is adopted and no gravitational claim is made.

## Files

- Note: `docs/ADMISSIBILITY_RULE_UNDER_THE_FREE_PARTICLE_STRETCH_RULE_THE_SEAS_ENERGY_STAYS_BOUNDED_AND_A_CLOSED_LATTICE_THAT_SEES_IT_NEED_NOT_BOUNCE_BOUNDED_THEOREM_NOTE_2026-09-27.md`
- Runner: `scripts/admissibility_rule_under_the_free_particle_stretch_rule_the_seas_energy_stays_bounded_2026_09_27.py`, with its cache under `logs/runner-cache/`
- Pack: `GOAL_block186.md`, `RESULTS_block186.md`, `CLAIM_STATUS_CERTIFICATE_block186.md` and `CHECKER_block186_findings.md`, plus the usual appends

## Verification

```bash
PYTHONPATH=scripts python3 scripts/admissibility_rule_under_the_free_particle_stretch_rule_the_seas_energy_stays_bounded_2026_09_27.py
```

- The runner gives `TOTAL: PASS=14 FAIL=0` in about 3 s.
- Mutation census 7/7: five in families A–E and two in G, each failing in its own family only.

## Review findings, imports, reachability

- **Imports.** Monotone bounded limits; integration of a first-order length equation; exact arithmetic.
- **Trace.** `frontier_discovery`.
- **Remaining.**
  - An other-family referee.
  - `m_sea(ℓ)` on larger tori away from `ℓ = 1`.
  - Adiabatic following of the sea.
  - Behaviour at `ℓ = √2`.
- **Review.** A same-family adversarial reviewer (Claude Fable 5.1, not a referee) found no mathematical error. Its corrections are in the second version.

🤖 Generated with [Claude Code](https://claude.com/claude-code)
