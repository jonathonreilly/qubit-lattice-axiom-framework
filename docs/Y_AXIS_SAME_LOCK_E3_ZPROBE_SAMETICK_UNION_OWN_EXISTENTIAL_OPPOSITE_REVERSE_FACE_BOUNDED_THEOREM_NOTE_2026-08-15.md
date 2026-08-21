---
claim_id: y_axis_same_lock_e3_zprobe_sametick_union_own_existential_opposite_reverse_face_bounded_theorem_note_2026-08-15
claim_type: bounded_theorem
claim_scope: "Reverse and face from same-tick ∪ own incoming lock on the four y-axis same-lock +e_3 z-probes are reported. Displayed, not adopted."
upstream_dependencies:
  - minimal_axioms
runner: scripts/y_axis_same_lock_e3_zprobe_sametick_union_own_existential_opposite_reverse_face_2026_08_15.py
---

# Same-Tick-Inclusive Union Own Incoming Reverse And Face On Four Y-Axis Same-Lock +e_3 Z-Probes

> **Key terms used in this doc** are indexed A-Z at `docs/KEY_TERMINOLOGY.md`;
> each row points to the canonical source-of-truth doc.

**Date:** 2026-08-15
**Type:** bounded_theorem
**Scope:** reverse and face from same-tick-inclusive six-neighbor locks union
the probe's own incoming lock on the four y-axis same-lock `+e_3` z-probes in
`B_3(0)`, no global T. Let `t(q)` be the formation tick of probe `q`. Let
`L(q)` be `q`'s own unique incoming lock; seeds use seed letters. If several
earliest incoming steps exist, `L(q)` is `UNDEFINED`. At that tick, `S^+(q)`
is the set of locks of six-neighbors of `q` that formed at tick `<= t(q)` and
are not `q`, union `{L(q)}` when `L(q)` is defined. Reverse holds if and only
if some lock in `S^+(A)` is the vector opposite of some lock in `S^+(B)`. Face
holds if and only if some lock in `S^+(C)` is the vector opposite of some
lock in `S^+(D)`. Empty `S^+` on either side of a comparison is `UNDEFINED`;
nonempty with no opposite pair fails. Occupancy `n` is not used. This is
not named-sign lettering. This is not a unique lock-vector leftover and not
a sum leftover. This is not leftover of same-tick-inclusive existential
opposite that excludes `q`: that display reports the same lock sets on these
z-probes because `L(A)` is `UNDEFINED` and `L(B)`, `L(C)`, and `L(D)` already
appear as neighbor locks. This is not leftover of strictly-earlier
own-lock-in: that display takes tick `< t(q)` union own lock and reports
`S^+(A)={+e_3}` with reverse fail and face hold. This is not leftover of
later-tick union own: that display waits for a global later T equal to the
max of the four formation ticks and reports five-lock sets at `B` and `D`.
This is not leftover of the unique own-incoming lock-vector letters on these
z-probes: that readout requires a singleton incoming step and reports reverse
`UNDEFINED` with face fail at mixed `A`. This is not leftover of
same-tick-inclusive union own on the four nnseed z-probes: that leftover
assigns `{+e_1, +e_3}` at `A` and `{+e_1, −e_2, +e_3}` at `D` and reports
reverse fail. This is not leftover of same-tick-inclusive union own on the
four nsopp z-probes: that leftover assigns `{+e_1, +e_3}` at `A` and reports
reverse fail. This is not leftover of y-axis opposite `±e_2` z-probe
same-tick union own: that leftover reports `S^+(A)={+e_2, +e_3}` and reverse
fail. This is not leftover of y-axis opposite ±e_3 z-probes: that leftover
uses seed `{0,(0,1,0)}` locking `+e_3/−e_3`; perp-step sees only the lock
axis, so the four z-probe `S^+` sets coincide with this display, while
y-probes split the two seeds (`fail`/`fail` here against `hold`/`fail`
there from `S^+(A)={+e_3, −e_3}`). This is not leftover of same-tick-inclusive
union own on the four y-axis same-lock `+e_3` y-probes: that leftover reports
reverse fail and face fail from seed `A=(0,1,0)` with `S^+(A)={+e_3}`. This
is not leftover of same-tick-inclusive union own on the four y-axis
same-lock `+e_3` x-probes: that leftover reports reverse fail and face hold.
This is not leftover of same-tick-inclusive union own on the four
y-axis opposite `±e_3` y-probes: that leftover reports `S^+(A)={+e_3, −e_3}`
at seed `A=(0,1,0)` and face fail. This is not leftover of same-tick-inclusive
union own on the four y-axis opposite `±e_3` x-probes: that leftover reports
reverse fail. Uniqueness of incoming locks is not required. Uniqueness of
the lock set is not required. `A` is not a seed. Displayed, not adopted.
This note does not write existential opposite into Admissibility and does
not attach a formation member from already-recorded six-neighbor locks.
**Audit-status authority:** independent audit lane only. This note authors no
audit verdict and predicts none.
**Primary runner:**
[`scripts/y_axis_same_lock_e3_zprobe_sametick_union_own_existential_opposite_reverse_face_2026_08_15.py`](../scripts/y_axis_same_lock_e3_zprobe_sametick_union_own_existential_opposite_reverse_face_2026_08_15.py)

