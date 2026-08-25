---
claim_id: two_axis_opposite_yprobe_one_two_split_two_tick_composition_reverse_face_bounded_theorem_note_2026-08-15
claim_type: bounded_theorem
claim_scope: "1-in 2-out split at t versus t+1 on the four y-probes of the two-axis opposite seed, reverse/face at each cut, and composition, are reported. Displayed, not adopted."
upstream_dependencies:
  - minimal_axioms
runner: scripts/two_axis_opposite_yprobe_one_two_split_two_tick_composition_reverse_face_2026_08_15.py
---

# Two-Tick Composition Of One-In Two-Out Axis Split Reverse And Face On Four Y-Probes Of The Two-Axis Opposite Seed

> **Key terms used in this doc** are indexed A-Z at `docs/KEY_TERMINOLOGY.md`;
> each row points to the canonical source-of-truth doc.

**Date:** 2026-08-15
**Type:** bounded_theorem
**Scope:** 1-in 2-out axis split of simultaneous earliest incoming set `M`
and outgoing dual `O` at each probe's formation tick `t` versus `t+1`,
reverse/face from that split at each cut, and composition HOLD iff split
at `τ0` equals split at `τ1` at `A,B,C,D`, on the four y-probes of the
two-axis opposite seed in `B_3(0)={n:n·n<=9}`. Same process and y-probes
as nm2ax. `M`, `O`, and split as nm2ax12. Process: two disjoint opposite
pairs. Seed at tick 0: origin locks `+e_1`, `(0,1,0)` locks `−e_1`,
`(0,0,1)` locks `+e_2`, `(0,1,1)` locks `−e_2`. The second pair is a new
seed, not a formed child. Perp-step, incoming lock. Let `t(q)` be the
formation tick of probe `q`. Let `τ0(q)=t(q)` and `τ1(q)=t(q)+1`. There
is no global T. `M(q,τ)` is the set of earliest incoming nearest-neighbor
steps at `q` using only records with tick `<= τ`. Seeds are a singleton
seed letter. `O(q,τ)` is the outgoing dual of `M`: the set of `e` in
`{±e_1,±e_2,±e_3}` such that `q+e` is formed and `e` is in `M(q+e,τ)`.
Unformed at `τ` is `UNDEFINED`. Empty `O` is empty, not `UNDEFINED`. Empty
`O` at `t` fails split. Axis of a defined lock set `S` is
`Axis(S)={e_i | some ±e_i in S}`. Cover HOLDs at `q` if and only if
`Axis(M)` intersect `Axis(O)` is empty and `Axis(M)` union `Axis(O)` equals
`{e_1,e_2,e_3}`. Split HOLDs at `q` if and only if cover HOLDs and
`|Axis(M)|=1` (hence `|Axis(O)|=2`). 2-in 1-out is fail of this object,
not UNDEFINED. Reverse HOLDs if and only if split HOLDs at `A` and at `B`.
Face HOLDs if and only if split HOLDs at `C` and at `D`. Composition HOLD
if and only if split at `τ0` equals split at `τ1` at `A`, at `B`, at `C`,
and at `D`. This is not leftover of nm2ax12 `t+1`-only split reverse hold
and face fail. This is not leftover of nmcover axis-cover. This is
not leftover of nm2ax axis-cover. This is not
leftover of frozen-`M` two-tick set equality. This is not leftover of
reverse/face-bit composition as a substitute for equality of the four
split reports. This is not leftover of leftover-of-`M` alone. This is not
leftover of leftover-of-`O` alone. This is not leftover-empty fail. This
is not leftover of exist-opposite of signed locks. This is not leftover of
the 1-axis opposite two-site seed. This is not leftover of nmt2opp `M`
frozen at `t`. This is not leftover of mixed #7188 fail/fail. The second
pair is a new seed, not a formed child. Uniqueness is not required. Mixed
remains a set. Occupancy of sites is not used. Displayed, not adopted. Do
not write into Admissibility. Do not attach L1.
**Audit-status authority:** independent audit lane only. This note authors no
audit verdict and predicts none.
**Primary runner:**
[`scripts/two_axis_opposite_yprobe_one_two_split_two_tick_composition_reverse_face_2026_08_15.py`](../scripts/two_axis_opposite_yprobe_one_two_split_two_tick_composition_reverse_face_2026_08_15.py)

