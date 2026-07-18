# Actual five-port `R_LB` macrostep adversarial audit — Cycle 99

Date: 2026-07-15  
Authority: none

## Result up front

Cycle 97 independently reruns at `24 PASS / 0 FAIL`.  Its important bounded
positive survives: the five occupied words are five separated physical face
blocks, not a flattened 48-bit candidate stream; the absent `+x` site grows an
EMPTY word; the distributed equality scan selects the real `R_LB` row; and the
written value is physically read through eight taps before MATCH starts the
next comparator.  No host decoder performs that transition.

The claim needs three explicit qualifications.

1. Cycle 97 does not physically establish the word **provenance** implied by
   “five validated macroblocks.”  It supplies five correct H0/H1 blocks and
   later compares them to supplied references, but it supplies no upstream
   `VALID` or `READY` record for any face.  Correct-valued but unvalidated input
   is accepted.
2. OPEN is absence-sensitive at the initial decision and not afterward.  Every
   one of 153 live contents at the monitored port makes the initial source
   completely quiet.  Once the sensor record forms, a later record at that
   port cannot revoke the cached OPEN certificate; all remaining stages still
   accept the EMPTY slot.
3. `R_LB` is physically consumed **indirectly**: DATA controls the taps, taps
   control MATCH, and MATCH is the next START.  The first eight candidate bits
   in the next comparator are nevertheless a disjoint supplied copy of
   `R_LB`, not the same eight DATA records.

The audit therefore does not edit Cycle 97.  Its disposition is:

```text
BOUNDED_POSITIVE_SURVIVES_WITH_EXPLICIT_QUALIFICATIONS
```

This source note has authority none and issues no independent audit verdict.

## Independent executable result

The Cycle-99 runner returns `38 PASS / 0 FAIL` and checks:

```text
Cycle-97 selected raw union                         5,809
compatible selected-law audit union                6,169
Cycle-97 supplied records                           4,539
Cycle-97 grown appends                              1,162
reachable stages                                   1,163
proper-cubic stage images                         27,912
proper-cubic raw images                          148,056
late-neighbour controls                   880 x 153 = 134,640
occupied/reference corruption controls                48
```

The compatible audit union is the Cycle-94 selected base plus Cycle 97 and the
compatible adapter domains from Cycles 92, 93, and 98.  It deliberately does
not re-import the complete pre-Cycle-94 base tables: those contain the old
`R_LA -> R_B11` association that Cycle 94 explicitly replaced by
`R_LA -> H1 START`.  Combining an old law version and its replacement is not a
“full live union”; it is a known six-image output conflict.  All compatible
adapter rows coexist in the 6,169-row selected-law union with one output per
input.

Every one of the 1,163 base stages has exactly its intended singleton frontier
or the quiet terminal under that union.  Exact closure of all 6,169 signatures
under all 24 proper-cubic rotations then lifts the complete stage result to all
27,912 stage images.  This is a covariance proof, not a sample of rotations.

## 1. Are the five inputs really spatial?

Yes.  The forty occupied bits form five nearest-neighbour connected components
of eight sites each.  Their candidate planes have signed seed-relative offset
24 on the `-x,-y,-z,+z,+y` faces; their equality status and reference planes
have offsets 25 and 26.  Each eight-site component carries exactly the live
codeword for its face role:

```text
-x  R_A22
-y  R_B12
-z  R_B21
+z  R_B23
+y  R_B32
```

The scan takes control to those five blocks in direction order and reads the
bits in place.  It never creates or supplies one contiguous 40- or 48-bit copy.
This closes the “flattened/symbolic bypass” attack for this one row.

What it does not close is provenance.  At source time the forty face bits,
their forty reference bits, and their cages are present; all forty face-status
sites are open.  No face has a separate record saying that an upstream word
finished, decoded, and became READY.  The later equality status proves “these
bits equal this row's supplied reference,” not “these bits were produced by a
validated predecessor macroblock.”

