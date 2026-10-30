# K4MATCH numerical registration

Registered before creating or executing the check implementation. These are
finite algebra checks, not measurements of a Yang–Mills Schwinger function.
All scientific decisions use integers or `fractions.Fraction`; no fitted
coefficient, floating-point sign decision, quadrature or stochastic sampling.

1. Recompute the collinear free coefficient from the three cycle weights
   `1/81, 1/256, 1/20736`: require `96 sum = 169/108`, two-point
   coefficient `12`, and ratio `169/15552` for one colour. Check the
   printed support bounds inside `(3/2,5/3)` and `(11,13)` exactly.
2. Enumerate partitions of four distinct labels: require counts
   `4:1, 3+1:4, 2+2:3, 2+1+1:6, 1+1+1+1:1`.
   Verify the law of total cumulance on an explicit finite rational
   probability table, by comparing unconditional moments with conditional
   cumulants and outer cumulants. Removing the `2+2` family must fail on
   the Gaussian variance mixture `T=1 or 3`, each with probability `1/2`:
   require its fourth cumulant `3` although every conditional fourth
   cumulant is zero.
3. On `P(x)=2^-4(1+t x1 x2 x3 x4)`, `x_i in {-1,1}`,
   for `t=-1/2,0,1/2`, require all proper-subset mixed moments equal,
   and the fourth cumulant equal to `t`. This is an information-content
   check, not a Yang–Mills counterexample.
4. For three fixed rational symmetric covariance slices and four fixed
   diagonal insertion matrices, verify that the fourth Gaussian cycle
   polynomial telescopes over tails. Direct allocation of all `3^4`
   edge-scale assignments by their minimum index must agree at each
   level. A same-slice-only replacement must disagree with the full sum.
5. Verify the formal order-`h^2` cumulant formula by two algorithms:
   expand normalized Gaussian polynomial moments and then cumulants;
   independently sum the five families of free cumulants with observable
   and action insertions. Use nonzero odd cubic and even quartic
   perturbations, and check orders two and four. The order-`h` coefficient
   must vanish. These polynomial data are controls for combinatorics,
   not lattice Yang–Mills vertex data.
6. Check exact cancellation of a common multiplicative field change
   in `K4/B^2` through order `h^2`. For the running-factor model
   `(1+x)^-4 / ((1+x)^-2)^2`, require ratio exactly one; its first
   numerator and denominator coefficients are `-4` and `-2`.
7. With relative numerator/denominator errors in `[-1/4,1/4]`,
   require the endpoint lower ratio `12/25` and hence the smooth-test
   lower bound `18/(4225 d)`. Verify the corresponding rational upper
   bound and the stated ratio-error inequality on the fixed grid
   `{-1/4,-1/8,0,1/8,1/4}^2`.
8. Verify the sixteen-term four-support projection on formal monomials:
   it kills every proper-subset monomial, and retains `t1 t2 t3 t4`
   with coefficient one, not `4!`.

Pass requires every registered equality/inequality and every specified
mutation control. Record a failure without relaxing a threshold. No
finite check can pass the separate open requirements of a uniform
renormalized YM coefficient, its sign, or its all-history remainder.

Execution: one serial process, no pools, exclusive numeric lock, nice
at least 10, OPENBLAS/OMP/MKL/VECLIB/NUMEXPR thread counts all one,
native `memory_pressure -Q` free percentage at least 30, all reported
load averages below 8, RSS below 800 MiB (stricter than 1 GB), and
elapsed time below 90 seconds. Guard failure is reported, not bypassed.
No writes outside `K4MATCH.md`, `K4MATCH_LOG.md`, `checks/k4match_*`.
