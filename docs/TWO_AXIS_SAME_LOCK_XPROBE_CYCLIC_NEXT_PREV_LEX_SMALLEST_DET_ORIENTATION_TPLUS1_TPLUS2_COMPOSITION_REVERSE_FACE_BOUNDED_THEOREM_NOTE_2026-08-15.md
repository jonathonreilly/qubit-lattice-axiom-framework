---
claim_id: two_axis_same_lock_xprobe_cyclic_next_prev_lex_smallest_det_orientation_tplus1_tplus2_composition_reverse_face_bounded_theorem_note_2026-08-15
claim_type: bounded_theorem
claim_scope: "Cyclic lex-smallest orientation at t+1 versus t+2 on the four x-probes of the two-axis same-lock seed, reverse/face at each cut, and composition, are reported. Displayed, not adopted."
upstream_dependencies:
  - minimal_axioms
runner: scripts/two_axis_same_lock_xprobe_cyclic_next_prev_lex_smallest_det_orientation_tplus1_tplus2_composition_reverse_face_2026_08_15.py
---

# Cyclic Lex-Smallest Orientation Freeze t+1 Versus t+2 Reverse And Face On Four X-Probes Of The Two-Axis Same-Lock Seed

> **Key terms used in this doc** are indexed A-Z at `docs/KEY_TERMINOLOGY.md`;
> each row points to the canonical source-of-truth doc.

**Date:** 2026-08-15
**Type:** bounded_theorem
**Scope:** cyclic next/prev lex-smallest outgoing determinant orientation of
the 1-in 2-out frame of simultaneous earliest incoming set `M` and outgoing
dual `O` at each probe's `τ1=t+1` and `τ2=t+2`, reverse/face from that sign
at each cut, and composition of Orient, on the four x-probes of the
two-axis same-lock seed in `B_3(0)={n:n·n<=9}`. Same process and x-probes
as nm2slx. Orient as nm2oricyccz at each cut. `M`, `O`, split as nm2sl12.
Cyclic `i`, `e_next`, `e_prev` as nm2oricyclz. Let `t(q)` be the formation
tick of probe `q`. Cuts are local: `τ1=t+1`, `τ2=t+2`. There is no global
T. Do not score τ=t. `M(q,τ)` is the set of earliest incoming
nearest-neighbor steps at `q` using only records with tick `<= τ`. Seeds
are a singleton seed letter. `O(q,τ)` is the outgoing dual of `M`: the set
of `e` in `{±e_1,±e_2,±e_3}` such that `q+e` is formed and `e` is in
`M(q+e,τ)`. Unformed at `τ` is `UNDEFINED`. Empty `O` is empty, not
`UNDEFINED`. Axis of a defined lock set `S` is
`Axis(S)={e_i | some ±e_i in S}`. Cover HOLDs at `q` if and only if
`Axis(M)` intersect `Axis(O)` is empty and `Axis(M)` union `Axis(O)` equals
`{e_1,e_2,e_3}`. Split HOLDs at `q` if and only if cover HOLDs and
`|Axis(M)|=1` (hence `|Axis(O)|=2`). Split HOLD required. When split
HOLDs, `m` is the unique vector in `M`. Let `i` in `{1,2,3}` be the axis
index of `m`. `e_next = e_{i+1}` with `3+1→1`. `e_prev = e_{i-1}` with
`1−1→3`. `O_next = O ∩ {±e_next}`. `O_prev = O ∩ {±e_prev}`. If either
empty, Orient fails, not `UNDEFINED`. Order `+e < −e`. `o_next` is the
lex-smallest vector in `O_next` (hence `+e` if both signs). `o_prev`
likewise. `Orient(q,τ)` is the sign of the integer determinant of the 3×3
matrix with columns `m`, `o_next`, `o_prev`. If split fails, Orient fails,
not `UNDEFINED`. Reverse HOLDs if and only if `Orient(A)=Orient(B)` both
`±1` at that cut. Face HOLDs if and only if `Orient(C)=Orient(D)` both
`±1` at that cut. Composition HOLDs if and only if `Orient` at `τ1` equals
`Orient` at `τ2` at `A,B,C,D`. Cover and split do not score handedness.
This is not leftover of nm2oricyccz cyclic lex-smallest at `t+1` alone.
This is not leftover of nm2ocyccslx cyclic lex-smallest at `t+1` alone on these x-probes.
This is not leftover of nm2simt2z simultaneous `M` and `O` freeze. This is
not leftover of nm2oricyclz lex-largest cyclic next/prev. This is not
leftover of nm2oricyclslx cyclic lex-largest on this same-lock seed. This
is not leftover of nm2orionez lex-one signed outgoing letters. This is not
leftover of nm2chiralz lexicographic unsigned `o1,o2` orientation. This is
not leftover of nm2oridetz unique signed outgoing letters. This is not
leftover of nm2orichz opposite-pair leftover-axis orientation. This is not
leftover of nm2slx axis-cover. This is not leftover of nm2axz axis-cover.
This is not leftover of nm2ax12z 1-in 2-out split. This is not leftover of
leftover-of-`M` alone. This is not leftover of leftover-of-`O` alone. This
is not leftover-empty fail of leftover axis. This is not leftover of
nmunopp union. This is not leftover of nmt2opp `M` frozen at `t`. This is
not leftover of nmot2opp two-tick composition. This is not leftover of
nmoutopp untimed eventual-`O`. This is not leftover of mixed #7188
fail/fail. This is not leftover of the 1-axis same-lock two-site seed.
This is not leftover of the two-axis opposite seed. Neither pair is
opposite. The second pair is a new seed, not a formed child. Uniqueness is
not required. Mixed remains a set. Displayed, not adopted. Do not write
into Admissibility. Do not attach L1.
**Audit-status authority:** independent audit lane only. This note authors no
audit verdict and predicts none.
**Primary runner:**
[`scripts/two_axis_same_lock_xprobe_cyclic_next_prev_lex_smallest_det_orientation_tplus1_tplus2_composition_reverse_face_2026_08_15.py`](../scripts/two_axis_same_lock_xprobe_cyclic_next_prev_lex_smallest_det_orientation_tplus1_tplus2_composition_reverse_face_2026_08_15.py)

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
and `Axis(O)`. Split is cover together with `|Axis(M)|=1`. The cyclic
next/prev lex-smallest oriented frame is the integer sign of
`det(m,o_next,o_prev)` with unique signed incoming letter `m`, cyclic axes
of `Axis(M)`, and the lex-smallest signed outgoing letter on each of those
cyclic slots under `+e < −e`. Reverse and face are scored on equal `±1`
signs at the paired probes at each cut. Composition is equality of those
four Orient reports across the two cuts. Named signs `{+,−}` of locks are
a coarser readout and are not used as the object. A singleton unique
outgoing lock letter is a different readout and is not used as the object.
Unsigned axis units of `Axis(O)` are a different readout and are not used.
Unique signed letters requiring `|O_i|=1` are a different readout and are
not used. Axis-order lex-one `(o_j,o_k)` is a different readout and is not
used. Lex-largest cyclic next/prev is a different readout and is not used.
Opposite-pair leftover-axis orientation is a different readout and is not
used. Existential opposite of signed locks is a different readout and is
not used. Axis-cover without the frame sign is a different readout and is
not used. 1-in 2-out split without the frame sign is a different readout
and is not used. Simultaneous `M` and `O` freeze is a different readout
and is not used. Leftover-empty fail of unsigned leftover axis sets is a
different readout and is not used. A `Z^3` sum of those locks is a
different readout and is not used. Occupancy of sites is not used. A
six-neighbor star is not the letter.

## Machine status and trace

