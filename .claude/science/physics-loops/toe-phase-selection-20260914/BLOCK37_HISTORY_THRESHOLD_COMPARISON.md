# Block 37 — finite temporal fillings compare history thresholds

Personal affirmative proof proposal,2026-09-15. This addresses the additional
history-subspace question left explicitly open in Block36. It does not alter
any axiom or assert a new matter sector. Fixed finite N,beta>0 throughout.

## 1. The elementary positive current comparison

On any finite free clock cell complex, expand every plaquette Villain weight
in its discrete Fourier series with coefficients c_k>0. Integration/summation
over the link clocks gives

 W(J)=Z_J/Z_0,
 Z_J=sum_(d1* s=J modN) product_p c_(s_p).              (1)

Orientation may replace J with -J and leaves W unchanged. All summands are
nonnegative. If J-K=d1*S for a finite integer plaquette chain S, shift the
summation variable s by S. With

 R(S)=product_p max_k c_k/c_(k+S_p),

strict positivity and coefficient evenness give

 R(S)^(-1) W(K)<=W(J)<=R(S) W(K).                      (2)

The fiber bijection also covers absent fibers: both sums then vanish. For a
nonempty contractible free cube and a finite conserved current, a finite
integer filling makes its fiber nonempty. The constants only use plaquettes
in S and are independent of the surrounding box. Infinite matched free-state
limits therefore preserve(2). This is a positive expansion of the original
clock weight, not a positive expansion of its logarithm or square root.

## 2. A history differs from a static reference only at its two ends

Use a word from Block36 in chronological order, with spatial insertions
j_1,...,j_m at integer times0<=t_1<=...<=t_m<=L. Put j_total=sum_i j_i
and rho=d0*j_total. Its diagonal transfer moment

 F_w(n)=<w,S^n w>, n>=0,

is the closed-current expectation on a temporal interval of length2L+n:
one insertion history near the left end, its reflection/conjugate near the
right end, and the fixed temporal charge rho between them. The reference
W_(j_total)(2L+n) places the total spatial current at each outer end.

Move each left spatial insertion j_i from time0 to t_i. The required filling
is the temporal strip j_i times the interval[0,t_i], with orientation fixed by
the boundary formula for a product chain. Its side boundary is exactly the
change of cumulative temporal charge. Summing these strips gives an explicit
finite integer temporal-plaquette chain S_w whose boundary is the difference
of the left endpoint currents. Reflect it for the other end. No existence-only
homology argument, spatial filling or large-beta source estimate is needed.
Overlapping strips are added algebraically. Even if the two reflected fillings
touch, the local ratio bound for their sum is bounded by the product of their
separate ratio bounds, by applying the shift twice.

Consequently

 R(S_w)^(-2) W_(j_total)(2L+n)
 <=F_w(n)<=R(S_w)^2 W_(j_total)(2L+n).                  (3)

The constant is finite for each fixed history, independent of n and spatial
volume. One convenient upper bound on R(S_w) is the product over each unit
time interval of K(j_total-j_past), where j_past is the sum of insertions
already made by that interval. This is the final-current strip filling, not
a claim that histories with the same final charge have equal finite-time
amplitudes. If no time interval is present, it reduces to the static insertion.

## 3. Equality on the full history sector

The static reference is strictly positive and has finite rate E_rho by
Blocks32-35. Its fixed shift in time2L does not change this rate. The fixed
multiplicative comparison(3) therefore gives

 -lim_(n to infinity) log F_w(n)/n=E_rho

for EVERY history word of charge rho. In particular every such word has
nonzero norm. Each word's spectral measure for the history Hamiltonian has
bottom E_rho. The spectral projection below E_rho kills all generating words
of that charge, hence their dense span. Since each word has spectral support
arbitrarily close to E_rho, the full charge-sector spectral bottom is E_rho.

This closes the larger-space bottom question from Block36 within its
specified history reconstruction. It does not prove time-zero cyclicity and
does not identify arbitrary other infinite-volume representations. The earlier
Coulomb-form upper bound consequently holds in this full history sector under
the source's stated large-beta curvature assumptions. The local gauge charge
profile is still preserved by the transfer operator; mobile matter is not
created by this reconstruction.

## Verification target and limits

Check equation(3) against actual finite transfer words and independently
computed Fourier strip coefficients, including histories with intermediate
charges different from rho and a terminal zero insertion. Reject omission of
the endpoint constants and of the2L reference-time shift using actual values.
The finite probes cannot certify the general cofinal state passage. This is
an author proof proposal awaiting independent source review, with no universal
no-go, independent wall count or axiom-update claim.

Executed evidence:108actual history comparisons on N=2,3,4; exact integer
endpoint-chain boundary checks; direct link enumeration versus plaquette-current
fibers on two full cubes (4096and531441link assignments). Maximum direct/fiber
discrepancy4.05e-14. Omitted constants and time shifts change actual values.
These checks were personal and supply no independent-review verdict.
