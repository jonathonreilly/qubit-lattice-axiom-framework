# CUMUL numerical criteria — registered before implementation

2026-10-30 UTC. This file precedes `cumul_exact.py` and its first run.
These are finite exact checks, not numerical evidence for interacting YM.
Written derivations need no pre-registration under PROCESS_LIGHT.

## Conventions and fixed tests

Four-dimensional Euclidean space, six unordered two-form components,
`d=N^2-1` colours, `e=(1/u) sum_(a,I) :F_I^a F_I^a:`.
Strip `pi^-2` from each coupling-one curvature covariance. The centres
are `(-3/2,0,0,0),(-1/2,0,0,0),(1/2,0,0,0),(3/2,0,0,0)`.
The four test supports are cubes of coordinate half-width `epsilon=1/10000`
about these centres. Each test is a nonnegative smooth unit-integral bump;
reflection exchanges 1 with 4 and 2 with 3. No fitted test geometry.

## Statements and thresholds

1. **Gaussian comparator:** formal raw moments with independent symbols
   for arbitrary means and every covariance entry have cumulants 3 and 4
   identically zero. An affine Gaussian with zero covariance is included.
2. **Curvature normalization:** the differentiated scalar Green function
   and the exterior-square reflection formula agree exactly at the rational
   vectors `(1,0,0,0)`, `(1,2,3,4)`, `(2,-1,0,3)`. At each vector the
   squared Frobenius norm is `6/|x|^8`, and the Hodge-star anticommutator
   is zero. These samples check implementation, not the universal proof.
3. **Quadratic Gaussian contractions:** direct pairings of two labelled
   legs at each vertex give 2 connected pairings for n=2, 8 for n=3,
   and 48 for n=4 (16 for each undirected four-cycle). Direct component
   contraction agrees with the independently coded matrix-cycle formula.
4. **Three-point route:** the four-dimensional scalar `F^2` three-point
   coefficient is exactly zero, both for the first three collinear centres
   and at `(0,0,0,0),(1,0,0,0),(0,1,1,0)`. The requested nonzero n=3
   free leading term is therefore a rejected candidate, not a YM result.
5. **Exact four-point coefficient:** at the four centres,
   `pi^8 u^4 S4^T/d = 169/108` and `pi^4 u^2 S2^T(2,3)/d = 12`.
   Their dimensionless quotient is `169/(15552 d)`.
6. **Separated smooth-test certificate:** outward rational interval
   arithmetic on the entire product of the four cubes must certify
   `3/2 < pi^8 u^4 S4^T(f1,f2,f3,f4)/d < 5/3`, and
   `11 < pi^4 u^2 S2^T(f2,f3)/d < 13`, for every choice of the stated
   nonnegative normalized bumps. No quadrature and no floating-point
   sign decision. Consequently `3/(338 d) < R4 < 5/(363 d)`.
7. **Discriminating controls:** omitting a four-cycle or changing its
   factor 16 to 8 must fail the independent Wick-pairing comparison.
   Omitting one Gaussian disconnected subtraction must produce a
   nonzero formal polynomial and fail Gaussian-nullity.
8. **Rescaling:** under `e -> a e + b`, n>=2 cumulants scale by `a^n`;
   check the finite formal centring identities and the fourth-to-second
   ratio for `a=-3/2,2/3`. The ratio is asserted only for a nonzero
   denominator; Gaussian zero-covariance cases use the polynomial witness.

## Execution and failure policy

One serial process; no worker pools. Exclusive `cumul_numeric.lock`;
nice >=10; OPENBLAS, OMP, MKL, VECLIB and NUMEXPR threads all set to one.
Require load1 <8 and native macOS free-memory percentage >=30 before
and during the run. A watchdog stops combined runner/child RSS above
800 MiB (below 1 GB); record peak RSS, load and memory. Wall limit 90 s.
If nice or any guard fails, report the failure; do not relax it.

Fractions and rational intervals carry all load-bearing values. Resource
measurements may be floating point. Preserve a failed run as failed;
any new numerical probe or criterion must be labelled post-hoc. These
checks cannot prove AF, matching, moment convergence or YM existence.
