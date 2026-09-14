# Local reference encodings: an exact graph map and a fermionic exchange boundary

**Status:** proposed_retained
**Date:** 2026-09-14
**Claim type:** bounded_theorem

Author-proposed conditional mathematics; actual source status conditional-support.
Independent scientific review is pending. This is neither a general obstruction
to fermions on qubits nor an axiom-forcing result.

A controlled-Pauli circuit explicitly connects the open no-reference-bond and
reference-bond encodings, preserving every logical phase and returning the
added ancillas under its inverse. On the square it supplies the previously
missing map between 76 and 80 edge qubits. Separately, the specified bounded
local hopping grammar fails an actual six-port two-particle exchange. Changing
occupation-basis phases or static edge flux cannot fix that grammar. A general
commutator argument gives support, weight, approximation and perturbation-order
bounds for any representative under an encoding with local occupation-bit
loaders. These results separate a constructive preparation transfer from the
remaining fermionic-operator obligation.

**Runner:** [self-contained primary](../scripts/local_reference_fermion_encoding_obstructions_and_constructive_graph_isometries_2026_09_14.py).
**Receipt:** [canonical cache](../logs/runner-cache/local_reference_fermion_encoding_obstructions_and_constructive_graph_isometries_2026_09_14.txt).
**Review:** [author record](../.claude/science/physics-loops/toe-charged-phase-20260914/deliveries/block7/REVIEW_HISTORY.md).

## Premises and quantified claims

| Supplied object | Derived statement | Scope limit |
|---|---|---|
| Isometry E and physical Hermitian unitary representatives of occupation-qubit X | Sharp operator-norm support obstruction for a specified CAR hopping | A local representative of a qubit X is an explicit hypothesis, not a property of every fermion encoding |
| Commuting disjoint local loaders and a fixed cell order | Interaction-weight bound and conditional perturbation-order selection rule | Direct compression or an analytic fixed-box expansion with invariant unperturbed resolvents |
| Open L^d grid, d>=2, with every nearest-neighbor stream available | An ordering-independent diverging weight/radius lower bound | One dimension and a special indivisible global update word are not excluded |
| Fixed six-port loop/D code, directed bounded operand grammar and occupation identification | Exact exchange mismatch, invariant under occupation-preserving rephasing | Changing the operator grammar, code constraints or physical identification is a different route |
| BKSF graph, selected short paths and positive-X ancillas | Signed local Clifford edge-addition isometry with returned ancillas | Bounded-range abstract edge-qubit gates; physical-site routing and autonomous genesis are separate |
| Ordinary fixed-parity BKSF or one distinguished reference mode | Explicit algebraic alternatives preserving local even matter operators | These are known/supplied encoding architectures, not framework-selected particle constructions |

All Hilbert spaces, CAR operators, graph edges, constraints, occupation maps,
initial ancilla states and circuit gate sets are supplied model data. Circuit
layer number is not physical time. No unmerged campaign result is a scientific
premise. The note gives its own operator proofs and reconstructs all scientific
checks without importing historical runners. The general Jordan-Wigner/BKSF
principles and Clifford changes of fermion encoding have prior art; the repo
review object is the explicit missing graph map and the quantified failure of
the specified local-loader/operand composition.

The state comparison uses current main
`b8c9d9d819911c5f3fec98b23d53355e7ff8c8bf`. The closest current notes are
`CYCLE703_BKSF_PATCH_TABLEAU_COVARIANCE_NOTE_2026-07-25.md`,
`CYCLE703_LOCAL_GAUSS_HELD_PATCH_GRAMMAR_ADDENDUM_2026-07-25.md`, and
`CYCLE703_OPEN_BKSF_STABILIZER_PREPARATION_NOTE_2026-07-25.md`, all under
`docs/work_history/repo/review_feedback/`. Their relevant graph and logical
operator definitions are restated below. Their historical PASS counts and
preparation algorithms are not treated as rerun evidence or scientific authority.

## 1. A representation-independent commutator test

Fix M fermion modes and their occupation basis with an explicit total order.
Identify that basis with M qubits. Let X_k be the ordinary occupation-bit flip
in this tensor-product basis, not the fermion Majorana. Write B_k=Z_k=1-2n_k.
For i<j the Hermitian unit-amplitude hopping is

    T_ij = c_i† c_j + c_j† c_i
         = (X_i X_j + Y_i Y_j)/2 product_(i<k<j) Z_k.

It has norm one and T²=(1-Z_i Z_j)/2. For every strict intermediate k,
{T,X_k}=0, while [T²,X_k]=0. This is an exact occupation-basis identity.

