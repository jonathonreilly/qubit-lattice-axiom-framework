---
claim_id: two_axis_same_lock_xprobe_one_two_split_tplus1_tplus2_composition_reverse_face_bounded_theorem_note_2026-08-15
claim_type: bounded_theorem
claim_scope: "1-in 2-out split at t+1 versus t+2 on the four x-probes of the two-axis same-lock seed, reverse/face at each cut, and composition, are reported. Displayed, not adopted."
upstream_dependencies:
  - minimal_axioms
runner: scripts/two_axis_same_lock_xprobe_one_two_split_tplus1_tplus2_composition_reverse_face_2026_08_15.py
---

# One-In Two-Out Axis Split At t+1 Versus t+2 Reverse And Face Composition On Four X-Probes Of The Two-Axis Same-Lock Seed

> **Key terms used in this doc** are indexed A-Z at `docs/KEY_TERMINOLOGY.md`;
> each row points to the canonical source-of-truth doc.

**Date:** 2026-08-15
**Type:** bounded_theorem
**Scope:** 1-in 2-out axis split of simultaneous earliest incoming set `M`
and outgoing dual `O` at each probe's formation tick plus one versus plus
two, reverse/face from that split at each cut, and composition HOLD iff
split at `τ1` equals split at `τ2` at `A,B,C,D`, on the four x-probes of
the two-axis same-lock seed in `B_3(0)={n:n·n<=9}`. Same process and
x-probes as nm2slx. `M`, `O`, and split as nm2sl12. Process: two disjoint
same-lock pairs. Seed at tick 0: origin locks `+e_1`, `(0,1,0)` locks
`+e_1`, `(0,0,1)` locks `+e_2`, `(0,1,1)` locks `+e_2`. The second pair is
a new seed, not a formed child. Perp-step, incoming lock. Let `t(q)` be the
formation tick of probe `q`. Let `τ1(q)=t(q)+1` and `τ2(q)=t(q)+2`. There
is no global T. `M(q,τ)` is the set of earliest incoming nearest-neighbor
steps at `q` using only records with tick `<= τ`. Seeds are a singleton
seed letter. `O(q,τ)` is the outgoing dual of `M`: the set of `e` in
`{±e_1,±e_2,±e_3}` such that `q+e` is formed and `e` is in `M(q+e,τ)`.
Unformed at `τ` is `UNDEFINED`. Empty `O` is empty, not `UNDEFINED`. Empty
O at t fails split. Axis of a defined lock set `S` is
`Axis(S)={e_i | some ±e_i in S}`. Cover HOLDs at `q` if and only if
`Axis(M)` intersect `Axis(O)` is empty and `Axis(M)` union `Axis(O)` equals
`{e_1,e_2,e_3}`. Split HOLDs at `q` if and only if cover HOLDs and
`|Axis(M)|=1` (hence `|Axis(O)|=2`). 2-in 1-out is fail of this object, not
UNDEFINED. Reverse HOLDs if and only if split HOLDs at `A` and at `B`. Face
HOLDs if and only if split HOLDs at `C` and at `D`. Composition HOLD if and
only if split at `τ1` equals split at `τ2` at `A`, at `B`, at `C`, and at
`D`. A is not a seed. This is not leftover of nm2slx `t+1`-only axis-cover
reverse fail and face fail. This is not leftover of nm2sl12 reverse hold
face fail. This is not leftover of split composition at `t` versus `t+1`.
This is not leftover of nm2splt2x reverse fail face fail. This is not
leftover of cover reverse. This is not leftover of frozen-`M` two-tick set
equality. This is not leftover of reverse/face-bit composition as a
substitute for equality of the four split reports. This is not leftover of
leftover-of-`M` alone. This is not leftover of leftover-of-`O` alone. This
is not leftover-empty fail. This is not leftover of exist-opposite of signed
locks. This is not leftover of the 1-axis same-lock two-site seed. This is
not leftover of the two-axis opposite seed. This is not leftover of mixed
#7188 fail/fail. This is not leftover of the two-tick lock-count clock
composition. The second pair is a new seed, not a formed child. Uniqueness
is not required. Mixed remains a set. Occupancy of sites is not used.
Displayed, not adopted. Do not write into Admissibility. Do not attach L1.
**Audit-status authority:** independent audit lane only. This note authors no
audit verdict and predicts none.
**Primary runner:**
[`scripts/two_axis_same_lock_xprobe_one_two_split_tplus1_tplus2_composition_reverse_face_2026_08_15.py`](../scripts/two_axis_same_lock_xprobe_one_two_split_tplus1_tplus2_composition_reverse_face_2026_08_15.py)

