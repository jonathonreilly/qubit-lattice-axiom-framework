# The tree gain and the normalization it does not supply

Personal derivation, 2026-09-15. This checks how the new degree estimate
interacts with combinatorics. It gives an honest positive tree estimate
and identifies a divergent series of proposed diagram MAJORANTS. It does
not prove that the physical diagram series diverges, or rule out a regrouping.

## A tree sum can absorb the three-quarter degree factorial

For labelled trees on n>=2 vertices, put

    Z_n(theta)=sum_T product_i (d_i(T)!)^theta, 0<=theta<1.

In the Prufer correspondence, a vertex of degree d_i occurs d_i-1 times
in the word of length n-2. Counting words with those occurrence numbers
gives exactly

    Z_n(theta)=(n-2)! [z^(n-2)] f_theta(z)^n,
    f_theta(z)=sum_(k>=0) ((k+1)!)^theta z^k/k!.

The coefficient ratios of f are (k+2)^theta/(k+1), tending to zero.
Hence f is entire. Its nonnegative coefficients give, at z=1,

    Z_n(theta)/n! <= f_theta(1)^n/[n(n-1)].             (1)

For theta=3/4 the bound can be made elementary and explicit. The k-th
coefficient has fourth power (k+1)^3/k!. Bound its first sixteen values
upwards by rationals with denominator1000, using integer fourth-power
comparisons. The coefficient ratio from k=15 onward is at most9/16:
17^3<9^4 and the ratio decreases with k. The exact rational sum and
geometric tail give

    f_(3/4)(1) <= 79781/7000 <11.398.                  (2)

Thus the new vertex cost is compatible with an exponential tree sum WHEN
the single labelled-tree normalization 1/n! is actually available. This
is a combinatorial statement; it does not provide a physical tree expansion.

## A separately enumerated spanning cycle has already spent that factor

Fix r electric and r magnetic labelled vertices. The number of undirected
alternating Hamiltonian cycles is r!(r-1)!/2 for r>=2. Dividing by the
physical two-species labelling factor (r!)^2 leaves 1/(2r), the familiar
cycle factor. Now decorate every such cycle with one arbitrary labelled
tree on each species. These are specified cycle/forest objects; they are
not claimed to be the actual BKAR/cut expansion.

The undecorated tree counts alone give the remaining multiplicity

    r^(2r-4)/(2r).

Even restricting the added trees to paths does not fix the issue. There
are r!/2 undirected Hamiltonian paths on each set of r labels, leaving

    (r!)^2/(8r)                                       (3)

decorations after the cycle normalization. Added degrees are now at most
two and total graph degrees at most four. Consequently this problem is
not only the growth of high-degree vertex factorials.

For any fixed rho>0 and any fixed per-extra-edge cost eta>0, blindly
using one uniform loop majorant rho^(2r-2) eta^(2r-2) on all these
decorations gives terms at least

    (r!)^2/(8r) (rho eta)^(2r-2).

They do not tend to zero. The ratio of consecutive displayed terms is
r(r+1)(rho eta)^2. No matter how tiny the fixed norm constants are,
this particular series of upper bounds eventually grows. Dividing by
another (r!)^2 would change the enumerated coefficients without an identity.

There is no claim here that each actual physical contribution is bounded
BELOW by these terms. These are the values of an unsuccessful common
upper-bound prescription. Cancellations, forest-parameter integrals, an
identification that counts fewer objects, and regrouping into blocks remain
possible routes. The actual physical multiplicities and residual mixed
factors are still to be supplied. Formula (1) suggests using the tree
normalization at the level of a valid block expansion, but supplies no such
block construction by itself.

## Verification scope

The runner enumerates Prufer words and independently extracts the generating
series coefficient through n=7. It separately enumerates alternating cycles
and paths for small r, and certifies (2) by rational fourth-power inequalities.
These finite challenges supplement the exact counting proofs. They do not
execute the full physical expansion or establish an axiom obstruction.
