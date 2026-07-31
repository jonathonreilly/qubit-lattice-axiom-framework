# Approach Registry

| Family | Object/formulation | Mechanism/invariant | Terminal obligation | Strength vs target | Status | Concrete evidence | Reopen condition |
|---|---|---|---|---|---|---|---|
| symbolic canonical reduction | `3x3` matrices | exact permutation conjugation | all six ordered pairs | weaker | candidate-complete | runner section A | counterexample pair |
| symbolic quotient | SymPy incidence matrix | rank, nullspaces, Smith form | generic quotient | weaker | candidate-complete | runner section B | SymPy/manual mismatch |
| plain-integer quotient | integer minors | determinantal divisors | rank five and unit Smith factors | weaker | candidate-complete | runner section C | nonunit divisor |
| global gauge section | integer phase lattice | `I+MG=e_6 w^T` | global rather than tangent quotient | weaker | candidate-complete | runner section C | identity failure or nonprimitive `w` |
| support graph census | 64 subgraphs | cycle rank and saturated incidence | every proper support | weaker | candidate-complete | runner sections C/D | proper cyclic mask or torsion |
| constructive rooted-forest gauge | proper-support forests | reverse leaf peeling and component-root phase propagation | remove every supported phase on all 63 proper masks | weaker | candidate-complete | runner section D and source support-strata proof | uncancelled edge phase or cyclic proper mask |
| proof synthesis | supplied texture, phase lattice, and support strata | compose reduction, quotient, and proper-support certificates | full three-part target conjunction | target-equivalent | candidate-complete | runner sections A-D and source theorem | any component family reopens |
