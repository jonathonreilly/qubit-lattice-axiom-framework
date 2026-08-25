---
claim_id: two_axis_opposite_xprobe_neighbor_read_one_two_split_tplus1_tplus2_composition_reverse_face_bounded_theorem_note_2026-08-15
claim_type: bounded_theorem
claim_scope: "Neighbor-read of the 1-in 2-out split at t+1 versus t+2 on the four x-probes of the two-axis opposite seed, reverse/face at each cut, and composition, are reported. Displayed, not adopted."
upstream_dependencies:
  - minimal_axioms
runner: scripts/two_axis_opposite_xprobe_neighbor_read_one_two_split_tplus1_tplus2_composition_reverse_face_2026_08_15.py
---

# Neighbor-Read Of The 1-In 2-Out Split At t+1 Versus t+2 Reverse Face And Composition On Four Two-Axis Opposite X-Probes

> **Key terms used in this doc** are indexed A-Z at `docs/KEY_TERMINOLOGY.md`;
> each row points to the canonical source-of-truth doc.

**Date:** 2026-08-15
**Type:** bounded_theorem
**Scope:** neighbor-read of the 1-in 2-out axis split of simultaneous earliest
incoming set `M` and outgoing dual `O` at each probe's `τ1=t+1` versus
`τ2=t+2`, reverse/face from that neighbor-read at each cut, and composition
of the neighbor-read bits, on the four x-probes of the two-axis opposite
seed in `B_3(0)={n:n·n<=9}`, no global T. Same process and x-probes as
nm2axx. `M`, `O`, and split as nm2ax12x. Let `t(q)` be the formation tick of
probe `q`. Let `τ1(q)=t(q)+1` and `τ2(q)=t(q)+2`. Neighbor-read of split
HOLDs at `q,τ` if and only if split HOLDs at `q` and some formed six-neighbor
`r` has split HOLD and `Axis(M(r,τ))=Axis(M(q,τ))` and
`Axis(O(r,τ))=Axis(O(q,τ))`. Unformed `q` is `UNDEFINED`. If split fails at
`q`, neighbor-read fails, not `UNDEFINED`. Reverse HOLDs at a cut if and
only if neighbor-read HOLDs at `A` and at `B`. Face HOLDs if and only if
neighbor-read HOLDs at `C` and at `D`. Composition HOLDs if and only if
neighbor-read at `τ1` equals neighbor-read at `τ2` at `A`, `B`, `C`, and
`D`. This is the first display of the nm2sreadx fail/fail neighbor-read bits
at `t+2`. This is not leftover of nm2sreadx one-cut. This is not leftover of
nm2ax12x 1-in 2-out split without neighbor-read. This is not leftover of
nm2axx axis-cover. This is not leftover of nm2readx neighbor-read of M.
This is not leftover of nm2oreadx neighbor-read of O. This is not leftover
of signed (M, O) set equality. This is not leftover of nm2sreadz
neighbor-read of the 1-in 2-out split on z-probes. Uniqueness is not
required. Mixed remains a set. Occupancy `n` is not used. Displayed, not
adopted. Do not write into Admissibility. Do not attach L1.
**Audit-status authority:** independent audit lane only. This note authors no
audit verdict and predicts none.
**Primary runner:**
[`scripts/two_axis_opposite_xprobe_neighbor_read_one_two_split_tplus1_tplus2_composition_reverse_face_2026_08_15.py`](../scripts/two_axis_opposite_xprobe_neighbor_read_one_two_split_tplus1_tplus2_composition_reverse_face_2026_08_15.py)

No runner cache is written.

Framework input:

- [`MINIMAL_AXIOMS_2026-06-29.md`](MINIMAL_AXIOMS_2026-06-29.md) supplies
  cubic-lattice sites `Z^3` with nearest-neighbor adjacency, the one-site
  algebra `M_2(C)`, and the Record sentences that records form and that a
  present record locks exactly one admissible local possibility.

Everything after that quoted input is a finite displayed process on `B_3(0)`
and the four named x-probes. Incoming lock letters are unit nearest-neighbor
steps. `O` is the outgoing dual of those incoming sets at each per-probe
cut. Axis is the unsigned lattice direction of a signed lock. Split is cover
together with `|Axis(M)|=1`. Neighbor-read of split compares unsigned axes of
`M` and of `O` at a formed six-neighbor that also has split HOLD. Reverse
and face are scored on neighbor-read HOLD at the paired probes at each cut.
Composition is equality of the four neighbor-read bits across the two cuts.
Named signs `{+,−}` are a coarser readout and are not used. A singleton
unique lock letter is a different readout and is not used as the object.
Neighbor-read of signed `M` as sets is leftover of nm2readx and is not used.
Neighbor-read of signed `O` as sets is leftover of nm2oreadx and is not
used. Freeze of split itself is not used as the scored composition.
Occupancy of sites is not used. This display does not use occupancy. A
six-neighbor star is not the letter. O is not M.

