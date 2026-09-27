## Summary

Block 185 (pushed) showed that on diagonal stretches the walk answers a further stretch with minus half its own symmetric stress, exactly under block 184's rule. Block 187 (pushed) fixed the energies for every uniform metric, shears included. This note asks whether the walk itself, as a matrix, can answer shears the same way. It works within block 69's coupling and block 139's staggered mass (both landed).

- **T1.** Every Clifford walk, `Σ_a F_a(k)X_a + μΓ` with hops of any form, satisfies the two book identities (hermitian densities need a pair-symmetric decomposition, exhibited for per-axis hops). Block 181's construction works with any divided-difference decomposition, because the square is a number. The single-wave stress is `¼(∂_ah ∂_bW + ∂_bh ∂_aW)`.
- **T2.** The stress-response principle, `∂h/∂g_ab = −½K^s_ab`, is block 69's coupling with `B = −(g − 1)/2` at first order, for all six components.
- **T3.** The `(11)` and `(12)` flows do not commute at second order. Their mismatch, `¼ cos k₁ cos k₂ cos 2k₁ (sin k₂, −sin k₁, 0)`, is orthogonal to the walk's Clifford vector: a rotation at fixed energy. The `(11)` and `(22)` flows commute.
- **T4.** No constant-coefficient placement of the metric's indices removes the mismatch. This is checked at 64 exact rational points.

- **T5.** A metric-independent rotation term is singular at `k₁ = 0`. A metric-dependent one, `−¼G₁₁ cos k₁ cos k₂ cos 2k₁ e₃ × F`, is local and cancels the `(11)/(12)` clash at second order. So the no-go is for the plain principle. Rotation terms restoring compatibility always exist.
- **T6.** At second order, of the fifteen pairs of responses, the six sharing no index commute. Each of the nine sharing one clashes by a rotation about a coordinate axis through `¼` times a product of cosines, one doubled. Those are local, so metric-dependent local rotations repair every clash at second order. The angles tend to `±¼` at long wavelength, so the clash is not a lattice effect. Higher orders are open.

**For the owner's third column (the coupling axis).** "Symmetric books" alone constrains nothing. The energies for every uniform metric are fixed (187), but the walk off the diagonal is not fixed by the stress response beyond first order; it needs a further supplied rule.

The supervisor's own derivation, unrefereed. Nothing is adopted and no gravitational claim is made.

## Files

- Note: `docs/ADMISSIBILITY_RULE_FOR_SHEARS_NO_WALK_ANSWERS_EVERY_UNIFORM_METRIC_WITH_MINUS_HALF_ITS_STRESS_BEYOND_FIRST_ORDER_THE_FLOWS_FAIL_TO_COMMUTE_BY_A_ROTATION_BOUNDED_THEOREM_NOTE_2026-09-27.md`
- Runner: `scripts/admissibility_rule_for_shears_no_walk_answers_every_uniform_metric_with_minus_half_its_stress_2026_09_27.py`, with its cache under `logs/runner-cache/`
- Pack: `GOAL_block188.md`, `RESULTS_block188.md`, `CLAIM_STATUS_CERTIFICATE_block188.md` and `CHECKER_block188_findings.md`, plus the usual appends

## Verification

```bash
PYTHONPATH=scripts python3 scripts/admissibility_rule_for_shears_no_walk_answers_every_uniform_metric_with_minus_half_its_stress_2026_09_27.py
```

- The runner gives `TOTAL: PASS=18 FAIL=0` in about 6 s.
- Mutation census 9/9: seven in families A–F and J, and two in G, each failing in its own family only.

## Review findings, imports, reachability

- **Imports.** Integrability of commuting flows; Hadamard's lemma; anticommuting involutions; exact arithmetic.
- **Trace.** `frontier_discovery`.
- **Remaining.**
  - An other-family referee.
  - A principle with a rotation term.
  - Higher orders.
- **Review.** A same-family adversarial reviewer (Claude Fable 5.1, not a referee) found no mathematical error. Its corrections are in the second version.

🤖 Generated with [Claude Code](https://claude.com/claude-code)
