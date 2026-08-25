---
claim_id: two_axis_opposite_xprobe_incoming_outgoing_one_two_split_tplus1_reverse_face_bounded_theorem_note_2026-08-15
claim_type: bounded_theorem
claim_scope: "1-in 2-out axis split of M and O at t+1 on the four x-probes of the two-axis opposite seed, and reverse/face from that, are reported. Displayed, not adopted."
upstream_dependencies:
  - minimal_axioms
runner: scripts/two_axis_opposite_xprobe_incoming_outgoing_one_two_split_tplus1_reverse_face_2026_08_15.py
---

# Incoming And Outgoing 1-In 2-Out Axis Split At t+1 Reverse And Face On Four Two-Axis Opposite X-Probes

> **Key terms used in this doc** are indexed A-Z at `docs/KEY_TERMINOLOGY.md`;
> each row points to the canonical source-of-truth doc.

**Date:** 2026-08-15
**Type:** bounded_theorem
**Scope:** 1-in 2-out axis split of simultaneous earliest incoming set `M`
and outgoing dual `O` at each probe's `τ=t+1`, and reverse/face from that
split, on the four x-probes of the two-axis opposite seed in
`B_3(0)={n:n·n<=9}`. Same process and x-probes as nm2axx. Let `t(q)` be the
formation tick of probe `q`. Let `τ(q)=t(q)+1`. `M(q,τ)` is the set of
earliest incoming nearest-neighbor steps at `q` using only records with
tick `<= τ`. Seeds are a singleton seed letter. `O(q,τ)` is the outgoing
dual of `M`: the set of `e` in `{±e_1,±e_2,±e_3}` such that `q+e` is formed
and `e` is in `M(q+e,τ)`. Unformed at `τ` is `UNDEFINED`. Empty `O` is
empty, not `UNDEFINED`. Axis of a defined lock set `S` is `Axis(S)={e_i |
some ±e_i in S}`. Cover holds at `q` if and only if `Axis(M)` intersect
`Axis(O)` is empty and `Axis(M)` union `Axis(O)` equals `{e_1,e_2,e_3}`.
Split holds at `q` if and only if cover holds and `|Axis(M)|=1`. Unformed
at `τ` is `UNDEFINED`. Else fail. Reverse holds if and only if split holds
at `A` and at `B`. Face holds if and only if split holds at `C` and at `D`.
Either side `UNDEFINED` is `UNDEFINED`. Cover fails on these x-probes at
`A` and at `D` because leftover axis `{e_2}` is missing. `|Axis(M)|=1` at
each of the four x-probes, so split equals cover on this member. This is
not leftover of y-probe 1-in 2-out on this seed. This is not leftover of
1-axis x-probe cover. This is not leftover-axis reverse. This is not leftover of leftover-axis reverse. This
is not leftover of leftover-of-`M` alone. This is not leftover of
leftover-of-`O` alone. This is not leftover of same-lock two-axis. This is
not leftover of nsopp one-axis two-site seed. Uniqueness of incoming or
outgoing locks is not required. Mixed remains a set. Occupancy of sites is
not used. Named-sign lettering is not used. The construction does not use a
six-neighbor star. A is not a seed. Displayed, not adopted. Do not write
into Admissibility. Do not attach L1. This note does not write the 1-in
2-out split into Admissibility and does not attach a formation member from
already-recorded six-neighbor locks. This display does not use occupancy.
Mixed stays a set.
**Audit-status authority:** independent audit lane only. This note authors no
audit verdict and predicts none.
**Primary runner:**
[`scripts/two_axis_opposite_xprobe_incoming_outgoing_one_two_split_tplus1_reverse_face_2026_08_15.py`](../scripts/two_axis_opposite_xprobe_incoming_outgoing_one_two_split_tplus1_reverse_face_2026_08_15.py)

Framework input:

- [`MINIMAL_AXIOMS_2026-06-29.md`](MINIMAL_AXIOMS_2026-06-29.md) supplies
  cubic-lattice sites `Z^3` with nearest-neighbor adjacency, the one-site
  algebra `M_2(C)`, and the Record sentences that records form and that a
  present record locks exactly one admissible local possibility.

