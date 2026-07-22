# Physical local N3 six-ray decoder tournament — Cycle 557

Date: 2026-07-21
Authority: none
Audit: unset
Constitutional effect: none

Companion runner:

`scripts/physical_local_N3_six_ray_decoder_tournament_cycle557_2026_07_21.py`

## Result

Cycle 557 closes the first local six-ray boundary left by Cycle 555, using two
independent constructive routes.  It does not close a global `N=3` network.

The declared one-cell space contains all 42 six-mode CAR words with `N<=3`.
There are 116 selected physical rays:

| local ray count | words | contribution |
|---:|---:|---:|
| 2 | 34 | 68 |
| 6 | 8 | 48 |
| **total** | **42** | **116** |

The eight six-ray words are decimal words `21, 22, 25, 26, 37, 38, 41, 42`.
The exact tournament disposition is:

| route | branch object | one-cell inverse | adjacent two-cell complete `N<=3` | disposition |
|---|---|---:|---:|---|
| Route A | existing flag plus companion M2 | no | not widened | fails only as the declared two-pivot decoder |
| Route B | six-M2 one-hot block per cell | exact | exact | bounded constructive comparator |
| Route C | one three-M2 binary slot, returned and reused | exact | exact | **strongest tested constructive route** |

Route A sees only the correlated patterns `00` and `11` on every six-ray
word.  It therefore has 32 decoder collisions: four missing labels for each
of eight words.  That is a finite-table failure of these two existing roles,
not a failure of larger local role subsets, one-hot blocks, reused slots, a
global network construction, or the M2 substrate.

Routes B and C use the full bounded physical pattern of the selected
representative.  Within each supplied q word all ray patterns are distinct.
The finite census finds that the 34 two-ray words need one word-conditioned
native role and each six-ray word needs five; the latter is an exact subset
census for this table, not a minimum-content claim about admissible physics.
There are no physical-pattern decoder collisions at L3 or held L4.

Route C then advances to an adjacent two-cell seam patch with 12 CAR modes and
the complete total `N<=3` domain:

| total number | columns |
|---:|---:|
| 0 | 1 |
| 1 | 12 |
| 2 | 66 |
| 3 | 220 |
| **total** | **299** |

Those columns expand to **1,324** physical product rows: 283 columns have four
rays and 16 have twelve.  After the first selected cell factor has acted, the
joint current physical pattern still determines the second cell's slot value
with zero conflicts.  The same three-M2 slot therefore returns to `000` after
cell 0, is reused, and returns to `000` after cell 1.  No previous-branch,
sector, parity, frame, or schedule query is made by a host.

This is a bounded one-/two-cell compiler result with constant overhead per
coarse cell.  It is not yet a complete-network `N<=3` theorem, an arbitrary-
size recurrence theorem, or a new physical law.

## Exact encoder identity

For a supplied local q word `w`, let `a_w,s` be the strict-pinned selected
coefficient and `P_w,s` its actual physical M2 Pauli representative.  Route C
uses a three-M2 slot and the exact finite sequence

```text
A_w |000> = sum_s a_w,s |s>,                 s in {0,...,r_w-1}
SELECT_w   = sum_s |s><s| tensor P_w,s,
D_w        = bounded (q word, physical pattern)-controlled XOR of s,
W_w        = D_w SELECT_w A_w.
```

The two unused values `110` and `111` are rejected by a local three-M2
validity predicate.  The physical-pattern table is injective within every q
word, so

```text
W_w |w>|Omega_fixed>|000>
  = |w> sum_s a_w,s P_w,s|Omega_fixed> |000>.
```

Route B realizes the same map in the one-excitation subspace of six branch
M2.  One X initializes rail zero, exact pairwise Givens rotations prepare the
one-hot amplitudes, selected Pauli factors act under the active rail, and the
physical decoder flips that rail back to the all-zero blank.

For the adjacent patch, the literal Route-C cell program is:

1. locally check slot blank/valid;
2. prepare the slot from the persistent cell q word;
3. apply the slot-selected physical Pauli factors;
4. XOR the slot from q plus the current bounded physical pattern;
5. locally check returned blank and reuse the same slot for the next cell.

