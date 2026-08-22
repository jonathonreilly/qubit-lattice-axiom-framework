---
claim_id: y_symmetric_three_site_incoming_outgoing_forall_orthogonal_tplus1_reverse_face_bounded_theorem_note_2026-08-15
claim_type: bounded_theorem
claim_scope: "Forall-orthogonal M vs O at t+1 on the four #7211 y-probes, and reverse/face from that, are reported. Displayed, not adopted."
upstream_dependencies:
  - minimal_axioms
runner: scripts/y_symmetric_three_site_incoming_outgoing_forall_orthogonal_tplus1_reverse_face_2026_08_15.py
---

# Forall-Orthogonal M Versus O At t+1 Reverse And Face On Four #7211 Y-Probes

> **Key terms used in this doc** are indexed A-Z at `docs/KEY_TERMINOLOGY.md`;
> each row points to the canonical source-of-truth doc.

**Date:** 2026-08-15
**Type:** bounded_theorem
**Scope:** forall-orthogonal `M` versus `O` at `t+1` on the four nmsyop
#7211 y-probes in `B_3(0)={n:n·n<=9}`, no global T, and reverse/face from
that. Same process and y-probes as nmsyop #7211 / nsyopp #7132. Let `t(q)`
be the formation tick of probe `q`. Let `τ(q)=t(q)+1`. `M(q,τ)` is the set
of earliest incoming nearest-neighbor steps at `q` using only records with
tick `<= τ`. `O(q,τ)` is the outgoing dual of `M`: the set of `e` in
`{±e_1,±e_2,±e_3}` such that `q+e` is formed in `B_3(0)` and `e` is in
`M(q+e,τ)`. Unformed at `τ` is `UNDEFINED`. Forall-perp holds if and only
if every `m` in `M(q,τ)` and every `o` in `O(q,τ)` have `m·o=0`. Empty or
`UNDEFINED` is `UNDEFINED`. Reverse HOLD if and only if forall-perp at `A`
and at `B`. Face likewise on `C,D`. Uniqueness is not required. Mixed
remains a set. This is not leftover of existential opposite of `M` versus
`O`. This is not leftover of unique own-incoming or own-outgoing letters.
This is not leftover of existential opposite inside `M` or inside `O`.
Occupancy `n` is not used. Displayed, not adopted. Do not write into
Admissibility. Do not attach L1.
**Audit-status authority:** independent audit lane only. This note authors no
audit verdict and predicts none.
**Primary runner:**
[`scripts/y_symmetric_three_site_incoming_outgoing_forall_orthogonal_tplus1_reverse_face_2026_08_15.py`](../scripts/y_symmetric_three_site_incoming_outgoing_forall_orthogonal_tplus1_reverse_face_2026_08_15.py)

Framework input:

- [`MINIMAL_AXIOMS_2026-06-29.md`](MINIMAL_AXIOMS_2026-06-29.md) supplies
  cubic-lattice sites `Z^3` with nearest-neighbor adjacency, the one-site
  algebra `M_2(C)`, and the Record sentences that records form and that a
  present record locks exactly one admissible local possibility.

Everything after that quoted input is a finite displayed process on `B_3(0)`
and the four named y-probes. Incoming lock letters are unit nearest-neighbor
steps. `O` is the outgoing dual of those incoming sets at the per-probe cut
`τ=t+1`. Reverse and face are scored on forall-perp of `M` versus `O` at
each probe, then conjoined on `{A,B}` and `{C,D}`. Named signs `{+,−}` are a
coarser readout and are not used. A singleton unique lock letter is a
different readout and is not used as the object. A `Z^3` sum of those locks
is a different readout and is not used. The construction does not sum. The
display does not use occupancy. A six-neighbor star is not the letter.

## Machine status and trace

