# R_B01 orientation-13 neighbouring-guard family — Cycle 128

Date: 2026-07-15

Authority: none

Disposition: campaign bounded-negative artifact for the fixed-G0/G1,
single-record, nearest-neighbour parent/gate family; audit status unset

Write scope: runner + review note only

Companion runner:

```text
scripts/r_b01_orientation13_neighbor_guard_family_cycle128_2026_07_15.py
```

No predecessor, foundation, axiom, primitive, registry, queue, policy, audit,
or git state is edited here. No commit, push, or PR is made. Cycle 124 supplies
the executable campaign terminal. Cycles 125 and 127 are cited only as
campaign bounded-negative artifacts;
their candidate rows are not inherited.

## Exact bounded object

Cycle 128 tests

```text
R_B01_ORIENTATION13_FIXED_G0_G1_SINGLE_GUARD_FAMILY
```

after granting the cleanest repair to Cycle 127's coordinate reuse: the
physical D7 and JOIN jobs may be relocated, while the phase coordinates remain

```text
G0 = (5,1,-3)
G1 = (6,1,-3).
```

The tested family contains the two smallest local repairs:

1. form one record at another nearest neighbour of G1, then use G0 plus that
   record as G1's two-parent local;
2. form one record beside D2 before G0, so the D2 local differs from the unary
   G1 local.

Every output role in the 153-role onsite alphabet is covered by the decisive
full-history test. The smaller terminal-only control exhausts every ordered
pair of distinct roles currently absent from the Cycle-124 terminal.

## Result 1: the only supported G1 parent has an impossible history

Besides G0, fixed G1 has five nearest neighbours:

```text
(5,1,-4)  empty local
(5,1,-2)  empty local
(6,0,-3)  unary L6
(6,2,-3)  empty local
(7,1,-3)  empty local
```

Thus only

```text
P = (6,0,-3)
```

can form directly from the Cycle-124 terminal. Its canonical source local is
exactly unary `L6`. Proper-cubic closure makes that row target 31 sites at the
terminal.

The terminal view is not enough. The subset-complete condition compiler was
therefore run from the exact Cycle-100 source across all Cycle-124 outputs. It
finds 36 places where unary `L6` can occur in some variable-neighbour subset.
The decisive three do not depend on treating an unreachable subset as
history: they already have unary `L6` in the exact 264-record source state,
before any Cycle-101-to-124 variable record appends, and are future campaign
outputs:

```text
(4,-1, 0) -> OPEN_B
(4, 1,-2) -> R_B00
(5,-1,-1) -> H0.
```

A single-valued unary-L6 row must assign one content to all three locals. They
require three different contents. Choosing `OPEN_B`, `R_B00`, or `H0` still
offers two wrong writes at source state zero; choosing any of the other 150
roles offers three. Therefore **all 153 roles fail**, with at least two exact,
reachable source-state miswrites for every choice.

This is stronger than a role-name or terminal-shell collision. The proposed
parent cannot be appended to the Cycle-100-to-124 candidate row union while
preserving the campaign history that produced the terminal on which the
construction was drawn.

## Terminal-only control: the attractive geometry is still not a word

As a hostile control, the full-history collision was temporarily hidden by
treating the finished Cycle-124 terminal as a fresh source. The search then
used:

- all 18 roles absent from that terminal;
- all 306 ordered distinct role pairs for P and G0;
- every proper-cubic image of the unary-L6 and L6+L6 rows;
- the exact two-parent G1-to-H1 row;
- the simultaneous Cycle-124 law table.

The static screen leaves 304 superficially single-valued role pairs. This
confirms that adding a genuine second local parent does separate intended G1
from D2 at the final snapshot. It does not establish an append-safe word.
Every survivor has at least nine unexpected targets.

The deterministic minimum representative is

```text
P role  = B_0_2
G0 role = B_1_2
```

with 45 proposed outputs, 55 compiled target conditions, and nine unexpected
condition targets. Its exact asynchronous factor graph is

```text
states       701
edges       1330
terminals      0
reached        36
first bad    state 160: (-1,-5,-2) -> H1.
```

So even the terminal-only indulgence does not yield a completed factor. The
full-history three-content collision already closes every output role before
this secondary shell failure is needed.

## Result 2: a merely nearby D2 gate is not prior

