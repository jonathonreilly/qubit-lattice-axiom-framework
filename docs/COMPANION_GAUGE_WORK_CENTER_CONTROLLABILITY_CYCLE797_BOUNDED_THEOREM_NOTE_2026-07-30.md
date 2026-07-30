# Companion gauge-work classification and local center controllability — Cycle 797

Date: 2026-07-30

Authority: none

Audit: unset

Status: bounded constructive theorem plus three route-specific pump falsifiers

Claim type: bounded_theorem

Runners:

- [`frontier_cycle797_companion_gauge_work_renewal_discriminator_2026_07_30.py`](../scripts/frontier_cycle797_companion_gauge_work_renewal_discriminator_2026_07_30.py)
- [`frontier_cycle797_companion_center_local_pump_discriminator_2026_07_30.py`](../scripts/frontier_cycle797_companion_center_local_pump_discriminator_2026_07_30.py)
- [`frontier_cycle797_companion_priority_center_preparation_2026_07_30.py`](../scripts/frontier_cycle797_companion_priority_center_preparation_2026_07_30.py)
- [`frontier_cycle797_companion_reversible_center_syndrome_stinespring_2026_07_30.py`](../scripts/frontier_cycle797_companion_reversible_center_syndrome_stinespring_2026_07_30.py)

Helper:

- [`frontier_cycle797_companion_axial_center_core_2026_07_30.py`](../scripts/frontier_cycle797_companion_axial_center_core_2026_07_30.py)

Constitutional effect: none. This package changes no axiom, foundation,
Qualification, primitive, registry, policy, queue, audit result, or audit
status. Sweep indices, rule order, cell labels, coframe labels, and circuit
ordinals are supplied computational structure. They are not physical time,
duration, cadence, rate, energy, Record, occurrence, or Born weight.

## Result up front

The Bell/correction work left by the landed Cycle-789 companion input channel
has now been classified against the actual Cycle-720 subsystem factorization.
On every tested box from one through thirty coarse cells, the output/reference
character algebra transfers exactly: the intended and realized output
generators have zero binary-span and zero signed-span failures on every row,
so subgroup-rank equality is not used as a surrogate for character identity.
Every residual output--environment
correlation vanishes after quotienting by the landed local gauge span, while
quotienting by the logical even-CAR pairs removes none of it. Thus the tested
residual is gauge work, not lost or corrupted logical information.

The one-mode repaired channel has an explicit six-gate environment-only
inverse with maximum output-plus-blank-work residual
`6.675402828397881e-16`. At multi-cell scope, the maximal environment-only
stabilizer subgroup is generated from radius-one cell neighborhoods, and
radius-one parity-even Paulis commuting with the full logical even-CAR basis
span every nonparity center syndrome through the held thirty-cell box.

The center-preparation step also closes constructively at reversible
syndrome-register level on a supplied finite axial frame and priority front.
Clean center-syndrome extraction, retained pivot-outcome copies, bounded
logical-commuting conditional Paulis, and explicit outcome-to-syndrome CNOT
fanout reset every tested lawful center syndrome without postselection while
preserving both total-parity blocks. The held thirty-cell complete macros
occupy at most twenty cells with diameter six. This is a bounded finite-box
channel, not autonomous renewal: the axial frame, boundary corner, finite
priority atlas, fresh work, bounded controlled-Pauli primitives, and literal
nearest-neighbour routing remain supplied or open.

Three simpler frozen local pump policies were also executed. Strict Hamming
descent traps; a fixed cyclic "fire every lit-overlap move" policy cycles;
and a fixed cyclic nonincrease policy traps or cycles. The tests refute
exactly those algorithms. A bounded rotor/marker transport, reversible gauge
echo, dissipative gauge refresh, or other autonomous local law remains live,
so there is no no-go, minimum-content theorem, shared obstruction, or axiom
pressure.

## Direct scientific dependencies

