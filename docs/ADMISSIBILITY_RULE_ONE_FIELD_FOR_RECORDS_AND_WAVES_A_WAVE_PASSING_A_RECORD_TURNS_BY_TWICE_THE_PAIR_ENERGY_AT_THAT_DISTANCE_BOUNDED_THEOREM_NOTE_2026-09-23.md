---
claim_id: admissibility_rule_one_field_for_records_and_waves_a_wave_passing_a_record_turns_by_twice_the_pair_energy_at_that_distance_bounded_theorem_note_2026-09-23
claim_type: bounded_theorem
claim_scope: "Exact mean-zero torus line sums and a weak-field continuum transverse integral; no universal identification with measured pair correlations."
upstream_dependencies:
  - minimal_axioms
  - admissibility_rule_records_that_move_on_their_own_clocks_and_slow_the_clocks_around_them_attract_with_a_one_over_r_potential_equal_both_ways_bounded_theorem_note_2026-09-23
  - admissibility_rule_a_record_that_cannot_read_the_field_from_its_own_motion_hops_on_its_own_clock_and_with_kept_books_records_attract_bounded_theorem_note_2026-09-23
  - admissibility_rule_no_master_clock_a_neighbour_determined_scale_covariant_tick_rate_obeys_the_lattice_laplace_equation_records_enter_as_additive_sources_bounded_theorem_note_2026-09-21
  - admissibility_rule_a_phase_timed_by_the_local_clock_every_packet_falls_towards_slow_clocks_force_is_energy_times_gradient_weight_and_inertia_tied_by_the_walk_bounded_theorem_note_2026-09-21
runner: scripts/admissibility_rule_one_field_for_records_and_waves_wave_turns_by_twice_the_pair_energy_2026_09_23.py
---

# Torus line sums and a supplied continuum ray integral

**Type:** bounded_theorem
**Status:** bounded-support; conditional supplied model, unaudited.

This note states conditional mathematics for explicitly supplied operators and fields. The stochastic, amplitude and field rules are not derived from the repository axioms, and no gravitational claim is made.
No bridge, Born-weight, plane-or-sum or gravity statement enters this note as a premise; this note does not fire wake condition 1 of the parked statistical-bridge decision.
Mathematical imports are stated explicitly with their hypotheses; none supplies a physical premise or an audit verdict.

## Premises and declared objects
On a simple periodic cubic lattice let G_d be the mean-zero inverse of2dI-Adj. Separately supply a continuum profile u(x,y)=6lambda/[4pi sqrt(x²+y²)], lambda<0, and a weak-field unit-speed ray moving alongx with impact parameter b>0. The continuum profile is not inferred here from a finite-torus fit. The ray model is conditional and not an exact quantum packet law.

## Theorem T1 — line sums
On a side-L torus, sum_x G_3(x,y,z)=G_2(y,z). A sum along the periodic coordinate kills every nonzero longitudinal mode; the remaining normalization is L/L³=1/L² and denominator is the plane Laplacian symbol. Both kernels have their constant mode removed. The runner verifies the identity for L=4,6 and the defining plane equation.

## Theorem T2 — supplied continuum integral
For b>0, integral over realx of partial_b[1/(4pi sqrt(x²+b²))] is -1/(2pi b). Substitute x=b t and integrate (1+t²)^(-3/2), whose antiderivative is t/sqrt(1+t²). Consequently the first-order transverse kick -integral partial_b u dx is3lambda/(pi b), directed toward the source. Its magnitude is2|U(b)| if U(b) is DEFINED to equal6lambda/(4pi b).

## Theorem T3 — ray scope and normalization
For epsilon(k)=sqrt(sum sin²k_j), Hess(epsilon²/2)=diag(cos2k_j). Its limiting tensor isI and the axial nonzero-k speed tends to1. The branch velocity is not differentiable as a vector at k=0 itself.
The supplied ray law is v'=-w²Hess(epsilon²/2)grad u+2(v.grad u)v. At weak field on an unperturbed axial ray, the second term is longitudinal at first order; its transverse component is second order. It is incorrect to call the entire term second order.

Writing g_weight(b)=exp[-U(b)] gives the algebraic identity |kick|=2log g_weight(b). This is an unnormalized weight, not a measured many-body pair correlation. In the separate two-record finite-torus model with W=1, probabilities PER OFFSET obey p(d)/p(d0)=exp[-U(d)+U(d0)]; shell counts need degeneracy factors. There is no generic equality between g_weight and a normalized pair excess, no finite-torus infinite-distance limit, and no nonlinear bending or changed-length result here.

