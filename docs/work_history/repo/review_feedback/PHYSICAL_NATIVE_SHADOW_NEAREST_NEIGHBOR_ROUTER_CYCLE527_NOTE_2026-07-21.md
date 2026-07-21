# Physical native-shadow nearest-neighbour router — Cycle 527 (2026-07-21)

Authority: none.  Audit: unset.  Constitutional effect: none.

Runner:
`scripts/physical_native_shadow_nearest_neighbor_router_cycle527_2026_07_21.py`.

## Result

Cycle 527 closes the **pre-seam physical nearest-neighbour routing** obligation
for Cycle 523's six-output decoder on the actual Cycle-522/Cycle-269 native
role identities.  Each coarse cell receives a fully installed periodic
`16 x 16 x 16` integer microgrid.  The installed union is therefore **4,096
M2 per cell**, of which 23 are the inherited native roles, six are the
occupation shadows, and 4,067 are blank route sites.

The actual native inventory is not multiplied by incidence counting.  On a
periodic lattice of `L^3` cells it contains exactly `15L^3` face M2,
`6L^3` port M2, `L^3` flags, and `L^3` companions: `23L^3` installed native
M2.  The `15L^3` faces have `30L^3` face-port incidences.  Cycle 527 reports
both numbers separately.

For cell `x` and direction vector `D_d`, the load-bearing decoder coordinates
inside the fine torus are

```text
f_x       at 16x,
c_(x,d)   at 16x + 2 D_d,
q_(x,d)   at 16x + 3 D_d.
```

The inward control is the actual neighboring opposite port
`c_(x+D_d,d^1)`, at `16x + 14D_d`.  Every required pair is therefore
collinear on one cubic axis.  Each remote CNOT moves its control along that
axis with ordinary SWAPs, applies one adjacent CNOT, and reverses every SWAP.
The route works for arbitrary intermediate M2 states; it does not rely on
silently blanking a native face, port, flag, companion, or previously computed
shadow.

The exact selected-pattern relation remains

```text
q_d = c_d XOR i_d XOR (c_d AND f)
      XOR (c_bar AND i_d) XOR (c_bar AND f).
```

Each direction uses two routed CNOTs and three Toffolis.  Every Toffoli is the
exact 15-gate H/T/CNOT decomposition from Cycle 523, and every constituent
CNOT is routed as above.  The resulting fixed decoder uses **1,338** one- or
two-M2 nearest-neighbour calls per cell:

| primitive | calls per cell |
|---|---:|
| ordinary SWAP | 1,056 |
| CNOT | 120 |
| H | 36 |
| T | 72 |
| T-dagger | 54 |
| total | **1,338** |

The inverse is the reversed dagger list and uses another 1,338 calls.  With
native controls unchanged it erases all six shadows and restores every route
site exactly.  No native control changes during compute or inverse.

At L5 and held L6 the combined selected-pattern census contains **327,360**
cell/direction tests and zero failures.  All 64 occupation words occur.
There are zero terminal route-work, native-control, inverse-shadow, or inverse
route-work failures.  Deleting the five monomials produces
`48, 48, 8, 16, 8` failures for every direction at both sizes.

This is a physical router for the pre-seam decoder, not the complete
Cycle-230 compiler.  No shared obstruction and no axiom pressure are inferred.

## Exact target contract

| field | Cycle-527 contract |
|---|---|
| target statement | On L5 and held L6, compile the selected-native six-shadow decoder and inverse into an injective periodic integer-3D schedule of one-/two-M2 nearest-neighbour gates. |
| domain | All 160 selected Cycle-522 local terms at every cell; all 24 proper-cubic frames; all 576 products. |
| allowed premises | Cycle-269 role identities, Cycle-522 selected grammar, Cycle-523 ANF, blank microgrid, ordinary H/T/CNOT/SWAP law. |
| forbidden weakenings | No nonlocal CNOT, hidden parity service, global Jordan-Wigner order, host-side branch, dirty terminal work, or fermionic FSWAP relabeled as ordinary routing. |
| completion witness | Injective coordinates; every two-M2 call has periodic fine-grid L1 distance one; exact decoder/inverse; zero layer clash; frame and group closure. |
| not closure | Post-reduction endpoint readout, transformed-output cleanup after a q-changing update, primitive native dense coin, recurrent full-volume seam, physical elapsed time. |

