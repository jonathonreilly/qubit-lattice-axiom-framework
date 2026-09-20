# Block 39 — results (2026-09-20)

- Runner `scripts/admissibility_rule_records_that_move_pair_weight_transit_static_equilibrium_binding_scale_2026_09_20.py`: `TOTAL: PASS=19 FAIL=0`; nine mutations, each in its own family.
- T1: detailed balance of every pair-weight move with the static law on the occupied set (heat-bath and min-ratio acceptance; 180 arrangements; three weight/scale choices); all 180 arrangements connected.
- T2: `K` unchanged by the scale; 288 moves with `k_x = k_y` agree between scales 1 and 1/2, 384 others differ; escape probability `1/(1 + (cp)^k)`.
- T3: normalized transit identical at both scales; four-move cycle with products `1/2592` against `1/2376`.
- T4: birth-death pair with rate `zZ_x` balanced on all 2401 configurations of the four-cycle; neutral scale `1/2` at (3,1,2) with multipliers `13/12, 1, 11/12`.
- T5: the complement of the empty state in the bond kernel has eigenvalues `c(p+q+4r) − 6`, `c(p+q−2r)` ×2, `c(p−q)` ×3: reflection positivity through bond planes iff `c ≥ c₀` (and `p ≥ q`, `p+q ≥ 2r`); reflection form of `v ⊗ w` on the four-site ring at (3,1,2): `−18`, `0`, `36` at `c = 1/4, 1/2, 1`.
- Executed: calibration onset between `c = 2.43` and `2.7` (literature 2.427); line (p,1,2) at density 0.3: onset near `p = 10` (neutral scale), between 5 and 6 (scale 1), between 8 and 12 (scale 1/2); acceptance down to `0.03` at scale 1, `p = 48`, with 70 % of sites empty.
