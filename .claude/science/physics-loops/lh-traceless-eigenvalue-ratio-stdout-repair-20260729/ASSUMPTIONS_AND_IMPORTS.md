# Assumptions And Imports

| Item | Role in claim | Current class | Source surface | Load-bearing? | Needed for target status? | Retirement path | Disposition |
|---|---|---|---|---|---|---|---|
| `n_color` is a positive integer | theorem domain | zero-input structural hypothesis | source note | yes | yes | none; quantified premise | explicit |
| `(a,b)` is a nonzero real pair | excludes the zero representative | zero-input structural hypothesis | source note | yes | yes | none; quantified premise | explicit |
| `2 n_color a + 2 b = 0` | homogeneous relation | zero-input structural hypothesis | source note | yes | yes | none; theorem antecedent | explicit |
| elementary linear/projective algebra | proof machinery | standard mathematics | source proof and runner | yes | yes | direct proof plus nullspace cross-check | discharged |
| `b = -1` | appendix normalization | admitted normalization | dated convention boundary | no for clean theorem | no | remain outside clean theorem | quarantined support |
| `Q = T_3 + Y/2` | appendix charge readout | admitted convention | dated convention boundary | no for clean theorem | no | remain outside clean theorem | quarantined support |

There are no cited dependencies, observed targets, fitted selectors, literature
values, new axioms, or new framework primitives in the clean theorem. The
primitive-registry check therefore finds no relevant primitive dependency to
classify.

## Counterfactual pass

| Assumption | What if it is wrong? | Concrete alternative | Direction it opens | Feasibility | Score |
|---|---|---|---|---|---|
| pair is nonzero | zero pair is admitted | `(a,b)=(0,0)` | destroys projective and affine ratios | falsified by exact counterexample | 0 |
| count is positive | zero count is admitted | `n_color=0`, `(a,b)=(1,0)` | destroys the two-nonzero conclusion | falsified by exact counterexample | 0 |
| absolute scale is derived | scale remains free | `lambda=2` or `-3` | confirms projective-only scope | live boundary control | 1 |
| charge functional is fixed by the theorem | use another functional | `Q=T_3+Y` | confirms readout is separate | live boundary control | 1 |
| runner cache depends only on runner bytes | the note may drift independently | declare the note in `AUDIT_INPUT_PATHS` | closes stale-input authentication risk | live artifact repair | 3 |

The selected counterfactual is the cache-input binding repair. The scale and
readout alternatives remain controls; they are not routes to enlarge the clean
theorem.
