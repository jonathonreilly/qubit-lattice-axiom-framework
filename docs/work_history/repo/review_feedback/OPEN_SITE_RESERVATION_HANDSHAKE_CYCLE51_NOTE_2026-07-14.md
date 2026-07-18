# Open-Site Reservation Handshake — Cycle 51

**Date:** 2026-07-14

**Type:** authority-free exact finite nearest-neighbor microtheorem, exhaustive
asynchronous transition graph, proper-cubic covariance test, and fresh bounded
N1–N8 gate

**Authority: none.** This note does not amend an axiom, register a primitive,
select a physical law, or alter a foundation or audit surface. It does not
issue an audit verdict. It does not authorize a commit, push, PR, or
publication. No live
foundation, registry, policy, queue, or audit state is changed.

Companion runner:

```text
scripts/open_site_reservation_handshake_cycle51_2026_07_14.py
```

## Result Up Front

One explicit append-only nearest-neighbor reservation handshake works exactly
for **one official target** `p` in the supplied finite role-coded seed.

The protocol has seven append rules:

```text
OPEN -> {ARM_L, ARM_R in either order} -> JOIN -> RELAY -> COMMIT -> WRITE(p).
```

`OPEN_p` can form only while `p` is absent because `p` is one of the six exact
open neighbors in the `OPEN` rule. After `OPEN_p` exists, the exhaustive graph
contains six pre-commit states. `p` is absent in every one, and no admitted
write to `p` is enabled. The two arms can form in either asynchronous order.
They meet at a caged join, relay to a role-distinct `COMMIT` adjacent to `p`,
and only then enable the designated write. That write rechecks the actual
target as open, appends `VALUE` exactly once, and never changes an old record.

The exact graph has:

```text
9 reachable states;
9 append edges;
2 maximal asynchronous histories;
1 terminal record set.
```

The runner also executes a **blocked-target control** and an **early competing
write request**. A pre-existing record at `p` prevents `OPEN_p`. An adversarial
request immediately after `OPEN_p` is rejected without changing the state;
the same request is accepted after `COMMIT`. In the terminal state, stale
permanent OPEN/COMMIT tokens remain readable but cannot rewrite `p` or
rebootstrap any rotated rule.

This is a conditional microtheorem for one supplied transition table. It does
not complete `FRAME_RETAINING_OPEN_QUARTET_PHASE_TRANSDUCER`, four reservations,
the official phase handshake, future-support avoidance, renewal, or the full
`W_C`. It does not show that an arbitrary additional local rule could not write
`p` early. The physical protection comes from the exact admitted law table;
reservation is not a force outside that table. No axiom language follows.

## 1. Exact Local Geometry

Use the cubic nearest-neighbor directions in the order

```text
(+x,-x,+y,-y,+z,-z).
```

The official target and writable role sites are

```text
p       = ( 0,0,0)
OPEN    = (-1,0,0)
ARM_L   = (-1,1,0)
ARM_R   = (-1,0,1)
JOIN    = (-1,1,1)
RELAY   = ( 0,1,1)
COMMIT  = ( 0,1,0).
```

Eleven permanent, role-distinct seed records supply the local frame:

```text
O_A=(-2,0,0)  O_B=(-1,-1,0) O_C=(-1,0,-1)
L_A=(-2,1,0)  L_B=(-1, 2,0)
R_A=(-2,0,1)  R_B=(-1, 0,2)
S_A=( 1,1,1)  S_B=( 0, 1,2)
C_A=( 1,1,0)  C_B=( 0, 2,0).
```

The labels denote distinct allowed record contents in this supplied candidate
sector. They are not new foundation primitives. Their purpose is to prevent a
scalar role from forgetting which arm it occupies when every proper-cubic copy
of the rule is live.

`OPEN` and `COMMIT` are perpendicular neighbors of `p`. They have exactly two
common nearest-neighbor sites: `p` and `ARM_L`. By commit time `ARM_L` already
carries a permanent record. It therefore cages the alternate two-parent write
site, leaving `p` as the only open common target.

