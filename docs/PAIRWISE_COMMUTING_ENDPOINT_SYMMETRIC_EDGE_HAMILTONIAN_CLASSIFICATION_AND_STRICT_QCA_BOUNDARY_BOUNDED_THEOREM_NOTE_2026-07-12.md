---
claim_id: pairwise_commuting_endpoint_symmetric_edge_hamiltonian_classification_and_strict_qca_boundary_bounded_theorem_note_2026-07-12
claim_type: bounded_theorem
claim_scope: "Exact classification of endpoint-SWAP-symmetric Hermitian two-qubit edge densities whose translates commute on overlapping nearest-neighbor edges. Up to one uniform onsite basis, every such density is c II+r(ZI+IZ)+g ZZ. Its uniform cubic interaction gives an order-free common-Hamiltonian flow and a strict quasi-local automorphism of radius at most one, with exact radius one iff sin(2gt) is nonzero. Every common-axis onsite observable is conserved. The tensor carrier, identical-edge ansatz, overlap commutation, basis frame, coefficients, and time are supplied. Arbitrary common Hamiltonians, noncommuting or special-time cancellations, physical selection, clocks, probability, and continuum limits are not classified."
upstream_dependencies:
  - minimal_axioms
runner: scripts/common_edge_hamiltonian_overlap_commutation_classification_2026_07_12.py
---

# Pairwise-Commuting Endpoint-Symmetric Edge Hamiltonians

**Date:** 2026-07-12

**Type:** bounded theorem

**Status authority:** independent audit only. This source changes no axiom,
primitive, framework rule, or audit verdict.

**Primary runner:**
[`scripts/common_edge_hamiltonian_overlap_commutation_classification_2026_07_12.py`](../scripts/common_edge_hamiltonian_overlap_commutation_classification_2026_07_12.py)

**Cached output:**
[`logs/runner-cache/common_edge_hamiltonian_overlap_commutation_classification_2026_07_12.txt`](../logs/runner-cache/common_edge_hamiltonian_overlap_commutation_classification_2026_07_12.txt)

## Question and bounded answer

Can a single common nearest-neighbor Hamiltonian remove the matching-layer
order imported by the preceding circuit grammars while remaining an exactly
strict finite-radius qubit dynamics?

This note answers one deliberately strong sufficient-condition subproblem.
Let the same endpoint-SWAP-symmetric Hermitian density `h` be placed on every
undirected nearest-neighbor edge, and demand that its translates commute on
the three-site overlap:

```text
[h_12,h_23] = 0.                                           (1)
```

Then, for one Hermitian Pauli axis `N=n.sigma`, `|n|=1`, and real
`c,r,g`, exactly

```text
h = c I tensor I
  + r (N tensor I + I tensor N)
  + g N tensor N.                                         (2)
```

Conversely every density (2) satisfies (1). Up to one uniform onsite unitary
frame it is `c II+r(ZI+IZ)+g ZZ`. The resulting uniform cubic interaction is
an order-free simultaneous common-Hamiltonian dynamics. Its infinite-lattice
automorphism has strict graph radius at most one at every time and exact
radius

```text
R(t) = 1  if sin(2 g t) != 0,
       0  if sin(2 g t) = 0.                              (3)
```

All `N_x` are conserved. Thus this nonempty simultaneous class supplies phase
entanglement and bounded operator spreading, but no transport of the
common-axis configuration.

Equation (1) is not necessary for a common Hamiltonian. The result therefore
does not classify arbitrary common-Hamiltonian evolution or the full
strict-QCA problem.

## Existing-science reading gate

The actual minimal-axiom, matching-QCA, transfer-log, exact-H expansion,
finite-range Lieb--Robinson, and clock-factor sources were read before fixing
this claim.

- The approved [minimal axioms](MINIMAL_AXIOMS_2026-06-29.md) supply cubic
  geometry, spatial symmetry, and the one-site `M_2(C)` presentation. They do
  not supply a multisite tensor carrier, Hamiltonian, interaction density,
  time parameter, probability law, or process selector.
- The preceding matching-QCA sources are context only.
  In particular, the symmetric-Clifford matching classification's
  complete-layer cancellations show that local
  overlap commutation is not necessary even for schedule independence at a
  stroboscopic tick.
- The transfer-log source finds an exponentially quasilocal, generally not
  finite-range, exact logarithm in its supplied free staggered model.
- The exact-H expansion source obstructs one canonical BCH/Magnus route, not
  the exact spectral logarithm or all Hamiltonian reconstructions.
- The finite-range-H/Lieb--Robinson source gives a quasilocal propagation
  bridge under supplied finite-range Hamiltonian assumptions; a
  Lieb--Robinson cone is not strict finite-radius support.
- The independent commuting clock-factor source warns that tensor-factor
  locality alone does not select a unique physical clock.

Those context surfaces are not imported as proof authority here. The local
classification, factorization, and radius statements below are proved
self-containedly. The only declared graph dependency is `minimal_axioms`.

## 1. Exact local classification

Expand an arbitrary endpoint-SWAP-symmetric Hermitian two-qubit density in a
Hermitian Pauli basis:

```text
h = c II + sum_i b_i (sigma_i I + I sigma_i)
    + sum_ij C_ij sigma_i sigma_j,                         (4)
```

where `c` and `b_i` are real and `C` is a real symmetric `3 x 3` matrix.
Separating `[h_12,h_23]/(2i)` by its independent endpoint supports gives:

```text
row_i(C) cross b       = 0,
b cross row_l(C)       = 0,
row_i(C) cross row_l(C)= 0                 for all i,l.   (5)
```

