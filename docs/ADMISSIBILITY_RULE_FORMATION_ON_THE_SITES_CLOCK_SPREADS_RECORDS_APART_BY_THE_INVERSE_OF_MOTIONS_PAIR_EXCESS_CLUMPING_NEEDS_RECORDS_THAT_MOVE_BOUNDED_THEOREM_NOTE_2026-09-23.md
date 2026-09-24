---
claim_id: admissibility_rule_formation_on_the_sites_clock_spreads_records_apart_by_the_inverse_of_motions_pair_excess_clumping_needs_records_that_move_bounded_theorem_note_2026-09-23
claim_type: bounded_theorem
claim_scope: "Separate birth and fixed-count motion models: inverse two-record weights, order-independent rate products, order-dependent probabilities and finite first-order normalizers."
upstream_dependencies:
  - minimal_axioms
  - admissibility_rule_records_that_move_on_their_own_clocks_and_slow_the_clocks_around_them_attract_with_a_one_over_r_potential_equal_both_ways_bounded_theorem_note_2026-09-23
  - admissibility_rule_a_record_that_cannot_read_the_field_from_its_own_motion_hops_on_its_own_clock_and_with_kept_books_records_attract_bounded_theorem_note_2026-09-23
  - admissibility_rule_no_master_clock_a_neighbour_determined_scale_covariant_tick_rate_obeys_the_lattice_laplace_equation_records_enter_as_additive_sources_bounded_theorem_note_2026-09-21
runner: scripts/admissibility_rule_formation_on_the_sites_clock_spreads_records_apart_clumping_needs_records_that_move_2026_09_23.py
---

# Sequential formation weights and their configuration-dependent normalizers

**Type:** bounded_theorem
**Status:** bounded-support; conditional supplied model, unaudited.

This note states conditional mathematics for explicitly supplied operators and fields. The stochastic, amplitude and field rules are not derived from the repository axioms, and no gravitational claim is made.
No bridge, Born-weight, plane-or-sum or gravity statement enters this note as a premise; this note does not fire wake condition 1 of the parked statistical-bridge decision.
Mathematical imports are stated explicitly with their hypotheses; none supplies a physical premise or an audit verdict.

## Premises and declared objects
Use the neutralized mean-zero torus field u_y(C)=6lambda sum_{r in C}G(y-r), with lambda real and positive activity z. A birth at an empty site has rate z exp u_y(C), with no motion during this sequential experiment. Contents do not change its total rate. Separately compare W=1 departure-clock motion at fixed count from PR8860. These are supplied dynamics, not an axiom-selected formation law.

## Theorem T1 — two-record weights
After one record at0, the next offset has probability exp U(d)/Zplus, d!=0, with U=6lambda G. Fixed-count two-record motion instead has per-offset stationary probability exp[-U(d)]/Zminus. The UNNORMALIZED weights multiply to1; normalized probabilities multiply to1/(Zplus Zminus).

## Theorem T2 — products are not probabilities
For distinct sites x1,...,xn, the product of birth rates along any order is z^n exp[sum_unordered_pairs U(r-s)]. Every pair enters exactly once, when its later site is filled; evenness removes orientation.
Actual ordered probabilities also divide by Z(C)=sum_{y notin C}exp u_y(C) at every intermediate set. These denominators depend on the partial configurations. Thus ordered probabilities are generally unequal, and the law of the final set is not generally proportional to the rate product.
On a fixed finite torus, power-series expansion and sum_y G(y-r)=0 give
Z(C)=V-n-6lambda[nG(0)+2sum_pairs G(r-s)]+O(lambda²).
The remainder is at fixed C and V. Low density alone provides no uniform bound in lambda or volume and does not justify dropping path-dependent normalizers.

## Theorem T3 — a finite preference
On L=4, G(1,0,0)>G(2,2,2). For lambda<0 the next birth is less likely at the first offset, while the stationary two-record motion has the opposite ratio. This is a two-offset comparison, not a no-clustering theorem for sequential many-record growth.
On any fixed finite torus with positive birth rates and no removal, full occupancy is absorbing and reached almost surely: there are finitely many births, each with positive finite total rate. No nontrivial stationary spread law or necessity of motion for physical clustering follows.

