---
claim_id: admissibility_rule_records_that_move_on_their_own_clocks_and_slow_the_clocks_around_them_attract_with_a_one_over_r_potential_equal_both_ways_bounded_theorem_note_2026-09-23
claim_type: bounded_theorem
claim_scope: "Positive fixed-count rates with symmetric proposals: exact fixed-field and neutralized torus pair laws, clock-only waiting times and finite kernel comparisons."
upstream_dependencies:
  - minimal_axioms
  - admissibility_rule_no_master_clock_a_neighbour_determined_scale_covariant_tick_rate_obeys_the_lattice_laplace_equation_records_enter_as_additive_sources_bounded_theorem_note_2026-09-21
  - admissibility_rule_records_that_move_pair_weight_transit_has_the_static_law_as_equilibrium_the_binding_scale_is_a_new_constant_clumping_and_jamming_executed_bounded_theorem_note_2026-09-20
runner: scripts/admissibility_rule_records_that_move_on_their_own_clocks_and_slow_the_clocks_around_them_attract_one_over_r_equal_both_ways_2026_09_23.py
---

# Detailed balance for fixed and configuration-following clocks

**Type:** bounded_theorem
**Status:** bounded-support; conditional supplied model, unaudited.

This note states conditional mathematics for explicitly supplied operators and fields. The stochastic, amplitude and field rules are not derived from the repository axioms, and no gravitational claim is made.
No bridge, Born-weight, plane-or-sum or gravity statement enters this note as a premise; this note does not fire wake condition 1 of the parked statistical-bridge decision.
Mathematical imports are stated explicitly with their hypotheses; none supplies a physical premise or an audit verdict.

## Premises and declared objects
On a simple periodic cubic torus of side L>=3 let Delta=6I-Adj, V=L³ and G its mean-zero inverse: Delta G=delta0-1/V. Let lambda=log kappa be real. The supplied configuration-following field is u_z(C)=6lambda sum_{r in C}G(z-r), with mean u=0. It solves Delta u=6lambda(n-|C|/V). The compensating background is an additional source prescription: the unneutralized positive-count equation is inconsistent on a torus unless lambda=0.

For positive W(C), fixed record count and a move x to an empty neighbor y, set h=W(C')/[W(C)+W(C')] and rate=exp[a u_x(C)+(1-a)u_y(C)] h/6, a real. Proposals are symmetric. Formation and delayed clocks are absent.

