---
claim_id: two_axis_same_lock_xprobe_incoming_outgoing_axis_cover_tplus1_reverse_face_bounded_theorem_note_2026-08-15
claim_type: bounded_theorem
claim_scope: "Axis-cover of M and O at t+1 on the four x-probes of the two-axis same-lock seed, and reverse/face from that, are reported. Displayed, not adopted."
upstream_dependencies:
  - minimal_axioms
runner: scripts/two_axis_same_lock_xprobe_incoming_outgoing_axis_cover_tplus1_reverse_face_2026_08_15.py
---

# Axis-Cover Of Incoming Versus Outgoing At t+1 On Four X-Probes Of The Two-Axis Same-Lock Seed

> **Key terms used in this doc** are indexed A-Z at `docs/KEY_TERMINOLOGY.md`;
> each row points to the canonical source-of-truth doc.

**Date:** 2026-08-15
**Type:** bounded_theorem
**Scope:** axis-cover of `M` versus `O` at each probe's `τ=t+1` on the
four x-probes of the two-axis same-lock seed in `B_3(0)={n:n·n<=9}`. Same
process as nm2sl, x-probes. Let `t(q)` be the formation tick of probe
`q`. Let `τ(q)=t(q)+1`. There is no global T. `M(q,τ)` is the set of
earliest incoming nearest-neighbor steps at `q` using only records with
tick `<= τ`. Seeds are a singleton seed letter. `O(q,τ)` is the outgoing
dual of `M`: the set of `e` in `{±e_1,±e_2,±e_3}` such that `q+e` is
formed and `e` is in `M(q+e,τ)`. Unformed at `τ` is `UNDEFINED`. Empty
`O` is empty, not `UNDEFINED`. Axis of a defined lock set `S` is
`Axis(S)={e_i | some ±e_i in S}`. Cover HOLD at formed `q` if and only if
`Axis(M)∩Axis(O)` is empty and `Axis(M)∪Axis(O)` equals `{e_1,e_2,e_3}`.
Unformed at `τ` is `UNDEFINED`. Empty `O` fails cover unless `Axis(M)`
already equals `{e_1,e_2,e_3}`. Reverse HOLD if and only if cover at `A`
and at `B`. Face likewise on `C,D`. Mixed remains a set. Uniqueness of
incoming or outgoing locks is not required. Occupancy of sites is not
used. This is not named-sign lettering. This is not leftover-empty fail.
This is not leftover of leftover-axis. This is not leftover of
forall-perp. This is not leftover of exist-opposite of M. This is not
leftover of exist-opposite of O. This is not leftover of leftover-of-`M`
alone. This is not leftover of leftover-of-`O` alone. This is not leftover
of two-axis opposite. This is not leftover of 1-axis same-lock cover-HOLD.
This is not leftover of the four y-probes of this same seed. Neither pair
is opposite. This display does not use a six-neighbor star. Displayed, not
adopted. Do not write into Admissibility. Do not attach L1. This note does
not write axis-cover into Admissibility and does not attach a formation
member from already-recorded six-neighbor locks. This display does not
use occupancy.
**Audit-status authority:** independent audit lane only. This note authors no
audit verdict and predicts none.
**Primary runner:**
[`scripts/two_axis_same_lock_xprobe_incoming_outgoing_axis_cover_tplus1_reverse_face_2026_08_15.py`](../scripts/two_axis_same_lock_xprobe_incoming_outgoing_axis_cover_tplus1_reverse_face_2026_08_15.py)

Framework input:

- [`MINIMAL_AXIOMS_2026-06-29.md`](MINIMAL_AXIOMS_2026-06-29.md) supplies
  cubic-lattice sites `Z^3` with nearest-neighbor adjacency, the one-site
  algebra `M_2(C)`, and the Record sentences that records form and that a
  present record locks exactly one admissible local possibility.

Everything after that quoted input is a finite displayed process on `B_3(0)`
and the four named x-probes. Incoming lock letters are unit nearest-neighbor
steps. `O` is the outgoing dual of those incoming sets at the per-probe cut
`τ=t+1`. Reverse and face are scored on axis-cover of `M` versus `O` at
that same cut. Named signs `{+,−}` are a coarser readout and are not used.
A singleton unique lock letter is a different readout and is not used as
the object. A `Z^3` sum of those locks is a different readout and is not
used. Occupancy of sites is not used. A six-neighbor star is not the letter.
O is not M.

