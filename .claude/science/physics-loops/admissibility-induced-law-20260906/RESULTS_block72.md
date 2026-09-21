# Block 72 — results (2026-09-21)

- Runner `scripts/admissibility_rule_which_species_fall_the_ledger_owes_reach_two_against_reach_three_2026_09_21.py`: `TOTAL: PASS=12 FAIL=0`; 8 mutations, each in its own family.
- T1: `i[φ, P_j]ψ = −½C²_j[d²_jφ]ψ` at all 150 sites of a `6×5×5` torus; `i[H_w, G] = φ(i[H, G])φ − (ΛHφ + φHΛ)` at all sites; `d⟨G⟩/dt` = pairing with `K[φψ]` − `Σξf^P`; total two-step momentum changes at minus the total force (not zero).
- T2: `6×6×6` torus, varying rates, all eight species, `j = 1, 2, 3`, all 216 sites: `𝔢 → s_n𝔢`; `f_j → s_nD_jf_j`; `f^P_j → s_nf^P_j`.
- T3: exact symbolic expansion on a line: smooth amplitude `f = f^P = 𝔢 du`; staggered amplitude `f = −𝔢 du`, `f^P = +𝔢 du`; lower orders vanish.
- Control: W1 `|div J + f| ≤ 6e-17`, `|div K + f^P| ≤ 3e-17` site by site on eigenvectors of `H_w` (`5×6×7`); W2 force over weight for packets: reach two `±0.9800, ±0.8775, ±0.6215` (`= D cos q`), reach three `+0.9207, +0.5400, −0.2273` for both species (`= cos 2q`), `q = 0.2, 0.5, 0.9`; W3 site-by-site spread below `0.001`.
- Consequence: block 66's requirement is met by all eight species under reach three; under reach two it fails with the opposite sign for species reflected along the gradient (remainder `2𝔢 du`).
