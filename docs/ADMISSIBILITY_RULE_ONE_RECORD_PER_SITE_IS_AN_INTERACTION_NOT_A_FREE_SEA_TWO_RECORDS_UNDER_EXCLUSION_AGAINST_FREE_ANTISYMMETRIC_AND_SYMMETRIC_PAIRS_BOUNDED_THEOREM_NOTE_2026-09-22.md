---
claim_id: admissibility_rule_one_record_per_site_is_an_interaction_not_a_free_sea_two_records_under_exclusion_against_free_antisymmetric_and_symmetric_pairs_bounded_theorem_note_2026-09-22
claim_type: bounded_theorem
claim_scope: "For supplied two-particle hopping compressed to different-site configurations, exact trace comparisons on rings of four through seven sites distinguish it from the free symmetric and antisymmetric sectors. One explicit projected pair fails additivity relative to its original orbitals. No universal nonadditivity or general ring-parity spectrum theorem is claimed."
upstream_dependencies:
  - minimal_axioms
  - admissibility_rule_a_phase_timed_by_the_local_clock_every_packet_falls_towards_slow_clocks_force_is_energy_times_gradient_weight_and_inertia_tied_by_the_walk_bounded_theorem_note_2026-09-21
  - admissibility_rule_action_and_reaction_the_rate_fields_source_is_the_amplitudes_energy_density_matched_pulls_and_a_kept_ledger_fix_the_clock_laws_second_order_bounded_theorem_note_2026-09-21
  - admissibility_rule_amplitudes_of_negative_energy_fall_like_the_others_and_source_the_opposite_field_a_negative_body_at_rest_has_a_largest_size_bounded_theorem_note_2026-09-21
  - admissibility_rule_the_filled_seas_energy_as_the_ledgers_field_term_a_chessboard_of_clocks_is_invisible_the_sea_induces_a_clock_stiffness_not_the_curvature_member_bounded_theorem_note_2026-09-22
runner: scripts/admissibility_rule_one_record_per_site_is_an_interaction_not_a_free_sea_two_records_under_exclusion_2026_09_22.py
---

# Two-particle site exclusion: finite trace comparisons and a failure of original-orbital additivity

**Type:** bounded_theorem
**Status:** bounded-support; conditional supplied model, unaudited.

This note states conditional mathematics for explicitly supplied operators and fields. The amplitude dynamics and composition rules are not derived from the repository axioms, and no gravitational claim is made.
No bridge, Born-weight, plane-or-sum or gravity statement enters this note as a premise; this note does not fire wake condition 1 of the parked statistical-bridge decision.
No value, constant or theorem is imported as authority; the standard mathematical imports are named at definition level.

## Premises and declared objects

Use the supplied ring walk H=phi sigma3 S phi on N sites, with two coin states per site and d=2N. The chosen two-particle dynamics is H2=H tensor I+I tensor H compressed by the fixed position projector P removing configurations with equal sites. This compression, tensor-product space and exchange rule are supplied model choices. The Record axiom does not by itself derive this Hamiltonian or its composition rule.

Free antisymmetric and symmetric sector dimensions are d(d-1)/2 and d(d+1)/2. The different-site sectors of either exchange sign have d(d-2)/2 states; the distinguishable sector has twice as many. The antisymmetric states removed by P are the N opposite-coin same-site pairs. Symmetric diagonal pairs are also excluded.

## Theorem T1 — specified finite second traces

For uniform phi=1 and N=4,5,6,7, exact `tr H2^2/dim` values are:

| N | Different-site, either sign or distinguishable | Free antisymmetric | Free symmetric |
|---|---|---|---|
|4|2/3|6/7|10/9|
|5|3/4|8/9|12/11|
|6|4/5|10/11|14/13|
|7|5/6|12/13|16/15|

These are finite computations, not an extrapolation to all rings. The runner forms A=iH as a real antisymmetric matrix and its two-particle sum, then compresses it to orthogonal sector vectors. If M contains matrix elements in that unnormalized basis and D its positive diagonal squared norms, D^-1 M is similar to the orthonormal matrix D^-1/2 M D^-1/2. Its trace powers therefore give the desired spectral moments, with signs -,+,- for H powers 2,4,6. The differences above prove non-equivalence to the specified free sectors in these examples.

## Theorem T2 — the finite exchange-sign comparison

On N=4,5,6,7 the three different-site sectors have equal normalized second traces. Their fourth traces agree for N=5,6,7, but at N=4 the antisymmetric and symmetric values are 5/6 and 7/6. Their sixth traces agree for N=5,7 and differ between exchange signs for N=6. These finite moments do not prove that exchange signs are generally irrelevant, that every odd-ring spectrum coincides, or that all differences are classified by parity.

## Theorem T3 — an explicit additivity counterexample

Take the six-site positive rational phi and the two orthogonal complex orbitals constructed explicitly in the runner by exact orthogonalization. Their free exterior product Psi has normalized expectation `<H2>=<H>_1+<H>_2`. For its nonzero projection P Psi, normalized expectation of P H2 P differs from that original-orbital sum. The runner computes both rational values directly.

