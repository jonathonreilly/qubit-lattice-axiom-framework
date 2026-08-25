---
claim_id: two_axis_same_lock_xprobe_neighbor_read_incoming_tplus1_tplus2_composition_reverse_face_bounded_theorem_note_2026-08-15
claim_type: bounded_theorem
claim_scope: "Neighbor-read of M at t+1 versus t+2 on the four x-probes of the two-axis same-lock seed, reverse/face at each cut, and composition, are reported. Displayed, not adopted."
upstream_dependencies:
  - minimal_axioms
runner: scripts/two_axis_same_lock_xprobe_neighbor_read_incoming_tplus1_tplus2_composition_reverse_face_2026_08_15.py
---

# Neighbor-Read Of Incoming M At t+1 Versus t+2 Reverse Face And Composition On Four Two-Axis Same-Lock X-Probes

> **Key terms used in this doc** are indexed A-Z at `docs/KEY_TERMINOLOGY.md`;
> each row points to the canonical source-of-truth doc.

**Date:** 2026-08-15
**Type:** bounded_theorem
**Scope:** neighbor-read of earliest incoming set `M` at each probe's
`τ1=t+1` versus `τ2=t+2`, reverse/face from that neighbor-read at each cut,
and composition of the neighbor-read bits, on the four x-probes of the
two-axis same-lock seed in `B_3(0)={n:n·n<=9}`, no global T. Same process
and x-probes as nm2slpx. Let `t(q)` be the formation tick of probe `q`. Let
`τ1(q)=t(q)+1` and `τ2(q)=t(q)+2`. `M(q,τ)` is the set of earliest incoming
nearest-neighbor steps at `q` using only records with tick `<= τ`. Seeds
are a singleton seed letter. Unformed at `τ` is `UNDEFINED`. Neighbor-read
HOLDs at `q,τ` if and only if some formed six-neighbor `r` has `M(r,τ)`
defined and equal to `M(q,τ)` as sets. Unformed `q` is `UNDEFINED`. Reverse
HOLDs at a cut if and only if neighbor-read HOLDs at `A` and at `B`. Face
HOLDs if and only if neighbor-read HOLDs at `C` and at `D`. Composition
HOLDs if and only if neighbor-read at `τ1` equals neighbor-read at `τ2` at
`A`, `B`, `C`, and `D`. This is the first neighbor-read of `M` at `t+1`
versus `t+2` on the nm2readslx HOLDING same-lock x member. This is not leftover
of nm2readslx one-cut neighbor-read. This is not leftover of nm2slpx
forall-perp. This is not leftover of nm2slx axis-cover. This is not leftover
of nm2simslx simultaneous. This is not leftover of nm2readslz same-lock
z-probe neighbor-read. This is not leftover of two-axis opposite x-probe
neighbor-read. This is not leftover of nm2t2slx M freeze. This is not leftover
of R-style recovery of the incoming step from neighbors. Neither pair is
opposite. Uniqueness is not required. Mixed remains a set.
Occupancy `n` is not used. Displayed, not adopted. Do not write into
Admissibility. Do not attach L1.
**Audit-status authority:** independent audit lane only. This note authors no
audit verdict and predicts none.
**Primary runner:**
[`scripts/two_axis_same_lock_xprobe_neighbor_read_incoming_tplus1_tplus2_composition_reverse_face_2026_08_15.py`](../scripts/two_axis_same_lock_xprobe_neighbor_read_incoming_tplus1_tplus2_composition_reverse_face_2026_08_15.py)

Framework input:

- [`MINIMAL_AXIOMS_2026-06-29.md`](MINIMAL_AXIOMS_2026-06-29.md) supplies
  cubic-lattice sites `Z^3` with nearest-neighbor adjacency, the one-site
  algebra `M_2(C)`, and the Record sentences that records form and that a
  present record locks exactly one admissible local possibility.

Everything after that quoted input is a finite displayed process on `B_3(0)`
and the four named x-probes. Incoming lock letters are unit nearest-neighbor
steps. Neighbor-read compares those incoming sets as sets at a formed
six-neighbor at each cut. Reverse and face are scored on neighbor-read HOLD
at the paired probes at each cut. Composition is equality of the four
neighbor-read bits across the two cuts. Named signs `{+,−}` are a coarser
readout and are not used. A singleton unique lock letter is a different
readout and is not used as the object. R-style recovery of the incoming step
as `−e` in `M(q+e,τ)` is a different readout and is not used. Forall-perp of
`M` versus outgoing dual `O` is a different readout and is not used.
Axis-cover of `M` and `O` is a different readout and is not used. Freeze of
`M` itself is leftover of nm2t2slx and is not used as the scored composition.
Occupancy of sites is not used. This display does not use occupancy. A
six-neighbor star is not the letter.

## Machine status and trace

