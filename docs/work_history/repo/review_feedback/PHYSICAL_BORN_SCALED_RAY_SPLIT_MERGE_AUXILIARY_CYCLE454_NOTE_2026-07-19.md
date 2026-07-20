# Physical Born scaled-ray split/merge auxiliary — Cycle 454

Date: 2026-07-19
Authority: none
Audit: unset

## Decision

Cycle 454 is a positive constructive follow-on to Cycle 448.  It builds **two
finite binary addition DAGs** on the existing G55 ray with Bloch direction
`(3,-4,0)/5`.  Each addition `A+B=C` is represented by the paired normalized
contexts

\[
(A,B,I-C),\qquad(C,I-C).
\]

The programs use the **actual Cycle-317 projector split isometry**.  Every
scaled ray effect, partial sum, and complement is an ordinary explicit effect
class.  Every auxiliary effect class is counted in the full augmented matrix.
In the frozen contract: **every auxiliary effect class counted**.
No grade homogeneity is assumed.

The retained Cycle 448 rank 33/nullity 23 surface is enlarged from `100 x 56`
to `152 x 104`.  The exact **full augmented rank is 84** and full augmented
nullity is 20.  The **projected-old nullity is 20** as well.  Thus the physical
auxiliary networks remove three further old-grade directions without hiding
their 48 new auxiliary classes.  Seventeen directions beyond the three Pauli
tangents remain.

This is not state or grade uniqueness and is not a Born-law derivation.

## Frozen finite construction

Let `P` be the rank-one projector on the `(3,-4,0)/5` ray.  Two supplied
finite arithmetic networks are installed.

### Centiray network

The atom is `q=P/100`.  Six doubling gadgets construct
`2q,4q,8q,16q,32q,64q`; finite binary additions then reach three existing G55
classes:

\[
23q=E_{44},\qquad61q=E_{11},\qquad77q=E_{45}.
\]

The 16 addition gadgets impose two independent relations among the three old
endpoint grades.  They use 32 normalized contexts.

### E11-centisplit network

The second atom is

\[
q'=E_{11}/100=61P/10000.
\]

Six doublings and four binary additions reach

\[
37q'=E_{14},\qquad100q'=E_{11}.
\]

These ten gadgets impose one further independent old-grade relation with 20
normalized contexts.

Together with the retained Cycle-448 pair, the extension contains 26 binary
addition gadgets and 54 new contexts.  It has 104 total effect classes: the 55
G55 classes, the Cycle-448 `0.36I` complement, and 48 scaled/partial/complement
classes introduced by the two networks.

The choice of ray, atoms, integer targets, addition trees, endpoint classes,
and invocation is supplied finite structure.  The grade constraints and rank
changes are derived from the physical contexts.

## Why this does not assume homogeneity

No equation of the form `g(lambda E)=lambda g(E)` is inserted.  For each
addition gadget, Cycle 317 splits the full projector into fine weights

\[
aP,\quad bP,\quad(1-a-b)P,\quad I-P
\]

and the runner uses two coarse groupings of the same fine isometry.  The first
has effects `(aP,bP,I-(a+b)P)`; the second has effects
`((a+b)P,I-(a+b)P)`.  Effect functionality makes the complement one shared
class.  Normalization of both eligible contexts then derives

\[
g(aP)+g(bP)=g((a+b)P).
\]

Repeated physical additions—not an imported numerical scaling rule—link each
atom to its existing G55 endpoints.  The auxiliary atom begins with its own
free grade.  A network with `m` old endpoints can therefore remove only
`m-1` old directions, which is exactly what the full matrix reports.

## Full augmented incidence result

| diagnostic | exact result |
|---|---:|
| Cycle-448 rows x columns | 100 x 56 |
| Cycle-448 rank/nullity | 33 / 23 |
| binary addition gadgets | 26 |
| added split/merge contexts | 52 |
| all retained-plus-new contexts | 54 |
| full Cycle-454 rows x columns | 152 x 104 |
| full augmented rank/nullity | 84 / 20 |
| projected-old nullity | 20 |
| reduction from Cycle 448 | 3 |
| remaining directions beyond Pauli tangent | 17 |

The maximum residual between the exact algebraic classes and their physical
contact-conjugated representatives is `2.515289221404185e-16`.  The maximum
train/held class residual is `1.8824747269678055e-16`, and the maximum actual
Cycle-317 split-isometry residual is `2.8031485794237153e-16`.

The trace grade normalizes all 152 rows with residual
`1.3322676295501878e-15`.  The three Pauli tangent columns remain in the
homogeneous kernel with residual `9.36435628181429e-16`.  Their rank is three;
the full and projected-old nullities are both 20.

## Deletion and held relations

Whole-family deletions distinguish the three new rank directions:

| deleted family | resulting exact rank | full nullity | projected-old nullity |
|---|---:|---:|---:|
| retained Cycle448 pair | 82 | 22 | 21 |
| centiray network | 53 | 51 | 22 |
| E11-centisplit network | 65 | 39 | 21 |

