# MIXGFF exact-check criteria (registered before implementation)

These are prospective exact finite-algebra checks, not numerical YM evidence.
The author has already derived the displayed formulas by hand; this is an
independent implementation check, not a blind prediction. No floating-point
sign, quadrature, Monte Carlo, or infinite-dimensional conclusion is authorized.

1. For a common-centred two-component scalar Gaussian mixture, full set-partition
   cumulants must equal the covariance-of-covariances formula. Threshold: exact
   rational equality for both following abstract four-coordinate cases:
   component weights 1/3 and 2/3, covariances I+v v^T with v=(1,2,3,4)
   and v=(4,1,2,3), and common mean either (0,0,0,0) or (1,2,3,4).
2. A random affine shift taking +/-1 equally must have fourth cumulant -2;
   a variance mixture with variance values 0 and 2 equally must have fourth
   cumulant 3 at one abstract Gaussian coordinate. These finite coordinates
   are algebra controls, not repeated coincident-e tests.
3. Differentiate the massless vector covariance algebraically or implement its
   Hessian formula, separately from the exterior-square reflection formula.
   The six-by-six curvature kernels must agree at every edge of both geometries.
4. On geometry A, points (0,0), (1,0), (2,0), (3,0), the three four-cycle
   exterior-square traces must all equal 6. On geometry B, points (0,0),
   (1,0), (0,1), (2,1), traces in cycle order 1234,1243,1324 must equal
   26/5, 2, 22/5. The associated inverse fourth-power edge products must be
   1/1600, 1/64, 1/400. Threshold: exact equality.
5. For geometry B the weighted trace average must be 182/75. The free-YM
   ratio difference d*(R_A-R_B) must equal 268/675 > 0. This verifies arithmetic,
   not a YM continuum matching hypothesis.
6. Enumerate connected pairings of labelled two-legged vertices at n=3,4.
   Counts must be 8 and 48; the n=4 graph classes must each have multiplicity
   16. This is independent of the trace-log derivation in the note.
7. For the scalar quadratic matrix diag(1,-1), odd trace powers must vanish
   and even trace powers must equal 2 through degree 8. The ratio coefficient
   4 tr(A^4)/(tr(A^2))^2 must equal 2. Repeated blocks represent the stated
   p-species construction by additivity of cumulants, not a numerical limit.
8. Deliberate factor or tensor mutations (replace each curvature reflection
   by identity, drop one cycle, change the cycle multiplicity from 16 to 8)
   must each be detected by at least one relevant equality above. An undetected
   mutation is a failed control and must be reported as such.

Execution conditions: exclusive checks/mixgff_numeric.lock, nice >=10, all
BLAS/OpenMP thread counts 1, no pools, combined memory below 1 GB (use an
800 MiB ceiling), load1 <8 and native available/free memory >=30% at start and
end. Stop on any failed guard. The current sandbox rejected nice; unless that
guard becomes available, these checks remain NOT RUN and no result counts
may be reported. Exact written proofs do not depend on a prospective PASS.
