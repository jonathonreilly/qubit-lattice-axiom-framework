# HOLEPAY finite-check criteria — registered before the runner

These are finite regression checks of the written combinatorics. They cannot
certify the actual all-history differentiated estimate EXTCONT E15.

1. On path6 and cycle6, enumerate every nested pair Lambda subset Omega and
   every nonempty connected input X meeting Lambda. Direct component filling
   must agree exactly with iterative inactive-neighbour growth. Require
   R_Lambda(R_Omega(X)) = R_Lambda(X), and unchanged active intersection.
2. On path6 and cycle6, for every mask, put coefficient one on every connected
   X meeting Lambda, with exact rational weight 4^(-S_X). Compute the full
   rooted input/output norms at exp(mu)=2. Require output <= 4 input,
   including inactive roots. On path3 with Lambda={0,2}, only singleton
   inputs at its endpoints, require input norm 2 and output root sums (1,2,1).
   A mutation restricting output roots to Lambda must fail that exact test.
3. In four dimensions with L=3 and floor-coordinate block projection, evolve
   the prescribed birth cohorts at levels 0,1,2 (two singleton births at
   (0,0,0,0),(12,0,0,0) at level 0; one at (1,0,0,0) at level 1; none at
   level 2). Up to level 5, direct recursive masks must equal the union of
   separately evolved cohorts and lie inside the radius-two projected birth
   cover; cardinality must be <=625 times the number of birth occurrences.
   Require two initial components and a later merger. This is a geometry
   regression, not a realization of a sampled gauge history.
4. For derivative orders 0 through 6, the Bell-polynomial coefficients used
   for exp(-Q) must agree exactly between the derivative recurrence and an
   independently enumerated set-partition construction. No target constant
   is fitted to the implementation.
5. For a four-dimensional cube of side 3, direct enumeration must give 81
   vertices and 216 external face neighbours. For side n=10, the exact
   logarithmic boundary-only norm ratio at mu=b=1 must be n^4-8n^3=2000>0.
   The infinite-family conclusion is the proof, not this finite comparison.

Use a nonblocking single-process lane lock; observed niceness >=10; all
BLAS/OMP/MKL/VECLIB/NUMEXPR thread variables set to 1; maximum load average
<8; system free-memory percentage >=30; peak RSS <1,000,000,000 bytes.
Check resources before mathematics, between sections and at completion.
No pools, RLIMIT_AS, stochastic sampling, or unguarded fallback. If a gate
cannot be verified, report NOT RUN (or INCOMPLETE if already started), retain
the actual receipts, and perform no further mathematical checks. Failures
remain failures. Any added probe must be identified as post-hoc.
