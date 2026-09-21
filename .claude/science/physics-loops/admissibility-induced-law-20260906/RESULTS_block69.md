# Block 69 — results (2026-09-21)

- Runner `scripts/admissibility_rule_reach_three_a_momentum_that_is_the_same_for_all_eight_species_2026_09_21.py`: `TOTAL: PASS=12 FAIL=0`; 8 mutations, each in its own family.
- T1: the four conditions on `a sin k + b cos k + c` have no solution (`b = c = 0`, then slopes `a` and `−a`); `½ sin 2k` meets them.
- T2: `P_j = S_jC_j` commutes with the walk at all 150 sites of a `6×5×5` torus (rational state, `j = 1, 2, 3`); the total of `Re ψ†P_jψ` does not change for a state in motion.
- T3: `i[H, G]ψ = Σσ_a½{C_a[d_aξ_j], P_j}ψ` at all 150 sites for a rational displacement and state; an amplitude on one site is carried three steps; the expectation equals the pairing of `d_aξ_j` with `K_a^j`.
- T4: `H² = Σ[s_a + c_aΣ_jB_a^js_jc_j]²` at all eight species' rational wave vectors; inverse metric `(1 + B)ᵀ(1 + B)` for every species by exact symbolic expansion, general strain; bending over fall `1 + β` for all eight.
- Control: packets of species `(0,0)` and `(1,0)`: sideways displacement `−10.57, −10.57` under reach three (`−15.06, −15.06` frame; `−12.64, +12.64` reach two); distances in a uniform stretch `32.9, 32.9` (`39.2, 39.2`; `35.5, 29.5`). Dense `5×6×7` torus: `|div K^j| ≤ 1.9e-17` at any site for 12 stationary states; local law `|d/dt Re ψ†P_jψ + div K^j| ≤ 1.3e-18` for a random state.
- The ladder: reach one (frame) — one set of lengths, no exact current; reach two — exact current, species-dependent lengths; reach three — both, with larger lattice corrections (the stretch is seen through `cos² k`).
