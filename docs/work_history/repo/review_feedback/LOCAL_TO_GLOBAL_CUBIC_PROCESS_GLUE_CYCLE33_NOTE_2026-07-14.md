# Local-to-Global Cubic Process Glue — Cycle 33

**Date:** 2026-07-14

**Type:** authority-free exact local-QCA construction, finite
decoherence/process gluing theorem, quasilocal extension witness,
boundary/extension independence control, placement gate, and N1–N8 scoped
obstruction audit

**Authority:** none. This note does not amend an axiom, register a primitive,
select the framework law or boundary, issue an audit verdict, or authorize a
constitutional edit. It is a local constructive probe only.

## Result up front

Cycle 30's strongest steelman works in exact finite form and has an exact
infinite-lattice type realization.

Take one qubit at each site of Z3 and put the same controlled-phase gate on
every undirected nearest-neighbor edge. All of these gates commute. In the
Heisenberg picture their product defines the radius-one rule

~~~text
alpha(Z_x) = Z_x,
alpha(X_x) = X_x product_(y nearest x) Z_y.
~~~

The rule is an involutive quasilocal automorphism. It commutes with lattice
translations and proper cubic rotations. Supply one normalized positive
boundary functional—for the positive construction, the all-plus product
boundary. Then every finite record-protocol answer is obtained by composing
the same local rule with the inserted local instruments and evaluating the
resulting finite-causal-cone effect on that boundary.

This yields, without a separately chosen global measure:

- an exact Bell pair from one nearest-neighbor controlled-phase gate and CHSH
  value 2 sqrt(2);
- a normalized strongly-positive decoherence functional whose coherent and
  recorded coarse-grainings give (1,0) and (1/2,1/2);
- normalized adaptive instruments with record-conditioned feed-forward;
- identity-slot containment, with omission distinct from measure-and-forget;
- projectively compatible finite density/process restrictions; and
- a conditional future functional determined by the complete protocol and
  outcome records.

For this construction, **no independent finite global measure atom survives**.
Strong positivity, normalization, Bell weights, interference, instrument
composition, and finite containment are theorems of local operator
composition plus the boundary. The global process/comb is a useful compiled
representation, not additional fundamental physics.

One independent item does survive: the **boundary/history datum survives**.
The identical local rule accepts an all-zero boundary and an all-plus
boundary, and they give different record laws. A local rule by itself
therefore does not determine this candidate's global process. Once an exact,
projectively consistent boundary functional is supplied, no further measure
choice is needed. If “boundary” means only a collection of separately
normalized finite guesses, global compatibility still has to be proved or
supplied. Thus **global consistency is a theorem obligation**, not
automatically a new axiom and not automatically free.

The placement result is conditional but sharp:

1. If the final TOE supplies one exact local compositional rule and derives
   its projective extension from an exact boundary/history datum, the global
   process belongs downstream as a theorem. **Retyped Admissibility**—more
   honestly, Admissibility reworked into Local Law—is the fundamental home.
   A separate global Law axiom would duplicate derived content.
2. If only a global decoherence/process functional is ever identified, with
   no local generator or gluing theorem, it needs **separate Law** placement.
3. The present Admissibility axiom cannot be silently read as the first case.
   It is explicitly availability-only and supplies no amplitudes, transition
   maps, normalization, record process, or boundary.

The construction also gives a zero-state-edit model. Conditional operators
are derived from the fixed rule, fixed boundary, and permanent protocol and
outcome records. They need not be an unrecorded physical carrier. Therefore
**no Qualification amendment is forced**. But record-only predictive
completeness still requires record-fibre future-equivalence: if two equal
complete record configurations can occur under different unfixed boundaries
and have different futures, the boundary must be fixed by the law, encoded in
records, or the state language must eventually change.

No live axiom or primitive edit is justified by this type witness.

## 1. Foundation and primitive boundary

The current foundation says:

> A state is a configuration of records.

It also says the one nearest-neighbor Admissibility rule determines which
possibilities are available and explicitly says Admissibility is not dynamics.
No approved primitive supplies an amplitude, process, probability,
normalization, boundary, instrument, or global extension.

The realized-state primitive supplies one law-admissible actual-state
reference for pointwise evaluation. It supplies no state content or boundary.
In particular, choosing the all-plus product boundary below is a conditional
construction input, not content hidden in that primitive.

