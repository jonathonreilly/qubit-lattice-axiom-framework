---
claim_id: opposite_lock_yprobe_sametick_union_own_existential_opposite_reverse_face_bounded_theorem_note_2026-08-15
claim_type: bounded_theorem
claim_scope: "Reverse and face from same-tick-inclusive 6-NN locks union own incoming lock on the four nsopp y-probes, no global T, are reported. Displayed, not adopted."
upstream_dependencies:
  - minimal_axioms
runner: scripts/opposite_lock_yprobe_sametick_union_own_existential_opposite_reverse_face_2026_08_15.py
---

# Same-Tick-Inclusive Union Own Incoming Reverse And Face On Four Opposite-Lock Y-Probes

> **Key terms used in this doc** are indexed A-Z at `docs/KEY_TERMINOLOGY.md`;
> each row points to the canonical source-of-truth doc.

**Date:** 2026-08-15
**Type:** bounded_theorem
**Scope:** reverse and face from same-tick-inclusive six-neighbor locks union
the probe's own incoming lock on the four nsopp y-probes in `B_3(0)`, no
global T. Let `t(q)` be the formation tick of probe `q`. Let `L(q)` be `q`'s
own unique incoming lock; seeds use seed letters. If several earliest
incoming steps exist, `L(q)` is `UNDEFINED`. At that tick, `S^+(q)` is the
set of locks of six-neighbors of `q` that formed at tick `<= t(q)` and are
not `q`, union `{L(q)}` when `L(q)` is defined. Reverse holds if and only if
some lock in `S^+(A)` is the vector opposite of some lock in `S^+(B)`. Face
holds if and only if some lock in `S^+(C)` is the vector opposite of some
lock in `S^+(D)`. Empty `S^+` on either side of a comparison is `UNDEFINED`;
nonempty with no opposite pair fails. Occupancy `n` is not used. This is
not named-sign lettering. This is not a unique lock-vector leftover and not
a sum leftover. This is not leftover of same-tick-inclusive existential
opposite that excludes `q`: that display reports reverse fail because
`S(A)={+e_1}` has no opposite in `S(B)`. This is not leftover of
strictly-earlier own-lock-in: that display takes tick `< t(q)` union own
lock and reports `S^+(A)={−e_1}` without the same-tick origin partner. This
is not leftover of later-tick union own: that display waits for a global
later T equal to the max of the four formation ticks. This is not leftover
of the unique own-incoming lock-vector letters on these y-probes: that
readout requires a singleton incoming step and reports reverse hold with
face `UNDEFINED` at mixed `D`. Uniqueness of incoming locks is not required.
Uniqueness of the lock set is not required. Displayed, not adopted. This
note does not write existential opposite into Admissibility and does not
attach a formation member from already-recorded six-neighbor locks.
**Audit-status authority:** independent audit lane only. This note authors no
audit verdict and predicts none.
**Primary runner:**
[`scripts/opposite_lock_yprobe_sametick_union_own_existential_opposite_reverse_face_2026_08_15.py`](../scripts/opposite_lock_yprobe_sametick_union_own_existential_opposite_reverse_face_2026_08_15.py)

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
claim_type_reason: "Exact report of S^+ as same-tick-inclusive six-neighbor locks union L(q) when defined, on the four nsopp y-probes at each probe's own t, no global T, with reverse hold using L(A) and face hold from existential opposite; uniqueness of incoming locks is not claimed and the bits are not adopted."
trace_class: frontier_discovery
target_claim_id: opposite_lock_yprobe_sametick_union_own_existential_opposite_reverse_face
target_blocker_text: "display reverse and face from same-tick-inclusive 6-NN locks union own incoming lock on the four nsopp y-probes, no global T, or UNDEFINED"
source_of_blocker_text: handoff
reachability_to_target: advances
artifact_role: theorem
next_trace_action: "Keep reverse and face displayed; do not write existential opposite into Admissibility, do not reduce to named sign, do not require a singleton lock vector, do not sum the lock set, do not use occupancy n, do not identify the sets with same-tick leftover that excludes q, do not identify the sets with strictly-earlier own-lock-in leftover, and do not identify the sets with later-tick union own leftover."
conditional_surface_status: "exact on B_3(0) for existential opposite of same-tick-inclusive six-neighbor locks union own incoming lock on the four nsopp y-probes, no global T; displayed, not adopted"
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

