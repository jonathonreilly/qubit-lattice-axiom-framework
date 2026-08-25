---
claim_id: two_axis_opposite_xprobe_one_two_split_two_tick_composition_reverse_face_bounded_theorem_note_2026-08-15
claim_type: bounded_theorem
claim_scope: "1-in 2-out split at t versus t+1 on the four x-probes of the two-axis opposite seed, reverse/face at each cut, and composition, are reported. Displayed, not adopted."
upstream_dependencies:
  - minimal_axioms
runner: scripts/two_axis_opposite_xprobe_one_two_split_two_tick_composition_reverse_face_2026_08_15.py
---

# Two-Tick Composition Of 1-In 2-Out Split Reverse And Face On Four X-Probes Of The Two-Axis Opposite Seed

> **Key terms used in this doc** are indexed A-Z at `docs/KEY_TERMINOLOGY.md`;
> each row points to the canonical source-of-truth doc.

**Date:** 2026-08-15
**Type:** bounded_theorem
**Scope:** 1-in 2-out axis split of simultaneous earliest incoming set `M`
and outgoing dual `O` at each probe's `τ0=t` versus `τ1=t+1`, reverse/face
from that split at each cut, and composition HOLD iff split at `τ0` equals
split at `τ1` at `A,B,C,D`, on the four x-probes of the two-axis opposite
seed in `B_3(0)={n:n·n<=9}`. Same process and x-probes as nm2axx. `M`, `O`,
and split as nm2ax12x. Let `t(q)` be the formation tick of probe `q`. Let
`τ0(q)=t(q)` and `τ1(q)=t(q)+1`. There is no global T. `M(q,τ)` is the set
of earliest incoming nearest-neighbor steps at `q` using only records with
tick `<= τ`. Seeds are a singleton seed letter. `O(q,τ)` is the outgoing
dual of `M`: the set of `e` in `{±e_1,±e_2,±e_3}` such that `q+e` is formed
and `e` is in `M(q+e,τ)`. Unformed at `τ` is `UNDEFINED`. Empty `O` is
empty, not `UNDEFINED`. Axis of a defined lock set `S` is `Axis(S)={e_i |
some ±e_i in S}`. Cover holds at `q` if and only if `Axis(M)` intersect
`Axis(O)` is empty and `Axis(M)` union `Axis(O)` equals `{e_1,e_2,e_3}`.
Split holds at `q` if and only if cover holds and `|Axis(M)|=1`. Unformed
at `τ` is `UNDEFINED`. Else fail. Reverse holds if and only if split holds
at `A` and at `B`. Face holds if and only if split holds at `C` and at `D`.
Either side `UNDEFINED` is `UNDEFINED`. Composition HOLD if and only if
split at `τ0` equals split at `τ1` at `A`, at `B`, at `C`, and at `D`. Any
side `UNDEFINED` makes composition `UNDEFINED`. nm2ax12x split fail/fail at
`t+1` on these x-probes. This is the first display of that split at `t`
versus `t+1`. Empty `O` at `t` fails split at `A`, `B`, and `C`. `|Axis(M)|=1`
at each of the four x-probes at both cuts, so split equals cover on this
member. This is not leftover of M set equality. This is not leftover of
reverse/face-bit composition. This is not leftover of y-probe 1-in 2-out.
This is not leftover of 1-axis x-probe cover. This is not leftover-axis
reverse. This is not leftover of leftover-of-`M` alone. This is not leftover
of leftover-of-`O` alone. This is not leftover of same-lock two-axis. This
is not leftover of nsopp one-axis two-site seed. Uniqueness of incoming or
outgoing locks is not required. Mixed remains a set. Occupancy of sites is
not used. Named-sign lettering is not used. The construction does not use a
six-neighbor star. A is not a seed. Displayed, not adopted. Do not write
into Admissibility. Do not attach L1. This note does not write the 1-in
2-out split into Admissibility and does not attach a formation member from
already-recorded six-neighbor locks. This display does not use occupancy.
Mixed stays a set. O is not M.
**Audit-status authority:** independent audit lane only. This note authors no
audit verdict and predicts none.
**Primary runner:**
[`scripts/two_axis_opposite_xprobe_one_two_split_two_tick_composition_reverse_face_2026_08_15.py`](../scripts/two_axis_opposite_xprobe_one_two_split_two_tick_composition_reverse_face_2026_08_15.py)