## Coordinate embedding and native inventory

Let the fine torus have side `16L`.  Coarse centers are `16x`.  Native port
M2 occupy `16x+2D_d`; the flag occupies `16x`; the unused companion is placed
at `16x+(1,1,1)`.  Internal triangular face M2 use the twelve distinct
offsets `D_d+D_e` for nonopposite pairs.  Each positive-owned outer square
face occupies the integer midpoint `16x+8e_a`.

These 23 native coordinates and the six shadow coordinates are injective at
every cell and across periodic cells at both sizes.  The rest of the full
microgrid is installed blank work.  This overprovisioning is deliberate: it
turns every required axis segment into a literal physical path and makes
crossings ordinary tensor-wire transport rather than an undeclared nonlocal
gate.

For the 22 native roles that transform geometrically in this decoder (faces,
ports, and flag), the canonical role map agrees with coordinate rotation in
all frames.  The companion `r` is not read, moved, or used by the schedule;
its spectator coordinate rotates with the code-frame placement family.  Thus
Cycle 527 proves covariance of the decoder and its full physical path family,
not a new canonical one-site geometric realization of the pre-existing
`f+r` gauge constraint.

## Ordinary SWAP is not fermionic FSWAP

The route primitive is ordinary tensor-factor SWAP,

```text
SWAP |11> = +|11>.
```

Cycle-230 fermionic FSWAP instead obeys

```text
FSWAP |11> = -|11>.
```

Their two-M2 matrices have Frobenius distance exactly 2.  The decoder moves
auxiliary wire states through a tensor-product microgrid; it never claims to
permute two CAR modes.  The FSWAP used by the coarse fermionic stream remains
a different physical operation with a different off-code completion.

The runner exhausts 135,260 basis cases for remote CNOT paths of lengths
`1,2,3,5,11,16`, including arbitrary intermediate states, with zero failures.
The bare Toffoli reconstruction residual is
`7.346882794269506e-16` and its inverse residual is
`1.2749064385906742e-15`.  Deleting the distance-11 CNOT core changes the
logical target, while deleting a return SWAP leaves intermediate M2 dirty.

## Simultaneous L5 and held-L6 routing

One cell's decoder touches a bounded union of six axis corridors.  Cycle 527
constructs the exact cell-support conflict graph, greedily colors it, and then
checks every scheduled physical layer.  The coloring is a compiler phase
label, not causal time.

| item | L5 train | held L6 |
|---|---:|---:|
| coarse cells | 125 | 216 |
| fine torus side | 80 | 96 |
| installed M2 union | 512,000 | 884,736 |
| native M2 union | 2,875 | 4,968 |
| global decoder calls | 167,250 | 289,008 |
| decoder-plus-inverse calls | 334,500 | 578,016 |
| conflict-graph maximum degree | 6 | 6 |
| cell color phases | 4 | 2 |
| same-color support collisions | 0 | 0 |
| gate-layer operand collisions | 0 | 0 |
| decoder depth upper bound | 5,352 | 2,676 |
| decoder-plus-inverse depth upper bound | 10,704 | 5,352 |
| maximum decoder uses of one physical edge | 40 | 40 |
| maximum roundtrip uses of one physical edge | 80 | 80 |

The odd L5 torus needs four constructive colors; held L6 needs two.  No
intercell route is applied concurrently with another route touching the same
site.  The number of colors is bounded by the finite local conflict graph; it
does not scale with the number of cells in either tested family.  No duration,
rate, generator, physical energy, Record, or realized history is inferred
from the gate or color counts.

## Proper-cubic covariance

Coordinate rotation maps every physical path edge to another integer path
edge of periodic L1 length one.  At both sizes:

- all assigned coordinates remain injective in all 24 frames;
- all geometric native role maps used by the decoder agree exactly;
- all six direction schedules map to the corresponding rotated direction
  schedules with zero failures;
- all cell support sets map exactly;
- every mapped color class remains conflict-free; and
- **all 576** frame products close with zero failures.

The L5 canonical cell schedule digest is
`5c8792e9b409e9a0123dd4e63962ad9c1e4f8d58223fd3b564f064c60f8df69c`;
the L6 digest is
`740a4818609fc36039cd9bc992536aa93d9a1c05d768fdc07f171309112fc67c`.
The lists are fixed once the size, microgrid scale, and candidate primitive
law are supplied.  There is no runtime frame query or host-side adaptation.

