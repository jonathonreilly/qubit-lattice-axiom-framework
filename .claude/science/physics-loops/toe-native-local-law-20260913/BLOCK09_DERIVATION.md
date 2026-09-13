# Local Grassmann interactions and the common metric

Author derivation in progress; no independent review. This extends a
supplied classical geometric construction to formal Grassmann-valued local
functionals. It is not an operator-ordered quantum constraint theorem or an
interacting quantum continuum proof.

## Deriving the interaction condition from a graded bracket

Use odd spinor fields q, qbar on a smooth slice, with an even canonical
Poisson bracket satisfying {q_a(x),qbar_b(y)}=-i delta_ab delta(x-y).
The bracket between two odd coordinates is symmetric. Right/left derivatives
give, for even F,G,

    {F,G}=-i sum_a [ (F <-d/dq_a)(d/dqbar_a ->G)
                       +(F <-d/dqbar_a)(d/dq_a ->G) ].

For bilinears this gives {qbar A q,qbar B q}=-i qbar[A,B]q. Thus the
bilinear matter and configuration-connection calculations of the free
classical construction carry to this graded setting with the same signs.
The metric variables are even. The Darboux momentum shift and its curvature
follow from the same bilinear identity, now in the formal Grassmann algebra.

Use ordinary spinors q=g^-1/4 psi when expressing a potential, and let U
be a real, even, derivative-free local polynomial in their components.
It has no explicit spacetime-coordinate dependence and is invariant under
the local spatial spin rotation. Define V[N]=int N sqrt(g) U(q,qbar).
The metric derivative of V is ultralocal in N. Hence its mixed bracket with
the gravitational kinetic term cancels after N,M antisymmetrization. Its
self bracket has no derivatives of delta and likewise cancels. The new
normal bracket comes from the kinetic spinor term and V.

At a background normal frame, the lapse-gradient part of the kinetic flow is

    {q,H_m[N]}=...- (partial_i N) alpha_i q/2,
    {qbar,H_m[N]}=...- (partial_i N) qbar alpha_i/2.

All remaining terms are proportional to N and cancel in the cross bracket.
Let B_i be the EVEN derivation defined by

    B_i q=alpha_i q/2, B_i qbar=qbar alpha_i/2.

It acts on a product with the ordinary Leibniz rule, since the transformation
itself is even even though its arguments anticommute. Then

    {H_m[N],V[M]}+{V[N],H_m[M]}
       =-int sqrt(g) (N partial_i M-M partial_i N) B_i U.

The alpha_i in an orthonormal frame are the two Weyl blocks. Consequently
within the stated local-potential ansatz the old normal bracket is preserved
exactly when B_i U=0 for each boost generator. Necessity can be checked
coefficientwise in the exterior algebra: vanishing against all N,M first
gives div B=0 with N=1, then arbitrary N gives B.grad N=0 and hence B=0.
Spatial covariance was separately assumed. Together, rotations and boosts
are precisely the infinitesimal proper Lorentz invariance condition on U.
This is a local polynomial criterion; it supplies no quantum renormalization
or existence theorem for the interacting model.

## Why the commuting-spinor shortcut is unsafe

In a single two-component Grassmann species R=(r0,r1), the quartic
Rbar0 Rbar1 r0 r1 spans its degree-four top exterior power. A determinant-one
Weyl boost or spin rotation preserves the two annihilator and two conjugate
volume factors. Thus its density square is Lorentz invariant after normal
ordering. Directly, n_R j_R^i=0 for each i in this Grassmann algebra.
For commuting components, n_R j_R^i is generally nonzero. Applying that
commuting counterexample to the physical two-component fermion would give
a false interaction obstruction. The finite CAR normal-ordering constant
must also be separated from the quartic symbol.

## Candidate invariant space for one Weyl pair