For cell 0 the decoder has 116 local rows.  For cell 1 it uses the 1,324-row
joint bounded-patch table because cell 0 has already acted.  This table is
large but constant for the declared two-cell block.  It is not an unbounded
lookup, global parity service, global Jordan-Wigner ordering, or nonlocal
host callback.

On the declared code space, persistent q labels make distinct logical columns
orthogonal; the branch preparations are normalized; SELECT and the XOR
decoder are reversible.  Thus exact Gram error, inverse error, and terminal
branch/slot leakage are zero algebraically.  The zero is supported by the
independent preparation, pattern-injectivity, constraint, routing, covariance,
and deletion tests below; it is not presented as independent evidence for
the supplied selected table.

Cycle 557 does not materialize a new global `N<=3` free-plus-contact update.
It establishes the missing local encoder/inverse required before that test.
The existing Cycle-555 complete-network `N<=2` identity
`E G_coarse = G_physical E` remains the strongest complete-network update
result.  The local mass, contact, and seam fixtures are replayed here to show
that widening the branch decoder does not replace those physical ingredients.

## Route A — two companion/flag pivots

The declared Route-A hypothesis was that the already present flag and
companion roles could label all six rays.  Exhaustive L3 and held-L4 tables
give the same result:

```text
six-ray flag/companion patterns = {00, 11}
unique patterns per six-ray word = 2
required ray labels              = 6
collisions                       = 8 * (6 - 2) = 32
```

A two-bit system can in principle carry four labels, but the actual selected
representatives occupy only two here.  Route A is stopped before patch
widening because it lacks an exact one-cell inverse.  No impossibility beyond
this exact flag/companion decoder is inferred.

## Route B — bounded one-hot block

Route B assigns six physical M2 to a one-hot ray block for each coarse cell.
For two-ray words only the first two rails participate; for six-ray words all
six do.  The local number-one constraint is a bounded six-M2 predicate.  The
decoder returns the entire block to its all-zero blank, so the constraint
type changes explicitly from number one during selection to number zero at
the terminal rather than being hidden.

| one-cell control | L3 | held L4 |
|---|---:|---:|
| branch M2 | 6 | 6 |
| q-controlled one-excitation Givens | 74 | 74 |
| decoder rows | 116 | 116 |
| decoder collisions | 0 | 0 |
| maximum preparation residual | `1.5700924586837752e-16` | same |
| maximum inverse residual | `2.4196749845665633e-16` | same |
| deleted-first-Givens residual | `0.41744238123296284` | same |
| deleted-one-decoder-row residual | `0.408248290463863` | same |
| terminal branch leakage | 0 | 0 |

On the adjacent patch Route B uses twelve branch M2, two local number-one
constraints, and a joint 1,324-row physical decoder.  Its 2,648 active-rail
XOR calls have zero label collisions, exact inverse, and zero terminal
leakage.  Deleting a joint decoder row leaves residual at least
`0.28867513459481287`.

## Route C — transported and reused three-M2 slot

Route C binary-encodes the six possible ray labels in three physical M2.  Its
two unused bit strings are locally rejected.  Exact two-level Givens are
expanded through inherited Gray-path controlled one-/two-M2 macros.  The
preparation counts and residuals equal Route B's because they encode the same
coefficient vectors.

On the patch there is one slot allocation, not one per cell.  The first local
decoder uses 90 multi-controlled-X activations.  The second joint decoder uses
726, with at most 38 equality controls: twelve persistent q M2 plus 26 joint
native physical roles.  The controls, clean conjunction work, slot, and
selected physical roles all lie in the bounded two-cell compiler block.

The current joint pattern plus current q word determines the second slot
label with zero conflicts over all 1,324 rows.  It does not consult or retain
the previous branch label.  Both terminal slot leakage and invalid-value
leakage are zero.  This is the strongest tested result because the same three
M2 are returned and reused while Route B retains six branch M2 per cell.
No claim is made that three M2 is resource-minimal among all encodings.

## Local constraints and lawful domain

