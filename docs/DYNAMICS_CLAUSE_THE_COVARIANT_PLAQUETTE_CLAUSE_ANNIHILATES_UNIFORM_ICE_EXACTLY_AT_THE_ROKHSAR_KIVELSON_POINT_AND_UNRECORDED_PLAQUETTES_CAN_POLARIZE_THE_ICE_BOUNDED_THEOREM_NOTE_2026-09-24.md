---
claim_id: dynamics_clause_the_covariant_plaquette_clause_annihilates_uniform_ice_exactly_at_the_rokhsar_kivelson_point_and_unrecorded_plaquettes_can_polarize_the_ice_bounded_theorem_note_2026-09-24
claim_type: bounded_theorem
claim_scope: Supplied soldered spin-half links and real covariant plaquette generators. The annihilator line is g(P_flip-U-Udagger); for g>0 its kernel is the span of flip-class uniform vectors. The coarse 2x2x2 torus has 9600 ice states, 937 classes, largest 864 and 760 frozen. Uniform readout does not select a unique mixed state. The specified D=0 normal-field plaquette potential has eight polarized minima for B>=0,J!=0; after adding a pure ring this remains true under 0<=g<(sqrt(B^2+2J^2)-B)/2. No preparation or thermodynamic phase is derived.
upstream_dependencies:
- minimal_axioms
runner: scripts/dynamics_clause_the_covariant_plaquette_clause_and_the_rokhsar_kivelson_point_2026_09_24.py
---

# Covariant plaquette generators, the RK kernel and a conditional polarization bound

**Type:** bounded_theorem

**Date:** 2026-09-24
**Status:** conditional-support; supplied finite models, unaudited.

## Supplied model and local algebra

Take four soldered spin-half links around a plaquette, with electric
eigenvalues ±1/2, fixed corner Gauss sums and the eight proper cubic
rotations preserving its site. All Hamiltonians, record contents and
readout below are supplied; the [minimal axioms](MINIMAL_AXIOMS_2026-06-29.md)
do not select them.

Orient the four fields relative to circulation. Their sixteen configurations
form four rotation orbits: flippable (all circulation signs equal), size two;
opposite, size two; adjacent, size four; and odd, size eight.
Only the two flippable configurations have the same four corner sums,
so only their block admits a nondiagonal Gauss-preserving operator.
A stabilizer exchanging them removes the imaginary ring coefficient.
The covariant Hermitian space therefore consists of four orbit projectors
and one real ring U+U†.

Requiring a generator to annihilate every nonflippable basis state forces
the other three orbit coefficients to zero. Annihilating the equal-amplitude
flippable vector then equates the flippability and negative ring coefficients:

    H_p=g(P_flip-U-U†)=2g |minus><minus|.

This is positive semidefinite for g≥0. The ground-space characterization
below requires g>0. At g=0 every vector is a ground state; for g<0 the
uniform zero vector need not minimize the energy.

## Finite graph and readout

On the coarse 2x2x2 torus there are eight vertices and twenty-four oriented
links. The two orientations with the same endpoint pair are distinct
link qubits; plaquette multiplicities are retained. Exact ice enumeration
and flip connectivity give 9600 states, 937 components, a largest component
of 864 states and 760 isolated configurations.

For g>0 the summed local term is the weighted flip-graph Laplacian.
Its quadratic form is a sum g|psi(c)-psi(c')|² over flip edges.
It vanishes exactly when amplitudes are constant on each connected
component. Thus the normalized class-uniform vectors form a basis
of the ground space. Every coherent superposition of them is also
a ground state, as is every density operator supported there.
The pure-ring Hamiltonian on the largest class has a nonuniform
ground vector, checked with a seeded eigensolver and residual.

Under a supplied configuration-basis Born/trace readout, class-diagonal
mixtures give globally uniform probabilities when the class weights are
their sizes divided by 9600. That does not select a unique quantum state:
the coherent uniform superposition over all configurations has the same
readout, as do suitable coherent class combinations. There is no preparation
theorem. A classical positive local specification selecting a finite joint
measure would likewise not supply a quantum ground-state preparation.

## Unrecorded plaquette qubit and ring competition

For the specified D=0 coupling after exact Gauss-sector compression,
an unrecorded plaquette qubit sees

    B_eff=B n+J sum_l E_l e_l,

where n is the plaquette normal, B≥0 and J is real.
Its minimized energy is -|B_eff|/2. The four orbit energies are

| Orbit | Energy |
|---|---|
| Flippable or opposite | -B/2 |
| Odd | -sqrt(B²+J²)/2 |
| Adjacent | -sqrt(B²+2J²)/2 |

For J≠0 the adjacent configurations uniquely minimize the local potential.
On the specified torus, enumeration gives exactly eight ice configurations
adjacent on every plaquette: the fields are constant along each axis,
with independent axis signs. None is flippable. At J=0 all configurations
instead have equal potential.

An added ring cannot be ignored merely because it occurs at fourth order
in some other model. Here is a sufficient comparison for the specified
potential plus -g(U+U†). Subtract the adjacent energy from each plaquette.
The nonflippable diagonal energies are nonnegative. The flippable block is

    [[Delta_f,-g],[-g,Delta_f]],
    Delta_f=(sqrt(B²+2J²)-B)/2.

For 0≤g<Delta_f, that block is positive definite, and the only local
zero states are the four adjacent configurations. The summed Hamiltonian
therefore has precisely the same eight global zero configurations above
its subtracted energy on this finite torus. At equality extra local
zeros occur; above it this argument gives no phase conclusion.
The primary checks a representative strict inequality in addition to
the analytic two-by-two bound.

This treatment minimizes the supplied plaquette qubit at fixed link
configuration; implementing the resulting effective potential alongside
other quantum dynamics needs its own elimination/scale control.
Recorded plaquettes with normal record contents have different compression
behavior; arbitrary record contents are not covered by a no-potential claim.
The original D=J minimizer enumeration and unconditional phase narrative
are deferred on the preserved PR branch.

## Evidence and negative-claim discipline

The [primary](../scripts/dynamics_clause_the_covariant_plaquette_clause_and_the_rokhsar_kivelson_point_2026_09_24.py)
and [receipt](../logs/runner-cache/dynamics_clause_the_covariant_plaquette_clause_and_the_rokhsar_kivelson_point_2026_09_24.txt)
check orbits, annihilator coefficients, exact finite counts, spectral residuals,
coherent readout and the local competition bound. No audit verdict is applied.

### N1
Examined alternatives are the RK line, pure ring, class mixtures/coherences
and the specified unrecorded-plaquette potential with a bounded ring.

### N2
Annihilating uniform ice, selecting a ground space and preparing a particular
state are distinct obligations.

### N3
Link variables, Gauss sectors, couplings, normal fields and readout are
supplied. No native quantum law or state selector is derived.

### N4
The explicit local algebra and finite graph carry these claims. Classical
measure-selection results do not imply quantum state preparation.

### N5
Five resolutions are retained: require g>0 for the ground-space statement;
include coherent counterexamples to unique-mixture selection; preserve
parallel-link geometry; bound ring competition by Delta_f; and separate
record/phase/preparation obligations. The runner reports each resolution.

### N6
Arbitrary record orientations, D!=0 couplings, unrestricted ring strengths,
thermodynamic phases and preparation remain open.

### N7
Coherent uniform states and g=0 are direct counterexamples to broader
uniqueness statements. They are not hidden by the finite enumeration.

### N8
The RK Laplacian mechanism is established model mathematics. This finite
application does not derive a photon phase or a physical gauge sector.
