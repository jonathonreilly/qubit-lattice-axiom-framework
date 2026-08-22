---
claim_id: z_symmetric_three_site_zprobe_incoming_outgoing_forall_orthogonal_tplus1_reverse_face_bounded_theorem_note_2026-08-15
claim_type: bounded_theorem
claim_scope: "Forall-orthogonal M vs O at t+1 on the four #7186 z-probes, and reverse/face from that, are reported. Displayed, not adopted."
upstream_dependencies:
  - minimal_axioms
runner: scripts/z_symmetric_three_site_zprobe_incoming_outgoing_forall_orthogonal_tplus1_reverse_face_2026_08_15.py
---

# Forall-Orthogonal Incoming Versus Outgoing Reverse And Face At t+1 On Four #7186 Z-Probes

> **Key terms used in this doc** are indexed A-Z at `docs/KEY_TERMINOLOGY.md`;
> each row points to the canonical source-of-truth doc.

**Date:** 2026-08-15
**Type:** bounded_theorem
**Scope:** forall-orthogonal readout of own earliest incoming nearest-neighbor
step set `M` against own outgoing dual `O` at each probe's `τ=t+1`, and
reverse/face from that readout, on the four nszopinz #7186 z-probes in
`B_3(0)={n:n·n<=9}`, no global T. Same process and z-probes as nszopinz
#7186. Let `t(q)` be the formation tick of probe `q`. Let `τ(q)=t(q)+1`.
`M(q,τ)` is the set of earliest incoming nearest-neighbor steps at `q`
using only records with tick `<= τ`. Seeds are a singleton seed letter.
Unformed at `τ` is `UNDEFINED`. `O(q,τ)` is the outgoing dual of `M`: the
set of `e` in `{±e_1,±e_2,±e_3}` such that `q+e` is formed in `B_3(0)` and
`e` is in `M(q+e,τ)`. Unformed `q` at `τ` is `UNDEFINED`. Empty `O` is
empty, not `UNDEFINED`. Forall-perp HOLD if and only if every `m` in
`M(q,τ)` and every `o` in `O(q,τ)` have integer dot `m·o=0`. Empty or
`UNDEFINED` on either side is `UNDEFINED`. Exist-perp (some pair dots to
0) is comparison only. Reverse HOLD if and only if forall-perp HOLDs at
`A` and at `B`. Face likewise on `C,D`. Empty or `UNDEFINED` on either
side of a comparison is `UNDEFINED`. This is the first forall-orthogonal
display of `M` versus `O` at `t+1` on the nmzpin HOLDING own-incoming
member. This is not leftover of exist-perp. This is not leftover of
nmsimzp exist-opposite of `M` or of `O`. This is not leftover of empty
intersection. This is not leftover of nstri forall-perp fail at B. This
is not leftover of nmt2zp `M` two-tick HOLD/HOLD. This is not leftover of
nmot2zp `O` two-tick. This is not leftover of unique own-incoming or
own-outgoing letters. This is not leftover of mixed #7188 fail/fail. This
is not leftover of a six-neighbor star. Uniqueness of incoming or outgoing
locks is not required. Mixed remains a set. Occupancy `n` is not used. O
is not M. Displayed, not adopted. Do not write into Admissibility. Do not
attach L1.
**Audit-status authority:** independent audit lane only. This note authors no
audit verdict and predicts none.
**Primary runner:**
[`scripts/z_symmetric_three_site_zprobe_incoming_outgoing_forall_orthogonal_tplus1_reverse_face_2026_08_15.py`](../scripts/z_symmetric_three_site_zprobe_incoming_outgoing_forall_orthogonal_tplus1_reverse_face_2026_08_15.py)

Framework input:

- [`MINIMAL_AXIOMS_2026-06-29.md`](MINIMAL_AXIOMS_2026-06-29.md) supplies
  cubic-lattice sites `Z^3` with nearest-neighbor adjacency, the one-site
  algebra `M_2(C)`, and the Record sentences that records form and that a
  present record locks exactly one admissible local possibility.

