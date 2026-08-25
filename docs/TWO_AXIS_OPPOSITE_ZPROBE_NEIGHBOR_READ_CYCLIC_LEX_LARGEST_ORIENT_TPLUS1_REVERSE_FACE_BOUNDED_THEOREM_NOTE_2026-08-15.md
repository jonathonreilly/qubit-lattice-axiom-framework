---
claim_id: two_axis_opposite_zprobe_neighbor_read_cyclic_lex_largest_orient_tplus1_reverse_face_bounded_theorem_note_2026-08-15
claim_type: bounded_theorem
claim_scope: "Neighbor-read of the cyclic lex-largest orientation at t+1 on the four z-probes of the two-axis opposite seed, and reverse/face from that, are reported. Displayed, not adopted."
upstream_dependencies:
  - minimal_axioms
runner: scripts/two_axis_opposite_zprobe_neighbor_read_cyclic_lex_largest_orient_tplus1_reverse_face_2026_08_15.py
---

# Neighbor-Read Of Cyclic Lex-Largest Orientation At t+1 Reverse And Face On Four Z-Probes Of The Two-Axis Opposite Seed

> **Key terms used in this doc** are indexed A-Z at `docs/KEY_TERMINOLOGY.md`;
> each row points to the canonical source-of-truth doc.

**Date:** 2026-08-15
**Type:** bounded_theorem
**Scope:** neighbor-read of the cyclic next/prev lex-largest outgoing
determinant orientation of the 1-in 2-out frame of simultaneous earliest
incoming set `M` and outgoing dual `O` at each probe's `τ=t+1`, and
reverse/face from that neighbor-read, on the four z-probes of the two-axis
opposite seed in `B_3(0)={n:n·n<=9}`. Same process and z-probes as nm2axz.
Orient as nm2oricyclz. Let `t(q)` be the formation tick of probe `q`. Let
`τ(q)=t(q)+1`. `M(q,τ)` is the set of earliest incoming nearest-neighbor
steps at `q` using only records with tick `<= τ`. Seeds are a singleton
seed letter. `O(q,τ)` is the outgoing dual of `M`: the set of `e` in
`{±e_1,±e_2,±e_3}` such that `q+e` is formed and `e` is in `M(q+e,τ)`.
Unformed at `τ` is `UNDEFINED`. Empty `O` is empty, not `UNDEFINED`. Split
HOLDs at `q` if and only if cover HOLDs and `|Axis(M)|=1`. When split
HOLDs, `m` is unique in `M`. `e_next = e_{i+1}` with `3+1→1`. `e_prev =
e_{i-1}` with `1−1→3`. Order `+e < −e`. `o_next` is the lex-largest vector
in `O ∩ {±e_next}`. `o_prev` likewise. `Orient(q)` is the sign of the
integer determinant of columns `m`, `o_next`, `o_prev`. If split fails,
Orient fails, not `UNDEFINED`. Neighbor-read HOLDs at `q` if and only if
`Orient(q)` is `±1` and some formed 6-NN `r` has `Orient(r)=Orient(q)` both
`±1` at the same cut `τ(q)`. If Orient fails at `q`, neighbor-read fails,
not `UNDEFINED`. Unformed `q` is `UNDEFINED`. Uniqueness is not required.
Mixed remains a set. Reverse HOLDs if and only if neighbor-read HOLDs at
`A` and at `B`. Face HOLDs if and only if neighbor-read HOLDs at `C` and
at `D`. This is not leftover of nm2oricyclz cyclic lex-largest Orient
reverse hold and face hold. This is not leftover of nm2oreadz neighbor-read
of O. This is not leftover of nm2readz neighbor-read of M. This is not
leftover of nm2axz axis-cover. This is not leftover of nm2ax12z 1-in 2-out
split. This is not leftover of nm2orichz leftover-axis. This is not leftover
of cyclic lex-smallest. Occupancy of sites is not used. Named-sign
lettering is not used. Displayed, not adopted. Do not write into
Admissibility. Do not attach L1.
**Audit-status authority:** independent audit lane only. This note authors no
audit verdict and predicts none.
**Primary runner:**
[`scripts/two_axis_opposite_zprobe_neighbor_read_cyclic_lex_largest_orient_tplus1_reverse_face_2026_08_15.py`](../scripts/two_axis_opposite_zprobe_neighbor_read_cyclic_lex_largest_orient_tplus1_reverse_face_2026_08_15.py)

