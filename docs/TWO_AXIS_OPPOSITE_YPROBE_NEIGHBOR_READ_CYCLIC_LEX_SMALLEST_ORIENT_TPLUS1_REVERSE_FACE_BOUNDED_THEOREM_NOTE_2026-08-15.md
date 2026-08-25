---
claim_id: two_axis_opposite_yprobe_neighbor_read_cyclic_lex_smallest_orient_tplus1_reverse_face_bounded_theorem_note_2026-08-15
claim_type: bounded_theorem
claim_scope: "Neighbor-read of cyclic lex-smallest Orient at t+1 on the four y-probes of the two-axis opposite seed, and reverse/face from that, are reported. Displayed, not adopted."
upstream_dependencies:
  - minimal_axioms
runner: scripts/two_axis_opposite_yprobe_neighbor_read_cyclic_lex_smallest_orient_tplus1_reverse_face_2026_08_15.py
---

# Neighbor-Read Of Cyclic Lex-Smallest Orientation At t+1 Reverse And Face On Four Two-Axis Opposite Y-Probes

> **Key terms used in this doc** are indexed A-Z at `docs/KEY_TERMINOLOGY.md`;
> each row points to the canonical source-of-truth doc.

**Date:** 2026-08-15
**Type:** bounded_theorem
**Scope:** neighbor-read of the cyclic next/prev lex-smallest outgoing
determinant orientation of the 1-in 2-out frame of `M` and `O` at each
probe's `τ=t+1`, and reverse/face from that neighbor-read, on the four
y-probes of the two-axis opposite seed in `B_3(0)={n:n·n<=9}`. Same
process and y-probes as nm2axo. Orient as nm2oricyccz. Let `t(q)` be the
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
leftover of nm2oricyccy Orient reverse hold and face fail. This is not
leftover of nm2oready neighbor-read of O. This is not leftover of
nm2ready neighbor-read of M. This is not leftover of nm2oricycy
lex-largest cyclic next/prev. This is not leftover of nm2ax axis-cover.
This is not leftover of nm2ax12 1-in 2-out split. Occupancy of sites is
not used. Named-sign lettering is not used. Uniqueness is not required.
Mixed remains a set. Displayed, not adopted. Do not write into
Admissibility. Do not attach L1.
**Audit-status authority:** independent audit lane only. This note authors no
audit verdict and predicts none.
**Primary runner:**
[`scripts/two_axis_opposite_yprobe_neighbor_read_cyclic_lex_smallest_orient_tplus1_reverse_face_2026_08_15.py`](../scripts/two_axis_opposite_yprobe_neighbor_read_cyclic_lex_smallest_orient_tplus1_reverse_face_2026_08_15.py)

Framework input:

- [`MINIMAL_AXIOMS_2026-06-29.md`](MINIMAL_AXIOMS_2026-06-29.md) supplies
  cubic-lattice sites `Z^3` with nearest-neighbor adjacency, the one-site
  algebra `M_2(C)`, and the Record sentences that records form and that a
  present record locks exactly one admissible local possibility.

