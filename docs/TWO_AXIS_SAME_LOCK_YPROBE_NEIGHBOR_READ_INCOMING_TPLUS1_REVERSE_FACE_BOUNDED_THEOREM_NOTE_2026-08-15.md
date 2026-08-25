---
claim_id: two_axis_same_lock_yprobe_neighbor_read_incoming_tplus1_reverse_face_bounded_theorem_note_2026-08-15
claim_type: bounded_theorem
claim_scope: "Neighbor-read of M at t+1 on the four y-probes of the two-axis same-lock seed, and reverse/face from that, are reported. Displayed, not adopted."
upstream_dependencies:
  - minimal_axioms
runner: scripts/two_axis_same_lock_yprobe_neighbor_read_incoming_tplus1_reverse_face_2026_08_15.py
---

# Neighbor-Read Of Incoming M At t+1 Reverse And Face On Four Two-Axis Same-Lock Y-Probes

> **Key terms used in this doc** are indexed A-Z at `docs/KEY_TERMINOLOGY.md`;
> each row points to the canonical source-of-truth doc.

**Date:** 2026-08-15
**Type:** bounded_theorem
**Scope:** neighbor-read of earliest incoming set `M` at each probe's
`τ=t+1`, and reverse/face from that neighbor-read, on the four y-probes of
the two-axis same-lock seed in `B_3(0)={n:n·n<=9}`. Same perp-step
incoming-lock process and y-probes as nm2slo. Let `t(q)` be the formation
tick of probe `q`. Let `τ(q)=t(q)+1`. `M(q,τ)` is the set of earliest
incoming nearest-neighbor steps at `q` using only records with tick `<= τ`.
Seeds are a singleton seed letter. Unformed at `τ` is `UNDEFINED`. For a
formed neighbor `r=q+e`, report `M(r,τ)`. Neighbor-read HOLDs at `q` if
and only if some formed six-neighbor `r` has `M(r,τ)` defined and equal to
`M(q,τ)` as sets. Unformed `q` is `UNDEFINED`. Reverse HOLDs if and only
if neighbor-read HOLDs at `A` and at `B`. Face HOLDs if and only if
neighbor-read HOLDs at `C` and at `D`. This is not leftover of nm2readslx
same-lock x-probe neighbor-read. This is not leftover of two-axis opposite
y-probe neighbor-read. This is not leftover of nm2slo timed-O
exist-opposite. This is not leftover of nm2sl axis-cover. This is not
leftover of nm2simsly simultaneous. This is not leftover of nm2ot3sly O
freeze. This is not leftover of R-style recovery of the incoming step from
neighbors. Neither pair is opposite. Uniqueness is not required. Mixed
remains a set. Occupancy of sites is not used. Occupancy `n` is not used.
This display does not use occupancy. Displayed, not adopted. Do not
write into Admissibility. Do not attach L1.
**Audit-status authority:** independent audit lane only. This note authors no
audit verdict and predicts none.
**Primary runner:**
[`scripts/two_axis_same_lock_yprobe_neighbor_read_incoming_tplus1_reverse_face_2026_08_15.py`](../scripts/two_axis_same_lock_yprobe_neighbor_read_incoming_tplus1_reverse_face_2026_08_15.py)

Framework input:

- [`MINIMAL_AXIOMS_2026-06-29.md`](MINIMAL_AXIOMS_2026-06-29.md) supplies
  cubic-lattice sites `Z^3` with nearest-neighbor adjacency, the one-site
  algebra `M_2(C)`, and the Record sentences that records form and that a
  present record locks exactly one admissible local possibility.

Everything after that quoted input is a finite displayed process on `B_3(0)`
and the four named y-probes. Incoming lock letters are unit nearest-neighbor
steps. Neighbor-read compares those incoming sets as sets at a formed
six-neighbor. Reverse and face are scored on neighbor-read HOLD at the
paired probes. Named signs `{+,−}` are a coarser readout and are not used.
A singleton unique lock letter is a different readout and is not used as
the object. R-style recovery of the incoming step as `−e` in `M(q+e,τ)` is
a different readout and is not used. Axis-cover of `M` and `O` is a
different readout and is not used. Forall-perp of integer dots `m·o` is a
different readout and is not used. Simultaneous nonempty disjoint `M` and
`O` is a different readout and is not used. Occupancy of sites is not used.
A six-neighbor star is not the letter.

