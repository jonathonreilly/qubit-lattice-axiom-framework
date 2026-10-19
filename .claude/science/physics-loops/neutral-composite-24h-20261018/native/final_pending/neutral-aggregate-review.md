# Independent coarse-subset aggregation check

Disposition: PASS for the arbitrary finite-subset diagonal identity and its fixed-n variational consequences. It is not a derivation of a closed coarse Hamiltonian, a global optimal shape, or stable many-feature bound states.

## Exact syndrome geometry

The feature in coarse cell (i,j) flips columns (4i,3j) and (4i+1,3j). Its bad plaquettes are

    S_(i,j) = {4i-1,4i+1} x {3j-1,3j}.

These are two vertical dominoes separated by one vacant plaquette column. Each feature has Q=4 and perimeter 12. Different coarse cells' syndromes are disjoint and have no nearest-neighbor bad-plaquette adjacency: the closest bad coordinates across neighboring coarse cells differ by two in the direction of separation. Thus for EVERY finite coarse subset A, not just rectangles,

    Q=4|A|, perimeter=12|A|.

The common scalar/P/nearest-PP coefficients consequently cancel against |A| separated features through the relevant orders. Each motif flips two columns and is plane neutral at L=10. In a positive-plane quotient, use a sufficiently large nonwrapping torus so that distinct finite patterns are not identified by a whole flat row/column flip; alternatively formulate the identity directly on the infinite column background.

## Why the complete D8 interaction is pairwise on this family

Use the complete distinguishing D8 operators, not only primitive loops. Their supports are:

* horizontal/vertical straight triomino: span two in one coordinate and zero in the other;
* box and L triomino: spans at most one in each coordinate;
* diagonal PP: spans one in each coordinate.

Because distinct motif syndromes are separated by at least two in the relevant coordinate, a box, L, or diagonal-PP support cannot meet two different motifs at all. These terms are exactly additive on A.

Only straight triominoes can bridge two motifs. For horizontal coarse neighbors there are exactly two bridging horizontal triominoes, one on each of their common bad-plaquette rows. Each meets one bad plaquette from each motif, with the intervening plaquette good. For vertical coarse neighbors there are exactly two analogous vertical triominoes, one at each common bad x coordinate. A diagonal or more distant coarse pair cannot be bridged by any retained support.

No retained support can meet three motifs: a straight span-two support meets at most the two closest motifs, and all other supports meet at most one. Therefore there is NO hidden three-body term in this order-eight restriction, even for an arbitrary large but finite subset with many neighboring cells.

A bridging straight product has coefficient -c, c=9/262144 per longitudinal layer. Its value is +1 in the vacuum, -1 with either individual motif, and +1 with both. The connected contrast is therefore 4*(-c)=-4c per bridge. With two bridges per coarse nearest-neighbor pair it is -8c=-9/32768. Hence exactly

    E8(A)-|A| E8(single)
       = - J v lambda^8 * edges(A),
    v=9L/32768,

where edges(A) counts unordered nearest-neighbor edges of the coarse square lattice.

The derivation also explains why the six-turn-loop and touching-square coefficients, although indispensable in general D8 shape competition, do not generate extra interactions on this particular spacing.

## Independent finite control

`/tmp/aggregation_check.py` constructs the physical column syndromes and evaluates all straight, box, four L, and two diagonal-PP supports with exact rational coefficients. It verifies the identity for every one of the 512 subsets of a 3 by 3 coarse array. Pair offsets (1,0),(0,1) give -9/32768 per layer; (1,1),(2,0),(0,2) give zero. This is an independent control of the analytic support proof, not a substitute for its arbitrary-subset argument.

## Square family and microscopic meaning

An m by m occupied coarse square has n=m^2 motifs and exactly 2m(m-1)=2n-2sqrt(n) coarse edges. Its order-eight binding contrast is therefore

    -J v lambda^8 (2n-2sqrt(n)).

Per motif this is -2Jv lambda^8(1-1/m), decreasing along the square family. The absolute excitation expectation remains positive at weak coupling, with leading term n J Delta lambda^4; common lower-order single-feature corrections are not to be discarded when quoting an absolute energy.

For each FIXED finite n and geometry, the diagonal calculation can be realized as a normal-form-dressed trial state in the native Hilbert space, and finite-order transfer gives its variational energy with higher-order corrections. The first winding term is order lambda^10 and is offdiagonal between distinct finite configurations; it does not change the order-eight diagonal identity. Other higher-order diagonal, mixing, and relaxation effects remain present. Comparison to n isolated relaxed features has the same leading order-eight contrast, subject to the already controlled single-feature energy expansion.

The per-feature monotonicity is an order-eight or fixed-family weak-coupling statement. At any fixed nonzero lambda it is NOT uniform for arbitrarily increasing m: the leading difference between consecutive square sizes shrinks and higher-order constants may grow with n. Nor does the variational upper bound establish an isolated eigenstate, a stable aggregate, absence of decay into other shapes, or an optimal macroscopic phase. No coarse kinetic rule or nearest-neighbor model has been adopted as an exact replacement for H. The result is a derived attractive diagonal contribution on a specified family of prepared native configurations.