Framework input:

- [`MINIMAL_AXIOMS_2026-06-29.md`](MINIMAL_AXIOMS_2026-06-29.md) supplies
  cubic-lattice sites `Z^3` with nearest-neighbor adjacency, the one-site
  algebra `M_2(C)`, and the Record sentences that records form and that a
  present record locks exactly one admissible local possibility.

Everything after that quoted input is a finite displayed process on `B_3(0)`
and the four named x-probes. Incoming lock letters are unit nearest-neighbor
steps. `O` is the outgoing dual of those incoming sets at the per-probe cuts
`τ1=t+1` and `τ2=t+2`. Axis is the unsigned lattice direction of a signed
lock. Cover is the complementary occupation of `{e_1,e_2,e_3}` by `Axis(M)`
and `Axis(O)`. Split is cover together with `|Axis(M)|=1`. Reverse and face
are scored on split HOLD at the paired probes at each cut. Composition is
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
claim_type_reason: "Exact report of 1-in 2-out axis split of M and O at t+1 and at t+2 on the four x-probes of the two-axis same-lock seed, reverse fail and face fail at both cuts, and composition HOLD because split at A,B,C,D is unchanged from t+1 to t+2; uniqueness of incoming locks is not claimed and the bits are not adopted."
trace_class: frontier_discovery
target_claim_id: two_axis_same_lock_xprobe_one_two_split_tplus1_tplus2_composition_reverse_face
target_blocker_text: "display 1-in 2-out split at t+1 versus t+2 on the four x-probes of the two-axis same-lock seed, reverse/face at each cut, and composition HOLD iff split at t+1 equals split at t+2"
source_of_blocker_text: handoff
reachability_to_target: advances
artifact_role: theorem
next_trace_action: "Keep 1-in 2-out split t+1 versus t+2 composition displayed; do not write split into Admissibility, do not reduce to cover, do not reduce to frozen-M set equality, do not replace split equality by reverse/face-bit equality, do not replace split by existential opposite of signed locks, do not reprint nm2slx t+1-only axis-cover reverse fail face fail as this two-cut report, do not reprint split composition at t versus t+1, and do not attach L1."
conditional_surface_status: "exact on B_3(0) for 1-in 2-out split at t+1 versus t+2 on the four x-probes of the two-axis same-lock seed, reverse/face at each cut, and composition; displayed, not adopted"
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
nm2slx. `M`, `O`, and split as nm2sl12.

Lock alphabet of the displayed process: `{±e_i}` with `i` in `{1,2,3}`.

Seed: two disjoint same-lock pairs recorded at formation tick 0. Origin
locks `+e_1`. Site `(0,1,0)` locks `+e_1`. Site `(0,0,1)` locks `+e_2`.
Site `(0,1,1)` locks `+e_2`. The second pair is a new seed, not a formed
child of the first pair. This seed is not the two-axis opposite seed
`{0,(0,1,0),(0,0,1),(0,1,1)}` with locks `+e_1/−e_1` and `+e_2/−e_2`. This
seed is not the 1-axis same-lock two-site seed `{0,(0,1,0)}` with only
`+e_1/+e_1`. This seed is not the perp two-site seed `+e_1/+e_2`. This seed
is not the opposite two-site seed `+e_1/−e_1`.

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

## Named 1-in 2-out axis split at `τ1=t+1` versus `τ2=t+2`

