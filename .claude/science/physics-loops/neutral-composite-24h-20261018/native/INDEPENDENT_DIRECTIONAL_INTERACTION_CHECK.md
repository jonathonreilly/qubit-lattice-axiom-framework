# Native diagonal-column pair interaction at eighth order

Disposition: PASS for the local nonwrapping diagonal interaction coefficient at fixed height L=10 (and heights exceeding the virtual-word reach). This is a connected energy coefficient, not a scattering amplitude or a statement about all interactions.

## Independent calculation of the two-square coefficient

I used a different expansion from the root's multivariate Rayleigh recursion: the vacuum Feshbach self-energy. For the eight distinct edge variables, the coefficient is the sum of all irreducible eight-edge permutations (no proper vacuum return), plus E4(A) Sigma4'(B)+E4(B) Sigma4'(A). This includes the energy dependence of the resolvents and hence the required folds. Each resolvent derivative contributes the original word weight times the sum of reciprocal positive intermediate costs.

Direct physical spin-bit evaluation of all 40320 permutations gives:

| layer offset | irreducible sum | folded sum | connected sum |
|---|---:|---:|---:|
| 0 | 1/131072 | 5/131072 | 3/65536 |
| 1 | -133/2654208 | 5/131072 | -127/10616832 |
| 2 | -5/131072 | 5/131072 | 0 |

For each isolated square E4=-1/128 and Sigma4'=-5/2048. This explicitly verifies the fold signs; discarding folds would give the wrong sign and fail the separated-layer cancellation. Reflection makes offsets +1 and -1 equal. For larger separated layers the vertical H0 energy is additive on the two supports, so the connected sum vanishes exactly just as at offset two.

The physical intermediate energy is 4 per flipped spin minus 4 for each adjacent simultaneously flipped pair on the shared column. This is the correct longitudinal ZZ energy relative to an aligned background. At coincident layers the squares share one actual spin; at neighboring layers they share a column with one interacting vertical bond. No interaction is present for layer separation at least two, outside periodic aliases.

## Primitive cycles and background signs

A second independent direct permutation sum for the three simple eight-cycles relevant to columns (0,0),(2,2) gives:
- 2-by-2 square boundary: -9/262144.
- Each of the two three-cell L boundaries: +5/262144.

The total is therefore +1/262144 per layer. The signs depend on the physical XX/YY word phases; replacing them with unsigned path counts would be incorrect.

The two-square monomial has background factor P_(0,0) P_(1,1). Each of the two specified columns occurs once in that product, while the shared corner cancels. The three simple-cycle products likewise contain both specified columns. A term c times such a parity product contributes 4c to the connected two-column energy E(both)-E(first)-E(second)+E(neither). This fixes the interaction sign without a convention for 'attraction'.

## Completeness at order eight

Below height-ten winding order, returning to N0 requires even flip degree at every physical vertex in every layer. The odd-multiplicity edge graph is therefore Eulerian in each layer. Repeated edges do not change the background Z monomial; denominators of aligned-column virtual states depend on flipped-spin patterns, not the signs of the background columns.

For a simple cycle to contain both (0,0) and (2,2), the two arcs joining them each have length at least four. At total perimeter eight they are shortest monotone paths. The simple cycles are exactly the 2-by-2 boundary and the two L-triomino boundaries just evaluated. Smaller four/six cycles, even with repeated edges, cannot have both columns in their sign support.

The remaining possibility is two four-cycles. To contain both specified columns and interact through shared physical-column support, their anchors must be (0,0) and (1,1). Equal-layer and neighboring-layer cases are precisely the computed coefficients. Disjoint column supports have additive H0 energies and their connected terms cancel. Two cycles already use all eight operations, so no extra connecting repeated edge can be inserted. Overlapping adjacent squares reduce to smaller-span sign monomials and cannot distinguish both specified columns. Folded products are included above and cannot create a missing spatial connection.

Although H0 has many aligned-column states, no different N0 configuration is reachable in eight transverse insertions at L=10: a nontrivial even-column change requires at least twenty physical flips, hence at least ten insertions. Thus the fixed-background scalar Rayleigh/Feshbach computation is valid through this order. It must not be extrapolated across winding orders without degenerate perturbation theory.

## Result and scope

There are L same-layer choices and L choices for each adjacent-layer offset on the periodic height-ten column. Therefore

 c_total = 1/262144+3/65536-2*(127/10616832)
         =545/21233664,

 V_(0,0),(2,2)=4JL lambda^8 c_total
              =JL lambda^8 *545/5308416 >0.

This is repulsive in the connected diagonal-energy convention. It is not the complete absolute energy, an all-order pair potential, or a full scattering result. Short transverse/longitudinal aliases are excluded.

Independent scratch: /tmp/neutral_diagonal_reviewer.py, /tmp/neutral_diagonal_reviewer.json, /tmp/neutral_diagonal_cycles_reviewer.py. Root /tmp/neutral_two_square_linked.py was read, not edited. No repository changes or formal audit.

## Companion axial separation (3,0)

PASS: the first connected interaction between columns (0,0) and (3,0) occurs at order eight. A simple cycle containing both as turning vertices needs perimeter at least eight. At perimeter eight the only possibilities are the two 3-by-1 rectangles immediately above and below their common axis. Each has the independently checked coefficient -9/262144 and contains both column signs once. Thus

 V_(0,0),(3,0)=4JL lambda^8 *2*(-9/262144)
              =-9JL lambda^8/32768.

Four- or six-edge sign cycles cannot span three along x; repeated edges cannot extend their sign monomial to the other endpoint. Two elementary squares containing the respective columns necessarily have disjoint physical-column supports: even their closest anchors are separated by two in x. Their connected coefficient vanishes, including when their layers are adjacent, since there is no shared vertical column interaction. No further connecting insertion is available at eight operations. Hence no omitted figure-eight term changes this axial coefficient.

This establishes shape-dependent order-eight attraction at axial separation three and repulsion at diagonal separation (2,2). Both exceed the order-ten elementary kinetic scale asymptotically. It does not classify the full Q8 perimeter-sixteen manifold, establish an isolated additional band, or justify a scattering/barrier interpretation beyond these connected diagonal energies.
