---
claim_id: two_axis_same_lock_xprobe_incoming_outgoing_forall_orthogonal_tplus1_reverse_face_bounded_theorem_note_2026-08-15
claim_type: bounded_theorem
claim_scope: "Forall-orthogonal M vs O at t+1 on the four x-probes of the two-axis same-lock seed, and reverse/face from that, are reported. Displayed, not adopted."
upstream_dependencies:
  - minimal_axioms
runner: scripts/two_axis_same_lock_xprobe_incoming_outgoing_forall_orthogonal_tplus1_reverse_face_2026_08_15.py
---

# Forall-Orthogonal Incoming Versus Outgoing Reverse And Face At t+1 On Four X-Probes Of The Two-Axis Same-Lock Seed

> **Key terms used in this doc** are indexed A-Z at `docs/KEY_TERMINOLOGY.md`;
> each row points to the canonical source-of-truth doc.

**Date:** 2026-08-15
**Type:** bounded_theorem
**Scope:** forall-orthogonal of earliest incoming set `M` versus outgoing dual
`O` at each probe's `τ=t+1`, and reverse/face from that predicate, on the
four x-probes of the two-axis same-lock seed in `B_3(0)={n:n·n<=9}`, no
global T. Same process as nm2sl, x-probes. Let `t(q)` be the formation
tick of probe `q`. Let `τ(q)=t(q)+1`. `M(q,τ)` is the set of earliest
incoming nearest-neighbor steps at `q` using only records with tick `<= τ`.
Seeds are a singleton seed letter. `O(q,τ)` is the outgoing dual of `M`:
the set of `e` in `{±e_1,±e_2,±e_3}` such that `q+e` is formed and `e` is
in `M(q+e,τ)`. Unformed is `UNDEFINED`. Forall-perp HOLD if and only if
every `m` in `M` and every `o` in `O` have integer dot `m·o=0`. Empty or
`UNDEFINED` is `UNDEFINED`. Exist-perp (some pair dots to 0) is comparison
only. Reverse HOLD if and only if forall-perp holds at `A` and at `B`. Face
on `C,D`. This is the first forall-orthogonal display of `M` versus `O` at
`t+1` on the nm2slx cover-FAIL x-probe direction of the two-axis same-lock
seed. nm2slx cover reverse FAIL face FAIL (union misses e_2 at `A` and at
`D`; axes still disjoint). Dual of nm2axpx, which reported forall-perp
HOLDING on two-axis opposite x-probes where cover FAIL/FAIL. Uniqueness of
incoming or outgoing locks is not required. Mixed remains a set. Occupancy
`n` is not used. O is not M. Displayed, not adopted. Do not write into
Admissibility. Do not attach L1.
**Audit-status authority:** independent audit lane only. This note authors no
audit verdict and predicts none.
**Primary runner:**
[`scripts/two_axis_same_lock_xprobe_incoming_outgoing_forall_orthogonal_tplus1_reverse_face_2026_08_15.py`](../scripts/two_axis_same_lock_xprobe_incoming_outgoing_forall_orthogonal_tplus1_reverse_face_2026_08_15.py)

Framework input:

- [`MINIMAL_AXIOMS_2026-06-29.md`](MINIMAL_AXIOMS_2026-06-29.md) supplies
  cubic-lattice sites `Z^3` with nearest-neighbor adjacency, the one-site
  algebra `M_2(C)`, and the Record sentences that records form and that a
  present record locks exactly one admissible local possibility.

Everything after that quoted input is a finite displayed process on `B_3(0)`
and the four named x-probes. Incoming lock letters are unit nearest-neighbor
steps. `O` is the outgoing dual of those incoming sets at the per-probe cut
`τ=t+1`. Reverse and face are scored on forall-orthogonal of `M` versus `O`
at that same cut. Named signs `{+,−}` are a coarser readout and are not
used. A singleton unique lock letter is a different readout and is not used
as the object. A `Z^3` sum of those locks is a different readout and is not
used. Occupancy `n` is not used. This display does not use occupancy. A
six-neighbor star is not the letter. Exist-opposite of `M` with `M` or of
`O` with `O` is a different predicate and is leftover. nm2slx axis-cover is
a different leftover readout.

