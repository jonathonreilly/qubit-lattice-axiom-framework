# The mean-current scope of a collinear four-site read footprint

Primary classification argument, 2026-09-21; the separate pre-source reconstruction agrees.
This is a bounded statement about a specified read footprint and stationary
product class. It is not a restriction on larger contexts, non-product
stationary laws, or all immutable-record physics. The six-site construction
in `POLYNOMIAL_FLUX_REALIZATION_DERIVATION.md` is an explicit route beyond
this footprint.

The independent report under `independent_polynomial_flux/REPORT.md` was
read in full together with its checker; all 12 artifacts and six dependencies
were hash-verified. Report SHA
`94d8ffa8681f9fbc605bd6ff196c495d6725e3c92fdd9013cee1b840577776e8`;
seal SHA `47f87385cccde288d7cd950cc7bd9860cf0b2379f3527ee133af2f0e75d2f174`.
It independently checks the general construction, applicability of the limit
proofs, the complete linear spectrum and nonlinear defects. This is not a
publication-source review, formal audit or retained-status verdict.

## 1. From product balance to a three-letter potential

Suppose a nearest-neighbor exchange rate reads only (l,a,b,r) at the two
endpoints and their two immediately external collinear sites. Let

`h(l,a,b,r)=c(l,a,b,r)-c(l,b,a,r)`.

It is antisymmetric under swapping a,b. Assume homogeneous full-support
products are stationary on every sufficiently large cubic torus. Since
swaps preserve a product configuration weight, stationarity is equivalent
to the pointwise sum of h over all lattice edges being zero.

Take a configuration depending only on one coordinate. Exchanges in the
other directions have identical endpoint states and hence h=0. It follows
that the line sum of the chosen direction's h is zero on every sufficiently
long periodic label string. Repeating a shorter periodic string supplies
the same conclusion for its shorter period.

Use the directed de Bruijn graph whose vertices are triples of labels and
whose edge (l,a,b,r) goes from (l,a,b) to (a,b,r). Periodic strings are its
closed walks. The graph is strongly connected and the sum of h on every
closed walk is zero. Fix a reference vertex, integrate h along paths, and
use a return path to show independence of the chosen path. Thus there is a
three-letter function G, unique up to a constant, such that

`h(l,a,b,r)=G(l,a,b)-G(a,b,r)`.                                (1)

This is a finite graph coboundary statement, not a mixing assumption.

## 2. Solving the endpoint antisymmetry condition

Antisymmetry of (1) says

`G(l,a,b)+G(l,b,a)=G(a,b,r)+G(b,a,r)`                           (2)

for every l,a,b,r. Each side must be a function T(a,b) independent of the
external label; T is symmetric. Set S(a,b)=T(a,b)/2 and define

`G_S(l,a,b)=S(l,a)-S(l,b)+S(a,b)`.

Both its last-pair and first-pair symmetrizations are T. Therefore
G-G_S changes sign under each adjacent transposition of its three arguments,
and is a completely alternating three-letter tensor A. Consequently every
such h has the form

`h(l,a,b,r)=S(l,a)-S(l,b)+S(a,r)-S(b,r)`

`             +A(l,a,b)-A(a,b,r)`,                            (3)

with S symmetric and A completely alternating. Conversely (3) is
antisymmetric and has pointwise zero periodic line sum, so it supplies the
entire class. A constant S changes neither h nor the current.

For an alphabet of q labels the dimension of this antisymmetric balanced
h space is q(q+1)/2 + binomial(q,3)-1. For q=7 it is 62. The tensor G
itself has the extra one-dimensional constant gauge. This dimension count
is a consequence of (1)-(3), not a rank extrapolation from short cycles.

## 3. The alternating part has zero product current

In a product average, the term containing A contributes zero to every
species current. Fixing either endpoint label leaves a sum over two
independent labels with a symmetric product weight and an alternating
two-slot tensor; that sum vanishes. The S part gives exactly

`J_a=2p_a[(S p)_a-p^T S p]`,                                  (4)

for every label including vacancy. Its chemical-potential potential is

`Psi(p)=p^T S p`.

Thus every rate in the stated four-site class has a quadratic polynomial
mean-current potential, whatever symmetric exchange traffic it also has.
The alternating tensor can alter dynamics and damping even though it is
invisible in these homogeneous mean currents. It cannot alter the leading
Euler current while keeping the other premises fixed.

## 4. Cubic covariance leaves three vector-potential coefficients

For the seven-label three-dimensional alphabet, let rho, g_i, q_i have their
usual meanings. Impose proper cubic covariance of the physical exchange
rule. Additive constant gauges can be fixed by taking the vector potential
to vanish at the uniform seven-state product. The resulting potential is
a cubic-covariant vector polynomial of degree at most two in the six
independent occupied probabilities.

Such a vector polynomial has precisely the form

`Psi_i=u g_i+A rho g_i+B q_i g_i`.                             (5)

One elementary way to see this is to use half-turns about the coordinate
axes. A component i can contain g_i times a constant or a linear function
of q_1,q_2,q_3, or the candidate g_j g_k for the other two axes. A quarter
turn about i changes the sign of g_j g_k while leaving the i component
unchanged, so that candidate vanishes. The same quarter turn equates the
coefficients of q_j and q_k. Axis permutations make the three surviving
coefficients common to all components. Since q_1+q_2+q_3=rho, this is (5).
The argument uses the proper cubic rotations; inversion is not an added
physical premise.

The general current spectrum already computed for (5) shows that a nonzero
pair with the same speed in every spatial direction, at every interior
isotropic composition, requires and is supplied by

`u=0`, `A+2B/3=0`, with a nonzero overall scale.

Hence its potential is proportional to

`g_i(2rho-3q_i)`,

the earlier axis-balanced construction. This identifies its mean current
within the complete stated four-site class, not just within a guessed
bilinear ansatz.

On q_i=rho/3 its finite-amplitude vector-current tensor consequently has
the -3alpha diag(g_i^2) contribution documented in
`AXIS_BALANCED_NONLINEAR_SCOPE.md`. Adding an alternating three-letter
component or changing symmetric traffic cannot remove that mean-current
term. This statement is about the specified record-moment fields and read
footprint, not every possible field identification or scaling limit.

The assumptions matter: larger read footprints, noncollinear contexts,
non-product invariant families, other update types or different field
identifications have not been classified. The polynomial realization
construction already gives a six-site cubic potential that cancels this
particular quadratic defect while leaving higher-order deviations explicit.
