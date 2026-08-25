---
claim_id: two_axis_same_lock_zprobe_incoming_outgoing_axis_cover_tplus1_reverse_face_bounded_theorem_note_2026-08-15
claim_type: bounded_theorem
claim_scope: "Axis-cover of M and O at t+1 on the four z-probes of the two-axis same-lock seed, and reverse/face from that, are reported. Displayed, not adopted."
upstream_dependencies:
  - minimal_axioms
runner: scripts/two_axis_same_lock_zprobe_incoming_outgoing_axis_cover_tplus1_reverse_face_2026_08_15.py
---

# Axis-Cover Of Own-Incoming And Own-Outgoing At t+1 Reverse And Face On Four Two-Axis Same-Lock Z-Probes

> **Key terms used in this doc** are indexed A-Z at `docs/KEY_TERMINOLOGY.md`;
> each row points to the canonical source-of-truth doc.

**Date:** 2026-08-15
**Type:** bounded_theorem
**Scope:** axis-cover of simultaneous earliest incoming set `M` and outgoing
dual `O` at each probe's `τ=t+1`, and reverse/face from that cover, on the
four z-probes of the two-axis same-lock seed in `B_3(0)={n:n·n<=9}`. Same
perp-step incoming-lock process as the two-axis same-lock y-probe cover, with
z-probes. Let `t(q)` be the formation tick of probe `q`. Let `τ(q)=t(q)+1`.
`M(q,τ)` is the set of earliest incoming nearest-neighbor steps at `q`
using only records with tick `<= τ`. Seeds are a singleton seed letter.
`O(q,τ)` is the outgoing dual of `M`: the set of `e` in `{±e_1,±e_2,±e_3}`
such that `q+e` is formed and `e` is in `M(q+e,τ)`. Unformed at `τ` is
`UNDEFINED`. Empty `O` is empty, not `UNDEFINED`. Axis of a defined lock
set `S` is `Axis(S)={e_i | some ±e_i in S}`. Cover HOLDs at `q` if and
only if `Axis(M)` intersect `Axis(O)` is empty and `Axis(M)` union
`Axis(O)` equals `{e_1,e_2,e_3}`. `UNDEFINED` if `M` or `O` is
`UNDEFINED`. Else fail. Reverse HOLDs if and only if cover HOLDs at `A`
and at `B`. Face HOLDs if and only if cover HOLDs at `C` and at `D`. This
is HOLD iff cover, not leftover-empty fail. This is not leftover of
exist-opposite of `M`. This is not leftover of leftover-of-`M` alone.
This is not leftover of leftover-of-`O` alone. This is not leftover of
nm2axz HOLDING. This is not leftover of 1-axis same-lock cover-HOLD.
Neither pair is opposite. Uniqueness is not required. Mixed remains a
set. Displayed, not adopted. Do not write into Admissibility. Do not
attach L1.
**Audit-status authority:** independent audit lane only. This note authors no
audit verdict and predicts none.
**Primary runner:**
[`scripts/two_axis_same_lock_zprobe_incoming_outgoing_axis_cover_tplus1_reverse_face_2026_08_15.py`](../scripts/two_axis_same_lock_zprobe_incoming_outgoing_axis_cover_tplus1_reverse_face_2026_08_15.py)

Framework input:

- [`MINIMAL_AXIOMS_2026-06-29.md`](MINIMAL_AXIOMS_2026-06-29.md) supplies
  cubic-lattice sites `Z^3` with nearest-neighbor adjacency, the one-site
  algebra `M_2(C)`, and the Record sentences that records form and that a
  present record locks exactly one admissible local possibility.

Everything after that quoted input is a finite displayed process on `B_3(0)`
and the four named z-probes. Incoming lock letters are unit nearest-neighbor
steps. `O` is the outgoing dual of those incoming sets at the per-probe cut
`τ=t+1`. Axis is the unsigned lattice direction of a signed lock. Cover is
the complementary occupation of `{e_1,e_2,e_3}` by `Axis(M)` and `Axis(O)`.
Reverse and face are scored on cover HOLD at the paired probes. Named signs
`{+,−}` are a coarser readout and are not used. A singleton unique lock
letter is a different readout and is not used as the object. Existential
opposite of signed locks is a different readout and is not used as the
cover reverse. Leftover-empty fail of unsigned leftover axis sets is a
different readout and is not used. A `Z^3` sum of those locks is a
different readout and is not used. Occupancy of sites is not used. A
six-neighbor star is not the letter.