## Machine status and trace

```yaml
actual_current_surface_status: bounded-support
target_claim_type: bounded_theorem
claim_type_reason: "Exact report of neighbor-read of the 1-in 2-out split at t+1 versus t+2 on the four x-probes of the two-axis opposite seed, fail at A and D and hold at B and C at both cuts, reverse fail and face fail at each cut, composition hold of the bits; uniqueness of incoming locks is not claimed and the bits are not adopted."
trace_class: frontier_discovery
target_claim_id: two_axis_opposite_xprobe_neighbor_read_one_two_split_tplus1_tplus2_composition_reverse_face
target_blocker_text: "display neighbor-read of the 1-in 2-out split at t+1 versus t+2 on the four x-probes of the two-axis opposite seed, reverse/face at each cut, and composition"
source_of_blocker_text: handoff
reachability_to_target: advances
artifact_role: theorem
next_trace_action: "Keep neighbor-read of the 1-in 2-out split at t+1 versus t+2 displayed; do not write the bits into Admissibility, do not reduce to nm2readx neighbor-read of M, do not reduce to nm2oreadx neighbor-read of O, do not reduce to nm2axx cover leftover, do not reduce to nm2ax12x one-cut leftover, do not reduce to nm2sreadx one-cut leftover, do not require a unique letter, and do not attach L1."
conditional_surface_status: "exact on B_3(0) for neighbor-read of the 1-in 2-out split at t+1 versus t+2 on the four x-probes of the two-axis opposite seed, reverse/face at each cut, and composition; displayed, not adopted"
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
neighbor-read of the 1-in 2-out split is scored:

```text
A = (1,0,0),  B = (1,1,1),  C = (2,0,0),  D = (1,1,0).
```

These are not the y-probes `A=(0,1,0)`, `B=(1,1,1)`, `C=(0,2,0)`,
`D=(1,1,0)`. These are not the z-probes `A=(0,0,1)`, `B=(1,1,1)`, `C=(0,0,2)`,
`D=(1,0,1)`. Probe `A` is not a seed. Same process and x-probes as nm2axx.

Lock alphabet of the displayed process: `{±e_i}` with `i` in `{1,2,3}`.

Seed: two disjoint opposite pairs recorded at formation tick 0. Origin
locks `+e_1`. Site `(0,1,0)` locks `−e_1`. Site `(0,0,1)` locks `+e_2`.
Site `(0,1,1)` locks `−e_2`. The second pair is a new seed, not a formed
child of the first pair. This seed is not the 1-axis opposite two-site seed
`{0,(0,1,0)}` with only `+e_1/−e_1`. This seed is not the perp two-site
seed `+e_1/+e_2`. This seed is not the same-lock two-site seed
`+e_1/+e_1`. This seed is not the z-symmetric three-site seed
`{0,(0,0,1),(0,0,-1)}`. This seed is not the y-symmetric three-site seed
that also records `(0,-1,0)` at tick 0. This seed is not the two-axis
same-lock seed `+e_1/+e_1` and `+e_2/+e_2`.

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

## Named neighbor-read of the 1-in 2-out split at `τ1=t+1` and `τ2=t+2`

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
this object.

Neighbor-read of split at a formed probe at the same cut:

```text
neighbor-read(q,τ) HOLDs iff split HOLDs at q and some formed 6-NN r
has split HOLD and Axis(M(r,τ))=Axis(M(q,τ)) and
Axis(O(r,τ))=Axis(O(q,τ)).
```

If `q` is unformed at `τ`, then neighbor-read is `UNDEFINED`. If split fails
at `q`, neighbor-read fails, not `UNDEFINED`. Empty match fails. Mixed
remains a set: axis equality is unsigned, not a unique-letter reduction and
not signed-set equality of `M` or of `O`. Occupancy of sites is not used.

Neighbor-read of signed `M` as sets is leftover of nm2readx: that leftover
HOLDs at every x-probe, so leftover reverse and face HOLD. Neighbor-read of
signed `O` as sets is leftover of nm2oreadx: that leftover fails at every
x-probe. Signed `(M, O)` set equality fails at `B` and at `C` because the
matching-axis neighbor recovers `M` as a set but not `O`. Freeze of split
bits is not this composition: this letter scores equality of neighbor-read
bits at `τ1` versus `τ2`.

Reverse neighbor-read holds at a cut if and only if neighbor-read HOLDs at
`A` and at `B`. Face neighbor-read holds if and only if neighbor-read HOLDs
at `C` and at `D`. Either side `UNDEFINED` is `UNDEFINED`. Else if both
sides HOLD, reverse or face HOLDs. Else fail.

Composition holds if and only if neighbor-read at `τ1` equals neighbor-read
at `τ2` at `A`, `B`, `C`, and `D`. Any `UNDEFINED` side is `UNDEFINED`. Else
if the four bits are equal across the two cuts, composition HOLDs. Else
fail.

Identifying a named sign of those locks with reverse or face is refused:
named-sign lettering lost the axis. Identifying nm2readx neighbor-read of
`M` with this reverse/face is refused: that leftover HOLDs reverse and face
because signed `M` of `A` matches `D`. Identifying nm2oreadx neighbor-read
of signed `O` with this reverse/face is refused: signed `O` fails at `B`
where this member HOLDs. Identifying signed `(M, O)` set equality with this
letter is refused: signed `O` of `B` is `{+e_2,+e_3,−e_3}` while signed `O`
of matching-axis `(1,0,1)` is `{−e_2,+e_3,−e_3}`. Identifying nm2ax12x
one-cut split with this freeze is refused: that leftover scores only
`τ=t+1` and does not ask for a matching-axis six-neighbor. Identifying
nm2sreadx one-cut with this freeze is refused: nm2sreadx scores only
`τ=t+1`. Identifying nm2axx axis-cover with this reverse/face is refused:
cover without `|Axis(M)|=1` is a different object.

## Theorem 1 — ticks, `M`, `O`, split, and neighbor-read at `τ1` and `τ2`

On this process the four x-probes form. Incoming is frozen at formation:
`M(q,t+1)=M(q,t)` at every scored probe, and remains frozen from `τ1` to
`τ2`. Outgoing dual `O` is likewise frozen from `τ1` to `τ2` at each scored
probe. Split fails at `A` and at `D`, and HOLDs at `B` and at `C`, at both
cuts. Neighbor-read of split fails at `A` and at `D`, and HOLDs at `B` and
at `C`, at both cuts. Reverse fails at both cuts. Face fails at both cuts.
Composition HOLDs. The match at `B` is `(1,0,1)` with Axis(`M`) `{e_1}` and
Axis(`O`) `{e_2, e_3}` at both cuts. The match at `C` is `(2,1,0)` with
Axis(`M`) `{e_1}` and Axis(`O`) `{e_2, e_3}` at both cuts. There is no
matching six-neighbor of `A` or of `D` at either cut.

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
O(D, τ1) = {+e_1, −e_1}
split(A, τ1) = fail
split(B, τ1) = hold
split(C, τ1) = hold
split(D, τ1) = fail
neighbor-read(A, τ1) = fail
neighbor-read(B, τ1) = hold
neighbor-read(C, τ1) = hold
neighbor-read(D, τ1) = fail
M(A, τ2) = {−e_3}
M(B, τ2) = {+e_1}
M(C, τ2) = {+e_1}
M(D, τ2) = {−e_3}
O(A, τ2) = {+e_1}
O(B, τ2) = {+e_2, +e_3, −e_3}
O(C, τ2) = {−e_2, +e_3, −e_3}
O(D, τ2) = {+e_1, −e_1}
split(A, τ2) = fail
split(B, τ2) = hold
split(C, τ2) = hold
split(D, τ2) = fail
neighbor-read(A, τ2) = fail
neighbor-read(B, τ2) = hold
neighbor-read(C, τ2) = hold
neighbor-read(D, τ2) = fail
formed 6-NN of A at τ1: (2, 0, 0) M={+e_1} O={} split=fail neighbor-read=fail, (0, 0, 0) M={+e_1} O={−e_2, −e_3} split=hold neighbor-read=hold, (1, 1, 0) M={−e_3} O={+e_1, −e_1} split=fail neighbor-read=fail, (1, -1, 0) M={+e_1} O={−e_2, −e_3} split=hold neighbor-read=fail, (1, 0, 1) M={+e_1} O={−e_2, +e_3, −e_3} split=hold neighbor-read=hold, (1, 0, -1) M={+e_1} O={−e_2, −e_3} split=hold neighbor-read=hold
formed 6-NN of B at τ1: (2, 1, 1) M=UNDEFINED O=UNDEFINED split=UNDEFINED neighbor-read=UNDEFINED, (0, 1, 1) M={−e_2} O={+e_1, −e_1, +e_3} split=hold neighbor-read=hold, (1, 2, 1) M={+e_2} O={} split=fail neighbor-read=fail, (1, 0, 1) M={+e_1} O={−e_2, +e_3, −e_3} split=hold neighbor-read=hold, (1, 1, 2) M={+e_1, +e_3} O={} split=fail neighbor-read=fail, (1, 1, 0) M={−e_3} O={−e_1} split=fail neighbor-read=fail
formed 6-NN of C at τ1: (1, 0, 0) M={−e_3} O={+e_1} split=fail neighbor-read=fail, (2, 1, 0) M={+e_1} O={+e_2, +e_3, −e_3} split=hold neighbor-read=hold, (2, -1, 0) M={−e_2, −e_3} O={} split=fail neighbor-read=fail, (2, 0, 1) M={+e_2, +e_3, −e_3} O={} split=fail neighbor-read=fail, (2, 0, -1) M={−e_3} O={} split=fail neighbor-read=fail
formed 6-NN of D at τ1: (2, 1, 0) M={+e_1} O={} split=fail neighbor-read=fail, (0, 1, 0) M={−e_1} O={+e_2, −e_3} split=hold neighbor-read=hold, (1, 2, 0) M={+e_1} O={−e_3} split=fail neighbor-read=fail, (1, 0, 0) M={−e_3} O={+e_1} split=fail neighbor-read=fail, (1, 1, 1) M={+e_1} O={+e_2, +e_3, −e_3} split=hold neighbor-read=hold, (1, 1, -1) M={+e_1} O={+e_2, −e_3} split=hold neighbor-read=hold
formed 6-NN of A at τ2: (2, 0, 0) M={+e_1} O={−e_2, +e_3, −e_3} split=hold neighbor-read=hold, (0, 0, 0) M={+e_1} O={−e_2, −e_3} split=hold neighbor-read=hold, (1, 1, 0) M={−e_3} O={+e_1, −e_1} split=fail neighbor-read=fail, (1, -1, 0) M={+e_1} O={−e_2, −e_3} split=hold neighbor-read=fail, (1, 0, 1) M={+e_1} O={−e_2, +e_3, −e_3} split=hold neighbor-read=hold, (1, 0, -1) M={+e_1} O={−e_2, −e_3} split=hold neighbor-read=hold
formed 6-NN of B at τ2: (2, 1, 1) M=UNDEFINED O=UNDEFINED split=UNDEFINED neighbor-read=UNDEFINED, (0, 1, 1) M={−e_2} O={+e_1, −e_1, +e_3} split=hold neighbor-read=hold, (1, 2, 1) M={+e_2} O={+e_1, +e_3} split=hold neighbor-read=fail, (1, 0, 1) M={+e_1} O={−e_2, +e_3, −e_3} split=hold neighbor-read=hold, (1, 1, 2) M={+e_1, +e_3} O={+e_1, +e_2} split=fail neighbor-read=fail, (1, 1, 0) M={−e_3} O={+e_1, −e_1} split=fail neighbor-read=fail
formed 6-NN of C at τ2: (1, 0, 0) M={−e_3} O={+e_1} split=fail neighbor-read=fail, (2, 1, 0) M={+e_1} O={+e_2, +e_3, −e_3} split=hold neighbor-read=hold, (2, -1, 0) M={−e_2, −e_3} O={} split=fail neighbor-read=fail, (2, 0, 1) M={+e_2, +e_3, −e_3} O={} split=fail neighbor-read=fail, (2, 0, -1) M={−e_3} O={} split=fail neighbor-read=fail
formed 6-NN of D at τ2: (2, 1, 0) M={+e_1} O={+e_2, +e_3, −e_3} split=hold neighbor-read=hold, (0, 1, 0) M={−e_1} O={+e_2, −e_3} split=hold neighbor-read=hold, (1, 2, 0) M={+e_1} O={−e_3} split=fail neighbor-read=fail, (1, 0, 0) M={−e_3} O={+e_1} split=fail neighbor-read=fail, (1, 1, 1) M={+e_1} O={+e_2, +e_3, −e_3} split=hold neighbor-read=hold, (1, 1, -1) M={+e_1} O={+e_2, −e_3} split=hold neighbor-read=hold
matching 6-NN of A at τ1: none
matching 6-NN of B at τ1: (1, 0, 1)
matching 6-NN of C at τ1: (2, 1, 0)
matching 6-NN of D at τ1: none
matching 6-NN of A at τ2: none
matching 6-NN of B at τ2: (1, 0, 1)
matching 6-NN of C at τ2: (2, 1, 0)
matching 6-NN of D at τ2: none
```