The last family says that all nonzero rows of `C` are parallel, hence
`rank(C)<=1`. Symmetry then gives `C=g n n^T` for one real axis `n` after
absorbing its norm into `g`. The first two families say that `b` is parallel
to the same axis whenever `C` is nonzero. If `C=0`, the nonzero vector `b`
itself defines the axis; if both vanish, the density is scalar. This proves
(2), including every degenerate case. Direct substitution proves the
converse.

There is also a basis-independent certificate. The real symmetric
operator-Schmidt coefficient matrix of `h` can be orthogonally diagonalized:

```text
h = sum_a lambda_a A_a tensor A_a.                         (6)
```

Then

```text
[h_12,h_23]
 = sum_ab lambda_a lambda_b
   A_a tensor [A_a,A_b] tensor A_b.                        (7)
```

Independence of the outer factors makes (7) vanish exactly when the nonzero
Schmidt operators commute pairwise. A commuting Hermitian subspace of `M_2`
lies in `span{I,N}`, again giving (2).

## 2. Uniform cubic interaction and simultaneity

On a finite cubic region or finite torus let

```text
H_L = sum_{<xy>} h_xy.                                    (8)
```

Every two edge term either has disjoint support or overlaps through the same
axis `N`, so all terms commute. On a six-regular torus,

```text
H_L = c |E_L| I + 6 r sum_x N_x + g sum_{<xy>} N_x N_y.  (9)
```

Therefore

```text
exp(-it H_L) = product_{<xy>} exp(-it h_xy),               (10)
```

with no matching choice or edge order. Translation and proper-cubic spatial
covariance follow for the supplied trivial action of spatial rotations on the
internal qubit axis.

On the infinite lattice, (8) is not asserted to be a literal bounded global
Hamiltonian operator. The finite-range interaction instead defines the local
automorphism consistently: for a local observable, all factors disjoint from
its initial support can be moved next to it and cancel from conjugation. Only
incident edges remain. This is the strict quasi-local-algebra statement used
below.

## 3. Exact support radius

Choose a normalized raising operator `S^+_x` transverse to `N_x`. With the
Heisenberg convention `alpha_t(A)=exp(itH) A exp(-itH)`, equation (9) gives

```text
alpha_t(S^+_x)
 = exp(i 12 r t) S^+_x
   product_{y~x} exp(i 2 g t N_y).                         (11)
```

The product touches only the six nearest neighbors. It is scalar on every
neighbor exactly when `sin(2gt)=0`. Otherwise dependence on every incident
`N_y` is nontrivial, so one transverse onsite observable has exact graph
radius one. The same formula with `t -> -t` proves the identical inverse
radius. This proves (3). In particular, `g=0` is onsite at every time and
`gt in (pi/2) Z` gives the complete exceptional-time set.

For any finite input region, edge-factor commutativity permits all factors
not incident on the original region to cancel before conjugation, so support
never iterates beyond its one-neighborhood. This is stronger than a
Lieb--Robinson tail, but only because (1) imposed an exactly commuting
interaction.

## 4. Transport and selection boundary

For every site,

```text
alpha_t(N_x) = N_x.                                       (12)
```

Every common-axis product-basis configuration is stationary up to phase. On
a regular cubic lattice, every isolated flipped-axis configuration has the
same energy independent of its position, and no matrix element moves it.
Thus (2) has entangling phase dynamics when `g` is nontrivial, but it does not
provide a translating one-particle carrier or a growing common-axis signal
front.

The family is also continuously underdetermined: the axis `N`, `c,r,g`, time
unit, and tick duration are supplied rather than selected. Neither `N_x` nor
its eigenvalue is identified with framework Record, matter, probability, or
an empirical observable.

## 5. Result boundary

This theorem classifies only one identical endpoint-symmetric nearest-neighbor
two-qubit density under the strong pairwise-overlap condition (1). It does not
classify:

- arbitrary endpoint-symmetric `h` in the common sum `sum_e h_e`;
- noncommuting finite-range Hamiltonian flows with quasilocal tails;
- special finite times with exact cancellations;
- complete-layer cancellations, partitioned/Margolus dynamics, repeated
  layers, clock/control registers, larger cells, or multibody interactions;
- arbitrary strict QCAs, their phases or indices;
- an Admissibility-to-Hamiltonian realization or a physical law selector;
- a clock, dimensionful rate, probability rule, continuum limit, QFT,
  Standard Model, or GR limit.

The positive family (2), the open noncommuting common-Hamiltonian class, and
the remaining stroboscopic and larger-carrier routes mean that this result
does not establish that an axiom update is necessary.

## Falsifiers

- An endpoint-SWAP-symmetric Hermitian `h` satisfying (1) that cannot be put
  in form (2).
- A density in form (2) with a nonzero overlap commutator.
- Failure of finite-volume factorization (10), or dependence on edge order.
- Infinite-lattice support outside the one-neighborhood.
- Radius zero when `sin(2gt)` is nonzero, or radius one when it vanishes.
- Failure of any conservation identity (12).

## Reproduction

```bash
python3 scripts/common_edge_hamiltonian_overlap_commutation_classification_2026_07_12.py
```

## Dependencies

- [MINIMAL_AXIOMS_2026-06-29.md](MINIMAL_AXIOMS_2026-06-29.md) supplies only
  cubic geometry, spatial symmetry, and the one-site algebra boundary.

Context only: the preceding matching-QCA notes, transfer-log
quasilocality note, exact-H expansion obstruction, finite-range-H/LR bridge,
and independent clock-factor no-go. None is load-bearing proof authority for
equations (1)--(12).
