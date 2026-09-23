# Block 89 — results (2026-09-23)

- Runner `scripts/admissibility_rule_the_unit_of_rate_decides_the_alternations_thresholds_in_log_rates_exact_mass_convexity_term_no_global_minimum_2026_09_23.py`: `TOTAL: PASS=17 FAIL=0`; 9 mutations, each in its own family (~3 s).
- T1: `h² = sin²k + sinh²δ`, `h = cosh δ h_lin(tanh δ)`; 16-block `H² = Σ sin²k_j + Σ sinh²δ_j`; ring of eight with amplitudes `2, 1/2`: `E² ∈ {9/16, 17/16, 25/16}`.
- T2: block 59's `M(0)(1,1,1) = 0`; pointwise second derivatives `−3/|s|` (log) and `−(3 − |s|²)/|s|` (linear), difference `−|s|`; threshold `⟨1/|s|⟩/4 = χ/12 + ⟨|s|⟩/12`.
- T3: extra pointwise term `(4a + b)/|s|`; threshold `(χ_a + 2⟨|s|⟩)/72`.
- T4: at `δ_w = 6 + 12√3κ`, `√3δ_w³/6 − 6κδ_w² − √3 = √3(δ_w² − 1) > 0`; corner nullity `4` at `a = 3/10` (e^δ = 2) and `0` at `a = 1/4`.
- Control: `⟨1/|s|⟩ = 0.91067`, `⟨|s|⟩ = 1.19380`, `χ = 1.53822`, `χ_a = 1.88273`; thresholds `0.2277` / `0.1282`, `0.0593` / `0.0262`; `6³` spectrum to `10⁻¹⁴`; balance table (barrier and runaway above threshold, interior minimum just below, runaway below `κ ≈ 0.19`); crowd `3×3`: log − linear = `|E(0)|` exactly.
