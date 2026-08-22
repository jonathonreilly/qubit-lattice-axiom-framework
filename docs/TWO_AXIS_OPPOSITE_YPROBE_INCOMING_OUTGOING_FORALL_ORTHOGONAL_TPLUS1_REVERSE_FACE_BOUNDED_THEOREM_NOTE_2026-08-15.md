---
claim_id: two_axis_opposite_yprobe_incoming_outgoing_forall_orthogonal_tplus1_reverse_face_bounded_theorem_note_2026-08-15
claim_type: bounded_theorem
claim_scope: "Forall-orthogonal M vs O at t+1 on the four y-probes of the two-axis opposite seed, and reverse/face from that, are reported. Displayed, not adopted."
upstream_dependencies:
  - minimal_axioms
runner: scripts/two_axis_opposite_yprobe_incoming_outgoing_forall_orthogonal_tplus1_reverse_face_2026_08_15.py
---

# Forall-Orthogonal Incoming Versus Outgoing Reverse And Face At t+1 On Four Y-Probes Of The Two-Axis Opposite Seed

> **Key terms used in this doc** are indexed A-Z at `docs/KEY_TERMINOLOGY.md`;
> each row points to the canonical source-of-truth doc.

**Date:** 2026-08-15
**Type:** bounded_theorem
**Scope:** forall-orthogonal of earliest incoming set `M` versus outgoing dual
`O` at each probe's `τ=t+1`, and reverse/face from that predicate, on the
four y-probes of the two-axis opposite seed in `B_3(0)={n:n·n<=9}`. Same
process and y-probes as nm2ax. Let `t(q)` be the formation tick of probe
`q`. Let `τ(q)=t(q)+1`. `M(q,τ)` is the set of earliest incoming
nearest-neighbor steps at `q` using only records with tick `<= τ`. Seeds
are a singleton seed letter. `O(q,τ)` is the outgoing dual of `M`: the set
of `e` in `{±e_1,±e_2,±e_3}` such that `q+e` is formed and `e` is in
`M(q+e,τ)`. Unformed at `τ` is `UNDEFINED`. For formed `q` with both `M`
and `O` defined and nonempty, forall-perp holds if and only if every `m` in
`M(q,τ)` and every `o` in `O(q,τ)` have integer dot `m·o=0`. Empty or
`UNDEFINED` is `UNDEFINED`. Exist-perp (some pair dots to 0) is comparison
only. Reverse holds if and only if forall-perp holds at `A` and at `B`.
Face holds if and only if forall-perp holds at `C` and at `D`. This is not
exist-opposite leftover. Uniqueness of incoming or outgoing locks is not
required. Mixed remains a set. Displayed, not adopted. Do not write into
Admissibility. Do not attach L1.
**Audit-status authority:** independent audit lane only. This note authors no
audit verdict and predicts none.
**Primary runner:**
[`scripts/two_axis_opposite_yprobe_incoming_outgoing_forall_orthogonal_tplus1_reverse_face_2026_08_15.py`](../scripts/two_axis_opposite_yprobe_incoming_outgoing_forall_orthogonal_tplus1_reverse_face_2026_08_15.py)

Framework input:

- [`MINIMAL_AXIOMS_2026-06-29.md`](MINIMAL_AXIOMS_2026-06-29.md) supplies
  cubic-lattice sites `Z^3` with nearest-neighbor adjacency, the one-site
  algebra `M_2(C)`, and the Record sentences that records form and that a
  present record locks exactly one admissible local possibility.

Everything after that quoted input is a finite displayed process on `B_3(0)`
and the four named y-probes. Incoming lock letters are unit nearest-neighbor
steps. `O` is the outgoing dual of those incoming sets at the per-probe cut
`τ=t+1`. Reverse and face are scored on forall-orthogonal of `M` versus `O`
at that same cut. Named signs `{+,−}` are a coarser readout and are not
used. A singleton unique lock letter is a different readout and is not used
as the object. A `Z^3` sum of those locks is a different readout and is not
used. Occupancy `n` is not used. This display does not use occupancy. A
six-neighbor star is not the letter. Exist-opposite of `M` with `M` or of
`O` with `O` is a different predicate and is leftover.