Every selected representative for every local `N<=3` word in both patch cells
is tested against all Cycle-269 port constraints, inherited local checks, and
fixed-Wilson-sector checks:

| audit | L3 | held L4 |
|---|---:|---:|
| selected entries | 232 | 232 |
| local role-pair failures | 0 | 0 |
| port commutator cases | 37,584 | 89,088 |
| port commutator failures | 0 | 0 |
| fixed-check cases | 69,600 | 164,024 |
| fixed-sector failures | 0 | 0 |

Auxiliary constraints are locally enforced as bounded block predicates: Route
B checks one excitation within each six-M2 block; Route C rejects slot values
6 and 7 within its three-M2 block and checks `000` before reuse.  These checks
do not provide physical energy, an autonomous penalty law, blank genesis, or
error correction.  They declare and verify the code space.

The lawful-domain restriction is complete total `N<=3` on one cell and the
named adjacent two-cell patch.  The persistent q word is supplied.  No global
number counter is invoked in this bounded test, and there is no parity or
Jordan-Wigner service.

## Literal locality and proper-cubic covariance

The adjacent patch uses 81 actual selected/reference physical M2 and twelve
persistent q M2.  Route B adds twelve branch and 36 reused conjunction-work
M2, for 141 compiler-live M2.  Route C adds three slot and 36 reused work M2,
for 132.  These counts are identical at L3 and held L4.

Every required logical pair is conservatively covered by an explicit
deterministic periodic Manhattan route: 9,870 universal pair routes for Route
B and 8,646 for Route C.  Every route edge is nearest-neighbour, each remote
macro reverses its route, and all route-edge failures are zero.  The maximum
base-chart path is 48 edges.

The actual wires and route edges are transported through all 24 proper-cubic
frames.  Mapped-wire injection and mapped nearest-neighbour failures are zero.
All 576 frame products close with zero group failures.  Separately, the
strict-pinned selected-shell covariance test is replayed at L3 and held L4:
physical branch, selector, normalization-orbit, and group failures are zero;
the largest coin/composition residual is `1.5574068580638927e-15`.

This is covariance of a transported circuit family.  The base-chart cell
program and factor order are mapped, not rediscovered by a runtime selector.
That compile-time presentation remains supplied.  **No schedule is time.**

## Mass, contact, seam, inverse, leakage, and deletions

The strict inherited fixtures remain green:

- Cycle-219 rest-mass source: `0.4534056541748851`;
- compiled rest mass: `0.453405654174885`;
- uniform one-particle residual: `8.7159799596118e-16`;
- Cycle-230 contact factorization residual: `2.149937642474629e-15`;
- nontrivial contact columns: 4,047; and
- all three axis-seam braid residuals: exactly zero over 4,096 complete Fock
  columns per axis.

The event-current adapter also replays 65,536 blank-output tests with zero
truth, continuity, terminal-work, recurrence, and Fredkin-basis failures.  It
is retained only under its existing scope; returning a compiler slot is not
called a Record.

Load-bearing deletions are distinct:

- deleting the first preparation Givens changes a one-cell ray by at least
  `0.41744238123296284`;
- deleting one one-cell decoder row leaves at least one slot/branch component
  with norm `0.408248290463863`;
- deleting one joint patch decoder row leaves residual at least
  `0.28867513459481287`;
- the inherited naive endpoint seam and deleted-first-FSWAP controls remain
  near residual 2; and
- reversing every routed remote macro is required to avoid route-work
  leakage.

Terminal branch/slot, validity, conjunction, and reversed-route leakage is
zero on the declared code space.  The exact zero follows algebraically from
the exhaustive decoder truth table and reversible gates; the nonzero deletion
tests show that the decoder and preparation rows are load bearing.

## Materialization, supplies, and novelty boundary

Materialized here are all 42 one-cell coefficient vectors, their 74 Givens
schedules, all 116 selected representatives and physical patterns, all 299
patch logical labels, all 1,324 joint ray patterns and phases, the one-hot and
binary decoder tables, all literal M2 coordinate assignments, and every
universal pair route.  Equality-controlled Givens, controlled Pauli factors,
clean conjunctions, exact Toffoli reductions, and route/reverse-route cores
use the hash-pinned exact inherited one-/two-M2 macro expansions.  The full
dense physical update matrix and arbitrary off-code completion are not
materialized.

