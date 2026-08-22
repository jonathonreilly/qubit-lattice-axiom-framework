---
claim_id: two_axis_opposite_zprobe_incoming_outgoing_one_two_split_tplus1_reverse_face_bounded_theorem_note_2026-08-15
claim_type: bounded_theorem
claim_scope: "1-in 2-out axis split of M and O at t+1 on the four z-probes of the two-axis opposite seed, and reverse/face from that, are reported. Displayed, not adopted."
upstream_dependencies:
  - minimal_axioms
runner: scripts/two_axis_opposite_zprobe_incoming_outgoing_one_two_split_tplus1_reverse_face_2026_08_15.py
---

# One-In Two-Out Axis Split Of Own-Incoming And Own-Outgoing At t+1 Reverse And Face On Four Z-Probes Of The Two-Axis Opposite Seed

> **Key terms used in this doc** are indexed A-Z at `docs/KEY_TERMINOLOGY.md`;
> each row points to the canonical source-of-truth doc.

**Date:** 2026-08-15
**Type:** bounded_theorem
**Scope:** 1-in 2-out axis split of simultaneous earliest incoming set `M` and
outgoing dual `O` at each probe's `τ=t+1`, and reverse/face from that split,
on the four z-probes of the two-axis opposite seed in `B_3(0)={n:n·n<=9}`.
Same process and z-probes as nm2axz. Let `t(q)` be the formation tick of
probe `q`. Let `τ(q)=t(q)+1`. `M(q,τ)` is the set of earliest incoming
nearest-neighbor steps at `q` using only records with tick `<= τ`. Seeds
are a singleton seed letter. `O(q,τ)` is the outgoing dual of `M`: the set
of `e` in `{±e_1,±e_2,±e_3}` such that `q+e` is formed and `e` is in
`M(q+e,τ)`. Unformed at `τ` is `UNDEFINED`. Empty `O` is empty, not
`UNDEFINED`. Axis of a defined lock set `S` is
`Axis(S)={e_i | some ±e_i in S}`. Cover HOLDs at `q` if and only if
`Axis(M)` intersect `Axis(O)` is empty and `Axis(M)` union `Axis(O)` equals
`{e_1,e_2,e_3}`. `UNDEFINED` if `M` or `O` is `UNDEFINED`. Else fail. Split
HOLDs at `q` if and only if cover HOLDs and `|Axis(M)|=1` (hence
`|Axis(O)|=2`). 2-in 1-out is fail of this object, not UNDEFINED. Reverse
HOLDs if and only if split HOLDs at `A` and at `B`. Face HOLDs if and only
if split HOLDs at `C` and at `D`. This is not leftover of the 1-axis
opposite two-site seed. This is not leftover of nmcover axis-cover. This is
not leftover of nm2axz axis-cover. This is not leftover of leftover-of-`M`
alone. This is not leftover of leftover-of-`O` alone. This is not
leftover-empty fail of leftover axis.
This is not leftover of nmunopp union. This is not leftover of nmt2opp `M`
frozen at `t`. This is not leftover of nmot2opp two-tick composition. This
is not leftover of nmoutopp untimed eventual-`O`. This is not leftover of
mixed #7188 fail/fail. This is not leftover of the same-lock two-site seed.
The second pair is a new seed, not a formed child. Uniqueness is not
required. Mixed remains a set. Displayed, not adopted. Do not write into
Admissibility. Do not attach L1.
**Audit-status authority:** independent audit lane only. This note authors no
audit verdict and predicts none.
**Primary runner:**
[`scripts/two_axis_opposite_zprobe_incoming_outgoing_one_two_split_tplus1_reverse_face_2026_08_15.py`](../scripts/two_axis_opposite_zprobe_incoming_outgoing_one_two_split_tplus1_reverse_face_2026_08_15.py)

Framework input:

- [`MINIMAL_AXIOMS_2026-06-29.md`](MINIMAL_AXIOMS_2026-06-29.md) supplies
  cubic-lattice sites `Z^3` with nearest-neighbor adjacency, the one-site
  algebra `M_2(C)`, and the Record sentences that records form and that a
  present record locks exactly one admissible local possibility.

