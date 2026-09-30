# Quantitative time modulus — author refinement, not yet checked

The frozen WORKING_PROOF stays unchanged. Its cutoff proof yields a more
explicit modulus after keeping the R dependence of the constants. This
refinement needs the same independent check; it does not change the law or
the output specification.

Every term in T10 except the diagonal electric commutator is bounded by a
constant times ||A|| and fixed support incidence. In particular the vacuum
hole part, bare jumps, grade-cross maps, circuit comparisons and bounded
remainder do not differentiate the cutoff and have no R dependence. The
support of P_R is fixed. Only T7 costs R^2+R. Hence T1 can be sharpened to

 ||Gamma(t)-Gamma(s)||_1
 <=C epsilon+C R^(-1/2)+C(1+R^2)|t-s|, R>=1.       (H1)

One may also remove the harmless S>=R restriction in the original proof.
For an arbitrary common-carrier observable O, first restrict its output
field indices to the actual spin box: O_S=P_S O P_S. This is a bounded
local observable of norm at most one, and gives exactly the original
embedded-state expectation. In T4 use O_S. Its support, A-occupancy
properties and all uniform local operator estimates are unchanged. The
cutoff P_R then bounds its fields by min(R,S); when R>=S it is the identity
on that link. T7 is still bounded by 2(R^2+R), and T11's field cutoff error
is zero on a link whose entire spin box lies inside the cutoff. No estimate
depends on an operator norm distance between P_S and the rotor identity.
Thus H1 holds for all sufficiently small epsilon in the stated coupled
family, even when the chosen R exceeds S.

For 0<h=|t-s|<=1, choose R=ceil(h^(-2/5)). Then R^(-1/2)<=h^(1/5),
R<=2h^(-2/5), and (1+R^2)h<=5h^(1/5). Therefore

 ||Gamma_(epsilon,L)(t)-Gamma_(epsilon,L)(s)||_1
                              <=C epsilon+C h^(1/5). (H2)

The value at h=0 is exactly zero. For h>1 on the fixed horizon use the
trivial trace-distance bound two and enlarge C. Every limiting trajectory
from the frozen proof is consequently Holder continuous with exponent1/5
and a constant depending only on the fixed output specification, horizon
and supplied couplings. This exponent is only a conservative consequence
of the first-moment cutoff and quadratic electric coefficient; optimality
is not asserted.

The additive C epsilon still allows small rapid microscopic oscillations.
The estimate does not provide global trace-norm speed, a common purification
of distinct times, a derivative of the limit, a second field moment or an
effective generator. Those missing consumers are unchanged.
