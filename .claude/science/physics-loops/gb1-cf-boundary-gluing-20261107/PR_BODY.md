Finite SU(2) plaquettes share noncommuting link operators, and treating every
patch boundary as a singlet discards states needed by its neighbors. This PR
derives the two-plaquette operators and an invariant joint gate, then extends
the same five-state link model to exact cutting and boundary-flux gluing.

For two closed plaquettes, the physical sector has four states and
`[B_L,B_R]|L> = -3|R>`. The joint exponential preserves gauge invariance and
square exchange at every angle; the specified ordered and Strang products
have explicit exchange defects. The note gives finite qubit encodings with
their initialization and locality limits.

The boundary extension constructs an isometric link cut whose full image is
the new-vertex singlet sector. It intertwines the transporter and its adjoint,
is associative under repeated cuts, and identifies the electric weights needed
to count each original link once. Regions glue by retaining boundary irreps
and multiplicities until each complete vertex incidence is present. On the
four-plaquette square, regional dimensions 325 and 13 reconstruct all 18
singlet states in three groupings. Premature zero-flux boundaries give only
4; deleting intertwiner multiplicity or an intermediate spin-one channel gives
16. With the outer boundary left open, the exact dimension is 22,265,625,
computed without a dense matrix.

These are conditional bounded theorems and upstream support for GB1-CF in
#10139. The finite gauge-model gluing obligation is established under the
specified model; full GB1-CF is still open. Native homogeneous qubit allocation,
spatially covariant nearest-neighbor updates, Admissibility/Record dynamics,
state selection and continuum identification are not supplied. No axiom or
authority record changes. Both author proposals await formal landing review
and audit; ready-for-review status is not scientific acceptance.

Validation and evidence:

- Separately authored exact coordinate/sparse-action and Haar/coefficient
  derivations agree. For the graph, occupancy/fusion, independent signed
  Laurent-character elimination and a direct cycle-space count agree.
  Contexts share a model family and raw premises; no different-provider
  independence is claimed.
- Focused complete-note checks and correction dispositions are preserved in
  the research packs. These are research checks, not formal landing panels.
- All four production runners have successful content-bound caches. Each
  primary statically imports its corresponding checker and declares that
  source as a cache input; actual helper extraction confirms reachability.
- The pair packet preserves seven scratch mutations and its checker faults.
  The gluing packet rejects incorrect cut normalization, reversed chain order,
  unweighted electric energy, premature boundary projection, discarded
  multiplicity and a missing intermediate-spin channel. Separate graph fault
  invocations fail with exit 1. Initial resource-limit failure evidence is
  preserved alongside the successful bounded final runs.
- Focused syntax, vocabulary, relative-link, cache-identity, source-recovery
  and diff checks passed. Full pipeline and formal landing/audit checks remain
  pending. There are no generated authority or dependency-policy edits.

The displayed failures are finite witnesses for particular shortcuts, not
no-go claims against other encodings or laws. Proofs, full outputs, source
identities, worker briefs and recovery paths are indexed by the two research
handoffs under `.claude/science/physics-loops/gb1-cf-pair-20261107/` and
`.claude/science/physics-loops/gb1-cf-boundary-gluing-20261107/`.
