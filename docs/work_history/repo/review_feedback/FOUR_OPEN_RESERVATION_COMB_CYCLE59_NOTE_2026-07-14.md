# Four Open-Reservation Comb — Cycle 59

**Date:** 2026-07-14

**Type:** authority-free positive exact finite candidate-law construction,
independent four-replica obstruction, exhaustive asynchronous graph,
proper-cubic covariance, support and infinite-rail composition gate

**Authority: none.** This note is not an axiom proposal, registered primitive,
retained theorem, audit verdict, or selection of Nature's law. It does not
authorize a foundation, registry, policy, queue, or audit edit. It issues no
commit, push, PR, or publication instruction. **No axiom need follows** from
this candidate-law result.

Companion runner:

```text
scripts/four_open_reservation_comb_cycle59_2026_07_14.py
```

## Result Up Front

Cycle 59 first independently confirms that four translated and properly
rotated copies of the Cycle-51 one-target handshake cannot simply be placed at

```text
q=(0,-1,0), a=(1,0,0), b=(2,0,0), c=(3,0,0).
```

One replica occupies 17 non-target sites. Across all `24^4 = 331,776`
orientation quartets, **zero** quartets have pairwise-disjoint footprints even
before official-support avoidance is imposed. The numbers of individually
official-support-safe orientations are respectively `7,1,1,5`; their product
also contains zero disjoint quartet. Independent replication is therefore not
the route.

A shared construction does work. One supplied extensional candidate table is
live from the original Cycle-57 state zero. It can start only after the
frame-visible `ARM+A_0_2+H1` triple exists. `START` at `(-1,3,0)` writes a
three-site `W1` orbit that reaches the `y=4` wake and the negative-`z` descent.
The comb then closes a three-record cage and branches once along the
negative-`z` side of the four official targets.
The canonical record-visible site/content certificates are

```text
q: (0,-1,-1): W6
a: (1, 0,-1): W6
b: (2, 0,-1): OPEN_B
c: (3, 0,-1): OPEN_C
```

Each certificate is a nearest neighbour of its target. Each defining exact
row sees that target as open. Inserting `BLOCKED_OFFICIAL_TARGET` at the target
disables the row; at each defining source the same is true for every content
in the complete live role alphabet and an arbitrary external sentinel.

The canonical `OPEN_C` record at `(3,0,-1)` is also the minimum downstream
**COMMIT** token: it cannot occur until the canonical `OPEN_B` record is
present; that record cannot occur until the `W6/J6/COMP6` cage has forced both
the `q` and `a` certificates. The exhaustive graph independently checks that
no reachable state contains `b` before `q,a`, and no state contains the
designated `c/COMMIT` before `q,a,b`.

All Cycle-57 builder rules and all Cycle-52 renewal rules remain installed
from state zero. Exhaustion of all 374 Cycle-57 builder states finds only two
comb-start cases: no comb assignment, or canonical `START`; `START` always has
`ARM,A_0_2,H1` already present. Its only adjacent builder additions are the two
parents already consumed by that row, so an early comb cannot suppress a
later builder target.

The comb footprint avoids all 29 current/future official-support sites and
misses the entire infinite future rail corridor

```text
x <= -2, 0 <= y <= 2, 0 <= z <= 3.
```

There is one controlled boundary contact: exterior `W1=(-2,3,0)` is adjacent
to the first-slice `B_0_2=(-2,2,0)`. Two exact schedule-tolerance rows close
that commuting diamond. `W1` first still enables `B_0_2`; `B_0_2` first still
enables `W1`; both orders join the identical map. Every other comb record is
at least distance three from the future corridor, except `START` at distance
two as the other endpoint of this same local diamond. Later slices are fully
separated. The composition is therefore live from state zero and indefinite,
not only checked after the builder terminal or for a sampled rail prefix.

The combined comb has 24 canonical exact inputs, 464 distinct proper-cubic
directional inputs, and 45 declared permanent additions. Exhausting every single-record
asynchronous order gives exactly

```text
4,784,509 states
46,716,061 edges
1 terminal containing all 45 additions
0 incomplete terminals
0 output conflicts
0 off-footprint or wrong-content writes.
```

In particular, no rotated comb row, live Cycle-57 row, or live Cycle-52 row
enables a write at `q,a,b,c` before the designated COMMIT. The present table is
reservation-only, so it does not write those targets after COMMIT either. A
future phase-distribution table must consume the COMMIT explicitly; Cycle 59
does not silently grant that future table authority.

This is a positive construction, so **no negative N1–N8 gate is invoked**. It
does not complete the full Cycle-47 transducer, select the physical local law,
derive formation occurrence, assign probability or rate, or amend an axiom.

## 1. Why Four Copies Fail

Cycle 51 uses 11 permanent anchors and six non-target dynamic sites
`OPEN, ARM_L, ARM_R, JOIN, RELAY, COMMIT`. The seventh dynamic site is the
official target and is excluded from the placement footprint because it must
remain open. Each translated/rotated replica therefore requires 17 sites.

