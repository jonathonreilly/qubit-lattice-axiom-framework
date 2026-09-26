# Block 156 — results (2026-09-26)

- **Runner.** `scripts/admissibility_rule_the_coins_spin_keeps_its_own_books_on_the_faces_and_a_spin_polarised_walker_at_rest_sources_only_the_shift_2026_09_26.py`: `TOTAL: PASS=18 FAIL=0` (about 4 s). Five mutations (three in families B and C, two in F), each failing in its own family.
- **T1.** For every state, dS~_l/dt + D(x) - D(x - e_l) = -sum_ij eps_lij (Theta_ij - Theta_ji). The spin current is isotropic (delta_il D), and the torque is the antisymmetric part of block 120's two-step stress. The curl gives block 138 T3.
- **T2.** A walker at rest with a real envelope has zero energy, two-step momentum and currents. It sources the shift only, through P^B = (1/4) curl S~, which is momentarily static.
- **T3.** On the declared lattice reading of block 136 T4, the static shift is the lattice vector potential of the magnetisation wbar S~/(16 alpha). It is divergence-free. A b^3 box carries total face spin b(b - 1)^2 n.
- **Referee.** grok-4.6 confirmed the probe's result (#9284).