## Machine status and trace

```yaml
actual_current_surface_status: bounded-support
target_claim_type: bounded_theorem
claim_type_reason: "Exact report of Axis-cover of M and O at t+1 on the four x-probes of the two-axis same-lock seed, reverse fail and face fail from cover at A,B and at C,D; uniqueness of locks is not claimed and the bits are not adopted."
trace_class: frontier_discovery
target_claim_id: two_axis_same_lock_xprobe_incoming_outgoing_axis_cover_tplus1_reverse_face
target_blocker_text: "display Axis-cover of M and O at t+1 on the four x-probes of the two-axis same-lock seed, and reverse/face from that, or UNDEFINED"
source_of_blocker_text: handoff
reachability_to_target: advances
artifact_role: theorem
next_trace_action: "Keep Axis-cover of M and O at t+1 displayed; do not write axis-cover into Admissibility, do not reduce to leftover-empty fail, do not replace cover by leftover of M alone or leftover of O alone, do not replace cover by two-axis opposite, do not replace cover by y-probe same-lock, do not reduce to a unique letter, do not use occupancy, and do not attach L1."
conditional_surface_status: "exact on B_3(0) for Axis-cover of M and O at t+1 on the four x-probes of the two-axis same-lock seed, reverse fail and face fail; displayed, not adopted"
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

No larger host is used. The four x-probes are the only sites whose own
incoming and outgoing sets are scored:

```text
A = (1,0,0),  B = (1,1,1),  C = (2,0,0),  D = (1,1,0).
```

These are not the y-probes `A=(0,1,0)`, `B=(1,1,1)`, `C=(0,2,0)`,
`D=(1,1,0)`. These are not the z-probes `A=(0,0,1)`, `B=(1,1,1)`,
`C=(0,0,2)`, `D=(1,0,1)`. `A` is not a seed. Same process as nm2sl,
x-probes.

Lock alphabet of the displayed process: `{±e_i}` with `i` in `{1,2,3}`.

Seed: two disjoint same-lock pairs recorded at formation tick 0. Origin
locks `+e_1` and `(0,1,0)` locks `+e_1`. `(0,0,1)` locks `+e_2` and
`(0,1,1)` locks `+e_2`. The second pair is a new seed, not a formed child
of the first pair, and neither pair is opposite. This seed is not the
1-axis same-lock two-site seed `{0,(0,1,0)}` with `+e_1/+e_1` alone. This
seed is not the two-axis opposite seed `+e_1/−e_1` and `+e_2/−e_2`. This
seed is not the nspar two-site seed. This seed is not the x-axis same-lock
seed `{0,(1,0,0)}` with `+e_2/+e_2`.

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

## Named incoming set `M`, outgoing set `O`, Axis, and cover at `τ=t+1`

Let `t(q)` be the formation tick of x-probe `q` when that tick is defined in
`B_3(0)`. Let `τ(q)=t(q)+1`. There is no global T.

`M(q,τ)` is the set of earliest incoming nearest-neighbor steps at `q`
using only records with tick `<= τ`. If `q` is unformed at `τ`, then
`M(q,τ)` is `UNDEFINED`. If `q` is a seed and `τ >= 0`, then `M(q,τ)` is
the singleton seed letter. Own incoming sets are the scored incoming
object.

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

Cover HOLD at formed `q` if and only if

```text
Axis(M(q,τ)) ∩ Axis(O(q,τ)) = empty
Axis(M(q,τ)) ∪ Axis(O(q,τ)) = {e_1,e_2,e_3}.
```

Unformed at `τ` is `UNDEFINED`. Empty `O` fails cover unless `Axis(M)`
already equals `{e_1,e_2,e_3}`. Overlap of axes fails even when the union
is full. Leftover of the union is `{e_1,e_2,e_3}` minus `(Axis(M) union
Axis(O))`. Empty leftover is leftover fail of leftover-empty scoring; this
display is HOLD iff cover, not leftover-empty fail. Leftover of `M` alone
is `{e_1,e_2,e_3}` minus `Axis(M)`, a different object. Leftover of `O`
alone is a different object.

Reverse HOLD if and only if cover at `A` and at `B`. Face HOLD if and only
if cover at `C` and at `D`. If either side of that pair is `UNDEFINED`, the
report is `UNDEFINED`. Else if either fails, the report is `fail`. The
report is one of `hold`, `fail`, or `UNDEFINED`.

Identifying a named sign of those locks with reverse or face is refused:
named-sign lettering lost the axis. Reverse and face are scored on
axis-cover of incoming versus outgoing at the same cut. They are not
scored on `{+,−}` names and are not an occupancy-kernel inner product.

## Theorem 1 — ticks, `M`, `O`, Axis, and cover at `A,B,C,D`

On this process the four x-probes form. Incoming is frozen at formation:
`M(q,t+1)=M(q,t)` at every scored probe. Outgoing is empty at `t` at each
of the four probes, then filled at `t+1`. This display reads `M` and `O`
together at the same cut `τ=t+1` and scores Axis and cover:

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
O(D, τ) = {+e_1}
Axis(M(A, τ)) = {e_3}
Axis(O(A, τ)) = {e_1}
Axis(M(B, τ)) = {e_1}
Axis(O(B, τ)) = {e_2, e_3}
Axis(M(C, τ)) = {e_1}
Axis(O(C, τ)) = {e_2, e_3}
Axis(M(D, τ)) = {e_3}
Axis(O(D, τ)) = {e_1}
cover(A): fail
cover(B): hold
cover(C): hold
cover(D): fail
```