- the landed [Cycle-720 recurrent companion physical update and mixed-gauge
  factorization](./RECURRENT_COMPANION_PHYSICAL_M2_UPDATE_LOCAL_CHOI_PREPARATION_CYCLE720_BOUNDED_THEOREM_NOTE_2026-07-27.md);
- the landed [Cycle-789 three-register companion input circuit](./THREE_REGISTER_COMPANION_INPUT_CIRCUIT_CYCLE789_BOUNDED_THEOREM_NOTE_2026-07-30.md); and
- the landed [Cycle-794 literal prefix, recurrent update, and signed
  proper-cubic shear](./LITERAL_THREE_BANK_PREFIX_RECURRENT_G_ACTUAL_SHEAR_CYCLE794_BOUNDED_THEOREM_NOTE_2026-07-30.md).

All public runners and helpers import only landed modules or other Cycle-797
package files. No scratch module is imported.

## Exact Bell-work classification

For the final stabilizer group, let `O/R` denote output plus diagnostic
reference and let the complement denote retained work. The runner computes
the exact subgroup supported on each side and the rank of their residual
cross correlations. It then adds, separately, the actual Cycle-720 logical
rows and the actual Cycle-720 local gauge span to the `O/R` quotient.

| shape | cells | character rank | raw cross rank | after logical quotient | after full gauge quotient | nonparity centers / radius-one move rank |
|---|---:|---:|---:|---:|---:|---:|
| `1x1x1` | 1 | 11 | 1 | 1 | 0 | 0 / 0 |
| `2x1x1` | 2 | 23 | 4 | 4 | 0 | 0 / 0 |
| `2x2x1` | 4 | 48 | 12 | 12 | 0 | 1 / 1 |
| `2x2x2` | 8 | 100 | 32 | 32 | 0 | 5 / 5 |
| `3x2x2` | 12 | 152 | 52 | 52 | 0 | 9 / 9 |
| `4x1x3` | 12 | 149 | 43 | 43 | 0 | 6 / 6 |
| `1x4x3` | 12 | 149 | 46 | 46 | 0 | 6 / 6 |
| `5x3x2` | 30 | 389 | 136 | 136 | 0 | 30 / 30 |

The anisotropic raw ranks `43` and `46` differ, but both disappear in the
full gauge quotient. This is a gauge/order-bookkeeping diagnostic, not a
logical covariance failure. The tempting finite-size formula `N + 2E` is
also actively falsified at held size: it predicts `148` for `5x3x2`, while
the exact raw cross rank is `136`.

The center slice is not the entire work sector. Resetting all nonparity
centers reduces the held raw rank from `136` to `106`; using the separately
supplied total-parity value reduces it to `105`. The remaining `105` ranks
belong to noncentral gauge-pair correlations. A coherent center reset moves
the old syndrome into retained work; it does not return the work bank blank.

## One-mode cleanup and active controls

For registers `O,I,L,aZ,aX`, the explicit cleanup is

1. `CZ(L,aX)`;
2. `CNOT(L,aZ)`;
3. `CNOT(I,aZ)`;
4. `H(aX)`;
5. `H(L)`;
6. `H(I)`.

It was executed on `|0>`, `|1>`, `|+>`, and `|+i>` inputs. The maximum
output-plus-blank-environment residual is `6.675402828397881e-16`, and the
minimum environment-ray overlap is `0.9999999999999989`. Deleting the second
gate gives residual approximately `1`; reversing the order gives
`1.2247448713915885`.

The multirow controls also detect a dirty Bell ancilla, a missing live
character row, a deleted private dual, and the hostile self-comparison
channel. Exact inverse round-trip mismatches are zero. The held-size formula
and anisotropic gauge-order controls prevent the rank census from merely
reprinting its own expectation.

## Local controllability and frozen pump policies

The second runner independently reconstructs local moves as radius-one
nullspace generators of the complete logical commutator system, pairs them to
preserve total parity, and computes their center syndromes. It does not import
the first runner's center-move implementation.