These are not the x-probes `A=(1,0,0)`, `B=(1,1,1)`, `C=(2,0,0)`,
`D=(1,1,0)`. `A` is a seed.

Lock alphabet of the displayed process: `{±e_i}` with `i` in `{1,2,3}`.

Seed: the two-record set `{0, (0,1,0)}` is recorded at formation tick 0 with
opposite locks `L(0)=+e_1` and `L(0,1,0)=−e_1`. This seed is not the perp
two-site seed `+e_1/+e_2`.

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

## Named existential opposite from same-tick-inclusive six-neighbor locks union own incoming lock

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
own-incoming lock-vector letters on these y-probes.

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

Direct enumeration of the displayed opposite-lock process on `B_3(0)` forms
all four y-probes. The formation ticks are `t(A)=0`, `t(B)=2`, `t(C)=1`,
`t(D)=3`. `A` is a seed. Those ticks locate the same-tick-inclusive
six-neighbor set. They are not occupancy kernels and are not a global later
T.

Own incoming locks and same-tick-inclusive union sets at each probe's own
formation tick are:

```text
A: +e_1 at (0, 0, 0); seed letter −e_1;
   t(A)=0;  L(A) = −e_1;  S^+(A) = {+e_1, −e_1}
B: +e_3 at (0, 1, 1), +e_1 at (1, 0, 1); incoming +e_1;
   t(B)=2;  L(B) = +e_1;  S^+(B) = {+e_1, +e_3}
C: −e_1 at (0, 1, 0); incoming +e_2;
   t(C)=1;  L(C) = +e_2;  S^+(C) = {−e_1, +e_2}
D: −e_1 at (0, 1, 0), +e_1 at (1, 2, 0), −e_3 at (1, 0, 0),
   +e_3 at (1, 0, 0), +e_2 at (1, 0, 0), +e_1 at (1, 1, 1),
   +e_1 at (1, 1, -1);
   t(D)=3;  L(D) = UNDEFINED;  S^+(D) = {+e_1, −e_1, +e_2, +e_3, −e_3}
```

`A` is a seed at tick 0. Its same-tick partner at the origin is a
six-neighbor locking `+e_1`. Same-tick-inclusive leftover that excludes `q`
reports `{+e_1}` at `A`. `L(A)` is the seed letter `−e_1`, so
`S^+(A)={+e_1, −e_1}`. Reverse HOLD uses L(A): the only opposite pair with
`S^+(B)` is `−e_1+(+e_1)=(0,0,0)`, and `−e_1` is not a same-tick neighbor
lock of `A`. `C`'s already-recorded neighbor is the seed partner `(0,1,0)`
locking `−e_1`, and `L(C)=+e_2`, so `S^+(C)={−e_1, +e_2}`. `D` forms at
tick 3 with mixed same-tick-inclusive neighbors; `L(D)` is `UNDEFINED` from
three earliest incoming steps, so `S^+(D)` is that neighbor set. Mixed
remains a set. `B` keeps the earlier neighbor `(0,1,1)` locking `+e_3` and
the same-tick neighbor `(1,0,1)` locking `+e_1`; `L(B)=+e_1` is already in
that neighbor set.

Incoming locks exist and need not be unique (`D` has three earliest incoming
steps `−e_2`, `−e_3`, and `+e_3`). That non-uniqueness leaves `L(D)`
`UNDEFINED` and does not empty `S^+(D)`. Uniqueness is not required.

The unique own-incoming letters on these same y-probes are `−e_1`, `+e_1`,
`+e_2`, `UNDEFINED`. Those are different objects: `S^+(A)` is not `{−e_1}`,
and `S^+(D)` is nonempty. Same-tick-inclusive leftover that excludes `q`
reports `{+e_1}` at `A` and reverse fail. Strictly-earlier own-lock-in
reports `{−e_1}` at `A` without the same-tick origin partner. Later-tick
union own reports a six-lock set at `A` after waiting for a global later T.

## Theorem 2 — reverse hold / fail / UNDEFINED

