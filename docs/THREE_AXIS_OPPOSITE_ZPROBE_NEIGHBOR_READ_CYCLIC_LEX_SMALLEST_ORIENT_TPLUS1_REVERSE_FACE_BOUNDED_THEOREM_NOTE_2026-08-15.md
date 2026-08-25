---
claim_id: three_axis_opposite_zprobe_neighbor_read_cyclic_lex_smallest_orient_tplus1_reverse_face_bounded_theorem_note_2026-08-15
claim_type: bounded_theorem
claim_scope: "Neighbor-read of the cyclic lex-smallest orientation at t+1 on the four z-probes of the three-axis opposite seed, and reverse/face from that, are reported. Displayed, not adopted."
upstream_dependencies:
  - minimal_axioms
runner: scripts/three_axis_opposite_zprobe_neighbor_read_cyclic_lex_smallest_orient_tplus1_reverse_face_2026_08_15.py
---

# Neighbor-Read Of Cyclic Lex-Smallest Orientation At t+1 Reverse And Face On Four Three-Axis Opposite Z-Probes

> **Key terms used in this doc** are indexed A-Z at `docs/KEY_TERMINOLOGY.md`;
> each row points to the canonical source-of-truth doc.

**Date:** 2026-08-15
**Type:** bounded_theorem
**Scope:** neighbor-read of the cyclic next/prev lex-smallest outgoing
determinant orientation of the 1-in 2-out frame of `M` and `O` at each
probe's `τ=t+1`, and reverse/face from that neighbor-read, on the four
z-probes of the three-axis opposite seed in `B_3(0)={n:n·n<=9}`. z-probes
as nm2axz. Orient as nm2oricyccz. Let `t(q)` be the formation tick of
probe `q`. Let `τ(q)=t(q)+1`. `M(q,τ)` is the set of earliest incoming
nearest-neighbor steps at `q` using only records with tick `<= τ`. Seeds
are a singleton seed letter. `O(q,τ)` is the outgoing dual of `M`: the
set of `e` in `{±e_1,±e_2,±e_3}` such that `q+e` is formed and `e` is in
`M(q+e,τ)`. Unformed at `τ` is `UNDEFINED`. Empty `O` is empty, not
`UNDEFINED`. Axis of a defined lock set `S` is `Axis(S)={e_i | some ±e_i
in S}`. Cover HOLDs at `q` if and only if `Axis(M)` intersect `Axis(O)`
is empty and `Axis(M)` union `Axis(O)` equals `{e_1,e_2,e_3}`. Split
HOLDs at `q` if and only if cover HOLDs and `|Axis(M)|=1` (hence
`|Axis(O)|=2`). When split HOLDs, `m` is the unique vector in `M`. Let
`i` in `{1,2,3}` be the axis index of `m`. `e_next = e_{i+1}` with
`3+1→1`. `e_prev = e_{i-1}` with `1−1→3`. `O_next = O ∩ {±e_next}`.
`O_prev = O ∩ {±e_prev}`. If either empty, Orient fails, not
`UNDEFINED`. Order `+e < −e`. `o_next` is the lex-smallest vector in
`O_next` (hence `+e` if both signs). `o_prev` likewise. `Orient(q)` is
the sign of the integer determinant of columns `m`, `o_next`, `o_prev`.
If split fails, Orient fails, not `UNDEFINED`. Neighbor-read HOLDs at
`q` if and only if `Orient(q)` is `±1` and some formed 6-NN `r` has
`Orient(r)=Orient(q)` both `±1`. If Orient fails at `q`, neighbor-read
fails, not `UNDEFINED`. Unformed `q` is `UNDEFINED`. Reverse HOLDs if
and only if neighbor-read HOLDs at `A` and at `B`. Face HOLDs if and
only if neighbor-read HOLDs at `C` and at `D`. This is not leftover of
two-axis neighbor-read of those Orient signs, which fails at `D`. This
is not leftover of three-axis cyclic lex-smallest Orient reverse hold
and face hold from equal `±1` signs. This is not leftover of
nm2oricycl3z lex-largest cyclic next/prev. This is not leftover of
nm2oreadz neighbor-read of O. This is not leftover of nm2readz
neighbor-read of M. This is not leftover of nm2axz axis-cover. This is
not leftover of nm2ax12z 1-in 2-out split. Occupancy of sites is not
used. Named-sign lettering is not used. Uniqueness is not required.
Mixed remains a set. Displayed, not adopted. Do not write into
Admissibility. Do not attach L1.
**Audit-status authority:** independent audit lane only. This note authors no
audit verdict and predicts none.
**Primary runner:**
[`scripts/three_axis_opposite_zprobe_neighbor_read_cyclic_lex_smallest_orient_tplus1_reverse_face_2026_08_15.py`](../scripts/three_axis_opposite_zprobe_neighbor_read_cyclic_lex_smallest_orient_tplus1_reverse_face_2026_08_15.py)

