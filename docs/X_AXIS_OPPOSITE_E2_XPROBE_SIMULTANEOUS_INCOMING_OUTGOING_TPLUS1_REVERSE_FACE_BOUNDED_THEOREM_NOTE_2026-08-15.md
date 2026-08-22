---
claim_id: x_axis_opposite_e2_xprobe_simultaneous_incoming_outgoing_tplus1_reverse_face_bounded_theorem_note_2026-08-15
claim_type: bounded_theorem
claim_scope: "Simultaneous M and O at t+1 on the four #7214 x-probes, intersection, and reverse/face of each are reported. Displayed, not adopted."
upstream_dependencies:
  - minimal_axioms
runner: scripts/x_axis_opposite_e2_xprobe_simultaneous_incoming_outgoing_tplus1_reverse_face_2026_08_15.py
---

# Simultaneous Incoming And Outgoing At T Plus One On Four #7214 X-Probes

> **Key terms used in this doc** are indexed A-Z at `docs/KEY_TERMINOLOGY.md`;
> each row points to the canonical source-of-truth doc.

**Date:** 2026-08-15
**Type:** bounded_theorem
**Scope:** simultaneous own incoming set `M` and own outgoing dual `O` at
each probe's `τ=t+1` on the four nmxe2x #7214 x-probes in
`B_3(0)={n:n·n<=9}`. Same process and x-probes as nmxe2x #7214. Let
`t(q)` be the formation tick of probe `q`. Let `τ(q)=t(q)+1`. `M(q,τ)` is
the set of earliest incoming nearest-neighbor steps at `q` using only
records with tick `<= τ`. Seeds use their seed letter as a singleton.
Unformed at `τ` is `UNDEFINED`. `O(q,τ)` is the outgoing dual of `M`: the
set of `e` in `{±e_1,±e_2,±e_3}` such that `q+e` is formed in `B_3(0)` and
`e` is in `M(q+e,τ)`. Unformed `q` at `τ` is `UNDEFINED`. Empty `O` is
empty, not `UNDEFINED`. Report `M`, `O`, and `M ∩ O` at `τ`. Reverse and
face from `M` at `τ`. Reverse and face from `O` at `τ`. Reverse holds if
and only if some lock in the `A` set is the vector opposite of some lock
in the `B` set. Face holds if and only if some lock in the `C` set is the
vector opposite of some lock in the `D` set. Empty or `UNDEFINED` on
either side of a comparison is `UNDEFINED`; nonempty with no opposite pair
fails. Unique `L` is not the object. Occupancy `n` is not used. This is
not named-sign lettering. This is not a unique lock-vector leftover and
not a sum leftover. This is not leftover of unique-L, which is
`UNDEFINED` when mixed. This is not leftover of nmxe2x M-only, which
reports `M` at formation without `O`. This is not leftover of O at t,
which leaves reverse and face `UNDEFINED` from empty `O` at `A`, `B`, and
`C`. This is not leftover of nmot2x2 O two-tick composition. This is not
leftover of nmt2x2 `M` two-tick. This is not leftover of the x-symmetric
three-site seed. The construction does not use a six-neighbor star.
Uniqueness of incoming or outgoing locks is not required. Displayed, not
adopted. Do not write into Admissibility. Do not attach L1. This note
does not write existential opposite into Admissibility and does not
attach a formation member from already-recorded six-neighbor locks. This
display does not use occupancy. Mixed stays a set. O is not M.
**Audit-status authority:** independent audit lane only. This note authors no
audit verdict and predicts none.
**Primary runner:**
[`scripts/x_axis_opposite_e2_xprobe_simultaneous_incoming_outgoing_tplus1_reverse_face_2026_08_15.py`](../scripts/x_axis_opposite_e2_xprobe_simultaneous_incoming_outgoing_tplus1_reverse_face_2026_08_15.py)

Framework input:

- [`MINIMAL_AXIOMS_2026-06-29.md`](MINIMAL_AXIOMS_2026-06-29.md) supplies
  cubic-lattice sites `Z^3` with nearest-neighbor adjacency, the one-site
  algebra `M_2(C)`, and the Record sentences that records form and that a
  present record locks exactly one admissible local possibility.

Everything after that quoted input is a finite displayed process on `B_3(0)`
and the four named x-probes. Incoming lock letters are unit nearest-neighbor
steps. `O` is the outgoing dual of those incoming sets at a per-probe cut
`τ=t+1`. Reverse and face are scored on existence of an opposite pair in
`M` at `τ` and, separately, in `O` at `τ`. Named signs `{+,−}` are a
coarser readout and are not used. A singleton unique lock-vector letter is
a different readout and is not used as the object: report `M` and `O`. A
`Z^3` sum of those locks is a different readout and is not used. The
construction does not sum. Occupancy `n` is not used.

## Machine status and trace

```yaml
actual_current_surface_status: bounded-support
target_claim_type: bounded_theorem
claim_type_reason: "Exact report of simultaneous M and O at t+1 on the four #7214 x-probes, with empty intersection, reverse hold and face hold from M, and reverse hold and face hold from O; uniqueness of incoming or outgoing locks is not claimed and the bits are not adopted."
trace_class: frontier_discovery
target_claim_id: x_axis_opposite_e2_xprobe_simultaneous_incoming_outgoing_tplus1_reverse_face
target_blocker_text: "display simultaneous M and O at t+1 on the four #7214 x-probes, intersection, and reverse/face of each, or UNDEFINED"
source_of_blocker_text: handoff
reachability_to_target: advances
artifact_role: theorem
next_trace_action: "Keep M, O, intersection, and reverse/face displayed; do not write existential opposite into Admissibility, do not reduce to named sign, do not require a singleton lock vector, do not sum the lock set, do not use occupancy n, do not identify the sets with unique-L leftover, do not identify the report with nmxe2x M-only, do not identify the report with O at t, do not identify the report with nmot2x2 O two-tick, and do not replace O by M."
conditional_surface_status: "exact on B_3(0) for simultaneous M and O at t+1 on the four #7214 x-probes; displayed, not adopted"
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
incoming sets and outgoing duals are scored:

```text
A = (1,0,0),  B = (1,1,1),  C = (2,0,0),  D = (1,1,0).
```

These are the nsopp x-probes. These are not the y-probes `A=(0,1,0)`,
`B=(1,1,1)`, `C=(0,2,0)`, `D=(1,1,0)`. These are not the z-probes
`A=(0,0,1)`, `B=(1,1,1)`, `C=(0,0,2)`, `D=(1,0,1)`. `A` is a seed. Same
process and x-probes as nmxe2x #7214.

Lock alphabet of the displayed process: `{±e_i}` with `i` in `{1,2,3}`.

Seed: the two-record set `{0, (1,0,0)}` is recorded at formation tick 0 with
opposite locks `L(0)=+e_2` and `L(1,0,0)=−e_2`. This seed is not the
same-lock two-site seed `+e_2/+e_2`. This seed is not the nspar two-site
seed `+e_1/−e_1`. This seed is not the x-axis opposite ±e_3 two-site seed
`+e_3/−e_3`. This seed is not the x-symmetric three-site seed
`{0,(1,0,0),(-1,0,0)}`.

From a recorded site `p` with lock `L_in(p)=±e_i`, a six-neighbor step
`s in NN` to `q=p+s` is allowed if and only if `s` is perpendicular to
`e_i`, that is

```text
s · e_i = 0.
```

If `q` lies in `B_3(0)`, is still unformed, and the step is allowed, then `q`
forms next and locks the incoming step `s`. If several allowed parents reach
`q` at the same earliest formation, each such incoming step is kept as a
possible lock. Mixed stays a set. Uniqueness is not required. A later parent
does not re-form `q`.

## Named simultaneous `M` and `O` at `τ=t+1`

Let `t(q)` be the formation tick of x-probe `q` when that tick is defined in
`B_3(0)`. Let `τ(q)=t(q)+1`. There is no global later T.

`M(q,τ)` is the set of earliest incoming nearest-neighbor steps at `q`
using only records with tick `<= τ`. If `q` is unformed at `τ`, then
`M(q,τ)` is `UNDEFINED`. If `q` is a seed and `τ >= 0`, then `M(q,τ)` is
the singleton seed letter. Mixed stays a set. Duplicate incoming steps
collapse in the set. The construction does not require `M(q,τ)` to be a
singleton. It does not sum `M(q,τ)`. Occupancy `n` is not used. Unique
`L(q)` is not used as the letter. This display does not use a six-neighbor
star.

`O(q,τ)` is the outgoing dual of `M`:

```text
O(q,τ) = { e in {±e_1,±e_2,±e_3} | q+e formed in B_3(0) and e in M(q+e,τ) }.
```

If `q` is unformed at `τ`, then `O(q,τ)` is `UNDEFINED`. Empty `O` is empty,
not `UNDEFINED`. Duplicate outgoing steps collapse in the set. The
construction does not require `O(q,τ)` to be a singleton. It does not sum
`O(q,τ)`. It does not replace `O` by `M`. O is not M.

The intersection at the same cut is `M(q,τ) ∩ O(q,τ)`. If either side is
`UNDEFINED`, the intersection is `UNDEFINED`. Empty intersection is empty,
not `UNDEFINED`.

Identifying a named sign of those locks with reverse or face is refused:
named-sign lettering lost the axis. Reverse and face are scored on existence
of a pair of lock vectors that add to zero. They are not scored on `{+,−}`
names and are not an occupancy-kernel inner product.

Reverse and face from `M` at `τ` (displayed):

```text
reverse from M  <=>  some a in M(A,τ) and some b in M(B,τ) with a+b=(0,0,0)
face from M     <=>  some c in M(C,τ) and some d in M(D,τ) with c+d=(0,0,0)
```

Reverse and face from `O` at `τ` (displayed):

```text
reverse from O  <=>  some a in O(A,τ) and some b in O(B,τ) with a+b=(0,0,0)
face from O     <=>  some c in O(C,τ) and some d in O(D,τ) with c+d=(0,0,0)
```

If either side of a comparison is empty or `UNDEFINED`, that bit is
`UNDEFINED`. Else the bit fails if no such pair exists. The report is one
of `hold`, `fail`, or `UNDEFINED`.

Admissibility is not edited. Existential opposite is not written into
Admissibility. Do not write into Admissibility. Do not attach L1.

## Theorem 1 — formation ticks, `M`, `O`, and intersection at `τ=t+1`

Direct enumeration of the displayed x-axis opposite ±e_2 process on `B_3(0)`
forms all four x-probes. The formation ticks are `t(A)=0`, `t(B)=2`,
`t(C)=1`, `t(D)=3`. `A` is a seed. Those ticks locate the per-probe cut
`τ=t+1`. They are not occupancy kernels and are not a global later T.

Own incoming sets, outgoing duals, and intersections at `τ=t+1` are:

```text
A: seed letter −e_2;
   t(A)=0;  M(A, τ) = {−e_2}
            O(A, τ) = {+e_1, +e_3, −e_3}
            (M ∩ O)(A, τ) = {}