Everything after that quoted input is a finite displayed process on `B_3(0)`
and the four named y-probes. Incoming lock letters are unit nearest-neighbor
steps. `O` is the outgoing dual of those incoming sets at the per-probe cut
`τ=t+1`. Orient is the cyclic next/prev lex-smallest outgoing determinant
of the 1-in 2-out frame, as in nm2oricyccz. Neighbor-read asks whether a
formed six-neighbor recovers that Orient sign as `±1`, without being Orient
itself. Reverse and face are scored on neighbor-read HOLD at the paired
probes. Equal Orient signs at `A` and at `B` are a different readout and
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
claim_type_reason: "Exact report of neighbor-read of cyclic lex-smallest Orient at t+1 on the four y-probes of the two-axis opposite seed, neighbor-read bits at each probe, reverse fail and face fail from those bits; uniqueness of outgoing locks is not claimed and the bits are not adopted."
trace_class: frontier_discovery
target_claim_id: two_axis_opposite_yprobe_neighbor_read_cyclic_lex_smallest_orient_tplus1_reverse_face
target_blocker_text: "display neighbor-read of cyclic lex-smallest Orient at t+1 on the four y-probes of the two-axis opposite seed, and reverse/face from that, HOLD iff some formed 6-NN recovers the same +/-1 Orient sign"
source_of_blocker_text: handoff
reachability_to_target: advances
artifact_role: theorem
next_trace_action: "Keep neighbor-read of cyclic lex-smallest Orient at t+1 displayed; do not write neighbor-read into Admissibility, do not reduce to nm2oricyccy Orient reverse/face, do not reduce to neighbor-read of O, do not reduce to neighbor-read of M, do not reduce to lex-largest cyclic next/prev, do not reduce to axis-cover or 1-in 2-out split, and do not attach L1."
conditional_surface_status: "exact on B_3(0) for neighbor-read of cyclic lex-smallest Orient at t+1 on the four y-probes of the two-axis opposite seed and reverse/face from that; displayed, not adopted"
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

No larger host is used. The four y-probes are the only sites whose
neighbor-read of cyclic lex-smallest Orient is scored:

```text
A = (0,1,0),  B = (1,1,1),  C = (0,2,0),  D = (1,1,0).
```

These are not the z-probes `A=(0,0,1)`, `B=(1,1,1)`, `C=(0,0,2)`,
`D=(1,0,1)`. These are not the x-probes `A=(1,0,0)`, `B=(1,1,1)`, `C=(2,0,0)`,
`D=(1,1,0)`. `A` is a seed of the first opposite pair. Same process and
y-probes as nm2axo.

Lock alphabet of the displayed process: `{±e_i}` with `i` in `{1,2,3}`.

Seed: two disjoint opposite pairs recorded at formation tick 0. Origin
locks `+e_1`. Site `(0,1,0)` locks `−e_1`. Site `(0,0,1)` locks `+e_2`.
Site `(0,1,1)` locks `−e_2`. The second pair is a new seed, not a formed
child of the first pair. This seed is not the 1-axis opposite two-site seed
`{0,(0,1,0)}` with only `+e_1/−e_1`. This seed is not the perp two-site
seed `+e_1/+e_2`. This seed is not the z-symmetric three-site seed
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

## Named neighbor-read of cyclic lex-smallest Orient at `τ=t+1`

Let `t(q)` be the formation tick of y-probe `q` when that tick is defined in
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

Identifying neighbor-read of Orient with nm2oricyccy reverse/face of equal
Orient signs is refused: Orient reverse HOLDs, while neighbor-read reverse
fails. Identifying neighbor-read of Orient with neighbor-read of `O` is
refused: neighbor-read of `O` fails at each of the four y-probes, while
this letter HOLDs at `A` by matching the origin and at `C` by matching
`A`. Identifying neighbor-read of Orient with neighbor-read of `M` is
refused: neighbor-read of `M` is fail at `A` and `C` and hold at `B` and
`D`. Identifying neighbor-read of Orient with lex-largest cyclic
neighbor-read is refused: lex-largest neighbor-read at `A` matches both
the origin and `(0,1,1)`, while this letter matches only the origin, and
lex-largest Orient at `B` is `−1` while this Orient at `B` is `+1`.

## Theorem 1 — ticks, `M`, `O`, Orient, neighbor-read at `τ=t+1`

On this process the four y-probes form. Compare to nm2oricyccy: that
leftover reports Orient `+1,+1,+1,fail`, reverse hold, and face fail.
Compare to nm2oready neighbor-read of `O`: that leftover reports fail at
each of the four y-probes. Compare to nm2ready neighbor-read of `M`: that
leftover reports fail at `A` and `C` and hold at `B` and `D`. This display
reads whether a formed six-neighbor recovers the cyclic lex-smallest Orient
sign:

```text
t(A)=0
t(B)=1
t(C)=1
t(D)=2
M(A, τ) = {−e_1}
M(B, τ) = {+e_1}
M(C, τ) = {+e_2}
M(D, τ) = {−e_3}
O(A, τ) = {+e_2, −e_3}
O(B, τ) = {+e_2, +e_3, −e_3}
O(C, τ) = {+e_1, −e_1, +e_3, −e_3}
O(D, τ) = {+e_1, −e_1}
Orient(A) = +1
Orient(B) = +1
Orient(C) = +1
Orient(D) = fail
neighbor-read(A) = hold
neighbor-read(B) = fail
neighbor-read(C) = hold
neighbor-read(D) = fail
formed 6-NN of A at τ: (1, 1, 0)=UNDEFINED, (-1, 1, 0)=UNDEFINED, (0, 2, 0)=fail, (0, 0, 0)=+1, (0, 1, 1)=−1, (0, 1, -1)=fail
formed 6-NN of B at τ: (2, 1, 1)=UNDEFINED, (0, 1, 1)=−1, (1, 2, 1)=fail, (1, 0, 1)=−1, (1, 1, 2)=fail, (1, 1, 0)=fail
formed 6-NN of C at τ: (1, 2, 0)=fail, (-1, 2, 0)=fail, (0, 1, 0)=+1, (0, 2, 1)=fail, (0, 2, -1)=fail
formed 6-NN of D at τ: (2, 1, 0)=fail, (0, 1, 0)=+1, (1, 2, 0)=fail, (1, 0, 0)=fail, (1, 1, 1)=+1, (1, 1, -1)=−1
matching 6-NN of A: (0, 0, 0)
matching 6-NN of B: none
matching 6-NN of C: (0, 1, 0)
matching 6-NN of D: none
```

`A` is a seed at tick 0 with seed letter `−e_1`. The partner of that pair,
the origin, is also a seed at tick 0 with seed letter `+e_1`. At `τ=1`
those two seeds do not share the same outgoing set: `O(A,τ)={+e_2, −e_3}`
while `O(0,τ)={−e_2, −e_3}`, so neighbor-read of `O` fails at `A`. Cyclic
lex-smallest Orient at the origin is `+1`, equal to `Orient(A)`, so
neighbor-read of Orient HOLDs at `A` by matching the origin. The second-pair
seed `(0,1,1)` is a formed six-neighbor of `A` with Orient `−1` and does
not recover `Orient(A)=+1`. Mixed remains a set: `O(A,τ)` has two outgoing
steps and still yields Orient `+1`. `O(C,τ)` has four outgoing steps and
still yields Orient `+1`; neighbor-read HOLDs at `C` by matching `A`. Unique
letters would assign `UNDEFINED` at mixed `O`. Here uniqueness is not
required. At `t`, `O` is empty at `A`, `B`, and `C`, split fails, Orient
fails, and neighbor-read fails, not `UNDEFINED`. At `D`, `O` at `t` is
already `{−e_1}`, split still fails, Orient fails, and neighbor-read fails,
not `UNDEFINED`. At `τ=t+1`, Orient is `±1` at `A`, `B`, and `C`, and fails
at `D` because split fails: `Axis(M(D))={e_3}` and `Axis(O(D))={e_1}` miss
`e_2`. `M` is frozen from `t` to `t+1` at each probe; `O` is not. O is not
M.

On the one-axis opposite two-site seed, `A=(0,1,0)` is still a seed of the
first pair, but `(0,0,1)` and `(0,1,1)` are formed children at tick 1
locking `+e_3`. Neighbor-read of cyclic lex-smallest Orient on that leftover
seed has reverse hold, not this reverse fail.

Empty `O` at a neighbor that is formed at `τ` yields Orient fail, not
`UNDEFINED`, and does not match a `±1` probe sign. Unformed at `τ` is
`UNDEFINED` and is not a match.

## Theorem 2 — reverse from neighbor-read of Orient at `τ`

