# Premises and current-axiom comparison

The adopted premise registry at main f5af11cd0102cfd0b51aef0911f600130bf5beb1
contains Lattice, Qubit, Admissibility, Record, and the scale-reference,
kinetic-isotropy and realized-state primitives. They remain unchanged.

| Item | Role in this probe | Physical status |
|---|---|---|
| Seven oriented links on two adjacent squares | Finite mathematical domain | Not a derived physical allocation of qubits |
| Five-state SU(2) link | Explicit matrix definition, re-derived here | Supplied model; no physical group selection |
| Ordinary tensor product over links | Mathematical realization | Native composition/locality identification is separate |
| Gauss singlet at every vertex, no external links or charges | Boundary/sector specification | Not a selected physical state or vacuum |
| Magnetic trace plus its adjoint | Chosen gauge-invariant interaction | No axiom derivation of its coefficient or choice |
| Equal treatment of the two squares | Exact symmetry target for this patch | Does not establish the full cubic lattice update |
| Electric Casimir and two update angles | Explicit finite-step model | No physical clock, coupling value, or unique Hamiltonian logarithm |
| Qubit code | Exact algebraic embedding on an initialized code subspace | Does not select a homogeneous code tiling or record dynamics |
| Haar integral / elementary SU(2) fusion | Independently checked mathematical tools | No continuum or vacuum theorem imported |

## Counterfactuals and limits

- External charges or dangling links change the physical sector; its dimension
  must be recomputed rather than transferred from this boundary problem.
- A different finite representation may change all coefficients and the sector.
- Reversing the orientation convention is allowed if every endpoint action,
  adjoint and loop product is transformed consistently.
- A nonzero ordered-update symmetry defect would be a witness for that specified
  product, not a result excluding joint gates, other schedules or other laws.
- An exact finite-patch qubit encoding does not decide whether the same code
  admits consistent, symmetry-preserving embeddings on overlapping patches.
- The current axioms distinguish permanent record content from the quantum
  possibility algebra. This computation supplies neither the forming-record
  probability law nor a proof that an implemented update preserves records.
- The registered kinetic-isotropy primitive supplies its stated kinetic form;
  it does not by itself establish covariance of this interacting update.
- The realized-state primitive permits evaluation at supplied state data; it
  does not turn the empty-flux reference into the physical vacuum.

## Branch context

PR #10139 at fb9508e8390bf66da8f29ddb44611d2a531768cb carries the proposed
PS-1 update, PS-5 enlarged site content, PS-6 gauge registers, and PS-1c cell
covariance. This probe does not adopt them. Its finite definitions are rebuilt
in the self-contained note and runner; unmerged branch proofs are
context rather than runtime dependencies.
