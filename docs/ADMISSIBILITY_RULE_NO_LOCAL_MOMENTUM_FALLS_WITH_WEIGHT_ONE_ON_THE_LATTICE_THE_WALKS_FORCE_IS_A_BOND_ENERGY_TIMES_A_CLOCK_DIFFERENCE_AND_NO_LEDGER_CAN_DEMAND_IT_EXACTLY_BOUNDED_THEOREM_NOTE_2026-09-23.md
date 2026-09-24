---
claim_id: admissibility_rule_no_local_momentum_falls_with_weight_one_on_the_lattice_the_walks_force_is_a_bond_energy_times_a_clock_difference_and_no_ledger_can_demand_it_exactly_bounded_theorem_note_2026-09-23
claim_type: bounded_theorem
claim_scope: "Formal first-order band derivatives, exact finite-lattice bond identities and a restricted leading-force representation obstruction."
upstream_dependencies:
  - minimal_axioms
  - admissibility_rule_a_phase_timed_by_the_local_clock_every_packet_falls_towards_slow_clocks_force_is_energy_times_gradient_weight_and_inertia_tied_by_the_walk_bounded_theorem_note_2026-09-21
  - admissibility_rule_what_the_walk_conserves_momentum_flows_on_bonds_relabellings_reach_second_neighbours_the_nearest_neighbour_frame_misses_by_two_differences_bounded_theorem_note_2026-09-21
  - admissibility_rule_bond_strains_and_plaquette_curls_a_field_energy_per_local_tick_that_does_not_see_the_coins_axes_is_the_curvature_member_bounded_theorem_note_2026-09-21
  - admissibility_rule_the_fall_is_owed_by_the_ledger_a_field_energy_per_local_tick_requires_the_contents_stress_gradient_to_equal_its_weight_bounded_theorem_note_2026-09-21
  - admissibility_rule_which_species_fall_the_ledger_owes_under_reach_two_a_reflected_species_has_minus_its_weight_under_reach_three_all_eight_agree_bounded_theorem_note_2026-09-21
runner: scripts/admissibility_rule_no_local_momentum_falls_with_weight_one_on_the_lattice_2026_09_23.py
---

# Periodic momentum weights and exact bond-force identities

**Type:** bounded_theorem
**Status:** bounded-support; conditional supplied model, unaudited.

This note states conditional mathematics for explicitly supplied operators and fields. The stochastic, amplitude and field rules are not derived from the repository axioms, and no gravitational claim is made.
No bridge, Born-weight, plane-or-sum or gravity statement enters this note as a premise; this note does not fire wake condition 1 of the parked statistical-bridge decision.
Mathematical imports are stated explicitly with their hypotheses; none supplies a physical premise or an audit verdict.

## Premises and declared objects
Supply the nearest-neighbor two-componentH=sum sigma_j S_j, clock rootphi>0, andH_w=phi H phi. Letchi=H(phi psi), rho_x=Re psi_x^dagger chi_x ande_x=phi_x rho_x.
DefineC_j[v]psi_x=[v_x psi_(x+e_j)+v_(x-e_j)psi_(x-e_j)]/2 andd_jphi=phi_(x+e_j)-phi_x. The force expression studied is
f_j(x)=Re[(C_j[dphi]psi)_x^dagger chi_x+psi_x^dagger(C_j[dphi]chi)_x].
These are supplied algebraic observables. Finite periodic systems avoid domain questions; infinite identities are formal on finite support.

## Theorem T1 — a periodic-band obstruction
LetP be finite-reach, translation-invariant, Hermitian and commuting withH. Away from band degeneracies, its eigenvaluepbar(k) is periodic and the band expectation ofpartial_k P equalspartial_k pbar, by differentiating the eigenvector equation. The shift commutator[X,T_n]=nT_n then gives a formal first-order uniform-clock-gradient coefficient-E grad u.grad_k pbar.
This is a symbol/local-density expansion: an infinite plane wave is not normalized and an affine positive-clock expansion is not a global positive field.
Along a closed momentum line avoiding band nodes, the integral ofpartial_j pbar iszero. It therefore cannot be identically1. Examples arecos k forsin k, cos2k forsin k cos k, and(4/3)cos k-(1/3)cos2k for the normalized fourth-order stencil. Arbitrary momenta need not have unit low-k normalization.