Framework input:

- [`MINIMAL_AXIOMS_2026-06-29.md`](MINIMAL_AXIOMS_2026-06-29.md) supplies
  cubic-lattice sites `Z^3` with nearest-neighbor adjacency, the one-site
  algebra `M_2(C)`, and the Record sentences that records form and that a
  present record locks exactly one admissible local possibility.

Everything after that quoted input is a finite displayed process on `B_3(0)`
and the four named z-probes. Incoming lock letters are unit nearest-neighbor
steps. Reverse and face are scored on existence of an opposite pair in the
same-tick-inclusive six-neighbor lock sets union the probe's own incoming
lock when defined. Named signs `{+,−}` are a coarser readout and are not
used. A singleton unique lock-vector letter is a different readout and is
not used. A `Z^3` sum of those locks is a different readout and is not used.

## Machine status and trace

```yaml
actual_current_surface_status: bounded-support
target_claim_type: bounded_theorem
claim_type_reason: "Exact report of S^+ as same-tick-inclusive six-neighbor locks union L(q) when defined, on the four y-axis same-lock +e_3 z-probes at each probe's own t, no global T, with reverse hold by neighbor–neighbor because L(A) is UNDEFINED, reverse HOLD does not use L(A), and face hold from −e_1 against +e_1; uniqueness of incoming locks is not claimed and the bits are not adopted."
trace_class: frontier_discovery
target_claim_id: y_axis_same_lock_e3_zprobe_sametick_union_own_existential_opposite_reverse_face
target_blocker_text: "display reverse and face from same-tick ∪ own incoming lock on the four y-axis same-lock +e_3 z-probes, no global T, or UNDEFINED"
source_of_blocker_text: handoff
reachability_to_target: advances
artifact_role: theorem
next_trace_action: "Keep reverse and face displayed; do not write existential opposite into Admissibility, do not reduce to named sign, do not require a singleton lock vector, do not sum the lock set, do not use occupancy n, do not identify the sets with same-tick leftover that excludes q, do not identify the sets with strictly-earlier own-lock-in leftover, and do not identify the sets with later-tick union own leftover."
conditional_surface_status: "exact on B_3(0) for existential opposite of same-tick-inclusive six-neighbor locks union own incoming lock on the four y-axis same-lock +e_3 z-probes, no global T; displayed, not adopted"
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

No larger host is used. The four z-probes are the only sites whose
same-tick-inclusive union sets are scored:

```text
A = (0,0,1),  B = (1,1,1),  C = (0,0,2),  D = (1,0,1).
```

These are not the x-probes `A=(1,0,0)`, `B=(1,1,1)`, `C=(2,0,0)`,
`D=(1,1,0)`. These are not the y-probes `A=(0,1,0)`, `B=(1,1,1)`,
`C=(0,2,0)`, `D=(1,1,0)`. A is not a seed.

Lock alphabet of the displayed process: `{±e_i}` with `i` in `{1,2,3}`.

Seed: the two-record set `{0, (0,1,0)}` is recorded at formation tick 0 with
same locks `L(0)=+e_3` and `L(0,1,0)=+e_3`. Those locks are the same letter
and are perpendicular to the seed edge. This seed is not the y-axis opposite
`±e_3` seed `{0,(0,1,0)}` with locks `+e_3/−e_3`. This seed is not the y-axis
opposite `±e_2` seed `{0,(0,1,0)}` with locks `±e_2`. This seed is not the
nnseed two-site seed `+e_1/+e_2`. This seed is not the opposite two-site
seed `+e_1/−e_1`. This seed is not the same-lock two-site seed `+e_1/+e_1`.

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

Let `t(q)` be the formation tick of z-probe `q` when that tick is defined in
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
not sum `S^+(q)`. It is not a unique lock-vector leftover and not a sum leftover.
It is not leftover of same-tick-inclusive existential opposite that excludes `q`.
It is not leftover of strictly-earlier own-lock-in.
It is not leftover of later-tick union own.
It is not leftover of the unique own-incoming lock-vector letters on these
z-probes.
It is not leftover of same-tick-inclusive union own on the four nnseed
z-probes.
It is not leftover of same-tick-inclusive union own on the four nsopp
z-probes.
It is not leftover of y-axis opposite ±e_2.
It is not leftover of y-axis opposite ±e_3 z-probes.
It is not leftover of same-tick-inclusive union own on the four y-axis
same-lock `+e_3` y-probes.
It is not leftover of same-tick-inclusive union own on the four y-axis
same-lock `+e_3` x-probes.
It is not leftover of same-tick-inclusive union own on the four y-axis
opposite `±e_3` y-probes.
It is not leftover of same-tick-inclusive union own on the four y-axis
opposite `±e_3` x-probes.

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

## Theorem 1 — formation ticks, own incoming locks, and S^+ at each z-probe

Direct enumeration of the displayed y-axis same-lock `+e_3` process on
`B_3(0)` forms all four z-probes. The formation ticks are `t(A)=3`, `t(B)=2`,
`t(C)=4`, `t(D)=2`. A is not a seed. Those ticks locate the
same-tick-inclusive six-neighbor set. They are not occupancy kernels and are
not a global later T.

Own incoming locks and same-tick-inclusive union sets at each probe's own
formation tick are:

```text
A: +e_3 at (1, 0, 1), +e_3 at (-1, 0, 1), −e_1 at (0, 1, 1), −e_2 at (0, 1, 1),
   +e_1 at (0, 1, 1), +e_3 at (0, -1, 1), +e_3 at (0, 0, 0);
   incoming −e_1, +e_2, +e_1;
   t(A)=3;  L(A) = UNDEFINED;  S^+(A) = {+e_1, −e_1, −e_2, +e_3}
