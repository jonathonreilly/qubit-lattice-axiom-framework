---
claim_id: admissibility_rule_three_responses_eight_species_the_frames_site_stress_has_the_wrong_sign_in_shear_for_six_species_only_the_two_step_current_serves_all_bounded_theorem_note_2026-09-21
claim_type: bounded_theorem
claim_scope: "Frame response Theta and one-step/two-step currents J,K obey exact site-sign transformation laws. They agree to leading smooth order near the first corner and differ by stated component signs near other corners. Sign-pattern counts and conditional stationary divergence comparisons do not classify physical species or establish field-equation nonexistence."
upstream_dependencies:
  - minimal_axioms
  - admissibility_rule_a_phase_timed_by_the_local_clock_every_packet_falls_towards_slow_clocks_force_is_energy_times_gradient_weight_and_inertia_tied_by_the_walk_bounded_theorem_note_2026-09-21
  - admissibility_rule_angles_are_the_tilt_of_the_coins_frame_with_them_two_disturbances_travel_at_one_direction_free_speed_and_the_price_is_a_conserved_stress_bounded_theorem_note_2026-09-21
  - admissibility_rule_what_the_walk_conserves_momentum_flows_on_bonds_relabellings_reach_second_neighbours_the_nearest_neighbour_frame_misses_by_two_differences_bounded_theorem_note_2026-09-21
  - admissibility_rule_the_fall_is_owed_by_the_ledger_a_field_energy_per_local_tick_requires_the_contents_stress_gradient_to_equal_its_weight_bounded_theorem_note_2026-09-21
  - admissibility_rule_reach_three_a_momentum_that_is_the_same_for_all_eight_species_gives_a_coupling_with_the_exact_current_and_one_geometry_for_all_bounded_theorem_note_2026-09-21
  - admissibility_rule_the_eight_species_are_exchanged_by_site_signs_and_a_half_turn_of_the_coin_what_each_varying_field_becomes_bounded_theorem_note_2026-09-21
  - admissibility_rule_which_species_fall_the_ledger_owes_under_reach_two_a_reflected_species_has_minus_its_weight_under_reach_three_all_eight_agree_bounded_theorem_note_2026-09-21
runner: scripts/admissibility_rule_three_responses_eight_species_site_stress_bond_current_two_step_current_2026_09_21.py
---

# Three lattice responses: exact sign transformations and conditional divergence comparisons

**Type:** bounded_theorem
**Status:** bounded-support; conditional supplied model, unaudited.

This note states conditional mathematics for explicitly supplied operators and fields. The amplitude dynamics and composition rules are not derived from the repository axioms, and no gravitational claim is made.
No bridge, Born-weight, plane-or-sum or gravity statement enters this note as a premise; this note does not fire wake condition 1 of the parked statistical-bridge decision.
No value, constant or theorem is imported as authority; the standard mathematical imports are named at definition level.

## Premises and declared objects

On an even finite torus use H=sum_a sigma_a S_a, P_j=S_j C_j and the maps V_n with D_a=(-1)^n_a,s=product D_a,rho=sD. Define Theta_a^j(x)=Re psi_x^dagger sigma_a(S_j psi)_x. It is the derivative of the supplied frame Hamiltonian expectation at the identity frame. Define the bond response from x to y=x+e_a by
`J_a^j(x,y)=Re[psi_y^dagger sigma_a(S_j psi)_x+(S_j psi)_y^dagger sigma_a psi_x]/2`,
and K by replacing S_j with P_j. All quantities are mathematical responses of the supplied models. For clocked comparisons apply them to phi psi and explicitly require stationarity when using a stationary divergence identity.

## Theorem T1 — the table

*Statement.* For every state, every species `n`, all `a, j`, at every site (bond): `Θ_a^j[V_nψ] = s_nD_aD_jΘ_a^j[ψ]`; `J_a^j[V_nψ] = s_nD_jJ_a^j[ψ]`; `K_a^j[V_nψ] = s_nK_a^j[ψ]`.

*Proof.* `V_n` is a unitary acting site by site with `V_n†σ_aV_n = (ρ_n)_aσ_a`, `S_jV_n = D_jV_nS_j`, `P_jV_n = V_nP_j` (block 70 T1(a)); moving from `x` to `x + e_a` brings the site sign `D_a`. So `Θ` picks up `ρ_aD_j = s_nD_aD_j`; `J` picks up `ρ_aD_aD_j = s_nD_j`; `K` picks up `ρ_aD_a = s_n`. ∎

## Theorem T2 — for the first species the three agree