## Machine status and trace

```yaml
actual_current_surface_status: bounded-support
target_claim_type: bounded_theorem
claim_type_reason: "Exact report of forall-orthogonal M versus O at t+1 on the four y-probes of the two-axis opposite seed, integer dots all zero, reverse hold from forall-perp at A and B, face hold from forall-perp at C and D; uniqueness of locks is not claimed and the bits are not adopted."
trace_class: frontier_discovery
target_claim_id: two_axis_opposite_yprobe_incoming_outgoing_forall_orthogonal_tplus1_reverse_face
target_blocker_text: "display forall m in M, o in O have m·o=0 at t+1 on the four y-probes of the two-axis opposite seed, and reverse/face from that, not exist-opposite leftover"
source_of_blocker_text: handoff
reachability_to_target: advances
artifact_role: theorem
next_trace_action: "Keep forall-orthogonal M versus O at t+1 displayed; do not write forall-perp into Admissibility, do not reduce to exist-opposite leftover, do not reduce to exist-perp leftover, do not require a unique letter, and do not attach L1."
conditional_surface_status: "exact on B_3(0) for forall-orthogonal M versus O at t+1 on the four y-probes of the two-axis opposite seed, and reverse/face from that; displayed, not adopted"
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

No larger host is used. The four y-probes are the only sites whose
incoming-versus-outgoing dots are scored:

```text
A = (0,1,0),  B = (1,1,1),  C = (0,2,0),  D = (1,1,0).
```

These are not the x-probes `A=(1,0,0)`, `B=(1,1,1)`, `C=(2,0,0)`,
`D=(1,1,0)`. `A` is a seed. Same process and y-probes as nm2ax.

Lock alphabet of the displayed process: `{±e_i}` with `i` in `{1,2,3}`.

Seed: two disjoint opposite pairs recorded at formation tick 0. The first
pair is `{0, (0,1,0)}` with opposite locks `L(0)=+e_1` and `L(0,1,0)=−e_1`.
The second pair is `{(0,0,1), (0,1,1)}` with opposite locks `L(0,0,1)=+e_2`
and `L(0,1,1)=−e_2`. The second pair is a new seed, not a formed child of
the first pair. On the one-axis opposite two-site process the sites
`(0,0,1)` and `(0,1,1)` form at tick 1 locking `+e_3`; here they are seeds
at tick 0 locking `+e_2` and `−e_2`. This seed is not the perp two-site
seed `+e_1/+e_2`. This seed is not the z-symmetric three-site seed
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

## Named incoming set `M`, outgoing set `O`, and forall-perp at `τ=t+1`

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
does not replace `O` by `M`. Occupancy `n` is not used.

For formed `q` with both `M(q,τ)` and `O(q,τ)` defined and nonempty,
forall-perp holds if and only if every `m` in `M(q,τ)` and every `o` in
`O(q,τ)` have integer dot `m·o=0`. Empty or `UNDEFINED` on either side is
`UNDEFINED`. Nonempty with some pair of nonzero dot fails.

Exist-perp holds if and only if some pair has integer dot zero. Exist-perp
is comparison only. It is not the scored predicate. A pair with
`m={+e_1,+e_2}` and `o={+e_2}` has exist-perp hold and forall-perp fail.

Reverse holds if and only if forall-perp holds at `A` and at `B`. Face
holds if and only if forall-perp holds at `C` and at `D`. If either side of
a reverse or face comparison is `UNDEFINED`, the comparison is
`UNDEFINED`. If either side fails, the comparison fails.

Exist-opposite leftover scores some pair that sums to zero inside `M` or
inside `O` across reverse or face. M reverse uses ±e_1; O reverse uses ±e_3.
That leftover is not this display. On this seed leftover M face fails,
because `M(C,τ)={+e_2}` and `M(D,τ)={−e_3}` share no opposite pair, while
forall-perp at `C` and at `D` both hold. Forall-perp scores every incoming-
versus-outgoing integer dot at one probe, not an opposite pair inside one
named set.

## Theorem 1 — ticks, `M`, `O`, integer dots, and forall-perp at `τ=t+1`

On this process the four y-probes form. Direct enumeration of the displayed
two-axis opposite perp-step incoming-lock process on `B_3(0)` reports:

```text
t(A)=0
t(B)=1
t(C)=1
t(D)=2
M(A, τ) = {−e_1}
M(B, τ) = {+e_1}
M(C, τ) = {+e_2}
M(D, τ) = {−e_3}
O(A, τ) = {+e_2, −e_3}
O(B, τ) = {+e_2, +e_3, −e_3}
O(C, τ) = {+e_1, −e_1, +e_3, −e_3}
O(D, τ) = {+e_1, −e_1}
```

`A` is a seed at tick 0. `B` forms at tick 1 from the second pair. Mixed
remains a set: `O(A,τ)` has two outgoing steps, `O(B,τ)` has three, and
`O(C,τ)` has four. Unique letters would assign `UNDEFINED` at mixed probes.
Here uniqueness is not required. On the one-axis opposite two-site process
the same y-probes form at ticks `0,2,1,3`; here they form at `0,1,1,2`.

Integer dots `m·o` at each probe, in six-neighbor order:

```text
A: (−e_1)·(+e_2)=0, (−e_1)·(−e_3)=0
   forall-perp at A: hold
