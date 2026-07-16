# Assumptions and Imports

The primitive registry was checked before classification. None of the approved
framework primitives is load-bearing for this finite Wilson operator theorem.

| Item | Role in claim | Current class | Source surface | Load-bearing? | Needed for target status? | Retirement path | Disposition |
|---|---|---|---|---|---|---|---|
| finite periodic cubic spatial lattice with `L_s>=2` and finite `L_t>=1` | carrier | explicit normalization/boundary condition | target note | yes | yes | none; theorem hypothesis | explicit |
| compact gauge group `SU(3)` with normalized Haar measure | operator carrier and measure | explicit normalization/boundary condition | target note | yes | yes | none; theorem hypothesis | explicit |
| Wilson one-link weight `w_beta(g)=exp[(beta/3) Re Tr g]`, `beta>=0` | mixed-plaquette kernel | zero-input structural on the explicitly named Wilson-model surface | target note | yes | yes | none; theorem hypothesis | explicit |
| field-independent `exp(-beta)` per plaquette in the canonical Wilson action | partition-function normalization | explicit normalization/boundary condition | target note | yes for unnormalized `Z`; no for positivity or normalized source states | yes | exact scalar relation `T_beta^W=exp(-2 beta |E|)T_beta` | explicit |
| finite-dimensional unitary representation decomposition | sign proof | zero-input structural | proved in note through tensor-power multiplicities | yes | yes | proof included | no literature import |
| Peter-Weyl/Schur orthogonality | convolution diagonalization | zero-input structural | proof formulas in note | yes | yes | proof included | no literature import |
| product Haar measure and gauge averaging | gauge projector | zero-input structural | target note | yes | yes | proof included | explicit |
| spatial Wilson half weight | transfer sandwich | explicit normalization/boundary condition | target note | yes | yes | exact plaquette census in proof | explicit |
| marked plaquette is spatial | insertion grammar | explicit normalization/boundary condition | target note | yes | yes | mixed case treated separately | explicit restriction |
| observed/fitted plaquette values | none | observational comparator | publication package | no | no | excluded | not consumed |
| `beta=6` Perron/thermal data | none | one computed lattice input | existing plaquette stack | no | no | separate tensor/Perron computation | excluded |
| strict positivity of every character coefficient | none | support-only stronger statement | prior plan hypothesis | no | no | unnecessary | not claimed |
| transfer-invariant source sector | none | unjustified import | source-sector pullback no-go | no | no | separate intertwining theorem | explicitly disclaimed |
| exhaustive finite `S_3` replacement-group model | transfer-factorization diagnostic | support-only | paired runner | no | no | remove without changing the analytic `SU(3)` proof | not theorem evidence |
| runner constants `NMAX_TENSOR=8`, `RECURRENCE_BOX=5`, `GRAM_SIZE=18`, seed `20260716`, `beta=1.7`, `S_3` couplings `0.61/0.37`, source `-0.29`, `L_t=2`, and `TOL=2e-11` | deterministic finite diagnostics and falsifiers only | insensitive nuisance | paired runner | no | no | vary or remove without changing the proof | not physical inputs |
| four fixed torus samples, tested recurrence range `0<=p,q<=3`, negative-beta sign control, and the matrix `[[1,2],[2,1]]` | deterministic recurrence and hostile controls | insensitive nuisance | paired runner | no | no | replace by other discriminating samples/controls | not physical inputs |

## Counterfactual pass

| Assumption | What if it is wrong? | Concrete alternative | Direction it opens | Feasibility | Score |
|---|---|---|---|---|---:|
| the marked insertion is spatial | the mark crosses the time step | differentiate/modify the mixed kernel instead of multiplying one slice | honest mixed-plaquette insertion theorem | live, separate block | 2 |
| positivity is proved after gauge projection | the unprojected convolution is handled first | prove one-link positive type, tensor it, then use commutation with `P_G` | direct Gram factorization | live and selected | 3 |
| the source sector must be transfer invariant | only the multiplication algebra is needed | pull back the positive trace state through the plaquette multiplication representation | avoids the false eigenvalue-preservation bridge | live and selected | 3 |
| the lattice has equal spatial and temporal extents | use general `L_s^3 x L_t` | keep only the spatial insertion theorem; do not use time-space axis exchange | broader finite-volume theorem | live and selected | 3 |
| character coefficients must be strictly positive | nonnegativity is sufficient | allow zero coefficients and prove only positive semidefiniteness | removes an unnecessary stronger burden | forced narrowing | 3 |
| literature reflection positivity is required | the finite kernel can be factored directly | representation-ring coefficient proof plus gauge projector | self-contained repair | live and selected | 3 |

The highest-value counterfactuals are the unprojected-convolution route, the
source-algebra pullback route, and the general `L_s^3 x L_t` spatial-insertion
scope.
