# EXTCONT finite checks — criteria registered before the checker

These are exact finite algebra/geometry regressions, not evidence for an
unproved Yang–Mills estimate. Written proof development preceded this file.
No numerical result or tuned acceptance threshold is recorded here.

1. On path6, cycle6 and the 2-by-3 rectangular grid, enumerate all active
   masks and all nonempty connected input supports. Component saturation
   must equal iterative addition of adjacent inactive vertices. It must
   preserve the input active vertices and add no vertex outside the input
   plus the touching inactive components. Equality tolerance: zero.
2. Set exp(mu)=2 and exp(-tau)=1/4. Give each support the rational activity
   1/(1+its binary mask), multiply it by 4^(-S_X), where S_X is the total
   size of inactive components meeting or adjacent to X, and saturate its
   support. At every active mask, the full-root/full-size output norm,
   including unchanged inactive activities, must be at most (11/2) times
   the original norm. Check also each single-support input. This uses
   sup_(m>=1) m/2^m=1/2 and the degree-eight bound, not a fitted constant.
   All arithmetic is rational; inequality tolerance: zero.
3. The shared norm implementation must give 2,16,2 for the input full,
   saturated full and active output norms of one unit singleton on cycle4
   with that singleton the only active vertex. On path3 with endpoints
   active and unit singleton inputs at both ends, its input and output
   full norms must be 2 and 8, with inactive middle root sum 8. Actual
   in-memory mutations replacing full weights by active weights, and
   deleting inactive roots, must each be rejected by these witnesses.
4. For monomials z^r J^c, 0<=r<=10, 0<=c<=4, and L=3,5, the degree-two
   Taylor projection must be idempotent, annihilate the first three field
   coefficients of the remainder, and commute with the included source
   derivatives. For r>=3, L^4 F(L^-2 z,J) has coefficient L^(4-2r)<=L^-2.
   Use exact rational arithmetic. A coefficient-scaling mutation using
   field dimension one must be rejected at r=3.
5. Derivatives of exp(H) and its reciprocal through order ten: independent
   set-partition counting and the binomial reciprocal recurrence must
   agree exactly, as polynomials in a nonnegative score bound B. At orders
   zero through four recover REALRGB's M,I,C polynomials, including
   C_4=2B+42B^2+156B^3+150B^4. At B=0 every positive-order bound must vanish.
6. In the scalar finite-jet norm on [-1,1], the sixth-derivative term of
   f_n(z)=n^(-6) sin(nz) is 1/6!, whereas its values tend to zero. For
   n=2,4,8 verify the exact coefficient ratio n^6. This is a scaling
   diagnostic, not evaluation of trigonometric functions or an actual
   RG counterexample. A moving-selector example is proved in the note,
   not inferred from this check.

Resource requirements: one sequential process, no pools, nice >=10,
OPENBLAS/MKL/OMP/VECLIB/NUMEXPR/BLIS thread variables all 1, maximum of the
three load averages <8, system-wide free memory >=30%, and RSS <1,000,000,000
bytes. Check before, between, and after groups. Use resource.getrusage;
never set RLIMIT_AS. Acquire the lane numeric lock atomically. A failed
guard means NOT_RUN or STOPPED with the completed checks retained; never
weaken the guard. Any failed mathematical criterion remains FAIL.
