# Physical detector-to-protected Record-state formation compiler — Cycle 433

Date: 2026-07-19

Authority: none

Audit: unset

## Result and exact boundary

Cycle 433 constructs a bounded coherent physical compiler candidate for the
Cycle-364 immediate formation interface. The **actual physical detector M2**
from the Cycle-427/Cycle-430 scalar apparatus is joined to a fixed local
X/CNOT/Toffoli circuit. On the **declared code space**, detector click plus the
locally encoded payload, faithful-close, predecessor-ready, provenance,
fresh-capacity, and protected-predecessor controls writes one complete
**79-M2 protected Record-state candidate packet** into a separately supplied
blank Cycle-370 carrier.

The output is **not a pointer**. The circuit writes an independent protected
occupancy word, target coordinate, all 30 content M2, predecessor-present
bit, predecessor coordinate, and three compatibility bits. Its endpoint is
accepted by the Cycle-370 carrier decoder. The proposal fields and prior
packet are unchanged, so the result is an independently readable candidate
packet rather than a reference to another register.

The full joined map obeys

```text
E_433 G_coarse = G_physical,433 E_433
```

on the declared code space, and the enlarged physical map has an **exact
inverse**. The equality is evaluated on three logical apparatus inputs at
trained L=3 and held L=6. The physical side first executes the actual
Cycle-424 update used by Cycle 427, then couples its detector M2 to one blank
bridge M2, executes the fixed formation circuit, and clears the bridge. The
coarse side separately evaluates the click/no-click Kraus branches and the
Cycle-364 candidate formation map before encoding the result. No physical
detector sector is queried to choose a gate schedule.

This is a physical compiler for a conditional candidate interface. The
**formation law is not selected**. The coherent output is not admitted as an
actual framework Record, no dependency edge is added, and there is **no
occurrence or actual history**. Squared branch norm remains a physical sector
weight only.

## Reconnaissance boundary

The construction uses the earlier cycles at their stated interfaces:

- Cycle 342 supplies the complete 30-M2 typed/permanent content grammar,
  fixture decoder, and proper-cubic payload map.
- Cycle 351 shows that grade-blind Record/tag corpora still need separately
  supplied occurrence, commit, fibre, and tag inputs.
- Cycles 364 and 367 supply three formation hypotheses and leave each
  unselected. Cycle 433 compiles only the immediate site-tethered hypothesis.
- Cycle 403 keeps detector/environment labels, sector weights, candidate
  formation, and actualization distinct.
- Cycle 424 constructs the reversible absorption detector and identifies the
  missing coherent detector-to-formation E/G join.
- Cycle 427 constructs the click/no-click instrument from the actual Cycle-424
  unitary. Its scalar class-13 apparatus preparation is deliberately supplied
  and inverse-designed; Cycle 433 preserves that boundary.
- Cycle 430 repeats the physical instrument and constructs only conditional
  branch-indexed histories. It selects no word or numerical law.
- Cycle 370 supplies the connected nearest-neighbor 79-M2 protected carrier,
  its `000/111` occupancy code, signed coordinate codec, finite blank-capacity
  ledger, and exact endpoint decoder.
- Cycle 380 shows that the immediate candidate reaches the protected-capacity
  lane only after conditional formation. It does not supply formation-law
  selection, autonomous predicate genesis, or capacity renewal.

Cycle 433 moves the immediate route one interface inward: the detector is now
a physical gate control and the append target is now the actual protected
carrier format. The local predicate values remain explicit physical input
bits, and their autonomous genesis remains open.

## Declared physical code space

One candidate block contains:

1. one Cycle-427 scalar instrument with its blank detector;
2. one blank 79-M2 Cycle-370 target carrier;
3. raw target-site, 30-M2 payload, predecessor-present, and predecessor-site
   fields;
4. one lawful 79-M2 protected predecessor packet;
5. 30 payload-presence M2;
6. predecessor-ready, fresh-capacity, lawful-payload-certificate,
   faithful-close, and provenance M2;
7. one blank detector bridge and one blank allocation witness; and
8. preallocated blank comparison, conjunction, fanout, and connectivity M2.

The encoder accepts only binary fixed-width values, nearest-neighbor target
and predecessor sites inside the signed seven-bit coordinate domain, one
fixture-lawful proposal payload, one fixture-lawful protected predecessor,
blank work, and a blank allocation witness. The lawful-payload certificate is
checked against the Cycle-342 decoder at the encoder boundary. It is a
supplied local certificate, not an autonomously generated theorem bit.

