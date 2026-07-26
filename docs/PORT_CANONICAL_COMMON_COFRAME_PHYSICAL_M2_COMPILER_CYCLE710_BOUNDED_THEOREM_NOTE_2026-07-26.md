# Cycle 710 port-canonical common-coframe physical-M2 compiler

**Date:** 2026-07-26

**Type:** bounded_theorem

**Authority:** none

**Audit:** unset

**Framework substrate:**
[`MINIMAL_AXIOMS_2026-06-29.md`](MINIMAL_AXIOMS_2026-06-29.md)

**Physical compiler input:**
[`LOCAL_SEAM_SIGNED_CLIFFORD_PHYSICAL_M2_COMPILER_CYCLE709_BOUNDED_THEOREM_NOTE_2026-07-26.md`](LOCAL_SEAM_SIGNED_CLIFFORD_PHYSICAL_M2_COMPILER_CYCLE709_BOUNDED_THEOREM_NOTE_2026-07-26.md)

**Primary runner:**
[`scripts/frontier_cycle710_port_canonical_common_coframe_physical_m2_2026_07_26.py`](../scripts/frontier_cycle710_port_canonical_common_coframe_physical_m2_2026_07_26.py)

## Result

Cycle 710 removes Cycle 709's supplied target-cell ordering on the tested open
rectangular signed-code family.  The landed BKSF incident prefixes and oriented
`A` operators are reconstructed exactly from radius-one physical port data:

```text
octahedral incident key  = (0, fixed rank of the two endpoint modes)
spoke incident key       = (1, matter-mode label)
cross-cell incident key  = (2, signed port in -x,-y,-z,+x,+y,+z)
```

Inside one cell, the canonical edge orientation is lower mode to higher mode.
Across a cell face it is the directed positive-axis endpoint to its neighbour.
No vertex number, edge number, cell-tuple rank, target sort position, global
Jordan-Wigner path, or branch-ray state enters these rules.

On five boxes and four independently shuffled target enumerations per box,
the local-port presentation needs zero `Z` or `CZ` order-transition factors.
Every declared semantic row is exact.  The declared stabilizers span the full
actual stabilizer group, and their union with the declared logical rows spans
the full signed-code centralizer.  Thus the result is not based only on a small
self-selected row family.

With one supplied common proper-cubic coframe, the transported compiler closes
all 24 frames and all 576 ordered frame products.  The global `3 x 2 x 2`
transition restricts exactly to each of its two overlapping `2 x 2 x 2` cubes
in all 96 frame/subcube/graph checks.  The local diagonal factors are encoded
on the landed repetition M2 registers and routed with exact code-space
intertwiners and leakage controls.  This is a finite compiler identity, not a
time law.

The theorem is conditional on a common coframe.  An explicit adversarial
fixture keeps that boundary live: two independent coframes on the same cube
differ by 108 open-graph and 88 patch-graph local terms; on the four-cell
shared slab of two overlapping cubes they disagree by 46 and 42 terms.  Cycle
710 does not silently identify those charts, generate coframe tags, or enforce
their transitions.

## Exact code-space relation

Let `C_a` be the fixed Cycle 709 signed compiler in the reference chart.  Let
`N_a,N_b` be the natural OpenReference/PatchGraph equivalences and let

```text
Q(a -> b) = D(a -> b) P(a -> b),
D = product Z_orientation product CZ_incident-inversions.
```

`P` is the bare physical edge-address relabeling.  Each `Z` is edge-local and
each `CZ` joins two edges incident on one graph vertex.  On the declared
overlapping-star signed code space, the transported compiler is

```text
C_b = Q_patch(a -> b) C_a N_a Q_open(a -> b)^-1 N_b^-1.
```

Writing `E_lit` for the landed repetition/rail placement and `R_b` for the
routed physical word gives

```text
E_lit C_b = R_b E_lit
```

on that code space.  For the identity coframe the local-port presentation
reproduces the landed representation exactly, so the extra diagonal gauge has
zero factors and `R_b` reduces to the Cycle 709 physical word.  For a
nonidentity common coframe, the additional factors remain bounded vertex/edge-
local commuting Clifford gates; the primary runner reports their complete
24-frame physical routing census and active deletions.

## Enumeration independence and code completeness

The twenty no-refit shuffled fixtures give:

| box | actual stabilizer rank `n-k` | full centralizer dimension `n+k` |
| --- | ---: | ---: |
| `2 x 2 x 2` | 120 | 216 |
| `3 x 2 x 2` | 184 | 328 |
| `4 x 2 x 2` | 248 | 440 |
| `3 x 3 x 2` | 282 | 498 |
| `3 x 3 x 3` | 432 | 756 |

The declared stabilizer rank equals `n-k`, its union with the actual
stabilizers has the same rank, and the declared semantic rank equals `n+k` on
every fixture.  All declared stabilizers decode with positive sign.  Every
ambient completion mismatch decodes as a signed stabilizer; none is outside
the code centralizer or non-Hermitian.  Ambient completion is therefore kept
separate from the signed code theorem rather than used to inflate or defeat
the result.

Across the twenty target shuffles:

- semantic, local-`A`, and local-support failures are zero;
- open and patch order-transition factor counts are zero;
- no fit or held-size parameter is introduced; and
- two independently enumerated overlapping cubes agree on all 80 shared
  augmented addresses, including 76 patch edges and four rails.

## Proper-cubic and overlap controls

All 24 proper-cubic frames and 576 ordered products have zero semantic,
inverse, open-product, patch-product, and locality failures.  The largest
abstract diagonal gauges on the `2 x 2 x 2` frame campaign contain:

| graph | maximum `CZ` | maximum `Z` |
| --- | ---: | ---: |
| OpenReference | 432 | 120 |
| PatchGraph | 408 | 108 |

Every `CZ` pair shares one graph vertex and has bounded cell diameter.  The
fixed rule factors without collisions through the finite proper-cubic coframe
and local half-edge features: 576 open and 504 patch `Z` feature classes, and
3,744 open and 2,520 patch pair-feature classes, have zero outcome collisions.

The common-coframe restriction test uses the complete `3 x 2 x 2` box, both
overlapping maximal cubes, both graph types, and all 24 frames.  All 96 term-
set restrictions agree exactly.  This is the overlapping-star consistency
theorem claimed here.

## Literal physical execution

For every common coframe on the primary `3 x 2 x 2` box, the runner executes

```text
physical pre-D ; address-relabelled landed Cycle709 word ; physical post-D.
```

The natural-map and bare `P` factors are compile-time physical wire/address
relabelings, derived independently on the input and output sides.  They have
zero permutation mismatches in all 24 frames.  Only the local `S/H/CNOT`
factors and all 1,265 relabelled Cycle 709 primitives are emitted as gates.

The complete physical census is:

| resource/control | exact result |
| --- | ---: |
| abstract PatchGraph-plus-rail qubits | 256 |
| primary assigned data/code/rail M2 sites | 276 |
| maximum total routed footprint M2 sites | 2,869 |
| maximum supplied blank route-work M2 sites | 2,593 |
| maximum traversed non-endpoint primary data M2 sites | 4 |
| encoded signed-Pauli rows | 12,288 |
| exact/code intertwiner failures | 0 |
| repetition stabilizer rows / leakage failures | 480 / 0 |
| semantic / encoded-number failures | 0 / 0 |
| primitive gates over the 24 frames | 1,265--5,777 |
| routed nearest-neighbour gates | 22,635--38,811 |
| maximum route distance | 24 |
| NN / operand-order / route-return failures | 0 / 0 / 0 |
| minimum first-route-SWAP deletion witnesses per frame | 723 |

The 276 assigned sites are the data/code/rail footprint, not the full routing
footprint.  The supplied serial router may additionally touch up to 2,593
blank route-work M2 sites in a frame, for 2,869 touched M2 sites total.

The identity coframe contains no extra gauge factors and reproduces the landed
Cycle 709 routed-word digest
`673932d45609b52da0c07495e93dd6d13fa5ef0afe323c8113448e63f5744f6d`.
The most demanding pre-gauge has 184 `Z` and 660 `CZ` factors; the most
demanding post-gauge has 164 and 612.  Logical `CZ` degree is at most six, and
greedy abstract `CZ` depth is at most eight on each side.  This is not a claim
that the present serial physical router has constant depth.

Deleting any active gauge `CZ` causes at least two local-`A` failures and any
active gauge `Z` causes at least one.  Deleting one `S` from the physical `Z`
intertwiner has residual `sqrt(2)`; deleting any one primitive from the
physical `H-CNOT-H` realization of `CZ` has residual at least
`1.9999999999999998`.  Every frame retains at least 723 active first-route-
SWAP deletion witnesses.

The unchanged upstream runner gives a one-particle coin eigen residual of
`2.594441202963249e-16`, mass residual `5.551115123125783e-17`, and zero
vacuum/one-particle and double-occupation contact residuals at the supplied
Cycle 230 coupling `0.37`.

The independent-coframe falsifier uses `diag(-1,-1,+1)` against the identity.
Both charts separately have zero semantic failures, but their physical
presentations are not equal:

| comparison | OpenReference difference | PatchGraph difference |
| --- | ---: | ---: |
| same physical cube | 108 terms | 88 terms |
| shared four-cell slab | 46 terms | 42 terms |

This distinguishes an unfinished chart-transition controller from a global-
ordering obstruction.  It is not a route-independent no-go or axiom-pressure
claim.

## Supplied, derived, and open structure

Supplied:

- one finite Cycle 709 reference word template;
- one common proper-cubic coframe on the declared overlapping-star domain;
- local edge kind, endpoint mode, signed physical port, and graph incidence;
- the Cycle 706 signed `A/B` convention and OpenReference source sector;
- prepared Cycle 707 repetition/PatchGraph/rail registers, deterministic
  numeric tolerances, blank route work, and the landed serial Manhattan
  micro-schedule.

Derived and executed:

- the landed presentation's incident prefixes and `A` orientations from
  radius-one port data;
- enumeration-independent address relabeling and local `Z/CZ` presentation
  gauges;
