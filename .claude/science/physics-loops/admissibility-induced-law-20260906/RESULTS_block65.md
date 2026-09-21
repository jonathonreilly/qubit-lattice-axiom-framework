# Block 65 — results (2026-09-21)

- Runner `scripts/admissibility_rule_the_blind_walk_a_scalar_hop_weighted_by_the_twist_of_the_coin_along_the_bond_2026_09_21.py`: `TOTAL: PASS=13 FAIL=0`; 9 mutations, each in its own family.
- T1: `5×4×3` torus, rational rotation field and state: the operator identity at all 60 sites; the scalar hop vanishes for a uniform rotation and for a rotation without twist.
- T2: the change of `H[ϑ]` under a coin rotation equals the shift `ϑ → ϑ + θ` site by site; hermitian; reach 1.
- T3: derivative of `⟨H[ϑ]⟩` in one site's rotation `= ½ d(ψ†σ_cψ)/dt` (exact difference, state in motion); on the exactly stationary state of the `4³` torus: zero with the hop at 39 sampled sites and axes, non-zero at all 39 without.
- T4: `ε·T = 2ε^{jkl}∂_kB_{jl}`; zero for symmetric strain; `−4 div ϑ` for the rotation; hop `→ ½ div ϑ = −⅛ ε·T`.
- Refuting pass W1–W4: finite rotations: `1.86 s²` with the hop, `1.10 s` without; spectrum shift `2.03 s²` against `0.6 s`; numerically found stationary state: `3×10⁻¹⁷` against up to `5.6×10⁻³`; the hop's local energy `½(∂ϑ) cos k` to `1.5×10⁻⁵`.
