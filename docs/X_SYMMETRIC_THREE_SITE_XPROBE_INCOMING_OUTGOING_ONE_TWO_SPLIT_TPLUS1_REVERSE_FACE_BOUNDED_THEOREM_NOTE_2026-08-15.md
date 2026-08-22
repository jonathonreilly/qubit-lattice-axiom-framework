---
claim_id: x_symmetric_three_site_xprobe_incoming_outgoing_one_two_split_tplus1_reverse_face_bounded_theorem_note_2026-08-15
claim_type: bounded_theorem
claim_scope: "1-in 2-out axis split of M and O at t+1 on the four #7213 x-probes, and reverse/face from that, are reported. Displayed, not adopted."
upstream_dependencies:
  - minimal_axioms
runner: scripts/x_symmetric_three_site_xprobe_incoming_outgoing_one_two_split_tplus1_reverse_face_2026_08_15.py
---

# Incoming And Outgoing 1-In 2-Out Axis Split At t+1 Reverse And Face On Four #7213 X-Probes

> **Key terms used in this doc** are indexed A-Z at `docs/KEY_TERMINOLOGY.md`;
> each row points to the canonical source-of-truth doc.

**Date:** 2026-08-15
**Type:** bounded_theorem
**Scope:** 1-in 2-out axis split of simultaneous earliest incoming set `M`
and outgoing dual `O` at each probe's `τ=t+1`, and reverse/face from that
split, on the four nmszopx #7213 x-probes in `B_3(0)={n:n·n<=9}`. Same
process and x-probes as nmszopx #7213. Let `t(q)` be the formation tick of
probe `q`. Let `τ(q)=t(q)+1`. `M(q,τ)` is the set of earliest incoming
nearest-neighbor steps at `q` using only records with tick `<= τ`. Seeds
are a singleton seed letter. `O(q,τ)` is the outgoing dual of `M`: the set
of `e` in `{±e_1,±e_2,±e_3}` such that `q+e` is formed and `e` is in
`M(q+e,τ)`. Unformed at `τ` is `UNDEFINED`. Empty `O` is empty, not
`UNDEFINED`. Axis of a defined lock set `S` is
`Axis(S)={e_i | some ±e_i in S}`. Cover HOLDs at `q` if and only if
`Axis(M)∩Axis(O)` is empty and `Axis(M)∪Axis(O)` equals `{e_1,e_2,e_3}`.
Split HOLDs at `q` if and only if cover HOLDs and `|Axis(M)|=1`. That is
1-in 2-out. `UNDEFINED` if `M` or `O` is `UNDEFINED`. Else fail. 2-in 1-out
is fail. Reverse HOLDs if and only if split HOLDs at `A` and at `B`. Face
HOLDs if and only if split HOLDs at `C` and at `D`. Either side
`UNDEFINED` is `UNDEFINED`. This is not leftover of leftover-of-cover
reverse/face. This is not leftover-empty fail. This is not leftover of
leftover-of-`M` alone. This is not leftover of leftover-of-`O` alone. This
is not leftover of nmszopx exist-opposite of `M`. This is not leftover of
mixed #7188 fail/fail. Uniqueness of incoming or outgoing locks is not
required. Mixed remains a set. Occupancy of sites is not used. Displayed,
not adopted. Do not write into Admissibility. Do not attach L1.
**Audit-status authority:** independent audit lane only. This note authors no
audit verdict and predicts none.
**Primary runner:**
[`scripts/x_symmetric_three_site_xprobe_incoming_outgoing_one_two_split_tplus1_reverse_face_2026_08_15.py`](../scripts/x_symmetric_three_site_xprobe_incoming_outgoing_one_two_split_tplus1_reverse_face_2026_08_15.py)

Framework input:

- [`MINIMAL_AXIOMS_2026-06-29.md`](MINIMAL_AXIOMS_2026-06-29.md) supplies
  cubic-lattice sites `Z^3` with nearest-neighbor adjacency, the one-site
  algebra `M_2(C)`, and the Record sentences that records form and that a
  present record locks exactly one admissible local possibility.

