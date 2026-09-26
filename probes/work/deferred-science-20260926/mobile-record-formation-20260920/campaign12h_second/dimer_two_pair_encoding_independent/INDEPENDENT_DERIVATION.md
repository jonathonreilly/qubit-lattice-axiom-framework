# Independent finite construction and rank certificate

The complete proposed construction was read before any author checker or
results. No source correction found. All calculations are finite and exact.

Enumerating the proper signed permutations gives stabilizer sizes four for
e1 and three for (1,1,1). Multiplication by a stabilizer permutes its summands
in S=I+sum_H(Vh v)(Vh v)^T; hence S is invariant. Any two orbit transports
differ by such a stabilizer, proving independence of the chosen transporter.
The same coset argument proves covariance of the fourteen transported states.
The independent script checks all transport choices and all 336 identities.

Each S dominates I exactly because the added terms are positive outer
products. Orthogonal conjugation preserves that order, and normalization
therefore gives a strictly positive density with eigenvalues at least
1/Tr(S). Trace is positive and independent of transporter. No numerical
eigenvalue estimate is used.

The script forms the 256-by-14 integer matrix of the transported unnormalized
states. Gaussian elimination over the verified prime 65537 gives rank14.
It records fourteen original operator rows and their entire integer minor,
whose independently computed determinant is nonzero modulo the prime.
This is an exact certificate that the integer minor is nonzero over the
rationals. Dividing columns by their nonzero trace scalars preserves rank.
Since every normalized column has trace one, any linear relation is an
affine relation, and full column rank14 is equivalent to affine rank13.
The script additionally checks rank13 of normalized differences modulo
the same prime, where all traces are invertible.

The alternating character multiplicities follow directly from the 24 exact
traces: (1/24)sum a(R)Tr(V(R))=0, whereas
(1/24)sum a(R)|Tr(V(R))|^2=7. These are different representations. The
constructed cubic-weighted density operator is explicitly nonzero and
has the required alternating covariance.

The construction consequently gives an injective affine preparation map
on the complete fourteen-color probability simplex. It does not make
single labels perfectly distinguishable. Every state is full rank, so
their supports coincide and any nonzero positive measurement effect has
positive probability on each state. The exact positive pairwise trace
overlaps provide an additional finite check. Recovering a mixture by
tomography is different from reading one unknown label in one sample.

No completely positive time evolution, positive inverse preparation map,
implementation of label-conditioned rates, physical locality, record
permanence, geometry-change compatibility or formation protocol follows
from linear independence. Those remain separate obligations. The claim
is only the specified dimension16 covariant positive preparation map;
no primitive, general no-go, publication or audit status is adopted.

The first independent execution succeeded with empty stderr and no
discarded attempt. Source, exact modular minor, outputs and receipt are
preserved before author comparison.
