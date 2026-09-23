# Independent reconstruction: the post-birth ring spectrum

For every L>=3 the entire specified H2 sector admits an explicit diagonalization.
It is two hard-core particles on the L-site B ring, coupled at the boundary to a
weighted cyclic shift of the L+2-record charge word. For L=4 this gives twelve
flat modes at -4 and twenty-four dispersive modes in each generic Fourier fiber.
Both prescribed formation outputs put exactly one half of every normalizable
state in the physical flat eigenspace. Their H2 variance is exactly two, so the
formation map does not itself prepare a single energy or the lowest band.
The coherent instrument's remaining spectral distribution can depend on the
initial field coherence. These are statements about the supplied conservative
H2 operator; they are not a subsequent-birth waiting law.

This is a pre-author-source independent reconstruction, not formal audit,
publication review or frontier authorship delegation. **Prior exposure:** I
checked the L=3 six-site path/Bessel example in the preceding campaign. That
case and its scope were known. The general-L reduction, L=4 spectrum and
formation-output distributions below were reconstructed from the neutral
model and checked with new code. No fourth-campaign author note, runner,
result, checkpoint or registry was read.

## 1. Model and coordinates

Orient the 2L ring edges e=(e,e+1), take A even, and impose

    E_e-E_(e-1)+1_(e even)-q_e=0.

A charge c hopping in the positive orientation shifts E_e by -c. T contains
minus this hop and its adjoint. P requires all A sites occupied. At record
number L+2 and total charge L there is exactly one minus record and L+1 plus
records. Exactly two B sites are occupied, and the other L-2 B sites are vacant.
Put M=L+2 and index B sites by j, with physical position 2j+1.

A P basis state is specified by:

- an unordered occupied B pair C={x,y}, 0<=x<y<L;
- r in {0,...,M-1}, the position of the minus record in the occupied-site word
  read from physical site 0 upwards;
- f=E_(2L-1), the independent integer field circulation.

Gauss fixes every remaining E uniquely. There is no field cutoff. Thus the
physical Hilbert space is `ell^2(Z) tensor C^(choose(L,2)) tensor C^M`, and
its angle fibers have dimension `M choose(L,2)`; it is 36 for L=4.

Every first hop from P empties an A site into a vacant B neighbor. Returning
that same record contributes one diagonal term to `-P T Pi1 T P`. Each of the
L-2 vacant B sites has two occupied A neighbors, giving the constant diagonal
`-c_L`, where `c_L=2(L-2)`. The only other return to P moves the occupied other
B neighbor into the newly empty A site. This translates a B occupancy by one
contracted-ring step and preserves the order of the two transported records.
Each continuation has coefficient -1 and one intermediate state. Therefore

    H2=-c_L I-C,

where C is the adjacency of these B-occupancy moves, including their charge and
field transport. This derivation accounts for all two-hop paths and their
multiplicities; there is no endpoint-only replacement of the actual T.

## 2. Boundary charge shift and complete spectrum

Use the Fourier convention `hat psi(theta)=sum_f psi_f exp(i f theta)` and
measure dtheta/(2pi). A bulk B hop leaves the ordered charge word unchanged.
The boundary move B0 -> B_(L-1) moves the charge initially at physical site 0
around the cut: it rotates the record word left once and shifts f by that
charge. In the r basis its operator is

    R_theta |r> = exp(i theta [1-2 delta_(r,0)]) |r-1 mod M>.

Its M-th power is `exp(i L theta) I`, because the total record charge is L.
Let

    phi_j(theta)=(L theta+2pi j)/M,       j=0,...,M-1,
    v_j(r)=M^(-1/2) exp(i r[phi_j-theta]).

Then `R_theta v_j=exp(i phi_j) v_j`; these M vectors form an orthonormal
basis. Hence the charge-word degree of freedom is completely diagonalized,
not replaced by its mean charge.

In sector j, C is the adjacency of two hard-core particles on the B ring,
with boundary hop 0 -> L-1 carrying exp(i phi_j). Its normalized eigenvectors
on x<y are the determinants

    w_mn(x,y)=[exp(i(k_m x+k_n y))-exp(i(k_n x+k_m y))]/L,
    k_m=(2pi m+pi+phi_j)/L,       0<=m<n<L.              (1)