```yaml
actual_current_surface_status: bounded-support
target_claim_type: bounded_theorem
claim_type_reason: "Exact report of cyclic next/prev lex-smallest outgoing determinant orientation of the 1-in 2-out frame of M and O at t+1 versus t+2 on the four x-probes of the two-axis same-lock seed, Orient fail,+1,-1,fail at A,B,C,D at each cut, reverse fail and face fail at each cut, composition hold; uniqueness of outgoing locks is not claimed and the bits are not adopted."
trace_class: frontier_discovery
target_claim_id: two_axis_same_lock_xprobe_cyclic_next_prev_lex_smallest_det_orientation_tplus1_tplus2_composition_reverse_face
target_blocker_text: "display cyclic lex-smallest orientation freeze t+1 versus t+2 reverse/face composition on the four x-probes of the two-axis same-lock seed"
source_of_blocker_text: handoff
reachability_to_target: advances
artifact_role: theorem
next_trace_action: "Keep cyclic next/prev lex-smallest outgoing determinant orientation of the 1-in 2-out frame of M and O at t+1 versus t+2 displayed; do not write Orient into Admissibility, do not reduce to nm2oricyccz t+1 alone, do not reduce to nm2ocyccslx t+1 alone, do not reduce to nm2simt2z M-and-O freeze, do not reduce to lex-largest cyclic next/prev, do not reduce to nm2oricyclslx same-lock lex-largest, do not reduce to lex-one signed axis-order, do not reduce to unique signed |O_i|=1, do not reduce to lexicographic unsigned o1,o2, do not reduce to opposite-pair leftover-axis, do not reduce to cover, do not reduce to split, do not reduce to leftover-empty fail, do not reduce to leftover of M alone or leftover of O alone, do not replace Orient by unique outgoing letters, do not replace Orient by existential opposite of signed locks, do not replace Orient by six-neighbor lock union, and do not attach L1."
conditional_surface_status: "exact on B_3(0) for cyclic next/prev lex-smallest outgoing determinant orientation of the 1-in 2-out frame of M and O at t+1 versus t+2 on the four x-probes of the two-axis same-lock seed, reverse/face at each cut, and composition; displayed, not adopted"
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
cyclic next/prev lex-smallest outgoing determinant orientation of `M`
and `O` at `τ1` and at `τ2` is scored:

```text
A = (1,0,0),  B = (1,1,1),  C = (2,0,0),  D = (1,1,0).
```

These are not the y-probes `A=(0,1,0)`, `B=(1,1,1)`, `C=(0,2,0)`,
`D=(1,1,0)`. These are not the z-probes `A=(0,0,1)`, `B=(1,1,1)`, `C=(0,0,2)`,
`D=(1,0,1)`. `A` is not a seed. Same process and
x-probes as nm2slx.

Lock alphabet of the displayed process: `{±e_i}` with `i` in `{1,2,3}`.

Seed: two disjoint same-lock pairs recorded at formation tick 0. Origin
locks `+e_1` and `(0,1,0)` locks `+e_1`. `(0,0,1)` locks `+e_2` and
`(0,1,1)` locks `+e_2`. The second pair is a new seed, not a formed
child of the first pair, and neither pair is opposite. This seed is not
the 1-axis same-lock two-site seed `{0,(0,1,0)}` with `+e_1/+e_1` alone.
This seed is not the two-axis opposite seed `+e_1/−e_1` and `+e_2/−e_2`.
This seed is not the perp two-site seed `+e_1/+e_2`. This seed is not the
x-axis same-lock seed `{0,(1,0,0)}` with `+e_2/+e_2`. This seed is not the
z-symmetric three-site seed `{0,(0,0,1),(0,0,-1)}`. This seed is not the
y-symmetric three-site seed that also records `(0,-1,0)` at tick 0.

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

## Named cyclic next/prev lex-smallest determinant of `M` and `O` at `τ1` and `τ2`

Let `t(q)` be the formation tick of x-probe `q` when that tick is defined in
`B_3(0)`. Let `τ1(q)=t(q)+1` and `τ2(q)=t(q)+2`. There is no global T.
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
not require `O` to be a singleton. It does not sum either set. It does not
replace `O` by `M`. It does not wait for a global later T. Occupancy of
sites is not used. O is not M.

Unsigned axis of a defined lock set:

```text
Axis(S) = { e_i | some ±e_i in S }.
```

Cover at a probe at a cut:

```text
cover(q) HOLDs iff Axis(M) intersect Axis(O) is empty
and Axis(M) union Axis(O) equals {e_1,e_2,e_3}.
```

Split at a probe at a cut:

```text
split(q) HOLDs iff cover HOLDs and |Axis(M)|=1
(hence |Axis(O)|=2).
```

2-in 1-out is fail of split, not UNDEFINED. If `q` is unformed at `τ`, then
split is `UNDEFINED`.

Oriented frame at a cut, as nm2oricyccz:

```text
When split HOLDs, m is the unique signed letter in M.
i in {1,2,3} is the axis index of m.
e_next = e_{i+1} with 3+1→1.
e_prev = e_{i-1} with 1−1→3.
O_next = O ∩ {±e_next}.
O_prev = O ∩ {±e_prev}.
If either is empty, Orient fails, not UNDEFINED.
Order +e < −e.
o_next is the lex-smallest vector in O_next (hence +e if both signs).
o_prev is the lex-smallest vector in O_prev.
Orient(q,τ) = sign of the integer determinant of columns (m, o_next, o_prev).
Else fail, not UNDEFINED, if split fails.
UNDEFINED if M or O is UNDEFINED.
```

The outgoing pair is signed. Mixed opposite signs on a cyclic slot make
`|O_next|=2` or `|O_prev|=2`; lex-smallest still picks `+e`, so Orient is
defined when split HOLDs. Unique outgoing letters of the whole set `O`
are not required: mixed `O` remains a set, and unique-letter readout of
mixed `O` is `UNDEFINED` while this Orient is a sign. Empty `O_next` or
empty `O_prev` is Orient fail, not `UNDEFINED`. A vanishing determinant
is fail. Sign of a nonzero integer determinant is `+1` or `−1`. Split
HOLD required: 2-in 1-out is Orient fail, not UNDEFINED. Lex-largest on
the same cyclic slots is a different readout and is not used. Axis-order
lex-one `(o_j,o_k)` is a different readout and is not used.

Reverse oriented frame at a cut holds if and only if `Orient(A)=Orient(B)`
and both signs are `±1`. Face oriented frame at a cut holds if and only if
`Orient(C)=Orient(D)` and both signs are `±1`. Either side `UNDEFINED` is
`UNDEFINED`. Else if both sides are equal `±1`, reverse or face HOLDs.
Else fail.

Composition holds if and only if `Orient(q,τ1)=Orient(q,τ2)` at each of
`A,B,C,D`. Either side `UNDEFINED` is `UNDEFINED`. Else if the four signs
agree across the two cuts, composition HOLDs. Else fail.

Cover and split do not score handedness. Identifying cover reverse with
this reverse is refused: cover reverse fails from leftover `{e_2}` at `A`
and cover face fails at `D` without reporting cyclic columns at `B` and
at `C`. Identifying split reverse with this reverse is refused: split
reverse fails and split face fails without cyclic next/prev columns.
Identifying leftover-empty fail with this reverse is refused:
leftover-empty fail scores leftover `{e_2}` at `A` and empty leftover at
`B` as reverse fail and face fail, while on unique signed
`O={+e_1,+e_3}` leftover is empty while Orient is `+1`. Identifying
lexicographic unsigned `o1,o2` with this reverse is refused: unsigned
reverse fails and unsigned face fails from Orient fail at `D`, while
unsigned Orient at `C` is `+1` and this Orient at `C` is `−1`.
Identifying unique signed `|O_i|=1` with this reverse is refused: unique
signed reverse fails and face fails because `B` and `C` have an opposite
pair in `O`, while this Orient at `B` is `+1` from lex-smallest `+e_3`.
Identifying opposite-pair leftover-axis orientation with this reverse is
refused: leftover-axis reverse fails and face fails, and leftover-axis
at `C` is `+1` while this Orient at `C` is `−1`. Identifying nm2orionez
lex-one axis-order with this reverse is refused: lex-one reverse fails
and lex-one face fails with `fail,+1,−1,fail`, matching these
reverse/face bits; those columns are axis-order `(o_j,o_k)`, not cyclic
`(o_next,o_prev)`, and `det(+e_2,+e_1,+e_3)=−1` while cyclic
`det(+e_2,+e_3,+e_1)=+1`. Identifying nm2oricyclz lex-largest cyclic
next/prev with this reverse is refused: opposite-seed lex-largest reverse
HOLDs. Identifying nm2oricyclslx lex-largest on this same-lock seed with
this reverse is refused: lex-largest reverse fails and face fails with
`fail,−1,+1,fail`, while this reverse fails and this face fails with
`fail,+1,−1,fail`. Identifying nm2oricyccz opposite-seed reverse hold and
face hold with this reverse is refused: nm2oricyccz has split HOLD at `A`
and `Orient(A)=+1`. Identifying nm2ocyccslx `t+1` alone with this freeze
is refused: that letter has no `t+2` cut. Identifying a named sign of
those locks with reverse or face is refused: named-sign lettering lost
the axis.

## Theorem 1 — ticks, `M`, `O`, and Orient at `τ1` and `τ2`

On this process the four x-probes form. Compare to leftover axis: leftover
at `A` is `{e_2}` and leftover at `B` is empty, so leftover reverse fails
and leftover face fails. Compare to nm2slx cover: cover fails at `A` and
at `D` from leftover `{e_2}` and HOLDs at `B` and at `C`, so cover reverse
fails and cover face fails. Compare to nm2oricyccz cyclic lex-smallest on
the two-axis opposite z-probes: that member has split HOLD at `A`,
`O(A,τ)={+e_1, −e_1, +e_3}` missing the partner letter, `Orient(A)=+1`,
reverse HOLDs from equal `+1` signs, and face HOLDs. Compare to
nm2oricyclslx lex-largest on these same-lock x-probes: reverse fails and
face fails with signs `fail,−1,+1,fail`. Compare to nm2orionez lex-one on
this same-lock member: reverse fails and face fails with signs
`fail,+1,−1,fail`. Compare to nm2chiralz lexicographic unsigned `o1,o2`
orientation on this same-lock member: reverse fails and face fails with
unsigned signs `fail,+1,+1,fail`. Compare to nm2oridetz unique signed
outgoing letters: reverse fails and face fails because `|O_i|≠1` at `B`
and at `C`. Compare to nm2orichz opposite-pair leftover-axis orientation:
reverse fails and face fails on this member. Compare to nm2ocyccslx: that
letter is the `t+1` cut alone on these x-probes. This display reads the
cyclic next/prev lex-smallest outgoing determinant of those same timed
sets at both cuts:

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
split(A, τ1) = fail
split(B, τ1) = hold
split(C, τ1) = hold
split(D, τ1) = fail
m(A, τ1) = −e_3
i(A, τ1) = 3
o_next(A, τ1) = +e_1
o_prev(A, τ1) = fail
det(A, τ1) = fail
Orient(A, τ1) = fail
m(B, τ1) = +e_1
i(B, τ1) = 1
o_next(B, τ1) = +e_2
o_prev(B, τ1) = +e_3
det(B, τ1) = 1
Orient(B, τ1) = +1
m(C, τ1) = +e_1
i(C, τ1) = 1
o_next(C, τ1) = −e_2
o_prev(C, τ1) = +e_3
det(C, τ1) = -1
Orient(C, τ1) = −1
m(D, τ1) = −e_3
i(D, τ1) = 3
o_next(D, τ1) = +e_1
o_prev(D, τ1) = fail
det(D, τ1) = fail
Orient(D, τ1) = fail
M(A, τ2) = {−e_3}
M(B, τ2) = {+e_1}
M(C, τ2) = {+e_1}
M(D, τ2) = {−e_3}
O(A, τ2) = {+e_1}
O(B, τ2) = {+e_2, +e_3, −e_3}
O(C, τ2) = {−e_2, +e_3, −e_3}
O(D, τ2) = {+e_1}
Orient(A, τ2) = fail
Orient(B, τ2) = +1
Orient(C, τ2) = −1
Orient(D, τ2) = fail
```

