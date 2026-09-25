# Block 149 — results (2026-09-25)

- **Runner.** `scripts/admissibility_rule_a_free_walker_never_emits_or_absorbs_one_of_the_members_travelling_disturbances_its_energies_stay_inside_the_members_cone_2026_09_25.py`: `TOTAL: PASS=14 FAIL=0` (about 1 s). Seven mutations (five in families B–E, two in F), each failing in its own family.
- **T1.** |E(k) - E(k - q)| < |p(q)|, p_j = 2 sin(q_j/2), strictly for q != 0, at every lattice momentum (identity s_j(k) - s_j(k - q) = 2 cos(k_j - q_j/2) sin(q_j/2); equality forces q = 0; 32768 rational configurations).
- **T2.** The staggered mass keeps it (1-Lipschitz energies).
- **T3.** No single free walker emits or absorbs a member disturbance; against the walker's own dispersion the bound fails at the zone edge (control).
- **T4.** sin q - 2 sin(q/2) = -q^3/8: one cone at long wavelength, the walker inside the member at the lattice scale.
- **T5 (added after a panel report).** T1–T4 are within one band. The member's frequency is exactly a symmetric pair's energy, |p(q)| = 2|s(q/2)|. The pair energy |s(k)| + |s(k + q)| equals |s(q)| < |p(q)| at k = 0 and 2|cos(q/2)| at k_a = pi/2 - q_a/2, which exceeds |p(q)| iff sum_a cos q_a > 0. So pair creation out of the filled sea is kinematically open; the rate is not computed. With the staggered mass the channel is closed for |p(q)| < 2 mu.
