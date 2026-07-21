# Physical rough-FSWAP Pauli-rotation gate compiler — Cycle 540

Date: 2026-07-21
Authority: none
Audit: unset
Constitutional effect: none

Companion runner:

`scripts/physical_rough_fswap_pauli_rotation_gate_compiler_cycle540_2026_07_21.py`

## Result

Cycle 540 closes Cycle 532's literal one-/two-M2 schedule obligation for each
support-13 mapped FSWAP block on the declared route-zero microgrid code space.
Every primitive is either a one-M2 basis/phase gate or a nearest-neighbor
two-M2 CNOT.  Every route has bounded diameter and a size-independent gate
profile at L5 and held L6.

The exact logical identity uses four pi/4 rotations in physical application
order:

```text
R_-(B_u), R_-(B_u), R_-(Ahat), R_+(B_u B_v Ahat),

R_s(P) = (I+s iP)/sqrt(2).
```

With `B_u=ZI`, `B_v=IZ`, and `Ahat=YX`, the four rotations give

```text
R_4 R_3 R_2 R_1 = -i FSWAP.
```

The raw matrix residual against `-i FSWAP` is
`6.661349775818914e-16`.  Multiplying the operator convention by `+i` per
block gives the Cycle-532 FSWAP convention with the same residual.  This
global phase bookkeeping is not a physical gate, wrapped energy, or time.

The logical and physical conjugation laws are exact:

```text
B_u       -> B_v,
B_v       -> B_u,
Ahat      -> -\widehat A.
```

The maximum matrix residual is `1.3322676295501878e-15`.  Every one of the
375 L5 and 648 held-L6 outer edges is compiled, including all periodic seam
orientations and Pauli signs.  All completed blocks commute with the fixed
stabilizers and full `N-1` gauge algebra.  The complete Cycle-529 full-Fock
Gamma(P) replay and Cycle-532 mass/contact/seam fixtures remain exact.

The closure is conditional on an explicit routing resource: one reset blank
M2 on every odd-coordinate point of the period-32 integer microgrid.  That is
28,672 blank route M2 per coarse period cell, in addition to 22 active rough
code M2.  The construction is deliberately generous rather than optimized.
It proves literal bounded compilation, not a minimum blank density or gate
count.

Cycle 532's separate three-Wilson topological initialization remains open.
Cycle 540 does not change that disposition and creates no axiom pressure.

## Exact target contract

| field | contract |
|---|---|
| Target | replace each Cycle-532 support-13 FSWAP polynomial by a literal bounded one-/two-M2 schedule |
| Domain | the fixed-spin rough-gauge code tensor route blanks initialized to `|0>`; every outer edge at L5 and held L6 |
| Allowed | supplied reset blank M2, one-M2 Clifford/Rz gates, nearest-neighbor two-M2 CNOT, finite boundary color tables, compiler framing/tie conventions |
| Forbidden | treating the support-13 polynomial as a primitive gate, non-nearest-neighbor CNOT, host parity service, runtime frame selection, or hidden route-state preparation |
| Required controls | stabilizer/gauge commutation, conjugation, full Gamma(P), mass/contact/seam, inverse, leakage, deletion, perturbation, all 24 frames and 576 products |
| Completion witness | explicit primitive schedule with route-zero intertwiner and bounded support/count/diameter |
| Not closure | a logical four-rotation identity without physical words, an abstract parity gadget without routes, or an unprepared blank bus |

## Four-rotation identity

Let

```text
P_1=P_2=B_u,
P_3=Ahat,
P_4=B_u B_v Ahat,
s=(-1,-1,-1,+1).
```

The runner constructs all four `4 x 4` matrices independently.  It applies
them in the written order, so the matrix product is `R_4 R_3 R_2 R_1`.
Testing the reverse matrix convention would give the wrong odd-sector signs;
the application-order statement is load bearing.

The product has zero phase-optimized FSWAP residual, zero unitarity residual
to `1.34e-15`, and the exact inverse obtained by reversing the factors and
their signs.  Deleting any one rotation gives:

```text
phase-optimized matrix residual: 1.530733729460359,
target overlap magnitude:        0.7071067811865474.
```

Thus the four displayed rotations are all active in this factorization.  No
minimum-rotation theorem is claimed.

## Actual physical Pauli words

For an oriented outer edge `(u,v)`, Cycle 540 uses the actual Cycle-532 words