## Machine status and trace

```yaml
actual_current_surface_status: bounded-support
target_claim_type: bounded_theorem
claim_type_reason: "Exact report of axis-cover of M and O at t+1 on the four z-probes of the two-axis same-lock seed, cover fail at A from overlapping e_2, complementary cover at B,C,D, reverse fail and face hold from cover; uniqueness of incoming locks is not claimed and the bits are not adopted."
trace_class: frontier_discovery
target_claim_id: two_axis_same_lock_zprobe_incoming_outgoing_axis_cover_tplus1_reverse_face
target_blocker_text: "display axis-cover of M and O at t+1 on the four z-probes of the two-axis same-lock seed, compare to nm2axz HOLDING, HOLD iff cover, not leftover-empty fail"
source_of_blocker_text: handoff
reachability_to_target: advances
artifact_role: theorem
next_trace_action: "Keep axis-cover of M and O at t+1 displayed; do not write cover into Admissibility, do not reduce to leftover-empty fail, do not reduce to leftover of M alone or leftover of O alone, do not replace cover by nm2axz HOLDING, do not replace cover by 1-axis same-lock cover-HOLD, and do not attach L1."
conditional_surface_status: "exact on B_3(0) for axis-cover of M and O at t+1 on the four z-probes of the two-axis same-lock seed and reverse/face from that cover; displayed, not adopted"
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

No larger host is used. The four z-probes are the only sites whose axis-cover
of `M` and `O` is scored:

```text
A = (0,0,1),  B = (1,1,1),  C = (0,0,2),  D = (1,0,1).
```

These are not the y-probes `A=(0,1,0)`, `B=(1,1,1)`, `C=(0,2,0)`,
`D=(1,1,0)`. These are not the x-probes `A=(1,0,0)`, `B=(1,1,1)`, `C=(2,0,0)`,
`D=(1,1,0)`. `A` is a seed of the second same-lock pair.

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

## Named axis-cover of `M` and `O` at `τ=t+1`

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

If `q` is unformed at `τ`, then cover is `UNDEFINED`. Empty `M` or empty
`O` fails because the union misses an axis. Overlapping axes fail even if
the union is complete. Incomplete union fails. Axis is unsigned: `+e_i`
and `−e_i` occupy the same axis. Leftover of the union is `{e_1,e_2,e_3}`
minus `(Axis(M) union Axis(O))`. Empty leftover is leftover fail of
leftover-empty scoring; this display is HOLD iff cover, not leftover-empty
fail. Leftover of `M` alone is `{e_1,e_2,e_3}` minus `Axis(M)`, a different
object. Leftover of `O` alone is a different object.

Reverse axis-cover holds if and only if cover HOLDs at `A` and at `B`. Face
axis-cover holds if and only if cover HOLDs at `C` and at `D`. Either side
`UNDEFINED` is `UNDEFINED`. Else if both sides HOLD, reverse or face HOLDs.
Else fail.

Identifying a named sign of those locks with reverse or face is refused:
named-sign lettering lost the axis. Identifying leftover-empty fail with
cover reverse is refused: leftover-empty fail scores empty leftover as
fail without checking disjoint axes, while cover fails at `A` from
overlapping `e_2`. Identifying nm2axz HOLDING with this reverse/face is
refused: nm2axz HOLDs at `A` and HOLDs reverse; this member fails at `A`
and fails reverse. Identifying 1-axis same-lock cover-HOLD with this
reverse is refused: 1-axis same-lock HOLDs at `A` with `t(A)=1`; here
`A` is a seed at tick 0.

## Theorem 1 — ticks, `M`, `O`, `Axis`, and cover at `τ=t+1`

On this process the four z-probes form. Compare to nm2axz HOLDING: the
two-axis opposite seed `+e_1/−e_1` and `+e_2/−e_2` reports cover HOLD at
each of the four z-probes, reverse hold, and face hold, with
`O(A,τ)={+e_1, −e_1, +e_3}` missing the partner-axis letter. This two-axis
same-lock member keeps the same z-probes and the same perp-step process,
but neither pair is opposite. Cover fails at `A` and HOLDs at `B`, at `C`,
and at `D`: `Axis(M)(A,τ)={e_2}` and `Axis(O)(A,τ)={e_1, e_2, e_3}`, so
the intersection is `{e_2}` even though the union is `{e_1,e_2,e_3}`.
Reverse fails. Face HOLDs.

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
Axis(M)(A, τ) = {e_2}
Axis(O)(A, τ) = {e_1, e_2, e_3}
Axis(M)(B, τ) = {e_1}
Axis(O)(B, τ) = {e_2, e_3}
Axis(M)(C, τ) = {e_3}
Axis(O)(C, τ) = {e_1, e_2}
Axis(M)(D, τ) = {e_1}
Axis(O)(D, τ) = {e_2, e_3}
cover(A) = fail
cover(B) = hold
cover(C) = hold
cover(D) = hold
```

