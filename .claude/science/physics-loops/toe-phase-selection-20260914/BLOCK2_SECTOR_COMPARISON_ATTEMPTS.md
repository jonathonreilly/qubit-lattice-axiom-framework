# Block 2: sector-comparison routes and a failed general principle

Status: personal exploratory derivation, not an independent result or a
phase/no-go claim. This block follows PR 8123 and keeps the actual cubic
Hamiltonian's sector ordering open.

## Exact counterexample to unrestricted central-fiber ordering

The tempting general statement was: for truncated coordinates in
{-1,0,1}^n, symmetric positive hopping along integer charge-preserving
unit-coordinate jumps, and a nonnegative quadratic electric potential, the
zero-charge sector has the lowest energy. This is false without additional
geometry. A bounded numerical probe found a four-coordinate example; it was
then reduced to the following exact rational certificate.

Take d=(1,1,2,3), charge d.b, potential sum_i b_i^2/5, and the four jumps

    f1=(0,1,1,-1), f2=(1,-1,0,0),
    f3=(1,0,1,-1), f4=(1,1,-1,0),
    (w1,w2,w3,w4)=(3,1,1,3).

Every d.fj=0. Let T_f shift by f when the result stays in the cube, and
vanish otherwise. The Hamiltonian is

    H = sum_i E_i^2/5 - sum_j wj (T_fj + T_fj^*).

It is real symmetric with nonpositive off-diagonal entries. Adding the
constant 2 sum_j wj makes it a sum of positive local hopping terms and the
nonnegative potential; that constant does not change sector ordering.

In lexicographic coordinate order the d.b=0 and d.b=1 sectors each have nine
states. All leading principal minors of H_zero+(137/20)I are positive:

    149/20, 22201/400, 536549/1600, 78217401/32000,
    5870630017/640000, 522373125493/12800000,
    12953708606817/51200000, 1017053561408773/1024000000,
    10410603177194777/20480000000.

Sylvester's criterion gives E_zero > -137/20. In the d.b=1 sector take the
integer vector (4,4,1,3,5,5,3,5,3), in the same lexicographic ordering.
Its Rayleigh quotient is -4646/675, strictly below -137/20 by 89/2700.
Consequently E_charge=1 < E_zero. This conclusion uses exact arithmetic,
not a fitted difference of approximate eigenvalues.

The row d is not a cubic incidence row; jump weights are unequal; this
example is not the supplied clock Hamiltonian. It invalidates only the
unrestricted comparison premise. It provides no axiom contradiction and no
counterexample to the actual geometric neutral-sector conjecture. The first
random-weight discovery and all attempted cases are retained in
BLOCK2_DISCRETE_SECTOR_PROBE.json; the exact rational version is a subsequent
simplification. Original equal-weight d=(1,1,2,3) checks favored zero charge.
A successful geometric proof must use additional structure explicitly.

## Why the usual angle-modulus proof still needs a replacement

The unconstrained electric lattice admits a Fourier representation in compact
angles. Quadratic electric energy becomes a positive differential kinetic
term and the plaquette terms become a multiplication potential. Modulus can
then lower the kinetic form and remove a charge character. The finite-spin
cutoff changes the admissible function space: modulus need not preserve its
Fourier support. Our new counterexample shows that there cannot be a general
replacement relying only on symmetric truncation, positive hopping and a
quadratic potential.

The cutoff one-link heat kernel is 1+2 exp(-g tau) cos(theta). It becomes
negative near theta=pi for g tau<log(2); hence positivity of the untruncated
heat kernel cannot be transferred to arbitrarily small steps after this
cutoff. Positivity at a large time step does not by itself identify the
Hamiltonian limit. This is an explicit step-specific obstruction, not an
exclusion of other finite-spin proofs.

## Literature scope refresh

