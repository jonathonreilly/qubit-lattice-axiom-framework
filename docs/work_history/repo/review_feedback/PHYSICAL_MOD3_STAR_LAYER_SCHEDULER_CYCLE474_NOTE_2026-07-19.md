# Physical mod-3 whole-layer star scheduler — Cycle 474 note (2026-07-19)

**Authority: none. Audit: unset.**

## Frozen question and bounded answer

Can the complete Cycle 470 seven-supercell local block be scheduled over every
target of every Cycle 463 train/held layer without simultaneous physical-M2,
path, face-port, or arithmetic-port conflicts, while retaining exact layer
dependencies and proper-cubic covariance?

Cycle 474 supplies a bounded positive answer.  It partitions targets by the
27 residue triples

```text
color(x,y,z) = (x mod 3, y mod 3, z mod 3).
```

Each layer has a fixed **27-color** sequence.  All targets of one color execute
their complete Cycle 470 blocks in elementary-event lockstep.  The runner tests
rather than assumes that they have **site-disjoint seven-supercell stars**.
It checks every target exactly once, all shell reads, every retained read/write
dependency, full forward/inverse histories, exact event/depth/capacity counts,
congestion bounds, deletions, malformed colors, and all 24 proper-cubic frames.

This closes Cycle 470's remaining overlapping-star scheduling residual for the
finite retained-history R1/R2 fixtures.  It does not show that 27 colors are
minimal or efficient.  It does not remove retained history, select the local
law, or identify the source or clocks physically.  Iteration count, color
round, and parallel depth are not time.  Source bits and schedule counts are
**not energy, stress, lapse, metric, proper time, backreaction, or gravity**.
No axiom, foundation, Qualification, primitive, registry, policy, queue, or
audit-status file is edited.

## Color schedule and conflict theorem

For update layer `k`, a round has the immutable declaration

```text
(layer=k, read_layer=k, write_layer=k+1, color=c,
 targets={x in active cube : x mod 3 = c}).
```

The round validator refuses any changed dependency, duplicate target, wrong
color, undeclared target, or pair of overlapping stars.  A local star is the
target supercell plus its six signed-axis neighbors.  Distinct same-color
targets differ by a nonzero multiple of three in at least one coordinate;
the executable enumerates every finite pair and confirms their stars do not
intersect.  Cycle 470 already proves each physical path stays inside that star.
Therefore same-round blocks have no common M2, route edge, face port, compact
port, work bit, source register, or target register.

The reference color list is the fixed Cartesian enumeration of `{0,1,2}^3`.
It is supplied scheduling structure.  It is independent of runtime field
values and contains no host-selected branch.

### Exact finite schedule results

Each domain has 96 layers times 27 colors, hence **all 2,592 rounds**:

| quantity | train R=1 | held R=2 |
|---|---:|---:|
| active targets per layer | 27 | 125 |
| maximum simultaneous blocks | 1 | 8 |
| simultaneous star conflicts | 0 | 0 |
| simultaneous M2/path/port conflicts | 0 | 0 |
| shell neighbor reads over 96 layers | 5,184 | 14,400 |
| maximum simultaneous support | 448,000 M2 | 3,584,000 M2 |
| physical domain capacity | 8,000,000 M2 | 21,952,000 M2 |
| elementary events manifested | 36,132,875,280 | 167,281,830,000 |
| strict event-lockstep parallel depth | 36,132,875,280 | 36,132,875,280 |
| schedule SHA-256 | `c737aaefd151680a4bdf34f9e5a9d742431c41da63bc4f56ccfb085d0761852e` | `8f7a79454a4c5d54e27730765dd8c53ef6dae6b41883ee5be5dd4fca5bf05082` |

The held cube gains event-level parallelism because some colors contain eight
targets separated by three along each axis.  The train cube has exactly one
target of each residue triple, so this witness gives no within-round speedup
there.  The equal strict depths are a consequence of keeping all 27 nonempty
color rounds in both domains.

## Retained-layer dependencies and inverse