Everything after that quoted input is a finite displayed process on `B_3(0)`
and the four named z-probes. Incoming lock letters are unit nearest-neighbor
steps. `O` is the outgoing dual of those incoming sets at the per-probe cut
`τ=t+1`. Axis is the unsigned lattice direction of a signed lock. Cover is
the complementary occupation of `{e_1,e_2,e_3}` by `Axis(M)` and `Axis(O)`.
Split is cover together with `|Axis(M)|=1`. Reverse and face are scored on
split HOLD at the paired probes. Named signs `{+,−}` are a coarser readout
and are not used. A singleton unique lock letter is a different readout and
is not used as the object. Existential opposite of signed locks is a
different readout and is not used as the split reverse. Axis-cover without
the one-axis incoming cardinality is a different readout and is not used.
Leftover-empty fail of unsigned leftover axis sets is a different readout
and is not used. A `Z^3` sum of those locks is a different readout and is
not used. Occupancy of sites is not used. A six-neighbor star is not the
letter.

## Machine status and trace

```yaml
actual_current_surface_status: bounded-support
target_claim_type: bounded_theorem
claim_type_reason: "Exact report of 1-in 2-out axis split of M and O at t+1 on the four z-probes of the two-axis opposite seed, split hold at A,B,C,D from cover hold with |Axis(M)|=1, reverse hold and face hold from that split; uniqueness of incoming locks is not claimed and the bits are not adopted."
trace_class: frontier_discovery
target_claim_id: two_axis_opposite_zprobe_incoming_outgoing_one_two_split_tplus1_reverse_face
target_blocker_text: "display 1-in 2-out axis split of M and O at t+1 on the four z-probes of the two-axis opposite seed, and reverse/face from that split, not cover, not exist-opposite"
source_of_blocker_text: handoff
reachability_to_target: advances
artifact_role: theorem
next_trace_action: "Keep 1-in 2-out axis split of M and O at t+1 displayed; do not write split into Admissibility, do not reduce to cover, do not reduce to leftover-empty fail, do not reduce to leftover of M alone or leftover of O alone, do not replace split by existential opposite of signed locks, do not replace split by six-neighbor lock union, and do not attach L1."
conditional_surface_status: "exact on B_3(0) for 1-in 2-out axis split of M and O at t+1 on the four z-probes of the two-axis opposite seed and reverse/face from that split; displayed, not adopted"
hypothetical_axiom_status: "no edit"
admitted_observation_status: null
audit_required_before_effective_retained: true
bare_retained_allowed: false
```

## Displayed process

Write `e_1=(1,0,0)`, `e_2=(0,1,0)`, and `e_3=(0,0,1)`. The six nearest-neighbor
steps are

```text
NN = {+e_1,-e_1,+e_2,-e_2,+e_3,-e_3}.
```

The finite host is the closed Euclidean ball of radius 3 centered at the
origin,

```text
B_3(0) = { n in Z^3 : n·n <= 9 }.
```

No larger host is used. The four z-probes are the only sites whose 1-in
2-out axis split of `M` and `O` is scored:

```text
A = (0,0,1),  B = (1,1,1),  C = (0,0,2),  D = (1,0,1).
```

These are not the y-probes `A=(0,1,0)`, `B=(1,1,1)`, `C=(0,2,0)`,
`D=(1,1,0)`. These are not the x-probes `A=(1,0,0)`, `B=(1,1,1)`, `C=(2,0,0)`,
`D=(1,1,0)`. `A` is a seed of the second opposite pair. Same process and
z-probes as nm2axz.

Lock alphabet of the displayed process: `{±e_i}` with `i` in `{1,2,3}`.

Seed: two disjoint opposite pairs recorded at formation tick 0. Origin
locks `+e_1`. Site `(0,1,0)` locks `−e_1`. Site `(0,0,1)` locks `+e_2`.
Site `(0,1,1)` locks `−e_2`. The second pair is a new seed, not a formed
child of the first pair. This seed is not the 1-axis opposite two-site seed
`{0,(0,1,0)}` with only `+e_1/−e_1`. This seed is not the perp two-site
seed `+e_1/+e_2`. This seed is not the same-lock two-site seed
`+e_1/+e_1`. This seed is not the z-symmetric three-site seed
`{0,(0,0,1),(0,0,-1)}`. This seed is not the y-symmetric three-site seed
that also records `(0,-1,0)` at tick 0.

From a recorded site `p` with lock `L_in(p)=±e_i`, a six-neighbor step
`s in NN` to `q=p+s` is allowed if and only if `s` is perpendicular to
`e_i`, that is

```text
s · e_i = 0.
```

If `q` lies in `B_3(0)`, is still unformed, and the step is allowed, then `q`
forms next and locks the incoming step `s`. If several allowed parents reach
`q` at the same earliest formation, each such incoming step is kept. A later
parent does not re-form `q`. Uniqueness is not required. Mixed remains a set.

## Named 1-in 2-out axis split of `M` and `O` at `τ=t+1`

