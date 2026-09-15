# Determinant exclusion with local derivatives and protected loop bounds

Personal proof candidate, 2026-09-15. Finite CAR/Gram and BKAR author
challenges pass, with the implementation failure preserved separately. This
construction retains the protected loop representation and local derivative
geometry simultaneously. No full graph convergence or independent review
is claimed.

For fixed component vertices and each footprint resource u, let I_u be the
set of vertices whose footprint contains u. Use the same symmetric parameter
matrix S with diagonal one, and define

    D(S)=product_resources det S_(I_u,I_u), det(empty)=1.

Resources of the two species are disjoint. The product is finite for a
finite list of finite components. At S=I it is one. At S=all-ones within
each species it is the exact full hard core, since a repeated resource
gives a determinant of rank one with size >=2. At a partition matrix it
factorizes into exact hard cores within the blocks. Thus the previous
stable Gaussian/mixed-phase W can use D instead of its hard-core factor
without changing any connected partition value or its physical endpoint.
D is a polynomial in the pair parameters, so finite BKAR smoothness holds.

At forest matrices S, positive semidefiniteness and diagonal one imply
0<=D(S)<=1 by Gram/Hadamard bounds. D need not be positive on every
arbitrary cube point s_ij in [0,1]; that is not needed for the forest
stability bound. This domain distinction must remain explicit.

For distinct differentiated edge parameters A, each derivative chooses a
common resource u in A_i intersect A_j and one of the two symmetric matrix
entries S_ij or S_ji inside its determinant. Differentiating a determinant
entry yields a signed minor, without dividing by that determinant. A repeated
row or column selection gives zero. At a forest PSD Gram matrix, every
remaining cross minor has absolute value <=1 by the Gram determinant bound.
The other resource determinants also have modulus <=1. Therefore

    |partial_A D(S)| <= 2^|A| product_(ij in A) |A_i intersect A_j|.

In particular partial_ij D is identically zero if the actual footprints do
not intersect. This repairs the artificial distant routing seen in the
random-partition interpolation. The overlap count is a local contact
factor with linear footprint size, not a Coulomb energy or filling-area cost.

There is an exact contraction representation of the undifferentiated residual.
Choose unit vectors v_i with Gram S. For each resource use fermionic Fock
space over their finite-dimensional one-particle space, creation C_i=a*(v_i),
and normalized trace tau. On Hilbert space K_u=L2(tau), let

    Q_(u,i)(X)=C_i* X C_i.

This is a contraction. All these maps commute: creation operators anticommute,
and their two minus signs cancel between the left and right multiplication
in Q_i Q_j. They commute across different resources as tensor factors.
The identity matrix is a unit vector in L2(tau), independently of dimension.
The finite creation-word identity is

    tau(C_1* ... C_m* C_m ... C_1)=2^(-m) det[<v_i,v_j>].

To prove it, expand the creation word in products of distinct orthonormal
mode creators. Products with repeated modes vanish by the canonical
anticommutation relations. Different m-element mode subsets are orthogonal
for the normalized Hilbert-Schmidt inner product. Each equal subset has
squared norm 2^-m, since exactly the occupation states with those m modes
empty can receive all creations; their fraction is 2^-m. Cauchy-Binet
then gives the Gram determinant. The same argument gives the cross-minor
identity with distinct ordered row and column lists. It also covers linear
dependence, including rank-one and partition endpoints. For a component multiply its
Q_(u,i) over the resources in its footprint. Consequently

    D(S)=2^(sum_i |A_i|) <I, product_i Q_i I>.

This has the same linear mass activity cost as the full hard-core identity,
commuting diagonal entries and unit boundary vectors. The
Gaussian-dressed loop source/length bound of the preceding complete-hard-core
note therefore applies at every forest matrix S, including this softened
exclusion. The component activity remains w_i 2^|A_i| exp(R|L_i|); the same
linear mass bound and x>=32768 sufficient constants apply. At each fixed
length, the earlier absolute graph Holder argument supplies cutoff passage,
using |D|<=1. The geometric bound then sums the fourth-order source remainder
over lengths. This assertion uses the defined 1/r loop weights and excludes
all non-cycle mixed pair factors.

The cubic quadratic-limit argument remains available for a family of S
matrices fixed independently of component labels and positions: these
matrices do not break spatial translations or the cubic mark symmetry.
There is no claim that choosing arbitrary replica correlations gives the
physical connected-expansion coefficients.

The displayed local derivative estimate is already enough for a fixed-order
absolute contact bound after Gaussian stability. An operator representation
of derivatives, needed for stronger mixed graph resummations, requires care:
cofactors have different retained row and column sets, and one-sided creation
maps need not commute. Do not transfer the undifferentiated source lemma to
those maps without resolving ordering/signs. A possible route is to factor
cofactor reordering signs into local membership phases, but that is only an
idea at present. Residual mixed phases and branching remain open either way.


## Finite verification and theorem hypotheses

The author runner verifies 240 creation-word Gram identities and 1,392
cross-minor identities up to five replica vectors, including degenerate
Gram matrices. Maximum discrepancy is 8.33e-16. The two-sided creation
maps commute to 6.67e-16. Symbolic determinant derivatives on several
resource-incidence families satisfy 7,488 finite point checks of the
contact bound, including zero derivatives at compatible pairs. These
checks challenge the written finite-dimensional proof; they are not an
independent audit or a proof by extrapolation in replica number.

On the shared actual electric cochain triple [0,6,1], only components 0
and 2 share resources, and their overlap has size three. The exclusion is
exactly (1-s_02^2)^3. The connected value with the full same-species
Gaussian and a complex physical source agrees with the analytically
differentiated BKAR integral to 3.31e-24 absolute error at quadrature order
28. The original physical connected value is about -2.41527e-8-9.89984e-12i.
Its source and cochains are shared with the earlier interpolation challenge;
no independence is claimed. A non-PSD cube matrix has determinant -1 and
rejects an unrestricted positivity claim. Missing the activity boost gives
1/2 for one resource, and using an unnormalized trace gives identity norm
squared 8 in an eight-dimensional Fock space.

The first runner halted before completing BKAR because a constant integer
zero derivative was broadcast into an integer array and then multiplied
in place by a real Gaussian derivative. The initial script and failure are
frozen in review/block2_determinant_initial. Explicit float conversion
repairs the implementation; the physical formula was not changed.

The finite Taylor forest formula and its PSD preservation are checked
against Abdesselam and Rivasseau, hep-th/9409094v1, Theorems III.1 and IV.5:
https://arxiv.org/html/hep-th/9409094v1 . The relevant section III and the
full IV.5 proof were read. Here the interpolated finite weight is a smooth
polynomial-times-exponential function of all pair parameters, defined on
all real parameter values. Positivity is required only at the forest
matrices, where the matrix is a convex combination of partition matrices.
At a partition it factors across blocks, so the forest identity gives the
connected tree identity by the ordinary partition inversion. This is an
algebraic finite identity; the cited theorem supplies no infinite-volume
cluster convergence or field-scaling theorem for this model.