Everything after that quoted input is a finite displayed process on `B_3(0)`
and the four named x-probes. Incoming lock letters are unit nearest-neighbor
steps. `O` is the outgoing dual of those incoming sets at the per-probe cut
`τ=t+1`. Axis is the unsigned lattice direction of a signed lock. Cover is
complementary occupation of `{e_1,e_2,e_3}` by `Axis(M)` and `Axis(O)`:
disjoint and complete. Split is cover plus `|Axis(M)|=1`: one incoming axis
and two outgoing axes. Reverse and face are scored on split at the two
reverse probes and the two face probes. Named signs `{+,−}` are a coarser
readout and are not used. A singleton unique lock letter is a different
readout and is not used as the object. Existential opposite of signed locks
is a different readout and is not used as the split reverse. Cover reverse
and cover face are a different readout: cover reverse HOLDs and cover face
HOLDs, while split reverse HOLDs and split face fails. Leftover of
unoccupied axes is a different readout. A `Z^3` sum of those locks is a
different readout and is not used. Occupancy of sites is not used. A
six-neighbor star is not the letter. O is not M.

## Machine status and trace

```yaml
actual_current_surface_status: bounded-support
target_claim_type: bounded_theorem
claim_type_reason: "Exact report of 1-in 2-out axis split of M and O at t+1 on the four #7213 x-probes, split hold at A,B,C, split fail at D, reverse hold and face fail from that split; uniqueness of incoming locks is not claimed and the bits are not adopted."
trace_class: frontier_discovery
target_claim_id: x_symmetric_three_site_xprobe_incoming_outgoing_one_two_split_tplus1_reverse_face
target_blocker_text: "display 1-in 2-out axis split of M and O at t+1 on the four #7213 x-probes, and reverse/face from that split, no unique lock required"
source_of_blocker_text: handoff
reachability_to_target: advances
artifact_role: theorem
next_trace_action: "Keep 1-in 2-out axis split of M and O at t+1 displayed; do not write split into Admissibility, do not reduce to leftover of cover reverse/face, do not reduce to leftover-empty fail, do not replace split by leftover of M alone or leftover of O alone, do not replace split by existential opposite of signed locks, do not use a six-neighbor star, do not use occupancy of sites, and do not attach L1."
conditional_surface_status: "exact on B_3(0) for 1-in 2-out axis split of M and O at t+1 on the four #7213 x-probes and reverse/face from that split; displayed, not adopted"
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

No larger host is used. The four x-probes are the only sites whose 1-in 2-out
axis split of `M` and `O` is scored:

```text
A = (1,0,0),  B = (1,1,1),  C = (2,0,0),  D = (1,1,0).
```

These are not the y-probes `A=(0,1,0)`, `B=(1,1,1)`, `C=(0,2,0)`,
`D=(1,1,0)`. `A` is a seed. Same process and x-probes as nmszopx #7213.

Lock alphabet of the displayed process: `{±e_i}` with `i` in `{1,2,3}`.

Seed: the three-record set `{0, (1,0,0), (-1,0,0)}` is recorded at formation
tick 0 with locks `+e_2` at the origin, `−e_2` at `(1,0,0)`, and `−e_2` at
`(-1,0,0)`. The third site is the x-mirror of the two-site opposite-lock
partner `(1,0,0)`. This seed is not the two-site opposite-lock seed
`{0,(1,0,0)}` and not the three-site opposite-lock seed whose third site is
`(0,1,0)` with lock `+e_1`. This seed is not the perp two-site seed
`+e_2/+e_1`. This seed is not the y-symmetric three-site seed
`{0,(0,1,0),(0,-1,0)}`. This seed is not the z-symmetric three-site seed
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

## Named 1-in 2-out axis split of `M` and `O` at `τ=t+1`

Let `t(q)` be the formation tick of x-probe `q` when that tick is defined in
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

Cover at the same cut:

```text
cover HOLD  <=>  Axis(M) ∩ Axis(O) empty
                 and Axis(M) ∪ Axis(O) = {e_1,e_2,e_3}