`A` is not a seed. `A=(1,0,0)` forms at tick 2 locking `−e_3`. The second
same-lock pair `(0,0,1)` and `(0,1,1)` are seeds at tick 0 with seed
letter `+e_2`. Mixed remains a set: `O(B,τ1)` has three outgoing steps and
`O(C,τ1)` has three outgoing steps. Unique outgoing letters would assign
`UNDEFINED` at mixed `O` at `B` and at `C`. Unique outgoing letters of
`O(A)={+e_1}` and `O(D)={+e_1}` are singletons, and unique-letter Orient
there is fail, not `UNDEFINED`, because split fails. Unique signed
`|O_i|=1` fails at `B` and at `C` because each has both `±e_3`. At `A`,
unique `m` still gives `i=3` and `o_next=+e_1`, but `O_prev` on `e_2` is
empty, so `(o_next,o_prev)` fails and split fails from leftover `{e_2}`,
so Orient fails, not `UNDEFINED`. Split HOLD is required. Cyclic
lex-smallest picks `+e` on each mixed cyclic slot, so `(o_next,o_prev)` is
defined at `B` and at `C`. `M` is a singleton at each probe, so the unique
signed `m` and axis index `i` exist. Cover and split fail at `A` and at
`D` from leftover `{e_2}` and HOLD at `B` and at `C`; they do not score
that cyclic lex-smallest Orient is `fail,+1,−1,fail`. At `B`, `i=1` so
`e_next=e_2` and `e_prev=e_3`; mixed `O_prev={+e_3,−e_3}` picks `+e_3`.
Unsigned axis-order 2-plane at `C` is `(e_2,e_3)` and lexicographic Orient
at `C` is `+1`, while cyclic `(o_next,o_prev)` at `C` is `(−e_2,+e_3)` and
Orient is `−1`. Opposite-pair leftover-axis at `A` fails from split fail.
Lex-one at `A` fails from split fail. Lex-largest cyclic at `A` also fails
from split fail, while at `B` lex-largest picks `o_prev=−e_3` and Orient
`−1` against this `+1`. O is empty at formation at every probe. O is not
M.

On the 1-axis same-lock two-site seed, `A=(1,0,0)` is a formed child at
tick 3 with mixed `M`, cover HOLDs, split fails from 2-in 1-out, and
Orient at `A` is fail, not UNDEFINED. Cover reverse HOLDs on that 1-axis
member while this cover reverse fails. That is leftover of the first pair.
Here both `(0,0,1)` and `(0,1,1)` are seeds of a second same-lock pair on a
second axis, and `t(A)=2`. On the y-probes of this same seed, split HOLDs
at `A` and `O(A)={+e_2,−e_3}` has nonempty cyclic slots, so cyclic
lex-smallest Orient at that y-probe is `−1`, lexicographic unsigned
`o1,o2` there is `+1`, and opposite-pair leftover-axis Orient there fails
from no opposite pair in `O`. Y-probe reverse fails (`−1,+1`) and y-face
fails, while this x-probe reverse fails (`fail,+1`) and this x-face fails
(`−1,fail`). The four z-probes of this same seed give reverse fail and
face HOLD.

