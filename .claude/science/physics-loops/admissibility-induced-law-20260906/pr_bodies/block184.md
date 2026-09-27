## Summary

Block 182 (pushed) found a trilemma for how the walk responds to a uniform stretch: reach three, covariance (each further stretch a relabelling) and symmetric books at finite stretch cannot all hold. It left open whether any covariant completion outside reach three is admissible at every stretch. This note takes the pair "covariance with symmetric books", within block 69's two-step coupling (landed), for a uniform isotropic stretch.

- **T1.** On every single wave and at every stretch, the momentum that generates further stretch is parallel to the velocity iff the generator is `γ(b)F∂_kF`. So `u = F²` obeys `∂_τu = (∂_ku)²/2`: one family, block 182's self-consistent flow, up to reparametrisation. The fixed-generator flow and the linear completion fail this at every `ℓ ≠ 1`.
- **T2.** Measured by the long-wave speed `∂_kF(0) = 1/ℓ`, the family is `k = k₀ + ((ℓ² − 1)/2) sin 2k₀` and `F = sin k₀ (sin² k₀ + ℓ² cos² k₀)^{1/2}`. Its second order is block 182 T4(b)'s, and it keeps the species corners.
- **T3.** For `0 < ℓ² < 2` it is a real-analytic relabelling of the free walk. Every wave with `E ≠ 0` is strictly slower than `1/ℓ` per label, per axis and in three dimensions; the bound is approached at the species points. The linear completion fails this beyond `7/6`, and the fixed-generator flow beyond `ℓ² = 3/2`.
- **T4.** The band-top curvature is `−1/(2 − ℓ²)`, so no family continuous in `ℓ` and twice differentiable in `k` reaches `ℓ = √2`. There the band top keeps zero slope but has infinite curvature, `1 − F ∝ |k − π/2|^{4/3}`.
- **T5.** At every `ℓ ≠ 1` the walk has infinite reach, since `∂_k²u` along characteristics has a pole off the real line. Its hops decay exponentially.
- **T6.** On a single wave the energy current is `F_a∂F_a`. Supplying block 181 T1's identification at every stretch (the energy current equals the momentum per unit strain) normalises the strain variable: `γ ≡ 1`, `b = (1 − ℓ²)/2`. The long-wave metric `ℓ² = 1 − 2b` is then exactly linear in it, while block 69 T4's `(1 + b)²` agrees only to first order.
- **T7.** Block 181's pair-level construction, built from divided differences of the hops, works for every walk `Σ_a F_a(k_a)X_a + μΓ` whose square is a number, with real per-axis hops. So every per-axis completion keeps its own exact books on pairs of waves. This family's stretch generator equals `P^s` on single waves; for the other completions it does not, and that is block 182 T6's twist. Placing the stretch generator as `P^s` on pairs of waves is open.
- **T8.** At fixed label momentum (sites held physical), `d log E/d log ℓ = −ℓ²|v|² = −|u|²` for every wave, the law of a relativistic free particle with fixed momentum per label, where `u = ℓv` is the velocity in lengths. So content presses with its kinetic pressure `Σ E|u|²/(3V)` at every stretch. Block 180's first-order result is the `ℓ = 1` case.

**For the owner's third column (the coupling axis).** "Covariance with symmetric books" fixes the stretch rule. It is admissible up to `√2`, but has hops of every length at any finite stretch, and has no smooth walk at `√2` or beyond. The same books fix the coupling's strain variable: the walk couples exactly linearly to `ℓ²`.

The supervisor's own derivation, unrefereed. Nothing is adopted and no gravitational claim is made.

## Files

- Note: `docs/ADMISSIBILITY_RULE_SYMMETRIC_BOOKS_AT_EVERY_STRETCH_FIX_ONE_STRETCH_RULE_IT_NEVER_OUTRUNS_THE_LONG_WAVES_AND_ENDS_AT_A_STRETCH_OF_ROOT_TWO_BOUNDED_THEOREM_NOTE_2026-09-27.md`
- Runner: `scripts/admissibility_rule_symmetric_books_at_every_stretch_fix_one_stretch_rule_2026_09_27.py`, with its cache under `logs/runner-cache/`
- Pack: `GOAL_block184.md`, `RESULTS_block184.md`, `CLAIM_STATUS_CERTIFICATE_block184.md` and `CHECKER_block184_findings.md`, plus the usual appends

## Verification

```bash
PYTHONPATH=scripts python3 scripts/admissibility_rule_symmetric_books_at_every_stretch_fix_one_stretch_rule_2026_09_27.py
```

- The runner gives `TOTAL: PASS=28 FAIL=0` in about 12 s.
- Mutation census 9/9: seven in families A–F and I, and two in G, each failing in its own family only.

## Review findings, imports, reachability

- **Imports.** Characteristics of a first-order equation; the inverse function, intermediate value and identity theorems; exponential decay of the hops of a function analytic on a strip; divided differences and anticommuting involutions; exact arithmetic.
- **Trace.** `frontier_discovery`.
- **Remaining.**
  - An other-family referee.
  - Anisotropic stretches.
  - Placing the stretch generator itself as `P^s` on pairs of waves; T6 matches them on single waves.
- **Review.** A same-family adversarial reviewer (Claude Fable 5.1, not a referee) found no mathematical error. Its scope corrections are in the third version.

🤖 Generated with [Claude Code](https://claude.com/claude-code)
