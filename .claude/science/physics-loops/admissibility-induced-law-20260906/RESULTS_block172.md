# Block 172 — results (2026-09-27)

- **Runner.** `scripts/admissibility_rule_walls_of_filled_regions_are_connected_through_edges_so_the_record_gas_makes_the_chessboard_up_to_a_larger_bond_cost_2026_09_27.py`: `TOTAL: PASS=12 FAIL=0` in about 3 s. Six mutations (four in families A–D, two in F), each failing in its own family only.
- **T1.** Walls of filled regions are edge-connected (12 neighbours).
- **T2.** The region count is `(k/4) r_k` with `r_k = (12/(k − 1)) C(11k, k − 2)`, radius `10¹⁰/11¹¹`.
- **T3.** At `x₀ = 347/10000` the defect sum is at most `11/100`, so `⟨σ⟩ ≥ 39/50`. Without contents this holds for `g ≤ (347/10000)²`, which is `(347/120)²` times block 117's bound. At `x₀ = 3/250` the sum is at most `4/10000`.
