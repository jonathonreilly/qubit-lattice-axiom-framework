# Assumptions and Imports

## First-principles reset

The permitted framework baseline is Lattice, Qubit, Admissibility, and Record.
The approved primitive registry contains only `minimal_axioms`,
`scale_reference_primitive`, `kinetic_isotropy_primitive`, and
`realized_state_primitive`. None supplies gauge dynamics, channel weighting, a
physical observable bridge, or a readout selector.

The bounded theorem itself needs none of the dimensionful or state primitives.
It is finite-dimensional linear algebra on a supplied `SU(N)` color carrier
and the explicit transformation law of a separated open bilocal.

Forbidden as proof inputs: the observed `8/9` runner output, a fitted
`kappa_EW`, PDG values, literature numerical values, a planar-population
slogan, or an unregistered axiom/primitive.

## Import ledger

| Item | Role in claim | Current class | Source surface | Load-bearing? | Needed for target status? | Retirement path | Disposition |
|---|---|---|---|---|---|---|---|
| `SU(N)` fundamental color carrier | Defines the finite representation under study | explicit bounded mathematical setup | Stated inline | yes | yes | Already explicit in theorem scope | accepted bounded setup |
| Separated open bilocal transformation `M -> Omega_x M Omega_y^dagger` | Supplies the endpoint product-group action | zero-input structural within the stated lattice-gauge setup | Derived inline from covariance of the finite lattice Dirac matrix and its inverse; matched to the legacy runner's `x != source` loop | yes | yes | Direct covariance derivation | derived in scope |
| Gauge-invariant equilibrium measure | Maps the conditional endpoint-orbit identity to the ideal ensemble expectation | explicit bounded ensemble condition | Stated in the equilibrium-ensemble corollary | yes for the runner-application corollary | yes for that corollary | Gauge invariance of link Haar measure and action | explicit condition; finite Markov estimator remains approximate |
| Haar second moment | Evaluates the endpoint orbit | explicitly named standard mathematical machinery | Inline index reduction; deterministic Weyl check | yes | yes | Inline reduction plus independent runner route | explicit method; no external numerical input |
| Schur classification | Distinguishes product-group and diagonal-conjugation commutants | explicitly named standard mathematical machinery | Inline representation decomposition; runner projectors and countermodels | yes | yes | Explicit reduction plus matrix checks | explicit method; no external numerical input |
| `8/9` legacy output | Historical target under explanation | observational comparator only | Legacy runner/cache | no | no | Not consumed by proof | comparator only |
| Physical EW current/readout | Needed only for a physical matching rule beyond this theorem | unsupported/open bridge | Not supplied by approved primitives | no for bounded theorem; yes for old positive claim | no for this target | Gauge-invariant current plus continuum matching theorem | remains open |
| `kappa_EW` | Continuum readout weight beyond the orbit theorem | unsupported/open selector | Current R_conn/EW no-go family | no for bounded theorem; yes for absolute EW normalization | no for this target | Exact matching computation or explicit bounded convention | remains open |

## Counterfactual pass

| Assumption | What if it's wrong? | Concrete alternative | Direction it opens | Feasibility | Score |
|---|---|---|---|---|---|
| Endpoints are distinct and independently gauge-rotatable | The object is coincident or its endpoint frames are already identified | Diagonal conjugation at one site | Opens the two-weight `P_1/P_adj` kernel and removes the forced `8/9` orbit fraction | live | 3 |
| The measured object is an open bilocal | A Wilson line closes it into a gauge-covariant matrix | `H=G_xy W_yx` | Makes the split gauge invariant but dynamical; supplies explicit countermodels `H proportional I` and traceless `H` | live | 3 |
| `connected` means the frame-dependent trace/traceless coordinate of the open bilocal | It means quark-line connected or cumulant connected | Full same-line current loop or cumulant subtraction | Exposes the semantic type error and the need for a current theorem | live | 3 |
| Large-N remainder has an irrelevant coefficient | The coefficient controls the finite `N_c=3` value | `q_N=1+c/N^2` family | Shows `O(1/N^4)` does not select exact `8/9` | live | 3 |
| A new primitive could select the readout | Primitive registry remains fixed | Explicit bounded convention or derived current matching | Keeps selector work in the allowed import/bounded/retirement shape | infeasible as a primitive route; live as bounded convention | 1 |

The selected route combines the first four live counterfactuals. It changes the
claim state by exactly deriving the runner statistic's ideal equilibrium
expectation and isolating the physical type boundary; it does not manufacture
positive matching closure.