Framework input:

- [`MINIMAL_AXIOMS_2026-06-29.md`](MINIMAL_AXIOMS_2026-06-29.md) supplies
  cubic-lattice sites `Z^3` with nearest-neighbor adjacency, the one-site
  algebra `M_2(C)`, and the Record sentences that records form and that a
  present record locks exactly one admissible local possibility.

Everything after that quoted input is a finite displayed process on `B_3(0)`
and the four named z-probes. Incoming lock letters are unit nearest-neighbor
steps. `O` is the outgoing dual of those incoming sets at the per-probe cut
`τ=t+1`. Orient is the cyclic next/prev lex-largest outgoing determinant of
the 1-in 2-out frame. Neighbor-read asks whether a formed six-neighbor
recovers that same `±1` Orient sign at the same cut, without being the
probe itself. Reverse and face are scored on neighbor-read HOLD at the
paired probes. Named signs `{+,−}` are a coarser readout and are not used.
A singleton unique lock letter is a different readout and is not used as
the object. Axis-cover of `M` and `O` is a different readout and is not
used. 1-in 2-out split is a different readout and is not used. Equal Orient
signs at `A` and at `B` are a different readout and are not used as this
reverse. Neighbor-read of `O` is a different readout and is not used.
Neighbor-read of `M` is a different readout and is not used. Leftover-axis
Orient is a different readout and is not used. Cyclic lex-smallest Orient
is a different readout and is not used. A `Z^3` sum of those locks is a
different readout and is not used. Occupancy of sites is not used. A
six-neighbor star is not the letter.

## Machine status and trace