Reverse neighbor-read holds if and only if neighbor-read HOLDs at `A` and
at `B`. Neighbor-read HOLDs at `A` and fails at `B`. Reverse fails. This is
HOLD iff neighbor-read at both reverse probes, not leftover of nm2oricyccy
Orient reverse hold from `Orient(A)=Orient(B)=+1`.

Reverse neighbor-read at τ: fail

Both sides are defined, so this is not `UNDEFINED`. nm2oricyccy Orient
reverse HOLDs because both signs are `+1`. Neighbor-read of `O` also has
reverse fail, but from fail at `A` as well as at `B`. Neighbor-read of `M`
also has reverse fail, but from the opposite pair of bits: fail at `A` and
hold at `B`. Lex-largest cyclic neighbor-read reverse also fails, but
lex-largest matching at `A` includes `(0,1,1)` in addition to the origin,
and lex-largest Orient at `B` is `−1`. Axis-cover reverse HOLDs. 1-in 2-out
split reverse HOLDs. Those leftovers are not this display.

Reverse fails.

## Theorem 3 — face from neighbor-read of Orient at `τ`

Face neighbor-read holds if and only if neighbor-read HOLDs at `C` and at
`D`. Neighbor-read HOLDs at `C` and fails at `D`. Face fails.

Face neighbor-read at τ: fail

Displayed, not adopted. The bits are not written into Admissibility.
Do not write into Admissibility. Do not attach L1.

nm2oricyccy Orient face fails because `Orient(D)` fails, without asking
whether a six-neighbor recovers `Orient(C)=+1`. Neighbor-read of `M` has
fail at `C` and hold at `D`. Axis-cover face fails from cover fail at `D`.
1-in 2-out split face fails from split fail at `D`. This display scores
neighbor-read of cyclic lex-smallest Orient, which HOLDs at `C` by matching
`A` and fails at `D` because Orient fails at `D`, so face fails.

On the same seed the four z-probes give neighbor-read hold only at `A`, so
reverse fail and face fail, but from fail at `C`, not hold at `C`. The four
x-probes fail at each probe. Those probe-direction readouts are not this
y-probe display.

Face fails.

## What this note does not claim

- It does not select a unique incoming or outgoing lock.
- It does not reduce lock vectors to named signs `{+,−}`.
- It does not require neighbor-read sides to be singletons.
- It does not sum either set.
- It does not replace neighbor-read of Orient by nm2oricyccy equal-sign reverse/face.
- It does not replace neighbor-read of Orient by neighbor-read of `O`.
- It does not replace neighbor-read of Orient by neighbor-read of `M`.
- It does not replace neighbor-read of Orient by nm2oricycy lex-largest cyclic next/prev.
- It does not replace neighbor-read by axis-cover of `M` and `O`.
- It does not replace neighbor-read by 1-in 2-out split.
- It does not replace `O` by `M`.
- It does not replace neighbor-read by locks of six-neighbors.
- It does not use a six-neighbor star as the letter.
- It does not wait for a global later T.
- It does not attach a formation member from already-recorded six-neighbor
  locks.
- It does not reprint nm2oricyccy Orient reverse hold and face fail.
- It does not reprint nm2oready neighbor-read of `O`.
- It does not reprint nm2ready neighbor-read of `M`.
- It does not reprint nm2ax axis-cover reverse hold and face fail.
- It does not reprint nm2ax12 1-in 2-out reverse hold and face fail.
- It does not treat the second opposite pair as a formed child of the first.
- It does not score the z-probes or the x-probes as this letter.
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
two-axis opposite process, neighbor-read of cyclic lex-smallest Orient at
`t+1`, and the reverse/face bits from that neighbor-read are displayed
theorem-domain data.

## Exact target and obligation graph

