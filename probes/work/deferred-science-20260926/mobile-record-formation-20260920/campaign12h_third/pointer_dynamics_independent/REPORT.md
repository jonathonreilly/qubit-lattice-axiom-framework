# Independent pointer-code and noisy-intertwiner check

This report and its exact runner were completed before access to the new
author pointer/noise notes, scripts or results. The supplied target is
recorded in `SPECIFICATION.md`; the unchanged routed definition and prior
elementary contraction argument are bound in `SOURCES.json`.

**Results.** The proposed 64-dimensional construction gives fourteen
orthonormal covariant pointer states and a valid invariant orthogonal
vacancy. Rank-one local Lindblad jumps implement the complete joint-law
evolution of any specified finite-state local classical process on such
orthogonal pointers, including the fixed-matching routed color process.
This is a supplied block encoding, with the native-record and moving-geometry
qualifications described below.

The noisy-pointer preparation has a different outcome. For the specified
N=12 input/output configurations, the full classical generator forces the
initial off-diagonal population entry

    -eta^2 (eta^2-2 eta+2) / [784 (1-eta)^2],              (1)

which is strictly negative for every 0<eta<1. At eta=1/2 it equals
**-5/3136**. Therefore there is no positive, and hence no CPTP, exact
intertwining family for this fixed preparation and the complete specified
classical law, already for sufficiently small positive time. This argument
tests the full generator; it does not require a CP implementation of each
classical jump separately. Meanwhile the transverse metric has u=4v, so
that earlier necessary metric condition does not decide this question.

## 1. Exact pointer construction

Order the six axis labels +e1,-e1,+e2,-e2,+e3,-e3 followed by the eight
cube corners in lexicographic sign order. Put u_z=(1,z), w_z=u_z^tensor3,
and let F have these fourteen columns. Its real Gram matrix is

    G_(z,z')=(1+z dot z')^3.

Its characteristic polynomial is exactly

    (lambda-48)^4 (lambda-6)^2
    (lambda^2-92 lambda+192)
    (lambda^2-88 lambda+384)^3.                          (2)

One can derive (2) by decomposing functions on the fourteen labels. The two
orbit-constant functions give the matrix [[12,32],[24,80]]. For each spatial
component the A-vector and B-vector functions give [[8,32],[8,80]]. The two
A-axis quadrupoles have eigenvalue 6; the three B-quadratic products and the
one B-cubic product have eigenvalue 48. These fourteen functions exhaust the
label space. The scalar/vector matrices are written in unnormalized bases,
so their displayed off-diagonal entries need not coincide.

The eigenvalues are 46+-2 sqrt(481), each once; 44+-4 sqrt(97), each three
times; 6 twice; and 48 four times. They are all strictly positive. Equivalently
G=F^dagger F has determinant

    192*384^3*6^2*48^4 = 2077601987473440768 > 0.

Thus F has exact column rank fourteen, the unique positive G^(-1/2) exists,
and W=F G^(-1/2) satisfies W^dagger W=I14. No numerical eigenvalue threshold
or approximate orthogonalization enters this conclusion.

For each proper cubic rotation R, let P_R permute the fourteen labels.
Then V_R F=F P_R, and G commutes with P_R. Positive functional calculus gives
G^(-1/2)P_R=P_R G^(-1/2), hence V_R W=W P_R. The exact checker verifies all
twenty-four integer tensor actions and Gram commutations.

Let

    vnum=sum_(i=1)^3 (|0 i i>-|i 0 i>),   v=vnum/sqrt(6).

The six tensor basis states are distinct, so ||vnum||^2=6. The occupied
w_z are symmetric under interchange of the first two tensor factors while
vnum is antisymmetric, hence F^dagger vnum=0. Orthogonalizing within the
occupied span preserves this orthogonality. Finally the contracted sums
over i are rotation invariant, since sum_i R_(j i) R_(k i)=delta_(j k).
Consequently V_R v=v. The result is an isometric fifteen-state code in
dimension 64, with a one-dimensional vacuum and forty-nine unused dimensions.

## 2. What the local jump construction implements

Write |a>_code for an occupied pointer column of W and |0>_code=v. On a
finite collection of blocks, take a specified finite-state local classical
event with local input i, output o and nonnegative rate c(i). Its quantum
jump can be

    J_(o,i)=sqrt(c(i)) |o>_code <i|_code,                 (3)

