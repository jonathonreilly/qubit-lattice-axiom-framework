# Physical shadow normal-form synchronization — Cycle 530 (2026-07-21)

Authority: none.  Audit: unset.  Constitutional effect: none.

Runner:
`scripts/physical_shadow_normal_form_sync_cycle530_2026_07_21.py`.

## Result

Cycle 530 gives a constructive partial factorization of the transformed-output
synchronization left by Cycles 526 and 527.  Retain all six Cycle-527
occupation shadows on each of the two selected cells.  The resulting twelve
M2 word labels every complete two-cell Fock state.  Let `E_12` be the actual
Cycle-522 selected native encoding with that twelve-bit word attached, and let
`A` put the same word beside one fixed off-code native anchor.  A supplied
dense normal-form unitary `S` is chosen so that

```text
S A = E_12.
```

The physical candidate is

```text
G_candidate = S G_q S^dagger,
S G_q S^dagger E_12 = E_12 G_coarse.
```

Here `S^dagger` removes the old native representative while retaining its
twelve occupation carriers, `G_q` performs the complete selected two-cell
coin–seam–contact update and Cycle-526 event/current/K macro on those
carriers, and `S` prepares the matching transformed native representative.
The old shadows are therefore not erased against changed controls.  They are
the logical carrier through the update and return already synchronized with
the new native code.

`G_q` is compiled here into **1,795 literal nearest-neighbour one-/two-M2
calls** on the Cycle-527 microgrid.  Its inverse is the reversed dagger list.
The exact selected seam is not one endpoint FSWAP.  It is a
**thirteen-FSWAP braid** on the bounded twelve-mode two-cell word.  This braid
reproduces the target occupation and every fermionic phase on all 4,096 Fock
columns for each of the three axes.  A single endpoint FSWAP retains operator
residual 2.

This is not the full primitive physical compiler.  The native normal-form
preparation/unpreparation `S` remains the supplied dense 95-M2 isometry
completion, and the fully installed blank **4,096-M2** microgrid remains a
supplied resource.  Cycle 530 does not relabel either import as a primitive
circuit.

## Strict load-bearing byte pins

Cycles 522, 523, 526, and 527 are executed or read as load-bearing inputs, so
semantic-name checks are insufficient.  The dry contract requires exact byte
equality for all four files, in addition to the older stable dependencies:

| import | load-bearing use | required SHA-256 |
|---|---|---|
| `scripts/physical_opposite_carrier_reearned_compiler_cycle522_2026_07_21.py` | selected encoder and 83-M2 native patch | `d6a7700d7575dfba02d4b4d2438e54d37a02c6ca7f71673c8a871b474f6e088b` |
| `scripts/physical_protected_shadow_coin_gate_compiler_cycle523_2026_07_21.py` | q coin/contact factors and occupation decoder | `d9dd02bbb4dfacebf0f75f6b8c56881ff56653843cb7ed75baa381d5aa605b9d` |
| `scripts/physical_selected_seam_event_current_adapter_cycle526_2026_07_21.py` | persistent-shadow and event/current/K semantics | `7c3d4a35664eaf5c7737c86464ca069e15ce29c40f61778081af8139970c37cd` |
| `scripts/physical_native_shadow_nearest_neighbor_router_cycle527_2026_07_21.py` | literal microgrid placement and initial decoder routes | `2ca2021fa76b889128b587a6a0d67986e236319ea8fb7ccd1dfaf31982c55fa0` |

There is no diagnostic-only or disabled hash gate for these inputs.  Any byte
change fails the Cycle-530 dry test before a science certificate can run.

The selected one-seam construction is exactly repeatable on its declared
code.  A separate simultaneous shared-cell audit also matters: translating
the same local braids to every B seam gives the correct global occupation
permutation but retains 59,880 wrong two-particle phases at L5 and 153,360 at
held L6.  The witness survives twelve tested axis/cell schedule orders.  This
is a route-specific volume failure, not a failure of the one-seam theorem and
not a general local-gauge no-go.  There is no axiom pressure.

## Exact target contract

