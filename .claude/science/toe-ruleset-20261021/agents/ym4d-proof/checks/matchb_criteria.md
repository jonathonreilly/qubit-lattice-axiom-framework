# MATCHB numerical criteria — registered before implementation

These finite rational diagnostics test the algebra of the proposed
interacting-reference comparison. They do not test the all-history SU(N)
bounds or prove regeneration of their constants. No tolerance is used:
all displayed identities must agree exactly in rational arithmetic.

1. For four signs x0,...,x3 with probability
   `2^-4 product_(i=0)^2 (1+t x_i x_(i+1))`, t=1/2, verify normalization,
   zero one-point means and `E[x0 x3]=1/8`. For g0=x0/8 and g3=x3/8,
   the difference from separate expectation factorization must be 1/512.
   The incorrect product-of-marginals calculation must be rejected.
2. In the same chain take t(y)=1/2+y/13 and multiply by
   `(1+a(y)x0)(1+b(y)x3)`, a(y)=1/5+y/7, b(y)=1/6-y/11.
   Compare the x0=+1 probability obtained by full summation and by
   the conditional-marginal ratio with `Z=1+a b t^3`, through degree four
   in y. Coefficients must agree exactly. Freezing Z at zero and,
   separately, freezing the inherited law's t at zero must each change
   at least one coefficient of positive degree. These are actual omission
   mutations of the same probability calculation.
3. For the four-sign chain at t=1/2 and g_i=x_i/10, construct every
   joint cumulant by the set-partition formula. Sum the gas of cumulant
   types compatible exactly when their atom-label sets are disjoint.
   It must equal the direct expectation of product_i(1+g_i).
   Keeping only singleton cumulants must give a different answer.
4. For three hidden signs z1,z2,z3 with chain parameter t=1/2 and
   conditionally independent observations with
   `P(x_i|z_i)=(1+s x_i z_i)/2`, s=2/3, sum all 64 joint states.
   The conditional covariance of x1 and x3 given x2=+1 must be 5/81,
   not zero. The determinant of the unnormalized endpoint matrix with
   x2=+1 must equal `s^2 t^2 (1-s^2)/16` and be strictly positive.
   This tests a finite-range-Markov regeneration inference on this
   finite sign model only, not a gauge-model counterexample.

Resource conditions: one nonblocking exclusive advisory lock, no pools,
observed nice >=10, OMP/OPENBLAS/MKL/VECLIB/NUMEXPR/BLIS threads all one,
every measured load average <8, available and system-free memory >=30%,
peak process RSS <1,000,000,000 bytes. Check before each diagnostic and
at exit. Never use RLIMIT_AS. If any condition cannot be verified or
fails, stop mathematical execution and record NOT RUN, or PARTIAL if
some diagnostics ran. Preserve a failed mathematical assertion as FAIL.