`A` is not a seed. `A` first forms at tick 2 from `(1,0,1)` by `−e_3`.
Split fails at `A` because leftover `{e_2}` is missing from
`Axis(M) union Axis(O)`. Neighbor-read(A) = fail, not `UNDEFINED`, at both
cuts. Split fails at `D` for the same leftover `{e_2}`, so
neighbor-read(D) = fail, not `UNDEFINED`, at both cuts. Site `(3,0,0)` lies
in `B_3(0)` and never forms, so it is absent from the formed six-neighbor
listing of `C`. Site `(2,1,1)` forms at tick 4, after `τ2=t(B)+2=3`, so it
stays `UNDEFINED` at both scored cuts of `B`.

Mixed remains a set: `O(B,τ)` has three outgoing steps and `O(D,τ)` has two
outgoing steps. Unique letters would assign `UNDEFINED` at mixed `O`. Here
uniqueness is not required. Neighbor-read of signed `M` HOLDs at `A` by `D`.
Neighbor-read of split fails at `A` because split itself fails. The matching
neighbor of `B` recovers `M` as `{+e_1}` but not signed `O`. Unsigned axes
agree, so neighbor-read(B) = hold at both cuts.

Formed six-neighbor listings are not frozen. At `τ2`, site `(2,0,0)` of `A`
acquires split HOLD, and site `(2,1,0)` of `D` acquires split HOLD. Those
later split HOLDs do not match Axis(`M`) and Axis(`O`) of `A` or of `D`, so
the neighbor-read bits of `A` and of `D` stay fail.

