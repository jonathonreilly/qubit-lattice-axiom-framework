# Positive return-series refinement of the two-source certificate

The fixed first calculation remains in BLOCK12_TWO_SOURCE_RESULT.json. Its
correct affine evaluation gives alpha intervals approximately[-199.68,378.48]
and[-185.47,392.56] for the two fixed coefficient families. A first evaluator
incorrectly distributed A0,C0 across interval monomials: that conservative but
nonconforming result is retained separately with its precise failure label.
No scalar sign was certified by either calculation.

## Analytical reduction

Write X=omega²=6(1-Z), where Z=(cos k1+cos k2+cos k3)/3 has a symmetric
law on[-1,1]. The even moments are cubic random-walk return probabilities

    p_(2n)=E Z^(2n)
          =binom(2n,n) sum_(j=0)^n binom(n,j)² binom(2j,j) /36^n.

This follows by selecting the equal positive/negative steps in each of the
three coordinate directions: the numerator also equals
(2n)! sum_(a+b+c=n)1/(a!²b!²c!²). The one-sum expression follows by first
summing two of the three coordinates with the binomial convolution.

Let c_m=binom(2m,m)/4^m. Averaging the two binomial series for(1±Z)^-1/2
leaves only nonnegative even terms. Tonelli and A0<infinity give

    C0=E X^-1/2=(1/sqrt6) sum_(n>=0)c_(2n) p_(2n),
    6A0=sum_(n>=0)p_(2n).

The coefficients c_m decrease, since c_(m+1)/c_m=(2m+1)/(2m+2)<1.
For S_N=sum_(n=0)^N c_(2n)p_(2n), P_N=sum_(n=0)^N p_(2n), it follows

    S_N/sqrt6 <= C0
       <=[S_N+c_(2N+2)(6A0-P_N)]/sqrt6.                 (G.1)

This is an exact positive-series remainder bound. It does not approximate
an integral by point samples or substitute a finite-volume vacuum. Outward
rational roots enclose1/sqrt6. A negative certified tail upper refuses.

## Fixed refinement protocol, before execution

Copy the s=0 A interval from the named elliptic_RESULT.json at source revision
281dbe3fde49512baa2c4005e15985c4fbfb4cde. The supplier note and source
radical/series derivation have been read. The source imports the Joyce lattice
Green identity through Guttmann; this refinement inherits that A0 certificate
conditionally and does not claim an independent replay or a new proof of that
identity. Record the copied bytes and hash. Its s=0 status must be CERTIFIED_TARGET.

Use exactly N=256 in(G.1), with exact binomial integers and rational arithmetic.
Check the one-sum count against the defining three-coordinate count through
n=10, and reject an omitted central-binomial factor. Budget60seconds,384MiB.

Then replace ONLY the broad A0,C0 intervals in the previous fixed certificate.
Keep both original p families, all90 nominal terms, all15 quartic candidates
and the same posterior comparison. Save a distinct refined result. No search
for a favored scalar value, no reoptimization, and no native alpha sign claim
unless the actual certified interval excludes zero. This determines whether
Green uncertainty is the practical limitation of this specific route.