```text
B_u,
B_u,
Ahat_(u,v),
B_u B_v Ahat_(u,v).
```

Orientation reversal is explicit: `Ahat_(v,u)=-Ahat_(u,v)`.  The Pauli parser
converts `i^phase X^x Z^z` into a tensor word over `X,Y,Z` plus a real sign;
that sign changes the compiled Rz angle where required.  This is essential on
the periodic seam.

There are two exact schedule profiles:

| outer-edge profile | count L5 | count held L6 | supports `(B_u,B_u,Ahat,B_uB_vAhat)` |
|---|---:|---:|---|
| nonseam | 300 | 540 | `(6,6,7,9)` |
| periodic seam | 75 | 108 | `(6,6,11,5)` |

The union support is exactly 13 on every edge.  Seam `Ahat` and
`B_uB_vAhat` both carry tensor sign `-1`; the compiled Rz sign absorbs it.
No global ordering or parity query is used.

For every physical edge, exact Pauli conjugation through the four rotations
has zero failures for `B_u<->B_v` and `Ahat->-Ahat`.  Every rotation generator
commutes with every fixed stabilizer and every explicit bounded gauge
generator.  This directly checks the actual physical words rather than only
the two-mode logical matrices.

## Literal Pauli-rotation gadget

For a Hermitian physical Pauli word `P`, the schedule is:

1. map each physical `X` to `Z` with `H`, and each `Y` to `Z` with
   `Sdg` then `H`;
2. compute the product parity into the outer-face root with a
   leaves-to-root CNOT ladder;
3. apply `Rz(-s sign(P) pi/2)` to the root;
4. reverse every CNOT; and
5. undo the basis changes with `H` or `H` then `S`.

The primitive alphabet is therefore:

```text
one M2: H, S, Sdg, Rz(+pi/2), Rz(-pi/2),
two M2: nearest-neighbor CNOT.
```

The runner symbolically conjugates root `Z` backward through every CNOT and
requires the result to be `Z` on every route-tree node.  Route nodes are
initialized to `Z=+1`, so their factors disappear on the route-zero code
space and leave exactly the data Pauli.  Reversing the ladder returns every
blank to `|0>` for arbitrary data input.

The exact schedule counts are:

| quantity | nonseam block | seam block | bound |
|---|---:|---:|---:|
| one-M2 gates | 16 | 16 | 16 |
| two-M2 CNOTs | 760 | 744 | 760 |
| total primitive gates | 776 | 760 | 776 |
| largest single rotation tree | 108 M2 | 166 M2 | 166 M2 |
| largest single rotation primitive count | 221 | 337 | 337 |
| complete block routing L1 diameter | at most 33 | at most 33 | 33 |
| maximum root L1 radius | at most 17 | at most 17 | 17 |

These counts are intentionally not optimized.  The duplicate `B_u` rotations
are compiled separately to preserve the verified factor contract.

## Explicit nearest-neighbor microgrid

Cycle 532 places all 22 active roles at even integer coordinates in a
period-32 macrocell.  Cycle 540 supplies route M2 at precisely

```text
{r in Z^3 : at least one coordinate of r is odd}.
```

There are

```text
32^3 - 16^3 = 28,672
```

such blank sites per coarse period cell.  The set is invariant under all
proper-cubic signed coordinate permutations.

For each support site, an explicit path first lifts to an odd transverse
coordinate, walks in the ordered bond frame, creates a second odd-coordinate
guard before changing the first lift, and enters the root only on the final
step.  Every interior position therefore belongs to the supplied blank set.
Every path edge has physical L1 length one.  The union of the paths is reduced
to a rooted spanning tree with a supplied lexicographic tie rule.

No unrelated active M2 is used as a bus.  The largest tree contains 166 M2 and
has diameter bounded independently of L.  The route reservoir is extremely
sparse in logical use but dense in supplied physical sites.  Reducing that
density is an optimization campaign, not part of this existence certificate.

## Whole-layer conflict schedule

Different completed FSWAP blocks commute in the target matching, but their
primitive route trees can overlap.  The runner builds the actual route-site
conflict graph and supplies a greedy finite-boundary coloring:

| size | blocks | maximum conflict degree | supplied color classes | same-color collisions |
|---:|---:|---:|---:|---:|
| L5 | 375 | 10 | 7 | 0 |
| held L6 | 648 | 10 | 6 | 0 |