`A` is a seed at tick 0 with seed letter `+e_2`. The partner of that pair,
`(0,1,1)`, is also a seed at tick 0 with seed letter `+e_2`. Mixed remains
a set: `O(A,τ)` has four outgoing steps. Unique letters would assign
`UNDEFINED` at mixed `O(A)`. Here uniqueness is not required. The same-lock
partner letter `+e_2` is already in `O(A)` at formation tick `t` itself:
`O(A,t)={+e_2}`. Cover therefore already fails at `A` at `t`, and still
fails at `τ=t+1` after `O` also occupies `e_1` and `e_3`. At `B`, `C`, and
`D`, `O` is empty at `t` and cover fails there until the `t+1` cut. At
`B`, `C`, and `D`, `Axis(M)` and `Axis(O)` are complementary: their union
is `{e_1,e_2,e_3}` and their intersection is empty. Leftover of the union
is empty at each of the four z-probes. Leftover-empty fail of that leftover
is not this object. O is not M.

On the 1-axis same-lock two-site seed, `A=(0,0,1)` is a formed child at
tick 1 locking `+e_3`, and cover HOLDs at each of the four z-probes,
reverse hold, and face hold. That is leftover of the first pair. Here `A`
is a seed of a second same-lock pair on a second axis.

New records in `B_3(0)` between `t` and `t+1` that meet a probe's
six-neighbors enter `O` and do not enter earliest `M`. The partner seed of
`A` is already recorded at tick 0, so it is not among those new records:

```text
new 6-NN of A at t(A)+1: (1, 0, 1), (-1, 0, 1), (0, 0, 2)
new 6-NN of B at t(B)+1: (1, 2, 1), (1, 1, 2), (1, 1, 0)
new 6-NN of C at t(C)+1: (1, 0, 2), (-1, 0, 2), (0, -1, 2)
new 6-NN of D at t(D)+1: (1, -1, 1), (1, 0, 2), (1, 0, 0)
```

Leftover of `M` alone at `A` is `{e_1, e_3}` and at `B` is `{e_2, e_3}`,
nonempty and unequal. Leftover of `O` alone at `A` is empty and at `B` is
`{e_1}`. Those one-sided leftovers are not this object. M exist-opposite
reverse fail: `M(A,τ)={+e_2}` and `M(B,τ)={+e_1}`.

## Theorem 2 — reverse from axis-cover at `τ`

Reverse axis-cover holds if and only if cover HOLDs at `A` and at `B`.
Cover fails at `A` and HOLDs at `B`. Reverse fails. This is HOLD iff
cover, not leftover-empty fail.

Reverse axis-cover at τ: fail

