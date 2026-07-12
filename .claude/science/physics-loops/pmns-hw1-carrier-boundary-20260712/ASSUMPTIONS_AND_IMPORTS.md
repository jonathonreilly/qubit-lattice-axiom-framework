# Assumptions And Imports

## Minimal allowed premise set

`A_min` is exactly the current Lattice, Qubit, Admissibility, and Record set in
[`MINIMAL_AXIOMS_2026-06-29.md`](../../../../docs/MINIMAL_AXIOMS_2026-06-29.md).
No approved primitive beyond `minimal_axioms` is relevant to this dimensionless
carrier question.

Forbidden proof inputs: measured mixing angles or phases, fitted PMNS
coordinates, a selected mass hierarchy, literature values, new axioms, new
framework primitives, an assumed source/action bridge, and the desired
`I_3` result itself.

## Import ledger

| Item | Role in claim | Current class | Source surface | Load-bearing? | Needed for target status? | Retirement path | Disposition |
|---|---|---|---|---|---|---|---|
| `Z^3` translations and proper cubic rotations | Supplies the spatial symmetry action | zero-input structural | `MINIMAL_AXIOMS_2026-06-29.md` | yes | yes | already supplied | allowed |
| One-site `M_2(C)` / `Cl(3,0)` presentation | Instantiates the local qubit algebra | zero-input structural | `MINIMAL_AXIOMS_2026-06-29.md` | yes for the framework packet, not for the 3-dimensional commutant algebra | yes | already supplied | allowed |
| `hw=1` joint-character triplet | Three restricted translation characters used by the source frame | retained support candidate reproduced locally | finite character calculation in the target runner; upstream context in `STAGGERED_DIRAC_REALIZATION_GATE_NOTE_2026-05-03.md` | yes | yes | reproduce in the runner, so no hidden import remains | in progress |
| `C_3[111]` action on the triplet | Connects the three characters by a supplied proper cubic rotation | framework-derived finite restriction | constructed locally from the Lattice rotation | yes | yes | construct and verify covariance in the runner | in progress |
| Map from `A_min` data to active/passive operators in `End(H_hw1)` | Gives physical meaning to `D_act,D_pass` | unsupported import | absent from `A_min`; the axiom memo explicitly excludes source/action and transfer dynamics | yes for the old identity claim | yes if `D=I_3` is asserted as derived | theorem route or exact underdetermination result | open |
| Scalar normalizations `alpha=beta=1` | Selects `(I_3,I_3)` from any scalar equivariant family | unsupported import | inserted by the current free-pack construction | yes for exact identity, no for a scalar-family boundary | yes only for the old claim | normalization theorem or remove from load-bearing conclusion | open |
| Active/passive resolvent formulas | Propagates a supplied block to response columns | support-only mathematical convention | defined in the target runner / PMNS helper stack | yes for the response corollary | no for the carrier no-go; yes for the family response theorem | state as explicit theorem definitions and check poles | disclose |
| One-sided minimal-PMNS support classifier | Rejects scalar/monomial pairs | retained-support candidate reproduced locally | local support-mask definition in the target runner | yes for local rejection | yes | inline and test exhaustively on the scalar family | in progress |
| Lower-level closure stack | Prior cross-check of rejection | support-only and currently non-retained | `PMNS_LOWER_LEVEL_END_TO_END_CLOSURE_NOTE.md` | no | no | remove from load-bearing packet | exclude |

## Counterfactual pass

| Assumption | What if it's wrong? | Concrete alternative | Direction it opens | Feasibility | Score |
|---|---|---|---|---|---|
| The zero-input carrier is exactly `I_3` | Its normalization is not fixed | `D=alpha I_3` with arbitrary scalar `alpha` | A family theorem may close the source/transfer boundary without selecting `alpha=1` | live | 3 |
| The carrier must commute with translations and `C_3` | A derived law could break a supplied lattice symmetry | General `3 x 3` Hermitian block | Opens nontrivial PMNS support, but requires an extra selector/carrier law absent from `A_min` | live only as an explicit import; not an axiom-only route | 2 |
| Active and passive sectors share a normalization | They may carry independent scalars | `(alpha I_3,beta I_3)` | Tests whether rejection is family-wide rather than tied to equal blocks | live | 3 |
| The PMNS closure helper is necessary | The local support criterion may be sufficient | Inline the exact one-sided minimal classifier | Removes a non-retained helper dependency | live | 3 |
| Pauli matrices determine the triplet carrier operator | Local algebra may provide no canonical map into `End(H_hw1)` | Treat local `M_2(C)` and triplet `M_3(C)` as distinct supplied/derived objects | Exposes the missing functor/source-action bridge | live | 3 |

The selected counterfactuals are the scalar-family classification, independent
active/passive scalar propagation, and local rejection without the imported
closure helper.
