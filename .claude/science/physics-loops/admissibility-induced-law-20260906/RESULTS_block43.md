# Block 43 — results (2026-09-20)

- Runner `scripts/admissibility_rule_record_layer_fields_arrive_by_diffusion_establishment_time_square_of_the_range_2026_09_20.py`: `TOTAL: PASS=13 FAIL=0`; eight mutations, each in its own family.
- T1: a wave is multiplied by `1 − hE(k)` per tick (sides 4, 6; `h = 1/6, 1/12`); `E_min ≤ (2π/L)²`; at least half the slowest mode's deviation remains for `n ≤ 1/(2hE_min)`, hence for `n ≤ L²/(8π²h)`.
- T2: exact path counts for 0–12 ticks: weight 1, nothing beyond `s` steps, mean-square reach exactly `s`; tail share beyond `R` at most `s/R²`; response to a switched-on source = sum of the kernels.
- T3: exact differentiation of block 42's odds map: a unit lean at a neighbour induces the lean `1/6` at (3,1,2) and `3/23` at (5,2,4): the linearized iteration is `6λ₁` times the simple walk.
- T4: with a mass term a mode with `E(k) ≤ m²` keeps half its deviation for `n ≤ 1/(4hm²)`.
- Corollary: `a ≥ R²/(2cT)`; comparators only: `0.09 mm` for the Earth–Sun distance and the age of the universe.
