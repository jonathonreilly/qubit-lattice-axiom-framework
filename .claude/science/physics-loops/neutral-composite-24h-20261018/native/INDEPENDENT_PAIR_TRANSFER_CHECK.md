# Native pair-channel microscopic transfer: focused check

PASS for the matched finite-time comparison, using the cited fixed-Q local-normal-form and exhaustive shape results. No fixed-lambda microscopic scattering theorem follows. No repository edits or formal audit.

Reviewed NATIVE_PAIR_SCATTERING_PROOF.md, especially its microscopic transfer section, against the termwise relative bound in POLYNOMIAL_GRID_NEUTRAL_POLE_PROOF.md and the complete Q8/perimeter16 classification in SECONDARY_NEUTRAL_MOLECULE_PROOF.md. The order-ten coefficient calculation and numerical scattering constant are separate previously checked inputs; this review does not independently replay those calculations.

## Channel and uniform gap

The zero order-eight-shift sector consists of the allowed two-column separations with all shifted shapes removed. The stated ordered domain excludes the 37-site Manhattan core except its four axial-distance-four tips. The infinite odd-rod family and T family are not forgotten: their nonzero order-eight shifts put them above this channel. Axis-three and skew-(3,1) shapes are below it; eliminating a lower band is valid when the spectral separation is uniform and does not assert those states disappear. The smallest magnitude of the order-eight separation is the skew gap v/2. Order-ten terms have bounded fixed-Q norm, so for sufficiently small lambda they cannot close this order-eight gap, uniformly in R.

Other perimeters have an order-six separation and other fixed charges an order-four separation. The global Q-relative positivity estimate is needed to exclude arbitrarily high-charge states from this low-energy window; an extensive no-wall bandwidth estimate alone would fail. The inherited all-polynomial low-energy embedding supplies this stronger statement. Exact total momentum and physical plane restrictions are maintained. The ordered representation must be restricted to inversion-even relative states to represent the identical physical columns; it is not a distinguishable-particle cross-section convention.

## Why the scaled remainder is O(lambda²)

The cited termwise local result says that a retained connected Q-preserving coefficient minus its flat scalar is sandwiched by a nearby-bad-plaquette projector. Bounded overlap gives norm C Q on a fixed-Q sector, independent of volume. Thus Q8 retained coefficients, including those acting on long inverse rod representatives, are uniformly bounded. One should count syndrome defects, not the number of reversed columns. Local Q-preserving moves away from all syndrome defects are scalar and cancel in vacuum subtraction.

On the perimeter16 sector the order-eight distinguishing diagonal has a uniform separation of its zero-shift subspace. Order-ten mixing has bounded norm, so its block rotation is O(lambda²), and its second-order feedback is O(Jlambda12). Eliminating more distant charge/perimeter sectors costs smaller enhancements and does not produce an earlier error. Subsequent fixed-order products/resolvents remain bounded by the gap constants and fixed order, rather than by the number of states. Checkerboard symmetry is scalar on the even-height wall-free basis and eliminates odd powers. Accordingly the first omitted retained coefficient after the complete order-ten operator is indeed order twelve, not an assumed order eleven.

This justifies ||B_lambda,R||<=C lambda²+C R²lambda^(M−10) after division by Jlambda10, provided M is the final order after every denominator loss and both states and operator are transformed together. Those qualifications are explicit. Large extensive scalar phases must be subtracted consistently; the proof does so. The leading K_R includes both the native winding adjacency and the full stated order-ten U, rather than suppressing winding at its first order.

## Evolution precision and scope

Duhamel gives |tau| times the scaled operator error. At R~lambda^(−2/3), tau~lambda^(−1), its two terms are lambda and lambda^(M−37/3), as stated. The O(lambda²) matching error refers to the eliminated shape-block identification in the dressed normal-form frame. It is not a claim that a bare physical product preparation is within O(lambda²): microscopic wall dressing can begin at O(lambda). The text requires matched preparation and leaves its error separately, which preserves this distinction.

For any fixed polynomial size exponent one can choose a sufficiently high final M; times o(lambda^(−2)) are controlled by the retained remainder. This is a comparison of finite-volume propagators, not automatically a scattering experiment: packets, boundary-return times, finite/infinite-volume approximation and extraction of a small on-shell signal need additional control. The text expressly declines these promotions. In particular it correctly says the O(lambda²) remainder does not control first-grid scattering energies on p>1 boxes over their inverse-energy timescale.

The positivity/no-resonance and logarithmic T statements refer only to the leading infinite relative-coordinate operator. The hard obstacle is a representation of eliminated channels, not a new microscopic repulsion. Numerical B is explicitly uncertified coefficient-model data, with a finite-integral definition. No physical rate, full inelastic S-matrix, universal force or empirical test is inferred. No remaining transfer issue identified within this scope.