New records in `B_3(0)` between `t` and `t+1` that meet a probe's
six-neighbors can enter neighbor split at `τ1`. No new six-neighbor of any
scored probe forms at `t+2`:

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

On the 1-axis opposite two-site seed, `t(A)=3` and only two tick-0 sites.
Here the second pair is a new opposite seed and `t(A)=2`.

On the four y-probes of this same seed, split neighbor-read reverse HOLDs
and face fails. On the four z-probes, reverse HOLDs and face HOLDs. Those
probe-direction readouts are not this x-probe display.

## Theorem 2 — reverse and face at `τ1` and at `τ2`

Reverse neighbor-read holds if and only if neighbor-read HOLDs at `A` and
at `B`. Neighbor-read fails at `A` and HOLDs at `B` at both cuts. Reverse
fails at both cuts. Face neighbor-read holds if and only if neighbor-read
HOLDs at `C` and at `D`. Neighbor-read HOLDs at `C` and fails at `D` at
both cuts. Face fails at both cuts.

Reverse neighbor-read at τ1: fail
Reverse neighbor-read at τ2: fail
Face neighbor-read at τ1: fail
Face neighbor-read at τ2: fail

Both sides are defined, so this is not `UNDEFINED`. nm2readx neighbor-read
of `M` reverse HOLDs because neighbor-read of `M` HOLDs at seed-absent `A`.
Neighbor-read of signed `O` reverse fails because signed `O` fails at every
x-probe, including at `B` where this letter HOLDs. nm2axx axis-cover does
not ask for a matching-axis six-neighbor. Those leftovers are not this
display. nm2sreadx scores reverse only at `τ=t+1`; this letter also scores
`τ2`.

