---
claim_id: symmetric_two_qubit_clifford_cubic_matching_qca_classification_bounded_theorem_note_2026-07-11
claim_type: bounded_theorem
claim_scope: "Exhaustive projective-automorphism classification of all 192 endpoint-SWAP-symmetric two-qubit Clifford gates used identically in the six parity-matching, exactly-once cubic macro-tick grammar. Under uniform onsite Clifford conjugacy there are 26 gate classes. The gates split 48/48/96 into 1, 8, or 720 exact signed-Pauli schedule automorphisms; schedule multiplicities, spatial/cyclic quotients, invariance, forward/inverse radii, and local-overlap commutation are exact. The tensor carrier, Clifford gate class, parity origin, composition grammar, and tick graining are supplied. No arbitrary-QCA, common-Hamiltonian, phase/index, or physical-selection theorem is claimed."
upstream_dependencies:
  - minimal_axioms
runner: scripts/symmetric_two_qubit_clifford_cubic_matching_qca_classification_2026_07_11.py
---

# Symmetric Two-Qubit Clifford Cubic Matching-QCA Classification

**Date:** 2026-07-11

**Type:** bounded theorem

**Status authority:** independent audit only. This source changes no axiom,
primitive, framework rule, or audit verdict.

**Primary runner:**
[`scripts/symmetric_two_qubit_clifford_cubic_matching_qca_classification_2026_07_11.py`](../scripts/symmetric_two_qubit_clifford_cubic_matching_qca_classification_2026_07_11.py)

**Cached output:**
[`logs/runner-cache/symmetric_two_qubit_clifford_cubic_matching_qca_classification_2026_07_11.txt`](../logs/runner-cache/symmetric_two_qubit_clifford_cubic_matching_qca_classification_2026_07_11.txt)

## Question and result

Block08 found one schedule product for CZ and eight for iSWAP. Are those gates
representative of the full endpoint-symmetric two-qubit Clifford class?

The exhaustive answer is a three-level classification:

| symmetric projective Clifford gates | uniform onsite-basis classes | products among 720 schedules | multiplicity |
|---:|---:|---:|---:|
| 48 | 10 | 1 | 720 |
| 48 | 10 | 8 | 90 each |
| 96 | 6 | 720 | 1 each |

Thus CZ and iSWAP represent the first two levels, but half of the symmetric
Clifford gates are fully order-faithful: every schedule is a different
automorphism.

This uses “Clifford” as a Pauli-normalizing Clifford-group automorphism. It is
a Clifford-group automorphism, not the static Clifford algebra used in other
repo lanes.

## Existing-science reading gate

The actual qubit-QCA, scalar CAR-QCA, matching-order, tensor-carrier, Bloch
tick, eta-twisted, tick/Admissibility, transfer-log, and exact-H-expansion
sources were read before this classification.

- The approved [minimal axioms](MINIMAL_AXIOMS_2026-06-29.md) supply cubic
  geometry, spatial symmetry, and the one-site `M_2(C)` presentation, but no
  global tensor product, Clifford-group gate, schedule, tick, or Hamiltonian.
- The Block08 two-gate and Block07 CAR results are branch-local/audit-pending
  context. Their algebra is not imported here.
- The retained lattice light-cone result supplies only generic declared-local
  graph reachability. The ordinary two-site tensor carrier remains a supplied
  mathematical realization on this surface.
- Existing simultaneous-tick sources are one-particle Bloch/Laurent results,
  not many-body Clifford-QCA classifications.
- No repo source supplies a GNVW or higher-dimensional QCA index, a Margolus
  phase classification, or a common-edge-Hamiltonian theorem.

The group generation, symmetry filter, schedule census, and infinite-lattice
support action are recomputed exactly by the runner.

## 1. Finite gate class

Work modulo scalar unitary phase and retain the complete signed action on all
Hermitian two-qubit Paulis. `H_1,H_2,S_1,S_2,CNOT_(1->2)` generate exactly

```text
|Cliff_2 / U(1)| = 11520.                                  (1)
```

Let `W` exchange the two endpoints. An unoriented edge gate is eligible when
its projective automorphism commutes with `W`. Exact signed-Pauli composition
gives

```text
|Centralizer_Cliff(W)| = 192.                              (2)
```

This is a projective-automorphism count, not an exact global-unitary count.
Pauli signs are retained; a bare binary symplectic matrix would be
insufficient.

A uniform onsite frame `C` sends

```text
G -> (C tensor C) G (C tensor C)^dag.                      (3)
```

Because every matching is perfect, (3) conjugates the complete lattice
automorphism by the same global onsite frame and preserves product counts,
spatial covariance, and range. The 24 single-qubit projective Clifford frames
split the 192 gates into 26 orbits with sizes

```text
1^2, 3^6, 6^10, 8^2, 12^4, 24^2.                         (4)
```

Uniform onsite conjugacy is only a basis quotient. Independent endpoint
frames, local left/right multiplication, and arbitrary finite-depth phase
equivalence are not quotiented.

## 2. Infinite period-two automorphism certificate