Reverse holds if and only if there exist `a` in `S^+(A)` and `b` in
`S^+(B)` with `a+b=(0,0,0)`. Both sets are nonempty: `S^+(A)={+e_1, −e_1}`
and `S^+(B)={+e_1, +e_3}`, so `−e_1+(+e_1)=(0,0,0)`. Reverse holds.

Reverse: hold

Reverse HOLD uses L(A). Same-tick-inclusive leftover that excludes `q`
leaves `S(A)={+e_1}` and reports reverse fail. The only opposite pair here
is the seed letter `L(A)=−e_1` with `+e_1` in `S^+(B)`. Holding reverse
does not need a global later T once the own lock is included.

This is not `fail` and not `UNDEFINED`. This is not leftover of
same-tick-inclusive existential opposite that excludes `q`. Unique
lock-vector lettering of the same union sets would report reverse
`UNDEFINED` because both sides mix. A sum leftover of the same lists would
replace `S^+(A)` by the origin and `S^+(B)` by `(1,0,1)` and would fail
reverse, while existential opposite holds. Unique own-incoming letters on
these y-probes also report reverse hold from `L(A)=−e_1` and `L(B)=+e_1`;
that leftover is a different object because its face report at mixed `D` is
`UNDEFINED`. Strictly-earlier own-lock-in also reports reverse hold, but
from `{−e_1}` at `A` without the same-tick origin partner. Later-tick union
own reports reverse hold on a later six-lock set at `A`. Reverse holds
because `L(A)` enters `S^+(A)`.

## Theorem 3 — face hold / fail / UNDEFINED

Face holds if and only if there exist `c` in `S^+(C)` and `d` in `S^+(D)`
with `c+d=(0,0,0)`. Both sets are nonempty: `S^+(C)={−e_1, +e_2}` and
`S^+(D)={+e_1, −e_1, +e_2, +e_3, −e_3}`, so `−e_1+(+e_1)=(0,0,0)`. Face holds.

Face: hold

Displayed, not adopted. The bits are not written into Admissibility.

This is not `fail` and not `UNDEFINED`. Unique own-incoming letters on these
same y-probes assign `L(D)=UNDEFINED` from three earliest incoming steps and
report face `UNDEFINED`. Unique lock-vector lettering of the union sets
would also report face `UNDEFINED` because `C` and `D` mix. A sum leftover
would replace `S^+(C)` by `(-1,1,0)` and `S^+(D)` by `+e_2` and would fail
face, while existential opposite holds. Named-sign lettering lost the axis
in mixed `{+,−}` at `C` and `D`. Face already holds at each probe's own
formation tick with same-tick partners included and own lock unioned; holding
face does not need a global later T.

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
- It does not reprint formation-time already-recorded lock sets on nnseed
  x-probes.
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
opposite-lock process, the same-tick-inclusive union sets, and the
existential-opposite reverse/face predicates are displayed theorem-domain
data.

## Exact target and obligation graph

| Obligation | Status |
|---|---|
| current Lattice / Admissibility / Record premises | quoted; no edit |
| perp-step incoming-lock process on `B_3(0)` | displayed; opposite-lock two-site seed `+e_1/−e_1` |
| ticks `t(A)`, `t(B)`, `t(C)`, `t(D)` | Theorem 1; `0`, `2`, `1`, `3` |
| own incoming locks `L(A)`, `L(B)`, `L(C)`, `L(D)` | Theorem 1; `−e_1`, `+e_1`, `+e_2`, `UNDEFINED` |
| lock sets `S^+(A)`, `S^+(B)`, `S^+(C)`, `S^+(D)` | Theorem 1; `{+e_1, −e_1}`, `{+e_1, +e_3}`, `{−e_1, +e_2}`, `{+e_1, −e_1, +e_2, +e_3, −e_3}` |
| reverse HOLD uses L(A) | Theorem 1; yes |
| reverse and face | Theorems 2–3; `hold` / `hold` |
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
| leftover of nnseed x-probe formation-time existential opposite | not this display |
| existential opposite as Admissibility content | not adopted |
| formation site / probability / rate | open |
| physical Record readout of the bits | open |

## Promotion value gate (V1–V5)