Use the cone spin basis R=q_+, L=sigma3 q_-. Their free symbols are
+sigma.p and -sigma.p, while spatial rotations act by the same SU(2)
matrix. Boosts act as +sigma_i/2 on R and -sigma_i/2 on L, and by the
Hermitian conjugates on their barred components. Define n_R=Rbar R,
j_R=Rbar sigma R and similarly for L (j_L is written with +sigma; its
physical left-Weyl current has the opposite sign).

A U(1)-charge-preserving quartic has two annihilators and two conjugates.
The annihilator-pair representation decomposes as

    wedge^2 (R plus L) = scalar plus vector plus scalar.

Pairing with the conjugate representation suggests five complex invariant
basis polynomials: rbar r, lbar l, rbar l, lbar r and

    U_cross=n_R n_L+j_R.j_L,
    r=r0 r1, l=l0 l1.

The bar on a pair reverses order under conjugation; explicit component
calculations below must preserve that sign. Four Hermitian scalar-pair
combinations and U_cross give five real Hermitian couplings. If separate
valley number is required, the two pair-transfer combinations are excluded,
leaving three. This representation argument and its exact component basis
are to be checked independently by the exterior-algebra generator kernel.

## Specific native on-site interaction and the node phases

For a concrete interaction use c_n0^dagger c_n1^dagger c_n1 c_n0 in the
specified two-orbital Wilson carrier. At lattice spacing a and fixed v,
normalized cone fields have the leading expansion

    c_n = a^(3/2)/sqrt(v)
                [ exp(i kappa n3) R(y)+exp(-i kappa n3) sigma3 L(y) ],
    y=D^-1 a n, kappa=acos zeta.

This normalization preserves sum_n c^dagger c -> int dy (Rbar R+Lbar L)
after suppressing nonresonant phases. In the range zeta in [1/2,1),
4 kappa is never a reciprocal-lattice multiple, so pair transfer oscillates.
The zero-phase quartic is a sum of same-valley pair terms and the cross
pair term associated with

    m=r1 l0+r0 l1.

Unlike a scalar pair, m is a specified spatial triplet component. Its
conjugate product is expected to have nonzero spin-rotation and boost
variations. The exact zero-phase expansion and those variations must be
computed, not assumed from a density label. This is a proposed explicit
finite-cutoff discriminator, not an axiom-wide obstruction.

## A finite native construction to test the invariant alternatives

Finite Laurent filters f_+(k)=(1+sin k3/v)/2 and
f_-(k)=(1-sin k3/v)/2 take values 1,0 at the respective nodes. Define
filtered native fields R_n=f_+ c_n and L_n=sigma3 f_- c_n. They are finite
range, but are not exact separate canonical species at general momentum.
Only even, normal-ordered quartic combinations are proposed as physical
operators. The three valley-number-preserving invariant polynomials above
can be formed from these finite combinations, with explicit Hermitian
symmetrization when their finite-cutoff contractions require it.

Their leading node quartics match the intended invariant polynomials;
wrong-node leakage is derivative-suppressed. This construction would show
that the specified on-site mismatch can be changed within finite native
couplings, without changing the carrier or adding an axiom. The exact CAR
normal-ordering and path support remain checks to do.

## Scaling is a separate obligation

If the physical Hamiltonian is (h_0+lambda W)/a and c_n scales as above,
a derivative-free quartic contributes lambda a^2/v times its continuum
polynomial. A fixed small dimensionless lambda therefore has a vanishing
engineering coefficient; a nonzero finite continuum g would require
lambda=v g/a^2. That leaves a fixed small-coupling hypothesis as a->0.
Engineering scaling by itself is not a proof that interactions cannot
renormalize relevant terms or that a particular strong-coupling limit exists.
The known native small-coupling theorem must be checked on its own stated
counterterm and observable domain before use.

Primary source read so far: Dreiner–Haber–Martin arXiv:0812.1594v6,
section 2 passages spanning equations 2.52–2.75 and in particular the
commuting/anticommuting distinction and Fierz equations 2.59–2.70. The
313-page review has NOT been read in full. The component and generator
calculations planned here will not import an invariant coefficient from it.