```yaml
actual_current_surface_status: bounded-support
target_claim_type: bounded_theorem
claim_type_reason: "Exact report of neighbor-read of cyclic lex-largest Orient at t+1 on the four z-probes of the two-axis opposite seed, neighbor-read bits at each probe, reverse fail and face fail from those bits; uniqueness of outgoing locks is not claimed and the bits are not adopted."
trace_class: frontier_discovery
target_claim_id: two_axis_opposite_zprobe_neighbor_read_cyclic_lex_largest_orient_tplus1_reverse_face
target_blocker_text: "display neighbor-read of cyclic lex-largest Orient at t+1 on the four z-probes of the two-axis opposite seed, HOLD iff some formed 6-NN recovers the same Orient sign"
source_of_blocker_text: handoff
reachability_to_target: advances
artifact_role: theorem
next_trace_action: "Keep neighbor-read of cyclic lex-largest Orient at t+1 displayed; do not write neighbor-read into Admissibility, do not reduce to neighbor-read of O or of M, do not reduce to nm2oricyclz equal-sign reverse, do not reduce to leftover-axis neighbor-read, do not reduce to cyclic lex-smallest neighbor-read, do not reduce to axis-cover or 1-in 2-out split, and do not attach L1."
conditional_surface_status: "exact on B_3(0) for neighbor-read of cyclic lex-largest Orient at t+1 on the four z-probes of the two-axis opposite seed and reverse/face from that; displayed, not adopted"
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
neighbor-read of cyclic lex-largest Orient is scored:

```text
A = (0,0,1),  B = (1,1,1),  C = (0,0,2),  D = (1,0,1).
```

These are not the y-probes `A=(0,1,0)`, `B=(1,1,1)`, `C=(0,2,0)`,
`D=(1,1,0)`. These are not the x-probes `A=(1,0,0)`, `B=(1,1,1)`, `C=(2,0,0)`,
`D=(1,1,0)`. `A` is a seed of the second opposite pair. Same process and
z-probes as nm2axz.

Lock alphabet of the displayed process: `{±e_i}` with `i` in `{1,2,3}`.

Seed: two disjoint opposite pairs recorded at formation tick 0. Origin
locks `+e_1`. Site `(0,1,0)` locks `−e_1`. Site `(0,0,1)` locks `+e_2`.
Site `(0,1,1)` locks `−e_2`. The second pair is a new seed, not a formed
child of the first pair. This seed is not the 1-axis opposite two-site seed
`{0,(0,1,0)}` with only `+e_1/−e_1`. This seed is not the perp two-site
seed `+e_1/+e_2`. This seed is not the same-lock two-site seed
`+e_1/+e_1`. This seed is not the z-symmetric three-site seed
`{0,(0,0,1),(0,0,-1)}`.

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

## Named neighbor-read of cyclic lex-largest Orient at `τ=t+1`

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

Cover HOLDs iff `Axis(M)` intersect `Axis(O)` is empty and `Axis(M)` union
`Axis(O)` equals `{e_1,e_2,e_3}`. Split HOLDs iff cover HOLDs and
`|Axis(M)|=1`. Cover and split do not score handedness.

Oriented frame at the same cut, as nm2oricyclz:

```text
When split HOLDs, m is the unique signed letter in M.
i in {1,2,3} is the axis index of m.
e_next = e_{i+1} with 3+1→1. e_prev = e_{i-1} with 1−1→3.
O_next = O ∩ {±e_next}. O_prev = O ∩ {±e_prev}.
If either is empty, Orient fails, not UNDEFINED.
Order +e < −e. o_next is lex-largest in O_next (hence −e if both signs).
o_prev likewise.
Orient(q) = sign of the integer determinant of columns (m, o_next, o_prev).
Else fail, not UNDEFINED, if split fails.
UNDEFINED if M or O is UNDEFINED.
```

Neighbor-read at a probe at the same cut:

```text
neighbor-read(q) HOLDs iff Orient(q) is ±1 and some formed 6-NN r
has Orient(r, τ(q)) = Orient(q) both ±1.
```

If `q` is unformed at `τ`, then neighbor-read is `UNDEFINED`. If Orient
fails at `q`, neighbor-read fails, not `UNDEFINED`. Else if no formed
six-neighbor recovers the same `±1` sign, neighbor-read fails. The probe
is not counted as its own neighbor. Empty matching is fail, not
`UNDEFINED`. Mixed remains a set: mixed `O` may still define a sign, and
that sign may still fail to match any neighbor.

Reverse neighbor-read holds if and only if neighbor-read HOLDs at `A` and
at `B`. Face neighbor-read holds if and only if neighbor-read HOLDs at `C`
and at `D`. Either side `UNDEFINED` is `UNDEFINED`. Else if both sides HOLD,
reverse or face HOLDs. Else fail.

Identifying neighbor-read of Orient with neighbor-read of `O` is refused:
neighbor-read of `O` HOLDs at `A` from the partner seed sharing the outgoing
set, while neighbor-read of Orient fails at `A` because that partner has
the opposite sign. Identifying neighbor-read of Orient with neighbor-read
of `M` is refused: neighbor-read of `M` HOLDs at `B`, `C`, and `D`.
Identifying this reverse with nm2oricyclz equal-sign reverse is refused:
Orient reverse HOLDs from `Orient(A)=Orient(B)=−1`, while this reverse
fails because neither reverse probe has a matching neighbor. Identifying
this reverse with leftover-axis neighbor-read is refused: leftover-axis
neighbor-read HOLDs at `B`, `C`, and `D` and leftover-axis face HOLDs.
Identifying this reverse with cyclic lex-smallest neighbor-read is refused:
lex-smallest neighbor-read HOLDs at `A` from the origin matching `+1`.
Identifying neighbor-read with axis-cover or 1-in 2-out split is refused:
those objects HOLD at each of these four z-probes.

## Theorem 1 — ticks, `M`, `O`, Orient, neighbor-read at `τ=t+1`

On this process the four z-probes form. Compare to nm2oricyclz: that leftover
reports Orient `−1,−1,+1,+1`, reverse hold, and face hold from equal `±1`
signs. Compare to nm2oreadz: that leftover reports neighbor-read of `O`
hold at `A` and fail at `B`, `C`, and `D`. This display reads whether a
formed six-neighbor recovers the cyclic lex-largest Orient sign:

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
O(B, τ) = {+e_2, +e_3, −e_3}
O(C, τ) = {+e_1, −e_1, −e_2}
O(D, τ) = {−e_2, +e_3, −e_3}
Orient(A) = −1
Orient(B) = −1
Orient(C) = +1
Orient(D) = +1
neighbor-read(A) = fail
neighbor-read(B) = fail
neighbor-read(C) = fail
neighbor-read(D) = fail
formed 6-NN of A at τ: (1, 0, 1)=fail, (-1, 0, 1)=fail, (0, 1, 1)=+1, (0, -1, 1)=UNDEFINED, (0, 0, 2)=fail, (0, 0, 0)=+1
formed 6-NN of B at τ: (2, 1, 1)=UNDEFINED, (0, 1, 1)=+1, (1, 2, 1)=fail, (1, 0, 1)=+1, (1, 1, 2)=fail, (1, 1, 0)=fail
formed 6-NN of C at τ: (1, 0, 2)=fail, (-1, 0, 2)=fail, (0, 1, 2)=−1, (0, -1, 2)=fail, (0, 0, 1)=−1
formed 6-NN of D at τ: (2, 0, 1)=UNDEFINED, (0, 0, 1)=−1, (1, 1, 1)=−1, (1, -1, 1)=fail, (1, 0, 2)=fail, (1, 0, 0)=fail
matching 6-NN of A: none
matching 6-NN of B: none
matching 6-NN of C: none
matching 6-NN of D: none
```

