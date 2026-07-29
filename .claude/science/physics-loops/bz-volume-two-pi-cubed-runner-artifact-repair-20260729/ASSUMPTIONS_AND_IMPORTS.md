# Assumptions And Imports

The primitive-registry check found no relevant approved primitive beyond the
canonical `minimal_axioms` node supplying the Lattice premise.

| Item | Role in claim | Current class | Source surface | Load-bearing? | Needed for target status? | Retirement path | Disposition |
|---|---|---|---|---:|---:|---|---|
| Unit-spaced `Z^3` substrate | fixes the discrete group | zero-input structural | `minimal_axioms` | yes | yes | none | supplied Lattice premise |
| `e^{ik·x}` pairing | fixes the `2π` coordinate period | admitted normalization | explicit theorem hypothesis | yes | yes | none within this coordinate-scoped theorem | retain explicitly |
| Pontryagin duality and Haar uniqueness | identifies `T^3` and probability Haar measure | literature theorem | standard abelian harmonic analysis | yes | yes | independent mathematical check | disclosed textbook machinery |
| Product Lebesgue volume | gives `(2π)^3` | retained support | standard measure theory and exact arithmetic | yes | yes | exact symbolic check | closed |
| Continuum Fourier denominator | numerical comparison only | admitted normalization | theorem step T4/B7 | no | no | already downstream-only | preserve scope guard |

## Counterfactual pass

| Assumption | What if it is wrong? | Concrete alternative | Direction it opens | Feasibility | Score |
|---|---|---|---|---|---:|
| pairing is `e^{ik·x}` | the coordinate period is not `2π` | use an `e^{2πik·x}` convention | changes the fundamental-domain coordinate and removes the stated formula from scope | live only as a different convention, not this target | 0 |
| spacing is one | lattice spacing is `a` | dual domain `[-π/a,π/a]^3` | produces the scaled coordinate formula | live only as a generalized theorem, not this target | 0 |
| Haar measure is probability-normalized | use unnormalized Haar measure | Lebesgue volume measure | removes the probability-density denominator | incompatible with the exact target | 0 |

No counterfactual changes the artifact repair: the current audit scope already
fixes the relevant convention and normalization.