The runner constructs all 24 images about the replica's own target and then
translates them to each of `q,a,b,c`. It does not stop after finding a local
collision. It tests all 331,776 orientation quartets for all six pairwise
footprint intersections.

Exact result:

| target | support-safe orientations |
|---|---:|
| `q` | 7 |
| `a` | 1 |
| `b` | 1 |
| `c` | 5 |

There are zero pairwise-disjoint quartets without the support condition and
zero with it. This is a bounded obstruction to copying the displayed Cycle-51
geometry, not a no-go against a shared reservation structure. The construction
below is the positive alternative.

## 2. Shared Comb Geometry

The rule table is installed at Cycle 57's original eight-record state zero; no
comb record is supplied. Across the exact 374-state Cycle-57 builder graph,
the only possible first comb assignment is

```text
(-1,3,0): ARM + A_0_2 + H1 -> START.
```

It is absent in 113 builder states and enabled at that one site in 261 states.
No rotated off-footprint copy is enabled. Since both adjacent builder
additions `ARM` and `A_0_2` are already permanent whenever `START` matches,
the comb can begin early without changing the remaining builder graph.

The staged full-orbit skeleton is:

| role | exact sites in the defining completed snapshot | visible input contents |
|---|---|---|
| `START` | `(-1,3,0)` | `ARM+A_0_2+H1` |
| `W1` | `(-2,3,0),(-1,3,-1),(-1,4,0)` | `START` |
| `W2` | `(0,3,-1)` | `H1+W1` |
| `W3` | `(0,2,-1)` | `H0+W2` |
| `W4` | `(0,1,-1)` | `H1+W3` |
| `W5` | `(0,0,-1)` | `Z0+W4` |
| `W6` | `(0,-1,-1),(0,0,-2),(1,0,-1)` | `W5` |
| `J6` | `(0,-1,-2),(1,-1,-1),(1,0,-2)` | `W6+W6` |
| `COMP6` | `(1,-1,-2)` | `J6+J6+J6` |
| `S7` | three sites around `COMP6` | `COMP6` |
| `E` | six sites | `J6+S7` |
| `OPEN_B` | three sites including `(2,0,-1)` | `E+E+W6` |
| `S8` | 12 defining sites, plus 3 reached schedule images | `E` |
| `OPEN_C` | three sites including `(3,0,-1)` | `OPEN_B+S8+S8` |

The site counts total 45. `W1`, `W6`, `J6`, `S7`, `E`, `OPEN_B`, `S8`, and
`OPEN_C` are proper-cubic signature orbits, not coordinate-indexed exceptions.
The labels `q,a,b,c` identify sites relative to the official frame; the law
itself uses only exact local contents.

The raw 14-row skeleton has partial schedules in which an earlier `S8` or
`OPEN_B` becomes an extra exact neighbour of a still-open orbit site. Eight
additional exact schedule-tolerance rows retain the intended `E`, `OPEN_B`, or
`S8` output for precisely those signatures. They are fixed rows, not
wildcards. Adding them closes every incomplete terminal without introducing a
new output or off-footprint site.

Two more exact rows close the sole rail contact:

```text
A_0_2 + B_1_2 + W1 -> B_0_2
START + B_0_2       -> W1.
```

They are the two sides of one append-order diamond, not a second rail law. The
first preserves Cycle 52's declared `B_0_2` output if exterior `W1` arrived
first; the second preserves the declared `W1` output if `B_0_2` arrived first.

## 3. Openness And Commit Order

The four site-relative certificates are record-visible permanent facts about
openness at their formation event. Their target is omitted from the exact
occupied-neighbour signature, so an occupied target changes the signature.
The runner performs the canonical blocked-target control at every defining
source and checks the entire live content alphabet there.

In the supplied open-target domain, the exhaustive graph gives the stronger
history statement: every edge that appends one of the four canonical
certificates has an absent target, because no predecessor contains a target
record and no live row can append one there.

The causal chain to the designated COMMIT is local and append-only:

```text
W5
 -> three W6 records (including q and a certificates)
 -> three pairwise J6 joins
 -> COMP6
 -> S7 and E branches
 -> canonical OPEN_B at b
 -> two S8 parents
 -> canonical OPEN_C at c = COMMIT.
```

`COMP6` is the important shared completion gate. Its three `J6` parents cover
all three `W6` records, preventing a branch from bypassing one of the first two
certificates. The canonical `OPEN_B` used by the `c` row is exactly the `b`
certificate. Consequently the last certificate doubles as the minimum
all-four completion token; no extra constitutional or primitive notion of
COMMIT is introduced.

The current live union contains no official-target writer. That is an exact
reservation result for this table, not an assertion that any arbitrary future
rule is forbidden. A later phase rule must have a displayed input path from
the permanent COMMIT and must be re-audited in the mixed graph.