Everything after that quoted input is a finite displayed process on `B_3(0)`
and the four named z-probes. Incoming lock letters are unit nearest-neighbor
steps. `O` is the outgoing dual of those incoming sets at a per-probe cut
`τ=t+1`. Forall-perp is scored on every integer dot of an incoming letter
against an outgoing letter at the same probe. Reverse and face are scored
from those four per-probe reports. Named signs `{+,−}` are a coarser readout
and are not used. A singleton unique lock letter is a different readout
and is not used as the object. Existential opposite of `M(A)` against
`M(B)` is a different readout and is not used as the object. Exist-perp is
a different leftover readout. Occupancy `n` is not used. A six-neighbor
star is not the letter. The construction does not use occupancy.

## Machine status and trace

```yaml
actual_current_surface_status: bounded-support
target_claim_type: bounded_theorem
claim_type_reason: "Exact report of t, M, O, integer dots, and forall-perp of M versus O at t+1 on the four #7186 z-probes, with reverse hold and face hold from those per-probe reports; uniqueness of locks is not claimed and the bits are not adopted."
trace_class: frontier_discovery
target_claim_id: z_symmetric_three_site_zprobe_incoming_outgoing_forall_orthogonal_tplus1_reverse_face
target_blocker_text: "display forall-orthogonal M versus O at t+1 on the four #7186 z-probes, and reverse/face from that, no global T"
source_of_blocker_text: handoff
reachability_to_target: advances
artifact_role: theorem
next_trace_action: "Keep forall-perp of M versus O at t+1 displayed; do not write the bits into Admissibility, do not reduce to exist-perp, do not reduce to exist-opposite of M or of O, do not replace orthogonality by empty intersection, do not reduce to a unique letter, do not replace O by M, do not replace either set by six-neighbor lock union, do not use occupancy n, and do not wait for a global later T."
conditional_surface_status: "exact on B_3(0) for forall-orthogonal M versus O at t+1 on the four #7186 z-probes, no global T; displayed, not adopted"
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

No larger host is used. The four z-probes are the only sites whose own
incoming sets, outgoing sets, integer dots, and forall-perp reports are
scored:

```text
A = (0,0,1),  B = (1,1,1),  C = (0,0,2),  D = (1,0,1).
```

These are not the x-probes `A=(1,0,0)`, `B=(1,1,1)`, `C=(2,0,0)`,
`D=(1,1,0)`. These are not the y-probes `A=(0,1,0)`, `B=(1,1,1)`,
`C=(0,2,0)`, `D=(1,1,0)`. `A` is a seed. Same process and z-probes as
nszopinz #7186.

Lock alphabet of the displayed process: `{±e_i}` with `i` in `{1,2,3}`.

Seed: the three-record set `{0, (0,0,1), (0,0,-1)}` is recorded at formation
tick 0 with locks `L(0)=+e_1`, `L(0,0,1)=−e_1`, and `L(0,0,-1)=−e_1`. The
third site is the z-mirror of the two-site opposite-lock partner `(0,0,1)`.
This seed is not the two-site opposite-lock seed `{0,(0,0,1)}` and not the
three-site opposite-lock seed whose third site is `(1,0,0)` with lock `+e_2`.
This seed is not the perp two-site seed `+e_1/+e_2`. This seed is not the
y-symmetric three-site seed `{0,(0,1,0),(0,-1,0)}`. This seed is not the
x-symmetric three-site seed `{0,(1,0,0),(-1,0,0)}`. Same process as nszmenu
#7188 on the x-probes; the scored sites here are the z-probes.

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

## Named forall-orthogonal readout of `M` versus `O` at `t+1`

Let `t(q)` be the formation tick of z-probe `q` when that tick is defined in
`B_3(0)`. Let `τ(q)=t(q)+1`. There is no global T.

`M(q,τ)` is the set of earliest incoming nearest-neighbor steps at `q`
using only records with tick `<= τ`. If `q` is unformed at `τ`, then
`M(q,τ)` is `UNDEFINED`. If `q` is a seed and `τ >= 0`, then `M(q,τ)` is
the singleton seed letter.

`O(q,τ)` is the outgoing dual of `M`:

```text
O(q,τ) = { e in {±e_1,±e_2,±e_3} | q+e formed in B_3(0) and e in M(q+e,τ) }.
```

If `q` is unformed at `τ`, then `O(q,τ)` is `UNDEFINED`. Empty `O` is empty,
not `UNDEFINED`. Duplicate outgoing steps collapse in the set. The
construction does not require `M` or `O` to be a singleton. It does not sum
either set. It does not replace `O` by `M`. It does not replace either set
by locks of six-neighbors of `q`. It does not wait for a global later T.
Occupancy `n` is not used. O is not M.

Forall-perp at a formed probe with both sets nonempty HOLDs if and only if
every `m` in `M(q,τ)` and every `o` in `O(q,τ)` have integer dot `m·o=0`.
Empty or `UNDEFINED` on either side is `UNDEFINED`. Nonempty with a
nonzero pair fails. Exist-perp (some pair has integer dot 0) is a leftover
comparison and is not the scored predicate. Empty intersection of `M` and
`O` is a leftover comparison: `{+e_1}` and `{−e_1}` are disjoint and have
dot `-1`. Existential opposite of `M(A)` against `M(B)`, or of `O(A)`
against `O(B)`, is a leftover comparison across probes, not a same-site
dot.

Reverse from forall-perp at `τ` HOLDs if and only if forall-perp HOLDs at
`A` and at `B`. Face likewise on `C,D`. Empty or `UNDEFINED` on either
side of a comparison is `UNDEFINED`; else a fail on either side fails.

Identifying a named sign of those locks with reverse or face is refused:
named-sign lettering lost the axis. Reverse and face are scored from
forall-perp of `M` versus `O` at the named probes. They are not an
occupancy-kernel inner product.

## Theorem 1 — ticks, `M`, `O`, dots, and forall-perp at `τ=t+1`

On this process the four z-probes form. Compare to nmt2zp: that leftover
reports `M(q,t+1)=M(q,t)` at every scored probe. Compare to nmot2zp: that
leftover reports `O` empty or singleton at `t` and enlarged at `t+1`. Compare
to nmsimzp: that leftover reports exist-opposite of `M` and of `O`
separately. Here `M` and `O` are read together at `τ=t+1` and scored by
forall-perp:

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
(−e_1)·(+e_2)=0, (−e_1)·(−e_2)=0, (−e_1)·(+e_3)=0
(+e_1)·(+e_2)=0, (+e_1)·(−e_2)=0, (+e_1)·(+e_3)=0
(+e_3)·(+e_1)=0, (+e_3)·(−e_1)=0, (+e_3)·(+e_2)=0, (+e_3)·(−e_2)=0
(+e_2)·(+e_1)=0, (+e_2)·(−e_1)=0, (−e_2)·(+e_1)=0, (−e_2)·(−e_1)=0, (−e_3)·(+e_1)=0, (−e_3)·(−e_1)=0
forall-perp(A)=hold
forall-perp(B)=hold
forall-perp(C)=hold
forall-perp(D)=hold
```

