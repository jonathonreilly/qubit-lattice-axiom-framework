# Block 48 — results (2026-09-21)

- Runner `scripts/admissibility_rule_free_capturing_bodies_are_carried_by_the_wind_capture_law_anisotropic_collisionless_shadow_dilution_law_of_motion_2026_09_21.py`: `TOTAL: PASS=20 FAIL=0`; eleven mutations, each in its own family.
- T1: `Σ_k max(0, s·e_k) = |s|₁` (174 rational unit contents), `1 ≤ |s|₁² ≤ 3`; witness: contents `(1,0,0)`, `(−3/5,−4/5,0)`: gas mean `(1/5,−2/5,0)`, captured mean `(1/15,−7/15,0)`.
- T2: `⟨|s|₁⟩ = 3/2`, `⟨|s|₁ s_i s_j⟩ = δ_ij/2`; face response `diag(1/16,1/16,1/8)`; cube `8,8,8`, ball of radius 3 `58,58,58`, plate `4,4,8` with response `5/4, 5/4, 3/2`.
- T3: multinomial deficit and its transport equation; shell sums 1; simplex integral `1/((n+1)(n+2))` at all 56 sites with `n ≤ 5`; multiplicities 1, 2, 4; coefficients `10201/7225, 121/49, 25/9, 361/121` against the collisional `9/4`; remainder `675/(n+4)` per component.
- T4: both capture channels bring `u`; content `(1 − f)p₀ + f u`.
- T5: early acceleration `3ρN₁/(16π(1−ρ)r²)`; `(q₁t)² = (π³/2)ρ(1−ρ)r³/N₁`; window: gas inside the radius against `8N₁/(3π²(1−ρ))`.
- Executed (300 seeds each): content over `u f`: `0.97 ± 0.03` (pinned, no scattering), `0.89 ± 0.03` (pinned, `γ = 1`), `0.78 ± 0.03` (free, `ρ = 0.3`), `0.87 ± 0.03` (free, `ρ = 0.1`). Free body released at separation 20 from a fixed capturing body (96 seeds): drift `3.74 ± 0.26` sites in 300 ticks, 84 % of seeds towards; content `0.79 ± 0.05` and drift `0.68 ± 0.05` of the closure along the measured path.