`A` is a seed at tick 0 with seed letter `+e_2`. The partner of that pair,
`(0,1,1)`, is also a seed at tick 0 with seed letter `−e_2`. At `τ=1` those
two seeds share the same outgoing set `{+e_1, −e_1, +e_3}`, so neighbor-read
of `O` HOLDs at `A`. They do not share Orient: flipping `m` from `+e_2` to
`−e_2` flips the determinant, so Orient at the partner is `+1` while Orient
at `A` is `−1`. Origin `(0,0,0)` also reports Orient `+1`. No formed
six-neighbor recovers `−1` at `A`. Mixed remains a set: `O(A,τ)` has three
outgoing steps and still defines Orient `−1`. Unique letters would assign
`UNDEFINED` at mixed `O`. Here uniqueness is not required. At `t`, `O` is
empty at each probe, split fails, Orient fails, and neighbor-read fails,
not `UNDEFINED`. `M` is frozen from `t` to `t+1`; `O` is not. O is not M.

On the 1-axis opposite two-site seed, `A=(0,0,1)` is a formed child at
tick 1 locking `+e_3`, neighbor-read of cyclic Orient HOLDs at `A` from
the origin, and reverse HOLDs. That is leftover of the first pair. Here
both `(0,0,1)` and `(0,1,1)` are seeds of a second opposite pair on a
second axis, and neighbor-read fails at `A`.

New records in `B_3(0)` between `t` and `t+1` that meet a probe's
six-neighbors enter `O` and do not enter earliest `M`. Site `(0,1,1)` is a
seed, so it is not a new 6-NN of `A`:

```text
new 6-NN of A at t(A)+1: (1, 0, 1), (-1, 0, 1), (0, 0, 2)
new 6-NN of B at t(B)+1: (1, 2, 1), (1, 1, 2), (1, 1, 0)
new 6-NN of C at t(C)+1: (1, 0, 2), (-1, 0, 2), (0, -1, 2)
new 6-NN of D at t(D)+1: (1, -1, 1), (1, 0, 2), (1, 0, 0)
```

Those new six-neighbors have empty `O` at the probe cut, so their Orient
fails and they do not match.

## Theorem 2 — reverse from neighbor-read of Orient at `τ`

Reverse neighbor-read holds if and only if neighbor-read HOLDs at `A` and
at `B`. Neighbor-read fails at `A` and at `B`. Reverse fails. This is HOLD
iff neighbor-read at both reverse probes, not leftover of nm2oricyclz
equal-sign reverse, not leftover of nm2oreadz neighbor-read of O.

Reverse neighbor-read at τ: fail

Both sides are defined, so this is not `UNDEFINED`. nm2oricyclz Orient
reverse HOLDs because `Orient(A)=−1` and `Orient(B)=−1`. Cover reverse
HOLDs. Split reverse HOLDs. Neighbor-read of `O` reverse fails from hold
at `A` with fail at `B`. Neighbor-read of `M` reverse fails from fail at
`A` with hold at `B`. Leftover-axis neighbor-read reverse fails from fail
at `A` with hold at `B`. Cyclic lex-smallest neighbor-read reverse fails
from hold at `A` with fail at `B`. Those leftovers are not this display.