New records in `B_3(0)` between `t` and `t+1` that meet a probe's
six-neighbors enter `O` and do not enter earliest `M`. The `t+1` neighbor
of `A` is `C=(2,0,0)`, which forms with earliest incoming `+e_1`, so
`+e_1` is in `O(A)`. No six-neighbor of any of the four x-probes forms at
`t+2`:

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

`M` is frozen from `t` to `t+1` and from `t+1` to `t+2`. At `t`, `O` is
empty at each of `A`, `B`, `C`, and `D`; split fails at each probe, and
Orient is fail, not UNDEFINED. Do not score `τ=t`.

## Theorem 2 — reverse and face from oriented frame at `τ1` and `τ2`

Reverse oriented frame holds if and only if `Orient(A)=Orient(B)` both
`±1`. At `τ1`, `Orient(A)` is fail and `Orient(B)=+1`. Reverse fails. At
`τ2`, `Orient(A)` is fail and `Orient(B)=+1`. Reverse fails. This is HOLD
iff equal `±1` signs, not leftover of nm2chiralz lexicographic unsigned
`o1,o2`, not leftover of nm2oridetz unique signed outgoing letters, not
leftover of nm2orichz opposite-pair leftover-axis, not leftover of
nm2orionez lex-one, not leftover of nm2oricyclz lex-largest, not leftover
of nm2oricyclslx lex-largest on this seed, not leftover of nm2oricyccz
opposite-seed reverse hold, not leftover of nm2slx axis-cover, not leftover
of nm2axz axis-cover, not leftover of nm2ax12z 1-in 2-out split, not
leftover-empty fail, and not exist-opposite.

Reverse oriented frame at τ1: fail
Reverse oriented frame at τ2: fail

Both sides are defined, so this is not `UNDEFINED`. Cover reverse fails
because cover fails at `A` from leftover `{e_2}`. Split reverse fails
because split fails at `A`. Cover and split do not score handedness.
Lexicographic unsigned reverse fails because unsigned Orient at `A` is
fail and at `B` is `+1`. Unique signed reverse fails because unique signed
Orient at `A` is fail and at `B` is fail. Opposite-pair leftover-axis
reverse fails because that Orient at `A` is fail. Lex-one signed reverse
fails because those signs are `fail,+1`. Lex-largest cyclic reverse on
this seed fails with `fail,−1`. nm2oricyccz reverse HOLDs with `+1,+1`.
Leftover-empty reverse fails because leftover of the union at `A` is
`{e_2}` and leftover at `B` is empty. Leftover of `M` reverse fails
because leftover of `M` at `A` is `{e_1, e_2}` and at `B` is `{e_2, e_3}`:
nonempty and unequal. Leftover of `O` reverse fails because leftover of
`O` at `A` is `{e_2, e_3}` and leftover of `O` at `B` is `{e_1}`.
Exist-opposite reverse of signed `M` fails. Exist-opposite reverse of
signed `O` fails. Presence of an opposite pair in `O` fails at `A` and
HOLDs at `B`. Those leftovers are not this display.

Face oriented frame holds if and only if `Orient(C)=Orient(D)` both `±1`.
At `τ1`, `Orient(C)=−1` and `Orient(D)` is fail. Face fails. At `τ2`,
`Orient(C)=−1` and `Orient(D)` is fail. Face fails.

Face oriented frame at τ1: fail
Face oriented frame at τ2: fail

Cover face fails because cover fails at `D` from leftover `{e_2}`. Split
face fails because split fails at `D`. Cyclic lex-smallest oriented face
fails because `Orient(D)` is fail. Lex-one signed oriented face also
fails because those signs are `−1,fail`; those columns are axis-order
`(o_j,o_k)`, not cyclic `(o_next,o_prev)`. Lexicographic unsigned face
fails because unsigned Orient at `C` is `+1` and at `D` is fail; those
signs are not these signs. Unique signed face fails because neither unique
signed sign is `±1`. Opposite-pair leftover-axis face fails because those
signs are `+1` and fail. Lex-largest cyclic face on this seed fails with
`+1,fail`, not these `−1,fail`. Cover and split do not score handedness.
Presence of an opposite pair in `O` HOLDs at `C` and fails at `D`. On the
1-axis same-lock two-site seed, cover reverse HOLDs while this cover
reverse fails, and cover face HOLDs while this cover face fails. This
two-axis member is not leftover of that 1-axis cover reverse HOLD. The
four y-probes of this same seed give cyclic lex-smallest Orient `−1` at
`A` and Orient fail at `D` from split fail, so oriented y-face fails while
this x-face also fails from a different pair of reports: y-probe `A` is a
seed with Orient `−1`, and this x-probe `A` is not a seed with Orient
fail. The four z-probes give oriented reverse fail and oriented face
HOLD. Those probe-direction readouts are not this x-probe display.
Leftover-empty face fails because leftover of the union is empty at `C`
and leftover at `D` is `{e_2}`. Leftover of `M` at `C` is `{e_2, e_3}` and
leftover of `M` at `D` is `{e_1, e_2}`: nonempty and unequal. Leftover of
`O` at `C` is `{e_1}` and leftover of `O` at `D` is `{e_2, e_3}`: nonempty
and unequal. Exist-opposite face of signed `M` fails. Exist-opposite face
of signed `O` fails. Cyclic lex-smallest oriented face fails at both cuts.

Empty leftover does not make reverse `UNDEFINED`. Leftover-empty fail is
not this reverse. Cover reverse fails from leftover `{e_2}` at `A`. Cover
fails at `D` and split fails at `D`. Orient at `D` is fail because
`O_prev` on `e_2` is empty and split fails. Orient at `A` is fail because
split fails, not because `O` is unformed.

Reverse fails at both cuts. Face fails at both cuts.

## Theorem 3 — composition of Orient at `τ1` versus `τ2`

Composition HOLDs if and only if `Orient` at `τ1` equals `Orient` at `τ2`
at `A,B,C,D`. `Orient(A,τ1)=Orient(A,τ2)=fail`,
`Orient(B,τ1)=Orient(B,τ2)=+1`, `Orient(C,τ1)=Orient(C,τ2)=−1`,
`Orient(D,τ1)=Orient(D,τ2)=fail`. Composition HOLDs.

Composition of Orient: hold

Displayed, not adopted. The bits are not written into Admissibility.
Do not write into Admissibility. Do not attach L1.

The reverse-fail and face-fail cyclic lex-smallest orientation of this
same-lock member at `t+1` freezes at `t+2`: the four reports are
unchanged. That freeze is the present letter. It is not leftover of
nm2oricyccz, which scores only one cut on the opposite seed with reverse
HOLD. It is not leftover of nm2ocyccslx, which scores only the `t+1` cut
on these x-probes. It is not leftover of nm2oricyclslx, which scores
lex-largest on this seed at `t+1` alone with signs `fail,−1,+1,fail`. It
is not leftover of nm2simt2z, which scores equality of `M` and of `O`
rather than equality of Orient. On this member `M` and `O` also freeze, so
simultaneous freeze HOLDs as a leftover; the scored object remains the
four Orient reports. Bit-stability of reverse fail and face fail is a
leftover predicate: those bits can agree while a probe sign flips, which
composition of Orient would fail. Composition of Orient at `τ=t` versus
`τ=t+1` fails because Orient is fail at formation at every probe and `+1`
at `B` at `t+1`. Do not score `τ=t`.

## What this note does not claim