## Machine status and trace

```yaml
actual_current_surface_status: bounded-support
target_claim_type: bounded_theorem
claim_type_reason: "Exact report of forall-orthogonal M versus O at t+1 on the four x-probes of the two-axis same-lock seed, integer dots all zero, reverse hold from forall-perp at A and B, face hold from forall-perp at C and D; uniqueness of locks is not claimed and the bits are not adopted."
trace_class: frontier_discovery
target_claim_id: two_axis_same_lock_xprobe_incoming_outgoing_forall_orthogonal_tplus1_reverse_face
target_blocker_text: "display forall m in M, o in O have m·o=0 at t+1 on the four x-probes of the two-axis same-lock seed, and reverse/face from that, not nm2slx cover leftover"
source_of_blocker_text: handoff
reachability_to_target: advances
artifact_role: theorem
next_trace_action: "Keep forall-orthogonal M versus O at t+1 displayed; do not write forall-perp into Admissibility, do not reduce to nm2slx cover leftover, do not reduce to exist-opposite leftover, do not reduce to exist-perp leftover, do not require a unique letter, and do not attach L1."
conditional_surface_status: "exact on B_3(0) for forall-orthogonal M versus O at t+1 on the four x-probes of the two-axis same-lock seed, and reverse/face from that; displayed, not adopted"
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

No larger host is used. The four x-probes are the only sites whose
incoming-versus-outgoing dots are scored:

```text
A = (1,0,0),  B = (1,1,1),  C = (2,0,0),  D = (1,1,0).
```

These are not the y-probes `A=(0,1,0)`, `B=(1,1,1)`, `C=(0,2,0)`,
`D=(1,1,0)`. These are not the z-probes `A=(0,0,1)`, `B=(1,1,1)`,
`C=(0,0,2)`, `D=(1,0,1)`. `A` is not a seed. Same process as nm2sl,
x-probes.

Lock alphabet of the displayed process: `{±e_i}` with `i` in `{1,2,3}`.

Seed: two disjoint same-lock pairs recorded at formation tick 0. Origin
locks `+e_1` and `(0,1,0)` locks `+e_1`. Independently, `(0,0,1)` locks
`+e_2` and `(0,1,1)` locks `+e_2`. The second pair is a new seed, not a
formed child of the first pair, and neither pair is opposite. This seed is
not the one-axis two-site same-lock seed `{0,(0,1,0)}` both locking `+e_1`.
This seed is not the opposite two-site seed `+e_1/−e_1`. This seed is not
the two-axis opposite seed that would lock the second pair as `+e_2/−e_2`.
This seed is not the z-symmetric three-site seed `{0,(0,0,1),(0,0,-1)}`.
This seed is not the y-symmetric three-site seed that also records
`(0,-1,0)` at tick 0.

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

## Named incoming set `M`, outgoing set `O`, and forall-perp at `τ=t+1`

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
does not replace `O` by `M`. Occupancy `n` is not used.

Forall-perp HOLD if and only if every `m` in `M` and every `o` in `O` have
integer dot `m·o=0`. Empty or `UNDEFINED` on either side is `UNDEFINED`.
Nonempty with some pair of nonzero dot fails.

Exist-perp holds if and only if some pair has integer dot zero. Exist-perp
is comparison only. It is not the scored predicate. A pair with
`m={+e_1,+e_2}` and `o={+e_2}` has exist-perp hold and forall-perp fail.

Reverse holds if and only if forall-perp holds at `A` and at `B`. Face
holds if and only if forall-perp holds at `C` and at `D`. If either side of
a reverse or face comparison is `UNDEFINED`, the comparison is
`UNDEFINED`. If either side fails, the comparison fails.

nm2slx cover leftover scores complementary occupation of `{e_1,e_2,e_3}`
by `Axis(M)` and `Axis(O)`. Cover HOLD at a probe if and only if the Axis
sets are disjoint and their union equals `{e_1,e_2,e_3}`. That leftover is
not this display. On these x-probes cover fails at `A` and at `D` because
the union misses e_2; axes still disjoint. Forall-perp HOLDs at those
probes because every incoming letter is orthogonal to every outgoing
letter.

Exist-opposite leftover scores some pair that sums to zero inside `M` or
inside `O` across reverse or face. That leftover is not this display. On
this seed leftover M reverse, O reverse, M face, and O face all fail,
while forall-perp at `A`, `B`, `C`, and `D` all hold. Forall-perp scores
every incoming-versus-outgoing integer dot at one probe, not an opposite
pair inside one named set.

## Theorem 1 — ticks, `M`, `O`, integer dots, and forall-perp at `τ=t+1`

On this process the four x-probes form. Incoming is frozen at formation:
`M(q,t+1)=M(q,t)` at every scored probe. Outgoing is empty at `t` at each
of the four probes, then filled at `t+1`. Compare to nm2slx cover: that
leftover reports reverse fail and face fail. Here `M` and `O` are read
together at the same cut `τ=t+1` and scored by forall-perp:

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
cover(A) = fail
cover(B) = hold
cover(C) = hold
cover(D) = fail
forall-perp(A)=hold
forall-perp(B)=hold
forall-perp(C)=hold
forall-perp(D)=hold
```

