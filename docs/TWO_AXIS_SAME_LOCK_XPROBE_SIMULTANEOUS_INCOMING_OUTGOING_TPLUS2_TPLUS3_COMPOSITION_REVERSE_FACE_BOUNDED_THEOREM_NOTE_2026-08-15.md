---
claim_id: two_axis_same_lock_xprobe_simultaneous_incoming_outgoing_tplus2_tplus3_composition_reverse_face_bounded_theorem_note_2026-08-15
claim_type: bounded_theorem
claim_scope: "Simultaneous M and O at t+2 versus t+3 on the four x-probes of the two-axis same-lock seed, reverse/face at each cut, and composition, are reported. Displayed, not adopted."
upstream_dependencies:
  - minimal_axioms
runner: scripts/two_axis_same_lock_xprobe_simultaneous_incoming_outgoing_tplus2_tplus3_composition_reverse_face_2026_08_15.py
---

# Simultaneous Own-Incoming And Own-Outgoing Freeze At t+2 Versus t+3 Reverse And Face On Four Two-Axis Same-Lock X-Probes

> **Key terms used in this doc** are indexed A-Z at `docs/KEY_TERMINOLOGY.md`;
> each row points to the canonical source-of-truth doc.

**Date:** 2026-08-15
**Type:** bounded_theorem
**Scope:** simultaneous earliest incoming set `M` and outgoing dual `O` at
each probe's `τ1=t+2` versus `τ2=t+3`, reverse/face from simultaneous HOLD
at each cut, and composition of those four `M` sets and four `O` sets, on
the four x-probes of the two-axis same-lock seed in
`B_3(0)={n:n·n<=9}`. Same process and x-probes as nm2slpx. Process: two
disjoint same-lock pairs. Seed at tick 0: origin locks `+e_1`, `(0,1,0)`
locks `+e_1`, `(0,0,1)` locks `+e_2`, `(0,1,1)` locks `+e_2`. Neither pair
is opposite. The second pair is a new seed, not a formed child. Perp-step,
incoming lock. Let `t(q)` be the formation tick of probe `q`. Let
`τ1(q)=t(q)+2` and `τ2(q)=t(q)+3`. There is no global T. Do not score
`τ=t`. `M(q,τ)` is the set of earliest incoming nearest-neighbor steps at
`q` using only records with tick `<= τ`. Seeds are a singleton seed letter.
`O(q,τ)` is the outgoing dual of `M`: the set of `e` in
`{±e_1,±e_2,±e_3}` such that `q+e` is formed and `e` is in `M(q+e,τ)`.
Unformed at `τ` is `UNDEFINED`. Empty `O` is empty, not `UNDEFINED`.
Intersection is `M(q,τ) ∩ O(q,τ)`; unformed is `UNDEFINED`. Empty
intersection is empty, not `UNDEFINED`. Simultaneous HOLDs at `q,τ` if and
only if both `M` and `O` are defined nonempty and `M ∩ O` is empty.
`UNDEFINED` if `M` or `O` is `UNDEFINED`. Else fail. Reverse HOLDs at a
cut if and only if simultaneous HOLDs at `A` and at `B` at that cut. Face
HOLDs if and only if simultaneous HOLDs at `C` and at `D` at that cut.
Composition HOLDs if and only if `M(τ1)=M(τ2)` and `O(τ1)=O(τ2)` at `A`,
`B`, `C`, and `D`. This is HOLD iff simultaneous, not leftover-empty fail
of leftover axis. This is the transfer of simultaneous freeze from `t+2`
to `t+3` on the nm2simt2slx HOLDING freeze x-probe member. This is not
leftover of nm2simt2slx simultaneous freeze t+1 versus t+2. This is not
leftover of nm2simslx simultaneous at `t+1` only. This is not leftover of
two-axis opposite simultaneous freeze.
This is not leftover of nm2ot3slx O freeze exist-opposite reverse fail.
This is not leftover of nmot2 `O` at `t` versus `t+1`. This is not leftover
of nmt2 `M` two-tick. This is not leftover of nmout eventual-`O`. This is
not leftover of nm2simz HOLDING. This is not leftover of nm2slpx
forall-perp. This is not leftover of nm2slx axis-cover. This is not leftover
of nm2simslz same-lock z-probe reverse fail. This is not leftover of 1-in
2-out split. This is not leftover of nmsimopp exist-opposite of `M` and of
`O` at `t+1`. This is not leftover of leftover-of-`M` alone. This is not
leftover of leftover-of-`O` alone. This is not leftover of nmunopp union.
This is not leftover of mixed #7188 fail/fail. Neither pair is opposite.
Uniqueness is not required. Mixed remains a set. Occupancy of sites is not
used. Occupancy `n` is not used. Displayed, not adopted. Do not write into
Admissibility. Do not attach L1. This note does not write simultaneous into
Admissibility and does not attach a formation member from already-recorded
six-neighbor locks. This display does not use occupancy. Mixed remains a
set. Unique `L` is not the object. The six-neighbor star is not the letter.
This is not named-sign lettering. This is not a unique lock-vector leftover
and not a sum leftover. O is not M. The construction does not sum. It does
not use a six-neighbor star. It is not leftover of unique-L. It is not the
two-tick lock-count clock composition.
**Audit-status authority:** independent audit lane only. This note authors no
audit verdict and predicts none.
**Primary runner:**
[`scripts/two_axis_same_lock_xprobe_simultaneous_incoming_outgoing_tplus2_tplus3_composition_reverse_face_2026_08_15.py`](../scripts/two_axis_same_lock_xprobe_simultaneous_incoming_outgoing_tplus2_tplus3_composition_reverse_face_2026_08_15.py)