| field | Cycle-530 contract |
|---|---|
| target statement | Integrate Cycle 527's literal compute-before-seam decoder with Cycle 526's persistent endpoint code and factor transformed-output synchronization as far as the evidence permits. |
| domain | Complete 4,096-column two-cell Fock code; all seam axes and endpoint reversals; L5 and held L6; all 24 proper-cubic frames. |
| allowed premises | Cycle-219 coin, Cycle-230 factor order/contact, Cycle-522 selected encoder, Cycle-526 adapter, Cycle-527 full blank microgrid and initial decoder. |
| forbidden weakenings | No global Jordan–Wigner string, global parity service, host-selected runtime branch, dirty terminal work, dropped fermionic phase, or dense block called primitive. |
| required edge cases | Vacuum/all number sectors, unequal and double-occupied seam endpoints, inverse, leakage, recurrence, deletions, shared-cell order, held size. |
| completion witness | Exact `S G_q S^dagger E_12 = E_12 G_coarse`, literal NN `G_q`, and primitive `S`. |
| what closes here | The selected-seam `G_q` and the exact normal-form synchronization mechanism conditional on supplied `S`. |
| what does not close | Primitive `S`, autonomous blank-grid preparation, simultaneous full-volume B, occurrence/Record/time/source. |

The last row is load bearing.  A target-equivalent primitive physical update
still requires a primitive `S`; an algebraic unitary completion does not count
as that construction.

## Full-shadow code and carrier normal form

Cycle 526 retained only the two seam endpoint bits because they were enough
for its event/current adapter.  Cycle 530 retains the complete pair of local
M64 words:

```text
q = (q_left,0,...,q_left,5,q_right,0,...,q_right,5).
```

For every logical label `ell`,

```text
E_12 |ell> = E_native |ell> tensor |q(ell)>.
```

At both L5 and held L6, `E_12` has 4,096 logical columns, 25,600 nonzero
amplitudes, 25,600 occupied augmented rows, no reused augmented row, and zero
Gram residual.  The complete q word therefore splits the 512 conflicts seen
by Cycle 526 and also provides a direct twelve-mode carrier for the full
logical update.

Because `A` and `E_12` are equal-rank isometries, their mapping extends to an
ambient unitary `S`.  On the code,

```text
S^dagger E_12 = A,
G_q A = A G_coarse,
S G_q S^dagger E_12 = E_12 G_coarse.
```

The same equations give exact inverse and recurrence by induction:

```text
(S G_q S^dagger)^k E_12 = E_12 G_coarse^k.
```

Terminal native/shadow constraint failures and terminal/inverse code leakage
are zero at the algebraic normal-form level.  Deleting the `S` pair and
updating only q leaves the old native carrier correlated with the wrong
logical word; the maximum complete-code column residual is `sqrt(2)`.

This proof does not construct `S`.  Its 95-M2 support consists of Cycle 522's
83-M2 selected seam patch plus twelve q shadows.  The supplied Cycle-522
preparation, its face-sector reference rays, and its off-code completion are
not silently treated as a list of one-/two-M2 gates.

## Why the seam needs thirteen FSWAPs

Use the bounded two-cell mode positions

```text
0,...,5 | 6,...,11.
```

For seam axis `a`, the selected boundary modes occupy positions

```text
p = 2a,
r = 6 + 2a + 1.
```

They are separated by six other local modes.  The exact transposition is the
adjacent braid

```text
FSWAP(p,p+1) ... FSWAP(r-1,r)
FSWAP(r-2,r-1) ... FSWAP(p,p+1).
```

It has seven forward and six return factors.  The first pass moves the left
mode through the local exterior order; the return pass restores every
intermediate mode.  Each double occupation encountered contributes the
FSWAP `-|11>` phase.  Those phases are precisely what a direct endpoint SWAP
misses.

For axes 0, 1, and 2 separately, the runner compares the complete braid with
Cycle 315/522's actual selected exterior seam on all 4,096 columns:

| test | result per axis |
|---|---:|
| target occupation failures | 0 |
| fermionic phase/intertwiner residual | 0 |
| raw maximum residual | 0 |
| naive endpoint-FSWAP operator residual | 2 |
| delete first braid FSWAP | operator residual 2 |

This is a bounded local CAR ordering inside one declared two-cell patch.  It
is not a global ordering of the lattice, a global parity string, or a host
parity callback.  Its failure when naively tiled across the full B matching
is reported separately below rather than hidden.

## Primitive q coin, seam, contact, and event adapter

The Cycle-219 `beta=-0.3` local coin uses the frozen Cycle-523 QR list: ten
fermionic Givens factors and one onsite phase.  Its 64-state reconstruction
residual is `5.0207498326926886e-15`.  The fifteen Cycle-230 pair phases at
`g=0.37` reconstruct contact with residual
`2.149937642474629e-15`.  On the two-cell q word,

```text
G_q,data = contact_left contact_right
           braid_seam
           coin_left coin_right.
```