| # | Answer |
|---|---|
| V1 | It answers the first-display question: same-tick-inclusive 6-NN locks union own incoming lock on the four nsopp y-probes, no global T, reverse/face or `UNDEFINED`. |
| V2 | Current main has no landed same-tick-inclusive union-own-lock existential-opposite reverse/face report on these four nsopp y-probes. |
| V3 | Same-tick-inclusive union sets and the `hold`/`hold` reports are independently finite and exact. |
| V4 | The theorem is more than a restatement of Record because it reads same-tick-inclusive six-neighbor lock vectors union `L(q)` when defined and scores existence of an opposite pair. |
| V5 | It is not an adopted content rule: the bits remain displayed. |

## No-go discipline gate

The negative content is narrow: the display does not write those bits into
Admissibility, does not reduce them to named signs, does not require a
singleton lock vector, does not sum the lock set, does not reprint unique
own-incoming letters, does not reprint same-tick leftover that excludes
`q`, does not reprint strictly-earlier own-lock-in, does not reprint
later-tick union own, and does not use occupancy `n`. No global
impossibility is claimed.

### N1 — materially distinct routes

| Route | Attack | Result |
|---|---|---|
| unique lock-vector lettering of the same union sets | require a singleton `{v}` subset `{±e_i}` | refused; leftover; reverse and face would be `UNDEFINED` while the mixed union sets are nonempty and both bits hold |
| sum of the same union sets | replace `S^+` by the `Z^3` sum | refused; leftover; sum of `S^+(A)` is the origin and sum of `S^+(B)` is `(1,0,1)`, which would fail reverse while `−e_1+(+e_1)=0`; sum of `S^+(C)` is `(-1,1,0)` and sum of `S^+(D)` is `+e_2` and would fail face |
| named-sign lettering of the same union sets | map `±e_i` to `{+,−}` | refused; lost the axis; mixed `{+,−}` at `A`, `B`, `C`, and `D` would hide `−e_1+(+e_1)=0` |
| unique own-incoming lock-vector leftover on these y-probes | reuse `L(A)=−e_1`, `L(B)=+e_1`, `L(C)=+e_2`, `L(D)=UNDEFINED` | refused; different object; that leftover reports reverse hold and face `UNDEFINED` while same-tick union reverse holds and face holds |
| leftover of same-tick-inclusive existential opposite that excludes `q` | reuse `S(A)={+e_1}` with reverse fail | refused; different set; `S^+(A)={+e_1, −e_1}` and reverse holds because reverse HOLD uses L(A) |
| leftover of strictly-earlier own-lock-in | reuse tick `< t(q)` union own lock with `S^+(A)={−e_1}` | refused; different set; this display keeps same-tick partners |
| leftover of later-tick union own | reuse global later T and a six-lock set at `A` | refused; different set; this display does not wait for a global later T |
| leftover of nnseed x-probe formation-time existential opposite | reuse seed `+e_1/+e_2` and x-probes | refused; different process and different frame |
| unique letter of occupancy `n` | assign one letter from occupancy `n` | different object; occupancy `n` is not used |
| occupancy-kernel inner product | score `n(A)·n(B)<0` and `n(C)·n(D)<0` | different object; not an occupancy-kernel inner product |
| reverse/face from formation-tick inequalities | score probes by formation order | different object; ticks locate `S^+` and are not the predicate |
| attach a formation member from already-recorded six-neighbor locks | form the probes by a neighbor-lock letter instead of perp-step | refused; not attached |
| adopt bits into Admissibility | rewrite the local rule by existential opposite | refused; displayed, not adopted |
| unique incoming lock required | demand one incoming step per probe | uniqueness is not required; all three earliest incoming steps at `D` are kept and `L(D)` is `UNDEFINED` |

### N2 — wall independence

Missing physical adoption, missing formation attachment from already-recorded
six-neighbor locks, and missing Record identification of existential opposite
are distinct open premises. This note claims no complete wall collection.

### N3 — hidden-condition scan

