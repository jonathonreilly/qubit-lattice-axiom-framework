# Physical proper-cubic persistent subsystem sink — Cycle 553 (2026-07-21)

Authority: none.  Audit: unset.  Constitutional effect: none.

Runner:
`scripts/physical_proper_cubic_persistent_subsystem_sink_cycle553_2026_07_21.py`.

## Result

Cycle 553 constructs the positive information-retaining escape identified by
Cycle 550.  It turns the replicated Cycle-547 branch fields into an explicit
proper-cubic **persistent subsystem** with local CSS constraints, exact
reversible transfer and inverse, and a fully enumerated sink commutant.  Two
codes are kept separate:

- a three-bit code retains only the independent Wilson labels;
- a six-bit code retains the Wilson and membrane-frame labels needed by the
  existing Cycle-547 relational target representation.

Both are one fixed physical object, not frame presentations.  They occupy six
or twelve installed blank microgrid M2 per coarse cell.  Their support-two
constraints have physical L1 diameter at most 16.  Coordinates, relation
types, logical symplectic quotients, phase-aware logical actions, and transfer
paths are exact under all 24 proper-cubic frames and all 576 products at L5
and held L6.

The sink is an actual stabilizer subsystem, not merely a CNOT register.  Its
stabilizer rank, complete centralizer modulo stabilizers, explicit logical
gauge algebra, deletion response, lawful domain, and direct-sum target
commutants are recomputed.  It is a CSS reference code and **not a completed
non-CSS code**.

The three-bit code exactly matches Cycle 550's minimum Wilson information and
has an exact local transfer of the syndrome/Wilson source family.  It leaves
the six frame-source M2 per cell untouched and is therefore not a retirement
of all six Cycle-547 branch fields.  It is not yet sufficient for the current
target-transparent covariant recurrence: 300 L5 and 432 L6 displayed target
generators have a nonzero signed-frame character.  The exact missing lemma is
an all-24 isometry that removes the three frame logicals while intertwining
every such generator.  Cycle 544 excludes the Pauli-affine subclass, not all
subsystem/non-Clifford constructions.

The six-bit code is sufficient for the existing Cycle-547 relational algebra.
It relocates both the syndrome/Wilson and frame source families by local
remote SWAP, leaves all six old field families blank, and preserves

```text
L(O)=O product_a Z(s_a)^eta_(a,0)(O) CZ(s_a,b_a)^chi_a(O),
C^dagger O C=L(O).
```

The sink is terminal gauge/reference content, not leakage.  Cycle 553 does
not prove that six bits are minimal.  The certified interval is
`3 <= retained bits <= 6`.

The rough-code input remains supplied.  Full Cycle-537 `Gamma(P)`, mass,
contact, seam, both matter parities, inverse, leakage, deletion, lawful-domain,
and held-L6 tests replay.  The target factor is preserved exactly by direct
sum.  A full `E G_coarse = G_physical E` recurrent update and product/reset
rough-code encoder remain open.

Broad negative gate: **FAIL / DO NOT SHIP**.  There is no shared substrate
obstruction and no axiom pressure.

## Physical sink codes

For signed direction `d`, coarse cell `x`, and its signed vector `D_d`, place

```text
r[Wilson sink,d,x] = 16x + 1 D_d,
r[frame sink,d,x]  = 16x + 3 D_d             (mod 16L).
```

The Wilson family stores equal opposite copies.  The frame family stores the
Cycle-547 complementary signed activation pair.  For every cell and axis,

```text
S_W(a,x) = + Z[W,+a,x] Z[W,-a,x],
S_b(a,x) = - Z[b,+a,x] Z[b,-a,x].
```

For each family and each signed copy, support-two `+ZZ` checks connect that
copy across every undirected nearest-neighbor coarse edge.  Thus all copies
of one axial logical belong to one connected component.  The minus phase in
the frame opposite-pair check enforces anti-equality without changing rank or
commutation.

For `N=L^3`, one family has `6N` M2, rank `6N-3`, and three logical qubits.
Two families have `12N` M2, rank `12N-6`, and six logical qubits.  A logical
`Z` is any one signed copy.  A logical `X` is the product of `X` over both
signed copies and all cells for that axis.  The latter support grows with N;
the local recurrence reads logical `Z` copies and never calls this a bounded
logical-X encoder.