Within one block, primitives are applied in the listed sequence.  Blocks in
one color class have disjoint route sites and may use the same primitive
index in parallel, padding shorter lists with identity.  Colors are then
executed in their supplied order.  The color number is a compiler layer, not
physical elapsed time.

The finite color tables are supplied structure.  Cycle 540 does not claim an
all-size translation-equivariant color formula or a minimum of six/seven
colors.  It does prove the requested L5/held-L6 collision-free schedules with
constant block support and primitive count.

## Proper-cubic compile-time covariance

At L3, the runner checks every physical factor on every outer edge in all 24
proper-cubic frames:

```text
24 frames * 81 outer edges * 4 rotations = 7,776 factor cases.
```

There are zero transformed-factor mismatches, including 972 cases whose
mapped edge endpoints reverse the stored orientation.  Every transformed
factor recompiles into the same one-/two-M2 alphabet with nearest-neighbor
CNOTs.  The runner also rebuilds and greedily colors the complete 81-block
route conflict graph after each of the 24 recompilations: every framed graph
has maximum conflict degree 10, uses seven color classes, and has zero
same-color route collisions.  Thus covariance covers the executable block
schedule, not only each block's target Pauli word.  The odd-coordinate route
reservoir is frame invariant.

The supplied right-handed ordered bond frame and lexicographic tie convention
are compiler presentation data.  Under a proper-cubic frame, the exact Pauli
word is first transported through Cycle 532's bounded framing Clifford and is
then recompiled.  Because that Clifford can change Pauli letters, the raw gate
list is not required to be only a site permutation.  The compiled operator,
primitive locality, route reservoir, and schedule bounds are covariant.

Cycle 532's complete action on every face `X/Z` generator is rerun for all 576
frame products—684,288 cases, zero mismatches.  There is no active runtime
frame selector.

## Full target, inverse, leakage, and deletions

Each phase-corrected primitive block equals the Cycle-532 mapped FSWAP on the
route-zero code space.  Therefore their complete matching retains:

- the exact quadratic full-Fock Gamma(P) theorem;
- complete L5 and held-L6 vacuum/N=1/N=2 censuses;
- the 4,096-state two-cell full-Fock patch;
- both 988-state straight/corner three-cell controls;
- the one-particle `beta=-0.3` mass residual;
- all 15 `g=0.37` contact phases; and
- the Cycle-230 seam block.

The full inverse is the reversed primitive list: invert `S/Sdg` and the Rz
angle, while `H` and CNOT are self-inverse.  Completed-block code leakage,
gauge transition, and route-blank return residual are zero.

Individual basis changes and CNOTs need not commute with the rough
stabilizers or gauge algebra.  Intermediate leakage is allowed inside the
declared compiler workspace.  Only the completed rotation/block and its
inverse are code-preserving.  No primitive gate is separately promoted to a
physical law update.

Deletion and perturbation controls are explicit:

- deleting any of the four rotations gives residual
  `1.530733729460359`;
- deleting the Rz from one Pauli gadget gives normalized Hilbert-Schmidt
  residual `sqrt(2-sqrt(2))=0.7653668647301795`;
- deleting a leaf parity CNOT gives normalized residual 1;
- an `X` error on a route blank flips the Pauli-rotation sign and gives
  operator-norm residual `sqrt(2)`; and
- perturbing one Rz angle by `1e-4` gives operator-norm residual
  `4.999999999479167e-5`.

Thus blank reset is load bearing and is not hidden inside “routing.”

## Supplied structure and novelty boundary

Supplied rather than derived are:

1. Cycle 532's rough graph, fixed three-Wilson sector, gauge factor, framing
   Clifford, and period-32 active placement;
2. 28,672 odd-coordinate reset blank M2 per coarse period cell;
3. initialization of every used route blank to `|0>`;
4. the right-handed bond frame and lexicographic route-tree tie convention;
5. the L5 and held-L6 greedy conflict-color tables;
6. one-/two-M2 primitives `H,S,Sdg,Rz,CNOT` and their matrices;
7. the `+i` per-block global phase convention; and
8. the Cycle-219 coin and Cycle-230 factor order/contact fixture.

No route pointer or copied parity is called a Record.  No schedule layer is
called time, no Rz angle or generator element is called energy or a rate, and
no source, gravity response, or Born law is inferred.