That distinction is required by the Cycle-91 `P_RLB_5` phrase “source begins
with five validated occupied-neighbour words” and by Cycle 96's
`STEP_NEIGHBOUR_STREAM` failure control on unvalidated data.

## 2. Minimum exact READY-gate repair

The audit constructs, but does not land into Cycle 97, an exact distributed
repair.  At the first status site of each face it:

- repurposes one existing guard site as an H1 `READY` token;
- repurposes the opposite guard as a `JOINT` type marker; and
- adds three `A_0_0` cage records around READY, fifteen new records total.

The five candidate blocks stay at exactly the same sites.  No flattened stream
is introduced.  The repaired source grows from 4,539 to 4,554 supplied records.
Its scan has 9 canonical / 153 raw rows, and its complete compatible union has
6,193 single-valued raw inputs.

All 1,163 stages remain exact.  For each face:

- removing READY stops the scan at that face;
- removing its `JOINT` type marker stops the scan; and
- replacing READY by any of the other 152 live contents leaves no intended or
  parasitic frontier (`5 x 152 = 760` controls).

This is an **INTERFACE-REPAIR-POSITIVE** result.  An explicit validated-source
type can gate a distributed matcher without flattening its data and without a
new onsite role.  It is not yet the upstream theorem.  The repaired runner
still supplies READY.  Making each actual predecessor word generate READY only
after its own literal codeword and VALID, then routing that READY to the correct
face, is the surviving `READY_PROVENANCE_ROUTE` obligation.

Cycle 100 has now closed the first seam for one actual `R_B11` endpoint:
`10010100 -> VALID -> READY` grows from the generated Cycle-85 boundary with
zero added binary source records.  It does not yet route five such macroblocks
into this `R_LB` cell.  Thus Cycle 100 is a real partial retirement path, not a
license to call Cycle 97's five supplied words validated retroactively.

## 3. Exact OPEN result, including every late schedule

The final EMPTY equality bit is the append at index 879.  The audit evaluates
all 880 states from the initial source through the state immediately before
that append.  At every state it inserts each of the 153 possible record
contents at the monitored `+x` port and recomputes the exact full frontier.

```text
state 0, before sensor:       153 / 153 make the whole source quiet
states 1..879, after sensor:  134,487 / 134,487 preserve the intended frontier
```

So “genuinely OPEN” has an exact two-part meaning here:

- **initial absence-sensitive:** yes;
- **late-arrival-sensitive or revocable:** no.

This is the same bounded-reservation boundary stated honestly in Cycle 86:
the certificate is permanent and cannot revoke itself if an external record is
forced after formation.  In Cycle 97's isolated reachable graph the sensor is
the unique first append and the monitored port is never naturally writable, so
there is no missing internal asynchronous schedule.  A neighbouring apparatus
or a stronger concurrency domain can still create the late-arrival case.

The sensor also requires its forward axial feed site to start open.  Supplying
any live content other than H1 there makes the source quiet; supplying H1 there
bypasses the sensor and starts the next feed site.  This is another exact
reservation condition on the supplied apparatus, not evidence for an axiom.

The narrow classification is therefore:

```text
INITIAL_OPEN_TO_EMPTY                         CLOSED, ONE ISOLATED CELL
LATE_NEIGHBOUR_RESERVATION                    LIVE W_MULTI / MIXED-DOMAIN WALL
```

Whether the correct global law serializes the sensor as a valid causal
snapshot or instead reserves the port until row commitment is selected-law
content.  Cycle 97 proves neither global convention.

## 4. Is the output physically consumed?

Yes, at value-gated causal-input grade.

The writer appends `R_LB=10110001`, then VALID and TURN, and then sweeps back
over all eight DATA bits.  Each TAP is a nearest neighbour of its DATA bit and
its exact local signature requires DATA to equal the supplied readable
reference.  Flipping any one DATA bit at its tap state makes the complete
frontier quiet.  Only after all eight taps does unsupplied MATCH form.