with all rate-reading context blocks included unchanged in i and o, and
identity on blocks outside that event's footprint. In the Lindblad generator
sum_J [J rho J^dagger-(1/2){J^dagger J,rho}], a diagonal classical mixture
receives exactly c(i) p_i at o and loses c(i) p_i at i. This holds for an
arbitrary correlated joint classical law. The diagonal code subspace is
invariant, so uniqueness of the finite-dimensional evolution proves exact
intertwining at all times. The construction has an ordinary CPTP extension
to the complete block Hilbert space; unused code-complement states can be
left dark. The generated evolution on coherences is an additional choice,
not an asserted continuation of a classical phase.

For the actual routed color channel this specializes to

    sqrt(k0/2+h(l,a,b,r)/4) |l,b,a,r><l,a,b,r|.

The stated rate is nonnegative, and the proof above applies without a product
law assumption. Vacancy-only moves use |a,0><0,a| with their stipulated
rates; births use |a><0|, or multi-block input/output words when the classical
birth creates an entire pair. Conditional rates are represented by including
their finite context in (3). There is no need to access a hidden preparation
label externally: the supplied pointer states themselves are orthogonal.

When the classical event family and rates are cubic covariant, rotations
permute these jump operators, so their Lindblad sum is also covariant. This
applies to the supplied proper-cubic routed rates. The quantum code alone
does not impose symmetry on an arbitrarily chosen birth-rate family.

There are two essential scope boundaries.

- A 64-dimensional factor is six qubits, mathematically grouped as three
  copies of 1 direct-sum 3. The code supplies a block, not a demonstrated
  assignment to the original two physical sites of a record pair. It also
  does not supply a deterministic quantum operation taking the nonorthogonal
  raw w_z, or unknown original physical qubits, to these orthogonal pointers.
  W=F G^(-1/2) defines the code; it is not such an operational encoder.
- The original routed note also has continuous immutable contents, unique
  antipodal keys, and a changing partner matching before filling. Fourteen
  color pointers plus one vacancy do not encode all of that information.
  For a fixed supplied matching they do implement the complete routed
  **color** joint law. For a finite colored-matching projection with births
  and slides, all required geometric state and admissibility information
  must also be represented orthogonally or otherwise supplied as part of a
  well-defined classical control. A claim about that enlarged finite-state
  process then follows from (3), but is not provided by the fifteen-state
  color block alone. In particular, the continuous tilted birth distribution
  and exact-content recognition in the source are not a finite-pointer
  quantum protocol. No unchanged native-projector or fine-site realization
  is inferred here.

These are limitations of what the specified code establishes, not a failure
of its exact orthonormality or of the Lindblad classical embedding.

## 3. Inverting the noisy preparation

Put d=14, r=1-eta and a=eta/d. In the pointer basis the local preparation
acts on classical probability columns by

    T=r I+a 11^T,
    T^-1=(I-a 11^T)/r.                                 (4)

For 0<eta<1 this is invertible; rho_a are strictly positive and linearly
independent diagonal matrices. For K=864 pairs, the joint preparation is
T^tensor K. If Q is the forward classical generator on probability columns,
an exact quantum intertwiner on all joint classical laws forces its action
on the complete diagonal operator subspace to be

    A=T^tensor K Q (T^-1)^tensor K.                     (5)

This follows by linearity, using the linearly independent encoded
configuration states as a basis. It leaves no freedom to repair the forced
image of a pure pointer projector by choosing an action on coherences.
For two different pointer configurations I,O, positivity requires
`<O|Lambda_t(|I><I|)|O> >= 0`; its value at t=0 is zero. Thus the forced
off-diagonal generator entry A_(O,I) must be nonnegative. A negative value
contradicts a positive extension, whether or not a proposed quantum
generator is decomposed into the classical events.

## 4. Complete routed support reduction

Take the input colors alpha=B(-1,-1,-1), beta=B(+1,-1,-1), chi=A(+e2)
at anchors x=0,10,8 on the first coordinate axis. The output is
(chi,alpha,beta). The remaining colors are A(+e1) in both pointer words.
The difference set therefore has exactly these three sites.

A four-context classical channel acts as Q_local tensor I on the remaining
sites. In (5), T T^-1=I outside the footprint. Its entry between I and O
is consequently zero unless its footprint includes all three differing
sites. This is an exact cancellation after the full inverse, not a
probabilistic approximation to the initially pure pointer configuration.

On the N=12 winding matching, delta=-e1 has route displacement -2 e1.
The other four nonidentity directions have displacement -e1+-e2 or
-e1+-e3; their four context positions cannot include three distinct sites
on this axis. There are exactly two qualifying directed channels:

    u=0:   contexts (2,0,10,8),
    u=10:  contexts (0,10,8,6),                         (6)

with the two suppressed coordinates zero. The independent code enumerates
all 864*5=4,320 nonidentity routed supports and finds precisely (6).
The +e1 route is fixed and absent. All four context sites are distinct.