Framework input:

- [`MINIMAL_AXIOMS_2026-06-29.md`](MINIMAL_AXIOMS_2026-06-29.md) supplies
  cubic-lattice sites `Z^3` with nearest-neighbor adjacency, the one-site
  algebra `M_2(C)`, and the Record sentences that records form and that a
  present record locks exactly one admissible local possibility.

Everything after that quoted input is a finite displayed process on `B_3(0)`
and the four named z-probes. Incoming lock letters are unit nearest-neighbor
steps. `O` is the outgoing dual of those incoming sets at the per-probe cut
`τ=t+1`. Orient is the cyclic next/prev lex-smallest outgoing determinant
of the 1-in 2-out frame, as in nm2oricyccz. Neighbor-read asks whether a
formed six-neighbor recovers that Orient sign as `±1`, without being Orient
itself. Reverse and face are scored on neighbor-read HOLD at the paired
probes. Equal Orient signs at `A` and at `B` are a different readout and
are not used as the object. Neighbor-read of `O` as sets is a different
readout and is not used. Neighbor-read of `M` is a different readout and
is not used. Lex-largest cyclic next/prev is a different readout and is
not used. Two-axis neighbor-read of the same Orient letter is a different
seed and is not used. Named signs `{+,−}` are a coarser readout and are
not used. A singleton unique lock letter is a different readout and is
not used as the object. Axis-cover of `M` and `O` is a different readout
and is not used. 1-in 2-out split is a different readout and is not used.
A `Z^3` sum of those locks is a different readout and is not used.
Occupancy of sites is not used. A six-neighbor star is not the letter.

## Machine status and trace

