# Physical adjacent-star recurrence tournament — Cycle 548

Date: 2026-07-21
Authority: none
Audit: unset
Constitutional effect: none

Companion runner:

`scripts/physical_adjacent_star_recurrence_tournament_cycle548_2026_07_21.py`

## Result

Cycle 548 extends the Cycle-545 recurrence mechanism from two updates inside
one four-cell star to two adjacent degree-three stars sharing a cell and their
common seam.  The union is one **six-cell**, five-seam patch with 36 logical
CAR modes.  Its complete declared domain through total number `N<=2` contains
**667** columns:

```text
1 + 36 + 630 = 667.
```

The two noncommuting lawful sweeps are retained separately as `A_then_B` and
`B_then_A`.  Route B is the strongest constructive result: one fixed-order
global code-space isometry and one **transported**, persistent physical
**slot** implement a two-step recurrence.  The slot alternates which star is
active and returns exactly after the second update.  Route A, one **joint S6**
role, is also exact but has a much larger conceptual decoder.  Route C, one
translation-covariant **eight-color** parity layer, succeeds on even held L6
and fails on odd L5 because periodic parity is not globally consistent there.
That last result is a failure of this coloring rule, not a volume no-go.

This is a fixed bounded compiler theorem.  It does not derive the patch
address, reference, blank auxiliaries, update choice, or physical time.  **No
schedule is time.**

## Geometry and exact target

The cell union is

```text
c0=(1,1,1), c1=(2,1,1), c2=(1,2,1), c3=(1,1,2),
c4=(2,2,1), c5=(2,1,2).
```

Star A acts on cells `(0,1,2,3)` and seams `(0,1,2)`.  Star B acts on
`(0,1,4,5)` and seams `(0,3,4)`.  Cells 0 and 1 are shared: each center is the
other star's leaf, and seam 0 is shared.  Each update is the Cycle-230
free-plus-contact law with the Cycle-219 `beta=-0.3` six-mode coin, three
fermionic FSWAP seams, and `g=0.37` onsite contact on its four addressed
cells.

The certificate tests:

- complete sectors `N=0,1,2`, including contact-sensitive two-particle rays;
- both distinct sweep orders, their inverses, and repeats 1–4;
- one-particle mass, local contact, all five seams, and deletion controls;
- literal one-/two-M2 primitives with nearest-neighbour routing;
- L5 construction and **held L6**;
- all 24 proper-cubic frames and all **576** frame products; and
- the Cycle-532 target-times-gauge comparator without identifying carriers.

## Shared six-cell isometry

For each of L5 and held L6, the fixed cell-factor order `0,1,2,3,4,5` gives
one normalized decoder over all 667 columns.  Every column has 64 branch
products, hence **42,688** decoder rows.  The decoder has 70 native role M2,
106 equality controls, zero branch-pattern collisions, and identical
normalized decoder and order-phase digests at the two sizes.  The maximum
selected representative support is finite and all inherited cell-role,
port, and fixed-sector constraints commute exactly on the declared code.

| item | L5 | held L6 |
|---|---:|---:|
| logical columns | 667 | 667 |
| decoder rows | 42,688 | 42,688 |
| decoder collisions | 0 | 0 |
| native role M2 | 70 | 70 |
| equality controls | 106 | 106 |
| maximum column-norm error | `1.3322676295501878e-15` | same |
| forward-W Toffoli upper count | 27,046,566 | 27,046,566 |

The decoder digest is
`5f82848eef9bfa7a590f1214e3a6e782956d8d1755dbce3ac1de2c75d03a7bde`;
the separately retained factor-order phase digest is
`310cbafcc30fb7dccc7a275b912c1b6f9cb71fbc92c317f7c87993b094af7b1a`.
Both match between construction and held size.  The maximum selected product
support is 26 M2.  All 480 selected cell-role pairs have zero pairing,
port-constraint, and fixed-sector commutator failures.