Everything after that quoted input is a finite displayed process on `B_3(0)`
and the four named x-probes. Incoming lock letters are unit nearest-neighbor
steps. `O` is the outgoing dual of those incoming sets at the per-probe cut
`τ=t+1`. Axis is the unsigned lattice direction of a signed lock. Cover is
complementary occupation of `{e_1,e_2,e_3}` by `Axis(M)` and `Axis(O)`.
Split is cover together with `|Axis(M)|=1`, so `|Axis(O)|=2` when split
holds. Reverse and face are scored on split at the paired probes. Named
signs `{+,−}` are a coarser readout and are not used. A singleton unique
lock letter is a different readout and is not used as the object: mixed
`O` remains a set. Existential opposite of signed locks is a different
readout and is not used as the split reverse: exist-opposite of signed M
fails reverse and face on these x-probes. Cover reverse fails here and
split reverse fails here because `|Axis(M)|=1` at each probe, so the extra
split cut does not change the reverse bit on this member. Cover reverse on
the 1-axis nsopp x-probes holds while split reverse there fails from 2-in
1-out; that is a different process. Y-probe 1-in 2-out reverse holds on
this same seed. Leftover-axis equality of nonempty leftovers is a different
readout. A `Z^3` sum of those locks is a different readout and is not used.
Occupancy of sites is not used. A six-neighbor star is not the letter.

## Machine status and trace

