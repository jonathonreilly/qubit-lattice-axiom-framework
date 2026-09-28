## Summary

Block 184 (pushed) found the one stretch rule that keeps the walker's books symmetric at every stretch, assuming block 182's covariance. This note removes that premise. It asks: does a uniform stretch slow every wave exactly as it would slow a free particle with fixed momentum per label, `d log E/d log ℓ = −|u|²`? The setting is block 69's coupling and block 139's staggered mass (both landed), for walks `Σ_a F(k_a; ℓ)X_a + μΓ`.

- **T1.** Every wave obeys `d log E/d log ℓ = −ℓ²|v|²` at every stretch iff `∂F/∂(ℓ²) = −½F(∂_kF)²` and the mass is unchanged. The proof separates variables through the species point `k = 0`.
- **T2.** That rule, from `F = sin k`, is block 184's family. Its long-wave speed is `1/ℓ`, as the law's own normalisation requires.
- **T3.** Equivalently, the walk's response to a further stretch of each axis is minus half its own symmetric stress, as a matrix.
- **T4.** The frame `H/ℓ` slows every wave alike (`−1`). Block 69's linear completion and the fixed-generator flow meet the law at `ℓ = 1` (block 180) and violate it at `ℓ ≠ 1`.
- **T5.** Under the rule, rest waves keep `E = μ`, and each wave presses between `0` and `E/(3V)`.
- **T6.** The law's velocity matters. Read with the Clifford vector `F` as the momentum (velocity `F/E`), the same law holds iff `F = sin k/ℓ`, the frame. So the plain question must name the group velocity.

**For the owner's third column (the coupling axis).** The choice becomes one plain question: does stretching slow every wave as it slows a free particle? If yes, the rule is block 184's.

The supervisor's own derivation, unrefereed. Nothing is adopted and no gravitational claim is made.

## Files

- Note: `docs/ADMISSIBILITY_RULE_A_UNIFORM_STRETCH_SLOWS_EVERY_WAVE_AS_IT_SLOWS_A_FREE_PARTICLE_ONLY_UNDER_BLOCK_184S_STRETCH_RULE_BOUNDED_THEOREM_NOTE_2026-09-27.md`
- Runner: `scripts/admissibility_rule_a_uniform_stretch_slows_every_wave_as_a_free_particle_only_under_one_rule_2026_09_27.py`, with its cache under `logs/runner-cache/`
- Pack: `GOAL_block185.md`, `RESULTS_block185.md`, `CLAIM_STATUS_CERTIFICATE_block185.md` and `CHECKER_block185_findings.md`, plus the usual appends

## Verification

```bash
PYTHONPATH=scripts python3 scripts/admissibility_rule_a_uniform_stretch_slows_every_wave_as_a_free_particle_only_under_one_rule_2026_09_27.py
```

- The runner gives `TOTAL: PASS=16 FAIL=0` in about 5 s.
- Mutation census 8/8: six in families A–F and two in G, each failing in its own family only.

## Review findings, imports, reachability

- **Imports.** Separation of variables; characteristics (as in block 184); anticommuting involutions; exact arithmetic.
- **Trace.** `frontier_discovery`.
- **Remaining.**
  - An other-family referee.
  - Off-diagonal strains.
  - Walks that are not per-axis.
- **Review.** A same-family adversarial reviewer (Claude Fable 5.1, not a referee) found no mathematical error. Its corrections are in the second version.

🤖 Generated with [Claude Code](https://claude.com/claude-code)