Cycle 532 supplied the support-13 polynomial and proved its exact target
action.  General Pauli-rotation gadgets and CNOT parity ladders are standard
quantum-circuit techniques; no general novelty is claimed.  Cycle 540's new
fixture-specific content is the exact four-rotation identity in the
Cycle-532 convention, physical-word/sign compilation on every L5/L6 outer
edge, explicit bounded NN odd-grid routes, full conflict coloring,
stabilizer/gauge/conjugation controls, and all-24 framed recompilation.

Thirring machinery is not used or compared.

## Dependency disposition

- `C_ref`: advances locally.  The support-13 block is no longer a primitive
  placeholder.  The period-32 origin, bond tie frame, global phase convention,
  and finite color tables remain supplied.
- `C_num`: unchanged.  Both matter parity sectors remain present.
- `C_wrap`: unchanged.  Rotation phases and compiler layers are not time,
  energy, or Records.
- `C_int`: advances.  The exact B schedule now lies in the same literal
  one-/two-M2 gate class as the onsite/contact compiler; mass/contact/seam
  comparators remain exact.
- `C_local`: advances conditionally.  Literal NN primitive routing, constant
  support/count, L5/L6 collision schedules, and compile-time frame covariance
  close.  Blank microgrid genesis/reset and the inherited Wilson initialization
  remain supplied.
- `C_source`: unchanged.

Maturity scores are unchanged by a compiler-detail closure: operational
quantum/records `2/5`, time `1/5`, inertia/matter `3/5`, gravity/source `2/5`,
and Born/probability `1/5`.

## No-go discipline N1–N8

Broad no-go gate status: **FAIL / DO NOT SHIP**.  Cycle 540 is a
positive construction with explicit supplies, not a minimum-gate, minimum-
blank, all-size-coloring, or topological-preparation no-go.

### N1 — alternative-route normalization

| family | object / mechanism / terminal obligation | status |
|---|---|---|
| odd-grid parity ladder | routed Pauli rotation / reset blank parity tree / literal one-/two-M2 block | **ATTEMPTED — POSITIVE** |
| active-support Steiner tree | only nearby active/selected blank sites / shorter parity tree / collision-free all-edge schedule | **OPEN — NOT ATTEMPTED** |
| movable accumulator | one reset ancilla transported by NN FSWAP/SWAP / sequential Pauli kickback / exact fermionic sign and blank return | **OPEN — NOT ATTEMPTED** |
| local cat parity bus | bounded-degree cat resource / parallel phase kickback / local preparation and uncompute | **OPEN — NOT ATTEMPTED** |
| direct Clifford+T synthesis | support-13 unitary matrix / circuit optimization / better exact one-/two-M2 count | **OPEN — NOT ATTEMPTED** |
| hardware-native multi-Pauli pulse | analog bounded block / direct exponential / reduce gates while retaining the strict one-/two-M2 target | **TARGET-CHANGING, NOT USED** |

The open constructive families forbid minimum-content or uniqueness claims.

### N2 — wall-independence audit

The raw routing labels collapse into two conditions:

```text
W_route-resource:
supply/reset the odd-coordinate blank microgrid, bond-frame tie convention,
and finite conflict coloring used by this literal schedule.

W_topological-encoding:
prepare Cycle 532's fixed all-plus Wilson sector while preserving full matter.
```

They are independent.  A better route tree does not initialize Wilsons, and a
Wilson initializer does not supply blank M2 or primitive routing.  Gate-count
optimization, blank-density optimization, and an all-size color formula are
downstream refinements of `W_route-resource`, not three additional physics
walls.

### N3 — hidden-wall scan

The mandatory scan covers “we assume,” “by construction,” “as is standard,”
“the framework provides,” “bridge context,” “background,” “naturally,”
“obviously,” “standard QFT,” “registered,” and “canonical.”  The period-32
origin, fixed Wilson sector, route blanks, blank-zero initialization, primitive
matrices, bond tie frame, global phase convention, finite color tables, and
intermediate code excursions are all explicit.  The word “standard” in the
prior-art sentence classifies the Pauli gadget; it does not discharge any
resource or proof obligation.

### N4 — residual matching