Reverse fails.

## Theorem 3 — face from neighbor-read of Orient at `τ`

Face neighbor-read holds if and only if neighbor-read HOLDs at `C` and at
`D`. Neighbor-read fails at `C` and at `D`. Face fails.

Face neighbor-read at τ: fail

Displayed, not adopted. The bits are not written into Admissibility.
Do not write into Admissibility. Do not attach L1.

nm2oricyclz Orient face HOLDs because both signs are `+1`. Cover face HOLDs.
Split face HOLDs. Neighbor-read of `M` has face hold. Leftover-axis
neighbor-read has face hold. Neighbor-read of `O` has face fail, but from
a different object: set equality of `O`, not equal Orient signs. At `C`,
formed neighbors report Orient `−1` at `(0,1,2)` and at `A`, opposite to
`Orient(C)=+1`. At `D`, formed neighbors report Orient `−1` at `A` and at
`B`, opposite to `Orient(D)=+1`.

On the same seed the four y-probes give neighbor-read hold at `A` and at
`C` and fail at `B` and at `D`, so reverse fail and face fail, but from
hold at y-probe `A`, not fail at z-probe `A`. The four x-probes fail at
each probe from Orient fail at `A` and at `D`. Those probe-direction
readouts are not this z-probe display.

Face fails.

## What this note does not claim

- It does not select a unique outgoing or leftover lock.
- It does not reduce lock vectors to named signs `{+,−}`.
- It does not require neighbor-read sides to be singletons.
- It does not sum either set.
- It does not replace neighbor-read of Orient by neighbor-read of `O`.
- It does not replace neighbor-read of Orient by neighbor-read of `M`.
- It does not replace neighbor-read by nm2oricyclz equal-sign reverse.
- It does not replace neighbor-read by leftover-axis neighbor-read.
- It does not replace neighbor-read by cyclic lex-smallest neighbor-read.
- It does not replace neighbor-read by axis-cover of `M` and `O`.
- It does not replace neighbor-read by 1-in 2-out split.
- It does not treat Orient fail as `UNDEFINED`.
- It does not treat empty matching as `UNDEFINED`.
- It does not replace `O` by `M`.
- It does not replace neighbor-read by locks of six-neighbors.
- It does not use a six-neighbor star as the letter.
- It does not wait for a global later T.
- It does not attach a formation member from already-recorded six-neighbor
  locks.
- It does not reprint nm2oricyclz Orient reverse hold and face hold.
- It does not reprint nm2oreadz neighbor-read of `O`.
- It does not reprint nm2readz neighbor-read of `M`.
- It does not reprint nm2axz axis-cover reverse hold and face hold.
- It does not reprint nm2ax12z 1-in 2-out reverse hold and face hold.
- It does not reprint nm2orichz leftover-axis reverse hold and face fail.
- It does not treat the second opposite pair as a formed child of the first.
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
two-axis opposite process, neighbor-read of cyclic lex-largest Orient at
`t+1`, and the reverse/face bits from that neighbor-read are displayed
theorem-domain data.

## Exact target and obligation graph