`A` is not a seed. `A` is the site `(1,0,0)` forming at tick 2 with
incoming `{−e_3}`. Mixed remains a set: `O(B,τ)` has three outgoing
steps and `O(C,τ)` has three outgoing steps. Unique letters would assign
`UNDEFINED` at those mixed outgoing sets and would leave reverse and face
`UNDEFINED`. Here uniqueness is not required. `M` and `O` are disjoint at
each of the four probes at `τ`. O is not M. Cover holds at `B` and at `C`
because the Axis sets are complementary partitions of `{e_1,e_2,e_3}`.
Cover fails at `A` and at `D` because `Axis(M)∪Axis(O)={e_1,e_3}` misses
`e_2`.

New records in `B_3(0)` between `t` and `t+1` that meet a probe's
six-neighbors enter `O` and do not enter earliest `M`:

```text
new 6-NN of A at t(A)+1: (2, 0, 0)
new 6-NN of B at t(B)+1: (1, 2, 1), (1, 1, 2), (1, 1, 0)
new 6-NN of C at t(C)+1: (2, -1, 0), (2, 0, 1), (2, 0, -1)
new 6-NN of D at t(D)+1: (2, 1, 0)
```

At `t`, `O` is empty at each of the four probes, so cover fails at `t`
because the union is not `{e_1,e_2,e_3}`. Reverse at `t` is `fail`. That
empty-at-`t` leftover is not this display. Forall-perp at those probes is
`UNDEFINED` at `t` from empty `O`, so empty-at-`t` already splits cover
from forall-perp. At `τ`, forall-perp HOLDs at `A` because `{−e_3}` is
orthogonal to `{+e_1}`, while cover FAILs at `A` because leftover-axis is
`{e_2}`. Leftover of the union at `τ` is `{e_2}` at `A` and empty at `B`;
leftover-empty reverse fails from empty leftover at `B` while cover HOLDs
at `B`. Two-axis opposite on these same x-probes also reports reverse fail
and face fail, but `O(D,τ)` there is `{+e_1, −e_1}` and `O(D,t)` there is
already `{−e_1}`; here `O(D,τ)` is `{+e_1}` and `O(D,t)` is empty. Y-probes
on this same seed report reverse hold and face fail; this display scores
the x-probes. 1-axis same-lock on these x-probes HOLDs cover at each probe
including `A` and `D`, with `t(A)=3` and mixed `M(A,τ)`.

## Theorem 2 — reverse hold / fail / UNDEFINED

Reverse HOLD if and only if cover at `A` and at `B`. Cover fails at `A`
and HOLDs at `B`. Reverse fails. Both sides are nonempty and defined, so
this is not `UNDEFINED`. This is not `hold`.

Reverse: fail