## Theorem T2 — exact bond form
Setepsilon_j(x)=Re[psi_(x+e_j)^dagger chi_x+psi_x^dagger chi_(x+e_j)]/2. ExpandingC gives
f_j(x)=d_jphi(x)epsilon_j(x)+d_jphi(x-e_j)epsilon_j(x-e_j).
Alsoepsilon_b=(rho_x+rho_y)/2-Re[(psi_y-psi_x)^dagger(chi_y-chi_x)]/2.
The identitydphi=Lambda d(log w)/2 uses the logarithmic mean ofphi endpoints, with its continuous equal-endpoint value. Thus the remainder involves bond information not fixed by site energy alone.
On a bipartite lattice a state on one sublattice has site energyzero; the supplied finite example has nonzero force. ParityGamma anticommutes withH_w, sends e toe's negative and keepsf unchanged. These parity statements require even torus sides; the bond identity itself holds on odd tori too.

## Theorem T3 — limited ledger implications
A differentiable functional of plaquette curls, withw held fixed as site multipliers, is invariant underB to B+d xi. Summation by parts givesdiv E=0. A separate sourced equationdiv E=f would then requiref=0; this is not a theorem forbidding all forces in arbitrary dynamics.
ForF=c0 sum w det(I-B), the specified upwind variation ofu cancels theB variation atB=0. This is a first-variation identity, not a completed nonlinear invariance proof.
At first order inphi=1+epsilon eta, two selected plane wavesk=(pi/2,0,0) and(0,pi/2,0), eachenergy1 and spinor norm²2, have the same UNPERTURBED energy density2 and the stated unperturbed momentum currentszero. Their leading forces alongaxis1 differ: one iszero, the other is proportional toeta_(x+e1)-eta_(x-e1).
This excludes a leading-force formula determined only by those unperturbed fields and a common supplied clock-gradient coefficient. It does not exclude functionals of perturbed densities, additional bond variables, their derivatives or nonlocal information.

## Theorem T4 — two-step momentum
P_j=S_j C_j has reach2. Its clock commutator isi[phi,P_j]=-C_j^(2)[d_j^(2)phi]/2. Combining it withH gives a reach-three force and the same bond formula with overall1/2 and step2. Its first-order plane-wave factor iscos2k_j with centered log-clock difference divided by4.
The48 selected energy-plus-or-minus-one fixtures on the8-torus give a nonzero test; they are not an enumeration of every momentum on that torus.

## Historical experiments — deferred

Original auxiliary calculations, floating-point scans, campaign conclusions and author review history remain recoverable on the original branch. They are not fresh evidence for this landing. The original filename and claim identifier are retained for traceability; the present title and scope control.

## No-Go Discipline Gate

### N1 — Quantifiers and exceptions
Band derivatives are formal first-order coefficients, and parity needs bipartiteness. The equal-unperturbed-data example excludes a restricted representation class, not every possible ledger.

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
Band derivatives are formal first-order coefficients, and parity needs bipartiteness. The equal-unperturbed-data example excludes a restricted representation class, not every possible ledger.

### N8 — Earlier claims
This scoped result supersedes stronger wording in the original submission. It is a landing review, not an independent audit verdict.

## Falsifiers

A failure of a stated identity under its full hypotheses, or a different exact result for a specified finite example, would refute the corresponding result. An example outside those hypotheses does not.

## Imports