Let `t(q)` be the formation tick of z-probe `q` when that tick is defined in
`B_3(0)`. Let `τ(q)=t(q)+1`. There is no global T.

`M(q,τ)` is the set of earliest incoming nearest-neighbor steps at `q`
using only records with tick `<= τ`. If `q` is unformed at `τ`, then
`M(q,τ)` is `UNDEFINED`. If `q` is a seed and `τ >= 0`, then `M(q,τ)` is
the singleton seed letter.

`O(q,τ)` is the outgoing dual of `M`:

```text
O(q,τ) = { e in {±e_1,±e_2,±e_3} | q+e formed and e in M(q+e,τ) }.
```

If `q` is unformed at `τ`, then `O(q,τ)` is `UNDEFINED`. Empty `O` is empty,
not `UNDEFINED`. Duplicate steps collapse in the set. The construction does
not require `M` or `O` to be a singleton. It does not sum either set. It
does not replace `O` by `M`. It does not wait for a global later T.
Occupancy of sites is not used. O is not M.

Unsigned axis of a defined lock set:

```text
Axis(S) = { e_i | some ±e_i in S }.
```

Cover at a probe at the same cut:

```text
cover(q) HOLDs iff Axis(M) intersect Axis(O) is empty
and Axis(M) union Axis(O) equals {e_1,e_2,e_3}.
```

If `q` is unformed at `τ`, then cover is `UNDEFINED`. Overlapping axes fail.
Incomplete union fails. Axis is unsigned: `+e_i` and `−e_i` occupy the same
axis.

Split at a probe at the same cut:

```text
split(q) HOLDs iff cover HOLDs and |Axis(M)|=1
(hence |Axis(O)|=2).
```

2-in 1-out is fail of this object, not UNDEFINED: cover HOLD with
`|Axis(M)|=2` (hence `|Axis(O)|=1`) is split fail. Cover without the
one-axis incoming cardinality is not this object. Unique letters are not
this object. One-in one-out with leftover axis is cover fail and therefore
split fail.

Reverse 1-in 2-out holds if and only if split HOLDs at `A` and at `B`. Face
1-in 2-out holds if and only if split HOLDs at `C` and at `D`. Either side
`UNDEFINED` is `UNDEFINED`. Else if both sides HOLD, reverse or face HOLDs.
Else fail.

Identifying a named sign of those locks with reverse or face is refused:
named-sign lettering lost the axis. Identifying leftover-empty fail with
split reverse is refused: leftover-empty fail scores empty leftover as
fail. Identifying axis-cover reverse/face of the 1-axis opposite two-site
seed with this reverse/face is refused: that 1-axis cover HOLDs at every
z-probe, including 2-in 1-out `C`, so cover face HOLDs while split face
fails. Identifying nm2axz cover reverse/face with this reverse/face is
refused: cover without `|Axis(M)|=1` is a different object even when those
bits agree on this member.

## Theorem 1 — ticks, `M`, `O`, `Axis`, cover, `|Axis(M)|`, and split at `τ=t+1`

On this process the four z-probes form. Compare to the 1-axis opposite
two-site seed: that member forms `A` at tick 1 as a child locking `+e_3`,
forms `B` at tick 2, forms `C` at tick 4 with mixed 2-in 1-out `M`, and
forms `D` at tick 2. Cover HOLDs at every 1-axis z-probe, including 2-in
1-out `C`, so cover face HOLDs while split face fails. Here the second pair
is a new seed, not a formed child, so `(0,0,1)` is already recorded at tick
0 with lock `+e_2` and `(0,1,1)` is already recorded at tick 0 with lock
`−e_2`. This display reads the 1-in 2-out split of timed `M` and `O` on
that new seed:

```text
t(A)=0
t(B)=1
t(C)=1
t(D)=1
M(A, τ) = {+e_2}
M(B, τ) = {+e_1}
M(C, τ) = {+e_3}
M(D, τ) = {+e_1}
O(A, τ) = {+e_1, −e_1, +e_3}
O(B, τ) = {+e_2, +e_3, −e_3}
O(C, τ) = {+e_1, −e_1, −e_2}
O(D, τ) = {−e_2, +e_3, −e_3}
Axis(M)(A, τ) = {e_2}
Axis(O)(A, τ) = {e_1, e_3}
Axis(M)(B, τ) = {e_1}
Axis(O)(B, τ) = {e_2, e_3}
Axis(M)(C, τ) = {e_3}
Axis(O)(C, τ) = {e_1, e_2}
Axis(M)(D, τ) = {e_1}
Axis(O)(D, τ) = {e_2, e_3}
|Axis(M)|(A, τ) = 1
|Axis(O)|(A, τ) = 2
|Axis(M)|(B, τ) = 1
|Axis(O)|(B, τ) = 2
|Axis(M)|(C, τ) = 1
|Axis(O)|(C, τ) = 2
|Axis(M)|(D, τ) = 1
|Axis(O)|(D, τ) = 2
cover(A) = hold
cover(B) = hold
cover(C) = hold
cover(D) = hold
split(A) = hold
split(B) = hold
split(C) = hold
split(D) = hold
```

