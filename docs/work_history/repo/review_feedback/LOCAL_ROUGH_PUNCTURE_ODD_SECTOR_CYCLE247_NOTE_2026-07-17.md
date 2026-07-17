# Local rough-puncture odd-sector compiler tournament — Cycle 247

Date: 2026-07-17
Status: constructive partial closure with three exact candidate discriminators
Authority: none
Audit: unset
Constitutional effect: none

Companion runner:

```text
scripts/local_rough_puncture_odd_sector_cycle247_2026_07_17.py
```

## Result up front

This cycle tests whether a bounded, repeated rough boundary or puncture can
replace the marked global charge/Wilson service in the Cycle-235
square-pyramid face code.  Every coarse cell receives the same proper-cubic
puncture at its center.  The constructions are periodic, preserve coarse-cell
unit translation as code families, use constant M2 overhead, and are tested
under all 24 proper-cubic frames.  This is not homogeneous one-site
translation on undifferentiated physical M2 factors: the inherited period-16
physical role marker remains supplied.

Three exact candidates separate rank, lawful dynamics, and auxiliary-sector
removal:

1. **Cubic puncture.** Add one sink mode and six spoke face qubits per cell.
   Bounded local cell-parity constraints give exactly the target exponent
   \(6N\) and leave all \(6N\) matter parities independent.  But every
   inter-cell stream generator violates two cell constraints.
2. **Cubic sink network.** Add three sink-network face qubits per cell and
   dress a matter stream with the parallel sink hop.  The dressed stream is
   lawful and the code still has exponent \(6N\), but two distinct streams
   incident on one coarse cell acquire a false anticommutation from their
   shared sink.  There are exactly \(15N\) extra anticommutations.
   In the runner contract: 15N extra anticommutations.
3. **Local rough terminal.** Add a terminal physical M2 factor to every sink
   and dress each stream by the two endpoint terminal \(X\)'s.  This gives an
   exact bounded even-CAR generator algebra, zero leakage, both matter-parity
   sectors, unit translation, and 24-frame covariance.  Its locally enforced
   code exponent is \(7N-1\), leaving exactly **N-1 excess boundary logical
   qubits**.  Adding two or three terminal factors with local pair constraints
   leaves the same excess.

Thus the strongest result is a genuine local rough-end **operator compiler
with auxiliary multiplicity**, not a physical code-space isometry.  The two
rank-matched candidates fail the stream algebra, while the algebraically exact
candidate has an oversized declared code.  Rank matching is not an isometry.
No tested candidate supplies a bounded local \(E\) with image equal to its
locally enforced code, so the equation

\[
E G_{\rm coarse}=G_{\rm physical}E
\]

is not claimed.  This is a narrowed candidate-family result, not a general
boundary, subsystem-code, or non-Pauli no-go.  There is no axiom pressure.

## Scoped prior-art boundary