The pi in (1) is essential: a boundary move of two ordered hard-core particles
changes the determinant's ordering sign. It is a mathematical coordinate
representation, not a claim of physical fermion statistics. The determinants
are orthonormal and directly satisfy every bulk and boundary equation.
Multiplying them by v_j gives the complete P eigenbasis, with

    E_jmn(theta)=-2(L-2)-2cos(k_m)-2cos(k_n).             (2)

This proves the general-L spectrum. It also supplies a full propagator by
multiplying each vector by `exp(-iu E_jmn)` in a fiber and Fourier-inverting.
An eigenvalue plot alone is not being used to infer this representation.

As theta varies, the physical spectrum is the interval

    [-2(L-2)-4cos(pi/L), -2(L-2)+4cos(pi/L)].             (3)

To see coverage, choose momentum difference one, vary the twist through a
complete circle, and range over the common momentum label. This covers the
cosine's complete range. Every other pair has no larger amplitude.
For even L, pairs n-m=L/2 have opposite momenta and give a flat eigenvalue
`-2(L-2)`, with generic fiber multiplicity `M L/2`. All other branches are
nonconstant analytic cosines. Consequently only this flat value can be a
point eigenvalue on the physical direct-integral space. The other spectral
parts are absolutely continuous; isolated turning points do not create
normalizable eigenvectors. For odd L there is no flat point spectrum.
In particular H2 is strictly negative with a uniform gap from zero for L>=4;
this is an energy statement, not a dissipative gap or a formation-dark claim.

There are also exactly L connected physical basis-state components. The
invariant is

    I=f+r modulo L.                                    (4)

A boundary rotation with r>0 changes (f,r) by (+1,-1). At r=0 it changes
(f,r) to (f-1,M-1), whose sum changes by M-2=L. Bulk steps leave both unchanged.
The two-particle B configuration graph is connected. At C={0,L-1}, moving the
particle at 0 successively to L-2, then the particle at L-1 to 0, then the
particle at L-2 to L-1 is a legal closed configuration loop with one boundary
crossing. It generates R or its inverse. M repetitions restore r and shift
f by L. This realizes every state consistent with (4), proving sufficiency
of that invariant. For L=3 these components reduce to the previously checked
infinite paths; for larger L they need not be paths.

## 3. The actual formation outputs and their spectral measures

Before the mark, all A records are plus and all B sites vacant, so Gauss forces
all links to have the same integer f. Let the arbitrary normalizable field
state have amplitudes psi_f. The chosen effective resolved mark has exactly
one permitted old-record destination: site 2L-1. The hop raises E_(2L-1) by
one, and the plus-at-0/minus-at-1 birth raises E0 by one. The other outward
hop occupies site 1 and blocks this mark.

The resolved output has occupied B pair C0={0,L-1}, minus index r=1, and free
flux f+1. The reverse charge orientation has the same B pair and free flux,
but minus index r=0 and E0 is lowered instead. Both unit-rotor amplitudes are
one. Thus the normalized fiber outputs, apart from their common factor
`exp(i theta) hat psi(theta)`, are

    resolved: |C0> tensor |1>,
    coherent: |C0> tensor (|0>+|1>)/sqrt(2).             (5)

The coherent normalization follows from the two orthogonal charge outputs;
it retains the relative sign of the stipulated unnormalized j_++j_-.

The squared charge-mode overlap at C0 is

    a_mn=4/L^2 sin^2(pi(m-n)/L),    sum_(m<n) a_mn=1.

The spin-sector weights are

    b_j^resolved=1/M,
    b_j^coherent(theta)=[1+cos(phi_j(theta)-theta)]/M.    (6)

For a pure field let g(theta)=|hat psi(theta)|^2, normalized in dtheta/(2pi).
For any bounded measurable F, the complete normalizable-state answer is

 <F(H2)> = integral g(theta) sum_(j,m<n)
              b_j(theta) a_mn F(E_jmn(theta)) dtheta/(2pi).       (7)