Reverse fails at τ1 and at τ2.
Face fails at τ1 and at τ2.

## Theorem 3 — composition of neighbor-read

Composition holds if and only if neighbor-read at `τ1` equals neighbor-read
at `τ2` at `A`, `B`, `C`, and `D`. Neighbor-read is fail, hold, hold, fail
at both cuts.

Composition of neighbor-read: hold

Displayed, not adopted. The bits are not written into Admissibility.
Do not write into Admissibility. Do not attach L1.

This is not `fail` and not `UNDEFINED`. Scoring only `τ=t+1` is leftover of
nm2sreadx one-cut. Scoring split without a matching-axis six-neighbor is
leftover of nm2ax12x. Formed six-neighbor listings change from `τ1` to `τ2`
at `A`, at `B`, and at `D`; composition of neighbor-read bits still HOLDs
because the probe bits themselves do not flip. nm2readx composition of `M`
neighbor-read bits HOLDs because hold at `A` is stable, while this reverse
fails; composition HOLD is not reverse HOLD. Z-probe split neighbor-read
composition is a different probe letter with reverse hold and face hold.
Those leftovers are not this display.

On the same seed the four y-probes give reverse hold and face fail. The
four z-probes give reverse hold and face hold. Those probe-direction
readouts are not this x-probe display.

Face fails at τ1 and at τ2.

## What this note does not claim

- It does not select a unique incoming, outgoing, or leftover lock.
- It does not reduce lock vectors to named signs `{+,−}`.
- It does not require neighbor-read sides to be singletons.
- It does not sum either set.
- It does not replace neighbor-read of split by neighbor-read of signed `M`.
- It does not replace neighbor-read of split by neighbor-read of signed `O`.
- It does not replace neighbor-read of split by nm2axx axis-cover.
- It does not replace neighbor-read of split by nm2ax12x one-cut split.
- It does not replace composition of neighbor-read bits by nm2sreadx one-cut.
- It does not treat 2-in 1-out as `UNDEFINED`.
- It does not replace `O` by `M`.
- It does not use a six-neighbor star as the letter.
- It does not wait for a global later T.
- It does not attach a formation member from already-recorded six-neighbor
  locks.
