# Route Portfolio

Scores are 0--3. `Value` is claim-state movement; `Hard` is hard-residual
pressure; `Risk` is overclaim/import risk, where larger is worse.

| Route | Attack | Value | Hard | Artifactability | Risk | Pre-execution trace |
|---|---|---:|---:|---:|---:|---|
| Direct carrier derivation | Derive a canonical map from `A_min` to `D_act,D_pass` and prove both equal `I_3` | 3 | 3 | 1 | 3 | direct blocker closure if successful |
| Equivariant commutant classification | Construct the `hw=1` symmetry representation and solve its joint commutant exactly | 3 | 3 | 3 | 1 | direct blocker closure or exact obstruction |
| Scalar-family propagation | Carry arbitrary `(alpha I_3,beta I_3)` through both resolvents, source columns, reconstruction, frame, and rejection | 3 | 2 | 3 | 1 | closes dependence of the boundary result on `alpha=beta=1` |
| Explicit model separation | Expand the same axiom/hw1 structure by two different equivariant carrier assignments | 3 | 3 | 3 | 1 | proves non-entailment of the identity normalization |
| Retained-atlas reuse | Search for a retained carrier/source-action bridge already present elsewhere | 3 | 2 | 2 | 1 | retires the import if an exact matching authority exists |
| Full unrestricted operator family | Classify every block that could appear after symmetry breaking | 1 | 3 | 2 | 3 | frontier-only; too broad for this block |

## Stuck fan-out frames

1. Symmetry/commutant: ask what the supplied translations and proper rotation
   force before selecting any values.
2. Model theory: ask whether the axiom language even contains the carrier
   symbol or a source/action map.
3. Atlas reuse: search the retained dependency graph for a matching carrier
   theorem rather than inferring one from a similarly named note.
4. Resolvent invariance: ask whether the rejection conclusion is independent
   of the missing normalization.
5. Counterexample/falsifier: introduce one non-scalar block and verify exactly
   which supplied symmetry it violates and which new support it can create.

## Selected route

Combine the equivariant commutant classification, model separation, and
scalar-family propagation. This can remove `I_3` as a load-bearing assumption
while giving a falsifiable boundary: a nontrivial PMNS-support block must fail
at least one of the explicit symmetry/zero-input hypotheses or import a
carrier law not present in `A_min`.