Let E: H_log -> H_phys be any isometry. Suppose a Hermitian physical unitary
Xbar_k obeys Xbar_k E=E X_k. Then also E†Xbar_k=X_k E†; no preparation or
stabilizer assumption is used. If O is any physical operator commuting with
Xbar_k, its compression A=E†OE commutes with X_k. Hence

    2 = ||[T,X_k]|| = ||[T-A,X_k]|| <= 2 ||T-A||,
    ||E† O E-T|| >= 1.

This remains true if O leaks from the code. In particular every exact
representative of T must have support intersecting supp(Xbar_k). Multiplying
by stabilizers, adding off-code terms, or using a non-Pauli representative
cannot evade this test at fixed E. A zero operator attains the error lower
bound, so it is sharp for the commuting linear operator class.

For U_theta=exp(-i theta T),

    U_theta=I+(cos(theta)-1)T²-i sin(theta)T,
    ||[U_theta,X_k]||=2|sin(theta)|.

Any compressed operator commuting with X_k therefore has approximation error
at least |sin(theta)|. At integer multiples of pi that particular witness
vanishes; no support conclusion is claimed from it there.

## 2. Joint symmetry sectors give a weight and perturbation-order test

Let K be m strict intermediate modes, with commuting Xbar_k. Define the
joint odd-sector map on operators

    D_k(O)=(O-Xbar_k O Xbar_k)/2,
    Q_K = composition_(k in K) D_k.

The second line composes linear maps; it is not a product of output matrices.
Each factor is a norm contraction and the factors commute. The logical
version obeys Q_K(T)=T and commutes with compression through E.

If the supports of the m loaders are pairwise disjoint, an operator on fewer
than m physical qubits misses at least one support. Its Q_K component is
zero. By linearity this holds for an arbitrary sum of such operators,
including terms distributed throughout the volume. Consequently

    inf_H ||E† H E-T|| >= 1

when H is a sum of terms of physical support size less than m. No coefficient
bound is needed, and the conclusion concerns direct compressed action. For
Pauli loaders, this can also be checked as a syndrome: each term of weight w
has odd commutation with at most w disjoint loaders. At least one term of an
exact representation must therefore have weight >=m. It is not enough that
the union of many low-weight terms reaches all intervening cells.

For overlap multiplicity b (every physical qubit belongs to at most b selected
loader supports), replace m by ceil(m/b). This does not assert optimal weight.

A conditional perturbation-order corollary: suppose H0 commutes with all
Xbar_k, P=EE† is a degenerate isolated H0 band, and V is a sum of terms each
supported on at most w qubits. Reduced resolvents of H0 and P commute with
all loaders. Every monomial containing n perturbation factors V, separated by
such resolvents/projectors, has zero joint-odd compression when n w b < m.
The reason is its commutation syndrome, which is the XOR sum of those of its
V factors, and has size at most n w b. The statement covers an analytic
finite-box effective-Hamiltonian expansion whose nth coefficient is a sum of
these monomials, including folded counterterms. It does not prove convergence,
control a thermodynamic gap, bound the first nonzero coefficient, or exclude
nonperturbative changes in the encoded low-energy space.

## 3. Applying the test to the exact Cycle703 logical loaders

A supplied connected graph has N coarse cells, each with six matter vertices
(x,a), a=0..5, and one reference (x,r). There are the twelve octahedral intra-cell
matter edges, six reference spokes, and the nearest-neighbor stream edges
(x,2mu+1)--(x+e_mu,2mu). Optional parallel reference bonds are considered
separately. Put a physical qubit on each graph edge. With a local incident
edge ordering define

    B_v = product_(e incident v) Z_e,
    A_uv = epsilon_uv X_uv
           product_(e preceding uv at u or v) Z_e.

The phase convention is i^p X^x Z^z, epsilon_uv=+1 for u<v and -1 for u>v.
Direct Pauli multiplication gives A²=B²=I and commuting B rows. A_uv
anticommutes with exactly B_u,B_v; distinct A edges anticommute exactly when
they share one endpoint. In a loop the endpoint signs cancel, so each loop
word commutes with every A and B. The code fixes
all independent loop operators i^ell product A along the oriented loop to +1,
and D_x=B_(x,r) product_a B_(x,a)=+1. With all loop characters fixed the
connected even-BKSF code has 7N-1 logical qubits before D and 6N after the N-1
independent D constraints. To see the ranks without a finite census, choose
any spanning tree. Each fundamental-cycle Pauli has the X of its unique
chord, so these cycle rows are independent and cannot multiply to -I.
Vertex B rows are the connected graph's incidence-star rows, whose only
binary relation is the product over every vertex. A product of D rows is
the B-star product over the union of their complete cells; it is identity
only for the empty or full connected vertex set. Thus the D increment is
N-1. Cycle rows with nonzero X components cannot cancel into the pure-Z D
span. Adding all B gives full physical rank, so the all-B vacuum is unique.
The following local logical operators are the phase-oriented ones used in
the current-main source:

    Zbar_(x,a)=B_(x,a),
    Xbar_(x,a)=-i [product_(b=a..5) B_(x,b)] A_((x,a),(x,r)).

