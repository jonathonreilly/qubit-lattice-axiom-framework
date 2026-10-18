# Polynomial-grid dispersion: focused independent check

PASS in substance for the finite-order route, with two short explanatory clarifications requested below. No source edits or formal audit were performed. This review checks the new proof, reusing the prior exact native coefficient and ten-layer mechanism checks. It does not treat numerical controls as a substitute for the uniform argument.

## Local Q relative bound

Charge averaging and inverse ad_Q preserve bounded support because Q is a sum of commuting local integer projectors and only overlapping plaquettes act on a local operator. The scalar-subtracted local coefficient bound is valid in the constrained physical algebra, provided the enlarged neighborhood contains the affected plaquettes and a bounded filling neighborhood for the invariant diagonal monomials. A Q-preserving local operation on a defect-free neighborhood cannot change Q elsewhere. An off-diagonal zero-syndrome move would be a row/column kernel flip, impossible with bounded support once R exceeds that support. Plane symmetry makes the remaining diagonal action constant on local flat configurations. Hermiticity then supplies the sandwich by Pi_t on both sides.

Summing the bounded-overlap projectors gives a form bound C Q, and hence a uniform norm on Q4. This controls the full charge-sector coefficient, not merely an individual configuration. Connected local commutators cancel disconnected vacuum-mediated paths, including off-diagonal far hops. The positive plane-sector and even-area constraints are retained; no unphysical single/two-flux state is imported.

The original wall-sector bridge also checks: extending the N0 term to the reference-spin label leaves wall labels unchanged; the difference is supported on configurations with a wall in its enlarged columns. The shared lower scalar can be subtracted even when extensive. For p<2, the remaining N0 bandwidth O(lambda^4 R^2) tends to zero and the wall-relative bound separates the entire N0 band from N>=2. Fixed-height whole-column flips are included, rather than wrongly excluded.

## Low-defect reductions and spatial moments

The Q4 coefficients have bounded row sums in the syndrome basis: a scalar-subtracted local term must meet one of four defects, has finitely many output configurations, and cannot translate a shortest feature to a distant position in one step. At fixed order only finitely many such steps occur. The thin/nonthin and endpoint/rest reference resolvents are diagonal in the rectangle basis and have uniform rescaled denominator bounds; they do not move configurations. Thus the composed paths have bounded row sums weighted by any fixed power of displacement. This makes the claimed second/fourth momentum estimates stronger than a bare operator-norm estimate and rules out nonlocal derivative leakage.

All retained common endpoint shifts can remain unspecified scalars. C4 equates the two onsite energies, while centered Bloch conventions plus inversion and real symmetry give a real even two-orientation matrix locally near q=0. Finite periodic Bloch-gauge twists away from that neighborhood do not affect the claimed grid asymptotic. Direct translating/orientation-changing native processes cannot preempt the previously checked lambda12 and lambda14 mechanisms; the Q-normal-form change itself begins at physical order sixteen.

For precision, explicitly state the staggered lambda-to-minus-lambda covariance: on N0 it acts as identity when longitudinal L is even, so the effective Hamiltonian can be chosen even in lambda. This justifies the next dispersive correction being lambda14, rather than an unexplained exclusion of lambda13.

Also state that both low-defect finite-order reductions are carried sufficiently far AFTER accounting for their lambda6/lambda8 denominators to leave an absolute remainder bounded by C R^2 lambda40. The initial microscopic order forty does not, without such accounting, automatically label every subsequent truncated reduction's remainder. Since these reductions have uniform rescaled gaps and arbitrary fixed expansion order is available, this is a bookkeeping clarification rather than an obstruction.

## Two-orientation eigenvalue and error powers

Let d(q) be half the diagonal difference and b(q) the off-diagonal entry. Then d(0)=0, d(q)=O(lambda12 |q|^2), b(0)=-eta lambda14[1+O(lambda^2)], and b(q)-b(0)=O(lambda14 |q|^2). Expanding the lower eigenvalue trace/2-sqrt(b^2+d^2) for q/lambda tending to zero gives precisely

    J(kappa/2)lambda12 |q|^2
      +O(Jlambda14 |q|^2+Jlambda10 |q|^4).

The lambda10 |q|^4 term is the squared imbalance divided by the orientation gap. The ordinary lambda12 |q|^4 term is smaller and can be absorbed. For p=21/20, the leading exponent is 14.1, orientation correction 14.2, higher quadratic correction 16.1, and global tail 37.9. All are in the claimed order. Exact momentum preservation lets the tail be compared separately in each fibre; no neighboring-momentum level spacing is used as a spectral denominator.

## Source and microscopic projection

The flat-vacuum source first enters Q4 at lambda10 only after the ground-mixing subtraction. Its normalized local-pattern Gram bound is uniform: distinct finite translated syndromes overlap only finitely often, and a spurious zero-syndrome ground component is removed before that estimate. Row/column orbit equivalence cannot identify far distinct bounded patterns when R exceeds their support range. The small-q endpoint eigenvector tends to the even combination because q^2/lambda^2 tends to zero. Hence the original source coefficient is preserved.

The smallest retained fibre gap is lambda14. Dividing the global tail R^2 lambda40 by this gap gives R^2 lambda26 state error. Even multiplication by the crude source norm O(R) gives lambda^(26-3p)=lambda22.85, smaller than lambda10. The ground uses its larger lambda4 gap. This is sufficient once Hamiltonian and source tails are both constructed to the stated order.

The theorem is therefore supportable as an actual selected-fibre finite-grid energy-difference and source-atom statement. It does not establish a continuously differentiable full-H dispersion uniformly outside these resolved grid points, a uniform global-ground character, three-dimensional propagation or empirical identification.

Reviewed initial SHA256: 6ece61ffe35ea6e760d8af9760297210f5a558e4b75a209af70941d513651418

## Affected-fix confirmation and enlarged p range — final PASS

Both requested clarifications are now explicit: staggered parity is scalar in the selected N0 sector and removes odd effective powers; both subsequent low-defect reductions are taken far enough, after denominator accounting, to preserve the absolute R^2 lambda40 tail and spatial-moment bounds.

The enlargement to every fixed 1<p<2 is valid for this local-Q route. Relative to the leading lambda^(12+2p) grid difference, the orientation error is smaller by lambda^(2p-2), the higher quadratic correction by lambda^2, and the global tail by lambda^(28-4p). The wall-sector bandwidth tends to zero as lambda^(4-2p). The crude source leakage has power 26-3p>20 and is smaller than the lambda10 source. Thus all inequalities are strict throughout the stated open interval. Constants may depend on the chosen fixed p; neither endpoint is included.

At p=3/2 the stated example powers are correct: leading 15, orientation correction 16, global tail 37, and source leakage 21.5. The earlier p=21/20 calculations in this report describe the initial draft, not a restriction on the final theorem. No material issue remains. Numerical controls being built by root were not used as a replacement for this analytic check.

Final canonical SHA256: 6ece61ffe35ea6e760d8af9760297210f5a558e4b75a209af70941d513651418.