For a mixed initial field, replace g by its angle-observable probability
density. A trace-class density has an absolutely continuous such measure.
No smoothness, energy moment or sharp-angle preparation is needed. Degenerate
eigenvalue weights in (7) are summed; individual basis weights inside a
degenerate eigenspace need not be unique.

A fixed theta fiber is not a normalizable state. Formula (7), not one chosen
fiber, is the spectral distribution of the specified physical preparation.
For even L its flat spectral mass is exactly

    sum_(n-m=L/2) a_mn = 2/L,                           (8)

for both instruments and every allowed initial field. Nonflat branches crossing
the same energy at isolated theta values add no physical point mass.

For a single integer-flux input, g=1. The resolved spectral law simplifies to
an arcsine mixture about the center -2(L-2): for d=1,...,L-1 use weight
`(2/L) sin^2(pi d/L)` and radius `4|cos(pi d/L)|`, interpreting radius zero
as a point mass. The coherent law is identical for this input. One proof of
the latter statement is (4): its r=0 and r=1 branches at the same f lie in
different invariant components, so their spectral cross term vanishes.
Each branch separately has the same diagonal spectral measure. The same holds
for mixtures diagonal in integer flux. It does not hold for every coherent
superposition of field circulations.

## 4. Explicit L=4 result and band-preparation limits

Here M=6 and the generic fiber spectrum consists of

    E_flat=-4,                   multiplicity 12,
    E_l(theta)=-4-2sqrt(2)cos((4theta+2pi l)/24),
                                  l=0,...,23.          (9)

Equivalently the exact characteristic polynomial is

 det(e I-H2(theta)) = (e+4)^12 2^13
       [T_24((e+4)/(2sqrt(2)))-cos(4theta)].            (10)

For a direct algebra check, the six-dimensional charge block at boundary
phase z has characteristic polynomial

    x^2[x^4-8x^2+8-4(z+z^-1)].

Multiplying it over `z=exp(i phi_j)` gives (10), using `T6(T4)=T24`.
Each generic dispersive mode has resolved weight 1/48; each of the twelve
flat basis modes has resolved weight 1/24. The coherent weights follow (6).
Both physical outputs have an atom of weight one half at -4. For a single
flux input the entire law is exactly

    (1/2) delta_-4 +(1/2) Arcsine(center=-4,radius=2sqrt(2)).      (11)

The remaining half is not silently discarded. At theta=0, two dispersive
modes cross -4, so the *fiber* mass at that energy is 13/24 for the resolved
output and 7/12 for the coherent output. Neither number is the point mass
of a normalizable rotor state; that remains 1/2. This distinction is checked
both by full-matrix diagonalization and the explicit mode weights.

For a generic fiber the lowest eigenvalue is simple and has resolved overlap
1/48. Hence every normalizable resolved output has weight exactly 1/48 in
the direct-integral projection onto the lowest fiber branch. The coherent
weight in that projection is at most 1/24. Exceptional crossing angles have
zero weight for a normalizable input. Thus a lowest-band preparation is a
substantial additional selection, not a consequence of this formation mark.
The flat spectral subspace is embedded among dispersive branches; it is not
a separated energy sector supplied by an automatic spectral gap.

For every L>=3 and both outputs, independently of the initial field,

    <H2>=-2(L-2),       Var(H2)=2.                      (12)

The centered operator takes C0 to two orthogonal new B-pair configurations,
each with norm one. This proves (12) directly. In particular no choice of the
initial field within the stated mark family makes the output an exact H2
eigenstate or drives its absolute energy variance to zero.

The L=4 coherent fourth centered moment illustrates the retained field
information more finely. In one charge block,
`<C^4>_(C0)=12+2(z+z^-1)`. Combining (6) yields

    <(H2+4)^4>_coherent
      =12+2 integral g(theta) cos(theta) dtheta/(2pi),
    <(H2+4)^4>_resolved=12.                             (13)