The Cycle 33 question is narrower than law selection:

> If an exact homogeneous local complex rule and an exact boundary are both
> given, must a separate global history measure still be chosen?

For the displayed QCA/process class, the answer is no.

## 2. One exact cubic nearest-neighbor rule

Let every site x carry M2(C). On every undirected nearest-neighbor edge
{x,y}, use the same gate

~~~text
CZ_xy = diag(1,1,1,-1).
~~~

Because controlled-phase gates are diagonal, gates on overlapping edges
commute. Their product can therefore be defined without choosing an edge
order. On any finite observable only the finitely many incident edge gates
matter, so the infinite product defines the displayed radius-one action alpha
on the quasilocal algebra.

This is **one fixed nearest-neighbor controlled-phase rule** on the supplied
cubic adjacency.

The rule has the exact properties needed for a local-to-global type witness:

- locality: one step expands support by at most one lattice edge;
- homogeneity: every undirected nearest-neighbor edge has the same gate;
- translation covariance: translating an observable translates its image;
- proper-cubic covariance: rotations merely permute the six neighbors;
- unitarity: each edge gate is unitary;
- reversibility: alpha squared is the identity; and
- causal composability: every finite record protocol has a finite causal
  contraction.

The runner enumerates all 24 proper rotations of an open cubic cell, verifies
that they preserve its twelve-edge set, checks the overlapping-gate
commutator, and proves the two-site Pauli conjugation identities exactly.

This is a simple Clifford QCA, not a candidate TOE. Its virtue is that nothing
about the local-to-global step is left metaphorical.