## Theorem T1 — fixed clocks
For a configuration-independent positive field w, pi(C) is proportional to W(C) product_{z in C}w_z^(1-2a).
Indeed pi(C)rate(C,C') contains the symmetric factor (w_x w_y)^(1-a)W(C)W(C')/[6(W(C)+W(C'))], times the unchanged-site factors.

## Theorem T2 — clocks recomputed after every move
For the torus field above,
pi(C) is proportional to W(C) exp[6lambda(1-2a) sum_{unordered pairs}G(r-s)].
Write D=C minus x, A=sum_D G(x-r), B=sum_D G(y-r), and g=G(x-y). The log forward/backward rate ratio is log[W(C')/W(C)]+6lambda(2a-1)(A-B); equal diagonal G(0) and even g cancel. The pair sum changes by B-A, proving balance. The fixed-field product evaluated after substitution would count pairs twice and is not this law.
This argument needs a translation-invariant symmetric kernel with constant diagonal. An arbitrary symmetric finite-graph kernel need not have constant diagonal and gives an additional self term.

## Theorem T3 — clock-only motion
Restrict now to W=1, so h=1/2. At a=1 every allowed hop of a record at x has rate w_x/12. Its conditional drift is (w_x/12)sum_{empty neighbors}e, zero when all six neighbors are empty, and -w_x e/12 for a single occupied neighbor in direction e. The embedded jump directions are uniform among empty neighbors. General W changes these directions and invalidates the clock-only conclusion.

Two records have equal departure clocks by evenness of G. Their relative-position stationary weight per offset is exp[-6lambda G(d)], up to normalization. This is a residence-weight identity, not a mechanical force. At arrival timing the drift is a weighted discrete sum; the runner checks its sign for one specified two-record geometry, not every configuration.

## Theorem T4 — finite reciprocal pair energies
Define U(d)=6(2a-1)lambda G(d). Evenness gives symmetric pair energies and opposite central differences between two fixed clusters. On L=4,6, the runner verifies axis and body-diagonal decrease through half the period. In particular G(1,0,0)-G(2,0,0)=228/7680 on L=4. If (2a-1)lambda<0, U is lower at the nearer of these tested offsets. A finite torus has no infinite-distance limit. No inverse-distance theorem, condensation threshold, inertial motion or arbitrary contact-dependent-source extension is established here.

## Historical experiments — deferred

Original auxiliary calculations, floating-point scans, campaign conclusions and author review history remain recoverable on the original branch. They are not fresh evidence for this landing. The original filename and claim identifier are retained for traceability; the present title and scope control.

## No-Go Discipline Gate

### N1 — Quantifiers and exceptions
The neutralizing background, mean clock gauge, constant kernel diagonal and symmetric proposals are essential. Uniform directions require W=1; the heat-bath factor halves the originally stated hop rates.

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
The neutralizing background, mean clock gauge, constant kernel diagonal and symmetric proposals are essential. Uniform directions require W=1; the heat-bath factor halves the originally stated hop rates.

### N8 — Earlier claims
This scoped result supersedes stronger wording in the original submission. It is a landing review, not an independent audit verdict.

## Falsifiers

A failure of a stated identity under its full hypotheses, or a different exact result for a specified finite example, would refute the corresponding result. An example outside those hypotheses does not.

## Imports

- [minimal_axioms](MINIMAL_AXIOMS_2026-06-29.md): repository boundary; it does not supply the mathematical model below.
- [admissibility_rule_no_master_clock_a_neighbour_determined_scale_covariant_tick_rate_obeys_the_lattice_laplace_equation_records_enter_as_additive_sources_bounded_theorem_note_2026-09-21](ADMISSIBILITY_RULE_NO_MASTER_CLOCK_A_NEIGHBOUR_DETERMINED_SCALE_COVARIANT_TICK_RATE_OBEYS_THE_LATTICE_LAPLACE_EQUATION_RECORDS_ENTER_AS_ADDITIVE_SOURCES_BOUNDED_THEOREM_NOTE_2026-09-21.md): supplied mathematical construction from PR #8568; no premise adoption or retained grade is inferred.
- [admissibility_rule_records_that_move_pair_weight_transit_has_the_static_law_as_equilibrium_the_binding_scale_is_a_new_constant_clumping_and_jamming_executed_bounded_theorem_note_2026-09-20](ADMISSIBILITY_RULE_RECORDS_THAT_MOVE_PAIR_WEIGHT_TRANSIT_HAS_THE_STATIC_LAW_AS_EQUILIBRIUM_THE_BINDING_SCALE_IS_A_NEW_CONSTANT_CLUMPING_AND_JAMMING_EXECUTED_BOUNDED_THEOREM_NOTE_2026-09-20.md): supplied mathematical construction from PR #8530; no premise adoption or retained grade is inferred.
- Standard mathematical definitions: finite-dimensional linear algebra, tensor products, spectral decompositions, exact rational arithmetic, differentiation and lattice shifts as explicitly used above.

## Review record

Original source: PR #8860 head `f9b34475df1a567d2e1abc2f69b7f259483b728f`, branch `physics-loop/admissibility-induced-law-block95-records-on-their-own-clocks-attract-one-over-r-equal-both-ways-20260923`. The present revision narrows the mathematical domain and corrects the material issues recorded in its statements. Original ancillary science is deferred with recovery preserved. No audit verdict is applied.

## Verification

```bash
PYTHONPATH=scripts python3 scripts/admissibility_rule_records_that_move_on_their_own_clocks_and_slow_the_clocks_around_them_attract_one_over_r_equal_both_ways_2026_09_23.py
```

Expected: a zero exit code and a final `TOTAL` with `FAIL=0`.
