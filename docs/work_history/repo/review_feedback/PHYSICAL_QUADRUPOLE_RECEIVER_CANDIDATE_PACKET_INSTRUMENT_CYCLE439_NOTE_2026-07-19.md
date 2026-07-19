# Physical quadrupole receiver / candidate-packet label instrument — Cycle 439

Date: 2026-07-19

Authority: none

Audit: unset

## Result

Cycle 439 replaces the Cycle-435 compressed-effect-only pointer with an exact
self-adjoint XOR pointer unitary.  On the declared one-particle receiver code,
the unitary couples the three fine position labels to two pointer M2 and has
an exact inverse.  It then applies three independent Cycle-433-pattern writer
patches linearly, so that every fine label writes its own complete
Cycle-370-compatible candidate carrier while all three labels remain coherent.

The construction is exercised on the actual Cycle-435 train and held evolved
packets at both physical strength analogues.  It retains the field sector,
216-dimensional source label, 18-dimensional receiver label, two-M2 pointer,
and every M2 in all three writer patches.  Candidate-sector weights are
reduced from the composed output state; they are not copied from the pointer
weight array.  The exact inverse with pointer and source retained is checked
on every actual row.

This is a bounded reversible candidate; the candidate packet is not a Record.
There is no outcome,
occurrence, Born weight, or selected readout.  In particular, no pointer label
or candidate carrier is selected, admitted, or actualized.  Cycle-420 named
and numeric flags remain false.

## Exact pointer coupling

The receiver code has 18 one-particle columns: six direction labels in each
of three receiver cells.  Let `P_j` project onto the six columns in cell
`j=0,1,2`, and let `XOR(j)` act on the four states of two pointer M2.  The
logical coupling is

```text
U_pointer = sum_j P_j tensor XOR(j).
```

Starting from pointer `00`, the three fine position labels become `00`, `01`,
and `10`; `11` is unused.  Since XOR is its own inverse,

```text
U_pointer dagger U_pointer - I = 0
U_pointer - U_pointer dagger   = 0
U_pointer^2 - I                = 0.
```

Thus this is an exact self-adjoint XOR pointer unitary for three fine position
labels and two pointer M2.  It is stronger than Cycle 435's effect-only
dilation because it supplies a reversible pointer action and inverse.

## Physical receiver compiler

For each Cycle-435 train/held receiver encoding `E_R`, the physical action is

```text
G_physical,439(M) = M + E_R [U_pointer(E_R^dagger M) - E_R^dagger M].
```

It acts as the XOR coupling on the encoded image and as the identity on its
orthogonal complement.  On the declared code space,

```text
E_439 G_439 = G_physical,439 E_439.
```

The train and held receiver encodings both have shape `(261328,18)`.  The
receiver matter support is 118 M2; including the two-M2 pointer gives one
120-M2 projector-controlled block.

| geometry | Gram max | E/G residual | inverse residual | leakage |
|---|---:|---:|---:|---:|
| train `a=1` | `0` | `9.31112232373328e-16` | `1.481582520491644e-15` | `6.892794313920941e-16` |
| held `a=2` | `0` | `1.045810647685796e-15` | `1.7612346877388343e-15` | `7.407274925672636e-16` |

The largest physical compiler residual is
`1.7612346877388343e-15`, far below the declared `9e-10` tolerance.

The pointer permutation never changes a receiver index.  Its one-particle
receiver diagonal and total number are therefore preserved exactly; the
runner tests zero diagonal-weight residual and number `1 -> 1`.  The mass
fixture and Cycle-230 contact update inside Cycle 435 are inherited unchanged,
not freshly rerun by Cycle 439.  This instrument follows that evolution and
does not modify its matter coin, contact, source, or stream factors.
The inherited mass value is `0.4534056541748851` (Cycle-435 eigenvector
residual `3.534751832054436e-16`), and each full Cycle-435 block retains the
645 nontrivial Cycle-230 contact columns.

The 120-M2 projector-controlled block is supplied.  Primitive synthesis
remains supplied and unconstructed; this cycle does not decompose that block
into a nearest-neighbour primitive schedule.  It therefore establishes a
bounded physical-code action, not an autonomous primitive implementation.

