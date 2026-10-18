# Independent final review: polynomial-grid neutral pole

Disposition: PASS for the conditional selected-plane-fibre theorem as presently scoped. No blocking volume or denominator error found. This is a focused mathematical review, not a formal repository audit. No source edits were made.

Reviewed native/POLYNOMIAL_GRID_NEUTRAL_POLE_PROOF.md, the public note, runner, and the inherited ten-layer mechanism. I challenged the local relative bounds, the successive small denominators, endpoint momentum estimates and source transfer separately; the conclusions below are not inferred from the numerical controls.

## Volume bounds

The first wall-relative comparison is valid because each retained term is individually N-preserving, and its support is completed to whole fixed-height columns. Its extension from the no-wall reference-spin operator acts trivially on wall labels. The difference annihilates the no-wall subspace on that completed support on both sides, by Hermiticity and N preservation. Summing its local projector bound gives C lambda N, not C lambda R^2. The remaining column bandwidth is O(lambda^4 R^2), tending to zero for p<2. This isolates the entire N0 band from wall excitations without assuming that full-column flips vanish at fixed height.

For the second reduction the termwise Q-preserving property is equally essential. Its support neighborhood must include the plaquettes affected by the operator and a bounded collar sufficient to test the local flat constraints. On a locally flat neighborhood, a finite-support zero-charge move cannot create remote defects. A zero-syndrome spin flip would have to contain a full noncontractible row/column and is excluded at fixed order once R exceeds the support range. The residual diagonal action is constant on local flat patterns by plane invariance. Thus the sandwich by a nearby-bad-plaquette projector is justified. Bounded overlap yields C Q as a form bound and hence a volume-independent norm on Q4.

This argument controls off-diagonal terms as well as energies. It is stronger than merely subtracting the diagonal vacuum energy; the latter would not remove the apparently distant vacuum-mediated transition. Linked local normal forms provide that necessary cancellation. The chosen physical plane sector and its area constraints are retained throughout.

## Denominators and retained momentum dependence

The successive denominators are genuinely separated: first lambda^4 between flux counts, then lambda^6 between thin and nonthin rectangles, then lambda^8 between shortest and other thin states. After the first charge reduction, the relevant sector norms are uniform, so the subsequent rescaled perturbations are small without an area multiplier. The proof explicitly requires sufficient expansion order after these divisions; it does not assume that an initial label 'order 40' automatically survives all subsequent truncations. An absolute R^2 lambda^40 final tail is attainable at a sufficiently high but fixed construction order.

For the retained two-endpoint matrix, every fixed-order path starts and ends at a shortest feature, contains finitely many local moves, and has diagonal reference resolvents. It therefore has bounded displacement moments independently of R. This endpoint-path statement avoids artifacts of choosing a center for arbitrary long complementary rectangles at the torus fold. Such folds cannot be reached by a fixed-order path from a shortest feature when R exceeds the retained support range. Uniform second/fourth derivatives near q=0 follow in the centered endpoint gauge. A norm estimate alone would not have been enough.

The charge-normal-form Hamiltonian correction starts at physical order sixteen, preserving the previously computed lambda^12 dispersion and lambda^14 orientation mixing. The scalar restriction of staggered lambda-sign covariance forbids odd effective powers. All uncomputed common diagonal shifts remain in e(lambda), rather than becoming a false curvature contribution.

For the two-orientation lower eigenvalue, the diagonal imbalance O(lambda^12 q^2) contributes its square divided by the lambda^14 gap, namely O(lambda^10 q^4). The off-diagonal variation contributes O(lambda^14 q^2). Therefore the stated leading difference and its errors follow. For every fixed 1<p<2, relative errors scale as lambda^(2p-2), lambda^2 and lambda^(28-4p), all tending to zero. The wall-bandwidth condition lambda^(4-2p)->0 independently explains the upper endpoint p<2. Neither endpoint is included.

## Actual state and original source

Exact momentum symmetry permits the comparison within each momentum fibre. The lambda^14 orientation gap is a valid projector denominator there; the much smaller spacing between neighboring momenta is not used. Within the selected plane fibre Q0 is one dimensional. The result does not need—and does not prove—uniform global selection of that fibre among all plane characters.

The normalized Fourier source first creates Q4 at lambda^10 only after the inherited direct-winding/ground-mixing cancellation. The proof retains that calculation rather than replacing it by a generic norm estimate. Each further retained coefficient applied to the flat vacuum is a finite translated-pattern sum with bounded overlap multiplicity, after centering away its scalar component. This gives a uniform Gram bound. The small-q lower eigenvector tends to the symmetric orientation vector because q^2/lambda^2->0.

The final Hamiltonian tail produces state error O(R^2 lambda^26), dividing by the smallest retained fibre gap. Even multiplication by the crude source norm O(R) gives O(lambda^(26-3p)), smaller than lambda^10 throughout 1<p<2. The ground projector has the larger lambda^4 gap. Thus neither source transfer nor actual energy comparison loses the claimed asymptotic signal to volume factors.

## Replay and claim limits

I executed both helpers directly and reproduced the runner assertions without generating repository output files. The connected second-order rows agreed at R=10,12,16,20: 33 nonzero entries, diagonal -7/2, absolute row sum 35/2, and exactly zero distant transition. The last three dispersion errors were approximately 1.053e-6, 2.344e-18 and 1.895e-6, passing the stated 2e-6 bound.

These computations validate concrete connected coefficients and the derived small two-orientation matrix. They do not diagonalize the enormous microscopic polynomial grids. The actual-grid conclusion rests on the analytic uniform bounds above, as both runner scope and proof state. The retained poor finite-lambda isotropy example is appropriate; the theorem provides no practical numerical lambda threshold.

The public note accurately reports a resolved discrete-momentum selected-sector pole and a source atom, rather than a three-dimensional scalar field, Lorentz invariance or universal gravity. This is stronger than the earlier coefficient-only curvature result, but remains conditional on the supplied ten-layer Hamiltonian, weak-anisotropy limit and chosen exact plane sector. No observational identification or uniform global-ground-character theorem is obtained.