```yaml
actual_current_surface_status: bounded-support
target_claim_type: bounded_theorem
claim_type_reason: "Exact report of neighbor-read of cyclic lex-smallest Orient at t+1 on the four z-probes of the three-axis opposite seed, neighbor-read bits at each probe, reverse fail and face fail from those bits; uniqueness of outgoing locks is not claimed and the bits are not adopted."
trace_class: frontier_discovery
target_claim_id: three_axis_opposite_zprobe_neighbor_read_cyclic_lex_smallest_orient_tplus1_reverse_face
target_blocker_text: "display neighbor-read of cyclic lex-smallest Orient at t+1 on the four z-probes of the three-axis opposite seed, and reverse/face from that, HOLD iff some formed 6-NN recovers the same +/-1 Orient sign"
source_of_blocker_text: handoff
reachability_to_target: advances
artifact_role: theorem
next_trace_action: "Keep neighbor-read of cyclic lex-smallest Orient at t+1 displayed; do not write neighbor-read into Admissibility, do not reduce to three-axis lex-smallest Orient reverse/face, do not reduce to two-axis neighbor-read of Orient, do not reduce to neighbor-read of O, do not reduce to neighbor-read of M, do not reduce to lex-largest cyclic next/prev, do not reduce to axis-cover or 1-in 2-out split, and do not attach L1."
conditional_surface_status: "exact on B_3(0) for neighbor-read of cyclic lex-smallest Orient at t+1 on the four z-probes of the three-axis opposite seed and reverse/face from that; displayed, not adopted"
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

No larger host is used. The four z-probes are the only sites whose
neighbor-read of cyclic lex-smallest Orient is scored:

```text
A = (0,0,1),  B = (1,1,1),  C = (0,0,2),  D = (1,0,1).
```

These are not the y-probes `A=(0,1,0)`, `B=(1,1,1)`, `C=(0,2,0)`,
`D=(1,1,0)`. These are not the x-probes `A=(1,0,0)`, `B=(1,1,1)`, `C=(2,0,0)`,
`D=(1,1,0)`. `A` is a seed of the second opposite pair. `C` of the
x-probes is the third-pair seed `(2,0,0)`. z-probes as nm2axz.

Lock alphabet of the displayed process: `{±e_i}` with `i` in `{1,2,3}`.

Seed: three disjoint opposite pairs recorded at formation tick 0. Origin
locks `+e_1`. Site `(0,1,0)` locks `−e_1`. Site `(0,0,1)` locks `+e_2`.
Site `(0,1,1)` locks `−e_2`. Site `(2,0,0)` locks `+e_3`. Site `(2,1,0)`
locks `−e_3`. The second pair is a new seed, not a formed child of the
first pair. The third pair is a new seed, not a formed child: on the
two-axis opposite seed those sites form at tick 3 locking `+e_1`. This
seed is not the two-axis opposite seed of nm2oricyccrdz. This seed is
not the 1-axis opposite two-site seed `{0,(0,1,0)}` with only
`+e_1/−e_1`. This seed is not the perp two-site seed `+e_1/+e_2`. This
seed is not the z-symmetric three-site seed `{0,(0,0,1),(0,0,-1)}`. This
seed is not the y-symmetric three-site seed that also records `(0,-1,0)`
at tick 0.

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

## Named neighbor-read of cyclic lex-smallest Orient at `τ=t+1`

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
not require `O` to be a singleton. It does not sum either set. It does not
replace `O` by `M`. It does not wait for a global later T. Occupancy of
sites is not used. O is not M.

Unsigned axis of a defined lock set:

```text
Axis(S) = { e_i | some ±e_i in S }.
```

Cover HOLDs iff `Axis(M)` intersect `Axis(O)` is empty and the union equals
`{e_1,e_2,e_3}`. Split HOLDs iff cover HOLDs and `|Axis(M)|=1`. Split HOLD
required for Orient. When split HOLDs, `m` is the unique signed letter in
`M`. Let `i` in `{1,2,3}` be the axis index of `m`. `e_next = e_{i+1}` with
`3+1→1`. `e_prev = e_{i-1}` with `1−1→3`. `O_next = O ∩ {±e_next}`.
`O_prev = O ∩ {±e_prev}`. If either is empty, Orient fails, not `UNDEFINED`.
Order `+e < −e`. `o_next` is the lex-smallest vector in `O_next` (hence `+e`
if both signs). `o_prev` likewise. `Orient(q)` is the sign of the integer
determinant of columns `m`, `o_next`, `o_prev`. If split fails, Orient
fails, not `UNDEFINED`. `UNDEFINED` if `M` or `O` is `UNDEFINED`. This is
Orient as nm2oricyccz.

Neighbor-read at a formed probe at the same cut:

```text
neighbor-read(q) HOLDs iff Orient(q) is ±1 and some formed 6-NN r
has Orient(r)=Orient(q) both ±1.
```

If `q` is unformed at `τ`, then neighbor-read is `UNDEFINED`. If Orient
fails at `q`, neighbor-read fails, not `UNDEFINED`. Else if no formed
six-neighbor recovers the same `±1` sign, neighbor-read fails. The probe
is not counted as its own neighbor. Empty matching is fail, not
`UNDEFINED`. Mixed remains a set: mixed `O` may still yield a defined
Orient sign, and that sign may still match a neighbor.

Reverse neighbor-read holds if and only if neighbor-read HOLDs at `A` and
at `B`. Face neighbor-read holds if and only if neighbor-read HOLDs at `C`
and at `D`. Either side `UNDEFINED` is `UNDEFINED`. Else if both sides HOLD,
reverse or face HOLDs. Else fail.

Identifying neighbor-read of Orient with three-axis cyclic lex-smallest
Orient reverse/face is refused: Orient reverse HOLDs and Orient face HOLDs,
while neighbor-read reverse fails and neighbor-read face fails. Identifying
this letter with two-axis neighbor-read of the same Orient is refused:
two-axis neighbor-read fails at `D`; this letter HOLDs at `D`. Identifying
neighbor-read of Orient with neighbor-read of `O` is refused: both HOLD
at `A`, but the matching neighbor at `A` is the origin for Orient and the
partner seed `(0,1,1)` for `O`, and neighbor-read of `O` fails at `D`.
Identifying neighbor-read of Orient with neighbor-read of `M` is refused:
neighbor-read of `M` is fail at `A` and hold at `B`, `C`, and `D`.
Identifying neighbor-read of Orient with lex-largest cyclic neighbor-read
is refused: lex-largest neighbor-read is fail at `A` and hold at `B`.

## Theorem 1 — ticks, `M`, `O`, Orient, neighbor-read at `τ=t+1`

On this process the four z-probes form. Compare to three-axis cyclic
lex-smallest Orient: that leftover reports Orient `+1,+1,−1,−1`, reverse
hold, and face hold. Compare to two-axis neighbor-read of those Orient
signs: that leftover reports hold only at `A` by matching the origin,
fail at `D`, reverse fail, and face fail. Compare to nm2oreadz
neighbor-read of `O`: that leftover reports hold at `A` by matching the
partner seed `(0,1,1)` as equal outgoing sets. Compare to nm2readz
neighbor-read of `M`: that leftover reports fail at `A` and hold at `B`,
`C`, and `D`. This display reads whether a formed six-neighbor recovers
the cyclic lex-smallest Orient sign on the three-axis opposite seed:

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
O(B, τ) = {+e_2, +e_3}
O(C, τ) = {+e_1, −e_1, −e_2}
O(D, τ) = {−e_2, +e_3}
Orient(A) = +1
Orient(B) = +1
Orient(C) = −1
Orient(D) = −1
neighbor-read(A) = hold
neighbor-read(B) = fail
neighbor-read(C) = fail
neighbor-read(D) = hold
formed 6-NN of A at τ: (1, 0, 1)=fail, (-1, 0, 1)=fail, (0, 1, 1)=−1, (0, -1, 1)=UNDEFINED, (0, 0, 2)=fail, (0, 0, 0)=+1
formed 6-NN of B at τ: (2, 1, 1)=UNDEFINED, (0, 1, 1)=−1, (1, 2, 1)=fail, (1, 0, 1)=−1, (1, 1, 2)=fail, (1, 1, 0)=fail
formed 6-NN of C at τ: (1, 0, 2)=fail, (-1, 0, 2)=fail, (0, 1, 2)=+1, (0, -1, 2)=fail, (0, 0, 1)=+1
formed 6-NN of D at τ: (2, 0, 1)=UNDEFINED, (0, 0, 1)=+1, (1, 1, 1)=+1, (1, -1, 1)=fail, (1, 0, 2)=fail, (1, 0, 0)=−1
matching 6-NN of A: (0, 0, 0)
matching 6-NN of B: none
matching 6-NN of C: none
matching 6-NN of D: (1, 0, 0)
```

