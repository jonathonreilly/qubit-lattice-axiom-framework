---
claim_id: z_symmetric_three_site_xprobe_incoming_outgoing_forall_orthogonal_tplus1_reverse_face_bounded_theorem_note_2026-08-15
claim_type: bounded_theorem
claim_scope: "Forall-orthogonal M vs O at t+1 on the four #7188 x-probes, and reverse/face from that, are reported. Displayed, not adopted."
upstream_dependencies:
  - minimal_axioms
runner: scripts/z_symmetric_three_site_xprobe_incoming_outgoing_forall_orthogonal_tplus1_reverse_face_2026_08_15.py
---

# Forall-Orthogonal Incoming Versus Outgoing Reverse And Face At t+1 On Four #7188 X-Probes

> **Key terms used in this doc** are indexed A-Z at `docs/KEY_TERMINOLOGY.md`;
> each row points to the canonical source-of-truth doc.

**Date:** 2026-08-15
**Type:** bounded_theorem
**Scope:** forall-orthogonal readout of own earliest incoming nearest-neighbor
step set `M` against own outgoing dual `O` at each probe's `τ=t+1`, and
reverse/face from that readout, on the four nszopinx #7188 x-probes in
`B_3(0)={n:n·n<=9}`, no global T. Same process and x-probes as nszopinx
#7188. Let `t(q)` be the formation tick of probe `q`. Let `τ(q)=t(q)+1`.
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
display of `M` versus `O` at `t+1` on the nmcfail cover-FAIL member of
#7188. nmcfail cover reverse FAIL face FAIL (union misses e_3; axes
still disjoint). This is not leftover of nmcfail cover. This is not
leftover of exist-perp. This is not leftover of empty intersection. This
is not leftover of nszmenu #7205 M exist-opposite fail/fail. This is not
leftover of nstri forall-perp fail at B. Uniqueness of incoming or
outgoing locks is not required. Mixed remains a set. Occupancy `n` is not
used. O is not M. Displayed, not adopted. Do not write into Admissibility.
Do not attach L1.
**Audit-status authority:** independent audit lane only. This note authors no
audit verdict and predicts none.
**Primary runner:**
[`scripts/z_symmetric_three_site_xprobe_incoming_outgoing_forall_orthogonal_tplus1_reverse_face_2026_08_15.py`](../scripts/z_symmetric_three_site_xprobe_incoming_outgoing_forall_orthogonal_tplus1_reverse_face_2026_08_15.py)

Framework input:

- [`MINIMAL_AXIOMS_2026-06-29.md`](MINIMAL_AXIOMS_2026-06-29.md) supplies
  cubic-lattice sites `Z^3` with nearest-neighbor adjacency, the one-site
  algebra `M_2(C)`, and the Record sentences that records form and that a
  present record locks exactly one admissible local possibility.

Everything after that quoted input is a finite displayed process on `B_3(0)`
and the four named x-probes. Incoming lock letters are unit nearest-neighbor
steps. `O` is the outgoing dual of those incoming sets at a per-probe cut
`τ=t+1`. Forall-perp is scored on every integer dot of an incoming letter
against an outgoing letter at the same probe. Reverse and face are scored
from those four per-probe reports. Named signs `{+,−}` are a coarser readout
and are not used. A singleton unique lock letter is a different readout
and is not used as the object. Existential opposite of `M(A)` against
`M(B)` is a different readout and is not used as the object. Exist-perp is
a different leftover readout. nmcfail axis-cover is a different leftover
readout. Occupancy `n` is not used. A six-neighbor star is not the letter.
The construction does not use occupancy.

## Machine status and trace