`A` is a seed at tick 0 with seed letter `+e_2`. Mixed remains a set:
`O(A,τ)` has three outgoing steps and `O(D,τ)` has three outgoing steps.
Unique letters would assign `UNDEFINED` at mixed `O`. Here uniqueness is
not required. At each probe, `Axis(M)` and `Axis(O)` are complementary:
their union is `{e_1,e_2,e_3}` and their intersection is empty. Cover
therefore HOLDs at each probe, and split HOLDs because `|Axis(M)|=1`. 2-in
1-out is fail of this object, not UNDEFINED; that identity remains, and it
is not the report at any of these four probes. Leftover of the union is
empty at each probe; leftover-empty fail of that leftover is not this
object.
O is not M.

Investment nm2axz cover on these four z-probes: cover HOLDs at every probe,
so cover reverse and cover face HOLD, and `|Axis(M)|=1` at each probe.
Cover without the one-axis incoming cardinality is still a different
object: 2-in 1-out is cover HOLD with split fail. On the 1-axis opposite
two-site seed that identity is live at `C`. On this two-axis member the
four split reports agree with cover, and reverse and face both HOLD. That
agreement is the first display of 1-in 2-out reverse HOLD and face HOLD on
this seed; it does not collapse split to cover. Leftover of `M` alone at
`A` is `{e_1,e_3}` and at `B` is `{e_2,e_3}`: nonempty and unequal.
Leftover of `O` alone at `A` is `{e_2}` and at `B` is `{e_1}`: nonempty and
unequal. Those one-sided leftovers are not this object.

New records in `B_3(0)` between `t` and `t+1` that meet a probe's
six-neighbors enter `O` and do not enter earliest `M`. Site `(0,1,1)` is a
seed, so it is not a new 6-NN of `A`:

```text
new 6-NN of A at t(A)+1: (1, 0, 1), (-1, 0, 1), (0, 0, 2)
new 6-NN of B at t(B)+1: (1, 2, 1), (1, 1, 2), (1, 1, 0)
new 6-NN of C at t(C)+1: (1, 0, 2), (-1, 0, 2), (0, -1, 2)
new 6-NN of D at t(D)+1: (1, -1, 1), (1, 0, 2), (1, 0, 0)
```

## Theorem 2 — reverse from 1-in 2-out split at `τ`

Reverse 1-in 2-out holds if and only if split HOLDs at `A` and at `B`.
Both splits HOLD. Reverse HOLDs. This is HOLD iff split, not leftover of
nmcover axis-cover, not leftover-empty fail, and not exist-opposite.

Reverse 1-in 2-out at τ: hold

Both sides are defined, so this is not `UNDEFINED`. Leftover-empty reverse
fails because leftover of the union is empty at `A` and at `B`. Cover
reverse HOLDs from complementary occupation of all three axes at `A` and at
`B`. Split reverse HOLDs because `A` and `B` are both 1-in 2-out. Leftover
of `M` reverse fails because leftover of `M` at `A` is `{e_1, e_3}` and at
`B` is `{e_2, e_3}`: nonempty and unequal. Leftover of `O` reverse fails
because leftover of `O` at `A` is `{e_2}` and at `B` is `{e_1}`: nonempty
and unequal. Exist-opposite reverse of signed `M` fails. Exist-opposite
reverse of signed `O` holds. Those leftovers are not this display.

Reverse holds.

## Theorem 3 — face from 1-in 2-out split at `τ`

Face 1-in 2-out holds if and only if split HOLDs at `C` and at `D`. Both
splits HOLD. Face HOLDs. 2-in 1-out is fail of this object, not UNDEFINED;
that identity is not the report at `C` or at `D` on this seed.

Face 1-in 2-out at τ: hold

Displayed, not adopted. The bits are not written into Admissibility.
Do not write into Admissibility. Do not attach L1.