## Decoder code, inverse, leakage, and deletions

Let `E_native` denote one selected Cycle-522 term with all new grid sites
blank, and let `E_shadow` append the six ANF values.  The certified decoder
`D_NN` satisfies on every selected term

```text
D_NN E_native = E_shadow.
```

Because every route moves a control through ordinary SWAPs, applies CNOT, and
reverses the same path, all intermediate states—not only initially blank
ones—are restored after each routed CNOT.  The native face, port, flag, and
companion values are terminally unchanged.  With the same native controls,

```text
D_NN^dagger E_shadow = E_native.
```

The inverse statement is conditional in a precise way.  If an intervening
operation changes a shadow without transforming its native controls into the
matching output pattern, applying `D_NN^dagger` leaves the XOR mismatch in the
shadow.  Cycle 527 does not call that unfinished transformed-output cleanup an
impossibility.

Deletion controls are load bearing at two levels:

1. deleting the five logical monomials yields the exact nonzero selected-row
   counts `48,48,8,16,8` per direction;
2. deleting a routed CNOT core changes its remote logical output, while
   deleting one return SWAP corrupts terminal intermediate restoration.

## Cycle-526 reduced-seam boundary

The decoder must be placed **compute-before-seam**.  Cycle 526's joint
two-cell reduction has 25,088 occupied reduced rows and 25,600 nonzero
amplitudes, hence **512 shared rows**.  All 512 conflict for the two actual
seam-endpoint occupation bits; the other ten cell/direction bits are
row-constant.  Applying the single-cell ANF naively after joint reduction
fails 18,528 of 51,200 endpoint/nonzero-row tests at both L5 and held L6.

Therefore Cycle 527 does not claim a diagonal post-reduction endpoint
readout.  Its exact result prepares six shadows on selected local terms before
joint multiplication.  Cycle 526 supplies a bounded dense augmented update
with persistent endpoint shadows, but primitive transformed-output cleanup
and recurrent volume remain separate obligations.  The new NN path theorem
does not silently turn that dense algebraic completion into a primitive law.

## Approach-family registry

| family | object / mechanism | terminal obligation | strength | status |
|---|---|---|---|---|
| full cubic microgrid | axis-collinear SWAP/CNOT transport through arbitrary states | injective NN paths, conflict coloring, inverse | target-equivalent | candidate-complete here |
| sparse private petals | degree-six incidence gadget with private blank routers | injective integer-3D embedding | target-equivalent | retired from Cycle 527 after degree alone proved insufficient |
| remote parity ladders | blank CNOT fanout chains without token transport | covariant sparse paths and collision-free global schedule | target-equivalent | unexplored/live efficiency route |
| shared moving bus | one reused courier per cell | constant color count and exact bus restoration | unknown/comparable | unexplored/live efficiency route |
| persistent edge shadows | transport endpoint values with the seam | primitive preparation plus transformed-output update | stronger than routing target | provisional in Cycle 526 |

The candidate-complete label applies only to the exact pre-seam routing target.
It does not apply to the stronger dynamic or recurrent obligations.

## Supplied structure and novelty boundary

| item | status in Cycle 527 |
|---|---|
| Cycle-269 face/port graph and 23 native roles per cell | supplied retained representation |
| Cycle-522 selected 160-term grammar | supplied candidate representation |
| Cycle-523 degree-two ANF | supplied exact decoder relation |
| Cycle-526 512-row joint-reduction conflict census | supplied exact boundary |
| `16 x 16 x 16` full microgrid and blank preparation | new supplied layout/preparation import |
| native and shadow integer coordinates | constructed here |
| ordinary H/T/CNOT/SWAP primitive matrices | supplied candidate physical gate law |
| remote CNOT and Toffoli NN decompositions | derived and exhaustively checked here |
| L5/L6 conflict coloring | constructed and checked here |
| physical gate duration or energy | not supplied or inferred |
| primitive native dense coin and transformed-output cleanup | not synthesized |
| full recurrent Cycle-230 stream | not synthesized |

The runner enforces strict SHA-256 equality for every load-bearing predecessor
that it imports or reads before accepting the certificate:

| predecessor | runner SHA-256 |
|---|---|
| Cycle 235 | `dd955ce629cde5e225b625be89f5f71045d688083a032b7bf104efa9b3f1bb34` |
| Cycle 269 | `c7b8673eb1a0dced08131820caa1fb2400fc8d1f73cfe2cddf5f8a28f9045d35` |
| Cycle 311 | `4495bf39e1e2661866501e377b8ec1aefff656e261e428fa5b6738f73b49699c` |
| Cycle 522 | `d6a7700d7575dfba02d4b4d2438e54d37a02c6ca7f71673c8a871b474f6e088b` |
| Cycle 523 | `d9dd02bbb4dfacebf0f75f6b8c56881ff56653843cb7ed75baa381d5aa605b9d` |
| Cycle 526 | `7c3d4a35664eaf5c7737c86464ca069e15ce29c40f61778081af8139970c37cd` |

Semantic-fragment checks remain supplementary and cannot substitute for the
byte-exact gates.

The novelty is the explicit integer-cubic embedding, complete routed gate
list, and collision/covariance certificate.  Generic SWAP routing, Clifford+T
Toffoli decomposition, and graph coloring are standard compiler machinery and
are not claimed as new physics.  The 4,096-M2 cell is a valid constant-overhead
witness, not a minimum-content or resource-optimality claim.

## N1–N8 no-go discipline

Gate status for any broad compiler impossibility, minimum-M2 conclusion, or
axiom-pressure claim: **FAIL / DO NOT SHIP**.  The only bounded negative
retained is the exact Cycle-526 post-reduction diagonal-readout counterexample.

### N1 — alternative-route map

1. **Full cubic microgrid routing — ATTEMPTED / POSITIVE HERE.**  Ordinary
   SWAP/CNOT corridors close the pre-seam NN route with constant but large
   overhead.
2. **Sparse private-router embedding — ATTEMPTED / RETIRED HERE.**  A
   degree-six abstract gadget was constructed, but degree and coarse span did
   not prove an injective integer embedding; it is not evidence against a
   better sparse gadget.
3. **Persistent endpoint-shadow update — ATTEMPTED BY CYCLE 526 / LIVE.**  It
   splits all 512 reduced-row conflicts algebraically; primitive preparation,
   transformed-output cleanup, and recurrence remain actionable.
4. **Remote parity-ladder routing — UNTESTED / LIVE.**  CNOT fanout chains
   could reduce the 4,067 blank work import while preserving the same ANF.
5. **Shared-bus time-multiplexed routing — UNTESTED / LIVE.**  A restored
   courier could trade M2 count for more bounded compiler phases.
6. **Native dense-transition factorization — UNTESTED / LIVE.**  Factoring
   Cycle 522/526's bounded dense update could transform native controls and
   make output-shadow cleanup exact.
7. **Protected edge-gauge stream — UNTESTED / LIVE.**  Keeping a covariant
   edge shadow through the B layer attacks the separate exterior-stream wall.

Several constructive families remain live.  No broad no-go passes N1.

### N2 — wall-independence audit

The NN preparation route is closed here.  Two collapsed obligations remain
for the stronger full compiler:

- `W_native-dynamics`: a primitive native/shadow transition and transformed
  output cleanup after q-changing coin/seam action;
- `W_recurrent-stream`: simultaneous full-volume exterior streaming with all
  overlapping constraints.

| pair | first closes second? | second closes first? | independent? |
|---|---|---|---|
| `W_native-dynamics` / `W_recurrent-stream` | no | no | yes |

The supplied full microgrid is an explicit resource import, not a third proof
wall.  Sparse resource retirement would improve the construction without
changing its exact routing theorem.

### N3 — hidden-wall scan

The proof uses no “standard QFT,” background parity service, registered
canonical route, or hidden host branch.  The full microgrid, blank preparation,
role coordinates, primitive gate alphabet, size, and color compiler are
listed as supplied.  “Exact,” “nearest-neighbour,” “covariant,” “pre-seam,”
and “inverse” refer to separate executable tests.  The untouched companion's
frame-placement boundary is explicit rather than hidden in “by construction.”

### N4 — residual matching

