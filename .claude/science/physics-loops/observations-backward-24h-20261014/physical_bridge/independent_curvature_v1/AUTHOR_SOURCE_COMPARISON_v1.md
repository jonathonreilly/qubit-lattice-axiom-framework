# Source-bound curvature comparison supplement

Reviewer /root/inertial_response_check; root remains author. This supplement
follows the frozen independent precheck, 209-condition synthetic run and
INDEPENDENT_REVIEW_v1.md. Those files retain their original hashes and scope.
I then read the COMPLETE author curvature note, complete critical control
script and result, the two massive working/refinement notes needed for its
BV and comparison suppliers, and the curved-count composition companion.
Exact unmodified copies are preserved here with AUTHOR_ prefixes. No author
aggregate suite was imported or rerun, and no raw observation was opened.

## Scoped result and exact sources

No consequential mathematical or implementation discrepancy was found in the
field/energy/weight transform, potential-comparison proof, its BV suppliers,
or their stated consumption in the count energy bound. The energy constants
are the same quadratic-form comparison in inverse orientation. This is a
focused source check, not a formal audit or complete canonical publication
review. The distinct independent four-endpoint construction and the full
massive-response review remain the other assigned checkers' scopes.

Inputs:

- CURVED_COUNT_WORKING_v1.md:
  84cb8fb11a008f6ca8fd268f20f1dede6d5aaded0b4a206065e93f57acba4ba2.
- curved_count_controls_v1.py:
  4a272c55ab3ba6a81b51bd3c1d33519a38cd13bd3b7d3a382c600baf43f79ae2.
- CURVED_COUNT_RESULTS_v1.json:
  204a5b8eaed4773dc8cc8d69e52557544d83483a86d5bc4463f902b9609cb46c.
- MASSIVE_RESPONSE_WORKING_v1.md:
  4131181f0d73351ef2eaddf7b24dbcceb5d680351db1ede0ed38badbdf433e8d.
- MASSIVE_REFINEMENT_WORKING_v1.md:
  448ec6ee42a4ae27c087cc05efcf940f047054228862be8fd76952c7493ce6bb.
- CURVED_COUNT_COMPOSITION_v1.md:
  dae8894dd8740055d12a9f84b59a33146e95e9284fc2046cd132c514593c7ce3.

The author note imports the explicit supplied action from the already read
curved-response canonical note; it is not yet a standalone canonical action
packet. Its force BV constants are supplied by the exact two massive notes
listed above. This dependency and the separately checked massless-reference
comparison must remain explicit in later packaging.

## Normalization, coordinates and energy

The author h equation and chi=a h transformation match the independent proof,
including -a''/a and V=(B-2)H^2 a^2. The time variable is conformal time and
the spatial coordinates/momenta are comoving. The reference lapse
ell=a sqrt(1-|u|^2) and coordinate Hubble force are retained; null-ray
conformal invariance alone does not flatten clocks or body dynamics.
The transformed clock term +(1-|u|^2)mathcalH(W.u)/a has the independently
derived sign. The source explicitly forms the curved reference adjoint rather
than substituting a different field into calibrated flat weights.

For its convention N0=integral[p^2+|grad f|^2+mu0^2 f^2], N0 is a SQUARED
norm. Its physical quadratic energy is E_phys=Q integral[(p-Hf)^2+
|grad f|^2+B H^2 f^2], because the action's scalar kinetic coefficient is
-Q, not -Q/2. The two-by-two physical/computational matrix is
[[1,-r],[-r,1+3r^2]], r=1/sqrt(B-2), with eigenvalues
1+3r^2/2 +/- sqrt(r^2+9r^4/4). They equal my 1/lambda_+ and
1/lambda_- respectively. Thus its final energy lower bound correctly uses
Q times its smaller eigenvalue and has no extra factor1/2. The initial slice
a=1 makes this comparison particularly simple; the author correctly states
the 1/a factor on another slice and makes no conserved global physical-energy
claim. Scalar initial data are arbitrary in the stated positive-energy class.

## Independent check of the coefficient and Gronwall argument

