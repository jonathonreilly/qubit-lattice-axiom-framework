## Summary

This harvests probe #9299 (a Claude Opus 5.5 worker, the supervisor's own model family). An other-family referee confirmed it in #9332 (`grok-4.6`). The note works within block 62's framed walk and member (and block 139's staggered mass for T4), with the sea's energy counted: this is block 147's reading, in which the member sees the half-filled sea.

- **T1.** The sea's static second-order response to a frame wave is `E2(q) = −⟨F(k, q)⟩`, with `0 ≤ F ≤ ‖ε‖_F²(a + b)/4`. So it tends to half the uniform response as `q → 0`, uniformly in the strain.
- **T2.** The uniform response `−⟨|s × εs|²/(2|s|³)⟩` is negative for every non-scalar strain, and negative definite on traceless strains.
- **T3.** On transverse traceless waves, `R₁ = 0` and the member costs `K w̄ (p²/4) tr(h²)`. So member plus sea lowers its static second-order energy under every long enough such wave, at every `K > 0`.
- **T4** (v2; the supervisor's extension, unrefereed). With block 139's staggered mass `μ > 0` the result is the same.
  - The mass anticommutes with every framed walk, so the sea is gapped by `2μ`.
  - The massive uniform form `−⟨(|s × εs|² + μ²|εs|²)/(2R³)⟩` is negative for every nonzero strain.

This answers block 155's open case of long waves (#9289). The `q²` part of the sea's response stays open; the probe has it in floating point only. Under block 147's other reading, nothing is driven.

Nothing is adopted and no gravitational claim is made.

## Files

- Note: `docs/ADMISSIBILITY_RULE_THE_SEAS_RESPONSE_TO_A_LONG_SHEAR_WAVE_IS_HALF_ITS_UNIFORM_RESPONSE_AND_MEMBER_PLUS_SEA_LOWERS_ITS_ENERGY_UNDER_LONG_ENOUGH_SHEARS_AT_EVERY_K_BOUNDED_THEOREM_NOTE_2026-09-26.md`
- Runner: `scripts/admissibility_rule_the_seas_response_to_a_long_shear_wave_is_half_its_uniform_response_2026_09_26.py`, with its cache under `logs/runner-cache/`
- Pack: `GOAL_block167.md`, `RESULTS_block167.md`, `CLAIM_STATUS_CERTIFICATE_block167.md` and `CHECKER_block167_findings.md`, plus the usual appends

## Verification

```bash
PYTHONPATH=scripts python3 scripts/admissibility_rule_the_seas_response_to_a_long_shear_wave_is_half_its_uniform_response_2026_09_26.py
```

- The runner gives `TOTAL: PASS=21 FAIL=0` in a few seconds.
- Mutation census 7/7: five in families A–E and two in F, each failing in its own family only.

## Review findings, imports, reachability

- **Imports.** Second-order perturbation theory for a Slater determinant; Lagrange's identity; Lebesgue's dominated limit theorem; exact arithmetic.
- **Trace.** `frontier_discovery`.
- **Remaining.** The `q²` part exactly; an other-family check of T4; the sea under one record per site.

🤖 Generated with [Claude Code](https://claude.com/claude-code)