Reverse fails. Unique-letter leftover reports reverse `UNDEFINED` from
mixed `O(B,τ)`. Leftover-empty leftover reports reverse `fail` from empty
leftover at `B`, but cover HOLDs at `B`; reverse fails here because cover
fails at `A`. Forall-perp leftover reports reverse hold from orthogonal
pairs at `A` and at `B` while cover reverse fails. Exist-opposite of `M`
leftover reports reverse fail from `{−e_3}` against `{+e_1}` and never
reads `O`. Exist-opposite of `O` leftover reports reverse fail from
`{+e_1}` against `{+e_2, +e_3, −e_3}`. Reverse HOLD uses cover at `A` and
at `B`.

Reverse fails.

## Theorem 3 — face hold / fail / UNDEFINED

Face HOLD if and only if cover at `C` and at `D`. Cover HOLDs at `C` and
fails at `D`. Face fails. Mixed `O(C,τ)` remains a three-element set and
`Axis(M(D,τ))={e_3}` against `Axis(O(D,τ))={e_1}` misses `e_2`.

Face: fail

Displayed, not adopted. The bits are not written into Admissibility.
Do not write into Admissibility. Do not attach L1.

This is not `hold` and not `UNDEFINED`. Face fails. Unique-letter leftover
reports face `UNDEFINED` from mixed `O(C,τ)`. Leftover-empty leftover
reports face `fail` from empty leftover at `C` while cover HOLDs at `C`;
face fails here because cover fails at `D`. Forall-perp leftover reports
face hold. Exist-opposite of `M` leftover reports face fail from `{+e_1}`
against `{−e_3}` inside incoming sets, not axis-cover of `M` versus `O`.
Face already fails at `τ=t+1` from cover at `C` and at `D`.

Face fails.

## What this note does not claim

- It does not select a unique incoming or outgoing lock.
- It does not reduce lock vectors to named signs `{+,−}`.
- It does not require either set to be a singleton.
- It does not sum either set.
- It does not replace `O` by `M`.
- It does not replace either set by locks of six-neighbors.
- It does not use a six-neighbor star as the letter.
- It does not wait for a global later T.
- It does not attach a formation member from already-recorded six-neighbor
  locks.
- It does not replace cover by leftover-empty fail.
- It does not replace cover by leftover of `M` alone.
- It does not replace cover by leftover of `O` alone.
- It does not reprint leftover-axis as the scored predicate.
- It does not reprint forall-perp as the scored predicate.
- It does not reprint exist-opposite of `M` as this display.
- It does not reprint exist-opposite of `O` as this display.
- It does not reprint two-axis opposite axis-cover.
- It does not reprint 1-axis same-lock cover-HOLD.
- It does not reprint y-probe same-lock reverse hold.
- It does not use occupancy of sites as the letter.
- It does not score reverse or face as an occupancy-kernel inner product.
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
two-axis same-lock four-site process, the own incoming and outgoing sets
at `t+1`, the Axis sets, and the axis-cover reverse/face bits are
displayed theorem-domain data.

## Exact target and obligation graph

| Obligation | Status |
|---|---|
| current Lattice / Admissibility / Record premises | quoted; no edit |
| perp-step incoming-lock process on `B_3(0)` | displayed; two disjoint same-lock pairs `+e_1/+e_1` and `+e_2/+e_2` |
| ticks `t(A)`, `t(B)`, `t(C)`, `t(D)` | Theorem 1; `2`, `1`, `3`, `2` |
| `M` at `τ=t+1` | Theorem 1; frozen equal to `M` at `t` |
| `O` at `τ=t+1` | Theorem 1; outgoing dual nonempty at `τ` |
| `Axis(M)` and `Axis(O)` at each probe | Theorem 1; complementary at `B,C`; leftover `{e_2}` at `A,D` |
| cover at `A,B,C,D` | Theorem 1; `fail`, `hold`, `hold`, `fail` |
| reverse and face from cover | Theorems 2–3; `fail` / `fail` |
| unique incoming or outgoing lock | not required |
| occupancy of sites as the letter | not used |
| named-sign `{+,−}` letter | not used; lost the axis |
| singleton unique lock-vector letter | not used as the object; mixed remains a set |
| `Z^3` sum of the lock set | not used; no aggregation |
| occupancy-kernel inner product | not used |
| leftover-empty fail | not this cover display |
| leftover of leftover-axis | not this display; empty leftover at `B` fails leftover-axis reverse while cover HOLDs at `B` |
| leftover of leftover-of-`M` alone | not this display |
| leftover of leftover-of-`O` alone | not this display |
| leftover of forall-perp | not this display; forall-perp reverse HOLDs while cover reverse fails |
| leftover of exist-opposite of M | not this display |
| leftover of exist-opposite of O | not this display |
| leftover of two-axis opposite | not this display; `O(D)` there is `{+e_1, −e_1}` |
| leftover of 1-axis same-lock cover-HOLD | not this display; 1-axis HOLDs at `A` and `D` |
| leftover of y-probe same-lock reverse hold | not this display |
| six-neighbor star as the letter | not used |
| axis-cover as Admissibility content | not adopted |
| formation site / probability / rate | open |
| physical Record readout of the bits | open |