- It does not select a unique outgoing or leftover lock.
- It does not reduce lock vectors to named signs `{+,−}`.
- It does not require outgoing sides to be singletons.
- It does not sum either set.
- It does not replace Orient by leftover-empty fail.
- It does not replace Orient by leftover of `M` alone.
- It does not replace Orient by leftover of `O` alone.
- It does not replace Orient by existential opposite of signed locks.
- It does not replace Orient by presence of an opposite pair in `O`.
- It does not replace Orient by lexicographic unsigned `o1,o2` orientation.
- It does not replace Orient by unique signed `|O_i|=1` letters.
- It does not replace Orient by nm2orionez lex-one axis-order letters.
- It does not replace Orient by nm2oricyclz lex-largest cyclic next/prev.
- It does not replace Orient by nm2oricyclslx lex-largest on this same-lock seed.
- It does not replace Orient by opposite-pair leftover-axis orientation.
- It does not replace Orient by unsigned axis units of `Axis(O)`.
- It does not replace Orient by axis-cover without the frame sign.
- It does not replace Orient by 1-in 2-out split without the frame sign.
- It does not replace Orient composition by nm2simt2z `M` and `O` freeze.
- It does not treat split fail as `UNDEFINED`.
- It does not treat empty `O_i` as `UNDEFINED`.
- It does not replace `O` by `M`.
- It does not replace Orient by locks of six-neighbors.
- It does not use a six-neighbor star as the letter.
- It does not wait for a global later T.
- It does not attach a formation member from already-recorded six-neighbor
  locks.
- It does not reprint nmsimopp exist-opposite of `M` and of `O` at `t+1`.
- It does not reprint nmcover axis-cover reverse hold face hold as this
  oriented display.
- It does not reprint nm2slx axis-cover reverse fail face fail as this
  oriented display.
- It does not reprint nm2axz axis-cover reverse hold face hold as this
  oriented display.
- It does not reprint nm2ax12z 1-in 2-out split reverse hold face hold as
  this oriented display.
- It does not reprint nm2chiralz lexicographic unsigned `o1,o2` reverse fail
  face hold with `+1,+1` as this oriented display.
- It does not reprint nm2oridetz unique signed reverse fail face fail as
  this oriented display.
- It does not reprint nm2orichz opposite-pair leftover-axis reverse fail
  face fail as this oriented display.
- It does not reprint nm2orionez lex-one reverse fail face hold as this
  oriented display.
- It does not reprint nm2oricyclz lex-largest cyclic reverse hold face hold
  with `−1,−1,+1,+1` as this oriented display.
- It does not reprint nm2oricyclslx lex-largest reverse fail face fail with
  `fail,−1,+1,fail` as this oriented display.
- It does not reprint nm2oricyccz cyclic lex-smallest orientation at `t+1`
  alone.
- It does not reprint nm2ocyccslx cyclic lex-smallest orientation at `t+1`
  alone on these x-probes.
- It does not reprint nm2simt2z simultaneous `M` and `O` freeze as this
  Orient composition.
- It does not reprint the 1-axis same-lock two-site seed as this member.
- It does not reprint the two-axis opposite seed as this member.
- It does not score the y-probes or the z-probes as this letter.
- It does not reprint nmunopp untimed union.
- It does not reprint nmt2opp `M` frozen at `t` as this oriented display.
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

This display uses Lattice to name `B_3(0)` and the four x-probes. It uses Qubit
only as the algebra of the local possibility domain. It uses Record only as a
boundary: a present lock is content. It does not rewrite Admissibility. The
two-axis same-lock seed process, cyclic next/prev lex-smallest outgoing
determinant orientation of the 1-in 2-out frame of `M` and `O` at `t+1`
versus `t+2`, reverse/face at each cut, and composition of Orient are
displayed theorem-domain data.

## Exact target and obligation graph

| Obligation | Status |
|---|---|
| current Lattice / Admissibility / Record premises | quoted; no edit |
| perp-step incoming-lock process on `B_3(0)` | displayed; two disjoint same-lock pairs `+e_1/+e_1` and `+e_2/+e_2` |
| ticks `t(A)`, `t(B)`, `t(C)`, `t(D)` | Theorem 1; `2`, `1`, `3`, `2` |
| `M` at `τ1` and at `τ2` | Theorem 1; frozen equal to `M` at `t` |
| `O` at `τ1` and at `τ2` | Theorem 1; outgoing dual `{+e_1}` at `A` and at `D`, mixed at `B` and at `C`, freeze |
| unique signed `m`, cyclic `i`, lex-smallest `(o_next,o_prev)` | Theorem 1; singleton `M`; cyclic pair defined at `B` and at `C`; empty `O_prev` at `A` and at `D` |
| integer `det(m,o_next,o_prev)` at both cuts | Theorem 1; fail, `1`, `-1`, fail at each cut |
| Orient at `τ1` | Theorem 1; fail, `+1`, `−1`, fail |
| Orient at `τ2` | Theorem 1; fail, `+1`, `−1`, fail |
| reverse from oriented frame at `τ1` and at `τ2` | Theorem 2; `fail` at each cut |
| face from oriented frame at `τ1` and at `τ2` | Theorem 2; `fail` at each cut |
| composition of Orient | Theorem 3; `hold` |
| unique outgoing lock | not required |
| occupancy of sites as the letter | not used |
| named-sign `{+,−}` letter | not used; lost the axis |
| singleton unique lock-vector letter | not used as the object; mixed remains a set |
| `Z^3` sum of the lock set | not used; no aggregation |
| six-neighbor star as the letter | not used |
| leftover-empty fail of leftover axis | not this oriented display |
| leftover of exist-opposite HOLD | not this oriented display |
| leftover of nmcover axis-cover HOLD | not this oriented display |
| leftover of nm2slx axis-cover | not this oriented display |
| leftover of nm2axz axis-cover HOLD | not this oriented display |
| leftover of nm2ax12z 1-in 2-out split HOLD | not this oriented display |
| leftover of nm2chiralz lexicographic unsigned `o1,o2` | not this oriented display |
| leftover of nm2oridetz unique signed `|O_i|=1` | not this oriented display |
| leftover of nm2orichz opposite-pair leftover-axis | not this oriented display |
| leftover of nm2orionez lex-one axis-order | not this oriented display |
| leftover of nm2oricyclz lex-largest cyclic next/prev | not this oriented display |
| leftover of nm2oricyclslx lex-largest on this seed | not this freeze letter |
| leftover of nm2oricyccz `t+1` alone | not this freeze letter |
| leftover of nm2ocyccslx `t+1` alone | not this freeze letter |
| leftover of nm2simt2z `M` and `O` freeze | not this Orient composition |
| leftover of opposite-pair presence in `O` | not this oriented display |
| y-probe or z-probe Orient on this seed | not this letter |
| leftover of leftover-of-`M` alone | not this display |
| leftover of leftover-of-`O` alone | not this display |
| leftover of nmunopp untimed union | not this display |
| leftover of nmt2opp `M` frozen at `t` | not this display |
| leftover of nmot2opp two-tick composition | not this display |
| leftover of nmoutopp untimed eventual-`O` | not this display |
| two-tick lock-count clock composition | not this display |
| leftover of mixed #7188 fail/fail | not this display |
| leftover of the 1-axis same-lock two-site seed | not this display |
| leftover of the two-axis opposite seed | not this display |
| split fail scored as `UNDEFINED` | refused; Orient fail |
| empty `O_i` scored as `UNDEFINED` | refused; Orient fail |
| score at `τ=t` | refused |
| global later T | not used |
| oriented frame as Admissibility content | not adopted |
| formation site / probability / rate | open |
| physical Record readout of the bits | open |

## Value gate (V1–V5)

