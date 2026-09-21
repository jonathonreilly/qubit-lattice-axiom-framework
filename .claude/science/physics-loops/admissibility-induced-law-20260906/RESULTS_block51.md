# Block 51 — results (2026-09-21)

- Runner `scripts/admissibility_rule_the_wind_of_a_capturing_body_is_not_isotropic_lattice_streaming_viscous_term_of_cubic_symmetry_2026_09_21.py`: `TOTAL: PASS=15 FAIL=0`; eight mutations, each in its own family.
- T1: streaming operator `= (1/√3)[−s·∇ + ½Σ_k|s_k|∂_k²]` exactly on fields of degree two (150 rational unit contents).
- T2: moments `1/2, 1/4, 1/8`; `ν_lat² = 3/256` for both the isotropic and the cubic part; `D_lat² = 1/48`; longitudinal damping `2, 3/2, 4/3` by direction.
- T3: curl of `(∂_x³, ∂_y³, ∂_z³)χ`: `240y` for `x⁵ − 10x³y² + 5xy⁴`; `70/2187` at `(1,2,2)` for `1/r` (symbolically `−105xy(x² − y²)/r⁹`).
- T4: the creeping solution satisfies both equations at five wave vectors and three `η`; homogeneous of degree `−1`; `k × g ≠ 0` at generic `k` for `η > 0`.
- Executed (r 6 to 10, eight seeds each): `γ = 0, ρ = 0.1`: `0.1798, 0.1426, 0.1158` (exact first-order ×`1/(1−ρ)`: `0.176, 0.147, 0.122`), ratio `1.55 ± 0.05`; `γ = 2, ρ = 0.1`: `0.1754, 0.1485, 0.1304`, ratio `1.35 ± 0.03`; `γ = 1, ρ = 0.3`: `0.2225, 0.1858, 0.1717`, ratio `1.30 ± 0.02` (isotropic closure `0.153`, `0.197`). Creeping solution: ratio `1.18, 1.37, 1.76` at `η = 1/4, 1/2, 1` (r 6 to 10), `1.26, 1.54, 2.18` at r 20 to 32.
