# Block 42 — results (2026-09-20)

- Runner `scripts/admissibility_rule_interaction_through_the_odds_of_unformed_sites_field_equation_massless_surface_2026_09_20.py`: `TOTAL: PASS=20 FAIL=0`; fourteen mutations, each in its own family.
- T1: gap weights `1 + 3λ₁ⁿ + 2λ₂ⁿ`, `1 − 3λ₁ⁿ + 2λ₂ⁿ`, `1 − λ₂ⁿ` at `n = 1..6`, three triples; content average exactly `1`; all 16 arrangements of the plaquette weigh `Z`; contents across unformed sites correlated.
- T2: factorization `(T/6)⁶ Π(1 + 6K₁δ_y)`; derivative `K₁ − 1/6` (36 entries, exact differentiation); spectrum `λ_i(6 − E(k))`; `6λ₁ = 1 ⟺ 5p = 7q + 4r` with `(3,1,2)` on it; `m² = 5/3` at (5,2,4), `3/2` at (7,3,5); `6λ₁ = 22/7` at (12,1,2); exact solve = mode sum at all 64 sites of the `4³` torus.
- T3: `R(ωx, ωy) ≤ R/((1−κ) + κR)` on 1600 random and 20 adversarial exact pairs (`999/1000` of the bound); product bound on 200 cases; `κ = 400/441`, `6(1−κ) = 82/147` at (21,20,20); silent at (5,2,4).
- T4: covariance under the 24 rotations with a record present; content-averaged weight `1 + 3λ₁² Σ m_y·m_{y'}`, no first-order term.
- T5: seven-outcome fixed point and eigenvalues `ρ(1−ρ)(g−1)/(1+ρ(g−1))`, `ρgλ₁/(1+ρ(g−1))` at four points; zero scalar strength at `g = 1`; `1/6` at `ρ = 1/2`, `g = 2`.
- T6: on the `5³` torus the field of a body of agreeing records is the reaching probability of a killed walk; interior charge exactly `1 − 6λ₁`; capacity per record `0.872, 0.520, 0.399` at (5,2,4) and `0.713, 0.277, 0.140` at `λ₁ = 19/119` for cubes of 1, 8, 27 records; monotone, subadditive.
- Executed (bodies, side 25, range 2.79): far lean of cubes of 8, 27, 64 records = `2.2, 3.2, 4.0` single records at 7 steps; 8 records spaced 4 apart = `2.5`.
- Executed: nonlinear lean ratios match the screened Green function to four digits at range `0.77`, within 2 % at range `1.95`; on the massless surface `r·v(r)` is flat at `0.28–0.30` for `r = 1..5` on side 27 (iterations grow like the square of the side); density excess `1.5·10⁻⁴, 3.5·10⁻⁷` at `g = 1` against `6.5·10⁻², 6.7·10⁻³` at `g = 1.5`.
