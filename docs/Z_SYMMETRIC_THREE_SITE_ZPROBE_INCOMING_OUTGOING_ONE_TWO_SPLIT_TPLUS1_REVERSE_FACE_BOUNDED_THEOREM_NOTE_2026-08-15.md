---
claim_id: z_symmetric_three_site_zprobe_incoming_outgoing_one_two_split_tplus1_reverse_face_bounded_theorem_note_2026-08-15
claim_type: bounded_theorem
claim_scope: "1-in 2-out axis split of M and O at t+1 on the four #7186 z-probes, and reverse/face from that, are reported. Displayed, not adopted."
upstream_dependencies:
  - minimal_axioms
runner: scripts/z_symmetric_three_site_zprobe_incoming_outgoing_one_two_split_tplus1_reverse_face_2026_08_15.py
---

# Incoming And Outgoing 1-In 2-Out Axis Split At t+1 Reverse And Face On Four #7186 Z-Probes

> **Key terms used in this doc** are indexed A-Z at `docs/KEY_TERMINOLOGY.md`;
> each row points to the canonical source-of-truth doc.

**Date:** 2026-08-15
**Type:** bounded_theorem
**Scope:** 1-in 2-out axis split of simultaneous earliest incoming set `M` and
outgoing dual `O` at each probe's `τ=t+1`, and reverse/face from that split,
on the four nszopinz #7186 z-probes in `B_3(0)={n:n·n<=9}`. Same process as
the z-symmetric three-site seed. Let `t(q)` be the formation tick of probe
`q`. Let `τ(q)=t(q)+1`. `M(q,τ)` is the set of earliest incoming
nearest-neighbor steps at `q` using only records with tick `<= τ`. Seeds are
a singleton seed letter. `O(q,τ)` is the outgoing dual of `M`: the set of
`e` in `{±e_1,±e_2,±e_3}` such that `q+e` is formed and `e` is in
`M(q+e,τ)`. Unformed at `τ` is `UNDEFINED`. Empty `O` is empty, not
`UNDEFINED`. Axis of a defined lock set `S` is `Axis(S)={e_i | some ±e_i in
S}`. Cover holds at `q` if and only if `Axis(M)` intersect `Axis(O)` is empty
and `Axis(M)` union `Axis(O)` equals `{e_1,e_2,e_3}`. Split holds at `q` if
and only if cover holds and `|Axis(M)|=1` (hence `|Axis(O)|=2`). Unformed at
`τ` is `UNDEFINED`. Else fail. 2-in 1-out is fail of this object, not
`UNDEFINED`. Reverse holds if and only if split holds at `A` and at `B`.
Face holds if and only if split holds at `C` and at `D`. Either side
`UNDEFINED` is `UNDEFINED`. This is not leftover-axis reverse of #7167. This
is not leftover of leftover-of-`M` alone. This is not leftover of
leftover-of-`O` alone. This is not leftover of the two-site opposite-lock
process. This is not leftover of nszopinz exist-opposite of signed locks.
This is not leftover of unique-letter mixed `UNDEFINED`. This is not leftover
of axis-cover reverse/face on the same four probes: cover can HOLD at a
2-in 1-out probe while split FAILs. Uniqueness of incoming or outgoing locks
is not required. Mixed remains a set. Occupancy of sites is not used.
Named-sign lettering is not used. The construction does not use a
six-neighbor star. Displayed, not adopted. Do not write into Admissibility.
Do not attach L1. This note does not write 1-in 2-out axis split into
Admissibility and does not attach a formation member from already-recorded
six-neighbor locks. This display does not use occupancy. Mixed stays a set.
**Audit-status authority:** independent audit lane only. This note authors no
audit verdict and predicts none.
**Primary runner:**
[`scripts/z_symmetric_three_site_zprobe_incoming_outgoing_one_two_split_tplus1_reverse_face_2026_08_15.py`](../scripts/z_symmetric_three_site_zprobe_incoming_outgoing_one_two_split_tplus1_reverse_face_2026_08_15.py)

Framework input:

