---
claim_id: admissibility_rule_the_walks_links_built_from_the_frame_carry_the_lengths_curvature_only_at_plaquette_reach_bounded_theorem_note_2026-09-23
claim_type: bounded_theorem
claim_scope: "Finite linked-operator covariance and rotation expansions; a stated four-parameter bond-symbol obstruction and a continuum linear curvature identity."
upstream_dependencies:
  - minimal_axioms
  - admissibility_rule_a_phase_timed_by_the_local_clock_every_packet_falls_towards_slow_clocks_force_is_energy_times_gradient_weight_and_inertia_tied_by_the_walk_bounded_theorem_note_2026-09-21
  - admissibility_rule_angles_are_the_tilt_of_the_coins_frame_with_them_two_disturbances_travel_at_one_direction_free_speed_and_the_price_is_a_conserved_stress_bounded_theorem_note_2026-09-21
  - admissibility_rule_bond_strains_and_plaquette_curls_a_field_energy_per_local_tick_that_does_not_see_the_coins_axes_is_the_curvature_member_bounded_theorem_note_2026-09-21
  - admissibility_rule_the_blind_walk_a_scalar_hop_weighted_by_the_twist_of_the_coin_along_the_bond_makes_a_varying_rotation_of_the_coin_axes_a_symmetry_bounded_theorem_note_2026-09-21
runner: scripts/admissibility_rule_the_walks_links_carry_the_lengths_curvature_only_at_plaquette_reach_2026_09_23.py
---

# Exact coin-link covariance and a linear curvature symbol

**Type:** bounded_theorem
**Status:** bounded-support; conditional supplied model, unaudited.

This note states conditional mathematics for explicitly supplied operators and fields. The stochastic, amplitude and field rules are not derived from the repository axioms, and no gravitational claim is made.
No bridge, Born-weight, plane-or-sum or gravity statement enters this note as a premise; this note does not fire wake condition 1 of the parked statistical-bridge decision.
Mathematical imports are stated explicitly with their hypotheses; none supplies a physical premise or an audit verdict.

## Premises and declared objects
For a directed bondx toy define its coefficientM_a(x)V_a(x)/(2i), withV inSU(2), and include the Hermitian adjoint reverse coefficient. This defines a finite Hermitian operator; on an infinite lattice use its formal finite-support expression unless a domain is supplied.
A frame is assumed nonsingular with a proper-rotation polar factor and symmetric stretch. A separate long-wavelength calculation takes symmetric small stretchs and commuting derivatives represented byik. This is not an exact finite-lattice geometry.

## Theorem T1 — exact link identities
Underpsi to Upsi, M to Ux M Ux^dagger andV to Ux V Uy^dagger, the bond product transforms to Ux M V Uy^dagger. Hence the whole finite operator is covariant.
ForM=Ux sigma_a Ux^dagger andV=Ux Uy^dagger, the operator is exactlyU H U^dagger. These pure-gauge links have identity holonomy around every closed loop; they do not themselves carry curvature.

## Theorem T2 — rotation expansion
ForUx=exp(-i theta_x.sigma/2), the bondUx sigma_a Uy^dagger has first-order part
[((theta_x+theta_y)/2) cross e_a].sigma+(i/2)(theta_y-theta_x)_a I,
and second-order part
(theta_x.sigma)sigma_a(theta_y.sigma)/4-(|theta_x|²+|theta_y|²)sigma_a/8.
The first-order scalar twist and its factor agree with the stated background-frame calculation. At a varying starting frameE_x, the scalar part is(i/2)E_x.(theta_y-theta_x), not the difference oftheta.E at the two ends.
This starting-end bond prescription does not equal the original endpoint-averaged anticommutator coupling for an arbitrary varying stretch.

## Theorem T3 — a specified bond-symbol class
Takeomega_a=ik_a L_a(s), with common cubic-covariant coefficients andL_a a linear map from symmetric matrices to vectors covariant under rotations fixing the directed axis. Its four components are
e_a cross(s e_a), s e_a, (tr s)e_a, and(e_a.s e_a)e_a.
The two-end linear rule that vanishes on uniform stretch has this leading-difference form. Substitution of a relabeling s=(i/2)(k xi^T+xi k^T) intoik_a omega_b-ik_b omega_a and equating all polynomial coefficients in the three planes forces all four coefficients tozero.
This is an obstruction in the displayed linear leading-symbol ansatz, not a classification of nonlinear rules or arbitrary higher-order effects.

## Theorem T4 — a curvature symbol with transverse derivatives
Setomega_a=-(ik) cross(s e_a). Its linear holonomyik_a omega_b-ik_b omega_a vanishes on the symmetric-gradient relabeling. The connectionomega itself generally changes by a gradient and is not invariant.
In plane(0,1), the normal holonomy component isk0²s11-2k0k1s01+k1²s00. Computing the linearized metric curvature for metricI+2s with the stated derivative and orientation convention gives the same expression. Alsoomega_a,c=-(1/2)sum_bd epsilon_cbd(ik_b s_da-ik_d s_ba).
These are continuum-symbol identities at first order in stretch. No exact nonlinearSU(2) plaquette equality, finite-lattice torsion-free completion, unique link rule or common matter dynamics is established.