`A` is a seed at tick 0. Mixed remains a set: `M(D,τ)` has three incoming
steps and `O(A,τ)` has three outgoing steps. Unique own-incoming letters
would assign `UNDEFINED` at `D`. Unique own-outgoing letters would assign
`UNDEFINED` at `A`, `B`, `C`, and `D`. Here uniqueness is not required.
Every displayed integer dot is 0. Empty `O` at `t` makes forall-perp
`UNDEFINED` at `A`, `B`, and `C` at the own-tick cut; at `τ=t+1` both
families are nonempty. O is not M. No six-neighbor star.

This is not leftover of exist-perp: some pair with integer dot 0 is a
weaker leftover. On the nstri three-site leftover, forall-perp fails at
`B` because `+e_1` sits in both `M(B,τ)` and `O(B,τ)` with `+e_1·+e_1=1`,
while exist-perp still HOLDs at `B`. This is not leftover of nmsimzp
exist-opposite: that leftover scores opposite pairs of `M` across `A,B`
and of `O` across `A,B`. This is not leftover of empty intersection:
`{+e_1}` and `{−e_1}` are disjoint and have integer dot `-1`. This is not
leftover of nstri forall-perp fail at B. This is not leftover of nmt2zp
`M` two-tick HOLD/HOLD. This is not leftover of nmot2zp `O` two-tick. This
is not leftover of unique own-incoming or own-outgoing letters. This is
not leftover of mixed #7188 fail/fail. This is not leftover of nmsimopp /
nmsimsy / nmsimzx: those leftovers use other seeds and other probe
families.