## Actual Cycle-435 composition

The runner evolves the actual Cycle-435 `Q0 direct-sum Q1` train and held
states and applies the pointer to the full source/receiver field state.  The
pointer weights and compression agree with the original three-cell receiver
weights and moments.

| geometry / strength | pointer weights `(j=0,1,2)` | unused `11` weight | pointer inverse |
|---|---|---:|---:|
| train / unit analogue | `(0.00566220, 0.98867559, 0.00566220)` | `0` | `0` |
| train / coefficient-two analogue | `(0.00566441, 0.98867119, 0.00566441)` | `0` | `0` |
| held / unit analogue | `(0.11323630, 0.77352740, 0.11323630)` | `0` | `0` |
| held / coefficient-two analogue | `(0.11323898, 0.77352203, 0.11323898)` | `0` | `0` |

The maximum receiver-versus-pointer weight residual is
`1.0547134782972093e-14`; the maximum centroid/second-moment/width compression
residual is `1.3877787807814457e-15`; the pointer inverse residual is exactly
zero.  These are coherent squared norms only, not probabilities or Born
frequencies.

## Three independent candidate writers

Each label controls its own Cycle-433-pattern writer.  Each writer occupies a
connected 468-M2 patch and uses a fixed 480-layer, 1026-gate X/CNOT/Toffoli
layout with maximum primitive support three M2.  Only 79 M2 in that patch are
the independent Cycle-370 candidate carrier.  The other 389 M2 contain the
proposal fields, lawful protected predecessor, predicate/certificate inputs,
router/work bits, and reversible workspace.

The three patches therefore contain three independent 79-M2 candidate
packets, not a single shared carrier and not merely pointers back to a source
register.  Every occupied carrier is written field-by-field: protected
occupancy, signed target site, 30 payload M2, predecessor presence/site, and
compatibility fields.  All 79 target lanes match the Cycle-370 encoder, the
decoder accepts the occupied carrier, workspace leakage is zero, and reverse
execution restores every supplied patch basis state exactly.

The position targets are:

| geometry | label 0 | label 1 | label 2 |
|---|---|---|---|
| train | `(5,-1,0)` | `(5,0,0)` | `(5,1,0)` |
| held `a=2` | `(17,-12,5)` | `(17,-11,5)` | `(17,-10,5)` |

The fourth pointer basis label writes no packet.  It has zero weight for all
tested physical inputs.

## Exact coherent pointer-to-packet action

The full tensor product would be unnecessarily enormous, so the runner uses
an exact factorwise block-sparse representation.  A nonzero block is keyed by

```text
(field sector, pointer label, complete three-writer-bank M2 signatures),
```

while its dense block axes retain all 216 source and 18 receiver labels.  A
bank signature contains every bit of each 468-M2 writer patch, not only its
79-M2 carrier.  Applying the actual writer permutations linearly gives 2019
nonzero train blocks and 4503 held blocks at each strength.  Reverse execution
maps every output signature back to its prepared signature.

Candidate weights are computed only after this action by summing squared
block norms in sectors whose actual 79-M2 target lanes are occupied.  For all
four physical rows:

```text
pointer-retention residual             0
candidate-sector / pointer residual    0
full factorwise inverse residual       0
retained coherent labels               (0,1,2)
selected label                         none.
```

This exact reduction closes the coherent three-label output check without
assuming its answer.

## Proper-cubic covariance

All 24 proper-cubic frames rotate the receiver direction payloads, physical
sites, target/predecessor sites, and 30-M2 payload fields together.  Position
cell labels are unchanged by this direction-frame action, so the pointer XOR
commutes with the induced 18-dimensional receiver representation.  The
runner checks all `24 x 2 x 3 = 144` rotated writer cases, including held
`a=2`, for accepted payloads, exact inverse, and valid connected support.

```text
maximum pointer covariance residual    0
writer payload failures                0 / 144
writer inverse failures                0 / 144
rotated support failures               0 / 144
```

This is covariance of the supplied family.  It does not derive the family or
the label router from autonomous local data.

## Deletions and lawful-domain controls