MATCH is literally the transformed START site of the next physical comparator.
Once it forms, the only enabled append is that comparator's first certificate.
The dynamics function consults nearest-neighbour signatures and the raw table;
it never calls a host decoder.  The Python conversion of H0/H1 to a bit tuple is
diagnostic only.

The stronger statement is false for this geometry.  The eight DATA sites and
the next comparator's first eight candidate sites are disjoint.  The latter
are already among the 4,539 supplied records and happen to carry the same
`10110001` word.  Hence:

```text
PHYSICAL_VALUE_TO_MATCH_TO_NEXT_START              CLOSED, ONE ROW
SUCCESSOR_LITERAL_REUSE/ALLOCATION                  LIVE W_STEP WALL
```

Directly reusing the output macroblock, or growing a successor candidate from
it, remains an architectural improvement and part of successor allocation.  It
is not a host-decode defect in the causal MATCH path that Cycle 97 actually
builds.

## 5. Exact supplied/grown recount

The author census is correct and its parts are disjoint:

```text
scan/port/reference/cage source                    4,258 supplied
readable writer source                                89 supplied
next comparator source                               192 supplied
total                                               4,539 supplied

OPEN/distributed scan path                         1,079 grown
writer plus reverse verification                      35 grown
next comparator certificates                          48 grown
total                                               1,162 grown
```

Inside the 4,258-record scan source, 189 records are the five candidate words,
six references, face/OPEN/sensor guards, and center marker; 4,069 are route
cages.  The READY repair adds fifteen cages and changes ten existing guard
contents, yielding 4,554 supplied records overall.  Neither form is seed-grown.

## 6. Disposition by interface

| Interface | Cycle-99 result | Class |
|---|---|---|
| five physical face blocks, no flattened candidate | exact positive | closed bounded interface |
| correct bits equal the one supplied `R_LB` reference | exact positive | closed bounded interface |
| explicit READY can gate each distributed face | exact positive repair | `INTERFACE-REPAIR-POSITIVE` |
| actual predecessors generate and route five READY records | not built; Cycle 100 closes one first seam only | `READY_PROVENANCE_ROUTE`, live `W_STEP/W_BOOT` |
| initial monitored-port absence | 153/153 blockers quiet | closed bounded interface |
| late occupancy after OPEN sensor | all 134,487 controls continue | `LATE_NEIGHBOUR_RESERVATION`, live `W_MULTI`/full-mixed-domain wall |
| written value physically controls next START | exact positive | closed bounded interface |
| same output block is the next candidate; successor source grows | not built | `SUCCESSOR_LITERAL_REUSE/ALLOCATION`, live `W_STEP` |
| 236-row bank, source growth, unbounded phase return, contact | intentionally outside one-row probe | existing `W_BOOT/W_STEP/W_MULTI` project obligations |

## 7. No-go discipline gate

**Gate result: PASS for the narrowed bounded-positive-with-qualifications
claim.**  A broad claim that Cycle 97 is “only a symbolic bypass,” that READY
requires flattening, or that the remaining interfaces require a new axiom is
rejected.  No global impossibility is claimed.

### N1 — alternative-route enumeration

1. **Distributed in-place matcher — ATTEMPTED.**  Attack: check whether the
   five alleged face blocks are one host-packed rail in disguise.  That attack
   fails: the runner finds five disjoint eight-site components on five signed
   face planes and no supplied EMPTY block (`A03-A05`).
2. **Full compatible mixed-union parasite — ATTEMPTED.**  Attack: add the live
   Cycle-92/93 selector adapters and Cycle-98 tap adapter, then search every
   reachable stage.  The attack fails on the selected law: all 1,163 states
   remain exact in the 6,169-row union (`B01-B04`).
3. **READY without flattening — ATTEMPTED.**  Attack: add a physically typed
   readiness gate beside each distributed face.  It succeeds, so the broader
   negative “validation needs a flat stream or axiom” fails; only upstream
   READY provenance remains (`D01-D07`).
