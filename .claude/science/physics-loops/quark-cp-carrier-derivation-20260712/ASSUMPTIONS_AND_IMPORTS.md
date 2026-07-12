# Assumptions And Imports

## Minimal premise reset

Allowed foundation: Lattice, Qubit, Admissibility, Record, plus the registered
scale-reference, kinetic-isotropy, and realized-state primitives. None supplies
a quark generation basis, mass matrix, texture selector, mixing observable,
mass ratio, phase, carrier normalization, or numerical target.

## Import ledger

| Item | Role in claim | Current class | Source surface | Load-bearing? | Needed for target status? | Retirement path | Disposition |
|---|---|---|---|---|---|---|---|
| Hermitian three-by-three Schur-NNI carrier ansatz | Defines the route being tested | support-only | target note and runner | yes, for the narrow no-go domain | yes | test its exact invariants | explicit route boundary |
| `xi_u`, `xi_d` fitted values | Historical numerical witness | fitted input | target note | no for exact no-go; yes for old positive fit | no | remove from proof role | witness only |
| Quark mass and CKM/J comparators | Historical optimizer targets | observational comparator | parent runner import | no for exact no-go; yes for old fit | no | derive in a separate lane | witness only |
| Dirac masses are read as singular values of the mass matrices | Standard physical identification used to interpret the old runner's mass claim | explicit observable definition | biunitary/singular-value mass convention already used by the runner's `M M^dagger` diagonalization | yes for the physical-claim diagnosis | yes | disclose separately from algebra | explicit standard identification, not derived here |
| Frobenius trace and exact eigenvalue-bracket identities | Tests whether the shipped matrices realize that mass readout | local exact derivation | obstruction runner | yes | yes | symbolic identity and rational sign certificate | derived in this block |
| Common weak-basis covariance | Identifies coordinate versus observable content | standard exact linear algebra | simultaneous unitary conjugation | yes | yes | exact orbit theorem | derived in this block |
| Weak-basis/texture selector | Would be needed to make `xi_s` a physical observable/readout rather than a conventional coordinate | unsupported import | absent from current target surface | yes for positive closure | yes for positive closure | new retained theorem | exposed blocker |
| Hermiticity | Makes each determinant real | explicit ansatz condition | target runner | yes for determinant-phase boundary | yes | exact determinant formula | derived consequence |

## Counterfactual pass

| Assumption | What if it is wrong? | Concrete alternative | Direction it opens | Feasibility | Score |
|---|---|---|---|---|---|
| Diagonal entries are physical masses | Read masses from singular values | optimize the singular spectrum itself | repairs the observable mismatch but remains a fit | live, bounded | 3 |
| `xi_s` is a physical scalar | Treat it as a weak-basis coordinate | derive a canonical joint-basis selector or use invariants | separates coordinate convention from physics | live | 3 |
| Fixed Schur-NNI tree coefficients select the physical basis | Derive rather than stipulate the texture | native dynamics/source theorem | could make coordinates meaningful | live but open | 3 |
| Hermiticity enforces strong-CP closure | Only determinant reality is automatic | derive determinant sign and the QCD theta/readout bridge separately | prevents phase-zero overreading | live | 2 |
| Imported comparators may define the coefficients | Forbid observations as proof inputs | derive masses and CKM invariants from the framework | only true positive-retention route | live but major open lane | 2 |
| A different non-Hermitian completion could evade the orbit argument | Enlarge the route family | biunitary weak-basis treatment | outside this narrow no-go; does not rescue this runner | live, out of scope | 1 |

Highest-scoring live counterfactuals are the singular-spectrum repair, a
derived joint-basis selector, and a native texture/source theorem. The current
block exactly tests the shipped singular-spectrum defect and weak-basis
non-invariance; selector construction and the native source theorem remain
open. It does not add a new axiom or primitive.