Independent controls delete the pointer coupling, the pointer high bit, one
label writer, the writer router, one payload-lane gate, and one protected
occupancy gate.  The first two change the actual train pointer distribution;
the label-writer and router deletions leave the target carrier blank; the
payload deletion creates a field mismatch; and the occupancy deletion makes
the resulting carrier fail the Cycle-370 decoder.

These are label, pointer, writer, payload, occupancy, and router deletions;
none is inferred from another deletion.  Six malformed-domain cases are
rejected: an out-of-code receiver index, wrong
pointer array shape, invalid deleted-bit index, invalid physical strength,
invalid label, and wrong inverse-writer arity.

```text
independently visible deletions    6 / 6
lawful-domain rejections           6 / 6
payload gates removed              1
payload lane mismatches            1
occupancy gates removed            1
occupancy-deleted decoder reject   true
```

## Supplied structure and exact boundary

Supplied structure is:

1. the Cycle-435 receiver encodings, actual evolved source/receiver packets,
   fixed strengths, coordinates, and fixed update;
2. the receiver position projectors, the 120-M2 projector-controlled XOR
   block, its still-unconstructed primitive synthesis, and identity
   completion outside the receiver code image;
3. three 468-M2 Cycle-433-pattern patches, blank 79-M2 target carriers, raw
   proposal fields, lawful protected predecessors, formation/certificate
   bits, payload-presence bits, faithful-close/provenance/readiness/freshness
   bits, and workspace;
4. the pointer-label writer multiplexor/router and its primitive synthesis;
   and
5. the train/held candidate payloads and protected predecessors.

Derived here are the exact two-M2 pointer unitary and inverse on both physical
receiver codes, its composition with the actual Cycle-435 packets, the exact
block-linear routing into three independent carriers, output-reduced sector
weights, all-24 covariance, and the stated deletion/domain controls.

The installed bounded support is `118 + 2 + 3*468 = 1524 M2`.  Relative to
the existing Cycle-435 receiver block, the added pointer/writer support is
`2 + 3*468 = 1406 M2`.  This is constant overhead for this fixed three-label
receiver cell.

The writer is only a Cycle-433-pattern writer.  No actual Cycle-424
detector/predicate interface is connected here.  Autonomous detector,
predicate and formation-bit genesis remain open.  The label router and
projector-controlled pointer block remain supplied.  Candidate admission,
occurrence, actual history, Record formation, and autonomous protected
capacity renewal remain open.

The Cycle-420 legacy packet/readout/numeric join is not selected or reproduced.
There is no selected centroid ensemble, force, physical energy, generator
rate, source-stress selection, metric, or gravity claim.

## Prior-art and novelty boundary

XOR pointer registers, reversible X/CNOT/Toffoli writers, block-diagonal
controlled unitaries, and coherent controlled routing are standard prior art;
no foundational novelty is claimed for those ingredients.  Cycle 439 claims
only the repo-local composition: the specific Cycle-435 physical receiver
code and actual train/held packet states are joined reversibly to three
Cycle-370-compatible carriers using the Cycle-433 layout, with the stated
physical E/G, inverse, covariance, and controls.  It neither extends nor uses
the Thirring engine.

## Disposition

Cycle 439 is a positive bounded reversible bridge from the Cycle-435 physical
one-particle receiver code to three Cycle-370-compatible candidate carriers.
It closes the previous effect-only pointer and basis-only writer-composition
gaps on the declared code space.  It does not close primitive synthesis or
autonomous control genesis, and it does not turn any candidate into a Record.

No no-go, minimum-content, shared-obstruction, or axiom-pressure claim is
made.  Authority remains none and audit remains unset.

## Verification

Run from the repository root:

```bash
python3 -m py_compile scripts/physical_quadrupole_receiver_candidate_packet_instrument_cycle439_2026_07_19.py
python3 scripts/physical_quadrupole_receiver_candidate_packet_instrument_cycle439_2026_07_19.py
```

Final cold-run result:

```text
SUMMARY {'pass': 11, 'fail': 0}
RESULT PHYSICAL_QUADRUPOLE_RECEIVER_CANDIDATE_PACKET_INSTRUMENT_CERTIFIED
```

The file hashes are reported with the handoff so that this note does not try
to contain its own self-referential digest.
