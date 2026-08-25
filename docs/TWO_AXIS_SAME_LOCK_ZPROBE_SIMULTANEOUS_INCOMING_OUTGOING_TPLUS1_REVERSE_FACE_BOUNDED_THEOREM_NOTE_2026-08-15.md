---
claim_id: two_axis_same_lock_zprobe_simultaneous_incoming_outgoing_tplus1_reverse_face_bounded_theorem_note_2026-08-15
claim_type: bounded_theorem
claim_scope: "Simultaneous M and O at t+1 on the four z-probes of the two-axis same-lock seed, and reverse/face from that, are reported. Displayed, not adopted."
upstream_dependencies:
  - minimal_axioms
runner: scripts/two_axis_same_lock_zprobe_simultaneous_incoming_outgoing_tplus1_reverse_face_2026_08_15.py
---

# Simultaneous Own-Incoming And Own-Outgoing At t+1 Reverse And Face On Four Two-Axis Same-Lock Z-Probes

> **Key terms used in this doc** are indexed A-Z at `docs/KEY_TERMINOLOGY.md`;
> each row points to the canonical source-of-truth doc.

**Date:** 2026-08-15
**Type:** bounded_theorem
**Scope:** simultaneous earliest incoming set `M` and outgoing dual `O` at
each probe's `τ=t+1`, their intersection, and reverse/face from simultaneous
HOLD, on the four z-probes of the two-axis same-lock seed in
`B_3(0)={n:n·n<=9}`. Same perp-step incoming-lock process and z-probes as
the two-axis same-lock z-probe axis-cover display. Let `t(q)` be the
formation tick of probe `q`. Let `τ(q)=t(q)+1`. `M(q,τ)` is the set of
earliest incoming nearest-neighbor steps at `q` using only records with
tick `<= τ`. Seeds are a singleton seed letter. `O(q,τ)` is the outgoing
dual of `M`: the set of `e` in `{±e_1,±e_2,±e_3}` such that `q+e` is formed
and `e` is in `M(q+e,τ)`. Unformed at `τ` is `UNDEFINED`. Empty `O` is
empty, not `UNDEFINED`. Intersection is `M(q,τ) ∩ O(q,τ)`; unformed is
`UNDEFINED`. Empty intersection is empty, not `UNDEFINED`. Simultaneous
HOLDs at `q` if and only if both `M` and `O` are defined nonempty and
`M ∩ O` is empty. `UNDEFINED` if `M` or `O` is `UNDEFINED`. Else fail.
Reverse HOLDs if and only if simultaneous HOLDs at `A` and at `B`. Face
HOLDs if and only if simultaneous HOLDs at `C` and at `D`. This is HOLD
iff simultaneous, not leftover-empty fail of leftover axis. This is not
leftover of nm2simz HOLDING. This is not leftover of nm2slz axis-cover.
This is not leftover of nm2sl12z 1-in 2-out split. This is not leftover of
nmsimopp exist-opposite of `M` and of `O` at `t+1`. This is not leftover of
leftover-of-`M` alone. This is not leftover of leftover-of-`O` alone. This
is not leftover of nmunopp union. This is not leftover of nmt2opp `M`
frozen at `t`. This is not leftover of nmot2opp two-tick composition. This
is not leftover of nmoutopp untimed eventual-`O`. This is not leftover of
mixed #7188 fail/fail. Neither pair is opposite. Uniqueness is not
required. Mixed remains a set. Occupancy of sites is not used. Occupancy
`n` is not used. Displayed, not adopted. Do not write into Admissibility.
Do not attach L1.
**Audit-status authority:** independent audit lane only. This note authors no
audit verdict and predicts none.
**Primary runner:**
[`scripts/two_axis_same_lock_zprobe_simultaneous_incoming_outgoing_tplus1_reverse_face_2026_08_15.py`](../scripts/two_axis_same_lock_zprobe_simultaneous_incoming_outgoing_tplus1_reverse_face_2026_08_15.py)

Framework input:

- [`MINIMAL_AXIOMS_2026-06-29.md`](MINIMAL_AXIOMS_2026-06-29.md) supplies
  cubic-lattice sites `Z^3` with nearest-neighbor adjacency, the one-site
  algebra `M_2(C)`, and the Record sentences that records form and that a
  present record locks exactly one admissible local possibility.

Everything after that quoted input is a finite displayed process on `B_3(0)`
and the four named z-probes. Incoming lock letters are unit nearest-neighbor
steps. `O` is the outgoing dual of those incoming sets at the per-probe cut
`τ=t+1`. Simultaneous is signed-letter disjointness of nonempty `M` and
nonempty `O` at that same cut. Reverse and face are scored on simultaneous
HOLD at the paired probes. Named signs `{+,−}` are a coarser readout and
are not used. A singleton unique lock letter is a different readout and is
not used as the object. Existential opposite of signed locks is a different
readout and is not used as the simultaneous reverse. Unsigned axis-cover of
`M` and `O` is a different readout and is not used. 1-in 2-out axis split
is a different readout and is not used. Leftover-empty fail of unsigned
leftover axis sets is a different readout and is not used. A `Z^3` sum of
those locks is a different readout and is not used. Occupancy of sites is
not used. The construction does not use occupancy. A six-neighbor star is
not the letter.

## Machine status and trace

```yaml
actual_current_surface_status: bounded-support
target_claim_type: bounded_theorem
claim_type_reason: "Exact report of simultaneous M and O at t+1 on the four z-probes of the two-axis same-lock seed, nonempty intersection at A, empty intersection at B,C,D, reverse fail and face hold from simultaneous; uniqueness of incoming locks is not claimed and the bits are not adopted."
trace_class: frontier_discovery
target_claim_id: two_axis_same_lock_zprobe_simultaneous_incoming_outgoing_tplus1_reverse_face
target_blocker_text: "display simultaneous M and O at t+1 on the four z-probes of the two-axis same-lock seed, compare to nm2simz HOLDING, HOLD iff simultaneous, not leftover-empty fail"
source_of_blocker_text: handoff
reachability_to_target: advances
artifact_role: theorem
next_trace_action: "Keep simultaneous M and O at t+1 displayed; do not write simultaneous into Admissibility, do not reduce to leftover-empty fail, do not reduce to leftover of M alone or leftover of O alone, do not replace simultaneous by existential opposite of signed locks, do not replace simultaneous by unsigned axis-cover, do not replace simultaneous by 1-in 2-out split, do not replace either set by six-neighbor lock union, and do not attach L1."
conditional_surface_status: "exact on B_3(0) for simultaneous M and O at t+1 on the four z-probes of the two-axis same-lock seed and reverse/face from that; displayed, not adopted"
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
simultaneous `M` and `O` is scored:

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

## Named simultaneous `M` and `O` at `τ=t+1`

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
Occupancy of sites is not used. Occupancy `n` is not used. O is not M.

Intersection at the same cut:

```text
(M ∩ O)(q,τ) = M(q,τ) ∩ O(q,τ).
```

If `q` is unformed at `τ`, then the intersection is `UNDEFINED`. Empty
intersection is empty, not `UNDEFINED`. Nonempty intersection is a set of
shared signed letters, not `UNDEFINED`.

Simultaneous at a probe at the same cut:

```text
sim(q) HOLDs iff M and O are defined nonempty and M ∩ O is empty.
```

If `q` is unformed at `τ`, then simultaneous is `UNDEFINED`. Empty `M` or
empty `O` fails. Nonempty overlapping letters fail. Simultaneous is signed
letter disjointness: `+e_i` and `−e_i` are distinct letters. Unsigned
axis-cover is a different object: opposite signs occupy the same axis, so
letter-disjoint sets can fail cover. 1-in 2-out is a different object:
cover HOLD with `|Axis(M)|=1`. Leftover of the union of unsigned axes is
`{e_1,e_2,e_3}` minus `(Axis(M) union Axis(O))`. Empty leftover is leftover
fail of leftover axis; this display is HOLD iff simultaneous, not
leftover-empty fail.

Reverse simultaneous holds if and only if simultaneous HOLDs at `A` and at
`B`. Face simultaneous holds if and only if simultaneous HOLDs at `C` and
at `D`. Either side `UNDEFINED` is `UNDEFINED`. Else if both sides HOLD,
reverse or face HOLDs. Else fail.

Identifying a named sign of those locks with reverse or face is refused:
named-sign lettering lost the axis. Identifying leftover-empty fail with
simultaneous reverse is refused: leftover-empty fail scores empty leftover
axis as fail. Identifying unsigned axis-cover with simultaneous is refused:
on this same seed the y-probe `D` has letter-disjoint nonempty `M` and `O`
and fails complementary occupation of `{e_1,e_2,e_3}`. Identifying 1-in
2-out with simultaneous is refused: on this same seed the y-probe `D` HOLDs
simultaneous and fails 1-in 2-out. Identifying nm2simz HOLDING with this
reverse is refused: nm2simz HOLDs at `A` and HOLDs reverse; this member
fails at `A` and fails reverse.

## Theorem 1 — ticks, `M`, `O`, intersection, and sim at `τ=t+1`

On this process the four z-probes form. Compare to leftover axis: that
leftover reports empty leftover at each probe and leftover reverse fail and
leftover face fail. Compare to nm2simz HOLDING: the two-axis opposite seed
`+e_1/−e_1` and `+e_2/−e_2` reports simultaneous HOLD at each of the four
z-probes, reverse hold, and face hold, with `O(A,τ)={+e_1, −e_1, +e_3}`
missing the partner-axis letter. Compare to nm2sl12z 1-in 2-out: that
leftover reports split fail at `A` from overlapping unsigned `e_2`, reverse
fail, and face hold. This two-axis same-lock member keeps the same z-probes
and the same perp-step process, but neither pair is opposite. Simultaneous
fails at `A` and HOLDs at `B`, at `C`, and at `D`: `M(A,τ)={+e_2}` and
`O(A,τ)={+e_1, −e_1, +e_2, +e_3}` share the signed letter `+e_2`. Reverse
fails. Face HOLDs.

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
M(A, τ) ∩ O(A, τ) = {+e_2}
M(B, τ) ∩ O(B, τ) = {}
M(C, τ) ∩ O(C, τ) = {}
M(D, τ) ∩ O(D, τ) = {}
sim(A) = fail
sim(B) = hold
sim(C) = hold
sim(D) = hold
```

