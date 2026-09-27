## Summary

Block 69 (landed) leaves the finite-stretch completion of its two-step coupling open. Block 176 (pushed) wrote every reach-three completion at uniform stretch as `ℓF = sin k (1 − q sin² k)`, admissible iff `q ≥ −1/6`. This note tests the natural principle, covariance: each further stretch acts on the stretched walk as a relabelling, `∂_bF = p ∂_kF`.

- **T1.** Within reach three, covariance forces `F = sin k (1 + β cos² k)`, so `q = 1 − ℓ`, block 69's linear completion. This is proved by induction and checked to order five with every generator coefficient free.
- **T2.** That completion is covariant, with generator `β′ sin k cos k/(1 + β − 3β sin² k)`.
- **T3.** Counted in lattice labels, it outruns `w/ℓ` beyond `ℓ = 7/6`.
- **T4.** The fixed-generator flow and the self-consistent flow are covariant and have reach-five terms at second order. The first outruns `w/ℓ` once `ℓ² > 3/2`.
- **T5.** For `ℓ > 2/3` the linear completion is the free walk relabelled: `F = g_ℓ(sin k)` with `g_ℓ` monotone.
- **T6.** Its generator is not parallel to the stretched walk's velocity, so its current twists at every `ℓ ≠ 1`. The momentum that keeps symmetric books generates the self-consistent flow, which leaves reach three. Of reach three, covariance and symmetric books at finite stretch, at most two hold.

**For the owner's third column** (item 5). The completion is a supplied choice among the trilemma's pairs, each with a worked cost. On a closed lattice a uniform stretch is a hopping law, not a relabelling, and block 176's speed limit applies.

The supervisor's own derivation, unrefereed. T5, T6 and the label-unit caveat came from a same-family panel lens and were checked exactly. Nothing is adopted and no gravitational claim is made.

## Files

- Note: `docs/ADMISSIBILITY_RULE_THE_ONLY_REACH_THREE_COMPLETION_THAT_KEEPS_EACH_FURTHER_STRETCH_A_RELABELLING_IS_BLOCK_69S_LINEAR_ONE_AND_IT_FAILS_BEYOND_SEVEN_SIXTHS_BOUNDED_THEOREM_NOTE_2026-09-27.md`
- Runner: `scripts/admissibility_rule_the_only_covariant_reach_three_completion_2026_09_27.py`, with its cache under `logs/runner-cache/`
- Pack: `GOAL_block182.md`, `RESULTS_block182.md`, `CLAIM_STATUS_CERTIFICATE_block182.md` and `CHECKER_block182_findings.md`, plus the usual appends

## Verification

```bash
PYTHONPATH=scripts python3 scripts/admissibility_rule_the_only_covariant_reach_three_completion_2026_09_27.py
```

- The runner gives `TOTAL: PASS=15 FAIL=0` in about 3 s.
- Mutation census 7/7: five in families A–E and two in F, each failing in its own family only.

## Review findings, imports, reachability

- **Imports.** Formal power series; trigonometric polynomials; integration along a vector field; exact arithmetic.
- **Trace.** `frontier_discovery`.
- **Remaining.**
  - An other-family referee.
  - Anisotropic stretches.
  - Admissible covariant completions outside reach three.

🤖 Generated with [Claude Code](https://claude.com/claude-code)