Framework input:

- [`MINIMAL_AXIOMS_2026-06-29.md`](MINIMAL_AXIOMS_2026-06-29.md) supplies
  cubic-lattice sites `Z^3` with nearest-neighbor adjacency, the one-site
  algebra `M_2(C)`, and the Record sentences that records form and that a
  present record locks exactly one admissible local possibility.

Everything after that quoted input is a finite displayed process on `B_3(0)`
and the four named x-probes. Incoming lock letters are unit nearest-neighbor
steps. `O` is the outgoing dual of those incoming sets at the per-probe cuts
`τ1=t+2` and `τ2=t+3`. Simultaneous is signed-letter disjointness of nonempty
`M` and nonempty `O` at the same cut. Reverse and face are scored on
simultaneous HOLD at the paired probes at each cut. Composition is equality
of those four own incoming sets and four own outgoing sets. Named signs
`{+,−}` are a coarser readout and are not used. A singleton unique lock
letter is a different readout and is not used as the object. Existential
opposite of signed locks is a different readout and is not used as the
simultaneous reverse. Unsigned axis-cover of `M` and `O` is a different
readout and is not used. Forall-perp of integer dots `m·o` is a different
readout and is not used. 1-in 2-out axis split is a different readout and
is not used. Leftover-empty fail of unsigned leftover axis sets is a
different readout and is not used. A `Z^3` sum of those locks is a
different readout and is not used. Occupancy of sites is not used. The
construction does not use occupancy. A six-neighbor star is not the letter.

## Machine status and trace

