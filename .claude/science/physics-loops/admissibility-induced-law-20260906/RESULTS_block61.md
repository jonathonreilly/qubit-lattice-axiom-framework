# Block 61 — results (2026-09-21)

- Runner `scripts/admissibility_rule_three_lengths_per_site_a_body_at_rest_stretches_them_alike_hop_energy_drives_whole_columns_2026_09_21.py`: `TOTAL: PASS=18 FAIL=0`; 12 mutations, each in its own family.
- T1: volume × curvature for `diag(ℓ_j²)`: first order `−2Σ_jΣ_{i≠j}∂_i²λ_j`; second order variationally equal to `2(∂_3λ_1∂_3λ_2 + ∂_2λ_1∂_2λ_3 + ∂_1λ_2∂_1λ_3)`; equal lengths `−4∇²λ`, `2|∇λ|²`; kinetic density `−2Σ_{i<m}λ̇_iλ̇_m/w²`.
- T2: `5³` box: 108 static equations non-singular; body at rest of energy 3/10: three lengths equal, `= −u`, `=` block 60's solution (0.022 at the body).
- T3: `7³` box, unit hop energy along axis 1: closed forms satisfy the three equations at 125 sites; tent `−1/6, −1/3, −1/2, −1/3, −1/6` (`K = 3/4`); heights `−1/3, −1/2, −7/6, −17/2` for `n = 3, 5, 13, 101`; rates exactly block 60's; equal hop energies leave `λ_1 + u = 1/9` next to the wall; the equal-lengths law's residual 0.061 one site from the source.
- T4: determinant `−16[(2m_1 − m_2)(m_1s² − (m_1 + m_2)σ)X² − 2(m_1s³ − (2m_1 + m_2)sσ + 3(m_1 + m_2)π)X + 4πs]`; comparator's term: `v_1 + v_2 = 1 − 3ρ`, `v_1v_2 = ρ`; coordinate planes `1, 0`; body diagonals `1/3` twice; at `(π/3, π/3, π)`: `X = 2/3, 4` (speeds² `1/9, 2/3`), lattice equations at 72 sites; isotropy conditions' reduced basis is 1.
- Controls: static/tent/mode checks; refuting pass W1–W5 (real-space evolution on `12³`, constraint kept to `10⁻¹¹`, peaks at the closed form).