4. **Late-neighbour revocation/reservation — ATTEMPTED.**  Attack: insert all
   live contents at every pre-acceptance stage.  Revocation fails after the
   sensor: the exact surviving residual is late contact/reservation, not basic
   initial openness (`B05`, `C02-C04`; Cycle 86 lines 125-134).
5. **Host-decode handoff — ATTEMPTED.**  Attack: corrupt DATA and inspect the
   transition into the next comparator.  The host-bypass allegation fails:
   eight physical taps gate MATCH/START; the stronger literal-reuse route
   remains supplied (`E01-E06`; Cycle 94 lines 99-185).
6. **Surface-generated validated block — ATTEMPTED.**  Attack: grow a real
   codeword plus VALID/READY from the generated boundary.  Cycle 100 is a
   positive one-row instance, so a no-go on provenance is premature; the
   untested route is five-face transport from those READY records.
7. **Prelaid recurrent allocation — ATTEMPTED.**  Attack: test whether repeated
   physical handoff itself forces self-allocation.  Cycle 98 executes repeated
   supplied cells but leaves the exact allocation spine, so it supports only
   the narrow successor-source qualification.

These are seven distinct mechanisms, not seven descriptions of one missing
rail.

### N2 — wall-independence audit

After the READY interface repair, the collapsed load-bearing residual set is:

- `W_V = READY_PROVENANCE_ROUTE`;
- `W_L = LATE_NEIGHBOUR_RESERVATION`; and
- `W_A = SUCCESSOR_LITERAL_REUSE/ALLOCATION`.

| pair | first closes second? | second closes first? | independent at current interface? |
|---|---:|---:|---:|
| `W_V / W_L` | no | no | yes |
| `W_V / W_A` | no | no | yes |
| `W_L / W_A` | no | no | yes |

Generating authenticated READY does not reserve the monitored port; reserving
the port does not authenticate the five words.  Reusing or allocating the next
word does neither automatically.  A monolithic self-hosting cell could still
close all three in one induction, so this table is not a universal mechanism
lower bound.

The missing-token and unflattened-routing phrases are not counted as separate
walls: the exact READY gate closes the first, and the existing spatial scan
closes the second.  This prevents wall inflation.

### N3 — hidden-wall scan

| phrase class | classification |
|---|---|
| “supplied” face words/references/cages/next comparator | explicit load-bearing source boundary; counted exactly |
| “by construction” | not used as proof; every geometry/count has a runner assertion |
| “canonical” signature | mathematical proper-cubic quotient, checked over all 24 images; not a physics admission |
| “registered” / “approved primitive” | cited registry boundary; none supplies READY, cages, late reservation, or allocation |
| “background” / “obviously” / “standard” | not used to carry a step |
| causal snapshot interpretation | explicitly left as selected-law content, not assumed |

The scan promotes validation provenance, late reservation, and successor
allocation to the three explicit residuals above.  No fourth hidden condition
is carried by prose.

### N4 — residual matching

| cited witness | witness residual | Cycle-99 residual | match? |
|---|---|---|---:|
| Cycle 91 lines 407-428 | literal five-port `P_RLB_5` acceptance | exact object audited here | yes |
| Cycle 86 lines 125-134 | isolated port is reserved naturally; external late record cannot be revoked | `W_L` | yes |
| Cycle 94 lines 99-185 | DATA must be re-read; next candidate remains supplied | physical handoff and `W_A` split | yes |
| Cycle 96 lines 184-190 | reject unvalidated input; consume literal output in next physical comparator | `W_V` and stronger `W_A` | yes |
| Cycle 98 sections 3-4 | repeated prelaid cells; exact successor allocation spine remains | `W_A` | yes |
| Cycle 100 result and N8 | one generated word reaches VALID/READY; harness transport remains | partial retirement path for `W_V` | yes |

No formation, probability, clock, gravity, or storage residual is cited as
evidence for these compiler interfaces.

### N5 — rhetoric and resolution audit

- “Spatial, not flattened” is proven for five blocks of this one `R_LB` row;
  it is not generalized to 236 rows or an unbounded lattice.