## Value gate (V1–V5)

| # | Answer |
|---|---|
| V1 | It answers the probe-direction discriminator: Axis-cover of `M` and `O` at `t+1` on the four x-probes of the two-axis same-lock seed, and reverse/face from that. |
| V2 | Current main has no landed Axis-cover of `M` and `O` reverse/face report on these four x-probes of the two-axis same-lock seed. |
| V3 | Incoming sets, outgoing sets, Axis sets, cover bits, and the `fail`/`fail` reports are independently finite and exact. |
| V4 | The theorem is more than a restatement of Record because it reads own incoming and own outgoing at the same `t+1` cut and scores disjoint full Axis cover. |
| V5 | It is not an adopted content rule: the bits remain displayed. |

## No-go discipline gate

The negative content is narrow: the display does not write those bits into
Admissibility, does not reduce them to named signs, does not require a
unique letter, does not replace `O` by `M`, does not replace cover by
leftover-empty fail, does not replace cover by leftover of `M` alone or
leftover of `O` alone, does not replace cover by leftover-axis, does not
replace cover by forall-perp, does not replace cover by exist-opposite of
`M` or of `O`, does not identify this display with two-axis opposite or
with y-probe same-lock, does not use a six-neighbor star, and does not use
occupancy of sites. No global impossibility is claimed.

### N1 — materially distinct routes

