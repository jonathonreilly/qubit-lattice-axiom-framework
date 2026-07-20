# Physical seven-supercell port-delivery compiler — Cycle 470 note (2026-07-19)

**Authority: none. Audit: unset.**

## Frozen question and answer

Can all six retained 249-bit Cycle 463 neighbor words be delivered from their
physical storage supercells into Cycle 467's declared arithmetic ports, used,
and returned with a fixed local schedule, exact inverse, bounded congestion,
and proper-cubic covariance?

Cycle 470 supplies a bounded positive **seven-supercell** answer.  A local
block consists of one target supercell and its six signed-axis neighbors.  For
each retained bit, a fixed nearest-neighbor path moves the source state next to
its assigned arithmetic port by SWAPs through occupied paths, applies CNOT,
and reverses every SWAP.  Thus the intermediate M2 sites may contain arbitrary
states: the construction uses **zero blank corridor ancillas**.  After Cycle
467 arithmetic, the inverse delivery schedule clears all neighbor and source
ports and returns every source/intermediate bit to its original placement.

For a complete local E/G map, the retained target word is endpoint-SWAPped into
the compact target register before arithmetic and SWAPped back afterward.  The
central persistent source bit is staged by the same remote-CNOT construction.
One actual held-domain block is executed through ingress, all 12,719,213 routed
Cycle 467 arithmetic primitives, inverse egress, and retained-target storage.

This closes Cycle 467's stated port-delivery residual for a single serial local
block.  It does not yet schedule overlapping stars across a whole layer in
parallel, and it does not derive the relaxation law, source, clocks, or gravity.
Iteration count and schedule depth are not time.  Retained words and source
bits are **not energy, stress, lapse, metric, proper time, backreaction, or
gravity**.  No axiom, foundation, Qualification, primitive, registry, policy,
queue, or audit-status file is changed.

## Persistent and compact placement

Every active scale-40 supercell uses a fixed Hamiltonian-coordinate placement.
The first 2,507 sites are exactly Cycle 467's compact interface:

| compact component | M2 |
|---|---:|
| six neighbor ports | 1,494 |
| source port | 1 |
| retained-target staging port | 249 |
| Cycle 467 declared work | 763 |
| **compact total** | **2,507** |

The 97 retained 249-bit history words follow, then a persistent source bit and
the complete Cycle 463 clock/sidecar allocation:

| active-supercell component | M2 |
|---|---:|
| compact arithmetic/interface region | 2,507 |
| persistent retained histories | 24,153 |
| persistent source | 1 |
| clocks and sidecars | 19,710 |
| **occupied total** | **46,371** |
| scale-40 capacity | 64,000 |
| remaining routing reserve | 17,629 |

The seven-active-supercell upper bound is 324,597 occupied M2 inside a
448,000-M2 envelope.  Shell cells need less, but the executable does not rely
on that reduction.  The overhead is constant per coarse cell and independent
of train/held domain size.

## Occupied-path remote primitives

Let `p0,...,pL` be a simple nearest-neighbor path, with the retained source at
`p0` and a declared port at `pL`.  Remote CNOT is compiled as

```text
SWAP(p0,p1), ..., SWAP(p[L-2],p[L-1]),
CNOT(p[L-1],pL),
SWAP(p[L-2],p[L-1]), ..., SWAP(p0,p1).
```

It has `2(L-1)` SWAPs and `6(L-1)+1` CNOT primitives after expanding each
SWAP into three nearest-neighbor CNOTs.  The endpoint CNOT toggles the blank
port by the retained source, while all intermediate values and physical
placements are restored exactly.

Target staging uses the endpoint-SWAP network

```text
SWAP(p0,p1), ..., SWAP(p[L-1],pL),
SWAP(p[L-2],p[L-1]), ..., SWAP(p0,p1),
```

which exchanges only the endpoints and restores every intermediate.  It uses
`2L-1` SWAPs or `3(2L-1)` adjacent CNOTs.  Both transcripts are palindromes of
self-inverse primitives.  The egress program is the ingress actions in reverse
order, so it is the literal circuit inverse.

The transport layer uses SWAP and CNOT; its Fredkin count is zero.  Cycle 467's
arithmetic segment retains its explicit NOT/CNOT/Toffoli primitives.  No
uncompiled long-range gate appears.