`A` is not a seed. `A` is the site `(1,0,0)` forming at tick 2 with
incoming `{−e_3}`. Mixed remains a set: `O(B,τ)` has three outgoing
steps and `O(C,τ)` has three outgoing steps. Unique letters would assign
`UNDEFINED` at those mixed outgoing sets and would leave reverse and face
`UNDEFINED`. Here uniqueness is not required. `M` and `O` are disjoint at
each of the four probes at `τ`. O is not M.

Integer dots `m·o` at each probe, in six-neighbor order:

```text
A: (−e_3)·(+e_1)=0
   forall-perp at A: hold
B: (+e_1)·(+e_2)=0, (+e_1)·(+e_3)=0, (+e_1)·(−e_3)=0
   forall-perp at B: hold
C: (+e_1)·(−e_2)=0, (+e_1)·(+e_3)=0, (+e_1)·(−e_3)=0
   forall-perp at C: hold
D: (−e_3)·(+e_1)=0
   forall-perp at D: hold
```

Every scored integer dot is `0`. Forall-perp holds at `A`, `B`, `C`, and
`D`. Exist-perp also holds at each probe on this process because every pair
already dots to zero; that coincidence is comparison only. The predicates
are not the same: exist-perp can hold while forall-perp fails.

Empty `O` at `t` makes forall-perp `UNDEFINED` at `A`, `B`, `C`, and `D`,
while nm2slx cover fails on empty `O`. At `τ=t+1` both families are
nonempty at every scored probe. Reverse at `t` is `UNDEFINED` from empty
`O` at `A`. That empty-at-`t` leftover is not this display.

At `A` and at `D`, nm2slx cover fails because the unsigned union misses
e_2; axes still disjoint. Forall-perp HOLDs at those probes because
`{−e_3}` is orthogonal to `{+e_1}` at `A` and at `D`. Does forall `m·o=0`
HOLD where cover fails? Yes. At `B` and at `C` both cover and forall-perp
HOLD. Perp versus cover split. Two-axis opposite leftover on these same
x-probes also reports cover reverse FAIL face FAIL, but `O(D,τ)` there is
`{+e_1, −e_1}` and `O(D,t)` there is already `{−e_1}`; here `O(D,τ)` is
`{+e_1}` and `O(D,t)` is empty. 1-axis same-lock leftover on these x-probes
HOLDs cover at each probe, with ticks `3,2,4,3`.

New records in `B_3(0)` between `t` and `t+1` that meet a probe's
six-neighbors enter `O` and do not enter earliest `M`:

```text
new 6-NN of A at t(A)+1: (2, 0, 0)
new 6-NN of B at t(B)+1: (1, 2, 1), (1, 1, 2), (1, 1, 0)
new 6-NN of C at t(C)+1: (2, -1, 0), (2, 0, 1), (2, 0, -1)
new 6-NN of D at t(D)+1: (2, 1, 0)
```

This is not leftover of exist-perp: some pair with integer dot 0 is a
weaker leftover. This is not leftover of empty intersection: `{+e_1}` and
`{−e_1}` are disjoint and have integer dot `-1`. This is not leftover of
nm2slx cover. This is not leftover of exist-opposite. This is not leftover
of unique own-incoming or own-outgoing letters. This is not leftover of the
y-probe forall-perp display on this same seed. This is not leftover of the
two-axis opposite x-probe forall-perp display.

## Theorem 2 — reverse hold / fail / UNDEFINED

Reverse holds if and only if forall-perp holds at `A` and at `B`. Both
sides hold. Both sides are nonempty and defined, so this is not
`UNDEFINED`. Reverse is not exist-opposite leftover of `M(A,τ)` against
`M(B,τ)`. Reverse is not nm2slx cover leftover.

Reverse: hold

Reverse from forall-perp at τ: hold

This is not `fail` and not `UNDEFINED`. Reverse holds.

nm2slx cover reverse fails because cover fails at `A` (union misses e_2;
axes still disjoint). Forall-perp reverse HOLDs because every pair at `A`
and at `B` has integer dot 0. Unique own-outgoing letters on these
x-probes report reverse `UNDEFINED` from mixed `O(B,τ)`. Exist-opposite of
`M` reports reverse fail from `{−e_3}` against `{+e_1}`. Exist-opposite of
`O` reports reverse fail from `{+e_1}` against `{+e_2, +e_3, −e_3}`.
Exist-perp leftover also reports reverse hold here, but exist-perp is
weaker: `{+e_1,+e_2}` versus `{+e_2}` has exist-perp hold and forall-perp
fail. Those are different objects. Reverse from forall-perp holds at `τ`
because every incoming letter at `A` is orthogonal to every outgoing
letter at `A`, and likewise at `B`.

Reverse holds.

## Theorem 3 — face hold / fail / UNDEFINED

Face holds if and only if forall-perp holds at `C` and at `D`. Both sides
hold. Both sides are nonempty and defined, so this is not `UNDEFINED`. Face
is not exist-opposite leftover of `M(C,τ)` against `M(D,τ)`.

Face: hold

Face from forall-perp at τ: hold

Displayed, not adopted. The bits are not written into Admissibility.
Do not write into Admissibility. Do not attach L1.

This is not `fail` and not `UNDEFINED`. Face holds.

nm2slx cover face fails because cover fails at `D` (union misses e_2;
axes still disjoint) while cover HOLDs at `C`. Unique own-outgoing letters
on these x-probes report face `UNDEFINED` from mixed `O(C,τ)`. Exist-opposite
leftover of `M` reports face fail from `{+e_1}` against `{−e_3}`.
Exist-opposite leftover of `O` reports face fail from `{−e_2, +e_3, −e_3}`
against `{+e_1}`. Those are different objects. Face from forall-perp holds
at `τ` because every incoming letter at `C` is orthogonal to every outgoing
letter at `C`, and likewise at `D`.

At the same cut, forall-perp HOLDs at all four probes, so reverse HOLDs
and face HOLDs. nm2slx cover reverse FAIL face FAIL. Simultaneous HOLD
of exist-perp does not name this predicate. Empty intersection at a
formed probe does not name this predicate. Cover fail at `A` and at `D`
does not name this predicate.

Face holds.

## What this note does not claim

- It does not select a unique incoming or outgoing lock.
- It does not reduce lock vectors to named signs `{+,−}`.
- It does not require either set to be a singleton.
- It does not sum either set.
- It does not replace `O` by `M`.
- It does not replace forall-perp by exist-perp.
- It does not reprint exist-opposite reverse/face as this predicate.
- It does not score reverse as an opposite pair inside `M` or inside `O`.
- It does not reprint nm2slx cover reverse fail and face fail as this
  predicate.
