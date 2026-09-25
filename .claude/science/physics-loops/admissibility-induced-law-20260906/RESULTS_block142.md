# Block 142 — results (2026-09-25)

- **Runner.** `scripts/admissibility_rule_one_record_per_site_pairs_bound_as_neighbours_have_half_the_walkers_speed_squared_on_a_line_and_never_its_speed_in_every_direction_2026_09_25.py`: `TOTAL: PASS=11 FAIL=0` (about 7 s). Seven mutations, each failing in its own family.
- **T1.** On the line, under one record per site, equal-coin pairs bound as neighbours have exactly E = V + sin²(K/2)/V, so c² = 1/2 for every V. Opposite coins give E = V + cos²(K/2)/V (inverted). Without exclusion the even channel has c² = 3/2.
- **T2.** At strong binding the part of the pair's generator that keeps its bond e_a is 5/2 − ½ cos K_a σ_aσ_a − Σ_{b≠a} cos K_b σ_bσ_b. Exclusion halves the along-bond term: the rear record cannot step first.
- **T3.** Covariance leaves five real numbers. The bound coins lie on a zero-spin ray, the spin ±1 plane, or an accidental union. On every rest level the three axis weights sum to at most 3/2, against 3 for a free record, so no strongly bound pair has weight one along all three axes. Fermion pairs on a ray never roll and have weight −1/2 along their bond.
- **T4.** Controls: a free record has 3; without exclusion the along-bond term is not halved; contact pairs have at most 1; the timed term scales like the hops.