```yaml
actual_current_surface_status: bounded-support
target_claim_type: bounded_theorem
claim_type_reason: "Exact report of simultaneous M and O at t+2 versus t+3 on the four x-probes of the two-axis same-lock seed, reverse hold and face hold from simultaneous HOLD at each cut, and composition HOLD; uniqueness of incoming locks is not claimed and the bits are not adopted."
trace_class: frontier_discovery
target_claim_id: two_axis_same_lock_xprobe_simultaneous_incoming_outgoing_tplus2_tplus3_composition_reverse_face
target_blocker_text: "display simultaneous M and O at t+2 versus t+3 on the four x-probes of the two-axis same-lock seed, reverse/face at each cut, and composition"
source_of_blocker_text: handoff
reachability_to_target: advances
artifact_role: theorem
next_trace_action: "Keep simultaneous M and O freeze displayed; do not write simultaneous into Admissibility, do not reduce to leftover of nm2simt2slx simultaneous freeze t+1 versus t+2, do not reduce to leftover-empty fail, do not reduce to leftover of M alone or leftover of O alone, do not replace simultaneous by existential opposite of signed locks, do not replace simultaneous by unsigned axis-cover, do not replace simultaneous by forall-perp, do not replace simultaneous by 1-in 2-out split, do not replace either set by six-neighbor lock union, do not identify the freeze with O-only composition or M-only composition, and do not attach L1."
conditional_surface_status: "exact on B_3(0) for simultaneous M and O at t+2 versus t+3 on the four x-probes of the two-axis same-lock seed, reverse/face at each cut, and composition; displayed, not adopted"
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

No larger host is used. The four x-probes are the only sites whose
simultaneous `M` and `O` at `τ1=t+2` and `τ2=t+3` is scored:

```text
A = (1,0,0),  B = (1,1,1),  C = (2,0,0),  D = (1,1,0).
```

These are not the y-probes `A=(0,1,0)`, `B=(1,1,1)`, `C=(0,2,0)`,
`D=(1,1,0)`. These are not the z-probes `A=(0,0,1)`, `B=(1,1,1)`, `C=(0,0,2)`,
`D=(1,0,1)`. `A` is not a seed. `A` is the site `(1,0,0)` forming at tick 2.

Lock alphabet of the displayed process: `{±e_i}` with `i` in `{1,2,3}`.

Seed: two disjoint same-lock pairs recorded at formation tick 0. Origin
locks `+e_1` and `(0,1,0)` locks `+e_1`. `(0,0,1)` locks `+e_2` and
`(0,1,1)` locks `+e_2`. The second pair is a new seed, not a formed child
of the first pair, and neither pair is opposite. This seed is not the 1-axis
same-lock two-site seed `{0,(0,1,0)}` with `+e_1/+e_1` alone. This seed is
not the two-axis opposite seed `+e_1/−e_1` and `+e_2/−e_2`. This seed is
not the y-symmetric three-site seed that also records `(0,-1,0)` at tick 0.
This seed is not the z-symmetric three-site seed `{0,(0,0,1),(0,0,-1)}`.

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

## Named simultaneous freeze at `τ1=t+2` versus `τ2=t+3`

Let `t(q)` be the formation tick of x-probe `q` when that tick is defined in
`B_3(0)`. Let `τ1(q)=t(q)+2` and `τ2(q)=t(q)+3`. There is no global T.
Do not score τ=t.

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
Occupancy of sites is not used. Occupancy `n` is not used. O is not M.

Intersection at the same cut:

```text
(M ∩ O)(q,τ) = M(q,τ) ∩ O(q,τ).
```

If `q` is unformed at `τ`, then the intersection is `UNDEFINED`. Empty
intersection is empty, not `UNDEFINED`.

Simultaneous at a probe at the same cut:

```text
sim(q,τ) HOLDs iff M and O are defined nonempty and M ∩ O is empty.
```

If `q` is unformed at `τ`, then simultaneous is `UNDEFINED`. Empty `M` or
empty `O` fails. Nonempty overlapping letters fail. Simultaneous is signed
letter disjointness: `+e_i` and `−e_i` are distinct letters.

Reverse simultaneous holds at a cut if and only if simultaneous HOLDs at
`A` and at `B` at that cut. Face simultaneous holds if and only if
simultaneous HOLDs at `C` and at `D` at that cut. Either side `UNDEFINED`
is `UNDEFINED`. Else if both sides HOLD, reverse or face HOLDs. Else fail.

Composition of simultaneous freeze (displayed):

```text
composition HOLDs iff M(A,τ1)=M(A,τ2) and O(A,τ1)=O(A,τ2)
and M(B,τ1)=M(B,τ2) and O(B,τ1)=O(B,τ2)
and M(C,τ1)=M(C,τ2) and O(C,τ1)=O(C,τ2)
and M(D,τ1)=M(D,τ2) and O(D,τ1)=O(D,τ2).
```

Any side `UNDEFINED` makes composition `UNDEFINED`. Else if some probe's
own incoming set or own outgoing set changes from `t+2` to `t+3`,
composition fails. Equality of reverse/face bits is a different object.
O-only composition is a different object. M-only composition is a different
object. This letter is equality of the four `M` sets and the four `O` sets.

Identifying a named sign of those locks with reverse or face is refused:
named-sign lettering lost the axis. Identifying leftover-empty fail with
simultaneous reverse is refused: leftover-empty fail scores empty leftover
axis as fail. Identifying unsigned axis-cover with simultaneous is refused:
on these x-probes cover fails at `A` and at `D` because the union misses
e_2, while simultaneous HOLDs. Identifying forall-perp with simultaneous
is refused: `{+e_1}` and `{−e_1}` HOLD simultaneous and fail forall-perp.
Identifying 1-in 2-out with simultaneous is refused: 1-in 2-out fails at
`A` and at `D` on these x-probes. Identifying nm2simz HOLDING with this
letter is refused: nm2simz scores the four z-probes of the two-axis
opposite seed. Identifying nm2simslx `t+1` only with this freeze is
refused: that leftover has no `t+2` cut. Identifying nm2simt2slx freeze
from `t+1` to `t+2` with this freeze is refused: that leftover scores
`τ1=t+1` versus `τ2=t+2` and reports no new six-neighbor at `t+2`.
Identifying nm2ot3slx O freeze
exist-opposite reverse fail with this reverse is refused: exist-opposite
of signed `O` reverse fails while simultaneous reverse HOLDs. Identifying
nmot2 `O` at `t` versus `t+1` is refused: at `t`, `O` is empty at all four
x-probes, so simultaneous fails and reverse/face fail. Identifying nmt2
`M` two-tick is refused: that leftover ignores `O`. Identifying nmout
eventual-`O` is refused: eventual `O` has no `t+2` versus `t+3` cut.

Admissibility is not edited. Simultaneous is not written into
Admissibility. Do not write into Admissibility. Do not attach L1.

## Theorem 1 — ticks, `M`, `O`, and sim at `τ1=t+2` and at `τ2=t+3`

On this process the four x-probes form. Incoming is frozen at formation:
`M(q,t+1)=M(q,t)` at every scored probe, and `M(q,t+2)=M(q,t+1)`, and
`M(q,t+3)=M(q,t+2)`. Outgoing is empty at `t` at each of the four probes,
then filled at `t+1`, frozen from `t+1` to `t+2` on the nm2simt2slx leftover,
and frozen from `t+2` to `t+3` here. Simultaneous HOLDs at each probe at
both cuts.

```text
t(A)=2
t(B)=1
t(C)=3
t(D)=2
M(A, τ1) = {−e_3}
M(B, τ1) = {+e_1}
M(C, τ1) = {+e_1}
M(D, τ1) = {−e_3}
O(A, τ1) = {+e_1}
O(B, τ1) = {+e_2, +e_3, −e_3}
O(C, τ1) = {−e_2, +e_3, −e_3}
O(D, τ1) = {+e_1}
M(A, τ1) ∩ O(A, τ1) = {}
M(B, τ1) ∩ O(B, τ1) = {}
M(C, τ1) ∩ O(C, τ1) = {}
M(D, τ1) ∩ O(D, τ1) = {}
sim(A, τ1) = hold
sim(B, τ1) = hold
sim(C, τ1) = hold
sim(D, τ1) = hold
M(A, τ2) = {−e_3}
M(B, τ2) = {+e_1}
M(C, τ2) = {+e_1}
M(D, τ2) = {−e_3}
O(A, τ2) = {+e_1}
O(B, τ2) = {+e_2, +e_3, −e_3}
O(C, τ2) = {−e_2, +e_3, −e_3}
O(D, τ2) = {+e_1}
M(A, τ2) ∩ O(A, τ2) = {}
M(B, τ2) ∩ O(B, τ2) = {}
M(C, τ2) ∩ O(C, τ2) = {}
M(D, τ2) ∩ O(D, τ2) = {}
sim(A, τ2) = hold
sim(B, τ2) = hold
sim(C, τ2) = hold
sim(D, τ2) = hold
```

`A` is not a seed. `A` is the site `(1,0,0)` forming at tick 2 with
incoming `{−e_3}`. Mixed remains a set: `O(B,τ1)` has three outgoing
steps and `O(C,τ1)` has three outgoing steps. Unique letters would assign
`UNDEFINED` at those mixed outgoing sets and would leave reverse and face
`UNDEFINED`. Here uniqueness is not required. `M` and `O` are disjoint at
each of the four probes at both cuts. O is not M.

New records in `B_3(0)` that meet a probe's six-neighbors:

```text
new 6-NN of A at t(A)+2: none
new 6-NN of B at t(B)+2: none
new 6-NN of C at t(C)+2: none
new 6-NN of D at t(D)+2: none
new 6-NN of A at t(A)+3: none
new 6-NN of B at t(B)+3: (2, 1, 1)
new 6-NN of C at t(C)+3: none
new 6-NN of D at t(D)+3: none
```

No new six-neighbor of any scored x-probe forms at `t+2`. At `t+3` a new
six-neighbor of `B` forms, namely `(2,1,1)`. That neighbor's earliest
incoming is `{−e_2, +e_3, −e_3}`, so `+e_1` is not in `M((2,1,1),τ)`. The
connecting step from `B` is parallel to `B`'s lock `+e_1` and is not an
allowed perp-step parent. Therefore that new six-neighbor does not grow
`O(B)`. Frozen `M` and frozen `O` from `t+2` to `t+3` is the first display
of that simultaneous freeze on this same-lock x-probe member. At `t`, `O`
is empty at all four x-probes, so simultaneous fails. Do not score `τ=t`.
This is not leftover of nm2simt2slx simultaneous freeze t+1 versus t+2:
that leftover reports reverse hold, face hold, and composition HOLD with
no new six-neighbor at `t+2` and no `t+3` cut.

Compare to two-axis opposite leftover: same x-probes, same perp-step, but
opposite partner letters. Opposite `O(D,τ1)={+e_1, −e_1}` includes `−e_1`.
This member has `O(D)={+e_1}`. Compare to 1-axis same-lock: ticks become
`3,2,4,3` and cover HOLDs at each x-probe. Here `t(A)=2` and
`M(A)={−e_3}`. Compare to nm2ot3slx O freeze: that leftover scores
exist-opposite of `O` and reports reverse fail and face fail with
composition HOLD of `O` alone. This letter scores simultaneous reverse
hold and face hold, and composition of both `M` and `O`.

On the same two-axis same-lock seed, nm2slpx forall-perp of `M` versus `O`
HOLDs at `A`,`B`,`C`,`D` at `t+1`. `{+e_1}` versus `{−e_1}` splits
forall-perp from simultaneous. Axis-cover fails at `A` and at `D`.

## Theorem 2 — reverse and face at `τ1` and at `τ2`

Reverse simultaneous holds at a cut if and only if simultaneous HOLDs at
`A` and at `B` at that cut. At `τ1` both simultaneous reports HOLD.
Reverse HOLDs. At `τ2` the same simultaneous reports remain, so reverse
HOLDs again. Reverse holds at τ1 and at τ2.

Reverse at τ1: hold
Reverse at τ2: hold

Both sides are defined, so this is not `UNDEFINED`. Leftover-empty reverse
fails because leftover of the unsigned-axis union is `{e_2}` at `A` and
empty at `B`. Exist-opposite reverse of signed `O` fails:
`O(A)={+e_1}` and `O(B)={+e_2, +e_3, −e_3}` include no opposite pair.
Exist-opposite reverse of signed `M` fails. nm2slx cover reverse fails
because cover fails at `A`. Unique-L leftover reports reverse `UNDEFINED`
from mixed `O(B)`. Those leftovers are not this display.

Reverse holds at τ1 and at τ2.

Face simultaneous holds at a cut if and only if simultaneous HOLDs at `C`
and at `D` at that cut. At `τ1` both simultaneous reports HOLD. Face
HOLDs. At `τ2` the same simultaneous reports remain, so face HOLDs again.
Face holds at τ1 and at τ2.

Face at τ1: hold
Face at τ2: hold

This is not `fail` and not `UNDEFINED`. Face holds. Unique-L leftover
reports face `UNDEFINED` from mixed `O(C)`. Axis-cover face fails from
cover fail at `D`. Exist-opposite face of signed `O` fails:
`O(C)={−e_2, +e_3, −e_3}` and `O(D)={+e_1}` include no opposite pair.
Named-sign lettering lost the axis.

Face holds at τ1 and at τ2.

## Theorem 3 — composition of `M` and `O` at `t+2` versus `t+3`

Composition HOLD if and only if `M(t+2)=M(t+3)` and `O(t+2)=O(t+3)` at
`A`, at `B`, at `C`, and at `D`. Each of the four own incoming sets and
four own outgoing sets at `τ2` equals the same set at `τ1`. None is
`UNDEFINED`.

Composition of M and O: hold

Displayed, not adopted. The bits are not written into Admissibility.
Do not write into Admissibility. Do not attach L1. Composition HOLD is
equality of the four `M` sets and the four `O` sets, not equality of
reverse/face bits: those bits also match here (`hold`/`hold` at both cuts)
by accident of frozen sets, and reverse/face-bit composition is a different
object. A new six-neighbor of `B` at `t(B)+3` does not enter `O`.

This is not leftover of nm2simt2slx simultaneous freeze t+1 versus t+2:
that leftover has no `t+3` cut and reports no new six-neighbor at `t+2`.
This is not leftover of nm2simslx simultaneous at `t+1` only: that leftover
has no `t+2` cut. This is not leftover of two-axis opposite simultaneous
freeze: that leftover has `−e_1` in `O(D)`. This is not leftover of
nm2ot3slx O freeze: that leftover scores exist-opposite reverse fail and
face fail, and composition of `O` alone. This is not leftover of nmot2
`O` at `t` versus `t+1`: empty `O` at `t` is not `O` at `t+1`, so that
leftover composition of `O` fails. This is not leftover of nmt2 `M`
two-tick. This is not leftover of nmout eventual-`O`. This is not leftover
of axis-cover. This is not leftover of forall-perp HOLD/HOLD. This is not
leftover of mixed #7188 fail/fail.

Composition HOLDs.

## What this note does not claim

- It does not select a unique incoming or outgoing lock.
- It does not reduce lock vectors to named signs `{+,−}`.
- It does not require simultaneous sides to be singletons.
- It does not sum either set.
- It does not replace simultaneous by leftover-empty fail.
- It does not replace simultaneous by leftover of `M` alone.
- It does not replace simultaneous by leftover of `O` alone.
- It does not replace simultaneous by existential opposite of signed locks.
- It does not replace simultaneous by unsigned axis-cover of `M` and `O`.
- It does not replace simultaneous by forall-perp of integer dots.
- It does not replace simultaneous by 1-in 2-out axis split.
- It does not replace `O` by `M`.
- It does not replace composition of `M` and `O` by O-only composition.
- It does not replace composition of `M` and `O` by M-only composition.
- It does not replace composition of the four `M` and `O` sets by
  reverse/face-bit equality.
- It does not attach a formation member from already-recorded six-neighbor
  locks.
- It does not use a six-neighbor star as the letter.
- It does not wait for a global later T.
- It does not reprint nm2simslx simultaneous at `t+1` only as this freeze.
- It does not reprint nm2simt2slx freeze from `t+1` to `t+2` as this freeze.
- It does not reprint two-axis opposite simultaneous freeze as this member.
- It does not reprint nm2ot3slx O freeze exist-opposite reverse fail.
- It does not reprint nmot2 `O` at `t` versus `t+1`.
- It does not reprint nmt2 `M` two-tick.
- It does not reprint nmout eventual-`O`.
- It does not reprint nm2simz HOLDING as this member.
- It does not reprint nm2slpx forall-perp reverse hold and face hold.
- It does not reprint nm2slx cover reverse fail and face fail as this
  member.
- It does not reprint nm2simslz same-lock z-probe reverse fail as this
  member.
- It does not reprint 1-axis same-lock reverse fail and face fail as this
  member.
- It does not reprint y-probe simultaneous reverse hold and face hold.
- It does not reprint z-probe simultaneous reverse fail and face hold.
- It does not reprint M exist-opposite reverse fail and face fail as this
  member.
- It does not reprint the two-tick lock-count clock composition.
- It does not reprint mixed #7188 fail/fail as this member.
- It does not treat the second same-lock pair as a formed child of the first.
- It does not score the y-probes or the z-probes as this letter.
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
two-axis same-lock four-site process, simultaneous `M` and `O` at `t+2` and
at `t+3`, reverse/face from simultaneous HOLD at each cut, and composition
as equality of those four `M` sets and four `O` sets are displayed
theorem-domain data.

## Exact target and obligation graph

| Obligation | Status |
|---|---|
| current Lattice / Admissibility / Record premises | quoted; no edit |
| perp-step incoming-lock process on `B_3(0)` | displayed; two disjoint same-lock pairs `+e_1/+e_1` and `+e_2/+e_2` |
| ticks `t(A)`, `t(B)`, `t(C)`, `t(D)` | Theorem 1; `2`, `1`, `3`, `2` |
| `M` and `O` at `τ1=t+2` and at `τ2=t+3` | Theorem 1; frozen equal; sim HOLD at each |
| reverse from simultaneous at `τ1` and `τ2` | Theorem 2; `hold`, `hold` |
| face from simultaneous at `τ1` and `τ2` | Theorem 2; `hold`, `hold` |
| composition of `M` and `O` at `t+2` versus `t+3` | Theorem 3; `HOLD` |
| comparison to two-axis opposite leftover | Theorem 1; opposite `O(D)` includes `−e_1` |
| comparison to 1-axis same-lock | Theorem 1; 1-axis `t(A)=3` and mixed `M(A)` |
| unique incoming lock | not required |
| occupancy of sites as the letter | not used |
| named-sign `{+,−}` letter | not used; lost the axis |
| singleton unique lock-vector letter | not used as the object; mixed remains a set |
| `Z^3` sum of the lock set | not used; no aggregation |
| six-neighbor star as the letter | not used |
| leftover of unique-L | not this display |
| leftover of axis-cover | not this display |
| leftover of leftover-empty fail | not this display |
| leftover of M exist-opposite | not this display |
| leftover of O exist-opposite | not this display |
| leftover of nm2simslx simultaneous at `t+1` only | not this display |
| leftover of nm2simt2slx simultaneous freeze t+1 versus t+2 | not this display; no `t+3` cut there |
| leftover of two-axis opposite simultaneous freeze | not this display |
| leftover of nm2ot3slx O freeze | not this display |
| leftover of nmot2 `O` at `t` versus `t+1` | not this display |
| leftover of nmt2 `M` two-tick | not this display |
| leftover of nmout eventual-`O` | not this display |
| leftover of y-probe simultaneous | not this display |
| leftover of z-probe simultaneous | not this display |
| leftover of forall-perp reverse/face | not this display |
| leftover of reverse/face-bit composition | not this display |
| leftover of mixed #7188 fail/fail | not this display |
| leftover of two-tick lock-count clock | not this display |
| second pair as formed child | refused; new seed |
| y-probe or z-probe simultaneous on this seed | not this letter |
| global later T | not used |
| simultaneous as Admissibility content | not adopted |
| formation site / probability / rate | open |
| physical Record readout of the bits | open |

## Value gate (V1–V5)

| # | Answer |
|---|---|
| V1 | It answers the first-display question: simultaneous `M` and `O` at `t+2` versus `t+3` on the four x-probes of the two-axis same-lock seed, reverse/face at each cut, and composition or `UNDEFINED`. |
| V2 | Current main has no landed simultaneous freeze `t+2` versus `t+3` reverse/face report on these four x-probes of this two-axis same-lock seed. |
| V3 | Simultaneous reports at two cuts, the four reverse/face bits, and composition as set equality of `M` and of `O` are independently finite and exact. |
| V4 | The theorem is more than a restatement of Record because it reads signed-letter disjointness of own incoming and own outgoing at `t+2` and at `t+3` and scores set equality of both. |
| V5 | It is not an adopted content rule: the bits remain displayed. |

## No-go discipline gate

The negative content is narrow: the display does not write those bits into
Admissibility, does not reduce them to named signs, does not require a
unique lock, does not sum the lock set, does not replace simultaneous by
leftover-empty fail, does not replace simultaneous by leftover of `M`
alone or leftover of `O` alone, does not replace simultaneous by
existential opposite of signed locks, does not replace simultaneous by
unsigned axis-cover, does not replace simultaneous by forall-perp, does
not replace simultaneous by 1-in 2-out split, does not identify this
display with nm2simt2slx simultaneous freeze t+1 versus t+2, does not
identify this display with nm2simslx `t+1` only, does not identify it
with nm2ot3slx O freeze exist-opposite reverse fail, does not identify it
with nmot2 `O` at `t` versus `t+1`, and does not identify it with
forall-perp reverse hold and face hold. No global impossibility is claimed.

### N1 — materially distinct routes

| Route | Attempt | Why it fails here | Marker |
|---|---|---|---|
| leftover-empty fail | score reverse/face as leftover nonempty-equal | leftover of the unsigned-axis union is `{e_2}` at `A` and at `D` and empty at `B` and at `C`, leftover reverse and face fail, while simultaneous HOLDs | ATTEMPTED |
| leftover of `M` alone | score `{e_1,e_2,e_3}` minus `Axis(M)` | leftover of `M` at `A` is `{e_1,e_2}` and at `B` is `{e_2,e_3}`, nonempty unequal, reverse would fail | ATTEMPTED |
| leftover of `O` alone | score `{e_1,e_2,e_3}` minus `Axis(O)` | leftover of `O` at `A` is `{e_2,e_3}` and at `B` is `{e_1}`, nonempty unequal, reverse would fail | ATTEMPTED |
| nmsimopp exist-opposite | reuse signed reverse hold and face hold of `M` and of `O` | signed `M` reverse fails and signed `O` reverse fails; simultaneous reverse HOLDs from per-probe letter-disjoint nonempty `M` and `O` | ATTEMPTED |
| nm2slx axis-cover | reuse complementary unsigned axes of `M` and `O` | cover reverse FAIL face FAIL because the union misses e_2 at `A` and at `D`; simultaneous reverse HOLD face HOLD | ATTEMPTED |
| nm2slpx forall-perp | score every integer dot `m·o=0` | `{+e_1}` and `{−e_1}` HOLD simultaneous and fail forall-perp; forall-perp is integer dots, simultaneous is signed-letter disjointness | ATTEMPTED |
| 1-in 2-out | require `|Axis(M)|=1` and cover | 1-in 2-out fails at `A` and at `D` on these x-probes; simultaneous HOLDs | ATTEMPTED |
| nm2simz HOLDING | reuse opposite seed `+e_1/−e_1` and `+e_2/−e_2` on z-probes | different seed and different probes; here x-probe `A` forms at tick 2 locking `−e_3` | ATTEMPTED |
| nm2simslx `t+1` only | score simultaneous at one cut | that leftover has no `t+2` freeze report; this letter compares `τ1` to `τ2` | ATTEMPTED |
| nm2simt2slx freeze t+1 versus t+2 | score `t+1` versus `t+2` | that leftover reports reverse hold, face hold, and composition HOLD with no `t+3` freeze and no new six-neighbor at `t+2` | ATTEMPTED |
| nm2ot3slx O freeze | score exist-opposite of `O` at two cuts | exist-opposite reverse fails and face fails; simultaneous reverse HOLDs and face HOLDs | ATTEMPTED |
| nmot2 `O` at `t` versus `t+1` | score freeze from formation tick | `O` empty at all four x-probes at `t`, simultaneous fail, composition of `O` fail; this letter starts at `t+2` | ATTEMPTED |
| nmt2 `M` two-tick | score equality of incoming sets | M exist-opposite reverse fail and face fail; composition here also requires frozen `O` | ATTEMPTED |
| nmout eventual-`O` | score neighbor locks with no tick cut | eventual `O` has no `t+2` versus `t+3` report | ATTEMPTED |
| unique-L leftover | require a singleton `{v}` else `UNDEFINED` | mixed `O(B,τ)` and mixed `O(C,τ)` have three steps; unique-L reverse and face are `UNDEFINED` while simultaneous HOLDs | ATTEMPTED |
| 1-axis same-lock | reuse seed `{0,(0,1,0)}` with `+e_1/+e_1` | 1-axis `t(A)=3` and mixed `M(A)`; here `t(A)=2` and `M(A)={−e_3}` | ATTEMPTED |
| y-probe simultaneous | score the four y-probes on this seed | y-probe reverse HOLDs and face HOLDs; this letter is the four x-probes | ATTEMPTED |
| z-probe simultaneous | score the four z-probes on this seed | z-probe reverse fails; this letter is the four x-probes | ATTEMPTED |
| reverse/face-bit composition | HOLD iff reverse/face bits match | the scored object is equality of the four `M` sets and four `O` sets; bit match is an accident of frozen sets | ATTEMPTED |
| sum of the same outgoing sets | replace `O` by the `Z^3` sum | the construction does not sum; sum of mixed `O(B)` is `+e_2`, not an opposite of `O(A)` | ATTEMPTED |
| named-sign lettering | collapse `{±e_i}` to `{+,−}` | named-sign lettering lost the axis | ATTEMPTED |
| six-neighbor lock union | score locks of six-neighbors formed by `t(q)` | that leftover union at `A` is `{+e_1,−e_3}`; own outgoing at `A` is `{+e_1}` | ATTEMPTED |
| mixed #7188 fail/fail | reuse z-symmetric mixed reverse-fail face-fail | different process; this member reports simultaneous HOLD reverse hold face hold | ATTEMPTED |
| two-tick lock-count clock | replace `M` and `O` by a count of locks | counts are not lock sets and are not this letter | ATTEMPTED |
| nsopp leftover child | treat `(0,0,1)` and `(0,1,1)` as formed children | they are tick-0 seeds with `+e_2/+e_2`, not tick-1 children | ATTEMPTED |
| global later T | wait until `max t(A,B,C,D)` before reading | `τ1(q)=t(q)+2` and `τ2(q)=t(q)+3` are per-probe; no global T | ATTEMPTED |
| attach a formation member from already-recorded six-neighbor locks | form the probes by a neighbor-lock letter instead of perp-step | refused; not attached | ATTEMPTED |
| adopt bits into Admissibility | rewrite the local rule by simultaneous | refused; displayed, not adopted | ATTEMPTED |

### N2 — wall independence

Missing physical adoption, missing identification of simultaneous with
leftover of `M` alone, missing identification of simultaneous with
leftover-empty fail, missing identification of simultaneous with
existential opposite of signed locks, missing identification of
simultaneous with unsigned axis-cover, missing identification of
simultaneous with forall-perp, missing identification of this freeze with
nm2simt2slx t+1 versus t+2, missing identification of this freeze with
nm2simslx `t+1` only, missing identification with nm2ot3slx O freeze, and
missing Record identification of simultaneous reverse are distinct open
premises. This note claims no complete wall collection.

### N3 — hidden-condition scan

The host `B_3(0)`, four-site two-axis same-lock seed locks `+e_1/+e_1` and
`+e_2/+e_2`, perpendicular step rule, incoming-step lock, own incoming set
and own outgoing dual from records with tick `<= τ`, per-probe `τ1=t+2`
and `τ2=t+3`, simultaneous as defined nonempty disjoint `M` and `O`, HOLD
iff simultaneous not leftover-empty fail, composition as equality of the
four `M` sets and four `O` sets, four x-probes with non-seed `A`, second
pair is a new seed, and mixed remains a set are declared. No uniqueness of
incoming locks, no six-neighbor lock union as the scored object, no
occupancy of sites as the letter, no named-sign reduction, no singleton
leftover as the object, no sum leftover, no unique-L leftover, no
axis-cover leftover, no nmot2 leftover as the scored cut, no global later
T, no formation attachment from already-recorded six-neighbor locks, and
no Admissibility rewrite are silently assumed.

### N4 — source residual matching

The current axiom memo supplies cubic sites, `M_2(C)`,
content-conditional-on-formation, and unreadable absence. The residual that
formation site, probability, and rate remain unsupplied is unchanged. The
simultaneous reverse-hold and face-hold reports, and composition HOLD of
frozen `M` and frozen `O`, do not close that residual.

### N5 — resolution and rhetoric audit

| Resolution | Executed | Not claimed |
|---|---|---|
| per element | each signed lock among `{±e_1,±e_2,±e_3}` in `M` or in `O` at a probe's `t+2` or `t+3` | no continuum alphabet |
| per site | `A,B,C,D` x-probes on `B_3(0)` only | no other cubic sites |
| per mode | no mode calculation | no spectral exhaustion |
| per block | four sim reports at two cuts plus reverse/face/composition | no adopted content law |
| lattice wide | checked and not executed | no lattice-wide lettering rule |

### N6 — live partial-closure paths

Live routes include a later Record content map for simultaneous reverse/face,
a formation-rate rule, and a physical selector among disjoint incoming and
outgoing letters. None is taken here.

### N7 — hostile steelman

**Steelman:** Simultaneous freeze should be refused as leftover because
nm2simt2slx already HOLDs simultaneous reverse, face, and composition from
`t+1` to `t+2`; nm2simslx already HOLDs simultaneous reverse and face at
`t+1`; nm2ot3slx already displayed O freeze composition HOLD; nmt2 already
displayed M freeze; two-axis opposite simultaneous freeze already reported
the same bits on these x-probes; nm2slpx already displayed forall-perp
HOLD/HOLD at `t+1`; axis-cover already answered three-axis occupation;
unique-L already fails at mixed `B`; `M` and `O` are frozen by construction
of earliest incoming of neighbors, so composition HOLD is tautological;
reverse/face bits already match, so bit composition is enough; 1-axis
same-lock already reports the same `O` letters; nmot2 already scored `O`
across two ticks; and empty `O` should be `UNDEFINED` like unformed.

**Answer:** nm2simt2slx scores `τ1=t+1` versus `τ2=t+2` and reports no new
six-neighbor at `t+2`. This letter scores `τ1=t+2` versus `τ2=t+3`. A new
six-neighbor of `B` forms at `t(B)+3` and still does not enter `O`.
nm2simslx scores one cut `τ=t+1` and has no freeze report. nm2ot3slx scores
exist-opposite of `O`: reverse fails and face fails. This letter scores
simultaneous reverse hold and face hold, and composition of both `M` and
`O`. Opposite leftover includes `−e_1` at `D`. This member has
`O(D)={+e_1}`. nm2slpx scores forall-perp of `M` versus `O` at `t+1` only:
forall-perp reverse HOLDs and face HOLDs, but `{+e_1}` versus `{−e_1}`
splits the predicates. Unique-L reverse is `UNDEFINED` at mixed `O(B)`
while simultaneous reverse HOLDs. Frozen earliest incoming of neighbors is
exactly the two-tick fact being displayed: `M` and `O` remain equal even
though a new six-neighbor of `B` forms at `t+3`. Reverse/face-bit equality
is a different object: it would HOLD even if some `O` changed while the
simultaneous bits stayed `hold`/`hold`. 1-axis same-lock has `t(A)=3` and
mixed `M(A)`; this member has `t(A)=2` and `M(A)={−e_3}`. nmot2 scores `O`
at `t` versus `t+1`, where simultaneous fails and composition of `O` fails.
Empty `O` is empty, not `UNDEFINED`; unformed at `τ` is `UNDEFINED`. Reverse
holds at `τ1` and at `τ2`. Face holds at `τ1` and at `τ2`. Composition of
`M` and `O` HOLDs.

### N8 — cross-cycle echo

nm2simt2slx reported simultaneous reverse hold, face hold, and composition
HOLD from `t+1` to `t+2` on these same-lock x-probes with no new
six-neighbor at `t+2`. nm2simslx reported simultaneous reverse hold and
face hold on these same-lock x-probes at `t+1` only. nm2ot3slx reported O
freeze reverse fail, face fail, and composition HOLD of `O` alone.
Two-axis opposite O freeze reported reverse fail, face fail, and
composition HOLD with `O(D)` including `−e_1`. nm2slpx reported forall-perp
reverse hold and face hold on these x-probes at `t+1`. nm2slx cover on
these x-probes reports cover fail at `A` and at `D`, reverse fail, and
face fail because the union misses e_2. nm2simslz on this same seed
reports simultaneous fail at z-probe `A`, reverse fail, and face hold.
This note is not those displays: it reports simultaneous `M` and `O` at
`t+2` versus `t+3` on two disjoint same-lock pairs with x-probes,
simultaneous HOLD at each of the four x-probes at both cuts, reverse hold
at both cuts, face hold at both cuts, and composition HOLD because
`M(t+2)=M(t+3)` and `O(t+2)=O(t+3)` at `A,B,C,D`. Discriminator versus
nm2simt2slx is the `t+3` cut and the new six-neighbor of `B` that does not
grow `O`. Discriminator versus nm2simslx is the `t+2` versus `t+3` cut.
Discriminator versus nm2ot3slx is both simultaneous bits versus
exist-opposite fail. Discriminator versus opposite leftover is the missing
`−e_1` at `D`. Discriminator versus forall-perp is signed-letter
disjointness versus integer dots. Discriminator versus 1-axis is `t(A)`
and `M(A)`. Discriminator versus y-probes is the probe set. Discriminator
versus z-probes is reverse hold versus reverse fail.

**Gate disposition:** PASS for the simultaneous freeze `t+2` versus `t+3`
reverse/face reports above. FAIL / DO NOT SHIP for “the predicate equals
the named sign,” “the predicate equals the unique singleton lock vector,”
“the predicate equals the sum of the lock set,” “the predicate equals
leftover-empty fail,” “the predicate equals leftover of `M` alone,” “the
predicate equals leftover of `O` alone,” “the predicate equals nmsimopp
exist-opposite HOLD,” “the predicate equals nm2slx axis-cover,” “the
predicate equals nm2slpx forall-perp,” “the predicate equals 1-in 2-out,”
“the predicate equals nm2simz HOLDING,” “the predicate equals nm2simslx
`t+1` only,” “the predicate equals nm2simt2slx t+1 versus t+2,” “the
predicate equals nm2ot3slx O freeze,” “the predicate equals nmot2 `O` at
`t` versus `t+1`,” “composition equals reverse/face-bit equality,” “bits
are Admissibility,” “simultaneous fails at `A`,” “reverse simultaneous
fails,” or “face simultaneous fails.”

## Primary runner

The paired runner builds Euclidean `B_3(0)`, runs the two-axis same-lock
perp-step incoming-lock process, reads each x-probe's own earliest incoming
set and own outgoing dual from the record prefix at that probe's `t+2` and
at `t+3`, reports simultaneous of the pair at each cut, scores reverse and
face from simultaneous HOLD at each cut, scores composition as equality of
the four `M` sets and the four `O` sets, lists new records in `B_3(0)`
between `t+2` and `t+3` that meet a probe's
six-neighbors, compares the same observables on the 1-axis same-lock seed
and on the two-axis opposite seed, and checks Theorems 1--3. It also checks
that simultaneous HOLDs at each probe at both cuts, that reverse holds and
face holds at both cuts, that composition HOLDs, that leftover-empty fail
is a different reverse and face, that leftover of `M` alone and leftover of
`O` alone are different objects, that mixed sets remain sets, that
unique-letter simultaneous is `UNDEFINED` at mixed `O(B)`, that
exist-opposite reverse of `O` fails, that the construction does not sum,
that a formation member from already-recorded six-neighbor locks is not
attached, that unsigned axis-cover is a different letter, that forall-perp
is a different letter, that 1-in 2-out is a different letter, that the
second pair is a new seed, and that the display is not the two-tick
lock-count clock composition. No runner cache is written.