Supplied rather than derived are:

1. the fixed-Wilson reference and its preparation;
2. blank branch/slot, conjunction, and route M2;
3. persistent q input and the complete `N<=3` cutoff;
4. strict-pinned selected coefficients, physical Pauli representatives, and
   exact analog Givens/physics angles;
5. the named one-cell and adjacent two-cell addresses;
6. the cell-factor and cell-program order;
7. finite L3/L4 periodic boundaries, base chart, router, and compile-time
   proper-cubic frame; and
8. the existing mass, contact, seam, and event-current fixtures.

New here are the explicit three-route six-ray census, the exact finite Route-A
collision witness, Route-B six-M2 one-hot decoder, Route-C three-M2 returned
slot decoder, complete adjacent-patch `N<=3` product census, post-first-cell
joint-pattern inverse, local validity checks, L3/held-L4 literal layouts, and
deletion sensitivities.

The result is not a global `N<=3` compiler, arbitrary-size theorem, reference
or blank genesis theorem, order-independence theorem, autonomous causal law,
time, duration, energy, rate, realized history, Record theorem, Born rule,
gravity/source response, minimum-content theorem, axiom, or no-go.  Wrapped
phase is not called physical energy and a generator element is not called a
rate.  Thirring machinery is neither used nor compared.

## Dependency ledger and maturity

- `C_ref`: unchanged.  Reference preparation, blanks, q input, selected table,
  exact angles, addresses, program order, finite frame, and router are supplied.
- `C_num`: advances from global `N<=2` to exact bounded one-/two-cell complete
  `N<=3` encoding only.  A complete network, number change, and all sectors
  remain open.
- `C_wrap`: unchanged.  The two cell programs and returned-slot sequence are a
  compiler presentation; no schedule is time or realized history.
- `C_int`: preserved.  The mass, contact, and all-axis seam fixtures remain
  exact behind the same strict-selected representatives, but no new global
  `N<=3` free-plus-contact recurrence is claimed.
- `C_local`: advances.  The first six-ray local inverse and an adjacent-seam
  extension close constructively by Routes B and C.
- `C_source`: unchanged.

No five-lane maturity score changes are proposed: operational quantum/records
`3.4/5`, causal time `1.8/5`, inertia/matter `4.2/5`, gravity/source `2.1/5`,
and Born/probability `2.0/5`.  This is a bounded compiler-sector advance, not a
cross-lane closure.  There is no shared substrate obstruction and **no axiom
pressure**.

## No-go discipline N1–N8

The refreshed `origin/main` no-go-discipline skill and proof-search governance
were applied.  Broad impossibility, minimum-content, and axiom-pressure gate:
**FAIL / DO NOT SHIP**.  Two constructive routes succeed and several scalable
extensions remain open.

### N1 — alternative-route normalization

| family | object / mechanism / terminal | disposition |
|---|---|---|
| Route A companion/flag | existing two roles / two-bit pattern / erase six-ray label | **ATTEMPTED: fails only as declared** |
| Route B one-hot | six-M2 block / one-excitation Givens plus joint decoder / exact blank return | **ATTEMPTED: succeeds** |
| Route C reused slot | three-M2 block / binary Givens plus current-pattern decoder / exact per-cell return | **ATTEMPTED: succeeds; strongest tested** |
| larger native-role subset | selected physical pattern / word-conditioned reversible lookup / local erasure | **partial: injective census; circuit subsumed by B/C** |
| three-cell/network slot rail | one transported slot / bounded rolling joint inverse / scalable recurrence | **open** |
| direct rough-carrier compiler | target-times-gauge code / local preparation and transduction / recurrent network | **partial; bridge open** |
| stabilization/reset | local checks / prepare reference and renew blanks / convergence | **open** |

These families use different branch objects and terminal mechanisms.  Route
A's collision cannot be transferred to B, C, a larger relational decoder, or
the rough-carrier family.