## Theorem 2 — reverse from forall-perp at `τ`

Reverse from forall-perp holds if and only if forall-perp HOLDs at `A` and
at `B`. Both reports are hold. Reverse holds.

Reverse from forall-perp at τ: hold

Unique own-incoming letters on these z-probes report reverse hold and face
`UNDEFINED` from mixed `M(D,τ)`. Same-tick-inclusive six-neighbor lock union
leftover reports reverse fail from `{+e_1}` at neighbors of seed `A`.
Exist-opposite of `M` reports reverse hold from `−e_1` at `A` against
`+e_1` at `B`; that pair is across probes, not a same-site `M` versus `O`
dot. Exist-perp leftover also reports reverse hold here, but fails to
separate this member from nstri, where exist-perp reverse HOLDs and
forall-perp reverse fails. Those are different objects. Reverse from
forall-perp holds at `τ` because every incoming letter at `A` is orthogonal
to every outgoing letter at `A`, and likewise at `B`.

## Theorem 3 — face from forall-perp at `τ`

Face from forall-perp holds if and only if forall-perp HOLDs at `C` and at
`D`. Both reports are hold. Face holds.

Face from forall-perp at τ: hold

Displayed, not adopted. The bits are not written into Admissibility.
Do not write into Admissibility. Do not attach L1. Unique own-outgoing
letters on these z-probes report reverse `UNDEFINED` and face `UNDEFINED`
from mixed `O` at `τ`. nmot2zp leftover reports reverse `UNDEFINED` at `t`
because `O` is empty at `A`, `B`, and `C`. nmsimzp leftover reports reverse
hold and face hold from exist-opposite of `M` and of `O`. Those are
different objects. Face from forall-perp holds at `τ` because every
incoming letter at `C` is orthogonal to every outgoing letter at `C`, and
likewise at `D`.

At the same cut, forall-perp HOLDs at all four probes, so reverse HOLDs
and face HOLDs. Simultaneous HOLD of exist-opposite of `M` and of `O` does
not name this predicate. Empty intersection at a formed probe does not
name this predicate.

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
- It does not reprint unique own-incoming or own-outgoing lock-vector
  letters on these z-probes as the object.
- It does not reprint nmt2zp `M` two-tick HOLD/HOLD.
- It does not reprint nmot2zp `O` two-tick.
- It does not reprint exist-perp as the scored predicate.
- It does not reprint nmsimzp exist-opposite of `M` or of `O`.
- It does not reprint empty intersection as orthogonality.
- It does not reprint nstri forall-perp fail at B as this member.
- It does not reprint mixed #7188 fail/fail as this member.
- It does not reprint nmsimopp / nmsimsy / nmsimzx simultaneous bits as
  this member.
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

This display uses Lattice to name `B_3(0)` and the four z-probes. It uses Qubit
only as the algebra of the local possibility domain. It uses Record only as a
boundary: a present lock is content. It does not rewrite Admissibility. The
z-symmetric three-site process, the incoming and outgoing sets at `t+1`, the
integer dots, the forall-perp reports, and reverse/face from those reports are
displayed theorem-domain data.

## Exact target and obligation graph