They are Hermitian unitaries, commute with loop/D stabilizers, and obey the
canonical M=6N qubit Pauli relations. For a<b in one cell the two A words
anticommute through their shared reference, while the suffix of Xbar_a
contributes one further anticommutation through B_b; the signs cancel.
Across cells the words commute. Each Xbar flips precisely its own matter B
and the reference B, preserving D. Its suffix anticommutes with its A, so
multiplication by -i makes it Hermitian with square I. Their common B=+1
vacuum and logical-X products are normalized, orthogonal (distinct B labels),
span the 2^(6N)-dimensional code and fix E up to a common phase. This is a
mathematical state definition;
a local circuit preparing E has not been inferred.

This formula follows directly in extended Fock space: each cell is mapped
as |n_0...n_5> -> |n_0...n_5, sum n_a mod 2>. Every extended cell has even
parity. The displayed suffix cancels the intra-cell Jordan-Wigner phase,
and the product of even preceding cells cancels inter-cell signs. Thus Xbar
acts as the ordinary matter-qubit X at fixed phases. BKSF subsequently maps
the extended even algebra into the edge code.

For the actual edge order (all intra-cell octahedral edges, then spokes in
mode order, then stream/reference bonds), the a=5 loader simplifies, up to
its fixed Hermitian phase, to

    Xbar_(x,5) = Y_(spoke x5) product_(a=0..4) Z_(spoke xa)
                Z_(outgoing +z matter stream),

with the last factor absent at an open +z boundary. The sign is positive in
the displayed Pauli convention, as direct multiplication shows. Its support
consists of
six own-cell spokes and at most one +z stream edge. These selected supports
are pairwise disjoint for distinct cells. A stream edge is used by the mode-5
loader only at its +z source, and reference bonds never enter this formula.
They have bounded geometric radius (at most one coarse-cell spacing).

Order whole cells arbitrarily and six modes consecutively within each cell.
A stream between cells at indices a<b has m=b-a-1 complete intermediate
cells. Its two fermionic Pauli summands and full T anticommute with the selected
mode-5 loader in each such cell. U_theta has a nonzero commutator with that
loader whenever sin(theta) is nonzero.
Sections 1-2 apply with overlap multiplicity one. In particular the exact same-E hopping requires
at least one physical Pauli term of weight m. No search over stabilizer
representatives can remove this exact lower bound.

This statement applies to the current phase-oriented E on either the
no-reference-bond graph or a reference-bond graph carrying these same logical
loaders. A rank equality between different graphs alone does not identify
their E. Replacing E with one whose occupation-flip representatives are
nonlocal changes a load-bearing hypothesis.

## 4. Uniform family consequences, with all geometric assumptions stated

The geometric argument holds for d>=2 under the stated local-loader and
nearest-neighbor-stream hypotheses. For the actual six-port graph take d=2
or 3. Use open L^d boxes with integer L>=2 and all nearest-neighbor cell
bonds represented by at least one specified fermionic stream. Let p(x)
be any bijection from cells to {0,...,L^d-1}. Pick cells with minimum and
maximum index and a shortest grid path between them. Its length is at most
d(L-1). The triangle inequality for index differences implies that some
nearest-neighbor edge obeys

    |p(x)-p(y)| >= ceil((L^d-1)/(d(L-1))).

Thus m>=ceil((L^d-1)/(d(L-1)))-1 for at least one stream. With the actual
disjoint loaders, some necessary Pauli term has weight Omega(L^(d-1)). This
elementary bound is not advertised as the optimal graph bandwidth theorem.
It holds for every total cell order, including Hamiltonian-path orders.

For a support-radius bound assume each selected loader lies within distance
r of its cell center and a proposed hopping representative lies within
distance R of its two endpoint cells, using the max norm. Every intermediate
cell center must then belong to the union of two radius R+r boxes. Therefore

    m <= 2 [2(R+r)+1]^d,
    R >= ((m/2)^(1/d)-1)/2-r.

Together these exclude a uniformly bounded R for any ordering when d>=2.
The weak general radius exponent is (d-1)/d; it is not silently improved to
linear. For the explicit two-row snake ordering
(0,0),...,(L-1,0),(L-1,1),...,(0,1), the adjacent endpoints (0,0),(0,1)
have every other row cell in between. A loader at (L-1,0) forces
R>=L-1-r. This provides a linear-radius witness for that ordering. The same
slice is present in the standard higher-dimensional snake.

One spatial dimension is a live control: nearest-neighbor cells can be
consecutive, so m=0. The theorem does not foreclose a local one-dimensional
Jordan-Wigner hopping. Disconnected graphs and missing streams also do not
satisfy the quantified grid premise.

