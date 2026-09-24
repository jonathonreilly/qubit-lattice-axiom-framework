---
claim_id: admissibility_rule_the_filled_seas_energy_as_the_ledgers_field_term_a_chessboard_of_clocks_is_invisible_the_sea_induces_a_clock_stiffness_not_the_curvature_member_bounded_theorem_note_2026-09-22
claim_type: bounded_theorem
claim_scope: "Finite supplied Hermitian hopping models: reciprocal bipartite clock factors leave opposite-parity hopping unchanged; the traceless reach-two family has an even negative-level energy. Free antisymmetric-state one-body expectations are additive. A separately declared quadratic comparator has the stated local response signs; it is not the exact sea Hessian. No induced stiffness, force or field-model exclusion is established."
upstream_dependencies:
  - minimal_axioms
  - admissibility_rule_a_phase_timed_by_the_local_clock_every_packet_falls_towards_slow_clocks_force_is_energy_times_gradient_weight_and_inertia_tied_by_the_walk_bounded_theorem_note_2026-09-21
  - admissibility_rule_action_and_reaction_the_rate_fields_source_is_the_amplitudes_energy_density_matched_pulls_and_a_kept_ledger_fix_the_clock_laws_second_order_bounded_theorem_note_2026-09-21
  - admissibility_rule_what_the_walk_conserves_momentum_flows_on_bonds_relabellings_reach_second_neighbours_the_nearest_neighbour_frame_misses_by_two_differences_bounded_theorem_note_2026-09-21
  - admissibility_rule_reach_three_a_momentum_that_is_the_same_for_all_eight_species_gives_a_coupling_with_the_exact_current_and_one_geometry_for_all_bounded_theorem_note_2026-09-21
  - admissibility_rule_the_eight_species_are_exchanged_by_site_signs_and_a_half_turn_of_the_coin_what_each_varying_field_becomes_bounded_theorem_note_2026-09-21
  - admissibility_rule_amplitudes_of_negative_energy_fall_like_the_others_and_source_the_opposite_field_a_negative_body_at_rest_has_a_largest_size_bounded_theorem_note_2026-09-21
runner: scripts/admissibility_rule_the_filled_seas_energy_as_the_ledgers_field_term_chessboard_clocks_invisible_2026_09_22.py
---

# Filled negative-level energy: hopping invariance, spectral evenness and additive free-particle sources

**Type:** bounded_theorem
**Status:** bounded-support; conditional supplied model, unaudited.

This note states conditional mathematics for explicitly supplied operators and fields. The amplitude dynamics and composition rules are not derived from the repository axioms, and no gravitational claim is made.
No bridge, Born-weight, plane-or-sum or gravity statement enters this note as a premise; this note does not fire wake condition 1 of the parked statistical-bridge decision.
No value, constant or theorem is imported as authority; the standard mathematical imports are named at definition level.

## Premises and declared objects

Use a finite even torus and the supplied Hermitian free walk H with only opposite-parity hopping and no on-site term. Let phi_x>0, w_x=phi_x^2 and H_w=phi H phi. The filled negative-level energy is E_-=sum_{lambda<0}lambda of this finite matrix. Filling and free antisymmetric composition are mathematical choices. Site-plus-coin antisymmetry permits two opposite-coin particles at one site; it does not impose exclusion of all double occupancy.

## Theorem T1 — reciprocal clock invariance

Let eps_x=(-1)^(x+y+z). For c>0 replace phi_x by phi_x c^eps_x. Every nonzero opposite-parity matrix element carries a factor c^(eps_x+eps_y)=1. Thus H_w, its spectrum and E_- are unchanged, including for nonuniform initial phi. In log rates u=2 log phi this is an exact translation invariance along eps.

This does not apply to a general reach-two strain term: that term has even-displacement entries. It also does not apply to on-site energy terms. At a point where E_- has a Hessian in u, that Hessian annihilates eps. Without differentiability, only the exact invariance is asserted.

## Theorem T2 — spectral evenness

For the supplied finite reach-two family H2[B], the unitary checkerboard map U obeys U H2[B] U=-H2[-B] and tr H2[B]=0. Spectral reversal therefore gives
`E_-(H2[-B])=-sum_{lambda>0}lambda=E_-(H2[B])`.
This evenness is exact for real supplied strain fields. A first derivative at B=0 is zero only if it exists. Evenness alone allows a cusp at zero eigenvalues: the matrix diag(t,-t) has negative-level energy -|t|. No smooth response coefficient is inferred from symmetry alone.