- [`MINIMAL_AXIOMS_2026-06-29.md`](MINIMAL_AXIOMS_2026-06-29.md) supplies
  cubic-lattice sites `Z^3` with nearest-neighbor adjacency, the one-site
  algebra `M_2(C)`, and the Record sentences that records form and that a
  present record locks exactly one admissible local possibility.

Everything after that quoted input is a finite displayed process on `B_3(0)`
and the four named z-probes. Incoming lock letters are unit nearest-neighbor
steps. `O` is the outgoing dual of those incoming sets at the per-probe cut
`τ=t+1`. Axis is the unsigned lattice direction of a signed lock. Cover is
complementary occupation of `{e_1,e_2,e_3}` by `Axis(M)` and `Axis(O)`.
Split is cover together with `|Axis(M)|=1`. Reverse and face are scored on
split at the paired probes. Named signs `{+,−}` are a coarser readout and
are not used. A singleton unique lock letter is a different readout and is
not used as the object. Existential opposite of signed locks is a different
readout and is not used as the split reverse. Leftover-axis equality of
nonempty leftovers is a different readout. Axis-cover reverse/face of the
same timed `M` and `O` is a different readout: cover HOLD at every probe
does not force split HOLD. A `Z^3` sum of those locks is a different
readout and is not used. Occupancy of sites is not used. A six-neighbor star
is not the letter.

## Machine status and trace