- It does not use a six-neighbor star as the letter.
- It does not wait for a global later T.
- It does not attach a formation member from already-recorded six-neighbor
  locks.
- It does not use occupancy `n`.
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
two-axis same-lock process, the incoming and outgoing sets at `t+1`, the
integer dots, and the forall-perp reverse/face bits are displayed
theorem-domain data.

## Exact target and obligation graph

| Obligation | Status |
|---|---|
| current Lattice / Admissibility / Record premises | quoted; no edit |
| perp-step incoming-lock process on `B_3(0)` | displayed; two disjoint same-lock pairs `+e_1/+e_1` and `+e_2/+e_2` |
| ticks `t(A)`, `t(B)`, `t(C)`, `t(D)` | Theorem 1; `2`, `1`, `3`, `2` |
| `M` at `τ=t+1` | Theorem 1; `{−e_3}`, `{+e_1}`, `{+e_1}`, `{−e_3}` |
| `O` at `τ=t+1` | Theorem 1; outgoing dual |
| integer dots `m·o` at `A,B,C,D` | Theorem 1; all `0` |
| forall-perp at `A,B,C,D` | Theorem 1; `hold` / `hold` / `hold` / `hold` |
| compare to nm2slx cover fail | Theorem 1; cover fail, hold, hold, fail; forall-perp hold at each |
| reverse from forall-perp at `A` and `B` | Theorem 2; `hold` |
| face from forall-perp at `C` and `D` | Theorem 3; `hold` |
| unique incoming or outgoing lock | not required |
| occupancy `n` as the letter | not used |
| named-sign `{+,−}` letter | not used; lost the axis |
| singleton unique lock-vector letter | not used as the object; mixed remains a set |
| `Z^3` sum of the lock set | not used; no aggregation |
| six-neighbor star as the letter | not used |
| leftover of exist-opposite | not this display; M reverse, O reverse, M face, and O face all fail |
| leftover of exist-perp | comparison only |
| leftover of nm2slx cover | not this display; cover reverse FAIL face FAIL; union misses e_2 |
| leftover of empty intersection | not this display |
| leftover of unique own-incoming or own-outgoing letters | not this display |
| leftover of y-probe forall-perp on this seed | not this display |
| leftover of two-axis opposite x-probe forall-perp | not this display; `O(D,τ)` there is `{+e_1, −e_1}` |
| leftover of 1-axis same-lock cover-HOLD | not this display; ticks `3,2,4,3` |
| global later T | not used |
| forall-perp as Admissibility content | not adopted |
| formation site / probability / rate | open |
| physical Record readout of the bits | open |

## Value gate (V1–V5)

| # | Answer |
|---|---|
| V1 | It answers the first-display question: forall `m` in `M`, `o` in `O` have `m·o=0` at `t+1` on the four x-probes of the two-axis same-lock seed, and reverse/face from that, on the nm2slx cover-FAIL probe direction. |
| V2 | Current main has no landed forall-orthogonal `M` versus `O` at `t+1` reverse/face on these four x-probes of the two-axis same-lock seed. |
| V3 | Integer dots, forall-perp at four probes, and reverse/face are independently finite and exact. |
| V4 | The theorem is more than a restatement of Record because it reads every incoming-versus-outgoing integer dot at `t+1` and scores the universal zero-dot predicate. |
| V5 | It is not an adopted content rule: the bits remain displayed. |

## No-go discipline gate

The negative content is narrow: the display does not write those bits into
Admissibility, does not reduce them to named signs, does not require a
unique letter, does not replace forall-perp by exist-perp, does not
identify this display with exist-opposite leftover, and does not identify
the bits with nm2slx cover. No global impossibility is claimed.

### N1 — materially distinct routes