```yaml
actual_current_surface_status: bounded-support
target_claim_type: bounded_theorem
claim_type_reason: "Exact report of neighbor-read of M at t+1 versus t+2 on the four x-probes of the two-axis same-lock seed, HOLD at A,B,C,D at both cuts, reverse hold and face hold at each cut, composition hold of the bits; uniqueness of incoming locks is not claimed and the bits are not adopted."
trace_class: frontier_discovery
target_claim_id: two_axis_same_lock_xprobe_neighbor_read_incoming_tplus1_tplus2_composition_reverse_face
target_blocker_text: "display neighbor-read of M at t+1 versus t+2 on the four x-probes of the two-axis same-lock seed, reverse/face at each cut, and composition"
source_of_blocker_text: handoff
reachability_to_target: advances
artifact_role: theorem
next_trace_action: "Keep neighbor-read of M at t+1 versus t+2 displayed; do not write the bits into Admissibility, do not reduce to R-style recovery, do not reduce to nm2slpx forall-perp, do not reduce to nm2slx cover leftover, do not reduce to nm2readslx one-cut leftover, do not reduce to nm2t2slx M freeze, do not replace the display by two-axis opposite x-probe neighbor-read, do not reduce to nm2simslx simultaneous, do not require a unique letter, and do not attach L1."
conditional_surface_status: "exact on B_3(0) for neighbor-read of M at t+1 versus t+2 on the four x-probes of the two-axis same-lock seed, reverse/face at each cut, and composition; displayed, not adopted"
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
neighbor-read of `M` is scored:

```text
A = (1,0,0),  B = (1,1,1),  C = (2,0,0),  D = (1,1,0).
```

These are not the y-probes `A=(0,1,0)`, `B=(1,1,1)`, `C=(0,2,0)`,
`D=(1,1,0)`. These are not the z-probes `A=(0,0,1)`, `B=(1,1,1)`, `C=(0,0,2)`,
`D=(1,0,1)`. `A` is not a seed. Same process and x-probes as nm2slpx.

Lock alphabet of the displayed process: `{±e_i}` with `i` in `{1,2,3}`.

Seed: two disjoint same-lock pairs recorded at formation tick 0. Origin
locks `+e_1` and `(0,1,0)` locks `+e_1`. `(0,0,1)` locks `+e_2` and
`(0,1,1)` locks `+e_2`. The second pair is a new seed, not a formed child
of the first pair, and neither pair is opposite. This seed is not the 1-axis
same-lock two-site seed `{0,(0,1,0)}` with `+e_1/+e_1` alone. This seed is
not the two-axis opposite seed `+e_1/−e_1` and `+e_2/−e_2`. This seed is
not the y-symmetric three-site seed that also records `(0,-1,0)` at tick 0.
This seed is not the x-axis same-lock seed `{0,(1,0,0)}` with `+e_2/+e_2`.
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

## Named neighbor-read of `M` at `τ1=t+1` and `τ2=t+2`

Let `t(q)` be the formation tick of x-probe `q` when that tick is defined in
`B_3(0)`. Let `τ1(q)=t(q)+1` and `τ2(q)=t(q)+2`. There is no global T.

`M(q,τ)` is the set of earliest incoming nearest-neighbor steps at `q`
using only records with tick `<= τ`. If `q` is unformed at `τ`, then
`M(q,τ)` is `UNDEFINED`. If `q` is a seed and `τ >= 0`, then `M(q,τ)` is
the singleton seed letter.

Neighbor-read at a formed probe at the same cut:

```text
neighbor-read(q,τ) HOLDs iff some formed 6-NN r has M(r,τ)
defined and equal to M(q,τ) as sets.
```

If `q` is unformed at `τ`, then neighbor-read is `UNDEFINED`. Empty match
fails. Mixed remains a set: equality is set equality, not a unique-letter
reduction. Occupancy of sites is not used. The construction does not require
`M` to be a singleton. It does not sum the set. It does not wait for a
global later T.

R-style recovery is a different object: the set of steps `e` such that
`−e` lies in `M(q+e,τ)`. Forall-perp of `M` versus outgoing dual `O` is a
different object. Axis-cover of `M` and `O` is a different object. Freeze of
`M` across the two cuts is leftover of nm2t2slx: that leftover scores
`M(τ1)=M(τ2)`, not neighbor-read bits.

Reverse neighbor-read holds at a cut if and only if neighbor-read HOLDs at
`A` and at `B`. Face neighbor-read holds if and only if neighbor-read HOLDs
at `C` and at `D`. Either side `UNDEFINED` is `UNDEFINED`. Else if both
sides HOLD, reverse or face HOLDs. Else fail.

Composition holds if and only if neighbor-read at `τ1` equals neighbor-read
at `τ2` at `A`, `B`, `C`, and `D`. Any `UNDEFINED` side is `UNDEFINED`. Else
if the four bits are equal across the two cuts, composition HOLDs. Else
fail.

Identifying a named sign of those locks with reverse or face is refused:
named-sign lettering lost the set. Identifying R-style recovery with
neighbor-read is refused: at `A`, R-style is `{−e_1}` while `M(A,τ1)={−e_3}`;
at `C`, R-style is `{+e_3}` while `M(C,τ1)={+e_1}`; at `B`,
R-style is empty while neighbor-read HOLDs; at `D`, R-style is `{−e_1}`
while `M(D,τ1)={−e_3}`. Identifying nm2slpx forall-perp
with this reverse/face is refused: forall-perp scores every incoming letter
against every outgoing dual letter at one probe; neighbor-read scores
set-equality of own incoming `M` at a formed six-neighbor. Identifying
nm2slx axis-cover with this reverse/face is refused: nm2slx cover fails at
`A` and at `D` and fails reverse and face; this member HOLDs at each
x-probe and HOLDs reverse and face at both cuts. Identifying nm2simslx
simultaneous with this reverse/face is refused: simultaneous asks whether
nonempty `M` and nonempty `O` are letter-disjoint; `O(A,τ)={+e_1}` is not
`M(A,τ)={−e_3}`. Identifying two-axis
same-lock z-probe neighbor-read with this reverse is refused: that leftover
has seed `A` at tick 0 with `M={+e_2}`; here `A` is not a seed, `t(A)=2`,
and `M(A,τ1)={−e_3}`. Identifying two-axis opposite x-probe neighbor-read
with this reverse is refused: opposite x-probes also HOLD reverse and face
and composition, but `M((0,1,1),τ)` there is `{−e_2}` while here it is
`{+e_2}`, and `M((0,1,0),τ)` there is `{−e_1}` while here it is `{+e_1}`.
Identifying nm2readslx one-cut neighbor-read with this freeze is refused: that
leftover scores only `τ=t+1`. Identifying nm2t2slx M freeze with this
composition is refused: that leftover scores equality of `M` sets; this
letter scores equality of neighbor-read bits. Opposite z-probe neighbor-read
freezes fail at seed `A`, so composition of those bits HOLDs while reverse
fails; this member HOLDs reverse.

## Theorem 1 — ticks, `M` and neighbor-read at `τ1` and `τ2`

On this process the four x-probes form. Incoming is frozen at formation:
`M(q,t+1)=M(q,t)` at every scored probe, and remains frozen from `τ1` to
`τ2`. Compare to nm2slpx forall-perp: that leftover HOLDs reverse and face
by scoring integer dots of `M` versus `O`. Compare to nm2readslx: that leftover
scores neighbor-read only at `τ=t+1`. Here `M` is read at both cuts `τ1=t+1`
and `τ2=t+2` and scored by set-equality at a formed six-neighbor. Neighbor-read
HOLDs at `A`, at `B`, at `C`, and at `D` at both cuts. Reverse HOLDs at both
cuts. Face HOLDs at both cuts. Composition HOLDs. The match at `A` is
`D=(1,1,0)` with the same letter `{−e_3}` at both cuts. The match at `D` is
`A=(1,0,0)` with the same letter `{−e_3}` at both cuts.

```text
t(A)=2
t(B)=1
t(C)=3
t(D)=2
M(A, τ1) = {−e_3}
M(B, τ1) = {+e_1}
M(C, τ1) = {+e_1}
M(D, τ1) = {−e_3}
neighbor-read(A, τ1) = hold
neighbor-read(B, τ1) = hold
neighbor-read(C, τ1) = hold
neighbor-read(D, τ1) = hold
M(A, τ2) = {−e_3}
M(B, τ2) = {+e_1}
M(C, τ2) = {+e_1}
M(D, τ2) = {−e_3}
neighbor-read(A, τ2) = hold
neighbor-read(B, τ2) = hold
neighbor-read(C, τ2) = hold
neighbor-read(D, τ2) = hold
formed 6-NN of A at τ1: (2, 0, 0)={+e_1}, (0, 0, 0)={+e_1}, (1, 1, 0)={−e_3}, (1, -1, 0)={+e_1}, (1, 0, 1)={+e_1}, (1, 0, -1)={+e_1}
formed 6-NN of B at τ1: (2, 1, 1)=UNDEFINED, (0, 1, 1)={+e_2}, (1, 2, 1)={+e_2}, (1, 0, 1)={+e_1}, (1, 1, 2)={+e_1, +e_3}, (1, 1, 0)={−e_3}
formed 6-NN of C at τ1: (1, 0, 0)={−e_3}, (2, 1, 0)={+e_1}, (2, -1, 0)={−e_2, −e_3}, (2, 0, 1)={+e_2, +e_3, −e_3}, (2, 0, -1)={−e_3}
formed 6-NN of D at τ1: (2, 1, 0)={+e_1}, (0, 1, 0)={+e_1}, (1, 2, 0)={+e_1}, (1, 0, 0)={−e_3}, (1, 1, 1)={+e_1}, (1, 1, -1)={+e_1}
formed 6-NN of A at τ2: (2, 0, 0)={+e_1}, (0, 0, 0)={+e_1}, (1, 1, 0)={−e_3}, (1, -1, 0)={+e_1}, (1, 0, 1)={+e_1}, (1, 0, -1)={+e_1}
formed 6-NN of B at τ2: (2, 1, 1)=UNDEFINED, (0, 1, 1)={+e_2}, (1, 2, 1)={+e_2}, (1, 0, 1)={+e_1}, (1, 1, 2)={+e_1, +e_3}, (1, 1, 0)={−e_3}
formed 6-NN of C at τ2: (1, 0, 0)={−e_3}, (2, 1, 0)={+e_1}, (2, -1, 0)={−e_2, −e_3}, (2, 0, 1)={+e_2, +e_3, −e_3}, (2, 0, -1)={−e_3}
formed 6-NN of D at τ2: (2, 1, 0)={+e_1}, (0, 1, 0)={+e_1}, (1, 2, 0)={+e_1}, (1, 0, 0)={−e_3}, (1, 1, 1)={+e_1}, (1, 1, -1)={+e_1}
matching 6-NN of A at τ1: (1, 1, 0)
matching 6-NN of B at τ1: (1, 0, 1)
matching 6-NN of C at τ1: (2, 1, 0)
matching 6-NN of D at τ1: (1, 0, 0)
matching 6-NN of A at τ2: (1, 1, 0)
matching 6-NN of B at τ2: (1, 0, 1)
matching 6-NN of C at τ2: (2, 1, 0)
matching 6-NN of D at τ2: (1, 0, 0)
```

`A` is not a seed. `A` is the site `(1,0,0)` forming at tick 2 with
incoming `{−e_3}`. Mixed remains a set: `M((1,1,2),τ1)` at `B`'s first cut
is `{+e_1, +e_3}`, and `M((2,0,1),τ1)` at `C`'s first cut is
`{+e_2, +e_3, −e_3}`. Unique letters would assign `UNDEFINED` at those mixed
neighbors. Here uniqueness is not required. `M` is frozen from `t` to
`τ1=t+1` and remains frozen from `τ1` to `τ2` at each of the four x-probes.
Unformed six-neighbors remain `UNDEFINED` at both cuts and do not match.
`(2,1,1)` of `B` forms at tick 4, after `τ2=t(B)+2=3`, so it stays
`UNDEFINED` at both scored cuts.

New records in `B_3(0)` between `t` and `t+1` that meet a probe's
six-neighbors can enter neighbor `M` at `τ1`. No new six-neighbor of any
scored probe forms at `t+2`, so neither own `M` nor neighbor `M` can grow
between `τ1` and `τ2`:

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

On the two-axis opposite seed with the same x-probes, neighbor-read also
HOLDs reverse and face and composition with the same ticks and the same
probe letters, but the formed neighbor `(0,1,1)` of `B` locks `{−e_2}` and
the formed neighbor `(0,1,0)` of `D` locks `{−e_1}`. Here those neighbors
lock `{+e_2}` and `{+e_1}` because neither pair is opposite. That leftover is
not this display.

On the two-axis same-lock z-probes, `A=(0,0,1)` is a seed at tick 0 with
`M={+e_2}`, and neighbor-read HOLDs reverse and face and composition from
the same-lock partner seed. Here `A` is not a seed.

On the two-axis opposite z-probes, neighbor-read fails at `A` because the
partner seed `(0,1,1)` locks `−e_2`, unequal to `M(A,τ)={+e_2}`. That
leftover fails reverse at both cuts while composition of those bits HOLDs.
This member HOLDs reverse on the x-probes.

On the 1-axis same-lock two-site seed, `t(A)=3` with mixed `M`,
neighbor-read fails at `A` and at `D`, reverse and face fail, and
composition of those fail bits HOLDs. That is leftover of the first pair.
Here the second pair is a new same-lock seed, `t(A)=2`, and reverse and face
HOLD.

## Theorem 2 — reverse and face at `τ1` and at `τ2`

Reverse neighbor-read holds if and only if neighbor-read HOLDs at `A` and
at `B`. Neighbor-read HOLDs at `A` and HOLDs at `B` at both cuts. Reverse
HOLDs at both cuts. Face neighbor-read holds if and only if neighbor-read
HOLDs at `C` and at `D`. Both neighbor-reads HOLD at both cuts. Face HOLDs
at both cuts.

Reverse neighbor-read at τ1: hold
Reverse neighbor-read at τ2: hold
Face neighbor-read at τ1: hold
Face neighbor-read at τ2: hold

Both sides are defined, so this is not `UNDEFINED`. nm2readslz same-lock
z-probe neighbor-read reverse HOLDs because seed `A` matches the partner
seed letter `+e_2`; that leftover has `t(A)=0`, not `t(A)=2`. Two-axis
opposite z-probe neighbor-read reverse fails because neighbor-read fails
at seed `A`. Two-axis same-lock y-probe neighbor-read reverse HOLDs and
face fails. nm2slx
axis-cover reverse fails because cover fails at `A` from a union that
misses e_2. R-style recovery at `A` is `{−e_1}`, not equal to
`M(A,τ1)={−e_3}`, and R-style at `B` is empty. Those leftovers are not
this display. nm2readslx scores reverse only at `τ=t+1`; this letter also
scores `τ2`.

Reverse holds at τ1 and at τ2.
Face holds at τ1 and at τ2.

## Theorem 3 — composition of neighbor-read

Composition holds if and only if neighbor-read at `τ1` equals neighbor-read
at `τ2` at `A`, `B`, `C`, and `D`. Neighbor-read HOLDs at every scored
probe at both cuts.

Composition of neighbor-read: hold

Displayed, not adopted. The bits are not written into Admissibility.
Do not write into Admissibility. Do not attach L1.

This is not `fail` and not `UNDEFINED`. Scoring only `τ=t+1` is leftover of
nm2readslx. Scoring `M(τ1)=M(τ2)` is leftover of nm2t2slx: `M` also freezes
here, but composition of `M` is not composition of neighbor-read bits.
Opposite z-probe neighbor-read composition HOLDs because fail at `A` is
stable, while reverse fails; composition HOLD is not reverse HOLD. Same-lock
y-probe neighbor-read composition HOLDs while reverse HOLDs and face fails.
1-axis same-lock composition HOLDs while reverse and face fail. Those leftovers
are not this display.

On the same seed the four y-probes give reverse hold and face fail, with
seed `A` at tick 0. The four z-probes give reverse hold and face hold, with
seed `A` at tick 0 and `M(A,τ)={+e_2}`. Those probe-direction readouts are
not this x-probe display.

nm2slx cover face fails because cover fails at `D`. 1-axis same-lock face
fails. Two-site opposite leftover face fails. Z-symmetric leftover fails
at `A` and HOLDs face. Those leftovers are not this display.

Face holds at τ1 and at τ2.

## What this note does not claim

- It does not select a unique incoming lock.
- It does not reduce lock vectors to named signs `{+,−}`.
- It does not require neighbor-read sides to be singletons.
- It does not sum the incoming set.
- It does not replace neighbor-read by R-style recovery.
- It does not replace neighbor-read by nm2slpx forall-perp.
- It does not replace neighbor-read by nm2slx axis-cover.
- It does not replace neighbor-read by nm2simslx simultaneous.
- It does not replace neighbor-read by nm2readslz same-lock z-probe neighbor-read.
- It does not replace neighbor-read by two-axis opposite x-probe neighbor-read.
- It does not replace this freeze by nm2readslx one-cut neighbor-read.
- It does not replace composition of neighbor-read bits by nm2t2slx M freeze.
- It does not use a six-neighbor star as the letter.
- It does not wait for a global later T.
- It does not attach a formation member from already-recorded six-neighbor
  locks.
- It does not reprint 1-axis same-lock neighbor-read as this member.
- It does not reprint two-axis same-lock y-probe neighbor-read.
- It does not reprint two-axis same-lock z-probe neighbor-read.
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
two-axis same-lock four-site process, neighbor-read of `M` at `t+1` versus
`t+2`, reverse/face bits at each cut, and composition are displayed
theorem-domain data.

## Exact target and obligation graph

| Obligation | Status |
|---|---|
| current Lattice / Admissibility / Record premises | quoted; no edit |
| perp-step incoming-lock process on `B_3(0)` | displayed; two disjoint same-lock pairs `+e_1/+e_1` and `+e_2/+e_2` |
| ticks `t(A)`, `t(B)`, `t(C)`, `t(D)` | Theorem 1; `2`, `1`, `3`, `2` |
| `M` at `τ1` and `τ2` | Theorem 1; frozen equal across the two cuts |
| `M` at formed 6-NN at both cuts | Theorem 1; `D` matches `A` on `{−e_3}` at both cuts |
| neighbor-read bit at `τ1` and `τ2` | Theorem 1; HOLD at `A`,`B`,`C`,`D` at both cuts |
| reverse from neighbor-read at `τ1` and `τ2` | Theorem 2; `hold`/`hold` |
| face from neighbor-read at `τ1` and `τ2` | Theorem 2; `hold`/`hold` |
| composition of neighbor-read bits | Theorem 3; `hold` |
| compare to nm2readslx one-cut | Theorem 1; nm2readslx scores only `τ=t+1`; this letter also scores `τ2` and composition |
| compare to nm2t2slx M freeze | Theorem 3; M freeze HOLDs here too; composition is of neighbor-read bits, not of `M` |
| compare to nm2slpx forall-perp | Theorem 1; forall-perp HOLDs reverse/face by `M` versus `O` dots; this member HOLDs by set-equality of `M` at a formed 6-NN |
| compare to nm2slx cover | Theorem 1; cover reverse FAIL face FAIL; neighbor-read reverse HOLD face HOLD |
| compare to two-axis same-lock z-probe neighbor-read | Theorem 1; same-lock z has seed `A` at tick 0 with `M={+e_2}`; here `t(A)=2` and `M={−e_3}` |
| compare to two-axis opposite x-probe neighbor-read | Theorem 1; opposite HOLDs reverse/face/composition but neighbor `M` at `(0,1,1)` and `(0,1,0)` differs by sign |
| unique incoming lock | not required |
| occupancy of sites as the letter | not used |
| named-sign `{+,−}` letter | not used |
| singleton unique lock-vector letter | not used as the object; mixed remains a set |
| `Z^3` sum of the lock set | not used; no aggregation |
| six-neighbor star as the letter | not used |
| leftover of nm2readslx one-cut neighbor-read | not this freeze display |
| leftover of nm2t2slx M freeze | not this composition |
| leftover of nm2slpx forall-perp | not this neighbor-read display |
| leftover of nm2slx axis-cover | not this display |
| leftover of nm2simslx simultaneous | not this display |
| leftover of two-axis same-lock z-probe neighbor-read | not this display |
| leftover of two-axis opposite x-probe neighbor-read | not this display |
| leftover of R-style | not this display |
| leftover of 1-axis same-lock neighbor-read | not this display |
| leftover of y-probe neighbor-read | not this display |
| leftover of z-probe neighbor-read | not this display |
| global later T | not used |
| neighbor-read as Admissibility content | not adopted |
| formation site / probability / rate | open |
| physical Record readout of the bits | open |

## Value gate (V1–V5)

| # | Answer |
|---|---|
| V1 | It answers the first-display question: neighbor-read of `M` at `t+1` versus `t+2` on the HOLDING same-lock x member, reverse/face at each cut, and composition of those bits. |
| V2 | Current main has no landed neighbor-read freeze reverse/face of timed `M` on these four two-axis same-lock x-probes. |
| V3 | Neighbor-read reports at two cuts, reverse/face bits, and composition are independently finite and exact. |
| V4 | The theorem is more than a restatement of Record because it reads set-equality of own incoming `M` at a formed six-neighbor at `t+1` versus `t+2`. |
| V5 | It is not an adopted content rule: the bits remain displayed. |

## No-go discipline gate

The negative content is narrow: the display does not write those bits into
Admissibility, does not reduce them to named signs, does not require a
unique lock, does not replace neighbor-read by R-style recovery, does not
replace neighbor-read by nm2slpx forall-perp, does not replace neighbor-read
by nm2slx axis-cover, does not identify this display with two-axis
same-lock neighbor-read, does not identify it with nm2readslx one-cut
neighbor-read, and does not identify composition with nm2t2slx M freeze. No
global impossibility is claimed.

### N1 — materially distinct routes

| Route | Attempt | Why it fails here | Marker |
|---|---|---|---|
| nm2readslx one-cut | score neighbor-read only at `τ=t+1` | this letter also scores `τ2=t+2` and composition of the bits | ATTEMPTED |
| nm2t2slx M freeze | score `M(τ1)=M(τ2)` | `M` freezes here too; composition is equality of neighbor-read bits, not of `M` sets; opposite z freezes fail bits while reverse fails | ATTEMPTED |
| nm2slpx forall-perp | score every `m·o=0` of `M` versus `O` | forall-perp is incoming-versus-outgoing integer dots at one probe; neighbor-read is set-equality of `M` at a formed 6-NN; `O(A,τ)={+e_1}` is not `M(A,τ)={−e_3}` | ATTEMPTED |
| nm2slx axis-cover | reuse cover of `M` and `O` | cover fails at `A` and at `D` and fails reverse and face; neighbor-read HOLDs at each x-probe and HOLDs reverse and face | ATTEMPTED |
| nm2simslx simultaneous | score nonempty disjoint `M` and `O` | simultaneous is letter-disjointness of `M` and `O` at one probe; `O(A,τ)={+e_1}` is not `M(A,τ)={−e_3}` | ATTEMPTED |
| two-axis same-lock z-probe neighbor-read | reuse seed `+e_1/+e_1` and `+e_2/+e_2` on z-probes | that leftover has seed `A` at tick 0 with `M={+e_2}`; here `A` is not a seed, `t(A)=2`, and `M={−e_3}` | ATTEMPTED |
| two-axis opposite x-probe neighbor-read | reuse seed `+e_1/−e_1` and `+e_2/−e_2` on these x-probes | opposite HOLDs reverse/face/composition, but `M((0,1,1),τ)={−e_2}` and `M((0,1,0),τ)={−e_1}` there; here those neighbors lock `{+e_2}` and `{+e_1}` | ATTEMPTED |
| R-style recovery | recover incoming as `−e` in `M(q+e,τ)` | R-style at `A` is `{−e_1}` unequal to `{−e_3}`; at `C` is `{+e_3}` unequal to `{+e_1}`; at `B` and at `D` it is empty while neighbor-read HOLDs | ATTEMPTED |
| 1-axis same-lock neighbor-read | reuse seed `{0,(0,1,0)}` with `+e_1/+e_1` | 1-axis fails reverse and face with `t(A)=3`; here `t(A)=2` and reverse and face HOLD | ATTEMPTED |
| two-site opposite leftover | reuse opposite `+e_1/−e_1` without the second pair | that leftover fails reverse and face; this member HOLDs face from four same-lock seeds | ATTEMPTED |
| unique letter | replace mixed sets by a singleton or `UNDEFINED` | mixed neighbor `M((1,1,2),τ)={+e_1,+e_3}` remains a set; unique-letter is `UNDEFINED` while neighbor-read HOLDs at `B` | ATTEMPTED |
| y-probe neighbor-read | score the four y-probes on this seed | y-probe reverse HOLDs and face fails with seed `A` at tick 0; this letter is the four x-probes | ATTEMPTED |
| z-probe neighbor-read | score the four z-probes on this seed | z-probe `t(A)=0` with `M={+e_2}`; this letter has non-seed `A` at tick 2 with `M={−e_3}` | ATTEMPTED |
| z-symmetric leftover | reuse seed `{0,(0,0,1),(0,0,-1)}` | that leftover fails at `A`; this member HOLDs at `A` | ATTEMPTED |
| perp two-site leftover | reuse seed `{0,(0,1,0)}` with `+e_1/+e_2` | perp fails at each x-probe; this member HOLDs reverse and face | ATTEMPTED |
| named-sign lettering | collapse `{±e_i}` to `{+,−}` | named-sign lettering lost the set | ATTEMPTED |
| global later T | wait until `max t(A,B,C,D)` before reading | `τ1(q)=t(q)+1` and `τ2(q)=t(q)+2` are per-probe; no global T | ATTEMPTED |
| attach a formation member from already-recorded six-neighbor locks | form the probes by a neighbor-lock letter instead of perp-step | refused; not attached | ATTEMPTED |
| adopt bits into Admissibility | rewrite the local rule by neighbor-read freeze | refused; displayed, not adopted | ATTEMPTED |

### N2 — wall independence

Missing physical adoption, missing identification of neighbor-read with
R-style recovery, missing identification of neighbor-read with nm2slpx
forall-perp, missing identification of neighbor-read with nm2slx
axis-cover, missing identification of neighbor-read with nm2simslx
simultaneous, missing identification of this member with two-axis opposite
x-probe neighbor-read, missing identification of this freeze with
nm2readslx one-cut or with nm2t2slx M freeze, and missing Record
identification of neighbor-read reverse are distinct open premises. This
note claims no complete wall collection.

### N3 — hidden-condition scan

The host `B_3(0)`, four-site two-axis same-lock seed, perpendicular step
rule, incoming-step lock, own
incoming set from records with tick `<= τ`, per-probe `τ1=t+1` and
`τ2=t+2`, neighbor-read as set-equality of `M` at a formed six-neighbor,
composition as equality of those bits, four x-probes with non-seed `A`,
reverse as neighbor-read at `A` and `B`, face as neighbor-read at `C` and
`D`, and mixed remains a set are declared. No uniqueness of incoming locks,
no R-style recovery as the scored object, no forall-perp as the scored
object, no axis-cover as the scored object, no simultaneous as the scored
object, no M freeze as the scored composition, no global later T, no
formation attachment from already-recorded six-neighbor locks, and no
Admissibility rewrite are silently assumed.

### N4 — source residual matching

The current axiom memo supplies cubic sites, `M_2(C)`,
content-conditional-on-formation, and unreadable absence. The residual that
formation site, probability, and rate remain unsupplied is unchanged. The
neighbor-read reverse hold, face hold, and composition hold reports do not
close that residual.

### N5 — resolution and rhetoric audit

| Resolution | Executed | Not claimed |
|---|---|---|
| per element | each earliest incoming lock set `M` at a probe and at formed 6-NN | no continuum alphabet |
| per site | `A,B,C,D` x-probes on `B_3(0)` only | no other cubic sites |
| per mode | no mode calculation | no spectral exhaustion |
| per block | four neighbor-read reports at t+1 and t+2 plus reverse/face/composition | no adopted content law |
| lattice wide | checked and not executed | no lattice-wide lettering rule |

### N6 — live partial-closure paths

Live routes include a later Record content map for neighbor-read reverse/face,
a formation-rate rule, and a physical selector among matching six-neighbors.
None is taken here.

### N7 — hostile steelman

**Steelman:** Two-axis same-lock neighbor-read freeze on x-probes is leftover
of nm2readslx because the `t+1` bits already HOLD reverse and face; leftover
of nm2t2slx because `M` also freezes; leftover of nm2slpx forall-perp because
the same process and probes already HOLD reverse and face; leftover of
two-axis opposite x-probe neighbor-read because only a sign of two seed
letters changed; leftover of nm2simslx simultaneous because `M` and `O` are
already disjoint; leftover of nm2slx cover with the union demand dropped;
leftover of R-style because some neighbor already carries an opposite step;
and uniqueness of `M` already answers the match.

**Answer:** nm2readslx scores only `τ=t+1`. This letter also scores `τ2` and
composition of the four neighbor-read bits. nm2t2slx scores equality of `M`
sets; this composition scores equality of neighbor-read bits. Opposite
z-probe neighbor-read composition HOLDs while reverse fails, so composition
HOLD is not reverse HOLD and is not M freeze as a reverse. Forall-perp pairs
every incoming letter with every outgoing dual letter at one probe.
Neighbor-read asks whether some formed six-neighbor carries the same
incoming set. `O(A,τ)={+e_1}` is not `M(A,τ)={−e_3}`. Opposite x-probes
HOLD reverse and face with the same probe letters, but `M((0,1,1),τ)` and
`M((0,1,0),τ)` differ by sign because the pairs are opposite there. nm2slx
cover reverse FAIL face FAIL because the union misses e_2 at `A` and at
`D`; neighbor-read reverse HOLD face HOLD. R-style at `A` is `{−e_1}`, not
`{−e_3}`. Mixed neighbor `M((1,1,2),τ)={+e_1,+e_3}` remains a set;
uniqueness is not required. Reverse neighbor-read is HOLD iff neighbor-read
at `A` and at `B`, not leftover of forall-perp and not leftover of
two-axis opposite x-probe neighbor-read.

### N8 — cross-cycle echo

nm2readslx reported neighbor-read of `M` at `τ=t+1` on these four x-probes
with reverse hold and face hold. Two-axis opposite x-probe neighbor-read
reports HOLD at `A`,`B`,`C`,`D` at both cuts, reverse hold, face hold, and
composition hold, with neighbor `(0,1,1)` locking `{−e_2}`. nm2slpx reported
forall-orthogonal `M` versus `O` on these four x-probes with reverse hold
and face hold. nm2slx reported axis-cover of `M` versus `O` on these four
x-probes with reverse fail and face fail because the union misses e_2.
nm2simslx reported simultaneous `M` and `O` on these four x-probes with
reverse hold and face hold. nm2t2slx reported `M` freeze from `t` to `t+1`
on these x-probes. nm2readslz reported neighbor-read of `M` on two-axis
same-lock z-probes with reverse hold and face hold from seed `A` at tick 0.
Two-axis opposite z-probe neighbor-read reports fail at `A`, HOLD at
`B`,`C`,`D`, reverse fail, and face hold. Two-axis same-lock y-probes report
reverse hold and face fail. This note is not those displays: it reports
neighbor-read of `M` at `τ1=t+1` versus `τ2=t+2` on two disjoint same-lock
pairs with x-probes, HOLD at `A`,`B`,`C`,`D` at both cuts, reverse hold and
face hold at each cut, and composition hold. HOLD iff some formed 6-NN
recovers `M` as a set, not leftover of nm2readslx one-cut, not leftover of
nm2t2slx M freeze, not leftover of nm2slpx forall-perp, and not leftover of
two-axis opposite x-probe neighbor-read.

**Gate disposition:** PASS for the neighbor-read `t+1` versus `t+2`
reverse/face/composition reports above. FAIL / DO NOT SHIP for “the
predicate equals the named sign,” “the predicate equals the unique
singleton lock vector,” “the predicate equals R-style recovery,” “the
predicate equals nm2slpx forall-perp,” “the predicate equals nm2slx
axis-cover,” “the predicate equals two-axis opposite x-probe neighbor-read,” “the
predicate equals nm2readslx one-cut neighbor-read,” “the predicate equals
nm2t2slx M freeze,” “the predicate equals nm2simslx simultaneous,” “bits are Admissibility,” “neighbor-read fails at
`A`,” “neighbor-read fails at `D`,” “reverse neighbor-read fails,” or “face
neighbor-read fails.”

## Primary runner

The paired runner builds Euclidean `B_3(0)`, runs the two-axis same-lock
perp-step incoming-lock process, reads each x-probe's own earliest incoming
set from the record prefix at that probe's `t+1` and `t+2`, reports `M` at
each formed six-neighbor at both cuts, reports neighbor-read as
set-equality of those incoming sets, lists matching six-neighbors, reports
reverse/face at each cut, reports composition of the four bits, compares to
two-axis opposite x-probe neighbor-read and to nm2readslz, and
checks Theorems 1--3. It also checks that neighbor-read HOLDs at `A` from
matching `D` at both cuts, that no new six-neighbor of a scored probe forms
at `t+2`, that R-style recovery is a different object, that mixed sets
remain sets, that unique-letter is `UNDEFINED` at mixed neighbors, that
composition of neighbor-read bits is not leftover of nm2t2slx M freeze as a
reverse, that the construction does not sum, that a formation member from
already-recorded six-neighbor locks is not attached, and that the display
is not leftover of nm2readslx one-cut neighbor-read, of nm2slpx forall-perp,
or of nm2slx axis-cover or of nm2simslx simultaneous. No runner cache is written.