The constant k0/2 exchange term acts on only the two endpoint colors after
conjugation, since T tensor T commutes with a swap. It cannot change three
pointer indices. In each of (6), the part of h reading the other context
site likewise has support missing one differing site and contributes zero.
What remains is a three-site calculation, still derived from the sum of
the complete positive-rate channels.

## 5. Closed-form calculation of the negative entry

In this section S is the actual color tensor for delta=-e1, including its
factor gamma/2. It is symmetric, has zero row and column sums, and has
S_(z,z)=0. On two pointer factors define

    H=(T tensor T) diag[S_(p,q)] (T^-1 tensor T^-1).

For distinct labels x,y, (4) gives

    T_(x,p)(T^-1)_(p,y)
       =-a delta_(p,x)+(a/r)delta_(p,y)-a^2/r.

Zero row/column sums eliminate the constant terms when these expressions
are contracted with S. The zero diagonal and symmetry give exactly

    H_((x,y),(y,x))=a^2(1+r^-2)S_(x,y).                (7)

Let P12 and P23 swap the indicated pointers on the three differing sites.
The first channel's surviving drive, after preparation conjugation, is

    (P12-I)(H13-H23)/4.

At the selected three-cycle entry, its -I terms vanish, the P12 H13 term
has an unchanged wrong index, and only -P12 H23 remains. Its value is
`-H_((chi,beta),(beta,chi))/4`. The second channel analogously has
`(P23-I)(H12-H13)/4` and contributes
`-H_((chi,alpha),(alpha,chi))/4`.

For the actual labels and gamma=1,

    S_(chi,alpha)=S_(chi,beta)=1/2.

Each contribution is therefore

    -eta^2 [1+(1-eta)^2] / [1568 (1-eta)^2],

and their sum is (1). This expression is strictly negative throughout the
specified open eta interval. At eta=1/2 the two complete four-context
contributions are individually -5/6272, with sum -5/3136.

The exact runner checks (1) in two separate ways: it performs symbolic
integer-polynomial summation over all 14^3 words for each surviving
three-site term, and at eta=1/2 independently sums the **complete** positive
four-context rates over all 14^4 words for each channel in (6). Both give
the displayed fractions. The actual rates over these complete enumerations
range from 1/20 to 21/20, and the constant-stirring contributions sum to
zero exactly.

## 6. The transverse metric and countercontrols

Uniform averaging gives tau=I14/14. The local tangent matrices are

    Rx=(r/2)diag(e_a2),    Ry=(r/8)diag(b_a3).

Consequently

    u=Tr Rx tau^-1 Rx=7r^2,
    v=Tr Ry tau^-1 Ry=7r^2/4,
    Tr Rx tau^-1 Ry=0.                                 (8)

Thus u=4v for every 0<eta<1. The first stationary transverse metric test
passes; it cannot establish positivity of the complete map. The full-law
entry (1) supplies a different necessary test and fails.

At eta=0, T=I and the entry is zero, consistently with the orthogonal
classical-pointer Lindblad realization. At eta=1, T is singular and all
fourteen rho_a coincide: a constant preparation can intertwine trivially
with a map fixing that single output state. The pole of (1) as eta approaches
one is an inverse-map effect and is not a claim about the eta=1 case.
The obstruction uses the supplied context drive. With gamma=0, identical
local T commute with every endpoint swap, so noisy preparation is compatible
with the random-swap process; noise alone is not a universal obstruction.

## Evidence, failures and limits

`check.py` is a separate implementation with no imports of author checkers.
`RESULTS.json` contains the exact Gram polynomial/determinant, covariance and
vacuum residuals, every selected route, symbolic polynomial coefficients,
full-rate sums and metric identities. `RUN.log`, `RUN.stderr` and
`RUN_RECEIPT.json` preserve the full first execution, which passed. No failed
mathematical control occurred. One context-only prose patch missed its
matching line and changed nothing; its error is preserved under
`failed_attempts/report_patch/`.

The unchanged routed source is bound at
dc7bac51a1ffb273e11e9356713778aeb645acbfb280973f927c1f1de007d873.
The earlier elementary metric argument is bound at
f8b7e30ac671f19c93e5c9456c1f4e892f221eaa7888435e7aec5155126455e7.
No new author pointer/noise file was opened. No complete many-body matrix,
thermodynamic limit, unknown-qubit interface, physical-site implementation,
publication, or formal audit status is claimed. The mathematical negative
result applies to this fixed noisy preparation, the stipulated exact
full-law intertwining, and the specified routed generator. Approximate
implementations, additional input-correlated resources and different
encodings are different targets.