| Route | Attempt | Why it fails here | Marker |
|---|---|---|---|
| exist-opposite leftover | score some pair in `M` or in `O` that sums to zero | leftover M reverse, O reverse, M face, and O face all fail while forall-perp reverse HOLD face HOLD | ATTEMPTED |
| exist-perp leftover | score some pair with `m·o=0` | comparison only; `{+e_1,+e_2}` versus `{+e_2}` exist-perp HOLDs and forall-perp fails | ATTEMPTED |
| nm2slx cover | score complementary occupation of `{e_1,e_2,e_3}` | cover reverse FAIL face FAIL because the union misses e_2 at `A` and at `D`; forall-perp reverse HOLD face HOLD; axes still disjoint | ATTEMPTED |
| empty intersection | treat `M ∩ O = {}` as the predicate | `{+e_1}` and `{−e_1}` are disjoint and have integer dot `-1` | ATTEMPTED |
| unique letter | replace mixed sets by a singleton or `UNDEFINED` | mixed `O(B,τ)` and `O(C,τ)` remain sets; uniqueness is not required; unique-letter reverse is `UNDEFINED` | ATTEMPTED |
| y-probes | score `A=(0,1,0)` | different probes; this member scores the x-probes; y-probe forall-perp reverse HOLD face HOLD is a different display | ATTEMPTED |
| two-axis opposite leftover | lock the pairs as `+e_1/−e_1` and `+e_2/−e_2` | neither pair is opposite; `O(D,τ)` here is `{+e_1}`, not `{+e_1, −e_1}` | ATTEMPTED |
| one-axis leftover seed | drop the second pair and keep only `{0,(0,1,0)}` both `+e_1` | ticks become `3,2,4,3` and cover HOLDs at each x-probe | ATTEMPTED |
| sum of a set | replace each set by its `Z^3` sum | the construction does not sum | ATTEMPTED |
| named-sign lettering | collapse `{±e_i}` to `{+,−}` | named-sign lettering lost the axis | ATTEMPTED |
| global later T | wait until `max t(A,B,C,D)` before reading | `τ(q)=t(q)+1` is per-probe; no global T | ATTEMPTED |
| attach a formation member from already-recorded six-neighbor locks | form the probes by a neighbor-lock letter instead of perp-step | refused; not attached | ATTEMPTED |
| adopt bits into Admissibility | rewrite the local rule by forall-perp | refused; displayed, not adopted | ATTEMPTED |

### N2 — wall independence

Missing physical adoption, missing identification of forall-perp with
nm2slx cover, missing identification of forall-perp with exist-perp, and
missing Record identification of the bits are distinct open premises. This
note claims no complete wall collection.

### N3 — hidden-condition scan

The host `B_3(0)`, two disjoint same-lock pairs with locks `+e_1`, `+e_1`,
`+e_2`, and `+e_2`, perpendicular step rule, incoming-step lock, own
incoming set and own outgoing dual from records with tick `<= τ`, per-probe
`τ=t+1`, integer dots, forall-perp, four x-probes with non-seed `A`, reverse as
forall-perp at `A` and `B`, face as forall-perp at `C` and `D`, and mixed
remains a set are declared. No uniqueness of locks, no exist-opposite as
the scored object, no exist-perp as the scored object, no nm2slx cover as
the scored object, no global later T, no formation attachment from
already-recorded six-neighbor locks, and no Admissibility rewrite are
silently assumed.

### N4 — source residual matching

The current axiom memo supplies cubic sites, `M_2(C)`,
content-conditional-on-formation, and unreadable absence. The residual that
formation site, probability, and rate remain unsupplied is unchanged. The
`hold`/`hold` reports do not close that residual.

### N5 — resolution and rhetoric audit

| Resolution | Executed | Not claimed |
|---|---|---|
| per element | each integer dot `m·o` of earliest incoming or outgoing nearest-neighbor step | no continuum alphabet |
| per site | `A,B,C,D` x-probes on `B_3(0)` only | no other cubic sites |
| per mode | no mode calculation | no spectral exhaustion |
| per block | four `M`/`O` pairs, integer dots, forall-perp, reverse/face | no adopted content law |
| lattice wide | checked and not executed | no lattice-wide lettering rule |

