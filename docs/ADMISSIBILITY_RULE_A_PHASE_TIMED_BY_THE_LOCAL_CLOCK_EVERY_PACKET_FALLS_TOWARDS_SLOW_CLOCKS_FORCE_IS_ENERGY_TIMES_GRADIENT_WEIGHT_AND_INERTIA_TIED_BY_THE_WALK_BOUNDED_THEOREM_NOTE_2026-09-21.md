---
claim_id: admissibility_rule_a_phase_timed_by_the_local_clock_every_packet_falls_towards_slow_clocks_force_is_energy_times_gradient_weight_and_inertia_tied_by_the_walk_bounded_theorem_note_2026-09-21
claim_type: bounded_theorem
claim_scope: "Within supplied two-component amplitudes, a Hermitian nearest-neighbour generator with soldered proper cubic rotations, and fixed positive local rates: classify the three generator parameters, prove finite weighted-matrix identities and a finite-support polynomial translation identity, and derive a ray acceleration identity for a separately supplied smooth dispersion. No exact universal packet-force law follows from the polynomial identity. A nonzero matrix anticommuting with all three content matrices is excluded; arbitrary gap mechanisms are not. Continuous-time evolution in an exponential unbounded field requires additional domain data; finite-slab propagation and a general ray limit are not proved."
upstream_dependencies:
  - minimal_axioms
runner: scripts/admissibility_rule_a_phase_timed_by_the_local_clock_every_packet_falls_towards_slow_clocks_force_is_energy_times_gradient_2026_09_21.py
---

# Clocked nearest-neighbour amplitudes: finite operator identities and conditional ray motion

**Date:** 2026-09-21
**Type:** bounded_theorem
**Status:** bounded-support (supplied mathematical models; unaudited)

This note works within a supplied clause for an amplitude whose phase is timed by local tick rates; it reports how such an amplitude moves in a given rate field; nothing is adopted and no gravitational claim is made.
No bridge, Born-weight, plane-or-sum or gravity statement enters this note as a premise; this note does not fire wake condition 1 of the parked statistical-bridge decision.
No value, constant or theorem is imported as authority; the standard mathematical imports are named at definition level.

## Result up front

The generator classification, weighted finite-matrix identities, and finite-support translation algebra survive review. The original exact force claim for every packet is withdrawn: an expectation of a product cannot generally be replaced by a product of expectations. The independent ray model has a valid acceleration formula, with velocity-dependent sign and lattice corrections. It is not an exact packet equation.

## Premises and declared objects

A supplied amplitude psi:Z^3->C^2 has content matrices sigma_j, the Pauli matrices. Define (T_e psi)(x)=psi(x-e), D_j=(i/2)(T_j-T_j^dagger), and H=sum_e A_e T_e, including e=0. H is Hermitian and covariant under proper cubic rotations acting on the content by conjugation of the sigma_j as a vector. This soldered action, amplitude dynamics and tick rates are extra model choices, not consequences of the axioms.

For fixed w_x>0, W=diag(w_x), the site-timed clause is i dotpsi=W H psi. The finite-volume statement below uses finite Hermitian matrices. On the infinite lattice its algebraic statements are on finite-support vectors; operator domains and extensions are separate. For the ray calculation supply a smooth real energy E(x,k)=w(x) epsilon(k), away from dispersion singularities, and Hamilton's equations dotx=partial_k E, dotk=-partial_x E. No assertion about record formation or a reading probability is made.

Named mathematical imports: Pauli matrix multiplication, similarity and weighted adjoints, finite-support difference operators, and Hamilton's ray equations. These are mathematical definitions or identities, not empirical inputs.

## Theorem T1 — classification and the anticommuting-mass boundary

The most general generator of the stated range and covariance has A_0=a_0 I and A_(+/-e_j)=a I +/- (i beta/2)sigma_j, with three real parameters. Its symbol is (a_0+2a sum_j cos k_j)I+beta sum_j sigma_j sin k_j.

To prove this, rotations fixing e_3 force A_(e_3)=a I+b sigma_3. A half turn reversing e_3 sends sigma_3 to -sigma_3, and transitivity fixes the same coefficients on all axes. Hermiticity gives real a and imaginary b=i beta/2; the onsite matrix commutes with all rotations and is scalar. The runner constructs the full real coefficient constraints and finds dimension3.