## 5. A local circuit cannot hide the missing long-range action

Also suppose a bounded physical Zbar_i represents the endpoint Z_i. For a
strict intermediate k,

    ||[U_theta† X_k U_theta, Z_i]||=2|sin(2 theta)|.

Indeed U†X_kU=[I+(cos(2theta)-1)T²+i sin(2theta)T]X_k and only the T term
anticommutes with Z_i. Let a physical depth-D circuit W have gates of range
a in a metric where conjugation expands support by at most a per layer.
If dist(supp Xbar_k, supp Zbar_i)>Da, their physical evolved commutator is
zero. If ||W E-E U_theta||<=eta, compression of evolved Xbar differs from
U†X_kU by at most 2eta, so eta>=|sin(2theta)|/2. At theta=pi/4 this is 1/2.
For exact synthesis, D a must reach the loader/endpoint separation. This
bound permits gates throughout the volume; it is not an assumption that W
acts only near the target bond. A fixed ancilla state can be included in E;
returned-work unitary circuits obey the same light-cone statement. Global
classical feed-forward or unbounded-range gates change the circuit premise.

If an encoding itself is prepared by a range-a depth-D_E unitary from
independent logical input qubits and a fixed ancilla state, its physical
logical loaders have radius at most D_E a (up to placement radius). Applying
the preceding support theorem yields a tradeoff between encoding depth and
the geometric range of exact hopping representatives. This is a conditional
tradeoff, not a claim that every successful fermion encoding has local loaders.

## 6. Exchange tests separate local pair shadows from actual CAR

For distinct cells x,y and modes u=(x,a), v=(y,b), the actual directed
bounded rule is completely specified by

    S_y = product_(s != b) B_(y,s),
    L_xy = -A_(r_x,u) A_(u,v) A_(v,r_y),
    K_uv = A_(u,v) L_xy = A_(r_x,u) A_(v,r_y),
    Hloc_uv = -S_y (1-B_u B_v) K_uv/2,
    Floc_uv = (B_u+B_v)/2 + Hloc_uv.

The path phase in L_xy is i²=-1. K is a Hermitian involution, anticommutes
with B_u and B_v and the two reference B operators, and commutes with every
other B. It commutes with S_y and all loop/D constraints. Therefore
Hloc²=(1-B_u B_v)/2, the two terms of Floc have orthogonal support, and
Floc²=I on the full physical space. This supplies the unitary factors used
in the exchange and error bounds below.

For x preceding y in the chosen cell order, substitute
E†A_((x,a),r_x)E=-Y_(x,a) product_(s>a) Z_(x,s) into K. The two target-cell
suffixes cancel against S_y, and (1-Z_u Z_v)Y_u Y_v/2=(X_u X_v+Y_u Y_v)/2.
It follows directly that

    E† Hloc_uv E = product_(x<z<y) product_s Z_(z,s) T_uv.

Thus the omitted complete-cell parity is an exact logical difference, not
merely a large representative found by a search. The actual directed formula
is used without reordering its source and target in the closed exchange test.
For intra-cell turns use T_uv=(i/2)A_uv(B_u-B_v) and
F_uv=(B_u+B_v)/2+T_uv, with the same unitary identity.

The q=1-per-cell reduction maps |n_x> to |n_x,n_x> in extended Fock space.
Its local even pair flip is the commuting encoded qubit flip. The locally
lifted directed hopping therefore has the hard-core qubit action b_y† b_x,
with no intervening parity string. This reduction is a diagnostic comparator,
not a statement that the full six-port graph is identical to a one-port graph.

On four cells ordered 0,1,2,3 around a ring, start with occupation {0,2} and
apply directed moves in this chronological order:

    0->1, 2->3, 1->2, 3->0.

Every move has one occupied source and empty target. The final occupation is
again {0,2}, but the two particles have exchanged. CAR gives amplitude -1;
the local pair-shadow/hard-core update gives +1. Both initial and final
states have even particle number. Thus restricting this same flawed grammar
to even matter parity does not fix it.

A one-particle path 0->1->2->3->0 has amplitude +1 in both representations.
Under arbitrary static complex edge phases t_yx of modulus one, both paths
pick up the same product around the oriented ring. Their ratio is still -1
for fermions and +1 for the pair shadow. A fixed magnetic flux therefore
cannot repair the relative statistical phase. The same comparison can stay
entirely at particle number two by placing a stationary second particle in
an otherwise unused pendant cell for the unexchanged circuit; that particle
has no worldline exchange with the moving one. Arbitrary diagonal rephasing
of occupation states also cancels on each closed configuration path. Neither
edge phases nor a global occupation-basis phase convention repairs the pair
shadow's multi-particle composition. A dynamical occupation-dependent gauge
field or nonlocal parity string is a different route.

