# Cycle 703 local cellular plaquette decoder — 2026-07-25

Authority: none

Audit: unset

## Scope and result

The preceding open-BKSF state encoder used an exact open-boundary Gaussian or
path decoder for the coarse plaquette stage.  Its checks were local, but the
chosen correction reached the boundary and was supplied by a size-dependent
table or path.  This checkpoint removes that host-selected correction.

There is one fixed radius-one cellular rule, identical at every size.  It
reads stored local plaquette outcomes, propagates prefix bits through the open
box, and lets each newly ready bit control its colocated matter-stream Z once.
The rule then becomes locally quiescent.  It uses no Gaussian table, selected
path, target-state query, global apply barrier, or host-selected stop.  The
number of iterations grows as `2(L-1)`, but no iteration counter is physical
time.

The construction is exact for every lawful syndrome on every finite open
cubic box, not only the tested sizes.  L2 is exhaustive over all 4,096 edge
error patterns and all 32 distinct lawful syndromes.  Exact basis, linearity,
Bianchi, covariance, and deletion tests pass through held L8.

The result is a local dissipative-controller construction, not yet a closed
physical-M2 controller compiler.  Plaquette measurement records, blank
classical cellular memory, irreversible ready flags, and later record reset
are explicit apparatus supply.  A scheduled XOR compute/control/uncompute
circuit can return its recurrence work, but an autonomous local reversal pulse
and unitary erasure of the measured syndrome record are not constructed.  No
general impossibility is claimed.

## Fixed cellular rule

Use the transported Cycle-232 coframe and its lower boundary corner.  Write the
measured coarse plaquette two-form as `F_xy,F_xz,F_yz` and choose the axial
gauge `A_x=0`.  Boundary seeds are zero, and the same three local recurrences
are iterated:

```text
A_y(0,y,z)       = 0,
A_y(x+1,y,z)     = A_y(x,y,z) xor F_xy(x,y,z),

A_z(0,0,z)       = 0,
A_z(0,y+1,z)     = A_z(0,y,z) xor F_yz(0,y,z),
A_z(x+1,y,z)     = A_z(x,y,z) xor F_xz(x,y,z).
```

A newly written `A_y` or `A_z` bit controls Z on the corresponding physical
matter-stream edge exactly once.  Ready flags prevent a second emission.
Every transition reads only a predecessor, one adjacent plaquette bit, and the
local blank target.  The spatial neighborhood radius is one.  The deepest
`A_z` value travels first along the lower x face in y and then through the box
in x, so the forward rule is quiescent after exactly `2(L-1)` rounds.

This is translation compatible when the box and its boundary corner are
translated together.  It is not a rule that mysteriously selects an absolute
origin from an unmarked homogeneous lattice.

## All-lawful-syndrome theorem

For an open L-cube there are

```text
P = 3 L (L-1)^2
```

plaquettes and `(L-1)^3` independent cube-Bianchi rows.  Hence the closed
two-form exponent is

```text
P - (L-1)^3 = (L-1)^2 (2L+1).
```

The edge-to-plaquette incidence rank is independently

```text
3 L^2 (L-1) - L^3 + 1 = (L-1)^2 (2L+1).
```

Thus, on an open contractible box, the lawful measured syndrome space is
exactly the cube-closed two-form space.

The first recurrence gives `(delta A)_xy=F_xy` and the third gives
`(delta A)_xz=F_xz` identically.  The boundary recurrence gives
`(delta A)_yz=F_yz` on the lower x face.  The cube-Bianchi identity

```text
Delta_x F_yz xor Delta_y F_xz xor Delta_z F_xy = 0
```

then propagates the last equality one x layer at a time.  Therefore
`delta A=F` for every lawful F and every L.  The finite runner checks the same
identity, image/closed-space rank equality, and every incidence basis column.

## Training and held-size controls

| L | Coarse edges | Plaquettes / rank | Cube-Bianchi rank | Basis cases | Output failures | Rounds |
|---:|---:|---:|---:|---:|---:|---:|
| 2 | 12 | `6 / 5` | 1 | 12 | 0 | 2 |
| 3 | 54 | `36 / 28` | 8 | 54 | 0 | 4 |
| 4 | 144 | `108 / 81` | 27 | 144 | 0 | 6 |
| 5 | 300 | `240 / 176` | 64 | 300 | 0 | 8 |
| 6 | 540 | `450 / 325` | 125 | 540 | 0 | 10 |
| 7 | 882 | `756 / 540` | 216 | 882 | 0 | 12 |
| 8 | 1,344 | `1,176 / 833` | 343 | 1,344 | 0 | 14 |

L2 enumerates all `2^12=4096` edge patterns, finds exactly `2^5=32`
distinct lawful syndromes, and closes all 32.  At every L the runner checks
every unit-edge incidence syndrome.  Because the ready pattern is geometric
and every value update is XOR-linear, those columns plus exact linearity imply
the result for every lawful XOR combination of syndrome bits.  Sixty-four
deterministic combined-column tests per size have zero linearity failures.
All basis inputs have zero cube-Bianchi residual and every work site becomes
ready.