The large full nullities after network deletion correctly include isolated
auxiliary classes.  They are not projected away.

Two endpoint gadgets are frozen as held relations: `77q=E45` in the centiray
network and `37q'=E14` in the E11-centisplit network.  Removing their four
context rows gives exact rank 80 and projected-old nullity 22.  Restoring them
adds four full-matrix rank directions and removes two projected-old freedoms.
Deleting any one of those four rows raises projected-old nullity from 20 to
21.  Held relation rows therefore test the shared-complement mechanism rather
than merely replaying a fitted coefficient equation.

## L3/L6 physical compiler

All 54 retained-plus-new contexts are compiled separately at train L=3 and
held L=6.  The 52 auxiliary contexts use Cycle 317's literal bounded
projector-split isometries; the retained Cycle-448 pair uses the same physical
positive-square-root compiler as its source cycle.  Every menu has at most
three coarse outcomes and at most four fine Kraus labels, within the retained
three-M2 pointer.

The complete result is:

| diagnostic | result |
|---|---:|
| train/held context programs | 108 |
| involved effect classes | 56 |
| active pointer cases | 272 |
| idle pointer cases | 592 |
| maximum effect residual | `1.8824747269678055e-16` |
| maximum completeness residual | `2.220446049250313e-16` |
| maximum fixed-bank isometry residual | `6.719544934422228e-16` |
| maximum exact E/G residual | `0.0` |
| maximum exact inverse residual | `0.0` |
| leakage failures | 0 |
| protected-packet failures | 0 |
| proper-cubic frames | 24 |
| all-frame packet cases | 2,688 |
| all-frame failures | 0 |
| L3/L6 encoding covariance residual | `0.0` / `0.0` |
| L3/L6 compiled-block covariance residual | `0.0` / `0.0` |
| one-particle mass relative residual | `2.220446049250313e-16` |

Programs are placed in bounded eight-program banks with a three-M2 program
register.  The pointer uses three M2.  The maximum primitive support is three
M2.  These are constant bounds for the frozen finite networks, not optimality
or autonomous-genesis claims.

The same physical effect class produces the same protected packet word across
all its new occurrences, while distinct involved classes separate.  Packet
formation, inverse, support, and payload mapping are tested under all 24
proper-cubic frames.  Candidate packets are not actual Records.  Coherent
norms are not probabilities.  There is no occurrence, probability, frequency,
or Born-law selection.

## Anti-fit and lawful-domain controls

- Replacing one binary coefficient by a value shifted by `1/10000` changes the
  exact radical-coordinate effect key.
- The actual Cycle-317 split constructor refuses a non-normalized split, a
  negative split, and an overweight split: `3/3` malformed schedules refused.
- Removing either context of a held addition raises projected-old freedom.
- L=6 reconstructs every split program and effect; it is not a relabelled L=3
  output.
- Full auxiliary columns remain present in every rank and deletion audit.

## No-Go Discipline Gate

The no-go-discipline skill was freshness-checked against `origin/main` in
Cycle 448; its newer repo copy remains the governing N1–N8 text.  This cycle
does not turn a residual finite nullspace into constitutional evidence.
**Gate disposition: FAIL.**  The result is
`partial-attempt-with-named-untested-routes`.

### N1 — Alternative route enumeration

1. **Two explicit same-ray addition DAGs — ATTEMPTED.**  They construct three
   independent old-grade constraints and reduce nullity from 23 to 20.
2. **The remaining exact rational G55 relations — LIVE / PARTLY SCREENED.**
   Cycle 448 found a fixed-surface rational rank ceiling at old nullity 14;
   Cycle 454 compiles only three of the nine directions beyond its first
   literal collision.
3. **Other G55 rays and mixed-effect addition DAGs — LIVE / NOT ATTEMPTED.**
   The present program freezes one rank-one ray and does not compile general
   positive-effect arithmetic networks.
4. **Larger literal-integer contexts — LIVE / NOT ATTEMPTED.**  Cycle 448
   exhausted only widths through four.
5. **Deliberately enlarged finite physical effect inventories — LIVE / NOT
   ATTEMPTED.**  New directions can alter the exact rational relation field
   and projected rank.
6. **Parametric Cycle-317 refinement families — LIVE / PRIOR POSITIVE
   CONDITIONAL ROUTE.**  Finite binary DAGs do not exhaust the supplied
   parametric same-ray mechanism.
7. **Continuous eligible POVM/functionality route — LIVE / PRIOR CONDITIONAL
   COMPARATOR.**  The Gleason/Busch trace-form route has a broader domain whose
   physical eligibility is not derived here.

Routes 2–7 remain live, so N1 fails for any no-go or minimum-content claim.

### N2 — Wall-independence audit

No independent-wall set is claimed.  The selected ray, two atoms, target
integers, binary-tree topology, and G55 inventory are nested declarations of
one frozen constructive family.  Relaxing them can change the rank.  They are
not inflated into multiple framework walls.

### N3 — Hidden-wall scan

