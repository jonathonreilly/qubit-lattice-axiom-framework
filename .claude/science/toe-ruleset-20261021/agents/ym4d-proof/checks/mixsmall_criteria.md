# MIXSMALL numerical criteria — registered before the runner

These finite controls test algebra and the explicit lattice witness, not
uniform mixed-group convergence for the interacting inherited law.

1. For orders 0 through 10, exponential derivative coefficients from the
   recurrence must equal a separate integer-partition formula exactly.
   Reciprocal coefficients must satisfy the differentiated product identity
   exactly. Coefficients at orders 1 through 4 must reproduce REALRGB G7.
2. Enumerate the actual 24 L^4 paired contours at L=3 for the specified SU(2)
   diagonal zero-mean field. The direction-one mean must have modulus below
   1e-12; its first and second directional derivatives must agree with the
   explicit root-of-unity sums to relative/absolute error below 1e-11.
   This is a finite witness control; the all-odd-L assertion uses the proof.
3. The closed face-neighbourhood of {-1,0,1}^4 must have 297 vertices and
   its external face boundary must have 216 vertices, by direct enumeration.
4. Mutation controls: omitting the local kernel normalizer derivative must
   disagree with the exact SU(2) zero-mean second derivative by more than
   1e-8 at L=3, u=10 and kappa=1; replacing the paired path divisor 24 L^4
   by 24 L^3 must fail the derivative comparison in criterion 2.

All criteria are required if the mathematical checks execute. Use no
stochastic sampling, no convergence extrapolation and no fitted constants.
Failures remain failures. Any unregistered follow-up is labelled post-hoc.

Execution requires a single-process nonblocking lane lock, observed nice at
least 10, BLAS and all relevant numerical thread settings equal to 1, maximum
of the reported load averages below 8, at least 30% free memory, and RSS below
1,000,000,000 bytes. Check before mathematics and between sections. If nice
or another gate cannot be verified, record NOT RUN and perform no check.