`A` is a seed at tick 0 with seed letter `+e_2`. The partner of that pair,
`(0,1,1)`, is also a seed at tick 0 with seed letter `−e_2`. At `τ=1` those
two seeds share the same outgoing set `{+e_1, −e_1, +e_3}`, so neighbor-read
of `O` HOLDs at `A` by matching `(0,1,1)`. Cyclic lex-smallest Orient at
the partner is `−1`, because `m=−e_2` while `m(A)=+e_2`, so the partner
does not recover `Orient(A)=+1`. The origin `(0,0,0)` at the same cut has
`M={+e_1}`, `O={−e_2, −e_3}`, and Orient `+1`, so neighbor-read of Orient
HOLDs at `A` by matching the origin.

The third pair is what two-axis neighbor-read lacked. Site `(2,0,0)` is a
seed at tick 0 locking `+e_3`. A perpendicular step `−e_1` forms `(1,0,0)`
at tick 1 locking `−e_1`. At `D`'s cut `τ=2`, that site has `M={−e_1}`,
`O={−e_2, −e_3}`, and Orient `−1`, so neighbor-read of Orient HOLDs at `D`
by matching `(1,0,0)`. On the two-axis opposite seed, `(1,0,0)` forms at
tick 2 with empty `O` at `D`'s cut, Orient fails there, and neighbor-read
fails at `D`. The third pair also drops `−e_3` from `O(B,τ)` and from
`O(D,τ)` relative to the two-axis leftover. Mixed remains a set:
`O(A,τ)` has three outgoing steps and still yields Orient `+1`. Unique
letters would assign `UNDEFINED` at mixed `O`. Here uniqueness is not
required. At `t`, `O` is empty at each probe, split fails, Orient fails,
and neighbor-read fails, not `UNDEFINED`. At `τ=t+1`, Orient is `±1` at
each probe. `M` is frozen from `t` to `t+1`; `O` is not. O is not M.

`B` still has no formed six-neighbor with Orient `+1`. Neighbor `(2,1,1)`
of `B` forms only at tick 3 and is `UNDEFINED` at `τ=2`. `C` still has no
formed six-neighbor with Orient `−1`: `(0,1,2)` and `A` are `+1`.

On the one-axis opposite two-site seed, `A=(0,0,1)` is a formed child at
tick 1 locking `+e_3`. That is leftover of the first pair. Here both
`(0,0,1)` and `(0,1,1)` are seeds of a second opposite pair on a second
axis, and `(2,0,0)` and `(2,1,0)` are seeds of a third opposite pair on a
third axis. Neighbor-read of cyclic lex-smallest Orient on that leftover
two-site seed has reverse hold, not this reverse fail.

Empty `O` at a neighbor that is formed at `τ` yields Orient fail, not
`UNDEFINED`, and does not match a `±1` probe sign. Unformed at `τ` is
`UNDEFINED` and is not a match.

