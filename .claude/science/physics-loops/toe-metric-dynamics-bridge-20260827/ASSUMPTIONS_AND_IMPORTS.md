# Assumptions and imports

| Item | Role in claim | Current class | Source surface | Load-bearing? | Needed for target status? | Retirement path | Disposition |
|---|---|---|---|---|---|---|---|
| finite nearest-neighbor graph | edge domain | zero-input structural | Lattice axiom | yes | yes | already supplied at structural level | allowed |
| D3(g,V) cell carrier | local inner product | retained support candidate on stacked branch | parent weighted-kernel note | yes | yes | independent review/audit of stack | declared conditional |
| local Gamma matrices | local direction forms | retained support candidate on stacked branch | parent weighted-kernel note | yes | yes | independent review/audit of stack | declared conditional |
| link comparison U_sr | compare neighboring exterior fibres | derived from A once a tangent map is supplied | cycle 2 exterior-lift theorem | yes | yes for a chosen variable-cell operator | exact normalization and Clifford compatibility proved here | partially retired |
| coframe E_s | square root of inverse metric | mathematical choice with local O(3) redundancy | cycle 2 factorization | yes for coordinates; no as physical observable | yes | quotient by E_s -> Q_s E_s | explicit gauge choice |
| orthogonal edge factor R_sr | independent compatible connection data | support-only supplied input | cycle 2 factorization | yes for a nontrivial chosen connection | yes | derive a selection/action or retain as open | exposed, not selected |
| physical time/Lorentzian map | physical interpretation | unsupported import if used | none | no in current block | yes for TOE completion | OS/Wick theorem | forbidden in current block |
| gravity action/backreaction | dynamics | unsupported import if used | none | no in current block | yes for TOE completion | later variational/action route | forbidden in current block |

## Counterfactual pass

| Assumption | What if it is wrong? | Concrete alternative | Direction it opens | Feasibility | Score |
|---|---|---|---|---|---|
| link comparison must be metric-compatible immediately | weighted skew may need less structure | arbitrary invertible cross-fibre comparison | separates adjoint existence from metric compatibility | live | 3 |
| endpoint transport is determined by endpoint metrics | connection may carry independent orthogonal data | factor transport into endpoint coframes and an orthogonal edge matrix | exposes curvature degrees | live | 3 |
| nontrivial curvature follows from varying endpoint metrics | endpoint factorization may be pure gauge | compute plaquette product explicitly | prevents false gravity closure | live | 3 |
| one coordinate is already physical time | labels may remain Euclidean | postpone OS/Wick identification | protects the claim boundary | live | 2 |

Selected routes: arbitrary cross-form classification; coframe-plus-orthogonal
connection factorization; explicit plaquette holonomy decomposition.

Cycle 2 retirement result: an arbitrary invertible fibre comparison is no
longer needed once tangent/Clifford compatibility is imposed. It is replaced
by the normalized exterior lift of `A=E_s^-1 R_sr E_r`. The orthogonal factor
`R_sr` remains an honest supplied input rather than being hidden in `U_sr`.
