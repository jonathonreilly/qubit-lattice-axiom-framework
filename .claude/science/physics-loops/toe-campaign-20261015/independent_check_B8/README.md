> Review status: the original report below is preserved as an unadopted proof
> candidate. Independent review matched the exact families and equations but
> did not certify exhaustive minimal-prime coverage. Historical exact-proof
> language below is not a current review verdict or adopted no-go.

# Independent check: no nearest-site staggered tick propagates (B6 Theorem 3)

A fresh agent context was given only the problem statement. Its verdict: no
such walk propagates, proved exactly over Q.

- **Model.** Exact covariant nearest-site family with 11 complex parameters.
  It was built for both inequivalent signed binary-octahedral classes, up to
  +-1 diagonal gauge (`setup.py`, `gaugecheck.py`).
- **Equations.** Unitarity gives 79 polynomials over Q in c and cb, with cb
  treated as independent.
- **Components.** Singular minAssGTZ gives 8 minimal primes for each class,
  of dimensions 4,4,2,2,2,2,4,4 (`sing0.log`, `sing1.log`).
- **Flatness, the decisive check.** On every prime, tr (z1 z2 z3 W)^p
  reduced modulo the prime is a multiple of (z1 z2 z3)^p for p = 1..8. So the
  characteristic polynomial is k-independent on the whole complex variety,
  with no real-point argument needed (`model*_flat_allprimes.sing`,
  `flatall*.log`).
- **Control.** For the zero ideal the test reports k-dependence at p = 2
  (`control_flat.sing`).
- **Numerical.** Searches found 81/150 and 91/150 unitary solutions, all
  flat (`numsearch.py`, `num*.log`).

Limit of independence: the checker is the same model family in a new
context, and the exact step rests on one CAS (Singular).