- It does not reprint the 1-axis opposite two-site seed as this member.
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
two-axis opposite four-site process, neighbor-read of the 1-in 2-out split at
`t+1` versus `t+2`, reverse/face bits at each cut, and composition are
displayed theorem-domain data.

## Exact target and obligation graph

| Obligation | Status |
|---|---|
| current Lattice / Admissibility / Record premises | quoted; no edit |
| perp-step incoming-lock process on `B_3(0)` | displayed; two-axis opposite seed `+e_1/−e_1` and `+e_2/−e_2` |
| ticks `t(A)`, `t(B)`, `t(C)`, `t(D)` | Theorem 1; `2`, `1`, `3`, `2` |
| `M` and `O` at `τ1` and `τ2` | Theorem 1; frozen equal across the two cuts |
| split at `τ1` and `τ2` | Theorem 1; fail at `A`,`D` and HOLD at `B`,`C` at both cuts |
| formed 6-NN split and axes at both cuts | Theorem 1; listings change at `τ2`; `(1,0,1)` matches `B`; `(2,1,0)` matches `C` |
| neighbor-read bit at `τ1` and `τ2` | Theorem 1; fail, hold, hold, fail at both cuts |
| reverse from neighbor-read at `τ1` and `τ2` | Theorem 2; `fail`/`fail` |
| face from neighbor-read at `τ1` and `τ2` | Theorem 2; `fail`/`fail` |
| composition of neighbor-read bits | Theorem 3; `hold` |
| compare to nm2sreadx one-cut | Theorem 1; nm2sreadx scores only `τ=t+1`; this letter also scores `τ2` and composition |
| compare to nm2ax12x one-cut | Theorem 1; nm2ax12x scores split without a matching-axis six-neighbor |
| compare to nm2readx neighbor-read of `M` | Theorem 1; nm2readx HOLDs at `A` and HOLDs reverse; this member fails at `A` because split fails |
| compare to nm2oreadx neighbor-read of signed `O` | Theorem 1; signed `O` fails at `B` where this member HOLDs |
| compare to nm2axx cover | Theorem 1; cover HOLDs without a matching-axis six-neighbor demand |
| unique incoming lock | not required |
| occupancy of sites as the letter | not used |
| named-sign `{+,−}` letter | not used; lost the axis |
| singleton unique lock-vector letter | not used as the object; mixed remains a set |
| `Z^3` sum of the lock set | not used; no aggregation |
| six-neighbor star as the letter | not used |
| leftover of nm2sreadx one-cut | not this freeze display |
| leftover of nm2ax12x 1-in 2-out split without neighbor-read | not this display |
| leftover of nm2readx neighbor-read of M | not this display |
| leftover of nm2oreadx neighbor-read of O | not this display |
| leftover of signed (M, O) set equality | not this display |
| leftover of nm2axx axis-cover | not this display |
| leftover of y-probe or z-probe split neighbor-read | not this display |
| leftover of the 1-axis opposite two-site seed | not this display |
| 2-in 1-out scored as `UNDEFINED` | refused; fail of this object |
| global later T | not used |
| neighbor-read of split as Admissibility content | not adopted |
| formation site / probability / rate | open |
| physical Record readout of the bits | open |

## Value gate (V1–V5)

| # | Answer |
|---|---|
| V1 | It answers the first-display question: neighbor-read of the 1-in 2-out split at `t+1` versus `t+2` on the four x-probes of the two-axis opposite seed, reverse/face at each cut, and composition of those bits. |
| V2 | Current main has no landed neighbor-read freeze reverse/face of the 1-in 2-out split on these four two-axis opposite x-probes. |
| V3 | Neighbor-read reports at two cuts, reverse/face bits, and composition are independently finite and exact. |
| V4 | The theorem is more than a restatement of Record because it reads unsigned axis-equality of own `M` and own `O` at a formed six-neighbor that also has 1-in 2-out split HOLD, at `t+1` versus `t+2`. |
| V5 | It is not an adopted content rule: the bits remain displayed. |

## No-go discipline gate

The negative content is narrow: the display does not write those bits into
Admissibility, does not reduce them to named signs, does not require a
unique lock, does not replace neighbor-read of split by neighbor-read of
signed `M`, does not replace neighbor-read of split by neighbor-read of
signed `O`, does not replace neighbor-read of split by nm2axx axis-cover,
does not identify this freeze with nm2sreadx one-cut, and does not identify
this freeze with nm2ax12x one-cut split. No global impossibility is
claimed.

### N1 — materially distinct routes