`A` is a seed at tick 0 with seed letter `+e_2`. The partner of that pair,
`(0,1,1)`, is also a seed at tick 0 with seed letter `+e_2`. Mixed remains
a set: `O(A,τ)` has four outgoing steps. Unique letters would assign
`UNDEFINED` at mixed `O(A)`. Here uniqueness is not required. The same-lock
partner letter `+e_2` is already in `O(A)` at formation tick `t` itself:
`O(A,t)={+e_2}`. Simultaneous therefore already fails at `A` at `t`, and
still fails at `τ=t+1` after `O` also occupies `+e_1`, `−e_1`, and `+e_3`.
At `B`, `C`, and `D`, `O` is empty at `t` and simultaneous fails there until
the `t+1` cut. At `B`, `C`, and `D`, `M` and `O` are defined nonempty and
disjoint as signed letters. Simultaneous therefore HOLDs at `B`, `C`, and
`D`. Leftover of the unsigned-axis union is empty at each probe;
leftover-empty fail of that leftover is not this object. Axis-cover also
fails at `A` and HOLDs at `B`, `C`, and `D`; that unsigned complementary
occupation is not this letter. 1-in 2-out also fails at `A` and HOLDs at
`B`, `C`, and `D`; that axis-cardinality split is not this letter. O is
not M.

On the 1-axis same-lock two-site seed, `A=(0,0,1)` is a formed child at
tick 1 locking `+e_3`, and simultaneous HOLDs at each of the four z-probes,
reverse hold, and face hold. That is leftover of the first pair. Here `A`
is a seed of a second same-lock pair on a second axis. On that 1-axis seed,
z-probe `C` is 2-in 1-out, so 1-in 2-out face fails while simultaneous face
HOLDs.

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