B: (+e_1)·(+e_2)=0, (+e_1)·(+e_3)=0, (+e_1)·(−e_3)=0
   forall-perp at B: hold
C: (+e_2)·(+e_1)=0, (+e_2)·(−e_1)=0, (+e_2)·(+e_3)=0, (+e_2)·(−e_3)=0
   forall-perp at C: hold
D: (−e_3)·(+e_1)=0, (−e_3)·(−e_1)=0
   forall-perp at D: hold
```

Every scored integer dot is `0`. Forall-perp holds at `A`, `B`, `C`, and
`D`. Exist-perp also holds at each probe on this process because every pair
already dots to zero; that coincidence is comparison only. The predicates
are not the same: exist-perp can hold while forall-perp fails.

## Theorem 2 — reverse hold / fail / UNDEFINED

Reverse holds if and only if forall-perp holds at `A` and at `B`. Both
sides hold. Both sides are nonempty and defined, so this is not
`UNDEFINED`. Reverse is not exist-opposite leftover of `M(A,τ)` against
`M(B,τ)`.

Reverse: hold

This is not `fail` and not `UNDEFINED`. Reverse holds.

Reverse holds.

## Theorem 3 — face hold / fail / UNDEFINED

Face holds if and only if forall-perp holds at `C` and at `D`. Both sides
hold. Both sides are nonempty and defined, so this is not `UNDEFINED`. Face
is not exist-opposite leftover of `M(C,τ)` against `M(D,τ)`. On this seed
leftover M face fails, while forall-perp face holds.

Face: hold

Displayed, not adopted. The bits are not written into Admissibility.
Do not write into Admissibility. Do not attach L1.

This is not `fail` and not `UNDEFINED`. Face holds.

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

This display uses Lattice to name `B_3(0)` and the four y-probes. It uses Qubit
only as the algebra of the local possibility domain. It uses Record only as a
boundary: a present lock is content. It does not rewrite Admissibility. The
two-axis opposite process, the incoming and outgoing sets at `t+1`, the
integer dots, and the forall-perp reverse/face bits are displayed
theorem-domain data.

## Exact target and obligation graph

| Obligation | Status |
|---|---|
| current Lattice / Admissibility / Record premises | quoted; no edit |
| perp-step incoming-lock process on `B_3(0)` | displayed; two-axis opposite seed `+e_1/−e_1` and `+e_2/−e_2` |
| ticks `t(A)`, `t(B)`, `t(C)`, `t(D)` | Theorem 1; `0`, `1`, `1`, `2` |
| `M` at `τ=t+1` | Theorem 1; `{−e_1}`, `{+e_1}`, `{+e_2}`, `{−e_3}` |
| `O` at `τ=t+1` | Theorem 1; outgoing dual |
| integer dots `m·o` at `A,B,C,D` | Theorem 1; all `0` |
| forall-perp at `A,B,C,D` | Theorem 1; `hold` / `hold` / `hold` / `hold` |
| reverse from forall-perp at `A` and `B` | Theorem 2; `hold` |
| face from forall-perp at `C` and `D` | Theorem 3; `hold` |
| unique incoming or outgoing lock | not required |
| occupancy `n` as the letter | not used |
| named-sign `{+,−}` letter | not used; lost the axis |
| singleton unique lock-vector letter | not used as the object; mixed remains a set |
| `Z^3` sum of the lock set | not used; no aggregation |
| six-neighbor star as the letter | not used |
| exist-opposite leftover | not this display; M reverse uses ±e_1; O reverse uses ±e_3; leftover M face fails |
| exist-perp leftover | comparison only |
| global later T | not used |
| forall-perp as Admissibility content | not adopted |
| formation site / probability / rate | open |
| physical Record readout of the bits | open |

## Value gate (V1–V5)

| # | Answer |
|---|---|
| V1 | It answers the first-display question: forall `m` in `M`, `o` in `O` have `m·o=0` at `t+1` on the four y-probes of the two-axis opposite seed, and reverse/face from that. |
| V2 | Current main has no landed forall-orthogonal `M` versus `O` at `t+1` reverse/face on these four y-probes of the two-axis opposite seed. |
| V3 | Integer dots, forall-perp at four probes, and reverse/face are independently finite and exact. |
| V4 | The theorem is more than a restatement of Record because it reads every incoming-versus-outgoing integer dot at `t+1` and scores the universal zero-dot predicate. |
| V5 | It is not an adopted content rule: the bits remain displayed. |

## No-go discipline gate

The negative content is narrow: the display does not write those bits into
Admissibility, does not reduce them to named signs, does not require a
unique letter, does not replace forall-perp by exist-perp, and does not
identify this display with exist-opposite leftover. No global impossibility
is claimed.

### N1 — materially distinct routes

| Route | Attempt | Why it fails here | Marker |
|---|---|---|---|
| exist-opposite leftover | score some pair in `M` or in `O` that sums to zero | leftover M reverse HOLDs from ±e_1 and leftover O reverse HOLDs from ±e_3, but leftover M face fails while forall-perp face holds | ATTEMPTED |
| exist-perp leftover | score some pair with `m·o=0` | comparison only; `{+e_1,+e_2}` versus `{+e_2}` exist-perp HOLDs and forall-perp fails | ATTEMPTED |
| unique letter | replace mixed sets by a singleton or `UNDEFINED` | mixed `O(A,τ)`, `O(B,τ)`, and `O(C,τ)` remain sets; uniqueness is not required | ATTEMPTED |
| intersection as the letter | score reverse/face inside `M ∩ O` | empty intersection is a different report, not forall-perp | ATTEMPTED |
| one-axis leftover seed | treat `(0,0,1)` and `(0,1,1)` as formed children locking `+e_3` | those sites are a new second pair at tick 0 locking `+e_2` and `−e_2` | ATTEMPTED |
| sum of a set | replace each set by its `Z^3` sum | the construction does not sum | ATTEMPTED |
| named-sign lettering | collapse `{±e_i}` to `{+,−}` | named-sign lettering lost the axis | ATTEMPTED |
| global later T | wait until `max t(A,B,C,D)` before reading | `τ(q)=t(q)+1` is per-probe; no global T | ATTEMPTED |
| attach a formation member from already-recorded six-neighbor locks | form the probes by a neighbor-lock letter instead of perp-step | refused; not attached | ATTEMPTED |
| adopt bits into Admissibility | rewrite the local rule by forall-perp | refused; displayed, not adopted | ATTEMPTED |

### N2 — wall independence

Missing physical adoption, missing identification of forall-perp with
exist-opposite, missing identification of forall-perp with exist-perp, and
missing Record identification of the bits are distinct open premises. This
note claims no complete wall collection.

### N3 — hidden-condition scan

The host `B_3(0)`, two disjoint opposite pairs with locks `+e_1`, `−e_1`,
`+e_2`, and `−e_2`, perpendicular step rule, incoming-step lock, own
incoming set and own outgoing dual from records with tick `<= τ`, per-probe
`τ=t+1`, integer dots, forall-perp, four y-probes with seed `A`, reverse as
forall-perp at `A` and `B`, face as forall-perp at `C` and `D`, and mixed
remains a set are declared. No uniqueness of locks, no exist-opposite as
the scored object, no exist-perp as the scored object, no global later T,
no formation attachment from already-recorded six-neighbor locks, and no
Admissibility rewrite are silently assumed.

### N4 — source residual matching

The current axiom memo supplies cubic sites, `M_2(C)`,
content-conditional-on-formation, and unreadable absence. The residual that
formation site, probability, and rate remain unsupplied is unchanged. The
`hold`/`hold` reports do not close that residual.

### N5 — resolution and rhetoric audit

| Resolution | Executed | Not claimed |
|---|---|---|
| per element | each integer dot `m·o` of earliest incoming or outgoing nearest-neighbor step | no continuum alphabet |
| per site | `A,B,C,D` y-probes on `B_3(0)` only | no other cubic sites |
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
exist-opposite HOLD using ±e_1 in `M` and ±e_3 in `O`; mixed `O` should
make the predicate `UNDEFINED`; exist-perp already answers some pair dots
to zero.

**Answer:** Empty intersection is a set-theoretic report. Forall-perp is
the universal integer-dot report at the same cut. Exist-opposite leftover
pairs locks inside `M` or inside `O`; this display pairs every incoming
lock with every outgoing lock at one probe. On this seed leftover M face
fails while forall-perp face holds, so the predicates split. Mixed
`O(A,τ)` remains `{+e_2, −e_3}` and forall-perp at `A` holds. Exist-perp
is comparison only and is a weaker predicate.

### N8 — cross-cycle echo

The one-axis opposite two-site process reports the same y-probes at ticks
`0,2,1,3` with mixed `M(D,τ)`. This note is not that display: the second
pair is a new seed, `B` forms at tick 1, `D` forms at tick 2, `M(D,τ)` is
`{−e_3}`, leftover M face fails, and forall-perp still holds at `A,B,C,D`
with reverse hold and face hold.

**Gate disposition:** PASS for the forall-orthogonal `M` versus `O` at `t+1`
reverse/face reports above. FAIL / DO NOT SHIP for “the predicate equals
exist-opposite leftover,” “the predicate equals exist-perp,” “the predicate
equals the unique singleton lock vector,” “bits are Admissibility,”
“reverse fails,” or “face is `UNDEFINED`.”

## Primary runner

The paired runner builds Euclidean `B_3(0)`, runs the two-axis opposite
perp-step incoming-lock process, reads each probe's own earliest incoming
set and own outgoing dual from the record prefix at that probe's `t+1`,
lists every integer dot `m·o`, scores forall-perp at `A,B,C,D`, and checks
Theorems 1--3. It also checks that exist-perp is comparison only, that
exist-opposite leftover of `M` uses ±e_1 and leftover of `O` uses ±e_3,
that leftover M face fails, that mixed sets remain sets, that uniqueness is
not required, that occupancy `n` is not used, and that a formation member
from already-recorded six-neighbor locks is not attached. No runner cache
is written.
