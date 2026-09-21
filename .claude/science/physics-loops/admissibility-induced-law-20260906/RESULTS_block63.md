# Block 63 — results (2026-09-21)

- Runner `scripts/admissibility_rule_what_the_walk_conserves_momentum_flows_on_bonds_relabellings_reach_second_neighbours_2026_09_21.py`: `TOTAL: PASS=17 FAIL=0`; 9 mutations, each in its own family.
- T1: `5³` torus, rational state in motion: `dπ_j/dt + div J = 0` at all 125 sites, `j = 1, 2, 3`; the current on a bond changes when the amplitude at `x + e_a + e_j` is changed, the site response does not.
- T2: `i[H, G_ξ]ψ = Σσ_a½{C_a[d_aξ_j], S_j}ψ` at all 125 sites; `⟨i[H, G_ξ]⟩ = Σ(d_aξ_j)J_a^j`; exactly stationary state on a `4³` torus (`Hψ = ψ`): divergence-free currents that vary from bond to bond.
- T3: `J = ½[Θ(x) + Θ(x + e_a)] − ½Re(d_aψ)†σ_a(d_aS_jψ)` on all 375 bonds, nine index pairs; plane waves with sines `(1/3, 2/3, 2/3)`, `(2/3, 1/3, 2/3)`: `Σ_a(s_a − s'_a)M_a = 0`; `sin k − sin k' = 2 sin(q/2) cos k̄` at rational points.
- T4: `H` reaches distance 1; `i[H, G_ξ]` reaches distance 2, both kinds.
- T5: the torque identity at all 125 sites; on the stationary state the antisymmetric response is the divergence of `b_c` and not zero.
- Control and refuting pass W1–W4: identities on a random complex state (`10⁻¹⁵`); `J(q)/Θ(q) = e^{iq_a/2} cos k̄_a` to `3×10⁻¹⁶`; two equal-energy pairs with the same `q`: symbols `14.6°` apart; block 62's defect `= Σ p_a(1 − cos k̄_a)M_a`.