## Theorem 2 — reverse from simultaneous at `τ`

Reverse simultaneous holds if and only if simultaneous HOLDs at `A` and at
`B`. Simultaneous fails at `A` and HOLDs at `B`. Reverse fails. This is
HOLD iff simultaneous, not leftover-empty fail.

Reverse simultaneous at τ: fail

Both sides are defined, so this is not `UNDEFINED`. Leftover-empty reverse
fails because leftover of the unsigned-axis union is empty at `A` and at
`B`. Simultaneous reverse fails because `M` and `O` share `+e_2` at `A`.
nm2simz reverse HOLDs because the opposite partner letter `−e_2` is not in
`O(A)`. Leftover-of-`M` reverse would fail because leftover of `M` at `A`
is `{e_1, e_3}` and leftover of `M` at `B` is `{e_2, e_3}`: nonempty and
unequal. Leftover-of-`O` reverse would fail because leftover of `O` at `A`
is empty. Exist-opposite reverse of signed `M` fails. Exist-opposite
reverse of signed `O` holds. Those leftovers are not this display. Unsigned
axis-cover reverse also fails on these z-probes; that is not this letter.
1-in 2-out reverse also fails on these z-probes; that is not this letter.

Reverse fails.

## Theorem 3 — face from simultaneous at `τ`

Face simultaneous holds if and only if simultaneous HOLDs at `C` and at
`D`. Both simultaneous reports HOLD. Face HOLDs.

Face simultaneous at τ: hold

Displayed, not adopted. The bits are not written into Admissibility.
Do not write into Admissibility. Do not attach L1.

Leftover-empty face fails because leftover of the unsigned-axis union is
empty at `C` and at `D`. Simultaneous face HOLDs from signed-letter
disjoint nonempty `M` and `O` at both face probes. Leftover-of-`M` face
would fail because leftover of `M` at `C` is `{e_1, e_2}` and leftover of
`M` at `D` is `{e_2, e_3}`: nonempty and unequal. Leftover of `O` at `C` is
`{e_3}` and leftover of `O` at `D` is `{e_1}`: nonempty and unequal.
Exist-opposite face of signed `M` fails and exist-opposite face of signed
`O` fails. This display scores simultaneous of `M` and `O`, which HOLDs at
`C` and at `D`, so face HOLDs.

Empty leftover does not make reverse `UNDEFINED`. Leftover-empty fail is
not this reverse. Simultaneous reverse fails from overlapping signed
letters at `A`. Simultaneous face HOLDs.

On the same seed the four y-probes give simultaneous reverse hold and
simultaneous face hold, but y-probe axis-cover face fails at `D`:
`M(D)={−e_3}` and `O(D)={+e_1}` are letter-disjoint and nonempty, yet
`Axis(M) ∪ Axis(O) = {e_1, e_3}` misses `e_2`. Y-probe 1-in 2-out face
likewise fails at `D`. The four x-probes give simultaneous reverse hold and
simultaneous face hold, but x-probe axis-cover reverse fails at `A`. Those
probe-direction readouts are not this z-probe display. Letter-disjoint
nonempty is not complementary axis-cover and is not 1-in 2-out.

Face holds.

## What this note does not claim

- It does not select a unique incoming, outgoing, or leftover lock.
- It does not reduce lock vectors to named signs `{+,−}`.
- It does not require simultaneous sides to be singletons.
- It does not sum either set.
- It does not replace simultaneous by leftover-empty fail.
- It does not replace simultaneous by leftover of `M` alone.
- It does not replace simultaneous by leftover of `O` alone.
- It does not replace simultaneous by existential opposite of signed locks.
- It does not replace simultaneous by unsigned axis-cover of `M` and `O`.
- It does not replace simultaneous by 1-in 2-out axis split.
- It does not replace `O` by `M`.
- It does not replace simultaneous by locks of six-neighbors.
- It does not use a six-neighbor star as the letter.
- It does not wait for a global later T.
- It does not attach a formation member from already-recorded six-neighbor
  locks.
