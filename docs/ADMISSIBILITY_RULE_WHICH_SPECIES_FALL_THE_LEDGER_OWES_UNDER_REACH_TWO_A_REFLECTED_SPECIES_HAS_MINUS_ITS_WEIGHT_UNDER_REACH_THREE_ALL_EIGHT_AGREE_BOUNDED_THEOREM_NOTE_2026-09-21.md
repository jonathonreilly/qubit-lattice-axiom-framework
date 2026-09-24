---
claim_id: admissibility_rule_which_species_fall_the_ledger_owes_under_reach_two_a_reflected_species_has_minus_its_weight_under_reach_three_all_eight_agree_bounded_theorem_note_2026-09-21
claim_type: bounded_theorem
claim_scope: "The supplied clocked free walk obeys an exact two-step commutator/current identity and exact site-sign transformations of its local force expressions. Smooth-envelope limits give D_j e du for one-step and e du for two-step momentum. Matching a separately imposed identity-frame comparator is not a general field-solution or nonexistence theorem."
upstream_dependencies:
  - minimal_axioms
  - admissibility_rule_a_phase_timed_by_the_local_clock_every_packet_falls_towards_slow_clocks_force_is_energy_times_gradient_weight_and_inertia_tied_by_the_walk_bounded_theorem_note_2026-09-21
  - admissibility_rule_what_the_walk_conserves_momentum_flows_on_bonds_relabellings_reach_second_neighbours_the_nearest_neighbour_frame_misses_by_two_differences_bounded_theorem_note_2026-09-21
  - admissibility_rule_bond_strains_and_plaquette_curls_a_field_energy_per_local_tick_that_does_not_see_the_coins_axes_is_the_curvature_member_bounded_theorem_note_2026-09-21
  - admissibility_rule_the_fall_is_owed_by_the_ledger_a_field_energy_per_local_tick_requires_the_contents_stress_gradient_to_equal_its_weight_bounded_theorem_note_2026-09-21
  - admissibility_rule_reach_three_a_momentum_that_is_the_same_for_all_eight_species_gives_a_coupling_with_the_exact_current_and_one_geometry_for_all_bounded_theorem_note_2026-09-21
  - admissibility_rule_the_eight_species_are_exchanged_by_site_signs_and_a_half_turn_of_the_coin_what_each_varying_field_becomes_bounded_theorem_note_2026-09-21
runner: scripts/admissibility_rule_which_species_fall_the_ledger_owes_reach_two_against_reach_three_2026_09_21.py
---

# Clocked two-step momentum: exact commutator and leading corner force terms

**Type:** bounded_theorem
**Status:** bounded-support; conditional supplied model, unaudited.

This note states conditional mathematics for explicitly supplied operators and fields. The amplitude dynamics and composition rules are not derived from the repository axioms, and no gravitational claim is made.
No bridge, Born-weight, plane-or-sum or gravity statement enters this note as a premise; this note does not fire wake condition 1 of the parked statistical-bridge decision.
No value, constant or theorem is imported as authority; the standard mathematical imports are named at definition level.

## Premises and declared objects

Use a finite even periodic lattice, H=sum_a sigma_a S_a, H_w=phi H phi, phi>0, u=2 log phi and e_x=Re psi_x^dagger(H_w psi)_x. Define P_j=S_j C_j, G=sum_j{xi_j,P_j}/2 with real xi. Put d2_j phi(x)=phi(x+2e_j)-phi(x) and C2_j[v]psi(x)=[v(x)psi(x+2e_j)+v(x-2e_j)psi(x-2e_j)]/2. Let Lambda=sum_j{xi_j,C2_j[d2 phi]/2}/2.

The one-step expression is f_j=Re[(C_j[d phi]psi)^dagger H phi psi+psi^dagger C_j[d phi]H phi psi]; fP_j uses C2_j[d2 phi]/2 instead of C_j[d phi]. The two-step bond current K is defined in PR #8601. Energy and forces here are quadratic forms in supplied states. The label force does not supply a universal center-of-packet acceleration law. The maps V_n,s_n,D_j are defined in PR #8602. Infinite-lattice versions require bounded coefficients or compatible operator domains.

## Theorem T1 — the walk's law for the two-step relabelling, exactly

