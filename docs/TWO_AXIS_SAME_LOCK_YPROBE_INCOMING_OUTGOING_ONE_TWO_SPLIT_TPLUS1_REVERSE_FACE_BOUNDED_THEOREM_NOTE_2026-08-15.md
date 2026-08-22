---
claim_id: two_axis_same_lock_yprobe_incoming_outgoing_one_two_split_tplus1_reverse_face_bounded_theorem_note_2026-08-15
claim_type: bounded_theorem
claim_scope: "1-in 2-out axis split of M and O at t+1 on the four y-probes of the two-axis same-lock seed, and reverse/face from that, are reported. Displayed, not adopted."
upstream_dependencies:
  - minimal_axioms
runner: scripts/two_axis_same_lock_yprobe_incoming_outgoing_one_two_split_tplus1_reverse_face_2026_08_15.py
---

# Incoming And Outgoing 1-In 2-Out Axis Split At t+1 Reverse And Face On Four Y-Probes Of The Two-Axis Same-Lock Seed

> **Key terms used in this doc** are indexed A-Z at `docs/KEY_TERMINOLOGY.md`;
> each row points to the canonical source-of-truth doc.

**Date:** 2026-08-15
**Type:** bounded_theorem
**Scope:** 1-in 2-out axis split of simultaneous earliest incoming set `M`
and outgoing dual `O` at each probe's `τ=t+1`, and reverse/face from that
split, on the four y-probes of the two-axis same-lock seed in
`B_3(0)={n:n·n<=9}`. Same process and y-probes as nm2sl. Let `t(q)` be the
formation tick of probe `q`. Let `τ(q)=t(q)+1`. `M(q,τ)` is the set of
earliest incoming nearest-neighbor steps at `q` using only records with
tick `<= τ`. Seeds are a singleton seed letter. `O(q,τ)` is the outgoing
dual of `M`: the set of `e` in `{±e_1,±e_2,±e_3}` such that `q+e` is formed
and `e` is in `M(q+e,τ)`. Unformed at `τ` is `UNDEFINED`. Empty `O` is
empty, not `UNDEFINED`. Axis of a defined lock set `S` is `Axis(S)={e_i |
some ±e_i in S}`. Cover holds at `q` if and only if `Axis(M)` intersect
`Axis(O)` is empty and `Axis(M)` union `Axis(O)` equals `{e_1,e_2,e_3}`.
Split holds at `q` if and only if cover holds and `|Axis(M)|=1`. 2-in 1-out
is fail of this object, not `UNDEFINED`. Unformed at `τ` is `UNDEFINED`.
Else fail. Reverse holds if and only if split holds at `A` and at `B`. Face
holds if and only if split holds at `C` and at `D`. Either side
`UNDEFINED` is `UNDEFINED`. Discriminator versus the two-axis opposite
seed: seed letters at `(0,1,0)` and `(0,1,1)` are same-lock, not opposite.
This is not leftover of cover reverse. This is not leftover-axis reverse.
This is not leftover of leftover-of-`M` alone. This is not leftover of
leftover-of-`O` alone. This is not leftover of the two-axis opposite seed.
This is not leftover of one-axis same-lock `+e_1/+e_1`. This is not leftover
of nsopp `+e_1/−e_1`. This is not leftover of nnseed `+e_1/+e_2`.
Uniqueness of incoming or outgoing locks is not required. Mixed remains a
set. Occupancy of sites is not used. Named-sign lettering is not used. The
construction does not use a six-neighbor star. A is a seed. Displayed, not
adopted. Do not write into Admissibility. Do not attach L1. This note does
not write the 1-in 2-out split into Admissibility and does not attach a
formation member from already-recorded six-neighbor locks. This display
does not use occupancy. Mixed stays a set.
**Audit-status authority:** independent audit lane only. This note authors no
audit verdict and predicts none.
**Primary runner:**
[`scripts/two_axis_same_lock_yprobe_incoming_outgoing_one_two_split_tplus1_reverse_face_2026_08_15.py`](../scripts/two_axis_same_lock_yprobe_incoming_outgoing_one_two_split_tplus1_reverse_face_2026_08_15.py)