An optional inversion symmetry of the evolution has two distinct readings. The antiunitary map which reverses the content, combined with x->-x, must send H to -H to commute with exp(-iHt); it leaves only beta. A linear inversion leaving content unchanged instead requires H invariant and removes beta. This antiunitary spectral-reversal choice is an extra assumption, not ordinary spatial inversion alone.

Set beta=1 and a=a_0=0 for the walk used below. Anticommutation gives H^2=sum_j D_j^2 and i[H,X_j]=sigma_j(T_j+T_j^dagger)/2. Velocity equals sigma_j only at leading long wavelength, not throughout the lattice band. No nonzero X in M_2(C) anticommutes with all three sigma_j: expanding X in I,sigma_1,sigma_2,sigma_3 gives zero for every coefficient. This excludes a constant anticommuting mass matrix preserving the scalar-square dispersion. It does not exclude every spectral gap or rest-energy interpretation of a modified model. For example a sufficiently large scalar energy offset gaps zero without anticommuting, but changes the dispersion and the ray response.

## Theorem T2 — fixed-rate weighted evolution

For a finite Hermitian H and fixed positive W, (WH)^dagger W^-1=W^-1 WH. Thus sum_x |psi_x|^2/w_x is conserved. WH is Hermitian in the plain inner product exactly when [W,H]=0; nonuniformity alone is not enough to exclude this. The change chi=W^-1/2 psi gives H_w=W^1/2 H W^1/2, a Hermitian matrix. Sending-site timing HW is similar to the same matrix with the corresponding inverse change of variable. Identical canonical states and transformed observables give equivalent evolutions; assigning the same untransformed initial amplitude to different timing models need not do so.

Scaling w by t>0 scales H_w by t. If W varies in time, the receiving-site equation instead gives i dotchi=H_w chi-(i/2)dotu chi, and the weighted norm need not be conserved. Choosing i dotchi=H_w(t)chi without this connection term is a separately supplied canonical dynamics. Infinite-volume self-adjointness and bounded similarity require their own domain hypotheses.

## Theorem T3 — polynomial translation identity and a counterexample to its former interpretation

Suppose w(x+a)=lambda_a w(x). On finite-support amplitudes whose n-step neighbourhood and translate lie in that region, H_w^n T_a=lambda_a^n T_a H_w^n. Indeed W^1/2 T_a=lambda_a^1/2 T_a W^1/2, and translation-invariant H commutes with T_a; multiply and iterate. A translation-covariant bond timing homogeneous of degree one has the same property. The runner checks powers1 and3 for several rational exponential rates and shifts, and a nonexponential counterexample.

This is a finite-power identity. In a finite slab, continuous-time hopping produces small tails beyond any finite step neighbourhood; boundaries spoil an exact evolution identity. On an infinite exponential field the generator is unbounded and needs a compatible self-adjoint realization before functional calculus can be used. Neither issue is solved by polynomial checks. Conditional on a well-defined realization with the required intertwining relation, one could infer U(t)T_a=T_a U(lambda_a t); this note does not establish such a realization.

Even that stronger relation would not imply the original packet-force conclusion. At time zero, where the algebra is valid, z=<T_a> has dotz=i(lambda_a-1)<T_a H_w>. Its phase rate for z!=0 is (lambda_a-1) Re(<T_a H_w>/<T_a>), generally not (lambda_a-1)<H_w>.

An exact counterexample uses a line, w_x=4^x, and symmetric nearest-neighbour hopping H=T+T^dagger with H_w bond entries 2^(2x+1). Take real amplitudes1,2,3 at x=0,1,2, normalized by sqrt14. Then <T>=4/7 and <H_w>=52/7, while the phase rate is 519/16, not 156/7. All relevant products fit in the interior of the nine-site calculation, so the counterexample does not depend on boundary leakage. An exact nonzero-energy eigenstate of a compatible global intertwining relation would instead have <T>=0 when lambda_a!=1, making that phase undefined.

## Theorem T4 — conditional ray acceleration

For the independently supplied differentiable ray model E=w epsilon, let v_j=w partial_j epsilon and u=log w. Differentiation gives

`dotv_j = -w^2 sum_l M_jl partial_l u + 2(v dot grad u)v_j`, with `M_jl=partial_j partial_l(epsilon^2/2)`.

The first chain-rule term is (v dot grad u)v_j; the second is -w^2 sum_l epsilon partial_j partial_l epsilon partial_l u. Replacing epsilon partial_j partial_l epsilon by M_jl-partial_j epsilon partial_l epsilon yields the formula.