*Statement.* For every state, rate field and real displacement `ξ`: (a) `i[φ, P_j] = −½C^{(2)}_j[d^{(2)}_jφ]`; (b) `i[H_w, G] = φ(i[H, G])φ − (ΛHφ + φHΛ)`; (c) `d⟨G⟩/dt = Σ_{a,j,x}(d_aξ_j)(x)K_a^j[φψ](x → x + e_a) − Σ_{j,x}ξ_j(x)f^P_j(x)`; (d) if `ψ` is stationary for `H_w`, the lattice divergence of `K^j[φψ]` equals `−f^P_j` at every site; (e) for uniform `ξ` the total two-step momentum changes at minus the total force.

*Proof.* (a) `[φ, P_j]ψ(x) = (1/(4i))[(φ(x) − φ(x + 2e_j))ψ(x + 2e_j) − (φ(x) − φ(x − 2e_j))ψ(x − 2e_j)]`, and `φ(x) − φ(x − 2e_j) = d^{(2)}_jφ(x − 2e_j)`. (b)–(e) as block 66 T3, with block 69 T3 for the bare term. ∎

## Theorem T2 — the species

*Statement.* For every state, every positive rate field, every species `n` and `j = 1, 2, 3`, at every site: `𝔢[V_nψ] = s_n𝔢[ψ]`; `f_j[V_nψ] = s_nD_jf_j[ψ]`; `f^P_j[V_nψ] = s_nf^P_j[ψ]`.

*Proof.* Block 70 T1(a): `C_j[v]V_n = D_jV_nC_j[v]`, `C^{(2)}_j[v]V_n = V_nC^{(2)}_j[v]` (two steps), `HφV_n = s_nV_nHφ`; `V_n` is unitary site by site, so it drops out of each bilinear. ∎

## Theorem T3 — leading force terms and a conditional comparison

For smooth phi and an amplitude V_n times a smooth envelope, the leading terms are `f_j=D_j e d_j u` and `fP_j=e d_j u`. Indeed C_j[d phi] tends to h partial_j phi and C2_j[d2 phi]/2 tends to the same expression; apply T2's exact sign table to the first-corner result.

If one separately imposes the identity-frame comparator f=e du, the reach-three leading term matches for all n; the reach-two leading term matches in a component iff (1-D_j)e d_j u=0. The reflected component's discrepancy has magnitude 2 e d_j u when nonzero. This is a comparison of expressions, not a general field-equation no-go or existence proof. The full coframe identity contains stress times derivatives of the coframe and its inverse; such terms can be the same perturbative order as e du. They cannot be discarded to infer the universal comparator from the field action.

Stationary divergence statements require a stationary state of H_w. An incoherent mixture adds these quadratic expectations; a coherent sum generally has interference terms. Finite-wavevector cosine estimates and historical packet fits are not universal corrections to this local expansion.

## Historical experiments — deferred

Original auxiliary calculations, floating-point scans, campaign conclusions and author review history remain recoverable on the original branch. They are not fresh evidence for this landing. The original filename and claim identifier are retained for traceability; the present title and scope control.

## No-Go Discipline Gate

### N1 — Quantifiers and exceptions
Full coframe stress terms can occur at the same order as the local weight term. A mismatch with an explicitly restricted comparator is not a no-go for all field actions; leading matching does not prove a solution exists.

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
Full coframe stress terms can occur at the same order as the local weight term. A mismatch with an explicitly restricted comparator is not a no-go for all field actions; leading matching does not prove a solution exists.

### N8 — Earlier claims
This scoped result supersedes stronger wording in the original submission. It is a landing review, not an independent audit verdict.

## Falsifiers

A failure of a stated identity under its full hypotheses, or a different exact result for a specified finite example, would refute the corresponding result. An example outside those hypotheses does not.

## Imports