## 2. Exact Nearest-Neighbor Table

Every row below is an exact six-neighbor pattern. `.` means the neighbor must
be open. The center must also be open, and a firing appends the stated output
at that center.

| rule/output | `+x` | `-x` | `+y` | `-y` | `+z` | `-z` |
|---|---|---|---|---|---|---|
| `OPEN` | `.` (`p`) | `O_A` | `.` (`ARM_L`) | `O_B` | `.` (`ARM_R`) | `O_C` |
| `ARM_L` | `.` (`COMMIT`) | `L_A` | `L_B` | `OPEN` | `.` (`JOIN`) | `.` |
| `ARM_R` | `.` | `R_A` | `.` (`JOIN`) | `.` | `R_B` | `OPEN` |
| `JOIN` | `.` (`RELAY`) | `.` | `.` | `ARM_R` | `.` | `ARM_L` |
| `RELAY` | `S_A` | `JOIN` | `.` | `.` | `S_B` | `.` (`COMMIT`) |
| `COMMIT` | `C_A` | `ARM_L` | `C_B` | `.` (`p`) | `RELAY` | `.` |
| `WRITE -> VALUE` | `.` | `OPEN` | `COMMIT` | `.` | `.` | `.` |

The physical rule set contains all 24 proper-cubic rotations of every row.
There is no coordinate argument. Translations use the identical table.

The exact patterns make the reservation law-owned rather than magical:

- `OPEN` sees the actual absence of `p`;
- `COMMIT` again sees the actual absence of `p`;
- `WRITE` requires the role-distinct `OPEN/COMMIT` pair and an open center;
- one-record-per-site blocks the alternate caged center; and
- every firing appends one new site/content pair while preserving the entire
  predecessor state.

## 3. Exhaustive Microtheorem

Let `T` be the transition relation containing exactly the rotated copies of the
seven rows above, and let `s_0` contain exactly the eleven seed records with all
seven role sites open.

### Theorem

Every maximal asynchronous `T`-history from `s_0` has one of the two rule
orders

```text
OPEN, ARM_L, ARM_R, JOIN, RELAY, COMMIT, WRITE
OPEN, ARM_R, ARM_L, JOIN, RELAY, COMMIT, WRITE.
```

Both histories end in the same record set. In every reachable state containing
`OPEN` but not `COMMIT`, `p` is absent. The unique `WRITE` edge has a predecessor
with `p` absent and `COMMIT` present, and its successor contains exactly one
`VALUE` record at `p`. Every old record remains at the same site with the same
content.

### Executable proof

The runner enumerates candidate centers adjacent to every extant record,
matches all six neighbor entries exactly against all `7 x 24 = 168` rotated
rule rows, and breadth-first explores the complete finite graph. Every rule has
occupied local evidence, so an enabled center must occur in that enumerated
neighbor set. Each transition adds one record, so the graph is acyclic.

The two arm writes are the only incomparable events. Their two orders converge
on the same state. `JOIN`, `RELAY`, `COMMIT`, and `WRITE` are then forced in
order. Direct inspection of every state and edge establishes the absence,
authorization, uniqueness, and permanence invariants.

This proves **every asynchronous interleaving** of the declared table, not only
one favored scheduler.

## 4. Controls And Graph Covariance

### Blocked target

Add a pre-existing `BLOCKED` record at `p` to the initial seed. The `OPEN`
pattern no longer matches. Exhaustive exploration returns one state, no edge,
and the unchanged `BLOCKED` content.

### Early competing writer

Immediately after `OPEN`, an external request asks the declared table to write
the official target. The request is real as a control, but the table has no
authorized `WRITE` edge because `COMMIT` is absent. It returns the identical
state. After `COMMIT`, the same request follows the unique designated edge.

This does not claim that a different law containing an extra `OPEN -> p` rule
would be stopped. It shows exactly what the displayed reservation table does.

### Stale tokens

