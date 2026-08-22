---
claim_id: opposite_lock_xprobe_incoming_outgoing_axis_cover_tplus1_reverse_face_bounded_theorem_note_2026-08-15
claim_type: bounded_theorem
claim_scope: "Axis-cover of M and O at t+1 on the four #7168 x-probes, and reverse/face from that, are reported. Displayed, not adopted."
upstream_dependencies:
  - minimal_axioms
runner: scripts/opposite_lock_xprobe_incoming_outgoing_axis_cover_tplus1_reverse_face_2026_08_15.py
---

# Axis-Cover Of Incoming Versus Outgoing At t+1 On Four #7168 X-Probes

> **Key terms used in this doc** are indexed A-Z at `docs/KEY_TERMINOLOGY.md`;
> each row points to the canonical source-of-truth doc.

**Date:** 2026-08-15
**Type:** bounded_theorem
**Scope:** axis-cover of `M` versus `O` at each probe's `τ=t+1` on the
four nsuoxinc #7168 x-probes in `B_3(0)={n:n·n<=9}`. Same process as nsopp
#7093. Same x-probes as nsuoxinc #7168. Let `t(q)` be the formation tick of
probe `q`. Let `τ(q)=t(q)+1`. There is no global T. `M(q,τ)` is the set of
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
incoming or outgoing locks is not required. Occupancy `n` is not used.
This is not named-sign lettering. This is not leftover of leftover-axis.
This is not leftover of forall-perp. This is not leftover of
exist-opposite of M. This is not leftover of exist-opposite of O. This
display does not use a six-neighbor star. Displayed, not adopted. Do not
write into Admissibility. Do not attach L1. This note does not write
axis-cover into Admissibility and does not attach a formation member from
already-recorded six-neighbor locks. This display does not use occupancy.
Y-probe cover HOLDING on the same seed is a different four-tuple.
nsmopx #7217 own-incoming exist-opposite fails on these x-probes.
**Audit-status authority:** independent audit lane only. This note authors no
audit verdict and predicts none.
**Primary runner:**
[`scripts/opposite_lock_xprobe_incoming_outgoing_axis_cover_tplus1_reverse_face_2026_08_15.py`](../scripts/opposite_lock_xprobe_incoming_outgoing_axis_cover_tplus1_reverse_face_2026_08_15.py)

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
used. Occupancy `n` is not used. A six-neighbor star is not the letter.
O is not M.

## Machine status and trace

