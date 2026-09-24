---
claim_id: admissibility_rule_in_discrete_ticks_a_local_clock_is_exact_only_for_walks_that_do_not_move_the_flat_band_theorem_and_a_walk_clocked_to_relative_eps_squared_bounded_theorem_note_2026-09-23
claim_type: bounded_theorem
claim_scope: "Exact line-step identities, scoped small-angle quasienergy expansions and bounded transport under explicit finite-range clock-scaling hypotheses."
upstream_dependencies:
  - minimal_axioms
  - admissibility_rule_no_master_clock_a_neighbour_determined_scale_covariant_tick_rate_obeys_the_lattice_laplace_equation_records_enter_as_additive_sources_bounded_theorem_note_2026-09-21
  - admissibility_rule_a_phase_timed_by_the_local_clock_every_packet_falls_towards_slow_clocks_force_is_energy_times_gradient_weight_and_inertia_tied_by_the_walk_bounded_theorem_note_2026-09-21
runner: scripts/admissibility_rule_in_discrete_ticks_a_local_clock_is_exact_only_for_walks_that_do_not_move_2026_09_23.py
---

# Partial-swap clock steps and a finite-range flat-band theorem

**Type:** bounded_theorem
**Status:** bounded-support; conditional supplied model, unaudited.

This note states conditional mathematics for explicitly supplied operators and fields. The stochastic, amplitude and field rules are not derived from the repository axioms, and no gravitational claim is made.
No bridge, Born-weight, plane-or-sum or gravity statement enters this note as a premise; this note does not fire wake condition 1 of the parked statistical-bridge decision.
Mathematical imports are stated explicitly with their hypotheses; none supplies a physical premise or an audit verdict.

## Premises and declared objects
A layer rotates each disjoint pair(up,x),(down,x+1) byexp(-i epsilon_b sigma_x); the second rotates(down,x),(up,x+1). SetU=BA andepsilon_b=epsilon0 sqrt(wx wy). All clocks arepositive. Each layer is unitary, even for unbounded angles, since it is a direct sum of finite rotations.

## Theorem T1 — step identities
U has range at most2. WithS translating the two components oppositely, a coinR atanglepi/2-epsilon_b, andG shifting down by-1 and multiplying it by-i,
U=-G^(-1)(SR)²G=V², V=iG^(-1)SRG of range1.
The first-order uniform generator is2cos k sigma_x; multiplication by i^x changes it to2sin k sigma_x. The variable-field generator weights each bond bysqrt(wx wy). Expansion is on finite-support vectors, or in operator norm for bounded clocks; no uniform error bound is asserted for an unbounded exponential field.

## Theorem T2 — smooth-branch formulas
The uniform symbol has determinant1 and half-trace1-2sin²epsilon cos²k. On a small positive-angle branch, omega=2asin(sin epsilon |cos k|), and
omega=2epsilon |cos k|[1-epsilon²sin²k/6]+O(epsilon^5).
Where the frequency is nonzero, epsilon omega_epsilon/omega=1-epsilon²sin²k/3+O(epsilon^4). Atcos k=0 a relative error quotient is undefined.
For a supplied smooth Hamiltonian ray model using this quasienergy, v'= (2v²+Psi)partial_x log w, with
Psi=4sin epsilon[epsilon cos epsilon-2sin epsilon sin²k]/[1-sin²epsilon cos²k].
Its series is4epsilon²cos2k+epsilon^4(2cos2k+3cos4k-1)/3+O(epsilon^6). Branch crossings and singular denominators are excluded; this is not an exact packet trajectory theorem.

## Theorem T3 — generic failure of clock doubling
Half-trace U(2epsilon)-cos[2omega(epsilon)]=2sin^4epsilon sin²2k.
For variable angles the four-site amplitude ofU² is the product of the four successive sines, whereasU[2w] has range at most2. Thus the proposed identity fails in general, as the nonzero rational-angle fixture shows. It need not fail for every exceptional field or mode: zero angles give identity steps.

## Theorem T4 — bounded transport theorem
LetV be a translation-invariant unitary on the infinite d-dimensional lattice withN components and max-norm rangeR. PutK=(2R+1)^d andM=N(K+1). IfV throughV^M all have range at mostR, their traces are trigonometric polynomials of degreeR in each coordinate. A tensor-product grid ofK nodes interpolates them.
For fixedk, collect the eigenvalues at k and at the grid nodes; there are at mostM distinct nonzero values. Interpolation of power sums for powers1 throughM and invertibility of the corresponding power matrix force each eigenvalue at k to occur among the node values. The characteristic polynomial is continuous on the connected torus and takes only finitely many values, so it is constant.
Withp distinct eigenvalues, spectral projections are polynomials inV of degreep-1. Every power therefore has range at most(p-1)R<=(N-1)R. This permits bounded motion; it does not mean the particle stays at one site.