B: incoming +e_2;
   t(B)=2;  M(B, τ) = {+e_2}
            O(B, τ) = {+e_1, +e_3, −e_3}
            (M ∩ O)(B, τ) = {}
C: incoming +e_1;
   t(C)=1;  M(C, τ) = {+e_1}
            O(C, τ) = {+e_2, −e_2, +e_3, −e_3}
            (M ∩ O)(C, τ) = {}
D: incoming −e_1, −e_3, +e_3;
   t(D)=3;  M(D, τ) = {−e_1, +e_3, −e_3}
            O(D, τ) = {+e_2, −e_2}
            (M ∩ O)(D, τ) = {}
```

`A` is a seed at tick 0. Mixed stays a set: `M(D,τ)` has three earliest
incoming steps `−e_1`, `−e_3`, and `+e_3`, and `O(A,τ)` has three outgoing
steps `+e_1`, `+e_3`, and `−e_3`. Unique-L leftover would assign
`UNDEFINED` from those mixes. Here uniqueness is not required.

`M` is frozen from formation to `t+1`: `M(q,t+1)=M(q,t)` at every scored
probe, matching nmxe2x HOLDING `M`. `O` is not frozen from `t`:
`O(A,t)={}`, `O(B,t)={}`, `O(C,t)={}`, `O(D,t)={−e_2}`. Empty `O` at `t`
for `A`, `B`, and `C` is empty, not `UNDEFINED`. New six-neighbor records
at `t+1` enter `O`:

```text
new 6-NN of A at t(A)+1: (2, 0, 0), (1, 0, 1), (1, 0, -1)
new 6-NN of B at t(B)+1: (2, 1, 1), (1, 1, 2), (1, 1, 0)
new 6-NN of C at t(C)+1: (2, 1, 0), (2, -1, 0), (2, 0, 1), (2, 0, -1)
new 6-NN of D at t(D)+1: (1, 2, 0)
```

`M` and `O` are disjoint at each of the four probes at `τ`. O is not M.
The own-incoming letters that HOLD reverse of nmxe2x, `−e_2` in `M(A)`
against `+e_2` in `M(B)`, are absent from `O(A,τ)` and `O(B,τ)`. The
own-outgoing opposite pair is `+e_3` against `−e_3` at reverse and `+e_2`
against `−e_2` at face.

This is not leftover of nmxe2x M-only: that leftover reports `M` at
formation without a simultaneous `O` cut. This is not leftover of O at t:
that leftover leaves reverse and face `UNDEFINED` from empty `O`. This is
not leftover of unique-L. This is not leftover of nmot2x2 O two-tick:
that leftover reports reverse `UNDEFINED` then hold and face `UNDEFINED`
then hold with composition fail, and omits simultaneous `M`. This is not
leftover of nmt2x2 `M` two-tick: that leftover reports `M(τ1)=M(τ0)` with
HOLD/HOLD and omits `O`. This is not leftover of the x-symmetric
three-site seed: that leftover records `(-1,0,0)` at tick 0.

Incoming and outgoing locks exist and need not be unique. That
non-uniqueness does not empty the sets. Uniqueness is not required.

## Theorem 2 — reverse and face from `M` at `τ`

Reverse from `M` holds if and only if there exist `a` in `M(A,τ)` and `b`
in `M(B,τ)` with `a+b=(0,0,0)`. Both sets are nonempty: `M(A,τ)={−e_2}`
and `M(B,τ)={+e_2}`, so `−e_2+(+e_2)=(0,0,0)`. Reverse from M holds.
Reverse HOLD uses a singleton `M(A)`.

Reverse from M: hold

This is not `fail` and not `UNDEFINED`. Reverse from M holds.

Face from `M` holds if and only if there exist `c` in `M(C,τ)` and `d` in
`M(D,τ)` with `c+d=(0,0,0)`. Both sets are nonempty: `M(C,τ)={+e_1}` and
`M(D,τ)={−e_1, +e_3, −e_3}`, so `+e_1+(−e_1)=(0,0,0)`. Face from M holds.

Face from M: hold

This is not `fail` and not `UNDEFINED`. Face from M holds. Unique-L leftover
reports face `UNDEFINED` from mixed `D`. Hold of face from `M` at mixed `D`
is the discriminator against unique-L. Reverse from M holds. Face from M
holds.

## Theorem 3 — reverse and face from `O` at `τ`

Reverse from `O` holds if and only if there exist `a` in `O(A,τ)` and `b`
in `O(B,τ)` with `a+b=(0,0,0)`. Both sets are nonempty:
`O(A,τ)={+e_1, +e_3, −e_3}` and `O(B,τ)={+e_1, +e_3, −e_3}`, so
`+e_3+(−e_3)=(0,0,0)`. Reverse from O holds.

Reverse from O: hold

Face from `O` holds if and only if there exist `c` in `O(C,τ)` and `d` in
`O(D,τ)` with `c+d=(0,0,0)`. Both sets are nonempty:
`O(C,τ)={+e_2, −e_2, +e_3, −e_3}` and `O(D,τ)={+e_2, −e_2}`, so
`+e_2+(−e_2)=(0,0,0)`. Face from O holds.

Face from O: hold

Displayed, not adopted. The bits are not written into Admissibility.
Do not write into Admissibility. Do not attach L1.

This is not `fail` and not `UNDEFINED`. Unique own-outgoing letters report
reverse `UNDEFINED` and face `UNDEFINED` from mixed `O`. O at t leftover
reports reverse `UNDEFINED` and face `UNDEFINED` from empty `O` at `A`,
`B`, and `C`. Eventual-`O` leftover already reports the `τ` outgoing sets
with no simultaneous `M` and no empty-at-`t` cut. nmot2x2 leftover reports
those `O` bits as a two-tick composition without simultaneous `M`. Those
are different objects. Reverse from O holds because a pair from `O(A,τ)`
and `O(B,τ)` is opposite. Face from O holds.

Face from O holds.

## What this note does not claim

- It does not select a unique incoming lock or a unique outgoing lock.
- It does not reduce lock vectors to named signs `{+,−}`.
- It does not require the own incoming set or the outgoing dual to be a
  singleton.
- It does not sum the own incoming set or the outgoing dual.
- It does not use occupancy `n`.
- It does not score reverse or face as an occupancy-kernel inner product.
- It does not attach a formation member from already-recorded six-neighbor
  locks.
- It does not census a sixteen-combination free lettering independent of
  lock vectors.
- It does not reprint unique-L letters on these x-probes as the object.
- It does not reprint nmxe2x M-only as the whole report.
- It does not reprint O at t `UNDEFINED`/`UNDEFINED` as this cut.
- It does not reprint nmot2x2 O two-tick composition as this cut.
- It does not reprint nmt2x2 `M` two-tick as this cut.
- It does not replace `O` by `M`.
- It does not use a six-neighbor star as the letter.
- It does not wait for a global later T.
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
x-axis opposite ±e_2 two-site process, the own incoming sets, the outgoing
duals at `t+1`, the intersections, and the reverse/face predicates are
displayed theorem-domain data.

## Exact target and obligation graph

| Obligation | Status |
|---|---|
| current Lattice / Admissibility / Record premises | quoted; no edit |
| perp-step incoming-lock process on `B_3(0)` | displayed; x-axis opposite ±e_2 seed `+e_2/−e_2` |
| ticks `t(A)`, `t(B)`, `t(C)`, `t(D)` | Theorem 1; `0`, `2`, `1`, `3` |
| `M` at `τ=t+1` | Theorem 1; `{−e_2}`, `{+e_2}`, `{+e_1}`, `{−e_1, +e_3, −e_3}` |
| `O` at `τ=t+1` | Theorem 1; `{+e_1, +e_3, −e_3}`, `{+e_1, +e_3, −e_3}`, `{+e_2, −e_2, +e_3, −e_3}`, `{+e_2, −e_2}` |
| `M ∩ O` at `τ` | Theorem 1; empty at each probe |
| reverse and face from `M` at `τ` | Theorem 2; `hold` / `hold` |
| reverse and face from `O` at `τ` | Theorem 3; `hold` / `hold` |
| unique incoming or outgoing lock | not required |
| occupancy `n` as the letter | not used |
| named-sign `{+,−}` letter | not used; lost the axis |
| singleton unique lock-vector letter | not used as the object; mixed stays a set |
| `Z^3` sum of the lock set | not used; no aggregation |
| occupancy-kernel inner product | not used |
| formation member from already-recorded six-neighbor locks | not attached |
| leftover of unique-L | not this display |
| leftover of nmxe2x M-only | not this display |
| leftover of O at t | not this display |
| leftover of nmot2x2 O two-tick | not this display |
| leftover of nmt2x2 `M` two-tick | not this display |
| six-neighbor star as the letter | not used |
| existential opposite as Admissibility content | not adopted |
| formation site / probability / rate | open |
| physical Record readout of the bits | open |

## Value gate (V1–V5)

| # | Answer |
|---|---|
| V1 | It answers the first-display question: simultaneous `M` and `O` at `t+1` on the four #7214 x-probes, intersection, reverse/face of each, or `UNDEFINED`. |
| V2 | Current main has no landed simultaneous incoming/outgoing `t+1` reverse/face report on these four #7214 x-probes. |
| V3 | The sets, the empty intersections, and the `hold` reports are independently finite and exact. |
| V4 | The theorem is more than a restatement of Record because it reads the probe's own incoming set and outgoing dual at `t+1` and scores existence of an opposite pair in each. |
| V5 | It is not an adopted content rule: the bits remain displayed. |

## No-go discipline gate

The negative content is narrow: the display does not write those bits into
Admissibility, does not reduce them to named signs, does not require a
singleton lock vector, does not sum the lock set, does not reprint unique-L,
does not reprint nmxe2x M-only as the whole report, does not reprint O at t,
does not reprint nmot2x2 O two-tick, does not use a six-neighbor star, does
not replace `O` by `M`, and does not use occupancy `n`. No global
impossibility is claimed.

### N1 — materially distinct routes

| Route | Attack | Result |
|---|---|---|
| unique-L leftover | require a singleton `{v}` subset `{±e_i}` else `UNDEFINED` | refused; leftover; face from `M` would be `UNDEFINED` when mixed while `M(D,τ)` is nonempty and face from `M` holds; reverse and face from `O` would be `UNDEFINED` from mixed `O` |
| nmxe2x M-only | report `M` at formation without simultaneous `O` | refused; leftover; that readout HOLDs reverse and face from `M` and omits `O`, intersection, and reverse/face from `O` |
| O at t | score outgoing dual at formation instead of `t+1` | refused; leftover; empty `O` at `A`, `B`, and `C` makes reverse and face `UNDEFINED` |
| nmot2x2 O two-tick | score `O` at `t` versus `t+1` without simultaneous `M` | refused; leftover; that readout reports reverse `UNDEFINED` then hold, face `UNDEFINED` then hold, composition fail, and omits `M` |
| nmt2x2 `M` two-tick | score frozen `M` at `t` and `t+1` without `O` | refused; leftover; that readout HOLDs reverse and face at both cuts and omits `O` |
| eventual-`O` without `M` | read neighbor locks after children exist, no simultaneous `M` | refused; leftover; that readout already reports the `τ` outgoing sets and hides that `M` is disjoint |
| six-neighbor lock union | score locks of six-neighbors formed by `τ` | refused; leftover; that readout includes `+e_2` at `A` from the origin partner, which is absent from `O(A,τ)` |
| sum of the same sets | replace `M` or `O` by the `Z^3` sum | refused; leftover; the construction does not sum; sum of mixed `M(D,τ)` cancels to `−e_1` while `M(D,τ)` stays a three-element set |
| unique letter of occupancy `n` | assign one letter from occupancy `n` | different object; occupancy `n` is not used |
| occupancy-kernel inner product | score `n(A)·n(B)<0` and `n(C)·n(D)<0` | different object; not an occupancy-kernel inner product |
| reverse/face from formation-tick inequalities | score probes by formation order | different object; ticks locate `τ` and are not the predicate |
| attach a formation member from already-recorded six-neighbor locks | form the probes by a neighbor-lock letter instead of perp-step | refused; not attached |
| adopt bits into Admissibility | rewrite the local rule by existential opposite | refused; displayed, not adopted |
| unique incoming lock required | demand one incoming or outgoing step per probe | uniqueness is not required; mixed stays a set |
| replace `O` by `M` | identify the outgoing dual with earliest incoming | refused; O is not M; the intersection is empty at each probe |
| x-symmetric three-site seed | add `(-1,0,0)` as a third seed | leftover; that seed records three sites at tick 0 |
| y-probes on the same process | score `A=(0,1,0)`, `C=(0,2,0)` | leftover; reverse from `M` fails and face from `M` fails from mixed `M` |
| z-probes on the same process | score `A=(0,0,1)`, `C=(0,0,2)` | leftover; reverse from `M` fails and face from `M` fails |
| same-lock `+e_2/+e_2` on these x-probes | replace the opposite seed | leftover; reverse from `M` fails |
| nspar `+e_1/−e_1` on these x-probes | replace the opposite seed | leftover; reverse from `M` fails |
| x-axis opposite ±e_3 on these x-probes | replace the seed axis | leftover; reverse from `M` holds and face from `M` fails |

### N2 — wall independence

Missing physical adoption, missing identification of `O` with `M`, and
missing Record identification of existential opposite are distinct open
premises. This note claims no complete wall collection.

### N3 — hidden-condition scan

The host `B_3(0)`, two-site seed locks `+e_2` and `−e_2`, perpendicular step
rule, incoming-step lock, own incoming set of earliest nearest-neighbor
steps from records with tick `<= τ`, outgoing dual of that set, mixed stays
a set, existential opposite, four x-probes with seed `A`, per-probe
`τ=t+1`, empty `O` empty not `UNDEFINED`, and reverse/face as existence of
a pair that sums to zero are declared. No uniqueness of incoming or
outgoing locks, no occupancy `n`, no named-sign reduction, no singleton
leftover as the object, no sum leftover, no unique-L leftover, no nmxe2x
M-only leftover, no O at t leftover, no nmot2x2 leftover, no six-neighbor
star as the letter, no global later T, no formation attachment from
already-recorded six-neighbor locks, and no Admissibility rewrite are
silently assumed.

### N4 — source residual matching

The current axiom memo supplies cubic sites, `M_2(C)`,
content-conditional-on-formation, and unreadable absence. The residual that
formation site, probability, and rate remain unsupplied is unchanged. The
`hold` reports do not close that residual.

### N5 — resolution and rhetoric audit

| Resolution | Executed | Not claimed |
|---|---|---|
| per element | each lock vector in an own incoming set or outgoing dual | no continuum alphabet |
| per site | `A,B,C,D` x-probes on `B_3(0)` only | no other cubic sites |
| per mode | no mode calculation | no spectral exhaustion |
| per block | four `M` sets, four `O` sets, four intersections, reverse/face of each | no adopted content law |
| lattice wide | checked and not executed | no lattice-wide lettering rule |

### N6 — live partial-closure paths

Live routes include a later Record content map for reverse/face, a
formation-rate rule, and a physical selector among `{±e_i}`. None is taken
here.

### N7 — hostile steelman

**Steelman:** Simultaneous `M` and `O` is leftover of nmxe2x because
`M` is already HOLDING at formation, leftover of O at t because children
will exist, leftover of nmot2x2 because the `t+1` outgoing bits already
HOLD, leftover of unique-L because `M(A)` is already the singleton
`{−e_2}`, leftover of eventual-`O` because the `t+1` outgoing sets already
equal the eventual neighbor locks, leftover of the x-symmetric three-site
seed because the scored letters match, the sets should be replaced by their
sums, named signs should suffice because they keep orientation, occupancy
`n` should track that vector, and empty intersection is tautological because
incoming and outgoing point opposite ways.

**Answer:** The named construction reports incoming sets `{−e_2}`,
`{+e_2}`, `{+e_1}`, `{−e_1, +e_3, −e_3}` and outgoing duals
`{+e_1, +e_3, −e_3}`, `{+e_1, +e_3, −e_3}`, `{+e_2, −e_2, +e_3, −e_3}`,
`{+e_2, −e_2}` at `A,B,C,D` from the record prefix at each probe's `t+1`.
Mixed stays a set. The construction does not sum. Occupancy `n` is not
used. Named signs lost the axis. `M` is frozen and disjoint from `O`. O is
not M. Reverse from M holds from singleton `M(A)`. Face from M holds at
mixed `D`. Reverse from O holds from `+e_3` against `−e_3`. Face from O
holds from `+e_2` against `−e_2`. Unique-L leftover reports face from `M`
`UNDEFINED` and reverse from `O` `UNDEFINED`. O at t leftover reports
reverse `UNDEFINED` and face `UNDEFINED`. nmxe2x M-only omits `O`.
nmot2x2 omits simultaneous `M`. Eventual-`O` omits simultaneous `M` and
the empty-at-`t` cut. The x-symmetric three-site seed records a third
site at tick 0. The sets are not those leftovers. The bits remain
displayed. Incoming-lock uniqueness is not required.

### N8 — cross-cycle echo

A unique-L display on these same #7214 x-probes would assign
`L(A)=−e_2`, `L(B)=+e_2`, `L(C)=+e_1`, `L(D)=UNDEFINED` and report reverse
from `M` hold with face `UNDEFINED`. nmxe2x M-only reports reverse hold
and face hold from `M` at formation with no `O`. O at t reports reverse
`UNDEFINED` and face `UNDEFINED` from empty `O` at `A`, `B`, and `C`.
nmot2x2 reports reverse `UNDEFINED` then hold and face `UNDEFINED` then
hold with composition fail and no simultaneous `M`. Eventual-`O` reports
the `τ` outgoing sets and hold/hold with no simultaneous `M`. Unique
lock-vector lettering of `O` would report reverse `UNDEFINED` and face
`UNDEFINED` because `A`, `C`, and `D` mix. A sum leftover of the same
lists would replace mixed `M(D,τ)` by `−e_1` after cancelling `+e_3` and
`−e_3`. This note is not those displays: mixed stays a set, the
construction does not sum, `M` and `O` are reported together at `t+1`, the
intersection is empty, Reverse from M holds, Face from M holds, Reverse
from O holds, and Face from O holds.

**Gate disposition:** PASS for the simultaneous `M` and `O` at `t+1`
reverse/face reports above. FAIL / DO NOT SHIP for “the predicate equals
the named sign,” “the predicate equals the unique singleton lock vector,”
“the predicate equals the sum of the lock set,” “bits are Admissibility,”
“the letter is occupancy `n`,” “the sets equal unique-L leftover,” “the
report equals nmxe2x M-only,” “the report equals O at t,” “O equals M,”
“reverse from M fails,” or “face from O is `UNDEFINED`.”

## Primary runner

The paired runner builds Euclidean `B_3(0)`, runs the x-axis opposite ±e_2
perp-step incoming-lock process, reads each probe's own incoming set and
outgoing dual from records with tick `<= t+1`, reports the intersection,
scores reverse and face from `M` and from `O` by existential opposite, and
checks Theorems 1--3. It also checks that the construction is not
named-sign lettering, that mixed stays a set, that the construction does
not sum, that occupancy `n` is not used, that a formation member from
already-recorded six-neighbor locks is not attached, that the sets are not
leftover of unique-L, that the report is not leftover of nmxe2x M-only,
and that the report is not leftover of O at t. No runner cache is written.
