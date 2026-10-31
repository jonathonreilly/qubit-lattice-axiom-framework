# REFMATCH numerical criteria (registered before the runner)

These finite diagnostics do not prove the infinite-family comparison or
the actual-model induction. All failures must be reported, without changing
these thresholds after observing them.

1. On three independent signs with affine means m1=1/5+y/8,
   m2=-1/7+y/9, m3=1/6-y/10, and background factors
   (1+a x1 x2)(1+b x2 x3), a=1/32+y/64, b=1/48-y/96, compare the
   normalized probability x1=+1 obtained by exhaustive eight-state summation
   with elimination of x2,x3 first. Taylor coefficients through order four
   at y=0 must agree exactly in rational arithmetic. Freezing the denominator
   at y=0 must change at least one positive-order coefficient. This is an
   actual omission mutation of the quotient calculation.
2. For SU(2), L=3, kappa=1 and u in {2,8,32}, compute the derivatives
   through order four of m(s) from its three original contour phases and
   insert the independently derived Haar second/fourth moments. Compare the
   second and fourth log-normalizer derivatives with 3u/8 and
   -81/16-9u^2/64. Relative/absolute error must be <=1e-10 times
   max(1,abs(expected)). This is a finite analytic-formula regression,
   not an independent Haar quadrature or proof for all u.
3. Construct the positive log/reciprocal/density score polynomials through
   order six by set partitions and independently by the reciprocal and
   moment recurrences. All coefficients must agree exactly; the four
   displayed density polynomials must agree exactly with the note.

Resources: exclusive nonblocking advisory lock, no pools; nice >=10;
OMP, OPENBLAS, MKL, VECLIB, NUMEXPR and BLIS thread counts all one;
maximum available load average <8; available memory >=30%; process peak
RSS <1,000,000,000 bytes. Recheck before each diagnostic and at exit.
Do not use RLIMIT_AS. If nice or any other guard is unavailable or fails,
perform no subsequent mathematical computation and record NOT RUN (or
PARTIAL if some checks had already run). The guard must not be bypassed.
