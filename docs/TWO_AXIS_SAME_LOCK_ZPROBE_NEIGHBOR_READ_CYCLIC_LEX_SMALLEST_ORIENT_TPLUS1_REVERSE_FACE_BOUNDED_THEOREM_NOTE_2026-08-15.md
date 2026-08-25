---
claim_id: two_axis_same_lock_zprobe_neighbor_read_cyclic_lex_smallest_orient_tplus1_reverse_face_bounded_theorem_note_2026-08-15
claim_type: bounded_theorem
claim_scope: "Neighbor-read of the cyclic lex-smallest orientation at t+1 on the four z-probes of the two-axis same-lock seed, and reverse/face from that, are reported. Displayed, not adopted."
upstream_dependencies:
  - minimal_axioms
runner: scripts/two_axis_same_lock_zprobe_neighbor_read_cyclic_lex_smallest_orient_tplus1_reverse_face_2026_08_15.py
---

# Neighbor-Read Of Cyclic Lex-Smallest Orientation At t+1 Reverse And Face On Four Two-Axis Same-Lock Z-Probes

> **Key terms used in this doc** are indexed A-Z at `docs/KEY_TERMINOLOGY.md`;
> each row points to the canonical source-of-truth doc.

**Date:** 2026-08-15
**Type:** bounded_theorem
**Scope:** neighbor-read of the cyclic next/prev lex-smallest outgoing
determinant orientation of the 1-in 2-out frame of `M` and `O` at each
probe's `τ=t+1`, and reverse/face from that neighbor-read, on the four
z-probes of the two-axis same-lock seed in `B_3(0)={n:n·n<=9}`. Same
process and z-probes as nm2slz. Orient as nm2oricyccz. Let `t(q)` be the
formation tick of probe `q`. Let `τ(q)=t(q)+1`. `M(q,τ)` is the set of
earliest incoming nearest-neighbor steps at `q` using only records with
tick `<= τ`. Seeds are a singleton seed letter. `O(q,τ)` is the outgoing
dual of `M`: the set of `e` in `{±e_1,±e_2,±e_3}` such that `q+e` is
formed and `e` is in `M(q+e,τ)`. Unformed at `τ` is `UNDEFINED`. Empty
`O` is empty, not `UNDEFINED`. Axis of a defined lock set `S` is
`Axis(S)={e_i | some ±e_i in S}`. Cover HOLDs at `q` if and only if
`Axis(M)` intersect `Axis(O)` is empty and `Axis(M)` union `Axis(O)`
equals `{e_1,e_2,e_3}`. Split HOLDs at `q` if and only if cover HOLDs
and `|Axis(M)|=1` (hence `|Axis(O)|=2`). When split HOLDs, `m` is the
unique vector in `M`. Let `i` in `{1,2,3}` be the axis index of `m`.
`e_next = e_{i+1}` with `3+1→1`. `e_prev = e_{i-1}` with `1−1→3`.
`O_next = O ∩ {±e_next}`. `O_prev = O ∩ {±e_prev}`. If either empty,
Orient fails, not `UNDEFINED`. Order `+e < −e`. `o_next` is the
lex-smallest vector in `O_next` (hence `+e` if both signs). `o_prev`
likewise. `Orient(q)` is the sign of the integer determinant of columns
`m`, `o_next`, `o_prev`. If split fails, Orient fails, not `UNDEFINED`.
Neighbor-read HOLDs at `q` if and only if `Orient(q)` is `±1` and some
formed 6-NN `r` has `Orient(r)=Orient(q)` both `±1`. If Orient fails at
`q`, neighbor-read fails, not `UNDEFINED`. Unformed `q` is `UNDEFINED`.
Reverse HOLDs if and only if neighbor-read HOLDs at `A` and at `B`. Face
HOLDs if and only if neighbor-read HOLDs at `C` and at `D`. This is not
leftover of nm2oricyccslz Orient reverse fail and face hold. This is not
leftover of nm2oricyccz Orient reverse hold and face hold. This is not
leftover of nm2oreadslz neighbor-read of O. This is not leftover of
nm2readslz neighbor-read of M. This is not leftover of nm2oricyclslz
lex-largest cyclic next/prev. This is not leftover of nm2oricyccrdz
opposite neighbor-read of Orient. This is not leftover of nm2slz
axis-cover. Occupancy of sites is not used. Named-sign lettering is not
used. Uniqueness is not required. Mixed remains a set. Displayed, not
adopted. Do not write into Admissibility. Do not attach L1.
**Audit-status authority:** independent audit lane only. This note authors no
audit verdict and predicts none.
**Primary runner:**
[`scripts/two_axis_same_lock_zprobe_neighbor_read_cyclic_lex_smallest_orient_tplus1_reverse_face_2026_08_15.py`](../scripts/two_axis_same_lock_zprobe_neighbor_read_cyclic_lex_smallest_orient_tplus1_reverse_face_2026_08_15.py)

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
probes. Equal Orient signs at `C` and at `D` are a different readout and
are not used as the object. Neighbor-read of `O` as sets is a different
readout and is not used. Neighbor-read of `M` is a different readout and
is not used. Lex-largest cyclic next/prev is a different readout and is
not used. Named signs `{+,−}` are a coarser readout and are not used. A
singleton unique lock letter is a different readout and is not used as the
object. Axis-cover of `M` and `O` is a different readout and is not used.
1-in 2-out split is a different readout and is not used. A `Z^3` sum of
those locks is a different readout and is not used. Occupancy of sites is
not used. A six-neighbor star is not the letter.

