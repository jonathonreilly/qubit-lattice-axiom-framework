# Block 84 — results (2026-09-22)

- Runner `scripts/admissibility_rule_bond_rates_alternate_on_their_own_below_a_threshold_stiffness_sea_against_bond_law_one_rest_energy_2026_09_22.py`: `TOTAL: PASS=17 FAIL=0`; 7 mutations, each in its own family (2 s).
- T1 (symbolic): `H² = β²Σ_j(sin²k_j + δ_j²cos²k_j)` with independent `δ_j`; `E(δ = 1) = −√3` exactly on the `4³` grid.
- T2 (symbolic): `M(πe_1) = diag(−4α − 8β, [[−8β − 4γ, 4β],[4β, −8β − 4γ]])`; long-wavelength `−(α + 2β + 2γ)q²`; `M(π,π,π) = −(4α + 8β + 8γ)·1`.
- T3 (symbolic): threshold `κ = χ/12`; single-axis integrand's cyclic partners sum to the three-axis one; pointwise second derivative `−s²c²/(s² + δ²c²)^{3/2}`.
- T4 (symbolic): corner crossing at `δ = 2a/β`. T5 (exact rank): ring of 12, two walls → `4` zero modes; none without.
- Control: `χ = 1.53808` (`128³`; `κ_c = 0.12817`); `E(δ)`: `−1.1938 … −1.7321`; `δ*(κ)`: `0.016, 0.098, 0.18, 0.33, 0.48, 0.64, 0.73` at `κ = 0.128, 0.125, 0.12, 0.11, 0.10, 0.09, 0.085`; runaway below `κ = 0.0897`; least `|E|` with the scalar hop zero up to `δ = 2a` and opening above.
