# A standard r=1 Wilson Fourier-sign witness on a full four-dimensional box

Author-proposed exact counterexample to positive Fourier type, not a no-go
for a phase or a different positive representation. This strengthens the
block2 r=2 witness: r=1 was explicitly left unresolved in that milestone.

Take the full open box {0,1}^4, all 32 nearest-neighbor links, four spin
components per vertex, and Wilson r=t0=1. For positive direction mu the
hopping block is -P_mu,- exp(i theta_l), for negative direction it is
-P_mu,+ exp(-i theta_l), with P_mu,+/-=(I+/-gamma_mu)/2. The four Hermitian
Euclidean gamma matrices are

    gamma_1,2,3 = sigma_1 tensor sigma_1,2,3,
    gamma_4 = sigma_2 tensor I.

Set D=M I+K, W=|det(I+K/M)|^2, M>8. This is within the block2 absolute
hopping domain. Write w_j(M) for the Fourier coefficient of W at the
integer edge current j.

## 1. The simple cycle and its exact spin trace

Starting at (1,1,0,1), traverse the direction word

    (-1,-4,+3,-2,-3,+1,+2,+3,+4,-3).

All ten visited vertices before closure are distinct and belong to {0,1}^4.
Let j put unit oriented flow on this cycle and zero on the other edges.
Then G^*j=0 and ||j||_1=10. There is no proper nonempty closed subcurrent
made from a subset of its oriented edges: each cycle vertex has exactly one
incoming and one outgoing selected edge, so following any selected edge
forces the whole cycle.

For a signed direction a put P_a=(I-sign(a)*gamma_|a|)/2. Direct exact
Clifford multiplication along the displayed word gives

    tr P_cycle=1/32,
    det(z I-P_cycle)=z^2(z^2-z/32+1/1024).

The runner checks the trace by both explicit matrices with exact rational
complex entries and a separate bit-mask Clifford-algebra multiplication.
The characteristic polynomial and cycle closure are additional checks.

## 2. Leading Fourier coefficient, including the fermion-loop sign

Expand W in lambda=1/M. A degree-r term contains exactly r hopping factors
across the two determinants. Its net edge current has l1 norm at most r.
Therefore the j coefficient is zero through degree 9.

At degree 10, attaining ||j||_1=10 leaves no reversed or off-cycle hop and
no cancellation between determinants. Gauge invariance requires each
nonconstant determinant cycle to be an integer closed subcurrent of j.
The simple-cycle property forces all ten hops into one determinant cycle
in one of the two factors. Equivalently, in

    log det(I+lambda K)=sum_{n>=1} (-1)^(n+1)
                                      lambda^n tr(K^n)/n,

the selected oriented loop has ten possible roots. Their factor ten cancels
1/n. The sign is negative at even n=10, while the ten minus signs in the
Wilson hoppings multiply to positive. Thus its coefficient in one log
determinant is -tr P_cycle=-1/32. Products of shorter closed currents cannot
supply j at the same degree, so exponentiation does not alter that leading
coefficient. The adjoint determinant contributes the reversed adjoint loop,
with the same real trace: gamma_5 conjugates every P_a to P_-a. Hence

    w_j(M)=-1/(16 M^10)+higher powers of M^-1.

This is a full-box coefficient statement: the other 22 links are present,
but cannot enter that minimum-degree Fourier coefficient.

## 3. A full-polynomial remainder certificate

The full matrix has dimension Dsize=64. Each axial hopping operator is a
compression of -[P_mu,- U_mu+P_mu,+ U_mu^*], whose norm is one because the
spin projectors are orthogonal and U_mu is unitary. Consequently ||K||<=4
uniformly in all link phases. A principal minor of order r has determinant
at most 4^r in absolute value, so the coefficient of lambda^r in either
determinant is bounded by binom(64,r)4^r. Multiplication and Vandermonde's
identity give the pointwise bound binom(128,r)4^r for the degree-r coefficient
of W. Its individual Fourier coefficient obeys the same bound by integration.
Thus

    |w_j(M)+1/(16 M^10)|
      <= sum_{r=11}^{128} binom(128,r)(4/M)^r
      <= binom(128,11)(4/M)^11 / (1-39/M),    M>39.

The final ratio bound is exact: for r>=11 the next/previous summand ratio
is 4(128-r)/[(r+1)M]<=39/M. With the explicit, deliberately conservative
choice M=2^100, dividing the remainder by the leading magnitude gives

    16 binom(128,11)4^11/(M-39) < 1.

Every quantity in this last inequality is an integer or rational number.
The bound is in fact strictly below one for every real M>39+16*binom(128,11)*4^11. Therefore Re w_j(M)<0 for this concrete full r=1 Wilson model. It is not
of positive Fourier type. No numerical subtraction of M^-10 terms is used
in the full-box certificate. The very large mass is an existence witness;
no useful physical threshold, sharp mass range, or empirical parameter is
claimed.

## 4. Scope and independent check limit

The cycle-only graph is also checked separately: its transfer product gives
an exact determinant as the product of det(I-lambda^10 z P_cycle) and the
reverse-loop factor. Direct full 40-by-40 determinants at several phases
agree with that formula. This challenges the loop sign and normalization
through a separate determinant calculation. The full-box remainder proof is
analytic and rational; the cycle-only numerical test does not replace it.

This result closes only the previously untested r=1 positive-Fourier-type
hypothesis. Pointwise W>0 persists, the physical Villain measure is positive,
and neither a signed local expansion nor another positive representation is
ruled out. In particular it does not establish that any charged Coulomb phase
fails, and it creates no contradiction with the framework axioms.