After conjugating by the logical-label-to-q permutation, the coin, seam,
contact, and composed update each have thresholded operator residual zero.
The composed raw maximum is `1.1102230246251565e-15`.  Thirty-two deterministic
complex-vector two-step recurrence tests have maximum residual
`1.5416528402018934e-15`; inverse tests have maximum
`1.1429443574931856e-15`.

Cycle 526's actual-change macro wraps the complete braid.  It copies the
pre-seam left endpoint to `P,w`, applies all thirteen FSWAP factors, compares
the post-seam endpoint, emits `EDGE_PASSED,J_plus,J_minus`, advances the
16-M2 one-hot K word, and erases `P,w`.  All 65,536 blank-output data-by-K
truth tests pass.  Continuity, one-hot transition, terminal work, Fredkin
decomposition, and two-step fresh-receipt recurrence have zero failures.
`EDGE_PASSED` remains an event-ready coherent carrier.  It is not occurrence,
a Record, an interval, a rate, or physical time.

## Literal nearest-neighbour schedule

The full Cycle-527 `16 x 16 x 16` integer microgrid is retained.  All native
roles and twelve q endpoints keep their Cycle-527 coordinates.  Twenty-one
blank sites host `P,w,EDGE_PASSED,J_plus,J_minus` and the sixteen K rails.

Every fermionic two-mode core is routed along a path whose intermediate M2
sites are blank.  FSWAP transport moves one fermionic carrier to the core and
reverses the path afterward.  Every CNOT in the event/current/K macro and in
the exact Toffoli/Fredkin decompositions is routed with ordinary tensor-factor
SWAP and reversed, so arbitrary intermediate wire states are restored.  The
two transports are not conflated:

```text
FSWAP |11> = -|11>,
ordinary SWAP |11> = +|11>.
```

The L5 and held-L6 compiled schedules have identical resource counts:

| item | each size |
|---|---:|
| physical one-/two-M2 calls | 1,795 |
| calls including inverse | 3,590 |
| fermionic blank-path macros | 63 |
| maximum blank path | 24 physical edges |
| FSWAP route calls | 978 |
| ordinary SWAP route calls | 458 |
| two-M2 CNOT cores | 139 |
| fermionic Givens cores | 20 |
| braid FSWAP cores | 13 |
| contact cores | 30 |
| one-M2 phase/H/T/T-dagger/X calls | 157 |
| non-nearest-neighbour calls | 0 |
| blank-path failures | 0 |
| maximum uses of one physical edge | 104 |

The canonical L5 digest is
`0b8cc0f36528e82636ec5167f40370ffb4d00d96fb6faf7268d640744a6d8265`;
held L6 is
`baff9541179c2c85cffb78eea5d81b6db71b45de69f42f567397766e2f1a82cb`.
The inverse is the reverse dagger list, not a host-side inverse oracle.

Cycle 527's initial compute-before-seam decoder remains literal: 1,338 NN
calls per cell compute all six q bits and the same count uncomputes them when
their controls are unchanged.  Cycle 530 does not use that old uncompute after
native controls change.  It enters the normal form before the update and
reprepares the matching output code instead.

## Proper-cubic covariance and orientations

The three axis braids are exact separately.  Under the 24 proper-cubic frames,
the canonical positive-x seam maps four times to each of the six oriented
directions.  Rotating every literal coordinate maps each primitive edge to a
nearest-neighbour edge and each blank fermionic corridor to a blank corridor.
Both sizes have:

- zero frame nearest-neighbour failures;
- zero frame blank-path failures;
- zero Cycle-526 endpoint/shadow/current covariance failures;
- twelve endpoint-preserving and twelve endpoint-reversing frames; and
- zero failures in all 576 frame products.

The covariance certificate is a **24-member schedule orbit**: map the
canonical physical list at compile time for each proper-cubic frame, then use
the corresponding frozen list.  Those mapped physical schedules inherit the
logical product covariance and close on all 576 products.  No runtime frame
query is used.  Cycle 530 does **not** claim one frame-independent gate
ordering whose literal ordered list is identical in all frames.  The local
twelve-position exterior convention and its frame cocycle are supplied code
conventions, not a lattice-wide Jordan–Wigner service.

## Mass, contact, inverse, leakage, and deletion controls

The data-only q update preserves the Cycle-219 mass fixture:

```text
Cycle-219 mass             0.4534056541748851
Cycle-530 q-core mass      0.4534056541748850
one-particle residual      8.7159799596118e-16
```

