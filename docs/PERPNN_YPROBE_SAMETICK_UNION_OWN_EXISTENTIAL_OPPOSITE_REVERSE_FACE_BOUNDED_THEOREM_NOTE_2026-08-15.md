---
claim_id: perpnn_yprobe_sametick_union_own_existential_opposite_reverse_face_bounded_theorem_note_2026-08-15
claim_type: bounded_theorem
claim_scope: "Reverse and face from same-tick ∪ own incoming lock on the four perpnn y-probes are reported. Displayed, not adopted."
upstream_dependencies:
  - minimal_axioms
runner: scripts/perpnn_yprobe_sametick_union_own_existential_opposite_reverse_face_2026_08_15.py
---

# Same-Tick Union Own Incoming Reverse And Face On Four Perpnn Y-Probes

> **Key terms used in this doc** are indexed A-Z at `docs/KEY_TERMINOLOGY.md`;
> each row points to the canonical source-of-truth doc.

**Date:** 2026-08-15
**Type:** bounded_theorem
**Scope:** reverse and face from same-tick ∪ own incoming lock on the four
perpnn y-probes in `B_3(0)`, no global T. Let `t(q)` be the formation tick of
probe `q`. Let `L(q)` be `q`'s own unique incoming lock; seeds use seed
letters. If several earliest incoming steps exist, `L(q)` is `UNDEFINED`.
At that tick, `S^+(q)` is the set of locks of six-neighbors of `q` that
formed at tick `<= t(q)` and are not `q`, union `{L(q)}` when `L(q)` is
defined. Reverse holds if and only if some lock in `S^+(A)` is the vector
opposite of some lock in `S^+(B)`. Face holds if and only if some lock in
`S^+(C)` is the vector opposite of some lock in `S^+(D)`. Empty `S^+` on
either side of a comparison is `UNDEFINED`; nonempty with no opposite pair
fails. Occupancy n is not used. Occupancy `n` is not used. This is not named-sign lettering. This is
not a unique lock-vector leftover and not a sum leftover. `A=(0,1,0)` is
not the 1-seed; origin is. Reverse HOLD uses L(A): no. Reverse fails.
This is not leftover of same-tick-inclusive existential opposite that excludes
`q`: those sets omit `L(A)` and `L(D)`. This is not leftover of
strictly-earlier own-lock-in: that letter uses tick `< t(q)` union own lock.
On these four probes there is no same-tick six-neighbor, so the four `S^+`
sets coincide with that leftover; the letter here is still same-tick-inclusive.
This is not leftover of later-tick union own: that leftover waits for a
global later T and reports reverse hold and face hold. This is not leftover
of opposite-lock same-tick union own: that display holds reverse when A is a seed.
A is not the 1-seed. This is not leftover of the unique own-incoming
lock-vector letters on these y-probes: that readout reports reverse
`UNDEFINED` and face `UNDEFINED` at mixed `B` and mixed `C`. Uniqueness of
incoming locks is not required. Uniqueness of the lock set is not required.
Displayed, not adopted. This note does not write existential opposite into
Admissibility and does not attach a formation member from already-recorded
six-neighbor locks.
**Audit-status authority:** independent audit lane only. This note authors no
audit verdict and predicts none.
**Primary runner:**
[`scripts/perpnn_yprobe_sametick_union_own_existential_opposite_reverse_face_2026_08_15.py`](../scripts/perpnn_yprobe_sametick_union_own_existential_opposite_reverse_face_2026_08_15.py)

Framework input:

- [`MINIMAL_AXIOMS_2026-06-29.md`](MINIMAL_AXIOMS_2026-06-29.md) supplies
  cubic-lattice sites `Z^3` with nearest-neighbor adjacency, the one-site
  algebra `M_2(C)`, and the Record sentences that records form and that a
  present record locks exactly one admissible local possibility.

Everything after that quoted input is a finite displayed process on `B_3(0)`
and the four named y-probes. Incoming lock letters are unit nearest-neighbor
steps. Reverse and face are scored on existence of an opposite pair in the
same-tick-inclusive six-neighbor lock sets union the probe's own incoming
lock when defined. Named signs `{+,−}` are a coarser readout and are not
used. A singleton unique lock-vector letter is a different readout and is
not used. A `Z^3` sum of those locks is a different readout and is not used.

