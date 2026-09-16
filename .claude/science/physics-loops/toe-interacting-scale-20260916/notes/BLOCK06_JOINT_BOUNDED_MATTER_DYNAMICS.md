# Bounded matter dynamics in the joint weak-coupling and volume limit

Personal derivation, 2026-09-16. **Provisional author theorem proposal.**
Dependencies: Block01 uniform ground field bounds and Block04 limiting
Slater matter state, hence also Block04's explicit provisional dependencies.
No independent review or audit. The matter law is the specified quadratic
paired Wilson Hamiltonian, without an additional fixed charge interaction.

Load-bearing proofs in this proposal: [uniform local ground-field bounds](BLOCK01_UNIFORM_COMPACT_FIELD_AND_SOFT_RESPONSE.md) and the [limiting Slater matter state](BLOCK04_JOINT_GAUGE_AND_MATTER_STATE.md), with the latter's explicitly linked dependencies.

## 1. Result and meaning of the dynamics

Use the same exact Gauss-law rotor model, fixed positive weights, and ground
trace rho_(g,L) in N_+=N_-=L^3 as in the preceding notes. Let B_1,...,B_n be
fixed finite CAR polynomials, each of total gauge charge zero, and let j_L
be a fixed finite-path root dressing as in Block04. Then

    rho_(g,L)[alpha_(t1)^(g,L)(j_L(B_1)) ...
                          alpha_(tn)^(g,L)(j_L(B_n))]
       -> omega_F[alpha_(t1)^0(B_1)...alpha_(tn)^0(B_n)]  (1)

along every joint g->0,L->infinity sequence, uniformly when the finitely
many times range over compact intervals. Here alpha^(g,L) is the supplied
Hamiltonian Heisenberg evolution and alpha^0 is the free paired Wilson CAR
evolution. Time is dimensionless for calH=aH; physical time is divided by a.
The limiting state omega_F is Block04's filled-band Slater state.

The Hamiltonian formula is used on the full Gauss Hilbert space, even though
the initial state lies in the specified number sector. A neutral observable
that changes both species' numbers can pass through other number sectors.
It cannot be treated as an internal operator on a closed fixed-number
subspace. The same supplied number-conserving Hamiltonian defines all these
sectors. Nonneutral root-dressed CAR operators appear only as auxiliary
algebraic factors; they are not asserted to be physical observables.

Statement (1) concerns bounded local neutral matter observables. Combined
with Block05 it supplies free matter dynamics and gauge two-point
propagation in the same joint limit. It does not add a theorem for arbitrary
mixed unbounded field/matter time words or full nonlinear gauge dynamics.

## 2. Root paths and exact elementary commutators

Choose coordinate paths on Z^3, first along x, then y, then z, with signed
steps when a coordinate is negative. Their lengths satisfy
len(p_x)=|x|_1. For charge q=+/-1 set

    a_x=U(p_x)^q c_x.                                   (2)

Orbital indices are implicit. The onsite matrices and hopping matrices mix
only orbitals of the same charge. As in Block04, a_x has its entire Gauss
charge at the root, and the a's satisfy exact CAR.

From E_l U(p)^q=U(p)^q(E_l+q p_l),

    [calH_E,a_x]
       =g q a_x P(W_E^(1/2)p_x)
          +(g^2 q^2/2)||W_E^(1/2)p_x||_2^2 a_x.        (3)

The magnetic potential commutes with a_x. The quadratic matter commutator
is

    [calH_m,a_x]
       =-sum_y h_xy(0) U(p_x+e_xy-p_y)^q a_y.           (4)

The sum includes the onsite matrix with zero loop; backwards hopping uses
the signed edge and the appropriate adjoint matrix. Equation (4) follows
by multiplying `[calH_m,c_x]=-sum_y h_xy(theta)c_y` by the root phase.

For nearest-neighbor x,y, the loop p_x+e_xy-p_y has a plaquette filling with
at most C(1+|x|_1) faces. This is the coordinate-strip construction: an
x-link has xy and xz strips, a y-link has a yz strip, and a z-link is in
the tree. Signed coordinates reverse orientations but not the count.