## 4. Complete Asynchronous Graph

The runner expands the 24 canonical inputs through every proper-cubic rotation
and compiles each comb-only raw six-neighbour pattern into a bit predicate over the 45
possible additions. Candidate centers include every open nearest neighbour of
the base or declared footprint, including all four official targets and all
off-footprint sites where a parasitic rotated row could fire.

Breadth-first exploration starts from the empty 45-bit extension after the
fixed frame context is available. The separate 374-state builder enumeration
and the exact rail diamond discharge the earlier live-table interleavings. At each
state it follows every enabled one-record append. No fairness order or favored
scheduler is chosen. Every transition strictly adds one record, so the graph
is finite and acyclic.

Exact result:

```text
reachable states:                 4,784,509
directed append edges:           46,716,061
terminal states:                          1
terminal size:                           45
incomplete dead terminals:                0
mixed-output conflict states:             0
off-footprint/wrong-content outputs:       0
COMMIT-order violations:                   0
```

A finite append-only graph in which every maximal history ends at the same
complete record set is asynchronous confluence for this bounded comb. The
large state count matters: the result is not a sequential demonstration of
the staged table.

## 5. Proper-Cubic Covariance

The 24 canonical rows generate 464 distinct raw directional signatures; rows
with internal symmetry have fewer than 24 distinct images. Every raw signature
has exactly one output. For each of the 24 proper rotations, canonicalizing the
rotated image returns the same canonical row and output.

Rotation is a bijection on sites and commutes with nearest-neighbour signature
evaluation and one-record append. The runner also checks that all four
certificate/target adjacencies survive every rotation. Therefore rotating the
base, targets, footprint, and histories maps the complete graph to an
isomorphic graph. No coordinate test is hidden in the table.

Translations are automatic because every row is expressed in neighbour
offsets only.

## 6. Official Support And Infinite Renewal

The 45 comb additions are disjoint from the exact 29-site Cycle-43/Cycle-53
official support, including `q,a,b,c`. The natural Cycle-52 transform is

```text
(x,y,z) -> (-x-1,z,y).
```

Every future canonical slice has original `x>=1`, `0<=y<=3`, `0<=z<=2`.
Its natural image therefore lies exactly inside

```text
x<=-2, 0<=y<=2, 0<=z<=3.
```

Exactly two comb sites are closer than three to that corridor:

```text
START=(-1,3,0): distance 2
W1   =(-2,3,0): distance 1, adjacent only to first-slice B_0_2.
```

The displayed two-sided tolerance rows make the `W1/B_0_2` square commute.
After `B_0_2` is permanent, no later rail target is adjacent to either site.
Every other comb addition has distance at least three. This gives analytic
infinite-tail separation, with the first 64 slices checked as an executable
control.

Composition with the builder is also live from its original state zero. The
runner enumerates all 374 Cycle-57 builder states. Before comb content exists,
the only possible comb output is canonical `START`, and its exact input already
contains both builder additions adjacent to it. No other comb site is adjacent
to a declared builder addition. Therefore a comb append cannot add an extra
neighbour to any unformed builder target. Comb-only roles do not occur in old
builder inputs, so they cannot create an off-footprint old-rule match either.

At the completed Cycle-57 base, the old builder has no enabled row and Cycle
52 exposes exactly `(-2,1,1):B_1_1`. The same statements hold after all 45 comb
writes. Canonical inputs collide with neither earlier table. The only output
alphabet overlap is the explicit tolerance row preserving Cycle 52's own
`B_0_2` content.

Thus the comb may interleave with indefinitely renewing Cycle 52 while all
tables remain live.

## 7. Exact Scope And Next Residual

Cycle 59 closes a precise candidate-law subproblem:

```text
four non-coexisting private handshakes
 -> one shared frame-anchored openness comb
 -> four permanent site-relative certificates
 -> one downstream all-four COMMIT
 -> no pre-COMMIT official target write
```

It does not yet provide the Cycle-47 `PHASE_DISTRIBUTION`, official post-COMMIT
writes, merge finalization with every phase input, or next-front binding of the
comb. It also does not show that the displayed 24-input table is uniquely
forced by the axioms or selected by experiment. Those are separate candidate-
law and science-selection obligations.

No foundation consequence follows. Record permanence is used exactly as
written; Admissibility supplies the slot for one fixed nearest-neighbour law
but does not select this table. Formation occurrence, probability, clock rate,
continuum recovery, matter counting, and gravity remain outside this finite
construction.

Because the shipped result is positive and its residuals are stated without a
no-go claim, no negative N1–N8 gate is invoked.

## Verification

```text
python3 scripts/four_open_reservation_comb_cycle59_2026_07_14.py
```

Expected exact graph line:

```text
4,784,509 states / 46,716,061 edges / 1 complete terminal / 0 failures
```