The runner exhausts both remote operations for path distances one through five
and every state of both endpoints and all intermediates.  This directly tests
arbitrary occupied paths, endpoint action, intermediate restoration, and
inverse closure.  Deleting one final elementary primitive supplies a witness
at every tested distance.

## Face-port geometry and fixed schedule

Physical coordinates are `40*c+p`, where `c` is a coarse-cell coordinate and
`p in [0,39]^3`.  Persistent words and compact ports use explicit Hamiltonian
indices.  A neighbor path first advances along its signed normal axis, crossing
exactly one nearest-neighbor face edge into the target supercell, and then
advances along the two carried transverse axes to the assigned Cycle 467 port.
Each action therefore has an actual source-face/target-face port pair; face
edges may be reused because the witness schedule is serial.

For every layer, ingress has exactly 1,744 fixed actions:

- 249 endpoint SWAPs from blank retained-target storage into target ports;
- one remote CNOT from persistent source to the source port;
- 1,494 remote CNOTs from the six retained neighbor words.

The action list is fixed before input state and has no host-selected runtime
branch.  Bit ordering is the supplied binary-register ordering.  Direction
ordering is only an enumeration of commuting endpoint operations; the entire
ordered list is carried under frames and is never re-sorted using global axes.
The strict serial schedule gives simultaneous route congestion one.  This is
a constructive upper-bound schedule, not an optimized depth claim.

All 96 layer-specific paths are enumerated and checked.  Because retained word
positions differ by layer, ingress costs vary:

| quantity | minimum | maximum |
|---|---:|---:|
| layer | 6 | 92 |
| ingress elementary CNOTs | 524,974 | 717,418 |
| ingress SWAPs before expansion | 174,493 | 238,641 |
| maximum individual path length | — | 127 |

The 96-layer action-manifest digest is
`85c736e58dcd92c580f00f0f8fbad892ee73362202a62d651acce2ecb0d0f670`.
Ingress and egress have equal counts.

## Exact Cycle 467 composition

The literal retained held block is the center operation at layer 48.  Its
ingress has 607,726 elementary CNOTs; ingress plus inverse egress has 1,215,452.
Composed with the frozen Cycle 467 arithmetic route, the complete block has:

| primitive | count |
|---|---:|
| NOT | 330,624 |
| CNOT | 13,327,345 |
| Toffoli | 276,696 |
| **total / strict serial depth** | **13,934,665** |
| maximum edge primitive incidence | 9,749 |

Cycle 467's routed segment reproduces its frozen digest
`4d6f058d95cc32538f3a15b6fd0eb620f7708371e6276298d063ba44078d1457`.
The ingress digest is
`ca22599b79200dfab81c2f5fe1e567e39cecfcd04d1bd18411b8d1deab36741b`;
the complete round-trip transfer digest is
`4c11713e64197239555b568facf1d47c2cff1908d15b80fe3c67d02406caec46`;
and the combined segment manifest is
`4b3c532fe2507e72c529e32a396d7288e28042a493492f55eff9dc6f906a7502`.

The executable initializes the six persistent source words and central source,
executes every ingress primitive, checks all port words, streams and executes
every Cycle 467 nearest-neighbor primitive, runs inverse egress, and compares
all 448,000 physical M2 states with the pre-block state.  The only permitted
difference is the retained target word, which must equal Cycle 463's exact
coarse output.  Port leakage, arithmetic work leakage, physical-bit residuals,
route adjacency failures, and final-placement failures are all zero.

## Train, held-size, domain, and deletion controls

All **14,592** Cycle 463 operations are replayed: 2,592 train and 12,000 held.
For each operation, the runner verifies its target-relative six-neighbor star
lies in the active-plus-shell physical domain, stages the exact endpoint words,
applies the frozen Cycle 467 32-state long-division permutation, and matches the
retained coarse target with zero remainder.  The all-row digest is
`f1e6c65e511044008e5ce04cce8117e646be40eafda1b806933e4774f7fd01db`.
This held cube test uses the same path family and capacity without refit.

The all-row replay uses exact endpoint semantics plus the already exhaustive
Cycle 467 divider permutation; it does not execute roughly fourteen million
primitives 14,592 separate times.  The one literal full-width held block and
the exhaustive occupied-path lemmas expose that distinction.

Controls require:

- deleting any of the six delivered center-neighbor values changes the selected
  held center output;
- deleting central-source delivery changes that output;
- deleting return leaves a populated port outside the code;
- deleting one route primitive has a finite exhaustive witness;
- a nonblank destination port is refused;
- a non-unit direction, layer 96 update, undeclared radius 3, or non-nearest
  path is refused.

These are route-local necessities, not constitutional minima.

## Proper-cubic covariance

Each proper-cubic frame acts on the coarse signed direction vector and on local
M2 coordinates together.  A negative local axis uses `p -> 39-p`, while coarse
cells transform linearly; this preserves boundary adjacency.  **Source and
target direction labels are carried**: `(source direction d, target 0)` maps
to `(F d, 0)`.  Endpoints, every path vertex, primitive support, action order,
and the composed Cycle 467 segment are carried by the same frame.

The runner constructs all 24 proper-cubic frames, carries every action in the
literal composed layer-48 block, checks every path edge and all six transformed
direction labels, and emits 24 distinct combined manifests.  The separately
enumerated 96-layer manifest uses the same uniform affine action.  There are zero carried-path
or label failures.  It does not infer schedule covariance from output
invariance and does not use a preferred global re-sorting rule.

The target-relative local frame is supplied structure.  Covariance of its full
24-frame orbit is established; an autonomous physical frame-selection law is
not derived.

## Prior-art and novelty boundary

Nearest-neighbor SWAP routing, the three-CNOT SWAP identity, and remote endpoint
operations by move/apply/unmove are standard reversible-circuit constructions.
Cycle 470 does not claim them as new and makes no optimality claim.

The repository advance is their exact composition with the frozen Cycle
463/467 objects: explicit persistent/compact placement, actual six-face
crossings, all 96 layer paths, exact capacity and congestion, every train/held
row, one literal 448,000-M2 held block including all arithmetic primitives, and
the all-24 carried schedule.  This is bounded compiler evidence, not new
transport physics.

## Complete supplied/constructed/open inventory

Supplied:

1. the Cycle 463 retained histories, central source, target schedule, 249-bit
   code, finite cubes/shells, `D`, six-neighbor law, and 96 layers;
2. Cycle 467's logical and routed arithmetic compiler;
3. scale-40 physical supercells and the new persistent/compact placement;
4. blank arithmetic ports/work and the computational-basis word code;
5. a target-relative reference frame, signed-direction action enumeration,
   Manhattan path convention, and strict serial schedule;
6. explicit wall/RSS test caps.

Constructed: occupied-path remote CNOT and endpoint SWAP; inverse return;
nearest-neighbor face crossings; exact action/gate/depth/congestion/capacity
counts; all-layer and held-size schedules; literal physical E/G composition;
deletions; and all-24 covariance.

Open: globally overlapped scheduling of adjacent target stars; a lower-depth or
lower-congestion router; an autonomous local-frame convention; removal of
retained history; derivation of the finite relaxation/source/clock laws;
infinite-volume and continuum limits; matter/energy-stress identification;
occurrence, Records, Born probability, lapse, metric, curvature, backreaction,
or gravity.

## TOE dependency ledger

| wall | Cycle 470 disposition |
|---|---|
| `C_ref` | unchanged; transport selects no vacuum, sea, phase origin, or preparation |
| `C_num` | unchanged; copying computational-basis ports does not choose a physical number reference or superselection law |
| `C_wrap` | unchanged; layer ordinal and 13,934,665-event schedule are not winding, causal interval, or time |
| `C_int` | unchanged; the transported/arithmetic law remains supplied and has no derived interaction selection, protection, or rate |
| `C_local` | constructively narrowed: Cycle 467's named inter-supercell delivery boundary closes for one exact serial seven-cell block with restored placement; overlapping lattice-wide star scheduling remains open |
| `C_source` | implementation-only narrowing: the supplied source bit reaches the arithmetic block locally, but its energy/stress meaning, conservation, and backreaction remain open |

No wall pair collapses.  Transporting a bit does not select its physical
meaning or law; deriving a source law would not by itself route its registers.

## Full no-go discipline

### N1 — Alternative route enumeration

