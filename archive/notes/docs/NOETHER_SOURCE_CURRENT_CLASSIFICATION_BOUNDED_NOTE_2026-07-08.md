# Finite-Basis Computational Conserved-Density And Source Classification

**Date:** 2026-07-08
**Type:** bounded_theorem
**Claim scope:** A deterministic floating-point computation classifies the
nullspace of a declared finite basis of nonconstant,
translation-covariant local densities modulo the identity
for five seeded coupling samples of a two-species one-dimensional fermion
Hamiltonian. At support windows of four and six sites and fermionic degree at
most four, the computed nullspace is three-dimensional and matches the two
species charges and the Hamiltonian density within the stated numerical gates.

**Primary runner:**
[`scripts/noether_source_current_classification_2026_07_08.py`](../scripts/noether_source_current_classification_2026_07_08.py)
**Runner cache:**
[`logs/runner-cache/noether_source_current_classification_2026_07_08.txt`](../logs/runner-cache/noether_source_current_classification_2026_07_08.txt)

## Declared Computational Surface

The comparator has two fermion species on a one-dimensional staggered chain.
Its cell Hamiltonian includes species hoppings `t_a,t_b`, staggered masses
`m_a,m_b`, on-site inter-species density coupling `U`, intra-species
nearest-neighbor density couplings `V_a,V_b`, and inter-species
nearest-neighbor density coupling `W_ab`.

The candidate density space is finite. Its elements are anchored, nonconstant,
Hermitian,
per-species-number-conserving, normal-ordered fermion operators with support
window `W in {4,6}` sites and fermionic degree at most four. The runner builds
the commutator map

```text
rho(o) = sum_m [tau^m(h), o]
```

in this basis and obtains its nullspace by floating-point singular-value
decomposition. Five coupling vectors are drawn deterministically from
`[0.3,1.7]^8` with seed `20260708`. A singular-gap gate of `10^6`, explicit
overflow accounting, and principal-angle comparisons define the numerical
classification.

The constant identity density is explicitly omitted: it is a trivial central
direction whose inclusion would add one null vector without changing the
nonconstant classification below.

This Hamiltonian family is a declared comparator input. Nothing in this note
claims that Record, Admissibility, or the other framework axioms select this
Hamiltonian or any dynamics.

## Results

1. **Computed membership.** At the checked samples, the two species charges
   `Q_a,Q_b` and the Hamiltonian density `h` lie in the numerical nullspace.
   Across all five samples, the worst commutator residual is `3.3e-16` and the worst reported
   principal-angle mismatch is `1.8e-13`.
2. **Finite-basis sample classification.** For all five seeded samples, the
   computed nullity is three at both support windows. The minimum gated
   singular separation is `4.2e14`; no output monomial is dropped.
3. **Controls.** With interactions removed, the six-site-window nullity is
   `20`. With the species decoupled but intra-species interactions retained,
   it is `4`, with separate species energy densities represented in the
   computed kernel.
4. **Named candidates.** The staggered charge and the two species particle
   currents have numerical commutator residual at least `1.0` at every checked
   sample and window.

## Conditional Source Reading

If a separate model assumes that a static source is a conserved density and
restricts its candidate source to this same finite operator basis, then at the
five checked samples the numerical source candidates reduce to

```text
alpha_a Q_a + alpha_b Q_b + gamma H.
```

This is only a classification inside the declared finite basis and sampled
parameter set. It does not select `gamma H`, exclude charge admixtures outside
the basis, derive species blindness, establish gravity, or supply field
dynamics.

## Independent Checks Built Into The Runner

- The normal-ordering/commutator implementation is compared with sparse
  many-body matrices on an open eight-site chain.
- A separate Jordan-Wigner/Pauli-string construction checks the finite-ring
  Hamiltonian representation.
- The free and decoupled controls change the computed nullity in the expected
  directions without being used to infer behavior away from the checked
  points.

## Boundaries

- This is bounded computational evidence, not an exact or generic-coupling
  theorem. No exact nonzero minor or symbolic rank proof is supplied.
- The classification is limited to `d=1`, two species, the displayed
  Hamiltonian family, degree at most four, windows at most six sites, and five
  seeded floating-point samples.
- Constant densities are quotiented out by omitting the identity basis element.
- The result says nothing about exhaustive gauged operator bases, continuum
  limits, transfer-operator formulations, gravitational sources, or dynamics.
- Audit classification and verdict remain the responsibility of the
  independent audit lane.

## Dependencies

No prior source note is load-bearing. The comparator, finite basis, numerical
gates, and controls are declared in this note and implemented by the paired
runner.
