# Block 151 — results (2026-09-26)

- **Runner.** `scripts/admissibility_rule_no_finite_range_interaction_keeps_two_excluded_records_total_energy_current_on_the_plane_or_in_space_2026_09_26.py`: `TOTAL: PASS=14 FAIL=0` (under 1 s). Eight mutations (six in families B–E, H and I, two in F), each failing in its own family.
- **Line check.** Every step S0–S7 of probe #9251 was read against block 143's landed T1, T4 and T6. The probe's own exact checker was rerun (7/7, about 3 min). No gap was found.
- **The theorem.** Two records under one record per site, on Z^2 or Z^3, either exchange sign; any bounded hermitian translation-invariant interaction of finite relative range; any placement in block 143's class: the total energy current is not conserved.
- **The route.** The one-body placement current is forced to vanish; the resolvent identity makes the pair transparent at almost every energy; the determinant identity makes the perturbation determinant real on the continuum; bounded spectral densities (block 143 T6) put it in H^2 of both half-planes, so it is one; the removed states make it vanish at their energy.
- **T2 (added after the first push).** Any number of records N >= 2 and any finite-range interaction of any body number: separating all but two records reduces a kept current exactly to the pair's (runner I1).
- **Not covered.** Infinite-range interactions, non-local placements.