```yaml
actual_current_surface_status: bounded-support
target_claim_type: bounded_theorem
claim_type_reason: "Exact report of M and O at t+1 on the four #7211 y-probes, all pair dots, forall-perp hold at A,B,C,D, reverse hold, and face hold; uniqueness of locks is not claimed and the bits are not adopted."
trace_class: frontier_discovery
target_claim_id: y_symmetric_three_site_incoming_outgoing_forall_orthogonal_tplus1_reverse_face
target_blocker_text: "display forall-orthogonal M versus O at t+1 on the four #7211 y-probes, and reverse/face from that, no global T"
source_of_blocker_text: handoff
reachability_to_target: advances
artifact_role: theorem
next_trace_action: "Keep reverse and face displayed; do not write forall-perp into Admissibility, do not reduce to a unique letter, do not replace forall-perp by existential opposite, do not replace M or O by six-neighbor lock union, do not use occupancy n, and do not wait for a global later T."
conditional_surface_status: "exact on B_3(0) for forall-orthogonal M versus O at t+1 reverse/face on the four #7211 y-probes, no global T; displayed, not adopted"
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

No larger host is used. The four y-probes are the only sites whose `M` and
`O` at `t+1` are scored:

```text
A = (0,1,0),  B = (1,1,1),  C = (0,2,0),  D = (1,1,0).
```

These are not the x-probes `A=(1,0,0)`, `B=(1,1,1)`, `C=(2,0,0)`,
`D=(1,1,0)`. `A` is a seed. Same process and y-probes as nmsyop #7211.

Lock alphabet of the displayed process: `{±e_i}` with `i` in `{1,2,3}`.

Seed: the three-record set `{0, (0,1,0), (0,-1,0)}` is recorded at formation
tick 0 with locks `L(0)=+e_1`, `L(0,1,0)=−e_1`, and `L(0,-1,0)=−e_1`. The
third site is the y-mirror of the two-site opposite-lock partner `(0,1,0)`.
This seed is not the two-site opposite-lock seed `{0,(0,1,0)}` and not the
three-site opposite-lock seed whose third site is `(1,0,0)` with lock `+e_2`.
This seed is not the perp two-site seed `+e_1/+e_2`. This seed is not the
z-symmetric three-site seed `{0,(0,0,1),(0,0,-1)}`.

From a recorded site `p` with lock `L_in(p)=±e_i`, a six-neighbor step
`s in NN` to `q=p+s` is allowed if and only if `s` is perpendicular to
`e_i`, that is

```text
s · e_i = 0.
```

If `q` lies in `B_3(0)`, is still unformed, and the step is allowed, then `q`
forms next and locks the incoming step `s`. If several allowed parents reach
`q` at the same earliest formation, each such incoming step is kept. A later
parent does not re-form `q`. Uniqueness is not required.

## Named sets `M` and `O` at `t+1`

Let `t(q)` be the formation tick of y-probe `q` when that tick is defined in
`B_3(0)`. Let `τ(q)=t(q)+1`. There is no global T.

`M(q,τ)` is the set of earliest incoming nearest-neighbor steps at `q`
using only records with tick `<= τ`. If `q` is unformed at `τ`, then
`M(q,τ)` is `UNDEFINED`. If `q` is a seed and `τ >= 0`, then `M(q,τ)` is
the singleton seed letter. Duplicate incoming steps collapse in the set.

`O(q,τ)` is the outgoing dual of `M`: the set of `e` in `{±e_1,±e_2,±e_3}`
such that `q+e` is formed in `B_3(0)` and `e` is in `M(q+e,τ)`. If `q` is
unformed at `τ`, then `O(q,τ)` is `UNDEFINED`. Empty `O` is empty, not
`UNDEFINED`. `O` is not `M`. The construction does not require `M` or `O`
to be a singleton. It does not sum. It does not replace `M` or `O` by locks
of six-neighbors of `q`. It does not wait for a global later T. Occupancy
`n` is not used.

Forall-perp at a probe holds if and only if that probe is formed by `τ` and
every `m` in `M(q,τ)` and every `o` in `O(q,τ)` have `m·o=0`. Empty or
`UNDEFINED` on either side is `UNDEFINED`; nonempty with a nonzero pair
fails. Reverse HOLD if and only if forall-perp at `A` and at `B`. Face HOLD
if and only if forall-perp at `C` and at `D`. Fail on either side of a pair
makes the pair fail. Else a missing side is `UNDEFINED`. Displayed, not
adopted.

Identifying a named sign of those locks with reverse or face is refused:
named-sign lettering lost the axis. Reverse and face are scored on forall
orthogonality of incoming versus outgoing vectors at `t+1`. They are not an
existential opposite inside one set, and they are not an occupancy-kernel
inner product.

## Theorem 1 — ticks, `M`, `O`, dots, and forall-perp at `t+1`

On this process the four y-probes form. At each probe's own `τ=t+1`:

```text
t(A)=0
t(B)=2
t(C)=1
t(D)=3
M(A, τ) = {−e_1}
M(B, τ) = {+e_1}
M(C, τ) = {+e_2}
M(D, τ) = {−e_2, +e_3, −e_3}
O(A, τ) = {+e_2, +e_3, −e_3}
O(B, τ) = {+e_2, +e_3, −e_3}
O(C, τ) = {+e_1, −e_1, +e_3, −e_3}
O(D, τ) = {+e_1, −e_1}
dots(A) = 0,0,0
dots(B) = 0,0,0
dots(C) = 0,0,0,0
dots(D) = 0,0,0,0,0,0
forall-perp at A: hold
forall-perp at B: hold
forall-perp at C: hold
forall-perp at D: hold
```

`A` is a seed at tick 0, so `M(A,τ)` stays the singleton seed letter
`{−e_1}`. Mixed remains a set: `M(D)` has three earliest incoming steps
`−e_2`, `+e_3`, and `−e_3`, and `O(A)` has three outgoing steps `+e_2`,
`+e_3`, and `−e_3`. Unique-L leftover would assign those mixed sets
`UNDEFINED`. Here uniqueness is not required. `O` is disjoint from `M` at
every scored probe. Every listed pair has inner product zero, so forall-perp
holds at `A`, `B`, `C`, and `D`.

New records in `B_3(0)` that meet a probe's six-neighbors at `t+1` enter
`O` when the step from the probe is an earliest incoming step of that
neighbor, and they do not enter earliest `M`:

```text
new 6-NN of A at t(A)+1: (0, 2, 0), (0, 1, 1), (0, 1, -1)
new 6-NN of B at t(B)+1: (1, 2, 1), (1, 1, 2), (1, 1, 0)
new 6-NN of C at t(C)+1: (1, 2, 0), (-1, 2, 0), (0, 2, 1), (0, 2, -1)
new 6-NN of D at t(D)+1: (2, 1, 0)
```

This is not leftover of unique own-incoming or own-outgoing letters: that
readout would replace mixed `O(A)` and mixed `M(D)` by `UNDEFINED`. This is
not leftover of existential opposite of `M` versus `O`: that leftover fails
at each probe because no pair `(m,o)` sums to zero, while forall-perp holds.
This is not leftover of existential opposite inside `M` or inside `O`. This
display does not use occupancy.

## Theorem 2 — reverse

Reverse holds if and only if forall-perp at `A` and at `B`. Both sides hold
and both sides are nonempty and defined, so reverse holds. This is not
`UNDEFINED`. Reverse HOLD uses mixed `O(A)` against singleton `M(A)`, and
mixed `O(B)` against singleton `M(B)`. Empty `O` at formation tick `t` would
make forall-perp at `A` `UNDEFINED`; the scored cut is `t+1`.

Reverse: hold

## Theorem 3 — face

Face holds if and only if forall-perp at `C` and at `D`. Both sides hold
and both sides are nonempty and defined, so face holds. Mixed `M(D)` remains
the three-element set `{−e_2, +e_3, −e_3}` against `O(D)={+e_1, −e_1}`. All
six pair dots are zero. Unique-L leftover would make face `UNDEFINED` from
that mix.

Face: hold

Displayed, not adopted. The bits are not written into Admissibility.
Do not write into Admissibility. Do not attach L1.

This is not leftover of unique own-incoming or own-outgoing letters (reverse
and face `UNDEFINED`). This is not leftover of existential opposite of `M`
versus `O` (fail at each probe). This is not leftover of existential
opposite inside `M` or inside `O` (those leftovers hold on this process for
a different predicate). This is not leftover of same-tick-inclusive
six-neighbor lock union.

## What this note does not claim

- It does not select a unique incoming or outgoing lock.
- It does not reduce lock vectors to named signs `{+,−}`.
- It does not require `M` or `O` to be a singleton.
- It does not sum `M` or `O`.
- It does not replace `M` or `O` by locks of six-neighbors.
- It does not score existential opposite of `M` versus `O`.
- It does not score existential opposite inside `M` or inside `O`.
- It does not wait for a global later T.
- It does not use occupancy `n`.
- It does not attach a formation member from already-recorded six-neighbor
  locks.
- It does not enlarge the host beyond `B_3(0)`.
- It does not edit Lattice, Qubit, Admissibility, or Record.
- It does not supply a physical rate or a continuum kernel.

## Current premise boundary

Physical sites are the points of the cubic lattice `Z^3`, with
nearest-neighbor adjacency.

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
y-symmetric three-site process, `M` and `O` at `t+1`, the pair dots, and the
forall-perp reverse/face bits are displayed theorem-domain data.

## No-Go Discipline Gate

The negative content here is only the bounded refusal to adopt the bits as
Admissibility, to identify forall-perp with existential opposite, to require
a unique letter, or to identify `M` or `O` with six-neighbor lock union. It
is not a claim that reverse cannot fail on another process.

### N1

| Route | Attempt | Why it fails here | Marker |
|---|---|---|---|
| unique letter | replace mixed `O(A)` or mixed `M(D)` by a singleton or `UNDEFINED` | mixed remains a set; unique-letter reverse and face are `UNDEFINED` while set reverse and face hold | ATTEMPTED |
| existential opposite of `M` versus `O` | score some `m+o=0` at a probe | that leftover fails at `A,B,C,D`; forall-perp holds because every pair has inner product zero | ATTEMPTED |
| existential opposite inside `M` or inside `O` | score reverse from `M(A)` against `M(B)`, or `O(A)` against `O(B)` | different predicate; those leftovers hold here, but they are not forall-perp of `M` versus `O` | ATTEMPTED |
| same-tick-inclusive six-neighbor lock union | score locks of six-neighbors formed by `τ` against `O` | that leftover at `A` includes `+e_2` from `C`, which is also in `O(A)`, so a pair has inner product one and leftover reverse fails | ATTEMPTED |
| empty `O` at formation tick `t` | score forall-perp at `t` instead of `t+1` | `O(A,t)` is empty, so forall-perp at `A` is `UNDEFINED`; the scored cut is `t+1` | ATTEMPTED |
| sum of `M` or `O` | replace each set by its `Z^3` sum | the construction does not sum; mixed `O(A)` cancels to `+e_2` while the set stays three elements | ATTEMPTED |
| named-sign lettering | collapse `{±e_i}` to `{+,−}` | named-sign lettering lost the axis | ATTEMPTED |
| occupancy `n` | assign one letter from occupancy | occupancy `n` is not used | ATTEMPTED |
| global later T | wait until `max t(A,B,C,D)` before reading `M` and `O` | `τ(q)=t(q)+1` is per-probe; no global T | ATTEMPTED |
| attach a formation member from already-recorded six-neighbor locks | form the probes by a neighbor-lock letter instead of perp-step | refused; not attached | ATTEMPTED |
| adopt bits into Admissibility | rewrite the local rule by forall-perp | refused; displayed, not adopted | ATTEMPTED |

### N2 — wall independence

Missing physical adoption, missing identification of forall-perp with
existential opposite, and missing Record identification of orthogonality are
distinct open premises. This note claims no complete wall collection.

### N3 — hidden-condition scan

The host `B_3(0)`, y-symmetric three-site seed locks `+e_1`, `−e_1`, and
`−e_1`, perpendicular step rule, incoming-step lock, own earliest incoming
set from records with tick `<= τ`, outgoing dual of that set, per-probe
`τ=t+1`, forall-perp of `M` versus `O`, four y-probes with seed `A`, and
reverse/face as conjunction of those bits are declared. No uniqueness of
locks, no six-neighbor lock union as the scored object, no occupancy `n`,
no global later T, no formation attachment from already-recorded
six-neighbor locks, and no Admissibility rewrite are silently assumed.

### N4 — source residual matching

The current axiom memo supplies cubic sites, `M_2(C)`,
content-conditional-on-formation, and unreadable absence. The residual that
formation site, probability, and rate remain unsupplied is unchanged. The
`hold`/`hold` reports do not close that residual.

### N5 — resolution and rhetoric audit

| Resolution | Executed | Not claimed |
|---|---|---|
| per element | each pair `(m,o)` with `m` in `M(q,t+1)` and `o` in `O(q,t+1)` | no continuum alphabet |
| per site | `A,B,C,D` y-probes on `B_3(0)` only | no other cubic sites |
| per mode | no mode calculation | no spectral exhaustion |
| per block | four `(M,O)` pairs at `t+1` and forall-perp reverse/face | no adopted content law |
| lattice wide | checked and not executed | no lattice-wide lettering rule |

### N6 — live partial-closure paths

Live routes include a later Record content map for reverse/face, a
formation-rate rule, and a physical selector among `{±e_i}`. None is taken
here.

### N7 — hostile steelman

**Steelman:** `M` and `O` should be opposite rather than orthogonal, so
reverse should fail; mixed `O(A)` and mixed `M(D)` should make the bits
`UNDEFINED`; six-neighbor lock union already answered reverse fail on this
same process; unique letters already answered `UNDEFINED`; existential
opposite inside `M` already answered reverse hold on #7211; empty `O` at
`t` already answered `UNDEFINED`; named signs should suffice; occupancy `n`
should track the vector; and forall-perp HOLD is only tautological because
perp-step forbids a parallel child.

**Answer:** Forall-perp scores `m·o=0` for every pair, not `m+o=0`. Mixed
sets remain sets; unique-letter reverse and face are `UNDEFINED` while the
set bits hold. Six-neighbor lock union is a different object and reports
reverse fail against `O`. Existential opposite of `M` versus `O` fails at
every probe. Existential opposite inside `M` or inside `O` is a different
predicate. Empty `O` at `t` is not the scored cut. Named signs lost the
axis. Occupancy `n` is not used. Perp-step constrains which children form;
forall-perp at `t+1` is the displayed fact that those children lock steps
orthogonal to the parent's own earliest incoming set. It is not an
Admissibility rewrite.

### N8 — cross-cycle echo

A unique own-incoming lock-vector display on these same #7211 y-probes
assigned `−e_1`, `+e_1`, `+e_2`, `UNDEFINED` and reported reverse hold with
face `UNDEFINED`. The nmsyop #7211 own-incoming display reported reverse
hold and face hold from existential opposite inside `M`. The nmoutsy and
nmot2sy outgoing displays scored existential opposite inside `O`, with empty
`O` at `t` and a larger `O` at `t+1`. This note is not those displays: the
object is forall-orthogonal `M` versus `O` at `t+1`, reverse holds, and
face holds.

**Gate disposition:** PASS for the forall-orthogonal `M` versus `O` at
`t+1` reverse/face reports above. FAIL / DO NOT SHIP for “the predicate
equals the named sign,” “the predicate equals the unique singleton lock
vector,” “the predicate equals existential opposite of `M` versus `O`,”
“the predicate equals existential opposite inside `M` or inside `O`,” “the
predicate equals six-neighbor lock union,” “bits are Admissibility,”
“reverse fails,” “face is `UNDEFINED`,” or “empty `O` at `t` is the scored
cut.”

## Primary runner

The paired runner builds Euclidean `B_3(0)`, runs the nsyopp #7132 perp-step
incoming-lock process, reads each probe's own earliest incoming set and
outgoing dual from the record prefix at that probe's `t+1`, lists pair dots,
and checks Theorems 1--3. It also checks that mixed sets remain sets, that
unique-letter reverse and face are `UNDEFINED`, that existential opposite of
`M` versus `O` fails, that existential opposite inside `M` or inside `O` is
a leftover, that empty `O` at `t` is empty not `UNDEFINED`, that
six-neighbor lock union leftover fails reverse, that the construction does
not sum, that occupancy `n` is not used, that a formation member from
already-recorded six-neighbor locks is not attached, and that the display is
not those leftovers. No runner cache is written.