The physical inputs `( |f=0>+|f=1> )/sqrt(2)` and
`( |f=0>-|f=1> )/sqrt(2)` therefore give 13 and 11 for the coherent output,
respectively; a single flux gives 12. These values were also computed by
untruncated physical-state hopping, without Fourier matrices. Treating the
coherent mark as a classical mixture would miss this difference.

## 5. Time and subsequent-formation boundary

The supplied microscopic scaling and the previously checked fixed-volume
approximation identify H2 motion on compact fast time
`u=delta tau/epsilon^2`. On that scale the bounded fourth-order and effective
birth terms have prefactor epsilon^2 at fixed L. Combining the inherited
O(epsilon) microscopic approximation with ordinary bounded-generator Duhamel
therefore gives the conservative H2 limit on such compact intervals. This
uses the already checked full-W theorem; it does not reuse the L=3 special
two-block proof where W could only be zero or one.
The comparison starts from the specified normalized effective-output state;
no uniform conditioned microscopic stopping-time theorem is asserted here.

The statement is not uniform on nonzero fixed laboratory intervals. The
present spectral calculation does not give a later no-event Hamiltonian,
averaged birth generator, repeated-birth law, local vacancy-spreading theorem,
or a large-volume field theory. Nor does a flat H2 component mean that the
formation jumps vanish on it.

A decisive check prevents importing the six-site no-further-birth conclusion.
For L=3 the one remaining vacancy makes every next pair birth zero. For L=4
the stated first output has vacancies at physical sites 3 and 5. The A record
at site 4 can hop into one and permit a birth on the other adjacent edge.
The exact effective resolved-channel loss at that particular initial output
is 4 kappa, for either specified first instrument; every resulting state has
eight records. This is only an initial operator calculation. It does not
make the later first-success clock exponential or prove completion under the
full interacting generator. No subsequent-formation author source was read.

## 6. Independent controls, failures and source seal

The new runner directly enumerates P charge words, legal microscopic hops,
integer cut-flux shifts and all two-hop returns. Its complete matrices are
compared against the independently derived product eigenvectors (1), including
phases and overlaps. L=3,4,5,6,7 at three angles were checked; the largest
full-eigenvector residual is below 2.5e-15. Numerical eigenvectors are not used
to invent the analytic spectrum. The general proof is the explicit operator
reduction above, not extrapolation from those sizes.

Additional decisive controls include:

- Exact SymPy charge-block characteristic polynomial and the full 36-by-36
  microscopic characteristic polynomial at theta=0.
- Untruncated integer-field formation moments through order six at L=3,...,6,
  including the coherent-field countercontrols in (13).
- Direct full-matrix L=4 flat-energy and lowest-band overlaps, including the
  exceptional theta=0 values.
- The proposed integer invariant and finite flux-mod-L connectivity at
  L=3,...,7; the analytic loop argument proves the unrestricted statement.
- Removing the required fermionic boundary pi produces an eigenvector residual
  1.732..., decisively failing the correct microscopic eigenproblem.
- The L=3 zero-next-birth and L=4 nonzero-next-birth initial operator controls.

The first run failed at a SymPy symbol-identity comparison: `charpoly` created
an unassumed x while the comparison x had `nonzero=True`. Its computed
coefficients were already the stated polynomial. Declaring x without assumptions
repaired that helper issue without changing coefficients, numerical thresholds
or the spectral formulas. The exact failing source, real stderr and command
receipt are preserved, with the diagnosis. Later scientific and provenance
runs passed, and their complete outputs and actual timed receipts are kept.
No failed probe or negative finding was removed.

The unchanged permitted model and prior-review identities are recorded in
SOURCE_IDENTITIES.json, including the previous L=3 exposure. No external
literature theorem is imported. Only the assigned independent directory was
written. The fourth-campaign author spectrum packet remains unopened.

This frozen reconstruction is ready for a source-bound comparison. It supplies
an exact finite-ring spectrum and formation-output spectral measure under the
specified model; it supplies no native-axiom, photon, thermodynamic, later-event,
physical-fermion or TOE conclusion. PRE_COMPARISON_SEAL.json binds the complete
source and independent evidence packet.