## Theorem 2 — reverse from neighbor-read of Orient at `τ`

Reverse neighbor-read holds if and only if neighbor-read HOLDs at `A` and
at `B`. Neighbor-read HOLDs at `A` and fails at `B`. Reverse fails. This is
HOLD iff neighbor-read at both reverse probes, not leftover of three-axis
cyclic lex-smallest Orient reverse hold from `Orient(A)=Orient(B)=+1`.

Reverse neighbor-read at τ: fail

Both sides are defined, so this is not `UNDEFINED`. Three-axis lex-smallest
Orient reverse HOLDs because both signs are `+1`. Two-axis neighbor-read
of Orient also has reverse fail, but from fail at `D` as well as at `B`,
not from hold at `D`. Neighbor-read of `O` also has reverse fail, but from
matching the partner seed at `A`, not the origin. Neighbor-read of `M` also
has reverse fail, but from the opposite pair of bits: fail at `A` and hold
at `B`. Lex-largest cyclic neighbor-read reverse fails from fail at `A`
and hold at `B`, the opposite reverse pair from this letter. Axis-cover
reverse HOLDs. 1-in 2-out split reverse HOLDs. Those leftovers are not this
display.

Reverse fails.

## Theorem 3 — face from neighbor-read of Orient at `τ`

Face neighbor-read holds if and only if neighbor-read HOLDs at `C` and at
`D`. Neighbor-read fails at `C` and HOLDs at `D`. Face fails.

Face neighbor-read at τ: fail

Displayed, not adopted. The bits are not written into Admissibility.
Do not write into Admissibility. Do not attach L1.

Three-axis lex-smallest Orient face HOLDs because `Orient(C)=Orient(D)=−1`.
Two-axis neighbor-read of Orient has face fail from fail at both `C` and
`D`. Neighbor-read of `M` has face hold. Axis-cover face HOLDs. 1-in 2-out
split face HOLDs. This display scores neighbor-read of cyclic lex-smallest
Orient, which fails at `C` and HOLDs at `D` by matching `(1,0,0)`, so face
fails.

On the same seed the four y-probes give neighbor-read hold at `A` and at
`C`, so reverse fail and face fail, but from hold at `C`, not fail at `C`.
The four x-probes hold at `A=(1,0,0)` and fail at `B`, `C`, and `D`. Those
probe-direction readouts are not this z-probe display. The third-pair seed
`(2,0,0)` is x-probe `C`, not a z-probe.

Face fails.

## What this note does not claim

- It does not select a unique incoming or outgoing lock.
- It does not reduce lock vectors to named signs `{+,−}`.
- It does not require neighbor-read sides to be singletons.
- It does not sum either set.
- It does not replace neighbor-read of Orient by three-axis lex-smallest equal-sign reverse/face.
- It does not replace neighbor-read of Orient by two-axis neighbor-read of Orient.
- It does not replace neighbor-read of Orient by neighbor-read of `O`.
- It does not replace neighbor-read of Orient by neighbor-read of `M`.
- It does not replace neighbor-read of Orient by nm2oricycl3z lex-largest cyclic next/prev.
- It does not replace neighbor-read by axis-cover of `M` and `O`.
- It does not replace neighbor-read by 1-in 2-out split.
- It does not replace `O` by `M`.
- It does not replace neighbor-read by locks of six-neighbors.
- It does not use a six-neighbor star as the letter.
- It does not wait for a global later T.
- It does not attach a formation member from already-recorded six-neighbor
  locks.
- It does not reprint three-axis lex-smallest Orient reverse hold and face hold.
- It does not reprint two-axis neighbor-read fail at `D`.
- It does not reprint nm2oreadz neighbor-read of `O`.
- It does not reprint nm2readz neighbor-read of `M`.
- It does not reprint nm2axz axis-cover reverse hold and face hold.
- It does not reprint nm2ax12z 1-in 2-out reverse hold and face hold.
- It does not treat the second opposite pair as a formed child of the first.
- It does not treat the third opposite pair as a formed child.
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
three-axis opposite process, neighbor-read of cyclic lex-smallest Orient at
`t+1`, and the reverse/face bits from that neighbor-read are displayed
theorem-domain data.

## Exact target and obligation graph