| Obligation | Status |
|---|---|
| current Lattice / Admissibility / Record premises | quoted; no edit |
| perp-step incoming-lock process on `B_3(0)` | displayed; two disjoint opposite pairs `+e_1/−e_1` and `+e_2/−e_2` |
| ticks `t(A)`, `t(B)`, `t(C)`, `t(D)` | Theorem 1; `0`, `1`, `1`, `2` |
| `M` at `τ=t+1` | Theorem 1; frozen equal to `M` at `t` |
| `O` at `τ=t+1` | Theorem 1; HOLDING outgoing dual |
| Orient at `τ` | Theorem 1; `+1`, `+1`, `+1`, fail as nm2oricyccz |
| Orient at formed 6-NN | Theorem 1; reported at each eventually-formed neighbor |
| neighbor-read bit at `τ` | Theorem 1; hold, fail, hold, fail |
| reverse from neighbor-read at `τ` | Theorem 2; `fail` |
| face from neighbor-read at `τ` | Theorem 3; `fail` |
| unique outgoing lock | not required |
| occupancy of sites as the letter | not used |
| named-sign `{+,−}` letter | not used |
| singleton unique lock-vector letter | not used as the object; mixed remains a set |
| `Z^3` sum of the lock set | not used; no aggregation |
| six-neighbor star as the letter | not used |
| leftover of nm2oricyccy Orient reverse/face | not this neighbor-read display |
| leftover of nm2oready neighbor-read of `O` | not this display |
| leftover of nm2ready neighbor-read of `M` | not this display |
| leftover of nm2oricycy lex-largest | not this display |
| leftover of nm2ax axis-cover | not this neighbor-read display |
| leftover of nm2ax12 1-in 2-out | not this neighbor-read display |
| one-axis opposite leftover of the second pair | not this seed |
| z-probe or x-probe neighbor-read on this seed | not this letter |
| global later T | not used |
| neighbor-read as Admissibility content | not adopted |
| formation site / probability / rate | open |
| physical Record readout of the bits | open |

## Value gate (V1–V5)

| # | Answer |
|---|---|
| V1 | It answers the first-display question: neighbor-read of cyclic lex-smallest Orient at `t+1` on the four y-probes of the two-axis opposite seed, and reverse/face from that. |
| V2 | Current main has no landed neighbor-read reverse/face of cyclic lex-smallest Orient on these four y-probes of this two-axis opposite seed. |
| V3 | Neighbor-read reports at one cut and the two reverse/face bits are independently finite and exact. |
| V4 | The theorem is more than a restatement of Record because it reads whether a formed six-neighbor recovers the cyclic lex-smallest Orient sign at the same `t+1` cut, HOLDs at `A` by matching the origin, HOLDs at `C` by matching `A`, and fails reverse while nm2oricyccy Orient reverse HOLDs. |
| V5 | It is not an adopted content rule: the bits remain displayed. |

## No-go discipline gate

The negative content is narrow: the display does not write those bits into
Admissibility, does not reduce them to named signs, does not require a
unique lock, does not replace neighbor-read of Orient by nm2oricyccy equal
signs, does not replace neighbor-read of Orient by neighbor-read of `O`,
does not replace neighbor-read of Orient by neighbor-read of `M`, does
not replace neighbor-read by lex-largest cyclic next/prev, and does not
identify this display with axis-cover or 1-in 2-out split. No global
impossibility is claimed.

### N1 — materially distinct routes