Both sides are defined, so this is not `UNDEFINED`. Leftover-empty reverse
fails because leftover of the union is empty at `A` and at `B`. Cover
reverse fails because `Axis(M)` and `Axis(O)` overlap on `e_2` at `A`.
nm2axz reverse HOLDs because the opposite partner letter `−e_2` is not in
`O(A)`. Leftover-of-`M` reverse would fail because leftover of `M` at `A`
is `{e_1, e_3}` and leftover of `M` at `B` is `{e_2, e_3}`: nonempty and
unequal. Leftover-of-`O` reverse would fail because leftover of `O` at `A`
is empty. Exist-opposite reverse of signed `M` fails. Exist-opposite
reverse of signed `O` holds. Those leftovers are not this display.

Reverse fails.

## Theorem 3 — face from axis-cover at `τ`

Face axis-cover holds if and only if cover HOLDs at `C` and at `D`. Both
covers HOLD. Face HOLDs.

Face axis-cover at τ: hold

Displayed, not adopted. The bits are not written into Admissibility.
Do not write into Admissibility. Do not attach L1.

Leftover-empty face fails because leftover of the union is empty at `C`
and at `D`. Cover face HOLDs from complementary occupation of all three
axes at `C` and at `D`. Leftover-of-`M` face would fail because leftover
of `M` at `C` is `{e_1, e_2}` and leftover of `M` at `D` is `{e_2, e_3}`:
nonempty and unequal. Leftover of `O` at `C` is `{e_3}` and leftover of
`O` at `D` is `{e_1}`: nonempty and unequal. Exist-opposite face of signed
`M` fails and exist-opposite face of signed `O` fails. This display scores
cover of `M` and `O`, which HOLDs at `C` and at `D`, so face HOLDs.

Empty leftover does not make reverse `UNDEFINED`. Leftover-empty fail is
not this reverse. Cover reverse fails from overlapping axes at `A`. Cover
face HOLDs.

On the same seed the four y-probes give reverse hold and face fail. The
four x-probes give reverse fail and face fail. Those probe-direction
readouts are not this z-probe display.

Face holds.

## What this note does not claim

- It does not select a unique incoming, outgoing, or leftover lock.
- It does not reduce lock vectors to named signs `{+,−}`.
- It does not require cover sides to be singletons.
- It does not sum either set.
- It does not replace cover by leftover-empty fail.
- It does not replace cover by leftover of `M` alone.
- It does not replace cover by leftover of `O` alone.
- It does not replace cover by existential opposite of signed locks.
- It does not replace `O` by `M`.
- It does not replace cover by locks of six-neighbors.
- It does not use a six-neighbor star as the letter.
- It does not wait for a global later T.
- It does not attach a formation member from already-recorded six-neighbor
  locks.
- It does not reprint nm2axz HOLDING as this member.
- It does not reprint 1-axis same-lock cover-HOLD as this member.
- It does not reprint two-axis same-lock y-probe axis-cover.
- It does not reprint x-axis same-lock z-probe axis-cover.
- It does not reprint nsopp exist-opposite HOLD.
- It does not reprint the two-tick lock-count clock composition.
- It does not reprint mixed #7188 fail/fail as this member.
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
two-axis same-lock four-site process, axis-cover of `M` and `O` at `t+1`, and
the reverse/face bits from cover are displayed theorem-domain data.

## Exact target and obligation graph