| Obligation | Status |
|---|---|
| current Lattice / Admissibility / Record premises | quoted; no edit |
| perp-step incoming-lock process on `B_3(0)` | displayed; three disjoint opposite pairs `+e_1/−e_1`, `+e_2/−e_2`, and `+e_3/−e_3` |
| ticks `t(A)`, `t(B)`, `t(C)`, `t(D)` | Theorem 1; `0`, `1`, `1`, `1` |
| `M` at `τ=t+1` | Theorem 1; frozen equal to `M` at `t` |
| `O` at `τ=t+1` | Theorem 1; HOLDING outgoing dual; `−e_3` dropped at `B` and `D` versus two-axis |
| Orient at `τ` | Theorem 1; `+1`, `+1`, `−1`, `−1` as nm2oricyccz |
| Orient at formed 6-NN | Theorem 1; reported at each eventually-formed neighbor |
| neighbor-read bit at `τ` | Theorem 1; hold, fail, fail, hold |
| reverse from neighbor-read at `τ` | Theorem 2; `fail` |
| face from neighbor-read at `τ` | Theorem 3; `fail` |
| unique outgoing lock | not required |
| occupancy of sites as the letter | not used |
| named-sign `{+,−}` letter | not used |
| singleton unique lock-vector letter | not used as the object; mixed remains a set |
| `Z^3` sum of the lock set | not used; no aggregation |
| six-neighbor star as the letter | not used |
| leftover of three-axis lex-smallest Orient reverse/face | not this neighbor-read display |
| leftover of two-axis neighbor-read of Orient | not this seed; that leftover fails at `D` |
| leftover of nm2oreadz neighbor-read of `O` | not this display |
| leftover of nm2readz neighbor-read of `M` | not this display |
| leftover of nm2oricycl3z lex-largest | not this display |
| leftover of nm2axz axis-cover | not this neighbor-read display |
| leftover of nm2ax12z 1-in 2-out | not this neighbor-read display |
| one-axis opposite leftover of the second pair | not this seed |
| two-axis leftover of the third pair | not this seed |
| y-probe or x-probe neighbor-read on this seed | not this letter |
| global later T | not used |
| neighbor-read as Admissibility content | not adopted |
| formation site / probability / rate | open |
| physical Record readout of the bits | open |

## Value gate (V1–V5)

| # | Answer |
|---|---|
| V1 | It answers the first-display question: neighbor-read of cyclic lex-smallest Orient at `t+1` on the four z-probes of the three-axis opposite seed, and reverse/face from that. |
| V2 | Current main has no landed neighbor-read reverse/face of cyclic lex-smallest Orient on these four z-probes of this three-axis opposite seed. |
| V3 | Neighbor-read reports at one cut and the two reverse/face bits are independently finite and exact. |
| V4 | The theorem is more than a restatement of Record because it reads whether a formed six-neighbor recovers the cyclic lex-smallest Orient sign at the same `t+1` cut, HOLDs at `A` by matching the origin and at `D` by matching `(1,0,0)` from the third pair, and fails reverse while three-axis lex-smallest Orient reverse HOLDs. |
| V5 | It is not an adopted content rule: the bits remain displayed. |

## No-go discipline gate

The negative content is narrow: the display does not write those bits into
Admissibility, does not reduce them to named signs, does not require a
unique lock, does not replace neighbor-read of Orient by three-axis
lex-smallest equal signs, does not replace neighbor-read of Orient by
two-axis neighbor-read of Orient, does not replace neighbor-read of Orient
by neighbor-read of `O`, does not replace neighbor-read of Orient by
neighbor-read of `M`, does not replace neighbor-read by lex-largest cyclic
next/prev, and does not identify this display with axis-cover or 1-in
2-out split. No global impossibility is claimed.

### N1 — materially distinct routes