| Route | Attempt | Why it fails here | Marker |
|---|---|---|---|
| nm2oricyccy equal Orient signs | score reverse/face from `Orient(A)=Orient(B)` both `±1` | Orient reverse HOLDs; neighbor-read reverse fails | ATTEMPTED |
| neighbor-read of `O` | score reverse/face from equal outgoing sets | neighbor-read of `O` fails at each y-probe; this letter HOLDs at `A` by matching `(0,0,0)` and at `C` by matching `A` | ATTEMPTED |
| neighbor-read of `M` | score reverse/face from equal incoming sets | neighbor-read of `M` is fail/hold/fail/hold; this letter is hold/fail/hold/fail | ATTEMPTED |
| nm2oricycy lex-largest cyclic | reuse lex-largest neighbor-read | lex-largest matching at `A` is `(0,0,0)` and `(0,1,1)`; this letter matches only `(0,0,0)`; lex-largest Orient at `B` is `−1` | ATTEMPTED |
| nm2ax axis-cover | reuse cover reverse hold and face fail | cover HOLDs at `A`, `B`, and `C`; neighbor-read of Orient fails at `B` | ATTEMPTED |
| nm2ax12 1-in 2-out | reuse split reverse hold and face fail | split HOLDs at `A`, `B`, and `C`; neighbor-read of Orient fails at `B` | ATTEMPTED |
| unique letter | replace mixed sets by a singleton or `UNDEFINED` | mixed `O(A,τ)` and mixed `O(C,τ)` remain sets; Orient is `+1` and neighbor-read still HOLDs at `A` and at `C` | ATTEMPTED |
| named-sign lettering | collapse `{±e_i}` to `{+,−}` | named-sign lettering lost the outgoing set and the cyclic columns | ATTEMPTED |
| z-probe neighbor-read | score the four z-probes on this seed | z-probe neighbor-read fails at `C`; this letter HOLDs at y-probe `C` | ATTEMPTED |
| x-probe neighbor-read | score the four x-probes on this seed | x-probe neighbor-read fails at each probe; this letter HOLDs at y-probe `A` and `C` | ATTEMPTED |
| one-axis leftover | treat `(0,0,1)` and `(0,1,1)` as formed children of `+e_1/−e_1` | those children lock `+e_3` at tick 1; here they are seeds locking `+e_2/−e_2` at tick 0; leftover reverse HOLDs | ATTEMPTED |
| sum of a set | replace neighbor-read by a `Z^3` sum | the construction does not sum; equality is equality of Orient signs | ATTEMPTED |
| global later T | wait until `max t(A,B,C,D)` before reading | `τ(q)=t(q)+1` is per-probe; no global T | ATTEMPTED |
| attach a formation member from already-recorded six-neighbor locks | form the probes by a neighbor-lock letter instead of perp-step | refused; not attached | ATTEMPTED |
| adopt bits into Admissibility | rewrite the local rule by neighbor-read of Orient | refused; displayed, not adopted | ATTEMPTED |

### N2 — wall independence

Missing physical adoption, missing identification of neighbor-read of Orient
with nm2oricyccy equal-sign reverse, missing identification with neighbor-read
of `O`, missing identification with neighbor-read of `M`, missing
identification with lex-largest cyclic neighbor-read, missing identification
with axis-cover, and missing Record identification of neighbor-read reverse
are distinct open premises. This note claims no complete wall collection.

### N3 — hidden-condition scan

The host `B_3(0)`, two disjoint opposite-pair seed locks `+e_1`, `−e_1`,
`+e_2`, and `−e_2`, perpendicular step rule, incoming-step lock, own
incoming set and own outgoing dual from records with tick `<= τ`, per-probe
`τ=t+1`, cyclic lex-smallest Orient as nm2oricyccz, neighbor-read as equal
`±1` Orient signs at some formed six-neighbor, Orient fail as neighbor-read
fail not `UNDEFINED`, four y-probes with seed `A`, and mixed remains a set
are declared. No uniqueness of outgoing locks, no six-neighbor lock union
as the scored object, no global later T, no formation attachment from
already-recorded six-neighbor locks, and no Admissibility rewrite are
silently assumed.

### N4 — source residual matching

The current axiom memo supplies cubic sites, `M_2(C)`,
content-conditional-on-formation, and unreadable absence. The residual that
formation site, probability, and rate remain unsupplied is unchanged. The
neighbor-read `hold`/`fail` reports do not close that residual.

### N5 — resolution and rhetoric audit

| Resolution | Executed | Not claimed |
|---|---|---|
| per element | cyclic lex-smallest Orient sign at a probe and at formed 6-NN, compared as `±1` at the probe's `t+1` | no continuum alphabet |
| per site | `A,B,C,D` y-probes on `B_3(0)` only | no other cubic sites |
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
a lock set; nm2oricyccy already asked whether reverse probes share a sign;
lex-largest already asked cyclic slots; neighbor-read of `M` already asked
whether a neighbor recovers a lock set; and reverse fail is only leftover
of nm2oready reverse fail.