Cover face HOLDs because cover HOLDs at `C` and at `D`. Split face HOLDs
because split HOLDs at `C` and at `D`. On this seed those two face bits
agree. They remain different predicates: 2-in 1-out is cover HOLD and split
fail. On the 1-axis opposite two-site seed, cover face HOLDs while split
face fails at `C` from 2-in 1-out. This two-axis member is not leftover of
that 1-axis split face fail. The four y-probes of this same seed give split
reverse hold and split face fail. The four x-probes give split reverse fail
and split face fail. Those probe-direction readouts are not this z-probe
display. Leftover-empty face fails because leftover of the union is empty
at `C` and at `D`. Leftover of `M` at `C` is `{e_1, e_2}` and leftover of
`M` at `D` is `{e_2, e_3}`: nonempty and unequal. Leftover of `O` at `C` is
`{e_3}` and leftover of `O` at `D` is `{e_1}`: nonempty and unequal.
Exist-opposite face of signed `M` fails. Exist-opposite face of signed `O`
fails. Split face HOLDs.

Empty leftover does not make reverse `UNDEFINED`. Leftover-empty fail is
not this reverse. Cover HOLDs at `D` and split HOLDs at `D`.

Face holds.

## What this note does not claim

- It does not select a unique incoming, outgoing, or leftover lock.
- It does not reduce lock vectors to named signs `{+,−}`.
- It does not require split sides to be singletons.
- It does not sum either set.
- It does not replace split by leftover-empty fail.
- It does not replace split by leftover of `M` alone.
- It does not replace split by leftover of `O` alone.
- It does not replace split by existential opposite of signed locks.
- It does not replace split by axis-cover without `|Axis(M)|=1`.
- It does not treat 2-in 1-out as `UNDEFINED`.
- It does not replace `O` by `M`.
- It does not replace split by locks of six-neighbors.
- It does not use a six-neighbor star as the letter.
- It does not wait for a global later T.
- It does not attach a formation member from already-recorded six-neighbor
  locks.
- It does not reprint nmsimopp exist-opposite of `M` and of `O` at `t+1`.
- It does not reprint nmcover axis-cover reverse hold face hold as this
  split display.
- It does not reprint nm2axz axis-cover reverse hold face hold as this
  split display.
- It does not reprint the 1-axis opposite two-site seed as this member.
- It does not score the y-probes or the x-probes as this letter.
- It does not reprint nmunopp untimed union.
- It does not reprint nmt2opp `M` frozen at `t` as this split display.
- It does not reprint nmot2opp two-tick composition of empty-then-HOLD `O`.
- It does not reprint nmoutopp untimed eventual-`O`.
- It does not reprint the two-tick lock-count clock composition.
- It does not reprint mixed #7188 fail/fail as this member.
- It does not use occupancy of sites as the letter.
- It does not enlarge the host beyond `B_3(0)`.
- It does not edit Lattice, Qubit, Admissibility, or Record.
- It does not supply a physical rate or a continuum kernel.

## Current premise boundary

The Lattice, Qubit, Admissibility, and Record premises are quoted from
[`MINIMAL_AXIOMS_2026-06-29.md`](MINIMAL_AXIOMS_2026-06-29.md):

Physical sites are the points of the cubic lattice `Z^3`, with nearest-neighbor
adjacency, standard translations, and proper cubic rotations about each site.

The full one-site possibility domain has algebraic presentation `M_2(C)`.

For each site, the probability distribution over the possibilities is determined by, and varies with, the nearest-neighbor conditions.

Records form.

When present, a record locks exactly one admissible local possibility.

A readout value is determined by record content alone.

A site with no record cannot be read.

The Admissibility reading note says the distribution concerns which possibility
a forming record locks, conditional on formation at that site; it does not
supply the formation site, probability, or rate.

This display uses Lattice to name `B_3(0)` and the four z-probes. It uses Qubit
only as the algebra of the local possibility domain. It uses Record only as a
boundary: a present lock is content. It does not rewrite Admissibility. The
two-axis opposite seed process, 1-in 2-out axis split of `M` and `O` at `t+1`,
and the reverse/face bits from that split are displayed theorem-domain data.

## Exact target and obligation graph

