# Independent reconstruction before author checker/results

2026-09-21. Complete note read at SHA-256
`935163267392a28e53447e940d0e4dd4b9cd07faa7ff146fc8a9740c61ac584d`.
The author checker, results and logs remain unopened. No contextual paper
was used as a mathematical input. This is a check of the supplied finite
construction, not a general quantum-realization classification.

## Orthogonal marked fibers

For K distinct antipodal key pairs, assigning pairs to K matching edges and
choosing the two orientations gives exactly F=K! 2^K marked configurations
over every perfect matching. Distinct marked basis vectors are orthogonal by
the additional Hilbert-space assumption. Thus the normalized fiber-sum map U
is an isometry.

For a declared square, rotation sends a flippable matching to its flip. Both
senses biject the entire source fiber with the entire target fiber. After a
flip the square remains flippable; hence R commutes with P, R^4=I and R is a
permutation, with identity action on configurations where the square is not
flippable. Consequently P U=U P_geom and P(R+R^dagger)U=2U T_geom, counting
each declared square separately. Multiplying by -t/2 gives the claimed -t
geometric off-diagonal entry. The potential intertwines too. A geometric
diagonal observable is constant on fibers, so also intertwines. These are
exact finite-dimensional statements, without a claim that the record rules
provide this orthogonal carrier or coherent state.

Independent enumeration on square, ladder and cube gives respectively
2,3,9 perfect matchings; fibers8,48,384; marked dimensions16,144,3456;
and32,384,18432 enabled two-sense channels. Every rotated record moves one
graph edge; four rotations and the inverse restore the exact labels. Integer
fiber sums directly verify the intertwiner including channel multiplicities.

## Square coherence test

On one four-cycle orbit, H=-(t/2)(R+R^dagger) has eigenvalues -t,0,t,0.
For u=t tau, starting at orbit state0, the two odd amplitudes are each
i sin(u)/2. Therefore their total probability is sin^2(u)/2. The same holds
from state2 and hence for the equal incoherent mixture of0 and2. Starting at
(|0>+|2>)/sqrt(2), the two odd amplitudes instead equal i sin(u)/sqrt(2),
giving sin^2(u). The common on-site potential on a square contributes only
a global phase. At u=pi/2 the probabilities are1/2 and1, respectively.

The check uses exact spectral projectors and verifies the complete propagator
is unitary. The full square fiber is a union of four such orbits. Equal
incoherent weighting does not create the missing off-diagonal coherences;
classical lumping or a uniform classical matching law is not a prescription
for those coherent amplitudes or phases.

## Literal product-map checks

For the stated square, the two configurations(0,1,2,3) and(2,1,0,3) belong
to distinct matchings. Their product overlap is exactly1/2. The literal
sixteen-column product map has rank11 for z/x keys.

More generally take the second real antipodal spinor pair(p,q),(-q,p),
p^2+q^2=1. Summing the eight products over each geometry gives the fiber Gram

    [[1+(p^2-q^2)^2, 1], [1, 1+(p^2-q^2)^2]].

This follows either by exact tensor expansion or from the symmetric pair
vectors Z=|01>+|10> and
X=-2pq|00>+(p^2-q^2)(|01>+|10>)+2pq|11>, whose norms are sqrt(2).
For p=q=1/sqrt(2) the two lifted geometry vectors coincide. For p=3/5,q=4/5,
the diagonal is674/625 and the determinant is63651/390625>0. Their span is
two-dimensional but the map is still nonisometric and nonorthogonal.

If Hermitian H_phys satisfies H_phys V=V H_mark, then
V^dagger H_phys V=G H_mark. Taking the adjoint, using Hermiticity of both
Hamiltonians, gives the necessary condition[G,H_mark]=0. No assumption of
invertibility or isometry of V is needed for this necessity.

For the specified ladder and z/x/y keys I independently assemble physical
product columns and the marked rotation matrices. Each product column has
Gaussian-integer entries divided by4, hence G has Gaussian-integer entries
divided by16. All commutator calculations use integer real/imaginary matrices
and exact rational scaling. In my lexicographic enumeration, states

    eta=(0,1,2,4,5,3), xi=(0,2,3,1,4,5)

have[G,H_mark]_(eta,xi)=-5/16-i/16 for each tested v=0,1,2/3 at t=1.
This entry suffices to refute the specified Hermitian intertwiner for each
of those cases. The independently enumerated indices differ from the note's
declared checker indices; author-index witnesses await comparison.

## Representative phases and positive controls

There is no adjustable relative column phase from choosing one representative
phase per record spinor in this fixed-inventory model. Every eta contains
each record once, so |n_a> -> exp(i theta_a)|n_a> multiplies every product
column by exp(i sum_a theta_a). G, its fiber Gram and the commutator are
unchanged. The checker verifies this for nontrivial exact rational-complex
unit phases. This observation strengthens the stated caution about phases;
it is scoped to the fixed set of records.

If instead the orthogonal configuration basis itself is rephased by a general
diagonal unitary D, consistent coordinates give V'=VD, H'=D^dagger H D and
G'=D^dagger G D. The commutator conjugates by D. Keeping H fixed while making
nonconstant changes to these coherent columns is a different proposed lift,
not merely a change of representative coordinates. Phase choices depending
on sites/configurations are not the single-spinor-per-record convention in
the supplied map.

Nonorthogonality or dimension excess alone does not forbid a Hermitian lift.
On a single square every allowed marked configuration is flippable, so its
rotation is an unconditional tensor-factor permutation on the physical
Hilbert space. The separate positive control verifies exactly P_phys V=VR,
H_phys V=V H_mark and[G,H_mark]=0 there, even with the rank11 map. It also
checks arbitrary consistent configuration-basis rephasing on this example.
Thus the ladder failure is a test of the supplied conditioned operator and
map, not an assertion that all nonorthogonal constructions fail.

## Boundary

All independent runs passed on their first execution, with empty stderr.
The positive orthogonal-fiber construction, missing-coherence observation,
and conditional literal-map obstruction are mutually consistent. No general
quantum no-go, operational key-recognition claim, carrier preparation,
low-energy phase, hydrodynamic limit or photon identification is supplied.
The two literature paragraphs remain contextual claims not checked here.
No mathematical defect has been found before author-source comparison.
