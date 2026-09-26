# Block 167 — results (2026-09-26; v2 adds T4)

- **Runner.** `scripts/admissibility_rule_the_seas_response_to_a_long_shear_wave_is_half_its_uniform_response_2026_09_26.py`: `TOTAL: PASS=21 FAIL=0` in a few seconds. Seven mutations (five in families A–E, two in F), each failing in its own family only.
- **T1.** `E2(q) = −⟨F(k, q)⟩` with `0 ≤ F ≤ ‖ε‖_F²(a + b)/4`, so `E2(q)` tends to `½E_unif(ε)`, uniformly in `ε`.
- **T2.** `E_unif(ε) = −⟨|s × εs|²/(2|s|³)⟩ < 0` for every non-scalar symmetric `ε`, and it is negative definite on traceless strains.
- **T3.** On transverse traceless waves `R₁ = 0` and the member's energy is `K w̄ (p²/4) tr(h²)`. Member plus sea lowers its static energy under every long enough such wave, at every `K > 0`.
- **T4** (v2; the supervisor's, unrefereed). With block 139's staggered mass, the sea is gapped by `2μ` for every frame. Its massive uniform form `−⟨(|s × εs|² + μ²|εs|²)/(2R³)⟩` is negative for every nonzero strain, so the conclusion holds for the massive sea too.