```yaml
actual_current_surface_status: bounded-support
target_claim_type: bounded_theorem
claim_type_reason: "Exact report of 1-in 2-out axis split of M and O at t+1 on the four #7186 z-probes, split hold at A,B,C and fail at D, reverse hold and face fail from split; uniqueness of locks is not claimed and the bits are not adopted."
trace_class: frontier_discovery
target_claim_id: z_symmetric_three_site_zprobe_incoming_outgoing_one_two_split_tplus1_reverse_face
target_blocker_text: "display 1-in 2-out axis split of M and O at t+1 on the four #7186 z-probes, and reverse/face from that split, no unique lock required"
source_of_blocker_text: handoff
reachability_to_target: advances
artifact_role: theorem
next_trace_action: "Keep 1-in 2-out axis split of M and O at t+1 displayed; do not write split into Admissibility, do not reduce to leftover-axis reverse of #7167, do not reduce to leftover of M alone or leftover of O alone, do not replace split by existential opposite of signed locks, do not identify the display with axis-cover reverse/face of the same four probes, do not identify the display with the two-site opposite-lock leftover-empty fail, and do not attach L1."
conditional_surface_status: "exact on B_3(0) for 1-in 2-out axis split of M and O at t+1 on the four #7186 z-probes and reverse/face from that split; displayed, not adopted"
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

No larger host is used. The four z-probes are the only sites whose 1-in 2-out
axis split of `M` and `O` is scored:

```text
A = (0,0,1),  B = (1,1,1),  C = (0,0,2),  D = (1,0,1).
```

These are not the y-probes `A=(0,1,0)`, `B=(1,1,1)`, `C=(0,2,0)`,
`D=(1,1,0)`. These are not the x-probes `A=(1,0,0)`, `B=(1,1,1)`,
`C=(2,0,0)`, `D=(1,1,0)`. `A` is a seed. Same process and z-probes as
nszopinz #7186.

Lock alphabet of the displayed process: `{±e_i}` with `i` in `{1,2,3}`.

Seed: the three-record set `{0, (0,0,1), (0,0,−1)}` is recorded at formation
tick 0 with locks `L(0)=+e_1`, `L(0,0,1)=−e_1`, and `L(0,0,−1)=−e_1`. This
seed is not the two-site opposite seed `{0,(0,0,1)}`. This seed is not the
perp two-site seed `+e_1/+e_2`. This seed is not the y-symmetric three-site
seed `{0,(0,1,0),(0,-1,0)}`. This seed is not the nstri third site
`(1,0,0)+e_3`.

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

Cover of `M` and `O` at the same cut:

```text
cover(q) HOLD iff Axis(M(q,τ)) intersect Axis(O(q,τ)) is empty
and Axis(M(q,τ)) union Axis(O(q,τ)) equals {e_1,e_2,e_3}.
```

1-in 2-out axis split of `M` and `O` at the same cut:

```text
split(q) HOLD iff cover(q) HOLD and |Axis(M(q,τ))|=1.
```

If `q` is unformed at `τ`, then split is `UNDEFINED`. Else fail. Axis is
unsigned: `+e_i` and `−e_i` occupy the same axis. Cover is complementary
occupation of the three lattice axes. Split is the strict 1-in 2-out slice
of cover: `|Axis(M)|=1` and therefore `|Axis(O)|=2`. 2-in 1-out is fail of
this object, not `UNDEFINED`: cover can HOLD with `|Axis(M)|=2` and
`|Axis(O)|=1`, and that is split fail. 0-in 3-out and 3-in 0-out also fail
split. Leftover of the union `{e_1,e_2,e_3}` minus `(Axis(M) union Axis(O))`
empty is weaker than cover, and cover is weaker than split. Leftover of `M`
alone is a different object. Leftover of `O` alone is a different object.

Reverse 1-in 2-out axis split holds if and only if split at `A` and split at
`B` both HOLD. Face 1-in 2-out axis split holds if and only if split at `C`
and split at `D` both HOLD. Either side `UNDEFINED` is `UNDEFINED`. Else
fail.

Identifying a named sign of those locks with reverse or face is refused:
named-sign lettering lost the axis. Identifying leftover-axis reverse of
#7167 with this reverse is refused: leftover reverse fails when leftover
is empty, and this reverse holds from split. Identifying existential
opposite of signed locks with split reverse is refused: opposite signs on
one axis exist-opposite HOLD and fail cover, hence fail split. Identifying
axis-cover reverse/face of the same four probes with this reverse/face is
refused: cover HOLD at `D` is 2-in 1-out, so cover face HOLD and split face
FAIL.

## Theorem 1 — ticks, `M`, `O`, `Axis`, cover, `|Axis(M)|`, and split at `τ=t+1`

On this process the four z-probes form. Compare to nszopinz #7186: that
leftover reports same-tick union own incoming lock with exist-opposite
reverse hold and face hold. Compare to #7167 leftover-axis: that leftover
reports empty leftover at each probe and leftover reverse fail, leftover
face fail. Compare to axis-cover of `M` and `O` at `t+1` on these four
z-probes: that leftover reports cover hold at each probe, reverse hold, and
face hold. This display reads unsigned 1-in 2-out axis split of timed `M`
and `O` on the z-symmetric three-site seed:

```text
t(A)=0
t(B)=2
t(C)=1
t(D)=3
M(A, τ) = {−e_1}
M(B, τ) = {+e_1}
M(C, τ) = {+e_3}
M(D, τ) = {+e_2, −e_2, −e_3}
O(A, τ) = {+e_2, −e_2, +e_3}
O(B, τ) = {+e_2, −e_2, +e_3}
O(C, τ) = {+e_1, −e_1, +e_2, −e_2}
O(D, τ) = {+e_1, −e_1}
Axis(M)(A, τ) = {e_1}
Axis(O)(A, τ) = {e_2, e_3}
Axis(M)(B, τ) = {e_1}
Axis(O)(B, τ) = {e_2, e_3}
Axis(M)(C, τ) = {e_3}
Axis(O)(C, τ) = {e_1, e_2}
Axis(M)(D, τ) = {e_2, e_3}
Axis(O)(D, τ) = {e_1}
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
At each probe, `Axis(M)` and `Axis(O)` are complementary: their union is
`{e_1,e_2,e_3}` and their intersection is empty. Cover therefore holds at
each probe. Split holds at `A`, `B`, and `C` because `|Axis(M)|=1`. Split
fails at `D` because `|Axis(M)|=2`: that is 2-in 1-out, and 2-in 1-out is
fail. Leftover of the union is empty at each probe. Empty leftover fails
leftover reverse of #7167; split reverse holds here. Axis-cover reverse
holds and axis-cover face holds; split face fails. O is not M.