The Cycle-230 contact retains exactly **4,047** nontrivial two-cell columns.
Appending event/current/K outputs generally entangles the one-particle ray;
that larger carrier is not claimed as a new mass eigenfixture.

Load-bearing controls include:

- deleting the `S` pair gives maximum native/q code-column residual `sqrt(2)`;
- replacing the thirteen-factor seam by endpoint FSWAP gives norm 2;
- deleting the first braid FSWAP gives norm 2;
- deleting the first coin or contact factor gives a nonzero reconstruction
  residual;
- every routed FSWAP corridor starts with blank intermediates and reverses;
- `P,w` return blank on every complete-Fock/K test;
- `S G_q S^dagger` and its adjoint preserve the code exactly, conditional on
  the supplied unitary `S`; and
- all invalid claims of primitive `S` remain false in the machine output.

## Shared-cell and full-B audit

A one-seam factor is not automatically a simultaneous B compiler.  Cycle 530
translates the same two-cell braid to every positive-axis seam, orders axes
`x,y,z` and cells lexicographically, and performs the complete vacuum/N=1/N=2
comparison with the exterior lift of the resulting full matching.  The
occupation permutation is always correct, but the phases are not:

| size | two-particle pairs | wrong phases | target failures |
|---:|---:|---:|---:|
| L5 | 280,875 | 59,880 | 0 |
| held L6 | 839,160 | 153,360 | 0 |

The first witness occupies directions 0 and 1 of the same cell.  The tiled
braids give phase `-1`; the exterior matching gives `+1`, an exact
basis-vector residual 2.  The same witness survives all six axis orders with
both lexicographic and reverse-lexicographic cell order, twelve schedule
families at each size.

This is a sharper result than the old endpoint product because one selected
seam is now exact.  It also distinguishes two obligations:

1. selected two-cell transformed-output synchronization, exact here
   conditional on `S`; and
2. a simultaneous shared-cell/full-volume B representation, still open.

The finite order audit does not exclude a correlated link code, a stateful
gauge transition, a higher-form carrier, or a different bounded braid whose
shared-cell action is not this translated construction.

## Supplied structure and novelty boundary

| item | status in Cycle 530 |
|---|---|
| Cycle-219 coin coefficients and mass fixture | supplied retained physics fixture |
| Cycle-230 contact coupling, factor order, and CAR seam target | supplied retained physics fixture |
| Cycle-522 83-M2 selected native encoder and preparation | supplied dense representation |
| Cycle-526 two-endpoint augmented code and event/current/K semantics | supplied algebraic bridge, integrated here |
| Cycle-527 twelve-shadow NN compute-before-seam router | supplied previously synthesized primitive schedule |
| Cycle-527 fully installed blank 4,096-M2 cell | supplied resource/preparation import |
| twelve-shadow `E_12` code and carrier-normal-form reduction | constructed and checked here |
| normal-form `S` ambient unitary completion | supplied dense import; not primitive-factorized |
| Cycle-523 q coin factor list for the Cycle-219 coefficients | supplied previously synthesized list; integrated and physically routed here |
| thirteen-FSWAP selected seam | new construction and exhaustive exact certificate |
| Cycle-523 q contact factors and Cycle-526 event/current/K logic | supplied previously synthesized lists; integrated and physically routed here |
| literal NN 1,795-call `G_q` schedule and inverse | constructed here |
| simultaneous translated-braid B | attempted and falsified on N=2 |
| physical duration, energy, Record, source, gravity | neither supplied nor inferred |

Generic adjacent-transposition decompositions, QR/Givens compilation,
Toffoli/Fredkin identities, and SWAP routing are standard compiler machinery;
they are not claimed as new physics.  The new physics-facing result is the
exact match between this bounded thirteen-FSWAP carrier braid and the actual
selected seam, together with the normal-form synchronization reduction and
its explicitly isolated dense import.

## Approach-family registry

