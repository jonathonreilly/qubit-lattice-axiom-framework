# First self-grown selector payload, literal bit-0 instance — Cycle 106

Date: 2026-07-15

Authority: none

This is an authority-free construction audit with no independent audit
verdict. It makes no foundation edit and changes no selected-law, registry,
queue, policy, audit, git, commit, push, PR, or axiom state.

Companion runner:

```text
scripts/first_self_grown_selector_payload_bit0_cycle106_2026_07_15.py
```

## Result

`FIRST_SELF_GROWN_SELECTOR_PAYLOAD` lands against the exact Cycle-108 surface
for one deliberately narrow case: the literal bit-0 instance of the fixed
Cycle-100 word, whose bit is `H1`.
The candidate bit, reference bit, typed arm, cage, comparison status, and
rejection control are all physical grown records. There are zero added
payload/harness source records.

The runner starts from the exact 264-record inherited generated boundary
certified by Cycle 100. Those records are the initial boundary of this runner;
they are not regenerated here, and they are not relabelled as “nothing.” What
is removed is Cycle 95's supplied selector apparatus: no candidate, reference,
arm, cage, status, decision, token, or launch record is present in that
boundary.

The correct causal path is:

```text
C101 literal reader
  -> C101 OUTPUT=(3,6,1)=H1                    grown candidate
  -> C108 CERT_TO_TYPE=(4,5,1)=R_B21           grown TYPE
  -> (4,5,0)=T_H2 -> (4,6,0)=T_H3              grown guarded arm
  -> (4,6,1)=JOINT                              grown compare/join certificate

C101 certificate
  -> (3,5,2)=BACKSTOP                          grown cage
  -> (2,5,2)=T_H0                              grown reference guard
  -> (2,6,2)=H1                                grown reference bit

candidate + reference + cage
  -> (3,6,2)=H1                                grown first-bit status
```

The law adds ten canonical rows, producing 240 proper-cubic raw images. They
are disjoint from Cycle 108's 6,896 raw inputs. The exact 7,136-input union is
single-valued and closed on the current 153-role onsite alphabet.

This is a literal bit-0 instance, not a generic binary selector. In
particular, `H0` at the new reference site is an explicit fault injection
performed only after the lawful `H1` reference frontier exists. It is not a reachable
lawful branch, not an occurrence model, and carries no probability claim.
Under that control the exact path is:

```text
REFERENCE := H0              external typed fault control
  -> STATUS=H0               mismatch certificate
  -> REJECT=AUX              physical rejection record
  -> LAUNCH=A_0_0            exact first rejected-branch launch
```

All 97 rail prefixes expose exactly the appropriate control stage plus the
next rail record. After launch is written, only the next rail record remains.

## What was actually minimized from Cycle 95

Cycle 95 contains 943 supplied records because it realizes two handoffs over
three complete 48-bit cells. An exhaustive search over the translated local
first-bit neighborhood finds a much smaller and exact dependency chain:

| Obligation | Unique minimum supplied subset in Cycle 95 |
|---|---:|
| compare correct `H1` versus wrong `H0` | 5 records |
| write exact mismatch `AUX` | 7 records |
| expose exact first `A_0_0` launch | 9 records |

The five-record kernel is candidate, reference, previous status, and two
`BACKSTOP` records. The seven-record cone adds two decision guards. The
nine-record cone adds two launch-token guards. Deleting any one of the nine
breaks the exact compare-to-launch sequence.

Cycle 106 does not merge the whole Cycle-95 law. Such a merge would have 5,240
overlapping raw inputs and six direct conflicts: Cycle 95 maps every rotated
one-parent `R_LA` signature to `R_B11`, while Cycle 100/Cycle 108 maps it to
`H1`. The dependency obligations are therefore reimplemented in ten new
canonical rows against the live Cycle-108 table.

The replacement is not a decorative nine-for-nine renaming. The old five
comparison records are replaced by the grown candidate, grown reference,
grown join certificate, grown cage, and grown reference guard. The decision
and launch obligations are then supplied by the grown `JOINT`, `BACKSTOP`,
`R_B21`, status, and `AUX` neighborhood. Every load-bearing record is in the
causal append history.

## Why the two added arm guards are necessary

The first candidate joined `OUTPUT=H1` directly to `TYPE=R_B21`. It was exact
on the correct history, but the bit-2 corruption history left the same
two-parent pattern open at `(1,6,1)`, where it wrote an unintended `JOINT`.
The landed arm grows:

```text
R_B33 + TYPE       -> T_H2
R_B32 + T_H2       -> T_H3
OUTPUT + TYPE + T_H3 -> JOINT
```

The two-parent stages each have one alternate common target already occupied,
and the three-parent join no longer aliases any corrupt-reader frontier. All
eight one-bit word corruptions retain Cycle 101's exact stopped state/edge
census and none reaches the candidate or payload. Bit 5 alone writes its
pre-existing `H1` reject poison at `(2,5,2)`, which is deliberately also the
correct path's reference-guard target; the poison occupies that site and
prevents reference growth.

The first reference candidate used only `R_B21 + R_B32 -> H1`. That pair
occurs naturally in the renewed rail and produced a side write after prefix
13. Freezing after one slice would hide rather than repair the collision. The
landed reference adds the independently grown `T_H0` guard:

```text
R_B21 + R_B32 + T_H0 -> H1
```

No new payload row matches any of the 97 rail-prefix local signatures.

## Exact asynchronous and debris coverage

The complete local graph includes every reachable schedule of the 22
Cycle-101 fragment records, inherited `TYPE`, and seven new correct-path
records:

```text
grown correct records          30 = 22 fragment + TYPE + 7 payload
local states                  982
local legal edges           3,850
local terminals                 1
bad frontiers                   0
maximum local frontier           7
premature AUX/launch             0
```

The new payload support is at minimum Manhattan distance seven from the first
96 renewed rail records. Cycle 108 already exhausts every reader schedule
against those 96 ordered rail appends. Cycle 106 additionally checks every
new payload raw row against all 97 rail prefixes and finds zero match. Locality
therefore gives the exact, not sampled, asynchronous product:

```text
product states  = 982 x 97                         = 95,254
product edges   = 3,850 x 97 + 982 x 96           = 467,722
product terminals                                      1
maximum combined frontier                                8
terminal frontier                       ninth-slice start only
```

This factorization does not weaken the schedule quantifier: all local reader
and payload schedules and all ordered rail prefixes are retained. The support
separation proves that no local target can see both dynamic regions, and the
explicit rail scan excludes a payload row matching wholly inside the rail.

Mixed old debris is covered in three ways. First, every correct local schedule
is exhausted against the full 264-record boundary. Second, every corrupted
literal-word graph is exhausted. Third, all 153 live role substitutions are
injected once at each of `REFERENCE_GUARD`, `REFERENCE`, and `STATUS`, for 459
typed controls. The guard is quiet for every wrong role. At reference and
status, the 19 roles that already have unary rows expose their inherited unary
side fronts at adjacent open sites; the remaining 134 roles obey the exact
quiet/bit-control frontier. None of the 459 substitutions exposes an illicit
`AUX` or launch. This is a transparent typed-fault census, not a claim that
arbitrary non-bit corruption is silent.

The full 7,136-row table is tested under all 24 proper-cubic rotations
(`171,264` raw images). All 24 rotations also preserve the complete correct
terminal and each of the four `H0` control stages.

## Exact interface closed and residual left

Closed here:

```text
FIRST_SELF_GROWN_SELECTOR_PAYLOAD_LITERAL_BIT0_INSTANCE
```

Meaning: for the fixed stored word's literal `H1` bit 0, a grown candidate and
grown reference meet in a grown physical cage/status, the correct history is
schedule-independent, and an explicitly injected `H0` reference produces a
physical mismatch certificate and first launch. No payload/harness record is
supplied beyond the inherited generated endpoint boundary.

Smallest live defect:

```text
LAWFUL_ALTERNATE_H0_REFERENCE_GENERATION
```

The current law does not grow an `H0` reference from a different valid literal
history. Cycle 101 instead fails closed when the fixed word is corrupted. That
is good corruption behavior but is not a two-valued selector implementation.
After a lawful alternate value exists, the next larger residuals are 48-bit
serial induction, successor-cell allocation, and unbounded rail recurrence.
Cycle 106 does not establish a full selector, a reusable 48-bit bank, an
unbounded compiler, or Nature's selected exact law.

## Literal Cycle-105 composition status

The standalone Cycle-108 result above does not advance after Cycle 105 without
a new literal-union proof. The exact marker is:

```text
C105_INTEGRATION_OPEN
```

Cycle 105 landed while this construction was in flight. Its generated spine
uses the same two arm coordinates with different contents:

| Site | Cycle 105 | standalone Cycle 106 |
|---|---|---|
| `(4,5,0)` | `AUX` | `T_H2` |
| `(4,6,0)` | `BTG` | `T_H3` |
| `(4,6,1)` | `JOINT` | `JOINT` |

The raw tables themselves are disjoint and form a 7,550-input single-valued
union. The defect is literal state composition, not a hidden raw-table output
conflict. Cycle 105's unary `JOINT -> R_B11` cap also writes at `(4,6,2)`,
exactly the site used here for wrong-branch `REJECT=AUX`. If that cap forms
before the current status, `STATUS=(3,6,2)` acquires an additional `R_B11`
neighbour and neither standalone status row matches. Coordinate occupation and
append timing therefore both block a post-Cycle-105 claim.

A concrete status-gated repair route remains live and unclaimed here: consume
Cycle 105's already-grown `AUX/BTG/JOINT` spine instead of regrowing the two
arm records, replace the unary cap at `(4,6,2)` with the directional rows

```text
JOINT + STATUS H1 -> R_B11
JOINT + STATUS H0 -> AUX
```

and retain the adjacent launch at `(4,5,2)`. This would turn the present reject
collision into the payload gate, but it needs its own literal asynchronous,
corruption, rotation, and old-debris proof before closure.

## N1–N8 no-go-discipline gate

No universal negative theorem is asserted. The bounded residual statements
above were stress-tested as follows.

### N1 — Alternative-route enumeration

| Route | Marker | Result |
|---|---|---|
| Import the full Cycle-95 table | `ATTEMPTED` | Rejected literally: 5,240 overlaps include six `R_LA` output conflicts. |
| Minimize the Cycle-95 first-bit source cone | `ATTEMPTED` | Exhaustive subset search gives unique minima 5/7/9 for compare/AUX/launch. |
| Use Cycle 101 plus the original Cycle-104 map | `ATTEMPTED` | The `R_B12/R_B31` rail aliases activate Cycle-101 unary caps; Cycle 108's `J1/J2` repair is consumed instead. |
| Freeze the rail after one slice | `ATTEMPTED` | Rejected as an artificial horizon repair; it hides the reference-pair collision. |
| Direct `R_B21 + R_B32` reference | `ATTEMPTED` | Fails at rail prefix 13 through an extra `H1` write. |
| Unary `JOINT` reference and two-`R_B32` cage | `ATTEMPTED` | Produces multiple symmetric side writes around open neighbors. |
| Unguarded `OUTPUT + TYPE -> JOINT` | `ATTEMPTED` | Correct history passes, but stored-word corruption 2 exposes a false `JOINT` in the reader. |
| Two-stage typed arm plus guarded reference | `ATTEMPTED` | Lands 982 local states, the exact 95,254-state rail product, all corruptions, rotations, and typed controls. |
| Compose literally with Cycle 105 | `ATTEMPTED` | Two arm sites have different permanent contents and Cycle 105's unary cap occupies the reject site; `C105_INTEGRATION_OPEN`. |
| Consume Cycle-105 spine and status-gate its payload cap | `LIVE` | Concrete `JOINT + STATUS` repair route; not proven in this cycle. |
| Grow a lawful alternate `H0` reference | `LIVE` | Not present in the fixed-word reader; retained as the smallest constructive residual. |

Guarding the old rail instead of remapping it, redesigning the reader to emit
both literal values, or using a different comparator geometry remain live
routes. They are not ruled out.

### N2 — Wall-independence audit

The standalone one-bit source removal is independent of its literal Cycle-105
composition, the lawful alternate value, 48-bit induction, successor
allocation, unbounded recurrence, occurrence/fairness semantics, and
selected-law identity. Closing the Cycle-105 coordinate/timing collision would
not generate a lawful `H0`, and growing `H0` would not reconcile permanently
different arm contents. A lawful `H0` source
would close the two-valued one-bit interface but would not allocate 47 more
stages or a successor cell. Conversely, serial or allocation geometry does not
make the present injected `H0` branch lawful. Unbounded recurrence is a larger
history claim than the eight-slice contact. Occurrence semantics and exact-law
selection are not premises of any finite append result. These walls are not
double-counted as separate axioms.

### N3 — Hidden-wall and primitive scan