| Obligation | Status |
|---|---|
| current Lattice / Admissibility / Record premises | quoted; no edit |
| perp-step incoming-lock process on `B_3(0)` | displayed; two-axis opposite seed `+e_1/−e_1` and `+e_2/−e_2` |
| ticks `t(A)`, `t(B)`, `t(C)`, `t(D)` | Theorem 1; `0`, `1`, `1`, `1` |
| `M` at `τ=t+1` | Theorem 1; frozen equal to `M` at `t` |
| `O` at `τ=t+1` | Theorem 1; HOLDING outgoing dual |
| `Axis(M)` and `Axis(O)` at `τ` | Theorem 1; complementary at each probe |
| cover at `τ` | Theorem 1; HOLD at each probe |
| `|Axis(M)|` at `τ` | Theorem 1; `1,1,1,1` |
| split at `τ` | Theorem 1; HOLD at each probe |
| reverse from 1-in 2-out at `τ` | Theorem 2; `hold` |
| face from 1-in 2-out at `τ` | Theorem 3; `hold` |
| unique incoming lock | not required |
| occupancy of sites as the letter | not used |
| named-sign `{+,−}` letter | not used; lost the axis |
| singleton unique lock-vector letter | not used as the object; mixed remains a set |
| `Z^3` sum of the lock set | not used; no aggregation |
| six-neighbor star as the letter | not used |
| leftover-empty fail of leftover axis | not this split display |
| leftover of exist-opposite HOLD | not this split display |
| leftover of nmcover axis-cover HOLD | not this split display |
| leftover of nm2axz axis-cover HOLD | not this split display |
| y-probe or x-probe split on this seed | not this letter |
| leftover of leftover-of-`M` alone | not this display |
| leftover of leftover-of-`O` alone | not this display |
| leftover of nmunopp untimed union | not this display |
| leftover of nmt2opp `M` frozen at `t` | not this display |
| leftover of nmot2opp two-tick composition | not this display |
| leftover of nmoutopp untimed eventual-`O` | not this display |
| two-tick lock-count clock composition | not this display |
| leftover of mixed #7188 fail/fail | not this display |
| leftover of the 1-axis opposite two-site seed | not this display |
| leftover of the same-lock two-site seed | not this display |
| 2-in 1-out scored as `UNDEFINED` | refused; fail of this object |
| global later T | not used |
| 1-in 2-out split as Admissibility content | not adopted |
| formation site / probability / rate | open |
| physical Record readout of the bits | open |

## Value gate (V1–V5)

| # | Answer |
|---|---|
| V1 | It answers the first-display question: 1-in 2-out axis split of `M` and `O` at `t+1` on the four z-probes of the two-axis opposite seed, and reverse/face from that split. |
| V2 | Current main has no landed 1-in 2-out reverse/face of timed `M` and `O` on these four z-probes of the two-axis opposite seed. |
| V3 | Split reports at one cut and the two reverse/face bits are independently finite and exact. |
| V4 | The theorem is more than a restatement of Record because it reads unsigned 1-in 2-out split of own incoming and own outgoing at the same `t+1` cut and scores HOLD iff cover and `|Axis(M)|=1`. |
| V5 | It is not an adopted content rule: the bits remain displayed. |

## No-go discipline gate

The negative content is narrow: the display does not write those bits into
Admissibility, does not reduce them to named signs, does not require a
unique lock, does not replace split by leftover-empty fail, does not
replace split by leftover of `M` alone or leftover of `O` alone, does not
replace split by existential opposite of signed locks, does not replace
split by nmcover axis-cover, does not replace split by nm2axz axis-cover,
does not identify this display with the 1-axis opposite two-site seed, and
does not identify it with nmunopp union. No global impossibility is
claimed.

### N1 — materially distinct routes

