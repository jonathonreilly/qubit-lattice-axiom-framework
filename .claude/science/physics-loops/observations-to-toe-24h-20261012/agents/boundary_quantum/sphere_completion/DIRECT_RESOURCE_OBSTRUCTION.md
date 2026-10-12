# An angular cusp imposes a resource cost on the stated quantum realization

Direct parent derivation, 2026-10-12. This extends the physical checks on the
existing fixed conditioned pair law without changing its observations or k.
The full-sphere classification remains subject to separate proof/certificate
review. The theorem here is conditional on a positive, normalized Legendre
expansion and does not need its claimed numerical threshold.

## Conditional theorem

Suppose f(c)=sum_l a_l P_l(c), with a_l>=0 and sum_l a_l=1. If

    lim_(theta down to0) [1-f(cos theta)]/theta = s > 0,

then sum_l l a_l diverges. Consequently the specific harmonic/Clifford
direct-sum pure state in SPHERE_THEOREM.md, whose l sector is maximally
entangled with local dimension2^l, has infinite entanglement entropy. Any
positive local Hamiltonian bounded below by epsilon*l on the l sector,
for fixed epsilon>0, has infinite expectation in that construction.

These conclusions concern this realization and that energy premise. They
are not lower bounds on the entanglement of every possible realization of
the same correlation, nor a no-go for finite-accuracy laboratory data.

## Proof of the moment obstruction

For integer l, Laplace's polynomial integral gives

    P_l(cos theta) = (1/pi) integral_0^pi
        (cos theta+i sin theta cos phi)^l dphi.

The polynomial identity follows either by expanding the integer power or
by analytic continuation of [DLMF14.12.7](https://dlmf.nist.gov/14.12.E7)
at order0. Both the complex base and its theta derivative have modulus at
most1 for real angles. Therefore |d_theta P_l(cos theta)|<=l and

    0 <= [1-P_l(cos theta)]/theta <= l,   theta>0.

For each fixed l, its numerator is O(theta^2), so the ratio tends to zero.
If sum_l l a_l were finite, dominated convergence on the discrete positive
measure a_l would make the corresponding ratio for f tend to zero. This
contradicts s>0. The expansion is uniformly absolutely convergent because
|P_l|<=1 and sum a_l=1; no unjustified differentiated infinite series is used.

For the stated direct-sum state, the reduced density operator has eigenvalue
a_l/2^l with multiplicity2^l. Its entropy, with natural logarithms, is exactly

    S = sum_l [-a_l log a_l + a_l*l*log2] = infinity.

All summands are nonnegative. The energy assertion follows directly from
sum a_l epsilon*l, without assuming an entropy-energy inequality.

## The fixed conditioned family has the required cusp

For 0<=theta<=pi, the previously declared u=(2/pi)arcsin(cos theta)
equals1-2theta/pi. With t(theta)=tanh(k cos theta), write

    f_k(cos theta) = [u+t]/[1+u*t].

At theta0, u=1, t'=0 and the derivative with respect to u is
(1-t)/(1+t)=exp(-2k). Hence for every finite k>=0,

    lim_(theta down to0) [1-f_k(cos theta)]/theta
       = (2/pi) exp(-2k) > 0.

Thus whenever this family has the positive normalized Legendre expansion,
its harmonic/Clifford construction has the resource obstruction above.
A normalized abstract state alone has not supplied a finite-energy source.
The extra energy premise is explicit; no Hamiltonian has been inferred from
pair probabilities. The standard ideal singlet correlation f(c)=c has zero
angular slope at coincidence and is not caught by this obstruction.

## Exact k0 benchmark and finite-accuracy escape

At k0 set C_n=binomial(2n,n)/4^n. Integration by parts using
(2l+1)P_l=P'_(l+1)-P'_(l-1), followed by the even Legendre angular integral,
gives the exact nonzero coefficients

    a_(2n+1) = C_n^2-C_(n+1)^2
             = C_n^2(4n+3)/(4(n+1)^2).

The angular integral itself follows by taking the constant Fourier coefficient
in the Legendre generating function: factor
(1-2t cos theta+t^2)^(-1/2) into
(1-t exp(i theta))^(-1/2)(1-t exp(-i theta))^(-1/2).
Its full-period constant coefficient is sum_n C_n^2 t^(2n); symmetry gives
integral_0^pi P_(2n)(cos theta)dtheta=pi C_n^2. This derives the formula
rather than assuming a fitted asymptotic tail.

Coefficients telescope: the harmonic tail above l=2N+1 is exactly
r_N=C_(N+1)^2. Moving r_N to the l1 sector yields a normalized PSD finite
kernel with uniform correlation error at most2r_N. C_n^2<=1/(n+1), by the
elementary central-binomial bound, gives the conservative explicit bound
2r_N<=2/(N+2). The state now uses finitely many sectors and has finite entropy
and energy for finite sector energies. Its error tolerance is an additional
experimental readout requirement, not a refit of the exact pair law.

The partial first moment has the exact telescoping identity

    sum_(n=0)^N (2n+1)a_(2n+1)
       = 1+2 sum_(n=1)^N C_n^2-(2N+1)C_(N+1)^2.

This is a useful executable benchmark for the otherwise all-order argument.
It does not replace the dominated-convergence proof. The result motivates
requiring an explicit finite-resource source and angular resolution before
using this candidate as a physical quantum component of a unification.

Author evidence: direct_resource_check.py and runtime quantum/direct_resource/
resource_check_v1.json. Narrow independent checking is pending. No formal
audit, observational exclusion, universal quantum no-go or novelty claim.