```yaml
actual_current_surface_status: bounded-support
target_claim_type: bounded_theorem
claim_type_reason: "Exact report of 1-in 2-out axis split of M and O at t+1 on the four x-probes of the two-axis opposite seed, cover fail at A and D from leftover e_2, |Axis(M)|=1 at each probe so split equals cover, reverse fail and face fail from that split; uniqueness of locks is not claimed and the bits are not adopted."
trace_class: frontier_discovery
target_claim_id: two_axis_opposite_xprobe_incoming_outgoing_one_two_split_tplus1_reverse_face
target_blocker_text: "display 1-in 2-out axis split of M and O at t+1 on the four two-axis opposite x-probes, and reverse/face from that split, where nm2axx cover FAILs"
source_of_blocker_text: handoff
reachability_to_target: advances
artifact_role: theorem
next_trace_action: "Keep 1-in 2-out axis split of M and O at t+1 displayed; do not write split into Admissibility, do not reduce to y-probe 1-in 2-out, do not reduce to 1-axis x-probe cover, do not reduce to leftover-axis reverse, do not reduce to leftover of M alone or leftover of O alone, do not replace split by existential opposite of signed locks, and do not attach L1."
conditional_surface_status: "exact on B_3(0) for 1-in 2-out axis split of M and O at t+1 on the four x-probes of the two-axis opposite seed and reverse/face from that split; displayed, not adopted"
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

No larger host is used. The four x-probes are the only sites whose 1-in
2-out axis split of `M` and `O` is scored:

```text
A = (1,0,0),  B = (1,1,1),  C = (2,0,0),  D = (1,1,0).
```

These are not the y-probes `A=(0,1,0)`, `B=(1,1,1)`, `C=(0,2,0)`,
`D=(1,1,0)`. These are not the z-probes `A=(0,0,1)`, `B=(1,1,1)`,
`C=(0,0,2)`, `D=(1,0,1)`. A is not a seed. Same process and x-probes as
nm2axx.

Lock alphabet of the displayed process: `{±e_i}` with `i` in `{1,2,3}`.

Seed: two disjoint opposite pairs recorded at formation tick 0. Origin
locks `+e_1` and `(0,1,0)` locks `−e_1`. The second pair is a new seed, not
a formed child: `(0,0,1)` locks `+e_2` and `(0,1,1)` locks `−e_2`. Four
sites form at tick 0. This seed is not the nsopp one-axis two-site seed
`{0,(0,1,0)}` with locks `+e_1/−e_1`. This seed is not the same-lock
two-axis seed with `+e_1/+e_1` and `+e_2/+e_2`. This seed is not the nnseed
two-site seed `+e_1/+e_2`. This seed is not the y-axis opposite `±e_2` seed.

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
Axis is unsigned: `+e_i` and `−e_i` occupy the same axis. Cover is
complementary occupation of the three lattice axes. Leftover of the union
`{e_1,e_2,e_3}` minus `(Axis(M) union Axis(O))` empty is weaker: two sides
that both occupy all three axes have empty leftover and fail cover because
the intersection is nonempty. Leftover of `M` alone is a different object.
Leftover of `O` alone is a different object. Cover without the `|Axis(M)|=1`
cut is a different object, even when that cut happens to hold at every
scored probe.

Reverse 1-in 2-out holds if and only if split at `A` and split at `B` both
HOLD. Face 1-in 2-out holds if and only if split at `C` and split at `D`
both HOLD. Either side `UNDEFINED` is `UNDEFINED`. Else fail.

Identifying a named sign of those locks with reverse or face is refused:
named-sign lettering lost the axis. Identifying leftover-axis reverse with
this reverse is refused: leftover reverse fails when leftover at `B` is
empty. Identifying y-probe 1-in 2-out reverse with this reverse is refused:
y-probe reverse holds on this seed. Identifying 1-axis x-probe cover reverse
with this reverse is refused: nsopp x-probe cover reverse holds. Identifying
existential opposite of signed locks with split reverse is refused:
exist-opposite of signed M fails reverse and face here.

## Theorem 1 — ticks, `M`, `O`, `Axis`, cover, `|Axis(M)|`, and split at `τ=t+1`

On this process the four x-probes form. Cover of timed `M` and `O` fails at
`A` and at `D` because leftover axis `{e_2}` is missing from the union.
`|Axis(M)|=1` at each of the four x-probes. Split therefore equals cover on
this member:

```text
t(A)=2
t(B)=1
t(C)=3
t(D)=2
M(A, τ) = {−e_3}
M(B, τ) = {+e_1}
M(C, τ) = {+e_1}
M(D, τ) = {−e_3}
O(A, τ) = {+e_1}
O(B, τ) = {+e_2, +e_3, −e_3}
O(C, τ) = {−e_2, +e_3, −e_3}
O(D, τ) = {+e_1, −e_1}
Axis(M)(A, τ) = {e_3}
Axis(O)(A, τ) = {e_1}
Axis(M)(B, τ) = {e_1}
Axis(O)(B, τ) = {e_2, e_3}
Axis(M)(C, τ) = {e_1}
Axis(O)(C, τ) = {e_2, e_3}
Axis(M)(D, τ) = {e_3}
Axis(O)(D, τ) = {e_1}
cover(A) = fail
cover(B) = hold
cover(C) = hold
cover(D) = fail
|Axis(M)|(A, τ) = 1
|Axis(M)|(B, τ) = 1
|Axis(M)|(C, τ) = 1
|Axis(M)|(D, τ) = 1
split(A) = fail
split(B) = hold
split(C) = hold
split(D) = fail
```

A is not a seed. `A` forms at tick 2 by the incoming step `−e_3`. Mixed
remains a set: `O(B,τ)` has three outgoing steps and `O(D,τ)` has two.
Unique letters would assign `UNDEFINED` at mixed `O`. Here uniqueness is
not required. At `B` and at `C`, `Axis(M)` and `Axis(O)` are complementary:
their union is `{e_1,e_2,e_3}` and their intersection is empty, so cover
holds and split holds. At `A` and at `D`, leftover of the union is `{e_2}`,
so cover fails and split fails even though `|Axis(M)|=1`. O is not M. `M`
at `τ` is frozen equal to `M` at `t`. `O` at `t` is empty at `A`, `B`, and
`C`; at `D`, `O` at `t` is already `{−e_1}` from the seed neighbor
`(0,1,0)`. Cover at `t` fails and split at `t` fails at each of the four
x-probes. New records at `t+1` fill `O` at `A` and add `+e_1` at `D`; cover
then holds at `B` and at `C` and still fails at `A` and at `D`.

New records in `B_3(0)` between `t` and `t+1` that meet a probe's
six-neighbors enter `O` and do not enter earliest `M`:

```text
new 6-NN of A at t(A)+1: (2, 0, 0)
new 6-NN of B at t(B)+1: (1, 2, 1), (1, 1, 2), (1, 1, 0)
new 6-NN of C at t(C)+1: (2, -1, 0), (2, 0, 1), (2, 0, -1)
new 6-NN of D at t(D)+1: (2, 1, 0)
```

## Theorem 2 — reverse from 1-in 2-out at `τ`

Reverse 1-in 2-out holds if and only if split at `A` and split at `B` both
HOLD. Split fails at `A` because cover fails: leftover `{e_2}` is missing.
Split holds at `B`. Reverse fails. Cover reverse also fails. On this member
the extra `|Axis(M)|=1` cut does not change the reverse bit.

Reverse 1-in 2-out at τ: fail

Both sides are defined, so this is not `UNDEFINED`. Leftover-axis reverse
fails because leftover at `B` is empty while leftover at `A` is `{e_2}`.
Leftover-of-`M` reverse would fail because leftover of `M` at `A` is
`{e_1, e_2}` and leftover of `M` at `B` is `{e_2, e_3}`: nonempty and
unequal. Leftover-of-`O` reverse would fail because leftover of `O` at `A`
is `{e_2, e_3}` and leftover of `O` at `B` is `{e_1}`. Exist-opposite of
signed M fails reverse: `{−e_3}` against `{+e_1}` has no pair summing to
zero. Y-probe 1-in 2-out reverse holds on this seed. 1-axis nsopp x-probe
cover reverse holds. Those leftovers are not this display. Reverse fails.

## Theorem 3 — face from 1-in 2-out at `τ`

Face 1-in 2-out holds if and only if split at `C` and split at `D` both
HOLD. Split holds at `C`. Split fails at `D` because cover fails: leftover
`{e_2}` is missing. Face fails. Cover face also fails.

Face 1-in 2-out at τ: fail

Displayed, not adopted. The bits are not written into Admissibility.
Do not write into Admissibility. Do not attach L1.

Leftover-axis face fails because leftover at `C` is empty while leftover at
`D` is `{e_2}`. Leftover-of-`M` face would fail because leftover of `M` at
`C` is `{e_2, e_3}` and leftover of `M` at `D` is `{e_1, e_2}`. Leftover of
`O` at `C` is `{e_1}` and leftover of `O` at `D` is `{e_2, e_3}`:
leftover-of-`O` face would fail. Exist-opposite of signed M fails face:
`{+e_1}` against `{−e_3}` has no opposite pair. Y-probe face on this seed
also fails, from split fail at y-probe `D`. This display scores 1-in 2-out
of `Axis(M)` and `Axis(O)` on the x-probes.

## What this note does not claim

- It does not select a unique incoming, outgoing, or leftover lock.
- It does not reduce lock vectors to named signs `{+,−}`.
- It does not require `M` or `O` to be a singleton of signed letters.
- It does not sum either set.
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
- It does not reprint leftover of y-probe 1-in 2-out.
- It does not reprint leftover of 1-axis x-probe cover.
- It does not reprint leftover-axis reverse.
- It does not reprint leftover of leftover-of-`M` alone.
- It does not reprint leftover of leftover-of-`O` alone.
- It does not reprint leftover of same-lock two-axis.
- It does not treat split fail at `A` as 2-in 1-out: `|Axis(M)|=1` at `A`.
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
two-axis opposite process, 1-in 2-out axis split of `M` and `O` at `t+1`, and
the reverse/face bits from that split are displayed theorem-domain data.

## Exact target and obligation graph

| Obligation | Status |
|---|---|
| current Lattice / Admissibility / Record premises | quoted; no edit |
| perp-step incoming-lock process on `B_3(0)` | displayed; two disjoint opposite pairs at tick 0 |
| ticks `t(A)`, `t(B)`, `t(C)`, `t(D)` | Theorem 1; `2`, `1`, `3`, `2` |
| `M` at `τ=t+1` | Theorem 1; frozen equal to `M` at `t` |
| `O` at `τ=t+1` | Theorem 1; outgoing dual |
| `Axis(M)` and `Axis(O)` at `τ` | Theorem 1; complementary at `B,C`; leftover `{e_2}` at `A,D` |
| cover at `τ` | Theorem 1; fail at `A,D`, hold at `B,C` |
| `|Axis(M)|` at `τ` | Theorem 1; `1`, `1`, `1`, `1` |
| split at `τ` | Theorem 1; fail at `A,D`, hold at `B,C`; equals cover on this member |
| reverse from split at `τ` | Theorem 2; `fail` |
| face from split at `τ` | Theorem 3; `fail` |
| unique lock | not required |
| occupancy of sites as the letter | not used |
| named-sign `{+,−}` letter | not used; lost the axis |
| singleton unique lock-vector letter | not used as the object; mixed remains a set |
| `Z^3` sum of the lock set | not used; no aggregation |
| six-neighbor star as the letter | not used |
| leftover of y-probe 1-in 2-out | not this split display |
| leftover of 1-axis x-probe cover | not this split display |
| leftover-axis reverse | not this split display |
| leftover of leftover-of-`M` alone | not this display |
| leftover of leftover-of-`O` alone | not this display |
| leftover of same-lock two-axis | not this display |
| global later T | not used |
| 1-in 2-out split as Admissibility content | not adopted |
| formation site / probability / rate | open |
| physical Record readout of the bits | open |

## Value gate (V1–V5)

| # | Answer |
|---|---|
| V1 | It answers the first-display question: 1-in 2-out axis split of `M` and `O` at `t+1` on the four x-probes of the two-axis opposite seed, and reverse/face from that split, where nm2axx cover FAILs. |
| V2 | Current main has no landed 1-in 2-out reverse/face of timed `M` and `O` on these four two-axis opposite x-probes. |
| V3 | Split bits at one cut and the two split reverse/face bits are independently finite and exact. |
| V4 | The theorem is more than a restatement of Record because it reads unsigned 1-in 2-out of own incoming and own outgoing at the same `t+1` cut and scores reverse/face from that split. |
| V5 | It is not an adopted content rule: the bits remain displayed. |

## No-go discipline gate

The negative content is narrow: the display does not write those bits into
Admissibility, does not reduce them to named signs, does not require a
unique lock, does not replace split by leftover of `M` alone or leftover of
`O` alone, does not replace split by leftover-axis reverse, does not replace
split by existential opposite of signed locks, and does not identify this
display with y-probe 1-in 2-out HOLD or with 1-axis x-probe cover HOLD. No
global impossibility is claimed.

### N1 — materially distinct routes

| Route | Attempt | Why it fails here | Marker |
|---|---|---|---|
| leftover of y-probe 1-in 2-out | score reverse/face on `A=(0,1,0)` | y-probe `A` is a seed; y-probe reverse holds; x-probe reverse fails | ATTEMPTED |
| leftover of 1-axis x-probe cover | reuse nsopp `{0,(0,1,0)}` `+e_1/−e_1` | nsopp has two tick-0 sites; `t(A)=3` and cover holds at each x-probe; here four tick-0 sites, `t(A)=2`, cover fails at `A` and `D` | ATTEMPTED |
| leftover of same-lock two-axis | reuse `+e_1/+e_1` and `+e_2/+e_2` | seed letter at `(0,1,0)` is `−e_1` here; `O(D,τ)` is `{+e_1, −e_1}` here and `{+e_1}` on same-lock | ATTEMPTED |
| leftover-axis reverse | score nonempty leftover-axis equality | leftover `{e_2}` at `A` and empty at `B`; leftover reverse fail | ATTEMPTED |
| leftover of `M` alone | score `{e_1,e_2,e_3}` minus `Axis(M)` | leftover of `M` at `A` is `{e_1,e_2}` and at `B` is `{e_2,e_3}`, nonempty unequal | ATTEMPTED |
| leftover of `O` alone | score `{e_1,e_2,e_3}` minus `Axis(O)` | leftover of `O` at `A` is `{e_2,e_3}` and at `B` is `{e_1}`, nonempty unequal | ATTEMPTED |
| leftover of nnseed `+e_1/+e_2` | reuse nnseed two-site seed | split at `A` and at `B` both fail from that seed | ATTEMPTED |
| leftover of y-axis opposite `±e_2` | reuse seed `{0,(0,1,0)}` with locks `±e_2` | this seed has four tick-0 sites and a second opposite pair on `e_2` | ATTEMPTED |
| leftover of z-probes on this seed | reuse `A=(0,0,1)` | z-probe `A` is a seed with cover hold; x-probe `A` is not a seed | ATTEMPTED |
| exist-opposite of signed locks | score `a+b=(0,0,0)` inside `M` or `O` | exist-opposite of signed M fails reverse and face | ATTEMPTED |
| unique letter | replace mixed sets by a singleton or `UNDEFINED` | mixed `O(B,τ)` remains a set; unique-letter split at `B` is `UNDEFINED`; this split at `B` is hold | ATTEMPTED |
| sum of a set | replace split by a `Z^3` sum | the construction does not sum; `O(D,τ)` sums to `0` while `Axis(O)(D)` is `{e_1}` | ATTEMPTED |
| named-sign lettering | collapse `{±e_i}` to `{+,−}` | named-sign lettering lost the axis | ATTEMPTED |
| global later T | wait until `max t(A,B,C,D)` before reading | `τ(q)=t(q)+1` is per-probe; no global T | ATTEMPTED |
| attach a formation member from already-recorded six-neighbor locks | form the probes by a neighbor-lock letter instead of perp-step | refused; not attached | ATTEMPTED |
| adopt bits into Admissibility | rewrite the local rule by 1-in 2-out | refused; displayed, not adopted | ATTEMPTED |

### N2 — wall independence

Missing physical adoption, missing identification of split with y-probe
1-in 2-out, missing identification of split with 1-axis x-probe cover,
missing identification of split with leftover-axis reverse, missing
identification of split with leftover of `M` alone, missing identification
of split with exist-opposite of signed `M`, and missing Record identification
of split reverse are distinct open premises. This note claims no complete
wall collection.

### N3 — hidden-condition scan

The host `B_3(0)`, two disjoint opposite pairs at tick 0, perpendicular
step rule, incoming-step lock, own incoming set and own outgoing dual from
records with tick `<= τ`, per-probe `τ=t+1`, unsigned axis, cover as empty
intersection and three-axis union, split as cover together with
`|Axis(M)|=1`, four x-probes with `A` not a seed, and mixed remains a set
are declared. No uniqueness of lock, no six-neighbor lock union as the
scored object, no leftover-axis equality as the scored reverse, no y-probe
reverse as the scored reverse, no global later T, no formation attachment
from already-recorded six-neighbor locks, and no Admissibility rewrite are
silently assumed.

### N4 — source residual matching

The current axiom memo supplies cubic sites, `M_2(C)`,
content-conditional-on-formation, and unreadable absence. The residual that
formation site, probability, and rate remain unsupplied is unchanged. The
split reverse `fail` and face `fail` reports do not close that residual.

### N5 — resolution and rhetoric audit

| Resolution | Executed | Not claimed |
|---|---|---|
| per element | each unsigned lattice axis among `{e_1,e_2,e_3}` | no continuum alphabet |
| per site | `A,B,C,D` x-probes on `B_3(0)` only | no other cubic sites |
| per mode | no mode calculation | no spectral exhaustion |
| per block | four split bits, reverse/face from 1-in 2-out | no adopted content law |
| lattice wide | checked and not executed | no lattice-wide lettering rule |

### N6 — live partial-closure paths

Live routes include a later Record content map for 1-in 2-out reverse/face, a
formation-rate rule, and a physical selector among complementary axis
splits. None is taken here.

### N7 — hostile steelman

**Steelman:** Split FAIL is only cover FAIL, so this is leftover of nm2axx
cover; y-probe 1-in 2-out already holds reverse on this seed; 1-axis nsopp
x-probes already fail split reverse; leftover `{e_2}` already names the
missing axis; unique singleton `M` already is 1-in; and mixed `O` is only
unique-letter `UNDEFINED`.

**Answer:** Cover fails at `A` and at `D` from leftover `{e_2}`. `|Axis(M)|=1`
at each of the four x-probes, so split equals cover on this member: that
coincidence is reported, not hidden. It is not leftover of 1-axis nsopp
x-probes, where cover holds at each probe and split fails at `A` from 2-in
1-out with `t(A)=3`. Here `t(A)=2` and `M(A,τ)={−e_3}`. It is not leftover
of y-probe 1-in 2-out: y-probe reverse holds and x-probe reverse fails. It
is not leftover of leftover-axis reverse: leftover at `B` is empty.
Unique-letter split at mixed `O(B)` is `UNDEFINED`; this split at `B` is
hold. Same-lock two-axis has `O(D,τ)={+e_1}`; this opposite seed has
`O(D,τ)={+e_1, −e_1}`. Split reverse is HOLD of split at `A` and at `B`.

### N8 — cross-cycle echo

nm2axx cover on these four x-probes fails reverse and fails face. 1-axis
nsopp x-probe cover holds reverse while 1-in 2-out split reverse fails from
2-in 1-out at `A`. Y-probe 1-in 2-out on this two-axis opposite seed holds
reverse and fails face. This note is not those displays: it reports 1-in
2-out axis split of `M` and `O` at `τ=t+1` on the two-axis opposite x-probes,
`|Axis(M)|=1` at each probe, cover fail at `A` and at `D` from leftover
`{e_2}`, reverse fail, and face fail.

**Gate disposition:** PASS for the 1-in 2-out `t+1` reverse/face reports
above. FAIL / DO NOT SHIP for “the predicate equals the named sign,” “the
predicate equals the unique singleton lock vector,” “the predicate equals
six-neighbor lock union,” “the predicate equals leftover of `M` alone,”
“the predicate equals leftover of `O` alone,” “the predicate equals
leftover-axis reverse,” “the predicate equals y-probe 1-in 2-out HOLD,”
“the predicate equals 1-axis x-probe cover HOLD,” “the predicate equals
exist-opposite of signed M,” “bits are Admissibility,” “split holds at
`A`,” “reverse 1-in 2-out holds,” “face 1-in 2-out holds,” or “empty
leftover at `B` is this reverse.”

## Primary runner

The paired runner builds Euclidean `B_3(0)`, runs the two-axis opposite
perp-step incoming-lock process, reads each probe's own earliest incoming
set and own outgoing dual from the record prefix at that probe's `t+1`,
reports unsigned axis of each, reports cover, reports `|Axis(M)|`, reports
1-in 2-out split, lists new records in `B_3(0)` between `t` and `t+1` that
meet a probe's six-neighbors, and checks Theorems 1--3. It also checks that
cover fails at `A` and at `D` from leftover `{e_2}` while `|Axis(M)|=1` at
each probe so split equals cover, that leftover empty at `B` fails leftover
reverse, that y-probe reverse holds while x-probe reverse fails, that
1-axis nsopp x-probe cover reverse holds, that leftover of `M` alone and
leftover of `O` alone are different objects, that exist-opposite of signed
M fails reverse and face, that mixed `O` remains a set, that unique-letter
split is `UNDEFINED` at mixed `O(B)` while this split holds, that
same-lock two-axis has a different `O(D)`, that the construction does not
sum, that a formation member from already-recorded six-neighbor locks is
not attached, and that the display is not the nsopp one-axis leftover
process. No runner cache is written.