## Machine status and trace

```yaml
actual_current_surface_status: bounded-support
target_claim_type: bounded_theorem
claim_type_reason: "Exact report of neighbor-read of M at t+1 on the four y-probes of the two-axis same-lock seed, HOLD at A from matching origin, HOLD at B and D, FAIL at C, reverse hold and face fail from those bits; uniqueness of incoming locks is not claimed and the bits are not adopted."
trace_class: frontier_discovery
target_claim_id: two_axis_same_lock_yprobe_neighbor_read_incoming_tplus1_reverse_face
target_blocker_text: "display neighbor-read of M at t+1 on the four y-probes of the two-axis same-lock seed, compare to nm2readslx HOLDING and to two-axis opposite y-probe neighbor-read, HOLD iff some formed 6-NN recovers M as a set"
source_of_blocker_text: handoff
reachability_to_target: advances
artifact_role: theorem
next_trace_action: "Keep neighbor-read of M at t+1 displayed; do not write the bits into Admissibility, do not reduce to R-style recovery, do not reduce to nm2slo timed-O, do not reduce to nm2sl axis-cover, do not reduce to nm2simsly simultaneous, do not reduce to nm2ot3sly O freeze, do not replace the display by nm2readslx same-lock x-probe neighbor-read, do not replace the display by two-axis opposite y-probe neighbor-read, and do not attach L1."
conditional_surface_status: "exact on B_3(0) for neighbor-read of M at t+1 on the four y-probes of the two-axis same-lock seed and reverse/face from that; displayed, not adopted"
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
neighbor-read of `M` is scored:

```text
A = (0,1,0),  B = (1,1,1),  C = (0,2,0),  D = (1,1,0).
```

These are not the x-probes `A=(1,0,0)`, `B=(1,1,1)`, `C=(2,0,0)`,
`D=(1,1,0)`. These are not the z-probes `A=(0,0,1)`, `B=(1,1,1)`, `C=(0,0,2)`,
`D=(1,0,1)`. `A` is a seed. Same process and y-probes as nm2slo.

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

## Named neighbor-read of `M` at `τ=t+1`

Let `t(q)` be the formation tick of y-probe `q` when that tick is defined in
`B_3(0)`. Let `τ(q)=t(q)+1`. There is no global T.

`M(q,τ)` is the set of earliest incoming nearest-neighbor steps at `q`
using only records with tick `<= τ`. If `q` is unformed at `τ`, then
`M(q,τ)` is `UNDEFINED`. If `q` is a seed and `τ >= 0`, then `M(q,τ)` is
the singleton seed letter.

Neighbor-read at a formed probe at the same cut:

```text
neighbor-read(q) HOLDs iff some formed 6-NN r has M(r,τ)
defined and equal to M(q,τ) as sets.
```

If `q` is unformed at `τ`, then neighbor-read is `UNDEFINED`. Empty match
fails. Mixed remains a set: equality is set equality, not a unique-letter
reduction. Occupancy of sites is not used. The construction does not require
`M` to be a singleton. It does not sum the set. It does not wait for a
global later T.

R-style recovery is a different object: the set of steps `e` such that
`−e` lies in `M(q+e,τ)`. Axis-cover of `M` and outgoing dual `O` is a
different object. Forall-perp of `M` versus `O` is a different object.
Simultaneous nonempty disjoint `M` and `O` is a different object.
Timed-O exist-opposite of signed `O` is a different object. O freeze of
`O(t+1)` versus `O(t+2)` is a different object.

Reverse neighbor-read holds if and only if neighbor-read HOLDs at `A` and
at `B`. Face neighbor-read holds if and only if neighbor-read HOLDs at `C`
and at `D`. Either side `UNDEFINED` is `UNDEFINED`. Else if both sides HOLD,
reverse or face HOLDs. Else fail.

Identifying a named sign of those locks with reverse or face is refused:
named-sign lettering lost the set. Identifying R-style recovery with
neighbor-read is refused: at `A`, `B`, and `C`, R-style is empty while
neighbor-read HOLDs at `A` and at `B` and fails at `C`; at `D`, R-style is
`{−e_1}` while `M(D,τ)={−e_3}`. Identifying nm2slo timed-O exist-opposite
with this reverse/face is refused: timed-O HOLDs reverse and HOLDs face from
opposite letters in `O`; neighbor-read HOLDs reverse and fails face from
set-equality of own incoming `M` at a formed six-neighbor. Identifying
nm2sl axis-cover with this reverse/face is refused: cover HOLDs at `C` and
fails at `D` because the unsigned union misses e_2; neighbor-read fails at
`C` and HOLDs at `D`. Identifying nm2simsly simultaneous with this
reverse/face is refused: simultaneous HOLDs at each of the four y-probes,
so face HOLDs; neighbor-read fails at `C`, so face fails. Identifying
nm2ot3sly O freeze with this reverse/face is refused: that leftover compares
outgoing sets at `t+1` and at `t+2`. Identifying nm2readslx same-lock
x-probe neighbor-read with this reverse is refused: that leftover has
non-seed `A` at tick 2 with `M={−e_3}` and HOLDs face; here `A` is a seed
at tick 0 with `M={+e_1}` and face fails. Identifying two-axis opposite
y-probe neighbor-read with this reverse is refused: opposite y-probes fail
reverse and fail face, with seed `A` locking `{−e_1}` and neighbor
`(0,1,1)` of `B` locking `{−e_2}`; here `A` locks `{+e_1}` and that
neighbor locks `{+e_2}`.

## Theorem 1 — ticks, `M` at probes and at formed 6-NN, and neighbor-read bit

On this process the four y-probes form. Incoming is frozen at formation:
`M(q,t+1)=M(q,t)` at every scored probe. Compare to two-axis opposite
y-probe neighbor-read: that leftover fails reverse and fails face with the
same ticks, but seed `A` locks `{−e_1}` and the formed neighbor `(0,1,1)` of
`B` locks `{−e_2}`. This two-axis same-lock member keeps the same y-probes
and the same perp-step process, but neither pair is opposite. Neighbor-read
HOLDs at `A`, at `B`, and at `D`, and fails at `C`. Reverse HOLDs. Face
fails. The match at `A` is the partner seed origin `(0,0,0)` with the same
letter `{+e_1}`. The match at `D` is `(1,0,0)` with the same letter
`{−e_3}`.

```text
t(A)=0
t(B)=1
t(C)=1
t(D)=2
M(A, τ) = {+e_1}
M(B, τ) = {+e_1}
M(C, τ) = {+e_2}
M(D, τ) = {−e_3}
neighbor-read(A) = hold
neighbor-read(B) = hold
neighbor-read(C) = fail
neighbor-read(D) = hold
formed 6-NN of A at τ: (1, 1, 0)=UNDEFINED, (-1, 1, 0)=UNDEFINED, (0, 2, 0)={+e_2}, (0, 0, 0)={+e_1}, (0, 1, 1)={+e_2}, (0, 1, -1)={−e_3}
formed 6-NN of B at τ: (2, 1, 1)=UNDEFINED, (0, 1, 1)={+e_2}, (1, 2, 1)={+e_2}, (1, 0, 1)={+e_1}, (1, 1, 2)={+e_1, +e_3}, (1, 1, 0)={−e_3}
formed 6-NN of C at τ: (1, 2, 0)={+e_1}, (-1, 2, 0)={−e_1}, (0, 1, 0)={+e_1}, (0, 2, 1)={+e_3}, (0, 2, -1)={+e_2, −e_3}
formed 6-NN of D at τ: (2, 1, 0)={+e_1}, (0, 1, 0)={+e_1}, (1, 2, 0)={+e_1}, (1, 0, 0)={−e_3}, (1, 1, 1)={+e_1}, (1, 1, -1)={+e_1}
matching 6-NN of A: (0, 0, 0)
matching 6-NN of B: (1, 0, 1)
matching 6-NN of C: none
matching 6-NN of D: (1, 0, 0)
```

`A` is a seed. `A` is the site `(0,1,0)` recorded at tick 0 with seed
letter `{+e_1}`. Mixed remains a set: `M((1,1,2),τ)` at `B`'s cut is
`{+e_1, +e_3}`, and `M((0,2,-1),τ)` at `C`'s cut is `{+e_2, −e_3}`.
Unique letters would assign `UNDEFINED` at those mixed neighbors. Here
uniqueness is not required. Empty match at `C` fails even though a mixed
neighbor carries `+e_2` as one letter of a larger set. `M` is frozen from
`t` to `τ=t+1` at each of the four y-probes. Unformed six-neighbors remain
`UNDEFINED` at the cut and do not match.

On the 1-axis same-lock two-site seed, reverse HOLDs and face fails with
the same `A` letter `{+e_1}`, but `t(B)=2` and `t(D)=3`, neighbor-read
fails at mixed `D`, and the formed neighbor `(0,1,1)` of `A` is a child
locking `{+e_3}`. That is leftover of the first pair. Here the second pair
is a new same-lock seed, `t(B)=1`, `t(D)=2`, neighbor-read HOLDs at `D`,
and `(0,1,1)` is a seed locking `{+e_2}`.

On the two-axis opposite seed with the same y-probes, neighbor-read fails
reverse and fails face: seed `A` locks `{−e_1}` and has no matching
six-neighbor, and neighbor `(0,1,1)` of `B` locks `{−e_2}`. Here those
sites lock `{+e_1}` and `{+e_2}` because neither pair is opposite. That
leftover is not this display.

On the two-axis same-lock x-probes, `A=(1,0,0)` is not a seed, `t(A)=2`
with `M={−e_3}`, and neighbor-read HOLDs reverse and HOLDs face. On the
two-axis same-lock z-probes, `A=(0,0,1)` is a seed at tick 0 with
`M={+e_2}`, and neighbor-read HOLDs reverse and HOLDs face, including at
`C`. Here `A` is the y-seed with `M={+e_1}`, and neighbor-read fails at
`C`.

## Theorem 2 — reverse from neighbor-read at `τ`

Reverse neighbor-read holds if and only if neighbor-read HOLDs at `A` and
at `B`. Neighbor-read HOLDs at `A` and HOLDs at `B`. Reverse HOLDs.

Reverse neighbor-read at τ: hold

Both sides are defined, so this is not `UNDEFINED`. nm2readslx same-lock
x-probe neighbor-read reverse HOLDs because non-seed `A` matches `D` on
`{−e_3}`; that leftover has `t(A)=2`, not `t(A)=0`. Two-axis opposite
y-probe neighbor-read reverse fails because neighbor-read fails at seed
`A`. nm2sl axis-cover reverse also HOLDs, but cover HOLDs at `C` while
neighbor-read fails at `C`. R-style recovery at `A` and at `B` is empty.
Those leftovers are not this display.

Reverse holds.

## Theorem 3 — face from neighbor-read at `τ`

Face neighbor-read holds if and only if neighbor-read HOLDs at `C` and at
`D`. Neighbor-read fails at `C` and HOLDs at `D`. Face fails.

Face neighbor-read at τ: fail

Displayed, not adopted. The bits are not written into Admissibility.
Do not write into Admissibility. Do not attach L1.

This is not `hold` and not `UNDEFINED`. Face fails.

On the same seed the four x-probes give reverse hold and face hold, with
non-seed `A` at tick 2 and `M(A,τ)={−e_3}`. The four z-probes give reverse
hold and face hold, with seed `A` at tick 0 and `M(A,τ)={+e_2}`. Those
probe-direction readouts are not this y-probe display.

nm2sl cover face also fails, but because cover fails at `D`, while
neighbor-read HOLDs at `D` and fails at `C`. nm2simsly simultaneous face
HOLDs. nm2slo timed-O face HOLDs. 1-axis same-lock face fails from a miss
at mixed `D`, not from a miss at `C`. Two-site opposite leftover face
fails. Those leftovers are not this display.

Face fails.

## What this note does not claim

- It does not select a unique incoming lock.
- It does not reduce lock vectors to named signs `{+,−}`.
- It does not require neighbor-read sides to be singletons.
- It does not sum the incoming set.
- It does not replace neighbor-read by R-style recovery.
- It does not replace neighbor-read by nm2slo timed-O exist-opposite.
- It does not replace neighbor-read by nm2sl axis-cover.
- It does not replace neighbor-read by nm2simsly simultaneous.
- It does not replace neighbor-read by nm2ot3sly O freeze.
- It does not replace neighbor-read by nm2readslx same-lock x-probe neighbor-read.
- It does not replace neighbor-read by nm2readslz same-lock z-probe neighbor-read.
- It does not replace neighbor-read by two-axis opposite y-probe neighbor-read.
- It does not use a six-neighbor star as the letter.
- It does not wait for a global later T.
- It does not attach a formation member from already-recorded six-neighbor
  locks.
- It does not reprint 1-axis same-lock neighbor-read as this member.
- It does not reprint two-axis same-lock x-probe neighbor-read.
- It does not reprint two-axis same-lock z-probe neighbor-read.
- It does not treat the second same-lock pair as a formed child of the first.
- It does not score the x-probes or the z-probes as this letter.
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
two-axis same-lock four-site process, neighbor-read of `M` at `t+1`, and the
reverse/face bits from that neighbor-read are displayed theorem-domain data.

## Exact target and obligation graph

| Obligation | Status |
|---|---|
| current Lattice / Admissibility / Record premises | quoted; no edit |
| perp-step incoming-lock process on `B_3(0)` | displayed; two disjoint same-lock pairs `+e_1/+e_1` and `+e_2/+e_2` |
| ticks `t(A)`, `t(B)`, `t(C)`, `t(D)` | Theorem 1; `0`, `1`, `1`, `2` |
| `M` at `τ=t+1` | Theorem 1; frozen equal to `M` at `t` |
| `M` at formed 6-NN | Theorem 1; origin matches `A` on `{+e_1}`; empty match at `C` |
| neighbor-read bit at `τ` | Theorem 1; HOLD at `A`,`B`,`D`; FAIL at `C` |
| reverse from neighbor-read at `τ` | Theorem 2; `hold` |
| face from neighbor-read at `τ` | Theorem 3; `fail` |
| compare to two-axis opposite y-probe neighbor-read | Theorem 1; opposite fails reverse/face; seed `A` locks `{−e_1}` and neighbor `M` at `(0,1,1)` differs by sign |
| compare to nm2readslx same-lock x-probe neighbor-read | Theorem 1; same-lock x has non-seed `A` at tick 2 with `M={−e_3}` and HOLDs face; here `t(A)=0` and face fails |
| compare to nm2readslz same-lock z-probe neighbor-read | Theorem 1; same-lock z has seed `A` at tick 0 with `M={+e_2}` and HOLDs at `C`; here `M={+e_1}` and `C` fails |
| compare to 1-axis same-lock neighbor-read | Theorem 1; 1-axis HOLDs reverse and fails face with `t(D)=3` and a miss at mixed `D`; this member has `t(D)=2` and HOLDs at `D` |
| unique incoming lock | not required |
| occupancy of sites as the letter | not used |
| named-sign `{+,−}` letter | not used |
| singleton unique lock-vector letter | not used as the object; mixed remains a set |
| `Z^3` sum of the lock set | not used; no aggregation |
| six-neighbor star as the letter | not used |
| leftover of nm2slo timed-O exist-opposite | not this neighbor-read display |
| leftover of nm2sl axis-cover | not this display |
| leftover of nm2simsly simultaneous | not this display |
| leftover of nm2ot3sly O freeze | not this display |
| leftover of nm2readslx same-lock x-probe neighbor-read | not this display |
| leftover of nm2readslz same-lock z-probe neighbor-read | not this display |
| leftover of two-axis opposite y-probe neighbor-read | not this display |
| leftover of R-style | not this display |
| leftover of 1-axis same-lock neighbor-read | not this display |
| leftover of x-probe neighbor-read | not this display |
| leftover of z-probe neighbor-read | not this display |
| leftover of x-axis same-lock y-probe neighbor-read | not this display |
| global later T | not used |
| neighbor-read as Admissibility content | not adopted |
| formation site / probability / rate | open |
| physical Record readout of the bits | open |

## Value gate (V1–V5)

| # | Answer |
|---|---|
| V1 | It answers the first-display question: neighbor-read of `M` at `t+1` on the four y-probes of the two-axis same-lock seed, compared to nm2readslx and to two-axis opposite y-probe neighbor-read, and reverse/face from those bits. |
| V2 | Current main has no landed neighbor-read reverse/face of timed `M` on these four two-axis same-lock y-probes. |
| V3 | Neighbor-read reports at one cut and the two reverse/face bits are independently finite and exact. |
| V4 | The theorem is more than a restatement of Record because it reads set-equality of own incoming `M` at a formed six-neighbor at the same `t+1` cut. |
| V5 | It is not an adopted content rule: the bits remain displayed. |

## No-go discipline gate

The negative content is narrow: the display does not write those bits into
Admissibility, does not reduce them to named signs, does not require a
unique lock, does not replace neighbor-read by R-style recovery, does not
replace neighbor-read by nm2slo timed-O, does not replace neighbor-read
by nm2sl axis-cover, does not replace neighbor-read by nm2simsly
simultaneous, does not replace neighbor-read by nm2ot3sly O freeze, and
does not identify this display with nm2readslx or with two-axis opposite
y-probe neighbor-read. No global impossibility is claimed.

### N1 — materially distinct routes

| Route | Attempt | Why it fails here | Marker |
|---|---|---|---|
| two-axis opposite y-probe neighbor-read | reuse seed `+e_1/−e_1` and `+e_2/−e_2` on these y-probes | opposite fails reverse/face; `M(A,τ)={−e_1}` and `M((0,1,1),τ)={−e_2}` there; here `A` locks `{+e_1}` and that neighbor locks `{+e_2}` | ATTEMPTED |
| nm2readslx same-lock x-probe neighbor-read | reuse seed `+e_1/+e_1` and `+e_2/+e_2` on x-probes | that leftover has non-seed `A` at tick 2 with `M={−e_3}` and HOLDs face; here `A` is a seed, `t(A)=0`, `M={+e_1}`, and face fails | ATTEMPTED |
| nm2readslz same-lock z-probe neighbor-read | reuse the same seed on z-probes | that leftover has seed `A` at tick 0 with `M={+e_2}` and HOLDs at `C`; here `M={+e_1}` and `C` fails | ATTEMPTED |
| nm2slo timed-O exist-opposite | score exist-opposite of signed `O` | timed-O HOLDs reverse and HOLDs face; neighbor-read HOLDs reverse and fails face; `O` is not `M` | ATTEMPTED |
| nm2sl axis-cover | reuse cover of `M` and `O` | cover HOLDs at `C` and fails at `D`; neighbor-read fails at `C` and HOLDs at `D`; same reverse/face bits, opposite `C`/`D` pattern | ATTEMPTED |
| nm2simsly simultaneous | score nonempty disjoint `M` and `O` | simultaneous HOLDs at each y-probe, so face HOLDs; neighbor-read fails at `C`, so face fails | ATTEMPTED |
| nm2ot3sly O freeze | compare `O(t+1)` with `O(t+2)` | that leftover is outgoing freeze across two later cuts; neighbor-read is set-equality of incoming `M` at a formed 6-NN at `t+1` | ATTEMPTED |
| R-style recovery | recover incoming as `−e` in `M(q+e,τ)` | R-style at `A`,`B`,`C` is empty; at `D` is `{−e_1}` unequal to `{−e_3}`; neighbor-read HOLDs at `A`,`B`,`D` and fails at `C` | ATTEMPTED |
| 1-axis same-lock neighbor-read | reuse seed `{0,(0,1,0)}` with `+e_1/+e_1` | 1-axis HOLDs reverse and fails face with `t(D)=3` and a miss at mixed `D`; here `t(D)=2` and `D` HOLDs | ATTEMPTED |
| two-site opposite leftover | reuse opposite `+e_1/−e_1` without the second pair | that leftover fails reverse and face; this member HOLDs reverse from four same-lock seeds | ATTEMPTED |
| unique letter | replace mixed sets by a singleton or `UNDEFINED` | mixed neighbor `M((0,2,-1),τ)={+e_2,−e_3}` remains a set; unique-letter is `UNDEFINED` while neighbor-read fails at `C` from empty exact match | ATTEMPTED |
| x-probe neighbor-read | score the four x-probes on this seed | x-probe reverse HOLDs and face HOLDs with non-seed `A` at tick 2; this letter is the four y-probes | ATTEMPTED |
| z-probe neighbor-read | score the four z-probes on this seed | z-probe `t(A)=0` with `M={+e_2}` and HOLDs at `C`; this letter fails at `C` with `M={+e_1}` | ATTEMPTED |
| x-axis same-lock y-probe | reuse seed `{0,(1,0,0)}` with `+e_2/+e_2` | different seed; this letter is two-axis same-lock on `+e_1/+e_1` and `+e_2/+e_2` | ATTEMPTED |
| z-symmetric leftover | reuse seed `{0,(0,0,1),(0,0,-1)}` | that leftover has `t(A)=1` and `M(A,τ)={+e_2}`; here `A` is a seed at tick 0 with `M={+e_1}` | ATTEMPTED |
| perp two-site leftover | reuse seed `{0,(0,1,0)}` with `+e_1/+e_2` | perp fails at each y-probe; this member HOLDs reverse | ATTEMPTED |
| named-sign lettering | collapse `{±e_i}` to `{+,−}` | named-sign lettering lost the set | ATTEMPTED |
| global later T | wait until `max t(A,B,C,D)` before reading | `τ(q)=t(q)+1` is per-probe; no global T | ATTEMPTED |
| attach a formation member from already-recorded six-neighbor locks | form the probes by a neighbor-lock letter instead of perp-step | refused; not attached | ATTEMPTED |
| adopt bits into Admissibility | rewrite the local rule by neighbor-read | refused; displayed, not adopted | ATTEMPTED |

### N2 — wall independence

Missing physical adoption, missing identification of neighbor-read with
R-style recovery, missing identification of neighbor-read with nm2slo
timed-O, missing identification of neighbor-read with nm2sl axis-cover,
missing identification of neighbor-read with nm2simsly simultaneous,
missing identification of neighbor-read with nm2ot3sly O freeze, missing
identification of this member with nm2readslx, missing identification of
this member with two-axis opposite y-probe neighbor-read, and missing
Record identification of neighbor-read reverse are distinct open premises.
This note claims no complete wall collection.

### N3 — hidden-condition scan

The host `B_3(0)`, four-site two-axis same-lock seed, perpendicular step
rule, incoming-step lock, own incoming set from records with tick `<= τ`,
per-probe `τ=t+1`, neighbor-read as set-equality of `M` at a formed
six-neighbor, four y-probes with seed `A`, and mixed remains a set are
declared. No uniqueness of incoming locks, no R-style recovery as the
scored object, no axis-cover as the scored object, no forall-perp as the
scored object, no simultaneous as the scored object, no timed-O as the
scored object, no O freeze as the scored object, no global later T, no
formation attachment from already-recorded six-neighbor locks, and no
Admissibility rewrite are silently assumed.

### N4 — source residual matching

The current axiom memo supplies cubic sites, `M_2(C)`,
content-conditional-on-formation, and unreadable absence. The residual that
formation site, probability, and rate remain unsupplied is unchanged. The
neighbor-read reverse hold and face fail reports do not close that residual.

### N5 — resolution and rhetoric audit

| Resolution | Executed | Not claimed |
|---|---|---|
| per element | each earliest incoming lock set `M` at a probe and at formed 6-NN | no continuum alphabet |
| per site | `A,B,C,D` y-probes on `B_3(0)` only | no other cubic sites |
| per mode | no mode calculation | no spectral exhaustion |
| per block | four neighbor-read reports, reverse/face from those bits | no adopted content law |
| lattice wide | checked and not executed | no lattice-wide lettering rule |

### N6 — live partial-closure paths

Live routes include a later Record content map for neighbor-read reverse/face,
a formation-rate rule, and a physical selector among matching six-neighbors.
None is taken here.

### N7 — hostile steelman

**Steelman:** Two-axis same-lock neighbor-read on y-probes is leftover of
two-axis opposite y-probe neighbor-read because only a sign of two seed
letters changed; leftover of nm2readslx because the same seed already HOLD
reverse on x-probes; leftover of nm2readslz because seed `A` already matches
a partner seed; leftover of nm2sl cover because reverse HOLD face FAIL is
already the cover report; leftover of nm2simsly simultaneous because `M`
and `O` are already disjoint; leftover of nm2slo timed-O because `O`
already carries opposite letters; leftover of nm2ot3sly because outgoing
already freezes; leftover of R-style because some neighbor already carries
an opposite step; leftover of 1-axis same-lock because reverse HOLD face
FAIL is already that report; and uniqueness of `M` already answers the
match.

**Answer:** Opposite y-probes fail reverse and fail face: seed `A` locks
`{−e_1}` with no matching six-neighbor, and `M((0,1,1),τ)={−e_2}` there.
Here `A` locks `{+e_1}` and matches origin, and that neighbor locks
`{+e_2}`. nm2readslx has non-seed `A` at tick 2 with `M={−e_3}` and HOLDs
face; here `A` is a seed, `t(A)=0`, `M={+e_1}`, and face fails.
nm2readslz has seed `A` with `M={+e_2}` and HOLDs at `C`; here `C` fails.
nm2sl cover HOLDs at `C` and fails at `D`; neighbor-read fails at `C` and
HOLDs at `D`. Simultaneous HOLDs at each probe, so face HOLDs; neighbor-read
face fails. Timed-O HOLDs face from opposite letters in `O`; neighbor-read
does not score `O`. O freeze compares two later outgoing cuts. R-style at
`A` is empty, not `{+e_1}`. 1-axis fails at mixed `D` with `t(D)=3`; here
`D` HOLDs at tick 2. Mixed neighbor `M((0,2,-1),τ)={+e_2,−e_3}` remains a
set; uniqueness is not required. Reverse neighbor-read is HOLD iff
neighbor-read at `A` and at `B`, not leftover of opposite y-probe
neighbor-read and not leftover of nm2readslx.

### N8 — cross-cycle echo

nm2readslx reported neighbor-read of `M` on two-axis same-lock x-probes
with reverse hold and face hold from non-seed `A` at tick 2. nm2readslz
reported neighbor-read of `M` on two-axis same-lock z-probes with reverse
hold and face hold from seed `A` at tick 0 with `M={+e_2}`. Two-axis
opposite y-probe neighbor-read reports FAIL at `A` and at `C`, reverse
fail, and face fail, with seed `A` locking `{−e_1}`. nm2slo reported
exist-opposite of signed `O` on these four y-probes with reverse hold and
face hold. nm2sl reported axis-cover of `M` versus `O` on these four
y-probes with reverse hold and face fail because the union misses e_2 at
`D`. nm2simsly reported simultaneous `M` and `O` on these four y-probes
with reverse hold and face hold. nm2ot3sly reported O freeze of `t+1`
versus `t+2` on these four y-probes. 1-axis same-lock neighbor-read reports
hold reverse and fail face with `t(D)=3` and a miss at mixed `D`. This
note is not those displays: it reports neighbor-read of `M` at `τ=t+1` on
two disjoint same-lock pairs with y-probes, HOLD at `A`,`B`,`D`, FAIL at
`C`, reverse hold, and face fail. HOLD iff some formed 6-NN recovers `M`
as a set, not leftover of opposite y-probe neighbor-read, and not leftover
of nm2readslx.

**Gate disposition:** PASS for the neighbor-read `t+1` reverse/face reports
above. FAIL / DO NOT SHIP for “the predicate equals the named sign,” “the
predicate equals the unique singleton lock vector,” “the predicate equals
R-style recovery,” “the predicate equals nm2slo timed-O,” “the predicate
equals nm2sl axis-cover,” “the predicate equals nm2simsly simultaneous,”
“the predicate equals nm2ot3sly O freeze,” “the predicate equals
nm2readslx,” “the predicate equals two-axis opposite y-probe neighbor-read,”
“bits are Admissibility,” “neighbor-read fails at `A`,” “neighbor-read
HOLDs at `C`,” “reverse neighbor-read fails,” or “face neighbor-read
holds.”

## Primary runner

The paired runner builds Euclidean `B_3(0)`, runs the two-axis same-lock
perp-step incoming-lock process, reads each y-probe's own earliest incoming
set from the record prefix at that probe's `t+1`, reports `M` at each formed
six-neighbor, reports neighbor-read as set-equality of those incoming sets,
lists matching six-neighbors, compares to two-axis opposite y-probe
neighbor-read and to nm2readslx, and checks Theorems 1--3. It also checks
that neighbor-read HOLDs at `A` from matching origin, that R-style recovery
differs, that mixed sets remain sets, that unique-letter is `UNDEFINED` at
mixed neighbors, that the construction does not sum, that a formation member
from already-recorded six-neighbor locks is not attached, and that the
display is not leftover of nm2sl axis-cover. No runner cache is written.