### N2 — wall-independence audit

The residual walls are:

```text
W_network  complete-network N<=3 scaling and returned-slot recurrence,
W_ref      fixed-reference genesis,
W_blank    blank-work genesis and renewal,
W_order    retirement of compile-time factor/program order,
W_auto     autonomous causal update choice,
W_bridge   selected-carrier <-> rough-carrier transduction.
```

| pair | first closes second? | second closes first? | independent? |
|---|---:|---:|---:|
| `W_network,W_ref` | no | no | yes |
| `W_network,W_blank` | no | no | yes |
| `W_network,W_order` | no | no | yes |
| `W_network,W_auto` | no | no | yes |
| `W_network,W_bridge` | no | no | yes |
| `W_ref,W_blank` | no | no | yes |
| `W_ref,W_order` | no | no | yes |
| `W_ref,W_auto` | no | no | yes |
| `W_ref,W_bridge` | no | no | yes |
| `W_blank,W_order` | no | no | yes |
| `W_blank,W_auto` | no | no | yes |
| `W_blank,W_bridge` | no | no | yes |
| `W_order,W_auto` | no | no | yes |
| `W_order,W_bridge` | no | no | yes |
| `W_auto,W_bridge` | no | no | yes |

Closing a bounded ray-label inverse does not prepare the reference or blanks,
retire presentation order, choose updates autonomously, or create a carrier
bridge.  Conversely none of those walls supplies a scalable `N<=3` inverse.

### N3 — hidden-wall scan

Fixed reference, blank auxiliary M2, persistent q input, selected coefficient
table, exact angles, `N<=3` cutoff, addresses, cell-factor and program order,
finite sizes, chart, router, frame, and carrier are explicit.  The 1,324-row
second-cell decoder is named rather than hidden under “locality.”  “Physical”
means an M2 placement with nearest-neighbour macro routes; it does not mean
initialized, autonomous, or experimentally realized.

### N4 — residual matching

| witness | exact source | residual attacked | Cycle-557 use | match? |
|---|---|---|---|---:|
| Cycle 555 six-ray boundary | `PHYSICAL_GLOBAL_SELECTED_NETWORK_ENCODER_CYCLE555_NOTE_2026-07-21.md`, N6 | local `N=3` branch erasure | exact tournament terminal | yes |
| Cycle 533 joint decoder | `physical_selected_seam_code_space_isometry_compiler_cycle533_2026_07_21.py:shared_decoder_controls` | one-cell inverse after a product | bounded second-cell joint lookup | yes |
| Cycle 533 selected-shell covariance | `physical_selected_seam_code_space_isometry_compiler_cycle533_2026_07_21.py:covariance_controls` | physical selected family under frames | replayed all-24/576 check | yes |
| Cycle 555 global N2 intertwiner | `physical_global_selected_network_encoder_cycle555_2026_07_21.py:certificate` | complete-network update | retained boundary only | no for global N3; dropped as proof |
| Cycle 532 rough quotient | `physical_rough_gauge_subsystem_quotient_cycle532_2026_07_21.py:covariance_controls` | rough target covariance | selected-to-rough bridge | no; dropped as bridge evidence |

The local decoder witness matches the local terminal.  Neither local success
nor inherited global `N<=2` recurrence is used to claim global `N<=3` closure.

### N5 — rhetoric audit

| resolution | tested statement |
|---|---|
| one ray | actual strict-pinned amplitude and Pauli pattern |
| one word | exact two- or six-ray preparation and erasure |
| one cell | all 42 words and 116 rays |
| adjacent two-cell patch | all 299 total-`N<=3` columns and 1,324 rows |
| held size | same bounded patch on L4 |
| all frames | transported selected shell, wires, and routes through 24/576 |
| complete network `N<=3` | not tested; open |
| autonomous update law | not tested; program order is not time |

“No parity” and “no Jordan-Wigner ordering” are scoped to the encoders actually
tested.  The supplied cell program order is still named.

### N6 — partial-closure path