- [minimal_axioms](MINIMAL_AXIOMS_2026-06-29.md): repository boundary; it does not supply the amplitude dynamics below.
- [admissibility_rule_a_phase_timed_by_the_local_clock_every_packet_falls_towards_slow_clocks_force_is_energy_times_gradient_weight_and_inertia_tied_by_the_walk_bounded_theorem_note_2026-09-21](ADMISSIBILITY_RULE_A_PHASE_TIMED_BY_THE_LOCAL_CLOCK_EVERY_PACKET_FALLS_TOWARDS_SLOW_CLOCKS_FORCE_IS_ENERGY_TIMES_GRADIENT_WEIGHT_AND_INERTIA_TIED_BY_THE_WALK_BOUNDED_THEOREM_NOTE_2026-09-21.md): supplied mathematical construction from PR #8570; no premise adoption or retained grade is inferred.
- [admissibility_rule_what_the_walk_conserves_momentum_flows_on_bonds_relabellings_reach_second_neighbours_the_nearest_neighbour_frame_misses_by_two_differences_bounded_theorem_note_2026-09-21](ADMISSIBILITY_RULE_WHAT_THE_WALK_CONSERVES_MOMENTUM_FLOWS_ON_BONDS_RELABELLINGS_REACH_SECOND_NEIGHBOURS_THE_NEAREST_NEIGHBOUR_FRAME_MISSES_BY_TWO_DIFFERENCES_BOUNDED_THEOREM_NOTE_2026-09-21.md): supplied mathematical construction from PR #8593; no premise adoption or retained grade is inferred.
- [admissibility_rule_bond_strains_and_plaquette_curls_a_field_energy_per_local_tick_that_does_not_see_the_coins_axes_is_the_curvature_member_bounded_theorem_note_2026-09-21](ADMISSIBILITY_RULE_BOND_STRAINS_AND_PLAQUETTE_CURLS_A_FIELD_ENERGY_PER_LOCAL_TICK_THAT_DOES_NOT_SEE_THE_COINS_AXES_IS_THE_CURVATURE_MEMBER_BOUNDED_THEOREM_NOTE_2026-09-21.md): supplied mathematical construction from PR #8595; no premise adoption or retained grade is inferred.
- [admissibility_rule_the_fall_is_owed_by_the_ledger_a_field_energy_per_local_tick_requires_the_contents_stress_gradient_to_equal_its_weight_bounded_theorem_note_2026-09-21](ADMISSIBILITY_RULE_THE_FALL_IS_OWED_BY_THE_LEDGER_A_FIELD_ENERGY_PER_LOCAL_TICK_REQUIRES_THE_CONTENTS_STRESS_GRADIENT_TO_EQUAL_ITS_WEIGHT_BOUNDED_THEOREM_NOTE_2026-09-21.md): supplied mathematical construction from PR #8597; no premise adoption or retained grade is inferred.
- [admissibility_rule_reach_three_a_momentum_that_is_the_same_for_all_eight_species_gives_a_coupling_with_the_exact_current_and_one_geometry_for_all_bounded_theorem_note_2026-09-21](ADMISSIBILITY_RULE_REACH_THREE_A_MOMENTUM_THAT_IS_THE_SAME_FOR_ALL_EIGHT_SPECIES_GIVES_A_COUPLING_WITH_THE_EXACT_CURRENT_AND_ONE_GEOMETRY_FOR_ALL_BOUNDED_THEOREM_NOTE_2026-09-21.md): supplied mathematical construction from PR #8601; no premise adoption or retained grade is inferred.
- [admissibility_rule_the_eight_species_are_exchanged_by_site_signs_and_a_half_turn_of_the_coin_what_each_varying_field_becomes_bounded_theorem_note_2026-09-21](ADMISSIBILITY_RULE_THE_EIGHT_SPECIES_ARE_EXCHANGED_BY_SITE_SIGNS_AND_A_HALF_TURN_OF_THE_COIN_WHAT_EACH_VARYING_FIELD_BECOMES_BOUNDED_THEOREM_NOTE_2026-09-21.md): supplied mathematical construction from PR #8602; no premise adoption or retained grade is inferred.
- Standard mathematical definitions: finite-dimensional linear algebra, tensor products, spectral decompositions, exact rational arithmetic, differentiation and lattice shifts as explicitly used above.

## Review record

Original source: PR #8605 head `a57dbbaba2aca4607a5ece3a4247f4cc546d82af`, branch `physics-loop/admissibility-induced-law-block72-which-species-fall-the-ledger-owes-20260921`. The present revision narrows the mathematical domain and corrects the material issues recorded in its statements. Original ancillary science is deferred with recovery preserved. No audit verdict is applied.

## Verification

```bash
PYTHONPATH=scripts python3 scripts/admissibility_rule_which_species_fall_the_ledger_owes_reach_two_against_reach_three_2026_09_21.py
```

Expected: a zero exit code and a final `TOTAL` with `FAIL=0`.
