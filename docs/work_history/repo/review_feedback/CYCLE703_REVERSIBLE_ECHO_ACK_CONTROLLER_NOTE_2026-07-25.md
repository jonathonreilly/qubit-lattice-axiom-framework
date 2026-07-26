# Cycle 703 reversible echo/ack controller — 2026-07-25

Authority: none

Audit: unset

## Scope and result

This Cycle-703 addendum replaces the forward-only ready-bit decoder by an
explicit bounded-state echo/ack controller.  Each axial dependency component
is a rooted tree.  A local token walks its Euler contour using a fixed port
permutation:

- on a parent-to-child dart, XOR the child value from its parent and adjacent
  syndrome bit, then let that value control the colocated physical Z;
- on the matching child-to-parent dart, apply the same XOR and return the child
  value blank;
- when the token returns to its own boundary root, park it idle and mark that
  local syndrome bank spent.

The controller has radius one, maximum tree degree three, and at most six M2
controller bits per dependency node.  Readiness, traversal, acknowledgement,
and return are local.  There is no host-selected correction, route, stop,
barrier, size table, or round counter.  Events are circuit/controller labels,
not physical time.

All recurrence work returns blank and every token returns idle.  The syndrome
bits and one-time fresh/spent epoch flags deliberately remain.  This is not a
pretended erasure.

The stronger state result is also positive.  Coherent syndrome extraction and
the phase-zero Z decoders factor the complete open L2 preparation as

```text
|vac_BKSF>_edge tensor |chi>_syndrome-bank,

|chi> = |+>^96_triangle
        tensor |uniform-even>_six-coarse
        tensor |+>^12_bond.
```

The physical vacuum and syndrome-bank factor are individually pure and have
Schmidt rank one across the edge/syndrome-bank cut.  The repaired logical
loader and every later edge-qubit update act trivially on the syndrome-bank
register.  Therefore one-time `E` does not require syndrome-bank reset: the
bounded local auxiliary can remain in a fixed immutable sector.  Reusing the
same bank as a new blank measurement target is a different obligation and is
not constructed.

## Local dependency forest and echo

There are two node types.  `A_y(x,y,z)` forms an x-directed line.  `A_z`
forms, for each z, a y-directed spine on the lower x face with one x branch at
each spine node.  Parent-source relations are exactly the uniform axial
recurrences from the cellular decoder.

The local port order is

```text
parent -> x-child -> y-child -> parent.
```

Missing ports are skipped.  Thus the router tables on the two-bit port code
`00=parent,01=x,10=y,11=unused` are:

| Local degree | Four-state permutation |
|---|---|
| leaf | `(0,1,2,3)` |
| one child | `(1,0,2,3)` |
| two children | `(1,2,0,3)` |

The last row is a three-cycle, not an irreversible selector.  A tree contour
uses each down-dart and up-dart exactly once.  No mutable path stack is needed;
the incoming port determines the next outgoing port.

The value gate has the complete truth rule

```text
(parent, source, child) ->
(parent, source, child xor parent xor source).
```

All eight rows round-trip under the same gate.  Token motion is an adjacent
SWAP.  The one-time epoch handshake is embedded in a four-cycle, and the
physical correction is controlled Z with basis phases `(1,1,1,-1)`.  The
runner finds zero XOR, router, token-SWAP, epoch-bijection, and controlled-Z
unitarity failures.  These are bounded M2 permutations plus one bounded phase
gate.

The fresh/spent state belongs to the retained syndrome bank.  It makes the
one-time preparation macro invertible: the inverse macro starts in the spent
sector, walks the inverse contour, and restores the fresh input while undoing
the physical correction.  Repeated autonomous application of the preparation
macro is not the recurrent physical law.

## Exact syndrome tests and returned work

L2 enumerates all 4,096 edge patterns and all 32 distinct lawful syndromes.
Every branch has zero correction, returned-work, or root-ack failure.

For L2--L8, the runner applies the echo controller to every unit-edge incidence
syndrome and to 64 deterministic XOR pairs per size:

| L | Basis cases | Dependency nodes / roots | Syndrome failures | Forward-CA mismatch | Work/ack/token failures | Linearity failures |
|---:|---:|---:|---:|---:|---:|---:|
| 2 | 12 | `8 / 3` | 0 | 0 | 0 | 0 |
| 3 | 54 | `36 / 8` | 0 | 0 | 0 | 0 |
| 4 | 144 | `96 / 15` | 0 | 0 | 0 | 0 |
| 5 | 300 | `200 / 24` | 0 | 0 | 0 | 0 |
| 6 | 540 | `360 / 35` | 0 | 0 | 0 | 0 |
| 7 | 882 | `588 / 48` | 0 | 0 | 0 | 0 |
| 8 | 1,344 | `896 / 63` | 0 | 0 | 0 | 0 |

There are `2L^2(L-1)` work nodes and `L^2-1` disjoint local roots.  Every
nonroot value is computed and uncomputed once.  Roots begin and finish with
value zero; their spent acknowledgement is retained with the syndrome bank.
No result depends on an event-count interpretation as time.

## Active transition deletions

All nine transition families are deleted independently on every L4 unit-edge
case:

| Deleted transition | Syndrome failures | Work failures | Root-ack failures | Stalled tokens |
|---|---:|---:|---:|---:|
| acknowledgement uncompute | 0 | 144 | 0 | 0 |
| child compute | 144 | 144 | 144 | 144 |
| controlled-Z emission | 144 | 0 | 0 | 0 |
| root spent acknowledgement | 0 | 144 | 144 | 0 |
| x-child route | 135 | 0 | 0 | 0 |
| y-child route | 87 | 0 | 0 | 0 |
| syndrome-source XOR | 144 | 0 | 0 | 0 |
| A-y root start | 96 | 0 | 144 | 0 |
| A-z root start | 108 | 0 | 144 | 0 |

Every deletion is detected.

## Proper-cubic, translation, and boundary covariance

The coframe, local port order, dependency roots, and lower boundary corner are
transported together.  On L4 the direct transported controller is compared
with the transformed canonical correction for all 144 unit-edge inputs, all
24 proper-cubic frames, and two translations: 6,912 cases with zero transport
failure.

This is proper-cubic chart covariance with supplied boundary/coframe data.  It
does not select a preferred global Jordan--Wigner order or claim that an
unmarked symmetric box chooses one corner by itself.  Periodic fixed-Wilson
preparation remains separate.

## Complete L2 phase and factorization proof

The open L2 graph has 168 BKSF edge qubits.  Its loop stages add independent ranks

```text
triangle / coarse quotient / bond = 96 / 5 / 12,
```

for total loop rank 113.  The six coarse rows have one quotient relation: their
product equals a phase-zero product of 24 already fixed triangle rows.  Hence
the six coarse syndrome bits have even parity and exactly 32 lawful values.

The executable checks:

- all 4,096 one-cell triangle syndrome columns, with the same table reused in
  all eight cells;
- all 32 coarse lawful columns through the echo controller;
- all 4,096 bond syndrome columns;
- exact commutators against the measured rows and all earlier-stage rows;
- pure-Z, phase-zero correction for every column;
- the dependent coarse relation including Pauli phase.

The load-bearing uniform-amplitude discriminator is independent of the
physical/syndrome-bank register split.  Select the 96 triangle rows, five independent
coarse rows, and 12 bond rows.  Their X-part has rank 113.  The X-part of all
114 measured rows also has rank 113, with the sole dependency the phase-zero
coarse relation.  Thus every nonidentity product of the 113 independent checks
is off-diagonal in the edge Z basis and has exactly zero `|0_edge>`
expectation.

The runner separately constructs 113 phase-zero pure-Z corrections.  Their
113-by-113 correction/check anticommutation matrix has rank 113, with unit
diagonal and no earlier-stage entries.  Therefore every syndrome character is
realized, while the X-rank test makes all nontrivial Fourier coefficients
zero.  This is the explicit uniform-amplitude discriminator; it does not infer
uniformity from a disjoint-register commutator.

Every residual is zero.  For every lawful stage syndrome `s`, correction
`A_s`, and syndrome projector `P_s`, the checked commutators give

```text
A_s P_s = P_+ A_s.
```

Every `A_s` is phase-zero pure Z, so `A_s|0_edge>=|0_edge>` exactly.  Therefore

```text
A_s P_s |0_edge> = P_+ |0_edge>
```

with no branch phase.  All `2^113` complete syndrome-bank columns have common
amplitude `2^(-113/2)` and phase zero.  This is an amplitude statement, not a
Born-frequency derivation.

