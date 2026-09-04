# Onsite-alphabet-closed frame rail — Cycle 104

Date: 2026-07-15

Authority: none

This is an authority-free construction audit with no independent audit verdict.
It does not alter Cycle 102, the selected-law state, the queue, the registry,
policy, or foundation.

Companion runner:

```text
scripts/onsite_alphabet_closed_frame_rail_cycle104_2026_07_15.py
```

## Result

Cycle 102's generated-endpoint geometry survives an exact onsite-role repair.
Its unmodified Cycle-52 rail uses 48 phase labels, of which 34 are outside the
current 153-role `FULL_ROLES` alphabet. The old `22 PASS / 0 FAIL` runner is
therefore a valid symbolic construction witness, but its literal `B/C/D`
labels are not a strict-compiler implementation.

There are exactly 36 `B/C/D` phase roles and exactly 36 live roles absent from
the Cycle-100 source. A tempting bijection between those two sets cannot work
as a pure relabel of the fixed Cycle-102 geometry. The absent pool contains
`R_LC`, whose existing one-parent row writes `R_A31`. Every non-launch phase
site exposes at least one open unary target other than the intended next rail
site, so placing `R_LC` there enables a parasite. Each of the three launch
sites exposes the intended next rail site itself; placing `R_LC` there demands
`R_A31`, which is neither the mapped `B/C` successor from the absent pool nor
the fixed `D -> A` successor. Thus:

```text
EXACT_ABSENT_POOL_PURE_RELABEL = obstructed
scope = fixed Cycle-102 geometry + unchanged Cycle-100/Cycle-52 rows
cause = forced use of R_LC
```

This is not a no-go for a guarded cage, a new tolerance row, a different rail,
or reuse of already-present roles. The last route works. Remove the two
unary-active absent roles `R_LB` and `R_LC`, and replace them with `B0` and
`L10`. Both are current onsite roles and neither has a one-parent row. The
result is an injective 36-role phase code and leaves all 48 `A/B/C/D` phase
roles distinct. It is **onsite-alphabet closed** but **not globally fresh**:
the Cycle-100 source already has two `B0` records and nine `L10` records.
Those eleven sites are therefore treated as possible alias debris and tested,
not ignored.

The exact relabel is:

| Cycle-52 role | Onsite role | Cycle-52 role | Onsite role |
|---|---|---|---|
| `B_1_2` | `B_1_2` | `B_0_2` | `B_0_2` |
| `LAUNCH_B` | `R_B40` | `LAUNCH_C` | `R_C22` |
| `LAUNCH_D` | `R_C12` | `B_0_0` | `R_C10` |
| `B_0_1` | `R_B20` | `B_1_0` | `R_B33` |
| `B_1_1` | `R_C02` | `B_2_0` | `R_B32` |
| `B_2_2` | `R_C00` | `B_3_0` | `R_C20` |
| `B_3_1` | `R_C40` | `B_3_2` | `R_B41` |
| `C_0_0` | `B0` | `C_0_1` | `R_C11` |
| `C_0_2` | `R_C13` | `C_1_0` | `R_B23` |
| `C_1_2` | `R_C30` | `C_2_0` | `R_C01` |
| `C_2_1` | `R_B21` | `C_2_2` | `R_B13` |
| `C_3_0` | `R_B01` | `C_3_1` | `R_B31` |
| `C_3_2` | `R_B30` | `D_0_0` | `R_B02` |
| `D_0_1` | `R_C23` | `D_0_2` | `R_C41` |
| `D_1_0` | `R_B10` | `D_1_1` | `R_B12` |
| `D_1_2` | `L10` | `D_2_0` | `R_C33` |
| `D_2_2` | `R_C32` | `D_3_0` | `R_B11` |
| `D_3_1` | `R_C21` | `D_3_2` | `R_B00` |

## Forced fixed points and adapter census

Two identities are forced if the current mixed table is held fixed:
`B_1_2 -> B_1_2` and `B_0_2 -> B_0_2`. The third renewed-rail write occurs
beside old `W1` debris. Its exact signature is:

```text
A_0_2 + B_1_2 + W1 -> B_0_2
```

This is the pre-existing Cycle-59 tolerance row already carried by Cycle 100;
it is the sole non-rail provider consumed by 96 renewed-rail appends. Swapping
either identity with another mapped phase role fails by that third write unless
a new W1-polluted adapter is added. No such row is added here.

The provider census is exact:

```text
95 writes  remapped Cycle-52 rail row
 1 write   pre-existing W1-polluted Cycle-100 adapter
 0 writes  overlapping providers
 0 writes  additional debris adapters
```

