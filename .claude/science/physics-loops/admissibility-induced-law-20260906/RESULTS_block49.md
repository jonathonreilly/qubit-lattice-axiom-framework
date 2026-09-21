# Block 49 — results (2026-09-21)

- Runner `scripts/admissibility_rule_the_attraction_is_tied_to_growth_a_body_in_balance_draws_no_wind_pull_proportional_to_net_uptake_2026_09_21.py`: `TOTAL: PASS=14 FAIL=0`; eight mutations, each in its own family.
- T1: flux out of a region = minus the net uptake inside (three regions of a `5×5×5` block, exact rational currents).
- T2: cosine law through six faces gives `|s|₁` and the step frequencies (five contents); surplus = deficit at the 63 sites of a `4×4×4` block (three contents); residue of uniform emission `5/18, 11/98, −5353/14450, 95/242`; angular mean `1 + 4/π − 9/4 ≈ 0.023`.
- T3: mean emitted content `(2/3)n`, zero over a body's faces; pushes `β₁`, `β₂` times `K₀Q₁Q₂/r²`.
- T4: `q₁/G = 8π(1 − ρ)/3` at three densities and for any kept fraction; comparator `3/(8πT) ≈ 1.5·10⁻⁶²` for `T ≈ 8·10⁶⁰`.
- Executed (side 96, `ρ = 0.3`, `γ = 1`, solid balls of radius 3 at separation 16, two seeds each; pushes over the reference): both capture `0.92 ± 0.05`; body in balance pushed `0.75 ± 0.06`, pulls `0.10 ± 0.07`; both in balance `0.05 ± 0.07`; net uptake of a body in balance below `0.003` per tick.
- Executed, uniform wind (`specs/supervisor_control_block49_wind.py`): momentum per captured record over `u` for a pinned body in balance: about 15 sites `0.85, 0.83, 0.80` (`± 0.03`) at `γ = 0, 1, 4` (capturing only: `0.97`, `0.89`); one site at `γ = 0`: `0.97 ± 0.03` in balance, `1.00 ± 0.02` capturing.