*Statement.* For a smooth two-component amplitude, with lattice spacing `h`: `Θ_a^j`, `J_a^j` and `K_a^j` all equal `h Re ψ†σ_a(−i∂_jψ) + O(h²)`, in all nine components. Hence, for an amplitude `V_n ×` (smooth): `Θ_a^j = D_aD_jK_a^j` and `J_a^j = D_jK_a^j` at leading order.

*Proof.* `S_jψ` and `P_jψ` are both `−ih∂_jψ + O(h³)`; evaluating one factor at `x + e_a` changes the product at the next order. Then T1. ∎

For a plane wave the exact polynomial relations are K=cos k_a cos k_j Theta and K=cos k_j J; the corresponding ratios require their nonzero denominators and a nonzero compared response, and `cos k_a = D_a cos q_a`: the signs of T1 are the lattice's cosines at the species' zero.

## Theorem T3 — sign patterns and divergence comparison

The sign identity D_a D_j=1 for all a,j holds exactly for n=(000),(111); D_j=1 for every j holds exactly for n=(000). K has its common overall energy sign for all eight. These are counts of sign-pattern identities; an actual response component can vanish, so they are not counts of physically allowed species.

At leading smooth order,
`sum_a d_a K_a^j-sum_a d_a Theta_a^j=2 sum_(a:D_a!=D_j) d_a K_a^j`,
`sum_a d_a K_a^j-sum_a d_a J_a^j=(1-D_j)sum_a d_a K_a^j`.
This is direct substitution of T2. When additionally the state is stationary for H_w, PR #8605's identity yields -div K[phi psi]=fP with leading term e du. Comparing Theta or J to THIS supplied identity-frame comparator then gives respectively the conditions sum_(a:D_a!=D_j)d_a K_a^j=0 or (1-D_j)e d_j u=0.

The former sum can vanish by cancellation among nonzero terms; it does not require each shear gradient to vanish. Generic oblique flow alone does not guarantee a mismatch. Full coframe field equations contain other stress terms at the same order, so these expressions do not establish physical species exclusion or a general no-static-solution theorem. K is the specified two-step current used for comparison, not a uniquely derived physical stress.

## Historical experiments — deferred

Original auxiliary calculations, floating-point scans, campaign conclusions and author review history remain recoverable on the original branch. They are not fresh evidence for this landing. The original filename and claim identifier are retained for traceability; the present title and scope control.

## No-Go Discipline Gate

### N1 — Quantifiers and exceptions
A sign mismatch has content only for a nonzero response. Divergence sums can cancel. The stationary comparator is not the complete coframe stress identity and supplies no physical species selection.

### N2 — Wall independence
No repository no-go wall is used.

### N3 — Supplied structure
The operators, domains, boundary conditions and state assumptions stated above are explicit mathematical hypotheses. They do not add a framework axiom or primitive.

### N4 — Dependencies
The dependencies below identify the actual supplied inputs; earlier stronger conclusions are not imported.

### N5 — Resolution
The canonical runner checks the finite examples and identities stated above using exact arithmetic. General conclusions require the displayed arguments, not extrapolation from samples. Historical simulations are deferred.

### N6 — Primitive boundary
No new primitive, species selection, filling rule or physical interpretation is adopted.

### N7 — Strongest objection
A sign mismatch has content only for a nonzero response. Divergence sums can cancel. The stationary comparator is not the complete coframe stress identity and supplies no physical species selection.

### N8 — Earlier claims
This scoped result supersedes stronger wording in the original submission. It is a landing review, not an independent audit verdict.

## Falsifiers

A failure of a stated identity under its full hypotheses, or a different exact result for a specified finite example, would refute the corresponding result. An example outside those hypotheses does not.

## Imports