This proves an algebraic code-space isometry on the declared six-cell patch.
It does not prepare its fixed-Wilson/reference state from product M2.  The
fixed-Wilson/reference preparation is supplied.  Branch, conjunction, tag,
slot, and route-work **blank** genesis is also supplied.

Let the fixed-order encoder be `E`.  During its decoded interval, the same 36
physical occupation-shadow M2 carry both updates.  With

```text
T = |0><1| tensor U_B + |1><0| tensor U_A,
```

the slot toggles on every step and

```text
T^2 = diag(U_B U_A, U_A U_B).
```

Thus it returns after two updates and selects either lawful order by its
initial local value, without a host query.  On the declared code space,

```text
E (U_B U_A) = G_AB E,
E (U_A U_B) = G_BA E.
```

The exact reverse schedule and the identity `E^dagger E=I` give arbitrary
repeat recurrence.  Intermediate primitives may leave the encoded subspace;
terminal branch, work, route displacement, and slot leakage are zero.

## Route A — joint S6 comparator

The symmetric alternative retains all `6! = 720` cell-factor orders in one
10-M2 S6 register.  The 719-Givens uniform preparation and its inverse are
exact to numerical tolerance.  It uses **30,735,360** conceptual
order-resolved decoder rows, 116 equality controls, and 691,200 selected
lookup entries.  Deleting the first order-preparation Givens leaves a
residual `0.03727427366380596`; deleting one complete S6 order amplitude gives
Gram residual `1/720 = 0.001388888888888889`.  The maximum preparation and
inverse residuals are respectively `5.550139255393381e-15` and
`7.363713786656372e-15`.  The conservative forward-W Toffoli upper count is
21,569,872,784 at either size.

Disposition: **EXACT, BOUNDED, SYMMETRIC, BUT LARGE.**  It is an existence
comparator, not an efficiency or minimum-content result.  One joint S6 role
is not six independent overlapping roles.

## Route B — transported returned slot

The retained route uses the fixed factor order in the transported patch
frame, one persistent 36-M2 occupation register, and one persistent slot.
For either L5 or L6, the **unconditioned decoded A+B base program** contains
69,972 core rows.  Appending its direct-sweep phase correction gives the
69,973 materialized rows in the table below: 6,505 one-M2 calls and 63,468
two-M2 calls.  This materialized base schedule is not by itself the complete
slot-controlled circuit.  It includes 406 Cycle-540 four-rotation FSWAP
blocks.  Their raw accumulated phase is `-1`; one explicit returned-slot
`Rz(2*pi)=-I` correction makes the compiled target phase exactly `+1`.

All primitive supports are one or two M2 and all two-M2 calls are
nearest-neighbour.  Route data are restored, slot and tags return, route
support color collisions are zero, and all mapped edges remain nearest
neighbour in all 24 frames.  The decoded schedule is materialized and hashed.

| size/order | total | one-M2 | two-M2 | schedule SHA256 |
|---|---:|---:|---:|---|
| L5 `A_then_B` | 69,973 | 6,505 | 63,468 | `861b108637681389a911cc14001966fead9933fd49fcb57dbd974efb58df9973` |
| L5 `B_then_A` | 69,973 | 6,505 | 63,468 | `bf65c918f5346bb1c1cb2412b17d5580bcde49de4f84e03ea2841d300b1962d7` |
| L6 `A_then_B` | 69,973 | 6,505 | 63,468 | `861b108637681389a911cc14001966fead9933fd49fcb57dbd974efb58df9973` |
| L6 `B_then_A` | 69,973 | 6,505 | 63,468 | `bf65c918f5346bb1c1cb2412b17d5580bcde49de4f84e03ea2841d300b1962d7` |

Both layouts use 374 compiler-live M2, maximum routed-pair length 80, at most
four route-support colors in a local stage, and zero support, wire,
same-color, or nearest-neighbour collisions.

The physical returned-slot skeleton is explicit.  In each half-cycle it
applies A under slot polarity zero, B under slot polarity one, and then one
literal slot `X`.  Control-on-zero is compiled as
`X / conventional-control / X`, not assumed as a new primitive.  Two halves
therefore contain:

| skeleton item | L5 | held L6 |
|---|---:|---:|
| controlled one-M2 bases -> two-M2 macros | 13,008 | 13,008 |
| controlled two-M2 bases -> three-M2 macros | 126,936 | 126,936 |
| polarity-conversion slot `X` | 4 | 4 |
| literal recurrence slot `X` | 2 | 2 |
| terminal slot `Rz(2*pi)` | 1 | 1 |
| unexpanded skeleton calls | 139,951 | 139,951 |
| required logical-wire pairs | 1,091 | 1,091 |
| required-pair NN route failures | 0 | 0 |

Its symbolic ordered digest is
`747fe8fddfe1b61395b26ebf3b8479cfa277ade22e4ab5de871a548b86bf4e02`
at both sizes.  Maximum required pair-route length is 38 edges.  Every route
is reversed after its macro pair call.

Making each decoded core conditional on the local slot changes a one-M2 core
to a two-M2 core and a two-M2 core to a local three-M2 macro.  The runner
forms each representative controlled 8-by-8 unitary and reconstructs it by
exact two-level QR.  A Gray path plus the inherited Cycle-533 clean
conjunction/Toffoli/uncompute decomposition reduces every such local macro to
one-/two-M2 nearest-neighbour calls.  This exact finite macro expansion is
counted and verified rather than allocating its repeated expanded rows.
The two star updates contain 6,504 controlled one-M2 cores and 63,468
controlled two-M2 cores before the final phase correction.  Across the 14
distinct local core programs, the maximum QR reconstruction residual is
`7.032886469331774e-16` and no program needs more than one nontrivial
two-level rotation beyond its diagonal phases.

At the logical level the runner separately forms
`M=diag(U_A,U_B)` and the literal slot involution `X_slot`.  It verifies
`X_slot M = T` at raw residual zero, `X_slot^2=I` at residual zero, and
`T^2=diag(U_B U_A,U_A U_B)` at residual zero.  The two literal recurrence
toggles are included in the physical skeleton and return the slot.  The raw
selected star program has phase `+i` per half, so the two-half skeleton has
phase `-1`; the terminal `Rz(2*pi)` corrects it to `+1`.

Disposition: **STRONGEST / SMALLEST EXACT ROUTE IN THIS TOURNAMENT.**  The
fixed factor order, patch chart, slot initialization, and two-step program are
supplied bounded presentation data.  The slot is not a Record and its toggle
is not physical time.

## Route C — translated colored layer

The candidate color is the parity triple of the star center.  Along every
axis, an arm points from the even endpoint toward the odd endpoint.  This
gives two transported Margolus presentations and eight color classes.

On even held L6 there are 216 centers, zero same-color support collisions,
and zero frame color-permutation failures over all 24 frames.  On odd L5,
periodic wrap identifies equal parity at a boundary: the route has 90
same-color collisions and 111 frame color-permutation failures.  For example,
centers `(0,0,0)` and `(0,0,4)` have the same color and overlap at `(0,0,0)`.

Disposition: **FAILED AS DECLARED ON ODD L5; PASSES EVEN L6.**  A
boundary-aware finite coloring, a larger translated motif, or Route B can
repair this route.  The failure is neither shared by A/B nor evidence for a
route-independent obstruction.

## Logical fixtures, inverse, and deletions

Both 667-by-667 star updates are unitary on every complete declared sector.
The two sweep orders are genuinely different, with nonzero raw difference.
Their maximum raw difference is `0.753076624400765`, with 61,701 nonzero
entries.  The maximum per-star sector unitarity residual is
`6.661430332022944e-16`.  Across 24 repeat cases, the maximum norm residual is
`4.440892098500626e-16` and the maximum inverse residual is
`3.2086675760508887e-15`.
For each active 24-mode one-particle star, the compiled uniform eigenphase
gives rest mass `0.453405654174885...`, matching the Cycle-219 fixture to
numerical tolerance.  Each four-cell contact is nontrivial on 60 declared
columns.  The shared and nonshared Cycle-230 seams retain their CAR sign.