| shape | centers | syndrome rank | maximum move cells | maximum diameter | tested syndrome states |
|---|---:|---:|---:|---:|---:|
| `2x2x1` | 1 | 1 | 2 | 1 | 2 exhaustive |
| `2x2x2` | 5 | 5 | 3 | 2 | 32 exhaustive |
| `3x2x2` | 9 | 9 | 4 | 2 | 512 exhaustive |
| `5x3x2` | 30 | 30 | 4 | 2 | 4,127 deterministic controls/samples |

All move/logical and move/parity commutator failure counts are zero.

The executed route-specific failures are:

- strict Hamming descent leaves `16/32` nonzero states trapped on `2x2x2`
  and `448/512` trapped on `3x2x2`;
- the fixed lit-overlap sweep has sixteen fixed cycles on `2x2x2` and 480
  seven-cycles on `3x2x2`; and
- the fixed nonincrease sweep closes `2x2x2` but traps `448/512` states on
  `3x2x2`.

The deterministic held sample finds nonzero recurrent or trapped states for
all three policies. This is an active held control, not an exhaustive
thirty-bit census.

## Bounded center preparation with a supplied priority front

The third runner reconstructs the nonparity center as elementary products of
companion-eta link words around coarse plaquettes. In one supplied axial
proper-cubic frame, all `xy` and `xz` plaquettes plus the `yz` plaquettes on
the `x=0` face form independent coordinates of rank `E - V + 1`. For each
radius-two cell ball, the runner enumerates the complete local
logical-commuting, parity-even syndrome subspace and chooses a finite-box
triangular atlas.

This identification is checked against the actual Cycle-720 gauge radical,
not inferred from the expected rank alone. Plaquettes plus total parity have
ranks `2`, `6`, `10`, and `31` on the four fixtures, equal the reconstructed
Cycle-720 center rank in each case, and give zero span mismatches.

At atlas row `j`, the channel remeasures the current local plaquette pivot
into a fresh retained register. It then conditionally applies the chosen
Pauli. This just-in-time remeasurement is load-bearing: an earlier correction
may flip a later check, so no stale stored syndrome is host-updated. Every
measurement and control environment is retained. This specifies a
trace-preserving nonpostselected channel at stabilizer-macro level; literal
nearest-neighbour decomposition of the measurement/correction macros remains
open.

| shape | center rank / atlas rows | tested lawful fluxes | max correction cells / diameter / Pauli weight | max joint measure+correct cells / diameter | construction attempts | residual failures |
|---|---:|---:|---:|---:|---:|---:|
| `2x2x1` | 1 / 1 | 2 exhaustive | 2 / 1 / 3 | 4 / 2 | 1 | 0 |
| `2x2x2` | 5 / 5 | 32 exhaustive | 4 / 3 / 7 | 6 / 3 | 1 | 0 |
| `3x2x2` | 9 / 9 | 512 exhaustive | 8 / 4 / 18 | 10 / 4 | 1 | 0 |
| `5x3x2` | 30 / 30 | 4,128 deterministic controls/samples | 11 / 4 / 36 | 14 / 6 | 192 | 0 |

All atlas-move commutators with the complete logical even-CAR basis and total
parity vanish. All center phases are consistent. Deleting any atlas row is
detected. Flipping each just-in-time measurement outcome in turn from the
zero-center input leaves a nonzero final syndrome in every tested mutation.
The held construction searches a finite atlas and is not evidence that one
translation-compatible priority rule exists.

### Executed reversible syndrome registers

The fourth runner replaces the remeasurement abstraction by an explicit
reversible auxiliary word. It coherently extracts the independent center
checks into clean syndrome M2, copies the current pivot to one retained
outcome M2, applies the controlled physical Pauli, and fans that retained
outcome into every syndrome bit toggled by the correction. The syndrome bank
therefore tracks the current physical center without host-side mutation and
returns to zero after the triangular pass. The retained outcome bank carries
the initial syndrome, so the induced center-sector map is an isometry rather
than deletion.