- [minimal_axioms](MINIMAL_AXIOMS_2026-06-29.md): repository boundary; it does not supply the amplitude dynamics below.
- [admissibility_rule_a_phase_timed_by_the_local_clock_every_packet_falls_towards_slow_clocks_force_is_energy_times_gradient_weight_and_inertia_tied_by_the_walk_bounded_theorem_note_2026-09-21](ADMISSIBILITY_RULE_A_PHASE_TIMED_BY_THE_LOCAL_CLOCK_EVERY_PACKET_FALLS_TOWARDS_SLOW_CLOCKS_FORCE_IS_ENERGY_TIMES_GRADIENT_WEIGHT_AND_INERTIA_TIED_BY_THE_WALK_BOUNDED_THEOREM_NOTE_2026-09-21.md): supplied mathematical construction from PR #8570; no premise adoption or retained grade is inferred.
- [admissibility_rule_angles_are_the_tilt_of_the_coins_frame_with_them_two_disturbances_travel_at_one_direction_free_speed_and_the_price_is_a_conserved_stress_bounded_theorem_note_2026-09-21](ADMISSIBILITY_RULE_ANGLES_ARE_THE_TILT_OF_THE_COINS_FRAME_WITH_THEM_TWO_DISTURBANCES_TRAVEL_AT_ONE_DIRECTION_FREE_SPEED_AND_THE_PRICE_IS_A_CONSERVED_STRESS_BOUNDED_THEOREM_NOTE_2026-09-21.md): supplied mathematical construction from PR #8592; no premise adoption or retained grade is inferred.
- [admissibility_rule_what_the_walk_conserves_momentum_flows_on_bonds_relabellings_reach_second_neighbours_the_nearest_neighbour_frame_misses_by_two_differences_bounded_theorem_note_2026-09-21](ADMISSIBILITY_RULE_WHAT_THE_WALK_CONSERVES_MOMENTUM_FLOWS_ON_BONDS_RELABELLINGS_REACH_SECOND_NEIGHBOURS_THE_NEAREST_NEIGHBOUR_FRAME_MISSES_BY_TWO_DIFFERENCES_BOUNDED_THEOREM_NOTE_2026-09-21.md): supplied mathematical construction from PR #8593; no premise adoption or retained grade is inferred.
- [admissibility_rule_the_fall_is_owed_by_the_ledger_a_field_energy_per_local_tick_requires_the_contents_stress_gradient_to_equal_its_weight_bounded_theorem_note_2026-09-21](ADMISSIBILITY_RULE_THE_FALL_IS_OWED_BY_THE_LEDGER_A_FIELD_ENERGY_PER_LOCAL_TICK_REQUIRES_THE_CONTENTS_STRESS_GRADIENT_TO_EQUAL_ITS_WEIGHT_BOUNDED_THEOREM_NOTE_2026-09-21.md): supplied mathematical construction from PR #8597; no premise adoption or retained grade is inferred.
- [admissibility_rule_reach_three_a_momentum_that_is_the_same_for_all_eight_species_gives_a_coupling_with_the_exact_current_and_one_geometry_for_all_bounded_theorem_note_2026-09-21](ADMISSIBILITY_RULE_REACH_THREE_A_MOMENTUM_THAT_IS_THE_SAME_FOR_ALL_EIGHT_SPECIES_GIVES_A_COUPLING_WITH_THE_EXACT_CURRENT_AND_ONE_GEOMETRY_FOR_ALL_BOUNDED_THEOREM_NOTE_2026-09-21.md): supplied mathematical construction from PR #8601; no premise adoption or retained grade is inferred.
- [admissibility_rule_the_eight_species_are_exchanged_by_site_signs_and_a_half_turn_of_the_coin_what_each_varying_field_becomes_bounded_theorem_note_2026-09-21](ADMISSIBILITY_RULE_THE_EIGHT_SPECIES_ARE_EXCHANGED_BY_SITE_SIGNS_AND_A_HALF_TURN_OF_THE_COIN_WHAT_EACH_VARYING_FIELD_BECOMES_BOUNDED_THEOREM_NOTE_2026-09-21.md): supplied mathematical construction from PR #8602; no premise adoption or retained grade is inferred.
- [admissibility_rule_which_species_fall_the_ledger_owes_under_reach_two_a_reflected_species_has_minus_its_weight_under_reach_three_all_eight_agree_bounded_theorem_note_2026-09-21](ADMISSIBILITY_RULE_WHICH_SPECIES_FALL_THE_LEDGER_OWES_UNDER_REACH_TWO_A_REFLECTED_SPECIES_HAS_MINUS_ITS_WEIGHT_UNDER_REACH_THREE_ALL_EIGHT_AGREE_BOUNDED_THEOREM_NOTE_2026-09-21.md): supplied mathematical construction from PR #8605; no premise adoption or retained grade is inferred.
- Standard mathematical definitions: finite-dimensional linear algebra, tensor products, spectral decompositions, exact rational arithmetic, differentiation and lattice shifts as explicitly used above.

## Review record

Original source: PR #8607 head `c331c7f282e422c209816553d8d703b6a03ef78b`, branch `physics-loop/admissibility-induced-law-block74-three-responses-eight-species-20260921`. The present revision narrows the mathematical domain and corrects the material issues recorded in its statements. Original ancillary science is deferred with recovery preserved. No audit verdict is applied.

## Verification

```bash
PYTHONPATH=scripts python3 scripts/admissibility_rule_three_responses_eight_species_site_stress_bond_current_two_step_current_2026_09_21.py
```

Expected: a zero exit code and a final `TOTAL` with `FAIL=0`.