| sink-code control | 3-bit L5 | 3-bit L6 | 6-bit L5 | 6-bit L6 |
|---|---:|---:|---:|---:|
| physical sink M2 | 750 | 1,296 | 1,500 | 2,592 |
| M2 per coarse cell | 6 | 6 | 12 | 12 |
| displayed local constraints | 2,625 | 4,536 | 5,250 | 9,072 |
| constraint rank | 747 | 1,293 | 1,494 | 2,586 |
| code exponent | 3 | 3 | 6 | 6 |
| sink gauge quotient dimension/rank | 6/6 | 6/6 | 12/12 | 12/12 |
| full sink commutant dimension/rank | 6/6 | 6/6 | 12/12 | 12/12 |
| phase inconsistencies | 0 | 0 | 0 | 0 |
| site / rough-site collisions | 0/0 | 0/0 | 0/0 | 0/0 |
| maximum check support / diameter | 2/16 | 2/16 | 2/16 | 2/16 |
| lawful branch cases / failures | 8/0 | 8/0 | 64/0 | 64/0 |

The explicit logical `X,Z` pairs exhaust the complete stabilizer centralizer
modulo stabilizers; there is no undeclared sink logical.  Constraint-constraint
and logical-constraint commutator failures are zero.

A proper frame permutes family, direction, and cell labels.  On canonical
logical representatives its exact phase-aware action is

```text
Z[frame,+a] -> (-1)^sign_flip Z[frame,target(a)],
X[frame,a]  -> X[frame,target(a)],
Z/X[Wilson,a] -> Z/X[Wilson,target(a)].
```

The frame-`Z` sign is the physical `-ZZ` anti-equality relation, not a phase
dropped in the symplectic quotient.  All-24 coordinate, constraint-relation,
logical-symplectic-quotient, and phase-aware logical-action failures are zero.
All-576 site-action and phase-aware logical group-law failures are zero.

Deleting the seven bounded checks incident on one sink M2 isolates that M2.
The stabilizer rank drops by one and the code exponent grows by one at both
sizes and in both codes.  This is a bounded deletion control.  Removing one
redundant displayed edge would not change the code and is not misreported as
a falsifier.

## Exact reversible physical transfer

The source fields are the lawful Cycle-547 arrays:

```text
frame source    16x + 5D_d,
syndrome source 16x + 6D_d.
```

For every cell and signed direction, a remote SWAP exchanges the source M2
with its sink M2.  It is compiled along the signed axial path by forward
nearest-neighbour SWAPs and the reverse word excluding the final edge.  This
exchanges the endpoints while restoring every intermediate M2 exactly.

```text
frame distance  = 2, primitive word length = 3,
Wilson distance = 5, primitive word length = 9.
```

All frame-family transfers occur as one disjoint covariant layer sequence;
all Wilson-family transfers occur as the second.  The family phase order is a
rotation-invariant scalar distinction, not an axis or frame choice.  Within
every primitive layer, operand collisions are zero.

| transfer control | 3-bit L5 | 3-bit L6 | 6-bit L5 | 6-bit L6 |
|---|---:|---:|---:|---:|
| endpoint pairs | 750 | 1,296 | 1,500 | 2,592 |
| forward NN SWAP calls | 6,750 | 11,664 | 9,000 | 15,552 |
| forward-plus-inverse calls | 13,500 | 23,328 | 18,000 | 31,104 |
| NN / endpoint / layer failures | 0/0/0 | 0/0/0 | 0/0/0 | 0/0/0 |
| all-24 route-coordinate failures | 0 | 0 | 0 | 0 |
| endpoint-permutation failures | 0 | 0 | 0 | 0 |
| inverse truth failures | 0 | 0 | 0 | 0 |
| declared global branch assignments | 8 | 8 | 64 | 64 |
| declared state-transfer / terminal-lawful / inverse failures | 0/0/0 | 0/0/0 | 0/0/0 | 0/0/0 |
| Cycle-547 displayed source rows per transferred family | 1,125 | 1,944 | 1,125 | 1,944 |
| terminal sink rows per transferred family | 2,625 | 4,536 | 2,625 | 4,536 |
| untouched Cycle-547 frame-source M2 | 750 | 1,296 | 0 | 0 |
| all frame and syndrome source M2 terminally blank | false | false | true | true |