B: +e_3 at (1, 0, 1), +e_1 at (1, 1, 0); incoming +e_3;
   t(B)=2;  L(B) = +e_3;  S^+(B) = {+e_1, +e_3}
C: +e_3 at (0, 1, 2), −e_1 at (0, 0, 1), +e_2 at (0, 0, 1), +e_1 at (0, 0, 1);
   incoming +e_3;
   t(C)=4;  L(C) = +e_3;  S^+(C) = {+e_1, −e_1, +e_2, +e_3}
D: +e_3 at (1, 1, 1), +e_1 at (1, 0, 0); incoming +e_3;
   t(D)=2;  L(D) = +e_3;  S^+(D) = {+e_1, +e_3}
```

`A` forms at tick 3 by three earliest incoming steps `−e_1`, `+e_2`, and
`+e_1`. `L(A)` is `UNDEFINED`. Its same-tick neighbor `(0, 1, 1)` mixes
`−e_1`, `−e_2`, and `+e_1`. Earlier neighbors `(1, 0, 1)`, `(-1, 0, 1)`,
`(0, -1, 1)`, and the origin each lock `+e_3`. Reverse HOLD uses L(A): no.
The own–own channel is `UNDEFINED` because `L(A)` is `UNDEFINED`. The
own–neighbor channel that would read a unique `L(A)` against a lock at `B`
does not fire. Reverse holds by neighbor–neighbor: `−e_1` at same-tick
`(0, 1, 1)` is opposite `+e_1` in `S^+(B)`. `B` keeps the same-tick neighbor
`(1, 0, 1)` locking `+e_3` and the earlier neighbor `(1, 1, 0)` locking
`+e_1`; `L(B)=+e_3` already sits in that neighbor set, so
`S^+(B)={+e_1, +e_3}`. `C` keeps the same-tick neighbor `(0, 1, 2)` locking
`+e_3` and the earlier neighbor at `A` mixing `−e_1`, `+e_2`, and `+e_1`;
`L(C)=+e_3`, so `S^+(C)={+e_1, −e_1, +e_2, +e_3}`. `D` keeps the same-tick
neighbor `B` locking `+e_3` and the earlier neighbor `(1, 0, 0)` locking
`+e_1`; `L(D)=+e_3`, so `S^+(D)={+e_1, +e_3}`. Mixed remains a set at every
probe.

Incoming locks exist and need not be unique (`A` has three earliest incoming
steps `−e_1`, `+e_2`, and `+e_1`). That non-uniqueness leaves `L(A)`
`UNDEFINED` and does not empty `S^+(A)`. Uniqueness is not required. Mixed
earliest incoming steps are also kept wherever they occur, for example at
`(1,2,0)`.

The unique own-incoming letters on these same z-probes are `UNDEFINED`,
`+e_3`, `+e_3`, `+e_3`. Those are different objects: `S^+(A)` is nonempty,
and `S^+(B)` is not `{+e_3}`. Same-tick-inclusive leftover that excludes `q`
reports the same four lock sets on these z-probes because `L(A)` is
`UNDEFINED` and the other three letters already sit in the neighbor sets;
the letter is still the union. Strictly-earlier own-lock-in reports `{+e_3}`
at `A` without the same-tick mix at `(0, 1, 1)`. Later-tick union own
reports `{+e_1, −e_1, +e_2, −e_2, +e_3}` at `B` and at `D` after waiting for
a global later T. Same-tick-inclusive union own on the four nnseed z-probes
reports `{+e_1, +e_3}` at `A` and `{+e_1, −e_2, +e_3}` at `D`. Same-tick-
inclusive union own on the four nsopp z-probes reports `{+e_1, +e_3}` at
`A`. Y-axis opposite `±e_2` z-probe same-tick union own reports
`{+e_2, +e_3}` at `A`. Y-axis opposite `±e_3` z-probes report the same four
`S^+` sets because perp-step sees only the lock axis; the seed letter at
`(0,1,0)` is `−e_3` there and `+e_3` here. Same-tick-inclusive union own on
the four y-axis same-lock `+e_3` y-probes reports `{+e_3}` at seed
`A=(0,1,0)` with reverse fail and face fail. Same-tick-inclusive union own
on the four y-axis same-lock `+e_3` x-probes reports reverse fail and face
hold. Same-tick-inclusive union own on the four y-axis
opposite `±e_3` y-probes reports `{+e_3, −e_3}` at seed `A=(0,1,0)`.

## Theorem 2 — reverse hold / fail / UNDEFINED

Reverse holds if and only if there exist `a` in `S^+(A)` and `b` in
`S^+(B)` with `a+b=(0,0,0)`. Both sets are nonempty:
`S^+(A)={+e_1, −e_1, −e_2, +e_3}` and `S^+(B)={+e_1, +e_3}`, so
`−e_1+(+e_1)=(0,0,0)`. Reverse holds.

Reverse: hold

Reverse holds. Reverse HOLD uses L(A): no. Reverse holds by
neighbor–neighbor. The own–own channel is `UNDEFINED` because `L(A)` is
`UNDEFINED`. The own–neighbor channel does not fire. Same-tick leftover
that excludes `q` leaves the same `S(A)` and also reports reverse hold
because `L(A)` adds no letter. Strictly-earlier own-lock-in reports
`{+e_3}` at `A` and reverse fail. Later-tick union own waits for a global
later T and then reports reverse hold from a five-lock set at `B`. Unique
own-incoming letters on these z-probes report reverse `UNDEFINED` from
mixed `A`.

This is not `fail` and not `UNDEFINED`. This is not leftover of
same-tick-inclusive existential opposite that excludes `q`: that leftover
coincides on these z-probes only because `L(A)` is `UNDEFINED`. Unique
lock-vector lettering of the same union sets would report reverse
`UNDEFINED` because both sides mix. A sum leftover of the same lists would
replace `S^+(A)` by `(0,-1,1)` and `S^+(B)` by `(1,0,1)` and would fail
reverse; that leftover is a different object because existential opposite
holds reverse. Unique own-incoming letters on these z-probes report reverse
`UNDEFINED` from mixed `A`. Opposite-lock nnseed and nsopp z-probe
same-tick union own report reverse fail from `{+e_1, +e_3}` at `A`. Y-axis
opposite `±e_2` z-probes report reverse fail from `{+e_2, +e_3}` at `A`.
Y-axis opposite `±e_3` z-probes report reverse hold from the same `S^+`
sets; that leftover is a different seed (`+e_3/−e_3` at `(0,1,0)`). Y-axis
same-lock `+e_3` y-probes report reverse fail. Y-axis same-lock `+e_3`
x-probes report reverse fail. Y-axis opposite `±e_3` x-probes report reverse
fail. Reverse holds because `−e_1` at `A` is opposite `+e_1` at `B`.

Reverse holds.

## Theorem 3 — face hold / fail / UNDEFINED

Face holds if and only if there exist `c` in `S^+(C)` and `d` in `S^+(D)`
with `c+d=(0,0,0)`. Both sets are nonempty:
`S^+(C)={+e_1, −e_1, +e_2, +e_3}` and `S^+(D)={+e_1, +e_3}`. The pair
`−e_1+(+e_1)=(0,0,0)` is opposite. Face holds.

Face: hold

Displayed, not adopted. The bits are not written into Admissibility.

This is not `fail` and not `UNDEFINED`. Face holds. Unique own-incoming
letters on these same z-probes assign `L(C)=+e_3` and `L(D)=+e_3` and
report face fail from singleton `+e_3` against `+e_3`. Unique lock-vector
lettering of the union sets would report face `UNDEFINED` because `C` and
`D` mix. A sum leftover would replace `S^+(C)` by `(0,1,1)` and `S^+(D)` by
`(1,0,1)` and would fail face; that leftover is a different object because
existential opposite holds face. Named-sign lettering lost the axis in mixed
`{+,−}` at `A` and `C`. Same-tick leftover that excludes `q` already holds
face as the same pair `−e_1` against `+e_1`. Strictly-earlier own-lock-in
also holds face from the earlier mix at `A` union `L(C)=+e_3`. Later-tick
union own reports face hold after a global later T on a later five-lock set
at `D`. Y-axis opposite `±e_3` z-probes report face hold from the same
`S^+` sets; that leftover is a different seed. Y-axis same-lock `+e_3`
y-probes report face fail. Y-axis same-lock `+e_3` x-probes report face
hold from a different `S^+(C)` and `S^+(D)`. Y-axis opposite `±e_3` y-probes
report face fail. Face already holds
at each probe's own formation tick with same-tick partners included and own
lock unioned; it does not wait for a global later T.

Face holds.

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
  z-probes.
- It does not reprint same-tick-inclusive existential opposite that excludes
  `q`.
- It does not reprint strictly-earlier own-lock-in.
- It does not reprint later-tick union own.
- It does not wait for a global later T.
- It does not reprint same-tick-inclusive union own on the four nnseed
  z-probes.
- It does not reprint same-tick-inclusive union own on the four nsopp
  z-probes.
- It does not reprint y-axis opposite `±e_2` z-probe same-tick union own.
- It does not reprint y-axis opposite `±e_3` z-probe same-tick union own.
- It does not reprint same-tick-inclusive union own on the four y-axis
  same-lock `+e_3` y-probes.
- It does not reprint same-tick-inclusive union own on the four y-axis
  same-lock `+e_3` x-probes.
- It does not reprint same-tick-inclusive union own on the four y-axis
  opposite `±e_3` y-probes.
- It does not reprint same-tick-inclusive union own on the four y-axis
  opposite `±e_3` x-probes.
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
y-axis same-lock `+e_3` process, the same-tick-inclusive union sets, and the
existential-opposite reverse/face predicates are displayed theorem-domain
data.

## Exact target and obligation graph

| Obligation | Status |
|---|---|
| current Lattice / Admissibility / Record premises | quoted; no edit |
| perp-step incoming-lock process on `B_3(0)` | displayed; y-axis same-lock two-site seed `+e_3/+e_3` |
| ticks `t(A)`, `t(B)`, `t(C)`, `t(D)` | Theorem 1; `3`, `2`, `4`, `2` |
| own incoming locks `L(A)`, `L(B)`, `L(C)`, `L(D)` | Theorem 1; `UNDEFINED`, `+e_3`, `+e_3`, `+e_3` |
| lock sets `S^+(A)`, `S^+(B)`, `S^+(C)`, `S^+(D)` | Theorem 1; `{+e_1, −e_1, −e_2, +e_3}`, `{+e_1, +e_3}`, `{+e_1, −e_1, +e_2, +e_3}`, `{+e_1, +e_3}` |
| reverse HOLD uses `L(A)` | Theorem 1; no; neighbor–neighbor; own–own `UNDEFINED` |
| reverse and face | Theorems 2–3; `hold` / `hold` |
| unique incoming lock | not required |
| occupancy `n` as the letter | not used |
| named-sign `{+,−}` letter | not used; lost the axis |
| singleton unique lock-vector letter | not used; mixed remains a set |
| `Z^3` sum of the lock set | not used; no aggregation |
| occupancy-kernel inner product | not used |
| formation member from already-recorded six-neighbor locks | not attached |
| leftover of unique own-incoming letters on these z-probes | not this display |
| leftover of same-tick-inclusive existential opposite that excludes `q` | not this display |
| leftover of strictly-earlier own-lock-in | not this display |
| leftover of later-tick union own | not this display |
| leftover of same-tick-inclusive union own on the four nnseed z-probes | not this display |
| leftover of same-tick-inclusive union own on the four nsopp z-probes | not this display |
| leftover of y-axis opposite `±e_2` | not this display |
| leftover of y-axis opposite `±e_3` z-probes | not this display |
| leftover of y-axis same-lock `+e_3` y-probe same-tick-inclusive union own | not this display |
| leftover of y-axis same-lock `+e_3` x-probe same-tick-inclusive union own | not this display |
| leftover of y-axis opposite `±e_3` y-probe same-tick-inclusive union own | not this display |
| leftover of y-axis opposite `±e_3` x-probe same-tick-inclusive union own | not this display |
| leftover of same-lock two-site seed `+e_1/+e_1` | not this display |
| existential opposite as Admissibility content | not adopted |
| formation site / probability / rate | open |
| physical Record readout of the bits | open |

## Promotion value gate (V1–V5)

| # | Answer |
|---|---|
| V1 | It answers the first-display question: same-tick ∪ own incoming lock on the four y-axis same-lock `+e_3` z-probes, no global T, reverse/face or `UNDEFINED`. |
| V2 | Current main has no landed same-tick-inclusive union-own-lock existential-opposite reverse/face report on these four y-axis same-lock `+e_3` z-probes. |
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
| unique lock-vector lettering of the same union sets | require a singleton `{v}` subset `{±e_i}` | refused; leftover; reverse and face would be `UNDEFINED` while the mixed union sets are nonempty, reverse holds, and face holds |
| sum of the same union sets | replace `S^+` by the `Z^3` sum | refused; leftover; sum of `S^+(A)` is `(0,-1,1)` and sum of `S^+(B)` is `(1,0,1)`; sum of `S^+(C)` is `(0,1,1)` and sum of `S^+(D)` is `(1,0,1)`; those sums fail reverse and fail face, while existential opposite holds both |
| named-sign lettering of the same union sets | map `±e_i` to `{+,−}` | refused; lost the axis; mixed `{+,−}` at `A` and `C` would hide `−e_1+(+e_1)=0` |
| unique own-incoming lock-vector leftover on these z-probes | reuse `L(A)=UNDEFINED`, `L(B)=+e_3`, `L(C)=+e_3`, `L(D)=+e_3` | refused; different object; that leftover reports reverse `UNDEFINED` and face fail while the mixed union sets hold reverse and hold face |
| leftover of same-tick-inclusive existential opposite that excludes `q` | reuse neighbor locks without `{L(q)}` | refused; different letter; the sets coincide on these z-probes only because `L(A)` is `UNDEFINED` and the other letters already appear as neighbor locks |
| leftover of strictly-earlier own-lock-in | reuse tick `< t(q)` union own lock with `S^+(A)={+e_3}` | refused; different set; this display keeps the same-tick mix at `(0, 1, 1)`, so reverse holds |
| leftover of later-tick union own | reuse global later T and five-lock sets at `B` and `D` | refused; different sets; this display does not wait for a global later T |
| leftover of same-tick-inclusive union own on the four nnseed z-probes | reuse nnseed `+e_1/+e_2` with `{+e_1, +e_3}` at `A` and `−e_2` at `D` | refused; different process; this `A` includes `−e_1` and this `D` omits `−e_2`; nnseed reverse fails |
| leftover of same-tick-inclusive union own on the four nsopp z-probes | reuse opposite seed `+e_1/−e_1` with `{+e_1, +e_3}` at `A` | refused; different process; this `A` includes `−e_1` and nsopp reverse fails |
| leftover of y-axis opposite ±e_2 | reuse seed `{0,(0,1,0)}` with locks `±e_2` and z-probes | refused; different process; that leftover reports `S^+(A)={+e_2, +e_3}` and reverse fail |
| leftover of y-axis opposite `±e_3` z-probes | reuse seed `{0,(0,1,0)}` with locks `+e_3/−e_3` on these z-probes | refused; different seed; z-probe `S^+` coincide because perp-step sees only the lock axis; y-probes split `fail`/`fail` here against `hold`/`fail` there |
| leftover of y-axis same-lock `+e_3` y-probe same-tick-inclusive union own | reuse y-probes with `S^+(A)={+e_3}` at seed `A=(0,1,0)` | refused; different frame; z-probe `A` is `(0,0,1)` with `L(A)` `UNDEFINED`; that leftover reports reverse fail and face fail |
| leftover of y-axis same-lock `+e_3` x-probe same-tick-inclusive union own | reuse x-probes with reverse fail and face hold | refused; different frame; z-probe reverse holds |
| leftover of y-axis opposite `±e_3` y-probe same-tick-inclusive union own | reuse y-probes with `S^+(A)={+e_3, −e_3}` at seed `A=(0,1,0)` | refused; different seed and frame; z-probe `A` is `(0,0,1)` with `L(A)` `UNDEFINED`; that leftover reports face fail |
| leftover of y-axis opposite `±e_3` x-probe same-tick-inclusive union own | reuse opposite-seed x-probes with reverse fail and face hold from `−e_3` at `D` | refused; different seed and frame; z-probe reverse holds |
| unique letter of occupancy `n` | assign one letter from occupancy `n` | different object; occupancy `n` is not used |
| occupancy-kernel inner product | score `n(A)·n(B)<0` and `n(C)·n(D)<0` | different object; not an occupancy-kernel inner product |
| reverse/face from formation-tick inequalities | score probes by formation order | different object; ticks locate `S^+` and are not the predicate |
| attach a formation member from already-recorded six-neighbor locks | form the probes by a neighbor-lock letter instead of perp-step | refused; not attached |
| adopt bits into Admissibility | rewrite the local rule by existential opposite | refused; displayed, not adopted |
| unique incoming lock required | demand one incoming step per probe | uniqueness is not required; three earliest incoming steps at `A` are kept and `L(A)` is `UNDEFINED` |

### N2 — wall independence

Missing physical adoption, missing formation attachment from already-recorded
six-neighbor locks, and missing Record identification of existential opposite
are distinct open premises. This note claims no complete wall collection.

### N3 — hidden-condition scan

The host `B_3(0)`, two-site seed locks `+e_3` and `+e_3` perpendicular to the
seed edge, perpendicular step rule, incoming-step lock, same-tick-inclusive
lock set of six-neighbors formed at tick `<=` each probe's own `t` with the
probe excluded, union with `L(q)` when defined, existential opposite, four
z-probes, and reverse/face as existence of a pair that sums to zero are
declared. No uniqueness of incoming locks, no occupancy `n`, no named-sign
reduction, no singleton leftover, no sum leftover, no unique own-incoming
leftover, no same-tick exclude-`q` leftover, no strictly-earlier own-lock-in
leftover, no later-tick leftover, no global later T, no formation attachment
from already-recorded six-neighbor locks, and no Admissibility rewrite are
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
| per site | `A,B,C,D` z-probes on `B_3(0)` only | no other cubic sites |
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
own-incoming letters already answered reverse `UNDEFINED` with face fail,
same-tick-inclusive existential opposite already answered the
exist-opposite question because the sets coincide, strictly-earlier
own-lock-in already answered the union question without same-tick partners,
later-tick union own already answered the union question after a global T
with hold/hold, nnseed and nsopp z-probe same-tick union own already
answered with fail/hold, y-axis opposite `±e_2` already answered reverse
fail with face hold on these z-probes, y-axis opposite `±e_3` z-probes
already answered hold/hold because the z-probe `S^+` coincide, y-axis
same-lock `+e_3` y-probes already answered fail/fail on a seed, y-axis
same-lock `+e_3` x-probes already answered fail/hold, named signs should
suffice because they keep orientation, occupancy `n` should track that
vector, and reverse HOLD uses `L(A)`.

**Answer:** The named construction reports lock sets `{+e_1, −e_1, −e_2, +e_3}`,
`{+e_1, +e_3}`, `{+e_1, −e_1, +e_2, +e_3}`, `{+e_1, +e_3}` at `A,B,C,D` from
same-tick-inclusive six-neighbor locks union `{L(q)}` when defined. Mixed
remains a set. The construction does not sum. Occupancy `n` is not used.
Named signs lost the axis. Some pair from `S^+(A)` and `S^+(B)` is
opposite, so reverse holds. Reverse HOLD does not use L(A): `L(A)` is
`UNDEFINED`, own–own is `UNDEFINED`, and reverse holds by
neighbor–neighbor from `−e_1` against `+e_1`. A pair from `S^+(C)` and
`S^+(D)` is opposite, so face holds. Same-tick leftover that excludes `q`
coincides on these z-probes only because `L(A)` is `UNDEFINED` and
`L(B)`, `L(C)`, `L(D)` already appear as neighbor locks; the letter is
still the union. Strictly-earlier own-lock-in reports `{+e_3}` at `A` and
fails reverse. Later-tick leftover waits for a global later T and then
reports five-lock sets at `B` and `D`. Unique own-incoming leftover reports
reverse `UNDEFINED` and face fail. Nnseed and nsopp z-probe leftovers
assign `{+e_1, +e_3}` at `A` and fail reverse. Y-axis opposite `±e_2`
assigns `{+e_2, +e_3}` at `A` and fails reverse. Y-axis opposite `±e_3`
z-probes coincide on these four `S^+` sets because perp-step sees only the
lock axis; that leftover is a different seed (`L(0,1,0)=−e_3`). Y-probe
leftover on this same-lock seed reports `{+e_3}` at seed `A=(0,1,0)` and
fails reverse and face. X-probe leftover on this seed reports reverse fail
and face hold. Opposite-seed y-probe leftover reports `{+e_3, −e_3}` at
seed `A=(0,1,0)` and fails face. The sets are not those leftovers. The bits
remain displayed. Incoming-lock uniqueness is not required.

### N8 — cross-cycle echo

A unique own-incoming lock-vector display on these same y-axis same-lock
`+e_3` z-probes would assign `L(A)=UNDEFINED`, `L(B)=+e_3`, `L(C)=+e_3`,
`L(D)=+e_3` and report reverse `UNDEFINED` with face fail from mixed `A`. A
same-tick-inclusive existential opposite display that excludes `q` assigned
the same four lock sets because `L(A)` is `UNDEFINED`. Strictly-earlier
own-lock-in assigned `{+e_3}`, `{+e_1, +e_3}`, `{+e_1, −e_1, +e_2, +e_3}`,
`{+e_1, +e_3}` and reported reverse fail with face hold. Later-tick union
own reported reverse hold and face hold on different later sets
`{+e_1, −e_1, +e_2, −e_2, +e_3}` at `B` and at `D` after a global later T.
Same-tick-inclusive union own on the four nnseed z-probes reported reverse
fail and face hold with `{+e_1, +e_3}` at `A` and `{+e_1, −e_2, +e_3}` at
`D`. Y-axis opposite `±e_2` z-probe same-tick union own reported reverse
fail and face hold from `{+e_2, +e_3}` at `A`. Y-axis opposite `±e_3`
z-probe same-tick union own reported reverse hold and face hold from the
same four `S^+` sets on a different seed. Y-axis same-lock `+e_3` y-probe
same-tick union own reported reverse fail and face fail from `{+e_3}` at
seed `A`. Y-axis same-lock `+e_3` x-probe same-tick union own reported
reverse fail and face hold. Y-axis opposite `±e_3`
y-probe same-tick union own reported reverse hold and face fail from
`{+e_3, −e_3}` at seed `A`. Unique lock-vector lettering of the union sets
would report reverse `UNDEFINED` and face `UNDEFINED` because every union
set mixes. A sum leftover of the same lists would report reverse fail and
face fail because the sums are `(0,-1,1)` with `(1,0,1)` and `(0,1,1)` with
`(1,0,1)`. This note is not those displays: mixed remains a set, the
construction does not sum, `S^+(A)` includes the same-tick mix at
`(0, 1, 1)`, reverse HOLD does not use `L(A)`, reverse holds because
`−e_1+(+e_1)=(0,0,0)`, and face holds because `S^+(C)` and `S^+(D)` share
that opposite pair.

**Gate disposition:** PASS for the same-tick-inclusive six-neighbor-lock union
own incoming existential-opposite reverse/face reports above. FAIL / DO NOT SHIP
for “the predicate equals the named sign,” “the predicate equals the unique
singleton lock vector,” “the predicate equals the sum of the lock set,”
“bits are Admissibility,” “the letter is occupancy `n`,” “the sets equal
unique own-incoming letters,” “the sets equal same-tick leftover that
excludes `q`,” “the sets equal strictly-earlier own-lock-in,” “the sets
equal later-tick union own,” “reverse is `fail`,” “reverse HOLD uses
`L(A)`,” or “face is `fail`.”

## Primary runner

The paired runner builds Euclidean `B_3(0)`, runs the y-axis same-lock
two-site perp-step incoming-lock process, reads each probe's own unique
incoming lock or `UNDEFINED`, collects six-neighbor locks formed at tick
`<=` each probe's own formation tick with the probe excluded, unions those
locks with `{L(q)}` when defined, reads the union sets at the four z-probes,
reports whether reverse HOLD uses `L(A)`, and checks Theorems 1--3. It also
checks that the construction is not named-sign lettering, that mixed sets
remain defined, that the construction does not sum, that occupancy `n` is
not used, that a formation member from already-recorded six-neighbor locks
is not attached, that the sets are not leftover of unique own-incoming
letters, that the sets are not leftover of same-tick-inclusive existential
opposite that excludes `q`, that the sets are not leftover of
strictly-earlier own-lock-in, and that the sets are not leftover of
later-tick union own. No runner cache is written.