## Historical experiments — deferred

Original auxiliary calculations, floating-point scans, campaign conclusions and author review history remain recoverable on the original branch. They are not fresh evidence for this landing. The original filename and claim identifier are retained for traceability; the present title and scope control.

## No-Go Discipline Gate

### N1 — Quantifiers and exceptions
Rate products and normalized sequential probabilities differ. The source law, fixed-count comparison, positive birth clause and finite-volume expansion must remain explicit.

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
Rate products and normalized sequential probabilities differ. The source law, fixed-count comparison, positive birth clause and finite-volume expansion must remain explicit.

### N8 — Earlier claims
This scoped result supersedes stronger wording in the original submission. It is a landing review, not an independent audit verdict.

## Falsifiers

A failure of a stated identity under its full hypotheses, or a different exact result for a specified finite example, would refute the corresponding result. An example outside those hypotheses does not.

## Imports

- [minimal_axioms](MINIMAL_AXIOMS_2026-06-29.md): repository boundary; it does not supply the mathematical model below.
- [admissibility_rule_records_that_move_on_their_own_clocks_and_slow_the_clocks_around_them_attract_with_a_one_over_r_potential_equal_both_ways_bounded_theorem_note_2026-09-23](ADMISSIBILITY_RULE_RECORDS_THAT_MOVE_ON_THEIR_OWN_CLOCKS_AND_SLOW_THE_CLOCKS_AROUND_THEM_ATTRACT_WITH_A_ONE_OVER_R_POTENTIAL_EQUAL_BOTH_WAYS_BOUNDED_THEOREM_NOTE_2026-09-23.md): supplied mathematical construction from PR #8860; no premise adoption or retained grade is inferred.
- [admissibility_rule_a_record_that_cannot_read_the_field_from_its_own_motion_hops_on_its_own_clock_and_with_kept_books_records_attract_bounded_theorem_note_2026-09-23](ADMISSIBILITY_RULE_A_RECORD_THAT_CANNOT_READ_THE_FIELD_FROM_ITS_OWN_MOTION_HOPS_ON_ITS_OWN_CLOCK_AND_WITH_KEPT_BOOKS_RECORDS_ATTRACT_BOUNDED_THEOREM_NOTE_2026-09-23.md): supplied mathematical construction from PR #8872; no premise adoption or retained grade is inferred.
- [admissibility_rule_no_master_clock_a_neighbour_determined_scale_covariant_tick_rate_obeys_the_lattice_laplace_equation_records_enter_as_additive_sources_bounded_theorem_note_2026-09-21](ADMISSIBILITY_RULE_NO_MASTER_CLOCK_A_NEIGHBOUR_DETERMINED_SCALE_COVARIANT_TICK_RATE_OBEYS_THE_LATTICE_LAPLACE_EQUATION_RECORDS_ENTER_AS_ADDITIVE_SOURCES_BOUNDED_THEOREM_NOTE_2026-09-21.md): supplied mathematical construction from PR #8568; no premise adoption or retained grade is inferred.
- Standard mathematical definitions: finite-dimensional linear algebra, tensor products, spectral decompositions, exact rational arithmetic, differentiation and lattice shifts as explicitly used above.

## Review record

Original source: PR #8882 head `87e166dbec1eeddc6aec3158b26d378e1effe34e`, branch `physics-loop/admissibility-induced-law-block99-formation-spreads-records-motion-gathers-them-20260923`. The present revision narrows the mathematical domain and corrects the material issues recorded in its statements. Original ancillary science is deferred with recovery preserved. No audit verdict is applied.

## Verification

```bash
PYTHONPATH=scripts python3 scripts/admissibility_rule_formation_on_the_sites_clock_spreads_records_apart_clumping_needs_records_that_move_2026_09_23.py
```

Expected: a zero exit code and a final `TOTAL` with `FAIL=0`.