On the declared blank-sink domain, every **transferred** source family ends
blank and the sink inherits its globally consensed branch values.  Reversing
the physical word restores those sources and blanks those sink M2.  The
physical endpoint operation is an arbitrary-state unitary SWAP, not
measurement, copying, reset, or postselection.  Deleting the last primitive
SWAP leaves a nonidentity endpoint/intermediate permutation residual (`2` per
family), so the inverse audit is sensitive.  In the three-bit route only the
syndrome/Wilson family is transferred: all `6N` Cycle-547 frame-source M2 are
untouched, and this route cannot reduce the full Cycle-547 physical content
without the missing frame-compression isometry.

The terminal code-law claim is deliberately narrower than the arbitrary-state
SWAP claim.  Cycle 547 displays `9N` source-constraint rows per family (the
opposite-pair rows and direction-line neighbor rows), whereas the terminal
sink displays `21N` rows per family because it includes all three spatial
neighbor directions.  There is no one-to-one stabilizer/check-group
conjugation and no changing-check law or code-deformation construction here.
Instead the runner exhausts all 8 three-bit or 64 six-bit globally consensed
branch assignments: source-to-blank-sink SWAP gives a terminal sink satisfying
the stronger local checks, transferred sources are blank, and the inverse
restores the source and blank sink with zero failures.  For the frame family,
product blank `|00>` is outside the terminal `-ZZ` anti-equality code; this is
why the result is stated as a declared-domain state-space transfer rather than
as simultaneous source/sink check enforcement.

Intermediate paths cross installed active microgrid roles, but the remote
SWAP word restores them exactly.  No path is treated as empty host memory.

## Exact Cycle-532 and Cycle-537 commutants

The sink has disjoint support from the base code.  Therefore its complete
centralizer is an exact Pauli direct sum with the enumerated base commutant.
The runner does not infer “gauge” from code exponent: it separately enumerates
the sink centralizer, proves that the displayed sink logicals exhaust it, and
then assembles the base-plus-sink quotient dimensions and symplectic ranks.

Matter representatives acquire identity on the sink.  Explicit gauge
representatives acquire all sink `X,Z` logical pairs.  Hence matter dimensions
and ranks remain unchanged, gauge and full-commutant dimensions/ranks each
increase by `2k`, and the shared parity radical remains one-dimensional.

### L5

| base / sink | total M2 | stabilizer rank | code exponent | matter dim/rank | gauge dim/rank | full commutant dim/rank |
|---|---:|---:|---:|---:|---:|---:|
| Cycle532 + 3 | 3,500 | 2,623 | 877 | 1,499/1,498 | 255/254 | 255/254 |
| Cycle532 + 6 | 4,250 | 3,370 | 880 | 1,499/1,498 | 261/260 | 261/260 |
| Cycle537 + 3 | 3,620 | 2,743 | 877 | 1,499/1,498 | 255/254 | 255/254 |
| Cycle537 + 6 | 4,370 | 3,490 | 880 | 1,499/1,498 | 261/260 | 261/260 |

### Held L6

| base / sink | total M2 | stabilizer rank | code exponent | matter dim/rank | gauge dim/rank | full commutant dim/rank |
|---|---:|---:|---:|---:|---:|---:|
| Cycle532 + 3 | 6,048 | 4,534 | 1,514 | 2,591/2,590 | 437/436 | 437/436 |
| Cycle532 + 6 | 7,344 | 5,827 | 1,517 | 2,591/2,590 | 443/442 | 443/442 |
| Cycle537 + 3 | 6,228 | 4,714 | 1,514 | 2,591/2,590 | 437/436 | 437/436 |
| Cycle537 + 6 | 7,524 | 6,007 | 1,517 | 2,591/2,590 | 443/442 | 443/442 |

Cross-support matter-sink and base-gauge-sink commutator failures are zero by
literal bit support.  The explicit base gauge plus sink logical algebra
exhausts the full matter commutant in all eight base/size/sink cases.  Both
matter parities remain nonempty, matter and gauge parity keep their inherited
shared center, and the sink introduces no new radical.

## Three bits versus six

Cycle 550 proves that three distinguishing bits are necessary if all eight
Wilson sectors are admitted reversibly.  Cycle 553 now constructs a physical
three-bit code and exact syndrome/Wilson transfer, so three are also sufficient
for the **sector-information and dimension ledger**.  It leaves `6N` frame
source M2 untouched and does not yet retire or compress the complete six-field
Cycle-547 representation.