| Obligation | Status |
|---|---|
| current Lattice / Admissibility / Record premises | quoted; no edit |
| perp-step incoming-lock process on `B_3(0)` | displayed; nszopinz #7186 seed `+e_1/−e_1/−e_1` |
| ticks `t(A)`, `t(B)`, `t(C)`, `t(D)` | Theorem 1; `0`, `2`, `1`, `3` |
| `M` at `τ=t+1` | Theorem 1; frozen incoming sets |
| `O` at `τ=t+1` | Theorem 1; enlarged outgoing duals |
| integer dots of `M` versus `O` at `τ` | Theorem 1; every displayed pair is 0 |
| forall-perp at `A,B,C,D` | Theorem 1; hold at each |
| reverse from forall-perp at `τ` | Theorem 2; hold |
| face from forall-perp at `τ` | Theorem 3; hold |
| unique incoming or outgoing lock | not required |
| occupancy `n` as the letter | not used |
| named-sign `{+,−}` letter | not used; lost the axis |
| singleton unique lock-vector letter | not used as the object; mixed remains a set |
| `Z^3` sum of the lock set | not used; no aggregation |
| six-neighbor star as the letter | not used |
| leftover of exist-perp | not this display |
| leftover of nmsimzp exist-opposite | not this display |
| leftover of empty intersection | not this display |
| leftover of nstri forall-perp fail at B | not this display |
| leftover of nmt2zp `M` two-tick HOLD/HOLD | not this display |
| leftover of nmot2zp `O` two-tick | not this display |
| leftover of unique own-incoming or own-outgoing letters | not this display |
| leftover of mixed #7188 fail/fail | not this display |
| leftover of nmsimopp / nmsimsy / nmsimzx | not this display |
| global later T | not used |
| forall-perp as Admissibility content | not adopted |
| formation site / probability / rate | open |
| physical Record readout of the bits | open |

## Value gate (V1–V5)

| # | Answer |
|---|---|
| V1 | It answers the first-display question: forall-orthogonal `M` versus `O` at `t+1` on the four #7186 z-probes, and reverse/face from that. |
| V2 | Current main has no landed forall-orthogonal incoming-versus-outgoing reverse/face at `t+1` on these four #7186 z-probes. |
| V3 | Own incoming sets, own outgoing sets, integer dots, forall-perp reports, and the `hold`/`fail`/`UNDEFINED` reverse/face bits are independently finite and exact. |
| V4 | The theorem is more than a restatement of Record because it reads both duals at one cut and scores every integer dot, not existence of an opposite pair. |
| V5 | It is not an adopted content rule: the bits remain displayed. |

## No-go discipline gate

The negative content is narrow: the display does not write those bits into
Admissibility, does not reduce them to named signs, does not require a
unique letter, does not replace `O` by `M`, does not replace either set by
six-neighbor lock union, does not identify this display with exist-perp,
does not identify the bits with nmsimzp exist-opposite, does not identify
orthogonality with empty intersection, does not identify the bits with
nstri forall-perp fail at B, does not identify the bits with nmt2zp `M`
HOLD/HOLD, does not identify the bits with nmot2zp `O` two-tick, and does
not identify the bits with mixed #7188 fail/fail. No global impossibility
is claimed.

### N1 — materially distinct routes