## Historical experiments — deferred

Original auxiliary calculations, floating-point scans, campaign conclusions and author review history remain recoverable on the original branch. They are not fresh evidence for this landing. The original filename and claim identifier are retained for traceability; the present title and scope control.

## No-Go Discipline Gate

### N1 — Quantifiers and exceptions
Pure-gauge rotations have zero curvature. The nontrivial curvature result is a first-order continuum symbol; only its holonomy, not its connection, is relabeling invariant.

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
Pure-gauge rotations have zero curvature. The nontrivial curvature result is a first-order continuum symbol; only its holonomy, not its connection, is relabeling invariant.

### N8 — Earlier claims
This scoped result supersedes stronger wording in the original submission. It is a landing review, not an independent audit verdict.

## Falsifiers

A failure of a stated identity under its full hypotheses, or a different exact result for a specified finite example, would refute the corresponding result. An example outside those hypotheses does not.

## Imports

- [minimal_axioms](MINIMAL_AXIOMS_2026-06-29.md): repository boundary; it does not supply the mathematical model below.
- [admissibility_rule_a_phase_timed_by_the_local_clock_every_packet_falls_towards_slow_clocks_force_is_energy_times_gradient_weight_and_inertia_tied_by_the_walk_bounded_theorem_note_2026-09-21](ADMISSIBILITY_RULE_A_PHASE_TIMED_BY_THE_LOCAL_CLOCK_EVERY_PACKET_FALLS_TOWARDS_SLOW_CLOCKS_FORCE_IS_ENERGY_TIMES_GRADIENT_WEIGHT_AND_INERTIA_TIED_BY_THE_WALK_BOUNDED_THEOREM_NOTE_2026-09-21.md): supplied mathematical construction from PR #8570; no premise adoption or retained grade is inferred.
- [admissibility_rule_angles_are_the_tilt_of_the_coins_frame_with_them_two_disturbances_travel_at_one_direction_free_speed_and_the_price_is_a_conserved_stress_bounded_theorem_note_2026-09-21](ADMISSIBILITY_RULE_ANGLES_ARE_THE_TILT_OF_THE_COINS_FRAME_WITH_THEM_TWO_DISTURBANCES_TRAVEL_AT_ONE_DIRECTION_FREE_SPEED_AND_THE_PRICE_IS_A_CONSERVED_STRESS_BOUNDED_THEOREM_NOTE_2026-09-21.md): supplied mathematical construction from PR #8592; no premise adoption or retained grade is inferred.
- [admissibility_rule_bond_strains_and_plaquette_curls_a_field_energy_per_local_tick_that_does_not_see_the_coins_axes_is_the_curvature_member_bounded_theorem_note_2026-09-21](ADMISSIBILITY_RULE_BOND_STRAINS_AND_PLAQUETTE_CURLS_A_FIELD_ENERGY_PER_LOCAL_TICK_THAT_DOES_NOT_SEE_THE_COINS_AXES_IS_THE_CURVATURE_MEMBER_BOUNDED_THEOREM_NOTE_2026-09-21.md): supplied mathematical construction from PR #8595; no premise adoption or retained grade is inferred.
- [admissibility_rule_the_blind_walk_a_scalar_hop_weighted_by_the_twist_of_the_coin_along_the_bond_makes_a_varying_rotation_of_the_coin_axes_a_symmetry_bounded_theorem_note_2026-09-21](ADMISSIBILITY_RULE_THE_BLIND_WALK_A_SCALAR_HOP_WEIGHTED_BY_THE_TWIST_OF_THE_COIN_ALONG_THE_BOND_MAKES_A_VARYING_ROTATION_OF_THE_COIN_AXES_A_SYMMETRY_BOUNDED_THEOREM_NOTE_2026-09-21.md): supplied mathematical construction from PR #8596; no premise adoption or retained grade is inferred.
- Standard mathematical definitions: finite-dimensional linear algebra, tensor products, spectral decompositions, exact rational arithmetic, differentiation and lattice shifts as explicitly used above.

## Review record

Original source: PR #8941 head `26ad00872889164f5c8c5d3dc6b1ae586a6b7dbe`, branch `physics-loop/admissibility-induced-law-block107-the-walks-links-carry-the-lengths-curvature-20260923`. The present revision narrows the mathematical domain and corrects the material issues recorded in its statements. Original ancillary science is deferred with recovery preserved. No audit verdict is applied.

## Verification

```bash
PYTHONPATH=scripts python3 scripts/admissibility_rule_the_walks_links_carry_the_lengths_curvature_only_at_plaquette_reach_2026_09_23.py
```

Expected: a zero exit code and a final `TOTAL` with `FAIL=0`.