That does not yet make three sufficient for the current covariant target
interface.  The two signed correction membranes differ by target logical
action.  In the Cycle-547 displayed algebra, the number of generators with a
nonzero `chi` side character is 300 at L5 and 432 at L6.  Erasing the frame
logical removes the corresponding `CZ(s,b)` factor.  The missing lemma is:

> Construct an all-24 covariant physical isometry from the six-bit relational
> branch code to the three-bit Wilson sink that blanks the frame subsystem and
> intertwines every `chi`-dependent target generator.

The exact Pauli-affine Wilson-flipper solve is empty for all three axes, but a
general subsystem deformation or non-Clifford isometry is not excluded.

Six bits are sufficient because the six-bit sink is isomorphic, on its lawful
branch domain, to the complete Cycle-547 `(s,b)` relation.  It preserves every
branch factor rather than averaging it.  Six are not shown necessary; the
current result leaves a genuine `3..6` optimization interval.

## Recurrence interface

After transfer, the sink copies sit nearer the cell center than the old fields
but remain a constant distance from each correction face.  A membrane face at
signed offset eight uses Wilson sink offset one and frame sink offset three in
the nearest adjacent cell.  Every controlled factor has support three and
maximum physical L1 diameter seven.  There are 150 factors at L5 and 216 at
L6.  Sink coordinates and the signed membrane set rotate covariantly.

The correction controls only sink computational values and therefore
preserves every sink `Z` constraint.  The sink is persistent gauge/reference
state, not terminal leakage.  The full target matter algebra has the exact
six-bit relational intertwiner.  The inherited `Gamma(P)`, mass, contact, and
seam operators extend by the appropriate sink factors.

This is an algebra and locality **recurrence interface**, not a completed
recurrent law.  Cycle 537 itself records that the correlated shadow coin and
reverse-A transition are not synthesized and does not claim a full physical
update intertwiner.  Cycle 553 likewise sets the full update claim false.

## Comparison with promised-plus preparation

The promised-plus product-encoding route starts in one Wilson sector and
therefore needs no three-bit Wilson sink.  It must still build the full lawful
rough/fill code from product/reset matter and gauge inputs.  That encoder is
not constructed here.

The retained-field route accepts arbitrary Wilson sectors and keeps the
branch relation as physical gauge/reference content.  Its input domain and
terminal Hilbert space are larger.  These routes solve different contracts
and are not evidence for or against one another.

## Supplied-structure inventory

Supplied:

- the Cycle-527 scale-16 microgrid and ordinary NN SWAP law;
- the lawful Cycle-532 rough-code input and target/gauge interpretation;
- Cycle-547 lawful source fields after its product/reset consensus;
- macro-cell partition, family offsets one and three, and the scalar transfer
  phase order `frame then Wilson`;
- periodic L5 and held-L6 geometry.

Constructed:

- the physical three- and six-logical-qubit CSS sink codes;
- all local checks, phases, logical pairs, complete sink centralizers, and
  all-24 symplectic-quotient and phase-aware logical actions;
- the exact source-to-sink NN remote-SWAP and inverse, with terminal sink-code
  membership exhaustively checked on the declared global branch domain;
- all Cycle532/537 direct-sum matter commutants and parity accounting;
- the six-bit relational recurrence interface and exact specification of the
  still-missing three-bit lemma.

Not constructed:

- a non-CSS subsystem code;
- an autonomous product/reset encoder for the rough matter/gauge code;
- a reversible preparation of the Cycle-547 lawful source fields from pure
  blanks (their existing preparation is dissipative);
- a one-to-one source/sink check-group conjugation or autonomous changing-check
  law;
- a proof that three frame bits can be removed, or that six are minimal;
- a full recurrent physical update, causal clock, gravity/source, Born, or
  realized-history law.

## No-go discipline N1–N8

### N1 — Alternative-route enumeration

1. **Six-bit persistent CSS relational sink:** constructive in this cycle for
   code, commutant, transfer, inverse, and local recurrence interface.
2. **Three-bit Wilson-only CSS sink:** constructive for information storage,
   ranks, commutant, and syndrome/Wilson transfer; the Cycle-547 frame source
   remains untouched and target-intertwining frame removal remains open.
3. **Proper-cubic non-CSS/subsystem compression:** open; no completed non-CSS
   code is claimed.
4. **Promised-plus local-Clifford/product encoder:** open and has a different
   input domain.