Besides G0, D2 has five nearest-neighbour gate positions. All five are open in
the Cycle-124 terminal. Three have nonempty source locals:

```text
(4,2,-3)  L6 + T_H3
(5,2,-2)  H1 + H1 + T_H3
(5,3,-3)  H1 + R_B01.
```

The other two, `(5,2,-4)` and `(6,2,-3)`, have empty locals. None of the five
gate positions neighbours G0: each is Manhattan distance two from it.

That topology decides the one-record gate proposal. A supported gate and G0
are independently enabled from the same terminal. Append-only asynchronous
semantics therefore contains an order in which G0 forms first. At that moment
G1 and D2 again have the same canonical unary-G0 local for every one of the
153 possible G0 roles, exactly as Cycle 127 proved. If that unary row writes
G1=H1, it can write D2=H1 before the gate exists. A later gate cannot revoke
the record.

Calling the gate “earlier” in a preferred drawing does not supply causal
priority. To repair this branch, the gate must enter the local prerequisite
chain that enables G0, which requires at least one further bridge at this
geometry, or G1 itself must require a provenance structure that cannot be
skipped. The live requirement is therefore a **causally forced multi-parent
guard**, not merely any second parent.

## Smallest live frontier

The fixed-coordinate, one-record family is closed. The preferred next route is
the separately executable two-record/guarded-renewal provenance detour: reuse
its
causally forced multi-parent guard as the source of the G1-distinguishing
parent, instead of inventing another unary phase orbit.

Still live are:

- a **relocated/nonlocal cage** whose multiple records are forced before the
  ambiguous step;
- an **orientation-20 redesign** with its tail anchored rather than supplied;
- the **separately executable guarded-renewal detour**, supported only by its
  own campaign runner and not promoted by this note;
- a longer orientation-13 bridge that causally gates G0 before exposing D2;
- a fully new R_B01 writer geometry.

This is **not a no-go against every orientation-13 redesign**. It is **not a no-go against an R_B01 writer**. It is not a negative about two-witness record
formation, clocks, probability, or recurrence. **No axiom addition follows**
from this bounded local failure.

## Bare-metal meaning

“Two records exist nearby” and “the write requires two causally prior records”
are different statements. Only the second changes the set of allowed partial
histories. At bare metal there is no scheduler that promises the helpful
record happens first, and a later clock tick cannot repair an already legal
wrong write. Causal provenance must be carried in the local enabling pattern
itself.

This is directly relevant to formation-language drafting. A phrase such as
“has two witnesses” is too weak if “has” only describes one convenient final
snapshot. The operational content needed by this probe is that both witness
records are prerequisites of the forming transition in every allowed append
history. This note does not promote that observation to an axiom; it supplies
one exact construction-level discriminator for later constitutional work.

## N1–N8 no-go-discipline gate

Status: **PASS only for
`R_B01_ORIENTATION13_FIXED_G0_G1_SINGLE_GUARD_FAMILY`; FAIL for a universal
orientation-13, writer, provenance, recurrence, or axiom-need no-go.** The
current `origin/main` no-go-discipline body governs this note.

### N1 — Alternative routes

| route | marker | result |
|---|---|---|
| fixed G1 plus one terminal-supported parent | `EXHAUSTED / NEGATIVE` | only unary-L6 P exists; all 153 output roles corrupt the campaign history from source state zero |
| fixed D2 plus one independently supported gate | `EXHAUSTED / NEGATIVE` | G0-first append order exposes the alias before the gate |
| terminal-only unused-role pair indulgence | `EXHAUSTED / NEGATIVE CONTROL` | 304 static survivors, all with at least nine unexpected targets |
| causally forced multi-parent guard from guarded renewal | `LIVE / PREFERRED` | removes both unary history reuse and scheduler dependence |
| relocated/nonlocal cage | `LIVE` | can make provenance prior through a multi-step local chain |
| orientation-20 redesign | `LIVE` | must anchor the Cycle-125 empty tail |
| longer orientation-13 G0-gating bridge | `LIVE` | can force the D2 gate before G0 at cost of another record |
| new R_B01 writer geometry | `LIVE` | abandons the fixed G0/G1 premise entirely |

At least five materially different constructive routes remain. No universal
negative ships.

### N2 — Residual independence

