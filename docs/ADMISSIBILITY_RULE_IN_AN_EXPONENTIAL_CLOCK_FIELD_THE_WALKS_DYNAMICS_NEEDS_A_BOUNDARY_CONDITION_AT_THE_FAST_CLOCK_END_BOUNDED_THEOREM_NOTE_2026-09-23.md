---
claim_id: admissibility_rule_in_an_exponential_clock_field_the_walks_dynamics_needs_a_boundary_condition_at_the_fast_clock_end_bounded_theorem_note_2026-09-23
claim_type: bounded_theorem
claim_scope: "The exponential line operator has deficiency indices (2,2); chain-separated boundary domains and a circle of translation-compatible choices, with explicit operator-theory imports."
upstream_dependencies:
  - minimal_axioms
  - admissibility_rule_no_master_clock_a_neighbour_determined_scale_covariant_tick_rate_obeys_the_lattice_laplace_equation_records_enter_as_additive_sources_bounded_theorem_note_2026-09-21
  - admissibility_rule_a_phase_timed_by_the_local_clock_every_packet_falls_towards_slow_clocks_force_is_energy_times_gradient_weight_and_inertia_tied_by_the_walk_bounded_theorem_note_2026-09-21
runner: scripts/admissibility_rule_in_an_exponential_clock_field_the_walks_dynamics_needs_a_boundary_condition_at_the_fast_clock_end_2026_09_23.py
---

# Boundary domains for an exponentially clocked line operator

**Type:** bounded_theorem
**Status:** bounded-support; conditional supplied model, unaudited.

This note states conditional mathematics for explicitly supplied operators and fields. The stochastic, amplitude and field rules are not derived from the repository axioms, and no gravitational claim is made.
No bridge, Born-weight, plane-or-sum or gravity statement enters this note as a premise; this note does not fire wake condition 1 of the parked statistical-bridge decision.
Mathematical imports are stated explicitly with their hypotheses; none supplies a physical premise or an audit verdict.

## Premises and declared objects
Onl²(Z;C²), let(Tpsi)_x=psi_(x-1), D=(i/2)(T-T^dagger), w_x=lambda^x withlambda>1, andH_w=sqrt W sigma_x D sqrt W initially onc00. It is symmetric. ChainA usesup at even sites anddown at odd sites; chainB uses the other components. Each is indexed by the physical integerx.

## Theorem T1 — recurrence and endpoint tests
H_w T_a=lambda^a T_a H_w onc00. On either chain its imaginary off-diagonal coefficients become real positive bonds b_n=lambda^(n+1/2)/2 underJ=G^dagger H G, G_nn=i^n. Thus the real-gauge state isf_n=i^(-n)psi_n.
Original-gauge zero solutions supported on one parity have value lambda^(-m) atn=2m or2m+1. Real-gauge basis solutions may be chosen
chi_(2m)=(-1)^m lambda^(-m), chi_odd=0,
phi_(2m+1)=(-1)^m lambda^(-m), phi_even=0.
Their fast-end squared sums arelambda²/(lambda²-1); at the slow end they grow. The reciprocal-bond sum diverges at the slow end.

## Theorem T2 — the imported domain conclusions
The endpoint theorem cited under Imports and used here says that square summability of all solutions at one energy implies the limit-circle case; divergent reciprocal-bond sums imply limit point. A chain with one endpoint of each type has deficiency indices(1,1). Hence the direct-sum walk has(2,2).
At a limit-circle endpoint a real projective line of reference solutions specifies a separated self-adjoint domain by a vanishing limiting Wronskian; the limit-point endpoint needs no condition. These statements are mathematical imports, specified under Imports, not established by finite-window tests.

ForJ defineDmax={f in l²:Jf in l²}. At the fast end usev=a chi+b phi, real(a,b) nonzero, and impose lim W_n(v,f)=0, W_n(v,f)=b_n(v_n f_(n+1)-v_(n+1)f_n). A cutoff ofv at the slow end supplies a maximal-domain reference without changing its fast-end germ. Complex boundary forms use conjugation; v is real. One such real line per chain gives the chain-separated domains. Chain-mixing extensions are not classified here.

## Theorem T3 — translation-compatible domains
LetS be the ordinary right shift of real-gauge sequences. On coefficients(a,b), S acts asM(a,b)=(-lambda b,a); M²=-lambda I. The physical translation in this gauge is-iS, which has the same action on projective reference lines up to a common scalar. PhysicalT2 acts aslambda on both basis germs, preserving every chain-separated pair of lines.

The identityJ T_a=lambda^a T_a J mapsDmax onto itself. Wronskians of two shifted sequences obeyW_n(S^a f,S^a g)=lambda^a W_(n-a)(f,g); their zero limits are therefore preserved in the corresponding image domains. This proves domain covariance, not merely recurrence covariance.
For a one-site translation choose the chainB line to beM times the chainA line. The reverse compatibility follows fromM² being scalar. These choices form one real projective circle. For them the self-adjoint operators satisfyH T_a=lambda^a T_a H for every integera; spectral functional calculus givesexp(-itH)T_a=T_a exp(-i lambda^a t H).
All chain-separated choices obey the even-translation version. No classification of all chain-mixing choices is asserted.

## Theorem T4 — a geometric sum only
The sum of inverse clocks fromx0 toward the fast end islambda^(-x0)/(1-1/lambda). It is a tendnt scalar series, not a quantum arrival-time theorem or proof that a wavepacket reaches infinity. For other clock fields a reciprocal-bond endpoint test concerns1/sqrt(w_n w_(n+1)), not automatically1/w_n.

## Imports — endpoint theory source
[Gerald Teschl, Jacobi Operators and Completely Integrable Nonlinear Lattices, section2.6](https://www.mat.univie.ac.at/~gerald/ftp/book-jac/jacop.pdf): Lemma2.15, equation2.165, Lemma2.20 and Theorems2.18/2.21 provide the endpoint and Wronskian-domain results under positive real bonds and real diagonal coefficients. Their hypotheses hold for each chain above. The original finite-window checks verify identities and examples; the domain conclusions additionally use these stated theorems.

## Historical experiments — deferred

Original auxiliary calculations, floating-point scans, campaign conclusions and author review history remain recoverable on the original branch. They are not fresh evidence for this landing. The original filename and claim identifier are retained for traceability; the present title and scope control.

## No-Go Discipline Gate

### N1 — Quantifiers and exceptions
The result is for the infinite exponential line and chain-separated extensions. The boundary reference must be interpreted in the real gauge, and no arrival-time or three-dimensional conclusion follows.

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
The result is for the infinite exponential line and chain-separated extensions. The boundary reference must be interpreted in the real gauge, and no arrival-time or three-dimensional conclusion follows.

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

Original source: PR #8945 head `305272de6f7f3c3b44c91174231444d34209cfde`, branch `physics-loop/admissibility-induced-law-block108-the-walks-dynamics-needs-a-boundary-condition-at-the-fast-clock-end-20260923`. The present revision narrows the mathematical domain and corrects the material issues recorded in its statements. Original ancillary science is deferred with recovery preserved. No audit verdict is applied.

## Verification

```bash
PYTHONPATH=scripts python3 scripts/admissibility_rule_in_an_exponential_clock_field_the_walks_dynamics_needs_a_boundary_condition_at_the_fast_clock_end_2026_09_23.py
```

Expected: a zero exit code and a final `TOTAL` with `FAIL=0`.