- “No validation provenance” means no per-face upstream token in Cycle 97;
  it does not deny the equality scan or Cycle 100's one generated READY.
- “OPEN is not late-sensitive” means one monitored site, all 153 contents, and
  states 1 through 879 under the 6,169-row selected union.  It is not a theorem
  about every port, multi-apparatus history, or alternative global law.
- “No host decode” refers to the dynamic transition; Python decoding remains a
  diagnostic assertion.  “No literal reuse” refers to disjoint DATA and next
  candidate sites, not absence of physical causal consumption.
- Rotation is exact at the local-table and complete finite-stage resolutions;
  translation/phase induction and lattice-wide iteration are not claimed.

Every negative phrase is therefore pinned to the narrowest tested resolution.

### N6 — partial-closure paths and approved primitive check

The approved primitive registry and all three primitive source notes were read.
The scale reference supplies units only; kinetic isotropy supplies only
`c_t=c_s` form; realized state supplies pointwise evaluation only.  None
generates READY, reserves a late port, or allocates a successor.

There are concrete import-retirement paths that require no axiom:

1. the Cycle-99 caged READY gate repairs the five-face consumer interface;
2. Cycle 100 grows one actual codeword then VALID then READY;
3. Cycle 52's self-growing rail and Cycle 98's named allocation spine are
   candidate transport/build paths; and
4. a causal snapshot or reservation theorem can close `W_L` inside the exact
   selected law.

Therefore the remaining work is `W_STEP/W_MULTI` local-law construction, not
“new axiom required.”

### N7 — strongest hostile steelman

A hostile reviewer can reasonably argue that Cycle 97 already passes the
original Cycle-91 bounded contract: “validated words” were allowed as supplied
boundary objects, and the equality sweep rechecks every literal bit; once the
OPEN sensor forms, a later neighbour is causally later than the row snapshot,
so preserving EMPTY is correct rather than stale; and P_RLB asked for physical
consumption, which taps-to-MATCH supplies, not same-site word reuse.  On that
reading all three audit findings are scope clarifications, not failures.  This
steelman is strong and is why Cycle 99 does **not** ship a no-go or invalidate
Cycle 97.  It narrows “validated” to supplied-boundary status, names snapshot
semantics as selected-law content, and separates causal value consumption from
literal block reuse.

### N8 — cross-cycle echo

- Cycle 86 first closed isolated OPEN and explicitly retained the late external
  insertion caveat.  Cycle 97 packs that module but does not retire the caveat.
- Cycle 94 replaced a sealed output by a readable tap sweep; a local geometry
  change retired the host-decode/type boundary for one row.
- Cycle 98 shows repeated physical execution on prelaid sources and narrows the
  successor residual to an allocation spine.
- Cycle 100 retires the first binary-source seam by growing one actual word,
  VALID, and READY directly from the endpoint.

These echoes show that similar “missing interface” walls have repeatedly been
retired by local adapter geometry, source growth, and induction—not by adding
formation prose.  The same mechanisms remain live here, so no universal no-go
or constitutional lower bound is asserted.

## Constitutional disposition

No foundation edit is made and no axiom addition follows.  The exact READY
repair, late-neighbour classification, and value-gated handoff are candidate-
law/interface facts downstream of Lattice, Qubit, Admissibility, and Record.
They neither define generic record formation nor supply which record occurs,
with what weight, or at what rate.

The positive constructions continue to weaken proposed Record additions about
reading, a second witness, a clock, or a storage budget: in these finite models
the local append makes a permanent record; later records validate and route its
content without retroactively locking it.  The complete selected law and its
scientific uniqueness/identity gate remain separate.

No queue, policy, registry, foundation, commit, push, or PR change is made.

## Verification

```text
python3 scripts/actual_five_port_open_rlb_macrostep_cycle97_2026_07_15.py
python3 scripts/actual_five_port_open_rlb_macrostep_audit_cycle99_2026_07_15.py
```