For one, five, and nine center coordinates, all `2`, `32`, and `512` sectors
are exhaustive and the dense environment Gram residual is exactly zero. On
the held thirty-coordinate box, all `4,128` deterministic controls/samples
have zero physical-reset, syndrome-register-return, and remeasurement
disagreement failures; the retained-environment GF(2) map has rank `30/30`.
Extraction, pivot-copy, correction, and update deletions are active, and dirty
syndrome/outcome inputs are exposed. The held nontrivial atlas gives `4,122 /
4,128` residual sectors for both reversed order and the hostile stale-register
word.

The held auxiliary census is thirty syndrome plus thirty retained-outcome M2,
sixty extraction Hadamards, 288 controlled extraction-Pauli factors, thirty
pivot copies, 380 controlled correction-Pauli factors, and 59 syndrome-update
CNOTs. The complete macro support is at most twenty cells with diameter six;
the correction alone is at most eleven cells with diameter four. These are
finite stabilizer-macro counts. `literal_NN_route_executed` remains false.

## Covariance boundary

The gauge-work runner checks that radius-one support and cell labels transport
under all 24 proper-cubic frames and 576 ordered products with zero failures.
The reversible syndrome runner also transports the supplied atlas macro
supports through 24 frames and 576 products with zero distance or product
failures. These are conditional support/label covariance checks only. The full
signed prefix/update covariance remains the separate Cycle-794 result; this
package does not silently promote a support-radius check into a signed
physical covariance theorem. No translation-compatible recurrent pump exists
yet whose signed covariance could be tested; the supplied-front preparation
is one-frame only.

## Supplied / derived / open

### Supplied

- the Cycle-720 companion dictionary, subsystem factorization, cell chart,
  finite boundary, and one total-parity sector;
- the Cycle-789 prepared `O/I` Choi resource, encoded live `L` bank,
  private-dual atlas, and clean Bell syndrome ancillas;
- finite cell/coframe labels and fixed runner order; and
- one axial frame, open-boundary corner, finite triangular priority atlas,
  fresh clean syndrome/outcome M2, bounded controlled-Pauli primitives, and a
  finite route chart.

### Derived

- exact output/reference character transfer on the tested one- through
  thirty-cell boxes;
- an exact quotient proving that all tested residual cross correlations lie
  in the landed local gauge span and none in the logical pair span;
- an explicit exact one-mode environment-only cleanup;
- radius-one generation of the maximal environment-only stabilizer subgroup;
- radius-one parity-preserving logical-commuting controllability of every
  nonparity center syndrome through held thirty-cell scope;
- a trace-preserving nonpostselected center-sector preparation channel at
  bounded tested-box reversible syndrome-register scope with a supplied
  priority front; and
- exact traps or cycles for three named frozen pump algorithms.

### Open

- a translation-compatible recurrent priority/front law replacing the
  supplied axial frame, corner, and finite-box atlas;
- renewal or a reversible bounded destination that returns the fresh
  measurement/syndrome work blank across repeated epochs;
- classification and refresh of the noncentral gauge-pair sector;
- literal nearest-neighbour routing/coloring of a successful simultaneous
  renewal law;
- renewal of the supplied `O/I` Choi resource and Bell ancillas;
- translation-compatible genesis/enforcement of coframe, cell colours,
  parity sector, and clean code domain; and
- one literal returned epoch composing preparation, Cycle-789 input,
  Cycle-720 recurrent update, and renewal.

## No-go discipline N1--N8

The universal negative gate fails, deliberately: constructive alternatives
remain open. Therefore this package ships no no-go. Its negative content is
only the exact behavior of three frozen algorithms.

### N1 -- normalized alternatives