| Route | Attempt | Why it fails here | Marker |
|---|---|---|---|
| exist-perp | score some pair with integer dot 0 | weaker leftover; nstri `B` has exist-perp hold and forall-perp fail from `+e_1·+e_1=1` | ATTEMPTED |
| nmsimzp exist-opposite | score opposite pairs of `M` across `A,B` and of `O` across `A,B` | that leftover is cross-probe opposite, not same-site `M` versus `O` dots | ATTEMPTED |
| empty intersection | treat `M ∩ O = {}` as the predicate | `{+e_1}` and `{−e_1}` are disjoint and have integer dot `-1` | ATTEMPTED |
| nstri forall-perp fail at B | reuse the three-site leftover whose third seed is `(1,0,0)` with lock `+e_2` | different seed; that leftover reports reverse fail | ATTEMPTED |
| nmt2zp `M` two-tick | reuse earliest incoming `M` at `t` versus `t+1` | that leftover is HOLD/HOLD composition of `M` alone; it does not display `O` dots | ATTEMPTED |
| nmot2zp `O` two-tick | reuse outgoing `O` at `t` versus `t+1` | that leftover reports reverse `UNDEFINED` then hold; empty `O` at `t` makes forall-perp `UNDEFINED` | ATTEMPTED |
| unique own letter | replace mixed `M` or `O` by a singleton or `UNDEFINED` | `M(D,τ)` has three incoming steps and `O(A,τ)` has three outgoing steps; mixed remains a set; unique-letter face from `M` is `UNDEFINED` | ATTEMPTED |
| same-tick-inclusive six-neighbor lock union | score locks of six-neighbors formed by `t(q)` | that leftover includes `+e_1` at `A` from the origin partner; `M(A,τ)` is `{−e_1}` and `O(A,τ)` does not contain `+e_1` | ATTEMPTED |
| mixed #7188 fail/fail | reuse z-symmetric mixed `M` reverse-fail face-fail on the x-probes | different probes of this process; this member reports forall-perp hold at each z-probe | ATTEMPTED |
| nmsimopp / nmsimsy / nmsimzx | reuse simultaneous bits on other seeds or probe families | different seeds and probes; not this member | ATTEMPTED |
| sum of `M` or `O` | replace each set by its `Z^3` sum | the construction does not sum; forall-perp reads pairs, not a sum | ATTEMPTED |
| named-sign lettering | collapse `{±e_i}` to `{+,−}` | named-sign lettering lost the axis | ATTEMPTED |
| global later T | wait until `max t(A,B,C,D)` before reading the sets | `τ(q)=t(q)+1` is per-probe; no global T | ATTEMPTED |
| attach a formation member from already-recorded six-neighbor locks | form the probes by a neighbor-lock letter instead of perp-step | refused; not attached | ATTEMPTED |
| adopt bits into Admissibility | rewrite the local rule by forall-perp | refused; displayed, not adopted | ATTEMPTED |

### N2 — wall independence

Missing physical adoption, missing identification of forall-perp with
exist-opposite, and missing Record identification of orthogonality are
distinct open premises. This note claims no complete wall collection.

### N3 — hidden-condition scan

The host `B_3(0)`, z-symmetric three-site seed locks `+e_1`, `−e_1`, and
`−e_1`, perpendicular step rule, incoming-step lock, own incoming set and
own outgoing dual from records with tick `<= τ`, per-probe `τ=t+1`,
forall-perp of every integer dot, four z-probes with seed `A`, empty or
`UNDEFINED` as `UNDEFINED`, mixed remains a set, and reverse/face from
those reports are declared. No uniqueness of locks, no six-neighbor lock
union as the scored object, no exist-perp as the scored predicate, no
global later T, no formation attachment from already-recorded six-neighbor
locks, and no Admissibility rewrite are silently assumed.

### N4 — source residual matching

The current axiom memo supplies cubic sites, `M_2(C)`,
content-conditional-on-formation, and unreadable absence. The residual that
formation site, probability, and rate remain unsupplied is unchanged. The
hold reports do not close that residual.

### N5 — resolution and rhetoric audit

| Resolution | Executed | Not claimed |
|---|---|---|
| per element | each integer dot of an earliest incoming step against an outgoing dual step | no continuum alphabet |
| per site | `A,B,C,D` z-probes on `B_3(0)` only | no other cubic sites |
| per mode | no mode calculation | no spectral exhaustion |
| per block | four incoming sets, four outgoing sets, integer dots, four forall-perp reports, reverse/face | no adopted content law |
| lattice wide | checked and not executed | no lattice-wide lettering rule |

### N6 — live partial-closure paths

Live routes include a later Record content map for reverse/face, a
formation-rate rule, and a physical selector among `{±e_i}`. None is taken
here.

### N7 — hostile steelman