Investment nm12opp first of 1-in 2-out. Transfer onto HOLDING `M` of
nszopinz #7186 uses the z-symmetric three-site seed, not the two-site #7167
seed. The four z-probe `M` and `O` values at `τ` coincide with those
two-site opposite-lock z-probe values; the seed is still three sites at
tick 0, including `(0,0,−1)`.

New records in `B_3(0)` between `t` and `t+1` that meet a probe's
six-neighbors enter `O` and do not enter earliest `M`:

```text
new 6-NN of A at t(A)+1: (0, 1, 1), (0, -1, 1), (0, 0, 2)
new 6-NN of B at t(B)+1: (1, 2, 1), (1, 0, 1), (1, 1, 2)
new 6-NN of C at t(C)+1: (1, 0, 2), (-1, 0, 2), (0, 1, 2), (0, -1, 2)
new 6-NN of D at t(D)+1: (2, 0, 1)
```

## Theorem 2 — reverse from 1-in 2-out axis split at `τ`

Reverse 1-in 2-out axis split holds if and only if split at `A` and split at
`B` both HOLD. Both splits HOLD. Reverse holds.

Reverse 1-in 2-out axis split at τ: hold

Both sides are defined, so this is not `UNDEFINED`. Leftover-axis reverse
of #7167 fails because leftover is empty at `A` and at `B`. Leftover-of-`M`
reverse would hold because leftover of `M` at `A` and at `B` is
`{e_2, e_3}`. Leftover-of-`O` reverse would hold because leftover of `O`
at `A` and at `B` is `{e_1}`. Exist-opposite reverse of signed `M` holds.
Axis-cover reverse of the same four probes holds. Those leftovers are not
this display.

## Theorem 3 — face from 1-in 2-out axis split at `τ`

Face 1-in 2-out axis split holds if and only if split at `C` and split at
`D` both HOLD. Split at `C` HOLDs. Split at `D` FAILs because cover HOLDs
with `|Axis(M)|=2`: 2-in 1-out is fail. Face fails.

Face 1-in 2-out axis split at τ: fail

Displayed, not adopted. The bits are not written into Admissibility.
Do not write into Admissibility. Do not attach L1.

Leftover-axis face of #7167 fails because leftover is empty at `C` and at
`D`. Leftover-of-`M` face would fail because leftover of `M` at `C` is
`{e_1, e_2}` and leftover of `M` at `D` is `{e_1}`: nonempty and unequal.
Leftover of `O` at `C` is `{e_3}` and leftover of `O` at `D` is `{e_2, e_3}`:
nonempty and unequal. Exist-opposite face of signed `M` holds and
exist-opposite face of signed `O` holds. Axis-cover face of the same four
probes holds because cover HOLDs at `C` and at `D`. This display scores
1-in 2-out split of `Axis(M)` and `Axis(O)`, which fails at `D`, so face
fails.

## What this note does not claim

- It does not select a unique incoming, outgoing, or leftover lock.
- It does not reduce lock vectors to named signs `{+,−}`.
- It does not require split sides to be a singleton lock.
- It does not sum either set.
- It does not replace split by leftover of `M` alone.
- It does not replace split by leftover of `O` alone.
- It does not replace split by leftover-axis equality of nonempty leftovers.
- It does not replace split by existential opposite of signed locks.
- It does not replace split by axis-cover reverse/face of the same four probes.
- It does not replace `O` by `M`.
- It does not replace split by locks of six-neighbors.
- It does not use a six-neighbor star as the letter.
- It does not wait for a global later T.
- It does not attach a formation member from already-recorded six-neighbor
  locks.
- It does not reprint leftover-axis reverse of #7167.
- It does not reprint leftover of leftover-of-`M` alone.
- It does not reprint leftover of leftover-of-`O` alone.
- It does not reprint leftover of the two-site opposite-lock process.
- It does not reprint nszopinz exist-opposite of signed locks.
- It does not reprint mixed unique-letter `UNDEFINED` as this split.
- It does not reprint axis-cover reverse/face as this split reverse/face.
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
z-symmetric three-site process, 1-in 2-out axis split of `M` and `O` at
`t+1`, and the reverse/face bits from split are displayed theorem-domain data.

