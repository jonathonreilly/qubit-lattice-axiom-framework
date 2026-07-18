# Isotropic Weyl-QCA Lattice Compatibility

**Date:** 2026-07-14

**Type:** meta

**Authority:** none. This is a literature-grounded compatibility test and
finite structural probe. It is not an axiom proposal, an audit verdict, a
re-proof of the cited classification, or a claim that quantum-walk kinematics
is already the framework's many-body sampled-record law.

## Why This Route Matters

There is a much stronger symmetry reduction in the QCA literature than the
pair-exchange result. D'Ariano, Erba, and Perinotti classify homogeneous local
unitary isotropic quantum walks on lattices in dimensions one through three
with minimal coin dimension `s=2`. In three dimensions, their classification
leaves two Weyl walks. The small-wave-vector limit is the Weyl equation.

Primary sources:

- [Isotropic quantum walks on lattices and the Weyl equation](https://arxiv.org/abs/1708.00826)
- [Free quantum field theory from quantum cellular automata](https://arxiv.org/abs/1601.04832)

This is exactly the kind of result the derive-first program should seek: strong
structural assumptions reduce a large law space to a tiny one. It therefore
deserves a direct compatibility check against the live foundation.

## The Adjacency Does Not Match

The live Lattice axiom fixes standard six-neighbor cubic adjacency on `Z^3`.
The nontrivial three-dimensional `s=2` isotropic walk in the cited
classification uses the body-centered-cubic Cayley graph: four positive
generators and their inverses, for eight neighbors. In a standard integer
embedding these are body diagonals such as

```text
(1,1,1), (1,-1,-1), (-1,1,-1), (-1,-1,1)
```

and their negatives. Each has Manhattan length three, not one. Both neighbor
sets are invariant under proper cubic rotations, but they are different
graphs. The cited result explicitly reports that only the BCC case supports
the nontrivial three-dimensional solution under its hypotheses.

Therefore the classification is not a direct completion of the current
standard six-neighbor Admissibility rule. Using it constitutionally would
require one of:

1. changing primitive adjacency to BCC;
2. deriving BCC propagation as a multi-step or block graph on the existing
   lattice;
3. relaxing the quantum-walk isotropy/locality/minimality hypotheses; or
4. using a staggered/multicell realization whose effective internal carrier is
   larger than one primitive site.

Option 2 or 4 is the least disruptive. A block/staggered encoding remains live,
but it needs an exact generated-composition, locality, and equivalence theorem.

## Coin Dimension Is Not Yet The Onsite Many-Body Carrier

The quantum-walk coin `s=2` is a two-component single-particle amplitude. A
second-quantized fermionic two-component field has two local modes and local
Fock dimension `2^2=4`; a four-component Dirac field has local Fock dimension
`2^4=16`. The live one-site algebra `M_2(C)` has Hilbert dimension two.

This does not rule out a Weyl/Dirac descendant. Staggering or a finite block of
primitive qubits can encode the components. It does rule out treating the
paper's `s=2` label as a theorem that one primitive `M_2` site already is the
complete many-body Weyl carrier.

## What The Classification Actually Selects

In three dimensions the result leaves two Weyl walks, the two chirality
partners. A parity or boundary condition may exchange or select them, but the
classification does not make one chirality uniquely actual. Coupling two Weyl
automata gives a Dirac automaton with a remaining normalized mass parameter.

The cited program obtains impressive free-field kinematics:

- a Weyl continuum limit from homogeneity, locality, isotropy, unitarity, and
  minimal internal dimension;
- Dirac dynamics after a larger coupled carrier and a mass parameter; and
- a composite free-Maxwell construction with additional qualifications.

It does not, by that classification alone, supply:

- interacting Standard Model dynamics or the exact Wilson/staggered effective
  sector used elsewhere in this repository;
- physical contexts, record formation, pointer permanence, or one actual
  outcome;
- Born sampling, a prepared-trial link, or empirical frequency law;
- record renewal, thermodynamics, gravity, or a cosmological boundary; or
- a theorem identifying BCC quantum-walk steps with the live clock metric.

## Constitutional Effect

This route materially narrows the search for the reversible kinetic part, but
it is not a direct completion of the four axioms. It reveals a precise fork:

- If standard six-neighbor adjacency is load-bearing, the Weyl-QCA uniqueness
  theorem must be reproduced through an exact block/staggered construction.
- If the BCC graph is fundamental, Lattice—not merely Admissibility—would need
  a constitutional change.

Neither choice should be made for drafting convenience. The first route fits
the existing framework's historical staggered program and should be attacked
before any lattice rewrite. Even if it succeeds, a sampled-record law and the
interacting/gravity lanes remain additional work.

## Verification

Run:

```bash
python3 scripts/isotropic_weyl_qca_lattice_compatibility_probe_2026_07_14.py
```

The runner checks the finite graph/carrier facts used in the compatibility
argument. It does not re-prove the published classification. Its PASS total is
not an independent evidence count.