| witness | witness residual | Cycle-540 use | match? |
|---|---|---|---:|
| `PHYSICAL_ROUGH_GAUGE_SUBSYSTEM_QUOTIENT_CYCLE532_NOTE_2026-07-21.md:142-176` | exact support-13 FSWAP polynomial, literal primitive factorization absent | direct target closed here | yes |
| same note, `:185-210` | bounded onsite Givens/contact words but old two-M2 schedule not transplanted | comparator only; Cycle 540 compiles B, not the onsite words | partial; not negative evidence |
| same note, `:238-284` | three Wilson signs remain supplied initialization | inherited independent condition, not a schedule failure | yes as remaining inventory |
| Cycle 523 | literal onsite one-/two-M2 gate style | primitive-format precedent, not proof of the rough FSWAP schedule | no; not used as proof |

No endpoint-shadow or Wilson-preparation failure is cited against the positive
gate factorization.

### N5 — rhetoric audit

| resolution | tested result |
|---|---|
| logical two-mode block | exact four-rotation matrix and conjugation |
| one physical Pauli word | exact sign parser, tree parity, Rz, uncompute |
| one primitive | one/two M2; every CNOT nearest neighbor |
| one physical outer edge | completed code/gauge commutation and conjugation |
| all L5/L6 outer edges | 375/648 complete schedules; seam and nonseam profiles |
| whole B layer | collision colors and inherited full-Fock Gamma(P) |
| all 24 frames | 7,776 factor recompilations |
| all 576 products | inherited exact physical frame group law |
| all sizes | not certified; no all-size coloring claim |
| minimum gates/blanks | not tested; no minimum claim |

“Literal” is restricted to the supplied route-zero microgrid and declared
primitive alphabet.  It is not widened to resource genesis or optimality.

### N6 — partial-closure path

Cycle 540 follows the import-retirement shape: take explicit route blanks and
tie/color data, prove the bounded primitive theorem, and expose a later
resource-retirement audit.  Candidate retirement paths are a much smaller
Steiner reservoir, a movable accumulator using existing blank lattice sites,
a covariant local conflict-color rule, or an autonomous blank reset law.

These are compiler/resource constructions.  They do not request an axiom edit.

### N7 — hostile steelman

> A hostile reviewer should reject any claim that 28,672 blanks per cell or
> 760 CNOTs are necessary.  The runner deliberately routes every support point
> through the entire odd-coordinate reservoir with a simple star-to-root
> construction.  The actual words touch at most 11 data M2 in a diameter-32
> neighborhood.  A bounded Steiner tree, movable phase-kickback ancilla, or
> cat-state parity bus could reduce both density and depth dramatically while
> preserving the same exact four-rotation identity.  The terminal obligation
> is to build and collision-audit that alternative, not to infer new physics.

The concrete alternatives block all minimum or uniqueness claims.

### N8 — cross-cycle echo

Cycle 523 showed that a logical onsite compiler becomes physical only after a
literal primitive schedule and route inventory are supplied.  Cycle 529
separated exact stateful B algebra from nonlocal code preparation.  Cycle 532
replaced the chart with a local gauge subsystem but left each support-13 block
unfactorized.  Cycle 535 then isolated Wilson initialization from the already
exact runtime.  Cycle 540 retires only the support-13 primitive placeholder.

Earlier routing walls were repeatedly narrowed by adding a center tag, blank
carrier, or finite schedule orbit.  The same mechanisms could reduce this
cycle's generous odd-grid resource.  The cross-cycle echo supports further
optimization, not a no-go or axiom pressure.

## Disposition and next campaign

Retain Cycle 540 as the literal physical gate layer for Cycle 532:

- four verified pi/4 rotations per mapped FSWAP;
- actual physical words and seam signs;
- only one-/two-M2 primitives;
- NN CNOTs on an explicit invariant blank microgrid;
- exact blank return and inverse;
- 375/648 edge-complete schedules;
- six/seven collision colors;
- all-24 framed recompilation and inherited 576 group law; and
- exact full-Fock, mass, contact, and seam preservation.

Do not count its 28,672 blank M2/cell as derived physical economy, do not call
its finite color order time, and do not treat primitive intermediate leakage
as a stabilizer-preserving microstep law.

The optimal next compiler campaign is route-resource compression: construct a
proper-cubic bounded Steiner/cat/accumulator network using far fewer reset
sites and a size-uniform collision coloring.  The optimal overall TOE campaign
still remains the independent Cycle-532 Wilson-initialization route.