| Route | Attempt | Why it fails here | Marker |
|---|---|---|---|
| three-axis lex-smallest equal Orient signs | score reverse/face from `Orient(A)=Orient(B)` both `±1` | Orient reverse HOLDs and Orient face HOLDs; neighbor-read reverse fails and neighbor-read face fails | ATTEMPTED |
| two-axis neighbor-read of Orient | reuse the two-axis opposite seed | two-axis neighbor-read fails at `D`; this letter HOLDs at `D` by matching `(1,0,0)` | ATTEMPTED |
| neighbor-read of `O` | score reverse/face from equal outgoing sets | neighbor-read of `O` HOLDs at `A` by matching `(0,1,1)` and fails at `D`; this letter HOLDs at `A` by matching `(0,0,0)` and HOLDs at `D` | ATTEMPTED |
| neighbor-read of `M` | score reverse/face from equal incoming sets | neighbor-read of `M` is fail/hold/hold/hold and face hold; this letter is hold/fail/fail/hold and face fail | ATTEMPTED |
| nm2oricycl3z lex-largest cyclic | reuse lex-largest neighbor-read | lex-largest neighbor-read is fail/hold/fail/hold; this letter is hold/fail/fail/hold | ATTEMPTED |
| nm2axz axis-cover | reuse cover reverse hold and face hold | cover HOLDs at each z-probe; neighbor-read of Orient HOLDs only at `A` and `D` | ATTEMPTED |
| nm2ax12z 1-in 2-out | reuse split reverse hold and face hold | split HOLDs at each z-probe; neighbor-read of Orient HOLDs only at `A` and `D` | ATTEMPTED |
| unique letter | replace mixed sets by a singleton or `UNDEFINED` | mixed `O(A,τ)` remains a set; Orient is `+1` and neighbor-read still HOLDs at `A` | ATTEMPTED |
| named-sign lettering | collapse `{±e_i}` to `{+,−}` | named-sign lettering lost the outgoing set and the cyclic columns | ATTEMPTED |
| y-probe neighbor-read | score the four y-probes on this seed | y-probe neighbor-read HOLDs at `C`; this letter fails at z-probe `C` | ATTEMPTED |
| x-probe neighbor-read | score the four x-probes on this seed | x-probe `A` is `(1,0,0)` and x-probe `C` is the third-pair seed; this letter scores z-probes | ATTEMPTED |
| one-axis leftover | treat `(0,0,1)` and `(0,1,1)` as formed children of `+e_1/−e_1` | those children lock `+e_3` at tick 1; here they are seeds locking `+e_2/−e_2` at tick 0; leftover reverse HOLDs | ATTEMPTED |
| two-axis leftover of the third pair | treat `(2,0,0)` and `(2,1,0)` as formed children | those children lock `+e_1` at tick 3; here they are seeds locking `+e_3/−e_3` at tick 0 | ATTEMPTED |
| sum of a set | replace neighbor-read by a `Z^3` sum | the construction does not sum; equality is equality of Orient signs | ATTEMPTED |
| global later T | wait until `max t(A,B,C,D)` before reading | `τ(q)=t(q)+1` is per-probe; no global T | ATTEMPTED |
| attach a formation member from already-recorded six-neighbor locks | form the probes by a neighbor-lock letter instead of perp-step | refused; not attached | ATTEMPTED |
| adopt bits into Admissibility | rewrite the local rule by neighbor-read of Orient | refused; displayed, not adopted | ATTEMPTED |

### N2 — wall independence

Missing physical adoption, missing identification of neighbor-read of Orient
with three-axis lex-smallest equal-sign reverse, missing identification with
two-axis neighbor-read of Orient, missing identification with neighbor-read
of `O`, missing identification with neighbor-read of `M`, missing
identification with lex-largest cyclic neighbor-read, missing identification
with axis-cover, and missing Record identification of neighbor-read reverse
are distinct open premises. This note claims no complete wall collection.

### N3 — hidden-condition scan

The host `B_3(0)`, three disjoint opposite-pair seed locks `+e_1`, `−e_1`,
`+e_2`, `−e_2`, `+e_3`, and `−e_3`, perpendicular step rule, incoming-step
lock, own incoming set and own outgoing dual from records with tick
`<= τ`, per-probe `τ=t+1`, cyclic lex-smallest Orient as nm2oricyccz,
neighbor-read as equal `±1` Orient signs at some formed six-neighbor,
Orient fail as neighbor-read fail not `UNDEFINED`, four z-probes with seed
`A`, and mixed remains a set are declared. No uniqueness of outgoing
locks, no six-neighbor lock union as the scored object, no global later T,
no formation attachment from already-recorded six-neighbor locks, and no
Admissibility rewrite are silently assumed.

### N4 — source residual matching

The current axiom memo supplies cubic sites, `M_2(C)`,
content-conditional-on-formation, and unreadable absence. The residual that
formation site, probability, and rate remain unsupplied is unchanged. The
neighbor-read `hold`/`fail` reports do not close that residual.

### N5 — resolution and rhetoric audit

| Resolution | Executed | Not claimed |
|---|---|---|
| per element | cyclic lex-smallest Orient sign at a probe and at formed 6-NN, compared as `±1` at the probe's `t+1` | no continuum alphabet |
| per site | `A,B,C,D` z-probes on `B_3(0)` only | no other cubic sites |
| per mode | no mode calculation | no spectral exhaustion |
| per block | four neighbor-read reports, reverse/face from those bits | no adopted content law |
| lattice wide | checked and not executed | no lattice-wide lettering rule |

### N6 — live partial-closure paths

Live routes include a later Record content map for neighbor-read reverse/face,
a formation-rate rule, and a physical selector among matching neighbors.
None is taken here.