| Route | Attempt | Why it fails here | Marker |
|---|---|---|---|
| leftover-empty fail | score reverse/face as leftover nonempty-equal | leftover of the union is empty at `B`, leftover reverse fails, while cover HOLDs at `B`; reverse fails here from cover fail at `A` | ATTEMPTED |
| leftover-axis | score equality of nonempty `{e_1,e_2,e_3}` minus `Axis(M)∪Axis(O)` | leftover is empty at `B` so leftover-axis reverse fails while cover HOLDs at `B` | ATTEMPTED |
| leftover of `M` alone | score `{e_1,e_2,e_3}` minus `Axis(M)` | leftover of `M` at `A` is `{e_1,e_2}` and at `B` is `{e_2,e_3}`, nonempty unequal, reverse would fail, but that is not cover of the pair | ATTEMPTED |
| leftover of `O` alone | score `{e_1,e_2,e_3}` minus `Axis(O)` | leftover of `O` at `A` is `{e_2,e_3}` and at `B` is `{e_1}`, nonempty unequal | ATTEMPTED |
| forall-perp | score every pair `m·o=0` | leftover; forall-perp reverse HOLDs while cover reverse fails because leftover at `A` is `{e_2}` | ATTEMPTED |
| exist-opposite of M | score `a+b=0` inside `M(A)` and `M(B)` | leftover; that readout never reads `O` | ATTEMPTED |
| exist-opposite of O | score `a+b=0` inside `O(A)` and `O(B)` | leftover; that readout never reads `M` | ATTEMPTED |
| unique letter | replace mixed sets by a singleton or `UNDEFINED` | mixed `O(B,τ)` and `O(C,τ)` remain sets; unique-letter reverse and face are `UNDEFINED` | ATTEMPTED |
| empty `O` at `t` | score cover at formation tick | `O` is empty at each probe at `t` so reverse at `t` is `fail`; this cut is `τ=t+1` | ATTEMPTED |
| y-probes on the same process | score `A=(0,1,0)`, `C=(0,2,0)` | leftover; y-probe reverse HOLDs while x-probe reverse fails; `M(A)` there is `{+e_1}`, not `{−e_3}` | ATTEMPTED |
| z-probes on the same process | score `A=(0,0,1)`, `C=(0,0,2)` | leftover; z-probe reverse fails and face HOLDs; `M(A)` is `{+e_2}`, not `{−e_3}` | ATTEMPTED |
| two-axis opposite on these x-probes | replace same-lock second letters by opposites | leftover; `O(D)` there is `{+e_1, −e_1}` and `O(D,t)` is `{−e_1}`; here `O(D)` is `{+e_1}` and `O(D,t)` is empty | ATTEMPTED |
| 1-axis same-lock on these x-probes | drop the second same-lock pair | leftover; 1-axis HOLDs cover at each probe including `A` and `D`, with `t(A)=3` and mixed `M(A)` | ATTEMPTED |
| nsopp on these x-probes | replace the seed by `+e_1/−e_1` | leftover; nsopp reverse HOLDs and face HOLDs; `M(A)` is mixed, not `{−e_3}` | ATTEMPTED |
| nspar `+e_1/−e_1` on these x-probes | replace the same-lock seed | leftover; cover FAILs at `B` from overlapping axes | ATTEMPTED |
| x-axis same-lock y-probe leftover | reuse seed `{0,(1,0,0)}` with `+e_2/+e_2` | leftover; `A` is a seed locking `+e_2` and reverse HOLDs | ATTEMPTED |
| sum of a set | replace each set by its `Z^3` sum | the construction does not sum; mixed `O(B,τ)` sums to `{+e_2}` only after cancellation of `±e_3` | ATTEMPTED |
| named-sign lettering | collapse `{±e_i}` to `{+,−}` | named-sign lettering lost the axis | ATTEMPTED |
| occupancy-kernel inner product | score an occupancy inner product | different object; not an occupancy-kernel inner product | ATTEMPTED |
| six-neighbor lock union | score locks of six-neighbors formed by `t(q)` | this display does not use a six-neighbor star | ATTEMPTED |
| global later T | wait until `max t(A,B,C,D)` before reading | `τ(q)=t(q)+1` is per-probe; no global T | ATTEMPTED |
| attach a formation member from already-recorded six-neighbor locks | form the probes by a neighbor-lock letter instead of perp-step | refused; not attached | ATTEMPTED |
| adopt bits into Admissibility | rewrite the local rule by axis-cover | refused; displayed, not adopted | ATTEMPTED |

### N2 — wall independence

Missing physical adoption, missing identification of cover with leftover-empty
fail, missing identification of cover with leftover of `M` alone, missing
identification of cover with two-axis opposite, missing identification of
cover with y-probe same-lock, missing identification of cover with
forall-perp, and missing Record identification of axis-cover are distinct
open premises. This note claims no complete wall collection.

### N3 — hidden-condition scan

The host `B_3(0)`, four-site two-axis same-lock seed locks `+e_1`, `+e_1`,
`+e_2`, and `+e_2`, perpendicular step rule, incoming-step lock, own
incoming set and own outgoing dual from records with tick `<= τ`,
per-probe `τ=t+1`, unsigned axis, cover as complementary occupation of
`{e_1,e_2,e_3}` by `Axis(M)` and `Axis(O)`, HOLD iff cover not leftover-empty
fail, four x-probes with `A` not a seed, empty or `UNDEFINED` as declared,
and mixed remains a set are declared. No uniqueness of locks, no
six-neighbor star as the scored object, no leftover-empty fail as the
scored predicate, no leftover of `M` alone, no leftover of `O` alone, no
forall-perp as the scored predicate, no exist-opposite of `M` or of `O` as
the scored predicate, no global later T, no formation attachment from
already-recorded six-neighbor locks, and no Admissibility rewrite are
silently assumed.

### N4 — source residual matching

The current axiom memo supplies cubic sites, `M_2(C)`,
content-conditional-on-formation, and unreadable absence. The residual that
formation site, probability, and rate remain unsupplied is unchanged. The
cover `fail`/`fail` reports do not close that residual.

### N5 — resolution and rhetoric audit

| Resolution | Executed | Not claimed |
|---|---|---|
| per element | each earliest incoming or outgoing nearest-neighbor step | no continuum alphabet |
| per site | `A,B,C,D` x-probes on `B_3(0)` only | no other cubic sites |
| per mode | no mode calculation | no spectral exhaustion |
| per block | four incoming sets, four outgoing sets, Axis, cover, reverse/face | no adopted content law |
| lattice wide | checked and not executed | no lattice-wide lettering rule |