The same conclusion holds for uniformly range-R, translation-invariantV_c on an open clock interval with eigenvaluesexp[-ic f_b(k)], f_b real and independent ofc: apply interpolation to the traces and linear independence of finitely many exponential functions ofc. Clock continuity for a local rule and exact identitiesU[mw]=U[w]^m in gradients approaching constantc giveU[mc]=U[c]^m and the finite-power hypothesis for the UNIFORM steps. No classification of arbitrary inhomogeneous transport follows.
The dimer symbolH=[[0,exp(-ik)],[exp(ik),0]] hasH²=I. Its groupcos c I-i sin c H has exact scaling and moves amplitude one site, attaining the bounded-motion conclusion.

## Historical experiments — deferred

Original auxiliary calculations, floating-point scans, campaign conclusions and author review history remain recoverable on the original branch. They are not fresh evidence for this landing. The original filename and claim identifier are retained for traceability; the present title and scope control.

## No-Go Discipline Gate

### N1 — Quantifiers and exceptions
Uniform finite range, finite component count and the stated exact identities are essential. Flat bands allow bounded motion; small-angle ray formulas require smooth nonzero-frequency branches.

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
Uniform finite range, finite component count and the stated exact identities are essential. Flat bands allow bounded motion; small-angle ray formulas require smooth nonzero-frequency branches.

### N8 — Earlier claims
This scoped result supersedes stronger wording in the original submission. It is a landing review, not an independent audit verdict.

## Falsifiers

A failure of a stated identity under its full hypotheses, or a different exact result for a specified finite example, would refute the corresponding result. An example outside those hypotheses does not.

## Imports

- [minimal_axioms](MINIMAL_AXIOMS_2026-06-29.md): repository boundary; it does not supply the mathematical model below.
- [admissibility_rule_no_master_clock_a_neighbour_determined_scale_covariant_tick_rate_obeys_the_lattice_laplace_equation_records_enter_as_additive_sources_bounded_theorem_note_2026-09-21](ADMISSIBILITY_RULE_NO_MASTER_CLOCK_A_NEIGHBOUR_DETERMINED_SCALE_COVARIANT_TICK_RATE_OBEYS_THE_LATTICE_LAPLACE_EQUATION_RECORDS_ENTER_AS_ADDITIVE_SOURCES_BOUNDED_THEOREM_NOTE_2026-09-21.md): supplied mathematical construction from PR #8568; no premise adoption or retained grade is inferred.
- [admissibility_rule_a_phase_timed_by_the_local_clock_every_packet_falls_towards_slow_clocks_force_is_energy_times_gradient_weight_and_inertia_tied_by_the_walk_bounded_theorem_note_2026-09-21](ADMISSIBILITY_RULE_A_PHASE_TIMED_BY_THE_LOCAL_CLOCK_EVERY_PACKET_FALLS_TOWARDS_SLOW_CLOCKS_FORCE_IS_ENERGY_TIMES_GRADIENT_WEIGHT_AND_INERTIA_TIED_BY_THE_WALK_BOUNDED_THEOREM_NOTE_2026-09-21.md): supplied mathematical construction from PR #8570; no premise adoption or retained grade is inferred.
- Standard mathematical definitions: finite-dimensional linear algebra, tensor products, spectral decompositions, exact rational arithmetic, differentiation and lattice shifts as explicitly used above.

## Review record

Original source: PR #8934 head `6cad973f8d12f3385529a197247b5a54f5c33a2f`, branch `physics-loop/admissibility-induced-law-block105-in-discrete-ticks-a-local-clock-is-exact-only-for-walks-that-do-not-move-20260923`. The present revision narrows the mathematical domain and corrects the material issues recorded in its statements. Original ancillary science is deferred with recovery preserved. No audit verdict is applied.

## Verification

```bash
PYTHONPATH=scripts python3 scripts/admissibility_rule_in_discrete_ticks_a_local_clock_is_exact_only_for_walks_that_do_not_move_2026_09_23.py
```

Expected: a zero exit code and a final `TOTAL` with `FAIL=0`.