| Route | Attempt | Why it fails here | Marker |
|---|---|---|---|
| nmcover axis-cover | score reverse/face as cover HOLD | on the 1-axis opposite two-site seed cover HOLDs at every z-probe so cover face HOLDs, while split face fails at `C` from 2-in 1-out; cover without `|Axis(M)|=1` is not this object | ATTEMPTED |
| nm2axz axis-cover | reuse cover reverse hold and cover face hold on these z-probes | cover HOLDs here and split HOLDs here because `|Axis(M)|=1`; 2-in 1-out remains cover HOLD and split fail on the 1-axis z-probes | ATTEMPTED |
| leftover-empty fail | score reverse/face as leftover nonempty-equal | leftover of the union is empty at each probe, leftover reverse and face fail, while split reverse and face HOLD | ATTEMPTED |
| leftover of `M` alone | score `{e_1,e_2,e_3}` minus `Axis(M)` | leftover of `M` at `A` is `{e_1,e_3}` and at `B` is `{e_2,e_3}`, nonempty unequal, reverse would fail | ATTEMPTED |
| leftover of `O` alone | score `{e_1,e_2,e_3}` minus `Axis(O)` | leftover of `O` at `A` is `{e_2}` and at `B` is `{e_1}`, nonempty unequal, reverse would fail | ATTEMPTED |
| exist-opposite | reuse signed reverse hold and face hold of `M` and of `O` | exist-opposite reverse of signed `M` fails while split reverse HOLDs; exist-opposite face of signed `O` fails while split face HOLDs | ATTEMPTED |
| nmunopp untimed union | score reverse/face from `M ∪ O` | union is signed letters; split is unsigned 1-in 2-out of `M` and `O` | ATTEMPTED |
| unique letter | replace mixed sets by a singleton or `UNDEFINED` | mixed `O(A,τ)` remains a set; split still HOLDs | ATTEMPTED |
| 2-in 1-out as `UNDEFINED` | treat `|Axis(M)|=2` cover as unformed | 2-in 1-out is fail of this object, not UNDEFINED; none of these four probes is 2-in 1-out | ATTEMPTED |
| letter intersection as split | score reverse/face inside `M ∩ O` | letter intersection empty is not 1-in 2-out; opposite signs can share an axis | ATTEMPTED |
| 1-axis opposite two-site seed | reuse `t(A)=1`, `t(C)=4`, mixed `M(C)`, split fail at `C` | different seed; second pair is a new seed, not a formed child; here `t(A)=0` and split HOLDs at `C` | ATTEMPTED |
| y-probe split | score the four y-probes on this seed | y-probe face fails at `D`; this letter is the four z-probes | ATTEMPTED |
| x-probe split | score the four x-probes on this seed | x-probe reverse fails at `A`; this letter is the four z-probes | ATTEMPTED |
| two-tick lock-count clock | score a lock-count clock across two ticks | different member; this display scores 1-in 2-out of own incoming and outgoing at `t+1` | ATTEMPTED |
| mixed #7188 fail/fail | reuse z-symmetric mixed `M` reverse-fail face-fail | different process; this member reports split HOLD and reverse hold face hold | ATTEMPTED |
| same-lock two-site seed | reuse `+e_1/+e_1` | different seed; this member is two disjoint opposite pairs | ATTEMPTED |
| sum of a set | replace split by a `Z^3` sum | the construction does not sum; split is cover plus `|Axis(M)|=1` | ATTEMPTED |
| named-sign lettering | collapse `{±e_i}` to `{+,−}` | named-sign lettering lost the axis | ATTEMPTED |
| global later T | wait until `max t(A,B,C,D)` before reading | `τ(q)=t(q)+1` is per-probe; no global T | ATTEMPTED |
| attach a formation member from already-recorded six-neighbor locks | form the probes by a neighbor-lock letter instead of perp-step | refused; not attached | ATTEMPTED |
| adopt bits into Admissibility | rewrite the local rule by 1-in 2-out split | refused; displayed, not adopted | ATTEMPTED |

### N2 — wall independence

Missing physical adoption, missing identification of split with leftover of
`M` alone, missing identification of split with leftover-empty fail, missing
identification of split with existential opposite of signed locks, missing
identification of split with nmcover axis-cover, missing identification of
split with nm2axz axis-cover, missing identification of this seed with the
1-axis opposite two-site seed, and missing Record identification of split
reverse are distinct open premises. This note claims no complete wall
collection.

### N3 — hidden-condition scan

The host `B_3(0)`, two disjoint opposite seed pairs `+e_1/−e_1` and
`+e_2/−e_2`, perpendicular step rule, incoming-step lock, own incoming set
and own outgoing dual from records with tick `<= τ`, per-probe `τ=t+1`,
unsigned axis, cover as complementary occupation of `{e_1,e_2,e_3}`, split
as cover and `|Axis(M)|=1`, 2-in 1-out as fail not `UNDEFINED`, four
z-probes with seed `A`, second pair as a new seed not a formed child, and
mixed remains a set are declared. No uniqueness of incoming locks, no
six-neighbor lock union as the scored object, no lock-count clock, no
global later T, no formation attachment from already-recorded six-neighbor
locks, and no Admissibility rewrite are silently assumed.

### N4 — source residual matching

The current axiom memo supplies cubic sites, `M_2(C)`,
content-conditional-on-formation, and unreadable absence. The residual that
formation site, probability, and rate remain unsupplied is unchanged. The
split `hold`/`fail` reports do not close that residual.

### N5 — resolution and rhetoric audit

| Resolution | Executed | Not claimed |
|---|---|---|
| per element | each unsigned lattice axis among `{e_1,e_2,e_3}` | no continuum alphabet |
| per site | `A,B,C,D` z-probes on `B_3(0)` only | no other cubic sites |
| per mode | no mode calculation | no spectral exhaustion |
| per block | four split reports, reverse/face from 1-in 2-out HOLD | no adopted content law |
| lattice wide | checked and not executed | no lattice-wide lettering rule |

### N6 — live partial-closure paths

Live routes include a later Record content map for split reverse/face, a
formation-rate rule, and a physical selector among 1-in 2-out axes. None
is taken here.