## Machine status and trace

```yaml
actual_current_surface_status: bounded-support
target_claim_type: bounded_theorem
claim_type_reason: "Exact report of S^+ as same-tick-inclusive six-neighbor locks union L(q) when defined, on the four perpnn y-probes at each probe's own t, no global T, with reverse fail and face fail from existential opposite; reverse HOLD does not use L(A); uniqueness of incoming locks is not claimed and the bits are not adopted."
trace_class: frontier_discovery
target_claim_id: perpnn_yprobe_sametick_union_own_existential_opposite_reverse_face
target_blocker_text: "display reverse and face from same-tick ∪ own incoming lock on the four perpnn y-probes, or UNDEFINED"
source_of_blocker_text: handoff
reachability_to_target: advances
artifact_role: theorem
next_trace_action: "Keep reverse and face displayed; do not write existential opposite into Admissibility, do not reduce to named sign, do not require a singleton lock vector, do not sum the lock set, do not use occupancy n, do not identify the sets with same-tick leftover that excludes q, do not identify the letter with strictly-earlier own-lock-in leftover, do not identify the sets with later-tick union own leftover, and do not identify the bits with opposite-lock same-tick union own leftover."
conditional_surface_status: "exact on B_3(0) for existential opposite of same-tick-inclusive six-neighbor locks union own incoming lock on the four perpnn y-probes, no global T; displayed, not adopted"
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
same-tick-inclusive union sets are scored:

```text
A = (0,1,0),  B = (1,1,1),  C = (0,2,0),  D = (1,1,0).
```

These are the same y-probes as the nnseed y-probe display. They are not the
x-probes `A=(1,0,0)`, `B=(1,1,1)`, `C=(2,0,0)`, `D=(1,1,0)`. `A` is not a
seed.

Lock alphabet of the displayed process: `{±e_i}` with `i` in `{1,2,3}`.

Seed: the origin is recorded at tick `0` with lock letter `+e_1`. This is
the perpnn 1-seed. It is not the two-site opposite-lock seed
`{0,(0,1,0)}` with `+e_1/−e_1`, not the perp two-site seed `+e_1/+e_2`, and
not the three-site seed `{0,(0,1,0),(1,0,0)}`.

From a recorded site `p` with lock `L_in(p)=±e_i`, a six-neighbor step
`s in NN` to `q=p+s` is allowed if and only if `s` is perpendicular to
`e_i`, that is

```text
s · e_i = 0.
```

If `q` lies in `B_3(0)`, is still unformed, and the step is allowed, then `q`
forms next and locks the incoming step `s`. If several allowed parents reach
`q` at the same earliest formation, each such incoming step is kept as a
possible lock. Uniqueness is not required. A later parent does not re-form
`q`.

## Named existential opposite from same-tick ∪ own incoming lock

Let `t(q)` be the formation tick of y-probe `q` when that tick is defined in
`B_3(0)`. Let `L(q)` be `q`'s own unique incoming lock in `{±e_i}`. Seeds
use seed letters. If several earliest incoming steps exist, `L(q)` is
`UNDEFINED`. At the own formation tick of each probe `q`, let `S^+(q)` be
the set of locks of six-neighbors of `q` that formed at tick `<= t(q)`
(same-tick-inclusive) and are not `q`, union `{L(q)}` when `L(q)` is defined.
Same-tick partners are kept when they are neighbors. The probe itself is
excluded from the neighbor set and re-enters only through `{L(q)}` when
that letter is defined. This display does not wait for a global later T.
This display does not use occupancy `n`. Duplicate locks collapse in the
set. The construction does not require `S^+(q)` to be a singleton. It does
not sum `S^+(q)`. It is not a unique lock-vector leftover and not a sum
leftover. It is not leftover of same-tick-inclusive existential opposite
that excludes `q`. It is not leftover of strictly-earlier own-lock-in. It
is not leftover of later-tick union own. It is not leftover of unique
own-incoming lock-vector letters on these y-probes. It is not leftover of
opposite-lock same-tick union own.

Identifying a named sign of those locks with reverse or face is refused:
named-sign lettering lost the axis. Reverse and face are scored on existence
of a pair of lock vectors that add to zero. They are not scored on `{+,−}`
names and are not an occupancy-kernel inner product.

Reverse and face (displayed):

```text
reverse  <=>  some a in S^+(A) and some b in S^+(B) with a+b=(0,0,0)
face     <=>  some c in S^+(C) and some d in S^+(D) with c+d=(0,0,0)
```

If `S^+(A)` or `S^+(B)` is empty, reverse is `UNDEFINED`. Else reverse fails
if no such pair exists. If `S^+(C)` or `S^+(D)` is empty, face is
`UNDEFINED`. Else face fails if no such pair exists. The report is one of
`hold`, `fail`, or `UNDEFINED`.

Admissibility is not edited. Existential opposite is not written into
Admissibility.

## Theorem 1 — formation ticks, own incoming locks, and S^+ at each y-probe

Direct enumeration of the displayed perpnn 1-seed process on `B_3(0)` forms
all four y-probes. The formation ticks are `t(A)=1`, `t(B)=3`, `t(C)=4`,
`t(D)=2`. `A` is not a seed. The 1-seed is the origin at tick `0` with lock
`+e_1`. Those ticks locate the same-tick-inclusive six-neighbor set. They are
not occupancy kernels and are not a global later T.

Own incoming locks and same-tick-inclusive union sets at each probe's own
formation tick are:

```text
A: incoming +e_2; +e_1 at (0, 0, 0);
   t(A)=1;  L(A) = +e_2;  S^+(A) = {+e_1, +e_2}
