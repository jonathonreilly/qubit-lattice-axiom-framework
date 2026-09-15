# The compatible dressed loop functional has a quadratic macroscopic limit

Personal derivation candidate, 2026-09-15. This completes the source limit
of the restricted loop functional from the hard-core note. It does not
identify that functional with the logarithm of a physical characteristic
function. The absent mixed residual factors and branching networks remain
necessary for the actual clock law.

## 1. Two-source version of the trace bound

The commuting-contraction trace proof works with any positive integer
number K of source insertions: put all K at one vertex, split |L|^(K/2)
between the two boundary Hilbert-Schmidt maps, then use the same simplex
three-lines argument. In particular, for two insertions,

    |F_with_two_sources|<=rho^(l-2) S2,
    S2=Tr |L|^2 J^2.                                  (1.1)

All parameters here are at zero source. Use q_i=w_i 2^|A_i| in J, so
the additional source exponential reserve is not needed for (1.1).
The conservative moment bound from the hard-core note still applies.
Let u_e,u_m be arbitrary finite real two-form tests, and set
L_e=-g<S,u_e>, L_m=-i b<n,u_m>. The filling frame gives

    S2<=c^2 [M_m(2) g^2 M_e(4)||u_e||_2^2
                       +M_e(2)b^2 M_m(4)||u_m||_2^2].  (1.2)

Indeed a row of J^2 is at most c^2 q_i M_other(2)||fill_i||_1^2,
and |<F,u>|^2<=||F||_1 sum_y |F(y)||u(y)|^2. The required weighted
anchored moment is order four. No macroscopic source shape is used in (1.2).

## 2. Quadratic coefficient operators at each length

Denote by B_l(u_e,u_m) the quadratic coefficient of the length-l compatible
Gaussian-dressed loop source. Its weight includes all l sine bonds and
the optional factor i^l=(-1)^(l/2). The orientation signs from those bonds
cancel around the cycle. The remaining Gaussian is invariant under flipping
all electric signs separately and under flipping all magnetic signs
separately. Hard core and activities have the same invariance. Consequently
the mixed electric-magnetic quadratic coefficient is zero, and

    B_l(u_e,u_m)=<u_e,D_e,l u_e>-<u_m,D_m,l u_m>.        (2.1)

The minus sign comes from the two magnetic source factors -i, rather than
from a positivity assertion about D_m,l. Neither operator is claimed positive.
Each is a real symmetric coefficient operator, defined by the finite sums
with the factor one half from the second source derivative. Equations
(1.1)-(1.2), with at most l^2 ordered choices of source vertices, imply

    ||D_species,l||_(2->2)<=C l^2 rho^(l-2),            (2.2)

for a fixed finite constant C independent of l and component restrictions.
Polarization gives the corresponding bilinear bound. Both rho and C use
the same fixed model parameters and complete anchored moment bounds.

At every fixed l these operators have absolutely summable spatial kernels.
To see this, root one component anchor and take the absolute value of the
remaining spatial sums. The spatial graph is a cycle. Average its l
spanning trees obtained by deleting one edge: every edge has inclusion
probability (l-1)/l, so the earlier graph Holder lemma uses the finite norm
||kappa||_(l/(l-1)), with kappa(x)=(1+|x|_1)^(-4). The fixed number of
fill factors, source-kernel row/column sums and spatial translations cost
only fixed-degree mass polynomials. The full same-species Gaussian has
modulus at most one after the stable local self-weight split, hard core
has modulus at most one, and all those moments converge exponentially.
For an output kernel row, the earlier anchor estimate covers the finitely
many root-component locations whose filling contains that row. This proves
absolute row and column summability at each fixed l, and identifies the
operator cutoff limit with its ordinary kernel sum.

This fixed-l absolute estimate need not be uniform in l. It establishes
existence and continuity of each individual Fourier symbol; the different
signed bound (2.2) will control the sum of their operator norms.

## 3. The full length sum has a continuous symbol

Prescribe for each length a replica correlation matrix independent of
component labels and positions, or any normalized average of such matrices.
The scalar matrices do not break spatial symmetries. The physical kernels,
component count, local footprint and normalized cubic filling marks make
D_species,l translation covariant and covariant under the signed cubic
group. Its Fourier symbol is continuous by section2.

For the defining loop coefficients 1/r, l=2r>=4, set

    D_species=sum_(r>=2) D_species,2r/r.               (3.1)

Equation (2.2) gives convergence in operator norm. For translation-invariant
operators, that norm is the essential supremum of the matrix Fourier
symbol. Differences of finite partial sums have continuous symbols, whose
supremum equals their essential supremum. Thus the symbols converge
uniformly and the limiting symbol remains continuous.

Signed cubic covariance forces its zero-frequency matrix on two-forms
to be scalar. Coordinate reflections kill off-diagonal entries between
distinct two-form orientations, and coordinate permutations equate all
diagonal entries. Write

    D_e(0)=alpha_e I, D_m(0)=alpha_m I.                 (3.2)

The constants are finite and real. Their signs or nonzero values are not
inferred from a single sine loop. These are coefficients of the restricted
functional, not yet physical dielectric constants or field covariances.

## 4. Macroscopic source limit

For h_a=a^2 f(a midpoint), use u_e=P h_a, u_m=Q h_a. Smooth-source Fourier
concentration, the continuum Hodge-symbol limit, and continuity (3.2) give

    sum_(r>=2) B_(2r)(P h_a,Q h_a)/r
       ->alpha_e ||P_cont f||_2^2-alpha_m ||Q_cont f||_2^2.            (4.1)

One can first take the limit at finitely many lengths and use (2.2) for
the uniformly bounded l2 source tail, or use the uniformly continuous
summed symbol directly. Both keep the order of limits explicit.

Together with the O(a^4) summed source remainder in the hard-core note,
(4.1) proves a quadratic limit for the complete source-subtracted restricted
loop functional, at all lengths, for every finite real linear combination
of smooth tests. The subtraction is internal to the sums. A separate
thermodynamic pressure limit or free-box field identification is not needed
for this defined infinite-kernel functional and is not asserted.

The result controls a complete analytic source object within this loop
family. It does not establish positivity of its exponential as a finite
characteristic function, does not replace the original clock probability
law by that exponential, and does not supply the omitted graph families.