The load-bearing inputs are explicit: the 264-record inherited boundary,
Cycle 101's 22-record literal reader, Cycle 108's repaired rail and `TYPE`
contact, ten new canonical rows, the fixed bit-0=`H1` word, and the 96-append
horizon. The boundary is not called empty or source-free. `H0` is labeled a
fault injection rather than a law-generated branch. “All schedules” means all
reachable local schedules combined with every ordered rail prefix, not
fairness, rate, or occurrence. The approved primitive register remains
`REF_SCALE`, `REF_KINETIC`, and `REF_REALIZED_STATE`; no payload mechanism is
hidden as a primitive.

### N4 — Residual matching

| Witness | Exact content consumed here | Match? |
|---|---|---:|
| Cycle 95 | supplied first-bit status/AUX/launch obligations | yes; minimized, not merged |
| Cycle 100 | exact 264-record terminal and stored `10010100` literal | yes |
| Cycle 101 | grown candidate, literal reader, certificate, corruption stops | yes |
| Cycle 104 | onsite role-closed rail and the original alias hazard | yes, through its Cycle-108 repair |
| Cycle 108 | fragment-safe `J1/J2` map, 96-record rail, inherited TYPE | yes |
| Cycle 105 | generated `AUX/BTG/JOINT` spine and unary three-cap | integration collision identified; not consumed by the positive theorem |

No probability, formation, clock, full-selector, or selected-law witness is
cited as evidence for this one-bit finite construction.

### N5 — Rhetoric and resolution audit

“Self-grown payload” means zero added payload/harness source records relative
to the inherited Cycle-100 terminal. It does not mean the 264-record boundary
is regenerated by this runner. “Selector” is restricted in the title and
result to the literal bit-0 instance on the Cycle-108 surface. It is not called
post-Cycle-105 integrated. The positive value is `H1`; the `H0`
path is a typed fault control. “Eight slices” is exactly 96 rail appends, not
an infinite rail. “All rotations” is the 24-element proper-cubic group. No
probability claim, generic binary comparison, full 48-bit selection, or TOE
completion is stated.

### N6 — Partial closure and axiom scan

This closure is exact-law implementation content: local signatures, role
differentiation, guarded intersections, and finite append graphs. It consumes
no new record sort, witness definition, read-lock, clock-lock, storage budget,
formation trigger, counting convention, or actuality rule. The earlier
failures are repaired by additional physical records and local rows. Therefore
no axiom addition follows from Cycle 106. A later inability to obtain a lawful
alternate value after exhaustive exact-law routes would require a separate
exercise; this bounded fixed-word result supplies no such no-go.

### N7 — Steelman

A hostile reviewer should reject any claim of a general selector. The table is
compiled around one known literal `H1`; a lawful `H0` writer is absent; ten
rows and several role choices are candidate-law design data; the initial
boundary is inherited; the rail theorem is bounded; and the literal Cycle-105
union is open. The same reviewer
cannot correctly call the payload supplied: candidate, reference, guards,
cage, status, `AUX`, and launch are absent initially and each appears only at
an exact enabled local frontier. Nor can the reviewer revive the known
prefix-13, corruption-2, or Cycle-104 alias defects; each is explicitly
reproduced and repaired before the landed graph is counted.

### N8 — Cross-cycle echo

Cycles 93 and 95 showed that a comparator works once its cage is supplied but
left a large apparatus boundary. Cycles 100 and 101 moved the stored word,
literal reader, candidate, and certificate into the append history. Cycles
104 and 108 showed that apparently harmless role reuse fails only under
literal law composition and is repaired by exact role differentiation. Cycle
106 repeats that pattern twice: a rail-pair collision and a corrupt-reader
join collision are local codebook/geometric defects, not evidence for new
Record wording. The newly visible Cycle-105 coordinate/timing collision is a
third literal-composition instance and already has a local status-gated repair
route. The remaining integration, lawful-`H0`, and serial-extension tasks
should be attacked as constructions before any constitutional inference.

No-go discipline status: `PASS` for the bounded residual wording; all broader
negative claims are withheld.

## Constitutional disposition

No foundation edit and no axiom addition follow. This result strengthens the
case that candidate/reference/cage/status formation inside a chosen finite
law can be realized by ordinary nearest-neighbor append rules. It neither
selects that law as Nature's law nor supplies an occurrence rule for when an
enabled append happens. Those constitutional questions remain separate from
the standalone literal bit-0 payload-source interface and the explicitly open
Cycle-105 integration.