| Obligation | Status |
|---|---|
| current Lattice / Admissibility / Record premises | quoted; no edit |
| perp-step incoming-lock process on `B_3(0)` | displayed; two disjoint opposite pairs `+e_1/−e_1` and `+e_2/−e_2` |
| ticks `t(A)`, `t(B)`, `t(C)`, `t(D)` | Theorem 1; `0`, `1`, `1`, `1` |
| `M` at `τ=t+1` | Theorem 1; frozen equal to `M` at `t` |
| `O` at `τ=t+1` | Theorem 1; HOLDING outgoing dual |
| Orient at `τ` | Theorem 1; `−1`, `−1`, `+1`, `+1` |
| Orient at formed 6-NN | Theorem 1; reported at each eventually-formed neighbor |
| neighbor-read bit at `τ` | Theorem 1; fail, fail, fail, fail |
| reverse from neighbor-read at `τ` | Theorem 2; `fail` |
| face from neighbor-read at `τ` | Theorem 3; `fail` |
| unique outgoing lock | not required |
| occupancy of sites as the letter | not used |
| named-sign `{+,−}` letter | not used |
| singleton unique lock-vector letter | not used as the object; mixed remains a set |
| `Z^3` sum of the lock set | not used; no aggregation |
| six-neighbor star as the letter | not used |
| leftover of nm2oricyclz equal-sign reverse | not this neighbor-read display |
| leftover of nm2oreadz neighbor-read of `O` | not this display |
| leftover of nm2readz neighbor-read of `M` | not this display |
| leftover of nm2axz axis-cover | not this neighbor-read display |
| leftover of nm2ax12z 1-in 2-out | not this neighbor-read display |
| leftover of nm2orichz leftover-axis | not this display |
| leftover of cyclic lex-smallest | not this display |
| one-axis opposite leftover of the second pair | not this seed |
| y-probe or x-probe neighbor-read on this seed | not this letter |
| global later T | not used |
| neighbor-read as Admissibility content | not adopted |
| formation site / probability / rate | open |
| physical Record readout of the bits | open |

## Value gate (V1–V5)

| # | Answer |
|---|---|
| V1 | It answers the first-display question: can a formed six-neighbor recover the same cyclic lex-largest Orient sign at `t+1` on the four z-probes of the two-axis opposite seed, and reverse/face from that. |
| V2 | Current main has no landed neighbor-read reverse/face of cyclic lex-largest Orient on these four z-probes of this two-axis opposite seed. |
| V3 | Neighbor-read reports at one cut and the two reverse/face bits are independently finite and exact. |
| V4 | The theorem is more than a restatement of Record because it reads whether a formed six-neighbor recovers the same `±1` Orient sign at the same `t+1` cut: the partner seed shares `O` and flips Orient, so neighbor-read of `O` HOLDs at `A` while this fails at every z-probe. |
| V5 | It is not an adopted content rule: the bits remain displayed. |

## No-go discipline gate

The negative content is narrow: the display does not write those bits into
Admissibility, does not reduce them to named signs, does not require a
unique lock, does not replace neighbor-read of Orient by neighbor-read of
`O` or of `M`, does not replace it by nm2oricyclz equal-sign reverse, and
does not identify this display with leftover-axis neighbor-read, cyclic
lex-smallest neighbor-read, axis-cover, or 1-in 2-out split. No global
impossibility is claimed.

### N1 — materially distinct routes