[Tanaka, arXiv:1507.05362](https://arxiv.org/pdf/1507.05362), sections II,
III and IV A read (model and coefficient-matrix/local-field argument).
The higher interactions there are powers of isotropic pairwise Heisenberg
couplings, rewritten as multipole products. They are not arbitrary
plaquette shift products. The argument requires real reflected crossing
operators with a particular sign; its all-ground-state conclusion uses a
field inequality. No matching decomposition of this gauge Hamiltonian has
been shown. Its theorem is not imported.

[Dey, Banerjee and Huffman, arXiv:2512.14833v2](https://arxiv.org/html/2512.14833v2),
entire main letter read through conclusions, supplementary material not
read. This model has spin-half links and dynamical matter. Its sign-sector
analysis and finite ground-energy comparisons demonstrate why a sector
should be checked explicitly. Adding a magnetic term changes the favored
sector in their finite calculations. It supplies neither the carrier nor a
uniform ordering proof for our matter-free spin-one model. No theorem is
imported; the current title/version differs from the search-index v1 title.

## Next exact obligations

1. Identify which reflection can split the full cubic link/plaquette Hilbert
   space with an admissible product form; charge conjugation symmetry alone
   only pairs sectors and does not rank them.
2. If pursuing a path comparison, preserve integer divergence, the electric
   cutoff, each allowed plaquette jump, and its weight simultaneously. A
   midpoint map that violates any of these does not compare partition sums.
3. Search a geometric sufficient condition or an actual-state route that
   avoids this ranking. Stop reusing the refuted general premise.

## Static midpoint construction on the actual cubic carrier

There is a useful positive statement that uses genuine cubic geometry. On a
full rectangular box, let x,y be integer face fields in {-1,0,1} with
D x = -D y. Put z=x+y. There exist u,v in the same electric cube such that

    D u=D v=0, u+v=z,
    u_p,v_p in {floor(z_p/2),ceil(z_p/2)},
    sum_p (u_p^2+v_p^2) <= sum_p (x_p^2+y_p^2).

Proof: D is a reduced oriented incidence matrix of the dual graph, including
an outside vertex for boundary faces. Each column has at most two nonzero
entries, and two entries have opposite signs. Every square subdeterminant
is 0,+1,-1: expand a column with at most one nonzero entry inductively; if
all columns have two entries, the rows sum to zero. The polytope

    D u=0, floor(z/2)<=u<=ceil(z/2)

is nonempty because z/2 belongs to it, and is bounded. A vertex solves a
nonsingular square system built from rows of D and integer coordinate
bounds. Its determinant is +/-1 by the same argument (adjoining identity
rows preserves this property), so Cramer's rule makes the vertex integral.
Choose that u and set v=z-u. Each coordinate pair is the closest integer
pair with its prescribed sum, which minimizes its sum of squares.
Contractibility makes the resulting integer-neutral fields physical modulo
three. Different global flux constraints must be included on other topologies.

This is an existence statement for configurations. It establishes neither
an injective map of pairs nor preservation of kinetic histories. It therefore
does not compare partition functions or ground energies by itself.

## The kinetic incidence matrix is different

The preceding proof uses D, the cube-face incidence. Kinetic histories use
F, the edge-face incidence. Total unimodularity of D does not imply it for F.
A bounded search in an actual 3x3x3 cubic complex produced a 7x7 submatrix of
F with determinant -2. Translating the same pattern into a 5x5x5 box puts all
seven event edges in bulk stars of size four. With columns in event order,
the selected minor is

    [ 1  1  0  0  0  0  0 ]
    [ 0  1 -1  0  0  0  0 ]
    [ 0  0  1  1  0  0  0 ]
    [ 0  0  0 -1  1  0  0 ]
    [ 0  0  0  0  1  1  0 ]
    [ 0  0  0  0  0  1 -1 ]
    [-1  0  0  0  0  0  1 ].

The event edges (axis; anchor) are

    (z;3,1,1), (x;2,1,1), (x;2,2,1), (y;3,2,1),
    (x;3,2,1), (z;4,2,1), (z;4,1,1).

The selected faces (ordered axes; anchor) are

    (xz;2,1,1), (xy;2,1,1), (xy;2,2,1), (xy;3,2,1),
    (xz;3,2,1), (yz;4,1,1), (xz;3,1,1).

The sparse cochain checker computes each face coefficient directly from
curl_ij a(x)=a_i(x)+a_j(x+ei)-a_i(x+ej)-a_j(x), independently of the dense
product-cell builder. It reproduces the minor and determinant exactly.
The determinant alone concerns an integer-programming shortcut; the next
construction supplies a physically allowed input history for the proposed
midpoint method.

## A valid pair of histories that cannot be exactly balanced by event allocation

BLOCK2_CUBIC_PATH_EXACT_CHECK.json and its self-contained sparse checker give
an initial field x with fifteen nonzero faces, integer charge -1 at cube
(0,1,1) and +1 at cube (1,1,1), and zero flux on the outer boundary. Apply
all seven listed positive edge moves to x in order. Every intermediate face
field stays in {-1,0,1}; the integer charge is unchanged. Append the inverse
moves in reverse order to close this fourteen-event path. In a second copy,
keep -x fixed. Both are legitimate charged-sector histories. The first copy
has no face wrap at any event, so every hopping matrix element has weight t.

A separate dense finite-clock check solves F a=x modulo three, producing an
explicit twenty-edge Z3 coordinate word. It executes all fourteen original
clock moves and verifies the claimed principal fluxes, constant integer
charges, zero branch mismatch, and return to the initial clock word. Thus
physical membership is checked in original coordinates, rather than assumed
from an informal dual diagram.

Consider the specific attempted map that (i) preserves the sum of the two
fields at every time, (ii) allocates each original jump, unchanged, to exactly
one output copy, and (iii) makes both outputs the coordinatewise closest
integer pair at the initial time and after the first seven events. Initially
the sum is zero, so (iii) forces u=v=0. Write epsilon_j in {0,1} for allocating
event j to u. After the seven events, the selected-face sum is
(2,0,2,0,2,0,0). Exact balance there requires

    M epsilon = (1,0,1,0,1,0,0)^T.

The first two equations give epsilon_2=epsilon_3=1-epsilon_1; the next two
give epsilon_4=epsilon_5=epsilon_1; the next two give
epsilon_6=epsilon_7=1-epsilon_1. The last equation gives
epsilon_7=epsilon_1, hence every epsilon_j=1/2. There is no binary solution.
This is also checked by enumerating the 128 assignments. The contradiction
uses only two times; enforcing all intermediate conditions cannot fix it.

This excludes that exact balancing/event-allocation construction on the
actual geometric model. It does not exclude a transformation using unbalanced
neutral initial states, extra or reordered events, a different weighted
coupling, cancellations after summation, or an operator reflection argument.
Any of those needs its own measure/weight comparison. No ground-sector
energy order or phase result follows from the failed construction.

The static positive lemma survives: D admits an integral circulation split,
while requiring that split to follow whole events governed by F is an
additional condition. Treating the two incidence matrices as interchangeable
would have hidden precisely this step.

A search reached [Dey, Hirani and Krishnamoorthy, arXiv:1001.0338](https://arxiv.org/abs/1001.0338),
whose abstract connects total unimodularity to relative torsion, and
[Krishnamoorthy and Smith, arXiv:1304.4985](https://arxiv.org/abs/1304.4985),
whose abstract describes some integral optima even without total
unimodularity. Only the abstracts were read; neither theorem is imported.
The explicit incidence minor and path above are derived directly.