The same rule and coefficients are frozen from L2 onward; L6--L8 are held
sizes, not refits.

## Proper-cubic and boundary covariance

The rule is axial in its local chart, so the covariance obligation is chart
covariance, not literal equality after rotating the lattice while freezing the
coframe labels.  The runner transports the coframe, lower-face boundary
corner, syndrome plaquettes, and correction edges together.

On L4 it tests all 144 unit-edge inputs, all 24 proper-cubic frames, and two
translations: 6,912 frame/translation/input cases.  A direct transported-chart
decoder has zero output-transport failures; transformed corrections have zero
syndrome failures and every transformed box retains 64 distinct cells.  The
coframe and boundary corner remain supplied structure.  An origin-free
isotropic decoder is not claimed.

## Code preservation and deletions

Every emitted operation is Z on a matter-stream edge M2.  Therefore it
commutes with every vertex `B_v` and local `D_x`, and it does not reopen the
cell-triangle stage.  It can change a bond-rectangle outcome, which is why the
existing fixed local bond correction remains stage three.  No periodic Wilson
sector is present or tested.

On L4 the runner deletes each rule clause independently and replays all 144
unit-edge syndromes:

| Deleted clause | Syndrome failures | Incomplete wavefronts | Nonquiescent emissions |
|---|---:|---:|---:|
| correction emission | 144 | 0 | 0 |
| one-shot ready latch | 111 | 0 | 144 |
| A-y propagation | 96 | 144 | 0 |
| A-z boundary propagation | 87 | 144 | 0 |
| A-z x propagation | 99 | 144 | 0 |
| A-y seed | 96 | 144 | 0 |
| A-z seed | 108 | 144 | 0 |
| F-xy source XOR | 96 | 0 | 0 |
| F-xz source XOR | 96 | 0 | 0 |
| F-yz source XOR | 24 | 0 | 0 |

All ten active clauses are detected.

## Auxiliary return and dissipative measurement supply

At the Boolean circuit level, each recurrence is XOR into a blank target from
a retained predecessor and retained syndrome bit.  All eight local truth rows
round-trip exactly under a second application.  Consequently a scheduled
finite circuit can:

```text
stored syndrome
  -> compute recurrence into blank local work
  -> apply controlled physical Z
  -> reverse recurrence and return the work blank.
```

That statement does not provide an autonomous returned-work CA.  The actual
fixed rule tested here uses irreversible `not-ready -> ready` writes and emits
when a value first becomes ready.  Its classical memory is part of the local
measurement apparatus and is reset dissipatively.  More importantly, the
original plaquette outcomes remain nonblank even if recurrence work is
uncomputed.  Erasing those records unitarily after mapping all syndrome
branches to the same vacuum would violate reversibility unless the branch
information is retained elsewhere.

The honest resource disposition is therefore:

- no host selects a correction, path, coefficient, or stopping size;
- bounded classical memory per local edge/check is sufficient;
- measurement, outcome retention, and reset are dissipative apparatus supply;
- a returned-work local echo/ack controller and its M2 realization remain
  open;
- no pointer copy here is called a Record.

## Supplied structure and dependency effect

Supplied structure is the open boundary and its lower coframe corner, the
transported Cycle-232 proper-cubic coframe, local plaquette measurements,
blank bounded classical controller memory, dissipative record reset, and
uniform iteration of the fixed rule.  There is no global parity service,
Gaussian inverse table, stored correction path, target-amplitude query, or
runtime host correction choice.

| Wall | Effect |
|---|---|
| `C_ref` | improved operationally: the supplied coframe/reference graph now generates its correction through one local recurrence; coframe and boundary-corner genesis remain supplied |
| `C_num` | unchanged: the decoder is syndrome-linear and number blind |
| `C_wrap` | unchanged: CA rounds and measurement stages are not causal time or realized history |
| `C_int` | improved indirectly: the inherited local contact/seam update can now start from a locally decoded open code without a host path table |
| `C_local` | materially improved: the one-shot growing-range feedforward is replaced by a radius-one uniform rule with growing iteration count; physical M2 controller and dissipative reset remain explicit |
| `C_source` | unchanged |

This is not a Record, Born/probability, gravity/source, or causal-time result.
No axiom pressure follows.

## No-go-discipline N1-N8 gate

The fresh `origin/main` no-go-discipline instructions were applied.  The
positive cellular result is retained.  The broader proposition that no
closed-unitary autonomous decoder exists fails the N1/N7 gate because concrete
routes remain untested.  Accordingly this note makes only an inventory
statement: such a decoder is not constructed here.

### N1 — alternative route enumeration

1. **Forward dissipative axial CA — ATTEMPTED.** It succeeds exactly for every
   open-box lawful syndrome and removes host-selected paths/tables.
