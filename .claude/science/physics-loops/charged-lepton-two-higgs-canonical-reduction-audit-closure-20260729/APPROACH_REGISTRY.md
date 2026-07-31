# Approach Registry

| Family | Object/formulation | Mechanism/invariant | Terminal obligation | Strength vs target | Status | Concrete evidence | Reopen condition |
|---|---|---|---|---|---|---|---|
| symbolic canonical reduction | `3x3` matrices | exact permutation conjugation | all six ordered pairs | target-equivalent | validated | runner section A | counterexample pair |
| symbolic quotient | SymPy incidence matrix | rank, nullspaces, Smith form | generic quotient | target-equivalent | validated | runner section B | SymPy/manual mismatch |
| plain-integer quotient | integer minors | determinantal divisors | rank five and unit Smith factors | target-equivalent | validated | runner section C | nonunit divisor |
| global gauge section | integer phase lattice | `I+MG=e_6 w^T` | global rather than tangent quotient | target-equivalent | validated | runner section C | identity failure or nonprimitive `w` |
| support graph census | 64 subgraphs | cycle rank and saturated incidence | every proper support | target-equivalent | validated | runner sections C/D | proper cyclic mask or torsion |
