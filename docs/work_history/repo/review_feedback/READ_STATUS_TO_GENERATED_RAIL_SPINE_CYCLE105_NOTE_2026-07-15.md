# Read Status to Generated Rail Spine — Cycle 105

Date: 2026-07-15
Authority: none
Disposition: bounded constructive result; runner and review note only

## Result

`READ_STATUS_TO_GENERATED_RAIL_SPINE` is **CLOSED** on the exact Cycle-100 / Cycle-101 endpoint.

Starting with the exact 264-record Cycle-100 terminal and no Cycle-105 static
records, one finite proper-cubic table does all of the following:

1. grows a role-closed shell from the already-generated Cycle-52 A slice;
2. reads Cycle 101's literal physical `OUTPUT` and its `CERT`-derived type;
3. makes the first status/rail join only when those two read-side records and
   the generated rail-spine tip are simultaneously present; and
4. writes a first physical typed payload cap whose onsite content is literally
   `R_B11`.

The positive reader/spine graph has **5,048 states / 21,426 edges / one
terminal / zero bad fronts**. The rail-locality factor with all prefixes of
eight renewed slices exhausts **489,656 mixed states / 2,562,930 edges**.
Every one-bit corruption, wrong `VALID`, and wrong `READY` stops before the
join and payload. All proper-cubic images remain live.

This is a zero supplied static residue result. The generated A slice is not a
Cycle-105 supply: all twelve A records plus `BACKSTOP` were already records in
the exact Cycle-100 terminal.

## Exact source and role alphabet

The source is exactly:

```text
Cycle-100 terminal records     264
Cycle-105 supplied records       0
```

Cycle 108 is consumed directly for the integrated rail alphabet:

- `ROLE_MAP`
- `REMAPPED_RAW`
- `INTEGRATED_RAW`
- `NINE_SLICES`

Cycle 108 retains Cycle 104's 36-role injective B/C/D map except for the exact
two substitutions needed for simultaneous life with Cycle 101:

| Abstract phase role | Cycle-104 content | Integrated content |
|---|---|---|
| `C_3_1` | `R_B31` | `J2` |
| `D_1_1` | `R_B12` | `J1` |

The need is executable, not cosmetic. Cycle 101 has exactly two unary reader
rows with those inputs:

```text
R_B31 -> R_B32
R_B12 -> R_B13
```

With Cycle 104's original map, rail prefix 16 exposes its lawful
`(-3,0,3) -> R_B01` record and two unlawful `R_B32` images at `(-4,1,3)` and
`(-3,1,4)`. The `J1/J2` repair removes those aliases. Both replacements are
already-live onsite roles, have no unary input rows in the pre-rail union, and
preserve a 36-role injection inside `FULL_ROLES`.

The exact table census is:

| Surface | Canonical rows | Raw proper-cubic rows |
|---|---:|---:|
| Cycle 100 + Cycle 101 + repaired rail | — | 6,896 |
| Cycle-105 spine/join/payload | 18 | 414 |
| complete union | — | 7,310 |

The new raw domain is disjoint from the integrated 6,896-row domain; every
raw input is single-valued; every input and output content belongs to the
153-role live onsite alphabet.

## Bare-metal construction

### 1. Reverse rail shell

The shell grows from the generated rail toward the readout, not from the
readout toward a remote label. That direction is load-bearing: the final join
can then literally see a persistent rail descendant and the literal read-side
records in one nearest-neighbour signature.

The shell uses sixteen generations and seventeen physical writes:

| Generation | Target(s) | Output |
|---:|---|---|
| 0 | `(0,0,3)` | `AUXZ` |
| 1 | `(1,0,3)` | `C_Q` |
| 2 | `(2,0,3)` | `BTP` |
| 3 | `(2,-1,3)` | `L3` |
| 4 | `(3,-1,3)` | `ARM` |
| 5 | `(3,-1,2)` | `W1` |
| 6 | `(3,-1,1)` | `AUXY` |
| 7 | `(3,-1,0)` | `R_A31` |
| 8 | `(4,-1,0)` | `OPEN_B` |
| 9 | `(4,0,0)` | `MARK` |
| 10 | `(4,1,0)`, `(4,0,1)` | `P2` |
| 11 | `(4,2,0)` | `OY` |
| 12 | `(4,3,0)` | `TZ` |
| 13 | `(4,4,0)` | `J3` |
| 14 | `(4,5,0)` | `AUX` |
| 15 | `(4,6,0)` | `BTG` |

The first target has the exact signature `A_3_0 + H0`. `A_3_0` is the
persistent generated-rail record at `(-1,0,3)`. Every later primary target
contains its predecessor plus old endpoint support. Generation 10 has two
equal proper-cubic images. Treating the second as debris or selecting only one
would choose an axis outside the local law; both `P2` records are therefore
part of the physical shell. They are simultaneously enabled by the same local
row, neither is supplied, either may append first, and every terminal contains
both.

### 2. Inherited certificate type

Cycle 108's repaired rail table contains the exact unary row required by the
read-side certificate:

```text
CERT (3,5,1) = R_B40
             |
             v
TYPE (4,5,1) = R_B21
```

At `(4,5,1)`, `CERT` is the only occupied neighbour. The type is not supplied
and is not a new Cycle-105 row. It is an existing proper-cubic instance of the
role-closed rail law. A wrong literal word never reaches `CERT`, so it never
grows this type.

### 3. Literal three-parent join

The first record joining the two causal branches is:

```text
JOIN (4,6,1) -> JOINT
```

Its complete exact signature is:

| Parent site | Content | Meaning |
|---|---|---|
| `(3,6,1)` | `H1` | literal Cycle-101 `OUTPUT` |
| `(4,5,1)` | `R_B21` | grown `CERT`-derived type |
| `(4,6,0)` | `BTG` | persistent generated-rail spine tip |

Removing any one parent removes the table row. The exhaustive graph also
shows that no asynchronous schedule writes `JOIN` before all three parents
exist. This is the requested bare-metal bind: no host reads a symbolic status,
chooses a direction, or attaches a supplied harness.

### 4. First typed payload

`JOINT` has three remaining sole-parent open neighbours. Proper-cubic closure
therefore grows all three images:

```text
(4,6,2) -> R_B11
(4,7,1) -> R_B11
(5,6,1) -> R_B11
```

This is a typed payload cap, not yet a selected directed payload rail. Its
content is literally the role named by the eight-bit word read in Cycle 101:
`R_B11 = 10010100`.

## Exhaustive asynchronous result

The reader/spine state tracks:

- every reachable subset of Cycle 101's 22 records;
- the inherited type;
- all sixteen ordered shell generations;
- either ordering of the extra `P2` cap image;
- the literal three-parent join; and
- all subsets of the three payload images.

The runner recomputes the full exact nearest-neighbour frontier at every
state. It does not merely replay the declared path.

```text
reader/spine states       5,048
reader/spine edges       21,426
terminals                     1
bad fronts                    0
premature joins               0
```

At the one terminal, the only frontier is the first repaired-rail record.

The runner then grows 96 rail writes—eight full slices—against the completed
reader/spine under the same 7,310-row law. Every prefix has exactly one lawful
rail frontier, and prefix 96 exposes only the ninth-slice start.

The complete async product factors exactly. Reader/spine and renewed-rail
variable sites have minimum L1 distance two, and their only common-neighbour
target is `A_3_0`, which is already occupied permanently in the source. Hence
neither factor can alter an open local signature of the other. Both factors
are exhausted under the same full raw table, so their Cartesian schedule
product is exact:

```text
states = 5,048 x 97 = 489,656
edges  = 21,426 x 97 + 5,048 x 96 = 2,562,930
```

## Fail-closed controls