### N6 — live partial-closure paths

Live routes include a later Record content map for axis-cover reverse/face,
a formation-rate rule, and a physical selector among `{±e_i}`. None is taken
here.

### N7 — hostile steelman

**Steelman:** Axis-cover of `M` versus `O` on these x-probes is only the
two-axis opposite x-probe leftover because reverse/face are `fail`/`fail`
and `M`/`O` at `A`,`B`,`C` match; it is only leftover-empty fail because
leftover at `A` is `{e_2}`; it is only forall-perp because every pair at
`τ` dots to zero and forall-perp reverse HOLDs; it is only the y-probe
cover because the seed is the same; mixed `O(B)` should make reverse
`UNDEFINED`; and 1-axis same-lock x-probes already HOLD.

**Answer:** Two-axis opposite has `O(D,τ)={+e_1, −e_1}` and `O(D,t)={−e_1}`;
this member has `O(D,τ)={+e_1}` and empty `O(D,t)`. Leftover-empty reverse
fails from empty leftover at `B` while cover HOLDs at `B`. Reverse fails
here because cover fails at `A`, where the union misses `e_2`. Forall-perp
HOLDs at `A` from `{−e_3}·{+e_1}=0` while cover FAILs at `A`. Y-probes are
a different four-tuple; reverse HOLDs there and fails here. Mixed
`O(B,τ)` remains `{+e_2, +e_3, −e_3}` and reverse is `fail`, not
`UNDEFINED`. 1-axis same-lock HOLDs cover at `A` and at `D` with `t(A)=3`.

### N8 — cross-cycle echo

nm2sl reported axis-cover of `M` versus `O` on the four y-probes of this
same two-axis same-lock seed: reverse hold and face fail. nm2axx reported
axis-cover on the four x-probes of the two-axis opposite seed: reverse
fail and face fail with `O(D)={+e_1, −e_1}`. This note is the
probe-direction discriminator on two-axis same-lock: Axis-cover of `M`
versus `O` at `τ=t+1` on the four x-probes, leftover `{e_2}` at `A` and at
`D`, reverse fail, and face fail, with singleton `O(D)={+e_1}`. HOLD iff
cover, not leftover-empty fail, and not leftover of two-axis opposite.

**Gate disposition:** PASS for the Axis-cover of `M` vs `O` at `t+1`
reverse/face reports above. FAIL / DO NOT SHIP for “the predicate equals the
named sign,” “the predicate equals the unique singleton lock vector,” “the
predicate equals leftover-empty fail,” “the predicate equals leftover of `M`
alone,” “the predicate equals leftover-axis,” “the predicate equals
forall-perp,” “the predicate equals exist-opposite of `M`,” “the predicate
equals two-axis opposite,” “the predicate equals y-probe same-lock,” “bits
are Admissibility,” “cover holds at `A`,” “reverse holds,” “face is
`UNDEFINED`,” or “`O` is `M`.”

## Primary runner

The paired runner builds Euclidean `B_3(0)`, runs the two-axis same-lock
perp-step incoming-lock process, reads each probe's own earliest incoming
set and own outgoing dual from the record prefix at that probe's `t+1`,
reports Axis sets and cover at `A,B,C,D`, lists new records in `B_3(0)`
between `t` and `t+1` that meet a probe's six-neighbors, and checks
Theorems 1--3. It also checks that `M` is frozen from `t` to `t+1`, that
`O` is empty at `t` at each of the four probes so cover fails at that
leftover cut, that mixed sets remain sets, that unique-letter reverse and
face are `UNDEFINED`, that leftover-empty reverse fails from empty leftover
at `B` while cover HOLDs at `B`, that forall-perp reverse HOLDs while cover
reverse fails, that leftover of `M` alone and leftover of `O` alone are
different objects, that the construction does not sum, that a formation
member from already-recorded six-neighbor locks is not attached, that
y-probe reverse HOLDs on this same seed, that two-axis opposite `O(D)` is
`{+e_1, −e_1}` while this `O(D)` is `{+e_1}`, and that 1-axis same-lock
cover HOLDs at `A` and at `D`. No runner cache is written.