Framework input:

- [`MINIMAL_AXIOMS_2026-06-29.md`](MINIMAL_AXIOMS_2026-06-29.md) supplies
  cubic-lattice sites `Z^3` with nearest-neighbor adjacency, the one-site
  algebra `M_2(C)`, and the Record sentences that records form and that a
  present record locks exactly one admissible local possibility.

Everything after that quoted input is a finite displayed process on `B_3(0)`
and the four named y-probes. Incoming lock letters are unit nearest-neighbor
steps. `O` is the outgoing dual of those incoming sets at the per-probe cut
`τ=t+1`. Axis is the unsigned lattice direction of a signed lock. Cover is
complementary occupation of `{e_1,e_2,e_3}` by `Axis(M)` and `Axis(O)`.
Split is cover together with `|Axis(M)|=1`, so `|Axis(O)|=2`. Reverse and
face are scored on split at the paired probes. 2-in 1-out is fail. Named
signs `{+,−}` are a coarser readout and are not used. A singleton unique
lock letter is a different readout and is not used as the object.
Existential opposite of signed locks is a different readout and is not used
as the split reverse: exist-opposite of signed M fails reverse here, while
split reverse holds. Cover reverse holds here while leftover reverse fails.
On this member `|Axis(M)|=1` at each of the four y-probes, so split equals
cover at each probe; D fails cover by missing `e_2`, not by 2-in 1-out. A
`Z^3` sum of those locks is a different readout and is not used. Occupancy
of sites is not used. A six-neighbor star is not the letter.

## Machine status and trace