| Obligation | Status |
|---|---|
| current Lattice / Admissibility / Record premises | quoted; no edit |
| perp-step incoming-lock process on `B_3(0)` | displayed; two disjoint same-lock pairs `+e_1/+e_1` and `+e_2/+e_2` |
| ticks `t(A)`, `t(B)`, `t(C)`, `t(D)` | Theorem 1; `0`, `1`, `1`, `1` |
| `M` at `τ=t+1` | Theorem 1; frozen equal to `M` at `t` |
| `O` at `τ=t+1` | Theorem 1; outgoing dual includes partner `+e_2` at `A` |
| `Axis(M)` and `Axis(O)` at `τ` | Theorem 1; overlapping at `A`; complementary at `B`,`C`,`D` |
| cover at `τ` | Theorem 1; fail at `A`; HOLD at `B`,`C`,`D` |
| reverse from axis-cover at `τ` | Theorem 2; `fail` |
| face from axis-cover at `τ` | Theorem 3; `hold` |
| compare to nm2axz HOLDING | Theorem 1; nm2axz HOLDs at `A` and HOLDs reverse; this member fails `A` and fails reverse |
| compare to 1-axis same-lock cover-HOLD | Theorem 1; 1-axis HOLDs at `A` with `t(A)=1`; this member has seed `A` at tick 0 |
| unique incoming lock | not required |
| occupancy of sites as the letter | not used |
| named-sign `{+,−}` letter | not used; lost the axis |
| singleton unique lock-vector letter | not used as the object; mixed remains a set |
| `Z^3` sum of the lock set | not used; no aggregation |
| six-neighbor star as the letter | not used |
| leftover-empty fail | not this cover display |
| leftover of exist-opposite of `M` | not this cover display |
| leftover of leftover-of-`M` alone | not this display |
| leftover of leftover-of-`O` alone | not this display |
| leftover of nm2axz HOLDING | not this display |
| leftover of 1-axis same-lock cover-HOLD | not this display |
| leftover of two-axis opposite | not this display |
| leftover of x-axis same-lock z-probe axis-cover | not this display |
| leftover of nsopp exist-opposite HOLD | not this display |
| two-tick lock-count clock composition | not this display |
| leftover of mixed #7188 fail/fail | not this display |
| global later T | not used |
| axis-cover as Admissibility content | not adopted |
| formation site / probability / rate | open |
| physical Record readout of the bits | open |

## Value gate (V1–V5)

| # | Answer |
|---|---|
| V1 | It answers the first-display question: axis-cover of `M` and `O` at `t+1` on the four z-probes of the two-axis same-lock seed, compared to nm2axz HOLDING, and reverse/face from that cover. |
| V2 | Current main has no landed axis-cover reverse/face of timed `M` and `O` on these four two-axis same-lock z-probes. |
| V3 | Cover reports at one cut and the two reverse/face bits are independently finite and exact. |
| V4 | The theorem is more than a restatement of Record because it reads unsigned axis-cover of own incoming and own outgoing at the same `t+1` cut and scores HOLD iff cover. |
| V5 | It is not an adopted content rule: the bits remain displayed. |

## No-go discipline gate

The negative content is narrow: the display does not write those bits into
Admissibility, does not reduce them to named signs, does not require a
unique lock, does not replace cover by leftover-empty fail, does not
replace cover by leftover of `M` alone or leftover of `O` alone, does not
replace cover by existential opposite of signed locks, and does not
identify this display with nm2axz HOLDING or with 1-axis same-lock
cover-HOLD. No global impossibility is claimed.

### N1 — materially distinct routes