```yaml
actual_current_surface_status: bounded-support
target_claim_type: bounded_theorem
claim_type_reason: "Exact report of t, M, O, integer dots, and forall-perp of M versus O at t+1 on the four #7188 x-probes, with reverse hold and face hold from those per-probe reports; uniqueness of locks is not claimed and the bits are not adopted."
trace_class: frontier_discovery
target_claim_id: z_symmetric_three_site_xprobe_incoming_outgoing_forall_orthogonal_tplus1_reverse_face
target_blocker_text: "display forall-orthogonal M versus O at t+1 on the four #7188 x-probes, and reverse/face from that, no global T"
source_of_blocker_text: handoff
reachability_to_target: advances
artifact_role: theorem
next_trace_action: "Keep forall-perp of M versus O at t+1 displayed; do not write the bits into Admissibility, do not reduce to exist-perp, do not reduce to nmcfail cover, do not replace orthogonality by empty intersection, do not reduce to a unique letter, do not replace O by M, do not replace either set by six-neighbor lock union, do not use occupancy n, and do not wait for a global later T."
conditional_surface_status: "exact on B_3(0) for forall-orthogonal M versus O at t+1 on the four #7188 x-probes, no global T; displayed, not adopted"
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
incoming sets, outgoing sets, integer dots, and forall-perp reports are
scored:

```text
A = (1,0,0),  B = (1,1,1),  C = (2,0,0),  D = (1,1,0).
```

These are not the y-probes `A=(0,1,0)`, `B=(1,1,1)`, `C=(0,2,0)`,
`D=(1,1,0)`. These are not the z-probes `A=(0,0,1)`, `B=(1,1,1)`,
`C=(0,0,2)`, `D=(1,0,1)`. `A` is not a seed. Same process and x-probes as
nszopinx #7188.

Lock alphabet of the displayed process: `{±e_i}` with `i` in `{1,2,3}`.

Seed: the three-record set `{0, (0,0,1), (0,0,-1)}` is recorded at formation
tick 0 with locks `L(0)=+e_1`, `L(0,0,1)=−e_1`, and `L(0,0,-1)=−e_1`. The
third site is the z-mirror of the two-site opposite-lock partner `(0,0,1)`.
This seed is not the two-site opposite-lock seed `{0,(0,0,1)}` and not the
three-site opposite-lock seed whose third site is `(1,0,0)` with lock `+e_2`.
This seed is not the perp two-site seed `+e_1/+e_2`. This seed is not the
y-symmetric three-site seed `{0,(0,1,0),(0,-1,0)}`. This seed is not the
x-symmetric three-site seed `{0,(1,0,0),(-1,0,0)}`. Same process as nszmenu
#7188 and as nmcfail cover on these x-probes.

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

Let `t(q)` be the formation tick of x-probe `q` when that tick is defined in
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
dot `-1`. Axis-cover of `M` and `O` is a leftover comparison: cover HOLDs
only when axes are disjoint and the unsigned union equals `{e_1,e_2,e_3}`.
nmcfail cover reverse FAIL face FAIL on these same probes because the
union misses `e_3` at `A`, `C`, and `D`; axes still disjoint. Forall-perp
does not demand that union.

Reverse from forall-perp at `τ` HOLDs if and only if forall-perp HOLDs at
`A` and at `B`. Face likewise on `C,D`. Empty or `UNDEFINED` on either
side of a comparison is `UNDEFINED`; else a fail on either side fails.

Identifying a named sign of those locks with reverse or face is refused:
named-sign lettering lost the axis. Reverse and face are scored from
forall-perp of `M` versus `O` at the named probes. They are not an
occupancy-kernel inner product.

## Theorem 1 — ticks, `M`, `O`, dots, and forall-perp at `τ=t+1`

On this process the four x-probes form. Compare to nmcfail cover: that
leftover reports complementary occupation of `{e_1,e_2,e_3}` by `Axis(M)`
and `Axis(O)`, reverse fail, and face fail. Compare to nszmenu #7205: that
leftover reports `M` exist-opposite reverse fail and face fail. Here `M`
and `O` are read together at `τ=t+1` and scored by forall-perp:

```text
t(A)=3
t(B)=2
t(C)=4
t(D)=2
M(A, τ) = {+e_2, −e_2}
M(B, τ) = {+e_1}
M(C, τ) = {+e_1}
M(D, τ) = {+e_1}
O(A, τ) = {+e_1}
O(B, τ) = {+e_2, −e_2, +e_3}
O(C, τ) = {+e_2, −e_2}
O(D, τ) = {+e_2, −e_2}
(+e_2)·(+e_1)=0, (−e_2)·(+e_1)=0
(+e_1)·(+e_2)=0, (+e_1)·(−e_2)=0, (+e_1)·(+e_3)=0
(+e_1)·(+e_2)=0, (+e_1)·(−e_2)=0
(+e_1)·(+e_2)=0, (+e_1)·(−e_2)=0
forall-perp(A)=hold
forall-perp(B)=hold
forall-perp(C)=hold
forall-perp(D)=hold
cover(A) = fail
cover(B) = hold
cover(C) = fail
cover(D) = fail
```

`A` is not a seed. Mixed remains a set: `M(A,τ)` has two earliest incoming
steps and `O(B,τ)` has three outgoing steps. Unique letters would assign
`UNDEFINED` at mixed probes. Here uniqueness is not required.
Every displayed integer dot is 0. Empty `O` at `t` makes forall-perp
`UNDEFINED` at each x-probe at the own-tick cut, while nmcfail cover
fails on empty `O`. At `τ=t+1` both families are nonempty. O is not M.
No six-neighbor star.

At `A`, `C`, and `D`, nmcfail cover fails because the unsigned union
misses `e_3`; axes still disjoint. Forall-perp HOLDs at those probes
because every incoming letter is orthogonal to every outgoing letter.
Does forall `m·o=0` HOLD where cover fails? Yes. At `B` both cover and
forall-perp HOLD. Perp versus cover split.

This is not leftover of exist-perp: some pair with integer dot 0 is a
weaker leftover. On the nstri three-site leftover, forall-perp fails at
`B` because `+e_1` sits in both `M(B,τ)` and `O(B,τ)` with `+e_1·+e_1=1`,
while exist-perp still HOLDs at `B`. This is not leftover of empty
intersection: `{+e_1}` and `{−e_1}` are disjoint and have integer dot
`-1`. This is not leftover of nmcfail cover. This is not leftover of
nszmenu #7205 M exist-opposite. This is not leftover of nstri forall-perp
fail at B. This is not leftover of unique own-incoming or own-outgoing
letters. This is not leftover of nszopinx same-tick-inclusive six-neighbor
lock union.

New records in `B_3(0)` between `t` and `t+1` that meet a probe's
six-neighbors enter `O` and do not enter earliest `M`:

```text
new 6-NN of A at t(A)+1: (2, 0, 0)
new 6-NN of B at t(B)+1: (1, 2, 1), (1, 0, 1), (1, 1, 2)
new 6-NN of C at t(C)+1: (2, 1, 0), (2, -1, 0)
new 6-NN of D at t(D)+1: (1, 2, 0), (1, 0, 0)
```

## Theorem 2 — reverse from forall-perp at `τ`

Reverse from forall-perp holds if and only if forall-perp HOLDs at `A` and
at `B`. Both reports are hold. Reverse holds.

Reverse from forall-perp at τ: hold

nmcfail cover reverse fails because cover fails at `A` (union misses
`e_3`; axes still disjoint). Forall-perp reverse HOLDs because every pair
at `A` and at `B` has integer dot 0. Unique own-incoming letters on these
x-probes report reverse `UNDEFINED` from mixed `M(A,τ)`. Same-tick-inclusive
six-neighbor lock union leftover is a different object. Exist-opposite of
`M` reports reverse fail from `{+e_2, −e_2}` at `A` against `{+e_1}` at
`B`. Exist-perp leftover also reports reverse hold here, but fails to
separate this member from nstri, where exist-perp reverse HOLDs and
forall-perp reverse fails. Those are different objects. Reverse from
forall-perp holds at `τ` because every incoming letter at `A` is orthogonal
to every outgoing letter at `A`, and likewise at `B`.

Reverse holds.

## Theorem 3 — face from forall-perp at `τ`

Face from forall-perp holds if and only if forall-perp HOLDs at `C` and at
`D`. Both reports are hold. Face holds.

Face from forall-perp at τ: hold

Displayed, not adopted. The bits are not written into Admissibility.
Do not write into Admissibility. Do not attach L1. nmcfail cover face
fails because cover fails at `C` and at `D` (union misses `e_3`; axes
still disjoint). Unique own-outgoing letters on these x-probes report
face `UNDEFINED` from mixed `O` at `C`. nszmenu #7205 leftover reports
face fail from exist-opposite of `M`. Those are different objects. Face
from forall-perp holds at `τ` because every incoming letter at `C` is
orthogonal to every outgoing letter at `C`, and likewise at `D`.

At the same cut, forall-perp HOLDs at all four probes, so reverse HOLDs
and face HOLDs. nmcfail cover reverse FAIL face FAIL. Simultaneous HOLD
of exist-perp does not name this predicate. Empty intersection at a
formed probe does not name this predicate. Cover fail at `A`, `C`, and
`D` does not name this predicate.

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
- It does not reprint unique own-incoming or own-outgoing lock-vector
  letters on these x-probes as the object.
- It does not reprint nmcfail cover reverse fail and face fail.
- It does not reprint nszmenu #7205 M exist-opposite fail/fail.
- It does not reprint exist-perp as the scored predicate.
- It does not reprint empty intersection as orthogonality.
- It does not reprint nstri forall-perp fail at B as this member.
- It does not reprint nszopinx same-tick-inclusive six-neighbor lock union.
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
z-symmetric three-site process, the incoming and outgoing sets at `t+1`, the
integer dots, the forall-perp reports, and reverse/face from those reports are
displayed theorem-domain data.

## Exact target and obligation graph

| Obligation | Status |
|---|---|
| current Lattice / Admissibility / Record premises | quoted; no edit |
| perp-step incoming-lock process on `B_3(0)` | displayed; nszopinx #7188 seed `+e_1/−e_1/−e_1` |
| ticks `t(A)`, `t(B)`, `t(C)`, `t(D)` | Theorem 1; `3`, `2`, `4`, `2` |
| `M` at `τ=t+1` | Theorem 1; frozen incoming sets |
| `O` at `τ=t+1` | Theorem 1; nonempty outgoing duals |
| integer dots of `M` versus `O` at `τ` | Theorem 1; every displayed pair is 0 |
| forall-perp at `A,B,C,D` | Theorem 1; hold at each |
| reverse from forall-perp at `τ` | Theorem 2; hold |
| face from forall-perp at `τ` | Theorem 3; hold |
| compare to nmcfail cover fail | Theorem 1; cover fail, hold, fail, fail; forall-perp hold at each |
| unique incoming or outgoing lock | not required |
| occupancy `n` as the letter | not used |
| named-sign `{+,−}` letter | not used; lost the axis |
| singleton unique lock-vector letter | not used as the object; mixed remains a set |
| `Z^3` sum of the lock set | not used; no aggregation |
| six-neighbor star as the letter | not used |
| leftover of exist-perp | not this display |
| leftover of nmcfail cover | not this display |
| leftover of empty intersection | not this display |
| leftover of nstri forall-perp fail at B | not this display |
| leftover of nszmenu #7205 M exist-opposite | not this display |
| leftover of unique own-incoming or own-outgoing letters | not this display |
| leftover of nszopinx six-neighbor lock union | not this display |
| global later T | not used |
| forall-perp as Admissibility content | not adopted |
| formation site / probability / rate | open |
| physical Record readout of the bits | open |

## Value gate (V1–V5)

| # | Answer |
|---|---|
| V1 | It answers the first-display question: forall-orthogonal `M` versus `O` at `t+1` on the four #7188 x-probes, and reverse/face from that, on the nmcfail cover-FAIL member. |
| V2 | Current main has no landed forall-orthogonal incoming-versus-outgoing reverse/face at `t+1` on these four #7188 x-probes. |
| V3 | Own incoming sets, own outgoing sets, integer dots, forall-perp reports, and the `hold`/`fail`/`UNDEFINED` reverse/face bits are independently finite and exact. |
| V4 | The theorem is more than a restatement of Record because it reads both duals at one cut and scores every integer dot, not complementary axis-cover and not existence of an opposite pair. |
| V5 | It is not an adopted content rule: the bits remain displayed. |

## No-go discipline gate

The negative content is narrow: the display does not write those bits into
Admissibility, does not reduce them to named signs, does not require a
unique letter, does not replace `O` by `M`, does not replace either set by
six-neighbor lock union, does not identify this display with exist-perp,
does not identify the bits with nmcfail cover, does not identify
orthogonality with empty intersection, does not identify the bits with
nstri forall-perp fail at B, and does not identify the bits with nszmenu
#7205 M exist-opposite fail/fail. No global impossibility is claimed.

### N1 — materially distinct routes

| Route | Attempt | Why it fails here | Marker |
|---|---|---|---|
| exist-perp | score some pair with integer dot 0 | weaker leftover; nstri `B` has exist-perp hold and forall-perp fail from `+e_1·+e_1=1` | ATTEMPTED |
| nmcfail cover | score complementary occupation of `{e_1,e_2,e_3}` | cover reverse FAIL face FAIL because the union misses `e_3`; forall-perp reverse HOLD face HOLD; axes still disjoint | ATTEMPTED |
| empty intersection | treat `M ∩ O = {}` as the predicate | `{+e_1}` and `{−e_1}` are disjoint and have integer dot `-1` | ATTEMPTED |
| nstri forall-perp fail at B | reuse the three-site leftover whose third seed is `(1,0,0)` with lock `+e_2` | different seed; that leftover reports reverse fail | ATTEMPTED |
| nszmenu #7205 M exist-opposite | reuse signed reverse fail and face fail of `M` | those bits fail for a signed pair across probes; forall-perp HOLDs at each probe | ATTEMPTED |
| unique own letter | replace mixed `M` or `O` by a singleton or `UNDEFINED` | `M(A,τ)` has two incoming steps and `O(B,τ)` has three outgoing steps; mixed remains a set; unique-letter reverse from `M` is `UNDEFINED` | ATTEMPTED |
| same-tick-inclusive six-neighbor lock union | score locks of six-neighbors formed by `t(q)` | that leftover is a six-neighbor star; forall-perp reads `M` versus `O` dots | ATTEMPTED |
| z-probes | score `A=(0,0,1)` | different probes; this member scores the #7188 x-probes | ATTEMPTED |
| two-site opposite-lock seed | drop the z-mirror `(0,0,−1)` | different process; `M(A)` then includes `+e_3` | ATTEMPTED |
| y-probes | score `A=(0,1,0)` | different probes; this member scores the #7188 x-probes | ATTEMPTED |
| sum of `M` or `O` | replace each set by its `Z^3` sum | mixed `M(A)` sums to the origin; forall-perp reads pairs, not a sum | ATTEMPTED |
| named-sign lettering | collapse `{±e_i}` to `{+,−}` | named-sign lettering lost the axis | ATTEMPTED |
| global later T | wait until `max t(A,B,C,D)` before reading the sets | `τ(q)=t(q)+1` is per-probe; no global T | ATTEMPTED |
| attach a formation member from already-recorded six-neighbor locks | form the probes by a neighbor-lock letter instead of perp-step | refused; not attached | ATTEMPTED |
| adopt bits into Admissibility | rewrite the local rule by forall-perp | refused; displayed, not adopted | ATTEMPTED |

### N2 — wall independence

Missing physical adoption, missing identification of forall-perp with
nmcfail cover, missing identification of forall-perp with exist-perp, and
missing Record identification of orthogonality are distinct open premises.
This note claims no complete wall collection.

### N3 — hidden-condition scan

The host `B_3(0)`, z-symmetric three-site seed locks `+e_1`, `−e_1`, and
`−e_1`, perpendicular step rule, incoming-step lock, own incoming set and
own outgoing dual from records with tick `<= τ`, per-probe `τ=t+1`,
forall-perp of every integer dot, four x-probes with non-seed `A`, empty
or `UNDEFINED` as `UNDEFINED`, mixed remains a set, and reverse/face from
those reports are declared. No uniqueness of locks, no six-neighbor lock
union as the scored object, no exist-perp as the scored predicate, no
nmcfail cover as the scored predicate, no global later T, no formation
attachment from already-recorded six-neighbor locks, and no Admissibility
rewrite are silently assumed.

### N4 — source residual matching

The current axiom memo supplies cubic sites, `M_2(C)`,
content-conditional-on-formation, and unreadable absence. The residual that
formation site, probability, and rate remain unsupplied is unchanged. The
hold reports do not close that residual.

### N5 — resolution and rhetoric audit

| Resolution | Executed | Not claimed |
|---|---|---|
| per element | each integer dot of an earliest incoming step against an outgoing dual step | no continuum alphabet |
| per site | `A,B,C,D` x-probes on `B_3(0)` only | no other cubic sites |
| per mode | no mode calculation | no spectral exhaustion |
| per block | four incoming sets, four outgoing sets, integer dots, four forall-perp reports, reverse/face | no adopted content law |
| lattice wide | checked and not executed | no lattice-wide lettering rule |

### N6 — live partial-closure paths

Live routes include a later Record content map for reverse/face, a
formation-rate rule, and a physical selector among `{±e_i}`. None is taken
here.

### N7 — hostile steelman

**Steelman:** Because every displayed integer dot is 0, forall-perp is only
exist-perp, or only empty intersection, or only nmcfail cover with the
union demand dropped. nstri is a different seed so it cannot separate the
predicate. Empty `O` at `t` already made reverse `UNDEFINED`, so `t+1` is
tautological because children form. Mixed `A` incoming and mixed `B`
outgoing should make reverse `UNDEFINED`. Cover fail is only empty leftover
`{e_3}`. Named signs should suffice. And HOLD of forall-perp is only
tautological because the step rule is already perpendicular.

**Answer:** Forall-perp scores every pair, not some pair. On the nstri
leftover, exist-perp HOLDs at `B` while forall-perp fails from a shared
`+e_1`. Empty intersection is not orthogonality: `{+e_1}` and `{−e_1}`
are disjoint with integer dot `-1`. nmcfail cover demands complementary
occupation of all three axes; the union misses `e_3` at `A`, `C`, and `D`
so cover reverse FAIL face FAIL, while forall-perp HOLDs because axes
still disjoint. Empty leftover `{e_3}` is not this object. Empty `O` at
`t` makes forall-perp `UNDEFINED` at each x-probe, while cover fails on
empty `O`; the `t+1` cut is the first cut where both families are nonempty
at every scored probe. Mixed `M(A,τ)` and mixed `O(B,τ)` remain sets;
reverse and face hold. Named signs lost the axis. The formation step rule
is perpendicular to the parent lock; forall-perp here is a readout of
already-formed incoming letters against outgoing dual letters at `t+1`,
not a restatement of the step rule and not an Admissibility rewrite.

### N8 — cross-cycle echo

nszopinx #7188 reported reverse hold and face hold from same-tick-inclusive
six-neighbor lock union on these x-probes. nszmenu #7205 reported reverse
fail and face fail from own incoming `M`. nmcfail cover reverse FAIL face
FAIL on these same probes because the union misses `e_3`; axes still
disjoint. Forall-perp HOLDING on five HOLDING-M members is a different
probe family or a different seed. This note is not those displays:
forall-perp of `M` versus `O` is read at `t+1` on the four #7188 x-probes,
every displayed integer dot is 0, reverse HOLDs, and face HOLDs, including
where nmcfail cover fails.

**Gate disposition:** PASS for the forall-orthogonal incoming-versus-outgoing
reverse/face reports above. FAIL / DO NOT SHIP for “the predicate equals
exist-perp,” “the predicate equals nmcfail cover,” “the predicate equals
empty intersection,” “the predicate equals nstri forall-perp fail at B,”
“the predicate equals nszmenu #7205 M exist-opposite fail/fail,” “the
predicate equals the named sign,” “the predicate equals the unique
singleton lock vector,” “the predicate equals six-neighbor lock union,”
“bits are Admissibility,” or “`M` equals `O`.”

## Primary runner

The paired runner builds Euclidean `B_3(0)`, runs the nszopinx #7188
perp-step incoming-lock process, reads each probe's own incoming set and
own outgoing dual from the record prefix at that probe's `t+1`, reports
integer dots and forall-perp, compares those reports to nmcfail cover,
and checks Theorems 1--3. It also checks that empty or `UNDEFINED` is
`UNDEFINED`, that mixed sets remain sets, that exist-perp is a leftover,
that nmcfail cover is a leftover, that empty intersection is not
forall-perp, that nstri forall-perp fail at B is a leftover, that a
formation member from already-recorded six-neighbor locks is not attached,
and that forall-perp HOLDs where cover fails. No runner cache is written.