The note and runner were scanned for `we assume`, `by construction`, `as is
standard`, `the framework provides`, `bridge context`, `background`,
`naturally`, `obviously`, `standard QFT`, `registered`, and `canonical`.
Load-bearing inputs are named in the supplied inventory: effect functionality,
context eligibility, atom and target coefficients, network topology, packet
codec, program preparation, and invocation.  No hidden condition is used as
negative evidence.

### N4 — Residual matching

| source | source residual | Cycle-454 use | match? |
|---|---|---|---|
| Cycle 448 exact-context recon | full/projected nullity 23 after one exact context pair | starting incidence residual | yes |
| Cycle 317 contact ternary bridge | bounded physical same-ray split/merge isometry | physical construction of each addition gadget | yes |
| Cycle 440 protected-packet compiler | finite effect-class packet functionality at L3/L6/all24 | packet compiler and covariance surface | yes |
| continuum Gleason/Busch comparator | trace representation on a broader eligible effect domain | current finite nullity | no; retained only as a live counter-route |

No nonmatching comparator is used to support a failure claim.

### N5 — Rhetoric audit

The tested resolution is two fixed finite arithmetic DAGs on one G55 ray.  It
does not cover all rank-one rays, mixed effects, larger finite inventories,
continuous effects, all local blocks, or the lattice-wide substrate.  The note
therefore claims only a three-direction rank reduction on this family.  It
does not say that Born affinity is unavailable at any broader resolution.

### N6 — Partial-closure path scan

The exact rational rank map already supplies an immediate non-axiom next path:
compile the remaining manageable relation vectors with explicit addition DAGs
and complete auxiliary accounting.  Further paths include other rays, mixed
positive effects, enlarged finite menus, and a physical eligibility theorem.
No convention or registry edit is needed to attempt them, and none is silently
treated as a new axiom.

### N7 — Steelman

A hostile reviewer should regard nullity 20 as evidence for continuing the
construction, not stopping it.  Cycle 448's exact rational calculation leaves
six further fixed-G55 relation directions between this result and its
old-nullity-14 algebraic ceiling, and Cycle 454 has now shown how to replace
forbidden grade homogeneity by finite physical addition DAGs with honest
auxiliary columns.  The same method can be extended to the remaining short
relations or generalized beyond this ray.  Nothing here supports a shared
obstruction.

This steelman is decisive, so N7 forces demotion of every negative claim.

### N8 — Cross-cycle echo

The prescribed repository search for `structurally undecidable`, `no retained
primitive`, `requires new axiom`, and `cannot be derived from A_min` was
retained from the Cycle-448 gate.  The relevant echo is constructive: Cycle
317 supplied the physical refinement machinery; Cycle 440 exposed a finite
nullspace without overclaiming; Cycle 448 found one exact literal relation;
and Cycle 454 retires the grade-homogeneity shortcut for three more directions
by adding explicit physical classes.  The historical mechanism is progressive
domain and compiler extension, which remains live.

### Gate result

N1 and N7 fail for a negative claim.  Cycle 454 ships only its positive finite
rank gain and named open routes.  There is **no no-go, minimum-content,
shared-obstruction, or axiom-pressure claim**.

## Supplied / derived / open

### Supplied

- the Cycle-440 G55 effects, effect-functionality premise, 98 eligible menus,
  and protected-packet codec;
- the retained Cycle-448 context pair and `0.36I` complement;
- the `(3,-4,0)/5` ray, the two atom sizes, five target integers/endpoints,
  binary addition topology, and invocation of all 52 auxiliary contexts;
- the Cycle-317 contact, projector split constructor, coarse groupings, blank
  pointer, program banks, local matcher, layouts, payloads, and frame action.

### Derived

- exact identity of all five atom multiples with their old G55 endpoints;
- 26 normalized physical addition gadgets and 48 auxiliary classes;
- the `152 x 104` exact incidence matrix, rank 84/nullity 20, and
  projected-old nullity 20;
- the three-direction reduction relative to Cycle 448;
- trace and Pauli-tangent kernel controls, network deletions, and held-relation
  rank gains;
- train/held physical programs, exact E/G, exact inverse, zero leakage,
  protected packet equality/separation, all-24 covariance, and resource
  bounds.

### Open

- the six further exact rational G55 relation directions between old nullity
  20 and the Cycle-448 algebraic route-map value 14;
- other rays, mixed effects, larger literal contexts, and enlarged finite
  effect inventories;
- reduction to exactly the three Pauli tangent directions;
- autonomous physical genesis and eligibility of the supplied networks;
- selection of a density state, numerical grade, Born probability,
  occurrence, actuality, frequency, or Record formation;
- any route-independent obstruction or axiom pressure.

## Status

Final cold run: **8 pass / 0 fail**.

The strongest constructive result is an honest three-direction reduction of
both full augmented and projected-old grade freedom using explicit Cycle-317
split/merge auxiliaries, with no grade-homogeneity import.  Authority remains
none and audit remains unset.
