## Summary

This harvests probe #9222 (a Claude Opus 5.5 worker, the supervisor's own model family), which recovered the owner-requested deferred finding U9-R2. An other-family referee confirmed it in #9337 (`grok-4.6`). The note works within blocks 88 and 89, both landed. Both left the anisotropy's equality case open.

- **T1.** In linear rates, the sea energy's cubic coefficient along the traceless path is `(3/2)⟨Σ_i u_i(u_j − u_k)²/|s|⁵⟩ > 0`, with `u_j = sin² k_j`.
- **T2.** In log rates it is `−⟨(s₁³ + 9s₁s₂/2 + 81s₃/2)/(3|s|⁵)⟩ < 0`.
- **T3.** The law's cost has no cubic part, and every derivative of `√Q` is homogeneous of degree one in `s`. So at each threshold the path energy is `e₃ε³ + O(ε⁴)` with `e₃ ≠ 0`, and the uniform rates are not a local minimum along the path. The special axis weakens in linear rates and strengthens in log rates.

Nothing is adopted and no gravitational claim is made.

## Files

- Note: `docs/ADMISSIBILITY_RULE_AT_THE_ANISOTROPY_THRESHOLDS_THE_UNIFORM_BOND_RATES_ARE_NOT_A_LOCAL_MINIMUM_BECAUSE_THE_SEA_HAS_A_CUBIC_TERM_OF_DEFINITE_SIGN_BOUNDED_THEOREM_NOTE_2026-09-27.md`
- Runner: `scripts/admissibility_rule_at_the_anisotropy_thresholds_the_uniform_bond_rates_are_not_a_local_minimum_2026_09_27.py`, with its cache under `logs/runner-cache/`
- Pack: `GOAL_block175.md`, `RESULTS_block175.md`, `CLAIM_STATUS_CERTIFICATE_block175.md` and `CHECKER_block175_findings.md`, plus the usual appends

## Verification

```bash
PYTHONPATH=scripts python3 scripts/admissibility_rule_at_the_anisotropy_thresholds_the_uniform_bond_rates_are_not_a_local_minimum_2026_09_27.py
```

- The runner gives `TOTAL: PASS=11 FAIL=0` in about 1 s.
- Mutation census 6/6: four in families A–D and two in F, each failing in its own family only.

## Review findings, imports, reachability

- **Imports.** Differentiation under an integral with a dominating function; symmetric functions; exact arithmetic.
- **Trace.** `frontier_discovery`.
- **Remaining.** The window above threshold; directions at intermediate wave numbers.

🤖 Generated with [Claude Code](https://claude.com/claude-code)