`R_LB` is omitted conservatively because it also has an existing unary row,
`R_LB -> R_C22`. The present proof does **not** show that every mapping which
retains `R_LB` fails. One explicit keep-`R_LB` candidate failed at rail write
13 through an extra `R_C32` frontier; that is a failed candidate, not a general
obstruction. Only forced use of `R_LC` proves the exact-absent-pool result.

## Executable coverage

The relabelled rail contributes 1,080 single-valued raw inputs. Its input set
is disjoint from Cycle 100's 5,444 inputs, so the 6,524-input mixed table is
single-valued. Every input and output content lies in the exact 153-member
`FULL_ROLES` alphabet.

The runner then checks:

- all `11 x 97 = 1,067` code-prefix by rail-prefix states through eight full
  rail slices;
- the exact ninth-slice start after the 96th rail append;
- every enabled remapped row against all two `B0` and nine `L10` source-debris
  sites, with zero debris participation;
- all `11 x 13 x 24 = 3,432` first-slice asynchronous states under every
  proper-cubic rotation;
- all `6,524 x 24 = 156,576` rotated raw-table images; and
- the resulting `1,067 x 24 = 25,608` rotated eight-slice state theorem by
  exact table covariance.

This closes `ROLE_CLOSED_FRAME_RAIL_REMAP` at the same bounded construction
grade as Cycle 102. It does not yet prove that reuse of `B0/L10` is harmless
for every unbounded mixed history, every future macroblock, or every possible
multi-contact arrangement. The next construction interface remains:

```text
READY_ROW_TO_RAIL_PAYLOAD_BIND
```

The frame still grows beside the physical row; it does not yet consume the
stored bits and `READY`, route the selected payload, or gate a working
comparator launch.

## N1–N8 no-go-discipline gate

The negative statement governed here is deliberately narrow:
`EXACT_ABSENT_POOL_PURE_RELABEL` fails for the fixed Cycle-102 geometry and
unchanged mixed rows. The positive statement is the bounded role-closed
repair above.

### N1 — Alternative-route enumeration

| Route | Marker | Attempt and result |
|---|---|---|
| Keep the literal Cycle-52 phase labels | `ATTEMPTED` | The Cycle-89/Cycle-100 alphabet census finds 34 foreign labels, so this preserves symbolic renewal but fails onsite closure. |
| Map bijectively to the exact 36 source-absent roles | `ATTEMPTED` | The exhaustive first-occurrence exposure census places the unavoidable `R_LC` either at an extra unary opening or at a launcher with the wrong `R_A31` successor; no placement survives. |
| Replace both unary-active roles with source-present unary-inert roles | `ATTEMPTED` | The explicit `B0/L10` mapping lands all 1,067 product states and all rotation checks; this bypasses, rather than contradicts, the exact-pool obstruction. |
| Remove only `R_LC` and retain `R_LB` | `ATTEMPTED` | One explicit candidate reaches write 13 and then exposes an extra `R_C32`; the route remains unexhausted and no general negative is claimed. |
| Reassign either W1-contact role instead of holding the two identities fixed | `ATTEMPTED` | Both controlled swaps fail by write three against the Cycle-59 `A_0_2 + B_1_2 + W1` tolerance signature; adding a new adapter would be a different-table route. |
| Break the repair through code/rail ordering or orientation | `ATTEMPTED` | All 1,067 asynchronous prefix pairs, all 3,432 rotated first-slice states, and all 156,576 rotated raw images agree exactly. |

Guarding `R_LC` with a cage, changing its unary row, or designing a different
rail remain live routes outside the pure-relabel statement. Their existence
is why the claim is not phrased as a universal alphabet no-go.

### N2 — Wall-independence audit

Alphabet closure is retired by this bounded repair and is not counted again.
The downstream residuals are:

- `W_G`: unbounded/global alias safety for source-present `B0/L10` reuse;
- `W_P`: `READY_ROW_TO_RAIL_PAYLOAD_BIND`; and
- `W_L`: promotion from an extensional candidate-law table to a selected
  complete law.

| Pair | Closing first closes second? | Closing second closes first? | Independent? |
|---|---:|---:|---:|
| `W_G`, `W_P` | no | no | yes |
| `W_G`, `W_L` | no | no | yes |
| `W_P`, `W_L` | no | no | yes |

No wall collapses into another. None is a premise of the bounded result: each
marks a larger-resolution or downstream claim not made here. The exact-pool
obstruction is also not inflated into a residual, because the safe-pool route
already bypasses it.

### N3 — Hidden-wall scan

The note and runner were scanned for “we assume,” “by construction,” “as is
standard,” “the framework provides,” “bridge context,” “background,”
“naturally,” “obviously,” “standard QFT,” “registered,” and “canonical.” No
load-bearing occurrence supplies an unstated premise. The actual inputs are
named explicitly: Cycle 100's source and mixed table, Cycle 52's rail rows and
geometry, Cycle 89's `FULL_ROLES`, the 36-entry relabel, and the bounded prefix
horizon. `B0/L10` reuse and the W1-polluted adapter are exposed as tested
contacts, not hidden as “context.” No additional wall is promoted by this
scan.