Schumacher and Werner define QCA as translation-compatible infinite quantum
lattice dynamics with finite propagation and show how local rules generate
global automata, including constructions from commuting translates
([Schumacher and Werner, 2004](https://arxiv.org/abs/quant-ph/0405174)).
Arrighi, Nesme, and Werner prove a converse-style localizability result for
unitary causal evolutions on graphs
([Arrighi, Nesme, and Werner, 2007/2009](https://arxiv.org/abs/0711.3975)).
Those are external type authorities, not sources of this framework's rule.

## 3. Exact local-to-global theorem

Let omega be a normalized positive boundary functional on the quasilocal
algebra. Define the evolved functional by

~~~text
omega_alpha(A) = omega(alpha(A)).
~~~

Because alpha is a star-automorphism, positivity and normalization follow:

~~~text
omega_alpha(A dagger A)
 = omega(alpha(A) dagger alpha(A)) >= 0,

omega_alpha(I)=omega(I)=1.
~~~

For a finite adaptive record history

~~~text
h=(program_1,r_1,...,program_T,r_T),
~~~

compose the corresponding local completely positive branch maps with alpha.
In the Heisenberg picture this produces a positive effect E_h supported in a
finite causal cone. Define

~~~text
p(h)=omega(E_h).
~~~

Instrument completeness gives

~~~text
sum_(r_T) E_(h,r_T)=E_h,
~~~

so normalization and prefix consistency follow inductively. Adaptivity adds
no new mathematical atom: after a record r is written, that record selects
the next already-defined local instrument. An omitted slot inserts the
identity map. Summing the outcomes of a real instrument inserts its
nonselective channel instead.

For coherent history alternatives with class operators C_h, define

~~~text
D(h,h') = omega(C_(h') dagger C_h).
~~~

For every finite coefficient family c_h,

~~~text
sum_(h,h') conjugate(c_h) c_(h') D(h,h')
 = omega(B dagger B) >= 0,

B=sum_h conjugate(c_h) C_h.
~~~

Thus D is strongly positive. If the exhaustive class operators sum to the
identity, D(Omega,Omega)=1. Both the decoherence functional and the process
comb are contractions of the same local tensors and boundary; neither is a
second law choice.

Chiribella, D'Ariano, and Perinotti's link product gives the corresponding
network composition calculus and shows how combs arise from connected
elementary quantum networks
([Chiribella, D'Ariano, and Perinotti, 2009](https://arxiv.org/abs/0904.4483)).
The constructive direction is the relevant one here: the compiled comb is
determined by the connected circuit and boundary.

### Finite-volume theorem

For any finite region, finite horizon, normalized boundary density operator,
and complete local instrument tree, ordinary matrix contraction proves all
the claims above. This is an exact finite-volume theorem.

### Infinite Z^3 extension

The displayed alpha acts directly on every finite-support observable and is
norm preserving. The compatible union therefore extends to the quasilocal
algebra. The all-plus product functional is already a normalized positive
functional on that algebra. Composing it with alpha produces one exact
infinite Z3 state and every finite process restriction without invoking an
infinite state vector.

This discharges projective extension for the displayed candidate. It does not
prove that every proposed local kernel or every per-volume tensor family has
an extension.

## 4. Exact finite positive construction

### Cubic graph-state restriction family

On the eight vertices of one open cubic cell, start from the all-plus product
boundary and apply CZ on all twelve internal edges. The amplitude of a bit
word z is

~~~text
psi(z)=2^(-4) (-1)^[sum_(edges xy) z_x z_y].
~~~

The runner proves normalization, positivity, and exact nested partial-trace
consistency. The one-site reduced density is I/2, while the local graph
stabilizer

~~~text
X_x product_(y nearest x) Z_y
~~~

has expectation one. These answers are generated by the edge rule and
boundary, not entered as a finite global table.

There is an important boundary warning. A **naive open-boundary truncation**
of one plus site has the pure plus density. The same site embedded in a
two-site plus boundary with one CZ edge has reduced density I/2. Restricting a
global process means tracing its exterior while preserving the induced
boundary, not deleting every cross-boundary gate and rerunning a smaller open
circuit.

### Bell from one edge

On two adjacent sites,

~~~text
CZ |++> = (I tensor H) |Phi-plus>.
~~~

Appropriate local Pauli-axis records therefore give exact CHSH value 2
sqrt(2), with normalized positive contexts and unbiased no-signalling
marginals. This is an explicit example in which the probability table is
globally non-Bell-factorizing even though its amplitudes were generated by one
strictly local edge gate.

### Interference and a derived decoherence functional

On a plus boundary, take intermediate Z alternatives followed by a final X
record. With class operators

~~~text
C_(z,x)=P_x^X P_z^Z,
~~~

the derived four-history matrix has eigenvalues

~~~text
(1/2,1/2,0,0).
~~~

It is Hermitian, strongly positive, and normalized. Coherently summing over
the unrecorded Z alternative gives final X weights (1,0). Treating Z as a
formed record removes the cross terms and gives (1/2,1/2). The law-side
history matrix is therefore derived from local amplitudes and the record
context.

### Adaptive instruments

For the two-site graph state, first write the Z outcome r on the first site.
The second site is plus for r=0 and minus for r=1. Apply the record-controlled
correction Z^r, then write an X record. The exact transcript weights are

~~~text
p(r=0,X-plus)=1/2,
p(r=1,X-plus)=1/2,
p(X-minus)=0.
~~~

The future branch is a deterministic function of the fixed rule, boundary,
and record r. At the next optional slot, identity insertion preserves X-plus
with certainty, while a Z instrument followed by outcome erasure gives
half-half. This simultaneously proves **adaptive instruments** and
**identity-slot containment** for the finite witness.

The generalized extension theorem for processes with active interventions is
the proper comparison for containment families
([Milz et al., 2020](https://arxiv.org/abs/1712.02589)). The paper does not
select this local QCA or its boundary.

## 5. Factorization through records

Fix alpha and omega. Let every preparation choice, physical instrument,
setting, correction, and outcome that changes later predictions be represented
in the permanent record history h. Then the recursive branch functional is a
derived calculator. The same complete h gives the same branch functional and
the same future process.

This is the required **record-fibre future-equivalence** condition:

~~~text
equal complete record configurations
    imply
equal future record laws for every legal adaptive continuation.
~~~

The construction factors through records only relative to its fixed boundary
and named instrument repertoire. If two boundary instances are both physically
possible, produce the same complete records, and give different futures, the
factorization fails. The record-only route then has three options:

1. the exact law fixes a unique boundary;
2. a persistent preparation/boundary record distinguishes the instances; or
3. the physical state type is enlarged explicitly.

The first two show why no Qualification amendment is forced by local quantum
composition itself. They also show why a density matrix that is merely a
derived conditional summary does not violate the state qualification.

## 6. Paired boundary and extension controls

### Same local rule, different boundary

Apply the identical CZ rule to two exact product boundaries:

~~~text
omega_0  = all-zero product;
omega_+  = all-plus product.
~~~

The zero boundary is fixed and gives Z_x=+1 with certainty. The graph boundary
gives Z_x expectation zero. The local rule, locality radius, covariance, and
composition law are identical. Only the boundary differs. Therefore this
candidate's local rule alone does not select its global record law.

This is a boundary nonuniqueness witness, not a universal theorem that no
local law can derive its boundary. A mixing or fixed-point-selecting law may
have a unique admissible invariant state; that is a live retirement route.

### Same proper-subregion data, different finite extension

On the eight-site cube, GHZ-plus and GHZ-minus have identical reduced density
operators on every proper site subset but opposite full-cube X tensor-eight
records. The cube has twelve edges, so the all-edge CZ rule leaves both GHZ
phases fixed. Thus even complete proper-subregion marginals do not determine
the full finite extension.

This control is deliberately limited to the **finite cube**. In the infinite
**quasilocal limit**, the GHZ relative phase is invisible to every
finite-support observable; the two phase sequences define the same quasilocal
mixed functional. It would be an overclaim to turn the finite full-support
phase bit into an independent infinite local-physics atom. Operationally
identical extensions should be quotiented.

### Individually normalized but incompatible volumes

The runner also displays a normalized one-site law with p(0)=1/2 and a
normalized two-site law whose first-site marginal is p(0)=2/3. Both volumes
normalize, but they are not a projective family. This proves only that
per-volume normalization is weaker than extension compatibility. It does not
apply to the explicit product-boundary QCA family, whose compatibility was
constructed.

## 7. What is and is not independent

For this architecture, the minimal exact contract is:

| field | status in the construction |
|---|---|
| local compositional rule L | supplied as the exact CZ quasilocal automorphism |
| causal/schedule convention | derived from commuting edges for this one-step rule; discrete step remains part of L |
| boundary/history datum B | supplied as an exact positive product functional |
| instrument/record decoder R | supplied finite protocol category; arbitrary CP instruments are supported but physical repertoire is not selected |
| global process W | derived from L+B+R by contraction |
| positivity and normalization | derived |
| projective consistency | derived for the constructed quasilocal family |
| actual realized history | separate pointwise interface; not selected by W |
| record-fibre future-equivalence | holds in the finite witness relative to fixed L, B, and complete R records; universal theorem still required |

The collapsed scientific residue is therefore L+B+R, not L+B+R+W+an
independent normalization measure. A global process matrix may be stored for
calculation, but it contains no freely selectable value after its local tensors
and boundary are fixed.

The boundary/history datum is not automatically a second law. It may be a
conditional preparation record, a cosmological boundary, a unique invariant
state derived from L, or part of one exact complete-history law. Its physical
classification must follow the eventual theory. The realized-state primitive
does not silently fill it.

## 8. Placement: retyped Admissibility versus separate Law

### Retyped Admissibility wins for the proved architecture

If Nature's exact rule has the form proved here, the fundamental content is
the local compositional map alpha and its exact domain. The global D, comb,
and record transcript law are generated consequences. The correct endpoint is
an explicit **retyped Admissibility** or renamed Local Law axiom, with the
boundary separately derived or typed. Adding a separate global process axiom
would count the same physics twice.

The minimum semantic form would be something like:

> There is one fixed nearest-neighbor composition rule, covariant under
> lattice translations and proper cubic rotations. Its finite compositions
> determine the law of every record continuation.

This is not a landing proposal. “Composition,” the complex codomain, causal
step, generated joint algebra, and record instrument must all be defined by
the exact selected rule. The second sentence is a theorem only after the
gluing and boundary work lands. A generic class statement does not select a
TOE law.

### Separate Law wins if the local theorem fails

If the final object remains a global action, decoherence functional, or
process tensor with no exact nearest-neighbor generator, then it is not
type-identical to the current availability map. It belongs in **separate Law**
placement. The finite constructions show that such placement is not forced by
quantum probability itself; it is forced only by the architecture actually
selected.

### Present foundation status

Current Admissibility cannot be enlarged by interpretation. Retyping would be
a constitutional change with the same audit blast radius as any other axiom
change. Before that is considered, the project still needs an exact candidate
local rule that reaches the matter, chirality, interaction, record, clock, and
gravity lanes. CZ is only a clean existence witness.

## 9. TOE-lane consequences

| lane | supplied by local-to-global glue | still missing |
|---|---|---|
| probability | positive normalized process weights and interference follow from local contraction | selection of the exact local rule and empirical Born/frequency interface |
| Bell/locality | local amplitudes generate CHSH 2 sqrt(2) without Bell-local probability factorization | relativistic microcausality and continuum cone |
| formation | local instruments can write branch-labelled records | autonomous trigger, physical pointer, strict permanence, actual branch |
| state | conditional operator is derivable from fixed law, boundary, and records | universal record-fibre future-equivalence or explicit state revision |
| time | causal circuit depth orders local events | metric time, rate, clock universality, foliation independence for noncommuting rules |
| arrow | record protocols can be append-only | low-record boundary, entropy theorem, irreversible sector mechanism |
| matter/QFT | coherent local propagation architecture is available | actual fermions, chirality, interactions, continuum, couplings |
| gravity | a local process can jointly generate geometry and records in principle | conserved source, field equation, lapse, equivalence principle |
| capacity | process separates working amplitudes from permanent records | renewal/export and resource cost |
| actuality/frequency | neither is supplied by unitary glue | realized member is separate; corpus frequencies need their own theorem |

The gluing result closes a process-construction lane, not the TOE.

## 10. No-Go Discipline Gate

The only narrow obstruction claimed is:

> For the displayed controlled-phase architecture, the local rule alone does
> not determine the global record process; an exact boundary/history datum is
> additionally required unless a boundary-selection theorem is proved.

The note does not claim that every local rule has multiple invariant
boundaries, that no boundary can be derived, that global history laws are
impossible, or that a new axiom is required.

### N1 — alternative-route enumeration

| route | marker | outcome |
|---|---|---|
| commuting-edge Clifford QCA | ATTEMPTED | exact positive construction; global W derives from L+B+R |
| noncommuting brickwork/Margolus QCA | live, primary-source supported | can derive W after an exact schedule/partition and boundary are supplied; not tested as a cubic winner |
| causal unitary localized circuit | live, primary-source supported | localizability can turn a causal U into local gates; it does not select U or B |
| Hamiltonian/Lieb-Robinson route | live | may yield quasilocal rather than strict cones; exact action, state, and instrument glue remain |
| tensor-network/path-amplitude route | live | can contract a global D from local tensors; boundary tensor and infinite contraction must be controlled |
| local CP/open-system process | live | finite comb follows from channels and environment boundary; autonomous record instrument and dilation remain |
| unique invariant/fixed-point boundary | live steelman | could derive B from L and retire the boundary input; CZ is involutive and does not do so |
| global D/comb adopted directly | live alternative placement | bypasses local derivation and therefore needs separate Law placement |
| operational quotient of inequivalent extensions | ATTEMPTED on GHZ phase | retires extensions indistinguishable by every finite record protocol |

The positive routes prevent any universal no-go.

### N2 — wall-independence audit

After collapsing derived fields, the open contract has three physical inputs:

~~~text
L  exact local compositional law, including carrier and causal schedule;
B  exact positive consistent boundary/history datum;
R  physical record-instrument category and decoder.
~~~

The actual-state reference A is already an approved primitive at its narrow
pointwise scope; it is not counted as a wall and supplies none of L, B, or R.

| pair | first closes second? | second closes first? | independent? |
|---|---|---|---|
| L,B | no: same CZ admits zero and plus boundaries | no: one boundary supports many laws | yes |
| L,R | no: QCA does not select physical record instruments | no: an instrument category does not select dynamics | yes |
| B,R | no: a boundary does not select allowed interventions | no: protocols do not select cosmological/preparation boundary | yes |

For the explicit automorphism and product B, projective consistency G and
global W follow by construction. They are not counted as additional
independent walls. For an arbitrary per-volume kernel, G would have to be
restored as a separate condition until an extension theorem closes it.

### N3 — hidden-wall scan

| phrase | hidden risk | treatment |
|---|---|---|
| by construction | can hide boundary positivity or infinite convergence | product functional and local automorphism are stated and checked separately |
| same local rule | may omit schedule or carrier | L includes qubit tensor net, discrete step, and commuting-edge product |
| global state | may imply an infinite vector | use a positive quasilocal functional |
| arbitrary instruments | may imply the law physically supplies them | construction supports CP maps; R remains a supplied physical category |
| record-only | may assume future sufficiency | require record-fibre future-equivalence |
| restriction | may mean rerun with open boundary | use partial trace/induced boundary; include the open-truncation counterexample |
| boundary | may be hidden in the realized-state primitive | registry check confirms it is not supplied there |
| normalized local rule | may be mistaken for a compatible family | incompatible-volume control separates them |
| naturally | no load-bearing use | excluded from the proof claims |

### N4 — exact residual matching

| prior witness | its exact residual | use here | match? |
|---|---|---|---|
| Cycle 30, Global Record-History Process Law, sections 2 and 8 | global D/comb type existed; local generator and infinite extension open | Cycle 33 supplies one exact local generator and product-boundary extension | yes |
| Full-Lattice FD-SLIR, sections 2–3 | separately normalized finite instruments require gluing and projective cylinder compatibility | used only for the extension-type comparison and incompatible-volume control | yes, at extension scope |
| Generated Finite Composition theorem | local M2 copies do not alone exclude extra global carrier sectors | L is explicitly defined on the generated quasilocal tensor algebra | yes, domain only |
| Adaptive Record-Protocol QCA theorem | adaptive CP histories compose and full frame transport preserves probabilities | used only to support adaptive protocol typing, not boundary selection | partial; not a boundary witness |
| realized-state primitive | actual reference supplies no boundary or measure | prevents laundering B through A | yes |

No probability or formation note is cited as proof that CZ selects a boundary.

### N5 — rhetoric and resolution audit

The statement “no independent global measure atom survives” is proved for:

- every finite protocol built from a specified normalized boundary, the exact
  local unitary rule, and complete CP instruments; and
- the displayed infinite quasilocal product-boundary construction.

It is not asserted for arbitrary per-volume kernels, nonnormal infinite states,
noncausal global constraints, or unspecified path integrals.

The statement “local rule alone does not determine the boundary” is witnessed
for this exact CZ rule on one edge, the finite cube, and its product-state
quasilocal extensions. It is not generalized to every possible mixing or
boundary-selecting law.

The GHZ phase result holds for full-support measurements on the finite cube.
It is explicitly retired as an infinite quasilocal distinction.

### N6 — partial-closure paths

1. A unique invariant-state or attractor theorem for the selected L can derive
   B and retire the boundary import.
2. A fixed product, tensor-network, Gibbs, or cosmological boundary can be
   stated as a named conditional while its retirement is attacked.
3. Persistent preparation/boundary records can make B part of the record
   configuration for laboratory protocols.
4. Operational quotienting can remove extensions that no finite record
   protocol distinguishes.
5. Defining the exact law directly on a positive quasilocal functional can
   package L and B once; this is separate Law architecture, not proof that B
   disappeared.

The realized-state primitive is not a closure path for B because its source
explicitly supplies no boundary content.

### N7 — strongest steelman

The boundary residue may be an artifact of choosing an involutive CZ rule.
A genuinely dissipative local quantum channel, a primitive causal automaton
with a unique invariant vacuum, or a variational law with a uniquely selected
ground functional could derive its only admissible quasilocal boundary.
Schumacher–Werner and localizability results show that nontrivial exact local
automata are broad enough that CZ cannot represent the whole class. If such a
unique-boundary theorem also proves record-fibre sufficiency, L alone could
generate W and B, leaving no independent boundary datum. This is why the
negative is restricted to the displayed architecture and why boundary
selection is the next scientific attack, not an axiom ruling.

### N8 — cross-cycle echo

Earlier work repeatedly promoted compiled global objects before checking
whether a local generator made them derived. The generated-composition theorem
showed that a law can own its quasilocal domain; Cycle 30 showed a global
process can preserve record-only ontology; FD-SLIR separated finite
normalization from extension; and the infinite-redundancy probe showed that a
finite GHZ phase can disappear in the quasilocal quotient. Cycle 33 applies
all four lessons: derive W when possible, retain B honestly, require extension
compatibility, and do not count an operationally invisible tail phase as new
physics.

**No-go-discipline status: PASS.**

## Verification

Run:

~~~bash
python3 scripts/local_to_global_cubic_process_glue_cycle33_2026_07_14.py
~~~

The runner must report zero failures. It changes no authority surface.