For the actual six-mode graph, take cells 0=(0,0), 1=(1,0), 2=(1,1),
3=(0,1), with empty unmentioned modes, initial particles (0,1),(2,0), and
these eight chronological mode moves:

    (0,1)->(1,0), (2,0)->(3,1), (1,0)->(1,3), (1,3)->(2,2),
    (3,1)->(3,2), (3,2)->(0,3), (2,2)->(2,0), (0,3)->(0,1).

The actual directed local-D stream Pauli words and bare intra-cell even
hopping words decode to +1 on this closed path, while CAR gives -1. The
one-particle comparator starts at (0,1) and follows the same directed moves
in the cyclic order needed to remain on occupied sources; it gives +1 for
both. Every move has one occupied source and an empty destination. The
number-diagonal part (B_u+B_v)/2 of each FSWAP vanishes on those states, so
the same witness applies to the full FSWAP factors; for pi/2 hopping rotations
the eight common -i factors multiply to +1. Arbitrary fixed phases on those
same directed edges have identical products in the two paths.

This was checked by independent integer CAR occupation actions and by exact
phase-aware decoding of the supplied physical A/B formulas through loop/D
stabilizers and all logical X/Z rows. The directed source/target orientation
is preserved even on the closing 3->0 bond. The one-particle success is
therefore insufficient for the actual multi-particle compiler, not merely
for an unrelated one-mode toy.

### Occupation-preserving re-encoding does not fix this fixed grammar

In the fully loop/D-fixed code every complete matter-occupation label has a
one-dimensional eigenspace: adding all matter B rows to the code stabilizers
has full physical rank. Hence any other isometry into this same code that
preserves all occupations differs from E only by a diagonal phase on each
occupation state. The closed exchange amplitude is unchanged by those phases.
The actual bounded local grammar therefore fails for every such isometry,
not just the displayed suffix-loader chart. This statement concerns the fixed
grammar on the fixed code; it is not a theorem against all local encodings.

The mismatch is finite and robust. Compare the eight physical FSWAP factors
on the exchange path with their eight fermionic targets. Their product acts
with opposite signs on the declared starting state. If each factor had
intertwining error <=epsilon under one occupation-preserving isometry, the
unitary telescoping bound would give 2<=8epsilon, so epsilon>=1/4 for at
least one factor. Both endpoints of the witness are in even matter parity.
Allowing arbitrary fixed directed-edge phases does not remove the obstruction:
the two paths use the same eight directed moves, so the same phase lambda
multiplies both physical closed amplitudes. Since
max(|lambda-1|,|lambda+1|)>=sqrt(2), at least one factor in those paths has
error >=sqrt(2)/8 if a common phase calibration is allowed. These are operator
intertwining errors, not noise-rate or experimental lower bounds.

## 7. Constructive escape and its precise cost

Ordinary fixed-parity BKSF on a connected graph of M matter modes is prior
art, not a new mapping. It has one physical qubit per edge, cycle constraints
of rank |E|-M+1 and code dimension 2^(M-1). The usual A/B even-fermion algebra
is represented locally, with B weight at most degree Delta and A weight at
most 2Delta-1. With the present convention A_ij=-i gamma_i gamma_j and
B_i=-i gamma_i eta_i, direct CAR expansion gives

    T_ij = (i/2) A_ij (B_i-B_j).

The hopping sign follows these definitions and is checked directly against
annihilation matrices; no transcribed literature sign is a premise. The
one-qubit occupation flip X_k
changes global parity and has no action within the fixed-parity code. The
local-loader premise used above is absent. Bounded loop constraints may
leave Wilson sectors on a torus; fixing them and preparing the code remain
supplied operations. Connected finite open boxes suffice for this escape.

For the six-port matter-only graph each bulk mode has four octahedral
neighbors and one stream neighbor, degree at most five. There are 12N
intra-cell edges plus d(L-1)L^(d-1) stream edges in an open d<=3 box, with
directions restricted to the physical axes. Thus the fixed-even code has
6N-1 logical qubits and bounded even update support. This is a concrete
resource contrast with all-parity local reference loaders. It does not select
a native lattice representation, state preparation or autonomous update.

An all-parity algebraic escape is also possible with one extra reference
mode r, fixed total extended even parity and no local-D constraints. Embed
|n> as |n, parity(n)> with r ordered last. Original even matter operators
leave r untouched and retain their matrix elements. Connect r by one graph
edge to keep the BKSF graph connected. This has dimension 2^M, local original
even matter terms, and no uniform local representatives for matter X flips.
In that code B_r equals total matter parity. A representative of a distant
matter X must anticommute with B_r on the code and therefore must reach its
support. This proves the stated loss of uniform local occupation-bit loaders.
It supplies a distinguished reference site and a global encoding/preparation
relation; it is not an order-free native local loader. Unlike Cycle232's
uniform-reference construction, it has no even-volume capacity failure.