- It does not reprint nm2simz HOLDING as this member.
- It does not reprint nm2slz axis-cover as this member.
- It does not reprint nm2sl12z 1-in 2-out reverse fail as this member.
- It does not reprint 1-axis same-lock simultaneous HOLD as this member.
- It does not reprint nmsimopp exist-opposite of `M` and of `O` at `t+1`.
- It does not reprint nmunopp untimed union.
- It does not reprint nmt2opp `M` frozen at `t` as this simultaneous display.
- It does not reprint nmot2opp two-tick composition of empty-then-HOLD `O`.
- It does not reprint nmoutopp untimed eventual-`O`.
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
two-axis same-lock process, simultaneous `M` and `O` at `t+1`, and the
reverse/face bits from simultaneous HOLD are displayed theorem-domain data.

## Exact target and obligation graph

| Obligation | Status |
|---|---|
| current Lattice / Admissibility / Record premises | quoted; no edit |
| perp-step incoming-lock process on `B_3(0)` | displayed; two disjoint same-lock pairs `+e_1/+e_1` and `+e_2/+e_2` |
| ticks `t(A)`, `t(B)`, `t(C)`, `t(D)` | Theorem 1; `0`, `1`, `1`, `1` |
| `M` at `τ=t+1` | Theorem 1; frozen equal to `M` at `t` |
| `O` at `τ=t+1` | Theorem 1; outgoing dual includes partner `+e_2` at `A` |
| `M ∩ O` at `τ` | Theorem 1; `{+e_2}` at `A`; empty at `B`,`C`,`D` |
| sim at `τ` | Theorem 1; fail at `A`; HOLD at `B`,`C`,`D` |
| reverse from simultaneous at `τ` | Theorem 2; `fail` |
| face from simultaneous at `τ` | Theorem 3; `hold` |
| compare to nm2simz HOLDING | Theorem 1; nm2simz HOLDs at `A` and HOLDs reverse; this member fails `A` and fails reverse |
| compare to nm2sl12z 1-in 2-out reverse fail | Theorem 1; split reverse also fails here; y-probe 1-in 2-out face fails while y-probe sim face HOLDs |
| unique incoming lock | not required |
| occupancy of sites as the letter | not used |
| named-sign `{+,−}` letter | not used; lost the axis |
| singleton unique lock-vector letter | not used as the object; mixed remains a set |
| `Z^3` sum of the lock set | not used; no aggregation |
| six-neighbor star as the letter | not used |
| leftover-empty fail of leftover axis | not this simultaneous display |
| leftover of nm2simz HOLDING | not this simultaneous display |
| leftover of nm2slz axis-cover | not this simultaneous display |
| leftover of nm2sl12z 1-in 2-out | not this simultaneous display |
| leftover of nmsimopp exist-opposite HOLD | not this simultaneous display |
| leftover of leftover-of-`M` alone | not this display |
| leftover of leftover-of-`O` alone | not this display |
| leftover of nmunopp untimed union | not this display |
| leftover of nmt2opp `M` frozen at `t` | not this display |
| leftover of nmot2opp two-tick composition | not this display |
| leftover of nmoutopp untimed eventual-`O` | not this display |
| two-tick lock-count clock composition | not this display |
| leftover of mixed #7188 fail/fail | not this display |
| 1-axis same-lock leftover of the second pair | not this seed |
| y-probe or x-probe simultaneous on this seed | not this letter |
| global later T | not used |
| simultaneous as Admissibility content | not adopted |
| formation site / probability / rate | open |
| physical Record readout of the bits | open |

## Value gate (V1–V5)

| # | Answer |
|---|---|
| V1 | It answers the first-display question: simultaneous `M` and `O` at `t+1` on the four z-probes of the two-axis same-lock seed, compared to nm2simz HOLDING, and reverse/face from that. |
| V2 | Current main has no landed simultaneous reverse/face of timed `M` and `O` on these four z-probes of this two-axis same-lock seed. |
| V3 | Simultaneous reports at one cut and the two reverse/face bits are independently finite and exact. |
| V4 | The theorem is more than a restatement of Record because it reads signed-letter disjointness of own incoming and own outgoing at the same `t+1` cut and scores HOLD iff simultaneous. |
| V5 | It is not an adopted content rule: the bits remain displayed. |