The certificate separates the following load-bearing deletions:

- deleting star B gives raw residual `1.316097915613727`;
- deleting the shared seam gives raw residual `0.8740010519307571`;
- deleting one decoder minterm leaves a branch;
- deleting one legality minterm rejects a lawful ray;
- deleting one S6 order amplitude gives Gram residual `1/720`;
- deleting the global-sign correction leaves exact raw sign error 2;
- inherited Cycle-540 rotation, Rz, CNOT, and bad-blank controls remain
  nonzero; and
- deleting a return SWAP leaves routed data displaced.

Random normalized sector vectors test both sweep orders, repeats 1–4, norm
preservation, and exact reverse round trips.  This is complete on `N<=2`, not
a sample-only replacement for the explicit sector matrices.

## Proper-cubic covariance

The runner constructs the 36-mode exterior-algebra representation for each
of all 24 proper-cubic frames.  Each individual star and both ordered sweeps
intertwine with their recompiled targets.  All 576 representation products
close.  Separately, every physical live site and every actual route edge is
mapped through the 24 compile-time frames at both L5 and L6, with zero site
injection, nearest-neighbour, or group failures.

The maximum logical update covariance residual is
`6.206335383118183e-17`; the maximum ordered-sweep residual is
`2.2591401799415137e-16`.  There are zero failures in 48 update cases, 48
sweep cases, and 576 frame products.

This is covariance of a transported compiler family.  It is not one raw gate
list invariant under all frames, and it does not use an active runtime frame
selector.

## Carrier and supply boundary

Cycle 548 retains the Cycle-539/Cycle-545 **selected carrier** for the
recurrent compiler.  Cycle 532's fixed-spin **rough carrier** is replayed only
as an independent target-times-gauge comparator for the same target CAR law.
No selected-to-rough physical transducer is supplied, and the two Hilbert
spaces are not silently identified.

Supplied rather than derived are:

1. fixed-Wilson/reference preparation and its fixed sector;
2. branch, conjunction, tag, slot, and route blank initialization;
3. selected coefficients, physical representatives, legality/decoder tables,
   and exact analog angles;
4. the fixed six-cell patch, its chart, factor order, slot program, and sweep
   choice;
5. the Cycle-219 coin and Cycle-230 contact, coupling, ports, and seam order;
6. the L5/L6 periodic boundaries, compile-time proper-cubic frame, and color
   origin; and
7. the complete-domain cutoff `N<=2`.

New here are the six-cell 667-column decoder; adjacent-star logical update;
exact joint-S6 and transported-slot routes; exact returned-slot recurrence;
materialized 69,973-call decoded schedules; controlled-local-core macro
certificate; odd/even colored-layer discriminator; all-frame update/sweep
covariance; and the explicit carrier audit.

The result is not a reference or blank genesis theorem, an arbitrary-network
tiling, an all-sector compiler, autonomous causal time, realized history, a
Record theorem, Born probability, gravity/source response, a minimum theorem,
or an axiom.

## Dependency-ledger effect

- `C_ref`: unchanged.  Fixed-Wilson/reference, blanks, finite tables, patch
  chart, factor order, and compile-time frame remain supplied.
- `C_num`: advances in cell count but narrows sector depth: the recurrent
  compiler now covers a six-cell adjacent-star union through complete `N<=2`.
  `N>=3`, number change, and arbitrary volume remain open.
- `C_wrap`: unchanged.  The slot cycle and two schedules are supplied
  compiler order; no schedule is time, duration, energy, rate, Record, or
  realized history.
- `C_int`: advances.  Two adjacent, noncommuting four-cell updates, their
  mass/contact/five-seam fixtures, both orders, inverses, and repeats are
  behind one recurrent compiler.
- `C_local`: advances materially.  A six-cell adjacent-star patch now has two
  exact bounded routes, literal nearest-neighbour schedules, held-size and
  all-frame controls.  An all-size translation-equivariant layer is not
  closed because the tested parity rule fails on odd periodic size.