Every block at layer `k` reads only the complete retained history word at layer
`k` and XOR-writes its unique blank target at `k+1`.  All blocks in a round
compute their values from the unchanged read layer before any target write.
Because different colors still write distinct target words and read the same
retained predecessor layer, the 27 rounds reproduce Cycle 463's local rule
without an intra-layer causal dependency.

The executable runs the full 96-layer integer history in color order for both
domains and compares every retained word with Cycle 463's original schedule.
Mismatch count is zero.  It then reverses layers 95 through 0, reverses the
color and target action order, validates each output against its retained
predecessor, and clears it.  Both train and held histories return exactly to
the central-source/blank-history input.

A mutated `read_layer=k+1`, malformed write layer, or wrong inverse dependency
is refused.  This checks dependency direction rather than inferring it from the
final field.

## Complete Cycle 470 block manifests

For each layer the runner regenerates Cycle 470's 1,744 ingress actions and
their path digest.  A block manifest is the ordered concatenation

```text
ingress(layer) |
Cycle467 routed arithmetic |
inverse ingress(layer).
```

Cycle 467's arithmetic contributes 12,719,213 elementary events.  Cycle 470
ingress varies with retained-word placement, so a complete local block ranges
from 13,769,161 to 14,154,049 events.  The exact sum for one target across all
96 layers is 1,338,254,640 events.  Thus:

- train forward event count is `27 * 1,338,254,640 = 36,132,875,280`;
- held forward event count is `125 * 1,338,254,640 = 167,281,830,000`;
- strict event-lockstep depth is
  `27 * 1,338,254,640 = 36,132,875,280` for either domain;
- forward-plus-inverse strict depth is 72,265,750,560.

The event manifest is not repeated primitive execution.  It hashes each exact
layer block once and instantiates it by target translation in every round.  The
runner does execute the full forward/inverse integer histories, enumerates all
star supports and dependencies, regenerates every Cycle 470 transfer path, and
literally recompiles all 12,719,213 Cycle 467 routed arithmetic events once to
recover the frozen digest and edge congestion.  Executing 167 billion gates is
neither hidden nor falsely claimed.

## Capacity, depth, and congestion bounds

Cycle 470's per-active-supercell occupancy remains 46,371 of 64,000 M2.  A
local block uses at most seven full supercells, 448,000 M2.  Since same-round
stars are disjoint, the held maximum of eight blocks occupies at most 56
supercells or 3,584,000 M2 simultaneously, within its radius-3 physical
envelope.  No new M2 storage or transport ancilla is introduced by coloring.

The frozen arithmetic route is regenerated exactly:

| quantity | value |
|---|---:|
| arithmetic events | 12,719,213 |
| arithmetic route SHA-256 | `4d6f058d95cc32538f3a15b6fd0eb620f7708371e6276298d063ba44078d1457` |
| arithmetic maximum edge incidence | 9,749 |
| transfer round-trip maximum edge incidence across layers | 576–1,500 |
| composed local-block maximum edge incidence across layers | 9,749–10,241 |
| literal Cycle 470 layer-48 composed incidence | 9,749 |

Same-round translated edge sets are disjoint, so peak simultaneous primitive
edge conflict is zero.  A physical supercell can occur in at most its own star
and the six adjacent target stars, giving the conservative exact-construction
upper bounds:

- per complete layer, no physical edge exceeds `7 * 10,241 = 71,687`
  primitive incidences;
- across the full forward history, no physical edge exceeds 6,579,468
  primitive incidences.

These are strict serial-within-block/parallel-between-block bounds.  They are
not optimized circuit depths, hardware times, or lower bounds.

## Held boundary and deletion/domain controls

The held cube's 125 targets and radius-3 blank shell are tested without refit.
Each of its 14,400 shell reads belongs to exactly one target update and every
same-round shell-containing star remains disjoint.  A nonblank shell is
refused by the physical code validator.

Additional controls establish:

- deleting the held center target at layer 48 leaves that retained target blank
  and changes later history;
