---
claim_id: admissibility_rule_where_moving_records_cannot_clump_a_sharp_one_site_bound_gives_uniqueness_below_a_ratio_spread_of_49_over_25_bounded_theorem_note_2026-09-23
claim_type: bounded_theorem
claim_scope: "Positive grand-canonical nearest-neighbor conditionals: sharp total-variation influence, an explicit uniqueness criterion, reflection identities and finite arithmetic without a coexistence claim."
upstream_dependencies:
  - minimal_axioms
  - admissibility_rule_records_that_move_pair_weight_transit_has_the_static_law_as_equilibrium_the_binding_scale_is_a_new_constant_clumping_and_jamming_executed_bounded_theorem_note_2026-09-20
runner: scripts/admissibility_rule_where_moving_records_cannot_clump_2026_09_23.py
---

# A sharp influence bound, uniqueness window and finite cube arithmetic

**Type:** bounded_theorem
**Status:** bounded-support; conditional supplied model, unaudited.

This note states conditional mathematics for explicitly supplied operators and fields. The stochastic, amplitude and field rules are not derived from the repository axioms, and no gravitational claim is made.
No bridge, Born-weight, plane-or-sum or gravity statement enters this note as a premise; this note does not fire wake condition 1 of the parked statistical-bridge decision.
Mathematical imports are stated explicitly with their hypotheses; none supplies a physical premise or an audit verdict.

## Premises and declared objects
Each site has seven states: vacancy or one of six axes. A bond weight is1 if either end is vacant, otherwise c times(p,q,r) for equal, opposite or orthogonal contents. All parameters and fugacity z are positive and finite. The specification is grand-canonical; fixing total count does not give the same one-site conditionals.

## Theorem T1 — multiplier influence
For P'=hP/E_P h, 0<m<=h<=M,
TV(P,P')<=(sqrt M-sqrt m)/(sqrt M+sqrt m).
If m=M the distance iszero. Otherwise write H=E h. The convex chord bound gives E(h-H)_+ <=(H-m)(M-H)/(M-m); dividing byH and maximizing gives H=sqrt(mM). Two-point endpoint laws attain the bound.
For a neighbor change b tob', h(a)=W(a,b')/W(a,b). Let R be the largest max_a h/min_a h. Each neighbor influence is at most q=(sqrt R-1)/(sqrt R+1).

## Theorem T2 — the sufficient window
If6q<1, equivalently R<49/25, the infinite-volume specification has a unique probability state. One coupling proof repeatedly updates a site using a maximal coupling of its conditional laws. Its disagreement probability is bounded by q times the sum of neighboring disagreements. Iterating the bound from a distant boundary gives a sum of path weights, at most(6q)^distance/(1-6q); it tends tozero. Finite-state positive local specifications have subsequential volume limits, and vanishing boundary influence makes them equal. This is the explicit contraction argument used here.

For content-independent occupied weights cw, R=max(cw,1/cw), giving25/49<cw<49/25. At cw=1 occupation is independent (the sixfold content multiplicity changes the effective activity).
For(p,q,r)=(9,8,8), occupied/vacant changes require8c>25/49 and9c<49/25; content changes have spread at most81/64. Thus25/392<c<49/225.
For(3,1,2), opposite-content changes include ratios3 and1/3, hence R>=9 for everyc. Failure of this sufficient test is not proof of coexistence.

## Theorem T3 — reflection algebra
The single-bond seven-state matrix is positive semidefinite exactly when its Schur complement cOmega-J is. Its invariant subspaces have eigenvalues c(p+q+4r)-6, c(p-q), c(p+q-2r), with multiplicities1,3,2. These inequalities supply the usual bond-factor reflection construction.
For a reflection-invariant nearest-neighbor law on a reflected finite box, or an even torus separated by two fixed site planes, conditioning on the separating sites makes the two halves independent reflected copies. The reflected quadratic expectation is a positive average of absolute squares. Positivity of arbitrary weights alone, without the reflected geometry and symmetry, is not the statement.

## Theorem T4 — finite arithmetic only
The runner enumerates254 nonconstant binary patterns on a2 by2 by2 periodic cube. Their occupied fractions rho, mixed-bond densities e and occupied-component counts divided by8 (kap) form16 classes, with min e=3/4.
Define epsilon_M as the class-multiplicity sum of6^kap 2^(rho-kap) M^(-4e), or omit both content factors in the contentless version. Replacing eighth roots of2 and6 by the explicit rational upper bounds in the runner proves676epsilon_44<=1/4 and676epsilon_38<=1/4 respectively.
This is a defined finite sum inequality. No contour-to-probability bound, coexistence fugacity, thermodynamic phase construction or quantitative onset is proved by it here.

## Historical experiments — deferred

Original auxiliary calculations, floating-point scans, campaign conclusions and author review history remain recoverable on the original branch. They are not fresh evidence for this landing. The original filename and claim identifier are retained for traceability; the present title and scope control.

## No-Go Discipline Gate

### N1 — Quantifiers and exceptions
Uniqueness concerns a grand-canonical equilibrium specification, not absence of local clusters or dynamic jams. Finite cube arithmetic is not a coexistence certificate.

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
Uniqueness concerns a grand-canonical equilibrium specification, not absence of local clusters or dynamic jams. Finite cube arithmetic is not a coexistence certificate.

### N8 — Earlier claims
This scoped result supersedes stronger wording in the original submission. It is a landing review, not an independent audit verdict.

## Falsifiers

A failure of a stated identity under its full hypotheses, or a different exact result for a specified finite example, would refute the corresponding result. An example outside those hypotheses does not.

## Imports

- [minimal_axioms](MINIMAL_AXIOMS_2026-06-29.md): repository boundary; it does not supply the mathematical model below.
- [admissibility_rule_records_that_move_pair_weight_transit_has_the_static_law_as_equilibrium_the_binding_scale_is_a_new_constant_clumping_and_jamming_executed_bounded_theorem_note_2026-09-20](ADMISSIBILITY_RULE_RECORDS_THAT_MOVE_PAIR_WEIGHT_TRANSIT_HAS_THE_STATIC_LAW_AS_EQUILIBRIUM_THE_BINDING_SCALE_IS_A_NEW_CONSTANT_CLUMPING_AND_JAMMING_EXECUTED_BOUNDED_THEOREM_NOTE_2026-09-20.md): supplied mathematical construction from PR #8530; no premise adoption or retained grade is inferred.
- Standard mathematical definitions: finite-dimensional linear algebra, tensor products, spectral decompositions, exact rational arithmetic, differentiation and lattice shifts as explicitly used above.

## Review record

Original source: PR #8903 head `d3c8f4f96278b395f7b92c61679b0533faf15305`, branch `physics-loop/admissibility-induced-law-block102-where-moving-records-cannot-clump-20260923`. The present revision narrows the mathematical domain and corrects the material issues recorded in its statements. Original ancillary science is deferred with recovery preserved. No audit verdict is applied.

## Verification

```bash
PYTHONPATH=scripts python3 scripts/admissibility_rule_where_moving_records_cannot_clump_2026_09_23.py
```

Expected: a zero exit code and a final `TOTAL` with `FAIL=0`.