## No-go discipline gate

The negative content is narrow: the display does not write those bits into
Admissibility, does not reduce them to named signs, does not require a
unique lock, does not replace simultaneous by leftover-empty fail, does not
replace simultaneous by leftover of `M` alone or leftover of `O` alone,
does not replace simultaneous by existential opposite of signed locks, does
not replace simultaneous by unsigned axis-cover, does not replace
simultaneous by 1-in 2-out split, does not identify this display with
nm2simz HOLDING, and does not identify it with nmunopp union. No global
impossibility is claimed.

### N1 — materially distinct routes

| Route | Attempt | Why it fails here | Marker |
|---|---|---|---|
| leftover-empty fail | score reverse/face as leftover nonempty-equal | leftover of the unsigned-axis union is empty at each probe, leftover reverse and face fail, while simultaneous reverse fails from overlapping `+e_2` at `A` and simultaneous face HOLDs | ATTEMPTED |
| leftover of `M` alone | score `{e_1,e_2,e_3}` minus `Axis(M)` | leftover of `M` at `A` is `{e_1,e_3}` and at `B` is `{e_2,e_3}`, nonempty unequal; face would fail while simultaneous face HOLDs | ATTEMPTED |
| leftover of `O` alone | score `{e_1,e_2,e_3}` minus `Axis(O)` | leftover of `O` at `A` is empty, leftover reverse fails for a one-sided empty leftover, not signed-letter overlap | ATTEMPTED |
| nmsimopp exist-opposite | reuse signed reverse hold and face hold of `M` and of `O` | signed `M` reverse fails and signed `O` reverse holds; simultaneous reverse fails from per-probe overlapping `+e_2` at `A` | ATTEMPTED |
| nm2slz axis-cover | reuse complementary unsigned axes of `M` and `O` | on this seed y-probe `D` is letter-disjoint nonempty and fails cover; simultaneous is signed letters, not unsigned axes | ATTEMPTED |
| nm2sl12z 1-in 2-out | require `|Axis(M)|=1` and cover | on this seed y-probe `D` HOLDs simultaneous and fails 1-in 2-out; 1-axis `C` is 2-in 1-out with simultaneous HOLD | ATTEMPTED |
| nm2simz HOLDING | reuse opposite seed `+e_1/−e_1` and `+e_2/−e_2` | nm2simz `O(A)` misses `+e_2` and HOLDs simultaneous at `A`; here `O(A)` includes `+e_2` and simultaneous fails at `A` | ATTEMPTED |
| 1-axis same-lock sim-HOLD | reuse seed `{0,(0,1,0)}` with `+e_1/+e_1` | 1-axis HOLDs at `A` with `t(A)=1` locking `+e_3`; here `t(A)=0`, `M(A)={+e_2}`, simultaneous fails at `A` | ATTEMPTED |
| nmunopp untimed union | score reverse/face from `M ∪ O` | union is signed letters without a disjointness test against the pair | ATTEMPTED |
| unique letter | replace mixed sets by a singleton or `UNDEFINED` | mixed `O(A,τ)` remains a set; unique-letter simultaneous at `A` is `UNDEFINED` while simultaneous fails | ATTEMPTED |
| exist-opposite of leftover axes | score `a+b=(0,0,0)` inside leftover axis vectors | leftover reverse is leftover-empty fail here; simultaneous reverse is HOLD iff simultaneous | ATTEMPTED |
| same-tick-inclusive six-neighbor lock union | score locks of six-neighbors formed by `t(q)` | that leftover includes partner seed letters; simultaneous is own `M` against own `O` | ATTEMPTED |
| two-tick lock-count clock | score a lock-count clock across two ticks | different member; this display scores simultaneous of own incoming and outgoing at `t+1` | ATTEMPTED |
| mixed #7188 fail/fail | reuse z-symmetric mixed `M` reverse-fail face-fail | different process; this member reports reverse fail and face hold from simultaneous | ATTEMPTED |
| one-axis leftover | treat `(0,0,1)` and `(0,1,1)` as formed children of `+e_1/+e_1` | those children lock `+e_3` at tick 1; here they are seeds locking `+e_2/+e_2` at tick 0 | ATTEMPTED |
| y-probe simultaneous | score the four y-probes on this seed | y-probe reverse HOLDs and face HOLDs; this letter is the four z-probes with seed `A` locking `+e_2` | ATTEMPTED |
| x-probe simultaneous | score the four x-probes on this seed | x-probe reverse HOLDs and face HOLDs; this letter is the four z-probes | ATTEMPTED |
| sum of a set | replace simultaneous by a `Z^3` sum | the construction does not sum; simultaneous is signed-letter disjointness of two sets | ATTEMPTED |
| named-sign lettering | collapse `{±e_i}` to `{+,−}` | named-sign lettering lost the axis | ATTEMPTED |
| global later T | wait until `max t(A,B,C,D)` before reading | `τ(q)=t(q)+1` is per-probe; no global T | ATTEMPTED |
| attach a formation member from already-recorded six-neighbor locks | form the probes by a neighbor-lock letter instead of perp-step | refused; not attached | ATTEMPTED |
| adopt bits into Admissibility | rewrite the local rule by simultaneous | refused; displayed, not adopted | ATTEMPTED |

