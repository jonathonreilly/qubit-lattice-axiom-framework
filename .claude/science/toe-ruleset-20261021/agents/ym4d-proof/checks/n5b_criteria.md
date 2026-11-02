# N5B numerical criteria

Written before the check script or its execution. These are finite exact
probability checks, not Yang–Mills estimates. Balaban and Dimock are credited
for the constructive RG methods discussed in the source packet; no literature
result supplies any check premise.

1. **C1, covariance at an intermediate cut.** On a strictly positive
   four-level, three-state Markov chain, direct enumeration must equal the
   telescoping sum of expected one-step conditional covariances plus the
   covariance of the two conditional images, at each of cuts 1, 2 and 3.
   All equalities use exact rational arithmetic. The terminal Cauchy bound,
   squared, must hold with the optimal single constant for the seam image.
   At least one terminal covariance must be nonzero.
2. **X1, missing terminal term.** Omitting that nonzero terminal covariance
   must fail equality. **X2, non-Markov tower.** For independent uniform
   signs X,Y, U0=X, U1=Y, U2=X, the asserted reverse tower through U1 must
   fail. Neither control is a Yang–Mills counterexample.
3. **C2, conditional decay versus total covariance.** For independent
   uniform signs X,E,H, let F=X+E and S=X+H/3. Given X, the covariance must
   equal zero at both values; the unconditional covariance must equal 1.
   **X3, field-dependent centering.** Substituting c(X)=E[S|X] for a single
   constant must falsely predict zero and must be detected.
4. **C3, rare-event amplitude budget.** For n=2,4,8,16,32 and a Bernoulli
   variable B of probability 1/n², take F=nB. With S=nB the covariance
   must equal 1−1/n² and be at least 3/4 despite decreasing P(B=1). With
   S=B it must equal (1−1/n²)/n and be at most 1/n. In both cases the
   squared covariance must obey Var(F)·E[S²1_{B=1}]. This checks the
   amplitude-weighted tail bound, and rejects probability-only inference.
5. A mathematical PASS requires every C criterion and every X detection.
   A failed criterion is a failure, not a changed threshold; process exit
   must be nonzero on failure. No simulated continuum limit, measured
   exponent, or numerical evidence for N5 on K_a will be claimed.
6. One process, no pools, nice priority at least 10, BLAS/OMP/MKL/OpenBLAS/
   vecLib/NumExpr thread settings all 1. Acquire a lock named
   checks/n5b_numeric.lock before computation. Require 1-minute load <8
   and memory_pressure free memory >=30%. Abort if RSS reaches
   1,000,000,000 bytes or runtime reaches 60 seconds. A denied nice change
   or failed resource guard means NOT RUN, never permission to weaken it.
