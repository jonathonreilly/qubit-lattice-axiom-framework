<!-- Original PR9769 source SHA256 08d9207ababe3dcd8a325bee131c2c49803573a5460bf26faaa28670476bfc26. -->
**Source boundary:** Complete mathematical argument follows. Historical verdicts, execution narratives and provisional instructions are provenance only. Exact identities and conditional mathematical implications remain live; no audit status or additional physical premise is conferred. Earlier exploratory statements are read with their explicit later corrections.

# Fixed-order rectangular corner law: focused check

Disposition: PASS with explicit locality, background, and boundary qualifications. This is a coefficient-level diagonal bulk statement, not an eigenmode or convergent all-orders theorem.

## Symmetry and locality

Fix a finite perturbative order m. Assume the local normal-form construction is equivariant under the exact physical plane symmetries, and each coefficient admits finite-support local terms with transverse coordinate span bounded by R_m (and finite longitudinal span). Evaluate its diagonal matrix element in a Z-product configuration that is longitudinally constant throughout the neighborhood of every term considered. This produces a finite-range function of column signs s_xy. Off-diagonal matrix elements do not enter this diagonal energy statement. For sufficiently long ordered intervals, a bounded-support term cannot flip whole columns while remaining inside that interior subspace, but that observation is not needed to prove the diagonal claim itself.

A physical plane symmetry can attach basis phases while flipping a row or column of signs. Those phases cancel in a diagonal expectation. Equivariance therefore makes the diagonal function invariant under each full row/column sign flip. In its unique Walsh expansion, every nonzero monomial has an even number of sites in each x slice and each y slice: conjugation multiplies that monomial by its slice parity, so an odd monomial's aggregated coefficient must vanish. This is a statement about collected Walsh coefficients. A chosen unsymmetrized local-term decomposition need not satisfy it term by term before cancellations. Averaging the local decomposition over symmetry actions, or simply collecting Walsh coefficients, preserves the finite support and gives the needed representation.

The symmetries must be exact for the actual geometry, and the selected normal-form gauge/construction must preserve them. These are legitimate explicit premises; exact microscopic symmetry alone would not authorize an arbitrary non-equivariant effective gauge without transforming the symmetry too.

## Rectangle cancellation

Let F=I_x x I_y be a rectangle, and M_S(s)=product_(r in S) s_r an allowed Walsh monomial. Flipping F multiplies M_S by (-1)^(|S intersect F|). If S does not cross a y boundary, either its y coordinates all lie inside I_y, in which case |S intersect F| is a sum of even x-slice incidences, or all lie outside, in which case the intersection is empty. The same argument with x and y exchanged applies when S does not cross an x boundary.

Thus an odd intersection requires crossing BOTH an x boundary and a y boundary. Bounded transverse span then places the support within O(R_m) of a rectangle corner. With opposite boundaries separated by more than twice the range, no one such support couples different corners. The cost per longitudinal layer receives contributions from only O(R_m^2) possible transverse anchor locations near the four corners, multiplied by a coefficient-dependent finite number of cluster types. It has no area or perimeter contribution at that fixed order. The O(R_m^2) description counts anchor locations, not a universal bound on the number or norms of all order-m monomials.

## Exact size independence and its limits

Translation invariance plus a homogeneous reference column pattern makes each separated corner contribution independent of the two side lengths. More generally, it suffices that the four translated corner neighborhoods have the same local background patterns in the comparisons. Translation invariance of the Hamiltonian alone does NOT make the coefficient independent of side length in an arbitrary nonuniform background: the corner monomials sample that background and their signs can change as corners move. The support-only corner law still holds there.

On a transverse torus require both the rectangle widths and the complementary wraparound separations to exceed the relevant range. A rectangle spanning a complete period, or corners close across the periodic seam, is not covered by the four-separated-corner count. Small circumferences can likewise introduce winding supports or identify corners. In the longitudinal direction the statement is for a bulk layer farther than the coefficient's range from the two droplet endpoints; endpoint terms and terms bridging the endpoints require separate bookkeeping. At fixed order all these qualifications can be enforced geometrically.

## Leading native coefficient

For the native plaquette term -kappa sum P with P initially +1, a nonwrapping separated rectangle produces exactly four bad plaquettes. Each costs 2kappa, hence the diagonal bulk tension is 8kappa=Jz lambda^4/16 with the stated kappa=Jz lambda^4/128. This leading coefficient is independent of rectangular area and side lengths. A finite longitudinal droplet has two broken longitudinal bonds per flipped column; each costs 2Jz, so its unperturbed endpoint/rest energy is 4Jz times the rectangle area. These are compatible statements about different parts of its energy.

Higher fixed-order corner coefficients need not be positive. The result supplies neither a full spectral tension nor a pole, binding, stability, or large-feature eigenstate theorem. It does not sum the perturbation series, interchange order with large-shape limits, or justify uniform control as m grows. One may state a separate exact coefficient corner law for each finite m and rectangles larger than its locality range.

No repository changes or independent numerical replay were required; this report checks the stated symmetry/locality argument and its mathematical scope.