The terminal state retains `OPEN`, both arms, `JOIN`, `RELAY`, and `COMMIT`.
Because `p` permanently contains `VALUE`, the write center is not open. All
other role centers are also permanently occupied. Exhaustive evaluation finds
no enabled rotated copy. Thus stale permanent OPEN/COMMIT cannot rebootstrap
this one-target protocol.

### Proper-cubic and translation covariance

For each of the 24 proper rotations, the runner rotates the entire seed and
independently rebuilds its transition graph. Its state set, edges, two histories,
and terminal are exactly the rotated images of the canonical graph. Two
nontrivial translations pass the same graph-isomorphism check. The blocked
control is also rotation covariant.

## 5. Constitutional And TOE Disposition

This result closes one very small candidate-law subproblem:

```text
one role-distinct OPEN_p
  + append-only two-arm handshake
  + caged alternative target
  + role-distinct COMMIT
  -> one authorized permanent write at p.
```

It does not prove a generic formation trigger, occurrence rate, branch weight,
actual outcome, clock law, or universal reservation principle. It does not
derive the eleven seed roles from the current foundation. It does not assemble
the four official reservations, phase distribution, support avoidance, or
renewal required by Cycle 47. Those remain candidate-law work.

Record needs no revision: the theorem uses one record per site and full
site/content permanence. Admissibility needs no new sentence: this is one
explicit downstream local transition table, not selection of the physical law.
Qualification is not engaged. The result is neither a `W_C` promotion nor an
axiom proposal.

## 6. Next Constructive Use

The immediate follow-up is to replicate the role-distinct reservation at
`q,a,b,c`, prove that their cages coexist under every rotated mixed rule, and
make the four permanent reservations inputs to the official phase protocol.
Only then should the compiler add merge finalization, future-support avoidance,
and next-front renewal/rebinding.

The reusable lesson is precise: an open-site observation becomes a durable
reservation only because the later law checks a record-visible authorization
chain and refuses every uncommitted target write. Permanence preserves that
certificate; it does not supply the refusal rule.

## 7. Fresh No-Go Discipline Gate

The positive microtheorem is exact. The bounded negative is only that no early
or repeated write occurs in the complete graph of the **declared transition
table**. It is not a no-go against an arbitrary extra writer, another seed, or
a complete transducer.

### N1 — Alternative-route enumeration

| route | marker | exact attack and result |
|---|---|---|
| blocked p | ATTEMPTED | put a permanent record at `p`; `OPEN` is disabled and the graph has no edge |
| early competing writer | ATTEMPTED | request `p` immediately after `OPEN`; the request is rejected without `COMMIT` |
| left-first schedule | ATTEMPTED | form `ARM_L` before `ARM_R`; the history reaches the common terminal |
| right-first schedule | ATTEMPTED | form `ARM_R` before `ARM_L`; the history reaches the common terminal |
| rotated-copy cross-fire | ATTEMPTED | enable all 168 rotated rows at once; the complete graph has no parasitic write |
| stale OPEN/COMMIT | ATTEMPTED | retain every handshake token after `VALUE`; no rule reboots and `p` is not rewritten |
| one-record-per-site failure | ATTEMPTED | inspect every edge and state; each edge adds one absent center and preserves all old pairs |
| arbitrary extra writer | ATTEMPTED | add the hostile conceptual rule `OPEN -> p`; it would defeat the broad claim and is explicitly outside this table |
| translated apparatus | ATTEMPTED | translate the seed twice; both complete graphs are exact translated images |

No route is marked `RULED OUT BY PRIOR`.

### N2 — Wall-independence audit

No multiwall no-go is claimed. Openness, arm confluence, commit authorization,
and permanence are clauses of **one bounded transition invariant** for one
table. They are not promoted to four physical assumptions. The residual outside
the theorem is the complete Cycle-47 transducer, not a counted set of axiom
walls.

### N3 — Hidden-wall scan

| phrase | explicit classification |
|---|---|
| declared transition table | exactly the seven rows and all rotated copies; not every possible law |
| exact neighborhood | all six nearest-neighbor contents and an open output center are matched |
| all interleavings | every maximal path in the exhaustive finite state graph, not arbitrary external interventions |
| role-distinct | eleven supplied anchor contents and seven supplied output contents; not foundation-derived labels |
| initial seed | the exact finite anchor configuration; no nucleation theorem is claimed |
| competing request | a request evaluated by this table; an unlisted writer is outside the theorem |