| normalized route family | object / mechanism / terminal obligation | status |
|---|---|---|
| occupied-path walk | retained words / SWAP-move, endpoint action, unmove / exact serial seven-cell block | **ATTEMPTED — SUCCEEDS** |
| clean fanout corridors | retained words plus blank lanes / CNOT propagation and cleanup / parallel bounded block | **OPEN — NOT ATTEMPTED** |
| face caches | redundant locally constrained words / six cached faces / low-depth repeated delivery | **OPEN — NOT ATTEMPTED** |
| packet or sorting network | labeled word packets / reversible routing network / globally conflict-free layer | **OPEN — NOT ATTEMPTED** |
| staggered edge coloring | overlapping stars / cubic coloring and time multiplexing / full-layer schedule | **OPEN — NOT ATTEMPTED** |
| link/gauge mediator | link registers / autonomous local transport dynamics / delivered interaction/source response | **OPEN — NOT ATTEMPTED** |

The positive occupied-path route defeats an impossibility claim.  Open routes
also prevent minimum-depth, minimum-congestion, and unique-content claims.

### N2 — Wall-independence audit

Collapse details into `Wp` local port delivery, `Wo` overlapping full-layer
scheduling, `Wa` arithmetic, `Wl` finite law/boundary selection, `Ws` source
meaning/conservation, `Wc` causal clock interpretation, and `Wg` geometry/
backreaction.  `Wp` closes neither `Wo` nor any physics wall.  Arithmetic does
not deliver ports; overlap scheduling does not select a law; source meaning
does not derive time; clock interpretation does not imply curvature; gravity
does not select this router.  They remain independent at the tested level.

### N3 — Hidden-wall scan

The scan exposes persistent/compact placement, blank ports/work, basis-word
code, target staging, source staging, fixed histories, `D`, layer-dependent
paths, target-relative frame, bit/direction enumeration, and strict serial
conflict policy.  Paths traverse arbitrary states, so no hidden blank-corridor
condition is used.  Global overlapping-star scheduling remains explicit.

### N4 — Residual matching

Cycle 467 named inter-supercell delivery to its declared ports as the exact
residual.  This construction matches it directly and composes the frozen trace.
It does not match finite-law selection, source conservation, time, continuum,
or gravity residuals and is not cited against them.

### N5 — Rhetoric audit

Evidence is per primitive, arbitrary short occupied path, bit, word, layer,
local star, train/held schedule row, literal 448,000-M2 block, and carried frame.
Claims stop at one serial local block.  Depth is a schedule count, not time;
source is a bit, not energy/stress.  No lower bound, optimum, universal network,
continuum, or gravity conclusion is promoted.

### N6 — Partial-closure path scan

Cycle 467 made the port boundary explicit.  Cycle 470 closes it constructively
for a serial block without an axiom edit.  The next partial closure is an
overlap-aware whole-layer router or a more efficient face-cache/network route,
followed separately by law/source derivation.  No “new axiom required” step is
licensed.

### N7 — Steelman

A hostile reviewer should object that serial move/apply/unmove is extremely
deep, repeatedly loads congested edges, supplies a local frame, and does not
execute simultaneous adjacent stars.  Face caches with local equality checks,
reversible sorting networks, edge-colored staggered schedules, or dynamical
link variables could be much stronger.  Those are live constructive campaigns.

### N8 — Cross-cycle echo and claim gate

Cycle 467's exact port-delivery residual is retired only at the stated serial
local-block terminal.  Cycle 463's law/source/time/gravity cautions remain.
Earlier `C_local` failures concerned different CAR or global scheduling
obligations; they are not promoted through this successful arithmetic route.
`C_wrap`, `C_source`, continuum, and backreaction echoes remain unresolved.

**No-go claim: FAIL. Minimum-content claim: FAIL. Axiom-pressure claim: FAIL.**
There is **no axiom pressure**.

## Frozen executable disposition

Retention requires zero failed tests, exact reproduction of the frozen Cycle
467 routed digest, and resource use below 240 seconds and 1,536 MiB.  The Cycle
470 runner and note keep authority none and audit unset and do not authorize an
audit verdict, merge, or protected-surface edit.

The final cold run reports `RESULT pass=11 fail=0`, takes 104.786 seconds, and
peaks at 118.53 MiB.  Runner SHA-256:
`287b72625b4bf7d29cb847e0a59ed5d64f58b3ec55e5b312942f96bbc0ea6674`.