Use the same six parity matchings and exactly-once schedule as Block08. For
each gate and schedule, the runner propagates `X` and `Z` from each of the
eight parity origins through the six infinite matching layers. These 16 signed
finite Pauli strings determine the complete period-two Clifford automorphism.

No torus extrapolation is used. The support remains finite, so this is a direct
automorphism of the supplied quasi-local qubit algebra on `Z^3`. It also avoids
the wraparound aliases that a depth-six circuit can have on small tori.

## 3. Exact trichotomy

### Schedule-independent level: 48 gates

Twenty-four product gates give onsite automorphisms of exact graph radius zero.
Twenty-four entangling gates give exact graph-radius-one automorphisms. Every
schedule produces the same translation- and proper-cubic-invariant result.

Local three-site overlap commutation is sufficient but not necessary:

```text
36 gates: G_01 G_12 = G_12 G_01 as automorphisms;
12 gates: local overlap does not commute, but the six complete
          perfect-matching layers still give one product.          (5)
```

The second line is a genuine layer-assembly cancellation, so a purely local
edge-commutator test would miss one quarter of this level.

### Axis-orientation level: 48 gates

Twenty-four are SWAP-product gates and 24 are entangling. For every gate, the
product depends exactly on the three relative orders of the two parity layers
on each axis. Hence there are eight products with 90 schedules each.

All eight products form one spatial orbit and one cyclic time-origin
conjugacy orbit. No member is invariant under every unit translation or every
proper cubic rotation. Every product has exact nearest-neighbor graph/`l1`
radius six and `l_infinity` radius two.

### Fully order-faithful level: 96 gates

All 96 gates are entangling and all 720 schedules give distinct signed-Pauli
automorphisms. The products split into

```text
15 space-group orbits of size 48;
120 cyclic time-origin orbits of size 6.                   (6)
```

No product is invariant under every unit translation or under every proper
cubic rotation. Every forward automorphism again has exact graph radius six and
`l_infinity` radius two.

## 4. Inverses and Hamiltonian boundary

For an arbitrary gate in this class,

```text
U_pi(G)^(-1) = U_(reverse pi)(G^(-1)).                    (7)
```

The runner constructs the exact inverse signed-Pauli map and verifies that
forward and inverse graph/`l_infinity` radii match in all 26 basis classes.
Unlike the special six-layer iSWAP identity, fixed-gate schedule reversal is
not asserted for a general gate.

Equation (5) is automorphism-level commutation. It does not establish exact
unitary commutation with a chosen scalar phase, commuting Hermitian logarithms,
or a common Hamiltonian `exp(-i sum_e h_e)`. The 12 layer-cancellation gates
show especially clearly why schedule independence is not itself a local
commuting-Hamiltonian theorem. Noncommuting logarithms with special
stroboscopic cancellations remain a separate problem.

## 5. Result boundary

This theorem exhausts every endpoint-symmetric two-qubit Clifford-group
automorphism in one identical-gate, six-matching, exactly-once grammar. It
does not classify arbitrary qubit QCAs, non-Clifford or continuously
parameterized gates, oriented/axis-dependent gates, inserted onsite layers,
alternative covers, repeated or partial schedules, clock registers, or
Margolus grammars.

It establishes no QCA phase, index, topological class, excitation-transport
classification, physical gate selector, Record coupling, probability rule,
clock, rate, continuum limit, Standard Model limit, or GR limit. Entanglement,
Pauli spreading, and occupation transport are distinct; general Clifford
gates need not conserve computational occupation.

It does not establish a common Hamiltonian. It does not establish that an
axiom update is necessary. Non-Clifford gates, common-Hamiltonian evolution,
clocked/partitioned circuits, larger cells, schedule averaging, and a derived
Admissibility-to-update realization remain live.

## Falsifiers

- A projective two-qubit Clifford outside the generated 11,520-element group,
  or a SWAP-centralizing count different from 192.
- A uniform onsite Clifford quotient different from the 26 orbits in (4).
- A symmetric gate whose schedule count is not `1`, `8`, or `720`, or a gate
  count different from `48/48/96` across those levels.
- Failure of the `720`, `90`, or `1` schedule multiplicities.
- An eight-product or fully order-faithful member with graph radius below six,
  or a mismatch between forward and inverse radius.
- A member in either nonunique level invariant under all unit translations or
  under all proper cubic rotations.
- Local overlap commutation outside the 36-gate subset, or failure of complete
  layer cancellation for the additional 12 unique-product gates.

## Reproduction

```bash
python3 scripts/symmetric_two_qubit_clifford_cubic_matching_qca_classification_2026_07_11.py
```

## Dependencies

- [MINIMAL_AXIOMS_2026-06-29.md](MINIMAL_AXIOMS_2026-06-29.md) supplies only
  cubic geometry, spatial symmetry, and the one-site algebra boundary.

Context only: the Block07/08 sources, overlap-order source, tensor-carrier and
light-cone notes, one-particle simultaneous-tick/eta sources,
tick/Admissibility bridge, transfer-log note, and exact-H-expansion
obstruction. None is load-bearing proof authority for equations (1)--(7).