| # | Answer |
|---|---|
| V1 | It answers the first-display question: does the reverse-and-face cyclic lex-smallest orientation of nm2oricyccz freeze from `t+1` to `t+2` on the four x-probes of the two-axis same-lock seed. |
| V2 | Current main has no landed cyclic-next-prev-lex-smallest-outgoing-determinant reverse/face composition of timed `M` and `O` at `t+1` versus `t+2` on these four x-probes of the two-axis same-lock seed. |
| V3 | Orient reports at two cuts, the reverse/face bits at each cut, and composition are independently finite and exact. |
| V4 | The theorem is more than a restatement of Record because it reads cyclic next/prev lex-smallest outgoing letters of `Axis(M)` at two local cuts and reports that reverse fails from Orient fail at `A`, face fails from Orient fail at `D`, and the four reports freeze, while lex-largest at `B` is `−1` against this `+1`, unsigned at `C` is `+1` against this `−1`, leftover-axis at `C` is `+1`, nm2oricyccz reverse HOLDs, nm2ocyccslx scores only `t+1`, and nm2simt2z scores lock-set equality rather than Orient equality. |
| V5 | It is not an adopted content rule: the bits remain displayed. |

## No-go discipline gate

The negative content is narrow: the display does not write those bits into
Admissibility, does not reduce them to named signs, does not require a
unique outgoing lock, does not replace Orient by leftover-empty fail, does
not replace Orient by leftover of `M` alone or leftover of `O` alone, does
not replace Orient by existential opposite of signed locks, does not
replace Orient by presence of an opposite pair in `O`, does not replace
Orient by nm2chiralz lexicographic unsigned `o1,o2`, does not replace
Orient by nm2oridetz unique signed `|O_i|=1`, does not replace Orient by
nm2orionez lex-one, does not replace Orient by nm2oricyclz lex-largest,
does not replace Orient by nm2oricyclslx lex-largest on this seed, does
not replace Orient by nm2orichz opposite-pair leftover-axis, does
not replace Orient by nmcover axis-cover, does not replace Orient by
nm2slx axis-cover, does not replace Orient by nm2axz axis-cover, does not
replace Orient by nm2ax12z 1-in 2-out split, does not replace this freeze
by nm2oricyccz `t+1` alone, does not replace Orient composition by
nm2simt2z `M` and `O` freeze, does not identify this display with the
1-axis same-lock two-site seed, does not identify it with the two-axis
opposite seed, and does not identify it with nmunopp union. No global
impossibility is claimed.

### N1 — materially distinct routes

| Route | Attempt | Why it fails here | Marker |
|---|---|---|---|
| nm2oricyccz `t+1` alone | reuse reverse hold and face hold at one cut | that letter has no `t+2` cut, no Orient composition, and reverse HOLDs on the opposite seed | ATTEMPTED |
| nm2ocyccslx `t+1` alone | reuse reverse fail and face fail at one cut on these x-probes | that letter has no `t+2` cut and no Orient composition | ATTEMPTED |
| nm2oricyclslx lex-largest same-lock x | reuse lex-largest reverse fail and face fail at `t+1` | lex-largest signs are `fail,−1,+1,fail`; this letter is `fail,+1,−1,fail` at both cuts | ATTEMPTED |
| nm2simt2z `M` and `O` freeze | score equality of lock sets | simultaneous freeze HOLDs here as leftover; composition of this letter is equality of Orient reports | ATTEMPTED |
| reverse/face bit-stability | score reverse and face bits equal across cuts | those bits can agree while a probe sign flips; composition of Orient would then fail | ATTEMPTED |
| nm2chiralz lexicographic unsigned `o1,o2` | reuse unsigned reverse fail and face fail | unsigned reverse fails with these bits; unsigned Orient at `C` is `+1` while this Orient at `C` is `−1` | ATTEMPTED |
| nm2oridetz unique signed `|O_i|=1` | reuse unique signed reverse fail and face fail | unique signed reverse fails and face fails; an opposite pair in `O` at `B` and at `C` makes `|O_i|≠1` but lex-smallest still picks `+e` and Orient at `B` is `+1` | ATTEMPTED |
| nm2orionez lex-one axis-order | reuse lex-one reverse fail and face fail | lex-one reverse fails and lex-one face fails with `fail,+1,−1,fail`, matching these bits; columns are axis-order, and `det(+e_2,+e_1,+e_3)=−1` while cyclic `det(+e_2,+e_3,+e_1)=+1` | ATTEMPTED |
| nm2oricyclz lex-largest cyclic next/prev | reuse lex-largest reverse hold and face hold | opposite-seed lex-largest reverse HOLDs with `−1,−1`; this reverse fails | ATTEMPTED |
| nm2orichz opposite-pair leftover-axis | reuse leftover-axis reverse and face | leftover-axis reverse fails and face fails; leftover-axis at `C` is `+1` while this Orient at `C` is `−1` | ATTEMPTED |
| nm2slx axis-cover | reuse cover reverse fail and cover face fail | cover does not report signed det; cover HOLDs at `B` and at `C` while Orient is `+1` and `−1` | ATTEMPTED |
| nm2axz axis-cover | reuse opposite-seed cover reverse hold and cover face hold | nm2axz HOLDs at `A`; here cover fails at `A` from leftover `{e_2}` | ATTEMPTED |
| nm2ax12z 1-in 2-out split | reuse opposite-seed split reverse hold and split face hold | opposite split HOLDs at `A`; here split fails at `A`; Cover and split do not score handedness | ATTEMPTED |
| leftover-empty fail | score reverse/face as leftover nonempty-equal | leftover reverse fails with these bits, leftover face fails with these bits; unique signed `O={+e_1,+e_3}` has empty leftover and Orient `+1` | ATTEMPTED |
| leftover of `M` alone | score `{e_1,e_2,e_3}` minus `Axis(M)` | leftover of `M` at `A` is `{e_1,e_2}` and at `B` is `{e_2,e_3}`, nonempty unequal | ATTEMPTED |
| leftover of `O` alone | score `{e_1,e_2,e_3}` minus `Axis(O)` | leftover of `O` at `A` is `{e_2,e_3}`, leftover reverse fails for unequal leftovers, not Orient fail from empty `O_prev` | ATTEMPTED |
| exist-opposite across probes | reuse signed reverse hold and face hold of `M` and of `O` | exist-opposite reverse of signed `O` fails with these bits; that object is signed opposite presence, not cyclic det | ATTEMPTED |
| opposite-pair presence in `O` | score reverse/face as both sides containing some `e` and `−e` | pair-presence fails at `A` and HOLDs at `B`; that object is pair presence, not cyclic det | ATTEMPTED |
| nmunopp untimed union | score reverse/face from `M ∪ O` | union is signed letters; Orient is integer sign of unique signed incoming and cyclic lex-smallest outgoing letters | ATTEMPTED |
| unique outgoing letter | replace mixed `O` by a singleton or `UNDEFINED` | mixed `O(B,τ1)` remains a set; unique-letter Orient is `UNDEFINED` at `B` while this Orient is `+1` | ATTEMPTED |
| unsigned incoming axis | replace signed `m` by the positive `Axis(M)` unit | on this member both fail at `A` and agree at `B` and at `C`; flipping `m` on unique signed `O={+e_1,+e_3}` from `+e_2` to `−e_2` flips Orient from `+1` to `−1` | ATTEMPTED |
| 2-in 1-out as `UNDEFINED` | treat `|Axis(M)|=2` cover as unformed | split fail is Orient fail, not UNDEFINED; `A` fails from leftover `{e_2}`, not from 2-in 1-out | ATTEMPTED |
| empty `O_i` as `UNDEFINED` | treat empty signed outgoing on an axis as unformed | empty `O_i` is Orient fail, not UNDEFINED | ATTEMPTED |
| 1-axis same-lock two-site seed | reuse `t(A)=3`, `t(C)=4`, mixed `M(A)`, Orient fail at `A` | different seed; second pair is a new seed, not a formed child; here `t(A)=2` and cover reverse fails | ATTEMPTED |
| y-probe Orient | score the four y-probes on this seed | y-probe reverse fails (`−1,+1`) and y-face fails; this letter is the four x-probes with Orient fail at `A` | ATTEMPTED |
| z-probe Orient | score the four z-probes on this seed | z-probe reverse fails and z-face HOLDs; this letter is the four x-probes | ATTEMPTED |
| score at `τ=t` | compose Orient at formation versus `t+1` | leftover of nmot2opp; Orient is fail at `t` and `fail/+1/−1/fail` at `t+1`; Do not score `τ=t` | ATTEMPTED |
| two-tick lock-count clock | score a lock-count clock across two ticks | different member; this display scores cyclic next/prev lex-smallest outgoing determinant orientation of own incoming and outgoing at `t+1` versus `t+2` | ATTEMPTED |
| mixed #7188 fail/fail | reuse z-symmetric mixed `M` reverse-fail face-fail | different process; this member reports reverse fail and face fail at both cuts on the two-axis same-lock x-probes with singleton `M` | ATTEMPTED |
| 1-axis same-lock two-site reuse | reuse `+e_1/+e_1` alone | different seed; this member is two disjoint same-lock pairs | ATTEMPTED |
| two-axis opposite seed | reuse `+e_1/−e_1` and `+e_2/−e_2` | different seed; neither pair is opposite; here `O(A)={+e_1}` | ATTEMPTED |
| sum of a set | replace Orient by a `Z^3` sum | the construction does not sum; `O(A)` sums to `+e_1` while Orient at `A` fails | ATTEMPTED |
| named-sign lettering | collapse `{±e_i}` to `{+,−}` | named-sign lettering lost the axis | ATTEMPTED |
| global later T | wait until `max t(A,B,C,D)` before reading | `τ1(q)=t(q)+1` and `τ2(q)=t(q)+2` are per-probe; no global T | ATTEMPTED |
| attach a formation member from already-recorded six-neighbor locks | form the probes by a neighbor-lock letter instead of perp-step | refused; not attached | ATTEMPTED |
| adopt bits into Admissibility | rewrite the local rule by the oriented frame | refused; displayed, not adopted | ATTEMPTED |

