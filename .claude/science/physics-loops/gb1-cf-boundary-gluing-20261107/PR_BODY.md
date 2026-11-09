The supplied five-state SU(2) link model needs compatible overlapping patches,
retained boundary flux, and an explicit placement on native qubits. This PR
provides four finite-model notes and three checked research continuations. The
physical law and continuum identifications remain open.

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
- **Neighborhood propagation and records:** a fixed conditional record-copy
  law relays a record through successive neighbors. For the quantum code,
  19 adjacent pair gates and seven onsite gates measure the full five-state
  electric Casimir, with one fresh output and no work qubits. The completed
  instrument restores the active code, preserves occupied-sector coherence
  and commutes with endpoint gauge actions, including on entangled patches.
- **All-origin output registers (research packet):** releasing only the coarse
  vertices for output preserves the orthogonality of all 125 origin sectors.
  Each coarse cell then has 12 active qubits, one output and 112 fixed qubits.
  A supplied finite, covariant instrument measures incident electric sectors,
  appends an outcome, and protects every prior record through a guard on its
  entire support. The supplied native Hamiltonian, including magnetic terms,
  restricts to `H tensor I_outputs` on the enlarged code. The proof and checks
  are in `native_records/RESULT.md`; canonical note packaging remains pending.
- **Preparation and history (research packet):** a binary header and spatially
  ordered permanent log on the existing free vertices determine a finite CP
  history, with magnetic pulses or separately recorded magnetic ticks. Seven
  intrinsic marker records identify the frame, so no external counter or
  preferred origin is used. The next-content kernel reads a finite neighborhood
  of radius `10(d+N)+35` for a fixed experiment budget. A rank-one preparation
  herald certifies the post-success state independently of its earlier input.
  The proof is in `preparation_history/RESULT.md`; its physical law and
  preparation calibration remain conditional.
- **Local verifier and controller (research packet):** an exact adjacent-gate
  herald certifies the empty-flux vector on the full native data space, with
  coherent failure and clean returned work. All pair gates route inside an
  ordinary finite Z3 box without periodic shortcuts. A finite reversible controller
  reads old records without changing them. One added completion record per
  output distinguishes recorded zero from unused zero; masked copies permit
  clean workspace after the next pointer changes. All resources fit the same
  native site allocation, with separate simultaneous scratch banks. The proof
  and exact compiler diagnostics are in `local_implementation/RESULT.md`.
  This implements finite driven words, including deterministic-edge electric
  readers. Gated permanent registration and microstep sequencing remain supplied.

The code retains an extra encoding-origin degree of freedom and needs a
physical preparation/selection account. The explicit adjacent-gate readout
circuit is for a fixed origin. The new all-origin instrument is an abstract
finite-range construction; an adjacent-gate implementation of its detector is
not supplied. An observed output position can select an origin, so origin
coherence is not generally preserved. Record capacity is finite: one output
per coarse cell. Regional gluing on the fixed coarse graph is preserved;
subdivision requires separate target register allocation.

The unrestricted joint quantum-state/record process does not factor through
its bare outcome records: empty-flux and loop states with the same empty record
give corner probabilities 0 and 1/3. The new prepared-domain construction puts
the preparation and ordered process information in actual record slots and
proves a record-only kernel for that finite model. It supplies tensor quantum
states, Born instruments, a fixed dictionary and a scheduler; these inputs are
not derived from the axioms. The neighborhood radius grows with the chosen
history budget. The local compiler temporarily borrows frozen unrecorded
qubits and restores them at completed boundaries, with unwanted H evolution
suspended. It does not implement the unobserved six-edge mixture with all
work returned pure, or synthesize arbitrary full magnetic exponentials.
Autonomous microscopic control, preparation genesis and calibration, physical
clock, couplings and continuum comparison remain open. No
vacuum or mass-gap closure or evidence that the framework is physically correct
is claimed. Explicit finite dimension comparisons also reject the same-site-count
full-sector identification under ordinary tensor composition.

Validation and evidence:

- Separate coordinate and Haar/fusion derivations agree on the pair and
  boundary results, with different graph-counting routes. A fresh native
  placement derivation independently gives capacity bounds and a different
  invariant code using spacing-nine markers. The supervisor's spacing-five
  construction was frozen before reading that result. For electric readout,
  separate hand derivations give a two-work-qubit vacuum test and a simpler
  five-site parity flag. They agree on the code and differ off it. The
  supervisor hand-checked both and simulated the explicit words independently.
  Same model family and
  shared raw premises remain limitations on independence.
- A separate fresh-context hand derivation checks the vertex-output extension,
  instrument completeness and magnetic intertwiner. The supervisor candidate
  was frozen first; both arguments and the integrated-source check are retained.
  An exact residue probe checks all 15,500 distinct origin pairs and 375,000
  rotation/class images. The control that frees every unused site fails, with
  an explicit overlapping-sector witness. Enumeration checks geometry; the
  arbitrary-volume and operator claims rest on the hand arguments.
- The preparation/history checker independently derives future-effect
  sufficiency, CP history reconstruction and a different finite vertex
  allocation. Exact checks test the supervisor's parser on 1,536 prefix/frame
  cases and all 125 origin residues, and compare density-matrix and pure-path
  propagation on reduced gauge fixtures. Missing-marker and coherent-hidden-
  branch mutations fail. Omitted-order and omitted-magnetic-pulse examples
  produce different future probabilities. These are research checks; full
  formal review and audit of the continuation packets remain pending.
- A separate fresh-context proof derives the full native herald and routing.
  Its source-exposed check validates masked control and identifies three
  repaired details: simultaneous workspace, failed-herald halt and route frame.
  Exact diagnostics compare 544 native basis columns, check 375 returned routes,
  six record-control routes, 236 controller cases and 11,672 compiled predicates.
  Omitting AND cleanup or the history mask fails the checks. These are small
  circuit and pure-proof checks, not a full-torus or physical-clock simulation.
- Complete mathematical source comparisons and scoped correction receipts
  are preserved. These are research checks, not formal landing panels or audits.
- Six production runners have successful content-bound caches. The native
  runner checks all 625 matrix-unit products, all phase residues and proper
  rotations, support geometry and graph ranks using exact arithmetic. No
  enormous native Hilbert-space matrix is constructed.
- Exact Gaussian-rational readout checks cover all five code columns with both
  pointer inputs and the full clean-work basis of the alternate circuit.
  Four separate mutations fail on routing return, square-root phases,
  data-first dephasing and electric uncomputation.
- Mutations test normalization, operator order, energy counting, boundary
  constraints and multiplicity in the earlier packets. Three separate native
  faults reject incorrect reversal parity, nonzero quiescent overlap, and a
  preferred origin. Full successful and failed execution evidence is preserved.
- Focused syntax, vocabulary, local links, source identities, cache evidence
  and diff checks passed. Full pipeline and formal landing/audit remain pending.
  The readout replay after the axiom merge passed 5,009 checks; the initial
  launcher error from an omitted thread setting is preserved separately.

These are conditional bounded theorems supporting GB1-CF, not full GB1-CF
closure. The capacity evidence consists of explicit finite counterexamples;
the committed scope check claims no general negative-packet PASS. Other codes,
emergent sectors and frameworks remain live. No audit authority, premise
registry, or shared instruction files change.

The existing pair and boundary research packs index complete proofs, original
outputs, worker briefs, source identities and recovery paths. The current
checkpoint is `.claude/science/physics-loops/gb1-cf-boundary-gluing-20261107/STATE.yaml`;
its `local_implementation/HANDOFF.md` indexes the latest continuation. The owner-approved
two-word governing locality substitution landed separately in
[PR #10143](https://github.com/jonathonreilly/qubit-lattice-axiom-framework/pull/10143)
at `43a1fcc374711ca50626eca667441d3ca575c7d1`, now merged into this branch.
The two earlier notes' current-axiom prose is synchronized, with their
mathematical arguments unchanged. Two requested Luna scans are preserved in
`native_law/luna_reassessment`: they identify narrow models worth extending,
without a confirmed proof invalidated by the wording change. No additional
axiom change is part of this science PR.
