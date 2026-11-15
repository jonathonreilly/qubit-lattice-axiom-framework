# K4CORR numerical registration

Registration precedes creation and execution of the numerical checker.
Only exact rational polynomial/interval checks are registered. None evaluates
an interacting Yang--Mills integral or certifies a Yang--Mills remainder.

1. **Coupling units.** With `g_std=sqrt(2N) h`, the coefficient of
   `-h^3` is `2N b0_std`; the slope of `u=h^-2` is twice that
   coefficient. After removing the displayed powers of pi, the respective
   coefficients are `11 N^2/24` and `11 N^2/12`. A missing factor of
   two must fail the comparison.
2. **Action-density RG algebra.** For formal
   `beta_h=-b0 h^3-b1 h^5-b2 h^7`, differentiate independently in h
   and in u. With `D e_R=-gamma_e e_R`, both routes must give
   `gamma_e=beta_h'-3 beta_h/h=-2 b1 h^4-4 b2 h^6`.
   The canonical `F_can^2` convention must instead give
   `beta_h'-beta_h/h=-2 b0 h^2-4 b1 h^4-6 b2 h^6`.
   Substituting the canonical result for the clover result must be detected.
3. **Ward factor.** For `H=-beta_h/(b0 h^3)`, the polynomial identity
   `beta_h H'=gamma_e H` must hold through the represented orders.
   Multiplying a four-point function by H^4 and a two-point function
   by H^2 must leave their normalized ratio unchanged. A denominator
   with only one H factor must fail.
4. **Common logarithms and finite factors.** In the separated action-density
   RG equation the relative first-order log coefficients must be `8 b0`
   for the fourth cumulant and `4 b0` for the covariance. Their ratio
   log coefficient is exactly zero. A common finite operator factor and
   a near-identity coupling change must not change the first coefficient
   of the ratio. Reversing a log sign or omitting the square of the
   denominator must fail. If that ratio coefficient is c, its next-order
   scale-log coefficient must be `2 b0 c`.
5. **Free denominator and positivity certificate.** The CUMUL rational
   support enclosures must imply `3/2<A<5/3`, `11<B0<13` and
   `3/(338d)<R0<5/(363d)`. Relative errors of magnitude at most 1/4
   must give the exact ratio interval `[12/25,20/9]`, and the lower
   witness bound `18/(4225d)`. The certificate must accept both signs
   of the first correction and must reject the claim that these bounds
   hold without a bound on the remainder.
6. **Reciprocal running bound.** If `u=Bm+v`, `B,m>0` and
   `|v|<=E<=Bm/2`, the reciprocal error is bounded by
   `2E/(B^2 m^2)`. Verify the denominator inequality and both signs by
   exact polynomial/rational arithmetic; the bound with the factor two
   removed must have an exact counterexample. This checks the rate
   implication only, not the hypotheses on the actual trajectory.

Every assertion must pass exactly; no floating-point tolerance, Monte Carlo,
or fitted parameter is permitted. Mutation controls pass only when their
specified false assertion is rejected. A failed assertion is recorded as a
failure, not reclassified as a successful Yang--Mills check.

Resource conditions: one serial numerical child, no pools; exclusive locks
on the existing lane numerical locks without modifying them, plus a new
`k4corr_` lock; nice at least 10; all five BLAS/OpenMP library thread limits
one; combined monitored RSS below 800 MiB (strictly below 1 GB); all three
load averages below 8; native available/free-memory report at least 30%.
Failure of a resource condition stops the run. No weakened fallback is
registered.