Retain Route C and test one three-cell path with the same returned slot.  The
third decoder must depend only on the persistent q words and the current
bounded physical pattern after two cells, not retained branch history.  If
that exact inverse closes, widen to the smallest complete periodic `N<=3`
network using a bounded rolling decoder or a provable local pivot rule.  Route
B remains an independent exact comparator.  Reference/order/autonomy/bridge
campaigns can proceed separately.

### N7 — hostile steelman

> A hostile reviewer should reject “global N3 physical compiler.”  The
> strongest decoder after the first cell is a supplied 1,324-row lookup over a
> named two-cell block; the reference, blank slot, q input, coefficient table,
> exact angles, addresses, order, finite boundaries, and frame are supplied.
> The result neither derives the coarse law nor materializes a new global
> free-plus-contact update.  But the same evidence defeats a no-go: two
> independent bounded encodings erase all six-ray labels exactly, the slot is
> reused once, and a three-cell rolling test is concrete and falsifiable.

### N8 — cross-cycle echo

Cycles 319/324 replaced incompatible independent roles with joint roles or
slots.  Cycle 533 replaced an invariant one-cell decoder with a joint decoder.
Cycles 539/545 decoded a shared patch once.  Cycles 548/551 widened recurrence,
and Cycle 555 found a companion pivot that closes complete-network `N<=2`.
Cycle 557 again shows that a route-specific local decoder collision can be
removed by a relational one-hot or returned-slot construction.  The repeated
echo is constructive import retirement, not constitutional failure.

No route-independent obstruction, minimum-content theorem, constitutional
change, or axiom pressure survives N1–N8.

## Disposition and next campaign

Retain Route C as the strongest bounded `N<=3` compiler result:

- one three-M2 slot, locally validity checked, returned after each cell;
- exhaustive 42-word/116-ray one-cell inverse;
- exhaustive 299-column/1,324-row adjacent-patch inverse;
- zero pattern conflicts, Gram error, inverse error, and terminal leakage;
- literal bounded M2 placement and nearest-neighbour routes;
- all-24/576 transported selected-shell covariance;
- exact mass/contact/seam preservation fixtures; and
- no parity string, Jordan-Wigner ordering, or host selector.

Route B is retained as the exact independent comparator.  Route A is retired
only in its tested two-role form.

The optimal next campaign is the three-cell returned-slot path described in
N6, followed only on success by the smallest complete periodic `N<=3`
network and a new contact-sensitive update/intertwiner test.  A failure at the
third cell must be compared against Route B, larger relational role subsets,
and a bounded rolling gauge register before any obstruction language.

## Cold certificate

The integrated pre-freeze certificate passed all **12/12** aggregate
predicates in `19.994074207963422` internal seconds (`21.11` timed wall
seconds), reached `190,693,376` internal maximum RSS bytes
(`217,071,616` timed maximum resident-set bytes), and reported zero process
swaps.

The literal layout audit found:

| size / route | live M2 | universal pair routes | distinct NN edges | maximum path |
|---|---:|---:|---:|---:|
| L3 / B | 141 | 9,870 | 6,938 | 48 |
| L3 / C | 132 | 8,646 | 6,841 | 48 |
| held L4 / B | 141 | 9,870 | 6,645 | 48 |
| held L4 / C | 132 | 8,646 | 6,548 | 48 |

All base and mapped nearest-neighbour route-edge failures were zero.  The
one-cell preparation and physical-pattern digests, identical at L3 and held
L4, are:

```text
preparation       100a41dede658af604c6f544a0736a18084fc7c901258dedfe2c822a128724c5
physical pattern  17eeaa840dc2b8dd3924cc1bf57c131915b344fceb5b0bbb9972585ebb46aaca
```

The adjacent-patch decoder and ordered-factor-phase digests are:

```text
joint decoder      b49a80dcb7f71cd53355267f2e39343cbd11ebae0ed0ac9b44aa10ff596a8edd
factor/order phase cb32d01a7413065c88a049048c22b8aeece8c209abafb5d8ea0d86ed22cc2af2
```

The final post-note cold certificate is regenerated after this note and runner
are frozen.  Only that final JSON and the reported frozen hashes are packaging
evidence.