| Route | Attempt | Why it fails here | Marker |
|---|---|---|---|
| leftover-empty fail | score reverse/face as leftover nonempty-equal | leftover of the union is empty at each probe, leftover reverse and face fail, while cover reverse fails from overlapping `e_2` at `A` and cover face HOLDs | ATTEMPTED |
| leftover of `M` alone | score `{e_1,e_2,e_3}` minus `Axis(M)` | leftover of `M` at `A` is `{e_1,e_3}` and at `B` is `{e_2,e_3}`, nonempty unequal; face would fail while cover face HOLDs | ATTEMPTED |
| leftover of `O` alone | score `{e_1,e_2,e_3}` minus `Axis(O)` | leftover of `O` at `A` is empty, leftover reverse fails for a one-sided empty leftover, not overlapping cover | ATTEMPTED |
| exist-opposite of `M` | reuse signed reverse and face of `M` | M exist-opposite reverse fail and face fail; cover face HOLDs from unsigned complementary axes at `C` and `D` | ATTEMPTED |
| exist-opposite of `O` | reuse signed reverse and face of `O` | O exist-opposite reverse hold and face fail; cover reverse fails | ATTEMPTED |
| nm2axz HOLDING | reuse opposite seed `+e_1/−e_1` and `+e_2/−e_2` | nm2axz `O(A)` misses `+e_2` and HOLDs cover at `A`; here `O(A)` includes `+e_2` and cover fails at `A` | ATTEMPTED |
| 1-axis same-lock cover-HOLD | reuse seed `{0,(0,1,0)}` with `+e_1/+e_1` | 1-axis HOLDs at `A` with `t(A)=1` locking `+e_3`; here `t(A)=0`, `M(A)={+e_2}`, cover fails at `A` | ATTEMPTED |
| two-axis opposite | reuse seed `+e_1/−e_1` and `+e_2/−e_2` | that leftover HOLDs reverse; this member fails reverse | ATTEMPTED |
| x-axis same-lock z-probe | reuse seed `{0,(1,0,0)}` with `+e_2/+e_2` | different seed; this letter is two-axis same-lock on `+e_1/+e_1` and `+e_2/+e_2` | ATTEMPTED |
| nsopp exist-opposite HOLD | reuse opposite `+e_1/−e_1` z-probes | that leftover is a two-site opposite seed; this member has four same-lock seeds | ATTEMPTED |
| unique letter | replace mixed sets by a singleton or `UNDEFINED` | mixed `O(A,τ)` remains a set; unique-letter cover at `A` is `UNDEFINED` while cover fails | ATTEMPTED |
| letter intersection as cover | score reverse/face inside `M ∩ O` | letter intersection empty is not axis-cover; opposite signs can share an axis | ATTEMPTED |
| same-tick-inclusive six-neighbor lock union | score locks of six-neighbors formed by `t(q)` | that leftover is a signed exist-opposite readout; cover is unsigned complementary axes | ATTEMPTED |
| two-tick lock-count clock | score a lock-count clock across two ticks | different member; this display scores axis-cover of own incoming and outgoing at `t+1` | ATTEMPTED |
| mixed #7188 fail/fail | reuse z-symmetric mixed `M` reverse-fail face-fail | different process; this member reports reverse fail and face hold from cover | ATTEMPTED |
| y-probe cover | score the four y-probes on this seed | y-probe reverse HOLDs and face fails; this letter is the four z-probes | ATTEMPTED |
| x-probe cover | score the four x-probes on this seed | x-probe reverse fails and face fails; this letter is the four z-probes | ATTEMPTED |
| sum of a set | replace cover by a `Z^3` sum | the construction does not sum; cover is a complementary pair of unsigned axis sets | ATTEMPTED |
| named-sign lettering | collapse `{±e_i}` to `{+,−}` | named-sign lettering lost the axis | ATTEMPTED |
| global later T | wait until `max t(A,B,C,D)` before reading | `τ(q)=t(q)+1` is per-probe; no global T | ATTEMPTED |
| attach a formation member from already-recorded six-neighbor locks | form the probes by a neighbor-lock letter instead of perp-step | refused; not attached | ATTEMPTED |
| adopt bits into Admissibility | rewrite the local rule by axis-cover | refused; displayed, not adopted | ATTEMPTED |

### N2 — wall independence

Missing physical adoption, missing identification of cover with leftover of
`M` alone, missing identification of cover with leftover-empty fail, missing
identification of cover with existential opposite of signed locks, missing
identification of this member with nm2axz HOLDING, and missing Record
identification of cover reverse are distinct open premises. This note
claims no complete wall collection.

### N3 — hidden-condition scan

The host `B_3(0)`, four-site two-axis same-lock seed, perpendicular step
rule, incoming-step lock, own incoming set and own outgoing dual from
records with tick `<= τ`, per-probe `τ=t+1`, unsigned axis, cover as
complementary occupation of `{e_1,e_2,e_3}` by `Axis(M)` and `Axis(O)`, HOLD
iff cover not leftover-empty fail, four z-probes with seed `A`, and mixed
remains a set are declared. No uniqueness of incoming locks, no six-neighbor
lock union as the scored object, no lock-count clock, no global later T, no
formation attachment from already-recorded six-neighbor locks, and no
Admissibility rewrite are silently assumed.

### N4 — source residual matching

The current axiom memo supplies cubic sites, `M_2(C)`,
content-conditional-on-formation, and unreadable absence. The residual that
formation site, probability, and rate remain unsupplied is unchanged. The
cover reverse fail and face hold reports do not close that residual.

### N5 — resolution and rhetoric audit