The particular universal form with M=I holds for every gradient exactly when epsilon^2=|k-k_0|^2+C on a connected region. For C>=0, |v|<=w. A ray at rest or transverse to the gradient has acceleration -w^2 grad u. A ray parallel to it has coefficient -w^2+2v^2, so acceleration reverses sign above |v|=w/sqrt2. Therefore even this continuum formula does not mean that every moving ray accelerates towards slow clocks with the same magnitude.

For the selected walk dispersion, M=diag(cos 2k_j). Adding a scalar m^2 to epsilon^2 preserves this identity as a separate dispersion model; it is not a three-dimensional two-component anticommuting mass construction. At long wavelength M=I+O(|k|^2). In the continuum massless model epsilon=|k|+e_0, transverse acceleration is -w^2(1+e_0/|k|)grad u. For the separately supplied scalar quadratic dispersion epsilon=e_0+|k|^2/(2M_0), a ray at rest has acceleration -(e_0/M_0)w^2 grad u. The runner's numerical examples of these last two formulas set w=1.

## No-Go Discipline Gate

### N1 — Alternative routes
Longer-range generators, larger internal spaces, scalar energy offsets, different rate timing, and different ray dispersions lie outside individual subclaims. The anticommuting-matrix obstruction is not a universal ban on gaps or composite masses.

### N2 — Wall independence
No repository no-go wall is assumed. Finite-support and fixed-rate restrictions are mathematical domain conditions.

### N3 — Hidden assumptions
The rate field in T2 is static. T3 requires a translation-compatible local region for every tested power. T4 assumes a smooth dispersion and ray equations; no general packet-to-ray theorem is supplied.

### N4 — Dependencies
The axioms supply the site algebra and symmetry context. The companion rate note motivates w but is not needed to prove its existence as a supplied input. The weak-field packet is a comparison target, not a theorem establishing this model's physical interpretation.

### N5 — Resolution
per_element: executed — content products, full generator coefficient constraints, optional inversion conditions and anticommuting-matrix rank.
per_site: executed — finite-support walk square, velocity operator and translation powers; explicit nonuniversal packet-phase example.
per_mode: executed — exact rational ray jets, lattice corrections, velocity-dependent sign, continuum offset and quadratic dispersion controls.
per_block: executed — fixed-rate weighted finite matrices on the side-three torus and degree-one timing scale.
lattice_wide: only the stated algebraic and conditional ray proofs; global unbounded evolution, universal packet force and record formation are not established.

### N6 — Partial closure and primitives
No primitive fixes this dynamics or supplies a packet-to-ray theorem. None is newly registered.

### N7 — Strongest objection
The polynomial identity cannot justify an exact force for arbitrary packets. The explicit counterexample establishes this objection; the claim is withdrawn, and the conditional ray law is kept separately.

### N8 — Historical scope
The original packet simulations, orientation comparisons and sideways-drift fits are historical author calculations, not a general ray-limit proof. Their exact programs and outputs remain recoverable with the original source.

## Original-source disposition and boundaries

PR #8570 at `664e733aa21f0288cdb49d1d474d56bdafdda362` on `physics-loop/admissibility-induced-law-block54-phase-timed-by-the-local-clock-every-packet-falls-towards-slow-clocks-20260921` preserves every original file and historical numerical table. Large packet experiments are deferred, not freshly reproduced by this canonical runner. T1 and T2 are retained with their hypotheses; T3 is narrowed to polynomial algebra with the false force interpretation explicitly refuted; T4 retains its mathematical ray content. No physical clock, source, force, or record-reading law is established.

## Dependencies

- [Minimal axioms](MINIMAL_AXIOMS_2026-06-29.md)
- [Local rate model](ADMISSIBILITY_RULE_NO_MASTER_CLOCK_A_NEIGHBOUR_DETERMINED_SCALE_COVARIANT_TICK_RATE_OBEYS_THE_LATTICE_LAPLACE_EQUATION_RECORDS_ENTER_AS_ADDITIVE_SOURCES_BOUNDED_THEOREM_NOTE_2026-09-21.md)
- [Weak-field comparison target](GRAVITY_WEAK_FIELD_SOURCE_RESPONSE_BRIDGE_BOUNDED_THEOREM_NOTE_2026-06-11.md)

## Verification

Run `python3 scripts/admissibility_rule_a_phase_timed_by_the_local_clock_every_packet_falls_towards_slow_clocks_force_is_energy_times_gradient_2026_09_21.py`. Review is not a formal audit verdict.