Framework input:

- [`MINIMAL_AXIOMS_2026-06-29.md`](MINIMAL_AXIOMS_2026-06-29.md) supplies
  cubic-lattice sites `Z^3` with nearest-neighbor adjacency, the one-site
  algebra `M_2(C)`, and the Record sentences that records form and that a
  present record locks exactly one admissible local possibility.

Everything after that quoted input is a finite displayed process on `B_3(0)`
and the four named y-probes. Incoming lock letters are unit nearest-neighbor
steps. `O` is the outgoing dual of those incoming sets at the per-probe cuts
`τ0=t` and `τ1=t+1`. Axis is the unsigned lattice direction of a signed lock.
Cover is the complementary occupation of `{e_1,e_2,e_3}` by `Axis(M)` and
`Axis(O)`. Split is cover together with `|Axis(M)|=1`. Reverse and face are
scored on split HOLD at the paired probes at each cut. Composition is
equality of those four split reports across the two cuts. Named signs
`{+,−}` are a coarser readout and are not used. A singleton unique lock
letter is a different readout and is not used as the object. Existential
opposite of signed locks is a different readout and is not used as the
split reverse. Axis-cover without the one-axis incoming cardinality is a
different readout and is not used. Frozen-`M` set equality is a different
readout and is not used as the composition object. Reverse/face-bit
equality is a different readout and is not used as the composition object.
Occupancy of sites is not used. A six-neighbor star is not the letter.

## Machine status and trace

