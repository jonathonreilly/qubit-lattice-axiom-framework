The supplied five-state SU(2) link model needs compatible overlapping patches,
retained boundary flux, and an explicit placement on native qubits. This PR
provides three connected finite-model results, with the physical law and
continuum identifications kept separate.

- **Two plaquettes:** the complete closed sector has four states, with exact
  shared-link commutator `[B_L,B_R]|L> = -3|R>`. A joint exponential preserves
  gauge invariance and square exchange; the specified ordered and Strang
  products have explicit exchange defects.
- **Boundary gluing:** cutting is an isometric, coassociative reconstruction
  that intertwines transporters and their adjoints. Electric weights must
  count the original edge once. Retaining boundary irreps and multiplicities
  reconstructs all 18 closed states of the four-plaquette square in three
  groupings; premature zero flux gives 4 and clipped multiplicity/channel
  gives 16. The open-boundary count is obtained without a dense matrix.
- **Native placement:** four collinear native qubits encode one link and its
  reversal by literal site permutation. At coarse spacing five, all 125 grid
  origins form orthogonal code sectors on the same one-qubit-per-site lattice.
  Their direct sum is invariant under every native translation and proper
  cubic rotation. Local 24-qubit projectors distinguish the origins and give
  an exact finite-range extension of a supplied cubic gauge Hamiltonian.

The native construction retains an extra encoding-origin degree of freedom,
12 active qubits and 113 fixed spectators per coarse cell. It is a chosen
quantum code, not an origin-free single copy or a physical code-selection
mechanism. Its interactions reach beyond nearest neighbors. Regional gluing
on the fixed coarse graph is preserved; subdivision requires separate target
register allocation. Native Admissibility/Record dynamics, physical state,
clock, couplings, and continuum comparison remain open. No vacuum or mass-gap
closure, axiom edit, or evidence that the framework is physically correct is
claimed. Explicit finite dimension comparisons also reject the same-site-count
full-sector identification under ordinary tensor composition.

Validation and evidence:

- Separate coordinate and Haar/fusion derivations agree on the pair and
  boundary results, with different graph-counting routes. A fresh native
  placement derivation independently gives capacity bounds and a different
  invariant code using spacing-nine markers. The supervisor's spacing-five
  construction was frozen before reading that result. Same model family and
  shared raw premises remain limitations on independence.
- Complete mathematical source comparisons and scoped correction receipts
  are preserved. These are research checks, not formal landing panels or audits.
- Five production runners have successful content-bound caches. The native
  runner checks all 625 matrix-unit products, all phase residues and proper
  rotations, support geometry and graph ranks using exact arithmetic. No
  enormous native Hilbert-space matrix is constructed.
- Mutations test normalization, operator order, energy counting, boundary
  constraints and multiplicity in the earlier packets. Three separate native
  faults reject incorrect reversal parity, nonzero quiescent overlap, and a
  preferred origin. Full successful and failed execution evidence is preserved.
- Focused syntax, vocabulary, local links, source identities, cache evidence
  and diff checks passed. Full pipeline and formal landing/audit remain pending.

These are conditional bounded theorems supporting GB1-CF, not full GB1-CF
closure. The capacity evidence consists of explicit finite counterexamples;
the committed scope check claims no general negative-packet PASS. Other codes,
emergent sectors and frameworks remain live. No audit authority, premise
registry, or shared instruction files change.

The existing pair and boundary research packs index complete proofs, original
outputs, worker briefs, source identities and recovery paths. The current
checkpoint is `.claude/science/physics-loops/gb1-cf-boundary-gluing-20261107/STATE.yaml`;
its `native_placement/HANDOFF.md` indexes the latest result.
