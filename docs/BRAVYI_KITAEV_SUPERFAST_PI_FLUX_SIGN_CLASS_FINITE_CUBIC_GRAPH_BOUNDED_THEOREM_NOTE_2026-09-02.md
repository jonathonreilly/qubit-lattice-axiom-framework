---
claim_id: bravyi_kitaev_superfast_pi_flux_sign_class_finite_cubic_graph
claim_type: bounded_theorem
claim_scope: "On the explicitly declared open 2x2x2, 3x3x3, and 4x4x4 cubic graphs and the periodic 4x4x4 cubic torus only: the Bravyi-Kitaev-superfast encoded four-hop face transport equals the face stabilizer with its Z4 phase; the all-minus face syndrome is algebraically consistent; for the torus Wilson triple fixed explicitly to (+,+,+), its induced edge-sign field is Z2-gauge equivalent to the separately declared staggered-pattern sign field and has the same checked Hermitian hopping spectrum; and on the open 2x2x2 graph the all-minus stabilizer sector has dimension 128 and its encoded hopping spectrum matches the even-parity free-fermion spectrum."
upstream_dependencies: []
runner: scripts/bravyi_kitaev_superfast_pi_flux_sign_class_finite_cubic_graph_check_2026_09_02.py
---

# BKSF pi-flux sign class on four finite cubic graphs

**Date:** 2026-09-02

**Type:** bounded_theorem

**Status:** proposed_retained

**Audit:** unset; independent audit remains a separate lane.

**Primary runner:**
[bravyi_kitaev_superfast_pi_flux_sign_class_finite_cubic_graph_check_2026_09_02.py](../scripts/bravyi_kitaev_superfast_pi_flux_sign_class_finite_cubic_graph_check_2026_09_02.py)

**Runner cache:**
[bravyi_kitaev_superfast_pi_flux_sign_class_finite_cubic_graph_check_2026_09_02.txt](../logs/runner-cache/bravyi_kitaev_superfast_pi_flux_sign_class_finite_cubic_graph_check_2026_09_02.txt)

## Boundary

This is a finite theorem about explicitly declared cubic graphs, a standard
Bravyi-Kitaev-superfast-style edge-qubit encoding, and a separately declared
edge-sign pattern. It does not identify the graphs with the framework's
physical lattice, the sign pattern with a landed kinetic law, or the encoded
states with an emergent physical fermion. It makes no continuum, spin/taste,
cubic-representation, chirality, role-pattern, labelling, or dynamical-sector
claim.

The retained fixtures are only:

- open `2x2x2`, `3x3x3`, and `4x4x4` cubic graphs;
- the periodic `4x4x4` cubic torus with Wilson triple supplied as
  `(+1,+1,+1)`.

No universal torus-period classification is asserted. The Wilson triple is a
required boundary-condition input, not a consequence of the face syndrome.

## Declared algebra

Each undirected graph edge carries one qubit. At each vertex `i`, order the
incident directed edges and define the usual edge operator `A_ij` as one `X`
on edge `ij`, dressed by the preceding incident `Z` operators at its two
endpoints, with the directed sign chosen so `A_ji=-A_ij`. Define

```text
B_i = product of Z_e over edges incident to i.
```

For an oriented four-edge face `f=(i,j,k,l)`, define

```text
S_f = i^4 A_ij A_jk A_kl A_li.
```

For a directed legal hop from an occupied vertex `i` to an empty adjacent
vertex `j`, define the single-hop operator

```text
h_(j<-i) = (i/2) A_ij (B_i - B_j).
```

On that source-occupied/target-empty subspace `B_i-B_j=-2`, so
`h_(j<-i)=i A_ji`.  The ordered four-hop transport in T1 is the product of
these reduced legal-hop operators.  On the open cube the encoded hopping
Hamiltonian used in T4 is declared explicitly as

```text
H_enc = sum_{positively oriented edges (i,j)} (i/2) A_ij (B_i - B_j).
```

The runner constructs these operators in exact `Z4` symplectic form
`i^k X^x Z^z`. It checks multiplication phases, Hermiticity, squares,
commutators, and every face relation without dense-matrix tolerance.

## Results

### T1. Encoded face transport

On every face of all four fixtures, the ordered product of the four legal hop
operators `i A_ji` equals `S_f` exactly, including the `Z4` phase. Every retained `S_f`
is a Hermitian involution, the face operators commute pairwise, and each
commutes with every `B_i`. The runner also enumerates all computational basis
states of the open cube and checks that the factor `B_j-B_i` equals `2` on
every directed source-occupied/target-empty hop.

### T2. All-minus face syndrome

For each fixture, every `F2` relation among face stabilizers is multiplied in
the Pauli algebra and has product `+I` and even support. Independently, the
binary face-incidence system with right-hand side one is solvable. These two
checks establish consistency of the finite `S_f=-1` syndrome on the four named
graphs only.

### T3. Explicit sign-class witness

The all-minus syndrome and a spanning-tree gauge convention determine an edge
sign field after all independent cycle eigenvalues are supplied. On the
periodic fixture those data include the required Wilson triple
`(+1,+1,+1)`. The runner verifies every face holonomy is `-1`, verifies all
three torus Wilson products directly, and constructs a vertex-sign function
`s(v)` satisfying, edge by edge,

```text
eta_staggered(v,w) = s(v) s(w) eta_induced(v,w),
```

where the separately declared pattern is

```text
eta_1(v)=1,
eta_2(v)=(-1)^(v_1),
eta_3(v)=(-1)^(v_1+v_2).
```

This is a finite `Z2` gauge-equivalence statement. It does not assert that the
declared pattern is supplied by another framework artifact.

### T4. Hopping spectra

For every fixture, form the Hermitian adjacency

```text
K_eta = sum_(v,w) eta_vw (|v><w| + |w><v|).
```

The sorted, unrounded eigenvalues for `eta_induced` and `eta_staggered` agree
with `rtol=0` and `atol=1e-9`; the runner prints the maximum absolute error.
This is explicitly numerical corroboration of the exact edge-by-edge gauge
witness.

On the open cube, the face-stabilizer rank is exactly `5`, so the all-minus
joint eigenspace in the `2^12` edge-qubit Hilbert space has dimension
`2^(12-5)=128`. The vertex-star rank is exactly `7`, giving the same `128`
even-parity `B` syndromes. A deterministic basis is constructed by stabilizer
projection of computational basis vectors using complex NumPy arithmetic,
with nonzero seeds selected at norm threshold `1e-12` and then numerically
normalized. In that basis, the encoded hopping is numerically Hermitian and
its sorted `128` eigenvalues agree with the even-occupation sums of the eight
one-particle eigenvalues at `rtol=0` and `atol=1e-11`.

## Evidence and falsifiers

The algebraic and rank/dimension checks use integer bit masks and exact
`F2/Z4` arithmetic. The deterministic projected-basis construction, its
Hermiticity check, and the two explicitly labelled eigenvalue comparisons use
floating-point arithmetic with the thresholds stated above. The runner
contains required falsifiers for:

- a transport phase/sign flip;
- a corrupted face-incidence bit;
- each of the three Wilson signs independently;
- one changed induced edge sign;
- omission of one independent face-stabilizer constraint;
- a `1e-7 I` one-particle spectral shift;
- a perturbed encoded many-body target.

Each mutation must be rejected for the runner to pass. The paired cache pins
the runner hash and direct output. Neither the cache nor this note supplies an
audit verdict.

## What does not move

This source changes no axiom, primitive, framework rule, physical dictionary,
audit status, effective status, or retained-grade label. Its path-derived
claim remains unaudited pending the independent audit lane.