## Theorem T3 — free antisymmetric expectations

For two nonzero orthogonal vectors psi1,psi2 and Psi=psi1 tensor psi2-psi2 tensor psi1, any one-body operator O gives
`<Psi|(O tensor I+I tensor O)|Psi>/<Psi|Psi> = <O>_1+<O>_2`.
Expand the tensor product: cross terms contain the vanishing overlap and the norm is twice the product of individual squared norms. The same calculation applies to each local energy operator {P_x,H_w}/2 and extends to a finite exterior product of orthogonal states. Removing one occupied orbital changes its source by minus that orbital's density. For an eigenvector with eigenvalue lambda<0, e_x=lambda||psi_x||^2/||psi||^2<=0, so this removal is nonnegative at every site and positive in total. An arbitrary state of negative energy expectation guarantees only positive total removal energy.

The runner uses an eight-site ring for the exact phase exp(-i pi x/2), so its negative eigenvalue identity holds at every site including the periodic boundary. No claim about an interacting projected state or a physically supplied filling rule follows.

## Theorem T4 — a distinct quadratic comparator

Define, independently of the exact E_-, a mean-zero linear equation with mode denominators c+kappa L(q), where L(q)=sum_j 2(1-cos q_j), kappa>0, c<0 and c+12kappa<0. For a mean-subtracted unit source on a finite three-dimensional torus,
`u(0)=-(1/V)sum_{q!=0}1/(c+kappa L(q))>0`.
For c=0 the same expression is negative. This follows by the sign of every denominator. The runner checks the declared rational inputs c=-1193/1000 and kappa=95/1000 on a four-sided torus. They are inputs, not derived sea coefficients. The local sign of u alone proves no interbody force or acceleration law.

The comparator cannot equal the exact sea Hessian at all momenta: its checkerboard denominator is c+12kappa, whereas T1 requires a checkerboard null direction wherever the Hessian exists. An exact Hessian equation A u=-j requires sum_x eps_x j_x=0. A mean-subtracted point source violates this condition on an even torus, so that exact equation has no solution for this source. For compatible sources, the checkerboard component remains undetermined if a solution exists. There is no universal field-induction no-go here.

## Historical experiments — deferred

Original auxiliary calculations, floating-point scans, campaign conclusions and author review history remain recoverable on the original branch. They are not fresh evidence for this landing. The original filename and claim identifier are retained for traceability; the present title and scope control.

## No-Go Discipline Gate

### N1 — Quantifiers and exceptions
Reciprocal invisibility requires opposite-parity hopping. Even spectral energy need not be differentiable. Free-state additivity does not supply site exclusion. A fitted low-momentum comparator cannot be substituted for the full exact Hessian.

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
Reciprocal invisibility requires opposite-parity hopping. Even spectral energy need not be differentiable. Free-state additivity does not supply site exclusion. A fitted low-momentum comparator cannot be substituted for the full exact Hessian.

### N8 — Earlier claims
This scoped result supersedes stronger wording in the original submission. It is a landing review, not an independent audit verdict.

## Falsifiers

A failure of a stated identity under its full hypotheses, or a different exact result for a specified finite example, would refute the corresponding result. An example outside those hypotheses does not.

## Imports