## Exact component result and a dimension proof

The exterior calculation passed 76 initial checks. It found a five-dimensional
invariant subspace inside the 36-dimensional complex charge-preserving quartic
space, versus ten dimensions for rotations alone and three when separate valley
number is imposed. The listed five polynomials are independent and invariant;
the calculation also agrees with direct finite-CAR phase averages.

The dimension has an analytical proof rather than depending on the matrix
rank output. Complexify the proper Lorentz Lie algebra into the two commuting
sl(2) factors. R and L are their two fundamental representations, with an
inverse/conjugate representation identified by the invariant epsilon tensor.
Their same-species antisymmetric pairs r and l are scalars. The four mixed
components R_a L_b carry the tensor-product vector representation. It is
irreducible: the two sl(2) actions generate M2 tensor I and I tensor M2,
and their products span M4. A commuting endomorphism of that space is
therefore scalar, while no invariant vector lies in it. The two scalar
copies have four independent pairings with the two conjugate scalar copies;
the vector sector has one. This proves 4+1 dimensions. The explicit five
polynomials exhibit all of them. Hermitian conjugation fixes a five-real-
parameter family; separate valley phase invariance removes rbar l and its
conjugate, leaving the three stated real polynomials.

With monomial order Rbar0,Rbar1,Lbar0,Lbar1,r0,r1,l0,l1, the cross invariant is

    U_cross=-2 [Rbar0 Lbar0 r0 l0+Rbar1 Lbar1 r1 l1
                       +Rbar0 Lbar1 r1 l0+Rbar1 Lbar0 r0 l1].

It also equals -2 (Rbar L)(Lbar R), with precisely this Grassmann order.
The same-species relations are n_R^2=2 rbar r and
j_R.j_R=-3 n_R^2. These identities explain why a commuting null-current
formula is not the correct quartic reduction for a Grassmann field.

For the native zero-phase polynomial U_site=rbar r+lbar l+mbar m, the
third boost gives the explicit nonzero polynomial

    B_3 U_site=-2 Rbar0 Lbar1 r0 l1
                          +2 Rbar1 Lbar0 r1 l0.

The first two boosts give zero, the first two rotations give nonzero
polynomials, and the third rotation gives zero. This anisotropy is tied to
the actual relative sigma3 basis between the two native cones. It would be
missed by replacing the two orbital densities with two independently rotated
continuum species before carrying out the node expansion.

## Finite filtered operators and their honest domain

At v=.8, the finite filters satisfy

    {R_n0,L_n0^dagger}=(1/4-1/(8v^2)) I,

which is nonzero. Thus the construction does not claim exact microscopic
separate CAR species. Evaluate each degree-four invariant as a normal-ordered
polynomial in the filtered fields, with every creation factor to the left
of every annihilation factor. The three valley-preserving invariant operators
are Hermitian and commute with total fermion parity on the actual six-mode
CAR space at the neighboring z cells. This is a direct 64-dimensional
operator check, distinct from the exterior-algebra calculation.

For each microscopic monomial the exact identity

    c_i^dagger c_j^dagger c_k c_l
      =delta_jk c_i^dagger c_l
                           -(c_i^dagger c_k)(c_j^dagger c_l)

expresses it through even bilinears. All endpoints lie in three adjacent
z cells and two orbitals, so their x/z protected paths have length at most
three. The native even-path dictionary therefore encodes the full quartic
on bounded support. Normal ordering is essential: replacing this polynomial
with an un-normal-ordered product can add finite-cutoff bilinear terms.
Those terms have not been silently folded into the invariant quartic.

At a specified node, the finite filters have exact desired values. Their
wrong-node factors are O(a) on fixed smooth wave packets. The leading
four-leg vertex of these normal-ordered operators is therefore the intended
continuum invariant, with derivative-suppressed corrections. A proof of
renormalized interacting fields or the quantum constraint algebra does not
follow from this tree-level statement.
