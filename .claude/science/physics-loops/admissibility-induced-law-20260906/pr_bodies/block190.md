## Summary

> **Third version (2026-09-28).** A same-family referee (Claude Sonnet 5) confirmed it with wording corrections, now applied: the plain summary is narrowed to small uniform shears; hidden assumptions are declared; and positive definiteness on every volume-preserving direction follows by cubic symmetry. Runner `TOTAL: PASS=16 FAIL=0`.

The zero-of-energy row of the owner's third column asks whether the member sees the filled sea. Block 183 (pushed) found that, under the two-step coupling with block 176's reach-three completions, the seen sea gives way under a volume-preserving stretch. Blocks 184–187 (pushed) then found the free-particle stretch rule, which is not reach three. This note asks the shear question under that rule, within blocks 69 and 147 (landed).

- **T1.** For any per-axis completion with second-order term `s(½ + a s² + b s⁴)`, the sea's second-order energy is `−Σ_a λ_a²⟨s_a²(½ + a s_a² + b s_a⁴)/E⟩` plus an interband term (block 183 T2 is `b = 0`).
- **T2.** Block 184's rule has `a = −4` and `b = 7/2`.
- **T3.** For a volume-preserving diagonal stretch the sea's energy rises: exactly `0` on side 4, `4/27 + (34√3 + 65√6)/864` on side 6, and positive on side 8, including with block 139's staggered mass. The reach-three completions with `q₂ = −½` give negative values.
- **T4.** Through block 187's spectrum, the off-diagonal volume-preserving shear raises it too: `25/648 + (9√6 − 8√3)/1728` per `ε²` on side 6, and positive on side 8.
- **T5** (second version). On the infinite lattice, by exact outward-rounded interval sums, the diagonal value lies in `[1/16, 7/20]` and the off-diagonal value in `[1/40, 3/40]` per `ε²`. Both are positive, so block 191's gap holds on the infinite lattice.

**For the owner's third column (the zero-of-energy row).** Under the free-particle rule the seen sea resists shear, and the bounce needs a small source (186). Both worked dangers of a seen sea soften.

The supervisor's own derivation, unrefereed. Nothing is adopted and no gravitational claim is made.

## Files

- Note: `docs/ADMISSIBILITY_RULE_UNDER_THE_FREE_PARTICLE_STRETCH_RULE_THE_SEA_RESISTS_SHEAR_BOTH_SHEAR_CLASSES_RAISE_ITS_ENERGY_BOUNDED_THEOREM_NOTE_2026-09-28.md`
- Runner: `scripts/admissibility_rule_under_the_free_particle_stretch_rule_the_sea_resists_shear_2026_09_28.py`, with its cache under `logs/runner-cache/`
- Pack: `GOAL_block190.md`, `RESULTS_block190.md`, `CLAIM_STATUS_CERTIFICATE_block190.md` and `CHECKER_block190_findings.md`, plus the usual appends

## Verification

```bash
PYTHONPATH=scripts python3 scripts/admissibility_rule_under_the_free_particle_stretch_rule_the_sea_resists_shear_2026_09_28.py
```

- The runner gives `TOTAL: PASS=16 FAIL=0` (second version, about 10 s).
- Mutation census 8/8: six in families A–E and I, two in G, each failing in its own family only.

## Review findings, imports, reachability

- **Imports.** Norm expansion; the matrix exponential; exact radicals.
- **Trace.** `frontier_discovery`.
- **Remaining.**
  - An other-family referee.
  - Long shear waves.
  - The massive sea on the infinite lattice.

🤖 Generated with [Claude Code](https://claude.com/claude-code)