### N2 — wall independence

Missing physical adoption, missing identification of Orient with leftover of
`M` alone, missing identification of Orient with leftover-empty fail, missing
identification of Orient with existential opposite of signed locks, missing
identification of Orient with presence of an opposite pair in `O`, missing
identification of Orient with nm2chiralz lexicographic unsigned `o1,o2`,
missing identification of Orient with nm2oridetz unique signed `|O_i|=1`,
missing identification of Orient with nm2orionez lex-one, missing
identification of Orient with nm2oricyclz lex-largest cyclic next/prev,
missing identification of Orient with nm2oricyclslx lex-largest on this seed,
missing identification of Orient with nm2orichz opposite-pair leftover-axis,
missing identification of Orient with nmcover axis-cover, missing
identification of Orient with nm2slx axis-cover, missing identification of
Orient with nm2axz axis-cover, missing identification of Orient with
nm2ax12z 1-in 2-out split, missing identification of this freeze
with nm2oricyccz `t+1` alone, missing identification of Orient composition
with nm2simt2z `M` and `O` freeze, missing identification of this seed with
the 1-axis same-lock two-site seed, missing identification of this seed with
the two-axis opposite seed, and missing Record identification of
Orient reverse are distinct open premises. This note claims no complete wall
collection.

### N3 — hidden-condition scan

The host `B_3(0)`, two disjoint same-lock seed pairs `+e_1/+e_1` and
`+e_2/+e_2`, perpendicular step rule, incoming-step lock, own incoming set
and own outgoing dual from records with tick `<= τ`, per-probe `τ1=t+1`
and `τ2=t+2`, unsigned axis, cover as complementary occupation of
`{e_1,e_2,e_3}`, split as cover and `|Axis(M)|=1`, unique signed `m` when
split HOLDs, cyclic `e_next` and `e_prev` of the axis of `m`, lex-smallest
signed outgoing letter on each cyclic slot under `+e < −e`, integer
determinant sign, empty `O_next` or empty `O_prev` as Orient fail not
`UNDEFINED`, split fail as Orient fail not `UNDEFINED`, four x-probes with
non-seed `A`, second pair as a new seed not a formed child, mixed remains a
set, and composition as equality of Orient at the two cuts are declared.
No uniqueness of outgoing locks, no six-neighbor lock union as the scored
object, no lock-count clock, no global later T, no formation attachment
from already-recorded six-neighbor locks, and no Admissibility rewrite are
silently assumed.

### N4 — source residual matching

The current axiom memo supplies cubic sites, `M_2(C)`,
content-conditional-on-formation, and unreadable absence. The residual that
formation site, probability, and rate remain unsupplied is unchanged. The
Orient `fail`/`hold` reports do not close that residual.

### N5 — resolution and rhetoric audit

| Resolution | Executed | Not claimed |
|---|---|---|
| per element | unique signed incoming letter and cyclic next/prev lex-smallest outgoing letters of `Axis(M)` at a probe's `t+1` and `t+2` | no continuum alphabet |
| per site | `A,B,C,D` x-probes on `B_3(0)` only | no other cubic sites |
| per mode | no mode calculation | no spectral exhaustion |
| per block | four Orient reports at `t+1` and `t+2`, reverse/face at each cut, composition | no adopted content law |
| lattice wide | checked and not executed | no lattice-wide lettering rule |

### N6 — live partial-closure paths

Live routes include a later Record content map for Orient reverse/face, a
formation-rate rule, a later cut `t+3`, and a physical selector among 1-in
2-out frames. None is taken here.

### N7 — hostile steelman

**Steelman:** Orient reverse fail and face fail are only leftover of
nm2oricyccz cyclic lex-smallest on opposite z; they are only leftover of
nm2oricyclslx lex-largest on this seed; they are only leftover of
nm2orionez lex-one on this seed; they are only leftover of nm2slx cover;
nm2chiralz unsigned `o1,o2` already answers mixed `O`; unique signed
`|O_i|=1` already answers mixed `O`; cover reverse and split reverse already
answer the three-axis occupation; leftover of `M` alone already answers
reverse; leftover of `O` alone already answers reverse; exist-opposite of
signed `O` already answers reverse; opposite-pair leftover-axis already
answers handedness; mixed #7188 already reported fail/fail; the second pair
is only the formed child `(0,0,1)` of the 1-axis seed; unique outgoing
letters should be required; unsigned incoming axis already gives the same
signs because each `M` letter is the positive unit; because `M` and `O`
freeze, composition is nm2simt2z; because reverse fail and face HOLD at
both cuts, composition is only bit-stability; and nm2oricyccz already
answered reverse-and-face orientation.