- [minimal_axioms](MINIMAL_AXIOMS_2026-06-29.md): repository boundary; it does not supply the amplitude dynamics below.
- [admissibility_rule_a_phase_timed_by_the_local_clock_every_packet_falls_towards_slow_clocks_force_is_energy_times_gradient_weight_and_inertia_tied_by_the_walk_bounded_theorem_note_2026-09-21](ADMISSIBILITY_RULE_A_PHASE_TIMED_BY_THE_LOCAL_CLOCK_EVERY_PACKET_FALLS_TOWARDS_SLOW_CLOCKS_FORCE_IS_ENERGY_TIMES_GRADIENT_WEIGHT_AND_INERTIA_TIED_BY_THE_WALK_BOUNDED_THEOREM_NOTE_2026-09-21.md): supplied mathematical construction from PR #8570; no premise adoption or retained grade is inferred.
- [admissibility_rule_action_and_reaction_the_rate_fields_source_is_the_amplitudes_energy_density_matched_pulls_and_a_kept_ledger_fix_the_clock_laws_second_order_bounded_theorem_note_2026-09-21](ADMISSIBILITY_RULE_ACTION_AND_REACTION_THE_RATE_FIELDS_SOURCE_IS_THE_AMPLITUDES_ENERGY_DENSITY_MATCHED_PULLS_AND_A_KEPT_LEDGER_FIX_THE_CLOCK_LAWS_SECOND_ORDER_BOUNDED_THEOREM_NOTE_2026-09-21.md): supplied mathematical construction from PR #8571; no premise adoption or retained grade is inferred.
- [admissibility_rule_what_the_walk_conserves_momentum_flows_on_bonds_relabellings_reach_second_neighbours_the_nearest_neighbour_frame_misses_by_two_differences_bounded_theorem_note_2026-09-21](ADMISSIBILITY_RULE_WHAT_THE_WALK_CONSERVES_MOMENTUM_FLOWS_ON_BONDS_RELABELLINGS_REACH_SECOND_NEIGHBOURS_THE_NEAREST_NEIGHBOUR_FRAME_MISSES_BY_TWO_DIFFERENCES_BOUNDED_THEOREM_NOTE_2026-09-21.md): supplied mathematical construction from PR #8593; no premise adoption or retained grade is inferred.
- [admissibility_rule_reach_three_a_momentum_that_is_the_same_for_all_eight_species_gives_a_coupling_with_the_exact_current_and_one_geometry_for_all_bounded_theorem_note_2026-09-21](ADMISSIBILITY_RULE_REACH_THREE_A_MOMENTUM_THAT_IS_THE_SAME_FOR_ALL_EIGHT_SPECIES_GIVES_A_COUPLING_WITH_THE_EXACT_CURRENT_AND_ONE_GEOMETRY_FOR_ALL_BOUNDED_THEOREM_NOTE_2026-09-21.md): supplied mathematical construction from PR #8601; no premise adoption or retained grade is inferred.
- [admissibility_rule_the_eight_species_are_exchanged_by_site_signs_and_a_half_turn_of_the_coin_what_each_varying_field_becomes_bounded_theorem_note_2026-09-21](ADMISSIBILITY_RULE_THE_EIGHT_SPECIES_ARE_EXCHANGED_BY_SITE_SIGNS_AND_A_HALF_TURN_OF_THE_COIN_WHAT_EACH_VARYING_FIELD_BECOMES_BOUNDED_THEOREM_NOTE_2026-09-21.md): supplied mathematical construction from PR #8602; no premise adoption or retained grade is inferred.
- [admissibility_rule_amplitudes_of_negative_energy_fall_like_the_others_and_source_the_opposite_field_a_negative_body_at_rest_has_a_largest_size_bounded_theorem_note_2026-09-21](ADMISSIBILITY_RULE_AMPLITUDES_OF_NEGATIVE_ENERGY_FALL_LIKE_THE_OTHERS_AND_SOURCE_THE_OPPOSITE_FIELD_A_NEGATIVE_BODY_AT_REST_HAS_A_LARGEST_SIZE_BOUNDED_THEOREM_NOTE_2026-09-21.md): supplied mathematical construction from PR #8603; no premise adoption or retained grade is inferred.
- Standard mathematical definitions: finite-dimensional linear algebra, tensor products, spectral decompositions, exact rational arithmetic, differentiation and lattice shifts as explicitly used above.

## Review record

Original source: PR #8611 head `2fc37b9f66dd04517137a7addadfeeb7f416d114`, branch `physics-loop/admissibility-induced-law-block76-the-filled-seas-energy-as-the-ledgers-field-term-20260922`. The present revision narrows the mathematical domain and corrects the material issues recorded in its statements. Original ancillary science is deferred with recovery preserved. No audit verdict is applied.

## Verification

```bash
PYTHONPATH=scripts python3 scripts/admissibility_rule_the_filled_seas_energy_as_the_ledgers_field_term_chessboard_clocks_invisible_2026_09_22.py
```

Expected: a zero exit code and a final `TOTAL` with `FAIL=0`.