The rail-descended shell is allowed to grow on a wrong word. It stops two
primary sites short because its final approach requires the inherited
`CERT`-type. More importantly, neither `JOIN` nor any payload image is ever
reachable.

| Flipped literal bit | Reader/spine states | Edges | Join | Payload |
|---:|---:|---:|---|---|
| 0 | 760 | 2,274 | no | no |
| 1 | 680 | 2,022 | no | no |
| 2 | 600 | 1,770 | no | no |
| 3 | 440 | 1,186 | no | no |
| 4 | 120 | 238 | no | no |
| 5 | 200 | 490 | no | no |
| 6 | 80 | 152 | no | no |
| 7 | 60 | 109 | no | no |

The bit-5 history-mixed `H1` reject poison remains explicit. Wrong `VALID`
has 40 states / 66 edges; wrong `READY` has 20 states / 23 edges. Each has one
stopped terminal and no join or payload.

All corrupt products retain the independent 97-state eight-slice rail factor,
but no rail schedule can supply the missing literal read parents because the
only common target is already occupied.

## Covariance and permanence controls

- All `7,310 x 24 = 175,440` raw proper-cubic image checks preserve output.
- The positive terminal, eight bit-corrupt terminals, wrong `VALID`, and wrong
  `READY` were each transformed under all 24 proper-cubic rotations: 264
  complete terminal controls, all exposing only the rotated ninth-slice start.
- Old Cycle-100, Cycle-101, A-slice, shell, join, payload, and eight-slice rail
  records stay present. No overwrite or deletion operation exists.
- The complete law remains closed on `FULL_ROLES`.

## Claim boundary

Cycle 105 closes exactly:

```text
READ_STATUS_TO_GENERATED_RAIL_SPINE
ZERO_SOURCE_LITERAL_OUTPUT_TO_FIRST_TYPED_PAYLOAD_CAP
```

It does not close the complete reusable harness. Specifically, the symmetric
three-image `R_B11` cap has not yet been converted into a selected renewable
payload direction, and no complete 48-bit candidate/reference
compare-select-write pass is claimed here.

The next constructive surface is:

```text
TYPED_PAYLOAD_CAP_TO_REUSABLE_HARNESS
```

That name is a work target, not a no-go and not an axiom request. Cycle 105
does not prove global minimality of 17 shell writes, 18 canonical rows, or
three payload images.

## N1–N8 no-go discipline gate

The current `origin/main` no-go-discipline skill was used because this note
ships a bounded positive with an explicit residual. Result: **PASS only for
the narrowed partial-positive wording; no no-go is shipped.**

### N1 — Alternative route enumeration

| Route | Status | Result |
|---|---|---|
| Direct `R_B21 + H1` pair join after inherited type | ATTEMPTED | A one-bit corrupt state exposes the same pair at `(1,6,1)`; using it either writes a parasite or repairs the corrupt reader and false-accepts. Rejected. |
| Forward `CERT/OUTPUT -> A_3_0` thin shell | ATTEMPTED | A 16-site route works geometrically, but the final record only sees a status descendant plus A. It is weaker than a literal read-side final join. |
| Distinct `CERT` tag + status join + three-image turn cap | ATTEMPTED | It closes locally and fail-closes, but adds a cap before the long shell. The reverse shell gives the requested literal final join with fewer new canonical rows. |
| Reverse `A_3_0 -> OUTPUT` shell | ATTEMPTED | Selected. It puts the rail descendant, literal output, and certificate type in one exact final signature. |
| Unmodified Cycle-104 role map | ATTEMPTED | Executably fails at renewed-rail prefix 16 through the `R_B31/R_B12` unary aliases. |
| Exact two-role integrated remap | ATTEMPTED | Selected via Cycle 108; eight slices and the full mixed product pass. |

These routes defeat any universal negative claim. The result is therefore a
selected positive construction, not “no route exists.”

### N2 — Wall-independence audit

