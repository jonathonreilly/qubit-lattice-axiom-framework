Two adjacent plaquettes share a finite SU(2) link, so their magnetic operators
need not commute. This draft derives the complete zero-external-charge sector
of the specified seven-link, five-state model and constructs a joint update
that preserves gauge invariance and exchange of the two squares at every
real step angle.

The physical sector has dimension four. The exact shared-link witness is
`[B_L,B_R]|L> = -3|R>`. Ordered and left-centered Strang products have explicit
exchange defects; the joint exponential `exp[-i theta(B_L+B_R)]` preserves
exchange exactly, including when composed with the uniform electric layer.
The note gives a 21-qubit full-link code and a two-logical-qubit description
of the closed physical sector, with their initialization and locality limits.

This is a conditional bounded theorem and upstream support for GB1-CF in
#10139. It does not close GB1-CF or derive the supplied model from the lattice
axioms. Homogeneous qubit allocation, boundary sectors and compatible overlap
updates, full spatial covariance, Admissibility/Record dynamics, state selection
and continuum comparison remain open. No axiom, audit authority or registry is
changed. Author status is `proposed_retained` / `candidate-retained-grade`;
formal landing review and independent audit remain pending.

Validation:

- Exact sparse operator action and a separately authored Haar/fusion derivation
  agree on the sector, magnetic/electric matrices, commutator and exchange action.
  The checker was excluded from primary artifacts until its derivation was
  frozen; both contexts used the same model family and supplied premises.
- A focused complete note check verified the mathematics and both encodings.
  Its three convention/provenance/code-scope clarifications were incorporated
  and rechecked. This was not a formal review-loop panel or audit.
- Both runners executed successfully through the repository's content-bound
  cache API. The primary imports the checker and declares its source as a cache
  input; the helper extractor confirms packet reachability. No dependency-policy
  registry change is needed.
- Seven scratch mutations were rejected: link normalization, Gauss endpoint
  assignment, magnetic trace normalization, geometric link inversions, Strang
  half-step, logical magnetic coefficient and electric coefficient. The Haar
  checker additionally rejects two coefficient mutations and a missing-term
  tamper. Full outputs and frozen original sources are preserved in the pack.
- Focused Python syntax, vocabulary, relative-link, cache-identity and diff checks
  passed. Full pipeline and formal landing/audit checks remain pending.

The ordering results are finite existence witnesses, not a no-go against other
schedules. The positive joint-gate example does not require route-exhaustion
claims. See the theorem note and
`.claude/science/physics-loops/gb1-cf-pair-20261107/HANDOFF.md` for exact source
identities, execution receipts, assumptions and the next overlap obligation.