## Exact target and obligation graph

| Obligation | Status |
|---|---|
| current Lattice / Admissibility / Record premises | quoted; no edit |
| perp-step incoming-lock process on `B_3(0)` | displayed; z-symmetric three-site seed `+e_1/−e_1/−e_1` |
| ticks `t(A)`, `t(B)`, `t(C)`, `t(D)` | Theorem 1; `0`, `2`, `1`, `3` |
| `M` at `τ=t+1` | Theorem 1; frozen equal to `M` at `t` |
| `O` at `τ=t+1` | Theorem 1; HOLDING outgoing dual |
| `Axis(M)` and `Axis(O)` at `τ` | Theorem 1; complementary at each probe |
| `|Axis(M)|` at `τ` | Theorem 1; `1,1,1,2` |
| cover at `τ` | Theorem 1; hold at each probe |
| split at `τ` | Theorem 1; hold at `A,B,C`; fail at `D` (2-in 1-out) |
| reverse from split at `τ` | Theorem 2; `hold` |
| face from split at `τ` | Theorem 3; `fail` |
| unique lock | not required |
| occupancy of sites as the letter | not used |
| named-sign `{+,−}` letter | not used; lost the axis |
| singleton unique lock-vector letter | not used as the object; mixed remains a set |
| `Z^3` sum of the lock set | not used; no aggregation |
| six-neighbor star as the letter | not used |
| leftover-axis reverse of #7167 | not this split display |
| leftover of leftover-of-`M` alone | not this display |
| leftover of leftover-of-`O` alone | not this display |
| leftover of the two-site opposite-lock process | not this display |
| leftover of nszopinz exist-opposite of signed locks | not this display |
| leftover of axis-cover reverse/face | not this display |
| global later T | not used |
| 1-in 2-out axis split as Admissibility content | not adopted |
| formation site / probability / rate | open |
| physical Record readout of the bits | open |

## Value gate (V1–V5)

| # | Answer |
|---|---|
| V1 | It answers the first-display question: 1-in 2-out axis split of `M` and `O` at `t+1` on the four #7186 z-probes, and reverse/face from that split. |
| V2 | Current main has no landed 1-in 2-out reverse/face of timed `M` and `O` on these four #7186 z-probes. |
| V3 | Split bits at one cut and the two split reverse/face bits are independently finite and exact. |
| V4 | The theorem is more than a restatement of Record because it reads unsigned 1-in 2-out axis split of own incoming and own outgoing at the same `t+1` cut and scores reverse/face from split. |
| V5 | It is not an adopted content rule: the bits remain displayed. |

## No-go discipline gate

The negative content is narrow: the display does not write those bits into
Admissibility, does not reduce them to named signs, does not require a
unique lock, does not replace split by leftover of `M` alone or leftover of
`O` alone, does not replace split by leftover-axis reverse of #7167, does
not replace split by existential opposite of signed locks, does not replace
split by axis-cover reverse/face of the same four probes, and does not
identify this display with the two-site opposite-lock leftover-empty fail.
No global impossibility is claimed.

### N1 — materially distinct routes