## Historical experiments — deferred

Original auxiliary calculations, floating-point scans, campaign conclusions and author review history remain recoverable on the original branch. They are not fresh evidence for this landing. The original filename and claim identifier are retained for traceability; the present title and scope control.

## No-Go Discipline Gate

### N1 — Quantifiers and exceptions
Keep the torus identity, independently supplied continuum profile and weak-field ray calculation separate. Pair-weight normalization and transverse projection are essential.

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
Keep the torus identity, independently supplied continuum profile and weak-field ray calculation separate. Pair-weight normalization and transverse projection are essential.

### N8 — Earlier claims
This scoped result supersedes stronger wording in the original submission. It is a landing review, not an independent audit verdict.

## Falsifiers

A failure of a stated identity under its full hypotheses, or a different exact result for a specified finite example, would refute the corresponding result. An example outside those hypotheses does not.

## Imports

- [minimal_axioms](MINIMAL_AXIOMS_2026-06-29.md): repository boundary; it does not supply the mathematical model below.
- [admissibility_rule_records_that_move_on_their_own_clocks_and_slow_the_clocks_around_them_attract_with_a_one_over_r_potential_equal_both_ways_bounded_theorem_note_2026-09-23](ADMISSIBILITY_RULE_RECORDS_THAT_MOVE_ON_THEIR_OWN_CLOCKS_AND_SLOW_THE_CLOCKS_AROUND_THEM_ATTRACT_WITH_A_ONE_OVER_R_POTENTIAL_EQUAL_BOTH_WAYS_BOUNDED_THEOREM_NOTE_2026-09-23.md): supplied mathematical construction from PR #8860; no premise adoption or retained grade is inferred.
- [admissibility_rule_a_record_that_cannot_read_the_field_from_its_own_motion_hops_on_its_own_clock_and_with_kept_books_records_attract_bounded_theorem_note_2026-09-23](ADMISSIBILITY_RULE_A_RECORD_THAT_CANNOT_READ_THE_FIELD_FROM_ITS_OWN_MOTION_HOPS_ON_ITS_OWN_CLOCK_AND_WITH_KEPT_BOOKS_RECORDS_ATTRACT_BOUNDED_THEOREM_NOTE_2026-09-23.md): supplied mathematical construction from PR #8872; no premise adoption or retained grade is inferred.
- [admissibility_rule_no_master_clock_a_neighbour_determined_scale_covariant_tick_rate_obeys_the_lattice_laplace_equation_records_enter_as_additive_sources_bounded_theorem_note_2026-09-21](ADMISSIBILITY_RULE_NO_MASTER_CLOCK_A_NEIGHBOUR_DETERMINED_SCALE_COVARIANT_TICK_RATE_OBEYS_THE_LATTICE_LAPLACE_EQUATION_RECORDS_ENTER_AS_ADDITIVE_SOURCES_BOUNDED_THEOREM_NOTE_2026-09-21.md): supplied mathematical construction from PR #8568; no premise adoption or retained grade is inferred.
- [admissibility_rule_a_phase_timed_by_the_local_clock_every_packet_falls_towards_slow_clocks_force_is_energy_times_gradient_weight_and_inertia_tied_by_the_walk_bounded_theorem_note_2026-09-21](ADMISSIBILITY_RULE_A_PHASE_TIMED_BY_THE_LOCAL_CLOCK_EVERY_PACKET_FALLS_TOWARDS_SLOW_CLOCKS_FORCE_IS_ENERGY_TIMES_GRADIENT_WEIGHT_AND_INERTIA_TIED_BY_THE_WALK_BOUNDED_THEOREM_NOTE_2026-09-21.md): supplied mathematical construction from PR #8570; no premise adoption or retained grade is inferred.
- Standard mathematical definitions: finite-dimensional linear algebra, tensor products, spectral decompositions, exact rational arithmetic, differentiation and lattice shifts as explicitly used above.

## Review record

Original source: PR #8878 head `6672f80380772bc01bbeda5a1cd7cf6db2d456c0`, branch `physics-loop/admissibility-induced-law-block98-one-field-for-records-and-waves-20260923`. The present revision narrows the mathematical domain and corrects the material issues recorded in its statements. Original ancillary science is deferred with recovery preserved. No audit verdict is applied.

## Verification

```bash
PYTHONPATH=scripts python3 scripts/admissibility_rule_one_field_for_records_and_waves_wave_turns_by_twice_the_pair_energy_2026_09_23.py
```

Expected: a zero exit code and a final `TOTAL` with `FAIL=0`.