```yaml
actual_current_surface_status: bounded-support
target_claim_type: bounded_theorem
claim_type_reason: "Exact report of Axis-cover of M and O at t+1 on the four #7168 x-probes, reverse hold and face hold from cover at A,B and at C,D; uniqueness of locks is not claimed and the bits are not adopted."
trace_class: frontier_discovery
target_claim_id: opposite_lock_xprobe_incoming_outgoing_axis_cover_tplus1_reverse_face
target_blocker_text: "display Axis-cover of M and O at t+1 on the four #7168 x-probes, and reverse/face from that, or UNDEFINED"
source_of_blocker_text: handoff
reachability_to_target: advances
artifact_role: theorem
next_trace_action: "Keep Axis-cover of M and O at t+1 displayed; do not write axis-cover into Admissibility, do not reduce to leftover-axis, do not replace cover by forall-perp, do not replace cover by exist-opposite of M or of O, do not reduce to a unique letter, do not use occupancy n, and do not attach L1."
conditional_surface_status: "exact on B_3(0) for Axis-cover of M and O at t+1 on the four #7168 x-probes, reverse hold and face hold; displayed, not adopted"
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

These are the nsuoxinc #7168 x-probes. These are not the y-probes `A=(0,1,0)`,
`B=(1,1,1)`, `C=(0,2,0)`, `D=(1,1,0)`. These are not the z-probes
`A=(0,0,1)`, `B=(1,1,1)`, `C=(0,0,2)`, `D=(1,0,1)`. `A` is not a seed. Same
process as nsopp #7093.

Lock alphabet of the displayed process: `{±e_i}` with `i` in `{1,2,3}`.

Seed: the two-record set `{0, (0,1,0)}` is recorded at formation tick 0 with
opposite locks `L(0)=+e_1` and `L(0,1,0)=−e_1`. This seed is not the perp
two-site seed `+e_1/+e_2`. This seed is not the z-symmetric three-site seed
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
Occupancy `n` is not used. O is not M.

Axis of a defined lock set is the unsigned lattice direction:

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
is full. Leftover-axis `{e_1,e_2,e_3}` minus that union is comparison only:
empty leftover with overlapping axes is not cover.

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
`M(q,t+1)=M(q,t)` at every scored probe. Outgoing is empty at `t` for
`A`, `B`, and `C`, then filled at `t+1`. This display reads `M` and `O`
together at the same cut `τ=t+1` and scores Axis and cover:

```text
t(A)=3
t(B)=2
t(C)=4
t(D)=3
M(A, τ) = {+e_2, +e_3, −e_3}
M(B, τ) = {+e_1}
M(C, τ) = {+e_1}
M(D, τ) = {−e_2, +e_3, −e_3}
O(A, τ) = {+e_1}
O(B, τ) = {+e_2, +e_3, −e_3}
O(C, τ) = {−e_2, +e_3, −e_3}
O(D, τ) = {+e_1, −e_1}
Axis(M(A, τ)) = {e_2, e_3}
Axis(O(A, τ)) = {e_1}
Axis(M(B, τ)) = {e_1}
Axis(O(B, τ)) = {e_2, e_3}
Axis(M(C, τ)) = {e_1}
Axis(O(C, τ)) = {e_2, e_3}
Axis(M(D, τ)) = {e_2, e_3}
Axis(O(D, τ)) = {e_1}
cover(A): hold
cover(B): hold
cover(C): hold
cover(D): hold
```

`A` is not a seed. Mixed remains a set: `M(A,τ)` has three earliest
incoming steps and `M(D,τ)` has three earliest incoming steps. Unique
letters would assign `UNDEFINED` at mixed probes and would leave reverse
and face `UNDEFINED`. Here uniqueness is not required. `M` and `O` are
disjoint at each of the four probes at `τ`. O is not M. Axis sets are
complementary partitions of `{e_1,e_2,e_3}` at each probe, so cover holds
at each probe.

Y-probe cover HOLDING on the same seed reports `t(A)=0`,
`M(A,τ)={−e_1}`, and cover hold at each y-probe. That leftover is a
different four-tuple. nsmopx #7217 own-incoming exist-opposite on these
same x-probes reports reverse fail and face fail from mixed `M(A)` against
singleton `M(B)`. Cover reverse holds while that leftover fails.

New records in `B_3(0)` between `t` and `t+1` that meet a probe's
six-neighbors enter `O` and do not enter earliest `M`:

```text
new 6-NN of A at t(A)+1: (2, 0, 0)
new 6-NN of B at t(B)+1: (1, 2, 1), (1, 1, 2), (1, 1, 0)
new 6-NN of C at t(C)+1: (2, -1, 0), (2, 0, 1), (2, 0, -1)
new 6-NN of D at t(D)+1: (2, 1, 0)
```

At `t`, `O(A,t)`, `O(B,t)`, and `O(C,t)` are empty, so cover at those
probes fails at `t` because the union is not `{e_1,e_2,e_3}`. Reverse at
`t` is `fail`. That empty-at-`t` leftover is not this display. Forall-perp
at those probes is `UNDEFINED` at `t` from empty `O`, so empty-at-`t`
already splits cover from forall-perp. Leftover-axis of `M` and `O` at
`τ` is empty at each probe; leftover-axis reverse fails from empty
leftover while cover holds. Exist-opposite of `M(A)` against `M(B)` fails
because `{+e_2, +e_3, −e_3}` is not opposite `{+e_1}` while cover at `A`
and at `B` holds. Exist-opposite of `O(A)` against `O(B)` likewise fails.

## Theorem 2 — reverse hold / fail / UNDEFINED

Reverse HOLD if and only if cover at `A` and at `B`. Both bits are
`hold`. Reverse holds. Both sides are nonempty and defined, so this is not
`UNDEFINED`. This is not `fail`.

Reverse: hold

Reverse holds. Unique-letter leftover reports reverse `UNDEFINED` from mixed
`M(A,τ)`. Leftover-axis leftover reports reverse `fail` from empty leftover
at `A` and at `B`. Exist-opposite of `M` leftover reports reverse fail from
mixed `M(A)` against singleton `M(B)`. Exist-opposite of `O` leftover
reports reverse fail from `{+e_1}` against `{+e_2, +e_3, −e_3}`. Reverse
HOLD uses cover at `A` and at `B`. Y-probe cover HOLDING on the same seed
also reports reverse hold, but `M(A)` there is the seed letter `{−e_1}`,
not the mixed three-element set.

Reverse holds.

## Theorem 3 — face hold / fail / UNDEFINED

Face HOLD if and only if cover at `C` and at `D`. Both bits are
`hold`. Face holds. Mixed `M(D,τ)` remains a three-element set and
`Axis(M(D,τ))={e_2,e_3}` is disjoint from `Axis(O(D,τ))={e_1}` with full
union.

Face: hold

Displayed, not adopted. The bits are not written into Admissibility.
Do not write into Admissibility. Do not attach L1.

This is not `fail` and not `UNDEFINED`. Face holds. Unique-letter leftover
reports face `UNDEFINED` from mixed `M(D,τ)`. Leftover-axis leftover
reports face `fail` from empty leftover. Exist-opposite of `M` leftover
reports face fail from `{+e_1}` against `{−e_2, +e_3, −e_3}`. Exist-opposite
of `O` leftover reports face fail from `{−e_2, +e_3, −e_3}` against
`{+e_1, −e_1}`. Face already holds at `τ=t+1` from cover at `C` and at `D`.

Face holds.

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
- It does not reprint leftover-axis as the scored predicate.
- It does not reprint forall-perp as the scored predicate.
- It does not reprint exist-opposite of `M` as this display.
- It does not reprint exist-opposite of `O` as this display.
- It does not use occupancy `n`.
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
opposite-lock two-site process, the own incoming and outgoing sets
at `t+1`, the Axis sets, and the axis-cover reverse/face bits are
displayed theorem-domain data.

## Exact target and obligation graph

| Obligation | Status |
|---|---|
| current Lattice / Admissibility / Record premises | quoted; no edit |
| perp-step incoming-lock process on `B_3(0)` | displayed; nsopp #7093 seed `+e_1/−e_1` |
| ticks `t(A)`, `t(B)`, `t(C)`, `t(D)` | Theorem 1; `3`, `2`, `4`, `3` |
| `M` at `τ=t+1` | Theorem 1; frozen equal to `M` at `t` |
| `O` at `τ=t+1` | Theorem 1; outgoing dual |
| `Axis(M)` and `Axis(O)` at each probe | Theorem 1; complementary partitions of `{e_1,e_2,e_3}` |
| cover at `A,B,C,D` | Theorem 1; `hold` at each |
| reverse and face from cover | Theorems 2–3; `hold` / `hold` |
| unique incoming or outgoing lock | not required |
| occupancy `n` as the letter | not used |
| named-sign `{+,−}` letter | not used; lost the axis |
| singleton unique lock-vector letter | not used as the object; mixed remains a set |
| `Z^3` sum of the lock set | not used; no aggregation |
| occupancy-kernel inner product | not used |
| leftover of leftover-axis | not this display; empty leftover fails leftover-axis reverse |
| leftover of forall-perp | not this display; empty `O` at `t` splits the predicates |
| leftover of exist-opposite of M | not this display; nsmopx #7217 reverse fail face fail |
| leftover of exist-opposite of O | not this display |
| six-neighbor star as the letter | not used |
| y-probe cover HOLDING on the same seed | discriminator; different four-tuple; same hold/hold |
| axis-cover as Admissibility content | not adopted |
| formation site / probability / rate | open |
| physical Record readout of the bits | open |

## Value gate (V1–V5)

| # | Answer |
|---|---|
| V1 | It answers the first-display question: Axis-cover of `M` and `O` at `t+1` on the four #7168 x-probes, and reverse/face from that. |
| V2 | Current main has no landed Axis-cover of `M` and `O` reverse/face report on these four #7168 x-probes. |
| V3 | Incoming sets, outgoing sets, Axis sets, cover bits, and the `hold`/`hold` reports are independently finite and exact. |
| V4 | The theorem is more than a restatement of Record because it reads own incoming and own outgoing at the same `t+1` cut and scores disjoint full Axis cover. |
| V5 | It is not an adopted content rule: the bits remain displayed. |

## No-go discipline gate

The negative content is narrow: the display does not write those bits into
Admissibility, does not reduce them to named signs, does not require a
unique letter, does not replace `O` by `M`, does not replace cover by
leftover-axis, does not replace cover by forall-perp, does not replace
cover by exist-opposite of `M` or of `O`, does not use a six-neighbor
star, and does not use occupancy `n`. No global impossibility is claimed.

### N1 — materially distinct routes

| Route | Attempt | Why it fails here | Marker |
|---|---|---|---|
| leftover-axis | score equality of nonempty `{e_1,e_2,e_3}` minus `Axis(M)∪Axis(O)` | leftover is empty at each probe so leftover-axis reverse fails while cover holds | ATTEMPTED |
| leftover of `M` alone | score `{e_1,e_2,e_3}` minus `Axis(M)` | leftover of `M` at `A` is `{e_1}` and at `B` is `{e_2,e_3}`; reverse would fail | ATTEMPTED |
| leftover of `O` alone | score `{e_1,e_2,e_3}` minus `Axis(O)` | leftover of `O` at `A` is `{e_2,e_3}` and at `B` is `{e_1}`; reverse would fail | ATTEMPTED |
| forall-perp | score every pair `m·o=0` | leftover; empty `O` at `t` makes forall-perp `UNDEFINED` while cover fails; this cut is `τ=t+1` | ATTEMPTED |
| exist-opposite of M | score `a+b=0` inside `M(A)` and `M(B)` | leftover; nsmopx #7217 reverse fail face fail while cover holds | ATTEMPTED |
| exist-opposite of O | score `a+b=0` inside `O(A)` and `O(B)` | leftover; reverse of `O` fails from `{+e_1}` against `{+e_2, +e_3, −e_3}` | ATTEMPTED |
| unique letter | replace mixed sets by a singleton or `UNDEFINED` | mixed `M(A,τ)` and mixed `M(D,τ)` remain sets; unique-letter reverse and face are `UNDEFINED` | ATTEMPTED |
| empty `O` at `t` | score cover at formation tick | `O(A,t)` is empty so reverse at `t` is `fail`; this cut is `τ=t+1` | ATTEMPTED |
| y-probes on the same process | score `A=(0,1,0)`, `C=(0,2,0)` | leftover; y-probe cover HOLDING, but `M(A)` is `{−e_1}` not `{+e_2, +e_3, −e_3}` | ATTEMPTED |
| z-probes on the same process | score `A=(0,0,1)`, `C=(0,0,2)` | leftover; `M(A)` is a seed letter on z, not the mixed x-probe set | ATTEMPTED |
| perp two-site seed | replace the opposite seed | leftover; `M(A)` differs | ATTEMPTED |
| six-neighbor lock union | score locks of six-neighbors formed by `t(q)` | this display does not use a six-neighbor star; nsuoxinc #7168 leftover HOLDs reverse from that star | ATTEMPTED |
| sum of a set | replace each set by its `Z^3` sum | the construction does not sum; sum of mixed `M(A,τ)` cancels to `+e_2` while the set stays three-element | ATTEMPTED |
| named-sign lettering | collapse `{±e_i}` to `{+,−}` | named-sign lettering lost the axis | ATTEMPTED |
| occupancy-kernel inner product | score a signed occupancy product | different object; not an occupancy-kernel inner product | ATTEMPTED |
| global later T | wait until `max t(A,B,C,D)` before reading | `τ(q)=t(q)+1` is per-probe; no global T | ATTEMPTED |
| attach a formation member from already-recorded six-neighbor locks | form the probes by a neighbor-lock letter instead of perp-step | refused; not attached | ATTEMPTED |
| adopt bits into Admissibility | rewrite the local rule by axis-cover | refused; displayed, not adopted | ATTEMPTED |

### N2 — wall independence

Missing physical adoption, missing identification of cover with leftover-axis,
missing identification of cover with forall-perp, missing identification of
cover with exist-opposite of `M` or of `O`, and missing Record identification
of axis-cover are distinct open premises. This note claims no complete wall
collection.

### N3 — hidden-condition scan

The host `B_3(0)`, two-site seed locks `+e_1` and `−e_1`, perpendicular step
rule, incoming-step lock, own incoming set and own outgoing dual from
records with tick `<= τ`, per-probe `τ=t+1`, Axis of signed locks, cover as
disjoint full union of `{e_1,e_2,e_3}`, four x-probes with non-seed `A`, empty
or `UNDEFINED` as declared, and mixed remains a set are declared. No
uniqueness of locks, no six-neighbor star as the scored object, no leftover-axis
as the scored predicate, no forall-perp as the scored predicate, no
exist-opposite of `M` or of `O` as the scored predicate, no global later T,
no formation attachment from already-recorded six-neighbor locks, and no
Admissibility rewrite are silently assumed.

### N4 — source residual matching

The current axiom memo supplies cubic sites, `M_2(C)`,
content-conditional-on-formation, and unreadable absence. The residual that
formation site, probability, and rate remain unsupplied is unchanged. The
cover `hold`/`hold` reports do not close that residual.

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

**Steelman:** Axis-cover of `M` versus `O` is only leftover-axis because the
leftover is empty; it is only forall-perp because disjoint axes already
force every pair to dot to zero; it is only y-probe cover HOLDING on the
same seed; mixed `A` should make reverse `UNDEFINED`; empty `O` at `t`
should make reverse `UNDEFINED`; and nsmopx already answered these x-probes
by exist-opposite of `M`.

**Answer:** Leftover-axis reverse fails from empty leftover while cover
holds. Forall-perp is comparison only. Empty `O` at `t` makes forall-perp
`UNDEFINED` while cover fails. Y-probes are a different four-tuple;
`M(A)` there is `{−e_1}`, not `{+e_2, +e_3, −e_3}`. Mixed `M(A,τ)` remains
a three-element set and reverse holds. Empty `O` at `t` makes reverse `fail`
at that leftover cut; this display scores `τ=t+1`. nsmopx #7217 exist-opposite
of `M` reports reverse fail and face fail; cover reports reverse hold and
face hold.

### N8 — cross-cycle echo

nsuoxinc #7168 reported reverse hold from same-tick-inclusive six-neighbor
locks union own incoming lock. nsmopx #7217 reported reverse fail and face
fail from own incoming `M`. Y-probe cover HOLDING on the same seed reports
cover hold, reverse hold, and face hold on `A=(0,1,0)` and `C=(0,2,0)`.
This note is not those displays: it reports Axis-cover of `M` versus `O`
at `τ=t+1` on the four #7168 x-probes, complementary Axis partitions,
reverse hold, and face hold. Discriminator versus y-probe cover HOLDING:
same hold/hold, different probes, and exist-opposite of `M` fails here.

**Gate disposition:** PASS for the Axis-cover of `M` vs `O` at `t+1`
reverse/face reports above. FAIL / DO NOT SHIP for “the predicate equals the
named sign,” “the predicate equals the unique singleton lock vector,” “the
predicate equals leftover-axis,” “the predicate equals forall-perp,” “the
predicate equals exist-opposite of `M`,” “the predicate equals exist-opposite
of `O`,” “bits are Admissibility,” “cover fails at `A`,” “reverse fails,”
“face is `UNDEFINED`,” or “`O` is `M`.”

## Primary runner

The paired runner builds Euclidean `B_3(0)`, runs the nsopp #7093 perp-step
incoming-lock process, reads each probe's own earliest incoming
set and own outgoing dual from the record prefix at that probe's `t+1`,
reports Axis sets and cover at `A,B,C,D`, lists new records in `B_3(0)`
between `t` and `t+1` that meet a probe's six-neighbors, and checks
Theorems 1--3. It also checks that `M` is frozen from `t` to `t+1`, that
`O` is empty at `t` for `A`, `B`, and `C` so cover fails at that leftover
cut, that mixed sets remain sets, that unique-letter reverse and face are
`UNDEFINED`, that leftover-axis reverse fails from empty leftover, that
forall-perp at `t` is `UNDEFINED` while cover at `t` fails, that
exist-opposite of `M` fails while cover holds, that y-probe cover HOLDING
on the same seed is a different four-tuple, that the construction does not
sum, that a formation member from already-recorded six-neighbor locks is
not attached, and that occupancy is not used. No runner cache is written.
