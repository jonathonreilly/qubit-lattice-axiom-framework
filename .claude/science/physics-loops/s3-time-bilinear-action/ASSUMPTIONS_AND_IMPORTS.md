# Assumptions and imports

## Minimal first-principles surface

The theorem uses only finite-dimensional real linear algebra:

- a slice space `R^n`, `n >= 2`;
- a symmetric-positive matrix `Lambda_R`;
- nonzero vectors `k in R^4` and `u_* in R^n`;
- a differentiable scalar functional `I_R`.

No observed value, fitted selector, physical readout, unit convention,
literature theorem, new axiom, or new primitive is used.

## Import ledger

| Item | Role in claim | Current class | Source surface | Load-bearing? | Needed for target status? | Retirement path | Disposition |
|---|---|---|---|---|---|---|---|
| `Lambda_R` symmetry and positivity | ensures the declared carrier has a nonzero generator on nonzero `u_*` | named generic mathematical premise | theorem statement | yes | yes | proved for the generic witness in the runner; theorem is conditional only on the displayed premise | explicit |
| `I_R` | scalar summand of the displayed action | arbitrary differentiable input | theorem statement | no, beyond differentiability | no | none needed; proof is uniform in `I_R` | discharged generically |
| `K_R` coefficients | provide `k=vec K_R(q)` | arbitrary nonzero vector for headline theorem | theorem statement | only nonzero `k` is needed | yes | no endpoint or physical identification is used | discharged generically |
| `u_*` | initial slice vector | arbitrary nonzero vector | theorem statement | yes | yes | no canonical-seed claim is used | discharged generically |
| Einstein/Regge interpretation | old desired physical bridge | unsupported physical identification | old note/audit target | no, excluded from exact no-go scope | no | requires a new tensor-field action plus physical bridge | remains open outside theorem |
| generator action `S_gen` | falsifier/control showing how the semigroup could be generated | locally constructed mathematical control | source note and runner | no; control only | no | not proposed as framework physics | explicit non-authority control |

## Counterfactual pass

| Assumption | What if it is wrong? | Concrete alternative | Direction it opens | Feasibility | Score |
|---|---|---|---|---|---|
| `a` is the only tensor variable in `I_TB` | the action could instead vary the full carrier field | replace `a in R^4` by `A in R^4 tensor R^n` | permits a generator-bearing action | live, but it changes the action | 3 |
| the tensor penalty is `I_4` stiffness | the stiffness could carry slice dynamics | use `I_4 tensor Lambda_R` on `A` | exactly generates the declared semigroup under gradient flow | live control, not derived physics | 3 |
| `q` is fixed | vary `q` as well | add the algebraic equation `D K_R(q)^T(K_R(q)-a)=0` | adds only an algebraic equation and no slice generator | attempted; does not close | 1 |
| action/carrier identification means variational generation | identification might be declared non-variationally | append the semigroup as an independent law | produces a coupled package by admission, not derivation | live bounded import path | 1 |
| `Lambda_R` is positive definite | allow zero modes | positive semidefinite `Lambda_R` | can make selected carrier directions static but still does not put the generator in `I_TB` | live but does not break structural theorem | 1 |

The two highest-scoring alternatives are combined in the completion control.
They show that the obstruction is repairable only by changing the field/action
surface, not by reinterpreting the existing quadratic penalty.