| family | object / mechanism | terminal obligation | strength | status |
|---|---|---|---|---|
| carrier normal form | full twelve-shadow code; `S G_q S^dagger` | primitive `G_q` plus primitive `S` | target-equivalent | provisional: `G_q` complete, `S` open |
| endpoint FSWAP | two endpoint q M2 only | match full selected exterior phase | weaker | retired: norm 2 |
| bounded two-cell braid | thirteen adjacent local FSWAPs | exact one-seam CAR action | weaker than full volume | candidate-complete for selected seam |
| tiled local braid | translated two-cell braids with colored/order schedule | full simultaneous B exterior action | target-equivalent for B | blocked-local: exact phase witness |
| correlated/stateful link | live gauge sector changed by B | constraint-preserving recurrent B isometry | target-equivalent | unexplored/live |
| distributed prefix/higher-form | locally constrained parity field | fixed-depth preparation/recode and B action | target-equivalent | provisional/live after Cycle 528 |
| direct native preparation compiler | Cycle-522 stabilizer/ray isometry | literal one-/two-M2 `S` and inverse | target-equivalent | unexplored/live |

The selected-braid result does not upgrade either target-equivalent open row to
“routine.”

## N1–N8 no-go discipline

Gate status for a full-compiler impossibility, minimum-resource claim, or
axiom-pressure claim: **FAIL / DO NOT SHIP**.  Cycle 530 retains the exact
translated-braid counterexample only for that route and reports a constructive
partial closure.

### N1 — alternative-route map

1. **Twelve-shadow carrier normal form — ATTEMPTED / POSITIVE PARTIAL.**
   `S G_q S^dagger` solves transformed synchronization exactly; primitive `S`
   remains the terminal obligation.
2. **Single endpoint FSWAP — ATTEMPTED / RETIRED.**  It gets the endpoint
   occupation right but misses complete-Fock phases with operator residual 2.
3. **Thirteen-FSWAP bounded braid — ATTEMPTED / POSITIVE ONE SEAM.**  It is
   exact on all 4,096 columns for all axes and has a literal NN route.
4. **Translated simultaneous braids — ATTEMPTED / BLOCKED FOR THIS
   SCHEDULE FAMILY.**  The complete L5/L6 N=2 census gives the stated
   59,880/153,360 phase mismatches.
5. **Correlated or non-diagonal link gauge — OPEN.**  Cycle 528's exact
   one-link comparator provides an actionable seed, but no recurrent shared-
   cell transition has been tested.
6. **Distributed prefix or higher-form code — OPEN.**  Cycle 528 localizes
   the runtime phase but leaves fixed-depth preparation/recode open.
7. **Direct stabilizer/ray preparation compiler for `S` — OPEN.**  A Clifford
   preparation of face reference rays plus controlled selected amplitudes
   could retire the sole dense normal-form import.

Several materially distinct routes remain live, so a broad no-go fails N1.

### N2 — wall-independence audit

The collapsed primitive wall set has two members:

- `W_S`: synthesize the 95-M2 native carrier-normal-form preparation and
  inverse with local one-/two-M2 primitives;
- `W_volume`: replace the failing translated braid by a simultaneous
  shared-cell/full-volume B representation.

| pair | first closes second? | second closes first? | independent? |
|---|---:|---:|---:|
| `W_S`, `W_volume` | no | no | yes |

The old “coin shadow update,” “contact shadow update,” and “transformed-output
cleanup” labels collapse into `W_S` after the exact `G_q` construction; they
are not counted as three independent walls.  History formation, metric time,
and source/gravity remain downstream TOE lanes, not extra compiler walls in
this target.

### N3 — hidden-wall scan

The selected encoder, face-sector reference rays, normal-form unitary `S`,
off-code completion, full blank microgrid, blank corridor preparation,
compile-time q order, primitive gate alphabet, factor order, coefficients,
finite seam, and adapter auxiliaries are explicit.  “Exact” is separated into
code-image, phase, path, inverse, and leakage tests.  “Physical” means literal
M2 locations and gates for `G_q`; it does not describe `S`.  The words “by
construction,” “standard QFT,” “obviously,” and “the framework provides” are
not used to discharge a proof obligation.  The two “canonical” hits name the
frozen L5 schedule digest and the positive-x representative whose complete
proper-cubic orbit is tested; they are explicit indexing conventions rather
than hidden dynamics.  The trigger words in this paragraph are the scan's own
reported strings and are non-load-bearing.

### N4 — residual matching

| witness | witness residual | Cycle-530 residual | match? |
|---|---|---|---:|
| Cycle 522 | selected 83-M2 encoder and dense recurrent completion | same selected encoder; primitive preparation remains | yes |
| Cycle 523 | exact q coin/contact and local decoder, direct B norm 2 | same q carrier and same direct endpoint-B sign residual | yes |
| Cycle 526 | persistent endpoint code; dense transformed-output completions | full twelve-shadow extension and normal-form update | yes for synchronization target |
| Cycle 527 | literal NN pre-seam q preparation | same initial twelve-shadow schedule | yes |
| Cycle 528 | product/local response fails simultaneous B; correlated routes open | translated-braid volume audit | yes for volume boundary; not evidence against selected seam |
| Cycle 219 | one-particle mass fixture | data-only q update mass | yes |
| Cycle 230 | selected seam/contact block | q braid/contact target | yes |