**Steelman:** Because every displayed integer dot is 0, forall-perp is only
exist-perp, or only empty intersection, or only nmsimzp exist-opposite of
`M` and of `O`. nstri is a different seed so it cannot separate the
predicate. Empty `O` at `t` already made reverse `UNDEFINED`, so `t+1` is
tautological because children form. Mixed `D` incoming and mixed `A`
outgoing should make face or reverse `UNDEFINED`. Six-neighbor lock union
already answered reverse fail on this same process. Mixed #7188 already
answered fail/fail. Named signs should suffice. And HOLD of forall-perp
is only tautological because the step rule is already perpendicular.

**Answer:** Forall-perp scores every pair, not some pair. On the nstri
leftover, exist-perp HOLDs at `B` while forall-perp fails from a shared
`+e_1`. Empty intersection is not orthogonality: `{+e_1}` and `{−e_1}`
are disjoint with integer dot `-1`. nmsimzp exist-opposite scores
cross-probe opposite pairs inside `M` or inside `O`; same-site `M(A)`
versus `O(A)` has no opposite pair and still has forall-perp HOLD.
Empty `O` at `t` makes forall-perp `UNDEFINED` at `A`, `B`, and `C`; the
`t+1` cut is the first cut where both families are nonempty at every
scored probe. Mixed `M(D,τ)` and mixed `O(A,τ)` remain sets; reverse and
face hold. Six-neighbor lock union is a different object. Mixed #7188
fail/fail is a different probe family of this process. Named signs lost
the axis. The formation step rule is perpendicular to the parent lock;
forall-perp here is a readout of already-formed incoming letters against
outgoing dual letters at `t+1`, not a restatement of the step rule and
not an Admissibility rewrite.

### N8 — cross-cycle echo

A unique own-incoming lock-vector display on these same z-probes assigned
`−e_1`, `+e_1`, `+e_3`, `UNDEFINED` and reported reverse hold with face
`UNDEFINED`. nszopinz #7186 own incoming exist-opposite reported reverse
hold and face hold from `M`. nmt2zp `M` two-tick composition reported
reverse hold and face hold at both cuts. nmot2zp `O` two-tick composition
reported reverse `UNDEFINED` then hold. nmsimzp reported empty
intersection with reverse/face hold from `M` and from `O` separately.
nstri forall-perp fail at B is a different seed whose reverse from
forall-perp fails. Mixed #7188 two-tick composition reported reverse fail
and face fail. nmsimopp / nmsimsy / nmsimzx score other seeds or other
probe families. This note is not those displays: forall-perp of `M`
versus `O` is read at `t+1` on the four #7186 z-probes, every displayed
integer dot is 0, reverse HOLDs, and face HOLDs.

**Gate disposition:** PASS for the forall-orthogonal incoming-versus-outgoing
reverse/face reports above. FAIL / DO NOT SHIP for “the predicate equals
exist-perp,” “the predicate equals nmsimzp exist-opposite,” “the predicate
equals empty intersection,” “the predicate equals nstri forall-perp fail
at B,” “the predicate equals the named sign,” “the predicate equals the
unique singleton lock vector,” “the predicate equals `M` two-tick of
nmt2zp,” “the predicate equals nmot2zp `O` two-tick,” “the predicate
equals six-neighbor lock union,” “the predicate equals mixed #7188
fail/fail,” “the predicate equals nmsimopp / nmsimsy / nmsimzx,” “bits
are Admissibility,” or “`M` equals `O`.”

## Primary runner

The paired runner builds Euclidean `B_3(0)`, runs the nszopinz #7186
perp-step incoming-lock process, reads each probe's own incoming set and
own outgoing dual from the record prefix at that probe's `t+1`, reports
integer dots and forall-perp, and checks Theorems 1--3. It also checks
that empty or `UNDEFINED` is `UNDEFINED`, that mixed sets remain sets,
that exist-perp is a leftover, that nmsimzp exist-opposite is a leftover,
that empty intersection is not forall-perp, that nstri forall-perp fail
at B is a leftover, that a formation member from already-recorded
six-neighbor locks is not attached, and that the display is not nmt2zp `M`
two-tick HOLD/HOLD and not nmot2zp `O` two-tick. No runner cache is
written.