| Resolution | Executed | Not claimed |
|---|---|---|
| per element | each unsigned lattice axis among `{e_1,e_2,e_3}` | no continuum alphabet |
| per site | `A,B,C,D` z-probes on `B_3(0)` only | no other cubic sites |
| per mode | no mode calculation | no spectral exhaustion |
| per block | four cover reports, reverse/face from cover HOLD | no adopted content law |
| lattice wide | checked and not executed | no lattice-wide lettering rule |

### N6 — live partial-closure paths

Live routes include a later Record content map for cover reverse/face, a
formation-rate rule, and a physical selector among complementary axes. None
is taken here.

### N7 — hostile steelman

**Steelman:** Two-axis same-lock is still cover HOLD on z-probes because
nm2axz HOLDs and same-lock is only a sign flip of opposite; leftover empty
already answered three-axis occupation at `A`; leftover of `M` alone
already gives `{e_1,e_3}` at `A`; and signed exist-opposite of `O` already
answered reverse.

**Answer:** Cover fails at `A` because `Axis(M)={e_2}` intersects
`Axis(O)={e_1,e_2,e_3}`. nm2axz HOLDs at `A` because the opposite partner
letter is `−e_2`, which is not in `O(A)`. This member has same-lock partner
letter `+e_2` already in `O(A)` at tick 0. Leftover empty at each probe is
leftover reverse fail and leftover face fail, while cover face HOLDs.
Leftover of `M` alone reverse would fail from unequal leftovers and is not
complementary cover of the pair. Signed exist-opposite of `O` reverse-holds
while cover reverse fails. Reverse axis-cover is HOLD iff cover at `A` and
at `B`, not leftover-empty fail and not leftover of nm2axz HOLDING.

### N8 — cross-cycle echo

nm2axz HOLDING on two-axis opposite z-probes reports cover HOLD at each of
the four z-probes, reverse hold, and face hold. 1-axis same-lock cover-HOLD
on `{0,(0,1,0)}` with `+e_1/+e_1` reports cover HOLD at each of the four
z-probes, reverse hold, and face hold, with `t(A)=1`. Two-axis same-lock
y-probes report reverse hold and face fail. This note is not those
displays: it reports axis-cover of `M` and `O` at `τ=t+1` on two disjoint
same-lock pairs with z-probes, cover fail at `A`, cover HOLD at `B`,`C`,`D`,
reverse fail, and face hold. HOLD iff cover, not leftover-empty fail, and
not leftover of nm2axz HOLDING.

**Gate disposition:** PASS for the axis-cover `t+1` reverse/face reports
above. FAIL / DO NOT SHIP for “the predicate equals the named sign,” “the
predicate equals the unique singleton lock vector,” “the predicate equals
six-neighbor lock union,” “the predicate equals leftover-empty fail,” “the
predicate equals leftover of `M` alone,” “the predicate equals leftover of
`O` alone,” “the predicate equals exist-opposite of `M`,” “the predicate
equals nm2axz HOLDING,” “the predicate equals 1-axis same-lock cover-HOLD,”
“bits are Admissibility,” “cover HOLDs at `A`,” “cover fails at `D`,”
“reverse axis-cover HOLDs,” or “face axis-cover fails.”

## Primary runner

The paired runner builds Euclidean `B_3(0)`, runs the two-axis same-lock
perp-step incoming-lock process, reads each z-probe's own earliest incoming
set and own outgoing dual from the record prefix at that probe's `t+1`,
reports unsigned axis of each, reports cover of the pair, lists new records
in `B_3(0)` between `t` and `t+1` that meet a probe's six-neighbors, compares
to nm2axz HOLDING, and checks Theorems 1--3. It also checks that cover
fails at `A` and HOLDs at `B`,`C`,`D`, that leftover-empty fail is a
different face, that leftover of `M` alone and leftover of `O` alone are
different objects, that signed exist-opposite of `O` holds reverse while
cover reverse fails, that mixed sets remain sets, that unique-letter cover
is `UNDEFINED` at mixed `O(A)`, that the construction does not sum, that a
formation member from already-recorded six-neighbor locks is not attached,
and that the display is not the two-tick lock-count clock composition. No
runner cache is written.