Cycle 528's global result is not cited against primitive `S`; those residuals
do not match.

### N5 — rhetoric audit

| resolution | tested | disposition |
|---|---:|---|
| one adjacent physical edge | every emitted two-M2 `G_q` call | exact periodic L1 distance one |
| one routed fermionic core | all 63 blank paths | blank intermediates and exact reverse transport |
| one selected two-cell seam | all 4,096 Fock columns, three axes | exact occupations and phases |
| repeated same-seam data code | algebraic all-k identity plus two-step vectors | exact conditional on `S` |
| simultaneous translated B | complete vacuum/N=1/N=2 at L5/L6 | fails this route with named counts |
| arbitrary full-Fock volume | not tested | no negative statement |
| correlated/stateful gauge | not tested | explicitly live |

Thus “not a simultaneous B compiler” names only this translated-braid family;
it is not widened to “local information cannot compile B.”

### N6 — partial-closure path

Cycle 530 follows the legitimate import-bearing form: retain the explicit
dense `S`, prove an exact bounded `G_q` theorem, and isolate primitive `S` as
the import-retirement audit.  A stabilizer/ray state-preparation circuit can
attack `S` without an axiom edit.  Independently, a correlated link or
higher-form carrier can replace only the failing simultaneous B layer.  The
4,096-M2 grid can later be sparsified without changing the one-seam algebra.

### N7 — hostile steelman

A hostile reviewer should reject any claim that the transformed-output wall
or physical CAR compiler is closed: the displayed intertwiner begins and ends
with an unsynthesized 95-M2 unitary `S`, which is exactly where the selected
native face-sector amplitudes enter.  Moreover, the local braid's success on
one edge does not survive shared-cell tiling.  The strongest constructive
counter-route is to synthesize `S` from the Cycle-522 stabilizer references and
selected branch amplitudes while a correlated link sector supplies the global
B cocycle.  Cycle 527 proves the grid can route bounded circuits, and Cycle
528 proves live auxiliary state can repair one link, so neither terminal
obligation is foreclosed.  A broad no-go or axiom claim would therefore be
premature.

### N8 — cross-cycle echo

Cycle 311 replaced a common-M64 mismatch with relational native roles.  Cycle
522 replaced the old carrier grammar and recovered an exact selected dense
seam.  Cycle 523 replaced an abstract occupation observable by a five-monomial
decoder and primitive q coin/contact.  Cycle 526 replaced a host event input
with persistent endpoint shadows and actual pre/post change.  Cycle 527
replaced nonlocal decoder calls by literal NN paths.  Cycle 528 replaced one
link's abstract sign comparison by a live constrained carrier while exposing
the global product failure.  Cycle 530 now replaces the monolithic augmented
coin/contact synchronization import by one explicit primitive q core plus one
named normal-form isometry.  This repeated import-retirement pattern argues
for attacking `S` and shared-cell B constructively, not for axiom pressure.

## Dependency impact and next campaign

| wall | Cycle-530 change | remaining obligation |
|---|---|---|
| `C_ref` | the twelve-shadow normal form and local exterior order are explicit | derive/retire the selected native preparation and local-order convention |
| `C_num` | all 4,096 columns and exact q phases are checked | primitive preparation coefficients and error/precision theorem |
| `C_wrap` | repeatable same-seam code update and all frames close | simultaneous full-volume B and any physical interval calibration |
| `C_int` | major advance: coin, selected seam, contact, event/current are literal NN q gates | primitive `S`; correlated shared-cell B |
| `C_local` | major advance: 1,795-call NN `G_q`, inverse, blank routes, all orientations | sparse grid retirement and full-volume schedule |
| `C_source` | unchanged | lawful energy/stress source, response, gravity, realized-history bridge |

The optimal next campaign is a direct primitive compiler for `S`: expose the
Cycle-522 face stabilizer reference state and its selected branch amplitudes,
factor their preparation/unpreparation into local Clifford plus controlled
amplitude gates, route them on the existing grid, and test the exact
`S G_q S^dagger` code image.  In parallel only after that concrete core, reopen
the simultaneous B lane with a correlated/stateful link transition rather
than another product endpoint phase.