## Machine status and trace

```yaml
actual_current_surface_status: bounded-support
target_claim_type: bounded_theorem
claim_type_reason: "Exact report of neighbor-read of cyclic lex-smallest Orient at t+1 on the four z-probes of the two-axis same-lock seed, neighbor-read bits fail/hold/fail/fail at A,B,C,D, reverse fail and face fail from those bits; uniqueness of outgoing locks is not claimed and the bits are not adopted."
trace_class: frontier_discovery
target_claim_id: two_axis_same_lock_zprobe_neighbor_read_cyclic_lex_smallest_orient_tplus1_reverse_face
target_blocker_text: "display neighbor-read of cyclic lex-smallest Orient at t+1 on the four z-probes of the two-axis same-lock seed, and reverse/face from that, HOLD iff some formed 6-NN recovers the same +/-1 Orient sign"
source_of_blocker_text: handoff
reachability_to_target: advances
artifact_role: theorem
next_trace_action: "Keep neighbor-read of cyclic lex-smallest Orient at t+1 displayed; do not write neighbor-read into Admissibility, do not reduce to nm2oricyccslz Orient reverse/face, do not reduce to nm2oricyccz Orient reverse/face, do not reduce to neighbor-read of O, do not reduce to neighbor-read of M, do not reduce to lex-largest cyclic next/prev, do not reduce to axis-cover or 1-in 2-out split, and do not attach L1."
conditional_surface_status: "exact on B_3(0) for neighbor-read of cyclic lex-smallest Orient at t+1 on the four z-probes of the two-axis same-lock seed and reverse/face from that; displayed, not adopted"
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
`D=(1,1,0)`. `A` is a seed of the second same-lock pair. Same process and
z-probes as nm2slz.

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

Identifying neighbor-read of Orient with nm2oricyccslz reverse/face of
equal Orient signs is refused: Orient reverse fails and Orient face HOLDs,
while neighbor-read reverse fails and neighbor-read face fails. Identifying
neighbor-read of Orient with neighbor-read of `O` is refused: neighbor-read
of `O` fails at each of the four z-probes, while this letter HOLDs at `B`.
Identifying neighbor-read of Orient with neighbor-read of `M` is refused:
neighbor-read of `M` HOLDs at each of the four z-probes. Identifying
neighbor-read of Orient with lex-largest cyclic neighbor-read is refused:
lex-largest neighbor-read also HOLDs only at `B`, but by matching partner
Orient `−1`, while this letter matches partner Orient `+1`. Identifying
this display with nm2oricyccrdz opposite neighbor-read of Orient is
refused: opposite HOLDs at `A` by matching the origin and fails at `B`.

## Theorem 1 — ticks, `M`, `O`, Orient, neighbor-read at `τ=t+1`

On this process the four z-probes form. Compare to nm2oricyccslz: that
leftover reports Orient fail, `+1`, `−1`, `−1`, reverse fail, and face
hold. Compare to nm2oricyccz: that leftover reports Orient `+1,+1,−1,−1`,
reverse hold, and face hold. Compare to nm2oreadslz neighbor-read of `O`:
that leftover reports fail at `A`, `B`, `C`, and `D`. Compare to
nm2readslz neighbor-read of `M`: that leftover reports hold at each of
the four z-probes. This display reads whether a formed six-neighbor
recovers the cyclic lex-smallest Orient sign:

```text
t(A)=0
t(B)=1
t(C)=1
t(D)=1
M(A, τ) = {+e_2}
M(B, τ) = {+e_1}
M(C, τ) = {+e_3}
M(D, τ) = {+e_1}
O(A, τ) = {+e_1, −e_1, +e_2, +e_3}
O(B, τ) = {+e_2, +e_3, −e_3}
O(C, τ) = {+e_1, −e_1, −e_2}
O(D, τ) = {−e_2, +e_3, −e_3}
Orient(A) = fail
Orient(B) = +1
Orient(C) = −1
Orient(D) = −1
neighbor-read(A) = fail
neighbor-read(B) = hold
neighbor-read(C) = fail
neighbor-read(D) = fail
formed 6-NN of A at τ: (1, 0, 1)=fail, (-1, 0, 1)=fail, (0, 1, 1)=+1, (0, -1, 1)=UNDEFINED, (0, 0, 2)=fail, (0, 0, 0)=+1
formed 6-NN of B at τ: (2, 1, 1)=UNDEFINED, (0, 1, 1)=+1, (1, 2, 1)=fail, (1, 0, 1)=−1, (1, 1, 2)=fail, (1, 1, 0)=fail
formed 6-NN of C at τ: (1, 0, 2)=fail, (-1, 0, 2)=fail, (0, 1, 2)=+1, (0, -1, 2)=fail, (0, 0, 1)=fail
formed 6-NN of D at τ: (2, 0, 1)=UNDEFINED, (0, 0, 1)=fail, (1, 1, 1)=+1, (1, -1, 1)=fail, (1, 0, 2)=fail, (1, 0, 0)=fail
matching 6-NN of A: none
matching 6-NN of B: (0, 1, 1)
matching 6-NN of C: none
matching 6-NN of D: none
```

`A` is a seed at tick 0 with seed letter `+e_2`. The partner of that pair,
`(0,1,1)`, is also a seed at tick 0 with seed letter `+e_2`. At `τ=1`
those two seeds do not share the same outgoing set: `O(A,τ)` has four
outgoing steps including partner `+e_2`, while `O((0,1,1),τ)` is
`{+e_1, −e_1, +e_3}`, so neighbor-read of `O` fails at `A`. Cyclic
lex-smallest Orient at the partner is `+1`, because `m=+e_2` as at `A`,
but `Orient(A)` is fail from overlapping `e_2` in `Axis(O)`, so the
partner does not make neighbor-read HOLD at `A`. The origin `(0,0,0)` at
the same cut has `M={+e_1}`, `O={−e_2, −e_3}`, and Orient `+1`; that is a
formed six-neighbor of `A` with a `±1` sign, but neighbor-read still
fails at `A` because Orient at `A` itself is fail, not `±1`. Neighbor-read
HOLDs at `B` by matching the partner seed `(0,1,1)`, whose Orient is
`+1`. Mixed remains a set: `O(A,τ)` has four outgoing steps and
`O(B,τ)` has three outgoing steps. Unique letters would assign
`UNDEFINED` at mixed `O`. Here uniqueness is not required. At `t`,
`O(A)={+e_2}` already from the partner seed, `O` is empty at `B`, at
`C`, and at `D`, split fails at each probe, Orient fails, and
neighbor-read fails, not `UNDEFINED`. At `τ=t+1`, Orient is fail at `A`
and `±1` at `B`, `C`, and `D`. `M` is frozen from `t` to `t+1`; `O` is
not. O is not M.

On the 1-axis same-lock two-site seed, `A=(0,0,1)` is a formed child at
tick 1 locking `+e_3`. That is leftover of the first pair. Here both
`(0,0,1)` and `(0,1,1)` are seeds of a second same-lock pair on a second
axis. Neighbor-read of cyclic lex-smallest Orient on that leftover seed
has reverse hold, not this reverse fail.

Empty `O` at a neighbor that is formed at `τ` yields Orient fail, not
`UNDEFINED`, and does not match a `±1` probe sign. Unformed at `τ` is
`UNDEFINED` and is not a match.

## Theorem 2 — reverse from neighbor-read of Orient at `τ`

Reverse neighbor-read holds if and only if neighbor-read HOLDs at `A` and
at `B`. Neighbor-read fails at `A` and HOLDs at `B`. Reverse fails. This is
HOLD iff neighbor-read at both reverse probes, not leftover of
nm2oricyccslz Orient reverse fail from `Orient(A)` fail and
`Orient(B)=+1`.

Reverse neighbor-read at τ: fail

Both sides are defined, so this is not `UNDEFINED`. nm2oricyccslz Orient
reverse also fails because `Orient(A)` is fail, but that leftover does not
ask whether a six-neighbor recovers the sign at `B`. nm2oricyccz Orient
reverse HOLDs from equal `+1` signs. Neighbor-read of `O` also has reverse
fail, but from fail at both `A` and `B`. Neighbor-read of `M` has reverse
hold. Lex-largest cyclic neighbor-read reverse also fails from fail at
`A` and hold at `B`, but the recovered partner sign is `−1`, not `+1`.
Opposite-seed neighbor-read reverse fails from the opposite pair of bits:
hold at `A` and fail at `B`. Axis-cover reverse fails. 1-in 2-out split
reverse fails. Those leftovers are not this display.

Reverse fails.

## Theorem 3 — face from neighbor-read of Orient at `τ`

Face neighbor-read holds if and only if neighbor-read HOLDs at `C` and at
`D`. Neighbor-read fails at `C` and at `D`. Face fails.

Face neighbor-read at τ: fail

Displayed, not adopted. The bits are not written into Admissibility.
Do not write into Admissibility. Do not attach L1.

nm2oricyccslz Orient face HOLDs because `Orient(C)=Orient(D)=−1`.
nm2oricyccz Orient face also HOLDs with `−1,−1` on the opposite seed.
Neighbor-read of `M` has face hold. Axis-cover face HOLDs. 1-in 2-out
split face HOLDs. Neighbor-read of `O` has face fail from fail at each
probe, while this letter HOLDs at `B`. This display scores neighbor-read
of cyclic lex-smallest Orient, which fails at `C` and at `D` because no
formed six-neighbor recovers `−1`, so face fails.

On the same seed the four y-probes give neighbor-read fail at `A` from
Orient `−1` with no matching neighbor, hold at `B`, and fail at `C`, so
reverse fail and face fail, but from Orient `−1` at y-probe `A`, not
Orient fail at z-probe `A`. The four x-probes fail at `A` and HOLD at
`B`, with reverse fail and face fail, but x-probe `A` is `(1,0,0)` at
tick 2, not the seed `A=(0,0,1)`. Those probe-direction readouts are not
this z-probe display.

Face fails.

## What this note does not claim

- It does not select a unique incoming or outgoing lock.
- It does not reduce lock vectors to named signs `{+,−}`.
- It does not require neighbor-read sides to be singletons.
- It does not sum either set.
- It does not replace neighbor-read of Orient by nm2oricyccslz equal-sign reverse/face.
- It does not replace neighbor-read of Orient by nm2oricyccz equal-sign reverse/face.
- It does not replace neighbor-read of Orient by neighbor-read of `O`.
- It does not replace neighbor-read of Orient by neighbor-read of `M`.
- It does not replace neighbor-read of Orient by nm2oricyclslz lex-largest cyclic next/prev.
- It does not replace neighbor-read of Orient by nm2oricyccrdz opposite neighbor-read.
- It does not replace neighbor-read by axis-cover of `M` and `O`.
- It does not replace neighbor-read by 1-in 2-out split.
- It does not replace `O` by `M`.
- It does not replace neighbor-read by locks of six-neighbors.
- It does not use a six-neighbor star as the letter.
- It does not wait for a global later T.
- It does not attach a formation member from already-recorded six-neighbor
  locks.
- It does not reprint nm2oricyccslz Orient reverse fail and face hold.
- It does not reprint nm2oricyccz Orient reverse hold and face hold.
- It does not reprint nm2oreadslz neighbor-read of `O`.
- It does not reprint nm2readslz neighbor-read of `M`.
- It does not reprint nm2slz axis-cover reverse fail and face hold.
- It does not reprint nm2ax12z 1-in 2-out reverse hold and face hold.
- It does not treat the second same-lock pair as a formed child of the first.
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
two-axis same-lock process, neighbor-read of cyclic lex-smallest Orient at
`t+1`, and the reverse/face bits from that neighbor-read are displayed
theorem-domain data.

## Exact target and obligation graph

| Obligation | Status |
|---|---|
| current Lattice / Admissibility / Record premises | quoted; no edit |
| perp-step incoming-lock process on `B_3(0)` | displayed; two disjoint same-lock pairs `+e_1/+e_1` and `+e_2/+e_2` |
| ticks `t(A)`, `t(B)`, `t(C)`, `t(D)` | Theorem 1; `0`, `1`, `1`, `1` |
| `M` at `τ=t+1` | Theorem 1; frozen equal to `M` at `t` |
| `O` at `τ=t+1` | Theorem 1; outgoing dual includes partner `+e_2` at `A` |
| Orient at `τ` | Theorem 1; fail, `+1`, `−1`, `−1` as nm2oricyccslz / nm2oricyccz on this seed |
| Orient at formed 6-NN | Theorem 1; reported at each eventually-formed neighbor |
| neighbor-read bit at `τ` | Theorem 1; fail, hold, fail, fail |
| reverse from neighbor-read at `τ` | Theorem 2; `fail` |
| face from neighbor-read at `τ` | Theorem 3; `fail` |
| unique outgoing lock | not required |
| occupancy of sites as the letter | not used |
| named-sign `{+,−}` letter | not used |
| singleton unique lock-vector letter | not used as the object; mixed remains a set |
| `Z^3` sum of the lock set | not used; no aggregation |
| six-neighbor star as the letter | not used |
| leftover of nm2oricyccslz Orient reverse/face | not this neighbor-read display |
| leftover of nm2oricyccz Orient reverse/face | not this neighbor-read display |
| leftover of nm2oreadslz neighbor-read of `O` | not this display |
| leftover of nm2readslz neighbor-read of `M` | not this display |
| leftover of nm2oricyclslz lex-largest | not this display |
| leftover of nm2oricyccrdz opposite neighbor-read | not this display |
| leftover of nm2slz axis-cover | not this neighbor-read display |
| leftover of nm2ax12z 1-in 2-out | not this neighbor-read display |
| 1-axis same-lock leftover of the second pair | not this seed |
| y-probe or x-probe neighbor-read on this seed | not this letter |
| global later T | not used |
| neighbor-read as Admissibility content | not adopted |
| formation site / probability / rate | open |
| physical Record readout of the bits | open |

## Value gate (V1–V5)

| # | Answer |
|---|---|
| V1 | It answers the first-display question: neighbor-read of cyclic lex-smallest Orient at `t+1` on the four z-probes of the two-axis same-lock seed, and reverse/face from that. |
| V2 | Current main has no landed neighbor-read reverse/face of cyclic lex-smallest Orient on these four z-probes of this two-axis same-lock seed. |
| V3 | Neighbor-read reports at one cut and the two reverse/face bits are independently finite and exact. |
| V4 | The theorem is more than a restatement of Record because it reads whether a formed six-neighbor recovers the cyclic lex-smallest Orient sign at the same `t+1` cut, fails at `A` because Orient is fail, HOLDs at `B` by matching the partner seed, and fails face while nm2oricyccslz Orient face HOLDs. |
| V5 | It is not an adopted content rule: the bits remain displayed. |

## No-go discipline gate

The negative content is narrow: the display does not write those bits into
Admissibility, does not reduce them to named signs, does not require a
unique lock, does not replace neighbor-read of Orient by nm2oricyccslz
equal signs, does not replace neighbor-read of Orient by nm2oricyccz
equal signs, does not replace neighbor-read of Orient by neighbor-read of
`O`, does not replace neighbor-read of Orient by neighbor-read of `M`,
does not replace neighbor-read by lex-largest cyclic next/prev, and does
not identify this display with axis-cover or 1-in 2-out split. No global
impossibility is claimed.

### N1 — materially distinct routes

| Route | Attempt | Why it fails here | Marker |
|---|---|---|---|
| nm2oricyccslz equal Orient signs | score reverse/face from `Orient(A)=Orient(B)` both `±1` | Orient reverse fails and Orient face HOLDs; neighbor-read reverse fails and neighbor-read face fails | ATTEMPTED |
| nm2oricyccz equal Orient signs | reuse opposite-seed reverse hold and face hold | opposite has `Orient(A)=+1` with split HOLD; here split fails at `A` and neighbor-read fails at `A` | ATTEMPTED |
| neighbor-read of `O` | score reverse/face from equal outgoing sets | neighbor-read of `O` fails at each z-probe; this letter HOLDs at `B` by matching partner Orient `+1` | ATTEMPTED |
| neighbor-read of `M` | score reverse/face from equal incoming sets | neighbor-read of `M` is hold/hold/hold/hold and reverse hold and face hold; this letter is fail/hold/fail/fail | ATTEMPTED |
| nm2oricyclslz lex-largest cyclic | reuse lex-largest neighbor-read | lex-largest neighbor-read HOLDs at `B` by matching partner Orient `−1`; this letter HOLDs at `B` by matching partner Orient `+1` | ATTEMPTED |
| nm2oricyccrdz opposite neighbor-read | reuse opposite hold at `A` matching the origin | opposite HOLDs at `A` and fails at `B`; this letter fails at `A` and HOLDs at `B` | ATTEMPTED |
| nm2slz axis-cover | reuse cover reverse fail and face hold | cover HOLDs at `B`,`C`,`D` and cover face HOLDs; neighbor-read of Orient fails at `C` and at `D` | ATTEMPTED |
| nm2ax12z 1-in 2-out | reuse split reverse/face | split fails at `A` and HOLDs at `B`,`C`,`D`; split face HOLDs while this face fails | ATTEMPTED |
| unique letter | replace mixed sets by a singleton or `UNDEFINED` | mixed `O(B,τ)` remains a set; Orient is `+1` and neighbor-read still HOLDs at `B` | ATTEMPTED |
| named-sign lettering | collapse `{±e_i}` to `{+,−}` | named-sign lettering lost the outgoing set and the cyclic columns | ATTEMPTED |
| y-probe neighbor-read | score the four y-probes on this seed | y-probe `A` has Orient `−1` with neighbor-read fail; this z-probe `A` has Orient fail | ATTEMPTED |
| x-probe neighbor-read | score the four x-probes on this seed | x-probe `A` is `(1,0,0)` at tick 2; this letter is seed `A=(0,0,1)` at tick 0 | ATTEMPTED |
| 1-axis leftover | treat `(0,0,1)` and `(0,1,1)` as formed children of `+e_1/+e_1` | those children lock `+e_3` at tick 1; here they are seeds locking `+e_2` at tick 0; leftover reverse HOLDs | ATTEMPTED |
| sum of a set | replace neighbor-read by a `Z^3` sum | the construction does not sum; equality is equality of Orient signs | ATTEMPTED |
| global later T | wait until `max t(A,B,C,D)` before reading | `τ(q)=t(q)+1` is per-probe; no global T | ATTEMPTED |
| attach a formation member from already-recorded six-neighbor locks | form the probes by a neighbor-lock letter instead of perp-step | refused; not attached | ATTEMPTED |
| adopt bits into Admissibility | rewrite the local rule by neighbor-read of Orient | refused; displayed, not adopted | ATTEMPTED |

### N2 — wall independence

Missing physical adoption, missing identification of neighbor-read of Orient
with nm2oricyccslz equal-sign reverse, missing identification with
nm2oricyccz equal-sign reverse, missing identification with neighbor-read
of `O`, missing identification with neighbor-read of `M`, missing
identification with lex-largest cyclic neighbor-read, missing identification
with opposite-seed neighbor-read, missing identification with axis-cover,
and missing Record identification of neighbor-read reverse are distinct open
premises. This note claims no complete wall collection.

### N3 — hidden-condition scan

The host `B_3(0)`, two disjoint same-lock seed pairs `+e_1/+e_1` and
`+e_2/+e_2`, perpendicular step rule, incoming-step lock, own incoming set
and own outgoing dual from records with tick `<= τ`, per-probe `τ=t+1`,
cyclic lex-smallest Orient as nm2oricyccz, neighbor-read as equal `±1`
Orient signs at some formed six-neighbor, Orient fail as neighbor-read fail
not `UNDEFINED`, four z-probes with seed `A`, second pair as a new seed not
a formed child, and mixed remains a set are declared. No uniqueness of
outgoing locks, no six-neighbor lock union as the scored object, no global
later T, no formation attachment from already-recorded six-neighbor locks,
and no Admissibility rewrite are silently assumed.

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
outgoing `O`; neighbor-read of `O` already asked whether a neighbor recovers
a lock set; nm2oricyccslz already asked whether reverse probes share a sign;
lex-largest already asked cyclic slots and HOLDs at the same probe `B`;
neighbor-read of `M` already asked whether a neighbor recovers a lock set;
opposite neighbor-read already asked this letter on the opposite seed; and
reverse fail is only leftover of nm2oreadslz reverse fail.

**Answer:** The partner seed `(0,1,1)` does not match `O(A,τ)`: partner
outgoing is `{+e_1, −e_1, +e_3}` while `O(A,τ)` also contains `+e_2`.
Neighbor-read of `O` fails at each of the four z-probes. Neighbor-read of
Orient fails at `A` because `Orient(A)` is fail from overlapping `e_2`,
even though the origin and the partner both have Orient `+1`. It HOLDs at
`B` by matching the partner seed's Orient `+1`, not an outgoing set.
nm2oricyccslz reverse fails from equal-sign failure at `A` and face HOLDs
from `−1,−1` at `C` and `D` without asking whether a six-neighbor recovers
those signs; this face fails because no formed six-neighbor of `C` or of
`D` has Orient `−1`. Lex-largest neighbor-read HOLDs at `B` by matching
partner Orient `−1`; this letter matches partner Orient `+1`. Neighbor-read
of `M` HOLDs at each probe. Opposite-seed neighbor-read HOLDs at `A` by
matching the origin and fails at `B`. Reverse fail of neighbor-read of `O`
is fail at both reverse probes, not fail at `A` and hold at `B`.

### N8 — cross-cycle echo

nm2oricyccslz reported cyclic lex-smallest Orient fail, `+1`, `−1`, `−1`,
reverse fail, and face hold. nm2oricyccz reported cyclic lex-smallest
Orient `+1,+1,−1,−1`, reverse hold, and face hold. nm2slz reported
axis-cover fail at `A` from overlapping `e_2`, cover HOLD at `B`,`C`,`D`,
reverse fail, and face hold. nm2readslz reported neighbor-read of `M` hold
at each of four z-probes, reverse hold, and face hold. nm2oreadslz reported
neighbor-read of `O` fail at each of those probes, reverse fail, and face
fail. nm2oricyclslz lex-largest cyclic next/prev reported Orient
`fail,−1,+1,+1`. nm2oricyccrdz reported neighbor-read of Orient hold only
at `A` by matching the origin on the opposite seed. This note is not those
displays: it reports neighbor-read of cyclic lex-smallest Orient at
`τ=t+1` on the four z-probes of the two-axis same-lock seed, fail at `A`
from Orient fail, hold at `B` by matching the partner seed, reverse fail,
and face fail.

**Gate disposition:** PASS for the neighbor-read of cyclic lex-smallest
Orient `t+1` reverse/face reports above. FAIL / DO NOT SHIP for “the
predicate equals the named sign,” “the predicate equals the unique
singleton lock vector,” “the predicate equals six-neighbor lock union,”
“the predicate equals nm2oricyccslz Orient reverse/face,” “the predicate
equals nm2oricyccz Orient reverse/face,” “the predicate equals
neighbor-read of `O`,” “the predicate equals neighbor-read of `M`,” “the
predicate equals nm2oricyclslz lex-largest,” “the predicate equals
nm2oricyccrdz opposite neighbor-read,” “the predicate equals nm2slz
axis-cover,” “the predicate equals nm2ax12z 1-in 2-out,” “bits are
Admissibility,” “neighbor-read of Orient HOLDs at `A`,” “reverse
neighbor-read HOLDs,” or “face neighbor-read HOLDs.”

## Primary runner

The paired runner builds Euclidean `B_3(0)`, runs the two-axis same-lock
perp-step incoming-lock process, reads each z-probe's cyclic lex-smallest
Orient from the record prefix at that probe's `t+1`, reads Orient at each
eventually-formed six-neighbor at the same cut, reports neighbor-read as
equal `±1` signs at some formed six-neighbor, and checks Theorems 1--3. It
also checks that neighbor-read HOLDs only at `B` by matching the partner
seed, that the partner seed does not match `O` at `A`, that neighbor-read
of `M` is a different pattern, that lex-largest neighbor-read HOLDs at `B`
from partner Orient `−1` while this letter matches `+1`, that
nm2oricyccslz Orient face HOLDs while this face fails, that mixed sets
remain sets, that unique-letter neighbor-read is not required at mixed
`O`, that the construction does not sum, that a formation member from
already-recorded six-neighbor locks is not attached, that the second pair
is a seed and not a formed child, and that the display is not the y-probe
or x-probe neighbor-read. No runner cache is written.