Next research should change one of these explicit architectural conditions or
construct the remaining native formation bridge. More finite weight descent
on the same all-parity local-loader E cannot remove the proved joint syndrome.

## 8. A constructive local Clifford map for adding reference bonds

This is an explicit graph-change proof, independent of the locality negative.
Let G be a connected BKSF graph. Add a new edge e=(u,v), placed last in the
incident ordering at each endpoint, and an ancilla qubit e initially in |+>.
Choose an existing simple path p from u to v of length ell. Define

    L_p = i^(ell-1) product_(a,b along p) A_ab,
    S_e = epsilon_uv B_u B_v L_p,
    C_e = |0><0|_e tensor I + |1><1|_e tensor S_e.

L_p is the Hermitian endpoint Majorana pair on the old loop code. S_e is a
Hermitian Pauli involution on the whole old physical Hilbert space. The
endpoint commutation rules imply that S_e commutes with every old A and
anticommutes with exactly B_u and B_v. Consequently C_e is a Clifford
involution satisfying exact full-Pauli identities

    C_e A_f C_e = A_f                         (every old edge f),
    C_e B_w C_e = B_w Z_e^(w=u or w=v),
    C_e X_e C_e = X_e S_e.

The first two are precisely the new graph's A/B words. Its new edge word is
A'_uv=epsilon_uv X_e B_u B_v. The added cycle constraint is

    A'_uv L_p = X_e S_e = +1.

On the input X_e=+1 sector, the pulled-back new A'_uv equals L_p. Thus C_e
maps the complete old-loop code times |+>_e onto the new-loop code with the
added positive cycle character, intertwining the even algebra of the unchanged
graph vertices. With references these are the extended seven modes per cell;
this is not an identification with the original six-matter-fermion algebra.
The cycle rank rises by one and no logical degree of freedom is added. This
proves an actual signed isometry, not a dimension-count coincidence.

For reference endpoints u=r_x,v=r_y, use the actual three-edge path
r_x--m_xa--m_yb--r_y. Matter B and all local logical loaders are unchanged
by C_e. The local D rows transform to the new D rows because their reference
B acquires Z_e. The positive all-B vacuum transforms to the new vacuum.
Consequently the same phase-oriented matter encoding obeys

    E_reference = U_add (E_patch tensor |+>^(number of added bonds)),

up to one common phase, after any required local incidence-order gauge.
The inverse returns every added qubit to |+> on the entire encoded matter
space. Therefore a preparation of this matched reference-graph E transfers
to the no-reference-bond E by U_add† with returned added qubits. This is
conditional on the supplied preparation and on its stated logical phases;
it neither executes the prior controller nor supplies native genesis.

An adjacent swap of two incident edges e,f is implemented by CZ_(e,f): it
adds Z_f to A_e and Z_e to A_f and leaves all B fixed. A product of these
local incidence-order gauges brings the appended-edge ordering to a specified
reference-graph ordering. Physical edge labels can be identified by their
endpoints; index permutations relabel the same geometric qubits and do not
move states to distant sites. If vertex labels change edge orientation, a local Z on that edge
fixes the corresponding sign. Matching the matter tensor-product occupation
labels by coordinates is explicit; this is not a new assertion of proper-
cubic covariance of the original matter Fock permutation.

For the six-port open boxes, S_e touches the two endpoints' reference spokes,
their single matter stream, and earlier reference bonds incident to them.
With the actual edge order its weight before prior-reference factors is
13-a-b = 12-4mu on an axis-mu stream (a=2mu+1,b=2mu). At most ten earlier
reference bonds can be incident to the two endpoints, so weight(S_e)<=22.
The ancilla control adds one qubit. Exact Pauli words verify this bound in
the graph runner.

A uniform coarse-local schedule exists: color each positive coarse edge by
(axis, source coordinates modulo 3), at most 81 colors in three dimensions.
Two edges of one color have disjoint endpoint stars, so their controlled
Paulis act on disjoint qubits, including all earlier reference bonds. Perform
colors in order. Each C_e decomposes into at most 22 controlled single-Pauli
Clifford gates and at most one Z on the control for its overall sign. The
final reference-incidence gauge has at most 15 CZs per cell; a bipartite cell
coloring gives at most 30 additional layers. One initial Hadamard layer and
one orientation-sign layer give the deliberately loose constant depth bound
81*23+30+2=1895 in this bounded-range abstract edge-qubit Clifford gate set.
A physical nearest-neighbor site placement, circuit-order genesis or native
time interpretation is not included. On the 2x2 graph the exact count is
76 old edge qubits plus four returned |+> inputs equals 80 reference-graph
edge qubits. No asymptotic state vector computation is required for the proof.