- `C_source`: unchanged.

This compiler-only result does not by itself change the five framework
maturity scores.  There is no shared obstruction and **no axiom pressure**.

## No-go discipline N1–N8

Broad impossibility, minimum-content, and axiom-pressure gate status:
**FAIL / DO NOT SHIP**.

### N1 — alternative-route normalization

| normalized family | mechanism and terminal obligation | disposition |
|---|---|---|
| joint adjacent-star S6 role | one symmetric six-cell decoder; exact recurrence | **attempted: exact, large** |
| fixed-order transported slot | one shared decoder and returned local selector | **attempted: exact, retained** |
| parity-colored translated layer | eight disjoint star classes and covariant sweep | **attempted: even L6 pass, odd L5 fail** |
| larger translated role or motif | replace parity boundary rule by a finite covariant block | **open** |
| direct rough-carrier compiler | compile the same law on Cycle-532 rough code | **partial: local seam exists; preparation/transducer absent** |
| measurement/reset preparation | stabilize reference and renew clean work | **open** |

The families differ in encoded object, load-bearing auxiliary, and terminal
obligation.  Two positive routes and several open repairs prohibit a broad
negative.

### N2 — wall-independence audit

The residuals are

```text
W_ref      fixed-Wilson/reference genesis,
W_blank    branch/tag/slot blank genesis and renewal,
W_number   N>=3 sectors, number change, and scalable domain,
W_network  arbitrary adjacent-star/all-size translated recurrence,
W_bridge   selected-carrier <-> rough-carrier physical transduction.
```

The required pairwise audit is:

| pair | first closes second? | second closes first? | independent? |
|---|---:|---:|---:|
| `W_ref`, `W_blank` | no | no | yes |
| `W_ref`, `W_number` | no | no | yes |
| `W_ref`, `W_network` | no | no | yes |
| `W_ref`, `W_bridge` | no | no | yes |
| `W_blank`, `W_number` | no | no | yes |
| `W_blank`, `W_network` | no | no | yes |
| `W_blank`, `W_bridge` | no | no | yes |
| `W_number`, `W_network` | no | no | yes |
| `W_number`, `W_bridge` | no | no | yes |
| `W_network`, `W_bridge` | no | no | yes |

The independence is operational rather than rhetorical: a lawful encoded
reference can still lack renewable clean work; either can still be restricted
to `N<=2`; sector widening does not provide a translated layer; and a direct
selected-to-rough transducer is not produced by any of those closures.
Conversely, a transducer or network tiling does not prepare the reference,
renew blanks, or widen the sector.  Fixed six-cell recurrence and literal
routing are closed here and are not renamed as residual walls.

### N3 — hidden-wall scan

The scan covers “we assume,” “by construction,” “as is standard,” “the
framework provides,” “bridge context,” “background,” “naturally,”
“obviously,” “standard QFT,” “registered,” and “canonical.”  None discharges
a proof obligation.  Reference, blanks, q input, tables, angles, cutoff,
patch and color origins, factor and sweep order, finite sizes, frame, slot
program, boundary rule, router, and carrier are explicit supplies.

### N4 — residual matching

| witness | source line | Cycle-548 residual | match? |
|---|---:|---|---:|
| Cycle 545 fixed-volume recurrence | Cycle-545 note `:14` | two adjacent stars under one decode/update/re-encode terminal | yes; fixed adjacent patch closes |
| Cycle 539 selected decoder/order preparation | runner `:244`, `:218` | 667-column six-cell injective decoder and S6 preparation | yes; mechanism extends |
| Cycle 540 FSWAP identity | runner `:425` | every decoded seam/tag FSWAP, including accumulated phase | yes |
| Cycle 532 rough factor and `Gamma(P)` | rough runner `:911`, `:935` | common CAR target comparator | yes for target; no for carrier transduction |
| Cycle 548 colored layer | runner `:1044` | odd-L5 parity collision | yes only for Route C |