### N7 — hostile steelman

**Steelman:** Split HOLD is only cover HOLD; on this seed cover reverse and
cover face already match split reverse and split face; leftover of `M`
alone already answers reverse; leftover of `O` alone already answers
reverse; complementary occupation is only letter intersection empty; empty
leftover should be `UNDEFINED`; the second pair is only the formed child
`(0,0,1)` of the 1-axis seed; and exist-opposite already answers reverse.

**Answer:** Cover HOLDs at each of the four z-probes and split HOLDs
because `|Axis(M)|=1`. Split requires that cardinality in addition to
cover, so 2-in 1-out is cover HOLD and split fail even when those bits
agree on this seed. On the 1-axis opposite two-site seed, cover face HOLDs
while split face fails at `C` from 2-in 1-out. Letter intersection empty is
signed-letter disjointness. Opposite signs on one axis are letter-disjoint
and occupy that axis, so they are not cover and not 1-in 2-out. Leftover of
`M` alone at `A` is `{e_1,e_3}` and at `B` is `{e_2,e_3}`: nonempty unequal,
so leftover-of-`M` reverse fails while split reverse HOLDs. Leftover of `O`
alone at `A` is `{e_2}` and at `B` is `{e_1}`: leftover-of-`O` reverse
fails. `D` is formed at tick 1; 1-in 2-out is cover HOLD and split HOLD,
not UNDEFINED. The second pair is a new seed, not a formed child: `(0,0,1)`
is recorded at tick 0 with lock `+e_2`, whereas the 1-axis child forms at
tick 1 with lock `+e_3`. Exist-opposite reverse of signed `M` fails while
split reverse HOLDs. Reverse 1-in 2-out is HOLD iff split at `A` and at
`B`, not leftover of nm2axz axis-cover.

### N8 — cross-cycle echo

nsmopp #7208 reported reverse hold and face hold from own incoming `M` on
the 1-axis opposite two-site seed. nmcover axis-cover on that seed reported
cover HOLD at each of the four z-probes, reverse hold, and face hold, with
split face fail from 2-in 1-out at `C`. nm2axz cover on this two-axis seed
reported cover HOLD at each of the four z-probes, reverse hold, and face
hold, with `|Axis(M)|=1` at each probe. The four y-probes of this same seed
reported split reverse hold and split face fail. This note is not those
displays: it reports 1-in 2-out axis split of `M` and `O` at `τ=t+1` on
the two-axis opposite seed, with `t(A)=0`, `t(B)=1`, `t(C)=1`, and
`t(D)=1`, split HOLD at `A`, `B`, `C`, and `D`, reverse hold, and face
hold.

**Gate disposition:** PASS for the 1-in 2-out `t+1` reverse/face reports
above. FAIL / DO NOT SHIP for “the predicate equals the named sign,” “the
predicate equals the unique singleton lock vector,” “the predicate equals
six-neighbor lock union,” “the predicate equals leftover-empty fail,” “the
predicate equals leftover of `M` alone,” “the predicate equals leftover of
`O` alone,” “the predicate equals exist-opposite HOLD,” “the predicate
equals nmcover axis-cover HOLD,” “the predicate equals nm2axz axis-cover
HOLD,” “the predicate equals the 1-axis opposite two-site seed,” “the
predicate equals nmunopp union,” “bits are Admissibility,” “2-in 1-out is
UNDEFINED,” “reverse 1-in 2-out fails,” or “face 1-in 2-out fails.”

## Primary runner

The paired runner builds Euclidean `B_3(0)`, runs the two-axis opposite
perp-step incoming-lock process, reads each probe's own earliest incoming
set and own outgoing dual from the record prefix at that probe's `t+1`,
reports unsigned axis of each, reports cover of the pair, reports
`|Axis(M)|` and the 1-in 2-out split, lists new records in `B_3(0)` between
`t` and `t+1` that meet a probe's six-neighbors, and checks Theorems 1--3.
It also checks that split HOLDs at `A`, `B`, `C`, and `D`, that 2-in 1-out
is fail not `UNDEFINED`, that the 1-axis opposite two-site seed is a
different member with split face fail at `C`, that leftover-empty fail is
a different reverse and face, that leftover of `M` alone and leftover of
`O` alone are different objects, that mixed sets remain sets, that
unique-letter split is `UNDEFINED` at mixed `O`, that the construction does
not sum, that a formation member from already-recorded six-neighbor locks
is not attached, that the second pair is a new seed not a formed child,
that the y-probes and x-probes of this seed are not this letter, and that
the display is not the two-tick lock-count clock composition. No runner
cache is written.