This constructive equivalence does not evade Sections 1-5: it preserves the
same local matter loaders. It transfers the preparation obligation while
leaving the fermionic-hopping locality obstruction intact. The next useful
architecture must therefore distinguish the two obligations rather than
expect the extra reference bonds alone to repair the exchange sign.

## Scope guard after the constructive map

The obstructions above concern the named independently selectable hopping
generators/gates and the fixed local-D operand grammar. A special indivisible
global update word may have cancellations between factors. It has not been
ruled out merely because a proposed factor-by-factor compiler fails. Likewise,
restricted occupation patterns, fixed particle-number code sectors with a
different encoding, new dynamical gauge variables, or a nonperturbatively
changed code require their own tests. The explicit exchange witness already
lies in even particle number, so that particular grammar is not repaired by
simply declaring parity superselection. None of these statements rules out
fermions on qubit lattices or forces a framework axiom update.

## Proof obligations and falsification evidence

| Obligation | Proof mechanism | Different check of the load-bearing step |
|---|---|---|
| Fermionic hopping and local reference phases | CAR/Jordan-Wigner expansion and explicit even-cell embedding | Dense annihilation matrices; every local reference column for q=1,2,6 |
| Arbitrary representative obstruction | Compression commutator and norm-contractive joint-odd projection | Full small-matrix unitary commutators, exhaustive low-weight Pauli syndromes and degree-two products |
| Same code and actual exchange | Signed stabilizer quotient, unique occupation eigenspaces and closed configuration paths | Integer CAR actions versus independently decoded physical A/B words, including actual directed orientation |
| General support growth | Triangle inequality on a shortest grid path, then lattice volume bound | Several dimensions/sizes/orders and an explicit long snake chord; finite samples do not prove the family theorem |
| Constructive graph equivalence | Controlled-Pauli conjugation of every A/B, D, new loop and logical loader | All 64 dense Pauli conjugations for a minimal edge addition; exact full signed graph maps through open L4 |
| Known constructive escape | Fixed-even BKSF and an explicitly marked last reference mode | Dense code isometries, direct hopping intertwining and the reference/global-parity identity |

On the four-cell graph, the exchange and one-particle paths have relative
fermion/local amplitudes -1 and +1. A fifth pendant cell carrying a stationary
spectator repeats both paths at fixed particle number two, preserving the
same relative mismatch and static-flux test. The graph map checks the actual
76->80, 156->168, 540->594 and 1296->1440 edge-qubit pairs, all logical X/Z
and D phases, full stabilizer-group images, incidence-order gauges and
orientation signs. Removing each added controlled-Pauli map loses its required
cycle character. These are author checks, not an independent review.

## No-Go Discipline Gate

### N1 — examined routes and live alternatives

| Route family | Disposition in this note | Matching mechanism |
|---|---|---|
| Stabilizer-coset optimization and arbitrary off-code/non-Pauli completion | ATTEMPTED: excluded for a representative disjoint from the specified loader | Section 1 applies to arbitrary compression, including leakage; it is not a greedy-decoder failure |
| Low-weight Hamiltonian sums and analytic perturbative generation | ATTEMPTED: direct norm gap and minimum possible perturbation order within stated assumptions | Joint-odd operator sector in Section 2; nonperturbative code changes remain open |
| Returned-ancilla local circuit synthesis | ATTEMPTED: finite-depth light-cone bound for the named hopping gate | Section 5 allows gates throughout the volume and fixed ancillas |
| Mode-order optimization | ATTEMPTED: every total cell order has a long index gap on the stated grid | Section 4 uses a general path/volume argument, not a search over selected orders |
| Static edge flux and occupation-basis rephasing | ATTEMPTED: cannot repair the actual closed exchange ratio | Section 6 uses the same directed moves in exchanged and unexchanged histories |
| Local reference-bond graph extension | ATTEMPTED: positively constructed; preserves the loaders and transfers preparation | Section 8 closes graph equivalence while preserving the preceding obstruction |

These are author-proposed proofs/tests, not prior ratified no-gos. Ordinary
fixed-parity BKSF, a distinguished global reference, changed gauge constraints,
nonlocal odd loaders, a new operand algebra, and a specially composed global
update remain live alternatives. The table is a packet search record, not a
claim of exhaustive impossibility.

### N2 — one obstruction and a separate positive obligation

The direct support, weight and finite-depth consequences share the same local
loader/fermionic-hop incompatibility; they are not counted as independent axiom
walls. The graph-isometry obligation is constructively closed for the stated
open graphs. That closure preserves the loader and therefore does not close
the hopping obligation. No independence claim is made about native selection,
state formation, metric dynamics or physical clock interpretation.

### N3 — hidden hypotheses