- the exact inverse, 24 frames, 576 products, and 96 common-coframe overlap
  restrictions;
- full signed-code centralizer coverage on all twenty shuffle fixtures;
- physical repetition-code `Z/CZ` intertwiners, leakage/number controls,
  nearest-neighbour route-and-return words, and active deletions; and
- unchanged replay of the landed Cycle 219 one-particle mass, Cycle 230
  contact, Cycle 708 endpoint, and Cycle 709 seam/compiler regression
  surfaces.

Open and not claimed:

- autonomous production and local enforcement of coframe tags and their
  overlap transition rule;
- collision-free autonomous recurrence of the nonidentity coframe gauge and
  controller-token/route-work genesis;
- local genesis and enforcement of OpenReference, PatchGraph, repetition,
  rail, source, and Wilson sectors;
- periodic, holed, irregular, or all-volume closure;
- a physical predecessor/interval bank, occurrence/admission law, permanent
  Record production, Born/history actualization, source/gravity response, or
  an empirical prediction; and
- any route-independent no-go, minimum theorem, shared obstruction, or axiom
  pressure.

No circuit step, colour layer, or schedule counter is called physical time.
No static constraint is called physical energy.  No generator element is
called a rate, and no pointer copy is called a Record.

## No-Go Discipline Gate

**Gate result: FAIL for a broad negative.  Disposition: retain the positive
bounded theorem and the exact conditional falsifier; make no impossibility,
minimum-content, shared-obstruction, or axiom-pressure claim.**

### N1 — normalized constructive routes

| route family | mechanism and terminal obligation | status |
| --- | --- | --- |
| local port presentation | reconstruct incident prefixes and orientations from bounded edge features | ATTEMPTED; succeeds in Cycle 710 |
| local diagonal chart gauge | compile presentation changes as vertex-local `CZ` and edge-local `Z` | ATTEMPTED; succeeds conditionally on a coframe |
| overlap transition cocycle | enforce chart changes on intersections and triple overlaps | UNFINISHED in this theorem |
| dynamical coframe-tag sector | prepare and locally enforce frame tags without a global choice | UNFINISHED |
| staggered local transport | time-multiplex feature/coframe transport with a fixed covariant schedule | UNFINISHED |
| direct order-free PatchGraph law | rebuild the physical update directly in local ports without a reference word | UNFINISHED |

Because four normalized routes remain unexhausted and the first two are
constructive, N1 rejects any broad negative.

### N2 — wall-independence audit

The raw independent-chart mismatch and a chart-transition controller are the
same residual and are collapsed to one item.  Coframe-tag genesis/enforcement,
source/code-sector genesis/enforcement, and autonomous recurrent scheduling
do not imply one another.  Periodic-sector closure is outside the tested open-
box domain and is not counted as evidence against it.

### N3 — hidden-wall scan

The load-bearing words `supplied`, `reference`, `common coframe`, `prepared`,
and `canonical` were scanned.  Every occurrence is classified in the explicit
inventory above.  No framework primitive is silently used to provide a
coframe, source sector, code genesis, controller, time metric, or history law.

### N4 — residual matching

Cycle 709's exact residual is target-order-dependent signed coarse-face phase.
Cycle 710 retires that residual.  The retained 108/88 and 46/42 residual is
instead independent-coframe physical presentation equality.  The two are not
conflated, and neither is cited as evidence against source genesis, recurrence,
time, Record, Born/history, or gravity.

### N5 — rhetoric audit

Tested resolutions are local edge, incident pair, full cube, two overlapping
cubes, five open boxes, 24 frames, and 576 products.  Periodic, irregular,
holed, independently coframed, and lattice-wide recurrent versions are not
claimed.  Accordingly the result says target enumeration is removed on the
tested family, not that every fermionization choice is derived lattice-wide.

### N6 — partial-closure scan

A bounded overlap `Z/CZ` transition, a finite coframe gauge field, sparse local
tag constraints, and staggered transport are live import-retirement paths.
None requires declaring a new axiom.  The primitive registry supplies no
coframe-tag generation or physical controller and is not invoked as though it
did.

### N7 — steelman against a no-go

A hostile reviewer can directly take the XOR of the two local diagonal chart
gauges on an overlap, interpret it as a bounded transition function, and test
the cocycle on triple intersections.  That concrete route could remove the
46/42 mismatch without a preferred global frame.  Therefore an obstruction
claim would be premature.

### N8 — cross-cycle echo

Cycles 706--709 repeatedly turned apparently nonlocal signed-order residuals
into explicit finite local gauges, endpoint variables, or routed Clifford
words.  Cycle 710 follows that constructive pattern.  Those prior retirements
are evidence to attempt the overlap-cocycle and local-tag routes, not evidence
for a constitutional obstruction.

## Claim boundary

Cycle 710 is a bounded, executable, common-coframe physical-M2 compiler and an
enumeration-independence theorem on the stated open-box signed code space.  It
is unaudited.  It is not a translation-invariant autonomous recurrent law, a
coframe-genesis theorem, a periodic fermionization theorem, a time law, a
source/gravity law, a Record/Born law, an empirical prediction, or axiom
pressure.