The current runner's decisive surfaces are the fixed decoder at `:164`, joint
S6 comparator at `:296`, logical two-star/slot algebra at `:436`, physical
schedule at `:689`, slot macro at `:910`, colored layer at `:1044`, and
covariance audit at `:1116`.  Evidence is not transferred across unlike
terminals: in particular, the L5 parity collision is dropped from evidence
against Routes A and B, and the Cycle-532 target factor is dropped from
evidence for a physical carrier bridge.

### N5 — rhetoric audit

| resolution | tested claim |
|---|---|
| one primitive | one-/two-M2 support; every pair nearest-neighbour |
| one seam block | exact Cycle-540 four-rotation FSWAP with tracked phase |
| one local cell core | coin/contact reconstruction and tag return |
| one star | complete six-cell `N<=2` embedding, mass/contact/three seams |
| two adjacent stars | both orders, returned slot, inverse, deletions, repeats |
| one fixed six-cell patch | exact A and B recurrence routes |
| even held L6 | Route C collision-free and frame-covariant |
| odd L5 | this parity coloring fails; no general negative |
| arbitrary network/infinite volume | untested; no closure or no-go claimed |

“Literal materialized base” applies to the 69,973-gate unconditioned decoded
schedule.  The 139,951-call two-half slot skeleton is literally ordered and
hashed, but its controlled three-M2 cores and the enormous W are exact bounded
macro decompositions and counts rather than materialized repeated primitive
rows.

### N6 — partial-closure path

Retain Route B and test a boundary-aware covariant coloring or larger
translated motif on both odd and even periodic sizes.  Then compose several
adjacent-star slot returns and prove that one persistent slot and q/reference
allocation suffice without patch-global decoder duplication.  Independently,
measurement/reset or dissipative stabilization can attack reference and blank
genesis, and a direct rough-code isometry can attack the carrier bridge.

### N7 — hostile steelman

> A hostile reviewer should reject “volume compiler” if it is read as an
> arbitrary-network theorem.  Routes A and B still use a supplied fixed
> six-cell truth table, patch chart, factor order, reference, blank work, and
> programmed two-step schedule.  The controlled-slot expansion is a local
> macro proof, not one fully materialized billion-row circuit.  But this does
> not support a no-go: Route A and Route B both close the stated bounded
> adjacent-star terminal, even L6 closes the parity-color construction, and a
> boundary-aware color or larger local role remains constructive.

### N8 — cross-cycle echo

Cycles 319 and 324 replaced inconsistent independent edge roles with joint
roles or slots.  Cycle 533 replaced invariant pair separators with a joint
decoder.  Cycle 539 compiled one star.  Cycle 545 decoded one shared patch
only once to recur across overlapping updates.  Cycle 548 again finds two
positive relational auxiliaries—joint S6 and a returned slot—while one naive
parity layer fails only at its odd boundary.  The repeated evidence is for
constructive auxiliary redesign, not a route-independent substrate wall.

No cross-cycle evidence supports an impossibility, minimum-content theorem,
constitutional change, or axiom pressure.

## Disposition and next campaign

Retain Route B as the strongest adjacent-star compiler candidate and Route A
as its exact symmetric comparator.  Route C should be retained as an honest
odd/even discriminator, not generalized into a negative.

The highest-value next campaign is a multi-star translated recurrence test:
repair Route C with a boundary-aware finite coloring or larger motif, then
compare that construction against composing Route B's exact returned-slot
macro across a periodic network.  Require one persistent q/reference
allocation, local return at layer boundaries, both odd and even held sizes,
all 24/576 covariance, and no runtime frame or host parity service.  Reference
and blank genesis and the selected-to-rough transducer remain independent
campaigns.

## Cold certificate

The pre-freeze complete run passed all 12 aggregate predicates in
`183.05363262502942` seconds with maximum RSS 177,127,424 bytes and process
swap count zero.  The final cold certificate is regenerated after this note
is frozen; only that post-freeze output is packaging evidence.