The syndrome-bank state above has 114 independent stabilizer rows on its 114
auxiliary qubits: 96 triangle X rows, five independent even-X shifts plus the six-bit Z
parity row for the coarse block, and 12 bond X rows.  It has rank 114, zero
phase failures, and zero commutator failures.  The physical vacuum tableau has
rank 168.  Their direct product has rank 282 on 282 qubits.  Thus:

```text
edge reduced purity   = 1,
syndrome-bank reduced purity = 1,
edge/syndrome-bank Schmidt rank = 1.
```

Fixed spent flags and parked-idle token states are additional local product
factors; omitting those constant rows from the displayed 282-qubit tableau
does not change purity or Schmidt rank.

A 336-row type-separation census confirms that the recurrent physical Pauli
algebra is typed on the edge register while the fixed syndrome bank occupies its own
register.  The resulting commutators are tautological by disjoint support; they
check later-update inertness at the declared interface but do not prove
factorization.  Factorization and equal amplitudes rest instead on the
X-projection, full-rank correction/check pairing, phase-zero branch relations,
and the two complete stabilizer tableaux above.

## Syndrome-bank retention and reuse boundary

During later physics the local spent-sector rule is identity on both possible
syndrome bits.  The runner checks its two truth rows exactly.  The syndrome bank may
therefore remain as a bounded inert auxiliary for a one-time state isometry;
it neither carries later logical input nor participates in `G_physical`.
Keeping this fixed pure state does not consume growing memory during recurrent
matter updates.

Three reset questions must not be conflated:

1. **One-time coherent E:** no reset is required.  The syndrome bank is fixed,
   factorized, and inert.
2. **Reset of coherent `|chi>`:** a unitary exists because `|chi>` is one known
   pure stabilizer state.  A uniform local inverse-bank encoder is not
   constructed here.
3. **Reset after actual measurement/dephasing:** the syndrome bank is a mixture over
   `2^113` orthogonal values.  Mapping all of them to one blank while the
   already identical physical vacuum and every other register remain fixed has
   `2^113-1` collisions.  A unitary reset must export that entropy; a
   dissipative reset is an explicit alternative.

The same bank is therefore not claimed reusable as a blank measurement target
without a reset/export circuit.  That does not block the one-time compiler.
No pointer copy is called a Record.

The controller is embedded only in the abstract dependency graph.  A
collision-free allocation of its work qubits into the Cycle-232 spacing-16
`Z^3` macrocells, including nearest-neighbor routing around carrier sites, is
not constructed and remains a physical-site compiler obligation.
It acts on the parallel-reference-bond `OpenReferenceGraph`, not the
no-reference-bond `PatchGraph` used by the scaled schedule.  No common-E
equivalence between those graph codes is constructed here.

## Supplied structure and dependency effect

Supplied structure is the open boundary, transported coframe and port order,
one fresh/spent preparation epoch state per root, coherent or measured local
syndrome bits, bounded blank token/value M2, and one invocation of preparation
isometry `E`.

| Wall | Effect |
|---|---|
| `C_ref` | improved: bounded reference/gauge state preparation now has a local returned-work controller; coframe/boundary genesis remains supplied |
| `C_num` | unchanged: controller and syndrome-bank factorization are number blind |
| `C_wrap` | unchanged: token events and preparation stages are not causal time or realized history |
| `C_int` | improved operationally: the inherited local update starts from an exact phase-oriented state encoder with an inert factorized preparation auxiliary |
| `C_local` | materially improved: host table/path, forward-only work, and mandatory one-time reset are removed; blank-bank reuse and physical genesis of boundary/coframe remain open |
| `C_source` | unchanged |

There is no Record, Born rule, source law, shared obstruction, or axiom
pressure.

## No-go-discipline N1-N8 gate

The fresh `origin/main` no-go-discipline instructions were applied to the only
negative boundary: a dephased syndrome bank cannot be unitarily reset to one
blank while the identical vacuum and all other registers remain fixed.  The
claim is deliberately this narrow injectivity statement, not a no-go for
coherent reset, syndrome-bank retention, entropy export, or dissipative reuse.

### N1 — alternative route enumeration

1. **Syndrome-bank-only unitary reset — ATTEMPTED.** `2^113` orthogonal dephased inputs
   would map to one output, producing `2^113-1` collisions.