| Route | Attempt | Why it fails here | Marker |
|---|---|---|---|
| nm2sreadx one-cut | score neighbor-read only at `τ=t+1` | this letter also scores neighbor-read at `τ2=t+2` and composition of the bits | ATTEMPTED |
| nm2ax12x one-cut | score split only at `τ=t+1` without a matching-axis six-neighbor | neighbor-read(B) = hold and neighbor-read(C) = hold are not split bits | ATTEMPTED |
| nm2readx neighbor-read of `M` | score set-equality of signed `M` at a formed 6-NN | that leftover HOLDs at `A` by `D` and HOLDs reverse; this member fails at `A` because split fails | ATTEMPTED |
| nm2oreadx neighbor-read of signed `O` | score set-equality of signed `O` at a formed 6-NN | signed `O` fails at `B` while split neighbor-read HOLDs | ATTEMPTED |
| signed (M, O) set equality | require `M` and `O` equal as signed sets | signed `O` of `B` differs from signed `O` of `(1,0,1)` by the sign of `e_2` | ATTEMPTED |
| nm2axx axis-cover | reuse cover of `M` and `O` | cover HOLDs without a matching-axis six-neighbor; leftover `{e_2}` at `A` is cover fail and split fail | ATTEMPTED |
| 1-axis opposite two-site seed | reuse `t(A)=3` and two tick-0 sites | different seed; second pair is a new seed, not a formed child; here `t(A)=2` | ATTEMPTED |
| y-probe split neighbor-read | score the four y-probes on this seed | y-probe reverse HOLDs; this letter is the four x-probes | ATTEMPTED |
| z-probe split neighbor-read | score the four z-probes on this seed | z-probe reverse HOLDs and face HOLDs; this letter is the four x-probes | ATTEMPTED |
| unique letter | replace mixed sets by a singleton or `UNDEFINED` | mixed `O(B,τ)` remains a set; split neighbor-read still HOLDs at `B` | ATTEMPTED |
| 2-in 1-out as `UNDEFINED` | treat `|Axis(M)|=2` cover as unformed | 2-in 1-out is fail of this object, not UNDEFINED | ATTEMPTED |
| named-sign lettering | collapse `{±e_i}` to `{+,−}` | named-sign lettering lost the axis | ATTEMPTED |
| global later T | wait until `max t(A,B,C,D)` before reading | `τ1(q)=t(q)+1` and `τ2(q)=t(q)+2` are per-probe; no global T | ATTEMPTED |
| attach a formation member from already-recorded six-neighbor locks | form the probes by a neighbor-lock letter instead of perp-step | refused; not attached | ATTEMPTED |
| adopt bits into Admissibility | rewrite the local rule by split neighbor-read freeze | refused; displayed, not adopted | ATTEMPTED |

### N2 — wall independence

Missing physical adoption, missing identification of neighbor-read of split
with neighbor-read of signed `M`, missing identification of neighbor-read
of split with neighbor-read of signed `O`, missing identification of
neighbor-read of split with nm2axx axis-cover, missing identification of
this freeze with nm2sreadx one-cut or with nm2ax12x one-cut, and missing
Record identification of split neighbor-read reverse are distinct open
premises. This note claims no complete wall collection.

### N3 — hidden-condition scan

The host `B_3(0)`, two disjoint opposite pairs with locks `+e_1`, `−e_1`,
`+e_2`, and `−e_2`, perpendicular step rule, incoming-step lock, own
incoming set and own outgoing dual from records with tick `<= τ`, per-probe
`τ1=t+1` and `τ2=t+2`, unsigned axis, split as cover and `|Axis(M)|=1`,
neighbor-read as split HOLD together with unsigned axis-equality of `M` and
of `O` at a formed six-neighbor that also has split HOLD, composition as
equality of those bits, four x-probes with non-seed `A`, reverse as
neighbor-read at `A` and `B`, face as neighbor-read at `C` and `D`, and
mixed remains a set are declared. No uniqueness of incoming locks, no
signed-set equality of `M` as the scored object, no signed-set equality of
`O` as the scored object, no axis-cover as the scored object, no one-cut
neighbor-read as the scored composition, no global later T, no formation
attachment from already-recorded six-neighbor locks, and no Admissibility
rewrite are silently assumed.

### N4 — source residual matching

The current axiom memo supplies cubic sites, `M_2(C)`,
content-conditional-on-formation, and unreadable absence. The residual that
formation site, probability, and rate remain unsupplied is unchanged. The
neighbor-read reverse fail, face fail, and composition hold reports do not
close that residual.

### N5 — resolution and rhetoric audit

| Resolution | Executed | Not claimed |
|---|---|---|
| per element | each unsigned lattice axis of `M` and of `O` at a probe and at formed 6-NN | no continuum alphabet |
| per site | `A,B,C,D` x-probes on `B_3(0)` only | no other cubic sites |
| per mode | no mode calculation | no spectral exhaustion |
| per block | four neighbor-read reports at t+1 and t+2 plus reverse/face/composition | no adopted content law |
| lattice wide | checked and not executed | no lattice-wide lettering rule |

