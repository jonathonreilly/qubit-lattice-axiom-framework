---
claim_id: two_axis_same_lock_zprobe_neighbor_read_one_two_split_tplus1_tplus2_composition_reverse_face_bounded_theorem_note_2026-08-15
claim_type: bounded_theorem
claim_scope: "Neighbor-read of the 1-in 2-out split at t+1 versus t+2 on the four z-probes of the two-axis same-lock seed, reverse/face at each cut, and composition, are reported. Displayed, not adopted."
upstream_dependencies:
  - minimal_axioms
runner: scripts/two_axis_same_lock_zprobe_neighbor_read_one_two_split_tplus1_tplus2_composition_reverse_face_2026_08_15.py
---

# Neighbor-Read Of The 1-In 2-Out Split At t+1 Versus t+2 Reverse Face And Composition On Four Two-Axis Same-Lock Z-Probes

> **Key terms used in this doc** are indexed A-Z at `docs/KEY_TERMINOLOGY.md`;
> each row points to the canonical source-of-truth doc.

**Date:** 2026-08-15
**Type:** bounded_theorem
**Scope:** Neighbor-read of the 1-in 2-out split at t+1 versus t+2 on the four z-probes of the two-axis same-lock seed, reverse/face at each cut, and composition, are reported. Displayed, not adopted.
**Audit-status authority:** independent audit lane only. This note authors no
audit verdict and predicts none.
**Primary runner:**
[`scripts/two_axis_same_lock_zprobe_neighbor_read_one_two_split_tplus1_tplus2_composition_reverse_face_2026_08_15.py`](../scripts/two_axis_same_lock_zprobe_neighbor_read_one_two_split_tplus1_tplus2_composition_reverse_face_2026_08_15.py)

No runner cache is written.

Framework input:

- [`MINIMAL_AXIOMS_2026-06-29.md`](MINIMAL_AXIOMS_2026-06-29.md) supplies
  cubic-lattice sites `Z^3` with nearest-neighbor adjacency, the one-site
  algebra `M_2(C)`, and the Record sentences that records form and that a
  present record locks exactly one admissible local possibility.

Everything after that quoted input is a finite displayed process on `B_3(0)`
and the four named z-probes. Same process and z-probes as nm2slz. Incoming
lock letters are unit nearest-neighbor steps. `O` is the outgoing dual of
those incoming sets at each per-probe cut. Axis is the unsigned lattice
direction of a signed lock. Split is cover together with `|Axis(M)|=1`.
Neighbor-read of split compares unsigned axes of `M` and of `O` at a formed
six-neighbor that also has split HOLD, as nm2sreadslz, at each cut. Reverse
and face are scored on neighbor-read HOLD at the paired probes at each cut.
Composition is equality of the four neighbor-read bits across the two cuts.
Named signs `{+,−}` are a coarser readout and are not used. A singleton
unique lock letter is a different readout and is not used as the object.
Neighbor-read of signed `M` as sets is leftover of nm2readslz and is not used.
Neighbor-read of signed `O` as sets is leftover of nm2oreadslz and is not used.
Freeze of split itself is leftover of nm2splt2slz and is not used as the
scored composition. Occupancy of sites is not used. This display does not
use occupancy. A six-neighbor star is not the letter. O is not M.

This is the first display of the nm2sreadslz neighbor-read bits at `t+2`.
This is not leftover of nm2sreadslz one-cut neighbor-read at `t+1` only.
This is not leftover of nm2sl12z 1-in 2-out split without neighbor-read.
This is not leftover of nm2splt2slz split composition of `t` versus `t+1`.
This is not leftover of nm2readslz neighbor-read of M. This is not leftover
of nm2oreadslz neighbor-read of O. This is not leftover of signed (M, O) set
equality. This is not leftover of nm2sreadt2z neighbor-read composition on
opposite z. Uniqueness is not required. Mixed remains a set. Displayed, not
adopted. Do not write into Admissibility. Do not attach L1.

## Machine status and trace