Framework input:

- [`MINIMAL_AXIOMS_2026-06-29.md`](MINIMAL_AXIOMS_2026-06-29.md) supplies
  cubic-lattice sites `Z^3` with nearest-neighbor adjacency, the one-site
  algebra `M_2(C)`, and the Record sentences that records form and that a
  present record locks exactly one admissible local possibility.

Everything after that quoted input is a finite displayed process on `B_3(0)`
and the four named x-probes. Incoming lock letters are unit nearest-neighbor
steps. `O` is the outgoing dual of those incoming sets at the per-probe cuts
`τ0=t` and `τ1=t+1`. Axis is the unsigned lattice direction of a signed lock.
Cover is complementary occupation of `{e_1,e_2,e_3}` by `Axis(M)` and
`Axis(O)`. Split is cover together with `|Axis(M)|=1`. Reverse and face are
scored on split at the paired probes at each cut. Composition is equality of
the four split bits across the two cuts. Named signs `{+,−}` are a coarser
readout and are not used. A singleton unique lock letter is a different
readout and is not used as the object: mixed `O` remains a set. Existential
opposite of signed locks is a different readout and is not used as the split
reverse: exist-opposite of signed M fails reverse and face on these
x-probes. Equality of the four `M` sets is a different object: `M` is frozen
while split at `B` and at `C` changes when `O` fills. Reverse/face-bit
equality is a different object: those bits stay `fail` at both cuts while
split at `B` and at `C` changes. Occupancy of sites is not used. A
six-neighbor star is not the letter.

## Machine status and trace

