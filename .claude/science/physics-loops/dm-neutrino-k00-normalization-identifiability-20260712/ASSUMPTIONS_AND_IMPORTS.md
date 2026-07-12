# Assumptions And Imports

## Minimal premise reset

`A_min` is Lattice + Qubit + Admissibility + Record, as registered by
[`MINIMAL_AXIOMS_2026-06-29.md`](../../../../docs/MINIMAL_AXIOMS_2026-06-29.md).
The approved primitive set is exactly the scale-reference, kinetic-isotropy,
and realized-state primitives. None supplies a source/action map, physical
observable identification, selector magnitude, or normalization rule.

Forbidden proof inputs: observed neutrino values, fitted selectors, literature
normalizations, `K00 = 2` as a target, hard-coded `tau_E = tau_T = 1/2`, or a
new axiom/primitive.

## Import ledger

| Item | Role in claim | Current class | Source surface | Load-bearing? | Needed for positive target? | Retirement path | Disposition |
|---|---|---|---|---|---|---|---|
| `F00 = J3/3` | target bright-ray projector | zero-input finite algebra within packet | target note/runner | yes | yes | already constructed exactly | closed |
| `P+ = J2/2` | source swap-even projector | zero-input finite algebra within packet | target note/runner | yes | yes | already constructed exactly | closed |
| scalar-baseline log-determinant response | compare coefficient deformations | support-only finite algebra | target note/runner | yes | yes | derive symbolic determinant identities | closed as algebra |
| source embedding scale `c` in `S = c tau_+ P+` | turns coordinates into physical source operator | unsupported import in positive claim | no supplied typed map | yes | yes | source-action theorem or explicit bounded convention | open |
| source magnitude `tau_+` | fixes endpoint after coefficient law | unsupported import in positive claim | swap symmetry fixes only its ray | yes | yes | source-selection theorem | open |
| equality as a physical cross-sector response | identifies source and target coefficients | unsupported import in positive claim | no supplied typed observable map | yes | yes | source-to-heavy response theorem | open; grouped with typed embedding wall |
| observed or fitted values | none | forbidden | none | no | no | not applicable | absent |

## Counterfactual pass

| Assumption | What if it is wrong? | Concrete alternative | Direction it opens | Feasibility | Score |
|---|---|---|---|---|---|
| The physical source is `tau_+ J2` | the physical source is the sharp projector `tau_+ P+` | set `c = 1` instead of `c = 2` | produces an exact response-matched `K00 = tau_+` countermodel | live | 3 |
| A projector column defines physical source coordinates | the unit bright vector defines them | `(1/sqrt(2),1/sqrt(2))` rather than `(1/2,1/2)` | exposes coordinate normalization as a separate rule | live | 3 |
| Isospectrality identifies physical coefficients | it identifies only normalized rays | retain a free intertwiner scale `c` | yields the general law `K00 = c tau_+` | live | 3 |
| Swap symmetry fixes the source value | it fixes only the invariant line | `tau = a(1,1)` | exposes the independent source-magnitude parameter | live | 3 |
| Record additivity supplies the physical map | Record is only readout additivity | require a typed source/action and observable bridge | prevents axiom laundering | forced by current axiom memo | 0 |

The highest-scoring counterfactuals are combined in the selected
two-parameter countermodel route.