Haegeman, Van Acoleyen, Schuch, Cirac, and Verstraete,
[*Gauging quantum states: from global to local symmetries in many-body
systems*](https://arxiv.org/abs/1407.1025), provide the retained state-gauging
motivation: a globally invariant input sector can be mapped isometrically to
a locally gauge-invariant matter-plus-gauge sector with local symmetric
operator images.  Cycle 245 instantiated that result on this graph and kept a
boundary or ungauged charge sink live.  The source does not supply the
puncture geometry, the terminal M2 code, or a full odd-sector physical
compiler tested here.

Wei et al., [*High-Distance Error-Correcting Codes for Fermion-to-Qubit
Mappings in 2D and 3D*](https://arxiv.org/abs/2509.00147), use the 3D
Chen--Kapustin base to obtain local constant-weight coding constructions and
retain nontrivial membrane-sector structure on periodic domains.  Their
periodic treatment motivates keeping emergent total parity and boundary
resources explicit.  It is not imported as a local rough-puncture state
preparation or as the Cycle-230 physical update.

The new content here is repo-native: exact puncture cellulations and ranks,
explicit mapped generators on the six-pyramid graph, held-size and full-frame
tests, and the boundary-multiplicity discriminator.

## Physical puncture cellulations

Let \(N=L^3\).  The Cycle-235 matter graph has \(6N\) pyramid vertices and
\(15N\) face-qubit edges.  For each cell \(x\), introduce one auxiliary sink
vertex \(s_x\) and connect it to the six pyramid modes by six new spoke face
qubits.  The physical Hilbert space is still a tensor product of M2 factors:
the auxiliary sink is an algebra label; its encoded parity is the product of
the incident face \(Z\)'s.

The local cycle family consists of:

- the Cycle-235 primal-edge cycles;
- one sink--matter--matter triangle for every onsite octahedron edge; and
- for the network candidate, one sink--matter--matter--sink square per coarse
  lattice bond.

The first two families have local rank \(14N-2\); the three inherited Wilson
cycles raise this to \(14N+1\).  Adding the sink squares raises the ranks to
\(17N-2\) and \(17N+1\).  Every added loop has length three or four.

Write \(B_{s_x}\) for the sink flux and \(B_{x,a}\) for the six matter fluxes.
The proper-cubic cell constraint is

\[
C_x=B_{s_x}\prod_{a=0}^{5}B_{x,a}=+1.
\]

Without a terminal, the spokes cancel in \(C_x\), leaving the six matter
stream faces on the coarse-cell boundary.  With sink-network edges it has
those six matter faces plus the six incident sink edges.  The family has one
closed-torus dependency,

\[
\prod_x C_x=I,
\]

and therefore rank \(N-1\).  The resulting code exponents are

| Candidate | M2 factors/cell | Full-cycle rank | Cell rank | Code exponent |
|---|---:|---:|---:|---:|
| cubic puncture | 21 | \(14N+1\) | \(N-1\) | \(6N\) |
| sink network | 24 | \(17N+1\) | \(N-1\) | \(6N\) |

The actual signed-Pauli ranks at L=3 have no minus-identity inconsistency, and
adjoining the matter \(B\) rows increases rank by all \(6N\) generators.
Hence both total matter parities are present.  That is a rank and parity
statement; it does not yet provide lawful stream generators or a state map.

## Cubic-puncture stream leakage

The extended framed \(A_e\) presentation retains the even-CAR incidence
algebra on the matter graph.  Onsite matter edges have both endpoints in the
same \(C_x\) block and commute with all cell constraints.  A stream edge has
one endpoint in cell \(x\) and one in cell \(y\); it anticommutes with exactly
\(C_x\) and \(C_y\).  At every tested size the target-rank puncture therefore
fails the lawful-domain update test.

The spoke operator \(A_{(x,a),s_x}\) is a bounded local terminator: it flips
one matter parity and the sink parity in the same cell and commutes with
\(C_x\).  The six terminators inside one cell have the correct mutual
anticommutation because they share the sink.  Terminators belonging to
distinct cells have disjoint support and commute.  They therefore do not form
the full graded CAR net across cells.  A bounded termination of charge into a
local reservoir is not automatically a global CAR representation.

## Sink-network dressing

The sink-network candidate adds the cubic edge \((s_x,s_y)\) parallel to each
matter stream edge \((u_x,v_y)\) and maps that stream generator to

\[
\widehat A_{xy}=A_{u_xv_y}A_{s_xs_y}.
\]

It flips one matter and one sink parity in each endpoint cell, so it commutes
with every \(C_x\).  It also commutes with every modified-loop stabilizer.
The failure is an exact algebra sign.  Distinct matter stream edges never
share a matter pyramid mode, so their target \(A\)'s commute.  Any two sink
edges incident on one cell share \(s_x\) and anticommute.  A degree-six cubic
sink has \(\binom 62=15\) such pairs, producing \(15N\) false
anticommutations.

The runner exhausts the radius-zero endpoint-parity dressings.  If the six
incident sink edges carry endpoint bits \(p_j\), commuting every pair requires

\[
p_j+p_k=1\pmod 2
\]

for every pair \(j\ne k\).  None of the \(2^6\) assignments satisfies these
conditions.  This rejects only endpoint \(B_s\) dressings.  Radius-one
dressings, extra local Clifford factors, subsystem gauge operators, and
non-Pauli maps remain live.

## Rough-terminal algebraic closure

Now add one rough terminal face qubit \(h_x\) at every sink.  Its \(Z\) enters
\(B_{s_x}\), and the terminal is last in the local incident-face ordering.
Thus modified loop stabilizers contain no terminal \(Z\), and \(X_{h_x}\)
is a local sink-parity flipper.

The terminal makes the \(C_x\) rows independent: their product is
\(\prod_xZ_{h_x}\), so their rank is \(N\).  Map an onsite edge to its usual
extended \(A_e\), and map a stream edge between cells \(x,y\) to

\[
\widehat A_{xy}=A_{u_xv_y}X_{h_x}X_{h_y}.
\]

The matter hop and terminal flip each contribute one cell-constraint
anticommutation at both endpoints, so the total operator is lawful.  The
terminal \(X\)'s mutually commute and do not alter the matter \(A\)-\(B\) or
\(A\)-\(A\) signs.  The L=3 exhaustive generator test finds:

- zero stabilizer leakage;
- zero endpoint \(A\)-\(B\) failures;
- zero hopping-pair commutation failures; and
- bounded maximum Pauli weight.

This is the strongest constructive result of Cycle 247: a bounded local
proper-cubic representation of the full **even** matter generator algebra,
including lawful stream transport and both total matter parities.

It is not yet the requested \(E\).  With one terminal per cell,

\[
(21N+N)-(14N+1)-N=7N-1,
\]

so the declared code has \(N-1\) excess logical qubits.  With \(k=2,3\)
terminal factors, impose the local proper-cubic stabilizers

\[
X_{h_{x,0}}X_{h_{x,j}}=+1,\qquad j=1,\ldots,k-1.
\]

They commute with the terminal flux product, cell constraints, loop
stabilizers, and the chosen \(X_{h_{x,0}}\) flipper.  Nevertheless, the code
exponent remains \(7N-1\) for both tested values.  The redundancy locally
encodes one boundary logical per puncture; it does not remove that logical.

## Why the obvious local boundary gauge fixes fail

Fixing every \(Z_{h_x}\) removes terminal sectors, but every dressed stream
anticommutes with the two endpoint fixes.  Edge equalities
\(Z_{h_x}Z_{h_y}=+1\) have rank \(N-1\), but a neighboring stream sharing only
one endpoint leaks from them.

More generally, within the tested diagonal boundary-Z ansatz, a word
\(Z(h)^z\) commutes with every stream dressing \(X_{h_x}X_{h_y}\) exactly when

\[
z_x+z_y=0
\]

on every edge of the connected cubic cell graph.  The only words are identity
and \(\prod_xZ_{h_x}\).  The latter has weight \(N\).  Thus this ansatz offers
only one lattice-wide selector, not the \(N-1\) bounded constraints needed to
remove the multiplicity.

This centralizer statement is deliberately scoped.  It does not reject
non-diagonal stabilizers, subsystem quotients, bounded non-Pauli constraints,
or an explicit locality-preserving isometry whose image is selected by a
different commutant.

## Global open-boundary control

An ordinary open cubic box is the expected target-changing escape.  Remove
periodic stream wraps and add the \(6L^2\) missing boundary half-faces.  The
matter-flux rows become independent and odd flux can end on the outer surface.
The raw boundary code, however, has exponent

\[
6L^3+6L^2-1,
\]

before boundary-sector fixing.  Its overhead is an area resource, it has no
unit-translation symmetry, and the graph distance from a central mode to the
surface grows between the tested L=3 and L=7 boxes.  The centered cube keeps a
24-frame box family, but it is not the homogeneous bounded-puncture contract.

## Covariance, held size, deletion, and lawful-domain controls

All periodic candidates place an identical scalar sink and terminal cage in
every supplied puncture macro-cell.  Coarse-cell unit translations permute
their constraints.  This covariance is not homogeneous one-site translation
on an undifferentiated physical M2 lattice: the inherited period-16 physical
role marker remains supplied rather than autonomously prepared.  On the rough
candidate, all 24 proper frames preserve the graph, matter/sink/terminal
labels, cell constraints, and stabilizer group.  The inherited local
incident-order gauge repairs every framed \(A\); because terminal factors are
ordered last, it has zero action on the rough flippers.  Every mapped rough
stream transforms to the corresponding mapped stream.

Ranks and overhead are tested at L=3,4,5 and held-out L=6.  The L=6 rows obey
the same \(14N\), \(17N\), \(6N\), and \(7N-1\) laws.  The runner also checks:

- one bare terminal \(X\) violates exactly one \(C_x\);
- the fully dressed stream violates zero constraints;
- deleting the two terminal \(X\)'s from one stream gives exactly two cell
  violations;
- deleting one independent \(C_x\) adds one spurious logical qubit; and
- in the two-terminal code, deleting one local terminal-pair stabilizer adds
  one spurious boundary logical.

These are code-space leakage and deletion controls, not merely operator
support counts.

## Rank matching, state isometry, and fixture firewall

The candidate table is intentionally asymmetric:

| Candidate | Exact \(6N\) exponent | Lawful exact even-CAR update | Declared bounded code-space \(E\) |
|---|---|---|---|
| cubic puncture | yes | no: stream leaks | no |
| sink network | yes | no: \(15N\) wrong signs | no |
| rough terminal | no: \(N-1\) excess | yes | no |

An abstract isometry into a chosen subspace of the rough code exists by
dimension alone, but no bounded locally enforced image subspace or preparation
of it is constructed.  Calling the rough algebra map \(E\) would silently
supply the missing boundary-sector selector.

Therefore the mass/contact/seam firewall remains active.  The runner does not
import or execute the Cycle-219 mass, Cycle-230 contact, or rank-73 seam
fixtures.  No one-particle preservation, contact reproduction, or seam
intertwining residual is reported.  Those tests become lawful only after one
candidate supplies an actual physical code-space isometry.

## Supplied-structure inventory

Cycle 247 supplies, rather than derives:

1. the Cycle-235 periodic square-pyramid matter graph and local Pauli framing;
2. one auxiliary sink vertex per coarse cell;
3. six spoke M2 factors per cell;
4. optionally three sink-network M2 factors per cell;
5. optionally one, two, or three rough terminal M2 factors per cell;
6. the local puncture triangle and sink-square constraint families;
7. the cell constraints \(C_x\) and, for \(k>1\), terminal-pair stabilizers;
8. the terminal-last local ordering convention and its bounded frame gauge;
9. the inherited torus and three fixed Wilson constraints;
10. the choice to regard the terminal cage as a physical rough end rather
    than a dynamical reservoir with its own occurrence law; and
11. any selection/preparation of an auxiliary boundary sector or isometry
    image.

The puncture geometry is a candidate physical architecture, not a new
primitive or axiom.

## Exact runner and residual ledger

Run:

```bash
python3 scripts/local_rough_puncture_odd_sector_cycle247_2026_07_17.py
```

| Residual | Cycle-247 disposition |
|---|---|
| bounded local odd-charge termination | constructive inside each puncture cell |
| global graded CAR of local terminators | not closed across cells |
| rank-matched puncture | constructive |
| lawful stream on rank-matched puncture | falsified for two explicit dressings |
| lawful exact even algebra with rough ends | constructive |
| local removal of rough boundary multiplicity | not closed in tested Pauli ansätze |
| unit translation and 24 frames | exact for rough family |
| held-out L=6 | exact predicted ranks |
| physical code-space isometry \(E\) | not constructed |
| mass/contact/seam | firewalled |

For the campaign ledger, \(C_{local}\) advances: bounded repeated rough ends
can carry the exact even update algebra without a global Jordan--Wigner order.
Its remaining dependency is now an explicit boundary-multiplicity/image
selector.  \(C_{num}\) is sharpened because both matter parity sectors are
present algebraically.  \(C_{int}\) does not move because no lawful \(E\)
permits the contact/seam test.  \(C_{ref}\) records the supplied puncture and
boundary sector.  \(C_{wrap}\) and \(C_{source}\) are unchanged.

## N1–N8 no-go-discipline gate

The gate status is PASS only for these narrow candidate dispositions.  It
fails, and therefore rejects, a general statement that rough boundaries or
punctures cannot compile fermions.

### N1 — Alternative-route enumeration

| Route | Honesty marker | Attempt and exact disposition |
|---|---|---|
| one sink per coarse cell | ATTEMPTED | target rank and both parities close; bare streams violate two \(C\)'s |
| local spoke terminators | ATTEMPTED | lawful within a cell; disjoint-cell terminators commute rather than form graded CAR |
| cubic sink network | ATTEMPTED | paired streams preserve \(C\); sink incidence adds \(15N\) wrong signs |
| endpoint sink-parity dressing | ATTEMPTED | all 64 degree-six assignments fail the pairwise commutation equations |
| one rough terminal per cell | ATTEMPTED | exact even algebra closes; locally enforced code retains \(N-1\) boundary logicals |
| two/three terminal cage | ATTEMPTED | local pair stabilizers remove terminal redundancy but leave the same one logical per puncture |
| onsite/edge boundary-Z fixing | ATTEMPTED | onsite fixing leaks on every stream; edge equality leaks on neighboring streams |
| one global outer boundary | ATTEMPTED | odd flux ends, but area overhead, growing bulk distance, and broken unit translation change the contract |

The rough candidate's positive algebra result prevents an algebraic no-go.
Untested subsystem, non-Pauli, radius-one, and measurement-assisted routes
prevent a general isometry no-go.

### N2 — Wall-independence audit

After collapsing state preparation and fixture claims downstream of an actual
\(E\), two independent candidate conditions remain:

- \(K_{alg}\): bounded mapped generators preserve the local code and the
  exact even-CAR relations;
- \(K_{rank}\): bounded local constraints select exactly a \(6N\)-dimensional
  exponent with both matter parity sectors and no multiplicity.

| Pair | first closes second? | second closes first? | Independent? |
|---|---|---|---|
| \(K_{alg},K_{rank}\) | no: rough terminal closes algebra but not rank | no: cubic/network candidates close rank but not algebra | yes |

A declared local code-space isometry and the fixture intertwiner require both;
they are downstream outcomes, not inflated independent walls.  Covariance is
closed for the rough construction and is not counted as a third wall.

### N3 — Hidden-wall scan

The note's load-bearing supplied choices are listed explicitly: graph,
puncture placement, terminal cage, constraints, ordering gauge, torus/Wilson
sector, and boundary-sector preparation.  “By construction” is not used to
hide a rank or locality premise.  “Naturally” and “obviously” are absent.
“Background” appears only when naming the earlier marked-charge resource, not
as an admission.  “Standard” appears only in bibliographic/source scope and
does not supply a compiler step.  No “framework provides,” “registered,” or
“canonical” claim carries scientific weight.

### N4 — Residual matching

| Witness | Witness residual | Cycle-247 residual | Match? |
|---|---|---|---|
| Cycle 235, `EXACT_3D_HIGHER_FORM_BOSONIZATION_CYCLE235_NOTE_2026-07-17.md:375` | closed face flux fixes total even; a boundary may carry odd flux | puncture makes matter \(B\)'s independent and both parities present | yes, parity only |
| Cycle 245, `HAEGEMAN_PARITY_SECTOR_GAUGING_CYCLE245_NOTE_2026-07-17.md:52-64,393-396` | closed all-plus gauging needs a charge sink or reference | local sinks replace the marked charge algebraically | yes, charge sink only |
| Cycle 246, `OFF_CODE_LOCAL_AUXILIARY_COMPLETION_CYCLE246_NOTE_2026-07-17.md:143-174,311-320` | local conjugates become leakage/global after multiplicity removal | rough terminals retain lawful paired stream dressing but leave \(N-1\) multiplicity | yes, auxiliary multiplicity only |
| Wei et al. 2025, periodic 3D encoding/membrane discussion | local periodic code with explicit global sector structure | motivation for keeping terminal sector supplied | comparison only; not negative evidence |

No Haegeman or Wei claim is used as proof of the new rank/algebra
discriminators.  Those come from the runner.

### N5 — Rhetoric audit

| Resolution | Tested | Not established |
|---|---|---|
| one puncture | local charge termination and terminal algebra | autonomous physical reservoir dynamics |
| one cell | six terminator signs, \(C_x\), terminal cage | global CAR from cellwise odd fields |
| incident stream pair | network false sign and rough exact sign | every radius-one/non-Pauli dressing |
| L=3,4,5, held-out L=6 | ranks, exponent, parity, leakage | infinite-lattice QCA classification |
| all 24 frames | graph/code/mapped rough algebra up to bounded framing gauge | preparation of a selected image sector |
| lattice-wide | boundary-Z centralizer within the diagonal ansatz | arbitrary subsystem commutant |

Accordingly the note says the displayed candidates do not close \(E\), not
that odd charge is not local or that punctures cannot work.

### N6 — Partial-closure path scan

The rough-terminal map closes bounded even-algebra locality and is retained.
The rank-matched puncture closes both parity sectors and is retained.  A next
candidate can try to combine them using a subsystem gauge quotient, a
non-diagonal local commutant, a radius-one cubic Klein-factor cage, or an
explicit measurement-assisted isometry.  The global open box remains a
target-changing boundary control.  These are constructive import-retirement
paths; none calls for a new axiom or registry edit.

### N7 — Steelman

> The negative isometry disposition is far from universal.  The rough
> terminal construction already has every difficult local operator property:
> bounded support, exact CAR incidence signs, lawful constraints, both matter
> parities, unit translation, and all-frame covariance.  Its only tested
> failure is stabilizer multiplicity.  The runner searches only diagonal
> boundary-Z selectors and endpoint sink-parity dressings.  A subsystem code
> can quotient local gauge qubits without fixing their conjugate as a
> stabilizer, and a radius-one cubic Clifford cage can distribute Klein
> factors beyond a single sink endpoint.  Haegeman-style isometries also show
> that image selection need not be a product-state stabilizer preparation.
> Any of these could select one \(6N\)-dimensional invariant copy inside the
> rough code.  Cycle 247 therefore cannot support a general puncture no-go.

The steelman is convincing.  The result remains a partial attempt with named
live routes.

### N8 — Cross-cycle echo

- Cycle 235 left an open/punctured odd-flux route live after closing only the
  periodic total-even face code.
- Cycle 237 separated a covariant local marker family from selection and
  preparation of one sector.
- Cycle 240 separated local projection from global decoding and preparation.
- Cycle 241 found a bounded-stabilizer rank deficit but kept subalgebra and
  non-Clifford isometries live.
- Cycle 245 constructed exact sector gauging and showed that a marked charge
  or boundary changes the closed neutrality contract.
- Cycle 246 localized the parity conjugate off code and exposed its loss under
  simple local multiplicity constraints.

Cycle 247 advances rather than repeats those walls: the repeated rough end now
produces the exact lawful even update algebra.  The recurring sector-selection
issue becomes an explicit \(N-1\) boundary commutant problem.  Prior cycles
retired comparable partial walls by changing representation and adding local
gauge structure, so the same mechanism remains live here.

## Time firewall

The puncture triangles, sink squares, terminal dressing, Pauli ordering,
constraint-projection order, and runner loop are compiler schedules and
algebraic operations.  No schedule index is physical time, no circuit depth is
a duration, no constraint application is a realized occurrence or Record, no
wrapped phase is called energy, and no generator element is called a rate.

No axioms, foundation, Qualification, primitives, registries, policies,
queues, or audit status were edited.
