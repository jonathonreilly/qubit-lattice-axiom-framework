# Assumptions and Imports

The primitive registry was checked before classification. None of the approved
framework primitives is load-bearing for this finite Wilson operator theorem.

| Item | Role in claim | Current class | Source surface | Load-bearing? | Needed for target status? | Retirement path | Disposition |
|---|---|---|---|---|---|---|---|
| finite periodic spatial lattice with finite link/vertex sets | carrier | zero-input structural on the named theorem surface | target note | yes | yes | none; theorem hypothesis | explicit |
| compact gauge group `SU(3)` with normalized Haar measure | operator carrier | zero-input structural on the named theorem surface | target note | yes | yes | none; theorem hypothesis | explicit |
| Wilson one-link weight `w_beta(g)=exp[(beta/3) Re Tr g]`, `beta>=0` | mixed-plaquette kernel | explicit model definition | target note | yes | yes | none; theorem hypothesis | explicit |
| finite-dimensional unitary representation decomposition | sign proof | standard self-contained mathematics | proved in note through tensor-power multiplicities | yes | yes | proof included | no literature import |
| Peter-Weyl/Schur orthogonality | convolution diagonalization | standard self-contained mathematics | proof formulas in note | yes | yes | proof included | no literature import |
| product Haar measure and gauge averaging | gauge projector | zero-input structural on the finite gauge model | target note | yes | yes | proof included | explicit |
| spatial Wilson half weight | transfer sandwich | explicit model definition | target note | yes | yes | exact plaquette census in proof | explicit |
| marked plaquette is spatial | insertion grammar | theorem scope | target note | yes | yes | mixed case treated separately | explicit restriction |
| observed/fitted plaquette values | none | forbidden import | publication package | no | no | excluded | not consumed |
| `beta=6` Perron/thermal data | none | open downstream data | existing plaquette stack | no | no | separate tensor/Perron computation | excluded |
| strict positivity of every character coefficient | none | stronger unneeded statement | prior plan hypothesis | no | no | unnecessary | not claimed |
| transfer-invariant source sector | none | unsupported bridge | source-sector pullback no-go | no | no | separate intertwining theorem | explicitly disclaimed |
| runner constants `NMAX_TENSOR=8`, `RECURRENCE_BOX=5`, `GRAM_SIZE=18`, seed `20260716`, `beta=1.7`, `S_3` couplings `0.61/0.37`, source `-0.29`, and `L_t=2` | deterministic finite diagnostics and falsifiers only | insensitive runner-only support parameters | paired runner | no | no | vary or remove without changing the proof | not physical inputs |

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