Block01 gives both

    ||P_l||_rho<=C,
    ||U_p-1||_rho<=Cg.                                 (5)

The constants do not depend on location or volume. Telescope the loop
product and use (3)-(5) to obtain

    ||([calH,a_x]+sum_y h_xy(0)a_y)rho^(1/2)||
       <=C g(1+|x|_1),               0<g<=1.            (6)

Multiplication by a bounded CAR factor does not enlarge the loop-defect
norm because the scalar angle function commutes with that factor. For the
electric term, Minkowski bounds the smear norm by a constant times path
length. The displayed scalar g^2 term is no larger than that bound.

The adjoint version also holds, but does not follow by equating an
operator's state norm with its adjoint's. Move P past a_x^* explicitly;
the extra commutator is g times a scalar path overlap and a bounded CAR
operator, hence contributes only O(g^2) after the outer g in (3).

## 3. Polynomial residual and its spatial weight

Let delta_0 be the local free-matter derivation `[H_m,free,.]`, defined
directly by its one-particle matrix and the Leibniz rule. This notation does
not require an extensive infinite-volume Hamiltonian to be a bounded CAR
element. For a CAR monomial B of degree m at sites x_1,...,x_m, (6) and the
Leibniz rule give

    ||([calH,j_L(B)]-j_L(delta_0 B))rho^(1/2)||
       <=C_m g [1+sum_j |x_j|_1].                      (7)

To justify applying (6) inside a product, move each remaining electric
smear to the right until it acts on rho^(1/2). Its commutator with another
dressed factor is g times a weighted path overlap. The bound

    |<p_x,W_E p_y>|<=e_max sqrt(len(p_x)len(p_y))
                      <=e_max[len(p_x)+len(p_y)]/2      (8)

keeps the total spatial weight linear for fixed degree. These terms have
an additional outer factor g from (3), and g^2<=g in the stated range.
All other factors have norm at most one. Loop defects remain scalar
functions and commute with the dressed CAR factors. This proves (7),
including adjoint factors, without a higher electric-moment hypothesis.

Finite linear combinations follow by summing the absolute coefficients.
The estimate is valid whenever the paths and their nearest neighbors embed
without wrapping in the periodic box. It does not bound a noncontractible
large loop by elementary plaquettes.

## 4. Free spreading and controlled truncation

For an initial local polynomial B set

    B_t=alpha_(-t)^0(B),           partial_t B_t=-i delta_0 B_t.  (9)

Each creation or annihilation factor evolves linearly under the bounded,
finite-range Wilson one-particle matrix h. The number of factors in each
monomial is unchanged. On coefficient vectors, the weighted norm

    ||f||_(1,w)=sum_(x,orbital) (1+|x|_1)|f_(x,orbital)|

is preserved up to exp(K|t|): the finite-range matrix and its relevant
transpose/conjugate are bounded on this weighted l1 space, because
`1+|x|_1<=2(1+|y|_1)` for nearest neighbors. The exponential series proves
the bound. Consequently the absolute coefficient sum of the spatial
weight in (7), for B_t or for any spatial truncation of its factors, is
bounded by a constant C_(B,T) for |t|<=T, independent of truncation radius.

Let B_t^R be obtained by truncating each evolving one-particle coefficient
to the cube [-R,R]^3. Then, uniformly on |t|<=T,

    ||B_t-B_t^R||<=epsilon_R(T),
    ||partial_t B_t^R+i delta_0 B_t^R||<=epsilon_R(T),
    epsilon_R(T)->0.                                   (10)

These are CAR operator-norm bounds. For example, the one-particle
exponential series has no amplitude beyond n lattice steps at order n.
For an initial support radius R0, its l2 tail is bounded by
`||f||_2 sum_(n>=R-R0)(T||h||)^n/n!`. The derivative truncation error is the
commutator of the spatial projection with h, controlled by the neighboring
tail. CAR norm continuity in the l2 coefficients and telescoping fixed
degree products give (10). Onsite terms do not increase the propagation
distance, and do not invalidate this estimate.