2. **Use the already corrected code as entropy sink while restoring the same
   vacuum — ATTEMPTED.** The output code column is identical by the exact
   factorization proof, so it supplies no orthogonal destination labels.
3. **Use recurrence work while returning it blank — ATTEMPTED.** Echo returns
   every value/token; requiring the same blank output reproduces the collision.
4. **Retain the syndrome bank inert — ATTEMPTED AND POSITIVE.** It avoids reset and is
   sufficient for one-time `E`, so it lies outside the reset premise.
5. **Coherently unprepare fixed pure `|chi>` — ATTEMPTED AT EXISTENCE LEVEL.**
   Purity/rank prove a unitary exists; its uniform local circuit remains open
   and the dephased premise does not apply.
6. **Export entropy or use a bath/new bank — OPEN ESCAPES.** These change the
   fixed-other-register premise and are not excluded.

The narrow collision claim survives.  Any broader reset/preparation no-go
would fail because routes 4--6 remain.

### N2 — wall independence

The collapsed open conditions are `W_blank-reuse` (a local reset/export
circuit), `W_boundary` (coframe/corner genesis), and `W_Wilson` (periodic
sector selection).

| Pair | First closes second? | Second closes first? | Independent? |
|---|---|---|---|
| blank-reuse / boundary | no | no | yes |
| blank-reuse / Wilson | no | no | yes |
| boundary / Wilson | no | no | yes |

Returned recurrence work is closed and is not counted as another wall.

### N3 — hidden-wall scan

Fresh/spent epoch state, coherent-versus-dephased syndrome-bank domain,
one-time use, open boundary, coframe/port order, token/value M2, syndrome-bank
retention, and absent blank-bank reset are explicit.  “Fixed syndrome bank” means the exact displayed
rank-114 stabilizer state, not a silently selected classical outcome.

### N4 — residual matching

The predecessor CA note left autonomous returned work open; this runner attacks
that exact residual and closes it.  The new reuse residual concerns only
dephased syndrome-bank entropy after physical factorization.  Periodic Wilson,
same-register rephase, and direct-route failures are not cited as witnesses.

### N5 — rhetoric audit

Tested resolutions are every local gate truth row, every L2 lawful coarse
syndrome, all triangle/bond columns, every unit-edge generator L2--L8, complete
L2 factor tableaux/phases, and all 24 transported frames at L4.  Not tested are
arbitrary shapes, noisy/fault-tolerant controllers, a local coherent
`|chi> -> |0>` circuit, periodic sectors, or repeated measurement-bank reuse.
The equal-amplitude test does not use the 336 type-separated cross-register
commutators: it uses the independent check X-rank 113 and the correction/check
pairing rank 113.
The collision claim is only for a dephased bank with every other output fixed.

### N6 — partial-closure paths

One-time inert retention already closes the compiler need.  Coherent inverse
stabilizer synthesis can close pure-bank reset; a boundary rail, another
retained bank, or a bath can close dephased reuse by carrying entropy.  These
are resource/interface constructions, not reasons for a new axiom.

### N7 — steelman

A hostile reviewer should reject any claim that “the syndrome bank cannot be
reset.”  The syndrome bank is one fixed pure stabilizer state in the coherent route,
so Clifford synthesis can unprepare it; after dephasing, a local boundary
conveyor can export its entropy.  The only surviving theorem is injectivity:
no unitary can merge `2^113` orthogonal dephased inputs when code, work, and
environment outputs are all required identical.

### N8 — cross-cycle echo

The one-shot feedforward range was retired by iterated CA, and the forward-only
work wall is retired here by the echo contour.  The same pattern forbids
promoting blank-bank reuse into constitutional evidence.  It is a scoped
entropy-interface obligation with explicit coherent, retained, export, and
dissipative escape routes; there is no axiom pressure.

## Reproduction

Run:

```text
PYTHONPATH=scripts python3 scripts/frontier_cycle703_reversible_echo_ack_controller_2026_07_25.py
```

The terminal marker is
`CYCLE703_ECHO_WORK_RETURNED_SYNDROME_BANK_FACTORS_AND_STAYS_INERT`.
The content-pinned cache is
`logs/runner-cache/frontier_cycle703_reversible_echo_ack_controller_2026_07_25.txt`.
