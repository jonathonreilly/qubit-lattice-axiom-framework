# Block 177 — results (2026-09-27)

- **Runner.** `scripts/admissibility_rule_a_jammed_box_of_moving_records_rearranges_only_from_its_surface_2026_09_27.py`: `TOTAL: PASS=11 FAIL=0` in about 3 s. Six mutations (four in families A–D, two in F), each failing in its own family only.
- **T1.** The movable set grows by one layer per move.
- **T2.** `N₂ = 18L⁴ + 33L² − 24L`, checked for `L = 2..9`.
- **T3.** `N_T = (6L²)^T/T! + O(L^{2T−2})`, with no `L^{2T−1}` term.