5. **Dissipative branch retirement:** live with an explicit bath and no exact
   inverse; target coherence must be rechecked.
6. **Persistent puncture/changed topology:** live; it changes the terminal
   commutant and must be enumerated.
7. **Direct recurrent relational dynamics:** open beyond the present algebra
   interface.

### N2 — Wall-independence audit

Three walls remain separate:

- `W_frame-compress`: reduce six relational bits toward the three-bit Wilson
  minimum while preserving all `chi` target characters and covariance;
- `W_prepare`: construct the rough matter/gauge code and lawful source fields
  from the declared product/reset domain;
- `W_recur`: synthesize the complete physical recurrent update on target,
  gauge, and sink.

The complete pairwise audit of this collapsed three-wall set is:

| pair | first implies second? | second implies first? | disposition |
|---|---|---|---|
| `W_frame-compress`, `W_prepare` | No.  A three-bit intertwining isometry can consume the already supplied lawful rough/source state without preparing it from product/reset inputs. | No.  A product/reset encoder may prepare the existing six-bit relational state while leaving all frame logicals present. | independent |
| `W_frame-compress`, `W_recur` | No.  Removing the frame family does not synthesize the correlated shadow coin, reverse-A transition, or complete target/gauge update. | No.  A recurrent law can act on the sufficient six-bit sink without compressing it to three bits. | independent |
| `W_prepare`, `W_recur` | No.  Preparing the lawful input code does not synthesize its recurrent dynamics. | No.  A recurrent law declared on the supplied lawful code space need not encode that space from product/reset inputs. | independent |

Thus no closure among the three walls entails either of the other two.  A
six-bit sink closes storage without closing preparation or recurrence; a
three-bit isometry would close compression without preparing the rough code;
and a preparation or recurrent construction can retain all six relational
bits.

### N3 — Hidden-wall scan

The macro-cell partition, source-field preparation, family offsets, family
phase order, periodic domain, sink phases, persistent terminal gauge, and
unbounded logical-X support are declared.  The sink is not called blank,
leakage, a Record, or realized history.  No runtime frame selector, global
Jordan–Wigner order, host parity callback, postselection, or hidden reset is
used in the transfer.  The three-bit route is named syndrome-only, with the
frame source untouched.  The terminal stronger-check claim is restricted to
the 8/64 declared global branch assignments; neither check-group conjugation
nor code deformation is supplied.  The full update and pure-state field
preparation are named missing.

### N4 — Residual matching

Cycle 532 supplies three Wilson rank increments.  Cycle 550 proves the narrow
three-bit reversible information minimum.  Cycle 547 supplies three additional
frame characters for target transparency.  Cycle 553 matches both exactly:
the three-bit code restores the factor-eight dimension, while the six-bit
code reproduces every `Z(s)` and `CZ(s,b)` character.  The direct-sum
commutant gains exactly `2k`, with no unexplained radical or target change.

### N5 — Rhetoric audit

- “Subsystem” means the enumerated sink logical algebra is appended to the
  target commutant as gauge/reference content.
- “CSS” is used accurately; no non-CSS construction is claimed.
- “Exact transfer” is the arbitrary-state physical remote SWAP from an already
  lawful source, not preparation of that source.  Terminal membership in the
  stronger sink check space is proved only for all declared 8/64 global branch
  assignments; no one-to-one check-group conjugation or code deformation is
  claimed.
- “Transferred sources blank” refers only to the families actually moved.  In
  the three-bit route the frame source is untouched; all six old field families
  are blank only in the six-bit route.
- “Local” applies to checks, transfer primitives, and recurrence controls;
  logical `X` support grows with volume.
- “Six sufficient” refers to the existing Cycle-547 relational interface;
  “six minimum” is explicitly not claimed.
- Transfer depth is not physical time, phase is not energy, and the sink is
  not a Record.

### N6 — Partial-closure path scan

1. Search for a proper-cubic Clifford/non-Clifford frame-compression isometry
   and test every `chi` generator, not only rank.
2. Promote the CSS sink to a genuinely local subsystem gauge code with bounded
   representatives for both logical quadratures.
3. Compile the complete lifted Cycle-230 update on target plus sink.
4. Independently attempt the promised-plus product/reset rough encoder.
5. Replace the supplied dissipative source-field preparation with a reversible
   autonomous field encoder or declare its bath as permanent resource.