**Answer:** The partner seed of `A` is the origin. Neighbor-read of `O` fails
at `A` because `O(A,τ)={+e_2, −e_3}` is not `O(0,τ)={−e_2, −e_3}`.
Neighbor-read of Orient HOLDs at `A` by matching the origin, whose Orient
is `+1`. The second-pair seed `(0,1,1)` is a formed six-neighbor of `A` with
Orient `−1`. nm2oricyccy reverse HOLDs from equal signs `+1,+1` without asking
whether a six-neighbor recovers that sign; this reverse fails because `B`
has no formed six-neighbor with Orient `+1`. Lex-largest neighbor-read at
`A` matches both the origin and `(0,1,1)`. Neighbor-read of `M` fails at
`A` and HOLDs at `B`. Reverse fail of neighbor-read of `O` is fail at every
probe, not hold at `A` and `C`.

### N8 — cross-cycle echo

nm2oricyccy reported cyclic lex-smallest Orient `+1,+1,+1,fail`, reverse
hold, and face fail. nm2ax reported axis-cover HOLD at `A`, `B`, and `C`
and fail at `D`, reverse hold, and face fail. nm2ax12 reported 1-in 2-out
split HOLD at `A`, `B`, and `C` and fail at `D`, reverse hold, and face
fail. nm2ready reported neighbor-read of `M` fail at `A` and `C` and hold
at `B` and `D`, reverse fail, and face fail. nm2oready reported
neighbor-read of `O` fail at each of the four y-probes, reverse fail, and
face fail. nm2oricycy lex-largest cyclic next/prev reported Orient
`+1,−1,+1,fail` and matching at `A` of both the origin and `(0,1,1)`.
This note is not those displays: it reports neighbor-read of cyclic
lex-smallest Orient at `τ=t+1` on the four y-probes of the two-axis
opposite seed, hold at `A` by matching the origin, hold at `C` by matching
`A`, reverse fail, and face fail.

**Gate disposition:** PASS for the neighbor-read of cyclic lex-smallest
Orient `t+1` reverse/face reports above. FAIL / DO NOT SHIP for “the
predicate equals the named sign,” “the predicate equals the unique
singleton lock vector,” “the predicate equals six-neighbor lock union,”
“the predicate equals nm2oricyccy Orient reverse/face,” “the predicate
equals neighbor-read of `O`,” “the predicate equals neighbor-read of
`M`,” “the predicate equals nm2oricycy lex-largest,” “the predicate
equals nm2ax axis-cover,” “the predicate equals nm2ax12 1-in 2-out,”
“bits are Admissibility,” “neighbor-read of Orient fails at `A`,”
“reverse neighbor-read HOLDs,” or “face neighbor-read HOLDs.”

## Primary runner

The paired runner builds Euclidean `B_3(0)`, runs the two-axis opposite
perp-step incoming-lock process, reads each y-probe's cyclic lex-smallest
Orient from the record prefix at that probe's `t+1`, reads Orient at each
eventually-formed six-neighbor at the same cut, reports neighbor-read as
equal `±1` signs at some formed six-neighbor, and checks Theorems 1--3. It
also checks that neighbor-read HOLDs at `A` by matching the origin and at
`C` by matching `A`, that the partner origin matches Orient and not `O`,
that neighbor-read of `M` is a different pattern, that lex-largest matching
at `A` is a larger set, that nm2oricyccy Orient reverse HOLDs while this
reverse fails, that mixed sets remain sets, that unique-letter neighbor-read
is not required at mixed `O`, that the construction does not sum, that a
formation member from already-recorded six-neighbor locks is not attached,
that the second pair is a seed and not a formed child, and that the display
is not the z-probe or x-probe neighbor-read. No runner cache is written.