This is an existential counterexample to a universal original-orbital formula after projection. It does not assert that every projected pair fails that formula: special states may agree. A one-body expectation is still linear in the actual state's one-particle reduced density matrix. No general sign of a hole source or physical many-particle filling follows from this example.

## Historical experiments — deferred

Original auxiliary calculations, floating-point scans, campaign conclusions and author review history remain recoverable on the original branch. They are not fresh evidence for this landing. The original filename and claim identifier are retained for traceability; the present title and scope control.

## No-Go Discipline Gate

### N1 — Quantifiers and exceptions
All trace claims concern the four listed finite rings. Compression is a supplied dynamical choice. Projection can change original-orbital expectations, but nonadditivity is not universal and does not invalidate linearity in the actual reduced density matrix.

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
All trace claims concern the four listed finite rings. Compression is a supplied dynamical choice. Projection can change original-orbital expectations, but nonadditivity is not universal and does not invalidate linearity in the actual reduced density matrix.

### N8 — Earlier claims
This scoped result supersedes stronger wording in the original submission. It is a landing review, not an independent audit verdict.

## Falsifiers

A failure of a stated identity under its full hypotheses, or a different exact result for a specified finite example, would refute the corresponding result. An example outside those hypotheses does not.

## Imports

- [minimal_axioms](MINIMAL_AXIOMS_2026-06-29.md): repository boundary; it does not supply the amplitude dynamics below.
- [admissibility_rule_a_phase_timed_by_the_local_clock_every_packet_falls_towards_slow_clocks_force_is_energy_times_gradient_weight_and_inertia_tied_by_the_walk_bounded_theorem_note_2026-09-21](ADMISSIBILITY_RULE_A_PHASE_TIMED_BY_THE_LOCAL_CLOCK_EVERY_PACKET_FALLS_TOWARDS_SLOW_CLOCKS_FORCE_IS_ENERGY_TIMES_GRADIENT_WEIGHT_AND_INERTIA_TIED_BY_THE_WALK_BOUNDED_THEOREM_NOTE_2026-09-21.md): supplied mathematical construction from PR #8570; no premise adoption or retained grade is inferred.
- [admissibility_rule_action_and_reaction_the_rate_fields_source_is_the_amplitudes_energy_density_matched_pulls_and_a_kept_ledger_fix_the_clock_laws_second_order_bounded_theorem_note_2026-09-21](ADMISSIBILITY_RULE_ACTION_AND_REACTION_THE_RATE_FIELDS_SOURCE_IS_THE_AMPLITUDES_ENERGY_DENSITY_MATCHED_PULLS_AND_A_KEPT_LEDGER_FIX_THE_CLOCK_LAWS_SECOND_ORDER_BOUNDED_THEOREM_NOTE_2026-09-21.md): supplied mathematical construction from PR #8571; no premise adoption or retained grade is inferred.
- [admissibility_rule_amplitudes_of_negative_energy_fall_like_the_others_and_source_the_opposite_field_a_negative_body_at_rest_has_a_largest_size_bounded_theorem_note_2026-09-21](ADMISSIBILITY_RULE_AMPLITUDES_OF_NEGATIVE_ENERGY_FALL_LIKE_THE_OTHERS_AND_SOURCE_THE_OPPOSITE_FIELD_A_NEGATIVE_BODY_AT_REST_HAS_A_LARGEST_SIZE_BOUNDED_THEOREM_NOTE_2026-09-21.md): supplied mathematical construction from PR #8603; no premise adoption or retained grade is inferred.
- [admissibility_rule_the_filled_seas_energy_as_the_ledgers_field_term_a_chessboard_of_clocks_is_invisible_the_sea_induces_a_clock_stiffness_not_the_curvature_member_bounded_theorem_note_2026-09-22](ADMISSIBILITY_RULE_THE_FILLED_SEAS_ENERGY_AS_THE_LEDGERS_FIELD_TERM_A_CHESSBOARD_OF_CLOCKS_IS_INVISIBLE_THE_SEA_INDUCES_A_CLOCK_STIFFNESS_NOT_THE_CURVATURE_MEMBER_BOUNDED_THEOREM_NOTE_2026-09-22.md): supplied mathematical construction from PR #8611; no premise adoption or retained grade is inferred.
- Standard mathematical definitions: finite-dimensional linear algebra, tensor products, spectral decompositions, exact rational arithmetic, differentiation and lattice shifts as explicitly used above.

## Review record

Original source: PR #8613 head `88a8e6752e01205879181758e70b2a47f2bad275`, branch `physics-loop/admissibility-induced-law-block78-one-record-per-site-is-an-interaction-not-a-free-sea-20260922`. The present revision narrows the mathematical domain and corrects the material issues recorded in its statements. Original ancillary science is deferred with recovery preserved. No audit verdict is applied.

## Verification

```bash
PYTHONPATH=scripts python3 scripts/admissibility_rule_one_record_per_site_is_an_interaction_not_a_free_sea_two_records_under_exclusion_2026_09_22.py
```

Expected: a zero exit code and a final `TOTAL` with `FAIL=0`.
