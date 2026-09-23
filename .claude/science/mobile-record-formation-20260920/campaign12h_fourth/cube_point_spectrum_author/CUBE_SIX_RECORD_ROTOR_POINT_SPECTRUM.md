# Physical point spectrum of the six-record cube rotor

Status: root conditional theorem candidate in the supplied model, September 23,
2026. This concerns the second-order operator on one finite cube. It is not a
theorem about arbitrary geometries, a thermodynamic limit, or a different
scaling. A selective independent reconstruction is still required.

## Physical Hilbert space and the exact operator

Label the cube vertices by three binary bits, 0 through 7. Edges join vertices
differing in one bit, and are oriented from the smaller label to the larger.
Let A={0,3,5,6}. In the six-record sector the total charge is four: five records
have charge +1, one has charge -1, and two vertices are vacant. The penalty-zero
sector P has all four A vertices occupied. There are 36 possible charge words
q. The one-penalty sector Q has one vacant A vertex and has 96 charge words.

Electric fields E are integer valued on the twelve oriented edges. The
physical Gauss equation is

    div E = q - 1_A.

Both sides have zero sum. Choose the spanning tree

    (0,1), (0,2), (0,4), (1,3), (1,5), (2,6), (3,7).

The remaining chords, in order, are

    (2,3), (4,5), (4,6), (5,7), (6,7).

For each q and each chord field f in Z^5, the tree fields are determined
uniquely and are integers. This follows either by successively removing tree
leaves or by the unimodularity of the reduced tree incidence matrix. Thus the
physical P space is exactly l2(Z^5) tensor C^36, with no missing Gauss sectors
and no extra field degrees of freedom. The Q space is similarly l2(Z^5)
tensor C^96.

The unit-rotor hopping operator moves a nonzero charge q_u to an empty
neighbor v, with coefficient -1 and the unique unit electric shift required
by Gauss. For an oriented edge u<v, the shift is -q_u when moving u to v,
and +q_v when moving v to u. Under Fourier transformation of f, this becomes
-exp(i theta dot Delta f). Tree hops have Delta f=0. Each P word has six
legal hops, all into Q. Write their 96 by 36 matrix as A(theta). The parent
effective-target theorem gives

    H2(theta) = -A(theta)^* A(theta).

Every entry is a finite Laurent polynomial in the five exp(i theta_j), and
the full physical bounded self-adjoint H2 is multiplication by these Hermitian
matrices on L2(T^5;C^36). Its diagonal entries are all -6. This calculation
does not substitute the eight-site ring's squeezed-coordinate factorization.

## An exact three-fiber certificate

Let p_v(x)=det(x I-H2(pi v/2)). The integer quarter-turn vectors below produce
Gaussian-integer hopping matrices and integer characteristic polynomials.
`cube_fiber_polynomials.py` stores every coefficient, with the complete words,
edges and source identity. The exact outputs are:

    v0=(0,0,0,0,0), v1=(1,0,0,0,0), v2=(1,2,0,1,3),

    p_v0 = (x+2)^5 (x+3)^3 (x+4) (x+5)^5 (x+6)^6 (x+7)^5
           (x+8)(x+14)(x^3+25x^2+176x+248)^3,

    gcd(p_v0,p_v1) = (x+2)^2 (x+5)(x+6),
    gcd(p_v0,p_v1,p_v2) = 1.

The gcd is over Q[x]. Since all polynomials have rational coefficients, gcd
one also means no common root over C. Two additional exact fibers are saved
as controls but are not needed for the certificate. Numeric fibers only
illustrate the result; they play no role in this inference.

The separate `cube_certificate_check.py` reconstructs the complete physical
transition matrix using a reduced incidence solve and its own local hopping
enumeration. It checks the Gauss embedding, rederives all three polynomials,
and checks that p_v2 is nonzero at the only three distinct roots surviving the
first gcd. This is a second author implementation, not an independent agent
check. The neutral independent reconstruction must remain separately identified.

## Why this settles the physical point spectrum

Suppose H2 psi=lambda psi with nonzero normalizable psi. The Hermitian bounded
operator forces lambda real. In Fourier coordinates psi(theta) can be nonzero
only where

    D_lambda(theta)=det(H2(theta)-lambda I)=0.

The support of a nonzero L2 function has positive Haar measure. But a nonzero
finite Laurent polynomial on T^5 has a zero set of Haar measure zero. Here is
the elementary argument: multiply by a monomial to remove negative exponents,
expand in the last coordinate, and select one nonzero coefficient polynomial.
By induction its zero set on T^4 is null. Off that set the last-coordinate
polynomial is nonzero and has finitely many roots on the unit circle. Fubini
then gives a null zero set. The one-variable base is the finite-root property.
The same proof covers constant coefficient polynomials and complex coefficients.

Consequently D_lambda would have to vanish identically. In particular lambda
would be a common root of the three exact p_v above, contradicting their gcd.
There is therefore no nonzero normalizable eigenvector of this physical H2
at any energy. In particular, the cube sector does not have the ring's physical
constant-energy eigenspace on which the prepared electric theorem was built.

This proves absence of point spectrum. No assertion of absolute continuity
is needed or made. Special-angle fiber eigenvectors still exist, but a vector
supported at one angle is not a normalizable field state. Wave packets and
approximate eigenvectors are not excluded.

## Scope and next obligations

This is a graph-specific diagnostic for the proposed common matter/field
regime. It does not prohibit other preparations, interaction pictures,
semiclassical limits, other record sectors, other graphs, or useful finite-S
behavior. It rules out copying the particular fixed-energy ring preparation
into this six-record cube without a new argument.

No conclusion about actual finite-spin dynamics follows merely from the three
polynomials. A further dynamical argument must check convergence on a common
physical core, uniform control of the remaining generator, the topology of
any field observation, and the ordering of time/spin limits. The full
unselected formation output and later formation counts remain separate
obligations. Neither a phenomenological TOE prediction nor a native-axiom
derivation is asserted.