- deleting color `(0,0,0)` from layer zero omits a held target;
- duplicating a target or assigning a target to the wrong color is refused;
- changing `read_layer=k` or inverse dependency order is refused;
- mod-2 coloring has 225 explicit overlapping-star pairs in R2, including
  centers separated by two with their middle supercell shared.

The mod-2 failure is only a control against accidental overlap.  It does not
show that 27 colors are minimal; other colorings and schedules remain live.

## Proper-cubic carried covariance

A proper-cubic signed permutation `F` maps a residue color by

```text
c -> F c mod 3.
```

It maps the complete target set of color `c` onto the complete target set of
color `F c`, and maps every seven-supercell star onto the corresponding carried
star.  The read/write layer labels and target-relative Cycle 470 block manifest
are unchanged.

The runner checks all 24 proper-cubic frames, both radii, every layer, color,
target, and star.  The carried schedule is the image of the reference ordered
sequence.  There is **no global re-sort** into lexicographic order after a
frame transformation.  This prevents a hidden preferred-axis scheduler while
retaining a deterministic carried program.  All carried failures are zero and
the 24 frame schedule manifests are distinct.

The reference color order is still supplied.  Establishing covariance of its
24-frame orbit is not an autonomous frame-selection or causal-clock law.

## Prior-art and novelty boundary

Residue coloring, conflict-graph scheduling, and lockstep execution of disjoint
local circuits are standard parallel-computation techniques.  Cycle 474 does
not claim these ideas, 27-color minimality, or a new graph-coloring theorem.

The repository advance is the exact composition with the frozen physical
objects: all finite R1/R2 stars, all 96 retained dependencies, Cycle 470's
layer-dependent transfer manifests, Cycle 467's literal arithmetic transcript,
exact capacity/event/depth/congestion ledgers, full history inverse, shell and
deletion controls, and the no-resort all-24 carried schedule.

## Supplied/constructed/open inventory

Supplied:

1. Cycle 463's R1/R2 domains, blank shells, retained histories, local law,
   source, precision, and layer count;
2. Cycle 467's arithmetic trace and Cycle 470's serial seven-cell block;
3. the 27 reference residue colors, their reference enumeration, layer barriers,
   and strict serial-within-block event-lockstep policy;
4. scale-40 capacity and the Cycle 470 placement;
5. authority none, audit unset, and explicit resource caps.

Constructed: exact color partition and conflict checks; complete finite
round manifests; retained forward/inverse histories; translated physical
support/capacity accounting; strict depth and edge-congestion upper bounds;
held shell/deletion/domain controls; and proper-cubic no-resort covariance.

Open: fewer-color or lower-depth schedules; asynchronous or pipelined local
barriers; globally optimized edge routing; removal/compression of retained
history; derivation of the relaxation/source/clock laws; infinite-volume and
continuum limits; matter/energy-stress, occurrence, Records, Born probability,
lapse, metric, curvature, backreaction, or gravity.

## TOE dependency ledger

| wall | Cycle 474 disposition |
|---|---|
| `C_ref` | unchanged; a color schedule selects no vacuum, sea, phase origin, or preparation |
| `C_num` | unchanged; residue labels do not select a physical number reference or superselection law |
| `C_wrap` | unchanged; iteration, color round, and parallel depth remain compiler ordinals, not retained winding or time |
| `C_int` | unchanged; scheduling does not select, protect, or assign a rate to the supplied update law |
| `C_local` | constructively narrowed: Cycle 470's overlapping-star residual closes for every finite R1/R2 retained layer with exact conflict-free physical manifests and inverse; efficiency and history removal remain open |
| `C_source` | unchanged in meaning; source-conditioned blocks are scheduled, but no energy/stress conservation or backreaction is derived |

No pair collapses: a scheduler does not select the law/source, and a source law
would not itself supply a conflict-free physical schedule.

## Full no-go discipline

### N1 — Alternative route enumeration