The source is not already a Record packet. It contains only the raw site,
payload, and predecessor fields. Six output lanes—the three protected
occupancy bits and three compatibility bits—are generated from the accepted
control. The other 73 lanes are copied field-by-field through separate
Toffoli gates into the dedicated output. Decoding never follows a source
reference, address, hash, or pointer.

The output compatibility bits make the packet directly legible to the
Cycle-370 carrier codec. They are supplied adapter metadata. Cycle 433 does
not create a Cycle-368 source-bank member, reciprocal-link history, or a
protected-capacity source bank.

## Fixed local reversible schedule

The output carrier, raw proposal fields, blank-match work, prefix/fanout bus,
protected predecessor packet, scalar controls, detector bridge, and allocation
witness occupy one connected cubic patch. The actual detector is adjacent to
the bridge. Every primitive has support at most three M2 and is X, CNOT, or
Toffoli on a connected nearest-neighbor support.

The fixed schedule is:

```text
actual detector -> blank bridge
compute all-zero target match
conjoin protected predecessor 111
conjoin readiness, freshness, 30 presence bits, lawfulness, close, provenance
conjoin the detector bridge
latch the allocation witness
clean the conjunction workspace
fan out the witness through the blank bus
write all 79 protected packet lanes
clean the fanout bus
actual detector -> clear bridge
```

The target-blank check and allocation witness distinguish newly written
packets from pre-existing occupied packets. A dirty `000` target and a lawful
pre-existing `111` target are both left unchanged. On reverse execution the
packet is first cleared, the blank predicate is rebuilt, the witness is
cleared, and every work M2 returns to zero.

The allocation witness is an invertibility resource. It is not permanence,
occurrence, or an actual-history label.

## Coherent detector join and intertwiner

Let `J` be the Cycle-430 logical-plus-apparatus embedding and let `U_424` be
the physical update. For each physical basis output, the detector bit itself
controls the adjacent bridge CNOT. The rest of the formation schedule is
identical in click and no-click sectors.

The coarse comparator uses the independently extracted Kraus maps:

```text
K_0 = B_0 U_424 J
K_1 = B_1 U_424 J
```

and applies the Cycle-364 answer separately in each detector sector. On the
complete local controls, no-click gives `blocked:faithful_close` and click
gives one candidate packet with the exact target, payload, and predecessor.
Encoding those answers matches the physical coherent state. Reversing the
formation circuit and then `U_424` returns the embedded apparatus input.

The class-13 click sector and candidate-packet sector have the same squared
norm. That equality is an operator/encoding diagnostic, not occurrence,
probability, a sampling rule, or a frequency statement.

## Train, held, and proper-cubic controls

The compiler is frozen before the held call and tested at:

| case | fixture | target | predecessor | content | output |
|---|---:|---|---|---:|---:|
| train | L=3 | `(5,0,0)` | `(4,0,0)` | 30 M2 | 79 M2 |
| held | L=6 | `(17,-11,5)` | `(16,-11,5)` | 30 M2 | 79 M2 |

For **all 24 proper-cubic frames**, the complete Cycle-342 payload is mapped,
the semantic sites and predecessor are rotated, the micro-layout is rotated,
and the physical apparatus direction is transformed. The output carrier
decodes to the transformed candidate, its protected occupancy remains `111`,
the inverse is exact, and every gate support remains connected nearest
neighbor. The signed coordinate field is re-encoded under the frame action;
it is not treated as a scalar lane label.

The resource width and gate word are independent of L, semantic target
coordinate, payload value, detector branch, and proper-cubic frame. This is
constant overhead per declared candidate cell, not a resource-optimality
statement.

## Exact executable results

The complete runner cold execution reports `PASS 7`, `FAIL 0`, and
`PHYSICAL_DETECTOR_TO_PROTECTED_RECORD_FORMATION_COMPILER_CERTIFIED`.