**Answer:** Leftover empty is unsigned unoccupied directions of `M` and `O`
together. Leftover-empty fail scores leftover `{e_2}` at `A` and empty
leftover at `B` as reverse fail and face fail. Orient reverse fails
because `Orient(A)` is fail and `Orient(B)=+1`. Orient face fails because
`Orient(C)=−1` and `Orient(D)` is fail. Cover and split fail reverse and
fail face on this member and do not score that signed pair at `B` and at
`C`. nm2oricyccz on the opposite seed has `Orient(A)=+1` with split HOLD
and reverse HOLDs; here `O(A)={+e_1}`, split fails, `Orient(A)` is fail,
and reverse fails. nm2oricyclslx lex-largest on this same-lock seed has
Orient `fail,−1,+1,fail`; this display has `fail,+1,−1,fail`. nm2orionez
lex-one on this same-lock seed has Orient `fail,+1,−1,fail`; those columns
are axis-order, and `det(+e_2,+e_1,+e_3)=−1` while cyclic
`det(+e_2,+e_3,+e_1)=+1`. nm2slx cover reverse fails from leftover `{e_2}`
at `A` but does not report `+1` at `B` and `−1` at `C`. Lexicographic
unsigned `o1,o2` reverse fails with `fail,+1` and unsigned Orient at `C`
is `+1` while this Orient at `C` is `−1`. Unique signed `|O_i|=1` reverse
fails and face fails because mixed opposite pairs occupy `O` at `B` and at
`C`; this Orient at `B` is `+1`. Opposite-pair leftover-axis reverse fails
and face fails; leftover-axis at `C` is `+1`. Presence of an opposite pair
in `O` fails at `A` and HOLDs at `B`. Leftover of `M` alone at `A` is
`{e_1,e_2}` and at `B` is `{e_2,e_3}`: nonempty unequal. Leftover of `O`
alone at `A` is `{e_2,e_3}`. Exist-opposite reverse of signed `O` fails
with these bits. Unique outgoing letters would assign `UNDEFINED` at mixed
`O(B)`; this Orient at `B` is `+1`. On unique signed `O={+e_1,+e_3}`
leftover is empty while Orient is `+1`, so leftover-empty fail is not this
predicate. Mixed #7188 is a different z-symmetric process with mixed `M`.
The second pair is a new seed, not a formed child: `(0,0,1)` is recorded
at tick 0 with lock `+e_2`. nm2oricyccz scores only `τ=t+1` on the
opposite seed. nm2ocyccslx scores only `τ=t+1` on these x-probes.
nm2simt2z scores equality of `M` and of `O`. Reverse/face bit-stability
can HOLD while a probe sign flips. Reverse oriented frame is HOLD iff
equal `±1` signs at `A` and at `B` at that cut, not leftover of
nm2oricyccz cyclic lex-smallest and not leftover of nm2slx axis-cover.
Composition of Orient: hold.

### N8 — cross-cycle echo

nm2slx axis-cover on this two-axis same-lock seed reported cover fail at
`A` and at `D` from leftover `{e_2}`, cover HOLD at `B` and at `C`, reverse
fail, and face fail. nm2oricyccz cyclic lex-smallest on the two-axis
opposite seed reported `Orient(A)=+1` with split HOLD, reverse hold, and
face hold at `t+1` alone. nm2ocyccslx cyclic lex-smallest on these
x-probes reported Orient `fail,+1,−1,fail`, reverse fail, and face fail at
`t+1` alone. nm2oricyclslx lex-largest on this same-lock seed reported
Orient `fail,−1,+1,fail`, reverse fail, and face fail. nm2orionez lex-one
on this same-lock seed reported Orient `fail,+1,−1,fail`, reverse fail,
and face fail. nm2axz cover on the opposite seed reported cover HOLD at
each of the four z-probes, reverse hold, and face hold. nm2ax12z 1-in
2-out split on the opposite seed reported split HOLD at each of the four
z-probes, reverse hold, and face hold. Leftover axis reported leftover
`{e_2}` at `A` and at `D` and empty leftover at `B` and at `C`, leftover
reverse fail, and leftover face fail. The four y-probes of this same seed
reported cyclic lex-smallest Orient `−1` at `A` from `{+e_2,−e_3}` and
Orient fail at `D` from split fail, so y-reverse fails and y-face fails.
The four z-probes of this same seed reported reverse fail and face hold.
This note is not those displays: it reports cyclic next/prev lex-smallest
outgoing determinant orientation of the 1-in 2-out frame of `M` and `O` at
`τ1=t+1` versus `τ2=t+2` on the two-axis same-lock seed, with `t(A)=2`,
`t(B)=1`, `t(C)=3`, and `t(D)=2`, `Orient` fail,`+1`,`−1`,fail at both
cuts, reverse fail at both cuts, face fail at both cuts, and composition
hold. Cover and split do not score handedness.

**Gate disposition:** PASS for the cyclic-next-prev-lex-smallest-outgoing-determinant `t+1` versus `t+2`
reverse/face reports and displayed composition above. FAIL / DO NOT SHIP
for “the predicate equals the named sign,” “the predicate equals the unique
singleton lock vector,” “the predicate equals six-neighbor lock union,”
“the predicate equals leftover-empty fail,” “the predicate equals leftover
of `M` alone,” “the predicate equals leftover of `O` alone,” “the
predicate equals exist-opposite HOLD,” “the predicate equals opposite-pair
presence in `O`,” “the predicate equals nm2chiralz lexicographic unsigned
`o1,o2` HOLD,” “the predicate equals nm2oridetz unique signed HOLD,” “the
predicate equals nm2orionez lex-one HOLD,” “the predicate equals
nm2oricyclz lex-largest HOLD,” “the predicate equals nm2oricyclslx
lex-largest HOLD,” “the predicate equals nm2orichz opposite-pair
leftover-axis HOLD,” “the predicate equals nmcover axis-cover HOLD,” “the
predicate equals nm2slx axis-cover HOLD,” “the predicate equals nm2axz
axis-cover HOLD,” “the predicate equals nm2ax12z 1-in 2-out split HOLD,”
“the predicate equals nm2oricyccz `t+1` alone,” “the predicate equals
nm2simt2z `M` and `O` freeze,” “the predicate equals the 1-axis same-lock
two-site seed,” “the predicate equals the two-axis opposite seed,” “the
predicate equals nmunopp union,” “bits are Admissibility,” “split fail is
UNDEFINED,” “empty `O_next` or empty `O_prev` is UNDEFINED,” “reverse
oriented frame holds,” “face oriented frame holds,” or “composition of
Orient fails.”

## Primary runner

The paired runner builds Euclidean `B_3(0)`, runs the two-axis same-lock
perp-step incoming-lock process, reads each probe's own earliest incoming
set and own outgoing dual from the record prefix at that probe's `t+1` and
`t+2`, reports split of the pair, reports the unique signed incoming letter,
the cyclic axis index, and the lex-smallest `o_next` and `o_prev`, reports
the integer determinant and its sign at both cuts, lists new records in
`B_3(0)` between `t` and `t+1` and between `t+1` and `t+2` that meet a
probe's six-neighbors, and checks Theorems 1--3. It also checks that Orient
is fail,`+1`,`−1`,fail at `A,B,C,D` at both cuts, that reverse fails at both
cuts and face fails at both cuts while leftover-empty reverse fails, that
composition HOLDs, that split fail is Orient fail not `UNDEFINED`, that
empty `O_next` or empty `O_prev` is Orient fail not `UNDEFINED`, that
nm2oricyccz opposite-seed Orient at `A` is `+1` while this Orient at `A`
is fail and that opposite reverse HOLDs while this reverse fails, that the
1-axis same-lock two-site seed is a different member with cover reverse
HOLD, that leftover-empty fail is a different predicate, that leftover of
`M` alone and leftover of `O` alone are different objects, that mixed
sets remain sets, that unique-letter Orient is `UNDEFINED` at mixed `O`
at `B`, that lexicographic unsigned Orient at `C` is `+1` while this Orient
at `C` is `−1`, that unique signed Orient at `B` fails while this Orient
at `B` is `+1`, that opposite-pair leftover-axis Orient at `C` is `+1`
while this Orient at `C` is `−1`, that lex-largest cyclic Orient at `B`
is `−1` while this Orient at `B` is `+1`, that the construction does not
sum, that a formation member from already-recorded six-neighbor locks is
not attached, that the second pair is a new seed not a formed child, that
neither pair is opposite, that the y-probes and z-probes of this seed are
not this letter, that `τ=t` is not scored, and that the display is not the
two-tick lock-count clock composition. No runner cache is written.