The scan found no load-bearing “obvious,” “natural,” “standard,” “by
construction,” “the framework provides,” “registered,” or “canonical” shortcut.
**Unresolved hidden conditions: 0** at the bounded scope.

### N4 — Exact residual matching

| source | residual there | Cycle-51 use | match? |
|---|---|---|---|
| `SEED_ORBIT_WRITE_ONCE_TRANSDUCER_CYCLE47_NOTE_2026-07-14.md`, lines 140–161 | an openness certificate is stale without reservation and phase coupling | constructs one exact OPEN/reservation/COMMIT microcomponent | partial positive match only; no `W_C` closure |
| same note, lines 163–170 | failed scalar table is candidate-law compilation, not axiom need | keeps this successful microtable downstream | exact constitutional disposition |
| same note, lines 257–270 | caged sidecar and delayed official write remain live positive paths | implements one caged delayed-write instance | exact positive route, narrower scope |

No cited residual is used to claim the whole quartet or transducer has landed.

### N5 — Rhetoric and resolution audit

| resolution | tested? | licensed statement |
|---|---:|---|
| one canonical target | yes | exact nine-state reservation graph |
| 24 proper-cubic rotations | yes | exact graph covariance for the supplied seed |
| two translated seeds | yes | translation covariance of the same graph |
| four-target OPEN quartet | no | remains open |
| complete W_C | no | remains open |
| arbitrary additional local law | no | can contain an early writer; no exclusion claim |
| multi-front/collision domain | no | outside scope |

The negative wording is restricted to the declared graph.

### N6 — Partial-closure paths

1. Compose **four role-distinct reservations** and exhaust mixed rotated rules.
2. Make the four COMMIT certificates inputs to **phase distribution** and merge
   finalization.
3. Prove future-support avoidance and **renewal rebinding** on the next front.
4. Replace supplied role labels by a seed-derived frame orbit or caged spatial
   motifs where possible.

Each is candidate-law construction, not a new axiom.

### N7 — Strongest hostile steelman

**Hostile reviewer:** “Your reservation has no power against an **unlisted early writer**.
Add one covariant local row that sees `OPEN` next to an empty `p`, and
it writes before COMMIT. Therefore you have not proved that records intrinsically
reserve sites or that permanence enforces mutual exclusion.”

That objection is correct against the broad statement. **Broad negative fails.**
The surviving theorem is table-relative: the complete declared rule
graph contains no early or repeated official write. That is exactly the right
acceptance test for a candidate law and nothing more.

### N8 — Cross-cycle echo

| prior result | lesson carried forward | present effect |
|---|---|---|
| Cycle 43 | a labeled seed can carry a cubic frame, but the transducer was unassembled | use explicit role-distinct local parents without claiming seed derivation |
| Cycle 47 | scalar roles cross-fire and an uncaged perpendicular parent pair has two targets | use role-distinct triads and occupy the alternate OPEN/COMMIT common target |
| Cycle-34 moving-front result | stale permanent wake can coexist with a translated logical apparatus | require terminal non-rebootstrap now; defer renewal to the moving-front integration |

No echo is treated as proof of full `W_C`.
**Gate result: PASS for the bounded microtheorem and its declared-table
negative; PASS for no broader no-go.**

## 8. Reproduction And Exact Disposition

Run:

```bash
python3 scripts/open_site_reservation_handshake_cycle51_2026_07_14.py
```

The runner constructs all rotated rule rows, exhausts the canonical, blocked,
rotated, and translated graphs, checks every state and edge invariant, and
audits the fresh N1–N8 text. The exact result is `PASS=98 FAIL=0`.

**Disposition:** exact conditional microtheorem for one supplied target and
transition table. It is a reusable Cycle-47 construction component, not a
formation axiom, physical-law selection, quartet completion, or `W_C` promotion.