### N7 — hostile steelman

**Steelman:** Neighbor-read HOLD of Orient is only the partner seed sharing
outgoing `O`; two-axis neighbor-read already asked the same letter; the
third pair cannot change a z-probe six-neighborhood; nm2oricycl3z already
said lex-smallest reverse HOLDs and face HOLDs; neighbor-read of `O`
already asked whether a neighbor recovers a lock set; and reverse fail is
only leftover of two-axis reverse fail.

**Answer:** The partner seed `(0,1,1)` matches `O(A,τ)` as a set of three
outgoing steps and has Orient `−1`, not `Orient(A)=+1`. Neighbor-read of
Orient HOLDs at `A` by matching the origin `(0,0,0)`, whose outgoing set
`{−e_2, −e_3}` is not `O(A)`. Two-axis neighbor-read fails at `D` because
`(1,0,0)` has empty `O` and Orient fail at that cut. The third pair seeds
`(2,0,0)` at tick 0, forms `(1,0,0)` at tick 1 locking `−e_1`, and that
site recovers `Orient(D)=−1`, so this letter HOLDs at `D`. Three-axis
lex-smallest Orient reverse HOLDs from equal signs `+1,+1` without asking
whether a six-neighbor recovers that sign; this reverse fails because `B`
has no formed six-neighbor with Orient `+1`. Neighbor-read of `O` fails at
`D`. Reverse fail of two-axis neighbor-read is the same reverse bit, but
from fail at `D` as well as at `B`, not from hold at `D`.

### N8 — cross-cycle echo

Three-axis cyclic lex-smallest Orient reports `+1,+1,−1,−1`, reverse hold,
and face hold. Two-axis neighbor-read of those Orient signs reports hold
only at `A` by matching the origin, reverse fail, and face fail.
nm2oricycl3z lex-largest cyclic next/prev reports Orient `−1,+1,+1,−1`.
nm2axz reported axis-cover HOLD at each of four z-probes, reverse hold,
and face hold. nm2ax12z reported 1-in 2-out split HOLD at each of those
probes, reverse hold, and face hold. nm2readz reported neighbor-read of
`M` fail at `A` and hold at `B`, `C`, and `D`, reverse fail, and face
hold. nm2oreadz reported neighbor-read of `O` hold only at `A` by matching
`(0,1,1)`, reverse fail, and face fail. This note is not those displays:
it reports neighbor-read of cyclic lex-smallest Orient at `τ=t+1` on the
four z-probes of the three-axis opposite seed, hold at `A` by matching the
origin and hold at `D` by matching `(1,0,0)`, reverse fail, and face fail.

**Gate disposition:** PASS for the neighbor-read of cyclic lex-smallest
Orient `t+1` reverse/face reports above. FAIL / DO NOT SHIP for “the
predicate equals the named sign,” “the predicate equals the unique
singleton lock vector,” “the predicate equals six-neighbor lock union,”
“the predicate equals three-axis lex-smallest Orient reverse/face,” “the
predicate equals two-axis neighbor-read of Orient,” “the predicate equals
neighbor-read of `O`,” “the predicate equals neighbor-read of `M`,” “the
predicate equals nm2oricycl3z lex-largest,” “the predicate equals nm2axz
axis-cover,” “the predicate equals nm2ax12z 1-in 2-out,” “bits are
Admissibility,” “neighbor-read of Orient fails at `D`,” “reverse
neighbor-read HOLDs,” or “face neighbor-read HOLDs.”

## Primary runner

The paired runner builds Euclidean `B_3(0)`, runs the three-axis opposite
perp-step incoming-lock process, reads each z-probe's cyclic lex-smallest
Orient from the record prefix at that probe's `t+1`, reads Orient at each
eventually-formed six-neighbor at the same cut, reports neighbor-read as
equal `±1` signs at some formed six-neighbor, and checks Theorems 1--3. It
also checks that neighbor-read HOLDs at `A` by matching the origin and at
`D` by matching `(1,0,0)`, that the partner seed matches `O` and not
Orient, that two-axis neighbor-read fails at `D`, that neighbor-read of
`M` is a different pattern, that lex-largest neighbor-read HOLDs at `B`
and fails at `A`, that three-axis lex-smallest Orient reverse HOLDs while
this reverse fails, that mixed sets remain sets, that unique-letter
neighbor-read is not required at mixed `O`, that the construction does not
sum, that a formation member from already-recorded six-neighbor locks is
not attached, that the second pair and the third pair are seeds and not
formed children, and that the display is not the y-probe or x-probe
neighbor-read. No runner cache is written.