```

Split at the same cut:

```text
split HOLD  <=>  cover HOLD and |Axis(M)| = 1
```

when both `M` and `O` are defined. If `q` is unformed at `τ`, then split is
`UNDEFINED`. Else fail. Axis is unsigned: `+e_i` and `−e_i` occupy the same
axis. 1-in 2-out is cover with a singleton incoming axis. 2-in 1-out is fail:
cover may HOLD while `|Axis(M)|=2`, and that is not this split.

Reverse 1-in 2-out split holds if and only if split at `A` and split at `B`
both hold. Face 1-in 2-out split holds if and only if split at `C` and split
at `D` both hold. Either side `UNDEFINED` is `UNDEFINED`. Else if either
side fails, reverse or face fails.

Identifying a named sign of those locks with reverse or face is refused:
named-sign lettering lost the axis. Identifying existential opposite of
signed locks with split reverse is refused: split reverse is both-split of
unsigned 1-in 2-out. Identifying leftover-empty fail with split HOLD is
refused. Identifying leftover of leftover-of-cover reverse/face with this
split is refused: cover reverse HOLDs and cover face HOLDs, while this
face fails.

## Theorem 1 — ticks, `M`, `O`, `Axis`, cover, `|Axis(M)|`, and split at `τ=t+1`

On this process the four x-probes form. Compare to nmszopx: that leftover
reports own incoming `M` at formation with exist-opposite reverse hold and
face hold. Compare to axis-cover of timed `M` and `O` together at `τ=t+1`:
that leftover reports cover hold at each probe, cover reverse hold, and
cover face hold. This display reads unsigned 1-in 2-out axis split of timed
`M` and `O` together at `τ=t+1`:

```text
t(A)=0
t(B)=2
t(C)=1
t(D)=3
M(A, τ) = {−e_2}
M(B, τ) = {+e_2}
M(C, τ) = {+e_1}
M(D, τ) = {−e_1, +e_3, −e_3}
O(A, τ) = {+e_1, +e_3, −e_3}
O(B, τ) = {+e_1, +e_3, −e_3}
O(C, τ) = {+e_2, −e_2, +e_3, −e_3}
O(D, τ) = {+e_2, −e_2}
Axis(M)(A, τ) = {e_2}
Axis(O)(A, τ) = {e_1, e_3}
Axis(M)(B, τ) = {e_2}
Axis(O)(B, τ) = {e_1, e_3}
Axis(M)(C, τ) = {e_1}
Axis(O)(C, τ) = {e_2, e_3}
Axis(M)(D, τ) = {e_1, e_3}
Axis(O)(D, τ) = {e_2}
|Axis(M)|(A, τ) = 1
|Axis(M)|(B, τ) = 1
|Axis(M)|(C, τ) = 1
|Axis(M)|(D, τ) = 2
cover(A) = hold
cover(B) = hold
cover(C) = hold
cover(D) = hold
split(A) = hold
split(B) = hold
split(C) = hold
split(D) = fail
```

`A` is a seed at tick 0. Mixed remains a set: `M(D,τ)` has three earliest
incoming steps and `O(A,τ)` has three outgoing steps. Unique letters would
assign `UNDEFINED` at mixed probes. Here uniqueness is not required.
At `A`, `B`, and `C`, `Axis(M)` is a singleton and `Axis(O)` occupies the
other two axes: cover HOLDs and `|Axis(M)|=1`, so split HOLDs. At `D`,
`Axis(M)` occupies two axes and `Axis(O)` occupies one: cover HOLDs, but
2-in 1-out is fail, so split fails. Leftover of the union is empty at each
probe. Leftover-empty fail is not this object. Cover reverse HOLDs and
cover face HOLDs: those bits are leftover of leftover-of-cover reverse/face,
not this split. O is not M.

Investment nmszopx: signed exist-opposite of own incoming `M` HOLDs reverse
and face. Letter-opposite is not 1-in 2-out axis split. Leftover of `M`
alone at `A` and `B` is `{e_1,e_3}`, nonempty and equal, so leftover-of-`M`
reverse would hold while leftover-of-`M` face would fail. Leftover of `O`
alone at `A` and `B` is `{e_2}`, nonempty and equal, so leftover-of-`O`
reverse would hold while leftover-of-`O` face would fail. Those one-sided
leftovers are not this object.

New records in `B_3(0)` between `t` and `t+1` that meet a probe's
six-neighbors enter `O` and do not enter earliest `M`:

```text
new 6-NN of A at t(A)+1: (2, 0, 0), (1, 0, 1), (1, 0, -1)
new 6-NN of B at t(B)+1: (2, 1, 1), (1, 1, 2), (1, 1, 0)
new 6-NN of C at t(C)+1: (2, 1, 0), (2, -1, 0), (2, 0, 1), (2, 0, -1)
new 6-NN of D at t(D)+1: (1, 2, 0)
```

Split frozen at `t` fails reverse and face: `O` at `A`, `B`, and `C` is
empty at formation, so those probes miss axes until `t+1`. Split at `D`
already fails at formation because `|Axis(M)|=2`. Split at `τ` uses those
new neighbors at `A`, `B`, and `C`. The `t+1` cut is required. There is no
global T.

## Theorem 2 — reverse from 1-in 2-out axis split at `τ`

Reverse 1-in 2-out split holds if and only if split at `A` and split at `B`
both hold. Both splits are `hold`. Reverse holds.

Reverse 1-in 2-out split at τ: hold

Both sides are defined, so this is not `UNDEFINED`. This is not `fail`.
Leftover-empty reverse fails because leftover of the union is empty at `A`
and at `B`. Leftover-of-`M` reverse would hold because leftover of `M` at
`A` and at `B` is `{e_1, e_3}`. Leftover-of-`O` reverse would hold because
leftover of `O` at `A` and at `B` is `{e_2}`. Exist-opposite reverse of
signed `M` holds. Cover reverse HOLDs. Those leftovers are not this
display. Reverse HOLD uses split at `A` and at `B`.

Reverse holds.

## Theorem 3 — face from 1-in 2-out axis split at `τ`

Face 1-in 2-out split holds if and only if split at `C` and split at `D`
both hold. Split at `C` is `hold`. Split at `D` is `fail` because 2-in
1-out is fail. Face fails.

Face 1-in 2-out split at τ: fail

Displayed, not adopted. The bits are not written into Admissibility.
Do not write into Admissibility. Do not attach L1.

This is not `hold` and not `UNDEFINED`. Cover face HOLDs because cover HOLDs
at `C` and at `D`. Leftover-empty face fails because leftover of the union
is empty at `C` and at `D`. Leftover of `M` at `C` is `{e_2, e_3}` and
leftover of `M` at `D` is `{e_2}`: nonempty and unequal, so leftover-of-`M`
face would fail. Leftover of `O` at `C` is `{e_1}` and leftover of `O` at
`D` is `{e_1, e_3}`: nonempty and unequal, so leftover-of-`O` face would
fail. Exist-opposite face of signed `M` holds and exist-opposite face of
signed `O` holds. Unique-letter leftover reports face `UNDEFINED` from
mixed `D`. This display scores 1-in 2-out complementary occupation of the
three lattice axes by `M` and `O` at `τ`, which HOLDs at `C` and fails at
`D`, so face fails.

Face fails.

## What this note does not claim

- It does not select a unique incoming, outgoing, or leftover lock.
- It does not reduce lock vectors to named signs `{+,−}`.
- It does not require split to be a singleton lock on either side.
- It does not sum either set.
- It does not replace split by leftover of leftover-of-cover reverse/face.
- It does not replace split by leftover-empty fail.
- It does not replace split by leftover of `M` alone.
- It does not replace split by leftover of `O` alone.
- It does not replace split by existential opposite of signed locks.
- It does not replace `O` by `M`.
- It does not replace split by locks of six-neighbors.
- It does not use a six-neighbor star as the letter.
- It does not wait for a global later T.
- It does not attach a formation member from already-recorded six-neighbor
  locks.
- It does not reprint nmszopx exist-opposite of `M`.
- It does not reprint leftover-empty fail as this member.
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
x-symmetric three-site process, 1-in 2-out axis split of `M` and `O` at
`t+1`, and the reverse/face bits from that split are displayed theorem-domain
data.

## Exact target and obligation graph

| Obligation | Status |
|---|---|
| current Lattice / Admissibility / Record premises | quoted; no edit |
| perp-step incoming-lock process on `B_3(0)` | displayed; nmszopx #7213 seed `+e_2/−e_2/−e_2` |
| ticks `t(A)`, `t(B)`, `t(C)`, `t(D)` | Theorem 1; `0`, `2`, `1`, `3` |
| `M` at `τ=t+1` | Theorem 1; frozen equal to `M` at `t` |
| `O` at `τ=t+1` | Theorem 1; HOLDING outgoing dual |
| `Axis(M)` and `Axis(O)` at `τ` | Theorem 1; complementary at each probe |
| cover at `τ` | Theorem 1; hold at each probe |
| `|Axis(M)|` at `τ` | Theorem 1; `1`,`1`,`1`,`2` |
| split at `τ` | Theorem 1; hold, hold, hold, fail |
| reverse from 1-in 2-out split at `τ` | Theorem 2; `hold` |
| face from 1-in 2-out split at `τ` | Theorem 3; `fail` |
| unique incoming lock | not required |
| occupancy of sites as the letter | not used |
| named-sign `{+,−}` letter | not used; lost the axis |
| singleton unique lock-vector letter | not used as the object; mixed remains a set |
| `Z^3` sum of the lock set | not used; no aggregation |
| six-neighbor star as the letter | not used |
| leftover of leftover-of-cover reverse/face | not this split display |
| leftover of leftover-empty fail | not this split display |
| leftover of leftover-of-`M` alone | not this display |
| leftover of leftover-of-`O` alone | not this display |
| leftover of nmszopx exist-opposite of `M` | not this display |
| leftover of mixed #7188 fail/fail | not this display |
| global later T | not used |
| 1-in 2-out axis split as Admissibility content | not adopted |
| formation site / probability / rate | open |
| physical Record readout of the bits | open |

## Value gate (V1–V5)

| # | Answer |
|---|---|
| V1 | It answers the first-display question: 1-in 2-out axis split of `M` and `O` at `t+1` on the four #7213 x-probes, and reverse/face from that split. |
| V2 | Current main has no landed 1-in 2-out split reverse/face of timed `M` and `O` on these four #7213 x-probes. |
| V3 | Split bits at one cut and the two split reverse/face bits are independently finite and exact. |
| V4 | The theorem is more than a restatement of Record because it reads unsigned 1-in 2-out occupation of own incoming and own outgoing at the same `t+1` cut and scores reverse/face from that split. |
| V5 | It is not an adopted content rule: the bits remain displayed. |

## No-go discipline gate

The negative content is narrow: the display does not write those bits into
Admissibility, does not reduce them to named signs, does not require a
unique lock, does not replace split by leftover of leftover-of-cover
reverse/face, leftover-empty fail, leftover of `M` alone, or leftover of
`O` alone, does not replace split by existential opposite of signed locks,
and does not identify this display with nmszopx exist-opposite HOLD. No
global impossibility is claimed.

### N1 — materially distinct routes

| Route | Attempt | Why it fails here | Marker |
|---|---|---|---|
| leftover of leftover-of-cover reverse/face | score reverse/face from cover without `|Axis(M)|=1` | cover HOLDs at each probe, cover reverse HOLDs, cover face HOLDs; split face fails at 2-in 1-out `D` | ATTEMPTED |
| leftover-empty fail | score leftover of the union empty as reverse fail | leftover of the union is empty at each probe, leftover-empty reverse fails, split reverse HOLDs | ATTEMPTED |
| leftover of `M` alone | score `{e_1,e_2,e_3}` minus `Axis(M)` | leftover of `M` at `A` and `B` is `{e_1,e_3}`, nonempty equal, leftover-of-`M` reverse would hold while leftover-of-`M` face would fail | ATTEMPTED |
| leftover of `O` alone | score `{e_1,e_2,e_3}` minus `Axis(O)` | leftover of `O` at `A` and `B` is `{e_2}`, nonempty equal, leftover-of-`O` reverse would hold while leftover-of-`O` face would fail | ATTEMPTED |
| nmszopx exist-opposite of `M` | reuse signed reverse hold and face hold of own incoming `M` | those bits HOLD; split is unsigned 1-in 2-out of `M` and `O` together at `t+1` | ATTEMPTED |
| unique letter | replace mixed sets by a singleton or `UNDEFINED` | mixed `M(D,τ)` and mixed `O(A,τ)` remain sets; unique-letter split at `D` is `UNDEFINED`; this split fails at `D` | ATTEMPTED |
| exist-opposite of leftover axes | score `a+b=(0,0,0)` inside leftover axis vectors | split reverse is both-split of 1-in 2-out, not opposite of unsigned leftover axes | ATTEMPTED |
| letter intersection as split | score reverse/face inside `M ∩ O` | letter intersection empty is not 1-in 2-out; opposite signs can share an axis | ATTEMPTED |
| same-tick-inclusive six-neighbor lock union | score locks of six-neighbors formed by `t(q)` | that leftover includes neighbor locks; split is unsigned 1-in 2-out of `M` and `O` at `t+1` | ATTEMPTED |
| frozen split at `t` | score split from `M` and `O` at formation | split at `t` fails reverse and face because `O` at `A`, `B`, and `C` is empty at formation | ATTEMPTED |
| mixed #7188 fail/fail | reuse z-symmetric mixed `M` reverse-fail face-fail | different process; this member reports split hold, hold, hold, fail, reverse hold, and face fail | ATTEMPTED |
| sum of a set | replace split by a `Z^3` sum | the construction does not sum; split is 1-in 2-out of unsigned axes | ATTEMPTED |
| named-sign lettering | collapse `{±e_i}` to `{+,−}` | named-sign lettering lost the axis | ATTEMPTED |
| global later T | wait until `max t(A,B,C,D)` before reading | `τ(q)=t(q)+1` is per-probe; no global T | ATTEMPTED |
| attach a formation member from already-recorded six-neighbor locks | form the probes by a neighbor-lock letter instead of perp-step | refused; not attached | ATTEMPTED |
| adopt bits into Admissibility | rewrite the local rule by 1-in 2-out split | refused; displayed, not adopted | ATTEMPTED |

### N2 — wall independence

Missing physical adoption, missing identification of split with leftover of
leftover-of-cover reverse/face, missing identification of split with
leftover-empty fail, missing identification of split with leftover of `M`
alone, missing identification of split with existential opposite of signed
locks, and missing Record identification of split reverse are distinct open
premises. This note claims no complete wall collection.

### N3 — hidden-condition scan

The host `B_3(0)`, x-symmetric three-site seed locks `+e_2`, `−e_2`, and
`−e_2`, perpendicular step rule, incoming-step lock, own incoming set and
own outgoing dual from records with tick `<= τ`, per-probe `τ=t+1`,
unsigned axis, cover of `Axis(M)` and `Axis(O)`, split HOLD iff cover HOLD
and `|Axis(M)|=1`, reverse HOLD iff split at `A` and `B`, four x-probes
with seed `A`, and mixed remains a set are declared. No uniqueness of
incoming locks, no six-neighbor lock union as the scored object, no
leftover-empty fail as the scored object, no leftover of leftover-of-cover
as the scored object, no global later T, no formation attachment from
already-recorded six-neighbor locks, and no Admissibility rewrite are
silently assumed.

### N4 — source residual matching

The current axiom memo supplies cubic sites, `M_2(C)`,
content-conditional-on-formation, and unreadable absence. The residual that
formation site, probability, and rate remain unsupplied is unchanged. The
split `hold`/`fail` reports do not close that residual.

### N5 — resolution and rhetoric audit

| Resolution | Executed | Not claimed |
|---|---|---|
| per element | each unsigned lattice axis among `{e_1,e_2,e_3}` occupied by `M` or by `O` | no continuum alphabet |
| per site | `A,B,C,D` x-probes on `B_3(0)` only | no other cubic sites |
| per mode | no mode calculation | no spectral exhaustion |
| per block | four 1-in 2-out split bits, reverse/face from split at `t+1` | no adopted content law |
| lattice wide | checked and not executed | no lattice-wide lettering rule |

### N6 — live partial-closure paths

Live routes include a later Record content map for split reverse/face, a
formation-rate rule, and a physical selector among `{±e_i}`. None is taken
here.

### N7 — hostile steelman

**Steelman:** Split HOLD is only cover restated; cover reverse HOLDs and
cover face HOLDs already answered complementary occupation; leftover-empty
fail already answered complementary occupation; leftover of `M` alone
already gives the third directions `{e_1,e_3}` at `A`; leftover of `O`
alone already gives `{e_2}`; nmszopx already answered reverse hold and
face hold from signed `M`; mixed `D` should be `UNDEFINED`; and 1-in 2-out
is only `|Axis(M)|=1`, not a split predicate.

**Answer:** Cover HOLDs at each of the four x-probes, so cover reverse HOLDs
and cover face HOLDs. Split requires cover and `|Axis(M)|=1`. At `D`,
cover HOLDs with `|Axis(M)|=2`: 2-in 1-out is fail. Those two predicates
disagree on face: cover face HOLDs, split face fails. Leftover of the union
is unsigned unoccupied directions of `M` and `O` together. Leftover-empty
reverse fails by declaration of nonempty leftover equality. Split reverse
HOLDs. Leftover of `M` alone and leftover of `O` alone are nonempty
one-sided leftovers. Exist-opposite of signed `M` HOLDs reverse and face
without reading `O`. Unique-letter leftover reports face `UNDEFINED` from
mixed `D`; mixed remains a set and split fails at `D` because two incoming
axes occupy cover. 1-in 2-out is why split HOLDs at `A`, `B`, and `C` and
fails at `D`. Reverse 1-in 2-out split is both-split, not leftover of
leftover-of-cover reverse/face and not exist-opposite of signed locks.

### N8 — cross-cycle echo

nmszopx #7213 reported reverse hold and face hold from own incoming `M`.
Axis-cover of `M` and `O` at `τ=t+1` on this same process reports cover
hold at each probe, cover reverse hold, and cover face hold. Leftover-axis
of `M` and `O` at `τ=t+1` on a different two-site process reported leftover
empty at each probe, leftover reverse fail, and leftover face fail. This
note is not those displays: it reports 1-in 2-out axis split of `M` and `O`
at `τ=t+1` on the four #7213 x-probes, split hold at `A`, `B`, and `C`,
split fail at `D`, reverse hold, and face fail.

**Gate disposition:** PASS for the 1-in 2-out `t+1` reverse/face reports
above. FAIL / DO NOT SHIP for “the predicate equals the named sign,” “the
predicate equals the unique singleton lock vector,” “the predicate equals
six-neighbor lock union,” “the predicate equals leftover of leftover-of-cover
reverse/face,” “the predicate equals leftover-empty fail,” “the predicate
equals leftover of `M` alone,” “the predicate equals leftover of `O`
alone,” “the predicate equals nmszopx exist-opposite HOLD,” “bits are
Admissibility,” “split HOLDs at `D`,” “reverse 1-in 2-out split fails,”
“face 1-in 2-out split HOLDs,” or “mixed split is `UNDEFINED`.”

## Primary runner

The paired runner builds Euclidean `B_3(0)`, runs the nmszopx #7213
perp-step incoming-lock process, reads each probe's own earliest incoming
set and own outgoing dual from the record prefix at that probe's `t+1`,
reports unsigned axis of each, reports cover of those axes, reports
`|Axis(M)|`, reports 1-in 2-out split, lists new records in `B_3(0)`
between `t` and `t+1` that meet a probe's six-neighbors, and checks
Theorems 1--3. It also checks that split HOLDs at `A`, `B`, and `C` and
fails at `D`, that 2-in 1-out is fail, that cover reverse HOLDs and cover
face HOLDs while split face fails, that leftover-empty reverse fails while
split reverse HOLDs, that leftover of `M` alone and leftover of `O` alone
are different objects, that mixed sets remain sets, that unique-letter
split at mixed `D` is `UNDEFINED`, that split frozen at `t` fails reverse
and face, that the construction does not sum, that a formation member from
already-recorded six-neighbor locks is not attached, and that occupancy of
sites is not used. No runner cache is written.