| Route | Attempt | Why it fails here | Marker |
|---|---|---|---|
| leftover-axis reverse of #7167 | score nonempty leftover-axis equality | leftover empty at each probe, leftover reverse fail, leftover face fail; split reverse hold | ATTEMPTED |
| leftover of `M` alone | score `{e_1,e_2,e_3}` minus `Axis(M)` | leftover of `M` at `A` and `B` is `{e_2,e_3}`, nonempty equal; face of leftover of `M` fails | ATTEMPTED |
| leftover of `O` alone | score `{e_1,e_2,e_3}` minus `Axis(O)` | leftover of `O` at `A` and `B` is `{e_1}`, nonempty equal; face of leftover of `O` fails | ATTEMPTED |
| leftover of the two-site opposite-lock process | reuse two-site seed `{0,(0,0,1)}` | this seed also records `(0,0,−1)` at tick 0; process is z-symmetric three-site | ATTEMPTED |
| nszopinz exist-opposite | reuse signed reverse hold and face hold | those bits HOLD from signed opposite pairs; split is unsigned 1-in 2-out | ATTEMPTED |
| axis-cover reverse/face | reuse cover hold at each probe | cover HOLDs at `D` with `|Axis(M)|=2`; split FAILs there; cover face HOLD, split face FAIL | ATTEMPTED |
| unique letter | replace mixed sets by a singleton or `UNDEFINED` | mixed `M(D,τ)` and mixed `O(A,τ)` remain sets; split still holds at `A` and fails at `D` | ATTEMPTED |
| shared-axis leftover empty | both sides occupy all three axes | leftover empty, cover fails, split fails | ATTEMPTED |
| exist-opposite of signed locks | score `a+b=(0,0,0)` inside `M` or `O` | opposite signs on one axis HOLD exist-opposite and fail cover, hence fail split | ATTEMPTED |
| 2-in 1-out as HOLD | treat `|Axis(M)|=2` cover HOLD as split HOLD | 2-in 1-out is fail of this object | ATTEMPTED |
| same-tick-inclusive six-neighbor lock union | score locks of six-neighbors formed by `t(q)` | that leftover includes partner locks; split is unsigned 1-in 2-out of `M` and `O` | ATTEMPTED |
| sum of a set | replace split by a `Z^3` sum | the construction does not sum; split is 1-in 2-out unsigned axes | ATTEMPTED |
| named-sign lettering | collapse `{±e_i}` to `{+,−}` | named-sign lettering lost the axis | ATTEMPTED |
| global later T | wait until `max t(A,B,C,D)` before reading | `τ(q)=t(q)+1` is per-probe; no global T | ATTEMPTED |
| attach a formation member from already-recorded six-neighbor locks | form the probes by a neighbor-lock letter instead of perp-step | refused; not attached | ATTEMPTED |
| adopt bits into Admissibility | rewrite the local rule by 1-in 2-out split | refused; displayed, not adopted | ATTEMPTED |

### N2 — wall independence

Missing physical adoption, missing identification of split with leftover-axis
reverse of #7167, missing identification of split with leftover of `M` alone,
missing identification of split with axis-cover reverse/face, and missing
Record identification of split reverse are distinct open premises. This note
claims no complete wall collection.

### N3 — hidden-condition scan

The host `B_3(0)`, z-symmetric three-site seed locks `+e_1`, `−e_1`, and
`−e_1`, perpendicular step rule, incoming-step lock, own incoming set and
own outgoing dual from records with tick `<= τ`, per-probe `τ=t+1`,
unsigned axis, cover as empty intersection and three-axis union, split as
cover and `|Axis(M)|=1`, four z-probes with seed `A`, 2-in 1-out as fail,
and mixed remains a set are declared. No uniqueness of lock, no
six-neighbor lock union as the scored object, no leftover-axis equality as
the scored reverse, no axis-cover reverse/face as the scored reverse/face,
no global later T, no formation attachment from already-recorded
six-neighbor locks, and no Admissibility rewrite are silently assumed.

### N4 — source residual matching

The current axiom memo supplies cubic sites, `M_2(C)`,
content-conditional-on-formation, and unreadable absence. The residual that
formation site, probability, and rate remain unsupplied is unchanged. The
split reverse `hold` and face `fail` reports do not close that residual.

### N5 — resolution and rhetoric audit

| Resolution | Executed | Not claimed |
|---|---|---|
| per element | each unsigned lattice axis among `{e_1,e_2,e_3}` | no continuum alphabet |
| per site | `A,B,C,D` z-probes on `B_3(0)` only | no other cubic sites |
| per mode | no mode calculation | no spectral exhaustion |
| per block | four split bits, reverse/face from split | no adopted content law |
| lattice wide | checked and not executed | no lattice-wide lettering rule |