| Route | Attempt | Why it fails here | Marker |
|---|---|---|---|
| nm2oricyclz equal-sign reverse | reuse Orient reverse hold and face hold | Orient reverse HOLDs from `−1,−1` and face HOLDs from `+1,+1`; this reverse fails and this face fails because no formed 6-NN recovers the same sign | ATTEMPTED |
| nm2oreadz neighbor-read of `O` | score reverse/face from equal outgoing sets | neighbor-read of `O` HOLDs at `A` from partner seed `(0,1,1)`; this fails at `A` because that partner has Orient `+1` | ATTEMPTED |
| nm2readz neighbor-read of `M` | score reverse/face from equal incoming sets | neighbor-read of `M` is fail/hold/hold/hold and face hold; this is fail/fail/fail/fail and face fail | ATTEMPTED |
| leftover-axis neighbor-read | score neighbor-read of leftover-axis Orient | leftover-axis neighbor-read is fail/hold/hold/hold and face hold; this face fails | ATTEMPTED |
| cyclic lex-smallest neighbor-read | reuse same cyclic axes with `+e` if both signs | lex-smallest neighbor-read HOLDs at `A` from origin matching `+1`; this fails at `A` | ATTEMPTED |
| nm2axz axis-cover | reuse cover reverse hold and face hold | cover HOLDs at each z-probe; neighbor-read of Orient fails at each z-probe | ATTEMPTED |
| nm2ax12z 1-in 2-out | reuse split reverse hold and face hold | split HOLDs at each z-probe; Cover and split do not score handedness | ATTEMPTED |
| unique signed `|O_i|=1` | replace mixed `O` by unique letters | unique signed Orient fails at each probe, so that neighbor-read fails from Orient fail, not from unmatched `±1` signs | ATTEMPTED |
| unique letter | replace mixed sets by a singleton or `UNDEFINED` | mixed `O(A,τ)` remains a set; Orient is `−1`, not `UNDEFINED`; neighbor-read still fails | ATTEMPTED |
| named-sign lettering | collapse `{±e_i}` to `{+,−}` | named-sign lettering lost the axis and the frame | ATTEMPTED |
| y-probe neighbor-read | score the four y-probes on this seed | y-probe neighbor-read HOLDs at `A`; this letter fails at z-probe `A` | ATTEMPTED |
| x-probe neighbor-read | score the four x-probes on this seed | x-probe neighbor-read fails at `A` from Orient fail; this letter has Orient `−1` at z-probe `A` | ATTEMPTED |
| 1-axis leftover | treat `(0,0,1)` and `(0,1,1)` as formed children of `+e_1/−e_1` | those children lock `+e_3` at tick 1; here they are seeds locking `+e_2/−e_2` at tick 0; 1-axis neighbor-read reverse HOLDs | ATTEMPTED |
| Orient fail as `UNDEFINED` | treat split fail as unformed | Orient fail is neighbor-read fail, not UNDEFINED; at `t`, empty `O` makes Orient fail and neighbor-read fail | ATTEMPTED |
| empty matching as `UNDEFINED` | treat no matching neighbor as unformed | empty matching is fail, not UNDEFINED | ATTEMPTED |
| sum of a set | replace neighbor-read by a `Z^3` sum | the construction does not sum; equality is equality of `±1` signs | ATTEMPTED |
| global later T | wait until `max t(A,B,C,D)` before reading | `τ(q)=t(q)+1` is per-probe; no global T | ATTEMPTED |
| attach a formation member from already-recorded six-neighbor locks | form the probes by a neighbor-lock letter instead of perp-step | refused; not attached | ATTEMPTED |
| adopt bits into Admissibility | rewrite the local rule by neighbor-read of Orient | refused; displayed, not adopted | ATTEMPTED |

### N2 — wall independence

Missing physical adoption, missing identification of neighbor-read of Orient
with neighbor-read of `O`, missing identification with neighbor-read of `M`,
missing identification with nm2oricyclz equal-sign reverse, missing
identification with leftover-axis neighbor-read, missing identification
with cyclic lex-smallest neighbor-read, missing identification with
axis-cover, and missing Record identification of neighbor-read reverse are
distinct open premises. This note claims no complete wall collection.

### N3 — hidden-condition scan

The host `B_3(0)`, two disjoint opposite-pair seed locks `+e_1`, `−e_1`,
`+e_2`, and `−e_2`, perpendicular step rule, incoming-step lock, own
incoming set and own outgoing dual from records with tick `<= τ`, per-probe
`τ=t+1`, cyclic next/prev lex-largest Orient of the 1-in 2-out frame,
neighbor-read as equal `±1` Orient at some formed six-neighbor at the same
cut, Orient fail as neighbor-read fail not `UNDEFINED`, four z-probes with
seed `A`, and mixed remains a set are declared. No uniqueness of outgoing
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
| per element | cyclic lex-largest Orient at a probe and at formed 6-NN, compared as `±1` signs at the probe's `t+1` | no continuum alphabet |
| per site | `A,B,C,D` z-probes on `B_3(0)` only | no other cubic sites |
| per mode | no mode calculation | no spectral exhaustion |
| per block | four neighbor-read reports, reverse/face from those bits | no adopted content law |
| lattice wide | checked and not executed | no lattice-wide lettering rule |

### N6 — live partial-closure paths

Live routes include a later Record content map for neighbor-read reverse/face,
a formation-rate rule, and a physical selector among matching neighbors.
None is taken here.

### N7 — hostile steelman

**Steelman:** Neighbor-read of Orient must HOLD at `A` because the partner
seed shares `O`; neighbor-read of `O` already asked whether a neighbor
recovers a lock set; nm2oricyclz already answered reverse HOLD from equal
signs; leftover-axis neighbor-read already HOLDs at `B`, `C`, and `D`;
cyclic lex-smallest already HOLDs at `A`; y-probe neighbor-read already
HOLDs at `A`; cover and split already HOLD reverse and face; empty `O` at
a neighbor should be `UNDEFINED`; and reverse fail is only leftover of
nm2oreadz reverse fail.

