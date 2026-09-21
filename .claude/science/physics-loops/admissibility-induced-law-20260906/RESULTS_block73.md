# Block 73 — results (2026-09-21)

- Runner `scripts/admissibility_rule_the_two_step_momentum_is_the_only_one_2026_09_21.py`: `TOTAL: PASS=12 FAIL=0`; 7 mutations, each in its own family (~25 s).
- T1: `[a + b·σ, H] = 2i(b × s)·σ`; `b = cs` commutes; `b = (sin k_2, 0, 0)` does not.
- T2: 7 monomials of reach ≤ 1, 32 conditions: no solution; general `α`: species `n` sees `(1 + BαD)ᵀ(1 + BαD)` (exact symbolic expansion, all eight).
- T3: 25 monomials of reach ≤ 2: one particular solution `½ sin 2k_1`, six free directions, rank-six overlap with `sin k_b sin k_c`; the quarter turn about axis 1 and the half turn about axis 2 force all six coefficients to zero.
- T4: the c-part's uniform-strain contribution is the scalar `γΣB_a^j s_a s_j c_a`, second order at each of the eight zeros (`γΣB_a^jD_jq_aq_j`).
- Control (numerical linear algebra): commutant dimensions `8, 32, 88` for reach `1, 2, 3` = counts of `a + cH`; conditions: reach one residual `2.83`, reach two rank 19 / nullity 6; six functions' singular values under covariance `8.2–22.7` (none vanishes).