### N4 — Residual matching

| Witness | Witness residual | Present use | Match? |
|---|---|---|---:|
| `SELF_EXTENDING_FRAME_CAGE_RAIL_CYCLE52_NOTE_2026-07-14.md:25-57` | autonomous role-distinct four-phase renewal from a supplied slice | supplies the geometry and 1,080-row symbolic rail being relabelled | yes |
| `FOUR_OPEN_RESERVATION_COMB_CYCLE59_NOTE_2026-07-14.md:178-191` | commuting `W1/B_0_2` boundary contact | identifies the exact third-write tolerance row and fixed labels | yes |
| `LIVE_EIGHT_BIT_PHYSICAL_COMPARATOR_CYCLE89_NOTE_2026-07-15.md:13-21` | current 153-role live compiler alphabet | supplies the exact closure alphabet, not rail renewal | yes |
| `ZERO_BINARY_SOURCE_ENDPOINT_MACROBLOCK_BIND_CYCLE100_NOTE_2026-07-15.md:20-29,78-85` | generated 254-record endpoint and 5,444-row mixed law | supplies the exact source debris and base table | yes |
| `GENERATED_ENDPOINT_AUTONOMOUS_FRAME_RAIL_CYCLE102_NOTE_2026-07-15.md:8-51` | composes code and symbolic rail, leaving role remap and payload bind | exact role-remap residual audited here; payload bind remains | yes |

No witness about payload transfer is cited as evidence for alphabet closure,
and no alphabet result is cited as evidence that the payload bind has landed.

### N5 — Rhetoric and resolution audit

The claim “onsite-alphabet closed” is tested at these resolutions:

| Resolution | Tested? | Result |
|---|---:|---|
| per phase role | yes | all 36 mapped injectively; all 48 phase roles remain distinct |
| per rail row | yes | 1,080 single-valued rows |
| complete mixed table | yes | 6,524 single-valued inputs; every content in `FULL_ROLES` |
| bounded async state | yes | 1,067 exact fronts through eight slices |
| proper-cubic image | yes | 3,432 state images and 156,576 row images |
| arbitrary unbounded mixed history | no | not claimed |
| arbitrary future macroblock/multi-contact placement | no | not claimed |

Accordingly, “not globally fresh” is kept explicit. The result is not called
globally alias-free, unbounded compiler closure, a working harness, or a
selected-law theorem.

### N6 — Partial-closure and axiom scan

The operative closure is a finite codebook relabel plus local conflict audit.
It requires no new physics, import, primitive, record sort, read rule, clock,
formation mechanism, or axiom. The existing Record/Lattice/Quantum baseline
neither chooses the map nor blocks it; the map is implementation data for a
candidate local law. A cage or tolerance-row repair would likewise be a local
construction route, not automatically a constitutional amendment. Therefore
no axiom addition follows from either the narrow obstruction or its repair.

### N7 — Steelman

A hostile reviewer should reject any broader no-go: `R_LC` is fatal only
because the fixed geometry exposes a unary opening and the unchanged base law
already maps that role to `R_A31`. One extra occupied cage site, a guarded
local signature, or a changed tolerance row could consume the exact absent
pool. The same reviewer should also reject an unbounded positive claim: eight
slices cannot exclude a later `B0/L10` alias created by a new macroblock or a
second rail contact. Those routes are real, so the shipped result is only the
fixed-geometry pure-relabel obstruction plus the stated bounded repair.

### N8 — Cross-cycle echo

Cycle 52 already showed that a scalar/two-phase presentation could fail by a
rotated-parent alias while a role-distinct four-phase encoding repaired it.
Cycle 59 repaired a real boundary collision with two explicit commuting
tolerance rows, not a new axiom. Cycles 89 and 100 then made the live role
alphabet and endpoint debris explicit enough to test rather than assume.
Cycle 104 uses the same two repair mechanisms—finite role refactoring and an
already-explicit local adapter—and therefore does not convert a codebook
problem into a foundation claim. The echo also warns against overreach: as in
those cycles, bounded local compatibility does not itself select the complete
law or prove every future composition safe.

No-go discipline status: `PASS` for the narrow
`EXACT_ABSENT_POOL_PURE_RELABEL` statement; broader alphabet and rail no-go
statements are explicitly withheld.

## Constitutional disposition

No foundation edit is made and no axiom addition follows. Cycle 104 is an
authority-free bounded construction/audit artifact. It weakens the case for
adding read-, witness-, clock-, storage-, or formation-locking language to the
Record axiom: this compiler gap is closed by an explicit finite relabel and
local-context check. The dormant complete-law identity question remains
separate and untouched.