For f''+(omega^2+U)f=0 with f(0)=1, f'(0)=i omega, define
A_+=(f+f'/(i omega))exp(-i omega t)/2 and
A_-=(f-f'/(i omega))exp(i omega t)/2. Their matrix equation is
A'=M A, M=(iU/(2omega))[[1,exp(-2iomega t)],[-exp(2iomega t),-1]].
Its induced l1 norm is |U|/omega exactly. Its derivative norm is at most
|U'|/omega+|U|; differentiating the off-diagonal phases is essential for the
second term. Therefore
sum|A|<=R, sum|A'|<=R U0/mu0, and
sum|A''|<=R[U1/mu0+U0+U0^2/mu0^2], R=exp(S/mu0).
This proves the author's constants. The coefficient difference from (1,0)
is at most R S/omega; multiplying by omega in f' gives R S. Positivity of
mu0, fixed initial epoch and finite T<1/H are essential. These constants may
be much looser than the monotone-energy estimate I derived independently,
but that is not an invalidity. No estimate is asserted uniformly at the chart
boundary or after changing the initial-data convention.

## Exact branch force identity and BV tail

With the author's exp(i sigma omega t-i k n.x) convention, branch force
starts from the derivative of A_sigma exp(i sigma omega t), so it includes
A_sigma'. Integration by parts of the phase gives precisely
(1/omega) integral[A_sigma j_sigma-A_sigma' r_sigma] exp(i phase),
j_sigma=-(b_sigma.W)',
r_sigma=(b_sigma+(1-|u|^2)u).W.
Using the constrained total f' expression instead yields b_sigma in the
A_sigma' term, but the difference cancels in the summed branches because
sum A_sigma' exp(i sigma omega t)=0. Thus the author's extra u term is
consistent; it must be retained if a branch is treated as a separate field.
The second BV integration divides by d_sigma and contributes the second
1/omega. It retains all zero-extension jumps. Compact continuous W with
W' BV and C3 paths is enough. This is a stronger force-weight hypothesis
than the original full M6 H1 domain; the source labels it as such.

For a complex BV product, TV(A g)<=sup|A| TV(g)+sup|A'| ||g||1.
Apply it once to A_sigma j_sigma/d_sigma and once to
A_sigma' r_sigma/d_sigma. Summing both branches yields the stated C_F.
The factor2 is conservative because separate suprema need not occur at the
same time. The frozen positive branch is bounded by V_F/omega^2. Therefore
the difference tail (C_F+V_F)/k^2 is valid, including interference, without
assuming a massive/massless Loewner order.

I checked the quotient-rule suppliers B0,B1,B2 in the original massive note:
the numerator derivative bounds Q1 a and (2+6beta)a^2+Q1 j are valid, and
the two denominator-derivative terms give the listed B2. For r_sigma,
R0=B0+beta and R1=B1+(1+2beta^2)||u'|| are conservative. Product variation
then gives the stated G_F, R_L and V_R. C3/path partition assumptions and BV
zero extensions are necessary inputs, not values recovered from data.

## Low/high combination and physical consequence

The normalized real-energy positive-frequency kernel uses the initial
omega. Direct clock comparison is R S C/omega^2; radial integration gives
R S C sqrt(pi/(4mu0)). Hence compact L2 clocks suffice on the finite support;
no additional BV clock condition is required for this comparison. This is
stronger than my joint-amplitude precheck, which used BV c to combine the
clock and force before the split.

The low-force estimate is R S D/omega, D=(1+beta)sum||W||1. Its radial
norm below K is at most R S D sqrt(K), while the tail is at most
(C_F+V_F)/sqrt(K). Minimizing their triangle upper bound gives
K=(C_F+V_F)/(R S D) and 2sqrt(R S D(C_F+V_F)). Multiplication by
1/(sqrt(2)pi) is exactly the radial factor from the real energy Hilbert norm,
not an extra independent negative-frequency branch. The source handles
S=0, absent force and limiting cutoffs separately. A Pythagorean treatment
could improve this conservative constant but is not needed for correctness.

Adding the already supplied frozen-mass comparison is legitimate only on its
common energy-amplitude isometry. That isometry does not preserve physical
initial fields between different masses; the massive note says so explicitly.
The varying-potential and frozen-massive pair, in contrast, DO use the same
initial chi data. A single origin is used for all paths and mass-comparison
moments. The resulting bound on a true curved response norm, followed by
E_phys>=Q lambda_- N0, gives the stated residual lower-energy inequality.
It supplies no energy upper bound, measured residual/error, state or parameter.
The denominator-zero feasibility case is explicitly separated.

## Critical code and count-weight interactions

The complete control script's f evolution implements k^2+mu0^2 a^2 and
initial derivative i omega. Its perturbed comoving body evolution implements
(a delta u)'=-alpha grad chi in the chosen plane-wave convention, and its
station clock obeys eta'=alpha chi. The original two-leg endpoint evaluation
retains emission, bounce, reception, the shared station clock and both body
positions. Its weighted comparison uses the transformed curved coefficients,
not flat coefficients. Arbitrary initial orbit/clock values are changed in a
separate check. The proper-time count conversion uses logarithmic de Sitter
proper intervals and the beta cumulative-sum weights with the correct sign.
The result file binds the exact note/code hashes and records 20 author
aggregate controls; it is read evidence, not a rerun by me. Small error and
random tests are not proofs of rank, uniform remainder or physical calibration.

I checked the input interaction with the four-endpoint construction: the
quadratic P, gamma moments, beta=d_e gamma, zero outer weight traces and
total comparison-clock cancellation are consistent with the independently
derived field/energy mapping. The response to a constant chi in the massless
comparison is the relevant C0; this must not be reworded as selecting a
homogeneous physical h. The stationary suppliers C, Wsum, Wp and V_F in the
composition companion follow from the finite step-function moments and BV
jumps; the stated constants are conservative for 0<H<5/22. Their common
origin is the initial conformal epoch0. The exact Gram's piecewise event
ordering, force/clock signs and 1/(4pi) angular factor are consistent with the
M6 real norm. I do not replace the other checker's independent four-endpoint
Gram derivation with another claim of independent reproduction. Its H=0
value agrees with the previously independently derived M6 difference-channel
norm 329/(54pi).

## Narrow new evidence and limitations

I wrote and ran author_potential_comparison_v1.py, using separately solved
modes and my independent polynomial moving-path fixture; it imports no author
module and reruns none of the author aggregate suite. Five momentum values,
three directions and both branches test the full branch identity. Separate
121-point grids per momentum check the coefficient matrix derivative and
Gronwall bounds. There are 747 recorded conditions, of which605 are those
grid-point matrix checks; this is not747 independent physical tests. All
passed, with no failed execution. Maximum branch/total-force identity error
was7.55e-16; matrix-norm discrepancy was2.78e-17. The largest sampled Gronwall
ratio was0.9790771. These checks support, but do not replace, the complete
analytic coefficient/BV reasoning above. The root C1 bound was evaluated with
conservative analytic suppliers; no fitted prefactor or changed tolerance was
used. All numerical quadrature is non-certified.

No change to the reviewed author source is requested. No actual physical
count, measured cosmological/field energy, source environment, nonlinear
history, action selection or initial-state selection has been established.
No source/index/branch/lock/state/publication action, network, raw-data read,
additional agent or formal audit was performed. This supplement and its exact
input copies remain in the assigned independent_curvature_v1 directory.