### N2 — wall independence

Missing physical adoption, missing identification of simultaneous with
leftover of `M` alone, missing identification of simultaneous with
leftover-empty fail, missing identification of simultaneous with
existential opposite of signed locks, missing identification of
simultaneous with unsigned axis-cover, missing identification of
simultaneous with 1-in 2-out split, missing identification of this member
with nm2simz HOLDING, and missing Record identification of simultaneous
reverse are distinct open premises. This note claims no complete wall
collection.

### N3 — hidden-condition scan

The host `B_3(0)`, four-site two-axis same-lock seed, perpendicular step
rule, incoming-step lock, own incoming set and own outgoing dual from
records with tick `<= τ`, per-probe `τ=t+1`, simultaneous as defined
nonempty disjoint `M` and `O`, HOLD iff simultaneous not leftover-empty
fail, four z-probes with seed `A`, and mixed remains a set are declared. No
uniqueness of incoming locks, no six-neighbor lock union as the scored
object, no lock-count clock, no global later T, no formation attachment
from already-recorded six-neighbor locks, and no Admissibility rewrite are
silently assumed.

### N4 — source residual matching

The current axiom memo supplies cubic sites, `M_2(C)`,
content-conditional-on-formation, and unreadable absence. The residual that
formation site, probability, and rate remain unsupplied is unchanged. The
simultaneous reverse fail and face hold reports do not close that residual.

### N5 — resolution and rhetoric audit

| Resolution | Executed | Not claimed |
|---|---|---|
| per element | each signed lock among `{±e_1,±e_2,±e_3}` in `M` or in `O` | no continuum alphabet |
| per site | `A,B,C,D` z-probes on `B_3(0)` only | no other cubic sites |
| per mode | no mode calculation | no spectral exhaustion |
| per block | four sim reports, reverse/face from sim HOLD | no adopted content law |
| lattice wide | checked and not executed | no lattice-wide lettering rule |

### N6 — live partial-closure paths

Live routes include a later Record content map for simultaneous reverse/face,
a formation-rate rule, and a physical selector among disjoint incoming and
outgoing letters. None is taken here.

### N7 — hostile steelman

**Steelman:** Simultaneous HOLD is only leftover empty; leftover-empty fail
already answered three-axis occupation; leftover of `M` alone already gives
a third direction; complementary occupation is only nm2slz cover; empty
letter intersection is only nmsimopp; 1-in 2-out already failed reverse on
these z-probes; the second pair is only a child of the first pair; nm2simz
already HOLDs simultaneous on z-probes so same-lock is only a sign flip;
and empty `M` or empty `O` should be `UNDEFINED` like unformed.