| witness | witness residual | Cycle-527 residual | match? |
|---|---|---|---|
| Cycle 523 | native-to-shadow nearest-neighbour routing unsynthesized | literal integer NN decoder paths | yes; closed here |
| Cycle 522 | selected native 160-term grammar, primitive recurrence open | same selected rows and same ANF inputs | yes for routing; dynamics still open |
| Cycle 526 | local ANF preparation/routing supplied before joint reduction | same compute-before-seam shadow preparation | yes |
| Cycle 526 | 512 conflicting reduced rows and 18,528 naive endpoint failures | post-reduction diagonal readout | no closure claimed |
| Cycle 231 | exterior B exchange-sign residual | pre-seam local decoder paths | no; distinct residual |

Cycle 231 is not used as evidence against this routing construction.

### N5 — rhetoric audit

| resolution | tested | disposition |
|---|---:|---|
| primitive edge | every emitted two-M2 gate at L5/L6 | periodic integer L1 distance exactly one |
| routed CNOT path | all path lengths used, arbitrary intermediate bits | exact endpoint action and restoration |
| selected local term | all 160 patterns | six shadows exact |
| all cells | L5 and held L6 | 327,360 direction tests, zero failures |
| simultaneous colored lattice | every color and gate layer | zero site clashes |
| proper-cubic orbit | all 24 frames and 576 products | exact path/support closure |
| reduced two-cell ray | inherited Cycle-526 exhaustive census | diagonal endpoint readout fails on all 512 shared rows |
| recurrent full volume | not tested | no negative statement |

“Not a post-reduction diagonal decoder” is restricted to the exact selected
Cycle-526 reduced rows.  It is not broadened to all auxiliary encodings.

### N6 — partial-closure path

Cycle 527 is the executed import-bearing partial closure: take a full blank
microgrid, prove a bounded exact NN theorem, then expose sparse-grid retirement
as an efficiency audit.  Cycle 526 supplies the other constructive path:
prepare persistent endpoint shadows before reduction and transport them with
the seam.  Neither route requires an axiom change.  A sparse embedding,
moving bus, or factorized dense transition could retire current imports by
new construction rather than constitutional language.

### N7 — hostile steelman

A hostile reviewer should reject any claim that Cycle 527 completes the
physical CAR compiler.  Cycle 526 proves that the combined reduced seam does
not carry a diagonal value for its two endpoint occupations: 512 physical
rows support conflicting logical values.  The viable response is not a
no-go, but to compute persistent shadows before reduction, factor the dense
native-plus-shadow transition into physical gates, transport them through all
overlapping seams, and clean them against transformed native outputs.  Cycle
527 supplies only the first primitive preparation router.  That concrete
mechanism leaves a broad obstruction or axiom-pressure claim premature.

### N8 — cross-cycle echo

Cycle 311 introduced the native `f+r` relational shell but left primitive
routing open.  Cycle 522 changed the carrier grammar and recovered exact
local/adjacent separation.  Cycle 523 found the five-monomial selected-term
decoder and decomposed its logical Toffolis, while leaving physical paths
open.  Cycle 526 showed why pre-reduction shadows must persist across the
joint seam.  Cycle 527 now retires the literal NN preparation-path wall with a
large but finite microgrid.  Each advance replaces an import with a bounded
construction; the cross-cycle record supports primitive dynamic factorization,
not axiom pressure.

## Dependency impact and next campaign

| wall | Cycle-527 change | remaining obligation |
|---|---|---|
| `C_ref` | explicit integer origin, scale, role coordinates, and blank grid | retire the large blank-layout import; autonomous preparation |
| `C_num` | six selected-term occupation shadows computed and inverted exactly | transformed-output synchronization through native dynamics |
| `C_wrap` | L5/L6 colored schedules and all frames close | physical event/interval calibration; recurrent general-size proof |
| `C_int` | pre-seam decoder now has literal NN gates | factor native dense coin/seam/contact and clean output shadows |
| `C_local` | major advance: injective integer embedding, support at most two, zero congestion | sparse covariant router and full overlapping-seam recurrence |
| `C_source` | unchanged | source/resource/gravity and realized-history bridge |

The optimal next campaign is not another local decoder.  Combine Cycle 527's
compute-before-seam preparation with Cycle 526's persistent endpoint-shadow
code, then factor the native-plus-shadow transformed update into primitive
gates.  Require exact output cleanup, the 512 shared-row split, all seam
orientations, simultaneous colored recurrence, inverse/leakage/deletions, and
held-size closure before calling the native dynamics synchronized.