Choose R(L)=floor((L-3)/4) for sufficiently large L. The root paths inside
the truncation and their nearest neighbors embed without wrapping. The
weighted l1 bound and (7) therefore yield

    ||([calH,j_L(B_t^R)]-j_L(delta_0 B_t^R))rho^(1/2)||
       <=C_(B,T) g,                                   (11)

with a constant independent of R,L. Neutrality is preserved by the free
evolution and by each truncation.

## 5. Vector comparison with the microscopic dynamics

Let G=calH-E_ground on the full ambient or Gauss Hilbert space as appropriate
to the factors. The initial density matrix satisfies G rho^(1/2)=0. For
neutral B, all complete polynomials below preserve Gauss law. At finite
g,L the dressed polynomials are smooth bounded functions of the angles
with finite CAR matrices; they take the smooth ground vectors into the
operator domain. Thus

    G j_L(B)rho^(1/2)=[calH,j_L(B)]rho^(1/2).            (12)

Differentiate `exp(itG)j_L(B_t^R)rho^(1/2)`. Equations (10)-(12) bound its
derivative in Hilbert--Schmidt norm by C_(B,T)g+epsilon_R(T). When R contains
the initial support, B_0^R=B. Duhamel then gives

    ||exp(-itG)j_L(B)rho^(1/2)-j_L(B_t^R)rho^(1/2)||
       <=C_(B,T)g+T epsilon_R(T),         |t|<=T.       (13)

Only self-adjoint unitary evolution is needed. There is no assumption that
G is nonnegative in every number sector reached by an auxiliary factor.
Nor is a gap or an inverse level spacing used anywhere in (13).

To combine this with the static state theorem, do not apply Block04
directly to the growing-support B_t^R. Fix a radius r first. For L large
enough that R(L)>r, the exact finite CAR homomorphism gives

    ||j_L(B_t^R)-j_L(B_t^r)||
       <=||B_t^R-B_t^r||<=2 epsilon_r(T).               (14)

Take the joint g,L limit at fixed r and then let r grow. The residual in
(13) tends to zero without any relation between g and L. Uniformity over
t follows either from these same estimates or from a finite time net for
the finite-dimensional coefficient family at fixed r.

## 6. Finite multi-time words

Define the ground-created vectors T_(g,L)(B)=j_L(B)rho^(1/2) for local
neutral polynomials. Block04 says their pairwise inner products converge
to omega_F(B^*C). Multiplication is exact:

    j_L(A) T_(g,L)(B)=T_(g,L)(AB),
    ||j_L(A)||<=||A||.                                 (15)

Equations (13)-(14) intertwine the microscopic unitary on these vectors
with the free CAR vacuum evolution, with arbitrarily small norm error
after a fixed-radius approximation.

A ground-state time word can be rewritten, by stationarity, as alternating
bounded j_L(B_j)'s and unitaries exp(-is_j G) acting on rho^(1/2). Start
from the rightmost factor. Apply the vector comparison, approximate the
resulting free-evolved polynomial by a fixed-radius polynomial, multiply
by the next bounded factor using (15), and repeat. The number of steps is
fixed and the errors are multiplied only by the fixed operator norms of
the remaining B_j's. The final inner products are covered by Block04.

This proves (1). All estimates are uniform for the original times in a
compact set, since the finitely many intervening time differences then
lie in another fixed compact interval. Fixed alternative path/root choices
also give the same limit. Extend any such finite specification by coordinate
paths at all other sites; the finitely many exceptions only change the
constants in the weighted residual estimate. For a changed root use
coordinate paths from that fixed root, with an equivalent spatial weight.
The same vector comparison and Block04's static path independence then
apply. No growth assumption is made about an arbitrary infinite path system.

## 7. Scope

The substantive new step is the norm residual (7) and its integration
along free spreading with no dependence on the finite-volume energy gap.
The electric dressing cost and compact hopping remainders are both retained
and controlled; the interaction is not set to zero inside the finite model.

The limit still sends the microscopic gauge coupling to zero. It provides
no theorem that size alone weakens a fixed nonzero coupling, no full
interacting infrared construction, and no axiom-level selection of the
Hamiltonian or state. Gauge two-point propagation belongs to Block05;
higher unbounded gauge products and general mixed multi-time field/matter
products remain separate obligations.