Only one residual is retained: turn the symmetric typed cap into a complete
reusable compare-select-write harness. “Choose a payload direction” and “run
the complete harness” are ordered stages of that one construction, not two
independent walls; the first is consumed by the second. No inflated wall count
is claimed.

### N3 — Hidden-wall scan

The note and runner were scanned for `assume`, `by construction`, `standard`,
`framework provides`, `bridge context`, `background`, `naturally`,
`obviously`, `registered`, and `canonical`.

- `canonical` refers only to the executable proper-cubic signature quotient;
  it contributes no supplied physical record.
- `construction` refers to the explicit finite record list and table builder;
  every append is rechecked against the full frontier.
- No `assume`, “standard physics,” background apparatus, or hidden supplied
  harness is load-bearing.

No hidden condition was promoted.

### N4 — Residual matching

| Witness | Witness residual | Cycle-105 use | Match |
|---|---|---|---|
| `ZERO_SOURCE_RELATIONAL_FIRST_HARNESS_CYCLE101_NOTE_2026-07-15.md` | `READ_STATUS_TO_GENERATED_RAIL_SPINE` | exact residual closed here | yes |
| `FRAGMENT_SAFE_ROLE_REMAP_TYPE_INTEGRATION_CYCLE108_NOTE_2026-07-15.md` | reader-safe role remap and inherited type through eight slices | exact rail/type input consumed here | yes |
| `ONSITE_ALPHABET_CLOSED_FRAME_RAIL_CYCLE104_NOTE_2026-07-15.md` | role closure against Cycle 100 alone | cited only as the pre-integration map, not as reader-safe authority | no; narrowed |
| `SELF_EXTENDING_FRAME_CAGE_RAIL_CYCLE52_NOTE_2026-07-14.md` | renewable role-coded slice mechanism | supports rail recurrence only | yes, for recurrence only |

No mismatched witness is used to support complete-harness closure.

### N5 — Rhetoric audit

The only negative phrase is the scoped statement that Cycle 105 does not
close the complete reusable harness. The tested resolutions are per-site,
per-local-signature, per-bounded reader/spine block, and the eight-slice mixed
product. An unbounded complete compare-select-write machine was not tested;
the note therefore makes no lattice-wide impossibility statement.

### N6 — Partial-closure path scan

The residual has an explicit constructive path: use the three generated
`R_B11` images as the next local cage/selection surface, bind one image to a
renewed rail phase, and then consume the already-tested comparator/writer
blocks. This needs a runner, not a convention, primitive, import, or new axiom.
No foundation-content conclusion follows from this engineering residual.

### N7 — Steelman

A hostile reviewer should say: “You have already paid for a proper-cubic
three-image `R_B11` cap beside a unique literal three-parent join, while the
repaired rail renews for eight slices under the same law. One cap image can be
caged by the existing shell/rail occupancy and made the directed launch for
the previously tested comparator/writer. Therefore the remaining harness may
be a short constructive extension, and any suggestion that a new principle or
structural obstruction is needed would be premature.” This steelman is strong;
accordingly no no-go is claimed and `TYPED_PAYLOAD_CAP_TO_REUSABLE_HARNESS` is
the next target.

### N8 — Cross-cycle echo

Cycle 101's disconnected thin-surface residual was retired by reversing the
growth direction and accepting proper-cubic cap multiplicity. Cycle 104's
later-slice collision was retired by an exact two-role remap in Cycle 108.
Both are examples of apparent walls closed by a local constructive reframing,
not an axiom. The same mechanism—cage the symmetric cap and continue—is
explicitly retained for the next cycle.

## Authority and repository effects

This note and its runner have authority `none`.

- No foundation edit.
- No axiom addition.
- No primitive or import registration.
- No audit verdict.
- No queue edit.
- No policy edit.
- No commit, push, or pull request.

The only Cycle-105 artifacts are this note and
`scripts/read_status_to_generated_rail_spine_cycle105_2026_07_15.py`.