- [minimal_axioms](MINIMAL_AXIOMS_2026-06-29.md): repository boundary; it does not supply the mathematical model below.
- [admissibility_rule_a_phase_timed_by_the_local_clock_every_packet_falls_towards_slow_clocks_force_is_energy_times_gradient_weight_and_inertia_tied_by_the_walk_bounded_theorem_note_2026-09-21](ADMISSIBILITY_RULE_A_PHASE_TIMED_BY_THE_LOCAL_CLOCK_EVERY_PACKET_FALLS_TOWARDS_SLOW_CLOCKS_FORCE_IS_ENERGY_TIMES_GRADIENT_WEIGHT_AND_INERTIA_TIED_BY_THE_WALK_BOUNDED_THEOREM_NOTE_2026-09-21.md): supplied mathematical construction from PR #8570; no premise adoption or retained grade is inferred.
- [admissibility_rule_what_the_walk_conserves_momentum_flows_on_bonds_relabellings_reach_second_neighbours_the_nearest_neighbour_frame_misses_by_two_differences_bounded_theorem_note_2026-09-21](ADMISSIBILITY_RULE_WHAT_THE_WALK_CONSERVES_MOMENTUM_FLOWS_ON_BONDS_RELABELLINGS_REACH_SECOND_NEIGHBOURS_THE_NEAREST_NEIGHBOUR_FRAME_MISSES_BY_TWO_DIFFERENCES_BOUNDED_THEOREM_NOTE_2026-09-21.md): supplied mathematical construction from PR #8593; no premise adoption or retained grade is inferred.
- [admissibility_rule_bond_strains_and_plaquette_curls_a_field_energy_per_local_tick_that_does_not_see_the_coins_axes_is_the_curvature_member_bounded_theorem_note_2026-09-21](ADMISSIBILITY_RULE_BOND_STRAINS_AND_PLAQUETTE_CURLS_A_FIELD_ENERGY_PER_LOCAL_TICK_THAT_DOES_NOT_SEE_THE_COINS_AXES_IS_THE_CURVATURE_MEMBER_BOUNDED_THEOREM_NOTE_2026-09-21.md): supplied mathematical construction from PR #8595; no premise adoption or retained grade is inferred.
- [admissibility_rule_the_fall_is_owed_by_the_ledger_a_field_energy_per_local_tick_requires_the_contents_stress_gradient_to_equal_its_weight_bounded_theorem_note_2026-09-21](ADMISSIBILITY_RULE_THE_FALL_IS_OWED_BY_THE_LEDGER_A_FIELD_ENERGY_PER_LOCAL_TICK_REQUIRES_THE_CONTENTS_STRESS_GRADIENT_TO_EQUAL_ITS_WEIGHT_BOUNDED_THEOREM_NOTE_2026-09-21.md): supplied mathematical construction from PR #8597; no premise adoption or retained grade is inferred.
- [admissibility_rule_which_species_fall_the_ledger_owes_under_reach_two_a_reflected_species_has_minus_its_weight_under_reach_three_all_eight_agree_bounded_theorem_note_2026-09-21](ADMISSIBILITY_RULE_WHICH_SPECIES_FALL_THE_LEDGER_OWES_UNDER_REACH_TWO_A_REFLECTED_SPECIES_HAS_MINUS_ITS_WEIGHT_UNDER_REACH_THREE_ALL_EIGHT_AGREE_BOUNDED_THEOREM_NOTE_2026-09-21.md): supplied mathematical construction from PR #8605; no premise adoption or retained grade is inferred.
- Standard mathematical definitions: finite-dimensional linear algebra, tensor products, spectral decompositions, exact rational arithmetic, differentiation and lattice shifts as explicitly used above.

## Review record

Original source: PR #8939 head `b8a4e01b96d95638866a503384757084d9103247`, branch `physics-loop/admissibility-induced-law-block106-no-local-momentum-falls-with-weight-one-20260923`. The present revision narrows the mathematical domain and corrects the material issues recorded in its statements. Original ancillary science is deferred with recovery preserved. No audit verdict is applied.

## Verification

```bash
PYTHONPATH=scripts python3 scripts/admissibility_rule_no_local_momentum_falls_with_weight_one_on_the_lattice_2026_09_23.py
```

Expected: a zero exit code and a final `TOTAL` with `FAIL=0`.