### N6 — live partial-closure paths

Live routes include a later Record content map for reverse/face, a
formation-rate rule, and a physical selector among `{±e_i}`. None is taken
here.

### N7 — hostile steelman

**Steelman:** Forall-perp is only empty intersection, because disjoint
axis-aligned `M` and `O` already force `m·o=0`; reverse/face are only
nm2slx cover with the union demand dropped; mixed `O` should make the
predicate `UNDEFINED`; exist-perp already answers some pair dots to zero;
HOLD of forall-perp is tautological because the step rule is already
perpendicular; the second same-lock pair is just the one-axis child
`(0,1,1)`; this is only nm2axpx with the seed renamed.

**Answer:** Empty intersection is a set-theoretic report. Forall-perp is
the universal integer-dot report at the same cut. `{+e_1}` and `{−e_1}`
are disjoint with integer dot `-1`. Exist-opposite leftover pairs locks
inside `M` or inside `O`; this display pairs every incoming lock with
every outgoing lock at one probe. On this seed leftover exist-opposite
reverse and face fail while forall-perp reverse and face hold, so the
predicates split. Mixed `O(B,τ)` remains `{+e_2, +e_3, −e_3}` and
forall-perp at `B` holds. Exist-perp is comparison only and is a weaker
predicate. nm2slx cover demands complementary occupation of all three
axes; the union misses e_2 at `A` and at `D` so cover reverse FAIL face
FAIL, while forall-perp HOLDs because axes still disjoint. The formation
step rule is perpendicular to the parent lock; forall-perp here is a
readout of already-formed incoming letters against outgoing dual letters
at `t+1`, not a restatement of the step rule and not an Admissibility
rewrite. Seed `(0,1,1)` keeps letter `+e_2`; 1-axis leftover forms that
site at tick 1 locking `+e_3` and HOLDs cover at each x-probe. Two-axis
opposite leftover fills `O(D,τ)` with `{+e_1, −e_1}` and already has
`O(D,t)={−e_1}`; here `O(D,τ)={+e_1}` and `O(D,t)` is empty.

### N8 — cross-cycle echo

nm2slp reported forall-orthogonal `M` versus `O` on the four y-probes of
this same seed with reverse hold and face hold. nm2slx reported axis-cover
of `M` versus `O` on these four x-probes with reverse fail and face fail
because the union misses e_2; axes still disjoint. nm2axpx reported
forall-perp HOLDING on the two-axis opposite x-probes where cover FAIL/FAIL.
This note is not those displays: forall-perp of `M` versus `O` is read at
`t+1` on the four x-probes of the two-axis same-lock seed, every displayed
integer dot is 0, reverse HOLDs, and face HOLDs, including where nm2slx
cover fails.

**Gate disposition:** PASS for the forall-orthogonal `M` versus `O` at `t+1`
reverse/face reports above. FAIL / DO NOT SHIP for “the predicate equals
exist-opposite leftover,” “the predicate equals exist-perp,” “the predicate
equals nm2slx cover,” “the predicate equals empty intersection,” “the
predicate equals the unique singleton lock vector,” “bits are Admissibility,”
“reverse fails,” or “face is `UNDEFINED`.”

## Primary runner

The paired runner builds Euclidean `B_3(0)`, runs the two-axis same-lock
perp-step incoming-lock process, reads each probe's own earliest incoming
set and own outgoing dual from the record prefix at that probe's `t+1`,
lists every integer dot `m·o`, scores forall-perp at `A,B,C,D`, compares
those reports to nm2slx cover, and checks Theorems 1--3. It also checks
that exist-perp is comparison only, that exist-opposite leftover of `M`
and of `O` fails on reverse and on face, that mixed sets remain sets, that
uniqueness is not required, that occupancy `n` is not used, that a
formation member from already-recorded six-neighbor locks is not attached,
and that forall-perp HOLDs where cover fails. No runner cache is written.