| normalized route family | status | result |
|---|---|---|
| finite-box triangular center preparation | ATTEMPTED | closes a nonpostselected bounded stabilizer-macro channel with supplied frame/front, but not autonomous recurrent renewal |
| memoryless local potential descent | ATTEMPTED | strict Hamming descent has the exact traps reported above |
| fixed cyclic overlap sweep | ATTEMPTED | lit-overlap and nonincrease policies have the exact cycles/traps reported above |
| reversible gauge-pair echo with retained ACK | UNTESTED/OPEN | Cycle 703 supplies relevant abstract prior art, but not this companion-code renewal law |
| bounded rotor/marker defect transport | UNTESTED/OPEN | local memory may break the observed cycles without a global solve |
| staggered covariant feature transport | UNTESTED/OPEN | a fixed local phase schedule remains constructively available |
| local gauge-mixing or subsystem refresh channel | UNTESTED/OPEN | the lawful-domain and repeatability obligations remain untested |

Fewer than five normalized families are attempted or ruled out by retained
prior authority. N1 therefore blocks every route-independent impossibility
claim.

### N2 -- wall independence

The supplied-front center reset is closed at tested scope. Autonomous front
generation, noncentral gauge-pair refresh, and blank work return are treated
as one collapsed recurrent-renewal obligation because one reversible local
construction may close them together. Resource genesis, local coframe/sector
enforcement, and occurrence/admission are distinct: none is implied merely by
refreshing gauge work. No inflated wall count is used.

### N3 -- hidden-wall scan

The fixed parity sector, finite boundary, companion dictionary, prepared Choi
bank, clean Bell ancillas, private-dual atlas, cell/coframe labels, axial
frame/corner, finite priority atlas, rule order, and fresh syndrome work are
explicit supplies. No appeal to standard QFT, background control, canonical
ordering, or framework-provided measurement is load-bearing and hidden.

### N4 -- residual matching

Cycle 703 concerns abstract BKSF stabilizer preparation and a growing exact
feedforward decoder. Cycle 797 concerns renewal of the landed Cycle-720
companion gauge/center work after the Cycle-789 input channel. The residuals
are similar but not identical, so Cycle 703 is prior art and a cross-cycle
echo, not evidence that closes this residual.

### N5 -- rhetoric and resolution

The positive span and supplied-front preparation results are tested per
bounded cell neighborhood and on finite boxes through thirty cells. The
frozen-rule failures are exhaustive only through nine center bits and
deterministic-sampled at thirty bits. No lattice-wide failure, minimum
support, or impossibility of local pumping is stated.

### N6 -- partial closure

The logical-information question is closed at tested scope: the residual is
gauge-only. The center-algebra reachability question is closed at tested
scope, and the supplied-front center preparation is upgraded from projection
to an explicit reversible syndrome-register channel. These positive partial
closures move the remaining obligation to autonomous front generation,
literal routing, and recurrent work renewal; they do not require a new axiom
or primitive.

### N7 -- steelman

A hostile reviewer should reject any no-go because the failed rules are
memoryless or use a frozen sweep, while the local move set is fully
controllable and a finite supplied-front preparation channel now closes.
One bounded rotor per cell/edge, a reversible ACK echo, or a locally mixed
gauge-refresh channel could generate that front and return work without a
one-hot global inverse. The actionable terminal test is repeated epochs on
the same dirty work bank with exact logical intertwining, bounded support,
translation compatibility, and signed proper-cubic covariance.

### N8 -- cross-cycle echo

Cycle 703 already separated local check/move availability from a growing
exact decoder and used reversible echo/ACK structure. Cycle 794 also retired a
same-slot frame shortcut by adding a bounded local shear/phase wrapper. Both
histories argue for another constructive local-memory route, not for a shared
substrate obstruction.

## Verdict

The physical compiler's current failure is no longer unexplained Bell
information loss, absence of local center controls, or postselected center
projection. Logical information is intact, the residual work is gauge-only,
every nonparity center syndrome is locally reachable, and a bounded
nonpostselected supplied-front center preparation channel closes at tested
scope. What is still missing is a translation-compatible priority/front,
literal routed measurement/correction macros, and an executed repeated law
that renews gauge/center work without accumulating retained garbage, followed
by autonomous resource/domain genesis. That sharper target is meaningful
progress, but the recurrent autonomous physical-M2 compiler remains open.