### N6 — live partial-closure paths

Live routes include a later Record content map for split neighbor-read
reverse/face, a formation-rate rule, and a physical selector among matching
six-neighbors. None is taken here.

### N7 — hostile steelman

**Steelman:** Neighbor-read of the 1-in 2-out split freeze on x-probes is
leftover of nm2sreadx because the `t+1` bits already fail reverse and face;
leftover of nm2ax12x because split already fails reverse and face; leftover
of nm2readx because some neighbor already carries a related incoming letter;
leftover of neighbor-read of signed `O` because reverse already fails; leftover
of nm2axx cover with the matching-neighbor demand dropped; and uniqueness of
`M` already answers the match.

**Answer:** nm2sreadx scores only `τ=t+1`. This letter also scores `τ2` and
composition of the four neighbor-read bits. Formed six-neighbor listings
change at `τ2`; the probe bits do not. nm2ax12x scores split without a
matching-axis six-neighbor; neighbor-read(B) = hold is not a split bit.
nm2readx HOLDs at `A` because signed `M` of `D` equals `{−e_3}`; this member
fails at `A` because split fails. Signed `O` of `B` is not signed `O` of
`(1,0,1)`; neighbor-read of signed `O` fails at `B` while this member HOLDs.
nm2axx cover does not ask for a matching-axis six-neighbor. Mixed `O(B,τ)`
remains a set; uniqueness is not required. Reverse neighbor-read is HOLD iff
neighbor-read of split at `A` and at `B`, not leftover of nm2readx and not
leftover of signed-`O` neighbor-read.

### N8 — cross-cycle echo

nm2sreadx reported neighbor-read of the 1-in 2-out split at `τ=t+1` on these
four x-probes with reverse fail and face fail. nm2ax12x reported 1-in 2-out
split of `M` and `O` at `τ=t+1` on these four x-probes with reverse fail and
face fail. nm2axx reported axis-cover on the same probes. nm2readx reported
neighbor-read of `M` at `τ=t+1` with HOLD at `A` and reverse hold. Two-axis
opposite z-probes report split-neighbor-read reverse hold and face hold.
Two-axis opposite y-probes report reverse hold and face fail. This note is
not those displays: it reports neighbor-read of the 1-in 2-out split at
`τ1=t+1` versus `τ2=t+2` on two disjoint opposite pairs with x-probes,
fail at `A`,`D` and HOLD at `B`,`C` at both cuts, reverse fail and face fail
at each cut, and composition hold. HOLD iff split HOLDs and some formed 6-NN
has split HOLD with matching Axis(`M`) and Axis(`O`), not leftover of
nm2sreadx one-cut, not leftover of nm2ax12x one-cut split, not leftover of
nm2readx neighbor-read of `M`, and not leftover of neighbor-read of signed
`O`.

**Gate disposition:** PASS for the neighbor-read of split `t+1` versus
`t+2` reverse/face/composition reports above. FAIL / DO NOT SHIP for “the
predicate equals the named sign,” “the predicate equals the unique
singleton lock vector,” “the predicate equals neighbor-read of signed `M`,”
“the predicate equals neighbor-read of signed `O`,” “the predicate equals
nm2axx axis-cover,” “the predicate equals nm2sreadx one-cut,” “the
predicate equals nm2ax12x one-cut split,” “bits are Admissibility,”
“neighbor-read HOLDs at `A`,” “neighbor-read HOLDs at `D`,” “reverse
neighbor-read HOLDs,” or “face neighbor-read HOLDs.”

## Primary runner

The paired runner builds Euclidean `B_3(0)`, runs the two-axis opposite
perp-step incoming-lock process, reads each x-probe's own earliest incoming
set and own outgoing dual from the record prefix at that probe's `t+1` and
`t+2`, reports split of those pairs, reports split and axes at each formed
six-neighbor at both cuts, reports neighbor-read as split HOLD together with
unsigned axis-equality of `M` and of `O` at a formed six-neighbor that also
has split HOLD, lists matching six-neighbors, reports reverse/face at each
cut, reports composition of the four bits, compares to neighbor-read of
signed `M` and of signed `O` and to same-lock and 1-axis leftovers, and
checks Theorems 1--3. It also checks that neighbor-read fails at `A` and at
`D` at both cuts, that mixed sets remain sets, that unique-letter is
`UNDEFINED` at mixed `O`, that composition of neighbor-read bits is not
leftover of nm2sreadx one-cut as a reverse, that the construction does not
sum, that a formation member from already-recorded six-neighbor locks is not
attached, and that the display is not leftover of nm2ax12x one-cut split, of
nm2readx neighbor-read of `M`, or of nm2axx axis-cover. No runner cache is
written.