Let `t(q)` be the formation tick of x-probe `q` when that tick is defined in
`B_3(0)`. Let `τ1(q)=t(q)+1` and `τ2(q)=t(q)+2`. There is no global T.

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
cover(q) HOLD iff Axis(M(q,τ)) intersect Axis(O(q,τ)) is empty
and Axis(M(q,τ)) union Axis(O(q,τ)) equals {e_1,e_2,e_3}.
```

Split of `M` and `O` at the same cut:

```text
split(q) HOLD iff cover(q) HOLD and |Axis(M(q,τ))|=1.
```

If `q` is unformed at `τ`, then cover and split are `UNDEFINED`. Else fail.
2-in 1-out is fail of this object, not UNDEFINED: cover can HOLD with
`|Axis(M)|=2` and `|Axis(O)|=1`, and that is split fail. Axis is unsigned:
`+e_i` and `−e_i` occupy the same axis. Empty O at t fails split.

Reverse 1-in 2-out holds if and only if split at `A` and split at `B` both
HOLD at that cut. Face 1-in 2-out holds if and only if split at `C` and
split at `D` both HOLD at that cut. Either side `UNDEFINED` is `UNDEFINED`.
Else fail. Composition HOLD if and only if split at `τ1` equals split at
`τ2` at `A`, at `B`, at `C`, and at `D`.

## Theorem 1 — ticks, `M`, `O`, and split at `τ1=t+1` and at `τ2=t+2`

On this process the four x-probes form. Earliest incoming `M` is frozen
from `t` through `t+2`. Outgoing dual `O` is empty at each of the four
x-probes at formation tick. Empty O at t fails split. At `t+1` the
HOLDING outgoing duals appear at `B` and at `C`, while `A` and `D` remain
1-in 1-out with leftover `{e_2}`. At `t+2` those same `M` and `O` reports
repeat: none of the four x-probes has a new six-neighbor at `t(q)+2`.

```text
t(A)=2
t(B)=1
t(C)=3
t(D)=2
M(A, τ1) = {−e_3}
M(B, τ1) = {+e_1}
M(C, τ1) = {+e_1}
M(D, τ1) = {−e_3}
M(A, τ2) = {−e_3}
M(B, τ2) = {+e_1}
M(C, τ2) = {+e_1}
M(D, τ2) = {−e_3}
O(A, τ1) = {+e_1}
O(B, τ1) = {+e_2, +e_3, −e_3}
O(C, τ1) = {−e_2, +e_3, −e_3}
O(D, τ1) = {+e_1}
O(A, τ2) = {+e_1}
O(B, τ2) = {+e_2, +e_3, −e_3}
O(C, τ2) = {−e_2, +e_3, −e_3}
O(D, τ2) = {+e_1}
split(A, τ1) = fail
split(B, τ1) = hold
split(C, τ1) = hold
split(D, τ1) = fail
split(A, τ2) = fail
split(B, τ2) = hold
split(C, τ2) = hold
split(D, τ2) = fail
```

A is not a seed. `A` is the site `(1,0,0)` forming at tick 2 with incoming
`{−e_3}`. Mixed remains a set: `O(B,τ1)` has three outgoing steps and
`O(C,τ1)` has three outgoing steps. Unique letters would assign
`UNDEFINED` at mixed `O`. Here uniqueness is not required. At `τ1` and at
`τ2`, `B` and `C` are 1-in 2-out, so split HOLDs, and `A` and `D` remain
1-in 1-out with leftover `{e_2}`, so split fails. 2-in 1-out is fail of
this object, not UNDEFINED; that identity remains, and it is not the `A`
or `D` report on this seed. Cover matches split on this member at both
cuts by accident of `|Axis(M)|=1` at every scored probe. O is not M.
Frozen `M` is not this composition object. Frozen `O` from `t+1` to `t+2`
is not this composition object.

New records in `B_3(0)` between `t` and `t+1` that meet a probe's
six-neighbors enter `O` and do not enter earliest `M`. None of the four
x-probes has a new 6-NN at `t+2`:

```text
new 6-NN of A at t(A)+1: (2, 0, 0)
new 6-NN of B at t(B)+1: (1, 2, 1), (1, 1, 2), (1, 1, 0)
new 6-NN of C at t(C)+1: (2, -1, 0), (2, 0, 1), (2, 0, -1)
new 6-NN of D at t(D)+1: (2, 1, 0)
new 6-NN of A at t(A)+2: none
new 6-NN of B at t(B)+2: none
new 6-NN of C at t(C)+2: none
new 6-NN of D at t(D)+2: none
```

Compare to nm2slx `t+1` only. Same seed, same x-probes, same `M` and `O`
at `τ1`, same cover fail at `A` and `D` and hold at `B` and `C`, reverse
fail and face fail. That leftover does not score split at `t+2`, does not
score reverse/face at `t+2`, and does not score two-cut split equality.
Compare to split at `t` versus `t+1` on this seed: empty `O` at `t` fails
split at all four probes, so that leftover composition fails. Compare to
1-axis same-lock two-site seed: that member forms `A` at tick 3 and `D` at
tick 3 and has cover HOLD at `A` and at `D` from 2-in 1-out. Here the
second pair is a new seed, not a formed child.

## Theorem 2 — reverse and face at `τ1` and at `τ2`

Reverse 1-in 2-out holds if and only if split HOLDs at `A` and at `B`. At
`τ1` split fails at `A` and HOLDs at `B`. Reverse fails. At `τ2` the same
pair of reports. Reverse fails. This is HOLD iff split, not leftover of
cover reverse, not leftover-empty fail, and not exist-opposite.

Reverse 1-in 2-out at τ1: fail
Reverse 1-in 2-out at τ2: fail

Both sides are defined, so this is not `UNDEFINED`. Reverse fails at `t+1`
and fails at `t+2`. Frozen-`M` exist-opposite reverse fails at both cuts
because `M(A)={−e_3}` and `M(B)={+e_1}` have no pair summing to zero.
Cover reverse fails at both cuts, which agrees on the bits by accident of
cover matching split on this member. Those leftovers are not this
display. nm2sl12 reverse hold face fail is a different frame: y-probes,
not these x-probes.

Reverse fails at τ1.
Reverse fails at τ2.

Face 1-in 2-out holds if and only if split HOLDs at `C` and at `D`. At
`τ1` split HOLDs at `C` and fails at `D`. Face fails. At `τ2` split HOLDs
at `C` and fails at `D`. Face fails. The `D` failure at both cuts is cover
fail from leftover `{e_2}` (1-in 1-out), which is fail of this object, not
UNDEFINED.

Face 1-in 2-out at τ1: fail
Face 1-in 2-out at τ2: fail

Displayed, not adopted. The bits are not written into Admissibility.
Do not write into Admissibility. Do not attach L1.

Face fails at both cuts. Cover face fails at both cuts by the same `D`
cover fail. Split face fails because split fails at `D` at both cuts.
Exist-opposite face of signed `M` fails at both cuts. Exist-opposite face
of signed `O` fails at both cuts. Unique-letter face is `UNDEFINED` from
mixed `O(C)`. Those leftovers are not this split face.

Face fails at τ1.
Face fails at τ2.

## Theorem 3 — composition of split at `t+1` versus `t+2`

Composition HOLD if and only if split at `τ1` equals split at `τ2` at `A`,
at `B`, at `C`, and at `D`. Split at `A` stays fail. Split at `B` and at
`C` stays hold. Split at `D` stays fail. None is `UNDEFINED`.

Composition of split at t+1 versus t+2: HOLD

Displayed, not adopted. The bits are not written into Admissibility.
Do not write into Admissibility. Do not attach L1. Composition HOLD is
equality of the four split reports, not equality of the four `M` sets:
those four `M` sets stay equal (frozen earliest incoming), so frozen-`M`
two-tick composition HOLDs as a different leftover. Outgoing duals also
stay equal from `t+1` to `t+2`, so frozen-`O` composition HOLDs as a
different leftover. Reverse/face-bit composition also HOLDs here because
reverse stays fail and face stays fail; that leftover is still a different
object, because it scores two pair bits rather than the four split reports.
It would still HOLD if `B` changed hold to fail while `A` stayed fail and
face stayed fail, and split composition would fail.

This is not leftover of nm2slx `t+1`-only axis-cover reverse fail and face
fail: that display does not score split at `t+2`. This is not leftover of
split composition at `t` versus `t+1`: empty `O` at `t` fails split at
`B` and at `C`, so that leftover composition fails while this letter HOLDs.
This is not leftover of nm2splt2x reverse fail face fail: that leftover is
two-axis opposite at `t` versus `t+1`. This is not leftover of nm2sl12
reverse hold face fail. This is not leftover of mixed #7188 fail/fail.
This is not leftover of the two-tick lock-count clock composition.

Composition holds.

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
- It does not reprint nm2slx `t+1`-only axis-cover reverse fail and face
  fail as this two-cut report.
- It does not reprint split composition at `t` versus `t+1` as this letter.
- It does not reprint nm2splt2x reverse fail face fail as this member.
- It does not reprint nm2sl12 reverse hold face fail as this member.
- It does not reprint cover reverse as this split reverse.
- It does not reprint the 1-axis same-lock two-site seed as this member.
- It does not reprint the two-axis opposite seed as this member.
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

This display uses Lattice to name `B_3(0)` and the four x-probes. It uses Qubit
only as the algebra of the local possibility domain. It uses Record only as a
boundary: a present lock is content. It does not rewrite Admissibility. The
two-axis same-lock seed process, 1-in 2-out axis split of `M` and `O` at
`t+1` and at `t+2`, reverse/face from that split at each cut, and
composition of those four split reports are displayed theorem-domain data.

## Exact target and obligation graph

| Obligation | Status |
|---|---|
| current Lattice / Admissibility / Record premises | quoted; no edit |
| perp-step incoming-lock process on `B_3(0)` | displayed; two-axis same-lock seed `+e_1/+e_1` and `+e_2/+e_2` |
| ticks `t(A)`, `t(B)`, `t(C)`, `t(D)` | Theorem 1; `2`, `1`, `3`, `2` |
| `M` at `τ1=t+1` and at `τ2=t+2` | Theorem 1; frozen equal |
| `O` at `τ1=t+1` and at `τ2=t+2` | Theorem 1; HOLDING at `B,C`; singleton at `A,D`; equal across cuts |
| split at `τ1` | Theorem 1; fail at `A,D`; HOLD at `B,C` |
| split at `τ2` | Theorem 1; fail at `A,D`; HOLD at `B,C` |
| reverse from 1-in 2-out at `τ1` and `τ2` | Theorem 2; `fail`, `fail` |
| face from 1-in 2-out at `τ1` and `τ2` | Theorem 2; `fail`, `fail` |
| composition of split at `t+1` versus `t+2` | Theorem 3; `HOLD` |
| unique incoming lock | not required |
| occupancy of sites as the letter | not used |
| named-sign `{+,−}` letter | not used; lost the axis |
| singleton unique lock-vector letter | not used as the object; mixed remains a set |
| `Z^3` sum of the lock set | not used; no aggregation |
| six-neighbor star as the letter | not used |
| leftover-empty fail of leftover axis | not this split display |
| leftover of exist-opposite HOLD | not this split display |
| leftover of cover reverse | not this split display |
| leftover of leftover-of-`M` alone | not this display |
| leftover of leftover-of-`O` alone | not this display |
| leftover of frozen-`M` two-tick set equality | not this composition |
| leftover of reverse/face-bit composition | not this composition |
| leftover of nm2slx `t+1`-only axis-cover | not this two-cut report |
| leftover of split composition at `t` versus `t+1` | not this letter |
| leftover of nm2splt2x reverse fail face fail | not this display |
| leftover of nm2sl12 reverse hold face fail | not this display |
| leftover of the two-axis opposite seed | not this display |
| leftover of mixed #7188 fail/fail | not this display |
| leftover of the 1-axis same-lock two-site seed | not this display |
| leftover of the two-tick lock-count clock | not this display |
| 2-in 1-out scored as `UNDEFINED` | refused; fail of this object |
| global later T | not used |
| 1-in 2-out split as Admissibility content | not adopted |
| formation site / probability / rate | open |
| physical Record readout of the bits | open |

## Value gate (V1–V5)

| # | Answer |
|---|---|
| V1 | It answers the first-display question: 1-in 2-out split at `t+1` versus `t+2` on the four x-probes of the two-axis same-lock seed, reverse/face at each cut, and composition. |
| V2 | Current main has no landed 1-in 2-out split t+1 versus t+2 composition reverse/face report on these four x-probes of the two-axis same-lock seed. |
| V3 | Split reports at two cuts, the four reverse/face bits, and composition as split equality are independently finite and exact. |
| V4 | The theorem is more than a restatement of Record because it reads unsigned 1-in 2-out split of own incoming and own outgoing at `t+1` and at `t+2` and scores equality of those four reports. |
| V5 | It is not an adopted content rule: the bits remain displayed. |

## No-go discipline gate

The negative content is narrow: the display does not write those bits into
Admissibility, does not reduce them to named signs, does not require a
unique lock, does not replace split by leftover-empty fail, does not
replace split by leftover of `M` alone or leftover of `O` alone, does not
replace split by existential opposite of signed locks, does not replace
split by cover reverse, does not replace split equality by frozen-`M` set
equality, does not replace split equality by reverse/face-bit equality,
does not identify this display with nm2slx `t+1` only, does not identify
this display with split composition at `t` versus `t+1`, does not identify
this display with the two-axis opposite seed, and does not identify it with
nm2sl12 reverse hold face fail. No global impossibility is claimed.

### N1 — materially distinct routes

| Route | Attempt | Why it fails here | Marker |
|---|---|---|---|
| nm2slx `t+1` only | reuse cover reverse fail and face fail at `t+1` | that leftover does not score split at `t+2`; this letter scores both cuts and composition | ATTEMPTED |
| split at `t` versus `t+1` | HOLD iff split at `t` equals split at `t+1` | empty `O` at `t` fails split at `B,C`; that leftover composition fails while this letter HOLDs | ATTEMPTED |
| frozen-`M` two-tick set equality | HOLD iff `M(t+1)=M(t+2)` at `A,B,C,D` | the four `M` sets stay equal, so that leftover HOLDs; the scored object is still the four split reports | ATTEMPTED |
| reverse/face-bit composition | HOLD iff reverse/face bits match | those two pair bits HOLD here because reverse stays fail and face stays fail; the scored object is still the four split reports | ATTEMPTED |
| cover reverse | score reverse/face as cover HOLD | cover reverse fails at both cuts with split; 2-in 1-out is still cover HOLD and split fail on the 1-axis seed | ATTEMPTED |
| leftover-empty fail | score reverse/face as leftover nonempty-equal | leftover of the union is `{e_2}` at `A` and empty at `B`; leftover reverse fails, and leftover-empty would HOLD if both leftovers were `{e_2}` while split reverse still fails | ATTEMPTED |
| leftover of `M` alone | score `{e_1,e_2,e_3}` minus `Axis(M)` | leftover of `M` at `A` is `{e_1,e_2}` and does not see outgoing duals | ATTEMPTED |
| leftover of `O` alone | score `{e_1,e_2,e_3}` minus `Axis(O)` | leftover of `O` at `A` is `{e_2,e_3}`; that is not this split | ATTEMPTED |
| exist-opposite of signed `M` | reuse signed reverse of frozen `M` | exist-opposite reverse fails at both cuts by a signed pairwise test, not `|Axis(M)|=1` cover | ATTEMPTED |
| exist-opposite of signed `O` | score reverse/face inside `O` | exist-opposite of `O` never reads `M`; unique-letter reverse is `UNDEFINED` at mixed `O(B)` while split reverse fails | ATTEMPTED |
| unique letter | replace mixed sets by a singleton or `UNDEFINED` | mixed `O(B,τ1)` remains a set; unique-letter split at `B` is `UNDEFINED`; this split is hold | ATTEMPTED |
| 2-in 1-out as `UNDEFINED` | treat `|Axis(M)|=2` cover as unformed | 2-in 1-out is fail of this object, not UNDEFINED; `A` here is 1-in 1-out cover fail, also not UNDEFINED | ATTEMPTED |
| 1-axis same-lock two-site seed | reuse `t(A)=3`, `t(D)=3`, cover HOLD at `A` and `D` | different seed; second pair is a new seed, not a formed child | ATTEMPTED |
| two-axis opposite seed | reuse `O(D)={+e_1,−e_1}` | this seed has `O(D)={+e_1}`; unique letter at opposite `O(D)` is `UNDEFINED` | ATTEMPTED |
| nm2splt2x reverse fail face fail | reuse opposite x-probe split at `t` versus `t+1` | different seed and different cuts; that leftover composition fails from empty `O` at `t` | ATTEMPTED |
| nm2sl12 reverse hold face fail | reuse same-lock y-probes | different probes; reverse HOLDs and face fails there, reverse fails and face fails here | ATTEMPTED |
| two-tick lock-count clock | score a lock-count clock across two ticks | different member; this display scores 1-in 2-out of own incoming and outgoing at two cuts | ATTEMPTED |
| mixed #7188 fail/fail | reuse z-symmetric mixed `M` reverse-fail face-fail | different process; this member reports split hold at `B` and at `C` | ATTEMPTED |
| sum of a set | replace split by a `Z^3` sum | the construction does not sum; split is cover plus `|Axis(M)|=1` | ATTEMPTED |
| named-sign lettering | collapse `{±e_i}` to `{+,−}` | named-sign lettering lost the axis | ATTEMPTED |
| global later T | wait until `max t(A,B,C,D)` before reading | `τ1(q)=t(q)+1` and `τ2(q)=t(q)+2` are per-probe; no global T | ATTEMPTED |
| attach a formation member from already-recorded six-neighbor locks | form the probes by a neighbor-lock letter instead of perp-step | refused; not attached | ATTEMPTED |
| adopt bits into Admissibility | rewrite the local rule by 1-in 2-out split | refused; displayed, not adopted | ATTEMPTED |

### N2 — wall independence

Missing physical adoption, missing identification of split with leftover of
`M` alone, missing identification of split composition with frozen-`M` set
equality, missing identification of split with leftover-empty fail, missing
identification of split with existential opposite of signed locks, missing
identification of split with cover reverse, missing identification of this
seed with the 1-axis same-lock two-site seed, missing identification of
this two-cut report with nm2slx `t+1` only, missing identification with
split composition at `t` versus `t+1`, and missing Record identification of
split reverse are distinct open premises. This note claims no complete wall
collection.

### N3 — hidden-condition scan

The host `B_3(0)`, two disjoint same-lock seed pairs `+e_1/+e_1` and
`+e_2/+e_2`, perpendicular step rule, incoming-step lock, own incoming set
and own outgoing dual from records with tick `<= τ`, per-probe `τ1=t+1` and
`τ2=t+2`, unsigned axis, cover as complementary occupation of
`{e_1,e_2,e_3}`, split as cover and `|Axis(M)|=1`, empty `O` at `t` fails
split, 2-in 1-out as fail not `UNDEFINED`, composition as equality of the
four split reports, four x-probes with A not a seed, second pair as a new
seed not a formed child, and mixed remains a set are declared. No uniqueness
of incoming locks, no six-neighbor lock union as the scored object, no
lock-count clock, no frozen-`M` leftover as the composition object, no
reverse/face-bit leftover as the composition object, no global later T, no
formation attachment from already-recorded six-neighbor locks, and no
Admissibility rewrite are silently assumed.

### N4 — source residual matching

The current axiom memo supplies cubic sites, `M_2(C)`,
content-conditional-on-formation, and unreadable absence. The residual that
formation site, probability, and rate remain unsupplied is unchanged. The
split `hold`/`fail` reports at two cuts, and composition HOLD, do not close
that residual.

### N5 — resolution and rhetoric audit

| Resolution | Executed | Not claimed |
|---|---|---|
| per element | each unsigned lattice axis among `{e_1,e_2,e_3}` | no continuum alphabet |
| per site | `A,B,C,D` x-probes on `B_3(0)` only | no other cubic sites |
| per mode | no mode calculation | no spectral exhaustion |
| per block | four split reports at two cuts, reverse/face at each cut, and composition | no adopted content law |
| lattice wide | checked and not executed | no lattice-wide lettering rule |

### N6 — live partial-closure paths

Live routes include a later Record content map for split reverse/face, a
formation-rate rule, and a physical selector among 1-in 2-out axes. None
is taken here.

### N7 — hostile steelman

**Steelman:** Split two-cut composition should be refused as leftover
because nm2slx already reported reverse fail and face fail at `t+1`; `M`
and `O` are frozen from `t+1` to `t+2` so composition of those sets already
answers two ticks; reverse/face-bit composition already HOLDs; two-axis
opposite has the same split bits at these cuts; y-probes already give a
same-lock reverse/face report; and 1-in 1-out at `A` and at `D` should be
`UNDEFINED`.

**Answer:** nm2slx scores axis-cover at `t+1` only. This letter scores split
at `t+1` and at `t+2`, reverse/face at each cut, and composition as equality
of the four split reports. Those are extra reports, not a reprint.
Frozen-`M` two-tick composition HOLDs because earliest incoming does not
change; frozen-`O` composition HOLDs because none of the four x-probes has
a new 6-NN at `t+2`. The scored object is still the four split reports.
Split composition at `t` versus `t+1` fails from empty `O` at `t`, so freeze
is not automatic from the first tick. Reverse/face-bit composition scores
two pair bits; this letter scores four split reports. Two-axis opposite has
`O(D)={+e_1,−e_1}`; this seed has `O(D)={+e_1}`. nm2sl12 reverse hold face
fail is y-probes, not these x-probes. `A` and `D` are formed; 1-in 1-out is
cover fail and split fail, not UNDEFINED. Reverse 1-in 2-out fails at both
cuts. Face fails at both cuts. Composition of split HOLDs.

### N8 — cross-cycle echo

nm2slx reported axis-cover reverse fail and face fail at `t+1` on these
x-probes, with cover fail at `A` and `D` and hold at `B` and `C`. nm2splt2x
reported reverse fail face fail with composition fail at `t` versus `t+1`
on two-axis opposite x-probes. nm2sl12 reported reverse hold and face fail
on same-lock y-probes. Frozen-`M` two-tick composition on this two-axis
same-lock seed HOLDs. This note is not those displays: it reports 1-in
2-out axis split of `M` and `O` at `τ1=t+1` and at `τ2=t+2` on the
two-axis same-lock seed, with `t(A)=2`, `t(B)=1`, `t(C)=3`, and `t(D)=2`,
split fail at `A` and `D` and HOLD at `B` and `C` at both cuts, reverse
fail at both cuts, face fail at both cuts, and composition HOLD.

**Gate disposition:** PASS for the 1-in 2-out t+1 versus t+2 reverse/face and
composition reports above. FAIL / DO NOT SHIP for “the predicate equals
the named sign,” “the predicate equals the unique singleton lock vector,”
“the predicate equals six-neighbor lock union,” “the predicate equals
leftover-empty fail,” “the predicate equals leftover of `M` alone,” “the
predicate equals leftover of `O` alone,” “the predicate equals
exist-opposite HOLD,” “the predicate equals cover reverse HOLD,”
“the predicate equals nm2slx `t+1` only,” “the predicate equals frozen-`M`
set equality,” “composition equals reverse/face-bit equality,” “the
predicate equals split composition at `t` versus `t+1`,” “the predicate
equals the two-axis opposite seed,” “the predicate equals nm2splt2x reverse
fail face fail,” “the predicate equals nm2sl12 reverse hold face fail,”
“bits are Admissibility,” “2-in 1-out is UNDEFINED,” “reverse 1-in 2-out
holds at `t+1`,” “reverse 1-in 2-out holds at `t+2`,” “face 1-in 2-out
holds,” or “composition of split fails.”

## Primary runner

The paired runner builds Euclidean `B_3(0)`, runs the two-axis same-lock
perp-step incoming-lock process, reads each probe's own earliest incoming
set and own outgoing dual from the record prefix at that probe's `t+1` and
at `t+2`, reports unsigned axis of each, reports cover of the pair, reports
the 1-in 2-out split at both cuts, scores reverse and face from split at
each cut, scores composition as equality of the four split reports, lists
new records in `B_3(0)` between `t` and `t+1` that meet a probe's
six-neighbors and the empty new 6-NN at `t+2`, and checks Theorems 1--3.
It also checks that split fails at `A` and at `D` and HOLDs at `B` and at
`C` at both cuts, that empty `O` at `t` fails split, that reverse fails at
both cuts, that face fails at both cuts, that composition HOLDs, that split
composition at `t` versus `t+1` fails as a different leftover, that
frozen-`M` two-tick composition HOLDs as a different leftover, that 2-in
1-out is fail not `UNDEFINED`, that the 1-axis same-lock two-site seed is a
different member, that leftover-empty fail is a different reverse and face,
that mixed sets remain sets, that unique-letter split is `UNDEFINED` at
mixed `O`, that the construction does not sum, that a formation member from
already-recorded six-neighbor locks is not attached, that the second pair
is a new seed not a formed child, that the display is not the two-axis
opposite leftover process, that the display is not nm2splt2x reverse fail
face fail, and that the display is not the two-tick lock-count clock
composition. No runner cache is written.