The host `B_3(0)`, two-site seed locks `+e_1` and `−e_1`, perpendicular step
rule, incoming-step lock, same-tick-inclusive lock set of six-neighbors formed
at tick `<=` each probe's own `t` with the probe excluded, union with `L(q)`
when defined, existential opposite, four y-probes with seed `A`, and
reverse/face as existence of a pair that sums to zero are declared. No
uniqueness of incoming locks, no occupancy `n`, no named-sign reduction, no
singleton leftover, no sum leftover, no unique own-incoming leftover, no
same-tick exclude-`q` leftover, no strictly-earlier own-lock-in leftover, no
later-tick leftover, no global later T, no formation attachment from
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

**Steelman:** The union is leftover of unique own-incoming letters plus
same-tick neighbor locks, mixed neighbor locks should make reverse and
face `UNDEFINED`, the sets should be replaced by their sums, unique
own-incoming letters already answered reverse hold with face `UNDEFINED`,
same-tick-inclusive existential opposite already answered the exist-opposite
question with reverse fail, strictly-earlier own-lock-in already answered the
union question without same-tick partners, later-tick union own already
answered the union question after a global T, named signs should suffice
because they keep orientation, and occupancy `n` should track that vector.

**Answer:** The named construction reports lock sets `{+e_1, −e_1}`,
`{+e_1, +e_3}`, `{−e_1, +e_2}`, `{+e_1, −e_1, +e_2, +e_3, −e_3}` at
`A,B,C,D` from same-tick-inclusive six-neighbor locks union `{L(q)}` when
defined. Mixed remains a set. The construction does not sum. Occupancy `n`
is not used. Named signs lost the axis. Some pair from `S^+(A)` and
`S^+(B)` is opposite, so reverse holds. Reverse HOLD uses L(A). Some pair
from `S^+(C)` and `S^+(D)` is opposite, so face holds. Same-tick leftover
that excludes `q` leaves `S(A)={+e_1}` and reverse fail. Strictly-earlier
own-lock-in reports `{−e_1}` at `A`. Later-tick union own waits for a
global later T. Unique own-incoming leftover reports face `UNDEFINED` at
mixed `D`. The sets are not those leftovers. Holding reverse does not need
a global later T once the own lock is included. The bits remain displayed.
Incoming-lock uniqueness is not required.

### N8 — cross-cycle echo

A unique own-incoming lock-vector display on these same opposite-lock
y-probes assigned `L(A)=−e_1`, `L(B)=+e_1`, `L(C)=+e_2`, `L(D)=UNDEFINED` and
reported reverse hold with face `UNDEFINED`. A same-tick-inclusive
existential opposite display that excludes `q` assigned `{+e_1}` at `A` and
reported reverse fail with face hold. Strictly-earlier own-lock-in assigned
`{−e_1}`, `{+e_1, +e_3}`, `{−e_1, +e_2}`, `{+e_1, −e_1}` and reported reverse
hold with face hold. Later-tick union own reported reverse hold and face hold
on a six-lock set at `A` after a global later T. Unique lock-vector lettering
of the union sets would report reverse `UNDEFINED` and face `UNDEFINED`
because every union set mixes. A sum leftover of the same lists would report
reverse fail and face fail because the sums are the origin with `(1,0,1)` and
`(-1,1,0)` with `+e_2`. This note is not those displays: mixed remains a set,
the construction does not sum, `S^+(A)` includes the seed letter and the
same-tick origin partner, reverse HOLD uses L(A), reverse holds, and
`−e_1+(+e_1)=(0,0,0)` so face holds.

**Gate disposition:** PASS for the same-tick-inclusive six-neighbor-lock union
own incoming existential-opposite reverse/face reports above. FAIL / DO NOT SHIP
for “the predicate equals the named sign,” “the predicate equals the unique
singleton lock vector,” “the predicate equals the sum of the lock set,”
“bits are Admissibility,” “the letter is occupancy `n`,” “the sets equal
unique own-incoming letters,” “the sets equal same-tick leftover that
excludes `q`,” “the sets equal strictly-earlier own-lock-in,” “the sets
equal later-tick union own,” “reverse fails,” or “face is `UNDEFINED`.”

## Primary runner

The paired runner builds Euclidean `B_3(0)`, runs the opposite-lock two-site
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
`q`, that the sets are not leftover of strictly-earlier own-lock-in, and that
the sets are not leftover of later-tick union own. No runner cache is
written.
