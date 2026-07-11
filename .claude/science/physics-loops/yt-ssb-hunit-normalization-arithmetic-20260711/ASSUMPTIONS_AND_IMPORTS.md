# Assumptions And Imports

## Import ledger

| Item | Role in claim | Current class | Source surface | Load-bearing? | Needed for target status? | Retirement path | Disposition |
|---|---|---|---|---|---|---|---|
| Positive integers `N_iso,N_c` | Define `D=N_iso N_c` | zero-input structural | theorem variables | yes | yes | none; theorem domain | explicit |
| Orthonormal diagonal contractors `E_i` | Fix `Tr(E_i^dagger E_j)=delta_ij` | zero-input structural | local definition | yes | yes | none; theorem hypothesis | explicit |
| Equal-weight direction `S_D=sum_i E_i` | Object to normalize | zero-input structural | local definition | yes | yes | none; theorem hypothesis | explicit |
| Hilbert-Schmidt inner product | Computes `||S_D||^2` | standard finite-dimensional machinery | local definition | yes | yes | displayed contraction | derived in source |
| Positive representative `c>0` | Fixes the sign/phase of the one-dimensional ray | zero-input structural | local representative definition | yes for the sign, no for `|c|` | yes for signed coefficient | none; the invariant magnitude is derived before the representative is selected | explicit and non-physical |
| Stated instance `(N_iso,N_c)=(2,3)` | Specializes `D` to `6` | zero-input structural | theorem parameter choice | yes only for the numeral `6` | yes only for `(T3)` | general theorem already covers all positive dimensions | explicit |

No measured value, fitted selector, literature value, physical readout map, or
unapproved primitive is used. The primitive registry was checked; none of its
registered primitives is relevant to this self-contained finite-dimensional
claim.

## Counterfactual pass

| Assumption | What if it's wrong? | Concrete alternative | Direction it opens | Feasibility | Score |
|---|---|---|---|---|---|
| The contractor basis is orthonormal | Gram matrix is nonidentity | positive-definite Gram matrix `G` | coefficient becomes `1/sqrt(1^T G 1)` | live bounded generalization, not needed here | 1 |
| The diagonal direction is equal-weight | coefficients are nonuniform | supplied coefficient vector `w` | unit coefficient becomes `1/sqrt(w^dagger w)` and component equality generally fails | live falsifier; runner exercises it | 3 |
| The positive representative is selected | only norm is fixed | allow phase `e^{i theta}` | theorem fixes magnitude only | live; already exposed in source and runner | 2 |
| The stated dimension is six | choose another positive dimension | `(3,4)` or `(1,1)` | tests the general formula away from the target instance | live; runner exercises both | 2 |

The selected route retains the exact stated hypotheses and adds the two
highest-value falsifiers: nonuniform weights and sign reversal.