### N7 — Steelman

The strongest compression rival uses the sink gauge freedom rather than a
Pauli membrane.  A non-CSS subsystem code could absorb the side-difference
logical into gauge and realize an all-24 isometry with only three persistent
qubits.  Cycle 544's Pauli-affine failure does not exclude that construction.
The strongest preparation rival never creates arbitrary Wilson branches: a
local-Clifford/product encoder targets the plus sector directly.  Both remain
live and sharply specified.

### N8 — Cross-cycle echo

Cycles 532, 544, 547, 550, and 553 now agree on an exact information ledger:
three Wilson labels distinguish the rough sectors; three frame labels retain
the signed correction relation; erasure needs a bath or changed terminal
space; persistence gives an exact commutant.  This is constructive convergence,
not evidence that six bits or CSS form is fundamental.  Because compression,
non-CSS, promised-sector, dissipative, and changed-topology routes remain
live, no broader minimum or axiom-pressure claim survives N1–N8.

## Six-wall and TOE dependency update

| wall | Cycle-553 effect |
|---|---|
| `C_ref` | Advances substantially: the retained relation is now an explicit local CSS code with exact transfer, inverse, commutant, and covariance.  Three-to-six compression remains open. |
| `C_num` | Sharpens: three sink qubits exactly restore the Wilson factor; six support the current relational target; minimum six is not established. |
| `C_wrap` | Inherited seam/wrapped-phase controls replay; no wrapped phase is called energy. |
| `C_int` | Advances at the algebra interface: every mass/contact/seam operator has the six-bit relational lift.  Full recurrent dynamics remains open. |
| `C_local` | Advances: support-two constraints, support-two NN transfer, support-three recurrence controls, constant 6/12 M2 per cell, all24/576, deletion, and held-size recurrence are explicit. |
| `C_source` | Unchanged: no autonomous source/resource/gravity law is added. |

Maturity remains operational quantum/records `3/5`, time `1/5`,
inertia/matter `2/5`, gravity/source `1/5`, Born/probability `1/5`.  The sink
is a reference/gauge subsystem, not yet a realized Record.

## Disposition and next campaign

The six-bit persistent CSS sink is retained as the strongest constructive
reference compiler.  The three-bit sink is retained as the exact lower-bound
and compression testbed.  Neither is an axiom candidate.

The highest-value next campaign is the exact missing lemma: attempt an
all-24 subsystem/Clifford/non-Clifford isometry that removes the frame family
while preserving all 300/432 `chi` characters.  A clean failure across those
normalized routes would tighten the `3..6` interval; a positive would reduce
the physical reference content immediately.  The promised-plus product
encoder remains the independent preparation campaign.

## Cold certificate

The final cold command was:

```text
/usr/bin/time -lp python3 \
  scripts/physical_proper_cubic_persistent_subsystem_sink_cycle553_2026_07_21.py \
  --mode persistent-sink-certificate
```

It passed `10/10` top-level tests.  Internal elapsed time was
`214.64554966706783 s`; external wall time was `216.03 s`.  Maximum RSS was
`134,430,720` bytes with zero process swaps.  The pinned Cycle-537 target
replay completed at `147.8579746671021 s`; all sink codes, transfers,
Cycle-532 factorizations, direct sums, and recurrence controls completed at
`214.6452594170114 s`.  The hard wall was 1,200 seconds.

Zero cold residuals include sink phase inconsistency, constraint and gauge
commutators, unaccounted commutant logicals, site collisions, lawful-domain
violations, all-24 coordinate/relation/symplectic-quotient/phase-aware-logical/
route covariance, all-576 site-action and phase-aware logical group law,
NN/endpoint/layer transfer, all 8/64 declared-domain state transfers, terminal
stronger-check membership, transferred-source blanking, exact inverse,
remote-SWAP permutation, matter-sink cross commutators, target leakage, and
inherited physics residuals subject to their declared tolerances.  The cold
certificate explicitly records that one-to-one source/sink check-group
conjugation and changing-check/code-deformation construction are false.  It
also records 750/1,296 untouched frame-source M2 in the three-bit route.
Nonzero sensitivity controls remain: deleting one sink site's seven incident
checks drops rank by one; deleting the last remote-SWAP primitive gives
permutation residual two per family; and 300/432 target generators retain a
frame-side character, keeping the three-bit recurrence lemma genuinely open.