```yaml
actual_current_surface_status: bounded-support
target_claim_type: bounded_theorem
claim_type_reason: "Exact report of 1-in 2-out axis split of M and O at t and at t+1 on the four y-probes of the two-axis opposite seed, empty O at t fails split so reverse fail and face fail at t, reverse hold and face fail at t+1 as nm2ax12, and composition fail because split at A,B,C changes from fail to hold; uniqueness of incoming locks is not claimed and the bits are not adopted."
trace_class: frontier_discovery
target_claim_id: two_axis_opposite_yprobe_one_two_split_two_tick_composition_reverse_face
target_blocker_text: "display 1-in 2-out split at t versus t+1 on the four y-probes of the two-axis opposite seed, reverse/face at each cut, and composition HOLD iff split at t equals split at t+1"
source_of_blocker_text: handoff
reachability_to_target: advances
artifact_role: theorem
next_trace_action: "Keep 1-in 2-out split two-tick composition displayed; do not write split into Admissibility, do not reduce to cover, do not reduce to frozen-M set equality, do not replace split equality by reverse/face-bit equality, do not replace split by existential opposite of signed locks, do not reprint nm2ax12 t+1-only reverse hold face fail as this two-tick report, and do not attach L1."
conditional_surface_status: "exact on B_3(0) for 1-in 2-out split at t versus t+1 on the four y-probes of the two-axis opposite seed, reverse/face at each cut, and composition; displayed, not adopted"
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

No larger host is used. The four y-probes are the only sites whose 1-in
2-out axis split of `M` and `O` is scored:

```text
A = (0,1,0),  B = (1,1,1),  C = (0,2,0),  D = (1,1,0).
```

These are not the x-probes `A=(1,0,0)`, `B=(1,1,1)`, `C=(2,0,0)`,
`D=(1,1,0)`. These are not the z-probes `A=(0,0,1)`, `B=(1,1,1)`,
`C=(0,0,2)`, `D=(1,0,1)`. `A` is a seed. Same process and y-probes as
nm2ax. `M`, `O`, and split as nm2ax12.

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

## Named 1-in 2-out axis split at `τ0=t` versus `τ1=t+1`

Let `t(q)` be the formation tick of y-probe `q` when that tick is defined in
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
not `UNDEFINED`. Empty `O` at `t` fails split. Empty O at t fails split. Duplicate steps collapse in
the set. The construction does not require `M` or `O` to be a singleton. It
does not sum either set. It does not replace `O` by `M`. It does not wait
for a global later T. Occupancy of sites is not used. O is not M.

Unsigned axis of a defined lock set:

```text
Axis(S) = { e_i | some ±e_i in S }.
```

Cover at a probe at a cut:

```text
cover(q) HOLDs iff Axis(M) intersect Axis(O) is empty
and Axis(M) union Axis(O) equals {e_1,e_2,e_3}.
```

If `q` is unformed at the cut, then cover is `UNDEFINED`. Overlapping axes
fail. Incomplete union fails, including empty `O`. Axis is unsigned: `+e_i`
and `−e_i` occupy the same axis.

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

Reverse 1-in 2-out at a cut holds if and only if split HOLDs at `A` and at
`B` at that cut. Face 1-in 2-out at a cut holds if and only if split HOLDs
at `C` and at `D` at that cut. Either side `UNDEFINED` is `UNDEFINED`. Else
if both sides HOLD, reverse or face HOLDs. Else fail.

Composition of split (displayed):

```text
composition HOLDs iff split(A,τ0)=split(A,τ1)
and split(B,τ0)=split(B,τ1)
and split(C,τ0)=split(C,τ1)
and split(D,τ0)=split(D,τ1).
```

Any side `UNDEFINED` makes composition `UNDEFINED`. Else if some probe's
split report changes from `t` to `t+1`, composition fails. Equality of the
four `M` sets is a different object: those sets may stay equal while split
changes because `O` fills in. Equality of reverse/face bits is a different
object: those bits may match while some probe's split changes, and they
may fail to match while the four split reports stay equal. This letter is
equality of the four split reports.

Admissibility is not edited. Split is not written into Admissibility. Do
not write into Admissibility. Do not attach L1.

## Theorem 1 — ticks, `M`, `O`, and split at `τ0=t` and at `τ1=t+1`

On this process the four y-probes form. Earliest incoming `M` is frozen
from `t` to `t+1`. Outgoing dual `O` is empty at `A`, `B`, and `C` at
formation tick, and is `{−e_1}` at `D` at formation tick. Empty `O` at `t`
fails split. At `t+1` the nm2ax12 HOLDING outgoing duals appear at `A`,
`B`, and `C`, and `D` remains 1-in 1-out.

```text
t(A)=0
t(B)=1
t(C)=1
t(D)=2
M(A, τ0) = {−e_1}
M(B, τ0) = {+e_1}
M(C, τ0) = {+e_2}
M(D, τ0) = {−e_3}
M(A, τ1) = {−e_1}
M(B, τ1) = {+e_1}
M(C, τ1) = {+e_2}
M(D, τ1) = {−e_3}
O(A, τ0) = {}
O(B, τ0) = {}
O(C, τ0) = {}
O(D, τ0) = {−e_1}
O(A, τ1) = {+e_2, −e_3}
O(B, τ1) = {+e_2, +e_3, −e_3}
O(C, τ1) = {+e_1, −e_1, +e_3, −e_3}
O(D, τ1) = {+e_1, −e_1}
split(A, τ0) = fail
split(B, τ0) = fail
split(C, τ0) = fail
split(D, τ0) = fail
split(A, τ1) = hold
split(B, τ1) = hold
split(C, τ1) = hold
split(D, τ1) = fail
```

`A` is a seed at tick 0. Mixed remains a set: `O(A,τ1)` has two outgoing
steps and `O(B,τ1)` has three outgoing steps. Unique letters would assign
`UNDEFINED` at mixed `O`. Here uniqueness is not required. At `τ0`, empty
`O` at `A`, `B`, and `C` makes union of axes incomplete, so cover fails
and split fails. At `D` at `τ0`, `Axis(M)={e_3}` and `Axis(O)={e_1}`, so
leftover of the union is `{e_2}`: 1-in 1-out, cover fail, split fail. At
`τ1`, `A`, `B`, and `C` are 1-in 2-out, so split HOLDs, and `D` remains
1-in 1-out with leftover `{e_2}`, so split fails. 2-in 1-out is fail of
this object, not UNDEFINED; that identity remains, and it is not the `D`
report on this seed. O is not M. Frozen `M` is not this composition
object.

New records in `B_3(0)` between `t` and `t+1` that meet a probe's
six-neighbors enter `O` and do not enter earliest `M`. Site `(0,1,1)` is a
seed, so it is not a new 6-NN of `A`:

```text
new 6-NN of A at t(A)+1: (0, 2, 0), (0, 1, -1)
new 6-NN of B at t(B)+1: (1, 2, 1), (1, 1, 2), (1, 1, 0)
new 6-NN of C at t(C)+1: (1, 2, 0), (-1, 2, 0), (0, 2, 1), (0, 2, -1)
new 6-NN of D at t(D)+1: (2, 1, 0)
```

Compare to nm2ax12 `t+1` only. Same seed, same y-probes, same `M` and `O`
at `τ1`, same split HOLD at `A`, `B`, and `C` and fail at `D`, reverse
hold and face fail. That leftover does not score split at `t`, does not
score reverse/face at `t`, and does not score two-tick split equality.
Compare to 1-axis opposite two-site seed: that member forms `B` at tick 2
and `D` at tick 3, has mixed `M(D,τ)`, and has cover HOLD at `D` from 2-in
1-out. Here the second pair is a new seed, not a formed child.

## Theorem 2 — reverse and face at `τ0` and at `τ1`

Reverse 1-in 2-out holds if and only if split HOLDs at `A` and at `B`. At
`τ0` both splits fail from empty `O`. Reverse fails. At `τ1` both splits
HOLD. Reverse HOLDs. This is HOLD iff split, not leftover of nmcover
axis-cover, not leftover-empty fail, and not exist-opposite.

Reverse 1-in 2-out at τ0: fail
Reverse 1-in 2-out at τ1: hold

Both sides are defined, so this is not `UNDEFINED`. Reverse fails at `t`
and HOLDs at `t+1`. Frozen-`M` exist-opposite reverse HOLDs at both cuts
because `M(A)={−e_1}` and `M(B)={+e_1}` are frozen. Cover reverse fails at
`t` and HOLDs at `t+1`, which agrees on the bits by accident of empty `O`
at `t` and complementary occupation at `t+1`. Those leftovers are not this
display.

Reverse fails at τ0.
Reverse holds at τ1.

Face 1-in 2-out holds if and only if split HOLDs at `C` and at `D`. At
`τ0` split fails at `C` from empty `O` and fails at `D` from 1-in 1-out.
Face fails. At `τ1` split HOLDs at `C` and fails at `D`. Face fails. The
`D` failure at both cuts is cover fail from leftover `{e_2}` (1-in 1-out),
which is fail of this object, not UNDEFINED.

Face 1-in 2-out at τ0: fail
Face 1-in 2-out at τ1: fail

Displayed, not adopted. The bits are not written into Admissibility.
Do not write into Admissibility. Do not attach L1.

Face fails at both cuts. Cover face fails at both cuts by the same `D`
cover fail at `t+1` and by empty `O` at `C` at `t`. Split face fails
because split fails at `D` at both cuts and at `C` at `t`. Exist-opposite
face of signed `M` fails at both cuts. Exist-opposite face of signed `O`
is `UNDEFINED` at `t` from empty `O` and HOLDs at `t+1`. Those leftovers
are not this split face.

Face fails at τ0.
Face fails at τ1.

## Theorem 3 — composition of split at `t` versus `t+1`

Composition HOLD if and only if split at `τ0` equals split at `τ1` at
`A`, at `B`, at `C`, and at `D`. Split at `A`, `B`, and `C` changes from
fail to hold. Split at `D` stays fail. None is `UNDEFINED`.

Composition of split at t versus t+1: fail

Displayed, not adopted. The bits are not written into Admissibility.
Do not write into Admissibility. Do not attach L1. Composition fail is
inequality of the four split reports, not inequality of the four `M`
sets: those four `M` sets stay equal (frozen earliest incoming), so
frozen-`M` two-tick composition HOLDs while this split composition fails.
New six-neighbor records between `t` and `t+1` enter `O` and do not enter
earliest `M`. Reverse/face-bit composition also fails here because reverse
changes from fail to hold; that leftover is still a different object,
because it scores two pair bits rather than the four split reports.

This is not leftover of nm2ax12 `t+1`-only reverse hold and face fail:
that display does not score split at `t`. This is not leftover of nmt2opp
`M` frozen at `t` as a different seed. This is not leftover of mixed
#7188 fail/fail. This is not leftover of the two-tick lock-count clock
composition.

Composition fails.

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
- It does not replace composition of the four split reports by frozen-`M`
  set equality.
- It does not replace composition of the four split reports by
  reverse/face-bit equality.
- It does not replace split by locks of six-neighbors.
- It does not use a six-neighbor star as the letter.
- It does not wait for a global later T.
- It does not attach a formation member from already-recorded six-neighbor
  locks.
- It does not reprint nm2ax12 `t+1`-only reverse hold and face fail as this
  two-tick report.
- It does not reprint nmcover axis-cover reverse hold face fail as this
  split composition.
- It does not reprint the 1-axis opposite two-site seed as this member.
- It does not reprint nmt2opp `M` frozen at `t` as this split display.
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

This display uses Lattice to name `B_3(0)` and the four y-probes. It uses Qubit
only as the algebra of the local possibility domain. It uses Record only as a
boundary: a present lock is content. It does not rewrite Admissibility. The
two-axis opposite seed process, 1-in 2-out axis split of `M` and `O` at `t`
and at `t+1`, reverse/face from that split at each cut, and composition of
those four split reports are displayed theorem-domain data.

## Exact target and obligation graph

| Obligation | Status |
|---|---|
| current Lattice / Admissibility / Record premises | quoted; no edit |
| perp-step incoming-lock process on `B_3(0)` | displayed; two-axis opposite seed `+e_1/−e_1` and `+e_2/−e_2` |
| ticks `t(A)`, `t(B)`, `t(C)`, `t(D)` | Theorem 1; `0`, `1`, `1`, `2` |
| `M` at `τ0=t` and at `τ1=t+1` | Theorem 1; frozen equal |
| `O` at `τ0=t` and at `τ1=t+1` | Theorem 1; empty at `A,B,C` at `t`; HOLDING at `t+1` |
| split at `τ0` | Theorem 1; fail at `A,B,C,D`; empty `O` at `t` fails split |
| split at `τ1` | Theorem 1; HOLD at `A,B,C`; fail at `D` |
| reverse from 1-in 2-out at `τ0` and `τ1` | Theorem 2; `fail`, `hold` |
| face from 1-in 2-out at `τ0` and `τ1` | Theorem 2; `fail`, `fail` |
| composition of split at `t` versus `t+1` | Theorem 3; `fail` |
| unique incoming lock | not required |
| occupancy of sites as the letter | not used |
| named-sign `{+,−}` letter | not used; lost the axis |
| singleton unique lock-vector letter | not used as the object; mixed remains a set |
| `Z^3` sum of the lock set | not used; no aggregation |
| six-neighbor star as the letter | not used |
| leftover-empty fail of leftover axis | not this split display |
| leftover of exist-opposite HOLD | not this split display |
| leftover of nmcover axis-cover | not this split display |
| leftover of leftover-of-`M` alone | not this display |
| leftover of leftover-of-`O` alone | not this display |
| leftover of frozen-`M` two-tick set equality | not this composition |
| leftover of reverse/face-bit composition | not this composition |
| leftover of nm2ax12 `t+1`-only split | not this two-tick report |
| leftover of nmt2opp `M` frozen at `t` | not this display |
| leftover of mixed #7188 fail/fail | not this display |
| leftover of the 1-axis opposite two-site seed | not this display |
| leftover of the two-tick lock-count clock | not this display |
| 2-in 1-out scored as `UNDEFINED` | refused; fail of this object |
| global later T | not used |
| 1-in 2-out split as Admissibility content | not adopted |
| formation site / probability / rate | open |
| physical Record readout of the bits | open |

## Value gate (V1–V5)

| # | Answer |
|---|---|
| V1 | It answers the first-display question: 1-in 2-out split at `t` versus `t+1` on the four y-probes of the two-axis opposite seed, reverse/face at each cut, and composition. |
| V2 | Current main has no landed 1-in 2-out two-tick composition reverse/face report on these four y-probes of the two-axis opposite seed. |
| V3 | Split reports at two cuts, the four reverse/face bits, and composition as split equality are independently finite and exact. |
| V4 | The theorem is more than a restatement of Record because it reads unsigned 1-in 2-out split of own incoming and own outgoing at `t` and at `t+1` and scores equality of those four reports. |
| V5 | It is not an adopted content rule: the bits remain displayed. |

## No-go discipline gate

The negative content is narrow: the display does not write those bits into
Admissibility, does not reduce them to named signs, does not require a
unique lock, does not replace split by leftover-empty fail, does not
replace split by leftover of `M` alone or leftover of `O` alone, does not
replace split by existential opposite of signed locks, does not replace
split by nmcover axis-cover, does not replace split equality by frozen-`M`
set equality, does not replace split equality by reverse/face-bit
equality, does not identify this display with nm2ax12 `t+1` only, does not
identify this display with the 1-axis opposite two-site seed, and does not
identify it with nmt2opp frozen `M`. No global impossibility is claimed.

### N1 — materially distinct routes

| Route | Attempt | Why it fails here | Marker |
|---|---|---|---|
| nm2ax12 `t+1` only | reuse reverse hold and face fail at `t+1` | that leftover does not score split at `t`; reverse fails at `t` from empty `O` | ATTEMPTED |
| frozen-`M` two-tick set equality | HOLD iff `M(t)=M(t+1)` at `A,B,C,D` | the four `M` sets stay equal, so that leftover HOLDs while split composition fails | ATTEMPTED |
| reverse/face-bit composition | HOLD iff reverse/face bits match | those two pair bits fail here because reverse changes; the scored object is still the four split reports | ATTEMPTED |
| nmcover axis-cover | score reverse/face as cover HOLD | cover reverse fails at `t` and HOLDs at `t+1` with split; 2-in 1-out is still cover HOLD and split fail | ATTEMPTED |
| leftover-empty fail | score reverse/face as leftover nonempty-equal | leftover of the union is empty at `A` and at `B` at `t+1`, leftover reverse fails, while split reverse HOLDs at `t+1` | ATTEMPTED |
| leftover of `M` alone | score `{e_1,e_2,e_3}` minus `Axis(M)` | leftover of `M` is frozen and is not `|Axis(M)|=1` cover of the pair | ATTEMPTED |
| leftover of `O` alone | score `{e_1,e_2,e_3}` minus `Axis(O)` | empty `O` at `t` makes leftover of `O` the full three axes; that is not this split | ATTEMPTED |
| exist-opposite of signed `M` | reuse signed reverse hold and face fail of frozen `M` | exist-opposite reverse HOLDs at both cuts while split reverse fails at `t` | ATTEMPTED |
| exist-opposite of signed `O` | score reverse/face inside `O` | empty `O` at `t` makes exist-opposite `UNDEFINED`; split reverse is fail, not `UNDEFINED` | ATTEMPTED |
| unique letter | replace mixed sets by a singleton or `UNDEFINED` | mixed `O(A,τ1)` and mixed `O(B,τ1)` remain sets; split still reports hold at `A` at `t+1` and fail at `D` | ATTEMPTED |
| 2-in 1-out as `UNDEFINED` | treat `|Axis(M)|=2` cover as unformed | 2-in 1-out is fail of this object, not UNDEFINED; `D` here is 1-in 1-out cover fail, also not UNDEFINED | ATTEMPTED |
| 1-axis opposite two-site seed | reuse `t(B)=2`, `t(D)=3`, mixed `M(D)`, cover HOLD at `D` | different seed; second pair is a new seed, not a formed child | ATTEMPTED |
| nmt2opp `M` frozen at `t` | reuse 1-axis y-probe two-tick `M` | different seed and different letter; this letter is split equality | ATTEMPTED |
| two-tick lock-count clock | score a lock-count clock across two ticks | different member; this display scores 1-in 2-out of own incoming and outgoing at two cuts | ATTEMPTED |
| mixed #7188 fail/fail | reuse z-symmetric mixed `M` reverse-fail face-fail | different process; this member reports split reverse fail at `t` and hold at `t+1` | ATTEMPTED |
| same-lock two-site seed | reuse `+e_1/+e_1` | different seed; this member is two disjoint opposite pairs | ATTEMPTED |
| sum of a set | replace split by a `Z^3` sum | the construction does not sum; split is cover plus `|Axis(M)|=1` | ATTEMPTED |
| named-sign lettering | collapse `{±e_i}` to `{+,−}` | named-sign lettering lost the axis | ATTEMPTED |
| global later T | wait until `max t(A,B,C,D)` before reading | `τ0(q)=t(q)` and `τ1(q)=t(q)+1` are per-probe; no global T | ATTEMPTED |
| attach a formation member from already-recorded six-neighbor locks | form the probes by a neighbor-lock letter instead of perp-step | refused; not attached | ATTEMPTED |
| adopt bits into Admissibility | rewrite the local rule by 1-in 2-out split | refused; displayed, not adopted | ATTEMPTED |

### N2 — wall independence

Missing physical adoption, missing identification of split with leftover of
`M` alone, missing identification of split composition with frozen-`M` set
equality, missing identification of split with leftover-empty fail, missing
identification of split with existential opposite of signed locks, missing
identification of split with nmcover axis-cover, missing identification of
this seed with the 1-axis opposite two-site seed, missing identification of
this two-tick report with nm2ax12 `t+1` only, and missing Record
identification of split reverse are distinct open premises. This note claims
no complete wall collection.

### N3 — hidden-condition scan

The host `B_3(0)`, two disjoint opposite seed pairs `+e_1/−e_1` and
`+e_2/−e_2`, perpendicular step rule, incoming-step lock, own incoming set
and own outgoing dual from records with tick `<= τ`, per-probe `τ0=t` and
`τ1=t+1`, unsigned axis, cover as complementary occupation of
`{e_1,e_2,e_3}`, split as cover and `|Axis(M)|=1`, empty `O` at `t` fails
split, 2-in 1-out as fail not `UNDEFINED`, composition as equality of the
four split reports, four y-probes with seed `A`, second pair as a new seed
not a formed child, and mixed remains a set are declared. No uniqueness of
incoming locks, no six-neighbor lock union as the scored object, no
lock-count clock, no frozen-`M` leftover as the composition object, no
reverse/face-bit leftover as the composition object, no global later T, no
formation attachment from already-recorded six-neighbor locks, and no
Admissibility rewrite are silently assumed.

### N4 — source residual matching

The current axiom memo supplies cubic sites, `M_2(C)`,
content-conditional-on-formation, and unreadable absence. The residual that
formation site, probability, and rate remain unsupplied is unchanged. The
split `hold`/`fail` reports at two cuts, and composition fail, do not close
that residual.

### N5 — resolution and rhetoric audit

| Resolution | Executed | Not claimed |
|---|---|---|
| per element | each unsigned lattice axis among `{e_1,e_2,e_3}` | no continuum alphabet |
| per site | `A,B,C,D` y-probes on `B_3(0)` only | no other cubic sites |
| per mode | no mode calculation | no spectral exhaustion |
| per block | four split reports at two cuts, reverse/face at each cut, and composition | no adopted content law |
| lattice wide | checked and not executed | no lattice-wide lettering rule |

### N6 — live partial-closure paths

Live routes include a later Record content map for split reverse/face, a
formation-rate rule, and a physical selector among 1-in 2-out axes. None
is taken here.

### N7 — hostile steelman

**Steelman:** Split two-tick composition should be refused as leftover
because nm2ax12 already reported reverse hold and face fail at `t+1`;
`M` is frozen so composition of `M` already answers two ticks; empty `O`
at `t` should be `UNDEFINED` like unformed; cover already matches split
at both cuts on this seed; leftover of `M` alone is frozen; exist-opposite
of signed `M` already HOLDs reverse at both cuts; reverse/face-bit
composition already fails; and 1-in 1-out at `D` should be `UNDEFINED`.

**Answer:** nm2ax12 scores split at `t+1` only. This letter scores split at
`t` and at `t+1`, reverse/face at each cut, and composition as equality of
the four split reports. Those are extra reports, not a reprint. Frozen-`M`
two-tick composition HOLDs because earliest incoming does not change; split
composition fails because empty `O` at `t` fills in at `t+1` at `A`, `B`,
and `C`. Empty `O` is empty, not `UNDEFINED`; unformed at `τ` is
`UNDEFINED`. Cover HOLDs at `A`, `B`, and `C` at `t+1` and fails at `D`
from leftover `{e_2}`. Split requires `|Axis(M)|=1` in addition to cover, so
2-in 1-out is cover HOLD and split fail even when those bits agree on this
seed. Exist-opposite reverse of signed `M` HOLDs at both cuts while split
reverse fails at `t`. Reverse/face-bit composition scores two pair bits;
this letter scores four split reports. `D` is formed at tick 2; 1-in 1-out
is cover fail and split fail, not UNDEFINED. Reverse 1-in 2-out fails at
`t` and HOLDs at `t+1`. Face fails at both cuts. Composition of split
fails.

### N8 — cross-cycle echo

nm2ax12 reported 1-in 2-out reverse hold and face fail at `t+1` on these
y-probes, with split HOLD at `A`, `B`, and `C` and fail at `D`. nm2ax
reported axis-cover reverse hold and face fail at `t+1`. nsmopp #7208
reported reverse hold and face hold from own incoming `M` on the 1-axis
opposite two-site seed. The 1-axis 1-in 2-out split reported split HOLD at
`A`, `B`, and `C`, split fail at `D` from 2-in 1-out, reverse hold, and
face fail, with `t(B)=2` and `t(D)=3`. Frozen-`M` two-tick composition on
this two-axis seed HOLDs. This note is not those displays: it reports 1-in
2-out axis split of `M` and `O` at `τ0=t` and at `τ1=t+1` on the two-axis
opposite seed, with `t(B)=1` and `t(D)=2`, split fail at all four probes at
`t` from empty `O` or leftover `{e_2}`, split HOLD at `A`, `B`, and `C` and
fail at `D` at `t+1`, reverse fail at `t` and hold at `t+1`, face fail at
both cuts, and composition fail.

**Gate disposition:** PASS for the 1-in 2-out two-tick reverse/face and
composition reports above. FAIL / DO NOT SHIP for “the predicate equals
the named sign,” “the predicate equals the unique singleton lock vector,”
“the predicate equals six-neighbor lock union,” “the predicate equals
leftover-empty fail,” “the predicate equals leftover of `M` alone,” “the
predicate equals leftover of `O` alone,” “the predicate equals
exist-opposite HOLD,” “the predicate equals nmcover axis-cover HOLD,”
“the predicate equals nm2ax12 `t+1` only,” “the predicate equals frozen-`M`
set equality,” “composition equals reverse/face-bit equality,” “the
predicate equals the 1-axis opposite two-site seed,” “bits are
Admissibility,” “2-in 1-out is UNDEFINED,” “reverse 1-in 2-out holds at
`t`,” “reverse 1-in 2-out fails at `t+1`,” “face 1-in 2-out holds,” or
“composition of split HOLDs.”

## Primary runner

The paired runner builds Euclidean `B_3(0)`, runs the two-axis opposite
perp-step incoming-lock process, reads each probe's own earliest incoming
set and own outgoing dual from the record prefix at that probe's `t` and
at `t+1`, reports unsigned axis of each, reports cover of the pair, reports
the 1-in 2-out split at both cuts, scores reverse and face from split at
each cut, scores composition as equality of the four split reports, lists
new records in `B_3(0)` between `t` and `t+1` that meet a probe's
six-neighbors, and checks Theorems 1--3. It also checks that split fails at
all four probes at `t`, that empty `O` at `t` fails split, that split HOLDs
at `A`, `B`, and `C` and fails at `D` at `t+1`, that reverse fails at `t`
and HOLDs at `t+1`, that face fails at both cuts, that composition fails,
that frozen-`M` two-tick composition HOLDs as a different leftover, that
2-in 1-out is fail not `UNDEFINED`, that the 1-axis opposite two-site seed
is a different member, that leftover-empty fail is a different reverse and
face, that mixed sets remain sets, that unique-letter split is `UNDEFINED`
at mixed `O`, that the construction does not sum, that a formation member
from already-recorded six-neighbor locks is not attached, that the second
pair is a new seed not a formed child, and that the display is not the
two-tick lock-count clock composition. No runner cache is written.
