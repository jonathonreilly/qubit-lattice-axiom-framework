# A large-field test for one attempted coupled Gaussian representation

Personal route calculation,2026-09-15. This tests a SPECIFIED absolute-value
Gaussian norm. Its failure is not a phase obstruction or an axiom wall.
Signed integration, contour choices, compact phases and multiscale methods
remain available. This is not a public no-go submission or a claim that
all resummations have been exhausted.

## 1. An exact finite Gaussian realization of the coupled quadratic weight

Let P,Q be complementary real orthogonal projections in a finite two-form
space. Let A,C be independent centered real Gaussians with covariance P,
and B an independent centered real Gaussian with covariance Q. Put

    Z_e=g A,
    Z_m=b B+b C-i b A,
    c=g b.

Their bilinear covariances (without complex conjugation) are

    E Z_e tensor Z_e=g^2 P,
    E Z_m tensor Z_m=b^2 Q,
    E Z_e tensor Z_m=-i c P.

Consequently, for real fills S,n,

    E exp[i<S,Z_e>+i<n,Z_m>]
       =exp[-g^2||PS||^2/2-b^2||Qn||^2/2+i c<n,PS>].   (1.1)

This identity is exact. It has the desired electric-magnetic phase when
c=2pi N. It is an expectation of a COMPLEX integrand under a positive
Gaussian measure; it is not a positive joint electric-magnetic gas.
The two P-valued magnetic contributions cancel in the bilinear covariance.
Taking absolute values before their integration discards that cancellation:

    E |exp[i<n,Z_m>]|=exp[b^2||Pn||^2/2].              (1.2)

The physical magnetic self-energy involves Qn, whereas(1.2) involves Pn.
They cannot be identified merely because n fills a closed magnetic defect.

## 2. The growth is forced if the electric Gaussian remains real

The problem is not peculiar to the displayed three-noise construction.
Suppose Z_e is kept real Gaussian with covariance g^2 P and Z_m=X+iY
is a jointly Gaussian complex magnetic field with the same cross covariance
-i c P. Then Cov(Z_e,Y)=-c P. Positivity of the REAL joint covariance of
(Z_e,Y), or equivalently the variance of Y+(c/g^2)Z_e, gives

    Cov(Y)>=b^2 P.                                   (2.1)

Hence every such realization has

    E |exp[i<n,Z_m>]|>=exp[b^2||Pn||^2/2].             (2.2)

The same lower bound holds if the electric covariance is g^2 P_c with
0<P_c<=P on range(P), as after extracting a positive local electric
self-energy: the Schur complement gives
Cov(Y)>=c^2 P(g^2 P_c)^+P>=b^2 P. If a kernel direction of P_c is coupled
by the nonzero cross covariance, no such jointly Gaussian realization exists.

This is a restriction on keeping this electric field real and using this
bilinear cross covariance. A more general complex representation is outside
the statement, as are norm estimates that retain oscillatory cancellation.

## 3. Integer fillings can have area energy but perimeter Coulomb energy

Now work on the infinite cubic lattice Z^4. Consider a square dual
one-current j_R with unit values on its boundary, side length R, lying in
the dual1-2 plane. It has mass||j_R||_1=4R. Let q_R be its primal closed
three-form counterpart. For ANY finite integer two-form n with d_2 n=q_R,
the dual surface fills this square. Discrete Stokes against the affine
one-form x_1 dx_2 gives

    |sum_x n_34(x)|=R^2.

Since every nonzero integer coefficient obeys |n(p)|^2>=|n(p)|,

    ||n||_2^2>=||n||_1>=R^2.                         (3.1)

The real Coulomb filling energy is different:

    ||Qn||_2^2=<q_R,H_3^-1 q_R>=<j_R,H_1^-1 j_R>
                   <=C_0 R.                          (3.2)

For completeness, the componentwise lattice Green kernel in four dimensions
has a bound |G(x)|<=C/(1+|x|^2), following from its leading asymptotic and
the finite values at bounded x. On either pair of parallel sides of the
square, the sum of this bound from any one edge over the other edges is
at most2C sum_(k in Z)(1+k^2)^-1<=2C(1+pi). There are4R edges, and
different orientations have zero scalar-Hodge cross kernel. Dropping the
signs therefore gives(3.2), for example C_0=8C(1+pi). No optimized constant
or sharp asymptotic is needed. The Green bound is classical; see Lawler-
Limic, *Random Walk: A Modern Introduction*, Theorem4.3.1, with the
conversion H=8(I-P_SRW). No derivative of its error term is used.

Equations(3.1)-(3.2) give for every integer filling of the square defect

    ||Pn||_2^2=||n||_2^2-||Qn||_2^2>=R^2-C_0 R.       (3.3)

Thus changing the integer filling alone cannot make the absolute Gaussian
factor in(2.2) controlled by the magnetic Coulomb energy of this family.
In particular a bound exp[C_1||Qn||^2] with fixed C_1 cannot dominate it
uniformly over these square loops. This is a comparison of norms, not a
statement that the actual physical loop activity grows.

## 4. Extracting local self-energy does not repair this absolute norm

A usual ultraviolet split can extract an activity
exp[-a||q||^2], with fixed a>0, leaving a positive magnetic Gaussian
covariance on the other variables. For example replace the B covariance
in section1 by Q-(2a/b^2)d_2*d_2; it is nonnegative for0<a<=b^2/32,
since the Hodge spectrum is at most16. The extracted local norm is
additive on disjoint component supports. This is an exact energy split,
and the imaginary part of Z_m is unchanged. For the square defect,
||q_R||^2=4R.
In the one-sided realization just tested, the product of that activity
and the absolute magnetic vertex expectation has the lower bound

    exp[-4aR+b^2(R^2-C_0R)/2].                        (4.1)

It grows for large R. Even using a fixed multiple of the full Coulomb
self-energy instead of the local norm cannot dominate the R^2 term.
Thus this particular absolute Gaussian-vertex majorant is not a small
all-component activity norm, even when both physical defect species have
exponentially small self-activities. A statement about the convergence of
the ACTUAL signed series does not follow from(4.1).

One control makes the distinction especially transparent. In the abstract
finite case P=I,Q=0 with integer S,n and c=2pi N, the mixed phase is
identically1. There is no mixed interaction at all, while(1.2) still has
arbitrarily large growth. It would plainly be incorrect to infer a physical
instability from this norm's failure. This control is not a gauge phase.

## 5. Consequence for the ongoing proof search

The positive real-Gaussian regulator arguments in Brydges-Dimock-Hurd1998,
Lemma3 and the Gaussian appendix, do not automatically control the complex
vertices in(1.1). Their positivity-based convolution estimate needs an
actual regulator bound; replacing the bilinear covariance by its formal
quadratic inverse does not supply one. Likewise a fixed local strip in
the integer filling source cannot ignore the area-versus-perimeter family.

The viable next target is to preserve the mixed phase or its signed Hodge
operator through a scale-dependent integration, with a regulator proved
for that representation. The preceding coefficient derivation supplies
the physical source and the first quadratic extraction, but no such
all-order norm is established here. No framework axiom has been changed.