### N6 — live partial-closure paths

Live routes include a later Record content map for split reverse/face, a
formation-rate rule, and a physical selector among complementary axis
splits. None is taken here.

### N7 — hostile steelman

**Steelman:** Split HOLD is only leftover empty of #7167; reverse HOLD is
only nszopinz exist-opposite HOLD; leftover of `M` alone already gives a
third direction `{e_2,e_3}` at `A`; leftover of `O` alone already gives
`{e_1}`; the four z-probe `M` and `O` values match two-site opposite-lock
so the third seed is idle; cover HOLD at every probe already is the split;
and complementary occupation is only three-axis covering already implied by
leftover empty.

**Answer:** Leftover empty is unsigned union equal to `{e_1,e_2,e_3}`. Cover
also requires empty intersection. Split also requires `|Axis(M)|=1`. Cover
HOLDs at `D` with `|Axis(M)|=2` and `|Axis(O)|=1`; that 2-in 1-out FAILs
split. Leftover reverse of #7167 fails on empty leftover; split reverse
holds. Exist-opposite HOLD is signed opposite pairs and can HOLD on one
shared axis. Leftover of `M` alone and leftover of `O` alone are one-sided
leftovers; they are not 1-in 2-out of the union. The z-symmetric seed
records `(0,0,−1)` at tick 0; that is not the two-site opposite-lock
process even when the four z-probe timed sets coincide. Axis-cover reverse
and face HOLD on these probes; split face FAILs. Split reverse is HOLD of
split at `A` and at `B`, not leftover-axis equality, not exist-opposite of
signed locks, and not axis-cover reverse/face.

### N8 — cross-cycle echo

nszopinz #7186 reported reverse hold and face hold from same-tick union own
incoming lock. #7167 leftover-axis reported empty leftover, leftover reverse
fail, and leftover face fail on a two-site opposite seed. Axis-cover of `M`
and `O` at `t+1` on these four z-probes reported cover hold at each probe,
reverse hold, and face hold. This note is not those displays: it reports
1-in 2-out axis split of `M` and `O` at `τ=t+1` on the z-symmetric
three-site seed, split hold at `A,B,C`, split fail at `D` (2-in 1-out),
reverse hold, and face fail.

**Gate disposition:** PASS for the 1-in 2-out `t+1` reverse/face reports
above. FAIL / DO NOT SHIP for “the predicate equals the named sign,” “the
predicate equals the unique singleton lock vector,” “the predicate equals
six-neighbor lock union,” “the predicate equals leftover of `M` alone,”
“the predicate equals leftover of `O` alone,” “the predicate equals
leftover-axis reverse of #7167,” “the predicate equals nszopinz
exist-opposite HOLD,” “the predicate equals axis-cover reverse/face,”
“bits are Admissibility,” “split holds at `D`,” “2-in 1-out is HOLD,”
“reverse 1-in 2-out fails,” “face 1-in 2-out holds,” or “empty leftover is
this reverse.”

## Primary runner

The paired runner builds Euclidean `B_3(0)`, runs the z-symmetric three-site
perp-step incoming-lock process, reads each probe's own earliest incoming
set and own outgoing dual from the record prefix at that probe's `t+1`,
reports unsigned axis of each, reports cover of the union, reports
`|Axis(M)|` and 1-in 2-out split, lists new records in `B_3(0)` between `t`
and `t+1` that meet a probe's six-neighbors, and checks Theorems 1--3. It
also checks that cover holds at each probe, that split holds at `A,B,C` and
fails at `D`, that leftover empty fails leftover reverse while split reverse
holds, that leftover of `M` alone and leftover of `O` alone are different
objects, that mixed sets remain sets, that unique-letter split is
`UNDEFINED` at mixed `O(A)`, that shared-axis leftover empty fails split,
that 2-in 1-out fails split while cover holds, that the construction does
not sum, that a formation member from already-recorded six-neighbor locks
is not attached, and that the display is not the two-site opposite-lock
leftover process. No runner cache is written.