```yaml
actual_current_surface_status: bounded-support
target_claim_type: bounded_theorem
claim_type_reason: "Exact report of 1-in 2-out axis split of M and O at t and at t+1 on the four x-probes of the two-axis opposite seed, empty O at t fails split at A,B,C, |Axis(M)|=1 at each probe so split equals cover, reverse fail and face fail at each cut, composition fail because split at B and at C changes from fail at t to hold at t+1; uniqueness of locks is not claimed and the bits are not adopted."
trace_class: frontier_discovery
target_claim_id: two_axis_opposite_xprobe_one_two_split_two_tick_composition_reverse_face
target_blocker_text: "display 1-in 2-out split at t versus t+1 on the four two-axis opposite x-probes, reverse/face from that split at each cut, and composition, where nm2ax12x split FAILs reverse and FAILs face at t+1"
source_of_blocker_text: handoff
reachability_to_target: advances
artifact_role: theorem
next_trace_action: "Keep 1-in 2-out split at t versus t+1 displayed; do not write split into Admissibility, do not reduce to M set equality, do not reduce to reverse/face-bit composition, do not reduce to y-probe 1-in 2-out, do not reduce to 1-axis x-probe cover, do not reduce to leftover-axis reverse, do not replace split by existential opposite of signed locks, and do not attach L1."
conditional_surface_status: "exact on B_3(0) for 1-in 2-out split at t versus t+1 on the four x-probes of the two-axis opposite seed, reverse/face at each cut, and composition; displayed, not adopted"
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

No larger host is used. The four x-probes are the only sites whose 1-in
2-out axis split of `M` and `O` is scored:

```text
A = (1,0,0),  B = (1,1,1),  C = (2,0,0),  D = (1,1,0).
```

These are not the y-probes `A=(0,1,0)`, `B=(1,1,1)`, `C=(0,2,0)`,
`D=(1,1,0)`. These are not the z-probes `A=(0,0,1)`, `B=(1,1,1)`,
`C=(0,0,2)`, `D=(1,0,1)`. A is not a seed. Same process and x-probes as
nm2axx.

Lock alphabet of the displayed process: `{±e_i}` with `i` in `{1,2,3}`.

Seed: two disjoint opposite pairs recorded at formation tick 0. Origin
locks `+e_1` and `(0,1,0)` locks `−e_1`. The second pair is a new seed, not
a formed child: `(0,0,1)` locks `+e_2` and `(0,1,1)` locks `−e_2`. Four
sites form at tick 0. This seed is not the nsopp one-axis two-site seed
`{0,(0,1,0)}` with locks `+e_1/−e_1`. This seed is not the same-lock
two-axis seed with `+e_1/+e_1` and `+e_2/+e_2`. This seed is not the nnseed
two-site seed `+e_1/+e_2`. This seed is not the y-axis opposite `±e_2` seed.

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

## Named 1-in 2-out split at `τ0=t` versus `τ1=t+1`

Let `t(q)` be the formation tick of x-probe `q` when that tick is defined in
`B_3(0)`. Let `τ0(q)=t(q)` and `τ1(q)=t(q)+1`. There is no global T.

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

Cover of `M` and `O` at the same cut:

```text
cover(q,τ) HOLD iff Axis(M(q,τ)) intersect Axis(O(q,τ)) is empty
and Axis(M(q,τ)) union Axis(O(q,τ)) equals {e_1,e_2,e_3}.
```

Split of `M` and `O` at the same cut:

```text
split(q,τ) HOLD iff cover(q,τ) HOLD and |Axis(M(q,τ))|=1.
```

If `q` is unformed at `τ`, then cover and split are `UNDEFINED`. Else fail.
Axis is unsigned: `+e_i` and `−e_i` occupy the same axis. Empty `O` fails
cover and therefore fails split.

Reverse 1-in 2-out at a cut holds if and only if split at `A` and split at
`B` both HOLD. Face 1-in 2-out at a cut holds if and only if split at `C`
and split at `D` both HOLD. Either side `UNDEFINED` is `UNDEFINED`. Else
fail.

Composition of split (displayed):

```text
composition HOLDs iff split(A,τ0)=split(A,τ1)
and split(B,τ0)=split(B,τ1)
and split(C,τ0)=split(C,τ1)
and split(D,τ0)=split(D,τ1).
```

Any side `UNDEFINED` makes composition `UNDEFINED`. Else if some probe's
split bit changes from `t` to `t+1`, composition fails. The scored object
is equality of the four split bits. Equality of the four `M` sets is a
different object. Equality of reverse/face bits is a different object.

Identifying leftover-axis reverse with this reverse is refused. Identifying
y-probe 1-in 2-out reverse with this reverse is refused: y-probe reverse
holds on this seed at `t+1`. Identifying 1-axis x-probe cover reverse with
this reverse is refused. Identifying existential opposite of signed locks
with split reverse is refused: exist-opposite of signed M fails reverse and
face here.

## Theorem 1 — ticks, `M`, `O`, and split at `τ0=t` and at `τ1=t+1`

On this process the four x-probes form. `M` is frozen: earliest incoming at
`τ1` equals earliest incoming at `τ0`. Empty `O` at `t` fails split at `A`,
`B`, and `C`. At `D`, `O` at `t` is already `{−e_1}` from the seed neighbor
`(0,1,0)`, leftover axis `{e_2}` is missing, and split fails. New records
at `t+1` fill `O`. Split then holds at `B` and at `C` and still fails at
`A` and at `D`. `|Axis(M)|=1` at each probe at both cuts, so split equals
cover on this member.

```text
t(A)=2
t(B)=1
t(C)=3
t(D)=2
M(A, τ0) = {−e_3}
M(B, τ0) = {+e_1}
M(C, τ0) = {+e_1}
M(D, τ0) = {−e_3}
M(A, τ1) = {−e_3}
M(B, τ1) = {+e_1}
M(C, τ1) = {+e_1}
M(D, τ1) = {−e_3}
O(A, τ0) = {}
O(B, τ0) = {}
O(C, τ0) = {}
O(D, τ0) = {−e_1}
O(A, τ1) = {+e_1}
O(B, τ1) = {+e_2, +e_3, −e_3}
O(C, τ1) = {−e_2, +e_3, −e_3}
O(D, τ1) = {+e_1, −e_1}
split(A, τ0) = fail
split(B, τ0) = fail
split(C, τ0) = fail
split(D, τ0) = fail
split(A, τ1) = fail
split(B, τ1) = hold
split(C, τ1) = hold
split(D, τ1) = fail
```

A is not a seed. `A` forms at tick 2 by the incoming step `−e_3`. Mixed
remains a set: `O(B,τ1)` has three outgoing steps and `O(D,τ1)` has two.
Unique letters would assign `UNDEFINED` at mixed `O`. Here uniqueness is
not required. O is not M. `M` at `τ1` is frozen equal to `M` at `τ0`. Empty
`O` is empty, not `UNDEFINED`.

New records in `B_3(0)` between `t` and `t+1` that meet a probe's
six-neighbors enter `O` and do not enter earliest `M`:

```text
new 6-NN of A at t(A)+1: (2, 0, 0)
new 6-NN of B at t(B)+1: (1, 2, 1), (1, 1, 2), (1, 1, 0)
new 6-NN of C at t(C)+1: (2, -1, 0), (2, 0, 1), (2, 0, -1)
new 6-NN of D at t(D)+1: (2, 1, 0)
```

Those new neighbors are why split at `B` and at `C` changes from fail at
`t` to hold at `t+1`, while `M` stays frozen.

## Theorem 2 — reverse and face at `τ0` and at `τ1`

Reverse 1-in 2-out holds if and only if split at `A` and split at `B` both
HOLD. At `τ0` split fails at `A` and at `B` because `O` is empty at both.
Reverse fails. At `τ1` split fails at `A` because leftover `{e_2}` is
missing, and split holds at `B`. Reverse fails.

Reverse 1-in 2-out at τ0: fail
Reverse 1-in 2-out at τ1: fail

Both sides are defined, so this is not `UNDEFINED`. Leftover-axis reverse
fails because leftover at `B` is empty while leftover at `A` is `{e_2}`.
Exist-opposite of signed M fails reverse: `{−e_3}` against `{+e_1}` has no
pair summing to zero. Y-probe 1-in 2-out reverse holds on this seed at
`t+1`. Those leftovers are not this display. Reverse fails at both cuts.

Face 1-in 2-out holds if and only if split at `C` and split at `D` both
HOLD. At `τ0` split fails at `C` and at `D`. Face fails. At `τ1` split
holds at `C` and fails at `D` because leftover `{e_2}` is missing. Face
fails.

Face 1-in 2-out at τ0: fail
Face 1-in 2-out at τ1: fail

Displayed, not adopted. The bits are not written into Admissibility.
Do not write into Admissibility. Do not attach L1.

nm2ax12x already reported reverse fail and face fail at `t+1`. This note
adds the same reverse/face predicates at `t`, where empty `O` fails split
at `A`, `B`, and `C`. Reverse fails at both cuts. Face fails at both cuts.

## Theorem 3 — composition of split at `t` versus `t+1`

Composition HOLD if and only if split at `τ0` equals split at `τ1` at `A`,
at `B`, at `C`, and at `D`. Split at `A` is fail at both cuts. Split at `D`
is fail at both cuts. Split at `B` changes from fail at `τ0` to hold at
`τ1`. Split at `C` changes from fail at `τ0` to hold at `τ1`. None is
`UNDEFINED`. Composition fails.

Composition of 1-in 2-out split at t versus t+1: fail

Displayed, not adopted. The bits are not written into Admissibility.
Do not write into Admissibility. Do not attach L1. Composition fail is
equality of the four split bits, not equality of reverse/face bits: those
bits match here (`fail`/`fail` at both cuts) by accident of the unpaired
split fails, and reverse/face-bit composition is a different object.
Composition fail is not leftover of M set equality: the four `M` sets are
frozen, so M composition HOLDs while split composition fails. Cover
composition also fails on this member because `|Axis(M)|=1` at each probe
at both cuts, so split equals cover; that coincidence is reported, not
hidden. New six-neighbor records between `t` and `t+1` enter `O` and flip
split at `B` and at `C`.

Composition fails.

## What this note does not claim

- It does not select a unique incoming, outgoing, or leftover lock.
- It does not reduce lock vectors to named signs `{+,−}`.
- It does not require `M` or `O` to be a singleton of signed letters.
- It does not sum either set.
- It does not replace split by leftover of `M` alone.
- It does not replace split by leftover of `O` alone.
- It does not replace split by leftover-axis equality of nonempty leftovers.
- It does not replace split by existential opposite of signed locks.
- It does not replace `O` by `M`.
- It does not replace split composition by M set equality.
- It does not replace split composition by reverse/face-bit composition.
- It does not replace split by locks of six-neighbors.
- It does not use a six-neighbor star as the letter.
- It does not wait for a global later T.
- It does not attach a formation member from already-recorded six-neighbor
  locks.
- It does not reprint leftover of y-probe 1-in 2-out.
- It does not reprint leftover of 1-axis x-probe cover.
- It does not reprint leftover-axis reverse.
- It does not reprint leftover of leftover-of-`M` alone.
- It does not reprint leftover of leftover-of-`O` alone.
- It does not reprint leftover of same-lock two-axis.
- It does not reprint leftover of nm2ax12x at `t+1` only.
- It does not reprint leftover of nm2t2x M two-tick composition HOLD.
- It does not treat split fail at `A` as 2-in 1-out: `|Axis(M)|=1` at `A`.
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

This display uses Lattice to name `B_3(0)` and the four x-probes. It uses Qubit
only as the algebra of the local possibility domain. It uses Record only as a
boundary: a present lock is content. It does not rewrite Admissibility. The
two-axis opposite process, 1-in 2-out axis split of `M` and `O` at `t` and at
`t+1`, reverse/face from that split at each cut, and composition as equality
of those four split bits are displayed theorem-domain data.

## Exact target and obligation graph

| Obligation | Status |
|---|---|
| current Lattice / Admissibility / Record premises | quoted; no edit |
| perp-step incoming-lock process on `B_3(0)` | displayed; two disjoint opposite pairs at tick 0 |
| ticks `t(A)`, `t(B)`, `t(C)`, `t(D)` | Theorem 1; `2`, `1`, `3`, `2` |
| `M` at `τ0=t` and at `τ1=t+1` | Theorem 1; frozen equal |
| `O` at `τ0=t` | Theorem 1; empty at `A,B,C`; `{−e_1}` at `D` |
| `O` at `τ1=t+1` | Theorem 1; outgoing dual fills |
| split at `τ0` | Theorem 1; fail at each of `A,B,C,D` |
| split at `τ1` | Theorem 1; fail at `A,D`, hold at `B,C` |
| reverse from split at `τ0` and `τ1` | Theorem 2; `fail`, `fail` |
| face from split at `τ0` and `τ1` | Theorem 2; `fail`, `fail` |
| composition of split at `t` versus `t+1` | Theorem 3; `fail` |
| unique lock | not required |
| occupancy of sites as the letter | not used |
| named-sign `{+,−}` letter | not used; lost the axis |
| singleton unique lock-vector letter | not used as the object; mixed remains a set |
| `Z^3` sum of the lock set | not used; no aggregation |
| six-neighbor star as the letter | not used |
| leftover of M set equality | not this split composition |
| leftover of reverse/face-bit composition | not this split composition |
| leftover of y-probe 1-in 2-out | not this split display |
| leftover of 1-axis x-probe cover | not this split display |
| leftover-axis reverse | not this split display |
| leftover of leftover-of-`M` alone | not this display |
| leftover of leftover-of-`O` alone | not this display |
| leftover of same-lock two-axis | not this display |
| leftover of nm2ax12x at `t+1` only | not this two-tick display |
| leftover of nm2t2x frozen `M` | not this letter |
| global later T | not used |
| 1-in 2-out split as Admissibility content | not adopted |
| formation site / probability / rate | open |
| physical Record readout of the bits | open |

## Value gate (V1–V5)

| # | Answer |
|---|---|
| V1 | It answers the first-display question: 1-in 2-out split at `t` versus `t+1` on the four x-probes of the two-axis opposite seed, reverse/face at each cut, and composition, where nm2ax12x split FAILs reverse and FAILs face at `t+1`. |
| V2 | Current main has no landed 1-in 2-out split two-tick composition reverse/face report on these four two-axis opposite x-probes. |
| V3 | Split bits at two cuts, reverse/face at each cut, and composition as equality of the four split bits are independently finite and exact. |
| V4 | The theorem is more than a restatement of Record because it reads unsigned 1-in 2-out of own incoming and own outgoing at `t` and at `t+1` and scores reverse/face and composition from that split. |
| V5 | It is not an adopted content rule: the bits remain displayed. |

## No-go discipline gate

The negative content is narrow: the display does not write those bits into
Admissibility, does not reduce them to named signs, does not require a
unique lock, does not replace split by leftover of `M` alone or leftover of
`O` alone, does not replace split by leftover-axis reverse, does not replace
split composition by M set equality, does not replace split composition by
reverse/face-bit composition, does not replace split by existential
opposite of signed locks, and does not identify this display with y-probe
1-in 2-out HOLD or with 1-axis x-probe cover HOLD. No global impossibility
is claimed.

### N1 — materially distinct routes

| Route | Attempt | Why it fails here | Marker |
|---|---|---|---|
| leftover of M set equality | HOLD iff `M(t)=M(t+1)` at `A,B,C,D` | `M` is frozen so that leftover HOLDs; split at `B` and at `C` changes; this composition fails | ATTEMPTED |
| leftover of reverse/face-bit composition | HOLD iff reverse/face bits match | reverse fail and face fail at both cuts, so bit leftover HOLDs; split at `B` and at `C` still changes | ATTEMPTED |
| leftover of y-probe 1-in 2-out | score reverse/face on `A=(0,1,0)` | y-probe `A` is a seed; y-probe reverse holds at `t+1`; x-probe reverse fails | ATTEMPTED |
| leftover of 1-axis x-probe cover | reuse nsopp `{0,(0,1,0)}` `+e_1/−e_1` | nsopp has two tick-0 sites; `t(A)=3` and mixed `M(A)`; here four tick-0 sites, `t(A)=2` | ATTEMPTED |
| leftover of same-lock two-axis | reuse `+e_1/+e_1` and `+e_2/+e_2` | seed letter at `(0,1,0)` is `−e_1` here; `O(D,τ1)` is `{+e_1, −e_1}` here and `{+e_1}` on same-lock | ATTEMPTED |
| leftover-axis reverse | score nonempty leftover-axis equality | leftover `{e_2}` at `A` and empty at `B`; leftover reverse fail | ATTEMPTED |
| leftover of `M` alone | score `{e_1,e_2,e_3}` minus `Axis(M)` | leftover of `M` at `A` is `{e_1,e_2}` and at `B` is `{e_2,e_3}`, nonempty unequal | ATTEMPTED |
| leftover of `O` alone | score `{e_1,e_2,e_3}` minus `Axis(O)` | leftover of `O` at `A` at `t+1` is `{e_2,e_3}` and at `B` is `{e_1}` | ATTEMPTED |
| leftover of nnseed `+e_1/+e_2` | reuse nnseed two-site seed | split at `A` and at `B` both fail from that seed | ATTEMPTED |
| leftover of y-axis opposite `±e_2` | reuse seed `{0,(0,1,0)}` with locks `±e_2` | this seed has four tick-0 sites and a second opposite pair on `e_2` | ATTEMPTED |
| leftover of z-probes on this seed | reuse `A=(0,0,1)` | z-probe `A` is a seed with split hold at `t+1`; x-probe `A` is not a seed | ATTEMPTED |
| leftover of nm2ax12x at `t+1` only | score split reverse/face at `t+1` without `t` | that leftover does not report split at `t` and does not score two-tick equality | ATTEMPTED |
| leftover of nm2t2x frozen `M` | reuse M two-tick composition HOLD | that leftover HOLDs because `M` is frozen; this letter fails because `O` fills | ATTEMPTED |
| exist-opposite of signed locks | score `a+b=(0,0,0)` inside `M` or `O` | exist-opposite of signed M fails reverse and face | ATTEMPTED |
| unique letter | replace mixed sets by a singleton or `UNDEFINED` | mixed `O(B,τ1)` remains a set; unique-letter split at `B` is `UNDEFINED`; this split at `B` at `t+1` is hold | ATTEMPTED |
| sum of a set | replace split by a `Z^3` sum | the construction does not sum; `O(D,τ1)` sums to `0` while `Axis(O)(D)` is `{e_1}` | ATTEMPTED |
| named-sign lettering | collapse `{±e_i}` to `{+,−}` | named-sign lettering lost the axis | ATTEMPTED |
| global later T | wait until `max t(A,B,C,D)` before reading | `τ0(q)=t(q)` and `τ1(q)=t(q)+1` are per-probe; no global T | ATTEMPTED |
| attach a formation member from already-recorded six-neighbor locks | form the probes by a neighbor-lock letter instead of perp-step | refused; not attached | ATTEMPTED |
| adopt bits into Admissibility | rewrite the local rule by 1-in 2-out | refused; displayed, not adopted | ATTEMPTED |

### N2 — wall independence

Missing physical adoption, missing identification of split composition with
M set equality, missing identification of split composition with
reverse/face-bit composition, missing identification of split with y-probe
1-in 2-out, missing identification of split with 1-axis x-probe cover,
missing identification of split with leftover-axis reverse, missing
identification of split with leftover of `M` alone, missing identification
of split with exist-opposite of signed `M`, and missing Record
identification of split reverse are distinct open premises. This note
claims no complete wall collection.

### N3 — hidden-condition scan

The host `B_3(0)`, two disjoint opposite pairs at tick 0, perpendicular
step rule, incoming-step lock, own incoming set and own outgoing dual from
records with tick `<= τ`, per-probe `τ0=t` and `τ1=t+1`, unsigned axis,
cover as empty intersection and three-axis union, split as cover together
with `|Axis(M)|=1`, composition as equality of the four split bits, four
x-probes with `A` not a seed, and mixed remains a set are declared. No
uniqueness of lock, no six-neighbor lock union as the scored object, no
leftover-axis equality as the scored reverse, no y-probe reverse as the
scored reverse, no M set equality as the scored composition, no
reverse/face-bit leftover as the composition object, no global later T, no
formation attachment from already-recorded six-neighbor locks, and no
Admissibility rewrite are silently assumed.

### N4 — source residual matching

The current axiom memo supplies cubic sites, `M_2(C)`,
content-conditional-on-formation, and unreadable absence. The residual that
formation site, probability, and rate remain unsupplied is unchanged. The
split reverse `fail` and face `fail` reports at both cuts, and composition
fail of the four split bits, do not close that residual.

### N5 — resolution and rhetoric audit

| Resolution | Executed | Not claimed |
|---|---|---|
| per element | each unsigned lattice axis among `{e_1,e_2,e_3}` | no continuum alphabet |
| per site | `A,B,C,D` x-probes on `B_3(0)` only | no other cubic sites |
| per mode | no mode calculation | no spectral exhaustion |
| per block | four split bits at two cuts, reverse/face at each cut, composition | no adopted content law |
| lattice wide | checked and not executed | no lattice-wide lettering rule |

### N6 — live partial-closure paths

Live routes include a later Record content map for 1-in 2-out reverse/face,
a formation-rate rule, and a physical selector among complementary axis
splits. None is taken here.

### N7 — hostile steelman

**Steelman:** Split two-tick composition should be refused as leftover
because nm2ax12x already reported reverse fail and face fail at `t+1`; `M`
is frozen so composition of the interesting object HOLDs; reverse/face bits
already match, so bit composition is enough; cover composition already
fails because split equals cover; empty `O` at `t` is only unfilled dual;
y-probe 1-in 2-out already holds reverse on this seed; 1-axis nsopp already
fails split reverse; leftover `{e_2}` already names the missing axis; and
mixed `O` is only unique-letter `UNDEFINED`.

**Answer:** nm2ax12x scores split at `t+1` only. This letter scores split at
`t` and at `t+1`, reverse/face at each cut, and composition as equality of
the four split bits. Those are extra reports, not a reprint. `M` is frozen,
so M composition HOLDs; split at `B` and at `C` changes from fail to hold
when new six-neighbor records fill `O`. That is the two-tick fact being
displayed. Reverse/face-bit equality HOLDs by accident of unpaired split
fails; it would HOLD even if those unpaired fails stayed unpaired while the
hold/fail pattern at the four probes changed. Cover composition fails with
split composition because `|Axis(M)|=1` at each probe at both cuts; that
coincidence is reported, not hidden, and cover is still a different object
without the `|Axis(M)|=1` cut. Empty `O` at `t` is empty, not `UNDEFINED`,
and fails split at `A`, `B`, and `C`. Y-probe reverse holds at `t+1` while
x-probe reverse fails. Unique-letter split at mixed `O(B)` at `t+1` is
`UNDEFINED`; this split at `B` at `t+1` is hold. Split reverse is HOLD of
split at `A` and at `B`. Composition of 1-in 2-out split fails.

### N8 — cross-cycle echo

nm2ax12x 1-in 2-out on these four x-probes fails reverse and fails face at
`t+1`. nm2axx cover on these four x-probes fails reverse and fails face at
`t+1`. nm2t2x reports frozen `M` composition HOLD with exist-opposite
reverse fail and face fail. Y-probe 1-in 2-out on this two-axis opposite
seed holds reverse and fails face at `t+1`. This note is not those
displays: it reports 1-in 2-out axis split of `M` and `O` at `τ0=t` and at
`τ1=t+1` on the two-axis opposite x-probes, empty `O` at `t` failing split
at `A`, `B`, and `C`, `|Axis(M)|=1` at each probe, reverse fail at both
cuts, face fail at both cuts, and composition fail because split at `B`
and at `C` changes from fail to hold.

**Gate disposition:** PASS for the 1-in 2-out two-tick reverse/face and
composition reports above. FAIL / DO NOT SHIP for “the predicate equals
the named sign,” “the predicate equals the unique singleton lock vector,”
“the predicate equals six-neighbor lock union,” “the predicate equals
leftover of `M` alone,” “the predicate equals leftover of `O` alone,” “the
predicate equals leftover-axis reverse,” “the predicate equals y-probe
1-in 2-out HOLD,” “the predicate equals 1-axis x-probe cover HOLD,” “the
predicate equals exist-opposite of signed M,” “composition equals M set
equality,” “composition equals reverse/face-bit equality,” “bits are
Admissibility,” “split holds at `A`,” “reverse 1-in 2-out holds,” “face
1-in 2-out holds,” “composition of split HOLDs,” or “empty leftover at `B`
is this reverse.”

## Primary runner

The paired runner builds Euclidean `B_3(0)`, runs the two-axis opposite
perp-step incoming-lock process, reads each probe's own earliest incoming
set and own outgoing dual from the record prefix at that probe's `t` and
at `t+1`, reports 1-in 2-out split at each cut, scores reverse and face
from split at each cut, scores composition as equality of the four split
bits, lists new records in `B_3(0)` between `t` and `t+1` that meet a
probe's six-neighbors, and checks Theorems 1--3. It also checks that empty
`O` at `t` fails split at `A`, `B`, and `C`, that `|Axis(M)|=1` at each
probe so split equals cover, that reverse fails and face fails at both
cuts, that composition fails because split at `B` and at `C` changes, that
M set equality HOLDs while split composition fails, that reverse/face-bit
composition HOLDs while split composition fails, that leftover empty at
`B` fails leftover reverse, that y-probe reverse holds while x-probe
reverse fails, that mixed `O` remains a set, that unique-letter split is
`UNDEFINED` at mixed `O(B)` while this split holds at `t+1`, that same-lock
two-axis has a different `O(D)`, that the construction does not sum, that a
formation member from already-recorded six-neighbor locks is not attached,
and that the display is not the nsopp one-axis leftover process. No runner
cache is written.