2. **Scheduled reversible XOR compute/control/uncompute — ATTEMPTED.** Every
   local truth row returns, but the scheduled construction retains the measured
   syndrome and does not supply an autonomous reversal controller.
3. **Local leaf-acknowledgement/echo CA — OPEN.** A boundary echo could reverse
   the axial dependency forest after every child emits; its collision-free
   reversible state machine and M2 embedding were not attempted.
4. **Direct measurement-free Clifford vacuum circuit — OPEN.** It can bypass
   syndrome records entirely; the existing unique stabilizer tableau makes
   this a concrete synthesis obligation, not an excluded route.
5. **Local dissipative cooling/Lindblad preparation — OPEN.** It would retain
   locality while replacing explicit measurement records by an admitted bath.
6. **Boundary export of syndrome entropy — OPEN.** A local conveyor can move
   branch information to a boundary reservoir, but finite returned capacity
   and repeated-use reset are not constructed.

Because routes 3--6 are open, a general no-go is premature.  The gate outcome
for such a claim is **FAIL**, so no negative claim ships.

### N2 — wall-independence audit

After collapsing implementation phrasings, the remaining conditions are:
`W_M2-return` (autonomous local returned-work controller), `W_reset`
(measurement-record entropy/reset), `W_boundary` (origin/coframe genesis), and
`W_Wilson` (periodic sector selection).

| Pair | First closes second? | Second closes first? | Independent? |
|---|---|---|---|
| M2-return / reset | no | no | yes |
| M2-return / boundary | no | no | yes |
| M2-return / Wilson | no | no | yes |
| reset / boundary | no | no | yes |
| reset / Wilson | no | no | yes |
| boundary / Wilson | no | no | yes |

A reversible controller can still retain a measurement record; a dissipative
reset does not choose a boundary chart; and neither open-boundary issue selects
a periodic Wilson sector.

### N3 — hidden-wall scan

The open shape, lower corner, coframe, boundary markers, local measurement,
blank controller bits, irreversibility of ready writes, record retention/reset,
fixed-point iteration, and absent returned pulse/M2 controller are explicit.
“Lawful” means the measured syndrome lies in the edge-incidence image, which
the rank/Bianchi equality tests rather than assumes.  “Canonical” is not used
to hide a selector.

### N4 — residual matching

The predecessor open-preparation note established a growing radius for a
one-shot local correction.  This checkpoint attacks exactly that residual by
allowing a fixed radius-one rule to iterate; it does not cite phase-rephase,
direct-route, or periodic-Wilson failures as witnesses.  The new resource
residual is different: dissipative controller/record supply after the host
path has been removed.

### N5 — rhetoric audit

Tested resolutions are each recurrence truth row, every L2 lawful syndrome,
every unit-edge generator through L8, all lawful syndromes by linear/Bianchi
proof, and all 24 transported bulk/boundary charts at L4.  Arbitrary open
shapes, unmarked-boundary origin selection, periodic boxes, noisy syndromes,
fault tolerance, M2 controller gates, and repeated finite-capacity reset are
not tested.  Therefore the result is phrased as an exact open cubic-box
decoder, not a universal local-decoding fact.

### N6 — partial-closure paths

The principal partial closure is already positive: replace one-shot range by
growing rounds of one local law.  A local echo/ack state machine can target
returned work; direct Clifford synthesis can avoid measurement; persistent
outcome storage can defer reset; and a named local bath can make dissipation an
explicit resource.  These are implementation/import-retirement paths, not
evidence for a new axiom.

### N7 — steelman

A hostile reviewer should reject any closed-unitary no-go immediately.  The
axial recurrence forms a bounded-degree dependency forest.  Each leaf can emit
its controlled Z and return an acknowledgement; acknowledgements can propagate
backward while locally uncomputing child values, and a direct Clifford
synthesis of the already full-rank vacuum tableau may avoid the syndrome tape
altogether.  The terminal obligation is an explicit finite-state reversible
local transition table, returned auxiliaries, M2 gate decomposition, and
held-size/covariance tests.  Those actionable routes remain open.

### N8 — cross-cycle echo

The earlier diagonal-rephase failures were escaped by changing to the
local-Gauss representation.  The predecessor feedforward-radius obstruction is
escaped here by changing from one-shot correction to iterated local dynamics.
Both echoes warn against constitutional inference.  The remaining
dissipation/return issue must be attacked as its own controller-resource lane;
it creates no shared obstruction or axiom pressure.

## Reproduction

With the Cycle-703 runner and pinned repaired-loader dependencies on
`PYTHONPATH`, run:

```text
python3 scripts/frontier_cycle703_local_cellular_plaquette_decoder_2026_07_25.py
```

The terminal marker is
`CYCLE703_UNIFORM_RADIUS1_CA_CLEARS_ALL_OPEN_L2_L8_BASIS_SYNDROMES`.
The content-pinned cache is
`logs/runner-cache/frontier_cycle703_local_cellular_plaquette_decoder_2026_07_25.txt`.