**Answer:** The partner seed `(0,1,1)` matches `O(A,τ)` as a set of three
outgoing steps and reports Orient `+1`, opposite to `Orient(A)=−1`, because
`m` flips from `+e_2` to `−e_2`. Neighbor-read of `O` HOLDs at `A`.
Neighbor-read of Orient fails at every z-probe. nm2oricyclz reverse HOLDs
from equal signs at `A` and at `B` without asking a neighbor. Leftover-axis
neighbor-read HOLDs at `B` from `D` matching `−1`, and leftover-axis face
HOLDs; this face fails. Cyclic lex-smallest neighbor-read HOLDs at `A` from
origin matching `+1`; this fails at `A`. Y-probe neighbor-read HOLDs at `A`;
this z-probe letter fails at `A`. Cover and split HOLD reverse and face
without cyclic signed columns. Empty `O` at a formed neighbor is Orient
fail, not `UNDEFINED`, and does not match a `±1` probe sign. Reverse fail
of neighbor-read of `O` is hold at `A` with fail at `B`. Reverse fail here
is fail at `A` with fail at `B`.

### N8 — cross-cycle echo

nm2oricyclz reported cyclic lex-largest Orient `−1,−1,+1,+1`, reverse hold,
and face hold. nm2oreadz reported neighbor-read of `O` hold only at `A`,
reverse fail, and face fail. nm2readz reported neighbor-read of `M` fail at
`A` and hold at `B`, `C`, and `D`, reverse fail, and face hold. nm2axz
reported axis-cover HOLD at each of four z-probes, reverse hold, and face
hold. nm2ax12z reported 1-in 2-out split HOLD at each of those probes,
reverse hold, and face hold. nm2orichz leftover-axis reported Orient
`−1,−1,+1,−1`, reverse hold, and face fail. Cyclic lex-smallest on the same
seed reports Orient `+1,+1,−1,−1` and neighbor-read hold at `A`. The four
y-probes of this same seed report neighbor-read hold at `A`. This note is
not those displays: it reports neighbor-read of cyclic lex-largest Orient
at `τ=t+1` on the four z-probes of the two-axis opposite seed, fail at each
probe, reverse fail, and face fail.

**Gate disposition:** PASS for the neighbor-read of cyclic lex-largest Orient
`t+1` reverse/face reports above. FAIL / DO NOT SHIP for “the predicate
equals the named sign,” “the predicate equals the unique singleton lock
vector,” “the predicate equals six-neighbor lock union,” “the predicate
equals neighbor-read of `O`,” “the predicate equals neighbor-read of `M`,”
“the predicate equals nm2oricyclz equal-sign reverse,” “the predicate
equals leftover-axis neighbor-read,” “the predicate equals cyclic
lex-smallest neighbor-read,” “the predicate equals nm2axz axis-cover,”
“the predicate equals nm2ax12z 1-in 2-out,” “bits are Admissibility,”
“neighbor-read of Orient HOLDs at `A`,” “reverse neighbor-read HOLDs,” or
“face neighbor-read HOLDs.”

## Primary runner

The paired runner builds Euclidean `B_3(0)`, runs the two-axis opposite
perp-step incoming-lock process, reads each z-probe's own cyclic
lex-largest Orient from the record prefix at that probe's `t+1`, reads
Orient at each eventually-formed six-neighbor at the same cut, reports
neighbor-read as equal `±1` signs at some formed six-neighbor, and checks
Theorems 1--3. It also checks that neighbor-read fails at each of `A,B,C,D`,
that neighbor-read of `O` HOLDs at `A`, that neighbor-read of `M` is a
different pattern, that leftover-axis neighbor-read HOLDs at `B,C,D`, that
cyclic lex-smallest neighbor-read HOLDs at `A`, that Orient fail is
neighbor-read fail not `UNDEFINED`, that mixed sets remain sets, that
unique-letter Orient is not required at mixed `O`, that the construction
does not sum, that a formation member from already-recorded six-neighbor
locks is not attached, that the second pair is a seed and not a formed
child, that the 1-axis opposite two-site seed is a different member with
neighbor-read reverse hold, and that the display is not the y-probe or
x-probe neighbor-read. No runner cache is written.