B: incoming +e_1, +e_2, +e_3; +e_3 at (0, 1, 1), +e_2 at (0, 1, 1),
   +e_1 at (1, 0, 1), +e_1 at (1, 1, 0);
   t(B)=3;  L(B) = UNDEFINED;  S^+(B) = {+e_1, +e_2, +e_3}
C: incoming +e_1, −e_1, +e_3, −e_3; +e_2 at (1, 2, 0), +e_2 at (-1, 2, 0),
   +e_2 at (0, 1, 0), +e_2 at (0, 2, 1), +e_2 at (0, 2, -1);
   t(C)=4;  L(C) = UNDEFINED;  S^+(C) = {+e_2}
D: incoming +e_1; +e_2 at (0, 1, 0);
   t(D)=2;  L(D) = +e_1;  S^+(D) = {+e_1, +e_2}
```

`A` forms at tick 1 from the origin by the perpendicular step `+e_2`. Its
same-tick-inclusive neighbor is the seed origin locking `+e_1`. There is no
same-tick six-neighbor of `A`. `L(A)` is the unique incoming lock `+e_2`, so
`S^+(A)={+e_1, +e_2}`. `B`'s already-recorded neighbors mix `+e_3` and `+e_2`
at `(0,1,1)` with `+e_1` at `(1,0,1)` and at `D`. Mixed remains a set. There
is no same-tick six-neighbor of `B`. `L(B)` is `UNDEFINED` from three
earliest incoming steps, so `S^+(B)` is that neighbor set `{+e_1, +e_2, +e_3}`.
`C`'s already-recorded neighbors are five copies of `+e_2`. There is no
same-tick six-neighbor of `C`. `L(C)` is `UNDEFINED` from four earliest
incoming steps, so `S^+(C)={+e_2}`. `D`'s already-recorded neighbor is `A`
locking `+e_2`, and `L(D)=+e_1`, so `S^+(D)={+e_1, +e_2}`. There is no
same-tick six-neighbor of `D`.

Incoming locks exist and need not be unique (`B` has three earliest incoming
steps `+e_1`, `+e_2`, and `+e_3`; `C` has four). That non-uniqueness leaves
`L(B)` and `L(C)` `UNDEFINED` and does not empty `S^+(B)` or `S^+(C)`.
Uniqueness is not required.

Reverse HOLD uses L(A): no. Reverse HOLD uses `L(A)`: no. `L(A)=+e_2` is a
member of `S^+(A)`, but `S^+(B)` contains no `−e_2`. Dropping `L(A)` leaves
`{+e_1}` at `A`, which also finds no opposite in `S^+(B)`. Reverse fails
with or without `L(A)`. Own lock does not recover reverse on this 1-seed
process. Same-tick partners do not recover reverse: there is no same-tick
six-neighbor at `A` or at `B`.

The unique own-incoming letters on these same y-probes are `+e_2`,
`UNDEFINED`, `UNDEFINED`, `+e_1`. Those are different objects: `S^+(A)` is
not `{+e_2}`, and `S^+(D)` is not `{+e_1}`. Same-tick-inclusive leftover that
excludes `q` reports `S(A)={+e_1}`, not `{+e_1, +e_2}`, and `S(D)={+e_2}`,
not `{+e_1, +e_2}`. Strictly-earlier own-lock-in reports the same four `S^+`
sets on these probes because there is no same-tick six-neighbor; that leftover
uses tick `< t(q)`. Later-tick union own on these same y-probes reports
`{+e_1, −e_1, +e_2, +e_3, −e_3}` at `A` after waiting for a global later T.

## Theorem 2 — reverse hold / fail / UNDEFINED

Reverse holds if and only if there exist `a` in `S^+(A)` and `b` in
`S^+(B)` with `a+b=(0,0,0)`. Both sets are nonempty: `S^+(A)={+e_1, +e_2}`
and `S^+(B)={+e_1, +e_2, +e_3}`. No pair sums to the origin. Reverse fails.

Reverse: fail

This is not `hold` and not `UNDEFINED`. Reverse HOLD uses `L(A)`: no.
This is not leftover of later-tick union own on these y-probes: that leftover
reports reverse hold from `−e_1` at a later neighbor of `A`. This is not
leftover of opposite-lock same-tick union own: that leftover holds reverse
when `A` is a seed with letter `−e_1`. Unique lock-vector lettering of the
same union sets would report reverse `UNDEFINED` because `A` and `B` mix. A
sum leftover of the same lists would replace `S^+(A)` by `(1,1,0)` and
`S^+(B)` by `(1,1,1)`, which are not lock letters. Unique own-incoming
letters on these y-probes report reverse `UNDEFINED` because `L(B)` is
`UNDEFINED`. Reverse fails.

## Theorem 3 — face hold / fail / UNDEFINED

Face holds if and only if there exist `c` in `S^+(C)` and `d` in `S^+(D)`
with `c+d=(0,0,0)`. Both sets are nonempty: `S^+(C)={+e_2}` and
`S^+(D)={+e_1, +e_2}`. No pair sums to the origin. Face fails.

Face: fail

Displayed, not adopted. The bits are not written into Admissibility.

This is not `hold` and not `UNDEFINED`. Unique own-incoming letters on these
same y-probes assign `L(C)=UNDEFINED` from four earliest incoming steps and
report face `UNDEFINED`. Unique lock-vector lettering of the union sets
would report face `UNDEFINED` because `D` mixes. A sum leftover would
replace `S^+(C)` by `+e_2` and `S^+(D)` by `(1,1,0)` and would also fail
face, but those sums are a different object. Named-sign lettering lost the
axis: every lock in the four union sets is a positive letter, so `{+,−}`
cannot tell `+e_1` from `+e_2`. Later-tick union own on these y-probes
reports face hold from `−e_2` at a later neighbor of `D`. Face fails here
because this display does not wait for that later neighbor.

## What this note does not claim

- It does not select a unique incoming lock.
- It does not reduce lock vectors to named signs `{+,−}`.
- It does not require the same-tick-inclusive union set to be a singleton.
- It does not sum the same-tick-inclusive union set.
- It does not use occupancy `n`.
- It does not score reverse or face as an occupancy-kernel inner product.
- It does not attach a formation member from already-recorded six-neighbor
  locks.
- It does not census a sixteen-combination free lettering independent of
  lock vectors.
- It does not reprint unique own-incoming lock-vector letters on these
  y-probes.
- It does not reprint same-tick-inclusive existential opposite that excludes
  `q`.
- It does not reprint strictly-earlier own-lock-in.
- It does not reprint later-tick union own.
- It does not wait for a global later T.
- It does not reprint opposite-lock same-tick union own leftover.
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
perpnn 1-seed process, the same-tick-inclusive union sets, and the
existential-opposite reverse/face predicates are displayed theorem-domain
data.

## Exact target and obligation graph

| Obligation | Status |
|---|---|
| current Lattice / Admissibility / Record premises | quoted; no edit |
| perp-step incoming-lock process on `B_3(0)` | displayed; perpnn 1-seed origin lock `+e_1` |
| ticks `t(A)`, `t(B)`, `t(C)`, `t(D)` | Theorem 1; `1`, `3`, `4`, `2` |
| own incoming locks `L(A)`, `L(B)`, `L(C)`, `L(D)` | Theorem 1; `+e_2`, `UNDEFINED`, `UNDEFINED`, `+e_1` |
| lock sets `S^+(A)`, `S^+(B)`, `S^+(C)`, `S^+(D)` | Theorem 1; `{+e_1, +e_2}`, `{+e_1, +e_2, +e_3}`, `{+e_2}`, `{+e_1, +e_2}` |
| reverse HOLD uses `L(A)` | Theorem 1; no |
| reverse and face | Theorems 2–3; `fail` / `fail` |
| unique incoming lock | not required |
| occupancy `n` as the letter | not used |
| named-sign `{+,−}` letter | not used; lost the axis |
| singleton unique lock-vector letter | not used; mixed remains a set |
| `Z^3` sum of the lock set | not used; no aggregation |
| occupancy-kernel inner product | not used |
| formation member from already-recorded six-neighbor locks | not attached |
| leftover of unique own-incoming letters on these y-probes | not this display |
| leftover of same-tick-inclusive existential opposite that excludes `q` | not this display |
| leftover of strictly-earlier own-lock-in | not this display |
| leftover of later-tick union own | not this display |
| leftover of opposite-lock same-tick union own | not this display |
| existential opposite as Admissibility content | not adopted |
| formation site / probability / rate | open |
| physical Record readout of the bits | open |

## Promotion value gate (V1–V5)

| # | Answer |
|---|---|
| V1 | It answers the first-display question: same-tick ∪ own incoming lock on the four perpnn y-probes, no global T, reverse/face or `UNDEFINED`. |
| V2 | Current main has no landed same-tick-inclusive union-own-lock existential-opposite reverse/face report on these four perpnn y-probes. |
| V3 | Same-tick-inclusive union sets and the `fail`/`fail` reports are independently finite and exact. |
| V4 | The theorem is more than a restatement of Record because it reads same-tick-inclusive six-neighbor lock vectors union `L(q)` when defined and scores existence of an opposite pair. |
| V5 | It is not an adopted content rule: the bits remain displayed. |

## No-go discipline gate

The negative content is narrow: the display does not write those bits into
Admissibility, does not reduce them to named signs, does not require a
singleton lock vector, does not sum the lock set, does not reprint unique
own-incoming letters, does not reprint same-tick leftover that excludes
`q`, does not reprint strictly-earlier own-lock-in, does not reprint
later-tick union own, does not reprint opposite-lock same-tick union own,
and does not use occupancy `n`. No global impossibility is claimed.

### N1 — materially distinct routes

| Route | Attack | Result |
|---|---|---|
| unique lock-vector lettering of the same union sets | require a singleton `{v}` subset `{±e_i}` | refused; leftover; reverse would be `UNDEFINED` while the mixed union sets are nonempty and reverse fails |
| sum of the same union sets | replace `S^+` by the `Z^3` sum | refused; leftover; sums `(1,1,0)` and `(1,1,1)` are not lock letters |
| named-sign lettering of the same union sets | map `±e_i` to `{+,−}` | refused; lost the axis; all four union sets are positive letters and cannot tell `+e_1` from `+e_2` |
| unique own-incoming lock-vector leftover on these y-probes | reuse `L(A)=+e_2`, `L(B)=UNDEFINED`, `L(C)=UNDEFINED`, `L(D)=+e_1` | refused; different object; that leftover reports reverse `UNDEFINED` and face `UNDEFINED` while same-tick union reverse fails and face fails |
| leftover of same-tick-inclusive existential opposite that excludes `q` | reuse `S(A)={+e_1}` and `S(D)={+e_2}` | refused; different set; `S^+(A)={+e_1, +e_2}` and `S^+(D)={+e_1, +e_2}` |
| leftover of strictly-earlier own-lock-in | reuse tick `< t(q)` union own lock | refused; different letter; this display is same-tick-inclusive. On these four probes there is no same-tick six-neighbor, so the four `S^+` sets coincide with that leftover, but the construction keeps same-tick partners when they exist |
| leftover of later-tick union own | reuse global later T and reverse hold | refused; different set; this display does not wait for a global later T; reverse fails here |
| leftover of opposite-lock same-tick union own | reuse seed `{0,(0,1,0)}` with reverse hold when `A` is a seed | refused; different process; `A` is not the 1-seed and reverse fails |
| leftover of perpnn later-tick existential opposite on x-probes | reuse reverse fail and face hold at a later common T | refused; different probes and different readout; face fails here |
| unique letter of occupancy `n` | assign one letter from occupancy `n` | different object; occupancy `n` is not used |
| occupancy-kernel inner product | score `n(A)·n(B)<0` and `n(C)·n(D)<0` | different object; not an occupancy-kernel inner product |
| reverse/face from formation-tick inequalities | score probes by formation order | different object; ticks locate `S^+` and are not the predicate |
| attach a formation member from already-recorded six-neighbor locks | form the probes by a neighbor-lock letter instead of perp-step | refused; not attached |
| adopt bits into Admissibility | rewrite the local rule by existential opposite | refused; displayed, not adopted |
| unique incoming lock required | demand one incoming step per probe | uniqueness is not required; all three earliest incoming steps at `B` and all four at `C` are kept and `L(B)`, `L(C)` are `UNDEFINED` |

### N2 — wall independence

Missing physical adoption, missing formation attachment from already-recorded
six-neighbor locks, and missing Record identification of existential opposite
are distinct open premises. This note claims no complete wall collection.

### N3 — hidden-condition scan

The host `B_3(0)`, 1-seed origin lock `+e_1`, perpendicular step rule,
incoming-step lock, same-tick-inclusive lock set of six-neighbors formed
at tick `<=` each probe's own `t` with the probe excluded, union with `L(q)`
when defined, existential opposite, four y-probes with non-seed `A`, and
reverse/face as existence of a pair that sums to zero are declared. No
uniqueness of incoming locks, no occupancy `n`, no named-sign reduction, no
singleton leftover, no sum leftover, no unique own-incoming leftover, no
same-tick exclude-`q` leftover, no strictly-earlier own-lock-in leftover, no
later-tick leftover, no opposite-lock same-tick union own leftover, no
global later T, no formation attachment from already-recorded six-neighbor
locks, and no Admissibility rewrite are silently assumed.

### N4 — source residual matching

The current axiom memo supplies cubic sites, `M_2(C)`,
content-conditional-on-formation, and unreadable absence. The residual that
formation site, probability, and rate remain unsupplied is unchanged. The
`fail`/`fail` reports do not close that residual.

### N5 — resolution and rhetoric audit

| Resolution | Executed | Not claimed |
|---|---|---|
| per element | each lock vector in a same-tick-inclusive union set | no continuum alphabet |
| per site | `A,B,C,D` y-probes on `B_3(0)` only | no other cubic sites |
| per mode | no mode calculation | no spectral exhaustion |
| per block | four lock sets and two reverse/face comparisons | no adopted content law |
| lattice wide | checked and not executed | no lattice-wide lettering rule |

### N6 — live partial-closure paths

Live routes include a later Record content map for reverse/face, a
formation-rate rule, and a physical selector among `{±e_i}`. None is taken
here.

### N7 — hostile steelman

**Steelman:** Same-tick partners or own lock should recover reverse on the
1-seed process because opposite-lock same-tick union own recovered reverse
when `A` is a seed, mixed neighbor locks should make reverse and face
`UNDEFINED`, the sets should be replaced by their sums, later-tick union own
already answered the exist-opposite question with reverse hold and face hold,
strictly-earlier own-lock-in already answered the union question because the
sets coincide, unique own-incoming letters already answered the own-lock
question, named signs should suffice because every lock here is positive, and
occupancy `n` should track that vector.

**Answer:** The named construction reports lock sets `{+e_1, +e_2}`,
`{+e_1, +e_2, +e_3}`, `{+e_2}`, `{+e_1, +e_2}` at `A,B,C,D` from
same-tick-inclusive six-neighbor locks union `{L(q)}` when defined. Mixed
remains a set. The construction does not sum. Occupancy `n` is not used.
Named signs lost the axis. `A` is not the 1-seed; origin is. Reverse HOLD
uses L(A): no. No pair from `S^+(A)` and `S^+(B)` is opposite, so reverse
fails. No pair from `S^+(C)` and `S^+(D)` is opposite, so face fails. There
is no same-tick six-neighbor at these four probes, so the four `S^+` sets
coincide with strictly-earlier own-lock-in; the letter is still
same-tick-inclusive. Later-tick leftover waits for a global later T and
holds reverse from `−e_1` at `A`. Opposite-lock same-tick union own leftover
holds reverse because that `A` is a seed. Unique own-incoming leftover
reports reverse `UNDEFINED`. The sets are not those leftovers. The bits
remain displayed. Incoming-lock uniqueness is not required.

### N8 — cross-cycle echo

A unique own-incoming lock-vector display on these same perpnn y-probes
assigns `L(A)=+e_2`, `L(B)=UNDEFINED`, `L(C)=UNDEFINED`, `L(D)=+e_1` and
reports reverse `UNDEFINED` with face `UNDEFINED`. A same-tick-inclusive
existential opposite display that excludes `q` assigns `{+e_1}` at `A` and
`{+e_2}` at `D`. Strictly-earlier own-lock-in on these y-probes reports
reverse fail and face fail on the same four `S^+` sets because there is no
same-tick six-neighbor. Later-tick union own on these y-probes reports
reverse hold and face hold on different later sets
`{+e_1, −e_1, +e_2, +e_3, −e_3}` and `{+e_1, +e_2, −e_2, +e_3, −e_3}` after
a global later T. Opposite-lock same-tick union own on these y-probes reports
reverse hold and face hold because that `A` is a seed. Unique lock-vector
lettering of the union sets would report reverse `UNDEFINED` because `A` and
`B` mix. A sum leftover of the same lists would replace the sets by
`(1,1,0)` and `(1,1,1)`. This note is not those displays: mixed remains a
set, the construction does not sum, `S^+(A)` includes both the origin lock
and `L(A)`, reverse fails, and face fails. This is a 1-seed same-tick ∪ own
display on the four y-probes, not leftover of later-tick union own.

**Gate disposition:** PASS for the same-tick-inclusive six-neighbor-lock union
own incoming existential-opposite reverse/face reports above. FAIL / DO NOT SHIP
for “the predicate equals the named sign,” “the predicate equals the unique
singleton lock vector,” “the predicate equals the sum of the lock set,”
“bits are Admissibility,” “the letter is occupancy `n`,” “the sets equal
unique own-incoming letters,” “the sets equal same-tick leftover that
excludes `q`,” “the letter equals strictly-earlier own-lock-in,” “the sets
equal later-tick union own,” “the bits equal opposite-lock same-tick union
own,” “reverse holds,” “face holds,” or “reverse HOLD uses `L(A)`.”

## Primary runner

The paired runner builds Euclidean `B_3(0)`, runs the perpnn 1-seed
perp-step incoming-lock process, reads each probe's own unique incoming lock
or `UNDEFINED`, collects six-neighbor locks formed at tick `<=` each probe's
own formation tick with the probe excluded, unions those locks with `{L(q)}`
when defined, reads the union sets at the four y-probes, reports whether
reverse HOLD uses L(A), and checks Theorems 1--3. It also checks that the
construction is not named-sign lettering, that mixed sets remain defined,
that the construction does not sum, that occupancy `n` is not used, that a
formation member from already-recorded six-neighbor locks is not attached,
that the sets are not leftover of unique own-incoming letters, that the sets
are not leftover of same-tick-inclusive existential opposite that excludes
`q`, that the letter is not leftover of strictly-earlier own-lock-in, that
the bits are not leftover of later-tick union own, and that the bits are
not leftover of opposite-lock same-tick union own. No runner cache is
written.