**Answer:** Leftover empty is unsigned unoccupied directions of `M` and `O`
together. Leftover-empty fail scores that empty leftover as reverse fail
and face fail. Simultaneous HOLDs when `M` and `O` are defined nonempty
and signed-letter disjoint. Opposite signs on one axis are letter-disjoint
and occupy that axis, so they can HOLD simultaneous and fail cover. On this
same seed, y-probe `D` HOLDs simultaneous and fails cover and fails 1-in
2-out. Cover reverse and 1-in 2-out reverse also fail on these z-probes,
but that unsigned overlap of `e_2` is not this letter: here the shared
letter at `A` is the signed partner `+e_2`. nm2simz HOLDs at `A` because
the opposite partner letter is `−e_2`, which is not in `O(A)`. This member
has same-lock partner letter `+e_2` already in `O(A)` at tick 0. Leftover
of `M` alone and leftover of `O` alone are one-sided leftovers and are
unequal across reverse here. The second pair is seeded at tick 0 with
`+e_2/+e_2`, not formed at tick 1 with `+e_3`. Empty `M` or empty `O`
fails by declaration, and is not `UNDEFINED`. Reverse simultaneous is HOLD
iff simultaneous at `A` and at `B`, not leftover-empty fail and not leftover
of nm2simz HOLDING.

### N8 — cross-cycle echo

nm2simz HOLDING on two-axis opposite z-probes reports simultaneous HOLD at
each of the four z-probes, reverse hold, and face hold. nm2slz axis-cover
on this same seed reports cover fail at `A`, reverse fail, and face hold.
nm2sl12z 1-in 2-out on this same seed reports split fail at `A`, reverse
fail, and face hold. 1-axis same-lock simultaneous HOLDs at each of the
four z-probes, reverse hold, and face hold, with `t(A)=1`. Two-axis
same-lock y-probes report simultaneous reverse hold and simultaneous face
hold. This note is not those displays: it reports simultaneous `M` and `O`
at `τ=t+1` on two disjoint same-lock pairs with z-probes, simultaneous fail
at `A`, simultaneous HOLD at `B`,`C`,`D`, reverse fail, and face hold. HOLD
iff simultaneous, not leftover-empty fail, not axis-cover, not 1-in 2-out,
and not leftover of nm2simz HOLDING.

**Gate disposition:** PASS for the simultaneous `t+1` reverse/face reports
above. FAIL / DO NOT SHIP for “the predicate equals the named sign,” “the
predicate equals the unique singleton lock vector,” “the predicate equals
six-neighbor lock union,” “the predicate equals leftover-empty fail,” “the
predicate equals leftover of `M` alone,” “the predicate equals leftover of
`O` alone,” “the predicate equals nmsimopp exist-opposite HOLD,” “the
predicate equals nm2slz axis-cover,” “the predicate equals nm2sl12z 1-in
2-out,” “the predicate equals nm2simz HOLDING,” “the predicate equals
nmunopp union,” “bits are Admissibility,” “simultaneous HOLDs at `A`,”
“simultaneous fails at `D`,” “reverse simultaneous HOLDs,” or “face
simultaneous fails.”

## Primary runner

The paired runner builds Euclidean `B_3(0)`, runs the two-axis same-lock
perp-step incoming-lock process, reads each z-probe's own earliest incoming
set and own outgoing dual from the record prefix at that probe's `t+1`,
reports the intersection of the pair, reports simultaneous of the pair,
lists new records in `B_3(0)` between `t` and `t+1` that meet a probe's
six-neighbors, compares to nm2simz HOLDING, and checks Theorems 1--3. It
also checks that simultaneous fails at `A` and HOLDs at `B`,`C`,`D`, that
leftover-empty fail is a different face, that leftover of `M` alone and
leftover of `O` alone are different objects, that mixed sets remain sets,
that unique-letter simultaneous is `UNDEFINED` at mixed `O(A)`, that the
construction does not sum, that a formation member from already-recorded
six-neighbor locks is not attached, that unsigned axis-cover is a different
letter, that 1-in 2-out is a different letter, and that the display is not
the two-tick lock-count clock composition. No runner cache is written.