The total occupation order, local physical X representatives, independent
availability of the specified hopping gates, fixed loop/D sector, directed
operand formulas, empty spectators in the first exchange witness and the
stationary spectator in the fixed-number witness are explicit. The perturbative
claim assumes invariant H0 resolvents and an analytic fixed-box expansion.
The circuit bound assumes bounded-range unitary gates. The graph map assumes
available |+> ancillas and prescribed short paths. None is silently selected
by the axioms or by a numerical agreement.

### N4 — residual matching

The current-main patch note reports growing representatives and an unconstructed
76/80 graph isometry. The present proof replaces the representative search
with a general commutator invariant and supplies the signed graph map. The
held-grammar note tests projector/covariance properties without a global
matter-state intertwiner; the present exchange tests that missing intertwiner.
The old Cycle232 uniform-reference parity failure concerns different constraints
and is not used against the current local-D code. Literature BKSF and two-
dimensional gLU equivalences are constructive prior art, not negative witnesses.

### N5 — resolution and rhetoric

Per operator, matrix commutators and Pauli phases are exact. Per cell, every
q=6 local reference column is checked. Per mode, every logical X/Z and every
stream in the stated finite graphs is compared in a signed stabilizer quotient.
Per block, the full eight-factor closed paths test actual multi-particle
composition. The grid, joint-syndrome and controlled-edge proofs supply the
quantified family statements; finite size/rank counts do not. No thermodynamic
phase, arbitrary QCA classification or all-encoding no-go is claimed.

### N6 — constructive partial closure

The explicit Clifford map transfers a correctly phased reference-graph
preparation to the patch graph and returns the extra qubits. The ordinary
fixed-even encoding and marked-reference construction retain local even CAR
operators by giving up the problematic local all-parity loader condition.
These are architectural choices within supplied qubit models. No axiom or
primitive update is requested or inferred.

### N7 — strongest surviving alternatives

The locality test does not apply when the physical representative of an
occupation-qubit X is nonlocal, when the low-energy code changes, or when only
a special whole update word is required and its factors need not separately
match the stated hopping. The fixed bounded grammar nevertheless fails under
all occupation-preserving phase choices in its declared code, including an
even two-particle witness. A successful replacement must exhibit its actual
state/operator intertwiner; a dimension count or one-particle spectrum is
insufficient for that particular claim.

### N8 — cross-cycle and novelty boundary

Earlier pair-shadow and global-reference examples already exposed related
statistics/preparation issues. This result does not rebrand those principles
as a new universal obstruction. It gives a general same-encoding norm/weight
bound, an actual six-port exchange discriminator, and the missing signed
local graph isometry. The native physical realization remains open, and
independent review is required before these results are used as retained facts.

## Sources, reading limits and reproduction

[Setia, Bravyi, Mezzacapo and Whitfield](https://arxiv.org/abs/1810.05274v2)
provide the standard superfast encoding and loop-code construction. The ordinary
encoding section and Appendix A were read. [Chen and Xu](https://arxiv.org/abs/2201.05153v1)
study finite-depth Clifford/gLU equivalence in two dimensions; the introduction,
gLU definitions and BKSF comparison were read. Their general classification is
not imported as a three-dimensional theorem. The present graph addition is
proved directly. The committed reading ledger records source hashes and exact
review scope; whole-paper or historical-runner review is not claimed.

Run the paired primary with Python 3, NumPy and SciPy. It consumes no files or
unmerged scientific dependencies. The general conclusions rest on the proofs
above; the runner provides consequential falsifiers. Canonical execution uses
`scripts.runner_cache.execute_and_write_cache` with the declared 90-second
budget and records stdout, stderr, elapsed time and source hash.

The author ran focused syntax, canonical-cache freshness/hash, link, vocabulary,
whitespace and mutation checks. Full pipeline, strict global lint and combined
changed-evidence validation are deferred under conformance section 12 to the
exact integrated candidate. They are not reported as passed. No audit verdict,
main merge or effective retained status is written by this science branch.

## Claim-status certificate

```yaml
target_claim_type: bounded_theorem
actual_current_surface_status: conditional-support
trace_class: upstream_support
target_claim_id: null
source_of_blocker_text: frontier_question
reachability_to_target: supports
artifact_role: theorem
next_trace_action: Independently review the graph isometry and exchange/support bounds; construct a changed encoding or operand law with actual fermionic statistics.
conditional_surface_status: Supplied graph, code, occupation map and gate set; exact conditional mathematics with native selection and formation open.
hypothetical_axiom_status: null
admitted_observation_status: null
claim_type_reason: Constructive signed graph equivalence plus quantified same-encoding and fixed-grammar limits; no general fermion-on-qubit or axiom-forcing no-go.
audit_required_before_effective_retained: true
bare_retained_allowed: false
```