```yaml
actual_current_surface_status: bounded-support
target_claim_type: bounded_theorem
claim_type_reason: "Exact report of 1-in 2-out axis split of M and O at t+1 on the four y-probes of the two-axis same-lock seed, cover hold at A,B,C and cover fail at D from missing e_2, split hold at A,B,C and split fail at D, reverse hold and face fail from split; uniqueness of locks is not claimed and the bits are not adopted."
trace_class: frontier_discovery
target_claim_id: two_axis_same_lock_yprobe_incoming_outgoing_one_two_split_tplus1_reverse_face
target_blocker_text: "display 1-in 2-out axis split of M and O at t+1 on the four y-probes of the two-axis same-lock seed, and reverse/face from that split, discriminator versus two-axis opposite"
source_of_blocker_text: handoff
reachability_to_target: advances
artifact_role: theorem
next_trace_action: "Keep 1-in 2-out axis split of M and O at t+1 displayed; do not write split into Admissibility, do not reduce to cover reverse, do not reduce to leftover-axis reverse, do not reduce to leftover of M alone or leftover of O alone, do not replace split by existential opposite of signed locks, do not identify the display with the two-axis opposite seed, and do not attach L1."
conditional_surface_status: "exact on B_3(0) for 1-in 2-out axis split of M and O at t+1 on the four y-probes of the two-axis same-lock seed and reverse/face from that split; displayed, not adopted"
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

No larger host is used. The four y-probes are the only sites whose 1-in
2-out axis split of `M` and `O` is scored:

```text
A = (0,1,0),  B = (1,1,1),  C = (0,2,0),  D = (1,1,0).
```

These are not the x-probes `A=(1,0,0)`, `B=(1,1,1)`, `C=(2,0,0)`,
`D=(1,1,0)`. These are not the z-probes `A=(0,0,1)`, `B=(1,1,1)`,
`C=(0,0,2)`, `D=(1,0,1)`. A is a seed. Same process and y-probes as nm2sl.

Lock alphabet of the displayed process: `{±e_i}` with `i` in `{1,2,3}`.

Seed: the four-record set `{0, (0,1,0), (0,0,1), (0,1,1)}` is recorded at
formation tick 0 with two disjoint same-lock pairs `L(0)=+e_1`,
`L(0,1,0)=+e_1`, `L(0,0,1)=+e_2`, and `L(0,1,1)=+e_2`. This seed is not the
two-axis opposite seed `{0,(0,1,0),(0,0,1),(0,1,1)}` with locks
`+e_1/−e_1` and `+e_2/−e_2`. This seed is not the one-axis same-lock
two-site seed `{0,(0,1,0)}` with locks `+e_1/+e_1`. This seed is not the
nnseed two-site seed `+e_1/+e_2`. This seed is not the opposite two-site
seed `+e_1/−e_1`.

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

Split of `M` and `O` at the same cut:

```text
split(q) HOLD iff cover(q) HOLD and |Axis(M(q,τ))|=1.
```

If `q` is unformed at `τ`, then cover and split are `UNDEFINED`. Else fail.
2-in 1-out is fail of this object, not `UNDEFINED`: cover can HOLD with
`|Axis(M)|=2` and `|Axis(O)|=1`, and that is split fail. Axis is unsigned:
`+e_i` and `−e_i` occupy the same axis. Cover is complementary occupation
of the three lattice axes. Leftover of the union `{e_1,e_2,e_3}` minus
`(Axis(M) union Axis(O))` empty is weaker: two sides that both occupy all
three axes have empty leftover and fail cover because the intersection is
nonempty. Leftover of `M` alone is a different object. Leftover of `O`
alone is a different object. Cover without the `|Axis(M)|=1` cut is a
different object.

Reverse 1-in 2-out holds if and only if split at `A` and split at `B` both
HOLD. Face 1-in 2-out holds if and only if split at `C` and split at `D`
both HOLD. Either side `UNDEFINED` is `UNDEFINED`. Else fail.

Identifying a named sign of those locks with reverse or face is refused:
named-sign lettering lost the axis. Identifying leftover-axis reverse with
this reverse is refused: leftover reverse fails when leftover is empty at
`A` and at `B`. Identifying cover reverse with this reverse is refused:
cover without `|Axis(M)|=1` is a different object, even when the two bits
coincide on this member. Identifying existential opposite of signed locks
with split reverse is refused: exist-opposite of signed M fails reverse
here.

## Theorem 1 — ticks, `M`, `O`, `Axis`, cover, `|Axis(M)|`, and split at `τ=t+1`

On this process the four y-probes form. Compare to one-axis same-lock
cover-HOLD: that two-site seed `{0,(0,1,0)}` both locking `+e_1` has
`t(B)=2`, `t(D)=3`, cover hold at each of the four y-probes, and split fail
at `D` from 2-in 1-out. This four-site two-axis same-lock seed has earlier
`B` and `D`, cover fail at `D` from missing `e_2`, and `|Axis(M)|=1` at
`D`. Discriminator versus two-axis opposite: that seed locks `−e_1` at
`(0,1,0)` and `−e_2` at `(0,1,1)`; timed `M(A)` there is `{−e_1}` and
`O(D)` there is `{+e_1, −e_1}`. This display reads the 1-in 2-out axis
split of timed `M` and `O` on the same-lock four-site seed:

```text
t(A)=0
t(B)=1
t(C)=1
t(D)=2
M(A, τ) = {+e_1}
M(B, τ) = {+e_1}
M(C, τ) = {+e_2}
M(D, τ) = {−e_3}
O(A, τ) = {+e_2, −e_3}
O(B, τ) = {+e_2, +e_3, −e_3}
O(C, τ) = {+e_1, −e_1, +e_3, −e_3}
O(D, τ) = {+e_1}
Axis(M)(A, τ) = {e_1}
Axis(O)(A, τ) = {e_2, e_3}
Axis(M)(B, τ) = {e_1}
Axis(O)(B, τ) = {e_2, e_3}
Axis(M)(C, τ) = {e_2}
Axis(O)(C, τ) = {e_1, e_3}
Axis(M)(D, τ) = {e_3}
Axis(O)(D, τ) = {e_1}
cover(A) = hold
cover(B) = hold
cover(C) = hold
cover(D) = fail
|Axis(M)|(A, τ) = 1
|Axis(M)|(B, τ) = 1
|Axis(M)|(C, τ) = 1
|Axis(M)|(D, τ) = 1
split(A) = hold
split(B) = hold
split(C) = hold
split(D) = fail
```

A is a seed at tick 0. Mixed remains a set: `O(A,τ)` has two outgoing
steps, `O(B,τ)` has three, and `O(C,τ)` has four. Unique letters would
assign `UNDEFINED` at mixed `O(A)`. Here uniqueness is not required.
At `A`, `B`, and `C`, `Axis(M)` and `Axis(O)` are complementary: their
union is `{e_1,e_2,e_3}` and their intersection is empty, and
`|Axis(M)|=1`, so cover holds and split holds. At `D`, `|Axis(M)|=1` and
`Axis(O)={e_1}`, so the union is `{e_1,e_3}` and leftover of the union is
`{e_2}`. Cover fails at `D` from missing `e_2`. Split fails at `D` because
cover fails. That fail is not 2-in 1-out: `|Axis(M)|=1` at `D`. O is not
M. `M` at `τ` is frozen equal to `M` at `t`. `O` at `t` is empty at each of
the four y-probes, so cover at `t` fails and split at `t` fails; new
records at `t+1` fill `O` and cover holds at `A`, `B`, and `C`, while cover
still fails at `D`.

New records in `B_3(0)` between `t` and `t+1` that meet a probe's
six-neighbors enter `O` and do not enter earliest `M`:

```text
new 6-NN of A at t(A)+1: (0, 2, 0), (0, 1, -1)
new 6-NN of B at t(B)+1: (1, 2, 1), (1, 1, 2), (1, 1, 0)
new 6-NN of C at t(C)+1: (1, 2, 0), (-1, 2, 0), (0, 2, 1), (0, 2, -1)
new 6-NN of D at t(D)+1: (2, 1, 0)
```

The seed site `(0,1,1)` is a six-neighbor of `A` already recorded at tick
0, so it is not a new record at `t(A)+1`.

## Theorem 2 — reverse from 1-in 2-out at `τ`

Reverse 1-in 2-out holds if and only if split at `A` and split at `B` both
HOLD. Split holds at `A` and at `B`: each is 1-in 2-out. Reverse holds.
Cover reverse holds. Leftover reverse fails because leftover is empty at
`A` and at `B`. Exist-opposite of signed M fails reverse.

Reverse 1-in 2-out at τ: hold

Both sides are defined, so this is not `UNDEFINED`. Leftover-axis reverse
fails because leftover is empty at `A` and at `B`. Leftover-of-`M`
reverse would hold because leftover of `M` at `A` and at `B` is
`{e_2, e_3}`. Leftover-of-`O` reverse would hold because leftover of `O`
at `A` and at `B` is `{e_1}`. Exist-opposite of signed M fails reverse:
`{+e_1}` against `{+e_1}` has no pair summing to zero. On the two-axis
opposite seed, exist-opposite of signed M holds reverse from `{−e_1}`
against `{+e_1}`. Cover reverse holds from cover at `A` and at `B`. Those
leftovers are not this display. Reverse holds.

## Theorem 3 — face from 1-in 2-out at `τ`

Face 1-in 2-out holds if and only if split at `C` and split at `D` both
HOLD. Split holds at `C`. Split fails at `D` because cover fails from
missing `e_2`. Face fails.

Face 1-in 2-out at τ: fail

Displayed, not adopted. The bits are not written into Admissibility.
Do not write into Admissibility. Do not attach L1.

Leftover-axis face fails because leftover is empty at `C` while leftover
at `D` is `{e_2}`. Leftover-of-`M` face would fail because leftover of `M`
at `C` is `{e_1, e_3}` and leftover of `M` at `D` is `{e_1, e_2}`. Leftover
of `O` at `C` is `{e_2}` and leftover of `O` at `D` is `{e_2, e_3}`:
leftover-of-`O` face would fail. Exist-opposite of signed M fails face:
`{+e_2}` against `{−e_3}` has no opposite pair. Exist-opposite of signed
`O` holds face. Cover face fails from cover fail at `D`. On one-axis
same-lock, cover face holds while split face fails from 2-in 1-out at `D`.
This display scores 1-in 2-out of `Axis(M)` and `Axis(O)`, which fails at
`D` from missing `e_2`, so face fails.

## What this note does not claim

- It does not select a unique incoming, outgoing, or leftover lock.
- It does not reduce lock vectors to named signs `{+,−}`.
- It does not require `M` or `O` to be a singleton of signed letters.
- It does not sum either set.
- It does not replace split by cover reverse.
- It does not replace split by leftover of `M` alone.
- It does not replace split by leftover of `O` alone.
- It does not replace split by leftover-axis equality of nonempty leftovers.
- It does not replace split by existential opposite of signed locks.
- It does not replace `O` by `M`.
- It does not replace split by locks of six-neighbors.
- It does not use a six-neighbor star as the letter.
- It does not wait for a global later T.
- It does not attach a formation member from already-recorded six-neighbor
  locks.
- It does not reprint leftover of cover reverse.
- It does not reprint leftover-axis reverse.
- It does not reprint leftover of leftover-of-`M` alone.
- It does not reprint leftover of leftover-of-`O` alone.
- It does not reprint leftover of the two-axis opposite process.
- It does not reprint leftover of one-axis same-lock cover-HOLD.
- It does not reprint leftover of nsopp `+e_1/−e_1`.
- It does not reprint leftover of nnseed `+e_1/+e_2`.
- It does not reprint mixed unique-letter `UNDEFINED` as this split.
- It does not treat 2-in 1-out as `UNDEFINED`.
- It does not treat missing-axis cover fail as 2-in 1-out.
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
two-axis same-lock process, 1-in 2-out axis split of `M` and `O` at
`t+1`, and the reverse/face bits from that split are displayed theorem-domain
data.

## Exact target and obligation graph

| Obligation | Status |
|---|---|
| current Lattice / Admissibility / Record premises | quoted; no edit |
| perp-step incoming-lock process on `B_3(0)` | displayed; two-axis same-lock four-site seed `+e_1/+e_1` and `+e_2/+e_2` |
| ticks `t(A)`, `t(B)`, `t(C)`, `t(D)` | Theorem 1; `0`, `1`, `1`, `2` |
| `M` at `τ=t+1` | Theorem 1; frozen equal to `M` at `t` |
| `O` at `τ=t+1` | Theorem 1; HOLDING outgoing dual at `A,B,C`; singleton at `D` |
| `Axis(M)` and `Axis(O)` at `τ` | Theorem 1; complementary at `A,B,C`; missing `e_2` at `D` |
| cover at `τ` | Theorem 1; hold at `A,B,C`; fail at `D` from missing `e_2` |
| `|Axis(M)|` at `τ` | Theorem 1; `1`, `1`, `1`, `1` |
| split at `τ` | Theorem 1; hold at `A,B,C`; fail at `D` from cover fail, not 2-in 1-out |
| reverse from split at `τ` | Theorem 2; `hold` |
| face from split at `τ` | Theorem 3; `fail` |
| unique lock | not required |
| occupancy of sites as the letter | not used |
| named-sign `{+,−}` letter | not used; lost the axis |
| singleton unique lock-vector letter | not used as the object; mixed remains a set |
| `Z^3` sum of the lock set | not used; no aggregation |
| six-neighbor star as the letter | not used |
| leftover of cover reverse | not this split display |
| leftover-axis reverse | not this split display |
| leftover of leftover-of-`M` alone | not this display |
| leftover of leftover-of-`O` alone | not this display |
| leftover of two-axis opposite y-probes | not this display |
| leftover of one-axis same-lock cover-HOLD | not this display |
| leftover of nsopp exist-opposite | not this display |
| global later T | not used |
| 1-in 2-out split as Admissibility content | not adopted |
| formation site / probability / rate | open |
| physical Record readout of the bits | open |

## Value gate (V1–V5)

| # | Answer |
|---|---|
| V1 | It answers the first-display question: 1-in 2-out axis split of `M` and `O` at `t+1` on the four y-probes of the two-axis same-lock seed, and reverse/face from that split, discriminator versus two-axis opposite. |
| V2 | Current main has no landed 1-in 2-out reverse/face of timed `M` and `O` on these four y-probes of the two-axis same-lock seed. |
| V3 | Split bits at one cut and the two split reverse/face bits are independently finite and exact. |
| V4 | The theorem is more than a restatement of Record because it reads unsigned 1-in 2-out of own incoming and own outgoing at the same `t+1` cut and scores reverse/face from that split, not from opposite seed letters. |
| V5 | It is not an adopted content rule: the bits remain displayed. |

## No-go discipline gate

The negative content is narrow: the display does not write those bits into
Admissibility, does not reduce them to named signs, does not require a
unique lock, does not replace split by cover reverse, does not replace
split by leftover of `M` alone or leftover of `O` alone, does not replace
split by leftover-axis reverse, does not replace split by existential
opposite of signed locks, and does not identify this display with the
two-axis opposite seed. No global impossibility is claimed.

### N1 — materially distinct routes

| Route | Attempt | Why it fails here | Marker |
|---|---|---|---|
| leftover of cover reverse | score reverse/face as cover at `A,B` and `C,D` | on this member cover equals split at each y-probe because `|Axis(M)|=1`; one-axis same-lock has cover face hold and split face fail from 2-in 1-out at `D` | ATTEMPTED |
| leftover-axis reverse | score nonempty leftover-axis equality | leftover empty at `A` and at `B`, leftover reverse fail, while split reverse hold | ATTEMPTED |
| leftover of `M` alone | score `{e_1,e_2,e_3}` minus `Axis(M)` | leftover of `M` at `A` and at `B` is `{e_2,e_3}`, nonempty equal; reverse of leftover of `M` holds, which is not a discriminator of this split | ATTEMPTED |
| leftover of `O` alone | score `{e_1,e_2,e_3}` minus `Axis(O)` | leftover of `O` at `A` and at `B` is `{e_1}`, nonempty equal; reverse of leftover of `O` holds | ATTEMPTED |
| leftover of two-axis opposite | reuse seed `{0,(0,1,0),(0,0,1),(0,1,1)}` with locks `+e_1/−e_1` and `+e_2/−e_2` | this seed locks `+e_1/+e_1` and `+e_2/+e_2`; `M(A,τ)` is `{+e_1}` here and `{−e_1}` there; `O(D,τ)` is `{+e_1}` here and `{+e_1, −e_1}` there; exist-opposite of signed M reverse fails here and holds there | ATTEMPTED |
| leftover of one-axis same-lock | reuse seed `{0,(0,1,0)}` with locks `+e_1/+e_1` | `t(B)=2` and `t(D)=3` there versus `1` and `2` here; cover holds at `D` there as 2-in 1-out; cover fails at `D` here from missing `e_2` | ATTEMPTED |
| leftover of nsopp `+e_1/−e_1` | reuse opposite two-site seed | two-site seed; cover at `D` holds as 2-in 1-out; this seed has four sites | ATTEMPTED |
| leftover of nnseed `+e_1/+e_2` | reuse nnseed two-site seed | cover at `B` fails so reverse fails from cover fail; cover at `C` holds while split at `C` fails | ATTEMPTED |
| leftover of x-probes on this seed | reuse `A=(1,0,0)` | x-probe `A` forms at tick 2 with cover fail; y-probe `A` is a seed with split hold | ATTEMPTED |
| leftover of z-probes on this seed | reuse `A=(0,0,1)` | z-probe `A` is the `+e_2` seed, a different frame | ATTEMPTED |
| unique letter | replace mixed sets by a singleton or `UNDEFINED` | mixed `O(A,τ)` remains a set; unique-letter split at `A` is `UNDEFINED`; this split is hold, not `UNDEFINED` | ATTEMPTED |
| shared-axis leftover empty | both sides occupy all three axes | leftover empty, cover fails, split fails; here cover holds at `A,B,C` | ATTEMPTED |
| exist-opposite of signed locks | score `a+b=(0,0,0)` inside `M` or `O` | exist-opposite of signed M fails reverse; split reverse holds from 1-in 2-out at `A` and at `B` | ATTEMPTED |
| same-tick-inclusive six-neighbor lock union | score locks of six-neighbors formed by `t(q)` | that leftover includes partner locks; split is unsigned 1-in 2-out of `M` and `O` | ATTEMPTED |
| sum of a set | replace split by a `Z^3` sum | the construction does not sum; `O(A,τ)` sums to `+e_2−e_3` while `Axis(O)(A)` is `{e_2,e_3}` | ATTEMPTED |
| named-sign lettering | collapse `{±e_i}` to `{+,−}` | named-sign lettering lost the axis | ATTEMPTED |
| global later T | wait until `max t(A,B,C,D)` before reading | `τ(q)=t(q)+1` is per-probe; no global T | ATTEMPTED |
| attach a formation member from already-recorded six-neighbor locks | form the probes by a neighbor-lock letter instead of perp-step | refused; not attached | ATTEMPTED |
| adopt bits into Admissibility | rewrite the local rule by 1-in 2-out | refused; displayed, not adopted | ATTEMPTED |

### N2 — wall independence

Missing physical adoption, missing identification of split with cover reverse,
missing identification of split with leftover-axis reverse, missing
identification of split with leftover of `M` alone, missing identification
of split with exist-opposite of signed `M`, missing identification with the
two-axis opposite seed, and missing Record identification of split reverse
are distinct open premises. This note claims no complete wall collection.

### N3 — hidden-condition scan

The host `B_3(0)`, two-axis same-lock four-site seed locks `+e_1`, `+e_1`,
`+e_2`, and `+e_2`, perpendicular step rule, incoming-step lock, own
incoming set and own outgoing dual from records with tick `<= τ`,
per-probe `τ=t+1`, unsigned axis, cover as empty intersection and
three-axis union, split as cover together with `|Axis(M)|=1`, 2-in 1-out as
fail, four y-probes with `A` a seed, and mixed remains a set are declared.
No uniqueness of lock, no six-neighbor lock union as the scored object, no
leftover-axis equality as the scored reverse, no cover reverse as the
scored reverse, no global later T, no formation attachment from
already-recorded six-neighbor locks, and no Admissibility rewrite are
silently assumed.

### N4 — source residual matching

The current axiom memo supplies cubic sites, `M_2(C)`,
content-conditional-on-formation, and unreadable absence. The residual that
formation site, probability, and rate remain unsupplied is unchanged. The
split reverse `hold` and face `fail` reports do not close that residual.

### N5 — resolution and rhetoric audit

| Resolution | Executed | Not claimed |
|---|---|---|
| per element | each unsigned lattice axis among `{e_1,e_2,e_3}` | no continuum alphabet |
| per site | `A,B,C,D` y-probes on `B_3(0)` only | no other cubic sites |
| per mode | no mode calculation | no spectral exhaustion |
| per block | four split bits, reverse/face from 1-in 2-out | no adopted content law |
| lattice wide | checked and not executed | no lattice-wide lettering rule |

### N6 — live partial-closure paths

Live routes include a later Record content map for 1-in 2-out reverse/face, a
formation-rate rule, and a physical selector among complementary axis
splits. None is taken here.

### N7 — hostile steelman

**Steelman:** Split HOLD is only cover HOLD; reverse HOLD is only leftover
of `M` alone or only two-axis opposite; face FAIL is only leftover empty
or only exist-opposite of signed `M`; one-axis same-lock already gives
reverse hold and face fail; and missing `e_2` at `D` is only 2-in 1-out.

**Answer:** Cover holds at `A`, `B`, and `C` and fails at `D` from missing
`e_2`. Split requires cover and `|Axis(M)|=1`. At each of the four
y-probes `|Axis(M)|=1`, so split equals cover on this member. That
coincidence is not identity of the objects: one-axis same-lock has cover
hold at `D` with `|Axis(M)|=2`, which is 2-in 1-out, so cover face holds
and split face fails. Here `D` is 1-in 1-out with leftover `{e_2}`, so
cover fails and split fails. 2-in 1-out is fail of this object, not
`UNDEFINED`. Unique-letter split at mixed `O(A)` is `UNDEFINED`; this
split is hold. Leftover reverse fails on empty leftover at `A` and at `B`.
Exist-opposite of signed M fails reverse here and holds on two-axis
opposite. Two-axis opposite locks `−e_1` at seed `A`; this seed locks
`+e_1`. Split reverse is HOLD of split at `A` and at `B`, not exist-opposite
of signed locks and not leftover of `M` alone.

### N8 — cross-cycle echo

One-axis same-lock on these y-probes has cover hold at each probe and split
fail at `D` from 2-in 1-out. Two-axis opposite on these y-probes has the
same split reverse hold and face fail pattern, with `M(A)={−e_1}` and
exist-opposite of signed M reverse hold. Leftover-axis reverse fails
because leftover is empty at `A` and at `B`. This note is not those
displays: it reports 1-in 2-out axis split of `M` and `O` at `τ=t+1` on
the two-axis same-lock seed, split hold at `A,B,C`, split fail at `D` from
missing `e_2`, reverse hold, and face fail.

**Gate disposition:** PASS for the 1-in 2-out `t+1` reverse/face reports
above. FAIL / DO NOT SHIP for “the predicate equals the named sign,” “the
predicate equals the unique singleton lock vector,” “the predicate equals
six-neighbor lock union,” “the predicate equals leftover of `M` alone,”
“the predicate equals leftover of `O` alone,” “the predicate equals
leftover-axis reverse,” “the predicate equals cover reverse,” “the
predicate equals two-axis opposite,” “the predicate equals exist-opposite
of signed M,” “bits are Admissibility,” “2-in 1-out is `UNDEFINED`,”
“split fails at `A`,” “reverse 1-in 2-out fails,” “face 1-in 2-out holds,”
“cover holds at `D`,” or “empty leftover is this reverse.”

## Primary runner

The paired runner builds Euclidean `B_3(0)`, runs the two-axis same-lock
four-site perp-step incoming-lock process, reads each probe's own earliest
incoming set and own outgoing dual from the record prefix at that probe's
`t+1`, reports unsigned axis of each, reports cover, reports `|Axis(M)|`,
reports 1-in 2-out split, lists new records in `B_3(0)` between `t` and
`t+1` that meet a probe's six-neighbors, and checks Theorems 1--3. It also
checks that cover holds at `A,B,C` and fails at `D` from missing `e_2`,
that split holds at `A,B,C` and fails at `D`, that leftover empty fails
leftover reverse while split reverse holds, that leftover of `M` alone and
leftover of `O` alone are different objects, that exist-opposite of signed
M fails reverse, that mixed sets remain sets, that unique-letter split is
`UNDEFINED` at mixed `O(A)` while this split is hold, that shared-axis
leftover empty fails cover, that the construction does not sum, that a
formation member from already-recorded six-neighbor locks is not attached,
and that the display is not the two-axis opposite leftover process.
No runner cache is written.