| pair | first closes second? | second closes first? | treatment |
|---|---|---|---|
| unary-L6 historical collision vs terminal unexpected shell | yes, the historical collision already rejects P | no | shell is kept as an independent hostile control, not multiplied as a new wall |
| G1-parent failure vs D2-gate causal failure | no | no | distinct sides of the same local alias, both bounded here |
| single-record gate vs multi-record forced cage | no | cage strictly changes causal prerequisites | broader route remains live |
| writer existence vs exact-law selection | no | no | independent residuals |
| third word vs finite grammar vs recurrence | no direct closure | ordered dependency | one downstream chain, not three walls |

The 36-target history scan and 701-state factor graph are two resolutions of
one proposed G1-parent route. They are not presented as independent evidence
for a broad no-go.

### N3 — Hidden-condition scan

Explicit inputs are the Cycle-100 source, all 101 Cycle-124 grown outputs, the
8,744-row simultaneous proper-cubic table, orientation 13, fixed G0/G1/D2
coordinates, all five alternate neighbours on each side, all 153 onsite
roles, all variable-neighbour subsets in the campaign history, and every
asynchronous order in the representative factor. The terminal-only control is
labelled as such. No preferred direction, global scheduler, reader, clock,
hidden phase bit, supplied gate, or revocation operation is granted.

### N4 — Residual matching

| cited witness | witness residual | Cycle-128 residual | match and use |
|---|---|---|---|
| Cycle 124 positive | append-safe R_B01 allocator/port terminal | source for next writer | exact inherited source and law |
| Cycle 127 negative | unary G1/D2 alias at fixed coordinates | one-parent repairs of that alias | exact proposed follow-up |
| terminal-only two-parent screen | final-snapshot separation | full-history append safety | partial match only; useful control, not a positive |
| guarded renewal detour | causally forced two-record provenance | need a prior distinguishing parent | matching constructive genus; tested by a separate executable construction |
| generic orientation-13 writer | arbitrary relocated/caged geometry | fixed G0/G1 single-record family | no match; not closed |
| generic two-witness formation law | physical record formation | one candidate compiler word | no match; no constitutional inference |

Nonmatching residuals limit rhetoric; they do not support enlargement.

### N5 — Resolution and rhetoric

Exhausted: all alternate nearest-neighbour sites for fixed G1 and D2, all 153
output labels for the decisive unary-L6 history conflict, every subset of
variable neighbours in the Cycle-100-to-124 campaign history, all 306 ordered
pairs of unused phase roles in the terminal-only screen, and the complete
representative asynchronous factor graph. Not exhausted: two-record cages,
longer bridges, arbitrary relocated coordinates, other orientations, or all
possible writers. “Fixed one-record guard family fails” cannot become
“orientation 13 fails,” “two parents fail,” or “records need a new axiom.”

### N6 — Partial-closure paths and axiom discipline

The failure itself supplies a constructive criterion: the extra provenance
must be forced before the ambiguous local becomes enabled. The separately
executable guarded-renewal construction is the smallest campaign source of
that structure. A longer local
bridge into G0 is another. Both are ordinary candidate-law constructions under
the present nearest-neighbour, proper-cubic, append-only rules. The result does
not select axiom text, a primitive, or an import.

### N7 — Strongest hostile steelman

A hostile reviewer should say the attractive P construction was drawn only on
the final terminal and forgot that its unary-L6 trigger existed during the
history that built that terminal. The exact history compiler finds three
incompatible old outputs, so changing the phase label cannot help. The same
reviewer should reject a D2 “gate” that is merely independently enabled: an
adversarial append order places G0 first and permanence makes the resulting
mistake unrecoverable. But that reviewer cannot reject a causally forced
multi-record guard from these data, because it removes both premises rather
than renaming either one.

### N8 — Cross-cycle echo

Cycle 121 repaired a FRONT alias by restoring source-word provenance. Cycle
125 rejected an unanchored tail. Cycle 127 showed that one phase name cannot
distinguish rotation-equivalent unary locals. Cycle 128 now shows that a second
record helps only when its own formation is history-safe and causally required.
The echo is narrow but consistent: successful bare-metal words encode order in
local prerequisites; they do not receive order from prose, clocks, or a
preferred drawing. That points directly to the guarded-renewal detour and does
not establish an axiom need.

## Verification

```text
python3 scripts/r_b01_orientation13_neighbor_guard_family_cycle128_2026_07_15.py
```
