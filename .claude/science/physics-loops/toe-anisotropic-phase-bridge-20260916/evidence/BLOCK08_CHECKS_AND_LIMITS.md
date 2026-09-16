# Personal checks of the short-time bridge action

The current `block08_bridge_action_check.py` has SHA256
`9cefefd665591e4c2961f42aef1dbd3503bdd476715e8405291e77ec8be02d2f`.
ATTEMPT2 passed in1.115seconds with empty stderr. These are author checks,
not an independent review or a phase computation.

The first check retains the actual two-adjacent-plaquette metric
[[4,-1],[-1,4]]. Deterministic Gaussian quadrature integrates a bridge with
three time slices and four Gaussian coordinates, at quadrature orders16
and20. Twelve parameter/endpoint cases include small curls, curl pi and
endpoints straddling the compact branch. The finite time quadrature uses
its exact Dirichlet precision constant, not the continuum pi^2/T^2 value.
The largest quadrature-order change is3.856e-11. The covariance formula
for the endpoint Hessian agrees with finite differences to the stated
2e-7 tolerance. The Hessian correction, mean displacement and variance
are below the analytic comparison bounds. Omitting the covariance term
produces a detectable discrepancy. No rigorous Gaussian-quadrature or
time-quadrature remainder is certified by these finite comparisons.

A separate one-plaquette control has strictly convex interior path action
(r=.01778) but negative common-endpoint curvature(-.199334). It detects
the false inference from bridge convexity to global endpoint convexity.

The time-limit challenge diagonalizes the compact one-plaquette
Hamiltonian independently in its electric Fourier basis. Cutoffs24 and36
change the tested kernel by1.777e-15; this is a cutoff comparison, not a
rigorous infinite-cutoff certificate. At g=.4,T=.2,x=.3,y=.7, bridge time
quadratures with2,3,4,5 slices approach the spectral effective action with
errors.0001944,.00008633,.00004855,.00003107. The independent covering
image bound for all nonzero windings is8.719e-58 at these parameters.
These observations challenge normalization and limiting formulas; they
do not establish their general proof or the spatial phase.

## Manual correction after an initially passing run

ATTEMPT1 passed its own assertions, but subsequent source inspection found
that its quantity named a nonzero-winding bound summed only images k=-8
through8. That finite positive sum was not an upper bound for all images.
The source is preserved as `block08_bridge_action_check.ATTEMPT1.py`,
SHA256`48f456f21c11558be67689d4e6f25979036f7b4a843d06b6651bac352d15e25f`,
together with its stdout and empty stderr. Its PASS does not certify the
misnamed bound. ATTEMPT2 replaces that expression by a geometric majorant
for the complete infinite sum, using k^2>=|k| for nonzero integer k.
No numerical threshold was relaxed. The revised bound is larger, remains
below1e-40, and is the only winding bound used in the current receipt.

Run the current program with python3, NumPy and SciPy. Spatial derivative
locality is justified by the analytic vector-component Neumann argument;
this runner does not separately check long-distance locality. All results
remain supplied-Hamiltonian statements, with compact periodization and
long-time composition still explicit obligations.