| normalized route family | object / mechanism / terminal obligation | status |
|---|---|---|
| mod-3 residue rounds | seven-cell stars / 27 carried color classes / full finite layer without conflicts | **ATTEMPTED — SUCCEEDS** |
| denser conflict-graph coloring | finite stars / computed graph coloring / fewer rounds | **OPEN — NOT ATTEMPTED** |
| edge-colored pipeline | route edges / staggered block microsteps / lower depth without collisions | **OPEN — NOT ATTEMPTED** |
| moving-head schedule | target packets / reversible scanning head / bounded global layer | **OPEN — NOT ATTEMPTED** |
| cached-face schedule | redundant constrained ports / parallel local reads / low-depth layer | **OPEN — NOT ATTEMPTED** |
| asynchronous local barrier | retained readiness flags / causal dependency firing / frame-free autonomous schedule | **OPEN — NOT ATTEMPTED** |

The successful schedule defeats any impossibility claim.  Open alternatives
forbid minimum-color, minimum-depth, or unique-content promotion.

### N2 — Wall-independence audit

Collapse the residuals into `Wq` coloring/round count, `Wr` local routing,
`Wh` retained-history/barriers, `Wl` finite-law selection, `Ws` source meaning,
`Wc` causal-clock interpretation, and `Wg` continuum geometry/backreaction.
Coloring closes none of routing efficiency, history removal, law selection,
source conservation, clock interpretation, or gravity.  Conversely none of
those supplies this finite conflict schedule.  They remain independent.

### N3 — Hidden-wall scan

The inventory exposes 27 reference colors, reference enumeration, layer
barriers, retained blank targets, strict local event order, computational-basis
word semantics, finite boundaries, target translation, and frame-carried rather
than frame-selected scheduling.  The event totals are manifests; repeated
primitive execution is explicitly not claimed.

### N4 — Residual matching

Cycle 470 named overlapping whole-layer star scheduling as its precise
remaining compiler residual.  The 27-color construction matches that object,
mechanism, and terminal obligation for R1/R2.  It does not match history
removal, source/time, continuum, or gravity residuals and is not cited against
them.

### N5 — Rhetoric audit

Evidence covers target, color, round, star, face/shell support, retained layer,
full history, inverse, route manifest, domain, and carried frame.  The result is
finite and construction-specific.  “Parallel depth” means an event schedule,
not duration.  No optimal, minimal, universal, infinite, continuum, source,
energy, or gravity language is promoted.

### N6 — Partial-closure path scan

Cycle 470 made the global overlap wall explicit.  Cycle 474 supplies a complete
finite schedule without editing axioms.  Efficiency can be narrowed next by
denser coloring or an edge-colored pipeline; retained barriers can be attacked
separately.  Partial success creates no axiom pressure.

### N7 — Steelman

A hostile reviewer should object that the schedule is extraordinarily deep,
uses supplied reference colors and hard layer barriers, gives no train-domain
parallel gain, and manifests rather than executes 167 billion held primitives.
A conflict-graph coloring, microstep pipeline, local readiness mechanism, or
face-cache layout could do materially better.  These are concrete next routes.

### N8 — Cross-cycle echo and claim gate

Cycle 470's overlap residual closes only for finite retained R1/R2 scheduling.
Cycle 463's law/history/source/time/gravity boundaries remain.  Mod-2 failure is
not reused as a minimum theorem, and no CAR-compiler or continuum no-go is
inferred from this separate scheduler.  `C_wrap`, `C_source`, continuum, and
backreaction echoes remain unresolved.

**No-go claim: FAIL. Minimum-content claim: FAIL. Axiom-pressure claim: FAIL.**
There is **no axiom pressure**.

## Frozen executable disposition

Retention requires zero failed tests; exact Cycle 467/470 hashes and route
identities; exact schedule/event/depth ledgers; and resource use below 180
seconds and 1,536 MiB.  The Cycle 474 runner/note keep authority none and audit
unset and do not authorize an audit verdict, merge, or protected-surface edit.

The final cold run reports `RESULT pass=11 fail=0`, takes 93.242 seconds, and
peaks at 125.91 MiB.  Runner SHA-256:
`10a55ef2cb36f7d9f60b115911fc2bcffbffbe3ac0977db0ba319f6dcfd08755`.
