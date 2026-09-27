## Summary

Block 185 (pushed) showed that a diagonal stretch slows every wave as it slows a free particle only under block 184's rule. Shears were left open, since the walk is no longer a sum over axes there. This note asks every wave to obey the free particle's law for any uniform metric `g`, `∂E/∂g_ab = −½E v^a v^b`. It works with the energies, within block 69's coupling and block 139's staggered mass (both landed).

- **T1.** For `W = E²` the law is `∂W/∂g_ab = −¼W_aW_b`: six first-order flows whose Hamiltonians depend only on the slope, so they commute. The law is consistent.
- **T2.** From `W₀ = Σ sin² k + μ²` the unique solution is `k = k₀ + ½(g − 1)∇W₀(k₀)`, `E² = W₀ + ¼∇W₀·(g − 1)·∇W₀`. This is checked for a general symmetric `3 × 3` metric.
- **T3.** On diagonal metrics it is block 184's rule, and at the species points `E = μ` in every metric.
- **T4.** In every metric of the smooth set no wave is faster than one in lengths: `1 − v·g·v = (4W₀ − |∇W₀|²)/(4W) ≥ 0`.
- **T5.** The family is smooth exactly while every eigenvalue of `g` lies in `(0, 2)`. At an eigenvalue 2 the band top folds, and at 0 a species point folds. A pure shear is smooth iff `|ε| < 1`.
- **T6.** A walk realises the spectrum: `F = (1 + CGC)^{1/2} sin k₀` at `k₀(k)`, with `C = diag(cos k₀)`. It has `|F|² + μ² = E²`, is real-analytic in the smooth set, and is block 184's walk on the diagonal. It is not unique, since any rotation of `F` works; block 188 shows the stress response does not pick one beyond first order.

**For the owner's third column (the coupling axis).** Block 185's plain question, "must a stretch slow every wave as it slows a free particle?", now covers every uniform metric. A yes fixes the energies in all of them.

The supervisor's own derivation, unrefereed. Nothing is adopted and no gravitational claim is made.

## Files

- Note: `docs/ADMISSIBILITY_RULE_THE_FREE_PARTICLE_LAW_FOR_EVERY_UNIFORM_METRIC_SHEARS_INCLUDED_FIXES_ONE_SPECTRUM_SMOOTH_WHILE_THE_METRICS_EIGENVALUES_LIE_BETWEEN_ZERO_AND_TWO_BOUNDED_THEOREM_NOTE_2026-09-27.md`
- Runner: `scripts/admissibility_rule_the_free_particle_law_for_every_uniform_metric_2026_09_27.py`, with its cache under `logs/runner-cache/`
- Pack: `GOAL_block187.md`, `RESULTS_block187.md`, `CLAIM_STATUS_CERTIFICATE_block187.md` and `CHECKER_block187_findings.md`, plus the usual appends

## Verification

```bash
PYTHONPATH=scripts python3 scripts/admissibility_rule_the_free_particle_law_for_every_uniform_metric_2026_09_27.py
```

- The runner gives `TOTAL: PASS=15 FAIL=0` in about 4 s.
- Mutation census 9/9: seven in families A–F and I, and two in G, each failing in its own family only.

## Review findings, imports, reachability

- **Imports.** Commuting first-order flows and their characteristics; the operator norm; coverings of the torus; exact arithmetic.
- **Trace.** `frontier_discovery`.
- **Remaining.**
  - An other-family referee.
  - Which walk realises the spectrum off the diagonal (T6 gives one; it is not unique).
  - Non-uniform metrics.
- **Review.** A same-family adversarial reviewer (Claude Fable 5.1, not a referee) found no mathematical error. Its corrections are in the second version.

🤖 Generated with [Claude Code](https://claude.com/claude-code)