```yaml
actual_current_surface_status: bounded-support
target_claim_type: bounded_theorem
claim_type_reason: "Exact report of neighbor-read of the 1-in 2-out split at t+1 versus t+2 on the four z-probes of the two-axis same-lock seed, fail at A and HOLD at B,C,D at both cuts, reverse fail and face hold at each cut, composition hold of the bits; uniqueness of incoming locks is not claimed and the bits are not adopted."
trace_class: frontier_discovery
target_claim_id: two_axis_same_lock_zprobe_neighbor_read_one_two_split_tplus1_tplus2_composition_reverse_face
target_blocker_text: "display neighbor-read of the 1-in 2-out split at t+1 versus t+2 on the four z-probes of the two-axis same-lock seed, reverse/face at each cut, and composition"
source_of_blocker_text: handoff
reachability_to_target: advances
artifact_role: theorem
next_trace_action: "Keep neighbor-read of the 1-in 2-out split at t+1 versus t+2 displayed; do not write the bits into Admissibility, do not reduce to nm2sreadslz one-cut, do not reduce to nm2readslz neighbor-read of M, do not reduce to nm2oreadslz neighbor-read of O, do not reduce to nm2sl12z split without neighbor-read, do not reduce to nm2splt2slz split freeze, do not replace the display by nm2sreadt2z opposite-z composition, do not require a unique letter, and do not attach L1."
conditional_surface_status: "exact on B_3(0) for neighbor-read of the 1-in 2-out split at t+1 versus t+2 on the four z-probes of the two-axis same-lock seed, reverse/face at each cut, and composition; displayed, not adopted"
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
origin, `B_3(0)={n:n·n<=9}`,

```text
B_3(0) = { n in Z^3 : n·n <= 9 }.
```

No larger host is used. The four z-probes are the only sites whose
neighbor-read of the 1-in 2-out split is scored:

```text
A = (0,0,1),  B = (1,1,1),  C = (0,0,2),  D = (1,0,1).
```

These are not the y-probes `A=(0,1,0)`, `B=(1,1,1)`, `C=(0,2,0)`,
`D=(1,1,0)`. These are not the x-probes `A=(1,0,0)`, `B=(1,1,1)`, `C=(2,0,0)`,
`D=(1,1,0)`. `A` is a seed of the second same-lock pair. Same process and
z-probes as nm2slz.

Lock alphabet of the displayed process: `{±e_i}` with `i` in `{1,2,3}`.

Seed: two disjoint same-lock pairs recorded at formation tick 0. Origin
locks `+e_1`. Site `(0,1,0)` locks `+e_1`. Site `(0,0,1)` locks `+e_2`.
Site `(0,1,1)` locks `+e_2`. Neither pair is opposite. The second pair is a
new seed, not a formed child of the first pair. This seed is not the 1-axis
opposite two-site seed `{0,(0,1,0)}` with only `+e_1/−e_1`. This seed is not
the perp two-site seed `+e_1/+e_2`. This seed is not the same-lock two-site
seed `+e_1/+e_1`. This seed is not the z-symmetric three-site seed
`{0,(0,0,1),(0,0,-1)}`. This seed is not the y-symmetric three-site seed
that also records `(0,-1,0)` at tick 0. This seed is not the two-axis
opposite seed `+e_1/−e_1` and `+e_2/−e_2`.

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

Let `t(q)` be the formation tick of z-probe `q` when that tick is defined in
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

Neighbor-read of split at a formed probe at the same cut, as nm2sreadslz:

```text
neighbor-read(q,τ) HOLDs iff split HOLDs at q and some formed 6-NN r
has split HOLD and Axis(M(r,τ))=Axis(M(q,τ)) and
Axis(O(r,τ))=Axis(O(q,τ)).
```

If `q` is unformed at `τ`, then neighbor-read is `UNDEFINED`. If split fails
at `q`, neighbor-read fails, not `UNDEFINED`. Empty match fails. Mixed
remains a set: axis equality is unsigned, not a unique-letter reduction and
not signed-set equality of `M` or of `O`. Occupancy of sites is not used.

Neighbor-read of signed `M` as sets is leftover of nm2readslz: that leftover
HOLDs at seed `A` because the partner seed also locks `+e_2`. Neighbor-read
of signed `O` as sets fails at every z-probe. Freeze of split bits across
`t` and `t+1` is leftover of nm2splt2slz: that leftover scores
`split(τ0)=split(τ1)`, not neighbor-read bits at `τ1` versus `τ2`.

Reverse neighbor-read holds at a cut if and only if neighbor-read HOLDs at
`A` and at `B`. Face neighbor-read holds if and only if neighbor-read HOLDs
at `C` and at `D`. Either side `UNDEFINED` is `UNDEFINED`. Else if both
sides HOLD, reverse or face HOLDs. Else fail.

Composition holds if and only if neighbor-read at `τ1` equals neighbor-read
at `τ2` at `A`, `B`, `C`, and `D`. Any `UNDEFINED` side is `UNDEFINED`. Else
if the four bits are equal across the two cuts, composition HOLDs. Else
fail.

## Theorem 1 — ticks, `M`, `O`, split, and neighbor-read at `τ1` and `τ2`

On this process the four z-probes form. Incoming is frozen at formation:
`M(q,t+1)=M(q,t)` at every scored probe, and remains frozen from `τ1` to
`τ2`. Outgoing dual `O` is likewise frozen from `τ1` to `τ2` at each scored
probe. Split fails at `A` and HOLDs at `B`, at `C`, and at `D` at both cuts.
Neighbor-read of split fails at `A` and HOLDs at `B`, at `C`, and at `D` at
both cuts. Reverse fails at both cuts. Face HOLDs at both cuts. Composition
HOLDs. Probe `A` is a seed of the second same-lock pair. Both `A` and
`(0,1,1)` lock `+e_2`, so `O(A,τ)` contains `+e_2`. Then
`Axis(M)(A,τ)={e_2}` meets `Axis(O)(A,τ)={e_1,e_2,e_3}`, cover fails, and
split(A) = fail. Neighbor-read therefore fails at `A`, not `UNDEFINED`, at
both cuts. Site `(0,1,1)` itself has split HOLD at `A`'s `τ1` and at `A`'s
`τ2`, with `M={+e_2}` and `O={+e_1,−e_1,+e_3}`, but neighbor-read at that
site fails: no formed six-neighbor recovers the same 1-in 2-out axes. The
match at `B` is `D=(1,0,1)` with Axis(`M`) `{e_1}` and Axis(`O`)
`{e_2, e_3}` at both cuts. The match at `C` is `(0,1,2)` with Axis(`M`)
`{e_3}` and Axis(`O`) `{e_1, e_2}` at both cuts. The match at `D` is
`B=(1,1,1)` with Axis(`M`) `{e_1}` and Axis(`O`) `{e_2, e_3}` at both cuts.

```text
t(A)=0
t(B)=1
t(C)=1
t(D)=1
M(A, τ1) = {+e_2}
M(B, τ1) = {+e_1}
M(C, τ1) = {+e_3}
M(D, τ1) = {+e_1}
O(A, τ1) = {+e_1, −e_1, +e_2, +e_3}
O(B, τ1) = {+e_2, +e_3, −e_3}
O(C, τ1) = {+e_1, −e_1, −e_2}
O(D, τ1) = {−e_2, +e_3, −e_3}
split(A, τ1) = fail
split(B, τ1) = hold
split(C, τ1) = hold
split(D, τ1) = hold
neighbor-read(A, τ1) = fail
neighbor-read(B, τ1) = hold
neighbor-read(C, τ1) = hold
neighbor-read(D, τ1) = hold
M(A, τ2) = {+e_2}
M(B, τ2) = {+e_1}
M(C, τ2) = {+e_3}
M(D, τ2) = {+e_1}
O(A, τ2) = {+e_1, −e_1, +e_2, +e_3}
O(B, τ2) = {+e_2, +e_3, −e_3}
O(C, τ2) = {+e_1, −e_1, −e_2}
O(D, τ2) = {−e_2, +e_3, −e_3}
split(A, τ2) = fail
split(B, τ2) = hold
split(C, τ2) = hold
split(D, τ2) = hold
neighbor-read(A, τ2) = fail
neighbor-read(B, τ2) = hold
neighbor-read(C, τ2) = hold
neighbor-read(D, τ2) = hold
formed 6-NN of A at τ1: (1, 0, 1) M={+e_1} O={} split=fail neighbor-read=fail, (-1, 0, 1) M={−e_1} O={} split=fail neighbor-read=fail, (0, 1, 1) M={+e_2} O={+e_1, −e_1, +e_3} split=hold neighbor-read=fail, (0, -1, 1) M=UNDEFINED O=UNDEFINED split=UNDEFINED neighbor-read=UNDEFINED, (0, 0, 2) M={+e_3} O={} split=fail neighbor-read=fail, (0, 0, 0) M={+e_1} O={−e_2, −e_3} split=hold neighbor-read=hold
formed 6-NN of B at τ1: (2, 1, 1) M=UNDEFINED O=UNDEFINED split=UNDEFINED neighbor-read=UNDEFINED, (0, 1, 1) M={+e_2} O={+e_1, −e_1, +e_3} split=hold neighbor-read=fail, (1, 2, 1) M={+e_2} O={} split=fail neighbor-read=fail, (1, 0, 1) M={+e_1} O={−e_2, +e_3, −e_3} split=hold neighbor-read=hold, (1, 1, 2) M={+e_1, +e_3} O={} split=fail neighbor-read=fail, (1, 1, 0) M={−e_3} O={} split=fail neighbor-read=fail
formed 6-NN of C at τ1: (1, 0, 2) M={+e_1, +e_3} O={} split=fail neighbor-read=fail, (-1, 0, 2) M={−e_1, +e_3} O={} split=fail neighbor-read=fail, (0, 1, 2) M={+e_3} O={+e_1, −e_1, +e_2} split=hold neighbor-read=hold, (0, -1, 2) M={−e_2} O={} split=fail neighbor-read=fail, (0, 0, 1) M={+e_2} O={+e_1, −e_1, +e_2, +e_3} split=fail neighbor-read=fail
formed 6-NN of D at τ1: (2, 0, 1) M=UNDEFINED O=UNDEFINED split=UNDEFINED neighbor-read=UNDEFINED, (0, 0, 1) M={+e_2} O={+e_1, −e_1, +e_2, +e_3} split=fail neighbor-read=fail, (1, 1, 1) M={+e_1} O={+e_2, +e_3, −e_3} split=hold neighbor-read=hold, (1, -1, 1) M={−e_2} O={} split=fail neighbor-read=fail, (1, 0, 2) M={+e_1, +e_3} O={} split=fail neighbor-read=fail, (1, 0, 0) M={−e_3} O={} split=fail neighbor-read=fail
formed 6-NN of A at τ2: (1, 0, 1) M={+e_1} O={−e_2, +e_3, −e_3} split=hold neighbor-read=hold, (-1, 0, 1) M={−e_1} O={−e_2, +e_3, −e_3} split=hold neighbor-read=hold, (0, 1, 1) M={+e_2} O={+e_1, −e_1, +e_3} split=hold neighbor-read=fail, (0, -1, 1) M={+e_3} O={+e_2} split=fail neighbor-read=fail, (0, 0, 2) M={+e_3} O={+e_1, −e_1, −e_2} split=hold neighbor-read=hold, (0, 0, 0) M={+e_1} O={−e_2, −e_3} split=hold neighbor-read=hold
formed 6-NN of B at τ2: (2, 1, 1) M=UNDEFINED O=UNDEFINED split=UNDEFINED neighbor-read=UNDEFINED, (0, 1, 1) M={+e_2} O={+e_1, −e_1, +e_3} split=hold neighbor-read=fail, (1, 2, 1) M={+e_2} O={+e_1, +e_3} split=hold neighbor-read=fail, (1, 0, 1) M={+e_1} O={−e_2, +e_3, −e_3} split=hold neighbor-read=hold, (1, 1, 2) M={+e_1, +e_3} O={+e_1, +e_2} split=fail neighbor-read=fail, (1, 1, 0) M={−e_3} O={+e_1} split=fail neighbor-read=fail
formed 6-NN of C at τ2: (1, 0, 2) M={+e_1, +e_3} O={+e_1, −e_2} split=fail neighbor-read=fail, (-1, 0, 2) M={−e_1, +e_3} O={−e_1, −e_2} split=fail neighbor-read=fail, (0, 1, 2) M={+e_3} O={+e_1, −e_1, +e_2} split=hold neighbor-read=hold, (0, -1, 2) M={−e_2} O={+e_1, −e_1} split=fail neighbor-read=fail, (0, 0, 1) M={+e_2} O={+e_1, −e_1, +e_2, +e_3} split=fail neighbor-read=fail
formed 6-NN of D at τ2: (2, 0, 1) M=UNDEFINED O=UNDEFINED split=UNDEFINED neighbor-read=UNDEFINED, (0, 0, 1) M={+e_2} O={+e_1, −e_1, +e_2, +e_3} split=fail neighbor-read=fail, (1, 1, 1) M={+e_1} O={+e_2, +e_3, −e_3} split=hold neighbor-read=hold, (1, -1, 1) M={−e_2} O={+e_1, +e_3} split=hold neighbor-read=fail, (1, 0, 2) M={+e_1, +e_3} O={+e_1, −e_2} split=fail neighbor-read=fail, (1, 0, 0) M={−e_3} O={+e_1} split=fail neighbor-read=fail
matching 6-NN of A at τ1: none
matching 6-NN of B at τ1: (1, 0, 1)
matching 6-NN of C at τ1: (0, 1, 2)
matching 6-NN of D at τ1: (1, 1, 1)
matching 6-NN of A at τ2: none
matching 6-NN of B at τ2: (1, 0, 1)
matching 6-NN of C at τ2: (0, 1, 2)
matching 6-NN of D at τ2: (1, 1, 1)
```

`A` is a seed at tick 0 with seed letter `+e_2`. Mixed remains a set:
`O(A,τ1)` has four outgoing steps and `O(D,τ1)` has three outgoing steps.
Unique letters would assign `UNDEFINED` at mixed `O`. Here uniqueness is
not required. At `A`, neighbor-read of signed `M` HOLDs because the partner
seed locks `{+e_2}`, equal as a set to `{+e_2}`. Neighbor-read of split
fails because split itself fails at `A`. Unformed six-neighbors remain
`UNDEFINED` at the earlier cut and do not match. `(0,-1,1)` of `A` forms at
tick 2, so it is `UNDEFINED` at `τ1=1` and formed at `τ2=2`, where its
split fails. `(2,1,1)` of `B` forms after `τ2=t(B)+2=3`, so it stays
`UNDEFINED` at both scored cuts.

New records in `B_3(0)` between `t` and `t+1` that meet a probe's
six-neighbors can enter neighbor split at `τ1`. Site `(0,1,1)` is a seed,
so it is not a new 6-NN of `A`. One new six-neighbor of `A` forms at
`t+2`; it does not match Axis(`M`) and Axis(`O`) of `A`, and `A` itself
still fails split. No new six-neighbor of `B`, of `C`, or of `D` forms at
`t+2`. Formed six-neighbor split bits can change between the cuts — `D`
gains split HOLD at `A`'s `τ2`, and `(1,-1,1)` gains split HOLD at `D`'s
`τ2` — while the four probe neighbor-read bits stay equal. That is why
composition of neighbor-read is not leftover of listing formed-neighbor
split:

```text
new 6-NN of A at t(A)+1: (1, 0, 1), (-1, 0, 1), (0, 0, 2)
new 6-NN of B at t(B)+1: (1, 2, 1), (1, 1, 2), (1, 1, 0)
new 6-NN of C at t(C)+1: (1, 0, 2), (-1, 0, 2), (0, -1, 2)
new 6-NN of D at t(D)+1: (1, -1, 1), (1, 0, 2), (1, 0, 0)
new 6-NN of A at t(A)+2: (0, -1, 1)
new 6-NN of B at t(B)+2: none
new 6-NN of C at t(C)+2: none
new 6-NN of D at t(D)+2: none
```

On the two-axis opposite seed with the same z-probes, split neighbor-read
HOLDs at seed `A` and HOLDs reverse. Here the partner seed locks `+e_2`,
`O(A)` contains that same axis, split fails at `A`, and reverse fails.
That leftover is not this display.

On the 1-axis opposite two-site seed, `t(A)=1`, `t(C)=4`, split fails at
`C` from 2-in 1-out, and split-neighbor-read face fails. Here the second
pair is a new same-lock seed, `t(A)=0`, reverse fails, and face HOLDs.

On the four y-probes of this same seed, split neighbor-read reverse HOLDs
and face fails. On the four x-probes, reverse fails and face fails. Those
probe-direction readouts are not this z-probe display.

## Theorem 2 — reverse and face at `τ1` and at `τ2`

Reverse neighbor-read holds if and only if neighbor-read HOLDs at `A` and
at `B`. Neighbor-read fails at `A` and HOLDs at `B` at both cuts. Reverse
fails at both cuts. Face neighbor-read holds if and only if neighbor-read
HOLDs at `C` and at `D`. Both neighbor-reads HOLD at both cuts. Face HOLDs
at both cuts.

Reverse neighbor-read at τ1: fail
Reverse neighbor-read at τ2: fail
Face neighbor-read at τ1: hold
Face neighbor-read at τ2: hold

Both sides are defined, so this is not `UNDEFINED`. nm2readslz neighbor-read
of `M` reverse HOLDs because neighbor-read of `M` HOLDs at seed `A`.
Neighbor-read of signed `O` reverse fails and face fails. Two-axis opposite
z-probe split neighbor-read reverse HOLDs. nm2sl12z scores reverse of split
without neighbor-read; those pair-read bits agree here, but at seed
`(0,1,1)` split HOLDs while neighbor-read fails. Those leftovers are not
this display. nm2sreadslz scores reverse only at `τ=t+1`; this letter also
scores `τ2`.

Reverse fails at τ1 and at τ2.
Face holds at τ1 and at τ2.

## Theorem 3 — composition of neighbor-read

Composition holds if and only if neighbor-read at `τ1` equals neighbor-read
at `τ2` at `A`, `B`, `C`, and `D`. Neighbor-read fails at `A` and HOLDs at
`B`, at `C`, and at `D` at both cuts.

Composition of neighbor-read: hold

Displayed, not adopted. The bits are not written into Admissibility.
Do not write into Admissibility. Do not attach L1.

This is not `fail` and not `UNDEFINED`. Scoring only `τ=t+1` is leftover of
nm2sreadslz one-cut. Scoring `split(t)=split(t+1)` is leftover of
nm2splt2slz split composition: split also fails at `A` and HOLDs at `B,C,D`
here at both scored cuts, but composition of split is not composition of
neighbor-read bits. nm2readslz composition of `M` neighbor-read bits HOLDs
because HOLD at `A` is stable, while reverse HOLDs; composition HOLD is not
reverse HOLD. Opposite-z nm2sreadt2z composition HOLDs with reverse HOLD.
Y-probe split neighbor-read composition is a different probe letter with
face fail. Those leftovers are not this display.

On the same seed the four y-probes give reverse hold and face fail. The
four x-probes give reverse fail and face fail. Those probe-direction
readouts are not this z-probe display.

Face holds at τ1 and at τ2.

## What this note does not claim

- It does not select a unique incoming, outgoing, or leftover lock.
- It does not reduce lock vectors to named signs `{+,−}`.
- It does not require neighbor-read sides to be singletons.
- It does not sum either set.
- It does not replace neighbor-read of split by neighbor-read of signed `M`.
- It does not replace neighbor-read of split by neighbor-read of signed `O`.
- It does not replace neighbor-read of split by nm2sl12z split without
  neighbor-read.
- It does not replace neighbor-read of split by nm2sreadslz one-cut.
- It does not replace composition of neighbor-read bits by nm2splt2slz split
  freeze.
- It does not replace neighbor-read of split by nm2sreadt2z opposite-z
  composition.
- It does not treat 2-in 1-out as `UNDEFINED`.
- It does not replace `O` by `M`.
- It does not use a six-neighbor star as the letter.
- It does not wait for a global later T.
- It does not attach a formation member from already-recorded six-neighbor
  locks.
- It does not reprint the 1-axis opposite two-site seed as this member.
- It does not score the y-probes or the x-probes as this letter.
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
two-axis same-lock four-site process, neighbor-read of the 1-in 2-out split at
`t+1` versus `t+2`, reverse/face bits at each cut, and composition are
displayed theorem-domain data.

## Exact target and obligation graph

| Obligation | Status |
|---|---|
| current Lattice / Admissibility / Record premises | quoted; no edit |
| perp-step incoming-lock process on `B_3(0)` | displayed; two-axis same-lock seed `+e_1/+e_1` and `+e_2/+e_2` |
| ticks `t(A)`, `t(B)`, `t(C)`, `t(D)` | Theorem 1; `0`, `1`, `1`, `1` |
| `M` and `O` at `τ1` and `τ2` | Theorem 1; frozen equal across the two cuts |
| split at `τ1` and `τ2` | Theorem 1; fail at `A`, HOLD at `B`,`C`,`D` at both cuts |
| formed 6-NN split and axes at both cuts | Theorem 1; no match at `A`; `D` matches `B` |
| neighbor-read bit at `τ1` and `τ2` | Theorem 1; fail at `A`, HOLD at `B`,`C`,`D` at both cuts |
| reverse from neighbor-read at `τ1` and `τ2` | Theorem 2; `fail`/`fail` |
| face from neighbor-read at `τ1` and `τ2` | Theorem 2; `hold`/`hold` |
| composition of neighbor-read bits | Theorem 3; `hold` |
| compare to nm2sreadslz one-cut | Theorem 1; nm2sreadslz scores only `τ=t+1`; this letter also scores `τ2` and composition |
| compare to nm2splt2slz split freeze | Theorem 3; split fails at `A` here too; composition is of neighbor-read bits, not of split bits at `t` versus `t+1` |
| compare to nm2readslz neighbor-read of `M` | Theorem 1; nm2readslz HOLDs at seed `A` and HOLDs reverse; this member fails at `A` because split fails |
| compare to nm2oreadslz neighbor-read of `O` | Theorem 1; signed `O` fails at `B`,`C`,`D`; Axis(`O`) of `B` matches `D` |
| compare to nm2sl12z split without neighbor-read | Theorem 1; split HOLDs at `(0,1,1)` while neighbor-read fails there |
| compare to nm2sreadt2z opposite-z composition | Theorem 1; opposite z HOLDs at seed `A` and HOLDs reverse |
| unique incoming lock | not required |
| occupancy of sites as the letter | not used |
| named-sign `{+,−}` letter | not used; lost the axis |
| singleton unique lock-vector letter | not used as the object; mixed remains a set |
| `Z^3` sum of the lock set | not used; no aggregation |
| six-neighbor star as the letter | not used |
| leftover of nm2sreadslz one-cut | not this freeze display |
| leftover of nm2splt2slz split composition | not this composition |
| leftover of nm2readslz neighbor-read of M | not this display |
| leftover of nm2oreadslz neighbor-read of O | not this display |
| leftover of signed (M, O) set equality | not this display |
| leftover of nm2sl12z 1-in 2-out split without neighbor-read | not this display |
| leftover of nm2sreadt2z | not this display |
| leftover of y-probe or x-probe split neighbor-read | not this display |
| leftover of the 1-axis opposite two-site seed | not this display |
| 2-in 1-out scored as `UNDEFINED` | refused; fail of this object |
| global later T | not used |
| neighbor-read of split as Admissibility content | not adopted |
| formation site / probability / rate | open |
| physical Record readout of the bits | open |

## Value gate (V1–V5)

| # | Answer |
|---|---|
| V1 | It answers the first-display question: neighbor-read of the 1-in 2-out split at `t+1` versus `t+2` on the four z-probes of the two-axis same-lock seed, reverse/face at each cut, and composition of those bits. |
| V2 | Current main has no landed neighbor-read freeze reverse/face of the 1-in 2-out split on these four two-axis same-lock z-probes. |
| V3 | Neighbor-read reports at two cuts, reverse/face bits, and composition are independently finite and exact. |
| V4 | The theorem is more than a restatement of Record because it reads unsigned axis-equality of own `M` and own `O` at a formed six-neighbor that also has 1-in 2-out split HOLD, at `t+1` versus `t+2`. |
| V5 | It is not an adopted content rule: the bits remain displayed. |

## No-go discipline gate

The negative content is narrow: the display does not write those bits into
Admissibility, does not reduce them to named signs, does not require a
unique lock, does not replace neighbor-read of split by neighbor-read of
signed `M`, does not replace neighbor-read of split by neighbor-read of
signed `O`, does not replace neighbor-read of split by nm2sl12z split
without neighbor-read, does not identify this display with nm2sreadt2z
opposite-z composition, does not identify it with nm2sreadslz one-cut, and
does not identify composition with nm2splt2slz split freeze. No global
impossibility is claimed.

### N1 — materially distinct routes

| Route | Attempt | Why it fails here | Marker |
|---|---|---|---|
| nm2sreadslz one-cut | score neighbor-read only at `τ=t+1` | this letter also scores neighbor-read at `τ2=t+2` and composition of the bits | ATTEMPTED |
| nm2splt2slz split freeze | score `split(t)=split(t+1)` | split fails at `A` here too; composition is equality of neighbor-read bits at `t+1` versus `t+2`, not of split bits at `t` versus `t+1` | ATTEMPTED |
| nm2readslz neighbor-read of M | score set-equality of signed `M` at a formed 6-NN | that leftover HOLDs at seed `A` because partner `M={+e_2}` equals `M(A)`; this member fails at `A` because split fails | ATTEMPTED |
| nm2oreadslz neighbor-read of O | score set-equality of signed `O` at a formed 6-NN | signed `O` of `B` is `{+e_2,+e_3,−e_3}` while `D` has `{−e_2,+e_3,−e_3}`; signed `O` fails face while split neighbor-read HOLDs face | ATTEMPTED |
| signed (M, O) set equality | require `M` and `O` equal as signed sets | signed pair fails at every z-probe; Axis(`O`) of `B` matches `D` | ATTEMPTED |
| nm2sl12z 1-in 2-out split without neighbor-read | reuse split of `M` and `O` | split HOLDs at `(0,1,1)` while neighbor-read fails there | ATTEMPTED |
| nm2sreadt2z | reuse opposite seed `+e_1/−e_1` and `+e_2/−e_2` on z-probes | that leftover HOLDs at seed `A` and HOLDs reverse; here reverse fails from same-lock `O(A)` containing `+e_2` | ATTEMPTED |
| 1-axis opposite two-site seed | reuse `t(A)=1`, `t(C)=4`, mixed `M(C)`, split fail at `C` | different seed; second pair is a new seed, not a formed child; here `t(A)=0` and face HOLDs | ATTEMPTED |
| y-probe split neighbor-read | score the four y-probes on this seed | y-probe face fails; this letter is the four z-probes | ATTEMPTED |
| x-probe split neighbor-read | score the four x-probes on this seed | x-probe reverse fails and face fails; this letter is the four z-probes | ATTEMPTED |
| unique letter | replace mixed sets by a singleton or `UNDEFINED` | mixed `O(A,τ)` remains a set; split still fails at `A` | ATTEMPTED |
| 2-in 1-out as `UNDEFINED` | treat `|Axis(M)|=2` cover as unformed | 2-in 1-out is fail of this object, not UNDEFINED | ATTEMPTED |
| named-sign lettering | collapse `{±e_i}` to `{+,−}` | named-sign lettering lost the axis | ATTEMPTED |
| global later T | wait until `max t(A,B,C,D)` before reading | `τ1(q)=t(q)+1` and `τ2(q)=t(q)+2` are per-probe; no global T | ATTEMPTED |
| attach a formation member from already-recorded six-neighbor locks | form the probes by a neighbor-lock letter instead of perp-step | refused; not attached | ATTEMPTED |
| adopt bits into Admissibility | rewrite the local rule by split neighbor-read freeze | refused; displayed, not adopted | ATTEMPTED |

### N2 — wall independence

Missing physical adoption, missing identification of neighbor-read of split
with neighbor-read of signed `M`, missing identification of neighbor-read
of split with neighbor-read of signed `O`, missing identification of
neighbor-read of split with nm2sl12z split without neighbor-read, missing
identification of this member with nm2sreadt2z opposite-z composition,
missing identification of this freeze with nm2sreadslz one-cut or with
nm2splt2slz split freeze, and missing Record identification of split
neighbor-read reverse are distinct open premises. This note claims no
complete wall collection.

### N3 — hidden-condition scan

The host `B_3(0)`, two disjoint same-lock pairs with locks `+e_1`, `+e_1`,
`+e_2`, and `+e_2`, perpendicular step rule, incoming-step lock, own
incoming set and own outgoing dual from records with tick `<= τ`, per-probe
`τ1=t+1` and `τ2=t+2`, unsigned axis, split as cover and `|Axis(M)|=1`,
neighbor-read as split HOLD together with unsigned axis-equality of `M` and
of `O` at a formed six-neighbor that also has split HOLD, composition as
equality of those bits, four z-probes with seed `A`, reverse as
neighbor-read at `A` and `B`, face as neighbor-read at `C` and `D`, and
mixed remains a set are declared. No uniqueness of incoming locks, no
signed-set equality of `M` as the scored object, no signed-set equality of
`O` as the scored object, no split without neighbor-read as the scored
object, no split freeze as the scored composition, no global later T, no
formation attachment from already-recorded six-neighbor locks, and no
Admissibility rewrite are silently assumed.

### N4 — source residual matching

The current axiom memo supplies cubic sites, `M_2(C)`,
content-conditional-on-formation, and unreadable absence. The residual that
formation site, probability, and rate remain unsupplied is unchanged. The
neighbor-read reverse fail, face hold, and composition hold reports do not
close that residual.

### N5 — resolution and rhetoric audit

| Resolution | Executed | Not claimed |
|---|---|---|
| per element | each unsigned lattice axis of `M` and of `O` at a probe and at formed 6-NN | no continuum alphabet |
| per site | `A,B,C,D` z-probes on `B_3(0)` only | no other cubic sites |
| per mode | no mode calculation | no spectral exhaustion |
| per block | four neighbor-read reports at t+1 and t+2 plus reverse/face/composition | no adopted content law |
| lattice wide | checked and not executed | no lattice-wide lettering rule |

### N6 — live partial-closure paths

Live routes include a later Record content map for split neighbor-read
reverse/face, a formation-rate rule, and a physical selector among matching
six-neighbors. None is taken here.

### N7 — hostile steelman

**Steelman:** Neighbor-read of the 1-in 2-out split freeze on same-lock
z-probes is leftover of nm2sreadslz because the `t+1` bits already fail
reverse and HOLD face; leftover of nm2splt2slz because split also freezes;
leftover of nm2readslz because some neighbor already carries the same
incoming letter; leftover of neighbor-read of signed `O` because reverse
already fails; leftover of nm2sl12z split with the matching-neighbor demand
dropped; leftover of nm2sreadt2z because only a sign of two seed letters
changed; and uniqueness of `M` already answers the match.

**Answer:** nm2sreadslz scores only `τ=t+1`. This letter also scores `τ2` and
composition of the four neighbor-read bits. nm2splt2slz scores equality of
split bits at `t` versus `t+1`; this composition scores equality of
neighbor-read bits at `t+1` versus `t+2`. nm2readslz HOLDs at seed `A`
because signed `M` of the partner is `{+e_2}`; this member fails at `A`
because split fails. Signed `O` of `B` is not signed `O` of `D`;
neighbor-read of signed `O` fails face while this member HOLDs face.
nm2sl12z does not ask for a matching-axis six-neighbor; split HOLDs at
`(0,1,1)` while neighbor-read fails there. Opposite-z probes HOLD reverse
at seed `A`. Mixed `O(A,τ)` remains a set; uniqueness is not required.
Reverse neighbor-read is HOLD iff neighbor-read of split at `A` and at `B`,
not leftover of nm2readslz and not leftover of signed-`O` neighbor-read.

### N8 — cross-cycle echo

nm2sreadslz reported neighbor-read of the 1-in 2-out split at `τ=t+1` on
these four z-probes with reverse fail and face hold. nm2sl12z reported
1-in 2-out split of `M` and `O` at `τ=t+1` with reverse fail and face hold.
nm2readslz reported neighbor-read of `M` at `τ=t+1` with HOLD at seed `A`
and reverse hold. nm2splt2slz reported split composition of `t` versus
`t+1`. nm2sreadt2z reported neighbor-read composition on opposite z with
HOLD at `A` and reverse hold. Two-axis same-lock y-probes report
split-neighbor-read reverse hold and face fail. Two-axis same-lock
x-probes report reverse fail and face fail. This note is not those
displays: it reports neighbor-read of the 1-in 2-out split at `τ1=t+1`
versus `τ2=t+2` on two disjoint same-lock pairs with z-probes, fail at `A`
and HOLD at `B`,`C`,`D` at both cuts, reverse fail and face hold at each
cut, and composition hold. HOLD iff split HOLDs and some formed 6-NN has
split HOLD with matching Axis(`M`) and Axis(`O`), not leftover of
nm2sreadslz one-cut, not leftover of nm2splt2slz split composition, not
leftover of nm2readslz neighbor-read of M, and not leftover of
nm2oreadslz neighbor-read of O.

**Gate disposition:** PASS for the neighbor-read of split `t+1` versus
`t+2` reverse/face/composition reports above. FAIL / DO NOT SHIP for “the
predicate equals the named sign,” “the predicate equals the unique
singleton lock vector,” “the predicate equals neighbor-read of signed `M`,”
“the predicate equals neighbor-read of signed `O`,” “the predicate equals
nm2sl12z split without neighbor-read,” “the predicate equals nm2sreadt2z
opposite-z composition,” “the predicate equals nm2sreadslz one-cut,” “the
predicate equals nm2splt2slz split freeze,” “bits are Admissibility,”
“neighbor-read HOLDs at `A`,” “reverse neighbor-read HOLDs,” or “face
neighbor-read fails.”

## Primary runner

The paired runner builds Euclidean `B_3(0)`, runs the two-axis same-lock
perp-step incoming-lock process, reads each z-probe's own earliest incoming
set and own outgoing dual from the record prefix at that probe's `t+1` and
`t+2`, reports split of those pairs, reports split and neighbor-read at each
formed six-neighbor at both cuts, reports neighbor-read as split HOLD
together with unsigned axis-equality of `M` and of `O` at a formed
six-neighbor that also has split HOLD, lists matching six-neighbors, reports
reverse/face at each cut, reports composition of the four bits, compares to
neighbor-read of signed `M` and of signed `O` and to opposite and 1-axis
leftovers, and checks Theorems 1--3. It also checks that neighbor-read fails
at `A` because split fails at both cuts, that mixed sets remain sets, that
unique-letter is `UNDEFINED` at mixed `O`, that composition of neighbor-read
bits is not leftover of nm2splt2slz split freeze as a reverse, that the
construction does not sum, that a formation member from already-recorded
six-neighbor locks is not attached, and that the display is not leftover of
nm2sreadslz one-cut, of nm2readslz neighbor-read of M, or of nm2sreadt2z
opposite-z composition. No runner cache is written.