| executable diagnostic | result |
|---|---:|
| cold execution | `7 pass / 0 fail` |
| maximum forward `E_433 G_coarse - G_physical,433 E_433` residual | `0.0` |
| maximum enlarged physical inverse residual back to the encoded input | `4.775375822671983e-16` |
| click-sector / candidate-packet sector weight | `0.3900000000000006 / 0.3900000000000006` |
| maximum branch-weight disagreement | `0.0` |
| maximum nominal workspace leakage | `0 M2` |
| proper-cubic frames | `24` |
| train/held/frame packet cases | `48` |
| maximum apparatus frame residual | `2.172217384091364e-16` |
| maximum effect frame residual | `7.850462293418876e-16` |
| payload-map / packet / rotated-inverse / rotated-support failures | `0 / 0 / 0 / 0` |
| added compiler M2 | `468` |
| joined scalar-instrument plus compiler patch | `484 M2` |
| target / proposal / protected-predecessor widths | `79 / 73 / 79 M2` |
| fixed compiler layers, excluding detector load/unload | `480` |
| primitive gates, including detector load/unload | `1,028` |
| maximum primitive support | `3 M2` |
| connected-nearest-neighbor support failures | `0` |
| independently cleared formation controls | `8 / 8` |
| physical detector deletion candidate-sector weight | `0.0` |
| load-bearing payload / occupancy / allocation gate deletions | `3 / 3 visible` |
| single protected-occupancy-bit fault rejections | `3 / 3` |
| malformed or unlawful domain refusals | `9 / 9` |
| dirty target / preoccupied target refusals | `2 / 2` |

The inverse number is the numerical residual for the enlarged reversible
physical evolution after uncomputing the candidate packet and applying the
inverse Cycle-424 update. The Cycle-364 append predicate itself remains a
conditional semantic comparator; this table does not relabel it as a selected
reversible framework law. Likewise, `0.39` is the deliberately prepared
class-13 sector norm, not occurrence or actualization.

## Detector, payload, and control deletions

The runner exercises **detector, payload, and control deletions** separately:

- deleting the physical detector coupling from the Cycle-424 update removes
  every click-controlled candidate sector;
- omitting the detector-to-bridge gate leaves the target blank;
- clearing any one of predecessor protection, predecessor readiness,
  freshness, payload presence, payload-lawful certificate, faithful close, or
  provenance leaves the target blank with clean work;
- deleting one load-bearing payload-write gate produces a visible content
  mismatch or malformed protected packet;
- deleting one occupancy write produces a non-code `011` packet rejected by
  the Cycle-370 decoder;
- deleting the allocation-witness latch leaves the target blank; and
- flipping any one of the three protected occupancy M2 after a nominal write
  is rejected by the Cycle-370 repetition constraint.

The physical target-blank test also refuses both dirty and occupied inputs.
The dirty `000` word remains visibly malformed; an already occupied lawful
packet remains bit-for-bit unchanged with allocation witness zero.

Malformed widths, nonbinary controls, non-neighbor sites, coordinate overflow,
unlawful payloads, malformed target words, dirty compiler work, and nonbinary
detector inputs are rejected at the declared domain.

## Supplied / derived / open

Supplied:

- the Cycle-427/Cycle-430 scalar apparatus preparation, actual Cycle-424
  update, and blank detector;
- the Cycle-342 lawful payload fixture, decoder, and frame action;
- the Cycle-364 formation hypothesis and local predicate interfaces;
- one lawful protected predecessor and one blank Cycle-370 target carrier;
- raw coordinate/content/predecessor fields, presence word, local predicate
  values, and compatibility metadata; and
- the bounded micro-layout, blank work M2, frames, and fixed circuit.

Derived here:

- a uniform coherent detector-controlled formation permutation;
- a full independent 79-M2 protected candidate packet, written field by
  field rather than represented by a pointer;
- exact branchwise Cycle-364 site/content/predecessor agreement;
- exact `E_433 G_coarse = G_physical,433 E_433` and inverse;
- exact train/held and all-frame behavior; and
- explicit detector, payload, capacity, control, dirty-state, and malformed-
  domain diagnostics.

Open:

- selection of the Cycle-364 formation hypothesis;
- autonomous generation of payload, close, readiness, provenance,
  predecessor, fresh capacity, and compatibility metadata;
- admission of a coherent candidate packet as one framework Record;
- irreversible permanence, a new dependency edge, and an actual member;
- detector-outcome actualization, occurrence, sampling, realized history,
  and frequency;
- concurrent allocation, renewal, and full-lattice deployment; and
- numerical-law selection, metric time, calibrated source, and gravity
  response.

No formation law or detector branch is selected. The output remains a
reversible candidate packet on every coherent branch.
